---
decl: Roth.three_small_factors
file: Roth/MainLemma.lean
line: 180
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Source §6 display (three-small-factors) 2^(m r1), (1+A)^(m r1), (1+|alpha|)^(m r1) all below B_1^delta, stated about the project-only def mainCoeffBound (NO-composable, not upstreamable) under the Roth parameter hypothesis (32); every hypothesis sharp (compiled), no literature standing outside Roth proofs, not a 3-call mathlib composition (needs project sqrt_lt_floor, mul_log_div_two_lt_log_mainCoeffBound, two_lt_rpow_aux plus nlinarith); 3 callers in 2 files, so it is genuine project API but has no mathlib home.
action: Recommended - keep Roth.three_small_factors project-local in Roth/MainLemma.lean (callers MainLemma l.631, l.656 and Main l.502); no mathlib PR.
---

# Roth.three_small_factors

## Inventory entry

### `theorem Roth.three_small_factors`
- **Type**: `∀ {δ : ℝ}, 0 ≤ δ → ∀ {m q₁ r₁ : ℕ}, 0 < r₁ → ∀ {A α : ℝ}, 0 ≤ A → 2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log ↑q₁ → 2 ^ (m * r₁) < ↑(mainCoeffBound δ q₁ r₁) ^ δ ∧ (1 + A) ^ (m * r₁) < ↑(mainCoeffBound δ q₁ r₁) ^ δ ∧ (1 + |α|) ^ (m * r₁) < ↑(mainCoeffBound δ q₁ r₁) ^ δ`
- **What**: With `B₁ = ⌊q₁^{δ r₁}⌋` (`mainCoeffBound`), the non-strict form of the source's parameter condition (32), `2m + 1 + 2m log(1+A) + 2m log(1+|α|) ≤ δ² log q₁`, implies the three bounds `2^{m r₁} < B₁^δ`, `(1+A)^{m r₁} < B₁^δ`, `(1+|α|)^{m r₁} < B₁^δ` (source §6, eq. `roth:three-small-factors`, clean.tex l.1374).
- **How**: Nonnegativity of the two logs gives `1 ≤ δ² log q₁`; with `log 2 < 1` (`Real.log_lt_sub_one_of_pos`) the private `two_lt_rpow_aux` gives `X = q₁^{δ r₁} ≥ 2`, hence `δ > 0`. A local `key` lemma reduces `t^{m r₁} < B₁^δ` to `2 m log t ≤ δ² log q₁` via `Real.lt_rpow_of_log_lt`, positivity of `B₁` from `sqrt_lt_floor`, `Real.log_pow`, and `nlinarith` fed with `mul_log_div_two_lt_log_mainCoeffBound` (`log B₁ > ½ δ r₁ log q₁`). The three side conditions are closed by `nlinarith only` from `h32`.
- **Hypotheses**: `hδ0 : 0 ≤ δ`, `hr₁ : 0 < r₁`, `hA : 0 ≤ A`, `h32` (non-strict (32)). All four are necessary (evidence checks 1–3 for the first three; `h32` is the content).
- **Uses from project**: `Roth.mainCoeffBound`, `Roth.two_lt_rpow_aux` (private), `Roth.sqrt_lt_floor`, `Roth.mul_log_div_two_lt_log_mainCoeffBound`
- **Used by**: Roth/MainLemma.lean:631 (`exists_mem_RSet_le_index_of_log_bound_aux`, second conjunct with `α := 0`), Roth/MainLemma.lean:656 (`exists_auxiliary_polynomial_of_log_bound_aux`, first and third conjuncts), Roth/Main.lean:502 (first conjunct). No other uses.
- **Visibility**: public
- **Lines**: 171–212 (docstring 171–179, statement 180–184), proof length 28 lines
- **Notes**: none

## Junk check (Step 8)
- Used anywhere? Yes, 3 call sites in 2 files (MainLemma l.631, l.656; Main l.502).
- Wrapper of 1–2 mathlib calls? No: a 28-line estimate combining three project lemmas, `Real.lt_rpow_of_log_lt`, `Real.log_pow` and four `nlinarith` calls.
- Does mathlib have it? No (it mentions the project def `mainCoeffBound`; loogle / leansearch / Lean-Finder only return the reduction lemmas `Real.lt_rpow_of_log_lt`, `Real.pow_lt_iff_lt_log`).
- Too specific (inline?)? Specific to Roth's proof, but it is the source's named display and is used three times; inlining would triplicate the estimate. Keep.
- Well-chosen? Yes; a single conjunction destructured at each caller, matching the source's single display, with sharp hypotheses.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring starts "For positive"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `three_small_factors` / `namespace Roth`: no hit. Not a glue lemma, so a full run follows. Parent def `Roth.mainCoeffBound` is `NO-composable-from-mathlib`; the re-aim rule does not apply.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule; evidence file importing Roth.MainLemma elaborates cleanly via lean-lsp)
- decl `Roth.three_small_factors`: resolved at Roth/MainLemma.lean:180
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  §6 of the source: Roth's main lemma (Lemma 9) via pigeonhole over box polynomials with coefficients in [0, B_1]

### Statement (Phase 1)

`Roth.three_small_factors` is a theorem stating the following:

Let `δ ≥ 0`, `m, q₁` natural, `r₁ ≥ 1`, `A ≥ 0`, `α` real, and `B₁ = ⌊q₁^{δ r₁}⌋`. If `2m + 1 + 2m log(1+A) + 2m log(1+|α|) ≤ δ² log q₁`, then each of `2^{m r₁}`, `(1+A)^{m r₁}`, `(1+|α|)^{m r₁}` is strictly less than `B₁^δ`.

Variables / typeclasses involved (Lean side):
- `δ : ℝ`: Roth exponent parameter.
- `m q₁ r₁ : ℕ`: number of variables, first denominator, first degree.
- `A α : ℝ`: coefficient bound of the minimal polynomial and the algebraic number.

Hypotheses (Lean side):
- `hδ0 : 0 ≤ δ`, `hr₁ : 0 < r₁`, `hA : 0 ≤ A`: sign conditions.
- `h32`: the non-strict form of source condition (32).

Conclusion (math): the three bases raised to `m r₁` are below `B₁^δ`.

Conclusion (Lean): `2 ^ (m * r₁) < ↑(mainCoeffBound δ q₁ r₁) ^ δ ∧ (1 + A) ^ (m * r₁) < ↑(mainCoeffBound δ q₁ r₁) ^ δ ∧ (1 + |α|) ^ (m * r₁) < ↑(mainCoeffBound δ q₁ r₁) ^ δ`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a parameter estimate inside the proof of Roth's main lemma; not a main result, not named after anyone.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 28 substantive lines
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: check skipped (theorem).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof "2^{m r_1}" "B_1^\delta" coefficient bound Siegel lemma | partial | `B = ⌊q₁^{δ r₁}⌋` parameter bookkeeping | arXiv math/0307203 and arXiv 2502.00731 discuss the δ, r₁ choices; no standalone three-bound statement |
| 2 | WebSearch (general form) | if a^n < B^delta from n log a < delta log B elementary logarithm exponent comparison inequality | no | n/a | only the generic log-monotonicity equivalence, no named result |
| 3 | WebSearch (aliases) | Roth's lemma auxiliary polynomial height bound (1+A)^{m r} (1+abs alpha)^{m r} B^delta Davenport proof | no | n/a | surveys (arXiv 2502.00731, Evertse slides) state height bounds in other normalisations; this display not found |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | clean.tex l.1355–1384 | yes | display `roth:three-small-factors` plus Lean note | exact match; derived from `log B₁ > ½ δ r₁ log q₁` and (32) |
| 6 | nLab | Roth theorem / logarithm inequality | no | n/a | nLab has no elementary real-inequality content |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | real inequality, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 2–3) | no | n/a | elementary; no named result |
| 10 | recent arXiv | (covered by searches 1, 3) | no | n/a | Roth-type proofs state such bounds inline with their own constants |

### Literature summary (Phase 3)

Concept identified as: ad-hoc parameter estimate in the proof of Roth's main lemma; no standard name.
Sources agree on the standard form: n/a (only the project source states it, inline; other expositions normalise heights differently).
Most general standard form: `t^{m r₁} < B₁^δ` whenever `2 m log t ≤ δ² log q₁` and `log B₁ > ½ δ r₁ log q₁` (the proof's local `key`), applied to `t = 2, 1+A, 1+|α|`.
Generality dimensions where the literature varies:
  - the base `t`: any `t > 0` with `2m log t ≤ δ² log q₁`.
Disagreement with the literature: none.

### Generality analysis — `Roth.three_small_factors`

Literature-standard form (from Phase 3): the source display, conditional on (32).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hδ0 : 0 ≤ δ` | `0 ≤ δ` | `δ > 0` | no | needed: δ = −1, m = 0, q₁ = 3, r₁ = 1 satisfies h32 but B₁ = 0 and `1 < 0^{-1} = 0` fails (check 2) |
| 2 | `hr₁ : 0 < r₁` | `0 < r₁` | `r₁ ≥ 1` | no | needed: r₁ = 0 gives B₁ = 1, `1 < 1` fails (check 3) |
| 3 | `hA : 0 ≤ A` | `0 ≤ A` | `A ≥ 1` in source | no (already weaker than source) | needed: A = e^{−2} − 1 makes `log(1+A) = −2`, h32 holds with q₁ = 1, but `2 < 1` fails (check 1) |
| 4 | `h32` (non-strict) | `≤` | strict (32) | already weaker | non-strict suffices; it is the content |
| 5 | `α` arbitrary real | any | algebraic | already weaker | proof uses only `|α| ≥ 0` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (as a statement about `mainCoeffBound`; all three sign hypotheses shown necessary by compiled counterexamples)
Number of weakening opportunities found: 0
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | scalar hypotheses only | — |
| 2 | Sequences/metric vs filters? | no | no limits | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | `Real.log`/`Real.rpow` are ℝ-specific | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | — | — |
| 8 | Concrete-via-abstract? | partially | the local `key` is about an abstract `t > 0` and abstract `B` with `log B > ½ δ r₁ log q₁`; but `mainCoeffBound` is used essentially (via `sqrt_lt_floor` and `mul_log_div_two_lt_log_mainCoeffBound`) and an abstract-B form is just `Real.lt_rpow_of_log_lt` plus `nlinarith` | none in mathlib |
| 9 | False-generalisation guard | no false generalisation | — | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the only abstraction (the inner `key` with abstract base) is a one-call corollary of `Real.lt_rpow_of_log_lt`; there is no organisational gain for mathlib.

### Proof strategy — `Roth.three_small_factors`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | partial | `√X < ⌊X⌋₊` for `X ≥ 2` (project `sqrt_lt_floor`, BORDERLINE) | n/a (follow sqrt_lt_floor's decision) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (reduce to logs with `Real.lt_rpow_of_log_lt`, factor the common step as a local `key`, close linear-in-logs goals with `nlinarith only`).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.three_small_factors`

[A] Lean-Finder       "if 2 m log t ≤ δ² log q and log B > δ r log q / 2 then t^(m r) < B^δ"   no hits (Behrend bounds only)
[B] Loogle            `Real.log ?x < ?y * Real.log ?z → ?x < ?z ^ ?y`   `Real.lt_rpow_of_log_lt`, `Real.rpow_lt_of_lt_log` (building block)
[C] LeanSearch        "x ^ n < y ^ δ from n * log x < δ * log y real power comparison via logarithm"   `Real.pow_lt_iff_lt_log`, `Real.rpow_lt_iff_lt_log`, `Real.pow_lt_of_lt_log` (building blocks)
[D] Grep mathlib src  `three_small_factors`, `namespace Roth`   no hits
[E] Name pattern      `Roth.three_small_factors`   no mathlib decl (lean_local_search unavailable: ripgrep not installed; replaced by the grep in [D])

Searched for both:
  - the user's current form (about `mainCoeffBound`)
  - the abstract form (`t^{m r₁} < B^δ` from log bounds)

Concluded: found building blocks (`Real.lt_rpow_of_log_lt`, `Real.log_pow`, `Real.pow_lt_iff_lt_log`); neither form is in mathlib.

### Normal-form check — `Roth.three_small_factors`

Equivalent formalisms: three separate lemmas vs one conjunction; multiplicative vs logarithmic conclusion.
Does mathlib already have a canonical form? No. The conjunction matches the source's single display and callers destructure with `obtain`. OK. RHS convention: n/a (not an iff).

### Syntactic generality — `Roth.three_small_factors`

Alternative restatements attempted:
- current conjunction.
- three separate lemmas (one per base), each with only the hypotheses it needs.
- a single lemma about an arbitrary base `t` with `2m log t ≤ δ² log q₁` (the local `key`).

Chosen restatement: current; each caller passes the one hypothesis `h32` it already has (or a `simpa` of it) and takes the conjunct it needs.
Justification: the per-base form would make each caller derive its own side condition from (32).

### Superfluous-argument audit — `Roth.three_small_factors`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hδ0` | yes | check 2 |
| 2 | `hr₁` | yes | check 3 |
| 3 | `hA` | yes | check 1 |
| 4 | `h32` | yes | content |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (project-local).

### Call sites — `Roth.three_small_factors`

Internal use count: 1 outside the declaring file; 2 in the declaring file
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:631 | `obtain ⟨_, hTA, _⟩ := three_small_factors (m := m) (q₁ := q₁) (α := 0)` |
| Roth/MainLemma.lean:656 | `obtain ⟨h2, _, hα⟩ := three_small_factors hδ0 (Nat.pos_of_mul_pos_left <|` |
| Roth/Main.lean:502 | `exact hprodR.trans_lt (three_small_factors hδ0 hr0 hA h32).1` |

Inline-derivation grep (`Real.lt_rpow_of_log_lt` with `mainCoeffBound` across Roth/): (none besides this declaration).

### Composition check (Phase 6)

Can `Roth.three_small_factors` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Real.lt_rpow_of_log_lt hB (by rw [Real.log_pow]; nlinarith ...)` per conjunct.
  - Mathlib decls used: `Real.lt_rpow_of_log_lt`, `Real.log_pow`
  - Result: fails as a composition — needs positivity of `B₁` and `log B₁ > ½ δ r₁ log q₁` (project `sqrt_lt_floor`, `mul_log_div_two_lt_log_mainCoeffBound`), `X ≥ 2` (private `two_lt_rpow_aux`), and non-trivial `nlinarith` side conditions.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.three_small_factors`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): only the project source states it (clean.tex l.1374); no named result elsewhere.
- Generality analysis (Phase 4): MAXIMALLY GENERAL; every hypothesis shown necessary in compiled counterexamples.
- Mathlib search (Phase 5): building blocks only.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The statement is about `Roth.mainCoeffBound`, a project definition already judged not upstreamable, under the Roth-specific parameter condition (32); so this exact statement has no mathlib home. It is not composable from mathlib either (it rests on three project lemmas and four `nlinarith` steps), and it is real project API (3 callers in 2 files) with sharp hypotheses. Neither NO bucket fits, and a YES bucket has no gap to name: mathlib has no consumer for Roth-parameter estimates, and the only abstract core (`key`) is a one-call use of `Real.lt_rpow_of_log_lt`. The recommended answer is project-local.

Belongs-elsewhere: project-local, Roth/MainLemma.lean, encoding the source's display `roth:three-small-factors` for its three callers.

Numbered questions:
  1. Keep `Roth.three_small_factors` project-local with no mathlib PR (recommended: yes)?
  2. Split it into three per-base lemmas instead of one conjunction (recommended: no; callers destructure one conjunction and the source has one display)?
  3. Strengthen `hA : 0 ≤ A` to the source's `1 ≤ A` for fidelity (recommended: no; the weaker hypothesis is sharp and already sufficient)?

Next action: user answers; default is keep project-local with no change.

---

### Next step

Keep `Roth.three_small_factors` in Roth/MainLemma.lean (callers MainLemma l.631, l.656, Main l.502); no upstream PR.

## Evidence
- `grep -rn three_small_factors Roth/`: definition MainLemma l.180; uses MainLemma l.631, l.656, Main l.502.
- grep of `.lake/packages/mathlib/Mathlib/` for `three_small_factors`: no hits.
- lean_loogle, lean_leansearch, lean_leanfinder as recorded in Phase 5 (building blocks only). lean_local_search unavailable (ripgrep not installed).
- WebSearch x3 (Phase 3 rows 1–3): no standalone statement.
- clean.tex l.1355–1384: source statement and Lean note.
- Evidence file `.mathlib-quality/overview/evidence/Roth.three_small_factors/checks.lean` (checked with lean_diagnostic_messages: no errors or warnings, only the `#check` info): (1) dropping `hA`: A = e^{−2} − 1, δ = m = r₁ = q₁ = 1, α = 0 satisfies h32 but `2 < 1` fails; (2) dropping `hδ0`: δ = −1, m = 0, q₁ = 3, r₁ = 1 satisfies h32 but `1 < 0` fails; (3) dropping `hr₁`: r₁ = 0, δ = 1, m = 0, q₁ = 3 satisfies h32 but `1 < 1` fails; plus `#check` of the declaration.
