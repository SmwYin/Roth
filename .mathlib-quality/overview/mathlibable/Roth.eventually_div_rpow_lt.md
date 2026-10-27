---
decl: Roth.eventually_div_rpow_lt
file: Roth/Main.lean
line: 103
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: The statement is the eventually-greater consequence of tendsto_rpow_atTop (via Tendsto.eventually_gt_atTop and tendsto_natCast_atTop_atTop) followed by a one-line rpow rearrangement; its ∃ Q₀ : ℕ, ∀ q > Q₀ shape is project-specific and mathlib would only want the general rpow little-o fact, which is a different declaration.
action: Keep project-local (3 call sites in Roth/Main.lean:122, Roth/Main.lean:181, Roth/LeanEval.lean:46); optionally restate as ∀ᶠ x : ℝ in atTop with the filter_upwards proof in the evidence file; the side gap isLittleO_rpow_rpow_atTop_of_lt (real analogue of Asymptotics.isLittleO_pow_pow_atTop_of_lt) could be a separate PR to Mathlib/Analysis/SpecialFunctions/Pow/Asymptotics.lean.
---

# Roth.eventually_div_rpow_lt

## Inventory entry

### `theorem Roth.eventually_div_rpow_lt`
- **Type**: `{M κ κ' : ℝ} (hκ : κ' < κ) : ∃ Q₀ : ℕ, ∀ q : ℕ, Q₀ < q → M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ'`
- **What**: If κ' < κ then for every real constant M, M/q^κ < 1/q^κ' for all sufficiently large natural numbers q.
- **How**: Applies `Filter.Tendsto.eventually_gt_atTop` to `(tendsto_rpow_atTop (sub_pos.2 hκ)).comp tendsto_natCast_atTop_atTop` to get N with M < q^(κ-κ') for q ≥ N, extracted by `Filter.eventually_atTop`; then rewrites the goal with `div_lt_iff₀` (positivity from `Real.rpow_pos_of_pos`), `one_div_mul_eq_div` and `Real.rpow_sub`.
- **Hypotheses**: `hκ : κ' < κ`.
- **Uses from project**: `[]`
- **Used by**: Roth/Main.lean: `Roth.reduction` (line 122), `Roth.exists_reduced_approx` (line 181, fibre-finiteness step); Roth/LeanEval.lean: `isDiophantine_iff` (line 46).
- **Visibility**: public
- **Lines**: 103–111, proof length 7 lines
- **Notes**: Source: clean.tex §6 l.1171–1173 ("Pick any κ' such that 2 < κ' < κ. Then for q large enough, M/q^κ < 1/q^{κ'}") and l.1189. The ∃ Q₀ / strict `Q₀ < q` shape is tailored to `Roth.approxSet_den_le_finite`, which bounds denominators by `Q₀`.

## Junk check (Step 8)
- Used anywhere? Yes, 3 call sites in 2 files (Main.lean:122, Main.lean:181, LeanEval.lean:46).
- Wrapper of 1–2 mathlib calls? Essentially: `tendsto_rpow_atTop` + `Tendsto.eventually_gt_atTop` (+ nat cast) plus a 3-lemma rewrite. Not a pure term composition, but close.
- Does mathlib have it? No lemma of this shape (Loogle, LeanSearch, Lean-Finder, grep; see below). Mathlib has the ingredients and the ℕ-exponent analogue `Asymptotics.isLittleO_pow_pow_atTop_of_lt`, `tendsto_pow_div_pow_atTop_zero`.
- Too specific (inline?)? It is used three times with the same shape, matching the denominator-bound API of `approxSet_den_le_finite`; inlining would triplicate the 7-line argument.
- Well-chosen? Yes for the project. It reproduces the paper's §6 sentence and fits the `Q₀` denominator-bound pattern.

Conclusion: KEEP. Optional polish: state the core as `∀ᶠ x : ℝ in atTop, M / x ^ κ < 1 / x ^ κ'` (compiled, evidence file) and derive the ℕ form from it.

## Mathlibable assessment (Step 9)

Pre-filter: public. The name does not end in `_aux`, and the docstring is not internal or auxiliary. Step 8 said KEEP. A namespace-aware grep of `.lake/packages/mathlib/Mathlib/` finds no `eventually_div_rpow_lt`. The proof is not `rfl`/unfolding, so this is not a glue lemma. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the evidence file importing `Roth.Main` elaborates with no diagnostics)
- decl `Roth.eventually_div_rpow_lt`: resolved at Roth/Main.lean:103
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's theorem for real algebraic numbers, reduced via §6 to irrational real algebraic integers and proved via §7.

### Statement (Phase 1)

`Roth.eventually_div_rpow_lt` is a theorem stating the following:

Let M, κ, κ' be real numbers with κ' < κ. Then there is a natural number Q₀ such that for every natural number q > Q₀, M/q^κ < 1/q^{κ'}. Equivalently, q^{κ-κ'} eventually exceeds any fixed constant, i.e. a power with a larger exponent eventually beats any constant multiple of a power with a smaller one.

Variables / typeclasses involved (Lean side):
- `M : ℝ`: an arbitrary constant (no sign condition).
- `κ κ' : ℝ`: real exponents.
- `q : ℕ`, cast to ℝ: the variable going to infinity.

Hypotheses (Lean side):
- `hκ : κ' < κ`: strict exponent gap.

Conclusion (math): for all sufficiently large q ∈ ℕ, M q^{-κ} < q^{-κ'}.

Conclusion (Lean): `∃ Q₀ : ℕ, ∀ q : ℕ, Q₀ < q → M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ'`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an elementary asymptotic helper in the §6 reduction, not a main result or a new structure.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

n/a: kind is theorem. MULTI-LINE (7-line proof); check skipped.

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | "for q large enough" M/q^kappa < 1/q^kappa' Roth theorem reduction algebraic integer | partial | Roth reductions use this inline as "for q sufficiently large" | arXiv 2412.05867 §4, Klazar AKTC lecture notes. Nobody states it as a lemma |
| 2 | WebSearch (general form) | x^a = o(x^b) as x to infinity a < b power functions little o comparison | yes | x^a = o(x^b) for a < b, proved by x^a/x^b = x^{-(b-a)} → 0 | MIT 6.042 asymptotics notes, LibreTexts "Asymptotic Notation" (example 1000x^1.9 = o(x^2)) |
| 3 | WebSearch (named / aliases) | power function growth hierarchy eventually dominates constant multiple asymptotic order of x^s | yes | the growth hierarchy log ≪ x^α ≪ b^x; x^y → ∞ for y > 0 | K. Conrad "growth" notes; mathlib's Pow/Asymptotics docs (tendsto_rpow_atTop, tendsto_rpow_neg_atTop) |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "kappa'" | yes | l.1171–1173: "for q large enough, M/q^κ < 1/q^{κ'}"; l.1189: "M q^{-κ} < q^{-κ'} for all sufficiently large q" | the Lean statement matches the source verbatim |
| 6 | nLab | "Landau notation" / "asymptotic" | partial | nLab has no dedicated entry beyond generic limits; the fact is calculus folklore | nothing more general |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | real analysis on ℝ; not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | "x^a = o(x^b)" / "polynomial growth comparison real exponents" | yes (standard) | the ratio argument of #2; textbook exercise | no new generality |
| 10 | recent arXiv | "q sufficiently large" Roth reduction (arXiv 2412.05867) | partial | used inline, not as a lemma | confirms it is a routine step |

### Literature summary (Phase 3)

Concept identified as: comparison of power functions at infinity (x^a = o(x^b) for a < b), in its "eventually M x^{-κ} < x^{-κ'}" form.
Sources agree on the standard form: yes.
Most general standard form: for real a < b, x^a = o(x^b) as x → +∞ (over a real variable). Every "eventually c·x^a < x^b" statement, for any constant c, follows from it.
Generality dimensions where the literature varies:
  - variable: ℕ (sequences) vs ℝ (functions); the most general is ℝ along `atTop`. The ℕ version follows by composing with the cast.
  - formulation: explicit threshold (∃ Q₀) vs Landau little-o vs eventually-filter; the most idiomatic in mathlib is `=o[atTop]` or `∀ᶠ x in atTop`.
Disagreement with the literature: none. The user's form is the ℕ-indexed, explicit-threshold, fixed-constant instance.

### Generality analysis — `Roth.eventually_div_rpow_lt`

Literature-standard form: `(fun x : ℝ ↦ x ^ a) =o[atTop] fun x ↦ x ^ b` for a < b, or its eventually-form `∀ᶠ x : ℝ in atTop, M / x ^ κ < 1 / x ^ κ'`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `q : ℕ` (index) | natural number, cast to ℝ | real variable along `atTop` | yes | compiled: the ℝ filter form holds (evidence (1)), and the ℕ form follows from it via `tendsto_natCast_atTop_atTop.eventually` (evidence (2)) |
| 2 | `∃ Q₀, ∀ q, Q₀ < q → …` | explicit threshold, strict | `∀ᶠ q in atTop` | equivalent | `Filter.eventually_atTop` (with `le_of_lt`) |
| 3 | `M : ℝ` | arbitrary constant | arbitrary constant / little-o | no | already arbitrary, with no sign assumption |
| 4 | `hκ : κ' < κ` | strict gap | strict gap | no | needed; false for κ' = κ, M ≥ 1 |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD in the index dimension (ℕ vs ℝ), verified by compiling the ℝ filter form. Mathlib, however, already has the general ingredient (`tendsto_rpow_atTop`), and the ℝ form is itself a `filter_upwards` composition. So this is false-positive class 4 ("general form already in mathlib", or at least its ingredients are), not YES-but-generalise-first. The fully general little-o statement (evidence (3)) is a different declaration, discussed under Phase 4.6/7.
Number of weakening opportunities found: 1 (ℕ to ℝ), compiled.
Proposed restatement (project-local, optional):

```lean
theorem eventually_div_rpow_lt {M κ κ' : ℝ} (hκ : κ' < κ) :
    ∀ᶠ x : ℝ in atTop, M / x ^ κ < 1 / x ^ κ'
```

Cost of restatement: CHEAP (but the 3 call sites would each need `eventually_atTop.1 (tendsto_natCast_atTop_atTop.eventually _)`, so the current ℕ form is arguably more convenient locally).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | single numeric hypothesis | — |
| 2 | sequences to filters? | yes | `∀ᶠ x : ℝ in atTop, …` or `=o[atTop]` instead of ∃ Q₀ : ℕ | composes with `Filter.Eventually.mono`, `Tendsto.eventually` and the Asymptotics API |
| 3 | construction to universal property? | no | — | — |
| 4 | set to bundled substructure? | no | no sets | — |
| 5 | field-specific to weaker typeclasses? | no | rpow is ℝ-specific | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | ℕ to ℝ along atTop (or any filter tending to atTop) | `Tendsto.eventually` specialises it to any such sequence |
| 8 | concrete-via-abstract? | no | the statement is already abstract (arbitrary M, κ, κ') | — |
| 9 | false-generalisation guard | no false generalisation | ℕ to ℝ and ∃ Q₀ to ∀ᶠ preserve the meaning (compiled, evidence (2)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes. The filter form `∀ᶠ x : ℝ in atTop, M / x ^ κ < 1 / x ^ κ'` (CHEAP, compiled), or more fundamentally `(fun x ↦ x ^ (-κ)) =o[atTop] fun x ↦ x ^ (-κ')`. The idiomatic version is not a contribution in itself, though. It is a 3-line `filter_upwards` over mathlib lemmas, and the reusable content is the general little-o fact `isLittleO_rpow_rpow_atTop_of_lt`, a different declaration (see Phase 7).

### Proof strategy — `Roth.eventually_div_rpow_lt`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | partial | already filter-based (`Tendsto.eventually_gt_atTop`), but exits to an explicit `N` via `eventually_atTop`; `filter_upwards` keeps it in filter land | CHEAP |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | yes | state over ℝ and compose with `tendsto_natCast_atTop_atTop` at the end (evidence (2)) | CHEAP |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes (minor) | `isLittleO_rpow_rpow_atTop_of_lt : a < b → (fun x : ℝ ↦ x ^ a) =o[atTop] fun x ↦ x ^ b`, the real-exponent analogue of `Asymptotics.isLittleO_pow_pow_atTop_of_lt`, is absent; compiled in evidence (3) | CHEAP (separate follow-up) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (minor polish possible)
  - Proposed strategy: `filter_upwards [(tendsto_rpow_atTop (sub_pos.2 hκ)).eventually_gt_atTop M, eventually_gt_atTop 0]` + the same `rwa`, over ℝ, then cast to ℕ.
  - Cost: CHEAP
  - Missing mathlib API: `isLittleO_rpow_rpow_atTop_of_lt` (would not shorten this proof materially; it is a separate gap)
  - Would refactoring make the proof strictly shorter / cleaner? marginally (same length, more general statement).

### Diamond / defeq risk

n/a: declaration kind is theorem.

### Mathlib search-status: `Roth.eventually_div_rpow_lt`

[A] Lean-Finder       "for any constant M and a < b, eventually M / x^b < 1 / x^a as x tends to infinity"   hits: `tendsto_pow_div_pow_atTop_zero`, `tendsto_pow_div_pow_atTop_atTop`, `Asymptotics.isLittleO_pow_pow_atTop_of_lt` (all ℕ exponents), `tendsto_const_div_pow` (r / n^k → 0, ℕ exponent). No real-exponent version.
[B] Loogle            `Asymptotics.IsLittleO Filter.atTop (fun x : ℝ => x ^ _) (fun x : ℝ => x ^ _)`: no hits; `Filter.Eventually, HDiv.hDiv, HPow.hPow (_ : ℝ) (_ : ℝ), Filter.atTop`: no hits
[C] LeanSearch        "x ^ (-b) is little o of x ^ (-a) at top when a < b real powers"   hits: `Asymptotics.isLittleO_pow_pow_atTop_of_lt` (ℕ), `Asymptotics.IsLittleO.rpow`, `isLittleO_pow_pow_of_lt_left` (geometric). No direct hit.
[D] Grep mathlib src  `eventually_div_rpow_lt`, `isLittleO_rpow_rpow`, `rpow.*=o\[atTop\].*rpow`, the list of every `*isLittleO*rpow*`/`*tendsto*rpow*` theorem name   hits: `tendsto_rpow_atTop`, `tendsto_rpow_neg_atTop` (Analysis/SpecialFunctions/Pow/Asymptotics.lean:38, 50), `isLittleO_log_rpow_rpow_atTop`, `isLittleO_rpow_exp_atTop`, `tendsto_nat_rpow_inv`; no rpow-vs-rpow little-o and no eventually-form
[E] Name pattern      `lean_local_search isLittleO_rpow_rpow`   n/a: ripgrep not on PATH; replaced by the grep in [D]

Searched for both the user's form (eventually M/q^κ < 1/q^κ') and the literature-standard form (x^a = o(x^b) for real a < b).

Concluded: found building blocks (`tendsto_rpow_atTop`, `Filter.Tendsto.eventually_gt_atTop`, `tendsto_natCast_atTop_atTop`, `Filter.eventually_atTop`, `Real.rpow_sub`, `div_lt_iff₀`); composition would yield our form. The general rpow little-o lemma is not in mathlib.

### Normal-form check — `Roth.eventually_div_rpow_lt`

Equivalent formalisms: (a) ∃ Q₀ : ℕ, ∀ q > Q₀, M/q^κ < 1/q^κ'; (b) ∀ᶠ q : ℕ in atTop, …; (c) ∀ᶠ x : ℝ in atTop, …; (d) `(fun x ↦ x ^ (-κ)) =o[atTop] fun x ↦ x ^ (-κ')`; (e) ∀ᶠ x in atTop, M < x^(κ-κ').
Does mathlib already have a canonical form? For this idea, the canonical form is (d)/(e). (e) is `(tendsto_rpow_atTop _).eventually_gt_atTop M` verbatim; (d) is missing.
Our statement is a non-canonical explicit-threshold variant tailored to the project's `Q₀` API.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.eventually_div_rpow_lt`

Alternative restatements attempted:
- (c) the ℝ filter form (compiled).
- (b) the ℕ filter form.
- (a) the current form.
Chosen restatement: (a) for the project.
Justification: all 3 call sites feed `Q₀` into `approxSet_den_le_finite α κ Q₀` and use `hQ q (hq : Q₀ < q)` directly. (c) is preferable only if the statement were made public API.

### Superfluous-argument audit — `Roth.eventually_div_rpow_lt`

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `M : ℝ` | yes | the constant to beat; no superfluous sign condition |
| 2 | `κ κ' : ℝ` | yes | — |
| 3 | `hκ : κ' < κ` | yes | the conclusion fails for κ = κ', M ≥ 1 |
| 4 | index type ℕ | no (as such) | ℝ works (compiled); ℕ chosen for call-site convenience |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (only if upstreamed: use ∀ᶠ over ℝ or the little-o form)
Syntactic generality: OK for the project (ℕ/∃ Q₀ matches the call sites)
Superfluous arguments: NONE (the ℕ index is a specialisation, not a dead argument)

Overall: SHIP-AS-STATED for the project; moot for mathlib (verdict is NO)

### Call sites — `Roth.eventually_div_rpow_lt`

Internal use count: 1 outside the declaring file (3 in total, 2 in Roth/Main.lean)
External-to-file callers: 1 file (Roth/LeanEval.lean)

| Caller file:line | Usage pattern |
|---|---|
| Roth/Main.lean:122 (`Roth.reduction`) | `obtain ⟨Q₀, hQ₀⟩ := eventually_div_rpow_lt (M := M) (show (κ + 2) / 2 < κ by linarith)` |
| Roth/Main.lean:181 (`Roth.exists_reduced_approx`) | `obtain ⟨N, hN⟩ := eventually_div_rpow_lt (M := 1 / \|α - (x : ℝ)\|) hκ` |
| Roth/LeanEval.lean:46 (`isDiophantine_iff`) | `obtain ⟨Q, hQ⟩ := Roth.eventually_div_rpow_lt (M := 1 / C) (by linarith : 2 + (κ - 2) / 2 < κ)` |

Inline-derivation grep (`tendsto_rpow_atTop`, `eventually_gt_atTop` across `Roth/`): (none). Every caller goes through the lemma.

### Composition check (Phase 6)

Can `Roth.eventually_div_rpow_lt` be derived from mathlib in ≤3 chained calls?

Attempt 1 (core): `((tendsto_rpow_atTop (sub_pos.2 hκ)).comp tendsto_natCast_atTop_atTop).eventually_gt_atTop M` gives `∀ᶠ q : ℕ in atTop, M < (q : ℝ) ^ (κ - κ')` (2 calls). The pointwise conversion `M < q^(κ-κ') ↔ M / q^κ < 1 / q^κ'` is `rw [div_lt_iff₀ (Real.rpow_pos_of_pos hq0 κ), one_div_mul_eq_div, ← Real.rpow_sub hq0]`.
  - Mathlib decls used: `tendsto_rpow_atTop`, `tendsto_natCast_atTop_atTop`, `Filter.Tendsto.eventually_gt_atTop`, `Filter.eventually_atTop`, `div_lt_iff₀`, `one_div_mul_eq_div`, `Real.rpow_sub`, `Real.rpow_pos_of_pos`
  - Result: succeeds (this is the current proof, and the ℝ variant in evidence (1)–(2) compiles clean)
  - Notes: the composition is 2 calls plus a 3-lemma pointwise rewrite. By the 6b heuristic, a `rw` chain is "borderline". It is a fixed arithmetic rearrangement with no mathematical idea, so it is recorded as a trivial composition.
Attempt 2 (via a little-o lemma): from evidence (3)'s `isLittleO_rpow_rpow_atTop_of_lt` one still needs `IsLittleO.def` with ε = 1/(|M|+1) and sign bookkeeping. That is longer, not shorter.

Conclusion: COMPOSABLE (trivial composition: `Tendsto.eventually_gt_atTop` of `tendsto_rpow_atTop` plus a pointwise rpow rearrangement)

## Verdict: `Roth.eventually_div_rpow_lt`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the result is the textbook comparison x^a = o(x^b) (a < b) in eventually-form. The paper uses it inline (§6 l.1171) and no source states this ℕ, explicit-threshold form as a named lemma.
- Generality analysis (Phase 4): STRICTLY NARROWER only in the index (ℕ vs ℝ, compiled). The general ingredient is mathlib's `tendsto_rpow_atTop` (false-positive class 4).
- Mathlib search (Phase 5): building blocks found (`tendsto_rpow_atTop`, `Filter.Tendsto.eventually_gt_atTop`, `tendsto_natCast_atTop_atTop`, `Real.rpow_sub`, `div_lt_iff₀`). There is no exact or more general eventually-form lemma, and the real-exponent little-o lemma is absent.
- Composition check (Phase 6): COMPOSABLE (2 calls plus a fixed 3-lemma rewrite).

**Rationale:**

Mathematically, the statement says that q^{κ-κ'} → ∞, so it eventually exceeds M, rewritten as M/q^κ < 1/q^κ'. Mathlib has the first part verbatim as `(tendsto_rpow_atTop h).eventually_gt_atTop M` (composed with `tendsto_natCast_atTop_atTop` for ℕ). The rest is a pointwise rpow rearrangement (`div_lt_iff₀`, `one_div_mul_eq_div`, `Real.rpow_sub`). The explicit ∃ Q₀ : ℕ / strict `Q₀ < q` packaging exists only to feed `Roth.approxSet_den_le_finite`. Mathlib would not accept an explicit-threshold, ℕ-indexed, fixed-constant variant. The idiomatic restatement (∀ᶠ over ℝ) is itself a 3-line `filter_upwards` of mathlib lemmas (compiled), so there is no new content to upstream.

The asymptotic fact that is genuinely missing from mathlib is the real-exponent analogue of `Asymptotics.isLittleO_pow_pow_atTop_of_lt`, namely `(fun x : ℝ ↦ x ^ a) =o[atTop] fun x ↦ x ^ b` for a < b (compiled in evidence (3), 7 lines). It is a different declaration and does not shorten this proof. It is recorded as an optional side contribution, not as the verdict for this lemma.

WHY not: mathlib supplies the building blocks, and the statement is `Tendsto.eventually_gt_atTop` of `tendsto_rpow_atTop`, transported to ℕ and rearranged pointwise. The ∃ Q₀ shape is a project convenience.
Belongs-elsewhere check: keep project-local in Roth/Main.lean. It is the paper's §6 step and serves 3 call sites with an identical usage pattern. Inlining would triplicate a 7-line argument, so the refactor plan below does not delete it.
Mathlib building blocks:
- `tendsto_rpow_atTop` — Mathlib/Analysis/SpecialFunctions/Pow/Asymptotics.lean:38
- `Filter.Tendsto.eventually_gt_atTop` — Mathlib/Order/Filter/AtTopBot/Tendsto.lean
- `tendsto_natCast_atTop_atTop` — Mathlib/Order/Filter/AtTopBot/Archimedean.lean:44
- `Filter.eventually_atTop`, `Real.rpow_sub`, `Real.rpow_pos_of_pos`, `div_lt_iff₀`, `one_div_mul_eq_div`
Composition sketch:
```lean
example {M κ κ' : ℝ} (hκ : κ' < κ) : ∀ᶠ x : ℝ in atTop, M / x ^ κ < 1 / x ^ κ' := by
  filter_upwards [(tendsto_rpow_atTop (sub_pos.2 hκ)).eventually_gt_atTop M,
    eventually_gt_atTop 0] with x hx hx0
  rwa [div_lt_iff₀ (Real.rpow_pos_of_pos hx0 κ), one_div_mul_eq_div, ← Real.rpow_sub hx0]
```
Call sites in our project (from Phase 6.0): 3 (Roth/Main.lean:122, Roth/Main.lean:181, Roth/LeanEval.lean:46)
Refactor plan: none required. The lemma is a well-placed local helper. If the project wants the idiomatic form, restate it as the ℝ filter version above and add, at each of the 3 call sites, `obtain ⟨Q₀, hQ₀⟩ := eventually_atTop.1 (tendsto_natCast_atTop_atTop.eventually (eventually_div_rpow_lt h))`, then use `hQ₀ q hq.le` where `hQ q hq` is used now. This is a net loss in convenience, so it is not recommended.
Next action: keep `Roth.eventually_div_rpow_lt` as is. Do not upstream. Optionally open a separate small mathlib PR adding `isLittleO_rpow_rpow_atTop_of_lt` to Mathlib/Analysis/SpecialFunctions/Pow/Asymptotics.lean (proof in the evidence file).

## Next step

Keep the lemma project-local (3 call sites). Nothing to upstream for this declaration. The real-exponent little-o comparison `isLittleO_rpow_rpow_atTop_of_lt` is an optional independent mathlib contribution.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.eventually_div_rpow_lt/experiments.lean` (imports `Roth.Main`). It contains (1) the ℝ filter form via `filter_upwards`, (2) the project's exact ℕ statement recovered from (1), (3) `isLittleO_rpow_rpow_atTop_of_lt` for real a < b, and (4) a reference use of the project lemma. `lean_diagnostic_messages` reports no errors and no warnings (after moving the module docstring above `open`).
- WebSearch ×3 (see table). Lean-Finder ×1, LeanSearch ×1, Loogle ×2 (no hits). Grep of mathlib for `eventually_div_rpow_lt`, `isLittleO_rpow_rpow`, and every `*isLittleO*rpow*`/`*tendsto*rpow*` theorem name. `lean_local_search` was unavailable (ripgrep missing). The ChatGPT MCP was unavailable in this session.
