---
decl: Roth.le_index_sum
file: Roth/Index.lean
line: 118
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: The finite-sum ultrametric lower bound for the index (a common lower bound c for the nonzero summands bounds the index of a nonzero sum) is le_index_iff twice plus map_sum and Finset.exists_ne_zero_of_sum_ne_zero (compiled); its canonical counterparts are AddValuation.map_le_sum and, for weightedOrder, a two-call composition of le_weightedOrder and coeff_eq_zero_of_lt_weightedOrder (compiled), so nothing new for mathlib; hs is necessary (compiled).
action: Keep locally as the sum-form of Lemma 4-1 (single caller Roth/Theta.lean:398); do not upstream; optionally a generic MvPowerSeries.le_weightedOrder_sum could be proposed to Mathlib/RingTheory/MvPowerSeries/Order.lean as a convenience lemma, independent of this project.
---

# Roth.le_index_sum

## Inventory entry

### `theorem Roth.le_index_sum`
- **Type**: `{ι : Type*} {s : Finset ι} {f : ι → MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ} (hs : ∑ i ∈ s, f i ≠ 0) {c : ℝ} (hf : ∀ i ∈ s, f i ≠ 0 → c ≤ index (f i) α r) : c ≤ index (∑ i ∈ s, f i) α r` (with `[Fintype σ]`)
- **What**: If a finite sum of real polynomials is nonzero and every nonzero summand has index at least `c` (at `α`, weights `r`), then the sum has index at least `c`. This is the finite-sum form of `ind(P+Q) ≥ min(ind P, ind Q)` (source Lemma 4-1).
- **How**: `(le_index_iff hs).2`; for `d` with `(Δ_d Σ f_i)(α) ≠ 0`, push `hasseDeriv` and `eval` through the sum with `map_sum`, pick a summand with nonzero value by `Finset.exists_ne_zero_of_sum_ne_zero`, note that summand is nonzero, and conclude with `(le_index_iff hfi).1`.
- **Hypotheses**: `hs` (sum nonzero; necessary because of the junk value `index 0 = 0`, evidence (3)); `hf` (lower bound on nonzero summands only; the guard `f i ≠ 0 →` is a genuine weakening, since a zero summand has index `0`, evidence (4)).
- **Uses from project**: `Roth.index`, `Roth.le_index_iff`, `MvPolynomial.hasseDeriv` (via `map_sum`, it is a linear map)
- **Used by**: Roth/Theta.lean:398 (bound for the index of the Leibniz expansion of the generalised Wronskian determinant)
- **Visibility**: public
- **Lines**: 115–126, proof length 5 lines
- **Notes**: listed under Main results in the module docstring ("the index of sums and products").

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/Theta.lean:398).
- Wrapper of 1–2 mathlib calls? No: it is two applications of the project lemma `le_index_iff` around mathlib's `Finset.exists_ne_zero_of_sum_ne_zero`; about 5 lines of reasoning.
- Does mathlib have it? Not for `Roth.index`. Generic analogue `AddValuation.map_le_sum`; `Roth.index` is not an `AddValuation` (real-valued, junk `0` at `0`). For `MvPowerSeries.weightedOrder` mathlib has only the binary `min_weightedOrder_le_add`.
- Too specific (inline?)? Single caller, but it is the source's Lemma 4-1 (sum part) and is a named main result of the file; inlining would expose the support/sInf reasoning in the already long Theta proof.
- Well-chosen? Yes; the nonzero-summand guard is exactly what the determinant expansion needs (some Leibniz terms vanish).
- Conclusion: `KEEP`. Action: none.

## Mathlibable assessment (Step 9)

Pre-filter: public, not `_aux`, docstring not internal/auxiliary, Step 8 KEEP, no `namespace Roth` in mathlib and no `le_index_sum` hit under `.lake/packages/mathlib/Mathlib/`. Not a glue lemma (real proof), so full run. Parent `Roth.index` is BORDERLINE-needs-human, so the re-aim rule does not force a re-aim, but the canonical analogue is checked anyway (Phase 4c row 7, Phase 6 attempt 2).

### Baseline (Phase 0)
- lake build:               ✓ clean (per brief; evidence file importing `Roth.Index` compiles)
- decl `Roth.le_index_sum`:  ✓ resolved at Roth/Index.lean:118
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index of a real multivariate polynomial at a point relative to positive integer weights (Roth §4)

### Statement (Phase 1)

`Roth.le_index_sum` is a theorem stating the following. Let `f_i ∈ ℝ[x_j : j ∈ σ]` for `i` in a finite set `s`, with `Σ_i f_i ≠ 0`, and let `c ∈ ℝ`. If `ind_{α,r}(f_i) ≥ c` for every `i ∈ s` with `f_i ≠ 0`, then `ind_{α,r}(Σ_i f_i) ≥ c`. Equivalently, `ind(Σ f_i) ≥ min_{f_i ≠ 0} ind(f_i)`, the ultrametric inequality for the index.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: variables; `ι`, `s`: index type and finite index set
- `f`: the family of summands; `α`, `r`: point and weights; `c`: the lower bound

Hypotheses (Lean side):
- `hs : ∑ i ∈ s, f i ≠ 0`: the sum is nonzero (compensates the junk value at `0`)
- `hf`: `c` is a lower bound of the indices of the nonzero summands

Conclusion (math): `ind(Σ f_i) ≥ c`.

Conclusion (Lean): `c ≤ index (∑ i ∈ s, f i) α r`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: listed under Main results of the file, but mathematically it is the sum half of source Lemma 4-1, an immediate consequence of the definition (ultrametric inequality for a minimum over a support); no new structure.

### One-line check (Phase 2b)

Body line count: 5 (tactic proof)
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---|---|---|---|---|
| 1 | WebSearch (specific form) | Roth's theorem index of polynomial "ind(P+Q)" min index sum lemma | partial | index = min weighted degree of nonzero Taylor coefficients (arXiv math/0307203, 1806.10737); Wronskian index bounded below by a min over permutations of sums of indices (arXiv 1305.0926) | the sum inequality is used (exactly as in our only caller) but not stated as a separate lemma; immediate from the definition |
| 2 | WebSearch (general form) | valuation of a finite sum at least minimum of valuations of summands ultrametric inequality | yes | `v(x+y) ≥ min(v x, v y)` (valuation notes, arXiv 2409.16393); finite sums by induction | standard ultrametric inequality |
| 3 | WebSearch (aliases) | order of vanishing at a point of a sum of polynomials at least the minimum order of vanishing weighted multiplicity | partial | order of vanishing via vanishing derivatives (arXiv 1310.6482, 2107.05353) | `ord(f+g) ≥ min` is folklore, not stated explicitly |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not among available tools) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "lem4-1", "min" | yes | clean.tex l.589–597 Lemma 4-1 (`ind(P+Q) ≥ min(ind P, ind Q)` with `ind(0)=+∞`); l.825–833 applies it to the determinant expansion (min over `S_l`) | our lemma is exactly the finite-sum form used at l.825–827 |
| 6 | nLab | valuation / ultrametric | yes | valuation axioms include `v(x+y) ≥ min` | generic; no weighted point-order |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | valuation, order of vanishing | partial | discrete valuations satisfy the ultrametric inequality | no weighted point-order; same inequality |
| 9 | MathOverflow / Math.SE | (covered by #2, #3 results) | no | — | folklore; no stand-alone statement |
| 10 | recent arXiv (last 5 years) | (#1, #2 results: 2502.00731 (2025), 2409.16393 (2024)) | yes | same definitions and ultrametric inequality | nothing more general |

### Literature summary (Phase 3)

Concept identified as: the ultrametric (non-archimedean) inequality for the index, i.e. for a weighted order of vanishing at a point / monomial valuation, extended to finite sums.
Sources agree on the standard form: yes. `v(Σ x_i) ≥ min v(x_i)`, with `v(0) = +∞`.
Most general standard form: for any additive valuation (or any "order" function that is a minimum over a support) on a ring, `v(Σ_{i∈s} x_i) ≥ g` whenever `v(x_i) ≥ g` for all `i ∈ s`.
Generality dimensions where the literature varies:
  - value at `0`: `+∞` (source, mathlib), where no guard or nonvanishing is needed, vs the project's junk `0`, which forces `hs` and the `f i ≠ 0 →` guard
  - weights / coefficients: as for the parent def
Disagreement with the literature: none; the extra hypotheses come only from the junk-value convention, recorded in the parent report.

### Generality analysis — `Roth.le_index_sum`

Literature-standard form: `(∀ i ∈ s, g ≤ v(x_i)) → g ≤ v(Σ x_i)`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hs : Σ f_i ≠ 0` | nonzero sum | not needed when `ind 0 = ∞` | no (for this def) | for the empty sum and `c = 1` the conclusion fails (evidence (3), compiled) |
| 2 | `hf` guarded by `f i ≠ 0` | bound on nonzero summands only | bound on all summands | already weaker than the naive form | the unguarded form is strictly stronger as a hypothesis since `index 0 = 0` (evidence (4)) |
| 3 | coefficients `ℝ`, `[Fintype σ]` | fixed by `Roth.index` | any semiring | inherited | determined by the parent def |
| 4 | positivity of `r` | not assumed | — | already maximal | holds for all `r` |
| 5 | `Finset` sum vs binary `P + Q` | finite sum | binary in source | already more general | binary case is the two-element instance |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL relative to the parent definition `Roth.index`.
Number of weakening opportunities found: 0 (the one remaining hypothesis `hs` verified necessary; the guard in `hf` is already the weak form).
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no bundled hypotheses |
| 2 | sequences to filters? | no | — | finite algebraic statement |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | inherited | only via the parent def | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (re-aim) | `(∀ i ∈ s, n ≤ (f i).weightedOrder w) → n ≤ (Σ f i).weightedOrder w` | composes from `MvPowerSeries.le_weightedOrder` + `coeff_eq_zero_of_lt_weightedOrder` (evidence (2)); mathlib lacks only a packaged finite-sum version (it has binary `min_weightedOrder_le_add`) |
| 8 | concrete-via-abstract? | yes, trivially | the proof uses only that the index is a min over a support and the support of a sum is in the union of supports; this is `AddValuation.map_le_sum` in spirit | `Roth.index` is not an `AddValuation` (real-valued, junk 0, and not multiplicative-additive without nonvanishing), so the abstract lemma does not apply directly |
| 9 | false-generalisation guard | no false generalisation | the `weightedOrder` form is the canonical analogue, not a drop-in for the real-valued index | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no new contribution. The re-aimed statement is a two-call composition (evidence (2)); a packaged `MvPowerSeries.le_weightedOrder_sum` would be a generic convenience lemma, not this project's statement.

### Proof strategy — `Roth.le_index_sum`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | marginal | a finite-sum `weightedOrder` lower bound would let the proof go through `index_eq_weightedOrder_div`, but that needs positive `r` and is not shorter | n/a |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. A term-mode variant compiles (evidence (1)).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status

[A] Lean-Finder       "lower bound for the valuation of a finite sum given lower bounds for each summand"   hits: `AddValuation.map_le_sum`, `AddValuation.map_lt_sum`, `Valuation.map_sum_le`, `Valuation.map_sum_lt`
[B] Loogle            `MvPowerSeries.weightedOrder, Finset.sum`   hits: only `le_weightedOrder_prod`, `weightedOrder_prod` (products, not sums)
[C] LeanSearch        "order of a finite sum of power series is at least a common lower bound of the orders of the summands"   hits: binary only: `MvPowerSeries.min_order_le_add`, `PowerSeries.min_order_le_order_add`, `HahnSeries.min_order_le_order_add`, `meromorphicOrderAt_add`
[D] Grep mathlib src  `le_index_sum` (no hit); `order.*sum` in RingTheory/MvPowerSeries, PowerSeries, HahnSeries (no finite-sum lower bound); `map_le_sum` (RingTheory/Valuation/Basic.lean:1179); `min_weightedOrder_le_add` (RingTheory/MvPowerSeries/Order.lean:245)
[E] Name pattern      `lean_local_search` not run (grep [D] used instead, as in sibling reports)

Searched for both: the project form (index of a finite sum) and the literature-standard form (valuation / weighted order of a finite sum).

Concluded: found building blocks (`Finset.exists_ne_zero_of_sum_ne_zero`, `map_sum`, project `le_index_iff`); canonical analogues `AddValuation.map_le_sum` (generic) and binary `MvPowerSeries.min_weightedOrder_le_add`; no finite-sum `weightedOrder` lemma in mathlib.

### Normal-form check

Equivalent formalisms: `min`-form `ind(Σ f_i) ≥ min_{f_i≠0} ind f_i` (needs `Finset.inf'` over the nonzero summands); common-lower-bound form (chosen). Mathlib's canonical shape for finite sums is the common-lower-bound form (`AddValuation.map_le_sum`, `Finset.le_inf'_iff` style), which this lemma follows. RHS convention: n/a (inequality).

### Syntactic generality

Alternatives: (a) `min`/`inf'` form; (b) unguarded `∀ i ∈ s, c ≤ index (f i) α r`; (c) chosen guarded form. Chosen: (c). The caller (Theta.lean:398) applies it as `le_index_sum hdet fun s _ hs ↦ ?_` and uses the nonvanishing `hs` of the Leibniz term to derive nonvanishing of each matrix entry; form (b) would force a separate case split on zero terms, and (a) would need a nonempty filtered finset.

### Superfluous-argument audit

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hs` | yes | empty sum, `c = 1` is a counterexample (evidence (3)) |
| 2 | `f i ≠ 0 →` guard in `hf` | yes (as a weakening) | dropping the guard strengthens the hypothesis |
| 3 | `[Fintype σ]` | yes (via `Roth.index`/`weight`) | inherited |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE
Overall: SHIP-AS-STATED (locally)

### Call sites

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern |
|---|---|
| Roth/Theta.lean:398 | `refine le_index_sum hdet fun s _ hs ↦ ?_` (index of the Leibniz expansion `Matrix.det_apply'` of the generalised Wronskian) |

Inline-derivation grep: none found. No other site combines `Finset.exists_ne_zero_of_sum_ne_zero` with `le_index_iff`; `index_prod` (Index.lean:175) is the product counterpart, not a re-derivation.

### Composition check (Phase 6)

Can `Roth.le_index_sum` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(le_index_iff hs).2 fun d hd ↦ …` with `Finset.exists_ne_zero_of_sum_ne_zero (by simpa [map_sum] using hd)` and `(le_index_iff hfi).1 (hf i hi hfi) d hid`
  - Mathlib decls used: `map_sum`, `Finset.exists_ne_zero_of_sum_ne_zero`; project `Roth.le_index_iff`
  - Result: succeeds (evidence (1), compiled)

Attempt 2 (re-aim at the canonical object): finite-sum lower bound for `MvPowerSeries.weightedOrder` via `le_weightedOrder w fun d hd ↦ by rw [map_sum]; exact Finset.sum_eq_zero fun i hi ↦ coeff_eq_zero_of_lt_weightedOrder w (hd.trans_le (hf i hi))`
  - Result: succeeds (evidence (2), compiled); no nonvanishing hypothesis needed since `weightedOrder 0 = ⊤`.

Conclusion: COMPOSABLE. Two applications of the project's `le_index_iff` around one mathlib lemma; the canonical analogue is a two-call composition of existing mathlib API.

## Verdict: `Roth.le_index_sum`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the ultrametric inequality `v(Σ x_i) ≥ min v(x_i)` for valuations / orders of vanishing; the source's Lemma 4-1 (clean.tex l.589–597) and its use for the determinant expansion (l.825–833).
- Generality analysis (Phase 4): MAXIMALLY GENERAL relative to `Roth.index`; `hs` necessary (evidence (3)).
- Mathlib search (Phase 5): building blocks `Finset.exists_ne_zero_of_sum_ne_zero`, `map_sum`; analogues `AddValuation.map_le_sum`, `MvPowerSeries.min_weightedOrder_le_add`.
- Composition check (Phase 6): COMPOSABLE (evidence (1), (2)).

**Rationale:**

The lemma is the finite-sum ultrametric inequality for the project's index: a nonzero Hasse-derivative value of the sum at `α` forces a nonzero value for some summand (`Finset.exists_ne_zero_of_sum_ne_zero` after `map_sum`), whose weight is then bounded below by that summand's index (`le_index_iff`). Mathematically there is nothing new for mathlib. For a bundled valuation mathlib already has `AddValuation.map_le_sum`; for mathlib's canonical weighted order the analogous statement is a two-call composition of `le_weightedOrder` and `coeff_eq_zero_of_lt_weightedOrder` (evidence (2)). The only missing piece would be a packaged `MvPowerSeries.le_weightedOrder_sum`, a generic convenience lemma unrelated to this project's real-valued index. The extra hypotheses (`hs`, the nonvanishing guard) exist only because of the junk value `index 0 = 0`, which belongs to the parent's (BORDERLINE) question.

Despite having one caller, it should be kept rather than inlined: it is the sum part of the source's Lemma 4-1, a named main result of the file, and the caller (Theta.lean:398) is already a long determinant estimate. Junk verdict KEEP.

Belongs-elsewhere check: keep in Roth/Index.lean beside `index_mul` / `index_prod`.
Mathlib building blocks: `Finset.exists_ne_zero_of_sum_ne_zero` (Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean), `map_sum`; analogues `AddValuation.map_le_sum` (Mathlib/RingTheory/Valuation/Basic.lean:1179), `MvPowerSeries.min_weightedOrder_le_add` (Mathlib/RingTheory/MvPowerSeries/Order.lean:245), `MvPowerSeries.le_weightedOrder` (Order.lean:197), `MvPowerSeries.coeff_eq_zero_of_lt_weightedOrder` (Order.lean:180).
Composition sketch:
```lean
example (hs : ∑ i ∈ s, f i ≠ 0) (hf : ∀ i ∈ s, f i ≠ 0 → c ≤ index (f i) α r) :
    c ≤ index (∑ i ∈ s, f i) α r :=
  (le_index_iff hs).2 fun d hd ↦ by
    obtain ⟨i, hi, hid⟩ := Finset.exists_ne_zero_of_sum_ne_zero (by simpa [map_sum] using hd)
    exact (le_index_iff fun h0 ↦ hid (by simp [h0])).1 (hf i hi fun h0 ↦ hid (by simp [h0])) d hid
```
Call sites in our project: 1 (Roth/Theta.lean:398).
Refactor plan: none. Inlining at Theta.lean:398 is mechanically possible (the sketch above) but not recommended: the lemma is the source's Lemma 4-1 and keeps the determinant estimate readable. If `Roth.index` is ever rebased on `weightedOrder (taylor α P)` (parent question 3), reprove via a finite-sum `weightedOrder` lower bound (evidence (2)) and drop `hs` and the guard.
Next action: no upstreaming; keep as is.

---

## Next step

No upstreaming; keep `Roth.le_index_sum` as the sum form of Lemma 4-1. Optionally, independently of this project, a `MvPowerSeries.le_weightedOrder_sum` convenience lemma (evidence (2)) could be proposed for Mathlib/RingTheory/MvPowerSeries/Order.lean.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.le_index_sum/compose_reaim_necessity.lean` (imports `Roth.Index`) compiled clean with `lake env lean` (about 23 s). It contains:
  - (1) composition via `le_index_iff`, `map_sum`, `Finset.exists_ne_zero_of_sum_ne_zero`;
  - (2) re-aimed finite-sum lower bound for `MvPowerSeries.weightedOrder` via `le_weightedOrder` + `coeff_eq_zero_of_lt_weightedOrder`;
  - (3) `hs` is necessary: empty sum, `c = 1` fails (`simp [index]`);
  - (4) `index 0 = 0` (why the guard in `hf` is a weakening).
- WebSearch ×3 (queries in the literature table).
- Loogle `MvPowerSeries.weightedOrder, Finset.sum` (products only); LeanSearch and Lean-Finder queries as recorded.
- Greps: mathlib for `le_index_sum`, `order.*sum`, `map_le_sum`, `min_weightedOrder_le_add`; project for call sites; clean.tex for "lem4-1", "min".
- `ask_chatgpt_math` MCP not configured in this session.
