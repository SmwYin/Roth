---
decl: Roth.sum_inv_lt
file: Roth/Lattice.lean
line: 68
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: The auxiliary numeric inequality from the proof of Lemma 8 (sum over j of (λ-1+2j/r)⁻¹ < λ⁻¹√(m/(m-1))(r+1)); it has no standing in the literature and no counterpart in mathlib, and composing it needs two project lemmas plus field_simp arithmetic, so neither a YES bucket nor a NO bucket fits cleanly; recommended resolution is to keep it in the project.
action: Keep in Roth/Lattice.lean as a project lemma, not for mathlib; optionally make it private since its only caller is the private Roth.card_filter_weight_le_succ_aux (Roth/Lattice.lean:173); both hypotheses hr and hm are necessary (counterexamples compiled in evidence/Roth.sum_inv_lt/hypotheses.lean).
---

# Roth.sum_inv_lt

## Inventory entry

### `theorem Roth.sum_inv_lt`
- **Type**: `∀ {r m : ℕ}, 1 ≤ r → 2 ≤ m → ∀ {lam : ℝ}, 2 * √(m : ℝ) < lam → ∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ < lam⁻¹ * (√((m : ℝ) - 1))⁻¹ * √(m : ℝ) * (r + 1)`
- **What**: For integers `r ≥ 1` and `m ≥ 2` and a real `λ > 2√m`, `∑_{j=0}^r (λ - 1 + 2j/r)⁻¹ < λ⁻¹ (m-1)^{-1/2} m^{1/2} (r+1)`. This is the "statement to finish the proof" in clean.tex §6, proof of Lemma 8 (l.1100–1103).
- **How**: A three-step `calc`. Step 1 is the private pairing bound `Roth.sum_inv_le` (sum ≤ `(r+1) λ/(λ²-1)`). Step 2 rewrites `λ/(λ²-1) = λ⁻¹/(1-λ⁻²)` and uses `gcongr` with side goal `Roth.sqrt_one_sub_inv_lt` (`√(1-1/m) < 1-λ⁻²`). Step 3 turns `√(1-1/m)` into `√(m-1)/√m` with `Real.sqrt_div'`, then closes with `field_simp`. The setup uses `Real.lt_sqrt_of_sq_lt` (to get `2 < λ`) and `Real.sqrt_pos`, `div_lt_one`.
- **Hypotheses**: `hr : 1 ≤ r` (necessary; for `r = 0` the statement fails, see the compiled counterexample); `hm : 2 ≤ m` (necessary; for `m = 1` the RHS is `0`); `hlam : 2 * √m < lam` (the source's hypothesis, essential).
- **Uses from project**: `Roth.sum_inv_le` (private, Roth/Lattice.lean:47), `Roth.sqrt_one_sub_inv_lt` (Roth/Lattice.lean:29).
- **Used by**: `Roth.card_filter_weight_le_succ_aux` (private, Roth/Lattice.lean:173). `grep -rn sum_inv_lt Roth/` gives only l.68 and l.173.
- **Visibility**: public
- **Lines**: 63–90 (docstring 63–67, statement 68–70, proof 71–90), proof length 20 lines
- **Notes**: Its only caller is private and in the same file, so the declaration could be private too. The `(√(m-1))⁻¹ * √m` form copies the source's `(m-1)^{-1/2} m^{1/2}` word for word; the caller immediately normalises it with `push_cast`.

## Junk check (Step 8)
- Used anywhere? Yes, once (`Roth.card_filter_weight_le_succ_aux`, l.173), the induction step of Lemma 8.
- Wrapper of 1–2 mathlib calls? No. It chains two project lemmas with a `gcongr` step and two `field_simp` normalisations.
- Does mathlib have it? No (Phase 5 below).
- Too specific (inline?)? It is specific to Lemma 8, but it is the separately stated auxiliary claim in the source ("To finish the proof of the lemma we prove the following statement"), so keeping it named mirrors the paper and keeps the 30-line induction step readable. Inlining is not recommended.
- Well-chosen statement? Yes for the project. It matches the source verbatim and both natural-number hypotheses are necessary (compiled).
- Conclusion: `KEEP` (project-local; optionally make it `private`).

## Mathlibable assessment (Step 9)

Pre-filter: public; the name does not end in `_aux`; the docstring does not start with internal/auxiliary; Step 8 said KEEP; a namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `sum_inv_lt` finds nothing. Not a glue lemma (20-line proof). The full workflow follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (the project is built per the brief; the evidence file importing `Roth.Lattice` elaborates cleanly)
- decl `Roth.sum_inv_lt`:    ✓ resolved at Roth/Lattice.lean:68
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the lattice count estimate (Lemma 8): few multi-indices `j ≤ r` with `∑ j_i/r_i ≤ (m-λ)/2`.

### Statement (Phase 1)

`Roth.sum_inv_lt` is a theorem stating the following. Let `r ≥ 1` and `m ≥ 2` be integers and `λ > 2√m` real. Then the sum of the reciprocals of the `r+1` equally spaced points `λ - 1, λ - 1 + 2/r, …, λ + 1` is less than `(r+1)/λ · √(m/(m-1))`. The proof pairs the terms `j` and `r-j` (whose arguments average to `λ`), giving `(r+1) λ/(λ²-1)`. It then compares `1 - λ⁻² > 1 - 1/(4m) > √(1-1/m)`.

Variables / typeclasses involved (Lean side):
- `r : ℕ`: the exponent `r_m` of the last variable in Lemma 8's induction
- `m : ℕ`: the number of variables (cast to ℝ)
- `lam : ℝ`: Lemma 8's parameter λ

Hypotheses (Lean side):
- `hr : 1 ≤ r`: the source's "r ≥ 1"; needed for the spacing `2/r`
- `hm : 2 ≤ m`: the source's "m ≥ 2"; makes `(m-1)^{-1/2}` finite
- `hlam : 2 * √m < lam`: the source's "λ > 2√m"

Conclusion (math): `∑_{j=0}^r (λ - 1 + 2j/r)⁻¹ < λ⁻¹ (m-1)^{-1/2} m^{1/2} (r+1)`.

Conclusion (Lean): `∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ < lam⁻¹ * (√((m : ℝ) - 1))⁻¹ * √(m : ℝ) * (r + 1)`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an auxiliary numeric inequality inside the proof of Lemma 8. It is not a structure and not a main result, and it carries no person's name.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 20
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | `"sum_{j=0}^r" "(\lambda - 1 + 2j/r)^{-1}" Roth lemma index estimate` | no | none | results: Roth over function fields (arXiv 1806.10737), quantitative Roth–Ridout (arXiv math/0307203) with a related counting lemma, Evertse's Luminy slides; none states this sum bound |
| 2 | WebSearch (general form) | `sum of reciprocals arithmetic progression symmetric pairing bound convexity 1/(a-x)+1/(a+x) inequality` | partial | only the identity `1/(a-x)+1/(a+x) = 2a/(a²-x²)` (folklore algebra) | the hits are about integrality of reciprocal sums of arithmetic progressions (Erdős–Niven, arXiv 1311.1389), not upper bounds |
| 3 | WebSearch (named-after / aliases) | `Roth's theorem proof index lemma number of lattice points sum j_i/r_i lambda 2 sqrt m Cassels Schmidt` | partial | the lattice-count lemma exists in several forms (Cassels, Schmidt LNM 785, Bombieri–Gubler) | this numeric step is an internal computation of that lemma's proof, never stated on its own |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP is not configured in this session (no such tool among the deferred tools) |
| 5 | Local references | `grep -n "lem8\|2j/r" .mathlib-quality/references/clean.tex` | yes | clean.tex §6, l.1100–1103: "Let r ≥ 1 and m ≥ 2 be integers and suppose λ > 2√m. Then …" | the Lean statement matches the source word for word; the source proof splits into r even/odd cases, which the Lean proof merges via `sum_range_reflect` pairing |
| 6 | nLab | "harmonic sum inequality" / "arithmetic progression reciprocal" | n/a | none | nLab covers no elementary real inequalities of this kind; nothing to check beyond confirming the absence |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | covered by queries #2 and #3 (general web search spans these sites) | no | none | no thread states this bound; the convexity pairing is standard |
| 10 | recent arXiv (last 5 years) | covered by query #1 (arXiv hits on Roth's lemma) | no | none | no source isolates this inequality |

### Literature summary (Phase 3)

Concept identified as: an auxiliary estimate in the proof of Roth's lattice-count (index-counting) lemma. Its only standard ingredient is the pairing/convexity bound `1/(λ-x) + 1/(λ+x) ≤ 2λ/(λ²-1)` for `|x| ≤ 1`.
Sources agree on the standard form: n/a. Only the project's source states it.
Most general standard form: none. The general principle is "the mean of `1/t` over points symmetric about `λ` in `[λ-1, λ+1]` is at most `λ/(λ²-1)`", which no source isolates either.
Generality dimensions where the literature varies: none identified.
Disagreement with the literature: none (it matches clean.tex verbatim).

### Generality analysis — `Roth.sum_inv_lt`

Literature-standard form (from Phase 3): only the source statement exists.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hr : 1 ≤ r` | `r ≥ 1` | `r ≥ 1` | NO | counterexample at `r = 0`, `m = 2`, `λ = 3` compiled (LHS 1/2, RHS √2/3) |
| 2 | `hm : 2 ≤ m` | `m ≥ 2` | `m ≥ 2` | NO for ℕ | `m = 1` makes the RHS `0` (compiled counterexample); a real `m > 1` version would be a cosmetic change with no caller benefit |
| 3 | `hlam : 2√m < λ` | strict | strict | NO | gives `1-λ⁻² > √(1-1/m)`, which is essential |
| 4 | `m r : ℕ` vs `ℝ` | naturals | integers | cosmetic | `r` indexes the sum, so it must be a natural number; `m` could be real but nothing gains |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (for its hypotheses; both natural-number hypotheses are verified necessary)
Number of weakening opportunities found: 0 (only the cosmetic `m : ℝ`, not pursued)
Proposed restatement: none.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | typeclasses instead of bundled hypotheses | no | numeric inequality, no structure | n/a |
| 2 | filters instead of sequences | no | finite sum, no limits | n/a |
| 3 | universal property | no | no construction | n/a |
| 4 | bundled substructure | no | no sets | n/a |
| 5 | weaken field-specific typeclasses | no | needs `√`, so ℝ (it could live in a linear ordered field with `√` replaced by squares, but the source and caller use `√`) | n/a |
| 6 | higher-categorical | no | n/a | n/a |
| 7 | concrete index generalised | no | `range (r+1)` is the natural index | n/a |
| 8 | concrete-via-abstract | partly | the proof uses only the pairing lemma and a numeric comparison; the abstract content (`sum_inv_le`'s pairing) is itself project-specific | none in mathlib |
| 9 | false-generalisation guard | no | no generalisation proposed | n/a |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
- Reason: a fixed-constant numeric inequality over ℝ with no structure to abstract.

### Proof strategy — `Roth.sum_inv_lt`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | n/a | n/a |
| 2 | elements vs ideals | no | n/a | n/a |
| 3 | sequences vs nets | no | n/a | n/a |
| 4 | construction vs universal property | no | n/a | n/a |
| 5 | missing mathlib helpers | no | the pairing step uses `Finset.sum_range_reflect`; nothing missing | n/a |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (a `calc` through named helpers, `gcongr`, `field_simp`; it merges the source's even/odd case split into one reflection argument, which improves on the source)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.sum_inv_lt`

[A] Lean-Finder       "upper bound for sum_{j=0}^{r} 1/(a + b j) by (r+1) times reciprocal of midpoint"   no hits (only `sum_Ioc_inv_sq_le_sub`, `sum_Ioo_inv_sq_le`, FloorPow sums; unrelated)
[B] Loogle            `∑ _ ∈ Finset.range _, (_ + _ / _)⁻¹ < _`   no hits
[C] LeanSearch        "sum over range of inverse of affine function bounded by pairing terms j and r - j"   no hits (antidiagonal/finsum reindexing lemmas only)
[D] Grep mathlib src  `sum_inv_lt` (no hit); `sum_range_reflect` (building block, Mathlib/Algebra/BigOperators/Intervals.lean, used in GeomSum, TrapezoidalRule)
[E] Name pattern      lean_local_search not needed beyond [D]; the qualified name `Roth.sum_inv_lt` has no mathlib counterpart

Searched for both the user's form and the general pairing/convexity principle (Jensen for `1/t` on symmetric points): mathlib has general convexity (`ConvexOn`, Jensen via `ConvexOn.map_sum_le`) but no ready-made reciprocal-sum bound.

Concluded: not in mathlib (all 5 methods exhausted, plus the general form); building blocks: `Finset.sum_range_reflect`, `Finset.sum_le_sum`, `Real.sqrt_div'`, `Real.sqrt_lt'`.

### Normal-form check — `Roth.sum_inv_lt`

Equivalent formalisms this statement could take: `... < λ⁻¹ * √(m/(m-1)) * (r+1)`; `... < (r+1)/(λ √(1-1/m))`; the current `λ⁻¹ (√(m-1))⁻¹ √m (r+1)`.
Does mathlib already have a canonical form for this idea? no.
Name the canonical form we'd propose: none (not proposed for mathlib).
RHS convention respected? n/a (an inequality, not a simp lemma)

### Syntactic generality — `Roth.sum_inv_lt`

Alternative restatements attempted:
- RHS `λ⁻¹ * √(m/(m-1)) * (r+1)`
- RHS `(r+1) * (λ⁻¹ / √(1-1/m))` (the second calc line)

Chosen restatement: the current form.
Justification: it is the source's display word for word, and the single caller normalises it with one `push_cast`. None of the alternatives makes the call site shorter.

### Superfluous-argument audit — `Roth.sum_inv_lt`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hr : 1 ≤ r` | yes | `r = 0` counterexample compiled |
| 2 | `hm : 2 ≤ m` | yes | `m = 1` counterexample compiled |
| 3 | `hlam` | yes | essential |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.sum_inv_lt`

Internal use count: 1 (in the declaring file; 0 in other files)
External-to-file callers: 0

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Lattice.lean:173 | `have hs := sum_inv_lt (r := R) (m := n + 1) hr (Nat.succ_le_succ hn) hlam` in `Roth.card_filter_weight_le_succ_aux` |

Inline-derivation grep: `grep -rn "lam - 1 + 2 \* (j" Roth/` shows only `sum_inv_le` and `sum_inv_lt` themselves; there is no re-derivation elsewhere.

### Composition check (Phase 6)

Can `Roth.sum_inv_lt` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Finset.sum_le_sum` on the reflected sum + `Finset.sum_range_reflect` + `linarith`. This reproduces only the first calc step (`Roth.sum_inv_le`), and even that needs a per-term `nlinarith` inequality (`Roth.inv_add_inv_le`).
  - Mathlib decls used: `Finset.sum_le_sum`, `Finset.sum_range_reflect`, `Finset.sum_add_distrib`
  - Result: fails (the per-term pairing bound and the √ comparison are real proofs)
Attempt 2: chain `Roth.sum_inv_le` and `Roth.sqrt_one_sub_inv_lt` (the current proof). This uses project lemmas plus `gcongr` and `field_simp`, which counts as a real proof by the 6b heuristic.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.sum_inv_lt`

Verdict: BORDERLINE-needs-human

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): no literature beyond the project's source (clean.tex §6 l.1100–1103) states this inequality. Its only standard ingredient is the folklore pairing `1/(λ-x)+1/(λ+x) = 2λ/(λ²-x²)`.
- Generality analysis (Phase 4): MAXIMALLY GENERAL for its hypotheses; both `hr` and `hm` are verified necessary by compiled counterexamples.
- Mathlib search (Phase 5): not in mathlib; only the generic building blocks (`Finset.sum_range_reflect`, `Real.sqrt_div'`) exist.
- Composition check (Phase 6): NOT-COMPOSABLE (it needs two project lemmas, one of them a per-term `nlinarith` bound).

**Rationale:** This is a fixed-constant numeric estimate (`λ - 1 + 2j/r`, `2√m`, `(m-1)^{-1/2} m^{1/2}`) shaped for Lemma 8 of the Roth formalisation. It names no concept and has no standing in the literature, and nothing outside this development would call it. So neither YES bucket applies: there is no mathlib gap it fills. It is also not composable from mathlib in ≤3 calls, and mathlib does not have it, so neither NO bucket applies under the strict gates. As with its sibling `Roth.sqrt_one_sub_inv_lt` (also BORDERLINE), the judgment is "keep project-local". The same reasoning applies to the private `Roth.sum_inv_le` and `Roth.inv_add_inv_le` it depends on, which were assessed SKIP.

Numbered questions:
1. Do you agree this lemma should stay project-local and not be proposed to mathlib? (Recommended: yes.)
2. Should it be made `private`, since its only caller `Roth.card_filter_weight_le_succ_aux` (l.173) is private and in the same file? (Recommended: optional. Keeping it public documents the source's displayed auxiliary statement.)
3. Should the RHS stay in the source's `λ⁻¹ (√(m-1))⁻¹ √m (r+1)` form rather than a normalised `√(m/(m-1))` form? (Recommended: keep; it matches clean.tex.)

Next action: user answers the questions. With the recommended answers the lemma stays as is in Roth/Lattice.lean, used once at l.173.

---

### Next step

Keep `Roth.sum_inv_lt` in Roth/Lattice.lean as a project lemma; no mathlib PR. Optionally make it `private` (its single caller `Roth.card_filter_weight_le_succ_aux`, Roth/Lattice.lean:173, needs no change). No hypothesis can be dropped; see the evidence file.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.sum_inv_lt/hypotheses.lean` (imports `Roth.Lattice`), checked with `lean_diagnostic_messages`: clean, no errors or warnings. It contains a compiled counterexample for dropping `hm` (`m = 1`, `r = 1`, `λ = 3`: RHS is `0`), a compiled counterexample for dropping `hr` (`r = 0`, `m = 2`, `λ = 3`: `1/2 ≥ √2/3`), and the project statement re-checked. The first check failed only because of a superfluous `linarith` after `norm_num` (which had already closed the goal) and a misplaced module docstring; both were fixed.
- Searches: WebSearch ×3, Lean-Finder ×1, LeanSearch ×1, Loogle ×1, mathlib grep ×2, local grep of clean.tex (all recorded above). ChatGPT MCP: n/a (not configured in this session).
- `grep -rn sum_inv_lt Roth/` gives l.68 and l.173 only.
