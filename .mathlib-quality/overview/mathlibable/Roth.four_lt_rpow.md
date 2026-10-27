---
decl: Roth.four_lt_rpow
file: Roth/MainLemma.lean
line: 122
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Ad-hoc numerical estimate q1^(delta r1) > 4 from 3 at most delta^2 log q1 (source §6, X > 4); hypotheses delta at least 0 and r1 positive are necessary (counterexamples compiled); not in mathlib and not a 3-call composition (needs log 2 < 3/4 plus nlinarith after Real.lt_rpow_of_log_lt); no literature standing, so the call is project-local vs upstream.
action: Recommended - keep Roth.four_lt_rpow project-local in Roth/MainLemma.lean (callers MainLemma l.641, Main l.495); optional local golf - replace the hlog2 exp-quadratic argument by Real.log_two_lt_d9 (Mathlib/Analysis/Complex/ExponentialBounds.lean); no mathlib PR.
---

# Roth.four_lt_rpow

## Inventory entry

### `theorem Roth.four_lt_rpow`
- **Type**: `∀ {δ : ℝ}, 0 ≤ δ → ∀ {q₁ r₁ : ℕ}, 0 < r₁ → 3 ≤ δ ^ 2 * Real.log ↑q₁ → 4 < (↑q₁ : ℝ) ^ (δ * ↑r₁)`
- **What**: If `δ ≥ 0`, `r₁ ≥ 1` and `δ² log q₁ ≥ 3`, then `X = q₁^{δ r₁} > 4`. This is the source's §6 claim "`X > 4`" (clean.tex l.1367), which there follows from (32) and (29).
- **How**: Derives `log q₁ > 0` (`pos_of_mul_pos_right`), hence `q₁ ≥ 2` (`Real.log_pos_iff`); proves `log 2 < 3/4` via `Real.log_lt_iff_lt_exp` and `Real.quadratic_le_exp_of_nonneg`; reduces the goal with `Real.lt_rpow_of_log_lt` to `log 4 < δ r₁ log q₁`; proves `log 4 = 2 log 2 < δ log q₁` by contradiction with `nlinarith` (using `mul_self_le_mul_self`, `Real.log_le_log`, `Real.log_pos`), then multiplies by `r₁ ≥ 1` (`le_mul_of_one_le_right`).
- **Hypotheses**: `hδ0 : 0 ≤ δ` (necessary; δ = -2, q₁ = 3, r₁ = 1 is a counterexample, compiled), `hr₁ : 0 < r₁` (necessary; r₁ = 0 gives `X = 1`, compiled), `hq₁ : 3 ≤ δ² log q₁` (the constant 3 could be lowered to anything above `4 log 2 ≈ 2.77`, not pursued: no caller benefit).
- **Uses from project**: `[]`
- **Used by**: Roth/MainLemma.lean:641 (`Nat.floor_pos.2 <| (by norm_num : (1 : ℝ) ≤ 4).trans (four_lt_rpow hδ0 hr₁ hq).le`); Roth/Main.lean:495 (`sqrt_lt_floor ((by norm_num : (2 : ℝ) ≤ 4).trans (four_lt_rpow hδ0 hr0 h32').le)`).
- **Visibility**: public
- **Lines**: 118–141 (docstring 118–121, statement 122–123), proof length 18 lines
- **Notes**: Both callers use only `.le` and need only `1 ≤ X` resp. `2 ≤ X`; the strict `4 <` mirrors the source's "`X > 4`".

## Junk check (Step 8)
- Used anywhere? Yes, 2 call sites in 2 files (MainLemma l.641, Main l.495).
- Wrapper of 1–2 mathlib calls? No: 18-line proof with a numeric `log 2` bound and two `nlinarith` steps.
- Does mathlib have it? No (loogle `_ < (_ : ℝ) ^ (_ : ℝ), Real.log` returns only `Real.lt_rpow_of_log_lt`, `Real.rpow_lt_of_lt_log`, `Real.lt_rpow_iff_log_lt`; leansearch/Lean-Finder no matching statement).
- Too specific (inline?)? It is source-specific (constant 3 from (32)) but is used twice and inlining would duplicate 18 lines. Keep.
- Well-chosen? Yes; hypotheses δ ≥ 0 and r₁ > 0 are necessary (compiled). Minor golf: `hlog2` could use `Real.log_two_lt_d9`.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring starts "The bound"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `namespace Roth` / `four_lt_rpow`: no hit. Not a glue lemma, so a full run follows.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule; evidence file importing Roth.MainLemma elaborates cleanly via lean-lsp)
- decl `Roth.four_lt_rpow`: resolved at Roth/MainLemma.lean:122
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  §6 of the source: Roth's main lemma (Lemma 9), its parameters λ, γ, η, B_1, and the pigeonhole step

### Statement (Phase 1)

`Roth.four_lt_rpow` is a theorem stating the following:

Let `δ ≥ 0` be real and `q₁, r₁` natural numbers with `r₁ ≥ 1`. If `δ² log q₁ ≥ 3`, then `q₁^{δ r₁} > 4`. (The hypothesis forces `q₁ ≥ 2`; then `δ log q₁ = √(δ² log q₁ · log q₁) ≥ √(3 log 2) > 2 log 2 = log 4`.)

Variables / typeclasses involved (Lean side):
- `δ : ℝ`: the Roth exponent parameter.
- `q₁ r₁ : ℕ`: denominator of the first approximation and its degree.

Hypotheses (Lean side):
- `hδ0 : 0 ≤ δ`: sign of the exponent.
- `hr₁ : 0 < r₁`: so `δ r₁ ≥ δ`.
- `hq₁ : 3 ≤ δ² log q₁`: the source's consequence of (32) with `m ≥ 1`.

Conclusion (math): `q₁^{δ r₁} > 4`.

Conclusion (Lean): `4 < (q₁ : ℝ) ^ (δ * r₁)`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an elementary numerical parameter estimate inside the proof of Roth's main lemma; not a main result, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 18 substantive lines
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: check skipped (theorem).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof "q_1^{\delta r_1}" B_1 integer part log q_1 inequality | partial | n/a | arXiv math/0307203 (quantitative Roth–Ridout) has the same parameter set-up (log q₁ > δ⁻¹ m(2m+1)) but no standalone `X > 4` statement |
| 2 | WebSearch (general form) | inequality x^y > c from log bound "log x" exponent lower bound real power elementary lemma | no | `x^y > c ⟺ y log x > log c` | only the generic log reduction (mathlib `Real.lt_rpow_iff_log_lt`) |
| 3 | WebSearch (aliases / numeric ingredient) | log 2 < 3/4 bound "log 4" elementary estimate natural number q ≥ 2 exponent | partial | `log 2 < 3/4` | standard numeric fact (e.g. series bound, arXiv 2609.26444); mathlib has `Real.log_two_lt_d9` |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `X>4`, `whence` | yes | l.1367 "writing X = q_1^{δ r_1}, we have X > 4"; l.1383 Lean note for `X > 4` | exact match of the claim |
| 6 | nLab | real power / logarithm inequality | no | n/a | nLab has no elementary real-inequality content |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | real inequality, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 2–3) | no | n/a | elementary; no named result |
| 10 | recent arXiv | (covered by search 1) | no | n/a | Roth-type proofs state such bounds inline |

### Literature summary (Phase 3)

Concept identified as: ad-hoc numerical estimate in the proof of Roth's lemma; no standard name. Ingredients standard: `x < y^z ⟺ log x < z log y`, `log 2 < 3/4`.
Sources agree on the standard form: n/a (only the project source states it, inline).
Most general standard form: `c < q^{δr}` whenever `log c < δ r log q`; the specific numbers (3, 4) are project-specific.
Generality dimensions where the literature varies:
  - constant in the hypothesis: any `c > 4 log 2` works for the conclusion `> 4`.
Disagreement with the literature: none.

### Generality analysis — `Roth.four_lt_rpow`

Literature-standard form (from Phase 3): source's `X > 4` under (32), (29).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hδ0 : 0 ≤ δ` | `0 ≤ δ` | `δ > 0` | no | necessary: δ = -2, q₁ = 3, r₁ = 1 counterexample (evidence check 1) |
| 2 | `hr₁ : 0 < r₁` | `0 < r₁` | `r₁ ≥ 1` | no | necessary: r₁ = 0 gives `X = 1` (evidence check 2) |
| 3 | `hq₁ : 3 ≤ δ² log q₁` | constant 3 | from (32) | cosmetic only | constant can drop to any value above `4 log 2`; no caller has a smaller constant, so not a generalisation of interest |
| 4 | `q₁ : ℕ` | natural | natural | no | natural-ness forces `q₁ ≥ 2` from `log q₁ > 0`; for real `q₁ ∈ (1,2)` the conclusion fails for suitable δ |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (the only slack is the numeric constant 3, irrelevant to callers)
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | scalar hypotheses only | — |
| 2 | Sequences/metric vs filters? | no | no limits | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | `Real.rpow`/`Real.log` are ℝ-specific | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | ℕ is used essentially (q₁ ≥ 2) | — |
| 8 | Concrete-via-abstract? | no | no named object; the only abstract core is `Real.lt_rpow_of_log_lt`, already in mathlib | — |
| 9 | False-generalisation guard | no false generalisation | none proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: a numeric estimate with fixed constants; no structural content to abstract.

### Proof strategy — `Roth.four_lt_rpow`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | `Real.log_two_lt_d9` already exists and replaces the `hlog2` exp-quadratic argument (evidence check 4) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (log reduction via `Real.lt_rpow_of_log_lt`, then real arithmetic). Minor optional golf: `hlog2` via `Real.log_two_lt_d9` (needs `import Mathlib.Analysis.Complex.ExponentialBounds`).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.four_lt_rpow`

[A] Lean-Finder       "lower bound for real power of natural number given bound on delta squared times log q"   no hits (only Behrend bounds)
[B] Loogle            `_ < (_ : ℝ) ^ (_ : ℝ), Real.log`   building blocks only: `Real.lt_rpow_of_log_lt`, `Real.rpow_lt_of_lt_log`, `Real.lt_rpow_iff_log_lt`
[C] LeanSearch        "if log x < y * log b then x < b ^ y real power"   building blocks: `Real.rpow_lt_of_lt_log`, `Real.logb_lt_iff_lt_rpow`, `Real.lt_pow_of_log_lt`
[D] Grep mathlib src  `four_lt_rpow`, `lt_rpow_of_log_lt`, `namespace Roth`   only `Real.lt_rpow_of_log_lt` (Analysis/SpecialFunctions/Pow/Real.lean:805); `Real.log_two_lt_d9` (Analysis/Complex/ExponentialBounds.lean:86)
[E] Name pattern      `Roth.four_lt_rpow`, `four_lt_rpow`   no mathlib decl

Searched for both:
  - the user's current form
  - the general form `c < q^{δr}` from a log bound (exists: `Real.lt_rpow_of_log_lt`)

Concluded: found building blocks (`Real.lt_rpow_of_log_lt`, `Real.log_pos_iff`, `Real.log_two_lt_d9`, `Real.log_le_log`); the specific estimate is not in mathlib.

### Normal-form check — `Roth.four_lt_rpow`

Equivalent formalisms: `4 < q₁^{δ r₁}` vs `log 4 < δ r₁ log q₁` (via `Real.lt_rpow_iff_log_lt`).
Does mathlib already have a canonical form? The rpow form is what callers consume (fed to `sqrt_lt_floor`, `Nat.floor_pos`). OK. RHS convention: n/a (not an iff).

### Syntactic generality — `Roth.four_lt_rpow`

Alternative restatements attempted:
- conclusion `2 ≤ q₁^{δ r₁}` (all callers need at most this).
- log form `log 4 < δ r₁ log q₁`.
- current `4 < q₁^{δ r₁}`.

Chosen restatement: current; it matches the source's "`X > 4`" and implies what both callers need via `.le` plus a numeral step.
Justification: easiest to cite against the source; the weaker `2 ≤` would save one `norm_num` step at each caller but would drift from the source.

### Superfluous-argument audit — `Roth.four_lt_rpow`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hδ0 : 0 ≤ δ` | yes | counterexample compiled |
| 2 | `hr₁ : 0 < r₁` | yes | counterexample compiled |
| 3 | `hq₁ : 3 ≤ δ² log q₁` | yes | constant has slack (any `> 4 log 2`) but the hypothesis is needed |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (project-local).

### Call sites — `Roth.four_lt_rpow`

Internal use count: 2 (1 in the declaring file, 1 outside)
External-to-file callers: 1 distinct file (Roth/Main.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:641 | `(Nat.floor_pos.2 <| (by norm_num : (1 : ℝ) ≤ 4).trans (four_lt_rpow hδ0 hr₁ hq).le)` |
| Roth/Main.lean:495 | `sqrt_lt_floor ((by norm_num : (2 : ℝ) ≤ 4).trans (four_lt_rpow hδ0 hr0 h32').le)` |

Inline-derivation grep (`lt_rpow_of_log_lt`, `log_two` across Roth/): (none besides this declaration).

### Composition check (Phase 6)

Can `Roth.four_lt_rpow` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Real.lt_rpow_of_log_lt hq (h : log 4 < δ r₁ log q₁)` (evidence check 3).
  - Mathlib decls used: `Real.lt_rpow_of_log_lt`
  - Result: partial — reduces to `log 4 < δ r₁ log q₁`, which needs `q₁ ≥ 2`, `log 2 < 3/4` and an `nlinarith` argument (`(δ log q₁)² ≥ 3 log q₁ ≥ 3 log 2 > (2 log 2)²`).
Attempt 2: `Real.lt_rpow_iff_log_lt` plus `Real.log_two_lt_d9`.
  - Result: partial — same missing nonlinear step; by the 6b heuristics this is a real proof.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.four_lt_rpow`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): only the project source states it (clean.tex l.1367, l.1383); no named result.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (δ ≥ 0 and r₁ > 0 necessary, compiled).
- Mathlib search (Phase 5): building blocks only (`Real.lt_rpow_of_log_lt`, `Real.log_two_lt_d9`).
- Composition check (Phase 6): NOT-COMPOSABLE (needs a nonlinear arithmetic step).

**Rationale:**

The estimate is true, has no superfluous hypotheses, is absent from mathlib and is not a ≤3-call composition, so neither NO bucket fits. But the YES case is weak: the constants 3 and 4 are artefacts of the source's parameter choices, there is no literature presence as a standalone fact, and no mathlib gap or TODO calls for it; the generally useful core (`Real.lt_rpow_of_log_lt`) is already in mathlib. This is a taste/policy call, with the recommended answer being to keep it project-local.

Belongs-elsewhere: project-local, Roth/MainLemma.lean, encoding the source's "`X > 4`" for 2 call sites.

Numbered questions:
  1. Keep `Roth.four_lt_rpow` project-local (recommended: yes)?
  2. Golf `hlog2` to `by linarith [Real.log_two_lt_d9]` at the cost of importing `Mathlib.Analysis.Complex.ExponentialBounds` into Roth/MainLemma.lean?
  3. Since both callers only need `2 ≤ X`, keep the source-faithful `4 < X` (recommended) rather than weakening the conclusion?

Next action: user answers; default is keep project-local with no change.

---

### Next step

Keep `Roth.four_lt_rpow` in Roth/MainLemma.lean (callers MainLemma l.641, Main l.495); no upstream PR.

## Evidence
- `grep -rn four_lt_rpow Roth/`: definition l.122; uses MainLemma l.641, Main l.495.
- lean_loogle `_ < (_ : ℝ) ^ (_ : ℝ), Real.log`: building blocks only. lean_leansearch, lean_leanfinder: no matching statement (Phase 5).
- grep of `.lake/packages/mathlib/Mathlib/`: no `namespace Roth`, no `four_lt_rpow`; `Real.lt_rpow_of_log_lt` at Analysis/SpecialFunctions/Pow/Real.lean:805; `Real.log_two_lt_d9` at Analysis/Complex/ExponentialBounds.lean:86.
- WebSearch x3 (Phase 3 rows 1–3): no standalone statement.
- clean.tex l.1367, l.1383: source statement.
- Evidence file `.mathlib-quality/overview/evidence/Roth.four_lt_rpow/checks.lean` (checked with lean_diagnostic_messages: no errors, after adding the ExponentialBounds import): (1) δ = -2, q₁ = 3, r₁ = 1 satisfies the hypothesis but `3^{-2} ≤ 1`, so `hδ0` is necessary; (2) r₁ = 0 gives `X = 1`, so `hr₁` is necessary; (3) `Real.lt_rpow_of_log_lt` reduces the goal to the log inequality; (4) `log 2 < 3/4` from `Real.log_two_lt_d9`; (5) `#check` of the declaration.
