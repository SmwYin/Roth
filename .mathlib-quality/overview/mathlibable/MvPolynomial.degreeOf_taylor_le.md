---
decl: MvPolynomial.degreeOf_taylor_le
file: Roth/Taylor.lean
line: 170
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Translation preserves the degree in each variable; the inequality is real content (needs coeff_taylor) for the YES-add-as-is MvPolynomial.taylor, but the standard (and mathlib-univariate natDegree_taylor) form is the equality, which holds over any CommSemiring and was compiled (degreeOf_taylor in the evidence file).
action: Upstream as @[simp] degreeOf_taylor (equality, CommSemiring, proof in evidence/MvPolynomial.degreeOf_taylor_le/variants.lean) in new Mathlib/Algebra/MvPolynomial/Taylor.lean with the MvPolynomial.taylor PR, keeping degreeOf_taylor_le as the .le corollary; the call site Roth/Index.lean:229 needs no change.
---

# MvPolynomial.degreeOf_taylor_le

## Inventory entry

### `theorem MvPolynomial.degreeOf_taylor_le`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (j : σ) (P : MvPolynomial σ R), degreeOf j (taylor α P) ≤ degreeOf j P`
- **What**: Translating `P ↦ P(X + α)` does not increase the degree in any single variable `X j`.
- **How**: `degreeOf_le_iff` reduces to: every `e` in the support of `taylor α P` has `e j ≤ degreeOf j P`; by contradiction, if `degreeOf j P < e j` then the project's `coeff_taylor` gives coefficient `eval α (hasseDeriv e P)`, which vanishes by the project's `hasseDeriv_eq_zero_of_degreeOf_lt` (closed by `simp [mem_support_iff, ...]`).
- **Hypotheses**: `[CommSemiring R]` only (section variable; forced by `MvPolynomial`).
- **Uses from project**: `MvPolynomial.taylor`, `MvPolynomial.coeff_taylor`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` (and implicitly `MvPolynomial.hasseDeriv`)
- **Used by**: Roth/Index.lean:229 (`index_le_card`: `((degreeOf_taylor_le α j P).trans (hd j))`). No other use (`grep -rn degreeOf_taylor_le Roth/`).
- **Visibility**: public
- **Lines**: 168–173 (docstring 168–169), proof length 2 lines
- **Notes**: Over a commutative semiring the inequality is in fact an equality (evidence item 3c); over a ring this is a two-line consequence of `taylor_neg_taylor` (item 2).

## Junk check (Step 8)
- Used anywhere? Yes: Roth/Index.lean:229 (`index_le_card`, the bound `ind ≤ m` from §5 of the source).
- Wrapper of 1–2 mathlib calls? No: it needs the project's Taylor formula `coeff_taylor` and Hasse-derivative vanishing; plain `simp` fails (evidence item 1).
- Does mathlib have it? No (no `MvPolynomial.taylor`); the univariate analogue `Polynomial.natDegree_taylor` (equality, `@[simp]`) exists in Mathlib/Algebra/Polynomial/Taylor.lean:93.
- Too specific / inline? No: degree preservation is basic API of a Taylor shift, as in the univariate file.
- Well-chosen? The statement is weaker than the truth (equality); see verdict.
- Conclusion: `KEEP` — action: keep; add/upstream the equality `degreeOf_taylor`.

## Mathlibable assessment (Step 9)

Not a glue lemma (uses `coeff_taylor` and `hasseDeriv_eq_zero_of_degreeOf_lt`), not private / `_aux` / internal; `MvPolynomial.degreeOf_taylor_le` and `MvPolynomial.degreeOf_taylor` are absent from mathlib (namespace-aware grep). Full workflow run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Taylor` elaborates with no errors)
- decl `MvPolynomial.degreeOf_taylor_le`: resolved at Roth/Taylor.lean:170
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Taylor expansion of multivariate polynomials: translation `P ↦ P(X + α)` and its coefficients as Hasse derivatives.

### Statement (Phase 1)

`MvPolynomial.degreeOf_taylor_le` is a theorem stating the following:

Let `R` be a commutative semiring, `P ∈ R[X_σ]`, `α ∈ R^σ` and `j ∈ σ`. Then `deg_{X_j} P(X + α) ≤ deg_{X_j} P`: the translation does not raise the partial degree in any variable. (In fact equality holds.)

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variables; `R : Type*`, `[CommSemiring R]` — coefficients.
- `α : σ → R` — translation vector; `j : σ` — the variable; `P : MvPolynomial σ R`.

Hypotheses (Lean side):
- none.

Conclusion (math): `deg_{X_j}(τ_α P) ≤ deg_{X_j} P`.

Conclusion (Lean): `degreeOf j (taylor α P) ≤ degreeOf j P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma about the parent operator `MvPolynomial.taylor`; not a main result.

(Note: literature width is EXHAUSTIVE regardless. BIG/SMALL is recorded for framing only.)

### One-line check (Phase 2b)

Body line count: 2
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multivariate polynomial translation P(x+a) preserves degree in each variable | partial | invertible affine change of variables preserves degree: "at most" from the definition, equality via the inverse map (arXiv 1908.06833); leading-coefficient argument in each variable | equality is the standard statement; inequality is the first half of its proof |
| 2 | WebSearch (general form) | affine change of variables x_i -> x_i + a_i preserves multidegree Newton polytope polynomial | partial | translations preserve each partial degree and the total degree (top homogeneous part unchanged); the Newton polytope is not preserved | general form: degree (partial / total) is invariant under translation |
| 3 | WebSearch (named-after / aliases) | Taylor shift polynomial degree preserved, multivariate Hasse derivative partial degree | partial | univariate Taylor shift keeps the leading coefficient (hence degree); multivariate Taylor expansion via Hasse derivatives (arXiv 1812.07020, 1402.0643) | no explicit multivariate partial-degree statement; regarded as immediate |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "Taylor's theorem gives", "translat" | yes | l.666-667: "Taylor's theorem gives a nonzero derivative with 0 ≤ i_j ≤ r_j, of weight at most m" | uses exactly that the translate keeps `deg_{X_j} ≤ r_j` |
| 6 | nLab | polynomial ring / affine translations | no | translations are automorphisms of affine space; degree invariance not stated | automorphism viewpoint gives equality (inverse translation) |
| 7 | nCatLab | — | n/a | — | not a categorical statement |
| 8 | Stacks Project | — | n/a | — | elementary polynomial degree fact; Stacks has no partial-degree lemma for translations |
| 9 | MathOverflow / Math.SE | (results of #1-#3) | no | — | no dedicated thread; considered immediate |
| 10 | recent arXiv (last 5 years) | (results of #3) | partial | 2103.07239 (Hasse derivatives, skew polynomials) | no new form |

### Literature summary (Phase 3)

Concept identified as: invariance of (partial) degree under translation / Taylor shift.
Sources agree on the standard form: yes — degree is preserved (equality), usually via "≤ plus inverse translation" or the leading-coefficient argument.
Most general standard form: for any commutative (semi)ring `R` and `α ∈ R^σ`, `deg_{X_j} P(X + α) = deg_{X_j} P` for every `j` (also for total degree).
Generality dimensions where the literature varies:
  - conclusion strength: `≤` (proof step) vs `=` (standard statement); the strongest is `=`.
  - coefficients: fields / rings (via inverse translation) vs semirings (needs a maximal-monomial argument); `=` holds over semirings (evidence 3c).
Disagreement with the literature: the user's form is the weaker `≤`; mathlib's univariate analogue `Polynomial.natDegree_taylor` is the equality.

### Generality analysis — `MvPolynomial.degreeOf_taylor_le`

Literature-standard form (from Phase 3): `degreeOf j (taylor α P) = degreeOf j P` over any `CommSemiring R`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative (semi)ring | no | forced by `MvPolynomial` |
| 2 | `α`, `j`, `P` | arbitrary | arbitrary | no | already arbitrary |
| 3 | conclusion | `≤` | `=` | yes (stronger conclusion) | equality proved over `CommSemiring` (evidence item 3c, compiles): pick `m` maximal (pointwise) in the support among exponents with `m j = degreeOf j P`; then `hasseDeriv m P = C (coeff m P)`, so the Taylor coefficient at `m` is `coeff m P ≠ 0` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (weaker conclusion)
Number of weakening opportunities found: 1 (conclusion `≤` strengthens to `=`; verified clean with `lean_diagnostic_messages` on the evidence file)
Proposed restatement:

```lean
@[simp]
theorem degreeOf_taylor (α : σ → R) (j : σ) (P : MvPolynomial σ R) :
    degreeOf j (taylor α P) = degreeOf j P
```
(with `degreeOf_taylor_le` kept as the existing proof or as `(degreeOf_taylor α j P).le`).

Cost of restatement: CHEAP — the equality proof (≈20 lines plus a 10-line helper `coeff_taylor_of_maximal`) is already written and compiles in the evidence file; over `CommRing` it is a two-liner.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic statement |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | `degreeOf` is ℕ-valued by design | — |
| 8 | concrete-via-abstract? | no | proof uses `coeff_taylor`, specific to the operator; a general "substitution with `degreeOf j (g i) ≤ [i = j]`" lemma would give only `≤` and is not standard | — |
| 9 | false-generalisation guard | no false generalisation | the equality is the same object, strictly stronger | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the improvement is a stronger conclusion (Phase 4b), not a change of formalism.

### Proof strategy — `MvPolynomial.degreeOf_taylor_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | partial | `hasseCoeff_self : hasseCoeff m m = 1` and `coeff_taylor_of_maximal` (evidence 3a/3b) are needed for the equality; belong with the upstream `hasseDeriv`/`taylor` files | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (for the `≤` statement: `degreeOf_le_iff` + coefficient formula, 2 lines)
  - For the equality: support-maximal-monomial argument (evidence 3c), mirroring the univariate `coeff_taylor_natDegree` (leading coefficient preserved).
  - Missing mathlib API: none beyond the project's own Hasse-derivative/Taylor files being upstreamed.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.degreeOf_taylor_le`

[A] Lean-Finder       "degree in a variable of multivariate polynomial after substituting X i + C a i is unchanged"   `MonomialOrder.degree_X_add_C`, `degree_finSuccEquiv`, `degreeOf_eq_natDegree`, `degreeOf_mul_X_of_ne`; no translation lemma
[B] Loogle            `MvPolynomial.degreeOf _ (MvPolynomial.aeval _ _)`   no results
[C] LeanSearch        "degreeOf of aeval of multivariate polynomial bounded by degreeOf"   `MvPolynomial.aeval_natDegree_le` (total degree into univariate), `monomial_le_degreeOf`; building blocks only
[D] Grep mathlib src  `degreeOf_taylor`, `taylor` under Algebra/MvPolynomial and RingTheory/MvPolynomial, `degreeOf.*(aeval|bind₁|eval₂|rename)`   no taylor hits; only `degreeOf_rename_of_injective` (Degrees.lean:419); univariate precedent `Polynomial.natDegree_taylor` / `degree_taylor` (Algebra/Polynomial/Taylor.lean:93, 108)
[E] Name pattern      `MvPolynomial.degreeOf_taylor_le`, `MvPolynomial.degreeOf_taylor` (namespace-aware grep)   no hits

Searched for both the user's form (`≤`) and the literature-standard form (`=`).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); the operator `MvPolynomial.taylor` itself is absent. Building blocks: `degreeOf_le_iff`, `monomial_le_degreeOf`, `Finset.exists_le_maximal`.

### Normal-form check — `MvPolynomial.degreeOf_taylor_le`

Equivalent formalisms this statement could take: `degreeOf j (taylor α P) ≤ degreeOf j P` (current); `degreeOf j (taylor α P) = degreeOf j P` (true, stronger); `degrees (taylor α P) = degrees P` (multiset form, follows from per-variable equality).
Does mathlib already have a canonical form for this idea? Univariate yes: `@[simp] Polynomial.natDegree_taylor : natDegree (taylor r p) = natDegree p`.
Our statement is stated against the canonical form? no — the canonical form is the `@[simp]` equality with the translated polynomial on the LHS.
RHS convention respected? yes for the proposed equality (simp normal form drops `taylor`).

### Syntactic generality — `MvPolynomial.degreeOf_taylor_le`

Alternative restatements attempted:
- `≤` (current)
- `=` over `CommRing` (evidence 2)
- `=` over `CommSemiring` (evidence 3c)
Chosen restatement: `=` over `CommSemiring`, as `@[simp] degreeOf_taylor`, with `degreeOf_taylor_le` retained (or derived as `.le`).
Justification: equality rewrites at call sites (`rw [degreeOf_taylor]`) and serves `≥` uses too; the current call site uses `.trans`, which works with `(degreeOf_taylor α j P).le`.

### Superfluous-argument audit — `MvPolynomial.degreeOf_taylor_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial` |
| 2 | `α`, `j`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (target: `@[simp] degreeOf_taylor : degreeOf j (taylor α P) = degreeOf j P`)
Syntactic generality: RESTATE (equality)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.degreeOf_taylor_le`

Internal use count: 1  (outside the declaring file); 0 inside Roth/Taylor.lean
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:229 | `((degreeOf_taylor_le α j P).trans (hd j))` (in `index_le_card`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `MvPolynomial.degreeOf_taylor_le`?):
  - (none) — `grep -rn "degreeOf j (taylor\|degreeOf_taylor" Roth/` finds only the declaration and this call; `eq_sum_box_hasseDeriv` (Taylor.lean:198-207) uses the same vanishing fact `hasseDeriv_eq_zero_of_degreeOf_lt` coefficientwise, not the degree bound.

K = 1, but the lemma is standard degree API of the new operator (univariate precedent `natDegree_taylor`), so the K = 1 inline signal does not apply.

### Composition check (Phase 6)

Can `MvPolynomial.degreeOf_taylor_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: plain `simp` (evidence item 1).
  - Result: fails.

Attempt 2: `degreeOf_le_iff` + coefficient formula (the project proof).
  - Mathlib decls used: `MvPolynomial.degreeOf_le_iff`, `mem_support_iff`.
  - Result: succeeds only with the project's `coeff_taylor` (Taylor's theorem) and `hasseDeriv_eq_zero_of_degreeOf_lt`; no mathlib composition (mathlib has no multivariate translation or `degreeOf` bound for `aeval`, Loogle [B] empty).

Conclusion: NOT-COMPOSABLE

## Verdict: `MvPolynomial.degreeOf_taylor_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): translation preserves partial (and total) degree; the standard statement is the equality, `≤` being one half of its proof (arXiv 1908.06833 pattern; univariate `Polynomial.natDegree_taylor`); source use at clean.tex l.666-667.
- Generality analysis (Phase 4): STRICTLY NARROWER (conclusion `≤` vs `=`); equality verified to compile over `CommSemiring` (evidence 3c) and over `CommRing` in two lines (evidence 2).
- Mathlib search (Phase 5): not in mathlib in either form.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.taylor` is YES-add-as-is and its planned upstream file lists `degreeOf_taylor_le`. Degree preservation is basic API of a Taylor shift: mathlib's univariate file has it as the `@[simp]` equalities `natDegree_taylor` and `degree_taylor`. Shipping only the inequality in the multivariate file would be weaker than both the literature statement and the univariate precedent, and would leave users to re-prove the reverse inequality (over rings via `taylor_neg_taylor`, over semirings via a maximal-monomial argument). The equality holds over any commutative semiring and its proof is written and compiles in the evidence file, so the generalisation is mechanical and cheap.

Reason for the generalisation: LITERATURE-WEAKENING (the standard and mathlib-univariate form is the equality; ours is the `≤` half).
Proposed restatement:
```lean
@[simp]
theorem degreeOf_taylor (α : σ → R) (j : σ) (P : MvPolynomial σ R) :
    degreeOf j (taylor α P) = degreeOf j P := by
  classical
  refine le_antisymm (degreeOf_taylor_le α j P) ?_
  -- maximal-monomial argument, see evidence/MvPolynomial.degreeOf_taylor_le/variants.lean
```
(helpers: `hasseCoeff_self : hasseCoeff m m = 1`; `coeff_taylor_of_maximal : (∀ e ∈ P.support, m ≤ e → e = m) → (taylor α P).coeff m = P.coeff m`.)
Estimated cost of regeneralisation: CHEAP (already compiled).
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/Taylor.lean (new file, with `MvPolynomial.taylor`).
PR grouping: ship with `MvPolynomial.taylor`, `taylor_X`, `taylor_C`, `taylor_monomial`, `coeff_taylor`, `eval_taylor`, `taylor_taylor`, `taylor_zero`, `taylor_map`, `taylor_rename`, `taylor_injective`; `hasseCoeff_self` goes with the `MvPolynomial.hasseDeriv` file.
Optional companion: `degrees_taylor : (taylor α P).degrees = P.degrees` and `totalDegree_taylor`, mirroring `degree_taylor`.
Next action: run `/generalise MvPolynomial.degreeOf_taylor_le` (target: the equality above), add `degreeOf_taylor` to Roth/Taylor.lean, keep `degreeOf_taylor_le` (or redefine as `.le`); Roth/Index.lean:229 needs no change.
Pre-PR checklist before opening:
  - [ ] `/generalise MvPolynomial.degreeOf_taylor_le`
  - [ ] `/cleanup Roth/Taylor.lean MvPolynomial.degreeOf_taylor` — simpNF check for `@[simp]`
  - [ ] Pick a mathlib reviewer from recent `Mathlib/Algebra/MvPolynomial/` commits

---

## Next step

Add the equality `@[simp] degreeOf_taylor` (CommSemiring; proof from evidence/MvPolynomial.degreeOf_taylor_le/variants.lean) next to `degreeOf_taylor_le` in Roth/Taylor.lean and upstream it with the `MvPolynomial.taylor` PR in Mathlib/Algebra/MvPolynomial/Taylor.lean; Roth/Index.lean:229 is unaffected.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.degreeOf_taylor_le/variants.lean` (imports `Roth.Taylor`; checked with `lean_diagnostic_messages`: no errors, only an unreachable-tactic warning inside the `fail_if_success` probe and a long-line warning in a comment): (1) `fail_if_success (simp; done)` — plain simp does not prove the statement; (2) `degreeOf_taylor_ring`: equality over `CommRing` via `le_antisymm` and `taylor_neg_taylor`; (3a) `hasseCoeff_self'`; (3b) `coeff_taylor_of_maximal`; (3c) `degreeOf_taylor`: equality over any `CommSemiring`.
- Earlier iterations of the same file had small errors (missing `classical`, `exists_le_maximal` binder order, `symm` direction), fixed in place; final version compiles.
- Loogle `MvPolynomial.degreeOf _ (MvPolynomial.aeval _ _)`: no results. LeanSearch / Lean-Finder as in [A]/[C]. Mathlib grep: no `degreeOf_taylor*`, no MvPolynomial taylor; univariate `natDegree_taylor`, `degree_taylor` (Algebra/Polynomial/Taylor.lean:93, 108).
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn degreeOf_taylor_le Roth/` (declaration + Roth/Index.lean:229); `.mathlib-quality/references/clean.tex` l.666-667.
