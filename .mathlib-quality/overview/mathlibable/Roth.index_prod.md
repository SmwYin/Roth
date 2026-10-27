---
decl: Roth.index_prod
file: Roth/Index.lean
line: 175
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: Iterated Lemma 4-1 for the project-only def Roth.index; it is MvPowerSeries.weightedOrder_prod transported through index_eq_weightedOrder_div plus ENat.toNat_sum (compiled induction-free proof), hf is necessary in Lean (compiled counterexample), and the subject is not a mathlib notion, so nothing goes upstream.
action: Keep in Roth/Index.lean (sole caller Theta.lean:407); optionally reprove via MvPowerSeries.weightedOrder_prod as in evidence/Roth.index_prod/hyps_and_alt.lean (needs import Mathlib.Data.ENat.BigOperators); do not upstream.
---

# Roth.index_prod

## Inventory entry

### `theorem Roth.index_prod`
- **Type**: `{σ : Type*} [Fintype σ] {ι : Type*} (s : Finset ι) {f : ι → MvPolynomial σ ℝ} (hf : ∀ i ∈ s, f i ≠ 0) (α : σ → ℝ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) : index (∏ i ∈ s, f i) α r = ∑ i ∈ s, index (f i) α r`
- **What**: For a finite family of nonzero real polynomials and positive integer weights `r`, the Roth index at `α` of the product is the sum of the indices.
- **How**: `Finset.induction_on`. Empty case: `Finset.prod_empty`, `Finset.sum_empty`, then `index_eq_zero_iff one_ne_zero hr α` (index of `1` is `0` since `eval α 1 ≠ 0`). Insert case: `Finset.prod_insert`, `Finset.sum_insert`, `index_mul` (nonzeroness of the tail product via `Finset.prod_ne_zero_iff`) and the induction hypothesis.
- **Hypotheses**: `hf : ∀ i ∈ s, f i ≠ 0` (necessary in Lean, evidence (1)); `hr : ∀ j, 0 < r j` (needed by `index_mul` / `index_eq_zero_iff` / the bridge; mathematically expected superfluous, not verified, same situation as `index_mul`).
- **Uses from project**: `Roth.index`, `Roth.index_mul`, `Roth.index_eq_zero_iff`.
- **Used by**: Roth/Theta.lean:407 (index of the product of matrix entries in a determinant term); module docstring Roth/Index.lean:37.
- **Visibility**: public
- **Lines**: 172–186, proof length 10 lines
- **Notes**: Formalises clean.tex Lemma 4-1 iterated, as used at clean.tex line 825 (proof of Lemma 6).

## Junk check (Step 8)
- Used anywhere? Yes: Theta.lean:407.
- Wrapper of 1–2 mathlib calls? Close to it. Up to the project bridge it is `MvPowerSeries.weightedOrder_prod` plus `ENat.toNat_sum` (evidence (2)). But it is about a project def and names the iterated Lemma 4-1.
- Does mathlib have it? No. `Roth.index` is project-only. The only `index_prod` in mathlib is `Subgroup.index_prod` (GroupTheory/Index.lean:621), which is unrelated.
- Too specific (inline)? There is one call site, but the lemma is the natural `_prod` companion of `index_mul` and inlining it would duplicate an induction. Keep it.
- Well-chosen? Yes. `hf` is needed because Lean has `index 0 = 0`.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; no `Roth.index_prod` in mathlib (no `namespace Roth` anywhere in mathlib). Not a glue lemma (10-line induction), so this is a full run. Parent def `Roth.index` is BORDERLINE-needs-human (not NO-mathlib-has-it), so no re-aim.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Index` elaborates with no diagnostics)
- decl `Roth.index_prod`:    resolved at Roth/Index.lean:175
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the Roth index of a real multivariate polynomial at a point and its basic properties (§4 of the source)

### Statement (Phase 1)

`Roth.index_prod` is a theorem stating the following:

Let `σ` be finite and let `P_i ∈ ℝ[X_j : j ∈ σ]` (for `i` in a finite set `S`) be nonzero. Fix `α ∈ ℝ^σ` and positive integers `r_j`. With `ind(P) = min { ∑ d_j / r_j : [X^d] P(X + α) ≠ 0 }`, we have `ind(∏_{i∈S} P_i) = ∑_{i∈S} ind(P_i)`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the variables; `ι`, `s`: the index set; `f`: the family; `α`: the point; `r`: the weights.

Hypotheses (Lean side):
- `hf : ∀ i ∈ s, f i ≠ 0`: excludes zero factors (the source has `ind(0) = +∞`; Lean has `0`).
- `hr : ∀ j, 0 < r j`: weight positivity.

Conclusion (math): the index is additive over finite products.

Conclusion (Lean): `index (∏ i ∈ s, f i) α r = ∑ i ∈ s, index (f i) α r`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: the iterated form of a basic property (Lemma 4-1) of a project definition.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 10 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth index of a product of polynomials equals sum of indices ind(P1...Pl) Roth's theorem lemma | partial | index with weights, Roth's lemma context | hits: Evertse et al. arXiv math/0307203, JTNB 2001 (Faltings product theorem), Ru's Roth notes; no explicit finite-product statement, but the two-factor form is in arXiv 2502.00731 Lemma 2.23 (see Roth.index_mul report) |
| 2 | WebSearch (general form) | valuation of finite product equals sum of valuations monomial valuation weighted order multivariate power series product | partial | weighted (monomial) order is a valuation, so additive over finite products | arXiv math/0212203 (valuations in power series fields); mathlib MvPowerSeries.Order docs surfaced |
| 3 | WebSearch (aliases) | order of vanishing at a point of product of polynomials multiplicity additive weighted index Dyson lemma | yes | multiplicity at a point is multiplicative-additive: `mult_p(PQ) = mult_p(P) + mult_p(Q)` | Tao, polynomial method survey (arXiv 1310.6482) |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep clean.tex for Lemma 4-1 and its iterated use | yes | clean.tex 589–616: `ind(PQ) = ind(P) + ind(Q)`; line 825 (proof of Lemma 6): "By Lemma 4-1" applied to the product `∏_ν Δ...` | the source iterates the two-factor lemma without stating it separately |
| 6 | nLab | valuation | no | abstract valuations only | nothing on weighted orders at a point |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | valuations / order of vanishing | partial | valuations are additive on products (hence finite products) | not the weighted multi-index form |
| 9 | MathOverflow / Math.SE | (covered by searches 2–3) | no | n/a | additivity over finite products follows by induction from the binary case; no dedicated thread |
| 10 | recent arXiv | 2502.00731, 1310.6482 | yes | same as #1, #3 | the standard form is "monomial valuation is a valuation" |

### Literature summary (Phase 3)

Concept identified as: additivity of a monomial (weighted) valuation centred at a point, iterated over a finite product.
Sources agree on the standard form: yes. `v(∏ f_i) = ∑ v(f_i)` over a domain, with `v(0) = +∞`, by induction from `v(fg) = v(f) + v(g)`.
Most general standard form: for any integral domain, any nonnegative weights, any point, and any finite family, the weighted order of the product is the sum of the orders, with no nonzeroness hypothesis in `ℕ∞`.
Generality dimensions where the literature varies:
  - weights: nonnegative reals vs `1/r_j` (Roth) vs naturals (mathlib).
  - zero convention: `+∞` vs the project's `0`.
  - coefficients: any domain vs `ℝ`.
Disagreement with the literature: none in substance; `hf` is an artefact of `ind(0) = 0`.

### Generality analysis — `Roth.index_prod`

Literature-standard form: `ord_{α,w}(∏ f_i) = ∑ ord_{α,w}(f_i)` in `ℕ∞` for every finite family over a domain.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hf : ∀ i ∈ s, f i ≠ 0` | required | none (with `ord 0 = +∞`) | NO (for this statement) | evidence (1): `f false = 0`, `f true = X true` gives `0 ≠ 0 + 1`; compiled |
| 2 | `hr : ∀ j, 0 < r j` | required | any nonnegative weights | likely yes mathematically, not mechanically | the same situation as `index_mul`: it would need a generalised bridge. Not verified, MODERATE, and the only caller has positive `r` |
| 3 | `ι`, `s : Finset ι` | arbitrary finset | arbitrary finite family | n/a | already general |
| 4 | ring `ℝ` | fixed | any domain | not for this statement | `Roth.index` is defined only over `ℝ` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (no verified weakening; `hf` provably needed; dropping `hr` is unverified)
Number of weakening opportunities found: 0 verified
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | data-level positivity | — |
| 2 | Sequences vs filters? | no | finite algebraic identity | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | in principle | an `ℕ∞`-valued polynomial weighted order at a point over a domain would make this `weightedOrder_prod` directly | parent-def question (Roth.index BORDERLINE) |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | partial | "index is (a scaling of) an `AddValuation`", which gives `map_prod`-style lemmas for free | parent-def redesign |
| 8 | Concrete-via-abstract? | yes (diagnostic fires on evidence (2)) | in the induction-free proof, `index` disappears after the first rewrite and the content is `MvPowerSeries.weightedOrder_prod` | the abstract form already exists in mathlib |
| 9 | False-generalisation guard | no false generalisation | the `ℕ∞` form agrees for nonzero factors | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (for this lemma)
  - Reason: the abstract content is already in mathlib as `MvPowerSeries.weightedOrder_prod`. Modernising further means redesigning the parent def, which is assessed separately.

### Proof strategy — `Roth.index_prod`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | the induction re-derives the finite-product case; mathlib's `MvPowerSeries.weightedOrder_prod` does it once (evidence (2), 6 lines, compiles; needs `import Mathlib.Data.ENat.BigOperators` for `ENat.toNat_sum`) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (induction on the binary lemma is the standard `_prod` derivation; the alternative via `weightedOrder_prod` is equally short, so it is not a required refactor)
  - Optional alternative: evidence (2), induction-free through `MvPowerSeries.weightedOrder_prod`, `ENat.toNat_sum`, `Nat.cast_sum`, `Finset.sum_div`. It removes the dependence on `index_mul` and `index_eq_zero_iff` but adds an import.
  - Missing mathlib API: none.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.index_prod`

[A] Lean-Finder       "weighted order of a finite product of multivariate polynomials equals sum of weighted orders"   hits: `MvPowerSeries.weightedOrder_prod`, `le_weightedOrder_prod`, `weightedOrder_mul`, `MvPolynomial.IsWeightedHomogeneous.prod` (power-series / homogeneity, not an index at a point)
[B] Loogle            `MvPowerSeries.weightedOrder, Finset.prod`   hits: `weightedOrder_prod`, `le_weightedOrder_prod`, `coeff_mul_prod_one_sub_of_lt_weightedOrder`, `summable_prod_of_tendsto_weightedOrder_atTop_nhds_top`
[C] LeanSearch        "order of vanishing of a finite product of polynomials is the sum of the orders"   hits: `analyticOrderAt_smul`, `analyticOrderNatAt_mul`, `Polynomial.rootMultiplicity_mul`, `meromorphicOrderAt_mul` (one-variable analogues)
[D] Grep mathlib src  `theorem index_prod`, `namespace Roth`, `weightedOrder_prod`   only `Subgroup.index_prod` (unrelated); `weightedOrder_prod` at Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean:176
[E] Name pattern      `Roth.index_prod`, `index_prod`   no mathlib decl in a matching namespace

Searched for both:
  - the user's current form (Roth index additive on finite products)
  - the literature-standard form (weighted order at a point additive on finite products)

Concluded: found building blocks (`MvPowerSeries.weightedOrder_prod`, `MvPolynomial.coeToMvPowerSeries.ringHom_apply`, `map_prod`, `ENat.toNat_sum`, `Nat.cast_sum`, `Finset.sum_div`); composed with the project bridge `index_eq_weightedOrder_div` they yield our form (evidence (2)).

### Normal-form check — `Roth.index_prod`

Equivalent formalisms: (a) this `ℝ`-valued finite-product additivity; (b) `MvPowerSeries.weightedOrder_prod` in `ℕ∞`; (c) `AddValuation` `map_prod`.
Does mathlib already have a canonical form? yes: `MvPowerSeries.weightedOrder_prod` (product on the LHS, sum on the RHS).
Our statement has the same shape and the `_prod` naming convention. OK.
RHS convention respected? yes

### Syntactic generality — `Roth.index_prod`

Alternative restatements attempted:
- current (`s` explicit, `f` implicit, membership-guarded `hf`)
- `hf : ∀ i, f i ≠ 0` (unguarded): strictly harder to supply; rejected
- `Fintype ι` with `∏ i, f i`: a special case of the current form (the caller uses `s = univ`); rejected

Chosen restatement: current.
Justification: the membership-guarded `hf` matches mathlib's `Finset.prod_ne_zero_iff` and is what the caller supplies (`fun i _ ↦ hentry i`).

### Superfluous-argument audit — `Roth.index_prod`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed by `Roth.index` |
| 2 | `hf` | yes | evidence (1), compiled counterexample |
| 3 | `hr` | yes for the proof | conclusion likely holds without it; unverified; caller has positive `r` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE verified

Overall: SHIP-AS-STATED (locally; not a mathlib candidate)

### Call sites — `Roth.index_prod`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:407 | `rw [hidx, index_prod _ (fun i _ ↦ hentry i) α hr, ...` (index of `∏ i, Matrix.of E (s i) i` in a determinant term) |
| Roth/Index.lean:37 | module docstring entry |

Inline-derivation grep:
  - (none) — no other site re-derives a finite-product index identity; no use of `weightedOrder_prod` in `Roth/`.

### Composition check (Phase 6)

Can `Roth.index_prod` be derived from mathlib in ≤3 chained calls?

Attempt 1: rewrite with `index_eq_weightedOrder_div`, push the product through `taylor` and the coercion ring hom, apply `MvPowerSeries.weightedOrder_prod`, and finish with `ENat.toNat_sum`, `Nat.cast_sum`, `Finset.sum_div`, then the bridge termwise.
  - Mathlib decls used: `MvPowerSeries.weightedOrder_prod` (Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean:176), `MvPolynomial.coeToMvPowerSeries.ringHom_apply` (Mathlib/RingTheory/MvPowerSeries/Basic.lean:918), `map_prod`, `ENat.toNat_sum` (Mathlib/Data/ENat/BigOperators.lean:75), `Nat.cast_sum`, `Finset.sum_div`, `Finset.prod_ne_zero_iff`.
  - Result: succeeds (evidence (2), compiled).
  - Notes: one rewrite chain plus a termwise `sum_congr`. The only non-mathlib ingredient is the project bridge `index_eq_weightedOrder_div`.

Attempt 2: `Finset.induction_on` with `index_mul` (the current proof). It succeeds, and it is the standard derivation of `_prod` from `_mul`.

Conclusion: COMPOSABLE (with the project's own bridge; no residual statement for mathlib).

## Verdict: `Roth.index_prod`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): standard fact, the iteration of "monomial valuations are valuations"; the source iterates Lemma 4-1 at clean.tex line 825.
- Generality analysis (Phase 4): MAXIMALLY GENERAL in the Lean convention. `hf` is necessary (compiled counterexample).
- Mathlib search (Phase 5): building block `MvPowerSeries.weightedOrder_prod` and helpers. Nothing exists on polynomials at a point.
- Composition check (Phase 6): COMPOSABLE (evidence (2)).

**Rationale:**

Mathematically, the lemma is mathlib's `MvPowerSeries.weightedOrder_prod` read through the project's translation `index_eq_weightedOrder_div` of the `ℝ`-valued Roth index into an integer-weighted order. Evidence (2) compiles an induction-free proof along exactly this route. The current proof derives it instead by induction from `index_mul`, which is itself `weightedOrder_mul` transported. Either way, `Roth.index` is not a mathlib notion (the Roth.index report rated it BORDERLINE). An upstream `ℕ∞`-valued weighted order at a point would get this as `weightedOrder_prod` composed with `map_prod`, so no `index_prod` would be needed there.

`hf` is needed because Lean uses `index 0 = 0`. Evidence (1) shows the failure for `{0, X true}`. Like `index_mul`, the lemma probably holds without `hr`, but proving that needs a generalised bridge, and the only caller has positive `r`.

WHY not: the lemma is one mathlib lemma (`MvPowerSeries.weightedOrder_prod`) transported through a project bridge about a project def. It contributes nothing new to mathlib.
Belongs-elsewhere check: keep it project-local in Roth/Index.lean as the `_prod` companion of `index_mul`. It is used at Theta.lean:407, and inlining it there would replace one rewrite with an induction or a six-step chain.
Mathlib building blocks: `MvPowerSeries.weightedOrder_prod` (Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean:176), `MvPolynomial.coeToMvPowerSeries.ringHom_apply` (Mathlib/RingTheory/MvPowerSeries/Basic.lean:918), `ENat.toNat_sum` (Mathlib/Data/ENat/BigOperators.lean:75), `Nat.cast_sum`, `Finset.sum_div`.
Composition sketch:
```lean
rw [index_eq_weightedOrder_div (Finset.prod_ne_zero_iff.2 hf) hr, map_prod,
  ← MvPolynomial.coeToMvPowerSeries.ringHom_apply, map_prod, MvPowerSeries.weightedOrder_prod,
  ENat.toNat_sum fun i hi ↦ by simp [hf i hi], Nat.cast_sum, Finset.sum_div]
exact Finset.sum_congr rfl fun i hi ↦ (index_eq_weightedOrder_div (hf i hi) hr α).symm
```
Call sites in our project (from Phase 6.0): 1 (Roth/Theta.lean:407).
Refactor plan: do not inline; keep the named lemma for Theta.lean:407. The proof may optionally be replaced by the composition above, which needs `import Mathlib.Data.ENat.BigOperators` in Roth/Index.lean. This is cosmetic: both proofs are about 10 lines.
Next action: keep locally; do not upstream.

## Next step

Keep `Roth.index_prod` in Roth/Index.lean with its current signature. Do not upstream it: its abstract content is `MvPowerSeries.weightedOrder_prod`. Optionally swap in the induction-free proof from evidence (2).

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_prod/hyps_and_alt.lean` (imports `Roth.Index` and `Mathlib.Data.ENat.BigOperators`; `lean_diagnostic_messages`: no diagnostics):
  - (1) an `example` showing the conclusion fails for `s = univ : Finset Bool`, `f false = 0`, `f true = X true`, `α = 0`, `r = 1`: LHS `0`, RHS `1`. So `hf` is necessary.
  - (2) an `example` reproving `index_prod` without induction via `MvPowerSeries.weightedOrder_prod`, `ENat.toNat_sum`, `Nat.cast_sum`, `Finset.sum_div` and the bridge `index_eq_weightedOrder_div`.
- WebSearch ×3 (queries in the table); local grep of `.mathlib-quality/references/clean.tex` (Lemma 4-1 at lines 589–616, iterated use at line 825); Lean-Finder, Loogle, LeanSearch, and a mathlib grep as recorded in Phase 5.
- ChatGPT channel n/a: the `ask_chatgpt_math` MCP is not configured in this session.
