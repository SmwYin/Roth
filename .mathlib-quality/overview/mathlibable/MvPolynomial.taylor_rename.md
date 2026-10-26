---
decl: MvPolynomial.taylor_rename
file: Roth/Taylor.lean
line: 164
kind: theorem
visibility: public
verdict: YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Naturality of multivariate translation in the variable set (taylor commutes with rename), the counterpart of mathlib's rename_expand / bind₁_rename for the new operator; maximally general (any f, no injectivity), core API of the YES-add-as-is MvPolynomial.taylor, used by Roth/Index.lean index_rename; proof should switch to an import-robust bind₁ form.
action: Upstream with MvPolynomial.taylor in new Mathlib/Algebra/MvPolynomial/Taylor.lean keeping the current statement and orientation, with proof simp [taylor, bind₁_rename, rename_bind₁, Function.comp_def] (evidence item 1b); locally keep (call site Roth/Index.lean:216).
---

# MvPolynomial.taylor_rename

## Inventory entry

### `theorem MvPolynomial.taylor_rename`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] {τ : Type*} (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R), (taylor α) ((rename f) P) = (rename f) ((taylor (α ∘ f)) P)`
- **What**: Translating a renamed polynomial by `α` is the same as renaming the polynomial translated by the pulled-back point `α ∘ f`: `(f_* P)(X + α) = f_*(P(X + α∘f))`.
- **How**: one `simp` call: unfold `taylor` to `aeval`, rewrite `rename` as `aeval (X ∘ f)` via mathlib's `MvPolynomial.rename_eq_aeval` (Mathlib/Algebra/MvPolynomial/Rename.lean), then `MvPolynomial.comp_aeval_apply` (Mathlib/Algebra/MvPolynomial/Eval.lean) composes the two substitutions.
- **Hypotheses**: `[CommSemiring R]` (forced by `MvPolynomial`); `f : σ → τ` arbitrary (no injectivity); no propositional hypotheses.
- **Uses from project**: `MvPolynomial.taylor`
- **Used by**: Roth/Index.lean:216 (`index_rename`, `rw [index, index, taylor_rename, support_rename_of_injective hf, ...]`).
- **Visibility**: public
- **Lines**: 161–165 (docstring 161–163), proof length 1 line
- **Notes**: Proof is import-fragile: with `Mathlib.Algebra.MvPolynomial.Monad` imported, simp normalises `aeval` to `bind₁` and the current proof fails (evidence item 1); `simp [taylor, bind₁_rename, rename_bind₁, Function.comp_def]` works (item 1b). Same phenomenon as recorded for `MvPolynomial.taylor_map`.

## Junk check (Step 8)
- Used anywhere? Yes: Roth/Index.lean:216 (`index_rename`, the variable-renaming invariance of the index requested by the source note clean.tex l.630-633).
- Wrapper of 1–2 mathlib calls? Short (`rename_eq_aeval` + `comp_aeval_apply`, or `bind₁_rename` + `rename_bind₁`), but it is stated in terms of the project operator `taylor`, and plain `simp` fails (item 2).
- Does mathlib have it? No (no `taylor` on `MvPolynomial`); analogues for other operators exist (`rename_expand`, `bind₁_rename`, `rename_bind₁`, `map_rename`).
- Too specific / inline? No: rename-compatibility is standard API for every `MvPolynomial` operator in mathlib.
- Well-chosen? Yes; the orientation (eliminating `rename` from under `taylor`) is the simp-usable direction (LHS has a general `α`).
- Conclusion: `KEEP` — action: keep; switch proof to the import-robust form when upstreaming.

## Mathlibable assessment (Step 9)

Not a glue lemma (needs `rename_eq_aeval`/`comp_aeval_apply` or `bind₁_rename`/`rename_bind₁`; plain `simp` fails, evidence item 2), not private / `_aux` / internal; qualified names `MvPolynomial.taylor_rename` and `MvPolynomial.rename_taylor` are absent from mathlib (namespace-aware grep). Full workflow run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Taylor` compiles, only linter warnings)
- decl `MvPolynomial.taylor_rename`: resolved at Roth/Taylor.lean:164
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Taylor expansion of multivariate polynomials: translation `P ↦ P(X + α)` and its coefficients as Hasse derivatives.

### Statement (Phase 1)

`MvPolynomial.taylor_rename` is a theorem stating the following:

Let `R` be a commutative semiring, `f : σ → τ` any map of variable sets, `f_* : R[X_σ] → R[X_τ]` the induced renaming `X_i ↦ X_{f(i)}`, and `τ_α P = P(X + α)` translation. For `α ∈ R^τ`, `τ_α ∘ f_* = f_* ∘ τ_{α∘f}`; i.e. translation is natural in the set of variables (translation by `α` restricted along `f` is translation by the pullback `f^*α`).

Variables / typeclasses involved (Lean side):
- `σ τ : Type*` — source and target variable sets.
- `R : Type*`, `[CommSemiring R]` — coefficients.
- `f : σ → τ` — renaming map.
- `α : τ → R` — translation vector on the target.
- `P : MvPolynomial σ R`.

Hypotheses (Lean side):
- none.

Conclusion (math): `(f_* P)(X + α) = f_*(P(X + α∘f))`.

Conclusion (Lean): `taylor α (rename f P) = rename f (taylor (α ∘ f) P)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma (naturality in the variables) of the parent definition `MvPolynomial.taylor`; not a main result.

(Note: literature width is EXHAUSTIVE regardless. BIG/SMALL is recorded for framing only.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | polynomial substitution commutes with renaming variables translation P(x+a) embedding into larger polynomial ring | partial | renaming is the algebra map `X_i ↦ X_{f(i)}`; composition of substitutions (mathlib Rename docs, `rename_rename`, `killCompl`) | no source isolates the translation case; it is the composition law of substitutions |
| 2 | WebSearch (general form) | functoriality of polynomial ring in the set of variables, map of index sets induces algebra homomorphism, naturality of substitution | partial | `I ↦ R[X_I]` is a functor (free commutative algebra on a set); substitutions compose (universal property) | commalg subwiki "Polynomial ring", mathlib FreeCommRing.map docs, arXiv math/0412287 Lemma 2.1 (naturality argument) |
| 3 | WebSearch (named-after / aliases) | "Taylor shift" multivariate polynomial change of variables relabeling variables compatibility | partial | multivariate Taylor expansion via Hasse derivatives `f(x+y)` (arXiv 1812.07020); relabeling in CAS (dimod relabel_variables) | no explicit statement of Taylor-shift/relabel compatibility; regarded as immediate |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for renam / embedded / larger polynomial ring | yes | l.621 proof of Lemma 4-2: "When P is embedded into the larger polynomial ring, its translated monomials have zero exponent in x_p, so its index is unchanged"; l.630-633 Lean note: "Prove invariance under nonzero scalars and variable renaming ... as separate lemmas" | exactly the use made in `index_rename` |
| 6 | nLab | polynomial ring as free commutative algebra / functoriality | partial | `Set → CRing_R`, `I ↦ R[I]`, left adjoint to forgetful; substitutions are Kleisli morphisms of the free-algebra monad | translation `X ↦ X + α` is a Kleisli map; naturality under `f` is the monad law (mathlib `bind₁_rename`, `rename_bind₁`) |
| 7 | nCatLab | — | n/a | — | beyond the monad/Kleisli remark of row 6 nothing categorical to add |
| 8 | Stacks Project | — | n/a | — | geometrically: for `f : σ → τ`, the projection `A^τ → A^σ` intertwines translation by `α` and by `f^*α`; no elementary polynomial-ring lemma in Stacks |
| 9 | MathOverflow / Math.SE | (results of #1, #2) | no | — | no dedicated thread; considered immediate from the universal property |
| 10 | recent arXiv (last 5 years) | (results of #2, #3) | no | — | nothing beyond the Hasse-derivative Taylor expansion papers (1812.07020) |

### Literature summary (Phase 3)

Concept identified as: naturality of the translation (Taylor shift) in the set of variables, i.e. compatibility with variable renaming / embedding into a larger polynomial ring.
Sources agree on the standard form: yes (implicitly; it is the composition law of substitutions, the monad law of the free commutative algebra).
Most general standard form: for any map of sets `f : σ → τ` and any commutative (semi)ring `R`, `(f_* P)(X + α) = f_*(P(X + α∘f))`; more generally any substitution `g` satisfies `bind g ∘ f_* = bind (g ∘ f)` (mathlib `bind₁_rename`).
Generality dimensions where the literature varies:
  - renaming map: injective embeddings (the paper's use) vs arbitrary maps; ours is arbitrary, the most general.
  - coefficients: fields to commutative semirings; ours is commutative semiring, forced by `MvPolynomial`.
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.taylor_rename`

Literature-standard form (from Phase 3): `τ_α ∘ f_* = f_* ∘ τ_{α∘f}` for any `f : σ → τ`, commutative semiring `R`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative (semi)ring | no | forced by `MvPolynomial` (parent evidence `MvPolynomial.taylor`) |
| 2 | `f : σ → τ` | arbitrary function | arbitrary map of sets | no | already arbitrary; no injectivity required (evidence item 6 instantiates with a constant map) |
| 3 | `α : τ → R` | arbitrary | vector in `R^τ` | no | already arbitrary |
| 4 | substitution | translation | arbitrary substitution | n/a | general form is mathlib's `bind₁_rename` / `rename_bind₁`; this lemma is its specialisation to the named operator |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (no hypotheses; `f` arbitrary; typeclass forced by `MvPolynomial`).
Proposed restatement: none.

Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | no | proof is already via universal property (composition of `aeval`/`bind₁`) | — |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical / bundled? | partial | bundled `AlgHom` form `(taylor α).comp (rename f) = (rename f).comp (taylor (α ∘ f))` (evidence item 5, compiles) | optional companion for `AlgHom.ext` arguments, mirroring `rename_comp_expand` / `bind₁_comp_rename`; not required |
| 7 | concrete index to general? | no | — | variable sets already arbitrary types |
| 8 | concrete-via-abstract? | no | proof uses only the generic substitution-composition law, which mathlib has abstractly (`bind₁_rename`, `rename_bind₁`); the lemma is that law specialised to the named operator, as `rename_expand` is for `expand` | — |
| 9 | false-generalisation guard | no false generalisation | the bundled form is the same statement | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the pointwise rename-compatibility lemma is exactly the shape mathlib uses for other `MvPolynomial` operators (`rename_expand`, `bind₁_rename`, `map_rename`); the bundled form is an optional companion.

### Proof strategy — `MvPolynomial.taylor_rename`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | already universal-property based | — |
| 5 | missing mathlib helpers | no | `bind₁_rename`, `rename_bind₁` (or `rename_eq_aeval`, `comp_aeval_apply`) suffice | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED (minor)
  - Proposed strategy: `simp [taylor, bind₁_rename, rename_bind₁, Function.comp_def]` (evidence item 1b).
  - Cost: CHEAP
  - Missing mathlib API (if any): none
  - Would refactoring make the proof strictly shorter / cleaner? same length, but robust: the current proof fails once `Mathlib.Algebra.MvPolynomial.Monad` is imported (simp lemma `aeval_eq_bind₁` fires first; evidence item 1). The robust proof works in that import context; the upstream file will likely have Monad in its closure.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.taylor_rename`

[A] Lean-Finder       "translation of multivariate polynomial P(X + a) commutes with rename of variables"   `MvPolynomial.rename_comp_toMvPolynomial`, `rename_expand`, `rename_comp_expand`, `rename_toMvPolynomial`, `rename_polynomial_aeval_X`; analogues for other operators only, no translation hit
[B] Loogle            `MvPolynomial.rename, MvPolynomial.aeval, MvPolynomial.C`   no results
[C] LeanSearch        "renaming variables commutes with substituting X i + C (a i) in multivariate polynomial"   `MvPolynomial.bind₁_rename`, `rename_comp_bind₁`, `rename_bind₁`, `rename_toMvPolynomial`, `bind₁_comp_rename`; building blocks only
[D] Grep mathlib src  `rename_taylor`, `taylor_rename`, `taylor` in `MvPolynomial` namespace   no hits; precedent `@[simp] rename_expand` (Algebra/MvPolynomial/Expand.lean:133, used in RingTheory/WittVector/StructurePolynomial.lean:217); building blocks `bind₁_rename` (Monad.lean:224), `rename_bind₁` (Monad.lean:209), `eval₂_rename` / `aeval_rename` (Rename.lean:239, 250), `map_rename` (Rename.lean:68)
[E] Name pattern      `MvPolynomial.taylor_rename`, `MvPolynomial.rename_taylor` (namespace-aware grep; `lean_local_search` unavailable: ripgrep not installed)   no hits

Searched for both the user's form and the literature-standard form (general substitution/renaming compatibility, which mathlib has as `bind₁_rename` / `rename_bind₁`).

Concluded: found building blocks (`MvPolynomial.bind₁_rename`, `MvPolynomial.rename_bind₁`, `MvPolynomial.rename_eq_aeval`, `MvPolynomial.comp_aeval_apply`); the translation form is not in mathlib because the operator itself is not.

### Normal-form check — `MvPolynomial.taylor_rename`

Equivalent formalisms this statement could take: `taylor α (rename f P) = rename f (taylor (α ∘ f) P)` (current); reverse `rename f (taylor (α ∘ f) P) = taylor α (rename f P)` (evidence item 4); bundled AlgHom composition (item 5).
Does mathlib already have a canonical form for this idea? Partially: `bind₁_rename : bind₁ f (rename g φ) = bind₁ (f ∘ g) φ` (operator outside, rename inside on LHS, pullback `f ∘ g` on RHS) and `rename_expand : rename f (expand p φ) = expand p (rename f φ)`.
Our statement is stated against the canonical form? yes — it follows the `bind₁_rename` pattern (operator applied to a renamed polynomial on the LHS, `α ∘ f` pullback on the RHS). The `rename_expand` orientation is not available as a good simp lemma here: its LHS would contain `taylor (α ∘ f) P`, which only matches when the translation vector is syntactically a composition.
RHS convention respected? yes (LHS has general `α`, so the lemma is usable left-to-right by `rw`/`simp`, as at Roth/Index.lean:216).

### Syntactic generality — `MvPolynomial.taylor_rename`

Alternative restatements attempted:
- current orientation with `α ∘ f`
- reversed orientation (item 4; poor simp LHS, see above)
- bundled `(taylor α).comp (rename f) = (rename f).comp (taylor (α ∘ f))` (item 5)
Chosen restatement: current.
Justification: general `α` on the LHS makes it directly rewritable at call sites (the `index_rename` use) and simp-usable; matches `bind₁_rename`.

### Superfluous-argument audit — `MvPolynomial.taylor_rename`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial` |
| 2 | `f`, `α`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (proof switch only, Phase 4.6; optional `@[simp]` tag and bundled companion)

### Call sites — `MvPolynomial.taylor_rename`

Internal use count: 1  (outside the declaring file); 0 inside Roth/Taylor.lean
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:216 | `rw [index, index, taylor_rename, support_rename_of_injective hf, Finset.coe_image,` (in `index_rename`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `MvPolynomial.taylor_rename`?):
  - (none) — `grep -rn "rename_eq_aeval\|bind₁_rename\|rename_bind₁" Roth/` finds `rename_eq_aeval` only in this proof.

K = 1: a single consumer, but it is a structural one (variable-renaming invariance of the index, explicitly requested by the source note) and the lemma is a missing-API anchor for the upstream operator rather than a project-specific wrapper, so the K = 1 "inline" signal does not apply.

### Composition check (Phase 6)

Can `MvPolynomial.taylor_rename` be derived from mathlib in ≤3 chained calls?

Attempt 1: on the unfolded statement (`taylor α = bind₁ (X + C α)` by rfl), `rw [bind₁_rename, rename_bind₁]; simp [Function.comp_def]` (evidence item 3).
  - Mathlib decls used: `MvPolynomial.bind₁_rename`, `MvPolynomial.rename_bind₁`, `rename_X`, `rename_C`, `map_add` (simp set).
  - Result: succeeds, but needs the operator `taylor` (absent from mathlib) to state the lemma, and a `simp` step.
  - Notes: plain `simp` does not prove the project form (item 2).

Attempt 2: `rename_eq_aeval` + `comp_aeval_apply` (the project proof).
  - Result: succeeds only without `Mathlib.Algebra.MvPolynomial.Monad` in scope (item 1).

Conclusion: NOT-COMPOSABLE (the operator is new; with it, this is the operator's rename-compatibility lemma, exactly as `rename_expand` is for `expand`)

## Verdict: `MvPolynomial.taylor_rename`

**Category:** YES-add-as-is

**Evidence:**
- Literature search (Phase 3): naturality of substitution in the variable set (functoriality of `I ↦ R[X_I]`, monad law of the free commutative algebra); the project source uses it in the proof of Lemma 4-2 (clean.tex l.621) and requests the renaming-invariance lemma (l.630-633).
- Generality analysis (Phase 4): MAXIMALLY GENERAL (arbitrary `f`, no hypotheses); Phase 4c: no modernisation required.
- Mathlib search (Phase 5): not in mathlib; building blocks `bind₁_rename`, `rename_bind₁`; precedent `rename_expand`.
- Composition check (Phase 6): NOT-COMPOSABLE (operator absent; plain `simp` fails).

**Rationale:**

The parent `MvPolynomial.taylor` was assessed YES-add-as-is and its planned upstream file already lists `taylor_rename`. Compatibility with `rename` is standard API for every `MvPolynomial` operator in mathlib (`rename_expand`, `bind₁_rename`, `rename_bind₁`, `map_rename`, `aeval_rename`); a multivariate Taylor file without it would force users to unfold `taylor` into `bind₁` and invoke the monad laws by hand, as the project's `index_rename` would otherwise have to. The statement has no hypotheses, `f` is an arbitrary map, and the typeclass is forced, so nothing can be weakened; the orientation already matches the `bind₁_rename` pattern and is the one usable by `rw`/`simp`.

The only pre-PR change is the proof: replace `simp [taylor, rename_eq_aeval, comp_aeval_apply]` by `simp [taylor, bind₁_rename, rename_bind₁, Function.comp_def]`, because the current proof breaks when `Mathlib.Algebra.MvPolynomial.Monad` is imported (evidence item 1), which an upstream Taylor file is likely to do.

WHY add it:
  - New content for mathlib: rename-naturality of the multivariate translation. Mathlib has the general substitution laws (`bind₁_rename`, `rename_bind₁`) but no translation operator on `MvPolynomial` and hence no such lemma; the gap is the missing multivariate counterpart of `Mathlib/Algebra/Polynomial/Taylor.lean`, whose operators each come with rename/map compatibility in the `MvPolynomial` world (`rename_expand`, `map_rename`).
  - Composes with: `support_rename_of_injective`, `coeff_rename_mapDomain` and `coeff_taylor` to transport Taylor coefficients and index/vanishing-order statements along variable embeddings (the project's `index_rename`, and the disjoint-variable product formula of Lemma 4-2).
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/Taylor.lean (new file, with the parent `MvPolynomial.taylor`).
Proposed PR title: "feat(Algebra/MvPolynomial): add multivariate Taylor shift MvPolynomial.taylor" (lemma included in the parent PR).
PR grouping: ship with `MvPolynomial.taylor`, `taylor_X`, `taylor_C`, `taylor_monomial`, `coeff_taylor`, `eval_taylor`, `taylor_taylor`, `taylor_zero`, `taylor_map` (as `map_taylor`), `degreeOf_taylor_le`, `taylor_neg_taylor`, `taylor_injective` as one PR.
Restatement to apply before the PR: none for the statement; proof change only:
```lean
theorem taylor_rename {τ : Type*} (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R) :
    taylor α (rename f P) = rename f (taylor (α ∘ f) P) := by
  simp [taylor, bind₁_rename, rename_bind₁, Function.comp_def]
```
Optional companion: `taylor_comp_rename : (taylor α).comp (rename f) = (rename f).comp (taylor (α ∘ f))` (evidence item 5), mirroring `bind₁_comp_rename`.
Pre-PR checklist before opening:
  - [ ] `/generalise MvPolynomial.taylor_rename` — confirm no easy further weakening (none expected)
  - [ ] `/cleanup Roth/Taylor.lean MvPolynomial.taylor_rename` — switch to the `bind₁` proof; decide on `@[simp]` (run the simpNF linter)
  - [ ] Pick a mathlib reviewer from recent `Mathlib/Algebra/MvPolynomial/` commits

---

## Next step

Include the lemma unchanged in the `MvPolynomial.taylor` upstream PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) with the import-robust proof `simp [taylor, bind₁_rename, rename_bind₁, Function.comp_def]`; locally the single call site Roth/Index.lean:216 needs no change.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.taylor_rename/variants.lean` (imports `Roth.Taylor` and `Mathlib.Algebra.MvPolynomial.Monad`; compiles with `lake env lean`, no errors, only an unused-simp-arg and an unreachable-tactic linter warning inside the `fail_if_success` probes): (1) with Monad imported the project proof `simp [taylor, rename_eq_aeval, comp_aeval_apply]` fails (goal left in `bind₁` form), checked by `fail_if_success (...; done)`; (1b) `simp [taylor, bind₁_rename, rename_bind₁, Function.comp_def]` proves the statement; (2) `fail_if_success (simp; done)` confirms plain `simp` cannot prove it; (3) mathlib-only composition on the unfolded form `rw [bind₁_rename, rename_bind₁]; simp [Function.comp_def]`, and (3b) the same via `change` on the project statement; (4) reversed orientation `rename_taylor'` by `.symm`; (5) bundled `taylor_comp_rename` via `AlgHom.ext`; (6) instance with a non-injective constant map, confirming no injectivity is needed.
- First compile attempt asserted the project proof works with Monad imported and failed; that failure is recorded as item (1).
- Loogle `MvPolynomial.rename, MvPolynomial.aeval, MvPolynomial.C`: no results. LeanSearch / Lean-Finder as in [A]/[C]. Mathlib grep: no `rename_taylor`/`taylor_rename`; precedent `rename_expand` (Expand.lean:133). `lean_local_search` unavailable (ripgrep not installed); replaced by grep.
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn taylor_rename Roth/` (declaration + Roth/Index.lean:216); grep of `.mathlib-quality/references/clean.tex` (l.621, l.630-633).
