---
decl: Roth.exists_nat_mul_isIntegral
file: Roth/Main.lean
line: 62
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: INLINE
rationale: The statement is the ℚ-to-ℤ, ℕ-valued specialisation of IsAlgebraic.exists_integral_multiple; mathlib's Algebra.natDenominator API (natDenominator_ne_zero plus isIntegral_natDenominator_smul, with IsFractionRing.isAlgebraic_iff) gives it as a compiled one-term composition, in any commutative ℚ-algebra, so there is nothing new to upstream.
action: Inline at its single call site Roth.reduction (Roth/Main.lean:121) by taking M := Algebra.natDenominator α (add import Mathlib.RingTheory.Algebraic.Denominator), then delete the lemma; or keep it as the paper's §6 Lemma with its body replaced by the composition in evidence/Roth.exists_nat_mul_isIntegral/composition.lean.
---

# Roth.exists_nat_mul_isIntegral

## Inventory entry

### `theorem Roth.exists_nat_mul_isIntegral`
- **Type**: `{α : ℝ} (hα : IsAlgebraic ℚ α) : ∃ M : ℕ, 0 < M ∧ IsIntegral ℤ ((M : ℝ) * α)`
- **What**: Every real algebraic number has a positive integer multiple that is an algebraic integer.
- **How**: Transfers algebraicity from `ℚ` to `ℤ` with `IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ`, applies `IsAlgebraic.exists_integral_multiple` to get `y ≠ 0 : ℤ` with `y • α` integral, takes `M = y.natAbs` (`Int.natAbs_pos`), and fixes the sign with `IsIntegral.zsmul` by `y.sign` and `Int.sign_mul_self` inside a `simpa`.
- **Hypotheses**: `hα : IsAlgebraic ℚ α`.
- **Uses from project**: `[]`
- **Used by**: Roth/Main.lean: `Roth.reduction` (line 121). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 62–67, proof length 4 lines
- **Notes**: Source: clean.tex §6 Lemma (l.1154): "If α is an algebraic number, there is an integer M>0 such that Mα is an algebraic integer." Mathlib now has `Algebra.natDenominator` (Mathlib/RingTheory/Algebraic/Denominator.lean), which supplies the canonical (least) such `M`. Roth.Main does not currently import that file.

## Junk check (Step 8)
- Used anywhere? Once, in `Roth.reduction` (Main.lean:121).
- Wrapper of 1–2 mathlib calls? Yes. It is `IsAlgebraic.exists_integral_multiple` after the `ℚ → ℤ` transfer, plus sign bookkeeping. With mathlib's `Algebra.natDenominator` API the whole statement is one anonymous-constructor term of three mathlib lemmas (compiled in the evidence file).
- Does mathlib have it? Not under this name or shape (∃ M : ℕ, 0 < M ∧ IsIntegral ℤ (M * α) for ℚ-algebraic α). Its content is in `IsAlgebraic.exists_integral_multiple`, `IsAlgebraic.exists_nsmul_eq` (integral-closure form, ℤ-algebraic), and `Algebra.natDenominator` with `IsAlgebraic.natDenominator_ne_zero` and `Algebra.isIntegral_natDenominator_smul`. The closest exact-shape statement is `NumberField.exists_nat_le_mulHeight₁`, which is specific to number fields.
- Too specific (inline?)? It has one call site. The composition is one term, so inlining at `reduction` is mechanical.
- Well-chosen? It matches the paper's §6 Lemma word for word, which the project values. It does not justify a separate mathlib lemma.

Conclusion: INLINE. At `Roth.reduction`, obtain `M := Algebra.natDenominator α` with the composition from the evidence file, then delete the lemma. If the project wants to keep the paper-lemma name, the alternative is to keep it and replace its body with that composition.

## Mathlibable assessment (Step 9)

Pre-filter: the theorem is public. Its name does not end in `_aux`, and its docstring is not internal or auxiliary. Step 8 said INLINE, not REMOVE. A namespace-aware grep finds no `Roth.exists_nat_mul_isIntegral` in `.lake/packages/mathlib/Mathlib/`. It is not a glue lemma (`rfl`/unfolding). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Main` elaborates with no diagnostics)
- decl `Roth.exists_nat_mul_isIntegral`: resolved at Roth/Main.lean:62
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's theorem for real algebraic numbers, reduced via §6 to irrational real algebraic integers and proved via §7.

### Statement (Phase 1)

`Roth.exists_nat_mul_isIntegral` is a theorem stating the following:

If α ∈ ℝ is algebraic over ℚ, then there is a positive integer M such that Mα is an algebraic integer, i.e. Mα is a root of a monic polynomial with integer coefficients.

Variables / typeclasses involved (Lean side):
- `α : ℝ`: the algebraic number.

Hypotheses (Lean side):
- `hα : IsAlgebraic ℚ α`: α is a root of a nonzero rational polynomial.

Conclusion (math): some positive integer multiple of α is an algebraic integer.

Conclusion (Lean): `∃ M : ℕ, 0 < M ∧ IsIntegral ℤ ((M : ℝ) * α)`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper lemma used once in the §6 reduction. It is a classical textbook fact, not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

n/a: kind is theorem. MULTI-LINE (4-line proof); check skipped.

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | "algebraic number integer multiple is algebraic integer leading coefficient lemma" | yes | for α in a number field K there is a nonzero c ∈ ℤ with cα ∈ O_K; the leading coefficient of a vanishing polynomial works | Bristol lecture notes (Lemma 1); Isabelle AFP `algebraic_imp_algebraic_int` (leading-coefficient form) |
| 2 | WebSearch (general form) | "element algebraic over domain R nonzero r in R such that r x integral over R fraction field" | partial | over any domain R: if a_n x^n + … = 0 with a_n ≠ 0, then a_n x is integral | commutative algebra notes (Gotti, Gathmann). This is mathlib's `IsAlgebraic.exists_integral_multiple` (any CommRing R) |
| 3 | WebSearch (named / aliases) | "denominator of an algebraic number definition smallest positive integer d with d alpha algebraic integer" | yes | the denominator d(α) is the positive generator of the ideal {k ∈ ℤ : kα integral} | arXiv 2211.13822, arXiv 2106.01311, MaRDI entry. Matches mathlib's `Algebra.natDenominator` exactly |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP is not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "algebraic integer" | yes | §6 Lemma l.1154: "there is an integer M>0 such that Mα is an algebraic integer"; proof multiplies by a power of the leading coefficient | the Lean statement matches the source |
| 6 | nLab | "algebraic integer" | yes (concept) | algebraic integer = root of a monic integer polynomial; clearing denominators is folklore | no separate entry for the multiple lemma |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | "integral over" / Tag 00GH area (integral extensions) | partial | localisation and integral-closure statements; x algebraic over a domain A has a nonzero a ∈ A with ax integral (standard lemma in the integral-extension chapter) | same general form as #2 |
| 9 | MathOverflow / Math.SE | "multiply algebraic number by integer to get algebraic integer" | yes (standard) | the leading-coefficient trick; a frequently asked basic question | no generality beyond #2 |
| 10 | recent arXiv | "denominator algebraic number" (arXiv 2211.13822, 2106.01311) | yes | d(γ) divides c(γ), which divides d(γ)^n; d(γ) is the ideal generator | refines #3; no new generality |

### Literature summary (Phase 3)

Concept identified as: "every algebraic number has an integer multiple that is an algebraic integer" (clearing denominators); the canonical witness is the denominator of α.
Sources agree on the standard form: yes.
Most general standard form: for any commutative ring R and R-algebra A, if z ∈ A is algebraic over R then y•z is integral over R for some nonzero y ∈ R. For R = ℤ, the y with y•z integral form a principal ideal, generated by the denominator.
Generality dimensions where the literature varies:
  - base ring: ℤ (number theory) up to an arbitrary commutative ring (commutative algebra); the most general is an arbitrary CommRing.
  - ambient: ℂ / number field / arbitrary algebra; the most general is an arbitrary algebra.
  - witness: any nonzero multiplier, the leading coefficient, or the least one (the denominator).
Disagreement with the literature: none. The user's form is the specialisation R = ℤ, A = ℝ, with algebraicity stated over ℚ = Frac ℤ and the multiplier taken in ℕ.

### Generality analysis — `Roth.exists_nat_mul_isIntegral`

Literature-standard form: `IsAlgebraic R z → ∃ y ≠ 0, IsIntegral R (y • z)` over any CommRing R (mathlib's `IsAlgebraic.exists_integral_multiple`), plus the denominator refinement for ℤ (`Algebra.natDenominator`).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `α : ℝ` | real number | element of any (commutative) ℚ-algebra / any R-algebra | yes | the proof never uses ℝ. The evidence file compiles the same composition for any `[CommRing A] [Algebra ℚ A]` |
| 2 | `IsAlgebraic ℚ α` | algebraic over ℚ | algebraic over R (here ℤ) | equivalent | `IsFractionRing.isAlgebraic_iff ℤ ℚ` makes these the same |
| 3 | `M : ℕ, 0 < M` | positive natural multiplier | nonzero y ∈ R | equivalent for ℤ | ℕ-valued positivity is the ℤ-specific refinement; mathlib's `natDenominator` gives it |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (ℝ could be any commutative ℚ-algebra; verified in the evidence file). The general form is already in mathlib (`IsAlgebraic.exists_integral_multiple` and `Algebra.natDenominator`), so this is false-positive class 4 ("general form already in mathlib"). It does not route to YES-but-generalise-first.
Number of weakening opportunities found: 1 (ℝ to an arbitrary commutative ℚ-algebra), compiled.
Proposed restatement: none to upstream. The general statement is mathlib's.
Cost of restatement: CHEAP (n/a for upstreaming).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | single hypothesis already a Prop predicate | — |
| 2 | sequences to filters? | no | algebraic, no topology | — |
| 3 | construction to universal property? | no | — | — |
| 4 | set to bundled substructure? | partial | the ideal of clearing multipliers is mathlib's colon ideal `(integralClosure ℤ S).colon {x}`, generated by `Algebra.denominator` | already in mathlib |
| 5 | field-specific to weaker typeclasses? | yes | any CommRing R in place of ℤ, any algebra in place of ℝ | already `IsAlgebraic.exists_integral_multiple` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | ℕ multiplier to ring element y | already in mathlib |
| 8 | concrete-via-abstract? | yes | the proof never uses ℝ after the statement; abstract form = mathlib lemma | already in mathlib |
| 9 | false-generalisation guard | no false generalisation | ℝ to commutative ℚ-algebra keeps the meaning | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes, but already in mathlib. The idiomatic form is `Algebra.natDenominator α` together with `IsAlgebraic.natDenominator_ne_zero` and `Algebra.isIntegral_natDenominator_smul`. It gives the canonical least multiplier rather than an existential. There is nothing to contribute; the project should use it.

### Proof strategy — `Roth.exists_nat_mul_isIntegral`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | yes | the colon-ideal / `Algebra.natDenominator` API replaces the `natAbs`/`sign` bookkeeping | CHEAP |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | everything is in `Mathlib/RingTheory/Algebraic/Denominator.lean` | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: `⟨natDenominator α, Nat.pos_of_ne_zero (isAlgebraic_iff ℤ ℚ ℝ).2 hα |>.natDenominator_ne_zero, by simpa [nsmul_eq_mul] using isIntegral_natDenominator_smul α⟩`
  - Cost: CHEAP (one extra import)
  - Missing mathlib API: none
  - Would refactoring make the proof strictly shorter / cleaner? yes. It removes the `sign`/`natAbs` bookkeeping and gives the canonical witness.

### Diamond / defeq risk

n/a: declaration kind is theorem.

### Mathlib search-status: `Roth.exists_nat_mul_isIntegral`

[A] Lean-Finder       "every algebraic element over ℚ has a nonzero natural multiple integral over ℤ"   hits: `IsAlgebraic.exists_integral_multiple`, `IsAlgebraic.iff_exists_smul_integral`, `Algebra.IsAlgebraic.exists_integral_multiples` (more general, ring-element multiplier)
[B] Loogle            `IsAlgebraic, IsIntegral, Nat`   no hits (the ℕ form is not stated with these constants)
[C] LeanSearch        "algebraic number has a positive natural number multiple that is an algebraic integer"   hits: `IsAlgebraic.exists_integral_multiple`, `IsIntegral.nsmul`, `IsAlgebraic.nsmul`
[D] Grep mathlib src  `exists_integral_multiple`, `exists_nonzero_dvd`, `isIntegral_leadingCoeff_smul`, `IsIntegral ℤ` with nat/nsmul, `natDenominator`   hits: `IsAlgebraic.exists_integral_multiple` (RingTheory/Algebraic/Integral.lean:146), `IsAlgebraic.exists_nonzero_dvd` (Algebraic/Basic.lean:564, divisibility form, not integrality), `isIntegral_leadingCoeff_smul` (leading-coefficient form, needs an explicit polynomial), `IsAlgebraic.exists_nsmul_eq` (Integral.lean:207, ℕ multiple into an integral closure, ℤ-algebraic), `Algebra.natDenominator`, `Algebra.isIntegral_natDenominator_smul`, `IsAlgebraic.natDenominator_ne_zero` (RingTheory/Algebraic/Denominator.lean:66–90), `NumberField.exists_nat_le_mulHeight₁` (NumberTheory/Height/NumberField.lean:306, number-field-specific)
[E] Name pattern      `lean_local_search natDenominator`   n/a: ripgrep not on PATH; replaced by the grep in [D]

Searched for both the user's form (ℕ multiple, ℚ-algebraic) and the literature-standard form (nonzero ring-element multiple; denominator).

Concluded: found building blocks (`IsFractionRing.isAlgebraic_iff`, `IsAlgebraic.natDenominator_ne_zero`, `Algebra.isIntegral_natDenominator_smul`); composition would yield our form. The more general ring-element form is `IsAlgebraic.exists_integral_multiple`.

### Normal-form check — `Roth.exists_nat_mul_isIntegral`

Equivalent formalisms: (a) ∃ M : ℕ, 0 < M ∧ IsIntegral ℤ (M * α); (b) ∃ y ≠ 0 : ℤ, IsIntegral ℤ (y • α); (c) `natDenominator α ≠ 0` together with `IsIntegral ℤ (natDenominator α • α)`.
Does mathlib already have a canonical form? yes: (b) as `IsAlgebraic.exists_integral_multiple`, and (c) via `Algebra.natDenominator`.
Our statement is a non-canonical existential variant. Mathlib would not want it alongside (b) and (c).
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.exists_nat_mul_isIntegral`

Alternative restatements attempted:
- (b) ℤ-multiplier form: needs sign handling at the call site, which uses `M : ℕ` (via `Irrational.natCast_mul`).
- (c) `natDenominator` form: supplies `M` directly with the needed positivity and integrality.
Chosen restatement: (c) at the call site.
Justification: the caller needs a positive natural number, and `natDenominator` is exactly that.

### Superfluous-argument audit — `Roth.exists_nat_mul_isIntegral`

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `α : ℝ` (type ℝ) | no (ℝ itself) | any commutative ℚ-algebra works (compiled) |
| 2 | `hα : IsAlgebraic ℚ α` | yes | without it the denominator is 0 (mathlib's `example` on `X : ℤ[X]`) |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (use `Algebra.natDenominator`, or `IsAlgebraic.exists_integral_multiple`)
Syntactic generality: RESTATE (natDenominator form)
Superfluous arguments: 1 (the ℝ specialisation)

Overall: RESTATE-BEFORE-SHIP (moot: verdict is NO)

### Call sites — `Roth.exists_nat_mul_isIntegral`

Internal use count: 1 (in the declaring file; no other files)
External-to-file callers: 0

| Caller file:line | Usage pattern |
|---|---|
| Roth/Main.lean:121 (`Roth.reduction`) | `obtain ⟨M, hM0, hMint⟩ := exists_nat_mul_isIntegral halg` |

Inline-derivation grep: (none). No other place re-derives an integral multiple.

### Composition check (Phase 6)

Can `Roth.exists_nat_mul_isIntegral` be derived from mathlib in ≤3 chained calls?

Attempt 1: `⟨natDenominator α, Nat.pos_of_ne_zero ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 hα).natDenominator_ne_zero, by simpa [nsmul_eq_mul] using isIntegral_natDenominator_smul α⟩`
  - Mathlib decls used: `IsFractionRing.isAlgebraic_iff`, `IsAlgebraic.natDenominator_ne_zero`, `Algebra.isIntegral_natDenominator_smul` (plus `Nat.pos_of_ne_zero`, `nsmul_eq_mul`)
  - Result: succeeds (compiled clean in evidence/Roth.exists_nat_mul_isIntegral/composition.lean, needs `import Mathlib.RingTheory.Algebraic.Denominator`)
Attempt 2 (current proof): `IsAlgebraic.exists_integral_multiple` plus `natAbs`/`sign` bookkeeping. This also works, but the sign fix is a small proof, not a pure composition.

Conclusion: COMPOSABLE (one term, three mathlib lemmas plus a trivial `simpa [nsmul_eq_mul]` cast)

## Verdict: `Roth.exists_nat_mul_isIntegral`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): a classical clearing-denominators fact. The general form is "algebraic over R ⇒ nonzero R-multiple integral"; the canonical witness is the denominator.
- Generality analysis (Phase 4): STRICTLY NARROWER (ℝ is inessential, compiled), but the general form is mathlib's (false-positive class 4).
- Mathlib search (Phase 5): building blocks found: `IsAlgebraic.exists_integral_multiple`, `Algebra.natDenominator`, `IsAlgebraic.natDenominator_ne_zero`, `Algebra.isIntegral_natDenominator_smul`, `IsFractionRing.isAlgebraic_iff`.
- Composition check (Phase 6): COMPOSABLE, a compiled one-term composition.

**Rationale:**

The lemma is the specialisation R = ℤ, A = ℝ of `IsAlgebraic.exists_integral_multiple`, with algebraicity transferred from ℚ = Frac ℤ and the multiplier made a positive natural number. Since `Mathlib/RingTheory/Algebraic/Denominator.lean`, mathlib has the canonical witness `Algebra.natDenominator α`, together with `IsAlgebraic.natDenominator_ne_zero` (positivity for ℤ-algebraic elements) and `Algebra.isIntegral_natDenominator_smul` (integrality). The composition above proves the project's exact statement in one term, and in fact over any commutative ℚ-algebra. It does not depend on `IsAlgebraic.exists_nonzero_dvd` (a divisibility statement) or `isIntegral_leadingCoeff_smul` (which needs an explicit polynomial); those are the lower-level routes.

There is therefore no gap for a new mathlib lemma. An ℕ-valued existential next to `natDenominator` would be a non-canonical duplicate. The only project value of the name is fidelity to the paper's §6 Lemma.

WHY not: mathlib has the building blocks, and the statement is a one-term composition of `IsFractionRing.isAlgebraic_iff`, `IsAlgebraic.natDenominator_ne_zero` and `Algebra.isIntegral_natDenominator_smul`.
Belongs-elsewhere check: keeping it project-local (as the paper's §6 Lemma) is acceptable. Nothing goes upstream.
Mathlib building blocks:
- `IsFractionRing.isAlgebraic_iff` — Mathlib/RingTheory/Localization/Integral.lean:106
- `IsAlgebraic.natDenominator_ne_zero` — Mathlib/RingTheory/Algebraic/Denominator.lean:87
- `Algebra.isIntegral_natDenominator_smul` — Mathlib/RingTheory/Algebraic/Denominator.lean:76
- (general form) `IsAlgebraic.exists_integral_multiple` — Mathlib/RingTheory/Algebraic/Integral.lean:146
Composition sketch:
```lean
example {α : ℝ} (hα : IsAlgebraic ℚ α) : ∃ M : ℕ, 0 < M ∧ IsIntegral ℤ ((M : ℝ) * α) :=
  ⟨Algebra.natDenominator α,
    Nat.pos_of_ne_zero ((IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 hα).natDenominator_ne_zero,
    by simpa [nsmul_eq_mul] using Algebra.isIntegral_natDenominator_smul α⟩
```
Call sites in our project (from Phase 6.0): 1
Refactor plan: add `import Mathlib.RingTheory.Algebraic.Denominator` to Roth/Main.lean. In `Roth.reduction` (Main.lean:121), replace `obtain ⟨M, hM0, hMint⟩ := exists_nat_mul_isIntegral halg` with the composition above, destructured the same way (or set `M := Algebra.natDenominator α` with `hM0` and `hMint` from the two mathlib lemmas). The rest of `reduction` uses only `M : ℕ`, `0 < M` and `IsIntegral ℤ (M * α)`, so nothing else changes.
Next action: delete `Roth.exists_nat_mul_isIntegral` and inline the composition at `Roth.reduction`. Alternatively, keep the name for paper fidelity and replace its 4-line body with the composition.

## Next step

Inline the `Algebra.natDenominator` composition at `Roth.reduction` (Roth/Main.lean:121) and delete the lemma, or keep it as the §6 Lemma with the composition as its body. Do not upstream.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.exists_nat_mul_isIntegral/composition.lean`. It imports `Roth.Main` and `Mathlib.RingTheory.Algebraic.Denominator` and contains (1) the composition proving the exact statement over ℝ, (2) the same composition over any `[CommRing A] [Algebra ℚ A]`, and (3) a reference use of the project lemma. `lake env lean` compiled it with no errors or warnings. A first run without the Denominator import failed with unknown identifiers, which shows Roth.Main does not import that file today.
- WebSearch ×3 (see table). Lean-Finder, LeanSearch and Loogle queries as recorded. Grep of mathlib for `exists_integral_multiple`, `exists_nonzero_dvd`, `isIntegral_leadingCoeff_smul`, `natDenominator`, `IsIntegral ℤ`. `lean_local_search` unavailable (ripgrep missing). ChatGPT MCP unavailable in this session.
