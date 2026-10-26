---
decl: MvPolynomial.taylor_neg_taylor
file: Roth/Taylor.lean
line: 182
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Translation by -α inverts translation by α is core API of the YES-add-as-is MvPolynomial.taylor, but mathlib's univariate precedent ships it only as the two inverse fields of the AlgEquiv Polynomial.taylorEquiv (with taylorEquiv_symm), so the mathlib form is the bundled MvPolynomial.taylorEquiv plus both one-sided inverses with Pi negation, all compiled in evidence.
action: In the MvPolynomial.taylor upstream PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) state taylor_neg_taylor as taylor (-α) (taylor α P) = P, add taylor_taylor_neg and taylorEquiv with coe_taylorEquiv and taylorEquiv_symm (evidence items 3-5); locally keep (call sites Roth/Taylor.lean:188 taylor_injective, Roth/Taylor.lean:208 eq_sum_box_hasseDeriv).
---

# MvPolynomial.taylor_neg_taylor

## Inventory entry

### `theorem MvPolynomial.taylor_neg_taylor`
- **Type**: `∀ {σ A : Type*} [CommRing A] (α : σ → A) (P : MvPolynomial σ A), (taylor fun j ↦ -α j) ((taylor α) P) = P`
- **What**: Translating by `α` and then by `-α` gives back the polynomial: `P(X + α)(X - α) = P(X)`. So translation by `-α` is a left inverse of translation by `α`.
- **How**: one `simp [taylor_taylor]`: the project lemma `taylor_taylor` merges the two translations into translation by `fun j ↦ -α j + α j`, simp turns that into `fun _ ↦ 0` with `neg_add_cancel`, and the simp lemma `taylor_zero` finishes.
- **Hypotheses**: `[CommRing A]` (section variable; negation is needed); no propositional hypotheses.
- **Uses from project**: `MvPolynomial.taylor`, `MvPolynomial.taylor_taylor`, `MvPolynomial.taylor_zero` (simp lemma, used implicitly)
- **Used by**: Roth/Taylor.lean:188 (`taylor_injective`, via `Function.LeftInverse.injective`), Roth/Taylor.lean:208 (`eq_sum_box_hasseDeriv`, first `calc` step). Indirect: `taylor_eq_zero_iff` (through `taylor_injective`, Roth/Taylor.lean), `eval_eq_sum_box` (Roth/Taylor.lean) and so Roth/Main.lean:390. No direct uses outside Roth/Taylor.lean (`grep -rn taylor_neg_taylor Roth/`).
- **Visibility**: public
- **Lines**: 182–184 (docstring 181), proof length 1 line
- **Notes**: Only the left-inverse direction is stated; the right inverse (`taylor α (taylor (-α) P) = P`, surjectivity) is absent from the project. Negation is written as the lambda `fun j ↦ -α j` rather than Pi negation `-α` (definitionally equal, evidence item 3).

## Junk check (Step 8)
- Used anywhere? Yes: two direct call sites (Roth/Taylor.lean:188, 208), and through them Taylor's expansion `eq_sum_box_hasseDeriv` / `eval_eq_sum_box`, which Roth/Main.lean:390 uses.
- Wrapper of 1–2 mathlib calls? It is a two-step corollary of project lemmas (`taylor_taylor` + `taylor_zero`), not of mathlib calls; plain `simp` does not prove it (evidence item 2).
- Does mathlib have it? No multivariate translation operator, so no. The univariate content exists in mathlib only inside `Polynomial.taylorEquiv` (fields `left_inv` / `right_inv`, Mathlib/Algebra/Polynomial/Taylor.lean:191) and in `Polynomial.algEquivAevalXAddC_symm`.
- Too specific / inline? No: invertibility of translation is the basic structural fact used for injectivity and for Taylor's expansion.
- Well-chosen? Yes, but better packaged as an `AlgEquiv` (see Phase 4c).
- Conclusion: `KEEP`. Action: keep locally; upstream with `MvPolynomial.taylor` as part of an `MvPolynomial.taylorEquiv`.

## Mathlibable assessment (Step 9)

Not private, not `_aux`, docstring not internal/auxiliary, Step 8 said KEEP; the qualified name `MvPolynomial.taylor_neg_taylor` is absent from mathlib (namespace-aware grep: no `taylor_neg_taylor` anywhere in Mathlib). It is not a glue lemma: its proof needs `taylor_taylor` and `taylor_zero`, and plain `simp` fails (evidence item 2). Full workflow run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Taylor` elaborates with no errors in lean-lsp)
- decl `MvPolynomial.taylor_neg_taylor`: resolved at Roth/Taylor.lean:182
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Taylor expansion of multivariate polynomials: translation `P ↦ P(X + α)`, its coefficients as Hasse derivatives, and Taylor's expansion.

### Statement (Phase 1)

`MvPolynomial.taylor_neg_taylor` is a theorem stating the following:

Let `A` be a commutative ring, `σ` a set of variables, `α ∈ A^σ`, and `τ_α : A[X_σ] → A[X_σ]`, `τ_α P = P(X + α)`, the translation. Then `τ_{-α} ∘ τ_α = id`: for every polynomial `P`, `P(X + α)` evaluated at `X - α` is `P`. Together with the symmetric statement (obtained by replacing `α` with `-α`), translation by `α` is an `A`-algebra automorphism of `A[X_σ]` with inverse translation by `-α`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `A : Type*`, `[CommRing A]` — coefficient ring; negation needed.
- `α : σ → A` — translation vector.
- `P : MvPolynomial σ A` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `τ_{-α}(τ_α P) = P`.

Conclusion (Lean): `taylor (fun j ↦ -α j) (taylor α P) = P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API corollary (left inverse) of the parent definition `MvPolynomial.taylor`; not a main result.

(Note: literature width is EXHAUSTIVE regardless. BIG/SMALL is recorded for framing only.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | inverse of polynomial translation P(X+a) by P(X-a) multivariate polynomial automorphism | partial | maps of the form `Id + H` with inverse `Id - H` (quasi-translations); translation `X ↦ X + a` has inverse `X ↦ X - a` | arXiv 1506.01654, 1601.00332, 1611.01940 (inversion of polynomial maps); the translation case is treated as immediate |
| 2 | WebSearch (general form) | translations are automorphisms of polynomial ring R[x1,...,xn] x_i maps to x_i + a_i inverse group | partial | translations form a subgroup of `Aut(R[X_1..X_n])` isomorphic to `(R^n, +)`; Jacobian identity, so automorphism; univariate: `X ↦ aX + b` invertible with inverse `a⁻¹(X - b)` | arXiv 1710.08022, math/0512215, math/0604477, 1207.2045; most general form: automorphism of `A[X_σ]` for `A` a commutative ring |
| 3 | WebSearch (named-after / aliases) | "Taylor shift" inverse shift by -a invertible polynomial | partial | Taylor shift `p(x) ↦ p(x + a)`; inverse is the shift by `-a` | planetcalc "Polynomial Taylor Shift", Codeforces Taylor shifts blog, arXiv 2305.17877 (analogous shift inverse); alias "Taylor shift" matches mathlib's `taylor` name |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for translat / `P_\alpha` / `X+\alpha` | partial | l.547 "Let `P_α(X)=P(X+α)`"; l.600–629 translated polynomials | the paper never states invertibility; the project needs it for Taylor's expansion (recovering `P` from `P(X + α)`) and for `taylor_injective` |
| 6 | nLab | automorphism / affine space / translation | partial | translations of affine space `A^n` are automorphisms (the additive group acting on itself); on the coordinate ring they act by `A`-algebra automorphisms | no polynomial-specific lemma; confirms the group-action packaging (an action of a group lands in automorphisms) |
| 7 | nCatLab | — | n/a | — | not a categorical statement beyond the action remark in row 6 |
| 8 | Stacks Project | — | n/a | — | translations are the action of the group scheme `G_a^n` on `A^n`; Stacks has no elementary polynomial-ring translation lemma |
| 9 | MathOverflow / Math.SE | (results of #1, #2) | no | — | no dedicated thread; regarded as immediate |
| 10 | recent arXiv (last 5 years) | (results of #1–#3) | partial | arXiv 2401.11072 (2024), 2305.17877 (2023) | same "translation is an automorphism with inverse the opposite translation" form |

### Literature summary (Phase 3)

Concept identified as: invertibility of translation (Taylor shift); translations are automorphisms of the polynomial ring, `τ_α⁻¹ = τ_{-α}`.
Sources agree on the standard form: yes.
Most general standard form: for `A` a commutative ring and any variable set, `τ_α` is an `A`-algebra automorphism of `A[X_σ]` with inverse `τ_{-α}` (both composites are the identity).
Generality dimensions where the literature varies:
  - coefficient ring: field to commutative ring; ours is commutative ring, the natural setting where `-α` exists.
  - packaging: one-sided identity vs. "is an automorphism with inverse τ_{-α}" (automorphism-group literature, and mathlib's univariate `taylorEquiv` / `algEquivAevalXAddC`).
Disagreement with the literature: the project states only one composite (left inverse) and not the automorphism.

### Generality analysis — `MvPolynomial.taylor_neg_taylor`

Literature-standard form (from Phase 3): `τ_α` is an `A`-algebra automorphism of `A[X_σ]` with inverse `τ_{-α}`, `A` a commutative ring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommRing A]` | commutative ring | commutative ring | only with an extra hypothesis | `-α` needs negation. A `CommSemiring` version with hypothesis `β + α = 0` compiles (evidence item 7), but it is the same statement with the inverse named, has no mathlib precedent (univariate `taylorEquiv` is `CommRing`-only) and would only matter for semirings with additive units; not proposed |
| 2 | `α : σ → A` | arbitrary | vector in `A^σ` | no | already the full group `σ → A` |
| 3 | `σ : Type*` | arbitrary | finite | no (already more general) | — |
| 4 | one-sided statement | left inverse only | two-sided inverse / automorphism | n/a (packaging) | right inverse `taylor_taylor_neg` and the `AlgEquiv` compile (evidence items 4, 5); recorded under Phase 4c |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (the only typeclass is needed for negation; the semiring form with a hypothesis, evidence item 7, is a restatement rather than a useful weakening and is not proposed).
Proposed restatement: none for hypothesis generality; the packaging change is Phase 4c.

Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | no | proof is generic (composition law + zero translation) | — |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | `CommRing` needed for `-α` (row 1 of 4a) | — |
| 6 | higher-categorical / bundled? | yes | bundle as `taylorEquiv α : MvPolynomial σ A ≃ₐ[A] MvPolynomial σ A` with `coe_taylorEquiv` and `taylorEquiv_symm : (taylorEquiv α).symm = taylorEquiv (-α)` (evidence item 5, compiles), exactly mirroring `Polynomial.taylorEquiv` / `taylorEquiv_symm` (Mathlib/Algebra/Polynomial/Taylor.lean:191, 201) | the whole `AlgEquiv` API: `injective`, `surjective`, `map_eq_zero_iff`, `symm_apply_apply`, transport of ideals and submodules (`Ideal.map`/`comap`, as mathlib does univariately in RingTheory/Polynomial/DegreeLT.lean:161–172 with `comap_taylorEquiv_degreeLT`); the project's `taylor_injective` and `taylor_eq_zero_iff` become one-liners (evidence item 6), and surjectivity, currently unavailable, comes for free |
| 7 | concrete index to general? | no | index already general | — |
| 8 | concrete-via-abstract? | no | statement mentions only the project operator; proof is the group law of an action, which is already the abstract content | — |
| 9 | false-generalisation guard | no false generalisation | the `AlgEquiv` is the same mathematical object (its inverse field is literally this lemma); `taylor_neg_taylor` stays as a named lemma | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement:
    ```lean
    theorem taylor_neg_taylor (α : σ → A) (P : MvPolynomial σ A) : taylor (-α) (taylor α P) = P
    theorem taylor_taylor_neg (α : σ → A) (P : MvPolynomial σ A) : taylor α (taylor (-α) P) = P
    noncomputable def taylorEquiv (α : σ → A) : MvPolynomial σ A ≃ₐ[A] MvPolynomial σ A :=
      AlgEquiv.ofAlgHom (taylor α) (taylor (-α)) (AlgHom.ext (taylor_taylor_neg α))
        (AlgHom.ext (taylor_neg_taylor α))
    @[simp] theorem coe_taylorEquiv (α : σ → A) : (taylorEquiv α : _ → _) = taylor α
    @[simp] theorem taylorEquiv_symm (α : σ → A) : (taylorEquiv α).symm = taylorEquiv (-α)
    ```
  - Cost: CHEAP (all compiled in evidence items 3–5).
  - Mathlib downstream this enables: `AlgEquiv.injective` / `surjective` / `map_eq_zero_iff` (replacing hand-rolled `taylor_injective`, `taylor_eq_zero_iff`), `Ideal.map_comap_of_equiv`-style transport (the univariate `comap_taylorEquiv_degreeLT` pattern), and composition with `AlgEquiv.trans` (e.g. with `rename` equivalences).
  - Real mathematical improvement: it states the actual theorem of the literature (translation is an automorphism with inverse `τ_{-α}`), supplies the missing right inverse, and matches the established univariate mathlib API shape.

### Proof strategy — `MvPolynomial.taylor_neg_taylor`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | composition law + identity, as in `Polynomial.taylorEquiv`'s `left_inv` | — |
| 5 | missing mathlib helpers | no | needs only the parent-PR lemmas `taylor_taylor`, `taylor_zero` | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (`simp [taylor_taylor]`; mirrors `Polynomial.sum_taylor_eq`'s `rw [taylor_taylor, neg_add_cancel, taylor_zero]`. With the Pi-negation statement a mathlib version could be `by rw [taylor_taylor, neg_add_cancel, taylor_zero]` once `taylor_zero` is stated as `taylor 0 P = P`).

### Diamond / defeq risk

n/a — declaration kind is theorem. (The proposed companion `taylorEquiv` is built by `AlgEquiv.ofAlgHom` from existing `AlgHom`s with `coe_taylorEquiv` holding by `rfl`, the same construction pattern as `Polynomial.taylorEquiv`; no new instances or coercions.)

### Mathlib search-status: `MvPolynomial.taylor_neg_taylor`

[A] Lean-Finder       "translation of a multivariable polynomial ring by a vector is an algebra automorphism with inverse translation by the negative"   `Polynomial.algEquivAevalXAddC_symm`, `Polynomial.algEquivAevalXAddC`, `Polynomial.taylorEquiv` (all univariate), `MvPolynomial.mvPolynomialEquivMvPolynomial_symm_apply` (generic ring-equiv builder); no multivariate translation
[B] Loogle            `MvPolynomial.aeval, Neg.neg, MvPolynomial.X, MvPolynomial.C`   no hits
[C] LeanSearch        "multivariate polynomial substitute X + C a then X - C a gives back the polynomial"   `Polynomial.algEquivAevalXAddC_symm` / `_symm_apply` / `_apply`, `Polynomial.dvd_comp_X_add_C_iff` (all univariate); no hit
[D] Grep mathlib src  `taylor_neg_taylor`, `taylorEquiv`, `X i + C`, `X i - C` under `Mathlib/Algebra/MvPolynomial`, `Mathlib/RingTheory/MvPolynomial`   only `MonomialOrder.lean:1440–1458` (degree/monic of `X i ± C r`, unrelated); `taylorEquiv` only univariate (Algebra/Polynomial/Taylor.lean:191–204, used in RingTheory/Polynomial/DegreeLT.lean:161–172)
[E] Name pattern      `MvPolynomial.taylor_neg_taylor`, `MvPolynomial.taylorEquiv` (namespace-aware grep of `.lake/packages/mathlib/Mathlib/`)   no hits

Searched for both the user's form (left-inverse identity) and the literature-standard form (translation as an algebra automorphism with inverse translation by `-α`; mathlib has this only univariately as `Polynomial.taylorEquiv` and `Polynomial.algEquivAevalXAddC`).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); univariate templates `Polynomial.taylorEquiv`, `Polynomial.taylorEquiv_symm`, `Polynomial.algEquivAevalXAddC_symm`.

### Normal-form check — `MvPolynomial.taylor_neg_taylor`

Equivalent formalisms this statement could take: `taylor (fun j ↦ -α j) (taylor α P) = P` (current); `taylor (-α) (taylor α P) = P` (Pi negation); `(taylor (-α)).comp (taylor α) = AlgHom.id`; `(taylorEquiv α).symm = taylorEquiv (-α)` together with `AlgEquiv.symm_apply_apply`.
Does mathlib already have a canonical form for this idea? yes (univariate): `Polynomial.taylorEquiv` with `taylorEquiv_symm : (taylorEquiv r).symm = taylorEquiv (-r)`; the pointwise inverse identity is not a standalone mathlib lemma, it is a field of the equiv.
Our statement is stated against the canonical form? partly: it is the `left_inv` field; the canonical packaging (the `AlgEquiv` plus `symm` lemma) is missing.
RHS convention respected? yes (simplifies to `P`).

### Syntactic generality — `MvPolynomial.taylor_neg_taylor`

Alternative restatements attempted:
- current lambda form
- Pi negation `taylor (-α) (taylor α P) = P` (evidence item 3, by the term `taylor_neg_taylor α P`)
- right inverse `taylor α (taylor (-α) P) = P` (item 4)
- `AlgEquiv` packaging (item 5)
Chosen restatement: Pi negation as the pointwise lemma, plus `taylor_taylor_neg` and `taylorEquiv` / `taylorEquiv_symm`.
Justification: `-α` matches mathlib's `taylorEquiv (-r)` and rewrites with `neg_add_cancel`, `Pi.neg_apply`; the equiv gives callers `injective`/`surjective`/`map_eq_zero_iff` without re-deriving them.

### Superfluous-argument audit — `MvPolynomial.taylor_neg_taylor`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommRing A]` | yes | `-α` requires negation; the semiring variant needs an explicit inverse hypothesis (item 7) |
| 2 | `α`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (canonical form is the `AlgEquiv` `taylorEquiv` with `taylorEquiv_symm`, keeping this lemma as the pointwise left inverse)
Syntactic generality: RESTATE (Pi negation `taylor (-α)`; add right inverse `taylor_taylor_neg`)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.taylor_neg_taylor`

Internal use count: 0  (outside the declaring file); 2 inside Roth/Taylor.lean
External-to-file callers: 0 distinct files (indirect: Roth/Main.lean:390 via `eval_eq_sum_box`)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Taylor.lean:188 | `Function.LeftInverse.injective (taylor_neg_taylor α)` (proof of `taylor_injective`) |
| Roth/Taylor.lean:208 | `calc P = taylor (fun j ↦ -α j) (taylor α P) := (taylor_neg_taylor α P).symm` (proof of `eq_sum_box_hasseDeriv`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `MvPolynomial.taylor_neg_taylor`?):
  - (none) — `grep -rn "taylor_taylor\|neg_add_cancel" Roth/` shows `taylor_taylor` used only in this proof; no other inversion of a translation in the project.

### Composition check (Phase 6)

Can `MvPolynomial.taylor_neg_taylor` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [taylor_taylor, neg_add_cancel, taylor_zero]` (Pi form) / `simp [taylor_taylor]` (current form).
  - Mathlib decls used: `neg_add_cancel`; but `taylor_taylor` and `taylor_zero` are project lemmas about an operator absent from mathlib.
  - Result: succeeds only given the parent operator and its API; plain `simp` fails (evidence item 2).
  - Notes: in the univariate mathlib case the same three-step argument is the `left_inv` field of `taylorEquiv`.

Attempt 2: unfold to `aeval` and use `comp_aeval_apply` + `aeval_X_left_apply`.
  - Result: partial — `rw [comp_aeval_apply]` then a `simp` step is needed; a proof, not a call chain, and still needs the operator to state the lemma.

Conclusion: NOT-COMPOSABLE (the operator is new; with it, this is a corollary that mathlib's univariate API packages into `taylorEquiv`)

## Verdict: `MvPolynomial.taylor_neg_taylor`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): translations are automorphisms of the polynomial ring forming a group isomorphic to `(A^σ, +)`, inverse of `X ↦ X + a` is `X ↦ X - a` (arXiv 1710.08022, 1506.01654; Taylor-shift literature).
- Generality analysis (Phase 4): MAXIMALLY GENERAL in hypotheses; Phase 4c: modern idiom available — bundle as the `AlgEquiv` `taylorEquiv` (compiled, evidence item 5).
- Mathlib search (Phase 5): not in mathlib; univariate templates `Polynomial.taylorEquiv`, `Polynomial.taylorEquiv_symm`, `Polynomial.algEquivAevalXAddC_symm`.
- Composition check (Phase 6): NOT-COMPOSABLE (operator absent from mathlib).

**Rationale:**

The parent `MvPolynomial.taylor` is YES-add-as-is, and invertibility of translation over a ring is basic API for it: the project uses it to get injectivity and to recover `P` from `P(X + α)` in Taylor's expansion (`eq_sum_box_hasseDeriv`, and through `eval_eq_sum_box` the main argument at Roth/Main.lean:390). But mathlib's univariate precedent does not ship this as a standalone one-sided lemma. It ships the `AlgEquiv` `Polynomial.taylorEquiv r` (inverse `taylorAlgHom (-r)`) with `coe_taylorEquiv` and `taylorEquiv_symm`, and downstream code (RingTheory/Polynomial/DegreeLT.lean) consumes the equiv. The project form states only the left inverse, so surjectivity is missing, and `taylor_injective` / `taylor_eq_zero_iff` are rebuilt by hand.

So the content should go to mathlib, restated for the modern idiom: `taylor_neg_taylor` with Pi negation `taylor (-α)`, the missing right inverse `taylor_taylor_neg`, and the bundled `taylorEquiv` with `coe_taylorEquiv` and `taylorEquiv_symm`. All of these compile from the current lemma (evidence items 3–5), and the project's `taylor_injective`, surjectivity and `taylor_eq_zero_iff` become `AlgEquiv` one-liners (item 6). No hypothesis can usefully be weakened (`CommRing` is needed for `-α`; the semiring form with a `β + α = 0` hypothesis compiles, item 7, but has no precedent and is not proposed). The bucket is generalise-first because of the packaging (MODERN-IDIOM), not because of a dropped hypothesis.

Reason for the generalisation:
  - MODERN-IDIOM (Bourbaki 2.0): bundle the two-sided inverse as the `AlgEquiv` `MvPolynomial.taylorEquiv`, matching `Polynomial.taylorEquiv`.
Proposed restatement:
```lean
theorem taylor_neg_taylor (α : σ → A) (P : MvPolynomial σ A) : taylor (-α) (taylor α P) = P := by
  simp [taylor_taylor]  -- or rw [taylor_taylor, neg_add_cancel, taylor_zero] with taylor_zero : taylor 0 P = P

theorem taylor_taylor_neg (α : σ → A) (P : MvPolynomial σ A) : taylor α (taylor (-α) P) = P := by
  simpa using taylor_neg_taylor (-α) P

noncomputable def taylorEquiv (α : σ → A) : MvPolynomial σ A ≃ₐ[A] MvPolynomial σ A :=
  AlgEquiv.ofAlgHom (taylor α) (taylor (-α))
    (AlgHom.ext fun P ↦ taylor_taylor_neg α P) (AlgHom.ext fun P ↦ taylor_neg_taylor α P)

@[simp] theorem coe_taylorEquiv (α : σ → A) : (taylorEquiv α : _ → _) = taylor α := rfl

@[simp] theorem taylorEquiv_symm (α : σ → A) : (taylorEquiv α).symm = taylorEquiv (-α) := by
  ext P : 1; rfl
```
Estimated cost of regeneralisation: CHEAP (all compiled in `.mathlib-quality/overview/evidence/MvPolynomial.taylor_neg_taylor/variants.lean`).
Mathlib downstream this enables:
  - `AlgEquiv.injective`, `AlgEquiv.surjective`, `map_eq_zero_iff` for translation (replacing the hand-rolled `taylor_injective` / `taylor_eq_zero_iff`; surjectivity currently unavailable).
  - Transport of ideals / submodules along translation, as `comap_taylorEquiv_degreeLT` does univariately (RingTheory/Polynomial/DegreeLT.lean:161–172), e.g. degree-bounded submodules `restrictDegree` preserved by `degreeOf_taylor_le`.
  - `AlgEquiv.trans` with renaming / `uniqueAlgEquiv` (bridge to `Polynomial.taylorEquiv`).
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/Taylor.lean (new file, with the parent `MvPolynomial.taylor`).
PR grouping: ship in the `MvPolynomial.taylor` PR with `taylor_taylor`, `taylor_zero`, `taylor_injective` (as `(taylorEquiv α).injective`).
Next action: run `/generalise MvPolynomial.taylor_neg_taylor` to confirm the `taylorEquiv` packaging and Pi-negation restatement before the PR.

---

## Next step

Before the `MvPolynomial.taylor` upstream PR, restate as `taylor (-α) (taylor α P) = P`, add `taylor_taylor_neg`, `taylorEquiv`, `coe_taylorEquiv`, `taylorEquiv_symm` (evidence items 3–5), and derive `taylor_injective` / `taylor_eq_zero_iff` from the equiv; locally no change is needed (call sites Roth/Taylor.lean:188, 208 work with either spelling).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.taylor_neg_taylor/variants.lean` (checked with `lean_diagnostic_messages`: no errors; only the header-docstring style linter warning): (1) project statement re-proved by the project proof; (2) `fail_if_success simp` shows plain `simp` does not prove it; (3) Pi-negation form `taylor (-α) (taylor α P) = P` by the term `taylor_neg_taylor α P` (definitionally equal); (4) right inverse `taylor_taylor_neg`; (5) `taylorEquiv` via `AlgEquiv.ofAlgHom`, `coe_taylorEquiv` (rfl), `taylorEquiv_symm`; (6) injectivity, surjectivity and `taylor α P = 0 ↔ P = 0` as `AlgEquiv` one-liners; (7) `CommSemiring` variant with hypothesis `β + α = 0` compiles (not proposed).
- Searches: WebSearch ×3 (table rows 1–3); Loogle `MvPolynomial.aeval, Neg.neg, MvPolynomial.X, MvPolynomial.C` (no hits); LeanSearch and Lean-Finder (univariate `algEquivAevalXAddC_symm`, `taylorEquiv` only); mathlib grep for `taylor_neg_taylor`, `taylorEquiv`, `X i ± C` (univariate only; `MonomialOrder.lean` unrelated). ChatGPT MCP: n/a (not configured).
- Project greps: `grep -rn taylor_neg_taylor Roth/` (Roth/Taylor.lean:182, 188, 208); downstream `grep -rn "taylor_injective\|taylor_eq_zero_iff\|eq_sum_box_hasseDeriv\|eval_eq_sum_box" Roth/` (only Roth/Main.lean:390 outside Taylor.lean); `.mathlib-quality/references/clean.tex` l.547, 600–629.
