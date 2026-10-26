# Project overview: Roth

Updated: 2026-10-26. **IN PROGRESS — 4/293 declaration assessments complete.**

## Executive summary

Roth formalizes Roth’s theorem through Hasse derivatives, Wronskians, coefficient bounds,
weighted indices, lattice counting and an auxiliary-polynomial argument. This read-only
overview assesses contribution potential without changing production Lean sources.

The first complete assessment finds that `MvPolynomial.hasseCoeff` is a direct composition
of `Finsupp.prod` and `Nat.choose` as a standalone addition. Its semantic name remains
useful locally; this result gives no verdict on the substantive multivariate Hasse API.
The report records all required literature channels, mathlib searches, generality/risk/
strategy/shape checks, actual compiler proofs and every source caller.

The second complete assessment recommends `MvPolynomial.hasseDeriv` as a mathlib addition:
its arbitrary-variable, characteristic-free linear operator fills the gap between ordinary
multivariate partial derivatives and univariate Hasse derivatives. A mathlib-only scratch
construction and monomial characterization compiled, and all required assessment gates passed.

This document includes only completed declaration findings. The source roadmap is not
a partial assessment of the remaining declarations. See the completed-only
[progress record](.mathlib-quality/overview/progress.md) and
[restart contract](.mathlib-quality/overview/README.md).

## Statistics

- Production Lean files: 14; written declarations: 293 (28 definitions,191 theorems,74 lemmas).
- Visibility:215 public,78 private; root Roth.lean has no declarations.
- Completed applicable assessments: 4; remaining: 289.
- Verdicts: 3 NO-composable-from-mathlib, 1 YES-add-as-is, 0 YES-but-generalise-first, 0 NO-mathlib-has-it, 0 BORDERLINE-needs-human, 0 SKIP.
- Baseline full build:PASS,2,467 jobs; sources and pins unchanged.

## Part 1: Declaration inventory

The [source roadmap](.mathlib-quality/overview/declaration-order.json) lists every written
declaration, source location, kind, visibility and span identity. Detailed assessment
entries are published only after the corresponding full applicable workflow is complete.

### Completed: `MvPolynomial.hasseCoeff`

- Type: `{σ : Type u} → (σ →₀ ℕ) → (σ →₀ ℕ) → ℕ`.
- What: coordinatewise binomial coefficient for finitely supported natural multiindices.
- How: support product using `Finsupp.prod` and `Nat.choose`.
- Hypotheses: none; arbitrary universe-polymorphic variable type.
- Uses from project: []; visibility: public; source: Roth/HasseDeriv.lean:50.
- Callers:16 same-file declarations plus2 external declarations on3 external code lines.
- Full signatures, all caller excerpts, source hashes, verification and notes:
  [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff.md).

### Completed: `MvPolynomial.hasseDeriv`

- Type: `{σ : Type u} → {R : Type v} → [CommSemiring R] → (σ →₀ ℕ) → MvPolynomial σ R →ₗ[R] MvPolynomial σ R`.
- What: the normalized multivariate Hasse differential operator of finite multiorder.
- How: linear extension of the binomial-weighted monomial rule through `Finsupp.lsum`.
- Hypotheses: arbitrary variables and independent coefficient universe; commutative semiring.
- Uses from project: `MvPolynomial.hasseCoeff`; public; source: Roth/HasseDeriv.lean:57.
- Callers: 59 declarations on 92 code lines, including 41 declarations outside its file.
- Recommendation: YES-add-as-is, as a coherent multivariate differential API.
- [Complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv.md) records full evidence.

### Completed: `MvPolynomial.hasseDeriv_monomial`

- Type: `{σ R : Type*} [CommSemiring R] (d k : σ →₀ ℕ) (a : R) : hasseDeriv d (monomial k a) = monomial (k-d) ((hasseCoeff d k : R)*a)`.
- What: Computes the Hasse derivative of a scalar monomial.
- How: Evaluates the Finsupp.lsum defining hasseDeriv on the single coefficient supported at the input exponent.
- Hypotheses: A commutative coefficient semiring, any differentiation and monomial indices, and any scalar.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseCoeff
- Callers: 4 declarations on 5 code lines, with 7 explicit uses; 3 uses in one external Taylor helper.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_monomial.md).

### Completed: `MvPolynomial.hasseDeriv_apply`

- Type: `{σ : Type u} {R : Type v} [CommSemiring R] (d : σ →₀ ℕ) (P : MvPolynomial σ R) : hasseDeriv d P = ∑ k ∈ P.support, monomial (k-d) ((hasseCoeff d k : R) * P.coeff k)`
- What: Expands a multivariate Hasse derivative as the finite sum of the differentiated monomials of its input.
- How: Evaluates the defining Finsupp.lsum on the coefficient vector and exposes the polynomial support sum.
- Hypotheses: A commutative coefficient semiring, arbitrary variable type, differentiation multiindex and polynomial; no proposition hypotheses.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseCoeff
- Caller summary: whole project: lines: 1; occurrences: 1; distinct callers: 1; outside defining file: lines: 1; occurrences: 1; distinct callers: 1; files: 1; same file: lines: 0; occurrences: 0; distinct callers: 0; caller: Roth.normOne_hasseDeriv_le at Roth/CoeffNorm.lean:151
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_apply.md).

## Part 2: Cross-file dependencies

| File | Project imports | Written declarations |
|---|---|---:|
| `Roth/HasseDeriv.lean` | [] | 25 |
| `Roth/Box.lean` | [] | 14 |
| `Roth/Wronskian.lean` | [] | 13 |
| `Roth/Taylor.lean` | `Roth.Box`, `Roth.HasseDeriv` | 22 |
| `Roth/CoeffNorm.lean` | `Roth.Box`, `Roth.HasseDeriv` | 26 |
| `Roth/GenWronskian.lean` | `Roth.HasseDeriv`, `Roth.Wronskian` | 19 |
| `Roth/Lattice.lean` | `Roth.Box` | 13 |
| `Roth/Index.lean` | `Roth.Box`, `Roth.Taylor` | 19 |
| `Roth/Separation.lean` | `Roth.CoeffNorm`, `Roth.GenWronskian` | 27 |
| `Roth/Theta.lean` | `Roth.CoeffNorm`, `Roth.Index`, `Roth.Separation` | 50 |
| `Roth/MainLemma.lean` | `Roth.Lattice`, `Roth.Theta` | 38 |
| `Roth/Main.lean` | `Roth.MainLemma` | 23 |
| `Roth/LeanEval.lean` | `Roth.Main` | 4 |
| `Roth.lean` | `Roth.HasseDeriv`, `Roth.Box`, `Roth.Wronskian`, `Roth.Taylor`, `Roth.CoeffNorm`, `Roth.GenWronskian`, `Roth.Lattice`, `Roth.Index`, `Roth.Separation`, `Roth.Theta`, `Roth.MainLemma`, `Roth.Main` | 0 |

## Part 3: Mathlib API audit

Completed finding: hasseCoeff uses the existing finite-support product and natural choice
operations. `Finsupp.multinomial` is a different operation and is not a replacement. The
mathlib-only construction compiled without importing the project target.

Completed derivative finding: pinned mathlib has ordinary multivariate `pderiv` and
univariate `Polynomial.hasseDeriv`, but no verified arbitrary-multiindex normalized
operator. Generic coefficient-linear extension constructs it; this is distinct from
a ready-made differential API replacement.

Completed `MvPolynomial.hasseDeriv_monomial`: Existing Finsupp.lsum_single generic evaluation; univariate Polynomial.hasseDeriv_monomial and order-one MvPolynomial.pderiv_monomial are partial analogues, not arbitrary-multiindex replacements.

Completed `MvPolynomial.hasseDeriv_apply`: Direct Finsupp.lsum_apply term accepted for original target. MvPolynomial.sum_def is existing support-sum bridge; Polynomial.hasseDeriv_apply is only univariate analogue.

## Part 4: Moral duplications

For the completed declaration, no second independent implementation of the same support
product was found in project code. The all-coordinate finite product is a bridge, not a
better replacement for arbitrary variable types. Other declaration findings remain unpublished.

Completed `MvPolynomial.hasseDeriv_monomial`: Proof is generic linear-extension evaluation; no independent rederivation of exact monomial law found in written production code.

Completed `MvPolynomial.hasseDeriv_apply`: Generic finite-support linear-extension evaluation instantiated with defining component maps; no independent exact inline rederivation found in canonical production sources.

## Part 5: Generalization opportunities

The completed assessment compiled an optional extension accepting an arbitrary upper-index
function instead of a Finsupp. It is not needed for the standard monomial API and does not
create independent upstream content. No production change is recommended during this review.

The derivative already uses arbitrary variable types and commutative-semiring coefficients.
The rejected `Semiring` experiment fails at `MvPolynomial` itself; no weakening is proposed.

Completed `MvPolynomial.hasseDeriv_monomial`: No verified hypothesis weakening; CommSemiring floor confirmed. Natural-index/Laurent widening changes domains. Q8 points to already-existing abstract evaluation theorem.

Completed `MvPolynomial.hasseDeriv_apply`: No verified hypothesis weakening; Semiring floor cannot form current operator. Q8 identifies existing arbitrary-family lsum_apply abstraction; unrelated higher derivations are not this fixed coordinate operator.

## Part 6: API improvements

A named coefficient may belong with a coherent multivariate Hasse derivative package.
The derivative assessment supports a coherent upstream operator API; its supporting
identities still await their own assessments. This is not
a reason for a separate PR consisting only of this two-operation alias.

Completed `MvPolynomial.hasseDeriv_monomial`: No new generic evaluation API needed: existing Finsupp.lsum_single directly proves the law after definitional transport. Exact coordinate operator name absent in mathlib-only environment is not a mathematical absence proof.

Completed `MvPolynomial.hasseDeriv_apply`: No new generic evaluation API needed. Mathlib-only exact qualified name check does not establish absence of all equivalent mathematics.

## Part 7: Junk / removable

hasseCoeff is live API, not dead code. Keep it locally during this read-only overview.
The detailed report provides an optional all-callers inlining plan for a later authorized
refactor; it has not been executed or falsely reported as validated.

The derivative is live API across Taylor expansions, multiplicities and generalized
Wronskians; retain it. No production removal or refactor was performed.

Completed `MvPolynomial.hasseDeriv_monomial`: Not junk: seven explicit uses across four caller declarations, including Taylor interface.

Completed `MvPolynomial.hasseDeriv_apply`: Not junk: one explicit caller uses the support expansion to bound normOne.

## Part 8: Mathlibable assessment

| # | Declaration | Verdict | Detail and evidence |
|---|---|---|---|
| 1 | `MvPolynomial.hasseCoeff` | NO-composable-from-mathlib (standalone def) | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff/root-acceptance.json) |
| 2 | `MvPolynomial.hasseDeriv` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/root-acceptance.json) |
| 3 | `MvPolynomial.hasseDeriv_monomial` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_monomial.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_monomial/root-acceptance.json) |
| 4 | `MvPolynomial.hasseDeriv_apply` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_apply.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_apply/root-acceptance.json) |

All remaining declarations are unfinished; none has an assigned final verdict here.

Completed `MvPolynomial.hasseDeriv_monomial` action: Retain local semantic simp helper during read-only overview; no standalone upstream addition. If future authorized wrapper removal, inline direct generic evaluation at seven explicit uses on five lines, update parent docstring, audit implicit simp use and rebuild.

Completed `MvPolynomial.hasseDeriv_apply` action: Retain production API during read-only overview. No standalone upstream theorem; if future wrapper removal authorized, inline the verified generic equality at the sole normOne caller, remove theorem and rebuild; package-level semantic API review remains separate.

## Recommended action plan

1. Retain the useful local coefficient alias while assessing the complete Hasse API.
2. Do not submit a standalone PR for this direct two-operation definition.
3. Prepare the multivariate Hasse operator for a future coherent mathlib contribution; assess
   `MvPolynomial.hasseCoeff_eq_zero_iff` next. Supporting identities receive their own applicable checks.
4. Preserve all per-declaration query/proof/log evidence and publish only accepted complete assessments.
5. Keep production Lean sources and pins unchanged; use a warm server and bounded, batched scratch checks.
