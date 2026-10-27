---
decl: Roth.mul_log_div_two_lt_log_mainCoeffBound
file: Roth/MainLemma.lean
line: 149
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Source step log B_1 > half delta r_1 log q_1 (§6), stated about the project-only def mainCoeffBound (itself NO-composable, not upstreamable); its abstract core log X / 2 < log natfloor X for X at least 2 (compiled, threshold 2 sharp) is not in mathlib and needs the project's sqrt_lt_floor (BORDERLINE), so it is not a 3-call mathlib composition; single caller, no literature standing, so the call is project-local vs upstream.
action: Recommended - keep Roth.mul_log_div_two_lt_log_mainCoeffBound project-local in Roth/MainLemma.lean (single caller three_small_factors at MainLemma l.205); no mathlib PR; if sqrt_lt_floor is ever upstreamed, the abstract X-form could ride along in Mathlib/Analysis/SpecialFunctions/Pow/Real.lean.
---

# Roth.mul_log_div_two_lt_log_mainCoeffBound

## Inventory entry

### `theorem Roth.mul_log_div_two_lt_log_mainCoeffBound`
- **Type**: `∀ {δ : ℝ} {q₁ r₁ : ℕ}, 2 ≤ (↑q₁ : ℝ) ^ (δ * ↑r₁) → δ * ↑r₁ * Real.log ↑q₁ / 2 < Real.log ↑(mainCoeffBound δ q₁ r₁)`
- **What**: With `X = q₁^{δ r₁}` and `B₁ = ⌊X⌋₊ = mainCoeffBound δ q₁ r₁`, if `X ≥ 2` then `½ δ r₁ log q₁ < log B₁`. This is the source's §6 step "Thus `log B_1 > ½ δ r_1 log q_1`" (clean.tex l.1371).
- **How**: One `simpa` term: `Real.log_lt_log` applied to `√X > 0` (`Real.sqrt_pos`) and the project's `sqrt_lt_floor hX` (`√X < ⌊X⌋₊`), then rewriting `log √X = ½ log X` (`Real.log_sqrt`) and `log X = δ r₁ log q₁` (`Real.log_rpow`, with `0 < q₁` extracted from `1 < X` via `Real.one_lt_rpow_iff`).
- **Hypotheses**: `hX : 2 ≤ q₁^{δ r₁}` (necessary: δ = 0 gives `X = 1` and the conclusion `0 < log 1` fails, compiled; threshold 2 is sharp in the abstract form: `X = 3/2` fails, compiled).
- **Uses from project**: `Roth.mainCoeffBound`, `Roth.sqrt_lt_floor`
- **Used by**: Roth/MainLemma.lean:205 (inside `Roth.three_small_factors`, `mul_lt_mul_of_pos_left (mul_log_div_two_lt_log_mainCoeffBound hX) hδ`). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 143–154 (docstring 143–148, statement 149–150), proof length 4 lines
- **Notes**: none

## Junk check (Step 8)
- Used anywhere? Yes, once (MainLemma l.205, in `three_small_factors`).
- Wrapper of 1–2 mathlib calls? Close to it: `Real.log_lt_log` plus rewrites by `Real.log_sqrt`/`Real.log_rpow`, but it also depends on the project lemma `sqrt_lt_floor` and the positivity extraction from `Real.one_lt_rpow_iff`.
- Does mathlib have it? No (loogle `Real.log ((⌊_⌋₊ : ℕ) : ℝ)`: no hits; leansearch / Lean-Finder: no statement of `log X / 2 < log ⌊X⌋₊`; nearest is `Nat.div_two_lt_floor`, which gives `X/2 < ⌊X⌋₊`, a different bound).
- Too specific (inline?)? Single use; inlining would add ~4 lines to `three_small_factors`. It names the source's displayed inequality, so it is a reasonable named step. Keep (inlining is an acceptable optional local golf).
- Well-chosen? Yes; one sharp hypothesis, conclusion matches the source.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring starts "If"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `namespace Roth` / `mul_log_div_two_lt_log`: no hit. Not a glue lemma (`simpa` with a real inequality), so a full run follows. Parent def `Roth.mainCoeffBound` was assessed `NO-composable-from-mathlib` (not upstreamable); the re-aim rule does not apply (parent is not NO-mathlib-has-it).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule; evidence file importing Roth.MainLemma elaborates cleanly via lean-lsp)
- decl `Roth.mul_log_div_two_lt_log_mainCoeffBound`: resolved at Roth/MainLemma.lean:149
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  §6 of the source: Roth's main lemma (Lemma 9) via pigeonhole over box polynomials with coefficients in [0, B_1]

### Statement (Phase 1)

`Roth.mul_log_div_two_lt_log_mainCoeffBound` is a theorem stating the following:

Let `δ` be real, `q₁, r₁` natural numbers, `X = q₁^{δ r₁}` and `B₁ = ⌊X⌋`. If `X ≥ 2`, then `log B₁ > ½ δ r₁ log q₁`. Equivalently, `log ⌊X⌋ > ½ log X` for `X ≥ 2`, specialised to `X = q₁^{δ r₁}`.

Variables / typeclasses involved (Lean side):
- `δ : ℝ`: the Roth exponent parameter.
- `q₁ r₁ : ℕ`: denominator of the first approximation and its degree.

Hypotheses (Lean side):
- `hX : 2 ≤ q₁^{δ r₁}`: lower bound on `X` (in the source it follows from `X > 4`).

Conclusion (math): `½ δ r₁ log q₁ < log B₁`.

Conclusion (Lean): `δ * ↑r₁ * Real.log ↑q₁ / 2 < Real.log ↑(mainCoeffBound δ q₁ r₁)`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an elementary parameter estimate inside the proof of Roth's main lemma; not a main result, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 4 substantive lines (one `simpa` term)
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: check skipped (theorem).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof "log B_1" "1/2" delta r_1 log q_1 integer part q_1^{delta r_1} | partial | `B = ⌊q₁^{δ r₁}⌋` | arXiv math/0307203 (quantitative Roth–Ridout) has the same `B` (its eq. (23)) but no standalone log-bound statement |
| 2 | WebSearch (general form) | inequality log floor(x) > (1/2) log x for x ≥ 2 integer part logarithm bound | no | n/a | no source states `log ⌊x⌋ > ½ log x`; only unrelated floor/log exercises (OEIS A392007, MathGroup) |
| 3 | WebSearch (aliases / ingredient) | floor x greater than sqrt x for x at least 2 elementary inequality | partial | `n − 1 > √n` for `n > 2` | ProofWiki "Number Less One is Greater than Square Root" (integer version of the ingredient); no named real-floor statement |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `log B_1` | yes | l.1371 `\log B_1>\tfrac12\delta r_1\log q_1`; l.1384 Lean note | exact match of the claim; derived from `B₁ > X − 1 > √X` |
| 6 | nLab | logarithm / floor inequality | no | n/a | nLab has no elementary real-inequality content |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | real inequality, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 2–3) | no | n/a | elementary; no named result |
| 10 | recent arXiv | (covered by search 1) | no | n/a | Roth-type proofs state such bounds inline |

### Literature summary (Phase 3)

Concept identified as: ad-hoc parameter estimate in the proof of Roth's lemma; no standard name. Ingredients standard: `⌊X⌋ > √X` for `X ≥ 2` (elementary), monotonicity of `log`, `log X^a = a log X`.
Sources agree on the standard form: n/a (only the project source states it, inline).
Most general standard form: `½ log X < log ⌊X⌋` for real `X ≥ 2`; the `X = q₁^{δ r₁}` specialisation is project-specific.
Generality dimensions where the literature varies:
  - the base quantity: any real `X ≥ 2` (here `X = q₁^{δ r₁}`).
Disagreement with the literature: none.

### Generality analysis — `Roth.mul_log_div_two_lt_log_mainCoeffBound`

Literature-standard form (from Phase 3): source's `log B₁ > ½ δ r₁ log q₁`; abstract core `½ log X < log ⌊X⌋₊` for `X ≥ 2`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hX : 2 ≤ q₁^{δ r₁}` | `2 ≤ X` | `X > 4` in source | no | sharp: δ = 0 (X = 1) fails (evidence check 1); abstract X = 3/2 fails (check 2) |
| 2 | specialisation `X = q₁^{δ r₁}` | concrete `mainCoeffBound` | arbitrary real `X ≥ 2` | yes, as a restatement (not a hypothesis drop) | the abstract X-form compiles (check 3); but it is a different statement, not about `mainCoeffBound` |
| 3 | no sign hypothesis on δ | none | δ > 0 in source | already weaker | positivity of `q₁` is extracted from `1 < X` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (as a statement about `mainCoeffBound`; the only "weakening" is restating about an abstract `X`, which is the abstraction move recorded in 4c, not a hypothesis drop)
Number of weakening opportunities found: 0 hypothesis weakenings
Proposed restatement: none for this declaration.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | scalar hypothesis only | — |
| 2 | Sequences/metric vs filters? | no | no limits | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | `Real.log`/`Real.rpow` are ℝ-specific | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | — | — |
| 8 | Concrete-via-abstract? | yes | `theorem Real.log_div_two_lt_log_natFloor {X : ℝ} (hX : 2 ≤ X) : Real.log X / 2 < Real.log ⌊X⌋₊` (evidence check 3); `mainCoeffBound` is unfolded at once and the proof uses only `X ≥ 2` | none beyond this project: mathlib has no consumer for `log ⌊X⌋₊` lower bounds |
| 9 | False-generalisation guard | no false generalisation | the X-form is the same inequality with `X` abstracted | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (as a mathlib contribution)
  - One-line reason: Q8 fires (the proof is about an abstract `X ≥ 2`), but the abstract form is just `sqrt_lt_floor` composed with `log` monotonicity; it is not a real organisational improvement for mathlib and has no mathlib downstream, so it stays a local refactor option, not a "generalise-first" target.

### Proof strategy — `Roth.mul_log_div_two_lt_log_mainCoeffBound`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | partial | `√X < ⌊X⌋₊` for `X ≥ 2` (project `sqrt_lt_floor`) is the missing helper; assessed separately as BORDERLINE | n/a (follow sqrt_lt_floor's decision) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (log monotonicity plus `Real.log_sqrt`/`Real.log_rpow` rewrites in one `simpa`).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.mul_log_div_two_lt_log_mainCoeffBound`

[A] Lean-Finder       "logarithm of the integer part of a real number x ≥ 2 exceeds half the logarithm of x"   no hits (only `Real.natLog_le_logb`, `Real.log2_le_logb`, Behrend bounds)
[B] Loogle            `Real.log ((⌊_⌋₊ : ℕ) : ℝ)`   no hits
[C] LeanSearch        "half of log x is less than log of floor of x for x at least 2"   nearest `Int.div_two_lt_floor` (`a/2 < ⌊a⌋`), `Nat.log_lt_self`; no log-of-floor bound
[D] Grep mathlib src  `mul_log_div_two_lt_log`, `namespace Roth`, `log_floor`, `div_two_lt_floor`   only `Nat.div_two_lt_floor` (Algebra/Order/Floor/Semifield.lean:81) and `Int.div_two_lt_floor` (Algebra/Order/Floor/Ring.lean:809)
[E] Name pattern      `Roth.mul_log_div_two_lt_log_mainCoeffBound`, `log_div_two_lt_log`   no mathlib decl

Searched for both:
  - the user's current form (about `mainCoeffBound`)
  - the abstract form `log X / 2 < log ⌊X⌋₊`

Concluded: found building blocks (`Real.log_lt_log`, `Real.log_sqrt`, `Real.log_rpow`, `Real.sqrt_pos`, `Real.one_lt_rpow_iff`, `Nat.div_two_lt_floor`); neither form is in mathlib.

### Normal-form check — `Roth.mul_log_div_two_lt_log_mainCoeffBound`

Equivalent formalisms: `½ δ r₁ log q₁ < log B₁` vs `q₁^{δ r₁/2} < B₁` vs `√X < B₁`.
Does mathlib already have a canonical form? No. The log form is what the single caller consumes (fed into `nlinarith` after `Real.lt_rpow_of_log_lt`). OK. RHS convention: n/a (not an iff).

### Syntactic generality — `Roth.mul_log_div_two_lt_log_mainCoeffBound`

Alternative restatements attempted:
- abstract `Real.log X / 2 < Real.log ⌊X⌋₊` for `2 ≤ X` (compiled, check 3).
- multiplicative `q₁^{δ r₁/2} < B₁`.
- current log form about `mainCoeffBound`.

Chosen restatement: current; it is exactly the term `nlinarith` needs at the caller and matches the source's display.
Justification: the abstract form would force the caller to rewrite `Real.log_rpow` itself.

### Superfluous-argument audit — `Roth.mul_log_div_two_lt_log_mainCoeffBound`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hX : 2 ≤ q₁^{δ r₁}` | yes | sharp (checks 1–2) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (project-local).

### Call sites — `Roth.mul_log_div_two_lt_log_mainCoeffBound`

Internal use count: 0 outside the declaring file; 1 in the declaring file
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:205 | `mul_lt_mul_of_pos_left (mul_log_div_two_lt_log_mainCoeffBound hX) hδ]` (inside `three_small_factors`, `nlinarith only [...]`) |

Inline-derivation grep (`Real.log_sqrt`, `log_lt_log .* sqrt_lt_floor` across Roth/): (none besides this declaration).

### Composition check (Phase 6)

Can `Roth.mul_log_div_two_lt_log_mainCoeffBound` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Real.log_lt_log (Real.sqrt_pos.2 _) (sqrt_lt_floor hX).1` then rewrite with `Real.log_sqrt`, `Real.log_rpow` (the current proof; abstract version is evidence check 3).
  - Mathlib decls used: `Real.log_lt_log`, `Real.sqrt_pos`, `Real.log_sqrt`, `Real.log_rpow`, `Real.one_lt_rpow_iff`
  - Result: partial — needs the project lemma `Roth.sqrt_lt_floor`, which itself is not a ≤3-call mathlib composition (per its own report: `Real.sqrt_lt'` + `Nat.lt_floor_add_one` + `nlinarith`).
Attempt 2: via mathlib's `Nat.div_two_lt_floor` (`X/2 < ⌊X⌋₊`, evidence check 4).
  - Result: fails — yields only `log X − log 2 < log ⌊X⌋₊`, weaker than `½ log X` for `X < 4`.

Conclusion: NOT-COMPOSABLE (from mathlib alone; it is a 1-call composition on top of the project's `sqrt_lt_floor`)

### Verdict: `Roth.mul_log_div_two_lt_log_mainCoeffBound`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): only the project source states it (clean.tex l.1371, l.1384); no named result.
- Generality analysis (Phase 4): MAXIMALLY GENERAL for its statement (hypothesis sharp, compiled); Q8 abstraction available but not a mathlib improvement.
- Mathlib search (Phase 5): building blocks only.
- Composition check (Phase 6): NOT-COMPOSABLE from mathlib alone (needs project `sqrt_lt_floor`).

**Rationale:**

As stated, the lemma is about `Roth.mainCoeffBound`, a project definition already judged not upstreamable, so this exact statement cannot go to mathlib. Its abstract core `½ log X < log ⌊X⌋₊` (X ≥ 2) is true with a sharp threshold, absent from mathlib, and is not a ≤3-call mathlib composition because its key ingredient `√X < ⌊X⌋₊` is itself missing (the project's `sqrt_lt_floor`, BORDERLINE). Neither NO bucket fits, but a YES is weak: no literature standing, no mathlib gap or consumer, and the core is a one-line `log` corollary of `sqrt_lt_floor`. Whether anything goes upstream is therefore tied to the human decision on `sqrt_lt_floor`; recommended answer is to keep it project-local.

Belongs-elsewhere: project-local, Roth/MainLemma.lean, encoding the source's "`log B_1 > ½ δ r_1 log q_1`" for its single caller.

Numbered questions:
  1. Keep `Roth.mul_log_div_two_lt_log_mainCoeffBound` project-local (recommended: yes)?
  2. If `Roth.sqrt_lt_floor` is upstreamed, also add the abstract `Real.log X / 2 < Real.log ⌊X⌋₊` corollary alongside it (recommended: no, too thin)?
  3. Inline it into its single caller `three_small_factors` (MainLemma l.205) instead of keeping a named lemma (recommended: no; it names the source's display)?

Next action: user answers; default is keep project-local with no change.

---

### Next step

Keep `Roth.mul_log_div_two_lt_log_mainCoeffBound` in Roth/MainLemma.lean (single caller MainLemma l.205); no upstream PR.

## Evidence
- `grep -rn mul_log_div_two_lt_log_mainCoeffBound Roth/`: definition l.149; single use l.205.
- lean_loogle `Real.log ((⌊_⌋₊ : ℕ) : ℝ)`: no hits. lean_leansearch, lean_leanfinder: no matching statement (Phase 5).
- grep of `.lake/packages/mathlib/Mathlib/`: no `namespace Roth`, no `mul_log_div_two_lt_log`; `Nat.div_two_lt_floor` at Algebra/Order/Floor/Semifield.lean:81, `Int.div_two_lt_floor` at Algebra/Order/Floor/Ring.lean:809.
- WebSearch x3 (Phase 3 rows 1–3): no standalone statement.
- clean.tex l.1362–1384: source statement and Lean note.
- Evidence file `.mathlib-quality/overview/evidence/Roth.mul_log_div_two_lt_log_mainCoeffBound/checks.lean` (checked with lean_diagnostic_messages: no errors or warnings): (1) δ = 0, q₁ = 3, r₁ = 1 makes the conclusion false, so `hX` cannot be dropped; (2) abstract form fails at X = 3/2, so threshold 2 is sharp; (3) abstract form `Real.log X / 2 < Real.log ⌊X⌋₊` for `2 ≤ X` from `sqrt_lt_floor`; (4) `Nat.div_two_lt_floor` statement (the nearest mathlib lemma); (5) `#check` of the declaration.
