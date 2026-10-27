#!/usr/bin/env python3
"""Read-only scratch/integrated validator. Current copy-manifest is authoritative."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

NAME = "Roth.wronskian_ne_zero_of_linearIndependent"
HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()

def read(name):
    return json.loads((HERE / name).read_text())

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def nodes(value):
    yield value
    if isinstance(value, dict):
        for val in value.values():
            yield from nodes(val)
    elif isinstance(value, list):
        for val in value:
            yield from nodes(val)

a = read("assessment.json")
assert a["declaration"] == NAME and a["completed"] is True
assert a["allphases"] == "PASS" and a["unresolved"] == []
assert a["root_acceptance"] in ("pending", "PASS")
phases = ["0","1","2","3","4a","4b","4c","4.5","4.6","5","5.5","6.0","6","7","8"]
assert all(a["phases"][phase] == "PASS" for phase in phases)

# Never substitute worker-copy-manifest.json for this current manifest.
m = read("copy-manifest.json")
seen = set()
for item in m["files"]:
    dest = Path(item["destination"])
    if "/mathlibable/" in item["destination"]:
        path = HERE / "report.md" if (HERE / "report.md").exists() else ROOT / dest
    else:
        path = HERE / dest.name
    assert path.is_file(), path
    assert digest(path) == item["sha256"] and path.stat().st_size == item["bytes"], path
    seen.add(dest.name)
assert {"assessment.json","verification.json","overview-entry.json","validate.py",NAME+".md"} <= seen

v = read("verification.json")
assert v["unresolved"] == []
allowed = {"propext","Classical.choice","Quot.sound"}
assert set(v["standard_axioms"]) == allowed
assert {x["experiment"] for x in v["accepted"]} == {"target","domain","guards","callers"}
for item in v["accepted"]:
    source = HERE / item["source"]
    assert digest(source) == item["source_sha256"]
    text = source.read_text()
    assert not re.search(r"\b(?:sorry|admit|native_decide|unsafe)\b|\baxiom\s|set_option\s+(?:maxHeartbeats|maxRecDepth)", text)
    r = read(item["receipt"])
    assert not r["result"].get("isError",False)
    payloads = [n for n in nodes(r["result"]) if isinstance(n,dict) and n.get("success") is True]
    assert payloads, item
    for payload in payloads:
        assert payload.get("partial",False) is False
        assert payload.get("timed_out",False) is False
        assert not payload.get("failed_dependencies")
        diagnostics = payload.get("diagnostics",payload.get("items",[]))
        assert not [d for d in diagnostics if d.get("severity") in ("error","warning") or d.get("category") == "sorry"]
        axioms = re.findall(r"depends on axioms: \[([^]]*)\]","\n".join(d.get("message","") for d in diagnostics))
        assert axioms
        for ax in axioms:
            assert {x.strip() for x in ax.split(",") if x.strip()} <= allowed
    if item["label"] == "isolated":
        assert r["request"]["code"] == text
        assert not re.search(r"^import Roth\b",text,re.M)
        assert "#check_failure "+NAME in text
for rejected in v["rejected"]:
    assert (HERE / rejected).exists()
inputs = read(v["inputs"])
assert len(inputs) == 17
for item in inputs + read(v["mathlib_inputs"]):
    f = ROOT / item["path"]
    assert digest(f) == item["sha256"] and f.stat().st_size == item["bytes"], f
for original, archived in v["source_links"].items():
    assert digest(ROOT / original) == digest(HERE / archived)
assert read("input-hash-check.json")["all_pass"] is True
report = HERE / "report.md"
if not report.exists():
    report = ROOT / ".mathlib-quality/overview/mathlibable" / (NAME+".md")
t = report.read_text()
prefix = "../evidence/"+NAME+"/"
for target in re.findall(r"\]\(([^)]+)\)",t):
    if target.startswith("https://"):
        continue
    assert target.startswith(prefix),target
    assert (HERE / target[len(prefix):]).exists(),target
assert "## Phase 8" in t
assert read("overview-entry.json")["type"].startswith("∀")
for method in ["finder","loogle","leansearch","local"]:
    for form in ["current","standard","abstract","domain"]:
        r = read("formal-"+method+"-"+form+".json")
        assert "request" in r and "result" in r
        assert not r["result"].get("isError",False)
for form in ["current","standard","abstract"]:
    assert (HERE / ("rg-"+form+".json")).exists()
web = [read(f.name) for f in HERE.glob("web-*.json")]
queries = [q["q"] for w in web for q in w["request"].get("search_query",[])]
assert len(set(queries)) >= 10
for domain in ["site:ncatlab.org/nlab","site:ncatlab.org ","site:stacks.math.columbia.edu","site:mathoverflow.net","site:arxiv.org"]:
    assert any(domain in q for q in queries),domain
for w in web:
    assert len(w["response_sha256"]) == 64 and w["response_bytes"] > 0
    assert "response" not in w
assert read("canonical-entry.json")["name"] == NAME
assert {x["declaration"] for x in read("accepted-grouping.json")} == {"Roth.det_choose_eq","Roth.coeff_wronskian_of_natDegree_injective","Roth.wronskian_ne_zero_of_natDegree_injective"}
subprocess.run([sys.executable,str(ROOT/".mathlib-quality/overview/evidence/shared/scan_evidence_secrets.py"),str(HERE)],check=True)
print("PASS: current manifest, 15 phases, native complete success/standard axioms, 17 source/pin hashes, exact receipts, links and credentials")

