# Optional public wrapper removal — pending approval

`Roth.aeval_X_eq_rename` is exactly the pointwise form of the existing mathlib
`Polynomial.toMvPolynomial_eq_rename_comp`. Declaration 11 published a one-term proof
with its complete original public type and documentation preserved. The public name
remains in the repository; no API deletion or caller edit for this option is applied.

The concrete option is to delete this public wrapper and replace every use with:

```lean
← Polynomial.toMvPolynomial, Polynomial.toMvPolynomial_eq_rename_comp,
  AlgHom.comp_apply, AlgEquiv.coe_toAlgHom
```

At the D12 candidate source hash below, there are **seven references at six proof sites**: two external Theta uses (current
lines 490 and 574), plus five uses at four Separation sites:
`degreeOf_aeval_X_none_of_ne`, `aeval_X_none_ne_zero`,
`degreeOf_none_rename_mul_aeval`, and `map_aeval_X_none` (two uses).
The first proposal inventory covered external callers only; the full project scan
corrected that scope before any source action or approval request for application.

## Concrete compiler evidence

All commands use `/Users/ramin/.elan/bin/lake env lean` from the project root:

| Exact scratch candidate | Session | Result |
|---|---:|---|
| `/private/tmp/roth-separation-wrapper-removal-theta-candidate.lean` | 61602 | Exit 0; full Theta, only the two proof substitutions changed |
| `/private/tmp/roth-separation-wrapper-removal-source-candidate.lean` | 81314 | Exit 0; full Separation, public wrapper absent and all five internal uses replaced |
| `/private/tmp/roth-separation-wrapper-removal-combined-candidate.lean` | 88401 | Exit 0; both complete modules in one compilation, with no import of actual Roth.Separation; environment assertion verifies the deleted public wrapper is absent |

Matching `.log` files contain complete output. Apart from the explicitly proposed
public deletion and seven proof substitutions, statements, definitions, assumptions,
comments and documentation remain those of the actual files. Repository source was
untouched by these probes. All owner compiler requests completed and drained.

Two preliminary Theta attempts failed and are excluded as successful evidence:
pointwise equality rewriting did not unfold `toMvPolynomial`, then a direct rewrite
sequence needed the explicit AlgEquiv-to-AlgHom coercion bridge. The final successful
candidate includes both bridges. No weakening, new axiom, sorry or limit increase was
used in the candidates.

This option removes one redundant public API name and expands the seven caller rewrite
lists with existing mathlib references. The published one-term wrapper also compiles
and preserves current clients. Approval must specifically cover the public deletion
and all seven substitutions before application. This is separate from the pending
12-theorem unused-instance menu.

Source hashes at the combined probe:

- Separation: `1d7e167ce78eb18a4815866a71a286989095d26499f49534db6af2ee823d2137`.
- Theta: `7804edad88aa3e586df46b7722755ba89e67566c5434c58ae970d0dd2fbfa4fd`.

Subsequent D13 private-helper removal moves and duplicates an internal wrapper call. The
compiled proposal above records its explicit historical source hashes. Both proposals
remain unapplied; refresh the full project inventory and exact candidate against the
then-current source before applying any eventual approval.
