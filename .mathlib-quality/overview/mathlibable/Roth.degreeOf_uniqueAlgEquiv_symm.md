---
decl: Roth.degreeOf_uniqueAlgEquiv_symm
file: Roth/Separation.lean
line: 174
kind: theorem
visibility: public
verdict: YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Mathlib's new uniqueAlgEquiv (2026-04) has coeff and monomial API but no degree API, while its siblings finSuccEquiv and optionEquivLeft both have natDegree = degreeOf lemmas; the forward twin natDegree_uniqueAlgEquiv plus this symm form compile over any CommSemiring with mathlib-only imports and the names are free.
action: Upstream `MvPolynomial.natDegree_uniqueAlgEquiv` and `MvPolynomial.degreeOf_uniqueAlgEquiv_symm` (proofs in evidence reaim.lean) to Mathlib/Algebra/MvPolynomial/Equiv.lean after coeff_uniqueAlgEquiv_symm; until then keep the project lemma for its 2 call sites (Separation.lean:226, Theta.lean:427), then delete it and use the mathlib name.
---

# Roth.degreeOf_uniqueAlgEquiv_symm

## Inventory entry

### `theorem Roth.degreeOf_uniqueAlgEquiv_symm`
- **Type**: `∀ {R : Type*} [CommSemiring R] {σ : Type*} [Unique σ] (f : Polynomial R), degreeOf default ((uniqueAlgEquiv R σ).symm f) = f.natDegree`
- **What**: If you view a univariate polynomial `f` as a polynomial in the single variable indexed by a singleton type `σ`, its degree in that variable equals `f.natDegree`.
- **How**: `le_antisymm`. For `≤`, `degreeOf_le_iff` reduces to support monomials `e`. Then `MvPolynomial.coeff_uniqueAlgEquiv_symm` turns `e ∈ support` into `f.coeff (e default) ≠ 0`, and `Polynomial.le_natDegree_of_ne_zero` closes it. For `≥`, `Polynomial.natDegree_le_iff_coeff_eq_zero` reduces to `n` above the degreeOf, and `MvPolynomial.notMem_support_of_degreeOf_lt` applied at `Finsupp.single default n`, combined with `coeff_uniqueAlgEquiv_symm` and `Finsupp.single_eq_same`, closes it.
- **Hypotheses**: `[CommSemiring R]` and `[Unique σ]` only.
- **Uses from project**: `[]` (the `coeff_uniqueAlgEquiv_symm` calls are explicitly qualified `MvPolynomial.`, so they refer to mathlib's lemma, not `Roth.coeff_uniqueAlgEquiv_symm`)
- **Used by**: `Roth.degreeOf_none_rename_mul_aeval` (Roth/Separation.lean:226, `.trans (degreeOf_uniqueAlgEquiv_symm V)`); `Roth.index_separated_mul_le_aux` (private, Roth/Theta.lean:427, `rw [..., degreeOf_uniqueAlgEquiv_symm]`). Both are bare-name uses that resolve to `Roth.` (no mathlib decl of that name exists).
- **Visibility**: public
- **Lines**: 173-185, proof length 10 lines
- **Notes**: Docstring has no source citation. Lives in `section General` (`[CommSemiring R]`) of Roth/Separation.lean.

## Junk check (Step 8)
- Used anywhere? Yes, at 2 call sites in 2 files (Separation.lean:226, Theta.lean:427).
- Wrapper of 1-2 mathlib calls? No. It is a 10-line two-sided support argument.
- Does mathlib have it? No (Phase 5). `uniqueAlgEquiv` has `coeff`, `monomial` and `eval₂` lemmas only. There is no degree lemma for it in either direction.
- Too specific (inline)? No. It is a natural basic-API fact about a mathlib equivalence.
- Well-chosen? Yes. Mathlib would want the forward `natDegree_uniqueAlgEquiv` as the primary form, with this as a one-line corollary.
- **Conclusion: `KEEP`** locally until upstreamed, then replace it with the mathlib lemma.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name does not end in `_aux`; docstring not internal/auxiliary; Step 8 = KEEP; the qualified names `Roth.degreeOf_uniqueAlgEquiv_symm` and `MvPolynomial.degreeOf_uniqueAlgEquiv_symm` are both absent from mathlib (grep, plus a clash-free declaration in the evidence file). It is not a glue lemma, so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file compiles with no diagnostics)
- decl `Roth.degreeOf_uniqueAlgEquiv_symm`: resolved at Roth/Separation.lean:174
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`) in polynomials over `Option τ`, towards Lemma 2 of the source (`F = U(x_τ) V(x_none)`).

### Statement (Phase 1)

`Roth.degreeOf_uniqueAlgEquiv_symm` is a theorem stating the following:

Let `R` be a commutative semiring and `σ` a one-element type, so `R[x_σ] ≅ R[X]`. For `f ∈ R[X]`, the degree of the corresponding polynomial in the variable `x_*` equals the degree of `f` (with `deg 0 = 0`).

Variables / typeclasses involved (Lean side):
- `R : Type*`, `[CommSemiring R]`: coefficients.
- `σ : Type*`, `[Unique σ]`: the singleton variable index.
- `f : Polynomial R`.

Hypotheses (Lean side):
- none.

Conclusion (math): `deg_{x_*}(f(x_*)) = natDeg f`.

Conclusion (Lean): `degreeOf default ((uniqueAlgEquiv R σ).symm f) = f.natDegree`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a basic API lemma for an existing mathlib equivalence; not a structure or main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 10
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | degree of polynomial in one variable equals degree in that variable of multivariate polynomial ring in one indeterminate isomorphism R[X] | partial | isomorphism `R[x_σ] ≅ R[X]` for singleton σ (ProofWiki "Uniqueness of Polynomial Ring in One Variable", Mizar Watase 2023 forma-2023-0001) | degree compatibility treated as immediate; no named statement |
| 2 | WebSearch (general form) | partial degree deg_{x_i} multivariate polynomial definition maximum exponent univariate degree special case | yes | partial degree = max exponent of x_i (Wikipedia "Degree of a polynomial"); reduces to the ordinary degree in one variable | folklore |
| 3 | WebSearch (aliases / mathlib) | Mathlib MvPolynomial uniqueAlgEquiv pUnitAlgEquiv natDegree degreeOf | no | `pUnitAlgEquiv` docs (eval₂ lemmas), `degreeOf` docs; no natDegree link | confirms the API gap |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "degree" | yes | lines 365, 435: "V is of degree at most l r_p in x_p"; "individual degrees of U,V equal the corresponding degrees of F" | the source identifies deg of V with its x_p-degree implicitly |
| 6 | nLab | polynomial ring | no | universal property of polynomial algebras; no degree statement | too elementary |
| 7 | nCatLab | n/a | n/a | — | not a categorical concept (a degree equality under a concrete iso) |
| 8 | Stacks Project | n/a | n/a | — | basic commutative algebra; Stacks has no per-variable degree API |
| 9 | MathOverflow / Math.SE | (covered by #1/#2) | no | — | too elementary to be discussed |
| 10 | recent arXiv | covered by #1 (arXiv 2009.01586 per-variable degree bounds) | partial | inline use only | folklore |

### Literature summary (Phase 3)

Concept identified as: the degree of a polynomial is preserved by the canonical iso between the one-variable multivariate polynomial ring and `R[X]`.
Sources agree on the standard form: yes. It is folklore, immediate from the coefficient identification.
Most general standard form: any commutative semiring `R`, any singleton index type.
Generality dimensions where the literature varies:
  - direction: forward (`natDeg (φ p) = deg_{x_*} p`) or inverse. Both are the same fact, and mathlib's sibling lemmas use the forward direction.
  - coefficient ring: a commutative semiring is already the most general setting for `MvPolynomial`.
Disagreement with the literature: none.

### Generality analysis — `Roth.degreeOf_uniqueAlgEquiv_symm`

Literature-standard form (from Phase 3): `natDegree (uniqueAlgEquiv R σ p) = degreeOf default p` for `[CommSemiring R] [Unique σ]`, together with its inverse form.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | required by `MvPolynomial`, `degreeOf`, `uniqueAlgEquiv` |
| 2 | `[Unique σ]` | unique | unique | no | required by `uniqueAlgEquiv` itself (and by `default`) |
| 3 | direction | symm only | forward primary, symm corollary | n/a (same statement) | add the forward form; this one follows by `AlgEquiv.apply_symm_apply` (evidence (2)) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0
Proposed restatement (if STRICTLY NARROWER): n/a. Only a companion forward lemma is proposed, and it is compiled in evidence (1).
Cost of restatement: CHEAP — mechanical

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | no bundled hypotheses | — |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | no | already stated about the canonical iso | — |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field-specific to (semi)ring? | no | already `CommSemiring` | — |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general monoid? | no | `ℕ` degree intrinsic | — |
| 8 | Concrete-via-abstract? | no | the proof uses only `uniqueAlgEquiv` coefficient lemmas; there is no concrete witness to abstract | — |
| 9 | False-generalisation guard | no | forward and symm forms are the same fact | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the statement is already about mathlib's canonical equivalence at full generality. Adding the forward direction is a statement-shape matter (Phase 5.5), not a reformulation.

### Proof strategy — `Roth.degreeOf_uniqueAlgEquiv_symm`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes (it IS the missing helper) | prove forward `natDegree_uniqueAlgEquiv` by the same support argument; symm becomes `rw [← natDegree_uniqueAlgEquiv, AlgEquiv.apply_symm_apply]` | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
  - It is a two-sided support argument, the same shape as mathlib's `natDegree_finSuccEquiv` and `natDegree_optionEquivLeft` (which go through `degree_*` + `degreeOf_eq_sup`). For the mathlib PR the forward form should be primary, with the symm form derived from it (evidence (1),(2)).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.degreeOf_uniqueAlgEquiv_symm`

[A] Lean-Finder       "degree in the single variable of the multivariate polynomial corresponding to a univariate polynomial equals its natDegree"   hits: `degreeOf_eq_natDegree` (optionEquivLeft/subtype form), `natDegree_finSuccEquiv`, `degree_finSuccEquiv`; nothing for uniqueAlgEquiv
[B] Loogle            `MvPolynomial.degreeOf, MvPolynomial.uniqueAlgEquiv` and `Polynomial.natDegree, MvPolynomial.uniqueAlgEquiv`   hits: none (both empty)
[C] LeanSearch        "degreeOf of a univariate polynomial viewed as MvPolynomial over a unique index type equals natDegree"   hits: `degreeOf_eq_natDegree`, `natDegree_optionEquivLeft`, `degree_finSuccEquiv`, `degreeOf_eq_sup`; no uniqueAlgEquiv lemma
[D] Grep mathlib src  `uniqueAlgEquiv\|pUnitAlgEquiv` combined with `deg`; `degreeOf.*toMvPolynomial`, `natDegree.*toMvPolynomial`   no hits. The only uniqueAlgEquiv API (Mathlib/Algebra/MvPolynomial/Equiv.lean:60-240) is `uniqueAlgEquiv_monomial`, `uniqueAlgEquiv_symm_monomial`, `coeff_uniqueAlgEquiv`, `coeff_uniqueAlgEquiv_symm`, `eval₂_uniqueAlgEquiv_symm`, `eval₂_const_uniqueAlgEquiv_symm`
[E] Name pattern      clash test instead of name lookup: `MvPolynomial.natDegree_uniqueAlgEquiv` and `MvPolynomial.degreeOf_uniqueAlgEquiv_symm` were declared inside `namespace MvPolynomial` in the evidence file and elaborate with no clash, so both names are free (evidence (1),(2))

Searched for both:
  - the user's current form (symm, `degreeOf default (symm f) = natDegree f`): absent.
  - the literature-standard forward form (`natDegree (uniqueAlgEquiv R σ p) = degreeOf default p`): absent. The siblings `natDegree_finSuccEquiv` (Equiv.lean:815) and `natDegree_optionEquivLeft` (Equiv.lean:578) exist.

Concluded: not in mathlib (all 5 methods exhausted, in both directions). The building blocks exist, and the statement is a genuine API gap in the new `uniqueAlgEquiv` section.

### Normal-form check — `Roth.degreeOf_uniqueAlgEquiv_symm`

Equivalent formalisms: (a) `degreeOf default ((uniqueAlgEquiv R σ).symm f) = f.natDegree`; (b) `(uniqueAlgEquiv R σ p).natDegree = degreeOf default p`; (c) `totalDegree` versions, since for `Unique σ` `totalDegree = degreeOf default`.
Does mathlib already have a canonical form for this idea? Yes for the shape. The equivalence siblings state `(e p).natDegree = degreeOf _ p` (`natDegree_finSuccEquiv`, `natDegree_optionEquivLeft`), so (b) is canonical, with `degreeOf` on the RHS.
Is our statement stated against the canonical form? It is the inverse-side spelling. Ship (b) as the primary lemma and (a) as a corollary; both are useful as rewrite rules (the project rewrites with (a)).
RHS convention respected? yes for (b); (a) is its symm-side companion, like `coeff_uniqueAlgEquiv` / `coeff_uniqueAlgEquiv_symm`.

### Syntactic generality — `Roth.degreeOf_uniqueAlgEquiv_symm`

Alternative restatements attempted:
- (b) forward, explicit `p`: compiles (evidence (1)).
- (a) symm, explicit `f`, derived from (b) in one `rw`: compiles (evidence (2)).
- `degreeOf i` for arbitrary `i : σ` instead of `default`: equivalent via `Subsingleton.elim` (the Theta.lean:427 site does exactly this rewrite first). Kept `default` to match `coeff_uniqueAlgEquiv` (`Finsupp.single default n`).

Chosen restatement: the pair (b) + (a).
Justification: (b) matches the sibling API, and (a) matches the `coeff_uniqueAlgEquiv` / `coeff_uniqueAlgEquiv_symm` pairing and is what call sites rewrite with.

### Superfluous-argument audit — `Roth.degreeOf_uniqueAlgEquiv_symm`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial` |
| 2 | `[Unique σ]` | yes | required by `uniqueAlgEquiv` |
| 3 | `f` | yes | appears in the conclusion |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (add the forward `natDegree_uniqueAlgEquiv` as primary; keep this as its symm corollary)
Syntactic generality: OK
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP (adds a companion; the symm statement itself is unchanged)

### Call sites — `Roth.degreeOf_uniqueAlgEquiv_symm`

Internal use count: 1 outside the declaring file (plus 1 inside it)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:226 (declaring file, `degreeOf_none_rename_mul_aeval`) | `(fun _ _ _ ↦ rfl) ()).trans (degreeOf_uniqueAlgEquiv_symm V)` |
| Roth/Theta.lean:427 (`index_separated_mul_le_aux`) | `rw [Subsingleton.elim j default, hV', degreeOf_uniqueAlgEquiv_symm]` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using it?):
  - (none). `grep -rn natDegree Roth/` shows no other place that relates `degreeOf` of a `uniqueAlgEquiv.symm` image to `natDegree`.

### Composition check (Phase 6)

Can `Roth.degreeOf_uniqueAlgEquiv_symm` be derived from mathlib in ≤3 chained calls?

Attempt 1: via `degreeOf_eq_natDegree default p`. That gives `natDegree (optionEquivLeft R {b // b ≠ default} (rename (Equiv.optionSubtypeNe default).symm p))`, which would then have to be identified with `uniqueAlgEquiv R σ p`. That identification is itself a missing lemma (an equivalence-compatibility statement over an empty subtype with `C`-coefficients in `MvPolynomial (empty) R ≅ R`).
  - Result: fails (needs ≥2 missing lemmas).

Attempt 2: via `natDegree_finSuccEquiv` with `n = 0`. It needs `Fin 1` variables and a comparison between `finSuccEquiv R 0` (coefficients in `MvPolynomial (Fin 0) R`) and `uniqueAlgEquiv`.
  - Result: fails (no bridge lemma in mathlib).

Attempt 3: direct support argument (the current proof).
  - Result: works, but it is a 10-line two-sided proof, not a composition.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.degreeOf_uniqueAlgEquiv_symm`

Verdict: YES-add-as-is (together with the forward companion `natDegree_uniqueAlgEquiv`)

**Category:** YES-add-as-is

**Evidence:**
- Literature search (Phase 3): folklore; holds over any commutative semiring and singleton index.
- Generality analysis (Phase 4): MAXIMALLY GENERAL.
- Mathlib search (Phase 5): not in mathlib in either direction. Siblings `natDegree_finSuccEquiv` and `natDegree_optionEquivLeft` exist. Names are free.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**
`MvPolynomial.uniqueAlgEquiv` was introduced on 2026-04-15, replacing `pUnitAlgEquiv`. It ships with coefficient and monomial lemmas (`coeff_uniqueAlgEquiv`, `coeff_uniqueAlgEquiv_symm`, `uniqueAlgEquiv_monomial`) and `eval₂` lemmas, but no degree lemma. The two sibling equivalences in the same file do have one: `natDegree_finSuccEquiv` (Equiv.lean:815) and `natDegree_optionEquivLeft` (Equiv.lean:578), each stating `natDegree (e p) = degreeOf _ p`. The missing `uniqueAlgEquiv` row is a concrete gap. This project needed to fill it to identify "V has degree ≤ l r_p" with the `RSet` per-variable degree condition (Theta.lean:427). That is exactly the bookkeeping any user of `uniqueAlgEquiv` must do when moving between `R[X]` and one-variable `MvPolynomial`.

The project statement is already maximally general (`CommSemiring`, any `Unique σ`). The mathlib PR should make the forward form primary. Evidence (1) proves it in 8 lines with mathlib-only imports, and the symm form then follows in one `rw` (evidence (2)), mirroring the `coeff_uniqueAlgEquiv` / `coeff_uniqueAlgEquiv_symm` pair.

WHY add it:
- New content: degree compatibility of the canonical iso `MvPolynomial σ R ≃ₐ R[X]` for `Unique σ`, in both directions.
- Specific gap: it is the `uniqueAlgEquiv` row missing from the `natDegree_finSuccEquiv` / `natDegree_optionEquivLeft` family, and the degree counterpart of the existing `coeff_uniqueAlgEquiv(_symm)` pair.
- Composition: the degree hypotheses already in mathlib (`degreeOf_le_iff`, `degreeOf_mul_eq`, `degreeOf_rename_of_injective`) can then be transported to and from `Polynomial.natDegree` lemmas. Separation.lean:226 shows the pattern: `degreeOf_rename_of_injective ... |>.trans degreeOf_uniqueAlgEquiv_symm`.

Proposed mathlib location:    Mathlib/Algebra/MvPolynomial/Equiv.lean, section `Equiv`, after `coeff_uniqueAlgEquiv_symm`. Equiv.lean may not import Mathlib/Algebra/Polynomial/Degree/Lemmas.lean (home of `natDegree_le_iff_coeff_eq_zero`); if not, rewrite the `≤` half via `Polynomial.natDegree_le_iff_degree_le`/`degree_le_iff_coeff_zero` or follow `natDegree_finSuccEquiv`'s `degree` + `degreeOf_eq_sup` route. Verify at PR time.
Proposed PR title:            "feat(Algebra/MvPolynomial/Equiv): add `natDegree_uniqueAlgEquiv` and `degreeOf_uniqueAlgEquiv_symm`"
PR grouping (if applicable):  one PR for the pair. Not related to other YES verdicts in this file (`degreeOf_coeffNone_le` targets the `optionEquivLeft` section; it could share a PR titled "degree API for MvPolynomial equivalences" if a reviewer prefers).
Proposed statement:
```lean
theorem natDegree_uniqueAlgEquiv [Unique σ] (p : MvPolynomial σ R) :
    (uniqueAlgEquiv R σ p).natDegree = degreeOf default p := by
  apply le_antisymm
  · refine Polynomial.natDegree_le_iff_coeff_eq_zero.2 fun n hn ↦ ?_
    rw [coeff_uniqueAlgEquiv, ← notMem_support_iff]
    exact notMem_support_of_degreeOf_lt (i := default) (by simpa using hn)
  · rw [degreeOf_le_iff]
    intro e he
    rw [Finsupp.unique_single e, mem_support_iff, ← coeff_uniqueAlgEquiv] at he
    exact Polynomial.le_natDegree_of_ne_zero he

theorem degreeOf_uniqueAlgEquiv_symm [Unique σ] (f : Polynomial R) :
    degreeOf default ((uniqueAlgEquiv R σ).symm f) = f.natDegree := by
  rw [← natDegree_uniqueAlgEquiv, AlgEquiv.apply_symm_apply]
```
Pre-PR checklist before opening:
  - [ ] `/generalise` — none expected (already CommSemiring, any Unique σ)
  - [ ] `/cleanup` the snippet against mathlib style; settle the import question above
  - [ ] Pick a reviewer from recent commits to Mathlib/Algebra/MvPolynomial/Equiv.lean (the 2026-04-15 uniqueAlgEquiv refactor author is natural)
Next action: open the mathlib PR with the pair above. In the project, keep `Roth.degreeOf_uniqueAlgEquiv_symm` until it lands, then delete it and point Separation.lean:226 and Theta.lean:427 at `MvPolynomial.degreeOf_uniqueAlgEquiv_symm` (same argument order; at Theta.lean the bare name would then resolve via `open MvPolynomial`).

---

## Next step

Upstream `MvPolynomial.natDegree_uniqueAlgEquiv` + `MvPolynomial.degreeOf_uniqueAlgEquiv_symm` to Mathlib/Algebra/MvPolynomial/Equiv.lean after `coeff_uniqueAlgEquiv_symm`; keep the project lemma for its 2 call sites until then.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.degreeOf_uniqueAlgEquiv_symm/reaim.lean` imports only `Mathlib.Algebra.MvPolynomial.Equiv` and `Mathlib.Algebra.Polynomial.Degree.Lemmas`. `lean_diagnostic_messages` returned no diagnostics after two fixes to my first draft: a missing import for `natDegree_le_iff_coeff_eq_zero`, and a needed `(i := default)`. Its three checks:
  - (1) `MvPolynomial.natDegree_uniqueAlgEquiv` declared inside `namespace MvPolynomial` with no clash, proved over `[CommSemiring R]`.
  - (2) `MvPolynomial.degreeOf_uniqueAlgEquiv_symm` derived from (1) in one `rw`, also with no clash.
  - (3) The project's proof, verbatim, compiles with mathlib-only imports.
- Searches: 3 WebSearch queries; Loogle (2 queries, both empty), LeanSearch and Lean-Finder; a mathlib grep for uniqueAlgEquiv/pUnitAlgEquiv combined with deg and for toMvPolynomial degree lemmas (no hits). All are recorded above. ChatGPT MCP was n/a (not configured in this session).
- Project-wide grep of `Roth/` for `degreeOf_uniqueAlgEquiv_symm`: the declaration (Separation.lean:174) and call sites Separation.lean:226 and Theta.lean:427.
