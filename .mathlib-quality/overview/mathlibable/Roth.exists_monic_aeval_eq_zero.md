---
decl: Roth.exists_monic_aeval_eq_zero
file: Roth/Main.lean
line: 142
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: INLINE
rationale: The statement is the definition of IsIntegral (or minpoly.monic plus minpoly.aeval) padded by X^2 to force degree at least 2; it is a compiled one-term composition of minpoly.monic, Monic.mul, monic_X_pow and natDegree_mul_X_pow, and the degree bound is an artificial padding device rather than mathematical content.
action: Inline at its single call site Roth.exists_roth_parameters_aux (Roth/Main.lean:415) as the term from evidence/Roth.exists_monic_aeval_eq_zero/composition.lean (minpoly ℤ α * X ^ 2), then delete the lemma; or keep it as the paper's §6 sentence with its body replaced by that term.
---

# Roth.exists_monic_aeval_eq_zero

## Inventory entry

### `theorem Roth.exists_monic_aeval_eq_zero`
- **Type**: `{α : ℝ} (hint : IsIntegral ℤ α) : ∃ f : Polynomial ℤ, f.Monic ∧ Polynomial.aeval α f = 0 ∧ 2 ≤ f.natDegree`
- **What**: An algebraic integer is a root of a monic integer polynomial of degree at least 2.
- **How**: Destructures `hint` (the `IsIntegral` definition gives a monic `f` with `eval₂ (algebraMap ℤ ℝ) α f = 0`), takes `f * X ^ 2`, gets monicity from `Monic.mul` with `monic_X_pow 2`, the root from `map_mul`, `aeval_def` and `zero_mul`, and the degree bound from `simp` (via `natDegree_mul_X_pow` and `Monic.ne_zero`).
- **Hypotheses**: `hint : IsIntegral ℤ α`.
- **Uses from project**: `[]`
- **Used by**: Roth/Main.lean: `Roth.exists_roth_parameters_aux` (private, line 415). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 142–147, proof length 4 lines
- **Notes**: The docstring cites clean.tex §6 (l.1201–1205), where the paper gets degree at least 2 from irrationality. The Lean proof does not use irrationality. It pads by `X ^ 2`, so the witness may be reducible, as the docstring says. The only consumer uses `2 ≤ f.natDegree` as a numeric bound (`nlinarith only [hm, hdeg]`) and never needs `f` irreducible or minimal.

## Junk check (Step 8)
- Used anywhere? Once, in the private `Roth.exists_roth_parameters_aux` (Main.lean:415).
- Wrapper of 1–2 mathlib calls? Yes. It is the `IsIntegral` definition plus `Monic.mul (monic_X_pow 2)`. Equivalently it is one anonymous-constructor term over `minpoly.monic`, `minpoly.aeval` (through `simp`) and `natDegree_mul_X_pow` (compiled in the evidence file).
- Does mathlib have it? Not in this shape: no mathlib lemma produces a monic annihilating polynomial of degree at least `n`. Mathlib's canonical witness is `minpoly`. `minpoly.two_le_natDegree_iff` gives `2 ≤ natDegree (minpoly A x) ↔ x ∉ range (algebraMap A B)`, which is the paper's genuine route, but over a non-field base ℤ it would need the ℤ ⊂ ℝ range argument from irrationality.
- Too specific (inline?)? Yes. It has one call site and the composition is one term.
- Well-chosen? The `X ^ 2` padding is a technical device to meet a numeric bound. It is not a meaningful mathematical statement, so it does not deserve its own API.

Conclusion: INLINE. At `Roth.exists_roth_parameters_aux`, replace the `obtain` with the term from the evidence file and delete the lemma. If the project wants to keep the paper sentence as a named lemma, the alternative is to keep it with that one-term body.

## Mathlibable assessment (Step 9)

Pre-filter: the theorem is public. Its name does not end in `_aux`, and its docstring is not internal or auxiliary. Step 8 said INLINE, not REMOVE. A namespace-aware grep of `.lake/packages/mathlib/Mathlib/` finds no `Roth.exists_monic_aeval_eq_zero`. Mathlib has unrelated `Polynomial.exists_monic_aeval_eq_zero_forall_mem_*` lemmas with different names and content, in RingTheory/IntegralClosure/Algebra/Ideal.lean. It is not a glue lemma: the proof builds a new witness, `f * X ^ 2`, rather than unfolding the definition. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Main` compiled with no diagnostics)
- decl `Roth.exists_monic_aeval_eq_zero`: resolved at Roth/Main.lean:142
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's theorem for real algebraic numbers, reduced via §6 to irrational real algebraic integers and proved via §7.

### Statement (Phase 1)

`Roth.exists_monic_aeval_eq_zero` is a theorem stating the following:

If a real number α is an algebraic integer, then there is a monic polynomial f ∈ ℤ[x] of degree at least 2 with f(α) = 0.

Variables / typeclasses involved (Lean side):
- `α : ℝ`: the algebraic integer.

Hypotheses (Lean side):
- `hint : IsIntegral ℤ α`: α is a root of a monic integer polynomial.

Conclusion (math): α is a root of a monic integer polynomial of degree ≥ 2.

Conclusion (Lean): `∃ f : Polynomial ℤ, f.Monic ∧ Polynomial.aeval α f = 0 ∧ 2 ≤ f.natDegree`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper used once in the parameter-choice lemma of §7. It is a restatement of a definition with a padding trick.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

n/a: kind is theorem. MULTI-LINE (4-line proof); check skipped.

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | "algebraic integer root of monic integer polynomial definition degree at least 2 irrational" | yes | algebraic integer = root of a monic polynomial in ℤ[x]; irrational ones have minimal degree ≥ 2 | Wikipedia "Algebraic integer", Stein ANT notes, Kedlaya notes |
| 2 | WebSearch (general form) | "element integral over ring root of monic polynomial of any sufficiently large degree multiply by power of X" | partial | the definition of integral element over any commutative ring; no source states the "any large degree" padding as a lemma | ProofWiki, mathlib docs. Padding by a power of X is folklore and trivial |
| 3 | WebSearch (named / aliases) | "\"integral over\" ring equivalent definitions monic polynomial finitely generated module x^n" | yes | equivalent characterisations of integrality (monic relation, R[x] finitely generated, faithful finite module) | Waterloo notes, Hochster notes, ProofWiki. None includes a degree lower bound |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP is not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "algebraic integer, by definition" | yes | §6 l.1201–1205: by definition there is a monic integer f with f(α)=0, "Its degree n is at least 2, since α is irrational" | the paper's degree bound comes from irrationality (minimal-degree argument); the Lean statement drops irrationality and pads instead |
| 6 | nLab | "monic polynomial", "integral element" | yes (concept) | definition of monic polynomial and integral element | no degree-bound lemma |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | integral ring maps chapter (Tag 00GH area) | partial | definition of integral element via monic relation | no degree-bound variant |
| 9 | MathOverflow / Math.SE | "algebraic integer degree at least 2 irrational" | yes (standard) | an irrational algebraic number has minimal degree ≥ 2; trivial | no new generality |
| 10 | recent arXiv | "monic polynomial algebraic integer degree" | no | nothing beyond the definition | the statement is too elementary to appear as a result |

### Literature summary (Phase 3)

Concept identified as: the definition of algebraic integer (integral element over ℤ), with a degree lower bound.
Sources agree on the standard form: yes. An element is integral when it is a root of a monic polynomial over the base ring.
Most general standard form: for a commutative ring R and an R-algebra A, x ∈ A is integral over R iff some monic p ∈ R[x] has p(x) = 0. Multiplying p by x^n gives such a p of degree ≥ n for every n, provided R is nontrivial.
Generality dimensions where the literature varies:
  - base ring: ℤ up to any commutative ring (nontrivial for the degree bound).
  - ambient: ℂ / ℝ up to any R-algebra.
  - degree bound: none in the definition; the paper's "≥ 2" uses irrationality and the minimal polynomial. The Lean version gets any bound n by padding.
Disagreement with the literature: the paper derives degree ≥ 2 from irrationality, which is meaningful for the minimal polynomial. The Lean statement gets it by padding, which is meaningless as mathematics but enough for the downstream numeric use.

### Generality analysis — `Roth.exists_monic_aeval_eq_zero`

Literature-standard form: `IsIntegral R x ↔ ∃ p, Monic p ∧ eval₂ (algebraMap R A) x p = 0` (mathlib's definition), with the canonical witness `minpoly R x` (`minpoly.monic`, `minpoly.aeval`).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | base ring ℤ | ℤ | any nontrivial CommRing R | yes | the proof uses only `Monic.mul`, `monic_X_pow`, `natDegree_mul_X_pow`, `Monic.ne_zero` (needs Nontrivial). Compiled in the evidence file |
| 2 | `α : ℝ` | real number | element of any `[Ring A] [Algebra R A]` | yes | ℝ is never used. Compiled |
| 3 | degree bound `2` | fixed constant 2 | any `n : ℕ` | yes | `X ^ n` padding. Compiled |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (ℤ, ℝ and 2 all generalise; verified in evidence/Roth.exists_monic_aeval_eq_zero/composition.lean, which compiles `exists_monic_aeval_eq_zero_le_natDegree` for `[CommRing R] [Nontrivial R] [Ring A] [Algebra R A]` and any `n`). The generalised form is still a one-term composition of mathlib primitives (`IsIntegral` / `minpoly` plus `Monic.mul (monic_X_pow n)`). That is false-positive class 4 territory (the content is already in mathlib), and the generalisation does not create a lemma mathlib would want.
Number of weakening opportunities found: 3 (base ring, ambient algebra, degree bound), all compiled.
Proposed restatement: `theorem exists_monic_aeval_eq_zero_le_natDegree {R A : Type*} [CommRing R] [Nontrivial R] [Ring A] [Algebra R A] {x : A} (hx : IsIntegral R x) (n : ℕ) : ∃ f : R[X], f.Monic ∧ aeval x f = 0 ∧ n ≤ f.natDegree`. Not proposed for upstreaming.
Cost of restatement: CHEAP.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | single Prop hypothesis | — |
| 2 | sequences to filters? | no | algebraic, no topology | — |
| 3 | construction to universal property? | partial | the canonical witness is `minpoly`, characterised by minimality | already in mathlib |
| 4 | set to bundled substructure? | no | — | — |
| 5 | field-specific to weaker typeclasses? | yes | any nontrivial CommRing R and any R-algebra A | already in mathlib via `IsIntegral` / `minpoly` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | the constant 2 to any n | trivial padding, not API-worthy |
| 8 | concrete-via-abstract? | yes | the proof never uses ℝ, ℤ or 2 beyond the padding exponent; the abstract form is the definition of `IsIntegral` | already in mathlib |
| 9 | false-generalisation guard | no false generalisation | the generalisations keep the meaning | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes, but already in mathlib. The idiomatic witness is `minpoly ℤ α`, with `minpoly.monic` and `minpoly.aeval`. If the minimal degree were really needed, `minpoly.two_le_natDegree_iff` / `minpoly.two_le_natDegree_subalgebra` is the paper's route. The degree-padding variant adds no organisational value.

### Proof strategy — `Roth.exists_monic_aeval_eq_zero`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | partial | use `minpoly ℤ α` as the base witness instead of destructuring `IsIntegral` | CHEAP |
| 5 | missing mathlib helpers | no | everything needed exists | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (as a proof). For the call site, REFACTOR-RECOMMENDED: inline the one-term composition.
  - Proposed strategy: `⟨minpoly ℤ α * X ^ 2, (minpoly.monic hint).mul (monic_X_pow 2), by simp, by simp [(minpoly.monic hint).ne_zero]⟩`
  - Cost: CHEAP (no new imports; `Roth.Main` already imports `Mathlib.RingTheory.Algebraic.Integral`, and the evidence compiled against `Roth.Main`)
  - Missing mathlib API: none
  - Would refactoring make the proof strictly shorter / cleaner? yes. It replaces a separate lemma with one term.

### Diamond / defeq risk

n/a: declaration kind is theorem.

### Mathlib search-status: `Roth.exists_monic_aeval_eq_zero`

[A] Lean-Finder       "if x is integral over R then for every n there is a monic polynomial of degree at least n with x as root"   hits: `IsIntegral` (definition), `minpoly.monic`, `IsIntegral.of_aeval_monic`, `Polynomial.exists_monic_aeval_eq_zero_forall_mem_pow_of_isIntegral` (different content: coefficients in ideal powers). None has a degree lower bound.
[B] Loogle            `IsIntegral, Polynomial.Monic, Polynomial.natDegree`   hits: `IsIntegral.of_aeval_monic`, `IsIntegral.of_aeval_monic_of_isIntegral_coeff`, `Polynomial.exists_monic_aeval_eq_zero_forall_mem_pow_of_isIntegral`, `isIntegral_of_isIntegralElem_of_monic_of_natDegree_lt`. None matches.
[C] LeanSearch        "integral element is root of monic polynomial of arbitrarily large degree"   hits: `AdjoinRoot.isIntegral_root'`, `IsIntegral.of_aeval_monic`, `isInteger_of_is_root_of_monic`, `minpoly.IsIntegrallyClosed.isIntegral_iff_leadingCoeff_dvd`. None matches.
[D] Grep mathlib src  `IsIntegral` combined with `≤ .*natDegree` / `X ^ n` / `monic_X_pow`; `def IsIntegral`; `minpoly` `theorem monic` / `theorem aeval`   hits: `IsIntegral` def (RingTheory/IntegralClosure/IsIntegral/Defs.lean:53), `minpoly.monic` (FieldTheory/Minpoly/Basic.lean:54), `minpoly.aeval` (:89), `minpoly.two_le_natDegree_iff` (:225), `minpoly.two_le_natDegree_subalgebra` (:230), `Polynomial.Monic.mul` (Algebra/Polynomial/Monic.lean:85), `Polynomial.natDegree_mul_X_pow` (Algebra/Polynomial/Degree/Operations.lean:524)
[E] Name pattern      `exists_monic_aeval_eq_zero` grep in mathlib   hits only `Polynomial.exists_monic_aeval_eq_zero_forall_mem_of_mem_map` / `_pow_of_isIntegral` / `_pow_of_mem_map` (different statements, about coefficients in ideals). `lean_local_search` not used (ripgrep unavailable in earlier runs); replaced by grep.

Searched for both the user's form (monic, root, degree ≥ 2) and the literature-standard form (`IsIntegral` definition, `minpoly`).

Concluded: found building blocks (`IsIntegral` def / `minpoly.monic` + `minpoly.aeval`, `Polynomial.Monic.mul`, `Polynomial.monic_X_pow`, `Polynomial.natDegree_mul_X_pow`); composition yields our form.

### Normal-form check — `Roth.exists_monic_aeval_eq_zero`

Equivalent formalisms: (a) `IsIntegral ℤ α` (mathlib definition, eval₂ form); (b) `∃ f, Monic f ∧ aeval α f = 0`; (c) `minpoly ℤ α` with `minpoly.monic` / `minpoly.aeval`; (d) our padded form with `2 ≤ natDegree`.
Does mathlib already have a canonical form? yes: (a), with (c) as the canonical witness.
Our statement is a non-canonical variant of (a) with an artificial degree bound.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.exists_monic_aeval_eq_zero`

Alternative restatements attempted:
- the generalised `exists_monic_aeval_eq_zero_le_natDegree` (any R, A, n): compiled.
- the inline `minpoly ℤ α * X ^ 2` term: compiled.
Chosen restatement: the inline term at the single call site.
Justification: the caller destructures `f, hf, hfα, hdeg` and only needs the numeric bound, which the anonymous constructor supplies directly.

### Superfluous-argument audit — `Roth.exists_monic_aeval_eq_zero`

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `α : ℝ` (type ℝ) | no (ℝ itself) | any ring algebra works (compiled) |
| 2 | base ring ℤ | no (ℤ itself) | any nontrivial CommRing works (compiled) |
| 3 | `hint : IsIntegral ℤ α` | yes | it supplies the monic relation |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (use `IsIntegral` / `minpoly` directly)
Syntactic generality: RESTATE (inline term)
Superfluous arguments: 2 specialisations (ℝ, ℤ) plus the fixed constant 2

Overall: RESTATE-BEFORE-SHIP (moot: verdict is NO)

### Call sites — `Roth.exists_monic_aeval_eq_zero`

Internal use count: 1 (in the declaring file; no other files)
External-to-file callers: 0

| Caller file:line | Usage pattern |
|---|---|
| Roth/Main.lean:415 (`Roth.exists_roth_parameters_aux`, private) | `obtain ⟨f, hf, hfα, hdeg⟩ := exists_monic_aeval_eq_zero hint`; `hdeg` used only in `nlinarith only [hm, hdeg]` |

Inline-derivation grep: (none). No other place in `Roth/` builds a monic integer annihilator.

### Composition check (Phase 6)

Can `Roth.exists_monic_aeval_eq_zero` be derived from mathlib in ≤3 chained calls?

Attempt 1: `⟨minpoly ℤ α * X ^ 2, (minpoly.monic hint).mul (monic_X_pow 2), by simp, by simp [(minpoly.monic hint).ne_zero]⟩`
  - Mathlib decls used: `minpoly.monic`, `minpoly.aeval` (simp), `Polynomial.Monic.mul`, `Polynomial.monic_X_pow`, `Polynomial.natDegree_mul_X_pow` (simp), `Polynomial.Monic.ne_zero`
  - Result: succeeds (compiled clean in evidence/Roth.exists_monic_aeval_eq_zero/composition.lean)
Attempt 2 (current proof): destructure the `IsIntegral` definition, then the same `Monic.mul (monic_X_pow 2)` padding. Also works.

Conclusion: COMPOSABLE (one anonymous-constructor term; two trivial `simp` closings)

## Verdict: `Roth.exists_monic_aeval_eq_zero`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): this is the definition of algebraic integer. The paper's degree ≥ 2 comes from irrationality via the minimal polynomial. The Lean form replaces that with padding.
- Generality analysis (Phase 4): STRICTLY NARROWER (ℤ, ℝ and 2 all generalise; compiled), but the general form is still a one-term composition of the `IsIntegral` / `minpoly` API (false-positive class 4).
- Mathlib search (Phase 5): building blocks found: `IsIntegral`, `minpoly.monic`, `minpoly.aeval`, `Polynomial.Monic.mul`, `Polynomial.monic_X_pow`, `Polynomial.natDegree_mul_X_pow`.
- Composition check (Phase 6): COMPOSABLE (compiled term).

**Rationale:**

Mathlib's `IsIntegral ℤ α` is by definition `∃ p, Monic p ∧ eval₂ (algebraMap ℤ ℝ) α p = 0`, and `minpoly ℤ α` is the canonical witness (`minpoly.monic`, `minpoly.aeval`). The only extra content here is `2 ≤ f.natDegree`, which the proof obtains by multiplying by `X ^ 2`. That device works for any degree bound and does not use irrationality. It is not a mathematical statement mathlib would want: a degree lower bound on some non-canonical annihilator is meaningless, and the meaningful version, a lower bound on the minimal polynomial's degree, is already `minpoly.two_le_natDegree_iff` / `minpoly.two_le_natDegree_subalgebra`. Even generalised to any nontrivial commutative ring, any algebra and any n (compiled), the statement remains a one-term composition.

WHY not: mathlib has the building blocks, and the statement is a one-term composition of `minpoly.monic`, `minpoly.aeval`, `Polynomial.Monic.mul`, `Polynomial.monic_X_pow` and `Polynomial.natDegree_mul_X_pow`.
Belongs-elsewhere check: keeping it project-local as the paper's §6 sentence is acceptable. Nothing goes upstream.
Mathlib building blocks:
- `minpoly.monic` — Mathlib/FieldTheory/Minpoly/Basic.lean:54
- `minpoly.aeval` — Mathlib/FieldTheory/Minpoly/Basic.lean:89
- `Polynomial.Monic.mul` — Mathlib/Algebra/Polynomial/Monic.lean:85
- `Polynomial.monic_X_pow` — Mathlib/Algebra/Polynomial/Monic.lean
- `Polynomial.natDegree_mul_X_pow` — Mathlib/Algebra/Polynomial/Degree/Operations.lean:524
- (alternative base) `IsIntegral` — Mathlib/RingTheory/IntegralClosure/IsIntegral/Defs.lean:53
Composition sketch:
```lean
example {α : ℝ} (hint : IsIntegral ℤ α) :
    ∃ f : ℤ[X], f.Monic ∧ aeval α f = 0 ∧ 2 ≤ f.natDegree :=
  ⟨minpoly ℤ α * X ^ 2, (minpoly.monic hint).mul (monic_X_pow 2), by simp,
    by simp [(minpoly.monic hint).ne_zero]⟩
```
Call sites in our project (from Phase 6.0): 1
Refactor plan: in `Roth.exists_roth_parameters_aux` (Roth/Main.lean:415), replace `obtain ⟨f, hf, hfα, hdeg⟩ := exists_monic_aeval_eq_zero hint` with `obtain ⟨f, hf, hfα, hdeg⟩ : ∃ f : Polynomial ℤ, f.Monic ∧ Polynomial.aeval α f = 0 ∧ 2 ≤ f.natDegree := ⟨minpoly ℤ α * Polynomial.X ^ 2, (minpoly.monic hint).mul (Polynomial.monic_X_pow 2), by simp, by simp [(minpoly.monic hint).ne_zero]⟩`. The rest of the lemma uses only `f`, `hf`, `hfα` and `hdeg`, so nothing else changes. No new import is needed.
Next action: delete `Roth.exists_monic_aeval_eq_zero` and inline the term at `Roth.exists_roth_parameters_aux`. Alternatively, keep the name for paper fidelity with the one-term body.

## Next step

Inline the `minpoly ℤ α * X ^ 2` term at `Roth.exists_roth_parameters_aux` (Roth/Main.lean:415) and delete the lemma, or keep it as the §6 sentence with that body. Do not upstream.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.exists_monic_aeval_eq_zero/composition.lean`. It imports `Roth.Main` and contains (1) the `minpoly` one-term composition proving the exact statement, (2) the generalisation `exists_monic_aeval_eq_zero_le_natDegree` over `[CommRing R] [Nontrivial R] [Ring A] [Algebra R A]` with any degree bound `n`, (3) the project statement derived from (2), and (4) a reference use of the project lemma. `lake env lean` compiled it with no errors or warnings (~39 s).
- WebSearch ×3 (see table). Lean-Finder, LeanSearch and Loogle queries as recorded. Grep of mathlib for `IsIntegral` with natDegree bounds and `X ^ n`, the `IsIntegral` definition, `minpoly.monic` / `minpoly.aeval` / `two_le_natDegree_*`, and `Monic.mul` / `natDegree_mul_X_pow`. Grep of clean.tex §6. ChatGPT MCP unavailable in this session.
