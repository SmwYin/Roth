# Project overview: Roth

Updated: 2026-10-26. **IN PROGRESS — 25/293 declaration assessments complete.**

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
- Completed applicable assessments: 25; remaining: 268.
- Verdicts: 4 NO-composable-from-mathlib, 11 YES-add-as-is, 0 YES-but-generalise-first, 0 NO-mathlib-has-it, 7 BORDERLINE-needs-human, 3 SKIP.
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

### Completed: `MvPolynomial.hasseDeriv_map`

- Type: `theorem: ∀ f : R →+* S, ∀ d P, hasseDeriv d (map f P) = map f (hasseDeriv d P)`
- What: Hasse derivatives commute with arbitrary coefficient ring homomorphisms.
- How: Coefficient extensionality, coefficient Hasse/map formulas, preservation of natural-number casts and multiplication.
- Hypotheses: Arbitrary variable type; independent commutative semirings R/S; any ring hom, multi-index and polynomial.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.coeff_hasseDeriv
- Caller summary: Seven explicit uses in five declarations: Separation533; Theta524/580; MainLemma409/489/492/495. Scoped context/nesting experiments only.
- Verdict: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_map.md).

### Completed: `MvPolynomial.hasseDeriv_rename`

- Type: `theorem: ∀ hf : Function.Injective f, ∀ d P, hasseDeriv (d.mapDomain f) (rename f P) = rename f (hasseDeriv d P)`
- What: Hasse derivatives commute with injective variable renaming when the multi-index is transported along the same injection.
- How: Monomial/additive induction; binomial product transport and mapDomain truncated subtraction compatibility.
- Hypotheses: Independent arbitrary variable types σ/τ, CommSemiring R, any injective f, finite multi-index d and polynomial P.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseDeriv_monomial, MvPolynomial.hasseCoeff
- Caller summary: One explicit call in Roth.hasseDeriv_rename_mul_aeval, Separation165; no internal uses; indirect Separation365 not counted.
- Verdict: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_rename.md).

### Completed: `MvPolynomial.hasseCoeff_mul_hasseCoeff`

- Type: `private lemma hasseCoeff_mul_hasseCoeff (f d e : σ →₀ ℕ) :
    hasseCoeff d (f + d) * hasseCoeff e (f + d + e) =
      hasseCoeff d (d + e) * hasseCoeff (d + e) (f + (d + e)); section {σ : Type*}; no coefficient-ring assumption`
- What: Proves the multiplicative binomial identity underlying composition of divided derivatives.
- How: Enlarges four Finsupp products to the union of the two differentiation supports using Finsupp.prod_of_support_subset, distributes products, then applies Nat.choose_mul coordinatewise and Nat.choose_symm_add.
- Hypotheses: Three natural finitely supported multi-indices; no coefficient-ring assumption.
- Project dependencies: MvPolynomial.hasseCoeff
- Caller summary: Two explicit same-file callers: hasseDeriv_hasseDeriv at179 and hasseCoeff_mul_succ at195. No explicit external source references; source-level scope only.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_mul_hasseCoeff.md).

### Completed: `MvPolynomial.hasseDeriv_hasseDeriv`

- Type: `∀ {σ R : Type*} [CommSemiring R] (d e : σ →₀ ℕ) (P : MvPolynomial σ R), hasseDeriv d (hasseDeriv e P) = (hasseCoeff d (d + e) : R) • hasseDeriv (d + e) P`
- What: Composing Hasse derivatives adds orders with product-binomial scalar.
- How: Coefficient comparison plus finite-support product Nat.choose_mul cocycle.
- Hypotheses: MAXIMALLY GENERAL for pinned canonical interface: CommSemiring, arbitrary variable types, indices and polynomial; literal Semiring parent fails.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseCoeff, MvPolynomial.coeff_hasseDeriv, private hasseCoeff_mul_hasseCoeff
- Caller summary: Two explicit invocations: HasseDeriv187 and Index113; both scoped algebra contexts verified, not full Index rebuild or implicit dependency closure.
- Verdict: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_hasseDeriv.md).

### Completed: `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`

- Type: `∀ {σ R : Type*} [CommSemiring R] {d e : σ →₀ ℕ}, Disjoint d.support e.support → ∀ P : MvPolynomial σ R, hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P`
- What: Hasse derivatives in disjoint variable supports compose with no binomial scalar.
- How: General iterativity then support-disjoint finite-product factors equal1.
- Hypotheses: MAXIMALLY GENERAL for geometric support-separation corollary; scalar-cast-one criterion verified strictly weaker in characteristic2 and already subsumed by unrestricted parent law.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseCoeff, MvPolynomial.hasseDeriv_hasseDeriv
- Caller summary: One explicit invocation at Separation156, Option.some/none support proof and reverse rewrite verified as a scoped fragment.
- Verdict: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint.md).

### Completed: `MvPolynomial.hasseCoeff_mul_succ`

- Type: `private lemma hasseCoeff_mul_succ (j : σ) (d e : σ →₀ ℕ) :
    hasseCoeff d (e + Finsupp.single j 1 + d) * (e j + 1) =
      (d j + 1) * hasseCoeff (d + Finsupp.single j 1) (e + Finsupp.single j 1 + d); section {σ : Type*}, no coefficient-ring assumption`
- What: Proves the single-coordinate successor form of the binomial composition identity.
- How: Specializes hasseCoeff_mul_hasseCoeff to the one-coordinate multi-index and simplifies the single-support binomial factors.
- Hypotheses: Natural finitely supported indices and a distinguished variable; no ring assumptions.
- Project dependencies: MvPolynomial.hasseCoeff, MvPolynomial.hasseCoeff_mul_hasseCoeff
- Caller summary: One explicit same-file caller pderiv_hasseDeriv at205; no external explicit source references.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_mul_succ.md).

### Completed: `MvPolynomial.pderiv_hasseDeriv`

- Type: `∀ {σ R : Type*} [CommSemiring R] (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R), pderiv j (hasseDeriv d P) = ((d j + 1 : ℕ) : R) • hasseDeriv (d + Finsupp.single j 1) P`
- What: Ordinary partial differentiation increments the Hasse multi-order with its necessary successor scalar.
- How: Coefficient extensionality and product-binomial successor recurrence.
- Hypotheses: MAXIMALLY GENERAL for canonical pinned polynomial/pderiv interface; arbitrary variables, semiring, order and input. Literal Semiring parent fails.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.coeff_hasseDeriv, private hasseCoeff_mul_succ
- Caller summary: Two direct invocations: HasseDeriv291 full factorial induction replay; GenWronskian159 scoped aeval scalar extraction only.
- Verdict: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.pderiv_hasseDeriv.md).

### Completed: `MvPolynomial.degreeOf_hasseDeriv_le`

- Type: `theorem: coordinate natural degree nonincrease under arbitrary-order multivariate Hasse derivative`
- What: deg_j Δ_dP ≤deg_jP for arbitrary σ and commutative semiring R, including zero.
- How: A nonzero output coefficient at m implies a nonzero input coefficient at m+d; apply coordinate-degree support bound.
- Hypotheses: arbitrary σ,R, CommSemiring R parent interface, j:σ, d:σ→₀ℕ, arbitrary P; no finiteness/characteristic/nonzero conditions
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.coeff_hasseDeriv
- Caller summary: Five invocations, CoeffNorm253 and MainLemma465/467/491/504; shared arbitrary-r transitivity checked, not whole downstream modules rebuilt.
- Verdict: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.degreeOf_hasseDeriv_le.md).

### Completed: `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`

- Type: `theorem: coordinate degree below multi-index implies multivariate Hasse derivative zero`
- What: If degreeOf j P < d j for any coordinate j, Δ_dP=0.
- How: Each derivative coefficient comes from exponent e+d, excluded from input support by the strict degree bound.
- Hypotheses: arbitrary σ,R with CommSemiring R, j:σ,d:σ→₀ℕ,P arbitrary, degreeOf j P < d j
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.coeff_hasseDeriv
- Caller summary: Three explicit invocations Taylor173/207, MainLemma425. Full degreeOf_taylor_le replay and generic outside-box evalzero/evalnonzero-degree-bound fragments verified.
- Verdict: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt.md).

### Completed: `MvPolynomial.hasseDeriv_monomial_mul`

- Type: `private lemma hasseDeriv_monomial_mul {d a : σ →₀ ℕ} (ha : ∀ j ∈ d.support, a j = 0) (c : R)
    (g : MvPolynomial σ R) : hasseDeriv d (monomial a c * g) = monomial a c * hasseDeriv d g; section {σ R : Type*} [CommSemiring R]`
- What: A scalar monomial supported away from the differentiation coordinates passes unchanged through the Hasse derivative of a product.
- How: Additive monomial induction and hasseDeriv_monomial reduce to exponent subtraction; a coordinate split proves a+b-d=a+(b-d), while the support-disjoint condition preserves hasseCoeff.
- Hypotheses: Commutative coefficients and a monomial exponent that vanishes on the differentiation support.
- Project dependencies: MvPolynomial.hasseCoeff, MvPolynomial.hasseDeriv_monomial
- Caller summary: One explicit same-file invocation in hasseDeriv_mul_of_degreeOf_eq_zero at246; no explicit external helper invocation.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_monomial_mul.md).

### Completed: `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`

- Type: `theorem`
- What: A factor independent of all variables in d.support passes through the canonical multi-index Hasse derivative.
- How: Expand f into monomials; degree-zero gives exponent zero in differentiated variables; prove monomial compatibility then extend by linearity.
- Hypotheses: arbitrary variable type and coefficient type, CommSemiring R, d finitely supported natural multi-index, forall j in d.support, degreeOf j f=0
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseCoeff, MvPolynomial.hasseDeriv_monomial, MvPolynomial.hasseDeriv_monomial_mul (private)
- Caller summary: count: 2; files: Roth/Separation.lean; locations: Roth/Separation.lean:157, Roth/Separation.lean:161; owner: Roth.hasseDeriv_rename_mul_aeval; effect: Pass complementary-variable factors through none-block and some-block Hasse operators; used in determinant separation.
- Verdict: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero.md).

### Completed: `MvPolynomial.hasseDeriv_single_aeval_X`

- Type: `theorem`
- What: The coordinate embedding of univariate polynomials intertwines Hasse derivatives.
- How: Additive/monomial induction; alternatively existing monomial-basis extensionality and closing definition simp.
- Hypotheses: arbitrary sigma and R universes, CommSemiring R, j : sigma, n : Nat, f : Polynomial R
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseDeriv_monomial, MvPolynomial.hasseCoeff
- Caller summary: count: 1; sites: Roth/Separation.lean:160; detail: Roth.hasseDeriv_rename_mul_aeval uses j=none; compiled literal instance.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_single_aeval_X.md).

### Completed: `MvPolynomial.uniqueAlgEquiv_hasseDeriv`

- Type: `theorem`
- What: Canonical identification of a singleton-variable polynomial algebra commutes with every Hasse derivative.
- How: Coefficient extensionality and singleton-binomial normalization; isolated raw basis proof also closes by definitions.
- Hypotheses: CommSemiring R, Unique σ
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.coeff_hasseDeriv, MvPolynomial.hasseCoeff
- Caller summary: count: 1; callers: Roth.index_unique at Roth/Index.lean:239; scope: explicit source references, not opaque kernel or simp closure
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.uniqueAlgEquiv_hasseDeriv.md).

### Completed: `MvPolynomial.hasseCoeff_le_two_pow`

- Type: `theorem`
- What: The natural binomial factor of a multivariate Hasse derivative is bounded by two to the sum of a degree box.
- How: Expand finite product, bound choose coordinatewise, lift through product monotonicity and normalize product of powers.
- Hypotheses: Fintype σ, d,k : σ →₀ ℕ, r : σ → ℕ, ∀ j,k j ≤ r j
- Project dependencies: MvPolynomial.hasseCoeff, MvPolynomial.hasseCoeff_eq_prod
- Caller summary: count: 2; callers: Roth.abs_coeff_hasseDeriv_le at Roth/CoeffNorm.lean:140, Roth.normOne_hasseDeriv_le at Roth/CoeffNorm.lean:157; scope: Explicit source references, not opaque kernel/simp closure
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_le_two_pow.md).

### Completed: `MvPolynomial.factorial_smul_hasseDeriv_single`

- Type: `theorem`
- What: n! times coordinate Hasse derivative equals iterated partial differentiation over any commutative semiring.
- How: Induct on order using scalar compatibility and pderiv_hasseDeriv recurrence.
- Hypotheses: Arbitrary σ,R, CommSemiring R, coordinate j, natural order n and polynomial P.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseDeriv_zero, MvPolynomial.pderiv_hasseDeriv
- Caller summary: 0 explicit proof callers; 1 module-doc reference; inline audit found no rederivation. Not opaque kernel dependency closure.
- Verdict: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.factorial_smul_hasseDeriv_single.md).

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

Completed `MvPolynomial.hasseDeriv_map`: Pinned Polynomial.hasseDeriv_map and MvPolynomial.pderiv_map are analogues, not all-multiorder arbitrary-variable replacements. Actual raw construction needs monomial calculation and additive induction.

Completed `MvPolynomial.hasseDeriv_rename`: Pinned pderiv_rename is first-order analogue; Finsupp.prod_mapDomain_index_inj/mapDomain_apply_of_injective/mapDomain_tsub supply individual monomial transports, not full Hasse identity.

Completed `MvPolynomial.hasseCoeff_mul_hasseCoeff`: Applicable private-helper triage: existing Nat.choose_mul/choose_symm_add and Finsupp support-product extension supply the scalar proof. Exact native replay validated. Full public mathlibable search n/a by private prefilter.

Completed `MvPolynomial.hasseDeriv_hasseDeriv`: Five actual search methods: univariate Polynomial.hasseDeriv_comp analogue is not arbitrary-variable replacement.

Completed `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`: All five actual methods on current/literature/abstract forms; univariate iteration is analogue only; lattice predicate equivalence verified.

Completed `MvPolynomial.hasseCoeff_mul_succ`: Private specialization of the shared binomial cocycle; native exact-body replay passes. Public mathlibable phase n/a by explicit private prefilter.

Completed `MvPolynomial.pderiv_hasseDeriv`: All five methods on three forms; pinned univariate analogue compiled but does not directly cover arbitrary multivariate inputs.

Completed `MvPolynomial.degreeOf_hasseDeriv_le`: Univariate natDegree_hasseDeriv_le exists at HasseDeriv179, generic degreeOf_le_iff/monomial_le_degreeOf support API at Degrees235/268; no arbitrary-variable bridge established.

Completed `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: Polynomial.hasseDeriv_eq_zero_of_lt_natDegree is univariate analogue; MvPolynomial.notMem_support_of_degreeOf_lt, notMem_support_iff and extensionality are generic blocks. No multivariate normalization supplied by ≤3 existing calls.

Completed `MvPolynomial.hasseDeriv_monomial_mul`: Existing polynomial induction/monomial product and support-product congruence prove the separated monomial step; exact native replay verified. Private-prefilter public search n/a.

Completed `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`: Univariate hasseDeriv_mul and first-order pderiv_mul are partial analogues; base-R map_smul cannot pass general undifferentiated polynomial factors. No existing multivariate bridge.

Completed `MvPolynomial.hasseDeriv_single_aeval_X`: All five methods on current/literature/abstract forms; positive toMvPolynomial and monomial/ext API, no existing Hasse bridge; local indexes unavailable.

Completed `MvPolynomial.uniqueAlgEquiv_hasseDeriv`: Univariate Hasse and canonical polynomial equivalence exist; no named pinned multivariate compatibility. All five methods on three forms; local index unavailable.

Completed `MvPolynomial.hasseCoeff_le_two_pow`: Five actual methods on three forms identify scalar choose bound and generic product/power infrastructure. Four substantive facts needed; local index unavailable.

Completed `MvPolynomial.factorial_smul_hasseDeriv_single`: Polynomial.factorial_smul_hasseDeriv and LaurentSeries.derivative_iterate are analogous different domains; commutative ideal DividedPowers not arbitrary operator composition.

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

Completed `MvPolynomial.hasseDeriv_map`: No verified replacement; analogous univariate and first-order naturality patterns.

Completed `MvPolynomial.hasseDeriv_rename`: No verified direct replacement; standard all-order extension of first-order injective renaming law.

Completed `MvPolynomial.hasseCoeff_mul_hasseCoeff`: Shared coordinatewise binomial cocycle used twice, no duplicated downstream scalar proof identified in source search.

Completed `MvPolynomial.hasseDeriv_hasseDeriv`: Divided-derivative iteration extends univariate composition; not automatic for arbitrary HS families.

Completed `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`: Support-separated corollary of new general composition; not a ≤3call composition from existing pinned mathlib.

Completed `MvPolynomial.hasseCoeff_mul_succ`: Isolates one-coordinate normalization for the sole partial/Hasse compatibility proof; no duplicated independent successor proof found in source audit.

Completed `MvPolynomial.pderiv_hasseDeriv`: Coordinate case of additive iterativity, extending univariate Hasse composition.

Completed `MvPolynomial.degreeOf_hasseDeriv_le`: Same degree-lowering idea as univariate Hasse bound; generic support-shift helper overlaps degreeOf support-sup infrastructure. Not a literal duplicate.

Completed `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: Same support-vanishing idea as univariate theorem; not a literal duplicate.

Completed `MvPolynomial.hasseDeriv_monomial_mul`: Monomial induction helper for public arbitrary-factor separation, no same-interface duplicate found by source audit.

Completed `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`: Constant-factor special case of future full multivariate Leibniz API, not a duplicate of the pinned univariate or ordinary derivative API.

Completed `MvPolynomial.hasseDeriv_single_aeval_X`: A short basis-ext and definition-simp proof exists; Phase6b review case.

Completed `MvPolynomial.uniqueAlgEquiv_hasseDeriv`: Equivalent to coordinate aeval compatibility in the unique-variable case, but that bridge is project API. Generic linear conjugacy needs normalization.

Completed `MvPolynomial.hasseCoeff_le_two_pow`: Hasse-named packaging of a finite-product natural combinatorial bound; not an exact named replacement claim.

Completed `MvPolynomial.factorial_smul_hasseDeriv_single`: Shared generic additive recurrence induction, compiled for Polynomial and MvPolynomial; no exact pinned replacement.

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

Completed `MvPolynomial.hasseDeriv_map`: Optional additive coefficient-map companion verified with AddMonoidAlgebra.map. Fixed RingHom map interface remains canonical and literature-compatible.

Completed `MvPolynomial.hasseDeriv_rename`: Actual collision counterexample proves global injectivity cannot simply be dropped; support-local injectivity plausible but no verified weakening. Embedding/square variants equivalent; literal Semiring interfaces fail.

Completed `MvPolynomial.hasseCoeff_mul_hasseCoeff`: Arbitrary variable type and natural multi-indices; no R/CommSemiring argument in actual replay type; no unverified wider cocycle claim.

Completed `MvPolynomial.hasseDeriv_hasseDeriv`: MAXIMALLY GENERAL for pinned canonical interface: CommSemiring, arbitrary variable types, indices and polynomial; literal Semiring parent fails.

Completed `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`: MAXIMALLY GENERAL for geometric support-separation corollary; scalar-cast-one criterion verified strictly weaker in characteristic2 and already subsumed by unrestricted parent law.

Completed `MvPolynomial.hasseCoeff_mul_succ`: Arbitrary variable type, distinguished variable and natural multi-indices; no ring assumptions in actual replay type.

Completed `MvPolynomial.pderiv_hasseDeriv`: MAXIMALLY GENERAL for canonical pinned polynomial/pderiv interface; arbitrary variables, semiring, order and input. Literal Semiring parent fails.

Completed `MvPolynomial.degreeOf_hasseDeriv_le`: All arguments already broad within parent CommSemiring interface; conclusion not maximally strong. Same-argument degree-minus-order bound verified and strictly improves X³ witness.

Completed `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: MAXIMALLY GENERAL fixed CommSemiring parent interface; strictness essential. Stronger support/coefficient zero criteria are companions; existential j wrapper syntactically equivalent.

Completed `MvPolynomial.hasseDeriv_monomial_mul`: Arbitrary variables and commutative semiring; arbitrary c,g; exponent separation on support d sufficient, no necessity or unverified weakening claimed.

Completed `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`: Current fixed-parent signature maximally general. Vars-disjoint equivalent and symmetric-side companion tested; abstract sum extension tested with actual compatibility premise.

Completed `MvPolynomial.hasseDeriv_single_aeval_X`: No verified weakening under canonical parent; bundled square is equivalent.

Completed `MvPolynomial.uniqueAlgEquiv_hasseDeriv`: No strict weakening verified; Subsingleton plus a chosen variable repackages Unique. Inverse/bundled forms equivalent.

Completed `MvPolynomial.hasseCoeff_le_two_pow`: Verified same conclusion with hk only on d.support; stronger support-sum form needs no Fintype. Raw finite-set form uses ordinary functions.

Completed `MvPolynomial.factorial_smul_hasseDeriv_single`: MAXIMALLY GENERAL for fixed CommSemiring MvPolynomial/pderiv interface; no verified literal weakening. Q8 fires; meaningful shared induction extraction compiled with two consumers, but not mandatory replacement of canonical coordinate compatibility theorem. Concrete recurrence obligations remain.

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

Completed `MvPolynomial.hasseDeriv_map`: Multivariate all-order divided derivative coefficient-change law beside the parent Hasse operator.

Completed `MvPolynomial.hasseDeriv_rename`: Injective-renaming naturality for all multivariate divided derivative orders.

Completed `MvPolynomial.hasseCoeff_mul_hasseCoeff`: No missing generic finite-product API needed here; public Hasse composition assessed separately.

Completed `MvPolynomial.hasseDeriv_hasseDeriv`: Canonical multivariate polynomial Hasse iterativity, analogous to Polynomial.hasseDeriv_comp but for finitely supported multi-orders.

Completed `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`: Canonical multivariate Hasse composition for disjoint differential supports, grouped with parent iterativity.

Completed `MvPolynomial.hasseCoeff_mul_succ`: Existing finite-product and choose simplification suffice; public partial/Hasse derivative compatibility assessed separately.

Completed `MvPolynomial.pderiv_hasseDeriv`: Canonical multivariate Hasse compatibility with ordinary pderiv in arbitrary characteristic.

Completed `MvPolynomial.degreeOf_hasseDeriv_le`: Coordinate-degree/degree-box preservation for canonical multivariate Hasse derivative, with sharp primary companion matching univariate degree-minus-order convention.

Completed `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: Coordinate-degree annihilation for canonical multivariate Hasse derivative; support and exact weighted-coefficient criteria useful companions.

Completed `MvPolynomial.hasseDeriv_monomial_mul`: Generic monomial/support infrastructure sufficient; public factor-separation operator API assessed next.

Completed `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`: Canonical multivariate Hasse factor-independence/relative-linearity rule; eventual full multi-index product formula.

Completed `MvPolynomial.hasseDeriv_single_aeval_X`: Public coordinate compatibility API for new multivariate Hasse derivatives, subject to packing decision.

Completed `MvPolynomial.uniqueAlgEquiv_hasseDeriv`: Public API choice for unique-variable Hasse transport beside proposed multivariate Hasse operator.

Completed `MvPolynomial.hasseCoeff_le_two_pow`: Design choice whether general Finset/Nat binomial-product estimate merits named upstream API.

Completed `MvPolynomial.factorial_smul_hasseDeriv_single`: Characteristic-free multivariate Hasse to iterated partial compatibility.

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

Completed `MvPolynomial.hasseDeriv_map`: False

Completed `MvPolynomial.hasseDeriv_rename`: False

Completed `MvPolynomial.hasseCoeff_mul_hasseCoeff`: Retain shared private helper, two real uses; no deletion/export recommended.

Completed `MvPolynomial.hasseDeriv_hasseDeriv`: No: canonical normalization used by disjoint law and index inequality.

Completed `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`: No: reusable geometric API supporting separated-variable determinant proof.

Completed `MvPolynomial.hasseCoeff_mul_succ`: Retain private descriptive two-line specialization, no source change recommended.

Completed `MvPolynomial.pderiv_hasseDeriv`: No: factorial iteration and generalized Wronskian recurrence use it.

Completed `MvPolynomial.degreeOf_hasseDeriv_le`: No: five direct invocations in two files, canonical common API.

Completed `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: No: reused in translation degree, finite Taylor expansion and index box restriction.

Completed `MvPolynomial.hasseDeriv_monomial_mul`: Retain focused private induction helper; one real use, no deletion/export recommended.

Completed `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`: No: two explicit calls in one theorem are essential steps toward separated determinant factorization.

Completed `MvPolynomial.hasseDeriv_single_aeval_X`: Not dead: one explicit consumer; no inline duplicate located.

Completed `MvPolynomial.uniqueAlgEquiv_hasseDeriv`: False

Completed `MvPolynomial.hasseCoeff_le_two_pow`: False

Completed `MvPolynomial.factorial_smul_hasseDeriv_single`: Unused explicitly in project; retain as standard canonical operator compatibility API, not evidence of hidden callers.

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
| 11 | `MvPolynomial.hasseDeriv_map` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_map.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_map/root-acceptance.json) |
| 12 | `MvPolynomial.hasseDeriv_rename` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_rename.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_rename/root-acceptance.json) |
| 13 | `MvPolynomial.hasseCoeff_mul_hasseCoeff` | SKIP | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_mul_hasseCoeff.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/root-acceptance.json) |
| 14 | `MvPolynomial.hasseDeriv_hasseDeriv` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_hasseDeriv.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_hasseDeriv/root-acceptance.json) |
| 15 | `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint/root-acceptance.json) |
| 16 | `MvPolynomial.hasseCoeff_mul_succ` | SKIP | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_mul_succ.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff_mul_succ/root-acceptance.json) |
| 17 | `MvPolynomial.pderiv_hasseDeriv` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.pderiv_hasseDeriv.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.pderiv_hasseDeriv/root-acceptance.json) |
| 18 | `MvPolynomial.degreeOf_hasseDeriv_le` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.degreeOf_hasseDeriv_le.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.degreeOf_hasseDeriv_le/root-acceptance.json) |
| 19 | `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/root-acceptance.json) |
| 20 | `MvPolynomial.hasseDeriv_monomial_mul` | SKIP | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_monomial_mul.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_monomial_mul/root-acceptance.json) |
| 21 | `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/root-acceptance.json) |
| 22 | `MvPolynomial.hasseDeriv_single_aeval_X` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseDeriv_single_aeval_X.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_single_aeval_X/root-acceptance.json) |
| 23 | `MvPolynomial.uniqueAlgEquiv_hasseDeriv` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.uniqueAlgEquiv_hasseDeriv.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/root-acceptance.json) |
| 24 | `MvPolynomial.hasseCoeff_le_two_pow` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_le_two_pow.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff_le_two_pow/root-acceptance.json) |
| 25 | `MvPolynomial.factorial_smul_hasseDeriv_single` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.factorial_smul_hasseDeriv_single.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.factorial_smul_hasseDeriv_single/root-acceptance.json) |

All remaining declarations are unfinished; none has an assigned final verdict here.

Completed `MvPolynomial.hasseDeriv_monomial` action: Retain local semantic simp helper during read-only overview; no standalone upstream addition. If future authorized wrapper removal, inline direct generic evaluation at seven explicit uses on five lines, update parent docstring, audit implicit simp use and rebuild.

Completed `MvPolynomial.hasseDeriv_apply` action: Retain production API during read-only overview. No standalone upstream theorem; if future wrapper removal authorized, inline the verified generic equality at the sole normOne caller, remove theorem and rebuild; package-level semantic API review remains separate.

Completed `MvPolynomial.hasseCoeff_eq_zero_iff` action: BORDERLINE-needs-human for upstream packaging and verified upper-function widening. Retain local theorem during read-only overview; all execution checks complete; proceed after root acceptance.

Completed `MvPolynomial.coeff_hasseDeriv` action: YES-add-as-is: include with multivariate Hasse operator in a focused upstream module; inline scalar alias in statement if hasseCoeff is omitted, retain shifted coefficient normal form.

Completed `MvPolynomial.hasseCoeff_eq_prod` action: NO-composable-from-mathlib: inline d.prod_fintype _ (fun _ ↦ Nat.choose_zero_right _) at the sole bound caller and delete the wrapper in a future source refactor. Retaining it in the project-local Hasse package remains possible while the alias is kept; no standalone mathlib addition is needed.

Completed `MvPolynomial.hasseDeriv_zero_apply` action: BORDERLINE-needs-human: decide pointwise versus map-only zero API, naming, and dependency direction. If retaining, group with Hasse definition/coefficient API upstream work; if removing, independently prove bundled equality and migrate both Index simp sites. All formal checks complete; no production edits or decision needed to finish read-only overview.

Completed `MvPolynomial.hasseDeriv_zero` action: BORDERLINE-needs-human: closing-simp policy and bundled-versus-pointwise API choice. Keep project-local pending future design; if included, group with accepted Hasse definition and coefficient API in Mathlib/Algebra/MvPolynomial/HasseDeriv.lean. No user input needed to complete read-only assessment.

Completed `MvPolynomial.hasseDeriv_C` action: BORDERLINE-needs-human under closing-simp composition policy. Keep project-local pending named normalization/API choice. Potential Mathlib/Algebra/MvPolynomial/HasseDeriv.lean grouping with accepted parent; if omitted upstream, inline verified affected branch using local scalar-zero proof.

Completed `MvPolynomial.hasseDeriv_map` action: YES-add-as-is; group with hasseDeriv and coeff_hasseDeriv in Mathlib/Algebra/MvPolynomial/HasseDeriv.lean; generalise/cleanup and current-pin duplicate check before PR.

Completed `MvPolynomial.hasseDeriv_rename` action: YES-add-as-is; group with accepted multivariate Hasse parent/coefficient/map API in Mathlib/Algebra/MvPolynomial/HasseDeriv.lean; generalise/cleanup and fresh duplicate check before PR.

Completed `MvPolynomial.hasseCoeff_mul_hasseCoeff` action: SKIP-private under overview Step9a; completed inventory/structural triage and verification, no full public-contribution verdict. Keep production sources unchanged and continue next canonical declaration.

Completed `MvPolynomial.hasseDeriv_hasseDeriv` action: YES-add-as-is grouped in Mathlib/Algebra/MvPolynomial/HasseDeriv.lean; run generalise/cleanup; private cocycle remains overview SKIP.

Completed `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` action: YES-add-as-is with parent multivariate API; run generalise and cleanup, optionally bundle; retain geometric support interface.

Completed `MvPolynomial.hasseCoeff_mul_succ` action: SKIP-private under overview9a; complete applicable inventory/structural review, exact proof replay and evidence; continue with pderiv_hasseDeriv.

Completed `MvPolynomial.pderiv_hasseDeriv` action: YES-add-as-is grouped with canonical multivariate Hasse construction/coefficient/naturality/composition API; run generalise and cleanup before upstream PR.

Completed `MvPolynomial.degreeOf_hasseDeriv_le` action: YES-add-as-is weak corollary with sharp primary companion and coherent parent/API PR; run generalise and cleanup; no production change authorized by this assessment.

Completed `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` action: YES-add-as-is with parent operator and coefficient API, optional support/exact coefficient criteria, generalise and cleanup before upstream PR.

Completed `MvPolynomial.hasseDeriv_monomial_mul` action: SKIP-private under overview9a; complete applicable inventory, structural triage, exact proof replay and evidence. Continue with public factor-separation theorem.

Completed `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` action: YES-add-as-is; retain source calls, contribute with canonical multivariate Hasse API; keep monomial helper private and consider vars/right-factor corollaries after cleanup.

Completed `MvPolynomial.hasseDeriv_single_aeval_X` action: BORDERLINE-needs-human: settle three public API questions; retain local theorem meanwhile, or localize verified basis proof at Separation:160.

Completed `MvPolynomial.uniqueAlgEquiv_hasseDeriv` action: BORDERLINE: retain locally pending three upstream API questions; if omitted inline exact local bridge at the single Index caller.

Completed `MvPolynomial.hasseCoeff_le_two_pow` action: BORDERLINE: retain locally pending three concrete API questions; migrate both CoeffNorm consumers if later wrapper omitted.

Completed `MvPolynomial.factorial_smul_hasseDeriv_single` action: YES-add-as-is; upstream with base Hasse and pderiv recurrence family, optional common induction helper.

## Recommended action plan

1. Retain the useful local coefficient alias while assessing the complete Hasse API.
2. Do not submit a standalone PR for this direct two-operation definition.
3. Prepare the multivariate Hasse operator for a future coherent mathlib contribution; assess
   `Roth.box` next. Supporting identities receive their own applicable checks.
4. Preserve all per-declaration query/proof/log evidence and publish only accepted complete assessments.
5. Keep production Lean sources and pins unchanged; use a warm server and bounded, batched scratch checks.
