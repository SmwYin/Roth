---
decl: Roth.degreeOf_det_hasseDeriv_le
file: Roth/CoeffNorm.lean
line: 245
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The Leibniz degree bound for a determinant of multivariate polynomials (per-variable degree of det M at most the sum of the column bounds, so card n times k for uniform bounds) is absent from mathlib, whose only det-degree lemma is the special Polynomial.natDegree_det_X_add_C_le; the Hasse-derivative entries are concrete-via-abstract (the proof uses only entry degree bounds), and the general form over any CommRing and Fintype index compiled clean with the project lemma as a one-line corollary.
action: Upstream MvPolynomial.degreeOf_det_le_sum (column bounds), a row variant and the uniform degreeOf_det_le (card n * k) to Mathlib/LinearAlgebra/Matrix/MvPolynomial.lean or Mathlib/Algebra/MvPolynomial/Degrees.lean (with a Polynomial.natDegree_det_le companion); locally keep the Roth form as the corollary used at Roth/Separation.lean:555 and :558.
---

# Roth.degreeOf_det_hasseDeriv_le

## Inventory entry

### `theorem Roth.degreeOf_det_hasseDeriv_le`
- **Type**: `{σ : Type*} {l : ℕ} (E : Fin l → Fin l → (σ →₀ ℕ)) (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) (j : σ) : degreeOf j (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det ≤ l * r j`
- **What**: If `P` has degree at most `r_j` in each variable `x_j`, then the `l × l` determinant `det(Δ_{E μ ν} P)` of Hasse derivatives of `P` has degree at most `l r_j` in `x_j`.
- **How**: `Matrix.det_apply'` expands the determinant by Leibniz; `degreeOf_sum_le` plus `Finset.sup_le` reduce to one permutation; `degreeOf_C_mul_le` drops the sign; `degreeOf_prod_le` bounds the product by the sum of entry degrees; each entry is bounded by `degreeOf_hasseDeriv_le` then `hP j`; `Finset.sum_le_sum` and `simpa` give `l * r j`.
- **Hypotheses**: `hP` (partial degree bounds on `P`).
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.degreeOf_hasseDeriv_le`
- **Used by**: Roth/Separation.lean:555 and :558 (`exists_det_eq_mul`, degree bounds `l r_j` for `U` and `l r_p` for `V`). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 245–253 (docstring 241–244), proof length 6 lines
- **Notes**: Source: clean.tex l.435 (end of the proof of Lemma 2): the determinant of an `l × l` matrix with entries of degree at most `r_j` in `x_j` has degree at most `l r_j` in `x_j`.

## Junk check (Step 8)
- Used anywhere? Yes: 2 call sites in Roth/Separation.lean (555, 558).
- Wrapper of 1–2 mathlib calls? No: a 6-line Leibniz-expansion argument (sum, sign, product, entry bounds).
- Does mathlib have it? No (Phase 5). Mathlib has the building blocks `degreeOf_sum_le`, `degreeOf_prod_le`, `degreeOf_C_mul_le`, `degreeOf_neg`, but no determinant degree bound for `MvPolynomial`; for `Polynomial` only `Polynomial.natDegree_det_X_add_C_le` (special shape `X • A + B`).
- Too specific / inline? The Hasse-derivative specialisation is too specific (the content is the general determinant bound), but the lemma itself has 2 call sites and states the paper's step.
- Well-chosen? Correct, but stated for a specific matrix; the general matrix lemma is the reusable content.
- Conclusion: `KEEP`. Action: keep locally as a corollary of a general `MvPolynomial.degreeOf_det_le` (evidence item 4); upstream the general form.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name absent from mathlib (`grep -rn "degreeOf.*det\|det.*degreeOf" .lake/packages/mathlib/Mathlib/`: no hits). Not a glue lemma (6-line proof). Full workflow below.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` elaborates with no diagnostics)
- decl `Roth.degreeOf_det_hasseDeriv_le`: resolved at Roth/CoeffNorm.lean:245
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms of integer polynomials and the estimates (Hasse derivatives, diagonal substitution, evaluation) for Lemmas 3 and 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.degreeOf_det_hasseDeriv_le` is a theorem stating the following: let `P ∈ ℤ[x_j : j ∈ σ]` have degree at most `r_j` in each variable `x_j`, and let `F = det(Δ_{E(μ,ν)} P)_{μ,ν < l}` be an `l × l` determinant whose entries are Hasse derivatives of `P`. Then `deg_{x_j} F ≤ l r_j` for every `j`. (Each entry has degree at most `r_j` in `x_j`, and every Leibniz term is a product of `l` entries.)

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variable index set.
- `l : ℕ` — matrix size; `E : Fin l → Fin l → (σ →₀ ℕ)` — derivative orders.
- `P : MvPolynomial σ ℤ` — the polynomial; `r : σ → ℕ` — degree bounds; `j : σ` — the variable.

Hypotheses (Lean side):
- `hP : ∀ j, degreeOf j P ≤ r j` — partial degree bounds.

Conclusion (math): `deg_{x_j} det(Δ_{E μ ν} P) ≤ l r_j`.

Conclusion (Lean): `degreeOf j (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det ≤ l * r j`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a degree-bound step inside Lemma 2; not a main result, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 6
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | degree of determinant of polynomial matrix at most n times max entry degree Leibniz formula | yes | `deg det A ≤ n d` if all entries have degree `≤ d`; "immediate from the definition of the determinant" (arXiv 1607.04176 §2.3); Laplace-induction proof in arXiv 2211.06732 | folklore |
| 2 | WebSearch (general form) | "degree of the determinant" polynomial matrix bounded by sum of column degrees | yes | `deg det A ≤ min(∑ row degrees, ∑ column degrees)`; finer generic bound `max_π ∑_i deg a_{i,π(i)}` (arXiv 1607.04176; 1409.5462; 2010.04662 Thm 1.2 for equality in the row-reduced case) | standard in polynomial-matrix computer algebra |
| 3 | WebSearch (named-after / aliases) | Roth theorem generalized Wronskian determinant degree at most l r_j in each variable | partial | Roth 1955 (Mathematika) Lemma 1 and expositions (arXiv 2502.00731) use per-variable degree bounds on generalized Wronskians silently | routine step, never named |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` grep "determinant", "l r_j" | yes | l.435: "Since `F` is a determinant of an `l×l` matrix whose entries are polynomials of degree at most `r_j` in `x_j` ... `F` will be of degree at most `l r_j`" | exactly the project statement, argued for a general matrix |
| 6 | nLab | determinant | no | — | nLab's determinant page treats the categorical/multilinear definition, no degree bounds |
| 7 | nCatLab | — | n/a | — | not a categorical statement (degree estimate) |
| 8 | Stacks Project | determinant / degree | no | — | Stacks treats determinants of modules/complexes, not degree bounds of polynomial matrices |
| 9 | MathOverflow / Math.SE | (results of #1, #2) | partial | the Leibniz/Laplace `n d` bound appears as a folklore answer | stated in passing |
| 10 | recent arXiv (last 5 years) | (results of #1, #2) | yes | arXiv 2010.04662 (2020), 2211.06732 (2022), 2406.01008 (2024) | same bound used as a tool |

### Literature summary (Phase 3)

Concept identified as: the Leibniz (or "column-degree") degree bound for the determinant of a polynomial matrix.
Sources agree on the standard form: yes: `deg det A ≤ ∑_k (column degree of k)` (and the same for rows), hence `≤ n d` for uniformly bounded entries; for multivariate polynomials the same holds per variable.
Most general standard form: for any commutative ring `R`, any finite index type `n`, any matrix `M ∈ Mat_n(R[x_σ])` and any variable `x_j`: `deg_{x_j} det M ≤ ∑_k c_k` whenever `deg_{x_j} M_{ik} ≤ c_k` for all `i,k` (row version symmetric).
Generality dimensions where the literature varies:
  - entries: arbitrary polynomials (literature) vs Hasse derivatives of one polynomial (project).
  - degree data: per-column/row sums (finest standard) vs uniform `n d` (project).
  - coefficient ring: any commutative ring vs `ℤ` (project).
  - index type: any finite type vs `Fin l` (project).
Disagreement with the literature: none; the project statement is a specialisation of the general bound (as the paper's own phrasing at l.435 already indicates).

### Generality analysis — `Roth.degreeOf_det_hasseDeriv_le`

Literature-standard form (from Phase 3): `[CommRing R] [Fintype n] [DecidableEq n] (M : Matrix n n (MvPolynomial σ R)) (hM : ∀ i k, degreeOf j (M i k) ≤ c k) : degreeOf j M.det ≤ ∑ k, c k`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | entries `hasseDeriv (E μ ν) P` | specific matrix | arbitrary matrix `M` | yes | proof only uses `degreeOf j (entry) ≤ r j`; verified (evidence (1), (2), (4)) |
| 2 | coefficients `ℤ` | `MvPolynomial σ ℤ` | `[CommRing R]` | yes | sign handled by `Int.units_eq_one_or` and `degreeOf_neg`; verified (evidence (1)) |
| 3 | `[CommRing R]` vs `CommSemiring` | — | `CommRing` | no | `Matrix.det` requires `CommRing` |
| 4 | index `Fin l` | `Fin l` | `[Fintype n] [DecidableEq n]` | yes | verified (evidence (1)); bound becomes `Fintype.card n * k` |
| 5 | uniform bound `l * r j` | uniform | per-column sum `∑ c k` (rows via `det_transpose`) | yes | verified (evidence (1), (3)) |
| 6 | `hP` | on `P` | on entries | yes | entry form; the `P`-form is recovered with `degreeOf_hasseDeriv_le` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 4 (rows 1, 2, 4, 5), all verified in one evidence file (`lean_diagnostic_messages`: success, no diagnostics).
Proposed restatement:

```lean
theorem MvPolynomial.degreeOf_det_le_sum {σ n R : Type*} [CommRing R] [Fintype n] [DecidableEq n]
    (M : Matrix n n (MvPolynomial σ R)) (j : σ) {c : n → ℕ}
    (hM : ∀ i k, degreeOf j (M i k) ≤ c k) : degreeOf j M.det ≤ ∑ k, c k

theorem MvPolynomial.degreeOf_det_le {σ n R : Type*} [CommRing R] [Fintype n] [DecidableEq n]
    (M : Matrix n n (MvPolynomial σ R)) (j : σ) {k : ℕ}
    (hM : ∀ i i', degreeOf j (M i i') ≤ k) : degreeOf j M.det ≤ Fintype.card n * k
```

Cost of restatement: CHEAP — the project proof with the sign step rewritten (compiled).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | hypotheses are genuine degree data |
| 2 | sequences to filters? | no | — | finite algebraic estimate |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | could alternatively be phrased via `degrees`/`Submodule` of polynomials of bounded degree, but the `degreeOf` inequality is the mathlib style (`degreeOf_prod_le`) |
| 5 | field-specific to (semi)ring? | yes | `ℤ` to any `[CommRing R]` | applies to matrices over `MvPolynomial σ R` for every ring |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | `Fin l` to `[Fintype n]` | matches `Matrix.det` API, which is stated for `Fintype n` |
| 8 | concrete-via-abstract? | yes | diagnostic: `hasseDeriv` occurs in the proof body only once, in the entry bound `degreeOf_hasseDeriv_le _ _ _` on the last line; everything else is the generic Leibniz argument. Abstract restatement above; project form is a one-line corollary (evidence (4)) | any matrix with entrywise degree bounds (Wronskians, Sylvester/resultant matrices, Vandermonde-type matrices) |
| 9 | false-generalisation guard | no false generalisation | the original statement is recovered exactly (evidence (4), `simpa using degreeOf_det_le ...`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.degreeOf_det_le_sum` and `MvPolynomial.degreeOf_det_le` as in 4b (row variant via `Matrix.det_transpose`, evidence (3)).
  - Cost: CHEAP
  - Mathlib downstream this enables: per-variable degree bounds for any determinant of multivariate polynomials (e.g. `Matrix.det_mvPolynomialX`, resultants, Wronskians); a univariate companion `Polynomial.natDegree_det_le` would generalise the special `Polynomial.natDegree_det_X_add_C_le` (whose proof repeats the same Leibniz argument).
  - Real mathematical improvement: removes the irrelevant Hasse-derivative structure; the content is the Leibniz bound.

### Proof strategy — `Roth.degreeOf_det_hasseDeriv_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | the general determinant bound itself (and a `degreeOf_zsmul`/`degreeOf_units_smul` lemma would remove the `Int.units_eq_one_or` case split) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (Leibniz expansion, same strategy as mathlib's `Polynomial.natDegree_det_X_add_C_le`)
  - Missing mathlib API (if any): the general determinant degree bound; optionally `degreeOf` of a `ℤˣ`-smul.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.degreeOf_det_hasseDeriv_le`

[A] Lean-Finder       "determinant of a matrix whose entries are multivariate polynomials of degree at most k in variable x_i has degree at most n*k in x_i"   hits: `Polynomial.natDegree_det_X_add_C_le`, `Matrix.det_mvPolynomialX_ne_zero`, `Matrix.toMvPolynomial_totalDegree_le` — none the general bound
[B] Loogle            `MvPolynomial.degreeOf, Matrix.det`   no hits
[C] LeanSearch        "degree of determinant of matrix of polynomials at most sum of degrees of entries"   hits: `Matrix.det_matrixOfPolynomials`, `Polynomial.natDegree_prod_le`, `Polynomial.degree_prod_le`, `Matrix.charmatrix_apply_natDegree_le` — building blocks / unrelated
[D] Grep mathlib src  `degreeOf.*det`, `det.*degreeOf`, `natDegree_det`, `degree_det`, `totalDegree_det`   hits: only `Polynomial.natDegree_det_X_add_C_le` (Mathlib/LinearAlgebra/Matrix/Polynomial.lean:40, special shape `X • A + B`)
[E] Name pattern      `MvPolynomial.degreeOf_sum_le`, `degreeOf_prod_le`, `degreeOf_C_mul_le` (Algebra/MvPolynomial/Degrees.lean:303, :311, :407), `degreeOf_neg` (CommRing.lean:129), `Matrix.det_apply`   hits (building blocks, all used in evidence)

Searched for both the user's form (Hasse-derivative determinant) and the literature-standard form (arbitrary matrix, column sums; univariate `natDegree` analogue).

Concluded: found building blocks (`degreeOf_sum_le`, `degreeOf_prod_le`, `degreeOf_neg`, `Matrix.det_apply`) and the special univariate case `Polynomial.natDegree_det_X_add_C_le`; the general bound is not in mathlib.

### Normal-form check — `Roth.degreeOf_det_hasseDeriv_le`

Equivalent formalisms: (a) `degreeOf j M.det ≤ ∑ k, c k` (column bounds); (b) row-bound version; (c) uniform `Fintype.card n * k`; (d) `Multiset`-valued `degrees M.det ≤ ...`.
Does mathlib already have a canonical form for this idea? No (only the special `natDegree_det_X_add_C_le`).
Is our statement stated against the canonical form? Propose (a) as the main lemma with (b), (c) as corollaries, mirroring `degreeOf_prod_le` (sum on RHS).
RHS convention respected? yes (inequality; bound on RHS).

### Syntactic generality — `Roth.degreeOf_det_hasseDeriv_le`

Alternative restatements attempted:
- (a) column-sum form (compiles; evidence (1))
- (b) row-sum form via `det_transpose` (compiles; evidence (3))
- (c) uniform form (compiles; evidence (2))
- project form from (c) (compiles; evidence (4))
Chosen restatement: (a) as the main lemma, (c) as the convenient corollary.
Justification: (c) is what callers with uniform bounds (like Roth) apply directly; (a) is the strongest Leibniz-type bound that remains a one-hypothesis statement.

### Superfluous-argument audit — `Roth.degreeOf_det_hasseDeriv_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | Hasse-derivative structure of the entries (`E`, `P`) | no | only entry degree bounds matter |
| 2 | coefficient ring `ℤ` | no | any `CommRing` |
| 3 | `Fin l` | no | any `Fintype` |
| 4 | `hP` | yes (as an entry bound) | becomes `hM` |
| 5 | `j` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (after restatement to the general matrix form)
Syntactic generality: RESTATE (forms (a)/(c))
Superfluous arguments: 3 to drop (Hasse-derivative entries, `ℤ`, `Fin l`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.degreeOf_det_hasseDeriv_le`

Internal use count: 2 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:555 (`exists_det_eq_mul`) | `exact degreeOf_det_hasseDeriv_le (fun μ ν : Fin l ↦ (D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P hr (some j)` |
| Roth/Separation.lean:558 (`exists_det_eq_mul`) | `exact degreeOf_det_hasseDeriv_le (fun μ ν : Fin l ↦ ...) P hr none` |

Inline-derivation grep (`degreeOf_prod_le`, `det_apply` over `Roth/`):
  - (none) — the Leibniz degree argument appears only in this lemma.

### Composition check (Phase 6)

Can `Roth.degreeOf_det_hasseDeriv_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Polynomial.natDegree_det_X_add_C_le`
  - Mathlib decls used: `Polynomial.natDegree_det_X_add_C_le`
  - Result: fails — univariate and only for matrices `X • A + B` with constant `A, B`.
Attempt 2: `Matrix.det_apply` then `degreeOf_sum_le`, `Finset.sup_le`, sign case split with `degreeOf_neg`, `degreeOf_prod_le`, `Finset.sum_le_sum` with `degreeOf_hasseDeriv_le`
  - Mathlib decls used: `Matrix.det_apply`, `MvPolynomial.degreeOf_sum_le`, `MvPolynomial.degreeOf_prod_le`, `MvPolynomial.degreeOf_neg`, `Int.units_eq_one_or`, `Finset.sum_le_sum`
  - Result: succeeds only as a 6–8 line proof with a case split, i.e. a real proof.
Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.degreeOf_det_hasseDeriv_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the Leibniz bound `deg det A ≤ ∑ column degrees ≤ n d` is folklore (arXiv 1607.04176 §2.3 and others); the paper (clean.tex l.435) argues it for a general matrix.
- Generality analysis (Phase 4): STRICTLY NARROWER (Hasse-derivative entries, `ℤ`, `Fin l`, uniform bound); all four weakenings compiled clean.
- Mathlib search (Phase 5): not in mathlib; only the special univariate `Polynomial.natDegree_det_X_add_C_le`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The specific gap: mathlib has per-variable degree bounds for sums, products and powers of multivariate polynomials (`MvPolynomial.degreeOf_sum_le`, `degreeOf_prod_le`, `degreeOf_pow_le` in Mathlib/Algebra/MvPolynomial/Degrees.lean) but none for determinants. Its only determinant degree bound, `Polynomial.natDegree_det_X_add_C_le` (Mathlib/LinearAlgebra/Matrix/Polynomial.lean:40), is univariate, for one special matrix shape, and repeats the Leibniz argument inline. Every argument that bounds the degree of a Wronskian, resultant or similar determinant needs the general bound.

The project form is concrete-via-abstract (Phase 4c Q8): `hasseDeriv` enters only through an entry bound on the last line of the proof. The general lemma compiles for any `[CommRing R]` and `[Fintype n]` with column bounds `∑ k, c k` (evidence (1)), with a row variant (3) and the uniform `Fintype.card n * k` corollary (2). The Roth statement is a one-line corollary (4). It is reasonable to keep the Roth form locally for its two call sites.

Reason for the generalisation: LITERATURE-WEAKENING (arbitrary matrix, any commutative ring, column sums) and MODERN-IDIOM (concrete-via-abstract; `Fintype` index as in the `Matrix.det` API).
Proposed restatement:
```lean
theorem MvPolynomial.degreeOf_det_le_sum {σ n R : Type*} [CommRing R] [Fintype n] [DecidableEq n]
    (M : Matrix n n (MvPolynomial σ R)) (j : σ) {c : n → ℕ}
    (hM : ∀ i k, degreeOf j (M i k) ≤ c k) : degreeOf j M.det ≤ ∑ k, c k

theorem MvPolynomial.degreeOf_det_le {σ n R : Type*} [CommRing R] [Fintype n] [DecidableEq n]
    (M : Matrix n n (MvPolynomial σ R)) (j : σ) {k : ℕ}
    (hM : ∀ i i', degreeOf j (M i i') ≤ k) : degreeOf j M.det ≤ Fintype.card n * k
```
Estimated cost of regeneralisation: CHEAP (compiled in evidence).
Mathlib downstream this enables:
  - Per-variable degree bounds for any determinant over `MvPolynomial` (Wronskians, resultants via Sylvester matrices, `Matrix.det_mvPolynomialX`).
  - A univariate companion `Polynomial.natDegree_det_le` (same proof) of which `Polynomial.natDegree_det_X_add_C_le` becomes a corollary.
  - The Roth Lemma 2 degree bound as a one-liner.
Proposed mathlib location: Mathlib/LinearAlgebra/Matrix/MvPolynomial.lean (already imports determinants and `MvPolynomial`), or next to `Polynomial.natDegree_det_X_add_C_le` in Mathlib/LinearAlgebra/Matrix/Polynomial.lean together with the univariate version.
PR grouping: independent of the Hasse-derivative PR (needs no project definitions); optionally add `degreeOf` of a `ℤˣ`-smul to avoid the sign case split.
Next action: run `/generalise Roth.degreeOf_det_hasseDeriv_le` targeting `MvPolynomial.degreeOf_det_le_sum` / `degreeOf_det_le`, then `/cleanup` and `/pre-submit`.

---

## Next step

Upstream `MvPolynomial.degreeOf_det_le_sum` and `MvPolynomial.degreeOf_det_le` (plus the row variant and a univariate `Polynomial.natDegree_det_le` companion). Locally, restate `Roth.degreeOf_det_hasseDeriv_le` as the one-line corollary (evidence (4)). The call sites Roth/Separation.lean:555 and :558 stay as they are.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.degreeOf_det_hasseDeriv_le/general.lean` (imports `Roth.CoeffNorm`). Final `lean_diagnostic_messages`: success, no diagnostics. It contains:
  - (1) `degreeOf_det_le_sum`: column-sum bound over any `[CommRing R]`, `[Fintype n]`.
  - (2) `degreeOf_det_le`: uniform `Fintype.card n * k` corollary.
  - (3) `degreeOf_det_le_sum_rows`: row-sum version via `det_transpose`.
  - (4) the project statement recovered as an `example` from (2) and `degreeOf_hasseDeriv_le`.
- Iterations: the first check of (4) failed because `simpa` unfolded `Matrix.of`. Passing the matrix explicitly fixed it, and a module docstring was added to silence the header linter. Both checks ran via the LSP, with no cold `lake env lean` run.
- Loogle (1), LeanSearch (1), Lean-Finder (1) queries and mathlib greps as recorded in the search-status block.
- WebSearch: 3 queries (literature table rows 1–3). ChatGPT MCP: n/a (not configured). Local refs: clean.tex l.435.
- Project greps: `grep -rn degreeOf_det_hasseDeriv_le Roth/` (call sites); inline-derivation grep for `degreeOf_prod_le` / `det_apply`.
