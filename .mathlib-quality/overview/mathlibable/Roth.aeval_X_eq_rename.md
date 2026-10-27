---
decl: Roth.aeval_X_eq_rename
file: Roth/Separation.lean
line: 137
kind: theorem
visibility: public
verdict: NO-mathlib-has-it
cost: n/a
junk: KEEP
rationale: The statement is exactly the applied form of mathlib's Polynomial.toMvPolynomial_eq_rename_comp (toMvPolynomial i is by definition aeval (X i)), and the project proof is literally AlgHom.congr_fun of that lemma; nothing new for mathlib, kept locally only as an aeval-spelled rewrite lemma.
action: No mathlib PR. Keep as a local rw lemma for its 5 call sites (Separation.lean:162, 207, 224; Theta.lean:437, 528) or replace each rw with `rw [← Polynomial.toMvPolynomial.eq_def, Polynomial.toMvPolynomial_eq_rename_comp]` (verified in evidence); optionally mark the docstring as the applied form of the mathlib lemma.
---

# Roth.aeval_X_eq_rename

## Inventory entry

### `theorem Roth.aeval_X_eq_rename`
- **Type**: `{R : Type*} [CommSemiring R] {σ : Type*} (i : σ) (f : Polynomial R) : Polynomial.aeval (X i : MvPolynomial σ R) f = rename (fun _ : Unit ↦ i) ((uniqueAlgEquiv R Unit).symm f)` (confirmed by `#check`, evidence (0); the section's `[Fintype τ] [DecidableEq τ]` do not appear since `τ` is unused)
- **What**: Substituting `X ↦ X_i` in a univariate polynomial `f` equals viewing `f` as a one-variable `MvPolynomial Unit` and renaming that variable to `i`.
- **How**: term proof `AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f`, using that `Polynomial.toMvPolynomial i` is definitionally `aeval (X i)`.
- **Hypotheses**: `[CommSemiring R]` only.
- **Uses from project**: `[]`
- **Used by**: `Roth.hasseDeriv_rename_mul_aeval` (Roth/Separation.lean:162, `simp [aeval_X_eq_rename, degreeOf, ...]`), the degree lemma at Roth/Separation.lean:207 (`simp [aeval_X_eq_rename, ...]`), `Roth.degreeOf_none_rename_mul_aeval` (Roth/Separation.lean:224, `rw [..., aeval_X_eq_rename]`), Roth/Theta.lean:437 (`rw [aeval_X_eq_rename, _root_.map_mul, map_rename, ...]`), Roth/Theta.lean:528 (`rw [aeval_X_eq_rename, map_eq_zero_iff _ (rename_injective _ ...)]`).
- **Visibility**: public
- **Lines**: 134–140, proof length 1 line
- **Notes**: Mathlib states the same identity at the `AlgHom` level for `Polynomial.toMvPolynomial i`; the project consistently writes `Polynomial.aeval (X i)` instead, so the mathlib lemma does not fire by `rw`/`simp` without first unfolding `toMvPolynomial` (evidence (3)).

## Junk check (Step 8)
- Used anywhere? Yes, 5 call sites in 2 files.
- Wrapper of 1–2 mathlib calls? Yes: `AlgHom.congr_fun` of `Polynomial.toMvPolynomial_eq_rename_comp`.
- Does mathlib have it? Yes, `Polynomial.toMvPolynomial_eq_rename_comp` (Mathlib/Algebra/MvPolynomial/Equiv.lean:891), modulo the defeq `toMvPolynomial i = aeval (X i)` (evidence (1), (2)).
- Too specific? No; it is a useful rewrite lemma in the project's spelling.
- Well-chosen? Acceptable: it bridges the project's `aeval (X i)` spelling to the `rename` form used for degree and `index` computations, at 5 sites; inlining would need a 2-step `rw [← Polynomial.toMvPolynomial.eq_def, Polynomial.toMvPolynomial_eq_rename_comp]` at each.
- Conclusion: `KEEP` (local convenience lemma; no mathlib action).

## Mathlibable assessment (Step 9)

Pre-filter: not private; not `_aux`; docstring not internal/auxiliary; Step 8 = KEEP; qualified name `Roth.aeval_X_eq_rename` absent from mathlib (grep: no `aeval_X_eq_rename` in `.lake/packages/mathlib/Mathlib/`). No project parent def (it is about mathlib's `aeval`/`rename`/`uniqueAlgEquiv`), so INHERITED does not apply. Full workflow below.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` compiles)
- decl `Roth.aeval_X_eq_rename`: resolved at Roth/Separation.lean:137
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`) in polynomials over `Option τ`, towards Lemma 2 of the source (`F = U(x_τ) V(x_none)`).

### Statement (Phase 1)

`Roth.aeval_X_eq_rename` is a theorem stating the following: for a commutative semiring `R`, a variable index `i ∈ σ` and a univariate polynomial `f ∈ R[X]`, the polynomial `f(X_i) ∈ R[X_σ]` obtained by substituting `X ↦ X_i` equals the image of `f`, regarded as a polynomial in the single variable indexed by `Unit`, under the variable-renaming homomorphism `R[X_Unit] → R[X_σ]`, `X_() ↦ X_i`.

Variables / typeclasses involved (Lean side):
- `R : Type*`, `[CommSemiring R]` — coefficients.
- `σ : Type*` — variable index set.
- `i : σ` — target variable.
- `f : Polynomial R` — the univariate polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `f(X_i) = rename_{() ↦ i}(f)` where `f` is viewed in `R[X_Unit] ≅ R[X]`.

Conclusion (Lean): `Polynomial.aeval (X i : MvPolynomial σ R) f = rename (fun _ : Unit ↦ i) ((uniqueAlgEquiv R Unit).symm f)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-line bookkeeping identity between two descriptions of the same algebra map; not a structure, not a main result, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | embedding univariate polynomial R[X] into multivariate polynomial ring X ↦ X_i substitution homomorphism | partial | `R[X] → R[X_1..X_n]`, `X ↦ X_i`, unique by the universal property; injective | Magma / Sage docs describe homs out of `R[x]` by image of `x`; no named theorem |
| 2 | WebSearch (general form) | polynomial ring functoriality in the set of variables map of sets induces algebra homomorphism R[X_S] → R[X_T] rename variables | partial | `S ↦ R[X_S]` is a functor (free commutative algebra); maps determined on variables | the identity is an instance of "two algebra maps agreeing on generators are equal" |
| 3 | WebSearch (aliases / mathlib) | Mathlib Polynomial.toMvPolynomial toMvPolynomial_eq_rename_comp | partial | doc pages for `MvPolynomial.rename` (rename_rename etc.) | web index lacks the lemma; confirmed locally by Phase 5 [A]/[B]/[D] |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `toMvPolynomial`, `uniqueAlgEquiv`, `rename` | no | — | source paper treats `V(x_p)` as a polynomial in one variable without comment; the identity is Lean bookkeeping |
| 6 | nLab | polynomial ring / free commutative algebra | yes | `R[X_S]` is the free commutative `R`-algebra on `S`; functorial in `S` | identity follows from freeness; no coefficient-level statement |
| 7 | nCatLab | n/a | n/a | — | not a categorical result beyond freeness covered in #6 |
| 8 | Stacks Project | n/a | n/a | — | elementary commutative algebra; nothing to compare |
| 9 | MathOverflow / Math.SE | (covered by #1/#2) | no | — | too elementary to be discussed |
| 10 | recent arXiv | arXiv 2404.16382, 2408.07499 surfaced by #1/#2 | no | — | use polynomial substitutions without stating this identity |

### Literature summary (Phase 3)

Concept identified as: the substitution embedding `R[X] → R[X_σ]`, `X ↦ X_i`, and its factorisation through the one-variable ring via functoriality of `S ↦ R[X_S]`.
Sources agree on the standard form: yes — both sides are the unique `R`-algebra map with `X ↦ X_i`.
Most general standard form: equality of algebra maps `R[X] → R[X_σ]` (the `AlgHom` statement), for any commutative semiring `R` and any `σ`.
Generality dimensions where the literature varies:
  - coefficient ring: commutative (semi)ring; `CommSemiring` is already most general for `MvPolynomial`.
  - level: elementwise identity vs equality of homomorphisms; the homomorphism form is the more general/canonical one.
Disagreement with the literature: none.

### Generality analysis — `Roth.aeval_X_eq_rename`

Literature-standard form (from Phase 3): `Polynomial.toMvPolynomial i = (rename fun _ ↦ i).comp (uniqueAlgEquiv R Unit).symm` as `AlgHom`s, `[CommSemiring R]`, any `σ`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | required by `MvPolynomial`, `Polynomial.aeval` |
| 2 | `σ : Type*` | arbitrary | arbitrary | no | already arbitrary |
| 3 | elementwise vs `AlgHom` | elementwise | `AlgHom` equality | no (as a weakening) | the `AlgHom` form is mathlib's `toMvPolynomial_eq_rename_comp`; the elementwise form is its `congr_fun` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0
Proposed restatement (if STRICTLY NARROWER): n/a
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | no hypotheses | — |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | no | both sides are already canonical maps; mathlib's proof is by `ext` (universal property) | — |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field-specific to (semi)ring? | no | already `CommSemiring` | — |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general monoid? | no | `Unit` could be any `Unique` type, but `uniqueAlgEquiv R Unit` is the mathlib lemma's own choice | — |
| 8 | Concrete-via-abstract? | no | proof is a single mathlib term; nothing concrete to abstract | — |
| 9 | False-generalisation guard | no | no generalisation proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the mathlib-idiomatic (`AlgHom`, `toMvPolynomial`) form already exists as `Polynomial.toMvPolynomial_eq_rename_comp`.

### Proof strategy — `Roth.aeval_X_eq_rename`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | already the `congr_fun` of an `ext`-proved hom equality | — |
| 5 | missing mathlib helpers | no | an applied `toMvPolynomial` lemma would only rename this one; not needed | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.aeval_X_eq_rename`

[A] Lean-Finder       "evaluating a univariate polynomial at the variable X i in MvPolynomial σ R equals renaming the Unit-indexed MvPolynomial via uniqueAlgEquiv"   hit: `Polynomial.toMvPolynomial_eq_rename_comp` (top), `MvPolynomial.rename_polynomial_aeval_X`, `MvPolynomial.aeval_toMvPolynomial`
[B] Loogle            `MvPolynomial.rename, MvPolynomial.uniqueAlgEquiv`   single hit: `Polynomial.toMvPolynomial_eq_rename_comp`
[C] LeanSearch        "aeval (X i) of a univariate polynomial equals rename of the polynomial viewed as MvPolynomial Unit"   hits: `Polynomial.toMvPolynomial` (def, `:= aeval (MvPolynomial.X i)`), `MvPolynomial.rename_polynomial_aeval_X`, `MvPolynomial.aeval_comp_toMvPolynomial`
[D] Grep mathlib src  `toMvPolynomial_eq_rename_comp`, `aeval_X_left`, `rename_eq_aeval`, `aeval_rename`, `rename_polynomial_aeval_X`   `Polynomial.toMvPolynomial_eq_rename_comp` at Mathlib/Algebra/MvPolynomial/Equiv.lean:891; `MvPolynomial.rename_eq_aeval` (`rename f = aeval (X ∘ f)`) at Rename.lean:98; `MvPolynomial.aeval_rename` at Rename.lean:250; `MvPolynomial.aeval_X_left` at Eval.lean:601; `MvPolynomial.rename_polynomial_aeval_X` at Equiv.lean:867. Only the first states our identity; the others are about `MvPolynomial.aeval`, not `Polynomial.aeval`.
[E] Name pattern      `aeval_X_eq_rename`, `toMvPolynomial_apply`   no mathlib decl with either name (grep); `Polynomial.toMvPolynomial_eq_rename_comp` is the only `toMvPolynomial`–`rename` lemma

Searched for both:
  - the user's current form (elementwise, `Polynomial.aeval (X i)` spelling): no verbatim statement.
  - the literature-standard form (`AlgHom` equality on `toMvPolynomial i`): present as `Polynomial.toMvPolynomial_eq_rename_comp`.

Concluded: found in mathlib as `Polynomial.toMvPolynomial_eq_rename_comp`; identical content at the `AlgHom` level (our form is its `congr_fun`, with `toMvPolynomial i ≡ aeval (X i)` by definition).

### Normal-form check — `Roth.aeval_X_eq_rename`

Equivalent formalisms: (a) `Polynomial.aeval (X i) f` (project); (b) `f.toMvPolynomial i` (mathlib's named embedding, defeq to (a)); (c) `rename (fun _ ↦ i) ((uniqueAlgEquiv R Unit).symm f)`.
Does mathlib already have a canonical form? yes — mathlib names the embedding `Polynomial.toMvPolynomial` and relates it to (c) by `toMvPolynomial_eq_rename_comp`.
Is our statement stated against the canonical form? It uses the unfolded spelling (a), which mathlib also uses widely (e.g. `rename_polynomial_aeval_X`); fine as a local rewrite lemma.
RHS convention respected? yes (RHS is the `rename` form used downstream).

### Syntactic generality — `Roth.aeval_X_eq_rename`

Alternative restatements attempted:
- `AlgHom` form: is the mathlib lemma.
- elementwise in `toMvPolynomial` spelling: `congr_fun` of the mathlib lemma; would not match the project's `aeval (X i)` terms syntactically.

Chosen restatement: current (elementwise, `aeval (X i)` spelling).
Justification: it rewrites directly at the 5 call sites, where the terms appear as `Polynomial.aeval (X none)`; the mathlib lemma needs a preceding `rw [← Polynomial.toMvPolynomial.eq_def]` (evidence (3)).

### Superfluous-argument audit — `Roth.aeval_X_eq_rename`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | needed by `MvPolynomial` |
| 2 | section `[Fintype τ] [DecidableEq τ]` | no | not included (τ does not occur), confirmed by `#check` (evidence (0)) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; nothing to ship to mathlib)

### Call sites — `Roth.aeval_X_eq_rename`

Internal use count: 2 outside the declaring file (Roth/Theta.lean); 3 inside Roth/Separation.lean.
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:162 | `hasseDeriv_rename_mul_aeval`: `simp [aeval_X_eq_rename, degreeOf, degrees_rename_of_injective ...]` |
| Roth/Separation.lean:207 | degreeOf lemma (Domain section): `simp [aeval_X_eq_rename, degreeOf, ...]` |
| Roth/Separation.lean:224 | `degreeOf_none_rename_mul_aeval`: `rw [..., zero_add, aeval_X_eq_rename]` |
| Roth/Theta.lean:437 | `rw [aeval_X_eq_rename, _root_.map_mul, map_rename, map_rename, index_mul ...]` |
| Roth/Theta.lean:528 | `rw [aeval_X_eq_rename, map_eq_zero_iff _ (rename_injective _ ...)]` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `aeval_X_eq_rename`?):
  - (none). Roth/Separation.lean:205, 221 use the mathlib sibling `Polynomial.toMvPolynomial_injective none` directly on `Polynomial.aeval (X none)` (works by defeq inside `map_ne_zero_iff`), confirming the two spellings are used interchangeably.

### Composition check (Phase 6)

Can `Roth.aeval_X_eq_rename` be derived from mathlib in ≤3 chained calls?

Attempt 1: `AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f`
  - Mathlib decls used: `Polynomial.toMvPolynomial_eq_rename_comp`, `AlgHom.congr_fun`
  - Result: succeeds (evidence (1)); this is the project's own proof.

Attempt 2 (as a rewrite at call sites): `rw [← Polynomial.toMvPolynomial.eq_def, Polynomial.toMvPolynomial_eq_rename_comp]` (or the same as `simp` lemmas)
  - Result: succeeds (evidence (3), (4)); a bare `rw [Polynomial.toMvPolynomial_eq_rename_comp]` fails to find the pattern (evidence (3), `fail_if_success`).

Conclusion: COMPOSABLE (it is the applied form of a single mathlib lemma)

## Verdict: `Roth.aeval_X_eq_rename`

Verdict: NO-mathlib-has-it

**Category:** NO-mathlib-has-it

**Evidence:**
- Literature search (Phase 3): standard consequence of the universal property / functoriality of `S ↦ R[X_S]`; no named result.
- Generality analysis (Phase 4): MAXIMALLY GENERAL.
- Mathlib search (Phase 5): found as `Polynomial.toMvPolynomial_eq_rename_comp` (Mathlib/Algebra/MvPolynomial/Equiv.lean:891).
- Composition check (Phase 6): COMPOSABLE; 1 mathlib term.

**Rationale:**
Mathlib defines `Polynomial.toMvPolynomial i := aeval (MvPolynomial.X i)` and proves `toMvPolynomial i = (rename fun _ : Unit ↦ i).comp (uniqueAlgEquiv R Unit).symm`. The project lemma is the pointwise version of that `AlgHom` equality, with `toMvPolynomial i` unfolded to `aeval (X i)` by definitional equality (evidence (2)). Its proof is literally `AlgHom.congr_fun` of the mathlib lemma. The other mathlib lemmas the orchestrator flagged do not state it: `MvPolynomial.aeval_X_left`, `MvPolynomial.rename_eq_aeval` (`rename f = aeval (X ∘ f)`) and `MvPolynomial.aeval_rename` all concern multivariate `aeval`, and `rename_polynomial_aeval_X` is a different identity. Still, the content is already in mathlib.

The lemma earns its place locally. The project writes the embedding as `Polynomial.aeval (X none)`, so the mathlib lemma does not fire by `rw`/`simp` without first folding `toMvPolynomial` (evidence (3)). Five call sites use it as a one-step rewrite. Keeping it costs one line, while replacing it would cost two rewrites at each site. An applied `toMvPolynomial` lemma could be added to mathlib, but it would be a trivial `congr_fun`, which mathlib does not usually add separately. It is not worth a PR.

WHY not: mathlib already has the identity as `Polynomial.toMvPolynomial_eq_rename_comp`. Our form is its `congr_fun` in the unfolded `aeval (X i)` spelling.
Belongs-elsewhere check: keep it project-local, in Roth/Separation.lean, as a rewrite lemma in the project's spelling. Nothing to upstream.
Existing mathlib decl:        `Polynomial.toMvPolynomial_eq_rename_comp`
Located at:                   `Mathlib/Algebra/MvPolynomial/Equiv.lean:891`
Our form follows in ≤1 line:
```lean
example (i : σ) (f : Polynomial R) :
    Polynomial.aeval (X i : MvPolynomial σ R) f =
      rename (fun _ : Unit ↦ i) ((uniqueAlgEquiv R Unit).symm f) :=
  AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f
```
Call sites in our project (from Phase 6.0): 5
Refactor plan (optional; KEEP is recommended): to delete the lemma, replace `aeval_X_eq_rename` in each call with `← Polynomial.toMvPolynomial.eq_def, Polynomial.toMvPolynomial_eq_rename_comp`, followed by `AlgHom.comp_apply` / `AlgEquiv.coe_toAlgHom` where needed. The sites are:
- Roth/Separation.lean:162 (`simp`)
- Roth/Separation.lean:207 (`simp`)
- Roth/Separation.lean:224 (`rw`)
- Roth/Theta.lean:437 (`rw`)
- Roth/Theta.lean:528 (`rw`)

Evidence (3) and (4) check the 2-step rewrite and the `simp` form on the bare statement only. They do not check it at the call sites.
Next action: no mathlib PR. Keep `Roth.aeval_X_eq_rename` as a local convenience lemma. Optionally extend its docstring to say it is the applied form of `Polynomial.toMvPolynomial_eq_rename_comp`.

---

## Next step

No mathlib PR. Keep the lemma locally for its 5 rewrite uses; optionally note in the docstring that it is `AlgHom.congr_fun` of mathlib's `Polynomial.toMvPolynomial_eq_rename_comp`.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.aeval_X_eq_rename/check.lean` (imports `Roth.Separation`). One `lake env lean` run (about 34 s) printed only the `#check` output, with no errors. (0) `#check @Roth.aeval_X_eq_rename` gives the signature with `[CommSemiring R]` only. (1) The statement is the term `AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp i) f`. (2) `Polynomial.aeval (X i) f = f.toMvPolynomial i` holds by `rfl`. (3) A bare `rw [Polynomial.toMvPolynomial_eq_rename_comp]` fails (`fail_if_success`), while `rw [← Polynomial.toMvPolynomial.eq_def, Polynomial.toMvPolynomial_eq_rename_comp]; rfl` closes the goal. (4) `simp [← Polynomial.toMvPolynomial.eq_def, Polynomial.toMvPolynomial_eq_rename_comp]` closes it.
- Searches: 3 WebSearch queries, recorded above. Lean-Finder returned `toMvPolynomial_eq_rename_comp` as its top hit, and Loogle on `MvPolynomial.rename, MvPolynomial.uniqueAlgEquiv` returned it as the unique hit. LeanSearch found the `toMvPolynomial` def and its sibling lemmas. A mathlib grep found `toMvPolynomial_eq_rename_comp`, `rename_eq_aeval`, `aeval_rename`, `aeval_X_left` and `rename_polynomial_aeval_X`, and no applied `toMvPolynomial` lemma. ChatGPT MCP was n/a (not configured in this session).
