Source: /Users/ramin/.local/share/roth-mathlib-quality/commands/overview.md

#### Step 9a — Pre-filter (cheap)

Some declarations don't need a full run because the answer is obvious from
cheap signals. Skip a declaration if any of:

- `private` or `local` modifier
- in a `test/` or `examples/` directory
- name ends in `_aux` (intended to be inlined, not PR'd)
- docstring starts with `internal` or `auxiliary`
- already flagged REMOVE by Step 8 (Junk Identification)
- the exact unqualified name already exists in mathlib (cheap grep over
  `.lake/packages/mathlib/Mathlib/` for `(theorem|lemma|def) <name> ` — if
  found, record as `SKIP-collides-with-mathlib` and don't dispatch)

Record these as `SKIP` in the verdict table with a one-line reason. They do
NOT get a full `/mathlibable` run.

#### Step 9b — Dispatch (orchestrator-worker)
