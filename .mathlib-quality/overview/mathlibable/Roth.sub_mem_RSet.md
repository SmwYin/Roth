---
decl: Roth.sub_mem_RSet
file: Roth/MainLemma.lean
line: 388
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: The difference of two distinct boxFamily members lies in RSet B r; the proof is an anonymous constructor of three mathlib facts (sub_ne_zero, MvPolynomial.degreeOf_sub_le, abs_sub_le_of_nonneg_of_le) about two project-local sets that are themselves NO-composable, and mathlib's own Siegel lemma inlines the identical step, so nothing to upstream.
action: Do not upstream; keep in Roth/MainLemma.lean as the named Lemma 9 step (sole caller exists_mem_RSet_le_index_aux at Roth/MainLemma.lean:560), or optionally inline the three-term composition there; no mathlib PR.
---

# Roth.sub_mem_RSet

## Inventory entry

### `theorem Roth.sub_mem_RSet`
- **Type**: `∀ {σ : Type*} {r : σ → ℕ} {B : ℕ} {W' W'' : MvPolynomial σ ℤ}, W' ∈ Roth.boxFamily r B → W'' ∈ Roth.boxFamily r B → W' ≠ W'' → W' - W'' ∈ Roth.RSet (↑B) r`
- **What**: If `W'` and `W''` are distinct members of the family `𝒲` (degree at most `r j` in each variable `X j`, every coefficient in `[0, B]`), then `W' - W''` is nonzero, still has degree at most `r j` in each variable, and has every coefficient of absolute value at most `B`; that is, it lies in `ℛ(B; r)`.
- **How**: `refine` with three components: `sub_ne_zero.2 hne`; `(MvPolynomial.degreeOf_sub_le j W' W'').trans (max_le ..)`; and for coefficients `rw [MvPolynomial.coeff_sub, ← Int.cast_abs]` followed by `exact_mod_cast abs_sub_le_of_nonneg_of_le` applied to the four box bounds.
- **Hypotheses**: `h' : W' ∈ boxFamily r B`, `h'' : W'' ∈ boxFamily r B`, `hne : W' ≠ W''`. No finiteness of `σ` or of the support of `r`.
- **Uses from project**: `Roth.boxFamily`, `Roth.RSet`
- **Used by**: `Roth.exists_mem_RSet_le_index_aux` (private, Roth/MainLemma.lean:560). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 388–394, proof length 4 lines
- **Notes**: Source clean.tex §6, proof of Lemma 9 (line 1511): `W^*` is not identically zero and its coefficients do not exceed `B_1` in absolute value.

## Junk check (Step 8)
- Used anywhere? Yes, once (`exists_mem_RSet_le_index_aux`, MainLemma.lean:560), where its `.1` component is also reused.
- Wrapper of 1–2 mathlib calls? It combines three mathlib facts (`sub_ne_zero`, `MvPolynomial.degreeOf_sub_le`, `abs_sub_le_of_nonneg_of_le`) into the project's `RSet` membership. It is a thin bridge between two project-local sets.
- Does mathlib have it? No: `boxFamily` and `RSet` are project-local (no `namespace Roth` in mathlib). The generic coefficient fact is `abs_sub_le_of_nonneg_of_le` / `Int.natAbs_coe_sub_coe_le_of_le`.
- Too specific (inline?)? It could be inlined into its single caller, but it states one sentence of the source proof, keeps the private main-lemma assembly readable, and is stated without finiteness hypotheses. Inlining saves nothing significant.
- Well-chosen? Yes.
- Conclusion: `KEEP`. Action: none (optional inline at MainLemma.lean:560).

## Mathlibable assessment (Step 9)

Pre-filter: public, name not `_aux`, docstring not internal, Step 8 KEEP, qualified name absent from mathlib. Not pure glue (it uses `degreeOf_sub_le` and an absolute-value inequality, not just unfolding), so a full run follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; evidence file importing `Roth.MainLemma` elaborates)
- decl `Roth.sub_mem_RSet`:  ✓ resolved at Roth/MainLemma.lean:388
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's Lemma 9 (main lemma): construction of an auxiliary polynomial of large index at (α, …, α) via a pigeonhole argument on the box family.

### Statement (Phase 1)

`Roth.sub_mem_RSet` is a theorem stating the following: let `𝒲` be the set of integer polynomials in variables indexed by `σ` with `deg_{x_j} W ≤ r_j` and every coefficient in `{0, …, B}`. If `W', W'' ∈ 𝒲` are distinct then `W^* = W' − W''` is a nonzero integer polynomial with `deg_{x_j} W^* ≤ r_j` and every coefficient of absolute value at most `B`, i.e. `W^* ∈ ℛ_m(B; r)`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variable index set (arbitrary).
- `r : σ → ℕ` — degree bounds per variable.
- `B : ℕ` — coefficient bound.
- `W' W'' : MvPolynomial σ ℤ` — the two box polynomials.

Hypotheses (Lean side):
- `h' : W' ∈ boxFamily r B`, `h'' : W'' ∈ boxFamily r B` — membership in `𝒲`.
- `hne : W' ≠ W''` — distinctness (gives nonvanishing of the difference).

Conclusion (math): `W' − W'' ∈ ℛ_m(B; r)`.

Conclusion (Lean): `W' - W'' ∈ Roth.RSet (↑B) r`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-step helper lemma inside the proof of Lemma 9; not a main result, no new structure, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: n/a
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form) | Roth theorem proof Lemma 9 W* = W' - W'' auxiliary polynomial coefficients absolute value do not exceed B | yes | difference of two distinct polynomials with the B_1-property has integer coefficients bounded by B_1 | arXiv math/0307203 (quantitative Roth–Ridout) states exactly this as an inline step of the auxiliary-polynomial construction |
|  2 | WebSearch (general form) | Siegel lemma pigeonhole difference of two polynomials coefficients bounded by B nonzero auxiliary polynomial | yes | Thue–Siegel pigeonhole: two vectors in [0,B]^N with equal image; their difference is a nonzero solution with entries in [-B,B] | Wikipedia Siegel's lemma; arXiv 1310.6482 polynomial version; always an inline proof step, never a stated lemma |
|  3 | WebSearch (aliases) | difference set of integer box [0,B]^n contained in [-B,B]^n Minkowski lattice point argument | partial | [0,B]^n − [0,B]^n ⊆ [-B,B]^n, used in Blichfeldt/Minkowski-type arguments | treated as an obvious remark; no named result |
|  4 | ChatGPT MCP | n/a | n/a | n/a | n/a: `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
|  5 | Local references | grep `.mathlib-quality/references/clean.tex` for "not identically zero", "B_1" | yes | line 1511: "Also W^* is not identically zero, and its coefficients in absolute value do not exceed B_1" | the exact source sentence the lemma formalises; an inline remark |
|  6 | nLab | box polynomials / Siegel's lemma | no | none | nLab has no entry for Siegel's lemma or auxiliary polynomials; elementary number theory not covered |
|  7 | nCatLab | n/a | n/a | n/a | not a categorical concept (an elementary inequality about integer coefficients) |
|  8 | Stacks Project | n/a | n/a | n/a | not an algebraic-geometry concept; Stacks does not cover Diophantine approximation |
|  9 | MathOverflow / Math.SE | "Siegel's lemma difference of two solutions bounded" | no new | same inline pigeonhole-difference step as #2 | no separate named statement; consistent with #2 |
| 10 | recent arXiv | auxiliary polynomial pigeonhole difference coefficient bound (seen via #1, #2: arXiv 1806.10737, 2303.02037) | yes | same inline step | step reused in every auxiliary-polynomial argument, never isolated |

### Literature summary (Phase 3)

Concept identified as: the "difference of two pigeonholed box elements" step of the Thue–Siegel–Roth auxiliary-polynomial (Siegel's lemma) method.
Sources agree on the standard form: yes — if `x, y ∈ [0,B]^N` are distinct then `x − y ≠ 0` and `x − y ∈ [-B,B]^N`; for polynomials, degree bounds are preserved by subtraction.
Most general standard form: for any linearly ordered additive group, `0 ≤ a, b ≤ n ⇒ |a − b| ≤ n` (applied coefficientwise), plus `deg_{x_j}(p − q) ≤ max(deg_{x_j} p, deg_{x_j} q)`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ in the literature; the coefficient inequality holds in any linearly ordered additive group.
  - interval: `[0,B]` vs `[a, a+B]` — the difference bound only needs an interval of length `B`.
Disagreement with the literature: none. The literature never isolates this as a lemma.

### Generality analysis — `Roth.sub_mem_RSet`

Literature-standard form (from Phase 3): coefficientwise `|a − b| ≤ n` for `a, b ∈ [0,n]`, plus subtraction preserving degree bounds.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `σ : Type*` | arbitrary | finite set of variables | no (already more general) | no finiteness assumed |
| 2 | coefficient ring ℤ | fixed by `boxFamily`/`RSet` | ℤ | only by changing the project defs | `RSet` is a set of integer polynomials (paper notation); the generic ring fact is mathlib's `abs_sub_le_of_nonneg_of_le` (evidence example 2) |
| 3 | `h'`, `h''` | box membership | box membership | no | all three components (degree, lower, upper bound) are used |
| 4 | `hne` | `W' ≠ W''` | distinct | no | needed for `W' − W'' ≠ 0` in `RSet` |
| 5 | `B : ℕ` | natural | integer bound | no | `boxFamily` takes `B : ℕ`; `RSet` receives its cast |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (relative to the two project defs it connects)
Number of weakening opportunities found: 0
Proposed restatement: none. The only generalisation (arbitrary ordered coefficient ring) is a statement about mathlib primitives that mathlib already has as `abs_sub_le_of_nonneg_of_le`; compiled in evidence example 2.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | typeclasses instead of bundled hypotheses? | no | membership hypotheses are the natural form | — |
| 2 | sequences/metric → filters? | no | finite algebraic statement, no topology | — |
| 3 | construction → universal property? | no | no construction | — |
| 4 | set-with-predicate → bundled substructure? | no | `RSet` is not closed under any operation (it excludes 0); bundling makes no sense | — |
| 5 | field-specific → weaker typeclasses? | no | ℤ is fixed by the paper's definitions; the generic coefficient fact is already in mathlib | — |
| 6 | 1-categorical → higher? | no | not categorical | — |
| 7 | concrete index → general monoid? | no | degree index ℕ is intrinsic to `degreeOf` | — |
| 8 | concrete-via-abstract? | yes (trivially) | after unfolding, the proof only uses `degreeOf_sub_le` and `abs_sub_le_of_nonneg_of_le` — both already abstract mathlib lemmas | none new; the abstract content is already in mathlib |
| 9 | false-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
- One-line reason: the abstract content is exactly two existing mathlib lemmas; the lemma itself only bridges two Roth-specific set notations.

### Proof strategy — `Roth.sub_mem_RSet`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ where filters would compose? | no | — | — |
| 2 | elementwise where ideals/submodules would abstract? | no | — | — |
| 3 | sequences where nets would generalise? | no | — | — |
| 4 | construction where universal property would characterise? | no | — | — |
| 5 | missing mathlib helpers? | no | all three facts exist (`sub_ne_zero`, `MvPolynomial.degreeOf_sub_le`, `abs_sub_le_of_nonneg_of_le`) | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.sub_mem_RSet`

[A] Lean-Finder       "if 0 ≤ a ≤ n and 0 ≤ b ≤ n then |a - b| ≤ n"   hits: `abs_sub_le_of_nonneg_of_le`, `Int.natAbs_coe_sub_coe_le_of_le` (building blocks)
[B] Loogle            `|?a - ?b| ≤ ?n`                                  hits only generic abs lemmas (`abs_sub`, `abs_sub_nonpos`, ...); no polynomial-box lemma
[C] LeanSearch        "difference of two multivariate polynomials with degree in each variable at most r and coefficients in [0,B] has coefficients bounded by B"   hits: `MvPolynomial.degreeOf_sub_le`, `MvPolynomial.coeff_sub`, `Polynomial.natDegree_sub_le_of_le` (building blocks); no combined statement
[D] Grep mathlib src  `boxPoly`, `abs_sub_le_of_nonneg_of_le`, `sub_ne_zero.mpr hneq` in `Mathlib/NumberTheory/`   `Polynomial.boxPoly` (MahlerMeasure.lean:55) has no difference lemma; `Mathlib/NumberTheory/SiegelsLemma.lean:163-174` re-derives the same step inline (`x - y`, `sub_ne_zero.mpr hneq`, coordinatewise `|x i - y i| ≤ B` by `lia`)
[E] Name pattern      `lean_local_search` / grep for `sub_mem_RSet`, `sub_mem_boxPoly`, `namespace Roth`   no hits in mathlib

Searched for both:
  - the user's current form (box family / RSet)
  - the literature-standard form (coefficientwise difference bound; degree of a difference)

Concluded: found building blocks (`sub_ne_zero`, `MvPolynomial.degreeOf_sub_le`, `MvPolynomial.coeff_sub`, `abs_sub_le_of_nonneg_of_le`); composition yields our form. Mathlib's Siegel lemma inlines the identical step rather than naming it.

### Normal-form check — `Roth.sub_mem_RSet`

Equivalent formalisms: membership `W' - W'' ∈ RSet B r`; the unfolded triple (`≠ 0`, degree bounds, coefficient bounds).
Does mathlib already have a canonical form? No (project-local sets).
Our statement is stated against the project's canonical set `RSet`, which is what callers consume. RHS convention: n/a (not an iff/equation).

### Syntactic generality — `Roth.sub_mem_RSet`

Alternative restatements attempted:
- unfolded conjunction instead of `∈ RSet`
- coefficient-only form over an ordered ring (evidence example 2)

Chosen restatement: current membership form.
Justification: the single caller needs `RSet` membership directly (and its `.1`); the membership form applies in one term.

### Superfluous-argument audit — `Roth.sub_mem_RSet`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `h'` | yes | degree and both coefficient bounds of `W'` |
| 2 | `h''` | yes | same for `W''` |
| 3 | `hne` | yes | nonvanishing clause of `RSet` |
| 4 | finiteness of `σ` / support of `r` | not assumed | already dropped |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE
Overall: SHIP-AS-STATED (locally; not proposed for mathlib)

### Call sites — `Roth.sub_mem_RSet`

Internal use count: 1 (in the declaring file; 0 outside it)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:560 | `have hP := sub_mem_RSet hW' hW'' hne` (in private `exists_mem_RSet_le_index_aux`; `hP` and `hP.1` reused) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.sub_mem_RSet`?):
  - (none in the project). In mathlib, `Mathlib/NumberTheory/SiegelsLemma.lean:163-174` re-derives the analogous vector step inline.

### Composition check (Phase 6)

Can `Roth.sub_mem_RSet` be derived from mathlib in ≤3 chained calls?

Attempt 1: `⟨sub_ne_zero.2 hne, fun j ↦ (degreeOf_sub_le j W' W'').trans (max_le (h'.1 j) (h''.1 j)), fun d ↦ by rw [coeff_sub, ← Int.cast_abs]; exact_mod_cast abs_sub_le_of_nonneg_of_le ..⟩`
  - Mathlib decls used: `sub_ne_zero`, `MvPolynomial.degreeOf_sub_le`, `MvPolynomial.coeff_sub`, `Int.cast_abs`, `abs_sub_le_of_nonneg_of_le`
  - Result: succeeds (compiled in `evidence/Roth.sub_mem_RSet/composition.lean`, example 1)
  - Notes: one mathlib call per component of `RSet`, plus a cast normalisation.

Conclusion: COMPOSABLE (three component calls; the cast step is a `rw` + `exact_mod_cast`)

## Verdict: `Roth.sub_mem_RSet`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the step appears only inline (clean.tex line 1511; arXiv math/0307203; Siegel's lemma proofs); no named statement anywhere.
- Generality analysis (Phase 4): MAXIMALLY GENERAL relative to the project defs; no weakening available.
- Mathlib search (Phase 5): building blocks `sub_ne_zero`, `MvPolynomial.degreeOf_sub_le`, `abs_sub_le_of_nonneg_of_le` found; mathlib's Siegel lemma inlines the same step.
- Composition check (Phase 6): COMPOSABLE.

**Rationale:**

The lemma links two Roth-specific set notations, the box family `𝒲` (`Roth.boxFamily`, NO-composable-from-mathlib) and `ℛ_m(B; r)` (`Roth.RSet`, NO-composable-from-mathlib). Neither set is going to mathlib, so a membership lemma between them has no upstream home. Its mathematical content is one mathlib fact per component of `RSet`: `sub_ne_zero` for nonvanishing, `MvPolynomial.degreeOf_sub_le` for the degree bounds, and `abs_sub_le_of_nonneg_of_le` for the coefficient bound. All three are already in mathlib at full generality. The literature treats this step as a one-sentence remark, and mathlib's own `Int.exists_ne_zero_int_vec_norm_le` (Siegel's lemma) re-derives the analogous vector step inline instead of calling a named lemma.

If `boxFamily` is ever upstreamed as a multivariate `Polynomial.boxPoly` (see `Roth.boxFamily.md`, `Roth.ncard_boxFamily.md`), a "difference of two box elements has coefficients in `[B₁ − B₂, B₂ − B₁]`" lemma might go with it. That would be a new statement about the new mathlib def, not this lemma.

WHY not:
- Mathlib has the building blocks, and the statement is a three-component anonymous-constructor composition over two project-local sets.

Belongs-elsewhere check: keep it project-local in `Roth/MainLemma.lean`. It is the named formalisation of the source sentence "W^* is not identically zero, and its coefficients in absolute value do not exceed B_1".

Mathlib building blocks:
- `sub_ne_zero` (Mathlib/Algebra/Group/Basic.lean)
- `MvPolynomial.degreeOf_sub_le` (Mathlib/Algebra/MvPolynomial/CommRing.lean:132)
- `MvPolynomial.coeff_sub` (Mathlib/Algebra/MvPolynomial/CommRing.lean)
- `abs_sub_le_of_nonneg_of_le` (Mathlib/Algebra/Order/Group/Abs.lean)

Composition sketch (≤3 lines):
```lean
example (h' : W' ∈ boxFamily r B) (h'' : W'' ∈ boxFamily r B) (hne : W' ≠ W'') : W' - W'' ∈ RSet B r :=
  ⟨sub_ne_zero.2 hne, fun j ↦ (degreeOf_sub_le j W' W'').trans (max_le (h'.1 j) (h''.1 j)), fun d ↦ by
    rw [coeff_sub, ← Int.cast_abs]; exact_mod_cast abs_sub_le_of_nonneg_of_le (h'.2 d).1 (h'.2 d).2 (h''.2 d).1 (h''.2 d).2⟩
```

Call sites in our project (from Phase 6.0): 1 (Roth/MainLemma.lean:560).

Refactor plan: no mathlib PR. Locally, keep the lemma, since it names a source step and makes the private assembly in `exists_mem_RSet_le_index_aux` readable. If inlining is preferred, replace `have hP := sub_mem_RSet hW' hW'' hne` at Roth/MainLemma.lean:560 with the composition above. The arguments match exactly, and `hP.1` is still available as the first component.

Next action: none for mathlib; keep `Roth.sub_mem_RSet` next to `boxFamily` in Roth/MainLemma.lean (optionally inline it at line 560).

---

## Next step

Do not upstream. Keep `Roth.sub_mem_RSet` locally as the named Lemma 9 step. Optionally inline the three-component composition at its sole call site Roth/MainLemma.lean:560.

## Evidence
- `grep -rn sub_mem_RSet Roth/`: definition at MainLemma.lean:388; one use at MainLemma.lean:560.
- Parent reports read: `.mathlib-quality/overview/mathlibable/Roth.RSet.md` and `Roth.boxFamily.md` (both NO-composable-from-mathlib), plus `Roth.ncard_boxFamily.md` and `Roth.one_mem_RSet.md`.
- Mathlib grep: `Mathlib/NumberTheory/SiegelsLemma.lean:156-174` (the same step inline), `Mathlib/NumberTheory/MahlerMeasure.lean:55` (`boxPoly`, no difference lemma), `Mathlib/Data/Int/Lemmas.lean:67-73` (`Int.natAbs_coe_sub_coe_le_of_le`).
- Searches: Lean-Finder, Loogle and LeanSearch queries as listed in Phase 5. Three WebSearch queries as listed in Phase 3. ChatGPT MCP: n/a (not configured in this session).
- Evidence file `.mathlib-quality/overview/evidence/Roth.sub_mem_RSet/composition.lean` (imports `Roth.MainLemma`). Example 1 is the inline composition proving the exact statement. Example 2 is the coefficient bound over any linearly ordered commutative ring. Checked with `lean_diagnostic_messages`: no errors, and only a module-docstring placement style warning.
