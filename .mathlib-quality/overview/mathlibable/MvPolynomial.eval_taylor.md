---
decl: MvPolynomial.eval_taylor
file: Roth/Taylor.lean
line: 141
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Evaluation of the translate, eval x (P(X + α)) = P(x + α), is the multivariate counterpart of mathlib's Polynomial.taylor_eval and belongs to the YES-add-as-is MvPolynomial.taylor API, but it should ship in the verified more general aeval form (evaluation in any commutative R-algebra S) with the eval statement as a one-line corollary.
action: Upstream with MvPolynomial.taylor in new Mathlib/Algebra/MvPolynomial/Taylor.lean as aeval_taylor (proof rw [taylor_apply, comp_aeval_apply]; simp, evidence item 4) plus eval_taylor as its specialisation; locally keep (unused in project, zero call sites; no edits needed).
---

# MvPolynomial.eval_taylor

## Inventory entry

### `theorem MvPolynomial.eval_taylor`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (α x : σ → R) (P : MvPolynomial σ R), (eval x) ((taylor α) P) = (eval fun j ↦ x j + α j) P`
- **What**: Evaluating the translate `P(X + α)` at the point `x` equals evaluating `P` at the shifted point `x + α`.
- **How**: one `simp` call: unfold `taylor` to `aeval (fun j ↦ X j + C (α j))`, rewrite `aeval_def` and right-to-left with mathlib's `MvPolynomial.eval_assoc` (`eval (eval g ∘ f) p = eval g (eval₂ C f p)`), then `Function.comp_def` and `eval_X`/`eval_C`/`eval_add` close it.
- **Hypotheses**: `[CommSemiring R]` (forced by `MvPolynomial`); no propositional hypotheses.
- **Uses from project**: `MvPolynomial.taylor`
- **Used by**: unused in project (`grep -rn eval_taylor Roth/` finds only the declaration; `git log -S eval_taylor` shows it present since the initial autoformalisation commit 3cab03b, never consumed).
- **Visibility**: public
- **Lines**: 141–143 (docstring 140), proof length 1 line
- **Notes**: Name follows mathlib's `eval x (f y)` → `eval_f` convention for `MvPolynomial` (univariate mathlib uses `taylor_eval` because of `(taylor r f).eval s` dot notation). Not tagged `@[simp]`; neither is `Polynomial.taylor_eval`.

## Junk check (Step 8)
- Used anywhere? No: zero uses in the project.
- Wrapper of 1–2 mathlib calls? Close to it: the proof is one `simp` with `eval_assoc` as the key lemma; but plain `simp` and `simp [taylor]` both fail to close it (evidence items 2a, 2b), so it is not a trivial simp consequence.
- Does mathlib have it? No: mathlib has no multivariate `taylor`; the univariate `Polynomial.taylor_eval` is the template.
- Too specific / inline? No: it is the evaluation API lemma of the `taylor` operator, the exact analogue of `Polynomial.taylor_eval` (which mathlib uses in Henselian.lean, IsIntegral.lean, Resultant/Basic.lean). The parent report lists it in the planned upstream API.
- Well-chosen? Yes, though the more general `aeval` form should be the primary statement.
- Conclusion: `KEEP` — action: keep locally (harmless, no call sites); upstream with `MvPolynomial.taylor` in the generalised `aeval` form.

## Mathlibable assessment (Step 9)

Not a glue lemma (needs `eval_assoc`; unfolding alone does not close it, evidence 2b), and not private / `_aux` / internal; qualified name not in mathlib. Full workflow run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Taylor` compiles with no errors or warnings)
- decl `MvPolynomial.eval_taylor`: resolved at Roth/Taylor.lean:141
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Taylor expansion of multivariate polynomials: translation `P ↦ P(X + α)` and its coefficients as Hasse derivatives.

### Statement (Phase 1)

`MvPolynomial.eval_taylor` is a theorem stating the following:

Let `R` be a commutative semiring, `σ` a set of variables, `α, x ∈ R^σ` and `P ∈ R[X_σ]`. Let `P_α(X) = P(X + α)` be the translate of `P`. Then `P_α(x) = P(x + α)`: evaluating the translated polynomial at `x` is the same as evaluating the original at the shifted point. This is associativity of substitution: substituting `X ↦ X + α` and then `X ↦ x` is substituting `X ↦ x + α`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `R : Type*`, `[CommSemiring R]` — coefficient ring.
- `α : σ → R` — the translation vector.
- `x : σ → R` — the evaluation point.
- `P : MvPolynomial σ R` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `P(X + α)|_{X = x} = P(x + α)`.

Conclusion (Lean): `eval x (taylor α P) = eval (fun j ↦ x j + α j) P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma of the parent definition `MvPolynomial.taylor`; not a main result.

(Note: literature width is EXHAUSTIVE regardless. BIG/SMALL is recorded for framing only.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multivariate polynomial translation P(X+a) evaluated at x equals P(x+a) shift operator | yes | shift operator `E^a p(x) = p(x + a)` (MathWorld "Shift Operator", Rota–Kahaner–Odlyzko finite operator calculus); CGAL `TranslateHomogeneous` for per-variable shifts | the statement is the defining property of the shift; univariate in most sources, coordinatewise in CGAL |
| 2 | WebSearch (general form) | substitution homomorphism evaluation composition "eval" polynomial ring universal property associativity of substitution | yes | universal property of `A[X_1..X_n]`: unique hom extending `A → B` sending `X_i ↦ b_i` (ProofWiki "Polynomial Evaluation Homomorphism", arXiv 1605.04832, arXiv 2408.07499); composition of substitutions follows by uniqueness | most general form: evaluation into any `A`-algebra `B`; our statement is the case `B = A` |
| 3 | WebSearch (named-after / aliases) | "Taylor shift" multivariate polynomial evaluation composition substitution homomorphism | partial | Taylor shift `f(x) ↦ f(x + a)` as a computational primitive (arXiv 2003.12468, 0905.3993); no source isolates the evaluation identity as a lemma | folklore, immediate from substitution |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for taylor / translation / `P(X+\alpha)` | partial | l.547 Lean note "Let `P_α(X) = P(X+α)`"; l.600–621 use translated polynomials | the paper uses only the coefficient form (`coeff_taylor`), never the evaluated form; consistent with zero call sites |
| 6 | nLab | polynomial ring / free commutative algebra | yes | `R[X_σ]` is the free commutative `R`-algebra on `σ`; substitution = Kleisli composition of the polynomial monad | evaluation-after-substitution = monad associativity (mathlib: `MvPolynomial.bind₁`, `eval_assoc`, `aeval_bind₁`) |
| 7 | nCatLab | — | n/a | — | beyond the monad remark in row 6, not a categorical statement |
| 8 | Stacks Project | — | n/a | — | translation is an automorphism of affine space; Stacks has no translation-specific lemma (pure commutative algebra identity) |
| 9 | MathOverflow / Math.SE | (results of #1, #3) | no | — | no dedicated thread; regarded as immediate |
| 10 | recent arXiv (last 5 years) | (results of #2, #3) | partial | arXiv 2003.12468 (2020, bivariate Taylor shifts), 2507.05327 (2025, substitution in Lean MvPowerSeries) | no new formulation |

### Literature summary (Phase 3)

Concept identified as: evaluation of the translate / shift operator; an instance of associativity of polynomial substitution (universal property of `R[X_σ]`).
Sources agree on the standard form: yes.
Most general standard form: for any commutative `R`-algebra `S` and `x ∈ S^σ`, `P(X + α)` evaluated at `x` equals `P` evaluated at `x + α·1_S` (substitution into any algebra).
Generality dimensions where the literature varies:
  - target of evaluation: `R` itself (our form) vs. any `R`-algebra `S` (universal-property form; most general).
  - shift: by constants `α ∈ R^σ` vs. by polynomials (general substitution; that is `bind₁`/`eval_assoc`, already in mathlib).
Disagreement with the literature: none; our form is the `S = R` specialisation.

### Generality analysis — `MvPolynomial.eval_taylor`

Literature-standard form (from Phase 3): `aeval x (P(X + α)) = aeval (x + algebraMap α) P` for `x : σ → S`, `S` a commutative `R`-algebra.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | evaluation point `x : σ → R` via `eval` | point in `R^σ` | point in `S^σ`, `S` any commutative `R`-algebra, via `aeval` | yes | verified: `aeval_taylor'` compiles with proof `rw [taylor_apply, comp_aeval_apply]; simp` (evidence item 4); the current form follows by `simpa [coe_aeval_eq_eval]` (item 5) |
| 2 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | forced by `MvPolynomial σ R` (parent evidence `MvPolynomial.taylor`) |
| 3 | `α : σ → R` | constants | constants (polynomial shifts are general substitution, already `eval_assoc`) | no | widening to polynomial shifts changes the operator from `taylor` to `bind₁` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (evaluation target `R` → any commutative `R`-algebra `S`; verified compiled, evidence item 4).
Proposed restatement:

```lean
theorem aeval_taylor {S : Type*} [CommSemiring S] [Algebra R S] (α : σ → R) (x : σ → S)
    (P : MvPolynomial σ R) :
    aeval x (taylor α P) = aeval (fun j ↦ x j + algebraMap R S (α j)) P := by
  rw [taylor_apply, comp_aeval_apply]
  simp

theorem eval_taylor (α x : σ → R) (P : MvPolynomial σ R) :
    eval x (taylor α P) = eval (fun j ↦ x j + α j) P := by
  simpa [coe_aeval_eq_eval] using aeval_taylor α x P
```

Cost of restatement: CHEAP — mechanical; both proofs compile (evidence items 4, 5).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | yes (mild) | the `aeval` form is the universal-property statement (evaluation into any algebra) | composes with `aeval` API (`comp_aeval_apply`, `aeval_algebraMap_apply`, `Polynomial.aeval`-style evaluations into extensions, e.g. `ℤ`-polynomials at real points) |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | no | an `AlgHom` equation `(aeval x).comp (taylor α) = aeval (x + algebraMap ∘ α)` is equivalent; pointwise form is what `simp`/`rw` use | — |
| 7 | concrete index to general? | no | index type already general | — |
| 8 | concrete-via-abstract? | no | no named object; proof uses only substitution associativity | — |
| 9 | false-generalisation guard | no false generalisation | the `aeval` form specialises back to exactly the project statement (evidence item 5); same mathematical object | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes (it coincides with the literature weakening of Phase 4b)
  - Proposed mathlib-idiomatic restatement: `aeval_taylor` as in Phase 4b.
  - Cost: CHEAP
  - Mathlib downstream this enables: evaluation of translated integer/rational polynomials at points of an extension (`ℤ` → `ℝ`, the project's typical pattern) without first mapping coefficients; composition with `MvPolynomial.aeval` lemmas.
  - Real mathematical improvement: the identity is the universal property of substitution, which holds for evaluation into any `R`-algebra; restricting to `S = R` is arbitrary.

### Proof strategy — `MvPolynomial.eval_taylor`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | proof already goes through substitution associativity (`eval_assoc` / `comp_aeval_apply`) | — |
| 5 | missing mathlib helpers | no | `eval_assoc`, `comp_aeval_apply`, `coe_aeval_eq_eval` suffice | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (one `simp` via `eval_assoc`; in the generalised form `rw [taylor_apply, comp_aeval_apply]; simp`, mirroring `Polynomial.taylor_eval`'s `simp only [taylor_apply, eval_comp, ...]`).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.eval_taylor`

[A] Lean-Finder       "eval x (aeval (fun j => X j + C (a j)) P) = eval (x + a) P for multivariate polynomials"   `MvPolynomial.eval_add`, `MvPolynomial.polynomial_eval_eval₂`, `eval_eq_eval_mv_eval'`; no translation lemma
[B] Loogle            `MvPolynomial.eval _ (MvPolynomial.aeval _ _)`   no results; `"taylor"` names exist only under `Polynomial`
[C] LeanSearch        "evaluate multivariate polynomial after substituting X + C a equals evaluation at shifted point"   `Polynomial.algEquivAevalXAddC(_apply)` (univariate), `MvPolynomial.eval₂Hom_C_left`; no multivariate shift-evaluation lemma
[D] Grep mathlib src  `eval_taylor`, `taylor_eval`, `taylor` under `Mathlib/Algebra/MvPolynomial`   only univariate `Polynomial.taylor_eval` (Algebra/Polynomial/Taylor.lean:160), `taylor_eval_sub` (:204); nothing in `Algebra/MvPolynomial`; building blocks `MvPolynomial.eval_assoc` (Algebra/MvPolynomial/Eval.lean:303), `comp_aeval_apply`, `aeval_bind₁` (Monad.lean:255)
[E] Name pattern      `MvPolynomial.eval_taylor` (namespace-aware grep; `lean_local_search` unavailable: ripgrep not installed)   no hits

Searched for both the user's form and the literature-standard `aeval` form (and the general-substitution form `eval_assoc`/`aeval_bind₁`, which mathlib has but which is stated for arbitrary polynomial substitutions, not the `taylor` operator).

Concluded: found building blocks (`MvPolynomial.eval_assoc`, `MvPolynomial.comp_aeval_apply`, `MvPolynomial.coe_aeval_eq_eval`); the `taylor`-operator form is not in mathlib because the operator itself is not.

### Normal-form check — `MvPolynomial.eval_taylor`

Equivalent formalisms this statement could take: `eval x (taylor α P) = eval (x + α) P` (current, pointwise `fun j ↦ x j + α j`); `eval x (taylor α P) = eval (x + α) P` with Pi addition; `(eval x).comp (taylor α) = eval (x + α)` (AlgHom/RingHom form); `aeval` generalisation.
Does mathlib already have a canonical form for this idea? yes: `Polynomial.taylor_eval : (taylor r f).eval s = f.eval (s + r)` — evaluation of the translate on the LHS, evaluation at the shifted point on the RHS, shift added on the right.
Our statement is stated against the canonical form? yes (same orientation, `x + α` with the shift on the right).
RHS convention respected? yes (pushes `taylor` away, simp-normal direction).

### Syntactic generality — `MvPolynomial.eval_taylor`

Alternative restatements attempted:
- current (`fun j ↦ x j + α j`)
- Pi-addition `x + α` (needs `Pi.add_apply` unfolding at use sites; the lambda form matches `taylor_taylor` in the same file)
- `aeval` form (evidence item 4)
Chosen restatement: `aeval_taylor` in the lambda form, with `eval_taylor` kept as its `S = R` corollary.
Justification: the `aeval` form applies to evaluation in extensions; keeping `eval_taylor` as well matches mathlib practice of having both `eval` and `aeval` lemmas and keeps the `S = R` case directly rewritable.

### Superfluous-argument audit — `MvPolynomial.eval_taylor`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `α`, `x`, `P` | yes | — |
| 3 | evaluation target fixed to `R` | not needed | generalises to any commutative `R`-algebra (Phase 4b) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (add `aeval_taylor` as the primary statement; `eval_taylor` as corollary)
Superfluous arguments: NONE (but target ring generalisable)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.eval_taylor`

Internal use count: 0  (within the project, outside the declaring file; also 0 inside Roth/Taylor.lean)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| (none) | `grep -rn eval_taylor Roth/` returns only the declaration at Roth/Taylor.lean:141 |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `MvPolynomial.eval_taylor`?):
  - (none) — `grep -rn "eval_assoc\|eval .*(taylor" Roth/` finds no inline re-derivation; the project consumes translation only through `coeff_taylor` (Roth/Index.lean) and `eval_eq_sum_box`.

### Composition check (Phase 6)

Can `MvPolynomial.eval_taylor` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [taylor_apply, aeval_def, algebraMap_eq, ← eval_assoc]; simp [Function.comp_def]` (evidence item 3).
  - Mathlib decls used: `MvPolynomial.aeval_def`, `MvPolynomial.algebraMap_eq`, `MvPolynomial.eval_assoc`, simp set.
  - Result: succeeds, but needs the project's `taylor` (not in mathlib) and a rewrite chain plus `simp`; plain `simp` and `simp [taylor]` do not close it (items 2a, 2b).
  - Notes: from mathlib alone the statement cannot even be written (no multivariate `taylor`).

Attempt 2: as a corollary of the general `aeval_taylor` (items 4–5).
  - Result: succeeds; this is the proposed restatement, not a mathlib composition.

Conclusion: NOT-COMPOSABLE (the operator is new; with the operator, it is the operator's evaluation API lemma, exactly as `Polynomial.taylor_eval` is for the univariate operator)

## Verdict: `MvPolynomial.eval_taylor`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the shift operator is defined by `E^a p(x) = p(x + a)` (MathWorld, Rota et al.); the identity is associativity of substitution from the universal property of `R[X_σ]` (ProofWiki, arXiv 1605.04832), most generally stated for evaluation in any `R`-algebra.
- Generality analysis (Phase 4): STRICTLY NARROWER (evaluation target `R` → any commutative `R`-algebra `S`, verified compiled, evidence item 4); Phase 4c agrees (universal-property form).
- Mathlib search (Phase 5): not in mathlib; building blocks `eval_assoc`, `comp_aeval_apply`; template `Polynomial.taylor_eval`.
- Composition check (Phase 6): NOT-COMPOSABLE (operator absent from mathlib).

**Rationale:**

The parent `MvPolynomial.taylor` was assessed YES-add-as-is, with `eval_taylor` listed in its planned upstream file. Mathlib's univariate `Polynomial.taylor` carries exactly this lemma (`Polynomial.taylor_eval`, used in Henselian.lean, IsIntegral.lean, Resultant/Basic.lean), so the multivariate operator needs it for API parity. The statement is in mathlib's canonical orientation and is not a trivial simp consequence (plain `simp` and `simp [taylor]` fail; `eval_assoc` is needed).

The current form restricts evaluation to points of `R` itself. The identity is the universal property of substitution and holds for evaluation into any commutative `R`-algebra; that form, `aeval_taylor`, compiles with a two-step proof and specialises back to `eval_taylor` in one line. This is a single mechanical addition, not a threaded restatement, so the bucket is YES-but-generalise-first. The zero local call sites do not weigh against it: the project uses the coefficient form `coeff_taylor`, and this lemma is operator API that mathlib consumers of `MvPolynomial.taylor` would need (the univariate analogue has three mathlib consumers).

Reason for the generalisation: LITERATURE-WEAKENING (and MODERN-IDIOM, coinciding): evaluation into an arbitrary `R`-algebra is the universal-property form.
Proposed restatement:
```lean
theorem aeval_taylor {S : Type*} [CommSemiring S] [Algebra R S] (α : σ → R) (x : σ → S)
    (P : MvPolynomial σ R) :
    aeval x (taylor α P) = aeval (fun j ↦ x j + algebraMap R S (α j)) P := by
  rw [taylor_apply, comp_aeval_apply]
  simp

theorem eval_taylor (α x : σ → R) (P : MvPolynomial σ R) :
    eval x (taylor α P) = eval (fun j ↦ x j + α j) P := by
  simpa [coe_aeval_eq_eval] using aeval_taylor α x P
```
Estimated cost of regeneralisation: CHEAP (both proofs already compile in the evidence file).
Mathlib downstream this enables:
  - evaluating translated polynomials with coefficients in `R` at points of an extension `S` (e.g. integer polynomials at real or algebraic points, the Roth-type pattern) directly, without `MvPolynomial.map`;
  - composes with `MvPolynomial.comp_aeval_apply`, `aeval_algebraMap_apply` and the `aeval` evaluation API, which the `eval`-only form blocks.
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/Taylor.lean (new file, with the parent `MvPolynomial.taylor`).
PR grouping: ship with `MvPolynomial.taylor`, `taylor_X`, `taylor_C`, `taylor_monomial`, `coeff_taylor`, `taylor_taylor`, `taylor_zero`, `taylor_map`, `taylor_rename`, `degreeOf_taylor_le` in the parent's Taylor PR.
Next action: run `/generalise MvPolynomial.eval_taylor` (target: the `aeval_taylor` form above) before opening the PR; add `aeval_taylor` and derive `eval_taylor` from it.

---

## Next step

In the `MvPolynomial.taylor` upstream PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean), add `aeval_taylor` (evaluation in any commutative `R`-algebra, proof `rw [taylor_apply, comp_aeval_apply]; simp`) and state `eval_taylor` as its one-line corollary; locally no change is required (zero call sites).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.eval_taylor/variants.lean` (compiles with `lake env lean`, no errors or warnings): (1) statement re-proved by the project proof; (2a) `fail_if_success simp` confirms plain `simp` cannot prove it; (2b) `simp [taylor]` stalls at `eval₂ ((eval x).comp C) (fun i ↦ x i + α i) P = eval (fun i ↦ x i + α i) P` (checked with `fail_if_success done`), finished by identifying `(eval x).comp C = RingHom.id R`; (3) composition via `rw [taylor_apply, aeval_def, algebraMap_eq, ← eval_assoc]; simp [Function.comp_def]`; (4) generalised `aeval_taylor'` into any commutative `R`-algebra `S`, proof `rw [taylor_apply, comp_aeval_apply]; simp`; (5) project form recovered from (4) by `simpa [coe_aeval_eq_eval]`; (6) with `attribute [local simp] eval_taylor`, plain `simp` closes `eval x (taylor α (taylor β P)) = eval (fun j ↦ x j + α j + β j) P` without looping.
- An intermediate version of the evidence file had (2) as `fail_if_success simp [taylor]`, which errored because `simp [taylor]` makes progress; it was replaced by (2a)/(2b) above, and the final file compiles clean.
- Loogle `MvPolynomial.eval _ (MvPolynomial.aeval _ _)`: no results. LeanSearch / Lean-Finder: as recorded in [A]/[C]. Mathlib grep: `taylor_eval` only in `Polynomial` (Algebra/Polynomial/Taylor.lean:160, 204) and three mathlib consumers. `lean_local_search` unavailable (ripgrep not installed); replaced by grep.
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn eval_taylor Roth/` (only the declaration), `git log -S eval_taylor -- Roth` (introduced in 3cab03b, never used); grep of `.mathlib-quality/references/clean.tex` for translation (l.547, 600–621; coefficient form only).
