---
decl: Roth.sqrt_lt_floor
file: Roth/MainLemma.lean
line: 115
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Elementary estimate sqrt X < natfloor X and natfloor X at most X for real X at least 2 (source §6, B_1 = floor X > sqrt X); not in mathlib under any of five search methods, no literature standing as a named fact, threshold 2 sharp (compiled), but not a 3-call composition (strict half needs Real.sqrt_lt' plus Nat.lt_floor_add_one plus nlinarith); an ad-hoc conjunction mathlib is unlikely to want, so the call is project-local vs upstream.
action: Recommended - keep Roth.sqrt_lt_floor project-local in Roth/MainLemma.lean (callers MainLemma l.154, l.201, Main l.494); if upstreaming is desired, ship only the strict half as Nat.sqrt_lt_floor-style lemma in Mathlib/Analysis/Real/Sqrt.lean, never the conjunction.
---

# Roth.sqrt_lt_floor

## Inventory entry

### `theorem Roth.sqrt_lt_floor`
- **Type**: `∀ {X : ℝ}, 2 ≤ X → √X < (⌊X⌋₊ : ℝ) ∧ (⌊X⌋₊ : ℝ) ≤ X`
- **What**: For real `X ≥ 2`, the natural floor of `X` lies strictly above `√X` and at or below `X`. This is the source's §6 estimate `B₁ = ⌊X⌋ > X - 1 > √X` with `X = q₁^{δ r₁}`, together with the retained upper bound `B₁ ≤ X`.
- **How**: Anonymous-constructor pairing: the strict half is the private helper `Roth.sqrt_lt_nat_floor_aux hX` (itself `Real.sqrt_lt'` + `Nat.le_floor` + `Nat.lt_floor_add_one` + `nlinarith`), the upper half is mathlib's `Nat.floor_le (by positivity)`.
- **Hypotheses**: `hX : 2 ≤ X`. Sharp: at `X = 1` the strict half fails (`√1 = 1 = ⌊1⌋₊`, compiled in evidence), and for `X ∈ [1,2)` generally `⌊X⌋₊ = 1 ≤ √X`. The upper half alone needs only `0 ≤ X`.
- **Uses from project**: `Roth.sqrt_lt_nat_floor_aux`
- **Used by**: `Roth.mul_log_div_two_lt_log_mainCoeffBound` (Roth/MainLemma.lean:154, `.1`); the `key` step of a theorem at Roth/MainLemma.lean:201 (`.1`); Roth/Main.lean:494 (`obtain ⟨hsqB, hBX⟩ := sqrt_lt_floor ...`, both halves).
- **Visibility**: public
- **Lines**: 108–116 (docstring 108–114, statement 115), proof length 1 line
- **Notes**: Hypothesis was weakened from `4 < X` to `2 ≤ X` in commit 9bebcd0 (source has `X > 4`, clean.tex l.1383). The strict half was split off as the private `sqrt_lt_nat_floor_aux` (assessed SKIP).

## Junk check (Step 8)
- Used anywhere? Yes, 3 call sites in 2 files (MainLemma l.154, l.201; Main l.494).
- Wrapper of 1–2 mathlib calls? The upper half is exactly `Nat.floor_le`; the strict half is a short nlinarith proof, not a mathlib call.
- Does mathlib have it? No (loogle `Real.sqrt _ < ((Nat.floor _ : ℕ) : ℝ)`: no results; leansearch/Lean-Finder return only `Real.sqrt_lt'`, `Real.real_sqrt_lt_nat_sqrt_succ`, `Nat.sqrt_lt_self`, etc.).
- Too specific (inline?)? The conjunction mirrors the source's single sentence and is consumed as a pair at Main l.494; two callers use only `.1`. Inlining would duplicate the nlinarith argument. Keep.
- Well-chosen? Yes; hypothesis sharp. Minor option: callers using only `.1` could call the strict half directly if it were made public, but this is cosmetic.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring starts "If `X ≥ 2`"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `Roth.sqrt_lt_floor` / `namespace Roth`: no hit. Not a glue lemma (not `rfl`), so a full run follows.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule; evidence file importing Roth.MainLemma compiles cleanly)
- decl `Roth.sqrt_lt_floor`: resolved at Roth/MainLemma.lean:115
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  §6 of the source: Roth's main lemma, its parameters λ, γ, η, B_1, and the pigeonhole step

### Statement (Phase 1)

`Roth.sqrt_lt_floor` is a theorem stating the following:

For every real number `X ≥ 2` one has `√X < ⌊X⌋ ≤ X`, where `⌊X⌋` is the (natural) integer part. Equivalently `⌊X⌋² > X`, i.e. the integer part already exceeds the square root as soon as it is at least 2.

Variables / typeclasses involved (Lean side):
- `X : ℝ`: the real number (in the application `X = q₁^{δ r₁}`).

Hypotheses (Lean side):
- `hX : 2 ≤ X`: ensures `⌊X⌋₊ ≥ 2`, so `⌊X⌋₊² ≥ ⌊X⌋₊ + 2 > X`.

Conclusion (math): `√X < ⌊X⌋ ≤ X`.

Conclusion (Lean): `√X < (⌊X⌋₊ : ℝ) ∧ (⌊X⌋₊ : ℝ) ≤ X`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an elementary real-number estimate used as a parameter bound in Roth's proof; not a main result, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: check skipped (theorem).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | "sqrt(x) < floor(x)" for x >= 2 inequality | no | n/a | only floor exercises (ProofWiki "Floor of Root 2", areteem forum); no stated lemma; hand proof as in Phase 1 |
| 2 | WebSearch (general form) | floor function inequality x - 1 < floor(x) <= x lower bound by square root | yes (partial) | `x - 1 < ⌊x⌋ ≤ x` | ProofWiki "Floor is between Number and One Less" (Knuth TAOCP 1.2.4); no square-root form |
| 3 | WebSearch (named-after / source context) | Roth theorem proof "B_1" integer part q_1^{delta r_1} "log B_1" Cassels | no | n/a | Cassels Ch. VI, arXiv math/0307203; no standalone statement of this estimate |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep clean.tex for `B_1`, `lfloor X` | yes | l.1368 `B_1=⌊X⌋>X-1>√X`; l.1383 Lean note `√X<⌊X⌋≤X for X>4` | exact match (Lean has the sharper `2 ≤ X`) |
| 6 | nLab | floor function / integer part | no | n/a | nLab has no elementary floor-inequality content |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | real inequality, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–2) | no | n/a | elementary; only exercise-level threads on floor bounds |
| 10 | recent arXiv | (covered by search 3) | no | n/a | Roth-type proofs use their own ad-hoc bounds |

### Literature summary (Phase 3)

Concept identified as: elementary floor estimate; no standard name. Standard nearby fact: `x - 1 < ⌊x⌋ ≤ x`.
Sources agree on the standard form: n/a (only the project source states this exact estimate, with `X > 4`).
Most general standard form: `√X < ⌊X⌋` iff `⌊X⌋ ≥ 2` iff `X ≥ 2`; upper half `⌊X⌋ ≤ X` for `X ≥ 0`.
Generality dimensions where the literature varies:
  - threshold: source `X > 4` (via `X - 1 > √X`, valid for `X > (3+√5)/2`), Lean `X ≥ 2` (sharp).
  - ordered field: could be any `FloorSemiring` linear ordered field with a square root, but `√` is real-specific in mathlib.
Disagreement with the literature: none; Lean form strictly sharper than the source's.

### Generality analysis — `Roth.sqrt_lt_floor`

Literature-standard form (from Phase 3): `√X < ⌊X⌋ ≤ X` for `X > 4` (source); sharp form `X ≥ 2`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `X : ℝ` | real | real | no | `Real.sqrt` is ℝ-specific; `NNReal.sqrt` variant would be a restatement, not a weakening |
| 2 | `hX : 2 ≤ X` | `2 ≤ X` | `4 < X` | no | sharp: `X = 1` counterexample compiled (evidence check 2); for the upper half alone `0 ≤ X` suffices (check 3) but the conjunction needs `2 ≤ X` |
| 3 | `⌊·⌋₊` (Nat.floor) vs `⌊·⌋` (Int.floor) | Nat.floor | integer part | no | equal for `X ≥ 0`; Nat.floor is what the caller needs (B₁ a natural number) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (no hypothesis can be weakened; counterexample compiled)
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | single real variable | — |
| 2 | Sequences/metric vs filters? | no | no limits | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | `Real.sqrt` only exists on ℝ (and NNReal) | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | — | — |
| 8 | Concrete-via-abstract? | no | statement has no named object; the proof is already about a generic `X` | — |
| 9 | False-generalisation guard | no false generalisation | none proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: an elementary real estimate with no structural content to abstract; the only shape question is conjunction vs separate lemmas (Phase 5.5).

### Proof strategy — `Roth.sqrt_lt_floor`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | building blocks `Real.sqrt_lt'`, `Nat.lt_floor_add_one`, `Nat.le_floor`, `Nat.floor_le` exist | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(Reduce `√X < f` to `X < f²` with `Real.sqrt_lt'`, then `X < f + 1 ≤ f²` by nlinarith from `Nat.lt_floor_add_one`, `f ≥ 2`.)

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.sqrt_lt_floor`

[A] Lean-Finder       "for real x ≥ 2, sqrt x < ⌊x⌋₊"            no hits (closest `Real.real_sqrt_lt_nat_sqrt_succ`, `Nat.sqrt_lt_self`, `Nat.sqrt_mul_sqrt_lt_succ`)
[B] Loogle            `Real.sqrt _ < ((Nat.floor _ : ℕ) : ℝ)`     no results
[C] LeanSearch        "square root of x is less than the floor of x, and floor of x is at most x, for real x at least 2"   no hits (`Real.sqrt_lt'`, `Real.sqrt_lt`, `Real.nat_floor_real_sqrt_eq_nat_sqrt`, `Nat.sqrt_le'`, `Real.sqrt_le_one`)
[D] Grep mathlib src  `theorem .*sqrt.*floor` / `.*floor.*sqrt`; `sub_one_lt_floor`, `lt_floor_add_one`   only `Real.floor_real_sqrt_eq_nat_sqrt`, `Real.nat_floor_real_sqrt_eq_nat_sqrt` (Analysis/Real/Sqrt.lean:429, 435), building blocks `Nat.lt_floor_add_one` (Algebra/Order/Floor/Semiring.lean:63), `Nat.sub_one_lt_floor` (Semiring.lean:386)
[E] Name pattern      `Roth.sqrt_lt_floor`, `sqrt_lt_floor`, `Real.sqrt_lt_floor`   no mathlib decl

Searched for both:
  - the user's current form (conjunction)
  - the literature-standard / sharp strict half `√X < ⌊X⌋₊` and the `X²`-form `X < ⌊X⌋₊²`

Concluded: found building blocks (`Real.sqrt_lt'`, `Nat.le_floor`, `Nat.lt_floor_add_one`, `Nat.floor_le`); not in mathlib in either form.

### Normal-form check — `Roth.sqrt_lt_floor`

Equivalent formalisms: `√X < ⌊X⌋₊` vs `X < ⌊X⌋₊ ^ 2` (via `Real.sqrt_lt'`); conjunction vs two separate lemmas.
Does mathlib already have a canonical form? For the upper half yes, `Nat.floor_le`. For the strict half no.
Mathlib convention would be separate lemmas, not a conjunction bundling an existing lemma (`Nat.floor_le`) with a new one. RHS convention: n/a (not an iff).

### Syntactic generality — `Roth.sqrt_lt_floor`

Alternative restatements attempted:
- strict half alone `√X < ⌊X⌋₊` (exists as private `sqrt_lt_nat_floor_aux`).
- squared form `X < ⌊X⌋₊ ^ 2`.
- conjunction (current).

Chosen restatement: current conjunction for the project (Main l.494 destructures both halves; it mirrors the source sentence). For mathlib, the strict half alone.
Justification: the project consumes the pair at one site; mathlib would never want `∧ Nat.floor_le`.

### Superfluous-argument audit — `Roth.sqrt_lt_floor`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hX : 2 ≤ X` | yes | strict half fails at `X = 1` (compiled); upper half alone would need only `0 ≤ X` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK for project use; for mathlib REFACTOR (drop the `∧ Nat.floor_le` half)
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (project); RESTATE-BEFORE-SHIP if ever upstreamed (strict half only).

### Call sites — `Roth.sqrt_lt_floor`

Internal use count: 3 (2 in the declaring file, 1 outside)
External-to-file callers: 1 distinct file (Roth/Main.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:154 | `Real.log_lt_log (Real.sqrt_pos.2 ...) (sqrt_lt_floor hX).1` |
| Roth/MainLemma.lean:201 | `(Real.sqrt_nonneg _).trans_lt (sqrt_lt_floor hX).1` |
| Roth/Main.lean:494 | `obtain ⟨hsqB, hBX⟩ := sqrt_lt_floor ((by norm_num : (2 : ℝ) ≤ 4).trans (four_lt_rpow hδ0 hr0 h32').le)` |

Inline-derivation grep (`Nat.lt_floor_add_one`, `Real.sqrt_lt'` with `⌊` across Roth/): (none besides `sqrt_lt_nat_floor_aux`).

### Composition check (Phase 6)

Can `Roth.sqrt_lt_floor` be derived from mathlib in ≤3 chained calls?

Attempt 1: `⟨(Real.sqrt_lt' (by positivity)).2 (by nlinarith only [Nat.lt_floor_add_one X, hf]), Nat.floor_le (by positivity)⟩` with `hf : 2 ≤ ⌊X⌋₊` from `Nat.le_floor hX`.
  - Mathlib decls used: `Real.sqrt_lt'`, `Nat.lt_floor_add_one`, `Nat.le_floor`, `Nat.floor_le`
  - Result: succeeds (evidence check 1), but needs a `have` plus `nlinarith`: by the 6b heuristics this is a proof, not a composition.
Attempt 2: `Nat.sub_one_lt_floor` chained with `X - 1 > √X`.
  - Result: fails at `X = 2` (`2 - 1 < √2`, evidence check 4); only works for `X > (3+√5)/2`, so not available under `2 ≤ X`.

Conclusion: NOT-COMPOSABLE (upper half alone is a 1-call composition `Nat.floor_le`; strict half is a short genuine proof).

### Verdict: `Roth.sqrt_lt_floor`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): only the project source states it (clean.tex l.1368, l.1383); nearest standard fact `x - 1 < ⌊x⌋ ≤ x`.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (`2 ≤ X` sharp, compiled).
- Mathlib search (Phase 5): building blocks only; not in mathlib in either form.
- Composition check (Phase 6): NOT-COMPOSABLE (strict half needs nlinarith).

**Rationale:**

The statement is true, sharp and not in mathlib, and it is not a ≤3-call composition, so neither NO bucket fits. But the YES case is weak: no literature presence as a named fact, the conjunction bundles an existing mathlib lemma (`Nat.floor_le`), and the genuinely new half `√X < ⌊X⌋₊` for `2 ≤ X` is an ad-hoc numeric estimate of the kind mathlib generally does not collect (no TODO or recurring re-derivation in mathlib points to it). The decision is therefore a taste/policy call between "keep project-local" (recommended) and "upstream the strict half to Mathlib/Analysis/Real/Sqrt.lean next to `Real.real_sqrt_lt_nat_sqrt_succ`".

Belongs-elsewhere: project-local, Roth/MainLemma.lean, where it encodes the source's B₁ estimate for 3 call sites.

Numbered questions:
  1. Keep `Roth.sqrt_lt_floor` project-local as the source's B₁ estimate (recommended: yes)?
  2. If upstreaming is wanted, ship only the strict half (e.g. `Real.sqrt_lt_natFloor {x : ℝ} (hx : 2 ≤ x) : √x < ⌊x⌋₊`) in Mathlib/Analysis/Real/Sqrt.lean, without the `∧ Nat.floor_le` half?
  3. Locally, should the private `sqrt_lt_nat_floor_aux` be made public so the two `.1`-only callers (MainLemma l.154, l.201) use it directly, keeping the pair only for Main l.494?

Next action: user answers; default is keep project-local with no change.

---

### Next step

Keep `Roth.sqrt_lt_floor` in Roth/MainLemma.lean (callers MainLemma l.154, l.201, Main l.494); no upstream PR unless question 2 is answered yes, in which case upstream only the strict half to Mathlib/Analysis/Real/Sqrt.lean.

## Evidence
- `grep -rn sqrt_lt_floor Roth/`: definition l.115; uses MainLemma l.154, l.201; Main l.494.
- lean_loogle `Real.sqrt _ < ((Nat.floor _ : ℕ) : ℝ)`: no results. lean_leansearch and lean_leanfinder: no matching lemma (listed in Phase 5).
- grep of `.lake/packages/mathlib/Mathlib/`: no `sqrt`/`floor` lemma of this shape; building blocks located (Phase 5 [D]); no `namespace Roth`.
- WebSearch x3 (Phase 3 rows 1–3): no standalone statement.
- clean.tex l.1368, l.1383: source statement (with `X > 4`).
- Evidence file `.mathlib-quality/overview/evidence/Roth.sqrt_lt_floor/checks.lean` (`lake env lean`, compiles cleanly, one run after a one-token fix): (1) mathlib-only proof of the full statement; (2) `X = 1` counterexample to the strict half; (3) upper half needs only `0 ≤ X`; (4) `2 - 1 < √2`, so the `Nat.sub_one_lt_floor` route fails at `X = 2`.
