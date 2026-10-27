---
decl: Roth.card_filter_weight_le
file: Roth/Lattice.lean
line: 202
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: MODERATE
junk: KEEP
rationale: Roth's Lemma 8 (lattice count estimate) - a classical but purely internal step of Roth's theorem with no standing outside proofs of Roth-type theorems; mathlib has neither it nor Roth's Diophantine theorem, it is not composable, all hypotheses are needed (hr counterexample compiled), and its statement is phrased via the project-local box and weight that are slated for REPLACE, so upstreaming only makes sense as part of a Roth-theorem contribution.
action: Keep in Roth/Lattice.lean (sole external caller Roth.mul_card_filter_weight_le_aux, Roth/MainLemma.lean:574); if Roth's theorem is ever upstreamed, restate it over Finset.Iic and Finsupp.weight (after the box/weight REPLACE refactor) and ship it with card_filter_box_last and sum_inv_lt in a Roth-specific file under Mathlib/NumberTheory/Diophantine/.
---

# Roth.card_filter_weight_le

## Inventory entry

### `theorem Roth.card_filter_weight_le`
- **Type**: `∀ (m : ℕ) (r : Fin m → ℕ), (∀ j, 0 < r j) → ∀ {lam : ℝ}, 0 < lam → (((box r).filter fun d ↦ weight r d ≤ ((m : ℝ) - lam) / 2).card : ℝ) ≤ 2 * √(m : ℝ) / lam * ∏ j, ((r j : ℝ) + 1)`
- **What**: Lemma 8 of the source (clean.tex §6, `roth:lem8`): for positive integers `r_1, …, r_m` and `λ > 0`, the number of multi-indices `0 ≤ j_i ≤ r_i` with `∑ j_i / r_i ≤ (m - λ)/2` is at most `2 √m λ⁻¹ ∏ (r_i + 1)`.
- **How**: Induction on `m` generalising `λ`. Case `m = 0`: the filter is empty by `Roth.filter_weight_le_eq_empty` (since `0 < λ`). Case `n + 1`: if `λ ≤ 2√(n+1)` use `Roth.card_filter_weight_le_of_le_sqrt_aux` (trivial bound by `card_box`); if `n = 0` and `λ > 2` the filter is again empty (`Roth.filter_weight_le_eq_empty`); otherwise the inductive step `Roth.card_filter_weight_le_succ_aux` (fibre count `Roth.card_filter_box_last`, re-thresholding `Roth.card_filter_fiber_eq`, and the numeric estimate `Roth.sum_inv_lt`). Mathlib lemmas named directly: `Nat.eq_zero_or_pos`, `lt_of_not_ge`, `Finset.card_empty`.
- **Hypotheses**: `hr : ∀ j, 0 < r j` (necessary - compiled counterexample with `r = 0`); `hlam : 0 < lam` (necessary - at `λ = 0` the Lean RHS is `0` while the count of the zero index is positive). `m = 0` is allowed (the source requires `m ≥ 1`), so the Lean form is marginally more general than the source.
- **Uses from project**: `Roth.box`, `Roth.weight`, `Roth.filter_weight_le_eq_empty` (private), `Roth.card_filter_weight_le_of_le_sqrt_aux` (private), `Roth.card_filter_weight_le_succ_aux` (private; which in turn uses `Roth.card_filter_box_last`, `Roth.card_filter_fiber_eq`, `Roth.sum_inv_lt`).
- **Used by**: `Roth.mul_card_filter_weight_le_aux` (private, Roth/MainLemma.lean:574). `grep -rn card_filter_weight_le Roth/` shows no other caller of this exact name (other hits are the `_aux` helpers in Roth/Lattice.lean).
- **Visibility**: public
- **Lines**: 197–220 (docstring 197–201, statement 202–204, proof 205–220), proof length 16 lines
- **Notes**: This is the source's Lemma 8, a named lemma of the paper and of Roth's original 1955 proof. Its statement inherits `Roth.box` and `Roth.weight`, which earlier reports classify `NO-mathlib-has-it`/`REPLACE` (`Finset.Iic` and `Finsupp.weight`).

## Junk check (Step 8)
- Used anywhere? Yes: once, in `Roth.mul_card_filter_weight_le_aux` (Roth/MainLemma.lean:574), which feeds the main lemma.
- Wrapper of 1–2 mathlib calls? No. It is a 16-line induction over four project helpers.
- Does mathlib have it? No (Phase 5 below; mathlib has no Diophantine Roth theorem at all, only the additive-combinatorics Roth theorems under `Mathlib/Combinatorics/Additive/`).
- Too specific (inline?)? No. It is a named lemma of the source and the public interface between Roth/Lattice.lean and Roth/MainLemma.lean.
- Well-chosen statement? Yes. It matches the source verbatim (with the harmless extension to `m = 0`), and all hypotheses are necessary.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; the name does not end in `_aux`; the docstring starts with "**Lemma 8**", not internal/auxiliary; Step 8 said KEEP; a namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `card_filter_weight_le` finds nothing. Not a glue lemma. The full workflow follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per the brief; the evidence file importing `Roth.Lattice` elaborates without diagnostics)
- decl `Roth.card_filter_weight_le`: ✓ resolved at Roth/Lattice.lean:202
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the lattice count estimate (Lemma 8): few multi-indices `j ≤ r` have `∑ j_i/r_i ≤ (m-λ)/2`.

### Statement (Phase 1)

`Roth.card_filter_weight_le` is a theorem stating the following. Let `r_1, …, r_m` be positive integers and `λ > 0`. Among the `∏ (r_i + 1)` lattice points `j` of the box `0 ≤ j_i ≤ r_i`, those whose normalised coordinate sum `∑ j_i/r_i` lies at least `λ/2` below its mean `m/2` number at most `2√m/λ · ∏ (r_i + 1)`. Probabilistically: if `X_i` is uniform on `{0, 1/r_i, …, 1}`, then `P(∑ X_i ≤ m/2 - λ/2) ≤ 2√m/λ`, a weak (Markov/Chebyshev-type) lower-tail bound.

Variables / typeclasses involved (Lean side):
- `m : ℕ`: the number of coordinates
- `r : Fin m → ℕ`: the box side lengths `r_i`
- `lam : ℝ`: the deviation parameter λ

Hypotheses (Lean side):
- `hr : ∀ j, 0 < r j`: the source's "positive integers"
- `hlam : 0 < lam`: the source's "λ > 0"

Conclusion (math): `#{j ∈ ∏[0, r_i] : ∑ j_i/r_i ≤ (m - λ)/2} ≤ 2 m^{1/2} λ⁻¹ ∏ (r_i + 1)`.

Conclusion (Lean): `(((box r).filter fun d ↦ weight r d ≤ ((m : ℝ) - lam) / 2).card : ℝ) ≤ 2 * √(m : ℝ) / lam * ∏ j, ((r j : ℝ) + 1)`

### Size classification (Phase 2a)

Verdict: BIG
Reason: it is a named lemma of the source paper (Lemma 8, `roth:lem8`) and of Roth's original proof, and the main result of Roth/Lattice.lean; however it is not a main result of the whole project (that is Roth's theorem).

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 16
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | `Roth theorem lemma number of lattice points j_1/r_1 + ... + j_m/r_m ≤ (m-λ)/2 bound 2 m^{1/2} λ^{-1}` | yes | arXiv math/0307203 (quantitative Roth–Ridout), Lemma 2.5: weighted generalisation `a_0 i_0/r_0 + a_1(∑ i_j/r_j) < κ/2 (m-λ)` with bound `2 m^{1/2} λ'^{-1} ∏(r_j+1)`, described as a modification of Lemma 8 of Roth's 1955 paper | confirms this is Roth's own Lemma 8; the only generalisation in the literature is a weighted variant tailored to Roth–Ridout |
| 2 | WebSearch (general form) | `concentration of measure uniform distribution on box sum of independent uniform variables lower tail Chebyshev bound count lattice points simplex` | partial | general lower-tail bounds for sums of independent uniforms (Chebyshev, Hoeffding, sharp Gaussian domination arXiv 2305.06235) | the conceptual general form is a tail bound for sums of independent discrete uniforms; Hoeffding gives the far stronger `exp(-λ²/(2m))` bound; no source states the `2√m/λ` lattice form outside Roth proofs |
| 3 | WebSearch (named-after / aliases) | `Cassels Diophantine approximation Roth's lemma index counting lemma "2 m^{1/2}" lattice points induction` | partial | Cassels' book and Schmidt LNM 785 are cited as standard textbook homes of Roth's proof; no standalone statement surfaced | standard expositions (Schmidt, Bombieri–Gubler) instead use a Chernoff/law-of-large-numbers count with `exp`-type bounds |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP is not configured in this session (no such tool among the available/deferred tools) |
| 5 | Local references | `grep -n "lem8" .mathlib-quality/references/clean.tex` | yes | clean.tex l.1050–1060: Lemma 8, "If m≥1, r_1,…,r_m are positive integers and λ>0, then the number … does not exceed 2 m^{1/2} λ^{-1} (r_1+1)⋯(r_m+1)" | Lean statement matches verbatim (Lean also allows m = 0); proof structure (induction, trivial case λ ≤ 2√m, fibre over j_m) matches l.1061–1100 |
| 6 | nLab | "Roth's theorem" / "lattice point count" | no | none | nLab has no entry on Diophantine approximation lemmas of this kind |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | covered by queries #2 and #3 (general web search spans these sites) | no | none | no thread isolates this lemma |
| 10 | recent arXiv (last 5 years) | covered by query #1 (arXiv 2502.00731 "Diophantine approximation and the subspace theorem" surfaced) | partial | modern expositions treat the count via concentration bounds | no new standard form |

### Literature summary (Phase 3)

Concept identified as: Roth's lattice-count lemma (Lemma 8 of Roth 1955), a weak lower-tail estimate for the normalised coordinate sum of a uniformly random lattice point of a box.
Sources agree on the standard form: yes for Roth-style proofs (Roth, Cassels, clean.tex); later expositions replace it by Chernoff/Hoeffding-type counts with exponential bounds, and Roth–Ridout uses a weighted variant.
Most general standard form: a tail bound `P(|∑ X_i - m/2| ≥ λ/2) ≤ …` for independent uniform variables on `{0, 1/r_i, …, 1}`; the strongest standard form is Hoeffding's inequality.
Generality dimensions where the literature varies:
  - bound shape: `2√m/λ` (Roth, this file) vs exponential `exp(-λ²/(2m))` (Hoeffding/Chernoff in modern expositions)
  - weights: unweighted (Roth) vs weighted coordinates (Roth–Ridout Lemma 2.5)
Disagreement with the literature: none; the Lean form is the source's Lemma 8.

### Generality analysis — `Roth.card_filter_weight_le`

Literature-standard form (from Phase 3): Roth's Lemma 8 as stated; the conceptual generalisation is a probabilistic tail bound.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hr : ∀ j, 0 < r j` | positive sides | positive integers | NO | compiled counterexample (`m = 9`, `r = 0`, `λ = 7`): count `1` > bound `6/7` |
| 2 | `hlam : 0 < lam` | strict | λ > 0 | NO | at `λ ≤ 0` the RHS is `≤ 0` (Lean's `x/0 = 0` at `λ = 0`) while the zero multi-index is counted |
| 3 | `m : ℕ`, index `Fin m` | `Fin m` | `m ≥ 1` | already more general | Lean allows `m = 0`; a general `Fintype σ` index would be cosmetic (the induction needs `Fin` and could be transported) |
| 4 | the `2√m/λ` bound | Roth's constant | Hoeffding gives `exp(-λ²/(2m))` | different theorem | a stronger bound is a different result, not a weakening of this one |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (for Roth's Lemma 8; both hypotheses verified necessary, `hr` by compiled counterexample)
Number of weakening opportunities found: 0 (a `Fintype σ` index is cosmetic and not pursued)
Proposed restatement: none at the level of hypotheses; see 4c for the idiomatic restatement over mathlib's `Finset.Iic`/`Finsupp.weight`.
Cost of restatement: MODERATE (follows the box/weight REPLACE refactor)

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | typeclasses instead of bundled hypotheses | no | numeric count statement | n/a |
| 2 | filters instead of sequences | no | finite count, no limits | n/a |
| 3 | universal property | no | no construction | n/a |
| 4 | bundled substructure | yes (mild) | state over `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` and `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)` instead of `Roth.box`/`Roth.weight` | interval API (`Finsupp.card_Iic`, `Finset.mem_Iic`) and `AddMonoidHom` API of `Finsupp.weight` |
| 5 | weaken field-specific typeclasses | no | needs `√` over ℝ | n/a |
| 6 | higher-categorical | no | n/a | n/a |
| 7 | concrete index generalised | no | `Fin m` is needed for the induction; a `Fintype σ` version is a transport | n/a |
| 8 | concrete-via-abstract | partly | the abstract content is a tail bound for sums of independent uniforms (probability), but mathlib's route there would be Hoeffding, a different and stronger theorem; the Roth constant is specific | none |
| 9 | false-generalisation guard | no | the row-4 restatement is the same mathematical object (earlier reports verified `box = Iic`, `weight = Finsupp.weight`) | n/a |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes (mild, inherited)
- Proposed mathlib-idiomatic restatement: `((Finset.Iic (Finsupp.equivFunOnFinite.symm r)).filter fun d ↦ Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) d ≤ ((m : ℝ) - lam) / 2).card ≤ 2 * √m / lam * ∏ j, ((r j : ℝ) + 1)`
- Cost: MODERATE (comes for free once the project's box/weight REPLACE refactor is done)
- Mathlib downstream this enables: interval and `Finsupp.weight` API instead of project definitions
- Real mathematical improvement: it removes two project-local definitions from the statement; it does not change the content.

### Proof strategy — `Roth.card_filter_weight_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | n/a | n/a |
| 2 | elements vs ideals | no | n/a | n/a |
| 3 | sequences vs nets | no | n/a | n/a |
| 4 | construction vs universal property | no | n/a | n/a |
| 5 | missing mathlib helpers | yes (mild) | a fibrewise count of a filtered `piFinset` over the last coordinate (`Fin.snoc`), proposed in the `Roth.card_filter_box_last` report | see that report (BORDERLINE) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (induction exactly following the source; the case split into private helpers keeps each step small)
- An alternative proof via Chebyshev (variance `∑ Var X_i ≤ m/4`, giving `P ≤ m/λ²`) needs a measure-theoretic bridge from box counts to independent uniforms that mathlib lacks; not recommended over the elementary induction.

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.card_filter_weight_le`

[A] Lean-Finder       "number of points in a box of integer vectors with weighted sum at most a threshold is bounded by a fraction of the box size"   no relevant hits (Behrend box lemmas, ZLattice sums, BoxIntegral prepartition counts)
[B] Loogle            `(Finset.filter _ (Fintype.piFinset _)).card, Real.sqrt`   no hits
[C] LeanSearch        "card of filter of Finset.Iic with sum of coordinates divided by bounds at most (m - lambda)/2"   no hits (only `Finset.card_filter_le`)
[D] Grep mathlib src  `card_filter_weight_le` (no hit); `Roth` (only additive-combinatorics files `Combinatorics/Additive/Corner/Roth.lean`, `AP/Three/*`; no Diophantine Roth theorem; `NumberTheory/Transcendental/Liouville/` has only Liouville-type results)
[E] Name pattern      `Roth.card_filter_weight_le` has no mathlib counterpart

Searched for both the user's form and the general form (tail bounds for sums of independent uniform variables / Hoeffding over finite boxes): mathlib has probabilistic Hoeffding-type machinery in `Mathlib/Probability/Moments/SubGaussian.lean`, but no counting statement over lattice boxes and nothing that yields Roth's constant directly.

Concluded: not in mathlib (all 5 methods exhausted, plus the general form).

### Normal-form check — `Roth.card_filter_weight_le`

Equivalent formalisms this statement could take: (a) count over `Roth.box` with `Roth.weight` (current); (b) count over `Finset.Iic` with `Finsupp.weight`; (c) count over `Fintype.piFinset (fun i ↦ range (r i + 1))` of functions `Fin m → ℕ`; (d) probability statement for a uniform measure on the box.
Does mathlib already have a canonical form for this idea? no (no statement of this kind exists); for the ambient objects, `Finset.Iic` and `Finsupp.weight` are canonical.
Name the canonical form we'd propose: (b) or (c).
RHS convention respected? n/a (an inequality, not a simp lemma)

### Syntactic generality — `Roth.card_filter_weight_le`

Alternative restatements attempted:
- (b) `Finset.Iic`/`Finsupp.weight` form
- (c) `piFinset` form on `Fin m → ℕ`
- natural-number count form `card ≤ ⌊…⌋` (rejected; the bound is real)

Chosen restatement: the current form for the project (its caller `Roth.mul_card_filter_weight_le_aux` works with `box`/`weight` directly); (b) if upstreamed.
Justification: the sole caller and the rest of Roth/MainLemma.lean are phrased with `box`/`weight`.

### Superfluous-argument audit — `Roth.card_filter_weight_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hr : ∀ j, 0 < r j` | yes | compiled counterexample in evidence |
| 2 | `hlam : 0 < lam` | yes | λ = 0 makes the Lean RHS 0 |
| 3 | `classical` inside the proof | n/a | only for decidability of the filter predicate |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR if upstreamed (state over `Finset.Iic`/`Finsupp.weight`); OK for the project
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (project); RESTATE-BEFORE-SHIP (mathlib, form (b))

### Call sites — `Roth.card_filter_weight_le`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:574 | `(card_filter_weight_le m r hr (by positivity)) ha.le).trans_eq ?_` in private `Roth.mul_card_filter_weight_le_aux` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.card_filter_weight_le`?):
  - (none) — `grep -rn "weight r d ≤" Roth/` shows only Lattice.lean helpers and the MainLemma caller.

### Composition check (Phase 6)

Can `Roth.card_filter_weight_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Finset.card_filter_le` + `card_box` (the trivial bound). Covers only the case `λ ≤ 2√m` (this is `Roth.card_filter_weight_le_of_le_sqrt_aux`).
  - Mathlib decls used: `Finset.card_filter_le`, `le_mul_of_one_le_left`
  - Result: partial
Attempt 2: a probabilistic tail bound (Chebyshev/Hoeffding over the uniform measure on the box). Mathlib has no bridge from box counts to sums of independent uniforms; building it (and combining with the trivial bound for small λ) is a multi-step proof, not a composition.
  - Result: fails (real proof needed)

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.card_filter_weight_le`

Verdict: BORDERLINE-needs-human

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): this is Roth's Lemma 8 (clean.tex l.1050; arXiv math/0307203 Lemma 2.5 calls its weighted variant a modification of Roth's Lemma 8); it lives only inside proofs of Roth-type theorems; modern expositions replace it with Hoeffding/Chernoff counts.
- Generality analysis (Phase 4): MAXIMALLY GENERAL; `hr` verified necessary by a compiled counterexample, `hlam` trivially necessary.
- Mathlib search (Phase 5): not in mathlib; mathlib has no Diophantine Roth theorem to host it.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:** The lemma is a genuine, literature-named result, correctly stated at maximal generality, not in mathlib and not composable from mathlib. Those facts would point to YES-add-as-is, but there is no mathlib gap it fills on its own: nothing in mathlib needs a `2√m/λ` lattice-count bound, the conceptual general form (a lower-tail bound for sums of independent uniforms) is better served in mathlib by Hoeffding-type results, and the lemma only earns its place as a step towards Roth's theorem, which is not in mathlib. Its statement is also phrased with `Roth.box` and `Roth.weight`, both assessed `NO-mathlib-has-it`/`REPLACE` (mathlib's `Finset.Iic` and `Finsupp.weight`), so any upstream form must be restated first. Whether to upstream therefore depends on a project-policy decision (is Roth's theorem headed for mathlib?), which the skill cannot make; hence BORDERLINE, with the recommended answer "keep project-local for now".

Numbered questions:
1. Is Roth's theorem (this project) intended to be upstreamed to mathlib as a whole? If no (recommended assumption), keep this lemma project-local.
2. If yes, should Lemma 8 be shipped in the same PR series as its helpers `Roth.card_filter_box_last` (BORDERLINE, general `piFinset`/`Fin.snoc` form available) and `Roth.sum_inv_lt` (BORDERLINE), in a Roth-specific file under `Mathlib/NumberTheory/Diophantine/`?
3. Should the statement be moved to mathlib's `Finset.Iic`/`Finsupp.weight` vocabulary as part of the box/weight REPLACE refactor, even if it stays in the project? (Recommended: yes, together with that refactor.)
4. Would you prefer to replace Roth's constant by a Hoeffding-type exponential count (as in modern expositions) if Roth's theorem were upstreamed? (Recommended: no; keep the source's Lemma 8.)

Next action: user answers the questions. With the recommended answers the lemma stays in Roth/Lattice.lean; its single caller `Roth.mul_card_filter_weight_le_aux` (Roth/MainLemma.lean:574) is unaffected; the statement is migrated to `Finset.Iic`/`Finsupp.weight` only when the box/weight refactor is done.

---

### Next step

Keep `Roth.card_filter_weight_le` in Roth/Lattice.lean as the project's Lemma 8; no standalone mathlib PR. Revisit only if Roth's theorem is upstreamed, then restate over `Finset.Iic`/`Finsupp.weight` and ship with `Roth.card_filter_box_last` and `Roth.sum_inv_lt`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.card_filter_weight_le/hypotheses.lean` (imports `Roth.Lattice`), checked with `lean_diagnostic_messages`: clean on first run (no errors, no warnings). It proves that the statement with `hr` dropped is false, via `m = 9`, `r = 0`, `λ = 7`: the filtered box is the whole box `{0}` (count `1`) while the bound is `2·3/7 < 1`.
- Searches: WebSearch ×3, Lean-Finder ×1, LeanSearch ×1, Loogle ×1, mathlib grep ×2, local grep of clean.tex (recorded above). ChatGPT MCP: n/a (not configured in this session).
- `grep -rn card_filter_weight_le Roth/`: declaration at Roth/Lattice.lean:202, sole external use Roth/MainLemma.lean:574.
- Earlier reports consulted: Roth.box.md, Roth.weight.md, Roth.sum_inv_lt.md, Roth.card_filter_box_last.md, Roth.card_filter_weight_le_succ_aux.md.
