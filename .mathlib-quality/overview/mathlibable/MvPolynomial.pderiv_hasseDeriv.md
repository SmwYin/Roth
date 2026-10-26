---
decl: MvPolynomial.pderiv_hasseDeriv
file: Roth/HasseDeriv.lean
line: 200
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The identity d_j Delta_d = (d_j+1) Delta_(d+e_j) is genuine multivariate Hasse-derivative API absent from mathlib, but mathlib's univariate design factors it as hasseDeriv_one plus hasseDeriv_comp, so it should ship as an operator-form corollary of a new hasseDeriv_single_one and the composition law (both verified in evidence).
action: Upstream with the parent into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as `hasseDeriv_single_one : hasseDeriv (single j 1) = (pderiv j).toLinearMap` (coefficient proof, verified) followed by operator form `(pderiv j).toLinearMap ∘ₗ hasseDeriv d = (d j + 1) • hasseDeriv (d + single j 1)` and the pointwise lemma as corollary of hasseDeriv_comp; locally keep as is (callers Roth/GenWronskian.lean:159, Roth/HasseDeriv.lean:291).
---

# MvPolynomial.pderiv_hasseDeriv

## Inventory entry

### `theorem MvPolynomial.pderiv_hasseDeriv`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R), (pderiv j) (hasseDeriv d P) = (↑(d j + 1) : R) • hasseDeriv (d + Finsupp.single j 1) P`
- **What**: A partial derivative of a multivariate Hasse derivative: `∂_j Δ_d P = (d_j + 1) · Δ_{d + e_j} P`.
- **How**: `ext e`, rewrite with `coeff_pderiv`, `coeff_smul` and `coeff_hasseDeriv` (twice), reassociate the multi-indices (`add_assoc`, `add_right_comm`) and casts (`Nat.cast_add_one`, `Nat.cast_mul`), and close with the private absorption identity `hasseCoeff_mul_succ` (itself a specialisation of the private `hasseCoeff_mul_hasseCoeff`, a product of `Nat.choose_mul`).
- **Hypotheses**: none (section variable `[CommSemiring R]`).
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff_mul_succ` (private; via it `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_mul_hasseCoeff`)
- **Used by**: Roth/GenWronskian.lean:159 (`derivative_kronHasse_aux`, in a `simp [..., pderiv_hasseDeriv, ...]` set); Roth/HasseDeriv.lean:291 (`factorial_smul_hasseDeriv_single`, induction step `rw [..., pderiv_hasseDeriv, ...]`). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 200–205, proof length 4 lines
- **Notes**: Listed under `## Main results` of the module docstring. Mathlib's univariate API has no direct analogue (`derivative ∘ hasseDeriv k = (k+1) • hasseDeriv (k+1)` is not stated); there it follows from `Polynomial.hasseDeriv_one` + `Polynomial.hasseDeriv_comp`.

## Junk check (Step 8)
- Used anywhere? Yes: Roth/GenWronskian.lean:159 (chain rule for the Kronecker substitution, paper §2 Lemma 1) and Roth/HasseDeriv.lean:291 (`factorial_smul_hasseDeriv_single`).
- Wrapper of 1–2 mathlib calls? No: mathlib has no multivariate Hasse derivative; even from the project's own API the proof needs the multi-index absorption identity (`simp [coeff_pderiv, coeff_hasseDeriv, hasseCoeff]` does not close it, evidence item 4).
- Does mathlib have it? No (searches below); not even the univariate analogue as a named lemma.
- Too specific / inline? No: it is the basic interaction of `pderiv` with `hasseDeriv`, used twice, and stated in the source paper.
- Well-chosen? Yes; for upstreaming, it is better derived from `hasseDeriv (single j 1) = pderiv j` and the composition law (evidence item 2).
- Conclusion: `KEEP` — action: keep locally; upstream with the parent in operator normal form.

## Mathlibable assessment (Step 9)

Real content (not glue), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` elaborates with no diagnostics)
- decl `MvPolynomial.pderiv_hasseDeriv`: resolved at Roth/HasseDeriv.lean:200
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.pderiv_hasseDeriv` is a theorem stating the following:

For a commutative semiring `R`, a set of variables `σ`, a variable `j ∈ σ` and a multi-index `d ∈ ℕ^(σ)`, the formal partial derivative `∂_j` composed with the Hasse derivative `Δ_d` on `R[X_σ]` is `(d_j + 1)` times the Hasse derivative of order `d + e_j`: `∂_j Δ_d = (d_j + 1) Δ_{d + e_j}`. Since `∂_j = Δ_{e_j}`, this is the special case `Δ_{e_j} Δ_d = binom(d + e_j, e_j) Δ_{d+e_j}` of the iterativity law.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `R : Type*`, `[CommSemiring R]` — coefficients.
- `j : σ` — the variable being differentiated.
- `d : σ →₀ ℕ` — order of the Hasse derivative.
- `P : MvPolynomial σ R` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `∂_j (Δ_d P) = (d_j + 1) · Δ_{d+e_j} P`.

Conclusion (Lean): `pderiv j (hasseDeriv d P) = ((d j + 1 : ℕ) : R) • hasseDeriv (d + Finsupp.single j 1) P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma about the BIG parent `MvPolynomial.hasseDeriv` (listed in the file's `## Main results`, but a corollary of the composition law, not a main result of the project).

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 4
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | partial derivative of Hasse derivative "(i_j+1)" D^(i+e_j) multivariate polynomial | partial | Hasse derivative of order `e_j` is the formal partial `∂_j` (arXiv 1303.0084); monomial action `binom(b,a) x^(b-a)` (arXiv 2112.00792 Lemma 2.14); composition law | no source states `∂_j Δ_d = (d_j+1) Δ_{d+e_j}` verbatim; it is the composition law with one index `e_j` (arXiv 1509.00279, 1412.5012) |
| 2 | WebSearch (general form) | Hasse-Schmidt derivation D_1 D_n = (n+1) D_{n+1} first derivative composed with higher derivation | partial | holds for iterative HS derivations (in particular `D_n = ∂^n/n!` and the canonical one on polynomials); not an axiom for arbitrary HS derivations | arXiv 1903.08985, 2007.14171, 2305.04537 (composition formulas with first-order partials) |
| 3 | WebSearch (named-after / aliases) | divided power derivative ∂ ∂^[n] = (n+1) ∂^[n+1] Hasse derivative first derivative relation | partial | Wikipedia "Hasse derivative"; in char 0 `D^(n) = ∂^n/n!` gives the identity; over any ring it is `(n+1) binom(m,n+1) = (m-n) binom(m,n)` on monomials | Narváez Macarro, *Hasse–Schmidt derivations, divided powers and differential smoothness* (AIF 2009, arXiv 0903.0246) for the divided-power viewpoint |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `\partial_j\Delta_d` | yes | l.305: "Here ∂_jΔ_d=(d_j+1)Δ_{d+e_j} follows directly on monomials" (proof of §2 Lemma 1) | exactly our statement; the call site Roth/GenWronskian.lean:159 implements that proof |
| 6 | nLab | Hasse-Schmidt derivation | yes | HS derivations, iterativity as compatibility with `t ↦ t⊗1 + 1⊗t` | the identity is the `(1, n)` instance of iterativity |
| 7 | nCatLab | (same nLab pages) | partial | no categorical statement beyond iterativity | not needed for a polynomial identity |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry statement; Stacks has no Hasse-derivative tag (differential operators section treats `D^(n)` only abstractly) |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | partial | folklore: `D^(1) D^(n) = (n+1) D^(n+1)` in characteristic-free form | no dedicated thread |
| 10 | recent arXiv (last 5 years) | (results of #1, #2) | yes | arXiv 2305.04537 (2023), 2205.00342 (2022), 2112.00792 (2021) | all derive the identity from the composition law |

### Literature summary (Phase 3)

Concept identified as: interaction of the first-order partial derivative with (multivariate) Hasse derivatives; the `(e_j, d)` instance of the iterativity law `Δ_a Δ_b = binom(a+b, a) Δ_{a+b}` combined with `Δ_{e_j} = ∂_j`.
Sources agree on the standard form: yes — whenever stated, it is `∂_j Δ_d = (d_j+1) Δ_{d+e_j}` (or univariately `D D^(n) = (n+1) D^(n+1)`), and it is obtained from the composition law.
Most general standard form: any commutative (semi)ring, any multi-index; as an operator identity; equally valid for power series and for any iterative HS derivation family.
Generality dimensions where the literature varies:
  - object: polynomials / power series / iterative HS derivations (operator choice is the parent's).
  - presentation: standalone lemma vs immediate corollary of `Δ_{e_j} = ∂_j` + iterativity (most sources, and mathlib's univariate file).
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.pderiv_hasseDeriv`

Literature-standard form (from Phase 3): `∂_j ∘ Δ_d = (d_j+1) Δ_{d+e_j}` on `R[X_σ]`, `R` a commutative semiring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | `MvPolynomial σ R` and `pderiv` require `CommSemiring R` (parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`) |
| 2 | `σ` | arbitrary | finite index set | no (already more general) | — |
| 3 | `j d P` | arbitrary | arbitrary | n/a | no hypotheses |
| 4 | statement level | pointwise, `R`-cast scalar | operator identity, `ℕ`-scalar; derived from `Δ_{e_j} = ∂_j` + composition | yes (form, not hypotheses) | operator form compiles from the current lemma (evidence item 3); the current lemma compiles from `hasseDeriv_single_one` + `hasseDeriv_hasseDeriv` (item 2) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (no hypotheses; typeclass forced by `MvPolynomial`).
Number of weakening opportunities found: 0 hypothesis weakenings; 1 verified restatement (operator normal form, derived via the missing `hasseDeriv_single_one`).
Cost of restatement: CHEAP — mechanical (evidence items 1', 2, 3 compile with no diagnostics).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | partial | operator identity in `Module.End R (MvPolynomial σ R)`: `(pderiv j).toLinearMap ∘ₗ hasseDeriv d = (d j + 1) • hasseDeriv (d + single j 1)` | same shape as `Polynomial.hasseDeriv_comp`; composes with `LinearMap`/`Module.End` rewriting |
| 7 | concrete index to general? | yes (structural) | first state `hasseDeriv (single j 1) = (pderiv j).toLinearMap` (analogue of `Polynomial.hasseDeriv_one`), then this lemma is `hasseDeriv_comp (single j 1) d` with `(d + single j 1).choose (single j 1) = d j + 1` | puts `pderiv` and `hasseDeriv` in one API; `pderiv`-facts transfer to `Δ_{e_j}` and back |
| 8 | concrete-via-abstract? | no | proof uses only the coefficient formula and binomial absorption for these operators | — |
| 9 | false-generalisation guard | no false generalisation | operator and pointwise forms are interderivable (items 2–3); `hasseDeriv_single_one` is a genuine equality (item 1') | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement:
    `theorem hasseDeriv_single_one (j : σ) : hasseDeriv (Finsupp.single j 1) = (pderiv (R := R) j).toLinearMap`
    `theorem pderiv_comp_hasseDeriv (j : σ) (d : σ →₀ ℕ) : (pderiv (R := R) j).toLinearMap ∘ₗ hasseDeriv d = (d j + 1) • hasseDeriv (d + Finsupp.single j 1)`
    with the current pointwise `pderiv_hasseDeriv` kept as a corollary.
  - Cost: CHEAP
  - Mathlib downstream this enables: matches the univariate organisation (`Polynomial.hasseDeriv_one`, `Polynomial.hasseDeriv_comp`, `Polynomial.factorial_smul_hasseDeriv`); `hasseDeriv_single_one` lets `pderiv` lemmas (`pderiv_X`, `pderiv_monomial`, `Derivation` Leibniz) be used for `Δ_{e_j}`; `ℕ`-smul operator identity rewrites inside `Module.End` without `Nat.cast` bookkeeping.
  - Real mathematical improvement: it exposes that the lemma is the `(e_j, d)` instance of iterativity, removing a separate binomial argument (the private `hasseCoeff_mul_succ`) from the upstream file.

### Proof strategy — `MvPolynomial.pderiv_hasseDeriv`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `hasseDeriv_single_one` (analogue of `Polynomial.hasseDeriv_one'`) and the composition law; then the proof is `rw [← hasseDeriv_single_one, hasseDeriv_hasseDeriv]` + a one-line `hasseCoeff` computation (evidence item 2) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED (for the upstream version)
  - Proposed strategy: derive from `hasseDeriv_single_one` + `hasseDeriv_hasseDeriv` instead of a separate coefficient computation with the private `hasseCoeff_mul_succ`.
  - Cost: CHEAP
  - Missing mathlib API (if any): `MvPolynomial.hasseDeriv_single_one` (and the parent operator / composition law, all absent).
  - Would refactoring make the proof strictly shorter / cleaner? yes — it drops the private absorption helper (evidence item 2: 4 lines, no private lemma).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.pderiv_hasseDeriv`

[A] Lean-Finder       "derivative of the k-th Hasse derivative of a polynomial equals (k+1) times the (k+1)-th Hasse derivative"   `Polynomial.factorial_smul_hasseDeriv`, `Polynomial.hasseDeriv_comp`, `Polynomial.hasseDeriv_one'`, `Polynomial.derivativeFinsupp_derivative`; no direct univariate or multivariate statement
[B] Loogle            `Polynomial.derivative, Polynomial.hasseDeriv`   only `Polynomial.hasseDeriv_one`, `Polynomial.hasseDeriv_one'`, `Polynomial.factorial_smul_hasseDeriv`
[C] LeanSearch        "partial derivative of a Hasse derivative equals (d j + 1) times Hasse derivative of order d + single j 1"   `MvPolynomial.pderiv`, `LaurentSeries.derivative_iterate`, `LaurentSeries.hasseDeriv`, `MvPolynomial.pderiv_def`, `Polynomial.hasseDeriv`; nothing combining `pderiv` with a Hasse derivative
[D] Grep mathlib src  `hasseDeriv` occurs only in Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean; `pderiv_hasseDeriv`, `derivative_hasseDeriv`: no hits
[E] Name pattern      `MvPolynomial.pderiv_hasseDeriv`, `Polynomial.derivative_hasseDeriv`, `MvPolynomial.hasseDeriv_single_one` (grep of `.lake/packages/mathlib/Mathlib`)   no hits

Searched for both the user's pointwise form and the literature-standard operator / iterativity form (and the univariate analogue).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); univariate building blocks `Polynomial.hasseDeriv_one` + `Polynomial.hasseDeriv_comp` exist, multivariate operator absent.

### Normal-form check — `MvPolynomial.pderiv_hasseDeriv`

Equivalent formalisms this statement could take: pointwise with `R`-cast (current); operator identity with `ℕ`-smul; `Δ_{e_j} ∘ Δ_d` form via `hasseDeriv_single_one` (an instance of `hasseDeriv_comp`); coefficientwise.
Does mathlib already have a canonical form for this idea? yes, univariately: the idea is expressed through `Polynomial.hasseDeriv_one` and `Polynomial.hasseDeriv_comp` (operator form, `ℕ`-smul), with no standalone `derivative ∘ hasseDeriv` lemma.
Our statement is stated against the canonical form? partially (same content, pointwise, `R`-cast) → REFACTOR: add `hasseDeriv_single_one` and state `pderiv_comp_hasseDeriv` in operator form; keep pointwise as corollary.
RHS convention respected? yes (composite on the LHS, single Hasse derivative on the RHS).

### Syntactic generality — `MvPolynomial.pderiv_hasseDeriv`

Alternative restatements attempted:
- operator form with `ℕ`-smul (evidence item 3, compiles)
- pointwise `R`-cast form (current; recovered from `hasseDeriv_single_one` + `hasseDeriv_hasseDeriv`, item 2)
- `Δ_{e_j} Δ_d = (d_j+1) Δ_{d+e_j}` (instance of the composition law)
Chosen restatement: ship operator `pderiv_comp_hasseDeriv` and keep pointwise `pderiv_hasseDeriv`.
Justification: both call sites (Roth/GenWronskian.lean:159 in a `simp` set, Roth/HasseDeriv.lean:291 by `rw` after `Derivation.map_smul`) need the pointwise `R`-scalar form; the operator form is mathlib's normal form.

### Superfluous-argument audit — `MvPolynomial.pderiv_hasseDeriv`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` and `pderiv` |
| 2 | `j`, `d`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (add `hasseDeriv_single_one`; operator form `pderiv_comp_hasseDeriv`)
Syntactic generality: OK (keep pointwise as corollary)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.pderiv_hasseDeriv`

Internal use count: 1 outside the declaring file (+1 inside it)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/GenWronskian.lean:159 | `simp [kronHasse, kronecker, derivative_aeval, pderiv_hasseDeriv, map_smul, ...]` (`derivative_kronHasse_aux`) |
| Roth/HasseDeriv.lean:291 | `rw [Function.iterate_succ_apply', ← ih, Derivation.map_smul, pderiv_hasseDeriv, smul_smul, ...]` (`factorial_smul_hasseDeriv_single`) |

Inline-derivation grep: (none) — `grep -rn "single j 1" Roth/` finds only the declaration, its private helper `hasseCoeff_mul_succ` (Roth/HasseDeriv.lean:191) and the consumer statement Roth/GenWronskian.lean:156.

### Composition check (Phase 6)

Can `MvPolynomial.pderiv_hasseDeriv` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib alone.
  - Mathlib decls used: none applicable — `MvPolynomial.hasseDeriv` is not in mathlib; `Polynomial.hasseDeriv_one`/`hasseDeriv_comp` are univariate.
  - Result: fails

Attempt 2: from the (to-be-upstreamed) parent API: `rw [← hasseDeriv_single_one, hasseDeriv_hasseDeriv, add_comm]; congr 2; simp [hasseCoeff, Finsupp.prod_single_index, add_comm]` (evidence item 2).
  - Mathlib decls used: none in mathlib today; needs the new `hasseDeriv_single_one` and `hasseDeriv_hasseDeriv`.
  - Result: succeeds (4 lines), but not from current mathlib.
  - Notes: `simp [coeff_pderiv, coeff_hasseDeriv, hasseCoeff]` alone does not close it (evidence item 4).

Conclusion: NOT-COMPOSABLE (from mathlib); a short corollary of new parent API.

## Verdict: `MvPolynomial.pderiv_hasseDeriv`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the identity is used verbatim in the source paper (clean.tex l.305). Elsewhere it appears as the `(e_j, d)` instance of Hasse iterativity combined with `Δ_{e_j} = ∂_j` (arXiv 1303.0084, 1509.00279; HS-derivation literature 2305.04537, 0903.0246).
- Generality analysis (Phase 4): MAXIMALLY GENERAL in hypotheses. Phase 4c/4.6/5.5 found an operator normal form and a cleaner derivation, both verified.
- Mathlib search (Phase 5): not in mathlib, not even univariately as a named lemma.
- Composition check (Phase 6): NOT-COMPOSABLE from mathlib.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` is assessed YES-but-generalise-first because mathlib has no multivariate Hasse derivative. This lemma is the basic link between that operator and mathlib's existing `MvPolynomial.pderiv`. It is what the chain rule for the Kronecker substitution needs (Roth/GenWronskian.lean:159). It is also what gives `n! Δ_{n e_j} = ∂_j^n` (Roth/HasseDeriv.lean:291), the multivariate analogue of `Polynomial.factorial_smul_hasseDeriv`. It belongs in the upstream file.

It should not ship in its current shape, as a standalone coefficient computation through the private absorption identity `hasseCoeff_mul_succ`. Mathlib's univariate file states `hasseDeriv_one : hasseDeriv 1 = derivative` and the operator law `hasseDeriv_comp`, and has no separate `derivative ∘ hasseDeriv` lemma. The multivariate file should do the same. First comes `hasseDeriv_single_one : hasseDeriv (single j 1) = (pderiv j).toLinearMap`, which is currently missing in the project too and has a direct coefficient proof (evidence item 1'). Then this lemma becomes a 4-line corollary of the composition law (item 2), stated as an operator identity (item 3), with the pointwise form kept for `rw`/`simp` call sites.

Reason for the generalisation: MODERN-IDIOM (Bourbaki 2.0) — normal-form alignment with `Polynomial.hasseDeriv_one`/`Polynomial.hasseDeriv_comp`, plus the missing `hasseDeriv_single_one` API.
Proposed restatement:
```lean
theorem hasseDeriv_single_one (j : σ) :
    hasseDeriv (Finsupp.single j 1) = (pderiv (R := R) j).toLinearMap := by
  ext ... -- coefficient proof verified pointwise in evidence item 1'

theorem pderiv_comp_hasseDeriv (j : σ) (d : σ →₀ ℕ) :
    (pderiv (R := R) j).toLinearMap ∘ₗ hasseDeriv d =
      (d j + 1) • hasseDeriv (d + Finsupp.single j 1) := by
  -- from hasseDeriv_single_one + hasseDeriv_comp (evidence items 2, 3)

theorem pderiv_hasseDeriv (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    pderiv j (hasseDeriv d P) = ((d j + 1 : ℕ) : R) • hasseDeriv (d + Finsupp.single j 1) P
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
  - `hasseDeriv_single_one` lets the whole `MvPolynomial.pderiv` API (`pderiv_X`, `pderiv_monomial`, Leibniz via `Derivation`) be used for `Δ_{e_j}`, mirroring how `Polynomial.hasseDeriv_one` connects to `Polynomial.derivative`.
  - The operator form rewrites in `Module.End R (MvPolynomial σ R)` alongside `hasseDeriv_comp`, in `ℕ`-smul without casts.
  - The multivariate `factorial_smul_hasseDeriv_single` (analogue of `Polynomial.factorial_smul_hasseDeriv`) follows by induction from it.
  - The private `hasseCoeff_mul_succ` is no longer needed upstream.
WHY it belongs in mathlib (gap): `Mathlib/Algebra/MvPolynomial/PDeriv.lean` has partial derivatives but nothing relating them to higher-order (Hasse) derivatives. Any characteristic-free chain-rule / Taylor / multiplicity argument over `MvPolynomial` (Roth's lemma, the method of multiplicities) needs `∂_j Δ_d = (d_j+1) Δ_{d+e_j}`, and today it has no statement.
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new file, with the parent)
PR grouping: ship with `Finsupp.choose`, `MvPolynomial.hasseDeriv`, `coeff_hasseDeriv`, `hasseDeriv_comp`/`hasseDeriv_hasseDeriv`, the new `hasseDeriv_single_one`, and `factorial_smul_hasseDeriv_single`.
Next action: run `/generalise MvPolynomial.pderiv_hasseDeriv` (target: `hasseDeriv_single_one` + operator form above) before opening a PR.

---

## Next step

Upstream with the parent: add `hasseDeriv_single_one` (coefficient proof) and `pderiv_comp_hasseDeriv` in operator form derived from the composition law, keeping `pderiv_hasseDeriv` as its pointwise corollary. Locally no change is needed. Both call sites (Roth/GenWronskian.lean:159, Roth/HasseDeriv.lean:291) use the pointwise form. Optionally, add `hasseDeriv_single_one` to Roth/HasseDeriv.lean as well.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.pderiv_hasseDeriv/variants.lean`. Final `lean_diagnostic_messages`: success, no diagnostics. It contains:
  - (1) `hasseDeriv_single_one_apply : hasseDeriv (single j 1) P = pderiv j P`, from `factorial_smul_hasseDeriv_single j 1`.
  - (1') The same statement proved directly by `ext e; simp [coeff_hasseDeriv, coeff_pderiv, hasseCoeff, Finsupp.prod_single_index, mul_comm]`, with no dependence on `pderiv_hasseDeriv`.
  - (2) The pointwise `pderiv_hasseDeriv` recovered from (1) + `hasseDeriv_hasseDeriv` in 4 lines.
  - (3) The operator form `(pderiv j).toLinearMap ∘ₗ hasseDeriv d = (d j + 1) • hasseDeriv (d + single j 1)` via `LinearMap.ext` + `rw [LinearMap.comp_apply, LinearMap.smul_apply, Derivation.coeFn_coe, pderiv_hasseDeriv, Nat.cast_smul_eq_nsmul]`.
  - (4) `fail_if_success (simp [coeff_pderiv, coeff_hasseDeriv, hasseCoeff]; done)`, which confirms the coefficient API alone does not close the identity.
- Iterations: first draft had a coercion error in (3) and an unknown identifier in (4); a `simp` attempt for (3) left a cast goal, and `Derivation.toLinearMap_apply` does not exist. All were fixed and rechecked via the LSP, with no cold `lake env lean` run.
- Parent evidence `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/weaken_semiring_fails.lean` (`CommSemiring` forced).
- Loogle `Polynomial.derivative, Polynomial.hasseDeriv`; LeanSearch and Lean-Finder queries as in [A]–[C]; mathlib grep as in [D]–[E].
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project greps: `grep -rn pderiv_hasseDeriv Roth/` (call sites), `grep -rn "single j 1" Roth/` (inline derivations: none), and the `.mathlib-quality/references/clean.tex` grep (l.305).
