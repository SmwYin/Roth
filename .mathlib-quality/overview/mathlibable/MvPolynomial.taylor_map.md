---
decl: MvPolynomial.taylor_map
file: Roth/Taylor.lean
line: 157
kind: theorem
visibility: public
verdict: YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Naturality of multivariate translation in the coefficient ring, the exact counterpart of mathlib's simp lemma Polynomial.map_taylor (consumed in RingTheory/Polynomial/Resultant/Basic.lean); maximally general and core API of the YES-add-as-is MvPolynomial.taylor, but unused locally and should ship reoriented as @[simp] map_taylor with an import-robust proof.
action: Upstream with MvPolynomial.taylor in new Mathlib/Algebra/MvPolynomial/Taylor.lean as @[simp] map_taylor (map f (taylor α P) = taylor (f ∘ α) (map f P), proof simp [taylor, map_bind₁]; evidence items 1b and 4); locally keep (no call sites; source note clean.tex l.154 asks for coefficient-map compatibility).
---

# MvPolynomial.taylor_map

## Inventory entry

### `theorem MvPolynomial.taylor_map`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] {S : Type*} [CommSemiring S] (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R), (taylor fun j ↦ f (α j)) (map f P) = map f ((taylor α) P)`
- **What**: Translation commutes with change of coefficient ring: applying `f` to the coefficients of `P(X + α)` gives `(f P)(X + f(α))`.
- **How**: one `simp` call: unfold `taylor` to `aeval`, `aeval_def` to `eval₂`, then mathlib's `MvPolynomial.map_eval₂` (Mathlib/Algebra/MvPolynomial/Eval.lean) and `Function.comp_def` identify the two substitutions.
- **Hypotheses**: `[CommSemiring R]`, `[CommSemiring S]` (forced by `MvPolynomial`); no propositional hypotheses.
- **Uses from project**: `MvPolynomial.taylor`
- **Used by**: unused in project (`grep -rn taylor_map Roth/` finds only the declaration at Roth/Taylor.lean:157).
- **Visibility**: public
- **Lines**: 155–159 (docstring 155–156), proof length 1 line
- **Notes**: Orientation is opposite to mathlib's univariate `Polynomial.map_taylor : (p.taylor r).map f = (p.map f).taylor (f r)` (`@[simp]`, Mathlib/Algebra/Polynomial/Taylor.lean:120). The proof is import-fragile: with `Mathlib.Algebra.MvPolynomial.Monad` imported, simp normalises `aeval` to `bind₁` and the current proof fails (evidence item 1); `simp [taylor, map_bind₁]` works (item 1b).

## Junk check (Step 8)
- Used anywhere? No call sites in `Roth/`. The source note (clean.tex l.154, "prove compatibility with coefficient maps before passing between Z, Q and R") motivates it; the passage between coefficient rings currently goes through Hasse derivatives rather than translation.
- Wrapper of 1–2 mathlib calls? Short (`map_eval₂` or `map_bind₁` plus simp), but the statement needs the project operator `taylor`, and plain `simp` fails (item 2).
- Does mathlib have it? No multivariate version; the univariate `Polynomial.map_taylor` is the template.
- Too specific / inline? No: naturality in the coefficient ring is standard API for any polynomial operator (mathlib has `map_rename`, `map_bind₁`, `map_expand`, `Polynomial.map_taylor`).
- Well-chosen? Mathematically yes; orientation and name should match `Polynomial.map_taylor`.
- Conclusion: `KEEP` — action: keep (harmless API lemma, unused locally); upstream with `MvPolynomial.taylor` as `@[simp] map_taylor`.

## Mathlibable assessment (Step 9)

Not a glue lemma (needs `map_eval₂`/`map_bind₁`; plain `simp` fails, evidence item 2), not private / `_aux` / internal; qualified name `MvPolynomial.taylor_map` (and `MvPolynomial.map_taylor`) absent from mathlib (namespace-aware grep: `map_taylor` occurs only as `Polynomial.map_taylor`). Full workflow run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Taylor` compiles, only linter warnings)
- decl `MvPolynomial.taylor_map`: resolved at Roth/Taylor.lean:157
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Taylor expansion of multivariate polynomials: translation `P ↦ P(X + α)` and its coefficients as Hasse derivatives.

### Statement (Phase 1)

`MvPolynomial.taylor_map` is a theorem stating the following:

Let `f : R → S` be a homomorphism of commutative semirings, `σ` a set of variables, `α ∈ R^σ`, and write `f_*` for the induced map `R[X_σ] → S[X_σ]` on coefficients and `τ_α P = P(X + α)` for translation. Then `τ_{f(α)} ∘ f_* = f_* ∘ τ_α`, i.e. `(f_* P)(X + f(α)) = f_*(P(X + α))`. Translation is natural in the coefficient ring.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `R S : Type*`, `[CommSemiring R] [CommSemiring S]` — coefficient rings.
- `f : R →+* S` — the change of coefficients.
- `α : σ → R` — translation vector.
- `P : MvPolynomial σ R`.

Hypotheses (Lean side):
- none.

Conclusion (math): `f_*(τ_α P) = τ_{f∘α}(f_* P)`.

Conclusion (Lean): `taylor (fun j ↦ f (α j)) (map f P) = map f (taylor α P)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma (naturality) of the parent definition `MvPolynomial.taylor`; not a main result.

(Note: literature width is EXHAUSTIVE regardless. BIG/SMALL is recorded for framing only.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | polynomial translation P(x+a) commutes with ring homomorphism reduction of coefficients | partial | `φ(P(x+a)) = P^φ(x + φ(a))`, derived from the universal property of `R[x]` (substitution principle) | UCSD Math 100B notes l_8 (Lemma 8.3, universal property), Harvard Math 371 lecture 8; no source isolates the identity, treated as immediate |
| 2 | WebSearch (general form) | base change of polynomial ring, naturality of substitution homomorphism, coefficient map commutes with evaluation | partial | `R[X_σ] ⊗_R S ≅ S[X_σ]` and substitution is natural under base change; most general form: any substitution `X ↦ g` commutes with `f_*` after mapping `g` | MIT 18.702 summary (substitution principle), Conrad "Tensor products II", Gathmann Comm. Alg. ch. 5; mathlib form: `map_bind₁`, `map_eval₂` |
| 3 | WebSearch (named-after / aliases) | "Taylor shift" polynomial modular reduction homomorphic image shift commutes | partial | Taylor shift `p(x) ↦ p(x + x0)` (ResearchGate "Polynomial Taylor Shifting", AtCoder ABC215 editorial); modular algorithms compute it mod p, which presupposes the naturality | alias "Taylor shift" = mathlib's name; no explicit statement |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for compatib / coefficient map / translat | yes | l.154 "prove compatibility with coefficient maps before passing between Z, Q and R"; l.547 `P_α(X)=P(X+α)` | the paper's Lean note requests exactly this kind of compatibility (stated for Hasse derivatives) |
| 6 | nLab | polynomial functor / base change / naturality | partial | `R ↦ R[X_σ]` is a functor (free commutative algebra, left adjoint), and substitution morphisms are natural transformations | translation by `α` is natural once `α` is transported along `f`; no specific entry |
| 7 | nCatLab | — | n/a | — | not a categorical statement beyond the naturality remark in row 6 |
| 8 | Stacks Project | — | n/a | — | geometrically: the translation `A^n_R → A^n_R` base-changes to translation by `f(α)` on `A^n_S`; Stacks has no elementary polynomial-ring lemma for this |
| 9 | MathOverflow / Math.SE | (results of #1, #3) | no | — | no dedicated thread; regarded as immediate from the universal property |
| 10 | recent arXiv (last 5 years) | (results of #2) | no | — | nothing new; arXiv 2512.05750 (formalising polynomial laws) uses base-change naturality in Lean but not for translations |

### Literature summary (Phase 3)

Concept identified as: naturality (base-change compatibility) of the translation / Taylor shift in the coefficient ring.
Sources agree on the standard form: yes (implicitly; it is the universal property of polynomial rings applied to `X ↦ X + α`).
Most general standard form: for any homomorphism of commutative (semi)rings `f : R → S`, `f_*(P(X + α)) = (f_* P)(X + f(α))`; more generally any substitution `X ↦ g` commutes with `f_*` after transporting `g` (mathlib: `map_bind₁`).
Generality dimensions where the literature varies:
  - coefficient rings: fields / rings to commutative semirings; ours is commutative semiring, the most general for `MvPolynomial`.
  - substitution: translation only vs. arbitrary substitution (the latter is in mathlib as `map_bind₁`, `map_aeval`).
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.taylor_map`

Literature-standard form (from Phase 3): `f_*(τ_α P) = τ_{f∘α}(f_* P)` for `f : R →+* S`, commutative semirings.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]`, `[CommSemiring S]` | commutative semirings | commutative (semi)rings | no | forced by `MvPolynomial σ R` / `MvPolynomial σ S` (parent evidence `MvPolynomial.taylor`) |
| 2 | `f : R →+* S` | ring hom | ring hom | no | `MvPolynomial.map` takes a `RingHom`; a weaker map does not induce a ring map on polynomials |
| 3 | `α : σ → R` | arbitrary | vector in `R^σ` | no | already arbitrary |
| 4 | substitution | translation | arbitrary substitution | n/a | the general-substitution form is mathlib's `map_bind₁`; this lemma is its specialisation to the named operator, which is the point of the API lemma |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (no hypotheses; typeclasses forced by `MvPolynomial`; `f` is the minimal data `map` accepts).
Proposed restatement: none for generality (orientation/name change is recorded in Phase 5.5; it is the `.symm` of the current statement, evidence item 4).

Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | no | proof already via universal property (`map_eval₂` / `map_bind₁`) | — |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical / bundled? | partial | bundled ring-hom form `(map f).comp (taylor α).toRingHom = (taylor (f ∘ α)).toRingHom.comp (map f)` (evidence item 6, compiles) | optional companion for `RingHom.ext` arguments; mathlib's univariate operator has only the pointwise `map_taylor`, so not required |
| 7 | concrete index to general? | no | — | — |
| 8 | concrete-via-abstract? | no | proof uses only the generic naturality of substitution (`map_bind₁`), which mathlib already has in the abstract form; the lemma is its specialisation to the named operator, exactly as `Polynomial.map_taylor` is | — |
| 9 | false-generalisation guard | no false generalisation | the bundled form and the reoriented form are the same mathematical statement | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the pointwise naturality lemma is precisely the shape mathlib uses for the univariate operator (`Polynomial.map_taylor`); the bundled form is an optional one-line companion, not an organisational improvement.

### Proof strategy — `MvPolynomial.taylor_map`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | already universal-property based | — |
| 5 | missing mathlib helpers | no | `map_bind₁` / `map_eval₂` suffice | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED (minor)
  - Proposed strategy: `simp [taylor, map_bind₁]` (evidence item 1b) instead of `simp [taylor, aeval_def, map_eval₂, Function.comp_def]`.
  - Cost: CHEAP
  - Missing mathlib API (if any): none
  - Would refactoring make the proof strictly shorter / cleaner? yes — shorter, and robust: the current proof fails once `Mathlib.Algebra.MvPolynomial.Monad` is imported (its simp lemma `aeval_eq_bind₁` rewrites `aeval` to `bind₁` first; evidence item 1). In mathlib, where Monad will typically be in the import closure of a Taylor file, this matters.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.taylor_map`

[A] Lean-Finder       "applying a ring hom to the coefficients commutes with translating a multivariate polynomial P(X + a)"   `Polynomial.map_taylor` (univariate), `Polynomial.map_expand`, `Polynomial.taylor_apply`, `Polynomial.algEquivAevalXAddC_apply`, `Polynomial.taylorAlgHom_apply`; no multivariate hit
[B] Loogle            `MvPolynomial.map _ (MvPolynomial.aeval _ _)`   no results
[C] LeanSearch        "map coefficients of multivariate polynomial commutes with substitution X + C a"   `MvPolynomial.map_bind₁`, `MvPolynomial.eval₂_map_comp_C`, `MvPolynomial.map_eval`, `MvPolynomial.eval₂Hom_C_left`; building blocks only
[D] Grep mathlib src  `map_taylor`, `taylor_map`, `taylor` in files with `namespace MvPolynomial`   `map_taylor` only at Algebra/Polynomial/Taylor.lean:120 (univariate, `@[simp]`) with consumer RingTheory/Polynomial/Resultant/Basic.lean:783, 793; no `taylor` in any `MvPolynomial` namespace; building blocks `MvPolynomial.map_bind₁` (Monad.lean:241), `map_aeval` (Eval.lean:618), `eval₂_map` (Eval.lean:441), `map_rename` (Rename.lean:68)
[E] Name pattern      `MvPolynomial.taylor_map`, `MvPolynomial.map_taylor` (namespace-aware grep; `lean_local_search` unavailable: ripgrep not installed)   no hits

Searched for both the user's form and the literature-standard form (general substitution naturality, which mathlib has as `map_bind₁`).

Concluded: found building blocks (`MvPolynomial.map_bind₁`, `MvPolynomial.map_eval₂`, `MvPolynomial.map_aeval`); the translation form is not in mathlib because the operator itself is not.

### Normal-form check — `MvPolynomial.taylor_map`

Equivalent formalisms this statement could take: `taylor (fun j ↦ f (α j)) (map f P) = map f (taylor α P)` (current); `map f (taylor α P) = taylor (f ∘ α) (map f P)` (mathlib orientation); bundled ring-hom composition (item 6).
Does mathlib already have a canonical form for this idea? yes: `Polynomial.map_taylor : (p.taylor r).map f = (p.map f).taylor (f r)`, `@[simp]`, `map` on the outside on the LHS (same convention as `map_bind₁`, `map_expand`, `map_rename`: push `map` inward).
Our statement is stated against the canonical form? no — it is the reverse orientation, so it cannot serve as the simp lemma that pushes `map` inward, and the name `taylor_map` breaks the `map_<op>` naming pattern.
RHS convention respected? no (current RHS has `map` outermost); fix by reorienting.

### Syntactic generality — `MvPolynomial.taylor_map`

Alternative restatements attempted:
- current orientation with lambda `fun j ↦ f (α j)`
- reoriented `map f (taylor α P) = taylor (f ∘ α) (map f P)` (evidence item 4, the term `(taylor_map f α P).symm`, so definitionally the same; with `@[simp]` it closes the current form by `simp [Function.comp_def]`, item 5)
- bundled `(map f).comp (taylor α).toRingHom = (taylor (f ∘ α)).toRingHom.comp (map f)` (item 6)
Chosen restatement: reoriented `@[simp] map_taylor` with `f ∘ α`.
Justification: matches `Polynomial.map_taylor`, `map_bind₁`, `map_rename`; usable as a simp lemma pushing coefficient maps inward, which is how such lemmas are consumed (e.g. `rw [← map_taylor]` in Resultant/Basic.lean).

### Superfluous-argument audit — `MvPolynomial.taylor_map`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]`, `[CommSemiring S]` | yes | required by `MvPolynomial` |
| 2 | `f`, `α`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (reorient to `map f (taylor α P) = taylor (f ∘ α) (map f P)`, `@[simp]`, rename `map_taylor`)
Syntactic generality: RESTATE (as above; `f ∘ α` instead of the lambda)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP (cosmetic: `.symm` of the current statement)

### Call sites — `MvPolynomial.taylor_map`

Internal use count: 0  (outside the declaring file); 0 inside Roth/Taylor.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| (none) | `grep -rn taylor_map Roth/` returns only the declaration, Roth/Taylor.lean:157 |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `MvPolynomial.taylor_map`?):
  - (none) — `grep -rn "map_eval₂\|map_bind₁" Roth/` finds `map_eval₂` only in this proof; Roth/Index.lean's coefficient-ring passages go through Hasse derivatives, not translation.

K = 0 with no inline re-derivation: the lemma is unused locally. It is kept for API completeness (it is the multivariate analogue of a mathlib simp lemma that mathlib itself consumes), which is the API-gap justification required for a YES on an unused lemma.

### Composition check (Phase 6)

Can `MvPolynomial.taylor_map` be derived from mathlib in ≤3 chained calls?

Attempt 1: on the unfolded statement (`taylor α = bind₁ (X + C α)` by rfl, evidence item 3), `rw [map_bind₁]; simp`.
  - Mathlib decls used: `MvPolynomial.map_bind₁`, `map_add`, `map_X`, `map_C` (simp set).
  - Result: succeeds, but it is `rw` + `simp`, and needs the operator `taylor` (absent from mathlib) to state the lemma.
  - Notes: plain `simp` does not prove the project form (item 2).

Attempt 2: `map_eval₂` route (the project proof).
  - Result: succeeds only without `Mathlib.Algebra.MvPolynomial.Monad` in scope (item 1).

Conclusion: NOT-COMPOSABLE (the operator is new; with it, this is the operator's naturality lemma, exactly as `Polynomial.map_taylor` is for the univariate operator)

## Verdict: `MvPolynomial.taylor_map`

**Category:** YES-add-as-is

**Evidence:**
- Literature search (Phase 3): naturality of substitution under change of coefficients (universal property of polynomial rings: UCSD Lemma 8.3, MIT 18.702 substitution principle; base change `R[X_σ] ⊗ S ≅ S[X_σ]`); project source asks for coefficient-map compatibility (clean.tex l.154).
- Generality analysis (Phase 4): MAXIMALLY GENERAL; Phase 4c: no modernisation required.
- Mathlib search (Phase 5): not in mathlib; template `Polynomial.map_taylor`; building blocks `map_bind₁`, `map_eval₂`.
- Composition check (Phase 6): NOT-COMPOSABLE (operator absent; plain `simp` fails).

**Rationale:**

The parent `MvPolynomial.taylor` was assessed YES-add-as-is, with `taylor_map` already in its planned upstream file. Compatibility with coefficient maps is standard API for every polynomial operator in mathlib (`map_rename`, `map_bind₁`, `map_expand`, and for the univariate shift `Polynomial.map_taylor`, a simp lemma consumed in RingTheory/Polynomial/Resultant/Basic.lean:783 and 793 to move between coefficient rings). A multivariate Taylor file without it would force users to unfold `taylor` and invoke `map_bind₁` by hand. The statement has no hypotheses and its typeclasses are forced by `MvPolynomial`, so there is nothing to weaken.

Before shipping, apply two cosmetic changes, neither a generalisation: (a) reorient and rename to `@[simp] map_taylor : map f (taylor α P) = taylor (f ∘ α) (map f P)`, matching `Polynomial.map_taylor` and simp-normal direction (evidence items 4–5); (b) use the robust proof `simp [taylor, map_bind₁]` (item 1b), since the current proof breaks when the Monad file is imported (item 1). The lemma is unused in the project (K = 0); this does not count against inclusion because it is a missing-API anchor rather than project-specific glue.

WHY add it:
  - New content for mathlib: naturality of the multivariate translation in the coefficient ring. Mathlib has the univariate `Polynomial.map_taylor` and the general substitution naturality `MvPolynomial.map_bind₁`, but no translation operator on `MvPolynomial` and hence no such lemma; the gap is the missing multivariate counterpart of `Mathlib/Algebra/Polynomial/Taylor.lean`.
  - Composes with: `map_taylor` as a simp lemma lets `coeff_taylor` / `hasseDeriv` statements be transported between `ℤ`, `ℚ`, `ℝ` (the project's stated need, clean.tex l.154), e.g. combined with a `map_hasseDeriv` lemma it gives `coeff_taylor` over `S` from `coeff_taylor` over `R`.
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/Taylor.lean (new file, with the parent `MvPolynomial.taylor`).
Proposed PR title: "feat(Algebra/MvPolynomial): add multivariate Taylor shift MvPolynomial.taylor" (lemma included in the parent PR).
PR grouping: ship with `MvPolynomial.taylor`, `taylor_X`, `taylor_C`, `taylor_monomial`, `coeff_taylor`, `eval_taylor`, `taylor_taylor`, `taylor_zero`, `taylor_rename`, `degreeOf_taylor_le`, `taylor_neg_taylor`, `taylor_injective` as one PR.
Restatement to apply before the PR (from Phase 5.5 and 4.6):
```lean
@[simp]
theorem map_taylor {S : Type*} [CommSemiring S] (f : R →+* S) (α : σ → R)
    (P : MvPolynomial σ R) : map f (taylor α P) = taylor (f ∘ α) (map f P) := by
  simp [taylor, map_bind₁]
```
Pre-PR checklist before opening:
  - [ ] `/generalise MvPolynomial.taylor_map` — confirm no easy further weakening (none expected)
  - [ ] `/cleanup Roth/Taylor.lean MvPolynomial.taylor_map` — reorient, rename to `map_taylor`, switch to the `map_bind₁` proof
  - [ ] Pick a mathlib reviewer from recent `Mathlib/Algebra/MvPolynomial/` and `Mathlib/Algebra/Polynomial/Taylor.lean` commits

---

## Next step

Include the lemma in the `MvPolynomial.taylor` upstream PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) as `@[simp] map_taylor : map f (taylor α P) = taylor (f ∘ α) (map f P)` proved by `simp [taylor, map_bind₁]`; locally no call sites need changing (there are none), and the reorientation/rename can be applied in Roth/Taylor.lean at any time.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.taylor_map/variants.lean` (imports `Roth.Taylor` and `Mathlib.Algebra.MvPolynomial.Monad`; compiles with `lake env lean`, no errors, only unused-simp-arg / unreachable-tactic linter warnings inside the `fail_if_success` probes): (1) with Monad imported, the project proof `simp [taylor, aeval_def, map_eval₂, Function.comp_def]` fails to close the goal (left with a `bind₁` goal), checked by `fail_if_success (...; done)`; (1b) `simp [taylor, map_bind₁]` proves the project statement; (2) `fail_if_success (simp; done)` confirms plain `simp` cannot prove it; (3) mathlib-only composition on the unfolded form, `rw [map_bind₁]; simp`, plus `taylor α P = bind₁ (fun j ↦ X j + C (α j)) P := rfl`; (4) reoriented `@[simp] map_taylor' : map f (taylor α P) = taylor (f ∘ α) (map f P)` by the term `(taylor_map f α P).symm`; (5) with (4) in the simp set, `simp [Function.comp_def]` closes the project form; (6) bundled companion `map_comp_taylor` via `RingHom.ext`.
- First compile failed because `bind₁` needs `Mathlib.Algebra.MvPolynomial.Monad`; adding that import revealed the fragility recorded in item (1).
- Loogle `MvPolynomial.map _ (MvPolynomial.aeval _ _)`: no results. LeanSearch / Lean-Finder: as recorded in [A]/[C]. Mathlib grep: `map_taylor` only univariate (Algebra/Polynomial/Taylor.lean:120) with consumer RingTheory/Polynomial/Resultant/Basic.lean:783, 793. `lean_local_search` unavailable (ripgrep not installed); replaced by grep.
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn taylor_map Roth/` (declaration only); grep of `.mathlib-quality/references/clean.tex` (l.154, l.547).
