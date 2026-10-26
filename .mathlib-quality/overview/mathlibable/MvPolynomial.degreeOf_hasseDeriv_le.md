---
decl: MvPolynomial.degreeOf_hasseDeriv_le
file: Roth/HasseDeriv.lean
line: 210
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Basic degree bound for the multivariate Hasse derivative, absent from mathlib with the parent operator; mathlib's univariate normal form is the sharp natDegree_hasseDeriv_le (deg Delta_n p le deg p - n), so upstream should state the sharp per-variable bound degreeOf j (Delta_d P) le degreeOf j P - d j (verified, same 3-line proof) plus a totalDegree companion (verified).
action: Upstream with the parent into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as `degreeOf_hasseDeriv_le : degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j` and `totalDegree_hasseDeriv_le : totalDegree (hasseDeriv d P) ≤ totalDegree P - d.degree`; locally keep the weak form (callers Roth/MainLemma.lean:465,467,491,504 and Roth/CoeffNorm.lean:253 need only the weak bound) or derive it from the sharp one by `.trans tsub_le_self`.
---

# MvPolynomial.degreeOf_hasseDeriv_le

## Inventory entry

### `theorem MvPolynomial.degreeOf_hasseDeriv_le`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R), degreeOf j (hasseDeriv d P) ≤ degreeOf j P`
- **What**: A Hasse derivative `Δ_d` does not increase the degree of a polynomial in any variable `x_j`.
- **How**: `degreeOf_le_iff` reduces to monomials `m` in the support of `Δ_d P`; `coeff_hasseDeriv` rewrites the coefficient as `hasseCoeff d (m + d) * coeff (m + d) P`, so `m + d ∈ P.support` (`right_ne_zero_of_mul`); then `monomial_le_degreeOf j` gives `(m + d) j ≤ degreeOf j P`, and `m j ≤ (m + d) j` closes by `simp`.
- **Hypotheses**: none (section variable `[CommSemiring R]`).
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`
- **Used by**: Roth/MainLemma.lean:465, :467 (`abs_eval_iterated_hasseDeriv_lt_aux`), :491 (`exists_hasseDeriv_index_eval_bound_aux`), :504 (`abs_coeff_diag_hasseDeriv_modByMonic_le_aux`); Roth/CoeffNorm.lean:253 (`degreeOf_det_hasseDeriv_le`). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 210–214, proof length 3 lines
- **Notes**: Mathlib's univariate counterpart is the sharper `Polynomial.natDegree_hasseDeriv_le : natDegree (hasseDeriv n p) ≤ natDegree p - n`; the project form drops the `- d j`.

## Junk check (Step 8)
- Used anywhere? Yes: 5 call sites in 2 files (MainLemma, CoeffNorm), all chaining `.trans` with a degree-box hypothesis.
- Wrapper of 1–2 mathlib calls? No: `hasseDeriv` is not in mathlib; the proof is a 3-line support argument.
- Does mathlib have it? No (Phase 5); only univariate `Polynomial.natDegree_hasseDeriv_le`.
- Too specific / inline? No: 5 call sites, basic API.
- Well-chosen? Statement is correct but weaker than the natural sharp form (evidence item 1).
- Conclusion: `KEEP` — action: keep; upstream in sharp form.

## Mathlibable assessment (Step 9)

Real content (not glue), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` elaborates with no diagnostics)
- decl `MvPolynomial.degreeOf_hasseDeriv_le`: resolved at Roth/HasseDeriv.lean:210
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.degreeOf_hasseDeriv_le` is a theorem stating the following:

For a commutative semiring `R`, a set of variables `σ`, a variable `x_j` and a multi-index `d`, the Hasse derivative `Δ_d P` of any polynomial `P ∈ R[X_σ]` has degree in `x_j` at most the degree of `P` in `x_j`: `deg_{x_j} Δ_d P ≤ deg_{x_j} P`. (In fact `Δ_d` lowers it by at least `d_j`.)

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `R : Type*`, `[CommSemiring R]` — coefficients.
- `j : σ` — the variable whose degree is measured.
- `d : σ →₀ ℕ` — order of the Hasse derivative.
- `P : MvPolynomial σ R` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `deg_{x_j}(Δ_d P) ≤ deg_{x_j}(P)`.

Conclusion (Lean): `degreeOf j (hasseDeriv d P) ≤ degreeOf j P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic degree-bound API lemma about the BIG parent `MvPolynomial.hasseDeriv`; not listed under `## Main results`.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Hasse derivative degree in each variable does not increase multivariate polynomial | partial | multivariate monomial formula `Δ_a x^e = binom(e,a) x^(e-a)` (arXiv 2111.07572, 1509.00279, 1707.01354); each exponent drops by `a_k` | no source states the per-variable bound as a lemma; it is read off the monomial formula |
| 2 | WebSearch (general form) | Hasse derivative degree of i-th Hasse derivative le deg f - i | yes | univariate `deg D^(i) f ≤ deg f − i` (arXiv cs/0508098, 1501.07502; mathlib docs mirror at cs.brown.edu) | the sharp `- i` form is the standard univariate statement and the one mathlib ships |
| 3 | WebSearch (named-after / aliases) | Roth's lemma differential operator degree at most r_j in x_j derivative index | yes | Roth/Ridout/Schmidt arguments keep derivatives in the box `R_m(B; r_1..r_m)` of degree at most `r_j` in `x_j` (arXiv math/0307203, 2502.00731; Roth 1955 Mathematika) | only the weak (box-preserving) form is used there |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `degree` | yes | l.435 (proof of §2 Lemma 2): entries `Δ_μ φ_ν` keep degree at most `r_j` in `x_j`, so the determinant has degree at most `l r_j` | exactly the weak form; implemented by Roth/CoeffNorm.lean:253 |
| 6 | nLab | Hasse-Schmidt derivation | partial | HS derivations / iterativity; no degree statement | degree is not a categorical notion |
| 7 | nCatLab | (same nLab pages) | n/a | — | not a categorical statement (a degree inequality on polynomials) |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry statement; Stacks has no Hasse-derivative tag |
| 9 | MathOverflow / Math.SE | (results of #1, #2) | partial | folklore "Hasse derivatives lower degree" | no dedicated thread |
| 10 | recent arXiv (last 5 years) | (results of #1–#3) | yes | arXiv 2111.07572 (2021), 2502.00731 (2025), 2603.03841 (2026) | all use the monomial formula; degree drop stated in passing |

### Literature summary (Phase 3)

Concept identified as: degree bound for (multivariate) Hasse derivatives; per variable `deg_{x_j} Δ_d P ≤ deg_{x_j} P − d_j` and totally `deg Δ_d P ≤ deg P − |d|`.
Sources agree on the standard form: yes — univariately the standard (and mathlib) form is the sharp `deg D^(n) p ≤ deg p − n`; Roth-type sources use only the weak box-preserving consequence.
Most general standard form: any commutative semiring, any multi-index, sharp per-variable bound with truncated subtraction, plus the total-degree analogue.
Generality dimensions where the literature varies:
  - sharpness: weak `≤ deg P` (Roth sources, this project) vs sharp `≤ deg P − d_j` (coding theory, mathlib univariate); sharp is stronger.
  - degree notion: per variable (`degreeOf`) vs total (`totalDegree`).
Disagreement with the literature: the project's form is the weak consequence of the standard sharp form.

### Generality analysis — `MvPolynomial.degreeOf_hasseDeriv_le`

Literature-standard form (from Phase 3): `degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j` (and `totalDegree (hasseDeriv d P) ≤ totalDegree P - d.degree`).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | `MvPolynomial σ R` requires `CommSemiring R` (parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`) |
| 2 | `σ` | arbitrary | arbitrary | no | — |
| 3 | `j d P` | arbitrary | arbitrary | n/a | no hypotheses |
| 4 | conclusion | `≤ degreeOf j P` | `≤ degreeOf j P - d j` | yes (strengthening) | same 3-line proof with `omega` in place of `simp` (evidence item 1); original is `.trans tsub_le_self` (item 2) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (the conclusion is weaker than the standard sharp bound; no hypotheses to drop).
Number of weakening opportunities found: 0 hypothesis weakenings; 1 verified strengthening of the conclusion (item 1), plus a verified total-degree companion (item 3).
Proposed restatement:

```lean
theorem degreeOf_hasseDeriv_le (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j
```

Cost of restatement: CHEAP — mechanical (evidence item 1 compiles, no diagnostics).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic inequality |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | partial | `hasseDeriv d` maps `restrictDegree`-type submodules (degree box) into themselves; could be stated as `Submodule.map`-inclusion | not needed; the per-variable inequality is mathlib's style (`degreeOf_C_mul_le`, `degreeOf_mul_X_self`) |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | no | not a categorical statement | — |
| 7 | concrete index to general? | yes (normal-form) | sharp `- d j` form matching `Polynomial.natDegree_hasseDeriv_le`, plus `totalDegree_hasseDeriv_le` | same shape as univariate API; immediately gives `hasseDeriv_eq_zero`-type vanishing via degree, and `totalDegree` bounds used in multiplicity arguments |
| 8 | concrete-via-abstract? | no | proof uses only the coefficient formula of `hasseDeriv` | — |
| 9 | false-generalisation guard | no false generalisation | the sharp form implies the current one (item 2); same object, stronger conclusion | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement:
    `theorem degreeOf_hasseDeriv_le (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) : degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j`
    `theorem totalDegree_hasseDeriv_le (d : σ →₀ ℕ) (P : MvPolynomial σ R) : totalDegree (hasseDeriv d P) ≤ totalDegree P - d.degree`
  - Cost: CHEAP
  - Mathlib downstream this enables: mirrors `Polynomial.natDegree_hasseDeriv_le` (so `Polynomial.hasseDeriv_natDegree_eq_C`-style corollaries transfer per variable); the total-degree form plugs into `MvPolynomial.totalDegree` API (`totalDegree_mul`, Schwartz–Zippel / `MvPolynomial.schwartz_zippel_totalDegree`) as used in the method of multiplicities.
  - Real mathematical improvement: the sharp bound carries the information `d_j` that the weak bound discards, and is the form the univariate mathlib API already uses.

### Proof strategy — `MvPolynomial.degreeOf_hasseDeriv_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | the support argument via `degreeOf_le_iff` + `monomial_le_degreeOf` is the standard mathlib pattern (cf. `Polynomial.natDegree_hasseDeriv_le` via `natDegree_sum_le`) | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (the same 3-line proof proves the sharp form, ending in `omega`).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.degreeOf_hasseDeriv_le`

[A] Lean-Finder       "degreeOf j of a derivative of an MvPolynomial is at most degreeOf j of the polynomial"   `MvPolynomial.IsHomogeneous.pderiv`, `Polynomial.degree_derivative_le`, `MvPolynomial.degreeOf_mul_X_self`, `MvPolynomial.degreeOf_le_totalDegree`, `IsWeightedHomogeneous.pderiv`; no `degreeOf` bound for any multivariate derivative
[B] Loogle            `MvPolynomial.degreeOf, Polynomial.hasseDeriv`   no hits
[C] LeanSearch        "degree in a variable of a Hasse derivative of a multivariate polynomial is at most the original degree"   `Polynomial.natDegree_hasseDeriv_le` (univariate, sharp), `MvPolynomial.degreeOf_le_totalDegree`, `Polynomial.degree_derivative_le`; no multivariate hit
[D] Grep mathlib src  `hasseDeriv` occurs only in Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean; `degreeOf_pderiv`, `degreeOf_hasseDeriv`, `totalDegree_pderiv`, `degrees_pderiv`: no hits
[E] Name pattern      `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.totalDegree_hasseDeriv_le` (grep of `.lake/packages/mathlib/Mathlib`)   no hits

Searched for both the user's weak form and the literature-standard sharp / total-degree forms (and the univariate analogue).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); univariate analogue `Polynomial.natDegree_hasseDeriv_le` exists (sharp), and mathlib has not even a `degreeOf` bound for `pderiv`.

### Normal-form check — `MvPolynomial.degreeOf_hasseDeriv_le`

Equivalent formalisms this statement could take: weak `≤ degreeOf j P` (current); sharp `≤ degreeOf j P - d j`; degree-box preservation (`P ∈ restrictDegree`-type submodule implies `Δ_d P` in it); total-degree `≤ totalDegree P - d.degree`.
Does mathlib already have a canonical form for this idea? yes, univariately: `Polynomial.natDegree_hasseDeriv_le` (sharp, truncated subtraction on the RHS).
Our statement is stated against the canonical form? no (weak consequence) → REFACTOR: state the sharp form; the weak form is `.trans tsub_le_self`.
RHS convention respected? yes (bound on the RHS).

### Syntactic generality — `MvPolynomial.degreeOf_hasseDeriv_le`

Alternative restatements attempted:
- sharp per-variable form (evidence item 1, compiles)
- weak form recovered from sharp (item 2, compiles)
- total-degree form (item 3, compiles)
Chosen restatement: ship the sharp form under the name `degreeOf_hasseDeriv_le` (mirroring `Polynomial.natDegree_hasseDeriv_le`), plus `totalDegree_hasseDeriv_le`.
Justification: all 5 call sites use `(degreeOf_hasseDeriv_le ..).trans h`; with the sharp form they become `(degreeOf_hasseDeriv_le ..).trans (tsub_le_self.trans h)`, a trivial adjustment, while the sharp form serves callers that need the drop.

### Superfluous-argument audit — `MvPolynomial.degreeOf_hasseDeriv_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `j`, `d`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (sharp `≤ degreeOf j P - d j`, matching `Polynomial.natDegree_hasseDeriv_le`)
Syntactic generality: OK (callers adapt with `tsub_le_self`)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.degreeOf_hasseDeriv_le`

Internal use count: 5 (outside the declaring file)
External-to-file callers: 2 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:465 | `(degreeOf_hasseDeriv_le j k P).trans (hP j)` (`abs_eval_iterated_hasseDeriv_lt_aux`) |
| Roth/MainLemma.lean:467 | `(fun j ↦ (degreeOf_hasseDeriv_le j i _).trans (hdQ j))` (same lemma) |
| Roth/MainLemma.lean:491 | `fun j ↦ (degreeOf_hasseDeriv_le j k P).trans (hd j)` (`exists_hasseDeriv_index_eval_bound_aux`) |
| Roth/MainLemma.lean:504 | `(degreeOf_hasseDeriv_le k j P).trans (hd k)` (`abs_coeff_diag_hasseDeriv_modByMonic_le_aux`) |
| Roth/CoeffNorm.lean:253 | `(fun (i : Fin l) _ ↦ (degreeOf_hasseDeriv_le _ _ _).trans (hP j))` (`degreeOf_det_hasseDeriv_le`) |

Inline-derivation grep: (none) — `grep -rn "degreeOf.*hasseDeriv" Roth/` finds only these uses, `hasseDeriv_eq_zero_of_degreeOf_lt` (a different statement, Roth/MainLemma.lean:425), `hasseDeriv_mul_of_degreeOf_eq_zero`, and `degreeOf_det_hasseDeriv_le`.

### Composition check (Phase 6)

Can `MvPolynomial.degreeOf_hasseDeriv_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib alone.
  - Mathlib decls used: none applicable — `MvPolynomial.hasseDeriv` is not in mathlib; `Polynomial.natDegree_hasseDeriv_le` is univariate and does not transfer without a `finSuccEquiv`-style transport plus a multi-index decomposition.
  - Result: fails

Attempt 2: from the parent API: `degreeOf_le_iff.2` + `coeff_hasseDeriv` + `monomial_le_degreeOf` (the current 3-line proof).
  - Mathlib decls used: `MvPolynomial.degreeOf_le_iff`, `MvPolynomial.monomial_le_degreeOf`, `right_ne_zero_of_mul`; plus project `coeff_hasseDeriv`.
  - Result: succeeds, but it is a proof (rewrite + support argument), not a composition, and needs the non-mathlib parent.

Conclusion: NOT-COMPOSABLE (from mathlib).

## Verdict: `MvPolynomial.degreeOf_hasseDeriv_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): degree drop of Hasse derivatives is standard in its sharp form (univariate `deg D^(n) f ≤ deg f − n`, multivariate via the monomial formula). Roth-type sources use only the weak box-preserving form (clean.tex l.435).
- Generality analysis (Phase 4): the conclusion is strictly weaker than standard; the sharp form compiles with the same proof (evidence item 1).
- Mathlib search (Phase 5): not in mathlib; univariate sharp analogue `Polynomial.natDegree_hasseDeriv_le` exists.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` is assessed YES-but-generalise-first because mathlib has no multivariate Hasse derivative. A degree bound is part of the minimal API of such an operator: mathlib's univariate file has `natDegree_hasseDeriv_le`, and the Roth development uses this bound at 5 call sites to keep derivatives in the degree box `deg_{x_j} ≤ r_j`. It belongs upstream with the parent.

It should not ship in its current weak form. The univariate normal form is the sharp `natDegree (hasseDeriv n p) ≤ natDegree p - n`. The same 3-line proof gives `degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j` (evidence item 1, `omega` in place of `simp`). The project form then follows by `.trans tsub_le_self` (item 2). A total-degree companion `totalDegree (hasseDeriv d P) ≤ totalDegree P - d.degree` also compiles in 6 lines (item 3).

Reason for the generalisation: LITERATURE-WEAKENING (sharp bound is the literature standard) and MODERN-IDIOM (normal-form alignment with `Polynomial.natDegree_hasseDeriv_le`).
Proposed restatement:
```lean
theorem degreeOf_hasseDeriv_le (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j := by
  refine degreeOf_le_iff.2 fun m hm ↦ ?_
  rw [mem_support_iff, coeff_hasseDeriv] at hm
  have := monomial_le_degreeOf j (mem_support_iff.2 (right_ne_zero_of_mul hm))
  simp only [Finsupp.add_apply] at this
  omega

theorem totalDegree_hasseDeriv_le (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    totalDegree (hasseDeriv d P) ≤ totalDegree P - d.degree
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
  - Per-variable analogue of `Polynomial.natDegree_hasseDeriv_le`, so `Polynomial.hasseDeriv_natDegree_eq_C`-type corollaries have multivariate counterparts (e.g. `Δ_d P` is constant in `x_j` when `d j = degreeOf j P`).
  - `totalDegree_hasseDeriv_le` composes with `MvPolynomial.totalDegree` API (`totalDegree_mul`, `degreeOf_le_totalDegree`, Schwartz–Zippel `MvPolynomial.schwartz_zippel_totalDegree`), as needed in the method of multiplicities.
  - The weak form used by Roth callers is a one-step corollary.
WHY it belongs in mathlib (gap): `Mathlib/Algebra/MvPolynomial/Degrees.lean` and `PDeriv.lean` have no degree bound for any multivariate derivative (not even `degreeOf (pderiv i p) ≤ degreeOf i p - 1`; the only derivative/degree facts are the homogeneity lemmas `IsHomogeneous.pderiv`, `IsWeightedHomogeneous.pderiv`). Any Roth/Siegel-lemma or multiplicity argument that differentiates polynomials inside a degree box needs this.
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new file, with the parent)
PR grouping: ship with `Finsupp.choose`, `MvPolynomial.hasseDeriv`, `coeff_hasseDeriv`, `hasseDeriv_comp`, `pderiv`-compatibility, and `hasseDeriv_eq_zero_of_degreeOf_lt` (its natural companion, analogue of `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree`).
Next action: run `/generalise MvPolynomial.degreeOf_hasseDeriv_le` (target: sharp `- d j` form above, plus `totalDegree_hasseDeriv_le`) before opening a PR.

---

## Next step

Upstream with the parent in sharp form `degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j` plus `totalDegree_hasseDeriv_le`. Locally, optionally replace the project lemma by the sharp form and adjust the 5 callers (Roth/MainLemma.lean:465, :467, :491, :504; Roth/CoeffNorm.lean:253) with `tsub_le_self.trans`; otherwise keep as is.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.degreeOf_hasseDeriv_le/variants.lean`. Final `lean_diagnostic_messages`: success, no diagnostics. It contains:
  - (1) `degreeOf_hasseDeriv_le_sub : degreeOf j (hasseDeriv d P) ≤ degreeOf j P - d j`, same proof skeleton as the project lemma, closing with `omega`.
  - (2) The project statement as `(degreeOf_hasseDeriv_le_sub j d P).trans tsub_le_self`.
  - (3) `totalDegree_hasseDeriv_le : totalDegree (hasseDeriv d P) ≤ totalDegree P - d.degree`, via `Finset.sup_le`, `le_totalDegree` and `map_add Finsupp.degree`.
- Iterations: first draft used a non-existent `totalDegree_le_iff_mem_support`; a later `simp only` made no progress. Both were fixed and rechecked via the LSP, with no cold `lake env lean` run.
- Parent evidence `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/weaken_semiring_fails.lean` (`CommSemiring` forced).
- Loogle `MvPolynomial.degreeOf, Polynomial.hasseDeriv`; LeanSearch and Lean-Finder queries as in [A]–[C]; mathlib grep as in [D]–[E].
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project greps: `grep -rn degreeOf_hasseDeriv_le Roth/` (call sites), `grep -rn "degreeOf.*hasseDeriv" Roth/` (inline derivations: none), and the `.mathlib-quality/references/clean.tex` grep (l.435).
