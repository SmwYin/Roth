---
decl: Roth.index_mul_left_weights
file: Roth/Index.lean
line: 200
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: ind(P; α; l r) = ind(P; α; r)/l about the project-only def Roth.index is a short composition of Set.image_smul, Set.image_congr with the project weight_mul_left and Real.sInf_smul_of_nonneg (verified), needs no 0 < l (l = 0 compiled), and its ℕ∞ power-series analogue (weightedOrder homogeneous in the weight) is a short proof from weightedOrder_le and le_weightedOrder, so nothing goes upstream.
action: Keep in Roth/Index.lean as the source's requested weight-scaling lemma for its single call site Roth/Theta.lean:447 (lem6 bound); no mathlib PR. Optional unrelated tiny PR is MvPowerSeries.weightedOrder_nsmul_weight in Mathlib/RingTheory/MvPowerSeries/Order.lean.
---

# Roth.index_mul_left_weights

## Inventory entry

### `theorem Roth.index_mul_left_weights`
- **Type**: `{σ : Type*} [Fintype σ] {l : ℕ} (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : Roth.index P α (fun j ↦ l * r j) = Roth.index P α r / l`
- **What**: Scaling all index weights `r j` by the same natural number `l` divides the index by `l`.
- **How**: Proves the image identity `weight (l r) '' supp = (l : ℝ)⁻¹ • (weight r '' supp)` with `Set.image_smul`, `Set.image_image`, `Set.image_congr` and the project's `Roth.weight_mul_left`, then unfolds `index` and pulls the scalar out of the infimum with `Real.sInf_smul_of_nonneg` (`(l:ℝ)⁻¹ ≥ 0` by `positivity`).
- **Hypotheses**: none. In particular no `0 < l` and no `P ≠ 0` (with `l = 0` both sides are `0`; evidence (2)).
- **Uses from project**: `Roth.index`, `Roth.weight`, `Roth.weight_mul_left` (Roth/Box.lean:110), `MvPolynomial.taylor` (Roth/Taylor.lean)
- **Used by**: Roth/Theta.lean:447 (`rw [index_mul_left_weights] at hUΘ hVΘ`, in the Lemma 6 product bound). No other use (`grep -rn index_mul_left_weights Roth/`).
- **Visibility**: public
- **Lines**: 199-207 (docstring 199, statement 200-201, proof 202-207), proof length 6 lines
- **Notes**: Formalises clean.tex:636-640, `ind(P;α;lr) = (1/l) ind(P;α;r)` stated for `l > 0`; the Lean form drops `l > 0`. The Lean note at clean.tex:627-634 asks for "scaling of the index weights" as a separate lemma.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Theta.lean:447.
- Wrapper of 1-2 mathlib calls? Nearly: `Real.sInf_smul_of_nonneg` plus image bookkeeping and the project `weight_mul_left`.
- Does mathlib have it? Not for the project-only `Roth.index`. No mathlib lemma on scaling the weights of `MvPowerSeries.weightedOrder` or `Finsupp.weight` either (grep / loogle below).
- Too specific (inline)? Inlining at Theta.lean:447 would require unfolding `index` twice inside a long proof and repeating the 6-line image argument. The source explicitly asks for this as a separate lemma. Keep.
- Well-chosen? Yes; hypothesis-free and in the `fun j ↦ l * r j` shape that the caller produces.
- Conclusion: `KEEP` — keep in Roth/Index.lean unchanged.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; `Roth.index_mul_left_weights` not in mathlib (no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`). Proof is a tactic composition, not `rfl`, so not a glue lemma: full run. Parent `Roth.index` is BORDERLINE-needs-human (not NO-mathlib-has-it), so no re-aim; the related `Roth.weight_mul_left` is NO-composable-from-mathlib.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Index` has no diagnostics)
- decl `Roth.index_mul_left_weights`: resolved at Roth/Index.lean:200
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the Roth index of a real multivariate polynomial at a point and its basic properties (§4 of the source)

### Statement (Phase 1)

`Roth.index_mul_left_weights` is a theorem stating the following: for `P ∈ ℝ[X_j : j ∈ σ]`, `α ∈ ℝ^σ`, `r ∈ ℕ^σ` and `l ∈ ℕ`, with `ind(P; α; r) = min { ∑_j d_j / r_j : coefficient of X^d in P(X + α) nonzero }`, one has `ind(P; α; l r) = ind(P; α; r) / l`.

Variables / typeclasses involved (Lean side):
- `σ`, `[Fintype σ]`: the variables.
- `l : ℕ` (implicit): the common scaling factor.
- `P`: the polynomial. `α`: the point. `r`: the weights.

Hypotheses (Lean side):
- none (source has `l > 0`; Lean's `x / 0 = 0` makes `l = 0` true as `0 = 0`).

Conclusion (math): the index is homogeneous of degree `-1` in the weight vector `r`.

Conclusion (Lean): `index P α (fun j ↦ l * r j) = index P α r / l`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-line scaling remark at the end of source §4 about a project definition; not a main result, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 6 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem index of polynomial ind(P; α; l r) = (1/l) ind(P; α; r) scaling weights | partial | index = min of ∑ i_h/r_h over nonzero derivatives (arXiv math/9708214, 1305.0926, M. Ru's Roth notes math.uh.edu/~minru/fields/roth.pdf) | no source states the scaling as a lemma; it is immediate from the definition |
| 2 | WebSearch (general form) | weighted order monomial valuation scaling weight vector homogeneity ord_{λw}(f) = λ ord_w(f) | partial | monomial weight = dot product of exponent and weight vector (Singular/Macaulay2 manuals, arXiv 1608.03725); min over support scales by λ > 0 | positive homogeneity of the monomial valuation in its weight vector; nowhere stated as a named result |
| 3 | WebSearch (aliases: Newton polyhedron support function) | Newton polyhedron support function homogeneous of degree one weighted degree min over support scaling | partial | support function h_P(u) = max over P of u·v is positively homogeneous (Newton polytope surveys, arXiv 2106.06869, 0706.1004) | the index is the (min-convention) support function of the Newton polyhedron of P(X+α) evaluated at u = (1/r_j); positive homogeneity is the general form |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep clean.tex for `ind(P;\alpha;lr)` | yes | clean.tex:636-640 states `ind(P;α;lr) = (1/l) ind(P;α;r)` for `l > 0`; Lean note clean.tex:627-634 asks for "scaling of the index weights" as a separate lemma | Lean statement matches and drops `l > 0` |
| 6 | nLab | valuation / support function | no | abstract valuations only | no weight-vector scaling content |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | not an algebraic-geometry concept beyond orders of vanishing (tag 02MB), which carry no weight vector |
| 9 | MathOverflow / Math.SE | covered by searches 2-3 | no | n/a | considered immediate; no dedicated thread |
| 10 | recent arXiv | Roth index / subspace theorem (2111.12409, 2502.00731) | partial | index used with weights scaled implicitly | no standalone statement |

### Literature summary (Phase 3)

Concept identified as: positive homogeneity of the weighted order (monomial valuation / Newton-polyhedron support function) in its weight vector.
Sources agree on the standard form: yes — `ord_{λw}(f) = λ ord_w(f)` for `λ ≥ 0` (with `f ≠ 0`, or under `0·∞ = 0` conventions).
Most general standard form: for any weight vector `w ∈ ℝ_{≥0}^σ` and `λ ≥ 0`, `min_{d ∈ supp f} ⟨λw, d⟩ = λ min_{d ∈ supp f} ⟨w, d⟩`.
Generality dimensions where the literature varies:
  - scale: `λ > 0` (source) vs `λ ≥ 0`; the Lean form covers all `l ∈ ℕ` including `0`.
  - weights: real `1/r_j` (project) vs natural (mathlib `weightedOrder`).
  - zero polynomial: `+∞` (literature) vs `0` (project); irrelevant here, both sides vanish.
Disagreement with the literature: none.

### Generality analysis — `Roth.index_mul_left_weights`

Literature-standard form: `ind(P; α; l r) = ind(P; α; r)/l`, i.e. positive homogeneity in the weight.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `l : ℕ` | any natural, no positivity | `l > 0` | already weaker than source | evidence (2): `l = 0` instance compiles |
| 2 | `l` natural vs real scale | ℕ | positive real `λ` | not for this def | `Roth.index` takes `r : σ → ℕ`, so a real scale is not expressible without redesigning the parent def |
| 3 | `P` | arbitrary | arbitrary / nonzero | already general | no `P ≠ 0` needed |
| 4 | `r` | arbitrary, no positivity | positive | already general | junk `r j = 0` handled by `x/0 = 0` in `weight_mul_left` |
| 5 | `fun j ↦ l * r j` vs `l • r` | lambda | either | equivalent | evidence (3): `l • r` form closes by the same term (defeq) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (for the project definition; it is already hypothesis-free and weaker than the source).
Number of weakening opportunities found: 0
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | no hypotheses | — |
| 2 | Sequences vs filters? | no | finite algebraic identity | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no for this lemma | depends on redesigning `Roth.index` (ℝ-only) | parent-def question (BORDERLINE) |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | partial | `index P α (l • r) = index P α r / l` with the scale in any ordered semifield would need real weights in the parent def | parent-def redesign |
| 8 | Concrete-via-abstract? | yes (diagnostic fires) | after `rw [index, index]` the proof never mentions `index`; it is "sInf of a positively scaled image" (`Real.sInf_smul_of_nonneg`) plus `weight_mul_left`. The abstract statement is already mathlib's `Real.sInf_smul_of_nonneg`; the ℕ∞ weighted-order analogue `weightedOrder (l • w) f = l * weightedOrder w f` is missing but short (evidence (4)) | nothing substantive to add |
| 9 | False-generalisation guard | no false generalisation | the `l • r` form is the same statement | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (for this lemma)
  - Reason: the abstract content is `Real.sInf_smul_of_nonneg`; anything further is a redesign of the parent `Roth.index`, assessed separately as BORDERLINE.

### Proof strategy — `Roth.index_mul_left_weights`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no (for this proof) | side observation: mathlib lacks homogeneity of `MvPowerSeries.weightedOrder` in the weight; a route via `index_eq_weightedOrder_div` would need it plus `0 < r j`, whereas the current sInf route needs neither | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. Pointwise-image plus `Real.sInf_smul_of_nonneg` is the direct route and avoids the positivity hypotheses of the weighted-order bridge.
  - Missing mathlib API: none for this lemma.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.index_mul_left_weights`

[A] Lean-Finder       "weighted order of multivariate power series with weights scaled by a constant equals constant times weighted order"   hits: `le_weightedOrder_smul`, `le_weightedOrder_pow`, `le_order_smul`, `weightedOrder`, `weightedOrder_monomial` — none scales the weight
[B] Loogle            `MvPowerSeries.weightedOrder, HMul.hMul`   hits: `le_weightedOrder_mul`, `weightedOrder_mul`, `weightedHomogeneousComponent_mul_of_le_weightedOrder`, `coeff_mul_*_of_lt_weightedOrder`, `PowerSeries.le_weightedOrder_subst` — all multiply series, not weights
[C] LeanSearch        "infimum of image under scalar multiple equals scalar times infimum of image, real numbers"   hits: `Real.sInf_smul_of_nonneg` (Mathlib/Data/Real/Pointwise.lean, the building block used), `Real.iInf_mul_of_nonneg`, `Real.smul_iInf_of_nonneg`, `NNReal.mul_iInf`
[D] Grep mathlib src  `weightedOrder (. • `, `weightedOrder (fun .* \* `, `weight (. • `, `weight_smul`, `weight_nsmul`: no hits. `Real.sInf_smul_of_nonneg` at Mathlib/Basic/Real/Pointwise.lean:41 (used in Gauge.lean)
[E] Name pattern      `Roth.index_mul_left_weights`: no `namespace Roth` in mathlib; `lean_local_search` not used (grep instead)

Searched for both:
  - the user's current form (Roth index under weight scaling)
  - the literature-standard form (weighted order positively homogeneous in the weight)

Concluded: found building blocks (`Real.sInf_smul_of_nonneg`, `Set.image_smul`, `Set.image_image`, `Set.image_congr`, plus project `Roth.weight_mul_left`); composition gives our form.

### Normal-form check — `Roth.index_mul_left_weights`

Equivalent formalisms:
- `index P α (fun j ↦ l * r j) = index P α r / l` (current)
- `index P α (l • r) = index P α r / l` (evidence (3))
- `index P α (fun j ↦ l * r j) = (l : ℝ)⁻¹ * index P α r`
- `l * index P α (fun j ↦ l * r j) = index P α r` (needs `l ≠ 0`)

Does mathlib already have a canonical form? n/a (project definition). The current form follows the source and the `_mul_left` naming of `weight_mul_left`.
Is our statement against a canonical form? Yes: scaled weights on the LHS, simpler term on the RHS.
RHS convention respected? yes

### Syntactic generality — `Roth.index_mul_left_weights`

Alternative restatements attempted:
- lambda `fun j ↦ l * r j` (current)
- `l • r` (evidence (3), defeq, same proof term)
- inverse-multiplication RHS

Chosen restatement: current.
Justification: the caller (Theta.lean:447) rewrites hypotheses whose weights are literally `fun j ↦ l * r j`, then uses `div_le_iff₀'`, which matches the `/ l` RHS directly; and it is the only form valid without `l ≠ 0`.

### Superfluous-argument audit — `Roth.index_mul_left_weights`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed by `Roth.weight` / `Roth.index` |
| 2 | `l` implicit | yes | inferred from the LHS at the `rw` call site |
| 3 | `P`, `α`, `r` | yes | unconstrained data |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; not a mathlib candidate)

### Call sites — `Roth.index_mul_left_weights`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:447 | `rw [index_mul_left_weights] at hUΘ hVΘ` |

Inline-derivation grep:
  - (none) — no other site uses `Real.sInf_smul_of_nonneg` or re-derives weight scaling under `index`.

### Composition check (Phase 6)

Can `Roth.index_mul_left_weights` be derived from mathlib in ≤3 chained calls?

Attempt 1: image identity via `Set.image_smul` + `Set.image_image` + `Set.image_congr` (with project `weight_mul_left`), then `Real.sInf_smul_of_nonneg`.
  - Mathlib decls used: `Set.image_smul`, `Set.image_image`, `Set.image_congr`, `Real.sInf_smul_of_nonneg` (Mathlib/Basic/Real/Pointwise.lean:41), `smul_eq_mul`, `div_eq_inv_mul`.
  - Result: succeeds (evidence (1)).
  - Notes: two rewrite chains plus a `have`; the only non-mathlib step is the project's `weight_mul_left`, itself a one-`simp` composition (Roth.weight_mul_left.md).

Conclusion: COMPOSABLE

## Verdict: `Roth.index_mul_left_weights`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): clean.tex:636-640 states it (for `l > 0`); in the literature it is the immediate positive homogeneity of a weighted order / support function in the weight vector.
- Generality analysis (Phase 4): MAXIMALLY GENERAL; already hypothesis-free, weaker than the source (`l = 0` compiled).
- Mathlib search (Phase 5): building blocks `Real.sInf_smul_of_nonneg` and pointwise-image lemmas; no weight-scaling lemma for `MvPowerSeries.weightedOrder` or `Finsupp.weight`.
- Composition check (Phase 6): COMPOSABLE.

**Rationale:**

After unfolding `Roth.index`, the lemma is "the infimum of a set scaled by `1/l ≥ 0` is `1/l` times the infimum" (`Real.sInf_smul_of_nonneg`), applied to the image identity supplied by the project's `weight_mul_left`. Q8 fires: the proof never mentions `index` after unfolding, and its abstract content is already in mathlib. The subject `Roth.index` is a project-specific real normalisation of a weighted order at a point (its own report is BORDERLINE), so this lemma has no direct mathlib home. The natural upstream analogue, `MvPowerSeries.weightedOrder (l • w) f = l * weightedOrder w f` for `l ≠ 0`, is missing from mathlib but is a ~10-line proof from `weightedOrder_le`, `le_weightedOrder` and `exists_coeff_ne_zero_and_weightedOrder` (evidence (4)); it is a possible tiny independent addition, not this declaration.

WHY not: the lemma is a short composition of mathlib's `Real.sInf_smul_of_nonneg` with pointwise-image bookkeeping, about a project definition; it adds no mathematics mathlib lacks.
Belongs-elsewhere check: keep project-local in Roth/Index.lean — it is the source's explicitly requested "scaling of the index weights" lemma (clean.tex:627-640) and saves the Lemma 6 proof from unfolding `index`.
Mathlib building blocks: `Real.sInf_smul_of_nonneg` (Mathlib/Basic/Real/Pointwise.lean:41), `Set.image_smul`, `Set.image_image`, `Set.image_congr`; project `Roth.weight_mul_left` (Roth/Box.lean:110).
Composition sketch (≤3 lines):
```lean
  have himg : weight (fun j ↦ l * r j) '' S = (l : ℝ)⁻¹ • (weight r '' S) := by
    rw [← Set.image_smul, Set.image_image]; exact Set.image_congr fun d _ ↦ by rw [weight_mul_left, smul_eq_mul, div_eq_inv_mul]
  rw [index, index, himg, Real.sInf_smul_of_nonneg (by positivity), smul_eq_mul, div_eq_inv_mul]
```
Call sites in our project (from Phase 6.0): 1 (Roth/Theta.lean:447).
Refactor plan: do not delete or inline. Inlining at Theta.lean:447 would put the image computation above into the Lemma 6 proof for two hypotheses (`hUΘ`, `hVΘ`) and lose the named source identity; the verdict is "not for mathlib", not "inline".
Next action: keep locally; do not upstream.

## Next step

Keep `Roth.index_mul_left_weights` in Roth/Index.lean unchanged; do not upstream. Optionally, as an independent tiny mathlib PR, add homogeneity of `MvPowerSeries.weightedOrder` in the weight (`weightedOrder (l • w) f = l * weightedOrder w f` for `l ≠ 0`, proof in evidence (4)) to Mathlib/RingTheory/MvPowerSeries/Order.lean.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_mul_left_weights/scaling.lean` (imports `Roth.Index`); `lean_diagnostic_messages` reports no diagnostics after fixing a missing `open scoped Pointwise` and a renamed lemma (`mul_le_mul_left'` replaced by `mul_le_mul'`). Contents:
  - (1) current proof reproduced as a composition.
  - (2) the `l = 0` instance: `index P α (fun j ↦ 0 * r j) = 0`, confirming `l > 0` is not needed.
  - (3) the `l • r` spelling closes by the same term.
  - (4) `MvPowerSeries.weightedOrder (l • w) f = l * weightedOrder w f` for `l ≠ 0` over any semiring (not in mathlib; short proof).
- WebSearch ×3 (queries in the table).
- Local grep of `.mathlib-quality/references/clean.tex` (lines 627-640).
- Lean-Finder, Loogle, LeanSearch, grep of `.lake/packages/mathlib/Mathlib/` as in Phase 5.
- `grep -rn index_mul_left_weights Roth/`: the declaration plus Theta.lean:447.
- ChatGPT channel n/a: `ask_chatgpt_math` MCP not configured in this session.
