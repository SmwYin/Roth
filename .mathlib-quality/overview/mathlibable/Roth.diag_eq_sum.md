---
decl: Roth.diag_eq_sum
file: Roth/CoeffNorm.lean
line: 164
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Re-aimed at the mathlib term aeval (fun _ ↦ X), the identity aeval (fun _ ↦ X) P = ∑ k ∈ P.support, monomial k.degree (coeff k P) is absent from mathlib (loogle/leansearch/leanfinder/grep empty), is not a 1-3 call composition, and holds verbatim over any CommSemiring R (and in weighted form X_i ↦ X ^ w i with Finsupp.weight w), all compiled in evidence; upstream the general-R form plus the coefficient corollary.
action: Upstream to Mathlib/RingTheory/Polynomial/Basic.lean (next to MvPolynomial.aeval_natDegree_le) as MvPolynomial.aeval_X_pow_eq_sum (weighted) with corollaries aeval_X_eq_sum and coeff_aeval_X over [CommSemiring R]; locally restate diag_eq_sum over CommSemiring R (proof unchanged), call sites Roth/CoeffNorm.lean:176 and :185 unaffected.
---

# Roth.diag_eq_sum

## Inventory entry

### `theorem Roth.diag_eq_sum`
- **Type**: `{σ : Type*} (P : MvPolynomial σ ℤ) : diag P = ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k)`
- **What**: The diagonal substitution `P(x, …, x)` sends each monomial `a_k X^k` to `a_k x^{|k|}`, so `diag P = ∑_k a_k x^{|k|}`.
- **How**: `rw [diag, aeval_def, eval₂_eq]`, then `simp_rw` with `Finset.prod_pow_eq_pow_sum`, `← Finsupp.degree_apply`, `Polynomial.algebraMap_eq`, `Polynomial.C_mul_X_pow_eq_monomial`.
- **Hypotheses**: none.
- **Uses from project**: `Roth.diag`
- **Used by**: Roth/CoeffNorm.lean:176 (`abs_coeff_diag_le`), Roth/CoeffNorm.lean:185 (`natDegree_diag_le`); no uses outside CoeffNorm.lean.
- **Visibility**: public
- **Lines**: 163–168, proof 3 lines
- **Notes**: Stated over `ℤ` only; nothing about `ℤ` is used (evidence: same proof over any `CommSemiring R`).

## Junk check (Step 8)
- Used anywhere? Yes: the two coefficient/degree lemmas `abs_coeff_diag_le` and `natDegree_diag_le` both start with `rw [diag_eq_sum]`.
- Wrapper of 1–2 mathlib calls? No: `eval₂_eq` plus four rewriting lemmas; a short but genuine proof.
- Does mathlib have it? No (loogle `Polynomial.coeff (MvPolynomial.aeval _ _) _` empty; leansearch/leanfinder return only `eval₂_eq`, `homogeneousComponent_apply`; grep finds no `aeval (fun _ ↦ X)` expansion). mathlib only has the `[Unique σ]` case `MvPolynomial.coeff_uniqueAlgEquiv`.
- Too specific (inline)? No; it is the bridge used twice and is the natural API for `diag`.
- Well-chosen? Yes, except the coefficient ring is needlessly `ℤ`.
- Conclusion: `KEEP` — action: keep; optionally restate over `[CommSemiring R]` with the re-aimed `aeval` form.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.diag_eq_sum` absent from mathlib. Not a glue lemma (real proof). Parent `Roth.diag` is `NO-composable-from-mathlib` (= `MvPolynomial.aeval (fun _ ↦ Polynomial.X)`), so per the re-aim rule this lemma is assessed as a statement about that mathlib term: `aeval (fun _ ↦ X) P = ∑ k ∈ P.support, monomial k.degree (coeff k P)`. The parent report flags this coefficient formula as the one real gap.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` has no diagnostics)
- decl `Roth.diag_eq_sum`:   resolved at Roth/CoeffNorm.lean:164
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms of integer polynomials and the estimates (Hasse derivatives, diagonal substitution, evaluation) for Lemmas 3 and 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.diag_eq_sum` is a theorem stating the following: for a polynomial `P = ∑_k a_k X^k` in variables indexed by `σ`, substituting the single variable `x` for every `X_j` gives `P(x, …, x) = ∑_{k ∈ supp P} a_k x^{|k|}`, where `|k| = ∑_j k_j` is the total degree of the monomial. Equivalently, the coefficient of `x^n` in `P(x, …, x)` is the sum of the coefficients of the degree-`n` homogeneous component of `P`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variable index set (no finiteness).
- `P : MvPolynomial σ ℤ` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `P(x, …, x) = ∑_{k ∈ supp P} a_k x^{|k|}`.

Conclusion (Lean): `diag P = ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k)`; re-aimed: `aeval (fun _ ↦ Polynomial.X) P = ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an explicit expansion formula for a specialisation of the evaluation homomorphism; a helper lemma.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3 (theorem)
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | coefficient of x^n in P(x,x,...,x) equals sum of coefficients of homogeneous component of degree n multivariate polynomial | partial | the identity itself, folklore: each monomial of total degree n collapses to x^n | CGAL `SubstituteHomogeneous` docs only; no textbook statement found |
| 2 | WebSearch (general form) | evaluation homomorphism k[x_1..x_n] to k[t], x_i to t, image as sum of homogeneous components t^d | partial | universal property / substitution homomorphism (ProofWiki "Polynomial Evaluation Homomorphism", UTK notes §5.1); `f(t,…,t) = ∑_d f_d(1,…,1) t^d` | the formula is derived, not stated, in sources |
| 3 | WebSearch (named-after / aliases) | "diagonal" specialization multivariate polynomial all variables equal "total degree" generating function | partial | warning: "diagonal" of a multivariate series in combinatorics means the equal-exponent part (Salvy, Adamczewski–Bell), a different operation | naming hazard; avoid "diag" in a mathlib name |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "same variable" | yes | l.1449 "When we replace x_1, …, x_m by the same variable x the absolute value of the coefficients ... at most the number of terms" | the paper uses exactly this expansion to bound coefficients (Lemma 9) |
| 6 | nLab | polynomial ring / free commutative algebra | partial | universal property; grading of `R[x_j]` by total degree | the map `x_j ↦ x` is graded of degree 0 for the total-degree grading; the identity says it is the graded map `R[x_j] → R[x]` summing each graded piece |
| 7 | nCatLab | — | n/a | — | not a categorical concept beyond the free-algebra adjunction (covered by #6) |
| 8 | Stacks Project | graded rings, polynomial algebra universal property (Tag 00EE area) | partial | `R[x_i] → S` determined by images of `x_i`; graded ring maps | no explicit formula; not algebraic-geometry specific |
| 9 | MathOverflow / Math.SE | (results of #1, #2) | partial | folklore "set all variables equal, group by total degree" | stated in answers without names |
| 10 | recent arXiv (last 5 years) | (results of #3) | partial | arXiv 2608.22561 uses total-degree specialisations of symmetric functions | ad hoc; principal specialisation `p(1,…,1)` analogues in symmetric-function theory |

### Literature summary (Phase 3)

Concept identified as: expansion of the evaluation homomorphism `R[x_j : j ∈ σ] → R[x]`, `x_j ↦ x`; equivalently its compatibility with the total-degree grading (`x^n`-coefficient = coefficient sum of the degree-`n` homogeneous component).
Sources agree on the standard form: yes (folklore; always derived in one line from the universal property).
Most general standard form: over any commutative (semi)ring; weighted version `x_j ↦ x^{w_j}` collects monomials by weighted degree `∑ w_j k_j`.
Generality dimensions where the literature varies:
  - coefficient ring: `ℤ` (Roth) to any commutative semiring.
  - substitution: `x_j ↦ x` to `x_j ↦ x^{w_j}` (weighted grading).
Disagreement with the literature: none; naming caveat only ("diagonal" means something else for power series).

### Generality analysis — `Roth.diag_eq_sum`

Literature-standard form (from Phase 3): for `[CommSemiring R]` and `w : σ → ℕ`, `aeval (fun i ↦ X ^ w i) P = ∑ k ∈ P.support, monomial (weight w k) (coeff k P)`; the unweighted case `w = 1` gives `monomial k.degree`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficients `ℤ` | `MvPolynomial σ ℤ` | any `CommSemiring R` | yes | proof uses only `eval₂_eq` and semiring rewriting; verified (evidence (1)) |
| 2 | `diag` (project name) | `Roth.diag P` | `aeval (fun _ ↦ X) P` | yes (re-aim) | `diag` is `aeval (fun _ ↦ X)` by definition; verified (evidence `example` from (1)) |
| 3 | substitution `x_j ↦ x` | constant family `X` | `X ^ w j` (weighted) | yes | verified (evidence (2), and (1) recovered as `w = 1`) |
| 4 | `σ` | arbitrary | arbitrary | no | already general (no `Fintype`) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 3 (rows 1–3), each compiled clean in the evidence file (`lean_diagnostic_messages`: no diagnostics).
Proposed restatement:

```lean
theorem MvPolynomial.aeval_X_pow_eq_sum [CommSemiring R] (w : σ → ℕ) (P : MvPolynomial σ R) :
    aeval (fun i ↦ (Polynomial.X : R[X]) ^ w i) P =
      ∑ k ∈ P.support, Polynomial.monomial (Finsupp.weight w k) (P.coeff k)
theorem MvPolynomial.aeval_X_eq_sum [CommSemiring R] (P : MvPolynomial σ R) :
    aeval (fun _ ↦ (Polynomial.X : R[X])) P =
      ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k)
theorem MvPolynomial.coeff_aeval_X [CommSemiring R] (P : MvPolynomial σ R) (n : ℕ) :
    (aeval (fun _ ↦ (Polynomial.X : R[X])) P).coeff n = ∑ k ∈ P.support with k.degree = n, P.coeff k
```

Cost of restatement: CHEAP — mechanical; the existing proof works verbatim for (1), the weighted proof is 4 lines (evidence (2)).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | pure algebra |
| 3 | construction vs universal property? | no | already about `aeval` (universal property) after re-aim | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | yes | `ℤ` to `CommSemiring R` | applies to `R[X]`-valued substitutions over any base, e.g. `ℕ`, `ℚ`, `ℤ_[p]` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | total degree to `Finsupp.weight w` | aligns with `weightedHomogeneousComponent`, `Finsupp.weight` API |
| 8 | concrete-via-abstract? | yes (mild) | proof never uses `diag` after `rw [diag]`; the content is about `aeval (fun _ ↦ X)` | the re-aim itself |
| 9 | false-generalisation guard | no false generalisation | `Roth.diag_eq_sum` is the `R = ℤ` instance of (1) by term application; (1) is the `w = 1` instance of (2) (both compiled) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `aeval_X_pow_eq_sum` / `aeval_X_eq_sum` / `coeff_aeval_X` as in 4b.
  - Cost: CHEAP
  - Mathlib downstream this enables: coefficient/degree arguments about `aeval (fun _ ↦ X)` (e.g. a sharper companion to `MvPolynomial.aeval_natDegree_le`; `natDegree ≤ totalDegree` in one line, evidence of the parent `Roth.diag` (4)); a general-`σ` analogue of `MvPolynomial.coeff_uniqueAlgEquiv`.
  - Real mathematical improvement: removes the irrelevant `ℤ` and the project-local name, so the lemma is about mathlib's own term.

### Proof strategy — `Roth.diag_eq_sum`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | the lemma itself is the missing helper; an alternative route via `rename (fun _ ↦ ())` + `uniqueAlgEquiv` + `coeff_uniqueAlgEquiv` would need a missing `coeff_rename` sum formula for `MvPolynomial` (only `MvPowerSeries.coeff_rename` exists) | n/a |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (expand by `eval₂_eq`, collapse the product with `Finset.prod_pow_eq_pow_sum`, recognise `C a * X ^ n` as `monomial`)
  - Missing mathlib API (if any): this lemma and its coefficient form; optionally `MvPolynomial.coeff_rename` as a sum.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.diag_eq_sum`

[A] Lean-Finder       "coefficient of x^n in P(x,...,x) equals sum of coefficients of P over monomials of total degree n"   hits: `homogeneousComponent_apply`, `coeff_sum`, `Polynomial.coeff_homogenize`, Vieta lemmas — none about `aeval (fun _ ↦ X)`
[B] Loogle            `Polynomial.coeff (MvPolynomial.aeval _ _) _`   no hits (also no hits in the parent run; `Polynomial.natDegree (MvPolynomial.aeval _ _)` hits only `aeval_natDegree_le`)
[C] LeanSearch        "evaluating a multivariate polynomial with every variable replaced by X equals sum over support of monomial of total degree"   hits: `eval_eq'`, `eval₂_eq`, `eval_eq`, `eval₂_eq'`, `homogeneousComponent_apply`, `support_sum_monomial_coeff` — building blocks only
[D] Grep mathlib src  `coeff_uniqueAlgEquiv`, `uniqueAlgEquiv_monomial`, `theorem coeff_rename`, `rename_monomial`, `degree_mapDomain`, `monomial .*\.degree`, `fun _ ↦ X` / `fun _ => Polynomial.X`, `aeval_eq_sum`, `eval₂_eq'`   hits: `MvPolynomial.coeff_uniqueAlgEquiv` (Mathlib/Algebra/MvPolynomial/Equiv.lean:103, `[Unique σ]` only), `MvPolynomial.rename_monomial` (Algebra/MvPolynomial/Rename.lean:94), `Finsupp.degree_mapDomain` (Data/Finsupp/Weight.lean:273), `MvPolynomial.rename_homogeneousComponent` (RingTheory/MvPolynomial/Homogeneous.lean:580); `coeff_rename` only for `MvPowerSeries`; `aeval_eq_sum` only for (Mv)PowerSeries evaluation; no general-σ diagonal expansion
[E] Name pattern      `MvPolynomial.eval₂_eq`, `MvPolynomial.aeval_def`, `Finset.prod_pow_eq_pow_sum`, `Finsupp.degree_apply`, `Finsupp.weight_apply`, `Finsupp.degree_eq_weight_one`, `Polynomial.C_mul_X_pow_eq_monomial`, `Polynomial.finsetSum_coeff` (all used in the compiled evidence)   hits (building blocks)

Searched for both the user's form (`diag P = ∑ …`) and the literature-standard forms (unweighted and weighted `aeval` expansions, coefficient form).

Concluded: found building blocks (`MvPolynomial.eval₂_eq`, `Finset.prod_pow_eq_pow_sum`, `Polynomial.C_mul_X_pow_eq_monomial`, and the `[Unique σ]` case `MvPolynomial.coeff_uniqueAlgEquiv`); the statement itself is not in mathlib, in either form.

### Normal-form check — `Roth.diag_eq_sum`

Equivalent formalisms: (a) `aeval (fun _ ↦ X) P = ∑ k ∈ P.support, monomial k.degree (coeff k P)`; (b) `coeff n (aeval (fun _ ↦ X) P) = ∑ k ∈ P.support with k.degree = n, coeff k P`; (c) via `uniqueAlgEquiv R Unit (rename (fun _ ↦ ()) P)` and `coeff_uniqueAlgEquiv`.
Does mathlib already have a canonical form for this idea? For `[Unique σ]`, yes: `coeff_uniqueAlgEquiv` (coefficient form, LHS `coeff n (map P)`). For general σ, no.
Is our statement stated against the canonical form? After re-aim yes: LHS is mathlib's `aeval`, RHS the explicit expansion (matching `eval₂_eq`'s convention of expanding on the RHS).
RHS convention respected? yes.

### Syntactic generality — `Roth.diag_eq_sum`

Alternative restatements attempted:
- (a) sum-of-monomials form over `CommSemiring R` (compiles; evidence (1))
- weighted form with `Finsupp.weight w` (compiles; evidence (2))
- (b) coefficient form (compiles; evidence (3))
- (c) `rename` + `uniqueAlgEquiv` (equality compiles, evidence (4); the coefficient route would need a missing `MvPolynomial.coeff_rename` sum lemma)
Chosen restatement: weighted (2) as the main lemma, with (a) and (b) as corollaries.
Justification: (a) is what `rw` consumers use (both project call sites rewrite with it then take `coeff`/`natDegree`); (b) is the directly applicable coefficient fact, matching `coeff_uniqueAlgEquiv`; (2) is the general form at zero extra cost.

### Superfluous-argument audit — `Roth.diag_eq_sum`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | coefficient ring `ℤ` | no | any `CommSemiring R` (evidence (1)) |
| 2 | `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (after re-aim to `aeval`)
Syntactic generality: RESTATE (general `R`, weighted main lemma plus coefficient corollary)
Superfluous arguments: 1 to drop (the `ℤ` specialisation)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.diag_eq_sum`

Internal use count: 0 outside the declaring file (2 inside it)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:176 (`abs_coeff_diag_le`) | `rw [diag_eq_sum, Polynomial.finsetSum_coeff, Int.cast_sum, ← nsmul_eq_mul]` |
| Roth/CoeffNorm.lean:185 (`natDegree_diag_le`) | `rw [diag_eq_sum]` then `Polynomial.natDegree_sum_le_of_forall_le` |

Inline-derivation grep (`eval₂_eq`, `prod_pow_eq_pow_sum`, `C_mul_X_pow_eq_monomial` over `Roth/`):
  - (none) — the hits (MainLemma.lean:469, 528; GenWronskian.lean:63; HasseDeriv.lean:278; Separation.lean:73; CoeffNorm.lean:228) are unrelated expansions, none re-deriving the `aeval (fun _ ↦ X)` formula.

### Composition check (Phase 6)

Can `aeval (fun _ ↦ X) P = ∑ k ∈ P.support, monomial k.degree (coeff k P)` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [aeval_def, eval₂_eq]; simp_rw [Finset.prod_pow_eq_pow_sum, ← Finsupp.degree_apply, Polynomial.algebraMap_eq, Polynomial.C_mul_X_pow_eq_monomial]`
  - Mathlib decls used: `MvPolynomial.aeval_def`, `MvPolynomial.eval₂_eq`, `Finset.prod_pow_eq_pow_sum`, `Finsupp.degree_apply`, `Polynomial.algebraMap_eq`, `Polynomial.C_mul_X_pow_eq_monomial`
  - Result: succeeds, but it is a rewriting proof under a binder with six lemmas, not a chained call (heuristics table: "`by rw [...]; simp …`" is a real proof)
Attempt 2: `uniqueAlgEquiv R Unit (rename (fun _ ↦ ()) P)` + `coeff_uniqueAlgEquiv` for the coefficient form
  - Mathlib decls used: `MvPolynomial.uniqueAlgEquiv`, `MvPolynomial.rename`, `MvPolynomial.eval₂_rename`, `MvPolynomial.coeff_uniqueAlgEquiv`
  - Result: partial — reduces to `coeff (single () n) (rename (fun _ ↦ ()) P) = ∑ k with k.degree = n, coeff k P`, for which mathlib has no `MvPolynomial.coeff_rename` sum lemma (only `MvPowerSeries.coeff_rename`)
Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.diag_eq_sum`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): folklore expansion of the substitution hom `x_j ↦ x` (equivalently its grading compatibility); standard over any commutative semiring, naturally weighted; paper l.1449 uses it for the Lemma 9 coefficient bound.
- Generality analysis (Phase 4): STRICTLY NARROWER (`ℤ`, project name `diag`, unweighted); all three weakenings compiled clean.
- Mathlib search (Phase 5): not in mathlib in any form; only building blocks and the `[Unique σ]` case `coeff_uniqueAlgEquiv`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Re-aimed at the parent's mathlib term, the lemma says `aeval (fun _ ↦ X) P = ∑_{k ∈ supp P} coeff k P • x^{|k|}`. Mathlib can state this map but has no way to compute it for general `σ`. Loogle on `Polynomial.coeff (MvPolynomial.aeval _ _) _` returns nothing. The nearest lemma, `MvPolynomial.coeff_uniqueAlgEquiv`, covers only one variable (`[Unique σ]`). The other route, through `rename`, stops at a missing `MvPolynomial.coeff_rename` sum formula. So the gap is real: a coefficient formula for `aeval (fun _ ↦ X)`, which is also the partner of the existing degree bound `MvPolynomial.aeval_natDegree_le`. The project proof works unchanged over any `CommSemiring R`. The weighted version (`X_i ↦ X ^ w i`, giving `monomial (Finsupp.weight w k)`) costs four lines and contains the unweighted one as `w = 1`. All of this is compiled in the evidence file.

The generalisation is LITERATURE-WEAKENING (`ℤ` to `CommSemiring R`, constant to weighted substitution) together with the re-aim from `Roth.diag` to `aeval`. Avoid "diag" in the mathlib name, because "diagonal" of a multivariate series means the equal-exponent part in the combinatorics literature.

Reason for the generalisation: LITERATURE-WEAKENING (plus the re-aim to the mathlib term).
Proposed restatement:
```lean
theorem MvPolynomial.aeval_X_pow_eq_sum {σ R : Type*} [CommSemiring R] (w : σ → ℕ)
    (P : MvPolynomial σ R) :
    aeval (fun i ↦ (Polynomial.X : Polynomial R) ^ w i) P =
      ∑ k ∈ P.support, Polynomial.monomial (Finsupp.weight w k) (P.coeff k) := by
  rw [aeval_def, eval₂_eq]
  refine Finset.sum_congr rfl fun k _ ↦ ?_
  simp_rw [← pow_mul, Finset.prod_pow_eq_pow_sum, Polynomial.algebraMap_eq,
    Polynomial.C_mul_X_pow_eq_monomial, Finsupp.weight_apply, Finsupp.sum, smul_eq_mul, mul_comm]

theorem MvPolynomial.aeval_X_eq_sum (P : MvPolynomial σ R) :
    aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P =
      ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k)

theorem MvPolynomial.coeff_aeval_X (P : MvPolynomial σ R) (n : ℕ) :
    (aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P).coeff n =
      ∑ k ∈ P.support with k.degree = n, P.coeff k
```
Estimated cost of regeneralisation: CHEAP (all three compiled in evidence).
Proposed mathlib location: Mathlib/RingTheory/Polynomial/Basic.lean, next to `MvPolynomial.aeval_natDegree_le` (that file already imports both `Polynomial` and `MvPolynomial` with degree API). Alternative: Mathlib/RingTheory/MvPolynomial/WeightedHomogeneous.lean if the import of `Polynomial` is acceptable there.
PR grouping: one PR, "feat(RingTheory/Polynomial): expand `MvPolynomial.aeval (fun i ↦ X ^ w i)`", containing the three lemmas; optionally add `natDegree (aeval (fun _ ↦ X) P) ≤ totalDegree P` (parent `Roth.diag` evidence (4)) as a corollary.
Local refactor: restate `Roth.diag_eq_sum` over `[CommSemiring R]` (only if `diag` itself is generalised, as the parent report suggests) or prove it as `MvPolynomial.aeval_X_eq_sum P` once upstreamed. The call sites Roth/CoeffNorm.lean:176 (`abs_coeff_diag_le`, could then start from `coeff_aeval_X`) and :185 (`natDegree_diag_le`) need no change.
Next action: run `/generalise Roth.diag_eq_sum` targeting the weighted `aeval` form above, then `/cleanup` and `/pre-submit` before opening the mathlib PR.

---

## Next step

Upstream `MvPolynomial.aeval_X_pow_eq_sum` (weighted), with `aeval_X_eq_sum` and `coeff_aeval_X` as corollaries, over `[CommSemiring R]` to Mathlib/RingTheory/Polynomial/Basic.lean. Locally, `Roth.diag_eq_sum` becomes the `ℤ` instance; the two CoeffNorm.lean call sites are unchanged.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.diag_eq_sum/diag_eq_sum_general.lean` (imports `Roth.CoeffNorm`; `lean_diagnostic_messages`: no diagnostics, success). It contains: (1) `aeval_X_eq_sum` over `[CommSemiring R]`, with `Roth.diag_eq_sum`'s statement recovered by term application; (2) weighted `aeval_X_pow_eq_sum`, with (1) recovered as `w = 1` via `Finsupp.degree_eq_weight_one`; (3) `coeff_aeval_X`; (4) `aeval (fun _ ↦ X) P = uniqueAlgEquiv R Unit (rename (fun _ ↦ ()) P)`.
- Loogle (1), LeanSearch (1), Lean-Finder (1) queries as in the search-status block; mathlib greps as in [D].
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex (l.1449).
- Project greps: `grep -rn diag_eq_sum Roth/` (call sites); inline-derivation grep for `eval₂_eq`, `prod_pow_eq_pow_sum`, `C_mul_X_pow_eq_monomial`.
