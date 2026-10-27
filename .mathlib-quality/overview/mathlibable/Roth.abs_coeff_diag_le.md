---
decl: Roth.abs_coeff_diag_le
file: Roth/CoeffNorm.lean
line: 174
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Re-aimed at the mathlib term aeval (fun _ ↦ X), the bound norm of coeff n of aeval (fun i ↦ X ^ w i) P at most #support P times B is absent from mathlib (no coefficient API for aeval (fun _ ↦ X) at all) and not composable from current mathlib, and the project proof compiles verbatim over any SeminormedCommRing (weighted, plus a sharper per-degree card form), recovering the Z/abs statement; ship as a corollary of the coeff_aeval_X expansion.
action: Ship MvPolynomial.norm_coeff_aeval_X_le (sharp, filter by degree = n) and the #support corollary over [SeminormedCommRing R] in the same PR as MvPolynomial.aeval_X_pow_eq_sum / coeff_aeval_X (Mathlib/RingTheory/Polynomial/Basic.lean or an Analysis/Polynomial companion); keep the Z form for the single call site Roth/MainLemma.lean:509 via Int.norm_eq_abs.
---

# Roth.abs_coeff_diag_le

## Inventory entry

### `theorem Roth.abs_coeff_diag_le`
- **Type**: `{σ : Type*} (P : MvPolynomial σ ℤ) {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (n : ℕ) : |(((diag P).coeff n : ℤ) : ℝ)| ≤ P.support.card * B`
- **What**: Every coefficient of the diagonal specialisation `P(x, …, x)` is bounded in absolute value by the number of terms of `P` times a uniform bound `B` for the coefficients of `P`.
- **How**: Rewrites with `diag_eq_sum` and `Polynomial.finsetSum_coeff`, pushes the cast through with `Int.cast_sum`, then `Finset.abs_sum_le_sum_abs` followed by `Finset.sum_le_card_nsmul`; each summand is handled by `Polynomial.coeff_monomial` and `split_ifs <;> grind [abs_nonneg]` (the zero branch uses `0 ≤ |a| ≤ B`).
- **Hypotheses**: `hB` (uniform coefficient bound). No finiteness of `σ`.
- **Uses from project**: `Roth.diag`, `Roth.diag_eq_sum`
- **Used by**: Roth/MainLemma.lean:509 (`abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, private, applied to `hasseDeriv j P` with `B := 2^{∑ r_k} B`); also listed in the CoeffNorm.lean module docstring (line 32).
- **Visibility**: public
- **Lines**: 170–179 (docstring 170–173, statement 174–175), proof length 4 lines
- **Notes**: Source: §6, proof of Lemma 9 (clean.tex l.1449). The bound with `#support` is crude; the per-degree count `#{k ∈ supp P : |k| = n}` is the natural sharp form (evidence (2)).

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:509 (Lemma 9 coefficient estimate).
- Wrapper of 1–2 mathlib calls? No: it needs the project expansion `diag_eq_sum` plus three mathlib lemmas and a case split; mathlib has no coefficient formula for `aeval (fun _ ↦ X)`.
- Does mathlib have it? No (loogle `‖Polynomial.coeff (MvPolynomial.aeval _ _) _‖` empty; leansearch/leanfinder only general `norm_sum_le_of_le`, `Multiset.sum_le_card_nsmul`).
- Too specific / inline? Single use, but it is the named step of the paper's argument and keeps MainLemma readable; inlining would duplicate the expansion argument.
- Well-chosen? Yes, modulo the `ℤ`-with-cast-to-`ℝ` presentation (a norm statement over a seminormed ring is cleaner).
- Conclusion: `KEEP`. Action: keep; optionally restate via `‖·‖` over `[SeminormedCommRing R]` once `diag` is generalised.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.abs_coeff_diag_le` absent from mathlib (grep `theorem abs_coeff_diag_le` over `.lake/packages/mathlib/Mathlib/`: no hit). Not a glue lemma. Parent `Roth.diag` is `NO-composable-from-mathlib` (= `MvPolynomial.aeval (fun _ ↦ Polynomial.X)`) and `Roth.diag_eq_sum` is `YES-but-generalise-first`; per the re-aim rule this lemma is assessed as a statement about the mathlib term: `‖coeff n (aeval (fun _ ↦ X) P)‖ ≤ #supp P · B`.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` has no diagnostics)
- decl `Roth.abs_coeff_diag_le`: resolved at Roth/CoeffNorm.lean:174
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms of integer polynomials and the estimates (Hasse derivatives, diagonal substitution, evaluation) for Lemmas 3 and 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.abs_coeff_diag_le` is a theorem stating the following: let `P = ∑_k a_k X^k` be a polynomial in variables indexed by `σ` with integer coefficients, all satisfying `|a_k| ≤ B`. Then every coefficient of the one-variable polynomial `P(x, …, x)` has absolute value at most `N · B`, where `N` is the number of nonzero terms of `P`. (Indeed the coefficient of `x^n` is `∑_{|k| = n} a_k`.)

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variable index set (no finiteness).
- `P : MvPolynomial σ ℤ` — the polynomial.
- `B : ℝ` — coefficient bound; `n : ℕ` — coefficient index.

Hypotheses (Lean side):
- `hB : ∀ d, |(P.coeff d : ℝ)| ≤ B` — uniform coefficient bound.

Conclusion (math): `|[x^n] P(x, …, x)| ≤ #supp(P) · B`.

Conclusion (Lean): `|(((diag P).coeff n : ℤ) : ℝ)| ≤ P.support.card * B`; re-aimed: `‖(aeval (fun _ ↦ Polynomial.X) P).coeff n‖ ≤ P.support.card * B`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper coefficient estimate (triangle inequality on the expansion of a specialisation map).

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 4 (theorem)
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | coefficients of P(x,x,...,x) bounded by number of terms times maximum coefficient multivariate polynomial | partial | no source states it; folklore one-line argument (coefficient of `x^d` is sum of degree-`d` coefficients) | related term-count/height bounds in sparse-polynomial literature (arXiv 2609.08074, 1807.06256) |
| 2 | WebSearch (general form) | height of polynomial under specialization of variables bound "number of terms" height inequality | partial | height inequalities `H(f(g)) ≤ …` and term-count measures (Dobrowolski–Smyth arXiv 1606.04376, Krick survey arXiv 2506.18144) | general shape: height of image under a monomial map ≤ (max fibre size) · height |
| 3 | WebSearch (named-after / aliases) | Roth theorem proof Lemma replace variables by same variable coefficient bound "number of terms" | partial | Roth-proof expositions (Evertse notes, arXiv 2502.00731, Roth 1955) use it silently | it is a routine step of Roth-type proofs, never a named lemma |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "same variable" | yes | l.1449 "the absolute value of the coefficients of the resulting polynomial is at most the number of terms of the polynomial ... multiplied by the coefficient bound" | exactly the project statement |
| 6 | nLab | polynomial ring / free commutative algebra / graded ring | partial | `x_j ↦ x` is the graded map summing each total-degree piece | no norm content; supports the per-degree sharp form |
| 7 | nCatLab | — | n/a | — | not a categorical statement (an archimedean estimate) |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no norms on coefficients there |
| 9 | MathOverflow / Math.SE | (results of #1, #2) | partial | folklore triangle-inequality argument | stated in passing only |
| 10 | recent arXiv (last 5 years) | (results of #1, #2) | partial | sparse coefficient bounds depending on number of terms (arXiv 2609.08074) | ad hoc, not this statement |

### Literature summary (Phase 3)

Concept identified as: coefficient (height) bound for the specialisation `x_j ↦ x` (more generally the monomial map `x_j ↦ x^{w_j}`): the image's height is at most the maximum fibre size times the height, hence at most the number of terms times the height.
Sources agree on the standard form: yes (folklore; triangle inequality on the expansion).
Most general standard form: over any (semi)normed commutative ring; sharp constant is `#{k ∈ supp P : weight k = n}`; crude constant `#supp P`.
Generality dimensions where the literature varies:
  - coefficient ring: `ℤ` with `|·|` (Roth) to any seminormed commutative ring / absolute value.
  - substitution: `x_j ↦ x` to `x_j ↦ x^{w_j}`.
  - constant: `#supp P` to the per-degree count.
Disagreement with the literature: none.

### Generality analysis — `Roth.abs_coeff_diag_le`

Literature-standard form (from Phase 3): for `[SeminormedCommRing R]`, `w : σ → ℕ`, `‖coeff n (aeval (fun i ↦ X ^ w i) P)‖ ≤ #supp P · B`, and sharply (unweighted) `≤ #{k ∈ supp P : k.degree = n} · B`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficients `ℤ`, `|(· : ℝ)|` | `MvPolynomial σ ℤ` with cast-abs | `[SeminormedCommRing R]`, `‖·‖` | yes | proof uses only triangle inequality and `‖0‖ = 0`; verified (evidence (1)) |
| 2 | `diag` (project name) | `Roth.diag P` | `aeval (fun _ ↦ X) P` | yes (re-aim) | `diag` is `aeval (fun _ ↦ X)` by definition; recovered in evidence |
| 3 | substitution `x_j ↦ x` | constant `X` | `X ^ w j` | yes | verified (evidence (1)) |
| 4 | constant `#supp P` | `P.support.card` | `#{k ∈ supp P : k.degree = n}` | yes (sharper conclusion) | verified (evidence (2)); implies the crude form (evidence example) |
| 5 | `hB` | uniform bound | uniform bound | no | needed (only on `supp P` really, but `∀ d` is the standard shape and harmless since off-support coefficients are 0) |
| 6 | `σ` | arbitrary | arbitrary | no | already general |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 4 (rows 1–4), each compiled clean in the evidence file (`lean_diagnostic_messages`: success, no diagnostics).
Proposed restatement:

```lean
theorem MvPolynomial.norm_coeff_aeval_X_pow_le [SeminormedCommRing R] (w : σ → ℕ)
    (P : MvPolynomial σ R) {B : ℝ} (hB : ∀ d, ‖P.coeff d‖ ≤ B) (n : ℕ) :
    ‖(aeval (fun i ↦ (Polynomial.X : R[X]) ^ w i) P).coeff n‖ ≤ P.support.card * B
theorem MvPolynomial.norm_coeff_aeval_X_le [SeminormedCommRing R] (P : MvPolynomial σ R)
    {B : ℝ} (hB : ∀ d, ‖P.coeff d‖ ≤ B) (n : ℕ) :
    ‖(aeval (fun _ ↦ (Polynomial.X : R[X])) P).coeff n‖ ≤ #{k ∈ P.support | k.degree = n} * B
```

Cost of restatement: CHEAP — the project proof works with `abs_sum_le_sum_abs` replaced by `norm_sum_le`.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | single bound hypothesis |
| 2 | sequences to filters? | no | — | finite estimate |
| 3 | construction vs universal property? | no | already about `aeval` after re-aim | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | yes | `ℤ` with cast-to-`ℝ` abs to `[SeminormedCommRing R]` with `‖·‖` | matches mathlib's coefficient-norm API (`Polynomial.le_supNorm`, `norm_coeff_le_choose_mul_mahlerMeasure`); `ℤ` recovered via `Int.norm_eq_abs` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | total degree to `Finsupp.weight w` | aligns with `weightedHomogeneousComponent` |
| 8 | concrete-via-abstract? | yes (mild) | after `rw [diag_eq_sum]` the proof never mentions `diag`; content is about `aeval (fun _ ↦ X)` | the re-aim |
| 9 | false-generalisation guard | no false generalisation | the `ℤ` statement is recovered from (1) with `R = ℤ`, `w = 1` by `simpa [Roth.diag, Int.norm_eq_abs]` (compiled) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the two norm lemmas in 4b.
  - Cost: CHEAP
  - Mathlib downstream this enables: coefficient estimates for specialisations `MvPolynomial σ R → R[X]` over `ℤ`, `ℚ`, `ℂ`, `ℤ_[p]` alike, composing with `Polynomial` norm API (e.g. `Polynomial.supNorm`, remainder bounds).
  - Real mathematical improvement: removes the `ℤ`/cast detour and the project-local `diag`, and gives the sharp per-degree constant.

### Proof strategy — `Roth.diag_eq_sum`-based

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | the expansion `aeval_X_eq_sum` / `coeff_aeval_X` (assessed in `Roth.diag_eq_sum`) | file with that PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (expand, triangle inequality, `sum_le_card_nsmul`)
  - Missing mathlib API (if any): `MvPolynomial.coeff_aeval_X` (with it the sharp form is `norm_sum_le` + `sum_le_card_nsmul`, as in evidence (2)).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.abs_coeff_diag_le`

[A] Lean-Finder       "coefficient of P(X,...,X) bounded in norm by number of terms of multivariate polynomial P times maximum coefficient norm"   hits: `Polynomial.cauchyBound`, `Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`, Chevalley bounds — none relevant
[B] Loogle            `‖Polynomial.coeff (MvPolynomial.aeval _ _) _‖`   no hits (and `Polynomial.coeff (MvPolynomial.aeval _ _) _` also empty, per the `Roth.diag_eq_sum` run)
[C] LeanSearch        "norm of coefficient of a finite sum of monomials bounded by card times bound"   hits: `norm_sum_le_of_le`, `Multiset.sum_le_card_nsmul`, `ClassGroup.norm_le`, `norm_coeff_le_choose_mul_mahlerMeasure` — building blocks only
[D] Grep mathlib src  `theorem abs_coeff_diag_le`, `norm_coeff_aeval`, `coeff_aeval_X`, `norm_coeff.*card` in Analysis/Polynomial and RingTheory/Polynomial   no hits (only `Polynomial.card_support_mul_le`, unrelated)
[E] Name pattern      `norm_sum_le`, `Finset.sum_le_card_nsmul`, `Finset.card_filter_le`, `Polynomial.finsetSum_coeff`, `Polynomial.coeff_monomial`, `Int.norm_eq_abs` (all used in the compiled evidence)   hits (building blocks)

Searched for both the user's form (`|coeff n (diag P)| ≤ …`) and the literature-standard forms (norm over seminormed ring, weighted, per-degree sharp).

Concluded: found building blocks (`norm_sum_le`, `Finset.sum_le_card_nsmul`, `Polynomial.finsetSum_coeff`); the statement is not in mathlib in any form, and its prerequisite expansion of `aeval (fun _ ↦ X)` is also absent.

### Normal-form check — `Roth.abs_coeff_diag_le`

Equivalent formalisms: (a) `|((coeff n (diag P) : ℤ) : ℝ)| ≤ …` (project); (b) `‖coeff n (aeval (fun _ ↦ X) P)‖ ≤ …`; (c) a sup-norm statement `supNorm (aeval (fun _ ↦ X) P) ≤ #supp P · sup ‖coeff‖`.
Does mathlib already have a canonical form for this idea? No; mathlib's coefficient estimates are stated pointwise as `‖p.coeff n‖ ≤ …` (e.g. `Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`).
Is our statement stated against the canonical form? After re-aim, (b) follows the pointwise `‖coeff‖ ≤` convention.
RHS convention respected? yes (inequality; bound on RHS).

### Syntactic generality — `Roth.abs_coeff_diag_le`

Alternative restatements attempted:
- (b) weighted norm form with `#supp P` (compiles; evidence (1))
- (b) sharp per-degree form (compiles; evidence (2)), which implies the crude form (compiled example)
- (a) recovered from (1) (compiled example)
Chosen restatement: sharp per-degree form as the main lemma, `#supp P` as corollary (the form the call site uses, since it then bounds `#supp` by the box cardinality).
Justification: hypothesis `hB` is the same in all forms; the crude corollary is what consumers apply directly, the sharp form is free.

### Superfluous-argument audit — `Roth.abs_coeff_diag_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | coefficient ring `ℤ` | no | any `SeminormedCommRing R` (evidence (1)) |
| 2 | cast to `ℝ` + `|·|` | no | replaced by `‖·‖`; `ℤ` recovered via `Int.norm_eq_abs` |
| 3 | `hB` | yes | the bound |
| 4 | `P`, `n` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (after re-aim to `aeval` and `‖·‖`)
Syntactic generality: RESTATE (seminormed ring, weighted, sharp per-degree main lemma)
Superfluous arguments: 1 to drop (the `ℤ`/cast specialisation)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.abs_coeff_diag_le`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:509 (`abs_coeff_diag_hasseDeriv_modByMonic_le_aux`) | `(abs_coeff_diag_le _ (abs_coeff_hasseDeriv_le j P hd hc) k).trans (mul_le_mul_of_nonneg_right hsupp (by positivity))` |

Inline-derivation grep (`abs_sum_le_sum_abs`, `sum_le_card_nsmul` over `Roth/`):
  - (none) — hits at CoeffNorm.lean:115 (`normOne_le_card_mul`), :231, MainLemma.lean:718, Main.lean:403 are different estimates, none re-deriving the diagonal coefficient bound.

### Composition check (Phase 6)

Can `‖coeff n (aeval (fun _ ↦ X) P)‖ ≤ #supp P · B` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [aeval_def, eval₂_eq]`, then expand, `norm_sum_le`, `Finset.sum_le_card_nsmul`, `coeff_monomial` case split
  - Mathlib decls used: `MvPolynomial.eval₂_eq`, `Finset.prod_pow_eq_pow_sum`, `Polynomial.C_mul_X_pow_eq_monomial`, `Polynomial.finsetSum_coeff`, `norm_sum_le`, `Finset.sum_le_card_nsmul`, `Polynomial.coeff_monomial`
  - Result: succeeds only as a multi-step rewriting proof (two lemmas' worth of content: the expansion and the estimate)
Attempt 2: assuming the proposed `MvPolynomial.coeff_aeval_X` is upstreamed: `coeff_aeval_X` ▸ `(norm_sum_le _ _).trans (Finset.sum_le_card_nsmul …)`, then `Finset.card_filter_le` for the crude form
  - Mathlib decls used: `coeff_aeval_X` (not yet in mathlib), `norm_sum_le`, `Finset.sum_le_card_nsmul`, `Finset.card_filter_le`
  - Result: partial — 3–4 calls, but depends on a lemma mathlib does not have
Conclusion: NOT-COMPOSABLE (from current mathlib)

## Verdict: `Roth.abs_coeff_diag_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): folklore height bound for the specialisation `x_j ↦ x`; paper l.1449 states it verbatim; natural over any seminormed ring with sharp per-degree constant.
- Generality analysis (Phase 4): STRICTLY NARROWER (`ℤ` with cast-abs, project name `diag`, unweighted, crude constant); all four weakenings compiled clean.
- Mathlib search (Phase 5): not in mathlib; even the underlying coefficient formula for `aeval (fun _ ↦ X)` is missing.
- Composition check (Phase 6): NOT-COMPOSABLE from current mathlib.

**Rationale:**

The specific gap: mathlib has no coefficient API for the specialisation `aeval (fun _ ↦ X) : MvPolynomial σ R → R[X]` beyond the degree bound `MvPolynomial.aeval_natDegree_le` — no expansion (the gap found in `Roth.diag_eq_sum`) and no coefficient-size estimate. This lemma is the size companion: `‖[x^n] P(x,…,x)‖ ≤ #{k ∈ supp P : |k| = n} · B ≤ #supp P · B`. It is a standard step of Roth/Siegel-type auxiliary-polynomial arguments and of height computations under monomial maps, and composes with mathlib's pointwise coefficient-norm results (`Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`, `Polynomial.le_supNorm`) and with the remainder bounds the project already uses (`norm_coeff_modByMonic_le` at the call site). Mathematically it is small; it belongs in mathlib only as a corollary shipped next to the expansion lemma, not as a standalone PR.

The project's Lean form is a specialisation: the `ℤ`-cast-abs presentation, the local name `diag`, the unweighted substitution and the crude constant are all inessential. The project proof compiles over any `SeminormedCommRing R` with `norm_sum_le` in place of `abs_sum_le_sum_abs`, in weighted form, and the sharp per-degree form follows in two calls from the expansion; the original statement is recovered by `simpa [Roth.diag, Int.norm_eq_abs]` (evidence). Once `coeff_aeval_X` exists, the crude bound is a 3–4 call composition, so a reviewer might prefer only the sharp form be added; that is a PR-grain question, not a reason to drop it.

Reason for the generalisation: LITERATURE-WEAKENING (`ℤ` to `SeminormedCommRing R`; weighted; sharp constant) plus MODERN-IDIOM (re-aim to `aeval`, norm-based statement).
Proposed restatement:
```lean
theorem MvPolynomial.norm_coeff_aeval_X_le {σ R : Type*} [SeminormedCommRing R]
    (P : MvPolynomial σ R) {B : ℝ} (hB : ∀ d, ‖P.coeff d‖ ≤ B) (n : ℕ) :
    ‖(aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P).coeff n‖ ≤
      #{k ∈ P.support | k.degree = n} * B := by
  rw [coeff_aeval_X, ← nsmul_eq_mul]
  exact (norm_sum_le _ _).trans (Finset.sum_le_card_nsmul _ _ B fun k _ ↦ hB k)

theorem MvPolynomial.norm_coeff_aeval_X_pow_le [SeminormedCommRing R] (w : σ → ℕ)
    (P : MvPolynomial σ R) {B : ℝ} (hB : ∀ d, ‖P.coeff d‖ ≤ B) (n : ℕ) :
    ‖(aeval (fun i ↦ (Polynomial.X : Polynomial R) ^ w i) P).coeff n‖ ≤ P.support.card * B
```
Estimated cost of regeneralisation: CHEAP (all compiled in evidence).
Mathlib downstream this enables: coefficient-size control for `aeval (fun _ ↦ X)` over any seminormed ring, feeding `Polynomial` remainder/sup-norm estimates; pairs with `aeval_natDegree_le` to give the full (degree, height) control used in Diophantine approximation.
Proposed mathlib location: same PR as `MvPolynomial.aeval_X_pow_eq_sum` / `coeff_aeval_X` (Mathlib/RingTheory/Polynomial/Basic.lean), or, if normed imports are unwelcome there, an Analysis companion (e.g. Mathlib/Analysis/Polynomial/Basic.lean).
PR grouping: with `Roth.diag_eq_sum`'s proposed lemmas (and, optionally, the `MvPolynomial.l1Norm` PR of `Roth.normOne_le_card_mul`, where the bound reads `≤ l1Norm`-style).
Local refactor: keep the `ℤ` form for Roth/MainLemma.lean:509, proved as the `R = ℤ`, `w = 1` instance via `Int.norm_eq_abs`.
Next action: run `/generalise Roth.abs_coeff_diag_le` targeting the sharp `norm_coeff_aeval_X_le` form, then `/cleanup` and `/pre-submit` with the `coeff_aeval_X` PR.

---

## Next step

Ship `MvPolynomial.norm_coeff_aeval_X_le` (sharp) with the `#support` corollary over `[SeminormedCommRing R]` alongside `coeff_aeval_X`; locally `Roth.abs_coeff_diag_le` becomes the `ℤ` instance, call site Roth/MainLemma.lean:509 unchanged.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.abs_coeff_diag_le/abs_coeff_diag_le_general.lean` (imports `Mathlib.Analysis.Normed.Ring.Lemmas`, `Mathlib.Analysis.Normed.Group.Int`, `Roth.CoeffNorm`; `lean_diagnostic_messages`: success, no diagnostics after two import/elaboration fixes). Contents: weighted expansion `aeval_X_pow_eq_sum`; (1) `norm_coeff_aeval_X_pow_le` over `[SeminormedCommRing R]`; (2) sharp `norm_coeff_aeval_X_le` with the per-degree filter card; example (2) implies the `#support` form; example recovering `Roth.abs_coeff_diag_le` exactly from (1) with `R = ℤ`, `w = 1`.
- Loogle (1), LeanSearch (1), Lean-Finder (1) queries and mathlib greps as in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: clean.tex l.1449.
- Project greps: `grep -rn abs_coeff_diag_le Roth/` (call site); inline-derivation grep for `abs_sum_le_sum_abs`, `sum_le_card_nsmul`.
