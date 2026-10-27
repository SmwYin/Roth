# Applicable installed overview rule

Source: `/Users/ramin/.local/share/roth-mathlib-quality/commands/overview.md`. SHA256: `55b31b886b4090802cd30ae569b76fa4e02b71a00fc210200c703ed6b8a375c8`.

```text
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

```

Private declarations are excluded from the public contribution worker. Applicable overview inventory, structural review and verification remain required.
