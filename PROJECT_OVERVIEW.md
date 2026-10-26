# Project overview: Roth

Updated: 2026-10-26. **IN PROGRESS — 10/293 declaration assessments complete.**

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
- Completed applicable assessments: 10; remaining: 283.
- Verdicts: 4 NO-composable-from-mathlib, 2 YES-add-as-is, 0 YES-but-generalise-first, 0 NO-mathlib-has-it, 4 BORDERLINE-needs-human, 0 SKIP.
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

### Completed: `MvPolynomial.hasseCoeff_eq_zero_iff`

- Type: `∀ {σ : Type*} (d k : σ →₀ ℕ), hasseCoeff d k = 0 ↔ ¬d ≤ k`
- What: The natural multi-index binomial factor is zero exactly outside the coordinatewise exponent interval.
- How: Generic product-zero criterion, scalar choose-zero criterion, supported order and negation normalization.
- Hypotheses: Arbitrary variable type and two natural finitely supported indices; no coefficient classes.
- Project dependencies: MvPolynomial.hasseCoeff
- Caller summary: 3 direct callers: coeff_hasseDeriv and hasseDeriv_C in HasseDeriv; private coeff_taylor_monomial_single_add_aux in Taylor. All use vanishing from failed coordinate order.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_eq_zero_iff.md).

### Completed: `MvPolynomial.coeff_hasseDeriv`

- Type: `For arbitrary variable/coefficient types and CommSemiring R, d,e:σ→₀ℕ, P:MvPolynomial σ R: coeff e (hasseDeriv d P) = (hasseCoeff d (e+d):R) * coeff (e+d) P.`
- What: Computes each coefficient of a multivariate Hasse derivative as one shifted input coefficient multiplied by its natural binomial factor.
- How: Additive polynomial induction; monomial coefficient evaluation; distinguish reconstructed exponent, dominating order and vanishing binomial cases.
- Hypotheses: Arbitrary variable type and commutative coefficient semiring, finite natural derivative/output multiindices and arbitrary polynomial; no finite-variable, field, characteristic, domain or nontriviality hypotheses.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseCoeff, MvPolynomial.hasseDeriv_monomial, MvPolynomial.hasseCoeff_eq_zero_iff
- Caller summary: Eight explicit caller declarations (seven internal, one in CoeffNorm), eleven invocation tokens. Supplies zero/map/composition/pderiv/degree/vanishing/univariate-compatibility and absolute coefficient bound proofs. No identical inlined duplicate found in reviewed source; no opaque dependency closure claimed.
- Verdict: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_hasseDeriv.md).

### Completed: `MvPolynomial.hasseCoeff_eq_prod`

- Type: `For any variable type σ with Fintype σ and d,k:σ→₀ℕ, hasseCoeff d k = ∏j, Nat.choose (k j) (d j). No coefficient type R or semiring assumption occurs in the actual type.`
- What: Replaces the support product of coordinatewise binomial coefficients by the full product over finite variables.
- How: Specializes Finsupp.prod_fintype with the unit condition Nat.choose_zero_right; exactly two mathlib calls.
- Hypotheses: Arbitrary universe-polymorphic variable type, finite enumeration and two natural multiindices. No dominance, field, characteristic, nontriviality, nonempty or coefficient-ring assumption.
- Project dependencies: MvPolynomial.hasseCoeff
- Caller summary: One explicit same-file caller: MvPolynomial.hasseCoeff_le_two_pow at Roth/HasseDeriv.lean:276, invocation 278. Zero callers outside the declaring file. No identical inline duplicate; nearby support-subset binomial and full power-product uses are related generic routes. Explicit source audit only.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_eq_prod.md).

### Completed: `MvPolynomial.hasseDeriv_zero_apply`

- Type: `For arbitrary types σ,R with CommSemiring R and P:MvPolynomial σ R, MvPolynomial.hasseDeriv 0 P = P.`
- What: The multivariate Hasse derivative of order zero fixes every polynomial.
- How: Coefficient extensionality and coeff_hasseDeriv reduce to zero-index support product one; independently verified expanded lsum normalization also works.
- Hypotheses: Arbitrary universe-polymorphic variable/coefficient types, CommSemiring coefficients, arbitrary polynomial; no finiteness, characteristic, domain, nonzero or decidable equality assumptions.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.coeff_hasseDeriv, MvPolynomial.hasseCoeff
- Caller summary: Three explicit source uses in two declarations: LinearMap.ext in hasseDeriv_zero at HasseDeriv.lean:121, and two simp mentions in Roth.index_eq_zero_iff at Index.lean:104–105. Both caller alternatives formally replayed; explicit source scope only.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_zero_apply.md).

### Completed: `MvPolynomial.hasseDeriv_zero`

- Type: `For arbitrary types σ,R with CommSemiring R, MvPolynomial.hasseDeriv (0 : σ →₀ ℕ) = (LinearMap.id : MvPolynomial σ R →ₗ[R] MvPolynomial σ R).`
- What: The zero-order multivariate Hasse derivative is the identity linear operator.
- How: Current term applies LinearMap.ext to project hasseDeriv_zero_apply. Independently checked coefficient proof and mathlib-only reconstructed construction normalization establish the same bundled equality.
- Hypotheses: Arbitrary universe-polymorphic variable and coefficient types, CommSemiring coefficients; no finiteness, decidability, characteristic, domain or nontriviality assumptions.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseDeriv_zero_apply
- Caller summary: Zero explicit theorem-name proof callers in project source. Neighboring pointwise theorem has two Index.lean mentions, not callers of this target. Bare simp application and bundled composition consumers actually verified; no exhaustive implicit dependency claim.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_zero.md).

### Completed: `MvPolynomial.hasseDeriv_C`

- Type: `∀ {σ R : Type*} [CommSemiring R] {d : σ →₀ ℕ}, d ≠ 0 → ∀ a : R, MvPolynomial.hasseDeriv d (MvPolynomial.C a) = 0`
- What: Every nonzero-order multivariate Hasse derivative annihilates scalar constant polynomials.
- How: Rewrite constant as exponent-zero monomial, apply project Hasse monomial rule, kill binomial factor by nonzero order and simplify. Independent raw construction proof verified using typed Finsupp.lsum_single.
- Hypotheses: Arbitrary universes/variables; CommSemiring fixed parent floor; implicit finite natural multi-index d, essential d ≠ 0, arbitrary scalar a. No characteristic or nontriviality assumptions.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseCoeff, MvPolynomial.hasseDeriv_monomial, MvPolynomial.hasseCoeff_eq_zero_iff
- Caller summary: One explicit source call in private MvPolynomial.coeff_taylor_monomial_aux, Roth/Taylor.lean:127. Original and possible inline affected zero branch native-verified. Not a global simp rule; explicit simp argument. No opaque/implicit closure claim.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_C.md).

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

Completed `MvPolynomial.hasseCoeff_eq_zero_iff`: Five methods on 3 forms; Finsupp.prod_eq_zero_iff/prod_ne_zero_iff, Nat.choose_eq_zero_iff/choose_ne_zero_iff and Finsupp.le_iff verified at pin; generic simp passes.

Completed `MvPolynomial.coeff_hasseDeriv`: Univariate Polynomial.hasseDeriv_coeff is the direct analogue, not an arbitrary-variable replacement. LaurentSeries coefficient API, coeff_pderiv, lsum and comapDomain building blocks do not alone prove the truncated-subtraction collision/vanishing identity. All five search methods and isolated exact? guard executed; local symbol index unavailable.

Completed `MvPolynomial.hasseCoeff_eq_prod`: All five methods searched concrete/literature and abstract forms. Finsupp.prod_fintype (BigOperators/Finsupp/Basic:63) plus Nat.choose_zero_right (Choose/Basic:56) proves the exact target. Isolated pinned check and complete caller rewrite verified; unavailable local index supplies no absence evidence.

Completed `MvPolynomial.hasseDeriv_zero_apply`: All five methods actually searched current/literature and abstract forms. Polynomial zero laws are univariate analogues, generic reconstruction/lsum laws supply normalization machinery. Guarded mathlib-only reconstruction plus exact?/apply? positive controls and positive candidate signatures verified in pin. Local index unavailable.

Completed `MvPolynomial.hasseDeriv_zero`: All five methods actually searched current, literature and abstract forms. Polynomial.hasseDeriv_zero is an analogous bundled univariate law; LaurentSeries analogue distinct. LinearMap.ext and polynomial reconstruction support normalization, with native pinned positive checks. Local index unavailable.

Completed `MvPolynomial.hasseDeriv_C`: All five actual methods on current/literature/abstract forms. Polynomial.hasseDeriv_C is univariate analogue, pderiv_C ordinary first derivative only. C_apply and lsum_single genuine generic normalization blocks; local factor-zero is new proof, not existing replacement.

## Part 4: Moral duplications

For the completed declaration, no second independent implementation of the same support
product was found in project code. The all-coordinate finite product is a bridge, not a
better replacement for arbitrary variable types. Other declaration findings remain unpublished.

Completed `MvPolynomial.hasseDeriv_monomial`: Proof is generic linear-extension evaluation; no independent rederivation of exact monomial law found in written production code.

Completed `MvPolynomial.hasseDeriv_apply`: Generic finite-support linear-extension evaluation instantiated with defining component maps; no independent exact inline rederivation found in canonical production sources.

Completed `MvPolynomial.hasseCoeff_eq_zero_iff`: Combines existing generic/scalar/order API; no exact named existing theorem claimed.

Completed `MvPolynomial.coeff_hasseDeriv`: Natural multivariate extension of Polynomial.hasseDeriv_coeff; generic lowering characterization and weighted-pullback implementation are new alternatives rather than existing API duplicates.

Completed `MvPolynomial.hasseCoeff_eq_prod`: A specialization of generic identity-padding of a finitely supported product. Multinomial factorial ratios are a false friend, not the same coefficient.

Completed `MvPolynomial.hasseDeriv_zero_apply`: Mirrors univariate pointwise/map zero laws. Generic coefficient preservation implies identity via extensionality, but normalization for the concrete Hasse family remains content; new local abstraction is not an existing replacement.

Completed `MvPolynomial.hasseDeriv_zero`: Mirrors Polynomial.hasseDeriv_zero and neighboring pointwise normalization. Generic LinearMap.ext only packages a premise and is not unconditional concrete operator normalization.

Completed `MvPolynomial.hasseDeriv_C`: Mirrors Polynomial.hasseDeriv_C; generic C/monomial/lsum normalization exists but does not supply concrete nonzero-order binomial vanishing premise.

## Part 5: Generalization opportunities

The completed assessment compiled an optional extension accepting an arbitrary upper-index
function instead of a Finsupp. It is not needed for the standard monomial API and does not
create independent upstream content. No production change is recommended during this review.

The derivative already uses arbitrary variable types and commutative-semiring coefficients.
The rejected `Semiring` experiment fails at `MvPolynomial` itself; no weakening is proposed.

Completed `MvPolynomial.hasseDeriv_monomial`: No verified hypothesis weakening; CommSemiring floor confirmed. Natural-index/Laurent widening changes domains. Q8 points to already-existing abstract evaluation theorem.

Completed `MvPolynomial.hasseDeriv_apply`: No verified hypothesis weakening; Semiring floor cannot form current operator. Q8 identifies existing arbitrary-family lsum_apply abstraction; unrelated higher derivations are not this fixed coordinate operator.

Completed `MvPolynomial.hasseCoeff_eq_zero_iff`: No coefficient assumptions, arbitraryσ. Verified expanded theorem permits upper k:σ→ℕ; lower d supplies finite product support. Existing hasseCoeff signature fixes upperFinsupp, so realize widening by broader product statement or parent API change. Arbitrary-ring cast iff rejected.

Completed `MvPolynomial.coeff_hasseDeriv`: Maximal for pinned MvPolynomial CommSemiring domain. A Semiring-only domain is compile-rejected. Generic weighted L helper verified but optional; bundled lcoeff/function forms verified and less convenient at current rewrite callers.

Completed `MvPolynomial.hasseCoeff_eq_prod`: Verified expanded version accepts arbitrary upper k:σ→ℕ with the same proof. Generic factor/CommMonoid and finite ambient-set forms already exist in mathlib. The literal full ∏j expression needs Fintype; upper-function widening needs no new product construction.

Completed `MvPolynomial.hasseDeriv_zero_apply`: Current interface already arbitrary σ and CommSemiring. Unnormalized arbitrary linear maps, general zero-order differential operators, or general-codomain HS zero homomorphisms need not be identity; counterexample compiled.

Completed `MvPolynomial.hasseDeriv_zero`: Current operator interface already arbitrary-variable CommSemiring. Module-valued/general higher-derivation families require new definitions; no verified one-edit weakening. False arbitrary-linear-map identity formally refuted.

Completed `MvPolynomial.hasseDeriv_C`: Already arbitrary-variable commutative-semiring interface. Abstract HS-system packaging would require parent redevelopment. No verified mechanical weakening; d=0,C1 formal counterexample.

## Part 6: API improvements

A named coefficient may belong with a coherent multivariate Hasse derivative package.
The derivative assessment supports a coherent upstream operator API; its supporting
identities still await their own assessments. This is not
a reason for a separate PR consisting only of this two-operation alias.

Completed `MvPolynomial.hasseDeriv_monomial`: No new generic evaluation API needed: existing Finsupp.lsum_single directly proves the law after definitional transport. Exact coordinate operator name absent in mathlib-only environment is not a mathematical absence proof.

Completed `MvPolynomial.hasseDeriv_apply`: No new generic evaluation API needed. Mathlib-only exact qualified name check does not establish absence of all equivalent mathematics.

Completed `MvPolynomial.hasseCoeff_eq_zero_iff`: None proven; upstream packaging of natural multi-binomial/order criterion is a policy question.

Completed `MvPolynomial.coeff_hasseDeriv`: Arbitrary-variable characteristic-free Hasse derivative coefficient interface, next to MvPolynomial.PDeriv and the multivariate Hasse operator.

Completed `MvPolynomial.hasseCoeff_eq_prod`: None for the support/full-product bridge: Finsupp.prod_fintype and prod_of_support_subset already cover it.

Completed `MvPolynomial.hasseDeriv_zero_apply`: No separate generic helper gap established. Whether this pointwise normalization deserves its own exported corollary in the new multivariate Hasse API is an upstream design question.

Completed `MvPolynomial.hasseDeriv_zero`: Concrete multivariate Hasse definition and coefficient interface form the upstream context; no distinct missing generic extensionality helper. Exporting one or both zero-law forms is an API design question.

Completed `MvPolynomial.hasseDeriv_C`: Multivariate Hasse parent and coefficient/monomial interface are needed upstream context. Named scalar constant normalization/simp policy remains a design choice; no missing generic lsum-single helper.

## Part 7: Junk / removable

hasseCoeff is live API, not dead code. Keep it locally during this read-only overview.
The detailed report provides an optional all-callers inlining plan for a later authorized
refactor; it has not been executed or falsely reported as validated.

The derivative is live API across Taylor expansions, multiplicities and generalized
Wronskians; retain it. No production removal or refactor was performed.

Completed `MvPolynomial.hasseDeriv_monomial`: Not junk: seven explicit uses across four caller declarations, including Taylor interface.

Completed `MvPolynomial.hasseDeriv_apply`: Not junk: one explicit caller uses the support expansion to bound normOne.

Completed `MvPolynomial.hasseCoeff_eq_zero_iff`: Useful semantic interface at3callers; not dead or vacuous.

Completed `MvPolynomial.coeff_hasseDeriv`: None: substantial coefficient interface, not glue, unused code or a three-call wrapper.

Completed `MvPolynomial.hasseCoeff_eq_prod`: Useful local semantic rewrite with one caller, but a redundant standalone upstream wrapper; not narrow rfl/unfold glue.

Completed `MvPolynomial.hasseDeriv_zero_apply`: Used at three explicit sites and semantically standard; not dead code or rfl/unfold glue. It may be API-redundant if only bundled normalization is exported.

Completed `MvPolynomial.hasseDeriv_zero`: No explicit callers, but a registered simp rule with actual implicit-consumer demonstrations; not established dead code, and not rfl/unfold glue.

Completed `MvPolynomial.hasseDeriv_C`: Not junk: one real Taylor induction caller, standard positive-order law, no inherited glue classification.

## Part 8: Mathlibable assessment

| # | Declaration | Verdict | Detail and evidence |
|---|---|---|---|
| 1 | `MvPolynomial.hasseCoeff` | NO-composable-from-mathlib (standalone def) | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff/root-acceptance.json) |
| 2 | `MvPolynomial.hasseDeriv` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/root-acceptance.json) |
| 3 | `MvPolynomial.hasseDeriv_monomial` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_monomial.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_monomial/root-acceptance.json) |
| 4 | `MvPolynomial.hasseDeriv_apply` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_apply.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_apply/root-acceptance.json) |
| 5 | `MvPolynomial.hasseCoeff_eq_zero_iff` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_eq_zero_iff.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff_eq_zero_iff/root-acceptance.json) |
| 6 | `MvPolynomial.coeff_hasseDeriv` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_hasseDeriv.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.coeff_hasseDeriv/root-acceptance.json) |
| 7 | `MvPolynomial.hasseCoeff_eq_prod` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_eq_prod.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff_eq_prod/root-acceptance.json) |
| 8 | `MvPolynomial.hasseDeriv_zero_apply` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_zero_apply.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_zero_apply/root-acceptance.json) |
| 9 | `MvPolynomial.hasseDeriv_zero` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_zero.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_zero/root-acceptance.json) |
| 10 | `MvPolynomial.hasseDeriv_C` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_C.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_C/root-acceptance.json) |

All remaining declarations are unfinished; none has an assigned final verdict here.

Completed `MvPolynomial.hasseDeriv_monomial` action: Retain local semantic simp helper during read-only overview; no standalone upstream addition. If future authorized wrapper removal, inline direct generic evaluation at seven explicit uses on five lines, update parent docstring, audit implicit simp use and rebuild.

Completed `MvPolynomial.hasseDeriv_apply` action: Retain production API during read-only overview. No standalone upstream theorem; if future wrapper removal authorized, inline the verified generic equality at the sole normOne caller, remove theorem and rebuild; package-level semantic API review remains separate.

Completed `MvPolynomial.hasseCoeff_eq_zero_iff` action: BORDERLINE-needs-human for upstream packaging and verified upper-function widening. Retain local theorem during read-only overview; all execution checks complete; proceed after root acceptance.

Completed `MvPolynomial.coeff_hasseDeriv` action: YES-add-as-is: include with multivariate Hasse operator in a focused upstream module; inline scalar alias in statement if hasseCoeff is omitted, retain shifted coefficient normal form.

Completed `MvPolynomial.hasseCoeff_eq_prod` action: NO-composable-from-mathlib: inline d.prod_fintype _ (fun _ ↦ Nat.choose_zero_right _) at the sole bound caller and delete the wrapper in a future source refactor. Retaining it in the project-local Hasse package remains possible while the alias is kept; no standalone mathlib addition is needed.

Completed `MvPolynomial.hasseDeriv_zero_apply` action: BORDERLINE-needs-human: decide pointwise versus map-only zero API, naming, and dependency direction. If retaining, group with Hasse definition/coefficient API upstream work; if removing, independently prove bundled equality and migrate both Index simp sites. All formal checks complete; no production edits or decision needed to finish read-only overview.

Completed `MvPolynomial.hasseDeriv_zero` action: BORDERLINE-needs-human: closing-simp policy and bundled-versus-pointwise API choice. Keep project-local pending future design; if included, group with accepted Hasse definition and coefficient API in Mathlib/Algebra/MvPolynomial/HasseDeriv.lean. No user input needed to complete read-only assessment.

Completed `MvPolynomial.hasseDeriv_C` action: BORDERLINE-needs-human under closing-simp composition policy. Keep project-local pending named normalization/API choice. Potential Mathlib/Algebra/MvPolynomial/HasseDeriv.lean grouping with accepted parent; if omitted upstream, inline verified affected branch using local scalar-zero proof.

## Recommended action plan

1. Retain the useful local coefficient alias while assessing the complete Hasse API.
2. Do not submit a standalone PR for this direct two-operation definition.
3. Prepare the multivariate Hasse operator for a future coherent mathlib contribution; assess
   `MvPolynomial.hasseDeriv_map` next. Supporting identities receive their own applicable checks.
4. Preserve all per-declaration query/proof/log evidence and publish only accepted complete assessments.
5. Keep production Lean sources and pins unchanged; use a warm server and bounded, batched scratch checks.
