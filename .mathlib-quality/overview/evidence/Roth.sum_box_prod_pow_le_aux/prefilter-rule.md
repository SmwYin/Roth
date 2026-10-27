# Applicable private-declaration rule

### B1 — Pre-filter (cheap, namespace-aware)

For each enumerated declaration, run the cheap SKIP checks first:

- `private` / `local` modifier (already filtered in B0, but re-check)
- in `test/` or `examples/`
- name ends in `_aux`
- docstring starts with `internal` or `auxiliary`
- the **qualified** name already exists in mathlib — cheap grep over
  `.lake/packages/mathlib/Mathlib/` for the *namespace-aware* pattern
  `\b(theorem|lemma|def|...)\s+<Qualified.Name>\b` (and dot-notation
  variants like `<Namespace>.<name>`). **Do NOT match on bare name alone.**

**The bare-name SKIP is unsafe and has been removed.** Common short names
(`coeFun`, `translateCM`, `continuous_coeFun`, `finite_norm_le`) collide
with unrelated mathlib decls in other namespaces / types and would wrongly
drop genuine contributions. The cheap check stays cheap; it just requires
the qualified name match. A bare-name hit without namespace agreement
records as `MAYBE-COLLISION` and gets a full Agent run (it might be a
genuine contribution; the full workflow's Phase 5 mathlib search will
resolve it).

Record each pre-filtered SKIP decl with verdict `SKIP` and a one-line
reason. They do NOT get a full Agent run.


Source: /Users/ramin/.local/share/roth-mathlib-quality/commands/mathlibable.md
SHA256: 4beeb5d910a7723e6b1006d1e6c707a671721b3db3fc4e92e5a7979efa77923f
