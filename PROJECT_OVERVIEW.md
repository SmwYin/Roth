# Project overview: Roth

Updated: 2026-10-26. **IN PROGRESS — 190/293 declaration assessments complete.**

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
- Completed applicable assessments: 190; remaining: 103.
- Verdicts: 19 NO-composable-from-mathlib, 13 YES-add-as-is, 25 YES-but-generalise-first, 43 NO-mathlib-has-it, 57 BORDERLINE-needs-human, 33 SKIP.
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

### Completed: `Roth.box`

- Type: `{σ : Type u} → [Fintype σ] → [DecidableEq σ] → (σ → ℕ) → Finset (σ →₀ ℕ)`
- What: Finite coordinatewise bounded natural multi-indices.
- How: piFinset of ranges mapped through inverse finite-function/Finsupp equivalence.
- Hypotheses: Fintype σ and DecidableEq σ for literal enumeration; both mechanically weakenable noncomputably, r : σ → ℕ; no positivity or nonempty assumption
- Project dependencies: None
- Caller summary: 22 direct code lines outside Box, in Lattice/CoeffNorm/Taylor/Main/MainLemma; additional mem/card consumers fully mapped; source counts only.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.box.md).

### Completed: `Roth.weight`

- Type: `{σ : Type u} → [Fintype σ] → (σ → ℕ) → (σ →₀ ℕ) → ℝ`
- What: Real reciprocal-parameter weight of a natural multi-index.
- How: Full ambient finite sum of d_j/r_j; totalized division permits zero denominators.
- Hypotheses: Finite variable enumeration, natural parameter vector and natural Finsupp; no positivity or DecidableEq.
- Project dependencies: None
- Caller summary: 30 explicit source caller declarations, nine in Box; active local API, no dead-code claim; not a kernel/simp closure.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight.md).

### Completed: `Roth.mem_box`

- Type: `theorem`
- What: Membership in the finite box iff coordinatewise natural bounds.
- How: Transport equivalence membership, Cartesian product membership, natural range successor bound.
- Hypotheses: σ universe polymorphic, Fintype σ, DecidableEq σ, r : σ → ℕ, d : σ →₀ ℕ
- Project dependencies: Roth.box
- Caller summary: 9 explicit references in7 declaration callers,8 external references across5 files.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.mem_box.md).

### Completed: `Roth.card_box`

- Type: `theorem`
- What: Counts bounded natural multi-indices as product of coordinate sizes.
- How: Map cardinality, dependent finite-product cardinality, natural range cardinality.
- Hypotheses: Universe-polymorphic σ; Fintype σ; DecidableEq σ parent-interface; arbitrary r:σ→ℕ.
- Project dependencies: Roth.box
- Caller summary: 3 source occurrences: card_le_card_box, private lattice count helper, abs_eval_lt_of_le_index; 2 external files.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_box.md).

### Completed: `Roth.card_le_card_box`

- Type: `theorem`
- What: Distinct natural multiindices bounded coordinatewise by r have cardinality at most product(rj+1).
- How: Containment in finite coordinate product, or independent injective Fin-valued tuple representation.
- Hypotheses: arbitrary universe polymorphic σ, Fintype σ, r:σ→ℕ, s:Finset(σ→₀ℕ), ∀d∈s,j,dj≤rj; no public DecidableEq
- Project dependencies: Roth.mem_box, Roth.card_box
- Caller summary: count: 2; files: Roth/CoeffNorm.lean:264, Roth/MainLemma.lean:506; native tests: Both degreeOf-to-real-cardinality consumer formats verified using independent injection.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_le_card_box.md).

### Completed: `Roth.weight_nonneg`

- Type: `theorem`
- What: Every natural multi-index has nonnegative real reciprocal-parameter weight, allowing zero parameters.
- How: Finite sum of nonnegative quotients; natural-cast nonnegativity supplies both coordinates.
- Hypotheses: arbitrary universe-polymorphic type sigma, Fintype sigma, r:sigma to Nat, d:sigma finitely supported Nat; no positivity premise
- Project dependencies: Roth.weight (definition only)
- Caller summary: occurrences: 3; declarations: 3; files: Roth/Lattice.lean:145, Roth/Index.lean:94, Roth/Theta.lean:395; simp attribute: False; opaque dependency closure claimed: False
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_nonneg.md).

### Completed: `Roth.weight_zero`

- Type: `theorem`
- What: The zero natural multi-index has real weight zero for any natural parameter family.
- How: Finite sum of zeros using cast-zero and zero-division; source simp [weight].
- Hypotheses: Arbitrary σ with Fintype, No positive/nonzero denominator or DecidableEq premise
- Project dependencies: Roth.weight
- Caller summary: 0 explicit named references; @[simp] may normalize weight r 0 implicitly; Index.index_eq_zero_iff:105 potential consumer.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_zero.md).

### Completed: `Roth.weight_add`

- Type: `theorem`
- What: Real reciprocal-denominator weight is additive in natural exponent vectors.
- How: Nat.cast_add, add_div, and Finset.sum_add_distrib; independently verified explicit term.
- Hypotheses: Universe-polymorphic σ, Fintype σ, r : σ → ℕ, d e : σ →₀ ℕ; no positivity or DecidableEq.
- Project dependencies: Roth.weight
- Caller summary: 3 explicit source callers: Roth/Lattice.lean:155, Roth/Index.lean:114, Roth/Theta.lean:391; all three weight substitution shapes native-verified.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_add.md).

### Completed: `Roth.weight_eq_zero_iff`

- Type: `theorem`
- What: Positive reciprocal natural weights detect exactly the zero natural multi-index.
- How: Finite nonnegative sum zero iff every quotient zero, nonzero denominators and natural casts, finsupp extensionality.
- Hypotheses: Fintype σ fixed by parent; positivity globally can localize to d.support (verified); no DecidableEq.
- Project dependencies: Roth.weight
- Caller summary: One explicit caller Index.index_eq_zero_iff:102; no simp attribute; no inline duplicate found.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_eq_zero_iff.md).

### Completed: `Roth.weight_single`

- Type: `theorem`
- What: A single-coordinate multi-index has weight n/r j, with real division.
- How: Unfold finite weighted sum, evaluate the single coordinate; independently checked support-sum composition uses four distinct facts including cast-zero and zero-division.
- Hypotheses: Universe-polymorphic sigma with Fintype; r:sigma→Nat, j:sigma, n:Nat. No DecidableEq or denominator positivity.
- Project dependencies: Roth.weight
- Caller summary: explicit: 2; sites: Roth/Lattice.lean:155 card_filter_fiber_eq, Roth/Theta.lean:391 sum_max_sub_le_index_det; kernel closure not counted: True
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_single.md).

### Completed: `Roth.weight_le_card`

- Type: `theorem`
- What: A bounded normalized natural multi-index has real weight at most the number of variables.
- How: Bound each nonnegative-denominator ratio by one and sum.
- Hypotheses: Fintype variable type, natural denominators and finitely supported natural coefficients; all coordinates bounded. No strict positivity or public DecidableEq.
- Project dependencies: Roth.weight
- Caller summary: explicit count: 1; callers: {'name': 'Roth.index_le_card', 'file': 'Roth/Index.lean', 'line': 227}; inline derivations found: 0; not kernel or simp closure: True
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_le_card.md).

### Completed: `Roth.weight_mul_left`

- Type: `{σ : Type u} → [Fintype σ] → {l : ℕ} → (r : σ → ℕ) → (d : σ →₀ ℕ) → Roth.weight (fun j ↦ l * r j) d = Roth.weight r d / ↑l`
- What: Uniformly multiplying denominator parameters divides monomial weight by that scale.
- How: Cast product, distribute division over sum, reassociate division, commute denominator factors.
- Hypotheses: Finite variable enumeration; arbitrary natural scale and parameter family including zeros; no positivity or DecidableEq.
- Project dependencies: Roth.weight
- Caller summary: One explicit caller Roth.index_mul_left_weights at Index.lean:206; native complete Set.image equality fragment verified. Source references only, not kernel/simp closure.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_mul_left.md).

### Completed: `Roth.weight_le_degree_div`

- Type: `∀ {σ : Type u} [Fintype σ] {r : σ → ℕ} {m : ℕ}, 0 < m → (∀ j : σ, m ≤ r j) → ∀ d : σ →₀ ℕ, Roth.weight r d ≤ (Finsupp.degree d : ℝ) / (m : ℝ)`
- What: Bounds a multi-index reciprocal weight by total degree divided by a positive common lower bound on denominators.
- How: Rewrite degree as coordinate sum, cast and distribute division; use sum monotonicity and division antitonicity in positive denominators.
- Hypotheses: Fintype variable enumeration; natural denominators; positive natural m; all r_j at least m; natural finitely supported multi-index. No DecidableEq needed.
- Project dependencies: Roth.weight
- Caller summary: Zero explicit source callers; no simp tag. Related Theta.lean494-508 real-ratio bound reuses proof technique but is not the exact statement or a migrated consumer.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_le_degree_div.md).

### Completed: `Roth.weight_mapDomain`

- Type: `∀ {σ : Type u_3} [Fintype σ] {τ : Type u_4} [Fintype τ] {f : σ → τ}, Function.Injective f → ∀ (r : τ → ℕ) (d : σ →₀ ℕ), Roth.weight r (Finsupp.mapDomain f d) = Roth.weight (r ∘ f) d`
- What: Weighted evaluation of a multi-index is preserved by injective relabelling with pulled-back denominator parameters; actually arbitrary maps work.
- How: Original proof applies sum_mapDomain_index_inj then normalizes Finsupp.sum to the finite ambient sum. Re-aimed proof is exact existing linearCombination_mapDomain.
- Hypotheses: Fintype σ and Fintype τ required by fixed parent weight interface, Injective f removable, natively verified, no DecidableEq, positivity, or nonzero denominator assumptions
- Project dependencies: Roth.weight
- Caller summary: explicit references: 3; files: Roth/Lattice.lean:155, Roth/Index.lean:219, Roth/Theta.lean:391; inline duplicates: 0; scope: source-level explicit references, not kernel/simp closure
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_mapDomain.md).

### Completed: `Roth.wronskianMatrix`

- Type: `{K : Type u_1} → [inst : Field K] → {l : ℕ} → (Fin l → K[X]) → Matrix (Fin l) (Fin l) K[X]`
- What: Square matrix of successive univariate Hasse derivatives of a polynomial family.
- How: Matrix.of bundles (μ,ν) ↦ Polynomial.hasseDeriv μ (φ ν).
- Hypotheses: Universe-polymorphic K with Field K, mechanically weakenable to Semiring., Implicit length l : ℕ; explicit φ : Fin l → Polynomial K., No characteristic, independence, nonzero or positive-length assumption.
- Project dependencies: None
- Caller summary: declarations: 6; executable occurrences: 7; external to declaring file occurrences: 2; external files: 2; scope: Explicit source references only; not kernel/simp closure.; callers: {'name': 'Roth.wronskian_kronecker_eq_sum_aux', 'file': 'Roth/GenWronskian.lean', 'line': 238}, {'name': 'Roth.det_hasseDeriv_separated', 'file': 'Roth/Separation.lean', 'line': 351}, {'name': 'Roth.wronskian', 'file': 'Roth/Wronskian.lean', 'line': 60}, {'name': 'Roth.wronskian_eq_zero_of_not_linearIndependent', 'file': 'Roth/Wronskian.lean', 'line': 65}, {'name': 'Roth.coeff_wronskian_of_natDegree_injective', 'file': 'Roth/Wronskian.lean', 'line': 122}, {'name': 'Roth.wronskian_update_sub_smul', 'file': 'Roth/Wronskian.lean', 'line': 158}
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskianMatrix.md).

### Completed: `Roth.wronskian`

- Type: `@Roth.wronskian : {K : Type u_1} → [inst : Field K] → {l : ℕ} → (Fin l → K[X]) → K[X]`
- What: Determinant of consecutive Hasse derivatives of a finite polynomial family.
- How: Matrix.det of Roth.wronskianMatrix; exact expanded mathlib expression verified.
- Hypotheses: Field K in unchanged parent interface, implicit l : ℕ, arbitrary including0, explicit φ : Fin l → K[X]
- Project dependencies: Roth.wronskianMatrix
- Caller summary: 13 executable occurrences in9 caller declarations;5 in3 declarations outside declaring module,2 files. Source-level audit only.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian.md).

### Completed: `Roth.wronskian_eq_zero_of_not_linearIndependent`

- Type: `∀ {K : Type u_1} [inst : Field K] {l : ℕ} {φ : Fin l → Polynomial K}, ¬ LinearIndependent K φ → Roth.wronskian φ = 0`
- What: Coefficient-field linear dependence forces zero finite Hasse Wronskian.
- How: Extract nontrivial constant relation; Hasse linearity gives nonzero polynomial kernel vector; determinant vanishes. Verified improved four-call column-independence/scalar-restriction proof.
- Hypotheses: Field K, finite length l, family φ, ¬ LinearIndependent K φ
- Project dependencies: Roth.wronskian, Roth.wronskianMatrix
- Caller summary: explicit uses: 1; external to declaring file uses: 0; callers: Roth/Wronskian.lean:222 (wronskian_eq_zero_iff); inline analogues: Roth/GenWronskian.lean:40–50 (multivariate; different representation); caller experiment: PASS fragment; no production migration
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian_eq_zero_of_not_linearIndependent.md).

### Completed: `Roth.det_choose_eq`

- Type: `∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K] (d : Fin l → ℕ), (Matrix.of fun μ ν : Fin l ↦ ((d ν).choose μ : K)).det = (∏ μ : Fin l, ((μ : ℕ).factorial : K)⁻¹) * ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, ((d j : K) - d i)`
- What: Evaluates the natural-binomial matrix determinant as the Vandermonde difference product divided by the product of row factorials.
- How: Proves the entrywise falling-factorial evaluation/row-scaling bridge, then uses det scaling, transpose, existing monic evaluation determinant law and det_vandermonde.
- Hypotheses: Field K; CharZero K; arbitrary l and natural tops d. CharZero can be replaced by local factorial nonvanishing; arbitrary CommRing cancellation-free form is also verified.
- Project dependencies: None
- Caller summary: explicit proof callers: 1; within file: 1; outside file: 0; command internal K excluding declaring file: 0; callers: {'file': 'Roth/Wronskian.lean', 'line': 151, 'name': 'Roth.wronskian_ne_zero_of_natDegree_injective', 'pattern': 'simp rewrite in top-coefficient nonvanishing proof'}; opaque kernel simp closure claimed: False
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.det_choose_eq.md).

### Completed: `Roth.coeff_prod_of_natDegree_le'`

- Type: `{K : Type*} [Field K] {ι : Type*} (s : Finset ι) (f : ι → K[X]) (n : ι → ℕ) (h : ∀ i ∈ s, (f i).natDegree ≤ n i) : (∏ i ∈ s, f i).coeff (∑ i ∈ s, n i) = ∏ i ∈ s, (f i).coeff (n i)`
- What: Boundary coefficient of a finite polynomial product with per-factor degree bounds is the product of boundary coefficients.
- How: Finite-set induction, two-factor coefficient identity and product-degree bound.
- Hypotheses: Field source interface, same proof verified over CommSemiring. Arbitrary ambient indices and per-factor natural bounds on the finite set.
- Project dependencies: None
- Caller summary: One explicit same-file call at131 inside coeff_wronskian_of_natDegree_injective; no external calls.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_prod_of_natDegree_le'.md).

### Completed: `Roth.sum_range_le_sum_of_injective`

- Type: `∀ {l : ℕ} (d : Fin l → ℕ), Function.Injective d → (∑ ν : Fin l, (ν : ℕ)) ≤ ∑ ν, d ν`
- What: Any l distinct natural numbers have sum at least 0+1+⋯+(l−1).
- How: Embed the finite image into ℤ, apply Finset.sum_range_le_sum at c=0, normalize image cardinality/sums and reflect the inequality through casts.
- Hypotheses: {l : ℕ}, d : Fin l → ℕ, Function.Injective d. No coefficient field or characteristic binder.
- Project dependencies: None
- Caller summary: explicit source callers: None; count: 0; inline rederivations: 0; scope: Source-level explicit references only; no exhaustive kernel/simp closure claim. No simp attribute on target.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.sum_range_le_sum_of_injective.md).

### Completed: `Roth.coeff_wronskian_of_natDegree_injective`

- Type: `∀ {K : Type u} [Field K] {l : ℕ} {φ : Fin l → K[X]}, (Roth.wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) = (∏ ν, (φ ν).leadingCoeff) * (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : K)).det`
- What: Computes the coefficient at the top possible degree of a finite polynomial Hasse Wronskian as product of leading coefficients times a binomial determinant.
- How: Computes each permutation-product coefficient using individual Hasse degree bounds; excessive derivative orders make both sides zero; sums the signed determinant expansions.
- Hypotheses: Arbitrary polynomial family over a field; no nonzero, distinct-degree, CharZero, independence, or positive-size premise.
- Project dependencies: Roth.wronskian, Roth.wronskianMatrix, Roth.coeff_prod_of_natDegree_le'
- Caller summary: One explicit same-file proof caller: Wronskian.lean:152 in wronskian_ne_zero_of_natDegree_injective; no external-file callers; implementation-note prose excluded; not a kernel/simp dependency closure.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_wronskian_of_natDegree_injective.md).

### Completed: `Roth.wronskian_ne_zero_of_natDegree_injective`

- Type: `∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K]
  {φ : Fin l → K[X]}, (∀ (ν : Fin l), φ ν ≠ 0) → (Function.Injective fun ν ↦ (φ ν).natDegree) → Roth.wronskian φ ≠ 0`
- What: Nonzero polynomials of distinct degrees have nonzero normalized Hasse Wronskian in characteristic zero.
- How: One coefficient equals product of leading coefficients times a binomial determinant; Vandermonde gives nonvanishing.
- Hypotheses: Field K, CharZero K, all family members nonzero, natural-degree function injective
- Project dependencies: Roth.wronskian, Roth.coeff_wronskian_of_natDegree_injective, Roth.det_choose_eq
- Caller summary: total explicit proof callers: 1; within file: 1; outside file: 0; internal use count excluding declaring file: 0; callers: Roth/Wronskian.lean:210 Roth.wronskian_ne_zero_of_linearIndependent; inline rederivations: None
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian_ne_zero_of_natDegree_injective.md).

### Completed: `Roth.wronskian_update_sub_smul`

- Type: `∀ {K : Type u_1} [Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l}, ν ≠ ν' → ∀ (c : K), Roth.wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = Roth.wronskian φ`
- What: Subtracting a constant multiple of one distinct family member preserves its Hasse-Wronskian.
- How: Identify the updated Hasse matrix entrywise using coefficient linearity, then apply Matrix.det_updateCol_add_smul_self with negative constant scalar.
- Hypotheses: Field K fixed by parent interface; distinct Fin l indices; any constant c. No CharZero, independence, degree or nonzero assumptions.
- Project dependencies: Roth.wronskian, Roth.wronskianMatrix
- Caller summary: One explicit executable reference, Wronskian.lean:212 inside wronskian_ne_zero_of_linearIndependent; no external-to-file callers; documentation reference at 38 excluded.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian_update_sub_smul.md).

### Completed: `Roth.linearIndependent_update_sub_smul`

- Type: `∀ {K : Type u_1} [Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l}, ν ≠ ν' → ∀ c : K, LinearIndependent K φ → LinearIndependent K (Function.update φ ν' (φ ν' - Polynomial.C c * φ ν))`
- What: Elementary column subtraction preserves independence of a polynomial family.
- How: Rewrite independence as family cardinality equals span finrank; use span_range_update_sub_smul.
- Hypotheses: Field K (weakenable to Ring/module), distinct source/destination (necessary uniformly), initial independence (necessary)
- Project dependencies: None
- Caller summary: total explicit: 2; internal excluding declaring file: 0; external files: 0; callers: Roth.sum_natDegree_update_lt:190, Roth.wronskian_ne_zero_of_linearIndependent:214; verified rebuilds: True
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.linearIndependent_update_sub_smul.md).

### Completed: `Roth.sum_natDegree_update_lt`

- Type: `∀ {K : Type u} [Field K] {l : ℕ} {φ : Fin l → K[X]}, LinearIndependent K φ → ∀ {ν ν' : Fin l}, ν ≠ ν' → (φ ν).natDegree = (φ ν').natDegree → ∑ ρ, (Function.update φ ν' (φ ν' - C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν) ρ).natDegree < ∑ ρ, (φ ρ).natDegree`
- What: Cancelling equal leading terms strictly lowers the sum of degrees of an independent finite polynomial family.
- How: Prove updated difference nonzero, cancel leading coefficients, convert degree to natDegree, apply Finset.sum_lt_sum.
- Hypotheses: Field K, LinearIndependent K φ, distinct indices, equal natural degrees
- Project dependencies: Roth.linearIndependent_update_sub_smul (source proof only)
- Caller summary: One explicit executable caller at Roth/Wronskian.lean:213; full strong-induction caller rebuilt noncircularly.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.sum_natDegree_update_lt.md).

### Completed: `Roth.wronskian_ne_zero_of_linearIndependent`

- Type: `∀ {K : Type u_2} [inst : Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]}, LinearIndependent K φ → Roth.wronskian φ ≠ 0`
- What: The hard implication of the characteristic-zero polynomial Wronskian criterion: a linearly independent finite family has nonzero consecutive Hasse determinant.
- How: Strong induction on total natural degree; repeated degrees are removed by constant column shears, reducing to Vandermonde nonvanishing for distinct degrees.
- Hypotheses: Field K, CharZero K, φ : Fin l → K[X], LinearIndependent K φ
- Project dependencies: Roth.wronskian, Roth.wronskian_ne_zero_of_natDegree_injective, Roth.wronskian_update_sub_smul, Roth.sum_natDegree_update_lt, Roth.linearIndependent_update_sub_smul
- Caller summary: external to file count: 2; all explicit calls: 3; locations: Roth/Wronskian.lean:221, Roth/GenWronskian.lean:262, Roth/Separation.lean:534; scope: Explicit production source references; not opaque kernel/simp dependency closure
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian_ne_zero_of_linearIndependent.md).

### Completed: `Roth.wronskian_eq_zero_iff`

- Type: `∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]}, Roth.wronskian φ = 0 ↔ ¬ LinearIndependent K φ`
- What: The n-ary characteristic-zero polynomial Hasse Wronskian vanishes exactly for linearly dependent families.
- How: Packages the contrapositive of the project hard implication with the project easy implication; the hard proof uses degree elimination and Vandermonde nonvanishing.
- Hypotheses: Field K, CharZero K, φ : Fin l → K[X]
- Project dependencies: Roth.wronskian, Roth.wronskianMatrix, Roth.wronskian_ne_zero_of_linearIndependent, Roth.wronskian_eq_zero_of_not_linearIndependent
- Caller summary: external to file count: 0; all explicit calls: 0; locations: None; documentation: Roth/Wronskian.lean:32 lists as Main result; inline related: Roth/GenWronskian.lean:41 generalized easy direction, Roth/GenWronskian.lean:262 calls hard implication, Roth/Separation.lean:534 calls hard implication; scope: Whole production Lean source explicit references and inline audit, not opaque kernel/simp closure.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian_eq_zero_iff.md).

### Completed: `MvPolynomial.taylor`

- Type: `{σ : Type u_1} → {R : Type u_2} → [CommSemiring R] → (σ → R) → MvPolynomial σ R →ₐ[R] MvPolynomial σ R`
- What: Translation of multivariate polynomials by a constant vector, P(X+α).
- How: Universal algebra evaluation at X j + C (α j).
- Hypotheses: Arbitrary independent variable/coefficient universes, commutative coefficient semiring, arbitrary translation vector; no finiteness or characteristic restrictions.
- Project dependencies: None
- Caller summary: all explicit callers: 24; in declaring module: 17; external: 7; identifier occurrences: 41; detail: callers.json; scope: Source-level explicit references, not opaque kernel/simp closure.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor.md).

### Completed: `MvPolynomial.taylor_apply`

- Type: `∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (α : σ → R) (P : MvPolynomial σ R), (MvPolynomial.taylor α) P = (MvPolynomial.aeval fun j ↦ MvPolynomial.X j + MvPolynomial.C (α j)) P`
- What: Applying polynomial translation is substitution of X j + C (α j).
- How: Kernel reflexivity after unfolding the local taylor definition; no theorem calls.
- Hypotheses: Arbitrary independent variable/coefficient universes; commutative coefficient semiring; arbitrary α and P.
- Project dependencies: MvPolynomial.taylor (statement and definitional unfolding only)
- Caller summary: all explicit callers: 0; in declaring module: 0; external: 0; excluded: Roth/Index.lean:243 uses Polynomial.taylor_apply; inline parent unfolding lines: 143, 148, 153, 159, 166; detail: callers.json; scope: Source-level explicit named references, not opaque kernel/simp closure; target has no simp annotation.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_apply.md).

### Completed: `MvPolynomial.taylor_X`

- Type: `∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (α : σ → R) (j : σ), (MvPolynomial.taylor α) (MvPolynomial.X j) = MvPolynomial.X j + MvPolynomial.C (α j)`
- What: Translation sends the generator X j to X j plus the constant α j.
- How: Direct existing MvPolynomial.aeval_X theorem application after definitional reduction of the parent taylor; one existing-law call, no closing simp required.
- Hypotheses: Arbitrary independent variable and coefficient universes, CommSemiring R, arbitrary α : σ → R and j : σ.
- Project dependencies: MvPolynomial.taylor (statement and definitional specialization only)
- Caller summary: all explicit callers: 1; in declaring module: 1; external: 0; outside file internal use count: 0; caller: Roth/Taylor.lean:114, private coeff_taylor_monomial_single_add_aux; inline rederivations: None; simp api: True; scope: Named references do not measure opaque kernel/simp closure. Full caller and concrete simp consumers verified with target simp disabled.; detail: callers.json
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_X.md).

### Completed: `MvPolynomial.taylor_C`

- Type: `∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (α : σ → R) (a : R), (MvPolynomial.taylor α) (MvPolynomial.C a) = MvPolynomial.C a`
- What: Translation fixes constant polynomials.
- How: One existing-law specialization MvPolynomial.algHom_C _ _.
- Hypotheses: Arbitrary variable type σ, commutative coefficient semiring R, translation vector α, scalar a; no finiteness/nonzero/characteristic constraints.
- Project dependencies: type: MvPolynomial.taylor; proof: None
- Caller summary: explicit callers: 1; within file: 0; external to file: 1; locations: Roth/Index.lean:197 (Roth.index_C_mul); simp scope: @[simp] can serve implicit consumers; no exhaustive kernel/simp closure claim.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_C.md).

### Completed: `MvPolynomial.taylor_monomial`

- Type: `∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (α : σ → R) (k : σ →₀ ℕ) (a : R), (MvPolynomial.taylor α) ((MvPolynomial.monomial k) a) = MvPolynomial.C a * k.prod (fun j n ↦ (MvPolynomial.X j + MvPolynomial.C (α j)) ^ n)`
- What: Translation of a monomial is its coefficient times the product of translated coordinate powers.
- How: One direct application of existing MvPolynomial.aeval_monomial.
- Hypotheses: Arbitrary variable/coefficient universes; CommSemiring R; arbitrary shift α, finite natural exponent k, coefficient a.
- Project dependencies: type: MvPolynomial.taylor; body: None
- Caller summary: all explicit: 1; internal excluding declaring file: 0; external files: 0; callers: MvPolynomial.eq_sum_box_hasseDeriv at Roth/Taylor.lean:212; simp: False; opaque closure claimed: False
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_monomial.md).

### Completed: `MvPolynomial.coeff_aeval_X_mul`

- Type: `∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (i : σ) (f : R[X]) (B : MvPolynomial σ R),
  (∀ e ∈ B.support, e i = 0) →
    ∀ (d : σ →₀ ℕ), ((Polynomial.aeval (X i)) f * B).coeff d = f.coeff (d i) * B.coeff (Finsupp.erase i d)`
- What: Computes the coefficient of the product of a univariate polynomial in one variable and a multivariate polynomial independent of that variable.
- How: Expands Polynomial.eval₂_eq_sum and coeff_monomial_mul', then Finset.sum_eq_single selects the only possible univariate exponent; the support-independence hypothesis kills every other summand.
- Hypotheses: Arbitrary variable type and commutative semiring; second factor has zero selected-coordinate exponent throughout its support. No finiteness or nonzero assumptions.
- Project dependencies: None
- Caller summary: One explicit caller, private coeff_taylor_monomial_single_add_aux at Taylor115; no explicit outside-file references. Full caller replay uses fresh target replay.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_aeval_X_mul.md).

### Completed: `MvPolynomial.hasseCoeff_single_add_eq`

- Type: `∀ {σ : Type u_2} {i : σ} {n : ℕ} {k' : σ →₀ ℕ},
  k' i = 0 → ∀ (d : σ →₀ ℕ), hasseCoeff d (Finsupp.single i n + k') = n.choose (d i) * hasseCoeff (Finsupp.erase i d) k'`
- What: Splits a multivariate binomial factor into one coordinate's binomial coefficient and the factor on the erased multi-index.
- How: Uses Finsupp.mul_prod_erase' to extract the selected coordinate; all other coordinates are unchanged because the added one-coordinate term vanishes there.
- Hypotheses: Arbitrary variable type and natural finitely supported indices; residual exponent k′ has zero selected coordinate. No coefficient semiring or finite-variable assumption.
- Project dependencies: MvPolynomial.hasseCoeff
- Caller summary: One explicit caller private coeff_taylor_monomial_single_add_aux, use Taylor117; complete caller replay with fresh scalar-identity replay accepted.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_single_add_eq.md).

### Completed: `MvPolynomial.prod_pow_single_add_tsub`

- Type: `∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) {i : σ} {n : ℕ} {k' : σ →₀ ℕ},
  k' i = 0 →
    ∀ (d : σ →₀ ℕ),
      ((Finsupp.single i n + k' - d).prod fun j e ↦ α j ^ e) =
        α i ^ (n - d i) * (k' - Finsupp.erase i d).prod fun j e ↦ α j ^ e`
- What: Factors the evaluation of a lowered single-coordinate-plus-residual monomial into the selected coordinate power and the erased residual product.
- How: Coordinate extensionality identifies the truncated exponent subtraction; Finsupp.prod_add_index' and pow_add split the resulting product.
- Hypotheses: Original: arbitrary variables and commutative semiring; residual coordinate k′ i=0. Verified same proof under only CommMonoid for values, no semiring operations needed.
- Project dependencies: None
- Caller summary: One named caller private coeff_taylor_monomial_single_add_aux, Taylor117. Complete caller with fresh target replay verified.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.prod_pow_single_add_tsub.md).

### Completed: `MvPolynomial.coeff_taylor_monomial_single_add_aux`

- Type: `∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) (a : R) {i : σ} (n : ℕ) {k : σ →₀ ℕ},
  k i = 0 →
    (∀ (d : σ →₀ ℕ), ((taylor α) ((monomial k) a)).coeff d = (eval α) ((hasseDeriv d) ((monomial k) a))) →
      ∀ (d : σ →₀ ℕ),
        ((taylor α) ((monomial (Finsupp.single i n + k)) a)).coeff d =
          (eval α) ((hasseDeriv d) ((monomial (Finsupp.single i n + k)) a))`
- What: Proves the coefficient Taylor identity for a monomial after adding one new coordinate, assuming the identity for the residual monomial.
- How: Derives translated residual support independence, applies coefficient separation and the one-variable binomial theorem, then factors binomial and power products.
- Hypotheses: Arbitrary variables and commutative semiring; residual exponent zero in selected coordinate; induction hypothesis for all residual coefficients; n and a unrestricted.
- Project dependencies: MvPolynomial.coeff_aeval_X_mul, MvPolynomial.hasseCoeff_eq_zero_iff, MvPolynomial.hasseCoeff_single_add_eq, MvPolynomial.hasseDeriv, MvPolynomial.hasseDeriv_monomial, MvPolynomial.prod_pow_single_add_tsub, MvPolynomial.taylor, MvPolynomial.taylor_X
- Caller summary: One explicit caller private coeff_taylor_monomial_aux at Taylor129; full caller replay using fresh induction-step proof validated.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_taylor_monomial_single_add_aux.md).

### Completed: `MvPolynomial.coeff_taylor_monomial_aux`

- Type: `∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) (d k : σ →₀ ℕ) (a : R),
  ((taylor α) ((monomial k) a)).coeff d = (eval α) ((hasseDeriv d) ((monomial k) a))`
- What: Proves the coefficient Taylor identity for every monomial over arbitrary commutative semirings.
- How: Inducts on the finitely supported exponent; constant base cases use scalar homomorphism/derivative rules, coordinate extension uses private induction-step helper.
- Hypotheses: Arbitrary variable type and commutative semiring; arbitrary translation, coefficient and multi-indices, with no support/degree/nonzero/finite-variable assumptions.
- Project dependencies: MvPolynomial.coeff_taylor_monomial_single_add_aux, MvPolynomial.hasseDeriv, MvPolynomial.hasseDeriv_C, MvPolynomial.hasseDeriv_zero, MvPolynomial.taylor
- Caller summary: One explicit caller public coeff_taylor, Taylor138; entire public caller proof using fresh monomial replay validated.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_taylor_monomial_aux.md).

### Completed: `MvPolynomial.coeff_taylor`

- Type: `∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (α : σ → R) (d : σ →₀ ℕ) (P : MvPolynomial σ R), (MvPolynomial.taylor α P).coeff d = MvPolynomial.eval α (MvPolynomial.hasseDeriv d P)`
- What: The coefficient of a translated multivariate polynomial is its Hasse derivative evaluated at the translation point.
- How: Additive polynomial induction and a separately verified monomial binomial-coefficient calculation; native direct-constant audit excludes circular target use.
- Hypotheses: σ,R arbitrary independent universes, CommSemiring R; no Fintype, DecidableEq, Nontrivial, domain or characteristic assumptions, arbitrary α,d,P
- Project dependencies: MvPolynomial.taylor, MvPolynomial.hasseDeriv, private monomial proof chain58–62
- Caller summary: explicit references: 5; caller declarations: 4; external references: 3; external files: Roth/Index.lean; same file references: 2; full replays: native-callers-success.json
- Verdict: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_taylor.md).

### Completed: `MvPolynomial.eval_taylor`

- Type: `∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (α x : σ → R) (P : MvPolynomial σ R), eval x (taylor α P) = eval (fun j ↦ x j + α j) P`
- What: Evaluating a translated polynomial at x equals evaluating the original at x+α.
- How: Generic eval_assoc plus add, variable, and constant evaluation normalization; one closing simp.
- Hypotheses: CommSemiring R; arbitrary independent-universe σ,R; no finite or degree assumptions
- Project dependencies: MvPolynomial.taylor
- Caller summary: named source uses: 0; same file named uses: 0; external files: 0; inline exact duplicates: 0; references filter: five LSP locations include declaration and scratch inspections; no production uses
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.eval_taylor.md).

### Completed: `MvPolynomial.taylor_taylor`

- Type: `∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (α β : σ → R) (P : MvPolynomial σ R), taylor α (taylor β P) = taylor (fun j ↦ α j + β j) P`
- What: Two constant polynomial translations compose by adding their translation vectors.
- How: Generic comp_aeval_apply followed by normalization of evaluation on variable plus constant, associativity, and constant-map additivity.
- Hypotheses: CommSemiring R; arbitrary independent-universe σ,R; no finite variables, degree bound, characteristic, decidable equality, or nonzero condition
- Project dependencies: MvPolynomial.taylor
- Caller summary: named source uses: 1; same file named uses: 1; external files: 0; caller: Roth/Taylor.lean:184 taylor_neg_taylor; transitive: taylor_injective, taylor_eq_zero_iff, eq_sum_box_hasseDeriv
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_taylor.md).

### Completed: `MvPolynomial.taylor_zero`

- Type: `∀ {σ : Type u_3} {R : Type u_4} [CommSemiring R] (P : MvPolynomial σ R), (MvPolynomial.taylor fun x ↦ 0) P = P`
- What: Zero translation fixes every multivariate polynomial.
- How: Normalize each generator X j+C 0 to X j, then apply aeval_X_left_apply.
- Hypotheses: Arbitrary variable type σ, coefficient commutative semiring R, and polynomial P; no other hypotheses.
- Project dependencies: MvPolynomial.taylor
- Caller summary: 0 explicit refs; actual simp dependency in taylor_neg_taylor confirmed by disabling target and inspecting constants. Replacement inverse/injective/zero_iff chain verified.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_zero.md).

### Completed: `MvPolynomial.taylor_map`

- Type: `∀ {σ : Type u} {R : Type v} [CommSemiring R] {S : Type w} [CommSemiring S] (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R), MvPolynomial.taylor (fun j ↦ f (α j)) (MvPolynomial.map f P) = MvPolynomial.map f (MvPolynomial.taylor α P)`
- What: Translation commutes with coefficient change, mapping the translation vector as well as the polynomial.
- How: Generic substitution-map naturality followed by normalization of mapped generators using map_add/map_X/map_C.
- Hypotheses: Arbitrary independent-universe variable/source/target types, commutative semirings R and S, arbitrary unital semiring homomorphism f, translation vector and polynomial. No injectivity, characteristic or finite-variable conditions.
- Project dependencies: MvPolynomial.taylor
- Caller summary: 0 named production callers; no independent inline derivation found. Not simp-tagged; no exhaustive implicit dependency closure claimed.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_map.md).

### Completed: `MvPolynomial.taylor_rename`

- Type: `∀ {σ : Type u} {R : Type v} [CommSemiring R] {τ : Type w} (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R), MvPolynomial.taylor α (MvPolynomial.rename f P) = MvPolynomial.rename f (MvPolynomial.taylor (α ∘ f) P)`
- What: Translation commutes with arbitrary variable renaming, restricting the shift along the variable map.
- How: Generic aevaluation/renaming composition, then normalization of shifted generators.
- Hypotheses: Arbitrary independent-universe σ,τ,R; CommSemiring R; arbitrary map f including noninjective, arbitrary α,P. No finiteness/characteristic/nonzero assumptions.
- Project dependencies: MvPolynomial.taylor
- Caller summary: One explicit source caller Roth.index_rename at Index216; full native caller replay succeeds using fresh target replay. Its injectivity assumption belongs to support/weight transport.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_rename.md).

### Completed: `MvPolynomial.degreeOf_taylor_le`

- Type: `∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (α : σ → R) (j : σ) (P : MvPolynomial σ R), MvPolynomial.degreeOf j (MvPolynomial.taylor α P) ≤ MvPolynomial.degreeOf j P`
- What: Constant coordinate translation does not increase degree in any chosen variable.
- How: An exponent above the original coordinate degree has zero Hasse derivative, hence zero translated coefficient; apply the support characterization of degree.
- Hypotheses: Arbitrary independent-universe σ,R; CommSemiring R; arbitrary shift, variable and polynomial. No finiteness, nonzero, domain or characteristic restriction.
- Project dependencies: MvPolynomial.taylor, MvPolynomial.coeff_taylor, MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt
- Caller summary: One explicit caller Roth.index_le_card Index229; full copied proof verified using fresh target replay.
- Verdict: YES-add-as-is; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.degreeOf_taylor_le.md).

### Completed: `MvPolynomial.taylor_neg_taylor`

- Type: `∀ {σ : Type u_1} {A : Type u_2} [CommRing A] (α : σ → A) (P : MvPolynomial σ A), MvPolynomial.taylor (fun j ↦ -α j) (MvPolynomial.taylor α P) = P`
- What: Translating a polynomial and translating back by the negative vector returns the original polynomial.
- How: Substitution composition adds the shift vectors; additive cancellation and zero-translation identity then give the result.
- Hypotheses: Arbitrary independent-universe variable and coefficient types, commutative coefficient ring, every shift and polynomial. No finiteness, nonzero, field or characteristic assumptions.
- Project dependencies: MvPolynomial.taylor, MvPolynomial.taylor_taylor, MvPolynomial.taylor_zero (implicit simp)
- Caller summary: Two explicit callers, taylor_injective Taylor188 and eq_sum_box_hasseDeriv Taylor208; native full replays use fresh inverse proof.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_neg_taylor.md).

### Completed: `MvPolynomial.taylor_injective`

- Type: `∀ {σ : Type u_1} {A : Type u_2} [CommRing A] (α : σ → A), Function.Injective (MvPolynomial.taylor α : MvPolynomial σ A → MvPolynomial σ A)`
- What: Translation by any coefficient vector is injective on formal multivariate polynomials over a commutative ring.
- How: Apply generic Function.LeftInverse.injective to opposite-shift cancellation.
- Hypotheses: Arbitrary independent-universe variables and coefficients, CommRing, every shift. No finiteness, field, domain, characteristic or nontriviality hypotheses.
- Project dependencies: MvPolynomial.taylor, MvPolynomial.taylor_neg_taylor
- Caller summary: One explicit caller: taylor_eq_zero_iff, Taylor193; full fresh caller proof verified. Index zero-iff uses are transitive.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_injective.md).

### Completed: `MvPolynomial.taylor_eq_zero_iff`

- Type: `∀ {σ : Type u_1} {A : Type u_2} [CommRing A] (α : σ → A) (P : MvPolynomial σ A), MvPolynomial.taylor α P = 0 ↔ P = 0`
- What: Formal multivariate polynomial translation reflects zero; current ring hypothesis can be weakened to CommSemiring.
- How: Original proof derives zero reflection from inverse-based injectivity. Verified stronger proof chooses a maximal supported exponent, whose Hasse derivative is its nonzero constant coefficient, contradicting zero translate.
- Hypotheses: Arbitrary independent-universe variables and coefficients, shift and polynomial. CommRing currently, verified CommSemiring replacement; no finite/domain/characteristic/nontrivial assumptions.
- Project dependencies: MvPolynomial.taylor, MvPolynomial.taylor_injective
- Caller summary: 0explicit named refs,4 measured implicit simp consumers in Roth/Index: exists_weight_eq_index,le_index_iff,index_eq_weightedOrder_div,index_mul. All4 full fresh proofs pass with old target simp disabled and stronger theorem local simp.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_eq_zero_iff.md).

### Completed: `MvPolynomial.eq_sum_box_hasseDeriv`

- Type: `∀ {σ : Type u_1} {A : Type u_2} [CommRing A] [Fintype σ] [DecidableEq σ] (α : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A), (∀ j, MvPolynomial.degreeOf j P ≤ r j) → P = ∑ d ∈ Roth.box r, MvPolynomial.C (MvPolynomial.eval α (MvPolynomial.hasseDeriv d P)) * ∏ j, (MvPolynomial.X j - MvPolynomial.C (α j)) ^ d j`
- What: Reconstructs a polynomial from Hasse derivative values at a center as a finite sum of products of powers of X minus that center over a bounding coordinate box.
- How: Coefficient extensionality and coeff_taylor identify translated coefficients; hasseDeriv_eq_zero_of_degreeOf_lt kills out-of-box terms, and taylor_neg_taylor plus taylor_monomial transport back.
- Hypotheses: Arbitrary commutative coefficient ring, finite variable enumeration, arbitrary center and polynomial, natural coordinatewise degree bounds. Explicit DecidableEq can be removed using scoped Classical and propositional instance transport.
- Project dependencies: MvPolynomial.taylor, MvPolynomial.coeff_taylor, MvPolynomial.hasseDeriv, MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt, MvPolynomial.taylor_neg_taylor, MvPolynomial.taylor_monomial, Roth.box, Roth.mem_box
- Caller summary: 1 explicit caller, eval_eq_sum_box at Taylor220; no direct callers outside file. Full evaluated caller checked both for original arbitrary DecidableEq and no-explicit-DecidableEq core. Main390 application is transitive through evaluated corollary.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.eq_sum_box_hasseDeriv.md).

### Completed: `MvPolynomial.eval_eq_sum_box`

- Type: `∀ {σ : Type u_1} {A : Type u_2} [CommRing A] [Fintype σ] [DecidableEq σ] (α x : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A), (∀ j, MvPolynomial.degreeOf j P ≤ r j) → MvPolynomial.eval x P = ∑ d ∈ Roth.box r, MvPolynomial.eval α (MvPolynomial.hasseDeriv d P) * ∏ j, (x j - α j) ^ d j`
- What: Evaluates a polynomial as a finite Hasse Taylor expansion about an arbitrary center, over its coordinate degree-bounding box.
- How: Apply the evaluation ring homomorphism to eq_sum_box_hasseDeriv and distribute over finite sums, products, powers, variables and constants; no repeated binomial proof. Strongest scalar-extension form additionally transports degree via support_map_subset and Hasse evaluation via hasseDeriv_map/eval₂_eq_eval_map.
- Hypotheses: Arbitrary commutative coefficient ring and finite variable type, arbitrary center/point/polynomial, natural coordinate bounds with each degree bounded. Explicit DecidableEq removable through scoped Classical and propositional original-instance recovery.
- Project dependencies: MvPolynomial.eq_sum_box_hasseDeriv, MvPolynomial.hasseDeriv, Roth.box
- Caller summary: 1 explicit external-to-file caller Roth.abs_eval_lt_of_le_index at Main390; full estimate/private product-weight helper checked against fresh scalar recovery, intermediate algebra-target recovery and strongest B-valued center/point recovery (three full estimate replays).
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/MvPolynomial.eval_eq_sum_box.md).

### Completed: `Roth.normOne`

- Type: `∀ {σ : Type u_1}, MvPolynomial σ ℤ → ℝ`
- What: Coefficient ℓ¹ norm / length of an integer multivariate polynomial: finite sum of real absolute coefficient values.
- How: One support sum; definitionally equal to P.coeff.sum (fun _ z : ℤ ↦ |(z : ℝ)|), existing Finsupp.sum.
- Hypotheses: Arbitrary universe-polymorphic variable type σ and integer-coefficient polynomial; no Fintype, DecidableEq, nonzero or degree hypotheses.
- Project dependencies: None
- Caller summary: 14 distinct direct declaration consumers, all in CoeffNorm; no external-to-file named use. Four representative proofs replayed in mathlib-only native code; all fourteen have explicit transparent-substitution plans, not all claimed recompiled.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne.md).

### Completed: `Roth.diag`

- Type: `∀ {σ : Type u_1}, MvPolynomial σ ℤ → Polynomial ℤ`
- What: Diagonal specialization: replace all variables by a common polynomial indeterminate, adding coefficients when total exponents collide.
- How: One existing MvPolynomial.aeval application to constant Polynomial.X, exact rfl recovery. Alternative rename-to-PUnit then uniqueAlgEquiv is proved equal, not claimed defeq.
- Hypotheses: Arbitrary variable type σ and integer polynomial; no finiteness, DecidableEq, nonzero or degree assumptions.
- Project dependencies: None
- Caller summary: 11 distinct direct declaration consumers: 5 CoeffNorm and 6 MainLemma in one external file. Full vanishing/subtraction replays and mathlib-only generalized expansion verified; all 11 caller plans explicit. Arbitrary predicate-context rfl transport checked, not a claim all callers were separately rebuilt.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.diag.md).

### Completed: `Roth.normOne_nonneg`

- Type: `∀ {σ : Type u_1} (P : MvPolynomial σ ℤ), 0 ≤ Roth.normOne P`
- What: Nonnegativity of integer polynomial coefficient ℓ¹ norm.
- How: Finite sum of nonnegative real absolute values; exactly Finset.sum_nonneg + abs_nonneg.
- Hypotheses: Arbitrary universe-polymorphic variable type and polynomial. No Fintype, DecidableEq, nonzero, degree or sign assumptions.
- Project dependencies: Roth.normOne
- Caller summary: Two named consumers, normOne_prod_le107 and normOne_det_le128, both full proof replays validated with fresh replacement.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_nonneg.md).

### Completed: `Roth.normOne_eq_sum_of_support_subset`

- Type: `∀ {σ : Type u_1} {P : MvPolynomial σ ℤ} {s : Finset (σ →₀ ℕ)}, P.support ⊆ s → Roth.normOne P = ∑ d ∈ s, |((P.coeff d : ℤ) : ℝ)|`
- What: Coefficient ℓ¹ norm can be computed on any finite superset of polynomial support.
- How: Add only terms whose coefficient is zero; existing Finsupp.sum_of_support_subset specializes exactly after Int.cast_zero and abs_zero.
- Hypotheses: Arbitrary universe-polymorphic variable type; implicit integer polynomial and finite exponent set; support inclusion. No finite-variable, degree, norm-instance, sign or nonzero assumptions.
- Project dependencies: Roth.normOne
- Caller summary: Two named consumers in declaring module, four source applications: normOne_monomial61 and normOne_add_le79–81. Full replacement proof bodies native checked.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_eq_sum_of_support_subset.md).

### Completed: `Roth.normOne_monomial`

- Type: `∀ {σ : Type u_1} (e : σ →₀ ℕ) (c : ℤ), Roth.normOne (MvPolynomial.monomial e c) = |(c : ℝ)|`
- What: Coefficient ℓ¹ norm of a monomial is the absolute value of its coefficient, including zero.
- How: Single nonzero position, or empty support when coefficient zero; existing sum_monomial_eq applies directly with absolute-value cast size and explicit zero normalization.
- Hypotheses: Arbitrary universe-polymorphic variable type σ, exponent e : σ →₀ ℕ and c : ℤ. No finite variable, degree, coefficient nonzero or positivity hypotheses.
- Project dependencies: Roth.normOne, Roth.normOne_eq_sum_of_support_subset (original proof only)
- Caller summary: Three explicit consumers/three references, all in CoeffNorm: normOne_mul_le102, normOne_prod_le108, normOne_hasseDeriv_le155. All three full replacement proofs freshly native checked.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_monomial.md).

### Completed: `Roth.normOne_zero`

- Type: `∀ {σ : Type u_1}, Roth.normOne (0 : MvPolynomial σ ℤ) = 0`
- What: The zero integer multivariate polynomial has coefficient ℓ¹ norm zero.
- How: Empty coefficient support; direct existing Finsupp.sum_zero_index specialization is definitionally the project statement.
- Hypotheses: Only arbitrary universe-polymorphic σ. No Fintype, DecidableEq, degree, positivity or size-zero assumption.
- Project dependencies: Roth.normOne
- Caller summary: One explicit consumer: Roth.normOne_sum_le CoeffNorm92. All293 canonical production values audited; only that direct proof consumer and no additional hidden simp users. Full replacement sum proof checked. Audit is not transitive/external closure.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_zero.md).

### Completed: `Roth.abs_coeff_le_normOne`

- Type: `∀ {σ : Type u_2} (P : MvPolynomial σ ℤ) (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ Roth.normOne P`
- What: Every integer multivariate polynomial coefficient has absolute real value bounded by its coefficient ℓ1 sum.
- How: Direct Finsupp.single_eval_le_sum specialization, g z = |(z : ℝ)|; zero and nonnegativity are elementary abs facts.
- Hypotheses: No explicit hypotheses or typeclasses on σ; σ universe-polymorphic, P and d arbitrary. Integer coefficients and real output fixed by normOne.
- Project dependencies: Roth.normOne (statement only; transparent definitional coefficient-sum representation)
- Caller summary: One explicit caller: Roth.abs_coeff_det_hasseDeriv_le at CoeffNorm.lean:266; zero external-to-file refs. Full fresh determinant proof replay succeeds with direct generic call. Main.lean:424 independently uses analogous generic bound for univariate coefficients.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_le_normOne.md).

### Completed: `Roth.normOne_add_le`

- Type: `∀ {σ : Type u_1} (P Q : MvPolynomial σ ℤ), Roth.normOne (P + Q) ≤ Roth.normOne P + Roth.normOne Q`
- What: The coefficient absolute sum of P+Q is bounded by the sum of their coefficient lengths.
- How: Pad all three coefficient sums to the union of supports and sum the scalar absolute-value triangle inequality.
- Hypotheses: Arbitrary variable type σ; two integer polynomials P,Q. No finite-variable, degree, sign or coefficient-bound premise. Parent fixes integer coefficients and real-valued absolute sum.
- Project dependencies: type: Roth.normOne; proof: Roth.normOne_eq_sum_of_support_subset
- Caller summary: One explicit source caller Roth.normOne_sum_le in the same module; fresh293-value direct-proof audit finds precisely that caller. Not a transitive/generated-helper or external-user closure.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_add_le.md).

### Completed: `Roth.normOne_neg`

- Type: `∀ {σ : Type u_1} (P : MvPolynomial σ ℤ), Roth.normOne (-P) = Roth.normOne P`
- What: Negating an integer multivariate polynomial preserves its coefficient l1 length.
- How: Negation preserves support and absolute values; existing Finsupp negation reindexing supplies the abstract law.
- Hypotheses: Arbitrary σ and integer polynomial P, no additional assumptions. Parent fixes coefficient/output types.
- Project dependencies: type: Roth.normOne; proof: Roth.normOne
- Caller summary: One explicit caller Roth.normOne_det_le at CoeffNorm127; fresh293-value direct-proof audit finds exactly that consumer. Complete replacement determinant replay succeeds.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_neg.md).

### Completed: `Roth.normOne_sum_le`

- Type: `∀ {σ : Type u_1} {ι : Type u_2} (s : Finset ι) (f : ι → MvPolynomial σ ℤ), Roth.normOne (∑ i ∈ s, f i) ≤ ∑ i ∈ s, Roth.normOne (f i)`
- What: The coefficient ℓ1 size of a finite sum of integer multivariate polynomials is bounded by the sum of the coefficient sizes.
- How: Finset.le_sum_of_subadditive applied to normOne using project normOne_zero and normOne_add_le.
- Hypotheses: Arbitrary variable type σ, family index ι, finite set s and polynomial family f; no Fintype, DecidableEq, degree or coefficient bound assumptions.
- Project dependencies: Roth.normOne, Roth.normOne_zero, Roth.normOne_add_le
- Caller summary: 3 named direct consumers,4 source occurrences, all in CoeffNorm: normOne_mul_le99/101, normOne_det_le123, normOne_hasseDeriv_le152; full293 unique direct-proof audit.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_sum_le.md).

### Completed: `Roth.normOne_mul_le`

- Type: `∀ {σ : Type u_1} (P Q : MvPolynomial σ ℤ), Roth.normOne (P * Q) ≤ Roth.normOne P * Roth.normOne Q`
- What: Coefficient L1 size of a product is at most the product of sizes.
- How: Expand convolution, apply finite triangle twice and monomial size, then factor double scalar sum.
- Hypotheses: Arbitrary variable type σ and integer polynomials P,Q; no additional hypotheses.
- Project dependencies: Roth.normOne, Roth.normOne_sum_le, Roth.normOne_monomial
- Caller summary: One explicit use in normOne_prod_le; full caller replay and direct proof-value audit of293 canonical declarations agree.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_mul_le.md).

### Completed: `Roth.normOne_prod_le`

- Type: `∀ {σ : Type u_1} {ι : Type u_2} (s : Finset ι) (f : ι → MvPolynomial σ ℤ), Roth.normOne (∏ i ∈ s, f i) ≤ ∏ i ∈ s, Roth.normOne (f i)`
- What: Coefficient L1 of a finite product is bounded by the product of coefficient L1 sizes.
- How: Existing Finset nonnegative submultiplicative-map induction, using project nonnegative/unit/binary witnesses.
- Hypotheses: Arbitrary variable and index types σ,ι; any finite s and polynomial family f; ℤ/ℝ fixed by normOne.
- Project dependencies: Roth.normOne, Roth.normOne_nonneg, Roth.normOne_monomial, Roth.normOne_mul_le
- Caller summary: One explicit caller normOne_det_le in same module; full caller replay and exact293 direct proof audit agree.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_prod_le.md).

### Completed: `Roth.normOne_le_card_mul`

- Type: `∀ {σ : Type u_1} (P : MvPolynomial σ ℤ) {B : ℝ}, (∀ (d : σ →₀ ℕ), |((P.coeff d : ℤ) : ℝ)| ≤ B) → Roth.normOne P ≤ (P.support.card : ℝ) * B`
- What: Coefficient ℓ¹ sum bounded by support size times uniform coefficient bound.
- How: Direct specialization of Finset.sum_le_card_nsmul; unfold normOne and rewrite nsmul_eq_mul.
- Hypotheses: Arbitrary variable type; integer coefficients and real bound fixed by normOne interface; global coefficient bound can weaken to support-only.
- Project dependencies: Roth.normOne
- Caller summary: One explicit caller Roth.abs_coeff_det_hasseDeriv_le at CoeffNorm.lean:270; full caller replay succeeds with inline Finset bound; canonical293 unique audit confirms sole direct proof consumer.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_le_card_mul.md).

### Completed: `Roth.normOne_det_le`

- Type: `∀ {σ : Type u_1} {l : ℕ} (M : Matrix (Fin l) (Fin l) (MvPolynomial σ ℤ)) {C : ℝ}, (∀ μ ν, Roth.normOne (M μ ν) ≤ C) → Roth.normOne M.det ≤ ↑l.factorial * C ^ l`
- What: Bounds coefficient L1 size of an l×l polynomial determinant by l! C^l.
- How: Leibniz expansion, subadditive finite sum, sign invariance, submultiplicative finite product, entrywise monotonicity, count permutations.
- Hypotheses: Arbitrary variables σ and l; all entries size≤C; C unrestricted; includes empty matrix.
- Project dependencies: Roth.normOne, Roth.normOne_sum_le, Roth.normOne_neg, Roth.normOne_prod_le, Roth.normOne_nonneg
- Caller summary: One direct named caller: Roth.abs_coeff_det_hasseDeriv_le at CoeffNorm268; exact293unique canonical proof-value audit confirms.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_det_le.md).

### Completed: `Roth.abs_coeff_hasseDeriv_le`

- Type: `∀ {σ : Type u_1} [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}, (∀ j, MvPolynomial.degreeOf j P ≤ r j) → ∀ {B : ℝ}, (∀ e, |((P.coeff e : ℤ) : ℝ)| ≤ B) → ∀ e, |(((MvPolynomial.hasseDeriv d P).coeff e : ℤ) : ℝ)| ≤ 2 ^ (∑ j, r j) * B`
- What: Every coefficient of a multivariate Hasse derivative is bounded by 2^(sum coordinate degree bounds) times an input coefficient bound.
- How: Coefficient extraction has one preimage e+d; split membership in input support, bound binomial product, multiply coefficient bound, handle zero coefficients.
- Hypotheses: Arbitrary finite variable type; integer polynomial; coordinate degree bounds r; real coefficient bound B; no B≥0 assumption because hB implies it.
- Project dependencies: MvPolynomial.coeff_hasseDeriv, MvPolynomial.hasseCoeff_le_two_pow
- Caller summary: Three explicit applications in two private MainLemma declarations at lines468 and509; full replay and exact canonical293 unique proof-value audit.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_hasseDeriv_le.md).

### Completed: `Roth.normOne_hasseDeriv_le`

- Type: `∀ {σ : Type u_2} [inst : Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), degreeOf j P ≤ r j) → normOne ((hasseDeriv d) P) ≤ (2 ^ ∑ j, r j) * normOne P`
- What: Hasse derivative has coefficient ℓ¹ size at most 2 to sum of coordinate degree bounds times original size.
- How: Expand derivative into monomials, apply finite triangle inequality, bound each binomial product and sum.
- Hypotheses: Fintype σ; arbitrary derivative multi-index; integer polynomial with degreeOf j P ≤ r j.
- Project dependencies: MvPolynomial.hasseDeriv_apply, Roth.normOne_sum_le, Roth.normOne_monomial, MvPolynomial.hasseCoeff_le_two_pow, Roth.normOne
- Caller summary: One source proof caller, Roth.abs_coeff_det_hasseDeriv_le:269; same sole direct consumer in exact ordered293 native audit; full generic-specialization replay passed.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.normOne_hasseDeriv_le.md).

### Completed: `Roth.diag_eq_sum`

- Type: `∀ {σ : Type u_1} (P : MvPolynomial σ ℤ),
  Roth.diag P = ∑ k ∈ P.support, (monomial (Finsupp.degree k)) (P.coeff k)`
- What: Diagonal substitution sends each coefficient monomial to a univariate monomial at total degree.
- How: Unfold diag/aeval, use eval₂_eq, collapse product of powers, identify total exponent and polynomial monomial.
- Hypotheses: Arbitrary variable type σ and integer polynomial P; no finiteness, degree, or nonzero hypotheses.
- Project dependencies: Roth.diag
- Caller summary: Two explicit same-file callers: abs_coeff_diag_le at176 and natDegree_diag_le at185; zero external-to-file. Canonical293 direct proof audit agrees.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.diag_eq_sum.md).

### Completed: `Roth.abs_coeff_diag_le`

- Type: `∀ {σ : Type u_1} (P : MvPolynomial σ ℤ) {B : ℝ},
  (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) → ∀ (n : ℕ), |↑((Roth.diag P).coeff n)| ≤ ↑P.support.card * B`
- What: Each coefficient after identifying all variables is bounded by input support cardinality times a uniform input coefficient bound.
- How: Expand diagonal polynomial into monomials; coefficient linearity and integer cast give finite sum; triangle inequality and sum≤card·B finish, treating off-degree terms as zero.
- Hypotheses: Arbitrary σ, integer polynomial P, real B with every input coefficient bounded in cast absolute value, arbitrary output index n; hB implies B≥0.
- Project dependencies: Roth.diag, Roth.diag_eq_sum
- Caller summary: One explicit external-to-file private caller Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux at MainLemma.lean:509; exact canonical293 direct proof audit agrees and full caller replay passes.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_diag_le.md).

### Completed: `Roth.natDegree_diag_le`

- Type: `∀ {σ : Type u_1} [inst : Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ}, (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) → (Roth.diag P).natDegree ≤ ∑ j, r j`
- What: Diagonal substitution has degree at most the sum of coordinate degree bounds.
- How: Expand into monomials and sum exponent bounds; independently verified existing aeval total-degree route with multiset-count bridge.
- Hypotheses: arbitrary variable universe σ, Fintype σ for sum, P integer polynomial, r natural coordinate bounds, ∀j, degreeOf j P≤r j
- Project dependencies: Roth.diag, Roth.diag_eq_sum
- Caller summary: named count: 1; file: Roth/MainLemma.lean:513; declaration: _private.Roth.MainLemma.0.Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux; replay: complete exact caller with expanded generic specialization verified
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.natDegree_diag_le.md).

### Completed: `Roth.eval_diag`

- Type: `∀ {σ : Type u_1} (P : MvPolynomial σ ℤ) (x : ℝ), Polynomial.eval x (Polynomial.map (Int.castRingHom ℝ) (Roth.diag P)) = MvPolynomial.eval (fun _ ↦ x) (MvPolynomial.map (Int.castRingHom ℝ) P)`
- What: Evaluation of diagonal substitution equals evaluation at the diagonal tuple after coefficient cast.
- How: Original polynomial induction; exact replacement specializes existing comp_aeval_apply and transports eval/map into aeval.
- Hypotheses: σ arbitrary Type*; P arbitrary integer multivariate polynomial; x arbitrary real; no hypotheses/Fintype.
- Project dependencies: Roth.diag
- Caller summary: 0 named explicit callers,0 direct proof consumers in exact ordered293audit;1 inline bypass at MainLemma:409 over arbitrary CommRing S.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.eval_diag.md).

### Completed: `Roth.diag_sub`

- Type: `∀ {σ : Type u_1} (P Q : MvPolynomial σ ℤ), Roth.diag (P - Q) = Roth.diag P - Roth.diag Q`
- What: Diagonal substitution preserves subtraction.
- How: One generic map_sub application to MvPolynomial.aeval.
- Hypotheses: Arbitrary variable type; integer coefficients fixed by parent diag; two arbitrary polynomials.
- Project dependencies: Roth.diag
- Caller summary: One explicit reference and one native direct proof consumer: MainLemma408 eval_hasseDeriv_sub_eq_zero.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.diag_sub.md).

### Completed: `Roth.geom_sum_le_one_add_pow`

- Type: `∀ {t : ℝ}, 0 ≤ t → ∀ (r : ℕ), ∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r`
- What: Nonnegative finite geometric sum bounded by binomial power.
- How: Expand using add_pow and compare positive-binomial-coefficient summands.
- Hypotheses: t nonnegative; natural r. Real ambient type weakens to Semiring/PartialOrder/IsOrderedRing.
- Project dependencies: None; proof uses only mathlib.
- Caller summary: One direct source and kernel caller, private sum_box_prod_pow_le_aux; abs_eval_le uses it indirectly. Exact293 ordered unique audit complete.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.geom_sum_le_one_add_pow.md).

### Completed: `Roth.sum_box_prod_pow_le_aux`

- Type: `∀ {σ : Type u_1} [inst : Fintype σ] (r : σ → ℕ) {B : ℝ},
  0 ≤ B → ∀ (x : σ → ℝ), ∑ k ∈ Roth.box r, B * ∏ j, |x j| ^ k j ≤ B * ∏ j, (1 + |x j|) ^ r j`
- What: The weighted sum of products of absolute powers over a rectangular box is bounded by the corresponding binomial product.
- How: Factors the box sum using Finset.prod_univ_sum and applies geom_sum_le_one_add_pow independently in each coordinate.
- Hypotheses: A finite variable enumeration, a nonnegative common factor B, natural degree bounds, and real coordinates. Native original/replay types have no external DecidableEq or nonzero assumptions.
- Project dependencies: Roth.box, Roth.geom_sum_le_one_add_pow
- Caller summary: Exactly one explicit and canonical direct proof consumer Roth.abs_eval_le at CoeffNorm239; complete caller replay uses fresh exact private-helper replay.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.sum_box_prod_pow_le_aux.md).

### Completed: `Roth.abs_eval_le`

- Type: `∀ {σ : Type u_1} [inst : Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) →
    ∀ {B : ℝ},
      (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
        ∀ (x : σ → ℝ), |(MvPolynomial.eval x) ((MvPolynomial.map (Int.castRingHom ℝ)) P)| ≤ B * ∏ j, (1 + |x j|) ^ r j`
- What: An integer multivariate polynomial with common absolute coefficient bound B and coordinate degrees at most r has value at x at most B times the product of (1+|x_j|)^r_j.
- How: Expand evaluation, take the finite-sum triangle inequality, enlarge support to Roth.box using monomial_le_degreeOf and Roth.mem_box, and apply private Roth.sum_box_prod_pow_le_aux to factor the geometric majorant.
- Hypotheses: A finite variable type, an integer polynomial, coordinate natural degree bounds, a common real absolute coefficient bound, and any real evaluation point; B≥0 follows from hB at zero.
- Project dependencies: Roth.box, Roth.mem_box, _private.Roth.CoeffNorm.0.Roth.sum_box_prod_pow_le_aux
- Caller summary: source calls: 1; files: Roth/MainLemma.lean; explicit callers: _private.Roth.MainLemma.0.Roth.abs_eval_iterated_hasseDeriv_lt_aux; canonical audit: 293 requested, unique, present and values; the same sole direct proof consumer; inline rederivations: None
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_eval_le.md).

### Completed: `Roth.degreeOf_det_hasseDeriv_le`

- Type: `∀ {σ : Type u_1} {l : ℕ} (E : Fin l → Fin l → σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}, (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) → ∀ (j : σ), MvPolynomial.degreeOf j (Matrix.of fun μ ν ↦ (MvPolynomial.hasseDeriv (E μ ν)) P).det ≤ l * r j`
- What: A determinant of l×l Hasse derivatives of a polynomial of coordinate degrees ≤r has coordinate degrees ≤l*r.
- How: Expand determinant; degree of sum bounded by supremum; constants do not increase degree; products bounded by sums; Hasse derivatives do not increase coordinate degrees.
- Hypotheses: Arbitrary σ, l, E and P over ℤ; global coordinate upper bound hP; no nonzero, finite-variable or derivative-order restriction.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.degreeOf_hasseDeriv_le
- Caller summary: Two explicit calls in Roth.exists_det_eq_mul at Separation.lean555/558; canonical293 audit confirms one direct consumer.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_det_hasseDeriv_le.md).

### Completed: `Roth.abs_coeff_det_hasseDeriv_le`

- Type: `∀ {σ : Type u_1} [inst : Fintype σ] {l : ℕ} (E : Fin l → Fin l → σ →₀ ℕ)
  (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) →
    ∀ {B : ℝ},
      0 ≤ B →
        (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
          ∀ (d : σ →₀ ℕ),
            |↑((Matrix.of fun μ ν ↦ (MvPolynomial.hasseDeriv (E μ ν)) P).det.coeff d)| ≤
              (∏ j, (↑(r j) + 1)) ^ l * ↑l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l)`
- What: Every coefficient of an l×l determinant of arbitrary Hasse derivatives of P is bounded by N^l*l!*B^l*2^(S*l), N=∏(rj+1), S=∑rj.
- How: Coefficient ≤ coefficient length; support length ≤ box cardinality times B; each Hasse derivative length grows by at most2^S; expand determinant into l! products; scalar ring normalization.
- Hypotheses: Arbitrary finite variable type, natural matrix size including0, arbitrary derivative-index array and exponent; degree and coefficient bounds; explicit hB0 is redundant.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseDeriv_apply, MvPolynomial.hasseCoeff_le_two_pow, Roth.card_le_card_box, Roth.abs_coeff_le_normOne, Roth.normOne_hasseDeriv_le, Roth.normOne_det_le, Roth.normOne_le_card_mul
- Caller summary: One explicit use in Roth.index_det_le at Theta.lean475; canonical293 audit confirms sole direct consumer. Entire caller recompiled through strongest generic specialization.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_det_hasseDeriv_le.md).

### Completed: `Roth.genWronskian`

- Type: `∀ {K : Type u_1} [Field K] {σ : Type u_2} {l : ℕ}, (Fin l → σ →₀ ℕ) → (Fin l → MvPolynomial σ K) → MvPolynomial σ K`
- What: Generalized Hasse Wronskian of a finite polynomial family, with selected row multiorders.
- How: Determinant of the square matrix (μ,ν) ↦ hasseDeriv (D μ) (φ ν).
- Hypotheses: Field K (can weaken to CommRing), arbitrary variables σ, no Fintype parameter, finite square family Fin l, can generalize to arbitrary Fintype index with DecidableEq, no independence, order bound, nonemptiness or characteristic restriction
- Project dependencies: MvPolynomial.hasseDeriv
- Caller summary: 5 explicit caller declarations (3 internal,2 external);7 textual occurrences; all5 full bodies replay after mechanical signature generalization; native exact293-name audit independently matches5 direct constant consumers.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.genWronskian.md).

### Completed: `Roth.kronecker`

- Type: `∀ {K : Type u_1} [Field K] {σ : Type u_2} [Fintype σ], ℕ → MvPolynomial σ K →ₐ[K] Polynomial K`
- What: Chosen-enumeration Kronecker power substitution from multivariate to univariate polynomials.
- How: Existing MvPolynomial.aeval with generator j mapped to Polynomial.X ^ k ^ rank(j).
- Hypotheses: Field K, definition weakens to CommSemiring, Fintype σ supplies chosen enumeration; explicit weights require no finite variable type, k arbitrary natural; no degree/injectivity/characteristic hypotheses
- Project dependencies: None
- Caller summary: 9 explicit same-module callers;17 identifier occurrences on15 lines; zero external-to-file callers. Full declaring-module proof replay inlines existing aeval and removes the definition. Canonical293 ordered audit independently records constant consumers.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.kronecker.md).

### Completed: `Roth.kroneckerExp`

- Type: `∀ {σ : Type u_1} [Fintype σ], ℕ → (σ →₀ ℕ) → ℕ`
- What: Natural positional exponent sum for Kronecker substitution under the chosen finite enumeration.
- How: Sums d j * k ^ rank(j); existing Finsupp.weight specializes with power weights, independently of any coefficient field.
- Hypotheses: Fintype σ supplies finite summation and chosen equivFin enumeration, k arbitrary natural, d finitely supported natural exponent vector, No K, Field K, l, characteristic, base lower bound, or digit bound in elaborated type
- Project dependencies: None
- Caller summary: 3 explicit source callers on6 code lines (6 occurrences), zero external-to-file; one extra docstring occurrence. Full module replay migrates all applications/unfolding lists and reaches exists_genWronskian_ne_zero. Canonical293 value audit has4 direct consumers, additionally kronecker_eq_zero_iff via elaboration.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.kroneckerExp.md).

### Completed: `Roth.kronHasse`

- Type: `{K : Type u_1} →
  [inst : Field K] → {σ : Type u_2} → [Fintype σ] → ℕ → (σ →₀ ℕ) → MvPolynomial σ K → Polynomial K`
- What: Composes a multivariate Hasse derivative with Kronecker substitution, as a polynomial-valued function.
- How: Composes hasseDeriv pointwise with kronecker; represented as a function into univariate polynomials.
- Hypotheses: A field, a finite variable enumeration, a base, and a derivative multi-index. Actual kernel type retains Field and Fintype sigma; no characteristic-zero, positive-base or positive-order premise.
- Project dependencies: MvPolynomial.hasseDeriv, Roth.kronecker
- Caller summary: 4 explicit source caller declarations, all in GenWronskian.lean; 5 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.kronHasse.md).

### Completed: `Roth.kronSpan`

- Type: `{K : Type u_1} →
  [inst : Field K] →
    {σ : Type u_2} → [Fintype σ] → ℕ → ℕ → Submodule (Polynomial K) (MvPolynomial σ K → Polynomial K)`
- What: The polynomial-module span of substituted Hasse operators with total order at most the natural bound.
- How: Uses Submodule.span of the image of kronHasse over the degree-bounded exponent set.
- Hypotheses: A field, finite variable enumeration, and natural base and order bound. Actual kernel type retains Field and Fintype sigma; no characteristic-zero, positive-base or positive-order premise.
- Project dependencies: Roth.kronHasse
- Caller summary: 2 explicit source caller declarations, all in GenWronskian.lean; 2 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.kronSpan.md).

### Completed: `Roth.genWronskian_eq_zero_of_not_linearIndependent`

- Type: `∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} {l : ℕ} (D : Fin l → σ →₀ ℕ) {φ : Fin l → MvPolynomial σ K}, ¬LinearIndependent K φ → Roth.genWronskian D φ = 0`
- What: Linearly dependent polynomial families have zero generalized Hasse Wronskian for every row multi-index.
- How: Extract a nontrivial constant relation, transport through each linear Hasse operator, and apply the domain matrix kernel criterion.
- Hypotheses: Field K, arbitrary σ, no Fintype/Finite assumption, D : Fin l → σ →₀ ℕ, φ : Fin l → MvPolynomial σ K, ¬LinearIndependent K φ
- Project dependencies: Roth.genWronskian, MvPolynomial.hasseDeriv
- Caller summary: Zero source callers; canonical293 native audit found zero direct proof consumers. Analogous univariate easy direction is separate, not caller.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.genWronskian_eq_zero_of_not_linearIndependent.md).

### Completed: `Roth.kronecker_monomial`

- Type: `∀ {K : Type u_1} [Field K] {σ : Type u_2} [Fintype σ] (k : ℕ) (d : σ →₀ ℕ) (a : K), Roth.kronecker k (MvPolynomial.monomial d a) = Polynomial.C a * Polynomial.X ^ Roth.kroneckerExp k d`
- What: Computes the image of a coefficient-bearing monomial under geometric-power Kronecker substitution.
- How: Specializes MvPolynomial.aeval_monomial and normalizes product of powers to a power with weighted-sum exponent.
- Hypotheses: Field K and Fintype σ belong to fixed parent interfaces, Arbitrary natural k and finitely supported natural d; arbitrary a, No lower-base bound, digit bound, CharZero or l parameter
- Project dependencies: Roth.kronecker, Roth.kroneckerExp
- Caller summary: One explicit internal caller Roth.coeff_kronecker at GenWronskian.lean93; no external explicit references. Canonical293 exact-order value audit has same sole direct consumer. Full caller replay without target passes.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.kronecker_monomial.md).

### Completed: `Roth.kroneckerExp_injOn`

- Type: `∀ {σ : Type u} [Fintype σ] {k : ℕ}, 1 < k → Set.InjOn (Roth.kroneckerExp k) {d | ∀ j : σ, d j < k}`
- What: Uniqueness of bounded positional natural exponent vectors under Kronecker weighted sum.
- How: Convert enumerated Finsupp digits to List.ofFn, identify weighted sum with Nat.ofDigits, apply equal-length digit uniqueness, and transport list equality back.
- Hypotheses: Arbitrary universe σ, Fintype σ supplies canonical enumeration, Natural k and 1<k; hk verified removable even at original interface, Coordinate digits strictly less than k; no coefficient field or family-size parameter
- Project dependencies: Roth.kroneckerExp
- Caller summary: One explicit same-file caller Roth.coeff_kronecker97; exact canonical293 direct-consumer audit agrees. Full caller replay using new bridge passes, additionally dropping unused hk. No actual production change or completed next assessment.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.kroneckerExp_injOn.md).

### Completed: `Roth.coeff_kronecker`

- Type: `∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] {k : ℕ},
  1 < k →
    ∀ {P : MvPolynomial σ K},
      (∀ (j : σ), MvPolynomial.degreeOf j P < k) →
        ∀ {d : σ →₀ ℕ}, (∀ (j : σ), d j < k) → ((Roth.kronecker k) P).coeff (Roth.kroneckerExp k d) = P.coeff d`
- What: Bounded Kronecker substitution preserves each admissible monomial coefficient.
- How: Expand into monomials and isolate the coefficient using bounded positional injectivity.
- Hypotheses: Field K, Fintype sigma, 1 < k, each partial degree of P < k, each entry of d < k
- Project dependencies: Roth.kronecker, Roth.kroneckerExp, Roth.kronecker_monomial, Roth.kroneckerExp_injOn
- Caller summary: One same-module explicit and canonical direct consumer: Roth.kronecker_eq_zero_iff at111; no external-to-file explicit reference.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_kronecker.md).

### Completed: `Roth.kronecker_eq_zero_iff`

- Type: `∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] {k : ℕ},
  1 < k → ∀ {P : MvPolynomial σ K}, (∀ (j : σ), MvPolynomial.degreeOf j P < k) → ((Roth.kronecker k) P = 0 ↔ P = 0)`
- What: The Kronecker substitution detects zero under individual-degree bounds.
- How: Every support exponent lies in the bounded radix box; coefficient recovery prevents cancellation. Reverse direction is map_zero.
- Hypotheses: Field K, Fintype σ, k : ℕ, 1 < k, P : MvPolynomial σ K, ∀ j, degreeOf j P < k
- Project dependencies: Roth.kronecker, Roth.coeff_kronecker
- Caller summary: named: 1; callers: Roth.linearIndependent_kronecker; outside declaring file: 0; full replay: PASS
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.kronecker_eq_zero_iff.md).

### Completed: `Roth.linearIndependent_kronecker`

- Type: `∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] {l k : ℕ},
  1 < k →
    ∀ {φ : Fin l → MvPolynomial σ K},
      (∀ (ν : Fin l) (j : σ), MvPolynomial.degreeOf j (φ ν) < k) →
        LinearIndependent K φ → LinearIndependent K fun ν ↦ (Roth.kronecker k) (φ ν)`
- What: Kronecker substitution preserves linear independence of a family whose individual variable degrees are below the base.
- How: Pull scalar relations back using degree-bounded zero detection. Verified alternate proof puts the family span inside AddMonoidAlgebra.supported, uses restricted monomial-evaluation injectivity, then existing LinearIndependent.map_injOn.
- Hypotheses: coefficients: Field K in current parent interface; CommSemiring after reaim; variables: Fintype σ for chosen enumeration; arbitrary σ with weights or explicit e:σ≃Fin n; family: Fin l current; arbitrary index verified; base: 1<k current; hypothesis removable in support-based proof; bounds: ∀i j, degreeOf j (φ i)<k, or support containment in separated S; independence: LinearIndependent coefficients φ remains essential
- Project dependencies: Roth.kronecker, Roth.kronecker_eq_zero_iff
- Caller summary: explicit callers: Roth.exists_genWronskian_ne_zero; explicit count: 1; outside declaring file: 0; inline rederivations: 0; canonical audit: all293 ordered unique/present/value declarations; sole direct consumer matches
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.linearIndependent_kronecker.md).

### Completed: `Roth.derivative_aeval`

- Type: `@Roth.derivative_aeval : ∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] (γ : σ → Polynomial K)
  (P : MvPolynomial σ K),
  Polynomial.derivative ((MvPolynomial.aeval γ) P) =
    ∑ j, Polynomial.derivative (γ j) * (MvPolynomial.aeval γ) ((MvPolynomial.pderiv j) P)`
- What: Algebraic multivariate chain rule for polynomial coordinate substitution.
- How: Polynomial induction on constants, addition and multiplication by one variable; simplification uses Leibniz.
- Hypotheses: Field K (verified weakenable to CommSemiring R), Fintype σ for the univ-sum spelling, Arbitrary γ : σ → Polynomial K and P : MvPolynomial σ K, No CharZero or l parameter
- Project dependencies: None
- Caller summary: One same-file explicit caller: private Roth.derivative_kronHasse_aux at GenWronskian.lean:159; zero external-to-file callers; exact293 canonical audit confirms direct consumer.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.derivative_aeval.md).

### Completed: `Roth.derivative_kronHasse_aux`

- Type: `∀ {K : Type u_1} [inst : Field K] {σ : Type u_2}
  [inst_1 : Fintype σ] (k : ℕ) (d : σ →₀ ℕ),
  (fun P ↦ Polynomial.derivative (Roth.kronHasse✝ k d P)) =
    ∑ j,
      (Polynomial.derivative (Polynomial.X ^ k ^ ↑((Fintype.equivFin σ) j)) * Polynomial.C ↑(d j + 1)) •
        Roth.kronHasse✝ k (d + Finsupp.single j 1)`
- What: Differentiating a substituted Hasse operator is a polynomial-coefficient sum of next-order substituted Hasse operators.
- How: Combines derivative_aeval with pderiv_hasseDeriv, moving the scalar coefficient through kronecker.
- Hypotheses: A field, finite variable enumeration, and arbitrary base and derivative exponent. Actual kernel type retains Field and Fintype sigma; no characteristic-zero, positive-base or positive-order premise.
- Project dependencies: Roth.derivative_aeval, MvPolynomial.pderiv_hasseDeriv, Roth.kronHasse, Roth.kronecker
- Caller summary: 1 explicit source caller declarations, all in GenWronskian.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.derivative_kronHasse_aux.md).

### Completed: `Roth.derivative_mem_kronSpan`

- Type: `∀ {K : Type u_1} [inst : Field K] {σ : Type u_2}
  [inst_1 : Fintype σ] (k μ : ℕ) {F : MvPolynomial σ K → Polynomial K},
  F ∈ Roth.kronSpan✝ k μ → (fun P ↦ Polynomial.derivative (F P)) ∈ Roth.kronSpan✝ k (μ + 1)`
- What: Ordinary differentiation sends every operator in the order-mu substituted Hasse span into the order-(mu+1) span.
- How: Uses Submodule.span_induction: derivative_kronHasse_aux handles generators; sums are preserved; Polynomial.derivative_mul handles scalar multiplication, and span_mono embeds old-order operators.
- Hypotheses: A field and finite variable enumeration; the operator lies in kronSpan k μ. Actual kernel type retains Field and Fintype sigma; no characteristic-zero, positive-base or positive-order premise.
- Project dependencies: Roth.derivative_kronHasse_aux, Roth.kronSpan
- Caller summary: 1 explicit source caller declarations, all in GenWronskian.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.derivative_mem_kronSpan.md).

### Completed: `Roth.hasseDeriv_kronecker_mem`

- Type: `∀ {K : Type u_1} [inst : Field K] {σ : Type u_2}
  [inst_1 : Fintype σ] [CharZero K] (k μ : ℕ),
  (fun P ↦ (Polynomial.hasseDeriv μ) ((Roth.kronecker k) P)) ∈ Roth.kronSpan✝ k μ`
- What: Every univariate Hasse derivative of the Kronecker substitution operator lies in the corresponding bounded substituted-Hasse span.
- How: Inducts on μ, starts with the zero multi-index generator, uses derivative_mem_kronSpan, and divides by the nonzero successor integer via Polynomial.hasseDeriv_comp.
- Hypotheses: Characteristic zero field and a finite variable enumeration. Actual kernel type retains Field, Fintype sigma and CharZero; no positive-base or positive-order premise.
- Project dependencies: Roth.derivative_mem_kronSpan, Roth.kronSpan, Roth.kronHasse, Roth.kronecker
- Caller summary: 1 explicit source caller declarations, all in GenWronskian.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.hasseDeriv_kronecker_mem.md).

### Completed: `Roth.exists_hasseDeriv_kronecker_eq_sum`

- Type: `@Roth.exists_hasseDeriv_kronecker_eq_sum : ∀ {K : Type u_1} [Field K] {σ : Type u_2} [Fintype σ] [CharZero K] (k μ : ℕ), ∃ (s : Finset (σ →₀ ℕ)) (c : (σ →₀ ℕ) → Polynomial K), (∀ d ∈ s, d.degree ≤ μ) ∧ ∀ P : MvPolynomial σ K, Polynomial.hasseDeriv μ (Roth.kronecker k P) = ∑ d ∈ s, c d * Roth.kronecker k (MvPolynomial.hasseDeriv d P)`
- What: Uniform finite polynomial linear combination of substituted multivariate Hasse derivatives of order at most μ for a Kronecker pullback.
- How: Extract supported Finsupp coefficients from private order-filtered span membership; membership uses derivative stability, induction and successor-scalar division.
- Hypotheses: Field K and CharZero K in original, Fintype σ fixes concrete Kronecker enumeration, arbitrary natural k and μ; no k>1, degree bounds or l
- Project dependencies: Roth.hasseDeriv_kronecker_mem (private), Roth.kronSpan (private), Roth.kronHasse (private), Roth.kronecker, MvPolynomial.hasseDeriv
- Caller summary: One explicit same-file consumer Roth.exists_genWronskian_ne_zero at line260; canonical exact293 direct-consumer audit agrees. Full caller replays against strongest generalized theorem.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_hasseDeriv_kronecker_eq_sum.md).

### Completed: `Roth.det_sum_rows`

- Type: `@Roth.det_sum_rows {l : ℕ} {A : Type u_3} [CommRing A] {ι : Type u_4} (s : Fin l → Finset ι)
  (c : Fin l → ι → A) (N : Fin l → ι → Fin l → A) :
  (Matrix.of fun μ ν ↦ ∑ i ∈ s μ, c μ i * N μ i ν).det =
    ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Matrix.of fun μ ν ↦ N μ (f μ) ν).det`
- What: Expand determinant whose rows are finite linear combinations into finite choices, weighted by coefficient products.
- How: Specialize existing multilinear finite-sum law, extract simultaneous scalars, normalize function/matrix/scalar representations.
- Hypotheses: CommRing A; arbitrary A, no field/domain/characteristic condition, Fin l square matrix; arbitrary summand type ι; finite support per row, arbitrary s,c,N with no nonempty/nonzero assumptions
- Project dependencies: None
- Caller summary: One explicit same-file private caller wronskian_kronecker_eq_sum_aux at line245, no external-to-file caller. Exact293 canonical audit agrees; clean full caller replay available.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.det_sum_rows.md).

### Completed: `Roth.wronskian_kronecker_eq_sum_aux`

- Type: `∀ {K : Type u_1} [inst : Field K] {σ : Type u_2}
  [inst_1 : Fintype σ] {l : ℕ} (k : ℕ) (φ : Fin l → MvPolynomial σ K) (s : Fin l → Finset (σ →₀ ℕ))
  (c : Fin l → (σ →₀ ℕ) → Polynomial K),
  (∀ (μ ν : Fin l),
      (Polynomial.hasseDeriv ↑μ) ((Roth.kronecker k) (φ ν)) =
        ∑ d ∈ s μ, c μ d * (Roth.kronecker k) ((hasseDeriv d) (φ ν))) →
    (Roth.wronskian fun ν ↦ (Roth.kronecker k) (φ ν)) =
      ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Roth.kronecker k) (Roth.genWronskian f φ)`
- What: Expands the Wronskian after Kronecker substitution as a finite polynomial-coefficient sum of substituted generalized Wronskians, given the derivative-row expansions.
- How: Uses det_sum_rows and compatibility AlgHom.map_det to move Kronecker substitution through the determinant.
- Hypotheses: A field, finite variable enumeration, and supplied finite expansion formulas for each univariate derivative row. Actual kernel type retains Field and Fintype sigma; no characteristic-zero, positive-base or positive-order premise.
- Project dependencies: MvPolynomial.hasseDeriv, Roth.det_sum_rows, Roth.genWronskian, Roth.kronecker, Roth.wronskian, Roth.wronskianMatrix
- Caller summary: 1 explicit source caller declarations, all in GenWronskian.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.wronskian_kronecker_eq_sum_aux.md).

### Completed: `Roth.exists_genWronskian_ne_zero`

- Type: `@Roth.exists_genWronskian_ne_zero.{u_1, u_2} {K : Type u_1} [Field K] {σ : Type u_2} {l : ℕ} [Finite σ] [CharZero K]
  {φ : Fin l → MvPolynomial σ K} (h : LinearIndependent K φ) :
  ∃ D, (∀ (μ : Fin l), Finsupp.degree (D μ) ≤ ↑μ) ∧ Roth.genWronskian D φ ≠ 0`
- What: A linearly independent finite family of multivariate polynomials has a nonzero Hasse Wronskian with total derivative order at most each row index.
- How: Choose bounded injective Kronecker substitution, use univariate nonvanishing, expand higher substituted derivatives and determinant, contradict simultaneous vanishing.
- Hypotheses: Field K, CharZero K: essential for bounded row-order theorem, Finite σ: removable by verified finite-support restriction/rename proof, φ : Fin l → MvPolynomial σ K; LinearIndependent K φ; no positive l or nonempty σ assumption
- Project dependencies: Roth.genWronskian, Roth.exists_hasseDeriv_kronecker_eq_sum, Roth.wronskian_ne_zero_of_linearIndependent, Roth.linearIndependent_kronecker, private Roth.wronskian_kronecker_eq_sum_aux
- Caller summary: One explicit external-to-file caller: private Roth.exists_rat_factors_det_hasseDeriv_aux, Separation:524; exact293 canonical direct-consumer audit agrees; full caller replay with stronger theorem passes.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_genWronskian_ne_zero.md).

### Completed: `Roth.sqrt_one_sub_inv_lt`

- Type: `Roth.sqrt_one_sub_inv_lt {m : ℕ} (hm : 2 ≤ m) {lam : ℝ} (hlam : 2 * √↑m < lam) : √(1 - 1 / ↑m) < 1 - lam⁻¹ ^ 2`
- What: Strict square-root bound by an inverse-square threshold for a dimension parameter.
- How: Square the positive λ bound, compare reciprocals, reduce sqrt inequality to a polynomial inequality.
- Hypotheses: m : ℕ, 2 ≤ m, lam : ℝ, 2 * √(m : ℝ) < lam
- Project dependencies: None
- Caller summary: Exactly one explicit and canonical direct caller: Roth.sum_inv_lt, Lattice.lean:87. No separate inline rederivation found.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.sqrt_one_sub_inv_lt.md).

### Completed: `Roth.inv_add_inv_le`

- Type: `∀ {lam x : ℝ},
  2 < lam → 0 ≤ x → x ≤ 2 → (lam - 1 + x)⁻¹ + (lam - 1 + (2 - x))⁻¹ ≤ 2 * lam / (lam ^ 2 - 1)`
- What: Bounds the sum of two complementary reciprocal terms by twice the endpoint harmonic factor.
- How: Combines reciprocals with inv_add_inv, clears positive denominators, and uses x(2−x)≥0.
- Hypotheses: Real λ greater than two and x in the closed interval [0,2]. The exact type is over real numbers and natural grid sizes as printed; no additional project-defined structure is captured.
- Project dependencies: None
- Caller summary: 1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.inv_add_inv_le.md).

### Completed: `Roth.sum_inv_le`

- Type: `∀ {r : ℕ},
  1 ≤ r →
    ∀ {lam : ℝ}, 2 < lam → ∑ j ∈ Finset.range (r + 1), (lam - 1 + 2 * ↑j / ↑r)⁻¹ ≤ (↑r + 1) * (lam / (lam ^ 2 - 1))`
- What: Bounds the reciprocal arithmetic-grid sum by (r+1)*lambda/(lambda^2-1), using complementary-term pairing.
- How: Pairs each term j with r−j using inv_add_inv_le and Finset.sum_range_reflect, then divides the paired-sum estimate by two.
- Hypotheses: Positive natural r and real λ greater than two. The exact type is over real numbers and natural grid sizes as printed; no additional project-defined structure is captured.
- Project dependencies: Roth.inv_add_inv_le
- Caller summary: 1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.sum_inv_le.md).

### Completed: `Roth.sum_inv_lt`

- Type: `Roth.sum_inv_lt {r m : ℕ} (hr : 1 ≤ r) (hm : 2 ≤ m) {lam : ℝ} (hlam : 2 * √↑m < lam) : ∑ j ∈ Finset.range (r + 1), (lam - 1 + 2 * ↑j / ↑r)⁻¹ < lam⁻¹ * (√(↑m - 1))⁻¹ * √↑m * (↑r + 1)`
- What: Strict bound for reciprocal arithmetic-grid sum by (r+1)√m/(λ√(m−1)), for r≥1,m≥2,λ>2√m.
- How: Pair j with r−j to obtain rational endpoint bound; compare 1−λ⁻² with √(1−1/m), then normalize roots/inverses.
- Hypotheses: r,m:ℕ, 1≤r, 2≤m, lam:ℝ, 2√m<lam
- Project dependencies: private Roth.sum_inv_le, Roth.sqrt_one_sub_inv_lt
- Caller summary: explicit source callers: {'file': 'Roth/Lattice.lean', 'line': 173, 'declaration': 'Roth.card_filter_weight_le_succ_aux', 'visibility': 'private'}; external to file: 0; canonical kernel direct consumers: _private.Roth.Lattice.0.Roth.card_filter_weight_le_succ_aux; scope: Source refs and exact canonical direct value dependencies; not transitive simp/kernel closure.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.sum_inv_lt.md).

### Completed: `Roth.extend_apply_castSucc`

- Type: `∀ {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ) (j : Fin m),
  (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i) j.castSucc = d j`
- What: Extending a vector by a last coordinate preserves all earlier coordinates.
- How: Finsupp.mapDomain_apply_of_injective computes the embedded earlier coordinate and the disjoint single last-coordinate contribution vanishes.
- Hypotheses: A finite coordinate set Fin m, a finitely supported vector, and a natural last coordinate. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: None
- Caller summary: 1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.extend_apply_castSucc.md).

### Completed: `Roth.extend_apply_last`

- Type: `∀ {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ),
  (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i) (Fin.last m) = i`
- What: Extending a vector by a last coordinate assigns that last coordinate its prescribed value.
- How: Finsupp.mapDomain_of_notMem_range makes the embedded vector vanish at Fin.last.
- Hypotheses: A vector on Fin m and an arbitrary natural last coordinate. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: None
- Caller summary: 1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.extend_apply_last.md).

### Completed: `Roth.card_filter_box_fiber_aux`

- Type: `∀ {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop)
  [inst : DecidablePred p] {i : ℕ},
  i ≤ r (Fin.last m) →
    {d ∈ Roth.box (r ∘ Fin.castSucc) | p (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i)}.card =
      {d ∈ Finset.filter p (Roth.box r) | d (Fin.last m) = i}.card`
- What: A fixed last-coordinate fiber of a filtered rectangular box has the same cardinality as the smaller box filtered after extension by that coordinate.
- How: Constructs a Finset.card_bij with extension, proves coordinate bounds using extend_apply_castSucc/extend_apply_last, and reconstructs the inverse by restriction to earlier coordinates.
- Hypotheses: A natural rectangular box, a decidable predicate, and a last coordinate within its bound. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: Roth.extend_apply_castSucc, Roth.extend_apply_last, Roth.mem_box, Roth.box
- Caller summary: 1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_filter_box_fiber_aux.md).

### Completed: `Roth.card_filter_box_last`

- Type: `∀ {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop)
  [inst : DecidablePred p],
  (Finset.filter p (Roth.box r)).card =
    ∑ i ∈ Finset.range (r (Fin.last m) + 1),
      {d ∈ Roth.box (r ∘ Fin.castSucc) | p (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i)}.card`
- What: Count a filtered bounded natural multi-index box by last-coordinate sections.
- How: Existing finite fibre cardinality theorem; mem_box range containment; private bijection identifies each smaller filtered box.
- Hypotheses: m natural, arbitrary natural coordinate bounds r, arbitrary full-vector predicate p, DecidablePred p. No positivity or nonempty hypothesis.
- Project dependencies: Roth.box, Roth.mem_box, Roth.card_filter_box_fiber_aux
- Caller summary: One same-file explicit caller at Lattice175: private card_filter_weight_le_succ_aux; same one canonical direct value consumer. Actual caller body replayed with fresh target and actual private other helper.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_filter_box_last.md).

### Completed: `Roth.filter_weight_le_eq_empty`

- Type: `∀ {m : ℕ} (r : Fin m → ℕ) {lam : ℝ},
  ↑m < lam → {d ∈ Roth.box r | Roth.weight r d ≤ (↑m - lam) / 2} = ∅`
- What: The weighted filtered box is empty when lambda is greater than the dimension.
- How: Combines weight_nonneg with the strictly negative threshold to contradict membership.
- Hypotheses: Natural rectangular bounds and λ greater than the dimension; no positivity of coordinate bounds. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: Roth.weight_nonneg, Roth.box, Roth.weight
- Caller summary: 1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.filter_weight_le_eq_empty.md).

### Completed: `Roth.card_filter_fiber_eq`

- Type: `∀ {n : ℕ} (r : Fin (n + 1) → ℕ) (lam : ℝ) (i : ℕ),
  ↑{d ∈ Roth.box (r ∘ Fin.castSucc) |
          Roth.weight r (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last n) i) ≤
            (↑(n + 1) - lam) / 2}.card =
    ↑{d ∈ Roth.box (r ∘ Fin.castSucc) |
          Roth.weight (r ∘ Fin.castSucc) d ≤ (↑n - (lam - 1 + 2 * ↑i / ↑(r (Fin.last n)))) / 2}.card`
- What: Rewrites the weighted last-coordinate fiber as a smaller box with lambda shifted by the last-coordinate contribution.
- How: Uses weight_add, weight_mapDomain and weight_single, then rearranges the real expression.
- Hypotheses: Natural box bounds, real λ, and any chosen last coordinate. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: Roth.weight_add, Roth.weight_mapDomain, Roth.weight_single, Roth.box, Roth.weight
- Caller summary: 1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_filter_fiber_eq.md).

### Completed: `Roth.card_filter_weight_le_of_le_sqrt_aux`

- Type: `∀ (m : ℕ) (r : Fin m → ℕ) {lam : ℝ},
  0 < lam →
    lam ≤ 2 * √↑m → ↑{d ∈ Roth.box r | Roth.weight r d ≤ (↑m - lam) / 2}.card ≤ 2 * √↑m / lam * ∏ j, (↑(r j) + 1)`
- What: Bounds the weighted-filter cardinality by the lattice estimate directly when positive lambda is at most twice the square root of the dimension.
- How: Applies Finset.card_filter_le, card_box, and observes 2√m/λ≥1.
- Hypotheses: Positive λ at most 2√m; natural box bounds. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: Roth.box, Roth.card_box, Roth.weight
- Caller summary: 1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_filter_weight_le_of_le_sqrt_aux.md).

### Completed: `Roth.card_filter_weight_le_succ_aux`

- Type: `∀ {n : ℕ} (r : Fin (n + 1) → ℕ),
  0 < r (Fin.last n) →
    0 < n →
      ∀ {lam : ℝ},
        2 * √↑(n + 1) < lam →
          (∀ {t : ℝ},
              0 < t →
                ↑{d ∈ Roth.box (r ∘ Fin.castSucc) | Roth.weight (r ∘ Fin.castSucc) d ≤ (↑n - t) / 2}.card ≤
                  2 * √↑n / t * ∏ j, (↑((r ∘ Fin.castSucc) j) + 1)) →
            ↑{d ∈ Roth.box r | Roth.weight r d ≤ (↑(n + 1) - lam) / 2}.card ≤ 2 * √↑(n + 1) / lam * ∏ j, (↑(r j) + 1)`
- What: Carries the weighted lattice estimate from the smaller box to a positive last-coordinate extension in the large-lambda regime.
- How: Uses card_filter_box_last and card_filter_fiber_eq, applies the lower-dimensional bound in every fiber, then sum_inv_lt controls the reciprocals and Fin.prod_univ_castSucc restores the box product.
- Hypotheses: At least two coordinates, positive last-coordinate bound, λ>2√(n+1), and the full positive-parameter induction hypothesis for the smaller box. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: Roth.box, Roth.card_filter_box_last, Roth.card_filter_fiber_eq, Roth.sum_inv_lt, Roth.weight
- Caller summary: 1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_filter_weight_le_succ_aux.md).

### Completed: `Roth.card_filter_weight_le`

- Type: `∀ (m : ℕ) (r : Fin m → ℕ),
  (∀ (j : Fin m), 0 < r j) →
    ∀ {lam : ℝ},
      0 < lam → ↑{d ∈ Roth.box r | Roth.weight r d ≤ (↑m - lam) / 2}.card ≤ 2 * √↑m / lam * ∏ j, (↑(r j) + 1)`
- What: Lemma8: lower-tail count of normalized natural lattice vectors in a finite positive rectangular box is at most2sqrt(m)/lambda times total cardinality.
- How: Dimension induction; trivial total-count regime; empty zero/one-dimensional cases; last-coordinate fibres and shifted reciprocal sum in large-tail regime.
- Hypotheses: m natural includes0; r:Fin m→Nat; every rj positive; lambda real strictly positive. Both positivity premises essential by native counterexamples.
- Project dependencies: Roth.box, Roth.weight, Roth.filter_weight_le_eq_empty, Roth.card_filter_weight_le_of_le_sqrt_aux, Roth.card_filter_weight_le_succ_aux
- Caller summary: One explicit source caller MainLemma574 private mul_card_filter_weight_le_aux; same sole direct canonical kernel consumer. Original theorem with actual private helper constants and complete consumer body replayed natively.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.card_filter_weight_le.md).

### Completed: `Roth.index`

- Type: `{σ : Type u_1} → [Fintype σ] → MvPolynomial σ ℝ → (σ → ℝ) → (σ → ℕ) → ℝ`
- What: Minimum reciprocal-parameter weight of the Taylor support, with zero polynomial and zero denominators projected to the project real-valued convention.
- How: sInf of weight image of translated polynomial support. More general existing AddMonoidAlgebra.infDegree computes that finite minimum in WithTop ℝ; untopD 0 restores the project zero convention.
- Hypotheses: Fintype σ is required by Roth.weight global sum, avoidable by Finsupp weighting., P and α real-valued, r natural-valued; no nonzero/positive premises on the definition.
- Project dependencies: Roth.weight, MvPolynomial.taylor
- Caller summary: all explicit callers: 34; identifier occurrences: 60; same file: 16; external declarations: 18; external files: 3; direct kernel value consumers: 39; caveat: Explicit source references and canonical kernel-value references are distinct inventories.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index.md).

### Completed: `Roth.mem_support_taylor_iff`

- Type: `∀ {σ : Type u_1} {P : MvPolynomial σ ℝ} {α : σ → ℝ} {d : σ →₀ ℕ},
  d ∈ ((MvPolynomial.taylor α) P).support ↔ (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0`
- What: Taylor support membership is equivalent to nonvanishing of the corresponding Hasse derivative at the center.
- How: Combines mem_support_iff with the project coeff_taylor identity.
- Hypotheses: A real polynomial and point; no finiteness of the variable type. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: MvPolynomial.coeff_taylor, MvPolynomial.hasseDeriv, MvPolynomial.taylor
- Caller summary: 4 explicit source caller declarations, all in Index.lean; 4 direct original value consumers. Exact separate lists retained. Entire Index module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.mem_support_taylor_iff.md).

### Completed: `Roth.index_le_weight`

- Type: `Roth.index_le_weight.{u_1} {σ : Type u_1} [Fintype σ] {P : MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ} {d : σ →₀ ℕ}
  (h : (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0) : Roth.index P α r ≤ Roth.weight r d`
- What: Nonzero evaluated Hasse coefficient bounds the point index above by its weight.
- How: csInf_le on the finite image of Taylor support, using the private coefficient membership equivalence.
- Hypotheses: arbitrary σ with Fintype σ, real polynomial P and center α, natural parameters r, including zero entries, multi-index d with eval α (hasseDeriv d P) ≠ 0; no P≠0 or positivity assumptions
- Project dependencies: Roth.index, Roth.weight, MvPolynomial.taylor, MvPolynomial.hasseDeriv, MvPolynomial.coeff_taylor, private Roth.mem_support_taylor_iff
- Caller summary: explicit declarations: 6; occurrences: 6; within module: 5; outside module: 1; kernel direct consumers: 6; files: Roth/Index.lean, Roth/Main.lean
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_le_weight.md).

### Completed: `Roth.exists_weight_eq_index`

- Type: `Roth.exists_weight_eq_index.{u_1} {σ : Type u_1} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ)
  (r : σ → ℕ) : ∃ d, (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0 ∧ Roth.weight r d = Roth.index P α r`
- What: A nonzero polynomial has an evaluated Hasse derivative whose weight attains its index.
- How: Set.Nonempty.csInf_mem on finite nonempty weighted Taylor support, then private coefficient/support equivalence.
- Hypotheses: σ : Type u with Fintype σ, P : MvPolynomial σ ℝ with P≠0, α : σ→ℝ, r : σ→ℕ, allowing zeros; no positivity assumption
- Project dependencies: Roth.index, Roth.weight, MvPolynomial.taylor, MvPolynomial.taylor_eq_zero_iff, MvPolynomial.hasseDeriv, MvPolynomial.coeff_taylor, private Roth.mem_support_taylor_iff
- Caller summary: explicit declarations: 4; occurrences: 4; within module: 3; outside module: 1; kernel direct consumers: 4; files: Roth/Index.lean, Roth/MainLemma.lean
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_weight_eq_index.md).

### Completed: `Roth.le_index_iff`

- Type: `Roth.le_index_iff.{u_1} : ∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ}, P ≠ 0 → ∀ {α : σ → ℝ} {r : σ → ℕ} {c : ℝ}, c ≤ Roth.index P α r ↔ ∀ (d : σ →₀ ℕ), (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0 → c ≤ Roth.weight r d`
- What: A lower bound for a nonzero polynomial's weighted index at a point is equivalent to a common lower bound for all nonvanishing Hasse-derivative weights.
- How: Forward transitivity with index_le_weight; reverse conditional infimum introduction on translated support using coeff_taylor.
- Hypotheses: Fintype variables and real coefficients fixed by parent index/weight; P nonzero needed for zero-default real projection; no positive-r assumption.
- Project dependencies: Roth.index, Roth.weight, Roth.index_le_weight, Roth.mem_support_taylor_iff, MvPolynomial.taylor, MvPolynomial.hasseDeriv, MvPolynomial.coeff_taylor, MvPolynomial.taylor_eq_zero_iff
- Caller summary: Five explicit applications in four callers: le_index_sum twice, index_eq_weightedOrder_div, index_unique, le_index_of_forall_eval_eq_zero; one external module MainLemma. Fresh canonical audit four direct kernel-value consumers.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.le_index_iff.md).

### Completed: `Roth.index_nonneg`

- Type: `Roth.index_nonneg.{u_1} : ∀ {σ : Type u_1} [inst : Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ), 0 ≤ Roth.index P α r`
- What: The weighted index at any real point is nonnegative, including zero polynomial and zero denominator parameters.
- How: Real.sInf_nonneg applied to the image of translated coefficient support; all rational weights are nonnegative.
- Hypotheses: Fintype variables fixed by Roth.weight and Roth.index; no nonvanishing, positive denominator, nonempty variable or DecidableEq hypotheses.
- Project dependencies: Roth.index, Roth.weight, Roth.weight_nonneg, MvPolynomial.taylor
- Caller summary: Three applications in three declarations: Index.index_eq_zero_iff, Theta.Θ_nonneg and Theta.sum_max_sub_le_index_det; K=2 external-to-file applications in one module. Canonical kernel-value audit independently finds the same three direct consumers.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_nonneg.md).

### Completed: `Roth.index_eq_zero_iff`

- Type: `Roth.index_eq_zero_iff.{u_1} {σ : Type u_1} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hr : ∀ j, 0 < r j) (α : σ → ℝ) : Roth.index P α r = 0 ↔ (MvPolynomial.eval α) P ≠ 0`
- What: A nonzero polynomial has weighted index0 at a point iff its evaluation there is nonzero, for positive natural denominator parameters.
- How: Attain the support minimum; nonnegative positive weights have zero only at exponent0; Hasse derivative0 is identity. Converse uses weight0 and nonnegativity.
- Hypotheses: Fintype σ: fixed parent global sum; hP: essential under default0; actual zero-polynomial counterexample; hr: essential for uniform iff; actual Unit X and Bool mixedzero polynomial counterexamples; α: arbitrary center; empty σ allowed
- Project dependencies: Roth.exists_weight_eq_index, Roth.weight_eq_zero_iff, Roth.index_nonneg, Roth.index_le_weight, MvPolynomial.hasseDeriv_zero_apply, Roth.index, Roth.weight, MvPolynomial.taylor
- Caller summary: explicit applications: 1; declarations: Roth.index_prod; external to declaring file: 0; direct kernel value consumers: 1; simp: False; scope: source inventory and direct kernel values, not opaque/transitive/simp closure
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_eq_zero_iff.md).

### Completed: `Roth.index_sub_weight_le_index_hasseDeriv`

- Type: `Roth.index_sub_weight_le_index_hasseDeriv.{u_1} {σ : Type u_1} [Fintype σ] {P : MvPolynomial σ ℝ} {k : σ →₀ ℕ} (hk : (MvPolynomial.hasseDeriv k) P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) : Roth.index P α r - Roth.weight r k ≤ Roth.index ((MvPolynomial.hasseDeriv k) P) α r`
- What: Applying a nonzero Hasse derivative decreases weighted vanishing index by at most the weight of its multi-order.
- How: Choose an attaining derivative; composition gives a nonzero shifted coefficient; compare the original minimum and use additive weights.
- Hypotheses: Finite variable interface, real coefficients, nonzero Hasse derivative. Natural denominators may be zero. Expanded new theorem uses arbitrary sigma, CommRing coefficients and shift-compatible real degree.
- Project dependencies: Roth.index, Roth.weight_add, Roth.exists_weight_eq_index, Roth.index_le_weight, MvPolynomial.hasseDeriv_hasseDeriv, Roth.weight, MvPolynomial.hasseDeriv, MvPolynomial.hasseCoeff
- Caller summary: Two explicit proof callers: sum_max_sub_le_index_det at Theta:390 and private exists_hasseDeriv_index_eval_bound_aux at MainLemma:494. Both complete replays pass after replacement. Two direct canonical kernel consumers.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_sub_weight_le_index_hasseDeriv.md).

### Completed: `Roth.le_index_sum`

- Type: `Roth.le_index_sum.{u_1, u_2} : ∀ {σ : Type u_1} [inst : Fintype σ] {ι : Type u_2} {s : Finset ι}
  {f : ι → MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ},
  ∑ i ∈ s, f i ≠ 0 → ∀ {c : ℝ}, (∀ i ∈ s, f i ≠ 0 → c ≤ Roth.index (f i) α r) → c ≤ Roth.index (∑ i ∈ s, f i) α r`
- What: A common lower bound for the indices of nonzero summands is a lower bound for their nonzero finite sum.
- How: For every nonzero Hasse coefficient of the sum, map_sum and exists_ne_zero_of_sum_ne_zero select a nonzero summand coefficient; its assumed index bound controls the weight.
- Hypotheses: Finite variable interface, real coefficients, arbitrary finite summation type, nonzero sum, common bound for nonzero summands. Natural denominator weights may vanish; no positivity premise.
- Project dependencies: Roth.index, Roth.le_index_iff, Roth.weight, MvPolynomial.hasseDeriv
- Caller summary: One explicit application in Roth.sum_max_sub_le_index_det at Theta.lean398 after determinant expansion; one direct kernel consumer. Entire caller replay with replacement passes.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.le_index_sum.md).

### Completed: `Roth.weight_eq_finsuppWeight_div`

- Type: `∀ {σ : Type u} [Fintype σ] {r : σ → ℕ}, (∀ j, 0 < r j) → ∀ d : σ →₀ ℕ, Roth.weight r d = (Finsupp.weight (fun j ↦ (∏ i, r i) / r j) d : ℝ) / ↑(∏ i, r i)`
- What: Clear reciprocal natural parameter denominators using D=∏r.
- How: Expand weights, cast exact natural quotients, distribute division, cancel nonzero D.
- Hypotheses: Fintype σ; globally positive natural r; arbitrary finitely supported natural d.
- Project dependencies: Roth.weight
- Caller summary: One explicit caller Roth.index_eq_weightedOrder_div, two body rewrites at Index152/155; one audited direct kernel consumer.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.weight_eq_finsuppWeight_div.md).

### Completed: `Roth.index_eq_weightedOrder_div`

- Type: `Roth.index_eq_weightedOrder_div.{u_1} {σ : Type u_1} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ}
  (hr : ∀ (j : σ), 0 < r j) (α : σ → ℝ) :
  Roth.index P α r =
    ↑(MvPowerSeries.weightedOrder (fun j ↦ (∏ i, r i) / r j) ↑((MvPolynomial.taylor α) P)).toNat / ↑(∏ i, r i)`
- What: Identifies reciprocal-weight point index with natural weightedOrder of translated polynomial divided by common denominator.
- How: Finite order attained coefficient gives upper index bound; all support coefficients and weightedOrder_le give lower bound after denominator clearing and finite toNat monotonicity.
- Hypotheses: σ: Type*, Fintype for original full-product interface; P: real multivariate polynomial; hP: P≠0 is removable, verified exact formula allP; r: natural reciprocal denominators; hr: all positive; uniform removal false for mixedzero weights; α: real center
- Project dependencies: Roth.index, Roth.weight_eq_finsuppWeight_div, Roth.index_le_weight, Roth.le_index_iff, MvPolynomial.taylor, MvPolynomial.coeff_taylor
- Caller summary: distinct declarations: 1; proof body applications: 3; statement applications: 0; callers: Roth.index_mul; direct kernel consumers: Roth.index_mul; verified full caller: True
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_eq_weightedOrder_div.md).

### Completed: `Roth.index_mul`

- Type: `Roth.index_mul.{u_1} {σ : Type u_1} [Fintype σ] {P Q : MvPolynomial σ ℝ} (hP : P ≠ 0) (hQ : Q ≠ 0) (α : σ → ℝ)
  {r : σ → ℕ} (hr : ∀ (j : σ), 0 < r j) : Roth.index (P * Q) α r = Roth.index P α r + Roth.index Q α r`
- What: The point index of the product of two nonzero real multivariate polynomials is the sum of the indices.
- How: Clear positive reciprocal denominators to natural weights, translate and coerce into multivariate power series, invoke existing weightedOrder_mul, and project finite ENat values through toNat and real scaling.
- Hypotheses: σ/Fintype and ℝ are fixed parent-interface constraints. hP and hQ are necessary uniformly under real default-zero index; both zero-factor counterexamples compiled. hr is removable: D=∏ max 1 (r i) is positive and D/0=0 provides the natural weight for a zero reciprocal denominator.
- Project dependencies: Roth.index, Roth.index_eq_weightedOrder_div, MvPolynomial.taylor, MvPolynomial.taylor_eq_zero_iff (implicit simp dependency for hfin)
- Caller summary: Two source proof applications: Roth.index_prod at Index185 and private Roth.index_separated_mul_le_aux at Theta438. Exact293 kernel audit independently finds precisely these two consumers. Both entire callers compiled with the hr-free replacement.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_mul.md).

### Completed: `Roth.index_prod`

- Type: `Roth.index_prod.{u_1, u_2} {σ : Type u_1} [Fintype σ] {ι : Type u_2} (s : Finset ι) {f : ι → MvPolynomial σ ℝ}
  (hf : ∀ i ∈ s, f i ≠ 0) (α : σ → ℝ) {r : σ → ℕ} (hr : ∀ (j : σ), 0 < r j) :
  Roth.index (∏ i ∈ s, f i) α r = ∑ i ∈ s, Roth.index (f i) α r`
- What: The index of a finite product of nonzero real multivariate polynomials equals the sum of their indices at a common point and reciprocal weights.
- How: Finset induction: index of one is zero; apply the binary index_mul law to the inserted factor and remaining nonzero product, then the induction hypothesis.
- Hypotheses: σ/Fintype, ℝ and reciprocal natural r belong to the fixed parent interface. ι is arbitrary and s finite; f unrestricted. hf is necessary uniformly because index zero defaults to zero. hr is removable, verified through the all-r binary law and a direct index-one simplification.
- Project dependencies: Roth.index, Roth.index_mul, Roth.index_eq_zero_iff
- Caller summary: One explicit proof-body application: Roth.sum_max_sub_le_index_det at Roth/Theta.lean:407. Exact293 canonical kernel audit independently finds this sole direct consumer. Entire caller replay compiled using the hr-free replacement, with hr renamed _hr preserving position/type.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_prod.md).

### Completed: `Roth.index_neg`

- Type: `Roth.index_neg.{u_1} {σ : Type u_1} [Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : Roth.index (-P) α r = Roth.index P α r`
- What: Negating a polynomial preserves its index at any center and natural weight vector, including zero cases.
- How: Taylor map_neg preserves coefficient support via support_neg; identical weighted support infima.
- Hypotheses: Fintype variable index fixed by parent; arbitrary P, α, r; no positivity/nonzero assumptions.
- Project dependencies: Roth.index, Roth.weight, MvPolynomial.taylor
- Caller summary: 0 explicit statement/body uses, 0 direct kernel consumers among exact canonical293; Theta sign bypasses via broader index_C_mul.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_neg.md).

### Completed: `Roth.index_C_mul`

- Type: `Roth.index_C_mul.{u_1} {σ : Type u_1} [Fintype σ] {c : ℝ} (hc : c ≠ 0) (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : Roth.index (MvPolynomial.C c * P) α r = Roth.index P α r`
- What: Nonzero constant multiplication preserves the weighted Taylor index, including zero polynomials and zero weights.
- How: Taylor multiplication and constant compatibility reduce to support_smul_eq.
- Hypotheses: Fintype fixed by parent; c≠0 essential uniformly by P=X guard; P, α and r arbitrary.
- Project dependencies: Roth.index, Roth.weight, MvPolynomial.taylor, MvPolynomial.taylor_C
- Caller summary: 1 explicit body use at Theta405 in sum_max_sub_le_index_det; same sole direct consumer among exact canonical293; full caller replay passes.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_C_mul.md).

### Completed: `Roth.index_mul_left_weights`

- Type: `Roth.index_mul_left_weights.{u_1} {σ : Type u_1} [Fintype σ] {l : ℕ} (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
  (Roth.index P α fun j ↦ l * r j) = Roth.index P α r / ↑l`
- What: Scaling all natural denominator parameters by l divides the polynomial index by l, including l=0.
- How: Normalize the image of weighted Taylor support by weight_mul_left, then Real.sInf_smul_of_nonneg. Generic re-aim is map_finset_inf on infDegree.
- Hypotheses: Arbitrary σ : Type u with Fintype, real polynomial P and center α, r : σ→ℕ, l : ℕ. No positivity/nonzero premises.
- Project dependencies: Roth.index, Roth.weight, Roth.weight_mul_left, MvPolynomial.taylor
- Caller summary: One private caller Roth.index_separated_mul_le_aux, Roth/Theta.lean:447, applies twice at hUΘ/hVΘ; full caller replay accepted. One direct canonical kernel consumer.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_mul_left_weights.md).

### Completed: `Roth.index_rename`

- Type: `Roth.index_rename.{u_1, u_2} {σ : Type u_1} [Fintype σ] {τ : Type u_2} [Fintype τ] {f : σ → τ}
  (hf : Function.Injective f) (P : MvPolynomial σ ℝ) (α : τ → ℝ) (r : τ → ℕ) :
  Roth.index ((MvPolynomial.rename f) P) α r = Roth.index P (α ∘ f) (r ∘ f)`
- What: Injective variable renaming preserves the centered weighted polynomial index after pulling back center and denominator weights.
- How: Commute translation with rename, identify support image under mapDomain, preserve weights and take the same finite-support minimum.
- Hypotheses: Finite σ,τ in current parent interface; f injective; arbitrary P, α, r with zero polynomial/denominators allowed. Injection prevents cancellation; all other constraints are parent formation.
- Project dependencies: Roth.index, MvPolynomial.taylor, Roth.weight, MvPolynomial.taylor_rename, Roth.weight_mapDomain
- Caller summary: Two direct private Theta consumers, three proof applications on two source lines; full old-target-free replacement caller replays compile.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_rename.md).

### Completed: `Roth.index_le_card`

- Type: `Roth.index_le_card.{u_1} : ∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ}, P ≠ 0 → ∀ {r : σ → ℕ}, (∀ j, MvPolynomial.degreeOf j P ≤ r j) → ∀ α : σ → ℝ, Roth.index P α r ≤ ↑(Fintype.card σ)`
- What: Coordinate degree bounds by denominator parameters imply index at most number of variables.
- How: Choose a nonzero Taylor coefficient attaining the minimum; compare its coordinates with Taylor degrees and original degree bounds; sum quotients bounded by one.
- Hypotheses: Fintype σ, real P, arbitrary center α, natural denominators r, hP≠0, coordinate degree bounds. hP independently verified droppable under project real-default0 convention; not droppable under canonical∞.
- Project dependencies: Roth.index, Roth.exists_weight_eq_index, Roth.weight_le_card, MvPolynomial.degreeOf_taylor_le, Roth.mem_support_taylor_iff (private)
- Caller summary: Exactly two source proof applications and two direct canonical kernel consumers: indexSet_bddAbove and Θ_le_card. Both complete proofs replay cleanly using independently proved noNonzero and discarding map nonzero arguments.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_le_card.md).

### Completed: `Roth.index_unique`

- Type: `@Roth.index_unique : ∀ {σ : Type u_1} [inst : Fintype σ] [inst_1 : Unique σ] {P : MvPolynomial σ ℝ}, P ≠ 0 → ∀ (α : σ → ℝ) (r : σ → ℕ), Roth.index P α r = ↑(Polynomial.rootMultiplicity (α default) ((MvPolynomial.uniqueAlgEquiv ℝ σ) P)) / ↑(r default)`
- What: In one variable the normalized polynomial index equals root multiplicity divided by the denominator.
- How: Convert Hasse evaluations to coefficients of the univariate Taylor expansion; use least nonzero coefficient and nonnegative division.
- Hypotheses: Fintype σ: fixed weight/index interface; derivable from Unique, Unique σ: exactly one variable and uniqueAlgEquiv, P ≠ 0: removable under zero projection; independently verified, α arbitrary; r natural including zero; no positivity/domain/characteristic-zero assumption
- Project dependencies: Roth.index, Roth.weight, Roth.index_le_weight, Roth.le_index_iff, MvPolynomial.uniqueAlgEquiv_hasseDeriv, MvPolynomial.eval₂_uniqueAlgEquiv
- Caller summary: explicit applications: 1; proof body: 1; statement: 0; files: Roth/Theta.lean:242; callers: private Roth.index_unique_le_log_div; direct kernel value consumers: _private.Roth.Theta.0.Roth.index_unique_le_log_div; inline rederivations: 0; full native replay: IndexUniqueCallers151.logBoundReplay
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_unique.md).

### Completed: `Roth.coeffNone`

- Type: `Roth.coeffNone.{u_1, u_2} : {τ : Type u_1} → {R : Type u_2} → [CommSemiring R] → MvPolynomial (Option τ) R → ℕ → MvPolynomial τ R`
- What: Extract the coefficient polynomial of a distinguished variable power.
- How: Apply MvPolynomial.optionEquivLeft, then Polynomial.coeff.
- Hypotheses: τ: Arbitrary type, no Fintype/DecidableEq; R: CommSemiring, no field/domain/nontriviality; P: Arbitrary polynomial; ν: Arbitrary natural exponent
- Project dependencies: None
- Caller summary: explicit consuming declarations: 7; external to file callers: 0; direct kernel value consumers: Roth.coeff_coeffNone, Roth.eq_sum_X_none_pow_mul_coeffNone, Roth.degreeOf_coeffNone_le, Roth.coeff_rename_mul_aeval, _private.Roth.Separation.0.Roth.eq_sum_aeval_basis_coeffNone_aux, _private.Roth.Separation.0.Roth.exists_coeffNone_basis_aux, Roth.exists_separated_representation; note: Seven same-file consumers; coeff_rename_mul_aeval is body-only. Not simp/transitive closure.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeffNone.md).

### Completed: `Roth.eq_mapDomain_some_add_single`

- Type: `@Roth.eq_mapDomain_some_add_single : ∀ {τ : Type u_1} (d : Option τ →₀ ℕ),
  d = Finsupp.mapDomain some d.some + Finsupp.single none (d none)`
- What: Rebuild an Option-indexed natural multi-index from restriction and distinguished coordinate.
- How: Pointwise extensionality, two Option cases, mapDomain evaluation.
- Hypotheses: τ : Type u_1, d : Option τ →₀ ℕ; no Fintype, DecidableEq, or coefficient-ring instance
- Project dependencies: None
- Caller summary: explicit call sites: {'file': 'Roth/Separation.lean', 'line': 107, 'caller': 'Roth.eq_sum_X_none_pow_mul_coeffNone'}; internal use count excluding declaring file: 0; same file count: 1; direct kernel value consumers: Roth.eq_sum_X_none_pow_mul_coeffNone; inline derivations: coeff_coeffNone at86 independently normalizes inserted coordinates; not a duplicate full reconstruction
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.eq_mapDomain_some_add_single.md).

### Completed: `Roth.coeff_X_none_pow_mul_rename`

- Type: `∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R]
  (ν : ℕ) (Q : MvPolynomial τ R) (e : Option τ →₀ ℕ),
  (MvPolynomial.X none ^ ν * (MvPolynomial.rename some) Q).coeff e = if e none = ν then Q.coeff e.some else 0`
- What: The coefficient of X none ^ ν times rename some Q at e is Q.coeff e.some when e none = ν, and zero otherwise.
- How: Transport by optionEquivLeft and use Polynomial.coeff_monomial after identifying the renamed polynomial with a constant polynomial.
- Hypotheses: Commutative semiring coefficients and arbitrary variables. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: None
- Caller summary: 1 explicit source caller declarations, all in Separation.lean; 1 direct original value consumers. Exact separate lists retained. Entire Separation module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_X_none_pow_mul_rename.md).

### Completed: `Roth.coeff_coeffNone`

- Type: `@Roth.coeff_coeffNone : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (P : MvPolynomial (Option τ) R) (ν : ℕ)
  (d : τ →₀ ℕ), (Roth.coeffNone P ν).coeff d = P.coeff (Finsupp.mapDomain some d + Finsupp.single none ν)`
- What: Extracting exponent d from the coefficient polynomial at distinguished exponent ν recovers the original coefficient at those combined exponents.
- How: Unfold coeffNone, rewrite optionEquivLeft_coeff_coeff, normalize the Option multi-index pointwise.
- Hypotheses: τ : Type u_1, R : Type u_2, CommSemiring R, P : MvPolynomial (Option τ) R; ν : ℕ; d : τ →₀ ℕ, No Fintype τ or DecidableEq τ
- Project dependencies: Roth.coeffNone
- Caller summary: explicit call sites: {'file': 'Roth/Separation.lean', 'line': 107, 'caller': 'Roth.eq_sum_X_none_pow_mul_coeffNone'}, {'file': 'Roth/Separation.lean', 'line': 129, 'caller': 'Roth.coeff_rename_mul_aeval'}; internal use count excluding declaring file: 0; same file count: 2; direct kernel value consumers: Roth.eq_sum_X_none_pow_mul_coeffNone, Roth.coeff_rename_mul_aeval; inline derivations: Private coeff_X_none_pow_mul_rename and degreeOf_coeffNone_le use canonical coefficient/support API, not duplicate full target.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_coeffNone.md).

### Completed: `Roth.eq_sum_X_none_pow_mul_coeffNone`

- Type: `@Roth.eq_sum_X_none_pow_mul_coeffNone : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R]
  (P : MvPolynomial (Option τ) R) {n : ℕ},
  MvPolynomial.degreeOf none P ≤ n →
    P = ∑ ν ∈ Finset.range (n + 1), MvPolynomial.X none ^ ν * (MvPolynomial.rename some) (Roth.coeffNone P ν)`
- What: Expand an Option-variable polynomial with distinguished-variable degree at most n into powers0 through n with polynomial coefficients in the remaining variables.
- How: Source proof compares monomial coefficients, separates the matching distinguished exponent, and uses hn to kill out-of-range coefficients. Canonical refactor transports existing polynomial finite expansion through optionEquivLeft.
- Hypotheses: τ : Type u_1, R : Type u_2, CommSemiring R, P : MvPolynomial (Option τ) R; n : ℕ, degreeOf none P ≤ n, No Fintype τ or DecidableEq τ
- Project dependencies: Roth.coeffNone, Roth.coeff_coeffNone, Roth.eq_mapDomain_some_add_single, private Roth.coeff_X_none_pow_mul_rename
- Caller summary: explicit call sites: {'file': 'Roth/Separation.lean', 'line': 335, 'caller': 'Roth.exists_separated_representation'}; internal use count excluding declaring file: 0; same file count: 1; direct kernel value consumers: Roth.exists_separated_representation; inline derivations: Private basis/reconstruction helpers consume an expansion equality premise; no independent full derivation found.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.eq_sum_X_none_pow_mul_coeffNone.md).

### Completed: `Roth.degreeOf_coeffNone_le`

- Type: `@Roth.degreeOf_coeffNone_le : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (P : MvPolynomial (Option τ) R)
  (ν : ℕ) (j : τ), MvPolynomial.degreeOf j (Roth.coeffNone P ν) ≤ MvPolynomial.degreeOf (some j) P`
- What: Coefficient extraction in one distinguished variable cannot increase the degree in any remaining variable.
- How: Rewrite the coordinate degree bound as support-wise bounds; insert the distinguished exponent using optionEquivLeft support membership; bound that monomial exponent and normalize its some-coordinate.
- Hypotheses: τ : Type u_1; R : Type u_2, CommSemiring R, P : MvPolynomial (Option τ) R; ν : ℕ; j : τ, No Fintype, DecidableEq, nonzero, domain, characteristic or exponent bound assumptions
- Project dependencies: Roth.coeffNone
- Caller summary: explicit call sites: None; internal use count excluding declaring file: 0; same file count: 0; direct kernel value consumers: None; inline derivations: {'file': 'Roth/Separation.lean', 'line': 310, 'caller': 'private Roth.exists_coeffNone_basis_aux', 'detail': 'Span generator coordinate bound uses the same support insertion/monomial estimate inline at lines312–313. Full auxiliary replay through canonical degree bound checked.'}
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_coeffNone_le.md).

### Completed: `Roth.coeff_rename_mul_aeval`

- Type: `@Roth.coeff_rename_mul_aeval : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (U : MvPolynomial τ R)
  (V : Polynomial R) (a : τ →₀ ℕ) (b : ℕ),
  ((MvPolynomial.rename some) U * (Polynomial.aeval (MvPolynomial.X none)) V).coeff
      (Finsupp.mapDomain some a + Finsupp.single none b) =
    U.coeff a * V.coeff b`
- What: A coefficient of a product of polynomials in separate variable blocks is the product of the two corresponding coefficients.
- How: Transport through optionEquivLeft to a univariate polynomial over MvPolynomial τ R; normalize rename to C and aeval to map, then extract the two coefficients.
- Hypotheses: τ arbitrary Type u_1, R arbitrary Type u_2 with CommSemiring R, U : MvPolynomial τ R, V : Polynomial R, a : τ →₀ ℕ, b : ℕ, No Fintype/DecidableEq/domain/nonzero/characteristic assumptions
- Project dependencies: Roth.coeffNone, Roth.coeff_coeffNone
- Caller summary: explicit call sites: {'file': 'Roth/Separation.lean', 'line': 476, 'caller': 'Roth.exists_int_polynomial_of_primitive_factor_aux', 'visibility': 'private'}, {'file': 'Roth/Theta.lean', 'line': 480, 'caller': 'Roth.index_det_le'}, {'file': 'Roth/Theta.lean', 'line': 486, 'caller': 'Roth.index_det_le'}; direct kernel value consumers: _private.Roth.Separation.0.Roth.exists_int_polynomial_of_primitive_factor_aux, Roth.index_det_le; inline derivations: None; notes: Three source uses, two full callers; two external-to-declaring-file uses in one file. Both full callers replayed without assessed target or parent coefficient bridge.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_rename_mul_aeval.md).

### Completed: `Roth.aeval_X_eq_rename`

- Type: `Roth.aeval_X_eq_rename : ∀ {R : Type u_1} [inst : CommSemiring R] {σ : Type u_2} (i : σ) (f : Polynomial R),
  (Polynomial.aeval (MvPolynomial.X i)) f =
    (MvPolynomial.rename fun x ↦ i) ((MvPolynomial.uniqueAlgEquiv R Unit).symm f)`
- What: Embedding a univariate polynomial at a selected multivariate coordinate equals renaming its Unit-variable presentation.
- How: Applies AlgHom.congr_fun to existing Polynomial.toMvPolynomial_eq_rename_comp; no project proof dependencies.
- Hypotheses: R : Type u_1, CommSemiring R, sigma : Type u_2, i : sigma, f : Polynomial R; no finiteness/DecidableEq/domain assumptions
- Project dependencies: None
- Caller summary: explicit call sites: {'caller': 'Roth.hasseDeriv_rename_mul_aeval', 'file': 'Roth/Separation.lean', 'line': 162, 'refactor': 'Replace public wrapper with local specialization AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f; full body replay succeeded.'}, {'caller': 'Roth.degreeOf_rename_mul_aeval', 'file': 'Roth/Separation.lean', 'line': 207, 'refactor': 'Replace public wrapper with local specialization AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f; full body replay succeeded.'}, {'caller': 'Roth.degreeOf_none_rename_mul_aeval', 'file': 'Roth/Separation.lean', 'line': 224, 'refactor': 'Replace public wrapper with local specialization AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f; full body replay succeeded.'}, {'caller': '_private.Roth.Theta.0.Roth.index_separated_mul_le_aux', 'file': 'Roth/Theta.lean', 'line': 437, 'refactor': 'Replace public wrapper with local specialization AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f; full body replay succeeded.'}, {'caller': '_private.Roth.Theta.0.Roth.mapped_det_ne_zero_aux', 'file': 'Roth/Theta.lean', 'line': 528, 'refactor': 'Replace public wrapper with local specialization AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f; full body replay succeeded.'}; direct kernel value consumers: Roth.hasseDeriv_rename_mul_aeval, Roth.degreeOf_rename_mul_aeval, Roth.degreeOf_none_rename_mul_aeval, _private.Roth.Theta.0.Roth.index_separated_mul_le_aux, _private.Roth.Theta.0.Roth.mapped_det_ne_zero_aux; total explicit uses: 5; same file uses: 3; external to file uses: 2; external files: 1; internal use count excluding declaring file: 2; inline derivations: None; scope: Fresh lexical inventory, no-ignore rg, git grep and exact ordered canonical293 direct kernel-value audit; not opaque/simp closure.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.aeval_X_eq_rename.md).

### Completed: `Roth.hasseDeriv_rename_mul_aeval`

- Type: `@Roth.hasseDeriv_rename_mul_aeval.{u_1,
    u_2} : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring.{u_2} R] (d : Finsupp.{u_1, 0} τ ℕ) (ν : ℕ)
  (U : MvPolynomial.{u_1, u_2} τ R) (V : Polynomial.{u_2} R),
  Eq.{max (u_1 + 1) (u_2 + 1)}
    ((MvPolynomial.hasseDeriv.{u_1, u_2}
        (HAdd.hAdd.{u_1, u_1, u_1} (Finsupp.mapDomain.{u_1, u_1, 0} some.{u_1} d)
          (Finsupp.single.{u_1, 0} none.{u_1} ν)))
      (HMul.hMul.{max u_1 u_2, max u_1 u_2, max u_1 u_2} ((MvPolynomial.rename.{u_1, u_1, u_2} some.{u_1}) U)
        ((Polynomial.aeval.{u_2, max u_1 u_2} (MvPolynomial.X.{u_2, u_1} none.{u_1})) V)))
    (HMul.hMul.{max u_1 u_2, max u_1 u_2, max u_1 u_2}
      ((MvPolynomial.rename.{u_1, u_1, u_2} some.{u_1}) ((MvPolynomial.hasseDeriv.{u_1, u_2} d) U))
      ((Polynomial.aeval.{u_2, max u_1 u_2} (MvPolynomial.X.{u_2, u_1} none.{u_1}))
        ((Polynomial.hasseDeriv.{u_2} ν) V)))`
- What: Hasse differentiation of a product in disjoint variable blocks acts on each factor separately.
- How: Split the multi-index into disjoint supports, compose Hasse operators, pull out factors of degree zero in the active variables, and transport each factor derivative through its embedding.
- Hypotheses: arbitrary independent variable/coefficient universes, CommSemiring R, d : τ →₀ ℕ, ν : ℕ, U : MvPolynomial τ R, V : Polynomial R, no Fintype, DecidableEq, characteristic, field, domain or nonzero assumptions
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint, MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero, MvPolynomial.hasseDeriv_single_aeval_X, MvPolynomial.hasseDeriv_rename, Roth.aeval_X_eq_rename
- Caller summary: explicit call sites: {'file': 'Roth/Separation.lean', 'line': 365, 'declaration': 'Roth.det_hasseDeriv_separated', 'plan': 'Use new freshCoordinate law specialized to some/none inside the existing entrywise determinant proof; retain Field signature of this caller.'}; external to file occurrences: 0; direct kernel value consumers: Roth.det_hasseDeriv_separated; inline derivations: None; note: Two lexical occurrences include the declaration itself; one explicit caller within same file. Source-level enumeration and ordered293 kernel audit agree here; neither is transitive simp closure.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.hasseDeriv_rename_mul_aeval.md).

### Completed: `Roth.coeff_uniqueAlgEquiv_symm`

- Type: `Roth.coeff_uniqueAlgEquiv_symm : ∀ {R : Type u_1} [inst : CommSemiring R] {σ : Type u_2} [inst_1 : Unique σ]
  (f : Polynomial R) (n : ℕ), ((MvPolynomial.uniqueAlgEquiv R σ).symm f).coeff (Finsupp.single default n) = f.coeff n`
- What: The coefficient at singleton exponent n in the inverse singleton-variable polynomial equivalence is the ordinary nth coefficient.
- How: Specialize the existing arbitrary-exponent mathlib coefficient law and evaluate the finitely supported singleton at its own index.
- Hypotheses: R and σ independently universe-polymorphic; CommSemiring R and Unique σ; arbitrary f and natural n. No Fintype, DecidableEq, domain or nonzero premise.
- Project dependencies: None
- Caller summary: explicit call sites: None; explicit use count: 0; direct kernel value consumers: None; inline derivations: {'file': 'Roth/Theta.lean', 'line': 429, 'description': 'Uses more general fully qualified MvPolynomial.coeff_uniqueAlgEquiv_symm for arbitrary d coefficient bound; independently replayed exact coefficient subproof only.'}; nearby mathlib uses: Roth/Separation.lean:179, Roth/Separation.lean:182; scope: All canonical production files lexical-enumerated, no-ignore rg and tracked git grep cross-checked. Kernel audit covers293 canonical constants, direct value references only; not arbitrary external or opaque/simp closure.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.coeff_uniqueAlgEquiv_symm.md).

### Completed: `Roth.degreeOf_uniqueAlgEquiv_symm`

- Type: `@Roth.degreeOf_uniqueAlgEquiv_symm : ∀ {R : Type u_1} [inst : CommSemiring R] {σ : Type u_2} [inst_1 : Unique σ]
  (f : Polynomial R), MvPolynomial.degreeOf default ((MvPolynomial.uniqueAlgEquiv R σ).symm f) = f.natDegree`
- What: Identifies the degree in the unique variable of the inverse uniqueAlgEquiv image with the original polynomial natDegree, including zero.
- How: Two coefficient-support inequalities using mathlib coeff_uniqueAlgEquiv_symm directly; independent structural proof uses a newly proved optionSubtypeNe/optionEquivLeft normalization and existing degreeOf_eq_natDegree plus injective map degree.
- Hypotheses: Universe-polymorphic CommSemiring R and Unique sigma; arbitrary polynomial; no nonzero, finite, DecidableEq, domain or field hypotheses.
- Project dependencies: None
- Caller summary: explicit use count: 2; external to file use count: 1; explicit call sites: {'name': 'Roth.degreeOf_none_rename_mul_aeval', 'file': 'Roth/Separation.lean', 'line': 226}, {'name': 'Roth.index_separated_mul_le_aux', 'visibility': 'private', 'file': 'Roth/Theta.lean', 'line': 427}; direct kernel value consumers: Roth.degreeOf_none_rename_mul_aeval, _private.Roth.Theta.0.Roth.index_separated_mul_le_aux; inline derivations: None; complete replays verified: True
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_uniqueAlgEquiv_symm.md).

### Completed: `Roth.degreeOf_rename_mul_aeval`

- Type: `@Roth.degreeOf_rename_mul_aeval : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommRing R] [IsDomain R]
  (U : MvPolynomial τ R) {V : Polynomial R},
  V ≠ 0 →
    ∀ (j : τ),
      MvPolynomial.degreeOf (some j) ((MvPolynomial.rename some) U * (Polynomial.aeval (MvPolynomial.X none)) V) =
        MvPolynomial.degreeOf j U`
- What: Multiplication by a nonzero univariate factor in a disjoint variable preserves every old-variable partial degree, allowing the other factor to be zero.
- How: Split U=0; use degreeOf_mul_eq, injective rename preservation and singleton-renaming normalization to show the other factor contributes zero.
- Hypotheses: arbitrary τ and R universes, CommRing R, IsDomain R, U arbitrary including zero, V≠0, j:τ; no Fintype/DecidableEq assumptions
- Project dependencies: Roth.aeval_X_eq_rename
- Caller summary: explicit use count: 1; external to file use count: 0; explicit call sites: {'file': 'Roth/Separation.lean', 'line': 554, 'caller': 'Roth.exists_det_eq_mul', 'pattern': 'rw [← degreeOf_rename_mul_aeval U hV j, ← hFUV]'}; direct kernel value consumers: Roth.exists_det_eq_mul; inline derivations: None; verified replay: Entire original Finite τ caller checked with inline mathlib proof; target absent from new region.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_rename_mul_aeval.md).

### Completed: `Roth.degreeOf_none_rename_mul_aeval`

- Type: `@Roth.degreeOf_none_rename_mul_aeval : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommRing R] [IsDomain R]
  {U : MvPolynomial τ R},
  U ≠ 0 →
    ∀ (V : Polynomial R),
      MvPolynomial.degreeOf none ((MvPolynomial.rename some) U * (Polynomial.aeval (MvPolynomial.X none)) V) =
        V.natDegree`
- What: The none-variable degree of a separated product U(x_τ)V(x_none) equals V.natDegree for U≠0, including V=0.
- How: Source uses degreeOf_mul_eq, zero degree of renamed U and singleton-variable degree bridge; verified alternative uses optionEquivLeft and constant multiplication natDegree.
- Hypotheses: Arbitrary τ,R; CommRing+IsDomain; U≠0; arbitrary V. Verified weakening CommSemiring+NoZeroDivisors and point-local leading-coefficient nonannihilation.
- Project dependencies: Roth.aeval_X_eq_rename, Roth.degreeOf_uniqueAlgEquiv_symm
- Caller summary: explicit use count: 1; external to file use count: 0; explicit call sites: {'file': 'Roth/Separation.lean', 'line': 557, 'caller': 'Roth.exists_det_eq_mul'}; direct kernel value consumers: Roth.exists_det_eq_mul; inline derivations: None
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_none_rename_mul_aeval.md).

### Completed: `Roth.linearIndependent_coordinate_polynomials_aux`

- Type: `∀ {R : Type u_3} {M : Type u_4}
  [inst : CommRing R] [inst_1 : AddCommMonoid M] [inst_2 : Module R M] {n l : ℕ} (v : Fin (n + 1) → M)
  (b : Module.Basis (Fin l) R ↥(Submodule.span R (Set.range v))),
  LinearIndependent R fun ρ ↦ ∑ ν, Polynomial.C ((b.repr ⟨v ν, ⋯⟩) ρ) * Polynomial.X ^ ↑ν`
- What: Coordinate polynomials obtained by writing a finite spanning family in an arbitrary finite basis are linearly independent.
- How: A vanishing polynomial combination gives coefficient identities; form a linear functional and use LinearMap.ext_on on the spanning family, then evaluate it on basis vectors.
- Hypotheses: Module over a commutative ring with a finite indexed spanning family and basis. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: None
- Caller summary: 1 explicit source caller declarations, all in Separation.lean; 1 direct original value consumers. Exact separate lists retained. Entire Separation module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.linearIndependent_coordinate_polynomials_aux.md).

### Completed: `Roth.eq_sum_aeval_basis_coeffNone_aux`

- Type: `∀ {τ : Type u_1} {R : Type u_3}
  [inst : CommSemiring R] {P : MvPolynomial (Option τ) R} {n l : ℕ},
  P = ∑ ν, MvPolynomial.X none ^ ↑ν * (MvPolynomial.rename some) (Roth.coeffNone P ↑ν) →
    ∀ (b : Module.Basis (Fin l) R ↥(Submodule.span R (Set.range fun ν ↦ Roth.coeffNone P ↑ν))),
      P =
        ∑ ρ,
          (Polynomial.aeval (MvPolynomial.X none))
              (∑ ν, Polynomial.C ((b.repr ⟨Roth.coeffNone P ↑ν, ⋯⟩) ρ) * Polynomial.X ^ ↑ν) *
            (MvPolynomial.rename some) ↑(b ρ)`
- What: The separated expansion of a polynomial can be regrouped in any chosen basis of the span of its coefficient polynomials.
- How: Expand each coefficient with Module.Basis.sum_repr, exchange finite sums, and transport scalars through evaluation and renaming.
- Hypotheses: Commutative semiring, an existing coefficient expansion and a basis of its span. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: Roth.coeffNone
- Caller summary: 1 explicit source caller declarations, all in Separation.lean; 1 direct original value consumers. Exact separate lists retained. Entire Separation module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.eq_sum_aeval_basis_coeffNone_aux.md).

### Completed: `Roth.exists_coeffNone_basis_aux`

- Type: `∀ {τ : Type u_1} {K : Type u_2} [inst : Field K] {P : MvPolynomial (Option τ) K},
  P ≠ 0 →
    ∀ {n : ℕ},
      P = ∑ ν : Fin (n + 1), MvPolynomial.X none ^ ↑ν * (MvPolynomial.rename some) (Roth.coeffNone P ↑ν) →
        ∃ (l : ℕ) (b :
          Module.Basis (Fin l) K ↥(Submodule.span K (Set.range fun (ν : Fin (n + 1)) ↦ Roth.coeffNone P ↑ν))),
          1 ≤ l ∧ l ≤ n + 1 ∧ ∀ (ρ : Fin l) (j : τ), MvPolynomial.degreeOf j ↑(b ρ) ≤ MvPolynomial.degreeOf (some j) P`
- What: The coefficient-polynomial span of a nonzero separated expansion has a finite basis of positive size at most n+1, whose members satisfy the original individual degree bounds.
- How: Use Module.finBasis on the finite coefficient span, derive positive finrank from nonzero expansion, and contain the span in restrictSupport to retain degree bounds.
- Hypotheses: Field coefficients, nonzero polynomial, finite distinguished-variable expansion. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: Roth.coeffNone
- Caller summary: 1 explicit source caller declarations, all in Separation.lean; 1 direct original value consumers. Exact separate lists retained. Entire Separation module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_coeffNone_basis_aux.md).

### Completed: `Roth.exists_separated_representation`

- Type: `∀ {τ : Type u_1} {K : Type u_2} [inst : Field K] {P : MvPolynomial (Option τ) K},
  P ≠ 0 →
    ∀ {n : ℕ},
      MvPolynomial.degreeOf none P ≤ n →
        ∃ (l : ℕ),
          1 ≤ l ∧
            l ≤ n + 1 ∧
              ∃ (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K),
                LinearIndependent K φ ∧
                  LinearIndependent K ψ ∧
                    (∀ (ν : Fin l), (φ ν).natDegree ≤ n) ∧
                      (∀ (ν : Fin l) (j : τ), MvPolynomial.degreeOf j (ψ ν) ≤ MvPolynomial.degreeOf (some j) P) ∧
                        P =
                          ∑ ν : Fin l, (Polynomial.aeval (MvPolynomial.X none)) (φ ν) * (MvPolynomial.rename some) (ψ ν)`
- What: Every nonzero polynomial in one distinguished and arbitrary remaining variables has a bounded separated decomposition with both factor families linearly independent.
- How: Choose a finite basis of coefficient-polynomial span; build independent univariate coordinate polynomials; reconstruct by basis expansion and preserve support-box degrees.
- Hypotheses: τ : Type* arbitrary, K : Type* with Field K, P ≠ 0, degreeOf none P ≤ n
- Project dependencies: Roth.coeffNone, Roth.eq_sum_X_none_pow_mul_coeffNone, Roth.exists_coeffNone_basis_aux, Roth.linearIndependent_coordinate_polynomials_aux, Roth.eq_sum_aeval_basis_coeffNone_aux
- Caller summary: explicit use count: 1; external to file use count: 0; explicit call sites: {'file': 'Roth/Separation.lean', 'line': 522, 'declaration': 'Roth.exists_rat_factors_det_hasseDeriv_aux', 'private': True}; documentation occurrences: 31; direct kernel value consumers: _private.Roth.Separation.0.Roth.exists_rat_factors_det_hasseDeriv_aux; inline derivations: None
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_separated_representation.md).

### Completed: `Roth.det_hasseDeriv_separated`

- Type: `∀ {τ : Type u_1} {K : Type u_2} [inst : Field K] {l : ℕ} (D : Fin l → τ →₀ ℕ)
  (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K),
  (Matrix.of fun (μ ν : Fin l) ↦
        (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν))
          (∑ ρ : Fin l, (Polynomial.aeval (X none)) (φ ρ) * (rename some) (ψ ρ))).det =
    (rename some) (genWronskian D ψ) * (Polynomial.aeval (X none)) (wronskian φ)`
- What: The mixed Hasse derivative determinant of a separated polynomial sum is the product of the embedded generalized and univariate Hasse Wronskians.
- How: Identify entries with an embedded A·Bᵀ using factorwise separated Hasse differentiation and linearity; apply determinant multiplicativity, transpose invariance and AlgHom determinant transport.
- Hypotheses: Arbitrary variable type τ; no Fintype or DecidableEq τ survives elaboration, Field K is required by existing named Wronskian parents, while expanded identity verifies over CommRing, Any l including0, arbitrary D and families φ/ψ; no independence, characteristic, nonzero or order-bound premise
- Project dependencies: MvPolynomial.hasseDeriv, Roth.hasseDeriv_rename_mul_aeval, Roth.genWronskian, Roth.wronskian, Roth.wronskianMatrix
- Caller summary: explicit use count: 1; external to file count: 0; textual occurrences: 3; explicit callers: Roth/Separation.lean:529 in private exists_rat_factors_det_hasseDeriv_aux; direct kernel value consumers: _private.Roth.Separation.0.Roth.exists_rat_factors_det_hasseDeriv_aux; full caller replays: exact original proof clone, expanded CommRing identity through named-parent bridge, strongest fresh-coordinate arbitraryorders identity through specialization bridge; inline rederivations: None; audit: Fresh exact ordered293 names,293unique,293present/kernelvalues; source occurrence count is distinct from direct kernel/simp/transitive closure.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.det_hasseDeriv_separated.md).

### Completed: `Roth.exists_sum_mul_eq_gcd`

- Type: `∀ {ι : Type u_2} (s : Finset ι) (u : ι → ℤ), ∃ (z : ι → ℤ), ∑ i ∈ s, z i * u i = s.gcd u`
- What: The gcd of finitely many integers is an integer linear combination of the family.
- How: Specialize Finset.gcd_eq_sum_mul to integers; reverse equality and commute factors.
- Hypotheses: arbitrary universe-polymorphic index type ι, s : Finset ι, u : ι → ℤ; no nonemptiness, nonzero or coprimality assumptions
- Project dependencies: None
- Caller summary: explicit use count: 1; external to file count: 0; internal count excluding declaring file: 0; callers: Roth/Separation.lean:446 Roth.exists_int_eq_of_gcd_eq_one; direct kernel value consumers: Roth.exists_int_eq_of_gcd_eq_one
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_sum_mul_eq_gcd.md).

### Completed: `Roth.exists_nat_smul_eq_map`

- Type: `∀ {σ : Type u_2} (G : MvPolynomial σ ℚ),
  ∃ (N : ℕ) (U : MvPolynomial σ ℤ), 0 < N ∧ (map (Int.castRingHom ℚ)) U = ↑N • G`
- What: Clears all rational coefficients of an arbitrary multivariate polynomial by a positive natural scalar.
- How: Product of positive coefficient denominators on finite support, integer scaled coefficients, reconstruction and coefficient extensionality.
- Hypotheses: Only σ : Type* and G : MvPolynomial σ ℚ; no finite/decidable/nonzero assumptions.
- Project dependencies: None
- Caller summary: explicit use count: 1; statement use count: 0; external to file use count: 0; callers: {'name': 'Roth.exists_primitive_smul_eq', 'file': 'Roth/Separation.lean', 'line': 410, 'role': 'Obtain a positive integral multiple before primitive gcd extraction.'}; direct kernel value consumers: Roth.exists_primitive_smul_eq; audit scope: All293 canonical values, exact names/order/private names; not transitive/simp closure.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_nat_smul_eq_map.md).

### Completed: `Roth.exists_primitive_smul_eq`

- Type: `∀ {σ : Type u_2} {G : MvPolynomial σ ℚ},
  G ≠ 0 →
    ∃ (g : ℚ) (U : MvPolynomial σ ℤ),
      g ≠ 0 ∧ (map (Int.castRingHom ℚ)) U = g • G ∧ (U.support.gcd fun (d : σ →₀ ℕ) ↦ U.coeff d) = 1`
- What: Every nonzero rational multivariate polynomial admits a nonzero rational scalar multiple which has integral coefficients with normalized coefficient gcd one.
- How: Clear denominators; Finset.extract_gcd; reconstruct divided coefficients as a polynomial; prove nonzero gcd, coefficient scaling and support equality.
- Hypotheses: Arbitrary universe-polymorphic variable type σ, no Fintype/Finite/DecidableEq instances., G : MvPolynomial σ ℚ, G ≠ 0 essential.
- Project dependencies: Roth.exists_nat_smul_eq_map (denominator clearing); this is a project helper, not an existing mathlib building block.
- Caller summary: explicit use count: 1; declaration occurrences: 1; callers: {'name': 'Roth.exists_int_factors', 'file': 'Roth/Separation.lean', 'line': 491, 'role': 'Uses all scalar/map/gcd1 conclusions to descend separated factors and preserve degrees.'}; direct kernel value consumers: Roth.exists_int_factors; inline rederivations: 0; scope: Complete canonical production inventory, git grep and rg --no-ignore; direct kernel values are distinct from transitive/simp dependencies.
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_primitive_smul_eq.md).

### Completed: `Roth.exists_int_eq_of_gcd_eq_one`

- Type: `∀ {ι : Type u_2} {s : Finset ι} {u : ι → ℤ},
  s.gcd u = 1 → ∀ {v : ℚ}, (∀ a ∈ s, ∃ (z : ℤ), ↑(u a) * v = ↑z) → ∃ (z : ℤ), v = ↑z`
- What: A finite gcd-one integer family detects integrality of a rational scalar from integrality of all selected products.
- How: Use finite Bezout coefficients, choose integer product witnesses, and take their integer weighted sum; the generic proof uses submodule closure under finite sums/scalars.
- Hypotheses: arbitrary index type ι, finite subset s, integer coefficient family u, s.gcd u = 1, each (u a : ℚ) * v has an integer witness for a∈s
- Project dependencies: Roth.exists_sum_mul_eq_gcd
- Caller summary: explicit use count: 1; callers: {'name': '_private.Roth.Separation.0.Roth.exists_int_polynomial_of_primitive_factor_aux', 'file': 'Roth/Separation.lean', 'line': 473}; direct kernel value consumers: _private.Roth.Separation.0.Roth.exists_int_polynomial_of_primitive_factor_aux; inline rederivations: 0; kernel scope: 293 canonical declaration values, direct consumers only
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_int_eq_of_gcd_eq_one.md).

### Completed: `Roth.rescale_separated_factor_aux`

- Type: `∀ {τ : Type u_1} {K : Type u_2} [inst : Field K]
  {U' U : MvPolynomial τ K} {V' : Polynomial K} {F : MvPolynomial (Option τ) K} {g : K},
  g ≠ 0 →
    U = g • U' →
      F = (rename some) U' * (Polynomial.aeval (X none)) V' →
        F = (rename some) U * (Polynomial.aeval (X none)) (Polynomial.C g⁻¹ * V')`
- What: A nonzero scalar can be transferred from the multivariate separated factor to the univariate factor by multiplying the latter by the reciprocal constant polynomial.
- How: Move scalar constants through renaming and evaluation and cancel the scalar with its inverse.
- Hypotheses: Field coefficients; nonzero scale; a given separated factorization. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: None
- Caller summary: 1 explicit source caller declarations, all in Separation.lean; 1 direct original value consumers. Exact separate lists retained. Entire Separation module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.rescale_separated_factor_aux.md).

### Completed: `Roth.exists_int_polynomial_of_primitive_factor_aux`

- Type: `∀ {τ : Type u_1} {U : MvPolynomial τ ℤ} {V' : Polynomial ℚ} {F : MvPolynomial (Option τ) ℤ},
  U.support.gcd ⇑U.coeff = 1 →
    (map (Int.castRingHom ℚ)) F = (rename some) ((map (Int.castRingHom ℚ)) U) * (Polynomial.aeval (X none)) V' →
      ∃ (V : Polynomial ℤ), Polynomial.map (Int.castRingHom ℚ) V = V'`
- What: When an integer multivariate polynomial is a separated product of an integer factor with coefficient gcd one and a rational univariate factor, the univariate factor has integer coefficients.
- How: Extract every product coefficient with coeff_rename_mul_aeval and use exists_int_eq_of_gcd_eq_one; Polynomial.mem_map_range assembles the integral factor.
- Hypotheses: Primitive integral ordinary-variable factor and integral separated product. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: Roth.coeff_rename_mul_aeval, Roth.exists_int_eq_of_gcd_eq_one
- Caller summary: 1 explicit source caller declarations, all in Separation.lean; 1 direct original value consumers. Exact separate lists retained. Entire Separation module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_int_polynomial_of_primitive_factor_aux.md).

### Completed: `Roth.exists_int_factors`

- Type: `∀ {τ : Type u_1} {U' : MvPolynomial τ ℚ} {V' : Polynomial ℚ},
  U' ≠ 0 →
    V' ≠ 0 →
      ∀ {F : MvPolynomial (Option τ) ℤ},
        (map (Int.castRingHom ℚ)) F = (rename some) U' * (Polynomial.aeval (X none)) V' →
          ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ),
            U ≠ 0 ∧
              V ≠ 0 ∧
                F = (rename some) U * (Polynomial.aeval (X none)) V ∧
                  (∀ (j : τ), degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree`
- What: Descend a nonzero separated rational factorization of an integer polynomial to integer factors, preserving all factor degrees.
- How: Roth.exists_primitive_smul_eq supplies a primitive scalar representative; Roth.rescale_separated_factor_aux transfers the inverse scalar to the right factor; Roth.exists_int_polynomial_of_primitive_factor_aux descends its coefficients. MvPolynomial.map_injective descends equality; degrees_map_of_injective/degreeOf_C_mul and Polynomial.natDegree_map_eq_of_injective/natDegree_C_mul transport all degrees.
- Hypotheses: Arbitrary variable type τ; no Fintype or DecidableEq., Nonzero U′ and V′., Exact mapped factorization of integral F.
- Project dependencies: Roth.exists_primitive_smul_eq, Roth.rescale_separated_factor_aux, Roth.exists_int_polynomial_of_primitive_factor_aux
- Caller summary: explicit use count: 1; external to file count: 0; callers: {'declaration': 'Roth.exists_det_eq_mul', 'file': 'Roth/Separation.lean', 'line': 552, 'role': 'Integral nonzero determinant factors; degree equalities discarded, bounds rederived.'}; direct kernel value consumers: Roth.exists_det_eq_mul; inline rederivations: None
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_int_factors.md).

### Completed: `Roth.exists_rat_factors_det_hasseDeriv_aux`

- Type: `∀ {τ : Type u_1} [Finite τ] {P : MvPolynomial (Option τ) ℤ},
  P ≠ 0 →
    ∀ {n : ℕ},
      degreeOf none P ≤ n →
        ∃ (l : ℕ),
          1 ≤ l ∧
            l ≤ n + 1 ∧
              ∃ (D : Fin l → τ →₀ ℕ),
                (∀ (μ : Fin l), Finsupp.degree (D μ) ≤ ↑μ) ∧
                  ∃ (U : MvPolynomial τ ℚ) (V : Polynomial ℚ),
                    U ≠ 0 ∧
                      V ≠ 0 ∧
                        (map (Int.castRingHom ℚ))
                            (Matrix.of fun (μ ν : Fin l) ↦
                                (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) P).det =
                          (rename some) U * (Polynomial.aeval (X none)) V`
- What: A nonzero integer polynomial has a nonzero separated rational factorization of a finite Hasse-derivative determinant, with the determinant size and derivative orders bounded by the distinguished-variable degree.
- How: Apply exists_separated_representation over the rationals, choose differential operators with exists_genWronskian_ne_zero, and use det_hasseDeriv_separated with ordinary Wronskian nonvanishing.
- Hypotheses: Finitely many ordinary variables; nonzero integer polynomial with distinguished degree bound. The exact captured parameters and existing ambient types are printed; no additional project-defined structure is captured.
- Project dependencies: MvPolynomial.hasseDeriv, MvPolynomial.hasseDeriv_map, Roth.det_hasseDeriv_separated, Roth.exists_genWronskian_ne_zero, Roth.exists_separated_representation, Roth.genWronskian, Roth.wronskian, Roth.wronskian_ne_zero_of_linearIndependent
- Caller summary: 1 explicit source caller declarations, all in Separation.lean; 1 direct original value consumers. Exact separate lists retained. Entire Separation module proof bodies replay successfully with fresh target name.
- Verdict: SKIP; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_rat_factors_det_hasseDeriv_aux.md).

### Completed: `Roth.exists_det_eq_mul`

- Type: `∀ {τ : Type u_1} [Finite τ] {P : MvPolynomial (Option τ) ℤ},
  P ≠ 0 →
    ∀ {r : Option τ → ℕ},
      (∀ (j : Option τ), degreeOf j P ≤ r j) →
        ∃ (l : ℕ),
          1 ≤ l ∧
            l ≤ r none + 1 ∧
              ∃ (D : Fin l → τ →₀ ℕ),
                (∀ (μ : Fin l), Finsupp.degree (D μ) ≤ ↑μ) ∧
                  ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ),
                    U ≠ 0 ∧
                      V ≠ 0 ∧
                        (∀ (j : τ), degreeOf j U ≤ l * r (some j)) ∧
                          V.natDegree ≤ l * r none ∧
                            (Matrix.of fun (μ ν : Fin l) ↦
                                  (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) P).det =
                              (rename some) U * (Polynomial.aeval (X none)) V`
- What: A nonzero integer polynomial admits an order-bounded mixed Hasse-derivative determinant that factors into nonzero integer polynomials in disjoint variable groups, with l and both individual degree bounds.
- How: exists_rat_factors_det_hasseDeriv_aux uses exists_separated_representation, exists_genWronskian_ne_zero, wronskian_ne_zero_of_linearIndependent and det_hasseDeriv_separated; exists_int_factors descends to integers; degreeOf_rename_mul_aeval, degreeOf_none_rename_mul_aeval and degreeOf_det_hasseDeriv_le prove the bounds.
- Hypotheses: τ : Type*; Finite τ in original; verified arbitrary ambient τ, P ≠ 0, r : Option τ → ℕ; ∀ j, degreeOf j P ≤ r j, original coefficients ℤ; verified CommRing/IsDomain/NormalizedGCDMonoid/CharZero R
- Project dependencies: Roth.exists_rat_factors_det_hasseDeriv_aux, Roth.exists_int_factors, Roth.degreeOf_rename_mul_aeval, Roth.degreeOf_none_rename_mul_aeval, Roth.degreeOf_det_hasseDeriv_le, MvPolynomial.hasseDeriv
- Caller summary: source calls: 1; files: 1; callers: {'name': 'Roth.index_le_lem6', 'file': 'Roth/Theta.lean', 'declaration_line': 556, 'call_line': 571, 'plan': 'Apply generic theorem at R=ℤ; full caller replay verified with every original bound and hypothesis.'}; kernel direct consumers: Roth.index_le_lem6; inline rederivations: None
- Verdict: YES-but-generalise-first; [complete report](.mathlib-quality/overview/mathlibable/Roth.exists_det_eq_mul.md).

### Completed: `Roth.RSet`

- Type: `{σ : Type u_1} → ℝ → (σ → ℕ) → Set (MvPolynomial σ ℤ)`
- What: Nonzero integer multivariate polynomials with individual degrees bounded by r and every real-cast coefficient absolute value bounded by B.
- How: Constructs a Set by conjoining nonzero, degreeOf bounds, and all coefficient absolute-value bounds. The degree component is equivalent to the carrier of MvPolynomial.restrictSupport ℤ {d | ∀ j, d j ≤ r j}; this needs degreeOf_le_iff plus quantifier reordering, not a definitional replacement of the whole set.
- Hypotheses: Arbitrary universe-polymorphic σ, B : ℝ, r : σ → ℕ; no Fintype, DecidableEq, positivity, or finite-support assumption is captured.
- Project dependencies: None
- Caller summary: explicit external occurrences: 6; external files: Roth/MainLemma.lean; within module code occurrences excluding definition: 9; direct value consumers: Roth.indexSet, Roth.indexSet_nonempty, Roth.indexSet_bddAbove, Roth.index_le_Θ, Roth.Θ_nonneg, Roth.Θ_le_card, Roth.Θ_le_of_forall_index_le, Roth.Θ_mono, _private.Roth.Theta.0.Roth.indexSet_comp_subset, Roth.Θ_unique_le, _private.Roth.Theta.0.Roth.index_separated_mul_le_aux, Roth.index_det_le, Roth.index_le_lem6, Roth.Θ_option_le, _private.Roth.MainLemma.0.Roth.exists_mem_RSet_le_index_aux, _private.Roth.MainLemma.0.Roth.exists_mem_RSet_le_index_of_log_bound_aux, _private.Roth.MainLemma.0.Roth.exists_auxiliary_polynomial_of_log_bound_aux, _private.Roth.MainLemma.0.Roth.exists_auxiliary_polynomial_with_index_gap_aux, Roth.main_lemma; direct type consumers: Roth.one_mem_RSet, Roth.index_le_Θ, Roth.Θ_le_of_forall_index_le, _private.Roth.Theta.0.Roth.index_separated_mul_le_aux, Roth.index_det_le, Roth.index_le_lem6, Roth.sub_mem_RSet, _private.Roth.MainLemma.0.Roth.exists_mem_RSet_le_index_aux, _private.Roth.MainLemma.0.Roth.exists_mem_RSet_le_index_of_rpow_bound_aux, _private.Roth.MainLemma.0.Roth.exists_mem_RSet_le_index_of_log_bound_aux, _private.Roth.MainLemma.0.Roth.exists_auxiliary_polynomial_of_log_bound_aux, _private.Roth.MainLemma.0.Roth.exists_auxiliary_polynomial_with_index_gap_aux; scope: 293 canonical source declarations only; not full transitive or simp closure
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.RSet.md).

### Completed: `Roth.indexSet`

- Type: `{σ : Type u_1} → [Fintype σ] → ℝ → (σ → ℕ) → (σ → ℕ) → Set ℝ`
- What: Set of all real polynomial indices from nonzero integer polynomials with each degree and every coefficient bounded, evaluated at coordinatewise coprime integer numerators over fixed natural denominators.
- How: Two independent bounded existential choices are exactly Set.image2 of the index-evaluation map over RSet and the coprime numerator set. Native bridge is rfl; the expanded index infDegree bridge requires finite-order normalization.
- Hypotheses: Arbitrary universe-polymorphic σ, Fintype σ, B : ℝ, q r : σ → ℕ. No captured DecidableEq, positivity, nonempty variable type, positive denominators or weights.
- Project dependencies: Roth.RSet, Roth.index
- Caller summary: explicit external occurrences: 0; external files: None; within module callers: 4; within module code occurrences excluding definition: 5; direct value consumers: Roth.Θ, Roth.indexSet_nonempty, Roth.indexSet_bddAbove, Roth.index_le_Θ, Roth.Θ_nonneg, Roth.Θ_le_card, Roth.Θ_le_of_forall_index_le, Roth.Θ_mono, _private.Roth.Theta.0.Roth.indexSet_comp_subset, Roth.Θ_equiv; direct type consumers: Roth.indexSet_nonempty, Roth.indexSet_bddAbove, _private.Roth.Theta.0.Roth.indexSet_comp_subset; scope: 293 canonical production declarations only; source references distinct from direct kernel consumers and transitive/simp closure
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.indexSet.md).

### Completed: `Roth.Θ`

- Type: `{σ : Type u_1} → [Fintype σ] → ℝ → (σ → ℕ) → (σ → ℕ) → ℝ`
- What: Real supremum of weighted indices over nonzero integer polynomials with individual degree/coefficient bounds and all coprime numerator vectors at fixed natural denominators.
- How: Exactly SupSet.sSup applied to indexSet; independently re-aimed to sSup of Set.image2 with full index map, and freshly normalized to infDegree/Finsupp.weight/aeval with untopD0.
- Hypotheses: Universe-polymorphic σ, Fintype σ, B : ℝ, q r : σ → ℕ. No captured DecidableEq, positivity or nonempty variable condition.
- Project dependencies: Roth.indexSet
- Caller summary: explicit external occurrences: 3; external files: Roth/MainLemma.lean; within module callers: 16; within module code occurrences excluding definition: 25; total explicit caller declarations: 19; direct value consumers: Roth.lem6Φ, _private.Roth.Theta.0.Roth.index_separated_mul_le_aux, Roth.index_le_lem6, _private.Roth.Theta.0.Roth.theta_scaled_unique_le_aux, _private.Roth.Theta.0.Roth.theta_prefix_lt_aux, _private.Roth.Theta.0.Roth.theta_lt_base_aux, _private.Roth.Theta.0.Roth.theta_phi_lt_aux, _private.Roth.Theta.0.Roth.theta_lt_succ_aux, _private.Roth.Theta.0.Roth.theta_lt_of_large_delta_aux, Roth.Θ_lt, _private.Roth.MainLemma.0.Roth.theta_lt_eta_of_sq_log_bound_aux, _private.Roth.MainLemma.0.Roth.exists_auxiliary_polynomial_with_index_gap_aux, Roth.main_lemma; direct type consumers: Roth.index_le_Θ, Roth.Θ_nonneg, Roth.Θ_le_card, Roth.Θ_le_of_forall_index_le, Roth.Θ_mono, Roth.Θ_equiv, Roth.Θ_unique_le, Roth.Θ_option_le, _private.Roth.Theta.0.Roth.theta_scaled_unique_le_aux, _private.Roth.Theta.0.Roth.theta_prefix_lt_aux, _private.Roth.Theta.0.Roth.theta_lt_base_aux, _private.Roth.Theta.0.Roth.theta_phi_lt_aux, _private.Roth.Theta.0.Roth.theta_lt_succ_aux, _private.Roth.Theta.0.Roth.theta_lt_of_large_delta_aux, Roth.Θ_lt, _private.Roth.MainLemma.0.Roth.theta_lt_eta_of_sq_log_bound_aux, _private.Roth.MainLemma.0.Roth.exists_auxiliary_polynomial_with_index_gap_aux; scope: 293 canonical production declarations only; lexical references are distinct from direct kernel types/values and transitive/simp closure.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ.md).

### Completed: `Roth.lem6M`

- Type: `ℕ → ℕ → ℝ → ℕ → ℝ`
- What: Auxiliary coefficient envelope M=(r₁+1)^(pl) l! B^l 2^(plr₁) for Roth Lemma6.
- How: One arithmetic expression using natural casts, powers, factorial and multiplication.
- Hypotheses: p,r₁,l natural; B arbitrary real; no positivity, finiteness or DecidableEq assumptions.
- Project dependencies: None
- Caller summary: Six explicit caller declarations, all Theta; seven direct kernel-value and six direct kernel-type consumers.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.lem6M.md).

### Completed: `Roth.lem6Φ`

- Type: `{τ : Type u_2} → [Fintype τ] → (Option τ → ℕ) → (Option τ → ℕ) → ℝ → ℕ → ℝ`
- What: Auxiliary Phi of Roth Lemma6: sum of extremal polynomial indices in distinguished and complementary variables with common coefficient bound and scaled degree vectors.
- How: Adds two real suprema; both complete arithmetic input sets and totalized real sSup conventions independently verified.
- Hypotheses: τ arbitrary finite type; q,r:Option τ→ℕ; M:ℝ;l:ℕ. No DecidableEq, positivity or nonempty hypotheses.
- Project dependencies: Roth.Θ
- Caller summary: Eleven semantic source lines in five declarations, all Theta; five direct kernel-value and four direct kernel-type consumers.
- Verdict: NO-composable-from-mathlib; [complete report](.mathlib-quality/overview/mathlibable/Roth.lem6Φ.md).

### Completed: `Roth.one_mem_RSet`

- Type: `∀ {σ : Type u_1} {B : ℝ}, 1 ≤ B → ∀ (r : σ → ℕ), 1 ∈ Roth.RSet B r`
- What: Constant integer polynomial1 belongs to the complete nonzero degree-bounded coefficient-bounded family if1≤B.
- How: Local classical simplification using MvPolynomial.coeff_one and MvPolynomial.degreeOf_one=0, nonzero1 and0≤1≤B. Independent full arithmetic, generic normed-ring and exact Int specialization proofs verified.
- Hypotheses: σ arbitrary universe-polymorphic type; B real; r:σ→ℕ;1≤B necessary and sufficient. No Fintype, DecidableEq, positive degree or nonempty variable hypotheses.
- Project dependencies: Roth.RSet
- Caller summary: One explicit caller Roth.indexSet_nonempty at Theta:81, one direct kernel-value consumer, zero direct kernel-type consumers.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.one_mem_RSet.md).

### Completed: `Roth.indexSet_nonempty`

- Type: `∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ},   1 ≤ B → ∀ (q r : σ → ℕ), (Roth.indexSet B q r).Nonempty`
- What: For B≥1 the bounded integer polynomial index family is nonempty.
- How: Use polynomial1, whose degrees vanish and coefficients are bounded, and numerators constantly1, coprime to arbitrary q.
- Hypotheses: σ arbitrary universe; Fintype required by unchanged index parent, B:ℝ;1≤B, q r:σ→ℕ arbitrary including zeros; no DecidableEq
- Project dependencies: Roth.indexSet, Roth.RSet, Roth.index, Roth.one_mem_RSet
- Caller summary: 2 explicit calls, both Theta:127/136;0 outside-file; canonical293 finds2 value/0 type consumers. Both complete caller replacements native clean.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.indexSet_nonempty.md).

### Completed: `Roth.indexSet_bddAbove`

- Type: `∀ {σ : Type u_1} [inst : Fintype σ] (B : ℝ) (q : σ → ℕ) {r : σ → ℕ},
  BddAbove (Roth.indexSet B q r)`
- What: The real index family of degree/coefficient-bounded nonzero integer polynomials at coprime rational numerator choices is bounded above by cardσ.
- How: Choose cardσ, unpack family witnesses, transfer nonzero and degrees through integer-real coefficient map, apply project index_le_card. Generic image2 packaging independently verified.
- Hypotheses: Arbitrary universe σ with Fintype; arbitrary real B; natural vectors q,r. No positivity, 1≤B, DecidableEq or nonempty-family premise.
- Project dependencies: Roth.indexSet, Roth.RSet, Roth.index, Roth.index_le_card
- Caller summary: explicit applications: 2; external to file: 0; callers: Roth.index_le_Θ, Roth.Θ_mono; canonical value consumers: 2; canonical type consumers: 0
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.indexSet_bddAbove.md).

### Completed: `Roth.index_le_Θ`

- Type: `∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ} {q r : σ → ℕ} {R : MvPolynomial σ ℤ},
  R ∈ Roth.RSet B r →
    ∀ {h : σ → ℤ},
      (∀ (j : σ), IsCoprime (h j) ↑(q j)) →
        Roth.index ((map (Int.castRingHom ℝ)) R) (fun (j : σ) ↦ ↑(h j) / ↑(q j)) r ≤ Roth.Θ B q r`
- What: Every admissible polynomial index at a coprime rational point is at most Θ.
- How: Apply le_csSup with project indexSet_bddAbove and the explicit polynomial/numerator membership witness.
- Hypotheses: Fintype σ; R∈RSet B r; each h j coprime to q j. No DecidableEq, positivity of q or r, or 1≤B.
- Project dependencies: Roth.RSet, Roth.indexSet, Roth.Θ, Roth.index, Roth.indexSet_bddAbove
- Caller summary: Three explicit call occurrences in two declarations: private index_separated_mul_le_aux twice; main_lemma once. Canonical kernel audit: two value consumers, zero type consumers.
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.index_le_Θ.md).

### Completed: `Roth.Θ_nonneg`

- Type: `∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ}, 0 ≤ Roth.Θ B q r`
- What: The polynomial-index supremum Θ is nonnegative for every coefficient bound, denominator and natural weight vector.
- How: Real.sSup_nonneg applied to pointwise nonnegative index values; independent verification expands real support infimum, finite sums and natural ratios.
- Hypotheses: σ : Type u, Fintype σ, B : ℝ arbitrary, q r : σ → ℕ arbitrary; no additional proof premises
- Project dependencies: Roth.Θ, Roth.indexSet, Roth.index, Roth.weight, Roth.index_nonneg
- Caller summary: declarations: Roth.index_le_lem6; source line: 583; call occurrences: 2; direct kernel value consumers: 1; direct type consumers: 0; external module consumers: 0
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ_nonneg.md).

### Completed: `Roth.Θ_le_card`

- Type: `∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ},
  Roth.Θ B q r ≤ ↑(Fintype.card σ)`
- What: The supremum of all admissible polynomial indices is bounded by the number of variables, for every real coefficient bound and all natural denominator/weight vectors.
- How: Apply Real.sSup_le with nonnegative cardinality; destruct each admissible index, transport nonzero and coordinate degrees through the injective integer-to-real coefficient map, then apply project index_le_card.
- Hypotheses: Fintype σ; arbitrary B:ℝ and q,r:σ→ℕ. No DecidableEq, nonempty σ, B≥1, q>0 or r>0 assumptions. Hidden degree bounds matter; nonzero can be dropped only for a separately enlarged family under real-default0 index convention.
- Project dependencies: Roth.Θ, Roth.indexSet, Roth.RSet, Roth.index_le_card
- Caller summary: One explicit application at Theta.lean:939 in private theta_lt_of_large_delta_aux (933–958); zero external-file calls. Canonical audit293 confirms one direct value consumer and no type consumer. Complete caller replay verified with replacement.
- Verdict: BORDERLINE-needs-human; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ_le_card.md).

### Completed: `Roth.Θ_le_of_forall_index_le`

- Type: `∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ},
  1 ≤ B →
    ∀ {q r : σ → ℕ} {c : ℝ},
      (∀ R ∈ Roth.RSet B r,
          ∀ (h : σ → ℤ),
            (∀ (j : σ), IsCoprime (h j) ↑(q j)) →
              Roth.index ((map (Int.castRingHom ℝ)) R) (fun (j : σ) ↦ ↑(h j) / ↑(q j)) r ≤ c) →
        Roth.Θ B q r ≤ c`
- What: A supplied common upper bound on all admissible polynomial indices bounds their supremum Θ.
- How: Apply csSup_le to the nonempty family from hB; destruct existential indexSet witnesses and apply hc.
- Hypotheses: Universe-polymorphic σ with Fintype; B real with 1≤B; arbitrary natural q,r; arbitrary real c; hc is the full pointwise upper bound. No DecidableEq, positive r, or positive q required.
- Project dependencies: Roth.Θ, Roth.indexSet, Roth.indexSet_nonempty, Roth.RSet, Roth.index
- Caller summary: explicit applications: 2; external to file: 0; callers: Roth.Θ_unique_le, Roth.Θ_option_le; canonical value consumers: 2; canonical type consumers: 0
- Verdict: NO-mathlib-has-it; [complete report](.mathlib-quality/overview/mathlibable/Roth.Θ_le_of_forall_index_le.md).

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

Completed `Roth.box`: Existing Finset.Iic + Finsupp.equivFunOnFinite.symm gives same object; raw mathlib-only native equality/cardinality/sum-product verified.

Completed `Roth.weight`: Exact general existing Finsupp.weight specialized to ℕ scalars and reciprocal real weights; native representation equality verified.

Completed `Roth.mem_box`: Finset.mem_map_equiv, Fintype.mem_piFinset, Finset.mem_range_succ_iff, Finset.mem_Iic, Finsupp.le_def

Completed `Roth.card_box`: Finset.card_map, Fintype.card_piFinset, Finset.card_range, Finsupp.card_Iic, Finsupp.prod_fintype, Nat.card_Iic

Completed `Roth.card_le_card_box`: Five actual search methods on current/standard/abstract forms. Existing generic function-family bound composes in three facts. Original Fin injection uses four domain facts including endpoint conversion; expanded original uses seven. Finsupp.card_Iic gives support product; normalization tested.

Completed `Roth.weight_nonneg`: verdict: NO-composable-from-mathlib; facts: Finset.sum_nonneg, div_nonneg, Nat.cast_nonneg; distinct facts: 3; expanded applications: 4; formal methods times forms: 5 x 3 actual; local-name index unavailable recorded

Completed `Roth.weight_zero`: Finset.sum_eq_zero + Nat.cast_zero + zero_div; bundled Finsupp.weight has generic map_zero.

Completed `Roth.weight_add`: Three existing arithmetic facts compose at current representation; generic map_add already supplies abstract Finsupp.weight additivity after a proved reciprocal-weight bridge.

Completed `Roth.weight_eq_zero_iff`: Finsupp.weight_eq_zero_iff_eq_zero needs canonical order, not applicable directly to ℝ. le_weight_of_ne_zero enables verified new ordered-monoid positive-weight helper.

Completed `Roth.weight_single`: Finsupp.weight_single already supplies arbitrary semiring/module basis evaluation; original finite division sum requires ratio bridge. Finsupp.sum_single_index plus sum_fintype are generic primitives.

Completed `Roth.weight_le_card`: Finset.sum_le_card_nsmul + div_le_one_of_le₀ + Nat.cast_le + Nat.cast_nonneg + nsmul_one. Generic field form uses three facts; original requires casts.

Completed `Roth.weight_mul_left`: Genuine generator-family law supplied by (Finsupp.bilinearCombination R S).map_smul; Finsupp.weight underlying linearCombination. Reciprocal bridge independently compiled.

Completed `Roth.weight_le_degree_div`: Actual Finder/Loogle/LeanSearch/rg/local searches on original, weighted-degree and abstract linearCombination forms. Existing Finsupp.weight/degree relations and sum/division order primitives inspected; no analogous bundled upper-bound hit established.

Completed `Roth.weight_mapDomain`: Finsupp.linearCombination_mapDomain at Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean:158 is exact generic analogue on Finsupp.weight; finite sum/division bridge is propositional.

Completed `Roth.wronskianMatrix`: verdict: BORDERLINE-needs-human; building blocks: Matrix.of, Polynomial.hasseDeriv; near matches: Polynomial.wronskian (binary polynomial output), Polynomial.taylor_coeff (evaluated entries), LinearMap.toMatrix (basis-coordinates, not arbitrary-family constructor); gap anchor: Mathlib/RingTheory/Polynomial/Wronskian.lean TODO: define Wronskian for n-tuple, not necessarily two.; formal methods: Finder, Loogle, LeanSearch, rg, local each on current/standard/abstract forms.; local index: unavailable; no absence inference.

Completed `Roth.wronskian`: Binary Polynomial.wronskian exact Fin2 bridge; arbitrary n-tuple TODO pinned. Raw det/of/hasseDeriv three-building-block construction compiled.

Completed `Roth.wronskian_eq_zero_of_not_linearIndependent`: AlternatingMap.map_linearDependent existing abstract law, Matrix.det_eq_zero_of_not_linearIndependent_cols, LinearIndependent.restrict_scalars', LinearIndependent.of_comp, LinearMap.pi

Completed `Roth.det_choose_eq`: generic law: Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde already exists; native checked one-call abstract form; building blocks: Nat.cast_choose_eq_descPochhammer_div, Matrix.det_mul_column, Matrix.det_transpose, Matrix.det_vandermonde, Polynomial.monic_descPochhammer, Polynomial.descPochhammer_natDegree; private near match: Vandermonde.lean:301 of_eval_descPochhammer_eq_mul_of_choose is private over ℤ; not an accessible replacement; all five methods all three forms: True

Completed `Roth.coeff_prod_of_natDegree_le'`: Public coeff_prod_of_natDegree_le uses one common bound; this variant uses n i. Native signature comparison and replay verified.

Completed `Roth.sum_range_le_sum_of_injective`: replacement: Finset.sum_range_le_sum; path: Mathlib/Algebra/Order/Group/Int/Sum.lean:72; same mathematical law: True; bridge: Nat.castEmbedding + image cardinality + sum_image + Fin.sum_univ_eq_sum_range + Nat.cast_sum + cast order reflection; not defeq and not claimed ≤3 calls.

Completed `Roth.coeff_wronskian_of_natDegree_injective`: Five actual methods on current/literature/abstract forms. Binary Wronskian and affine/triangular determinant coefficient candidates are partial matches. Native exact? and simp attempts fail with residual mathematical work.

Completed `Roth.wronskian_ne_zero_of_natDegree_injective`: Mathlib has binary Polynomial.wronskian, an explicit n-tuple TODO, and generic Matrix.det_vandermonde_ne_zero_iff. All five actual methods searched current/literature/abstract forms; no direct family replacement. Local index unavailable does not prove absence.

Completed `Roth.wronskian_update_sub_smul`: Generic column law exists at Matrix/Determinant/Basic.lean:478. Binary Polynomial.wronskian differs. Three actual direct simpa routes fail; explicit representation bridge verified.

Completed `Roth.linearIndependent_update_sub_smul`: More-general existing linearIndependent_add_smul_iff; generic update bridge and exact old-form polynomial bridge compiled.

Completed `Roth.sum_natDegree_update_lt`: Existing degree_sub_lt_left, cancelLeads natural-degree law, natDegree_lt_natDegree, Finset.sum_lt_sum and sum_update_of_mem. No verified ≤3-call entire original proof.

Completed `Roth.wronskian_ne_zero_of_linearIndependent`: Pinned binary Polynomial.wronskian and IsCoprime criterion do not cover arbitrary families. Generic determinant independence changes scalars and does not supply jet-column independence. Wronskian.lean has an explicit n-tuple TODO. All five actual search methods on four forms; isolated exact? failed without timeout.

Completed `Roth.wronskian_eq_zero_iff`: Five actual methods on current, standard and abstract forms. Exact binary IsCoprime.wronskian_eq_zero_iff is a coprime/derivatives-zero theorem, not the n-ary criterion. Pinned TODO explicitly requests n-tuples. Mathlib-only raw iff exact? fails without timeout.

Completed `MvPolynomial.taylor`: aeval/bind₁ yield the exact term; Polynomial.taylorAlgHom and taylorEquiv cover one variable only. Named multivariate shift not located; missing local index is not absence proof.

Completed `MvPolynomial.taylor_apply`: MvPolynomial.aeval supplies the defining substitution; own bridge is reflexive. Pinned Polynomial.taylor_apply is an analogous rfl law on Polynomial/LinearMap, not an exact multivariate hit; aeval_def expands a different layer.

Completed `MvPolynomial.taylor_X`: Existing more general MvPolynomial.aeval_X at Mathlib/Algebra/MvPolynomial/Eval.lean:587; arbitrary commutative R-algebra assignment. eval₂_X is a broader coefficient-map generator rule. Polynomial.taylor_X is only a pinned univariate analogy.

Completed `MvPolynomial.taylor_C`: existing: MvPolynomial.algHom_C; file: Mathlib/Algebra/MvPolynomial/Basic.lean:441; broader: Arbitrary R-algebra homomorphism to any Semiring A with Algebra R A, including noncommutative A; scalar image algebraMap R A a; secondary: MvPolynomial.aeval_C, Polynomial.taylor_C; native: Target exact specialization, isolated arbitrary-AlgHom/raw translation, full copied named caller and target-disabled simp consumers all clean complete

Completed `MvPolynomial.taylor_monomial`: NO-mathlib-has-it: aeval_monomial at Mathlib/Algebra/MvPolynomial/Eval.lean:681; one-call exact target and independent mathlib-only arbitrary-algebra proof checked. Five actual methods × three forms.

Completed `MvPolynomial.coeff_aeval_X_mul`: Private coefficient-convolution reduction using polynomial evaluation sum and coeff_monomial_mul′; no public contribution verdict inferred.

Completed `MvPolynomial.hasseCoeff_single_add_eq`: Extracts one factor with Finsupp.mul_prod_erase′, then finite-product congruence; direct project definition hasseCoeff retained. No public mathlibable absence/inclusion claim.

Completed `MvPolynomial.prod_pow_single_add_tsub`: Existing finite-product splitting, powers and coordinate erasure express exact proof; no public contribution verdict under private rule.

Completed `MvPolynomial.coeff_taylor_monomial_single_add_aux`: Uses Polynomial.coeff_X_add_C_pow and existing monomial/evaluation/multiplication laws plus three separately reviewed private project helpers; not a library-only composition claim.

Completed `MvPolynomial.coeff_taylor_monomial_aux`: Finsupp.induction supplies exponent recursion; generic algHom_C handles constants. Direct expression audit maps private replay to canonical61 and confirms no later coeff_taylor use.

Completed `MvPolynomial.coeff_taylor`: existing analogue: Polynomial.taylor_coeff; exact multivariate hit: False; five methods three forms: formal-search.json; composition: No ≤3-call proof demonstrated; tested expanded simp and default exact? leave genuine coefficient normalization.

Completed `MvPolynomial.eval_taylor`: eval_assoc, comp_aeval_apply, eval_eval₂, map_add, eval_X, eval_C

Completed `MvPolynomial.taylor_taylor`: comp_aeval_apply, comp_aeval, map_add, aeval_X, algHom_C, add_assoc, C_add

Completed `MvPolynomial.taylor_zero`: Existing map_zero(C), add_zero, aeval_X_left_apply compose exact old form; structural congrArg×2/funext/Eq.trans×2 explicit. aeval_X_left is bundled canonical identity. Univariate Polynomial.taylor_zero is only analogue.

Completed `MvPolynomial.taylor_map`: map_eval₂ is exact generic substitution law; map_aeval/eval₂_map and Monad.map_bind₁ are related. Original translated-generator normalization is propositional, not a direct exact call. Polynomial.map_taylor is univariate analogue over Semiring.

Completed `MvPolynomial.taylor_rename`: aeval_rename and comp_aeval_apply are exact abstract compatibility laws. Original normalized translation square requires five mathematical facts; not a one-call defeq replacement.

Completed `MvPolynomial.degreeOf_taylor_le`: Existing degreeOf_le_iff and degree bounds on sums/products do not prove the essential translated coefficient vanishing. Polynomial.natDegree_taylor is univariate; aeval_natDegree_le uses total degree and a univariate target.

Completed `MvPolynomial.taylor_neg_taylor`: Univariate Polynomial.taylorEquiv and algEquivAevalXAddC are close analogues, not multivariate replacements. Generic inverse-application law needs an already verified multivariate equivalence.

Completed `MvPolynomial.taylor_injective`: Function.LeftInverse.injective exists but requires the project-specific inverse premise. Polynomial.taylor_injective works over Ring, univariate only. New translation AlgEquiv would supply injectivity generically, after proving its inverse fields.

Completed `MvPolynomial.taylor_eq_zero_iff`: Polynomial.taylor_eq_zero and comp_X_add_C_eq_zero_iff are Semiring/univariate at pinned revision; generic zero-preserving injection iff exists but requires an injectivity premise. New multivariate semiring maximal-support proof is not an existing-call composition.

Completed `MvPolynomial.eq_sum_box_hasseDeriv`: Polynomial.sum_taylor_eq is univariate CommRing analogue. eval₂_eq supplies arbitrary-variable finite-support reconstruction, but not Hasse coefficient identification or off-box vanishing. Isolated successful support expansion verifies the boundary.

Completed `MvPolynomial.eval_eq_sum_box`: eval₂_eq/aeval_sum/aeval_prod and Polynomial.sum_taylor_eq are generic evaluation/univariate inputs, not multivariate Hasse identity. Isolated support-evaluation via explicit RingHom succeeds but lacks Hasse coefficients and box cutoff.

Completed `Roth.normOne`: Finsupp.sum gives exact scalar construction by rfl. Finsupp WithLp1 dist-to-zero equals it, verified with zipWith/mapRange normalization. Current pinned file has metric structures, not a full normed-group/ring structure. Polynomial.supNorm is univariate maximum, not this sum.

Completed `Roth.diag`: MvPolynomial.aeval (Eval569) gives exact construction; comp_aeval_apply and Polynomial.aeval_X give arbitrary algebra-target evaluation. Existing rename and uniqueAlgEquiv supply alternate bundle. pUnitAlgEquiv deprecated in pinned source, avoided in probes.

Completed `Roth.normOne_nonneg`: Finset.sum_nonneg and abs_nonneg close exact expanded statement; Finsupp.sum_nonneg supplies generalized arbitrary-index ordered-codomain aggregation. No exact generic norm_nonneg application without correct norm structure bridge.

Completed `Roth.normOne_eq_sum_of_support_subset`: Existing same padding theorem Finsupp.sum_of_support_subset at arbitrary index/Zero coefficient/AddCommMonoid codomain; MvPolynomial sum definition provides representation. Finset.sum_subset and coefficient-vanishing give original proof. All5 methods/3forms checked.

Completed `Roth.normOne_monomial`: MvPolynomial.sum_monomial_eq exists in pinned Basic275–278; Finsupp.sum_single_index gives arbitrary Zero coefficient/AddCommMonoid codomain version. All5 methods/3forms actually searched and pinned law signatures compiled.

Completed `Roth.normOne_zero`: Pinned Finsupp.sum_zero_index generated at Algebra/BigOperators/Finsupp/Basic86–88; arbitrary indexed size, Zero coefficients and AddCommMonoid output, no zero-preservation premise. Direct old-interface term and all generic probes freshly compiled. All5 methods/3forms run; Loogle retries retained.

Completed `Roth.abs_coeff_le_normOne`: NO-mathlib-has-it: Finsupp.single_eval_le_sum, Mathlib/Data/Finsupp/Order.lean:165–170; independently pinned type and exact specialization verified. Four external/local formal methods × three forms plus rg on each; current Loogle syntax/rate failures retained and corrected query succeeded.

Completed `Roth.normOne_add_le`: Finsupp.sum_of_support_subset, Finset.sum_add_distrib, Finset.sum_le_sum and abs_add_le give a real common-support proof. sum_add_index requires equality; norm_add_le needs correct bundled structure. WithLp1 Finsupp has metric structure, and two freshly proved bridges recover triangle. No checked≤3-existing-call replacement.

Completed `Roth.normOne_neg`: Finsupp.sum_neg_index generated from prod_neg_index Basic265–268, Int.cast_neg and abs_neg give direct checked composition; Int.cast_zero/abs_zero discharge zero-preservation parameter. Generic norm_neg requires matching norm structure and is not treated as direct project norm law.

Completed `Roth.normOne_sum_le`: Existing Finset.le_sum_of_subadditive supplies finite induction; norm_sum_le needs a seminormed additive group compatible with this coefficient size. Project triangle is not an existing mathlib building block.

Completed `Roth.normOne_mul_le`: Existing convolution expansion, finite sums and scalar size identities; norm_mul_le needs an L1-compatible seminormed multiplication structure absent from tested environment.

Completed `Roth.normOne_prod_le`: Finset.le_prod_of_submultiplicative_of_nonneg already supplies all finite induction. Finset.norm_prod_le requires compatible NormedCommRing and NormOneClass; no raw instance in tested environment.

Completed `Roth.normOne_le_card_mul`: Finset.sum_le_card_nsmul at Algebra/Order/BigOperators/Group/Finset.lean:285 generated from prod_le_pow_card. Current native signature uses Preorder.

Completed `Roth.normOne_det_le`: Matrix.det_le requires multiplicative AbsoluteValue; existing RingSeminorm supports submultiplicativity but searched determinant law missing.

Completed `Roth.abs_coeff_hasseDeriv_le`: Polynomial.hasseDeriv_coeff and norm_nsmul_le cover separate ingredients; no searched multivariate Hasse coefficient-size bound. Isolated raw binomial bound and actual generic operator bound compiled.

Completed `Roth.normOne_hasseDeriv_le`: Five actual methods across current/standard/abstract forms. Existing finite sum/natural binomial facts are building blocks; actual multivariate Hasse operator absent in guarded mathlib-only native environment.

Completed `Roth.diag_eq_sum`: eval₂_eq plus aeval_def, prod_pow_eq_pow_sum, degree_apply, algebraMap_eq, C_mul_X_pow_eq_monomial compile generically. No exact diagonal theorem established; local index unavailable.

Completed `Roth.abs_coeff_diag_le`: Finset.abs_sum_le_sum_abs, Finset.le_sum_of_subadditive, Finset.sum_le_card_nsmul plus polynomial coefficient/evaluation normalization are existing blocks, not an established direct diagonal estimate. New assessment helpers are not mathlib replacements.

Completed `Roth.natDegree_diag_le`: aeval_natDegree_le in RingTheory/Polynomial/Basic:898 is broader substitution theorem; totalDegree_le_degrees_card, sum_count_eq_card, sum_le_sum and degreeOf_def derive its premise. No old-form <=3-call term established.

Completed `Roth.eval_diag`: NO-mathlib-has-it: MvPolynomial.comp_aeval_apply, Mathlib/Algebra/MvPolynomial/Eval.lean:612; hom_eval₂:198, map/eval/aeval transport.

Completed `Roth.diag_sub`: Existing map_sub (generated additive theorem of map_div) already proves this with weaker generic homomorphism assumptions.

Completed `Roth.geom_sum_le_one_add_pow`: Five actual methods on three forms; positive Commute.add_pow, Nat.choose_pos, Nat.mono_cast, sum and order primitives; related Bernoulli/geometric results differ.

Completed `Roth.sum_box_prod_pow_le_aux`: Finset.prod_univ_sum factors the rectangular sum; ordered finite product and nonnegative scalar monotonicity combine the separately assessed geometric bound. Full public contribution search n/a under private prefilter.

Completed `Roth.abs_eval_le`: Prefer eval₂ and existing size-hom classes. AbsoluteValue.eval_mvPolynomial_le is a homogeneous/coefficient-l1/sup bound, not the rectangular common-coefficient bound. GaussNorm estimates concern weighted coefficient suprema, not arbitrary real evaluation.

Completed `Roth.degreeOf_det_hasseDeriv_le`: Existing degreeOf_sum_le, degreeOf_C_mul_le, degreeOf_prod_le and det_apply' supply proof steps, not ≤3-call replacement. Closest natDegree_det_X_add_C_le is affine univariate matrix only.

Completed `Roth.abs_coeff_det_hasseDeriv_le`: Matrix.det_le requires multiplicative AbsoluteValue; coefficient length is submultiplicative RingSeminorm. Polynomial.hasseDeriv_coeff is univariate. Finsupp and Finset size inequalities supply steps, not a≤3-call replacement.

Completed `Roth.genWronskian`: Matrix.det and detRowAlternating are outer building blocks; Polynomial.wronskian is pairwise univariate; Polynomial.hasseDeriv univariate. All5 search methods/current,standard,abstract forms run; external/local-index completeness caveats retained.

Completed `Roth.kronecker`: Exact positive existing MvPolynomial.aeval; aeval_monomial and eval₂Hom native checked; unrelated Matrix.kronecker, expand, bind₁ and finSuccEquiv not mistaken for target.

Completed `Roth.kroneckerExp`: Exact positive Finsupp.weight in Mathlib/Data/Finsupp/Weight.lean, weight_eq_sum bridge; underlying Finsupp.linearCombination read and native checked. Five actual search methods on current/standard/abstract; abstract dotted Loogle failure retried successfully, local index unavailable honestly recorded.

Completed `Roth.kronHasse`: A pointwise composition: take one project multivariate Hasse derivative, then project Kronecker substitution. It provides generators for the polynomial-module span. Existing function composition is sufficient for the interface; this prefilter does not assign a separate public contribution verdict. The named private operator and the span have distinct roles.

Completed `Roth.kronSpan`: Existing Submodule.span takes the image of the private substituted Hasse operators whose total order is at most the bound. It organizes the derivative-stability induction and finite span witness. The span and its individual operator generators have distinct roles; no duplicate definition or new instance is introduced.

Completed `Roth.genWronskian_eq_zero_of_not_linearIndependent`: det_eq_zero_of_not_linearIndependent_cols + restrict_scalars' + of_comp + LinearMap.pi gives a checked four-call bridge; prebundled map needs three.

Completed `Roth.kronecker_monomial`: All five actual methods on current/standard/abstract forms; pinned aeval_monomial Eval.lean681 is the analogous law for re-aimed parent aeval. Independent map_eq/exp_eq bridges and original-form proof pass.

Completed `Roth.kroneckerExp_injOn`: All5 actual methods on current, standard and weight forms. Nat.injOn_ofDigits is existing list theorem, not the analogous weight theorem. Fresh weighted exact? fails without timeout; searches do not prove absence.

Completed `Roth.coeff_kronecker`: Finsupp.mapDomain_apply' supplies exact abstract coefficient transport; new nondefinitional aeval/mapDomain normalization bridge verified in arbitrary CommSemiring.

Completed `Roth.kronecker_eq_zero_iff`: exact abstract: Finsupp.mapDomain_injOn; alternative: Finsupp.mapDomain_support_of_injOn; normalization: Newly proved weighted aeval/mapDomain bridge; not existing replacement; automatic parent gate: aeval analogous law not established; no blanket NO

Completed `Roth.linearIndependent_kronecker`: existing: LinearIndependent.map_injOn, LinearMap.linearIndependent_iff_of_injOn, AddMonoidAlgebra.supported, AddMonoidAlgebra.mem_supported, Submodule.span_le, Finsupp.mapDomain_injOn; limit: Exact final transport exists, but specialized span-injectivity premise still requires new108–110 proofs. map′ global injectivity is false in two variables.

Completed `Roth.derivative_aeval`: Univariate Derivation.map_aeval and comp_aeval_eq are near misses. MvPolynomial.derivation_ext/mkDerivationEquiv classify derivations but do not state evaluated partial-sum law. Kaehler coordinate theorem requires further pullback/reconstruction.

Completed `Roth.derivative_kronHasse_aux`: This function-valued derivative identity follows pointwise from the project chain rule and the partial/Hasse commutation identity. It supplies the next-order generators in the bounded-span induction. Existing function extensionality and pointwise sums/scalars express the interface; there is no new definition, instance or coercion. It is a live internal recurrence, not a duplicate of the scalar chain rule. The public contribution verdicts of its ingredients remain separate.

Completed `Roth.derivative_mem_kronSpan`: Submodule.span_induction is the existing organizing API. The generator case uses the preceding private derivative recurrence and the bound on total Hasse order; the scalar case uses the polynomial Leibniz rule and inclusion of the old bounded span in the next one. This lifts a generator identity to closure of the whole polynomial-coefficient span. It is distinct from both the generator recurrence and the subsequent Hasse-iteration result. No new definition, class or instance is needed.

Completed `Roth.hasseDeriv_kronecker_mem`: Induction on the univariate Hasse order uses the order-zero span generator and the preceding derivative-span closure. Polynomial.hasseDeriv_comp relates the next Hasse derivative to differentiation, and characteristic zero makes the natural successor scalar invertible in the field. This is a live bridge from ordinary derivative closure to Hasse derivative span membership, not a duplicate of either preceding lemma. Existing span and scalar-restriction APIs supply the interface; no new class or instance is installed.

Completed `Roth.exists_hasseDeriv_kronecker_eq_sum`: Polynomial.hasseDeriv_comp is operator composition, not substitution; Finsupp span/extraction API supplies coefficients only after substantive membership. Analytic Faà di Bruno and univariate Taylor API are partial matches.

Completed `Roth.det_sum_rows`: MultilinearMap.map_sum_finset and map_smul_univ provide abstract mathematical content; detRowAlternating supplies determinant witness; explicit normalization bridge checked. One-shot weighted determinant simpa fails, abstract weighted simpa succeeds.

Completed `Roth.wronskian_kronecker_eq_sum_aux`: The supplied uniform derivative-row expansions substitute into the Wronskian matrix. The existing project det_sum_rows helper expands its determinant by row multilinearity, while AlgHom.map_det transports each chosen generalized Wronskian through Kronecker substitution. This is a live application bridge, distinct from the standalone determinant identity and the final nonvanishing theorem. It adds no structure or instance; its private status is appropriate to the project-specific transport.

Completed `Roth.exists_genWronskian_ne_zero`: Pinned pairwise Polynomial.Wronskian TODO explicitly requests n-tuples. Generic matrix determinant nonvanishing and Jacobian criteria do not select bounded derivative rows from coefficient-field independence. All five search methods executed on three forms.

Completed `Roth.sqrt_one_sub_inv_lt`: Real.sqrt_one_add_le supplies the standard tangent estimate; Real.sqrt_lt' and reciprocal comparison supply proof blocks. No ≤3-call exact threshold derivation verified.

Completed `Roth.inv_add_inv_le`: The two reciprocal denominators are positive under the real interval bounds. Existing inv_add_inv and div_le_div_iff reduce the estimate to the nonnegative product x*(2-x). This paired endpoint bound feeds the reflected finite-sum argument, and is distinct from the square-root threshold and the full reciprocal-sum estimate. No new structure or instance is needed.

Completed `Roth.sum_inv_le`: The preceding private complementary-pair bound is summed over the finite grid. Finset.sum_range_reflect identifies the reflected grid sum with the original one, and ordinary finite-sum distribution and arithmetic divide the resulting estimate by two. This upgrades the pointwise pair estimate to the whole reciprocal grid sum, without duplicating the public strict square-root bound.

Completed `Roth.sum_inv_lt`: All five methods on current, convex-endpoint literature and abstract symmetric-pair forms; local index unavailable. Pinned convexOn_zpow, chord and reflection APIs provide partial blocks; no existing ≤3-call replacement established. Three exact? failures not treated as absence proof.

Completed `Roth.extend_apply_castSucc`: Embedding a finitely supported vector along the injective Fin.castSucc map preserves each old coordinate. The added singleton at Fin.last has zero contribution at every castSucc coordinate. Finsupp.mapDomain_apply_of_injective and simplification prove the formula. This complements the last-coordinate helper and supports the filtered-box fiber bijection; it registers no instance or coercion.

Completed `Roth.extend_apply_last`: The image of Fin.castSucc excludes Fin.last, so the embedded finitely supported vector evaluates to zero there. The singleton contributes exactly its stored natural value. Finsupp.mapDomain_of_notMem_range and simplification prove the formula. This complements the castSucc-coordinate helper and supplies the last-coordinate requirement in the filtered-box fiber bijection.

Completed `Roth.card_filter_box_fiber_aux`: Finset.card_bij compares the smaller filtered box with the fixed last-coordinate fiber. Extension preserves all old coordinates and sets the last to i; the bound hi ensures membership. Injectivity follows by restriction to castSucc coordinates. Surjectivity reconstructs the smaller vector with Finsupp.equivFunOnFinite and proves its extension equals the original by Fin.lastCases. This is the geometric fiber-identification step; the public cardinality theorem separately sums the fibers.

Completed `Roth.card_filter_box_last`: Generic fibre theorem exact; filtered-product law closes by card_filter/sum_product simp. Existing snoc cardinality restricts predicate to init, so not exact arbitrary-p duplicate. All5methods on3forms retained.

Completed `Roth.filter_weight_le_eq_empty`: The threshold (m-lambda)/2 is strictly negative when lambda exceeds the dimension. Every natural exponent vector has nonnegative weight, even if some coordinate bounds vanish. Finset.filter_eq_empty_iff and weight_nonneg reduce each hypothetical member to an arithmetic contradiction. This handles the empty tail regime in the main lattice estimate; it is distinct from its small-lambda cardinality bound and inductive step.

Completed `Roth.card_filter_fiber_eq`: Weight additivity, injective mapDomain transport and singleton evaluation split the extended vector weight into the smaller-vector contribution plus i/r_last. An affine rearrangement moves that last-coordinate contribution into the shifted lambda parameter. Finset.filter_congr identifies the predicates before cardinalities are cast to real numbers. No denominator positivity is required for this rearrangement; all box bounds and last coordinates may be zero.

Completed `Roth.card_filter_weight_le_of_le_sqrt_aux`: A filtered box has cardinality at most the whole box by Finset.card_filter_le. card_box supplies the product of side cardinalities. Positive lambda and lambda at most twice the square root of the dimension make the requested prefactor at least one, so multiplying the nonnegative box cardinality gives the bound. This is the direct small-lambda regime, separate from the negative-threshold empty case and the large-lambda induction.

Completed `Roth.card_filter_weight_le_succ_aux`: Count by the last-coordinate fibers, rewrite each weighted predicate with the shifted lambda, and apply the full smaller-box induction hypothesis at each positive shifted parameter. Factor out the smaller-side product and use the harmonic reciprocal-grid estimate sum_inv_lt with positive last side and dimension at least two. Splitting the full product along Fin.castSucc and Fin.last cancels the square-root and side factors. This is the large-lambda inductive case, distinct from the direct small-lambda bound and empty-tail case.

Completed `Roth.card_filter_weight_le`: Five actual methods on current/literature/probability forms; generic cardinality and Chebyshev/variance/uniform APIs are partial matches. Pinned positive signatures and named Chebyshev application checked, no complete original specialization claimed. Bounded exact? nonclosure is not absence proof.

Completed `Roth.index`: existing: AddMonoidAlgebra.infDegree; other positive: MvPowerSeries.weightedOrder; weight: Finsupp.weight; translation: MvPolynomial.aeval; representation bridge: Finite infimum with WithTop and default zero; not definitional equality.; methods: Finder, Loogle, LeanSearch, rg, lean_local_search

Completed `Roth.mem_support_taylor_iff`: A multi-index lies in the Taylor support exactly when its Taylor coefficient is nonzero. mem_support_iff gives the coefficient criterion, and coeff_taylor identifies that coefficient with evaluation of the Hasse derivative. The private bridge is the common support-to-derivative interface for the index bound, attainment, lower-bound characterization and degree estimate. It is distinct from the quantitative inequalities it supports and requires no finite variable-type instance.

Completed `Roth.index_le_weight`: verdict: NO-mathlib-has-it; reaim parent: AddMonoidAlgebra.infDegree; analogous law: Finset.inf_le; projection: WithTop.untopD_le; premise: Finsupp.mem_support_iff; verified native: True

Completed `Roth.exists_weight_eq_index`: verdict: NO-mathlib-has-it; reaim parent: AddMonoidAlgebra.infDegree; analogous law: Finset.exists_mem_eq_inf; premise: nonempty coefficient support; verified native: True

Completed `Roth.le_index_iff`: Finset.le_inf_iff, generated dual at Data/Finset/Lattice/Fold.lean:99, is the exact analogous law for infDegree; Finset.le_inf'_iff at557, coe_inf', untopD_coe and coeff_taylor bridge the old spelling.

Completed `Roth.index_nonneg`: Finite-inf lower-bound introduction Finset.le_inf_iff.mpr already supplies the analogous nonnegativity law on infDegree under support-local nonnegative degrees; Real.sInf_nonneg is exact order-theoretic engine of old proof. Finset.le_inf′_iff, coe_inf′ and WithTop.untopD_coe/top preserve zero-default projection.

Completed `Roth.index_eq_zero_iff`: existing: Finset.inf_eq_bot_iff on AddMonoidAlgebra.infDegree; native: isolated abstract/general real laws; actual parent bridge; nonnegative NNReal recoding; bounded actual replacement; full Index consumer replay; old form call count: more than3 including normalization and project API; not claimed mathlib-only one-call; abstract call count: one finite-inf criterion plus exists_eq_right and Finsupp.mem_support_iff normalization

Completed `Roth.index_sub_weight_le_index_hasseDeriv`: infDegree, weightedOrder and finite infimum APIs exist, but no existing derivative-shift law identified. Univariate natDegree_hasseDeriv_le bounds maximum degree, not vanishing minimum. Twelve actual formal-method requests and pinned rg searches.

Completed `Roth.le_index_sum`: supDegree_sum_le with B:=OrderDual T is definitionally the finite-infDegree sum law (one existing call); Finset.le_inf_iff and trans give a common lower bound. Five actual methods on current, literature and abstract forms; positive candidates verified at pin.

Completed `Roth.weight_eq_finsuppWeight_div`: Finsupp.apply_linearCombination R f w d is existing generic naturality; independently checked cast/scaling specializations and actual denominator bridge.

Completed `Roth.index_eq_weightedOrder_div`: Existing infDegree and weightedOrder are canonical support-minimum constructions; no analogous coe comparison found across five methods×three forms. Native exact?/definition-simp closure probes fail, independent new proof succeeds.

Completed `Roth.index_mul`: Existing MvPowerSeries.weightedOrder_mul verified in isolation at Semiring/NoZeroDivisors generality, arbitrary σ and natural weights. AddMonoidAlgebra.le_infDegree_mul is only an inequality; supDegree_mul additionally requires injective degree. Real-weight component/decomposition infrastructure exists but no analogous general real-weight equality was established.

Completed `Roth.index_prod`: Existing MvPowerSeries.weightedOrder_prod independently verified over arbitrary σ, CommSemiring R, NoZeroDivisors R and Nontrivial R, natural weights, including zero factors. Coercion of polynomial products via coeToMvPowerSeries.ringHom and map_prod verified. Generic infDegree product equality for arbitrary real noninjective weights was not established. Fresh145 isolated IsWeightedHomogeneous.prod signature confirms AddCommMonoid weight target M and CommSemiring coefficients; this closure theorem is not an extremal component identity.

Completed `Roth.index_neg`: Existing AddMonoidAlgebra.supDegree_neg on OrderDual gives exact infDegree negation law. Independent isolated Ring/semilatticeinf/top and projected proof compiled.

Completed `Roth.index_C_mul`: Reaimed infDegree scalar law is core congrArg applied to existing Finsupp.support_smul_eq; independently compiled explicit existing-call term and canonical133 bridge transport.

Completed `Roth.index_mul_left_weights`: map_finset_inf (Data/Finset/Lattice/Fold.lean:93 generated dual) on generic infDegree; Real.sInf_smul_of_nonneg (Basic/Real/Pointwise.lean:41); complete five methods on three forms.

Completed `Roth.index_rename`: NO-composable-from-mathlib on canonical parent infDegree: exact two-call composition support_rename_of_injective + Finset.inf_image; weight normalization via linearCombination_mapDomain and centers via aeval composition. Bridge is not definitional.

Completed `Roth.index_le_card`: All five actual search methods on current/literature/abstract forms. Finset.inf_le exactly supplies canonical witness upper bound; csInf_le, finite-image boundedness, monomial_le_degreeOf, sum_le_sum and div_le_one_of_le₀ are building blocks. Full Taylor-degree/cardinality bound not located.

Completed `Roth.index_unique`: verdict: NO-mathlib-has-it; reaim: Polynomial.rootMultiplicity_eq_natTrailingDegree; path: Mathlib/Algebra/Polynomial/RingDivision.lean:133; methods: Finder, Loogle, LeanSearch, rg, local; old form existing call count: Not <=3; genuine representation normalization required; normalized form existing call count: 1; bridge: Independently checked minimumSupport/taylorMinimum/trailingInf/rootInf/realInfSupport/realRootInf; these are new bridge proofs, not existing declarations.

Completed `Roth.coeffNone`: verdict: NO-composable-from-mathlib; building blocks: MvPolynomial.optionEquivLeft, Polynomial.coeff; modern: Polynomial.lcoeff, Finsupp.comapDomain; calls: 2; formal methods: Finder, Loogle, LeanSearch, rg, local; current, literature, modern and supplementary pullback forms

Completed `Roth.eq_mapDomain_some_add_single`: canonical: Finsupp.optionElim_some; building blocks: Finsupp.optionElim_some, Finsupp.update_eq_add_single, Finsupp.embDomain_some_none; representation: Finsupp.embDomain_eq_mapDomain; old form existing calls: 4; embedding form existing calls: 3

Completed `Roth.coeff_X_none_pow_mul_rename`: The product of a pure power of the distinguished variable and a polynomial in the remaining variables has coefficients selected by the distinguished exponent. The proof moves through optionEquivLeft, computes the univariate monomial coefficient, and returns to the original exponent coordinates. This is a private computational interface for the subsequent coefficient-family expansion; it is distinct from the full expansion and determinant theorems.

Completed `Roth.coeff_coeffNone`: canonical: MvPolynomial.optionEquivLeft_coeff_coeff; canonical path: Mathlib/Algebra/MvPolynomial/Equiv.lean:610; canonical existing calls: 1; old form existing calls: 4; old form ingredients: MvPolynomial.optionEquivLeft_coeff_coeff, Finsupp.update_eq_add_single, Finsupp.embDomain_some_none, Finsupp.embDomain_eq_mapDomain; representation: optionElim versus mapDomain some + single none is propositional normalization, not definitional equality; abstract: Finsupp.comapDomain_apply at Mathlib/Data/Finsupp/Basic.lean:517

Completed `Roth.eq_sum_X_none_pow_mul_coeffNone`: canonical: Polynomial.as_sum_range_C_mul_X_pow'; canonical path: Mathlib/Algebra/Polynomial/Degree/Support.lean:93; canonical existing calls: 1; degree bridge: MvPolynomial.natDegree_optionEquivLeft; old form existing calls: >3 named ingredients plus genuine normalization proof; not NO-composable; old form ingredients: Polynomial.as_sum_range_C_mul_X_pow', MvPolynomial.natDegree_optionEquivLeft, MvPolynomial.optionEquivLeft, MvPolynomial.optionEquivLeft_symm_X, Polynomial.aevalTower_C, map_sum, map_mul, map_pow, mul_comm; representation: Inverse C/rename and finite sum transport are actual checked proofs, not definitional old-form equality.

Completed `Roth.degreeOf_coeffNone_le`: structural building blocks: MvPolynomial.degreeOf_le_iff, MvPolynomial.monomial_le_degreeOf, MvPolynomial.mem_support_coeff_optionEquivLeft; normalization: Finsupp.optionElim_apply_eq_elim, Option.elim_some; finite analog: MvPolynomial.degreeOf_coeff_finSuccEquiv; finite analog path: Mathlib/Algebra/MvPolynomial/Equiv.lean:834; old form calls: 3 structural calls plus nondefinitional projection rewrite; >3 named dependencies; canonical form calls: Same proof and normalization after replacing coeffNone with Polynomial.coeff of optionEquivLeft; search limitations: Local source search positive but index unavailable; external snapshots may differ. No absence claim inferred from empty queries.

Completed `Roth.coeff_rename_mul_aeval`: existing core: Polynomial.coeff_C_mul, Polynomial.coeff_map, AddMonoidAlgebra.coeff_mul_single_zero; coordinate transport: MvPolynomial.optionEquivLeft_coeff_coeff, Finsupp.update_eq_add_single, Finsupp.embDomain_some_none, Finsupp.embDomain_eq_mapDomain, MvPolynomial.optionEquivLeft_X_none, Polynomial.aeval_algHom_apply, Polynomial.aeval_X_left_eq_map; methods: Finder, Loogle, LeanSearch, rg, local; forms: current, standard, abstract; limits: Initial current Loogle query rejected unknown MvPolynomial.coeff; successful quoted-coeff retry empty. Local index unavailable with source fallback hits, no absence claim. External revisions differ from pinned source.

Completed `Roth.aeval_X_eq_rename`: verdict: NO-mathlib-has-it; existing: Polynomial.toMvPolynomial_eq_rename_comp; path: Mathlib/Algebra/MvPolynomial/Equiv.lean:891; proof: AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f; five methods all three forms: True; local index: unavailable; positive lexical fallback, not absence; pinned native positive: True

Completed `Roth.hasseDeriv_rename_mul_aeval`: verdict: YES-but-generalise-first; cells: 15; partial hits: Polynomial.hasseDeriv_mul, Polynomial.hasseDeriv_map, Polynomial.hasseDeriv_coeff, Polynomial.toMvPolynomial_eq_rename_comp, Polynomial.taylor_mul, Polynomial.taylor_coeff; note: All multivariate Hasse names in the project namespace originate in Roth/HasseDeriv.lean; pinned mathlib supplies univariate API only. Missing multivariate guard compiled in isolated mathlib environment.

Completed `Roth.coeff_uniqueAlgEquiv_symm`: existing: MvPolynomial.coeff_uniqueAlgEquiv_symm; file: Mathlib/Algebra/MvPolynomial/Equiv.lean:115; auxiliary: Finsupp.single_eq_same, Finsupp.unique_single; search: 15 method/form cells plus a repaired Loogle query and rate-limit retry; pinned exact signatures and specialization compiled without Roth imports.

Completed `Roth.degreeOf_uniqueAlgEquiv_symm`: verdict: BORDERLINE-needs-human; existing canonical law: MvPolynomial.degreeOf_eq_natDegree; other hits: MvPolynomial.natDegree_optionEquivLeft, MvPolynomial.coeff_uniqueAlgEquiv_symm, Polynomial.natDegree_map_eq_of_injective, MvPolynomial.C_injective, MvPolynomial.degreeOf_eq_sup, Polynomial.supDegree_eq_natDegree; exact target located: False; new bridge required: True; cells: 15; local index: unavailable; source hits checked natively

Completed `Roth.degreeOf_rename_mul_aeval`: verdict: BORDERLINE-needs-human; positive candidates: MvPolynomial.degreeOf_mul_eq, MvPolynomial.degreeOf_rename_of_injective, Polynomial.toMvPolynomial_eq_rename_comp, Polynomial.toMvPolynomial_injective, MvPolynomial.degreeOf_C_mul; search cells: 15; canonical bridge: Actual mathlib aeval/rename bridge replaces Roth.aeval_X_eq_rename; independent-degree normalization remains proof.

Completed `Roth.degreeOf_none_rename_mul_aeval`: All15 methods/forms executed; canonical natDegree_optionEquivLeft, Polynomial.natDegree_C_mul, natDegree_C_mul_of_mul_ne_zero and injective coefficient map degree verified.

Completed `Roth.linearIndependent_coordinate_polynomials_aux`: A vanishing linear combination gives one coefficient identity for each member of the spanning family. The corresponding weighted sum of basis coordinate functionals vanishes on that family, hence on its span by LinearMap.ext_on; evaluating on each basis vector forces every scalar coefficient to vanish. This is a live private linear-algebra component of the separated representation, distinct from the basis-existence and polynomial reconstruction helpers.

Completed `Roth.eq_sum_aeval_basis_coeffNone_aux`: Expand each coefficient polynomial in the chosen basis using Module.Basis.sum_repr, substitute into the given coefficient expansion, interchange the finite sums and normalize aeval, renaming and scalar multiplication. This reconstruction identity is distinct from coordinate-polynomial independence and from choosing a bounded basis.

Completed `Roth.exists_coeffNone_basis_aux`: The finitely many coefficient polynomials span a finite-dimensional space. Nonzero input forces at least one nonzero coefficient and thus positive finrank; finrank_range_le_card gives the upper bound. The span lies in a support-restriction submodule by coefficient-support transport, so every basis vector inherits the individual degree bounds. This basis-selection helper is distinct from reconstruction and coordinate-family independence.

Completed `Roth.exists_separated_representation`: formal search cells: 15; supplementary pid cells: 5; existing candidates: Module.finBasis, Module.free_of_finite_type_torsion_free', TensorProduct.exists_sum_tmul_eq, TensorProduct.eq_repr_basis_left, TensorProduct.eq_repr_basis_right, Matrix.exists_rank_normal_form; conclusion: Complete mathlib-only unconditional PID proof, complete rational caller and conditional free-span proof verified; existing finite/free/tensor/rank primitives still require substantive coordinate/degree reconstruction.

Completed `Roth.det_hasseDeriv_separated`: All15 cells executed. Pinned Matrix.det_mul, Matrix.det_transpose and AlgHom.map_det cover only the determinant core; isolated exact generic composition compiles. Binary Polynomial.wronskian and univariate hasseDeriv_mul do not replace the arbitrary-family mixed-variable theorem. Local symbol index unavailable; no universal absence claim.

Completed `Roth.exists_sum_mul_eq_gcd`: existing: Finset.gcd_eq_sum_mul; path: Mathlib/RingTheory/PrincipalIdealDomain.lean:233; normalization: eq_comm, mul_comm; verified: mathlib-only original/generic statements and full sole caller

Completed `Roth.exists_nat_smul_eq_map`: methods: 15; existing: IsLocalization.exists_integer_multiple, IsLocalization.exist_integer_multiples, MvPolynomial.isLocalization; exact replacement: Verified with genuine positivity/cast/scalar normalization; not ≤3 existing calls.; local index: unavailable; not absence evidence

Completed `Roth.exists_primitive_smul_eq`: verdict: YES-but-generalise-first; fifteen actual search cells: True; building blocks: Finset.extract_gcd, Finset.gcd_eq_zero_iff, MvPolynomial.isLocalization, IsLocalization.exists_integer_multiple, IsFractionRing.injective; near misses: Polynomial.primPart/content/IsPrimitive concern univariate polynomials., IsFractionRing.exists_reduced_fraction concerns one fraction., Projectivization.exists_smul_eq_mk_rep does not enforce integral gcd1 coordinates.; composition: No verified ≤3-existing-call composition; polynomial reconstruction, mapped-scalar normalization and support-gcd transport remain genuine proof.

Completed `Roth.exists_int_eq_of_gcd_eq_one`: actual search cells: 15; forms: current, standard, abstract; positive candidates: Finset.gcd_eq_sum_mul, Submodule.mem_of_span_top_of_smul_mem, Submodule.smul_mem_iff_of_isUnit, IsLocalization.IsInteger, IsLocalization.isInteger_smul; exact replacement: False; bridge: Finite gcd to submodule membership is a newly proved linear-combination bridge; existing unit-ideal law has a different premise.

Completed `Roth.rescale_separated_factor_aux`: Use the given scalar rescaling, move constant polynomials through coefficient renaming and polynomial evaluation, commute the four factors, and cancel the scalar with its inverse using the nonzero hypothesis. This scalar compensation identity is distinct from coefficient integrality and degree preservation, and is used by exists_int_factors.

Completed `Roth.exists_int_polynomial_of_primitive_factor_aux`: For each univariate coefficient, coeff_rename_mul_aeval identifies its products with the primitive factor coefficients as integer coefficients of the given product. exists_int_eq_of_gcd_eq_one then gives an integer witness for each coefficient, and Polynomial.mem_map_range assembles the integer polynomial. This coefficient descent is distinct from scalar compensation and from choosing a primitive representative.

Completed `Roth.exists_int_factors`: status: Partial Gauss/localization/reduced-GCD matches, no full target or ≤3-call proof verified.; existing: Polynomial.IsPrimitive.map_mul_mem_lifts_iff, Polynomial.IsPrimitive.mul_map_mem_lifts_iff, Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map, IsLocalization.surj_of_gcd_domain, MvPolynomial.isLocalization; search forms: current, standard, abstract; all five methods executed: True; index caveat: Local index unavailable; fallback hits include scratch project proofs, external versions can differ.

Completed `Roth.exists_rat_factors_det_hasseDeriv_aux`: Map the polynomial injectively to the rationals, apply exists_separated_representation, choose bounded derivative indices using exists_genWronskian_ne_zero, and factor the resulting determinant by det_hasseDeriv_separated. Independent univariate factors give wronskian_ne_zero_of_linearIndependent, while hasseDeriv_map transports the determinant back to the mapped integer determinant. This rational factor construction is distinct from the subsequent integer factor descent.

Completed `Roth.exists_det_eq_mul`: 15 actual search cells; positive univariate Hasse/binary Wronskian/matrix determinant/localization/degree-map building blocks inspected and native checked; no verified ≤3 existing-call replacement. Index unavailable is recorded, not absence.

Completed `Roth.RSet`: methods: 5; forms: 3; cells: 15; verified candidates: MvPolynomial.restrictSupport, MvPolynomial.mem_restrictSupport_iff, MvPolynomial.basisRestrictSupport, MvPolynomial.restrictSupport_add, MvPolynomial.mem_restrictDegree, MvPolynomial.degreeOf_le_iff; limitations: Online revision may differ. Local search reports index unavailable. No complete ≤3 existing-call replacement verified.

Completed `Roth.indexSet`: methods: 5; forms: 3; cells: 15; verified candidates: Set.image2, Set.mem_image2, Set.mem_image2_of_mem, Set.Nonempty.image2, Set.image2_nonempty_iff, Set.image2_subset, Set.forall_mem_image2, Set.image2_congr', AddMonoidAlgebra.infDegree; limitations: Initial standard Loogle sSup query rejected and corrected with SupSet.sSup. Local target index unavailable. Remote indexes may differ from pinned signatures.

Completed `Roth.Θ`: methods: 5; forms: 3; cells: 15; verified candidates: SupSet.sSup, le_csSup, csSup_le, csSup_le_csSup, Real.sSup_nonneg, Real.sSup_le, Real.sSup_empty, Real.sSup_of_not_bddAbove, sSup_image2, csSup_image; limitations: Local symbol index unavailable; online snapshots may differ. Complete-lattice sSup_image2 is not usable directly on real totalized suprema; negative instance guard verifies this.

Completed `Roth.lem6M`: Five methods on current/standard/abstract forms; arithmetic primitives confirmed; no identified existing parameterized bound.

Completed `Roth.lem6Φ`: All15cells; positive generic Add.add(sSup A)(sSup B) exactly3outercalls; expanded arithmetic inputs have morecalls and are not mislabeled.

Completed `Roth.one_mem_RSet`: All15 search cells; pinned degreeOf_one, coeff_one, coeff_one_zero, one_ne_zero, Nat.zero_le, abs_one/zero. Full family not replaced by univariate root or height results. Closing simp is SIMP-COMPOSABLE; no strict≤3existing-call term verified.

Completed `Roth.indexSet_nonempty`: All15 method×form cells: Set.Nonempty.image2 and Set.image2_nonempty_iff independently native verified; local index unavailable disclosed.

Completed `Roth.indexSet_bddAbove`: Set.forall_mem_image2 gives one-call structural predicate transport; constructor yields BddAbove from supplied uniform bound. BddAbove.image2 rejected because monotonicity and bounded ordered source premises differ. No full existing arithmetic theorem established.

Completed `Roth.index_le_Θ`: Pinned le_csSup exactly supplies the abstract membership-to-supremum law; Set.mem_image2_of_mem independently verifies image2 membership.

Completed `Roth.Θ_nonneg`: law: Real.sSup_nonneg; parent: SupSet.sSup; pointwise: Real.sInf_nonneg, Finset.sum_nonneg, div_nonneg, Nat.cast_nonneg; family transport: Set.forall_mem_image2.mpr; defaults: Real.sSup_empty, Real.sSup_of_not_bddAbove; status: 15 search cells and five clean native sets

Completed `Roth.Θ_le_card`: Five actual methods on current, literature and abstract forms. Real.sSup_le exactly covers supremum transport and Set.forall_mem_image2 covers quantifier transport. weightedOrder_le and polynomial degree lemmas are partial building blocks; full degree-normalized uniform bound still uses project index_le_card.

Completed `Roth.Θ_le_of_forall_index_le`: NO-mathlib-has-it: independently verified csSup_le at the exact sSup parent. Old representation uses one mathlib call plus one project nonempty helper and logical witness transport; parent helper is not counted as a mathlib block.

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

Completed `Roth.box`: Principal lower interval of Finsupp pointwise order, MainLemma282-323 already uses Iic(ofSupportFinite r) under finite-support bounds

Completed `Roth.weight`: Finsupp.weight, Finsupp.linearCombination

Completed `Roth.mem_box`: Box API duplicates existing product/interval membership.

Completed `Roth.card_box`: Generic finite Cartesian-product counting.

Completed `Roth.card_le_card_box`: Finite Cartesian-product cardinality and monotonicity under inclusion, Finsupp interval cardinality bound after membership and endpoint normalization

Completed `Roth.weight_nonneg`: Elementary sum positivity after definitional reduction; not a duplicated named Finsupp theorem

Completed `Roth.weight_zero`: Zero preservation already structural for bundled Finsupp.weight; bridge from ratio formula is not defeq.

Completed `Roth.weight_add`: Weighted monomial degree is an additive homomorphism; current ratio representation requires normalization.

Completed `Roth.weight_eq_zero_iff`: Positive sum zero principle already exists; reciprocal/cast/finsupp packaging is project API.

Completed `Roth.weight_single`: Finsupp.weight_single, Finsupp.sum_single_index

Completed `Roth.weight_le_card`: Instance of generic finite-sum upper bound. Parent Finsupp.weight bridge verified; no matching dedicated upper-cardinality law established.

Completed `Roth.weight_mul_left`: Finsupp.bilinearCombination.map_smul, Finsupp.linearCombination generator linearity

Completed `Roth.weight_le_degree_div`: Finset.sum_le_sum + div_le_div_of_nonneg_left proof pattern, Finsupp.sum_le_sum aggregation, Related real-ratio proof in Roth.weight_le_delta_aux

Completed `Roth.weight_mapDomain`: Naturality of free-module evaluation under generator relabelling, Finsupp.linearCombination_comp_lmapDomain bundled companion

Completed `Roth.wronskianMatrix`: Direct construction is a verified two-block composition; meaningful semantic API exemption., Multivariate genWronskian constructs related selected-operator matrix, not identical target.

Completed `Roth.wronskian`: Binary Wronskian specializes at l2, not arbitrary arity, Generic determinant infrastructure already handles raw data construction

Completed `Roth.wronskian_eq_zero_of_not_linearIndependent`: Multivariate easy direction repeats relation/kernel argument; generic operator-family route can unify.

Completed `Roth.det_choose_eq`: Generic monic evaluation content is already in mathlib; specific binomial normalization resembles an existing private integer bridge. Do not add another generic evaluation theorem.

Completed `Roth.coeff_prod_of_natDegree_le'`: Related public common-bound API, not the same statement; no project duplicate found.

Completed `Roth.sum_range_le_sum_of_injective`: Existing sharper lower-bounded finite integer-set sum theorem already contains the Nat/Fin c=0 case.

Completed `Roth.coeff_wronskian_of_natDegree_injective`: Classical leading-monomial/Vandermonde calculation; existing common-bound product coefficient theorem does not directly give varying bounds. No exact pinned replacement found.

Completed `Roth.wronskian_ne_zero_of_natDegree_injective`: Generic coefficient nonzero and Vandermonde nonzero steps already abstract. Hasse coefficient and binomial conversion bridges remain new mathematical helpers; downstream criterion cannot be used circularly.

Completed `Roth.wronskian_update_sub_smul`: Elementary determinant transvection, but not a defeq or strict <=3-existing-call replacement for the family statement.

Completed `Roth.linearIndependent_update_sub_smul`: linearIndependent_add_smul_iff, Mathlib/LinearAlgebra/LinearIndependent/Defs.lean:751

Completed `Roth.sum_natDegree_update_lt`: Standard leading-term cancellation plus generic finite-sum comparison; normalized cancelLeads bridge is compiled, not definitional.

Completed `Roth.wronskian_ne_zero_of_linearIndependent`: The existing general elementary-shear independence law replaces one helper, not the Wronskian criterion. Downstream iff and generalized Wronskian theorem are circular replacements.

Completed `Roth.wronskian_eq_zero_iff`: Propositional assembly duplicates no substantive mathlib theorem: both constituent criterion lemmas are project-local. Generic matrix determinant dependence helps only the easy direction with scalar/jet bridges.

Completed `MvPolynomial.taylor`: MvPolynomial.aeval (fun j ↦ X j + C (α j)), MvPolynomial.bind₁ with the same substitution, Polynomial.taylorAlgHom: univariate analogy only

Completed `MvPolynomial.taylor_apply`: Own defining equation applied to P, Polynomial.taylor_apply: genuine univariate API analogy only

Completed `MvPolynomial.taylor_X`: MvPolynomial.aeval_X specialized definitionally to the translation assignment

Completed `MvPolynomial.taylor_C`: Specialization of generic AlgHom coefficient preservation; univariate Polynomial.taylor_C is analogous but not identical.

Completed `MvPolynomial.taylor_monomial`: Existing aeval_monomial specialized to g j=X j+C(α j), A=MvPolynomial σ R.

Completed `MvPolynomial.coeff_aeval_X_mul`: One implementation and one direct caller; isolates the support-independent coefficient extraction, not the full Hasse/Taylor theorem.

Completed `MvPolynomial.hasseCoeff_single_add_eq`: Special coordinate factorization, distinct from general cocycle or successor identities in HasseDeriv; one shared implementation for the monomial induction.

Completed `MvPolynomial.prod_pow_single_add_tsub`: Exponent splitting differs from scalar binomial-coordinate helper; no second exact implementation in module.

Completed `MvPolynomial.coeff_taylor_monomial_single_add_aux`: Coordinate induction step is distinct from universal aeval_monomial and full coefficient theorem; scalar helpers separate different calculations.

Completed `MvPolynomial.coeff_taylor_monomial_aux`: Monomial special case is proof scaffold for linear extension, distinct from aeval_monomial image formula and full coefficient theorem.

Completed `MvPolynomial.coeff_taylor`: Univariate Polynomial.taylor_coeff is analogous, not a replacement for arbitrary σ., Direct aeval statement is definitionally equivalent, not a distinct theorem.

Completed `MvPolynomial.eval_taylor`: Abstract substitution-evaluation law already exists; Polynomial.taylor_eval is a univariate analogue only.

Completed `MvPolynomial.taylor_taylor`: Polynomial.taylor_taylor is only a univariate analogue; generic comp_aeval_apply needs nondefinitional generator normalization.

Completed `MvPolynomial.taylor_zero`: Elementary identity-assignment law after zero normalization; not a direct definitional specialization.

Completed `MvPolynomial.taylor_map`: Naturality of substitution specialized to translations; no distinct new mathematical argument.

Completed `MvPolynomial.taylor_rename`: Generic substitution naturality specialized to shifted generators; close analogue rename_expand, not same substitution.

Completed `MvPolynomial.degreeOf_taylor_le`: Univariate Taylor degree invariance is analogous but not direct replacement. Direct aeval spelling is definitionally equivalent.

Completed `MvPolynomial.taylor_neg_taylor`: Specializes additive composition to mutually cancelling shifts, and is a left-inverse interface for injectivity. Neither is a duplicate of composition or injectivity.

Completed `MvPolynomial.taylor_injective`: A generic left-inverse corollary, analogous to univariate Taylor injectivity. Not an independently available multivariate all-mathlib one-call term.

Completed `MvPolynomial.taylor_eq_zero_iff`: Univariate zero-reflection analogue and generic ring injectivity corollary; stronger arbitrary-variable semiring theorem provides genuine additional triangular coefficient content.

Completed `MvPolynomial.eq_sum_box_hasseDeriv`: Distinct coefficient, polynomial reconstruction and evaluation layers; same inverse-shift motif as univariate sum_taylor_eq but no direct specialization to multivariate Hasse box expansion.

Completed `MvPolynomial.eval_eq_sum_box`: Polynomial reconstruction, coefficient identification and evaluated scalar identity are distinct layers; Main consumer adds strict analytic estimates. No independent full evaluated expansion rederivation found.

Completed `Roth.normOne`: No second full coefficient-L1 definition found. Diagonal/evaluation absolute-sum estimates concern different quantities. Bound laws need independent assessments rather than automatic inheritance of construction verdict.

Completed `Roth.diag`: No second arbitrary-variable diagonal implementation found; HasseDeriv unique-variable transport is different. Not generating-series coefficient diagonal extraction. Bounds need independent assessments.

Completed `Roth.normOne_nonneg`: Generic finite-sum nonnegativity; individual abs_nonneg uses elsewhere are not duplicate full theorem.

Completed `Roth.normOne_eq_sum_of_support_subset`: Support-padding law already in Finsupp API. Univariate Polynomial.sum_eq_of_subset is analogous, not direct multivariate replacement. Hamming norm and module length semantic hits measure different objects.

Completed `Roth.normOne_monomial`: Exact singleton sum law already in MvPolynomial and Finsupp. Univariate Polynomial.sum_monomial_index analogous. supNorm_monomial/gaussNorm_monomial are distinct size functions, not whole normOne replacements.

Completed `Roth.normOne_zero`: Exact empty finite-support aggregate law already in mathlib; Polynomial.sum_zero_index analogous; support_zero+sum_empty alternative. Generic norm_zero requires a correct norm structure. Nearby normOne_neg/cardinality proofs are not inline duplicate zero laws.

Completed `Roth.abs_coeff_le_normOne`: A direct specialization of an existing general finite-support nonnegative coordinate bound. Mathlib NumberTheory/Height/MvPolynomial.lean:277 uses same generic law for absolute values.

Completed `Roth.normOne_add_le`: Mathematically an l1 triangle inequality, but existing sup-norm and integral norm theorems concern different objects; no inherited has-it result from parent.

Completed `Roth.normOne_neg`: Standard norm sign invariance; existing Finsupp coordinate reindexing is sufficient. Height/integralL1/fieldnorm are different objects.

Completed `Roth.normOne_sum_le`: Abstract subadditive finite-sum bound and norm_sum_le; direct existing theorem specializes once the project zero/triangle witnesses are supplied.

Completed `Roth.normOne_mul_le`: Discrete Young L1 convolution inequality; standard normed-ring law is analogous but no verified representation bridge.

Completed `Roth.normOne_prod_le`: Finite iteration of discrete Young coefficient L1 convolution bound; generic finite submultiplicative map bound already in mathlib.

Completed `Roth.normOne_le_card_mul`: Same scalar finite-family inequality independently used by abs_coeff_diag_le; exact target already duplicates existing generic Finset theorem.

Completed `Roth.normOne_det_le`: Analog of Matrix.det_le for merely submultiplicative real seminorms; degree/index/Wronskian determinant expansions prove different laws.

Completed `Roth.abs_coeff_hasseDeriv_le`: Same finite binomial factor appears in normOne_hasseDeriv_le; that is an L1 estimate and cannot retain the coefficient B without an unwanted support-cardinality factor.

Completed `Roth.normOne_hasseDeriv_le`: Univariate Hasse coefficient formula is an analogue; Gauss sup norm, Mahler measure, and coefficient sup bound are distinct estimates.

Completed `Roth.diag_eq_sum`: Elementary specialization and normalization of existing evaluation expansion; genuine product-power/monomial bridge prevents claiming definitional exact duplicate.

Completed `Roth.abs_coeff_diag_le`: A finite-fiber pushforward triangle bound; abstract Finset inequalities exist but the polynomial substitution-to-fiber bridge is real normalization, not definitional equality.

Completed `Roth.natDegree_diag_le`: Overlaps existing aeval substitution law; local coordinate sum hypothesis bridge is distinct and not definitional.

Completed `Roth.eval_diag`: Generic polynomial substitution associativity/naturality already in mathlib and re-used inline.

Completed `Roth.diag_sub`: Wrapper of map_sub; no independent algebraic content.

Completed `Roth.geom_sum_le_one_add_pow`: No project duplicate or inspected exact existing replacement; binomial expansion is mathematical source, not a direct replacement.

Completed `Roth.sum_box_prod_pow_le_aux`: Finite-box product estimate is an internal factorization stage, distinct from scalar geometric sum and polynomial support/evaluation bound. No duplicate full argument found in this source review.

Completed `Roth.abs_eval_le`: No duplicate: abs_coeff_diag_le handles coefficient collisions; normOne_le_card_mul is unweighted; Main.abs_eval_lt_of_le_index is a Taylor/index estimate. A future weighted-support majorant can share proof stages with the homogeneous bound.

Completed `Roth.degreeOf_det_hasseDeriv_le`: Generic polynomial determinant degree bound underlies this Hasse specialization; no current mathlib exact replacement verified.

Completed `Roth.abs_coeff_det_hasseDeriv_le`: A Hasse-specific assembly of support-cardinality, derivative-length and determinant seminorm estimates. Prior accepted project assessments do not make these existing mathlib lemmas.

Completed `Roth.genWronskian`: One-line determinant wrapper, with established semantic API exemption. Raw entry-dependent derivative matrices in CoeffNorm/Separation/Theta are related but not copies of its row-order/family-column form.

Completed `Roth.kronecker`: Literal one-call specialization of existing universal evaluation, with legitimate local semantic naming exemption.

Completed `Roth.kroneckerExp`: Specialization of existing generic weighted exponent map. Shared generic API pattern with independently accepted Roth.weight, which instead targets Real with reciprocal weights; these project maps are not equal.

Completed `Roth.kronHasse`: Private operator composition and bounded module span are different stages of the same derivative expansion, not duplicate full constructions.

Completed `Roth.kronSpan`: Private operator composition and bounded module span are different stages of the same derivative expansion, not duplicate full constructions.

Completed `Roth.genWronskian_eq_zero_of_not_linearIndependent`: Roth.wronskian_eq_zero_of_not_linearIndependent has analogous coefficient-witness proof

Completed `Roth.kronecker_monomial`: Redundant specialization of existing generic monomial evaluation under parent re-aim. Old spelling requires genuine finite-product normalization; not definitional and not a one-call old-form proof.

Completed `Roth.kroneckerExp_injOn`: Private NoetherNormalization.sum_r_mul_ne90–98 independently performs essentially same positional conversion. Its expanded statement replays using generalized weight helper; not a public exact replacement or actual source caller.

Completed `Roth.coeff_kronecker`: Coefficient separation is existing support-local mapDomain transport; exact aeval coefficient API not identified.

Completed `Roth.kronecker_eq_zero_iff`: Abstract support-local injection is already in Finsupp.mapDomain_injOn; no duplicate Finsupp theorem needed.

Completed `Roth.linearIndependent_kronecker`: Final linear relation transport duplicates generic map_injOn; degree-bound/weighted-support sufficient condition is additional specialized proof.

Completed `Roth.derivative_aeval`: Standard multivariable analogue of the existing univariate chain rule; no verified existing ≤3-call replacement.

Completed `Roth.derivative_kronHasse_aux`: Private operator composition and bounded module span are different stages of the same derivative expansion, not duplicate full constructions.

Completed `Roth.derivative_mem_kronSpan`: Private operator composition and bounded module span are different stages of the same derivative expansion, not duplicate full constructions.

Completed `Roth.hasseDeriv_kronecker_mem`: Private operator composition and bounded module span are different stages of the same derivative expansion, not duplicate full constructions.

Completed `Roth.exists_hasseDeriv_kronecker_eq_sum`: Final extraction is generic span linear algebra, but the private uniform higher chain-rule premise is new project content. No verified existing <=3-call replacement for the full law.

Completed `Roth.det_sum_rows`: Standard multilinearity, already represented by two generic mathlib laws; convenience wrapper inclusion is a Phase6b taste decision.

Completed `Roth.wronskian_kronecker_eq_sum_aux`: The determinant transport is distinct from the standalone row-multilinearity expansion and from the final nonvanishing implication; no duplicate full construction.

Completed `Roth.exists_genWronskian_ne_zero`: Classical Bostan–Dumas Theorem3 polynomial specialization, with Hasse normalization; not duplicated by existing two-polynomial Wronskian API.

Completed `Roth.sqrt_one_sub_inv_lt`: A specialized Bernoulli/AM-GM consequence, not an identical theorem.

Completed `Roth.inv_add_inv_le`: Complementary-pair and whole-grid reciprocal estimates are distinct steps of the lattice proof, not duplicate full constructions.

Completed `Roth.sum_inv_le`: Complementary-pair and whole-grid reciprocal estimates are distinct steps of the lattice proof, not duplicate full constructions.

Completed `Roth.sum_inv_lt`: Reciprocal convexity already follows from convexOn_zpow(-1); sum reindexing exists. Grid rational upper bound and sqrt comparison still need proof.

Completed `Roth.extend_apply_castSucc`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.extend_apply_last`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.card_filter_box_fiber_aux`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.card_filter_box_last`: Abstract counting is Finset.card_eq_sum_card_fiberwise; geometric Finsupp identification is real project proof.

Completed `Roth.filter_weight_le_eq_empty`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.card_filter_fiber_eq`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.card_filter_weight_le_of_le_sqrt_aux`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.card_filter_weight_le_succ_aux`: The helper has a distinct role in the lattice proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.card_filter_weight_le`: Not Roth arithmetic-progression/Behrend results. Generic fibre count handles decomposition, probability theory supplies a potential stronger route requiring new uniform-box moment/count bridges.

Completed `Roth.index`: Generic support minimum is already infDegree., Natural weightedOrder is a positive-integral-parameter alternate interface; its project bridge is actual proof, not an existing library call.

Completed `Roth.mem_support_taylor_iff`: The helper has a distinct role in the index proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.index_le_weight`: Finite infimum is bounded by each member, independently of the degree map; already Finset.inf_le.

Completed `Roth.exists_weight_eq_index`: Attainment of a finite nonempty support infimum in a linear order is already Finset.exists_mem_eq_inf., MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder provides the standard natural-weight analogue.

Completed `Roth.le_index_iff`: Finite meet lower-bound universal property, not a new theorem about derivatives.

Completed `Roth.index_nonneg`: Finite infimum preserves a common lower bound. Polynomial and point data select the finite support but add no order-theoretic content.

Completed `Roth.index_eq_zero_iff`: Finite support minimum equals bottom iff a supported degree is bottom, Taylor constant coefficient is evaluation at center

Completed `Roth.index_sub_weight_le_index_hasseDeriv`: Classical Roth/Milojevic derivative-index estimate. Generic infDegree sums/products are adjacent, not duplicates. New supportShift proof is not a preexisting mathlib call.

Completed `Roth.le_index_sum`: Classical minimum-order sum inequality, exactly generic finite-support degree inequality under OrderDual. MvPowerSeries.min_weightedOrder_le_add is adjacent natural-weight binary API.

Completed `Roth.weight_eq_finsuppWeight_div`: Generic map/linearity law already exists; no claim that denominator arithmetic is definitional or ≤3 calls.

Completed `Roth.index_eq_weightedOrder_div`: Original proof manually identifies two minima; this is missing generic bridge API, not duplicated existing comparison.

Completed `Roth.index_mul`: The natural-weight algebraic core is exactly the existing series multiplication theorem. The old real-index spelling requires genuine normalization and finite projection; new comparison proofs from133/143 are not preexisting mathlib calls.

Completed `Roth.index_prod`: Natural-series finite-product additivity is already mathlib. Old real default-zero form needs genuine normalization, finite projection and casting. Parent local binary law and earlier new bridge proofs are not existing mathlib calls.

Completed `Roth.index_neg`: Degree support-negation law; weightedOrder_neg/order_neg are related alternative APIs.

Completed `Roth.index_C_mul`: Scalar support invariance; related weightedOrder inequality/multiplication and negation API.

Completed `Roth.index_mul_left_weights`: Homogeneous scaling of a finite support minimum is existing finite-inf hom transport. Original representation bridge is genuine normalization, not definitional or a preexisting theorem.

Completed `Roth.index_rename`: Underlying finite-support transport duplicates generic lattice image functoriality; weightedTotalDegree rename is a related maximum law, not the exact minimum.

Completed `Roth.index_le_card`: Canonical support-witness estimate is existing infDegree/Finset.inf_le; coordinate weight bound overlaps weight_le_card. Neither alone is exact full theorem.

Completed `Roth.index_unique`: Existing rootMultiplicity_eq_natTrailingDegree is the analogous univariate law of the parent infDegree abstraction., Existing natTrailingDegree coefficient/support laws express the least nonzero coefficient.

Completed `Roth.coeffNone`: New plain-function name for existing equivalence followed by coordinate projection; local semantic-name exemption acknowledged.

Completed `Roth.eq_mapDomain_some_add_single`: Finsupp.optionElim_some expresses reconstruction at Zero generality; expanded additive form requires bridge

Completed `Roth.coeff_X_none_pow_mul_rename`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.coeff_coeffNone`: The existing canonical coefficient correspondence is the same mathematical law under normalized exponent coordinates.

Completed `Roth.eq_sum_X_none_pow_mul_coeffNone`: Polynomial coefficient reconstruction under the existing iterated polynomial-ring algebra equivalence.

Completed `Roth.degreeOf_coeffNone_le`: Arbitrary Option analogue of existing finite degreeOf_coeff_finSuccEquiv., Support insertion preserves remaining coordinate bounds; abstract finite supremum proof verified as a component, not existing full replacement.

Completed `Roth.coeff_rename_mul_aeval`: Canonical double coefficient law is exactly three existing calls; first-coefficient-only law is insufficient for the full theorem., No exact original Option/aeval law was verified as a single existing theorem.

Completed `Roth.aeval_X_eq_rename`: Pointwise specialization of existing equality of the same R-algebra homomorphisms; no new mathematical law.

Completed `Roth.hasseDeriv_rename_mul_aeval`: Univariate constant outer-factor Hasse law is proved in mathlib-only scratch; it covers only the none-coordinate part., Previous159 aeval bridge is already in mathlib, and its wrapper is eliminated in the target replay.

Completed `Roth.coeff_uniqueAlgEquiv_symm`: The Roth law is the singleton-exponent specialization of the existing arbitrary-finsupp law, not a namespace-aware prefilter hit.

Completed `Roth.degreeOf_uniqueAlgEquiv_symm`: The selected-variable/natDegree content exists canonically, but a genuine newly proved presentation bridge is needed to apply it to uniqueAlgEquiv. No automatic inherited NO from coefficient theorem161.

Completed `Roth.degreeOf_rename_mul_aeval`: Product-degree additivity plus injective renaming are existing mathlib facts., Analogous none-variable theorem is distinct because its RHS is V.natDegree.

Completed `Roth.degreeOf_none_rename_mul_aeval`: Canonical constant-multiplication degree law exists, but old separated form needs an actual new AlgHom normalization proof.

Completed `Roth.linearIndependent_coordinate_polynomials_aux`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.eq_sum_aeval_basis_coeffNone_aux`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.exists_coeffNone_basis_aux`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.exists_separated_representation`: Two-factor tensor/matrix rank factorization is abstract mathematical context; generic pure-tensor expansion loses simultaneous independence and bounds.

Completed `Roth.det_hasseDeriv_separated`: Outer matrix formula is existing det_mul+transpose. Full derivative matrix normalization uses project multivariate Hasse/product API and is not an existing ≤3-call mathlib replacement.

Completed `Roth.exists_sum_mul_eq_gcd`: Integer specialization and reordered equality of existing finite Bezout theorem.

Completed `Roth.exists_nat_smul_eq_map`: Same denominator mechanism as existing localization laws; concrete positive-natural output packaging is not an exact short existing-call theorem.

Completed `Roth.exists_primitive_smul_eq`: Classical content/primitive-part normalization underlying Gauss lemma, not the whole product-primitivity law., Finite-function gcd extraction is already mathlib; the multivariate/fraction-field bridge is additional.

Completed `Roth.exists_int_eq_of_gcd_eq_one`: finite Bezout identity, membership detected by generators of unit ideal

Completed `Roth.rescale_separated_factor_aux`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.exists_int_polynomial_of_primitive_factor_aux`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.exists_int_factors`: Gauss-type descent; univariate Gauss integrality is a partial match requiring actual multivariate and support/primitivity bridges.

Completed `Roth.exists_rat_factors_det_hasseDeriv_aux`: The helper has a distinct role in the separated polynomial proof as described in the structural review; no duplicate full construction is introduced.

Completed `Roth.exists_det_eq_mul`: det_mul and map_det cover transport but not bounded derivative-row selection, nonvanishing and original-ring separated descent. Binary Polynomial.wronskian is not the finite-family construction.

Completed `Roth.RSet`: Degree component is the existing restrictSupport carrier., Finite coefficient-array boxes compose with Finset.finsupp under extra finite exponent-box data., Polynomial.supNorm is univariate; projective Height and ℓ¹ norm are not the same bound.

Completed `Roth.indexSet`: Exact generic outer binary-image construction already exists., Parent index normalization re-aims to infDegree/Finsupp.weight/aeval, with explicit default0 projection.

Completed `Roth.Θ`: Outer supremum operation is exact existing SupSet.sSup specialization., Parent family is exact Set.image2; full index expansion uses existing infDegree with new finite-support normalization glue.

Completed `Roth.lem6M`: Chosen majorant of determinant coefficient estimate; not Matrix.det_le, whose hypotheses and object differ.

Completed `Roth.lem6Φ`: Existing addition of two supremal values; no standalone universal Roth Phi concept established. Real totalization prohibits silently replacing it by extended-real or product-set suprema.

Completed `Roth.one_mem_RSet`: Elementary unit-degree and coefficient-delta facts exist; exact all-three-condition family membership law not independently verified upstream. No absence claim from unavailable local index.

Completed `Roth.indexSet_nonempty`: Binary-image nonemptiness after accepted180 parent re-aim. Arithmetic complete-family witness is separately project mathematics, not a mathlib building block.

Completed `Roth.indexSet_bddAbove`: Θ_le_card repeats the same mapped-degree/index bound inside a stronger numeric supremum estimate; full target is useful local side-condition API.

Completed `Roth.index_le_Θ`: Dependent law of parent Θ, already exact SupSet.sSup; re-aim gate applies after independent native law/bridge checks.

Completed `Roth.Θ_nonneg`: Existing nonnegative real supremum law specialized to the project family; parent re-aim independently checked.

Completed `Roth.Θ_le_card`: indexSet_bddAbove repeats the same arithmetic pointwise proof but asserts existence of an upper bound; Θ_le_card retains the known bound. Neither is identical to the other, and BddAbove alone cannot supply this cardinality bound.

Completed `Roth.Θ_le_of_forall_index_le`: Structural supremum law shared with Real.sSup_le in Θ_le_card; unlike the preceding substantive bound, the full pointwise arithmetic premise is supplied here.

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

Completed `Roth.box`: Verified classical DecidableEq-free and Finite-only versions; finite-support bounds allow infinite ambient variables; unrestricted constant1 infinite box refuted natively.

Completed `Roth.weight`: Native arbitrary-index finite-support and AddCommMonoid M forms, Finite-only old syntax and arbitrary real denominators verified.

Completed `Roth.mem_box`: Existing generic interval; finite-only and arbitrary finite-support bounds verified after parent reaim.

Completed `Roth.card_box`: Mapped arbitrary dependent finite coordinate sets; support-indexed lower intervals. Already existing APIs. Scoped Classical hides decision instance rather than proving independence.

Completed `Roth.card_le_card_box`: Dependent finite coordinate FUNCTION-family form already composable; arbitrary ambient Finsupp finite-support upper-bound form verified. Support-local hs is equivalent, not strictly weaker.

Completed `Roth.weight_nonneg`: No unused original binder; larger formula and Finsupp representations compiled with ordinary families, finite subsets, nonnegative real denominators, ordered fields, arbitrary ambient variable types and ordered additive monoids. Signed-denominator false generalization rejected.

Completed `Roth.weight_zero`: Existing arbitrary ambient Finsupp.weight in AddCommMonoid and DivisionSemiring finite formula verified; no fixed-parent binder removal.

Completed `Roth.weight_add`: Current parent-interface constraints fixed; verified finite functions in DivisionSemiring and arbitrary semiring-coefficient module-valued Finsupp weights, including infinite ambient types.

Completed `Roth.weight_eq_zero_iff`: Verified support-local positivity; verified generic ordered-additive Finsupp.weight and ordered-field denominator representations.

Completed `Roth.weight_single`: Native finite_kernel permits arbitrary zero-preserving kernels; finite_division permits DivisionSemiring values and arbitrary denominators. Bundled Finsupp.weight drops ambient finiteness and has existing API. These replace the parent representation, not a mechanical weakening of Roth.weight.

Completed `Roth.weight_le_card`: Strictly weaken bounds to nonzero-denominator coordinates; support localization equivalent; support.card stronger conclusion; Finsupp representation drops ambient finiteness; ordered-field finite-function representation compiled.

Completed `Roth.weight_mul_left`: Native arbitrary semiring/module generator scaling without Fintype; arbitrary Field finite-set denominator identity; unchanged Roth interface is maximally general in hypotheses.

Completed `Roth.weight_le_degree_div`: Verified support-local and conditional nonzero-denominator hypotheses; arbitrary ambient index set; ordered Semifield reciprocal-weight comparison. hm cannot be dropped: Unit m0,r1,d1.

Completed `Roth.weight_mapDomain`: Drop hf in unchanged statement; on existing parent Finsupp.weight drop both Fintype instances, permit semiring coefficients and arbitrary module values.

Completed `Roth.wronskianMatrix`: Verified Field→Semiring for standalone same-body definition., Verified arbitrary rectangular row-order matrix specializes by rfl., Verified bundled R-linear operator specializes by rfl and provides map_add.

Completed `Roth.wronskian`: Expanded standalone body CommRing verified; unchanged Field-only matrix parent prevents literal binder-only drop. Arbitrary finite selected orders verified separately.

Completed `Roth.wronskian_eq_zero_of_not_linearIndependent`: Expanded determinant theorem verifies CommRing+NoZeroDivisors including zero ring; fixed public parents still require Field. Generic scalar-linear-family version verifies CommSemiring base, domain CommRing target, AddCommMonoid source, faithful algebra action.

Completed `Roth.det_choose_eq`: Verified exact quotient under local nonzero factorials; stronger arbitrary CommRing identity factorial-product * det(choose) = Vandermonde product, including zero ring. Char2 size2 positive specialization and size3 failure guard compile.

Completed `Roth.coeff_prod_of_natDegree_le'`: Verified same-body Field→CommSemiring, no domain/nontriviality/characteristic/finite-ambient restriction.

Completed `Roth.sum_range_le_sum_of_injective`: Arbitrary finite index type and integer-valued injective family with common lower bound c verified natively; existing finset theorem already covers it. Injectivity is necessary, verified Fin 2 constant-zero counterexample.

Completed `Roth.coeff_wronskian_of_natDegree_injective`: Native verified expanded CommRing identity for arbitrary finite ι and arbitrary r : ι → ℕ; original Field form and sole caller recovered. Does not claim literal Field deletion through project parent interface.

Completed `Roth.wronskian_ne_zero_of_natDegree_injective`: Verified same-parent Field weakening removes global CharZero in favor of cast-degree injectivity. Separately verified expanded CommRing+IsDomain form. No factorial-nonzero premise needed. ZMod2 positive and negative guards; ZxZ zero-divisor guard.

Completed `Roth.wronskian_update_sub_smul`: Raw [CommRing R], arbitrary finite index and selected Hasse orders verified; existing parent interface remains Field-bound.

Completed `Roth.linearIndependent_update_sub_smul`: Ring R; arbitrary AddCommGroup M with Module R M; arbitrary index; arbitrary coefficient function vanishing at source; iff. Already available.

Completed `Roth.sum_natDegree_update_lt`: Compiled Field→DivisionRing, arbitrary Fintype index, replace global LI and distinctness by local nonzero difference or positive common degree.

Completed `Roth.wronskian_ne_zero_of_linearIndependent`: Expanded CommRing+IsDomain+CharZero determinant theorem completely verified by fraction-field descent using explicit Field proof replay. Current Roth.wronskian is Field-bound, so this is a new theorem/interface decision rather than mechanical hypothesis weakening. CharZero drop refuted by compiled independent [1,X²] over ZMod2 with zero determinant.

Completed `Roth.wronskian_eq_zero_iff`: Complete expanded CommRing+IsDomain+CharZero iff compiled using fraction-field hard proof plus generic easy direction, and recovers original Field iff. Changing fixed Field parent interfaces is Class5, not a one-edit weakening. Compiled ZMod2 and CharZero product-ring counterexamples reject dropping CharZero and IsDomain.

Completed `MvPolynomial.taylor`: Already maximally general in this MvPolynomial/AlgHom representation; generic substitutions already aeval. Ring-only AlgEquiv is complementary infrastructure, not weakening.

Completed `MvPolynomial.taylor_apply`: Maximally general relative to the existing CommSemiring/AlgHom parent interface; arbitrary substitution already aeval; no verified strict weakening claimed.

Completed `MvPolynomial.taylor_X`: Maximally general relative to fixed parent interface. Expanded arbitrary-target/assignment representation already exists as aeval_X and is verified; no assumption weakening claimed.

Completed `MvPolynomial.taylor_C`: No same-interface assumption-drop opportunities; already-existing broader representation verified. No unverified weakenings.

Completed `MvPolynomial.taylor_monomial`: Already general over CommSemiring at fixed taylor interface; arbitrary assignment and target commutative algebra form already exists.

Completed `MvPolynomial.coeff_aeval_X_mul`: Already arbitrary variables/commutative semiring, f,B,d; no successful weakening proposed. hB is the coordinate-independence premise used to discard other summands.

Completed `MvPolynomial.hasseCoeff_single_add_eq`: Only variable type and natural exponent data occur in actual native type; zero R/Fintype/DecidableEq assumptions. No unverified weakening of residual-coordinate hypothesis.

Completed `MvPolynomial.prod_pow_single_add_tsub`: Native verified CommSemiring R to CommMonoid M with unchanged proof body; original source remains unchanged in read-only overview.

Completed `MvPolynomial.coeff_taylor_monomial_single_add_aux`: Native type needs no Fintype/DecidableEq/field/charzero/nonzero or npositive hypotheses; no additional weakening or circular use of later coeff_taylor claimed.

Completed `MvPolynomial.coeff_taylor_monomial_aux`: Native type already arbitrary variables/commutative semiring; no leftover k_i=0 or IH in final statement; no circular weakening using later theorem.

Completed `MvPolynomial.coeff_taylor`: Already commutative semiring/arbitrary variable generality; bundled and base-change forms verified derived companions.

Completed `MvPolynomial.eval_taylor`: No removable assumptions in fixed interface; arbitrary R-algebra target checked natively as expanded representation.

Completed `MvPolynomial.taylor_taylor`: Already arbitrary-variable CommSemiring interface; no removable assumptions. Bundled AlgHom composition verified; additive action or ring AlgEquiv is prospective structure, not an existing replacement.

Completed `MvPolynomial.taylor_zero`: Already general within parent CommSemiring interface. Arbitrary-algebra zero-perturbation of any assignment verified separately; no unverified class weakening.

Completed `MvPolynomial.taylor_map`: Maximal within fixed parent CommSemiring interface; arbitrary substitution/variable target is already existing mathlib. Bundled RingHom square verified without adding assumptions; no verified parent weakening.

Completed `MvPolynomial.taylor_rename`: Maximal within parent CommSemiring interface; bundled AlgHom square and arbitrary target-algebra evaluation verified. No mechanical weakening established.

Completed `MvPolynomial.degreeOf_taylor_le`: Maximal within CommSemiring parent interface; CommRing equality via inverse is a separately verified stronger specialization, not assumption weakening.

Completed `MvPolynomial.taylor_neg_taylor`: CommRing is the fixed negation/cancellation interface floor. Conditional mutually cancelling shifts over CommSemiring are an expanded statement, not dropping ring assumptions from unchanged negative-shift law.

Completed `MvPolynomial.taylor_injective`: No verified unchanged-signature mechanical weakening. Conditional semiring inverse-pair injectivity verified. Bare CommSemiring weakening refuted by WithTop Nat shift top colliding X+C1 and X+C2. Cancellative semiring alternatives not tested; no absolute minimality claim.

Completed `MvPolynomial.taylor_eq_zero_iff`: Verified CommRing→CommSemiring same statement and parent with replacement 28-line maximal-support/Hasse argument, not unchanged-body mechanical deletion. All measured consumers checked. Semiring injectivity remains false and is not claimed.

Completed `MvPolynomial.eq_sum_box_hasseDeriv`: Verified no explicit DecidableEq binder using open Classical in statement plus proof-local classical. Old arbitrary instance recovered by Subsingleton.elim and cases; propositional, not definitional transport. Fintype retained for full product and box. Raw arbitrary-variable support expansion is a different representation, not this same statement.

Completed `MvPolynomial.eval_eq_sum_box`: Strongest verified: coefficient CommSemiring A, arbitrary independent-universe CommRing A-algebra B, BOTH α/x : σ→B, aeval α derivative values. No explicit DecidableEq via scoped Classical; original CommRing A=A/arbitrary instance recovered propositionally by Subsingleton.elim/cases. Degree bound after coefficient map proved by support_map_subset; uses hasseDeriv_map and eval₂_eq_eval_map. Fintype, natural exponents and degree bound retained. Earlier center-in-A algebra law is intermediate.

Completed `Roth.normOne`: Verified CommSemiring R + Norm R coefficient sum and integer recovery; arbitrary Zero coefficient / AddCommMonoid value / arbitrary index Finsupp aggregation with exact rfl recovery. Arbitrary Norm data does not imply norm axioms. Universe/lifted-index and existing metric synthesis tested.

Completed `Roth.diag`: Verified CommSemiring R, independent arbitrary variable universe, exact ℤ specialization, empty/lifted variables and arbitrary commutative R-algebra evaluation. Bool/ℤ noninjectivity proved; no degree equality or equivalence claimed.

Completed `Roth.normOne_nonneg`: Fixed parent interface has no removable assumptions. Verified expanded formula to arbitrary Zero coefficients and ordered additive monoid sizes, requiring nonnegativity only on support; norm-coefficient specialization also verified.

Completed `Roth.normOne_eq_sum_of_support_subset`: No removable assumptions at fixed normOne interface. Expanded indexed zero-preserving coefficient size over Zero R/AddCommMonoid S verified; zero premise can be restricted further to added positions; norm-coefficient version verified.

Completed `Roth.normOne_monomial`: Fixed normOne interface has no removable assumptions. Expanded indexed zero-preserving size theorem and arbitrary Finsupp form verified; norm coefficient version verified. Local premise only size e0=0 needed; removing it false for coefficient0.

Completed `Roth.normOne_zero`: Fixed parent interface no assumptions to weaken. Expanded generic Finsupp/polynomial laws verified; sizeZeroUnnecessary guards removal of unnecessary size-zero premise.

Completed `Roth.abs_coeff_le_normOne`: Existing law permits arbitrary index α, Zero M, AddCommMonoid N, PartialOrder N, IsOrderedAddMonoid N, zero-preserving nonnegative g. Fresh lattice-ordered additive-group abs form compiled. New exploratory helper further weakens target order to Preorder/AddLeftMono and nonnegativity to actual support values, verified in isolated native general set; this new proof is not an existing replacement and does not alter original exact-hit verdict.

Completed `Roth.normOne_add_le`: Fresh generic AddZeroClass coefficient/ordered additive Preorder output indexed-size theorem; broader nonnegative-at-zero form also verified, including constant1 support cardinality. No claim of class-minimality.

Completed `Roth.normOne_neg`: Fixed parent interface has no droppable premises. Verified general indexed-size form over SubtractionMonoid coefficients and AddCommMonoid output with hzero and hneg; assumptions sufficient, not claimed minimal.

Completed `Roth.normOne_sum_le`: Fixed normOne interface maximal; expanded generic Finsupp-weight finite bound verified over arbitrary additive commutative coefficient monoid and ordered additive target.

Completed `Roth.normOne_mul_le`: Verified expanded CommSemiring coefficient size with zero/subadditivity/submultiplicativity; parent fixed interface has no droppable hypotheses.

Completed `Roth.normOne_prod_le`: Expanded genericProd verified over CommSemiring with nonnegative coefficient size, size1≤1 and zero/subadditive/submultiplicative laws; abstractProd verified arbitrary CommMonoid.

Completed `Roth.normOne_le_card_mul`: Support-only hB and arbitrary AddCommMonoid/Preorder/AddLeftMono codomain compile; existing mathlib law covers both.

Completed `Roth.normOne_det_le`: Verified arbitrary CommRing R, existing RingSeminorm p with p1≤1, arbitrary Fintype n; exact normOne specialization packaged and compiled.

Completed `Roth.abs_coeff_hasseDeriv_le`: Verified arbitrary CommRing R with AddGroupSeminorm R, followed by exact integer absolute-value specialization.

Completed `Roth.normOne_hasseDeriv_le`: Native-verified arbitrary CommRing R and AddGroupSeminorm R coefficient sum; exact int recovery. MODERN-IDIOM.

Completed `Roth.diag_eq_sum`: Verified CommSemiring R coefficient expansion with aeval; no need finite σ. Current diag remains fixed at ℤ.

Completed `Roth.abs_coeff_diag_le`: Verified CommSemiring coefficients, arbitrary subadditive size map and ordered additive monoid codomain; CommRing AddGroupSeminorm specialization. Stronger support-fiber sum/cardinality and fiber-local hypothesis recover original.

Completed `Roth.natDegree_diag_le`: Expanded statement verified for arbitrary CommSemiring R; totalDegree bound removes Fintype; integer parent interface unchanged.

Completed `Roth.eval_diag`: Compiled arbitrary CommSemiring R,S with f:R→+*S and Algebra aeval forms. Parent diag remains ℤ-specific.

Completed `Roth.diag_sub`: Expanded arbitrary CommRing diagonal and arbitrary algebra substitution compile; generic AddGroupHom law also compiles.

Completed `Roth.geom_sum_le_one_add_pow`: Verified noncommutative ordered semiring; no CharZero, no linear order; ht essential (t=-1,r=2).

Completed `Roth.sum_box_prod_pow_le_aux`: Finite variable enumeration, natural coordinate bounds, nonnegative real B and arbitrary real coordinates are explicit. No assumption weakening or broader public contribution is claimed under private triage.

Completed `Roth.abs_eval_le`: Verified strongest primary form: arbitrary CommSemiring R coefficients, CommSemiring S evaluation, ordered CommSemiring T output with PartialOrder and IsOrderedRing, FunLike F S T and existing Zero/Nonneg/Subadditive/Submultiplicative hom classes. Original ℤ/ℝ map input and full private caller specialize cleanly. No unit-size bound, injectivity, domain, total order, strict order or negation premise.

Completed `Roth.degreeOf_det_hasseDeriv_le`: CommRing coefficients, arbitrary finite matrix index, fixed-coordinate scalar bound verified. Factor generic entry/column determinant bounds.

Completed `Roth.abs_coeff_det_hasseDeriv_le`: Verified RingSeminorm over arbitrary CommRing, normalized at1, arbitrary finite matrix index; omit hB0.

Completed `Roth.genWronskian`: Native verified CommRing R and arbitrary finite square index; original specialization rfl. Variables already arbitrary. Semiring-N signed determinant guard rejects further weakening.

Completed `Roth.kronecker`: CommSemiring coefficients and arbitrary explicit ranks/weights verified; existing aeval is already more general. Hidden enumeration is noncanonical and changes the substitution.

Completed `Roth.kroneckerExp`: Existing arbitrary-index weight removes Fintype only when explicit weights replace chosen equivFin; generic semiring coefficients/module target compiled. Original chosen positional interface retains Fintype; coefficient Field is already absent.

Completed `Roth.kronHasse`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.kronSpan`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.genWronskian_eq_zero_of_not_linearIndependent`: Verified arbitrary finite index, CommRing+NoZeroDivisors polynomial coefficients; semiring base/module source abstract operator family with domain target/faithful scalar action. Plain ring false via ℤ×ℤ singleton.

Completed `Roth.kronecker_monomial`: Compiled arbitrary-σ CommSemiring weighted theorem and arbitrary commutative target algebra evaluation; fixed geometric enumeration remains a project representation choice.

Completed `Roth.kroneckerExp_injOn`: Checked explicit e:σ≃Fin n with proof-local Fintype and arbitrary k (no hk). Fixed original-interface no-hk bridge checked. Infinite-position injective maps and mixed radix considered but not claimed compiled.

Completed `Roth.coeff_kronecker`: Verified arbitrary sigma, CommSemiring, arbitrary weights with support-local InjOn; explicit finite enumeration and no hk positional specialization also checked.

Completed `Roth.kronecker_eq_zero_iff`: Verified CommSemiring, arbitrary σ and weights with support separation; positional explicit e and no hk; literal parents retain Field/Fintype constraints.

Completed `Roth.linearIndependent_kronecker`: Verified CommSemiring, arbitrary family index, arbitrary weighted variable set; explicit finite enumeration and no k>1 for positional theorem.

Completed `Roth.derivative_aeval`: Verified Field→CommSemiring; arbitrary algebra/module-valued derivation; arbitrary-variable finite-support sum over P.vars.

Completed `Roth.derivative_kronHasse_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.derivative_mem_kronSpan`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.hasseDeriv_kronecker_mem`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_hasseDeriv_kronecker_eq_sum`: Verified arbitrary γ : σ → Polynomial R, CommSemiring R + Algebra ℚ R, Finite σ. Original specialization and actual sole caller compile. Characteristic-independent primary literature formula not claimed compiled.

Completed `Roth.det_sum_rows`: Verified arbitrary finite square J and dependent I:J→Type*, original Fin l recovery. Abstract CommSemiring module-valued weighted expansion verified separately; determinant itself still requires CommRing.

Completed `Roth.wronskian_kronecker_eq_sum_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_genWronskian_ne_zero`: Verified deletion of Finite σ, using finite union of vars, LI.of_comp, derivative rename, degree_mapDomain and determinant rename. Direct one-edit replay fails at Fintype.ofFinite. Domain/fraction-field and formal-series extensions remain distinct unverified proposals.

Completed `Roth.sqrt_one_sub_inv_lt`: Verified candidate: real m≥1, nonstrict 2√m≤lam, still strict conclusion. Does not claim optimal hypotheses.

Completed `Roth.inv_add_inv_le`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.sum_inv_le`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.sum_inv_lt`: Verified real m>1 and weak2√m≤lam preserve strict conclusion; both private pair/grid proofs work for1<lam. Independent raw proof and sole caller replay clean.

Completed `Roth.extend_apply_castSucc`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.extend_apply_last`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.card_filter_box_fiber_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.card_filter_box_last`: Native generic finite α/β fibre map, arbitrary filtered product, dependent finite tuple sections and scoped classical predicate-decision removal. Independent tuple theorem does not claim complete recovery of original spelling.

Completed `Roth.filter_weight_le_eq_empty`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.card_filter_fiber_eq`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.card_filter_weight_le_of_le_sqrt_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.card_filter_weight_le_succ_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.card_filter_weight_le`: Arbitrary universe-polymorphic Fintype index transport actually compiled; expanded piFinset ordinary-sum form with DecidableEq and original Fin/Finsupp recovery compiled. These are new project-dependent proofs; no droppable original premise found.

Completed `Roth.index`: Verified arbitrary variable types, CommSemiring coefficient type, arbitrary real weights via finite support; Fintype dependence belongs only to the current weight interface.

Completed `Roth.mem_support_taylor_iff`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.index_le_weight`: Compiled abstract Semiring/any support-degree map/any SemilatticeInf OrderTop target, and translated CommSemiring arbitrary-variable arbitrary-real-degree version without Fintype.

Completed `Roth.exists_weight_eq_index`: Verified Semiring coefficients, arbitrary ambient support type with no Fintype, arbitrary degree map into any LinearOrder/OrderTop target with independent universes; separately verified real default-zero projection.

Completed `Roth.le_index_iff`: Verified arbitrary Semiring coefficients, arbitrary degree map and ambient support index type, arbitrary SemilatticeInf+OrderTop codomain; no nonzero hypothesis in unprojected law.

Completed `Roth.index_nonneg`: Verified Semiring coefficient carrier with arbitrary support index type, arbitrary degree map to SemilatticeInf+OrderTop and arbitrary lower bound c. Projected real nonnegative law verified for all P with support-local nonnegative D.

Completed `Roth.index_eq_zero_iff`: Expanded arbitrary Semiring coefficients/support carrier/distinguished exponent/bounded linear target; degree bottom iff distinguished exponent. Real degrees need nonnegativity and zero-fiber control; no unchanged-parent mechanical drop.

Completed `Roth.index_sub_weight_le_index_hasseDeriv`: Verified standalone projectedInfDegreeShift and expandedProjectedShift over arbitrary sigma, CommRing R, real degree D with D(i+k)=D(i)+D(k). supportShift separately CommSemiring. Parent fixed-interface restrictions are not claimed mechanically deleted. Infinity-preserving and general ordered-target variants remain optional unverified extensions.

Completed `Roth.le_index_sum`: Verified Semiring R, arbitrary support A, degree D:A→T and SemilatticeInf/OrderTop target, no finiteness on A or sum-nonzero premise in top-valued law. Point aeval projected form verified over CommRing and arbitrary sigma. Fixed parent restrictions are not silently deleted. Zero-default real projection retains sum nonzero; X+(-X) guard confirms cancellation necessity.

Completed `Roth.weight_eq_finsuppWeight_div`: Arbitrary Semifield K; nonzero cast common denominator and divisibility only on d.support; no ambient Fintype or CharZero needed in strongest accepted form. Generic parent law has arbitrary semiring coefficients and module targets.

Completed `Roth.index_eq_weightedOrder_div`: named weakening: delete hP, independently compiled zero case; expanded representation: CommSemiring/arbitraryσ/allP/assigned naturalw weightedOrder_coe, verified mathlib-only; projection scaling: scaledInfDegree real D≥0 including0/allP, verified; rejected: uniform hr removal false; arbitrary real w not same natural weightedOrder; negative real scaling not min-preserving

Completed `Roth.index_mul`: Verified exact-interface deletion of hr. Expanded natural-series law removes Fintype, ℝ, Taylor center, positivity and factor nonvanishing via infinity at zero; compiled. Broader arbitrary-real polynomial infDegree multiplication is a design proposal, not a compiled weakening.

Completed `Roth.index_prod`: Verified deletion of hr while preserving the exact conclusion. Natural-series and polynomial formulations remove finite-variable and real-coefficient restrictions, using infinity at zero. Arbitrary-real ordered polynomial extension is a proposal only.

Completed `Roth.index_neg`: Verified expanded representation arbitrary Ring coefficients, exponent type and degree map into semilatticeinf/top. No claim Fintype can drop from unchanged parent signature.

Completed `Roth.index_C_mul`: Verified arbitrary exponent/degree semilatticeinf/top and coefficient semiring acted on by scalar domain with torsion-free module. This library interface is not logical minimum; zero-preserving injective coefficient maps have existing support_mapRange_of_injective; unit/regular scalar extension not claimed compiled.

Completed `Roth.index_mul_left_weights`: No mechanically droppable hypotheses in fixed Roth interface. Verified expanded law for arbitrary semiring coefficients/A/degree targets and zero-preserving monotone maps; scalar specialization arbitrary ordered semiring and c≥0. Fintype/ℝ changes require parent restatement.

Completed `Roth.index_rename`: Verified expanded law has arbitrary variable types without Fintype, CommSemiring coefficients, additive direct weights into SemilatticeInf AddCommMonoid, WithTop and untopD0. Fixed original parent cannot simply drop its Fintype binders. hf remains essential, verified collision guard.

Completed `Roth.index_le_card`: Verified noNonzero drops hP; oneWitness weakens entire degree box to one nonzero Taylor coefficient in box; weightedWitness accepts arbitrary coefficient weight bound. Mathlib-only realSupport handles arbitrary finite exponent set; infDegreeWitness arbitrary semiring coefficients and grading/order target. Fixed parent interface remains real/Fintype.

Completed `Roth.index_unique`: verified drop: P ≠ 0; finite data: Unique.fintype supplies the Fintype interface; choice independence checked; expanded: Univariate Taylor coefficient minimum over arbitrary CommRing R, real numerical codomain and natural denominators; independently compiled; rejected: Signed scaling without nonnegativity, Unprojected infinite zero order identified with real zero, Arbitrary many-to-one variable collapse

Completed `Roth.coeffNone`: fixed interface: Already arbitrary CommSemiring and variable universes; no finite/equality classes. MvPolynomial carrier requires CommSemiring.; expanded representation: STRICTLY NARROWER representation level: existing Finsupp.comapDomain slices coefficients over Zero; actual native direct_coeff bridge proved. Fixed MvPolynomial carrier requires CommSemiring. Initial sum-filter remains exploratory.

Completed `Roth.eq_mapDomain_some_add_single`: status: STRICTLY NARROWER THAN STANDARD; fixed surface: AddCommMonoid M (mapDomain interface); embedding surface: AddZeroClass M; canonical surface: Zero M; native verified: True

Completed `Roth.coeff_X_none_pow_mul_rename`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.coeff_coeffNone`: status: MAXIMALLY GENERAL for fixed parent interface; canonical surface: CommSemiring R; arbitrary variable type and independent universes; expanded representation: Zero A suffices for underlying coefficient slicing by Finsupp.comapDomain; prior152 actual slice_apply and direct_coeff bridge reused with freshly matching17source/pin hashes. This is a wider representation, not a mechanical weakening of the fixed coeffNone interface.

Completed `Roth.eq_sum_X_none_pow_mul_coeffNone`: status: MAXIMALLY GENERAL for fixed parent interface; canonical surface: Existing finite Polynomial expansion over Semiring A with natDegree p < m.; expanded representation: Generic Semiring A reconstruction actually compiled. Setting A=MvPolynomial τ R gives canonical Option expansion; does not weaken CommSemiring required by fixed parent.

Completed `Roth.degreeOf_coeffNone_le`: status: MAXIMALLY GENERAL for fixed interface; canonical surface: degreeOf j ((optionEquivLeft R τ P).coeff ν) ≤ degreeOf (some j) P; abstract component: Finset support transport with pointwise weight bound implies supremum bound; independently compiled without DecidableEq or coefficient algebra. This is an expanded representation, not weakening CommSemiring in the original.

Completed `Roth.coeff_rename_mul_aeval`: status: MAXIMALLY GENERAL for fixed polynomial representation; verified: Underlying coefficient-times-singleton law holds for arbitrary Semiring S and AddZeroClass M, not just natural multidegrees.; boundary: CommSemiring R is required by existing MvPolynomial interface; abstract AddMonoidAlgebra restatement changes representation. Variable-disjointness cannot be removed, as collision_guard proves.

Completed `Roth.aeval_X_eq_rename`: fixed interface: MAXIMALLY GENERAL; verified weakenings: None; representation extension: Arbitrary Unique index verified by a new hom-ext proof; not counted as existing-call API.; modern idiom: Existing bundled equality already supplies canonical abstract form.; false generalization: Arbitrary replacement of X_i while keeping the chosen-coordinate rename is false; concrete coefficient guard verified.

Completed `Roth.hasseDeriv_rename_mul_aeval`: status: STRICTLY NARROWER representation interface; verified: HasseSeparation160.freshCoordinate; statement: Replace some : τ → Option τ and none by an arbitrary injective f : τ → σ and fresh i : σ satisfying ∀ j, f j ≠ i; no surjectivity/exhaustiveness required.; fixed interface: Original already uses weakest parent interface CommSemiring and arbitrary τ; no typeclass drop claimed.; original specialization: HasseSeparation160.originalFormAgain

Completed `Roth.coeff_uniqueAlgEquiv_symm`: status: More general exponent form already in mathlib; fixed parent interface maximally general; verified: arbitrary finitely supported exponent d, arbitrary coordinate j in Unique σ, representation d=single default (d default); rejected: Semiring alone cannot instantiate the fixed uniqueAlgEquiv algebra interface, Bool variable set lacks Unique; coordinate forgetting does not preserve coefficients

Completed `Roth.degreeOf_uniqueAlgEquiv_symm`: Already maximal for fixed CommSemiring/Unique interface; arbitrary coordinate is checked equivalent restatement. Arbitrary selected-variable general law is already in mathlib; Semiring interface drop and Bool uniqueness drop rejected.

Completed `Roth.degreeOf_rename_mul_aeval`: CommSemiring R + NoZeroDivisors R complete proof compiled; arbitrary-degree-zero-factor principle compiled separately; hV and nonannihilation guards compiled. NoZeroDivisors is a sufficient global condition; weakest point-local nonannihilation alternatives are not claimed.

Completed `Roth.degreeOf_none_rename_mul_aeval`: CommSemiring+NoZeroDivisors verified; arbitrary CommSemiring point-local V=0 or U*(V.map C).leadingCoeff≠0 verified. U-nonzero and zero-divisor counterexamples compiled.

Completed `Roth.linearIndependent_coordinate_polynomials_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.eq_sum_aeval_basis_coeffNone_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_coeffNone_basis_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_separated_representation`: status: verified sufficient scalar weakening; from: Field K; to: CommRing K + IsDomain K + IsPrincipalIdealRing K; preserved: arbitrary τ, hP nonzero, chosen n and hn, 1 ≤ l ≤ n+1, LinearIndependent K φ, LinearIndependent K ψ, all φ natDegree bounds, all ψ coordinate degree bounds, separated reconstruction; not claimed: PID is not claimed the weakest possible scalar condition; given-basis variant is conditional.; primary evidence: separated-repr-isolated-pid-executed.lean.txt / separated-repr-isolated-pid-receipt.json

Completed `Roth.det_hasseDeriv_separated`: Clean native full expanded CommRing law; arbitrary finite square indexι and arbitrary univariate ordersE; injected f:τ→σ plus fresh coordinatei outside its range. Original named full conclusion and sole full caller compile via both ring bridge and strongest fresh-coordinate bridge. Original named Field parents cannot mechanically lower unchanged.

Completed `Roth.exists_sum_mul_eq_gcd`: status: STRICTLY NARROWER THAN STANDARD; verified: CommRing R + IsBezout R + NormalizedGCDMonoid R; independently compiled; abstract ideal form: Ideal.mem_span_range_iff_exists_fun under Semiring R and Fintype ι is also existing; not claimed identical gcd theorem without Bezout.

Completed `Roth.exists_nat_smul_eq_map`: status: Verified broader existing interfaces; polynomial: CommRing R/S + Algebra R S + IsLocalization M S; clear denominator in M.map C.; finite family: CommSemiring A/B + localization; finite coefficient family common denominator.; fixed interface: Exact positive-natural rational/integer specialization retained.

Completed `Roth.exists_primitive_smul_eq`: current: Fixed ℤ/ℚ interface; all variable-type and nonzero assumptions essential or already unrestricted.; expanded: CommRing R + IsDomain R + NormalizedGCDMonoid R, Field K + Algebra R K + IsFractionRing R K, preserving g ≠ 0, map(algebraMap R K) U = g • G, gcd1.; scope: Full normalized-GCD-domain/fraction-field theorem native-checked, preserves every conclusion, no parent-definition migration. Concrete one-call specialization checked separately.; false generalization guard: gcd1 does not imply unit-ideal/unimodular coordinates over arbitrary GCD domains. No arbitrary field unrelated to R, no zero input, no infinite series.

Completed `Roth.exists_int_eq_of_gcd_eq_one`: reason: MODERN-IDIOM; primary: Submodule.gcd_smul_mem; signature: {R M ι : Type*} [CommRing R] [IsBezout R] [NormalizedGCDMonoid R] [AddCommMonoid M] [Module R M] (N : Submodule R M) (s : Finset ι) (u : ι → R) (v : M) (hv : ∀ i ∈ s, u i • v ∈ N) : s.gcd u • v ∈ N; secondary: IsUnit (s.gcd u) implies unscaled membership via existing smul_mem_iff_of_isUnit; original bridge: N = LinearMap.range (Algebra.linearMap ℤ ℚ); convert product witnesses; rewrite gcd=1; return integer witness with equality symmetry; guard: Arbitrary GCD rings need not be Bezout; no claim that gcd1 implies unit ideal without Bezout.

Completed `Roth.rescale_separated_factor_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_int_polynomial_of_primitive_factor_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_int_factors`: status: Verified full GCD-domain/fraction-field proof, exact concrete specialization and entire sole caller.; signature: variable {τ R K : Type*} [CommRing R] [IsDomain R] [NormalizedGCDMonoid R]
    [Field K] [Algebra R K] [IsFractionRing R K]
theorem exists_separated_factors {U' : MvPolynomial τ K} {V' : Polynomial K} (hU : U' ≠ 0) (hV : V' ≠ 0)
    {F : MvPolynomial (Option τ) R} (hF : map (algebraMap R K) F =
      rename some U' * Polynomial.aeval (X none : MvPolynomial (Option τ) K) V') :
    ∃ (U : MvPolynomial τ R) (V : Polynomial R), U ≠ 0 ∧ V ≠ 0 ∧
      F = rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V ∧
      (∀ j, degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree; no IsBezout: True; no UFD: True; all conclusions preserved: True

Completed `Roth.exists_rat_factors_det_hasseDeriv_aux`: No public generality claim under the private prefilter; preserve the existing definition and interface.

Completed `Roth.exists_det_eq_mul`: verified: True; coefficient ring: [CommRing R] [IsDomain R] [NormalizedGCDMonoid R] [CharZero R]; variables: arbitrary τ; remove Finite τ by finite-support bridge; fraction field: FractionRing R internal; arbitrary external K variant also proved; preserved: 1 ≤ l, l ≤ r none + 1, ∀ μ, (D μ).degree ≤ μ, U ≠ 0, V ≠ 0, ∀ j, degreeOf j U ≤ l * r (some j), V.natDegree ≤ l * r none, exact determinant factorization; parent interface: Field-only genWronskian remains over fraction field; base-ring Hasse API already valid.

Completed `Roth.RSet`: status: already broad variable/bound parameters; no mechanically droppable instance; verified: Generic degree/support bridge over arbitrary σ and CommSemiring; not a generic arithmetic development.; rejected: Do not replace by total degree, projective height, submodule including zero, or finite box without extra assumptions.

Completed `Roth.indexSet`: status: No mechanically removable class while keeping parent index signature. Existing image2 abstracts independent source/target types and universes. Expanded index representation supports arbitraryσ; finite specialization checked.; rejected: Do not omit nonzero/degree/coefficient/coprimality restrictions, impose positive q in all-input comparison, change default0 to infinity, or replace by submodule/total degree.

Completed `Roth.Θ`: status: No mechanically removable parameter within fixed indexSet interface. Generic outer SupSet already maximally abstract; expanded arbitrary-variable expression without Fintype and its finite specialization actually compile.; rejected: Do not alter full RSet/nonzero/degree/coefficient constraints, coprimality, total q/r zeros, or empty/unbounded real default0; do not apply CompleteLattice-only image2 supremum laws to ℝ.

Completed `Roth.lem6M`: Semiring expression compiles; representation expansion only, not literature-standard replacement or suggested new upstream definition.

Completed `Roth.lem6Φ`: Generic SupSet+Add formula compiled; arbitrary-variable expanded representation compiled. Fintype belongs to fixed Θ parent interface; no new generalization ticket needed for existing outer operations.

Completed `Roth.one_mem_RSet`: Already arbitrary σ and r under fixed RSet. Expanded normalized normed-ring form compiles and specializes back to ℤ via Int.norm_eq_abs; changing fixed RSet is a separate API project.

Completed `Roth.indexSet_nonempty`: Abstract law accepts arbitrary types/sets/total binary maps without Fintype, arithmetic, order or topology. Original hB is sharp: actual indexSet.Nonempty↔1≤B checked via nonzero integer coefficient.

Completed `Roth.indexSet_bddAbove`: No mechanical deletion of target assumptions verified or claimed. Generic structural law works at LE and arbitrary domains; it retains the substantive uniform-bound premise. Parent infDegree/Finsupp.weight representation does not settle full Taylor-degree/cardinality bound.

Completed `Roth.index_le_Θ`: Fixed polynomial interface needs Fintype; expanded generic conditionally complete lattice member law is already le_csSup, verified without Roth imports. Verified expanded allow_zero removes the hidden R≠0 conjunct, handling zero via index0=0 and independent Θ_nonneg; this separate real-default extension does not alter original member-law duplication.

Completed `Roth.Θ_nonneg`: unchanged parent: No extra premise to drop; Fintype fixed by current index interface.; expanded: Arbitrary Set ℝ or arbitrary real two-argument family with pointwise nonnegativity; already existing law.; guard: Negative singleton rules out deleting the nonnegative-value premise; preserve real default0.

Completed `Roth.Θ_le_card`: Verified expanded_family handles arbitrary sets of real multivariate polynomials (including zero) and arbitrary real evaluation points, with only coordinate degree bounds. This changes the parent family/interface; it is not deletion of a hypothesis from the existing Θ statement. Generic supremum law already exists.

Completed `Roth.Θ_le_of_forall_index_le`: Abstract csSup_le handles arbitrary conditionally complete lattices and arbitrary nonempty sets. Fixed Θ/index interface retains Fintype. Replacing hB by 0≤c is verified using Real.sSup_le, and under hc, Θ≤c iff0≤c; no unconditional premise deletion claimed. Actual compiled Roth counterexample at B=0,c=-1 supplies hc vacuously but Θ=0 fails≤-1, so unconditional hB deletion is false; family-only emptiness legitimately omits Fintype.

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

Completed `Roth.box`: None for constructing box; interval sum/product bridge a separate optional API question.

Completed `Roth.weight`: No missing API for definition; assess re-aimed dependent order/index lemmas separately.

Completed `Roth.mem_box`: None established.

Completed `Roth.card_box`: None

Completed `Roth.card_le_card_box`: No categorical missing-API claim. Design question: whether useful Finsupp natural-endpoint/support interval convenience bounds deserve upstream names.

Completed `Roth.weight_nonneg`: No necessary gap: generic sum/scalar positivity composes. A standalone Finsupp.weight_nonneg convenience name not found; no absence claim.

Completed `Roth.weight_zero`: No required missing upstream zero-preservation fact.

Completed `Roth.weight_add`: No new missing mathlib theorem identified; existing Finsupp.weight/map_add cover abstract content.

Completed `Roth.weight_eq_zero_iff`: Candidate positive-weight zero-fiber theorem without canonical-order assumption; design unresolved, absence not proven.

Completed `Roth.weight_single`: No demonstrated missing singleton-evaluation mathematics; design issue is whether to expose finite cast/division convenience API or migrate parent weight to bundled support sums.

Completed `Roth.weight_le_card`: Potential ordered Finsupp.weight upper bound by support.card • b; API design question, not established absence.

Completed `Roth.weight_mul_left`: No mathematical API gap established; dedicated weight_smul spelling would wrap bundled linearity.

Completed `Roth.weight_le_degree_div`: Potential support-local weight monotonicity or constant/degree upper bound; design choice, not an existing verified law.

Completed `Roth.weight_mapDomain`: None

Completed `Roth.wronskianMatrix`: Coherent named n-ary normalized Wronskian API; existing pinned TODO. No absolute absence theorem claimed.

Completed `Roth.wronskian`: Coherent normalized n-ary Wronskian name/compatibility/scaling API subject to upstream design.

Completed `Roth.wronskian_eq_zero_of_not_linearIndependent`: Design-dependent packaging of finite Hasse alternating map or generic operator-family determinant law; abstract vanishing law already exists.

Completed `Roth.det_choose_eq`: Public characteristic-aware binomial evaluation determinant API; Pochhammer monicity/degree can be transferred from ℤ to remove pinned NoZeroDivisors assumptions.

Completed `Roth.coeff_prod_of_natDegree_le'`: Potential varying-bound public coefficient generalization; full public contribution verdict n/a under private prefilter.

Completed `Roth.sum_range_le_sum_of_injective`: None

Completed `Roth.coeff_wronskian_of_natDegree_injective`: Coefficient of determinant of arbitrary finite Hasse derivative matrix at sum degrees minus sum orders; varying-bound coefficient-product helper supports its proof.

Completed `Roth.wronskian_ne_zero_of_natDegree_injective`: N-ary Hasse Wronskian top-coefficient/nonvanishing API, supported by cancellation-free binomial determinant identity.

Completed `Roth.wronskian_update_sub_smul`: Conditional on parent acceptance: finite-family Hasse-Wronskian alternating-map interface or family-to-matrix update compatibility. No missing generic determinant column law.

Completed `Roth.linearIndependent_update_sub_smul`: No mathematical gap; generic update spelling is optional convenience.

Completed `Roth.sum_natDegree_update_lt`: Potential normalized quotient cancellation corollary and relation to cancelLeads; generic finite-update wrapper is optional design question.

Completed `Roth.wronskian_ne_zero_of_linearIndependent`: N-ary polynomial Hasse Wronskian criterion, coherent binary/n-ary naming bridge, potentially reusable polynomial echelon basis.

Completed `Roth.wronskian_eq_zero_iff`: N-ary Hasse Wronskian foundation and criterion, coherent binary/n-ary naming and finite column reindexing.

Completed `MvPolynomial.taylor`: Design question: stable named multivariate translation with Hasse coefficient, composition and inverse APIs.

Completed `MvPolynomial.taylor_apply`: No mathematical normalization API needed for this constitutive equation. Optional stable unfold theorem may accompany a future upstream translation bundle.

Completed `MvPolynomial.taylor_X`: No mathematical gap for this law. A future translation bundle may independently choose its own stable generator simp interface.

Completed `MvPolynomial.taylor_C`: None

Completed `MvPolynomial.taylor_monomial`: None

Completed `MvPolynomial.coeff_aeval_X_mul`: No missing primitive blocks existing proof; public extraction API suitability is unassessed under private prefilter.

Completed `MvPolynomial.hasseCoeff_single_add_eq`: Existing product/erase/support primitives suffice; full public upstream assessment n/a under private rule.

Completed `MvPolynomial.prod_pow_single_add_tsub`: No missing primitive blocks proof. Potential generic monomial-evaluation formulation is a future public assessment, not claimed completed.

Completed `MvPolynomial.coeff_taylor_monomial_single_add_aux`: No missing primitive blocks current decomposition; prospective public multivariate Hasse/Taylor API assessed separately.

Completed `MvPolynomial.coeff_taylor_monomial_aux`: No missing primitive blocks exponent induction; prospective public Hasse/Taylor API separately assessed at next declaration.

Completed `MvPolynomial.coeff_taylor`: Coefficient normalization of multivariate substitution X+Cα against binomial Hasse derivative.

Completed `MvPolynomial.eval_taylor`: Translation-specific convenience API is an upstream design question; no missing generic engine established.

Completed `MvPolynomial.taylor_taylor`: Design question: package translation composition as named law or structural action API; no missing generic composition engine.

Completed `MvPolynomial.taylor_zero`: No mathematical API gap; parent translation naming/simp design independently assessed.

Completed `MvPolynomial.taylor_map`: Design choice whether a named multivariate translation API merits coefficient-map convenience law; no generic substitution gap.

Completed `MvPolynomial.taylor_rename`: No generic substitution gap; decision whether named multivariate translation API merits explicit rename convenience law.

Completed `MvPolynomial.degreeOf_taylor_le`: Coordinate-degree control under multivariate constant-shift substitution, with arbitrary variable type and commutative-semiring coefficients.

Completed `MvPolynomial.taylor_neg_taylor`: Potential bundled multivariate translation algebra equivalence; its inverse fields are new obligations, not a missing generic equivalence theorem.

Completed `MvPolynomial.taylor_injective`: Potential multivariate translation AlgEquiv; no missing generic left-inverse theorem.

Completed `MvPolynomial.taylor_eq_zero_iff`: Multivariate semiring translation zero-reflection and reusable maximal-support Hasse constant lemma.

Completed `MvPolynomial.eq_sum_box_hasseDeriv`: Multivariate Hasse/Taylor coefficient-to-finite-box reconstruction; optional support-indexed intermediate using generic evaluation sums.

Completed `MvPolynomial.eval_eq_sum_box`: Multivariate Hasse finite Taylor evaluated expansion and foundational coefficient/polynomial reconstruction; existing generic homomorphism transport should be reused.

Completed `Roth.normOne`: No missing scalar construction established; general coefficient L1/convolution normed structure and substantive bounds are separate potential contributions. Pinned Polynomial.Norm explicitly lists other Lp norms as TODO.

Completed `Roth.diag`: No missing scalar construction, hom bundle or evaluation-composition API established. Specialized coefficient/degree bounds remain separate assessment candidates.

Completed `Roth.normOne_nonneg`: None established for nonnegativity; full bundled coefficient/convolution norm structure is separate from this law.

Completed `Roth.normOne_eq_sum_of_support_subset`: None needed for support padding. No global coefficient norm instance proposed.

Completed `Roth.normOne_monomial`: None needed. No new coefficient norm instance recommended.

Completed `Roth.normOne_zero`: None. No proposed new global polynomial norm instance.

Completed `Roth.abs_coeff_le_normOne`: No missing API for this declaration. Optional separate generalization of existing single_eval_le_sum to Preorder/AddLeftMono/support-local nonnegativity now has a proof witness; no absence/novelty claim or new upstream verdict for that separate API.

Completed `Roth.normOne_add_le`: Design candidate: generic Finsupp support-sum subadditivity versus compatible L1 normed-group or translation-distance API. Searches establish candidates, not formal absence.

Completed `Roth.normOne_neg`: None required for the verified replacement; new assessment generic helper is not counted as existing mathlib.

Completed `Roth.normOne_sum_le`: Potential generic Finsupp sum subadditivity/coefficient-size bridge; existing finite induction itself has no gap.

Completed `Roth.normOne_mul_le`: Candidate shared coefficient-size convolution/RingSeminorm API; broad AddMonoidAlgebra endpoint is a future design question.

Completed `Roth.normOne_prod_le`: Substantive coefficient-size binary convolution/representation bridge, not finite-product induction.

Completed `Roth.normOne_le_card_mul`: No missing API required for this bound; broader coefficient norm representation issues do not obstruct this theorem.

Completed `Roth.normOne_det_le`: RingSeminorm determinant factorial bound beyond multiplicative AbsoluteValue.map_prod.

Completed `Roth.abs_coeff_hasseDeriv_le`: Quantitative coefficient bounds for multivariate Hasse derivatives, atop the proposed multivariate Hasse algebraic API.

Completed `Roth.normOne_hasseDeriv_le`: Multivariate Hasse derivative foundation and coefficient seminorm finite-support sum bound. State explicit coefficient sums, avoiding a new coefficient norm foundation.

Completed `Roth.diag_eq_sum`: Optional named constant-X evaluation expansion, contingent on upstream API design; no mathematical proof infrastructure gap.

Completed `Roth.abs_coeff_diag_le`: Optional coefficient formula for constant-X substitution, followed by a design choice about exposing a generic estimate. No missing finite-sum inequality infrastructure.

Completed `Roth.natDegree_diag_le`: Potential named coordinate-to-totalDegree inequality / bounded variant, pending upstream API choice; search failure not an absence proof.

Completed `Roth.eval_diag`: None established; no new normalization helper needed.

Completed `Roth.diag_sub`: None needed for subtraction preservation.

Completed `Roth.geom_sum_le_one_add_pow`: Finite geometric/binomial unweighted comparison without t<1 restriction.

Completed `Roth.sum_box_prod_pow_le_aux`: Existing finite-product, finite-sum and order primitives support the decomposition; prospective public geometric bound is independently assessed at96.

Completed `Roth.abs_eval_le`: Nonhomogeneous rectangular coordinate-degree polynomial evaluation majorant; generic geometric-sum bound from declaration96 is a separate new prerequisite.

Completed `Roth.degreeOf_det_hasseDeriv_le`: MvPolynomial coordinate degree bound on arbitrary polynomial matrix determinants; Hasse corollary after upstream multivariate Hasse API.

Completed `Roth.abs_coeff_det_hasseDeriv_le`: Coefficient l1 size API for multivariate polynomials, its Hasse estimate, and normalized RingSeminorm determinant estimate. Pinned Polynomial/Norm TODO documents missing lp norm API.

Completed `Roth.genWronskian`: Named finite-family multivariate Hasse Wronskian; upstream multivariate Hasse prerequisite. Existing pairwise Polynomial Wronskian file has n-tuple TODO.

Completed `Roth.kronecker`: No missing API for the definition itself; bounded encoding/injectivity and derivative results assessed separately.

Completed `Roth.kroneckerExp`: None for this definition. Radix injectivity and substitution coefficient/derivative laws require their own assessment; arbitrary weights do not inherit injectivity.

Completed `Roth.kronHasse`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.kronSpan`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.genWronskian_eq_zero_of_not_linearIndependent`: Design choice: shared scalar-linear determinant family lemma versus alternating generalized-Wronskian representation.

Completed `Roth.kronecker_monomial`: No missing evaluation infrastructure established; new weighted helper probe is not counted as an existing mathlib theorem.

Completed `Roth.kroneckerExp_injOn`: Public Finsupp geometric-weight injectivity on bounded digits; concrete recurring list conversion in Roth and pinned NoetherNormalization private helper.

Completed `Roth.coeff_kronecker`: Candidate normalization between aeval monomial powers and mapDomainAlgHom(weight); decide whether to expose extraction corollary.

Completed `Roth.kronecker_eq_zero_iff`: Weighted monomial-evaluation coefficient/mapDomain bridge; packaging of restricted aeval injection versus zero corollary remains API choice.

Completed `Roth.linearIndependent_kronecker`: aeval(X^w) coefficient mapDomain bridge and support-restricted injection; packaging inherited questions from109–110, independently evaluated for111. No missing generic linear-independence transport.

Completed `Roth.derivative_aeval`: Module-valued MvPolynomial evaluation chain rule expressed with pderiv, complementing Derivation.map_aeval.

Completed `Roth.derivative_kronHasse_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.derivative_mem_kronSpan`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.hasseDeriv_kronecker_mem`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_hasseDeriv_kronecker_eq_sum`: Higher polynomial-substitution law for multivariate Hasse derivatives, with choice of filtered-span, finitely supported coefficients or explicit Taylor formula.

Completed `Roth.det_sum_rows`: Possible named weighted multilinear finite-sum convenience law or determinant-specific row-expansion corollary, not a claimed missing mathematical theorem.

Completed `Roth.wronskian_kronecker_eq_sum_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_genWronskian_ne_zero`: Bounded generalized Hasse-Wronskian nonvanishing criterion for independent finite polynomial families; finite-family univariate criterion and multivariate Hasse interface are prerequisite API.

Completed `Roth.sqrt_one_sub_inv_lt`: No missing generic tangent API; whether to add the extra threshold convenience API is an upstream design question.

Completed `Roth.inv_add_inv_le`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.sum_inv_le`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.sum_inv_lt`: Candidate generic convex symmetric-average endpoint theorem or positive reciprocal-grid rational bound; exact sqrt corollary may remain downstream.

Completed `Roth.extend_apply_castSucc`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.extend_apply_last`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.card_filter_box_fiber_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.card_filter_box_last`: Design question: named arbitrary dependent tuple sections/cardinality law and binary filtered-product wrapper; no categorical structure required.

Completed `Roth.filter_weight_le_eq_empty`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.card_filter_fiber_eq`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.card_filter_weight_le_of_le_sqrt_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.card_filter_weight_le_succ_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.card_filter_weight_le`: Design choice: named finite-product normalized lower-tail count versus primary stronger product-measure concentration with local count corollary; retain redundant project box/weight aliases outside mathlib.

Completed `Roth.index`: No new generic minimum-support definition needed. A named point-index wrapper and normalization bridge can remain local; infinity-preserving API is distinct at zero.

Completed `Roth.mem_support_taylor_iff`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.index_le_weight`: No missing generic upper-bound law. Parent finite-sInf/infDegree projection bridge is normalization glue; coeff_taylor is separate project API.

Completed `Roth.exists_weight_eq_index`: No missing generic attained-minimum law. Parent finite-sInf/infDegree bridge and Taylor coefficient conversion are real normalization and separately justified project API.

Completed `Roth.le_index_iff`: No missing lower-bound law on infDegree. Parent coefficient/translation and real-default bridge are normalization API separately assessed.

Completed `Roth.index_nonneg`: No missing nonnegative-support lower-bound law on infDegree; project normalization bridge is actual new proof, not an existing mathlib call.

Completed `Roth.index_eq_zero_iff`: No missing generic finite-infimum bottom criterion; real/NNReal/Taylor bridges are new normalization proofs.

Completed `Roth.index_sub_weight_le_index_hasseDeriv`: Compatible coefficient-support shifts imply infDegree lower bounds, with Hasse derivative specialization and explicit finite minimum projection bridge.

Completed `Roth.le_index_sum`: No missing analogous sum law. Parent real-projection/Taylor normalization is a separately proved bridge, not existing-call replacement.

Completed `Roth.weight_eq_finsuppWeight_div`: No missing generic naturality law identified; supportClear is new normalization glue, not an existing mathlib replacement.

Completed `Roth.index_eq_weightedOrder_div`: MvPowerSeries.weightedOrder_coe against AddMonoidAlgebra.infDegree; proposed new theorem, not preexisting replacement

Completed `Roth.index_mul`: Potential extremal weighted-homogeneous component multiplication and arbitrary-real polynomial infDegree multiplication law. Existing component, support, graded decomposition APIs support arbitrary additive commutative weight monoids. Scope/normal-form design remains open; no absence theorem claimed.

Completed `Roth.index_prod`: Potential polynomial infDegree finite-product equality for real additive weights, likely grouped with binary equality and extremal weighted homogeneous component multiplication. No proof of absence claimed.

Completed `Roth.index_neg`: No essential gap; infDegree_neg name absent in loaded pin but exact law exists on OrderDual.

Completed `Roth.index_C_mul`: No essential mathematical gap. Named degree_smul convenience not identified; explicit congruence composition sufficient.

Completed `Roth.index_mul_left_weights`: No missing generic law: map_finset_inf. Project zero-default and reciprocal-weight adapters verified as new normalization proofs; not counted as existing mathlib primitives.

Completed `Roth.index_rename`: No essential mathematical gap. A discoverability-only infDegree rename wrapper is a separate API design choice; composition already uses two existing calls.

Completed `Roth.index_le_card`: Choice of named Taylor coordinate-degree envelope and its cardinality corollary versus generic support-witness use. Mathematical proofs are complete; upstream API questions remain.

Completed `Roth.index_unique`: Potential generic normalization API between finite real support minimum, projected infDegree and polynomial trailingDegree; exact new bridge evidence supplied, no unsupported absence claim.

Completed `Roth.coeffNone`: None required for the definition. Bundled coefficient map is existing composition; no claim of a preexisting name for whole composite.

Completed `Roth.eq_mapDomain_some_add_single`: No missing reconstruction law; optional naming question for additive Option normal form is not a blocking gap.

Completed `Roth.coeff_X_none_pow_mul_rename`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.coeff_coeffNone`: No missing coefficient law. An optional named Option-index bridge is a separate normal-form API question.

Completed `Roth.eq_sum_X_none_pow_mul_coeffNone`: No missing reconstruction theorem. A named inverse-C/rename bridge is optional convenience API; scratch bridge is new proof, not a counted mathlib call.

Completed `Roth.degreeOf_coeffNone_le`: Candidate Option-variable coordinate-degree coefficient law beside existing Fin analogue; whether to expose it directly or via a more general support-degree transport API is an upstream design question.

Completed `Roth.coeff_rename_mul_aeval`: Potential MvPolynomial coefficient adapter for separated Option-variable product, or reusable optionEquivLeft rename/aeval transport law; upstream API design question, not an absence theorem.

Completed `Roth.aeval_X_eq_rename`: None needed for exact target or five complete callers.

Completed `Roth.hasseDeriv_rename_mul_aeval`: Upstream multivariate Hasse derivative parent and compatibility API, Fresh-coordinate separated-product law over arbitrary injective embeddings; newly verified proof, not existing mathlib call

Completed `Roth.coeff_uniqueAlgEquiv_symm`: None

Completed `Roth.degreeOf_uniqueAlgEquiv_symm`: Potential named uniqueAlgEquiv degree rewrite or normalization bridge; upstream design choice rather than established mathematical gap.

Completed `Roth.degreeOf_rename_mul_aeval`: Design choice between degree preservation under multiplication by a nonzero zero-degree factor and degree zero outside the range of a renaming. No global absence claim.

Completed `Roth.degreeOf_none_rename_mul_aeval`: Design choice: general optionEquivLeft/rename-some AlgHom normalization bridge versus further separated degree wrapper.

Completed `Roth.linearIndependent_coordinate_polynomials_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.eq_sum_aeval_basis_coeffNone_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_coeffNone_basis_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_separated_representation`: Bounded independent separated decomposition, using generic finite-free coefficient-span machinery.

Completed `Roth.det_hasseDeriv_separated`: Multivariate Hasse derivative and fresh-coordinate factorwise law, settled finite-family Hasse-Wronskian API (binary polynomial Wronskian file has n-tuple TODO), and possible public separated derivative matrix/determinant factorization.

Completed `Roth.exists_sum_mul_eq_gcd`: None

Completed `Roth.exists_nat_smul_eq_map`: Design question: positive-natural rational-polynomial specialization versus generic map/scalar numerator bridge; no generic denominator-law gap.

Completed `Roth.exists_primitive_smul_eq`: MvPolynomial primitive representatives over a normalized GCD domain and its fraction field, with mapped scalar identity and coefficient gcd one. Finset.extract_gcd and localization are existing ingredients, not the full result.

Completed `Roth.exists_int_eq_of_gcd_eq_one`: finite-gcd scalar membership in an arbitrary submodule over a Bezout ring

Completed `Roth.rescale_separated_factor_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_int_polynomial_of_primitive_factor_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_int_factors`: Generic multivariate primitive representative (accepted172 proposal)., Finite primitive coefficient scalar descent over GCD domains (new reduced-fraction proof)., Separated polynomial factor descent with all degree conclusions.

Completed `Roth.exists_rat_factors_det_hasseDeriv_aux`: No new primitive is needed for this internal organization; full public contribution search is explicitly not run.

Completed `Roth.exists_det_eq_mul`: Finite-family Hasse Wronskian nonvanishing with bounded row orders, Separated original-ring factor descent over normalized GCD domains, Generic CommRing degree bound for Hasse derivative determinants, Synthesis theorem preserving separated nonzero factors and all individual bounds

Completed `Roth.RSet`: Potential generic multivariate naive coefficient-height interface and support/degree bridges; not an established upstream design.

Completed `Roth.indexSet`: No missing generic image API established; possible arithmetic-height/support laws require separate assessments.

Completed `Roth.Θ`: No missing generic supremum constructor/bound API established. Broader arithmetic-height/index development is a separate assessment.

Completed `Roth.lem6M`: Upstream packaging of auxiliary polynomial height/index infrastructure is a design question; later declarations assessed independently.

Completed `Roth.lem6Φ`: No missing API for outer constructor; index-infDegree bridge is new representation evidence assessed separately, not a claimed existing replacement.

Completed `Roth.one_mem_RSet`: Possible generic nonzero degree/height family unit-membership API, to be designed with BORDERLINE parent RSet; no missing primitive lemma needed for current proof.

Completed `Roth.indexSet_nonempty`: No missing binary-image nonempty law. Accepted184 bounded-family API judgment remains separate.

Completed `Roth.indexSet_bddAbove`: Upstream design choice for reusable weighted Taylor degree-envelope law; generic binary-image packaging needs no new theorem.

Completed `Roth.index_le_Θ`: No missing generic supremum law. Substantive arithmetic boundedness remains project API, accepted186 BORDERLINE; it is not a mathlib building block.

Completed `Roth.Θ_nonneg`: None

Completed `Roth.Θ_le_card`: Whether a Taylor coordinate-degree/cardinality envelope merits named upstream API after the index/Taylor parent representation is settled. Generic supremum transport is present; no claim that search failure proves absence.

Completed `Roth.Θ_le_of_forall_index_le`: No missing supremum-upper-bound API. image2 transport exists as Set.forall_mem_image2; arithmetic polynomial bounds remain separate.

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

Completed `Roth.box`: Useful local semantic API; not dead code.

Completed `Roth.weight`: No sorry/unsafe/raised limits; upstream duplicate, locally semantically useful.

Completed `Roth.mem_box`: Not dead:7 caller declarations. Thin wrapper candidate.

Completed `Roth.card_box`: Useful local API with 3 consumers, redundant as upstream addition.

Completed `Roth.card_le_card_box`: False

Completed `Roth.weight_nonneg`: Useful three-caller project API, not dead code.

Completed `Roth.weight_zero`: Not dead-code conclusion: simp API can be used without explicit name.

Completed `Roth.weight_add`: Useful local rewrite API (three callers), not dead code; no independent upstream addition recommended.

Completed `Roth.weight_eq_zero_iff`: False

Completed `Roth.weight_single`: Not dead: two explicit caller files; no simp attribute.

Completed `Roth.weight_le_card`: One real caller; not dead code.

Completed `Roth.weight_mul_left`: No sorry/unsafe/raised limits; active one-consumer local convenience theorem.

Completed `Roth.weight_le_degree_div`: No sorry/unsafe/raised limits. Zero explicit callers is only source-level evidence, not proof of dead public API.

Completed `Roth.weight_mapDomain`: Useful local API with three callers; redundant upstream analogue, not unused/dead code.

Completed `Roth.wronskianMatrix`: False

Completed `Roth.wronskian`: False

Completed `Roth.wronskian_eq_zero_of_not_linearIndependent`: False

Completed `Roth.det_choose_eq`: No; explicitly used once in Wronskian nonvanishing. No external-to-file reference claim or simp-closure inference.

Completed `Roth.coeff_prod_of_natDegree_le'`: Retain focused private induction helper for sole actual caller; prime distinguishes common-bound theorem.

Completed `Roth.sum_range_le_sum_of_injective`: Unused public convenience wrapper; zero explicit callers, zero inline re-derivations found.

Completed `Roth.coeff_wronskian_of_natDegree_injective`: No: sole local caller supplies nonvanishing induction base. Historical name can be improved.

Completed `Roth.wronskian_ne_zero_of_natDegree_injective`: False

Completed `Roth.wronskian_update_sub_smul`: Useful sole induction caller; not dead code.

Completed `Roth.linearIndependent_update_sub_smul`: Used twice; not dead code, but public polynomial-specific theorem duplicates existing generic law.

Completed `Roth.sum_natDegree_update_lt`: Live induction-measure helper, not junk.

Completed `Roth.wronskian_ne_zero_of_linearIndependent`: No: same-module iff plus two independent external consumers.

Completed `Roth.wronskian_eq_zero_iff`: No deletion: zero named source callers, but explicitly documented main public criterion; related downstream results use its primary implication. No simp attribute currently.

Completed `MvPolynomial.taylor`: One-line definition with concrete semantic/API-stability exemption; no automatic deletion merely from line count.

Completed `MvPolynomial.taylor_apply`: Zero named callers; standalone bridge is dispensable. Semantic translation definition is independently BORDERLINE, not inherited here.

Completed `MvPolynomial.taylor_X`: Used by one named private caller and exported as simp; not dead code. Redundant standalone mathematical result.

Completed `MvPolynomial.taylor_C`: Not dead code: one explicit named caller plus simp API; redundancy is independent of usage.

Completed `MvPolynomial.taylor_monomial`: Redundant local specialization with one explicit caller; no dead-code inference.

Completed `MvPolynomial.coeff_aeval_X_mul`: Retain private helper; useful boundary in monomial-induction proof. No sorry, resource raise, TODO or excessive proof size.

Completed `MvPolynomial.hasseCoeff_single_add_eq`: Keep private helper; short coordinate calculation separates scalar combinatorics from polynomial coefficient proof.

Completed `MvPolynomial.prod_pow_single_add_tsub`: Retain private helper; clear algebraic boundary in monomial coefficient induction; no sorry, resource raises or unused local assumptions.

Completed `MvPolynomial.coeff_taylor_monomial_single_add_aux`: Retain private induction-step helper to keep Finsupp induction case concise; no sorry, limitraise or long proof.

Completed `MvPolynomial.coeff_taylor_monomial_aux`: Retain private monomial boundary; full public theorem then reduces to additivity and this case.

Completed `MvPolynomial.coeff_taylor`: False

Completed `MvPolynomial.eval_taylor`: No named callers; not a simp theorem. Unused public compatibility API, not automatically dead code.

Completed `MvPolynomial.taylor_taylor`: Live: sole direct caller supplies negative-translation inverse, then injectivity/nonzero and Taylor expansion. No automatic junk verdict.

Completed `MvPolynomial.taylor_zero`: Not dead: simp attribute has verified implicit inverse-translation caller despite zero explicit references.

Completed `MvPolynomial.taylor_map`: Unused by explicit project source references, but standard base-change convenience law; zero references alone does not establish dead code.

Completed `MvPolynomial.taylor_rename`: Used in index invariance, not dead code. One source use and generic derivation do not by themselves force deletion.

Completed `MvPolynomial.degreeOf_taylor_le`: Used by index/cardinality bound; not dead code. Short proof relies on genuine new Hasse/Taylor content.

Completed `MvPolynomial.taylor_neg_taylor`: Two live mathematical callers, so not dead code; optional inlining depends on retaining or replacing the named translation API.

Completed `MvPolynomial.taylor_injective`: Live zero-reflection caller; named convenience corollary status depends on future translation API.

Completed `MvPolynomial.taylor_eq_zero_iff`: Live simplifier API with4 production consumers; not unused despite0explicit tokens.

Completed `MvPolynomial.eq_sum_box_hasseDeriv`: Keep standard substantive reconstruction theorem; actual evaluated consumer feeds main Diophantine estimate.

Completed `MvPolynomial.eval_eq_sum_box`: Keep standard exact identity with actual use in Roth upper estimate; short corollary of a missing substantive project theorem is not existing-mathlib duplication.

Completed `Roth.normOne`: Useful semantic one-line local API with fourteen consumers; keep in Roth/CoeffNorm.lean under production freeze. No assertion the norm laws or determinant estimates are junk.

Completed `Roth.diag`: Useful one-line semantic local API with eleven consumers; retain in CoeffNorm under production freeze. No claim downstream estimates are junk.

Completed `Roth.normOne_nonneg`: Useful local convenience with two consumers, not dead code. No production deletion in read-only survey.

Completed `Roth.normOne_eq_sum_of_support_subset`: Useful local convenience with two consumers/four rewrites; not dead code. No source changes in assessment.

Completed `Roth.normOne_monomial`: Useful project convenience with three consumers, not dead code; no source changes in read-only assessment.

Completed `Roth.normOne_zero`: Useful local public simp convenience with one explicit caller; not dead code. Direct proof audit closes293 values but does not justify deleting future/public simp API without refactor/rebuild.

Completed `Roth.abs_coeff_le_normOne`: Useful local convenience, not dead mathematics; no simp attribute, one explicit caller. Redundant as upstream theorem.

Completed `Roth.normOne_add_le`: Useful local subadditivity witness; one actual caller precludes dead-code classification.

Completed `Roth.normOne_neg`: Useful local sign simplification used in determinant, not dead code; redundant as an upstream contribution.

Completed `Roth.normOne_sum_le`: Not dead:4 occurrences in3 consumers. One-call local convenience whose upstream role follows coefficient-size API design.

Completed `Roth.normOne_mul_le`: Live main-result helper; not dead or junk.

Completed `Roth.normOne_prod_le`: Live helper for determinant norm estimate; no dead-code conclusion.

Completed `Roth.normOne_le_card_mul`: Thin wrapper with one caller; useful estimate, redundant public declaration.

Completed `Roth.normOne_det_le`: Not junk: module Main result and direct Lemma3 consumer.

Completed `Roth.abs_coeff_hasseDeriv_le`: Not junk: three explicit uses support main Lemma9, including iterated derivatives and diagonal remainder bounds.

Completed `Roth.normOne_hasseDeriv_le`: Keep estimate; integer-specific spelling becomes local specialization. Test-only size helper is not recommended public upstream API.

Completed `Roth.diag_eq_sum`: Not dead: two direct callers use the common expansion.

Completed `Roth.abs_coeff_diag_le`: Used by sole remainder coefficient estimate in Roth main lemma; not dead. No rewrite attribute or instance side effects.

Completed `Roth.natDegree_diag_le`: Not dead: one explicit and one canonical direct proof consumer, same private MainLemma theorem.

Completed `Roth.eval_diag`: Unused named wrapper; no simp attribute. Zero references alone not proof of mathematical uselessness.

Completed `Roth.diag_sub`: Not dead: one genuine consumer, mechanically replaceable using typed hdiag.

Completed `Roth.geom_sum_le_one_add_pow`: Used by private helper; not dead code.

Completed `Roth.sum_box_prod_pow_le_aux`: Retain this four-line private proof boundary with its single public caller. No sorry, new axiom, TODO or raised resource limit.

Completed `Roth.abs_eval_le`: Not junk: live main-lemma dependency and nontrivial finite weighted-support reasoning.

Completed `Roth.degreeOf_det_hasseDeriv_le`: Used twice; sound nonvacuous inequality; no junk classification.

Completed `Roth.abs_coeff_det_hasseDeriv_le`: Sound, used main-result lemma with nonempty and empty determinant cases; no junk finding.

Completed `Roth.genWronskian`: No dead-code claim; standard named invariant with5 explicit consumers and stable nonvanishing interface.

Completed `Roth.kronecker`: Useful local semantic API, not dead code. No new typeclass/coercion instance.

Completed `Roth.kroneckerExp`: Useful local semantic one-line API with3 callers; not dead code. No new instance/coercion structure.

Completed `Roth.kronHasse`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.kronSpan`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.genWronskian_eq_zero_of_not_linearIndependent`: No present named callers; mathematically standard paper lemma, not automatically junk.

Completed `Roth.kronecker_monomial`: Useful single-caller local coefficient calculation; no simp attribute, not dead code or an independent upstream contribution.

Completed `Roth.kroneckerExp_injOn`: Useful non-simp arithmetic helper, not dead; project alias should be replaced by general upstream law.

Completed `Roth.coeff_kronecker`: Not junk: actual zero-detection consumer supports generalized Wronskian theorem.

Completed `Roth.kronecker_eq_zero_iff`: Not dead: sole explicit caller and canonical direct dependency agree; no inline duplicate found.

Completed `Roth.linearIndependent_kronecker`: No; actual sole source consumer verified by replay.

Completed `Roth.derivative_aeval`: Live single-consumer helper feeding higher-order Kronecker/Hasse recurrence, not dead code.

Completed `Roth.derivative_kronHasse_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.derivative_mem_kronSpan`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.hasseDeriv_kronecker_mem`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_hasseDeriv_kronecker_eq_sum`: Live Wronskian helper; single explicit consumer does not make it dead or automatically composable.

Completed `Roth.det_sum_rows`: Live single-use helper; private local lemma or inlining is concrete alternative.

Completed `Roth.wronskian_kronecker_eq_sum_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_genWronskian_ne_zero`: Live module main theorem, substantive classical result; not junk despite a single direct consumer.

Completed `Roth.sqrt_one_sub_inv_lt`: Live single-use scalar helper; retain locally while upstream scope is undecided.

Completed `Roth.inv_add_inv_le`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.sum_inv_le`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.sum_inv_lt`: Not dead: one private induction caller supports public lattice-count estimate. No duplicate full inline derivation found.

Completed `Roth.extend_apply_castSucc`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.extend_apply_last`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.card_filter_box_fiber_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.card_filter_box_last`: No: sole live induction consumer. Public visibility could become private if current source API suffices.

Completed `Roth.filter_weight_le_eq_empty`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.card_filter_fiber_eq`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.card_filter_weight_le_of_le_sqrt_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.card_filter_weight_le_succ_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.card_filter_weight_le`: No: live sole count estimate on the auxiliary-polynomial/main-lemma path.

Completed `Roth.index`: False

Completed `Roth.mem_support_taylor_iff`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.index_le_weight`: False

Completed `Roth.exists_weight_eq_index`: False

Completed `Roth.le_index_iff`: Not dead: four consumers/five uses; not simp. Specialized wrapper need not be upstream.

Completed `Roth.index_nonneg`: Not dead; three consumers, not a simp theorem. Useful manuscript-facing local convenience, no upstream theorem gap.

Completed `Roth.index_eq_zero_iff`: Used local manuscript convenience API, not dead code; redundant upstream after parent re-aim.

Completed `Roth.index_sub_weight_le_index_hasseDeriv`: Used twice; no dead-code or duplicate-wrapper deletion justified.

Completed `Roth.le_index_sum`: Used once in determinant proof; not dead code. Local manuscript wrapper may remain while upstream contribution would duplicate existing degree API.

Completed `Roth.weight_eq_finsuppWeight_div`: Active local implementation bridge; not dead code.

Completed `Roth.index_eq_weightedOrder_div`: Active local API, three applications in sole caller; not dead code.

Completed `Roth.index_mul`: Not junk: two callers, one in another module, and a module main result. No independent production inline duplicate found.

Completed `Roth.index_prod`: Not junk: module main result and one determinant caller in another module. No independent inline duplicate found in production.

Completed `Roth.index_neg`: Currently unused theorem without simp attribute; harmless local compatibility helper, not evidence of external deadness.

Completed `Roth.index_C_mul`: Used compatibility adapter; not dead code. No proof holes or infrastructure changes.

Completed `Roth.index_mul_left_weights`: Not junk: two proof applications in sole private caller. Not a simp theorem; no external use inferred.

Completed `Roth.index_rename`: Useful transport API, not dead code: equivalence and separate-variable embeddings are genuine consumers.

Completed `Roth.index_le_card`: No. Two actual callers use the bound. hP is redundant only under current projected real convention.

Completed `Roth.index_unique`: False

Completed `Roth.coeffNone`: Useful local helper with seven consumers; not dead code.

Completed `Roth.eq_mapDomain_some_add_single`: Not dead: one explicit and direct-kernel caller.

Completed `Roth.coeff_X_none_pow_mul_rename`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.coeff_coeffNone`: Useful: two explicit callers and two direct kernel-value consumers.

Completed `Roth.eq_sum_X_none_pow_mul_coeffNone`: Useful: one source caller and one direct kernel-value consumer.

Completed `Roth.degreeOf_coeffNone_le`: Zero explicit/kernel callers; one mathematically relevant inline derivation. Not automatically dead or automatically public API.

Completed `Roth.coeff_rename_mul_aeval`: Useful local adapter: three uses in two callers; not junk.

Completed `Roth.aeval_X_eq_rename`: Useful in five callers, hence not dead code; public wrapper duplicates existing bundled Mathlib API.

Completed `Roth.hasseDeriv_rename_mul_aeval`: False

Completed `Roth.coeff_uniqueAlgEquiv_symm`: No explicit callers and no direct canonical kernel consumers; exact redundant law established independently, so zero-use count is supporting evidence rather than a dead-API inference.

Completed `Roth.degreeOf_uniqueAlgEquiv_symm`: Not dead: two actual source uses and two exact native direct kernel-value consumers.

Completed `Roth.degreeOf_rename_mul_aeval`: Not junk: one explicit project use and one direct kernel-value consumer.

Completed `Roth.degreeOf_none_rename_mul_aeval`: Not dead: one explicit and direct kernel consumer, Roth.exists_det_eq_mul.

Completed `Roth.linearIndependent_coordinate_polynomials_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.eq_sum_aeval_basis_coeffNone_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_coeffNone_basis_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_separated_representation`: Not junk: substantive finite-rank decomposition, both independent factor families and degree control are used to construct nonzero Wronskians in the sole caller.

Completed `Roth.det_hasseDeriv_separated`: Not junk: sole full private caller uses this identity to obtain rational separated factors, feeding integer separation; no duplicate inline derivation found.

Completed `Roth.exists_sum_mul_eq_gcd`: Useful current caller, so not dead code; redundant local wrapper.

Completed `Roth.exists_nat_smul_eq_map`: Live integrality helper with one source caller and one canonical direct consumer.

Completed `Roth.exists_primitive_smul_eq`: Not dead code: one explicit consumer uses every conclusion. Not safely deletable as a three-call wrapper.

Completed `Roth.exists_int_eq_of_gcd_eq_one`: dead code: False; reason: one source caller and one direct kernel consumer in integral polynomial descent

Completed `Roth.rescale_separated_factor_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_int_polynomial_of_primitive_factor_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_int_factors`: status: False; reason: Main module result used by determinant factorization.

Completed `Roth.exists_rat_factors_det_hasseDeriv_aux`: Retain a live private proof interface. No placeholders, unsafe proof, new axiom, TODO or raised limit.

Completed `Roth.exists_det_eq_mul`: False

Completed `Roth.RSet`: Retain: live local arithmetic API; no dead-code/deletion recommendation. For B<0 the set is empty; zero is always excluded. Zero degree limits and empty/infinite variable types are valid inputs. All coefficients, including absent ones, are tested.

Completed `Roth.indexSet`: Live local semantic alias with4 textual caller declarations/5 occurrences and10 direct kernel value consumers; retain in Theta.

Completed `Roth.Θ`: Live semantic local alias,19 explicit callers/28 occurrences,13 direct kernel-value and17 type consumers. Retain locally; no deletion recommended.

Completed `Roth.lem6M`: Retain locally: live semantic API used on19 source lines by six declarations; not dead code.

Completed `Roth.lem6Φ`: Retain locally: useful semantic name used by five declarations; not dead code.

Completed `Roth.one_mem_RSet`: Retain locally in Roth/Theta.lean: live unit witness for index-family nonemptiness.

Completed `Roth.indexSet_nonempty`: Useful locally to2 supremum callers; delete wrapper with parent re-aim and use existing image2 law; local paper-navigation compatibility is the only retention rationale.

Completed `Roth.indexSet_bddAbove`: Not dead: two explicit uses. Docstring wrongly suggests positive r despite no premise.

Completed `Roth.index_le_Θ`: Useful local helper; not dead. Upstream duplicate of generic supremum API.

Completed `Roth.Θ_nonneg`: Not dead code: two explicit calls in one declaration; not tagged simp.

Completed `Roth.Θ_le_card`: Not dead: used once to close the large-delta branch of Lemma7. Retain local API during read-only assessment.

Completed `Roth.Θ_le_of_forall_index_le`: Not dead: two explicit applications and two direct canonical value consumers; no simp attribute. Local convenience spelling may be retained only as a deliberate downstream choice.

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
| 26 | `Roth.box` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.box.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.box/root-acceptance.json) |
| 27 | `Roth.weight` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.weight.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.weight/root-acceptance.json) |
| 28 | `Roth.mem_box` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.mem_box.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.mem_box/root-acceptance.json) |
| 29 | `Roth.card_box` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.card_box.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.card_box/root-acceptance.json) |
| 30 | `Roth.card_le_card_box` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.card_le_card_box.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.card_le_card_box/root-acceptance.json) |
| 31 | `Roth.weight_nonneg` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.weight_nonneg.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.weight_nonneg/root-acceptance.json) |
| 32 | `Roth.weight_zero` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.weight_zero.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.weight_zero/root-acceptance.json) |
| 33 | `Roth.weight_add` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.weight_add.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.weight_add/root-acceptance.json) |
| 34 | `Roth.weight_eq_zero_iff` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.weight_eq_zero_iff.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.weight_eq_zero_iff/root-acceptance.json) |
| 35 | `Roth.weight_single` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.weight_single.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.weight_single/root-acceptance.json) |
| 36 | `Roth.weight_le_card` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.weight_le_card.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.weight_le_card/root-acceptance.json) |
| 37 | `Roth.weight_mul_left` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.weight_mul_left.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.weight_mul_left/root-acceptance.json) |
| 38 | `Roth.weight_le_degree_div` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.weight_le_degree_div.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.weight_le_degree_div/root-acceptance.json) |
| 39 | `Roth.weight_mapDomain` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.weight_mapDomain.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.weight_mapDomain/root-acceptance.json) |
| 40 | `Roth.wronskianMatrix` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.wronskianMatrix.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.wronskianMatrix/root-acceptance.json) |
| 41 | `Roth.wronskian` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.wronskian.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.wronskian/root-acceptance.json) |
| 42 | `Roth.wronskian_eq_zero_of_not_linearIndependent` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.wronskian_eq_zero_of_not_linearIndependent.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/root-acceptance.json) |
| 43 | `Roth.det_choose_eq` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.det_choose_eq.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.det_choose_eq/root-acceptance.json) |
| 44 | `Roth.coeff_prod_of_natDegree_le'` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.coeff_prod_of_natDegree_le'.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.coeff_prod_of_natDegree_le'/root-acceptance.json) |
| 45 | `Roth.sum_range_le_sum_of_injective` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.sum_range_le_sum_of_injective.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.sum_range_le_sum_of_injective/root-acceptance.json) |
| 46 | `Roth.coeff_wronskian_of_natDegree_injective` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.coeff_wronskian_of_natDegree_injective.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.coeff_wronskian_of_natDegree_injective/root-acceptance.json) |
| 47 | `Roth.wronskian_ne_zero_of_natDegree_injective` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.wronskian_ne_zero_of_natDegree_injective.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.wronskian_ne_zero_of_natDegree_injective/root-acceptance.json) |
| 48 | `Roth.wronskian_update_sub_smul` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.wronskian_update_sub_smul.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.wronskian_update_sub_smul/root-acceptance.json) |
| 49 | `Roth.linearIndependent_update_sub_smul` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.linearIndependent_update_sub_smul.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.linearIndependent_update_sub_smul/root-acceptance.json) |
| 50 | `Roth.sum_natDegree_update_lt` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.sum_natDegree_update_lt.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.sum_natDegree_update_lt/root-acceptance.json) |
| 51 | `Roth.wronskian_ne_zero_of_linearIndependent` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.wronskian_ne_zero_of_linearIndependent.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.wronskian_ne_zero_of_linearIndependent/root-acceptance.json) |
| 52 | `Roth.wronskian_eq_zero_iff` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.wronskian_eq_zero_iff.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.wronskian_eq_zero_iff/root-acceptance.json) |
| 53 | `MvPolynomial.taylor` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.taylor/root-acceptance.json) |
| 54 | `MvPolynomial.taylor_apply` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_apply.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.taylor_apply/root-acceptance.json) |
| 55 | `MvPolynomial.taylor_X` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_X.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.taylor_X/root-acceptance.json) |
| 56 | `MvPolynomial.taylor_C` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_C.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.taylor_C/root-acceptance.json) |
| 57 | `MvPolynomial.taylor_monomial` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_monomial.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.taylor_monomial/root-acceptance.json) |
| 58 | `MvPolynomial.coeff_aeval_X_mul` | SKIP | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_aeval_X_mul.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.coeff_aeval_X_mul/root-acceptance.json) |
| 59 | `MvPolynomial.hasseCoeff_single_add_eq` | SKIP | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.hasseCoeff_single_add_eq.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff_single_add_eq/root-acceptance.json) |
| 60 | `MvPolynomial.prod_pow_single_add_tsub` | SKIP | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.prod_pow_single_add_tsub.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.prod_pow_single_add_tsub/root-acceptance.json) |
| 61 | `MvPolynomial.coeff_taylor_monomial_single_add_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_taylor_monomial_single_add_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/root-acceptance.json) |
| 62 | `MvPolynomial.coeff_taylor_monomial_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_taylor_monomial_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.coeff_taylor_monomial_aux/root-acceptance.json) |
| 63 | `MvPolynomial.coeff_taylor` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.coeff_taylor.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.coeff_taylor/root-acceptance.json) |
| 64 | `MvPolynomial.eval_taylor` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.eval_taylor.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.eval_taylor/root-acceptance.json) |
| 65 | `MvPolynomial.taylor_taylor` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_taylor.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.taylor_taylor/root-acceptance.json) |
| 66 | `MvPolynomial.taylor_zero` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_zero.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.taylor_zero/root-acceptance.json) |
| 67 | `MvPolynomial.taylor_map` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_map.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.taylor_map/root-acceptance.json) |
| 68 | `MvPolynomial.taylor_rename` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_rename.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.taylor_rename/root-acceptance.json) |
| 69 | `MvPolynomial.degreeOf_taylor_le` | YES-add-as-is | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.degreeOf_taylor_le.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.degreeOf_taylor_le/root-acceptance.json) |
| 70 | `MvPolynomial.taylor_neg_taylor` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_neg_taylor.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.taylor_neg_taylor/root-acceptance.json) |
| 71 | `MvPolynomial.taylor_injective` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_injective.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.taylor_injective/root-acceptance.json) |
| 72 | `MvPolynomial.taylor_eq_zero_iff` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.taylor_eq_zero_iff.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.taylor_eq_zero_iff/root-acceptance.json) |
| 73 | `MvPolynomial.eq_sum_box_hasseDeriv` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.eq_sum_box_hasseDeriv.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.eq_sum_box_hasseDeriv/root-acceptance.json) |
| 74 | `MvPolynomial.eval_eq_sum_box` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/MvPolynomial.eval_eq_sum_box.md) · [Acceptance](.mathlib-quality/overview/evidence/MvPolynomial.eval_eq_sum_box/root-acceptance.json) |
| 75 | `Roth.normOne` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne/root-acceptance.json) |
| 76 | `Roth.diag` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.diag.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.diag/root-acceptance.json) |
| 77 | `Roth.normOne_nonneg` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne_nonneg.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne_nonneg/root-acceptance.json) |
| 78 | `Roth.normOne_eq_sum_of_support_subset` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne_eq_sum_of_support_subset.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne_eq_sum_of_support_subset/root-acceptance.json) |
| 79 | `Roth.normOne_monomial` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne_monomial.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne_monomial/root-acceptance.json) |
| 80 | `Roth.normOne_zero` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne_zero.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne_zero/root-acceptance.json) |
| 81 | `Roth.abs_coeff_le_normOne` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_le_normOne.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.abs_coeff_le_normOne/root-acceptance.json) |
| 82 | `Roth.normOne_add_le` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne_add_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne_add_le/root-acceptance.json) |
| 83 | `Roth.normOne_neg` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne_neg.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne_neg/root-acceptance.json) |
| 84 | `Roth.normOne_sum_le` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne_sum_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne_sum_le/root-acceptance.json) |
| 85 | `Roth.normOne_mul_le` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne_mul_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne_mul_le/root-acceptance.json) |
| 86 | `Roth.normOne_prod_le` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne_prod_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne_prod_le/root-acceptance.json) |
| 87 | `Roth.normOne_le_card_mul` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne_le_card_mul.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne_le_card_mul/root-acceptance.json) |
| 88 | `Roth.normOne_det_le` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne_det_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne_det_le/root-acceptance.json) |
| 89 | `Roth.abs_coeff_hasseDeriv_le` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_hasseDeriv_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.abs_coeff_hasseDeriv_le/root-acceptance.json) |
| 90 | `Roth.normOne_hasseDeriv_le` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.normOne_hasseDeriv_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.normOne_hasseDeriv_le/root-acceptance.json) |
| 91 | `Roth.diag_eq_sum` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.diag_eq_sum.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.diag_eq_sum/root-acceptance.json) |
| 92 | `Roth.abs_coeff_diag_le` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_diag_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.abs_coeff_diag_le/root-acceptance.json) |
| 93 | `Roth.natDegree_diag_le` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.natDegree_diag_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.natDegree_diag_le/root-acceptance.json) |
| 94 | `Roth.eval_diag` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.eval_diag.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.eval_diag/root-acceptance.json) |
| 95 | `Roth.diag_sub` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.diag_sub.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.diag_sub/root-acceptance.json) |
| 96 | `Roth.geom_sum_le_one_add_pow` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.geom_sum_le_one_add_pow.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.geom_sum_le_one_add_pow/root-acceptance.json) |
| 97 | `Roth.sum_box_prod_pow_le_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.sum_box_prod_pow_le_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.sum_box_prod_pow_le_aux/root-acceptance.json) |
| 98 | `Roth.abs_eval_le` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.abs_eval_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.abs_eval_le/root-acceptance.json) |
| 99 | `Roth.degreeOf_det_hasseDeriv_le` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_det_hasseDeriv_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.degreeOf_det_hasseDeriv_le/root-acceptance.json) |
| 100 | `Roth.abs_coeff_det_hasseDeriv_le` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.abs_coeff_det_hasseDeriv_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.abs_coeff_det_hasseDeriv_le/root-acceptance.json) |
| 101 | `Roth.genWronskian` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.genWronskian.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.genWronskian/root-acceptance.json) |
| 102 | `Roth.kronecker` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.kronecker.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.kronecker/root-acceptance.json) |
| 103 | `Roth.kroneckerExp` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.kroneckerExp.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.kroneckerExp/root-acceptance.json) |
| 104 | `Roth.kronHasse` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.kronHasse.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.kronHasse/root-acceptance.json) |
| 105 | `Roth.kronSpan` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.kronSpan.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.kronSpan/root-acceptance.json) |
| 106 | `Roth.genWronskian_eq_zero_of_not_linearIndependent` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.genWronskian_eq_zero_of_not_linearIndependent.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/root-acceptance.json) |
| 107 | `Roth.kronecker_monomial` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.kronecker_monomial.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.kronecker_monomial/root-acceptance.json) |
| 108 | `Roth.kroneckerExp_injOn` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.kroneckerExp_injOn.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.kroneckerExp_injOn/root-acceptance.json) |
| 109 | `Roth.coeff_kronecker` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.coeff_kronecker.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.coeff_kronecker/root-acceptance.json) |
| 110 | `Roth.kronecker_eq_zero_iff` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.kronecker_eq_zero_iff.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.kronecker_eq_zero_iff/root-acceptance.json) |
| 111 | `Roth.linearIndependent_kronecker` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.linearIndependent_kronecker.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.linearIndependent_kronecker/root-acceptance.json) |
| 112 | `Roth.derivative_aeval` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.derivative_aeval.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.derivative_aeval/root-acceptance.json) |
| 113 | `Roth.derivative_kronHasse_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.derivative_kronHasse_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.derivative_kronHasse_aux/root-acceptance.json) |
| 114 | `Roth.derivative_mem_kronSpan` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.derivative_mem_kronSpan.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.derivative_mem_kronSpan/root-acceptance.json) |
| 115 | `Roth.hasseDeriv_kronecker_mem` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.hasseDeriv_kronecker_mem.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.hasseDeriv_kronecker_mem/root-acceptance.json) |
| 116 | `Roth.exists_hasseDeriv_kronecker_eq_sum` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_hasseDeriv_kronecker_eq_sum.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_hasseDeriv_kronecker_eq_sum/root-acceptance.json) |
| 117 | `Roth.det_sum_rows` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.det_sum_rows.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.det_sum_rows/root-acceptance.json) |
| 118 | `Roth.wronskian_kronecker_eq_sum_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.wronskian_kronecker_eq_sum_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.wronskian_kronecker_eq_sum_aux/root-acceptance.json) |
| 119 | `Roth.exists_genWronskian_ne_zero` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_genWronskian_ne_zero.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_genWronskian_ne_zero/root-acceptance.json) |
| 120 | `Roth.sqrt_one_sub_inv_lt` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.sqrt_one_sub_inv_lt.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.sqrt_one_sub_inv_lt/root-acceptance.json) |
| 121 | `Roth.inv_add_inv_le` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.inv_add_inv_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.inv_add_inv_le/root-acceptance.json) |
| 122 | `Roth.sum_inv_le` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.sum_inv_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.sum_inv_le/root-acceptance.json) |
| 123 | `Roth.sum_inv_lt` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.sum_inv_lt.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.sum_inv_lt/root-acceptance.json) |
| 124 | `Roth.extend_apply_castSucc` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.extend_apply_castSucc.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.extend_apply_castSucc/root-acceptance.json) |
| 125 | `Roth.extend_apply_last` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.extend_apply_last.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.extend_apply_last/root-acceptance.json) |
| 126 | `Roth.card_filter_box_fiber_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.card_filter_box_fiber_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.card_filter_box_fiber_aux/root-acceptance.json) |
| 127 | `Roth.card_filter_box_last` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.card_filter_box_last.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.card_filter_box_last/root-acceptance.json) |
| 128 | `Roth.filter_weight_le_eq_empty` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.filter_weight_le_eq_empty.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.filter_weight_le_eq_empty/root-acceptance.json) |
| 129 | `Roth.card_filter_fiber_eq` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.card_filter_fiber_eq.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.card_filter_fiber_eq/root-acceptance.json) |
| 130 | `Roth.card_filter_weight_le_of_le_sqrt_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.card_filter_weight_le_of_le_sqrt_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.card_filter_weight_le_of_le_sqrt_aux/root-acceptance.json) |
| 131 | `Roth.card_filter_weight_le_succ_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.card_filter_weight_le_succ_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.card_filter_weight_le_succ_aux/root-acceptance.json) |
| 132 | `Roth.card_filter_weight_le` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.card_filter_weight_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.card_filter_weight_le/root-acceptance.json) |
| 133 | `Roth.index` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.index.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index/root-acceptance.json) |
| 134 | `Roth.mem_support_taylor_iff` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.mem_support_taylor_iff.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.mem_support_taylor_iff/root-acceptance.json) |
| 135 | `Roth.index_le_weight` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.index_le_weight.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_le_weight/root-acceptance.json) |
| 136 | `Roth.exists_weight_eq_index` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_weight_eq_index.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_weight_eq_index/root-acceptance.json) |
| 137 | `Roth.le_index_iff` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.le_index_iff.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.le_index_iff/root-acceptance.json) |
| 138 | `Roth.index_nonneg` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.index_nonneg.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_nonneg/root-acceptance.json) |
| 139 | `Roth.index_eq_zero_iff` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.index_eq_zero_iff.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_eq_zero_iff/root-acceptance.json) |
| 140 | `Roth.index_sub_weight_le_index_hasseDeriv` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.index_sub_weight_le_index_hasseDeriv.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_sub_weight_le_index_hasseDeriv/root-acceptance.json) |
| 141 | `Roth.le_index_sum` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.le_index_sum.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.le_index_sum/root-acceptance.json) |
| 142 | `Roth.weight_eq_finsuppWeight_div` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.weight_eq_finsuppWeight_div.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.weight_eq_finsuppWeight_div/root-acceptance.json) |
| 143 | `Roth.index_eq_weightedOrder_div` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.index_eq_weightedOrder_div.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_eq_weightedOrder_div/root-acceptance.json) |
| 144 | `Roth.index_mul` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.index_mul.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_mul/root-acceptance.json) |
| 145 | `Roth.index_prod` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.index_prod.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_prod/root-acceptance.json) |
| 146 | `Roth.index_neg` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.index_neg.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_neg/root-acceptance.json) |
| 147 | `Roth.index_C_mul` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.index_C_mul.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_C_mul/root-acceptance.json) |
| 148 | `Roth.index_mul_left_weights` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.index_mul_left_weights.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_mul_left_weights/root-acceptance.json) |
| 149 | `Roth.index_rename` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.index_rename.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_rename/root-acceptance.json) |
| 150 | `Roth.index_le_card` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.index_le_card.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_le_card/root-acceptance.json) |
| 151 | `Roth.index_unique` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.index_unique.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_unique/root-acceptance.json) |
| 152 | `Roth.coeffNone` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.coeffNone.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.coeffNone/root-acceptance.json) |
| 153 | `Roth.eq_mapDomain_some_add_single` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.eq_mapDomain_some_add_single.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.eq_mapDomain_some_add_single/root-acceptance.json) |
| 154 | `Roth.coeff_X_none_pow_mul_rename` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.coeff_X_none_pow_mul_rename.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.coeff_X_none_pow_mul_rename/root-acceptance.json) |
| 155 | `Roth.coeff_coeffNone` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.coeff_coeffNone.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.coeff_coeffNone/root-acceptance.json) |
| 156 | `Roth.eq_sum_X_none_pow_mul_coeffNone` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.eq_sum_X_none_pow_mul_coeffNone.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/root-acceptance.json) |
| 157 | `Roth.degreeOf_coeffNone_le` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_coeffNone_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.degreeOf_coeffNone_le/root-acceptance.json) |
| 158 | `Roth.coeff_rename_mul_aeval` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.coeff_rename_mul_aeval.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.coeff_rename_mul_aeval/root-acceptance.json) |
| 159 | `Roth.aeval_X_eq_rename` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.aeval_X_eq_rename.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.aeval_X_eq_rename/root-acceptance.json) |
| 160 | `Roth.hasseDeriv_rename_mul_aeval` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.hasseDeriv_rename_mul_aeval.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.hasseDeriv_rename_mul_aeval/root-acceptance.json) |
| 161 | `Roth.coeff_uniqueAlgEquiv_symm` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.coeff_uniqueAlgEquiv_symm.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.coeff_uniqueAlgEquiv_symm/root-acceptance.json) |
| 162 | `Roth.degreeOf_uniqueAlgEquiv_symm` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_uniqueAlgEquiv_symm.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.degreeOf_uniqueAlgEquiv_symm/root-acceptance.json) |
| 163 | `Roth.degreeOf_rename_mul_aeval` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_rename_mul_aeval.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.degreeOf_rename_mul_aeval/root-acceptance.json) |
| 164 | `Roth.degreeOf_none_rename_mul_aeval` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.degreeOf_none_rename_mul_aeval.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.degreeOf_none_rename_mul_aeval/root-acceptance.json) |
| 165 | `Roth.linearIndependent_coordinate_polynomials_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.linearIndependent_coordinate_polynomials_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.linearIndependent_coordinate_polynomials_aux/root-acceptance.json) |
| 166 | `Roth.eq_sum_aeval_basis_coeffNone_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.eq_sum_aeval_basis_coeffNone_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.eq_sum_aeval_basis_coeffNone_aux/root-acceptance.json) |
| 167 | `Roth.exists_coeffNone_basis_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_coeffNone_basis_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_coeffNone_basis_aux/root-acceptance.json) |
| 168 | `Roth.exists_separated_representation` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_separated_representation.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_separated_representation/root-acceptance.json) |
| 169 | `Roth.det_hasseDeriv_separated` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.det_hasseDeriv_separated.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.det_hasseDeriv_separated/root-acceptance.json) |
| 170 | `Roth.exists_sum_mul_eq_gcd` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_sum_mul_eq_gcd.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_sum_mul_eq_gcd/root-acceptance.json) |
| 171 | `Roth.exists_nat_smul_eq_map` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_nat_smul_eq_map.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_nat_smul_eq_map/root-acceptance.json) |
| 172 | `Roth.exists_primitive_smul_eq` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_primitive_smul_eq.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_primitive_smul_eq/root-acceptance.json) |
| 173 | `Roth.exists_int_eq_of_gcd_eq_one` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_int_eq_of_gcd_eq_one.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_int_eq_of_gcd_eq_one/root-acceptance.json) |
| 174 | `Roth.rescale_separated_factor_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.rescale_separated_factor_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.rescale_separated_factor_aux/root-acceptance.json) |
| 175 | `Roth.exists_int_polynomial_of_primitive_factor_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_int_polynomial_of_primitive_factor_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/root-acceptance.json) |
| 176 | `Roth.exists_int_factors` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_int_factors.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_int_factors/root-acceptance.json) |
| 177 | `Roth.exists_rat_factors_det_hasseDeriv_aux` | SKIP | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_rat_factors_det_hasseDeriv_aux.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_rat_factors_det_hasseDeriv_aux/root-acceptance.json) |
| 178 | `Roth.exists_det_eq_mul` | YES-but-generalise-first | [Report](.mathlib-quality/overview/mathlibable/Roth.exists_det_eq_mul.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.exists_det_eq_mul/root-acceptance.json) |
| 179 | `Roth.RSet` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.RSet.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.RSet/root-acceptance.json) |
| 180 | `Roth.indexSet` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.indexSet.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.indexSet/root-acceptance.json) |
| 181 | `Roth.Θ` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.Θ.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.Θ/root-acceptance.json) |
| 182 | `Roth.lem6M` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.lem6M.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.lem6M/root-acceptance.json) |
| 183 | `Roth.lem6Φ` | NO-composable-from-mathlib | [Report](.mathlib-quality/overview/mathlibable/Roth.lem6Φ.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.lem6Φ/root-acceptance.json) |
| 184 | `Roth.one_mem_RSet` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.one_mem_RSet.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.one_mem_RSet/root-acceptance.json) |
| 185 | `Roth.indexSet_nonempty` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.indexSet_nonempty.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.indexSet_nonempty/root-acceptance.json) |
| 186 | `Roth.indexSet_bddAbove` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.indexSet_bddAbove.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.indexSet_bddAbove/root-acceptance.json) |
| 187 | `Roth.index_le_Θ` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.index_le_Θ.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.index_le_Θ/root-acceptance.json) |
| 188 | `Roth.Θ_nonneg` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.Θ_nonneg.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.Θ_nonneg/root-acceptance.json) |
| 189 | `Roth.Θ_le_card` | BORDERLINE-needs-human | [Report](.mathlib-quality/overview/mathlibable/Roth.Θ_le_card.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.Θ_le_card/root-acceptance.json) |
| 190 | `Roth.Θ_le_of_forall_index_le` | NO-mathlib-has-it | [Report](.mathlib-quality/overview/mathlibable/Roth.Θ_le_of_forall_index_le.md) · [Acceptance](.mathlib-quality/overview/evidence/Roth.Θ_le_of_forall_index_le/root-acceptance.json) |

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

Completed `Roth.box` action: NO-composable-from-mathlib; do not upstream redundant definition; locally migrate domains to Iic or retain project wrapper pending coordinated normalization.

Completed `Roth.weight` action: NO-mathlib-has-it; migrate 30 callers per report and remove redundant definition after downstream validation; local notation/interface optional.

Completed `Roth.mem_box` action: Delete mem_box during cleanup; inline exact three-fact term or expand box in explicit simp sites; optionally migrate parent to Iic.

Completed `Roth.card_box` action: NO-composable-from-mathlib; coordinate delete with all 3 explicit caller rewrites; no production changes in assessment.

Completed `Roth.card_le_card_box` action: Keep local useful helper while resolving three upstream interface questions; do not inherit parent NO or count project parents as mathlib facts. No production edits.

Completed `Roth.weight_nonneg` action: Do not submit this wrapper upstream. In a later authorized refactor inline the documented proof in all three callers; or keep as readable project-local Roth/Box.lean API.

Completed `Roth.weight_zero` action: NO-mathlib-has-it under parent re-aim rule: use existing map_zero on reciprocal Finsupp.weight after coordinated parent migration; keep local compatibility API until full dependents compile.

Completed `Roth.weight_add` action: NO-mathlib-has-it under parent re-aim rule: use existing map_add on reciprocal Finsupp.weight after coordinated parent migration; keep local compatibility API until full dependents compile.

Completed `Roth.weight_eq_zero_iff` action: BORDERLINE-needs-human; retain local theorem pending three API-design choices in report.

Completed `Roth.weight_single` action: Re-aim at Finsupp.weight_single after coordinated parent weight migration; normalize smul/inverse to quotient at both Lattice155 and Theta391, then remove duplicate local singleton theorem once full caller modules compile. Transitional quotient wrapper belongs in Roth/Box.lean.

Completed `Roth.weight_le_card` action: BORDERLINE-needs-human: decide upstream convenience API versus sole-caller inline after parent migration. Keep local until that decision.

Completed `Roth.weight_mul_left` action: NO-mathlib-has-it via verified parent re-aim. Migrate sole Index pointwise image step to existing generator law and reciprocal normalization; remove local theorem during parent migration; retain locally in Box only if old interface remains.

Completed `Roth.weight_le_degree_div` action: BORDERLINE-needs-human. Keep local while deciding whether to add general Finsupp generator comparison API; no production change or PR. Three concrete upstream design questions in report.

Completed `Roth.weight_mapDomain` action: NO-mathlib-has-it. Future recommendation only: in a future parent migration (not performed or authorized by this read-only overview), migrate weight to reciprocal-generator Finsupp.weight, use linearCombination_mapDomain at all three callers, and delete the wrapper; alternatively retain a local no-hf compatibility lemma in Roth/Box.lean. Keep index_rename injectivity for support. Current production remains unchanged.

Completed `Roth.wronskianMatrix` action: Retain useful local name pending future upstream granularity/normalization choice. No implementation authorized; if anchor rejected, report lists all caller inlining plans.

Completed `Roth.wronskian` action: BORDERLINE-needs-human: retain active local anchor pending coherent upstream API decision; read-only future recommendations.

Completed `Roth.wronskian_eq_zero_of_not_linearIndependent` action: Retain locally pending upstream API choice; optional verified four-call proof cleanup.

Completed `Roth.det_choose_eq` action: YES-but-generalise-first: expose cancellation-free ring identity and local-factorial quotient corollary in Mathlib/LinearAlgebra/Vandermonde.lean; existing abstract law reused; focused separate PR; run /generalise and /cleanup before submission.

Completed `Roth.coeff_prod_of_natDegree_le'` action: SKIP-private under overview9a after complete applicable review/native verification. Future generalization recorded; production unchanged.

Completed `Roth.sum_range_le_sum_of_injective` action: Delete wrapper in follow-up cleanup; no caller edits. Conditionally inspect now-unused Int.Sum import with ordinary import/build checks. If desired retain private pedagogical helper in Roth/Wronskian.lean.

Completed `Roth.coeff_wronskian_of_natDegree_injective` action: YES-but-generalise-first MODERN-IDIOM: upstream raw coefficient determinant formula to Mathlib/RingTheory/Polynomial/Wronskian.lean with det_choose_eq; keep parent interfaces unchanged during local specialization.

Completed `Roth.wronskian_ne_zero_of_natDegree_injective` action: YES-but-generalise-first: /generalise target for cast-degree hypothesis; group with accepted coefficient theorem and coordinate determinant support; /cleanup before upstream Wronskian.lean PR. Sole caller supplies Nat.cast_injective.comp hinj.

Completed `Roth.wronskian_update_sub_smul` action: Retain local theorem pending three concrete upstream family-API questions; do not submit a duplicate generic determinant law.

Completed `Roth.linearIndependent_update_sub_smul` action: Delete public specialised wrapper during refactor; use existing shear iff and checked normalisation at both callers.

Completed `Roth.sum_natDegree_update_lt` action: BORDERLINE-needs-human: resolve three concrete upstream API questions; retain project-local measure helper meanwhile.

Completed `Roth.wronskian_ne_zero_of_linearIndependent` action: BORDERLINE-needs-human: retain locally; decide CommRing parent/Domain theorem and naming/echelon API before upstream submission.

Completed `Roth.wronskian_eq_zero_iff` action: Retain locally; resolve foundation Domain/Field, finite indexing and public iff/simp API questions before upstreaming.

Completed `MvPolynomial.taylor` action: Retain project-local pending upstream decision on named translation API versus direct aeval; see three concrete Phase 7 questions.

Completed `MvPolynomial.taylor_apply` action: Recommend remove unused docstring/theorem at Taylor lines45–47; zero caller edits; keep qualified univariate Index243 unchanged. Local retention for documentation remains possible.

Completed `MvPolynomial.taylor_X` action: Recommend delete standalone taylor_X, replace Taylor:114 rw token by a typed show equality from aeval_X _ _. For implicit simp consumers use local [taylor] and run full build in production refactor. Alternatively retain in Roth/Taylor.lean as an explicit project semantic API choice.

Completed `MvPolynomial.taylor_C` action: NO-mathlib-has-it: delete specialized theorem and replace Index197 taylor_C token with show taylor α (C c) = C c from algHom_C _ _. Existing generic simp law handles tested constant/product/power consumers. Run full build during production migration; alternative retain locally in Roth/Taylor.lean for documented semantic API rationale.

Completed `MvPolynomial.taylor_monomial` action: Delete taylor_monomial and replace sole named rewrite at eq_sum_box_hasseDeriv with typed show equality from aeval_monomial _ _ _, as accepted full caller replay. Parent taylor and caller content remain separately assessed.

Completed `MvPolynomial.coeff_aeval_X_mul` action: Keep unchanged; private prefilter SKIP after full applicable inventory/structural/native assessment.

Completed `MvPolynomial.hasseCoeff_single_add_eq` action: Retain unchanged; completed private-prefilter SKIP with full applicable structural/native evidence.

Completed `MvPolynomial.prod_pow_single_add_tsub` action: Keep source unchanged; record verified CommMonoid weakening as future refactor opportunity, private-prefilter SKIP complete.

Completed `MvPolynomial.coeff_taylor_monomial_single_add_aux` action: Keep unchanged; complete private-prefilter SKIP, proceed to private monomial coefficient theorem.

Completed `MvPolynomial.coeff_taylor_monomial_aux` action: Keep unchanged; complete private-prefilter SKIP, continue full public assessment of coeff_taylor.

Completed `MvPolynomial.coeff_taylor` action: Upstream with accepted public multivariate Hasse API; use direct aeval if optional taylor naming is declined.

Completed `MvPolynomial.eval_taylor` action: BORDERLINE-needs-human: retain in Roth/Taylor.lean pending named-law, target-algebra, naming/simp choices; zero callers to migrate.

Completed `MvPolynomial.taylor_taylor` action: BORDERLINE-needs-human: keep in Roth/Taylor.lean pending translation API design; if omitted upstream inline generator normalization at Taylor.lean:184.

Completed `MvPolynomial.taylor_zero` action: NO-composable-from-mathlib: decline separate upstream theorem. If removing local lemma, inline three-fact composition in taylor_neg_taylor proof after taylor_taylor/neg_add_cancel normalization and rebuild project; retain locally while named translation simp API is desired. Read-only assessment, no production edits.

Completed `MvPolynomial.taylor_map` action: BORDERLINE: decide translation convenience API, orientation/naming and whether to expose only generic substitution law. Keep production unchanged; no user input needed to complete this read-only assessment.

Completed `MvPolynomial.taylor_rename` action: BORDERLINE: choose named convenience law versus generic substitution API, bundled square and naming/orientation. Read-only assessment complete; production unchanged.

Completed `MvPolynomial.degreeOf_taylor_le` action: Propose in Mathlib/Algebra/MvPolynomial/Taylor.lean with coefficient Taylor and Hasse degree/vanishing API; direct aeval statement if named translation is declined.

Completed `MvPolynomial.taylor_neg_taylor` action: BORDERLINE: choose pointwise inverse law versus bundled translation equivalence, then decide simp/name policy. Assessment complete; no production edits.

Completed `MvPolynomial.taylor_injective` action: BORDERLINE: retain locally during read-only survey; decide bundled equivalence versus separate injectivity corollary upstream. Inline the tested generic term at Taylor193 if the concrete corollary is declined.

Completed `MvPolynomial.taylor_eq_zero_iff` action: YES-but-generalise-first: propose CommSemiring theorem in Mathlib/Algebra/MvPolynomial/Taylor.lean with coefficient theorem; retain production unchanged during survey, use direct aeval spelling if named translation API declined.

Completed `MvPolynomial.eq_sum_box_hasseDeriv` action: YES-but-generalise-first: drop explicit equality-decision requirement with verified transport; propose Mathlib/Algebra/MvPolynomial/Taylor.lean alongside coeff_taylor, using standard Finsupp interval infrastructure upstream. Production unchanged during survey.

Completed `MvPolynomial.eval_eq_sum_box` action: YES-but-generalise-first: propose Mathlib/Algebra/MvPolynomial/Taylor.lean with coefficient-CommSemiring/arbitrary-ring-algebra-target B-valued center/point/no-explicit-DecidableEq theorem and original recovery; group with accepted finite expansion/coefficient/Hasse foundations. Sources unchanged; full Taylor milestone build clean2467 jobs.

Completed `Roth.normOne` action: NO-composable-from-mathlib for upstream integer-only def. Reuse existing Finsupp.sum; retain local name for readable downstream bounds. If deleting later, use all fourteen caller plans and full dependent validation. Sources unchanged.

Completed `Roth.diag` action: NO-composable-from-mathlib upstream wrapper. Reuse existing aeval; if later deleting, apply all eleven explicit caller plans and full dependent validation. Production sources unchanged.

Completed `Roth.normOne_nonneg` action: NO-composable-from-mathlib upstream. Keep local CoeffNorm convenience or inline exact two-call proof at two specified callers after separate authorized source refactor.

Completed `Roth.normOne_eq_sum_of_support_subset` action: NO-mathlib-has-it. Use Finsupp.sum_of_support_subset with explicit absolute-value function and zero normalization at all four uses, or retain project-local CoeffNorm convenience pending separately authorized refactor; no upstream PR.

Completed `Roth.normOne_monomial` action: NO-mathlib-has-it. Use existing sum_monomial_eq/Finsupp.sum_single_index directly at all3 references or retain project-local CoeffNorm convenience pending authorized refactor. No upstream PR.

Completed `Roth.normOne_zero` action: NO-mathlib-has-it. Use existing sum_zero_index directly for the one explicit zero witness; retain project-local CoeffNorm simp bridge while parent spelling remains. No upstream PR and no production changes in assessment.

Completed `Roth.abs_coeff_le_normOne` action: During an authorized code cleanup, delete local theorem and replace the one CoeffNorm.lean:266 reference by Finsupp.single_eval_le_sum _ (g := fun z : ℤ ↦ |(z : ℝ)|) (by simp) (fun _ ↦ abs_nonneg _) _. Keep Roth/CoeffNorm.lean as alternative project-local destination if pedagogical naming is retained. Assessment only; production unchanged.

Completed `Roth.normOne_add_le` action: BORDERLINE-needs-human: preserve local theorem; decide generic Finsupp inequality versus compatible L1 structure before upstreaming. Full read-only assessment complete; no production edits.

Completed `Roth.normOne_neg` action: NO-composable-from-mathlib: recommended future cleanup deletes public helper and inserts explicit Finsupp composition as local quantified sign identity in determinant. Alternative stable destination remains Roth/CoeffNorm.lean. Assessment changes no production files.

Completed `Roth.normOne_sum_le` action: BORDERLINE-needs-human: retain local finite wrapper for now; settle common coefficient-size API and discoverability question. No production change made.

Completed `Roth.normOne_mul_le` action: BORDERLINE: retain local API pending generic coefficient-size convolution/representation design; no production edit.

Completed `Roth.normOne_prod_le` action: BORDERLINE: retain local wrapper pending shared coefficient-size API; inline existing finite induction in sole determinant caller if removing locally.

Completed `Roth.normOne_le_card_mul` action: NO-mathlib-has-it: inline Finset.sum_le_card_nsmul via local hsize in determinant caller and delete wrapper in separately authorized implementation. Keep source explanation in Roth/CoeffNorm.lean.

Completed `Roth.normOne_det_le` action: YES-but-generalise-first MODERN-IDIOM: propose Matrix.ringSeminorm_det_le in new Mathlib/LinearAlgebra/Matrix/Seminorm.lean; keep local normOne corollary; run /generalise and /cleanup.

Completed `Roth.abs_coeff_hasseDeriv_le` action: YES-but-generalise-first MODERN-IDIOM: add additive-seminorm version in proposed Mathlib/Analysis/Polynomial/MvHasseDeriv.lean, after upstream algebraic Hasse API; preserve local integer corollary.

Completed `Roth.normOne_hasseDeriv_le` action: YES-but-generalise-first: propose Mathlib/Analysis/Polynomial/MvHasseDeriv.lean after foundational algebra PR, group coefficient sup and coefficient sum bounds; generalise/cleanup before submission.

Completed `Roth.diag_eq_sum` action: BORDERLINE: retain production unchanged; resolve the three concrete upstream API questions before proposing a lemma or inlining.

Completed `Roth.abs_coeff_diag_le` action: BORDERLINE: decide upstream coefficient-fiber API and estimate scope. Keep local theorem until that choice; exact replay demonstrates migration if generic API is selected.

Completed `Roth.natDegree_diag_le` action: Retain local theorem; decide upstream coordinate-to-total bridge API before PR or deletion.

Completed `Roth.eval_diag` action: In a later authorized refactor remove eval_diag, update0 named callers, retain MainLemma409 existing stronger composition-law proof. Future callers specialize comp_aeval_apply or hom_eval₂.

Completed `Roth.diag_sub` action: NO-mathlib-has-it. In future cleanup replace the sole caller using accepted replay, delete local wrapper; alternative destination CoeffNorm only if stable local spelling deliberately retained.

Completed `Roth.geom_sum_le_one_add_pow` action: Generalize, clean and propose Mathlib/Algebra/Order/Ring/GeomSum.lean lemma; thereafter migrate sole caller. No production edits made.

Completed `Roth.sum_box_prod_pow_le_aux` action: Keep unchanged; completed private-prefilter SKIP with all applicable structural/native evidence. Continue full public assessment of Roth.abs_eval_le.

Completed `Roth.abs_eval_le` action: YES-but-generalise-first (MODERN-IDIOM); contribute a generic size-hom eval₂ theorem in Mathlib/Analysis/Polynomial/MvPolynomial.lean, then specialize the sole project caller.

Completed `Roth.degreeOf_det_hasseDeriv_le` action: YES-but-generalise-first; contribute generic determinant-degree API, then Hasse corollary with parent Hasse API; retain project convenience specialization if useful.

Completed `Roth.abs_coeff_det_hasseDeriv_le` action: YES-but-generalise-first; upstream generalized norm/Hasse infrastructure and coefficient bound, update sole caller to omit hB0.

Completed `Roth.genWronskian` action: YES-but-generalise-first; propose Mathlib/RingTheory/MvPolynomial/Wronskian.lean after upstream Hasse API; /generalise target then /cleanup target; root review pending.

Completed `Roth.kronecker` action: NO-mathlib-has-it. Inline existing aeval at all9 named callers per tested migration, or retain a documented local/private helper in Roth/GenWronskian.lean; do not propose this wrapper alone upstream.

Completed `Roth.kroneckerExp` action: NO-mathlib-has-it. Use Finsupp.weight power weights in kronecker_monomial, kroneckerExp_injOn, coeff_kronecker per compiled replay, or keep documented local/private helper in Roth/GenWronskian.lean. Do not upstream duplicate definition alone.

Completed `Roth.kronHasse` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.kronSpan` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.genWronskian_eq_zero_of_not_linearIndependent` action: BORDERLINE-needs-human: retain project-local until shared/alternating API chosen; optional verified four-call cleanup; no source callers to rewrite.

Completed `Roth.kronecker_monomial` action: NO-mathlib-has-it. Delete exported specialization during parent refactor; sole caller uses verified local hmon normalization from aeval_monomial then coeff_C_mul_X_pow. Alternative destination private/local helper in Roth/GenWronskian.lean.

Completed `Roth.kroneckerExp_injOn` action: YES-but-generalise-first. Propose Finsupp.weight_pow_injOn in Mathlib/Data/Nat/Digits/Finsupp.lean; independent foundational PR, then reuse in NoetherNormalization and generalized Wronskian development. Run /generalise and /cleanup before PR.

Completed `Roth.coeff_kronecker` action: BORDERLINE-needs-human; resolve three concrete upstream API packaging questions. Production unchanged.

Completed `Roth.kronecker_eq_zero_iff` action: verdict: BORDERLINE-needs-human; questions: Bridge-only weighted aeval/mapDomainAlgHom contribution versus packaged consequences?, Restricted Set.InjOn primary, with named support-local zero iff rewriting corollary?, Include positional degree-box zero test with explicit-enumeration separation API or keep it local?; local destination: Roth/GenWronskian.lean; refactor: At linearIndependent_kronecker:123 substitute verified zero_replay/chosen support-law specialization; preserve sum-degree premises and caller hk.

Completed `Roth.linearIndependent_kronecker` action: verdict: BORDERLINE-needs-human; questions: Expose support-family independence corollary or only restricted aeval injection plus existing LinearIndependent.map_injOn?, Expose explicit-enumeration arbitrary-family no-hk positional corollary or keep it project-local?, Keep span-to-supported inclusion local via Submodule.span_le or package it with the chosen evaluation API?; next: Choose whether support/positional corollary merits public API after restricted-injection bridge; keep local until choice. No production edits in assessment.; potential home: Mathlib/Algebra/MvPolynomial/MonomialEval.lean (bridge API/import layering provisional); distinct positional separation108 remains Mathlib/Data/Nat/Digits/Finsupp.lean; grouping: Accepted YES108 Roth.kroneckerExp_injOn;109/110 remain BORDERLINE, not inherited YES.

Completed `Roth.derivative_aeval` action: YES-but-generalise-first: generalize semiring/derivation API before upstreaming; update the actual private consumer using verified replay.

Completed `Roth.derivative_kronHasse_aux` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.derivative_mem_kronSpan` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.hasseDeriv_kronecker_mem` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.exists_hasseDeriv_kronecker_eq_sum` action: BORDERLINE-needs-human: choose primary upstream representation and characteristic scope; original Kronecker corollary can remain project-local. All assessment verification complete.

Completed `Roth.det_sum_rows` action: BORDERLINE-needs-human: choose determinant convenience theorem, generic weighted helper, or local-only expansion. If upstreamed broaden finite/dependent indices; no production edits.

Completed `Roth.wronskian_kronecker_eq_sum_aux` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.exists_genWronskian_ne_zero` action: YES-but-generalise-first: remove global variable finiteness with accepted support bridge, prepare new Mathlib/RingTheory/MvPolynomial/Wronskian.lean beside accepted parent proposal; retain CharZero/Field/row bounds; independently develop any domain or power-series extension.

Completed `Roth.sqrt_one_sub_inv_lt` action: BORDERLINE-needs-human: decide threshold API versus existing Bernoulli tangent theorem; keep local helper, consider private real-parameter form.

Completed `Roth.inv_add_inv_le` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.sum_inv_le` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.sum_inv_lt` action: BORDERLINE-needs-human: decide generic convex versus rational-grid API and whether sqrt corollary belongs upstream; preserve verified real/weak threshold if exposed.

Completed `Roth.extend_apply_castSucc` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.extend_apply_last` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.card_filter_box_fiber_aux` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.card_filter_box_last` action: Retain project-local Lattice theorem pending three concrete upstream API choices; no automatic NO via parent or new helper counted as existing mathlib.

Completed `Roth.filter_weight_le_eq_empty` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.card_filter_fiber_eq` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.card_filter_weight_le_of_le_sqrt_aux` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.card_filter_weight_le_succ_aux` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.card_filter_weight_le` action: Retain local theorem and caller pending3 concrete upstream API questions; no production refactor now, no cost-based downgrade, prior helper verdicts not inherited.

Completed `Roth.index` action: Retain Roth.index in Roth/Index.lean as the project convention wrapper; any refactor should implement it via infDegree and transport all 34 callers using the all-P/all-r bridge.

Completed `Roth.mem_support_taylor_iff` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.index_le_weight` action: Keep as a local manuscript convenience, or migrate parent to infDegree and replace all six applications with the generic projected bound. Full six-caller replay verified; no upstream PR for this theorem.

Completed `Roth.exists_weight_eq_index` action: Retain locally for manuscript vocabulary or migrate parent to projected infDegree and replace all four applications using existing Finset attainment. Delete this wrapper after replacing those calls; complete consumer replay verified. No upstream PR.

Completed `Roth.le_index_iff` action: NO-mathlib-has-it via parent re-aim. Migrate parent to projected infDegree, apply Finset.le_inf_iff (or le_inf'_iff after projection) at all five uses and retain caller arithmetic; otherwise keep local manuscript convenience in Roth/Index.lean.

Completed `Roth.index_nonneg` action: NO-mathlib-has-it via independently verified parent re-aim. Migrate parent/shared projection bridge; use existing finite-inf lower-bound law at each of three applications and preserve surrounding antisymmetry, supremum and determinant arithmetic. Alternative destination Roth/Index.lean local convenience API.

Completed `Roth.index_eq_zero_iff` action: After sharing parent projection and NNReal recoding bridges replace index_prod empty-product iff .2 application with existing finite-inf criterion and evaluation1 normalization; delete wrapper or retain project-local in Roth/Index.lean.

Completed `Roth.index_sub_weight_le_index_hasseDeriv` action: YES-but-generalise-first MODERN-IDIOM: contribute verified new aeval/infDegree derivative bound in Mathlib/Algebra/MvPolynomial/TaylorDegree.lean, staged after accepted Hasse/Taylor infrastructure; retain local point-index wrapper. Full PR title/grouping/reviewer and generalise/cleanup/pre-submit checklist in report.

Completed `Roth.le_index_sum` action: NO-mathlib-has-it by fresh parent re-aim: after shared parent bridge, inline common-bound introduction and OrderDual supDegree_sum_le at Theta.lean398; retain nonzero determinant and projection. Alternative local destination Roth/Index.lean; no upstream PR proposed.

Completed `Roth.weight_eq_finsuppWeight_div` action: NO-mathlib-has-it by Mode B parent re-aim. Keep documented project bridge in Roth/Index.lean or migrate parent and replace both sole-caller rewrites using checked representation bridge.

Completed `Roth.index_eq_weightedOrder_div` action: YES-but-generalise-first: remove hP locally; propose canonical polynomial/series comparison, with reciprocal denominator specialization kept project-local; review imports/naming and run generalise/cleanup.

Completed `Roth.index_mul` action: verdict: BORDERLINE-needs-human; questions: For polynomial finite-support orders, should the primary upstream law be stated directly for AddMonoidAlgebra.infDegree with real additive variable weights, rather than through natural MvPowerSeries.weightedOrder?, Should the broader law first expose an extremal weightedHomogeneousComponent multiplication API for arbitrary ordered additive weight targets, with the polynomial infDegree result as its corollary?, Should the reciprocal-weight real index remain project-local, using the independently checked natural-series normalization and existing weightedOrder_mul, while the broader infDegree/initial-form API is developed separately?; local refactor: Use the proved hr-free replacement at both call sites; full replays preserve their statements. For Theta the formerly sole-used hr0 becomes unused and can be renamed _hr0 without changing its position/type. Keep real default-zero nonvanishing guards.; upstream scope: Decide primary polynomial finite-order interface and whether to develop component multiplication as its reusable foundation. Do not submit a duplicate natural weightedOrder_mul.

Completed `Roth.index_prod` action: verdict: BORDERLINE-needs-human; questions: Should the upstream finite-product law target polynomial AddMonoidAlgebra.infDegree for arbitrary real additive weights, alongside the corresponding binary product law?, Should that law be organized through an extremal weightedHomogeneousComponent product theorem over ordered additive weights?, Should reciprocal-weight default-zero index_prod remain project-local while natural-weight applications use the existing MvPowerSeries.weightedOrder_prod API?; local refactor: Keep hf, replace original induction with hr-free binary induction and direct index-one base; entire determinant caller can invoke the hr-free theorem. Retain the theorem locally until upstream polynomial-order scope is settled.; upstream scope: Do not add a duplicate natural weightedOrder_prod wrapper. Decide the real-weight polynomial initial-form/order API together with its binary law.

Completed `Roth.index_neg` action: NO-mathlib-has-it via parent re-aim; do not upstream this specialization. Retain local adapter in Roth/Index.lean if parent retained; no explicit callers to refactor.

Completed `Roth.index_C_mul` action: NO-composable-from-mathlib on generic parent reaim. Do not upstream concrete specialization. At sole Theta405 caller, inline verified original-form support proof if removing wrapper; retain map_intCast and Taylor/parent bridge normalization. Alternative local home Roth/Index.lean during parent migration.

Completed `Roth.index_mul_left_weights` action: NO-mathlib-has-it via parent re-aim. Migrate minimum to infDegree and transport by map_finset_inf through checked zero-preserving projection. Replace both caller applications with identical-type bridge. Retain convention-bearing adapter locally in Roth/Index.lean if old index API retained; do not substitute raw map_finset_inf in old rw.

Completed `Roth.index_rename` action: Do not upstream Roth-specific theorem. With parent migration inline generic two-call support-inf transport at both Theta consumers; retain explicit center/weight adapter at current boundary, local in Roth/Index.lean or private near callers. No production mutation in this assessment.

Completed `Roth.index_le_card` action: BORDERLINE-needs-human: decide upstream coordinate-bound audience, zero∞ convention, and grouping with weight_le_card/Taylor degree API. Retain local theorem unchanged during read-only overview. Future local cleanup can drop hP and update both callers.

Completed `Roth.index_unique` action: Do not upstream project spelling. Keep a documented project-local all-polynomial bridge while retaining index; at Theta242 replace index_unique nonzeroProof by that bridge, retain hR for later coefficient/log estimate. After full parent migration normalize to Polynomial then use existing rootMultiplicity_eq_natTrailingDegree; delete old wrapper only after caller conversion. Read-only assessment makes no production edits.

Completed `Roth.coeffNone` action: Use direct optionEquivLeft/coeff upstream; optionally retain documented local Roth.coeffNone for readability. All seven refactors verified by entire Separation replay.

Completed `Roth.eq_mapDomain_some_add_single` action: Delete project theorem after replacing sole caller true branch with rw [Roth.coeffNone, optionEquivLeft_coeff_some_coeff_none]; complete caller replay verified. Retain optional exposition in Roth/Separation.lean docstring.

Completed `Roth.coeff_X_none_pow_mul_rename` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.coeff_coeffNone` action: Delete only after refactoring both callers: eqsum uses optionEquivLeft_coeff_some_coeff_none; coefficient product uses optionElim normalization then optionEquivLeft_coeff_coeff. Both full caller replays passed. Optional local exposition belongs in Roth/Separation.lean.

Completed `Roth.eq_sum_X_none_pow_mul_coeffNone` action: Refactor sole full caller exists_separated_representation using existing Polynomial expansion, degree identity and verified inverse-equivalence bridge; delete wrapper only after caller update. Optional explanatory local destination Roth/Separation.lean.

Completed `Roth.degreeOf_coeffNone_le` action: Keep local pending the two documented upstream API choices; if Option law accepted, rename to MvPolynomial.degreeOf_coeff_optionEquivLeft_le, remove coeffNone alias from statement and use it in private basis auxiliary.

Completed `Roth.coeff_rename_mul_aeval` action: verdict: BORDERLINE-needs-human; local: Keep current theorem in Roth/Separation.lean while deciding reusable coordinate bridge API. No production changes made.; future questions: Should mathlib expose a coefficient theorem for separated products in Option variables, despite its three-call iterated-polynomial core?, Should upstream instead expose the optionEquivLeft rename/aeval transport law and have users derive scalar coefficients through existing coefficient APIs?; possible home: Mathlib/Algebra/MvPolynomial/Equiv.lean, subject to import-layer review; no PR yet; caller refactor: If adapter is added, replace the simp/rw lemma at all three call sites; full caller replay demonstrates original signatures can be preserved.

Completed `Roth.aeval_X_eq_rename` action: Delete public wrapper and update all five caller uses to existing-law specialization; retain only local/private project rewrite helper if preferred. Read-only assessment made no production edits.

Completed `Roth.hasseDeriv_rename_mul_aeval` action: upstream file: Mathlib/Algebra/MvPolynomial/HasseDeriv.lean; pr title: feat(Algebra/MvPolynomial/HasseDeriv): differentiate products in a fresh variable; next steps: /generalise Roth.hasseDeriv_rename_mul_aeval, /cleanup Roth/Separation.lean Roth.hasseDeriv_rename_mul_aeval, Upstream parent multivariate Hasse API first; install generalized law in MvPolynomial namespace., Migrate sole determinant caller using specialization and remove old wrapper when new API exists.; reviewers: Moritz Firsching (hasseDeriv_map #42428), Yaël Dillies (MvPolynomial coefficient API #41427)

Completed `Roth.coeff_uniqueAlgEquiv_symm` action: Recommend delete Roth.coeff_uniqueAlgEquiv_symm; zero caller rewrites. Retain the existing fully qualified mathlib law in Separation and Theta. If compatibility is required temporarily, keep only a project-local deprecated wrapper in Roth/Separation.lean; no upstream PR.

Completed `Roth.degreeOf_uniqueAlgEquiv_symm` action: Retain locally pending upstream API choice: direct singleton degree rewrite, normalization bridge, and default versus arbitrary coordinate signature. Both full caller replacements compiled; no production edits made.

Completed `Roth.degreeOf_rename_mul_aeval` action: Keep local while deciding three upstream API questions; semiring weakening verified; sole caller can inline accepted derivation without changing original interface.

Completed `Roth.degreeOf_none_rename_mul_aeval` action: BORDERLINE: retain provisionally; decide upstream bridge/wrapper grain; weaken/refactor in separate cleanup. Full caller inline proof verified.

Completed `Roth.linearIndependent_coordinate_polynomials_aux` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.eq_sum_aeval_basis_coeffNone_aux` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.exists_coeffNone_basis_aux` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.exists_separated_representation` action: YES-but-generalise-first; propose new Mathlib/Algebra/MvPolynomial/Separation.lean leaf, preserve complete API, then cleanup/upstream review; production unchanged.

Completed `Roth.det_hasseDeriv_separated` action: BORDERLINE-needs-human: choose public fresh-coordinate determinant law versus primary matrix factorization after parent finite-family Wronskian API is settled. Keep Roth/Separation.lean and sole caller unchanged until that design decision; complete read-only verification unresolved[]. Provisional Mathlib/RingTheory/MvPolynomial/Wronskian.lean follows accepted genWronskian proposal, not a settled import commitment.

Completed `Roth.exists_sum_mul_eq_gcd` action: Delete wrapper; at Separation:446 use Finset.gcd_eq_sum_mul s u directly, retaining gcd-left/factor-right orientation and adapting the two arithmetic lines as verified in Bezout170.caller. No production change made.

Completed `Roth.exists_nat_smul_eq_map` action: BORDERLINE-needs-human: retain local helper pending three concrete upstream API questions; all verification complete, production unchanged.

Completed `Roth.exists_primitive_smul_eq` action: verdict: YES-but-generalise-first; reason: MODERN-IDIOM; declaration: MvPolynomial.exists_primitive_smul_eq; upstream file: Mathlib/RingTheory/MvPolynomial/Content.lean; new file: True; pr title: feat(MvPolynomial): primitive representatives over fraction fields; checklist: /generalise Roth.exists_primitive_smul_eq, /cleanup Roth/Separation.lean Roth.exists_primitive_smul_eq, Verify minimal new-module imports, generic signature, concrete specialization and full caller., /pre-submit before PR; grouping: Roth.exists_separated_representation, Roth.hasseDeriv_rename_mul_aeval; local destination: Roth/Separation.lean until upstream acceptance.; caller refactor: Roth.exists_int_factors:491 specializes new generic theorem with R := ℤ, K := ℚ, preserving witnesses and all conclusions.; optional followups: MvPolynomial content/IsPrimitive/primPart interface, Finsupp finite-coefficient gcd normalization; do not conflate gcd-primitive and unimodular.; reviewer candidates: Junyan Xu, Kim Morrison; reviewer evidence: reviewers.json

Completed `Roth.exists_int_eq_of_gcd_eq_one` action: verdict: YES-but-generalise-first; upstream file: Mathlib/RingTheory/PrincipalIdealDomain.lean; pr title: feat(RingTheory): finite gcd scalar membership in submodules over Bézout rings; grouping: Roth.exists_primitive_smul_eq; reviewer candidates: Xavier Roblot, Noah Walker; checklist: /generalise Roth.exists_int_eq_of_gcd_eq_one, Restate primary API as verified generic gcd-scaled submodule lemma, /cleanup Mathlib/RingTheory/PrincipalIdealDomain.lean Submodule.gcd_smul_mem, Review unit-gcd corollary for redundancy, Add docstring and run build/checks and /pre-submit; caller refactor: Replace sole helper call with checked original specialization of Submodule.gcd_smul_mem, preserving coefficients and witness orientation.; local destination: Roth/Separation.lean until generic API is adopted

Completed `Roth.rescale_separated_factor_aux` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.exists_int_polynomial_of_primitive_factor_aux` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.exists_int_factors` action: verdict: YES-but-generalise-first; upstream file: Mathlib/RingTheory/MvPolynomial/GaussLemma.lean; pr title: feat(MvPolynomial): descend separated fraction-field factors over GCD domains; grouping: Roth.exists_primitive_smul_eq, Roth.exists_int_eq_of_gcd_eq_one; checklist: /generalise Roth.exists_int_factors, /cleanup Roth/Separation.lean Roth.exists_int_factors, /cleanup Mathlib/RingTheory/MvPolynomial/GaussLemma.lean MvPolynomial.exists_separated_factors, Replay complete Roth.exists_det_eq_mul with generic specialization., /pre-submit; reviewer candidates: Justus Springer, Junyan Xu; local destination: Roth/Separation.lean during migration.

Completed `Roth.exists_rat_factors_det_hasseDeriv_aux` action: Keep unchanged; complete private-prefilter SKIP, then resume the next tracked declaration.

Completed `Roth.exists_det_eq_mul` action: verdict: YES-but-generalise-first; location: Mathlib/RingTheory/MvPolynomial/Separation.lean; title: feat(MvPolynomial): bounded Hasse determinants with separated factors; grouping: Roth.genWronskian, Roth.exists_genWronskian_ne_zero, Roth.exists_separated_representation, Roth.exists_primitive_smul_eq, Roth.exists_int_factors; checklist: /generalise Roth.exists_det_eq_mul: adopt exact verified arbitraryτ GCD-domain theorem, /cleanup Mathlib/RingTheory/MvPolynomial/Separation.lean MvPolynomial.exists_det_eq_mul, Reviewers Justus Springer and Junyan Xu based on focused relevant history; local destination: Roth/Separation.lean until layered API is upstreamed

Completed `Roth.RSet` action: verdict: BORDERLINE-needs-human; local destination: Roth/Theta.lean; recommendation: Retain the local stable name; choose generic upstream coefficient-height/support API before proposing this exact intersection. No edits requested.; questions: Generic multivariate coefficient sup-height API with RSet left local?, Include zero in a public bounded-coefficient body?, Arbitrary support set as primary degree parameter?, Independent uses for exact integer/real-bound/nonzero conjunction?

Completed `Roth.indexSet` action: verdict: NO-mathlib-has-it; existing declaration: Set.image2; existing path: Mathlib/Data/Set/Operations.lean; local destination: Roth/Theta.lean; recommendation: Retain alias; if eliminating, replace all5 textual occurrences with exact image2 term. Θ uses sSup, nonempty uses image2_nonempty_iff, boundedness and renaming preserve source proofs. No production edits in this assessment.

Completed `Roth.Θ` action: verdict: NO-mathlib-has-it; existing declaration: SupSet.sSup; existing path: Mathlib/Order/SetNotation.lean; local destination: Roth/Theta.lean; recommendation: Retain documented local Greek alias; no upstream primitive PR. If eliminating, replace all28 standalone occurrences at19 caller declarations with sSup(indexSet B q r), preserving their exact arguments; source table gives each plan.

Completed `Roth.lem6M` action: Retain locally; BORDERLINE standalone upstream status pending concrete scope decisions.

Completed `Roth.lem6Φ` action: NO-composable standalone upstream. Retain locally in Roth/Theta.lean; if future upstream rewrite deletes it, inline both summands at every listed caller and keep equivalence transport normalization.

Completed `Roth.one_mem_RSet` action: BORDERLINE; retain local theorem. Future generic family design could decide sufficient condition versus iff unit law and raw-set versus dedicated API. No standalone Roth-specific upstream PR yet.

Completed `Roth.indexSet_nonempty` action: NO-mathlib-has-it: re-aim indexSet at image2; replace nonempty premises at Θ_le_of_forall_index_le and Θ_mono by image2_nonempty_iff plus full unit and coprime witnesses; no upstream addition.

Completed `Roth.indexSet_bddAbove` action: BORDERLINE-needs-human: retain Roth/Theta.lean helper; decide upstream uniform envelope/infinity convention and coordinate-envelope versus card specialization. Keep arithmetic proof separate from generic image law.

Completed `Roth.index_le_Θ` action: Do not upstream this theorem. Inline le_csSup with explicit project boundedness and membership at all three call occurrences, or retain local helper in Roth/Theta.lean as project ergonomics. No production edits made.

Completed `Roth.Θ_nonneg` action: NO-mathlib-has-it. Inline Real.sSup_nonneg at both index_le_lem6 occurrences with independent pointwise premise, or retain project-local manuscript convenience theorem; no upstream addition.

Completed `Roth.Θ_le_card` action: BORDERLINE-needs-human: retain Roth/Theta.lean theorem; resolve upstream normalized-index envelope/parent representation and whether any family corollary belongs upstream. Future cleanup can factor shared pointwise arithmetic bound with indexSet_bddAbove. No production changes.

Completed `Roth.Θ_le_of_forall_index_le` action: Do not upstream. In a separately authorized cleanup, delete wrapper and update both callers with csSup_le (indexSet_nonempty hB q r), then destruct family witnesses; keep the substantive continuations. Alternative destination Roth/Theta.lean if local readability warrants retention.

## Recommended action plan

1. Retain the useful local coefficient alias while assessing the complete Hasse API.
2. Do not submit a standalone PR for this direct two-operation definition.
3. Prepare the multivariate Hasse operator for a future coherent mathlib contribution; assess
   `Roth.Θ_mono` next. Supporting identities receive their own applicable checks.
4. Preserve all per-declaration query/proof/log evidence and publish only accepted complete assessments.
5. Keep production Lean sources and pins unchanged; use a warm server and bounded, batched scratch checks.

Evidence correction 2026-10-27: the full-canonical caller audits for
`Roth.normOne_add_le` and `Roth.normOne_neg` were rerun against the exact 293
unique names after detecting duplicated entries in their earlier enumerators.
Their reports contain corrected receipts; callers, verdicts and completed count are unchanged.
