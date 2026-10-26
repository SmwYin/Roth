---
decl: MvPolynomial.hasseDeriv_hasseDeriv
file: Roth/HasseDeriv.lean
line: 175
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The iterativity/composition rule Delta_d Delta_e = binom(d+e,d) Delta_(d+e) is the standard defining property of (iterative) Hasse derivatives and is absent from mathlib for MvPolynomial; it should ship in the operator normal form of Polynomial.hasseDeriv_comp (LinearMap comp, Nat-smul, Finsupp.choose coefficient) with the pointwise form as a corollary.
action: Upstream with the parent into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as `hasseDeriv_comp : hasseDeriv d ∘ₗ hasseDeriv e = (d + e).choose d • hasseDeriv (d + e)` plus pointwise `hasseDeriv_hasseDeriv` corollary (verified in evidence variants.lean) and public Finsupp.choose_mul; locally keep as is (callers Roth/Index.lean:113, Roth/HasseDeriv.lean:187).
---

# MvPolynomial.hasseDeriv_hasseDeriv

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_hasseDeriv`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (d e : σ →₀ ℕ) (P : MvPolynomial σ R), hasseDeriv d (hasseDeriv e P) = (↑(hasseCoeff d (d + e)) : R) • hasseDeriv (d + e) P`
- **What**: Composition rule for multivariate Hasse derivatives: `Δ_d Δ_e P = binom(d+e, d) · Δ_{d+e} P`, with the multi-index binomial `binom(d+e,d) = ∏_j binom(d_j+e_j, d_j)`.
- **How**: `ext f`, then rewrite the three coefficients with `coeff_hasseDeriv` (and `coeff_smul`, `smul_eq_mul`), regroup with `mul_assoc`/`Nat.cast_mul`, and close with the private multi-index binomial identity `hasseCoeff_mul_hasseCoeff` (a product of `Nat.choose_mul`) plus `add_assoc`.
- **Hypotheses**: none (section variable `[CommSemiring R]`).
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff_mul_hasseCoeff` (private)
- **Used by**: Roth/Index.lean:113 (`index_sub_weight_le_index_hasseDeriv`, `rw [hasseDeriv_hasseDeriv, smul_eq_C_mul, ...] at hi`); Roth/HasseDeriv.lean:187 (`hasseDeriv_hasseDeriv_of_disjoint`, which in turn is used at Roth/Separation.lean:156 in `hasseDeriv_rename_mul_aeval`). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 175–179, proof length 3 lines
- **Notes**: Mathlib's univariate counterpart is `Polynomial.hasseDeriv_comp` (operator form, `ℕ`-smul); `LaurentSeries.hasseDeriv_comp` is pointwise with `ℕ`-smul. The project form is pointwise with an `R`-cast scalar.

## Junk check (Step 8)
- Used anywhere? Yes: directly at Roth/Index.lean:113 (index of a derivative, paper Lemma `index-of-derivative`) and via `hasseDeriv_hasseDeriv_of_disjoint` (Roth/HasseDeriv.lean:187, used at Roth/Separation.lean:156).
- Wrapper of 1–2 mathlib calls? No: it needs the coefficient formula plus the multi-index binomial identity (a support-aligned product of `Nat.choose_mul`); `simp [coeff_hasseDeriv, hasseCoeff]` leaves that identity open (evidence item 3).
- Does mathlib have it? No: only univariate `Polynomial.hasseDeriv_comp` and `LaurentSeries.hasseDeriv_comp(_coeff)`; no multivariate Hasse derivative at all.
- Too specific / inline? No: it is the basic iterativity law of the operator.
- Well-chosen? Yes; for upstreaming, add the operator-level form matching `Polynomial.hasseDeriv_comp`.
- Conclusion: `KEEP` — action: keep; upstream with the parent in operator normal form.

## Mathlibable assessment (Step 9)

Real content (not glue), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` elaborates with no diagnostics)
- decl `MvPolynomial.hasseDeriv_hasseDeriv`: resolved at Roth/HasseDeriv.lean:175
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus (listed under `## Main results`).

### Statement (Phase 1)

`MvPolynomial.hasseDeriv_hasseDeriv` is a theorem stating the following:

For a commutative semiring `R`, variables `σ`, and multi-indices `d, e ∈ ℕ^(σ)`, the Hasse derivatives on `R[X_σ]` satisfy the iterativity (composition) law `Δ_d ∘ Δ_e = binom(d+e, d) · Δ_{d+e}`, where `binom(d+e, d) = ∏_j binom(d_j+e_j, d_j)`. In particular Hasse derivatives commute, and `Δ_d Δ_e = Δ_{d+e}` when `d` and `e` have disjoint supports.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `R : Type*`, `[CommSemiring R]` — coefficients.
- `d e : σ →₀ ℕ` — orders of the two derivatives.
- `P : MvPolynomial σ R` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `Δ_d Δ_e P = binom(d+e,d) Δ_{d+e} P`.

Conclusion (Lean): `hasseDeriv d (hasseDeriv e P) = (hasseCoeff d (d + e) : R) • hasseDeriv (d + e) P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma of the BIG parent `MvPolynomial.hasseDeriv` (listed in the file's `## Main results`, but not a main result of the project).

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Hasse derivative composition rule D^(i) D^(j) = binom(i+j, i) D^(i+j) multivariate | yes | univariate `D^(k) D^(l) = binom(k+l,k) D^(k+l)` (Wikipedia "Hasse derivative"; mathlib docs `hasse_deriv_comp`); multivariate Hasse derivative = coeff of `Z^i` in `F(X+Z)` with componentwise multi-index binomials | arXiv 2403.19824, 1412.5012, 2003.09694 (multivariate HS derivations on exterior algebras) |
| 2 | WebSearch (general form) | Hasse-Schmidt derivation iterative higher derivation D_i D_j = binom(i+j,i) D_{i+j} | yes | an HS derivation `(D_k)` is *iterative* iff `D_a D_b = binom(a+b, b) D_{a+b}`; with several commuting HS derivations, the multi-index version | arXiv math/0510235 (Moosa–Scanlon prolongations), 0908.4230, 1412.2224; Matsumura strong integrability. Our lemma says the canonical HS derivation of `R[X_σ]` is iterative |
| 3 | WebSearch (named-after / aliases) | "Hasse derivatives" product rule composition binom multiplicity method polynomial several variables lemma | yes | DKSS method-of-multiplicities toolkit: `(f^(i))^(j) = binom(i+j, i) f^(i+j)` alongside the product rule; multi-index binomials componentwise | arXiv 1909.02431, 1909.03180, 1303.0084 (Lemma 5.4 product rule section), 2603.03841 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for hasse / index-of-derivative | yes | l.571–584, proof of Lemma `index-of-derivative`: "The Hasse composition identity gives `Δ_i Δ_k P = (∏_j binom(i_j+k_j, i_j)) Δ_{i+k} P`" | exactly our statement; the project's call site Roth/Index.lean:113 is that proof |
| 6 | nLab | Hasse-Schmidt derivation / Hasse-Schmidt derivative | yes | HS derivations as ring maps `A → A[[t]]`; iterativity as compatibility with the comultiplication `t ↦ t ⊗ 1 + 1 ⊗ t` | the multi-index composition law is the multivariate iterativity |
| 7 | nCatLab | (same nLab pages) | partial | iterativity = coaction of the additive formal group | no further categorical statement needed for a polynomial-ring identity |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry statement; Stacks has no Hasse-derivative tag |
| 9 | MathOverflow / Math.SE | (results of #3) | partial | same `binom(i+j,i)` composition law, stated as folklore | no dedicated thread |
| 10 | recent arXiv (last 5 years) | (results of #1, #3) | yes | arXiv 2403.19824 (2024), 2603.03841 (2026), 2204.01665 (2022) | all use the componentwise multi-index binomial |

### Literature summary (Phase 3)

Concept identified as: iterativity / composition law of (multivariate) Hasse derivatives; abstractly, the canonical HS derivation of `R[X_σ]` is iterative.
Sources agree on the standard form: yes — `D^(i) D^(j) = binom(i+j, i) D^(i+j)` with componentwise multi-index binomial.
Most general standard form: for any commutative (semi)ring and any multi-indices; as an operator identity (not just pointwise); for power series and abstract iterative HS derivations as well.
Generality dimensions where the literature varies:
  - object: polynomials / power series / abstract HS derivations (operator choice belongs to the parent report).
  - form: operator identity (most sources; mathlib's `Polynomial.hasseDeriv_comp`) vs pointwise (LaurentSeries, our lemma).
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.hasseDeriv_hasseDeriv`

Literature-standard form (from Phase 3): `Δ_d ∘ Δ_e = binom(d+e,d) Δ_{d+e}` on `R[X_σ]`, `R` a commutative semiring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | `MvPolynomial σ R` requires `CommSemiring R` (parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`) |
| 2 | `σ` | arbitrary | finite index set | no (already more general) | — |
| 3 | `d e P` | arbitrary | arbitrary | n/a | no hypotheses |
| 4 | statement level | pointwise in `P`, `R`-cast scalar | operator identity, `ℕ`-scalar | yes (form, not hypotheses) | operator form compiles from the current lemma in 2 lines (evidence item 1) and implies it back (item 2) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (no hypotheses to drop; typeclass forced by `MvPolynomial`).
Number of weakening opportunities found: 0 hypothesis weakenings; 1 verified restatement to operator normal form (see 4c / 5.5).
Cost of restatement: CHEAP — mechanical (evidence items 1–2 compile with no diagnostics).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | partial | operator identity in `Module.End R (MvPolynomial σ R)`: `hasseDeriv d ∘ₗ hasseDeriv e = (d + e).choose d • hasseDeriv (d + e)` | matches `Polynomial.hasseDeriv_comp`; composes with `LinearMap` algebra (`LinearMap.comp_smul`, `Module.End` commutation) |
| 7 | concrete index to general? | yes (coefficient spelling) | write the scalar as `(d + e).choose d` with the parent's `Finsupp.choose` instead of `hasseCoeff d (d + e)` | statement then reads verbatim like `Polynomial.hasseDeriv_comp` with `Nat.choose` replaced by `Finsupp.choose`; a public `Finsupp.choose_mul` replaces the private `hasseCoeff_mul_hasseCoeff` |
| 8 | concrete-via-abstract? | no | proof uses only the coefficient formula and binomial algebra about the operator itself | — |
| 9 | false-generalisation guard | no false generalisation | the operator form and the pointwise form are interderivable (evidence items 1–2); `Finsupp.choose` is `rfl`-equal to `hasseCoeff` with swapped arguments (parent evidence) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement:
    `theorem hasseDeriv_comp (d e : σ →₀ ℕ) : (hasseDeriv d : MvPolynomial σ R →ₗ[R] _) ∘ₗ hasseDeriv e = (d + e).choose d • hasseDeriv (d + e)`
    with the pointwise `hasseDeriv_hasseDeriv` kept as a corollary.
  - Cost: CHEAP
  - Mathlib downstream this enables: same normal form as `Polynomial.hasseDeriv_comp` (so `uniqueAlgEquiv_hasseDeriv` transports one to the other), `LinearMap`/`Module.End` rewriting (commutation `hasseDeriv d ∘ₗ hasseDeriv e = hasseDeriv e ∘ₗ hasseDeriv d`), `ℕ`-smul avoids `Nat.cast` bookkeeping.
  - Real mathematical improvement: it states the iterativity law as an identity of operators, the form in which the literature defines iterative HS derivations and mathlib states the univariate law.

### Proof strategy — `MvPolynomial.hasseDeriv_hasseDeriv`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | (a Taylor-expansion proof via `P(X+Y+Z)` exists in the literature but needs absent multivariate Taylor API) | — |
| 5 | missing mathlib helpers | yes | multi-index `Finsupp.choose_mul` (the private `hasseCoeff_mul_hasseCoeff`, a product of `Nat.choose_mul`) should be public API with the parent's `Finsupp.choose` | CHEAP (proof exists; file with `Finsupp.choose`) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (ext + coefficient formula, same as `LaurentSeries.hasseDeriv_comp_coeff`)
  - Missing mathlib API: `Finsupp.choose_mul` (multi-index `Nat.choose_mul`), to be shipped with `Finsupp.choose`.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.hasseDeriv_hasseDeriv`

[A] Lean-Finder       "iterated Hasse derivative D_d (D_e P) = binom(d+e, d) D_{d+e} P for multivariate polynomials"   `Polynomial.hasseDeriv_comp`, `LaurentSeries.hasseDeriv_comp`, `LaurentSeries.hasseDeriv_comp_coeff`, `Polynomial.hasseDeriv_coeff`; nothing multivariate
[B] Loogle            `"hasseDeriv_comp"`   `Polynomial.hasseDeriv_comp`, `LaurentSeries.hasseDeriv_comp`, `LaurentSeries.hasseDeriv_comp_coeff` only
[C] LeanSearch        "composition of Hasse derivatives of multivariate polynomials equals binomial coefficient times Hasse derivative of sum"   `Polynomial.hasseDeriv_comp`, `LaurentSeries.hasseDeriv_comp_coeff`, `Polynomial.iterate_derivative_mul`, `MvPolynomial.mkDerivation`; nothing multivariate
[D] Grep mathlib src  `hasseDeriv` (files: Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean only), `MvPolynomial.hasseDeriv`, `hasseDeriv_hasseDeriv`, `HasseSchmidt`, `IterativeDerivation`: no multivariate hits
[E] Name pattern      `MvPolynomial.hasseDeriv_comp`, `MvPolynomial.hasseDeriv_hasseDeriv` (grep of `.lake/packages/mathlib/Mathlib`)   no hits

Searched for both the user's pointwise form and the literature-standard operator / iterative-HS-derivation form.

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); `Polynomial.hasseDeriv_comp` is the univariate template, and the parent operator itself is absent.

### Normal-form check — `MvPolynomial.hasseDeriv_hasseDeriv`

Equivalent formalisms this statement could take: pointwise with `R`-cast scalar (current); pointwise with `ℕ`-smul (`LaurentSeries.hasseDeriv_comp`); operator identity with `ℕ`-smul (`Polynomial.hasseDeriv_comp`); coefficientwise (`LaurentSeries.hasseDeriv_comp_coeff`).
Does mathlib already have a canonical form for this idea? yes: `Polynomial.hasseDeriv_comp : hasseDeriv k ∘ₗ hasseDeriv l = (k + l).choose k • hasseDeriv (k + l)`.
Our statement is stated against the canonical form? partially (same orientation, but pointwise and with an `R`-cast scalar) → REFACTOR: primary statement `hasseDeriv_comp` in operator form; pointwise lemma as a corollary.
RHS convention respected? yes (composite on the LHS, single derivative on the RHS).

### Syntactic generality — `MvPolynomial.hasseDeriv_hasseDeriv`

Alternative restatements attempted:
- operator form with `ℕ`-smul (evidence item 1, compiles)
- pointwise `R`-cast form (current; recovered from operator form, evidence item 2)
- pointwise `ℕ`-smul form (LaurentSeries shape)
Chosen restatement: ship both — operator `hasseDeriv_comp` (normal form) and pointwise `hasseDeriv_hasseDeriv` (current, `R`-cast).
Justification: the call site Roth/Index.lean:113 rewrites with the pointwise form and immediately uses `smul_eq_C_mul`, which needs an `R`-scalar; the operator form is the canonical one for mathlib.

### Superfluous-argument audit — `MvPolynomial.hasseDeriv_hasseDeriv`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `d`, `e`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (add operator form `hasseDeriv_comp` matching `Polynomial.hasseDeriv_comp`)
Syntactic generality: OK (keep pointwise as corollary)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.hasseDeriv_hasseDeriv`

Internal use count: 1 outside the declaring file (+1 inside it)
External-to-file callers: 1 distinct file (plus 1 indirect via `hasseDeriv_hasseDeriv_of_disjoint`)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:113 | `rw [hasseDeriv_hasseDeriv, smul_eq_C_mul, map_mul, eval_C, mul_ne_zero_iff] at hi` (`index_sub_weight_le_index_hasseDeriv`) |
| Roth/HasseDeriv.lean:187 | `rw [hasseDeriv_hasseDeriv, show hasseCoeff d (d + e) = 1 from ...]` (`hasseDeriv_hasseDeriv_of_disjoint`) |
| Roth/Separation.lean:156 (indirect) | `rw [← hasseDeriv_hasseDeriv_of_disjoint hdisj, ...]` (`hasseDeriv_rename_mul_aeval`) |

Inline-derivation grep: (none) — `grep -rn "hasseDeriv .*(hasseDeriv"` over `Roth/` finds only statements at Roth/MainLemma.lean:462–701 that bound `|eval (Δ_i Δ_k P)|` directly without re-deriving the composition, and Roth/GenWronskian.lean:216 (univariate `Polynomial.hasseDeriv`).

### Composition check (Phase 6)

Can `MvPolynomial.hasseDeriv_hasseDeriv` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib alone.
  - Mathlib decls used: none applicable — `MvPolynomial.hasseDeriv` is not in mathlib; `Polynomial.hasseDeriv_comp` is univariate.
  - Result: fails

Attempt 2: `ext f; simp [coeff_hasseDeriv, hasseCoeff]` from the parent's API.
  - Result: fails — leaves `binom(f+d,d) binom(f+d+e,e) = binom(d+e,d) binom(f+d+e,d+e)` over `Finsupp.prod` (evidence item 3); closing it needs the 13-line support-aligned `Nat.choose_mul` argument.

Conclusion: NOT-COMPOSABLE

## Verdict: `MvPolynomial.hasseDeriv_hasseDeriv`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): iterativity `D^(i) D^(j) = binom(i+j,i) D^(i+j)` is the defining law of iterative HS derivations (arXiv math/0510235, 1412.2224) and a standard tool of the method of multiplicities (arXiv 1909.02431, 1909.03180); the source paper uses it verbatim (clean.tex l.579–582).
- Generality analysis (Phase 4): MAXIMALLY GENERAL in hypotheses; Phase 4c/5.5: operator normal form available and verified.
- Mathlib search (Phase 5): not in mathlib; template `Polynomial.hasseDeriv_comp`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` was assessed YES-but-generalise-first (absent from mathlib; ship with `Finsupp.choose`). The composition law is the operator's most important structural identity: it is what makes the canonical HS derivation of `R[X_σ]` iterative, it gives commutation of Hasse derivatives, and in the project it drives the index-of-derivative lemma (Roth/Index.lean:113) and, via the disjoint-support corollary, the separation-of-variables argument (Roth/Separation.lean:156). Its proof carries genuine content (the multi-index `Nat.choose_mul`), so it is not composable from the coefficient API by `simp`.

The bucket is generalise-first for reason MODERN-IDIOM (normal form), not hypothesis weakening: mathlib states the univariate law as an operator identity with an `ℕ` scalar, `Polynomial.hasseDeriv_comp`. The multivariate version should be stated the same way, with the scalar spelled `(d + e).choose d` via the parent's `Finsupp.choose`. The current pointwise `R`-cast lemma then stays as a corollary for `rw`-style call sites. Evidence items 1–2 verify that the two forms imply each other in two lines each.

Reason for the generalisation: MODERN-IDIOM (Bourbaki 2.0) — normal-form alignment with `Polynomial.hasseDeriv_comp`.
Proposed restatement:
```lean
theorem hasseDeriv_comp (d e : σ →₀ ℕ) :
    (hasseDeriv d : MvPolynomial σ R →ₗ[R] _) ∘ₗ hasseDeriv e =
      (d + e).choose d • hasseDeriv (d + e) := by
  refine LinearMap.ext fun P ↦ ?_
  simp [hasseDeriv_hasseDeriv, Nat.cast_smul_eq_nsmul]  -- verified with hasseCoeff d (d + e) in evidence

theorem hasseDeriv_hasseDeriv (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d (hasseDeriv e P) = ((d + e).choose d : R) • hasseDeriv (d + e) P := ...
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
  - same normal form as `Polynomial.hasseDeriv_comp`, so `uniqueAlgEquiv_hasseDeriv` transports between univariate and multivariate statements;
  - `LinearMap`/`Module.End` rewriting, including commutation `hasseDeriv d ∘ₗ hasseDeriv e = hasseDeriv e ∘ₗ hasseDeriv d` and the disjoint-support corollary `hasseDeriv d ∘ₗ hasseDeriv e = hasseDeriv (d + e)`;
  - a public `Finsupp.choose_mul` (replacing the private `hasseCoeff_mul_hasseCoeff`) for multi-index binomial algebra (Vandermonde / Taylor).
WHY it belongs in mathlib (gap): `Mathlib/Algebra/MvPolynomial/` has `pderiv` but no Hasse derivatives, so the iterativity law, needed by any multiplicity-method or Roth-type index argument in positive or mixed characteristic, has no multivariate statement.
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new file, with the parent)
PR grouping: ship with `Finsupp.choose` (+ `Finsupp.choose_mul`), `MvPolynomial.hasseDeriv`, `coeff_hasseDeriv`, `hasseDeriv_monomial`, `hasseDeriv_map`, `hasseDeriv_rename`, `hasseDeriv_hasseDeriv_of_disjoint`.
Next action: run `/generalise MvPolynomial.hasseDeriv_hasseDeriv` (target: the operator form above with `Finsupp.choose`) before opening a PR.

---

## Next step

Upstream with the parent: add `hasseDeriv_comp` in operator form (`∘ₗ`, `ℕ`-smul, `(d + e).choose d`) and keep `hasseDeriv_hasseDeriv` as its pointwise corollary, plus a public `Finsupp.choose_mul`. Locally no change is needed (call sites Roth/Index.lean:113 and Roth/HasseDeriv.lean:187 keep the pointwise form).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_hasseDeriv/variants.lean` (`lean_diagnostic_messages`: success, no diagnostics): (1) the operator form `hasseDeriv d ∘ₗ hasseDeriv e = hasseCoeff d (d + e) • hasseDeriv (d + e)` (`ℕ`-smul) derived via `LinearMap.ext` + `simp [hasseDeriv_hasseDeriv, Nat.cast_smul_eq_nsmul]`; (2) the pointwise `R`-cast form recovered from the operator form by `simpa [Nat.cast_smul_eq_nsmul] using LinearMap.congr_fun hcomp P`; (3) `fail_if_success (simp [coeff_hasseDeriv, hasseCoeff]; done)` confirms the coefficient API alone leaves the multi-index binomial identity open. One cold `lake env lean` run (first draft: `ext P : 1` reduced to monomials and failed; fixed to `LinearMap.ext`), then rechecked via the LSP.
- Parent evidence `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/weaken_semiring_fails.lean` (`CommSemiring` forced).
- Loogle `"hasseDeriv_comp"`; LeanSearch and Lean-Finder queries as in [A]–[C]; mathlib grep as in [D]–[E].
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project greps: `grep -rn hasseDeriv_hasseDeriv Roth/` (call sites), `grep -rn "hasseDeriv .*(hasseDeriv" Roth/` (inline derivations: none), `.mathlib-quality/references/clean.tex` grep (l.571–584).
