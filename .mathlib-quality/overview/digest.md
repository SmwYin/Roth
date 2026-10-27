# Per-declaration digest (generated from the 293 reports)

### #1 def MvPolynomial.hasseCoeff (public, Roth/HasseDeriv.lean:50)
- verdict: YES-but-generalise-first | cost: MODERATE | junk: KEEP
- rationale: The multi-index binomial coefficient binom(k,d) = prod_j binom(k_j,d_j) is standard (multi-index notation) and absent from mathlib; it should go upstream as a Finsupp-level `Finsupp.choose k d` alongside a multivariate Hasse derivative rather than as an MvPolynomial-namespaced helper.
- action: Upstream together with MvPolynomial.hasseDeriv as `Finsupp.choose k d` (Nat.choose argument order) in Mathlib/Data/Finsupp/ or Mathlib/Data/Nat/Choose/Multinomial.lean, porting hasseCoeff_eq_zero_iff and hasseCoeff_eq_prod; locally keep as is (used in Roth/HasseDeriv.lean, Roth/CoeffNorm.lean, Roth/Taylor.lean).
- Type: `{σ : Type*} → (d k : σ →₀ ℕ) → ℕ`
- What: The multi-index binomial coefficient `∏_{j ∈ supp d} (k j).choose (d j)`, i.e. `binom(k, d)`; the scalar by which the Hasse derivative `Δ_d` multiplies the monomial `X^k`.
- Hypotheses: none (no typeclasses; `R` from the section `variable` is not included).
- Uses from project: `[]`
- Used by: Roth/HasseDeriv.lean: `hasseDeriv`, `hasseDeriv_monomial`, `hasseDeriv_apply`, `hasseCoeff_eq_zero_iff`, `coeff_hasseDeriv`, `hasseCoeff_eq_prod`, `hasseDeriv_zero_apply`, `hasseDeriv_C`, `hasseDeriv_rename`, `hasseCoeff_mul_hasseCoeff` (private), `hasseDeriv_hasseDeriv`, `hasseDeriv_hasseDeriv_of_disjoint`, `hasseCoeff_mul_succ` (private), `pderiv_hasseDeriv`, `hasseDeriv_monomial_mul`, `hasseDer

### #2 def MvPolynomial.hasseDeriv (public, Roth/HasseDeriv.lean:57)
- verdict: YES-but-generalise-first | cost: MODERATE | junk: KEEP
- rationale: The multivariate Hasse derivative is standard (DKSS method of multiplicities, nLab, Roth-type arguments) and absent from mathlib, which has only univariate Polynomial.hasseDeriv and LaurentSeries.hasseDeriv; it should ship with its coefficient spelled via the multi-index binomial Finsupp.choose and ideally with an MvPowerSeries companion beside MvPowerSeries.pderiv.
- action: Upstream to a new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean together with Finsupp.choose (from the hasseCoeff report), coeff_hasseDeriv, hasseDeriv_hasseDeriv, pderiv_hasseDeriv, factorial_smul_hasseDeriv_single, uniqueAlgEquiv_hasseDeriv; locally keep as is (used in 8 Roth files).
- Type: `{σ R : Type*} → [CommSemiring R] → (d : σ →₀ ℕ) → MvPolynomial σ R →ₗ[R] MvPolynomial σ R`
- What: The multivariate Hasse derivative `Δ_d`, the `R`-linear map with `Δ_d (a X^k) = binom(k, d) a X^(k - d)` (zero unless `d ≤ k`); over a `ℚ`-algebra it is `(∏ j (d j)!)⁻¹ ∏ j ∂_j^(d j)`.
- Hypotheses: `[CommSemiring R]` (section variable); no other hypotheses.
- Uses from project: `MvPolynomial.hasseCoeff`
- Used by: Roth/HasseDeriv.lean (all lemmas from `hasseDeriv_monomial` to `factorial_smul_hasseDeriv_single`, ~60 occurrences); Roth/CoeffNorm.lean (`abs_coeff_hasseDeriv_le`, `normOne_hasseDeriv_le`, generalised-Wronskian degree/coefficient bounds l.247-265); Roth/GenWronskian.lean (`genWronskian` l.34, `kronHasse` l.146, l.241-245); Roth/Index.lean (l.63, l.70, taylor/index lemmas); Roth/Taylor.lean (l.103

### #3 theorem MvPolynomial.hasseDeriv_monomial (public, Roth/HasseDeriv.lean:66)
- verdict: INHERITED-YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Defining equation of MvPolynomial.hasseDeriv on monomials proved by simp [hasseDeriv] (pure unfolding); it is the multivariate analogue of mathlib's Polynomial.hasseDeriv_monomial and ships with the parent.
- action: Upstream with MvPolynomial.hasseDeriv in a new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, restating the coefficient as (k.choose d : R) per the hasseCoeff report; locally keep as is (used in coeff_hasseDeriv, hasseDeriv_C, hasseDeriv_monomial_mul, Taylor.lean coeff_taylor_monomial_single_add_aux).
- Type: `∀ {σ R : Type*} [CommSemiring R] (d k : σ →₀ ℕ) (a : R), hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a)`
- What: The Hasse derivative `Δ_d` sends `a X^k` to `binom(k, d) a X^(k - d)`, where `binom(k, d) = ∏ j (k j).choose (d j)`; the defining equation of `hasseDeriv` on monomials. Tagged `@[simp]`.
- Hypotheses: `[CommSemiring R]` (section variable); none else.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseCoeff`
- Used by: `MvPolynomial.coeff_hasseDeriv` (Roth/HasseDeriv.lean:94), `MvPolynomial.hasseDeriv_C` (Roth/HasseDeriv.lean:127), private `MvPolynomial.hasseDeriv_monomial_mul` (Roth/HasseDeriv.lean:233), private `coeff_taylor_monomial_single_add_aux` (Roth/Taylor.lean:111, 116); also available as a simp lemma project-wide.

### #4 theorem MvPolynomial.hasseDeriv_apply (public, Roth/HasseDeriv.lean:73)
- verdict: INHERITED-YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Definitional expansion of MvPolynomial.hasseDeriv as a sum over the support (closes by rfl; current proof simp [hasseDeriv, sum_def]); multivariate analogue of mathlib's Polynomial.hasseDeriv_apply, ships with the parent.
- action: Upstream with MvPolynomial.hasseDeriv in a new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, coefficient spelled (k.choose d : R) per the hasseCoeff report; locally keep (used in Roth/CoeffNorm.lean:151 normOne_hasseDeriv_le).
- Type: `∀ {σ R : Type*} [CommSemiring R] (d : σ →₀ ℕ) (P : MvPolynomial σ R), hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k)`
- What: Expands the Hasse derivative `Δ_d P` as the sum, over the monomials `a_k X^k` of `P`, of `binom(k, d) a_k X^(k - d)`.
- Hypotheses: `[CommSemiring R]` (section variable); none else.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseCoeff`
- Used by: `MvPolynomial.normOne_hasseDeriv_le` (Roth/CoeffNorm.lean:151); no other occurrence in `Roth/`.

### #5 theorem MvPolynomial.hasseCoeff_eq_zero_iff (public, Roth/HasseDeriv.lean:80)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The vanishing criterion binom(k,d) = 0 iff not d <= k is the basic API companion of the multi-index binomial (analogue of Nat.choose_eq_zero_iff), absent from mathlib; it should ship with the parent as Finsupp.choose_eq_zero_iff plus the positive forms choose_ne_zero_iff and choose_pos_iff.
- action: Upstream with MvPolynomial.hasseCoeff (as Finsupp.choose) in Mathlib/Data/Nat/Choose/Multinomial.lean or a new Mathlib/Data/Finsupp/Choose.lean, stated as Finsupp.choose_ne_zero_iff (simp-friendly, proof is simp [choose, Nat.choose_ne_zero_iff, Finsupp.le_iff]) with choose_eq_zero_iff and choose_pos_iff derived; locally keep (used in coeff_hasseDeriv, hasseDeriv_C, Taylor.lean l.113).
- Type: `∀ {σ : Type*} (d k : σ →₀ ℕ), hasseCoeff d k = 0 ↔ ¬d ≤ k`
- What: The multi-index binomial coefficient `binom(k, d) = ∏_{j ∈ supp d} (k j).choose (d j)` vanishes exactly when `d ≰ k` (componentwise order).
- Hypotheses: none (the section `[CommSemiring R]` is not included in the statement).
- Uses from project: `MvPolynomial.hasseCoeff`
- Used by: Roth/HasseDeriv.lean: `coeff_hasseDeriv` (l.99), `hasseDeriv_C` (l.127); Roth/Taylor.lean: `coeff_taylor_monomial_single_add_aux` (private, l.113)

### #6 theorem MvPolynomial.coeff_hasseDeriv (public, Roth/HasseDeriv.lean:89)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The coefficient formula [X^e] Δ_d P = binom(e+d, d) [X^(e+d)] P is the main computational API lemma of the multivariate Hasse derivative (multivariate analogue of Polynomial.hasseDeriv_coeff), absent from mathlib; it should ship with the parent with the coefficient spelled (e + d).choose d via Finsupp.choose.
- action: Upstream in the same PR as MvPolynomial.hasseDeriv (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean) restated as ((e + d).choose d : R) * P.coeff (e + d) with Finsupp.choose; locally keep (13 uses in Roth/HasseDeriv.lean and Roth/CoeffNorm.lean:137).
- Type: `∀ {σ R : Type*} [CommSemiring R] (d e : σ →₀ ℕ) (P : MvPolynomial σ R), coeff e (hasseDeriv d P) = ↑(hasseCoeff d (e + d)) * coeff (e + d) P`
- What: The coefficient of `X^e` in `Δ_d P` is `binom(e + d, d)` times the coefficient of `X^(e+d)` in `P`; in particular distinct surviving monomials do not merge under `Δ_d`.
- Hypotheses: `[CommSemiring R]` (section variable); no other hypotheses.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.hasseCoeff_eq_zero_iff`
- Used by: Roth/HasseDeriv.lean: `hasseDeriv_zero_apply` (l.114), `hasseDeriv_map` (l.137), `hasseDeriv_hasseDeriv` (l.178, three rewrites), `pderiv_hasseDeriv` (l.203, two rewrites), `degreeOf_hasseDeriv_le` (l.213), `hasseDeriv_eq_zero_of_degreeOf_lt` (l.222), `uniqueAlgEquiv_hasseDeriv` (l.270); Roth/CoeffNorm.lean: `abs_coeff_hasseDeriv_le` (l.137), which is in turn used in Roth/MainLemma.lean l.468, l.5

### #7 theorem MvPolynomial.hasseCoeff_eq_prod (public, Roth/HasseDeriv.lean:106)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The full-product formula binom(k,d) = prod over all j of binom(k_j,d_j) is the literature definition of the multi-index binomial and the bridge from the support-indexed Finsupp.prod to Finset.prod API; absent from mathlib, it should ship with the parent Finsupp.choose in the mathlib idiom choose_eq_prod_of_support_subset (any finset s containing d.support, mirroring Finsupp.multinomial_eq_of_support_subset) plus the Fintype corollary choose_eq_prod.
- action: Upstream in the Finsupp.choose PR (parent MvPolynomial.hasseCoeff; Mathlib/Data/Nat/Choose/Multinomial.lean or new Mathlib/Data/Finsupp/Choose.lean) as Finsupp.choose_eq_prod_of_support_subset and Finsupp.choose_eq_prod; locally keep (single call site Roth/HasseDeriv.lean:278 in hasseCoeff_le_two_pow).
- Type: `∀ {σ : Type*} [Fintype σ] (d k : σ →₀ ℕ), hasseCoeff d k = ∏ j, (k j).choose (d j)`
- What: Over a finite index type, the multi-index binomial `hasseCoeff d k` (defined as a product over `d.support`) equals the full product `∏_j binom(k_j, d_j)` over all variables.
- Hypotheses: `[Fintype σ]` (finite set of variables); the section `[CommSemiring R]` is not included.
- Uses from project: `MvPolynomial.hasseCoeff`
- Used by: Roth/HasseDeriv.lean: `hasseCoeff_le_two_pow` (l.278). No other use in `Roth/`.

### #8 theorem MvPolynomial.hasseDeriv_zero_apply (public, Roth/HasseDeriv.lean:112)
- verdict: YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Delta_0 P = P is the basic normalisation lemma of the multivariate Hasse derivative (pointwise analogue of mathlib's Polynomial.hasseDeriv_zero'), absent from mathlib, already maximally general (CommSemiring forced by MvPolynomial), and it is the lemma from which the bundled hasseDeriv_zero is proved; it ships unchanged in the parent's PR.
- action: Upstream with MvPolynomial.hasseDeriv (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean) as hasseDeriv_zero_apply beside @[simp] hasseDeriv_zero, proof adjusted to the Finsupp.choose spelling; locally keep (used by hasseDeriv_zero l.121 and Roth/Index.lean:104-105).
- Type: `∀ {σ R : Type*} [CommSemiring R] (P : MvPolynomial σ R), (hasseDeriv 0) P = P`
- What: The Hasse derivative of order zero fixes every polynomial: `Δ_0 P = P`.
- Hypotheses: `[CommSemiring R]` (section variable); no other hypotheses.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`
- Used by: Roth/HasseDeriv.lean: `hasseDeriv_zero` (l.121, `LinearMap.ext hasseDeriv_zero_apply`); Roth/Index.lean: `index_eq_zero_iff` (l.104 and l.105, as a `simpa` argument).

### #9 theorem MvPolynomial.hasseDeriv_zero (public, Roth/HasseDeriv.lean:120)
- verdict: INHERITED-YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Bundled form hasseDeriv 0 = LinearMap.id, proved as pure glue LinearMap.ext hasseDeriv_zero_apply exactly like mathlib's univariate Polynomial.hasseDeriv_zero; ships with the pointwise lemma and the parent operator.
- action: Upstream as @[simp] MvPolynomial.hasseDeriv_zero beside hasseDeriv_zero_apply in the new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean PR of MvPolynomial.hasseDeriv; locally keep (simp lemma, no named call sites).
- Type: `∀ {σ R : Type*} [CommSemiring R], hasseDeriv (0 : σ →₀ ℕ) = (LinearMap.id : MvPolynomial σ R →ₗ[R] MvPolynomial σ R)`
- What: The Hasse derivative of order zero is the identity linear map: `Δ_0 = id`.
- Hypotheses: `[CommSemiring R]` (section variable); none else.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_zero_apply`
- Used by: no explicit call site in `Roth/` (`grep -rn hasseDeriv_zero Roth/` finds only the declaration and the docstring of `hasseDeriv_zero_apply`); it is `@[simp]`, so it may fire implicitly in `simp` calls on `hasseDeriv 0 _` (e.g. the `simpa` calls in Roth/Index.lean:104-105, `index_eq_zero_iff`).

### #10 theorem MvPolynomial.hasseDeriv_C (public, Roth/HasseDeriv.lean:126)
- verdict: YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Delta_d (C a) = 0 for d ne 0 is the multivariate analogue of mathlib's Polynomial.hasseDeriv_C, absent from mathlib (no MvPolynomial Hasse derivative), maximally general (d ne 0 necessary, CommSemiring forced by MvPolynomial); ships unchanged with the parent operator, ideally beside a companion hasseDeriv_monomial_of_not_le.
- action: Upstream with MvPolynomial.hasseDeriv to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (proof via the Finsupp.choose spelling), optionally adding hasseDeriv_monomial_of_not_le and hasseDeriv_one (evidence file); locally keep (used at Roth/Taylor.lean:127).
- Type: `∀ {σ R : Type*} [CommSemiring R] {d : σ →₀ ℕ}, d ≠ 0 → ∀ (a : R), (hasseDeriv d) (C a) = 0`
- What: A multivariate Hasse derivative of nonzero order annihilates constants: `Δ_d (C a) = 0` for `d ≠ 0`.
- Hypotheses: `hd : d ≠ 0` (necessary: `Δ_0 = id`); `[CommSemiring R]` (section variable).
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.hasseCoeff_eq_zero_iff` (and implicitly `MvPolynomial.hasseCoeff`)
- Used by: Roth/Taylor.lean:127 (`coeff_taylor_monomial_aux`, zero case of the `Finsupp.induction`: `simp [← C_apply, hasseDeriv_C hd, hd.symm]`).

### #11 theorem MvPolynomial.hasseDeriv_map (public, Roth/HasseDeriv.lean:134)
- verdict: YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Delta_d commutes with coefficient change along any ring hom; it is the multivariate counterpart of mathlib's Polynomial.hasseDeriv_map and the Hasse analogue of MvPolynomial.pderiv_map, absent from mathlib (no MvPolynomial Hasse derivative), maximally general (RingHom of CommSemirings is exactly what MvPolynomial.map takes); should ship tagged simp like the univariate one.
- action: Upstream with MvPolynomial.hasseDeriv to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, adding the simp attribute (safe, evidence file); locally keep (call sites Roth/MainLemma.lean:409,489,492,495, Roth/Theta.lean:524,580, Roth/Separation.lean:533).
- Type: `∀ {σ R : Type*} [CommSemiring R] {S : Type*} [CommSemiring S] (f : R →+* S) (d : σ →₀ ℕ) (P : MvPolynomial σ R), (hasseDeriv d) ((map f) P) = (map f) ((hasseDeriv d) P)`
- What: The multivariate Hasse derivative commutes with changing coefficients along a ring homomorphism: `Δ_d (f_* P) = f_* (Δ_d P)`; used to pass between `ℤ`, `ℚ` and `ℝ` coefficients.
- Hypotheses: `f : R →+* S` between commutative semirings (forced by `MvPolynomial.map`); no propositional hypotheses.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv` (and implicitly `MvPolynomial.hasseCoeff`)
- Used by: Roth/MainLemma.lean:409 (`eval_hasseDeriv_sub_eq_zero`), Roth/MainLemma.lean:489, 492, 495 (`exists_hasseDeriv_index_eval_bound_aux`), Roth/Theta.lean:524 (`mapped_det_ne_zero_aux`), Roth/Theta.lean:580 (`index_le_lem6`), Roth/Separation.lean:533 (`exists_rat_factors_det_hasseDeriv_aux`).

### #12 theorem MvPolynomial.hasseDeriv_rename (public, Roth/HasseDeriv.lean:143)
- verdict: YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Delta_d commutes with injective renaming of variables when the multi-index is transported by mapDomain; it is the Hasse analogue of mathlib's MvPolynomial.pderiv_rename, absent from mathlib (no MvPolynomial Hasse derivative), and maximally general (injectivity is necessary, counterexample compiled).
- action: Upstream with MvPolynomial.hasseDeriv to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, stated exactly as now (mirrors pderiv_rename); locally keep (call site Roth/Separation.lean:165 in hasseDeriv_rename_mul_aeval).
- Type: `∀ {σ R : Type*} [CommSemiring R] {τ : Type*} {f : σ → τ}, Function.Injective f → ∀ (d : σ →₀ ℕ) (P : MvPolynomial σ R), (hasseDeriv (Finsupp.mapDomain f d)) ((rename f) P) = (rename f) ((hasseDeriv d) P)`
- What: For an injective relabelling `f : σ → τ` of variables, the Hasse derivative of order `f_* d` of the renamed polynomial is the renaming of `Δ_d P`: `Δ_{f_* d} ∘ rename f = rename f ∘ Δ_d`. In particular an operator in a subset of the variables acts on a polynomial that only involves those variables as it did before the embedding.
- Hypotheses: `hf : Function.Injective f` (necessary; see evidence item 3); `[CommSemiring R]`.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv_monomial` (via `simp`)
- Used by: Roth/Separation.lean:165 (`hasseDeriv_rename_mul_aeval`, with `f = some : τ → Option τ`), which in turn is used at Roth/Separation.lean:365.

### #13 lemma MvPolynomial.hasseCoeff_mul_hasseCoeff (private, Roth/HasseDeriv.lean:153)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private multi-index form of Nat.choose_mul (binom(f+d,d) binom(f+d+e,e) = binom(d+e,d) binom(f+d+e,d+e)), the combinatorial core of hasseDeriv_hasseDeriv and hasseCoeff_mul_succ; mathlib has only the scalar Nat.choose_mul and no multi-index binomial.
- action: Keep as private helper (call sites Roth/HasseDeriv.lean:179 hasseDeriv_hasseDeriv and :195 hasseCoeff_mul_succ); when upstreaming hasseCoeff as Finsupp.choose, publish it there as Finsupp.choose_mul in the Nat.choose_mul shape.
- Type: `∀ {σ : Type*} (f d e : σ →₀ ℕ), hasseCoeff d (f + d) * hasseCoeff e (f + d + e) = hasseCoeff d (d + e) * hasseCoeff (d + e) (f + (d + e))`
- What: Multi-index "subset-of-a-subset" binomial identity: for multi-indices f, d, e, binom(f+d, d) · binom(f+d+e, e) = binom(d+e, d) · binom(f+d+e, d+e), with binom(k, d) = ∏_j binom(k_j, d_j). It is the coefficient identity behind the Hasse-derivative composition rule Δ_d Δ_e = binom(d+e, d) Δ_{d+e}.
- Hypotheses: none beyond the types (`σ` arbitrary; section `[CommSemiring R]` is not included since R does not occur).
- Uses from project: `MvPolynomial.hasseCoeff`
- Used by: Roth/HasseDeriv.lean: `hasseDeriv_hasseDeriv` (l.179, `rw`), `hasseCoeff_mul_succ` (l.195, private, `simpa using hasseCoeff_mul_hasseCoeff e (Finsupp.single j 1) d`). No other use in `Roth/` (grep over `Roth/` and `Roth.lean`).

### #14 theorem MvPolynomial.hasseDeriv_hasseDeriv (public, Roth/HasseDeriv.lean:175)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The iterativity/composition rule Delta_d Delta_e = binom(d+e,d) Delta_(d+e) is the standard defining property of (iterative) Hasse derivatives and is absent from mathlib for MvPolynomial; it should ship in the operator normal form of Polynomial.hasseDeriv_comp (LinearMap comp, Nat-smul, Finsupp.choose coefficient) with the pointwise form as a corollary.
- action: Upstream with the parent into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as `hasseDeriv_comp : hasseDeriv d ∘ₗ hasseDeriv e = (d + e).choose d • hasseDeriv (d + e)` plus pointwise `hasseDeriv_hasseDeriv` corollary (verified in evidence variants.lean) and public Finsupp.choose_mul; locally keep as is (callers Roth/Index.lean:113, Roth/HasseDeriv.lean:187).
- Type: `∀ {σ R : Type*} [CommSemiring R] (d e : σ →₀ ℕ) (P : MvPolynomial σ R), hasseDeriv d (hasseDeriv e P) = (↑(hasseCoeff d (d + e)) : R) • hasseDeriv (d + e) P`
- What: Composition rule for multivariate Hasse derivatives: `Δ_d Δ_e P = binom(d+e, d) · Δ_{d+e} P`, with the multi-index binomial `binom(d+e,d) = ∏_j binom(d_j+e_j, d_j)`.
- Hypotheses: none (section variable `[CommSemiring R]`).
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff_mul_hasseCoeff` (private)
- Used by: Roth/Index.lean:113 (`index_sub_weight_le_index_hasseDeriv`, `rw [hasseDeriv_hasseDeriv, smul_eq_C_mul, ...] at hi`); Roth/HasseDeriv.lean:187 (`hasseDeriv_hasseDeriv_of_disjoint`, which in turn is used at Roth/Separation.lean:156 in `hasseDeriv_rename_mul_aeval`). No other use in `Roth/`.

### #15 theorem MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint (public, Roth/HasseDeriv.lean:185)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Disjoint-support special case Delta_d Delta_e = Delta_(d+e) of the Hasse composition law (binomial factor is 1 exactly when supports are disjoint, verified sharp); absent from mathlib, not simp-composable, and should ship next to the parent's operator-form hasseDeriv_comp as hasseDeriv_comp_of_disjoint with this pointwise lemma as corollary.
- action: Upstream with MvPolynomial.hasseDeriv_hasseDeriv into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, adding operator form `hasseDeriv d ∘ₗ hasseDeriv e = hasseDeriv (d + e)` (verified in evidence variants.lean) and an order-form `Disjoint d e` variant via Finsupp.disjoint_iff; locally keep as is (caller Roth/Separation.lean:156).
- Type: `∀ {σ R : Type*} [CommSemiring R] {d e : σ →₀ ℕ}, Disjoint d.support e.support → ∀ (P : MvPolynomial σ R), hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P`
- What: If the multi-indices `d` and `e` involve disjoint sets of variables, then `Δ_d Δ_e = Δ_{d+e}` (the binomial factor of the composition law is `1`).
- Hypotheses: `h : Disjoint d.support e.support`.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv`, `MvPolynomial.hasseCoeff`
- Used by: Roth/Separation.lean:156 (`hasseDeriv_rename_mul_aeval`, `rw [← hasseDeriv_hasseDeriv_of_disjoint hdisj, ...]`). No other use in `Roth/` (also referenced in the docstring of `hasseDeriv_hasseDeriv`, Roth/HasseDeriv.lean:172).

### #16 lemma MvPolynomial.hasseCoeff_mul_succ (private, Roth/HasseDeriv.lean:191)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private multi-index absorption identity binom(n,d)(e_j+1) = (d_j+1) binom(n,d+e_j) with n = e+e_j+d, a one-line specialisation of hasseCoeff_mul_hasseCoeff used only by pderiv_hasseDeriv; mathlib has only the scalar Nat.choose_succ_right_eq.
- action: Keep as private helper for its single call site Roth/HasseDeriv.lean:205 (pderiv_hasseDeriv); if hasseCoeff is upstreamed as Finsupp.choose, restate it there as a multi-index analogue of Nat.choose_succ_right_eq.
- Type: `∀ {σ : Type*} (j : σ) (d e : σ →₀ ℕ), hasseCoeff d (e + Finsupp.single j 1 + d) * (e j + 1) = (d j + 1) * hasseCoeff (d + Finsupp.single j 1) (e + Finsupp.single j 1 + d)`
- What: Multi-index absorption identity for the binomial coefficient binom(k, d) = ∏_i binom(k_i, d_i): with n = e + e_j + d (e_j the j-th unit multi-index), binom(n, d) · (e_j + 1) = (d_j + 1) · binom(n, d + e_j). Only the j-th factor changes; it is the scalar identity C(N, a)·(N - a) = (a+1)·C(N, a+1). It is the coefficient identity behind ∂_j Δ_d = (d_j + 1) Δ_{d + e_j}.
- Hypotheses: none beyond the types (σ arbitrary; R does not occur).
- Uses from project: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_mul_hasseCoeff` (private)
- Used by: Roth/HasseDeriv.lean: `pderiv_hasseDeriv` (l.200, `rw` at l.205) only (grep over `Roth/` and `Roth.lean`). Transitively: `factorial_smul_hasseDeriv_single` (Roth/HasseDeriv.lean:286, uses `pderiv_hasseDeriv` at l.291) and `derivative_kronHasse_aux` (Roth/GenWronskian.lean:153, uses `pderiv_hasseDeriv` at l.159).

### #17 theorem MvPolynomial.pderiv_hasseDeriv (public, Roth/HasseDeriv.lean:200)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The identity d_j Delta_d = (d_j+1) Delta_(d+e_j) is genuine multivariate Hasse-derivative API absent from mathlib, but mathlib's univariate design factors it as hasseDeriv_one plus hasseDeriv_comp, so it should ship as an operator-form corollary of a new hasseDeriv_single_one and the composition law (both verified in evidence).
- action: Upstream with the parent into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as `hasseDeriv_single_one : hasseDeriv (single j 1) = (pderiv j).toLinearMap` (coefficient proof, verified) followed by operator form `(pderiv j).toLinearMap ∘ₗ hasseDeriv d = (d j + 1) • hasseDeriv (d + single j 1)` and the pointwise lemma as corollary of hasseDeriv_comp; locally keep as is (callers Roth/GenWronskian.lean:159, Roth/HasseDeriv.lean:291).
- Type: `∀ {σ R : Type*} [CommSemiring R] (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R), (pderiv j) (hasseDeriv d P) = (↑(d j + 1) : R) • hasseDeriv (d + Finsupp.single j 1) P`
- What: A partial derivative of a multivariate Hasse derivative: `∂_j Δ_d P = (d_j + 1) · Δ_{d + e_j} P`.
- Hypotheses: none (section variable `[CommSemiring R]`).
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff_mul_succ` (private; via it `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_mul_hasseCoeff`)
- Used by: Roth/GenWronskian.lean:159 (`derivative_kronHasse_aux`, in a `simp [..., pderiv_hasseDeriv, ...]` set); Roth/HasseDeriv.lean:291 (`factorial_smul_hasseDeriv_single`, induction step `rw [..., pderiv_hasseDeriv, ...]`). No other use in `Roth/`.

### #18 theorem MvPolynomial.degreeOf_hasseDeriv_le (public, Roth/HasseDeriv.lean:210)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Basic degree bound for the multivariate Hasse derivative, absent from mathlib with the parent operator; mathlib's univariate normal form is the sharp natDegree_hasseDeriv_le (deg Delta_n p le deg p - n), so upstream should state the sharp per-variable bound degreeOf j (Delta_d P) le degreeOf j P - d j (verified, same 3-line proof) plus a totalDegree companion (verified).
- action: Upstream with the parent into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as `degreeOf_hasseDeriv_le : degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j` and `totalDegree_hasseDeriv_le : totalDegree (hasseDeriv d P) ≤ totalDegree P - d.degree`; locally keep the weak form (callers Roth/MainLemma.lean:465,467,491,504 and Roth/CoeffNorm.lean:253 need only the weak bound) or derive it from the sharp one by `.trans tsub_le_self`.
- Type: `∀ {σ R : Type*} [CommSemiring R] (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R), degreeOf j (hasseDeriv d P) ≤ degreeOf j P`
- What: A Hasse derivative `Δ_d` does not increase the degree of a polynomial in any variable `x_j`.
- Hypotheses: none (section variable `[CommSemiring R]`).
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`
- Used by: Roth/MainLemma.lean:465, :467 (`abs_eval_iterated_hasseDeriv_lt_aux`), :491 (`exists_hasseDeriv_index_eval_bound_aux`), :504 (`abs_coeff_diag_hasseDeriv_modByMonic_le_aux`); Roth/CoeffNorm.lean:253 (`degreeOf_det_hasseDeriv_le`). No other use in `Roth/`.

### #19 theorem MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt (public, Roth/HasseDeriv.lean:219)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Multivariate analogue of mathlib's Polynomial.hasseDeriv_eq_zero_of_lt_natDegree, absent with the parent operator; the content is the support criterion (no monomial of P dominates d) which compiles in 4 lines and gives both this per-variable form and a totalDegree form as one-line corollaries.
- action: Upstream with the parent into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as core `hasseDeriv_eq_zero_of_forall_not_le` plus corollaries `hasseDeriv_eq_zero_of_degreeOf_lt` (this statement, unchanged) and `hasseDeriv_eq_zero_of_totalDegree_lt`; locally keep as is (callers Roth/Taylor.lean:173,207 and Roth/MainLemma.lean:425 need no change).
- Type: `∀ {σ R : Type*} [CommSemiring R] {j : σ} {d : σ →₀ ℕ} {P : MvPolynomial σ R}, degreeOf j P < d j → hasseDeriv d P = 0`
- What: If the order `d j` of the Hasse derivative `Δ_d` in some variable `x_j` exceeds the degree of `P` in `x_j`, then `Δ_d P = 0`.
- Hypotheses: `h : degreeOf j P < d j` (section variable `[CommSemiring R]`).
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`
- Used by: Roth/Taylor.lean:173 (`degreeOf_taylor_le`), Roth/Taylor.lean:207 (`eq_sum_box_hasseDeriv`), Roth/MainLemma.lean:425 (`le_index_of_forall_eval_eq_zero`). No other use in `Roth/`.

### #20 lemma MvPolynomial.hasseDeriv_monomial_mul (private, Roth/HasseDeriv.lean:225)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private monomial case of hasseDeriv_mul_of_degreeOf_eq_zero (a monomial X^a c with a_j = 0 on supp d commutes with Δ_d), proved by induction_on' on g; single call site; mathlib has no multivariate Hasse derivative.
- action: Keep as private helper for its single call site hasseDeriv_mul_of_degreeOf_eq_zero (Roth/HasseDeriv.lean:246); upstream it together with that public lemma if MvPolynomial.hasseDeriv goes to Mathlib/Algebra/MvPolynomial/.
- Type: `∀ {σ R : Type*} [CommSemiring R] {d a : σ →₀ ℕ}, (∀ j ∈ d.support, a j = 0) → ∀ (c : R) (g : MvPolynomial σ R), hasseDeriv d (monomial a c * g) = monomial a c * hasseDeriv d g`
- What: If the exponent vector a vanishes on every variable that the multi-index d differentiates, then the monomial c X^a passes through the Hasse derivative: Δ_d (c X^a · g) = c X^a · Δ_d g. This is the monomial case of the "constants w.r.t. the differentiated variables pull out" rule.
- Hypotheses: `ha : ∀ j ∈ d.support, a j = 0` (needed: otherwise the binomial factor and exponent change); `R` a commutative semiring (file-wide variable).
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.hasseCoeff`
- Used by: Roth/HasseDeriv.lean: `hasseDeriv_mul_of_degreeOf_eq_zero` (l.243, used at l.246) only (grep over `Roth/` and `Roth.lean`). Transitively: Roth/Separation.lean `hasseDeriv_rename_mul_aeval` (l.146, uses `hasseDeriv_mul_of_degreeOf_eq_zero` at l.157 and l.161).

### #21 theorem MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero (public, Roth/HasseDeriv.lean:243)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Special case of the multivariate Leibniz rule for Hasse derivatives (absent from mathlib, which has only univariate Polynomial.hasseDeriv_mul); the Leibniz rule and a strictly weaker hypothesis form (Delta_a f = 0 for 0 ne a le d) both compile in a few lines, with this statement as a one-line corollary.
- action: Upstream with the parent into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as `hasseDeriv_mul` (Leibniz) + `hasseDeriv_mul_of_hasseDeriv_eq_zero` + this lemma as corollary (drops private hasseDeriv_monomial_mul); locally keep as is (callers Roth/Separation.lean:157,161 need no change).
- Type: `∀ {σ R : Type*} [CommSemiring R] {d : σ →₀ ℕ} {f g : MvPolynomial σ R}, (∀ j ∈ d.support, degreeOf j f = 0) → hasseDeriv d (f * g) = f * hasseDeriv d g`
- What: If `f` does not involve any variable that `Δ_d` differentiates (degree 0 in every `x_j` with `d j ≠ 0`), then `f` passes through the Hasse derivative: `Δ_d (f g) = f · Δ_d g`.
- Hypotheses: `hf : ∀ j ∈ d.support, degreeOf j f = 0` (equivalently `Disjoint f.vars d.support`); section variable `[CommSemiring R]`.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial_mul` (private)
- Used by: Roth/Separation.lean:157 and Roth/Separation.lean:161 (both in `hasseDeriv_rename_mul_aeval`, l.146). No other use in `Roth/`.

### #22 theorem MvPolynomial.hasseDeriv_single_aeval_X (public, Roth/HasseDeriv.lean:253)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Bridge Delta_{n e_j} (f(X_j)) = (D^(n) f)(X_j) between the multivariate and univariate Hasse derivatives, absent from mathlib (which lacks even the first-order pderiv analogue for Polynomial.toMvPolynomial); a strictly more general form for arbitrary multi-index d compiles, and the statement should be phrased with mathlib's Polynomial.toMvPolynomial.
- action: Upstream with the parent to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as `hasseDeriv_toMvPolynomial` (general d, evidence bridge.lean) plus this single-index form as corollary stated via Polynomial.toMvPolynomial; locally keep as is (caller Roth/Separation.lean:160 rewrites with the aeval form).
- Type: `∀ {σ R : Type*} [CommSemiring R] (j : σ) (n : ℕ) (f : Polynomial R), hasseDeriv (Finsupp.single j n) (Polynomial.aeval (X j : MvPolynomial σ R) f) = Polynomial.aeval (X j : MvPolynomial σ R) (Polynomial.hasseDeriv n f)`
- What: The multivariate Hasse derivative `Δ_{n e_j}` applied to a polynomial `f(x_j)` in the single variable `x_j` is the univariate Hasse derivative `D^(n) f`, evaluated at `x_j`.
- Hypotheses: none beyond section variables `[CommSemiring R]`.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseCoeff` (unfolded in simp; `hasseDeriv_monomial`/`hasseDeriv_apply` as simp lemmas)
- Used by: Roth/Separation.lean:160 (in `hasseDeriv_rename_mul_aeval`, l.146, `rw` chain). Mentioned in Roth/HasseDeriv.lean:36 (module docstring). No other use in `Roth/`.

### #23 theorem MvPolynomial.uniqueAlgEquiv_hasseDeriv (public, Roth/HasseDeriv.lean:266)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: One-variable bridge uniqueAlgEquiv (Delta_{n e} P) = D^(n) (uniqueAlgEquiv P) between the multivariate and univariate Hasse derivatives, absent from mathlib (which lacks even the pderiv/derivative analogue for uniqueAlgEquiv); it should be stated for an arbitrary multi-index d with D^(d default), a verified syntactic generalisation that removes the caller's Finsupp.unique_single rewrite.
- action: Upstream with the parent to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean in the general-d form (evidence bridge.lean item 1), plus the linear-map form; locally optional: restate with d and drop the Finsupp.unique_single rewrite at Roth/Index.lean:239.
- Type: `∀ {σ R : Type*} [CommSemiring R] [Unique σ] (n : ℕ) (P : MvPolynomial σ R), uniqueAlgEquiv R σ (hasseDeriv (Finsupp.single default n) P) = Polynomial.hasseDeriv n (uniqueAlgEquiv R σ P)`
- What: When `σ` has a single element, mathlib's algebra isomorphism `MvPolynomial σ R ≃ₐ[R] R[X]` carries the multivariate Hasse derivative `Δ_{n e}` to the univariate Hasse derivative `D^(n)`.
- Hypotheses: `[Unique σ]` (needed for `uniqueAlgEquiv`), section variable `[CommSemiring R]`.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff` (unfolded in simp)
- Used by: Roth/Index.lean:239 (in `index_unique`, l.234, `rw [Polynomial.taylor_coeff, ← uniqueAlgEquiv_hasseDeriv, ← Finsupp.unique_single d]`). Mentioned in Roth/HasseDeriv.lean:36 (module docstring). No other use in `Roth/`.

### #24 theorem MvPolynomial.hasseCoeff_le_two_pow (public, Roth/HasseDeriv.lean:276)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The multi-index analogue of Nat.choose_le_two_pow is missing from mathlib and is the natural basic bound for the proposed Finsupp.choose; but the box hypothesis k ≤ r and Fintype σ are artefacts of the call sites, and the verified general form is binom(k,d) ≤ 2 ^ k.degree (no Fintype, no r), from which the current form is a two-line corollary.
- action: Upstream with the Finsupp.choose PR (parent MvPolynomial.hasseCoeff; Mathlib/Data/Nat/Choose/Multinomial.lean or new Mathlib/Data/Finsupp/Choose.lean) as Finsupp.choose_le_two_pow_degree (k d) : k.choose d ≤ 2 ^ k.degree; locally optionally add hasseCoeff_le_two_pow_degree and derive this lemma from it (call sites Roth/CoeffNorm.lean:140 and :157 unchanged).
- Type: `∀ {σ : Type*} [Fintype σ] {d k : σ →₀ ℕ} {r : σ → ℕ}, (∀ j, k j ≤ r j) → hasseCoeff d k ≤ 2 ^ ∑ j, r j`
- What: On the box `k ≤ r` (componentwise), the multi-index binomial coefficient `binom(k, d) = ∏_j binom(k_j, d_j)` is at most `2^(r_1 + ⋯ + r_m)`.
- Hypotheses: `[Fintype σ]` (finitely many variables); `hk : ∀ j, k j ≤ r j` (the exponent lies in the degree box `r`). The section `[CommSemiring R]` is not included.
- Uses from project: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_eq_prod`
- Used by: Roth/CoeffNorm.lean: `abs_coeff_hasseDeriv_le` (l.140), `normOne_hasseDeriv_le` (l.157). No other use in `Roth/`.

### #25 theorem MvPolynomial.factorial_smul_hasseDeriv_single (public, Roth/HasseDeriv.lean:286)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Multivariate analogue of mathlib's Polynomial.factorial_smul_hasseDeriv (n! Delta_(n e_j) = d_j^n), absent from mathlib which has no multivariate Hasse derivative; a strictly more general form for an arbitrary base multi-index d (d_j^n Delta_d = n! C(d_j+n,n) Delta_(d+n e_j)) compiles and the lemma should also be offered in mathlib's operator (coe-of-smul = iterate) shape.
- action: Upstream with the parent into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as `iterate_pderiv_hasseDeriv` (general d, evidence general.lean) plus `factorial_smul_hasseDeriv_single` in operator form as the d = 0 corollary; locally keep as is (no code callers, only the module docstring at Roth/HasseDeriv.lean:35).
- Type: `∀ {σ R : Type*} [CommSemiring R] (j : σ) (n : ℕ) (P : MvPolynomial σ R), (n ! : R) • hasseDeriv (Finsupp.single j n) P = (⇑(pderiv j))^[n] P`
- What: `n! · Δ_{n e_j} P = ∂_j^n P`: the `n`-th iterate of the partial derivative in the variable `x_j` equals `n!` times the Hasse derivative of order `n e_j`. Over a `ℚ`-algebra this identifies `Δ_{n e_j}` with `(1/n!) ∂_j^n`.
- Hypotheses: none beyond section variables `[CommSemiring R]`.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.pderiv_hasseDeriv`, `MvPolynomial.hasseDeriv_zero_apply` (via `simp` in the zero case)
- Used by: unused in project (no code callers; `grep -rn factorial_smul_hasseDeriv_single Roth/` finds only the declaration and the module docstring `Roth/HasseDeriv.lean:35`).

### #26 def Roth.box (public, Roth/Box.lean:47)
- verdict: NO-mathlib-has-it | cost: MODERATE | junk: REPLACE
- rationale: box r is exactly mathlib's interval Finset.Iic (Finsupp.equivFunOnFinite.symm r) (equivalently Finset.Icc 0 _) in the locally finite order on σ →₀ ℕ, with membership by Finset.mem_Iic and cardinality by Finsupp.card_Iic plus Nat.card_Iic (all verified in evidence).
- action: Redefine Roth.box r := Finset.Iic (Finsupp.equivFunOnFinite.symm r) (or inline that at the call sites in Roth/Lattice.lean, Roth/MainLemma.lean, Roth/Main.lean, Roth/Taylor.lean, Roth/CoeffNorm.lean), reproving mem_box/card_box from Finset.mem_Iic and Finsupp.card_Iic and adding a piFinset bridge for Roth/CoeffNorm.lean:216; do not upstream.
- Type: `{σ : Type*} → [Fintype σ] → [DecidableEq σ] → (r : σ → ℕ) → Finset (σ →₀ ℕ)`
- What: The finite set of multi-indices `d : σ →₀ ℕ` with `d j ≤ r j` for every `j` (the box `∏ j [0, r j]` of exponent vectors).
- Hypotheses: `[Fintype σ]` (finite variable set), `[DecidableEq σ]` (needed by `Fintype.piFinset`).
- Uses from project: `[]`
- Used by: Roth/Box.lean: `mem_box` (l.51), `card_box` (l.57), `card_le_card_box` (l.66-68, via `mem_box`/`card_box`), docstring of `weight_le_card` (l.100); Roth/Taylor.lean: l.199, 200, 206, 219 (Taylor expansion over the box); Roth/CoeffNorm.lean: l.215, 216 (unfolds `box` to use `Finset.prod_univ_sum`), 234, 236; Roth/Main.lean: l.392, 404, 405; Roth/MainLemma.lean: l.570, 608, 616; Roth/Lattice.lean: l.

### #27 theorem Roth.mem_box (public, Roth/Box.lean:51)
- verdict: NO-mathlib-has-it | cost: CHEAP | junk: KEEP
- rationale: Re-aimed at the parent's mathlib form Finset.Iic (Finsupp.equivFunOnFinite.symm r), the statement is exactly Finset.mem_Iic.trans Finsupp.le_def (verified in evidence), so mathlib already has it.
- action: Keep as a local simp-style API lemma for Roth.box (9 call sites in Taylor, CoeffNorm, Main, MainLemma, Lattice, Box); if box is redefined via Finset.Iic, reprove it as Finset.mem_Iic.trans Finsupp.le_def; do not upstream.
- Type: `{σ : Type*} [Fintype σ] [DecidableEq σ] {r : σ → ℕ} {d : σ →₀ ℕ} : d ∈ Roth.box r ↔ ∀ j, d j ≤ r j`
- What: A multi-index `d` lies in the box `box r` iff it is bounded coordinatewise by `r`.
- Hypotheses: none beyond `[Fintype σ] [DecidableEq σ]` (section variables required by `box`).
- Uses from project: `Roth.box`
- Used by: Roth/Box.lean:68 (`card_le_card_box`); Roth/Taylor.lean:206; Roth/CoeffNorm.lean:236; Roth/Main.lean:404; Roth/MainLemma.lean:616; Roth/Lattice.lean:109, 117, 124, 138.

### #28 theorem Roth.card_box (public, Roth/Box.lean:57)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: Re-aimed at the parent's mathlib form Finset.Iic, the count is Pi.card_Iic plus Nat.card_Iic (or Finsupp.card_Iic plus Nat.card_Iic plus Finset.prod_subset), and for the current def it is card_map plus card_piFinset plus card_range; all verified in evidence, nothing new for mathlib.
- action: Keep as the local cardinality lemma of Roth.box (used at Roth/Box.lean:68, Roth/Main.lean:405, Roth/Lattice.lean:163); if box is redefined via Finset.Iic, reprove via Finsupp.card_Iic, Nat.card_Iic and Finset.prod_subset; do not upstream.
- Type: `{σ : Type*} [Fintype σ] [DecidableEq σ] (r : σ → ℕ) : (Roth.box r).card = ∏ j, (r j + 1)`
- What: The box of multi-indices `{d : σ →₀ ℕ : ∀ j, d j ≤ r j}` has `∏ j (r j + 1)` elements.
- Hypotheses: none beyond the section variables `[Fintype σ] [DecidableEq σ]` (required by `box`).
- Uses from project: `Roth.box`
- Used by: Roth/Box.lean:68 (`card_le_card_box`, which is in turn used at Roth/MainLemma.lean:506 and Roth/CoeffNorm.lean:264); Roth/Main.lean:405 (`rw [Finset.sum_const, card_box, nsmul_eq_mul]`); Roth/Lattice.lean:163 (`simp [card_box]`).

### #29 theorem Roth.card_le_card_box (public, Roth/Box.lean:65)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: Re-aimed at Finset.Iic the statement is Finset.card_le_card of s ⊆ Iic r followed by the card_Iic count (Pi.card_Iic or Finsupp.card_Iic plus Nat.card_Iic), and for the current def it is card_le_card plus mem_box plus card_box; all compiled in evidence, nothing new for mathlib.
- action: Keep locally as the convenience bound used at Roth/MainLemma.lean:506 and Roth/CoeffNorm.lean:264 (it spares both sites the box detour); if Roth.box is redefined as Finset.Iic, keep the proof as card_le_card plus mem_Iic plus card_box; do not upstream.
- Type: `{σ : Type*} [Fintype σ] {r : σ → ℕ} {s : Finset (σ →₀ ℕ)} (hs : ∀ d ∈ s, ∀ j, d j ≤ r j) : s.card ≤ ∏ j, (r j + 1)`
- What: A finset of multi-indices that are coordinatewise bounded by `r` has at most `∏ j (r j + 1)` elements (it sits inside the box `box r`).
- Hypotheses: `hs` — every element of `s` is bounded by `r` coordinatewise. Section variable `[Fintype σ]` (the `[DecidableEq σ]` is omitted and recovered by `classical`).
- Uses from project: `Roth.mem_box`, `Roth.card_box` (and through them `Roth.box`)
- Used by: Roth/MainLemma.lean:506 (`abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, bound on `#(hasseDeriv j P).support`); Roth/CoeffNorm.lean:264 (`abs_coeff_det_hasseDeriv_le`, Lemma 3, bound on `#P.support`).

### #30 def Roth.weight (public, Roth/Box.lean:71)
- verdict: NO-mathlib-has-it | cost: MODERATE | junk: REPLACE
- rationale: weight r d = sum_j d j / r j is exactly mathlib's Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d (an AddMonoidHom), verified for all r including r j = 0; weight_zero, weight_add, weight_single become map_zero, map_add, Finsupp.weight_single.
- action: Redefine Roth.weight r := Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) (keeping the name) with a bridge lemma weight_eq_sum, reprove the Box.lean API via map_add/map_zero/Finsupp.weight_single, and repoint the unfolding sites Index.lean:133,245,249, Theta.lean:500,502, Main.lean:366 at the bridge; do not upstream.
- Type: `{σ : Type*} [Fintype σ] (r : σ → ℕ) (d : σ →₀ ℕ) : ℝ`
- What: The real weight `∑ j, d j / r j` of a multi-index `d` with respect to the parameters `r`; the index of a polynomial (`Roth.index`) is the least weight of a nonvanishing Taylor coefficient.
- Hypotheses: section variable `[Fintype σ]` (the `[DecidableEq σ]` section variable is not included in the elaborated def).
- Uses from project: `[]`
- Used by: Roth/Box.lean (API: `weight_nonneg` 75, `weight_zero` 80, `weight_add` 85, `weight_eq_zero_iff` 91, `weight_single` 96, `weight_le_card` 103, `weight_mul_left` 110, `weight_le_degree_div` 118, `weight_mapDomain` 127); Roth/Index.lean:59 (definition of `Roth.index`), 70, 71, 77, 80, 86, 111, 131, 133, 202, 203, 245, 249; Roth/MainLemma.lean:421, 456, 555, 570, 609; Roth/Theta.lean:380, 496, 500, 50

### #31 theorem Roth.weight_nonneg (public, Roth/Box.lean:75)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: Re-aimed at Finsupp.weight (parent is NO-mathlib-has-it), mathlib has no Finsupp.weight_nonneg, but it is the one-call composition Finsupp.sum_nonneg fun i _ ↦ nsmul_nonneg (hw i) _ (zero_le when canonically ordered); the project form is itself one call (Fintype.sum_nonneg + positivity).
- action: Keep as a project-local API lemma for its 3 call sites (Index.lean:94, Theta.lean:395, Lattice.lean:145); if Roth.weight is refactored onto Finsupp.weight, reprove it as Finsupp.sum_nonneg fun j _ ↦ nsmul_nonneg (by positivity) _; no mathlib PR.
- Type: `{σ : Type*} [Fintype σ] (r : σ → ℕ) (d : σ →₀ ℕ) : 0 ≤ Roth.weight r d`
- What: The weight `∑ j, d j / r j` of any multi-index is nonnegative.
- Hypotheses: none beyond the section variable `[Fintype σ]` (needed by `Roth.weight`).
- Uses from project: `Roth.weight`
- Used by: Roth/Index.lean:94 (`index_nonneg`, via `Real.sInf_nonneg`); Roth/Theta.lean:395 (`(weight_nonneg _ _).trans h2`); Roth/Lattice.lean:145 (`linarith [weight_nonneg r d]` in private `filter_weight_le_eq_empty`).

### #32 theorem Roth.weight_zero (public, Roth/Box.lean:80)
- verdict: NO-mathlib-has-it | cost: n/a | junk: KEEP
- rationale: Re-aimed at Finsupp.weight (parent Roth.weight is NO-mathlib-has-it), the analogue Finsupp.weight w 0 = 0 is mathlib's generic simp lemma map_zero (Finsupp.weight w is an AddMonoidHom); the project form is a one-line simp unfolding with no explicit call sites (only a @[simp] lemma).
- action: Keep as the @[simp] companion of Roth.weight in Roth/Box.lean while Roth.weight is an unbundled function; if Roth.weight is refactored onto Finsupp.weight (parent report), delete it since map_zero (simp) covers it; no mathlib PR.
- Type: `{σ : Type*} [Fintype σ] (r : σ → ℕ) : Roth.weight r 0 = 0`
- What: The zero multi-index has weight `0`.
- Hypotheses: none beyond the section variable `[Fintype σ]` (needed by `Roth.weight`).
- Uses from project: `Roth.weight`
- Used by: no explicit reference anywhere in Roth/ (`grep -rn weight_zero Roth/` returns only the declaration); it is tagged `@[simp]`, so it may fire implicitly inside the ~18 `simp` calls in Roth/ that mention `weight`.

### #33 theorem Roth.weight_add (public, Roth/Box.lean:85)
- verdict: NO-mathlib-has-it | cost: n/a | junk: KEEP
- rationale: Re-aimed at Finsupp.weight (parent Roth.weight is NO-mathlib-has-it), the analogue Finsupp.weight w (d + e) = Finsupp.weight w d + Finsupp.weight w e is mathlib's generic map_add (Finsupp.weight w is an AddMonoidHom); the project form is a one-line simp unfolding used at 3 rewrite sites.
- action: Keep in Roth/Box.lean while Roth.weight is an unbundled function; if Roth.weight is refactored onto Finsupp.weight (parent report), delete it and replace weight_add by map_add at Index.lean:114, Theta.lean:391, Lattice.lean:155; no mathlib PR.
- Type: `{σ : Type*} [Fintype σ] (r : σ → ℕ) (d e : σ →₀ ℕ) : Roth.weight r (d + e) = Roth.weight r d + Roth.weight r e`
- What: The weight `∑ j, d j / r j` is additive in the multi-index.
- Hypotheses: none beyond the section variable `[Fintype σ]` (needed by `Roth.weight`).
- Uses from project: `Roth.weight`
- Used by: Roth/Index.lean:114 (`index_sub_weight_le_index_hasseDeriv`, `simpa [weight_add, hiw]`); Roth/Theta.lean:391 (`rw [weight_add, weight_mapDomain ..., weight_single] at h1`); Roth/Lattice.lean:155 (`rw [weight_add, weight_mapDomain (Fin.castSucc_injective n), weight_single, mul_div_assoc]`).

### #34 theorem Roth.weight_eq_zero_iff (public, Roth/Box.lean:91)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Re-aimed at Finsupp.weight, mathlib's Finsupp.weight_eq_zero_iff_eq_zero needs CanonicallyOrderedAdd M (excludes ℝ), while the form with strictly positive weights in any ordered additive monoid is missing, strictly generalises it (verified), and is a short proof, not a 1-3 call composition.
- action: Upstream Finsupp.weight_eq_zero_iff_of_pos (hw : ∀ i, 0 < w i) to Mathlib/Data/Finsupp/Weight.lean next to weight_eq_zero_iff_eq_zero (deriving the canonical one from it); keep Roth.weight_eq_zero_iff for its single call site Index.lean:102, reproved through it if Roth.weight is refactored onto Finsupp.weight.
- Type: `{σ : Type*} [Fintype σ] {r : σ → ℕ} (hr : ∀ j, 0 < r j) {d : σ →₀ ℕ} : Roth.weight r d = 0 ↔ d = 0`
- What: For strictly positive parameters `r`, the weight `∑ j, d j / r j` of a multi-index vanishes exactly when the multi-index is zero.
- Hypotheses: `hr : ∀ j, 0 < r j` (essential: with `r j = 0`, `d j / 0 = 0` and any `d` supported at `j` has weight 0; evidence (5)); section variable `[Fintype σ]`.
- Uses from project: `Roth.weight`
- Used by: Roth/Index.lean:102 (`index_eq_zero_iff`: `rw [h, weight_eq_zero_iff hr] at hdw`); mentioned in the Roth/Box.lean:31 module docstring.

### #35 theorem Roth.weight_single (public, Roth/Box.lean:96)
- verdict: NO-mathlib-has-it | cost: n/a | junk: KEEP
- rationale: Re-aimed at Finsupp.weight (parent Roth.weight is NO-mathlib-has-it), the analogue Finsupp.weight w (single s c) = c • w s is exactly mathlib's Finsupp.weight_single; the project form is a two-line simp unfolding used at 2 rewrite sites.
- action: Keep in Roth/Box.lean while Roth.weight is unbundled; if Roth.weight is refactored onto Finsupp.weight (parent report), reprove it as Finsupp.weight_single plus nsmul_eq_mul and div_eq_mul_inv (keeping the name for Theta.lean:391 and Lattice.lean:155); no mathlib PR.
- Type: `{σ : Type*} [Fintype σ] (r : σ → ℕ) (j : σ) (n : ℕ) : Roth.weight r (Finsupp.single j n) = n / r j`
- What: The single multi-index `n • e_j` has weight `n / r_j`.
- Hypotheses: none beyond the section variable `[Fintype σ]` (needed by `Roth.weight`).
- Uses from project: `Roth.weight`
- Used by: Roth/Theta.lean:391 (`rw [weight_add, weight_mapDomain (Option.some_injective _), weight_single] at h1`); Roth/Lattice.lean:155 (`rw [weight_add, weight_mapDomain (Fin.castSucc_injective n), weight_single, mul_div_assoc]`).

### #36 theorem Roth.weight_le_card (public, Roth/Box.lean:103)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: Re-aimed at Finsupp.weight (parent is NO-mathlib-has-it), mathlib has no upper-bound lemma for Finsupp.weight, but the general form weight w d ≤ card σ • c (termwise d i • w i ≤ c) is one call to Finset.sum_le_card_nsmul after Finsupp.weight_eq_sum, and the project form is one call plus div_le_one_of_le₀ (all verified).
- action: Keep as project-local API in Roth/Box.lean for its single call site Roth/Index.lean:227 (index_le_card); optionally reprove as Finset.sum_le_card_nsmul + div_le_one_of_le₀; no mathlib PR.
- Type: `{σ : Type*} [Fintype σ] {r : σ → ℕ} {d : σ →₀ ℕ} (hd : ∀ j, d j ≤ r j) : Roth.weight r d ≤ Fintype.card σ`
- What: A multi-index in the box `d ≤ r` (coordinatewise) has weight `∑ j, d j / r j` at most the number of variables `card σ`.
- Hypotheses: `hd : ∀ j, d j ≤ r j` (membership in `box r`, stated unbundled); section variable `[Fintype σ]`.
- Uses from project: `Roth.weight`
- Used by: Roth/Index.lean:227 (`index_le_card`, `exact hdw ▸ weight_le_card fun j ↦ ...`). Also listed in the Box.lean module docstring (Main results, line 32).

### #37 theorem Roth.weight_mul_left (public, Roth/Box.lean:110)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: Re-aimed at Finsupp.weight (parent is NO-mathlib-has-it), mathlib has no weight-is-linear-in-w lemma, but weight (c • w) f = c • weight w f is one simp via Finsupp.smul_sum and smul_comm, and the project form is one simp via Finset.sum_div and div_div (all verified).
- action: Keep as project-local API in Roth/Box.lean for its single call site Roth/Index.lean:206 (index_mul_left_weights); no mathlib PR.
- Type: `{σ : Type*} [Fintype σ] {l : ℕ} (r : σ → ℕ) (d : σ →₀ ℕ) : Roth.weight (fun j ↦ l * r j) d = Roth.weight r d / l`
- What: Scaling every parameter `r j` by the same natural number `l` divides the weight `∑ j, d j / r j` by `l`.
- Hypotheses: none (section variable `[Fintype σ]`).
- Uses from project: `Roth.weight`
- Used by: Roth/Index.lean:206 (`index_mul_left_weights`, `rw [weight_mul_left, smul_eq_mul, div_eq_inv_mul]` inside the image computation).

### #38 theorem Roth.weight_le_degree_div (public, Roth/Box.lean:118)
- verdict: SKIP | cost: n/a | junk: REMOVE
- rationale: Unused anywhere in the project (the Lemma 6 proof uses the private real-ratio variant Theta.lean weight_le_delta_aux instead), and its content is a single gcongr after Finsupp.degree_eq_sum and Finset.sum_div; Step 8 REMOVE fires the Step 9a pre-filter.
- action: Delete Roth.weight_le_degree_div from Roth/Box.lean:113-122 (no call sites to update); optionally, instead generalise it to a real lower bound 0 < c ≤ r j and reprove Roth/Theta.lean weight_le_delta_aux from it, in which case it would be KEEP.
- Type: `{σ : Type*} [Fintype σ] {r : σ → ℕ} {m : ℕ} (hm : 0 < m) (hr : ∀ j, m ≤ r j) (d : σ →₀ ℕ) : Roth.weight r d ≤ ↑d.degree / ↑m`
- What: If every parameter `r j` is at least a positive natural `m`, then the weight `∑ j, d j / r j` of a multi-index `d` is at most its total degree divided by `m`.
- Hypotheses: `hm : 0 < m` (needed so `d j / m` dominates `d j / r j`; with `m = 0` the RHS is `0`), `hr : ∀ j, m ≤ r j`; section variable `[Fintype σ]` (the `[DecidableEq σ]` section variable was omitted earlier in the file).
- Uses from project: `Roth.weight`
- Used by: unused in project (`grep -rn weight_le_degree_div Roth/ Roth.lean` returns only the declaration at Roth/Box.lean:118).

### #39 theorem Roth.weight_mapDomain (public, Roth/Box.lean:127)
- verdict: NO-mathlib-has-it | cost: n/a | junk: KEEP
- rationale: Re-aimed at Finsupp.weight (parent Roth.weight is NO-mathlib-has-it), the statement Finsupp.weight w (d.mapDomain f) = Finsupp.weight (w ∘ f) d is exactly mathlib's Finsupp.linearCombination_mapDomain, which needs no injectivity; the project's hf hypothesis is superfluous (verified in evidence).
- action: Keep in Roth/Box.lean as the project-local API name but drop the superfluous hypothesis hf (proof via Finsupp.sum_mapDomain_index, evidence (4)) and update the 3 callers Index.lean:219, Theta.lean:391, Lattice.lean:155; no mathlib PR.
- Type: `{σ : Type*} [Fintype σ] {τ : Type*} [Fintype τ] {f : σ → τ} (hf : Function.Injective f) (r : τ → ℕ) (d : σ →₀ ℕ) : Roth.weight r (d.mapDomain f) = Roth.weight (r ∘ f) d`
- What: Pushing a multi-index forward along an injective change of variables `f : σ → τ` and evaluating the weight with parameters `r` equals evaluating the weight of the original multi-index with the pulled-back parameters `r ∘ f`.
- Hypotheses: `hf : Function.Injective f` (superfluous, see below); section variable `[Fintype σ]`, plus `[Fintype τ]` (both needed for `Roth.weight` to typecheck).
- Uses from project: `Roth.weight`
- Used by: Roth/Index.lean:219 (`exact weight_mapDomain hf r d`, inside `index_rename`); Roth/Theta.lean:391 (`rw [weight_add, weight_mapDomain (Option.some_injective _), weight_single] at h1`); Roth/Lattice.lean:155 (`rw [weight_add, weight_mapDomain (Fin.castSucc_injective n), weight_single, mul_div_assoc]`). Also named in the Box.lean module docstring (line 33).

### #40 def Roth.wronskianMatrix (public, Roth/Wronskian.lean:56)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The l x l Hasse-derivative Wronskian matrix is standard (Hasse/Schmidt Wronskian, Garcia-Voloch) and fills mathlib's explicit TODO in RingTheory/Polynomial/Wronskian.lean (only the 2-polynomial Polynomial.wronskian exists, and its det equals ours for l = 2, verified); the def should be stated over an arbitrary semiring in the Polynomial namespace, not over a field.
- action: Upstream with Roth.wronskian as Polynomial.wronskianMatrix over [Semiring R] (verified in evidence) in Mathlib/RingTheory/Polynomial/Wronskian.lean, adding a lemma that its det for l = 2 is Polynomial.wronskian; locally keep (call sites Roth/Wronskian.lean l.60/71/139/161/163, Roth/GenWronskian.lean:244, Roth/Separation.lean:358).
- Type: `{K : Type*} → [Field K] → {l : ℕ} → (φ : Fin l → K[X]) → Matrix (Fin l) (Fin l) K[X]`
- What: The `l × l` Wronskian matrix of a family of univariate polynomials built from Hasse derivatives: entry `(μ, ν)` is `hasseDeriv μ (φ ν) = (1/μ!) d^μ φ_ν / dt^μ`.
- Hypotheses: `[Field K]` (section variable); no other hypotheses.
- Uses from project: `[]` (`hasseDeriv` here is mathlib's `Polynomial.hasseDeriv`)
- Used by: Roth/Wronskian.lean: `Roth.wronskian` (l.60, definition), `wronskian_eq_zero_of_not_linearIndependent` (l.71), `coeff_wronskian_of_natDegree_injective` (l.139), `wronskian_update_sub_smul` (l.161, l.163); Roth/GenWronskian.lean: `wronskian_kronecker_eq_sum_aux` (private, l.244); Roth/Separation.lean: `det_hasseDeriv_separated` (l.358)

### #41 def Roth.wronskian (public, Roth/Wronskian.lean:60)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The n-ary (Hasse) Wronskian det (D^(mu) phi_nu) is the object mathlib's RingTheory/Polynomial/Wronskian.lean lists as a TODO (only the 2-ary Polynomial.wronskian exists, and ours equals it at l = 2 over any CommRing, verified); the def only needs [CommRing R], not [Field K], and its name must be reconciled with the existing 2-ary Polynomial.wronskian.
- action: Upstream together with Roth.wronskianMatrix in Mathlib/RingTheory/Polynomial/Wronskian.lean over [CommRing R] (verified in evidence) under a non-clashing n-ary name, with the l = 2 bridge lemma to Polynomial.wronskian, a map/base-change lemma (verified) and wronskian_eq_zero_of_not_linearIndependent; locally keep (call sites Roth/Wronskian.lean l.66/123/139/149/159/206/220, Roth/GenWronskian.lean:241/244, Roth/Separation.lean:356/357/528).
- Type: `{K : Type*} → [Field K] → {l : ℕ} → (φ : Fin l → K[X]) → K[X]`
- What: The Wronskian of `l` univariate polynomials, `W(φ_0, …, φ_{l-1}) = det (D^{(μ)} φ_ν)_{0 ≤ μ, ν < l}` with `D^{(μ)} = hasseDeriv μ` the `μ`-th Hasse derivative (`(1/μ!) d^μ/dt^μ`).
- Hypotheses: `[Field K]` (section variable); no other hypotheses.
- Uses from project: `Roth.wronskianMatrix`
- Used by: Roth/Wronskian.lean: `wronskian_eq_zero_of_not_linearIndependent` (l.66), `coeff_wronskian_of_natDegree_injective` (l.123 statement, l.139 unfolds it), `wronskian_ne_zero_of_natDegree_injective` (l.149), `wronskian_update_sub_smul` (l.159), `wronskian_ne_zero_of_linearIndependent` (l.206), `wronskian_eq_zero_iff` (l.220); Roth/GenWronskian.lean: `wronskian_kronecker_eq_sum_aux` (private, l.241 sta

### #42 theorem Roth.wronskian_eq_zero_of_not_linearIndependent (public, Roth/Wronskian.lean:65)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The easy direction of the n-ary Wronskian criterion (dependent family has zero Wronskian) is absent from mathlib (n-ary Wronskian is a mathlib TODO); [Field K] weakens to [CommRing R] [IsDomain R] with the proof unchanged (verified), and IsDomain is necessary (ZMod 4 counterexample verified).
- action: Upstream with Roth.wronskianMatrix/Roth.wronskian to Mathlib/RingTheory/Polynomial/Wronskian.lean over [CommRing R] [IsDomain R] (proof verbatim, evidence file); locally keep (call site Roth/Wronskian.lean:222 in wronskian_eq_zero_iff).
- Type: `{K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]} (h : ¬ LinearIndependent K φ) : wronskian φ = 0`
- What: A `K`-linearly dependent family of `l` polynomials has vanishing (Hasse) Wronskian `det (D^{(μ)} φ_ν)`.
- Hypotheses: `[Field K]` (section variable); `h : ¬ LinearIndependent K φ`.
- Uses from project: `Roth.wronskian`, `Roth.wronskianMatrix`
- Used by: Roth/Wronskian.lean:222 (`wronskian_eq_zero_iff`, reverse direction). No other project use.

### #43 theorem Roth.det_choose_eq (public, Roth/Wronskian.lean:79)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The binomial determinant det (d_nu choose mu) = Vandermonde / prod mu! exists in mathlib only as the private ℤ-lemma Matrix.of_eval_descPochhammer_eq_mul_of_choose; the char-free form (prod mu!) * det = prod (d_j - d_i) holds over any CommRing (and with Ring.choose over any binomial ring), verified in evidence, and the project's CharZero-field statement is a 2-line corollary.
- action: Upstream to Mathlib/LinearAlgebra/Vandermonde.lean the CommRing lemmas det_eval_descPochhammer and prod_factorial_mul_det_choose (plus the BinomialRing Ring.choose version), replacing the private of_eval_descPochhammer_eq_mul_of_choose; keep det_choose_eq locally as the field corollary used at Roth/Wronskian.lean:151.
- Type: `∀ {K : Type*} [Field K] {l : ℕ} [CharZero K] (d : Fin l → ℕ), (Matrix.of fun μ ν : Fin l ↦ ((d ν).choose μ : K)).det = (∏ μ : Fin l, ((μ : ℕ).factorial : K)⁻¹) * ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, ((d j : K) - d i)`
- What: The binomial determinant `det (C(d_ν, μ))_{μ,ν}` equals the Vandermonde product `∏_{i<j} (d_j − d_i)` divided by `∏_{μ<l} μ!`.
- Hypotheses: `[Field K]` (section variable), `[CharZero K]`.
- Uses from project: `[]`
- Used by: Roth/Wronskian.lean:151 `wronskian_ne_zero_of_natDegree_injective` (in a `simpa` call). It is also named in the module docstring at l.28.

### #44 lemma Roth.coeff_prod_of_natDegree_le' (private, Roth/Wronskian.lean:93)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private per-index-bound version of the top coefficient of a finite product of polynomials; mathlib's Polynomial.coeff_prod_of_natDegree_le only has a uniform bound n (coefficient at card s * n) and is the special case n i := n, so it does not cover this; used once in coeff_wronskian_of_natDegree_injective.
- action: Keep as private helper for Roth/Wronskian.lean:131 (coeff_wronskian_of_natDegree_injective); optional small mathlib PR adding it (generalised to CommSemiring, verified) next to Polynomial.coeff_prod_of_natDegree_le in Mathlib/Algebra/Polynomial/BigOperators.lean.
- Type: `∀ {K : Type*} [Field K] {ι : Type*} (s : Finset ι) (f : ι → K[X]) (n : ι → ℕ), (∀ i ∈ s, (f i).natDegree ≤ n i) → (∏ i ∈ s, f i).coeff (∑ i ∈ s, n i) = ∏ i ∈ s, (f i).coeff (n i)`
- What: If each factor `f i` has degree at most `n i`, then the coefficient of `X^(∑ n i)` in `∏ f i` is the product of the coefficients of `X^(n i)` in the `f i` (the "top" coefficient of a product with per-factor degree bounds).
- Hypotheses: `h : ∀ i ∈ s, (f i).natDegree ≤ n i`; section variable `[Field K]` (only `CommSemiring` is needed, verified in evidence file).
- Uses from project: `[]` (only mathlib lemmas; `K[X]` from the section variable `{K : Type*} [Field K]`)
- Used by: Roth/Wronskian.lean:131 in `Roth.coeff_wronskian_of_natDegree_injective` (inside the `key` step) only (`grep -rn "coeff_prod_of_natDegree_le'" Roth/`). Transitively: `Roth.wronskian_ne_zero_of_natDegree_injective` (Roth/Wronskian.lean:148, uses it at l.152).

### #45 theorem Roth.sum_range_le_sum_of_injective (public, Roth/Wronskian.lean:107)
- verdict: SKIP | cost: n/a | junk: REMOVE
- rationale: Unused anywhere in the project (the Wronskian degree argument uses truncated ℕ subtraction, so D ≥ 0 is never needed) and its 4-line proof is just a specialisation of mathlib's Finset.sum_range_le_sum (ℤ, Mathlib/Algebra/Order/Group/Int/Sum.lean:72); Step 8 REMOVE fires the Step 9a pre-filter.
- action: Delete Roth.sum_range_le_sum_of_injective from Roth/Wronskian.lean:105-114 (no call sites; then check whether the import Mathlib.Algebra.Order.Group.Int.Sum is still needed); if the user wants the source step D ≥ 0 recorded, mention it in the docstring of coeff_wronskian_of_natDegree_injective instead.
- Type: `∀ {l : ℕ} (d : Fin l → ℕ), Function.Injective d → ∑ ν : Fin l, (ν : ℕ) ≤ ∑ ν, d ν`
- What: `l` pairwise distinct natural numbers sum to at least `0 + 1 + ⋯ + (l − 1) = l(l−1)/2`. This is the source's `D = ∑ d_ν − l(l−1)/2 ≥ 0` (clean.tex l.183).
- Hypotheses: `hd : Function.Injective d`. This is needed: for `l = 2` and `d = 0` the claim reads `1 ≤ 0`. The counterexample was kernel-checked in the earlier cleanup report `.mathlib-quality/cleanup/Wronskian-sum_range_le_sum_of_injective.md` and also appears in `.mathlib-quality/decomposition.md` R4.4.
- Uses from project: `[]`
- Used by: unused in project. `grep -rn sum_range_le_sum_of_injective Roth Roth.lean` finds only the declaration at Roth/Wronskian.lean:107. Outside `.lean` files the name appears only in planning and cleanup notes (`tickets.md`, `decomposition.md`, `cleanup/*.md`, `PROJECT_OVERVIEW.md`, `overview/decls.tsv`).

### #46 theorem Roth.coeff_wronskian_of_natDegree_injective (public, Roth/Wronskian.lean:122)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The classical leading-term formula for the n-ary Wronskian (coefficient of t^(sum d - l(l-1)/2) equals prod of leading coefficients times det (d_nu choose mu)) is absent from mathlib, which only has the 2-ary Polynomial.wronskian; the proof goes through verbatim over any CommRing (verified), and the name's _of_natDegree_injective suffix is misleading because the statement has no hypotheses.
- action: Upstream with Roth.wronskian / Roth.wronskianMatrix to Mathlib/RingTheory/Polynomial/Wronskian.lean over [CommRing R] (verified in evidence) under a hypothesis-free name such as coeff_wronskian_sum_natDegree_sub, together with the per-index product-coefficient helper (Roth.coeff_prod_of_natDegree_le') in Mathlib/Algebra/Polynomial/BigOperators.lean; locally keep (sole use Roth/Wronskian.lean:152).
- Type: `∀ {K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]}, (wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) = (∏ ν, (φ ν).leadingCoeff) * (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : K)).det`
- What: For any family `φ_0, …, φ_{l-1}` of polynomials with degrees `d_ν`, the coefficient of `t^D`, `D = ∑ d_ν − ∑ ν` (truncated subtraction), in the Hasse Wronskian `det (D^{(μ)} φ_ν)` is `(∏ lc(φ_ν)) · det (C(d_ν, μ))_{μ,ν}`.
- Hypotheses: `[Field K]` (section variable); none on `φ`.
- Uses from project: `Roth.wronskian`, `Roth.wronskianMatrix`, `Roth.coeff_prod_of_natDegree_le'` (private)
- Used by: Roth/Wronskian.lean:152 `wronskian_ne_zero_of_natDegree_injective` (in `simpa ... using`); also named in the module docstring at l.41.

### #47 theorem Roth.wronskian_ne_zero_of_natDegree_injective (public, Roth/Wronskian.lean:148)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Nonvanishing of the n-ary (Hasse) Wronskian for nonzero polynomials of distinct degrees is classical (Bostan-Dumas Lemma 3) and absent from mathlib, which has only the 2-ary Wronskian; [Field K] weakens to [CommRing R] [IsDomain R] [CharZero R] and a char-free core with hypothesis det (C(d_nu, mu)) ne 0 holds over any domain (both verified), while CharZero and hφ are necessary (counterexamples verified).
- action: Upstream with the n-ary Wronskian PR to Mathlib/RingTheory/Polynomial/Wronskian.lean as a char-free domain lemma (hypothesis det of binomial matrix ne 0) plus the CharZero distinct-degree corollary over [CommRing R] [IsDomain R] [CharZero R]; locally keep (sole call site Roth/Wronskian.lean:210 in wronskian_ne_zero_of_linearIndependent).
- Type: `∀ {K : Type*} [Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]}, (∀ ν, φ ν ≠ 0) → Function.Injective (fun ν ↦ (φ ν).natDegree) → wronskian φ ≠ 0`
- What: In characteristic zero, nonzero polynomials `φ_0, …, φ_{l-1}` of pairwise distinct degrees have nonzero (Hasse) Wronskian `det (D^{(μ)} φ_ν)`.
- Hypotheses: `[Field K]` (section variable), `[CharZero K]`, `hφ : ∀ ν, φ ν ≠ 0`, `hd : Function.Injective fun ν ↦ (φ ν).natDegree`.
- Uses from project: `Roth.wronskian`, `Roth.coeff_wronskian_of_natDegree_injective`, `Roth.det_choose_eq`
- Used by: Roth/Wronskian.lean:210 (`wronskian_ne_zero_of_linearIndependent`, base case of the strong induction); module docstring l.30.

### #48 theorem Roth.wronskian_update_sub_smul (public, Roth/Wronskian.lean:158)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Column-operation invariance of the n-ary Wronskian is a basic missing fact once the n-ary Wronskian (mathlib TODO) is upstreamed; [Field K] weakens to [CommRing R] verbatim and the literature-standard form W(phi A) = det A * W(phi) (stated in the project source itself) is verified, with this lemma as the transvection case.
- action: Upstream with Roth.wronskian to Mathlib/RingTheory/Polynomial/Wronskian.lean over [CommRing R], adding the change-of-basis lemma (wronskian of sum A rho nu smul phi rho = C (det A) * wronskian phi, verified) and this transvection lemma (preferably in the smul/add spelling); locally keep (call site Roth/Wronskian.lean:212).
- Type: `{K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l} (h : ν ≠ ν') (c : K) : wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = wronskian φ`
- What: Replacing `φ ν'` by `φ ν' - c φ ν` (constant `c`, `ν ≠ ν'`) does not change the Wronskian `det (D^{(μ)} φ_ρ)`.
- Hypotheses: `[Field K]` (section variable); `h : ν ≠ ν'`; `c : K`.
- Uses from project: `Roth.wronskian`, `Roth.wronskianMatrix`
- Used by: Roth/Wronskian.lean:212 (`wronskian_ne_zero_of_linearIndependent`, induction step on total degree). No other project use (also mentioned in the module docstring l.38).

### #49 theorem Roth.linearIndependent_update_sub_smul (public, Roth/Wronskian.lean:170)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Pure linear algebra (transvection preserves linear independence) that mathlib has only in the Pi-add spelling linearIndependent_add_smul_iff; the Function.update iff over [Ring R] for any module (verified, 4-line proof) is the missing companion of Submodule.span_range_update_add_smul, and the project lemma is a one-line corollary.
- action: Add linearIndependent_update_sub_smul_iff (and the add_smul variant) over [Ring R] [AddCommGroup M] to Mathlib/LinearAlgebra/LinearIndependent/Defs.lean next to linearIndependent_add_smul_iff; then reduce the project lemma (call sites Roth/Wronskian.lean:190 and :214) to a one-line corollary or inline it.
- Type: `{K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l} (h : ν ≠ ν') (c : K) (hφ : LinearIndependent K φ) : LinearIndependent K (Function.update φ ν' (φ ν' - C c * φ ν))`
- What: Replacing `φ ν'` by `φ ν' - c φ ν` (constant `c`, `ν ≠ ν'`) in a linearly independent family of polynomials keeps it linearly independent.
- Hypotheses: `[Field K]` (section variable); `h : ν ≠ ν'`; `c : K`; `hφ : LinearIndependent K φ`.
- Uses from project: `[]` (only mathlib lemmas; `wronskian` not involved)
- Used by: Roth/Wronskian.lean:190 (`sum_natDegree_update_lt`, nonvanishing of the updated member), Roth/Wronskian.lean:214 (`wronskian_ne_zero_of_linearIndependent`, induction step). No other project use.

### #50 theorem Roth.sum_natDegree_update_lt (public, Roth/Wronskian.lean:182)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: Project-specific induction measure (sum of natDegrees drops after one leading-term elimination); its only mathematical content is mathlib's degree_sub_lt_left (equivalently the division-free cancelLeads API) lifted through Finset.sum_lt_sum, and the hypotheses weaken (verified) to phi nu ne 0 plus nonvanishing of the updated member.
- action: Do not upstream; keep locally for its sole call site Roth/Wronskian.lean:213 (wronskian_ne_zero_of_linearIndependent), optionally restating with the verified weaker hypotheses (hp, hne, any Fintype index, DivisionRing) or inlining the degree_sub_lt_left plus Finset.sum_lt_sum composition there.
- Type: `{K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]} (hφ : LinearIndependent K φ) {ν ν' : Fin l} (h : ν ≠ ν') (hdeg : (φ ν).natDegree = (φ ν').natDegree) : ∑ ρ, (Function.update φ ν' (φ ν' - C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν) ρ).natDegree < ∑ ρ, (φ ρ).natDegree`
- What: In a linearly independent family of polynomials, if two distinct members have equal degree, replacing `φ ν'` by `φ ν' - (lc φ ν' / lc φ ν) φ ν` (cancelling its leading term) strictly decreases the total degree `∑ deg φ ρ`.
- Hypotheses: `[Field K]` (section variable); `hφ : LinearIndependent K φ`; `h : ν ≠ ν'`; `hdeg` equal natDegrees.
- Uses from project: `Roth.linearIndependent_update_sub_smul`
- Used by: Roth/Wronskian.lean:213 (`wronskian_ne_zero_of_linearIndependent`, decreasing measure in the strong induction). No other project use.

### #51 theorem Roth.wronskian_ne_zero_of_linearIndependent (public, Roth/Wronskian.lean:205)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The hard direction of the n-ary Wronskian criterion (linearly independent polynomials have nonzero Wronskian in char 0, Bostan-Dumas Thm 2) is absent from mathlib, which only has the 2-ary Wronskian; [Field K] weakens to [CommRing R] [IsDomain R] [CharZero R] via the fraction field (verified), and CharZero is necessary (ZMod 2 counterexample verified).
- action: Upstream with the n-ary Wronskian PR to Mathlib/RingTheory/Polynomial/Wronskian.lean over [CommRing R] [IsDomain R] [CharZero R] (field case as now, domain case by fraction-field transfer as in evidence), together with the iff form; locally keep (call sites Roth/Wronskian.lean:221, Roth/GenWronskian.lean:262, Roth/Separation.lean:534).
- Type: `∀ {K : Type*} [Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]}, LinearIndependent K φ → wronskian φ ≠ 0`
- What: In characteristic zero, a linearly independent family `φ_0, …, φ_{l−1}` of univariate polynomials has nonzero (Hasse) Wronskian `det (D^{(μ)} φ_ν)`.
- Hypotheses: `[Field K]` (section variable), `[CharZero K]`, `h : LinearIndependent K φ`.
- Uses from project: `Roth.wronskian`, `Roth.wronskian_ne_zero_of_natDegree_injective`, `Roth.wronskian_update_sub_smul`, `Roth.linearIndependent_update_sub_smul`, `Roth.sum_natDegree_update_lt`
- Used by: Roth/Wronskian.lean:221 (`wronskian_eq_zero_iff`, forward direction); Roth/GenWronskian.lean:262 (`exists_genWronskian_ne_zero`, applied to the Kronecker-substituted family); Roth/Separation.lean:534 (the separated representation of the main induction).

### #52 theorem Roth.wronskian_eq_zero_iff (public, Roth/Wronskian.lean:219)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The n-ary Wronskian criterion (Wronskian vanishes iff the family is dependent, char 0) is absent from mathlib (n-ary Wronskian is a TODO in Mathlib/RingTheory/Polynomial/Wronskian.lean); [Field K] weakens to [CommRing R] [IsDomain R] [CharZero R] (verified), and both CharZero (ZMod 2) and IsDomain (QxQ) are necessary (verified counterexamples).
- action: Ship as the headline theorem of the n-ary Wronskian PR to Mathlib/RingTheory/Polynomial/Wronskian.lean over [CommRing R] [IsDomain R] [CharZero R], adding the companion wronskian_ne_zero_iff (W ne 0 iff LinearIndependent); locally keep (no project call sites, it is the module's stated main result).
- Type: `∀ {K : Type*} [Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]}, wronskian φ = 0 ↔ ¬ LinearIndependent K φ`
- What: In characteristic zero, the (Hasse) Wronskian `det (D^{(μ)} φ_ν)` of a family of `l` polynomials is zero iff the family is linearly dependent over `K`.
- Hypotheses: `[Field K]` (section variable), `[CharZero K]`.
- Uses from project: `Roth.wronskian`, `Roth.wronskian_ne_zero_of_linearIndependent`, `Roth.wronskian_eq_zero_of_not_linearIndependent`
- Used by: unused in project (`grep -rn wronskian_eq_zero_iff Roth/ Roth.lean`: only the module docstring l.32 and the declaration l.219; call sites use the two directional lemmas directly)

### #53 def MvPolynomial.taylor (public, Roth/Taylor.lean:42)
- verdict: YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Multivariate translation P to P(X + α) is standard (multivariate Taylor expansion with Hasse-derivative coefficients) and mathlib has only the univariate Polynomial.taylor / taylorAlgHom / algEquivAevalXAddC; the one-line def is justified as the named API anchor (coeff_taylor, taylor_taylor, eval_taylor, Index.lean) exactly as Polynomial.taylor is in mathlib, and is already maximally general.
- action: Upstream with the MvPolynomial.hasseDeriv PR as Mathlib/Algebra/MvPolynomial/Taylor.lean (taylor, taylor_X, taylor_C, taylor_monomial, coeff_taylor, eval_taylor, taylor_taylor, taylor_zero, taylor_map, taylor_rename, degreeOf_taylor_le, taylor_injective) plus the compiled bridge uniqueAlgEquiv_taylor to Polynomial.taylor; locally keep as is (used in Roth/Index.lean).
- Type: `{σ R : Type*} → [CommSemiring R] → (α : σ → R) → MvPolynomial σ R →ₐ[R] MvPolynomial σ R`
- What: The translation (multivariate Taylor shift) `P ↦ P(X + α)`, the `R`-algebra endomorphism sending each variable `X j` to `X j + α j`.
- Hypotheses: `[CommSemiring R]` (section variable); none else.
- Uses from project: `[]`
- Used by: Roth/Taylor.lean (taylor_apply, taylor_X, taylor_C, taylor_monomial, private coeff_taylor_monomial_single_add_aux / coeff_taylor_monomial_aux, coeff_taylor, eval_taylor, taylor_taylor, taylor_zero, taylor_map, taylor_rename, degreeOf_taylor_le, taylor_neg_taylor, taylor_injective, taylor_eq_zero_iff, eq_sum_box_hasseDeriv); Roth/Index.lean (definition of `index` l.59, mem_support_taylor_iff l.63, 

### #54 theorem MvPolynomial.taylor_apply (public, Roth/Taylor.lean:46)
- verdict: INHERITED-YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Pure rfl unfolding lemma of MvPolynomial.taylor (taylor α P = aeval (X + C α) P); multivariate analogue of mathlib's Polynomial.taylor_apply, ships with the parent.
- action: Upstream with MvPolynomial.taylor in a new Mathlib/Algebra/MvPolynomial/Taylor.lean; locally keep as the named unfolding lemma (currently no project call site; Roth/Index.lean:243 uses the univariate Polynomial.taylor_apply).
- Type: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (P : MvPolynomial σ R), taylor α P = aeval (fun j ↦ X j + C (α j)) P`
- What: The translate `P(X + α)` is the evaluation of `P` at the point `X + α` (substitution `X j ↦ X j + α j`).
- Hypotheses: `[CommSemiring R]` (section variable); none else.
- Uses from project: `MvPolynomial.taylor`
- Used by: unused in project (`grep -rn taylor_apply Roth/` finds only the declaration and Roth/Index.lean:243, which is mathlib's univariate `Polynomial.taylor_apply`; not `@[simp]`, so no implicit uses).

### #55 theorem MvPolynomial.taylor_X (public, Roth/Taylor.lean:51)
- verdict: INHERITED-YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Defining simp equation of MvPolynomial.taylor on generators (taylor α (X j) = X j + C (α j)), proved by pure unfolding of taylor := aeval plus mathlib's aeval_X; multivariate analogue of mathlib's Polynomial.taylor_X, ships with the parent.
- action: Upstream with MvPolynomial.taylor in a new Mathlib/Algebra/MvPolynomial/Taylor.lean (keep @[simp]); locally keep as is (used by name at Roth/Taylor.lean:114 in coeff_taylor_monomial_single_add_aux).
- Type: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (j : σ), taylor α (X j) = X j + C (α j)`
- What: The translation `P ↦ P(X + α)` sends the variable `X j` to `X j + α j`.
- Hypotheses: `[CommSemiring R]` (section variable); none else.
- Uses from project: `MvPolynomial.taylor`
- Used by: Roth/Taylor.lean:114 (`coeff_taylor_monomial_single_add_aux`, private, in a `rw` chain). It is `@[simp]`, but no project `simp` call is on a goal containing `taylor α (X j)` in normal form (the simp calls mentioning `taylor` in Roth/Taylor.lean l.143-166 unfold `taylor` itself; Roth/Index.lean simp calls go through `coeff_taylor`), so no implicit uses found.

### #56 theorem MvPolynomial.taylor_C (public, Roth/Taylor.lean:55)
- verdict: INHERITED-YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Defining simp equation of MvPolynomial.taylor on constants (taylor α (C a) = C a), a direct instance of mathlib's MvPolynomial.algHom_C for the R-algebra hom taylor α; multivariate analogue of mathlib's Polynomial.taylor_C, ships with the parent.
- action: Upstream with MvPolynomial.taylor in a new Mathlib/Algebra/MvPolynomial/Taylor.lean (keep @[simp]); locally keep as is (used by name at Roth/Index.lean:197 in index_C_mul).
- Type: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (a : R), taylor α (C a) = C a`
- What: The translation `P ↦ P(X + α)` fixes constant polynomials.
- Hypotheses: `[CommSemiring R]` (section variable); none else.
- Uses from project: `MvPolynomial.taylor`
- Used by: Roth/Index.lean:197 (`index_C_mul`, in a `rw` chain). It is `@[simp]`, but no project `simp` call is on a goal containing `taylor α (C a)` (the simp calls mentioning `taylor` in Roth/Taylor.lean l.143-166 unfold `taylor` itself; Roth/Index.lean simp calls go through `coeff_taylor`), so no implicit uses found.

### #57 theorem MvPolynomial.taylor_monomial (public, Roth/Taylor.lean:59)
- verdict: INHERITED-YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Computation rule of MvPolynomial.taylor on monomials (taylor α (monomial k a) = C a * k.prod (X j + C (α j))^n), proved by pure unfolding of taylor := aeval plus mathlib's aeval_monomial; multivariate analogue of mathlib's Polynomial.taylor_monomial, ships with the parent.
- action: Upstream with MvPolynomial.taylor in a new Mathlib/Algebra/MvPolynomial/Taylor.lean; locally keep as is (used by name at Roth/Taylor.lean:212 in eq_sum_box_hasseDeriv).
- Type: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (k : σ →₀ ℕ) (a : R), taylor α (monomial k a) = C a * k.prod fun j n ↦ (X j + C (α j)) ^ n`
- What: The translate `P(X + α)` of the monomial `a X^k` is `a ∏_j (X_j + α_j)^{k_j}`.
- Hypotheses: `[CommSemiring R]` (section variable); none else.
- Uses from project: `MvPolynomial.taylor`
- Used by: Roth/Taylor.lean:212 (`eq_sum_box_hasseDeriv`, in a `rw` chain turning each `taylor (-α) (monomial d c)` into a product over `Fintype σ`). Not `@[simp]`; no other uses (the private `coeff_taylor_monomial_*_aux` lemmas only share the name prefix).

### #58 lemma MvPolynomial.coeff_aeval_X_mul (private, Roth/Taylor.lean:63)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private coefficient-splitting lemma coeff_d(f(X_i) * B) = f_{d_i} * B_{d.erase i} for B free of X_i, used only in the monomial induction step of coeff_taylor; mathlib has only the monomial case coeff_monomial_mul' and the Fin/Option equivalences.
- action: Keep as private helper for its single call site Roth/Taylor.lean:115 (coeff_taylor_monomial_single_add_aux); if coeff_taylor is upstreamed, carry it along privately or state it publicly in Mathlib/Algebra/MvPolynomial/Basic.lean next to coeff_monomial_mul'.
- Type: `∀ {σ R : Type*} [CommSemiring R] (i : σ) (f : Polynomial R) (B : MvPolynomial σ R), (∀ e ∈ B.support, e i = 0) → ∀ (d : σ →₀ ℕ), (Polynomial.aeval (X i) f * B).coeff d = f.coeff (d i) * B.coeff (d.erase i)`
- What: If the multivariate polynomial B does not involve the variable X_i (every monomial in its support has i-exponent 0), then the coefficient of the product f(X_i) · B at the multi-index d factors as (coefficient of t^{d_i} in the one-variable polynomial f) times (coefficient of B at d with the i-th entry deleted). It is the "separation of variables" coefficient formula.
- Hypotheses: `[CommSemiring R]`; `hB : ∀ e ∈ B.support, e i = 0` (B free of X_i). `classical` for decidability of `σ`.
- Uses from project: `[]` (only mathlib lemmas; it sits in the project namespace `MvPolynomial` but references no project declaration)
- Used by: Roth/Taylor.lean: `coeff_taylor_monomial_single_add_aux` (private, l.99; `rw [..., coeff_aeval_X_mul i _ _ hsupp, ...]` at l.115) only — `grep -rn coeff_aeval_X_mul Roth/` gives the definition and that use. Transitively: `coeff_taylor_monomial_aux` (l.121) → `coeff_taylor` (l.136) and everything downstream of Taylor's theorem.

### #59 lemma MvPolynomial.hasseCoeff_single_add_eq (private, Roth/Taylor.lean:82)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private splitting lemma hasseCoeff d (single i n + k') = n.choose (d i) * hasseCoeff (d.erase i) k' for k' i = 0, a 6-line Finsupp.mul_prod_erase' computation used once in the monomial induction step of coeff_taylor; mathlib has no hasseCoeff and no ready-made instance.
- action: Keep as private helper for its single call site Roth/Taylor.lean:117 (coeff_taylor_monomial_single_add_aux); if hasseCoeff and coeff_taylor are upstreamed, carry it along next to them (Mathlib/Algebra/MvPolynomial/HasseDeriv-style file).
- Type: `∀ {σ : Type*} {i : σ} {n : ℕ} {k' : σ →₀ ℕ}, k' i = 0 → ∀ (d : σ →₀ ℕ), hasseCoeff d (Finsupp.single i n + k') = n.choose (d i) * hasseCoeff (d.erase i) k'`
- What: The multinomial binomial factor hasseCoeff d k = ∏_{j ∈ supp d} C(k_j, d_j) splits off the i-th variable: if k = n·e_i + k' with k' not involving i, then hasseCoeff d k = C(n, d_i) · hasseCoeff (d with i-th entry removed) k'.
- Hypotheses: `hi : k' i = 0` (k' does not involve variable i); `classical`. No ring needed (statement is in ℕ); the ambient `[CommSemiring R]` section variable is not used by this lemma's statement.
- Uses from project: `hasseCoeff` (Roth/HasseDeriv.lean:50)
- Used by: Roth/Taylor.lean: `coeff_taylor_monomial_single_add_aux` (private, l.99; `rw [..., hasseCoeff_single_add_eq hi, ...]` at l.117) only — `grep -rn hasseCoeff_single_add_eq Roth/` gives the definition and that use. Transitively: `coeff_taylor_monomial_aux` → `coeff_taylor` and everything downstream of Taylor's theorem.

### #60 lemma MvPolynomial.prod_pow_single_add_tsub (private, Roth/Taylor.lean:92)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private splitting lemma ((single i n + k') - d).prod (α j ^ ·) = α i ^ (n - d i) * (k' - d.erase i).prod (α j ^ ·) for k' i = 0, a 5-line Finsupp ext plus prod_add_index' computation used once in the monomial induction step of coeff_taylor; mathlib has no ready-made form.
- action: Keep as private helper for its single call site Roth/Taylor.lean:117 (coeff_taylor_monomial_single_add_aux); if coeff_taylor is upstreamed, carry it along as a private helper beside hasseCoeff_single_add_eq.
- Type: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) {i : σ} {n : ℕ} {k' : σ →₀ ℕ}, k' i = 0 → ∀ (d : σ →₀ ℕ), (Finsupp.single i n + k' - d).prod (fun j e ↦ α j ^ e) = α i ^ (n - d i) * (k' - d.erase i).prod (fun j e ↦ α j ^ e)`
- What: The evaluated monomial α^(k - d) = ∏_j α_j^(k_j - d_j) splits off the i-th variable: if k = n·e_i + k' with k' not involving i, then α^(k - d) = α_i^(n - d_i) · α^(k' - d') where d' is d with its i-th entry erased.
- Hypotheses: `hi : k' i = 0` (k' does not involve variable i); `classical`. Only the commutative-monoid structure of R is used (powers and products); `[CommSemiring R]` comes from the section variable.
- Uses from project: `[]` (only mathlib `Finsupp` API: `Finsupp.single`, `Finsupp.erase`, `Finsupp.erase_ne`, `Finsupp.prod_add_index'`, `pow_add`, `Finsupp.single_tsub`)
- Used by: Roth/Taylor.lean: `coeff_taylor_monomial_single_add_aux` (private, l.101; `rw [..., prod_pow_single_add_tsub α hi]` at l.117) only — `grep -rn prod_pow_single_add_tsub Roth/` gives the definition (l.92) and that single use. Transitively: `coeff_taylor_monomial_aux` -> `coeff_taylor` and everything downstream of Taylor's theorem.

### #61 lemma MvPolynomial.coeff_taylor_monomial_single_add_aux (private, Roth/Taylor.lean:101)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private inductive step (single_add case of Finsupp.induction) of the monomial case of coeff_taylor; a 15-line rw chain via monomial_single_add, coeff_aeval_X_mul and Polynomial.coeff_X_add_C_pow, used once; mathlib has only the one-variable Polynomial.taylor_coeff.
- action: Keep as private helper for its single call site Roth/Taylor.lean:129 (coeff_taylor_monomial_aux); if coeff_taylor is upstreamed, carry it along with coeff_aeval_X_mul, hasseCoeff_single_add_eq, prod_pow_single_add_tsub.
- Type: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (a : R) {i : σ} (n : ℕ) {k : σ →₀ ℕ}, k i = 0 → (∀ d, (taylor α (monomial k a)).coeff d = eval α (hasseDeriv d (monomial k a))) → ∀ (d : σ →₀ ℕ), (taylor α (monomial (Finsupp.single i n + k) a)).coeff d = eval α (hasseDeriv d (monomial (Finsupp.single i n + k) a))`
- What: Inductive step of multivariate Taylor's theorem on monomials: if the coefficient formula coeff_d(P(X+α)) = (Δ_d P)(α) holds for the monomial a·X^k, and k does not involve variable i, then it holds for a·X_i^n·X^k.
- Hypotheses: `hi : k i = 0` (k does not involve variable i, as supplied by `Finsupp.induction`'s `single_add` case); `ih` is the induction hypothesis for `monomial k a`, for all d. `[CommSemiring R]` from the section variable (needed by `taylor`, `hasseDeriv`).
- Uses from project: `MvPolynomial.taylor`, `MvPolynomial.taylor_X`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.hasseCoeff_eq_zero_iff` (Roth/HasseDeriv.lean), `MvPolynomial.coeff_aeval_X_mul` (private), `MvPolynomial.hasseCoeff_single_add_eq` (private), `MvPolynomial.prod_pow_single_add_tsub` (private); implicitly `MvPolynomial.hasseCoeff` via `hasseDeriv_monomial`.
- Used by: Roth/Taylor.lean: `coeff_taylor_monomial_aux` (private, l.124; `exact coeff_taylor_monomial_single_add_aux α a n (Finsupp.notMem_support_iff.1 hi) ih d` at l.129) only. `grep -rn coeff_taylor_monomial_single_add_aux Roth/` gives the definition (l.101) and that single use. Transitively: `coeff_taylor` and everything downstream of Taylor's theorem (`degreeOf_taylor_le`, `eq_sum_box_hasseDeriv`, `eva

### #62 lemma MvPolynomial.coeff_taylor_monomial_aux (private, Roth/Taylor.lean:120)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private monomial case of coeff_taylor, a Finsupp.induction on the exponent whose zero case uses hasseDeriv_C and whose step is coeff_taylor_monomial_single_add_aux; used once; mathlib has only the one-variable Polynomial.taylor_coeff.
- action: Keep as private helper for its single call site Roth/Taylor.lean:138 (coeff_taylor, monomial case); if coeff_taylor is upstreamed, carry it along with coeff_taylor_monomial_single_add_aux and its three private helpers.
- Type: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (d k : σ →₀ ℕ) (a : R), (taylor α (monomial k a)).coeff d = eval α (hasseDeriv d (monomial k a))`
- What: Multivariate Taylor's theorem (coefficient form) for a single monomial: the coefficient at d of (a·X^k)(X + α) is the value at α of the Hasse derivative Δ_d(a·X^k).
- Hypotheses: none beyond `[CommSemiring R]` from the section variable (needed by `taylor`, `hasseDeriv`).
- Uses from project: `MvPolynomial.taylor`, `MvPolynomial.taylor_C` (simp), `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_C` (Roth/HasseDeriv.lean:126), `MvPolynomial.coeff_taylor_monomial_single_add_aux` (private, Roth/Taylor.lean:101); transitively `coeff_aeval_X_mul`, `hasseCoeff_single_add_eq`, `prod_pow_single_add_tsub`, `hasseDeriv_monomial`.
- Used by: Roth/Taylor.lean:138 `coeff_taylor` (monomial case of `MvPolynomial.induction_on'`) only; `grep -rn coeff_taylor_monomial_aux Roth/` gives just the definition (l.120) and that use. Transitively everything downstream of `coeff_taylor` (`degreeOf_taylor_le` l.173, `eq_sum_box_hasseDeriv` l.202, Roth/Index.lean:64,153,158, ...).

### #63 theorem MvPolynomial.coeff_taylor (public, Roth/Taylor.lean:134)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Multivariate Taylor theorem in coefficient form, coeff_d P(X + α) = (Δ_d P)(α), is the standard defining property of multi-index Hasse derivatives and is absent from mathlib (only univariate Polynomial.taylor_coeff); the statement is maximally general but must ship stated against the generalised MvPolynomial.hasseDeriv (Finsupp.choose coefficient), so it inherits the parent's restate-first requirement.
- action: Upstream with MvPolynomial.taylor and MvPolynomial.hasseDeriv in a new Mathlib/Algebra/MvPolynomial/Taylor.lean (statement unchanged, proof re-run after hasseCoeff becomes Finsupp.choose), promoting private helper coeff_aeval_X_mul to a public lemma; locally keep as is (used in Roth/Index.lean:64,153,158 and Roth/Taylor.lean:173,202).
- Type: `{σ R : Type*} [CommSemiring R] (α : σ → R) (d : σ →₀ ℕ) (P : MvPolynomial σ R) : (taylor α P).coeff d = eval α (hasseDeriv d P)`
- What: Taylor's theorem for multivariate polynomials, coefficient form: the coefficient of `X^d` in the translate `P(X + α)` is the value at `α` of the `d`-th Hasse derivative `Δ_d P`.
- Hypotheses: `[CommSemiring R]` (section variable); none else.
- Uses from project: `MvPolynomial.taylor`, `MvPolynomial.hasseDeriv`, private `coeff_taylor_monomial_aux` (which uses private `coeff_taylor_monomial_single_add_aux`, `coeff_aeval_X_mul`, `hasseCoeff_single_add_eq`, `prod_pow_single_add_tsub`, and public `taylor_X`, `hasseDeriv_monomial`, `hasseDeriv_C`, `hasseCoeff`, `hasseCoeff_eq_zero_iff`)
- Used by: Roth/Taylor.lean:173 (`degreeOf_taylor_le`), Roth/Taylor.lean:202 (`eq_sum_box_hasseDeriv`), Roth/Index.lean:64 (private `mem_support_taylor_iff`), Roth/Index.lean:153 and :158 (`index_eq_weightedOrder_div`)

### #64 theorem MvPolynomial.eval_taylor (public, Roth/Taylor.lean:141)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Evaluation of the translate, eval x (P(X + α)) = P(x + α), is the multivariate counterpart of mathlib's Polynomial.taylor_eval and belongs to the YES-add-as-is MvPolynomial.taylor API, but it should ship in the verified more general aeval form (evaluation in any commutative R-algebra S) with the eval statement as a one-line corollary.
- action: Upstream with MvPolynomial.taylor in new Mathlib/Algebra/MvPolynomial/Taylor.lean as aeval_taylor (proof rw [taylor_apply, comp_aeval_apply]; simp, evidence item 4) plus eval_taylor as its specialisation; locally keep (unused in project, zero call sites; no edits needed).
- Type: `∀ {σ R : Type*} [CommSemiring R] (α x : σ → R) (P : MvPolynomial σ R), (eval x) ((taylor α) P) = (eval fun j ↦ x j + α j) P`
- What: Evaluating the translate `P(X + α)` at the point `x` equals evaluating `P` at the shifted point `x + α`.
- Hypotheses: `[CommSemiring R]` (forced by `MvPolynomial`); no propositional hypotheses.
- Uses from project: `MvPolynomial.taylor`
- Used by: unused in project (`grep -rn eval_taylor Roth/` finds only the declaration; `git log -S eval_taylor` shows it present since the initial autoformalisation commit 3cab03b, never consumed).

### #65 theorem MvPolynomial.taylor_taylor (public, Roth/Taylor.lean:146)
- verdict: YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: The additive composition law of translations, P(X + β)(X + α) = P(X + α + β), is the exact multivariate counterpart of mathlib's Polynomial.taylor_taylor (used in FieldTheory/Laurent.lean and Polynomial/Taylor.lean) and is core API of the YES-add-as-is MvPolynomial.taylor; it is already maximally general (CommSemiring forced by MvPolynomial) and only needs the cosmetic restatement taylor (α + β) on the RHS before shipping.
- action: Upstream with MvPolynomial.taylor in new Mathlib/Algebra/MvPolynomial/Taylor.lean, stated as taylor α (taylor β P) = taylor (α + β) P (Pi addition, matching Polynomial.taylor_taylor; evidence item 4) plus the bundled companion taylor_comp_taylor (item 5); locally keep (one call site, Roth/Taylor.lean:184 taylor_neg_taylor).
- Type: `∀ {σ R : Type*} [CommSemiring R] (α β : σ → R) (P : MvPolynomial σ R), (taylor α) ((taylor β) P) = (taylor fun j ↦ α j + β j) P`
- What: Translating first by `β` and then by `α` is translating by `α + β`: `P(X + β)` evaluated at `X + α` is `P(X + α + β)`.
- Hypotheses: `[CommSemiring R]` (section variable, forced by `MvPolynomial`); no propositional hypotheses.
- Uses from project: `MvPolynomial.taylor`
- Used by: Roth/Taylor.lean:184 (`taylor_neg_taylor`, via `simp [taylor_taylor]`), which in turn feeds `taylor_injective` and `taylor_eq_zero_iff` (Roth/Taylor.lean) and through them Roth/Index.lean. No other direct uses (`grep -rn taylor_taylor Roth/`).

### #66 theorem MvPolynomial.taylor_zero (public, Roth/Taylor.lean:152)
- verdict: INHERITED-YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Glue simp lemma for MvPolynomial.taylor (translation by 0 is the identity), proved by unfolding taylor plus mathlib's aeval_X_left_apply; multivariate analogue of Polynomial.taylor_zero, ships with the YES-add-as-is parent, but should be restated with Pi zero since the current fun-form LHS does not fire on taylor 0 P.
- action: Upstream with MvPolynomial.taylor in new Mathlib/Algebra/MvPolynomial/Taylor.lean stated as @[simp] taylor 0 P = P (plus bundled taylor_zero' : taylor 0 = AlgHom.id R _), both compiled in evidence; locally keep (fires implicitly in simp of taylor_neg_taylor, Roth/Taylor.lean:184).
- Type: `∀ {σ R : Type*} [CommSemiring R] (P : MvPolynomial σ R), (taylor fun _ ↦ (0 : R)) P = P`
- What: Translation by the zero vector is the identity: `P(X + 0) = P`.
- Hypotheses: `[CommSemiring R]` (section variable); none else.
- Uses from project: `MvPolynomial.taylor`
- Used by: no use by name in `Roth/` (`grep -rn taylor_zero Roth/` finds only the declaration). It is `@[simp]` and fires implicitly in `MvPolynomial.taylor_neg_taylor` (Roth/Taylor.lean:184, `simp [taylor_taylor]`): evidence item 4 shows that `simp [taylor_taylor, -taylor_zero]` leaves `taylor (fun j ↦ 0) P = P` unsolved.

### #67 theorem MvPolynomial.taylor_map (public, Roth/Taylor.lean:157)
- verdict: YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Naturality of multivariate translation in the coefficient ring, the exact counterpart of mathlib's simp lemma Polynomial.map_taylor (consumed in RingTheory/Polynomial/Resultant/Basic.lean); maximally general and core API of the YES-add-as-is MvPolynomial.taylor, but unused locally and should ship reoriented as @[simp] map_taylor with an import-robust proof.
- action: Upstream with MvPolynomial.taylor in new Mathlib/Algebra/MvPolynomial/Taylor.lean as @[simp] map_taylor (map f (taylor α P) = taylor (f ∘ α) (map f P), proof simp [taylor, map_bind₁]; evidence items 1b and 4); locally keep (no call sites; source note clean.tex l.154 asks for coefficient-map compatibility).
- Type: `∀ {σ R : Type*} [CommSemiring R] {S : Type*} [CommSemiring S] (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R), (taylor fun j ↦ f (α j)) (map f P) = map f ((taylor α) P)`
- What: Translation commutes with change of coefficient ring: applying `f` to the coefficients of `P(X + α)` gives `(f P)(X + f(α))`.
- Hypotheses: `[CommSemiring R]`, `[CommSemiring S]` (forced by `MvPolynomial`); no propositional hypotheses.
- Uses from project: `MvPolynomial.taylor`
- Used by: unused in project (`grep -rn taylor_map Roth/` finds only the declaration at Roth/Taylor.lean:157).

### #68 theorem MvPolynomial.taylor_rename (public, Roth/Taylor.lean:164)
- verdict: YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Naturality of multivariate translation in the variable set (taylor commutes with rename), the counterpart of mathlib's rename_expand / bind₁_rename for the new operator; maximally general (any f, no injectivity), core API of the YES-add-as-is MvPolynomial.taylor, used by Roth/Index.lean index_rename; proof should switch to an import-robust bind₁ form.
- action: Upstream with MvPolynomial.taylor in new Mathlib/Algebra/MvPolynomial/Taylor.lean keeping the current statement and orientation, with proof simp [taylor, bind₁_rename, rename_bind₁, Function.comp_def] (evidence item 1b); locally keep (call site Roth/Index.lean:216).
- Type: `∀ {σ R : Type*} [CommSemiring R] {τ : Type*} (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R), (taylor α) ((rename f) P) = (rename f) ((taylor (α ∘ f)) P)`
- What: Translating a renamed polynomial by `α` is the same as renaming the polynomial translated by the pulled-back point `α ∘ f`: `(f_* P)(X + α) = f_*(P(X + α∘f))`.
- Hypotheses: `[CommSemiring R]` (forced by `MvPolynomial`); `f : σ → τ` arbitrary (no injectivity); no propositional hypotheses.
- Uses from project: `MvPolynomial.taylor`
- Used by: Roth/Index.lean:216 (`index_rename`, `rw [index, index, taylor_rename, support_rename_of_injective hf, ...]`).

### #69 theorem MvPolynomial.degreeOf_taylor_le (public, Roth/Taylor.lean:170)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Translation preserves the degree in each variable; the inequality is real content (needs coeff_taylor) for the YES-add-as-is MvPolynomial.taylor, but the standard (and mathlib-univariate natDegree_taylor) form is the equality, which holds over any CommSemiring and was compiled (degreeOf_taylor in the evidence file).
- action: Upstream as @[simp] degreeOf_taylor (equality, CommSemiring, proof in evidence/MvPolynomial.degreeOf_taylor_le/variants.lean) in new Mathlib/Algebra/MvPolynomial/Taylor.lean with the MvPolynomial.taylor PR, keeping degreeOf_taylor_le as the .le corollary; the call site Roth/Index.lean:229 needs no change.
- Type: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (j : σ) (P : MvPolynomial σ R), degreeOf j (taylor α P) ≤ degreeOf j P`
- What: Translating `P ↦ P(X + α)` does not increase the degree in any single variable `X j`.
- Hypotheses: `[CommSemiring R]` only (section variable; forced by `MvPolynomial`).
- Uses from project: `MvPolynomial.taylor`, `MvPolynomial.coeff_taylor`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` (and implicitly `MvPolynomial.hasseDeriv`)
- Used by: Roth/Index.lean:229 (`index_le_card`: `((degreeOf_taylor_le α j P).trans (hd j))`). No other use (`grep -rn degreeOf_taylor_le Roth/`).

### #70 theorem MvPolynomial.taylor_neg_taylor (public, Roth/Taylor.lean:182)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Translation by -α inverts translation by α is core API of the YES-add-as-is MvPolynomial.taylor, but mathlib's univariate precedent ships it only as the two inverse fields of the AlgEquiv Polynomial.taylorEquiv (with taylorEquiv_symm), so the mathlib form is the bundled MvPolynomial.taylorEquiv plus both one-sided inverses with Pi negation, all compiled in evidence.
- action: In the MvPolynomial.taylor upstream PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) state taylor_neg_taylor as taylor (-α) (taylor α P) = P, add taylor_taylor_neg and taylorEquiv with coe_taylorEquiv and taylorEquiv_symm (evidence items 3-5); locally keep (call sites Roth/Taylor.lean:188 taylor_injective, Roth/Taylor.lean:208 eq_sum_box_hasseDeriv).
- Type: `∀ {σ A : Type*} [CommRing A] (α : σ → A) (P : MvPolynomial σ A), (taylor fun j ↦ -α j) ((taylor α) P) = P`
- What: Translating by `α` and then by `-α` gives back the polynomial: `P(X + α)(X - α) = P(X)`. So translation by `-α` is a left inverse of translation by `α`.
- Hypotheses: `[CommRing A]` (section variable; negation is needed); no propositional hypotheses.
- Uses from project: `MvPolynomial.taylor`, `MvPolynomial.taylor_taylor`, `MvPolynomial.taylor_zero` (simp lemma, used implicitly)
- Used by: Roth/Taylor.lean:188 (`taylor_injective`, via `Function.LeftInverse.injective`), Roth/Taylor.lean:208 (`eq_sum_box_hasseDeriv`, first `calc` step). Indirect: `taylor_eq_zero_iff` (through `taylor_injective`, Roth/Taylor.lean), `eval_eq_sum_box` (Roth/Taylor.lean) and so Roth/Main.lean:390. No direct uses outside Roth/Taylor.lean (`grep -rn taylor_neg_taylor Roth/`).

### #71 theorem MvPolynomial.taylor_injective (public, Roth/Taylor.lean:187)
- verdict: YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Injectivity of multivariate translation over a commutative ring is the exact analogue of mathlib's standalone Polynomial.taylor_injective (kept in mathlib alongside taylorEquiv), is absent for MvPolynomial, and is maximally general since an explicit counterexample over the semiring ℕ∞ shows CommRing cannot be weakened to CommSemiring.
- action: Ship in the MvPolynomial.taylor upstream PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) next to taylor_neg_taylor and taylorEquiv, with proof (taylorEquiv α).injective and the simp companion taylor_inj mirroring Polynomial.taylor_inj; locally keep (only call site Roth/Taylor.lean:193 taylor_eq_zero_iff).
- Type: `∀ {σ A : Type*} [CommRing A] (α : σ → A), Function.Injective ⇑(taylor α : MvPolynomial σ A →ₐ[A] MvPolynomial σ A)`
- What: Over a commutative ring, the translation `P ↦ P(X + α)` is injective: `P(X + α) = Q(X + α)` implies `P = Q`.
- Hypotheses: `[CommRing A]` (section variable; needed, see Phase 4); no propositional hypotheses.
- Uses from project: `MvPolynomial.taylor`, `MvPolynomial.taylor_neg_taylor`
- Used by: Roth/Taylor.lean:193 (`taylor_eq_zero_iff`, via `(taylor_injective α).eq_iff' (map_zero _)`). `taylor_eq_zero_iff` is a `@[simp]` lemma not referenced by name elsewhere (`grep -rn taylor_eq_zero_iff Roth/`). No other uses in `Roth/`.

### #72 theorem MvPolynomial.taylor_eq_zero_iff (public, Roth/Taylor.lean:192)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Multivariate analogue of mathlib's simp lemma Polynomial.taylor_eq_zero (stated over a Semiring), absent for MvPolynomial; the project proves it over CommRing via injectivity, but a compiled top-total-degree-coefficient proof shows it holds over any CommSemiring, where injectivity itself fails.
- action: Upstream in the MvPolynomial.taylor PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) restated over CommSemiring, named taylor_eq_zero to mirror Polynomial.taylor_eq_zero, with helper coeff_taylor_of_totalDegree_le (evidence variants.lean); locally keep (implicit simp uses at Roth/Index.lean:80 and :169).
- Type: `∀ {σ A : Type*} [CommRing A] (α : σ → A) (P : MvPolynomial σ A), taylor α P = 0 ↔ P = 0`
- What: A multivariate polynomial vanishes iff its translate `P(X + α)` vanishes. Tagged `@[simp]`.
- Hypotheses: `[CommRing A]` (section variable; not needed, see Phase 4); no propositional hypotheses.
- Uses from project: `MvPolynomial.taylor`, `MvPolynomial.taylor_injective`
- Used by: never referenced by name (`grep -rn taylor_eq_zero_iff Roth/` gives only its declaration). As a `@[simp]` lemma it is the natural closer for the `simp`/`simpa` calls on translated polynomials in Roth/Index.lean:80 (`exists_weight_eq_index`, support of `taylor α P` nonempty from `hP : P ≠ 0`) and Roth/Index.lean:169 (`hfin`, `weightedOrder` of `↑(taylor α R)` is not `⊤` for `R ≠ 0`); these implicit

### #73 theorem MvPolynomial.eq_sum_box_hasseDeriv (public, Roth/Taylor.lean:197)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Multivariate Taylor expansion P = sum (Δ_d P)(α) (X - α)^d is standard and absent from mathlib (only univariate Polynomial.sum_taylor_eq), but the box form with Fintype, DecidableEq, a degree hypothesis and Roth.box is a corollary; the mathlib form is the hypothesis-free support-sum analogue of Polynomial.sum_taylor_eq plus an arbitrary-superset version, both compiled in evidence.
- action: Upstream in the MvPolynomial.taylor PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) as sum_taylor_eq (arbitrary σ, Finsupp.prod) and eq_sum_hasseDeriv_of_subset, with the box statement over Finset.Iic (Finsupp.equivFunOnFinite.symm r) as corollary (evidence items 2-4); locally keep (only caller eval_eq_sum_box at Roth/Taylor.lean:220, used at Roth/Main.lean:390).
- Type: `{σ A : Type*} [CommRing A] [Fintype σ] [DecidableEq σ] (α : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) : P = ∑ d ∈ Roth.box r, C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j`
- What: Taylor's expansion of a multivariate polynomial about `α`: if `deg_{X_j} P ≤ r_j` for every `j`, then `P = Σ_{d ≤ r} (Δ_d P)(α) ∏_j (X_j − α_j)^{d_j}`.
- Hypotheses: `[CommRing A]` (subtraction in `X j - C (α j)`, and `taylor_neg_taylor`), `[Fintype σ]` (the product `∏ j` and `Roth.box`), `[DecidableEq σ]` (for `Roth.box`), `hP` (degree bound per variable, so that the box contains all nonzero Taylor coefficients).
- Uses from project: `MvPolynomial.taylor`, `MvPolynomial.coeff_taylor`, `MvPolynomial.taylor_neg_taylor`, `MvPolynomial.taylor_monomial`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, `Roth.box`, `Roth.mem_box`
- Used by: Roth/Taylor.lean:220 (`eval_eq_sum_box`, which is in turn used at Roth/Main.lean:390). No other project uses (`grep -rn eq_sum_box_hasseDeriv Roth/`).

### #74 theorem MvPolynomial.eval_eq_sum_box (public, Roth/Taylor.lean:217)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Evaluated multivariate Taylor formula P(x) = sum (Δ_d P)(α) (x - α)^d is standard and absent from mathlib (no MvPolynomial.taylor, no univariate evaluated-sum form either), but the box form is a corollary of the verified CommSemiring hypothesis-free form eval (y + α) P = sum over supp(taylor α P) of (Δ_d P)(α) y^d plus a superset-s version, all compiled in evidence.
- action: Ship in the MvPolynomial Taylor PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) as eval_add_eq_sum_of_subset (CommSemiring, arbitrary σ) with the ring x - α form and the Finset.Iic box form as corollaries (evidence items 2-4); locally keep (one caller Roth/Main.lean:390, unchanged except the box spelling when Roth.box is replaced).
- Type: `{σ A : Type*} [CommRing A] [Fintype σ] [DecidableEq σ] (α x : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) : eval x P = ∑ d ∈ Roth.box r, eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j`
- What: Taylor's theorem in evaluated form: if `deg_{X_j} P ≤ r_j` for all `j`, then for every point `x`, `P(x) = Σ_{d ≤ r} (Δ_d P)(α) ∏_j (x_j − α_j)^{d_j}`.
- Hypotheses: `[CommRing A]` (subtraction `x j - α j`), `[Fintype σ]` (`∏ j`, `Roth.box`), `[DecidableEq σ]` (`Roth.box`), `hP` (degree box contains all nonzero Taylor coefficients).
- Uses from project: `MvPolynomial.eq_sum_box_hasseDeriv`, `MvPolynomial.hasseDeriv`, `Roth.box`
- Used by: Roth/Main.lean:390 (`abs_eval_lt_of_le_index`, `rw [eval_eq_sum_box (fun _ ↦ α) (fun j ↦ (h j : ℝ) / q j) r Q hd]`). Also named in the module docstring Roth/Taylor.lean:26. No other uses (`grep -rn eval_eq_sum_box Roth/`).

### #75 def Roth.normOne (public, Roth/CoeffNorm.lean:47)
- verdict: YES-but-generalise-first | cost: MODERATE | junk: KEEP
- rationale: The l1 coefficient norm (the length L(P) of a polynomial) is absent from mathlib, whose Analysis/Polynomial/Norm.lean lists l^p norms incl. l^1 as a TODO; the Z-only def generalises verbatim to MvPolynomial over any SeminormedCommRing with nonneg, coeff bound, triangle and submultiplicativity re-proved and a bridge back to Roth.normOne (compiled).
- action: Restate as a norm-valued l1Norm on MvPolynomial σ R for [SeminormedCommRing R] (with a univariate Polynomial companion next to Polynomial.supNorm in Mathlib/Analysis/Polynomial/Norm.lean), keep Roth.normOne as the R = ℤ abbreviation via Int.norm_eq_abs, and re-aim the 13 CoeffNorm.lean API lemmas at the general def before upstreaming.
- Type: `{σ : Type*} (P : MvPolynomial σ ℤ) : ℝ`
- What: The ℓ¹ norm `‖P‖₁ = ∑_e |a_e|` of the integer coefficients of a multivariate polynomial, as a real number.
- Hypotheses: none (no typeclass assumptions on `σ`).
- Uses from project: `[]`
- Used by: Roth/CoeffNorm.lean only (no other file mentions `normOne`; Theta.lean and Separation.lean import the module but use only the downstream `abs_coeff_det_hasseDeriv_le`/`abs_coeff_diag_le`/`abs_eval_le`, whose statements do not mention `normOne`). Within CoeffNorm.lean: `normOne_nonneg` 50, `normOne_eq_sum_of_support_subset` 54, `normOne_monomial` 59, `normOne_zero` 66, `abs_coeff_le_normOne` 71, `n

### #76 theorem Roth.normOne_nonneg (public, Roth/CoeffNorm.lean:50)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Standard nonnegativity companion of the l1 coefficient norm (cf. Polynomial.supNorm_nonneg, gaussNorm_nonneg, mahlerMeasure_nonneg); mathlib has no l1 norm on polynomials, and the same one-line proof compiles verbatim for MvPolynomial.l1Norm over any SeminormedCommRing (Evidence.l1Norm_nonneg).
- action: Ship as MvPolynomial.l1Norm_nonneg (proof Finset.sum_nonneg fun _ _ => norm_nonneg _) in the same PR as MvPolynomial.l1Norm (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean); keep Roth.normOne_nonneg as the R = ℤ specialisation used by normOne_prod_le (line 107) and normOne_det_le (line 128).
- Type: `{σ : Type*} (P : MvPolynomial σ ℤ) : 0 ≤ Roth.normOne P`
- What: The ℓ¹ coefficient norm `‖P‖₁ = ∑ |a_e|` of an integer polynomial is nonnegative.
- Hypotheses: none.
- Uses from project: `Roth.normOne`
- Used by: Roth/CoeffNorm.lean:107 (`normOne_prod_le`, as the nonnegativity argument of `Finset.le_prod_of_submultiplicative_of_nonneg`), Roth/CoeffNorm.lean:128 (`normOne_det_le`, inside `Finset.prod_le_prod₀`). No uses outside CoeffNorm.lean (`grep -rn normOne_nonneg Roth/`).

### #77 theorem Roth.normOne_eq_sum_of_support_subset (public, Roth/CoeffNorm.lean:54)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Standard support-enlargement API lemma for the l1 coefficient norm (analogue of Polynomial.sum_eq_of_subset and Finsupp.sum_of_support_subset); mathlib has no l1 polynomial norm, and the same proof compiles for MvPolynomial.l1Norm over any SeminormedCommRing (evidence file, diagnostics clean).
- action: Ship as MvPolynomial.l1Norm_eq_sum_of_support_subset over [SeminormedCommRing R] in the same PR as MvPolynomial.l1Norm (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the R = ℤ form for the call sites Roth/CoeffNorm.lean:61, 79, 80, 81.
- Type: `{σ : Type*} {P : MvPolynomial σ ℤ} {s : Finset (σ →₀ ℕ)} (hs : P.support ⊆ s) : Roth.normOne P = ∑ d ∈ s, |((P.coeff d : ℤ) : ℝ)|`
- What: The ℓ¹ coefficient norm `‖P‖₁ = ∑_{d ∈ supp P} |a_d|` may be computed as a sum over any finite set of exponents `s` containing the support.
- Hypotheses: `hs : P.support ⊆ s`.
- Uses from project: `Roth.normOne`
- Used by: Roth/CoeffNorm.lean:61 (`normOne_monomial`, with `support_monomial_subset`), Roth/CoeffNorm.lean:79, 80, 81 (`normOne_add_le`, three rewrites to put `P + Q`, `P`, `Q` over `P.support ∪ Q.support`). No uses outside CoeffNorm.lean (`grep -rn normOne_eq_sum_of_support_subset Roth/`).

### #78 theorem Roth.normOne_monomial (public, Roth/CoeffNorm.lean:59)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Standard simp-style evaluation lemma for the new l1 coefficient norm (exact analogue of mathlib's Polynomial.supNorm_monomial and Polynomial.gaussNorm_monomial); mathlib has no l1 polynomial norm and the verbatim proof compiles for MvPolynomial.l1Norm over any SeminormedCommRing (evidence file, diagnostics clean).
- action: Ship as MvPolynomial.l1Norm_monomial over [SeminormedCommRing R] in the same PR as MvPolynomial.l1Norm (Mathlib/Analysis/Polynomial/Norm.lean next to Polynomial.supNorm_monomial, or a new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the R = ℤ form for call sites Roth/CoeffNorm.lean:102, 108, 155.
- Type: `{σ : Type*} (e : σ →₀ ℕ) (c : ℤ) : Roth.normOne (MvPolynomial.monomial e c) = |(c : ℝ)|`
- What: The ℓ¹ coefficient norm of the monomial `c X^e` is `|c|`.
- Hypotheses: none.
- Uses from project: `Roth.normOne`, `Roth.normOne_eq_sum_of_support_subset`
- Used by: Roth/CoeffNorm.lean:102 (`normOne_mul_le`, as a simp lemma for the product of two monomials), Roth/CoeffNorm.lean:108 (`normOne_prod_le`, `normOne_monomial 0 1` gives `normOne 1 ≤ 1`), Roth/CoeffNorm.lean:155 (`normOne_hasseDeriv_le`, rewriting each Hasse-derivative monomial term). No uses outside CoeffNorm.lean (`grep -rn normOne_monomial Roth/`).

### #79 theorem Roth.normOne_zero (public, Roth/CoeffNorm.lean:66)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Standard simp-normal zero lemma for the new l1 coefficient norm (exact analogue of mathlib's Polynomial.supNorm_zero and Polynomial.gaussNorm_zero); mathlib has no l1 polynomial norm and the verbatim proof compiles for MvPolynomial.l1Norm over any SeminormedCommRing (evidence file, diagnostics clean).
- action: Ship as @[simp] MvPolynomial.l1Norm_zero over [SeminormedCommRing R] in the same PR as MvPolynomial.l1Norm (Mathlib/Analysis/Polynomial/Norm.lean next to Polynomial.supNorm_zero, or a new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the R = ℤ form for call site Roth/CoeffNorm.lean:92.
- Type: `{σ : Type*} : Roth.normOne (0 : MvPolynomial σ ℤ) = 0`
- What: The ℓ¹ coefficient norm of the zero polynomial is `0`.
- Hypotheses: none.
- Uses from project: `Roth.normOne`
- Used by: Roth/CoeffNorm.lean:92 (`normOne_sum_le`, as `normOne_zero.le` for `Finset.le_sum_of_subadditive`); also tagged `@[simp]`, so available to any `simp` call in CoeffNorm.lean on `normOne 0`. No uses outside CoeffNorm.lean (`grep -rn normOne_zero Roth/`).

### #80 theorem Roth.abs_coeff_le_normOne (public, Roth/CoeffNorm.lean:71)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Basic coefficient-domination lemma for the new l1 coefficient norm (exact analogue of mathlib's Polynomial.le_supNorm and Polynomial.le_gaussNorm); mathlib has no l1 polynomial norm, and the project's one-call proof via Finsupp.single_eval_le_sum compiles verbatim for MvPolynomial.l1Norm over any SeminormedCommRing (evidence file, diagnostics clean).
- action: Ship as MvPolynomial.norm_coeff_le_l1Norm (or le_l1Norm, mirroring Polynomial.le_supNorm) over [SeminormedCommRing R] in the same PR as MvPolynomial.l1Norm (Mathlib/Analysis/Polynomial/Norm.lean or a new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the ℤ form for the call site Roth/CoeffNorm.lean:266 via Int.norm_eq_abs.
- Type: `{σ : Type*} (P : MvPolynomial σ ℤ) (d : σ →₀ ℕ) : |((P.coeff d : ℤ) : ℝ)| ≤ Roth.normOne P`
- What: Each coefficient of an integer polynomial is bounded in absolute value by the ℓ¹ coefficient norm (`|a_d| ≤ ∑_e |a_e|`).
- Hypotheses: none.
- Uses from project: `Roth.normOne`
- Used by: Roth/CoeffNorm.lean:266 (first step of the `calc` in `Roth.abs_coeff_det_hasseDeriv_le`, Lemma 3). No other uses project-wide (`grep -rn abs_coeff_le_normOne Roth/`).

### #81 theorem Roth.normOne_add_le (public, Roth/CoeffNorm.lean:77)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Triangle inequality for the l1 coefficient norm (polynomial length), basic API of the parent l1Norm which mathlib lacks (Norm.lean TODO); the project proof compiles verbatim for MvPolynomial.l1Norm over any SeminormedCommRing and also for an AbsoluteValue-based l1 norm on a CommSemiring (evidence file, diagnostics clean).
- action: Ship as MvPolynomial.l1Norm_add_le over [SeminormedCommRing R] in the MvPolynomial.l1Norm PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the ℤ form for the call site Roth/CoeffNorm.lean:92 (normOne_sum_le) via Int.norm_eq_abs.
- Type: `{σ : Type*} (P Q : MvPolynomial σ ℤ) : Roth.normOne (P + Q) ≤ Roth.normOne P + Roth.normOne Q`
- What: Triangle inequality for the ℓ¹ coefficient norm: `∑ |a_e + b_e| ≤ ∑ |a_e| + ∑ |b_e|`.
- Hypotheses: none.
- Uses from project: `Roth.normOne`, `Roth.normOne_eq_sum_of_support_subset`
- Used by: Roth/CoeffNorm.lean:92 (`Roth.normOne_sum_le`, as the subadditivity argument of `Finset.le_sum_of_subadditive`). No other uses project-wide (`grep -rn normOne_add_le Roth/`); indirectly feeds `normOne_mul_le`, `normOne_det_le`, `normOne_hasseDeriv_le` and Lemma 3 through `normOne_sum_le`.

### #82 theorem Roth.normOne_neg (public, Roth/CoeffNorm.lean:86)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Standard negation-invariance lemma for the new l1 coefficient norm (analogue of mathlib's MvPowerSeries.gaussNorm_neg and lp.norm_neg); mathlib has no l1 polynomial norm and the verbatim proof compiles for MvPolynomial.l1Norm over any SeminormedCommRing (evidence file, diagnostics clean).
- action: Ship as @[simp] MvPolynomial.l1Norm_neg over [SeminormedCommRing R] in the same PR as MvPolynomial.l1Norm (Mathlib/Analysis/Polynomial/Norm.lean or a new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the R = ℤ form for call site Roth/CoeffNorm.lean:127 (normOne_det_le).
- Type: `{σ : Type*} (P : MvPolynomial σ ℤ) : Roth.normOne (-P) = Roth.normOne P`
- What: The ℓ¹ coefficient norm is invariant under negation, `‖-P‖₁ = ‖P‖₁`.
- Hypotheses: none.
- Uses from project: `Roth.normOne`
- Used by: Roth/CoeffNorm.lean:127 (`normOne_det_le`, in `simpa [h, normOne_neg]` to absorb the sign `-1` of an odd permutation). No uses outside CoeffNorm.lean (`grep -rn normOne_neg Roth/`).

### #83 theorem Roth.normOne_sum_le (public, Roth/CoeffNorm.lean:90)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Finite-sum triangle inequality for the l1 coefficient norm; a one-call Finset.le_sum_of_subadditive lemma but standard named-norm API exactly like mathlib's norm_sum_le / gauge_sum_le / eLpNorm_sum_le, with 4 project call sites; proof compiles verbatim for MvPolynomial.l1Norm over any SeminormedCommRing and for an AbsoluteValue-based l1 norm (evidence file clean).
- action: Ship as MvPolynomial.l1Norm_sum_le over [SeminormedCommRing R] in the MvPolynomial.l1Norm PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the ℤ form for call sites Roth/CoeffNorm.lean:99,101,123,152 via Int.norm_eq_abs.
- Type: `{σ : Type*} {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℤ) : Roth.normOne (∑ i ∈ s, f i) ≤ ∑ i ∈ s, Roth.normOne (f i)`
- What: Triangle inequality for the ℓ¹ coefficient norm over a finite sum: `‖∑ᵢ fᵢ‖₁ ≤ ∑ᵢ ‖fᵢ‖₁`.
- Hypotheses: none.
- Uses from project: `Roth.normOne`, `Roth.normOne_zero`, `Roth.normOne_add_le`
- Used by: Roth/CoeffNorm.lean:99 and :101 (`Roth.normOne_mul_le`, twice), Roth/CoeffNorm.lean:123 (`Roth.normOne_det_le`), Roth/CoeffNorm.lean:152 (`Roth.normOne_hasseDeriv_le`). No uses outside CoeffNorm.lean (`grep -rn normOne_sum_le Roth/`).

### #84 theorem Roth.normOne_mul_le (public, Roth/CoeffNorm.lean:96)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Submultiplicativity of the l1 coefficient norm (length L(PQ) ≤ L(P)L(Q), the l1(M) Banach-algebra inequality) is absent from mathlib (no l1 norm on (Mv)Polynomial or AddMonoidAlgebra; only the nonarchimedean gaussNorm_mul_le); the Z-only proof compiles with abs_mul replaced by norm_mul_le for MvPolynomial over any SeminormedCommRing, and also for AddMonoidAlgebra R M over a SeminormedRing and any AddMonoid (evidence file clean).
- action: Ship as MvPolynomial.l1Norm_mul_le over [SeminormedCommRing R] in the MvPolynomial.l1Norm PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean), optionally deriving it from an AddMonoidAlgebra l1 norm; keep the Z form for the call site Roth/CoeffNorm.lean:108 (normOne_prod_le) via Int.norm_eq_abs.
- Type: `{σ : Type*} (P Q : MvPolynomial σ ℤ) : Roth.normOne (P * Q) ≤ Roth.normOne P * Roth.normOne Q`
- What: The ℓ¹ coefficient norm (length) of integer multivariate polynomials is submultiplicative: `‖PQ‖₁ ≤ ‖P‖₁ ‖Q‖₁`.
- Hypotheses: none.
- Uses from project: `Roth.normOne`, `Roth.normOne_sum_le`, `Roth.normOne_monomial`
- Used by: Roth/CoeffNorm.lean:108 (`Roth.normOne_prod_le`, passed to `Finset.le_prod_of_submultiplicative_of_nonneg`); mentioned in the module docstring (line 27). No uses outside CoeffNorm.lean (`grep -rn normOne_mul_le Roth/`).

### #85 theorem Roth.normOne_prod_le (public, Roth/CoeffNorm.lean:105)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Finite-product submultiplicativity of the l1 coefficient norm (length of a product of k polynomials) is absent from mathlib (no l1 norm on (Mv)Polynomial, Norm.lean l1 TODO); the project proof compiles verbatim for MvPolynomial over any SeminormedCommRing once a norm-of-one hypothesis is added (NormOneClass R, or the weaker norm 1 le 1), plus a hypothesis-free nonempty variant mirroring Finset.norm_prod_le' (evidence clean).
- action: Ship as MvPolynomial.l1Norm_prod_le [NormOneClass R] and l1Norm_prod_le' (s.Nonempty) in the MvPolynomial.l1Norm PR next to l1Norm_mul_le (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the Z form for the call site Roth/CoeffNorm.lean:127 (normOne_det_le).
- Type: `{σ : Type*} {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℤ) : Roth.normOne (∏ i ∈ s, f i) ≤ ∏ i ∈ s, Roth.normOne (f i)`
- What: The ℓ¹ coefficient norm of a finite product of integer multivariate polynomials is at most the product of their ℓ¹ norms.
- Hypotheses: none.
- Uses from project: `Roth.normOne`, `Roth.normOne_nonneg`, `Roth.normOne_monomial`, `Roth.normOne_mul_le`
- Used by: Roth/CoeffNorm.lean:127 (`Roth.normOne_det_le`, bounding each Leibniz term `∏ i, M (τ i) i`). No other uses (`grep -rn normOne_prod_le Roth/`).

### #86 theorem Roth.normOne_le_card_mul (public, Roth/CoeffNorm.lean:113)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Comparison length L(P) at most #support times a uniform coefficient bound (l1 at most N times sup); a one-call Finset.sum_le_card_nsmul lemma but standard norm-comparison API (cf. norm_le_card_mul_iSup_norm_inner, mahlerMeasure_le_sqrt_natDegree_add_one_mul_supNorm) for the absent l1 norm; proof compiles verbatim for MvPolynomial.l1Norm over any SeminormedCommRing (even any CommSemiring with Norm) and recovers the Z form.
- action: Ship as MvPolynomial.l1Norm_le_card_mul over [SeminormedCommRing R] in the MvPolynomial.l1Norm PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean), optionally with an l1Norm_le_card_support_mul_supNorm companion; keep the Z form for the single call site Roth/CoeffNorm.lean:270 via Int.norm_eq_abs.
- Type: `{σ : Type*} (P : MvPolynomial σ ℤ) {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) : Roth.normOne P ≤ P.support.card * B`
- What: If every coefficient of `P` has absolute value at most `B`, then the ℓ¹ coefficient norm is at most (number of monomials) · `B`.
- Hypotheses: `hB` — uniform bound on all coefficients (only used on the support).
- Uses from project: `Roth.normOne`
- Used by: Roth/CoeffNorm.lean:270 (proof of `Roth.abs_coeff_det_hasseDeriv_le`, Lemma 3). No other uses (`grep -rn normOne_le_card_mul Roth/`).

### #87 theorem Roth.normOne_det_le (public, Roth/CoeffNorm.lean:119)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Leibniz bound n! C^n for the l1 coefficient norm of a determinant is absent from mathlib (Matrix.det_le needs a multiplicative AbsoluteValue, which the l1 norm is not; no l1 polynomial norm exists); the project proof compiles verbatim for MvPolynomial over any SeminormedCommRing with NormOneClass and any Fintype index, and its abstract companion norm_det_le for any SeminormedCommRing with NormOneClass also compiles (evidence clean).
- action: Ship Matrix.norm_det_le [SeminormedCommRing R] [NormOneClass R] (Fintype n) in Mathlib/Analysis/Matrix/Normed.lean (or beside Matrix.det_le in LinearAlgebra/Matrix/AbsoluteValue.lean with an Analysis import) and MvPolynomial.l1Norm_det_le in the MvPolynomial.l1Norm PR; keep the Z/Fin l form for the call site Roth/CoeffNorm.lean:268 (abs_coeff_det_hasseDeriv_le).
- Type: `{σ : Type*} {l : ℕ} (M : Matrix (Fin l) (Fin l) (MvPolynomial σ ℤ)) {C : ℝ} (hM : ∀ μ ν, Roth.normOne (M μ ν) ≤ C) : Roth.normOne M.det ≤ l.factorial * C ^ l`
- What: If every entry of an `l × l` matrix of integer multivariate polynomials has ℓ¹ coefficient norm at most `C`, then its determinant has ℓ¹ norm at most `l! C^l`.
- Hypotheses: `hM` — uniform entrywise ℓ¹ bound `C` (no sign condition needed on `C`).
- Uses from project: `Roth.normOne`, `Roth.normOne_sum_le`, `Roth.normOne_neg`, `Roth.normOne_prod_le`, `Roth.normOne_nonneg`
- Used by: Roth/CoeffNorm.lean:268 (`Roth.abs_coeff_det_hasseDeriv_le`, Lemma 3); mentioned in the module docstring (CoeffNorm.lean:27). No other uses (`grep -rn normOne_det_le Roth/`).

### #88 theorem Roth.abs_coeff_hasseDeriv_le (public, Roth/CoeffNorm.lean:134)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The coefficient bound for (multivariate) Hasse derivatives is standard in Roth-type arguments and absent from mathlib (not even for univariate Polynomial.hasseDeriv); but the Z/abs form with Fintype, box r and uniform bound B is a specialisation of the verified pointwise bound norm of [X^e] Delta_d P at most 2^deg(e+d) times norm of [X^(e+d)] P over any SeminormedCommRing.
- action: Ship MvPolynomial.norm_coeff_hasseDeriv_le (pointwise, SeminormedCommRing, via norm_nsmul_le) plus the box corollary in the MvPolynomial.hasseDeriv PR (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean or an Analysis companion), with a univariate Polynomial.norm_coeff_hasseDeriv_le; keep the Z form for Roth/MainLemma.lean:468 and :509 via Int.norm_eq_abs.
- Type: `{σ : Type*} [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ e, |((P.coeff e : ℤ) : ℝ)| ≤ B) (e : σ →₀ ℕ) : |(((hasseDeriv d P).coeff e : ℤ) : ℝ)| ≤ 2 ^ (∑ j, r j) * B`
- What: If `deg_{X_j} P ≤ r_j` for all `j` and all coefficients of the integer polynomial `P` are bounded by `B` in absolute value, then every coefficient of every Hasse derivative `Δ_d P` is bounded by `2^{r_1+⋯+r_m} B`.
- Hypotheses: `[Fintype σ]` (to form `∑ j, r j`), `hP` (degree box), `hB` (uniform coefficient bound).
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_le_two_pow`
- Used by: Roth/MainLemma.lean:468 (twice, nested, in private `abs_eval_iterated_hasseDeriv_lt_aux`, feeding `Roth.abs_eval_le`); Roth/MainLemma.lean:509 (in private `abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, feeding `Roth.abs_coeff_diag_le`). Not used elsewhere (`grep -rn abs_coeff_hasseDeriv_le Roth/`).

### #89 theorem Roth.normOne_hasseDeriv_le (public, Roth/CoeffNorm.lean:148)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The l1 (length) bound for Hasse derivatives L(Delta_d P) ≤ 2^deg L(P) is the standard Roth-type estimate and absent from mathlib (no l1 norm on polynomials, no MvPolynomial Hasse derivative, no size bound even univariately); the Z/abs box form generalises verbatim to l1Norm over any SeminormedCommRing and to a box-free 2^totalDegree form without Fintype, both compiled with the project statement recovered.
- action: Ship MvPolynomial.l1Norm_hasseDeriv_le_two_pow_totalDegree (plus the degreeOf-box corollary) over [SeminormedCommRing R] in the MvPolynomial.l1Norm / hasseDeriv PR (Mathlib/Analysis/Polynomial/Norm.lean companion or new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the Z form for the single call site Roth/CoeffNorm.lean:269 (abs_coeff_det_hasseDeriv_le) via Int.norm_eq_abs.
- Type: `{σ : Type*} [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) : normOne (hasseDeriv d P) ≤ 2 ^ (∑ j, r j) * normOne P`
- What: If `deg_{X_j} P ≤ r_j` for all `j`, every Hasse derivative `Δ_d P` of the integer polynomial `P` has ℓ¹ coefficient norm at most `2^{r_1+⋯+r_m} ‖P‖₁`.
- Hypotheses: `[Fintype σ]` (to form `∑ j, r j`), `hP` (partial degree box).
- Uses from project: `Roth.normOne`, `Roth.normOne_sum_le`, `Roth.normOne_monomial`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_apply`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_le_two_pow`
- Used by: Roth/CoeffNorm.lean:269 (proof of `Roth.abs_coeff_det_hasseDeriv_le`, Lemma 3). No other use (`grep -rn normOne_hasseDeriv_le Roth/`; line 29 is the module docstring).

### #90 def Roth.diag (public, Roth/CoeffNorm.lean:161)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: diag P is literally the single mathlib term MvPolynomial.aeval (fun _ ↦ Polynomial.X) P (equivalently uniqueAlgEquiv R Unit composed with rename (fun _ ↦ ())), valid over any CommSemiring; mathlib has the map but no name for it, and a one-line abbreviation is not mathlib material; keep it as a project-local name.
- action: Do not upstream; optionally generalise locally to CommSemiring R and bundle as aeval (fun _ ↦ X) : MvPolynomial σ R →ₐ[R] R[X]; re-aim downstream lemmas (natDegree_diag_le via MvPolynomial.aeval_natDegree_le, eval_diag via MvPolynomial.comp_aeval, diag_sub is map_sub); call sites Roth/MainLemma.lean:362-409, 497-538, 553, 602-606 unchanged.
- Type: `{σ : Type*} (P : MvPolynomial σ ℤ) : Polynomial ℤ`
- What: The diagonal substitution `P(x, …, x)`: replaces every variable `X_j` by the single variable `x`.
- Hypotheses: none.
- Uses from project: `[]`
- Used by: Roth/CoeffNorm.lean: `diag_eq_sum` (164), `abs_coeff_diag_le` (174), `natDegree_diag_le` (183), `eval_diag` (193), `diag_sub` (199); Roth/MainLemma.lean: 362, 365, 369, 404, 406, 408 (`diag_sub`), 409 (`simpa [..., diag, ...]` unfolds it), 497, 500, 507, 509, 513, 519, 532, 538, 553, 602 (13 lines outside the declaring file).

### #91 theorem Roth.diag_eq_sum (public, Roth/CoeffNorm.lean:164)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Re-aimed at the mathlib term aeval (fun _ ↦ X), the identity aeval (fun _ ↦ X) P = ∑ k ∈ P.support, monomial k.degree (coeff k P) is absent from mathlib (loogle/leansearch/leanfinder/grep empty), is not a 1-3 call composition, and holds verbatim over any CommSemiring R (and in weighted form X_i ↦ X ^ w i with Finsupp.weight w), all compiled in evidence; upstream the general-R form plus the coefficient corollary.
- action: Upstream to Mathlib/RingTheory/Polynomial/Basic.lean (next to MvPolynomial.aeval_natDegree_le) as MvPolynomial.aeval_X_pow_eq_sum (weighted) with corollaries aeval_X_eq_sum and coeff_aeval_X over [CommSemiring R]; locally restate diag_eq_sum over CommSemiring R (proof unchanged), call sites Roth/CoeffNorm.lean:176 and :185 unaffected.
- Type: `{σ : Type*} (P : MvPolynomial σ ℤ) : diag P = ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k)`
- What: The diagonal substitution `P(x, …, x)` sends each monomial `a_k X^k` to `a_k x^{|k|}`, so `diag P = ∑_k a_k x^{|k|}`.
- Hypotheses: none.
- Uses from project: `Roth.diag`
- Used by: Roth/CoeffNorm.lean:176 (`abs_coeff_diag_le`), Roth/CoeffNorm.lean:185 (`natDegree_diag_le`); no uses outside CoeffNorm.lean.

### #92 theorem Roth.abs_coeff_diag_le (public, Roth/CoeffNorm.lean:174)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Re-aimed at the mathlib term aeval (fun _ ↦ X), the bound norm of coeff n of aeval (fun i ↦ X ^ w i) P at most #support P times B is absent from mathlib (no coefficient API for aeval (fun _ ↦ X) at all) and not composable from current mathlib, and the project proof compiles verbatim over any SeminormedCommRing (weighted, plus a sharper per-degree card form), recovering the Z/abs statement; ship as a corollary of the coeff_aeval_X expansion.
- action: Ship MvPolynomial.norm_coeff_aeval_X_le (sharp, filter by degree = n) and the #support corollary over [SeminormedCommRing R] in the same PR as MvPolynomial.aeval_X_pow_eq_sum / coeff_aeval_X (Mathlib/RingTheory/Polynomial/Basic.lean or an Analysis/Polynomial companion); keep the Z form for the single call site Roth/MainLemma.lean:509 via Int.norm_eq_abs.
- Type: `{σ : Type*} (P : MvPolynomial σ ℤ) {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (n : ℕ) : |(((diag P).coeff n : ℤ) : ℝ)| ≤ P.support.card * B`
- What: Every coefficient of the diagonal specialisation `P(x, …, x)` is bounded in absolute value by the number of terms of `P` times a uniform bound `B` for the coefficients of `P`.
- Hypotheses: `hB` (uniform coefficient bound). No finiteness of `σ`.
- Uses from project: `Roth.diag`, `Roth.diag_eq_sum`
- Used by: Roth/MainLemma.lean:509 (`abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, private, applied to `hasseDeriv j P` with `B := 2^{∑ r_k} B`); also listed in the CoeffNorm.lean module docstring (line 32).

### #93 theorem Roth.natDegree_diag_le (public, Roth/CoeffNorm.lean:183)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: Re-aimed at diag = aeval (fun _ ↦ X), the bound is one call to MvPolynomial.aeval_natDegree_le (n = 1) fed by totalDegree ≤ ∑ degreeOf, itself a one-line simpa from totalDegree_le_degrees_card, degreeOf_def and Multiset.sum_count_eq_card; compiled over any CommSemiring, nothing new for mathlib.
- action: Do not upstream; optionally reprove Roth.natDegree_diag_le as the aeval_natDegree_le composition (needs import Mathlib.RingTheory.Polynomial.Basic in Roth/CoeffNorm.lean), keeping the name for its single call site Roth/MainLemma.lean:513.
- Type: `{σ : Type*} [Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) : (diag P).natDegree ≤ ∑ j, r j`
- What: If `P` has degree at most `r_j` in each variable `x_j`, the diagonal specialisation `P(x, …, x)` has degree at most `∑ r_j`.
- Hypotheses: `[Fintype σ]` (for `∑ j, r j`); `hP` (partial degree bounds).
- Uses from project: `Roth.diag`, `Roth.diag_eq_sum`
- Used by: Roth/MainLemma.lean:513 (private `abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, supplies the degree hypothesis of `norm_coeff_modByMonic_le`).

### #94 theorem Roth.eval_diag (public, Roth/CoeffNorm.lean:193)
- verdict: SKIP | cost: n/a | junk: REMOVE
- rationale: Unused in the project (its only former call site, eval_hasseDeriv_sub_eq_zero, was rewritten in 96928fd to inline MvPolynomial.comp_aeval_apply + Polynomial.aeval_X), and re-aimed at diag = aeval (fun _ ↦ X) it is exactly comp_aeval_apply plus aeval_X over any CommSemiring (compiled); Step 8 REMOVE fires the Step 9a pre-filter.
- action: Delete Roth.eval_diag from Roth/CoeffNorm.lean:190-195 (no call sites in Roth/ or Roth.lean); its content is already spelled inline at Roth/MainLemma.lean:409-410 via MvPolynomial.comp_aeval_apply and Polynomial.aeval_X; deletion needs user sign-off per the earlier keep-public-API instruction.
- Type: `{σ : Type*} (P : MvPolynomial σ ℤ) (x : ℝ) : Polynomial.eval x (Polynomial.map (Int.castRingHom ℝ) (diag P)) = eval (fun _ ↦ x) (map (Int.castRingHom ℝ) P)`
- What: Evaluating the diagonal polynomial `P(x, …, x)` (pushed to `ℝ[x]`) at a real `x` equals evaluating `P` (pushed to real coefficients) at the diagonal point `(x, …, x)`.
- Hypotheses: none.
- Uses from project: `Roth.diag`
- Used by: unused in project. `grep -rn eval_diag Roth Roth.lean` finds only the declaration at Roth/CoeffNorm.lean:193. Its one former use (`rwa [hasseDeriv_map, ← eval_diag, ...]` in `eval_hasseDeriv_sub_eq_zero`, Roth/MainLemma.lean) was removed in commit `96928fd` ("Generalize Hasse subtraction evaluation to commutative rings"), which replaced it by `simpa [..., diag, MvPolynomial.comp_aeval_apply, Polyn

### #95 theorem Roth.diag_sub (public, Roth/CoeffNorm.lean:199)
- verdict: NO-mathlib-has-it | cost: n/a | junk: REPLACE
- rationale: Re-aimed at diag = MvPolynomial.aeval (fun _ ↦ X) (an AlgHom), the statement is literally mathlib's map_sub (also MvPolynomial.eval₂_sub), which is already its one-term proof; used at a single simp call site that compiles without it.
- action: Optionally delete Roth.diag_sub (Roth/CoeffNorm.lean:197-200) and at its only call site Roth/MainLemma.lean:408 replace `diag_sub` by unfolding `diag` (`simp only [diag] at h ⊢` then `simp [map_sub, Polynomial.sub_modByMonic, h]`, compiled); or keep as a convenience simp lemma while diag is unbundled; no mathlib PR.
- Type: `{σ : Type*} (P Q : MvPolynomial σ ℤ) : diag (P - Q) = diag P - diag Q`
- What: The diagonal substitution `P ↦ P(x, …, x)` commutes with subtraction.
- Hypotheses: none.
- Uses from project: `Roth.diag`
- Used by: Roth/MainLemma.lean:408 (`simp [map_sub, diag_sub, Polynomial.sub_modByMonic, h]` inside `eval_hasseDeriv_sub_eq_zero`). No other uses (`grep -rn diag_sub Roth/`).

### #96 theorem Roth.geom_sum_le_one_add_pow (public, Roth/CoeffNorm.lean:205)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Elementary inequality sum over s in range (r+1) of t^s at most (1+t)^r for t nonneg, absent from mathlib (no hit across five methods), not a 3-call composition, and the identical proof compiles verbatim over any ordered (even non-commutative) semiring, so it should be upstreamed in that generality.
- action: Restate over [Semiring R] [PartialOrder R] [IsOrderedRing R] (compiled in evidence/Roth.geom_sum_le_one_add_pow/weaken.lean) and PR it to Mathlib/Algebra/Order/Ring/GeomSum.lean next to geom_sum_alternating_of_le_neg_one; the single caller Roth.sum_box_prod_pow_le_aux (Roth/CoeffNorm.lean:218) then uses the mathlib lemma unchanged.
- Type: `∀ {t : ℝ}, 0 ≤ t → ∀ (r : ℕ), ∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r`
- What: For real `t ≥ 0` and `r ∈ ℕ`, the truncated geometric sum `1 + t + ⋯ + t^r` is at most `(1 + t)^r`. This is the step in clean.tex §6, proof of Lemma 9 (l.1546, l.1567) that turns a monomial count into `(1 + |α|)^r`.
- Hypotheses: `ht : 0 ≤ t`. This is needed: `t = -1/2`, `r = 2` gives `3/4 ≤ 1/4` (counterexample compiled in the evidence file).
- Uses from project: `[]`
- Used by: `Roth.sum_box_prod_pow_le_aux` (private, Roth/CoeffNorm.lean:218), which feeds `Roth.abs_eval_le`. `grep -rn geom_sum_le_one_add_pow Roth/` finds only l.205 (declaration) and l.218.

### #97 theorem Roth.sum_box_prod_pow_le_aux (private, Roth/CoeffNorm.lean:214)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-use helper giving the last calc step of abs_eval_le, namely sum over box r of B times prod of |x j|^(k j) is at most B times prod of (1+|x j|)^(r j), via Finset.prod_univ_sum plus geom_sum_le_one_add_pow; no mathlib analogue.
- action: Keep as private helper for its single call site Roth/CoeffNorm.lean:239 (abs_eval_le, final calc step); if abs_eval_le is ever upstreamed, carry it along (or inline it there).
- Type: `∀ {σ : Type*} [Fintype σ] (r : σ → ℕ) {B : ℝ}, 0 ≤ B → ∀ (x : σ → ℝ), ∑ k ∈ box r, B * ∏ j, |x j| ^ k j ≤ B * ∏ j, (1 + |x j|) ^ r j` (stated under `open scoped Classical in`, so the `DecidableEq σ` needed by `box` is the classical instance).
- What: Summing `B · ∏_j |x_j|^{k_j}` over all multi-indices `k` with `0 ≤ k_j ≤ r_j` gives at most `B · ∏_j (1 + |x_j|)^{r_j}`: the box sum factors as `B · ∏_j ∑_{s ≤ r_j} |x_j|^s`, and each truncated geometric sum is at most `(1 + |x_j|)^{r_j}`.
- Hypotheses: `[Fintype σ]` (needed for `box` and the finite products); `0 ≤ B` (needed to multiply the inequality by `B`; without it the inequality flips). No redundant hypotheses.
- Uses from project: `Roth.box` (Roth/Box.lean:47), `Roth.geom_sum_le_one_add_pow` (Roth/CoeffNorm.lean:204).
- Used by: Roth/CoeffNorm.lean:239 `Roth.abs_eval_le` (last step of its calc) only; `grep -rn sum_box_prod_pow_le_aux Roth/` returns only the definition (l.214) and that use. Transitively everything downstream of `abs_eval_le`.

### #98 theorem Roth.abs_eval_le (public, Roth/CoeffNorm.lean:223)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The local value bound for a polynomial with sup-coefficient bound B and partial degrees at most r_j, namely the norm of P(x) is at most B times the product of (1 + norm x_j)^(r_j), is absent from mathlib (its nearest sibling AbsoluteValue.eval_mvPolynomial_le needs homogeneity, an l1 coefficient sum and a sup of the x_j) and not a short composition; the project proof compiles verbatim over any NormedCommRing with NormOneClass, recovering the Z-to-R statement.
- action: Ship MvPolynomial.norm_eval_le_mul_prod_one_add_pow over [NormedCommRing R] [NormOneClass R] (compiled in evidence/Roth.abs_eval_le/abs_eval_le_general.lean) next to AbsoluteValue.eval_mvPolynomial_le in Mathlib/NumberTheory/Height/MvPolynomial.lean or an Analysis/Polynomial companion, together with the geom_sum_le_one_add_pow PR and with box replaced by Finset.Iic; keep the Z form for the single caller Roth/MainLemma.lean:466.
- Type: `{σ : Type*} [Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (x : σ → ℝ) : |eval x (map (Int.castRingHom ℝ) P)| ≤ B * ∏ j, (1 + |x j|) ^ r j`
- What: If every coefficient of the integer polynomial `P` is at most `B` in absolute value and `P` has degree at most `r_j` in `x_j`, then `|P(x)| ≤ B ∏_j (1 + |x_j|)^{r_j}` for every real point `x`.
- Hypotheses: `[Fintype σ]`; `hP` (partial degree bounds); `hB` (uniform coefficient bound). Nonnegativity of `B` is derived from `hB 0`.
- Uses from project: `Roth.box`, `Roth.mem_box`, `Roth.sum_box_prod_pow_le_aux` (which uses `Roth.geom_sum_le_one_add_pow`)
- Used by: Roth/MainLemma.lean:466 (`abs_eval_iterated_hasseDeriv_lt_aux`, private, applied to `hasseDeriv i (hasseDeriv k P)` at the diagonal point `fun _ ↦ α`); also listed in the CoeffNorm.lean module docstring (line 32).

### #99 theorem Roth.degreeOf_det_hasseDeriv_le (public, Roth/CoeffNorm.lean:245)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The Leibniz degree bound for a determinant of multivariate polynomials (per-variable degree of det M at most the sum of the column bounds, so card n times k for uniform bounds) is absent from mathlib, whose only det-degree lemma is the special Polynomial.natDegree_det_X_add_C_le; the Hasse-derivative entries are concrete-via-abstract (the proof uses only entry degree bounds), and the general form over any CommRing and Fintype index compiled clean with the project lemma as a one-line corollary.
- action: Upstream MvPolynomial.degreeOf_det_le_sum (column bounds), a row variant and the uniform degreeOf_det_le (card n * k) to Mathlib/LinearAlgebra/Matrix/MvPolynomial.lean or Mathlib/Algebra/MvPolynomial/Degrees.lean (with a Polynomial.natDegree_det_le companion); locally keep the Roth form as the corollary used at Roth/Separation.lean:555 and :558.
- Type: `{σ : Type*} {l : ℕ} (E : Fin l → Fin l → (σ →₀ ℕ)) (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) (j : σ) : degreeOf j (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det ≤ l * r j`
- What: If `P` has degree at most `r_j` in each variable `x_j`, then the `l × l` determinant `det(Δ_{E μ ν} P)` of Hasse derivatives of `P` has degree at most `l r_j` in `x_j`.
- Hypotheses: `hP` (partial degree bounds on `P`).
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.degreeOf_hasseDeriv_le`
- Used by: Roth/Separation.lean:555 and :558 (`exists_det_eq_mul`, degree bounds `l r_j` for `U` and `l r_p` for `V`). No other use in `Roth/`.

### #100 theorem Roth.abs_coeff_det_hasseDeriv_le (public, Roth/CoeffNorm.lean:258)
- verdict: BORDERLINE-needs-human | cost: CHEAP | junk: KEEP
- rationale: Roth's Lemma 3 (paper-specific constant) is a 5-lemma chain through the project l1 norm API (abs_coeff_le_normOne, normOne_det_le, normOne_hasseDeriv_le, normOne_le_card_mul, card_le_card_box), each already slated for upstreaming as MvPolynomial.l1Norm lemmas; not composable from current mathlib (no l1 polynomial norm), but once that API lands it is a short corollary with a Roth-specific constant, so whether it merits its own mathlib lemma is a judgment call; hB0 is superfluous (follows from hB 0, compiled).
- action: Recommended answer is keep local (do not upstream separately); drop hB0 (derive it from hB 0, evidence weaken.lean) and simplify the single caller Roth/Theta.lean:475, optionally expose the stronger normOne_det_hasseDeriv_le form the paper actually proves; ship only the underlying l1Norm lemmas in the MvPolynomial.l1Norm PR.
- Type: `{σ : Type*} [Fintype σ] {l : ℕ} (E : Fin l → Fin l → (σ →₀ ℕ)) (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB0 : 0 ≤ B) (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (d : σ →₀ ℕ) : |(((Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det.coeff d : ℤ) : ℝ)| ≤ (∏ j, ((r j : ℝ) + 1)) ^ l * l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l)`
- What: Roth's Lemma 3: if `P ∈ ℤ[x_σ]` has partial degrees at most `r_j` and coefficients of absolute value at most `B`, every coefficient of the `l × l` determinant `det(Δ_{E μ ν} P)` of Hasse derivatives has absolute value at most `(∏ (r_j+1))^l · l! · B^l · 2^{(∑ r_j) l}`.
- Hypotheses: `hP` (partial degree bounds), `hB0` (`0 ≤ B`, superfluous: follows from `hB 0`), `hB` (sup coefficient bound), `[Fintype σ]` (finite variable set, needed for `∏`/`∑`).
- Uses from project: `Roth.normOne`, `Roth.abs_coeff_le_normOne`, `Roth.normOne_det_le`, `Roth.normOne_hasseDeriv_le`, `Roth.normOne_le_card_mul`, `Roth.card_le_card_box`, `MvPolynomial.hasseDeriv`
- Used by: Roth/Theta.lean:475 (`hFcoef`, Step 1 of the Lemma 6 coefficient bound, passing `hB0` as `(abs_nonneg _).trans (hR.2.2 0)`). No other use.

### #101 def Roth.genWronskian (public, Roth/GenWronskian.lean:32)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The generalized (Ostrowski-Roth) Wronskian det (Delta_{D mu} phi_nu) of multivariate polynomials is a standard named object (Roth 1955 Lemma 1, Schmidt LNM 785, Bostan-Dumas, Ball-Parks-Pong) absent from mathlib, which has only the 2-ary Polynomial.wronskian; [Field K] weakens to [CommRing R] with an rfl-equal body (verified), and it must ship after MvPolynomial.hasseDeriv.
- action: Upstream as MvPolynomial.genWronskian (placeholder name) over [CommRing R] in a new Mathlib/RingTheory/MvPolynomial/Wronskian.lean, after MvPolynomial.hasseDeriv and the n-ary Polynomial Wronskian, with the verified map and univariate bridge lemmas plus genWronskian_eq_zero_of_not_linearIndependent; locally keep (call sites Roth/GenWronskian.lean:42/242/244/256, Roth/Separation.lean:355/357/524/527).
- Type: `{K : Type*} → [Field K] → {σ : Type*} → {l : ℕ} → (D : Fin l → σ →₀ ℕ) → (φ : Fin l → MvPolynomial σ K) → MvPolynomial σ K`
- What: The generalized Wronskian of `l` multivariate polynomials `φ_0, …, φ_{l-1}` with respect to `l` Hasse operators `Δ_{D 0}, …, Δ_{D (l-1)}`: the determinant `det (Δ_{D μ} φ_ν)_{μ, ν}`.
- Hypotheses: `[Field K]` (section variable). The section's `[Fintype σ]` is not included (hover confirms). No order constraint `|D μ| ≤ μ` is imposed; that constraint lives in `exists_genWronskian_ne_zero`.
- Uses from project: `MvPolynomial.hasseDeriv`
- Used by: Roth/GenWronskian.lean: `genWronskian_eq_zero_of_not_linearIndependent` (l.42), `wronskian_kronecker_eq_sum_aux` (private, l.242 statement, l.244 unfolds it), `exists_genWronskian_ne_zero` (l.256); Roth/Separation.lean: `det_hasseDeriv_separated` (l.355 statement, l.357 unfolds it), `exists_rat_factors_det_hasseDeriv_aux` (private, l.524 uses `exists_genWronskian_ne_zero`, l.527 states `hFmap`); a

### #102 theorem Roth.genWronskian_eq_zero_of_not_linearIndependent (public, Roth/GenWronskian.lean:41)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The easy direction of the generalized-Wronskian criterion (dependent multivariate polynomials have all generalized Wronskians zero; Roth 1955, Bostan-Dumas, source paper section 2) is absent from mathlib; [Field K] weakens to [CommRing R] [IsDomain R] with the proof verbatim (verified, IsDomain necessary by a ZMod 4 counterexample), and the proof is an instance of an abstract det-of-linear-maps lemma (verified) that also yields Roth.wronskian_eq_zero_of_not_linearIndependent.
- action: Upstream with MvPolynomial.genWronskian (placeholder) over [CommRing R] [IsDomain R] in a new Mathlib/RingTheory/MvPolynomial/Wronskian.lean, preferably as a one-line corollary of the abstract lemma det_linearMap_eq_zero_of_not_linearIndependent (Mathlib/LinearAlgebra/Matrix/ToLinearEquiv.lean, next to Matrix.exists_mulVec_eq_zero_iff); locally keep (no project call sites; it is the source paper's second lemma of section 2).
- Type: `{K : Type*} [Field K] {σ : Type*} {l : ℕ} (D : Fin l → σ →₀ ℕ) {φ : Fin l → MvPolynomial σ K} (h : ¬ LinearIndependent K φ) : genWronskian D φ = 0`
- What: If multivariate polynomials `φ_0, …, φ_{l-1}` over a field are `K`-linearly dependent, then every generalized Wronskian `det (Δ_{D μ} φ_ν)` vanishes, for any choice of Hasse multi-indices `D` (no order constraint).
- Hypotheses: `[Field K]` (section variable); `[Fintype σ]` is omitted (`omit [Fintype σ] in`); `h : ¬ LinearIndependent K φ`.
- Uses from project: `Roth.genWronskian`, `MvPolynomial.hasseDeriv`
- Used by: unused in project (`grep -rn genWronskian_eq_zero_of_not_linearIndependent Roth/` returns only the declaration).

### #103 def Roth.kronecker (public, Roth/GenWronskian.lean:53)
- verdict: YES-but-generalise-first | cost: MODERATE | junk: KEEP
- rationale: Mathlib has no Kronecker-substitution def (only the term aeval (X ^ w ·) and a private reproof of the base-k injectivity inside RingTheory/NoetherNormalization); the named substitution plus its injectivity/coefficient API is a standard tool, but it should ship as a weighted substitution aeval (fun j ↦ X ^ w j) over [CommSemiring R] with no Fintype, with exponents via Finsupp.weight (all verified rfl/clean), not with the noncanonical Fintype.equivFin.
- action: Upstream (placeholder) MvPolynomial.weightedSubst w := aeval (fun j ↦ Polynomial.X ^ w j) in Mathlib/Algebra/MvPolynomial/ (next to Expand.lean) with monomial lemma via Finsupp.weight, base-k injectivity (deduplicating NoetherNormalization.sum_r_mul_ne), coeff and eq_zero_iff on the degree box; locally replace kroneckerExp by Finsupp.weight and restate kronecker_monomial/coeff_kronecker/kronecker_eq_zero_iff against it (call sites all in Roth/GenWronskian.lean:60-268).
- Type: `{K : Type*} → [Field K] → {σ : Type*} → [Fintype σ] → (k : ℕ) → MvPolynomial σ K →ₐ[K] Polynomial K`
- What: The Kronecker substitution `x_j ↦ t^{k^{e j}}`, where `e = Fintype.equivFin σ` is the (noncanonical) chosen enumeration of the variables, bundled as a `K`-algebra map `K[x_j : j ∈ σ] → K[t]`.
- Hypotheses: `[Field K]`, `[Fintype σ]` (section variables; `Fintype` is needed only for `Fintype.equivFin`).
- Uses from project: `[]`
- Used by: Roth/GenWronskian.lean only: `kronecker_monomial` (l.60–62, unfolds it), `coeff_kronecker` (l.88–93), `kronecker_eq_zero_iff` (l.106–111), `linearIndependent_kronecker` (l.117–123), private `kronHasse` (l.146), private `derivative_kronHasse_aux` (l.159, unfolds it), private `hasseDeriv_kronecker_mem` (l.190–205), `exists_hasseDeriv_kronecker_eq_sum` (l.214–219), private `wronskian_kronecker_eq_sum

### #104 def Roth.kroneckerExp (public, Roth/GenWronskian.lean:57)
- verdict: NO-mathlib-has-it | cost: CHEAP | junk: REPLACE
- rationale: kroneckerExp k is exactly the coercion of mathlib's AddMonoidHom Finsupp.weight (fun j ↦ k ^ equivFin σ j) (verified as a function equality), and after reindexing along equivFin it is mathlib's Behrend.map k, whose Behrend.map_injOn already gives the base-k injectivity the project reproves in kroneckerExp_injOn.
- action: Replace kroneckerExp by Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)) in Roth/GenWronskian.lean (kronecker_monomial l.60-62, kroneckerExp_injOn l.69-82, coeff_kronecker l.88-97); reprove kroneckerExp_injOn from Behrend.map_injOn via the reindexing (verified, 5 lines); do not upstream kroneckerExp itself.
- Type: `{σ : Type*} → [Fintype σ] → (k : ℕ) → (σ →₀ ℕ) → ℕ`
- What: The exponent of the image of the monomial `X^d` under the Kronecker substitution `x_j ↦ t^{k^{e j}}`: `kroneckerExp k d = ∑ j, d j * k ^ (e j)`, with `e = Fintype.equivFin σ`.
- Hypotheses: `[Fintype σ]` (for the `Finset.univ` sum and for `Fintype.equivFin`). The section's `[Field K]` is not a parameter (unused by this def).
- Uses from project: `[]`
- Used by: `Roth.kronecker_monomial` (Roth/GenWronskian.lean:61-62), `Roth.kroneckerExp_injOn` (Roth/GenWronskian.lean:69-74), `Roth.coeff_kronecker` (Roth/GenWronskian.lean:89, 97). Indirectly via `coeff_kronecker`: `Roth.kronecker_eq_zero_iff` (l.111). No use outside Roth/GenWronskian.lean.

### #105 theorem Roth.kronecker_monomial (public, Roth/GenWronskian.lean:60)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The monomial-evaluation lemma is the basic simp/API lemma of the Kronecker (weighted) substitution and has no mathlib counterpart (aeval_monomial leaves a Finsupp.prod of powers); re-aimed at weightedSubst w over CommSemiring with exponent Finsupp.weight w d it compiles verbatim (no Field, no Fintype) and the project lemma is a one-line specialisation.
- action: Ship as MvPolynomial.weightedSubst_monomial (simp) together with the def MvPolynomial.weightedSubst in Mathlib/Algebra/MvPolynomial/ (next to Expand.lean), in the same PR as the Roth.kronecker API; locally restate against Finsupp.weight and keep the single call site coeff_kronecker (Roth/GenWronskian.lean:93) rewriting with it.
- Type: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] (k : ℕ) (d : σ →₀ ℕ) (a : K) : kronecker k (monomial d a) = Polynomial.C a * Polynomial.X ^ kroneckerExp k d`
- What: The Kronecker substitution `x_j ↦ t^{k^{e j}}` sends the monomial `a x^d` to `a t^{∑_j d_j k^{e j}}`.
- Hypotheses: section variables `[Field K]`, `[Fintype σ]`; no hypotheses.
- Uses from project: `Roth.kronecker`, `Roth.kroneckerExp`
- Used by: `Roth.coeff_kronecker` (Roth/GenWronskian.lean:93, `simp_rw [kronecker_monomial, Polynomial.coeff_C_mul_X_pow]`). No other uses in `Roth/`.

### #106 theorem Roth.kroneckerExp_injOn (public, Roth/GenWronskian.lean:69)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: REPLACE
- rationale: Re-aimed at the parent's mathlib counterpart, the lemma is mathlib's Behrend.map_injOn composed (Set.InjOn.comp) with the injective reindexing d ↦ d ∘ equivFin.symm via a 2-line identity kroneckerExp k = Behrend.map k ∘ (· ∘ e.symm); verified in 3 proof lines, and the hypothesis 1 < k turns out to be superfluous.
- action: In Roth/GenWronskian.lean replace the 12-line Nat.ofDigits proof of kroneckerExp_injOn (l.69-82) by the Behrend.map_injOn composition (import Mathlib.Combinatorics.Additive.AP.Three.Behrend), drop hk, and update the single caller coeff_kronecker (l.97); fold into the kroneckerExp → Finsupp.weight refactor; do not upstream.
- Type: `{σ : Type*} [Fintype σ] {k : ℕ} (hk : 1 < k) : Set.InjOn (Roth.kroneckerExp (σ := σ) k) {d | ∀ j, d j < k}`
- What: The Kronecker exponent `d ↦ ∑ j, d j * k ^ (equivFin σ j)` is injective on exponent vectors all of whose entries are `< k` (uniqueness of base-`k` expansions).
- Hypotheses: `hk : 1 < k` (needed by `Nat.ofDigits_inj_of_len_eq`; mathematically superfluous, see below); `[Fintype σ]` (for `equivFin`).
- Uses from project: `Roth.kroneckerExp`
- Used by: `Roth.coeff_kronecker` (Roth/GenWronskian.lean:97). Nothing else in `Roth/`.

### #107 theorem Roth.coeff_kronecker (public, Roth/GenWronskian.lean:88)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The coefficient lemma is the core API fact of the Kronecker substitution and mathlib has no coefficient lemma for aeval (X ^ w ·); restated for weightedSubst w over CommSemiring (any σ, no Field, no Fintype) as an exact coefficient formula plus an InjOn-weight corollary, both verified clean, and the hypothesis 1 < k is superfluous (verified).
- action: Ship MvPolynomial.coeff_weightedSubst (sum over support with weight = n) and coeff_weightedSubst_weight (InjOn weight) with the weightedSubst PR in Mathlib/Algebra/MvPolynomial/ (next to Expand.lean); locally drop hk from coeff_kronecker (l.88) and update its sole caller kronecker_eq_zero_iff (l.111).
- Type: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] {k : ℕ} (hk : 1 < k) {P : MvPolynomial σ K} (hP : ∀ j, degreeOf j P < k) {d : σ →₀ ℕ} (hd : ∀ j, d j < k) : (kronecker k P).coeff (kroneckerExp k d) = P.coeff d`
- What: If every partial degree of `P` is `< k` and every entry of `d` is `< k`, then the coefficient of `t^{∑ d_j k^{e j}}` in the Kronecker substitution of `P` equals the coefficient of `X^d` in `P`.
- Hypotheses: `hk : 1 < k` (only passed on to `kroneckerExp_injOn`; superfluous, verified); `hP` (puts the support in the box `{e | ∀ j, e j < k}`); `hd` (puts `d` in the box); section variables `[Field K]` (not used, a CommSemiring is enough) and `[Fintype σ]` (only for `equivFin`).
- Uses from project: `Roth.kronecker`, `Roth.kroneckerExp`, `Roth.kronecker_monomial`, `Roth.kroneckerExp_injOn`
- Used by: `Roth.kronecker_eq_zero_iff` (Roth/GenWronskian.lean:111). Through that lemma it reaches `Roth.linearIndependent_kronecker` (l.121) and Lemma 1. No uses outside Roth/GenWronskian.lean.

### #108 theorem Roth.kronecker_eq_zero_iff (public, Roth/GenWronskian.lean:106)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Injectivity of the Kronecker substitution on the degree box is the standard folklore fact (PIT reduction) and mathlib has no analogue; it should ship as MvPolynomial.weightedSubst_eq_zero_iff for any weight injective on a set containing the support over a CommSemiring (plus an InjOn-on-restrictSupport form), all verified clean, and hk is superfluous (verified).
- action: Ship MvPolynomial.weightedSubst_eq_zero_iff and injOn_weightedSubst_restrictSupport with the weightedSubst PR in Mathlib/Algebra/MvPolynomial/ (next to Expand.lean); locally drop hk from kronecker_eq_zero_iff (l.106) and update its sole caller linearIndependent_kronecker (l.123).
- Type: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] {k : ℕ} (hk : 1 < k) {P : MvPolynomial σ K} (hP : ∀ j, degreeOf j P < k) : kronecker k P = 0 ↔ P = 0`
- What: A multivariate polynomial whose partial degrees are all `< k` vanishes iff its Kronecker substitution `x_j ↦ t^{k^{e j}}` vanishes, i.e. the substitution is injective on the degree box (kernel form).
- Hypotheses: `hk : 1 < k` (only passed to `coeff_kronecker`; superfluous, verified); `hP` (support in the box; essential, e.g. `x_2 - x_1^k` maps to 0); section variables `[Field K]` (unused, CommSemiring suffices) and `[Fintype σ]` (only for `equivFin` in the weight).
- Uses from project: `Roth.kronecker`, `Roth.coeff_kronecker`
- Used by: `Roth.linearIndependent_kronecker` (Roth/GenWronskian.lean:123). Through it, Lemma 1 (`exists_genWronskian_ne_zero` chain) in the same file. No uses outside Roth/GenWronskian.lean.

### #109 theorem Roth.linearIndependent_kronecker (public, Roth/GenWronskian.lean:117)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: Once the injectivity lemma for weightedSubst on restrictSupport ships (sibling kronecker_eq_zero_iff), this is one call to mathlib's LinearIndependent.map_injOn plus Submodule.span_le (verified over any CommSemiring and index type, without hk); no separate mathlib lemma is warranted.
- action: Do not upstream; ship injOn_weightedSubst_restrictSupport with the weightedSubst PR, then reprove l.117 as h.map_injOn (kronecker k).toLinearMap (injOn.mono (span_le.2 ...)) (drop hk, update the caller at Roth/GenWronskian.lean:263) or inline it there.
- Type: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] {l : ℕ} {k : ℕ} (hk : 1 < k) {φ : Fin l → MvPolynomial σ K} (hφ : ∀ ν j, degreeOf j (φ ν) < k) (h : LinearIndependent K φ) : LinearIndependent K fun ν ↦ kronecker k (φ ν)`
- What: The Kronecker substitution `x_j ↦ t^{k^{e j}}` sends a linearly independent family of multivariate polynomials, all of whose partial degrees are `< k`, to a linearly independent family of univariate polynomials.
- Hypotheses: `hk : 1 < k` (passed to `kronecker_eq_zero_iff`, whose `hk` is superfluous, and used as `0 < k` for `Finset.sup_lt_iff`; superfluous overall, verified); `hφ` (essential: supports in the digit box); `h` (essential); `[Field K]` (only semiring structure needed); `[Fintype σ]` (only for the weight `k ^
- Uses from project: `Roth.kronecker`, `Roth.kronecker_eq_zero_iff`
- Used by: `Roth.exists_genWronskian_ne_zero` (Lemma 1) at Roth/GenWronskian.lean:263. No other uses in `Roth/`.

### #110 theorem Roth.derivative_aeval (public, Roth/GenWronskian.lean:133)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The multivariate algebraic chain rule D(P(f)) = sum_i (d_i P)(f) D(f_i) is absent from mathlib (only the univariate Derivation.map_aeval exists); the project form is the special case D = Polynomial.derivative over a field, and the general derivation form over any commutative semiring compiles with the same three-case induction (evidence verified).
- action: Upstream `Derivation.map_mvPolynomial_aeval` (any D : Derivation R A M, f : σ → A, Fintype σ, CommSemiring R) next to `Derivation.map_aeval` or in Mathlib/Algebra/MvPolynomial/PDeriv.lean, with the `Polynomial.derivative` form as a one-line corollary via `Polynomial.derivative'`; locally weaken `[Field K]` to `[CommSemiring R]` optional, keep the one caller Roth/GenWronskian.lean:159 unchanged.
- Type: `∀ {K : Type*} [Field K] {σ : Type*} [Fintype σ] (γ : σ → Polynomial K) (P : MvPolynomial σ K), Polynomial.derivative (aeval γ P) = ∑ j, Polynomial.derivative (γ j) * aeval γ (pderiv j P)`
- What: The algebraic chain rule: for `γ = (γ_j)` univariate polynomials and `P` multivariate, `d/dt P(γ(t)) = ∑_j γ_j'(t) (∂_j P)(γ(t))`.
- Hypotheses: none beyond section variables `[Field K]`, `[Fintype σ]`.
- Uses from project: `[]`
- Used by: Roth/GenWronskian.lean:159 (`derivative_kronHasse_aux`, private, in a `simp [kronHasse, kronecker, derivative_aeval, pderiv_hasseDeriv, ...]` set). No other use in `Roth/`.

### #111 def Roth.kronHasse (private, Roth/GenWronskian.lean:145)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-line abbreviation P ↦ kronecker k (hasseDeriv d P) naming the generators of the K[X]-span kronSpan used in the proof of Lemma 1; mathlib has neither ingredient (no Kronecker substitution, no multivariate Hasse derivative), so nothing to replace it with.
- action: Keep as private helper for kronSpan (Roth/GenWronskian.lean:151), derivative_kronHasse_aux (l.153-159), hasseDeriv_kronecker_mem (l.196) and exists_hasseDeriv_kronecker_eq_sum (l.221); if Lemma 1 is upstreamed, carry it along with kronSpan, re-based on the generalised weighted substitution recommended for Roth.kronecker.
- Type: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] (k : ℕ) (d : σ →₀ ℕ) : MvPolynomial σ K → Polynomial K`
- What: The operator P ↦ (Δ_d P)(t, t^k, t^(k^2), ...), i.e. the Kronecker substitution of the d-th multivariate Hasse derivative of P, viewed as an element of the K[t]-module of functions MvPolynomial σ K → K[t].
- Hypotheses: `[Field K]`, `[Fintype σ]` from the section variables (`[Fintype σ]` needed by `kronecker`, which uses `Fintype.equivFin σ`; `Field` is more than the definition needs, `CommSemiring` would do for the composition itself, but the section and parent `kronecker` fix it).
- Uses from project: `Roth.kronecker` (Roth/GenWronskian.lean:53), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57).
- Used by: Roth/GenWronskian.lean only (`grep -rn kronHasse Roth/`): `kronSpan` l.151 (generators of the span, as `kronHasse k '' {d | d.degree ≤ μ}`), `derivative_kronHasse_aux` l.154,156 (statement) and l.159 (simp unfold), `derivative_mem_kronSpan` indirectly via `derivative_kronHasse_aux` at l.169, `hasseDeriv_kronecker_mem` l.196 (simp unfold), `exists_hasseDeriv_kronecker_eq_sum` l.221 (simp unfold). T

### #112 def Roth.kronSpan (private, Roth/GenWronskian.lean:149)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private K[X]-submodule spanned by the operators kronHasse k d with deg d at most mu; it is the induction invariant that turns the existential of exists_hasseDeriv_kronecker_eq_sum into closure lemmas (derivative_mem_kronSpan, hasseDeriv_kronecker_mem), and mathlib has no multivariate Hasse derivative or Kronecker substitution to build it from.
- action: Keep as private helper used by derivative_mem_kronSpan (Roth/GenWronskian.lean:162-188) and hasseDeriv_kronecker_mem (l.190-205); if Lemma 1 is upstreamed, carry it along with kronHasse, re-based on the weighted substitution aeval (fun j => X ^ w j) recommended in the Roth.kronecker report.
- Type: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] (k μ : ℕ) : Submodule (Polynomial K) (MvPolynomial σ K → Polynomial K)`
- What: The K[t]-submodule of the (pointwise) K[t]-module of functions MvPolynomial σ K → K[t] spanned by the operators P ↦ (Δ_d P)(t, t^k, t^(k^2), ...) for multi-indices d with total degree |d| ≤ μ. Membership of an operator F says F(P) = Σ_d c_d(t) · kronecker k (Δ_d P) uniformly in P, with all |d| ≤ μ.
- Hypotheses: `[Field K]`, `[Fintype σ]` from the section variables (`[Fintype σ]` inherited from `kronHasse`/`kronecker`, which use `Fintype.equivFin σ`; the span itself only needs `CommSemiring K`, but the section and parents fix `Field`).
- Uses from project: `Roth.kronHasse` (Roth/GenWronskian.lean:145).
- Used by: Roth/GenWronskian.lean only (`grep -rn kronSpan Roth/`): `derivative_mem_kronSpan` l.162–164 (hypothesis and conclusion; `Submodule.span_induction` on membership, `zero_mem` at l.175, `add_mem` at l.183, `span_mono` for the μ ≤ μ+1 monotonicity), `hasseDeriv_kronecker_mem` l.191 (statement), l.198 (`restrictScalars K` + `smul_mem_iff` to cancel the factor μ+1), l.201 (`change`), l.202 (calls `deri

### #113 lemma Roth.derivative_kronHasse_aux (private, Roth/GenWronskian.lean:153)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private chain-rule identity d/dt (kronHasse k d) = sum over j of (X^(k^j))' * (d j + 1) • kronHasse k (d + single j 1), the generator case of derivative_mem_kronSpan; combines the project lemmas derivative_aeval and pderiv_hasseDeriv, neither of which mathlib has.
- action: Keep as private helper of derivative_mem_kronSpan (Roth/GenWronskian.lean:169); if Lemma 1 is upstreamed, carry it with kronHasse/kronSpan, restated for the weighted substitution aeval (fun j ↦ X ^ w j) and derived from the generalised derivative_aeval and pderiv_hasseDeriv.
- Type: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] (k : ℕ) (d : σ →₀ ℕ) : (fun P ↦ Polynomial.derivative (kronHasse k d P)) = ∑ j, (Polynomial.derivative (Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ)) * Polynomial.C ((d j + 1 : ℕ) : K)) • kronHasse k (d + Finsupp.single j 1)`
- What: As an identity in the K[t]-module of functions MvPolynomial σ K → K[t]: differentiating (in t) the operator P ↦ (Δ_d P)(t, t^k, t^(k^2), ...) gives the K[t]-linear combination over j of (t^(k^(e j)))' · (d_j + 1) times the operator for the Hasse multi-index d + e_j. I.e. the derivative of a generator of `kronSpan k μ` lies in `kronSpan k (μ + 1)`, with explicit coefficients.
- Hypotheses: `[Field K]`, `[Fintype σ]` from section variables; `classical` for the Finsupp/sum decidability. No hypothesis on `k` or `d`.
- Uses from project: `Roth.kronHasse` (Roth/GenWronskian.lean:145), `Roth.kronecker` (l.53), `Roth.derivative_aeval` (l.133), `MvPolynomial.pderiv_hasseDeriv` (Roth/HasseDeriv.lean:200); implicitly `MvPolynomial.hasseDeriv` (through `kronHasse`).
- Used by: `grep -rn derivative_kronHasse_aux Roth/`: only `Roth.derivative_mem_kronSpan` (Roth/GenWronskian.lean:169, `rw` in the `mem` case of `Submodule.span_induction`). Transitively feeds `hasseDeriv_kronecker_mem`, `exists_hasseDeriv_kronecker_eq_sum` and Lemma 1 `exists_genWronskian_ne_zero`.

### #114 lemma Roth.derivative_mem_kronSpan (private, Roth/GenWronskian.lean:162)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private span-induction step showing the K[t]-span kronSpan k mu is mapped into kronSpan k (mu+1) by pointwise d/dt; specific to the private kronHasse/kronSpan machinery of Lemma 1, no mathlib analogue.
- action: Keep as private helper of hasseDeriv_kronecker_mem (Roth/GenWronskian.lean:202); if Lemma 1 is upstreamed, carry it with kronHasse/kronSpan/derivative_kronHasse_aux restated for the weighted substitution.
- Type: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] (k μ : ℕ) {F : MvPolynomial σ K → Polynomial K} (hF : F ∈ kronSpan k μ) : (fun P ↦ Polynomial.derivative (F P)) ∈ kronSpan k (μ + 1)`
- What: In the K[t]-module of functions MvPolynomial σ K → K[t], if F lies in the K[t]-span of the operators P ↦ kronecker k (Δ_d P) with |d| ≤ μ, then its pointwise t-derivative P ↦ (F P)' lies in the span of those with |d| ≤ μ + 1. This is the inductive step behind "d^μ/dt^μ h_ν is a K[t]-combination of Δ^{(i)}_μ φ_ν (γ(t)) with order ≤ μ" in §2, proof of Lemma 1.
- Hypotheses: `[Field K]`, `[Fintype σ]` from section variables; `classical` for the Finsupp decidability. No condition on `k`, `μ`.
- Uses from project: `Roth.kronSpan` (Roth/GenWronskian.lean:149), `Roth.kronHasse` (l.145, via the generator image set), `Roth.derivative_kronHasse_aux` (l.153); implicitly `Roth.kronecker` and `MvPolynomial.hasseDeriv` through `kronHasse`.
- Used by: `grep -rn derivative_mem_kronSpan Roth/`: only `Roth.hasseDeriv_kronecker_mem` (Roth/GenWronskian.lean:202, `convert ... using 1` in the `succ` case). Transitively feeds `exists_hasseDeriv_kronecker_eq_sum` and Lemma 1 `exists_genWronskian_ne_zero`.

### #115 lemma Roth.hasseDeriv_kronecker_mem (private, Roth/GenWronskian.lean:190)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private induction on mu showing the operator P mapsto hasseDeriv mu (kronecker k P) lies in the K[t]-span kronSpan k mu; membership form of exists_hasseDeriv_kronecker_eq_sum, specific to the private kronHasse/kronSpan machinery of Lemma 1, no mathlib analogue.
- action: Keep as private helper of exists_hasseDeriv_kronecker_eq_sum (Roth/GenWronskian.lean:219); if Lemma 1 is upstreamed, carry it with kronHasse/kronSpan/derivative_mem_kronSpan restated for the weighted substitution.
- Type: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] [CharZero K] (k μ : ℕ) : (fun P ↦ Polynomial.hasseDeriv μ (kronecker k P)) ∈ kronSpan k μ`
- What: The operator MvPolynomial σ K → K[t], P ↦ D^{(μ)}_t (P(t, t^k, …, t^{k^{p-1}})) (μ-th univariate Hasse derivative of the Kronecker substitution) lies in the K[t]-submodule of functions spanned by the operators P ↦ kronecker k (Δ_d P) with |d| ≤ μ (Δ_d the multivariate Hasse derivative). This is the "for each μ there are f^μ_i(t) and Δ^{(i)}_μ of order ≤ μ" statement of §2, proof of Lemma 1, in submodule-membership form.
- Hypotheses: `[Field K]`, `[Fintype σ]` (section variables), `[CharZero K]` (used to divide by μ+1). No condition on `k`.
- Uses from project: `Roth.kronecker` (Roth/GenWronskian.lean:53), `Roth.kronSpan` (l.149), `Roth.kronHasse` (l.145, in the base case), `Roth.derivative_mem_kronSpan` (l.162); implicitly `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57) through `kronHasse`.
- Used by: `grep -rn hasseDeriv_kronecker_mem Roth/`: only `Roth.exists_hasseDeriv_kronecker_eq_sum` (Roth/GenWronskian.lean:219, unpacked by `Finsupp.mem_span_image_iff_linearCombination`). Transitively feeds Lemma 1 `exists_genWronskian_ne_zero` (l.254).

### #116 theorem Roth.exists_hasseDeriv_kronecker_eq_sum (public, Roth/GenWronskian.lean:214)
- verdict: BORDERLINE-needs-human | cost: MODERATE | junk: KEEP
- rationale: Existential, Kronecker-specific shadow of the characteristic-free multivariate Hasse chain rule (D^(mu)(P(g)) as a K[t]-combination of (Delta_d P)(g) with total degree of d at most mu, for any g in R[t]^sigma over any commutative ring); mathlib has neither the multivariate Hasse derivative nor any algebraic Faa di Bruno, but the right mathlib form is that general chain rule, which needs a new Taylor-expansion proof (not a mechanical weakening), so shipping is a judgment call tied to the MvPolynomial.hasseDeriv PR.
- action: Keep locally (single caller Roth/GenWronskian.lean:260 in exists_genWronskian_ne_zero); if the MvPolynomial.hasseDeriv / MvPolynomial.taylor PR goes ahead, add a general `Polynomial.hasseDeriv_aeval` chain rule (any CommRing R, any g : sigma to R[X], explicit or existential coefficients) to the new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean and derive this lemma from it, dropping [CharZero K] and the private kronHasse/kronSpan machinery.
- Type: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] [CharZero K] (k μ : ℕ) : ∃ (s : Finset (σ →₀ ℕ)) (c : (σ →₀ ℕ) → Polynomial K), (∀ d ∈ s, d.degree ≤ μ) ∧ ∀ P : MvPolynomial σ K, Polynomial.hasseDeriv μ (kronecker k P) = ∑ d ∈ s, c d * kronecker k (hasseDeriv d P)`
- What: The `μ`-th Hasse derivative of the Kronecker substitution `h(t) = P(t^{k^{e j}})` is, uniformly in `P`, a `K[t]`-linear combination of Kronecker substitutions of the multivariate Hasse derivatives `Δ_d P` with `|d| ≤ μ`.
- Hypotheses: `[Field K]`, `[Fintype σ]` (section variables), `[CharZero K]` (needed by `hasseDeriv_kronecker_mem`, which divides by `μ + 1` to pass from `derivative ∘ D^(μ)` to `D^(μ+1)`).
- Uses from project: `Roth.kronecker`, `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean), private `Roth.hasseDeriv_kronecker_mem`, private `Roth.kronHasse` (and transitively `kronSpan`, `derivative_mem_kronSpan`, `derivative_kronHasse_aux`, `derivative_aeval`, `pderiv_hasseDeriv`).
- Used by: `Roth.exists_genWronskian_ne_zero` (Roth/GenWronskian.lean:260, via `choose s c hs hc using fun μ : Fin l ↦ exists_hasseDeriv_kronecker_eq_sum k μ`). No other uses in `Roth/`.

### #117 theorem Roth.det_sum_rows (public, Roth/GenWronskian.lean:228)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: Row-multilinear expansion of det is MultilinearMap.map_sum_finset applied to Matrix.detRowAlternating plus MultilinearMap.map_smul_univ and unfolding Matrix.det (the current 4-line proof); no det-specific mathlib lemma exists but the composition is mechanical and has one caller.
- action: Keep locally next to its single caller wronskian_kronecker_eq_sum_aux (Roth/GenWronskian.lean:245); optionally restate over an arbitrary [Fintype n] [DecidableEq n] index (verified in evidence); do not upstream.
- Type: `{l : ℕ} {A : Type*} [CommRing A] {ι : Type*} (s : Fin l → Finset ι) (c : Fin l → ι → A) (N : Fin l → ι → Fin l → A) : (Matrix.of fun μ ν ↦ ∑ i ∈ s μ, c μ i * N μ i ν).det = ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Matrix.of fun μ ν ↦ N μ (f μ) ν).det`
- What: If row `μ` of a square matrix is the linear combination `∑_{i ∈ s μ} c μ i • N μ i`, the determinant is the sum, over choice functions `f` with `f μ ∈ s μ`, of `∏_μ c μ (f μ)` times the determinant of the matrix with rows `N μ (f μ)`.
- Hypotheses: none (only `[CommRing A]`, needed for `Matrix.det`).
- Uses from project: `[]`
- Used by: Roth/GenWronskian.lean:245 (`wronskian_kronecker_eq_sum_aux`, private). No other uses in `Roth/`.

### #118 lemma Roth.wronskian_kronecker_eq_sum_aux (private, Roth/GenWronskian.lean:238)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-use helper of exists_genWronskian_ne_zero expanding the univariate Wronskian of Kronecker substitutions into a K[t]-combination of Kronecker images of generalized Wronskians, via det_sum_rows and AlgHom.map_det; mathlib has no Kronecker substitution or generalized Wronskian.
- action: Keep as private helper for its single call site Roth/GenWronskian.lean:268 (exists_genWronskian_ne_zero); optional cosmetic inlining there is not recommended; if Lemma 1 is ever upstreamed, carry it along with det_sum_rows.
- Type: `∀ {K : Type*} [Field K] {σ : Type*} [Fintype σ] {l : ℕ} (k : ℕ) (φ : Fin l → MvPolynomial σ K) (s : Fin l → Finset (σ →₀ ℕ)) (c : Fin l → (σ →₀ ℕ) → Polynomial K), (∀ μ ν : Fin l, Polynomial.hasseDeriv ↑μ (kronecker k (φ ν)) = ∑ d ∈ s μ, c μ d * kronecker k (hasseDeriv d (φ ν))) → wronskian (fun ν ↦ kronecker k (φ ν)) = ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * kronecker k (genWronskian f φ)` 
- What: If, for every row index `μ` and every `ν`, the `μ`-th Hasse derivative of the Kronecker substitution `φ_ν(t, t^k, t^{k^2}, …)` is the `K[t]`-combination `∑_{d ∈ s μ} c μ d · kronecker k (Δ_d φ_ν)`, then the (Hasse) Wronskian of the substituted family equals `∑_f (∏_μ c μ (f μ)) · kronecker k (W(φ; Δ_{f 0}, …, Δ_{f (l-1)}))`, the sum running over choice functions `f` with `f μ ∈ s μ`. This is the "multilinearity of the determinant in each row" step of the source's proof of Lemma 1 (§2).
- Hypotheses: `[Field K]`, `[Fintype σ]` (both from the file `variable` line; `Fintype σ` is needed because `kronecker` sends `X_j ↦ t^{k^{equivFin j}}`). `hc` is the essential hypothesis (row expansion); it is exactly what `exists_hasseDeriv_kronecker_eq_sum` produces, specialised at `φ ν`. No `CharZero` needed 
- Uses from project: `Roth.wronskian` (Roth/Wronskian.lean:60), `Roth.wronskianMatrix` (Roth/Wronskian.lean:56), `Roth.kronecker` (Roth/GenWronskian.lean:53), `Roth.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.genWronskian` (Roth/GenWronskian.lean:32), `Roth.det_sum_rows` (Roth/GenWronskian.lean:228). Mathlib: `Polynomial.hasseDeriv`, `Fintype.piFinset`, `AlgHom.map_det`, `Matrix.map`.
- Used by: Roth/GenWronskian.lean:268 `Roth.exists_genWronskian_ne_zero` (Lemma 1) only; `grep -rn wronskian_kronecker_eq_sum_aux Roth/` returns just the definition (l.238) and this use. Transitively everything downstream of Lemma 1.

### #119 theorem Roth.exists_genWronskian_ne_zero (public, Roth/GenWronskian.lean:254)
- verdict: YES-but-generalise-first | cost: MODERATE | junk: KEEP
- rationale: Roth's Lemma 1 (linearly independent multivariate polynomials have a generalized Wronskian with orders at most mu that is nonzero; Ostrowski, Roth 1955, Bostan-Dumas Thm 3) is absent from mathlib, which has only the 2-ary univariate Wronskian; [Finite sigma] drops via rename and [Field K] weakens to [CommRing R] [IsDomain R] [CharZero R] via the fraction field (both verified), CharZero is necessary.
- action: Upstream as MvPolynomial.exists_genWronskian_ne_zero (placeholder) over [CommRing R] [IsDomain R] [CharZero R] with no finiteness on sigma, in the new Mathlib/RingTheory/MvPolynomial/Wronskian.lean as a follow-up PR after MvPolynomial.hasseDeriv, the n-ary Polynomial Wronskian criterion, MvPolynomial.genWronskian and the weightedSubst (Kronecker) PR; locally keep (single caller Roth/Separation.lean:524 in private exists_rat_factors_det_hasseDeriv_aux).
- Type: `{K : Type*} [Field K] {σ : Type*} {l : ℕ} [Finite σ] [CharZero K] {φ : Fin l → MvPolynomial σ K} (h : LinearIndependent K φ) : ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0`
- What: Lemma 1 of the source (Roth's lemma): a linearly independent family of `l` multivariate polynomials over a characteristic-zero field has a generalized Wronskian `det (Δ_{D μ} φ_ν)`, with Hasse operators of total order `|D μ| ≤ μ`, that is not identically zero.
- Hypotheses: `[Field K]`, `[CharZero K]` (needed for the univariate criterion), `[Finite σ]` (needed for the Kronecker substitution `kronecker`, which uses `Fintype.equivFin`), and `h : LinearIndependent K φ`.
- Uses from project: `Roth.genWronskian`, `Roth.exists_hasseDeriv_kronecker_eq_sum`, `Roth.wronskian_ne_zero_of_linearIndependent`, `Roth.linearIndependent_kronecker`, `Roth.wronskian_kronecker_eq_sum_aux` (private), `Roth.kronecker`, `MvPolynomial.hasseDeriv` (via `genWronskian`)
- Used by: Roth/Separation.lean:524 (`exists_rat_factors_det_hasseDeriv_aux`, private, the proof of Lemma 2)

### #120 theorem Roth.sqrt_one_sub_inv_lt (public, Roth/Lattice.lean:29)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: A one-off numeric inequality from the proof of Lemma 8 with no literature standing and no mathlib counterpart; mathlib has the key building block Real.sqrt_one_add_le, but the remaining arithmetic for the lambda side is a real (if short) proof rather than a 3-call composition, so no bucket fits cleanly; recommended resolution is to keep it project-local.
- action: Keep in Roth/Lattice.lean as a project lemma (not for mathlib); optionally reprove via Real.sqrt_one_add_le and weaken 2 ≤ m to 1 ≤ m (both compiled in evidence/Roth.sqrt_one_sub_inv_lt/experiments.lean); single caller Roth.sum_inv_lt (Roth/Lattice.lean:87) needs no change.
- Type: `∀ {m : ℕ}, 2 ≤ m → ∀ {lam : ℝ}, 2 * √(m : ℝ) < lam → √(1 - 1 / (m : ℝ)) < 1 - lam⁻¹ ^ 2`
- What: For an integer `m ≥ 2` and real `λ > 2√m`, `√(1 - 1/m) < 1 - λ⁻²`. This is the chain `1 - λ⁻² > 1 - 1/(4m) > √(1 - 1/m)` in clean.tex §6, proof of Lemma 8 (l.1115–1117).
- Hypotheses: `hm : 2 ≤ m` (only `1 ≤ m` is needed, verified); `hlam : 2 * √m < lam` (essential).
- Uses from project: `[]`
- Used by: `Roth.sum_inv_lt` (Roth/Lattice.lean:87, inside a `gcongr` side goal). `grep -rn sqrt_one_sub_inv_lt Roth/` finds only l.29 and l.87.

### #121 lemma Roth.inv_add_inv_le (private, Roth/Lattice.lean:40)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private pairing inequality 1/(λ-1+x) + 1/(λ+1-x) ≤ 2λ/(λ²-1) for 0 ≤ x ≤ 2, the per-pair step of the j/(r-j) pairing in sum_inv_le; a 4-line field_simp/nlinarith fact with no mathlib counterpart and one call site.
- action: Keep as private helper for its single call site Roth.sum_inv_le (Roth/Lattice.lean:57); optionally weaken 2 < lam to 1 < lam (same proof, compiled in evidence/Roth.inv_add_inv_le/weaken.lean), not required since the caller has 2 < lam.
- Type: `∀ {lam x : ℝ}, 2 < lam → 0 ≤ x → x ≤ 2 → (lam - 1 + x)⁻¹ + (lam - 1 + (2 - x))⁻¹ ≤ 2 * lam / (lam ^ 2 - 1)`
- What: For real λ > 2 and 0 ≤ x ≤ 2, the sum of reciprocals 1/(λ - 1 + x) + 1/(λ + 1 - x) is at most 2λ/(λ² - 1). Writing a = λ - 1 + x and b = λ + 1 - x, one has a + b = 2λ and ab = λ² - (1 - x)² ≥ λ² - 1, so 1/a + 1/b = 2λ/(ab) ≤ 2λ/(λ² - 1); the extreme case is x ∈ {0, 2}. It is the bound on one pair (j, r - j) of terms in the harmonic-type sum of Lemma 8 (clean.tex §6), applied with x = 2j/r.
- Hypotheses: `hlam : 2 < lam` (only `1 < lam` is used, verified in evidence); `hx0 : 0 ≤ x` and `hx2 : x ≤ 2` (both necessary: the statement fails at x = -1 and at x = 3 with λ = 3, verified in evidence).
- Uses from project: `[]`
- Used by: `Roth.sum_inv_le` (private, Roth/Lattice.lean:47; use at l.57 inside the `Finset.sum_le_sum` step, with x = 2j/r and 2 - x rewritten as 2(r - j)/r). `grep -rn inv_add_inv_le Roth/ Roth.lean` finds only l.40 and l.57. Transitively feeds `Roth.sum_inv_lt` (l.68) and Lemma 8.

### #122 lemma Roth.sum_inv_le (private, Roth/Lattice.lean:47)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private pairing bound sum_{j=0}^r (λ-1+2j/r)⁻¹ ≤ (r+1)λ/(λ²-1), the first calc step of Roth.sum_inv_lt (Lemma 8); specialised to Lemma 8's parametrisation, no mathlib counterpart, one call site.
- action: Keep as private helper for its single call site Roth.sum_inv_lt (Roth/Lattice.lean:83); optional polish: use Finset.sum_flip instead of sum_range_reflect to drop the r+1-1-j rewrite, and 2 < lam may be weakened to 1 < lam (compiled in evidence/Roth.sum_inv_le/weaken.lean), not required.
- Type: `∀ {r : ℕ}, 1 ≤ r → ∀ {lam : ℝ}, 2 < lam → ∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ ≤ (r + 1) * (lam / (lam ^ 2 - 1))`
- What: For an integer r ≥ 1 and real λ > 2, the harmonic-type sum ∑_{j=0}^r 1/(λ - 1 + 2j/r) is at most (r + 1)·λ/(λ² - 1). Proof idea (source §6, Lemma 8): pair the term j with the term r - j; each pair is bounded by 2λ/(λ² - 1), so twice the sum is at most 2(r + 1)λ/(λ² - 1).
- Hypotheses: `hr : 1 ≤ r` (necessary: at r = 0, λ = 3 the left side is 1/2 and the right side 3/8, refuted by `norm_num` in evidence); `hlam : 2 < lam` (only `1 < lam` is used, verified in evidence by recompiling with the helper weakened the same way).
- Uses from project: `Roth.inv_add_inv_le` (private, Roth/Lattice.lean:40)
- Used by: `Roth.sum_inv_lt` (Roth/Lattice.lean:68, first `calc` step at l.83). `grep -rn sum_inv_le Roth/` finds only l.47 and l.83. Transitively feeds Lemma 8 (lattice count estimate).

### #123 theorem Roth.sum_inv_lt (public, Roth/Lattice.lean:68)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: The auxiliary numeric inequality from the proof of Lemma 8 (sum over j of (λ-1+2j/r)⁻¹ < λ⁻¹√(m/(m-1))(r+1)); it has no standing in the literature and no counterpart in mathlib, and composing it needs two project lemmas plus field_simp arithmetic, so neither a YES bucket nor a NO bucket fits cleanly; recommended resolution is to keep it in the project.
- action: Keep in Roth/Lattice.lean as a project lemma, not for mathlib; optionally make it private since its only caller is the private Roth.card_filter_weight_le_succ_aux (Roth/Lattice.lean:173); both hypotheses hr and hm are necessary (counterexamples compiled in evidence/Roth.sum_inv_lt/hypotheses.lean).
- Type: `∀ {r m : ℕ}, 1 ≤ r → 2 ≤ m → ∀ {lam : ℝ}, 2 * √(m : ℝ) < lam → ∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ < lam⁻¹ * (√((m : ℝ) - 1))⁻¹ * √(m : ℝ) * (r + 1)`
- What: For integers `r ≥ 1` and `m ≥ 2` and a real `λ > 2√m`, `∑_{j=0}^r (λ - 1 + 2j/r)⁻¹ < λ⁻¹ (m-1)^{-1/2} m^{1/2} (r+1)`. This is the "statement to finish the proof" in clean.tex §6, proof of Lemma 8 (l.1100–1103).
- Hypotheses: `hr : 1 ≤ r` (necessary; for `r = 0` the statement fails, see the compiled counterexample); `hm : 2 ≤ m` (necessary; for `m = 1` the RHS is `0`); `hlam : 2 * √m < lam` (the source's hypothesis, essential).
- Uses from project: `Roth.sum_inv_le` (private, Roth/Lattice.lean:47), `Roth.sqrt_one_sub_inv_lt` (Roth/Lattice.lean:29).
- Used by: `Roth.card_filter_weight_le_succ_aux` (private, Roth/Lattice.lean:173). `grep -rn sum_inv_lt Roth/` gives only l.68 and l.173.

### #124 lemma Roth.extend_apply_castSucc (private, Roth/Lattice.lean:92)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-line simp lemma evaluating the last-coordinate extension d.mapDomain Fin.castSucc + single (Fin.last m) i at j.castSucc; mathlib has Finsupp.cons/tail (front insertion) and Fin.snoc_castSucc for plain functions, but no Finsupp.snoc, so nothing covers this exact Finsupp form.
- action: Keep as private helper for its three uses in card_filter_box_fiber_aux (Roth/Lattice.lean:112, 115, 122) next to extend_apply_last; if a Finsupp.snoc/init API is ever added to Mathlib/Data/Finsupp/Fin.lean, replace the extension by Finsupp.snoc and this lemma by the corresponding snoc_castSucc.
- Type: `∀ {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ) (j : Fin m), (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i) j.castSucc = d j` (declared `private lemma`).
- What: Extending a finitely supported exponent vector `d : Fin m →₀ ℕ` to `Fin (m + 1)` by pushing it forward along `Fin.castSucc` and putting `i` in the last slot does not change the old coordinates: the extended vector evaluated at `j.castSucc` is `d j`. This is the Finsupp analogue of `Fin.snoc_castSucc`.
- Hypotheses: none beyond the data `m, d, i, j`; all are used. The codomain `ℕ` could be any `AddZeroClass`/`AddCommMonoid` (`mapDomain` needs `AddCommMonoid`), but the lemma is private and only used at `ℕ`.
- Uses from project: `[]` (only mathlib: `Finsupp.mapDomain`, `Finsupp.single`, `Fin.castSucc`, `Fin.last`, `Finsupp.mapDomain_apply_of_injective`, `Fin.castSucc_injective`).
- Used by: Roth/Lattice.lean `Roth.card_filter_box_fiber_aux` only (private), at l.112 (bounding coordinates in the box, `Fin.lastCases` castSucc branch), l.115 (injectivity of the extension map in `Finset.card_bij`), l.122 (surjectivity, `hext` ext step). `grep -rn extend_apply_castSucc Roth/` returns only the definition and these three uses. Transitively feeds the public `Roth.card_filter_box_last` (l.130)

### #125 lemma Roth.extend_apply_last (private, Roth/Lattice.lean:96)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-line simp lemma evaluating the last-coordinate extension d.mapDomain Fin.castSucc + single (Fin.last m) i at Fin.last m to i; mathlib has Fin.snoc_last for functions and Finsupp.cons/tail (front insertion) but no Finsupp.snoc, so nothing covers this exact Finsupp form.
- action: Keep as private helper for its three uses in card_filter_box_fiber_aux (Roth/Lattice.lean:110, 111, 122) next to extend_apply_castSucc; if a Finsupp.snoc/init API is ever added to Mathlib/Data/Finsupp/Fin.lean, replace the extension by Finsupp.snoc and this lemma by the corresponding snoc_last.
- Type: `∀ {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ), (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i) (Fin.last m) = i` (declared `private lemma`).
- What: Extending a finitely supported exponent vector `d : Fin m →₀ ℕ` to `Fin (m + 1)` by pushing it forward along `Fin.castSucc` and putting `i` in the last slot gives a vector whose last coordinate is `i`. This is the Finsupp analogue of `Fin.snoc_last`.
- Hypotheses: none beyond the data `m, d, i`; all are used. The codomain `ℕ` could be any `AddCommMonoid` (needed by `mapDomain`), but the lemma is private and only used at `ℕ`.
- Uses from project: `[]` (only mathlib: `Finsupp.mapDomain`, `Finsupp.single`, `Fin.castSucc`, `Fin.last`, `Finsupp.mapDomain_of_notMem_range`).
- Used by: Roth/Lattice.lean `Roth.card_filter_box_fiber_aux` only (private), at l.110 (the extended vector lies in the fibre `d (Fin.last m) = i`, used as a term), l.111 (bounding the last coordinate in the box, `Fin.lastCases` last branch, as simp lemma), l.122 (surjectivity, `hext` ext step, as simp lemma). `grep -rn extend_apply_last Roth/` returns only the definition and these three uses. Transitively f

### #126 lemma Roth.card_filter_box_fiber_aux (private, Roth/Lattice.lean:100)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private fibre-counting bijection (box in the first m coordinates filtered by the extended predicate vs. the fibre of box r filtered by p over last coordinate i); the single substantive step of card_filter_box_last, with no Finsupp-level counterpart in mathlib (mathlib's card_snocEquiv_filter_piFinset only handles predicates depending on init).
- action: Keep as private helper for its sole use in card_filter_box_last (Roth/Lattice.lean:141); revisit only if a Finsupp.snoc API is added to Mathlib/Data/Finsupp/Fin.lean, in which case the bijection could be rebuilt via Finset.filter_piFinset_eq_map_snocEquiv-style maps.
- Type: `∀ {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop) [DecidablePred p] {i : ℕ}, i ≤ r (Fin.last m) → ((box (r ∘ Fin.castSucc)).filter fun d ↦ p (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i)).card = (((box r).filter p).filter fun d ↦ d (Fin.last m) = i).card` (declared `private lemma`).
- What: For a box `box r ⊆ Fin (m+1) →₀ ℕ` and any decidable predicate `p`, the fibre of `{d ∈ box r | p d}` over last coordinate `i` (with `i ≤ r_last`) has the same cardinality as the set of `d` in the lower-dimensional box `box (r ∘ castSucc)` whose extension by `i` in the last slot satisfies `p`. Mathematically: the map `d ↦ (d, i)` is a bijection between those two sets.
- Hypotheses: `hi : i ≤ r (Fin.last m)` is genuinely needed (otherwise the right side is empty while the left side need not be, e.g. `p := True`). `[DecidablePred p]` is needed for `Finset.filter`. All used.
- Uses from project: `Roth.box`, `Roth.mem_box` (Roth/Box.lean:47, 51), `Roth.extend_apply_castSucc` (Roth/Lattice.lean:92), `Roth.extend_apply_last` (Roth/Lattice.lean:96).
- Used by: Roth/Lattice.lean `Roth.card_filter_box_last` only (l.141, in the `Finset.sum_congr` step after `Finset.card_eq_sum_card_fiberwise`). `grep -rn card_filter_box_fiber_aux Roth/` returns only the definition and this use. Transitively feeds `card_filter_weight_le_succ_aux` (l.175) and the lattice-point counting of Roth/Lattice.lean.

### #127 theorem Roth.card_filter_box_last (public, Roth/Lattice.lean:131)
- verdict: BORDERLINE-needs-human | cost: MODERATE | junk: KEEP
- rationale: Fibrewise (Fubini/double-counting) count of a filtered box over the last coordinate; the Roth form is tied to the project-local box (itself slated for REPLACE by Finset.Iic) and a hand-rolled Finsupp snoc, while the clean general form over Fintype.piFinset with Fin.snoc is absent from mathlib (only init-predicate versions exist) and compiles in 20 lines, so upstreaming is a judgment call.
- action: Keep in Roth/Lattice.lean (sole caller Roth.card_filter_weight_le_succ_aux, l.175); if the user wants an upstream PR, propose the piFinset form compiled in evidence/Roth.card_filter_box_last/general_piFinset.lean to Mathlib/Data/Fin/Tuple/Finset.lean next to Finset.card_snocEquiv_filter_piFinset.
- Type: `∀ {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop) [DecidablePred p], ((box r).filter p).card = ∑ i ∈ range (r (Fin.last m) + 1), ((box (r ∘ Fin.castSucc)).filter fun d ↦ p (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i)).card`
- What: For a box `∏_{j ≤ m} [0, r_j]` of multi-indices and any decidable predicate `p`, the number of points of the box satisfying `p` equals the sum over `i ∈ [0, r_last]` of the number of points `d` of the lower-dimensional box `∏_{j < m} [0, r_j]` whose extension `(d, i)` satisfies `p`. This is the discrete Fubini / double-counting identity for the last-coordinate projection.
- Hypotheses: `[DecidablePred p]` (needed for `Finset.filter`); no other hypotheses.
- Uses from project: `Roth.box`, `Roth.mem_box` (Roth/Box.lean:47, 51), `Roth.card_filter_box_fiber_aux` (Roth/Lattice.lean:100).
- Used by: Roth/Lattice.lean:175 (`rw [card_filter_box_last, ...]` in private `Roth.card_filter_weight_le_succ_aux`, the induction step of Lemma 8). `grep -rn card_filter_box_last Roth/` gives only l.131 and l.175.

### #128 lemma Roth.filter_weight_le_eq_empty (private, Roth/Lattice.lean:143)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private 3-line helper saying the filter of box r by weight r d ≤ (m - lam)/2 is empty when m < lam (negative threshold vs. weight_nonneg); used twice in the base cases of card_filter_weight_le, project-specific (weight is a Roth def), nothing to upstream.
- action: Keep as private helper for its two uses in Roth.card_filter_weight_le (Roth/Lattice.lean:208 and 214); optional polish only (state for any Finset s and any negative threshold), no upstream target.
- Type: `∀ {m : ℕ} (r : Fin m → ℕ) {lam : ℝ}, (m : ℝ) < lam → (box r).filter (fun d ↦ weight r d ≤ ((m : ℝ) - lam) / 2) = ∅` (declared `private lemma`).
- What: If `λ > m`, then no multi-index in the box `∏ [0, r_j]` has weight at most `(m - λ)/2`, because that threshold is negative while every weight `∑ d_j / r_j` is nonnegative. This is the trivial (empty) case of the Lemma 8 lattice count.
- Hypotheses: `hlam : (m : ℝ) < lam` is used (it makes the threshold negative); it is strict, and needed: at `lam = m` the zero multi-index has weight `0 ≤ 0` and lies in the filter. Membership in `box r` (the `_` binder) is not used, so the statement holds for any `Finset (Fin m →₀ ℕ)`; `Fin m` could be any `Fin
- Uses from project: `Roth.box` (Roth/Box.lean:47), `Roth.weight` (Roth/Box.lean:71), `Roth.weight_nonneg` (Roth/Box.lean:75).
- Used by: Roth/Lattice.lean `Roth.card_filter_weight_le` only, twice: l.208 (`zero` case of the induction on `m`, `m = 0`, from `0 < lam`) and l.214 (`succ` case with `n = 0` and `lam > 2 √1 = 2 > 1`). `grep -rn filter_weight_le_eq_empty Roth/` returns only the definition (l.143) and these two uses.

### #129 lemma Roth.card_filter_fiber_eq (private, Roth/Lattice.lean:147)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private 6-line helper rewriting the last-coordinate fibre count of the Lemma 8 weight filter as a weight filter in the first n coordinates with shifted parameter lam - 1 + 2i/r_last; single use in card_filter_weight_le_succ_aux, entirely about the project def weight, nothing to upstream.
- action: Keep as private helper for its single use in Roth.card_filter_weight_le_succ_aux (Roth/Lattice.lean:176); optional polish only (state for an arbitrary finset, since box membership is unused), no upstream target.
- Type: `∀ {n : ℕ} (r : Fin (n + 1) → ℕ) (lam : ℝ) (i : ℕ), (((box (r ∘ Fin.castSucc)).filter fun d ↦ weight r (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last n) i) ≤ (((n + 1 : ℕ) : ℝ) - lam) / 2).card : ℝ) = (((box (r ∘ Fin.castSucc)).filter fun d ↦ weight (r ∘ Fin.castSucc) d ≤ ((n : ℝ) - (lam - 1 + 2 * (i : ℝ) / r (Fin.last n))) / 2).card : ℝ)` (declared `private lemma`).
- What: In the inductive step of Lemma 8, the fibre of the filtered box over last coordinate `i` (a multi-index `d` in the first `n` coordinates, extended by `i` in the last) satisfies `weight_r(d, i) ≤ (n + 1 - λ)/2` iff `weight_{r∘castSucc}(d) ≤ (n - λ')/2` with `λ' = λ - 1 + 2i/r_{n+1}`; hence the two filtered cards (cast to ℝ) agree. This is the "reduce λ to λ' in one dimension lower" step of the paper's induction.
- Hypotheses: none beyond the data `r`, `lam`, `i`. No positivity of `r (Fin.last n)` is needed (if it is `0`, both `i / 0` and `2 * i / 0` are `0` in Lean, and the identity still holds). The box-membership binder in `filter_congr` (`fun d _`) is unused, so the statement holds for any `Finset (Fin n →₀ ℕ)` in pla
- Uses from project: `Roth.box` (Roth/Box.lean:47), `Roth.weight` (Roth/Box.lean:71), `Roth.weight_add` (Roth/Box.lean:85), `Roth.weight_mapDomain` (Roth/Box.lean:127), `Roth.weight_single` (Roth/Box.lean:96).
- Used by: Roth/Lattice.lean `Roth.card_filter_weight_le_succ_aux` only (l.176, inside `Finset.sum_congr rfl fun i _ ↦ card_filter_fiber_eq r lam i` to rewrite each summand after `card_filter_box_last`). `grep -rn card_filter_fiber_eq Roth/` returns only the definition (l.147) and this use.

### #130 lemma Roth.card_filter_weight_le_of_le_sqrt_aux (private, Roth/Lattice.lean:158)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private trivial-range case of Lemma 8 (lam at most 2 sqrt m) where the bound exceeds the full box size; a 3-step calc from Finset.card_filter_le, card_box and le_mul_of_one_le_left, used once in card_filter_weight_le.
- action: Keep as private helper for its sole use in Roth.card_filter_weight_le (Roth/Lattice.lean:212); optionally inline it there, nothing to upstream.
- Type: `∀ (m : ℕ) (r : Fin m → ℕ) {lam : ℝ}, 0 < lam → lam ≤ 2 * √(m : ℝ) → (((box r).filter fun d ↦ weight r d ≤ ((m : ℝ) - lam) / 2).card : ℝ) ≤ 2 * √(m : ℝ) / lam * ∏ j, ((r j : ℝ) + 1)` (declared `private lemma`).
- What: The easy case of Lemma 8 (lattice count estimate): when `0 < λ ≤ 2√m`, the claimed bound `2√m λ⁻¹ ∏ (r_j + 1)` is at least the total number `∏ (r_j + 1)` of points of the box, so the filtered count is trivially below it.
- Hypotheses: `hlam : 0 < lam` (used in `one_le_div`) and `h : lam ≤ 2 * √m` (the case condition) are both needed for `1 ≤ 2√m/λ`. The filter predicate (weight bound) is never used: the statement holds for any decidable predicate, the weight only appears to match the shape of `card_filter_weight_le`.
- Uses from project: `Roth.box` (Roth/Box.lean:47), `Roth.weight` (Roth/Box.lean:71, statement only), `Roth.card_box` (Roth/Box.lean:57).
- Used by: Roth/Lattice.lean `Roth.card_filter_weight_le` only (l.212, the `lam ≤ 2 * √(n+1)` branch of the `succ` case). `grep -rn card_filter_weight_le_of_le_sqrt Roth/` returns only the definition (l.158) and this use.

### #131 lemma Roth.card_filter_weight_le_succ_aux (private, Roth/Lattice.lean:166)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private inductive step (m = n+1 with n at least 1 and lam above 2 sqrt(n+1)) of Lemma 8 card_filter_weight_le; combines card_filter_box_last, card_filter_fiber_eq, the induction hypothesis and sum_inv_lt in a 4-step calc, so it is project-specific Roth combinatorics with no mathlib counterpart.
- action: Keep as private helper for its sole use in card_filter_weight_le (Roth/Lattice.lean:218); no upstream action (the public Lemma 8 statement is assessed separately).
- Type: `∀ {n : ℕ} (r : Fin (n + 1) → ℕ), 0 < r (Fin.last n) → 0 < n → ∀ {lam : ℝ}, 2 * √((n + 1 : ℕ) : ℝ) < lam → (∀ {t : ℝ}, 0 < t → (((box (r ∘ Fin.castSucc)).filter fun d ↦ weight (r ∘ Fin.castSucc) d ≤ ((n : ℝ) - t) / 2).card : ℝ) ≤ 2 * √(n : ℝ) / t * ∏ j, (((r ∘ Fin.castSucc) j : ℝ) + 1)) → (((box r).filter fun d ↦ weight r d ≤ (((n + 1 : ℕ) : ℝ) - lam) / 2).card : ℝ) ≤ 2 * √((n + 1 : ℕ) : ℝ) / lam 
- What: The inductive step of Lemma 8 (lattice count estimate) in the nontrivial regime: assuming the Lemma 8 bound in dimension `n` for the truncated box `r ∘ castSucc` and all `t > 0`, it holds in dimension `n + 1` for every `lam > 2 √(n+1)`, provided `n ≥ 1` and the last side `r_last ≥ 1`. Mathematically: split the count by the value `i ∈ [0, r_last]` of the last coordinate; the fibre over `i` is the `n`-dimensional count with `lam` replaced by `lam - 1 + 2i/r_last`; apply the hypothesis to each fibr
- Hypotheses: `hr` (feeds `sum_inv_lt`'s `1 ≤ r` and the division by `R`), `hn` (feeds `sum_inv_lt`'s `2 ≤ m`; also needed since `√n` is inverted), `hlam` (feeds `sum_inv_lt` and positivity of the shifted parameters), `ih` (the per-fibre bound). All used; none removable.
- Uses from project: `Roth.box` (Roth/Box.lean), `Roth.weight` (Roth/Box.lean:71), `Roth.sum_inv_lt` (Roth/Lattice.lean:68), `Roth.card_filter_box_last` (Roth/Lattice.lean:131), `Roth.card_filter_fiber_eq` (Roth/Lattice.lean:148).
- Used by: Roth/Lattice.lean `Roth.card_filter_weight_le` only (l.218, the `succ n` case with `lam > 2 √(n+1)` and `n > 0`). `grep -rn card_filter_weight_le_succ_aux Roth/` returns only the definition (l.166) and this use.

### #132 theorem Roth.card_filter_weight_le (public, Roth/Lattice.lean:202)
- verdict: BORDERLINE-needs-human | cost: MODERATE | junk: KEEP
- rationale: Roth's Lemma 8 (lattice count estimate) - a classical but purely internal step of Roth's theorem with no standing outside proofs of Roth-type theorems; mathlib has neither it nor Roth's Diophantine theorem, it is not composable, all hypotheses are needed (hr counterexample compiled), and its statement is phrased via the project-local box and weight that are slated for REPLACE, so upstreaming only makes sense as part of a Roth-theorem contribution.
- action: Keep in Roth/Lattice.lean (sole external caller Roth.mul_card_filter_weight_le_aux, Roth/MainLemma.lean:574); if Roth's theorem is ever upstreamed, restate it over Finset.Iic and Finsupp.weight (after the box/weight REPLACE refactor) and ship it with card_filter_box_last and sum_inv_lt in a Roth-specific file under Mathlib/NumberTheory/Diophantine/.
- Type: `∀ (m : ℕ) (r : Fin m → ℕ), (∀ j, 0 < r j) → ∀ {lam : ℝ}, 0 < lam → (((box r).filter fun d ↦ weight r d ≤ ((m : ℝ) - lam) / 2).card : ℝ) ≤ 2 * √(m : ℝ) / lam * ∏ j, ((r j : ℝ) + 1)`
- What: Lemma 8 of the source (clean.tex §6, `roth:lem8`): for positive integers `r_1, …, r_m` and `λ > 0`, the number of multi-indices `0 ≤ j_i ≤ r_i` with `∑ j_i / r_i ≤ (m - λ)/2` is at most `2 √m λ⁻¹ ∏ (r_i + 1)`.
- Hypotheses: `hr : ∀ j, 0 < r j` (necessary - compiled counterexample with `r = 0`); `hlam : 0 < lam` (necessary - at `λ = 0` the Lean RHS is `0` while the count of the zero index is positive). `m = 0` is allowed (the source requires `m ≥ 1`), so the Lean form is marginally more general than the source.
- Uses from project: `Roth.box`, `Roth.weight`, `Roth.filter_weight_le_eq_empty` (private), `Roth.card_filter_weight_le_of_le_sqrt_aux` (private), `Roth.card_filter_weight_le_succ_aux` (private; which in turn uses `Roth.card_filter_box_last`, `Roth.card_filter_fiber_eq`, `Roth.sum_inv_lt`).
- Used by: `Roth.mul_card_filter_weight_le_aux` (private, Roth/MainLemma.lean:574). `grep -rn card_filter_weight_le Roth/` shows no other caller of this exact name (other hits are the `_aux` helpers in Roth/Lattice.lean).

### #133 def Roth.index (public, Roth/Index.lean:58)
- verdict: BORDERLINE-needs-human | cost: EXPENSIVE | junk: KEEP
- rationale: The Roth index (min of sum d_j/r_j over the support of P(X+α)) is a real-weighted order of vanishing at a point; mathlib has only MvPowerSeries.weightedOrder (ℕ weights, ℕ∞ values, no MvPolynomial or at-a-point version), to which index equals weightedOrder(taylor α P)/∏r only for positive r (hP superfluous, compiled), so the real-valued Roth form is project-specific while a general "weighted order at a point" is a judgment-call upstream candidate.
- action: Keep Roth.index as is locally; optionally drop the superfluous hP from index_eq_weightedOrder_div (Index.lean:143) and reprove index_prod/index_neg via MvPowerSeries.weightedOrder_prod/weightedOrder_neg; any upstreaming should target a new MvPolynomial weighted order (via coeToMvPowerSeries) plus taylor in Mathlib/RingTheory/MvPolynomial, not the ℝ-valued index.
- Type: `{σ : Type*} [Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : ℝ`
- What: The index of `P` at `α` relative to the parameters `r`: the infimum (a minimum for `P ≠ 0`) of the weights `∑ j, d j / r j` over the multi-indices `d` in the support of the Taylor translate `P(X + α)`, i.e. over `d` with `(Δ_d P)(α) ≠ 0`; junk value `0` for `P = 0` (`sInf ∅ = 0`).
- Hypotheses: section variable `[Fintype σ]` (needed by `Roth.weight`). No positivity on `r`.
- Uses from project: `Roth.weight` (Roth/Box.lean:71), `MvPolynomial.taylor` (Roth/Taylor.lean:42).
- Used by: Roth/Index.lean (every lemma: `mem_support_taylor_iff` 62, `index_le_weight` 69, `exists_weight_eq_index` 76, `le_index_iff` 85, `index_nonneg` 93, `index_eq_zero_iff` 98, `index_sub_weight_le_index_hasseDeriv` 109, `le_index_sum` 118, `index_eq_weightedOrder_div` 143, `index_mul` 162, `index_prod` 175, `index_neg` 190, `index_C_mul` 195, `index_mul_left_weights` 200, `index_rename` 212, `index_le

### #134 lemma Roth.mem_support_taylor_iff (private, Roth/Index.lean:62)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-line bridge d ∈ (taylor α P).support ↔ eval α (hasseDeriv d P) ≠ 0 (MvPolynomial.mem_support_iff then coeff_taylor), used at four call sites in Roth/Index.lean to translate between the support-based definition of index and the derivative-based statements.
- action: Keep as private helper in Roth/Index.lean (uses at l.72, 81, 90, 228); optional low-priority generalisation from ℝ to any CommSemiring R if it is ever made public next to coeff_taylor in Roth/Taylor.lean.
- Type: `∀ {σ : Type*} {P : MvPolynomial σ ℝ} {α : σ → ℝ} {d : σ →₀ ℕ}, d ∈ (taylor α P).support ↔ eval α (hasseDeriv d P) ≠ 0`
- What: A multi-index d lies in the support of the Taylor shift P(X + α) iff the d-th Hasse derivative of P does not vanish at α; i.e. the support of the shifted polynomial is exactly the set of tuples entering the minimum that defines the index.
- Hypotheses: none beyond the implicit data; `omit [Fintype σ] in` drops the section's `Fintype σ`. Stated over ℝ only because the surrounding file is; the proof works verbatim over any `CommSemiring R` (both rewritten lemmas are stated at that generality).
- Uses from project: `MvPolynomial.taylor` (Roth/Taylor.lean:42), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean), `MvPolynomial.coeff_taylor` (Roth/Taylor.lean:134)
- Used by: Roth/Index.lean only (`grep -rn mem_support_taylor_iff Roth/`): `index_le_weight` (l.72, `.2`), `exists_weight_eq_index` (l.81, `.1`), `le_index_iff` (l.90, `.1`), `index_le_card` (l.228, `.2`). Transitively everything built on these index API lemmas.

### #135 theorem Roth.index_le_weight (public, Roth/Index.lean:69)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: The defining upper bound of the sInf-defined index (index at most the weight of any d with Hasse derivative nonvanishing at α) is csInf_le of a finite image plus the project coeff_taylor (compiled); its mathlib-canonical counterpart is MvPowerSeries.weightedOrder_le (one call, compiled), so nothing new for mathlib.
- action: Keep locally as the basic API lemma of Roth.index (used at Roth/Index.lean:87, 105, 114, 153, 245 and Roth/Main.lean:401); do not upstream; if index is ever rebased on weightedOrder of taylor (parent question 3), reprove via MvPowerSeries.weightedOrder_le.
- Type: `{P : MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ} {d : σ →₀ ℕ} (h : eval α (hasseDeriv d P) ≠ 0) : index P α r ≤ weight r d` (with `[Fintype σ]`)
- What: The index of `P` at `α` with weights `r` is at most the weight `∑ d_j / r_j` of any multi-index `d` whose Hasse derivative `Δ_d P` does not vanish at `α`.
- Hypotheses: `h`: the `d`-th Hasse derivative of `P` is nonzero at `α`, i.e. `d` lies in the support of `P(X + α)`.
- Uses from project: `Roth.index`, `Roth.weight`, `MvPolynomial.taylor`, `MvPolynomial.hasseDeriv`, `Roth.mem_support_taylor_iff` (private; via `MvPolynomial.coeff_taylor`)
- Used by: Roth/Index.lean:87 (`le_index_iff`), :105 (`index_eq_zero_iff`), :114 (`index_sub_weight_le_index_hasseDeriv`), :153 (`index_eq_weightedOrder_div`), :245 (`index_unique`); Roth/Main.lean:401

### #136 theorem Roth.exists_weight_eq_index (public, Roth/Index.lean:76)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: Attainment of the sInf-defined index of a nonzero polynomial is Set.Nonempty.csInf_mem on a finite nonempty image plus the project coeff_taylor (compiled); its mathlib-canonical counterpart is MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder (one call, compiled), so nothing new for mathlib; hP is necessary (compiled).
- action: Keep locally as the attainment API lemma of Roth.index (used at Roth/Index.lean:101, 112, 226 and Roth/MainLemma.lean:457); do not upstream; if index is ever rebased on weightedOrder of taylor (parent question 3), reprove via MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder.
- Type: `{P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) : ∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r` (with `[Fintype σ]`)
- What: For a nonzero polynomial the index is an attained minimum: some multi-index `d` with `(Δ_d P)(α) ≠ 0` has weight `∑ d_j / r_j` exactly equal to `index P α r`.
- Hypotheses: `hP : P ≠ 0` (makes the support of the Taylor expansion nonempty; necessary, see evidence (3)).
- Uses from project: `Roth.index`, `Roth.weight`, `MvPolynomial.taylor`, `MvPolynomial.hasseDeriv`, `Roth.mem_support_taylor_iff` (private), and the simp lemma(s) giving `taylor α P = 0 ↔ P = 0` used by `simpa using hP`
- Used by: Roth/Index.lean:101 (`index_eq_zero_iff`), :112 (`index_sub_weight_le_index_hasseDeriv`), :226 (`index_le_card`); Roth/MainLemma.lean:457 (`exists_hasseDeriv_eval_ne_zero`)

### #137 theorem Roth.le_index_iff (public, Roth/Index.lean:85)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: The greatest-lower-bound characterisation of the sInf-defined index (c at most index iff c at most every weight of a d with nonvanishing Hasse derivative) is le_csInf_iff on a finite nonempty image plus Set.forall_mem_image and the project coeff_taylor (compiled); its canonical counterpart is the pair MvPowerSeries.le_weightedOrder and weightedOrder_le (compiled), so nothing new for mathlib; hP is necessary (compiled).
- action: Keep locally as the lower-bound API lemma of Roth.index (used at Roth/Index.lean:121, 125, 154, 248 and Roth/MainLemma.lean:423); do not upstream; if index is ever rebased on weightedOrder of taylor (parent question 3), reprove via MvPowerSeries.le_weightedOrder and weightedOrder_le.
- Type: `{P : MvPolynomial σ ℝ} (hP : P ≠ 0) {α : σ → ℝ} {r : σ → ℕ} {c : ℝ} : c ≤ index P α r ↔ ∀ d, eval α (hasseDeriv d P) ≠ 0 → c ≤ weight r d` (with `[Fintype σ]`)
- What: For a nonzero polynomial, a real `c` is at most the index of `P` at `α` with weights `r` iff every multi-index `d` with `(Δ_d P)(α) ≠ 0` has weight `∑ d_j / r_j ≥ c`.
- Hypotheses: `hP : P ≠ 0` (nonempty support of `P(X+α)`; necessary, evidence (3)).
- Uses from project: `Roth.index`, `Roth.weight`, `Roth.index_le_weight`, `Roth.mem_support_taylor_iff` (private), `MvPolynomial.taylor`, `MvPolynomial.hasseDeriv`, and the simp lemma(s) giving `taylor α P = 0 ↔ P = 0` used by `simpa using hP`
- Used by: Roth/Index.lean:121 and :125 (`le_index_sum`), :154 (`index_eq_weightedOrder_div`), :248 (`index_unique`); Roth/MainLemma.lean:423 (`le_index_of_forall_eval_eq_zero`)

### #138 theorem Roth.index_nonneg (public, Roth/Index.lean:93)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: Nonnegativity of the sInf-defined index is one call to Real.sInf_nonneg with the project weight_nonneg (compiled); its canonical counterpart for mathlib's ℕ∞-valued MvPowerSeries.weightedOrder is just zero_le, so nothing new for mathlib.
- action: Keep locally as basic API of Roth.index (used at Roth/Index.lean:100 and Roth/Theta.lean:110, 395); do not upstream; if index is rebased on weightedOrder of taylor (Roth.index question 3), it becomes a positivity/div_nonneg one-liner.
- Type: `(P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : 0 ≤ index P α r` (with `[Fintype σ]`)
- What: The index of any real multivariate polynomial at any point, for any weights, is nonnegative.
- Hypotheses: none.
- Uses from project: `Roth.index`, `Roth.weight_nonneg` (Roth/Box.lean:75), implicitly `Roth.weight`, `MvPolynomial.taylor`
- Used by: Roth/Index.lean:100 (`index_eq_zero_iff`); Roth/Theta.lean:110 (`Θ_nonneg`), Roth/Theta.lean:395

### #139 theorem Roth.index_eq_zero_iff (public, Roth/Index.lean:98)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: The index vanishes iff P(alpha) is nonzero is the attained-minimum property plus weight_eq_zero_iff (weight zero forces d = 0 for positive r) plus coeff_taylor at d = 0 (compiled without sibling lemmas); the canonical analogue is the unweighted MvPowerSeries.order_ne_zero_iff_constCoeff_eq_zero and the weighted form composes from le_weightedOrder and weightedOrder_le (compiled); hP and hr both necessary (compiled).
- action: Keep locally as the source lemma of section 4 (used at Roth/Index.lean:182 in index_prod); do not upstream; optional tiny generic mathlib follow-up MvPowerSeries.weightedOrder_eq_zero_iff for positive weights (Mathlib/RingTheory/MvPowerSeries/Order.lean, next to order_ne_zero_iff_constCoeff_eq_zero).
- Type: `{P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hr : ∀ j, 0 < r j) (α : σ → ℝ) : index P α r = 0 ↔ eval α P ≠ 0` (with `[Fintype σ]`)
- What: For a nonzero real polynomial and positive weights, the index of `P` at `α` is zero iff `P(α) ≠ 0`.
- Hypotheses: `hP : P ≠ 0` (otherwise the junk value `index 0 = 0` breaks (→); necessary, evidence (3a)); `hr : ∀ j, 0 < r j` (otherwise `d_j / 0 = 0` gives weight-zero nonzero multi-indices; necessary, evidence (3b)).
- Uses from project: `Roth.index`, `Roth.exists_weight_eq_index`, `Roth.index_nonneg`, `Roth.index_le_weight`, `Roth.weight_eq_zero_iff` (Roth/Box.lean:91), `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_zero_apply` (Roth/HasseDeriv.lean:112)
- Used by: Roth/Index.lean:182 (`index_prod`, empty case: `index 1 α r = 0`)

### #140 theorem Roth.index_sub_weight_le_index_hasseDeriv (public, Roth/Index.lean:109)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: Differentiating by Delta_k lowers the index by at most weight r k is a 3-line consequence of the attained minimum (exists_weight_eq_index), the Hasse composition rule hasseDeriv_hasseDeriv and index_le_weight (direct sInf proof compiled); the canonical re-aimed form weightedOrder(taylor P) le weightedOrder(taylor Delta_k P) + weight k composes from MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder and weightedOrder_le over any comm semiring with no hypothesis (compiled); hk necessary (compiled counterexample).
- action: Keep locally as the source lemma lem:index-of-derivative (callers Roth/MainLemma.lean:494, Roth/Theta.lean:390); do not upstream on its own; if MvPolynomial.hasseDeriv and a weighted order at a point are upstreamed (see Roth.index and MvPolynomial.hasseDeriv_hasseDeriv reports), ship the ENat weightedOrder form of evidence (2) alongside them.
- Type: `{σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} {k : σ →₀ ℕ} (hk : hasseDeriv k P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) : index P α r - weight r k ≤ index (hasseDeriv k P) α r`
- What: If `Δ_k P ≠ 0`, then `ind(Δ_k P; α; r) ≥ ind(P; α; r) − ∑_j k_j / r_j`: a Hasse derivative of order `k` lowers the index by at most the weight of `k`.
- Hypotheses: `hk : hasseDeriv k P ≠ 0` (necessary: without it the junk value `index 0 = 0` breaks the inequality, evidence (3)); no positivity on `r` needed.
- Uses from project: `Roth.index`, `Roth.weight`, `Roth.exists_weight_eq_index`, `Roth.index_le_weight`, `Roth.weight_add` (Roth/Box.lean), `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv` (Roth/HasseDeriv.lean:175)
- Used by: Roth/MainLemma.lean:494 (index bound for the derivative `hasseDeriv k P` in the main-lemma construction); Roth/Theta.lean:390 (`hterm`, index of `E μ ν` in the Theta argument); listed in the module docstring of Roth/Index.lean:35.

### #141 theorem Roth.le_index_sum (public, Roth/Index.lean:118)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: The finite-sum ultrametric lower bound for the index (a common lower bound c for the nonzero summands bounds the index of a nonzero sum) is le_index_iff twice plus map_sum and Finset.exists_ne_zero_of_sum_ne_zero (compiled); its canonical counterparts are AddValuation.map_le_sum and, for weightedOrder, a two-call composition of le_weightedOrder and coeff_eq_zero_of_lt_weightedOrder (compiled), so nothing new for mathlib; hs is necessary (compiled).
- action: Keep locally as the sum-form of Lemma 4-1 (single caller Roth/Theta.lean:398); do not upstream; optionally a generic MvPowerSeries.le_weightedOrder_sum could be proposed to Mathlib/RingTheory/MvPowerSeries/Order.lean as a convenience lemma, independent of this project.
- Type: `{ι : Type*} {s : Finset ι} {f : ι → MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ} (hs : ∑ i ∈ s, f i ≠ 0) {c : ℝ} (hf : ∀ i ∈ s, f i ≠ 0 → c ≤ index (f i) α r) : c ≤ index (∑ i ∈ s, f i) α r` (with `[Fintype σ]`)
- What: If a finite sum of real polynomials is nonzero and every nonzero summand has index at least `c` (at `α`, weights `r`), then the sum has index at least `c`. This is the finite-sum form of `ind(P+Q) ≥ min(ind P, ind Q)` (source Lemma 4-1).
- Hypotheses: `hs` (sum nonzero; necessary because of the junk value `index 0 = 0`, evidence (3)); `hf` (lower bound on nonzero summands only; the guard `f i ≠ 0 →` is a genuine weakening, since a zero summand has index `0`, evidence (4)).
- Uses from project: `Roth.index`, `Roth.le_index_iff`, `MvPolynomial.hasseDeriv` (via `map_sum`, it is a linear map)
- Used by: Roth/Theta.lean:398 (bound for the index of the Leibniz expansion of the generalised Wronskian determinant)

### #142 theorem Roth.weight_eq_finsuppWeight_div (public, Roth/Index.lean:130)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: Clearing denominators in the rational weight (sum d_j/r_j = (sum d_j (D/r_j))/D with D = prod r_j) is a per-term field identity from Finsupp.weight_eq_sum, Nat.cast_sum/Nat.cast_div_charZero and field_simp (compiled); the re-aimed Finsupp.weight form adds nothing mathlib lacks beyond trivial cast/scaling algebra; hr is necessary (compiled) and D can be any nonzero common multiple (compiled).
- action: Keep locally as the bridge used twice by index_eq_weightedOrder_div (Roth/Index.lean:152,155); optionally generalise to weight_eq_finsuppWeight_div_of_dvd (any nonzero common multiple D) and restate via Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) once Roth.weight is redefined; do not upstream.
- Type: `{σ : Type*} [Fintype σ] {r : σ → ℕ} (hr : ∀ j, 0 < r j) (d : σ →₀ ℕ) : weight r d = (Finsupp.weight (fun j ↦ (∏ i, r i) / r j) d : ℝ) / ∏ i, r i`
- What: For positive integers `r_j` and `D = ∏ r_j`, the rational weight `∑ d_j / r_j` of a multi-index equals the natural-number weight `∑ d_j · (D / r_j)` (with the natural weights `w_j = D / r_j`) divided by `D`.
- Hypotheses: `hr` (all `r j` positive; necessary, evidence (3); only nonvanishing is used).
- Uses from project: `Roth.weight`
- Used by: Roth/Index.lean:152 and Roth/Index.lean:155 (both inside `Roth.index_eq_weightedOrder_div`); no other file.

### #143 theorem Roth.index_eq_weightedOrder_div (public, Roth/Index.lean:143)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: The bridge index = toNat(weightedOrder_w (taylor α P))/∏r with w_j = ∏r/r_j is the project def Roth.index read through MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder and weightedOrder_le after the project rescaling weight_eq_finsuppWeight_div; it is about a project-only def so nothing goes upstream; hP is superfluous (compiled) and hr is necessary (compiled counterexample).
- action: Keep locally as the bridge used by index_mul (Roth/Index.lean:164-165); drop the superfluous hP (proof - case split P = 0 with simp [index]) and simplify the three call sites in index_mul accordingly; do not upstream.
- Type: `{σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hr : ∀ j, 0 < r j) (α : σ → ℝ) : index P α r = (((taylor α P : MvPowerSeries σ ℝ).weightedOrder fun j ↦ (∏ i, r i) / r j).toNat : ℝ) / ∏ i, r i`
- What: For positive integer parameters `r`, the Roth index of `P` at `α` equals the weighted order of the Taylor translate `P(X + α)` (as a power series) with natural weights `w_j = D / r_j`, `D = ∏ r_j`, divided by `D`.
- Hypotheses: `hP : P ≠ 0` (superfluous, evidence (1)); `hr : ∀ j, 0 < r j` (necessary, evidence (2)).
- Uses from project: `Roth.index`, `MvPolynomial.taylor`, `MvPolynomial.coeff_taylor`, `Roth.weight_eq_finsuppWeight_div`, `Roth.index_le_weight`, `Roth.le_index_iff`, `Roth.weight` (via the rewrite).
- Used by: Roth/Index.lean:164, 165 (`index_mul`, three rewrites); mentioned in the module docstring Roth/Index.lean:38. No other file.

### #144 theorem Roth.index_mul (public, Roth/Index.lean:162)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: Lemma 4-1 (ind(PQ) = ind P + ind Q) for the project-only def Roth.index is MvPowerSeries.weightedOrder_mul transported through index_eq_weightedOrder_div plus ENat.toNat_add; hP and hQ are necessary in Lean (compiled counterexample, since index 0 = 0 not +infinity), and the subject is not a mathlib notion, so nothing goes upstream.
- action: Keep in Roth/Index.lean (used by index_prod at Index.lean:185 and Theta.lean:438); if index_eq_weightedOrder_div drops its superfluous hP, simplify the three rewrites at Index.lean:164-165; do not upstream.
- Type: `{σ : Type*} [Fintype σ] {P Q : MvPolynomial σ ℝ} (hP : P ≠ 0) (hQ : Q ≠ 0) (α : σ → ℝ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) : index (P * Q) α r = index P α r + index Q α r`
- What: For nonzero real polynomials `P`, `Q` and positive integer weights `r`, the Roth index at `α` is additive: `ind(PQ) = ind(P) + ind(Q)`.
- Hypotheses: `hP`, `hQ : _ ≠ 0` (necessary in Lean, evidence (1)); `hr : ∀ j, 0 < r j` (used by the proof through `index_eq_weightedOrder_div`; mathematically expected to be superfluous, not verified, see Phase 4).
- Uses from project: `Roth.index`, `Roth.index_eq_weightedOrder_div`, `MvPolynomial.taylor` (via `map_mul` on the algebra hom).
- Used by: Roth/Index.lean:185 (`index_prod`, insert step); Roth/Theta.lean:438 (Lemma 4-2-style split of an index over a product of renamed polynomials); module docstring Roth/Index.lean:37.

### #145 theorem Roth.index_prod (public, Roth/Index.lean:175)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: Iterated Lemma 4-1 for the project-only def Roth.index; it is MvPowerSeries.weightedOrder_prod transported through index_eq_weightedOrder_div plus ENat.toNat_sum (compiled induction-free proof), hf is necessary in Lean (compiled counterexample), and the subject is not a mathlib notion, so nothing goes upstream.
- action: Keep in Roth/Index.lean (sole caller Theta.lean:407); optionally reprove via MvPowerSeries.weightedOrder_prod as in evidence/Roth.index_prod/hyps_and_alt.lean (needs import Mathlib.Data.ENat.BigOperators); do not upstream.
- Type: `{σ : Type*} [Fintype σ] {ι : Type*} (s : Finset ι) {f : ι → MvPolynomial σ ℝ} (hf : ∀ i ∈ s, f i ≠ 0) (α : σ → ℝ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) : index (∏ i ∈ s, f i) α r = ∑ i ∈ s, index (f i) α r`
- What: For a finite family of nonzero real polynomials and positive integer weights `r`, the Roth index at `α` of the product is the sum of the indices.
- Hypotheses: `hf : ∀ i ∈ s, f i ≠ 0` (necessary in Lean, evidence (1)); `hr : ∀ j, 0 < r j` (needed by `index_mul` / `index_eq_zero_iff` / the bridge; mathematically expected superfluous, not verified, same situation as `index_mul`).
- Uses from project: `Roth.index`, `Roth.index_mul`, `Roth.index_eq_zero_iff`.
- Used by: Roth/Theta.lean:407 (index of the product of matrix entries in a determinant term); module docstring Roth/Index.lean:37.

### #146 theorem Roth.index_neg (public, Roth/Index.lean:190)
- verdict: SKIP | cost: n/a | junk: REMOVE
- rationale: Unused anywhere in the project (the source step "multiplication by a sign does not change the index" is formalised at Theta.lean:402-406 via index_C_mul with c = sign s), it is the c = -1 case of Roth.index_C_mul (compiled) and a one-line simp with support_neg; its mathlib analogue MvPowerSeries.weightedOrder_neg already exists; Step 8 REMOVE fires the Step 9a pre-filter.
- action: Delete Roth.index_neg from Roth/Index.lean:189-192 (no call sites); if a negation lemma is wanted later, derive it from index_C_mul (c = -1) or, after a weightedOrder rebase of index, from MvPowerSeries.weightedOrder_neg.
- Type: `{σ : Type*} [Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : Roth.index (-P) α r = Roth.index P α r`
- What: The index of a real polynomial at `α` with weights `r` is unchanged when the polynomial is negated.
- Hypotheses: none beyond the section variable `[Fintype σ]`; no nonvanishing or positivity hypothesis is needed (both sides are `0` for `P = 0`).
- Uses from project: `Roth.index` (and implicitly `MvPolynomial.taylor` through its unfolding)
- Used by: unused in project (`grep -rnw index_neg Roth/` returns only the declaration at Roth/Index.lean:190)

### #147 theorem Roth.index_C_mul (public, Roth/Index.lean:195)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: ind(cP) = ind(P) for c ≠ 0 about the project-only def Roth.index is a one-line rewrite (map_mul, taylor_C, smul_eq_C_mul, MvPolynomial.support_smul_eq). hc is needed (compiled counterexample). The subject is not a mathlib notion, and the power-series analogue (weightedOrder of a • f) is a two-call composition of weightedOrder_mul and weightedOrder_monomial_of_ne_zero, so nothing goes upstream.
- action: Keep in Roth/Index.lean as the named form of the source's scalar-invariance identity (one caller, Roth/Theta.lean:405). Do not upstream. Optional separate tiny mathlib PR is MvPowerSeries.weightedOrder_smul (equality for a ≠ 0 over a domain) in Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean, which is unrelated to this decl.
- Type: `{σ : Type*} [Fintype σ] {c : ℝ} (hc : c ≠ 0) (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : Roth.index (C c * P) α r = Roth.index P α r`
- What: Multiplying a real polynomial by a nonzero constant does not change its Roth index at `α` with weights `r`.
- Hypotheses: `hc : c ≠ 0`, which is necessary (evidence (1)). No positivity is needed on `r`, and no nonvanishing is needed on `P`.
- Uses from project: `Roth.index`, `MvPolynomial.taylor`, `MvPolynomial.taylor_C` (Roth/Taylor.lean:55)
- Used by: Roth/Theta.lean:405 (`sum_max_sub_le_index_det`, sign factor `Equiv.Perm.sign s` of a Leibniz-expansion term). It is used nowhere else; `grep -rn index_C_mul Roth/` returns only the declaration and that call.

### #148 theorem Roth.index_mul_left_weights (public, Roth/Index.lean:200)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: ind(P; α; l r) = ind(P; α; r)/l about the project-only def Roth.index is a short composition of Set.image_smul, Set.image_congr with the project weight_mul_left and Real.sInf_smul_of_nonneg (verified), needs no 0 < l (l = 0 compiled), and its ℕ∞ power-series analogue (weightedOrder homogeneous in the weight) is a short proof from weightedOrder_le and le_weightedOrder, so nothing goes upstream.
- action: Keep in Roth/Index.lean as the source's requested weight-scaling lemma for its single call site Roth/Theta.lean:447 (lem6 bound); no mathlib PR. Optional unrelated tiny PR is MvPowerSeries.weightedOrder_nsmul_weight in Mathlib/RingTheory/MvPowerSeries/Order.lean.
- Type: `{σ : Type*} [Fintype σ] {l : ℕ} (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : Roth.index P α (fun j ↦ l * r j) = Roth.index P α r / l`
- What: Scaling all index weights `r j` by the same natural number `l` divides the index by `l`.
- Hypotheses: none. In particular no `0 < l` and no `P ≠ 0` (with `l = 0` both sides are `0`; evidence (2)).
- Uses from project: `Roth.index`, `Roth.weight`, `Roth.weight_mul_left` (Roth/Box.lean:110), `MvPolynomial.taylor` (Roth/Taylor.lean)
- Used by: Roth/Theta.lean:447 (`rw [index_mul_left_weights] at hUΘ hVΘ`, in the Lemma 6 product bound). No other use (`grep -rn index_mul_left_weights Roth/`).

### #149 theorem Roth.index_rename (public, Roth/Index.lean:212)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: ind(rename f P; α; r) = ind(P; α∘f; r∘f) for injective f, about the project-only def Roth.index, is a 5-rewrite chain (project taylor_rename, mathlib support_rename_of_injective, Finset.coe_image, Set.image_image, weight via Finsupp.sum_mapDomain_index_inj), the exact min-analogue of mathlib's weightedTotalDegree_rename_of_injective; hf is necessary (compiled counterexample), so nothing goes upstream.
- action: Keep in Roth/Index.lean as the source-requested renaming-invariance lemma (callers Roth/Theta.lean:154 and Roth/Theta.lean:442 twice); do not upstream; if Roth.weight_mapDomain loses its superfluous hf, keep passing hf here since support_rename_of_injective needs it.
- Type: `{σ : Type*} [Fintype σ] {τ : Type*} [Fintype τ] {f : σ → τ} (hf : Function.Injective f) (P : MvPolynomial σ ℝ) (α : τ → ℝ) (r : τ → ℕ) : Roth.index (rename f P) α r = Roth.index P (α ∘ f) (r ∘ f)`
- What: Embedding a real polynomial into a larger set of variables by an injective renaming does not change its Roth index, provided the point and the weights are pulled back along the renaming.
- Hypotheses: `hf : Function.Injective f`, which is necessary (evidence (1)). `[Fintype τ]` is needed because `index` is defined on `τ`. No positivity is needed on `r`, and no nonvanishing is needed on `P`.
- Uses from project: `Roth.index`, `Roth.weight` (via the unfolded `index`), `MvPolynomial.taylor`, `MvPolynomial.taylor_rename` (Roth/Taylor.lean:164), `Roth.weight_mapDomain` (Roth/Box.lean:127)
- Used by: Roth/Theta.lean:154 (`simp [map_rename, index_rename e.injective, Function.comp_def]`, an equivalence relabelling) and Roth/Theta.lean:442 (used twice, `index_rename (Option.some_injective _)` and `index_rename hinjV`, in the disjoint-variable product step). It is also mentioned in the module docstring at Roth/Index.lean:39. There are no other uses (`grep -rn index_rename Roth/`).

### #150 theorem Roth.index_le_card (public, Roth/Index.lean:224)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: The bound ind(P; α; r) ≤ card σ when deg_{x_j} P ≤ r_j, about the project-only def Roth.index, is a 3-step chain (project exists_weight_eq_index, mathlib MvPolynomial.monomial_le_degreeOf with project degreeOf_taylor_le, project weight_le_card); hP is superfluous (index 0 = 0, compiled), hd is necessary (compiled counterexample), and nothing goes upstream.
- action: Keep in Roth/Index.lean for its callers Roth/Theta.lean:91 and Roth/Theta.lean:117; optionally drop the superfluous hP (proof in evidence/Roth.index_le_card/hyps.lean), which removes the map_ne_zero_iff argument at both Theta call sites; do not upstream.
- Type: `{σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hd : ∀ j, degreeOf j P ≤ r j) (α : σ → ℝ) : Roth.index P α r ≤ Fintype.card σ`
- What: If a real polynomial has degree at most `r j` in each variable `x_j`, then its Roth index at any point, with weights `r`, is at most the number of variables.
- Hypotheses: `hP : P ≠ 0` is superfluous, because `index 0 α r = sInf ∅ = 0` (evidence (1)). `hd` is necessary (evidence (3)). There is no positivity hypothesis on `r`; `r j = 0` forces `d j = 0` and the junk `0/0 = 0` term.
- Uses from project: `Roth.index`, `Roth.exists_weight_eq_index` (Roth/Index.lean:76), `Roth.mem_support_taylor_iff` (private, Roth/Index.lean:62), `MvPolynomial.taylor`, `MvPolynomial.degreeOf_taylor_le` (Roth/Taylor.lean:170), `Roth.weight_le_card` (Roth/Box.lean:103), `Roth.weight` (via the `hdw ▸`)
- Used by: Roth/Theta.lean:91 (`indexSet_bddAbove`) and Roth/Theta.lean:117 (`Θ_le_card`). Both have the same shape, `index_le_card ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0) (by simpa [degreeOf, degrees_map_of_injective ...] using hRd) _`. There are no other uses (`grep -rn index_le_card Roth/`).

### #151 theorem Roth.index_unique (public, Roth/Index.lean:234)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: The one-variable identity ind(P; α; r) = rootMultiplicity_α(P) / r, about the project-only def Roth.index, is mathlib's Polynomial.rootMultiplicity_eq_natTrailingDegree (multiplicity = trailing degree of p(X+α)) plus the project's index API (index_le_weight, le_index_iff) and the uniqueAlgEquiv/hasseDeriv bridge; hP is superfluous (compiled), and nothing goes upstream.
- action: Keep in Roth/Index.lean for its single caller Roth/Theta.lean:242 (index_unique_le_log_div); optionally drop the superfluous hP (proof in evidence/Roth.index_unique/hyps.lean), which removes the map_ne_zero_iff argument at Theta.lean:242; do not upstream.
- Type: `{σ : Type*} [Fintype σ] [Unique σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) : index P α r = (Polynomial.rootMultiplicity (α default) (uniqueAlgEquiv ℝ σ P) : ℝ) / r default`
- What: In one variable, the index of a nonzero polynomial `P` at `α` with weight `r` equals the multiplicity of `α` as a root of `P`, divided by `r`.
- Hypotheses: `hP : P ≠ 0`. It is superfluous: both sides are `0` at `P = 0` (evidence (1)). No positivity of `r` is assumed.
- Uses from project: `Roth.index`, `Roth.index_le_weight`, `Roth.le_index_iff`, `Roth.weight` (via `simpa [weight]`), `MvPolynomial.hasseDeriv`, `MvPolynomial.uniqueAlgEquiv_hasseDeriv` (Roth/HasseDeriv.lean:266).
- Used by: Roth/Theta.lean:242 (`index_unique_le_log_div`, private, which feeds `Θ_unique_le` = source Lemma 5). The reports for `index_le_card` and `index_sub_weight_le_index_hasseDeriv` also use it in their evidence counterexamples.

### #152 theorem Roth.eq_mapDomain_some_add_single (public, Roth/Separation.lean:57)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: REPLACE
- rationale: The identity d = d.some.mapDomain some + single none (d none) is mathlib's Finsupp.optionElim_some written in a non-canonical spelling, and its single call site is closed outright by MvPolynomial.optionEquivLeft_coeff_some_coeff_none, so no new lemma is needed.
- action: At Roth/Separation.lean:107 (eq_sum_X_none_pow_mul_coeffNone) replace `rw [coeff_coeffNone, ← eq_mapDomain_some_add_single]` with `exact (optionEquivLeft_coeff_some_coeff_none R τ e P).symm` (after unfolding coeffNone), then delete the lemma; optionally restate coeff_coeffNone with `d.optionElim ν` (= MvPolynomial.optionEquivLeft_coeff_coeff); no mathlib PR.
- Type: `{τ : Type*} (d : Option τ →₀ ℕ) : d = (Finsupp.some d).mapDomain some + Finsupp.single none (d none)`
- What: Every multi-index on the variable set `Option τ` splits as its restriction to `τ`, pushed back along `some`, plus its `none`-component placed at `none`.
- Hypotheses: none beyond the type `τ` (the section's `[Fintype τ] [DecidableEq τ]` are omitted).
- Uses from project: `[]`
- Used by: Roth/Separation.lean:107 (`rw [coeff_coeffNone, ← eq_mapDomain_some_add_single]` inside `eq_sum_X_none_pow_mul_coeffNone`). No other uses anywhere in `Roth/`.

### #153 lemma Roth.coeff_X_none_pow_mul_rename (private, Roth/Separation.lean:64)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private coefficient formula coeff_e(X_none^ν * rename some Q) = [e none = ν] Q_{e.some}, used once (simp_rw in eq_sum_X_none_pow_mul_coeffNone); mathlib has only the ingredients (optionEquivLeft_coeff_some_coeff_none, optionEquivLeft_X_none) and no rename-some / optionEquivLeft compatibility lemma.
- action: Keep as private helper for its single call site Roth/Separation.lean:104 (eq_sum_X_none_pow_mul_coeffNone); optionally factor the duplicated fact optionEquivLeft (rename some Q) = C Q (here l.67-70 and in coeff_rename_mul_aeval l.124-126) into one lemma, a candidate for Mathlib/Algebra/MvPolynomial/Equiv.lean.
- Type: `∀ {τ R : Type*} [CommSemiring R] (ν : ℕ) (Q : MvPolynomial τ R) (e : Option τ →₀ ℕ), (X none ^ ν * rename some Q).coeff e = if e none = ν then Q.coeff (Finsupp.some e) else 0`
- What: In polynomials over the variables `Option τ` (with `none` the distinguished variable), the coefficient of the monomial `x^e` in `x_none^ν · Q(x_τ)` is the coefficient of `Q` at the restriction of `e` to `τ` when the `none`-exponent of `e` equals `ν`, and zero otherwise. Separation-of-variables coefficient formula for a pure power of the distinguished variable times a polynomial in the other variables.
- Hypotheses: `[CommSemiring R]` only (the section's `[Fintype τ] [DecidableEq τ]` are omitted); `classical` inside the proof.
- Uses from project: `[]` (only mathlib lemmas)
- Used by: Roth/Separation.lean: `eq_sum_X_none_pow_mul_coeffNone` (l.104, `simp_rw [coeff_X_none_pow_mul_rename]`) only; `grep -rn coeff_X_none_pow_mul_rename Roth/` gives the definition (l.64) and that single use. Transitively everything downstream of `eq_sum_X_none_pow_mul_coeffNone` (the separated representation in Lemma 2, `exists_separated_representation`, `exists_det_eq_mul`).

### #154 def Roth.coeffNone (public, Roth/Separation.lean:80)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: coeffNone P ν is by definition (rfl) mathlib's idiom (optionEquivLeft R τ P).coeff ν, which mathlib uses unnamed everywhere with a full coefficient API (optionEquivLeft_coeff_coeff, mem_support_coeff_optionEquivLeft, natDegree_optionEquivLeft), so it is a harmless project-local abbreviation, not mathlib material.
- action: Keep as a local abbreviation (no mathlib PR); re-aim downstream lemmas at optionEquivLeft - restate coeff_coeffNone (Separation.lean:85) with d.optionElim ν so it is optionEquivLeft_coeff_coeff, and treat degreeOf_coeffNone_le (Separation.lean:114) as the candidate mathlib lemma degreeOf_coeff_optionEquivLeft (Mathlib/Algebra/MvPolynomial/Equiv.lean, next to degreeOf_coeff_finSuccEquiv).
- Type: `{τ : Type*} {R : Type*} [CommSemiring R] (P : MvPolynomial (Option τ) R) (ν : ℕ) : MvPolynomial τ R` (the section's `[Fintype τ] [DecidableEq τ]` are NOT included; checked with `#check`, evidence (0))
- What: The coefficient of `x_none^ν` in `P`, viewed as a polynomial in the remaining variables `τ`.
- Hypotheses: `[CommSemiring R]` only.
- Uses from project: `[]`
- Used by: all in Roth/Separation.lean: `coeff_coeffNone` (85–87), `eq_sum_X_none_pow_mul_coeffNone` (98–107), `degreeOf_coeffNone_le` (114–115), `coeff_rename_mul_aeval` (129, unfolds it), private `eq_sum_aeval_basis_coeffNone_aux` (265–275), private `exists_coeffNone_basis_aux` (291–297), and `exists_separated_representation`'s proof (332–342). No uses outside Separation.lean.

### #155 theorem Roth.coeff_coeffNone (public, Roth/Separation.lean:85)
- verdict: NO-mathlib-has-it | cost: n/a | junk: REPLACE
- rationale: After unfolding coeffNone (rfl) this is MvPolynomial.optionEquivLeft_coeff_coeff with the multi-index spelled d.mapDomain some + single none ν instead of mathlib's canonical d.optionElim ν; both call sites are served directly by mathlib lemmas.
- action: At Roth/Separation.lean:107 use `exact optionEquivLeft_coeff_some_coeff_none R τ e P` (after unfolding) and at :129 restate coeff_rename_mul_aeval with `a.optionElim b` and rewrite with `← optionEquivLeft_coeff_coeff`; then delete coeff_coeffNone (or keep it as the one-line `optionEquivLeft_coeff_coeff R P ν d` stated with optionElim); no mathlib PR.
- Type: `{τ : Type*} {R : Type*} [CommSemiring R] (P : MvPolynomial (Option τ) R) (ν : ℕ) (d : τ →₀ ℕ) : (coeffNone P ν).coeff d = P.coeff (d.mapDomain some + Finsupp.single none ν)` (section `[Fintype τ] [DecidableEq τ]` omitted via `omit ... in`; confirmed by `#check`, evidence (0))
- What: The coefficient of `x_τ^d` in the `x_none^ν`-coefficient of `P` is the coefficient of `x_τ^d x_none^ν` in `P`.
- Hypotheses: `[CommSemiring R]` only.
- Uses from project: `Roth.coeffNone`
- Used by: `Roth.eq_sum_X_none_pow_mul_coeffNone` (Roth/Separation.lean:107, `rw [coeff_coeffNone, ← eq_mapDomain_some_add_single]`), `Roth.coeff_rename_mul_aeval` (Roth/Separation.lean:129, `rw [← coeff_coeffNone, coeffNone, ...]`). No uses outside Separation.lean (`grep -rn coeff_coeffNone Roth/`).

### #156 theorem Roth.eq_sum_X_none_pow_mul_coeffNone (public, Roth/Separation.lean:98)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: INLINE
- rationale: Unfolding coeffNone (rfl) this is the inverse of optionEquivLeft (optionEquivLeft_symm_apply, an aevalTower of rename some and X none) expanded by Polynomial.eval₂_eq_sum_range' with the bound from natDegree_optionEquivLeft, a 2-line mathlib composition (compiled in evidence).
- action: Inline the 2-line composition at its single call site Roth/Separation.lean:335 (exists_separated_representation), or at least replace the 9-line proof by it; this also orphans the private coeff_X_none_pow_mul_rename (l.64) and eq_mapDomain_some_add_single (l.57), and removes a use of coeff_coeffNone; no mathlib PR.
- Type: `{τ : Type*} {R : Type*} [CommSemiring R] (P : MvPolynomial (Option τ) R) {n : ℕ} (hn : degreeOf none P ≤ n) : P = ∑ ν ∈ Finset.range (n + 1), X none ^ ν * rename some (coeffNone P ν)`. The section's `[Fintype τ] [DecidableEq τ]` are omitted via `omit ... in` (confirmed by `#check`, evidence (0)).
- What: If `P` has degree at most `n` in `x_none`, then `P = ∑_{ν ≤ n} x_none^ν · φ_ν(x_τ)`, where `φ_ν = coeffNone P ν`.
- Hypotheses: `[CommSemiring R]`; `hn : degreeOf none P ≤ n`.
- Uses from project: `Roth.coeffNone`, `Roth.coeff_coeffNone`, `Roth.eq_mapDomain_some_add_single`, private `Roth.coeff_X_none_pow_mul_rename`.
- Used by: `Roth.exists_separated_representation` (Roth/Separation.lean:335, `exact eq_sum_X_none_pow_mul_coeffNone P hn`) only (`grep -rn` over `Roth/`).

### #157 theorem Roth.degreeOf_coeffNone_le (public, Roth/Separation.lean:114)
- verdict: YES-add-as-is | cost: CHEAP | junk: REPLACE
- rationale: Re-aimed at optionEquivLeft it is the missing mathlib lemma degreeOf_coeff_optionEquivLeft (degreeOf j ((optionEquivLeft R σ p).coeff i) ≤ degreeOf (some j) p), the absent twin of the existing degreeOf_coeff_finSuccEquiv and of totalDegree_coeff_optionEquivLeft_le; verified absent (namespace clash test) and proved in 2 lines over any CommSemiring.
- action: Upstream `MvPolynomial.degreeOf_coeff_optionEquivLeft (p) (j) (i)` to Mathlib/Algebra/MvPolynomial/Equiv.lean right after totalDegree_coeff_optionEquivLeft_le (section optionEquivLeft); locally the project lemma has no callers, so delete it (or make it `degreeOf_coeff_optionEquivLeft P j ν` until the PR lands).
- Type: `∀ {τ R : Type*} [CommSemiring R] (P : MvPolynomial (Option τ) R) (ν : ℕ) (j : τ), degreeOf j (coeffNone P ν) ≤ degreeOf (some j) P` (section `[Fintype τ] [DecidableEq τ]` omitted via `omit ... in`)
- What: Taking the coefficient of `x_none^ν` (as a polynomial in the remaining variables `τ`) does not increase the degree in any remaining variable `x_j`.
- Hypotheses: none beyond `[CommSemiring R]`.
- Uses from project: `Roth.coeffNone`
- Used by: unused in project (grep of `Roth/` and `Roth.lean` finds only the declaration at Roth/Separation.lean:114)

### #158 theorem Roth.coeff_rename_mul_aeval (public, Roth/Separation.lean:123)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The disjoint-variables coefficient identity [x_τ^a x_*^b](U(x_τ)V(x_*)) = U_a V_b is absent from mathlib (no optionEquivLeft/rename-some compatibility lemma, no Sum analogue); it should ship in mathlib's canonical a.optionElim b spelling with the missing optionEquivLeft_rename_some API, plus the literature-standard Sum form, all verified to compile.
- action: Upstream to Mathlib/Algebra/MvPolynomial/Equiv.lean optionEquivLeft_comp_rename_some, optionEquivLeft_rename_some, optionEquivLeft_aeval_X_none and the coefficient lemma stated at a.optionElim b (optionally the Sum.inl/Sum.inr form); locally restate and update call sites Theta.lean:480,486 and Separation.lean:476.
- Type: `{τ : Type*} {R : Type*} [CommSemiring R] (U : MvPolynomial τ R) (V : Polynomial R) (a : τ →₀ ℕ) (b : ℕ) : (rename some U * Polynomial.aeval (X none) V).coeff (a.mapDomain some + Finsupp.single none b) = U.coeff a * V.coeff b` (section `[Fintype τ] [DecidableEq τ]` omitted; confirmed by `#check`, evidence (0))
- What: In `R[x_τ, x_*]`, the coefficient of `x_τ^a x_*^b` in the separated product `U(x_τ) V(x_*)` is `U_a · V_b`.
- Hypotheses: `[CommSemiring R]` only.
- Uses from project: `Roth.coeff_coeffNone`, `Roth.coeffNone`
- Used by: `Roth.index_det_le` in Roth/Theta.lean:480 and :486 (`rw [hF, coeff_rename_mul_aeval, Int.cast_mul, abs_mul] at h1`, bounding coefficients of `U` and `V`); private `exists_int_polynomial_of_primitive_factor_aux` in Roth/Separation.lean:476 (`simp only [coeff_rename_mul_aeval, coeff_map] at h`).

### #159 theorem Roth.aeval_X_eq_rename (public, Roth/Separation.lean:137)
- verdict: NO-mathlib-has-it | cost: n/a | junk: KEEP
- rationale: The statement is exactly the applied form of mathlib's Polynomial.toMvPolynomial_eq_rename_comp (toMvPolynomial i is by definition aeval (X i)), and the project proof is literally AlgHom.congr_fun of that lemma; nothing new for mathlib, kept locally only as an aeval-spelled rewrite lemma.
- action: No mathlib PR. Keep as a local rw lemma for its 5 call sites (Separation.lean:162, 207, 224; Theta.lean:437, 528) or replace each rw with `rw [← Polynomial.toMvPolynomial.eq_def, Polynomial.toMvPolynomial_eq_rename_comp]` (verified in evidence); optionally mark the docstring as the applied form of the mathlib lemma.
- Type: `{R : Type*} [CommSemiring R] {σ : Type*} (i : σ) (f : Polynomial R) : Polynomial.aeval (X i : MvPolynomial σ R) f = rename (fun _ : Unit ↦ i) ((uniqueAlgEquiv R Unit).symm f)` (confirmed by `#check`, evidence (0); the section's `[Fintype τ] [DecidableEq τ]` do not appear since `τ` is unused)
- What: Substituting `X ↦ X_i` in a univariate polynomial `f` equals viewing `f` as a one-variable `MvPolynomial Unit` and renaming that variable to `i`.
- Hypotheses: `[CommSemiring R]` only.
- Uses from project: `[]`
- Used by: `Roth.hasseDeriv_rename_mul_aeval` (Roth/Separation.lean:162, `simp [aeval_X_eq_rename, degreeOf, ...]`), the degree lemma at Roth/Separation.lean:207 (`simp [aeval_X_eq_rename, ...]`), `Roth.degreeOf_none_rename_mul_aeval` (Roth/Separation.lean:224, `rw [..., aeval_X_eq_rename]`), Roth/Theta.lean:437 (`rw [aeval_X_eq_rename, _root_.map_mul, map_rename, ...]`), Roth/Theta.lean:528 (`rw [aeval_X_eq

### #160 theorem Roth.hasseDeriv_rename_mul_aeval (public, Roth/Separation.lean:146)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The factorwise rule Delta_(d,nu)(U(x_tau)V(x_none)) = (Delta_d U)(x_tau)(D^(nu) V)(x_none) for Hasse derivatives of a product in disjoint variables is absent from mathlib (which has no multivariate Hasse derivative); it should ship with the parent API in the literature-standard Sum form and at mathlib's a.optionElim index, both verified to compile.
- action: Upstream with MvPolynomial.hasseDeriv into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as hasseDeriv_rename_inl_mul_rename_inr (Sum form) plus the Option form at d.optionElim nu; locally restate at optionElim and update the single call site det_hasseDeriv_separated (Roth/Separation.lean:365, its matrix index at :353).
- Type: `{τ R : Type*} [CommSemiring R] (d : τ →₀ ℕ) (ν : ℕ) (U : MvPolynomial τ R) (V : Polynomial R) : hasseDeriv (d.mapDomain some + Finsupp.single none ν) (rename some U * Polynomial.aeval (X none) V) = rename some (hasseDeriv d U) * Polynomial.aeval (X none) (Polynomial.hasseDeriv ν V)` (section `[Fintype τ] [DecidableEq τ]` omitted; confirmed by `#check`, evidence (0))
- What: The Hasse derivative `Δ_{d + ν e_none}` of a separated product `U(x_τ) V(x_none)` is `(Δ_d U)(x_τ) · (D^{(ν)} V)(x_none)`.
- Hypotheses: `[CommSemiring R]` only.
- Uses from project: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`, `MvPolynomial.hasseDeriv_single_aeval_X`, `MvPolynomial.hasseDeriv_rename`, `Roth.aeval_X_eq_rename`
- Used by: `Roth.det_hasseDeriv_separated` in Roth/Separation.lean:365 (`rw [mul_comm (...), hasseDeriv_rename_mul_aeval]`, entries of `A Bᵀ`). No other use in `Roth/`.

### #161 theorem Roth.coeff_uniqueAlgEquiv_symm (public, Roth/Separation.lean:169)
- verdict: SKIP | cost: n/a | junk: REMOVE
- rationale: Unused anywhere in the project and merely the d = single default n instance of mathlib's MvPolynomial.coeff_uniqueAlgEquiv_symm (proof is that lemma plus Finsupp.single_eq_same); it also reuses mathlib's short name inside namespace Roth, so every caller already writes MvPolynomial.coeff_uniqueAlgEquiv_symm explicitly.
- action: Delete the theorem at Roth/Separation.lean:169-171 (no call sites; the uses at Separation.lean:179, 182 and Theta.lean:429 already cite MvPolynomial.coeff_uniqueAlgEquiv_symm); no mathlib PR.
- Type: `∀ {R : Type*} [CommSemiring R] {σ : Type*} [Unique σ] (f : Polynomial R) (n : ℕ), ((uniqueAlgEquiv R σ).symm f).coeff (Finsupp.single default n) = f.coeff n`
- What: Viewing a univariate polynomial `f` as a polynomial in one variable indexed by a singleton type `σ`, the coefficient of the monomial `x^n` is the `n`-th coefficient of `f`.
- Hypotheses: `R` a commutative semiring, `σ` with `[Unique σ]`; no others.
- Uses from project: `[]`
- Used by: unused in project (`grep -rn coeff_uniqueAlgEquiv_symm Roth/` finds only the declaration itself and three uses that are explicitly qualified `MvPolynomial.coeff_uniqueAlgEquiv_symm`: Roth/Separation.lean:179, Roth/Separation.lean:182, Roth/Theta.lean:429)

### #162 theorem Roth.degreeOf_uniqueAlgEquiv_symm (public, Roth/Separation.lean:174)
- verdict: YES-add-as-is | cost: CHEAP | junk: KEEP
- rationale: Mathlib's new uniqueAlgEquiv (2026-04) has coeff and monomial API but no degree API, while its siblings finSuccEquiv and optionEquivLeft both have natDegree = degreeOf lemmas; the forward twin natDegree_uniqueAlgEquiv plus this symm form compile over any CommSemiring with mathlib-only imports and the names are free.
- action: Upstream `MvPolynomial.natDegree_uniqueAlgEquiv` and `MvPolynomial.degreeOf_uniqueAlgEquiv_symm` (proofs in evidence reaim.lean) to Mathlib/Algebra/MvPolynomial/Equiv.lean after coeff_uniqueAlgEquiv_symm; until then keep the project lemma for its 2 call sites (Separation.lean:226, Theta.lean:427), then delete it and use the mathlib name.
- Type: `∀ {R : Type*} [CommSemiring R] {σ : Type*} [Unique σ] (f : Polynomial R), degreeOf default ((uniqueAlgEquiv R σ).symm f) = f.natDegree`
- What: If you view a univariate polynomial `f` as a polynomial in the single variable indexed by a singleton type `σ`, its degree in that variable equals `f.natDegree`.
- Hypotheses: `[CommSemiring R]` and `[Unique σ]` only.
- Uses from project: `[]` (the `coeff_uniqueAlgEquiv_symm` calls are explicitly qualified `MvPolynomial.`, so they refer to mathlib's lemma, not `Roth.coeff_uniqueAlgEquiv_symm`)
- Used by: `Roth.degreeOf_none_rename_mul_aeval` (Roth/Separation.lean:226, `.trans (degreeOf_uniqueAlgEquiv_symm V)`); `Roth.index_separated_mul_le_aux` (private, Roth/Theta.lean:427, `rw [..., degreeOf_uniqueAlgEquiv_symm]`). Both are bare-name uses that resolve to `Roth.` (no mathlib decl of that name exists).

### #163 theorem Roth.degreeOf_rename_mul_aeval (public, Roth/Separation.lean:197)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The partial-degree identity deg_{x_j}(U(x_τ)V(x_*)) = deg_{x_j} U for V ≠ 0 is absent from mathlib, as are its two building blocks (degreeOf of a rename outside the range is 0; degreeOf (p*q) = degreeOf p when q ≠ 0 avoids the variable). The project form over-assumes CommRing + IsDomain (CommSemiring + NoZeroDivisors suffices, verified) and should ship as the Sum.inl/Sum.inr form plus the two API lemmas.
- action: Upstream degreeOf_rename_eq_zero_of_notMem_range (Mathlib/Algebra/MvPolynomial/Degrees.lean, after degreeOf_rename_of_injective), degreeOf_mul_of_degreeOf_eq_zero_right and degreeOf_inl_rename_inl_mul_rename_inr (Mathlib/Algebra/MvPolynomial/NoZeroDivisors.lean, after degreeOf_mul_eq), all proved in evidence weaken.lean; locally weaken to CommSemiring + NoZeroDivisors with the 2-rewrite proof, keeping its single call site Separation.lean:554.
- Type: `∀ {τ : Type*} {R : Type*} [CommRing R] [IsDomain R] (U : MvPolynomial τ R) {V : Polynomial R}, V ≠ 0 → ∀ (j : τ), degreeOf (some j) (rename some U * Polynomial.aeval (X none) V) = degreeOf j U` (section `[Fintype τ] [DecidableEq τ]` omitted; confirmed by `#check` in the evidence file)
- What: In `R[x_τ, x_*]` over a domain, for `V ≠ 0` the degree of the separated product `U(x_τ) V(x_*)` in a variable `x_j`, `j ∈ τ`, equals the degree of `U` in `x_j`.
- Hypotheses: `[CommRing R] [IsDomain R]` (section variables), `hV : V ≠ 0`.
- Uses from project: `Roth.aeval_X_eq_rename`
- Used by: `Roth.exists_det_eq_mul` in Roth/Separation.lean:554 (`rw [← degreeOf_rename_mul_aeval U hV j, ← hFUV]`, bounding `degreeOf j U` by the degree of the determinant `F`). No other uses in `Roth/`.

### #164 theorem Roth.degreeOf_none_rename_mul_aeval (public, Roth/Separation.lean:213)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The identity deg_{x_*}(U(x_τ)V(x_*)) = natDegree V for U ≠ 0 is absent from mathlib, as are its building blocks (degreeOf of a rename outside the range is 0; degreeOf (p*q) = degreeOf q when p ≠ 0 avoids the variable; degreeOf i (p.toMvPolynomial i) = natDegree p); the project form over-assumes CommRing + IsDomain (CommSemiring + NoZeroDivisors suffices, verified) and should ship as those API lemmas plus a Sum.inr corollary.
- action: Upstream Polynomial.degreeOf_toMvPolynomial_self (Mathlib/Algebra/MvPolynomial/Equiv.lean, section toMvPolynomial, after degreeOf_uniqueAlgEquiv_symm lands) together with the twin's degreeOf_rename_eq_zero_of_notMem_range, a left-factor degreeOf_mul_of_degreeOf_eq_zero_left and degreeOf_inr_rename_inl_mul_rename_inr (Mathlib/Algebra/MvPolynomial/NoZeroDivisors.lean), all proved in evidence weaken.lean; locally weaken to CommSemiring + NoZeroDivisors with the 2-step proof, keeping its single call site Separation.lean:557.
- Type: `∀ {τ : Type*} {R : Type*} [CommRing R] [IsDomain R] {U : MvPolynomial τ R}, U ≠ 0 → ∀ (V : Polynomial R), degreeOf none (rename some U * Polynomial.aeval (X none) V) = V.natDegree` (section `[Fintype τ] [DecidableEq τ]` omitted; confirmed by `#check` in the evidence file)
- What: In `R[x_τ, x_*]` over a domain, for `U ≠ 0` the degree of the separated product `U(x_τ) V(x_*)` in the distinguished variable `x_*` equals `natDegree V`.
- Hypotheses: `[CommRing R] [IsDomain R]` (section variables), `hU : U ≠ 0`.
- Uses from project: `Roth.aeval_X_eq_rename`, `Roth.degreeOf_uniqueAlgEquiv_symm`
- Used by: `Roth.exists_det_eq_mul` in Roth/Separation.lean:557 (`rw [← degreeOf_none_rename_mul_aeval hU V, ← hFUV]`, bounding `natDegree V` by the `x_none`-degree of the determinant `F`). No other uses in `Roth/` (grep over `Roth/` for the bare name, which covers in-namespace calls).

### #165 lemma Roth.linearIndependent_coordinate_polynomials_aux (private, Roth/Separation.lean:235)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-use helper of exists_separated_representation proving the coordinate polynomials sum_nu C(a nu rho) X^nu are linearly independent in rho; a genuine linear-algebra step (dual of a spanning family) not stated in mathlib, though composable from Basis.linearIndependent_coord.
- action: Keep as private helper for its single call site Roth/Separation.lean:339 (exists_separated_representation); optional golf via b.linearIndependent_coord.map' with an injective map Dual(span) to R[X] is possible but untested and not required.
- Type: `∀ {R M : Type*} [CommRing R] [AddCommMonoid M] [Module R M] {n l : ℕ} (v : Fin (n + 1) → M) (b : Module.Basis (Fin l) R (Submodule.span R (Set.range v))), LinearIndependent R (fun ρ ↦ ∑ ν : Fin (n + 1), Polynomial.C (b.repr ⟨v ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ) * Polynomial.X ^ (ν : ℕ))` (declared `private lemma`; the section variables `τ`, `Fintype τ`, `DecidableEq τ` are omitted and `K` is n
- What: Let `v_0, …, v_n` be vectors in an `R`-module and `b_1, …, b_l` a basis of their span, with `v_ν = ∑_ρ a_{νρ} b_ρ`. Then the `l` polynomials `φ_ρ(X) = ∑_ν a_{νρ} X^ν ∈ R[X]` are linearly independent over `R`. Equivalently, the columns of the `(n+1) × l` coordinate matrix `(a_{νρ})` are linearly independent, because the `v_ν` span. This is the "the `φ_ν` are linearly independent" claim in the separated decomposition of §2, proof of Lemma 2.
- Hypotheses: `[CommRing R]` (ring, not just semiring, because `Fintype.linearIndependent_iff` is used; commutativity is needed for `g ρ • b.coord ρ` to be a linear map). `[AddCommMonoid M] [Module R M]`. No field assumption: it is stated in more generality than the caller needs (the caller uses a field `K`). No 
- Uses from project: `[]` (only mathlib: `Fintype.linearIndependent_iff`, `Polynomial.finsetSum_coeff`, `Polynomial.coeff_C_mul_X_pow`, `Finset.sum_eq_single`, `Module.Basis.coord`, `LinearMap.ext_on`, `Submodule.span_span_coe_preimage`, `Module.Basis.repr_self`, `LinearMap.congr_fun`).
- Used by: Roth/Separation.lean:339 `Roth.exists_separated_representation` only (supplies `LinearIndependent K φ`); `grep -rn linearIndependent_coordinate_polynomials Roth/` returns only the definition (l.235) and this use. Transitively everything downstream of the separated representation (Lemma 2).

### #166 lemma Roth.eq_sum_aeval_basis_coeffNone_aux (private, Roth/Separation.lean:265)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-use helper of exists_separated_representation that regroups P = sum_nu x_none^nu coeffNone P nu, after expanding each coeffNone P nu in a basis of their span, as sum_rho phi_rho(x_none) psi_rho(x_tau); a bookkeeping rearrangement specific to Lemma 2 with no mathlib counterpart.
- action: Keep as private helper for its single call site Roth/Separation.lean:342 (exists_separated_representation); no change needed.
- Type: `∀ {τ : Type*} {R : Type*} [CommSemiring R] {P : MvPolynomial (Option τ) R} {n l : ℕ}, (P = ∑ ν : Fin (n + 1), X none ^ (ν : ℕ) * rename some (coeffNone P ν)) → ∀ (b : Module.Basis (Fin l) R (Submodule.span R (Set.range (fun ν : Fin (n + 1) ↦ coeffNone P ν)))), P = ∑ ρ, Polynomial.aeval (X none : MvPolynomial (Option τ) R) (∑ ν : Fin (n + 1), Polynomial.C (b.repr ⟨coeffNone P ν, Submodule.subset_s
- What: Suppose `P = ∑_{ν ≤ n} x_none^ν · c_ν(x_τ)` where `c_ν = coeffNone P ν`, and let `b_1, …, b_l` be a basis of the `R`-span of `c_0, …, c_n`, with `c_ν = ∑_ρ a_{νρ} b_ρ`. Then `P = ∑_ρ φ_ρ(x_none) · b_ρ(x_τ)` where `φ_ρ(X) = ∑_ν a_{νρ} X^ν`. This is the identity part of the separated decomposition in §2, proof of Lemma 2 (swap the order of summation after expanding each coefficient polynomial in the basis).
- Hypotheses: `[CommSemiring R]` only (more general than the caller's field `K`); `hP` the expansion of `P` in powers of `x_none` up to degree `n` (supplied by the caller from `eq_sum_X_none_pow_mul_coeffNone`); `b` any finite basis of the span. No redundant hypotheses: `hP` is essential (it encodes `degreeOf non
- Uses from project: `Roth.coeffNone` (Roth/Separation.lean:80). Everything else is mathlib.
- Used by: Roth/Separation.lean:342 `Roth.exists_separated_representation` only (supplies the final identity `P = ∑ ν, aeval (X none) (φ ν) * rename some (ψ ν)`); `grep -rn eq_sum_aeval_basis_coeffNone_aux Roth/` returns only the definition (l.265) and this use.

### #167 lemma Roth.exists_coeffNone_basis_aux (private, Roth/Separation.lean:291)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-use helper of exists_separated_representation producing a finite basis of the span of the x_none-coefficients of a nonzero P with 1 <= l <= n+1 and per-variable degree bounds; Lemma 2 bookkeeping with no mathlib counterpart.
- action: Keep as private helper for its single call site Roth/Separation.lean:336 (exists_separated_representation); no change needed.
- Type: `∀ {τ : Type*} {K : Type*} [Field K] {P : MvPolynomial (Option τ) K}, P ≠ 0 → ∀ {n : ℕ}, (P = ∑ ν : Fin (n + 1), X none ^ (ν : ℕ) * rename some (coeffNone P ν)) → ∃ l, ∃ b : Module.Basis (Fin l) K (Submodule.span K (Set.range (fun ν : Fin (n + 1) ↦ coeffNone P ν))), 1 ≤ l ∧ l ≤ n + 1 ∧ ∀ ρ j, degreeOf j (b ρ : MvPolynomial τ K) ≤ degreeOf (some j) P` (declared `private lemma`; section variables `[
- What: For a nonzero `P = ∑_{ν ≤ n} x_none^ν c_ν(x_τ)` over a field (with `c_ν = coeffNone P ν`), the span `V` of `c_0, …, c_n` has a basis `b_1, …, b_l` with `1 ≤ l ≤ n + 1`, and every basis vector has degree in `x_j` at most `degreeOf (some j) P`. This is the basis-choice step of the separated decomposition in §2, proof of Lemma 2.
- Hypotheses: `[Field K]` (needed for finite-dimensionality/`finBasis` and `finrank_pos`; a free-module version over a PID would also work but is not needed); `hP : P ≠ 0` (essential for `1 ≤ l`); `hP'` the expansion of `P` in powers of `x_none` up to `n` (used only to derive some `c_ν ≠ 0`; it encodes `degreeOf 
- Uses from project: `Roth.coeffNone` (Roth/Separation.lean:80, defined as `(optionEquivLeft R τ P).coeff ν`, which is why the mathlib lemma `MvPolynomial.mem_support_coeff_optionEquivLeft` applies after unfolding). All other identifiers (`restrictSupport`, `monomial_le_degreeOf`, `degreeOf_le_iff`, `finrank_range_le_card`, `Module.finBasis`, `Module.finrank_pos_iff_exists_ne_zero`, `FiniteDimensional.span_of_finite`)
- Used by: Roth/Separation.lean:336 `Roth.exists_separated_representation` only (`obtain ⟨l, b, hl1, hl2, hdegree⟩ := exists_coeffNone_basis_aux hP hP'`); `grep -rn exists_coeffNone_basis_aux Roth/` returns only the definition (l.291) and this use.

### #168 theorem Roth.exists_separated_representation (public, Roth/Separation.lean:325)
- verdict: BORDERLINE-needs-human | cost: MODERATE | junk: KEEP
- rationale: The real content is the standard linear-algebra fact that over a field every tensor x in M ⊗ N is a sum of l pure tensors with both factor families linearly independent (tensor/Schmidt rank decomposition). Mathlib has TensorProduct.exists_sum_tmul_eq without independence, so that abstract lemma is a genuine gap. But the project form is specialised to MvPolynomial (Option τ) K, adds degree bounds its only caller discards, and moving to the tensor form is a restatement plus a new proof, not a mechanical edit.
- action: Ask the user whether to upstream the abstract lemma TensorProduct.exists_sum_tmul_eq_of_linearIndependent (field K, x in M ⊗[K] N) to Mathlib/LinearAlgebra/TensorProduct/Finiteness.lean next to exists_sum_tmul_eq. Keep this theorem locally either way. Optionally drop the two degree-bound conclusions, which the only caller exists_rat_factors_det_hasseDeriv_aux (Separation.lean:521) discards.
- Type: `{τ : Type*} {K : Type*} [Field K] {P : MvPolynomial (Option τ) K} (hP : P ≠ 0) {n : ℕ} (hn : degreeOf none P ≤ n) : ∃ l, 1 ≤ l ∧ l ≤ n + 1 ∧ ∃ (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K), LinearIndependent K φ ∧ LinearIndependent K ψ ∧ (∀ ν, (φ ν).natDegree ≤ n) ∧ (∀ ν j, degreeOf j (ψ ν) ≤ degreeOf (some j) P) ∧ P = ∑ ν, Polynomial.aeval (X none) (φ ν) * rename some (ψ ν)` (`[Finty
- What: Over a field, a nonzero polynomial `P(x_τ, x_none)` of degree at most `n` in `x_none` can be written as `∑_{ν<l} φ_ν(x_none) ψ_ν(x_τ)`. Here `1 ≤ l ≤ n+1`, both families are linearly independent, `deg φ_ν ≤ n`, and `deg_{x_j} ψ_ν ≤ deg_{x_j} P`.
- Hypotheses: `[Field K]` (basis of a subspace), `hP : P ≠ 0` (only for `1 ≤ l`), `hn` (degree bound in `x_none`).
- Uses from project: `Roth.coeffNone`, `Roth.eq_sum_X_none_pow_mul_coeffNone`, private `Roth.exists_coeffNone_basis_aux`, private `Roth.linearIndependent_coordinate_polynomials_aux`, private `Roth.eq_sum_aeval_basis_coeffNone_aux`.
- Used by: `Roth.exists_rat_factors_det_hasseDeriv_aux` (private, Roth/Separation.lean:521–523). It uses `l, hl1, hl2, φ, ψ, hφ, hψ, hPQ` and discards both degree-bound conclusions (`-, -`). Also mentioned in the module docstring (line 31). No other uses in `Roth/`.

### #169 theorem Roth.det_hasseDeriv_separated (public, Roth/Separation.lean:351)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: The factorisation GW_(D,nu)(sum_rho phi_rho(x_none) psi_rho(x_tau)) = GW_D(psi) W(phi) (Hasse matrix of a separated sum is A B^T) is absent from mathlib, which has no multivariate Hasse derivative or n-ary Wronskian; it is the natural product formula for the planned generalized-Wronskian API and weakens from [Field K] to [CommRing R] with the proof unchanged (verified), but should ship at the optionElim index decided for its helper.
- action: Upstream with Roth.genWronskian and Roth.wronskian (CommRing versions) in the planned Mathlib/RingTheory/MvPolynomial/Wronskian.lean, restated over [CommRing R] with matrix index (D mu).optionElim nu; locally keep, updating the single call site exists_rat_factors_det_hasseDeriv_aux (Roth/Separation.lean:529) if the index changes.
- Type: `{τ K : Type*} [Field K] {l : ℕ} (D : Fin l → τ →₀ ℕ) (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K) : (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none ν) (∑ ρ, Polynomial.aeval (X none) (φ ρ) * rename some (ψ ρ))).det = rename some (genWronskian D ψ) * Polynomial.aeval (X none) (wronskian φ)` (section `[Fintype τ] [DecidableEq τ]` omitted; confirmed b
- What: For a separated sum `P = ∑_ρ φ_ρ(x_none) ψ_ρ(x_τ)`, the determinant `det(Δ_{(D μ, ν)} P)_{μ,ν}` equals `GW_D(ψ)(x_τ) · W(φ)(x_none)`, the product of the generalized Wronskian of `ψ` and the (Hasse) Wronskian of `φ`.
- Hypotheses: `[Field K]` (section variable; only needed because the parent defs `genWronskian`, `wronskian` are stated over a field).
- Uses from project: `Roth.genWronskian`, `Roth.wronskian`, `Roth.wronskianMatrix`, `MvPolynomial.hasseDeriv`, `Roth.hasseDeriv_rename_mul_aeval`
- Used by: `Roth.exists_rat_factors_det_hasseDeriv_aux` (private) at Roth/Separation.lean:529 (`rw [hFdef, RingHom.map_det, ← det_hasseDeriv_separated D φ ψ, ← hPQ]`). Also named in the module docstring (Separation.lean:33). No other use in `Roth/`.

### #170 theorem Roth.exists_sum_mul_eq_gcd (public, Roth/Separation.lean:374)
- verdict: NO-mathlib-has-it | cost: n/a | junk: REPLACE
- rationale: Restatement over ℤ (with sides and factors swapped) of mathlib's Finset.gcd_eq_sum_mul, which holds in any IsBezout NormalizedGCDMonoid commutative ring; the project proof is literally simpa using that lemma.
- action: At Roth/Separation.lean:446 (exists_int_eq_of_gcd_eq_one) use `obtain ⟨z, hz⟩ := Finset.gcd_eq_sum_mul s u` and adapt the calc to the orientation `s.gcd u = ∑ i ∈ s, u i * z i` (compiled in evidence); then delete exists_sum_mul_eq_gcd; no mathlib PR.
- Type: `∀ {ι : Type u_1} (s : Finset ι) (u : ι → ℤ), ∃ z : ι → ℤ, ∑ i ∈ s, z i * u i = s.gcd u` (confirmed by `#check`, evidence (0))
- What: Bézout's identity for a finite family of integers: the (normalized) finset gcd of `u` over `s` is an integer linear combination of the `u i`, `i ∈ s`.
- Hypotheses: none beyond the data `s`, `u`; ring fixed to `ℤ`.
- Uses from project: `[]`
- Used by: `Roth.exists_int_eq_of_gcd_eq_one` (Roth/Separation.lean:446, `obtain ⟨z, hz⟩ := exists_sum_mul_eq_gcd s u`). No other uses (`grep -rn exists_sum_mul_eq_gcd Roth/`).

### #171 theorem Roth.exists_nat_smul_eq_map (public, Roth/Separation.lean:380)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: REPLACE
- rationale: Mathlib has denominator clearing for univariate polynomials (IsLocalization.integerNormalization_spec) but no MvPolynomial analogue; the ℤ→ℚ positive-N form is a specialisation of the localization statement (∃ b ∈ M, ∃ U, map (algebraMap R S) U = b • G), which is verified to compile and to serve the only call site.
- action: Add `MvPolynomial.exists_smul_eq_map_of_isLocalization` (evidence (2)) to Mathlib/RingTheory/MvPolynomial/Localization.lean; in the project, use it at Roth/Separation.lean:410 (exists_primitive_smul_eq, compiled as evidence (5)) and delete exists_nat_smul_eq_map.
- Type: `∀ {σ : Type u_1} (G : MvPolynomial σ ℚ), ∃ N U, 0 < N ∧ (map (Int.castRingHom ℚ)) U = ↑N • G` (from `#check`, evidence (0)), with `N : ℕ` and `U : MvPolynomial σ ℤ`
- What: clearing denominators. Every rational multivariate polynomial `G` has a positive integer multiple `N • G` whose coefficients all lie in ℤ, i.e. `N • G` is the image of an integer polynomial `U`.
- Hypotheses: none. Base rings are fixed to ℤ ⊂ ℚ, and the multiplier must be a positive natural number.
- Uses from project: `[]`
- Used by: `Roth.exists_primitive_smul_eq` (Roth/Separation.lean:410, `obtain ⟨N, U0, hN, hU0⟩ := exists_nat_smul_eq_map G`). There are no other uses (`grep -rn exists_nat_smul_eq_map Roth/`).

### #172 theorem Roth.exists_primitive_smul_eq (public, Roth/Separation.lean:406)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Mathlib has content/primPart only for univariate Polynomial (RingTheory/Polynomial/Content.lean) and no MvPolynomial content or primitive-part API; the ℤ/ℚ statement is the instance of a GCD-domain/fraction-field statement that splits into an MvPolynomial content decomposition plus denominator clearing, both compiled as evidence.
- action: Add MvPolynomial.exists_eq_C_gcd_mul (content decomposition, evidence (2)) and MvPolynomial.exists_primitive_smul_eq_map (GCD domain R, IsFractionRing R K, evidence (3)) next to MvPolynomial.isLocalization in Mathlib/RingTheory/MvPolynomial/Localization.lean (or a new MvPolynomial/Content.lean); in the project replace the body at Roth/Separation.lean:406 by the specialisation (evidence (4)); sole caller exists_int_factors (Separation.lean:491) is unchanged.
- Type: `∀ {σ : Type u_1} {G : MvPolynomial σ ℚ}, G ≠ 0 → ∃ g U, g ≠ 0 ∧ (map (Int.castRingHom ℚ)) U = g • G ∧ (U.support.gcd fun d => U.coeff d) = 1` (from `#check`, evidence (0)), with `g : ℚ`, `U : MvPolynomial σ ℤ`.
- What: every nonzero rational multivariate polynomial has a nonzero rational multiple that is an integer polynomial whose coefficients have gcd 1 (a primitive integral polynomial).
- Hypotheses: `hG : G ≠ 0` (essential: for `G = 0` the gcd condition forces `U ≠ 0`, impossible). Base rings fixed to ℤ ⊂ ℚ.
- Uses from project: `Roth.exists_nat_smul_eq_map`
- Used by: `Roth.exists_int_factors` (Roth/Separation.lean:491, `obtain ⟨g, U, hg, hUmap, hgcd⟩ := exists_primitive_smul_eq hU`). No other uses (`grep -rn exists_primitive_smul_eq Roth/`).

### #173 theorem Roth.exists_int_eq_of_gcd_eq_one (public, Roth/Separation.lean:443)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: The ℤ/ℚ integrality test is the R = ℤ, M = ℚ, N = 1 instance of mathlib's Submodule.mem_of_span_top_of_smul_mem (unit ideal generated by s and r • x in N for each r gives x in N), once the hypothesis s.gcd u = 1 is turned into Ideal.span (u '' s) = ⊤ with Finset.gcd_eq_sum_mul; both steps compile from mathlib alone (evidence (4)), so nothing to upstream for this decl.
- action: No mathlib PR; keep as the local source-mirroring helper for its single caller exists_int_polynomial_of_primitive_factor_aux (Roth/Separation.lean:473), optionally reproving it via Submodule.mem_of_span_top_of_smul_mem plus Submodule.mem_one (evidence (4)); a tiny Finset Bézout bridge Ideal.span (u '' s) = ⊤ from s.gcd u = 1 (evidence (1)) could go to Mathlib/RingTheory/PrincipalIdealDomain.lean next to Finset.gcd_eq_sum_mul as a separate optional contribution.
- Type: `∀ {ι : Type u_1} {s : Finset ι} {u : ι → ℤ}, s.gcd u = 1 → ∀ {v : ℚ}, (∀ a ∈ s, ∃ z : ℤ, ↑(u a) * v = ↑z) → ∃ z : ℤ, v = ↑z` (from `#check`, evidence (0))
- What: if integers `u_a` (`a ∈ s`) have gcd 1 and every product `u_a v` with a rational `v` is an integer, then `v` is an integer.
- Hypotheses: `hu : s.gcd u = 1` (primitivity); `hv : ∀ a ∈ s, ∃ z : ℤ, (u a : ℚ) * v = z`.
- Uses from project: `Roth.exists_sum_mul_eq_gcd`
- Used by: `Roth.exists_int_polynomial_of_primitive_factor_aux` (private, Roth/Separation.lean:473). No other use (`grep -rn exists_int_eq_of_gcd_eq_one Roth/`).

### #174 lemma Roth.rescale_separated_factor_aux (private, Roth/Separation.lean:457)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-step rescaling identity (if U = g U' with g nonzero then rename U' * V'(x_none) = rename U * (g^-1 V')(x_none)) used once in exists_int_factors; mathlib has only the generic pieces (rename is an AlgHom, aeval_C, smul_eq_C_mul).
- action: Keep as private helper for its single call site Roth/Separation.lean:492 (exists_int_factors, result hF' reused at l.493 and l.502); optional inline as a have would need the long equation retyped, so not worth it.
- Type: `∀ {τ K : Type*} [Field K] {U' U : MvPolynomial τ K} {V' : Polynomial K} {F : MvPolynomial (Option τ) K} {g : K}, g ≠ 0 → U = g • U' → F = rename some U' * Polynomial.aeval (X none) V' → F = rename some U * Polynomial.aeval (X none) (Polynomial.C g⁻¹ * V')`
- What: Rescaling of a separated factorisation. If F = U'(x_τ) V'(x_none) and U = g U' with g a nonzero scalar, then F = U(x_τ) (g⁻¹ V')(x_none): the scalar moved into the first factor is compensated by its inverse in the second.
- Hypotheses: `[Field K]` (only `g⁻¹` with `mul_inv_cancel₀` and commutativity are needed, so a `Semifield` would suffice); `hg : g ≠ 0`; `hUmap : U = g • U'`; `hF` the given factorisation. Section variables `[Fintype τ] [DecidableEq τ]` are omitted (`omit ... in`).
- Uses from project: `[]` (only mathlib lemmas: `map_mul`, `Polynomial.aeval_C`, `MvPolynomial.algebraMap_eq`, `MvPolynomial.smul_eq_C_mul`, `MvPolynomial.rename_C`, `mul_mul_mul_comm`, `MvPolynomial.C_mul`, `mul_inv_cancel₀`, `MvPolynomial.C_1`, `one_mul`)
- Used by: Roth/Separation.lean: `exists_int_factors` (l.484; `have hF' := rescale_separated_factor_aux hg hUmap hF` at l.492, with `K := ℚ`, `U := map (Int.castRingHom ℚ) U`). `grep -rn rescale_separated_factor_aux Roth/` gives only the definition (l.457) and that use. Transitively: `exists_det_eq_mul` (Lemma 2, l.540) and downstream.

### #175 lemma Roth.exists_int_polynomial_of_primitive_factor_aux (private, Roth/Separation.lean:466)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private separated-variables Gauss-lemma step (primitive integral U and integral F = U(x_tau) V'(x_none) force V' integral) used once in exists_int_factors; mathlib's Gauss lemma is univariate and needs both factors primitive, so it does not cover this.
- action: Keep as private helper for its single call site Roth/Separation.lean:493 (exists_int_factors); no change needed.
- Type: `∀ {τ : Type u_1} {U : MvPolynomial τ ℤ} {V' : Polynomial ℚ} {F : MvPolynomial (Option τ) ℤ}, U.support.gcd ⇑U.coeff = 1 → map (Int.castRingHom ℚ) F = rename some (map (Int.castRingHom ℚ) U) * Polynomial.aeval (X none) V' → ∃ V : Polynomial ℤ, Polynomial.map (Int.castRingHom ℚ) V = V'`
- What: Integrality of the second factor in a separated factorisation. If U is an integral polynomial in the variables x_τ whose coefficients have gcd 1, and the integral polynomial F in x_τ, x_none equals U(x_τ) V'(x_none) over ℚ, then V' has integral coefficients. (Coefficient of x^a x_none^b in F is u_a v_b; primitivity of U gives an integral combination of the u_a equal to 1.)
- Hypotheses: `hgcd : U.support.gcd U.coeff = 1` (primitivity of U); `hF` the rational factorisation of the integral F. Section variables `[Fintype τ] [DecidableEq τ]` are omitted (`omit ... in`). No nonvanishing hypotheses are needed (all used).
- Uses from project: `Roth.exists_int_eq_of_gcd_eq_one` (Roth/Separation.lean:443), `Roth.coeff_rename_mul_aeval` (Roth/Separation.lean:123). Mathlib: `Polynomial.mem_map_range`, `MvPolynomial.coeff_map`.
- Used by: Roth/Separation.lean: `exists_int_factors` (l.493, `obtain ⟨V, hVmap⟩ := exists_int_polynomial_of_primitive_factor_aux hgcd hF'`). `grep -rn exists_int_polynomial_of_primitive_factor_aux Roth/` gives only the definition (l.466) and that use. Transitively: `exists_det_eq_mul` (Lemma 2) and downstream.

### #176 theorem Roth.exists_int_factors (public, Roth/Separation.lean:485)
- verdict: BORDERLINE-needs-human | cost: CHEAP | junk: KEEP
- rationale: A separated-variables instance of Gauss's lemma for MvPolynomial (factorisation over Frac R descends to R with equal partial degrees); mathlib's Gauss lemma is univariate only, the UFD/fraction-field generalisation compiles (evidence (6)), but whether mathlib wants this rename-some/aeval-X-none shape or only the general MvPolynomial Gauss lemma (not yet compiled, needs an MvPolynomial content API) is a judgment call.
- action: Keep in project (sole caller exists_det_eq_mul, Roth/Separation.lean:552); if upstreaming, first land the MvPolynomial content API from the Roth.exists_primitive_smul_eq verdict, then decide between exists_factors_of_map_eq_rename_mul_aeval (evidence (6), UFD R, IsFractionRing R K) and a general MvPolynomial Gauss lemma in Mathlib/RingTheory/MvPolynomial/Content.lean (new) or Mathlib/RingTheory/Polynomial/GaussLemma.lean.
- Type: `∀ {τ : Type u_1} {U' : MvPolynomial τ ℚ} {V' : Polynomial ℚ}, U' ≠ 0 → V' ≠ 0 → ∀ {F : MvPolynomial (Option τ) ℤ}, map (Int.castRingHom ℚ) F = rename some U' * Polynomial.aeval (X none) V' → ∃ U V, U ≠ 0 ∧ V ≠ 0 ∧ F = rename some U * Polynomial.aeval (X none) V ∧ (∀ j, degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree` (from `#check`, evidence (0)).
- What: if an integer polynomial `F(x_τ, y)` factors over ℚ as `U'(x_τ) V'(y)` with nonzero factors, then it factors over ℤ as `U(x_τ) V(y)` with nonzero factors of the same partial degrees.
- Hypotheses: `hU : U' ≠ 0` (needed for the primitive multiple), `hV : V' ≠ 0` (only for the conclusion `V ≠ 0`), `hF` the rational factorisation.
- Uses from project: `Roth.exists_primitive_smul_eq`, `Roth.rescale_separated_factor_aux` (private), `Roth.exists_int_polynomial_of_primitive_factor_aux` (private; itself uses `Roth.exists_int_eq_of_gcd_eq_one`, `Roth.coeff_rename_mul_aeval`)
- Used by: `Roth.exists_det_eq_mul` (Roth/Separation.lean:552, `obtain ⟨U, V, hU, hV, hFUV, -, -⟩ := exists_int_factors hU' hV' hFmap`); mentioned in module docstring Separation.lean:35. No other uses (`grep -rn exists_int_factors Roth/`). Indirectly feeds `Roth/Theta.lean:571` through `exists_det_eq_mul`.

### #177 lemma Roth.exists_rat_factors_det_hasseDeriv_aux (private, Roth/Separation.lean:510)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private rational half of Lemma 2 (the Hasse-derivative determinant of a nonzero integer P factors over Q as U(x_tau) V(x_none) with nonzero factors), used once in exists_det_eq_mul; no mathlib counterpart (mathlib has no multivariate Hasse derivative or generalized Wronskian).
- action: Keep as private helper for its single call site Roth/Separation.lean:551 (exists_det_eq_mul); inlining would add ~22 lines to Lemma 2 and blur the Q-factorisation / Z-integrality split.
- Type: `∀ {τ : Type*} [Finite τ] {P : MvPolynomial (Option τ) ℤ}, P ≠ 0 → ∀ {n : ℕ}, degreeOf none P ≤ n → ∃ l, 1 ≤ l ∧ l ≤ n + 1 ∧ ∃ D : Fin l → (τ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ ∃ (U : MvPolynomial τ ℚ) (V : Polynomial ℚ), U ≠ 0 ∧ V ≠ 0 ∧ map (Int.castRingHom ℚ) (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none ν) P).det = rename some U * Polynomial.aeval (X none) V`
- What: Rational form of Roth's Lemma 2. For a nonzero integer polynomial P in the variables x_τ and x_none with degree at most n in x_none, there are 1 ≤ l ≤ n + 1 and differential operators Δ_μ (multi-indices D μ in the x_τ variables of order at most μ) such that the l×l determinant det(Δ_μ ∂_{x_none}^ν P / ν!) (Hasse derivatives), viewed over ℚ, factors as U(x_τ) V(x_none) with U, V nonzero.
- Hypotheses: `[Finite τ]` (needed by `exists_genWronskian_ne_zero`); `hP : P ≠ 0`; `hn : degreeOf none P ≤ n`. Section variables `[Fintype τ] [DecidableEq τ]` omitted (`omit ... in`). All hypotheses used.
- Uses from project: `Roth.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.hasseDeriv_map` (Roth/HasseDeriv.lean:134), `Roth.exists_separated_representation` (Roth/Separation.lean:325), `Roth.det_hasseDeriv_separated` (Roth/Separation.lean:351), `Roth.exists_genWronskian_ne_zero` (Roth/GenWronskian.lean:254), `Roth.genWronskian` (Roth/GenWronskian.lean:32), `Roth.wronskian` (Roth/Wronskian.lean:60), `Roth.wronskian_ne_ze
- Used by: Roth/Separation.lean: `exists_det_eq_mul` (Lemma 2, l.542; call at l.551 `exists_rat_factors_det_hasseDeriv_aux hP (hr none)`). `grep -rn exists_rat_factors_det_hasseDeriv_aux Roth/` gives only the definition (l.510) and this use. Transitively everything downstream of Lemma 2.

### #178 theorem Roth.exists_det_eq_mul (public, Roth/Separation.lean:542)
- verdict: BORDERLINE-needs-human | cost: EXPENSIVE | junk: KEEP
- rationale: Roth's Lemma 2 (the Hasse-derivative determinant of a nonzero integer polynomial factors as U(x_1..x_{p-1}) V(x_p) with degree bounds) is absent from mathlib and is a named step of Roth's theorem, but it is a highly specialised auxiliary of one proof that can only land after five unlanded API PRs (MvPolynomial.hasseDeriv, genWronskian and Lemma 1, tensor-rank decomposition, MvPolynomial Gauss lemma, det degree bound), and its natural generalisation (UFD or CharZero domain, no Finite) is not a single mechanical edit; whether mathlib wants Roth-proof internals is a policy call.
- action: Keep in project (sole caller Roth.index_le_lem6, Roth/Theta.lean:571); decide whether a Roth-theorem development goes to Mathlib/NumberTheory/DiophantineApproximation/ (then upstream this as part of a final Roth PR series after its dependencies) or stays downstream; if upstreamed, restate over a UFD R with CharZero and drop [Finite τ].
- Type: `∀ {τ : Type u_1} [Finite τ] {P : MvPolynomial (Option τ) ℤ}, P ≠ 0 → ∀ {r : Option τ → ℕ}, (∀ j, degreeOf j P ≤ r j) → ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧ ∃ D : Fin l → (τ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧ (∀ j, degreeOf j U ≤ l * r (some j)) ∧ V.natDegree ≤ l * r none ∧ (Matrix.of fun μ ν ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single no
- What: Roth's Lemma 2: for a nonzero integer polynomial `P(x_τ, y)` with partial degrees `≤ r`, there are `1 ≤ l ≤ r_y + 1` and Hasse operators `Δ_{D μ}` in the `x_τ` variables of orders `≤ μ` such that `F = det(Δ_{D μ} Δ_y^{(ν)} P)_{μ,ν<l}` equals `U(x_τ) V(y)` with `U, V` nonzero integral, `deg_{x_j} U ≤ l r_j`, `deg V ≤ l r_y`.
- Hypotheses: `[Finite τ]` (needed by the private helper; evidence (1)); `hP : P ≠ 0` (needed: for `P = 0` the determinant is 0 but `U, V ≠ 0`); `hr` (all components used: `hr none` for `l ≤ r none + 1`, all for the degree bounds).
- Uses from project: `Roth.exists_rat_factors_det_hasseDeriv_aux` (private), `Roth.exists_int_factors`, `Roth.degreeOf_rename_mul_aeval`, `Roth.degreeOf_none_rename_mul_aeval`, `Roth.degreeOf_det_hasseDeriv_le`, `MvPolynomial.hasseDeriv` (project def)
- Used by: `Roth.index_le_lem6` (Roth/Theta.lean:571, `obtain ⟨l, hl, hl', D, hD, U, V, hU, hV, hUd, hVd, hF⟩ := exists_det_eq_mul hR.1 hR.2.1`); mentioned in module docstring Separation.lean:37. No other uses (`grep -rn exists_det_eq_mul Roth/`).

### #179 def Roth.RSet (public, Roth/Theta.lean:56)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: RSet is Yamada/Roth's paper notation R_m(B; r) (nonzero integer polynomials, degree at most r_j in x_j, coefficients at most B), a Roth-proof-specific set; its degree clause is exactly mathlib's MvPolynomial.degreesLE ℤ σ r.toMultiset (compiled) and the rest is R ≠ 0 plus a pointwise coefficient bound, so there is nothing general to upstream.
- action: Do not upstream; keep Roth.RSet in Roth/Theta.lean as the paper's named set (about 20 call sites in Theta.lean and MainLemma.lean, e.g. index_le_Θ, Θ_le_of_forall_index_le, index_det_le, index_le_lem6, sub_mem_RSet); optionally note the degreesLE bridge in the docstring; no call-site changes.
- Type: `{σ : Type*} (B : ℝ) (r : σ → ℕ) : Set (MvPolynomial σ ℤ)`
- What: The set `ℛ_m(B; r)` of nonzero integer polynomials whose degree in each variable `X j` is at most `r j` and whose coefficients all have absolute value at most `B`.
- Hypotheses: none. The section variables `[Fintype σ] [DecidableEq σ]` are not included (the evidence file elaborates `RSet` for a bare `σ`, and `sub_mem_RSet` uses it with no `Fintype`).
- Uses from project: `[]`
- Used by: Roth/Theta.lean: `indexSet` (63), `one_mem_RSet` (73, 75), `indexSet_nonempty` (81), `index_le_Θ` (99), `Θ_le_of_forall_index_le` (125), `indexSet_bddAbove` / `Θ_le_card` / `Θ_mono` / `Θ_equiv` (by destructuring membership), `index_separated_mul_le_aux` (416, 425), `index_det_le` (458), `index_le_lem6` (559); Roth/MainLemma.lean: `sub_mem_RSet` (388–390), `exists_mem_RSet_le_index_aux` (550–560), 

### #180 def Roth.indexSet (public, Roth/Theta.lean:62)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: indexSet is the paper's set of indices ind(R; h/q; r) over R in R_m(B; r) and h coprime to q, whose sSup is Θ_m; it is exactly the Set.image of the index map over RSet B r ×ˢ {h coprime to q} (compiled), a proof-internal object of the Roth/Ridout argument with nothing general to upstream.
- action: Do not upstream; keep Roth.indexSet in Roth/Theta.lean as the carrier of Θ (used only in Theta.lean by Θ, indexSet_nonempty, indexSet_bddAbove, index_le_Θ, Θ_le_of_forall_index_le, Θ_mono, indexSet_comp_subset, Θ_equiv); no call-site changes.
- Type: `{σ : Type*} [Fintype σ] (B : ℝ) (q r : σ → ℕ) : Set ℝ`
- What: The set of real numbers `ind(R; (h_j / q_j)_j; r)` where `R` ranges over `RSet B r` (nonzero integer polynomials with degree in `X j` at most `r j` and coefficients bounded by `B`) and `h : σ → ℤ` over tuples with each `h j` coprime to `q j`. Its supremum is `Θ_m(B; q; r)`.
- Hypotheses: none. Only `[Fintype σ]` is needed (inherited from `Roth.index`); the section variable `[DecidableEq σ]` is not included (evidence (1)).
- Uses from project: `Roth.RSet`, `Roth.index`
- Used by: Roth/Theta.lean only: `Θ` (68, `sSup (indexSet B q r)`), `indexSet_nonempty` (80), `indexSet_bddAbove` (87), `index_le_Θ` (102, via `indexSet_bddAbove` and membership), `Θ_le_of_forall_index_le` (127), `Θ_mono` (136), private `indexSet_comp_subset` (141–142), `Θ_equiv` (162–163). `Θ_nonneg` and `Θ_le_card` destructure membership through `Θ`'s `sSup`. Module docstring at lines 26 and 28. No uses ou

### #181 def Roth.Θ (public, Roth/Theta.lean:68)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: Θ is Ridout/Cassels' Θ_m(B; q; r), the sSup of the project's indexSet (itself a Set.image of Roth.index over RSet B r and h coprime to q); it is one mathlib sSup over that image (compiled), a Roth-proof-specific quantity with nothing general to upstream.
- action: Do not upstream; keep Roth.Θ in Roth/Theta.lean as the paper's Θ_m (consumers Θ_unique_le, Θ_option_le, Θ_lt, lem6Φ in Theta.lean and theta_lt_eta_of_sq_log_bound_aux, exists_auxiliary_polynomial_with_index_gap_aux, main_lemma in MainLemma.lean); optionally document the junk value Θ = 0 for B < 1 in the docstring; no call-site changes.
- Type: `{σ : Type*} [Fintype σ] (B : ℝ) (q r : σ → ℕ) : ℝ` (noncomputable)
- What: `Θ_m(B; q_1, …, q_m; r_1, …, r_m)`, the supremum of the indices `ind(R; (h_j/q_j)_j; r)` over nonzero integer polynomials `R` with `deg_{X_j} R ≤ r_j` and coefficients bounded by `B`, and over `h : σ → ℤ` with each `h_j` coprime to `q_j`.
- Hypotheses: none. Only `[Fintype σ]` is used; the section `[DecidableEq σ]` is not included (evidence (1)).
- Uses from project: `Roth.indexSet` (and through it `Roth.RSet`, `Roth.index`)
- Used by: Roth/Theta.lean: `index_le_Θ` (101), `Θ_nonneg` (107), `Θ_le_card` (114), `Θ_le_of_forall_index_le` (126), `Θ_mono` (135), `Θ_equiv` (160), private `index_unique_le_log_div` (253–258), `Θ_unique_le` (256–257, Lemma 5), `lem6M` (273), `lem6Φ` (276), private `index_separated_mul_le_aux` (443–450), `index_le_lem6` (583–591), `Θ_option_le` (593–599, Lemma 6), `lem7_Φ_bound` (707), private `theta_scale

### #182 theorem Roth.one_mem_RSet (public, Roth/Theta.lean:73)
- verdict: INHERITED-NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: Basic membership lemma (1 ∈ RSet B r for 1 ≤ B) proved by one simp unfolding RSet and evaluating coeff_one; glue about the project-local paper notation RSet, which is NO-composable-from-mathlib, so there is nothing to upstream.
- action: Do not upstream; keep in Roth/Theta.lean next to RSet as its nonemptiness witness (sole caller indexSet_nonempty at Roth/Theta.lean:81); no call-site changes.
- Type: `∀ {σ : Type*} {B : ℝ}, 1 ≤ B → ∀ (r : σ → ℕ), (1 : MvPolynomial σ ℤ) ∈ Roth.RSet B r`
- What: If `1 ≤ B`, the constant polynomial `1` lies in `ℛ_m(B; r)`: it is nonzero, has degree 0 in every variable, and every coefficient is 0 or 1, hence at most `B` in absolute value.
- Hypotheses: `hB : 1 ≤ B`. The section instances `[Fintype σ] [DecidableEq σ]` are omitted (`omit ... in`).
- Uses from project: `Roth.RSet`
- Used by: `Roth.indexSet_nonempty` (Roth/Theta.lean:81). No other uses in `Roth/`.

### #183 theorem Roth.indexSet_nonempty (public, Roth/Theta.lean:80)
- verdict: INHERITED-NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: One-term glue lemma (anonymous constructor with witness 1 from one_mem_RSet, h = 1, isCoprime_one_left, rfl) giving the csSup nonemptiness side condition for the project-local carrier set indexSet, which is NO-composable-from-mathlib; nothing to upstream.
- action: Do not upstream; keep in Roth/Theta.lean as the Nonempty side lemma of indexSet (callers Θ_le_of_forall_index_le at Roth/Theta.lean:127 and Θ_mono at Roth/Theta.lean:136); no call-site changes.
- Type: `∀ {σ : Type*} [Fintype σ] {B : ℝ}, 1 ≤ B → ∀ (q r : σ → ℕ), (Roth.indexSet B q r).Nonempty`
- What: If `1 ≤ B`, the set of indices `ind(R; h/q; r)` (over `R ∈ ℛ_m(B; r)` and `h` coprime to `q`) whose supremum is `Θ_m(B; q; r)` is nonempty. So the supremum is well-defined in the `csSup` sense.
- Hypotheses: `hB : 1 ≤ B` (needed for `1 ∈ RSet B r`). The section instance `[DecidableEq σ]` is omitted (`omit ... in`). `[Fintype σ]` is inherited from `indexSet`.
- Uses from project: `Roth.indexSet`, `Roth.one_mem_RSet` (and through them `Roth.RSet` and `Roth.index`)
- Used by: `Roth.Θ_le_of_forall_index_le` (Roth/Theta.lean:127, `csSup_le (indexSet_nonempty hB q r) ?_`), `Roth.Θ_mono` (Roth/Theta.lean:136, `csSup_le_csSup (indexSet_bddAbove B' q) (indexSet_nonempty hB q r) ?_`). No other uses in `Roth/`.

### #184 theorem Roth.indexSet_bddAbove (public, Roth/Theta.lean:87)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: BddAbove of the project-local indexSet, proved as BddAbove.intro with bound card σ and one call of the project lemma index_le_card; a csSup side condition about a proof-internal set with no mathlib home, and its body is duplicated verbatim in Θ_le_card.
- action: Do not upstream; keep in Roth/Theta.lean (callers index_le_Θ at Theta.lean:102 and Θ_mono at Theta.lean:136); optionally factor the shared body into card_mem_upperBounds_indexSet so indexSet_bddAbove and Θ_le_card (Theta.lean:113) become one-liners (evidence/Roth.indexSet_bddAbove/refactor.lean), and fix the docstring's spurious "if every r j is positive".
- Type: `∀ {σ : Type*} [Fintype σ] (B : ℝ) (q : σ → ℕ) {r : σ → ℕ}, BddAbove (Roth.indexSet B q r)`
- What: The set of indices `ind(R; h/q; r)`, taken over `R ∈ ℛ_m(B; r)` and `h` coprime to `q`, is bounded above by the number of variables `m = card σ`. This is the boundedness half of "the supremum `Θ_m` is well-defined".
- Hypotheses: none. `B` and `q` are arbitrary and `r` is implicit with no positivity. The section's `[DecidableEq σ]` is omitted.
- Uses from project: `Roth.indexSet`, `Roth.RSet` (destructured membership), `Roth.index_le_card`, and `Roth.index` through `indexSet`.
- Used by: `Roth.index_le_Θ` (Roth/Theta.lean:102, `le_csSup (indexSet_bddAbove B q) ...`) and `Roth.Θ_mono` (Roth/Theta.lean:136, `csSup_le_csSup (indexSet_bddAbove B' q) ...`). Nothing else uses it (`grep -rn indexSet_bddAbove Roth/`).

### #185 theorem Roth.index_le_Θ (public, Roth/Theta.lean:99)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: The le_csSup intro lemma for the project-local supremum Θ, proved as one call of mathlib's le_csSup with indexSet_bddAbove and a membership witness (compiled); it is about a Roth-proof-specific quantity, so there is nothing to upstream, but it is the named API that 3 call sites use.
- action: Do not upstream; keep in Roth/Theta.lean as the basic Θ API lemma (callers index_separated_mul_le_aux at Theta.lean:443 and 445, main_lemma at MainLemma.lean:760); no call-site changes.
- Type: `∀ {σ : Type*} [Fintype σ] {B : ℝ} {q r : σ → ℕ} {R : MvPolynomial σ ℤ}, R ∈ RSet B r → ∀ {h : σ → ℤ}, (∀ j, IsCoprime (h j) (q j : ℤ)) → index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ Θ B q r`
- What: Take any `R ∈ ℛ_m(B; r)` and any point `(h_j/q_j)_j` with each `h_j` coprime to `q_j`. The index of `R` at that point, relative to `r`, is at most `Θ_m(B; q; r)`. This is the "a member is at most the supremum" property of `Θ`.
- Hypotheses: `hR : R ∈ RSet B r` and `hh : ∀ j, IsCoprime (h j) (q j)`. Both are needed to build the membership witness. There is no `1 ≤ B` hypothesis, because `le_csSup` needs only `BddAbove`, not `Nonempty`. The section's `[DecidableEq σ]` is omitted.
- Uses from project: `Roth.Θ`, `Roth.indexSet`, `Roth.RSet`, `Roth.index`, `Roth.indexSet_bddAbove`
- Used by: Roth/Theta.lean:443 and 445 (private `index_separated_mul_le_aux`, which feeds Lemma 6, as `hUΘ` and `hVΘ`); Roth/MainLemma.lean:760 (`main_lemma`, `linarith only [hgap, index_le_Θ hW hh]`). Found with `grep -rn index_le_Θ Roth/`.

### #186 theorem Roth.Θ_nonneg (public, Roth/Theta.lean:107)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: The nonnegativity of the project-local supremum Θ, proved as one call of mathlib's Real.sSup_nonneg fed by the project's index_nonneg (compiled); it is about a Roth-proof-specific quantity, so there is nothing to upstream, but it is the paper-facing Θ API lemma (clean.tex 0 ≤ Θ_m) used at Theta.lean:583.
- action: Do not upstream; keep in Roth/Theta.lean next to Θ_le_card as the basic Θ API (caller index_numeric_bound application at Theta.lean:583, used twice there); no call-site changes.
- Type: `∀ {σ : Type*} [Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ}, 0 ≤ Θ B q r`
- What: For every coefficient bound `B`, denominators `q` and weights `r`, the quantity `Θ_m(B; q; r)` (the supremum of the indices `ind(R; h/q; r)` over admissible `R` and coprime numerators `h`) is nonnegative. This is the lower half of the paper's `0 ≤ Θ_m ≤ m`.
- Hypotheses: none (beyond `[Fintype σ]`). No `1 ≤ B`, no positivity of `r`; the section's `[DecidableEq σ]` is omitted.
- Uses from project: `Roth.Θ`, `Roth.indexSet`, `Roth.index`, `Roth.index_nonneg` (and `Roth.RSet` implicitly through the `indexSet` membership pattern)
- Used by: Roth/Theta.lean:583 (`add_nonneg (Θ_nonneg _) (Θ_nonneg _)`, the nonnegativity argument fed to `index_numeric_bound_aux` inside the Lemma 6 proof); also cited in the module docstring at Roth/Theta.lean:33. Found with `grep -rn Θ_nonneg Roth/`; no other file uses it.

### #187 theorem Roth.Θ_le_card (public, Roth/Theta.lean:114)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: The upper bound Θ ≤ card σ for the project-local supremum Θ, proved as one call of mathlib's Real.sSup_le fed by the project's index_le_card (compiled); about a Roth-proof-specific quantity so nothing to upstream, but it is the paper-facing Θ_m ≤ m API lemma used at Theta.lean:939.
- action: Do not upstream; keep in Roth/Theta.lean next to Θ_nonneg (caller theta_lt_of_large_delta_aux at Theta.lean:939); optionally remove the body duplicated with indexSet_bddAbove (Theta.lean:87) by factoring card_mem_upperBounds_indexSet as in evidence/Roth.indexSet_bddAbove/refactor.lean, making Θ_le_card the one-liner Real.sSup_le (card_mem_upperBounds_indexSet B q r) (Nat.cast_nonneg _).
- Type: `∀ {σ : Type*} [Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ}, Θ B q r ≤ ↑(Fintype.card σ)`
- What: For every coefficient bound `B`, denominators `q` and weights `r`, the quantity `Θ_m(B; q; r)` is at most the number `m = card σ` of variables. This is the upper half of the paper's `0 ≤ Θ_m ≤ m`.
- Hypotheses: none (beyond `[Fintype σ]`). No `1 ≤ B`, no positivity of `r`; the section's `[DecidableEq σ]` is omitted.
- Uses from project: `Roth.Θ`, `Roth.indexSet`, `Roth.RSet` (membership pattern), `Roth.index`, `Roth.index_le_card`
- Used by: Roth/Theta.lean:939 (`simpa using Θ_le_card (r := r) q`, inside private `theta_lt_of_large_delta_aux`, the large-δ case of Lemma 7); also named in the module docstring at Roth/Theta.lean:33. Found with `grep -rn Θ_le_card Roth/`; no other file uses it.

### #188 theorem Roth.Θ_le_of_forall_index_le (public, Roth/Theta.lean:124)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: The csSup_le elimination lemma for the project-local supremum Θ, proved as one call of mathlib's csSup_le with indexSet_nonempty and destructuring of indexSet membership (compiled); it is about a Roth-proof-specific quantity, so there is nothing to upstream, but it is the named API that Lemmas 5 and 6 use.
- action: Do not upstream; keep in Roth/Theta.lean as the basic upper-bound API lemma of Θ (callers Θ_unique_le at Theta.lean:258 and Θ_option_le at Theta.lean:599); no call-site changes.
- Type: `∀ {σ : Type*} [Fintype σ] {B : ℝ}, 1 ≤ B → ∀ {q r : σ → ℕ} {c : ℝ}, (∀ R ∈ RSet B r, ∀ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) → index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ c) → Θ B q r ≤ c`
- What: Suppose `B ≥ 1` and `c` bounds the index `ind(R; (h_j/q_j)_j; r)` for every `R ∈ ℛ_m(B; r)` and every `h` with each `h_j` coprime to `q_j`. Then `Θ_m(B; q; r) ≤ c`. This is the "the supremum is the least upper bound" property of `Θ`, the counterpart of `index_le_Θ`.
- Hypotheses: `hB : 1 ≤ B`, which makes `indexSet B q r` nonempty (it contains the index of the constant polynomial `1`). `hc` gives the pointwise bound. The section's `[DecidableEq σ]` is omitted.
- Uses from project: `Roth.Θ`, `Roth.indexSet`, `Roth.RSet`, `Roth.index`, `Roth.indexSet_nonempty`
- Used by: Roth/Theta.lean:258 (`Θ_unique_le`, Lemma 5) and Roth/Theta.lean:599 (`Θ_option_le`, Lemma 6). Found with `grep -rn Θ_le_of_forall_index_le Roth/`. There are no uses outside Theta.lean.

### #189 theorem Roth.Θ_mono (public, Roth/Theta.lean:134)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: Monotonicity in B of the project-local supremum Θ, which is one csSup_le_csSup call on the inclusion indexSet B ⊆ indexSet B' (compiled); the quantity is specific to the Roth proof, so nothing goes upstream, and the hypothesis 1 ≤ B is superfluous (a weakened version without it compiles).
- action: Do not upstream; keep in Roth/Theta.lean, optionally drop hB (proof in evidence Θ_mono') and remove the hM1 argument at the two call sites Theta.lean:758 and Theta.lean:790.
- Type: `∀ {σ : Type*} [Fintype σ] {B B' : ℝ}, 1 ≤ B → B ≤ B' → ∀ (q : σ → ℕ) {r : σ → ℕ}, Θ B q r ≤ Θ B' q r`
- What: If `1 ≤ B ≤ B'`, then `Θ_m(B; q; r) ≤ Θ_m(B'; q; r)`. Raising the coefficient bound enlarges `ℛ_m(B; r)`, which enlarges the set of indices, so it cannot decrease their supremum.
- Hypotheses: `hB : 1 ≤ B` is used only to make `indexSet B q r` nonempty. It is superfluous for the conclusion; see the evidence. `hBB' : B ≤ B'` carries the content. The section's `[DecidableEq σ]` is omitted.
- Uses from project: `Roth.Θ`, `Roth.indexSet`, `Roth.RSet`, `Roth.index`, `Roth.indexSet_bddAbove`, `Roth.indexSet_nonempty`
- Used by: Roth/Theta.lean:758 (in the private lemma that bounds Θ in one variable during the proof of Lemma 7) and Roth/Theta.lean:790 (`theta_prefix_lt_aux`, Lemma 7). Found with `grep -rn Θ_mono Roth/`. Theta.lean:34 is a docstring mention. There are no uses outside Theta.lean.

### #190 lemma Roth.indexSet_comp_subset (private, Roth/Theta.lean:141)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-direction inclusion used twice (with e and e.symm) to prove Θ_equiv; it is about the project-local indexSet, so it does not belong in mathlib, and a helper is warranted because both directions reuse it.
- action: Keep as is in Roth/Theta.lean as the helper for Θ_equiv (Theta.lean:162-163); nothing to upstream.
- Type: `∀ {σ : Type u_1} [Fintype σ] {τ : Type u_2} [Fintype τ] (e : σ ≃ τ) (B : ℝ) (q r : τ → ℕ), indexSet B (q ∘ ⇑e) (r ∘ ⇑e) ⊆ indexSet B q r`
- What: Renaming variables along an equivalence `e : σ ≃ τ` maps the set of indices `{ind(R; h/(q∘e); r∘e)}` over `R ∈ ℛ_σ(B; r∘e)` into the corresponding set for `(q, r)` over `τ`. A witness `(R, h)` is sent to `(rename e R, h ∘ e.symm)`.
- Hypotheses: `e : σ ≃ τ`. Only injectivity is needed for the index, nonzero, degree and coefficient goals. Surjectivity is needed to transport the degree bound to every `j : τ` and the coefficient bound to every exponent `d : τ →₀ ℕ`. Coprimality uses `e.symm`, so a full equivalence is the natural hypothesis. `[
- Uses from project: `Roth.indexSet`, `Roth.RSet` (destructured through `indexSet`), `Roth.index` (through `indexSet`), `Roth.index_rename` (Roth/Index.lean:212)
- Used by: Roth/Theta.lean:162 and Roth/Theta.lean:163, both in `Roth.Θ_equiv`, once with `e` and once with `e.symm`. Found with `grep -rn indexSet_comp_subset Roth/`. There are no other uses.

### #191 theorem Roth.Θ_equiv (public, Roth/Theta.lean:159)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: Renaming invariance of the project-local supremum Θ, proved as congrArg sSup of a set equality built from two applications of the private indexSet_comp_subset (rename e, index_rename); the only general content is reindexing a supremum along an equivalence (mathlib Equiv.iSup_congr / renameEquiv), so nothing goes upstream.
- action: Do not upstream; keep in Roth/Theta.lean as the paper-requested renaming lemma for Θ (single caller Theta.lean:919 in the Lemma 7 transport to Option (Fin (n+1))); no call-site changes.
- Type: `∀ {σ : Type*} [Fintype σ] {τ : Type*} [Fintype τ] (e : σ ≃ τ) (B : ℝ) (q r : τ → ℕ), Θ B (q ∘ e) (r ∘ e) = Θ B q r`
- What: `Θ_m(B; q; r)` does not change when the variables are relabelled by a bijection `e : σ ≃ τ`, with the denominators `q` and weights `r` relabelled along with them.
- Hypotheses: `e : σ ≃ τ` is a genuine bijection, needed for an equality and not just one inequality. `B` is arbitrary, with no `1 ≤ B`. Only `[Fintype σ]` and `[Fintype τ]` are needed; the section's `[DecidableEq σ]` is omitted.
- Uses from project: `Roth.Θ`, `Roth.indexSet`, `Roth.indexSet_comp_subset` (private, Theta.lean:141). The helper in turn uses `Roth.RSet`, `Roth.index` and `Roth.index_rename`.
- Used by: Roth/Theta.lean:919. That is the Lemma 7 proof, which transports from `Fin (n + 2)` to `Option (Fin (n + 1))` via `finSuccEquivLast`, with the rewrite `rw [← Θ_equiv e.symm ...]`. Theta.lean:34 is a module-docstring mention. Nothing outside Theta.lean uses it (`grep -rn Θ_equiv Roth/`).

### #192 lemma Roth.isPrimitive_linear (private, Roth/Theta.lean:167)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private 6-line helper showing q X - h in Z[X] is primitive when h and q are coprime; mathlib has no direct lemma (only Monic.isPrimitive, isPrimitive_iff_content_eq_one and the Irreducible.isPrimitive plus irreducible_C_mul_X_add_C route, which needs the extra hypothesis q ne 0); used once.
- action: Keep as private helper for its single call site Roth/Theta.lean:196 (exists_eq_pow_mul_of_rootMultiplicity); optional cosmetic generalisation to any CommRing with C a * X + C b (compiled in evidence) only if the lemma is ever upstreamed to Mathlib/RingTheory/Polynomial/Content.lean.
- Type: `∀ {h : ℤ} {q : ℕ}, IsCoprime h (q : ℤ) → (Polynomial.C (q : ℤ) * Polynomial.X - Polynomial.C h).IsPrimitive`
- What: If the integers h and q are coprime, the linear integer polynomial q·X − h is primitive, i.e. its only constant divisors in ℤ[X] are units.
- Hypotheses: `hcop : IsCoprime h (q : ℤ)`. No positivity of q is needed (q = 0 forces h to be a unit, still primitive).
- Uses from project: `[]` (only mathlib lemmas)
- Used by: Roth/Theta.lean:196 `exists_eq_pow_mul_of_rootMultiplicity` (as `isPrimitive_pow (isPrimitive_linear hcop) t`, feeding `Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast`) only; `grep -rn isPrimitive_linear Roth/` gives the definition (l.167) and that use. Transitively `pow_rootMultiplicity_le` (Roth/Theta.lean:206, uses it at l.209) and the §5 Lemma 5 chain downstream.

### #193 lemma Roth.isPrimitive_pow (private, Roth/Theta.lean:175)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private 2-line helper saying a power of a primitive polynomial in Z[X] is primitive; a direct Nat.rec over mathlib Polynomial.IsPrimitive.mul, and mathlib has no IsPrimitive.pow or content_pow lemma (checked by grep and loogle); used once.
- action: Keep as private helper for its single call site Roth/Theta.lean:196 (exists_eq_pow_mul_of_rootMultiplicity); if ever upstreamed, the NormalizedGCDMonoid form (compiled in evidence) belongs next to IsPrimitive.mul in Mathlib/RingTheory/Polynomial/Content.lean.
- Type: `∀ {p : Polynomial ℤ}, p.IsPrimitive → ∀ (t : ℕ), (p ^ t).IsPrimitive`
- What: Every natural power of a primitive integer polynomial is primitive (the t-fold form of Gauss's lemma on products).
- Hypotheses: `hp : p.IsPrimitive`; `t : ℕ` explicit. No hypothesis is superfluous; the base ring ℤ is more specific than needed (any `CommRing` with `NormalizedGCDMonoid` works, see Evidence).
- Uses from project: `[]` (only mathlib: `Polynomial.isPrimitive_one`, `Polynomial.IsPrimitive.mul`, `pow_succ`)
- Used by: Roth/Theta.lean:196 `exists_eq_pow_mul_of_rootMultiplicity` (as `isPrimitive_pow (isPrimitive_linear hcop) t`, the primitivity input to `Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast`) only; `grep -rn isPrimitive_pow Roth/` gives the definition (l.175) and that use. Transitively `pow_rootMultiplicity_le` (Roth/Theta.lean:206) and the §5 Lemma 5 chain.

### #194 theorem Roth.exists_eq_pow_mul_of_rootMultiplicity (public, Roth/Theta.lean:184)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Gauss-lemma consequence that (qX - h)^t divides R in Z[X] when h/q (coprime) is a root of multiplicity t over Q; mathlib has the pieces (IsPrimitive.dvd_of_fraction_map_dvd_fraction_map, pow_rootMultiplicity_dvd, num_den_reduced) but no such lemma, and the compiled general form over any normalized-GCD domain with fraction field (IsRelPrime, q ne 0, divisibility conclusion) is a natural multiplicity strengthening of mathlib's rational root theorem.
- action: Upstream the compiled general form pow_rootMultiplicity_dvd_of_isRelPrime (plus isPrimitive_C_mul_X_sub_C and a num/den corollary) to Mathlib/RingTheory/Polynomial/GaussLemma.lean; locally keep the lemma (sole caller Roth/Theta.lean:209 pow_rootMultiplicity_le) or restate it as a one-line corollary once upstreamed.
- Type: `∀ {R : Polynomial ℤ} {h : ℤ} {q : ℕ}, 0 < q → IsCoprime h (q : ℤ) → ∃ Q : Polynomial ℤ, R = (C (q : ℤ) * X - C h) ^ rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ)) * Q`
- What: If `h` and `q > 0` are coprime and `t` is the multiplicity of `h/q` as a root of `R` over ℚ, then `(qX − h)^t` divides `R` in ℤ[X].
- Hypotheses: `hq : 0 < q` (only `q ≠ 0` is used); `hcop : IsCoprime h q` (only relative primality is used). `R` need not be nonzero (for `R = 0` the multiplicity is 0).
- Uses from project: `Roth.isPrimitive_linear` (private, Theta.lean:167), `Roth.isPrimitive_pow` (private, Theta.lean:175).
- Used by: Roth/Theta.lean:209 (`pow_rootMultiplicity_le`, the leading-coefficient bound of Lemma 5). `grep -rn exists_eq_pow_mul_of_rootMultiplicity Roth/` gives only the definition and this use. Transitively used by `index_unique_le_log_div` (Theta.lean:245) and the Lemma 5 chain.

### #195 theorem Roth.pow_rootMultiplicity_le (public, Roth/Theta.lean:206)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Multiplicity form of the rational root theorem part 2 (den^mult divides the leading coefficient) packaged as a real bound; mathlib has only den_dvd_of_is_root (mult 1), and the compiled divisibility form over any normalized-GCD domain (q^mult divides leadingCoeff, IsRelPrime, q ne 0, no p ne 0) gives the Roth bound in 4 lines.
- action: Upstream pow_rootMultiplicity_dvd_leadingCoeff (and its den/num UFD corollary) in the same PR as the parent pow_rootMultiplicity_dvd_of_isRelPrime to Mathlib/RingTheory/Polynomial/RationalRoot.lean or GaussLemma.lean; locally keep the real bound (sole caller Roth/Theta.lean:245 index_unique_le_log_div), re-proved as a corollary once upstreamed.
- Type: `∀ {R : Polynomial ℤ}, R ≠ 0 → ∀ {h : ℤ} {q : ℕ}, 0 < q → IsCoprime h (q : ℤ) → ∀ {B : ℝ}, |(R.leadingCoeff : ℝ)| ≤ B → (q : ℝ) ^ rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ)) ≤ B`
- What: If `R ∈ ℤ[X]` is nonzero with `|lc(R)| ≤ B`, and `h/q` (coprime, `q > 0`) is a root of `R` of multiplicity `t` over ℚ, then `q^t ≤ B`.
- Hypotheses: `hR : R ≠ 0` (needed: for `R = 0`, `t = 0` and `1 ≤ B` fails at `B = 0`); `hq : 0 < q` (only `q ≠ 0` used); `hcop : IsCoprime h q` (only relative primality used); `hB` the leading-coefficient bound.
- Uses from project: `Roth.exists_eq_pow_mul_of_rootMultiplicity` (Theta.lean:184).
- Used by: Roth/Theta.lean:245 (`index_unique_le_log_div`, private; the one-variable case of Lemma 5). `grep -rn pow_rootMultiplicity_le Roth/` gives only the definition and this use.

### #196 lemma Roth.index_unique_le_log_div (private, Roth/Theta.lean:223)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private 22-line single-variable step of Lemma 5 converting q^t ≤ B (pow_rootMultiplicity_le) into ind ≤ log B / (r log q) via index_unique and a Q-to-R rootMultiplicity transfer; about the project-local index, used once.
- action: Keep as private helper for its single call site Roth/Theta.lean:259 (Θ_unique_le); nothing upstream.
- Type: `∀ {σ : Type u_1} [Fintype σ] [Unique σ] {B : ℝ} {q r : σ → ℕ}, 1 < q default → ∀ {R : MvPolynomial σ ℤ}, R ≠ 0 → |((uniqueAlgEquiv ℤ σ R).leadingCoeff : ℝ)| ≤ B → ∀ {h : σ → ℤ}, IsCoprime (h default) (q default : ℤ) → index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ Real.log B / (r default * Real.log (q default))`
- What: In one variable, if `R ∈ ℤ[X]` is nonzero with `|lc(R)| ≤ B`, and `h/q` is in lowest terms with `q > 1`, then `ind(R; h/q; r) ≤ log B / (r log q)`. This is the per-polynomial bound behind Lemma 5.
- Hypotheses: `hq : 1 < q default` is needed for `log q > 0` and, through `Nat.zero_lt_of_lt`, for `0 < q`. `hR : R ≠ 0` is needed by `index_unique` and `pow_rootMultiplicity_le`. `hRB` bounds only the leading coefficient of the one-variable polynomial, which is weaker than membership in `RSet`. `hh` gives coprim
- Uses from project: `Roth.index`, `Roth.index_unique`, `Roth.pow_rootMultiplicity_le`, `MvPolynomial.coeff_uniqueAlgEquiv` (mathlib), `MvPolynomial.uniqueAlgEquiv` (mathlib). The project identifiers are `index`, `index_unique` and `pow_rootMultiplicity_le`.
- Used by: only Roth/Theta.lean:259, in `Roth.Θ_unique_le` (Lemma 5), through `Θ_le_of_forall_index_le`. `grep -rn index_unique_le_log_div Roth/` returns the definition (l.223) and that one use.

### #197 theorem Roth.Θ_unique_le (public, Roth/Theta.lean:256)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: Lemma 5 of the source (Θ_1(B; q; r) ≤ log B / (r log q)) is a two-call composition of the project's Θ_le_of_forall_index_le and private index_unique_le_log_div about the Roth-proof-specific supremum Θ; hypotheses are essential (1 ≤ B compiled necessary), and the reusable arithmetic core (q^t ≤ lc) lives in pow_rootMultiplicity_le, assessed separately.
- action: Do not upstream; keep in Roth/Theta.lean as the paper's Lemma 5 (callers theta_scaled_unique_le_aux at Theta.lean:759 and theta_lt_base_aux at Theta.lean:822); no call-site changes.
- Type: `∀ {σ : Type*} [Fintype σ] [Unique σ] {B : ℝ}, 1 ≤ B → ∀ {q : σ → ℕ}, 1 < q default → ∀ {r : σ → ℕ}, Θ B q r ≤ Real.log B / (↑(r default) * Real.log ↑(q default))`
- What: Lemma 5 of the source. In one variable, if `q > 1` and `B ≥ 1`, the supremum `Θ_1(B; q; r)` of indices of nonzero integer polynomials with degree at most `r` and coefficients bounded by `B`, taken at rational points `h/q` with `gcd(h, q) = 1`, is at most `log B / (r log q)`.
- Hypotheses: `1 ≤ B` (needed for nonemptiness in `csSup_le`, and genuinely necessary, see Evidence (1)); `1 < q default` (needed so that `log q > 0`); `[Unique σ]` (the one-variable case); `[Fintype σ]` (needed by `Θ`). The section's `[DecidableEq σ]` is omitted. No positivity of `r` is assumed: when `r = 0` the
- Uses from project: `Roth.Θ`, `Roth.Θ_le_of_forall_index_le`, `Roth.index_unique_le_log_div` (private), `Roth.RSet` (membership projection `hR.1`, `hR.2.2`), `Roth.coeff_uniqueAlgEquiv` (in `simpa only`), `Roth.uniqueAlgEquiv` (via the helper's statement), `Roth.index`.
- Used by: Roth/Theta.lean:759 (inside private `theta_scaled_unique_le_aux`, the one-variable term of Lemma 6/7's Φ bound); Roth/Theta.lean:822 (inside private `theta_lt_base_aux`, the `m = 1` base case of Lemma 7); module docstring Roth/Theta.lean:35. Found with `grep -rn Θ_unique_le Roth/`; no other file uses it.

### #198 def Roth.lem6M (public, Roth/Theta.lean:270)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: lem6M is the ad hoc constant M = (r1+1)^(pl) l! B^l 2^(p l r1) from the proof of Lemma 6 (clean.tex eq. 16); it is a one-line real-arithmetic expression (ring-equal to l! * ((r1+1)^p B 2^(p r1))^l, compiled), with no literature or mathlib identity, so nothing to upstream.
- action: Do not upstream; keep Roth.lem6M in Roth/Theta.lean as the shared name for the Lemma 6/7 constant (used by one_le_lem6M, lem6M_lt, index_det_le, index_le_lem6, Θ_option_le, theta_phi_lt_aux); no call-site changes.
- Type: `(p r₁ : ℕ) (B : ℝ) (l : ℕ) : ℝ`
- What: The constant `M = (r₁ + 1)^{p l} · l! · B^l · 2^{p l r₁}` of Lemma 6. It bounds the coefficients of the generalised Wronskian determinant `F` built from `R ∈ RSet B r`.
- Hypotheses: none. It is declared in `section Lemma6`, but it uses none of the section variables (`τ`, `[Fintype τ]`, `[DecidableEq τ]`).
- Uses from project: `[]`
- Used by: Roth/Theta.lean only:

### #199 def Roth.lem6Φ (public, Roth/Theta.lean:275)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: lem6Φ is the proof-internal quantity Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q_1..q_{p-1}; l r_1..l r_{p-1}) of Lemma 6 (clean.tex eq. 15); it is a one-line sum of two project Θ terms (rfl, compiled), and Θ itself is NO-composable, so there is nothing to upstream.
- action: Do not upstream; keep Roth.lem6Φ in Roth/Theta.lean as the paper's Φ shared by index_separated_mul_le_aux, index_det_le, index_le_lem6, Θ_option_le and theta_lt_succ_aux; no call-site changes.
- Type: `{τ : Type*} [Fintype τ] (q r : Option τ → ℕ) (M : ℝ) (l : ℕ) : ℝ`
- What: The quantity `Φ` of Lemma 6. It is `Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q_1, …, q_{p-1}; l r_1, …, l r_{p-1})`. The variables are indexed by `Option τ`, and the distinguished last variable `p` is `none`.
- Hypotheses: `[Fintype τ]`, which `Θ` requires. The section variable `[DecidableEq τ]` is not taken.
- Uses from project: `Roth.Θ`
- Used by: Roth/Theta.lean only:

### #200 theorem Roth.one_le_lem6M (public, Roth/Theta.lean:279)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: The fact 1 <= M for the project-local Lemma 6 constant lem6M (given 1 <= B) is three applications of mathlib's one_le_mul_of_one_le_of_one_le to four one_le_pow0 or factorial facts (compiled); it concerns a Roth-proof-specific number, so there is nothing for mathlib.
- action: Do not upstream; keep Roth.one_le_lem6M in Roth/Theta.lean as the API lemma for lem6M (sole caller private theta_phi_lt_aux at Theta.lean:866, which feeds hM1 to Θ_mono-based bounds); no call-site changes.
- Type: `(p r₁ : ℕ) {B : ℝ} (hB : 1 ≤ B) (l : ℕ) : 1 ≤ lem6M p r₁ B l`
- What: If `B ≥ 1`, then the Lemma 6 constant `M = (r₁+1)^{pl} · l! · B^l · 2^{plr₁}` is at least `1`.
- Hypotheses: `hB : 1 ≤ B`. This is necessary (evidence (2), (3)).
- Uses from project: `Roth.lem6M`
- Used by: `Roth.theta_phi_lt_aux` (private, Roth/Theta.lean:866). There it supplies `hM1`, which is passed on at lines 884 and 888 to the Lemma 7 helpers that call `Θ_mono hM1 hM`. It is not used in any other file.

### #201 theorem Roth.floor_sq_div_two_le_sum (public, Roth/Theta.lean:289)
- verdict: SKIP | cost: n/a | junk: REMOVE
- rationale: Dead code since commit 9bf5ca8 (the strengthened positive-part bound mul_sq_div_three_le_sum_max_of_pos_aux re-derives a sharper (θr)²/3 bound inline and no longer calls it); its content is a 4-step consequence of mathlib's Finset.sum_range_id_mul_two plus Nat.floor_le, so Step 8 REMOVE fires the Step 9a pre-filter.
- action: Delete Roth.floor_sq_div_two_le_sum from Roth/Theta.lean:287-296 (no call sites; delete together with the equally dead sq_div_three_lt_floor_sq_div_two at l.298-302 after checking it too), or make it private if blueprint fidelity to the source's first FACT is wanted; needs user sign-off.
- Type: `∀ {a : ℝ}, 0 ≤ a → (⌊a⌋₊ : ℝ) ^ 2 / 2 ≤ ∑ ν ∈ Finset.range (⌊a⌋₊ + 1), (a - ν)`
- What: For real `a ≥ 0`, `∑_{0 ≤ ν ≤ ⌊a⌋} (a − ν) ≥ ⌊a⌋²/2`. This is the first FACT in the proof of Lemma 6 (§5, clean.tex l.857–875).
- Hypotheses: `ha : 0 ≤ a`, used for `Nat.floor_le`. It is needed: for negative `a`, `⌊a⌋₊ = 0` and the right side is `a < 0`.
- Uses from project: `[]`
- Used by: unused in project. `grep -rn floor_sq_div_two_le_sum Roth Roth.lean` finds only the declaration at Roth/Theta.lean:289. `git show 9bf5ca8` shows that the old proof of the Θ positive-part bound called it (together with `sq_div_three_lt_floor_sq_div_two`). That commit ("Strengthen Theta positive-part sum bound") replaced the call with the inline `hbound` in the private `mul_sq_div_three_le_sum_max_o

### #202 theorem Roth.sq_div_three_lt_floor_sq_div_two (public, Roth/Theta.lean:300)
- verdict: SKIP | cost: n/a | junk: REMOVE
- rationale: Dead code since commit 9bf5ca8 (its only caller, the old Theta positive-part bound, was replaced by the inline sharper bound in mul_sq_div_three_le_sum_max_of_pos_aux); it is a one-tactic nlinarith consequence of mathlib's Nat.lt_floor_add_one, so Step 8 REMOVE fires the Step 9a pre-filter.
- action: Delete Roth.sq_div_three_lt_floor_sq_div_two from Roth/Theta.lean:298-302 together with the equally dead floor_sq_div_two_le_sum (l.287-296), or make it private if blueprint fidelity to the source's second FACT is wanted; needs user sign-off.
- Type: `∀ {a : ℝ}, 10 < a → a ^ 2 / 3 < (⌊a⌋₊ : ℝ) ^ 2 / 2`
- What: For real `a > 10`, `a²/3 < ⌊a⌋²/2`. This is the second FACT in the proof of Lemma 6 (§5, clean.tex l.878–889).
- Hypotheses: `ha : 10 < a`. Some threshold is needed: for `a` in `[1, 2)`, `⌊a⌋²/2 = 1/2` while `a²/3` can reach about `4/3`. The constant 10 matches the source, but it is not sharp.
- Uses from project: `[]`
- Used by: unused in project. `grep -rn sq_div_three_lt_floor_sq_div_two Roth Roth.lean` finds only the declaration at Roth/Theta.lean:300. The diff of `git show 9bf5ca8` removes its last call, `(div_le_div_iff_of_pos_right hrp').2 (sq_div_three_lt_floor_sq_div_two hθ).le`.

### #203 lemma Roth.mul_div_two_le_sum_max_aux (private, Roth/Theta.lean:304)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private case lemma of min_le_sum_max (case l ≤ θr) giving lθ/2 ≤ ∑_{ν<l} max(0, θ - ν/r) via the Gauss sum; used twice in Theta.lean, nothing in mathlib states it, too specific to upstream.
- action: Keep as private helper for its call sites Roth/Theta.lean:354 (mul_sq_div_three_le_sum_max_aux) and Roth/Theta.lean:369 (min_le_sum_max); no change needed.
- Type: `∀ {θ r : ℝ} {l : ℕ}, (l : ℝ) ≤ θ * r → (l : ℝ) * θ / 2 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r)`
- What: If l ≤ θ r, then the truncated arithmetic-progression sum ∑_{ν<l} max(0, θ - ν/r) is at least lθ/2. This is the case "θ r_p ≥ l" of the combined estimate in §5, proof of Lemma 6 of the source (the sum has all l terms, average term ≥ θ/2).
- Hypotheses: `hl : (l : ℝ) ≤ θ * r`. No sign hypotheses on θ or r (handled by case split: θ ≤ 0 is trivial, θ > 0 forces r > 0 when l > 0).
- Uses from project: `[]` (only mathlib lemmas)
- Used by: Roth/Theta.lean only (`grep -rn mul_div_two_le_sum_max_aux Roth/`): `mul_sq_div_three_le_sum_max_aux` (private, l.343; use at l.354, boundary case θr = l) and `min_le_sum_max` (public, l.362; use at l.369, case l ≤ θr). Transitively via `min_le_sum_max`: `index_le_lem6` (Roth/Theta.lean:556, use at l.586) and its downstream (Lemma 6).

### #204 lemma Roth.mul_sq_div_three_le_sum_max_of_pos_aux (private, Roth/Theta.lean:322)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private case lemma (θr < l, r > 0) of min_le_sum_max giving rθ²/3 ≤ ∑_{ν<l} max(0, θ - ν/r) via an inline floor/Gauss-sum bound valid for all θr ≥ 0; single call site, nothing in mathlib states it, too specific to upstream.
- action: Keep as private helper for its call site Roth/Theta.lean:353 (mul_sq_div_three_le_sum_max_aux); separately remove the now-dead public floor_sq_div_two_le_sum and sq_div_three_lt_floor_sq_div_two (Roth/Theta.lean:289, :300), whose role this lemma's inline hbound took over.
- Type: `∀ {θ r : ℝ}, 0 < r → 0 ≤ θ → ∀ {l : ℕ}, θ * r < (l : ℝ) → r * θ ^ 2 / 3 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r)`
- What: If r > 0, θ ≥ 0 and θ r < l, then the truncated arithmetic-progression sum ∑_{ν<l} max(0, θ - ν/r) is at least r θ²/3. This is the case "θ r_p < l" of the combined estimate in §5, proof of Lemma 6 of the source, but without the source's assumption θ r_p > 10: the inner bound (θr)²/3 ≤ ∑_{ν ≤ ⌊θr⌋} (θr - ν) is proved for every θr ≥ 0, replacing the source's two FACTs (⌊a⌋²/2 ≤ ∑ and a²/3 < ⌊a⌋²/2 for a > 10).
- Hypotheses: `hr : 0 < r` (needed for the division by r; the r ≤ 0 case is handled trivially by the caller), `hθ : 0 ≤ θ` (necessary: for θ < 0 < r the right side is 0 and the left side is positive), `hl : θ * r < l` (strict is needed for ⌊θr⌋ + 1 ≤ l; the equality case θr = l is handled by the caller via `mul_d
- Uses from project: `[]` (only mathlib lemmas)
- Used by: Roth/Theta.lean only (`grep -rn mul_sq_div_three_le_sum_max_of_pos_aux Roth/`): `mul_sq_div_three_le_sum_max_aux` (private, l.347; use at l.353, case θr < l). Transitively: `min_le_sum_max` (public, l.362; use at l.370), then `index_le_lem6` (Roth/Theta.lean:586) and Lemma 6 downstream.

### #205 lemma Roth.mul_sq_div_three_le_sum_max_aux (private, Roth/Theta.lean:347)
- verdict: SKIP | cost: n/a | junk: INLINE
- rationale: Private 9-line case-dispatch lemma (r ≤ 0 / θr < l / θr = l) for the rθ²/3 branch of min_le_sum_max; its sole caller passes a strict θ rp < l so the equality branch is dead, and inlining into min_le_sum_max compiles (evidence file).
- action: Inline into min_le_sum_max (Roth/Theta.lean:370) as an rp = 0 split plus a direct call to mul_sq_div_three_le_sum_max_of_pos_aux, delete this lemma (removing the mul_div_two_le_sum_max_aux use at Roth/Theta.lean:354); proof in evidence/Roth.mul_sq_div_three_le_sum_max_aux/inline_into_min_le_sum_max.lean.
- Type: `∀ {θ r : ℝ}, 0 ≤ θ → ∀ {l : ℕ}, θ * r ≤ (l : ℝ) → r * θ ^ 2 / 3 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r)`
- What: If θ ≥ 0 and θ r ≤ l, then the truncated arithmetic-progression sum ∑_{ν<l} max(0, θ - ν/r) is at least r θ²/3. This is the case "θ r_p < l" of the combined estimate in §5, proof of Lemma 6 of the source ("∑_{ν<l} max(0, θ - ν/r_p) ≥ min(lθ/2, r_p θ²/3)"), extended to the closed case θ r ≤ l and to arbitrary real r, with no θ r_p > 10 assumption.
- Hypotheses: `hθ : 0 ≤ θ` (necessary: for θ < 0 < r with l = 0 the right side is 0 and the left side is positive), `hl : θ * r ≤ l` (closed form; the only caller actually has the strict form). No sign hypothesis on r (case r ≤ 0 is trivial).
- Uses from project: `Roth.mul_sq_div_three_le_sum_max_of_pos_aux` (private, Roth/Theta.lean:322), `Roth.mul_div_two_le_sum_max_aux` (private, Roth/Theta.lean:304)
- Used by: Roth/Theta.lean only (`grep -rn mul_sq_div_three_le_sum_max_aux Roth/`): `min_le_sum_max` (public, l.362; single use at l.370, case θ ≤ 0 excluded and l > θ rp strict, passed as `hl.le`). Transitively: `index_le_lem6` (Roth/Theta.lean:556, use at l.586) and Lemma 6 downstream.

### #206 theorem Roth.min_le_sum_max (public, Roth/Theta.lean:362)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: The combined numeric estimate of Roth's Lemma 6 (min(lθ/2, r θ²/3) ≤ ∑_{ν<l} max(0, θ - ν/r)); it has no standing in the literature and no counterpart in mathlib, and it is not a ≤3-call composition (it needs the Gauss sum plus a floor argument), so neither a YES nor a NO bucket fits; recommended resolution is to keep it in the project.
- action: Keep in Roth/Theta.lean as a project lemma (single caller Roth.index_le_lem6, Roth/Theta.lean:586); optionally generalise rp : ℕ to r : ℝ (same proof, compiled in evidence/Roth.min_le_sum_max/generalise_real_r.lean) and fix the docstring's leading "If θ r_p > 10" since the Lean statement has no such hypothesis.
- Type: `∀ {θ : ℝ} {rp : ℕ} (l : ℕ), min (↑l * θ / 2) (↑rp * θ ^ 2 / 3) ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ↑ν / ↑rp)`
- What: For all real θ and natural l, r_p: the sum of positive parts ∑_{ν<l} max(0, θ - ν/r_p) is at least min(lθ/2, r_p θ²/3). This is the "Combining everything" bound of clean.tex §5, proof of Lemma 6 (l.880–910), stated without the source's hypotheses θ > 0 and θ r_p > 10.
- Hypotheses: none (θ, r_p, l arbitrary). The source's assumptions θ > 0 and θ r_p > 10 are not needed.
- Uses from project: `Roth.mul_div_two_le_sum_max_aux` (private, Roth/Theta.lean:304), `Roth.mul_sq_div_three_le_sum_max_aux` (private, Roth/Theta.lean:347); transitively `Roth.mul_sq_div_three_le_sum_max_of_pos_aux` (private, l.322).
- Used by: `Roth.index_le_lem6` (Roth/Theta.lean:586). `grep -rn min_le_sum_max Roth/` gives only l.362 and l.586 (other hits are the `_aux` helpers' names).

### #207 theorem Roth.sum_max_sub_le_index_det (public, Roth/Theta.lean:376)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: The Lemma 6 step ind(F) ≥ ∑_{ν<l} max(0, ind R - ν/r_p) - lδ for the generalised-Wronskian determinant F of Roth's proof; it is a 30-line combination of four project index lemmas (le_index_sum, index_prod, index_C_mul, index_sub_weight_le_index_hasseDeriv) about the project-only Roth.index, has no standalone counterpart in the literature or mathlib, and is not a ≤3-call composition, so no YES or NO bucket fits cleanly; recommended resolution is to keep it in the project.
- action: Keep in Roth/Theta.lean (single caller Roth.index_le_lem6 at Roth/Theta.lean:576); optionally replace hD and hδ by the single hypothesis ∀ μ, weight (r ∘ some) (D μ) ≤ δ (same proof, original recovered in one line, compiled in evidence/Roth.sum_max_sub_le_index_det/restate.lean); do not upstream.
- Type: `{τ : Type*} [Fintype τ] {R : MvPolynomial (Option τ) ℝ} {l : ℕ} (D : Fin l → (τ →₀ ℕ)) (hD : ∀ μ, (D μ).degree ≤ μ) (hdet : (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none ν) R).det ≠ 0) (α : Option τ → ℝ) {r : Option τ → ℕ} (hr : ∀ j, 0 < r j) {δ : ℝ} (hδ : ∀ d : τ →₀ ℕ, d.degree ≤ l - 1 → weight (r ∘ some) d ≤ δ) : ∑ ν ∈ Finset.range l, max 0 (index R α r - ν
- What: For a real polynomial `R` in variables `Option τ` (`none` playing the role of `x_p`), the determinant `F = det(Δ_{D_μ} ∂_{x_p}^{(ν)} R)_{μ,ν<l}` (Hasse derivatives) has Roth index at least `∑_{ν<l} max(0, ind R - ν/r_p) - lδ`, provided `F ≠ 0`, `D_μ` has total degree `≤ μ`, and `δ` bounds the weights of all multi-indices of degree `≤ l - 1`. This is the displayed conclusion "We have proved ind(F) ≥ …" of clean.tex §5, proof of Lemma 6 (l.814–840).
- Hypotheses: `hD` and `hδ` (only used through `weight (r ∘ some) (D μ) ≤ δ`, see evidence); `hdet` (needed: Lean has `index 0 = 0`); `hr` (needed by `index_prod`).
- Uses from project: `Roth.index`, `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.weight`, `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.weight_add`, `Roth.weight_mapDomain`, `Roth.weight_single`, `Roth.index_nonneg`, `Roth.weight_nonneg`, `Roth.le_index_sum`, `Roth.index_C_mul`, `Roth.index_prod`.
- Used by: `Roth.index_le_lem6` (Roth/Theta.lean:576, `have hlower := sum_max_sub_le_index_det D hD (mapped_det_ne_zero_aux hU hV hF) α hr0 ...`). No other occurrence in `Roth/` or `Roth.lean`.

### #208 lemma Roth.index_separated_mul_le_aux (private, Roth/Theta.lean:414)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private Step-3 helper of index_det_le bounding the index of U(x_1..x_{p-1}) V(x_p) by l Phi via index_mul, index_rename, index_mul_left_weights and index_le_Θ; built on project-only notions (Roth index, RSet, Θ, lem6Φ) absent from mathlib.
- action: Keep as private helper for its single call site Roth/Theta.lean:491 (index_det_le); no change needed.
- Type: `∀ {τ : Type*} [Fintype τ] {r : Option τ → ℕ}, (∀ j, 0 < r j) → ∀ {q : Option τ → ℕ} {h : Option τ → ℤ}, (∀ j, IsCoprime (h j) (q j : ℤ)) → ∀ {M : ℝ} {l : ℕ}, 0 < l → ∀ {U : MvPolynomial τ ℤ}, U ∈ RSet M (fun j ↦ l * r (some j)) → ∀ {V : Polynomial ℤ}, V ≠ 0 → V.natDegree ≤ l * r none → (∀ b, |(V.coeff b : ℝ)| ≤ M) → index (map (Int.castRingHom ℝ) (rename some U * Polynomial.aeval (X none : MvPoly
- What: For a product F = U(x_1, …, x_{p-1}) · V(x_p) of an integer polynomial U ∈ ℛ_{p-1}(M; l r_1, …, l r_{p-1}) and a nonzero one-variable integer polynomial V of degree ≤ l r_p with coefficients bounded by M, the index of F at the point (h_j/q_j) with weights r is at most l Φ, where Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q_1..q_{p-1}; l r_1..l r_{p-1}). This is the source's Lemma 4-2 (additivity of the index for separated variables) combined with the definition of Θ as a supremum, Step 3 of eq. (17) in
- Hypotheses: `hr0` (positive weights, needed by `index_mul`); `hh` (coprimality, needed by `index_le_Θ`); `hl : 0 < l` (to clear the `/ l` from `index_mul_left_weights`); `hU` membership in RSet; `hV`, `hVd`, `hVc` are the unpacked RSet conditions for V (stated for a `Polynomial ℤ` rather than an `MvPolynomial U
- Uses from project: `Roth.RSet`, `Roth.index`, `Roth.lem6Φ`, `Roth.Θ` (via lem6Φ), `Roth.index_le_Θ`, `Roth.index_mul`, `Roth.index_rename`, `Roth.index_mul_left_weights`, `aeval_X_eq_rename` (Roth/Separation.lean:137), `degreeOf_uniqueAlgEquiv_symm` (Roth/Separation.lean:174), `MvPolynomial.coeff_uniqueAlgEquiv_symm` (Roth/Separation.lean:169)
- Used by: Roth/Theta.lean: `index_det_le` (l.468; `exact index_separated_mul_le_aux hr0 hh hl ⟨hU, hUd, hUc⟩ hV hVd hVc` at l.491). `grep -rn index_separated_mul_le_aux Roth/` returns only the definition (l.414) and this use. Transitively: `index_le_lem6` (l.556, via l.578) and `Θ_option_le` (Lemma 6, l.593), used at l.920 for Lemma 7.

### #209 theorem Roth.index_det_le (public, Roth/Theta.lean:457)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Eq. (17) of the proof of Roth's Lemma 6 (ind F ≤ l Φ for the factored generalised-Wronskian determinant F = U(x_1..x_{p-1}) V(x_p)); a 3-step chain of project lemmas (abs_coeff_det_hasseDeriv_le, coeff_rename_mul_aeval, index_separated_mul_le_aux) about project-only notions (Roth.index, RSet, Θ, lem6Φ, lem6M), with no standalone literature standing, no mathlib counterpart and no ≤3-call mathlib composition, so neither YES nor NO fits; recommended resolution is to keep it in the project.
- action: Keep in Roth/Theta.lean (single caller Roth.index_le_lem6 at Roth/Theta.lean:578); optionally make it private and drop the unused R ≠ 0 part of hR (compiled in evidence/Roth.index_det_le/weaken.lean); do not upstream.
- Type: `{τ : Type*} [Fintype τ] {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j) {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} {B : ℝ} {R : MvPolynomial (Option τ) ℤ} (hR : R ∈ RSet B r) {h : Option τ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) {l : ℕ} (hl : 1 ≤ l) {D : Fin l → (τ →₀ ℕ)} {U : MvPolynomial τ ℤ} {V : Polynomial ℤ} (hU : U ≠ 0) (hV : V ≠ 0) (hUd : ∀ j, degreeOf j U ≤ l * r (some j)) (hVd : V.natD
- What: Let `R ∈ ℛ_p(B; r)` with all `r_j ≤ r₁`, and suppose the generalised Wronskian `F = det(Δ_{D_μ} (1/ν!) ∂^ν_{x_p} R)_{μ,ν<l}` factors as `U(x_1, …, x_{p-1}) V(x_p)` with `U, V ≠ 0`, `deg_{x_j} U ≤ l r_j`, `deg V ≤ l r_p`. Then `ind(F; h/q; r) ≤ l Φ`, where `Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q'; l r')` and `M = (r₁+1)^{pl} l! B^l 2^{p r₁ l}`. Source: clean.tex §5, proof of Lemma 6, eq. (17) (l.734–777).
- Hypotheses: `hr0` (for `index_mul` inside the aux lemma); `hr₁` (uniform degree bound for Lemma 3); `hR` (only the degree and coefficient clauses are used; `R ≠ 0` is superfluous, see evidence); `hh` (coprimality for `index_le_Θ`); `hl` (to clear `/ l`); `hU`, `hV`, `hUd`, `hVd`, `hF` (Lemma 2 output). `[Decida
- Uses from project: `Roth.RSet`, `Roth.index`, `Roth.lem6Φ`, `Roth.lem6M`, `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean), `Roth.abs_coeff_det_hasseDeriv_le` (Roth/CoeffNorm.lean:258), `Roth.coeff_rename_mul_aeval` (Roth/Separation.lean:123), `Roth.index_separated_mul_le_aux` (Roth/Theta.lean:414, private)
- Used by: `Roth.index_le_lem6` (Roth/Theta.lean:578, `have hupper := index_det_le hr0 hr₁ hR hh hl hU hV hUd hVd hF`). No other occurrence in `Roth/` or `Roth.lean`. Transitively feeds `Roth.Θ_option_le` (Lemma 6, l.593).

### #210 lemma Roth.weight_le_delta_aux (private, Roth/Theta.lean:494)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private helper (Step 9a SKIP); it is the real-ratio weight bound used once in index_le_lem6 to feed sum_max_sub_le_index_det, it has real content (about 10 lines), mathlib has no Finsupp.weight-by-degree upper bound, and it is the live replacement for the unused public Roth.weight_le_degree_div.
- action: Keep in Roth/Theta.lean:493-508 (sole call site Roth/Theta.lean:577 in index_le_lem6); optional consolidation, not verified here, is to generalise Roth.weight_le_degree_div (Roth/Box.lean:118) to a real lower bound 0 < c with c at most r j and derive this helper from it with c = r none / delta, or delete weight_le_degree_div as its own report recommends.
- Type: `{τ : Type*} [Fintype τ] {δ : ℝ} (hδ : 0 ≤ δ) {r : Option τ → ℕ} (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {d : τ →₀ ℕ} (hd : d.degree ≤ r none) : Roth.weight (r ∘ some) d ≤ δ`
- What: If every parameter `r (some j)` of the first `p - 1` variables satisfies `r_p ≤ δ r_j` (the source's ratio condition, with `r_p = r none`), then every multi-index `d` in those variables of total degree at most `r_p` has weight `∑ j, d j / r_j ≤ δ`. This is the source's estimate `∑_{j<p} i_j / r_j ≤ w / r_{p-1}`-style step in the proof of Lemma 6, recast with a real ratio `δ`.
- Hypotheses: `hδ : 0 ≤ δ` (needed: with `δ < 0` and `d = 0` the conclusion `0 ≤ δ` fails); `hratio` (the ratio condition, needed for the termwise comparison and also yields `r (some j) > 0` when `r none > 0`); `hd : d.degree ≤ r none`. Section variable `[Fintype τ]` (needed for the finite sum in `weight`); `[Dec
- Uses from project: `Roth.weight` (Roth/Box.lean:71). All other identifiers are mathlib (`Finsupp.degree_eq_zero_iff`, `Finsupp.degree_eq_sum`, `Finset.sum_le_sum`, `Finset.sum_div`, `Finset.sum_mul`, `Nat.cast_sum`, `div_le_div_iff₀`, `div_le_iff₀`, `pos_of_mul_pos_right`, `mul_le_mul_of_nonneg_left`, `Nat.pos_of_ne_zero`, `Nat.eq_zero_of_le_zero`, `Nat.cast_nonneg`).
- Used by: `Roth.index_le_lem6` (Roth/Theta.lean:577), where `fun d hd ↦ weight_le_delta_aux hδ0 hratio (hd.trans (Nat.sub_le_iff_le_add.2 hl'))` discharges the hypothesis `hδ : ∀ d, d.degree ≤ l - 1 → weight (r ∘ some) d ≤ δ` of `Roth.sum_max_sub_le_index_det`. No other uses project-wide (`grep -rn weight_le_delta_aux Roth/`: declaration line 494 and call line 577 only).

### #211 lemma Roth.mapped_det_ne_zero_aux (private, Roth/Theta.lean:511)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private helper (Step 9a SKIP) transporting the integer factorisation F = U(x_tau) V(x_p) of the Lemma 6 determinant to nonvanishing of the real determinant; used once in index_le_lem6, a short composition of mathlib injectivity lemmas, Roth-specific in shape.
- action: Keep at Roth/Theta.lean:510-529 (sole call site Roth/Theta.lean:576 in index_le_lem6); optional golf verified by lean_multi_attempt - replace the last two lines (528-529) by exact (map_ne_zero_iff _ (Polynomial.toMvPolynomial_injective (R := ℤ) none)).2 hV, dropping the use of Roth.aeval_X_eq_rename.
- Type: `{τ : Type*} {R : MvPolynomial (Option τ) ℤ} {l : ℕ} {D : Fin l → (τ →₀ ℕ)} {U : MvPolynomial τ ℤ} {V : Polynomial ℤ} (hU : U ≠ 0) (hV : V ≠ 0) (hF : (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det = rename some U * Polynomial.aeval (X none) V) : (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) (map (In
- What: In the proof of Lemma 6 (source §5), the `l × l` determinant `F = det(Δ_{(D μ, ν)} R)` of Hasse derivatives of the integer polynomial `R` factors as `U(x_1,…,x_{p-1}) · V(x_p)` with `U, V ≠ 0` (from `exists_det_eq_mul`). This lemma concludes that the same determinant built from `R` viewed over `ℝ` is nonzero, which is the hypothesis `hdet` that `sum_max_sub_le_index_det` (the lower bound for `ind F`) requires.
- Hypotheses: `hU : U ≠ 0`, `hV : V ≠ 0` (both needed: either factor zero makes the determinant zero); `hF` the factorisation. Section variables `[Fintype τ] [DecidableEq τ]` are omitted (`omit ... in`), so the lemma holds for arbitrary `τ`. Implicitly uses that `ℤ` and `ℝ` are domains (via `mul_eq_zero` in `MvPo
- Uses from project: `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57), `MvPolynomial.hasseDeriv_map` (Roth/HasseDeriv.lean:134), `Roth.aeval_X_eq_rename` (Roth/Separation.lean:137). All other identifiers are mathlib (`RingHom.map_det`, `Matrix.ext`, `map_eq_zero_iff`, `MvPolynomial.map_injective`, `Int.cast_injective`, `MvPolynomial.rename_injective`, `Option.some_injective`, `mul_eq_zero`, `not_or`, `MvPolynomial.
- Used by: `Roth.index_le_lem6` (Roth/Theta.lean:576), as the `hdet` argument of `Roth.sum_max_sub_le_index_det`. No other uses project-wide (`grep -rn mapped_det_ne_zero_aux Roth/`: declaration line 511 and call line 576 only).

### #212 lemma Roth.index_numeric_bound_aux (private, Roth/Theta.lean:531)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private helper (Step 9a SKIP); it isolates the purely real-arithmetic final step of Lemma 6 (from min(l theta/2, r_p theta^2/3) at most l(Phi+delta) to theta at most 2(Phi+sqrt Phi+sqrt delta)), used once in index_le_lem6, about 17 lines of genuine case analysis that mathlib does not and should not contain.
- action: Keep in Roth/Theta.lean:531-551 (sole call site Roth/Theta.lean:582 in Roth.index_le_lem6); no change needed.
- Type: `{θ Φ δ rp l : ℝ} (hΦ : 0 ≤ Φ) (hδ1 : δ ≤ 1) (hrp : 3 ≤ rp) (hl : 0 < l) (hl' : l ≤ rp + 1) (hmin : min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ l * (Φ + δ)) : θ ≤ 2 * (Φ + √Φ + √δ)`
- What: The numerical conclusion of the source's Lemma 6 (§5). If `Φ ≥ 0`, `δ ≤ 1`, `r_p ≥ 3`, `0 < l ≤ r_p + 1` and `min(lθ/2, r_p θ²/3) ≤ l(Φ + δ)`, then `θ ≤ 2(Φ + Φ^{1/2} + δ^{1/2})`. In the paper this is the closing step "comparing the lower and upper bounds for the index of the Wronskian-type determinant `F`".
- Hypotheses: `hΦ` (needed for `(√Φ)² = Φ` in case 2); `hδ1` (needed for `δ ≤ √δ` in case 1); `hrp` (gives `r_p > 0` and, with `hl'`, `3l ≤ 4r_p`); `hl` (cancelling `l`, and nonnegativity of `Φ+δ`); `hl'` (size comparison). No nonnegativity of `δ` is required because `Real.sqrt` truncates (`Real.sq_sqrt'` with `m
- Uses from project: `[]` (all identifiers are mathlib: `min_le_iff`, `mul_div_assoc`, `mul_le_mul_iff_right₀`, `div_le_iff₀`, `Real.le_sqrt_self_iff`, `Real.sqrt_nonneg`, `mul_le_mul_of_nonneg_right`, `nonneg_of_mul_nonneg_right`, `div_nonneg`, `mul_nonneg`, `sq_nonneg`, `le_of_sq_le_sq`, `le_max_left`, `Real.sq_sqrt'`, `Real.sq_sqrt`; tactics `linarith`, `linear_combination`, `positivity`, `norm_num`).
- Used by: `Roth.index_le_lem6` (Roth/Theta.lean:582), via `apply index_numeric_bound_aux (Φ := Φ) (l := (l : ℝ)) ...`, with `hmin` supplied by `Roth.min_le_sum_max` chained with the lower/upper index bounds `sum_max_sub_le_index_det` and `index_det_le`. No other uses project-wide (`grep -rn index_numeric_bound_aux Roth/`: lines 531 and 582 only).

### #213 theorem Roth.index_le_lem6 (public, Roth/Theta.lean:556)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: The pointwise form of Roth's Lemma 6 (ind(R; h/q; r) ≤ 2(Φ + √Φ + √δ) for some 1 ≤ l ≤ r_p+1, for R ∈ ℛ_p(B; r)); it assembles six project lemmas (exists_det_eq_mul, sum_max_sub_le_index_det, index_det_le, min_le_sum_max and two private aux lemmas) about project-only notions (Roth.index, RSet, Θ, lem6Φ, lem6M), so it has no mathlib counterpart and is not a ≤3-call mathlib composition, while as an internal step of Roth's lemma it has no standalone literature standing; recommended resolution is to keep it in the project.
- action: Keep in Roth/Theta.lean (single caller Roth.Θ_option_le at Roth/Theta.lean:600); optionally drop the unused hypothesis _hq (compiled in evidence/Roth.index_le_lem6/weaken_hq.lean) and update that call site; optionally make it private; do not upstream.
- Type: `{τ : Type*} [Fintype τ] {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) {r : Option τ → ℕ} (hrp : 3 ≤ (r none : ℝ)) (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} (_hq : ∀ j, 0 < q j) {B : ℝ} {R : MvPolynomial (Option τ) ℤ} (hR : R ∈ RSet B r) {h : Option τ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) : ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧ index (map (Int.castRingHom ℝ
- What: Lemma 6 of the source (clean.tex §5, Lemma `roth:lem6`, l.704–) for a single polynomial and point: if `R ∈ ℛ_p(B; r)`, `r_p ≥ 3`, `r_p ≤ δ r_j` for `j < p`, `r_j ≤ r₁`, and `gcd(h_j, q_j) = 1`, then for some `1 ≤ l ≤ r_p + 1`, `ind(R; h/q; r) ≤ 2(Φ + Φ^{1/2} + δ^{1/2})` with `Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q'; l r')`, `M = (r₁+1)^{pl} l! B^l 2^{p r₁ l}`.
- Hypotheses: `hδ0`, `hδ1`, `hrp`, `hratio` (weight comparisons, used for `r j > 0` and the weight-≤-δ bound); `hr₁` (uniform degree bound for Lemma 3 via `index_det_le`); `hR` (Lemma 2 needs `R ≠ 0` and the degree bounds); `hh` (coprimality for `index_le_Θ`); `_hq` (positivity of the `q j`) is **unused** — see e
- Uses from project: `Roth.RSet`, `Roth.index` (Roth/Index.lean:58), `Roth.Θ_nonneg`, `Roth.lem6Φ`, `Roth.lem6M`, `Roth.exists_det_eq_mul` (Roth/Separation.lean:542), `Roth.sum_max_sub_le_index_det` (Theta.lean:376), `Roth.mapped_det_ne_zero_aux` (Theta.lean:511, private), `Roth.weight_le_delta_aux` (Theta.lean:494, private), `Roth.index_det_le` (Theta.lean:457), `MvPolynomial.hasseDeriv_map` (Roth/HasseDeriv.lean:134
- Used by: `Roth.Θ_option_le` (Roth/Theta.lean:600, `obtain ⟨l, hl, hl', hle⟩ := index_le_lem6 hδ0 hδ1 hrp hratio hr₁ hq hR hh`). No other occurrence in `Roth/` or `Roth.lean`. Transitively feeds Lemma 7 via `Θ_option_le` (Theta.lean:920).

### #214 theorem Roth.Θ_option_le (public, Roth/Theta.lean:593)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: The named Lemma 6 of the Roth development (Θ_p(B; q; r) ≤ 2 max over 1 ≤ l ≤ r_p+1 of Φ + √Φ + √δ), a 4-line sup-taking wrapper of the project lemmas Θ_le_of_forall_index_le and index_le_lem6 about project-only notions (Θ, lem6Φ, lem6M); mathlib has none of this and the literature states only the final Roth lemma standalone, so it is project-local; two hypotheses (hq, hB) are superfluous (compiled).
- action: Keep in Roth/Theta.lean (single caller Roth/Theta.lean:920 in Lemma 7); optionally drop hq (together with index_le_lem6's _hq) and hB per evidence/Roth.Θ_option_le/weaken_hq.lean and remove the two corresponding arguments at Theta.lean:920; do not upstream.
- Type: `{τ : Type*} [Fintype τ] {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) {r : Option τ → ℕ} (hrp : 3 ≤ (r none : ℝ)) (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} (hq : ∀ j, 0 < q j) {B : ℝ} (hB : 1 ≤ B) : Θ B q r ≤ 2 * (Finset.Icc 1 (r none + 1)).sup' _ (fun l ↦ lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l + √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) 
- What: Lemma 6 of the source (clean.tex §5, Lemma `roth:lem6`, l.704–725): `Θ_p(B; q; r) ≤ 2 max_{1 ≤ l ≤ r_p+1} (Φ + Φ^{1/2} + δ^{1/2})` with `Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q'; l r')`, `M = (r₁+1)^{pl} l! B^l 2^{p r₁ l}`; the last variable is `none : Option τ`.
- Hypotheses: `hδ0`, `hδ1`, `hrp`, `hratio`, `hr₁` (passed to `index_le_lem6`); `hq` (passed to `index_le_lem6`'s unused `_hq`, hence superfluous); `hB` (only for `indexSet_nonempty` inside `Θ_le_of_forall_index_le`; superfluous, see evidence (4)).
- Uses from project: `Roth.Θ` (Theta.lean:68), `Roth.lem6Φ` (Theta.lean:275), `Roth.lem6M` (Theta.lean:270), `Roth.Θ_le_of_forall_index_le` (Theta.lean:124), `Roth.index_le_lem6` (Theta.lean:556)
- Used by: `Roth/Theta.lean:920` (inductive step of Lemma 7, `refine (Θ_option_le (τ := Fin (n + 1)) hδ0.le hδ1.le ...).trans_lt ?_`); also named in the module docstring (Theta.lean:36). No other occurrence in `Roth/` or `Roth.lean`.

### #215 lemma Roth.factorial_coefficient_le_two_pow_aux (private, Roth/Theta.lean:609)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private natural-number arithmetic step of Lemma 7 bounding the non-B factors of lem6M, (r1+1)^(pl) l! 2^(pl r1), by 2^((2p+1) r1 l) when l is at most 2^r1; a 2-step calc from Nat.lt_two_pow_self and Nat.factorial_le_pow with no mathlib counterpart in this shape.
- action: Keep as private helper for its sole use in lem6M_lt (Roth/Theta.lean:658); no upstream action.
- Type: `∀ (p r₁ l : ℕ), l ≤ 2 ^ r₁ → (r₁ + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁) ≤ 2 ^ ((2 * p + 1) * r₁ * l)` (declared `private lemma`, all in `ℕ`).
- What: If `l ≤ 2^{r₁}` then `(r₁+1)^{pl} · l! · 2^{p l r₁} ≤ 2^{(2p+1) r₁ l}`. These are exactly the factors of `lem6M p r₁ B l = (r₁+1)^{pl} l! B^l 2^{p l r₁}` other than `B^l`; the lemma is the "the remaining factors are at most `2^{(2p+1) r₁ l}`" step of the source's proof of Lemma 7 (§5).
- Hypotheses: `hl : l ≤ 2 ^ r₁` (used only for the factorial bound `l! ≤ l^l ≤ (2^{r₁})^l`). Necessary in some form: without a bound on `l` relative to `r₁` the claim fails (e.g. `p = 0, r₁ = 0, l = 2`: `2! = 2 > 1 = 2^0`). Already the natural weak form (the call site has the stronger `l ≤ r₁` and weakens it).
- Uses from project: `[]` (only mathlib/core: `Nat.lt_two_pow_self`, `Nat.factorial_le_pow`, `Nat.pow_le_pow_left`, `pow_mul`, `pow_add`, `gcongr`, `ring_nf`).
- Used by: Roth/Theta.lean `Roth.lem6M_lt` only (l.658, `exact_mod_cast factorial_coefficient_le_two_pow_aux p r₁ l (hl'.trans Nat.lt_two_pow_self.le)`, to get the real-valued `hnatR`). `grep -rn factorial_coefficient_le_two_pow_aux Roth/` returns only the definition (l.609) and this use.

### #216 lemma Roth.two_pow_lt_rpow_aux (private, Roth/Theta.lean:621)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private real-analytic step of Lemma 7 showing 2^((2p+1) r1 l) < q^(delta/p * l r1) when log q is at least p(2p+1)/delta; a log/exp comparison built from Real.rpow_def_of_pos and log 2 < 1 whose shape is dictated by lem6M_lt, with no mathlib counterpart.
- action: Keep as private helper for its sole use in lem6M_lt (Roth/Theta.lean:668); no upstream action.
- Type: `∀ {p r₁ l : ℕ}, 0 < p → ∀ {δ q : ℝ}, 0 < δ → 0 ≤ q → (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q → 0 < l * r₁ → (2 : ℝ) ^ ((2 * p + 1) * r₁ * l) < q ^ (δ / p * (l * r₁))` (declared `private lemma`; left side is a natural-number power `Monoid.npow`, right side `Real.rpow`).
- What: If `p > 0`, `δ > 0`, `q ≥ 0`, `log q ≥ p(2p+1)/δ` and `l r₁ > 0`, then `2^{(2p+1) r₁ l} < q^{(δ/p) l r₁}`. This is the step of the source's proof of Lemma 7 (§5) that absorbs the factor `2^{(2p+1) r₁ l}` bounding the non-`B` part of `lem6M` into the extra `q₁^{δ l r₁ / p}`, giving `M < q₁^{δ(1+1/p) l r₁}`.
- Hypotheses: `hp : 0 < p` (needed: the division `δ / p` and the `le_div_iff₀` step; for `p = 0` the right side is `q^0 = 1` while the left is `2^{r₁ l} > 1`). `hδ : 0 < δ` (used in `div_le_iff₀`). `hq : 0 ≤ q` (needed for `Real.log_pos_iff`; for negative `q` Mathlib's `log q = log |q|` and `Real.rpow` of a negat
- Uses from project: `[]` (only mathlib: `Real.log_pos_iff`, `Real.log_lt_sub_one_of_pos`, `le_div_iff₀`, `div_le_iff₀`, `mul_div_assoc'`, `Real.rpow_natCast`, `Real.rpow_def_of_pos`, `Real.exp_lt_exp`, `mul_lt_mul_of_pos_right`, `mul_lt_of_lt_one_left`, tactics `positivity`, `linarith`, `push_cast`, `ring`).
- Used by: Roth/Theta.lean `Roth.lem6M_lt` only (l.668, `two_pow_lt_rpow_aux hp hδ0 hq1pos.le hq₁ (Nat.mul_pos (by lia) (by lia))`, the strict step of its `calc`). `grep -rn two_pow_lt_rpow_aux Roth/` returns only the definition (l.621) and this use.

### #217 theorem Roth.lem6M_lt (public, Roth/Theta.lean:649)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: The Lemma 7 estimate M < q1^(delta(1+1/p) l r1) for the project-local Lemma 6 constant lem6M with B = q1^(delta r1) (clean.tex l.973-981); a 4-step real-arithmetic chain through two private aux lemmas, with no literature standing and no mathlib counterpart, and not a 3-call mathlib composition; recommended resolution is to keep it project-local (a compiled weakening to real q1 and l at most 2^r1 exists but buys nothing at the single call site).
- action: Keep in Roth/Theta.lean (single caller private theta_phi_lt_aux at Roth/Theta.lean:871); optionally make it private or adopt the weakened signature of evidence/Roth.lem6M_lt/weaken.lean; do not upstream.
- Type: `{p : ℕ} (hp : 0 < p) {δ : ℝ} (hδ0 : 0 < δ) {r₁ q₁ : ℕ} (hq₁ : (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q₁) {l : ℕ} (hl : 1 ≤ l) (hl' : l ≤ r₁) : lem6M p r₁ ((q₁ : ℝ) ^ (δ * r₁)) l < (q₁ : ℝ) ^ (δ * (1 + 1 / p) * (l * r₁))`
- What: If `log q₁ ≥ p(2p+1)/δ` and `1 ≤ l ≤ r₁`, then the Lemma 6 constant `M = (r₁+1)^{pl} l! 2^{plr₁} B^l` with `B = q₁^{δ r₁}` satisfies `M < q₁^{δ₁ l r₁}` where `δ₁ = δ(1 + 1/p)`.
- Hypotheses: `hp` (p > 0, divides by p); `hδ0`; `hq₁` (forces `q₁ > 1` and gives `2p+1 ≤ (δ/p) log q₁`); `hl` (needed for strictness, since at `l = 0` both sides equal 1); `hl'` (only used to get `l ≤ 2^{r₁}` and `r₁ > 0`).
- Uses from project: `Roth.lem6M`, `Roth.factorial_coefficient_le_two_pow_aux` (private), `Roth.two_pow_lt_rpow_aux` (private)
- Used by: `Roth.theta_phi_lt_aux` (private) at Roth/Theta.lean:871; no other uses in `Roth/`

### #218 theorem Roth.lem7_Φ_bound (public, Roth/Theta.lean:678)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Pure numeric bookkeeping inequality delta1 + 10^(p-1) delta1^e < 3 10^(p-1) delta^e (e = (1/2)^(p-1), delta1 = delta(1+1/p)) from the proof of Lemma 7 (clean.tex l.1008-1019); every hypothesis is necessary (compiled counterexamples), no literature standing, no mathlib counterpart, not a 3-call composition; recommended resolution is to keep it project-local.
- action: Keep in Roth/Theta.lean (single caller private theta_phi_lt_aux at Roth/Theta.lean:876); optionally make it private and golf hδe with Real.self_le_rpow_of_le_one; do not upstream.
- Type: `{p : ℕ} (hp : 2 ≤ p) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1) : δ * (1 + 1 / p) + 10 ^ (p - 1) * (δ * (1 + 1 / p)) ^ ((1 / 2 : ℝ) ^ (p - 1)) < 3 * 10 ^ (p - 1) * δ ^ ((1 / 2 : ℝ) ^ (p - 1))`
- What: For `p ≥ 2` and `0 < δ ≤ 1`, with `δ₁ = δ(1 + 1/p)` and `e = (1/2)^{p-1}`, the inequality `δ₁ + 10^{p-1} δ₁^e < 3 · 10^{p-1} δ^e` holds.
- Hypotheses: - `hp`: needed for `1 + 1/p ≤ 3/2` and `10^{p-1} ≥ 10`. It fails at `p = 1`.
- Uses from project: `[]`
- Used by: `Roth.theta_phi_lt_aux` (private) at Roth/Theta.lean:876. It has no other uses in `Roth/`.

### #219 theorem Roth.lem7_numeric (public, Roth/Theta.lean:709)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Final numeric absorption step 2(Phi + sqrt Phi + sqrt delta) < 10^p delta^((1/2)^p) of the proof of Lemma 7 (clean.tex l.1023-1035); all hypotheses necessary (compiled counterexamples), ad hoc constants with no literature standing, no mathlib counterpart, not a 3-call composition; recommended resolution is keep project-local.
- action: Keep in Roth/Theta.lean (single caller private theta_phi_lt_aux at Roth/Theta.lean:879); optionally make it private alongside lem7_Φ_bound; do not upstream.
- Type: `{p : ℕ} (hp : 2 ≤ p) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1) {Φ : ℝ} (hΦ : Φ ≤ 3 * 10 ^ (p - 1) * δ ^ ((1 / 2 : ℝ) ^ (p - 1))) : 2 * (Φ + √Φ + √δ) < 10 ^ p * δ ^ ((1 / 2 : ℝ) ^ p)`
- What: For `p ≥ 2`, `0 < δ ≤ 1` and any real `Φ ≤ 3·10^{p-1} δ^{(1/2)^{p-1}}`, the inequality `2(Φ + √Φ + √δ) < 10^p δ^{(1/2)^p}` holds.
- Hypotheses: - `hp`: needed. It fails at `p = 1`.
- Uses from project: `[]`
- Used by: `Roth.theta_phi_lt_aux` (private, the Lemma 7 induction step) at Roth/Theta.lean:879. It has no other uses in `Roth/`.

### #220 lemma Roth.theta_scaled_unique_le_aux (private, Roth/Theta.lean:742)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-variable step of the Lemma 7 induction (Theta_1(M; q2; l r2) at most delta from Lemma 5 plus monotonicity in B and the balanced-log condition); about the project-specific Theta, so nothing upstreamable.
- action: Keep as private helper for its sole use in theta_phi_lt_aux (Roth/Theta.lean:883); optionally add a short docstring citing the source chain in the proof of Lemma 7.
- Type: `∀ {δ M : ℝ} {q₁ q₂ r₁ r₂ l : ℕ}, 1 < q₁ → 0 < r₁ → 0 < l → (r₁ : ℝ) * Real.log q₁ ≤ r₂ * Real.log q₂ → 1 ≤ M → M ≤ (q₁ : ℝ) ^ (δ * (l * r₁)) → Θ M (fun _ : Unit ↦ q₂) (fun _ ↦ l * r₂) ≤ δ` (declared `private lemma`).
- What: In one variable (index type `Unit`), if `q₁ > 1`, `r₁, l > 0`, the balanced-logarithm inequality `r₁ log q₁ ≤ r₂ log q₂` holds and `1 ≤ M ≤ q₁^{δ l r₁}`, then `Θ_1(M; q₂; l r₂) ≤ δ`. This is exactly the displayed chain in the source proof of Lemma 7: `Θ_1(M; q_p; l r_p) ≤ Θ_1(q_1^{δ_1 l r_1}; q_p; l r_p) ≤ log(q_1^{δ_1 l r_1})/(l r_p log q_p) ≤ δ_1` (clean.tex, around l.985), with `δ` playing the role of `δ_1`.
- Hypotheses: All six are used in the proof. `hq₁` gives `log q₁ > 0` (needed for `δ ≥ 0` and `q₂ > 1`); `hr₁`, `hl` are needed because if `r₁ = 0` or `l = 0` then `hM` forces `M ≤ 1` with `δ` unconstrained (possibly negative), while `Θ` is nonnegative-valued in that regime, so the conclusion would fail; `hM1` is
- Uses from project: `Roth.Θ` (Roth/Theta.lean:68), `Roth.Θ_mono` (Roth/Theta.lean:134), `Roth.Θ_unique_le` (Roth/Theta.lean:256).
- Used by: Roth/Theta.lean `Roth.theta_phi_lt_aux` only (l.883, the one-variable term of `Φ`, applied with `δ := ε = δ(1 + 1/(n+2))` via `hM.le`). `grep -rn theta_scaled_unique_le_aux Roth/` returns only the definition (l.742) and this use. Transitively: `theta_phi_lt_aux` → `theta_lt_succ_aux` (l.930) → public `Roth.Θ_lt` (Lemma 7, l.978).

### #221 lemma Roth.theta_delta_succ_lt_aux (private, Roth/Theta.lean:767)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private elementary real inequality delta(1+1/(n+2)) < 1/(n+1) for delta at most 1/(n+2), the step delta_1 < 1/(p-1) in the source proof of Lemma 7 feeding the induction hypothesis; too specific for mathlib.
- action: Keep as private helper for its sole use in theta_phi_lt_aux (Roth/Theta.lean:889); optionally add a one-line docstring citing the source inequality (p-1) delta_1 < (p-1)(p+1)/p^2 < 1.
- Type: `∀ (n : ℕ) {δ : ℝ}, δ ≤ 1 / ((n : ℝ) + 1 + 1) → δ * (1 + 1 / ((n : ℝ) + 1 + 1)) < 1 / ((n : ℝ) + 1)` (declared `private lemma`).
- What: With `p = n + 2`, if `δ ≤ 1/p` then `δ_1 := δ(1 + 1/p) < 1/(p-1)`. Mathematically: `δ(1 + 1/p) ≤ (p+1)/p² < 1/(p-1)` because `(p-1)(p+1) = p² - 1 < p²`. This is the source inequality `0 < (p-1)δ_1 < (p-1)(p+1)/p² < 1` (clean.tex l.995, proof of Lemma 7), which certifies that the enlarged parameter `δ_1` satisfies the induction hypothesis' bound `δ_1 ≤ 1/(p-1)`.
- Hypotheses: The single hypothesis `hδ` is necessary (for large `δ` the conclusion fails). No sign condition on `δ` is needed: the factor `1 + 1/(n+2)` is positive, so negative `δ` is covered by the same monotonicity step. `n` is explicit because it cannot be inferred from the conclusion's use site otherwise (it
- Uses from project: `[]` (only mathlib lemmas: `mul_le_mul_of_nonneg_right`, `lt_div_iff₀`, `one_div_mul_cancel`, `sq_pos_of_pos`, `one_div_pos`, tactics `positivity`, `nlinarith`).
- Used by: Roth/Theta.lean `Roth.theta_phi_lt_aux` only (l.889, as `(theta_delta_succ_lt_aux n hδ).le`, the `δ`-bound argument to the induction hypothesis `ih` at `ε = δ(1 + 1/(n+2))`). `grep -rn theta_delta_succ_lt_aux Roth/` returns only the definition (l.767) and this use. Transitively: `theta_phi_lt_aux` (l.840) → `theta_lt_succ_aux` (l.891) → public `Roth.Θ_lt` (Lemma 7, l.962).

### #222 lemma Roth.theta_prefix_lt_aux (private, Roth/Theta.lean:776)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private induction-step helper of Lemma 7 bounding the (p-1)-variable term Theta_{p-1}(M; q_1..q_{p-1}; l r_1..l r_{p-1}) via monotonicity in M and the induction hypothesis at delta_1; tied to the project-specific Theta, no mathlib home.
- action: Keep as private helper for its sole use in theta_phi_lt_aux (Roth/Theta.lean:886); optionally weaken hanti to the single inequality r (Fin.last (n+1)) at most r (Fin.last n).castSucc and add a docstring citing the source step (clean.tex l.989-1007).
- Type: `∀ {n : ℕ} {δ ε M : ℝ}, 0 < δ → δ ≤ ε → ∀ {r q : Fin (n + 2) → ℕ}, (∀ j, r (Fin.last (n + 1)) ≤ r j) → 3 ≤ (r (Fin.last (n + 1)) : ℝ) → (∀ i : Fin (n + 1), (r i.succ : ℝ) ≤ δ * r i.castSucc) → ((n : ℝ) + 1 + 1) * (2 * ((n : ℝ) + 1 + 1) + 1) / δ ≤ Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) → ∀ {l : ℕ}, 1 ≤ l → 1 ≤ M → M ≤ (q 0 : ℝ) ^ (ε * (l * r 0)) → (IH for dimensio
- What: In the induction step of Lemma 7 (dimension `p = n + 2`), bounds the `(p-1)`-variable term of `Φ` in Lemma 6: if `1 ≤ M ≤ q_1^{ε l r_1}` (with `ε = δ_1 = δ(1+1/p)` at the call site), then `Θ_{p-1}(M; q_1, …, q_{p-1}; l r_1, …, l r_{p-1}) < 10^{p-1} ε^{(1/2)^{p-1}}`. This is the source passage clean.tex l.989–1007: monotonicity of `Θ` in `M`, then verifying the four induction hypotheses for dimension `p-1`, parameter `δ_1`, degrees `l r_j`, then applying the induction hypothesis.
- Hypotheses: `hδ0` is needed for `div_le_div₀` (positivity of the smaller denominator). `hδε` drives obligations (2) and (3). `hanti` is used only at `j = (Fin.last n).castSucc`, so it could be weakened to that single inequality (cosmetic; the call site passes `fun j ↦ hanti (Fin.le_last j)`). `hl : 1 ≤ l` is ne
- Uses from project: `Roth.Θ` (def, Roth/Theta.lean:68), `Roth.Θ_mono` (Roth/Theta.lean:134). All other names are mathlib (`div_le_div₀`, `le_mul_of_one_le_left`, `mul_le_mul_of_nonneg_left`, `mul_le_mul_of_nonneg_right`, `mul_left_comm`, `mul_nonneg`, `add_nonneg`, `Nat.cast_nonneg`, `Nat.cast_mul`, `Fin.castSucc_zero`, `Fin.last`, `Fin.castSucc`; tactics `push_cast`, `linarith`, `norm_num`, `simp`, `simpa`, `exact_m
- Used by: Roth/Theta.lean `Roth.theta_phi_lt_aux` only (l.886, inside the final `exact`, as the `(p-1)`-variable summand of `Φ`, with `ε := δ(1 + 1/(n+2))` and `ih hε0 (theta_delta_succ_lt_aux n hδ).le`). `grep -rn theta_prefix_lt_aux Roth/` returns only the definition (l.776) and this use. Transitively: `theta_phi_lt_aux` (l.840) → `theta_lt_succ_aux` (l.891, use at l.930) → public `Roth.Θ_lt` (Lemma 7, l.

### #223 lemma Roth.theta_lt_base_aux (private, Roth/Theta.lean:818)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private m = 1 base case of Lemma 7 (Theta_1(q^{delta r}; q; r) at most delta, hence below 10 delta^{1/2}) via Lemma 5 Θ_unique_le; tied to the project-specific Theta, no mathlib home.
- action: Keep as private helper for its sole use in the zero case of Roth.Θ_lt (Roth/Theta.lean:973); optionally add a docstring citing clean.tex l.964-967 and use Real.self_le_rpow_of_le_one for h1.
- Type: `∀ {δ : ℝ}, 0 < δ → δ ≤ 1 → ∀ {r q : Fin 1 → ℕ}, 0 < r 0 → 1 < q 0 → Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ 1 * δ ^ ((1 / 2 : ℝ) ^ 1)` (declared `private lemma`).
- What: The `m = 1` base case of Lemma 7: for one variable with `r_1 > 0`, `q_1 > 1` and `0 < δ ≤ 1`, `Θ_1(q_1^{δ r_1}; q_1; r_1) < 10 δ^{1/2}`. Mirrors clean.tex l.964–967: by Lemma 5, `Θ_1 ≤ δ r_1 log q_1 / (r_1 log q_1) = δ < 10 δ^{1/2}`. The conclusion is stated in the literal shape `10 ^ 1 * δ ^ ((1/2) ^ 1)` of `Θ_lt` at `n = 0`, so it plugs in without rewriting.
- Hypotheses: `hδ0` for `Real.rpow_pos_of_pos`, positivity of the exponent, and `rpow_le_rpow_of_exponent_ge`; `hδ : δ ≤ 1` for `δ ≤ δ^{1/2}` (the call site handles `δ > 1` separately via `theta_lt_of_large_delta_aux`); `hrlast : 0 < r 0` for cancelling `r_0` in `field_simp`; `hq1 : 1 < q 0` for `Θ_unique_le`, `1
- Uses from project: `Roth.Θ` (def, Roth/Theta.lean:68), `Roth.Θ_unique_le` (Lemma 5, Roth/Theta.lean:256). All other names are mathlib (`Real.one_le_rpow`, `Real.log_rpow`, `Real.log_pos`, `Real.rpow_le_rpow_of_exponent_ge`, `Real.rpow_pos_of_pos`, `lt_mul_of_one_lt_left`, `Subsingleton.elim`, `ne_of_gt`; tactics `field_simp`, `norm_num`, `positivity`, `simpa`, `exact_mod_cast`).
- Used by: Roth/Theta.lean `Roth.Θ_lt` only (l.973, `zero` case of the induction, branch `δ ≤ 1`, with `hq1` supplied by `theta_denominators_one_lt_aux`). `grep -rn theta_lt_base_aux Roth/` returns only the definition (l.818) and this use.

### #224 lemma Roth.theta_denominators_one_lt_aux (private, Roth/Theta.lean:833)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private 3-line glue deriving 1 < q j from 0 < r 0, 0 < log q 0 and the Lemma 7 growth condition r 0 log q 0 at most r j log q j; Lemma-7-specific hypothesis shape, no mathlib home.
- action: Keep as private helper for its three uses in Roth/Theta.lean (theta_phi_lt_aux l.862, theta_lt_succ_aux l.907, Θ_lt l.974); optionally add a docstring; the same argument is re-derived inline in theta_scaled_unique_le_aux (l.752-757) but entangled with hr₂, so no refactor needed.
- Type: `∀ {n : ℕ} {r q : Fin (n + 1) → ℕ}, 0 < r 0 → 0 < Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) → ∀ (j : Fin (n + 1)), 1 < q j` (declared `private lemma`).
- What: Under the Lemma 7 growth condition `r_1 log q_1 ≤ r_j log q_j` (clean.tex (21)-type hypothesis `hqr` of `Θ_lt`), together with `r_1 > 0` and `log q_1 > 0`, every denominator satisfies `q_j > 1`. Supplies the `1 < q` side conditions needed by Lemma 5 (`Θ_unique_le`) and by `Real.one_le_rpow`.
- Hypotheses: `hrlast : 0 < r 0` and `hq1 : 0 < log (q 0)` both feed `mul_pos` and are necessary (with either zero the left side of `hqr` is `0` and nothing is forced); `hqr` used at index `j`. All used, none redundant. (`hrlast` is a misnomer here: it is positivity of `r 0`, not of the last entry.)
- Uses from project: `[]` (only mathlib names: `Real.log_pos_iff`, `pos_of_mul_pos_right`, `mul_pos`, `Nat.cast_nonneg`, `LT.lt.trans_le`; tactic `exact_mod_cast`).
- Used by: Roth/Theta.lean only: `Roth.theta_phi_lt_aux` (l.862, at `j = 0`), `Roth.theta_lt_succ_aux` (l.907, partially applied, used as `hq _` and `hq 0` at l.925-926), `Roth.Θ_lt` (l.974, zero case, at `j = 0`). `grep -rn theta_denominators_one_lt_aux Roth/` returns only these plus the definition.

### #225 lemma Roth.theta_phi_lt_aux (private, Roth/Theta.lean:840)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private induction-step helper of Lemma 7 bounding Phi + sqrt Phi + sqrt delta below half the target for each admissible l in Lemma 6; assembles project-specific Theta and lem6M estimates, no mathlib home.
- action: Keep as private helper for its sole use in theta_lt_succ_aux (Roth/Theta.lean:930); optionally drop the derivable hypotheses hanti and hδ1 (both follow from hδ and hratio, as theta_lt_succ_aux shows) and add a docstring citing clean.tex l.969-1018.
- Type: `∀ {n : ℕ} {δ : ℝ}, 0 < δ → δ ≤ 1 / ((n : ℝ) + 1 + 1) → δ < 1 → ∀ {r q : Fin (n + 2) → ℕ}, Antitone r → 3 ≤ (r (Fin.last (n + 1)) : ℝ) → (∀ i : Fin (n + 1), (r i.succ : ℝ) ≤ δ * r i.castSucc) → ((n : ℝ) + 1 + 1) * (2 * ((n : ℝ) + 1 + 1) + 1) / δ ≤ Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) → (IH: Lemma 7 for dimension n+1, universally quantified over δ, r, q) → ∀ {l 
- What: The per-`l` core of the induction step of Lemma 7 (dimension `p = n + 2`): for every admissible `l ∈ [1, r_p + 1]`, with `M` and `Φ` as in Lemma 6, `Φ + Φ^{1/2} + δ^{1/2} < 10^p δ^{(1/2)^p} / 2`. Source: clean.tex l.969–1018 (estimate of `M`, of the one-variable term by `δ_1`, of the `(p-1)`-variable term by the IH at `δ_1 = δ(1+1/p)`, then the numeric absorption `Φ < 3·10^{p-1} δ^{(1/2)^{p-1}}` and the final bound).
- Hypotheses: All are used. `hδ1` and `hanti` are redundant given the others: `hδ1` follows from `hδ` (as derived in `theta_lt_succ_aux`, l.903–904) and `hanti` follows from `hratio` + `hδ1` (as derived via `Fin.antitone_iff_succ_le` at l.905–906); the caller passes them already computed, so this is a deliberate 
- Uses from project: `Roth.Θ` (Roth/Theta.lean:68), `Roth.lem6M` (l.270), `Roth.one_le_lem6M` (l.279), `Roth.lem6M_lt` (l.649), `Roth.lem7_Φ_bound` (l.678), `Roth.lem7_numeric` (l.709), `Roth.theta_scaled_unique_le_aux` (l.742), `Roth.theta_delta_succ_lt_aux` (l.767), `Roth.theta_prefix_lt_aux` (l.776), `Roth.theta_denominators_one_lt_aux` (l.833). Mathlib names: `Finset.mem_Icc`, `Fin.le_last`, `Real.one_le_rpow`, `m
- Used by: Roth/Theta.lean `Roth.theta_lt_succ_aux` only (l.930, `exact fun l hl ↦ theta_phi_lt_aux … ih hl` after `Finset.sup'_lt_iff`). `grep -rn theta_phi_lt_aux Roth/` returns only the definition (l.840) and this use. Transitively: `theta_lt_succ_aux` (l.891) → public `Roth.Θ_lt` (Lemma 7, l.962).

### #226 lemma Roth.theta_lt_succ_aux (private, Roth/Theta.lean:891)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private induction step of Lemma 7 (dimension n+2, small delta case) applying Lemma 6 via finSuccEquivLast transport and closing with theta_phi_lt_aux; project-specific Theta estimate, no mathlib home.
- action: Keep as private helper for its sole use in Roth.Θ_lt (Roth/Theta.lean:978); optionally add a docstring citing clean.tex l.969-1021.
- Type: `∀ {n : ℕ} {δ : ℝ}, 0 < δ → δ ≤ 1 / ((n : ℝ) + 1 + 1) → ∀ {r q : Fin (n + 2) → ℕ}, 3 ≤ (r (Fin.last (n + 1)) : ℝ) → (∀ i : Fin (n + 1), (r i.succ : ℝ) ≤ δ * r i.castSucc) → ((n : ℝ) + 1 + 1) * (2 * ((n : ℝ) + 1 + 1) + 1) / δ ≤ Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) → (ih: Lemma 7 in dimension n+1 for every δ with 0 < δ ≤ 1/(n+1), every r q : Fin (n + 1) → ℕ satis
- What: The induction step of Lemma 7 for `p = n + 2` variables in the case `δ ≤ 1/p`: assuming Lemma 7 in `p - 1` variables, `Θ_p(q_1^{δ r_1}; q; r) < 10^p δ^{(1/2)^p}`. Source: clean.tex l.969–1021 (proof of `roth:lem7`, inductive step: apply Lemma 6, estimate `M` and `Φ` for every allowed `l`).
- Hypotheses: All used. `hδ0`, `hδ` give `δ < 1` and feed `Θ_option_le` and `theta_phi_lt_aux`; `hrlast`, `hratio` give antitonicity, positivity and the Lemma 6 ratio condition; `hq1`, `hqr` give `1 < q j` and are forwarded; `ih` is forwarded to `theta_phi_lt_aux`. The `ih` hypothesis carries an upper bound `δ ≤ 
- Uses from project: `Roth.Θ` (Roth/Theta.lean:68), `Roth.Θ_equiv` (l.159), `Roth.lem6Φ` (l.275), `Roth.Θ_option_le` (l.593, Lemma 6), `Roth.theta_denominators_one_lt_aux` (l.833), `Roth.theta_phi_lt_aux` (l.840). Mathlib names: `div_lt_one`, `Fin.antitone_iff_succ_le`, `mul_le_of_le_one_left`, `Fin.zero_le`, `Fin.le_last`, `Fin.succ_last`, `Fin.castSucc_le_castSucc_iff`, `mul_le_mul_of_nonneg_left`, `finSuccEquivLast
- Used by: Roth/Theta.lean `Roth.Θ_lt` only (l.978, `succ` case of the induction when `δ ≤ 1/(n+2)`). `grep -rn theta_lt_succ_aux Roth/` returns only the definition (l.891) and this use. Transitively feeds every user of the public Lemma 7 `Roth.Θ_lt`.

### #227 lemma Roth.theta_lt_of_large_delta_aux (private, Roth/Theta.lean:932)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private large-delta case of Lemma 7 (delta at least 1/(n+1)) closed by the trivial bound Theta at most card via Θ_le_card and (n+1)^2 < 4^(n+1); project-specific Theta estimate extending the source beyond its delta < 1/m hypothesis, no mathlib home.
- action: Keep as private helper for its two uses in Roth.Θ_lt (Roth/Theta.lean:975 and :980); optionally add a docstring noting it covers the delta range excluded by clean.tex eq. (19).
- Type: `∀ {n : ℕ} {δ : ℝ}, 1 / ((n : ℝ) + 1) ≤ δ → ∀ {r q : Fin (n + 1) → ℕ}, Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1))` (declared `private lemma`).
- What: For `m = n + 1` variables and `δ ≥ 1/m`, the Lemma 7 conclusion `Θ_m(q_1^{δ r_1}; q; r) < 10^m δ^{(1/2)^m}` holds unconditionally (no hypotheses on `r`, `q`). This is the range `δ ≥ 1/m` excluded by the source's hypothesis (19) `0 < δ < m^{-1}` (clean.tex l.935–960); the project's `Θ_lt` drops that upper bound, and this lemma discharges the extra case.
- Hypotheses: Only `hδ`, and it is used (last `calc` step, `Real.rpow_le_rpow`). It is essential in the sense that for small `δ` the right side tends to `0` while `Θ` can be positive; no hypotheses on `r`, `q` are needed (the bound `Θ ≤ card` is unconditional).
- Uses from project: `Roth.Θ` (Roth/Theta.lean:68), `Roth.Θ_le_card` (l.114). Mathlib names: `Nat.lt_two_pow_self`, `lt_div_iff₀`, `mul_self_lt_mul_self`, `mul_pow`, `pow_le_pow_left₀`, `mul_one_div`, `mul_le_mul_of_nonneg_left`, `Real.self_le_rpow_of_le_one`, `div_le_one`, `pow_le_one₀`, `Real.rpow_le_rpow`, `Nat.cast_nonneg`.
- Used by: Roth/Theta.lean `Roth.Θ_lt` only, twice: l.975 (`zero` case, `δ > 1`) and l.980 (`succ` case, `δ > 1/(n+2)`). `grep -rn theta_lt_of_large_delta_aux Roth/` returns only the definition (l.932) and these two uses. Transitively feeds every user of public Lemma 7 `Roth.Θ_lt`.

### #228 theorem Roth.Θ_lt (public, Roth/Theta.lean:962)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: The named Lemma 7 of the Roth development (Ridout/Cassels Θ_m(q_1^{δ r_1}; q; r) < 10^m δ^{(1/2)^m}), proved by induction on m from private helpers and Lemmas 5 and 6 about the project-only Θ; mathlib has no Roth index or Θ, the literature states it only inside Roth/Ridout proofs, and its hypotheses are already weaker than the source, so it stays project-local.
- action: Keep in Roth/Theta.lean as the paper's Lemma 7 (single caller: private theta_lt_eta_of_sq_log_bound_aux at Roth/MainLemma.lean:687); do not upstream; no call-site changes.
- Type: `(n : ℕ) {δ : ℝ} (hδ0 : 0 < δ) {r q : Fin (n + 1) → ℕ} (hrlast : 3 ≤ (r (Fin.last n) : ℝ)) (hratio : ∀ i : Fin n, (r i.succ : ℝ) ≤ δ * r i.castSucc) (hq1 : ((n : ℝ) + 1) * (2 * ((n : ℝ) + 1) + 1) / δ ≤ Real.log (q 0)) (hqr : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) : Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1))`
- What: Lemma 7 of the source (clean.tex §5, Lemma `roth:lem7`, l.935–960): for `m = n + 1` variables, rapidly decreasing weights `r` and denominators `q` with `log q_1` large and balanced `r_j log q_j ≥ r_1 log q_1`, the supremum of indices `Θ_m(q_1^{δ r_1}; q; r)` is `< 10^m δ^{(1/2)^m}`.
- Hypotheses: `hδ0` (positivity of δ; with δ = 0 the RHS is 0 and the claim is false since Θ ≥ 0); `hrlast` (needed by Lemma 6 and positivity of `r 0` in the base case); `hratio` (weight decay, fed to Lemma 6 and the induction); `hq1` (large `log q 0`, gives `q_j > 1` and the Lemma 5 bounds); `hqr` (balanced loga
- Uses from project: `Roth.Θ`, private `Roth.theta_lt_base_aux`, private `Roth.theta_denominators_one_lt_aux`, private `Roth.theta_lt_of_large_delta_aux`, private `Roth.theta_lt_succ_aux` (all in Roth/Theta.lean)
- Used by: Roth/MainLemma.lean:687 (private `theta_lt_eta_of_sq_log_bound_aux`, itself used at MainLemma.lean:724 on the path to `main_lemma`); named in the module docstring Roth/Theta.lean:39. No other occurrence in `Roth/` or `Roth.lean`.

### #229 def Roth.lam (public, Roth/MainLemma.lean:60)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: lam is the Roth-proof parameter λ = 4(1+3δ) n √m of the source's eq. (34), a single arithmetic expression in mathlib's Real.sqrt and ring operations with no general mathematical content; nothing to upstream, kept locally only as the paper's named parameter.
- action: Do not upstream; keep Roth.lam in Roth/MainLemma.lean as the paper's λ (consumers: def Roth.gam at MainLemma.lean:63 and the unfoldings grind/simp [gam, lam] at MainLemma.lean:102 eta_lt_gam_iff, MainLemma.lean:638 private exists_mem_RSet_le_index_of_log_bound_aux, Main.lean:244 exists_delta); no call-site changes.
- Type: `(δ : ℝ) (n m : ℕ) : ℝ`, defined as `4 * (1 + 3 * δ) * n * √(m : ℝ)`
- What: the parameter `λ = 4(1 + 3δ) n m^{1/2}` of §6 of the source (clean.tex eq. (34), l.1337–1341), used to define `γ = (m - λ)/2`.
- Hypotheses: none (total function; meaningful for `δ ≥ 0`, `m > 16 n²` in the source).
- Uses from project: `[]`
- Used by: `Roth.gam` (Roth/MainLemma.lean:63, definition body); `Roth.eta_lt_gam_iff` (Roth/MainLemma.lean:102, `grind [gam, lam]`); private `Roth.exists_mem_RSet_le_index_of_log_bound_aux` (Roth/MainLemma.lean:638, `simpa only [gam, lam]`); `Roth.exists_delta` (Roth/Main.lean:244, `simpa [gam, lam, eta, ...]`); mentioned in the module docstring Roth/MainLemma.lean:33. No other occurrence in `Roth/` (the `l

### #230 def Roth.gam (public, Roth/MainLemma.lean:63)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: gam is the Roth-proof parameter γ = (m - λ)/2 of the source's eq. (35), a one-line real expression over Roth.lam with no general mathematical content; nothing to upstream, kept locally as the paper's named parameter used in the statements of main_lemma and exists_delta.
- action: Do not upstream; keep Roth.gam in Roth/MainLemma.lean as the paper's γ (consumers: eta_lt_gam_iff MainLemma.lean:101, private auxiliaries MainLemma.lean:623/648/699, main_lemma MainLemma.lean:743-753, exists_delta Main.lean:230-244, private Main.lean:414/463); no call-site changes.
- Type: `(δ : ℝ) (n m : ℕ) : ℝ`, defined as `((m : ℝ) - lam δ n m) / 2`
- What: the parameter `γ = (m - λ)/2` of §6 of the source (clean.tex eq. (35), l.1342–1345); the target lower bound on the index of the auxiliary polynomial `W*` at `(α, …, α)` before differentiation, and `γ - η` the index bound in Roth's Lemma 9.
- Hypotheses: none (total function; meaningful for `δ ≥ 0`, `m > 16 n²`).
- Uses from project: `Roth.lam`
- Used by: `Roth.eta_lt_gam_iff` (Roth/MainLemma.lean:101–102, statement and `grind [gam, lam]`); private `Roth.exists_mem_RSet_le_index_of_log_bound_aux` (MainLemma.lean:623 statement, :638 `simpa only [gam, lam]`); private `Roth.exists_auxiliary_polynomial_of_log_bound_aux` (MainLemma.lean:648); private `Roth.exists_auxiliary_polynomial_with_index_gap_aux` (MainLemma.lean:699); `Roth.main_lemma` (MainLemma

### #231 def Roth.eta (public, Roth/MainLemma.lean:66)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: eta is the Roth-proof parameter η = 10^m δ^((1/2)^m) of the source's eq. (36), a one-line real expression (pow times rpow) with no general mathematical content; nothing to upstream, kept locally as the paper's named η used in main_lemma and exists_delta.
- action: Do not upstream; keep Roth.eta in Roth/MainLemma.lean (consumers MainLemma.lean:78/85/89/100-101/676/687/699/743/750/753, Main.lean:229-244/413-414/463); optional local tidy, move eta into Roth/Theta.lean and state Θ_lt (Theta.lean:966) and its helpers via eta.
- Type: `(δ : ℝ) (m : ℕ) : ℝ`, defined as `10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m)`
- What: the parameter `η = 10^m δ^{(1/2)^m}` of §6 of the source (clean.tex eq. (36), l.1346–1349); the upper bound from Lemma 7 (`Roth.Θ_lt`) on the index at `(h_j/q_j)_j`, and the loss in the index bound `γ - η` of Roth's Lemma 9.
- Hypotheses: none (total function; meaningful for `δ ≥ 0`; for `δ < 0` `Real.rpow` gives the junk value of the complex-branch definition).
- Uses from project: `[]`
- Used by: `Roth.exists_delta_bound` (Roth/MainLemma.lean:78 statement, :85 continuity, :89 `simpa [eta, ...]`); `Roth.eta_lt_gam_iff` (MainLemma.lean:100–101); private `Roth.theta_lt_eta_of_sq_log_bound_aux` (MainLemma.lean:676 statement, :687 `simpa [eta] using Θ_lt ...`); private `Roth.exists_auxiliary_polynomial_with_index_gap_aux` (MainLemma.lean:699); `Roth.main_lemma` (MainLemma.lean:743, :750, :753);

### #232 def Roth.mainCoeffBound (public, Roth/MainLemma.lean:69)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: mainCoeffBound is the Roth-proof coefficient bound B_1 = floor(q_1^(δ r_1)) of the source's eq. (37), a one-line Nat.floor of a real power with no general mathematical content; nothing to upstream, kept locally as the paper's named B_1 used in main_lemma and its helpers.
- action: Do not upstream; keep Roth.mainCoeffBound in Roth/MainLemma.lean (consumers MainLemma.lean:149-151/182-205/622-639/650-651/702/746, Main.lean:462/484-486); no refactor recommended.
- Type: `(δ : ℝ) (q₁ r₁ : ℕ) : ℕ`, defined as `⌊(q₁ : ℝ) ^ (δ * r₁)⌋₊`
- What: the integer coefficient bound `B_1 = [q_1^{δ r_1}]` of §6 of the source (clean.tex eq. (37), l.1351–1353); the coefficients of the box polynomials in the pigeonhole family `𝒲` range over `[0, B_1]`, and the Hasse derivatives of the auxiliary polynomial are bounded by `B_1^{1+3δ}`.
- Hypotheses: none (total; for `q₁^{δ r₁} < 0` impossible, `Nat.floor` gives 0 below 1).
- Uses from project: `[]`
- Used by: `Roth.mul_log_div_two_lt_log_mainCoeffBound` (Roth/MainLemma.lean:149–151, statement and `simpa [mainCoeffBound, ...]`); `Roth.three_small_factors` (MainLemma.lean:182–184 statement, :197–205 proof); private `Roth.exists_mem_RSet_le_index_of_log_bound_aux` (MainLemma.lean:622, 633–634, 639); private `Roth.exists_auxiliary_polynomial_of_log_bound_aux` (MainLemma.lean:650–651); private `Roth.exists_

### #233 theorem Roth.exists_delta_bound (public, Roth/MainLemma.lean:77)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Lemma m-delta of the source (fixed m > 16n^2 gives delta0 > 0 with (29) delta < 1/m and (30) eta + 2(1+3delta)n sqrt m < m/2 for all 0 <= delta <= delta0); a parameter-choice step of Roth's proof about the project-only eta, hypothesis necessary (compiled converse), no literature standing outside Roth proofs, no mathlib counterpart, and a 12-line continuity argument rather than a 3-call composition; recommended resolution is keep project-local.
- action: Keep in Roth/MainLemma.lean (single caller Roth.exists_delta at Roth/Main.lean:231); do not upstream; optional local restatement as an eventually-in-nhdsWithin-Ici-0 statement (compiled in evidence) if exists_delta is refactored to filters.
- Type: `{n m : ℕ} (hm : 16 * n ^ 2 < m) : ∃ δ₀ : ℝ, 0 < δ₀ ∧ ∀ δ : ℝ, 0 ≤ δ → δ ≤ δ₀ → δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2`
- What: Lemma `m-δ` of §6 of the source (clean.tex l.1211–1248), fixed-`m` form: for `m > 16 n²` there is `δ₀ > 0` such that every `δ ∈ [0, δ₀]` satisfies (29) `δ < 1/m` and (30) `10^m δ^{(1/2)^m} + 2(1+3δ) n √m < m/2`.
- Hypotheses: `hm : 16 * n ^ 2 < m` (necessary: the conclusion at `δ = 0` is equivalent to it, compiled in evidence).
- Uses from project: `Roth.eta`
- Used by: `Roth.exists_delta` (Roth/Main.lean:231); module docstring MainLemma.lean:40.

### #234 theorem Roth.eta_lt_gam_iff (public, Roth/MainLemma.lean:100)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: eta_lt_gam_iff is the source's eq. (38), the rearrangement "(30) iff eta < gamma" of the project-only parameters gam/lam/eta; after unfolding gam = m/2 - 2(1+3delta)n sqrt m it is exactly mathlib's lt_sub_iff_add_lt (compiled two-step composition), so nothing to upstream; kept locally as the paper's named step with two callers.
- action: Do not upstream; keep Roth.eta_lt_gam_iff in Roth/MainLemma.lean next to gam (callers Roth/Main.lean:241 and Roth/Main.lean:560, both via sub_pos); optional local tidy, restate as the gap form 0 < gam - eta (compiled in evidence) to drop the sub_pos at both call sites.
- Type: `(δ : ℝ) (n m : ℕ) : eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔ eta δ m < gam δ n m`
- What: inequality (30) of the source, `η + 2(1+3δ) n √m < m/2`, is equivalent to (38) `η < γ`, where `γ = (m - λ)/2` and `λ = 4(1+3δ) n √m`.
- Hypotheses: none (holds for all real `δ` and natural `n, m`).
- Uses from project: `Roth.eta`, `Roth.gam`, `Roth.lam`
- Used by: `Roth.exists_delta` (Roth/Main.lean:241, `sub_pos.mpr ((eta_lt_gam_iff 0 n m).mp …)`); a theorem at Roth/Main.lean:560 (`sub_pos.2 ((eta_lt_gam_iff _ _ _).1 h30)`).

### #235 lemma Roth.sqrt_lt_nat_floor_aux (private, Roth/MainLemma.lean:104)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private two-line helper giving the strict half sqrt X < natfloor X (for X at least 2) of the public Roth.sqrt_lt_floor; elementary consequence of Real.sqrt_lt' and Nat.lt_floor_add_one with no mathlib counterpart, private and _aux so not upstreamed.
- action: Keep as private helper for its sole use in Roth.sqrt_lt_floor (Roth/MainLemma.lean:116); no upstream action.
- Type: `∀ {X : ℝ}, 2 ≤ X → √X < (⌊X⌋₊ : ℝ)` (declared `private lemma`; `⌊X⌋₊` is `Nat.floor`, cast to `ℝ`).
- What: For a real `X ≥ 2`, the square root of `X` is strictly smaller than the natural floor of `X`. This is the strict inequality `B₁ = ⌊X⌋ > √X` of the source's §6 (with `X = q₁^{δ r₁}`), isolated as the first component of `Roth.sqrt_lt_floor`.
- Hypotheses: `hX : 2 ≤ X`. Needed in some form: for `X ∈ [1, 2)` the floor is `1` while `√X ≥ 1`, so the strict inequality fails (e.g. `X = 1`: `√1 = 1 = ⌊1⌋₊`); for `X < 1` the floor is `0`. The threshold `2` is not sharp (the claim holds iff `⌊X⌋₊ ≥ 2`, i.e. `X ≥ 2`, since for `X ∈ [2,3)` one has `X < 3 < 4 = 
- Uses from project: `[]` (only mathlib: `Nat.le_floor`, `Nat.lt_floor_add_one`, `Real.sqrt_lt'`; tactics `exact_mod_cast`, `positivity`, `nlinarith`).
- Used by: Roth/MainLemma.lean `Roth.sqrt_lt_floor` only (l.116, `⟨sqrt_lt_nat_floor_aux hX, Nat.floor_le (by positivity)⟩`). `grep -rn sqrt_lt_nat_floor_aux Roth/` returns only the definition (l.104) and this use. (Indirectly, through `sqrt_lt_floor`, it feeds Roth/MainLemma.lean l.154 and l.201 and Roth/Main.lean l.494.)

### #236 theorem Roth.sqrt_lt_floor (public, Roth/MainLemma.lean:115)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Elementary estimate sqrt X < natfloor X and natfloor X at most X for real X at least 2 (source §6, B_1 = floor X > sqrt X); not in mathlib under any of five search methods, no literature standing as a named fact, threshold 2 sharp (compiled), but not a 3-call composition (strict half needs Real.sqrt_lt' plus Nat.lt_floor_add_one plus nlinarith); an ad-hoc conjunction mathlib is unlikely to want, so the call is project-local vs upstream.
- action: Recommended - keep Roth.sqrt_lt_floor project-local in Roth/MainLemma.lean (callers MainLemma l.154, l.201, Main l.494); if upstreaming is desired, ship only the strict half as Nat.sqrt_lt_floor-style lemma in Mathlib/Analysis/Real/Sqrt.lean, never the conjunction.
- Type: `∀ {X : ℝ}, 2 ≤ X → √X < (⌊X⌋₊ : ℝ) ∧ (⌊X⌋₊ : ℝ) ≤ X`
- What: For real `X ≥ 2`, the natural floor of `X` lies strictly above `√X` and at or below `X`. This is the source's §6 estimate `B₁ = ⌊X⌋ > X - 1 > √X` with `X = q₁^{δ r₁}`, together with the retained upper bound `B₁ ≤ X`.
- Hypotheses: `hX : 2 ≤ X`. Sharp: at `X = 1` the strict half fails (`√1 = 1 = ⌊1⌋₊`, compiled in evidence), and for `X ∈ [1,2)` generally `⌊X⌋₊ = 1 ≤ √X`. The upper half alone needs only `0 ≤ X`.
- Uses from project: `Roth.sqrt_lt_nat_floor_aux`
- Used by: `Roth.mul_log_div_two_lt_log_mainCoeffBound` (Roth/MainLemma.lean:154, `.1`); the `key` step of a theorem at Roth/MainLemma.lean:201 (`.1`); Roth/Main.lean:494 (`obtain ⟨hsqB, hBX⟩ := sqrt_lt_floor ...`, both halves).

### #237 theorem Roth.four_lt_rpow (public, Roth/MainLemma.lean:122)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Ad-hoc numerical estimate q1^(delta r1) > 4 from 3 at most delta^2 log q1 (source §6, X > 4); hypotheses delta at least 0 and r1 positive are necessary (counterexamples compiled); not in mathlib and not a 3-call composition (needs log 2 < 3/4 plus nlinarith after Real.lt_rpow_of_log_lt); no literature standing, so the call is project-local vs upstream.
- action: Recommended - keep Roth.four_lt_rpow project-local in Roth/MainLemma.lean (callers MainLemma l.641, Main l.495); optional local golf - replace the hlog2 exp-quadratic argument by Real.log_two_lt_d9 (Mathlib/Analysis/Complex/ExponentialBounds.lean); no mathlib PR.
- Type: `∀ {δ : ℝ}, 0 ≤ δ → ∀ {q₁ r₁ : ℕ}, 0 < r₁ → 3 ≤ δ ^ 2 * Real.log ↑q₁ → 4 < (↑q₁ : ℝ) ^ (δ * ↑r₁)`
- What: If `δ ≥ 0`, `r₁ ≥ 1` and `δ² log q₁ ≥ 3`, then `X = q₁^{δ r₁} > 4`. This is the source's §6 claim "`X > 4`" (clean.tex l.1367), which there follows from (32) and (29).
- Hypotheses: `hδ0 : 0 ≤ δ` (necessary; δ = -2, q₁ = 3, r₁ = 1 is a counterexample, compiled), `hr₁ : 0 < r₁` (necessary; r₁ = 0 gives `X = 1`, compiled), `hq₁ : 3 ≤ δ² log q₁` (the constant 3 could be lowered to anything above `4 log 2 ≈ 2.77`, not pursued: no caller benefit).
- Uses from project: `[]`
- Used by: Roth/MainLemma.lean:641 (`Nat.floor_pos.2 <| (by norm_num : (1 : ℝ) ≤ 4).trans (four_lt_rpow hδ0 hr₁ hq).le`); Roth/Main.lean:495 (`sqrt_lt_floor ((by norm_num : (2 : ℝ) ≤ 4).trans (four_lt_rpow hδ0 hr0 h32').le)`).

### #238 theorem Roth.mul_log_div_two_lt_log_mainCoeffBound (public, Roth/MainLemma.lean:149)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Source step log B_1 > half delta r_1 log q_1 (§6), stated about the project-only def mainCoeffBound (itself NO-composable, not upstreamable); its abstract core log X / 2 < log natfloor X for X at least 2 (compiled, threshold 2 sharp) is not in mathlib and needs the project's sqrt_lt_floor (BORDERLINE), so it is not a 3-call mathlib composition; single caller, no literature standing, so the call is project-local vs upstream.
- action: Recommended - keep Roth.mul_log_div_two_lt_log_mainCoeffBound project-local in Roth/MainLemma.lean (single caller three_small_factors at MainLemma l.205); no mathlib PR; if sqrt_lt_floor is ever upstreamed, the abstract X-form could ride along in Mathlib/Analysis/SpecialFunctions/Pow/Real.lean.
- Type: `∀ {δ : ℝ} {q₁ r₁ : ℕ}, 2 ≤ (↑q₁ : ℝ) ^ (δ * ↑r₁) → δ * ↑r₁ * Real.log ↑q₁ / 2 < Real.log ↑(mainCoeffBound δ q₁ r₁)`
- What: With `X = q₁^{δ r₁}` and `B₁ = ⌊X⌋₊ = mainCoeffBound δ q₁ r₁`, if `X ≥ 2` then `½ δ r₁ log q₁ < log B₁`. This is the source's §6 step "Thus `log B_1 > ½ δ r_1 log q_1`" (clean.tex l.1371).
- Hypotheses: `hX : 2 ≤ q₁^{δ r₁}` (necessary: δ = 0 gives `X = 1` and the conclusion `0 < log 1` fails, compiled; threshold 2 is sharp in the abstract form: `X = 3/2` fails, compiled).
- Uses from project: `Roth.mainCoeffBound`, `Roth.sqrt_lt_floor`
- Used by: Roth/MainLemma.lean:205 (inside `Roth.three_small_factors`, `mul_lt_mul_of_pos_left (mul_log_div_two_lt_log_mainCoeffBound hX) hδ`). No other uses in `Roth/`.

### #239 lemma Roth.two_lt_rpow_aux (private, Roth/MainLemma.lean:156)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private numerical helper giving q1^(delta r1) > 2 from log 2 < delta^2 log q1 (delta at least 0, r1 positive), used once in three_small_factors; mathlib has only the reduction Real.lt_rpow_of_log_lt, the rest is a source-specific nlinarith estimate.
- action: Keep as private helper for its single call site Roth/MainLemma.lean:193 (three_small_factors); no mathlib PR; optionally note it shares the proof skeleton of Roth.four_lt_rpow (l.122) but neither subsumes the other.
- Type: `∀ {δ : ℝ}, 0 ≤ δ → ∀ {q₁ r₁ : ℕ}, 0 < r₁ → Real.log 2 < δ ^ 2 * Real.log ↑q₁ → 2 < (↑q₁ : ℝ) ^ (δ * ↑r₁)`
- What: If `δ ≥ 0`, `r₁ ≥ 1` and `log 2 < δ² log q₁`, then `X = q₁^{δ r₁} > 2`. Mathematically: the hypothesis forces `log q₁ > 0`, hence `q₁ ≥ 2` and `log q₁ ≥ log 2`, so `δ log q₁ = √(δ² log q₁ · log q₁) > √(log 2 · log 2) = log 2`, and multiplying by `r₁ ≥ 1` gives `δ r₁ log q₁ > log 2`.
- Hypotheses: `hδ0 : 0 ≤ δ` (necessary: δ = -1, q₁ = 3, r₁ = 1 satisfies `log 2 < log 3` but `3^{-1} < 2`); `hr₁ : 0 < r₁` (necessary: r₁ = 0 gives `X = 1`); `h1 : log 2 < δ² log q₁` (essentially sharp shape: at δ² log q₁ = log 2 with q₁ = 2, δ = 1, r₁ = 1 one gets X = 2, so strictness is needed for the strict co
- Uses from project: `[]` (only mathlib lemmas)
- Used by: Roth/MainLemma.lean:193 in `Roth.three_small_factors` (`have hX := (two_lt_rpow_aux hδ0 hr₁ (hlog2.trans_le h1)).le`) only; `grep -rn two_lt_rpow_aux Roth/` gives the definition (l.156) and this use. Transitively everything downstream of `three_small_factors`.

### #240 theorem Roth.three_small_factors (public, Roth/MainLemma.lean:180)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Source §6 display (three-small-factors) 2^(m r1), (1+A)^(m r1), (1+|alpha|)^(m r1) all below B_1^delta, stated about the project-only def mainCoeffBound (NO-composable, not upstreamable) under the Roth parameter hypothesis (32); every hypothesis sharp (compiled), no literature standing outside Roth proofs, not a 3-call mathlib composition (needs project sqrt_lt_floor, mul_log_div_two_lt_log_mainCoeffBound, two_lt_rpow_aux plus nlinarith); 3 callers in 2 files, so it is genuine project API but has no mathlib home.
- action: Recommended - keep Roth.three_small_factors project-local in Roth/MainLemma.lean (callers MainLemma l.631, l.656 and Main l.502); no mathlib PR.
- Type: `∀ {δ : ℝ}, 0 ≤ δ → ∀ {m q₁ r₁ : ℕ}, 0 < r₁ → ∀ {A α : ℝ}, 0 ≤ A → 2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log ↑q₁ → 2 ^ (m * r₁) < ↑(mainCoeffBound δ q₁ r₁) ^ δ ∧ (1 + A) ^ (m * r₁) < ↑(mainCoeffBound δ q₁ r₁) ^ δ ∧ (1 + |α|) ^ (m * r₁) < ↑(mainCoeffBound δ q₁ r₁) ^ δ`
- What: With `B₁ = ⌊q₁^{δ r₁}⌋` (`mainCoeffBound`), the non-strict form of the source's parameter condition (32), `2m + 1 + 2m log(1+A) + 2m log(1+|α|) ≤ δ² log q₁`, implies the three bounds `2^{m r₁} < B₁^δ`, `(1+A)^{m r₁} < B₁^δ`, `(1+|α|)^{m r₁} < B₁^δ` (source §6, eq. `roth:three-small-factors`, clean.tex l.1374).
- Hypotheses: `hδ0 : 0 ≤ δ`, `hr₁ : 0 < r₁`, `hA : 0 ≤ A`, `h32` (non-strict (32)). All four are necessary (evidence checks 1–3 for the first three; `h32` is the content).
- Uses from project: `Roth.mainCoeffBound`, `Roth.two_lt_rpow_aux` (private), `Roth.sqrt_lt_floor`, `Roth.mul_log_div_two_lt_log_mainCoeffBound`
- Used by: Roth/MainLemma.lean:631 (`exists_mem_RSet_le_index_of_log_bound_aux`, second conjunct with `α := 0`), Roth/MainLemma.lean:656 (`exists_auxiliary_polynomial_of_log_bound_aux`, first and third conjuncts), Roth/Main.lean:502 (first conjunct). No other uses.

### #241 lemma Roth.exists_norm_coeff_reduction_aux (private, Roth/MainLemma.lean:212)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-step leading-term elimination for modByMonic (deg f in (0, s], Q of degree at most s-1 with coefficient norms at most (1+A)C and the same remainder), the inductive step of norm_coeff_modByMonic_le; mathlib has no coefficient-norm bounds for modByMonic.
- action: Keep as private helper for its single call site Roth/MainLemma.lean:264 (norm_coeff_modByMonic_le); optionally shorten hmod via Polynomial.modByMonic_eq_of_dvd_sub instead of unfolding divModByMonicAux.
- Type: `∀ {R : Type*} [SeminormedRing R] {f P : Polynomial R} {A C : ℝ}, (∀ i, ‖f.coeff i‖ ≤ A) → (∀ i, ‖P.coeff i‖ ≤ C) → ∀ {s : ℕ}, P.natDegree ≤ s → f ≠ 1 → P %ₘ f ≠ P → 0 < f.natDegree ∧ f.natDegree ≤ s ∧ ∃ Q : Polynomial R, Q.natDegree ≤ s - 1 ∧ (∀ i, ‖Q.coeff i‖ ≤ (1 + A) * C) ∧ P %ₘ f = Q %ₘ f`
- What: One step of polynomial long division with coefficient-size control. If f has coefficients of norm at most A, P has coefficients of norm at most C and degree at most s, f is not 1 and reducing P modulo f actually changes P, then f is monic of degree between 1 and s, and subtracting the appropriate multiple f · lc(P) X^{deg P - deg f} gives a polynomial Q of degree at most s - 1 with coefficient norms at most (1 + A) C and the same remainder modulo f.
- Hypotheses: `[SeminormedRing R]` (no commutativity); coefficient bounds `hfA`, `hP`; `hs : P.natDegree ≤ s`; `hf1 : f ≠ 1`; `hself : P %ₘ f ≠ P` (encodes f monic and deg f ≤ deg P, P ≠ 0). Nonnegativity of A, C is derived from the norm bounds at index 0.
- Uses from project: `[]` (only mathlib lemmas)
- Used by: Roth/MainLemma.lean: `norm_coeff_modByMonic_le` (l.264, `obtain ⟨hn, hfs, Q, hQdeg, hQc, hmod⟩ := exists_norm_coeff_reduction_aux hfA hP hs hf1 hself`, the strong-induction step) only — `grep -rn exists_norm_coeff_reduction_aux Roth/` gives the definition and that use. Transitively everything downstream of `norm_coeff_modByMonic_le` (Lemma 9 remainder-coefficient bound in the main lemma).

### #242 theorem Roth.norm_coeff_modByMonic_le (public, Roth/MainLemma.lean:252)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Coefficient-norm bound for the monic remainder over any seminormed ring, ht(P mod f) at most (1+ht f)^(deg P+1-deg f) ht P; standard (arXiv 1401.7696 Lemma 4.5, Roth-Ridout math/0307203), absent from mathlib (only the algebraic analogue coeff_modByMonic_mem_pow_natDegree_mul in CoeffMem), not composable; mathlib form should be stated with Polynomial.supNorm (compiled corollary).
- action: Upstream to Mathlib/Analysis/Polynomial/Norm.lean as Polynomial.supNorm_modByMonic_le (supNorm form, compiled in evidence/checks.lean) plus the coefficientwise form with explicit bounds A C s; keep project lemma (single caller MainLemma l.512) or rewrite that caller via the supNorm form after upstreaming.
- Type: `∀ {R : Type*} [SeminormedRing R] {f : R[X]} {A : ℝ}, (∀ i, ‖f.coeff i‖ ≤ A) → ∀ (P : R[X]) {C : ℝ}, (∀ i, ‖P.coeff i‖ ≤ C) → ∀ {s : ℕ}, P.natDegree ≤ s → ∀ (i : ℕ), ‖(P %ₘ f).coeff i‖ ≤ (1 + A) ^ (s + 1 - f.natDegree) * C`
- What: If every coefficient of f has norm at most A, every coefficient of P has norm at most C, and deg P ≤ s, then every coefficient of the remainder P mod f (mathlib's `modByMonic`) has norm at most (1 + A)^(s + 1 − deg f) · C. No monicity is assumed (for nonmonic f, `modByMonic` returns P and the bound is trivial).
- Hypotheses: `[SeminormedRing R]` (no commutativity, no monicity); `hfA` coefficient bound for f; `hP` coefficient bound for P; `hs : P.natDegree ≤ s`. Nonnegativity of A, C is derived.
- Uses from project: `Roth.exists_norm_coeff_reduction_aux` (private)
- Used by: Roth/MainLemma.lean:512 (`abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, private, `norm_coeff_modByMonic_le (by simpa [Int.norm_eq_abs] using hA) _ ... i`); also listed in the module docstring (MainLemma l.41). `grep -rn norm_coeff_modByMonic_le Roth/` finds no other use.

### #243 def Roth.boxFamily (public, Roth/MainLemma.lean:275)
- verdict: NO-composable-from-mathlib | cost: CHEAP | junk: KEEP
- rationale: boxFamily r B is MvPolynomial.restrictSupport ℤ {d with d j ≤ r j for all j} intersected with the coefficient box Icc 0 B (one-line ext proof in evidence; restrictDegree for constant r); mathlib already has the univariate analogue Polynomial.boxPoly with ncard_boxPoly in Mathlib/NumberTheory/MahlerMeasure.lean, so the def itself is a project-local name for a mathlib composition.
- action: Keep boxFamily as a project-local abbreviation for the Lemma 9 family (used in Roth/MainLemma.lean:361-601), optionally restating its body via MvPolynomial.restrictSupport; do not upstream the def; re-aim any upstreaming of boxFamily_finite/ncard_boxFamily at a multivariate generalisation of Polynomial.boxPoly/ncard_boxPoly (support in a finite set S of monomials, coefficients in per-monomial intervals).
- Type: `{σ : Type*} → (r : σ → ℕ) → (B : ℕ) → Set (MvPolynomial σ ℤ)`
- What: The set `𝒲` of integer polynomials `W` with `degreeOf j W ≤ r j` for every variable `j` and every coefficient in `[0, B]`.
- Hypotheses: none (no finiteness on `σ`; finiteness enters only in `boxFamily_finite`/`ncard_boxFamily` via `[Finite (Function.support r)]`).
- Uses from project: `[]` (only mathlib `MvPolynomial.degreeOf`, `MvPolynomial.coeff`)
- Used by: Roth/MainLemma.lean: private `boxFamily_eq_image_finsupp_aux` (l.281), `boxFamily_finite` (l.302), `ncard_boxFamily` (l.313), statements/proofs at l.361, 364, 367, 368, 373 (`pigeonhole_count`), l.389 (`exists_ne_modByMonic_eq`), l.552, l.601 (main Lemma 9 construction); module docstring l.35. No uses outside Roth/MainLemma.lean.

### #244 lemma Roth.boxFamily_eq_image_finsupp_aux (private, Roth/MainLemma.lean:280)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private set identity rewriting boxFamily r B as the ofCoeff-image of Finset.finsupp over the monomial box Iic r with coefficient range Icc 0 B; shared step of boxFamily_finite and ncard_boxFamily, with no mathlib counterpart (mathlib's univariate ncard_boxPoly uses an ad hoc toFn/ofFn bijection instead).
- action: Keep as private helper for boxFamily_finite (Roth/MainLemma.lean:304) and ncard_boxFamily (Roth/MainLemma.lean:313); optionally turn the plain comment at l.278 into an accurate docstring and drop the redundant `classical` at l.284; revisit only if a multivariate boxPoly generalisation is upstreamed (then this becomes its card/finite proof step).
- Type: `∀ {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ), boxFamily r B = AddMonoidAlgebra.ofCoeff '' ↑((Finset.Iic (Finsupp.ofSupportFinite r (Set.toFinite _))).finsupp fun _ ↦ Finset.Icc (0 : ℤ) B)` (declared `private lemma` under `open scoped Classical in`; the image lives in `Set ((σ →₀ ℕ) →₀ ℤ)` coerced to `MvPolynomial σ ℤ`).
- What: The box family (integer polynomials with `degreeOf j W ≤ r j` for all `j` and all coefficients in `[0, B]`) equals the set of polynomials whose coefficient function is a finitely supported map supported in the monomial box `{d : d ≤ r}` (as `Finset.Iic` of `r` viewed as a finsupp) with values in `Icc 0 B`; i.e. the box family is the image of the finite set `Finset.finsupp (Iic r) (fun _ ↦ Icc 0 B)` under the coefficient-to-polynomial map.
- Hypotheses: `[Finite (Function.support r)]` is needed to form `Finsupp.ofSupportFinite r` and hence the finite box `Finset.Iic`; without it `boxFamily r B` can be infinite (e.g. `σ = ℕ`, `r = 1`, `B = 1`), so no finset image exists. No other hypotheses. All used.
- Uses from project: `Roth.boxFamily` (Roth/MainLemma.lean:275).
- Used by: Roth/MainLemma.lean only: `Roth.boxFamily_finite` (l.304, `rw`) and `Roth.ncard_boxFamily` (l.313, `rw` before `Set.ncard_image_of_injective` / `Finset.card_finsupp`). `grep -rn boxFamily_eq_image_finsupp_aux Roth/` returns only the declaration and these two uses.

### #245 theorem Roth.boxFamily_finite (public, Roth/MainLemma.lean:301)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Re-aimed per Roth.boxFamily at the general statement that polynomials with support in a finite monomial set S and coefficients in a finite set U form a finite set (any CommSemiring R); this is absent from mathlib, which re-derives the univariate case inline in Polynomial.bUnion_roots_finite and via ncard in the Northcott proof; the general lemma compiles and boxFamily_finite is a 3-line corollary (evidence).
- action: Upstream MvPolynomial.finite_setOf_support_subset_coeff_mem (and the Polynomial natDegree analogue) to Mathlib/RingTheory/MvPolynomial/Basic.lean next to restrictSupport, refactoring Polynomial.bUnion_roots_finite (Mathlib/Algebra/Polynomial/Roots.lean:622) to use it; locally keep boxFamily_finite (one call site Roth/MainLemma.lean:367) and re-prove it from the general lemma once available.
- Type: `∀ {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ), (boxFamily r B).Finite`
- What: The family `𝒲` of integer polynomials with `degreeOf j W ≤ r j` for all `j` and all coefficients in `[0, B]` is finite, provided only finitely many degree bounds `r j` are nonzero (σ may be infinite).
- Hypotheses: `[Finite (Function.support r)]` (needed: with infinitely many positive `r j` the family is infinite).
- Uses from project: `Roth.boxFamily`, `Roth.boxFamily_eq_image_finsupp_aux` (private)
- Used by: Roth/MainLemma.lean:367 (`exists_ne_modByMonic_eq`, to build `Fintype (boxFamily r B)`). No other uses in `Roth/`.

### #246 theorem Roth.ncard_boxFamily (public, Roth/MainLemma.lean:311)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Re-aimed per Roth.boxFamily at the multivariate generalisation of Polynomial.ncard_boxPoly - the number of polynomials with support in a finite monomial set S and coeff d in a finite set U d is the product of the card of U d over S (any CommSemiring R), with the integer-interval form as corollary; absent from mathlib, compiles in evidence, and ncard_boxFamily follows from it.
- action: Upstream MvPolynomial.ncard_setOf_support_subset_coeff_mem (plus the Icc corollary) to Mathlib/RingTheory/MvPolynomial/Basic.lean next to restrictSupport, grouped with the finiteness lemma from Roth.boxFamily_finite, and consider re-proving Polynomial.ncard_boxPoly (Mathlib/NumberTheory/MahlerMeasure.lean:57) from a univariate analogue; locally keep ncard_boxFamily (one call site Roth/MainLemma.lean:373) and re-derive it from the general lemma.
- Type: `∀ {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ), (boxFamily r B).ncard = (B + 1) ^ ∏ᶠ j, (r j + 1)`
- What: The family `𝒲` of integer polynomials with `degreeOf j W ≤ r j` and all coefficients in `[0, B]` has exactly `(B+1)^N` elements, `N = ∏ᶠ j, (r j + 1)` the number of monomials in the box `d ≤ r`.
- Hypotheses: `[Finite (Function.support r)]` (needed: otherwise the box of monomials is infinite and `ncard` is junk 0).
- Uses from project: `Roth.boxFamily`, `Roth.boxFamily_eq_image_finsupp_aux` (private)
- Used by: Roth/MainLemma.lean:373 (`exists_ne_modByMonic_eq`, in the `simpa` computing `Fintype.card` of the box family for the pigeonhole); mentioned in the module docstring l.43. No other uses in `Roth/`.

### #247 lemma Roth.floor_rpow_count_lt_aux (private, Roth/MainLemma.lean:320)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private one-use real inequality 2⌊x^c⌋+1 < (x+1)^(2c) for x>0, c≥1, the per-factor bound inside pigeonhole_count; proved via Real.add_rpow_le_rpow_add, Real.rpow_mul and nlinarith; too specific for mathlib, which has no such lemma.
- action: Keep as private helper for its single call site Roth/MainLemma.lean:343 (pigeonhole_count, first calc step); no change.
- Type: `∀ {x c : ℝ}, 0 < x → 1 ≤ c → ((2 * ⌊x ^ c⌋₊ + 1 : ℕ) : ℝ) < (x + 1) ^ (2 * c)`
- What: For real x > 0 and real exponent c ≥ 1, the number 2⌊x^c⌋ + 1 (the count of integers in [-⌊x^c⌋, ⌊x^c⌋]) is strictly less than (x + 1)^(2c).
- Hypotheses: `0 < x` (needed: at x = 0 the claim reads 1 < 1); `1 ≤ c` (needed: at c = 0 the claim reads 3 < 1, and superadditivity of t^c fails for c < 1).
- Uses from project: `[]` (only mathlib lemmas: `Real.rpow_pos_of_pos`, `Real.add_rpow_le_rpow_add`, `Real.rpow_mul`, `Real.rpow_two`, `pow_le_pow_left₀`, `sq_pos_of_pos`, `Nat.floor_le`).
- Used by: Roth/MainLemma.lean:343 `Roth.pigeonhole_count` (first `calc` step, via `pow_lt_pow_left₀`) only; `grep -rn floor_rpow_count_lt_aux Roth/` gives the definition (l.320) and that use. Transitively `pigeonhole_count` is used at Roth/MainLemma.lean:615 (Lemma 9 construction).

### #248 theorem Roth.pigeonhole_count (public, Roth/MainLemma.lean:334)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Ad-hoc counting inequality (2 natfloor(B^c)+1)^(nD) < (B+1)^N under B > 0, c at least 1, N > 0, c n D at most N/2 from the Lemma 9 pigeonhole (source §6); all four hypotheses necessary (compiled counterexamples) and already weaker than the source's B_1 > 1, c > 1; no literature standing, no mathlib counterpart (mathlib's own Siegel lemma keeps its analogous count card_S_lt_card_T private), not a 3-call composition; recommended resolution is keep project-local.
- action: Keep Roth.pigeonhole_count in Roth/MainLemma.lean (single caller, private exists_mem_RSet_le_index_of_rpow_bound_aux at l.615); optionally make it private together with floor_rpow_count_lt_aux; no mathlib PR.
- Type: `∀ {B : ℝ}, 0 < B → ∀ {c : ℝ}, 1 ≤ c → ∀ {n D N : ℕ}, 0 < N → c * ↑n * ↑D ≤ ↑N / 2 → ((2 * ⌊B ^ c⌋₊ + 1 : ℕ) : ℝ) ^ (n * D) < (B + 1) ^ N`
- What: For real `B > 0`, real `c ≥ 1`, naturals `n, D, N` with `N > 0` and `c n D ≤ N/2`, the number of remainder tuples `(2⌊B^c⌋ + 1)^{nD}` is strictly less than `(B + 1)^N` (the size of the box family when `B` is a natural number).
- Hypotheses: `hB : 0 < B` (necessary, fails at `B = 0`); `hc : 1 ≤ c` (cannot be dropped, fails at `c = 1/2`; not sharp, any valid threshold exceeds `log 3 / log 4`); `hN : 0 < N` (necessary, fails at `n = D = N = 0`); `hD : c n D ≤ N / 2` (necessary). All checked in the evidence file.
- Uses from project: `Roth.floor_rpow_count_lt_aux` (private)
- Used by: Roth/MainLemma.lean:615 (private `exists_mem_RSet_le_index_of_rpow_bound_aux`, supplying the `hcount` argument of `exists_mem_RSet_le_index_aux`); listed in the module docstring l.43. No other uses in `Roth/`.

### #249 theorem Roth.exists_ne_modByMonic_eq (public, Roth/MainLemma.lean:359)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Pigeonhole step of Lemma 9 (two distinct box polynomials with equal monic remainders of all selected diagonal Hasse derivatives); a 15-line application of Fintype.exists_ne_map_eq_of_card_lt plus ncard_boxFamily and sum_modByMonic_coeff; the Hasse/diag/box content is incidental (abstract form over any finite pigeon set compiles and implies it in 3 lines) but even the abstract form has no literature standing and mathlib precedent (SiegelsLemma, AdmissibleCardPowDegree) keeps such pigeonhole applications inline or local.
- action: Keep in Roth/MainLemma.lean (single caller, private exists_mem_RSet_le_index_aux at l.557); optionally restate it as the compiled abstract corollary of exists_ne_forall_modByMonic_eq (evidence/abstract.lean) or make it private; no mathlib PR.
- Type: `∀ {σ : Type u_1} (r : σ → ℕ) [Finite ↑(Function.support r)] (B : ℕ) {f : ℤ[X]}, f.Monic → ∀ (J : Finset (σ →₀ ℕ)) (C : ℕ), (∀ W ∈ boxFamily r B, ∀ j ∈ J, ∀ i < f.natDegree, |(diag (hasseDeriv j W) %ₘ f).coeff i| ≤ ↑C) → ↑(2 * C + 1) ^ (f.natDegree * J.card) < (↑B + 1) ^ ∏ᶠ j, (r j + 1) → ∃ W' ∈ boxFamily r B, ∃ W'' ∈ boxFamily r B, W' ≠ W'' ∧ ∀ j ∈ J, diag (hasseDeriv j W') %ₘ f = diag (hasseDeri
- What: If every member `W` of the box family `𝒲` (degree box `r`, coefficients in `[0, B]`) has all diagonal Hasse remainders `Δ_j W(x,…,x) mod f`, `j ∈ J`, with low coefficients bounded by `C`, and `(2C+1)^{deg f · |J|} < (B+1)^{∏(r_j+1)} = |𝒲|`, then two distinct `W', W'' ∈ 𝒲` have identical remainders for every `j ∈ J`.
- Hypotheses: `[Finite (Function.support r)]` (needed for `boxFamily_finite`/`ncard_boxFamily`); `hf : f.Monic` (needed: without it `%ₘ` is the identity and bounding coefficients below `natDegree f` does not determine the polynomial; e.g. one variable, `r = 1`, `B = 1`, `f = 2X`, `J = {0}`, `C = 1` satisfies `hC`
- Uses from project: `Roth.boxFamily`, `Roth.boxFamily_finite`, `Roth.ncard_boxFamily`, `Roth.diag`, `MvPolynomial.hasseDeriv`
- Used by: Roth/MainLemma.lean:557 (private `exists_mem_RSet_le_index_aux`); listed in the module docstring l.43. No other uses in `Roth/`.

### #250 theorem Roth.sub_mem_RSet (public, Roth/MainLemma.lean:388)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: The difference of two distinct boxFamily members lies in RSet B r; the proof is an anonymous constructor of three mathlib facts (sub_ne_zero, MvPolynomial.degreeOf_sub_le, abs_sub_le_of_nonneg_of_le) about two project-local sets that are themselves NO-composable, and mathlib's own Siegel lemma inlines the identical step, so nothing to upstream.
- action: Do not upstream; keep in Roth/MainLemma.lean as the named Lemma 9 step (sole caller exists_mem_RSet_le_index_aux at Roth/MainLemma.lean:560), or optionally inline the three-term composition there; no mathlib PR.
- Type: `∀ {σ : Type*} {r : σ → ℕ} {B : ℕ} {W' W'' : MvPolynomial σ ℤ}, W' ∈ Roth.boxFamily r B → W'' ∈ Roth.boxFamily r B → W' ≠ W'' → W' - W'' ∈ Roth.RSet (↑B) r`
- What: If `W'` and `W''` are distinct members of the family `𝒲` (degree at most `r j` in each variable `X j`, every coefficient in `[0, B]`), then `W' - W''` is nonzero, still has degree at most `r j` in each variable, and has every coefficient of absolute value at most `B`; that is, it lies in `ℛ(B; r)`.
- Hypotheses: `h' : W' ∈ boxFamily r B`, `h'' : W'' ∈ boxFamily r B`, `hne : W' ≠ W''`. No finiteness of `σ` or of the support of `r`.
- Uses from project: `Roth.boxFamily`, `Roth.RSet`
- Used by: `Roth.exists_mem_RSet_le_index_aux` (private, Roth/MainLemma.lean:560). No other uses in `Roth/`.

### #251 theorem Roth.eval_hasseDeriv_sub_eq_zero (public, Roth/MainLemma.lean:402)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: Congruence of diagonalised Hasse derivatives mod f gives vanishing of the derivative of W' - W'' at (alpha, ..., alpha); the content is the mathlib triple dvd_modByMonic_iff_dvd + sub_modByMonic + aeval_eq_zero_of_dvd_aeval_eq_zero plus a simp unfolding of the project-local diag and hasseDeriv_map, single caller, Roth-specific shape, nothing to upstream.
- action: Do not upstream; keep in Roth/MainLemma.lean as the named Lemma 9 step (sole caller exists_mem_RSet_le_index_aux at Roth/MainLemma.lean:567) or optionally inline its two-step proof there; no mathlib PR.
- Type: `∀ {σ : Type*} {S : Type*} [CommRing S] {f : Polynomial ℤ} {α : S}, Polynomial.aeval α f = 0 → ∀ {W' W'' : MvPolynomial σ ℤ} {j : σ →₀ ℕ}, Roth.diag (hasseDeriv j W') %ₘ f = Roth.diag (hasseDeriv j W'') %ₘ f → MvPolynomial.eval (fun _ ↦ α) (hasseDeriv j (MvPolynomial.map (Int.castRingHom S) (W' - W''))) = 0`
- What: If `f(α) = 0` and the diagonal substitutions `Δ_j W'(x, …, x)` and `Δ_j W''(x, …, x)` have the same remainder modulo `f`, then the Hasse derivative `Δ_j (W' - W'')`, with coefficients pushed into `S`, vanishes at the diagonal point `(α, …, α)`.
- Hypotheses: `hfα : aeval α f = 0`; `h` congruence of remainders. No monicity of `f` (`%ₘ` is used, but `dvd_modByMonic_iff_dvd` holds for any `f`), no finiteness of `σ`.
- Uses from project: `Roth.diag`, `Roth.diag_sub`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`
- Used by: `Roth.exists_mem_RSet_le_index_aux` (private, Roth/MainLemma.lean:567). No other uses in `Roth/`.

### #252 theorem Roth.le_index_of_forall_eval_eq_zero (public, Roth/MainLemma.lean:419)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: Vanishing of all box Hasse derivatives of weight below c gives c at most the index; it is le_index_iff.2 plus hasseDeriv_eq_zero_of_degreeOf_lt (compiled re-proof), the box-free form is the analogue of mathlib MvPowerSeries.le_weightedOrder, hP and hd both necessary (compiled counterexamples), single caller, nothing new for mathlib.
- action: Keep in Roth/MainLemma.lean as the named Lemma 9 step (sole caller exists_mem_RSet_le_index_aux at Roth/MainLemma.lean:562), optionally move next to le_index_iff in Roth/Index.lean; no mathlib PR.
- Type: `{σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hd : ∀ j, degreeOf j P ≤ r j) (α : σ → ℝ) {c : ℝ} (hvan : ∀ d, (∀ j, d j ≤ r j) → weight r d < c → eval α (hasseDeriv d P) = 0) : c ≤ index P α r`
- What: For a nonzero real polynomial `P` with `deg_{x_j} P ≤ r_j` for all `j`, if every Hasse derivative `Δ_d P` with `d` in the box `d ≤ r` and weight `∑ d_j/r_j < c` vanishes at `α`, then the index of `P` at `α` relative to `r` is at least `c`.
- Hypotheses: `hP : P ≠ 0` (needed by `le_index_iff`, junk `index 0 = 0`; necessary, evidence (2)); `hd` coordinate degree bounds (restrict the check to the box; necessary, evidence (3)); `hvan` the vanishing hypothesis. No positivity of `r`.
- Uses from project: `Roth.index`, `Roth.weight`, `Roth.le_index_iff`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`
- Used by: `Roth.exists_mem_RSet_le_index_aux` (private, Roth/MainLemma.lean:562). No other uses in `Roth/`.

### #253 theorem Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul (public, Roth/MainLemma.lean:433)
- verdict: SKIP | cost: n/a | junk: REMOVE
- rationale: Dead code - no caller anywhere in the project since commit 6c41716 replaced its only use with an inline variant (weak delta*m at most 1, conclusion at most L) at MainLemma l.681 that this strict statement cannot serve; a one-off ordered-field arithmetic step with no literature or mathlib standing, so Step 8 REMOVE triggers the Step 9a pre-filter.
- action: Delete Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul from Roth/MainLemma.lean (l.426-443, no call sites to update); optional alternative - restate it as the non-strict variant (delta*m at most 1 and 2m+1 at most delta^2 L give m(2m+1)/delta at most L) and use it for the have hq inside theta_lt_eta_of_sq_log_bound_aux (MainLemma l.681); either way project-local, no mathlib PR.
- Type: `∀ {K : Type*} [Semifield K] [LinearOrder K] [IsStrictOrderedRing K] [ExistsAddOfLE K] {δ m L : K}, 0 < 2 * m + 1 → δ * m < 1 → 2 * m + 1 ≤ δ ^ 2 * L → m * (2 * m + 1) / δ < L`
- What: In a linearly ordered semifield, from `0 < 2m+1`, `δm < 1` and `2m+1 ≤ δ²L`, deduce `m(2m+1)/δ < L`. With `L = log q₁` this is the source's Lemma `lem:lem7-satisfied` ("verify δ log q₁ > m(2m+1)", from (29) and (32)), i.e. the hypothesis of Lemma 7.
- Hypotheses: `hm : 0 < 2m+1` (positivity of the factor), `hδm : δm < 1` (strict, from (29) `δ < 1/m` style bound), `h32 : 2m+1 ≤ δ²L` (weak form of (32)).
- Uses from project: `[]`
- Used by: unused in project (grep of `Roth/`, `Roth.lean`, `Main.lean` and the whole repo outside `.lake`/`.mathlib-quality`: only the definition at Roth/MainLemma.lean:433 and an inventory heading in PROJECT_OVERVIEW.md). Its former caller (as `lem7_hyp_of_h32 (K := ℝ)`) was removed in commit 6c41716 ("Simplify Roth main lemma and weaken its hypotheses"); the needed bound is now re-derived inline as `have 

### #254 theorem Roth.exists_hasseDeriv_eval_ne_zero (public, Roth/MainLemma.lean:454)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: Strict-cutoff form of index attainment, one Exists.imp on exists_weight_eq_index or the contrapositive of le_index_iff (both compiled); its weighted-order analogue is the one-line contrapositive of MvPowerSeries.le_weightedOrder (compiled); hP necessary (compiled); nothing new for mathlib.
- action: Keep project-local (sole caller exists_hasseDeriv_index_eval_bound_aux at Roth/MainLemma.lean:486), optionally move beside exists_weight_eq_index in Roth/Index.lean; no mathlib PR.
- Type: `{σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) {c : ℝ} (hc : index P α r < c) : ∃ k : σ →₀ ℕ, weight r k < c ∧ eval α (hasseDeriv k P) ≠ 0`
- What: If a nonzero real polynomial `P` has index `< c` at `α` relative to `r`, then some Hasse derivative `Δ_k P` with weight `∑ k_j/r_j < c` does not vanish at `α`.
- Hypotheses: `hP : P ≠ 0` (necessary: junk value `index 0 = 0`, evidence (3)); `hc : index P α r < c` strict cutoff. No positivity on `r`, any finite `σ`.
- Uses from project: `Roth.index`, `Roth.weight`, `Roth.exists_weight_eq_index`, `MvPolynomial.hasseDeriv`
- Used by: `Roth.exists_hasseDeriv_index_eval_bound_aux` (private, Roth/MainLemma.lean:486). No other uses in `Roth/`.

### #255 lemma Roth.abs_eval_iterated_hasseDeriv_lt_aux (private, Roth/MainLemma.lean:459)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private Lemma 9 value estimate for a doubly Hasse-differentiated integer polynomial at the diagonal point, chaining abs_coeff_hasseDeriv_le twice into abs_eval_le and absorbing 2^s and (1+|alpha|)^s into beta; used once; mathlib has no multivariate Hasse derivative.
- action: Keep as private helper of its single call site Roth/MainLemma.lean:668 (exists_auxiliary_polynomial_of_log_bound_aux); no change.
- Type: `∀ {σ : Type*} [Fintype σ] {P : MvPolynomial σ ℤ} {r : σ → ℕ} {B α β : ℝ} {s : ℕ}, (∀ j, degreeOf j P ≤ r j) → 0 < B → ∑ j, r j ≤ s → (2 : ℝ) ^ s < β → (1 + |α|) ^ s ≤ β → (∀ d, |(P.coeff d : ℝ)| ≤ B) → ∀ i k : σ →₀ ℕ, |eval (fun _ ↦ α) (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))| < β * (β * B) * β`
- What: If an integer polynomial P has coordinate degrees deg_{X_j} P ≤ r_j and all coefficients bounded by B > 0, and β exceeds both 2^s and (1+|α|)^s where s ≥ ∑ r_j, then every iterated Hasse derivative Δ_i Δ_k P, evaluated at the diagonal point (α, …, α), has absolute value < β·(β·B)·β, i.e. < B·β³. This is the "|(Δ_i Q)(α, …, α)| < B^{1+3δ}" estimate of §6, Lemma 9, with β = B^δ.
- Hypotheses: `hP` (coordinate degree bounds; needed for the 2^{∑r} binomial bound and the evaluation bound), `hB : 0 < B` (needed for strictness: with P = 0, B = 0 the conclusion 0 < 0 fails), `hs` (lets the caller use the uniform exponent s = m·r₁), `h2` strict (gives the strict inequality), `hα` (non-strict su
- Uses from project: `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean), `MvPolynomial.degreeOf_hasseDeriv_le` (Roth/HasseDeriv.lean:210), `Roth.abs_eval_le` (Roth/CoeffNorm.lean:223), `Roth.abs_coeff_hasseDeriv_le` (Roth/CoeffNorm.lean:134).
- Used by: Roth/MainLemma.lean:668 `exists_auxiliary_polynomial_of_log_bound_aux` (private), as the last conjunct `∀ i k, |…| < B^{1+3δ}` after `trans_eq` with `hpow : B^{1+3δ} = B·β³`; `grep -rn abs_eval_iterated_hasseDeriv_lt_aux Roth/` gives only the definition (l.459) and that use.

### #256 lemma Roth.exists_hasseDeriv_index_eval_bound_aux (private, Roth/MainLemma.lean:477)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private final step of Lemma 9 that passes from the auxiliary polynomial W to a nonvanishing Hasse derivative Q = Delta_k W, transporting degree, index-gap and value bounds across the Int-to-Real coefficient map; used once by main_lemma; mathlib has no multivariate Hasse derivative or index.
- action: Keep as private helper of its single call site Roth/MainLemma.lean:752 (main_lemma); no change.
- Type: `∀ {σ : Type*} [Fintype σ] {P : MvPolynomial σ ℤ} {r : σ → ℕ} {α z : σ → ℝ} {C γ c : ℝ}, P ≠ 0 → (∀ j, degreeOf j P ≤ r j) → (∀ i k : σ →₀ ℕ, |eval α (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))| < C) → γ ≤ index (map (Int.castRingHom ℝ) P) α r → index (map (Int.castRingHom ℝ) P) z r < c → ∃ Q : MvPolynomial σ ℤ, Q ≠ 0 ∧ (∀ j, degreeOf j Q ≤ r j) ∧ γ - c < index (map (Int.castRingHom 
- What: Let P be a nonzero integer polynomial with deg_{X_j} P ≤ r_j, whose iterated Hasse derivatives Δ_i Δ_k P all have absolute value < C at α. If the index of P at α is at least γ and the index of P at z is less than c, then there is a nonzero integer polynomial Q (namely Q = Δ_k P for a suitable k) with the same degree bounds, index at α greater than γ − c, Q(z) ≠ 0, and |Δ_i Q (α)| < C for every i. This is the closing step of §6, proof of Lemma 9: "W* has some derivative Q = Δ_k W* with ∑ k_j/r_j 
- Hypotheses: `hP` (needed so the real image is nonzero, required by `exists_hasseDeriv_eval_ne_zero`), `hd` (propagated to the degree conjunct), `hbound` (propagated to the value conjunct; the double-derivative form is exactly what the caller's `exists_auxiliary_polynomial_with_index_gap_aux` provides), `hγ` and
- Uses from project: `Roth.exists_hasseDeriv_eval_ne_zero` (Roth/MainLemma.lean:454; assessed NO-composable-from-mathlib), `Roth.index_sub_weight_le_index_hasseDeriv` (Roth/Index.lean:109), `Roth.index` (Roth/Index.lean:58), `Roth.weight` (Roth/Box.lean:71, implicit through `hkw`), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean), `MvPolynomial.hasseDeriv_map` (Roth/HasseDeriv.lean:134), `MvPolynomial.degreeOf_hasseDe
- Used by: Roth/MainLemma.lean:752 `Roth.main_lemma` (public, Lemma 9), with γ := gam − eta + c, c := (index W − (gam − eta) + Θ)/2, z := (h_j/q_j)_j, closed by `simpa only [add_sub_cancel_right]`. `grep -rn exists_hasseDeriv_index_eval_bound Roth/` gives only the definition (l.477) and that use.

### #257 lemma Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux (private, Roth/MainLemma.lean:497)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private Lemma 9 bookkeeping step chaining the Hasse-derivative, diagonal-substitution and modByMonic coefficient bounds into one explicit remainder bound; used once by the floor variant; mathlib has no multivariate Hasse derivative, no diag map and no modByMonic coefficient bound.
- action: Keep as private helper of its single call site Roth/MainLemma.lean:533 (abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux, inside its local bound); no change.
- Type: `∀ {σ : Type*} [Fintype σ] {f : Polynomial ℤ} {P : MvPolynomial σ ℤ} {r : σ → ℕ} {A B : ℝ}, (∀ i, |(f.coeff i : ℝ)| ≤ A) → (∀ k, degreeOf k P ≤ r k) → (∀ d, |(P.coeff d : ℝ)| ≤ B) → ∀ (j : σ →₀ ℕ) (i : ℕ), |((diag (hasseDeriv j P) %ₘ f).coeff i : ℝ)| ≤ (1 + A) ^ ((∑ k, r k) + 1 - f.natDegree) * (((∏ k, (r k + 1) : ℕ) : ℝ) * (2 ^ (∑ k, r k) * B))`
- What: Let f be an integer polynomial with coefficients of absolute value at most A, and P an integer polynomial in the variables X_k (k ∈ σ) with deg_{X_k} P ≤ r_k and coefficients of absolute value at most B. For every multi-index j, every coefficient of the remainder of the diagonal substitution Δ_j P(x, …, x) on division by f (Lean `modByMonic`) has absolute value at most (1 + A)^{∑ r_k + 1 − deg f} · ∏_k (r_k + 1) · 2^{∑ r_k} · B. This is the explicit remainder bound of §6, proof of Lemma 9: abc(Δ
- Hypotheses: `hA` (coefficient bound for the divisor, fed to `norm_coeff_modByMonic_le`), `hd` (degree bounds, needed by `abs_coeff_hasseDeriv_le`, the support count and `natDegree_diag_le`), `hc` (coefficient bound for P, also gives `0 ≤ B`). No monicity of f is required (for nonmonic f, `modByMonic` returns th
- Uses from project: `Roth.diag` (Roth/CoeffNorm.lean:161), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean), `MvPolynomial.degreeOf_hasseDeriv_le` (Roth/HasseDeriv.lean:210), `Roth.card_le_card_box` (Roth/Box.lean:65), `Roth.abs_coeff_diag_le` (Roth/CoeffNorm.lean:174), `Roth.abs_coeff_hasseDeriv_le` (Roth/CoeffNorm.lean:134), `Roth.natDegree_diag_le` (Roth/CoeffNorm.lean:183), `Roth.norm_coeff_modByMonic_le` (Roth/M
- Used by: Roth/MainLemma.lean:533 `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` (private, l.515), inside its local `bound` helper (first `calc` step), applied both to f and, in the nonmonic degree-zero case, to g := 0. Transitively: floor_aux → `exists_mem_RSet_le_index_of_rpow_bound_aux` (l.581, use at l.606) → `exists_mem_RSet_le_index_of_log_bound_aux` (l.618) → `exists_auxiliary_polynomial_of

### #258 lemma Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux (private, Roth/MainLemma.lean:515)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private Lemma 9 bookkeeping step absorbing the explicit remainder bound of abs_coeff_diag_hasseDeriv_modByMonic_le_aux into the integer cutoff floor(B beta^3) used by the Siegel counting step; single call site; Roth-specific, nothing in mathlib.
- action: Keep as private helper of its single call site Roth/MainLemma.lean:606 (exists_mem_RSet_le_index_of_rpow_bound_aux, inside hC); no change.
- Type: `∀ {σ : Type*} [Fintype σ] {f : Polynomial ℤ} {P : MvPolynomial σ ℤ} {r : σ → ℕ} {A B β : ℝ} {s : ℕ}, (∀ i, |(f.coeff i : ℝ)| ≤ A) → (∀ k, degreeOf k P ≤ r k) → (∀ d, |(P.coeff d : ℝ)| ≤ B) → ∑ k, r k ≤ s → 2 ^ s ≤ β → (1 + A) ^ s ≤ β → ∀ (j : σ →₀ ℕ) (i : ℕ), |(diag (hasseDeriv j P) %ₘ f).coeff i| ≤ (⌊B * β ^ 3⌋₊ : ℤ)`
- What: Let f be an integer polynomial with coefficients bounded in absolute value by A, and P an integer polynomial in variables X_k (k ∈ σ) with deg_{X_k} P ≤ r_k and coefficients bounded by B. If ∑ r_k ≤ s, 2^s ≤ β and (1 + A)^s ≤ β, then for every multi-index j every coefficient of the remainder of the diagonal substitution Δ_j P(x, …, x) on division by f (Lean `modByMonic`) is an integer of absolute value at most ⌊B β³⌋. This is the crude form of the remainder bound in §6, proof of Lemma 9: each of
- Hypotheses: `hA` (divisor coefficient bound; also gives 0 ≤ A for the exponent step), `hd` (degree bounds, passed to the `_aux` lemma), `hc` (coefficient bound for P; gives 0 ≤ B), `hs` (links ∑ r_k to s), `h2` (gives β ≥ 1 and absorbs 2^{∑ r_k} and ∏ (r_k+1)), `hpow` (absorbs the elimination factor in the deg 
- Uses from project: `Roth.diag` (Roth/CoeffNorm.lean:161), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` (Roth/MainLemma.lean:497). All other names are mathlib (`one_le_pow₀`, `pow_le_pow_right₀`, `Finset.prod_pow_eq_pow_sum`, `Finset.prod_le_prod`, `Nat.lt_two_pow_self`, `mul_le_mul`, `mul_le_mul_of_nonneg_right`, `Polynomial.eq_one_of_monic_natDegree_zero`, 
- Used by: Roth/MainLemma.lean:606 `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` (private, l.581), in its `hC` step, composed with `Nat.floor_mono hpow` to bound the remainders by ⌊B^c⌋₊. Transitively: → `exists_mem_RSet_le_index_of_log_bound_aux` (l.618) → `exists_auxiliary_polynomial_of_log_bound_aux` → `main_lemma`. `grep -rn abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux Roth/` gives only the defi

### #259 lemma Roth.exists_mem_RSet_le_index_aux (private, Roth/MainLemma.lean:550)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private Lemma 9 assembly step (pigeonhole pair W' ne W'' gives W* = W' - W'' in RSet with index at least gamma) chaining four public project lemmas; single call site; Roth-specific, nothing in mathlib.
- action: Keep as private helper of its single call site Roth/MainLemma.lean:613 (exists_mem_RSet_le_index_of_rpow_bound_aux); no change.
- Type: `∀ {σ : Type*} [Fintype σ] {f : Polynomial ℤ} {α : ℝ}, f.Monic → Polynomial.aeval α f = 0 → ∀ (r : σ → ℕ) (B C : ℕ) (J : Finset (σ →₀ ℕ)) {γ : ℝ}, (∀ W ∈ boxFamily r B, ∀ j ∈ J, ∀ i < f.natDegree, |(diag (hasseDeriv j W) %ₘ f).coeff i| ≤ (C : ℤ)) → ((2 * C + 1 : ℕ) : ℝ) ^ (f.natDegree * J.card) < ((B : ℝ) + 1) ^ (∏ k, (r k + 1) : ℕ) → (∀ d, (∀ k, d k ≤ r k) → weight r d < γ → d ∈ J) → ∃ P : MvPoly
- What: Let f be a monic integer polynomial with root α, and 𝒲 the family of integer polynomials in the variables X_k (k ∈ σ) with deg_{X_k} ≤ r_k and coefficients in [0, B]. Suppose that for every W ∈ 𝒲 and every multi-index j ∈ J, the coefficients of the remainder of Δ_j W(x, …, x) on division by f are bounded by C, and that the counting inequality (2C+1)^{deg f · |J|} < (B+1)^{∏(r_k+1)} holds. If J contains every box multi-index of weight < γ, then there is a nonzero integer polynomial P with deg_{X_
- Hypotheses: `hf` (monicity, needed by `exists_ne_modByMonic_eq`), `hfα` (α a root, used by `eval_hasseDeriv_sub_eq_zero`), `hC` and `hcount` (pigeonhole inputs to `exists_ne_modByMonic_eq`), `hJ` (J covers all box multi-indices of weight < γ). All are used; none is redundant.
- Uses from project: `Roth.boxFamily` (Roth/MainLemma.lean:275), `Roth.diag` (Roth/CoeffNorm.lean:161), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.weight` (Roth/Box.lean:71), `Roth.RSet` (Roth/Theta.lean:56), `Roth.index` (Roth/Index.lean:58), `Roth.exists_ne_modByMonic_eq` (Roth/MainLemma.lean:359), `Roth.sub_mem_RSet` (Roth/MainLemma.lean:388), `Roth.le_index_of_forall_eval_eq_zero` (Roth/MainLemma.l
- Used by: Roth/MainLemma.lean:613 `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` (private, l.581), as its final step with C := ⌊B^c⌋₊, J := box multi-indices of weight ≤ (m − 4c·deg f·√m)/2, and `hcount` from `pigeonhole_count`. Transitively: → `exists_mem_RSet_le_index_of_log_bound_aux` → `exists_auxiliary_polynomial_of_log_bound_aux` → `main_lemma`. `grep -rn exists_mem_RSet_le_index_aux Roth/` gives o

### #260 lemma Roth.mul_card_filter_weight_le_aux (private, Roth/MainLemma.lean:569)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private 9-line arithmetic repackaging of Lemma 8 (card_filter_weight_le with lam = 4a sqrt m, multiplied by a, with the a le 0 case handled) into the counting inequality hD of Lemma 9; single call site; Roth-specific, nothing in mathlib.
- action: Keep as private helper of its single call site Roth/MainLemma.lean:612 (exists_mem_RSet_le_index_of_rpow_bound_aux); optional one-line docstring citing Lemma 8/9; no other change.
- Type: `∀ {m : ℕ}, 0 < m → ∀ (r : Fin m → ℕ), (∀ j, 0 < r j) → ∀ (a : ℝ), a * (((box r).filter fun d ↦ weight r d ≤ ((m : ℝ) - 4 * a * √(m : ℝ)) / 2).card : ℝ) ≤ ((∏ j, (r j + 1) : ℕ) : ℝ) / 2`
- What: For m ≥ 1, positive r_1, …, r_m and any real a, let N(a) be the number of multi-indices d with 0 ≤ d_j ≤ r_j and weight ∑ d_j/r_j ≤ (m − 4a√m)/2. Then a · N(a) ≤ ½ ∏ (r_j + 1). For a > 0 this is Lemma 8 of §6 (N ≤ 2√m λ⁻¹ ∏(r_j+1)) with λ = 4a√m, multiplied through by a; for a ≤ 0 the left side is ≤ 0. In the caller a = c·deg f, and the inequality is the counting input "c · deg f · |J| ≤ ½ ∏(r_j+1)" of the Siegel-lemma step of Lemma 9.
- Hypotheses: `hm : 0 < m` (needed: makes √m ≠ 0 for `field_simp`; the statement is false for m = 0, since then the filter is {0} (card 1) while the right side is 1/2, so a = 1 fails); `hr : ∀ j, 0 < r j` (passed to `card_filter_weight_le`, whose report records a compiled counterexample without it); `a` arbitrary
- Uses from project: `Roth.box` (Roth/Box.lean:47), `Roth.weight` (Roth/Box.lean:71), `Roth.card_filter_weight_le` (Roth/Lattice.lean:202). Mathlib names used: `mul_le_mul_of_nonneg_left`, `Real.sqrt_pos`, `Nat.cast_pos`, `mul_nonpos_of_nonpos_of_nonneg`, `le_of_not_gt`, `Nat.cast_nonneg`, tactics `push_cast`, `field_simp`, `ring`, `positivity`.
- Used by: Roth/MainLemma.lean:612 `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` (private, l.581), to produce `hD : c * f.natDegree * J.card ≤ (∏ (r j + 1) : ℕ) / 2` with a := c * f.natDegree (via `simpa [J, mul_assoc]`), which is fed to `pigeonhole_count`. Transitively: → `exists_mem_RSet_le_index_of_log_bound_aux` → … → `main_lemma`. `grep -rn mul_card_filter_weight_le_aux Roth/` gives only l.569 (defi

### #261 lemma Roth.exists_mem_RSet_le_index_of_rpow_bound_aux (private, Roth/MainLemma.lean:581)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private Lemma 9 numeric assembly (C := floor B^c, J := low-weight box indices, counting via pigeonhole_count) feeding exists_mem_RSet_le_index_aux; single call site; Roth-specific, nothing in mathlib.
- action: Keep as private helper of its single call site Roth/MainLemma.lean:639 (exists_mem_RSet_le_index_of_log_bound_aux); optionally add a docstring citing paper section 6 Lemma 9; no other change.
- Type: `∀ {f : Polynomial ℤ} {α A : ℝ}, f.Monic → Polynomial.aeval α f = 0 → (∀ i, |(f.coeff i : ℝ)| ≤ A) → ∀ {m : ℕ}, 0 < m → ∀ (r : Fin m → ℕ), (∀ j, 0 < r j) → ∀ {c β : ℝ} {B s : ℕ}, 0 < B → ∑ j, r j ≤ s → (1 + A) ^ s ≤ β → (B : ℝ) * β ^ 3 ≤ (B : ℝ) ^ c → ∃ P : MvPolynomial (Fin m) ℤ, P ∈ RSet B r ∧ ((m : ℝ) - 4 * c * f.natDegree * √(m : ℝ)) / 2 ≤ index (map (Int.castRingHom ℝ) P) (fun _ ↦ α) r`
- What: Let f be a monic integer polynomial with root α and coefficients bounded in absolute value by A. Let m ≥ 1, r_1, …, r_m ≥ 1 with ∑ r_j ≤ s, let B ≥ 1 be an integer, and let β, c be reals with (1+A)^s ≤ β and B·β³ ≤ B^c. Then there is a nonzero integer polynomial P in X_1, …, X_m with deg_{X_j} P ≤ r_j and coefficients bounded by B (P ∈ RSet B r) whose index at (α, …, α) relative to r is at least (m − 4c·deg f·√m)/2. This is the numerical core of §6, proof of Lemma 9 (the auxiliary polynomial via
- Hypotheses: `hf`, `hfα` (passed to `exists_mem_RSet_le_index_aux`); `hA` (coefficient bound for the remainder estimate, and gives 1 ≤ A); `hm`, `hr` (for `mul_card_filter_weight_le_aux` and to get s > 0); `hB` (B > 0 for `pigeonhole_count` and for the c ≥ 1 argument); `hs`, `hAβ` (remainder estimate and 2^s ≤ β
- Uses from project: `Roth.RSet` (Roth/Theta.lean:56), `Roth.index` (Roth/Index.lean:58), `Roth.boxFamily` (Roth/MainLemma.lean:275), `Roth.diag` (Roth/CoeffNorm.lean:161), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.box` (Roth/Box.lean:47), `Roth.mem_box` (Roth/Box.lean:51), `Roth.weight` (Roth/Box.lean:71), `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` (Roth/MainLemma.lean:515), `Roth.mul_c
- Used by: Roth/MainLemma.lean:639 `Roth.exists_mem_RSet_le_index_of_log_bound_aux` (private, l.619), with B := mainCoeffBound δ q₁ r₁, c := 1 + 3δ, β := B^δ. Transitively: → `exists_auxiliary_polynomial_of_log_bound_aux` → `exists_auxiliary_polynomial_with_index_gap_aux` → main lemma. `grep -rn exists_mem_RSet_le_index_of_rpow_bound_aux Roth/` gives only l.581 (definition) and l.639 (use).

### #262 lemma Roth.exists_mem_RSet_le_index_of_log_bound_aux (private, Roth/MainLemma.lean:618)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private Lemma 9 specialisation (B := mainCoeffBound, c := 1 + 3 delta, beta := B^delta) turning the log hypothesis (32 without the alpha term) into the rpow bound for exists_mem_RSet_le_index_of_rpow_bound_aux; single call site; Roth-specific, nothing in mathlib.
- action: Keep as private helper of its single call site Roth/MainLemma.lean:653 (exists_auxiliary_polynomial_of_log_bound_aux); optionally deduplicate the hpow identity and the 0 < r1 derivation that the caller repeats at l.656-665; no other change.
- Type: `∀ {f : Polynomial ℤ} {α A : ℝ}, f.Monic → Polynomial.aeval α f = 0 → (∀ i, |(f.coeff i : ℝ)| ≤ A) → ∀ {m q₁ r₁ : ℕ}, 0 < m → ∀ (r : Fin m → ℕ), (∀ j, 0 < r j) → ∑ j, r j ≤ m * r₁ → ∀ {δ : ℝ}, 0 ≤ δ → 2 * m + 1 + 2 * m * Real.log (1 + A) ≤ δ ^ 2 * Real.log q₁ → ∃ P : MvPolynomial (Fin m) ℤ, P ∈ RSet (mainCoeffBound δ q₁ r₁) r ∧ gam δ f.natDegree m ≤ index (map (Int.castRingHom ℝ) P) (fun _ ↦ α) r`
- What: Let f be a monic integer polynomial with root α and coefficients bounded in absolute value by A. Let m ≥ 1, r_1, …, r_m ≥ 1 with ∑ r_j ≤ m·r₁, δ ≥ 0, and assume 2m + 1 + 2m·log(1+A) ≤ δ²·log q₁ (the part of the paper's condition (32) not involving α). Then there is a nonzero integer polynomial P in X_1, …, X_m with deg_{X_j} P ≤ r_j and coefficients bounded by B₁ = ⌊q₁^{δ r₁}⌋ (P ∈ RSet B₁ r) whose index at (α, …, α) relative to r is at least γ = (m − 4(1+3δ)·deg f·√m)/2. This is §6, Lemma 9 (au
- Hypotheses: `hf`, `hfα`, `hA`, `hm`, `hr`, `hs` (all passed to `exists_mem_RSet_le_index_of_rpow_bound_aux`; `hA` also gives 1 ≤ A, `hm`/`hr`/`hs` also give r₁ > 0); `hδ0` (for `three_small_factors`, `four_lt_rpow`, and rpow positivity); `hL` (for `three_small_factors` and for 3 ≤ δ² log q₁). All used.
- Uses from project: `Roth.RSet` (Roth/Theta.lean:56), `Roth.mainCoeffBound` (Roth/MainLemma.lean:69), `Roth.gam` (Roth/MainLemma.lean:63), `Roth.lam` (Roth/MainLemma.lean:60), `Roth.index` (Roth/Index.lean:58), `Roth.three_small_factors` (Roth/MainLemma.lean:180), `Roth.four_lt_rpow` (Roth/MainLemma.lean:122), `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` (Roth/MainLemma.lean:581). Mathlib names used: `Polynomial
- Used by: Roth/MainLemma.lean:653 `Roth.exists_auxiliary_polynomial_of_log_bound_aux` (private, l.643), which first weakens its full (32) hypothesis (with the α-term) to this one's `hL`. Transitively → `exists_auxiliary_polynomial_with_index_gap_aux` (l.692) → main lemma. `grep -rn exists_mem_RSet_le_index_of_log_bound_aux Roth/` gives only l.618 (definition) and l.653 (use).

### #263 lemma Roth.exists_auxiliary_polynomial_of_log_bound_aux (private, Roth/MainLemma.lean:643)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private Lemma 9 assembly step adding the Hasse-derivative evaluation bound B1^(1+3 delta) to the auxiliary polynomial from exists_mem_RSet_le_index_of_log_bound_aux under full hypothesis (32); single call site; Roth-specific, nothing in mathlib.
- action: Keep as private helper of its single call site Roth/MainLemma.lean:719 (exists_auxiliary_polynomial_with_index_gap_aux); optionally share the hpow identity and the 0 < r1 derivation duplicated with exists_mem_RSet_le_index_of_log_bound_aux (l.625-637); no other change.
- Type: `∀ {f : Polynomial ℤ} {α A : ℝ}, f.Monic → Polynomial.aeval α f = 0 → (∀ i, |(f.coeff i : ℝ)| ≤ A) → ∀ {m q₁ r₁ : ℕ}, 0 < m → ∀ (r : Fin m → ℕ), (∀ j, 0 < r j) → ∑ j, r j ≤ m * r₁ → ∀ {δ : ℝ}, 0 ≤ δ → 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log q₁ → ∃ P : MvPolynomial (Fin m) ℤ, P ∈ RSet ((q₁ : ℝ) ^ (δ * r₁)) r ∧ gam δ f.natDegree m ≤ index (map (Int.castRi
- What: Let f be a monic integer polynomial with root α and coefficients bounded in absolute value by A; let m ≥ 1, r_1, …, r_m ≥ 1 with ∑ r_j ≤ m·r₁, δ ≥ 0, and assume the paper's condition (32): 2m + 1 + 2m·log(1+A) + 2m·log(1+|α|) ≤ δ²·log q₁. Then there is a nonzero integer polynomial P with deg_{X_j} P ≤ r_j and coefficients bounded by q₁^{δ r₁} (P ∈ RSet), whose index at (α, …, α) relative to r is at least γ = (m − 4(1+3δ)·deg f·√m)/2, and such that every iterated Hasse derivative ∂_i ∂_k P evalua
- Hypotheses: `hf`, `hfα`, `hm`, `hr`, `hs` (passed to `exists_mem_RSet_le_index_of_log_bound_aux`; `hm`/`hr`/`hs` also give r₁ > 0, `hs` also feeds `abs_eval_iterated_hasseDeriv_lt_aux`); `hA` (callee, plus 0 ≤ A for `three_small_factors`); `hδ0` (callee, `three_small_factors`, rpow positivity); `hL` (weakened f
- Uses from project: `Roth.RSet` (Roth/Theta.lean:56), `Roth.gam` (Roth/MainLemma.lean:63), `Roth.mainCoeffBound` (Roth/MainLemma.lean:69), `Roth.index` (Roth/Index.lean:58), `Roth.hasseDeriv` (Roth/HasseDeriv.lean:57, multivariate), `Roth.exists_mem_RSet_le_index_of_log_bound_aux` (Roth/MainLemma.lean:618), `Roth.three_small_factors` (Roth/MainLemma.lean:180), `Roth.abs_eval_iterated_hasseDeriv_lt_aux` (Roth/MainLemm
- Used by: Roth/MainLemma.lean:719 `Roth.exists_auxiliary_polynomial_with_index_gap_aux` (private, l.692), which feeds `Roth.main_lemma` (l.734). `grep -rn exists_auxiliary_polynomial_of_log_bound_aux Roth/` gives only l.643 (definition) and l.719 (use).

### #264 lemma Roth.theta_lt_eta_of_sq_log_bound_aux (private, Roth/MainLemma.lean:671)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private adapter restating Lemma 7 (Roth.Θ_lt) in Lemma 9's hypothesis shape (m with NeZero, delta*m le 1, ratio as r_j/delta le r_i, delta^2 log q_1 bound) with conclusion via eta; single call site; Roth-specific, nothing in mathlib.
- action: Keep as private helper of its single call site Roth/MainLemma.lean:724 (exists_auxiliary_polynomial_with_index_gap_aux); optionally add a docstring citing Lemma 7 / eqs. (31)-(33); no other change.
- Type: `∀ {m : ℕ} [NeZero m] {δ : ℝ}, 0 ≤ δ → δ * (m : ℝ) ≤ 1 → ∀ {r q : Fin m → ℕ}, 3 ≤ r (Fin.rev 0) → (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ ≤ r i) → 2 * (m : ℝ) + 1 ≤ δ ^ 2 * Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) → Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < eta δ m`
- What: For m ≥ 1, 0 ≤ δ with δm ≤ 1, degrees r_1, …, r_m with last degree r_m ≥ 3 and the chain condition r_{j+1}/δ ≤ r_j (paper's (31)), denominators q with 2m + 1 ≤ δ²·log q_1 (the α/A-free part of (32)) and r_1 log q_1 ≤ r_j log q_j (33), the quantity Θ_m(q_1^{δ r_1}; q; r) is strictly below η = 10^m δ^{(1/2)^m}. This is Lemma 7 of the source (`Roth.Θ_lt`) repackaged in the hypothesis form used by Lemma 9 (`main_lemma`).
- Hypotheses: `hδ0` (gives δ > 0 together with hL); `hδm` (used to pass from δ² log q_1 ≥ 2m+1 to the Θ_lt log bound); `hrlast` (Θ_lt's last-degree bound); `hratio` (Θ_lt's chain condition after `div_le_iff₀`); `hL` (log bound and δ > 0); `hqr` (passed verbatim). All used.
- Uses from project: `Roth.Θ` (Roth/Theta.lean:68), `Roth.eta` (Roth/MainLemma.lean:66), `Roth.Θ_lt` (Roth/Theta.lean:962). Mathlib names used: `Nat.exists_eq_succ_of_ne_zero`, `NeZero.ne`, `mul_le_mul_iff_of_pos_right`, `sq_pos_of_pos`, `mul_le_mul_of_nonneg_right`, `one_mul`, `div_le_iff₀`, `Fin.rev_zero`, `Nat.cast_le`, `Nat.cast_ofNat`, `Real.log`.
- Used by: Roth/MainLemma.lean:724 `Roth.exists_auxiliary_polynomial_with_index_gap_aux` (private, l.692), which feeds `Roth.main_lemma` (l.734). `grep -rn theta_lt_eta_of_sq_log_bound_aux Roth/` gives only l.671 (definition) and l.724 (use).

### #265 lemma Roth.exists_auxiliary_polynomial_with_index_gap_aux (private, Roth/MainLemma.lean:692)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private Lemma 9 assembly step combining the auxiliary polynomial (exists_auxiliary_polynomial_of_log_bound_aux) with Lemma 7 (theta_lt_eta_of_sq_log_bound_aux) to get the strict gap gam - eta + Theta < index; single call site in main_lemma; Roth-specific, nothing in mathlib.
- action: Keep as private helper of its single call site Roth/MainLemma.lean:747 (Roth.main_lemma); optionally add a docstring citing Lemmas 7-9 and drop the duplicated delta > 0 derivation shared with theta_lt_eta_of_sq_log_bound_aux (l.679-680 vs l.709-710); no other change.
- Type: `∀ {α : ℝ} {f : Polynomial ℤ}, f.Monic → Polynomial.aeval α f = 0 → ∀ {A : ℝ}, (∀ i, |(f.coeff i : ℝ)| ≤ A) → ∀ {m : ℕ} [NeZero m] {δ : ℝ}, 0 ≤ δ → δ ≤ 1 / m → ∀ {r : Fin m → ℕ}, 3 ≤ r (Fin.rev 0) → (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ ≤ r i) → ∀ {q : Fin m → ℕ}, 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log (q 0) → (∀ j, (r 0 : ℝ) * Real.log (q 
- What: Under the hypotheses of Roth's Lemma 9 (α a root of a monic integer polynomial f with coefficients bounded by A, m ≥ 1, 0 ≤ δ ≤ 1/m, r_m ≥ 3, chain condition (31) r_{j+1}/δ ≤ r_j, log bound (32), and (33) r_1 log q_1 ≤ r_j log q_j), there is an integer polynomial W in the set R_m(q_1^{δ r_1}; r) whose index at (α, …, α) strictly exceeds γ − η + Θ_m(q_1^{δ r_1}; q; r), and all of whose iterated Hasse derivatives ∂_i ∂_k W at (α, …, α) are bounded in absolute value by B_1^{1+3δ}, where B_1 = ⌊q_1^
- Hypotheses: `hf`, `hfα`, `hA` (passed to exists_auxiliary_polynomial_of_log_bound_aux; `hA 0` also used for log(1+A) ≥ 0); `hδ0` (upgraded to δ > 0); `hδm` (antitonicity of r and Lemma 7's δm ≤ 1); `hrlast` (positivity of all r_j and Lemma 7); `h31b` (antitonicity and Lemma 7); `h32` (auxiliary polynomial and, 
- Uses from project: `Roth.RSet` (Roth/Theta.lean:56), `Roth.Θ` (Roth/Theta.lean:68), `Roth.index` (Roth/Index.lean:58), `Roth.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.gam` (Roth/MainLemma.lean:63), `Roth.eta` (Roth/MainLemma.lean:66), `Roth.mainCoeffBound` (Roth/MainLemma.lean:69), `Roth.exists_auxiliary_polynomial_of_log_bound_aux` (Roth/MainLemma.lean:643), `Roth.theta_lt_eta_of_sq_log_bound_aux` (Roth/MainLemm
- Used by: Roth/MainLemma.lean:747 `Roth.main_lemma` (l.735). `grep -rn exists_auxiliary_polynomial_with_index_gap_aux Roth/` gives only l.692 (definition) and l.747 (use).

### #266 theorem Roth.main_lemma (public, Roth/MainLemma.lean:735)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Roth's main lemma (Lemma 9 of the source, Cassels/Ridout lineage) existence of an integer auxiliary polynomial with large index at (alpha,...,alpha), nonvanishing at (h_j/q_j) and bounded Hasse derivatives; a 16-line assembly of project helpers about the project-only index, Theta, RSet and Hasse derivatives with source-specific constants; mathlib has no Roth machinery, so it is a genuine gap but only upstreamable as part of a redesigned Roth development.
- action: Keep in Roth/MainLemma.lean as the paper's Lemma 9 (single caller: private one_lt_roth_eval_bound_aux at Roth/Main.lean:466); do not upstream on its own; no call-site changes.
- Type: `{α : ℝ} {f : Polynomial ℤ} (hf : f.Monic) (hfα : Polynomial.aeval α f = 0) {A : ℝ} (hA : ∀ i, |(f.coeff i : ℝ)| ≤ A) {m : ℕ} [NeZero m] {δ : ℝ} (hδ0 : 0 ≤ δ) (hδm : δ ≤ 1 / m) {r : Fin m → ℕ} (hrlast : 3 ≤ r (Fin.rev 0)) (h31b : ∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ ≤ r i) {q : Fin m → ℕ} (h32 : 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log (q 0))
- What: Roth's main lemma (clean.tex §6, Lemma `roth:lem9`, l.1392–1404): for a real root α of a monic integer polynomial f with coefficients bounded by A, m ≥ 1, 0 ≤ δ ≤ 1/m, degrees r_j with r_m ≥ 3 and r_{j+1}/δ ≤ r_j, denominators q_j with the logarithmic bounds (32), (33), and numerators h_j coprime to q_j, there is a nonzero Q ∈ ℤ[x_1..x_m] with deg_{x_j} Q ≤ r_j, index at (α,…,α) strictly greater than γ − η, Q(h_1/q_1,…,h_m/q_m) ≠ 0, and |Δ_i Q(α,…,α)| < B_1^{1+3δ} for all i, where B_1 = ⌊q_1^{δ 
- Hypotheses: `hf`, `hfα`, `hA` (α algebraic integer with coefficient bound; used by the auxiliary-polynomial construction via Euclidean reduction mod f); `hδ0`, `hδm` (parameter range); `hrlast`, `h31b` (degree chain (31), weakened); `h32` (log bound (32), weakened to ≤); `h33` (balanced logs); `hh` (coprimality
- Uses from project: private `Roth.exists_auxiliary_polynomial_with_index_gap_aux` (Roth/MainLemma.lean:692), private `Roth.exists_hasseDeriv_index_eval_bound_aux` (Roth/MainLemma.lean:477), `Roth.index_le_Θ` (Roth/Theta.lean:99), `Roth.index` (Roth/Index.lean:58), `Roth.Θ` (Roth/Theta.lean:68), `Roth.RSet` (Roth/Theta.lean:56, via `hW`), `Roth.gam`, `Roth.eta`, `Roth.mainCoeffBound` (Roth/MainLemma.lean:63, 66, 69), 
- Used by: Roth/Main.lean:466 (private `one_lt_roth_eval_bound_aux`, on the path to Roth's theorem); named in docstrings Roth/MainLemma.lean:21, :45 and Roth/Main.lean:34. No other occurrence in `Roth/` or `Roth.lean`.

### #267 def Roth.approxSet (public, Roth/Main.lean:55)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: approxSet is a one-line set-builder for the paper's eq. (1) over mathlib primitives; the mathlib notion carrying the same content is LiouvilleWith (whose docstring already names Thue-Siegel-Roth as the p > 2 statement), and a compiled bridge shows that, for irrational α, Roth.roth is equivalent to the statement that no α satisfies LiouvilleWith p α for p > 2, so the set itself has nothing to upstream.
- action: Do not upstream approxSet; keep it in Roth/Main.lean as the paper's eq. (1) (call sites in Main.lean and LeanEval.lean); the mathlib-facing form of Roth's theorem is roth_not_liouvilleWith (two bridges, compiled in evidence/Roth.approxSet/liouvilleWith_bridge.lean), to be added next to Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean if Roth is ever upstreamed.
- Type: `(α κ : ℝ) : Set (ℤ × ℕ)`
- What: The set of pairs `(h, q)` with `q > 0` and `|α - h/q| < 1/q^κ` (real power `κ`): the approximations of `α` of quality `κ`. Pairs need not be reduced.
- Hypotheses: none.
- Uses from project: `[]`
- Used by: Roth/Main.lean: `approxSet_den_le_finite` (73), `reduction` (119–124), `approxSet_num_den_mem_aux` (149–150, private), `exists_reduced_approx` (165–182), `exists_approximants` (257–264), `exists_degrees` (430–431), `roth_of_isIntegral` (548), `roth` (574), `roth_rat` (indirectly through `roth`); Roth/LeanEval.lean: `exists_pos_div_rpow_lt_aux` (21, 35, private), `isDiophantine_iff` (43, 49).

### #268 theorem Roth.exists_nat_mul_isIntegral (public, Roth/Main.lean:62)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: INLINE
- rationale: The statement is the ℚ-to-ℤ, ℕ-valued specialisation of IsAlgebraic.exists_integral_multiple; mathlib's Algebra.natDenominator API (natDenominator_ne_zero plus isIntegral_natDenominator_smul, with IsFractionRing.isAlgebraic_iff) gives it as a compiled one-term composition, in any commutative ℚ-algebra, so there is nothing new to upstream.
- action: Inline at its single call site Roth.reduction (Roth/Main.lean:121) by taking M := Algebra.natDenominator α (add import Mathlib.RingTheory.Algebraic.Denominator), then delete the lemma; or keep it as the paper's §6 Lemma with its body replaced by the composition in evidence/Roth.exists_nat_mul_isIntegral/composition.lean.
- Type: `{α : ℝ} (hα : IsAlgebraic ℚ α) : ∃ M : ℕ, 0 < M ∧ IsIntegral ℤ ((M : ℝ) * α)`
- What: Every real algebraic number has a positive integer multiple that is an algebraic integer.
- Hypotheses: `hα : IsAlgebraic ℚ α`.
- Uses from project: `[]`
- Used by: Roth/Main.lean: `Roth.reduction` (line 121). No other use in `Roth/`.

### #269 theorem Roth.approxSet_den_le_finite (public, Roth/Main.lean:73)
- verdict: BORDERLINE-needs-human | cost: CHEAP | junk: KEEP
- rationale: The stated form is about the project-local approxSet (itself NO-composable) and cannot go upstream as is; its real content, that only finitely many fractions h/q with q at most N lie in a bounded set, is missing from mathlib (mathlib re-derives it inline in Rat.finite_rat_abs_sub_lt_one_div_den_sq), so whether to upstream that generic lemma is a judgment call.
- action: Keep in Roth/Main.lean (callers reduction, exists_reduced_approx, LeanEval.isDiophantine_iff); optionally shorten the proof to the compiled Int.tendsto_coe_cofinite plus Finite.biUnion route in evidence/Roth.approxSet_den_le_finite/alt_proof.lean; if the human approves, upstream the generic finite_int_abs_sub_div_lt-style lemma to Mathlib/NumberTheory/DiophantineApproximation/Basic.lean.
- Type: `(α κ : ℝ) (Q₀ : ℕ) : {hq ∈ approxSet α κ | hq.2 ≤ Q₀}.Finite`
- What: Only finitely many approximations `(h, q)` of `α` of quality `κ` have denominator `q ≤ Q₀`.
- Hypotheses: none.
- Uses from project: `Roth.approxSet`
- Used by: Roth/Main.lean: `Roth.reduction` (line 124), `Roth.exists_reduced_approx` (lines 170, 182); Roth/LeanEval.lean: `isDiophantine_iff` (line 49).

### #270 theorem Roth.eventually_div_rpow_lt (public, Roth/Main.lean:103)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: The statement is the eventually-greater consequence of tendsto_rpow_atTop (via Tendsto.eventually_gt_atTop and tendsto_natCast_atTop_atTop) followed by a one-line rpow rearrangement; its ∃ Q₀ : ℕ, ∀ q > Q₀ shape is project-specific and mathlib would only want the general rpow little-o fact, which is a different declaration.
- action: Keep project-local (3 call sites in Roth/Main.lean:122, Roth/Main.lean:181, Roth/LeanEval.lean:46); optionally restate as ∀ᶠ x : ℝ in atTop with the filter_upwards proof in the evidence file; the side gap isLittleO_rpow_rpow_atTop_of_lt (real analogue of Asymptotics.isLittleO_pow_pow_atTop_of_lt) could be a separate PR to Mathlib/Analysis/SpecialFunctions/Pow/Asymptotics.lean.
- Type: `{M κ κ' : ℝ} (hκ : κ' < κ) : ∃ Q₀ : ℕ, ∀ q : ℕ, Q₀ < q → M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ'`
- What: If κ' < κ then for every real constant M, M/q^κ < 1/q^κ' for all sufficiently large natural numbers q.
- Hypotheses: `hκ : κ' < κ`.
- Uses from project: `[]`
- Used by: Roth/Main.lean: `Roth.reduction` (line 122), `Roth.exists_reduced_approx` (line 181, fibre-finiteness step); Roth/LeanEval.lean: `isDiophantine_iff` (line 46).

### #271 theorem Roth.reduction (public, Roth/Main.lean:118)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: The paper's §6 reduction to algebraic integers is stated over the project-local approxSet (itself NO-composable); in mathlib's LiouvilleWith vocabulary it is the two-call composition natDenominator plus LiouvilleWith.nat_mul, with the exponent preserved, compiled in the evidence file, so there is nothing new to upstream.
- action: Keep project-local in Roth/Main.lean as the §6 Lemma (single call site Roth.roth at Roth/Main.lean:576); if Roth is ever upstreamed in LiouvilleWith form, replace it by the composition reduction_liouvilleWith in evidence/Roth.reduction/liouvilleWith_reduction.lean (no new lemma for Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean).
- Type: `{α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ} (hκ : 2 < κ) (hinf : (approxSet α κ).Infinite) : ∃ (α' κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧ 2 < κ' ∧ (approxSet α' κ').Infinite`
- What: If an irrational real algebraic number α has infinitely many approximations of quality κ > 2, then some irrational real algebraic integer α' has infinitely many approximations of some quality κ' > 2. Concretely α' = Mα (M a positive integer clearing denominators) and κ' = (κ + 2)/2.
- Hypotheses: `hα : Irrational α`, `halg : IsAlgebraic ℚ α`, `hκ : 2 < κ`, `hinf : (approxSet α κ).Infinite`.
- Uses from project: `Roth.approxSet`, `Roth.exists_nat_mul_isIntegral`, `Roth.eventually_div_rpow_lt`, `Roth.approxSet_den_le_finite`
- Used by: Roth/Main.lean: `Roth.roth` (line 576). No other use in `Roth/`.

### #272 theorem Roth.exists_monic_aeval_eq_zero (public, Roth/Main.lean:142)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: INLINE
- rationale: The statement is the definition of IsIntegral (or minpoly.monic plus minpoly.aeval) padded by X^2 to force degree at least 2; it is a compiled one-term composition of minpoly.monic, Monic.mul, monic_X_pow and natDegree_mul_X_pow, and the degree bound is an artificial padding device rather than mathematical content.
- action: Inline at its single call site Roth.exists_roth_parameters_aux (Roth/Main.lean:415) as the term from evidence/Roth.exists_monic_aeval_eq_zero/composition.lean (minpoly ℤ α * X ^ 2), then delete the lemma; or keep it as the paper's §6 sentence with its body replaced by that term.
- Type: `{α : ℝ} (hint : IsIntegral ℤ α) : ∃ f : Polynomial ℤ, f.Monic ∧ Polynomial.aeval α f = 0 ∧ 2 ≤ f.natDegree`
- What: An algebraic integer is a root of a monic integer polynomial of degree at least 2.
- Hypotheses: `hint : IsIntegral ℤ α`.
- Uses from project: `[]`
- Used by: Roth/Main.lean: `Roth.exists_roth_parameters_aux` (private, line 415). No other use in `Roth/`.

### #273 theorem Roth.approxSet_num_den_mem_aux (private, Roth/Main.lean:149)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private helper showing that reducing h/q to lowest terms keeps a pair in approxSet (den divides q, so the bound 1/q^κ weakens to 1/den^κ for κ ≥ 0); used once in exists_reduced_approx; mathlib has no approxSet and no direct den-of-quotient-le lemma.
- action: Keep as private helper for its single call site Roth/Main.lean:174 (exists_reduced_approx); optionally inline there, no change required.
- Type: `∀ {α κ : ℝ}, 0 ≤ κ → ∀ {h : ℤ} {q : ℕ}, (h, q) ∈ approxSet α κ → (((h : ℚ) / q).num, ((h : ℚ) / q).den) ∈ approxSet α κ`
- What: If h/q is a solution of `0 < q`, `|α - h/q| < 1/q^κ`, then so is its reduced form `num/den`: the reduced denominator is at most q, so for κ ≥ 0 the bound only gets weaker, while the value of the fraction is unchanged.
- Hypotheses: `hκ : 0 ≤ κ` is genuinely needed (for κ < 0, `1/q^κ` is increasing in q, so shrinking the denominator could break the bound); `hq` membership provides `0 < q` (used for `Nat.le_of_dvd`) and the approximation inequality.
- Uses from project: `Roth.approxSet` (Roth/Main.lean:55).
- Used by: Roth/Main.lean:174 `Roth.exists_reduced_approx` only (`grep -rn approxSet_num_den_mem_aux Roth/` gives the definition l.149 and that use). Transitively everything downstream of `exists_reduced_approx` in Roth/Main.lean (the §7 main argument).

### #274 theorem Roth.exists_reduced_approx (public, Roth/Main.lean:164)
- verdict: BORDERLINE-needs-human | cost: CHEAP | junk: KEEP
- rationale: Stated over the project-local approxSet (NO-composable) so it cannot go upstream as is; its content, that for irrational x infinitely many unreduced approximations of quality κ > 0 give infinitely many rationals x with abs(x - r) below r.den^(-κ), is missing from mathlib (no bridge between the unreduced LiouvilleWith-style form and the den-form of Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational), so whether that generic equivalence is worth upstreaming is a judgment call.
- action: Keep in Roth/Main.lean (single caller exists_approximants at line 261); if the human approves, upstream the compiled equivalence approxSet_infinite_iff_rat (evidence/Roth.exists_reduced_approx/rat_form.lean), restated with LiouvilleWith-style unreduced fractions, to Mathlib/NumberTheory/DiophantineApproximation/Basic.lean.
- Type: `{α : ℝ} (hα : Irrational α) {κ : ℝ} (hκ : 0 < κ) (hinf : (approxSet α κ).Infinite) (Q₀ : ℕ) : ∃ hq ∈ approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 (hq.2 : ℤ)`
- What: If α is irrational, κ > 0 and α has infinitely many (possibly unreduced) approximations h/q of quality κ, then for every bound Q₀ there is a reduced approximation h/q (gcd 1) of quality κ with q > Q₀.
- Hypotheses: `hα` irrational (needed: for rational α = a/b and κ > 1 there are infinitely many unreduced solutions (ka, kb) but no reduced ones with large denominator); `hκ : 0 < κ` (used for reduction monotonicity and for the fibre bound; see Phase 5.5 for whether the conclusion needs it); `hinf` infinite appro
- Uses from project: `Roth.approxSet`, `Roth.approxSet_den_le_finite`, `Roth.approxSet_num_den_mem_aux`, `Roth.eventually_div_rpow_lt`
- Used by: Roth/Main.lean:261 `Roth.exists_approximants` (only; `grep -rn exists_reduced_approx Roth/`).

### #275 theorem Roth.exists_m (public, Roth/Main.lean:196)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Eq. (47) parameter choice of Roth's proof (for kappa > 2 pick m > 16n^2 with 2m/(m - 4n sqrt m) < kappa); no literature standing outside this proof, no mathlib counterpart, hypothesis 2 < kappa necessary (compiled converse), a 20-line explicit-witness argument rather than a 3-call composition; its middle conjunct 4n sqrt m < m is redundant (compiled from 16n^2 < m) and discarded at the only call site; recommended resolution keep project-local.
- action: Keep in Roth/Main.lean (single caller private Roth.exists_roth_parameters_aux at Roth/Main.lean:419); do not upstream; optionally drop the redundant conjunct 4 * n * sqrt m < m from the statement (derivable from 16 * n ^ 2 < m, evidence (1)) and the `-` pattern at Main.lean:419.
- Type: `{n : ℕ} {κ : ℝ} (hκ : 2 < κ) : ∃ m : ℕ, 16 * n ^ 2 < m ∧ 4 * n * √(m : ℝ) < m ∧ 2 * m / (m - 4 * n * √(m : ℝ)) < κ`
- What: the choice of the number of variables `m` in §7 of the source (eq. (47)): for `κ > 2` there is `m > 16 n²` with `4 n √m < m` and `2m / (m − 4n√m) < κ`.
- Hypotheses: `hκ : 2 < κ` (necessary: the conclusion forces it, compiled in evidence (2)).
- Uses from project: `[]`
- Used by: `Roth.exists_roth_parameters_aux` (private, Roth/Main.lean:419, which discards the middle conjunct with `-`); module docstring Roth/Main.lean:29; docstring of `Roth.exists_delta` (Main.lean:220).

### #276 theorem Roth.exists_delta (public, Roth/Main.lean:227)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Eqs. (29), (30), (48)/(49) choice of delta in Roth's proof (given m > 16n^2 and the eq. (47) bound, pick 0 < delta < 1/m with (30) and m(1+4delta)/(gam - eta) < kappa); both hypotheses necessary (compiled converse), about project-only eta/gam, no literature standing outside this proof, no mathlib counterpart, and a 24-line continuity argument rather than a 3-call composition; recommended resolution keep project-local.
- action: Keep in Roth/Main.lean (single caller private Roth.exists_roth_parameters_aux at Roth/Main.lean:420); do not upstream; optionally restate together with Roth.exists_delta_bound as eventually-in-nhdsWithin-Ioi-0 bounds combined by filter_upwards and Filter.Eventually.exists_gt.
- Type: `{n m : ℕ} (hm : 16 * n ^ 2 < m) {κ : ℝ} (h47' : 2 * m / (m - 4 * n * √(m : ℝ)) < κ) : ∃ δ : ℝ, 0 < δ ∧ δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧ (m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ`
- What: the choice of `δ` in §7 of the source (clean.tex l.1588–1607): given `m > 16n²` and the eq. (47) bound `2m/(m − 4n√m) < κ`, there is `δ ∈ (0, 1/m)` satisfying (30) `η + 2(1+3δ)n√m < m/2` and (49) `m(1+4δ)/(γ − η) < κ`.
- Hypotheses: `hm : 16 * n ^ 2 < m` (eq. (47) side condition, feeds `exists_delta_bound`); `h47' : 2 * m / (m - 4 * n * √m) < κ` (eq. (47)). Both necessary (compiled converse).
- Uses from project: `Roth.exists_delta_bound`, `Roth.eta`, `Roth.gam`, `Roth.lam`, `Roth.eta_lt_gam_iff`
- Used by: private `Roth.exists_roth_parameters_aux` (Roth/Main.lean:420); module docstring Main.lean:29.

### #277 theorem Roth.exists_approximants (public, Roth/Main.lean:256)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Eq. (50) selection step of Roth's proof (m reduced approximants in approxSet with log q_1 > L and log q_(j+1) > (2/delta) log q_j), stated over the project-local approxSet (NO-composable) and consumed once; its generic core (dependent choice of a sequence with prescribed growth from an unbounded function) is already essentially mathlib's exists_seq_of_forall_finset_exists (compiled), and the remaining content is log/ceil arithmetic, so there is nothing natural to upstream; recommended resolution keep project-local.
- action: Keep in Roth/Main.lean (single caller private Roth.exists_roth_parameters_aux at Roth/Main.lean:438); do not upstream; optionally note in the docstring that delta needs no hypothesis (compiled with delta = -1 in evidence/Roth.exists_approximants/generic_selection.lean).
- Type: `{α : ℝ} (hα : Irrational α) {κ : ℝ} (hκ : 0 < κ) (hinf : (approxSet α κ).Infinite) (m : ℕ) [NeZero m] {δ : ℝ} (L : ℝ) : ∃ (h : Fin m → ℤ) (q : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧ (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ L < Real.log (q 0) ∧ ∀ i j : Fin m, i.val + 1 = j.val → 2 / δ * Real.log (q i) < Real.log (q j)`
- What: For irrational α with infinitely many approximations of quality κ > 0, one can choose m reduced approximations h_j/q_j (j = 0, ..., m-1) of quality κ with q_j > 1, log q_0 > L, and log q_(j+1) > (2/δ) log q_j (paper eq. (32) for q_1 and eq. (50)).
- Hypotheses: `hα` irrational and `hκ : 0 < κ` (passed to `exists_reduced_approx`, needed there); `hinf` infinite approximation set; `m` with `[NeZero m]` (so `q 0` makes sense); `δ` and `L` arbitrary reals (no hypothesis on δ is needed; for δ ≤ 0 the growth condition is automatic).
- Uses from project: `Roth.approxSet`, `Roth.exists_reduced_approx`
- Used by: Roth/Main.lean:438 `Roth.exists_roth_parameters_aux` (private); also named in the module docstring (Main.lean:32). `grep -rn exists_approximants Roth/ Roth.lean`: no other hits.

### #278 theorem Roth.exists_degrees (public, Roth/Main.lean:282)
- verdict: BORDERLINE-needs-human | cost: n/a | junk: KEEP
- rationale: Source eqs. (51)-(53) rounding lemma choosing degrees r_j = ceil(s log q_1 / log q_j) in Roth's proof; hdelta0 and hq necessary (compiled converse) and h50 not droppable (compiled counterexample), no literature standing outside this proof, no mathlib counterpart, and a 30-line rounding argument rather than a 3-call composition; recommended resolution keep project-local.
- action: Keep in Roth/Main.lean (single caller private Roth.exists_roth_approximants_aux at Roth/Main.lean:440); do not upstream; optionally relax hδ1 to δ ≤ 10 (uncompiled observation) if a caller ever needs it.
- Type: `{m : ℕ} [NeZero m] {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1) {q : Fin m → ℕ} (hq : ∀ j, 1 < q j) (h50 : ∀ i j : Fin m, i.val + 1 = j.val → 2 / δ * Real.log (q i) ≤ Real.log (q j)) : ∃ r : Fin m → ℕ, (∀ j, 0 < r j) ∧ (∀ j, 10 / δ < r j) ∧ (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ < r i) ∧ (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) ∧ ∀ j, (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * 
- What: the choice of degrees in §7 of the source (clean.tex l.1615–1642): given denominators `q_j > 1` whose logarithms grow by a factor `≥ 2/δ` from one index to the next, there are positive degrees `r_j` with `r_j > 10/δ` (31), `r_{j+1}/δ < r_j` (31), `r_1 log q_1 ≤ r_j log q_j` (33) and `r_j log q_j < (1 + δ/10) r_1 log q_1` (53).
- Hypotheses: `hδ0` (positivity of δ, necessary), `hδ1 : δ ≤ 1` (used only to bound `(1+δ/10)/2 ≤ 11/20`), `hq` (logs positive, necessary), `h50` (eq. (50) growth, needed for (31b)).
- Uses from project: `[]` (only mathlib)
- Used by: private `Roth.exists_roth_approximants_aux` (Roth/Main.lean:440); module docstring Main.lean:33.

### #279 theorem Roth.one_le_prod_pow_mul_abs_eval (public, Roth/Main.lean:324)
- verdict: YES-but-generalise-first | cost: CHEAP | junk: KEEP
- rationale: Multivariate Liouville clearing-denominators bound (product of q_j^(r_j) times the absolute value of Q(h/q) is at least 1); mathlib has only the univariate one_le_pow_mul_abs_eval_div in Mathlib/Algebra/Polynomial/DenomsClearable.lean, and the project proof compiles verbatim over any Fintype sigma, any linearly ordered field K and integer denominators.
- action: Ship MvPolynomial.one_le_prod_pow_mul_abs_eval_div over [Fintype σ] [Field K] [LinearOrder K] [IsStrictOrderedRing K] with q : σ → ℤ (compiled in evidence/Roth.one_le_prod_pow_mul_abs_eval/general.lean) as the multivariate sibling of one_le_pow_mul_abs_eval_div, optionally with the integrality statement split out; keep the Fin m / ℝ form for the single caller Roth/Main.lean:476 or derive it from the general lemma.
- Type: `{m : ℕ} (Q : MvPolynomial (Fin m) ℤ) {r : Fin m → ℕ} (hQ : ∀ j, degreeOf j Q ≤ r j) (h : Fin m → ℤ) {q : Fin m → ℕ} (hq : ∀ j, 0 < q j) (hne : eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q) ≠ 0) : 1 ≤ (∏ j, (q j : ℝ) ^ r j) * |eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)|`
- What: If an integer polynomial `Q` in `m` variables has degree at most `r_j` in `x_j` and does not vanish at the rational point `(h_1/q_1, …, h_m/q_m)`, then `(∏_j q_j^{r_j}) |Q(h/q)| ≥ 1`.
- Hypotheses: `hQ` (partial degree bounds), `hq` (positive denominators), `hne` (non-vanishing at the rational point).
- Uses from project: `[]` (only mathlib: `MvPolynomial.eval_eq'`, `MvPolynomial.support_map_of_injective`, `MvPolynomial.coeff_map`, `MvPolynomial.monomial_le_degreeOf`, `pow_sub_mul_pow`, `Int.one_le_abs`, `Finset.prod_pos`)
- Used by: Roth/Main.lean:476 (inside the Lemma 9 / eq. (54) contradiction step of the main argument: `(one_le_prod_pow_mul_abs_eval Q hQd h hq0 hne).trans_lt ...`); also mentioned in the Main.lean module docstring (line 38).

### #280 lemma Roth.abs_prod_pow_le_rpow_of_le_weight (private, Roth/Main.lean:347)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private Roth-specific estimate turning coordinate bounds |x_j| at most q_j^(-κ) and q_0^(r_0/r_j) at most q_j into |∏ x_j^(d_j)| at most q_0^(-r_0 c κ) when c is at most weight r d; single caller abs_eval_lt_of_le_index, no mathlib analogue.
- action: Keep as private helper for its single call site Roth/Main.lean:400 (abs_eval_lt_of_le_index); no change needed.
- Type: `∀ {m : ℕ} [NeZero m] {r q : Fin m → ℕ}, (∀ j, 0 < q j) → ∀ {κ : ℝ}, 0 ≤ κ → ∀ {x : Fin m → ℝ}, (∀ j, |x j| ≤ 1 / (q j : ℝ) ^ κ) → (∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j) → ∀ (d : Fin m →₀ ℕ) {c : ℝ}, c ≤ weight r d → |∏ j, x j ^ d j| ≤ (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ)`
- What: If each coordinate x_j is bounded by q_j^(-κ) (κ ≥ 0, q_j positive integers), and the denominators grow as q_j ≥ q_0^(r_0/r_j), then for any multi-index d whose weight ∑ d_j/r_j is at least c, the monomial ∏ x_j^(d_j) has absolute value at most q_0^(-r_0 c κ). This is the term estimate in §7 of the Roth proof ("|∏ (h_j/q_j - α)^{i_j}| < q_1^{-r_1(γ-η)κ}").
- Hypotheses: `[NeZero m]` (to name index `0 : Fin m`); `hq : ∀ j, 0 < q j`; `hκ : 0 ≤ κ`; `hx` coordinate bounds; `hqr` denominator growth; `hw : c ≤ weight r d`. All are used (hκ for sign of exponent in steps 2 and 4, hq for positivity/q_0 ≥ 1). No positivity of r needed (r j = 0 gives exponent 0 and a zero wei
- Uses from project: `Roth.weight` (Roth/Box.lean:71, unfolded in step 3).
- Used by: Roth/Main.lean: `abs_eval_lt_of_le_index` (l.400) only — `grep -rn abs_prod_pow_le_rpow_of_le_weight Roth/` gives the definition (l.347) and that use. Transitively feeds the upper bound of §7 used in the main theorem.

### #281 theorem Roth.abs_eval_lt_of_le_index (public, Roth/Main.lean:380)
- verdict: BORDERLINE-needs-human | cost: MODERATE | junk: KEEP
- rationale: Roth §7 upper bound for Q(h/q) from the Taylor expansion at (α,…,α) once the index is at least c; a named step of the Roth proof, not a standalone mathlib lemma; built on project-only API (index, eval_eq_sum_box, hasseDeriv) with all seven hypotheses load-bearing, so it only goes upstream if the whole Roth development (and Roth.index, itself BORDERLINE) does.
- action: Keep in Roth/Main.lean for its single caller one_lt_roth_eval_bound_aux (Roth/Main.lean:477); revisit only if the Roth proof is upstreamed (Mathlib/NumberTheory/DiophantineApproximation/Roth or Archive), together with Roth.index and the MvPolynomial Taylor PR.
- Type: `{m : ℕ} [NeZero m] {Q : MvPolynomial (Fin m) ℝ} {r : Fin m → ℕ} (hd : ∀ j, degreeOf j Q ≤ r j) {α c : ℝ} (hidx : c ≤ index Q (fun _ ↦ α) r) {h : Fin m → ℤ} {q : Fin m → ℕ} (hq : ∀ j, 0 < q j) {κ : ℝ} (hκ : 0 ≤ κ) (happ : ∀ j, |α - (h j : ℝ) / q j| ≤ 1 / (q j : ℝ) ^ κ) (hqr : ∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j) {C : ℝ} (hC : ∀ i : Fin m →₀ ℕ, |eval (fun _ ↦ α) (hasseDeriv i Q)| < C) : |eval 
- What: If `Q` has partial degrees at most `r_j`, index at least `c` at `(α, …, α)`, all Hasse derivatives at that point bounded by `C`, and each `h_j/q_j` approximates `α` to order `κ` with `q_j ≥ q_0^{r_0/r_j}`, then `|Q(h/q)| < ∏(r_j+1) · C · q_0^{-r_0 c κ}`.
- Hypotheses: `hd` (partial degree bounds), `hidx` (index lower bound), `hq` (positive denominators), `hκ` (nonnegative exponent), `happ` (approximation quality), `hqr` (denominator growth eq. (52)), `hC` (Hasse-derivative bound, Lemma 9 (3)).
- Uses from project: `MvPolynomial.eval_eq_sum_box`, `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.index_le_weight`, `Roth.box`, `Roth.mem_box`, `Roth.card_box`, `Roth.abs_prod_pow_le_rpow_of_le_weight` (private)
- Used by: Roth/Main.lean:477 (`one_lt_roth_eval_bound_aux`, the final contradiction); mentioned in the module docstring Roth/Main.lean:39.

### #282 lemma Roth.exists_roth_parameters_aux (private, Roth/Main.lean:410)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private parameter-selection step of the proof of Roth's theorem (choose f, A, m, delta satisfying eqs. 29-30, 47-49 of the source) bundling exists_monic_aeval_eq_zero, exists_m and exists_delta; used once by roth_of_isIntegral; Roth-specific constants, nothing for mathlib.
- action: Keep as private helper of its single call site Roth/Main.lean:551 (roth_of_isIntegral); no change.
- Type: `∀ {α κ : ℝ}, IsIntegral ℤ α → 2 < κ → ∃ (f : Polynomial ℤ) (A : ℝ) (m : ℕ) (δ : ℝ), f.Monic ∧ Polynomial.aeval α f = 0 ∧ 1 ≤ A ∧ (∀ i, |(f.coeff i : ℝ)| ≤ A) ∧ 2 ≤ m ∧ 0 < δ ∧ δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * f.natDegree * √(m : ℝ) < m / 2 ∧ (m : ℝ) * (1 + 4 * δ) / (gam δ f.natDegree m - eta δ m) < κ`
- What: Let α be a real algebraic integer and κ > 2. Then there are a monic integer polynomial f with f(α) = 0, a real A ≥ 1 bounding all |coefficients| of f, an integer m ≥ 2 and a real δ with 0 < δ < 1/m such that η(δ, m) + 2(1 + 3δ) n √m < m/2 and m(1 + 4δ)/(γ(δ, n, m) − η(δ, m)) < κ, where n = deg f, η(δ, m) = 10^m δ^{(1/2)^m} and γ = (m − λ)/2. This is the opening parameter choice of §7 of the source (eqs. (29), (30), (47)–(49)), packaged for the proof by contradiction of Roth's theorem for algebra
- Hypotheses: `hint : IsIntegral ℤ α` (gives f via `exists_monic_aeval_eq_zero`), `hκ : 2 < κ` (needed by `exists_m`). Both used, neither redundant. Irrationality of α is not needed here (the `2 ≤ natDegree` is manufactured by multiplying by X²).
- Uses from project: `Roth.exists_monic_aeval_eq_zero` (Roth/Main.lean:142), `Roth.exists_m` (Roth/Main.lean:196), `Roth.exists_delta` (Roth/Main.lean:227), `Roth.eta` (Roth/MainLemma.lean:66), `Roth.gam` (Roth/MainLemma.lean:63).
- Used by: Roth/Main.lean:551 `Roth.roth_of_isIntegral` (destructured into f, A, m, δ and all nine facts). `grep -rn exists_roth_parameters_aux Roth/` gives only the definition (l.410) and this use. Transitively feeds `Roth.roth` (main theorem).

### #283 lemma Roth.exists_roth_approximants_aux (private, Roth/Main.lean:429)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private step of the proof of Roth's theorem choosing m reduced approximants h_j/q_j and balanced degrees r_j (source eqs. 31-33, 50-53) by chaining exists_approximants and exists_degrees plus an antitonicity argument; used once by roth_of_isIntegral; Roth-specific constants, nothing for mathlib.
- action: Keep as private helper of its single call site Roth/Main.lean:557 (roth_of_isIntegral); no change.
- Type: `∀ {α κ : ℝ}, Irrational α → 0 < κ → (approxSet α κ).Infinite → ∀ (m : ℕ) [NeZero m] {δ : ℝ}, 0 < δ → δ ≤ 1 → ∀ (A : ℝ), ∃ (h : Fin m → ℤ) (q r : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧ (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ (∀ j, 0 < r j) ∧ 3 ≤ r (Fin.rev 0) ∧ (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ ≤ r i) ∧ (∀ j, r j ≤ r 0) ∧ (2 * m + 1 + 2 * m * Real.log (1 + A) +
- What: Let α be irrational, κ > 0, and suppose α has infinitely many approximations h/q with |α − h/q| < q^{−κ}. Then for every m ≥ 1, 0 < δ ≤ 1 and real A there are m reduced approximations h_j/q_j (gcd(h_j, q_j) = 1, q_j > 1) and positive integer degrees r_j such that: the last degree r_{m−1} is ≥ 3; r_{j+1}/δ ≤ r_j (so r is non-increasing and r_j ≤ r_0); log q_0 is so large that 2m + 1 + 2m log(1 + A) + 2m log(1 + |α|) < δ² log q_0 (eq. (32)); and the r_j log q_j are balanced: r_0 log q_0 ≤ r_j log 
- Hypotheses: `hα : Irrational α`, `hκ : 0 < κ`, `hinf` (all three passed to `exists_approximants`); `hδ0 : 0 < δ`, `hδ1 : δ ≤ 1` (needed by `exists_degrees` and by both `le_div_self` steps); `[NeZero m]` (needed for `Fin m` indexing at 0 and for `exists_degrees`). `A` is a free parameter only entering the consta
- Uses from project: `Roth.approxSet` (Roth/Main.lean:55), `Roth.exists_approximants` (Roth/Main.lean:256), `Roth.exists_degrees` (Roth/Main.lean:282).
- Used by: Roth/Main.lean:557 `Roth.roth_of_isIntegral` (destructured into h, q, r and all ten facts, each of which is consumed: happ via `(happ j).2.le` into `one_lt_roth_eval_bound_aux`, hcop/hr0/hrlast/h31b/h33 into `one_lt_roth_eval_bound_aux`, hq1/h53 into `roth_log_bound_aux`, hr0max and h32 into `roth_product_bound_aux`). `grep -rn exists_roth_approximants_aux Roth/` gives only the definition (l.429) 

### #284 lemma Roth.one_lt_roth_eval_bound_aux (private, Roth/Main.lean:453)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private step of the proof of Roth's theorem (section 7) combining main_lemma (Lemma 9) with the integrality lower bound one_le_prod_pow_mul_abs_eval and the Taylor upper bound abs_eval_lt_of_le_index into the inequality 1 < (prod q_j^r_j) * upper bound; used once by roth_of_isIntegral; Roth-specific constants, nothing for mathlib.
- action: Keep as private helper of its single call site Roth/Main.lean:562 (roth_of_isIntegral); no change.
- Type: `∀ {α κ : ℝ} {f : Polynomial ℤ}, f.Monic → Polynomial.aeval α f = 0 → ∀ {A : ℝ}, (∀ i, |(f.coeff i : ℝ)| ≤ A) → ∀ {m : ℕ} [NeZero m] {δ : ℝ}, 0 ≤ δ → δ ≤ 1 / m → ∀ {r : Fin m → ℕ}, (∀ j, 0 < r j) → 3 ≤ r (Fin.rev 0) → (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ ≤ r i) → ∀ {q : Fin m → ℕ}, (∀ j, 0 < q j) → 0 ≤ κ → ∀ {h : Fin m → ℤ}, (∀ j, |α - (h j : ℝ) / q j| ≤ 1 / (q j : ℝ) ^ κ) → (∀ j, IsC
- What: Let α be a root of a monic integer polynomial f with coefficients bounded by A, let δ, m, the degrees r_j, the denominators q_j and the coprime approximations h_j/q_j (with |α − h_j/q_j| ≤ q_j^{−κ}) satisfy the hypotheses (31b), (32), (33) of Lemma 9 of the source. Then 1 < (∏_j q_j^{r_j}) · (∏_j (r_j + 1)) · B^{1+3δ} · q_0^{−r_0 (γ − η) κ}, where B = ⌊q_0^{δ r_0}⌋, γ = gam δ n m, η = eta δ m. This is the "the nonzero integer value is at least 1 but at most the Taylor bound" comparison of §7 of 
- Hypotheses: hf, hfα, hA, hδ0, hδm, hrlast, h31b, h32, h33, hcop are all passed to `main_lemma`; hr0 is used for `hqr` (division by r j; not derivable from h31b since δ = 0 is allowed, making h31b vacuous); hq0 for positivity and for both bounding lemmas; hκ0 and happ for `abs_eval_lt_of_le_index`. All used, non
- Uses from project: `Roth.main_lemma` (Roth/MainLemma.lean:735), `Roth.one_le_prod_pow_mul_abs_eval` (Roth/Main.lean:324), `Roth.abs_eval_lt_of_le_index` (Roth/Main.lean:380), `Roth.mainCoeffBound` (Roth/MainLemma.lean:69), `Roth.gam` (Roth/MainLemma.lean:63), `Roth.eta` (Roth/MainLemma.lean:66); indirectly through the main_lemma conclusion `Roth.index` and `Roth.hasseDeriv` (destructured, not named in the body excep
- Used by: Roth/Main.lean:562 `Roth.roth_of_isIntegral` (supplies the `hone` argument of `roth_log_bound_aux`). `grep -rn one_lt_roth_eval_bound_aux Roth/` gives only the definition (l.453) and this use. Transitively feeds `Roth.roth` (main theorem).

### #285 lemma Roth.roth_product_bound_aux (private, Roth/Main.lean:481)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private step of the section 7 proof of Roth's theorem packaging three facts about B = mainCoeffBound delta q_0 r_0 (B > 0, B at most q_0^(delta r_0), prod (r_j + 1) < B^delta) from (32) via sqrt_lt_floor, four_lt_rpow and three_small_factors; used once by roth_of_isIntegral; Roth-specific constants, nothing for mathlib.
- action: Keep as private helper of its single call site Roth/Main.lean:559 (roth_of_isIntegral); no change.
- Type: `∀ {m : ℕ} [NeZero m] {α A δ : ℝ}, 0 ≤ δ → 0 ≤ A → ∀ {q r : Fin m → ℕ}, 0 < r 0 → (∀ j, r j ≤ r 0) → 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log (q 0) → 0 < (mainCoeffBound δ (q 0) (r 0) : ℝ) ∧ (mainCoeffBound δ (q 0) (r 0) : ℝ) ≤ (q 0 : ℝ) ^ (δ * r 0) ∧ (∏ j, ((r j : ℝ) + 1)) < (mainCoeffBound δ (q 0) (r 0) : ℝ) ^ δ`
- What: Let m ≥ 1, δ ≥ 0, A ≥ 0, natural degrees r_j with r_0 > 0 maximal among them, and suppose the size condition (32) 2m + 1 + 2m log(1+A) + 2m log(1+|α|) ≤ δ² log q_0 holds. Then the coefficient scale B = ⌊q_0^{δ r_0}⌋ satisfies B > 0, B ≤ q_0^{δ r_0}, and ∏_j (r_j + 1) < B^δ. These are exactly the three facts about B consumed by the logarithmic comparison `roth_log_bound_aux` in §7 of the source.
- Hypotheses: hδ0 (for `four_lt_rpow`, `three_small_factors`); hA (log(1+A) ≥ 0 in h32', and `three_small_factors`); hr0 (for `four_lt_rpow`, `three_small_factors`); hr0max (bounding each factor by 2^{r_0}); h32 (source of h32' and input to `three_small_factors`); `[NeZero m]` (gives hm1 : 1 ≤ m, used implicitly 
- Uses from project: `Roth.mainCoeffBound` (Roth/MainLemma.lean:69), `Roth.sqrt_lt_floor` (Roth/MainLemma.lean:115), `Roth.four_lt_rpow` (Roth/MainLemma.lean:122), `Roth.three_small_factors` (Roth/MainLemma.lean:180).
- Used by: Roth/Main.lean:559 `Roth.roth_of_isIntegral` (destructured into hBpos, hBX, hN, passed to `roth_log_bound_aux`). `grep -rn roth_product_bound_aux Roth/` gives only the definition (l.481) and this use. Transitively feeds `Roth.roth` and `Roth.roth_rat`.

### #286 lemma Roth.roth_log_bound_aux (private, Roth/Main.lean:505)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private final step of the section 7 proof of Roth's theorem that takes logarithms of the evaluation bound 1 < P N B^(1+3 delta) q_0^(-r_0 G kappa) and combines it with (53), B at most q_0^(delta r_0) and N < B^delta to get G kappa < m (1 + 4 delta); Roth-specific real-analysis bookkeeping, used once by roth_of_isIntegral, nothing for mathlib.
- action: Keep as private helper of its single call site Roth/Main.lean:561 (roth_of_isIntegral); no change.
- Type: `∀ {m : ℕ} [NeZero m], 2 ≤ m → ∀ {δ G κ B : ℝ}, δ ≤ 1 → ∀ {q r : Fin m → ℕ}, (∀ j, 1 < q j) → (∀ j, (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r 0 * Real.log (q 0))) → 0 < B → B ≤ (q 0 : ℝ) ^ (δ * r 0) → (∏ j, ((r j : ℝ) + 1)) < B ^ δ → 1 < (∏ j, (q j : ℝ) ^ r j) * ((∏ j, ((r j : ℝ) + 1)) * B ^ (1 + 3 * δ) * (q 0 : ℝ) ^ (-(r 0 : ℝ) * G * κ)) → G * κ < m * (1 + 4 * δ)`
- What: Let m ≥ 2, δ ≤ 1, integers q_j > 1 and degrees r_j with r_j log q_j < (1 + δ/10) r_0 log q_0 for every j (inequality (53) of the source), and B > 0 with B ≤ q_0^{δ r_0} and N := ∏ (r_j + 1) < B^δ. If 1 < (∏ q_j^{r_j}) · N · B^{1+3δ} · q_0^{-r_0 G κ}, then G κ < m (1 + 4δ). This is the logarithmic comparison closing §7 of the source; combined with (49) it yields the contradiction in `roth_of_isIntegral`.
- Hypotheses: hm2 and hδ1 (only in the last step, to get 1 + 4δ ≤ (39/10) m); hq1 (positivity of q_j and log q_0 > 0); h53 (bound on log ∏ q_j^{r_j}, and source of r_0 > 0 and δ ≥ 0); hBpos (positivity for the logarithm rewrites); hBX (log B ≤ δ K); hN (log N < δ log B); hone (the inequality being logged); `[NeZe
- Uses from project: `[]` (no project identifiers in the statement or proof; all lemmas are from mathlib/core).
- Used by: Roth/Main.lean:561 `Roth.roth_of_isIntegral` (fed the conclusion of `one_lt_roth_eval_bound_aux` as `hone` and the three outputs of `roth_product_bound_aux` as hBpos, hBX, hN; its result contradicts (49)). `grep -rn roth_log_bound_aux Roth/` gives only the definition (l.505) and this use. Transitively feeds `Roth.roth` and `Roth.roth_rat`.

### #287 theorem Roth.roth_of_isIntegral (public, Roth/Main.lean:547)
- verdict: BORDERLINE-needs-human | cost: EXPENSIVE | junk: KEEP
- rationale: Roth's theorem for irrational real algebraic integers is the genuine core of a result mathlib lacks (LiouvilleWith's module docstring names Thue-Siegel-Roth but nothing proves it), yet the declaration is a strictly narrower one-term special case of Roth.roth (compiled), is stated over the project-local approxSet, and rests on the whole project machinery (main_lemma is itself BORDERLINE), so upstreaming it is a human decision about upstreaming the entire Roth development in LiouvilleWith form, not about this lemma.
- action: Keep in Roth/Main.lean as the paper's section 7 theorem (single caller Roth.roth at Roth/Main.lean:577); do not upstream on its own; if Roth is upstreamed, the mathlib statement is the general not_liouvilleWith form next to Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean and this lemma becomes an internal step (see evidence/Roth.roth_of_isIntegral/liouvilleWith_form.lean).
- Type: `{α : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α) {κ : ℝ} (hinf : (approxSet α κ).Infinite) : κ ≤ 2`
- What: Roth's theorem for irrational real algebraic integers: if `|α − h/q| < 1/q^κ` has infinitely many solutions `(h, q) ∈ ℤ × ℕ`, `q > 0`, then `κ ≤ 2`.
- Hypotheses: `hα : Irrational α`, `hint : IsIntegral ℤ α`, `hinf : (approxSet α κ).Infinite`.
- Uses from project: `Roth.approxSet`, `Roth.exists_roth_parameters_aux`, `Roth.exists_roth_approximants_aux`, `Roth.roth_product_bound_aux`, `Roth.roth_log_bound_aux`, `Roth.one_lt_roth_eval_bound_aux`, `Roth.eta_lt_gam_iff`
- Used by: Roth/Main.lean: `Roth.roth` (line 577). No other use in `Roth/` (also listed in the Main.lean module docstring, line 22).

### #288 theorem Roth.roth (public, Roth/Main.lean:573)
- verdict: YES-but-generalise-first | cost: EXPENSIVE | junk: KEEP
- rationale: Roth's theorem is a genuine named mathlib gap (the LiouvilleWith module docstring states Thue-Siegel-Roth without proof; lean-eval lists it as an open target) but the project statement uses the project-local approxSet and a superfluous Irrational hypothesis; the mathlib form IsAlgebraic.not_liouvilleWith (no irrationality hypothesis, plus the corollary LiouvilleWith.transcendental) is compiled from Roth.roth in the evidence file, while upstreaming the proof means landing the whole ~4.8k-line development bottom-up.
- action: Keep Roth.roth in Roth/Main.lean (callers Roth.roth_rat at Main.lean:583 and LeanEval thueSiegelRoth at LeanEval.lean:64); add the compiled IsAlgebraic.not_liouvilleWith / LiouvilleWith.transcendental wrappers to the project now; upstream target Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean (new file next to LiouvilleWith.lean) only after the MvPolynomial Hasse-derivative/Taylor API, index and main-lemma layers land.
- Type: `{α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ} (hinf : (approxSet α κ).Infinite) : κ ≤ 2`
- What: Roth's theorem: if α is an irrational real algebraic number and `|α − h/q| < 1/q^κ` has infinitely many solutions `(h, q) ∈ ℤ × ℕ` with `q > 0`, then `κ ≤ 2`.
- Hypotheses: `hα : Irrational α`, `halg : IsAlgebraic ℚ α`, `hinf : (approxSet α κ).Infinite`.
- Uses from project: `Roth.approxSet`, `Roth.reduction`, `Roth.roth_of_isIntegral`
- Used by: Roth/Main.lean: `Roth.roth_rat` (line 583). Roth/LeanEval.lean: `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth` (line 64; also named in docstrings at lines 8, 41). Listed in the Main.lean module docstring (line 20). Transitively the whole project feeds it.

### #289 theorem Roth.roth_rat (public, Roth/Main.lean:581)
- verdict: YES-but-generalise-first | cost: EXPENSIVE | junk: KEEP
- rationale: Den-form Roth theorem stated entirely in mathlib vocabulary (same shape as Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational) and absent from mathlib, but Irrational is superfluous (compiled roth_rat' via the mathlib iff for rational x) and the mathlib-facing form is the finiteness statement for 2 < κ; proof upstreaming waits on Roth.roth and the whole development.
- action: Keep in Roth/Main.lean (no project callers; listed in module docstring); drop the Irrational hypothesis now using evidence roth_rat'; upstream as IsAlgebraic.finite_rat_abs_sub_lt_one_div_den_rpow next to Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational (Mathlib/NumberTheory/DiophantineApproximation/Basic.lean) or in the planned Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean, as a corollary of IsAlgebraic.not_liouvilleWith once Roth.roth lands.
- Type: `{α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ} (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2`
- What: Roth's theorem in rational/denominator form: if α is an irrational real algebraic number and infinitely many rationals x satisfy `|α − x| < 1/den(x)^κ`, then `κ ≤ 2`.
- Hypotheses: `hα : Irrational α`, `halg : IsAlgebraic ℚ α`, `hinf` (infinitely many rational approximations of quality κ).
- Uses from project: `Roth.roth`, `Roth.approxSet` (implicitly, as the target of `.mono`)
- Used by: unused in project (only named in the Roth/Main.lean module docstring, line 21)

### #290 def LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine (public, Roth/LeanEval.lean:16)
- verdict: NO-composable-from-mathlib | cost: n/a | junk: KEEP
- rationale: IsDiophantine is the external lean-eval harness's verbatim problem predicate; a compiled bridge shows IsDiophantine x is equivalent to Irrational x and no LiouvilleWith p x for p above 2, i.e. a composition of mathlib's Irrational and LiouvilleWith (the idiom of ae_not_liouvilleWith), so the predicate itself has nothing to upstream.
- action: Keep IsDiophantine unchanged in Roth/LeanEval.lean (it must match the lean-eval statement verbatim; callers isDiophantine_iff at line 43 and thueSiegelRoth at line 62); do not upstream it; if Roth is upstreamed, state it as IsAlgebraic.not_liouvilleWith next to Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean (see Roth.roth report), optionally adding the compiled bridge isDiophantine_iff_liouvilleWith to LeanEval.lean.
- Type: `(x : ℝ) : Prop`
- What: For every `ε > 0` there is `C > 0` such that `C / q^(2+ε) < |x - p/q|` for all integers `p` and `q > 0` (real power). This says the irrationality exponent of `x` is at most 2, with a strict uniform lower bound.
- Hypotheses: none.
- Uses from project: `[]`
- Used by: Roth/LeanEval.lean only: `isDiophantine_iff` (43, statement) and `thueSiegelRoth` (62, conclusion). It is not used in Roth/Main.lean or any other project file. `Roth.lean` does not import `Roth.LeanEval` (grep), and no other file imports it.

### #291 lemma LeanEval.NumberTheory.ThueSiegelRothProblem.exists_pos_div_rpow_lt_aux (private, Roth/LeanEval.lean:20)
- verdict: SKIP | cost: n/a | junk: KEEP
- rationale: Private helper that turns finiteness of Roth.approxSet x κ for irrational x into a uniform positive constant C with C / q^κ < |x - p/q|; used once by isDiophantine_iff, has no direct mathlib counterpart, and is too long to inline cleanly.
- action: Keep as is in Roth/LeanEval.lean (sole caller isDiophantine_iff, line 54); no upstreaming since it is private and harness-specific; if Roth is upstreamed in LiouvilleWith form this helper is no longer needed.
- Type: `{x κ : ℝ} (hx : Irrational x) (hs : (Roth.approxSet x κ).Finite) : ∃ C : ℝ, 0 < C ∧ ∀ (p q : ℤ), 0 < q → C / (q : ℝ) ^ κ < |x - (p : ℝ) / q|`
- What: If `x` is irrational and there are only finitely many `(p, q)` with `q > 0` and `|x - p/q| < 1/q^κ`, then there is a uniform `C > 0` with `C / q^κ < |x - p/q|` for every integer `p` and positive integer `q`. This is the "finitely many good approximations gives a uniform lower bound" step.
- Hypotheses: `hx : Irrational x` (needed so that `f a > 0`; without it the minimum could be `0`); `hs : (Roth.approxSet x κ).Finite`. `κ` is arbitrary real (no sign hypothesis needed).
- Uses from project: `Roth.approxSet` (Roth/Main.lean:55). No other project identifiers. The `Set.exists_min_image`, `Irrational.ne_rational`, `Real.rpow_pos_of_pos`, `div_lt_iff₀`, `lt_div_iff₀`, `half_lt_self`, `min_le_left/right` calls are all mathlib.
- Used by: `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff` (Roth/LeanEval.lean:54, reverse direction) only. `grep -rn exists_pos_div_rpow_lt_aux Roth/ Roth.lean` gives just the declaration (line 20) and that call (line 54).

### #292 theorem LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff (public, Roth/LeanEval.lean:42)
- verdict: BORDERLINE-needs-human | cost: CHEAP | junk: KEEP
- rationale: The harness-glue equivalence between IsDiophantine and the project-local approxSet exponent bound links two non-mathlib predicates, so it cannot go upstream as is (compiled evidence shows that both sides reduce to the mathlib form, not LiouvilleWith p for p above 2, and that the Irrational hypothesis is superfluous); whether mathlib wants the underlying uniform-lower-bound characterisation of not LiouvilleWith is a judgment call.
- action: Keep in Roth/LeanEval.lean (sole caller thueSiegelRoth at LeanEval.lean:63); optionally drop the superfluous hx hypothesis (compiled isDiophantine_iff' in evidence) and add the compiled isDiophantine_iff_liouvilleWith bridge; upstream only a generic lower-bound-vs-LiouvilleWith lemma to Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean if the human approves.
- Type: `{x : ℝ} (hx : Irrational x) : IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2`
- What: For irrational `x`, the lean-eval predicate (for every `ε > 0` some `C > 0` gives `C/q^(2+ε) < |x − p/q|` for all `p/q`) is equivalent to the project's form of Roth's conclusion: every `κ` with infinitely many approximations `|x − h/q| < 1/q^κ` satisfies `κ ≤ 2`.
- Hypotheses: `hx : Irrational x` (only used in the ← direction, via the aux lemma). Superfluous for the statement (see evidence).
- Uses from project: `IsDiophantine`, `Roth.approxSet`, `Roth.eventually_div_rpow_lt`, `Roth.approxSet_den_le_finite`, `exists_pos_div_rpow_lt_aux` (private)
- Used by: `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth` (Roth/LeanEval.lean:63). No other use in `Roth/` (grep). `Roth.lean` does not import `Roth.LeanEval`.

### #293 theorem LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth (public, Roth/LeanEval.lean:61)
- verdict: YES-but-generalise-first | cost: EXPENSIVE | junk: KEEP
- rationale: The harness theorem is the Thue-Siegel-Roth theorem, a named gap that mathlib's LiouvilleWith docstring states without proof, but its signature is fixed by lean-eval and uses the non-mathlib predicate IsDiophantine; the mathlib form is IsAlgebraic.not_liouvilleWith (compiled from Roth.roth, with Irrational superfluous there although it is necessary in the harness form), and the harness statement is a compiled two-step corollary of that form.
- action: Keep thueSiegelRoth verbatim in Roth/LeanEval.lean (harness-mandated; no project callers); upstream the content as IsAlgebraic.not_liouvilleWith plus LiouvilleWith.transcendental in a new Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean together with Roth.roth, after the development lands bottom-up; do not upstream the harness statement itself.
- Type: `(x : ℝ) (_h_irr : Irrational x) (_h_alg : IsAlgebraic ℤ x) : IsDiophantine x`
- What: Every irrational algebraic real `x` is Diophantine in the lean-eval sense: for every `ε > 0` there is `C > 0` with `C / q^(2+ε) < |x − p/q|` for all `p ∈ ℤ`, `q ∈ ℤ_{>0}`. This is the Thue–Siegel–Roth theorem in its lower-bound form.
- Hypotheses: `_h_irr : Irrational x` is necessary in this form (compiled: `IsDiophantine 0` is false). `_h_alg : IsAlgebraic ℤ x` is interchangeable with the `ℚ` version (compiled `thueSiegelRoth_rat`).
- Uses from project: `IsDiophantine`, `isDiophantine_iff`, `Roth.roth`
- Used by: unused in project. This is the harness endpoint: grep of `Roth/` and `Roth.lean` finds only the declaration at Roth/LeanEval.lean:61, and `Roth.lean` does not import `Roth.LeanEval`.
