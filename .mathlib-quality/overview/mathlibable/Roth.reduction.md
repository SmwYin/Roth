---
decl: Roth.reduction
file: Roth/Main.lean
line: 118
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: The paper's §6 reduction to algebraic integers is stated over the project-local approxSet (itself NO-composable); in mathlib's LiouvilleWith vocabulary it is the two-call composition natDenominator plus LiouvilleWith.nat_mul, with the exponent preserved, compiled in the evidence file, so there is nothing new to upstream.
action: Keep project-local in Roth/Main.lean as the §6 Lemma (single call site Roth.roth at Roth/Main.lean:576); if Roth is ever upstreamed in LiouvilleWith form, replace it by the composition reduction_liouvilleWith in evidence/Roth.reduction/liouvilleWith_reduction.lean (no new lemma for Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean).
---

# Roth.reduction

## Inventory entry

### `theorem Roth.reduction`
- **Type**: `{α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ} (hκ : 2 < κ) (hinf : (approxSet α κ).Infinite) : ∃ (α' κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧ 2 < κ' ∧ (approxSet α' κ').Infinite`
- **What**: If an irrational real algebraic number α has infinitely many approximations of quality κ > 2, then some irrational real algebraic integer α' has infinitely many approximations of some quality κ' > 2. Concretely α' = Mα (M a positive integer clearing denominators) and κ' = (κ + 2)/2.
- **How**: `exists_nat_mul_isIntegral` gives M with Mα integral. `eventually_div_rpow_lt` with κ' = (κ+2)/2 < κ gives Q₀ with M/q^κ < 1/q^κ' for q > Q₀. Irrationality comes from `Irrational.natCast_mul`. Infinitude: remove the finite set `approxSet_den_le_finite α κ Q₀` from `approxSet α κ` (`Set.Infinite.sdiff`), then map by the injective `(h, q) ↦ (M h, q)` (`mul_right_injective₀.prodMap Function.injective_id`, `Set.Infinite.image`, `Set.Infinite.mono`). Each image pair is checked with `mul_div_assoc`, `mul_sub`, `abs_mul`, `mul_lt_mul_of_pos_left` and a `calc`.
- **Hypotheses**: `hα : Irrational α`, `halg : IsAlgebraic ℚ α`, `hκ : 2 < κ`, `hinf : (approxSet α κ).Infinite`.
- **Uses from project**: `Roth.approxSet`, `Roth.exists_nat_mul_isIntegral`, `Roth.eventually_div_rpow_lt`, `Roth.approxSet_den_le_finite`
- **Used by**: Roth/Main.lean: `Roth.roth` (line 576). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 118–134, proof length 14 lines
- **Notes**: Source: clean.tex §6 Lemma l.1148 ("If the theorem fails, then it also fails for an irrational real algebraic integer") and its proof l.1154–1189. Listed as step 1 of the proof outline in the module docstring. The exponent drop κ → (κ+2)/2 is needed only because `approxSet` fixes the constant 1 in 1/q^κ. With mathlib's `LiouvilleWith` (arbitrary constant C) the exponent is preserved.

## Junk check (Step 8)
- Used anywhere? Yes, once (`Roth.roth`, Main.lean:576), as the first step of the main theorem.
- Wrapper of 1–2 mathlib calls? Not in its current `approxSet` form (14-line set-theoretic argument over 3 project helpers). In the `LiouvilleWith` form it would be a 2-call composition (evidence (1)).
- Does mathlib have it? Not as stated (mathlib has no Roth development and no `approxSet`). The `LiouvilleWith` analogue is `LiouvilleWith.nat_mul` composed with `Algebra.natDenominator`.
- Too specific (inline?)? It has one call site, but it is a named step of the source (§6 Lemma), documented in the module outline. Inlining it into `Roth.roth` would make the main proof less readable.
- Well-chosen? Yes for the project, since it mirrors the paper's structure.

Conclusion: KEEP. No action locally. A possible project refactor is to phrase Roth via `LiouvilleWith`, which would reduce this to `reduction_liouvilleWith` (evidence (1)), but that is a whole-development decision (see Roth.approxSet report).

## Mathlibable assessment (Step 9)

Pre-filter: public. The name does not end in `_aux` and the docstring is not internal or auxiliary. Step 8 said KEEP. A namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `Roth.reduction` or a Roth development finds nothing (only author names "Rothgang"). The proof is not glue. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the evidence file importing `Roth.Main` elaborates with no diagnostics)
- decl `Roth.reduction`:     resolved at Roth/Main.lean:118
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's theorem for real algebraic numbers, reduced via §6 to irrational real algebraic integers and proved via §7.

### Statement (Phase 1)

`Roth.reduction` is a theorem stating the following:

Let α be an irrational real algebraic number and κ > 2, and suppose |α − h/q| < q^{−κ} has infinitely many solutions (h, q) ∈ ℤ × ℕ with q > 0. Then there exist an irrational real algebraic integer α' and an exponent κ' > 2 such that |α' − h/q| < q^{−κ'} has infinitely many solutions. In other words, a counterexample to Roth's theorem yields a counterexample at an algebraic integer.

Variables / typeclasses involved (Lean side):
- `α : ℝ`: the algebraic number.
- `κ : ℝ`: the approximation exponent.

Hypotheses (Lean side):
- `hα : Irrational α`: α is irrational.
- `halg : IsAlgebraic ℚ α`: α is algebraic over ℚ.
- `hκ : 2 < κ`: exponent beyond Roth's bound.
- `hinf : (approxSet α κ).Infinite`: infinitely many approximations of quality κ.

Conclusion (math): some irrational algebraic integer α' has infinitely many approximations of some quality κ' > 2.

Conclusion (Lean): `∃ (α' κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧ 2 < κ' ∧ (approxSet α' κ').Infinite`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a reduction step of the main proof (step 1 of the outline), not itself a main result. It is not listed under "Main results", and the named theorem is `Roth.roth`.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

n/a: kind is theorem. MULTI-LINE (14-line proof); check skipped.

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem reduction to algebraic integers "algebraic integer" multiply by denominator approximation exponent | partial | the reduction is named in course outlines (Klazar, Charles University NDMI045 2024/25: "reduction of Roth's inequality from algebraic numbers to algebraic integers") | no source states it as a separate theorem; Schmidt LNM 785 Ch. II is the standard reference |
| 2 | WebSearch (general form) | irrationality measure invariant under rational multiplication mu(r alpha) = mu(alpha) | partial | the irrationality exponent μ satisfies μ(rα) = μ(α) for rational r ≠ 0 (folklore; Murakami-type remarks give μ(1/r) = μ(r)) | the general principle behind the reduction: scaling by a nonzero rational preserves the approximation exponent |
| 3 | WebSearch (named / aliases) | Thue-Siegel-Roth theorem "without loss of generality" alpha algebraic integer proof | partial | Encyclopedia of Mathematics, Wikipedia, Houston notes: statement only; reductions multiply α by a leading coefficient, changing only constants | confirms the step is routine WLOG |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "algebraic integer" | yes | l.1148 Lemma: "If the theorem fails, then it also fails for an irrational real algebraic integer"; proof l.1154–1189 with M α and 2 < κ' < κ | Lean statement matches the source |
| 6 | nLab | "irrationality measure", "Roth's theorem" | no | nLab has no entry on Diophantine approximation exponents | nothing more general |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | Diophantine approximation on ℝ, not algebraic geometry |
| 9 | MathOverflow / Math.SE | "irrationality measure of rational multiple" | yes (standard) | μ(aα + b) = μ(α) for rational a ≠ 0, b; standard exercise | the general fact behind the reduction |
| 10 | recent arXiv | Roth reduction to algebraic integers (arXiv 2412.05867 §4, the Roth formalisation literature) | partial | used inline as a WLOG step | no new generality |

### Literature summary (Phase 3)

Concept identified as: invariance of the approximation (irrationality) exponent under multiplication by a nonzero rational, applied to clear denominators of an algebraic number. This is the standard "WLOG α is an algebraic integer" step in Roth's theorem.
Sources agree on the standard form: yes. Scaling by a nonzero rational preserves the exponent exactly. Only the constant changes.
Most general standard form: for x ∈ ℝ, p ∈ ℝ and r ∈ ℚ \ {0}, x has irrationality exponent ≥ p iff rx does. Combined with "every algebraic number has a nonzero integer multiple that is an algebraic integer", this gives the reduction with the same exponent.
Generality dimensions where the literature varies:
  - constant: fixed constant 1 (paper, `approxSet`) vs arbitrary constant C (standard, mathlib's `LiouvilleWith`). With an arbitrary constant, the exponent is preserved and no κ' < κ is needed.
  - scalar: ℕ vs ℤ vs ℚ multiple; most general is ℚ \ {0}.
Disagreement with the literature: none in substance. The project's form loses exponent (κ → (κ+2)/2) only because `approxSet` fixes the constant 1.

### Generality analysis — `Roth.reduction`

Literature-standard form: `LiouvilleWith p α → ∃ α', IsIntegral ℤ α' ∧ LiouvilleWith p α'` for algebraic α (exponent preserved). This is evidence (1), compiled.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `hα : Irrational α` | hypothesis | not needed in LiouvilleWith form | yes | evidence (1) does not use it; irrationality of α' follows from `LiouvilleWith.irrational` (p > 1). In the `approxSet` form it is needed for `approxSet_den_le_finite`-type finiteness and to transfer irrationality |
| 2 | `hκ : 2 < κ` | hypothesis | any p | yes | evidence (1) works for every p; `2 < κ` only feeds `2 < κ'` |
| 3 | `halg : IsAlgebraic ℚ α` | algebraic over ℚ | algebraic over ℚ | no | needed for the integral multiple |
| 4 | exponent loss κ' = (κ+2)/2 | weaker conclusion | κ' = κ | yes (in LiouvilleWith form) | `approxSet` hard-codes constant 1; `LiouvilleWith` absorbs constants (evidence (1)) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD in the sense that, restated with `LiouvilleWith`, the hypotheses `hα`, `hκ` disappear and the exponent is preserved (compiled, evidence (1), and the project statement is recovered from it in evidence (2)). But this is false-positive class 4/5. The general form is not a new lemma: it is a direct composition of mathlib's `LiouvilleWith.nat_mul` with `Algebra.natDenominator`. Switching from `approxSet` to `LiouvilleWith` is a development-wide restatement (see the Roth.approxSet report), not a single mechanical edit. So the generality gap does not support YES-but-generalise-first.
Number of weakening opportunities found: 3 (drop hα, drop hκ, preserve exponent), all in the LiouvilleWith restatement, compiled.
Proposed restatement (project-optional):

```lean
theorem reduction_liouvilleWith {α p : ℝ} (halg : IsAlgebraic ℚ α) (h : LiouvilleWith p α) :
    ∃ α' : ℝ, IsIntegral ℤ α' ∧ LiouvilleWith p α'
```

Cost of restatement: CHEAP for the lemma itself (2-term proof); MODERATE for the project (requires the approxSet ↔ LiouvilleWith bridges, already compiled).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | hypotheses are numeric/algebraic facts about one real | — |
| 2 | sequences to filters? | yes | `approxSet α κ` infinite to `LiouvilleWith p α` (an `∃ᶠ n in atTop` statement) | the whole `LiouvilleWith` API (`nat_mul`, `mul_rat`, `irrational`, `frequently_lt_rpow_neg`) |
| 3 | construction to universal property? | no | — | — |
| 4 | set to bundled substructure? | no | `approxSet` is a set of pairs, not a substructure; the idiom is the filter predicate in row 2 | — |
| 5 | field-specific to weaker typeclasses? | no | Diophantine approximation is ℝ-specific | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | partial | ℕ multiple to ℚ \ {0} multiple (`LiouvilleWith.mul_rat`) | — |
| 8 | concrete-via-abstract? | no | the proof uses α's algebraicity only via `exists_nat_mul_isIntegral`; the rest is the exponent-scaling fact, which is exactly the abstract `LiouvilleWith.nat_mul` | — |
| 9 | false-generalisation guard | no false generalisation | for irrational α, `approxSet α κ` infinite for some κ > 2 iff `LiouvilleWith p α` for some p > 2 (bridges compiled) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes. Use the `LiouvilleWith` form (evidence (1)). But it is a 2-term composition of existing mathlib lemmas, so the idiomatic version adds no declaration to mathlib.

### Proof strategy — `Roth.reduction`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | yes | the explicit `Set.Infinite.sdiff`/image/injectivity argument is what `LiouvilleWith.nat_mul` already does via `∃ᶠ` | MODERATE (development-wide) |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | yes | as row 1 | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | everything needed is in mathlib (`LiouvilleWith.nat_mul`, `Algebra.natDenominator`, `isIntegral_natDenominator_smul`, `LiouvilleWith.irrational`) | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED (only if the project adopts `LiouvilleWith`)
  - Proposed strategy: state the reduction for `LiouvilleWith` and prove it as `⟨natDenominator α * α, isIntegral_natDenominator_smul α, h.nat_mul _⟩`
  - Cost: CHEAP for the lemma, MODERATE for the project
  - Missing mathlib API (if any): none
  - Would refactoring make the proof strictly shorter / cleaner? yes (14 lines to 3), at the price of the bridge lemmas.

### Diamond / defeq risk

n/a: declaration kind is theorem.

### Mathlib search-status: `Roth.reduction`

[A] Lean-Finder       "if an algebraic real number has irrationality exponent p then some algebraic integer multiple has the same exponent"   hits: `LiouvilleWith.mul_int`, `LiouvilleWith.int_mul`, `LiouvilleWith.mul_int_iff`, `LiouvilleWith.int_mul_iff`, `LiouvilleWith.mul_nat_iff` (the scaling half); no combined reduction lemma.
[B] Loogle            `LiouvilleWith, IsIntegral`: no hits.
[C] LeanSearch        "LiouvilleWith p x implies LiouvilleWith p (n * x) for natural n nonzero"   hits: `LiouvilleWith.mul_nat`, `LiouvilleWith.nat_mul`, `LiouvilleWith.mul_nat_iff`, `LiouvilleWith.nat_mul_iff`, `LiouvilleWith.int_mul`.
[D] Grep mathlib src  `Roth`, `Thue`, `theorem reduction` over Mathlib/*.lean: no Diophantine Roth development (only author names); `LiouvilleWith.nat_mul` at Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean:164, `LiouvilleWith.irrational` at :283; `Algebra.natDenominator`, `isIntegral_natDenominator_smul` in Mathlib/RingTheory/Algebraic/Denominator.lean (used by the exists_nat_mul_isIntegral report).
[E] Name pattern      `lean_local_search` not used (ripgrep missing in earlier runs); replaced by the grep in [D].

Searched for both the user's form (approxSet reduction) and the literature-standard form (exponent invariance under rational scaling plus integral multiple).

Concluded: found building blocks (`LiouvilleWith.nat_mul`, `Algebra.natDenominator`, `isIntegral_natDenominator_smul`, `IsAlgebraic.natDenominator_ne_zero`, `IsFractionRing.isAlgebraic_iff`, `LiouvilleWith.irrational`); composition would yield our form (in LiouvilleWith vocabulary).

### Normal-form check — `Roth.reduction`

Equivalent formalisms: (a) `approxSet α κ` infinite for κ > 2 (project); (b) `LiouvilleWith p α` for p > 2 (mathlib); (c) irrationality exponent > 2.
Does mathlib already have a canonical form? yes: `LiouvilleWith` (its docstring cites Thue-Siegel-Roth as the p > 2 statement).
Our statement is stated against the non-canonical form (a). REFACTOR target (only if upstreamed): (b).
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.reduction`

Alternative restatements attempted:
- current `approxSet` form with exponent loss.
- `LiouvilleWith p α → ∃ α', IsIntegral ℤ α' ∧ LiouvilleWith p α'` (evidence (1)).
Chosen restatement: current form for the project (matches `roth_of_isIntegral`'s `approxSet` interface); LiouvilleWith form for any mathlib-facing version.
Justification: the single caller `Roth.roth` feeds the result directly to `roth_of_isIntegral`, which is stated with `approxSet`.

### Superfluous-argument audit — `Roth.reduction`

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hα : Irrational α` | yes (in this form) | gives `Irrational α'`; superfluous in LiouvilleWith form |
| 2 | `halg` | yes | integral multiple |
| 3 | `hκ : 2 < κ` | only for `2 < κ'` | any κ gives some κ' < κ; the hypothesis is the natural one for the Roth contrapositive |
| 4 | `hinf` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (only if upstreamed: LiouvilleWith)
Syntactic generality: OK for the project
Superfluous arguments: NONE in the current form

Overall: SHIP-AS-STATED for the project; moot for mathlib (verdict is NO)

### Call sites — `Roth.reduction`

Internal use count: 0 outside the declaring file (1 in total)
External-to-file callers: 0 files

| Caller file:line | Usage pattern |
|---|---|
| Roth/Main.lean:576 (`Roth.roth`) | `obtain ⟨α', κ', hα', hint', hκ', hinf'⟩ := reduction hα halg hκ hinf` |

Inline-derivation grep (`exists_nat_mul_isIntegral`, `natCast_mul` across `Roth/`): (none) outside `Roth.reduction`.

### Composition check (Phase 6)

Can `Roth.reduction` be derived from mathlib in ≤3 chained calls?

Attempt 1 (LiouvilleWith form): `⟨natDenominator α * α, isIntegral_natDenominator_smul α, h.nat_mul (IsAlgebraic.natDenominator_ne_zero _)⟩`
  - Mathlib decls used: `Algebra.natDenominator`, `isIntegral_natDenominator_smul`, `IsAlgebraic.natDenominator_ne_zero`, `IsFractionRing.isAlgebraic_iff`, `LiouvilleWith.nat_mul`
  - Result: succeeds (evidence (1), compiled clean)
  - Notes: in mathlib's vocabulary the reduction is a 2-call composition with no exponent loss.
Attempt 2 (project's exact `approxSet` form): evidence (2) derives it from Attempt 1 plus the two `approxSet` ↔ `LiouvilleWith` bridges and `LiouvilleWith.irrational`.
  - Result: succeeds (compiled), but the bridges are project-local (approxSet is project-local), so the `approxSet` form itself is a proof over project API, not a pure mathlib composition.

Conclusion: COMPOSABLE (in mathlib's canonical LiouvilleWith form; the approxSet packaging is project-specific)

## Verdict: `Roth.reduction`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the reduction is the standard "WLOG α is an algebraic integer" step, resting on invariance of the approximation exponent under nonzero rational scaling. The paper states it as §6 Lemma (clean.tex l.1148), and no other source states it as a standalone theorem.
- Generality analysis (Phase 4): strictly narrower than the LiouvilleWith form (exponent preserved, hα and hκ unnecessary, compiled), but the general form is itself a mathlib composition (false-positive class 4) and switching vocabulary is development-wide (class 5).
- Mathlib search (Phase 5): building blocks `LiouvilleWith.nat_mul`, `Algebra.natDenominator`, `isIntegral_natDenominator_smul`, `LiouvilleWith.irrational`; no combined lemma, none needed.
- Composition check (Phase 6): COMPOSABLE (2 calls, compiled).

**Rationale:**

The mathematical content of the reduction is two facts: an algebraic number has a positive integer multiple that is an algebraic integer, and multiplying by a nonzero integer does not change the approximation exponent. Mathlib has both: `Algebra.natDenominator` with `isIntegral_natDenominator_smul`, and `LiouvilleWith.nat_mul` (Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean:164). In mathlib's canonical vocabulary for Roth-type statements (`LiouvilleWith`, whose docstring already names Thue-Siegel-Roth), the reduction is the compiled one-term composition `reduction_liouvilleWith`, and it is stronger than the project statement: it keeps the exponent p, needs no irrationality and no 2 < p.

The 14-line project proof, with its κ → (κ+2)/2 exponent loss, the `approxSet_den_le_finite` sdiff and the injective image, exists only because the project's `approxSet` hard-codes the constant 1 in 1/q^κ. That set is itself NO-composable (Roth.approxSet report). Mathlib would not accept a lemma about `approxSet`, and the `LiouvilleWith` version is a composition. So there is nothing to upstream.

WHY not: mathlib has the building blocks, and in mathlib's canonical form the statement is `⟨natDenominator α * α, isIntegral_natDenominator_smul α, h.nat_mul _⟩`. The project form is tied to the project-local `approxSet`.
Belongs-elsewhere check: keep project-local in Roth/Main.lean. It is the paper's §6 Lemma, step 1 of the module's proof outline, and keeps `Roth.roth` a 3-line proof. If the development is ever upstreamed, it should be restated with `LiouvilleWith` (then this lemma becomes the composition below and need not be a named declaration).
Mathlib building blocks:
- `LiouvilleWith.nat_mul` — Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean:164
- `LiouvilleWith.irrational` — Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean:283
- `Algebra.natDenominator`, `isIntegral_natDenominator_smul`, `IsAlgebraic.natDenominator_ne_zero` — Mathlib/RingTheory/Algebraic/Denominator.lean
- `IsFractionRing.isAlgebraic_iff`
Composition sketch:
```lean
example {α p : ℝ} (halg : IsAlgebraic ℚ α) (h : LiouvilleWith p α) :
    ∃ α' : ℝ, IsIntegral ℤ α' ∧ LiouvilleWith p α' :=
  ⟨natDenominator α * α, by simpa [nsmul_eq_mul] using isIntegral_natDenominator_smul α,
    h.nat_mul ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 halg).natDenominator_ne_zero⟩
```
Call sites in our project (from Phase 6.0): 1 (Roth/Main.lean:576, `Roth.roth`)
Refactor plan: none required while the project uses `approxSet`. If the project switches to `LiouvilleWith` (per the Roth.approxSet report), replace the call at Roth/Main.lean:576 by `reduction_liouvilleWith halg (liouvilleWith_of_approxSet_infinite hα hinf)` followed by `approxSet_infinite_of_liouvilleWith` as in evidence (2), and delete `Roth.reduction`. Inlining it now is not recommended: it would replace a documented paper step with an equally long proof plus two bridges.
Next action: keep `Roth.reduction` as is. Do not upstream.

## Next step

Keep the lemma project-local (single call site `Roth.roth`). Nothing to upstream. The mathlib-facing form is the two-call composition `reduction_liouvilleWith` in the evidence file.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.reduction/liouvilleWith_reduction.lean` (imports `Roth.Main`, LiouvilleWith, Algebraic.Denominator). It contains (1) `reduction_liouvilleWith`, the composition in mathlib vocabulary; the two `approxSet` ↔ `LiouvilleWith` bridges copied from the Roth.approxSet evidence; (2) the project's exact statement recovered from (1) and the bridges; (3) a reference use of `Roth.reduction`. `lean_diagnostic_messages` reports no errors and no warnings.
- WebSearch ×3 (see table). Lean-Finder ×1, LeanSearch ×1, Loogle ×1 (no hits). Grep of mathlib for `Roth`, `Thue`, `theorem reduction`, `LiouvilleWith`. Grep of clean.tex for "algebraic integer". The ChatGPT MCP was unavailable in this session.
