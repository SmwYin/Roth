---
decl: Roth.mainCoeffBound
file: Roth/MainLemma.lean
line: 69
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: mainCoeffBound is the Roth-proof coefficient bound B_1 = floor(q_1^(δ r_1)) of the source's eq. (37), a one-line Nat.floor of a real power with no general mathematical content; nothing to upstream, kept locally as the paper's named B_1 used in main_lemma and its helpers.
action: Do not upstream; keep Roth.mainCoeffBound in Roth/MainLemma.lean (consumers MainLemma.lean:149-151/182-205/622-639/650-651/702/746, Main.lean:462/484-486); no refactor recommended.
---

# Roth.mainCoeffBound

## Inventory entry

### `def Roth.mainCoeffBound`
- **Type**: `(δ : ℝ) (q₁ r₁ : ℕ) : ℕ`, defined as `⌊(q₁ : ℝ) ^ (δ * r₁)⌋₊`
- **What**: the integer coefficient bound `B_1 = [q_1^{δ r_1}]` of §6 of the source (clean.tex eq. (37), l.1351–1353); the coefficients of the box polynomials in the pigeonhole family `𝒲` range over `[0, B_1]`, and the Hasse derivatives of the auxiliary polynomial are bounded by `B_1^{1+3δ}`.
- **How**: direct term; `Nat.floor` of the real power `Real.rpow (q₁ : ℝ) (δ * r₁)`.
- **Hypotheses**: none (total; for `q₁^{δ r₁} < 0` impossible, `Nat.floor` gives 0 below 1).
- **Uses from project**: `[]`
- **Used by**: `Roth.mul_log_div_two_lt_log_mainCoeffBound` (Roth/MainLemma.lean:149–151, statement and `simpa [mainCoeffBound, ...]`); `Roth.three_small_factors` (MainLemma.lean:182–184 statement, :197–205 proof); private `Roth.exists_mem_RSet_le_index_of_log_bound_aux` (MainLemma.lean:622, 633–634, 639); private `Roth.exists_auxiliary_polynomial_of_log_bound_aux` (MainLemma.lean:650–651); private `Roth.exists_auxiliary_polynomial_with_index_gap_aux` (MainLemma.lean:702); `Roth.main_lemma` (MainLemma.lean:746); private `Roth.one_lt_roth_eval_bound_aux` (Roth/Main.lean:462); private `Roth.roth_product_bound_aux` (Main.lean:484–486); module docstring MainLemma.lean:34.
- **Visibility**: public
- **Lines**: 68–69 (docstring 68, definition 69), proof length 0 lines (one-line body)
- **Notes**: the underlying real `X = (q₁ : ℝ) ^ (δ * r₁)` is also spelled inline as the real `RSet`/`Θ` bound (MainLemma.lean:123, 157, 647, 676, 698–699, 750; Main.lean:508); that is the unfloored quantity, a different object, so not a re-derivation of `mainCoeffBound`.

## Junk check (Step 8)
- Used anywhere? Yes: statements of 8 declarations across 2 files, including the public `main_lemma`, `three_small_factors`, `mul_log_div_two_lt_log_mainCoeffBound`.
- Wrapper of 1–2 mathlib calls? It is a one-line term (`Nat.floor` ∘ `Real.rpow`), not a lemma wrapper.
- Does mathlib have it? No (Phase 5): a paper-specific constant.
- Too specific (inline?)? Inlining `⌊(q 0 : ℝ) ^ (δ * r 0)⌋₊` into `main_lemma` and the helpers would lengthen the statements and lose the eq. (37) correspondence; the name also serves as the hook for `mul_log_div_two_lt_log_mainCoeffBound` and `three_small_factors`.
- Well-chosen definition? Yes; matches the source exactly; codomain ℕ is right because it bounds integer coefficient ranges (`boxFamily`).
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring starts "The coefficient bound"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `namespace Roth` / `mainCoeffBound`: no hit. Not a glue lemma (it is a def; siblings `Roth.lam`, `Roth.gam`, `Roth.eta` were assessed NO-composable-from-mathlib, but this is an independent def), so a full run follows.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule)
- decl `Roth.mainCoeffBound`: resolved at Roth/MainLemma.lean:69
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  §6 of the source: the main lemma (Roth's Lemma 9), its parameters λ, γ, η, B_1 and the pigeonhole step

### Statement (Phase 1)

`Roth.mainCoeffBound` is a definition of the following:

For a real `δ` and natural numbers `q₁, r₁`, `B_1(δ, q₁, r₁) = ⌊q₁^{δ r₁}⌋ ∈ ℕ`. In the Cassels-style proof of Roth's theorem, the auxiliary polynomial `W*` is a difference of two box polynomials with coefficients in `[0, B_1]`; `B_1` is large (`log B_1 > δ r₁ log q₁ / 2`), which absorbs the factors `2^{m r₁}`, `(1+A)^{m r₁}`, `(1+|α|)^{m r₁}` into `B_1^δ`.

Variables / typeclasses involved (Lean side):
- `δ : ℝ`: the small parameter.
- `q₁ : ℕ`: denominator of the first rational approximation.
- `r₁ : ℕ`: first degree bound.

Hypotheses (Lean side): none.

Conclusion (math): n/a — definition.

Conclusion (Lean): n/a — definition.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: listed under `## Main definitions`, but it is a numeric parameter, not a mathematical structure or concept.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                 | no       | consumers unfold explicitly (`simpa [mainCoeffBound, ...]` at MainLemma.lean:151); otherwise only used through the lemmas `mul_log_div_two_lt_log_mainCoeffBound` / `three_small_factors`; no barrier role |
| Avoid typeclass diamonds          | no       | a natural number, no instance involved |
| Mark semantic intent / API name   | yes (project-local) | names the paper's B_1 of eq. (37) in the statements of `main_lemma` (MainLemma.lean:746), `three_small_factors` (:182–184), `mul_log_div_two_lt_log_mainCoeffBound` (:150); benefit is paper correspondence inside the project only, no mathlib consumer |

Conclusion: ONE-LINER WITH-EXEMPTION (project-local naming only; no mathlib-level exemption)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof coefficient bound B_1 = [q_1^{delta r_1}] auxiliary polynomial Cassels | no | n/a | no indexed text states B_1 = [q_1^{δ r_1}]; hits arXiv 0908.4024 (auxiliary functions survey), 1806.10737, 2502.00731, Wikipedia |
| 2 | WebSearch (general form) | Roth's theorem auxiliary polynomial integer coefficients bounded by q^{delta r} Siegel lemma height bound | partial | auxiliary polynomial height bounded via Siegel's lemma, e.g. h(P) ≤ (Σ r_h) C (arXiv 2502.00731, Bombieri–Gubler style) | role (coefficient/height bound of the auxiliary polynomial) is standard; normalisation presentation-specific |
| 3 | WebSearch (aliases) | "floor" "q_1^{\delta r_1}" Roth main lemma height of auxiliary polynomial | no | H_2(P) ≤ (13𝓗)^q in arXiv 0709.1560 appendix | different normalisation; no named concept |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `B_1`, eq. (37) | yes | eq. (37) `B_1 = [q_1^{δ r_1}]` (l.1351–1353); largeness l.1360–1371; three small factors l.1375–1377 | exact match with the Lean body |
| 6 | nLab | Roth's theorem coefficient bound | no | n/a | nLab has no entry on Roth's proof constants |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | numeric Diophantine parameter, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread about this constant |
| 10 | recent arXiv | 2502.00731, 1806.10737, 0709.1560 | partial | as #2/#3 | each proof uses its own height normalisation (log height via Siegel's lemma, not a floor of q_1^{δ r_1}) |

### Literature summary (Phase 3)

Concept identified as: the coefficient bound of the pigeonhole/Siegel step in the Cassels-style proof of Roth's theorem (source eq. (37)); not a named mathematical concept.
Sources agree on the standard form: no — modern expositions (Bombieri–Gubler, arXiv 2502.00731) bound the logarithmic height of the auxiliary polynomial via Siegel's lemma instead of a floor of `q_1^{δ r_1}`.
Most general standard form: none; B_1 is presentation-specific bookkeeping.
Generality dimensions where the literature varies:
  - height normalisation (integer coefficient bound vs log height vs `(13𝓗)^q`): proof-specific.
Disagreement with the literature: none; matches the source exactly.

### Generality analysis — `Roth.mainCoeffBound`

Literature-standard form (from Phase 3): source eq. (37), `B_1 = [q_1^{δ r_1}]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `δ : ℝ` | real | positive real | no | already total over ℝ |
| 2 | `q₁ : ℕ` | natural | positive integer | no | already total over ℕ |
| 3 | `r₁ : ℕ` | natural | positive integer | no | already total over ℕ |
| 4 | codomain | ℕ | integer `[·]` | no | ℕ is the right type for a coefficient range `[0, B]`; `⌊·⌋₊` agrees with `[·]` on the nonnegative `q₁^{δ r₁}` |

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
| 5 | Field-specific vs typeclass-weakened? | no | rpow needs ℝ | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | `q₁, r₁ : ℕ` are counts | — |
| 8 | Concrete-via-abstract? | no | no proof body | — |
| 9 | False-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - Reason: a paper-specific numeric constant; nothing to reorganise.

### Proof strategy — `Roth.mainCoeffBound`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | definition, no proof | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | — | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (n/a for a definition with no proof; the body is the source formula verbatim)

### Diamond / defeq risk — `Roth.mainCoeffBound`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | value in ℕ via `Nat.floor` with the standard `FloorSemiring ℝ` instance; `Real.rpow` via the standard `HPow ℝ ℝ ℝ`; no instance introduced |
| 2 | Reducibility leak | none | plain semireducible def; consumers unfold explicitly (`simpa [mainCoeffBound, ...]`) |
| 3 | Non-canonical unfolding | none | not `@[simp]` |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | arguments in `Type` (ℝ, ℕ) |
| 6 | Coercion ambiguity | none | only the standard `ℕ → ℝ` casts of `q₁`, `r₁`; consumers cast the result back with `(mainCoeffBound … : ℝ)` |

### Risk verdict (Phase 4.5)

Overall risk: NONE
Top risks: none
Recommended mitigations: none

### Mathlib search-status: `Roth.mainCoeffBound`

[A] Lean-Finder       "natural floor of real power q^(δ r) as coefficient bound"   hits: `SzemerediRegularity.bound`, `SzemerediRegularity.initialBound`, `Behrend.bound`, `Behrend.dValue`, `mul_pow_le_nat_floor_pow` — analogous paper-specific constants in other developments (Behrend's `dValue = ⌊N^{1/n}/2⌋₊` is the closest shape; it is likewise a local def in its own file), not our constant
[B] Loogle            `ℝ → ℕ → ℕ → ℕ, Nat.floor`   no hits
[C] LeanSearch        "natural number floor of a natural number raised to a real power"   hits: `Nat.floorRoot_pow_self`, `ENat.floor`, `Nat.floor_nat`, `Int.floor_natCast` — unrelated
[D] Grep mathlib src  `namespace Roth`, `mainCoeffBound`   no hits
[E] Name pattern      `Roth.mainCoeffBound` via lean_local_search   not run (the mathlib grep [D] is authoritative for absence; previous workers found lean_local_search failing without ripgrep)

Searched for both:
  - the user's current form (B_1 = ⌊q_1^{δ r_1}⌋)
  - the literature-standard form (auxiliary-polynomial coefficient/height bound; none standard)

Concluded: found building blocks (`Nat.floor`, `Real.rpow`, `Nat.cast`); composition yields our form; not in mathlib as a named constant.

### Normal-form check — `Roth.mainCoeffBound`

Equivalent formalisms this statement could take: `⌊(q₁ : ℝ) ^ (δ * r₁)⌋₊` (current); `⌊((q₁ : ℝ) ^ δ) ^ r₁⌋₊`; `Int.toNat ⌊(q₁ : ℝ) ^ (δ * r₁)⌋`; `⌊Real.exp (δ * r₁ * Real.log q₁)⌋₊`.
Does mathlib already have a canonical form for this idea? no (no such constant).
Proposed canonical form: current (verbatim eq. (37); `Nat.floor` is mathlib's standard ℕ-valued floor).
RHS convention respected? n/a (definition).

### Syntactic generality — `Roth.mainCoeffBound`

Alternative restatements attempted:
- current
- `((q₁ : ℝ) ^ δ) ^ r₁` inner form
- `Int.floor` with ℤ codomain
- inlining into every statement

Chosen restatement: current.
Justification: ℕ codomain matches the `[0, B]` coefficient ranges of `boxFamily`; the exponent `δ * r₁` matches the real bound `(q₁ : ℝ) ^ (δ * r₁)` used for `RSet`/`Θ`, so `Nat.floor_le` / `Nat.lt_floor_add_one` apply directly.

### Superfluous-argument audit — `Roth.mainCoeffBound`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `δ` | yes | in the exponent |
| 2 | `q₁` | yes | base |
| 3 | `r₁` | yes | in the exponent |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; not proposed for mathlib)

### Call sites — `Roth.mainCoeffBound`

Internal use count: 4 lines in Roth/Main.lean (2 declarations) outside the declaring file; further lines in 6 declarations of Roth/MainLemma.lean
External-to-file callers: 1 distinct file (Roth/Main.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:150 | `δ * r₁ * Real.log q₁ / 2 < Real.log (mainCoeffBound δ q₁ r₁)` (statement of `mul_log_div_two_lt_log_mainCoeffBound`) |
| Roth/MainLemma.lean:151 | `simpa [mainCoeffBound, Real.log_sqrt ...]` |
| Roth/MainLemma.lean:182–184 | `(2 : ℝ) ^ (m * r₁) < (mainCoeffBound δ q₁ r₁ : ℝ) ^ δ ∧ ...` (statement of `three_small_factors`) |
| Roth/MainLemma.lean:199–200 | `t ^ (m * r₁) < (mainCoeffBound δ q₁ r₁ : ℝ) ^ δ`, `Real.lt_rpow_of_log_lt (y := mainCoeffBound δ q₁ r₁)` |
| Roth/MainLemma.lean:205 | `mul_log_div_two_lt_log_mainCoeffBound hX` |
| Roth/MainLemma.lean:622 | `P ∈ RSet (mainCoeffBound δ q₁ r₁) r ∧` (private `exists_mem_RSet_le_index_of_log_bound_aux`) |
| Roth/MainLemma.lean:633–634 | `(mainCoeffBound δ q₁ r₁ : ℝ) ^ (1 + 3 * δ) = mainCoeffBound δ q₁ r₁ * (...) ^ 3` |
| Roth/MainLemma.lean:639 | `exists_mem_RSet_le_index_of_rpow_bound_aux (B := mainCoeffBound δ q₁ r₁)` |
| Roth/MainLemma.lean:650–651 | `(mainCoeffBound δ q₁ r₁ : ℝ) ^ (1 + 3 * δ)`, `let B := mainCoeffBound δ q₁ r₁` (private `exists_auxiliary_polynomial_of_log_bound_aux`) |
| Roth/MainLemma.lean:702 | `(mainCoeffBound δ (q 0) (r 0) : ℝ) ^ (1 + 3 * δ)` (private `exists_auxiliary_polynomial_with_index_gap_aux`) |
| Roth/MainLemma.lean:746 | `(mainCoeffBound δ (q 0) (r 0) : ℝ) ^ (1 + 3 * δ)` (statement of `main_lemma`) |
| Roth/Main.lean:462 | `(mainCoeffBound δ (q 0) (r 0) : ℝ) ^ (1 + 3 * δ) *` (private `one_lt_roth_eval_bound_aux`) |
| Roth/Main.lean:484–486 | `0 < (mainCoeffBound δ (q 0) (r 0) : ℝ) ∧ ... ≤ (q 0 : ℝ) ^ (δ * r 0) ∧ ... < (...) ^ δ` (private `roth_product_bound_aux`) |

Inline-derivation grep (`grep -rnE "⌊.*\^ \(δ" Roth/`): no inline `⌊(q : ℝ) ^ (δ * r)⌋₊` re-derivation. The unfloored real `(q₁ : ℝ) ^ (δ * r₁)` appears at MainLemma.lean:123, 157, 647, 676, 698–699, 750 and Main.lean:508 as the real `RSet`/`Θ` bound; that is a different quantity (X, not ⌊X⌋), so (none).

### Composition check (Phase 6)

Can `Roth.mainCoeffBound` be derived from mathlib in ≤3 chained calls?

Attempt 1: `fun δ q₁ r₁ ↦ Nat.floor (Real.rpow (q₁ : ℝ) (δ * r₁))`
  - Mathlib decls used: `Nat.floor` (FloorSemiring ℝ), `Real.rpow`, `Nat.cast`
  - Result: succeeds (this is the body)
  - Notes: none

Conclusion: COMPOSABLE

## Verdict: `Roth.mainCoeffBound`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): B_1 is the source's eq. (37) bookkeeping constant; modern expositions use log heights via Siegel's lemma instead; no exposition treats it as a concept.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (nothing to weaken).
- Mathlib search (Phase 5): not in mathlib; building blocks `Nat.floor`, `Real.rpow`, `Nat.cast`.
- Composition check (Phase 6): COMPOSABLE (one mathlib-term expression).

**Rationale:**

`Roth.mainCoeffBound` is a one-line numeric constant specific to one presentation of Roth's theorem. It has no mathematical content beyond its formula, so mathlib would never want it; it is already "composed from mathlib" (`Nat.floor` of `Real.rpow`). Same treatment as its siblings `Roth.lam`, `Roth.gam`, `Roth.eta` (all NO-composable-from-mathlib, kept locally), and analogous to mathlib's own local constants like `Behrend.dValue`, which live in their application file rather than as general API.

WHY not: mathlib's building blocks (`Nat.floor` in Mathlib/Algebra/Order/Floor/Defs.lean, `Real.rpow` in Mathlib/Analysis/SpecialFunctions/Pow/Real.lean) give the expression directly. Belongs-elsewhere check: it belongs in the Roth project as the paper's named B_1; it appears in the public statements of `main_lemma`, `three_small_factors` and `mul_log_div_two_lt_log_mainCoeffBound`, so inlining would hurt readability and remove the name those lemmas are about.

Mathlib building blocks: `Nat.floor`, `Real.rpow`, `Nat.cast`.
Composition sketch:
```lean
example (δ : ℝ) (q₁ r₁ : ℕ) : Roth.mainCoeffBound δ q₁ r₁ = ⌊(q₁ : ℝ) ^ (δ * r₁)⌋₊ := rfl
```
Call sites in our project (from Phase 6.0): about 20 lines in 8 declarations (MainLemma.lean:150, 151, 182–184, 199, 200, 205, 622, 633, 634, 639, 650, 651, 702, 746; Main.lean:462, 484–486).
Refactor plan: none recommended for these sites. (Mechanically possible: replace `mainCoeffBound δ q r` by `⌊(q : ℝ) ^ (δ * r)⌋₊` at each site and drop the `mainCoeffBound` unfolding in the `simpa` at :151; rejected because it bloats `main_lemma` and loses the eq. (37) correspondence.)
Next action: do not upstream; keep `Roth.mainCoeffBound` in the project.

## Next step

Do not upstream; keep `Roth.mainCoeffBound` as the paper's B_1.

## Evidence
- WebSearch ×3 (queries in the literature table): no source states this constant; arXiv 0908.4024, 1806.10737, 2502.00731, 0709.1560, Wikipedia, Evertse notes surfaced.
- Local reference clean.tex l.1337–1353 (eq. (37)), l.1360–1377 (largeness of B_1 and the three small factors).
- lean_leanfinder, lean_leansearch, lean_loogle queries as recorded in Phase 5 (no relevant hit); grep over `.lake/packages/mathlib/Mathlib/` for `namespace Roth` / `mainCoeffBound` (no hit).
- `grep -rn mainCoeffBound Roth/` for call sites; inline-derivation grep for `⌊…^ (δ` (none). No Lean experiments were needed (no weakening proposed; the composition sketch is the definitional body); no evidence files written.
