---
decl: Roth.le_index_of_forall_eval_eq_zero
file: Roth/MainLemma.lean
line: 419
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: Vanishing of all box Hasse derivatives of weight below c gives c at most the index; it is le_index_iff.2 plus hasseDeriv_eq_zero_of_degreeOf_lt (compiled re-proof), the box-free form is the analogue of mathlib MvPowerSeries.le_weightedOrder, hP and hd both necessary (compiled counterexamples), single caller, nothing new for mathlib.
action: Keep in Roth/MainLemma.lean as the named Lemma 9 step (sole caller exists_mem_RSet_le_index_aux at Roth/MainLemma.lean:562), optionally move next to le_index_iff in Roth/Index.lean; no mathlib PR.
---

# Roth.le_index_of_forall_eval_eq_zero

## Inventory entry

### `theorem Roth.le_index_of_forall_eval_eq_zero`
- **Type**: `{σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hd : ∀ j, degreeOf j P ≤ r j) (α : σ → ℝ) {c : ℝ} (hvan : ∀ d, (∀ j, d j ≤ r j) → weight r d < c → eval α (hasseDeriv d P) = 0) : c ≤ index P α r`
- **What**: For a nonzero real polynomial `P` with `deg_{x_j} P ≤ r_j` for all `j`, if every Hasse derivative `Δ_d P` with `d` in the box `d ≤ r` and weight `∑ d_j/r_j < c` vanishes at `α`, then the index of `P` at `α` relative to `r` is at least `c`.
- **How**: `(le_index_iff hP).2`: for `d` with `(Δ_d P)(α) ≠ 0`, argue by contradiction on `weight r d < c`; `d` lies in the box because otherwise `d j > r j ≥ degreeOf j P` for some `j` and `hasseDeriv_eq_zero_of_degreeOf_lt` makes `Δ_d P = 0` (then `map_zero`); inside the box `hvan` gives vanishing, contradiction.
- **Hypotheses**: `hP : P ≠ 0` (needed by `le_index_iff`, junk `index 0 = 0`; necessary, evidence (2)); `hd` coordinate degree bounds (restrict the check to the box; necessary, evidence (3)); `hvan` the vanishing hypothesis. No positivity of `r`.
- **Uses from project**: `Roth.index`, `Roth.weight`, `Roth.le_index_iff`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`
- **Used by**: `Roth.exists_mem_RSet_le_index_aux` (private, Roth/MainLemma.lean:562). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 412–425 (docstring 412–418, statement 419–422), proof length 3 lines
- **Notes**: Paper step: §6, proof of Lemma 9 (clean.tex l.1511, "Multi-indices outside the degree box give identically zero derivatives as well. Hence the index of W^* ... is at least γ").

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:562 inside the private `exists_mem_RSet_le_index_aux`.
- Wrapper of 1–2 mathlib calls? It wraps one project API lemma (`le_index_iff`) and one project lemma (`hasseDeriv_eq_zero_of_degreeOf_lt`); no direct mathlib content beyond `le_of_not_gt`, `map_zero`.
- Does mathlib have it? No (project-local `index`, `hasseDeriv`); the box-free analogue for power series is `MvPowerSeries.le_weightedOrder`.
- Too specific (inline)? Single caller and a 3-line proof, but it names exactly one sentence of the paper (the box reduction) and keeps the caller's `refine` readable; same treatment as siblings `sub_mem_RSet`, `eval_hasseDeriv_sub_eq_zero` (both KEEP).
- Well-chosen? Yes: the strict cutoff and box restriction match the consumer, which only knows vanishing for box multi-indices `d ∈ J`.
- Conclusion: `KEEP`. Optional: relocate to Roth/Index.lean beside `le_index_iff` / `index_le_card` (it only needs `Roth.Index` + `Roth.HasseDeriv`, evidence (1) compiles importing `Roth.Index`).

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name absent from mathlib (grep for `le_index_of_forall` and `namespace Roth` in `.lake/packages/mathlib/Mathlib/`: 0 hits). Not a glue lemma (real proof using `le_index_iff` plus a box argument), so INHERITED does not apply; full run. Parent `Roth.index` is BORDERLINE-needs-human (not NO-mathlib-has-it), so no re-aim; the canonical analogue is still checked (Phase 4c row 7, Phase 6 attempt 2).

### Baseline (Phase 0)
- lake build:               ✓ clean (per brief; evidence file importing `Roth.Index` elaborates clean)
- decl `Roth.le_index_of_forall_eval_eq_zero`: ✓ resolved at Roth/MainLemma.lean:419
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's Lemma 9 (the main lemma): existence of an auxiliary integer polynomial with large index at (α, …, α) and controlled coefficients.

### Statement (Phase 1)

`Roth.le_index_of_forall_eval_eq_zero` is a theorem stating the following:

Let `P ∈ ℝ[x_j : j ∈ σ]` be nonzero with `deg_{x_j} P ≤ r_j` for every `j`, let `α ∈ ℝ^σ` and `c ∈ ℝ`. If `(Δ_d P)(α) = 0` for every multi-index `d` with `0 ≤ d_j ≤ r_j` and `∑_j d_j/r_j < c`, then `ind_{α,r}(P) ≥ c`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: finite variable set (needed by `weight`, `index`)
- `P`: the polynomial; `r`: degree bounds = weights; `α`: the point; `c`: the cutoff

Hypotheses (Lean side):
- `hP : P ≠ 0`: nonzero polynomial
- `hd : ∀ j, degreeOf j P ≤ r j`: P lies in the degree box
- `hvan`: box derivatives of weight `< c` vanish at `α`

Conclusion (math): the index of `P` at `α` is at least `c`.

Conclusion (Lean): `c ≤ index P α r`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: one step inside the proof of Lemma 9; not listed as a main result, not named.

### One-line check (Phase 2b)

Body line count: 3 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form) | Roth's theorem auxiliary polynomial index at least if all derivatives with sum i_j/r_j less than theta vanish | partial | index = min of `∑ k_j/r_j` over nonvanishing derivatives (arXiv math/0307203, 2502.00731, Evertse Leiden notes) | the contrapositive ("index < η gives a nonvanishing derivative of weight < η") appears in math/0307203; the lower-bound form is inline |
|  2 | WebSearch (general form) | order of vanishing of polynomial at a point lower bound all partial derivatives of order less than m vanish degree bounded box | yes | multiplicity ≥ k iff all derivatives of order ≤ k−1 vanish (arXiv 2010.00077, LibreTexts) | definitional; no box restriction appears because derivatives outside the degree box are zero |
|  3 | WebSearch (named / aliases) | "Hasse derivative" multiplicity vanishing "weighted" index polynomial box degree Siegel lemma Roth | yes | multiplicity via Hasse derivatives (arXiv 1310.6482, 2403.19824); weighted index (2502.00731 review, Evertse Bonn notes) | always stated as a definition, never as a separate lemma |
|  4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
|  5 | Local references | grep `.mathlib-quality/references/clean.tex` for "W^*", "at least" | yes | l.1511: "Multi-indices outside the degree box give identically zero derivatives as well. Hence the index of W^* ... is at least γ" | exactly the sentence formalised |
|  6 | nLab | Hasse derivative order of vanishing (WebSearch restricted to ncatlab.org) | partial | Hasse-Schmidt derivative page (definition only) | nothing on weighted order / index |
|  7 | nCatLab | n/a | n/a | n/a | not a categorical concept (elementary finite minimum) |
|  8 | Stacks Project | n/a | n/a | n/a | weighted point-index of a real polynomial is not an algebraic-geometry concept treated there; the lower-bound reading of an order of vanishing would be definitional |
|  9 | MathOverflow / Math.SE | covered by #2/#3 results | no | none | folklore; no thread states this |
| 10 | recent arXiv (last 5 years) | #1/#3 hit arXiv 2502.00731 (2025), 2403.19824 (2024) | yes | same definitions | step is inline |

### Literature summary (Phase 3)

Concept identified as: the lower-bound reading of the definition of the (weighted) index / order of vanishing: if all Taylor coefficients of `P(x+α)` of weighted degree `< c` vanish, the index is `≥ c`; plus the observation that coefficients outside the degree box vanish automatically.
Sources agree on the standard form: yes; definitional and always inline.
Most general standard form: for any (semi)ring and weights, `(∀ d, w(d) < n → coeff_d f = 0) → n ≤ ord_w(f)` (mathlib's `MvPowerSeries.le_weightedOrder`), no box restriction needed.
Generality dimensions where the literature varies:
  - weights: ℕ (mathlib) vs real `1/r_j` (Roth)
  - coefficients: ℝ vs any (semi)ring
  - test set: all `d` (standard) vs box `d ≤ r` (here, with `hd` making the two equivalent)
Disagreement with the literature: none.

### Generality analysis — `Roth.le_index_of_forall_eval_eq_zero`

Literature-standard form: `(∀ d, w(d) < n → coeff_d f = 0) → n ≤ ord_w f`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `hP : P ≠ 0` | nonzero | not needed when `ord 0 = ∞` | no (for this def) | with junk `index 0 = 0` the statement fails for `P = 0`, `c = 1` (evidence (2), compiled) |
| 2 | `hd` | degree box | absent (test all `d`) | no | dropping `hd` makes the conclusion false: `P = X²`, `r = 1`, `α = 0`, `c = 3` (evidence (3), compiled); `hd` is the price of testing only box `d` |
| 3 | `hvan` restricted to box | box + weight `< c` | all `d` with weight `< c` | n/a | the box restriction makes the hypothesis weaker, i.e. the lemma stronger; it is the useful direction for the caller |
| 4 | coefficients `ℝ`, `[Fintype σ]` | fixed by `Roth.index` | any semiring | inherited | determined by the parent def |
| 5 | positivity of `r` | not assumed | — | already maximal | holds for all `r` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (relative to the parent `Roth.index`)
Number of weakening opportunities found: 0 (both hypotheses `hP`, `hd` verified necessary in evidence (2), (3))
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | single-use hypotheses | — |
| 2 | sequences to filters? | no | finite algebraic statement | — |
| 3 | construction vs universal property? | no | it is the glb property of the defining minimum (via `le_index_iff`) | — |
| 4 | bundled substructure? | no | the box could be `d ∈ box r` (project `Roth.box`), cosmetic | — |
| 5 | field-specific to semiring? | inherited | only via parent def | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (re-aim) | `(∀ d, weight w d < n → coeff d (taylor α P) = 0) → n ≤ weightedOrder w (taylor α P)` | is exactly `MvPowerSeries.le_weightedOrder` (no box needed) |
| 8 | concrete-via-abstract? | yes, trivially | proof uses only: `index` is a glb (`le_index_iff`) and derivatives beyond the degree vanish | both abstractions already exist (mathlib `le_weightedOrder`; project `hasseDeriv_eq_zero_of_degreeOf_lt`) |
| 9 | false-generalisation guard | no false generalisation | the `weightedOrder` analogue is the canonical object but not a drop-in for the ℝ-valued index (as for the parent) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
One-line reason: the canonical analogue is already mathlib's `MvPowerSeries.le_weightedOrder`; the box restriction is a project-specific convenience, not a new organisational idea.

### Proof strategy — `Roth.le_index_of_forall_eval_eq_zero`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | already via the glb lemma | — |
| 5 | missing mathlib helpers | no | — | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (3 lines, reduces to the def's API lemma).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status

[A] Lean-Finder       "lower bound on order of vanishing of a polynomial at a point if all derivatives of low weight vanish there and degree is bounded in each variable"   hits: `MvPowerSeries.nat_le_order`, `le_order`, `le_weightedOrder`, `nat_le_weightedOrder` (box-free analogues)
[B] Loogle            `_ ≤ MvPowerSeries.weightedOrder _ _`   hits: `MvPowerSeries.le_weightedOrder` (the analogue), `le_weightedOrder_mul`, `_prod`, `_pow`, `_map`, `_smul` (unrelated)
[C] LeanSearch        "if all coefficients of weighted degree less than n vanish then weighted order is at least n"   hits: `MvPowerSeries.le_weightedOrder`, `nat_le_weightedOrder`, `le_order`, `coeff_eq_zero_of_lt_weightedOrder`
[D] Grep mathlib src  `le_index_of_forall`, `index_of_forall_eval`, `namespace Roth`: 0 hits; `le_weightedOrder` at Mathlib/RingTheory/MvPowerSeries/Order.lean:197
[E] Name pattern      grep [D] used in place of `lean_local_search` (no MvPolynomial Hasse derivative or point index exists in mathlib; see `MvPolynomial.hasseDeriv`, `Roth.index` reports)

Searched for both: the project form (box-restricted lower bound for the index) and the literature-standard form (lower bound for a weighted order).

Concluded: found building blocks; the canonical analogue is `MvPowerSeries.le_weightedOrder`; the project form is `le_index_iff.2` plus `hasseDeriv_eq_zero_of_degreeOf_lt`.

### Statement-shape verdict (Phase 5.5)

Normal-form check: equivalent formalisms are `∀ d ∈ box r, weight r d < c → …`, `∀ d, weight r d < c → …` (box-free, then `hd` unnecessary), and the `le_index_iff` form `∀ d, eval ≠ 0 → c ≤ weight`. Canonical form is `le_index_iff` (RHS pointwise); this lemma is the contrapositive-with-box consumer form, which is exactly what the caller supplies (`hJ d hd hw`). RHS convention: n/a (implication, not iff).
Syntactic generality: alternatives tried: box-free `hvan` (then no `hd`, but the caller only knows vanishing for `d ∈ J ⊆ box`); `d ∈ box r` membership. Chosen: current form; the caller passes `fun d hd hw ↦ …` directly.
Superfluous-argument audit:

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hP` | yes | evidence (2) |
| 2 | `hd` | yes | evidence (3) |
| 3 | `[Fintype σ]` | yes | via `weight`/`index` |

Normal form: OK. Syntactic generality: OK. Superfluous arguments: NONE.
Overall: SHIP-AS-STATED (locally)

### Call sites

Internal use count: 1 (declaring file only); external-to-file callers: 0 distinct files.

| Caller file:line | Usage pattern |
|---|---|
| Roth/MainLemma.lean:562 | `exact le_index_of_forall_eval_eq_zero (… hP.1) (by simpa … using hP.2.1) (fun _ ↦ α) fun d hd hw ↦ eval_hasseDeriv_sub_eq_zero hfα (hWeq d (hJ d hd hw))` in `exists_mem_RSet_le_index_aux` |

Inline-derivation grep: none; other lower bounds on the index (`le_index_sum`, `index_unique`, `index_eq_weightedOrder_div`) call `le_index_iff` directly and do not re-derive the box argument.

### Composition check (Phase 6)

Attempt 1: `(le_index_iff hP).2 fun d he ↦ le_of_not_gt fun hw ↦ he (hvan d (box from hasseDeriv_eq_zero_of_degreeOf_lt) hw)`
  - Decls used: project `Roth.le_index_iff`, project `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, mathlib `le_of_not_gt`, `map_zero`
  - Result: succeeds (evidence (1), compiled importing only `Roth.Index`)
Attempt 2 (canonical analogue): `MvPowerSeries.le_weightedOrder w h` — the box-free statement for the ℕ-weighted order is a single mathlib call.
  - Result: exists in mathlib verbatim (Order.lean:197).

Conclusion: COMPOSABLE (two project API lemmas; analogue is one mathlib lemma).

## Verdict: `Roth.le_index_of_forall_eval_eq_zero`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the index / order of vanishing is defined as a minimum; the lower-bound reading is definitional and always inline (clean.tex l.1511).
- Generality analysis (Phase 4): MAXIMALLY GENERAL; `hP`, `hd` necessary (evidence (2), (3)).
- Mathlib search (Phase 5): canonical analogue `MvPowerSeries.le_weightedOrder`; no point index in mathlib.
- Composition check (Phase 6): COMPOSABLE.

**Rationale:**

The statement is the lower-bound direction of the defining minimum of `Roth.index` (packaged by `le_index_iff`), plus the remark that Hasse derivatives outside the degree box vanish identically (`hasseDeriv_eq_zero_of_degreeOf_lt`). For mathlib's canonical weighted order the box-free version is literally `MvPowerSeries.le_weightedOrder`, and with the full test set the box hypothesis `hd` disappears. Nothing here is new mathematics for mathlib; its upstream fate is tied to the parent `Roth.index` (BORDERLINE) and to `MvPolynomial.hasseDeriv`.

WHY not: the content is a 2-lemma composition of project API whose mathlib analogue already exists. Belongs-elsewhere: keep project-local, either in Roth/MainLemma.lean (named Lemma 9 step) or beside `le_index_iff` / `index_le_card` in Roth/Index.lean.
Building blocks: project `Roth.le_index_iff` (Roth/Index.lean:85), project `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` (Roth/HasseDeriv.lean:219); mathlib analogue `MvPowerSeries.le_weightedOrder` (Mathlib/RingTheory/MvPowerSeries/Order.lean:197).
Composition sketch:
```lean
example (hP : P ≠ 0) (hd : ∀ j, degreeOf j P ≤ r j)
    (hvan : ∀ d, (∀ j, d j ≤ r j) → weight r d < c → eval α (hasseDeriv d P) = 0) :
    c ≤ index P α r := by
  refine (le_index_iff hP).2 fun d he ↦ le_of_not_gt fun hw ↦ he (hvan d (fun j ↦ ?_) hw)
  by_contra! hj
  exact he <| by rw [hasseDeriv_eq_zero_of_degreeOf_lt ((hd j).trans_lt hj), map_zero]
```
Call sites in our project: 1 (Roth/MainLemma.lean:562).
Refactor plan: none required. Inlining at Roth/MainLemma.lean:562 is possible (3 lines) but not recommended: it would mix the box argument into the coercion-heavy caller and lose the paper-sentence correspondence. Optional: move the lemma to Roth/Index.lean.
Next action: no upstreaming; keep as is.

---

## Next step

Do not upstream; keep `Roth.le_index_of_forall_eval_eq_zero` (sole caller Roth/MainLemma.lean:562), optionally relocating it to Roth/Index.lean beside `le_index_iff`. No mathlib PR.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.le_index_of_forall_eval_eq_zero/experiments.lean` (imports `Roth.Index`), checked with `lean_diagnostic_messages`: clean, no warnings, no sorry. Contains:
  - (1) re-proof of the declaration from `le_index_iff` + `hasseDeriv_eq_zero_of_degreeOf_lt`;
  - (2) `hP` necessary: for `P = 0`, `r = 0`, `c = 1` all hypotheses hold but `1 ≤ index 0 α r` fails;
  - (3) `hd` necessary: for `P = X²` in one variable, `r = 1`, `α = 0`, `c = 3`, all box derivatives vanish at 0 but `index ≤ weight (single () 2) = 2 < 3`.
- WebSearch ×4 (three generality levels + nLab-restricted), queries in the literature table.
- Loogle `_ ≤ MvPowerSeries.weightedOrder _ _`; LeanSearch and Lean-Finder queries as recorded.
- Greps: mathlib for `le_index_of_forall`, `index_of_forall_eval`, `namespace Roth` (0 hits); project for call sites; clean.tex for `W^*` (l.1505–1511).
- `ask_chatgpt_math` MCP not configured in this session.
