# Project overview: Roth

Updated: 2026-10-26. **IN PROGRESS — 66/293 declaration assessments complete.**

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
- Completed applicable assessments: 66; remaining: 227.
- Verdicts: 10 NO-composable-from-mathlib, 12 YES-add-as-is, 3 YES-but-generalise-first, 11 NO-mathlib-has-it, 21 BORDERLINE-needs-human, 9 SKIP.
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

## Recommended action plan

1. Retain the useful local coefficient alias while assessing the complete Hasse API.
2. Do not submit a standalone PR for this direct two-operation definition.
3. Prepare the multivariate Hasse operator for a future coherent mathlib contribution; assess
   `MvPolynomial.taylor_map` next. Supporting identities receive their own applicable checks.
4. Preserve all per-declaration query/proof/log evidence and publish only accepted complete assessments.
5. Keep production Lean sources and pins unchanged; use a warm server and bounded, batched scratch checks.
