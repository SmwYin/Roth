# Applicable installed overview rule

Source: `/Users/ramin/.local/share/roth-mathlib-quality/commands/overview.md`, lines445–455.
Source SHA256: `55b31b886b4090802cd30ae569b76fa4e02b71a00fc210200c703ed6b8a375c8`.

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
```

This source explicitly prefilters `private` or `local` declarations from the full mathlibable worker. The inventory and applicable overview review are still completed.
