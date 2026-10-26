# Per-declaration worker brief (/overview full run)

You assess exactly ONE declaration of the Roth project (Lean 4, mathlib `v4.34.0`) for the
`mathlib-quality:overview` run, then write ONE report file. You do not commit or push; the
orchestrator validates, assembles and commits after you return.

Working directory: `/Users/ramin/LEAN/Roth-2` (git worktree, branch `ramin-cleanup-2`).
Run every command from there. The project is built (`lake build` clean); lean-lsp MCP tools
are available (load them with ToolSearch, e.g. `select:mcp__lean-lsp__lean_hover_info,...`).

## Hard rules

- **Never modify** anything under `Roth/`, `Roth.lean`, `lakefile.toml`, `lake-manifest.json`,
  or `lean-toolchain`. Never run `git commit`, `git push`, `git stash`, `git checkout`, or
  `git reset`.
- Proof/weakening experiments go in scratch Lean files under
  `.mathlib-quality/overview/evidence/<Decl.Name>/` (e.g. `weaken_commsemiring.lean`,
  starting with `import Roth` or the needed `import Roth.<Module>`), compiled with
  `lake env lean <file>` or checked with `lean_run_code`. Keep every experiment file you
  rely on (they are tracked as evidence) and record its outcome in the report. Do not
  leave files that fail to compile unless the report states the failure is the evidence.
- Lean start-up is expensive on this 8 GB machine (a cold `lake env lean` of a one-line
  file takes 70–110 s). Keep Lean runs few: put ALL experiments for your declaration in
  ONE evidence file where possible, import only the module you need (e.g.
  `import Roth.HasseDeriv`, not `import Roth`), prefer the persistent lean-lsp tools
  (`lean_hover_info`, `lean_local_search`, `lean_diagnostic_messages` on your evidence
  file, re-checked in place after edits) over repeated `lake env lean` invocations, and
  never run two Lean processes at once.
- Do not mark anything complete that you did not do. If a channel/tool is unavailable,
  record `n/a` with the concrete reason (e.g. `ask_chatgpt_math` MCP not configured in
  this session).

## What to do

1. **Inventory entry (Step 2 of /overview).** Read the declaration and its whole proof
   (and the surrounding file as needed). Produce the fields below. "Uses from project"
   must be complete (grep every project identifier in the body); "Used by" must cover the
   whole project (`grep -rn` over `Roth/`), not just the file. For proofs >10 lines,
   "How" must name at least one specific lemma.
2. **Junk check (Step 8 of /overview).** Answer: used anywhere? wrapper of 1–2 mathlib
   calls? does mathlib have it (quick lean_local_search / leansearch / loogle)? too
   specific (inline?)? well-chosen definition? Conclude with one of `KEEP`,
   `INLINE`, `REMOVE`, `REPLACE` and a concrete action.
3. **Mathlibable assessment (Step 9).**
   - If the declaration is `private`: verdict `SKIP`, `Skip reason: private`.
   - Else apply the Step 9a pre-filter (name ends `_aux`; docstring starts
     `internal`/`auxiliary`; Step 8 said `REMOVE`; the *qualified* name already exists in
     mathlib per a namespace-aware grep of `.lake/packages/mathlib/Mathlib/`). If one
     fires: `SKIP` with `Skip reason: ...`.
   - Glue lemma (`:= rfl`, `Iff.rfl`, pure unfolding) about a parent def already assessed
     (see `.mathlib-quality/overview/mathlibable/`): verdict `INHERITED-<parent bucket>`
     with a line `Inherited from: <Parent>` — subject to the re-aim rule of the
     mathlibable command (if the parent is `NO-mathlib-has-it` because mathlib has a more
     general def, do a full run re-aimed at that def instead).
   - Otherwise run the **full** `/mathlibable` workflow: invoke
     `Skill(skill="mathlib-quality:mathlibable", args="<Decl.Name> --refs=/Users/ramin/.claude/plugins/cache/mathlib-quality-plugins/mathlib-quality/0.81.1/skills/mathlib-quality/references/")`
     and carry out every phase (0, 1, 2, 3 exhaustive nine-channel literature search
     including ≥3 WebSearch queries, 4a–4c, 4.6, 4.5 for def-like decls, 5 five-method
     search, 5.5, 6 incl. call-sites table, 7 with gate, 8). Use the project's own source
     paper notes in `.mathlib-quality/references/` for the local-references channel.
     Produce every required artifact heading verbatim as named in the skill (the validator
     looks for: `Baseline (Phase 0)`, `Statement (Phase 1)`, `Size classification`,
     `One-line check`, `Literature search table`, `Literature summary`,
     `Generality verdict`, `Modern-idiom verdict`, `Proof strategy verdict`,
     `Risk verdict` (def-like only), `Mathlib search-status`, `Statement-shape verdict`,
     `Call sites`, `Composition check`, `Verdict:`). Any claimed weakening must be
     compiled in an evidence file.
4. **Write the report** to `.mathlib-quality/overview/mathlibable/<Decl.Name>.md` in exactly
   this shape (front matter values on one line each, no `|` characters in them):

```
---
decl: <Decl.Name>
file: <Roth/File.lean>
line: <line>
kind: <theorem|def|...>
visibility: <public|private>
verdict: <SKIP|YES-add-as-is|YES-but-generalise-first|NO-mathlib-has-it|NO-composable-from-mathlib|BORDERLINE-needs-human|INHERITED-<bucket>>
cost: <n/a|CHEAP|MODERATE|EXPENSIVE>
junk: <KEEP|INLINE|REMOVE|REPLACE>
rationale: <one line>
action: <one-line concrete next action, naming call sites / target mathlib file where relevant>
---

# <Decl.Name>

## Inventory entry

### `<kind> <Decl.Name>`
- **Type**: ...
- **What**: ...
- **How**: ...
- **Hypotheses**: ...
- **Uses from project**: ... (or `[]`)
- **Used by**: ... (project-wide; or `unused in project`)
- **Visibility**: ...
- **Lines**: <a–b, proof length N lines>
- **Notes**: ... (or `none`)

## Junk check (Step 8)
...

## Mathlibable assessment (Step 9)
<SKIP: `Skip reason: ...` | INHERITED: `Inherited from: ...` + justification |
 full Phase 0–8 report with all artifacts and the Next step>

## Evidence
- commands / searches run and their outcomes (summarised), evidence files written
  (paths), or `none beyond the searches recorded above`.
```

5. Self-check: run
   `python3 .mathlib-quality/overview/scripts/assemble.py check <Decl.Name>` and fix
   until it prints `OK`. Then confirm `git status --short` shows changes only under
   `.mathlib-quality/overview/`.

Return to the orchestrator a single line: `<Decl.Name> | <verdict> | <one-line rationale>`
(or `FAILED: <reason>` if you could not complete the assessment).
