# Project overview: Roth

Updated: 2026-10-26. **IN PROGRESS — 1/293 declaration assessments complete.**

## Executive summary

Roth formalizes Roth’s theorem through Hasse derivatives, Wronskians, coefficient bounds,
weighted indices, lattice counting and an auxiliary-polynomial argument. This read-only
overview assesses contribution potential without changing production Lean sources.

The first complete assessment finds that `MvPolynomial.hasseCoeff` is a direct composition
of `Finsupp.prod` and `Nat.choose` as a standalone addition. Its semantic name remains
useful locally; this result gives no verdict on the substantive multivariate Hasse API.
The report records all required literature channels, mathlib searches, generality/risk/
strategy/shape checks, actual compiler proofs and every source caller.

This document includes only completed declaration findings. The source roadmap is not
a partial assessment of the remaining declarations. See the completed-only
[progress record](.mathlib-quality/overview/progress.md) and
[restart contract](.mathlib-quality/overview/README.md).

## Statistics

- Production Lean files: 14; written declarations: 293 (28 definitions,191 theorems,74 lemmas).
- Visibility:215 public,78 private; root Roth.lean has no declarations.
- Completed applicable assessments: 1; remaining: 292.
- Verdicts:1 NO-composable,0 YES-add-as-is,0 YES-but-generalise-first,0 NO-mathlib-has-it,0 BORDERLINE,0 SKIP.
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

## Part 4: Moral duplications

For the completed declaration, no second independent implementation of the same support
product was found in project code. The all-coordinate finite product is a bridge, not a
better replacement for arbitrary variable types. Other declaration findings remain unpublished.

## Part 5: Generalization opportunities

The completed assessment compiled an optional extension accepting an arbitrary upper-index
function instead of a Finsupp. It is not needed for the standard monomial API and does not
create independent upstream content. No production change is recommended during this review.

## Part 6: API improvements

A named coefficient may belong with a coherent multivariate Hasse derivative package.
That packaging decision awaits the substantive declarations’ own assessments; it is not
a reason for a separate PR consisting only of this two-operation alias.

## Part 7: Junk / removable

hasseCoeff is live API, not dead code. Keep it locally during this read-only overview.
The detailed report provides an optional all-callers inlining plan for a later authorized
refactor; it has not been executed or falsely reported as validated.

## Part 8: Mathlibable assessment

| # | Declaration | Verdict | Detail and evidence |
|---|---|---|---|
| 1 | `MvPolynomial.hasseCoeff` | NO-composable-from-mathlib (standalone def) | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff/root-acceptance.json) |

All remaining declarations are unfinished; none has an assigned final verdict here.

## Recommended action plan

1. Retain the useful local coefficient alias while assessing the complete Hasse API.
2. Do not submit a standalone PR for this direct two-operation definition.
3. Assess `MvPolynomial.hasseDeriv` next, without inheriting a NO verdict from its helper.
4. Preserve all per-declaration query/proof/log evidence and publish only accepted complete assessments.
5. Keep production Lean sources and pins unchanged; use a warm server and bounded, batched scratch checks.
