#!/usr/bin/env python3
"""Deterministic declaration list for the /overview run.

Emits TSV: index, qualified name, kind, visibility, file, line.
File order follows the module order in `Roth.lean`, then `Roth/LeanEval.lean`.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
ORDER = ["HasseDeriv", "Box", "Wronskian", "Taylor", "CoeffNorm", "GenWronskian",
         "Lattice", "Index", "Separation", "Theta", "MainLemma", "Main", "LeanEval"]
DECL = re.compile(r"^(?:@\[[^\]]*\]\s*)?((?:(?:private|protected|noncomputable)\s+)*)"
                  r"(theorem|lemma|def|abbrev|instance|structure|class|inductive)\s+([^\s:({\[]+)?")
NS = re.compile(r"^namespace\s+(\S+)")
END = re.compile(r"^end\s+(\S+)")

rows = []
for mod in ORDER:
    path = ROOT / "Roth" / f"{mod}.lean"
    stack = []
    in_comment = 0
    for i, line in enumerate(path.read_text().splitlines(), 1):
        # crude block-comment tracking so docstring text is not parsed
        if in_comment:
            in_comment += line.count("/-") - line.count("-/")
            continue
        if line.lstrip().startswith("/-"):
            in_comment = line.count("/-") - line.count("-/")
            continue
        if m := NS.match(line):
            stack.extend(m.group(1).split("."))
            continue
        if (m := END.match(line)) and stack and ".".join(stack).endswith(m.group(1)):
            del stack[len(stack) - len(m.group(1).split(".")):]
            continue
        if m := DECL.match(line):
            mods, kind, name = m.groups()
            vis = "private" if "private" in mods else ("protected" if "protected" in mods else "public")
            if name is None or name in ("where",):
                name = f"<anonymous-{kind}-L{i}>"
            q = name if name.startswith("_root_.") else ".".join(stack + [name])
            q = q.removeprefix("_root_.")
            rows.append((q, kind, vis, f"Roth/{mod}.lean", i))

for n, r in enumerate(rows, 1):
    print(n, *r, sep="\t")
