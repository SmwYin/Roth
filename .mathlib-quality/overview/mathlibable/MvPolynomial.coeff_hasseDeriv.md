---
decl: MvPolynomial.coeff_hasseDeriv
file: Roth/HasseDeriv.lean
line: 89
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The coefficient formula [X^e] Δ_d P = binom(e+d, d) [X^(e+d)] P is the main computational API lemma of the multivariate Hasse derivative (multivariate analogue of Polynomial.hasseDeriv_coeff), absent from mathlib; it should ship with the parent with the coefficient spelled (e + d).choose d via Finsupp.choose.
action: Upstream in the same PR as MvPolynomial.hasseDeriv (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean) restated as ((e + d).choose d : R) * P.coeff (e + d) with Finsupp.choose; locally keep (13 uses in Roth/HasseDeriv.lean and Roth/CoeffNorm.lean:137).
---

# MvPolynomial.coeff_hasseDeriv

## Inventory entry

### `theorem MvPolynomial.coeff_hasseDeriv`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (d e : σ →₀ ℕ) (P : MvPolynomial σ R), coeff e (hasseDeriv d P) = ↑(hasseCoeff d (e + d)) * coeff (e + d) P`
- **What**: The coefficient of `X^e` in `Δ_d P` is `binom(e + d, d)` times the coefficient of `X^(e+d)` in `P`; in particular distinct surviving monomials do not merge under `Δ_d`.
- **How**: Induction on `P` via `MvPolynomial.induction_on'`. Monomial case: `hasseDeriv_monomial`, `coeff_monomial` twice, then a case split on `k = e + d` and on `d ≤ k`, closed by `simp` using `tsub_eq_iff_eq_add_of_le` (when `d ≤ k`) or `hasseCoeff_eq_zero_iff` (when `d ≰ k`). Additive case: `simp [hp, hq, mul_add]`.
- **Hypotheses**: `[CommSemiring R]` (section variable); no other hypotheses.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv_monomial`, `MvPolynomial.hasseCoeff_eq_zero_iff`
- **Used by**: Roth/HasseDeriv.lean: `hasseDeriv_zero_apply` (l.114), `hasseDeriv_map` (l.137), `hasseDeriv_hasseDeriv` (l.178, three rewrites), `pderiv_hasseDeriv` (l.203, two rewrites), `degreeOf_hasseDeriv_le` (l.213), `hasseDeriv_eq_zero_of_degreeOf_lt` (l.222), `uniqueAlgEquiv_hasseDeriv` (l.270); Roth/CoeffNorm.lean: `abs_coeff_hasseDeriv_le` (l.137), which is in turn used in Roth/MainLemma.lean l.468, l.509.
- **Visibility**: public
- **Lines**: 89–101, proof length 11 lines
- **Notes**: Not `@[simp]`. Name follows mathlib's multivariate convention (`MvPolynomial.coeff_pderiv`, `MvPowerSeries.coeff_pderiv`), whereas the univariate analogue is `Polynomial.hasseDeriv_coeff`. Source paper explicitly asks for this identity (clean.tex l.147-151).

## Junk check (Step 8)
- Used anywhere? Yes: 13 occurrences across 2 files (8 distinct declarations), the main interface for `ext`-style proofs about `hasseDeriv`.
- Wrapper of 1–2 mathlib calls? No: an 11-line induction proof about a project definition.
- Does mathlib have it? No: only `Polynomial.hasseDeriv_coeff` and `LaurentSeries.hasseDeriv_coeff` (univariate); no multivariate Hasse derivative (Phase 5).
- Too specific / inline? No: it is the characteristic coefficient lemma of the operator.
- Well-chosen? Yes; matches `Polynomial.hasseDeriv_coeff` modulo the spelling of the binomial (parent-level rename to `Finsupp.choose`).
- Conclusion: `KEEP` — action: keep; upstream with the parent.

## Mathlibable assessment (Step 9)

Not a glue lemma (genuine induction proof), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` compiles with no errors or warnings)
- decl `MvPolynomial.coeff_hasseDeriv`: resolved at Roth/HasseDeriv.lean:89
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.coeff_hasseDeriv` is a theorem stating the following:

Let `R` be a commutative semiring, `P ∈ R[X_σ]`, and `d, e` multi-indices. Then the coefficient of `X^e` in the Hasse derivative `Δ_d P` equals `binom(e + d, d) · [X^(e+d)] P`, where `binom(e+d, d) = ∏_j binom(e_j + d_j, d_j)`. Equivalently `Δ_d (∑_k a_k X^k) = ∑_{k ≥ d} binom(k, d) a_k X^(k-d)` with no collisions among the `X^(k-d)`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `R : Type*`, `[CommSemiring R]` — coefficient ring.
- `d : σ →₀ ℕ` — order of the derivative.
- `e : σ →₀ ℕ` — exponent whose coefficient is extracted.
- `P : MvPolynomial σ R` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `[X^e] Δ_d P = binom(e+d, d) [X^(e+d)] P`.

Conclusion (Lean): `(hasseDeriv d P).coeff e = (hasseCoeff d (e + d) : R) * P.coeff (e + d)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: API lemma of the (BIG) parent definition; listed under `## Main results` of the module docstring, but it is the basic coefficient formula, not a headline theorem.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 11
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multivariate Hasse derivative coefficient formula binom(e+d, d) coefficient of X^(e+d) | yes | `H(F,i) = ∑_{j ≥ i} f_j binom(j,i) X^(j-i)`, multi-index binomial a product, zero when not `i ≤ j` | arXiv 2403.19824, 1412.5012, 1310.6482; the reindexed coefficient form is the immediate consequence |
| 2 | WebSearch (general form) | Hasse-Schmidt derivative power series coefficientwise definition D^(k) f = sum binom(n,k) a_n x^(n-k) | partial | coefficientwise `D^(k) ∑ a_n x^n = ∑ binom(n,k) a_n x^(n-k)`; abstract HS derivations `D_α` indexed by multi-indices | Wikipedia "Hasse–Schmidt derivation", arXiv 1810.08075, 2409.19093; same formula makes sense on power series (see parent evidence) |
| 3 | WebSearch (named-after / aliases) | "Hasse derivative" multi-index polynomial method multiplicity coefficient of P(X+Z) Taylor expansion | yes | `Δ_i P` = coefficient of `Z^i` in `P(X+Z)` | arXiv 0901.2529 (DKSS method of multiplicities), 2403.19824, 1402.0643, 1707.01354; mathlib docs for univariate `Polynomial.hasseDeriv` |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for hasse/binom | yes | l.147-151: "prove the coefficient identity `[X^e]Δ_dP=(∏_j binom(e_j+d_j, d_j))[X^{e+d}]P`", modelled on `Polynomial.hasseDeriv` | project source paper §1 asks for exactly this lemma |
| 6 | nLab | Hasse-Schmidt derivation / Hasse derivative (as in parent report) | partial | several-variable HS derivations; no coefficient formula entry | below nLab's granularity |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | Stacks treats differential operators abstractly, not coefficient formulas of Hasse derivatives on polynomial rings |
| 9 | MathOverflow / Math.SE | (results of #1, #3) | no | — | no dedicated thread surfaced; the formula is treated as immediate from the definition in all sources |
| 10 | recent arXiv (last 5 years) | (results of #1, #3) | yes | arXiv 2403.19824 (2024), 2603.03841 (2026), 2111.07572 (2021) | all use the monomial rule `X^j ↦ binom(j,i) X^(j-i)`, equivalent to this coefficient form |

### Literature summary (Phase 3)

Concept identified as: coefficient formula for the (multivariate) Hasse derivative / divided-power derivative `D^{(d)} = ∂^d / d!`.
Sources agree on the standard form: yes (stated either as the monomial rule or as the expansion `∑_{j≥i} binom(j,i) f_j X^(j-i)`; the coefficient-extraction form is the univariate `Polynomial.hasseDeriv_coeff` shape).
Most general standard form: for a (semi)ring `R` and `f = ∑ a_k X^k` (polynomial or formal power series in finitely many or arbitrarily many variables), `[X^e] D^{(d)} f = binom(e+d, d) a_{e+d}`.
Generality dimensions where the literature varies:
  - object: polynomials vs formal power series; both standard. Power-series version needs only `Semiring R` (parent evidence) but is a different operator in mathlib's organisation.
  - binomial spelling: `binom(e+d, d)` (= `binom(e+d, e)`).
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.coeff_hasseDeriv`

Literature-standard form (from Phase 3): `[X^e] Δ_d f = binom(e+d, d) [X^(e+d)] f` over any (semi)ring, for polynomials or power series.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | any semiring | no (for `MvPolynomial`) | `MvPolynomial σ R` itself requires `CommSemiring R` (parent evidence `weaken_semiring_fails.lean`) |
| 2 | `σ : Type*` | arbitrary | finite set of variables | no (already more general) | — |
| 3 | `d e : σ →₀ ℕ` | finsupp multi-indices | multi-indices | no | — |
| 4 | `P : MvPolynomial σ R` | polynomial | polynomial or power series | companion only | power-series operator is a separate definition (parent evidence: `MvPowerSeries.coeff_hasseDeriv` holds by `rfl` over `Semiring R`) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (as a statement about `MvPolynomial.hasseDeriv`)
Number of weakening opportunities found: 0 hypothesis weakenings; 1 verified restatement (binomial spelled `(e + d).choose d`, inherited from parent; compiles in evidence file).
Cost of restatement: CHEAP

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | no | — | coefficient formula of an operator |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | already a commutative semiring, the minimum for `MvPolynomial` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (inherited from parent) | coefficient spelled `((e + d).choose d : R)` with `Finsupp.choose`, matching `Polynomial.hasseDeriv_coeff : (hasseDeriv k f).coeff n = ((n + k).choose k) * f.coeff (n + k)` | uniform statements with the univariate API; reuse of multi-index binomial lemmas |
| 8 | concrete-via-abstract? | no | proof uses `hasseDeriv_monomial` essentially; the statement is about the specific operator | — |
| 9 | false-generalisation guard | no false generalisation | the restated form is the same proposition up to `rfl` (evidence file `coeff_hasseDeriv'` is proved by the project lemma directly) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `theorem MvPolynomial.coeff_hasseDeriv (d e : σ →₀ ℕ) (P : MvPolynomial σ R) : (hasseDeriv d P).coeff e = ((e + d).choose d : R) * P.coeff (e + d)` with `Finsupp.choose` from the parent report.
  - Cost: CHEAP (compiles in evidence, by the existing lemma)
  - Mathlib downstream this enables: identical shape to `Polynomial.hasseDeriv_coeff` and `LaurentSeries.hasseDeriv_coeff`, so `uniqueAlgEquiv_hasseDeriv`-style transfer lemmas become a rewrite plus `Finsupp.choose_single`; multi-index binomial lemmas apply directly.
  - Real mathematical improvement: the coefficient is the standard multi-index binomial `binom(e+d, d)` rather than a project-specific helper.

### Proof strategy — `MvPolynomial.coeff_hasseDeriv`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | mathlib's univariate proof (`hasseDeriv_apply` + `coeff_sum` + `Finset.sum_eq_single`) also works here (evidence `coeff_hasseDeriv_alt`), but is longer (~20 lines) than the current induction | n/a (keep current) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (induction on monomials with `induction_on'`, short and robust; the alternative sum-based proof mirroring `Polynomial.hasseDeriv_coeff` compiles but is longer).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.coeff_hasseDeriv`

[A] Lean-Finder       "coefficient of e in the d-th multivariate Hasse derivative equals product of binomials times coefficient of e + d"   no multivariate hit (returns `Polynomial.hasseDeriv_coeff`, `LaurentSeries.hasseDeriv_coeff`, `Polynomial.hasseDeriv_apply`, `Polynomial.hasseDeriv_monomial`)
[B] Loogle            `"hasseDeriv", MvPolynomial` no hits; `MvPolynomial.coeff, Finsupp.prod, Nat.choose` query error (Loogle could not resolve `MvPolynomial.coeff` as a constant); parent report: `(_ →₀ ℕ) → (_ →₀ ℕ) → ℕ` no hits
[C] LeanSearch        "coefficient of Hasse derivative of multivariate polynomial equals binomial times coefficient"   only univariate (`Polynomial.hasseDeriv_coeff`, `Polynomial.taylor_coeff`, ...)
[D] Grep mathlib src  `hasseDeriv` across `.lake/packages/mathlib/Mathlib`: only Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean; none in Algebra/MvPolynomial or RingTheory/MvPowerSeries (which have only `coeff_pderiv`)
[E] Name pattern      `MvPolynomial.coeff_hasseDeriv`, `MvPowerSeries.coeff_hasseDeriv` (grep; `lean_local_search` unavailable: ripgrep not installed)   no hits

Searched for both the user's form and the literature-standard form (power series / `choose` spelling).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); the univariate analogue `Polynomial.hasseDeriv_coeff` is the template.

### Normal-form check — `MvPolynomial.coeff_hasseDeriv`

Equivalent formalisms this statement could take: coefficient form `coeff e (Δ_d P) = binom(e+d,d) * coeff (e+d) P`; sum form `Δ_d P = ∑ k ∈ P.support, monomial (k - d) (binom(k,d) * coeff k P)` (`hasseDeriv_apply`); power-series form via coercion.
Does mathlib already have a canonical form for this idea? yes for the univariate case: `Polynomial.hasseDeriv_coeff` (coefficient form, LHS the coefficient of the derivative).
Our statement is stated against the canonical form? yes (same LHS/RHS orientation).
RHS convention respected? yes

### Syntactic generality — `MvPolynomial.coeff_hasseDeriv`

Alternative restatements attempted:
- `((e + d).choose d : R) * P.coeff (e + d)` with `Finsupp.choose` (compiles, evidence `coeff_hasseDeriv'`)
- current `hasseCoeff d (e + d)` form
- name `hasseDeriv_coeff` (univariate convention) vs `coeff_hasseDeriv` (multivariate convention, `MvPolynomial.coeff_pderiv`)
Chosen restatement: `Finsupp.choose` spelling, name `coeff_hasseDeriv` (matches `MvPolynomial.coeff_pderiv`).
Justification: call sites rewrite with it unchanged; the binomial spelling matches the univariate lemma used together with it at l.270.

### Superfluous-argument audit — `MvPolynomial.coeff_hasseDeriv`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `d` | yes | — |
| 3 | `e` | yes | — |
| 4 | `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (binomial spelled `(e + d).choose d`, inherited from parent rename)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.coeff_hasseDeriv`

Internal use count: 1 outside the declaring file (8 distinct callers, 13 occurrences in total)
External-to-file callers: 1 distinct file (Roth/CoeffNorm.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/HasseDeriv.lean:114 | `simp [coeff_hasseDeriv, hasseCoeff]` (in `hasseDeriv_zero_apply`) |
| Roth/HasseDeriv.lean:137 | `simp [coeff_hasseDeriv, coeff_map]` (in `hasseDeriv_map`) |
| Roth/HasseDeriv.lean:178 | `rw [coeff_smul, coeff_hasseDeriv, coeff_hasseDeriv, coeff_hasseDeriv, ...]` (in `hasseDeriv_hasseDeriv`) |
| Roth/HasseDeriv.lean:203 | `rw [coeff_pderiv, coeff_smul, coeff_hasseDeriv, coeff_hasseDeriv, ...]` (in `pderiv_hasseDeriv`) |
| Roth/HasseDeriv.lean:213 | `rw [mem_support_iff, coeff_hasseDeriv] at hm` (in `degreeOf_hasseDeriv_le`) |
| Roth/HasseDeriv.lean:222 | `simp [coeff_hasseDeriv, notMem_support_iff.1 ...]` (in `hasseDeriv_eq_zero_of_degreeOf_lt`) |
| Roth/HasseDeriv.lean:270 | `rw [coeff_uniqueAlgEquiv, coeff_hasseDeriv, Polynomial.hasseDeriv_coeff, ...]` (in `uniqueAlgEquiv_hasseDeriv`) |
| Roth/CoeffNorm.lean:137 | `rw [coeff_hasseDeriv, Int.cast_mul, Int.cast_natCast, abs_mul, Nat.abs_cast]` (in `abs_coeff_hasseDeriv_le`) |

Inline-derivation grep: (none) — no other proof in Roth/ recomputes coefficients of `hasseDeriv` from `hasseDeriv_monomial`/`hasseDeriv_apply` directly.

### Composition check (Phase 6)

Can `MvPolynomial.coeff_hasseDeriv` be derived from mathlib in ≤3 chained calls?

Attempt 1: `hasseDeriv_apply`, `MvPolynomial.coeff_sum`, `Finset.sum_eq_single` (the univariate proof pattern).
  - Mathlib decls used: `MvPolynomial.coeff_sum`, `Finset.sum_eq_single`, `MvPolynomial.coeff_monomial`, `tsub_add_cancel_of_le`
  - Result: succeeds (evidence `coeff_hasseDeriv_alt`) but needs ~20 lines with case splits and the project lemmas `hasseDeriv_apply`, `hasseCoeff_eq_zero_iff`
  - Notes: a real proof, not a composition.

Conclusion: NOT-COMPOSABLE (the operator is not in mathlib; this is its characteristic coefficient lemma).

## Verdict: `MvPolynomial.coeff_hasseDeriv`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard monomial/coefficient rule of the multivariate Hasse derivative (arXiv 0901.2529, 2403.19824, 1310.6482; project paper clean.tex l.147-151 asks for exactly this identity).
- Generality analysis (Phase 4): MAXIMALLY GENERAL as a statement; Phase 4c MODERN-IDIOM: binomial spelled `(e + d).choose d` (verified in evidence).
- Mathlib search (Phase 5): not in mathlib; template `Polynomial.hasseDeriv_coeff`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` was assessed YES-but-generalise-first. This lemma is its coefficient formula, the multivariate counterpart of `Polynomial.hasseDeriv_coeff` and `LaurentSeries.hasseDeriv_coeff`; mathlib has neither the operator nor this formula in `Algebra/MvPolynomial` (only `coeff_pderiv`). It is the main computational interface of the operator: 8 project declarations use it, including the composition rule, the commutation with `pderiv`, degree bounds, compatibility with `map` and with univariate `Polynomial.hasseDeriv`, and the integer coefficient bound in CoeffNorm.lean. Any upstream `MvPolynomial.hasseDeriv` PR needs exactly this lemma.

The "generalise first" part is the mechanical restatement inherited from the parent: spell the coefficient as the multi-index binomial `Finsupp.choose (e + d) d`, which is `rfl`-equal to `hasseCoeff d (e + d)` and gives the same shape as `Polynomial.hasseDeriv_coeff`. No hypothesis can be dropped (`CommSemiring` is forced by `MvPolynomial`); the power-series companion `MvPowerSeries.coeff_hasseDeriv` (over `Semiring R`, `rfl`) is a separate optional addition per the parent report. The current induction proof is short and should be kept.

Reason for the generalisation: MODERN-IDIOM (coefficient spelled with the standard multi-index binomial; Q7), plus Phase 5.5 RESTATE-BEFORE-SHIP.
Proposed restatement:
```lean
theorem MvPolynomial.coeff_hasseDeriv (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (hasseDeriv d P).coeff e = ((e + d).choose d : R) * P.coeff (e + d) := by
  sorry -- port of the current induction proof (verified: the restated form follows from it)
```
Estimated cost of regeneralisation: CHEAP
Mathlib downstream this enables:
- uniform statement with `Polynomial.hasseDeriv_coeff` / `LaurentSeries.hasseDeriv_coeff`, making univariate/multivariate transfer (`uniqueAlgEquiv_hasseDeriv`) a direct rewrite;
- the `ext`-based proofs of the composition rule `hasseDeriv_hasseDeriv` and of `pderiv_hasseDeriv` via multi-index binomial identities (`Finsupp.choose` lemmas);
- coefficient bounds for Hasse derivatives over `ℤ` (as in `abs_coeff_hasseDeriv_le`) and multiplicity statements for multivariate polynomials.
Next action: run `/generalise MvPolynomial.coeff_hasseDeriv` together with the parent; ship in the PR "feat(Algebra/MvPolynomial): multivariate Hasse derivatives" (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean), bundled with `Finsupp.choose`, `hasseDeriv`, `hasseDeriv_monomial`, `hasseDeriv_apply`.

---

## Next step

Ship as `MvPolynomial.coeff_hasseDeriv` with coefficient `((e + d).choose d : R)` in the parent's `MvPolynomial.hasseDeriv` PR (Mathlib/Algebra/MvPolynomial/HasseDeriv.lean); locally keep as is.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.coeff_hasseDeriv/restate_and_altproof.lean` (compiles with `lake env lean`, no errors or warnings): restated `coeff_hasseDeriv'` with `Finsupp.choose (e + d) d` proved by the project lemma; alternative proof `coeff_hasseDeriv_alt` following mathlib's univariate `hasseDeriv_apply` + `coeff_sum` + `Finset.sum_eq_single` pattern.
- Parent evidence `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/generalise_mvpowerseries.lean` (power-series companion, `rfl` coefficient lemma over `Semiring R`) and `weaken_semiring_fails.lean` (`CommSemiring` forced).
- Mathlib grep for `hasseDeriv` (only univariate Polynomial / Taylor / LaurentSeries) and for `coeff_pderiv` naming (Algebra/MvPolynomial/PDeriv.lean:121, RingTheory/MvPowerSeries/Derivative.lean:128).
- LeanSearch, Lean-Finder: univariate hits only; Loogle: one query no hits, one query errored (constant not resolved). `lean_local_search` unavailable (ripgrep not installed); replaced by grep.
- WebSearch: 3 queries (table rows 1-3). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn coeff_hasseDeriv Roth/` for Used-by and call sites.
