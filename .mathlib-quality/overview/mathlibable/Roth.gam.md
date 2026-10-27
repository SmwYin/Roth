---
decl: Roth.gam
file: Roth/MainLemma.lean
line: 63
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: gam is the Roth-proof parameter γ = (m - λ)/2 of the source's eq. (35), a one-line real expression over Roth.lam with no general mathematical content; nothing to upstream, kept locally as the paper's named parameter used in the statements of main_lemma and exists_delta.
action: Do not upstream; keep Roth.gam in Roth/MainLemma.lean as the paper's γ (consumers: eta_lt_gam_iff MainLemma.lean:101, private auxiliaries MainLemma.lean:623/648/699, main_lemma MainLemma.lean:743-753, exists_delta Main.lean:230-244, private Main.lean:414/463); no call-site changes.
---

# Roth.gam

## Inventory entry

### `def Roth.gam`
- **Type**: `(δ : ℝ) (n m : ℕ) : ℝ`, defined as `((m : ℝ) - lam δ n m) / 2`
- **What**: the parameter `γ = (m - λ)/2` of §6 of the source (clean.tex eq. (35), l.1342–1345); the target lower bound on the index of the auxiliary polynomial `W*` at `(α, …, α)` before differentiation, and `γ - η` the index bound in Roth's Lemma 9.
- **How**: direct term; one line of real arithmetic over `Roth.lam` and the cast `ℕ → ℝ`.
- **Hypotheses**: none (total function; meaningful for `δ ≥ 0`, `m > 16 n²`).
- **Uses from project**: `Roth.lam`
- **Used by**: `Roth.eta_lt_gam_iff` (Roth/MainLemma.lean:101–102, statement and `grind [gam, lam]`); private `Roth.exists_mem_RSet_le_index_of_log_bound_aux` (MainLemma.lean:623 statement, :638 `simpa only [gam, lam]`); private `Roth.exists_auxiliary_polynomial_of_log_bound_aux` (MainLemma.lean:648); private `Roth.exists_auxiliary_polynomial_with_index_gap_aux` (MainLemma.lean:699); `Roth.main_lemma` (MainLemma.lean:743, :750, :753); `Roth.exists_delta` (Roth/Main.lean:230, :233, :236 continuity via defeq `show`, :244 `simpa [gam, lam, eta, ...]`); private `Roth.exists_roth_parameters_aux` (Main.lean:414); private `Roth.one_lt_roth_eval_bound_aux` (Main.lean:463); module docstring MainLemma.lean:33.
- **Visibility**: public
- **Lines**: 62–63 (docstring 62, definition 63), proof length 0 lines (one-line body)
- **Notes**: listed under `## Main definitions` of Roth/MainLemma.lean; appears folded in the public statements of `main_lemma` and `exists_delta`.

## Junk check (Step 8)
- Used anywhere? Yes: in the statements of 7 declarations across 2 files (incl. the public `main_lemma`, `exists_delta`, `eta_lt_gam_iff`).
- Wrapper of 1–2 mathlib calls? No; a one-line arithmetic expression.
- Does mathlib have it? No (Phase 5): a paper-specific constant.
- Too specific (inline?)? Inlining would bloat the statements of `main_lemma` and `exists_delta` and lose the eq. (35) correspondence; it is a genuine named parameter of the paper.
- Well-chosen definition? Yes; matches the source exactly, total.
- Conclusion: `KEEP`. No action.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring starts "The parameter"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `namespace Roth`, `def gam`, `Roth.gam`: no hit. Not a glue lemma (it is a def; its parent `Roth.lam` was assessed NO-composable-from-mathlib, but `gam` is a separate def, so a full run follows). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule)
- decl `Roth.gam`:           resolved at Roth/MainLemma.lean:63
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  §6 of the source: the main lemma (Roth's Lemma 9), its parameters λ, γ, η, B_1 and the pigeonhole step

### Statement (Phase 1)

`Roth.gam` is a definition of the following:

For a real `δ` and natural numbers `n, m`, `γ(δ, n, m) = (m - λ(δ, n, m))/2` where `λ = 4(1 + 3δ) n √m`. In the Cassels/Ridout-style proof of Roth's theorem, the auxiliary polynomial `W*` is constructed (by pigeonhole) to vanish to index at least `γ` at `(α, …, α)`; after differentiation the polynomial `Q` of Lemma 9 has index at least `γ - η > 0`.

Variables / typeclasses involved (Lean side):
- `δ : ℝ`: the small parameter.
- `n : ℕ`: degree of α.
- `m : ℕ`: number of variables.

Hypotheses (Lean side): none.

Conclusion (math): n/a — definition.

Conclusion (Lean): n/a — definition.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: listed under `## Main definitions`, but it is a numeric parameter, not a new mathematical structure or concept.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                 | no       | consumers unfold explicitly (`grind [gam, lam]`, `simpa only [gam, lam]`, `simpa [gam, lam, eta, ...]`) or rely on defeq through `show` (Main.lean:236); no barrier role |
| Avoid typeclass diamonds          | no       | a real number, no instance involved |
| Mark semantic intent / API name   | yes (project-local) | names the paper's γ of eq. (35) in the statements of `main_lemma` (MainLemma.lean:743) and `exists_delta` (Main.lean:230); benefit is paper correspondence and readable statements inside the project only, no mathlib consumer |

Conclusion: ONE-LINER WITH-EXEMPTION (project-local naming only; no mathlib-level exemption)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof gamma = (m - lambda)/2 index auxiliary polynomial main lemma | no | n/a | no indexed source states γ = (m − λ)/2; hits arXiv 1806.10737, math/0307203, Evertse Luminy notes, Maculan notes, minru roth.pdf |
| 2 | WebSearch (general form) | Roth's theorem proof index of auxiliary polynomial at least m(1/2 - epsilon) lattice points j_1/r_1 + ... + j_m/r_m | partial | auxiliary polynomial with index ≥ (m/2)(1 − ε) at (α,…,α) (arXiv 2502.00731) | the general role of γ (index ≈ m/2 minus a lower-order term); normalisation is presentation-specific |
| 3 | WebSearch (aliases) | Cassels Introduction to Diophantine Approximation Roth Lemma 9 gamma eta parameters | partial | arXiv 2502.00731 uses η, weights r̄ with different conventions; Cassels text not indexed | confirms γ is local bookkeeping, not a named concept |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `gamma` / eq. (35) | yes | eq. (35) `γ = (m − λ)/2` (l.1342–1345); used at l.1358 (eq. (38) `η < γ`), l.1396, l.1430, l.1492, l.1511, l.1537 | exact match with the Lean body |
| 6 | nLab | Roth's theorem parameters | no | n/a | nLab has no entry on Roth's proof constants |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | numeric Diophantine parameter, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread about this constant |
| 10 | recent arXiv | 2502.00731, math/0307203, 1806.10737 | partial | as #2, #3 | each proof uses its own constants |

### Literature summary (Phase 3)

Concept identified as: the index target γ of the main lemma in the Cassels/Ridout-style proof of Roth's theorem (source eq. (35)); not a named mathematical concept.
Sources agree on the standard form: no — expositions choose their own normalisation (e.g. `(m/2)(1 − ε)` in arXiv 2502.00731).
Most general standard form: none; γ is presentation-specific bookkeeping.
Generality dimensions where the literature varies:
  - normalisation of the subtracted lower-order term: proof-specific.
Disagreement with the literature: none; matches the source exactly.

### Generality analysis — `Roth.gam`

Literature-standard form (from Phase 3): source eq. (35), `γ = (m − λ)/2`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `δ : ℝ` | real | real | no | the real parameter of the proof |
| 2 | `n m : ℕ` | naturals cast to ℝ | positive integers | no | already total over ℕ |
| 3 | codomain | ℝ | ℝ | no | λ involves √m |

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

### Proof strategy — `Roth.gam`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | definition, no proof | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | — | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (n/a for a definition with no proof; the body is the source formula verbatim)

### Diamond / defeq risk — `Roth.gam`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | value in ℝ; no instance introduced |
| 2 | Reducibility leak | none | plain semireducible def; `exists_delta` (Main.lean:236) uses defeq through `show` deliberately, all others unfold explicitly |
| 3 | Non-canonical unfolding | none | not `@[simp]`; unfolds only on request |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | all arguments in `Type` (ℝ, ℕ) |
| 6 | Coercion ambiguity | none | only the standard `ℕ → ℝ` cast |

### Risk verdict (Phase 4.5)

Overall risk: NONE
Top risks: none
Recommended mitigations: none

### Mathlib search-status: `Roth.gam`

[A] Lean-Finder       "real parameter (m - 4(1+3δ) n √m)/2 in Roth's theorem main lemma"   hits: `rothNumberNat_le`, `cornersTheoremBound`, `rothNumberNat_def`, `rothNumberNat_spec`, `ThreeAPFree.le_rothNumberNat` — unrelated (additive-combinatorics Roth)
[B] Loogle            `Real → ℕ → ℕ → ℝ, Real.sqrt, HDiv.hDiv`   no hits
[C] LeanSearch        "half of m minus lambda, parameter gamma in proof of Roth's theorem on Diophantine approximation"   hits: `Behrend.roth_lower_bound`, `Behrend.bound_aux`, `rothNumberNat_add_le` — unrelated
[D] Grep mathlib src  `namespace Roth`, `def gam`, `Roth.gam`   no hits
[E] Name pattern      `Roth.gam` via lean_local_search   n/a: tool failed (ripgrep not on PATH); covered by [D] grep

Searched for both:
  - the user's current form (γ = (m − λ)/2)
  - the literature-standard form (Roth-proof index target; none standard)

Concluded: found building blocks (`Roth.lam` itself composed from `Real.sqrt`, `Nat.cast`, ring/field operations on ℝ); composition yields our form; not in mathlib as a named constant (all 5 methods).

### Normal-form check — `Roth.gam`

Equivalent formalisms this statement could take: `((m : ℝ) - lam δ n m) / 2` (current); `m / 2 - 2 * (1 + 3 * δ) * n * √m`; `(m - lam δ n m) * (1/2)`.
Does mathlib already have a canonical form for this idea? no (no such constant).
Proposed canonical form: current (verbatim eq. (35)).
RHS convention respected? n/a (definition).

### Syntactic generality — `Roth.gam`

Alternative restatements attempted:
- current (in terms of `lam`)
- fully expanded `m / 2 - 2 * (1 + 3 * δ) * n * √m`
- inlining into every statement

Chosen restatement: current.
Justification: mirrors eq. (35); `eta_lt_gam_iff` already provides the bridge to the expanded eq. (30) shape used by callers.

### Superfluous-argument audit — `Roth.gam`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `δ` | yes | through `lam` |
| 2 | `n` | yes | through `lam` |
| 3 | `m` | yes | in the body and through `lam` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; not proposed for mathlib)

### Call sites — `Roth.gam`

Internal use count: 6 lines in Roth/Main.lean (3 declarations) outside the declaring file; 9 further lines (5 declarations) in Roth/MainLemma.lean
External-to-file callers: 1 distinct file (Roth/Main.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:101 | `eta δ m < gam δ n m` (statement of `eta_lt_gam_iff`) |
| Roth/MainLemma.lean:102 | `grind [gam, lam]` |
| Roth/MainLemma.lean:623 | `gam δ f.natDegree m ≤ index ...` (private `exists_mem_RSet_le_index_of_log_bound_aux`) |
| Roth/MainLemma.lean:638 | `simpa only [gam, lam] using ...` |
| Roth/MainLemma.lean:648 | `gam δ f.natDegree m ≤ index ...` (private `exists_auxiliary_polynomial_of_log_bound_aux`) |
| Roth/MainLemma.lean:699 | `gam δ f.natDegree m - eta δ m + Θ ...` (private `exists_auxiliary_polynomial_with_index_gap_aux`) |
| Roth/MainLemma.lean:743 | `gam δ f.natDegree m - eta δ m < index ...` (statement of `main_lemma`) |
| Roth/MainLemma.lean:750 | `(gam δ f.natDegree m - eta δ m) + Θ ...) / 2` (`main_lemma` proof) |
| Roth/MainLemma.lean:753 | `(γ := gam δ f.natDegree m - eta δ m + c)` (`main_lemma` proof) |
| Roth/Main.lean:230 | `(m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ` (statement of `exists_delta`) |
| Roth/Main.lean:233 | same expression in `ContinuousAt` goal |
| Roth/Main.lean:236 | `show ContinuousAt (fun δ ↦ gam δ n m) 0 from ...` (defeq unfolding) |
| Roth/Main.lean:244 | `simpa [gam, lam, eta, ...]` |
| Roth/Main.lean:414 | `... / (gam δ f.natDegree m - eta δ m) < κ` (private `exists_roth_parameters_aux`) |
| Roth/Main.lean:463 | `(q 0 : ℝ) ^ (-(r 0 : ℝ) * (gam δ f.natDegree m - eta δ m) * κ)` (private `one_lt_roth_eval_bound_aux`) |

Inline-derivation grep: the expression `m / 2 - 2 * (1 + 3 * δ) * n * √m` does not appear inline; the eq. (30) phrasing in `exists_delta_bound` / `eta_lt_gam_iff` / `exists_delta` is the paper's own and is bridged by `eta_lt_gam_iff`. (none)

### Composition check (Phase 6)

Can `Roth.gam` be derived from mathlib in ≤3 chained calls?

Attempt 1: `fun δ n m ↦ ((m : ℝ) - 4 * (1 + 3 * δ) * n * Real.sqrt m) / 2`
  - Mathlib decls used: `Real.sqrt`, `Nat.cast`, `HSub`/`HMul`/`HDiv` on ℝ
  - Result: succeeds (this is the body with `lam` unfolded)
  - Notes: none

Conclusion: COMPOSABLE

## Verdict: `Roth.gam`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): γ is the source's eq. (35) bookkeeping constant; no exposition treats it as a concept.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (nothing to weaken).
- Mathlib search (Phase 5): not in mathlib; building blocks `Real.sqrt`, `Nat.cast`, field operations (via `Roth.lam`).
- Composition check (Phase 6): COMPOSABLE (one mathlib-term expression).

**Rationale:**

`Roth.gam` is a one-line numeric constant specific to one presentation of Roth's theorem. It has no mathematical content beyond its formula, so mathlib would never want it; it is already "composed from mathlib" arithmetic. Same treatment as its parent `Roth.lam` (NO-composable-from-mathlib, kept locally).

WHY not: mathlib's building blocks (`Real.sqrt` in Mathlib/Analysis/Real/Sqrt.lean, `Nat.cast`, field operations on ℝ) give the expression directly. Belongs-elsewhere check: it belongs where it is, in Roth/MainLemma.lean, as the paper's named γ; unlike `lam`, it appears folded in the public statements of `main_lemma` and `exists_delta`, so inlining would actively hurt readability.

Mathlib building blocks: `Real.sqrt`, `Nat.cast`, field operations on `ℝ` (plus project `Roth.lam`).
Composition sketch:
```lean
example (δ : ℝ) (n m : ℕ) : Roth.gam δ n m = ((m : ℝ) - 4 * (1 + 3 * δ) * n * Real.sqrt m) / 2 := rfl
```
Call sites in our project (from Phase 6.0): 15 lines in 8 declarations (MainLemma.lean:101, 102, 623, 638, 648, 699, 743, 750, 753; Main.lean:230, 233, 236, 244, 414, 463).
Refactor plan: none recommended. (Mechanically possible: replace `gam δ n m` by its body at those sites; rejected because it bloats the `main_lemma` / `exists_delta` statements and loses the eq. (35) correspondence.)
Next action: do not upstream; keep `Roth.gam` in Roth/MainLemma.lean; no call-site changes.

## Next step

Do not upstream; keep `Roth.gam` as the paper's γ in Roth/MainLemma.lean; no call-site changes.

## Evidence
- WebSearch ×3 (queries in the literature table); local reference clean.tex l.1342–1345 (eq. (35)), 1358, 1396, 1430, 1492, 1511, 1537.
- lean_leanfinder, lean_leansearch, lean_loogle queries as recorded in Phase 5 (no relevant hit); lean_local_search failed (ripgrep not on PATH), replaced by grep over `.lake/packages/mathlib/Mathlib/` (no hit for `namespace Roth`, `def gam`, `Roth.gam`).
- `grep -rn gam Roth/` for call sites, enclosing declarations located by scanning back to the nearest declaration head. No Lean experiments were needed (no weakening proposed; the composition sketch is the definitional body); no evidence files written.
