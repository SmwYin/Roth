---
decl: MvPolynomial.taylor_injective
file: Roth/Taylor.lean
line: 187
kind: theorem
visibility: public
verdict: YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Injectivity of multivariate translation over a commutative ring is the exact analogue of mathlib's standalone Polynomial.taylor_injective (kept in mathlib alongside taylorEquiv), is absent for MvPolynomial, and is maximally general since an explicit counterexample over the semiring ℕ∞ shows CommRing cannot be weakened to CommSemiring.
action: Ship in the MvPolynomial.taylor upstream PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) next to taylor_neg_taylor and taylorEquiv, with proof (taylorEquiv α).injective and the simp companion taylor_inj mirroring Polynomial.taylor_inj; locally keep (only call site Roth/Taylor.lean:193 taylor_eq_zero_iff).
---

# MvPolynomial.taylor_injective

## Inventory entry

### `theorem MvPolynomial.taylor_injective`
- **Type**: `∀ {σ A : Type*} [CommRing A] (α : σ → A), Function.Injective ⇑(taylor α : MvPolynomial σ A →ₐ[A] MvPolynomial σ A)`
- **What**: Over a commutative ring, the translation `P ↦ P(X + α)` is injective: `P(X + α) = Q(X + α)` implies `P = Q`.
- **How**: one term, `Function.LeftInverse.injective (taylor_neg_taylor α)`: translation by `-α` is a left inverse (project lemma `taylor_neg_taylor`), and a map with a left inverse is injective.
- **Hypotheses**: `[CommRing A]` (section variable; needed, see Phase 4); no propositional hypotheses.
- **Uses from project**: `MvPolynomial.taylor`, `MvPolynomial.taylor_neg_taylor`
- **Used by**: Roth/Taylor.lean:193 (`taylor_eq_zero_iff`, via `(taylor_injective α).eq_iff' (map_zero _)`). `taylor_eq_zero_iff` is a `@[simp]` lemma not referenced by name elsewhere (`grep -rn taylor_eq_zero_iff Roth/`). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 186–188 (docstring 186, statement 187, proof 188), proof length 1 line
- **Notes**: Surjectivity is not stated in the project; the companion `taylor α P = taylor α Q ↔ P = Q` (mathlib univariate `Polynomial.taylor_inj`, simp) is also absent.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Taylor.lean:193 (`taylor_eq_zero_iff`).
- Wrapper of 1–2 mathlib calls? It is one mathlib call (`Function.LeftInverse.injective`) applied to the project lemma `taylor_neg_taylor`; the operator itself is not in mathlib, so it cannot be replaced by a mathlib lemma.
- Does mathlib have it? Not for `MvPolynomial` (no multivariate translation operator). Univariate analogue: `Polynomial.taylor_injective` (Mathlib/Algebra/Polynomial/Taylor.lean:130), used in Mathlib/FieldTheory/Laurent.lean:45–46.
- Too specific / inline? No: standard named API; mathlib keeps the univariate version as a standalone lemma even though `Polynomial.taylorEquiv` exists.
- Well-chosen? Yes.
- Conclusion: `KEEP`. Action: keep locally; upstream with `MvPolynomial.taylor`.

## Mathlibable assessment (Step 9)

Not private, not `_aux`, docstring not internal/auxiliary, Step 8 said KEEP; the qualified name `MvPolynomial.taylor_injective` is absent from mathlib (namespace-aware grep: `theorem taylor_injective` occurs only in Mathlib/Algebra/Polynomial/Taylor.lean, namespace `Polynomial`). Not a glue lemma in the brief's sense (not `rfl`/`Iff.rfl`/unfolding: it applies `LeftInverse.injective` to a project lemma with content), so the full workflow is run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Taylor` elaborates with no errors in lean-lsp)
- decl `MvPolynomial.taylor_injective`: resolved at Roth/Taylor.lean:187
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Taylor expansion of multivariate polynomials: translation `P ↦ P(X + α)`, its coefficients as Hasse derivatives, and Taylor's expansion.

### Statement (Phase 1)

`MvPolynomial.taylor_injective` is a theorem stating the following:

Let `A` be a commutative ring, `σ` a set of variables and `α ∈ A^σ`. The translation `τ_α : A[X_σ] → A[X_σ]`, `τ_α P = P(X + α)`, is injective: if `P(X + α) = Q(X + α)` then `P = Q`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `A : Type*`, `[CommRing A]` — coefficient ring.
- `α : σ → A` — translation vector.

Hypotheses (Lean side):
- none.

Conclusion (math): `τ_α` is injective.

Conclusion (Lean): `Function.Injective (taylor α : MvPolynomial σ A → _)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API corollary of the parent definition `MvPolynomial.taylor`; not a main result.

(Note: literature width is EXHAUSTIVE regardless. BIG/SMALL is recorded for framing only.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | polynomial translation P(x+a) injective map ring Taylor shift | partial | Taylor shift `p(x) ↦ p(x + a)`, computed as `e^{aD}`; inverse shift by `-a` | codeforces blog 99646, planetcalc 7726 (Shaw–Traub); injectivity treated as immediate from invertibility |
| 2 | WebSearch (general form) | translation x_i -> x_i + a_i automorphism of polynomial ring R[x_1,...,x_n] commutative ring | partial | translations `X ↦ X + v`, `v ∈ R^n`, form a subgroup of `Aut_R(R[X_1..X_n])` isomorphic to `(R^n, +)` | arXiv 1207.2045, 2210.00730, 0707.3151, 1709.04510; most general form: automorphism (hence injective) over any commutative ring |
| 3 | WebSearch (named-after / aliases) | "Taylor shift" multivariate polynomial invertible bijection semiring | partial | multivariate Taylor expansion via Hasse derivatives (arXiv 1812.07020, over finite fields); nothing for semirings | confirms the setting is rings; no semiring statement in the literature (and it is false, evidence item 5) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for injective / translat / `X+\alpha` | partial | l.547 "Let `P_α(X)=P(X+α)`"; l.600–629 translated polynomials | the paper never states injectivity; the project uses it only to get `taylor_eq_zero_iff` (`P ≠ 0 ⇒ P(X+α) ≠ 0`) |
| 6 | nLab | automorphism / affine space / translation | partial | translations of affine space are automorphisms (group acting on itself); on coordinate rings they act by algebra automorphisms | no polynomial-specific lemma |
| 7 | nCatLab | — | n/a | — | not a categorical statement beyond the action remark in row 6 |
| 8 | Stacks Project | — | n/a | — | translations are the `G_a^n` action on `A^n`; Stacks has no elementary polynomial-ring translation lemma |
| 9 | MathOverflow / Math.SE | (results of #1–#3) | no | — | no dedicated thread; regarded as immediate |
| 10 | recent arXiv (last 5 years) | (results of #1–#3) | partial | arXiv 2210.00730 (2022), 2501.10520 (2025): translations as elementary/affine tame automorphisms | same automorphism form |

### Literature summary (Phase 3)

Concept identified as: injectivity of the translation (Taylor shift) `P ↦ P(X + α)` on a polynomial ring.
Sources agree on the standard form: yes.
Most general standard form: for `A` a commutative ring and any variable set, `τ_α` is an `A`-algebra automorphism of `A[X_σ]` (inverse `τ_{-α}`), in particular injective.
Generality dimensions where the literature varies:
  - coefficient ring: field to commutative ring; ours is commutative ring. Over semirings injectivity fails in general (evidence item 5: over `ℕ∞`, `τ_⊤ X = τ_⊤ (X + 1)`).
  - packaging: "injective" vs. "automorphism".
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.taylor_injective`

Literature-standard form (from Phase 3): `τ_α` injective (indeed bijective) on `A[X_σ]`, `A` a commutative ring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommRing A]` | commutative ring | commutative ring | NO | false over commutative semirings: compiled counterexample over `ℕ∞` with `σ = Unit`, `α = ⊤`, where `taylor α X = X + ⊤ = taylor α (X + 1)` but `X ≠ X + 1` (evidence item 5). A cancellative-semiring version (via the Grothendieck ring and `taylor_map`) is plausible but not tested, has no mathlib precedent (univariate `Polynomial.taylor_injective` is `[Ring R]`) and is not claimed |
| 2 | `α : σ → A` | arbitrary | vector in `A^σ` | no | already the full group |
| 3 | `σ : Type*` | arbitrary | finite | no (already more general) | — |
| 4 | commutativity of `A` | `CommRing` | `Ring` in univariate mathlib | no | `MvPolynomial σ R` requires `CommSemiring R`, so commutativity is forced by the ambient type, not by the lemma |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (the only typeclass is necessary; its failure over semirings is compiled in evidence item 5).
Proposed restatement: none.

Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic statement |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | `CommRing` is necessary (item 5) | — |
| 6 | higher-categorical / bundled? | partly, but upstream | the bundling belongs to `taylor_neg_taylor` (proposed `taylorEquiv`); with it, this lemma's proof becomes `(taylorEquiv α).injective` (item 3). Mathlib keeps the univariate `Polynomial.taylor_injective` as a standalone lemma next to `Polynomial.taylorEquiv`, so the named lemma stays | `Function.Injective.eq_iff`, `injective_iff_map_eq_zero`, `LinearMap.map_eq_zero_iff` (as Mathlib/FieldTheory/Laurent.lean:45 uses the univariate one) |
| 7 | concrete index to general? | no | already general | — |
| 8 | concrete-via-abstract? | no | proof uses only the left inverse; the statement is about the project operator, and "map with a left inverse is injective" is already the mathlib lemma `Function.LeftInverse.injective` | — |
| 9 | false-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the statement already has mathlib's univariate shape (`Function.Injective (taylor r)`); the only idiomatic change (bundling as `taylorEquiv`) is a change to the proof and to the parent lemma `taylor_neg_taylor`, not to this statement.

### Proof strategy — `MvPolynomial.taylor_injective`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes (in the upstream PR) | `taylorEquiv` (proposed in the `taylor_neg_taylor` report); then `(taylorEquiv α).injective` | CHEAP (item 3 compiles) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (`Function.LeftInverse.injective` of the inverse identity; mathlib's univariate proof instead goes through `taylor_eq_zero` and leading coefficients, which does not generalise to several variables, so the left-inverse argument is the right one here). In the PR, `(taylorEquiv α).injective` is an equally short alternative once `taylorEquiv` is in.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.taylor_injective`

[A] Lean-Finder       "translation of multivariable polynomials by a vector is injective"   `MvPolynomial.expand_injective`, `MvPolynomial.X_injective`, `Polynomial.toMvPolynomial_injective`, `MvPolynomial.C_injective`, `Polynomial.expand_injective` (unrelated); no translation
[B] Loogle            `Function.Injective (MvPolynomial.aeval _)`   `MvPolynomial.aeval_injective_iff_of_isEmpty`, `algebraicIndependent_iff_injective_aeval` (building block, see Phase 6); no translation
[C] LeanSearch        "multivariate polynomial substitution X i + C (a i) is injective"   `Polynomial.toMvPolynomial_injective`, `MvPolynomial.C_injective`, `MvPolynomial.map_injective`, `MvPolynomial.X_injective`, `algebraicIndependent_iff_injective_aeval`; no hit
[D] Grep mathlib src  `taylor_injective`, `taylor_inj`, `taylorEquiv` under `Mathlib/`; `algebraicIndependent.*X` under RingTheory/AlgebraicIndependent   `taylor_injective` / `taylor_inj` only in Mathlib/Algebra/Polynomial/Taylor.lean:130–134 (univariate, `[Ring R]`); `MvPolynomial.algebraicIndependent_polynomial_aeval_X` (Transcendental.lean:265)
[E] Name pattern      `MvPolynomial.taylor_injective`, `MvPolynomial.taylor_inj` (namespace-aware grep of `.lake/packages/mathlib/Mathlib/`)   no hits

Searched for both the user's form (injectivity) and the literature-standard form (translation as an algebra automorphism; mathlib has it only univariately as `Polynomial.taylorEquiv`).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); univariate template `Polynomial.taylor_injective` / `Polynomial.taylor_inj`.

### Normal-form check — `MvPolynomial.taylor_injective`

Equivalent formalisms this statement could take: `Function.Injective (taylor α)` (current); `taylor α P = taylor α Q ↔ P = Q` (`taylor_inj`); `(taylorEquiv α).injective`; `RingHom.ker (taylor α) = ⊥`.
Does mathlib already have a canonical form for this idea? yes (univariate): `Polynomial.taylor_injective : Function.Injective (taylor r)` plus `@[simp] Polynomial.taylor_inj`.
Our statement is stated against the canonical form? yes (identical shape).
RHS convention respected? yes (for the proposed `taylor_inj`, RHS `P = Q`).

### Syntactic generality — `MvPolynomial.taylor_injective`

Alternative restatements attempted:
- `Function.Injective (taylor α)` (current; item 1)
- left inverse with Pi negation `taylor (-α)` (item 2, same proof)
- `(taylorEquiv α).injective` (item 3)
- `taylor α P = taylor α Q ↔ P = Q` (item 4)
Chosen restatement: current statement, plus the simp companion `taylor_inj`.
Justification: `Function.Injective` composes with `.eq_iff`, `.eq_iff'`, `injective_iff_map_eq_zero`; the `↔` companion is what `simp` uses, matching the univariate API.

### Superfluous-argument audit — `MvPolynomial.taylor_injective`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommRing A]` | yes | conclusion false over `ℕ∞` (item 5) |
| 2 | `α` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (add the companion `taylor_inj`, not a restatement)
Superfluous arguments: NONE

Overall: SHIP-AS-STATED

### Call sites — `MvPolynomial.taylor_injective`

Internal use count: 0  (outside the declaring file); 1 inside Roth/Taylor.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Taylor.lean:193 | `(taylor_injective α).eq_iff' (map_zero _)` (proof of `taylor_eq_zero_iff`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `MvPolynomial.taylor_injective`?):
  - (none) — `grep -rn "LeftInverse.injective\|taylor_neg_taylor" Roth/` shows only Roth/Taylor.lean:188 (this proof) and :208 (`eq_sum_box_hasseDeriv`, which uses the inverse identity directly, not injectivity).

### Composition check (Phase 6)

Can `MvPolynomial.taylor_injective` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Function.LeftInverse.injective (taylor_neg_taylor α)`.
  - Mathlib decls used: `Function.LeftInverse.injective`; but `taylor_neg_taylor` and `taylor` are project declarations absent from mathlib.
  - Result: succeeds only given the parent operator and its inverse lemma (item 1).
  - Notes: the statement cannot even be written without the new operator.

Attempt 2: unfold `taylor α = aeval (fun j ↦ X j + C (α j))` and use `algebraicIndependent_iff_injective_aeval` with `MvPolynomial.algebraicIndependent_polynomial_aeval_X` for `f j = Polynomial.X + Polynomial.C (α j)`.
  - Result: partial (untested sketch, not claimed to compile): needs transcendence of `X + C a`, a rewrite of `Polynomial.aeval (X j) (X + C a)` to `X j + C a`, and an unfolding of `taylor`; at least four steps, a heavier import (Transcendental), and it still needs the operator to state the lemma.

Conclusion: NOT-COMPOSABLE (the operator is new; with it, this is a one-term corollary, which is exactly how mathlib ships the univariate `Polynomial.taylor_injective`).

## Verdict: `MvPolynomial.taylor_injective`

**Category:** YES-add-as-is

**Evidence:**
- Literature search (Phase 3): translations form a subgroup of `Aut_A(A[X_σ])` isomorphic to `(A^σ, +)` (arXiv 1207.2045, 2210.00730), hence injective over any commutative ring; nothing for semirings.
- Generality analysis (Phase 4): MAXIMALLY GENERAL; `CommRing` necessary, with a compiled counterexample over `ℕ∞` (item 5). Phase 4c: no modern-idiom change to this statement.
- Mathlib search (Phase 5): not in mathlib; univariate template `Polynomial.taylor_injective` (Mathlib/Algebra/Polynomial/Taylor.lean:130) and `Polynomial.taylor_inj`.
- Composition check (Phase 6): NOT-COMPOSABLE (operator absent from mathlib).

**Rationale:**

The parent `MvPolynomial.taylor` is YES-add-as-is and its inverse lemma `taylor_neg_taylor` is YES-but-generalise-first (bundling as `taylorEquiv`). Injectivity is basic API for translation and has an exact univariate precedent. Mathlib ships `Polynomial.taylor_injective` as a standalone named lemma even though `Polynomial.taylorEquiv` exists, together with the simp lemma `Polynomial.taylor_inj`. Downstream mathlib code uses the named lemma directly (`LinearMap.map_eq_zero_iff _ (taylor_injective _)` in Mathlib/FieldTheory/Laurent.lean:45–46). The project statement has exactly that shape, so it is the right statement to add. In the project it supplies `taylor_eq_zero_iff`.

WHY add it: the gap is the missing multivariate translation API. There is no `MvPolynomial` analogue of Mathlib/Algebra/Polynomial/Taylor.lean, so the univariate injectivity / `taylor_inj` / `taylor_eq_zero` trio has no multivariate counterpart. Mathlib's univariate proof (leading coefficients via `taylor_eq_zero`) does not carry over to several variables. The left-inverse proof here does, and so does `(taylorEquiv α).injective` once the equiv lands. With the lemma, `Function.Injective.eq_iff`, `injective_iff_map_eq_zero` and `LinearMap.map_eq_zero_iff` apply to multivariate translation, as they do univariately. The statement cannot be weakened: `CommRing` is necessary (item 5). It is not the trivial `AlgEquiv.injective` of an existing mathlib equiv, because no multivariate equiv exists yet.

Proposed mathlib location:    Mathlib/Algebra/MvPolynomial/Taylor.lean (new file, with the parent `MvPolynomial.taylor`)
Proposed PR title:            "feat(Algebra/MvPolynomial): add MvPolynomial.taylor" (this lemma ships inside it, not as its own PR)
PR grouping:                  ship with `MvPolynomial.taylor`, `taylor_taylor`, `taylor_zero`, `taylor_neg_taylor` (restated with `-α`), the proposed `taylorEquiv` (proof `(taylorEquiv α).injective` is then available), plus the new companion `@[simp] taylor_inj` and `taylor_eq_zero_iff`.
Pre-PR checklist before opening:
  - [ ] `/generalise MvPolynomial.taylor_injective` — confirm no further weakening (the ℕ∞ counterexample, item 5, already rules out `CommSemiring`)
  - [ ] `/cleanup Roth/Taylor.lean MvPolynomial.taylor_injective` — full audit + diff gates
  - [ ] Pick a mathlib reviewer from recent commits under `Mathlib/Algebra/MvPolynomial/` and `Mathlib/Algebra/Polynomial/Taylor.lean`

---

## Next step

Include in the `MvPolynomial.taylor` upstream PR as stated, with proof `Function.LeftInverse.injective (taylor_neg_taylor α)` or `(taylorEquiv α).injective`, and add `@[simp] theorem taylor_inj : taylor α P = taylor α Q ↔ P = Q := (taylor_injective α).eq_iff` (item 4). Locally no change is needed (sole call site Roth/Taylor.lean:193).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.taylor_injective/variants.lean` (checked with `lean_diagnostic_messages`: no errors; only the header-docstring style linter warning): (1) project statement with the project proof; (2) same proof with Pi negation `g := taylor (-α)`; (3) `taylor_taylor_neg`, `taylorEquiv` via `AlgEquiv.ofAlgHom`, and injectivity as `(taylorEquiv α).injective`; (4) companion `taylor α P = taylor α Q ↔ P = Q` by `(taylor_injective α).eq_iff`; (5) counterexample: `¬ Function.Injective (taylor (fun _ : Unit ↦ (⊤ : ℕ∞)))`, since `taylor ⊤ X = taylor ⊤ (X + C 1)` by `top_add`, while their constant coefficients 0 and 1 differ. So `CommRing` cannot be weakened to `CommSemiring`.
- Searches: WebSearch ×3 (table rows 1–3); Lean-Finder, LeanSearch, Loogle `Function.Injective (MvPolynomial.aeval _)` (Phase 5 block); mathlib greps for `taylor_injective`, `taylor_inj`, `taylor_eq_zero`, `algebraicIndependent` (univariate Taylor.lean:104–134 only; Laurent.lean:45–46 as downstream user). ChatGPT MCP: n/a (not configured).
- Project greps: `grep -rn taylor_injective Roth/` (Roth/Taylor.lean:187, 193); `grep -rn taylor_eq_zero_iff Roth/` (only its declaration, Roth/Taylor.lean:192); `.mathlib-quality/references/clean.tex` l.547, 600–629.
