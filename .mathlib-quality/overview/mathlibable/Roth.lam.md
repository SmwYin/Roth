---
decl: Roth.lam
file: Roth/MainLemma.lean
line: 60
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: lam is the Roth-proof parameter λ = 4(1+3δ) n √m of the source's eq. (34), a single arithmetic expression in mathlib's Real.sqrt and ring operations with no general mathematical content; nothing to upstream, kept locally only as the paper's named parameter.
action: Do not upstream; keep Roth.lam in Roth/MainLemma.lean as the paper's λ (consumers: def Roth.gam at MainLemma.lean:63 and the unfoldings grind/simp [gam, lam] at MainLemma.lean:102 eta_lt_gam_iff, MainLemma.lean:638 private exists_mem_RSet_le_index_of_log_bound_aux, Main.lean:244 exists_delta); no call-site changes.
---

# Roth.lam

## Inventory entry

### `def Roth.lam`
- **Type**: `(δ : ℝ) (n m : ℕ) : ℝ`, defined as `4 * (1 + 3 * δ) * n * √(m : ℝ)`
- **What**: the parameter `λ = 4(1 + 3δ) n m^{1/2}` of §6 of the source (clean.tex eq. (34), l.1337–1341), used to define `γ = (m - λ)/2`.
- **How**: direct term; one line of real arithmetic using `Real.sqrt` and casts `ℕ → ℝ`.
- **Hypotheses**: none (total function; meaningful for `δ ≥ 0`, `m > 16 n²` in the source).
- **Uses from project**: `[]`
- **Used by**: `Roth.gam` (Roth/MainLemma.lean:63, definition body); `Roth.eta_lt_gam_iff` (Roth/MainLemma.lean:102, `grind [gam, lam]`); private `Roth.exists_mem_RSet_le_index_of_log_bound_aux` (Roth/MainLemma.lean:638, `simpa only [gam, lam]`); `Roth.exists_delta` (Roth/Main.lean:244, `simpa [gam, lam, eta, ...]`); mentioned in the module docstring Roth/MainLemma.lean:33. No other occurrence in `Roth/` (the `lam` identifiers in Roth/Lattice.lean are unrelated local variables).
- **Visibility**: public
- **Lines**: 59–60 (docstring 59, definition 60), proof length 0 lines (one-line body)
- **Notes**: listed under `## Main definitions` of Roth/MainLemma.lean. Never used except through `gam` or unfolded together with `gam`.

## Junk check (Step 8)
- Used anywhere? Yes: in the definition of `gam` and unfolded at three proof sites (MainLemma.lean:102, :638, Main.lean:244).
- Wrapper of 1–2 mathlib calls? It is a one-line arithmetic expression (`*`, `+`, `Real.sqrt`), not a mathlib-lemma wrapper.
- Does mathlib have it? No (Phase 5): a paper-specific constant.
- Too specific (inline?)? It could be inlined into `gam` (every proof site unfolds both), but it is the source's named parameter λ of eq. (34) and listed as a main definition; keeping it preserves the paper correspondence at zero cost.
- Well-chosen definition? Yes; matches the source exactly, total, no junk values that matter.
- Conclusion: `KEEP`. No action.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring starts "The parameter"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `namespace Roth`, `def lam`, `Roth.lam`: no hit. Not a glue lemma. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule)
- decl `Roth.lam`:           resolved at Roth/MainLemma.lean:60
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  §6 of the source: the main lemma (Roth's Lemma 9), its parameters λ, γ, η, B_1 and the pigeonhole step

### Statement (Phase 1)

`Roth.lam` is a definition of the following:

For a real `δ` and natural numbers `n, m`, `λ(δ, n, m) = 4(1 + 3δ) n √m`. In Roth's proof (Cassels/Ridout presentation) this is the width parameter for which the lattice-point count `#{j ≤ r : Σ j_h/r_h ≤ (m - λ)/2} ≤ 2√m λ^{-1} ∏(r_h + 1)` makes the number of derivative conditions at most `r/(2(1+3δ)n)`, so that Siegel's lemma / pigeonhole applies.

Variables / typeclasses involved (Lean side):
- `δ : ℝ`: the small parameter of the proof.
- `n : ℕ`: degree of the algebraic number α.
- `m : ℕ`: number of variables.

Hypotheses (Lean side): none.

Conclusion (math): n/a — definition.

Conclusion (Lean): n/a — definition.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: listed under `## Main definitions`, but it is a numeric parameter (one arithmetic expression), not a new mathematical structure or concept.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                 | no       | every consumer unfolds it explicitly (`grind [gam, lam]`, `simpa only [gam, lam]`, `simpa [gam, lam, eta, ...]`); no proof relies on it staying folded |
| Avoid typeclass diamonds          | no       | a real number, no instance involved |
| Mark semantic intent / API name   | yes (project-local) | names the source's λ of eq. (34) for `gam`; benefit is paper correspondence inside the project only, no mathlib consumer |

Conclusion: ONE-LINER WITH-EXEMPTION (project-local naming only; no mathlib-level exemption)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem proof parameter lambda = 4(1+3delta) n m^{1/2} main lemma Cassels | no | n/a | results are additive-combinatorics Roth theorems; the specific constant is not stated in any indexed source |
| 2 | WebSearch (general form) | Roth theorem proof auxiliary polynomial index bound "m - lambda" weight lattice point count parameters gamma eta | partial | general structure: choose ε, m, weights; auxiliary polynomial vanishing to index ≥ m(1/2 - ε) (arXiv 2502.00731, Evertse Luminy notes, minru/fields roth.pdf) | each exposition picks its own parameter normalisation; λ as such is presentation-specific |
| 3 | WebSearch (aliases) | Ridout p-adic Roth theorem proof Lemma 9 parameters lambda gamma eta delta | partial | Yamada arXiv math/0307203 (Roth–Ridout, parameters κ, a₀, a₁, λ with different meaning) | confirms λ is a local bookkeeping constant, not a named concept |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `lambda` / eq. (34) | yes | eq. (34) `λ = 4(1+3δ)nm^{1/2}` (l.1337–1341); used at l.1435 (`D ≤ 2m^{1/2}λ^{-1}r`) and l.1483 | exact match with the Lean body |
| 6 | nLab | Roth's theorem parameters | no | n/a | nLab has no entry on Roth's proof constants |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | numeric Diophantine parameter, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread about this constant |
| 10 | recent arXiv | 2502.00731, math/0307203, 1806.10737, 2601.11376 | partial | as #2, #3 | each proof uses its own constants |

### Literature summary (Phase 3)

Concept identified as: the parameter λ of the main lemma in the Cassels/Ridout-style proof of Roth's theorem (source eq. (34)); not a named mathematical concept.
Sources agree on the standard form: no — every exposition of Roth's theorem chooses its own parameters (Bombieri–Gubler use ε, η with `2mη`; Yamada uses κ, a₀, a₁, λ differently).
Most general standard form: none; λ is presentation-specific bookkeeping.
Generality dimensions where the literature varies:
  - constant factors and normalisation: proof-specific.
Disagreement with the literature: none; matches the source exactly.

### Generality analysis — `Roth.lam`

Literature-standard form (from Phase 3): source eq. (34), `λ = 4(1+3δ) n m^{1/2}`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `δ : ℝ` | real | real | no | the real parameter of the proof |
| 2 | `n m : ℕ` | naturals cast to ℝ | positive integers | no | already total over ℕ; casting is the natural shape for callers |
| 3 | codomain | ℝ | ℝ | no | √m requires ℝ |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (a concrete numeric definition; no hypotheses or typeclasses to weaken)
Number of weakening opportunities found: 0 (nothing proposed, so nothing needed compiling)
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | no hypotheses | — |
| 2 | Sequences vs filters? | no | a number | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | √ needs ℝ | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | `n m : ℕ` are counts | — |
| 8 | Concrete-via-abstract? | no | no proof body | — |
| 9 | False-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - Reason: a paper-specific numeric constant; nothing to reorganise.

### Proof strategy — `Roth.lam`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | definition, no proof | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | — | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (n/a for a definition with no proof; the body is the source formula verbatim)

### Diamond / defeq risk — `Roth.lam`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | value in ℝ; no instance introduced |
| 2 | Reducibility leak | none | plain (semireducible) def, not `@[reducible]`; consumers unfold explicitly |
| 3 | Non-canonical unfolding | none | not `@[simp]`; unfolds only on request (`simp only [lam]`, `grind [lam]`) |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | all arguments in `Type` (ℝ, ℕ) |
| 6 | Coercion ambiguity | none | only the standard `ℕ → ℝ` cast; no CoeFun/CoeSort |

### Risk verdict (Phase 4.5)

Overall risk: NONE
Top risks: none
Recommended mitigations: none

### Mathlib search-status: `Roth.lam`

[A] Lean-Finder       "real parameter defined as constant times n times square root of m, Roth theorem main lemma"   hits: `cornersTheoremBound`, `rothNumberNat_le`, `rothNumberNat_def`, `SzemerediRegularity.bound`, `Behrend.roth_lower_bound` — unrelated (additive-combinatorics Roth)
[B] Loogle            `Real → ℕ → ℕ → ℝ, Real.sqrt`   no hits
[C] LeanSearch        "4 * (1 + 3 * δ) * n * Real.sqrt m parameter in Roth's theorem"   hits: `Behrend.roth_lower_bound`, `rothNumberNat`, `roth_3ap_theorem_nat`, `Behrend.bound_aux` — unrelated
[D] Grep mathlib src  `namespace Roth`, `def lam`, `Roth.lam`   no hits
[E] Name pattern      `Roth.lam` via lean_local_search   n/a: tool failed (ripgrep not on PATH); covered by [D] grep

Searched for both:
  - the user's current form (λ = 4(1+3δ) n √m)
  - the literature-standard form (Roth-proof parameter; none standard)

Concluded: found building blocks (`Real.sqrt`, `Nat.cast`, ring operations on ℝ); composition yields our form; not in mathlib as a named constant (all 5 methods).

### Normal-form check — `Roth.lam`

Equivalent formalisms this statement could take: `4 * (1 + 3 * δ) * n * √m` (current); `4 * (1 + 3 * δ) * n * m ^ (1/2 : ℝ)`.
Does mathlib already have a canonical form for this idea? no (no such constant); `√` is mathlib's canonical spelling of the square root.
Proposed canonical form: current.
RHS convention respected? n/a (definition).

### Syntactic generality — `Roth.lam`

Alternative restatements attempted:
- current (`√(m : ℝ)`)
- `rpow` spelling `(m : ℝ) ^ (1/2 : ℝ)`
- inlining into `gam`

Chosen restatement: current.
Justification: `√` composes with `Real.sq_sqrt`, `Real.sqrt_pos` used throughout the callers (e.g. `exists_delta_bound`); a separate name mirrors eq. (34).

### Superfluous-argument audit — `Roth.lam`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `δ` | yes | appears in the body |
| 2 | `n` | yes | appears in the body |
| 3 | `m` | yes | appears in the body |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; not proposed for mathlib)

### Call sites — `Roth.lam`

Internal use count: 4 (MainLemma.lean is the declaring file; 1 external-file use)
External-to-file callers: 1 distinct file (Roth/Main.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:63 | `def gam ... := ((m : ℝ) - lam δ n m) / 2` |
| Roth/MainLemma.lean:102 | `grind [gam, lam]` (in `eta_lt_gam_iff`) |
| Roth/MainLemma.lean:638 | `simpa only [gam, lam] using ...` (private `exists_mem_RSet_le_index_of_log_bound_aux`) |
| Roth/Main.lean:244 | `simpa [gam, lam, eta, Real.zero_rpow ...]` (in `exists_delta`) |

Inline-derivation grep: the expression `2 * (1 + 3 * δ) * n * √(m : ℝ)` (= λ/2) appears inline in the statements of `exists_delta_bound` and `eta_lt_gam_iff` (source eq. (30) is phrased that way in the paper); this is the paper's own phrasing, not a missed reuse.

### Composition check (Phase 6)

Can `Roth.lam` be derived from mathlib in ≤3 chained calls?

Attempt 1: `fun δ n m ↦ 4 * (1 + 3 * δ) * (n : ℝ) * Real.sqrt m`
  - Mathlib decls used: `Real.sqrt`, `Nat.cast`, `HMul`/`HAdd` on ℝ
  - Result: succeeds (this is literally the body)
  - Notes: none

Conclusion: COMPOSABLE

## Verdict: `Roth.lam`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): λ is the source's eq. (34) bookkeeping constant; no exposition treats it as a concept, constants vary by presentation.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (nothing to weaken).
- Mathlib search (Phase 5): not in mathlib; building blocks `Real.sqrt`, `Nat.cast`, ring operations.
- Composition check (Phase 6): COMPOSABLE (the body is one mathlib-term expression).

**Rationale:**

`Roth.lam` is a one-line numeric constant specific to one presentation of Roth's theorem. It has no mathematical content beyond its own formula, so mathlib would never want it; mathematically it is already "composed from mathlib" (`Real.sqrt` and arithmetic). Same treatment as `Roth.Θ` (NO-composable-from-mathlib, kept locally).

WHY not: mathlib's building blocks (`Real.sqrt` in Mathlib/Analysis/Real/Sqrt.lean, `Nat.cast`) give the expression directly. Belongs-elsewhere check: it belongs exactly where it is, in Roth/MainLemma.lean, as the paper's named λ consumed by `gam`; inlining would be mechanical but loses the eq. (34) correspondence and buys nothing.

Mathlib building blocks: `Real.sqrt`, `Nat.cast`, ring operations on `ℝ`.
Composition sketch:
```lean
example (δ : ℝ) (n m : ℕ) : Roth.lam δ n m = 4 * (1 + 3 * δ) * n * Real.sqrt m := rfl
```
Call sites in our project (from Phase 6.0): 4 (MainLemma.lean:63, :102, :638; Main.lean:244).
Refactor plan: optional only — replace `lam δ n m` by its body in `gam` (MainLemma.lean:63) and drop `lam` from the unfolding lists at MainLemma.lean:102, :638 and Main.lean:244. Not recommended (paper correspondence).
Next action: do not upstream; keep `Roth.lam` in Roth/MainLemma.lean; no call-site changes.

## Next step

Do not upstream; keep `Roth.lam` as the paper's λ in Roth/MainLemma.lean; no call-site changes.

## Evidence
- WebSearch ×3 (queries in the literature table); local reference clean.tex l.1337–1341, 1435, 1483.
- lean_leansearch, lean_leanfinder, lean_loogle queries as recorded in Phase 5 (no relevant hit); lean_local_search failed (ripgrep not on PATH), replaced by grep over `.lake/packages/mathlib/Mathlib/` (no hit).
- `grep -rnw lam Roth/` for call sites. No Lean experiments were needed (no weakening proposed; the composition sketch is the definitional body); no evidence files written.
