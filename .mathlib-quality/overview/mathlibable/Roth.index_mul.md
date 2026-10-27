---
decl: Roth.index_mul
file: Roth/Index.lean
line: 162
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: Lemma 4-1 (ind(PQ) = ind P + ind Q) for the project-only def Roth.index is MvPowerSeries.weightedOrder_mul transported through index_eq_weightedOrder_div plus ENat.toNat_add; hP and hQ are necessary in Lean (compiled counterexample, since index 0 = 0 not +infinity), and the subject is not a mathlib notion, so nothing goes upstream.
action: Keep in Roth/Index.lean (used by index_prod at Index.lean:185 and Theta.lean:438); if index_eq_weightedOrder_div drops its superfluous hP, simplify the three rewrites at Index.lean:164-165; do not upstream.
---

# Roth.index_mul

## Inventory entry

### `theorem Roth.index_mul`
- **Type**: `{σ : Type*} [Fintype σ] {P Q : MvPolynomial σ ℝ} (hP : P ≠ 0) (hQ : Q ≠ 0) (α : σ → ℝ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) : index (P * Q) α r = index P α r + index Q α r`
- **What**: For nonzero real polynomials `P`, `Q` and positive integer weights `r`, the Roth index at `α` is additive: `ind(PQ) = ind(P) + ind(Q)`.
- **How**: Rewrites all three indices with `index_eq_weightedOrder_div` (natural weights `w_j = ∏ r / r_j`), merges with `← add_div`, pushes the product through `taylor` (`map_mul`) and the power-series coercion (`MvPolynomial.coe_mul`), applies `MvPowerSeries.weightedOrder_mul`, and closes with `ENat.toNat_add` (finiteness by `simp`, from nonzeroness) and `Nat.cast_add`.
- **Hypotheses**: `hP`, `hQ : _ ≠ 0` (necessary in Lean, evidence (1)); `hr : ∀ j, 0 < r j` (used by the proof through `index_eq_weightedOrder_div`; mathematically expected to be superfluous, not verified, see Phase 4).
- **Uses from project**: `Roth.index`, `Roth.index_eq_weightedOrder_div`, `MvPolynomial.taylor` (via `map_mul` on the algebra hom).
- **Used by**: Roth/Index.lean:185 (`index_prod`, insert step); Roth/Theta.lean:438 (Lemma 4-2-style split of an index over a product of renamed polynomials); module docstring Roth/Index.lean:37.
- **Visibility**: public
- **Lines**: 160–169, proof length 7 lines
- **Notes**: Formalises clean.tex §4 Lemma 4-1 (multiplicative half), following the paper's Lean note ("For integral r_j, apply weightedOrder_mul through translation and the normalisation").

## Junk check (Step 8)
- Used anywhere? Yes: `index_prod` (Index.lean:185) and Theta.lean:438.
- Wrapper of 1–2 mathlib calls? Close to it: one mathlib lemma (`MvPowerSeries.weightedOrder_mul`) plus the project bridge `index_eq_weightedOrder_div` and `ENat.toNat_add`. But it states a named source lemma (Lemma 4-1) about a project def and is used in two files, so it is real API.
- Does mathlib have it? No: `Roth.index` is project-only; mathlib has the power-series analogue `MvPowerSeries.weightedOrder_mul`.
- Too specific (inline)? No: two call sites, and it is the paper's Lemma 4-1.
- Well-chosen? Yes. `hP`/`hQ` are needed because Lean's `index 0 = 0` (not `+∞`).
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; no `Roth.index_mul` in mathlib (no `namespace Roth` there; `index_mul_card` in GroupTheory/Index.lean is unrelated). Not a glue lemma (7-line rewrite proof), so full run. Parent def `Roth.index` is BORDERLINE-needs-human (not NO-mathlib-has-it), so no re-aim.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Index` elaborates with no diagnostics)
- decl `Roth.index_mul`:     resolved at Roth/Index.lean:162
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the Roth index of a real multivariate polynomial at a point and its basic properties (§4 of the source)

### Statement (Phase 1)

`Roth.index_mul` is a theorem stating the following:

Let `P, Q ∈ ℝ[X_j : j ∈ σ]` be nonzero (σ finite), `α ∈ ℝ^σ`, and `r_j` positive integers. Let `ind(P) = min { ∑ d_j / r_j : the coefficient of X^d in P(X + α) is nonzero }`. Then `ind(PQ) = ind(P) + ind(Q)`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the variables; `P`, `Q`: the polynomials; `α`: the point; `r`: the integer weights.

Hypotheses (Lean side):
- `hP : P ≠ 0`, `hQ : Q ≠ 0`: the source uses `ind(0) = +∞`; Lean's real-valued index has `ind(0) = 0`, so the zero case must be excluded.
- `hr : ∀ j, 0 < r j`: positivity of the weights (needed by the bridge to `weightedOrder`).

Conclusion (math): the index is additive on products.

Conclusion (Lean): `index (P * Q) α r = index P α r + index Q α r`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a basic property of a project definition (Lemma 4-1 of the source), not a main result and not named after anyone.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 7 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma index of product of polynomials ind(PQ) = ind(P) + ind(Q) weighted | yes | Ind(PQ) = Ind(P) + Ind(Q) for the Roth index with fixed weights | arXiv 2502.00731 Lemma 2.23(1); arXiv math/9708214 (index as weighted multiplicity); a different "index" in arXiv 0807.2620 picks up a resultant term (unrelated notion) |
| 2 | WebSearch (general form) | weighted order of product of power series additive integral domain initial form lowest weighted homogeneous component | yes | order is an additive valuation over a domain; initial form of a product is the product of initial forms | Encyclopedia of Mathematics "formal power series"; mathlib MvPowerSeries.Order docs surfaced |
| 3 | WebSearch (aliases: valuation) | order of vanishing at a point multiplicative valuation monomial valuation multiplicity of product polynomials | yes | monomial valuation v_s(f) = min ∑ s_i d_i over monomials (nonneg real weights) is a valuation: v(fg) = v(f) + v(g) | Favre–Jonsson "The valuative tree" (math/0210265); Gathmann comm. alg. notes ch. 12 |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep clean.tex for Lemma 4-1 / weightedOrder_mul | yes | clean.tex lines 589–616: Lemma 4-1 `ind(PQ) = ind(P) + ind(Q)` with `ind(0) = +∞`, proof via lowest-weight components in a domain; Lean note: "For integral r_j, apply weightedOrder_mul through translation and the normalisation" | the Lean proof follows the Lean note exactly |
| 6 | nLab | valuation / order of vanishing | no | n/a | nLab has "valuation" abstractly; nothing on weighted orders of polynomials at a point |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | order of vanishing / valuations | partial | discrete valuations and orders of vanishing along divisors are additive | not the weighted multi-index form; monomial valuations not treated |
| 9 | MathOverflow / Math.SE | (covered by searches 2–3) | no | n/a | additivity of monomial/weighted valuations is textbook; no dedicated thread found |
| 10 | recent arXiv | Roth/subspace index (2502.00731), valuative tree | yes | same statement as #1 and #3 | confirms the standard form is "monomial valuation is a valuation" |

### Literature summary (Phase 3)

Concept identified as: additivity of the Roth index, i.e. the fact that a monomial (weighted) valuation centred at a point is a valuation.
Sources agree on the standard form: yes — `v(fg) = v(f) + v(g)` for the monomial valuation with nonnegative real weights over a domain, with `v(0) = +∞`.
Most general standard form: for any integral domain `R`, any nonnegative (real) weight vector, and the translate at any point, the weighted order is a valuation (additive on products, ultrametric on sums), with value `+∞` at `0`.
Generality dimensions where the literature varies:
  - weights: nonnegative reals (valuation theory) vs positive reciprocals `1/r_j` (Roth) vs natural numbers (mathlib `weightedOrder`).
  - zero convention: `+∞` (literature, mathlib `ℕ∞`) vs `0` (project's `ℝ`-valued `sInf`).
  - coefficients: any domain vs `ℝ` (project).
Disagreement with the literature: none in substance; the Lean form needs `P, Q ≠ 0` only because it uses `ind(0) = 0`.

### Generality analysis — `Roth.index_mul`

Literature-standard form: `ord_{α,w}(PQ) = ord_{α,w}(P) + ord_{α,w}(Q)` in `ℕ∞`/`ℝ≥0∞` for all `P, Q` over a domain, any nonnegative weights.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hP : P ≠ 0` | required | none (with `ind(0)=+∞`) | NO (for this statement) | evidence (1): `P = 0`, `Q = X true` gives `0 ≠ 0 + 1`; compiled. Only an `ℕ∞`-valued restatement would drop it |
| 2 | `hQ : Q ≠ 0` | required | none | NO | symmetric to row 1 |
| 3 | `hr : ∀ j, 0 < r j` | required | any nonnegative weights | likely yes mathematically, not mechanically | with `r_j = 0` Lean's weight term is `d_j/0 = 0`, i.e. weight `0`, and monomial valuations with zero weights are still additive; but the proof goes through `index_eq_weightedOrder_div`, whose `hr` is necessary (compiled counterexample in that report). A weakening would need a generalised bridge (`w_j = 0` when `r_j = 0`, `D = ∏_{r_j ≠ 0} r_j`). Not verified; MODERATE |
| 4 | ring `ℝ` | fixed | any integral domain | not for this statement | `Roth.index` is defined only over `ℝ` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (no weakening verified; `hP`/`hQ` provably needed in the Lean convention; the `hr` drop is unverified and would need a new bridge lemma)
Number of weakening opportunities found: 0 verified (1 conjectured: `hr`, MODERATE, not needed by any call site — both callers have positive `r`)
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | positivity of `r` is data-level | — |
| 2 | Sequences vs filters? | no | finite algebraic statement | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | yes in principle | an `ℕ∞`-valued weighted order at a point for `MvPolynomial σ R`, `R` a domain, would make this `MvPowerSeries.weightedOrder_mul` directly | belongs to the parent-def question (Roth.index BORDERLINE), not to this lemma |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | partial | the modern idiom is "the index is (the ℝ-scaling of) an `AddValuation`" | `AddValuation` API (map_add, map_mul, map_prod); again a parent-def redesign |
| 8 | Concrete-via-abstract? | yes (diagnostic fires) | after the first `rw [index_eq_weightedOrder_div ...]` the body never mentions `index` again; it is pure `MvPowerSeries.weightedOrder_mul`. The abstract statement is already mathlib's `weightedOrder_mul` | nothing new to add: the abstract form exists |
| 9 | False-generalisation guard | no false generalisation | the `ℕ∞` form agrees with this one for nonzero `P, Q` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (for this lemma)
  - Reason: the abstract content is already in mathlib as `MvPowerSeries.weightedOrder_mul` (Q8 points straight at it); any further modernisation (`ℕ∞`-valued polynomial weighted order or an `AddValuation`) is a redesign of the parent def `Roth.index`, assessed separately as BORDERLINE.

### Proof strategy — `Roth.index_mul`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | minor | the `hfin` side condition (`weightedOrder ≠ ⊤` from `≠ 0`) is `MvPowerSeries.ne_zero_iff_weightedOrder_finite`, closed by `simp`; nothing missing | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (transport through the bridge, apply `MvPowerSeries.weightedOrder_mul`, which is exactly the paper's Lean note).
  - Missing mathlib API: none. Related local remark (from the Roth.index report): `index_prod` could likewise use `MvPowerSeries.weightedOrder_prod` instead of induction on `index_mul`.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.index_mul`

[A] Lean-Finder       "weighted order of product of multivariate polynomials equals sum of weighted orders, order of vanishing at a point is additive"   hits: `MvPowerSeries.weightedOrder_mul`, `MvPowerSeries.weightedOrder_prod`, `le_weightedOrder_mul`, `le_weightedOrder_prod` (power series only)
[B] Loogle            `MvPowerSeries.weightedOrder (_ * _)`   no hits (pattern form); name search confirms `weightedOrder_mul` at Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean:146
[C] LeanSearch        "order of vanishing of product of polynomials at a point equals sum of orders"   hits: `analyticOrderAt_smul`, `analyticOrderNatAt_mul`, `meromorphicOrderAt_mul`, `Polynomial.rootMultiplicity_mul'` (one-variable / analytic analogues, not multivariate weighted)
[D] Grep mathlib src  `weightedOrder_mul`, `coe_mul` (MvPolynomial to MvPowerSeries, RingTheory/MvPowerSeries/Basic.lean:864), `index_mul` (only `Subgroup.index_mul_card`, unrelated)   no polynomial-level or at-a-point weighted-order additivity
[E] Name pattern      `Roth.index_mul`, `index_mul`   no mathlib decl in a matching namespace

Searched for both:
  - the user's current form (Roth index additive on products)
  - the literature-standard form (weighted/monomial order at a point is additive over a domain)

Concluded: found building blocks (`MvPowerSeries.weightedOrder_mul`, `MvPolynomial.coe_mul`, `ENat.toNat_add`, `MvPowerSeries.ne_zero_iff_weightedOrder_finite`); composition with the project bridge `index_eq_weightedOrder_div` yields our form.

### Normal-form check — `Roth.index_mul`

Equivalent formalisms: (a) additivity of the `ℝ`-valued index for nonzero factors (this lemma); (b) additivity of an `ℕ∞`-valued weighted order (mathlib `weightedOrder_mul`); (c) `AddValuation` map_mul.
Does mathlib already have a canonical form? yes — `MvPowerSeries.weightedOrder_mul` (`f * g` on the LHS, sum on the RHS).
Our statement has the same shape (`index (P * Q) = index P + index Q`), matching mathlib's `_mul` convention. OK.
RHS convention respected? yes

### Syntactic generality — `Roth.index_mul`

Alternative restatements attempted:
- current (hypotheses `hP hQ`, explicit `α`, implicit `r`)
- `ℕ∞`-valued version without `hP hQ` (not available: `index` is `ℝ`-valued)
- `index (P * Q) α r = index P α r + index Q α r` with `P Q` explicit (no gain: nonzeroness proofs already determine them)

Chosen restatement: current.
Justification: both callers supply nonzeroness proofs and positive `r` directly; the current argument order matches `index_prod` and Theta.lean:438.

### Superfluous-argument audit — `Roth.index_mul`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed by `Roth.weight` / `Roth.index` |
| 2 | `hP : P ≠ 0` | yes | evidence (1), compiled counterexample |
| 3 | `hQ : Q ≠ 0` | yes | symmetric to `hP` |
| 4 | `hr : ∀ j, 0 < r j` | yes for the proof; conclusion likely holds without it | not verified (needs a generalised bridge); no caller benefits |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE verified

Overall: SHIP-AS-STATED (locally; not a mathlib candidate)

### Call sites — `Roth.index_mul`

Internal use count: 1 outside the declaring file (plus 1 inside)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:185 | `index_mul (hf a (Finset.mem_insert_self a s)) (Finset.prod_ne_zero_iff.2 ...) α hr,` (in `index_prod`) |
| Roth/Theta.lean:438 | `index_mul ((map_ne_zero_iff (rename (R := ℝ) some) ...).2 hmU) (...) _ hr0,` (index of a product of renamed polynomials) |
| Roth/Index.lean:37 | module docstring entry |

Inline-derivation grep:
  - (none) — no other site applies `MvPowerSeries.weightedOrder_mul` to an index; `index_prod` goes through `index_mul`.

### Composition check (Phase 6)

Can `Roth.index_mul` be derived from mathlib in ≤3 chained calls?

Attempt 1: rewrite the three indices with `index_eq_weightedOrder_div`, then `MvPowerSeries.weightedOrder_mul`, then `ENat.toNat_add`.
  - Mathlib decls used: `MvPowerSeries.weightedOrder_mul` (Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean:146), `MvPolynomial.coe_mul` (Mathlib/RingTheory/MvPowerSeries/Basic.lean:864), `map_mul`, `add_div`, `ENat.toNat_add`, `Nat.cast_add`, `MvPowerSeries.ne_zero_iff_weightedOrder_finite` (via `simp`).
  - Result: succeeds (it is the current proof). The one non-mathlib ingredient is the project bridge `index_eq_weightedOrder_div` (itself NO-composable-from-mathlib).
  - Notes: a single rewrite chain plus a `toNat_add` finish; no new mathematics beyond `weightedOrder_mul`.

Conclusion: COMPOSABLE (mathlib's `weightedOrder_mul` composed with the project's own bridge; no residual statement for mathlib).

## Verdict: `Roth.index_mul`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): standard fact (clean.tex Lemma 4-1; arXiv 2502.00731 Lemma 2.23; monomial valuations are valuations).
- Generality analysis (Phase 4): MAXIMALLY GENERAL in the Lean convention. `hP`/`hQ` necessary (compiled counterexample); the `hr` drop is unverified and MODERATE.
- Mathlib search (Phase 5): building blocks `MvPowerSeries.weightedOrder_mul`, `MvPolynomial.coe_mul`, `ENat.toNat_add`. Nothing on polynomials or at a point.
- Composition check (Phase 6): COMPOSABLE.

**Rationale:**

Mathematically the lemma is mathlib's `MvPowerSeries.weightedOrder_mul` read through the project's translation of the `ℝ`-valued Roth index into an integer-weighted order: `index_eq_weightedOrder_div` with weights `w_j = ∏ r / r_j`, then a division by `∏ r`. Once that bridge has been rewritten in, the proof never mentions `index` again (the Q8 diagnostic fires), and the abstract statement it reduces to is already in mathlib. Its subject `Roth.index` is not a mathlib notion: the Roth.index report rated it BORDERLINE. Any upstream version would be an `ℕ∞`-valued weighted order at a point, and there additivity would be `weightedOrder_mul` composed with `coe_mul` and `map_mul` on `taylor`, with no `index_mul` needed.

`hP` and `hQ` are genuinely needed in the Lean statement. The source uses `ind(0) = +∞`, but Lean's `sInf ∅ = 0` gives `index 0 = 0`. Evidence (1) compiles the failure for `P = 0`, `Q = X true`. Positivity of `r` is needed by the proof route. The conclusion itself probably survives `r_j = 0`, since that coordinate then just gets weight 0. Proving it would need a generalised bridge, though, and both callers have positive `r`, so no change is recommended.

WHY not: the lemma is one mathlib lemma (`MvPowerSeries.weightedOrder_mul`) transported through a project bridge about a project def. It adds nothing to mathlib.
Belongs-elsewhere check: keep it project-local in Roth/Index.lean. It is the source's Lemma 4-1 and is consumed by `index_prod` and Theta.lean:438. Inlining it at both sites would duplicate the rewrite chain and lose the named reference to Lemma 4-1.
Mathlib building blocks: `MvPowerSeries.weightedOrder_mul` (Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean:146), `MvPolynomial.coe_mul` (Mathlib/RingTheory/MvPowerSeries/Basic.lean:864), `MvPowerSeries.ne_zero_iff_weightedOrder_finite` (Mathlib/RingTheory/MvPowerSeries/Order.lean), `ENat.toNat_add`.
Composition sketch:
```lean
rw [index_eq_weightedOrder_div hP hr, index_eq_weightedOrder_div hQ hr,
  index_eq_weightedOrder_div (mul_ne_zero hP hQ) hr, ← add_div, map_mul, MvPolynomial.coe_mul,
  MvPowerSeries.weightedOrder_mul, ENat.toNat_add (by simpa using hP) (by simpa using hQ), Nat.cast_add]
```
Call sites in our project (from Phase 6.0): 2 (Roth/Index.lean:185, Roth/Theta.lean:438).
Refactor plan: do not inline. Keep the lemma as the named form of Lemma 4-1 for its two call sites. If `index_eq_weightedOrder_div` drops its superfluous `hP` (per that report), remove the nonzeroness arguments from the three rewrites at Index.lean:164–165. `hP`/`hQ` stay in `index_mul`'s own signature. Optionally reprove `index_prod` through `MvPowerSeries.weightedOrder_prod` (see the Roth.index report).
Next action: keep locally; do not upstream.

## Next step

Keep `Roth.index_mul` in Roth/Index.lean with its current signature. Do not upstream it: its abstract content is `MvPowerSeries.weightedOrder_mul`. Simplify Index.lean:164–165 only if the `hP` drop on `index_eq_weightedOrder_div` lands.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_mul/hyps.lean` (imports `Roth.Index`; `lean_diagnostic_messages`: no diagnostics):
  - (1) an `example` showing the conclusion fails for `P = 0`, `Q = X true` (`σ = Bool`, `α = 0`, `r = 1`): LHS `0`, RHS `1`. So `hP` (and symmetrically `hQ`) is necessary.
  - (2) an `example` checking that `MvPowerSeries.weightedOrder_mul` applies to any `w : σ → ℕ` (zero weights included), the building block in Phase 6.
- WebSearch ×3 (queries in the table); local grep of `.mathlib-quality/references/clean.tex` (Lemma 4-1, lines 589–616, and the Lean note); Lean-Finder, LeanSearch, Loogle, and a mathlib grep as recorded in Phase 5.
- ChatGPT channel n/a: the `ask_chatgpt_math` MCP is not configured in this session.
