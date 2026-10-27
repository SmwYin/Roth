---
decl: Roth.le_index_iff
file: Roth/Index.lean
line: 85
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: The greatest-lower-bound characterisation of the sInf-defined index (c at most index iff c at most every weight of a d with nonvanishing Hasse derivative) is le_csInf_iff on a finite nonempty image plus Set.forall_mem_image and the project coeff_taylor (compiled); its canonical counterpart is the pair MvPowerSeries.le_weightedOrder and weightedOrder_le (compiled), so nothing new for mathlib; hP is necessary (compiled).
action: Keep locally as the lower-bound API lemma of Roth.index (used at Roth/Index.lean:121, 125, 154, 248 and Roth/MainLemma.lean:423); do not upstream; if index is ever rebased on weightedOrder of taylor (parent question 3), reprove via MvPowerSeries.le_weightedOrder and weightedOrder_le.
---

# Roth.le_index_iff

## Inventory entry

### `theorem Roth.le_index_iff`
- **Type**: `{P : MvPolynomial σ ℝ} (hP : P ≠ 0) {α : σ → ℝ} {r : σ → ℕ} {c : ℝ} : c ≤ index P α r ↔ ∀ d, eval α (hasseDeriv d P) ≠ 0 → c ≤ weight r d` (with `[Fintype σ]`)
- **What**: For a nonzero polynomial, a real `c` is at most the index of `P` at `α` with weights `r` iff every multi-index `d` with `(Δ_d P)(α) ≠ 0` has weight `∑ d_j / r_j ≥ c`.
- **How**: forward direction is `h.trans (index_le_weight hd)`; backward direction is `le_csInf` with nonemptiness from `simpa using hP`, then `rintro` over the image and the private `mem_support_taylor_iff` (`mem_support_iff` + `coeff_taylor`).
- **Hypotheses**: `hP : P ≠ 0` (nonempty support of `P(X+α)`; necessary, evidence (3)).
- **Uses from project**: `Roth.index`, `Roth.weight`, `Roth.index_le_weight`, `Roth.mem_support_taylor_iff` (private), `MvPolynomial.taylor`, `MvPolynomial.hasseDeriv`, and the simp lemma(s) giving `taylor α P = 0 ↔ P = 0` used by `simpa using hP`
- **Used by**: Roth/Index.lean:121 and :125 (`le_index_sum`), :154 (`index_eq_weightedOrder_div`), :248 (`index_unique`); Roth/MainLemma.lean:423 (`le_index_of_forall_eval_eq_zero`)
- **Visibility**: public
- **Lines**: 83–90, proof length 4 lines
- **Notes**: listed as a main result in the module docstring. No positivity of `r` needed. Third sibling of `index_le_weight` and `exists_weight_eq_index` in the "index = attained minimum" API.

## Junk check (Step 8)
- Used anywhere? Yes, 5 sites in 2 files (4 in Index.lean, 1 in MainLemma.lean).
- Wrapper of 1–2 mathlib calls? Essentially `le_csInf_iff` + `Set.forall_mem_image` plus the support translation, but it is the characterising lower-bound API lemma of the project def `Roth.index` and hides the `sInf`/image/support unfolding.
- Does mathlib have it? Not for `Roth.index`. For mathlib's weighted order there is only the one-directional `MvPowerSeries.le_weightedOrder` (plus `weightedOrder_le` for the converse), with no packaged iff.
- Too specific (inline?)? No: inlining would expose the `sInf` definition at 5 sites in 2 files.
- Well-chosen? Yes; it is the form every consumer needs (lower bounds for the index, as in Lemma 4-1 and Lemma 9 of the source).
- Conclusion: `KEEP`. Action: none locally.

## Mathlibable assessment (Step 9)

Pre-filter: public, name not `_aux`, docstring not internal or auxiliary, Step 8 KEEP. `Roth.le_index_iff` is not in mathlib: no `namespace Roth` under `Mathlib/`, and the grep for `le_index_iff` finds no hit. It is not a glue lemma (the proof uses `le_csInf` and `index_le_weight`, not `rfl`), so this is a full run. The parent `Roth.index` is BORDERLINE-needs-human, not NO-mathlib-has-it, so the re-aim rule does not apply. The canonical analogue is still checked (Phase 4c row 7, Phase 6 attempt 2).

### Baseline (Phase 0)
- lake build:               ✓ clean (per brief; evidence file importing `Roth.Index` compiles)
- decl `Roth.le_index_iff`:  ✓ resolved at Roth/Index.lean:85
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index of a real multivariate polynomial at a point relative to positive integer weights (Roth §4)

### Statement (Phase 1)

`Roth.le_index_iff` is a theorem stating the following. Let `P ∈ ℝ[x_j : j ∈ σ]` be nonzero, `α ∈ ℝ^σ`, `r ∈ ℕ^σ` and `c ∈ ℝ`. Then `c ≤ ind_{α,r}(P)` iff every multi-index `d` with `(Δ_d P)(α) ≠ 0` satisfies `∑_j d_j / r_j ≥ c`. Equivalently, `ind(P) ≥ c` iff all Taylor coefficients of `P(x+α)` of weighted degree `< c` vanish.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: finite set of variables (needed by `Roth.weight`)
- `P`, `α`, `r`: polynomial, point, weights
- `c`: the candidate lower bound

Hypotheses (Lean side):
- `hP : P ≠ 0`: the support of `P(X + α)` is nonempty

Conclusion (math): the index is the greatest lower bound of the weights of the support of `P(X+α)`.

Conclusion (Lean): `c ≤ index P α r ↔ ∀ d, eval α (hasseDeriv d P) ≠ 0 → c ≤ weight r d`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma of the project def `Roth.index`. It is listed under Main results, but only as the lower-bound interface, not as a theorem of the paper.

### One-line check (Phase 2b)

Body line count: 4 (tactic proof)
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---|---|---|---|---|
| 1 | WebSearch (specific form) | index of a polynomial Roth's theorem "index" at least θ iff all derivatives vanish weight sum i_j/r_j < θ | yes | index = smallest `∑ j_i/r_i` over nonzero Taylor coefficients (arXiv math/0307203, 2502.00731, 1806.10737) | the iff is never stated separately; it is immediate from "smallest value" |
| 2 | WebSearch (general form) | weighted order of vanishing of multivariate polynomial at a point lower bound iff all coefficients of weighted degree less than vanish | partial | weighted order as min over monomials (arXiv 2604.16698); order at a point via Hasse-derivative Taylor expansion (arXiv 1310.6482) | iff is definitional; mathlib's `le_weightedOrder` docstring gives the "if" half |
| 3 | WebSearch (aliases) | monomial valuation "greater than or equal" iff support lies in half-space weighted Newton polyhedron initial ideal | partial | monomial valuation / weighted degree as extremum over the support (arXiv 1607.04860); Newton polyhedron as an intersection of half-spaces | `v(f) ≥ c` iff the support lies in the half-space `⟨w,d⟩ ≥ c`; folklore |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not among available tools) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "minimum", "attained", "ind(P" | yes | clean.tex l.530–545 (index as minimum, "attained minimum"); l.592 Lemma 4-1 used in lower-bound form | the lemma is the lower-bound reading of the definition |
| 6 | nLab | order of vanishing / valuation | partial | valuation, order of vanishing | no weighted multivariate version; nothing at this granularity |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | order of vanishing | partial | `ord` along a divisor | no weighted point-order; the lower-bound iff would be definitional there too |
| 9 | MathOverflow / Math.SE | (covered by #2, #3 results) | no | — | folklore; no stand-alone statement |
| 10 | recent arXiv (last 5 years) | (#1 result 2502.00731 (2025), #2 result 2604.16698) | yes | same definitions | iff implicit |

### Literature summary (Phase 3)

Concept identified as: the greatest-lower-bound property of the minimum that defines the index. This is the same minimum as the weighted order of vanishing at a point, or a monomial valuation: `ord ≥ c` iff the support lies in the half-space `⟨w,d⟩ ≥ c`.
Sources agree on the standard form: yes. Every source defines the quantity as a minimum over a finite support, so the iff is definitional.
Most general standard form: for any (semi)ring `R`, weights `w`, `f` and `n ∈ ℕ∞`, `n ≤ ord_w(f)` iff `coeff_d f ≠ 0 → n ≤ ⟨w,d⟩`. No nonvanishing hypothesis is needed when `ord_w(0) = ∞`.
Generality dimensions where the literature varies:
  - weights: ℕ (mathlib, algebraic geometry) vs real `1/r_j` (Roth)
  - coefficients: ℝ (Roth) vs any (semi)ring
  - value at `0`: `+∞` (source, mathlib), where the iff holds for all `f`, vs the project's junk `0`, which forces `P ≠ 0`
Disagreement with the literature: none. `hP` comes only from the project's junk-value convention, which the parent report records.

### Generality analysis — `Roth.le_index_iff`

Literature-standard form: `n ≤ ord_w(f) ↔ ∀ d ∈ supp f, n ≤ ⟨w, d⟩`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `hP : P ≠ 0` | nonzero polynomial | not needed when `ord 0 = ∞` | no (for this def) | with junk `index 0 = 0` the iff fails for `P = 0`, `c = 1` (evidence (3), compiled); removing it would require changing the parent def |
| 2 | coefficients `ℝ` | fixed by `Roth.index` | any semiring | inherited | determined by the parent def |
| 3 | `[Fintype σ]` | required | not needed | inherited | only via `Roth.weight` |
| 4 | positivity of `r` | not assumed | — | already maximal | holds for all `r` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL relative to the parent definition `Roth.index`. The only hypothesis, `hP`, is verified necessary (evidence (3)). Further generality lives in the parent def (the junk value).
Number of weakening opportunities found: 0 at the lemma level.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no bundled hypotheses |
| 2 | sequences to filters? | no | — | finite algebraic minimum |
| 3 | construction vs universal property? | no | the iff is the universal property (glb) of the defining minimum | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | inherited | only via the parent def | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (re-aim) | `n ≤ (↑(taylor α P)).weightedOrder w ↔ ∀ d, eval α (Δ_d P) ≠ 0 → n ≤ weight w d` | composes from `MvPowerSeries.le_weightedOrder` + `weightedOrder_le` (evidence (2)); mathlib lacks only the packaged iff |
| 8 | concrete-via-abstract? | yes, trivially | proof uses only "glb of a finite nonempty set" | that abstract fact is mathlib's `le_csInf_iff` |
| 9 | false-generalisation guard | no false generalisation in the re-aim itself | the `weightedOrder` form is the canonical analogue but, as for the parent, not a drop-in for the real-valued `index` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no new contribution. The re-aimed statement is a two-lemma composition of existing mathlib API (`le_weightedOrder`, `weightedOrder_le`). A packaged `MvPowerSeries.le_weightedOrder_iff` would be a tiny convenience lemma, not tied to this project.

### Proof strategy — `Roth.le_index_iff`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | `le_csInf_iff` + `Set.forall_mem_image` give a 2-line proof (evidence (1)) | CHEAP (optional golf) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. A `rw [index, le_csInf_iff …, Set.forall_mem_image]; simp [...]` variant also compiles (evidence (1)); either is fine.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status

[A] Lean-Finder       "a ≤ sInf of a finite nonempty set of reals iff a is below every element"   hits: `le_csInf_iff`, `le_csInf_iff'`, `Set.Finite.lt_csInf_iff`, `Finset.lt_inf'_iff` (building blocks)
[B] Loogle            `_ ≤ MvPowerSeries.weightedOrder _ _ ↔ _`   no hits (mathlib has no packaged iff)
[C] LeanSearch        "weighted order of power series is at least n iff all coefficients of weight less than n vanish"   hits: `MvPowerSeries.le_weightedOrder`, `nat_le_weightedOrder`, `PowerSeries.le_order`, `MvPowerSeries.le_order` (one direction each)
[D] Grep mathlib src  `le_index_iff` (no hit); `iff` in Mathlib/RingTheory/MvPowerSeries/Order.lean (only `eq_top_iff`, `eq_nat_iff`, `ne_zero_iff_*`); `le_csInf_iff` (Order/ConditionallyCompleteLattice/Basic.lean); `le_weightedOrder` (Order.lean:197), `weightedOrder_le` (Order.lean:171)
[E] Name pattern      `lean_local_search` not run (grep [D] used instead, as in sibling reports)

Searched for both: the project form (lower bound for the index of a polynomial at a point) and the literature-standard form (lower bound for a weighted order of a power series).

Concluded: found building blocks (`le_csInf_iff`, `Set.forall_mem_image`, `Set.Finite.image`, `Set.Finite.bddBelow`, `MvPolynomial.mem_support_iff`). The canonical analogue is the pair `MvPowerSeries.le_weightedOrder` / `MvPowerSeries.weightedOrder_le` for the ℕ-weighted order.

### Normal-form check

Equivalent formalisms: `c ∈ lowerBounds (weight r '' (taylor α P).support)`, `∀ d ∈ (taylor α P).support, c ≤ weight r d`, and the Hasse-derivative form used here. The Hasse-derivative form matches the source and the siblings `index_le_weight` and `exists_weight_eq_index`. RHS convention respected: yes. This is an `X ≤ f ↔ pointwise` characterisation, in the shape of `le_csInf_iff` and `Finset.le_inf'_iff`.

### Syntactic generality

Alternatives: lower-bounds form; `∀ d ∈ support` form; a strict-inequality contrapositive (`∀ d, weight r d < c → eval α (Δ_d P) = 0`, the form used in MainLemma:423). Chosen: the existing form. Every call site applies `.2` with `fun d hd ↦ …` or `.1 … d hd`, which matches this shape directly.

### Superfluous-argument audit

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hP : P ≠ 0` | yes | iff false for `P = 0`, `c = 1` (evidence (3)) |
| 2 | `[Fintype σ]` | yes (via `Roth.weight`) | inherited from parent |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE
Overall: SHIP-AS-STATED (locally)

### Call sites

Internal use count: 5 (1 outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern |
|---|---|
| Roth/Index.lean:121 | `refine (le_index_iff hs).2 fun d hd ↦ ?_` (`le_index_sum`) |
| Roth/Index.lean:125 | `exact (le_index_iff hfi).1 (hf i hi hfi) d hid` (`le_index_sum`) |
| Roth/Index.lean:154 | `refine (le_index_iff hP).2 fun e he ↦ ?_` (`index_eq_weightedOrder_div`) |
| Roth/Index.lean:248 | `refine (le_index_iff hP).2 fun d hd ↦ ?_` (`index_unique`) |
| Roth/MainLemma.lean:423 | `refine (le_index_iff hP).2 fun d he ↦ le_of_not_gt …` (`le_index_of_forall_eval_eq_zero`) |

Inline-derivation grep: none found. No other site applies `le_csInf` or `le_csInf_iff` to the index set (`index_nonneg` uses `Real.sInf_nonneg`, which also covers `P = 0`).

### Composition check (Phase 6)

Can `Roth.le_index_iff` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [index, le_csInf_iff (finite image).bddBelow (nonempty), Set.forall_mem_image]; simp [mem_support_iff, coeff_taylor]`
  - Mathlib decls used: `le_csInf_iff`, `Set.Finite.bddBelow`, `Set.Finite.image`, `Finset.finite_toSet`, `Set.forall_mem_image`, `MvPolynomial.mem_support_iff`; project `MvPolynomial.coeff_taylor`
  - Result: succeeds (evidence (1), compiled)

Attempt 2 (re-aim at the canonical object): the `weightedOrder` iff from `MvPowerSeries.weightedOrder_le` (→) and `MvPowerSeries.le_weightedOrder` (←)
  - Result: succeeds (evidence (2), compiled). Two mathlib calls plus the `coeff_taylor` translation.

Conclusion: COMPOSABLE. It is one `le_csInf_iff` rewrite on a finite nonempty image, modulo the project's `coeff_taylor`. The canonical analogue is two existing mathlib lemmas.

## Verdict: `Roth.le_index_iff`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): every source defines the index / weighted order / monomial valuation as a minimum over a finite support, so the glb characterisation is definitional (clean.tex l.530–545).
- Generality analysis (Phase 4): MAXIMALLY GENERAL at the lemma level; `hP` verified necessary for this def (evidence (3)).
- Mathlib search (Phase 5): building block `le_csInf_iff`; canonical analogue `MvPowerSeries.le_weightedOrder` + `weightedOrder_le`.
- Composition check (Phase 6): COMPOSABLE (evidence (1), (2)).

**Rationale:**

The lemma is the greatest-lower-bound half of the definition of `Roth.index`. It applies `le_csInf_iff` to the finite nonempty set `weight r '' supp(P(X+α))`, then uses `Set.forall_mem_image`, and translates support membership into Hasse-derivative language with `coeff_taylor`. Mathematically nothing is new for mathlib. For mathlib's canonical weighted order the same statement follows from `le_weightedOrder` and `weightedOrder_le`, and evidence (2) shows this. The only missing piece is a packaged `le_weightedOrder_iff`, which would be a generic convenience lemma, not this project's statement. The upstream fate of `le_index_iff` is tied to the parent (`Roth.index`, BORDERLINE).

It should not be inlined, for the same reason as its siblings `index_le_weight` and `exists_weight_eq_index`. It is the characterising API lemma of a project definition, with 5 call sites in 2 files, and inlining would expose the `sInf`/image/support unfolding. Junk verdict KEEP.

Belongs-elsewhere check: keep in Roth/Index.lean as the basic API of `Roth.index`.
Mathlib building blocks: `le_csInf_iff` (Mathlib/Order/ConditionallyCompleteLattice/Basic.lean), `Set.forall_mem_image`, `Set.Finite.image`, `Set.Finite.bddBelow`, `Finset.finite_toSet`, `MvPolynomial.mem_support_iff`. Canonical analogue: `MvPowerSeries.le_weightedOrder` (Mathlib/RingTheory/MvPowerSeries/Order.lean:197) with `MvPowerSeries.weightedOrder_le` (Order.lean:171).
Composition sketch:
```lean
example (hP : P ≠ 0) : c ≤ index P α r ↔ ∀ d, eval α (hasseDeriv d P) ≠ 0 → c ≤ weight r d := by
  rw [index, le_csInf_iff ((taylor α P).support.finite_toSet.image (weight r)).bddBelow
    (by simpa using hP), Set.forall_mem_image]
  simp [mem_support_iff, coeff_taylor]
```
Call sites in our project: 5 (Roth/Index.lean:121, 125, 154, 248; Roth/MainLemma.lean:423).
Refactor plan: none. The 5 sites keep calling `le_index_iff`. Inlining is not recommended because the lemma is the def's interface. If `Roth.index` is rebased on `weightedOrder (taylor α P)` (parent question 3), reprove it via `MvPowerSeries.le_weightedOrder` and `weightedOrder_le` plus the scaling bridge `index_eq_weightedOrder_div`; the call sites stay unchanged.
Next action: no upstreaming; keep as is.

---

## Next step

No upstreaming; keep `Roth.le_index_iff` as the local lower-bound API lemma of `Roth.index`. Revisit only if the parent's question 3 (rebase on `MvPowerSeries.weightedOrder`) is answered yes. In that case reprove via `MvPowerSeries.le_weightedOrder` / `weightedOrder_le`.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.le_index_iff/compose_reaim_necessity.lean` (imports `Roth.Index`) compiled clean with `lake env lean` (no output, about 26 s). It contains three checks:
  - (1) composition via `le_csInf_iff` + `Set.forall_mem_image` + `coeff_taylor`;
  - (2) the re-aimed iff for `(↑(taylor α P)).weightedOrder w` via `MvPowerSeries.weightedOrder_le` + `MvPowerSeries.le_weightedOrder`;
  - (3) `hP` is necessary: for `P = 0`, `c = 1` the iff fails (closed by `simp [index]`).
- WebSearch ×3 (queries in the literature table).
- Loogle `_ ≤ MvPowerSeries.weightedOrder _ _ ↔ _` (no hits); LeanSearch and Lean-Finder queries as recorded.
- Greps: mathlib for `le_index_iff`, `iff` in MvPowerSeries/Order.lean, `le_csInf_iff`; project for call sites; clean.tex for "minimum", "attained", "ind(P".
- `ask_chatgpt_math` MCP not configured in this session.
