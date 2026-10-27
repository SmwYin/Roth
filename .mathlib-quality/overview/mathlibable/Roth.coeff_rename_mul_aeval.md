---
decl: Roth.coeff_rename_mul_aeval
file: Roth/Separation.lean
line: 123
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The disjoint-variables coefficient identity [x_τ^a x_*^b](U(x_τ)V(x_*)) = U_a V_b is absent from mathlib (no optionEquivLeft/rename-some compatibility lemma, no Sum analogue); it should ship in mathlib's canonical a.optionElim b spelling with the missing optionEquivLeft_rename_some API, plus the literature-standard Sum form, all verified to compile.
action: Upstream to Mathlib/Algebra/MvPolynomial/Equiv.lean optionEquivLeft_comp_rename_some, optionEquivLeft_rename_some, optionEquivLeft_aeval_X_none and the coefficient lemma stated at a.optionElim b (optionally the Sum.inl/Sum.inr form); locally restate and update call sites Theta.lean:480,486 and Separation.lean:476.
---

# Roth.coeff_rename_mul_aeval

## Inventory entry

### `theorem Roth.coeff_rename_mul_aeval`
- **Type**: `{τ : Type*} {R : Type*} [CommSemiring R] (U : MvPolynomial τ R) (V : Polynomial R) (a : τ →₀ ℕ) (b : ℕ) : (rename some U * Polynomial.aeval (X none) V).coeff (a.mapDomain some + Finsupp.single none b) = U.coeff a * V.coeff b` (section `[Fintype τ] [DecidableEq τ]` omitted; confirmed by `#check`, evidence (0))
- **What**: In `R[x_τ, x_*]`, the coefficient of `x_τ^a x_*^b` in the separated product `U(x_τ) V(x_*)` is `U_a · V_b`.
- **How**: Transports to `R[x_τ][X]` via `optionEquivLeft`: `rw [← coeff_coeffNone, coeffNone, map_mul]`, identifies `optionEquivLeft (rename some U) = Polynomial.C U` through the local `AlgHom` equation `h` (proved by `ext i; simp`), then `Polynomial.aeval_algHom_apply`, `optionEquivLeft_X_none`, `Polynomial.aeval_X_left_eq_map`, `Polynomial.coeff_C_mul`, `Polynomial.coeff_map`, `algebraMap_eq`, `coeff_C_mul`, `mul_comm`.
- **Hypotheses**: `[CommSemiring R]` only.
- **Uses from project**: `Roth.coeff_coeffNone`, `Roth.coeffNone`
- **Used by**: `Roth.index_det_le` in Roth/Theta.lean:480 and :486 (`rw [hF, coeff_rename_mul_aeval, Int.cast_mul, abs_mul] at h1`, bounding coefficients of `U` and `V`); private `exists_int_polynomial_of_primitive_factor_aux` in Roth/Separation.lean:476 (`simp only [coeff_rename_mul_aeval, coeff_map] at h`).
- **Visibility**: public
- **Lines**: 117–133, proof length 7 lines
- **Notes**: The `AlgHom` equation `h : (optionEquivLeft R τ).toAlgHom.comp (rename some) = Polynomial.CAlgHom` is re-proved identically in the private `coeff_X_none_pow_mul_rename` (Separation.lean:67); it is the Option analogue of mathlib's `sumAlgEquiv_comp_rename_inr`, which mathlib lacks.

## Junk check (Step 8)
- Used anywhere? Yes: 3 call sites in 2 files (Theta.lean:480, :486; Separation.lean:476).
- Wrapper of 1–2 mathlib calls? No: ~10 rewrites through `optionEquivLeft`, plus a locally proved `AlgHom` equation not in mathlib.
- Does mathlib have it? No (Phase 5 below: Lean-Finder, LeanSearch, grep found only building blocks).
- Too specific? No: it is the basic coefficient identity for a product of polynomials in disjoint variables, applied at three sites.
- Well-chosen? Mostly; the multi-index spelling `a.mapDomain some + single none b` is non-canonical (mathlib uses `a.optionElim b`, cf. `optionEquivLeft_coeff_coeff`).
- Conclusion: `KEEP` (restate in the `optionElim` spelling when upstreaming; see verdict).

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 = KEEP; qualified name absent from mathlib. Not a glue lemma (7-line rewrite proof), so no inheritance from `Roth.coeffNone`; full workflow below.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` elaborates with no errors)
- decl `Roth.coeff_rename_mul_aeval`: resolved at Roth/Separation.lean:123
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`) in polynomials over `Option τ`, towards Lemma 2 of the source (`F = U(x_τ) V(x_none)`).

### Statement (Phase 1)

`Roth.coeff_rename_mul_aeval` is a theorem stating the following: let `U ∈ R[x_τ]` be a polynomial in the variables `τ` and `V ∈ R[y]` a one-variable polynomial. View both inside `R[x_τ, x_*]` (variables `τ ⊔ {*}`), `U` via the inclusion of variables and `V` by substituting `y ↦ x_*`. Then the coefficient of `x_τ^a x_*^b` in `U(x_τ)V(x_*)` equals `U_a V_b`.

Variables / typeclasses involved (Lean side):
- `τ : Type*` — the non-distinguished variables.
- `R : Type*`, `[CommSemiring R]` — coefficients.
- `U : MvPolynomial τ R`, `V : Polynomial R`.
- `a : τ →₀ ℕ`, `b : ℕ` — the two halves of the multi-index.

Hypotheses (Lean side):
- none.

Conclusion (math): `[x_τ^a x_*^b] (U(x_τ) V(x_*)) = [x^a]U · [y^b]V`.

Conclusion (Lean): `(rename some U * Polynomial.aeval (X none) V).coeff (a.mapDomain some + Finsupp.single none b) = U.coeff a * V.coeff b`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a coefficient identity used as a helper; no new structure, not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 7
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | coefficient of product of polynomials in disjoint variables f(x)g(y) coefficient x^a y^b equals product of coefficients | partial | `f(x)g(y) = ∑ a_i b_j x^i y^j`, so `[x^a y^b] = a_a b_b` | no source states it as a named result; ProofWiki "Coefficients of Product of Two Polynomials" covers only one variable; Reznick (PAMS 1993) treats disjoint-variable products for norms |
| 2 | WebSearch (general form) | polynomial ring tensor product R[x] ⊗ R[y] ≅ R[x,y] monomial basis x^a y^b | yes | `R[X] ⊗_R R[Y] ≅ R[X ⊔ Y]`, `x^a ⊗ y^b ↦ x^a y^b` | Berkeley tensor-product notes, OSU solutions, Hawaii Math 612 assignment; the identity is the multiplicativity of this basis correspondence |
| 3 | WebSearch (aliases / mathlib) | Mathlib MvPolynomial coeff product rename disjoint variables lemma | no | — | only `coeff_rename_mapDomain`, `coeff_rename_embDomain`, `vars_add_of_disjoint` surfaced; no product lemma |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "disjoint" | yes | line 424: the integer claim follows because "the variables of the two factors are disjoint"; line 435 uses it again | the source uses exactly this coefficient identity, implicitly |
| 6 | nLab | polynomial ring / free commutative algebra (checked via parent assessment `Roth.coeffNone`) | yes | `A[X ⊔ Y] ≅ A[X] ⊗_A A[Y]` (free functor preserves coproducts) | only the isomorphism; coefficient bookkeeping not discussed |
| 7 | nCatLab | free commutative algebra / coproduct of commutative rings | yes | coproduct of comm. rings is the tensor product | same content as #6 |
| 8 | Stacks Project | n/a | n/a | — | elementary commutative algebra identity; Stacks states `R[x_i] ⊗ R[y_j] = R[x_i, y_j]` only implicitly, no coefficient statement to compare |
| 9 | MathOverflow / Math.SE | (covered by #1/#2; physicsforums "Is R[x,y] isomorphic to R[y,x]?" surfaced) | no | — | too elementary to be discussed as a result |
| 10 | recent arXiv | arXiv 2508.13165 (intro to rings and fields), arXiv 2312.13990 surfaced by #1/#2 | yes | `R[x,y]` vs `(R[x])[y]` identification | confirms standard treatment, no new form |

### Literature summary (Phase 3)

Concept identified as: coefficients of a product of polynomials in disjoint sets of variables; equivalently, multiplicativity of the monomial-basis identification `R[X] ⊗ R[Y] ≅ R[X ⊔ Y]`.
Sources agree on the standard form: yes — `[x^a y^b](f(x)g(y)) = f_a g_b`, treated as immediate.
Most general standard form: for any variable sets `X`, `Y` and commutative semiring `R`, `f ∈ R[X]`, `g ∈ R[Y]`: the coefficient of `x^a y^b` in `f g ∈ R[X ⊔ Y]` is `f_a g_b`.
Generality dimensions where the literature varies:
  - second block: one variable (the project, via `Option`/`Polynomial`) up to an arbitrary set (`Sum`); the most general is arbitrary `Y`.
  - coefficient ring: commutative semiring is already most general.
Disagreement with the literature: none mathematically; the project specialises the second block to one variable and spells the index `a.mapDomain some + single none b` rather than mathlib's `a.optionElim b`.

### Generality analysis — `Roth.coeff_rename_mul_aeval`

Literature-standard form (from Phase 3): `(rename Sum.inl p * rename Sum.inr q).coeff (Finsupp.sumElim a b) = p.coeff a * q.coeff b`; mathlib-idiomatic Option specialisation: `(rename some U * aeval (X none) V).coeff (a.optionElim b) = U.coeff a * V.coeff b`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | `MvPolynomial`, `rename`, `optionEquivLeft` require it |
| 2 | second block `{none}` with `V : Polynomial R` | one variable | arbitrary variable set `τ` (`Sum` form) | yes (restatement) | verified: `coeff_rename_inl_mul_rename_inr` compiles (evidence (3)) |
| 3 | multi-index `a.mapDomain some + single none b` | non-canonical | `a.optionElim b` (mathlib) | yes (restatement) | verified: `coeff_rename_some_mul_aeval_X_none` compiles (evidence (2)) |
| 4 | `τ : Type*` | arbitrary | arbitrary | no | section `Fintype`/`DecidableEq` already omitted |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (one-variable second block; non-canonical index)
Number of weakening opportunities found: 2 (both restatements, both verified clean with `lean_diagnostic_messages`, evidence (2)–(3))
Proposed restatement (if STRICTLY NARROWER):

```lean
theorem MvPolynomial.coeff_rename_some_mul_aeval_X_none (U : MvPolynomial τ R) (V : Polynomial R)
    (a : τ →₀ ℕ) (b : ℕ) :
    (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V).coeff
      (a.optionElim b) = U.coeff a * V.coeff b

theorem MvPolynomial.coeff_rename_inl_mul_rename_inr (p : MvPolynomial σ R)
    (q : MvPolynomial τ R) (a : σ →₀ ℕ) (b : τ →₀ ℕ) :
    (rename Sum.inl p * rename Sum.inr q).coeff (Finsupp.sumElim a b) = p.coeff a * q.coeff b
```

Cost of restatement: CHEAP — both proved in the evidence file (Option form: 1 `rw` chain using three new 1–3 line API lemmas; Sum form: ~15 lines via `coeff_mul`, `Finset.sum_eq_single`, `coeff_rename_ne_zero`, `coeff_rename_mapDomain`).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | no hypotheses | — |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | yes (partially) | factor through the structural lemmas `optionEquivLeft_comp_rename_some : (optionEquivLeft R τ).toAlgHom.comp (rename some) = Polynomial.CAlgHom` and `optionEquivLeft_aeval_X_none`, mirroring mathlib's `sumAlgEquiv_comp_rename_inr` | coefficient lemma becomes a short `rw` chain; also serves `coeff_X_none_pow_mul_rename` (Separation.lean:64) and any `optionEquivLeft (rename some _)` computation |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field-specific to (semi)ring? | no | already `CommSemiring` | — |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general monoid? | yes | second block `Unit`/`Option` to arbitrary `τ` (`Sum` form) | general disjoint-variables API; Option form follows via renaming |
| 8 | Concrete-via-abstract? | no | after `rw [← coeff_coeffNone, coeffNone]` the proof still uses `optionEquivLeft` and `X none` specifically; no abstract witness hidden | — |
| 9 | False-generalisation guard | no | Option form is the same statement in the canonical spelling; Sum form strictly contains it (Option τ ≃ τ ⊕ Unit) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the `a.optionElim b` statement above, proved from the new API lemmas `optionEquivLeft_comp_rename_some`, `optionEquivLeft_rename_some`, `optionEquivLeft_aeval_X_none`.
  - Cost: CHEAP
  - Mathlib downstream this enables: composes with `optionEquivLeft_coeff_coeff` and `mem_support_coeff_optionEquivLeft` (which already use `optionElim`); fills the Option analogue of `sumAlgEquiv_comp_rename_inl/inr`.
  - Real mathematical improvement: the index matches mathlib's existing normal form, so no Finsupp conversion lemma (`eq_mapDomain_some_add_single`) is needed by consumers.

### Proof strategy — `Roth.coeff_rename_mul_aeval`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | already transports through `optionEquivLeft` | — |
| 5 | missing mathlib helpers | yes | `optionEquivLeft_comp_rename_some`, `optionEquivLeft_rename_some`, `optionEquivLeft_aeval_X_none` (evidence (1)); the local `have h` is exactly the first | CHEAP (file with the PR) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: extract the local `AlgHom` equation and the `aeval (X none)` computation as API lemmas; restate at `a.optionElim b` so the proof starts with `← optionEquivLeft_coeff_coeff` rather than going through `coeff_coeffNone`.
  - Cost: CHEAP
  - Missing mathlib API (if any): the three lemmas in evidence (1)
  - Would refactoring make the proof strictly shorter / cleaner? yes

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.coeff_rename_mul_aeval`

[A] Lean-Finder       "coefficient of product of two multivariate polynomials in disjoint sets of variables is product of coefficients"; "optionEquivLeft of rename some p equals Polynomial.C p"   no hit for the statement: returned `MvPolynomial.coeff_mul`, `MonomialOrder.coeff_mul_of_add_of_degree_le`, `coeff_monomial_mul`, `coeff_mul_monomial`; second query returned `optionEquivLeft_X_some`, `optionEquivLeft_C`, `optionEquivLeft_apply` (no rename lemma)
[B] Loogle            `MvPolynomial.coeff, MvPolynomial.rename, HMul.hMul`   n/a: query error (loogle's parser did not resolve `MvPolynomial.coeff`); covered by [A], [C], [D]
[C] LeanSearch        "coeff of rename some p times polynomial in X none equals product of coefficients"   no hit: `coeff_rename_embDomain`, `coeff_rename_mapDomain`, `constantCoeff_rename`, `Polynomial.coeff_mul_X_pow` (building blocks only)
[D] Grep mathlib src  `optionEquivLeft.*rename`, `rename some`, `rename_mul_rename`, `coeff_mul_of_disjoint`, `sumElim`/`optionElim` in Algebra/MvPolynomial and RingTheory/MvPolynomial, `sumAlgEquiv` lemmas   no product-coefficient lemma; `sumAlgEquiv_comp_rename_inl/inr` exist (Equiv.lean:424/429) but no Option analogue; `rename some` occurs only inside the definition of `optionEquivLeft` (Equiv.lean:469)
[E] Name pattern      `coeff_rename`, `optionEquivLeft_`   via grep (all `optionEquivLeft_*` lemmas listed, Equiv.lean:473–612): none about `rename some` or `aeval (X none)`

Searched for both:
  - the user's current form (Option / `Polynomial.aeval (X none)`): not in mathlib.
  - the literature-standard form (`rename Sum.inl p * rename Sum.inr q`): not in mathlib.

Concluded: found building blocks (`optionEquivLeft_coeff_coeff`, `optionEquivLeft_X_none`, `Polynomial.aeval_algHom_apply`, `Polynomial.aeval_X_left_eq_map`, `coeff_rename_mapDomain`, `coeff_rename_ne_zero`, `coeff_mul`); no statement in either form.

### Normal-form check — `Roth.coeff_rename_mul_aeval`

Equivalent formalisms: index as (a) `a.mapDomain some + single none b` (project); (b) `a.optionElim b` (mathlib); (c) `a.embDomain .some + single none b`.
Does mathlib already have a canonical form? yes — (b), in `optionEquivLeft_coeff_coeff` and `mem_support_coeff_optionEquivLeft`.
Is our statement stated against the canonical form? NO → REFACTOR to (b).
RHS convention respected? yes (RHS `U.coeff a * V.coeff b` is the simp-normal product).

### Syntactic generality — `Roth.coeff_rename_mul_aeval`

Alternative restatements attempted:
- `optionElim` index (evidence (2)): compiles.
- structural form `optionEquivLeft R τ (rename some U * aeval (X none) V) = Polynomial.C U * V.map (algebraMap R _)`: immediate from evidence (1) by `map_mul`.
- Sum form (evidence (3)): compiles.

Chosen restatement: `optionElim` index for the Option lemma, plus the structural API lemmas.
Justification: all three call sites quantify over the index (Theta.lean `hFcoef` is `∀ d`, Separation.lean:476 builds the index itself), so they can supply `a.optionElim b` equally easily, and the result then rewrites directly against `optionEquivLeft_coeff_coeff`.

### Superfluous-argument audit — `Roth.coeff_rename_mul_aeval`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | needed by `MvPolynomial` |
| 2 | section `[Fintype τ] [DecidableEq τ]` | no | already omitted via `omit ... in` (evidence (0) shows no such binders) |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (index `a.optionElim b`)
Syntactic generality: RESTATE (add structural lemmas `optionEquivLeft_rename_some`, `optionEquivLeft_aeval_X_none`)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.coeff_rename_mul_aeval`

Internal use count: 2 (outside the declaring file); 1 inside Roth/Separation.lean.
External-to-file callers: 1 distinct file (Roth/Theta.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:480 | `rw [hF, coeff_rename_mul_aeval, Int.cast_mul, abs_mul] at h1` (bound on `U.coeff a`, index `a.mapDomain some + single none V.natDegree`) |
| Roth/Theta.lean:486 | `rw [hF, coeff_rename_mul_aeval, Int.cast_mul, abs_mul] at h1` (bound on `V.coeff b`, index `a₀.mapDomain some + single none b`) |
| Roth/Separation.lean:476 | `simp only [coeff_rename_mul_aeval, coeff_map] at h` in private `exists_int_polynomial_of_primitive_factor_aux` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `coeff_rename_mul_aeval`?):
  - Roth/Separation.lean:64–75 private `coeff_X_none_pow_mul_rename` re-proves the same `AlgHom` equation `h` (special case `V = X^ν`); it would use `optionEquivLeft_rename_some` after the refactor.

### Composition check (Phase 6)

Can `Roth.coeff_rename_mul_aeval` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [← optionEquivLeft_coeff_coeff, map_mul]` then compute `optionEquivLeft (rename some U)` and `optionEquivLeft (aeval (X none) V)`
  - Mathlib decls used: `optionEquivLeft_coeff_coeff`, `optionEquivLeft_X_none`, `Polynomial.aeval_algHom_apply`, `Polynomial.aeval_X_left_eq_map`, `Polynomial.coeff_C_mul`, `Polynomial.coeff_map`, `coeff_C_mul`
  - Result: partial — needs the `AlgHom` equation `optionEquivLeft ∘ rename some = Polynomial.C`, which mathlib lacks, plus ~8 further rewrites.
  - Notes: even with that lemma available the chain is ~8 rewrites (evidence (2)), not a ≤3-call composition.

Attempt 2: via `coeff_mul` and `Finset.sum_eq_single`
  - Mathlib decls used: `coeff_mul`, `coeff_rename_ne_zero`, `coeff_rename_mapDomain`
  - Result: a genuine multi-step proof (as in evidence (3)), not a composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.coeff_rename_mul_aeval`

Verdict: YES-but-generalise-first

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard identity, coefficients of a product in disjoint variables, i.e. multiplicativity of `R[X] ⊗ R[Y] ≅ R[X ⊔ Y]`; the source paper uses it at clean.tex:424, 435.
- Generality analysis (Phase 4): STRICTLY NARROWER. Index spelling and the one-variable second block, both restatements verified to compile (evidence (2), (3)).
- Mathlib search (Phase 5): not in mathlib in either form. Only building blocks found; no Option analogue of `sumAlgEquiv_comp_rename_inr`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**
Mathlib has the coefficient API for `optionEquivLeft` (`optionEquivLeft_coeff_coeff`) and for `rename` (`coeff_rename_mapDomain`). It has nothing that computes coefficients of a product of polynomials in disjoint variables. It also has no lemma saying `optionEquivLeft` sends `rename some p` to `Polynomial.C p`, although the `Sum` analogues `sumAlgEquiv_comp_rename_inl/inr` exist (Equiv.lean:424–432). The project proves that equation inline twice (Separation.lean:67 and :126). It then uses the coefficient identity at three sites to read off the coefficients of `U` and `V` from a separated product `F = U(x_τ)V(x_none)`. This is a recurring manual reformulation, which is the gap.

The project form should not ship as-is. Its index `a.mapDomain some + single none b` is not mathlib's normal form `a.optionElim b`. With the `optionElim` index, the statement rewrites directly against `optionEquivLeft_coeff_coeff`, and consumers no longer need the Finsupp conversion lemma (cf. the `Roth.coeff_coeffNone` report). The literature-standard statement is the `Sum` form with an arbitrary second block. Evidence (3) proves it in ~15 lines. The Option form is the one-variable case most useful with `optionEquivLeft` and `finSuccEquiv`.

Reason for the generalisation: both apply.
- LITERATURE-WEAKENING: the second block generalises from one variable to an arbitrary `τ` (`Sum` form).
- MODERN-IDIOM: the index moves to the `optionElim` normal form, and the proof factors through the structural `optionEquivLeft_comp_rename_some` API.

Proposed restatement:
```lean
theorem MvPolynomial.optionEquivLeft_comp_rename_some :
    (optionEquivLeft R τ).toAlgHom.comp (rename some) = Polynomial.CAlgHom
theorem MvPolynomial.optionEquivLeft_rename_some (p : MvPolynomial τ R) :
    optionEquivLeft R τ (rename some p) = Polynomial.C p
theorem MvPolynomial.optionEquivLeft_aeval_X_none (V : Polynomial R) :
    optionEquivLeft R τ (Polynomial.aeval (X none) V) = V.map (algebraMap R (MvPolynomial τ R))
theorem MvPolynomial.coeff_rename_some_mul_aeval_X_none (U : MvPolynomial τ R) (V : Polynomial R)
    (a : τ →₀ ℕ) (b : ℕ) :
    (rename some U * Polynomial.aeval (X none) V).coeff (a.optionElim b) = U.coeff a * V.coeff b
theorem MvPolynomial.coeff_rename_inl_mul_rename_inr (p : MvPolynomial σ R) (q : MvPolynomial τ R)
    (a : σ →₀ ℕ) (b : τ →₀ ℕ) :
    (rename Sum.inl p * rename Sum.inr q).coeff (Finsupp.sumElim a b) = p.coeff a * q.coeff b
```
All five already compile in evidence/Roth.coeff_rename_mul_aeval/restate.lean.
Estimated cost of regeneralisation: CHEAP
Mathlib downstream this enables:
- composes with `optionEquivLeft_coeff_coeff` and `mem_support_coeff_optionEquivLeft`, which already use `optionElim`
- completes the Option counterpart of `sumAlgEquiv_comp_rename_inl/inr`
- gives a coefficient formula for `rename f p * rename g q` with disjoint variables, which is currently only available through `coeff_mul` with a hand-made `sum_eq_single`

Proposed mathlib location: `Mathlib/Algebra/MvPolynomial/Equiv.lean` (Option lemmas next to `optionEquivLeft_coeff_coeff`; Sum lemma next to `sumAlgEquiv_comp_rename_inl`).
Proposed PR title: "feat(Algebra/MvPolynomial/Equiv): coefficients of products in disjoint variables"
PR grouping: ship together with the `optionEquivLeft_rename_some` API, which the private `Roth.coeff_X_none_pow_mul_rename` also needs.
Local refactor: restate the project lemma with `a.optionElim b` and prove it from the API lemmas. Then change the index at Theta.lean:479/485 (`hFcoef (a.optionElim V.natDegree)`, `hFcoef (a₀.optionElim b)`) and at Separation.lean:474–476. `hFcoef` is `∀ d`, so the change is mechanical.
Next action: run `/generalise Roth.coeff_rename_mul_aeval` with the `optionElim`/`Sum` targets above, then `/cleanup` and open the PR.

---

## Next step

Restate with `a.optionElim b`, add `optionEquivLeft_comp_rename_some`, `optionEquivLeft_rename_some` and `optionEquivLeft_aeval_X_none`, update the 3 call sites (Theta.lean:480, 486; Separation.lean:476), then upstream the Option and Sum coefficient lemmas to `Mathlib/Algebra/MvPolynomial/Equiv.lean`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.coeff_rename_mul_aeval/restate.lean` imports `Roth.Separation`. It was checked with `lean_diagnostic_messages` after one round of fixes, and the final version has no errors; the only messages are the `#check` info and a header-linter style warning. (0) `#check @Roth.coeff_rename_mul_aeval` shows `[CommSemiring R]` only. (1) `optionEquivLeft_comp_rename_some`, `optionEquivLeft_rename_some` and `optionEquivLeft_aeval_X_none` compile. (2) The `optionElim` restatement `coeff_rename_some_mul_aeval_X_none` compiles as a single `rw` chain. (3) The Sum form `coeff_rename_inl_mul_rename_inr` compiles via `coeff_mul`, `Finset.sum_eq_single`, `coeff_rename_ne_zero` and `coeff_rename_mapDomain`.
- Searches: 3 WebSearch queries, recorded above. Lean-Finder ×2 and LeanSearch ×1 found building blocks only. The Loogle query hit a parse error. Mathlib greps for `optionEquivLeft.*rename`, `rename some`, `sumElim`/`optionElim`, `rename_mul_rename`, `coeff_mul_of_disjoint` and the `sumAlgEquiv` lemmas found no product lemma and no Option `rename` lemma. ChatGPT MCP was n/a (not configured in this session).
