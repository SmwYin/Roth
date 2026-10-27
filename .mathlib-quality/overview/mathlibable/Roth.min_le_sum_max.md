---
decl: Roth.min_le_sum_max
file: Roth/Theta.lean
line: 362
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: The combined numeric estimate of Roth's Lemma 6 (min(lθ/2, r θ²/3) ≤ ∑_{ν<l} max(0, θ - ν/r)); it has no standing in the literature and no counterpart in mathlib, and it is not a ≤3-call composition (it needs the Gauss sum plus a floor argument), so neither a YES nor a NO bucket fits; recommended resolution is to keep it in the project.
action: Keep in Roth/Theta.lean as a project lemma (single caller Roth.index_le_lem6, Roth/Theta.lean:586); optionally generalise rp : ℕ to r : ℝ (same proof, compiled in evidence/Roth.min_le_sum_max/generalise_real_r.lean) and fix the docstring's leading "If θ r_p > 10" since the Lean statement has no such hypothesis.
---

# Roth.min_le_sum_max

## Inventory entry

### `theorem Roth.min_le_sum_max`
- **Type**: `∀ {θ : ℝ} {rp : ℕ} (l : ℕ), min (↑l * θ / 2) (↑rp * θ ^ 2 / 3) ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ↑ν / ↑rp)`
- **What**: For all real θ and natural l, r_p: the sum of positive parts ∑_{ν<l} max(0, θ - ν/r_p) is at least min(lθ/2, r_p θ²/3). This is the "Combining everything" bound of clean.tex §5, proof of Lemma 6 (l.880–910), stated without the source's hypotheses θ > 0 and θ r_p > 10.
- **How**: Case split. (i) θ ≤ 0: `min_le_left`, then lθ/2 ≤ 0 (`div_nonpos_of_nonpos_of_nonneg`, `mul_nonpos_of_nonneg_of_nonpos`) ≤ sum (`Finset.sum_nonneg`, `le_max_left`). (ii) l ≤ θ r_p: `min_le_left` with the private `mul_div_two_le_sum_max_aux` (Gauss sum `Finset.sum_range_id_mul_two`). (iii) θ r_p < l: `min_le_right` with the private `mul_sq_div_three_le_sum_max_aux` (which uses `mul_sq_div_three_le_sum_max_of_pos_aux`, a floor/Gauss-sum argument).
- **Hypotheses**: none (θ, r_p, l arbitrary). The source's assumptions θ > 0 and θ r_p > 10 are not needed.
- **Uses from project**: `Roth.mul_div_two_le_sum_max_aux` (private, Roth/Theta.lean:304), `Roth.mul_sq_div_three_le_sum_max_aux` (private, Roth/Theta.lean:347); transitively `Roth.mul_sq_div_three_le_sum_max_of_pos_aux` (private, l.322).
- **Used by**: `Roth.index_le_lem6` (Roth/Theta.lean:586). `grep -rn min_le_sum_max Roth/` gives only l.362 and l.586 (other hits are the `_aux` helpers' names).
- **Visibility**: public
- **Lines**: 357–370 (docstring 357–361, statement 362–363, proof 364–370), proof length 7 lines
- **Notes**: The docstring opens with "If `θ r_p > 10`, then …" although the Lean statement carries no such hypothesis (the last docstring line does say the inequality holds without them); the first sentence should be reworded. The sibling report for `mul_sq_div_three_le_sum_max_aux` recommends inlining that helper here (rp = 0 split + direct call to `mul_sq_div_three_le_sum_max_of_pos_aux`).

## Junk check (Step 8)
- Used anywhere? Yes, once: `Roth.index_le_lem6` (l.586), the step `ind F ≥ min(lθ/2, r_pθ²/3) - lδ` of Lemma 6.
- Wrapper of 1–2 mathlib calls? No; it dispatches to two project helpers that carry the real Gauss-sum and floor arguments.
- Does mathlib have it? No (Loogle `Finset.sum (Finset.range _) (fun _ => max 0 _)`: no hits; LeanSearch / Lean-Finder: unrelated Schlömilch-type and `Finset.sum_min_le` results; see Phase 5).
- Too specific (inline?)? It is Lemma-6-specific but is the displayed combined estimate in the source; naming it mirrors the paper and keeps `index_le_lem6` readable. Not recommended to inline.
- Well-chosen statement? Yes; hypothesis-free, which is strictly better than the source. Only the docstring's first clause is off.
- Conclusion: `KEEP` (project-local; reword docstring; optional `rp : ℕ` to `r : ℝ`).

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring does not start with internal/auxiliary; Step 8 said KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `min_le_sum_max`: no hit. Not a glue lemma (7-line proof with case split). The full workflow follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per the brief; the evidence file importing `Roth.Theta` compiles cleanly)
- decl `Roth.min_le_sum_max`: ✓ resolved at Roth/Theta.lean:362
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index across sets of polynomials `Θ_m(B; q; r)` and Lemmas 5, 6, 7 of the source.

### Statement (Phase 1)

`Roth.min_le_sum_max` is a theorem stating the following. For a real number θ and natural numbers l and r, the sum of the positive parts of the l terms θ, θ - 1/r, …, θ - (l-1)/r of a decreasing arithmetic progression is at least min(lθ/2, rθ²/3). Geometrically: if the progression stays positive for all l terms (l ≤ θr) the sum is a trapezoid of area ≥ lθ/2; otherwise it is (at least) a triangle with ~θr terms and height θ, of area ≥ rθ²/3.

Variables / typeclasses involved (Lean side):
- `θ : ℝ`: the index `ind R` of the polynomial in Lemma 6
- `rp : ℕ`: the weight r_p of the variable x_p
- `l : ℕ`: the size of the Wronskian-type determinant

Hypotheses (Lean side): none.

Conclusion (math): min(lθ/2, r_pθ²/3) ≤ ∑_{ν=0}^{l-1} max(0, θ - ν/r_p).

Conclusion (Lean): `min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / rp)`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an auxiliary numeric inequality inside the proof of Lemma 6; not a structure, not a main result, not named.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 7
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | `Roth theorem index lemma "\sum_{\nu=0}^{l-1} \max(0, \theta - \nu/r_p)" min(l θ/2, r θ^2/3)` | no | none | hits: Roth over function fields (arXiv 1806.10737), quantitative Roth (math/0307203), the subspace-theorem exposition (arXiv 2502.00731), Evertse's notes; none states this bound |
| 2 | WebSearch (general form) | `sum of positive parts of arithmetic progression lower bound min triangle area sum max(0, a - k/r) inequality` | no | none | hits are about Erdős–Debrunner and mean inequalities; the trapezoid/triangle comparison is folklore and not isolated anywhere |
| 3 | WebSearch (named-after / aliases) | `Roth's theorem proof Wronskian determinant index lower bound Cassels "index of F" Lemma 6 Schmidt Diophantine approximation` | partial | Wronskian-index lower bounds exist (arXiv 1305.0926 Prop. 6.21/Lemma 6.22; arXiv 2502.00731) | the index-of-Wronskian estimate appears in several forms, but this numeric min-bound is an internal step of the source's proof |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP is not configured in this session (no such tool among the deferred tools) |
| 5 | Local references | `grep -n "\\min" .mathlib-quality/references/clean.tex` | yes | clean.tex §5, l.893–910: the two cases θr_p < l (≥ r_pθ²/3, via the facts at l.860–890) and θr_p ≥ l (≥ lθ/2), combined into `ind F ≥ min(lθ/2, r_pθ²/3) - lδ` | the Lean statement is the source's combined bound, minus the source's hypotheses θ > 0 and θr_p > 10 |
| 6 | nLab | "arithmetic progression" / "index of a polynomial" | n/a | none | nLab covers no elementary real inequalities or Diophantine-approximation index estimates; absence confirmed |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | covered by queries #2 and #3 (general web search spans these sites) | no | none | no thread states this bound |
| 10 | recent arXiv (last 5 years) | covered by queries #1 and #3 (arXiv 2502.00731, 2025) | no | none | the modern exposition uses a different bookkeeping for the Wronskian index and never isolates this inequality |

### Literature summary (Phase 3)

Concept identified as: an auxiliary estimate in the Wronskian-index step of Roth's theorem (lower bound for the index of the determinant F in Lemma 6). Its only standard ingredient is the Gauss sum ∑_{ν<n} ν = n(n-1)/2.
Sources agree on the standard form: n/a; only the project's source states it, with hypotheses θ > 0, θ r_p > 10.
Most general standard form: none in the literature. The Lean form (no hypotheses) is already more general than the source.
Generality dimensions where the literature varies: none identified.
Disagreement with the literature: the Lean statement drops the source's θ r_p > 10 assumption (proved via a sharper floor argument), which is an improvement, not a disagreement.

### Generality analysis — `Roth.min_le_sum_max`

Literature-standard form (from Phase 3): only the source statement exists (with θ > 0, θ r_p > 10).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | θ > 0, θ r_p > 10 | absent | assumed | n/a | already dropped in the Lean statement |
| 2 | `rp : ℕ` | natural number | positive integer r_p | yes (cosmetic) | `r : ℝ` arbitrary works with the identical proof (helpers already take `r : ℝ`); compiled as `RothEvidence.min_le_sum_max_real`, and the ℕ form is its `r := ↑rp` instance by a bare term |
| 3 | `l : ℕ` | natural | integer l | NO | it indexes the sum |
| 4 | constants 1/2, 1/3 | fixed | fixed | NO | they are the source's constants; sharper constants would change the content consumed by `index_numeric_bound_aux` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (up to the cosmetic `rp : ℕ` to `r : ℝ` widening)
Number of weakening opportunities found: 1 (cosmetic; verified: `min_le_sum_max_real` compiles in evidence/Roth.min_le_sum_max/generalise_real_r.lean)
Proposed restatement: optional, `theorem min_le_sum_max {θ r : ℝ} (l : ℕ) : min (l * θ / 2) (r * θ ^ 2 / 3) ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r)`; the caller at l.586 would pass `(r := (r none : ℝ))` instead of `(rp := r none)`.
Cost of restatement: CHEAP (mechanical, proof unchanged)

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | typeclasses instead of bundled hypotheses | no | no hypotheses | n/a |
| 2 | filters instead of sequences | no | finite sum | n/a |
| 3 | universal property | no | no construction | n/a |
| 4 | bundled substructure | no | no sets | n/a |
| 5 | weaken field-specific typeclasses | partly | could be stated over a `LinearOrderedField` with `FloorSemiring` (the proof uses `⌊·⌋₊`, division, `linear_combination`) | none; nothing outside Roth consumes it |
| 6 | higher-categorical | no | n/a | n/a |
| 7 | concrete index generalised | yes (cosmetic) | `rp : ℕ` to `r : ℝ` (row 2 of 4a) | none beyond the caller |
| 8 | concrete-via-abstract | no | the statement mentions no named object; diagnostic n/a | n/a |
| 9 | false-generalisation guard | no | the `r : ℝ` widening is the same inequality (the ℕ form is a literal instance) | n/a |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
- Reason: a fixed-constant real inequality; the field-generic restatement would be generality for its own sake with no consumer.

### Proof strategy — `Roth.min_le_sum_max`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | n/a | n/a |
| 2 | elements vs ideals | no | n/a | n/a |
| 3 | sequences vs nets | no | n/a | n/a |
| 4 | construction vs universal property | no | n/a | n/a |
| 5 | missing mathlib helpers | no | uses `Finset.sum_range_id_mul_two`, `Nat.floor_le`, `Nat.lt_floor_add_one`, `Finset.sum_le_sum_of_subset_of_nonneg`; nothing missing | n/a |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (three-way case split dispatching to helpers; the one local improvement is the sibling report's suggestion to inline `mul_sq_div_three_le_sum_max_aux`, whose θ r = l branch is dead from this call site)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.min_le_sum_max`

[A] Lean-Finder       "sum of positive parts of a decreasing arithmetic progression is at least the minimum of half the trapezoid and a third of the triangle area"   no hits (only Schlömilch inequalities `Finset.le_sum_schlomilch'`, `Finset.sum_schlomilch_le`, `ENNReal.le_tsum_schlomilch`; unrelated)
[B] Loogle            `Finset.sum (Finset.range _) (fun _ => max 0 _)`   no hits
[C] LeanSearch        "lower bound for sum over range l of max 0 (θ - ν / r) by min of l θ / 2 and r θ^2 / 3"   no hits (`Finset.sum_range_le_sum`, `Finset.sum_min_le`, `Finset.le_sum_schlomilch`, unrelated)
[D] Grep mathlib src  `min_le_sum_max` (no hit); `sum_range_id_mul_two` (building block, Mathlib/Algebra/BigOperators/Intervals.lean:171)
[E] Name pattern      `lean_local_search min_le_sum_max`: n/a (tool error: ripgrep not on PATH); covered by the grep in [D]

Searched for both the user's form and the general principle (lower bounds for sums of positive parts / Riemann-sum comparison of a linear function): mathlib has only Schlömilch-type and integral-comparison bounds, none giving this.

Concluded: not in mathlib (all 5 methods exhausted, plus the general form); building blocks: `Finset.sum_range_id_mul_two`, `Nat.floor_le`, `Nat.lt_floor_add_one`, `Finset.sum_le_sum`, `Finset.sum_le_sum_of_subset_of_nonneg`.

### Normal-form check — `Roth.min_le_sum_max`

Equivalent formalisms this statement could take: the current `min … ≤ ∑ …`; a pair of conditional lemmas (l ≤ θr → lθ/2 ≤ ∑; θr ≤ l → rθ²/3 ≤ ∑); `∑ ν ∈ range l, (θ - ν/r)⁺` using `posPart`.
Does mathlib already have a canonical form for this idea? no.
Name the canonical form we'd propose: none (not proposed for mathlib). Locally, `max 0 x` matches the source and the caller `sum_max_sub_le_index_det`.
RHS convention respected? n/a (an inequality, not a simp lemma)

### Syntactic generality — `Roth.min_le_sum_max`

Alternative restatements attempted:
- `r : ℝ` instead of `rp : ℕ` (compiled)
- `(θ - ν / r)⁺` instead of `max 0 (θ - ν / r)`

Chosen restatement: the current form (or the `r : ℝ` variant).
Justification: matches the source display and the form produced by `sum_max_sub_le_index_det`, so the caller chains it with a single `.trans`.

### Superfluous-argument audit — `Roth.min_le_sum_max`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `θ : ℝ` | yes | the variable |
| 2 | `rp : ℕ` | yes, but its ℕ type is not essential | `r : ℝ` works (compiled) |
| 3 | `l : ℕ` | yes | indexes the sum |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (optional RESTATE to `r : ℝ`, cosmetic)
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.min_le_sum_max`

Internal use count: 1 (in the declaring file; 0 in other files)
External-to-file callers: 0

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:586 | `exact (min_le_sum_max (θ := index (map (Int.castRingHom ℝ) R) α r) (rp := r none) l).trans` in `Roth.index_le_lem6` |

Inline-derivation grep: `grep -rn "min (l \* θ / 2)\|max 0 (θ - ν" Roth/` shows only this lemma and its private helpers; no re-derivation elsewhere.

### Composition check (Phase 6)

Can `Roth.min_le_sum_max` be derived from mathlib in ≤3 chained calls?

Attempt 1: `min_le_left` + `Finset.sum_range_id_mul_two` + `Finset.sum_le_sum` for the case l ≤ θr.
  - Mathlib decls used: `min_le_left`, `Finset.sum_range_id_mul_two`, `Finset.sum_le_sum`, `Finset.sum_sub_distrib`
  - Result: fails as a composition (needs casts, rewriting and a `linarith` step; this is the 15-line `mul_div_two_le_sum_max_aux`)
Attempt 2: the θr < l case via `Nat.floor_le`, `Nat.lt_floor_add_one`, `Finset.sum_le_sum_of_subset_of_nonneg`.
  - Result: fails (a `linear_combination` certificate and a 4-step calc; the 25-line `mul_sq_div_three_le_sum_max_of_pos_aux`)

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.min_le_sum_max`

Verdict: BORDERLINE-needs-human

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): only the project source (clean.tex §5, l.893–910) states the bound; no other source isolates it.
- Generality analysis (Phase 4): MAXIMALLY GENERAL up to the cosmetic `rp : ℕ` to `r : ℝ` widening (compiled); already strictly more general than the source (no θ r_p > 10).
- Mathlib search (Phase 5): not in mathlib; only the generic building blocks (`Finset.sum_range_id_mul_two`, `Nat.floor_le`).
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:** This is a fixed-constant numeric estimate (constants 1/2 and 1/3) shaped for the index bound in Roth's Lemma 6. It names no concept, has no literature standing, and nothing outside this development would call it, so neither YES bucket applies: there is no mathlib gap it fills. It is not a ≤3-call composition and mathlib does not have it, so neither NO bucket applies under the strict gates. The judgment is "keep project-local", consistent with the analogous `Roth.sum_inv_lt` (BORDERLINE). Its three private helpers (#203–#205) were assessed SKIP (private); the sibling report for `mul_sq_div_three_le_sum_max_aux` recommends inlining that helper into this lemma.

Numbered questions:
1. Do you agree this lemma should stay project-local and not be proposed to mathlib? (Recommended: yes.)
2. Should `rp : ℕ` be widened to `r : ℝ` (identical proof, compiled; caller l.586 passes `(r := (r none : ℝ))`)? (Recommended: optional, low value.)
3. Should the docstring's first sentence ("If `θ r_p > 10`, then …") be reworded, since the Lean statement has no hypotheses? (Recommended: yes.)

Next action: user answers the questions. With the recommended answers the lemma stays in Roth/Theta.lean, used once at l.586, with a docstring fix.

---

### Next step

Keep `Roth.min_le_sum_max` in Roth/Theta.lean as a project lemma; no mathlib PR. Reword its docstring's opening clause (drop "If `θ r_p > 10`"; keep the source citation). Optionally widen `rp : ℕ` to `r : ℝ` per evidence/Roth.min_le_sum_max/generalise_real_r.lean and inline `mul_sq_div_three_le_sum_max_aux` per its own report.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.min_le_sum_max/generalise_real_r.lean` (`import Roth.Theta`; copies the three private helpers verbatim under namespace `RothEvidence`, proves `min_le_sum_max_real` with `r : ℝ` using the project proof verbatim, derives the project's ℕ statement from it as a bare term, and re-checks `Roth.min_le_sum_max l` against the same statement). `lake env lean` on it: compiles with no errors or warnings (about 38 s). The first draft copied `mul_sq_div_three_le_sum_max_aux` as `private`; it was made non-private before the single compile run.
- Searches: WebSearch ×3, Lean-Finder ×1, LeanSearch ×1, Loogle ×1, mathlib grep ×2, local grep of clean.tex (all recorded above). ChatGPT MCP: n/a (not configured in this session). `lean_local_search`: n/a (ripgrep missing on PATH).
- `grep -rn min_le_sum_max Roth/`: definition l.362, single use l.586.
