---
decl: MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt
file: Roth/HasseDeriv.lean
line: 219
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Multivariate analogue of mathlib's Polynomial.hasseDeriv_eq_zero_of_lt_natDegree, absent with the parent operator; the content is the support criterion (no monomial of P dominates d) which compiles in 4 lines and gives both this per-variable form and a totalDegree form as one-line corollaries.
action: Upstream with the parent into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as core `hasseDeriv_eq_zero_of_forall_not_le` plus corollaries `hasseDeriv_eq_zero_of_degreeOf_lt` (this statement, unchanged) and `hasseDeriv_eq_zero_of_totalDegree_lt`; locally keep as is (callers Roth/Taylor.lean:173,207 and Roth/MainLemma.lean:425 need no change).
---

# MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] {j : σ} {d : σ →₀ ℕ} {P : MvPolynomial σ R}, degreeOf j P < d j → hasseDeriv d P = 0`
- **What**: If the order `d j` of the Hasse derivative `Δ_d` in some variable `x_j` exceeds the degree of `P` in `x_j`, then `Δ_d P = 0`.
- **How**: `ext e`; `coeff_hasseDeriv` turns the coefficient into `hasseCoeff d (e + d) * coeff (e + d) P`. The second factor is zero by `notMem_support_of_degreeOf_lt j`, since `degreeOf j P < d j ≤ (e + d) j` (`simp`). `simp` closes the goal.
- **Hypotheses**: `h : degreeOf j P < d j` (section variable `[CommSemiring R]`).
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`
- **Used by**: Roth/Taylor.lean:173 (`degreeOf_taylor_le`), Roth/Taylor.lean:207 (`eq_sum_box_hasseDeriv`), Roth/MainLemma.lean:425 (`le_index_of_forall_eval_eq_zero`). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 219–223, proof length 3 lines
- **Notes**: This is the multivariate analogue of mathlib's `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree`.

## Junk check (Step 8)
- Used anywhere? Yes: 3 call sites in 2 files (Taylor, MainLemma).
- Wrapper of 1–2 mathlib calls? No. `hasseDeriv` is not in mathlib, and the proof is a short coefficient and support argument.
- Does mathlib have it? No. Mathlib has only the univariate `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree` (Phase 5).
- Too specific / inline? No. It has 3 call sites and is basic API that mirrors mathlib.
- Well-chosen? Yes, as a corollary. The underlying content is the more general support criterion (evidence item 1).
- Conclusion: `KEEP`. Action: keep locally, and upstream together with the support-criterion core lemma.

## Mathlibable assessment (Step 9)

This lemma has real content (it is not glue), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (the project is built per the brief; the evidence file importing `Roth.HasseDeriv` elaborates without errors)
- decl `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`: resolved at Roth/HasseDeriv.lean:219
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` is a theorem stating the following:

Let `R` be a commutative semiring and `P ∈ R[X_σ]`. Let `d` be a multi-index and `x_j` a variable with `deg_{x_j} P < d_j`. Then the Hasse derivative `Δ_d P` is the zero polynomial. The reason is that every monomial `X^k` of `P` has `k_j < d_j`, so the binomial factor `binom(k, d)` vanishes.

Variables / typeclasses involved (Lean side):
- `σ : Type*`: index set of the variables.
- `R : Type*`, `[CommSemiring R]`: the coefficients.
- `j : σ`: the variable whose degree is too small.
- `d : σ →₀ ℕ`: the order of the Hasse derivative.
- `P : MvPolynomial σ R`: the polynomial.

Hypotheses (Lean side):
- `h : degreeOf j P < d j`: in the variable `x_j`, the order of the derivative exceeds the degree.

Conclusion (math): `Δ_d P = 0`.

Conclusion (Lean): `hasseDeriv d P = 0`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a basic vanishing lemma about the BIG parent `MvPolynomial.hasseDeriv`; it is not listed under `## Main results`.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Hasse derivative vanishes order greater than degree multivariate polynomial | partial | binomial `binom(j,i)` vanishes when `j < i`; multivariate Hasse derivative as coefficient of `y^β` in `P(x+y)` (arXiv 1310.6482, 1707.01354, 2511.05176) | no source states the per-variable vanishing as a lemma; it is read off the monomial formula |
| 2 | WebSearch (general form) | Hasse derivative monomial binomial coefficient zero unless i le e, method of multiplicities | yes | multi-index binomial `binom(α,β) = ∏ binom(α_i,β_i)` is zero if some `α_i < β_i` (arXiv 0901.2529 DKSS, 1410.7084, 2403.19824) | general form: `Δ_β` kills every monomial `X^α` with `β` not ≤ `α`, so `Δ_β P = 0` if no monomial of `P` dominates `β` |
| 3 | WebSearch (named-after / aliases) | Roth's lemma index derivatives outside degree box identically zero, degree r_j in x_j | partial | Roth/Ridout/Schmidt: auxiliary polynomial of degree at most `r_h` in `X_h`; index relative to `r` (arXiv math/0307203, uh.edu Roth notes, Evertse Leiden notes) | the derivatives-outside-the-box vanishing is used implicitly |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `degree` / Lemma 9 | yes | l.1511 (proof of Lemma 9): multi-indices outside the degree box give identically zero derivatives | exactly the per-variable form; used at Roth/MainLemma.lean:425 |
| 6 | nLab | Hasse-Schmidt derivative / Hasse-Schmidt derivation (ncatlab.org) | partial | definition; motivation in positive characteristic (`(X^p)' = 0`) | no degree-vanishing statement on the visible page |
| 7 | nCatLab | (same nLab pages) | n/a | — | not a categorical statement; it is a vanishing fact about polynomials |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry statement; Stacks has no Hasse-derivative tag |
| 9 | MathOverflow / Math.SE | Hasse-Schmidt derivation higher derivative vanishes on polynomials of lower degree (combined query) | no | — | no dedicated thread; folklore |
| 10 | recent arXiv (last 5 years) | (results of #1–#3, #6) | yes | arXiv 2305.04537 (2023), 2403.19824 (2024), 2511.05176 (2025), 2609.19009 (2026) | all use the multi-index binomial vanishing convention |

### Literature summary (Phase 3)

Concept identified as: vanishing of high-order (multivariate) Hasse derivatives on polynomials of low degree.
Sources agree on the standard form: yes. Its source is the monomial formula `Δ_β X^α = binom(α, β) X^(α−β)`, with `binom(α, β) = 0` unless `β ≤ α` componentwise.
Most general standard form: `Δ_β P = 0` whenever no monomial `X^α` in the support of `P` satisfies `β ≤ α`. Per-variable degree (`deg_{x_j} P < β_j` for some `j`) and total degree (`deg P < |β|`) are the two common sufficient conditions.
Generality dimensions where the literature varies:
  - degree notion: per variable (Roth-type box arguments, this project) versus total degree (method of multiplicities); the support criterion covers both.
Disagreement with the literature: none. The project form is one of the standard sufficient conditions.

### Generality analysis — `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`

Literature-standard form (from Phase 3): `(∀ k ∈ P.support, ¬ d ≤ k) → hasseDeriv d P = 0`, with the per-variable and total-degree conditions as corollaries.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | `MvPolynomial σ R` requires `CommSemiring R` (parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`) |
| 2 | `σ` | arbitrary | arbitrary | no | — |
| 3 | `h : degreeOf j P < d j` | per-variable degree | no monomial of `P` dominates `d` | yes | strictly weaker hypothesis; verified in evidence item 1, and the current form follows in one line (item 2) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD. The hypothesis is one sufficient condition for the support criterion.
Number of weakening opportunities found: 1 (hypothesis weakened to the support criterion; verified to compile, evidence item 1). It also yields a total-degree companion (item 3).
Proposed restatement:

```lean
theorem hasseDeriv_eq_zero_of_forall_not_le {d : σ →₀ ℕ} {P : MvPolynomial σ R}
    (h : ∀ k ∈ P.support, ¬ d ≤ k) : hasseDeriv d P = 0
```
The current statement is kept as a one-line corollary under its current name.

Cost of restatement: CHEAP. It is mechanical: 4 lines for the core and 2 lines per corollary, all compiled.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | a single numeric hypothesis |
| 2 | sequences to filters? | no | — | algebraic statement |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | partial | equivalently `Δ_d` kills the submodule spanned by monomials `k` with `¬ d ≤ k` | not needed; mathlib states vanishing lemmas elementwise (`Polynomial.hasseDeriv_eq_zero_of_lt_natDegree`) |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | no | not a categorical statement | — |
| 7 | concrete index to general? | yes | support criterion `∀ k ∈ P.support, ¬ d ≤ k` | covers both `degreeOf` and `totalDegree` (`Finsupp.degree`) conditions with one proof |
| 8 | concrete-via-abstract? | yes (mild) | the proof uses only that the coefficient at `e + d` vanishes because `e + d ∉ support`; `degreeOf` is only one route to that | the core lemma is the abstract content |
| 9 | false-generalisation guard | no false generalisation | the support form implies the original (item 2) and is about the same operator | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: core `hasseDeriv_eq_zero_of_forall_not_le (h : ∀ k ∈ P.support, ¬ d ≤ k) : hasseDeriv d P = 0` with corollaries `hasseDeriv_eq_zero_of_degreeOf_lt` (unchanged) and `hasseDeriv_eq_zero_of_totalDegree_lt (h : P.totalDegree < d.degree)`.
  - Cost: CHEAP
  - Mathlib downstream this enables: the `totalDegree` corollary composes with `MvPolynomial.le_totalDegree` / `Finsupp.degree_mono`, which is the vanishing step in method-of-multiplicities arguments (multiplicity Schwartz–Zippel). The per-variable form mirrors `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree`, which mathlib uses to prove `Polynomial.natDegree_hasseDeriv`.
  - Real mathematical improvement: one core lemma replaces two parallel proofs. It states the actual reason for vanishing (the binomial factor kills every non-dominating monomial).

### Proof strategy — `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | coefficient extensionality with `coeff_hasseDeriv` plus `notMem_support_of_degreeOf_lt` is the same pattern as mathlib's univariate proof (`hasseDeriv_apply` plus `le_natDegree_of_mem_supp`) | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. For the general form the same coefficient argument is used, with a `by_cases` on membership in the support.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`

[A] Lean-Finder       "iterated partial derivative of MvPolynomial is zero when order exceeds degreeOf in that variable"   `MvPolynomial.pderiv_eq_zero_of_notMem_vars`, `Polynomial.iterate_derivative_eq_zero`, `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree` (univariate); no multivariate higher-order vanishing lemma
[B] Loogle            `MvPolynomial.degreeOf, MvPolynomial.pderiv`   no hits
[C] LeanSearch        "Hasse derivative of a multivariate polynomial vanishes when the order exceeds the degree in some variable"   `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree`, `Polynomial.hasseDeriv`, `LaurentSeries.hasseDeriv`, `Polynomial.natDegree_hasseDeriv_le`; no multivariate hit
[D] Grep mathlib src  `hasseDeriv` occurs only in Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean; `hasseDeriv_eq_zero_of_degreeOf_lt`, `hasseDeriv_eq_zero_of_totalDegree`, `hasseDeriv_eq_zero_of_forall`: no hits; PDeriv.lean has only `pderiv_eq_zero_of_notMem_vars`
[E] Name pattern      grep of `.lake/packages/mathlib/Mathlib` for `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` and the proposed core/total-degree names   no hits (`lean_local_search` unavailable in this session: ripgrep not on PATH; grep used instead)

Searched for both the user's per-variable form and the literature-standard support / total-degree forms (and the univariate analogue).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). The univariate analogue `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree` exists at Mathlib/Algebra/Polynomial/HasseDeriv.lean:89.

### Normal-form check — `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`

Equivalent formalisms this statement could take: per-variable degree hypothesis (current); support criterion; `∃ j, degreeOf j P < d j` (same content); a submodule-annihilation form.
Does mathlib already have a canonical form for this idea? Yes, univariately: `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree (p) (n) (h : p.natDegree < n) : hasseDeriv n p = 0`.
Our statement is stated against the canonical form? Yes. It is the per-variable analogue, with a degree hypothesis and `= 0` conclusion. The support-criterion core is added underneath.
RHS convention respected? yes (`= 0`).

### Syntactic generality — `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`

Alternative restatements attempted:
- support criterion core (evidence item 1, compiles)
- per-variable corollary (item 2, compiles)
- total-degree corollary (item 3, compiles)
Chosen restatement: ship all three. Keep the per-variable form under its current name with implicit `j`, `d` and `P`.
Justification: all 3 call sites supply `degreeOf j P < d j` via `.trans_lt` (Taylor.lean:207, MainLemma.lean:425) or directly (Taylor.lean:173). The implicit-argument per-variable form is easiest to apply. The core lemma serves other degree notions.

### Superfluous-argument audit — `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `h` | yes | it is the vanishing reason; it could be weakened to the support criterion (above) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (matches the univariate `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree`)
Syntactic generality: RESTATE (add the support-criterion core and the total-degree corollary; keep this form as a corollary)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`

Internal use count: 3 (outside the declaring file)
External-to-file callers: 2 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Taylor.lean:173 | `simp [mem_support_iff, coeff_taylor, hasseDeriv_eq_zero_of_degreeOf_lt h] at he` (`degreeOf_taylor_le`) |
| Roth/Taylor.lean:207 | `rw [hasseDeriv_eq_zero_of_degreeOf_lt ((hP j).trans_lt hj), map_zero]` (`eq_sum_box_hasseDeriv`) |
| Roth/MainLemma.lean:425 | `rw [hasseDeriv_eq_zero_of_degreeOf_lt ((hd j).trans_lt hj), map_zero]` (`le_index_of_forall_eval_eq_zero`) |

Inline-derivation grep: none. `grep -rn "degreeOf.*<\|degreeOf_lt" Roth/` finds only these uses, unrelated `GenWronskian` Kronecker hypotheses, and `Roth/Separation.lean:184` (`notMem_support_of_degreeOf_lt` for a univariate coefficient, not a Hasse-derivative vanishing).

### Composition check (Phase 6)

Can `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib alone.
  - Mathlib decls used: none applicable. `MvPolynomial.hasseDeriv` is not in mathlib, and `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree` is univariate.
  - Result: fails

Attempt 2: from the parent API, via `ext e` + `coeff_hasseDeriv` + `notMem_support_of_degreeOf_lt` (the current proof).
  - Mathlib decls used: `MvPolynomial.notMem_support_of_degreeOf_lt`, `MvPolynomial.notMem_support_iff`; plus project `coeff_hasseDeriv`.
  - Result: succeeds, but it is a short proof rather than a composition, and it needs the parent that is not in mathlib.

Conclusion: NOT-COMPOSABLE (from mathlib).

## Verdict: `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the vanishing comes from the multi-index binomial `binom(α, β) = 0` unless `β ≤ α` (DKSS arXiv 0901.2529 and others). Per-variable and total-degree conditions are both standard. Source clean.tex l.1511 uses the per-variable form.
- Generality analysis (Phase 4): STRICTLY NARROWER. The support criterion compiles (evidence item 1) and implies this form in one line (item 2).
- Mathlib search (Phase 5): not in mathlib. The univariate `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree` exists.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` is assessed YES-but-generalise-first because mathlib has no multivariate Hasse derivative. The vanishing of high-order derivatives is part of the minimal API of such an operator. Mathlib's univariate file has `hasseDeriv_eq_zero_of_lt_natDegree`, used to prove `natDegree_hasseDeriv`. The Roth development uses the multivariate version 3 times, for Taylor expansion over the degree box and for the index bound in Lemma 9. It belongs upstream with the parent.

The mathematical content is more general than the per-variable hypothesis: `Δ_d` kills every monomial `X^k` with `d` not ≤ `k`. Upstream should state that support criterion as the core lemma (4-line proof, evidence item 1). It should derive both this statement (item 2, unchanged name and signature) and a total-degree version (item 3) as one-line corollaries. The total-degree version is the form used in the method of multiplicities.

Reason for the generalisation: LITERATURE-WEAKENING (the support criterion is the standard reason for vanishing) and MODERN-IDIOM (one core lemma with per-variable and total-degree corollaries, mirroring `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree`).
Proposed restatement:
```lean
theorem hasseDeriv_eq_zero_of_forall_not_le {d : σ →₀ ℕ} {P : MvPolynomial σ R}
    (h : ∀ k ∈ P.support, ¬ d ≤ k) : hasseDeriv d P = 0 := by
  ext e
  by_cases he : e + d ∈ P.support
  · exact absurd le_add_self (h _ he)
  · simp [coeff_hasseDeriv, notMem_support_iff.1 he]

theorem hasseDeriv_eq_zero_of_degreeOf_lt {j : σ} {d : σ →₀ ℕ} {P : MvPolynomial σ R}
    (h : degreeOf j P < d j) : hasseDeriv d P = 0 :=
  hasseDeriv_eq_zero_of_forall_not_le fun _ hk hdk ↦
    (h.trans_le (hdk j)).not_ge (monomial_le_degreeOf j hk)

theorem hasseDeriv_eq_zero_of_totalDegree_lt {d : σ →₀ ℕ} {P : MvPolynomial σ R}
    (h : P.totalDegree < d.degree) : hasseDeriv d P = 0 :=
  hasseDeriv_eq_zero_of_forall_not_le fun _ hk hdk ↦
    (h.trans_le (Finsupp.degree_mono hdk)).not_ge (le_totalDegree hk)
```
Estimated cost of regeneralisation: CHEAP. All three compile (evidence file).
Mathlib downstream this enables:
  - A per-variable analogue of `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree`. Together with the sharp `degreeOf_hasseDeriv_le` (sibling report), it gives a multivariate analogue of `Polynomial.natDegree_hasseDeriv`.
  - `hasseDeriv_eq_zero_of_totalDegree_lt` composes with `MvPolynomial.le_totalDegree` / `Finsupp.degree_mono` and the multiplicity API (Schwartz–Zippel with multiplicities, DKSS).
  - Taylor expansion over a degree box (Roth/Taylor.lean `eq_sum_box_hasseDeriv`) uses exactly the per-variable corollary.
WHY it belongs in mathlib (gap): mathlib's `Mathlib/Algebra/MvPolynomial/PDeriv.lean` has only the first-order `pderiv_eq_zero_of_notMem_vars`. It has no vanishing lemma for any higher-order multivariate derivative. Mathlib also has no multivariate Hasse derivative at all (parent report).
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new file, with the parent)
PR grouping: ship with `Finsupp.choose`, `MvPolynomial.hasseDeriv`, `coeff_hasseDeriv`, `hasseDeriv_hasseDeriv`, `pderiv_hasseDeriv`, and the sharp `degreeOf_hasseDeriv_le` (its natural companion).
Next action: run `/generalise MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` (target: the support-criterion core plus the two corollaries above) before opening a PR.

---

## Next step

Upstream with the parent: add the core `hasseDeriv_eq_zero_of_forall_not_le` and derive this lemma (unchanged) and `hasseDeriv_eq_zero_of_totalDegree_lt` from it. Locally, optionally add the core lemma and rederive. The callers Roth/Taylor.lean:173, :207 and Roth/MainLemma.lean:425 need no change.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt/variants.lean`, checked with `lean_diagnostic_messages`: success with no errors. Its only diagnostic was an unused-binder linter warning, since fixed by renaming the binder to `_`; it was not re-run afterwards. It contains:
  - (1) `hasseDeriv_eq_zero_of_forall_not_le`, the support criterion.
  - (2) The project statement as a one-line corollary of (1).
  - (3) `hasseDeriv_eq_zero_of_totalDegree_lt` via `Finsupp.degree_mono` and `le_totalDegree`.
- Iterations: the first draft used a non-existent `coeff_zero` in `rw` and was fixed to put `coeff_hasseDeriv` inside `simp`. There was no cold `lake env lean` run.
- Parent evidence `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/weaken_semiring_fails.lean` (`CommSemiring` forced).
- Searches: Loogle `MvPolynomial.degreeOf, MvPolynomial.pderiv` (no hits); LeanSearch and Lean-Finder queries as in [A] and [C]; mathlib grep as in [D] and [E]. `lean_local_search` was unavailable (ripgrep not on PATH).
- WebSearch: 4 queries (table rows 1–3 and 6/9). ChatGPT MCP: n/a (not configured).
- Project greps: `grep -rn hasseDeriv_eq_zero_of_degreeOf_lt Roth/` (call sites), `grep -rn "degreeOf.*<\|degreeOf_lt" Roth/` (inline derivations: none), and `.mathlib-quality/references/clean.tex` (l.1511).
