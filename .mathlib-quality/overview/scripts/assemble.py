#!/usr/bin/env python3
"""Validate per-declaration /overview reports and regenerate the aggregate files.

Usage:
  assemble.py check <Decl.Name>   # validate one report; exit 1 on defects
  assemble.py build               # regenerate PROJECT_OVERVIEW.md and PROGRESS.md

A declaration counts as completed only when its report under `mathlibable/`
passes `check`.  Completion is contiguous in `decls.tsv` order: the next
declaration is the first one whose report is missing or fails validation.
"""
import collections, datetime, pathlib, re, sys

OV = pathlib.Path(__file__).resolve().parents[1]
ROOT = OV.parents[1]
REPORTS = OV / "mathlibable"
SYNTH = OV / "synthesis.md"

BUCKETS = ["YES-add-as-is", "YES-but-generalise-first", "NO-mathlib-has-it",
           "NO-composable-from-mathlib", "BORDERLINE-needs-human"]
META_KEYS = ["decl", "file", "line", "kind", "visibility", "verdict", "cost",
             "junk", "rationale", "action"]
INVENTORY_FIELDS = ["Type", "What", "How", "Hypotheses", "Uses from project", "Used by",
                    "Visibility", "Lines", "Notes"]
FULL_RUN_HEADINGS = ["Baseline (Phase 0)", "Statement (Phase 1)", "Size classification",
                     "One-line check", "Literature search table", "Literature summary",
                     "Generality verdict", "Modern-idiom verdict", "Proof strategy verdict",
                     "Mathlib search-status", "Statement-shape verdict", "Call sites",
                     "Composition check", "Verdict:"]
DEF_KINDS = {"def", "abbrev", "structure", "class", "instance", "inductive"}


def decls():
    rows = []
    for line in (OV / "decls.tsv").read_text().splitlines():
        idx, name, kind, vis, f, ln = line.split("\t")
        rows.append(dict(idx=int(idx), decl=name, kind=kind, visibility=vis, file=f, line=int(ln)))
    return rows


def report_path(name):
    return REPORTS / f"{name}.md"


def parse(path):
    text = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        return None, text
    meta = {}
    for ln in m.group(1).splitlines():
        if ":" in ln:
            k, v = ln.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def section(body, title):
    m = re.search(rf"^## {re.escape(title)}\s*\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1) if m else None


def check(row):
    p = report_path(row["decl"])
    if not p.exists():
        return ["report missing"]
    meta, body = parse(p)
    if meta is None:
        return ["front matter missing"]
    errs = [f"meta `{k}` missing/empty" for k in META_KEYS if not meta.get(k)]
    if meta.get("decl") != row["decl"]:
        errs.append(f"meta decl {meta.get('decl')!r} != {row['decl']!r}")
    v = meta.get("verdict", "")
    ok_verdict = (v in BUCKETS or v == "SKIP"
                  or any(v == f"INHERITED-{b}" for b in BUCKETS))
    if not ok_verdict:
        errs.append(f"bad verdict {v!r}")
    if row["visibility"] == "private" and v != "SKIP":
        errs.append("private declaration must be SKIP")
    inv = section(body, "Inventory entry")
    if inv is None:
        errs.append("missing `## Inventory entry`")
    else:
        for fld in INVENTORY_FIELDS:
            fm = re.search(rf"^- \*\*{re.escape(fld)}\*\*:\s*(.+)$", inv, re.M)
            if not fm or not fm.group(1).strip():
                errs.append(f"inventory field `{fld}` missing/empty")
    if section(body, "Junk check (Step 8)") is None:
        errs.append("missing `## Junk check (Step 8)`")
    ma = section(body, "Mathlibable assessment (Step 9)")
    if ma is None:
        errs.append("missing `## Mathlibable assessment (Step 9)`")
    elif v in BUCKETS:
        for h in FULL_RUN_HEADINGS:
            if h not in ma:
                errs.append(f"full run lacks artifact `{h}`")
        if row["kind"] in DEF_KINDS and "Risk verdict" not in ma:
            errs.append("def-like declaration lacks `Risk verdict (Phase 4.5)`")
        if v == "BORDERLINE-needs-human" and not re.search(r"^\s*1\.", ma, re.M):
            errs.append("BORDERLINE without numbered questions")
    elif v.startswith("INHERITED-") and "Inherited from" not in ma:
        errs.append("INHERITED verdict must cite `Inherited from`")
    elif v == "SKIP" and "Skip reason" not in ma:
        errs.append("SKIP verdict must state `Skip reason`")
    if section(body, "Evidence") is None:
        errs.append("missing `## Evidence`")
    return errs


def completed(rows):
    done = []
    for r in rows:
        if check(r):
            break
        done.append(r)
    return done


def build():
    rows = decls()
    done = completed(rows)
    nxt = rows[len(done)] if len(done) < len(rows) else None
    synth_done = SYNTH.exists() and "STATUS: COMPLETE" in SYNTH.read_text()
    metas = {r["decl"]: parse(report_path(r["decl"])) for r in done}
    counts = collections.Counter()
    for r in done:
        v = metas[r["decl"]][0]["verdict"]
        counts["INHERITED" if v.startswith("INHERITED-") else v] += 1
    today = datetime.date.today().isoformat()
    n_pub = sum(r["visibility"] == "public" for r in rows)
    kinds = collections.Counter(r["kind"] for r in rows)

    # ---------------- PROGRESS.md ----------------
    pg = [f"# /overview progress record", "",
          "Run: `mathlib-quality:overview` on the whole repository, including Step 9 (full",
          "`/mathlibable` per non-skipped public declaration).  Branch `ramin-cleanup-2`.",
          "Production Lean sources are not modified; experiments live under",
          "`.mathlib-quality/overview/evidence/`.", "",
          "Restart protocol: read this file, then continue with **Next declaration**.  A",
          "declaration is complete only when its report passes",
          "`python3 .mathlib-quality/overview/scripts/assemble.py check <Decl>`.", "",
          f"Last regenerated: {today}", "",
          f"- Declarations completed: **{len(done)}/{len(rows)}**",
          f"- Next declaration: " + (f"**#{nxt['idx']} `{nxt['decl']}`** ({nxt['file']}:{nxt['line']})"
                                    if nxt else "none — all declarations complete"),
          f"- Project-wide synthesis (Steps 3–8 cross-declaration analyses): "
          + ("complete" if synth_done else "pending (runs after the last declaration)"),
          "", "## Completed declarations", "",
          "| # | Declaration | File:line | Verdict | Report |", "|---|---|---|---|---|"]
    for r in done:
        m = metas[r["decl"]][0]
        pg.append(f"| {r['idx']} | `{r['decl']}` | {r['file']}:{r['line']} | {m['verdict']} | "
                  f"[report](mathlibable/{r['decl']}.md) |")
    pg += ["", "## Remaining declarations (in processing order)", ""]
    for r in rows[len(done):]:
        pg.append(f"- #{r['idx']} `{r['decl']}` ({r['file']}:{r['line']}, {r['visibility']} {r['kind']})")
    (OV / "PROGRESS.md").write_text("\n".join(pg) + "\n")

    # ---------------- PROJECT_OVERVIEW.md ----------------
    out = [f"# Project Overview: Roth", "",
           f"Generated by `mathlib-quality:overview` (full run, including Step 9). Last updated: {today}.",
           "",
           f"> **Status: {'complete' if (nxt is None and synth_done) else 'in progress'}** — "
           f"{len(done)}/{len(rows)} declarations assessed; project-wide synthesis "
           f"{'complete' if synth_done else 'pending'}.  Progress record: "
           "[`.mathlib-quality/overview/PROGRESS.md`](.mathlib-quality/overview/PROGRESS.md).", ""]
    synth = SYNTH.read_text() if SYNTH.exists() else ""
    exec_sum = section(synth, "Executive Summary") if synth_done else None
    out += ["## Executive Summary", "",
            exec_sum.strip() if exec_sum else
            "_Written in the project-wide synthesis unit after every declaration is assessed._", ""]
    out += ["## Statistics", "",
            f"- Files: 13, Declarations: {len(rows)} ({n_pub} public, {len(rows) - n_pub} private) — "
            + ", ".join(f"{k}: {v}" for k, v in sorted(kinds.items())),
            f"- Declarations assessed so far: {len(done)}",
            "- Mathlibable assessment (so far): " + ", ".join(
                f"{counts[b]} {b}" for b in BUCKETS) + f", {counts['INHERITED']} INHERITED, "
            f"{counts['SKIP']} pre-filtered SKIP", ""]
    out += ["---", "", "## Part 1: Declaration Inventory", ""]
    cur = None
    for r in done:
        if r["file"] != cur:
            cur = r["file"]
            out += [f"### `{cur}`", ""]
        inv = section(metas[r["decl"]][1], "Inventory entry").strip()
        out += [f"#### `{r['kind']} {r['decl']}`", "", inv, "",
                f"_Detail report: [.mathlib-quality/overview/mathlibable/{r['decl']}.md]"
                f"(.mathlib-quality/overview/mathlibable/{r['decl']}.md)_", ""]
    if nxt:
        out += [f"_Inventory continues from #{nxt['idx']} `{nxt['decl']}`._", ""]
    parts = [("Part 2: Cross-File Dependencies", "Cross-File Dependencies"),
             ("Part 3: Mathlib API Audit (MOST IMPORTANT)", "Mathlib API Audit"),
             ("Part 4: Moral Duplications", "Moral Duplications"),
             ("Part 5: Generalization Opportunities", "Generalization Opportunities"),
             ("Part 6: API Improvements", "API Improvements"),
             ("Part 7: Junk / Removable", "Junk / Removable")]
    for title, key in parts:
        body = section(synth, key) if synth_done else None
        out += [f"## {title}", "", body.strip() if body else
                "_Pending: produced by the project-wide synthesis unit from the completed inventory._", ""]
    out += ["## Part 8: Mathlibable Assessment", "",
            "| # | Declaration | File:line | Verdict | Cost | Junk (Step 8) | Rationale | Detail report |",
            "|---|---|---|---|---|---|---|---|"]
    for r in done:
        m = metas[r["decl"]][0]
        out.append(f"| {r['idx']} | `{r['decl']}` | {r['file']}:{r['line']} | {m['verdict']} | "
                   f"{m['cost']} | {m['junk']} | {m['rationale']} | "
                   f"[report](.mathlib-quality/overview/mathlibable/{r['decl']}.md) |")
    out += ["", "### Summary", ""]
    for b in ["SKIP"] + BUCKETS + ["INHERITED"]:
        out.append(f"- {b}: {counts[b]}")
    out += ["", "### Per-bucket action lists", ""]
    groups = collections.defaultdict(list)
    for r in done:
        m = metas[r["decl"]][0]
        v = m["verdict"]
        groups["INHERITED" if v.startswith("INHERITED-") else v].append((r, m))
    for b in BUCKETS + ["INHERITED"]:
        out += [f"#### {b}", ""]
        out += [f"- `{r['decl']}` ({r['file']}:{r['line']}) → {m['action']}" for r, m in groups[b]] or ["- (none yet)"]
        out.append("")
    out += ["---", "", "## Recommended Action Plan", ""]
    plan = section(synth, "Recommended Action Plan") if synth_done else None
    out += [plan.strip() if plan else
            "_Pending: written in the project-wide synthesis unit._", ""]
    (ROOT / "PROJECT_OVERVIEW.md").write_text("\n".join(out) + "\n")
    print(f"completed {len(done)}/{len(rows)}; next: {nxt['decl'] if nxt else 'none'}; "
          f"synthesis: {'complete' if synth_done else 'pending'}")


if __name__ == "__main__":
    if sys.argv[1] == "check":
        row = next(r for r in decls() if r["decl"] == sys.argv[2])
        errs = check(row)
        print("\n".join(errs) if errs else "OK")
        sys.exit(1 if errs else 0)
    build()
