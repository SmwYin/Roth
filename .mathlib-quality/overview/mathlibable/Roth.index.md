---
decl: Roth.index
file: Roth/Index.lean
line: 58
kind: def
visibility: public
verdict: BORDERLINE-needs-human
cost: EXPENSIVE
junk: KEEP
rationale: The Roth index (min of sum d_j/r_j over the support of P(X+α)) is a real-weighted order of vanishing at a point; mathlib has only MvPowerSeries.weightedOrder (ℕ weights, ℕ∞ values, no MvPolynomial or at-a-point version), to which index equals weightedOrder(taylor α P)/∏r only for positive r (hP superfluous, compiled), so the real-valued Roth form is project-specific while a general "weighted order at a point" is a judgment-call upstream candidate.
action: Keep Roth.index as is locally; optionally drop the superfluous hP from index_eq_weightedOrder_div (Index.lean:143) and reprove index_prod/index_neg via MvPowerSeries.weightedOrder_prod/weightedOrder_neg; any upstreaming should target a new MvPolynomial weighted order (via coeToMvPowerSeries) plus taylor in Mathlib/RingTheory/MvPolynomial, not the ℝ-valued index.
---

# Roth.index

## Inventory entry

### `def Roth.index`
- **Type**: `{σ : Type*} [Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : ℝ`
- **What**: The index of `P` at `α` relative to the parameters `r`: the infimum (a minimum for `P ≠ 0`) of the weights `∑ j, d j / r j` over the multi-indices `d` in the support of the Taylor translate `P(X + α)`, i.e. over `d` with `(Δ_d P)(α) ≠ 0`; junk value `0` for `P = 0` (`sInf ∅ = 0`).
- **How**: `sInf (weight r '' ((taylor α P).support : Set (σ →₀ ℕ)))`, using `Real.sInf` over the finite image of the support under `Roth.weight r`.
- **Hypotheses**: section variable `[Fintype σ]` (needed by `Roth.weight`). No positivity on `r`.
- **Uses from project**: `Roth.weight` (Roth/Box.lean:71), `MvPolynomial.taylor` (Roth/Taylor.lean:42).
- **Used by**: Roth/Index.lean (every lemma: `mem_support_taylor_iff` 62, `index_le_weight` 69, `exists_weight_eq_index` 76, `le_index_iff` 85, `index_nonneg` 93, `index_eq_zero_iff` 98, `index_sub_weight_le_index_hasseDeriv` 109, `le_index_sum` 118, `index_eq_weightedOrder_div` 143, `index_mul` 162, `index_prod` 175, `index_neg` 190, `index_C_mul` 195, `index_mul_left_weights` 200, `index_rename` 212, `index_le_card` 224, `index_unique` 234); Roth/MainLemma.lean:422, 455, 481, 482, 483, 556, 586, 623, 648, 700, 743, 749; Roth/Theta.lean:64, 101, 126, 226, 381, 382, 388, 402, 403, 408, 418, 465, 561, 586; Roth/Main.lean:381; Roth/Separation.lean:135 (docstring reference to the index of the embedded polynomial).
- **Visibility**: public
- **Lines**: 55–59, body 1 line
- **Notes**: The module docstring lists it as the main definition. The file already proves the bridge `index_eq_weightedOrder_div` (Index.lean:143) to mathlib's `MvPowerSeries.weightedOrder` with natural weights `(∏ r) / r j`, and uses it for `index_mul`. The `P ≠ 0` hypothesis of that bridge is superfluous (evidence (1)).

## Junk check (Step 8)
- Used anywhere? Yes: the central definition of the project; 17 lemmas in Index.lean and about 30 references in MainLemma, Theta, Main.
- Wrapper of 1–2 mathlib calls? Not literally. It is `sInf` of an image under a project def of a project def (`MvPolynomial.taylor`). For positive integer `r` it equals `(weightedOrder w ↑(taylor α P)).toNat / ∏ r` with `w j = ∏ r / r j` (Index.lean:143), but that bridge takes a 12-line proof, not a 1–2 call wrapper, and fails for `r j = 0` (evidence (4)).
- Does mathlib have it? No. Mathlib has `MvPowerSeries.weightedOrder` (ℕ weights, values in `ℕ∞`, power series at the origin) and univariate `Polynomial.rootMultiplicity`, with no multivariate order of vanishing at a point and no real-weighted order.
- Too specific (inline)? No. It is the paper's central notion, used in about 50 places.
- Well-chosen? Yes, for the project. The `sInf` form is total in `r`, matches the paper's definition directly (clean.tex §4), and handles arbitrary real-valued weights `1/r_j`. The paper itself (clean.tex Lean note) says the `weightedOrder` route works only for positive integral `r_j`, with the direct finite-support minimum otherwise.
- Conclusion: `KEEP`. Action: keep the definition. Optionally drop the superfluous `hP` from `index_eq_weightedOrder_div` and reprove `index_prod` and `index_neg` from mathlib's `weightedOrder_prod` and `weightedOrder_neg` (see Phase 6).

## Mathlibable assessment (Step 9)

Pre-filter: the def is not private and the name does not end in `_aux`. The docstring is not internal or auxiliary, and Step 8 said KEEP. `Roth.index` is not in mathlib: no `namespace Roth` exists under `Mathlib/`, and the `def index` hits there are unrelated, in `OpensLeCover`, `BoxIntegral` and `FaaDiBruno`. It is a def, not a glue lemma. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Index` compiles with no output)
- decl `Roth.index`:         resolved at Roth/Index.lean:58
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  The index of a real multivariate polynomial at a point relative to positive integer weights, and its basic API (Lemmas 4-1, 4-2, the derivative bound, and the scaling identities).

### Statement (Phase 1)

`Roth.index` is a definition. Let `σ` be a finite variable set, `P ∈ ℝ[X_j : j ∈ σ]`, `α ∈ ℝ^σ` and `r ∈ ℕ^σ`. The index of `P` at `α` relative to `r` is

  `ind(P; α; r) = min { ∑_j d_j / r_j : d ∈ ℕ^σ, (Δ_d P)(α) ≠ 0 }`,

where `Δ_d` is the Hasse derivative. Equivalently, it is the least `r`-weighted degree of a monomial with nonzero coefficient in the translate `P(X + α)`, a weighted order of vanishing of `P` at `α`. The minimum exists for `P ≠ 0`. Lean assigns the junk value `0` to `P = 0`, where the paper uses `+∞`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]`: the finite variable set, required by `Roth.weight`'s sum over `univ`.
- `P : MvPolynomial σ ℝ`: the polynomial.
- `α : σ → ℝ`: the point.
- `r : σ → ℕ`: the parameters. The weights are `1/r_j`, with Lean's `x/0 = 0` when `r_j = 0`.

Hypotheses (Lean side):
- none.

Conclusion (math): the real number `ind(P; α; r) ∈ [0, ∞)`.

Conclusion (Lean): n/a — definition (`noncomputable def index (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : ℝ := sInf (weight r '' ((taylor α P).support : Set (σ →₀ ℕ)))`).

### Size classification (Phase 2a)

Verdict: BIG
Reason: it is the project's central new notion, listed as the main definition of Roth/Index.lean, and it is the named concept ("index") of the Thue–Siegel–Roth–Schmidt method.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | no       | only a few sites unfold it (`rw [index, index, ...]` at Index.lean:197, 207, 216; `simp [index, ...]` at 192); nothing relies on it as a barrier |
| Avoid typeclass diamonds         | no       | no instances involved |
| Mark semantic intent / API name  | yes      | about 50 statements in MainLemma, Theta and Main are phrased with `index P α r` (e.g. `main_lemma`, MainLemma.lean:743; `Θ`, Theta.lean:64; Main.lean:381); the composite `sInf (weight r '' (taylor α P).support)` would be unreadable inline, and the paper's whole argument is about this quantity |

Conclusion: ONE-LINER WITH-EXEMPTION (API name / semantic intent)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | index of a polynomial at a point relative to weights r_1,...,r_m Roth's lemma definition minimum i_1/r_1+...+i_m/r_m | yes | index = min of `∑ j_i / r_i` over exponents of nonzero coefficients of `P` expanded at `α` (equivalently nonzero normalised derivatives) | arXiv math/0307203 (Roth–Ridout quantitative), arXiv 2502.00731 (Evertse, subspace theorem, Lemma 3.9 Roth's lemma), Evertse Bonn notes; derivative property `ind(∂P) ≥ ind P − ∑ k_i/r_i` also stated |
| 2 | WebSearch (general form) | weighted order of vanishing multivariate polynomial at a point weighted multiplicity definition | partial | weighted order = min of `w·a` over exponents `a` of nonzero coefficients at the point; `w = 1` gives the ordinary order of vanishing | arXiv 2604.16698 (weighted blowups), Lebl's *Tasty Bits of SCV* (order of vanishing via homogeneous Taylor components); no single canonical reference |
| 3 | WebSearch (named-after / aliases) | Bombieri Gubler "index" polynomial Roth's theorem weighted multiplicity Dyson lemma | yes | index as a minimum over nonvanishing derivatives weighted by order of differentiation; Dyson's lemma / Esnault–Viehweg as the higher-dimensional index bounds | arXiv math/9708214, 0811.3192, 1305.0926, 1806.10737; Bombieri–Gubler book not directly retrieved |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §4 (l.~530–600) | yes | `ind(P; α; r)` = min of `∑ i_j / r_j` with `Δ_i P(α) ≠ 0`, `ind(0) = +∞`; Lean note: for positive integral `r_j` use natural weights `w_j = D / r_j` in `MvPowerSeries.weightedOrder` and divide by `D`; arbitrary real `r_j` require the direct finite-support minimum | project paper |
| 6 | nLab | order of vanishing / multiplicity | partial | order of vanishing / multiplicity of a function at a point (unweighted) | no weighted or Diophantine "index" entry |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | order of vanishing, weighted blowup | partial | `ord_Z(f)` valuations along divisors; weighted gradings | the index is a monomial (quasi-monomial) valuation `v_w(P(X+α))` with weights `1/r_j`, the closest geometric notion; Stacks has no named weighted version |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | partial | weighted order = monomial valuation | folklore; no canonical general treatment found |
| 10 | recent arXiv (last 5 years) | (results of #1–#3) | yes | arXiv 2502.00731 (2025), 2604.16698 (2026), 1806.10737 | same definition |

### Literature summary (Phase 3)

Concept identified as: the index of a polynomial at a point relative to weights (Roth, Schmidt, Bombieri–Gubler), i.e. a weighted order of vanishing at a point. Valuation-theoretically it is the monomial valuation with weights `1/r_j` centred at `α`, applied to `P`.
Sources agree on the standard form: yes. Normalisations differ (Hasse derivatives vs `∂^I/I!`), and both agree in characteristic 0.
Most general standard form: for a commutative ring `R`, a point `α ∈ R^σ` and a weight vector `w` in an ordered additive monoid (ℕ, ℚ_{≥0}, ℝ_{≥0}), the weighted order of `P` at `α` is `min { ⟨w, d⟩ : coeff_d P(X + α) ≠ 0 }`, taking values in `M ∪ {∞}` with value `∞` at `P = 0`.
Generality dimensions where the literature varies:
  - weights: positive integers (algebraic geometry, mathlib) vs reals `1/r_j` (Roth). Scaling by `D = ∏ r_j` makes the two equivalent when the `r_j` are positive integers.
  - coefficient ring: ℝ or a number field (Roth) vs any (commutative) ring.
  - value at `0`: `+∞` (literature) vs `0` (Lean junk value here).
Disagreement with the literature: the Lean value at `P = 0` is `0`, not `+∞` (documented; every lemma carries nonvanishing hypotheses).

### Generality analysis — `Roth.index`

Literature-standard form (from Phase 3): weighted order at a point, `(R, α, w) ↦ min { ⟨w, d⟩ : d ∈ supp P(X + α) } ∈ M ∪ {∞}`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring `ℝ` | `MvPolynomial σ ℝ` | any `CommSemiring R` (`taylor` is general) | yes, but not mechanically | the codomain `ℝ` and `Real.sInf` do not depend on the coefficients, so `index` could be defined over any `CommSemiring R`; but the project only uses ℝ, and the API proofs use `ℝ`-specific facts (`index_mul` needs a domain, `index_unique` needs `Polynomial.rootMultiplicity` over a domain); not verified, not needed |
| 2 | weights `1/r_j`, `r : σ → ℕ` | real weights via `Roth.weight` | weight vector `w : σ → M` | yes (as a different def) | mathlib's general tool `weightedOrder` takes `w : σ → ℕ`; real weights would need a new def; ℕ weights capture the project form only for positive `r` (evidence (1), (4)) |
| 3 | value type `ℝ` with junk `0` | `ℝ` | `M ∪ {∞}` (`ℕ∞` / `WithTop`) | yes (as a different def) | `ℕ∞`-valued `weightedOrder` gives `⊤` at `0` and enables `weightedOrder_mul` without nonvanishing hypotheses; but the project needs real arithmetic (`index - weight`, `/ l`, `max 0 (index − ν/r)`) everywhere downstream |
| 4 | `[Fintype σ]` | required | not needed (`Finsupp.weight` / `weightedOrder` work for any `σ`) | yes | only needed by `Roth.weight`'s sum over `univ`; would disappear if `weight` were redefined via `Finsupp.weight` (see Roth.weight.md) |
| 5 | point `α` | `σ → ℝ` | `σ → R` | same as row 1 | — |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD in the coefficient ring (row 1) and in `[Fintype σ]` (row 4). The real-weight / real-value shape (rows 2–3) is a deliberate project choice. The general-weight version is not in mathlib (mathlib has only ℕ weights at the origin), so this is not false-positive class 4. Changing to the mathlib-idiomatic `ℕ∞`/ℕ-weight form means restating a foundational def threaded through four files (false-positive class 5), and that routes to BORDERLINE rather than generalise-first.
Number of weakening opportunities found: 2 mechanical-looking ones (rows 1, 4), not verified in Lean because neither is needed by the project. Row 4 depends on the separate `Roth.weight` refactor. The verified, compiled facts about generality are: (1) `index_eq_weightedOrder_div` holds without `P ≠ 0`; (4) the `sInf` def is total in `r` (`index P α 0 = 0`), where the `weightedOrder` formula degenerates to `0/0`.
Proposed restatement (mathlib-idiomatic target, if upstreamed): `MvPolynomial.weightedOrder (w : σ → ℕ) (p : MvPolynomial σ R) : ℕ∞ := (p : MvPowerSeries σ R).weightedOrder w`, with order at a point `(taylor α p).weightedOrder w`; the project's `index P α r` would then be `((taylor α P).weightedOrder (fun j ↦ ∏ r / r j)).toNat / ∏ r` for positive `r`.
Cost of restatement: EXPENSIVE locally. All 17 Index.lean lemmas and the real-arithmetic downstream (Theta, MainLemma) would have to go through `ℕ∞.toNat` casts and carry `0 < r`, which several lemmas currently avoid (`index_le_weight`, `le_index_iff`, `index_rename`, `index_mul_left_weights`, `index_le_card`, `index_unique`).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses on the def |
| 2 | sequences to filters? | no | — | finite algebraic minimum |
| 3 | construction vs universal property? | partial | characterise as the monomial valuation `v_{α,w}` (`AddValuation` on `R[X]` with `v(P) = min ⟨w, d⟩` over the support of `P(X + α)`) | `index_mul` and `le_index_sum` become `map_mul` and `map_add` of an `AddValuation`; mathlib has no multivariate monomial valuation (only `Polynomial.idealX` / `PowerSeries` adic valuations), so this is a larger development |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | yes | `MvPolynomial σ R`, `[CommSemiring R]` | general coefficient rings; `taylor` is already general |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | ℕ weights in `ℕ∞` via `MvPowerSeries.weightedOrder` composed with the coercion and `taylor` | `weightedOrder_le`, `exists_coeff_ne_zero_and_weightedOrder`, `min_weightedOrder_le_add`, `weightedOrder_mul`, `weightedOrder_prod`, `weightedOrder_neg`, `le_weightedOrder` apply directly (re-aim table in Phase 6) |
| 8 | concrete-via-abstract? | no | the def has no proof body; the API proofs (e.g. `index_mul`) already go through the abstract `weightedOrder` | — |
| 9 | false-generalisation guard | partial false generalisation | replacing `index` outright by `weightedOrder` (ℕ weights, `ℕ∞` values) is not the same object: it agrees only for positive `r` after scaling by `∏ r` and `toNat` (evidence (1)); for `r j = 0` the project def gives weight `0`, which ℕ weights `∏ r / r j` cannot reproduce (evidence (4)); value at `P = 0` differs (`0` vs `⊤`); so `weightedOrder` is the right upstream object but not a drop-in replacement for `Roth.index` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes (for an upstream contribution, not as a local replacement)
  - Proposed mathlib-idiomatic restatement: `(↑(MvPolynomial.taylor α P) : MvPowerSeries σ R).weightedOrder w : ℕ∞` for `w : σ → ℕ` (possibly packaged as `MvPolynomial.weightedOrder w P` plus `taylor`), with `Roth.index` kept as the project's real-valued normalisation.
  - Cost: EXPENSIVE (if the project def were rebased on it); CHEAP for the bridge, which already exists.
  - Mathlib downstream this enables: the whole `MvPowerSeries.weightedOrder` API (`weightedOrder_mul`, `weightedOrder_prod`, `weightedOrder_neg`, `min_weightedOrder_le_add`, `weightedOrder_le`, `le_weightedOrder`, `exists_coeff_ne_zero_and_weightedOrder`, weighted homogeneous components).
  - Real mathematical improvement: multiplicativity and the ultrametric inequality come from mathlib, not from project re-proofs, and the `+∞` convention at `0` matches the literature without nonvanishing side conditions.

### Proof strategy — `Roth.index`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | (a valuation formulation is possible, row 4c-3) | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | partial | monomial `AddValuation` | EXPENSIVE (new mathlib development) |
| 5 | missing mathlib helpers | yes | `MvPolynomial.weightedOrder` (order of a polynomial, avoiding the coercion to power series); a multivariate order of vanishing at a point; `weightedOrder_smul` equality for nonzero scalars over a domain (only `le_weightedOrder_smul` exists; needed for `index_C_mul`); `weightedOrder_rename` (needed for `index_rename`); `weightedOrder_eq_zero_iff` (the `order` analogue `order_ne_zero_iff_constCoeff_eq_zero` exists, the weighted one with positive weights does not; needed for `index_eq_zero_iff`) | follow-up PRs |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED (light, local)
  - Proposed strategy: keep the `sInf` def. Drop `hP` from `index_eq_weightedOrder_div` (evidence (1)) and use that bridge plus `MvPowerSeries.weightedOrder_prod` (evidence (2)) for `index_prod`, which drops its induction, and `weightedOrder_neg` (evidence (3)) for `index_neg` if desired. `index_neg` is already a one-line `simp`, so the gain there is nil.
  - Cost: CHEAP
  - Missing mathlib API: `MvPolynomial.weightedOrder`, `weightedOrder_rename`, `weightedOrder_smul_of_ne_zero` (domain), `weightedOrder_eq_zero_iff` for positive weights.
  - Would refactoring make the proof strictly shorter / cleaner? marginally (`index_prod`).

### Diamond / defeq risk — `Roth.index`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | defines no instances; `MvPolynomial σ ℝ` and `Real.sInf` instances are canonical |
| 2 | Reducibility leak | none | plain semireducible `noncomputable def`; unfolded only by explicit `rw [index]` / `simp [index]` (Index.lean:192, 197, 207, 216) |
| 3 | Non-canonical unfolding | low | the junk value `0` at `P = 0` (from `Real.sInf ∅ = 0`) differs from the literature's `+∞` and from `weightedOrder`'s `⊤`; that is why the API carries `P ≠ 0` hypotheses (`le_index_iff`, `index_mul`); documented in the module docstring |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `σ : Type*`; `index_rename` works across universes for `τ` |
| 6 | Coercion ambiguity | low | no coercion defined; the name `index` is generic, collides with three unrelated mathlib `index` defs in other namespaces (harmless inside `namespace Roth`), and would be a poor mathlib name |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none (the junk value at `0` and the generic name only matter for upstreaming)
Recommended mitigations: n/a. If upstreamed, use `ℕ∞` values with `⊤` at `0` and a descriptive name (e.g. `MvPolynomial.weightedOrder` / `weightedOrderAt`).

### Mathlib search-status: `Roth.index`

[A] Lean-Finder       "order of vanishing of a multivariate polynomial at a point with weights; minimal weighted degree of nonzero coefficient of P(X + a)"   hits: `MvPowerSeries.weightedOrder`, `weightedOrder_monomial`, `weightedOrder_le`, `le_weightedOrder_subst`; no polynomial / at-a-point version
[B] Loogle            `MvPowerSeries.weightedOrder`   hits: `weightedOrder`, `weightedOrder_zero`, `weightedOrder_one`, `weightedOrder_eq_top_iff`, `ne_zero_iff_weightedOrder_finite`, `weightedOrder_neg`, `le_weightedOrder_mul`, `le_weightedOrder_prod`
[C] LeanSearch        "weighted order of a multivariate polynomial, minimum weighted degree of monomials in support"   hits: `MvPowerSeries.weightedOrder`, `weightedOrder_monomial`, `coeff_eq_zero_of_lt_weightedOrder`, `MvPowerSeries.order`, `weightedOrder_le`
[D] Grep mathlib src  `weightedOrder`, `rootMultiplicity`, `vanishingOrder`, `orderAt` under `Mathlib/Algebra/MvPolynomial`, `Mathlib/RingTheory/MvPolynomial` (no hits); `theorem .*weightedOrder` (Order.lean:134–364, NoZeroDivisors.lean:146 `weightedOrder_mul`, :176 `weightedOrder_prod`, Substitution, PiTopology); `def weightedTotalDegree` (WeightedHomogeneous.lean:96, the max not the min); `def index` (unrelated: OpensLeCover, BoxIntegral, FaaDiBruno); `namespace Roth` (none)
[E] Name pattern      `MvPowerSeries.weightedOrder_prod`, `MvPowerSeries.weightedOrder_neg`, `MvPolynomial.coeToMvPowerSeries.ringHom_apply` (all used in compiled evidence); `MvPolynomial.coe_prod` / `MvPolynomial.coe_neg` do not exist (compile errors in a first draft of the evidence)

Searched for both the user's form (min of `∑ d_j / r_j` over the support of `P(X + α)`, real-valued) and the literature-standard form (weighted order at a point, ℕ/ordered-monoid weights, `∞` at `0`).

Concluded: found building blocks: `MvPowerSeries.weightedOrder` (ℕ weights, at the origin, power series), `MvPolynomial.coeToMvPowerSeries`, `Finsupp.weight`, plus the project's `MvPolynomial.taylor`, which is not in mathlib (YES-add-as-is in MvPolynomial.taylor.md). There is no polynomial-level weighted order, no order of vanishing at a point in several variables, and no real-weighted order.

### Normal-form check — `Roth.index`

Equivalent formalisms: (a) `sInf (weight r '' (taylor α P).support)` (current); (b) `min` over `d` with `eval α (hasseDeriv d P) ≠ 0` (characterised by `le_index_iff` / `exists_weight_eq_index`); (c) `(weightedOrder (∏ r / r ·) ↑(taylor α P)).toNat / ∏ r` for positive `r` (Index.lean:143); (d) `⨅ d ∈ support, weight r d`; (e) in one variable, `rootMultiplicity / r` (Index.lean:234).
Does mathlib already have a canonical form for this idea? Partly: `MvPowerSeries.weightedOrder` is mathlib's canonical weighted order (ℕ weights). There is none at a point and none with real weights.
Is our statement stated against the canonical form? The bridge (c) is stated as `index = (canonical)/∏ r`, with the canonical form on the RHS, which is OK. It has a superfluous `hP` (evidence (1)).
RHS convention respected? yes.

### Syntactic generality — `Roth.index`

Alternative restatements attempted:
- `ℕ∞`-valued with ℕ weights via `weightedOrder` (compiles as a bridge; not a drop-in, see Q9)
- `⨅ d ∈ (taylor α P).support, weight r d` (same junk value via `Real.iInf`; no gain)
- characterisation by Hasse derivatives (exists as `le_index_iff`)
Chosen restatement: keep (a). It is total in `r`, real-valued as every downstream use needs, and comes with the characterisation lemmas (b), (c), (e).
Justification: call sites do real arithmetic with the index (`index − weight`, `/ l`, `max 0 (index − ν/r)`, `γ − c < index`), so a real-valued def avoids `toNat` casts at about 30 sites.

### Superfluous-argument audit — `Roth.index`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | only through `Roth.weight` | would disappear if `weight` were redefined via `Finsupp.weight` (Roth.weight.md) |
| 2 | `P`, `α`, `r` | yes | — |
| 3 | (in `index_eq_weightedOrder_div`) `hP : P ≠ 0` | no | evidence (1): holds for `P = 0` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE on the def; 1 on the bridge lemma (`hP` of `index_eq_weightedOrder_div`)

Overall: SHIP-AS-STATED (as a project def); RESTATE-BEFORE-SHIP if upstreamed (`ℕ∞` values, ℕ weights, general `R`, descriptive name)

### Call sites — `Roth.index`

Internal use count: about 30 references outside the declaring file (plus all 17 lemmas of Roth/Index.lean)
External-to-file callers: 3 distinct files (MainLemma, Theta, Main), plus a docstring reference in Separation

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:422 | `c ≤ index P α r` (from vanishing of low-weight Hasse derivatives) |
| Roth/MainLemma.lean:455 | `(hc : index P α r < c) : ∃ k : σ →₀ ℕ, ...` |
| Roth/MainLemma.lean:481-483 | `(hγ : γ ≤ index (map (Int.castRingHom ℝ) P) α r) (hz : index (...) z r < c)`, `γ - c < index (map ... Q) α r` |
| Roth/MainLemma.lean:556, 586 | `γ ≤ index (map (Int.castRingHom ℝ) P) (fun _ ↦ α) r` |
| Roth/MainLemma.lean:623, 648, 700 | `gam δ f.natDegree m ≤ index (map (Int.castRingHom ℝ) P) (fun _ ↦ α) r` |
| Roth/MainLemma.lean:743, 749 | `gam ... - eta δ m < index (map ... Q) (fun _ ↦ α) r`; `let c := (index (map ... W) (fun _ ↦ α) r - ...` |
| Roth/Theta.lean:64 | `index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r = x` (definition of `Θ`) |
| Roth/Theta.lean:101, 126, 226 | `index (map ... R) (fun j ↦ h j / q j) r ≤ Θ B q r`, `≤ c` |
| Roth/Theta.lean:381-408 | `∑ ν, max 0 (index R α r - ν / r none) - l * δ ≤ index (det ...) α r`; `index (sign * ∏ ...) = index (∏ ...)` |
| Roth/Theta.lean:418, 465, 561, 586 | `index (map ... (det ...)) ...`; `min_le_sum_max (θ := index (map ... R) α r)` |
| Roth/Main.lean:381 | `(hidx : c ≤ index Q (fun _ ↦ α) r)` |
| Roth/Separation.lean:135 | docstring: "the index of the embedded `Q` is its one-variable index" |

Inline-derivation grep:
  - Roth/Index.lean:143 (`index_eq_weightedOrder_div`) re-expresses the index through `MvPowerSeries.weightedOrder`; this is the bridge, not a bypass.
  - No other site re-derives the minimum of weights over `(taylor α P).support` without `index`.

### Composition check (Phase 6)

Can `Roth.index` be derived from mathlib in ≤3 chained calls?

Attempt 1: `index P α r = ((MvPowerSeries.weightedOrder (fun j ↦ ∏ r / r j) ↑(taylor α P)).toNat : ℝ) / ∏ r`
  - Mathlib decls used: `MvPowerSeries.weightedOrder`, `MvPolynomial.coeToMvPowerSeries`, `ENat.toNat`, `Finsupp.weight`; plus the project's `MvPolynomial.taylor` (not in mathlib)
  - Result: partial. True for all `P` when `0 < r` (evidence (1)), but proving it takes about 12 lines (Index.lean:143–158, through `exists_coeff_ne_zero_and_weightedOrder`, `weightedOrder_le` and the `weight_eq_finsuppWeight_div` rescaling), and it fails without positivity (evidence (4)). `taylor` itself is not in mathlib.

Attempt 2: re-aim the downstream API at `weightedOrder` (what each `index_*` lemma becomes if the index is read through Attempt 1):

| Project lemma | Mathlib counterpart at the `weightedOrder` level | Status |
|---|---|---|
| `index_le_weight` (69) | `MvPowerSeries.weightedOrder_le` | in mathlib |
| `exists_weight_eq_index` (76) | `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder` | in mathlib |
| `le_index_iff` (85) | `MvPowerSeries.le_weightedOrder` / `nat_le_weightedOrder` + `weightedOrder_le` | in mathlib |
| `index_nonneg` (93) | trivial (`0 ≤` in `ℕ∞`) | trivial |
| `index_eq_zero_iff` (98) | weighted analogue of `MvPowerSeries.order_ne_zero_iff_constCoeff_eq_zero` (positive weights) | missing (only the unweighted `order` version) |
| `index_sub_weight_le_index_hasseDeriv` (109) | none (Hasse derivatives are project-only) | project-specific |
| `le_index_sum` (118) | `MvPowerSeries.min_weightedOrder_le_add` (binary; finset version missing) | partial |
| `index_mul` (162) | `MvPowerSeries.weightedOrder_mul` (already used) | in mathlib |
| `index_prod` (175) | `MvPowerSeries.weightedOrder_prod` (evidence (2)) | in mathlib, not yet used by the project |
| `index_neg` (190) | `MvPowerSeries.weightedOrder_neg` (evidence (3)) | in mathlib (current one-line `simp` proof is already fine) |
| `index_C_mul` (195) | only `MvPowerSeries.le_weightedOrder_smul`; equality for nonzero scalars over a domain missing | missing |
| `index_mul_left_weights` (200) | weightedOrder under scaling `w ↦ l • w` | missing |
| `index_rename` (212) | weightedOrder under injective `rename` | missing |
| `index_le_card` (224) | project-specific (box bound) | project-specific |
| `index_unique` (234) | `Polynomial.rootMultiplicity_eq_natTrailingDegree` + `Polynomial.taylor` (already used) | composite |

Conclusion: NOT-COMPOSABLE within ≤3 calls. The bridge is a short proof, not a composition, it needs positive `r`, and `MvPolynomial.taylor` is not in mathlib. With the index read through `weightedOrder`, 6 of the 15 downstream lemmas become direct mathlib calls. The rest are project-specific (3) or need missing `weightedOrder` API (`eq_zero_iff`, `smul` equality, weight scaling, `rename`, finset ultrametric inequality).

### Verdict: `Roth.index`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): standard notion (index in Roth/Schmidt/Evertse: arXiv math/0307203, 2502.00731; clean.tex §4), a weighted order of vanishing at a point. In the general literature it is a monomial valuation, with no single canonical general treatment.
- Generality analysis (Phase 4): narrower than standard in the coefficient ring and `[Fintype σ]`. The mathlib-idiomatic form (ℕ weights, `ℕ∞` values) is not a drop-in replacement (Q9: differs for `r j = 0` and at `P = 0`; evidence (1), (4)), and rebasing is a class-5 foundational restatement.
- Mathlib search (Phase 5): building blocks only (`MvPowerSeries.weightedOrder` at the origin with ℕ weights); no polynomial-level or at-a-point weighted order, no real weights.
- Composition check (Phase 6): NOT-COMPOSABLE in ≤3 calls (12-line bridge, positivity needed, `taylor` not in mathlib); re-aim table above.

**Rationale:**

The project's `index` is the Thue–Siegel–Roth index: the least `r`-weighted degree `∑ d_j/r_j` of a monomial in the support of `P(X + α)`. In this exact form (ℝ-valued, real weights `1/r_j`, junk `0` at `P = 0`, coefficients in ℝ, generic name) it is not a mathlib definition. Mathlib's canonical weighted order is `MvPowerSeries.weightedOrder` (ℕ weights, `ℕ∞`, `⊤` at `0`), and the file already shows `index P α r = (weightedOrder (∏ r / r ·) ↑(taylor α P)).toNat / ∏ r` for positive `r`. Evidence (1) shows this holds without `P ≠ 0`; evidence (4) shows it breaks for `r = 0`, where the `sInf` def still gives `0`. So the mathematically general object, a weighted order of vanishing of a multivariate polynomial at a point, is missing from mathlib. It would be built from `MvPolynomial.taylor` (judged YES-add-as-is) and `weightedOrder`. The real-valued normalisation is a Roth-specific convenience that the downstream real arithmetic needs (about 30 call sites in MainLemma, Theta, Main).

The verdict is BORDERLINE, not YES, because two calls are policy and taste rather than search results: whether mathlib wants a polynomial/at-a-point weighted order as its own def, or just the composite `weightedOrder w ↑(taylor α P)`; and whether the Roth project should rebase its central def on the `ℕ∞` form at EXPENSIVE cost, which would add `0 < r` to lemmas that currently need none. It is not NO-mathlib-has-it, since mathlib has no at-a-point or real-weight version. It is not NO-composable, since the bridge is a real proof that needs positivity and a non-mathlib `taylor`. Locally the def is well chosen and stays. The cheap local wins are dropping `hP` from the bridge and using `weightedOrder_prod` for `index_prod`.

Numbered questions:
1. Should the project upstream a polynomial-level weighted order (`MvPolynomial.weightedOrder w p := (p : MvPowerSeries σ R).weightedOrder w`, plus the order at a point via `taylor`) together with the `MvPolynomial.taylor`/`hasseDeriv` PR? Or is the composite `weightedOrder w ↑(taylor α p)` enough for mathlib?
2. Should the missing `weightedOrder` lemmas surfaced by the re-aim (`weightedOrder_eq_zero_iff` for positive weights, nonzero-scalar `weightedOrder_smul` over a domain, behaviour under `rename` and under weight scaling, a finset `min_weightedOrder_le_sum`) be filed as separate mathlib PRs? They are general and independent of Roth.
3. Should `Roth.index` stay real-valued with the `sInf` definition (recommended; KEEP), or be redefined as `(weightedOrder … ↑(taylor α P)).toNat / ∏ r`? The latter is EXPENSIVE: `0 < r` would be added to `index_le_weight`, `le_index_iff`, `index_rename`, `index_mul_left_weights`, `index_le_card` and `index_unique`, and `toNat` casts would spread to about 30 downstream sites.
4. Should the superfluous `hP : P ≠ 0` be dropped from `index_eq_weightedOrder_div` (Index.lean:143; compiled in evidence (1)), and `index_prod` reproved by `weightedOrder_prod` (evidence (2))?
5. Is generalising the coefficient ring of `index` from ℝ to a `CommSemiring R` wanted? Nothing in the project needs it.

Next action: user answers the questions. Default if unanswered: keep `Roth.index` as is; do question 4 as a cheap local cleanup; treat question 1 as part of the `MvPolynomial.taylor` upstreaming plan.

---

### Next step

Answer questions 1–4. The default is to keep the def, make the cheap bridge cleanup (drop `hP` at Index.lean:143, optionally reprove `index_prod` via `MvPowerSeries.weightedOrder_prod`), and consider an `MvPolynomial` weighted order at a point alongside the `taylor` PR (target `Mathlib/RingTheory/MvPolynomial/`, next to `WeightedHomogeneous.lean`).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.index/index_vs_weightedOrder.lean` (imports `Roth.Index`; `lake env lean` compiles with no output):
  (1) `index_eq_weightedOrder_div'`: the `weightedOrder` formula holds for all `P` (no `P ≠ 0`) when `0 < r`;
  (2) `weightedOrder` of `↑(taylor α (∏ f i))` equals the sum, by `MvPowerSeries.weightedOrder_prod`;
  (3) `weightedOrder` of `↑(taylor α (-P))`, by `MvPowerSeries.weightedOrder_neg`;
  (4) `index_zero_weights`: `index P α 0 = 0` for every `P` (the `sInf` def is total in `r`, unlike the `weightedOrder` form).
  A first draft failed on the nonexistent `MvPolynomial.coe_prod` / `coe_neg` and was fixed via `coeToMvPowerSeries.ringHom_apply` and the argument order of `weightedOrder_prod`.
- Mathlib greps: `weightedOrder` theorems (Order.lean, NoZeroDivisors.lean, Substitution, PiTopology); `rootMultiplicity|weightedOrder|vanishingOrder|orderAt` under MvPolynomial dirs (no hits); `def weightedTotalDegree`; `def index`; `namespace Roth`.
- Lean-Finder (1), LeanSearch (1), Loogle (1) queries as in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: clean.tex §4 index definition and Lean note.
- Project grep `grep -rnw index Roth` for the call-sites table.
