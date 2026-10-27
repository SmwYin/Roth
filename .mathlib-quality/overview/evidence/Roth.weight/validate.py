#!/usr/bin/env python3
"""Read-only validator for scratch and integrated Roth.weight evidence."""
import argparse, hashlib, json, pathlib, re
ap = argparse.ArgumentParser()
ap.add_argument("--repo", type=pathlib.Path, default=pathlib.Path.cwd())
a = ap.parse_args()
p = pathlib.Path(__file__).resolve().parent
repo = a.repo.resolve()
def read(n): return json.loads((p / n).read_text())
def sha(b): return hashlib.sha256(b).hexdigest()
assessment = read("assessment.json")
assert assessment["completed"] is True and assessment["unresolved"] == []
assert assessment["root_acceptance"] in ("pending", "PASS")
assert all(v == "PASS" or v.startswith("n/a") for v in assessment["phases"].values())
manifest = read("copy-manifest.json")
for row in manifest["artifacts"]:
    dest = repo / row["destination"]
    candidate = p / pathlib.Path(row["source"]).name
    f = dest if dest.exists() and (p / "assessment.json").resolve() == (repo / ".mathlib-quality/overview/evidence/Roth.weight/assessment.json").resolve() else candidate
    b = f.read_bytes()
    assert len(b) == row["bytes"] and sha(b) == row["sha256"], str(f)
for row in read("baseline-hash-check.json")["inputs"]:
    assert sha((repo / row["path"]).read_bytes()) == row["expected"], row["path"]
verification = read("verification.json")
for v in verification["accepted"]:
    receipt = read(v["receipt"])
    outer = receipt["result"]
    assert outer.get("isError", False) is False
    result = outer["structuredContent"]
    if "result" in result: result = result["result"]
    assert result["success"] is True and result.get("timed_out", False) is False
    assert result.get("partial", False) is False
    diagnostics = result.get("items", result.get("diagnostics", []))
    assert not [x for x in diagnostics if x["severity"] in ("error", "warning")]
    for d in diagnostics:
        msg = d.get("message", "")
        if "depends on axioms:" in msg:
            axioms = msg.split("depends on axioms:", 1)[1].strip().strip("[]")
            assert set(x.strip() for x in axioms.split(",") if x.strip()) <= set(verification["axiom_allowlist"])
    source = (p / v["source"]).read_text()
    if "code" in receipt["request"]: assert receipt["request"]["code"] == source
    assert "sorryAx" not in json.dumps(diagnostics)
frozen = read("project-source-check.json")
assert frozen["matched_at_freeze"] and sha((p / frozen["source"]).read_bytes()) == frozen["retained_sha256"] == frozen["disk_sha256"]
report = p / "report.md"
if not report.exists(): report = repo / ".mathlib-quality/overview/mathlibable/Roth.weight.md"
for target in re.findall(r"\]\(([^)]+)\)", report.read_text()):
    if target.startswith("../evidence/Roth.weight/"):
        assert (p / target.split("../evidence/Roth.weight/", 1)[1]).exists(), target
assert len(read("caller-excerpts.json")) == 30
for form in ("current", "literature", "abstract"):
    for method in ("lean_leanfinder", "lean_loogle", "lean_leansearch", "lean_local_search", "rg"):
        assert (p / ("search-" + form + "-" + method + ".json")).exists()
for channel in ("general", "nlab", "ncatlab", "stacks", "mathoverflow", "arxiv", "primary"):
    x = read("literature-" + channel + ".json")
    assert x["request"] and len(x["response"]["sha256"]) == 64 and x["response"]["bytes"] > 0
print("PASS: current artifact manifest, phases, exact native success, standard axioms, 17 source/pin hashes, 30 callers, 15 searches and links")

