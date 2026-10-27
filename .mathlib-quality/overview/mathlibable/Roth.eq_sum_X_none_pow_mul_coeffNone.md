---
decl: Roth.eq_sum_X_none_pow_mul_coeffNone
file: Roth/Separation.lean
line: 98
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: INLINE
rationale: Unfolding coeffNone (rfl) this is the inverse of optionEquivLeft (optionEquivLeft_symm_apply, an aevalTower of rename some and X none) expanded by Polynomial.eval₂_eq_sum_range' with the bound from natDegree_optionEquivLeft, a 2-line mathlib composition (compiled in evidence).
action: Inline the 2-line composition at its single call site Roth/Separation.lean:335 (exists_separated_representation), or at least replace the 9-line proof by it; this also orphans the private coeff_X_none_pow_mul_rename (l.64) and eq_mapDomain_some_add_single (l.57), and removes a use of coeff_coeffNone; no mathlib PR.
---

# Roth.eq_sum_X_none_pow_mul_coeffNone

## Inventory entry

### `theorem Roth.eq_sum_X_none_pow_mul_coeffNone`
- **Type**: `{τ : Type*} {R : Type*} [CommSemiring R] (P : MvPolynomial (Option τ) R) {n : ℕ} (hn : degreeOf none P ≤ n) : P = ∑ ν ∈ Finset.range (n + 1), X none ^ ν * rename some (coeffNone P ν)`. The section's `[Fintype τ] [DecidableEq τ]` are omitted via `omit ... in` (confirmed by `#check`, evidence (0)).
- **What**: If `P` has degree at most `n` in `x_none`, then `P = ∑_{ν ≤ n} x_none^ν · φ_ν(x_τ)`, where `φ_ν = coeffNone P ν`.
- **How**: Coefficientwise (`ext e`, `coeff_sum`). The private `coeff_X_none_pow_mul_rename` turns each summand's coefficient into an `if`, and `Finset.sum_ite_eq` collapses the sum. In range, it uses `coeff_coeffNone` plus `eq_mapDomain_some_add_single`. Out of range, it uses `monomial_le_degreeOf` with `hn` to show the coefficient is zero.
- **Hypotheses**: `[CommSemiring R]`; `hn : degreeOf none P ≤ n`.
- **Uses from project**: `Roth.coeffNone`, `Roth.coeff_coeffNone`, `Roth.eq_mapDomain_some_add_single`, private `Roth.coeff_X_none_pow_mul_rename`.
- **Used by**: `Roth.exists_separated_representation` (Roth/Separation.lean:335, `exact eq_sum_X_none_pow_mul_coeffNone P hn`) only (`grep -rn` over `Roth/`).
- **Visibility**: public
- **Lines**: 93–108, proof length 9 lines (100–108)
- **Notes**: It is the only user of the private `coeff_X_none_pow_mul_rename` and of `eq_mapDomain_some_add_single`. Both become dead once the proof is replaced by the mathlib composition.

## Junk check (Step 8)
- Used anywhere? Yes, once (Separation.lean:335).
- Wrapper of 1–2 mathlib calls? Yes, effectively. After unfolding `coeffNone` it is `optionEquivLeft_symm_apply` followed by `Polynomial.eval₂_eq_sum_range'`, with the degree bound from `natDegree_optionEquivLeft` (evidence (1)–(2)).
- Does mathlib have it? Not as a named statement. The pieces are there: `optionEquivLeft_symm_apply` exhibits the inverse as `Polynomial.aevalTower (rename some) (X none)`, and `eval₂_eq_sum_range'` expands any `eval₂` as a finite sum.
- Too specific (inline)? It has a single caller, and the composition is two lines.
- Well-chosen? The statement is reasonable, but its 9-line coefficientwise proof drags in three helper declarations that the composition makes unnecessary.
- Conclusion: `INLINE`. Inline the 2-line composition at :335, or keep the name with the 2-line proof if the source citation is wanted. Either way, delete the orphaned helpers `coeff_X_none_pow_mul_rename` and `eq_mapDomain_some_add_single`.

## Mathlibable assessment (Step 9)

Pre-filter: not private, not `_aux`, docstring not internal/auxiliary, Step 8 = INLINE (not REMOVE). The qualified name `Roth.eq_sum_X_none_pow_mul_coeffNone` is absent from mathlib (no `namespace Roth`, no `coeffNone`). It is not a glue lemma (9-line proof). The parent `Roth.coeffNone` is `NO-composable-from-mathlib`, not `NO-mathlib-has-it`, so no inheritance. Per the orchestrator's instruction the re-aim rule is still applied: `coeffNone P ν` is rfl-equal to `(optionEquivLeft R τ P).coeff ν`, and the lemma is evaluated re-aimed at `optionEquivLeft`. Full workflow below.

### Baseline (Phase 0)
- lake build:               clean (per brief; the evidence file importing `Roth.Separation` compiles)
- decl `Roth.eq_sum_X_none_pow_mul_coeffNone`: resolved at Roth/Separation.lean:98
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`) in polynomials over `Option τ`, towards Lemma 2 of the source (`F = U(x_τ) V(x_none)`).

### Statement (Phase 1)

`Roth.eq_sum_X_none_pow_mul_coeffNone` is a theorem stating the following. Let `P ∈ R[x_τ, x_∗]` have degree at most `n` in `x_∗`, and let `φ_ν ∈ R[x_τ]` be the coefficient of `x_∗^ν` under `R[x_τ, x_∗] ≅ R[x_τ][x_∗]`. Then `P = ∑_{ν=0}^{n} x_∗^ν φ_ν(x_τ)`, with `φ_ν` viewed back in `R[x_τ, x_∗]`.

Variables / typeclasses involved (Lean side):
- `τ : Type*`: the non-distinguished variables. `none` is the distinguished variable `x_∗`.
- `R : Type*`, `[CommSemiring R]`: the coefficients.
- `P : MvPolynomial (Option τ) R`, `n : ℕ`.

Hypotheses (Lean side):
- `hn : degreeOf none P ≤ n`: `x_∗`-degree bound, so the range `0..n` suffices.

Conclusion (math): `P = ∑_{ν ≤ n} x_∗^ν φ_ν`.

Conclusion (Lean): `P = ∑ ν ∈ Finset.range (n + 1), X none ^ ν * rename some (coeffNone P ν)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a bookkeeping expansion lemma: "a polynomial is the sum of its terms" after the iterated-ring identification. It is not a main result and not a new structure.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 9
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multivariate polynomial expansion in powers of one variable f = sum f_k(x_1..x_{n-1}) x_n^k degree in x_n | yes | `f = ∑_{k ≤ deg_{x_n} f} f_k(x') x_n^k`, coefficients polynomials in the other variables (cyjax `univariate_coefficients` docs, CGAL Polynomial manual) | treated as notation/convention, not a theorem |
| 2 | WebSearch (general form) | polynomial ring R[x_1..x_n] isomorphic R[x_1..x_{n-1}][x_n] every polynomial written uniquely as sum of powers of x_n | yes | `R[x_1..x_n] ≅ R[x_1..x_{n-1}][x_n]`; powers of `x_n` form a basis over `R[x']` (Encyclopedia of Mathematics "Polynomial ring"; arXiv 1210.1476 iterated (skew) polynomial rings; arXiv 1702.00779 uses the iso explicitly) | the expansion is the univariate `p = ∑ coeff_i X^i` transported along the iso |
| 3 | WebSearch (aliases / mathlib) | Mathlib MvPolynomial finSuccEquiv optionEquivLeft sum X pow mul rename coefficient expansion lemma | partial | mathlib docs for `finSuccEquiv_apply`, `coeff_isHomogeneous_of_optionEquivLeft_symm`, `totalDegree_coeff_finSuccEquiv_add_le` | no named expansion lemma surfaced |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "powers of" | yes | line 374: "we can let `l-1=r_p` and `φ_ν(x_p)=x_p^ν` by collecting the terms in terms of the powers of `x_p`" | the source states exactly this step, informally |
| 6 | nLab | polynomial ring (as in parent assessment `Roth.coeffNone`) | yes | `A[X ⊔ Y] ≅ A[X][Y]` (free commutative algebra preserves coproducts) | only the isomorphism |
| 7 | nCatLab | free commutative algebra / coproduct | yes | same as #6 | no further content |
| 8 | Stacks Project | n/a | n/a | — | elementary commutative algebra; Stacks uses `R[x_1..x_n]` notationally, no expansion statement to compare |
| 9 | MathOverflow / Math.SE | (covered by #1/#2) | no | — | too elementary to be discussed as a result |
| 10 | recent arXiv | arXiv 1210.1476, 1702.00779 (surfaced by #2) | yes | iterated polynomial ring with the outer variable's powers as a basis | confirms the standard treatment |

### Literature summary (Phase 3)

Concept identified as: expanding a multivariate polynomial in powers of one variable, `P = ∑_k φ_k(x') x_n^k`, i.e. `p = ∑_{i<n} coeff_i(p) X^i` transported along `R[x', x_n] ≅ R[x'][x_n]`.
Sources agree on the standard form: yes. Everywhere it is immediate from the iterated-ring identification.
Most general standard form: for any variable set `σ`, any commutative semiring `R`, and any `n > deg_{x_∗} P`: `P = ∑_{i<n} φ_i(x_σ) x_∗^i`.
Generality dimensions where the literature varies:
  - bound: exact degree (`range (deg+1)`) vs any upper bound (`range n`, `n > deg`). The upper-bound form is more general and is what mathlib's `as_sum_range'` / `eval₂_eq_sum_range'` use.
  - coefficient ring: a commutative semiring is already most general.
  - factor order: `φ_i x^i` (mathlib's `C a * X ^ i`, `f (coeff i) * x ^ i`) vs `x^i φ_i` (project).
Disagreement with the literature: none mathematically. The project uses the `≤ n`/`range (n+1)` spelling and the `X^ν * φ_ν` factor order, while mathlib's canonical forms are `< n`/`range n` and `coeff * X^i`.

### Generality analysis — `Roth.eq_sum_X_none_pow_mul_coeffNone`

Literature-standard form (from Phase 3): `P = ∑ i ∈ range n, rename some ((optionEquivLeft R σ P).coeff i) * X none ^ i` for `degreeOf none P < n`, `[CommSemiring R]`, arbitrary `σ`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | `MvPolynomial` / `optionEquivLeft` need it |
| 2 | `τ : Type*` | arbitrary | arbitrary | no | section `Fintype`/`DecidableEq` already omitted (evidence (0)) |
| 3 | `hn : degreeOf none P ≤ n` with `range (n+1)` | upper bound | upper bound `< n` with `range n` | no (equivalent) | same strength; `≤ n` ↔ `< n+1`. Only a spelling difference (evidence (2)). The bound itself is needed, since a smaller range drops terms |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0
Proposed restatement (if STRICTLY NARROWER): n/a
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | single degree hypothesis, no bundled structure | — |
| 2 | Sequences to filters? | no | finite algebraic identity, no topology | — |
| 3 | Construction vs universal property? | yes | the expansion is the universal-property inverse `(optionEquivLeft R τ).symm = aevalTower (rename some) (X none)` applied to `as_sum`, which is how the evidence proof goes | the whole `Polynomial.eval₂`/`aevalTower` API |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field-specific to (semi)ring? | no | already `CommSemiring` | — |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general monoid? | no | `ℕ` exponents are intrinsic | — |
| 8 | Concrete-via-abstract? | no | the proof body is about `coeffNone` and `X none` throughout, and no named concrete object is abstracted away. The proof does reduce to the univariate fact, which is exactly the composition in Phase 6 | — |
| 9 | False-generalisation guard | no | no generalisation proposed; the re-aimed form is the same statement up to rfl and factor order | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the mathlib-idiomatic route (transport the univariate expansion along `optionEquivLeft`) yields this statement in two calls. That is a NO-composable signal, not a restatement to upstream.

### Proof strategy — `Roth.eq_sum_X_none_pow_mul_coeffNone`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | yes (mild) | the current proof works coefficient by coefficient (`ext e`, if-then-else bookkeeping, `monomial_le_degreeOf`). The point-free alternative rewrites `P` as `(optionEquivLeft).symm (optionEquivLeft P)` and uses `eval₂_eq_sum_range'` | CHEAP |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | use `optionEquivLeft_symm_apply` (inverse = `aevalTower (rename some) (X none)`) instead of re-deriving coefficients | CHEAP |
| 5 | missing mathlib helpers | no | everything needed exists: `optionEquivLeft_symm_apply`, `Polynomial.eval₂_eq_sum_range'`, `natDegree_optionEquivLeft` | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: `conv_lhs => rw [← (optionEquivLeft R τ).symm_apply_apply P, optionEquivLeft_symm_apply]; exact Polynomial.eval₂_eq_sum_range' _ ((natDegree_optionEquivLeft R P).trans_lt hn) _` (evidence (1)), plus `mul_comm` for the factor order (evidence (2)).
  - Cost: CHEAP
  - Missing mathlib API (if any): none
  - Would refactoring make the proof strictly shorter / cleaner? yes. 9 lines become 2–4, and three helper declarations (`coeff_X_none_pow_mul_rename`, `eq_mapDomain_some_add_single`, one use of `coeff_coeffNone`) drop out.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.eq_sum_X_none_pow_mul_coeffNone`

[A] Lean-Finder       "expand a multivariable polynomial in powers of one distinguished variable with coefficients polynomials in the remaining variables, sum over range of degreeOf"   hits: only `MvPolynomial.expand`, `Polynomial.expand_eq_sum` (unrelated Frobenius-type expansion); no expansion lemma
[B] Loogle            `MvPolynomial.optionEquivLeft, Finset.sum`   no hits (no mathlib lemma mentions both)
[C] LeanSearch        "multivariate polynomial over Option σ equals sum over i of X none ^ i times rename some of the i-th coefficient of optionEquivLeft"   hits: `optionEquivLeft_apply`, `optionEquivLeft_coeff_coeff`, `optionEquivLeft`, `finSuccEquiv`, `optionEquivLeft_X_none`, `degreeOf_eq_natDegree`; no expansion lemma
[D] Grep mathlib src  `X none ^`, `X .none ^`, `eq_sum_X_pow`, `sum_X_pow_mul`, `optionEquivLeft_symm_apply`, `eval₂_eq_sum_range'`   no expansion lemma; building blocks `optionEquivLeft_symm_apply` (simps lemma of `optionEquivLeft`, Mathlib/Algebra/MvPolynomial/Equiv.lean:466–470, used e.g. RingTheory/Algebraic/MvPolynomial.lean:60), `Polynomial.eval₂_eq_sum_range'` (Mathlib/Algebra/Polynomial/Eval/Degree.lean:49), `Polynomial.as_sum_range'` (Mathlib/Algebra/Polynomial/Degree/Support.lean:86), `natDegree_optionEquivLeft` (Equiv.lean:578)
[E] Name pattern      `lean_local_search` / grep `eq_sum_X_none`, `coeffNone`, `optionEquivLeft_symm`   only `optionEquivLeft_symm_C_X`, `optionEquivLeft_symm_C_C`, `optionEquivLeft_symm_X`, `optionEquivLeft_symm_apply`; nothing for the expansion

Searched for both:
  - the user's current form (`X none ^ ν * rename some (coeffNone P ν)` over `range (n+1)`): absent.
  - the literature-standard / re-aimed form (`rename some ((optionEquivLeft R σ P).coeff i) * X none ^ i` over `range n`): absent as a named lemma, but it is exactly `eval₂_eq_sum_range'` applied to `optionEquivLeft P` after `optionEquivLeft_symm_apply`.

Concluded: found building blocks (`MvPolynomial.optionEquivLeft_symm_apply`, `Polynomial.eval₂_eq_sum_range'`, `MvPolynomial.natDegree_optionEquivLeft`); composition yields our form.

### Normal-form check — `Roth.eq_sum_X_none_pow_mul_coeffNone`

Equivalent formalisms: (a) the project form; (b) `P = ∑ i ∈ range n, rename some ((optionEquivLeft R σ P).coeff i) * X none ^ i` with `degreeOf none P < n`; (c) `optionEquivLeft R σ P = ∑ i ∈ range n, C (coeff i) * X ^ i`, which is `as_sum_range_C_mul_X_pow'` on the polynomial side.
Does mathlib already have a canonical form for this idea? Yes on the univariate side: `Polynomial.as_sum_range'`, `as_sum_range_C_mul_X_pow'`, `eval₂_eq_sum_range'` (coefficient first, `< n` bound). Mathlib does not state the transported form; consumers work on the `Polynomial` side via `optionEquivLeft`.
Is our statement stated against the canonical form? Partly: it uses the `X^ν * φ_ν` order and the `≤ n` bound instead of mathlib's `coeff * X^i` and `< n`.
RHS convention respected? n/a (an expansion identity, not an equivalence).

### Syntactic generality — `Roth.eq_sum_X_none_pow_mul_coeffNone`

Alternative restatements attempted:
- (b) above, with `degreeOf none P < n`: proved in 2 lines (evidence (1)).
- the unconditional `range (degreeOf none P + 1)` form: a 1-line corollary of (b) (evidence (3)).
- the project form: follows from (b) by `Finset.sum_congr rfl fun _ _ ↦ mul_comm _ _` (evidence (2)).

Chosen restatement: the project's form is fine for its single caller, which immediately re-indexes it to a `Fin (n+1)` sum with `X none ^ ν` first.
Justification: the caller at :335 needs `X none ^ ν * rename some (v ν)` with `ν : Fin (n+1)`, so the project's factor order and `≤ n` bound match the call site.

### Superfluous-argument audit — `Roth.eq_sum_X_none_pow_mul_coeffNone`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | needed by `MvPolynomial` |
| 2 | `hn : degreeOf none P ≤ n` | yes | without it the range may miss terms |
| 3 | section `[Fintype τ] [DecidableEq τ]` | no | already omitted via `omit ... in` (evidence (0)) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (local; mathlib's canonical form lives on the `Polynomial` side)
Syntactic generality: OK (matches its only call site)
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally). Not a mathlib candidate.

### Call sites — `Roth.eq_sum_X_none_pow_mul_coeffNone`

Internal use count: 0 outside the declaring file; 1 inside Roth/Separation.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:335 | `exists_separated_representation`: `rw [Fin.sum_univ_eq_sum_range ...]; exact eq_sum_X_none_pow_mul_coeffNone P hn` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `eq_sum_X_none_pow_mul_coeffNone`?):
  - (none). The private `eq_sum_aeval_basis_coeffNone_aux` (l.265–275) takes the expansion as a hypothesis rather than re-deriving it.

### Composition check (Phase 6)

Can `Roth.eq_sum_X_none_pow_mul_coeffNone` be derived from mathlib in ≤3 chained calls?

Attempt 1: `conv_lhs => rw [← (optionEquivLeft R τ).symm_apply_apply P, optionEquivLeft_symm_apply]; exact Polynomial.eval₂_eq_sum_range' _ ((natDegree_optionEquivLeft R P).trans_lt hn) _`
  - Mathlib decls used: `AlgEquiv.symm_apply_apply`, `MvPolynomial.optionEquivLeft_symm_apply`, `Polynomial.eval₂_eq_sum_range'`, `MvPolynomial.natDegree_optionEquivLeft`
  - Result: succeeds for the coefficient-first, `< n` form (evidence (1)).
  - Notes: 2 tactic lines. The `rename some (coeff i)` and `X none ^ i` come out syntactically because the inverse is `aevalTower (rename some) (X none)`.

Attempt 2: exact project statement: `(attempt 1 at Nat.lt_succ_of_le hn).trans (Finset.sum_congr rfl fun _ _ ↦ mul_comm _ _)`
  - Mathlib decls used: as above plus `Finset.sum_congr`, `mul_comm`
  - Result: succeeds (evidence (2)); `coeffNone` unfolds by rfl.

Conclusion: COMPOSABLE

## Verdict: `Roth.eq_sum_X_none_pow_mul_coeffNone`

Verdict: NO-composable-from-mathlib

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): standard and immediate. It is the univariate expansion `p = ∑ coeff_i X^i` transported along `R[x', x_n] ≅ R[x'][x_n]`, and the source (clean.tex:374) uses it as "collecting the terms in terms of the powers of `x_p`".
- Generality analysis (Phase 4): MAXIMALLY GENERAL (the `≤ n` vs `< n` difference is spelling only).
- Mathlib search (Phase 5): no named lemma; building blocks `optionEquivLeft_symm_apply`, `Polynomial.eval₂_eq_sum_range'`, `natDegree_optionEquivLeft`.
- Composition check (Phase 6): COMPOSABLE, 2 lines (evidence (1)–(2)).

**Rationale:**
As the `Roth.coeffNone` report anticipated, the re-aim works. `coeffNone P ν` is `(optionEquivLeft R τ P).coeff ν` by rfl, and the inverse of `optionEquivLeft` is literally `Polynomial.aevalTower (rename some) (X none)` (`optionEquivLeft_symm_apply`, the simps lemma). Writing `P = (optionEquivLeft R τ).symm (optionEquivLeft R τ P)` and expanding the `eval₂` with `Polynomial.eval₂_eq_sum_range'` therefore gives `P = ∑ i ∈ range n, rename some (coeffNone P i) * X none ^ i` directly. The bound `natDegree (optionEquivLeft P) < n` comes from `natDegree_optionEquivLeft` and `hn`. This is even simpler than the `Polynomial.as_sum_range'` transport proposed in the parent report, because there is no need to push `optionEquivLeft` through sums, powers and `rename`.

Mathlib leaves this transported expansion unnamed, as it does for `finSuccEquiv`: its consumers work on the `Polynomial` side. A named mathlib lemma would only repackage `eval₂_eq_sum_range'`. Inside the project, the current 9-line coefficientwise proof is the only reason the private `coeff_X_none_pow_mul_rename` (l.64–75) and `eq_mapDomain_some_add_single` (l.57–61) exist, and it is one of the two users of the non-canonical `coeff_coeffNone`. The composition removes all three dependencies.

WHY not: the statement is a 2-line composition of mathlib primitives (`optionEquivLeft_symm_apply` + `Polynomial.eval₂_eq_sum_range'` + `natDegree_optionEquivLeft`), i.e. univariate expansion transported along an existing algebra equivalence.
Belongs-elsewhere check: nowhere outside the project. If the name is kept for the source citation, it stays in Roth/Separation.lean with the 2-line proof.
Mathlib building blocks: `MvPolynomial.optionEquivLeft_symm_apply` (generated by `@[simps!]` on `optionEquivLeft`, Mathlib/Algebra/MvPolynomial/Equiv.lean:466–470), `Polynomial.eval₂_eq_sum_range'` (Mathlib/Algebra/Polynomial/Eval/Degree.lean:49), `MvPolynomial.natDegree_optionEquivLeft` (Mathlib/Algebra/MvPolynomial/Equiv.lean:578), `AlgEquiv.symm_apply_apply`.
Composition sketch (≤3 lines):
```lean
example (P : MvPolynomial (Option τ) R) {n : ℕ} (hn : degreeOf none P < n) :
    P = ∑ i ∈ Finset.range n, rename some ((optionEquivLeft R τ P).coeff i) * X none ^ i := by
  conv_lhs => rw [← (optionEquivLeft R τ).symm_apply_apply P, optionEquivLeft_symm_apply]
  exact Polynomial.eval₂_eq_sum_range' _ ((natDegree_optionEquivLeft R P).trans_lt hn) _
```
Call sites in our project (from Phase 6.0): 1 (Roth/Separation.lean:335).
Refactor plan:
- Roth/Separation.lean:333–335 (`exists_separated_representation`, `hP'`): replace `exact eq_sum_X_none_pow_mul_coeffNone P hn` with the composition. Either use the two lines above at `Nat.lt_succ_of_le hn` followed by `.trans (Finset.sum_congr rfl fun _ _ ↦ mul_comm _ _)` (evidence (2)), or restate `hP'` with the factors in the order `rename some (v ν) * X none ^ ν` if the downstream `exists_coeffNone_basis_aux hP hP'` accepts it. Check its hypothesis shape at l.291 first, since it currently expects `X none ^ ν * rename some (v ν)`.
- Then delete `eq_sum_X_none_pow_mul_coeffNone` (l.93–108), the private `coeff_X_none_pow_mul_rename` (l.63–75, no other users) and `eq_mapDomain_some_add_single` (l.56–61, no other users). `coeff_coeffNone` is then used only at :129, per its own report.
- Lighter alternative: keep the theorem for its source citation (§2, Lemma 2) but replace its proof with the 3-line version from evidence (1)+(2), and still delete the two orphaned helpers.
Next action: inline (or re-prove) via `optionEquivLeft_symm_apply` + `Polynomial.eval₂_eq_sum_range'`, then delete the orphaned helpers. No mathlib PR.

---

## Next step

No mathlib PR. Re-prove or inline at Separation.lean:335 using `optionEquivLeft_symm_apply` + `Polynomial.eval₂_eq_sum_range'` + `natDegree_optionEquivLeft` (2 lines). Then delete the now-unused `coeff_X_none_pow_mul_rename` and `eq_mapDomain_some_add_single`.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/reaim.lean` (imports `Roth.Separation`). The first `lake env lean` run (about 35 s) compiled (0) and (1) but failed on a `simpa only [mul_comm]` variant of (2), which hit a `Finset.range n.succ` normal-form mismatch. (2) was rewritten with `Finset.sum_congr rfl fun _ _ ↦ mul_comm _ _`. The second run printed only the `#check` output, with no errors. Checks: (0) `#check @Roth.eq_sum_X_none_pow_mul_coeffNone` shows `[CommSemiring R]` only. (1) `eq_sum_rename_coeff_optionEquivLeft_mul_X_none_pow`, the re-aimed `< n` form, is proved in 2 lines by `optionEquivLeft_symm_apply` + `Polynomial.eval₂_eq_sum_range'` + `natDegree_optionEquivLeft`. (2) The exact project statement follows from (1) plus `mul_comm` under `Finset.sum_congr`. (3) The unconditional `range (degreeOf none P + 1)` form is a 1-line corollary.
- Searches: 3 WebSearch queries, LeanSearch, Lean-Finder and Loogle, all recorded above. A mathlib grep for `X none ^`, `eq_sum_X_pow`, `sum_X_pow_mul`, `optionEquivLeft_symm_apply` and `eval₂_eq_sum_range'` found no expansion lemma, only the building blocks. A grep of clean.tex found the source step at line 374. A project grep confirms the single caller (:335) and that `coeff_X_none_pow_mul_rename` and `eq_mapDomain_some_add_single` have no other users. ChatGPT MCP was n/a (not configured in this session).
