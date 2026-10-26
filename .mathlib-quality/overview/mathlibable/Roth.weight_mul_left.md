---
decl: Roth.weight_mul_left
file: Roth/Box.lean
line: 110
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: Re-aimed at Finsupp.weight (parent is NO-mathlib-has-it), mathlib has no weight-is-linear-in-w lemma, but weight (c • w) f = c • weight w f is one simp via Finsupp.smul_sum and smul_comm, and the project form is one simp via Finset.sum_div and div_div (all verified).
action: Keep as project-local API in Roth/Box.lean for its single call site Roth/Index.lean:206 (index_mul_left_weights); no mathlib PR.
---

# Roth.weight_mul_left

## Inventory entry

### `theorem Roth.weight_mul_left`
- **Type**: `{σ : Type*} [Fintype σ] {l : ℕ} (r : σ → ℕ) (d : σ →₀ ℕ) : Roth.weight (fun j ↦ l * r j) d = Roth.weight r d / l`
- **What**: Scaling every parameter `r j` by the same natural number `l` divides the weight `∑ j, d j / r j` by `l`.
- **How**: One `simp [weight, Finset.sum_div, div_div, mul_comm]`: unfold to the sum, pull `/ l` inside with `Finset.sum_div`, merge with `div_div`, commute the product. Holds for `l = 0` too (both sides `0` under `x / 0 = 0`).
- **Hypotheses**: none (section variable `[Fintype σ]`).
- **Uses from project**: `Roth.weight`
- **Used by**: Roth/Index.lean:206 (`index_mul_left_weights`, `rw [weight_mul_left, smul_eq_mul, div_eq_inv_mul]` inside the image computation).
- **Visibility**: public
- **Lines**: 107–111, proof length 1 line
- **Notes**: Docstring cites clean.tex §4 l.639 (`ind(P; α; l r) = (1/l) ind(P; α; r)`); the paper's Lean note (l.630–634) asks for "scaling of the index weights" as a separate lemma.

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/Index.lean:206).
- Wrapper of 1–2 mathlib calls? Yes: `Finset.sum_div` + `div_div` after unfolding.
- Does mathlib have it? Not for `Roth.weight`; re-aimed at `Finsupp.weight` there is no `weight_smul`-type lemma (loogle `Finsupp.weight (_ • _)` empty), but the general form is one `simp` (evidence).
- Too specific (inline)? Single call site; inlining would require unfolding `weight` inside a `Set.image_congr` at Index.lean:206. The paper explicitly asks for this as a separate lemma, and it pairs with `index_mul_left_weights`. Keep.
- Well-chosen? Yes.
- Conclusion: `KEEP` — action: keep in Roth/Box.lean unchanged.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.weight_mul_left` not in mathlib (no `namespace Roth` in Mathlib). Not a glue lemma (a `simp` proof, not `rfl`). Parent `Roth.weight` is `NO-mathlib-has-it` because it equals `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`, so per the re-aim rule this run is re-aimed at `Finsupp.weight`: target statement `Finsupp.weight (c • w) f = c • Finsupp.weight w f` (linearity of the weighted degree in the weight vector), of which the project lemma is the case `c = (l : ℝ)⁻¹`, `w = fun j ↦ (r j : ℝ)⁻¹`.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Box` has no diagnostics)
- decl `Roth.weight_mul_left`: resolved at Roth/Box.lean:110
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.weight_mul_left` is a theorem stating the following: for a finite variable set `σ`, parameters `r ∈ ℕ^σ`, a multi-index `d ∈ ℕ^σ` and `l ∈ ℕ`, the weight with respect to the scaled parameters `l r` is `1/l` times the weight with respect to `r`: `∑_j d_j / (l r_j) = (1/l) ∑_j d_j / r_j`. Re-aimed: the weighted degree `⟨w, d⟩ = ∑ d_i w_i` is linear in the weight vector, `⟨c w, d⟩ = c ⟨w, d⟩`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]` — finite variable set.
- `l : ℕ` — the scaling factor (implicit).
- `r : σ → ℕ` — parameters `r_j` (with `x / 0 = 0`).
- `d : σ →₀ ℕ` — the multi-index.

Hypotheses (Lean side):
- none (no `0 < l` needed: `l = 0` gives `0 = 0`).

Conclusion (math): `w_{l r}(d) = w_r(d) / l`.

Conclusion (Lean): `Roth.weight (fun j ↦ l * r j) d = Roth.weight r d / ↑l`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an elementary scaling identity for a finite sum; helper for `index_mul_left_weights`, not listed as a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma index ind(P; α; l r) = (1/l) ind(P; α; r) scaling parameters | partial | index = min of `∑ i_h / r_h`; scaling identity not stated in hits | arXiv 1806.10737, 2111.12409, Evertse notes; identity immediate from the definition |
| 2 | WebSearch (general form) | weighted degree linear in weight vector scaling weights by constant scales weighted degree | partial | weighted sum scales linearly with a common weight factor | network-science analogue (arXiv 2510.23964); immediate from linearity of sums |
| 3 | WebSearch (named-after / aliases) | index of polynomial homogeneous in weights r_1..r_m Schmidt Diophantine approximation "index" properties multiplication of weights | yes | index with weights `t r` equals index with weights `r` divided by `t` | arXiv 2502.00731 (Evertse, Def. 2.20 and basic properties), arXiv 2005.06531 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `1/l`, `frac1l` | yes | l.636–640: `ind(P;α;lr) = (1/l) ind(P;α;r)` for `l > 0`; l.630–634 Lean note asks for "scaling of the index weights" as a separate lemma | project paper §4 |
| 6 | nLab | weighted degree / graded ring | partial | grading of polynomial rings by weights | rescaling a grading is folklore; no lemma-level entry |
| 7 | nCatLab | — | n/a | — | not a categorical concept (finite-sum identity) |
| 8 | Stacks Project | weighted polynomial rings / graded rings | n/a | — | checked graded-ring sections; integer weights only, no rescaling statement |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | no | — | immediate fact; no discussion found |
| 10 | recent arXiv (last 5 years) | (arXiv 2502.00731, 2005.06531 from #3) | yes | scaling property of the index listed among basic properties | same identity |

### Literature summary (Phase 3)

Concept identified as: homogeneity (degree −1) of the Roth index weight in the parameter vector; equivalently linearity of the weighted degree `⟨w, d⟩` in the weight vector `w`.
Sources agree on the standard form: yes (always listed as an immediate basic property).
Most general standard form: `⟨c • w, d⟩ = c • ⟨w, d⟩` for a scalar `c` acting on the weight module.
Generality dimensions where the literature varies:
  - scaling: positive integer `t` (Roth/Evertse) vs arbitrary scalar (linear algebra).
  - weights: `1/r_j` vs arbitrary.
Disagreement with the literature: none (the paper requires `l > 0`; Lean's form needs no hypothesis).

### Generality analysis — `Roth.weight_mul_left`

Literature-standard form (from Phase 3): `Finsupp.weight (c • w) f = c • Finsupp.weight w f`, `M` an `R`-module with a commuting `S`-action.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | weight vector / codomain | `1/r j` in ℝ | any `w : σ → M` | yes (re-aimed) | evidence `finsupp_weight_smul` compiles |
| 2 | scalar | `(l : ℝ)⁻¹` from `l : ℕ` | any `c : S`, `[DistribMulAction S M] [SMulCommClass R S M]` | yes (re-aimed) | evidence `finsupp_weight_smul` |
| 3 | `l > 0` (paper) | absent | — | already dropped | evidence (4): `l = 0` instance holds |
| 4 | `[Fintype σ]` | required for `Roth.weight` | not needed (re-aimed) | yes (re-aimed) | `finsupp_weight_smul` is stated with `omit [Fintype σ]` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the general re-aimed form is a one-`simp` composition of mathlib lemmas (`Finsupp.weight_apply`, `Finsupp.smul_sum`, `smul_comm`), verified in the evidence file; routed to NO-composable-from-mathlib, not generalise-first.
Number of weakening opportunities found: 3 (rows 1, 2, 4), verified for the re-aimed statement.
Proposed restatement (re-aimed, optional): `theorem Finsupp.weight_smul (c : S) (w : σ → M) (f : σ →₀ R) : weight (c • w) f = c • weight w f := by simp [weight_apply, Finsupp.smul_sum, smul_comm]`.
Cost of restatement: CHEAP (verified).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | finite sum identity |
| 3 | construction vs universal property? | marginal | linearity of `w ↦ Finsupp.weight w` as a linear map `(σ → M) →ₗ ((σ →₀ R) →+ M)` | none used anywhere |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | yes (re-aimed) | scalar action on a module | as row 2 of 4a |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (re-aimed) | `ℕ`-parameters to arbitrary weight vector | — |
| 8 | concrete-via-abstract? | no | proof body only unfolds and uses `Finset.sum_div`; nothing beyond row 1–2 | — |
| 9 | false-generalisation guard | no false generalisation | evidence (2) recovers the project lemma from the re-aimed form | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the only modernisation is "state against `Finsupp.weight`", which the parent refactor covers; the re-aimed statement is a one-`simp` consequence of `Finsupp.smul_sum`, not new organisation.

### Proof strategy — `Roth.weight_mul_left`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | `Finset.sum_div`, `div_div` suffice | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.weight_mul_left`

[A] Lean-Finder       "linearCombination is linear in the family of vectors: linearCombination R (c • v) f = c • linearCombination R v f"   hits: `Fintype.linearCombination`, `Finsupp.linearCombination_linear_comp`, `Finsupp.linearCombination_smul` (scalar-tower currying, not linearity in `v`) — no direct lemma
[B] Loogle            `Finsupp.weight (_ • _)`   no hits
[C] LeanSearch        "Finsupp.weight of scalar multiple of weight vector equals scalar times weight"   hits: `Finsupp.weight_single`, `Finsupp.smul_single`, `Finset.weightedVSub_const_smul` (analogue for affine combinations) — no `Finsupp.weight` lemma
[D] Grep mathlib src  `weight_smul`, `smul_weight`, `linearCombination_smul`, `weightedOrder_smul`, `weightedTotalDegree.*smul` over `.lake/packages/mathlib/Mathlib`   only `MvPowerSeries.le_weightedOrder_smul` (scalar on the series, unrelated) and `Finsupp.linearCombination_smul` (currying); theorem list of Mathlib/Data/Finsupp/Weight.lean has no scaling lemma
[E] Name pattern      `Finsupp.weight_smul`, `Finsupp.linearCombination_smul_left`   absent (grep of Weight.lean and LinearCombination.lean)

Searched for both the user's form (`∑ d j / (l r j) = (∑ d j / r j) / l`) and the re-aimed literature-standard form (`weight (c • w) f = c • weight w f`).

Concluded: found building blocks (`Finsupp.weight_apply`, `Finsupp.smul_sum`, `smul_comm`; for the project form `Finset.sum_div`, `div_div`); composition would yield our form.

### Normal-form check — `Roth.weight_mul_left`

Equivalent formalisms: `weight (l * r) d = weight r d / l`; `= (l)⁻¹ * weight r d`; `= (l : ℝ)⁻¹ • weight r d`; `Finsupp.weight ((l)⁻¹ • w) = (l)⁻¹ • Finsupp.weight w`.
Does mathlib already have a canonical form for this idea? No lemma; canonical object is `Finsupp.weight`.
Is our statement stated against the canonical form? Against the project def `Roth.weight` (parent refactor target); the `/ l` RHS matches the paper and the caller (which immediately rewrites `div_eq_inv_mul`).
RHS convention respected? yes (simpler expression `weight r d / l` on the RHS).

### Syntactic generality — `Roth.weight_mul_left`

Alternative restatements attempted:
- RHS `(l : ℝ)⁻¹ * weight r d` (would save the caller's `div_eq_inv_mul`)
- re-aimed `Finsupp.weight (c • w) f = c • Finsupp.weight w f` (compiles; evidence)
Chosen restatement: as stated.
Justification: matches the paper's `(1/l) ind` and the sibling `index_mul_left_weights` statement; the caller's extra rewrite is trivial.

### Superfluous-argument audit — `Roth.weight_mul_left`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed by `Roth.weight` |
| 2 | `l`, `r`, `d` | yes | — |
| 3 | `0 < l` | not present | correctly omitted (evidence (4)) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally)

### Call sites — `Roth.weight_mul_left`

Internal use count: 1 (outside Roth/Box.lean)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:206 | `rw [weight_mul_left, smul_eq_mul, div_eq_inv_mul]` (inside `index_mul_left_weights`, proving the image identity `weight (fun j ↦ l * r j) '' S = (l : ℝ)⁻¹ • (weight r '' S)`) |

Inline-derivation grep:
  - (none) — `grep -rn "Finset.sum_div" Roth/` shows no other re-derivation of the weight scaling.

### Composition check (Phase 6)

Can `Roth.weight_mul_left` be derived from mathlib in ≤3 chained calls?

Attempt 1 (project form): `simp only [Roth.weight, Finset.sum_div, div_div, Nat.cast_mul, mul_comm]`
  - Mathlib decls used: `Finset.sum_div`, `div_div`, `Nat.cast_mul`, `mul_comm`
  - Result: succeeds (evidence example (3)); trivial simp composition

Attempt 2 (re-aimed form): `simp [Finsupp.weight_apply, Finsupp.smul_sum, smul_comm]`
  - Mathlib decls used: `Finsupp.weight_apply`, `Finsupp.smul_sum`, `smul_comm`
  - Result: succeeds (evidence `finsupp_weight_smul`); the project lemma follows from it via the parent bridge (evidence example (2))

Conclusion: COMPOSABLE

## Verdict: `Roth.weight_mul_left`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the scaling `ind(P; α; l r) = (1/l) ind(P; α; r)` is a basic property listed without proof (clean.tex l.639, arXiv 2502.00731); it is linearity of the weighted degree in the weights.
- Generality analysis (Phase 4): STRICTLY NARROWER, but the general re-aimed form is a one-`simp` composition (verified).
- Mathlib search (Phase 5): no `Finsupp.weight` scaling lemma; building blocks `Finsupp.smul_sum`, `smul_comm`, `Finset.sum_div`, `div_div`.
- Composition check (Phase 6): COMPOSABLE (both forms, one `simp` each).

**Rationale:**

Re-aimed at `Finsupp.weight` (parent `Roth.weight` is `NO-mathlib-has-it`), the analogue `Finsupp.weight (c • w) f = c • Finsupp.weight w f` is absent from mathlib, but it closes by `simp [weight_apply, Finsupp.smul_sum, smul_comm]`: it is distributivity of a scalar over a finite sum, not new API. The project form is likewise `Finset.sum_div` plus `div_div` after unfolding.

WHY not: the content is "a common factor `1/l` comes out of a finite sum", which mathlib has as `Finset.sum_div` / `Finsupp.smul_sum`. A `Finsupp.weight_smul` lemma would be a harmless simp-lemma but has no consumer in mathlib and does not meet the bar on its own. Belongs-elsewhere check: keep project-local in Roth/Box.lean; the paper's Lean note (clean.tex l.630–634) asks for the index-weight scaling as a separate lemma, and its single caller reads better with the name.

Mathlib building blocks:      `Finset.sum_div` (Mathlib/Algebra/BigOperators/Field.lean), `div_div` (Mathlib/Algebra/Group/Basic.lean), `Finsupp.smul_sum` (Mathlib/Algebra/BigOperators/Finsupp/Basic.lean), `Finsupp.weight_apply` (Mathlib/Data/Finsupp/Weight.lean:85)
Composition sketch (≤3 lines):
```lean
example {l : ℕ} (r : σ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight (fun j ↦ l * r j) d = Roth.weight r d / l := by
  simp only [Roth.weight, Finset.sum_div, div_div, Nat.cast_mul, mul_comm]
```
Call sites in our project (from Phase 6.0):  1 (Roth/Index.lean:206)
Refactor plan: no inlining recommended (Step 8 KEEP): at Index.lean:206 the lemma is used inside `Set.image_congr`; inlining would require unfolding `weight` there. If `Roth.weight` is redefined via `Finsupp.weight` (parent report), reprove as in evidence (2) (`finsupp_weight_smul` after the bridge), or keep the current proof via the `weight_eq_sum` bridge; the caller is unchanged.
Next action: keep `Roth.weight_mul_left` locally; no mathlib PR.

---

## Next step

No mathlib action. Keep the lemma in Roth/Box.lean; reprove via the `weight_eq_sum` bridge only if the parent `Roth.weight` refactor is carried out.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.weight_mul_left/weight_mul_left_reaim.lean` (imports `Roth.Box`; `lean_diagnostic_messages`: no diagnostics after fixing one `ext; simp` step and adding `omit [Fintype σ]`): (1) `finsupp_weight_smul` — re-aimed general form `Finsupp.weight (c • w) f = c • Finsupp.weight w f`; (2) project lemma from (1) via the parent's bridge to `Finsupp.weight`; (3) project lemma by `simp only [Roth.weight, Finset.sum_div, div_div, Nat.cast_mul, mul_comm]`; (4) the `l = 0` instance holds, so no positivity hypothesis is needed.
- Loogle `Finsupp.weight (_ • _)` (no hits); LeanSearch and Lean-Finder queries as in the search-status block; mathlib greps for `weight_smul`, `smul_weight`, `linearCombination_smul`, `weightedOrder_smul`.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex (l.630–640).
- Project grep `grep -rn weight_mul_left Roth/` for the call-sites table.
