---
decl: MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero
file: Roth/HasseDeriv.lean
line: 243
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Special case of the multivariate Leibniz rule for Hasse derivatives (absent from mathlib, which has only univariate Polynomial.hasseDeriv_mul); the Leibniz rule and a strictly weaker hypothesis form (Delta_a f = 0 for 0 ne a le d) both compile in a few lines, with this statement as a one-line corollary.
action: Upstream with the parent into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as `hasseDeriv_mul` (Leibniz) + `hasseDeriv_mul_of_hasseDeriv_eq_zero` + this lemma as corollary (drops private hasseDeriv_monomial_mul); locally keep as is (callers Roth/Separation.lean:157,161 need no change).
---

# MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] {d : σ →₀ ℕ} {f g : MvPolynomial σ R}, (∀ j ∈ d.support, degreeOf j f = 0) → hasseDeriv d (f * g) = f * hasseDeriv d g`
- **What**: If `f` does not involve any variable that `Δ_d` differentiates (degree 0 in every `x_j` with `d j ≠ 0`), then `f` passes through the Hasse derivative: `Δ_d (f g) = f · Δ_d g`.
- **How**: Expand `f` as a sum of monomials (`MvPolynomial.as_sum`), distribute (`Finset.sum_mul`, `map_sum`), and apply the private monomial case `hasseDeriv_monomial_mul` termwise; its hypothesis `a j = 0` comes from `monomial_le_degreeOf j` and `hf`.
- **Hypotheses**: `hf : ∀ j ∈ d.support, degreeOf j f = 0` (equivalently `Disjoint f.vars d.support`); section variable `[CommSemiring R]`.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_monomial_mul` (private)
- **Used by**: Roth/Separation.lean:157 and Roth/Separation.lean:161 (both in `hasseDeriv_rename_mul_aeval`, l.146). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 243–247, proof length 3 lines
- **Notes**: Special case of the multivariate Leibniz rule `Δ_d (f g) = Σ_{a+b=d} Δ_a f · Δ_b g`, not present in the project or mathlib.

## Junk check (Step 8)
- Used anywhere? Yes: twice in `Separation.hasseDeriv_rename_mul_aeval` (Roth/Separation.lean:157, :161), the factorwise action of `Δ` on a separated product (source §2, Lemma 2).
- Wrapper of 1–2 mathlib calls? No. `hasseDeriv` is not in mathlib; the proof is a sum-over-support reduction to a 10-line private monomial lemma.
- Does mathlib have it? No (Phase 5). Mathlib has only univariate `Polynomial.hasseDeriv_mul` and first-order `MvPolynomial.pderiv_mul` / `pderiv_C_mul`.
- Too specific / inline? No: 2 uses, natural API ("constants for Δ_d pull out").
- Well-chosen? Yes as a corollary; the underlying content is the Leibniz rule (evidence item 2).
- Conclusion: `KEEP`. Action: keep locally; upstream with the Leibniz rule as its core.

## Mathlibable assessment (Step 9)

This lemma has real content (it is not glue), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; the evidence file importing `Roth.Taylor` elaborates)
- decl `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`: resolved at Roth/HasseDeriv.lean:243
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` is a theorem stating the following:

Let `R` be a commutative semiring, `d` a multi-index and `f, g ∈ R[X_σ]`. Suppose `f` does not involve any variable `x_j` with `d_j > 0`. Then `Δ_d (f g) = f · Δ_d g`, i.e. `f` behaves as a constant for the Hasse derivative `Δ_d`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`: index set of variables.
- `R : Type*`, `[CommSemiring R]`: coefficients.
- `d : σ →₀ ℕ`: order of the Hasse derivative.
- `f g : MvPolynomial σ R`: the two factors.

Hypotheses (Lean side):
- `hf : ∀ j ∈ d.support, degreeOf j f = 0`: `f` is free of the differentiated variables.

Conclusion (math): `Δ_d (f g) = f Δ_d g`.

Conclusion (Lean): `hasseDeriv d (f * g) = f * hasseDeriv d g`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a basic product lemma about the BIG parent `MvPolynomial.hasseDeriv`; not listed under `## Main results`.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's lemma Wronskian partial derivative of product of polynomial in separate variables factor out, Hasse derivative | partial | Roth-lemma treatments (arXiv 1305.0926) handle products of polynomials in separate variables | the factor-out step is used implicitly, never stated as a lemma |
| 2 | WebSearch (general form) | Hasse derivative product rule multivariate polynomial Leibniz formula sum over beta+gamma = alpha | yes | `Δ_α(FG) = Σ_{β+γ=α} Δ_β F · Δ_γ G` (arXiv 1509.00279 multiplicity codes, 2505.14472, 1802.09894) | the general form; our lemma is the case `Δ_β F = 0` for `0 ≠ β ≤ α` |
| 3 | WebSearch (named-after / aliases) | Hasse-Schmidt derivation multiplicative higher derivation D_n(ab) = sum D_i(a) D_j(b) linear over constants | yes | higher Leibniz rule is the defining axiom of a (multivariate) Hasse–Schmidt derivation; maps are linear over constants (arXiv 2007.14171, 1802.09894, Matsumura §27) | "constants pull out" is the standard consequence of the Leibniz axiom |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for U, V, φ_ρ, ψ_ρ | yes | l.363–414 (Lemma 2): `F = U(x_1..x_{p-1}) V(x_p)` and `Δ_μ (1/ν!) ∂^ν (φ_ρ(x_p) ψ_ρ(...)) = (Δ_μ ψ_ρ)(...)`, differential operators in disjoint variables | exactly the use at Roth/Separation.lean:146 |
| 6 | nLab | Hasse-Schmidt derivation (ncatlab.org) | partial | definition with higher Leibniz rule | no "constant factor" statement, but it follows from the axiom |
| 7 | nCatLab | (same nLab page) | n/a | — | not a categorical statement |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; Stacks has no Hasse-derivative tag (differential operators section is first-order/PD) |
| 9 | MathOverflow / Math.SE | (covered by query #3, which surfaced no MO/MSE thread) | no | — | folklore |
| 10 | recent arXiv (last 5 years) | results of #2–#3 | yes | arXiv 2505.14472 (2025), 2007.14171 (2020/23), 2305.04537 (2023) | all state the multi-index Leibniz rule |

### Literature summary (Phase 3)

Concept identified as: Leibniz rule for (multivariate) Hasse derivatives / Hasse–Schmidt derivations; "elements constant for Δ pull out".
Sources agree on the standard form: yes. `Δ_α(FG) = Σ_{β+γ=α} Δ_β F Δ_γ G`.
Most general standard form: Leibniz rule; corollary: if `Δ_β F = 0` for all `0 ≠ β ≤ α`, then `Δ_α(FG) = F Δ_α G`.
Generality dimensions where the literature varies:
  - hypothesis on `F`: "F free of the differentiated variables" (Roth-type arguments, this project) versus "all lower Hasse derivatives of F vanish" (strictly weaker in positive characteristic, e.g. `F = X^p`).
Disagreement with the literature: none; the project form is a special case.

### Generality analysis — `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`

Literature-standard form (from Phase 3): Leibniz rule, with corollary `(∀ a ≤ d, a ≠ 0 → hasseDeriv a f = 0) → hasseDeriv d (f * g) = f * hasseDeriv d g`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative ring/semiring | no | `MvPolynomial σ R` requires `CommSemiring R` (parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`) |
| 2 | `σ` | arbitrary | arbitrary | no | — |
| 3 | `hf : ∀ j ∈ d.support, degreeOf j f = 0` | f free of differentiated variables | lower Hasse derivatives of `f` vanish | yes | strictly weaker: compiles (evidence item 3), implies the current form (item 4), and is strictly weaker (item 5: `X^2` over `ZMod 2`, `d = e_0`) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD.
Number of weakening opportunities found: 1 (hypothesis weakened to vanishing of lower Hasse derivatives; verified, evidence items 3–5), resting on the Leibniz rule (item 2, verified).
Proposed restatement:

```lean
theorem hasseDeriv_mul [DecidableEq σ] (d : σ →₀ ℕ) (f g : MvPolynomial σ R) :
    hasseDeriv d (f * g) =
      ∑ x ∈ Finset.antidiagonal d, hasseDeriv x.1 f * hasseDeriv x.2 g

theorem hasseDeriv_mul_of_hasseDeriv_eq_zero {d : σ →₀ ℕ} {f g : MvPolynomial σ R}
    (hf : ∀ a ≤ d, a ≠ 0 → hasseDeriv a f = 0) :
    hasseDeriv d (f * g) = f * hasseDeriv d g
```
with the current statement kept under its current name as a corollary.

Cost of restatement: CHEAP. All compile in the evidence file (Leibniz: 1 line via Taylor shift; corollary 8 lines; project form 5 lines).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | single hypothesis on `f` |
| 2 | sequences to filters? | no | — | algebraic |
| 3 | construction vs universal property? | partial | Leibniz = `taylor X` is a ring hom and `Δ_d` its coefficients (Hasse–Schmidt derivation structure) | the Leibniz proof in evidence item 2 is exactly this |
| 4 | set-with-predicate to bundled substructure? | partial | `Δ_d` is linear over the subalgebra `supported R (↑d.support)ᶜ` | not needed; mathlib states such facts elementwise (`pderiv_C_mul`) |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | — |
| 8 | concrete-via-abstract? | yes | the proof only uses that `Δ_a f = 0` for lower `a`; `degreeOf` is one route | core lemma `hasseDeriv_mul_of_hasseDeriv_eq_zero` |
| 9 | false-generalisation guard | no false generalisation | same operator, weaker hypothesis, original recovered (item 4) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `hasseDeriv_mul` (multivariate Leibniz, mirroring `Polynomial.hasseDeriv_mul`) as the core; `hasseDeriv_mul_of_hasseDeriv_eq_zero` and this lemma as corollaries.
  - Cost: CHEAP
  - Mathlib downstream this enables: multivariate analogue of `Polynomial.hasseDeriv_mul`; with `factorial_smul_hasseDeriv_single` it yields the general Leibniz rule for iterated `pderiv`, which mathlib lacks (it has only `pderiv_mul`); multiplicity / vanishing-order arguments (`Δ_β(FG)` at a common zero) need it.
  - Real mathematical improvement: replaces a monomial-by-monomial computation (the private 10-line `hasseDeriv_monomial_mul`) by the structural Leibniz rule, from which this and other product facts are one-liners.

### Proof strategy — `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | derive from Leibniz, itself from multiplicativity of the Taylor shift `taylor X ∘ map C` (evidence item 1–2) | CHEAP |
| 5 | missing mathlib helpers | yes | multivariate `hasseDeriv_mul` (Leibniz) | CHEAP (file with parent PR) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: prove `hasseDeriv_mul` (Leibniz) and deduce this lemma by `Finset.sum_eq_single (0, d)`, killing lower terms with `hasseDeriv_eq_zero_of_degreeOf_lt`.
  - Cost: CHEAP
  - Missing mathlib API: multivariate Hasse derivative with Leibniz rule (parent PR). Note: the 1-line Leibniz proof uses the project's `taylor` (Roth/Taylor.lean) and `coeff_taylor`; upstream either ships the Taylor shift first or proves Leibniz directly from a multi-index Vandermonde identity (MODERATE).
  - Would refactoring make the proof strictly shorter / cleaner? yes (removes the private monomial helper).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`

[A] Lean-Finder       "multivariate polynomial: higher derivative in some variables of f * g equals f times derivative of g when f does not involve those variables"   `MvPolynomial.pderiv_mul`, `pderiv_C_mul`, `X_mul_pderiv_monomial`, `leibniz_iff_X`; no higher-order multivariate hit
[B] Loogle            `MvPolynomial.pderiv _ (_ * _) = _ * MvPolynomial.pderiv _ _`   only `MvPolynomial.pderiv_C_mul`
[C] LeanSearch        "Hasse derivative of product of multivariate polynomials Leibniz rule"   `MvPolynomial.pderiv_mul`, `Polynomial.hasseDeriv_mul` (univariate), `MvPolynomial.leibniz_iff_X`, `Polynomial.derivative_mul`; no multivariate Hasse
[D] Grep mathlib src  `hasseDeriv` only in Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean; `hasseDeriv_mul` only univariate (HasseDeriv.lean:211); PDeriv.lean has `pderiv_mul`, `pderiv_eq_zero_of_notMem_vars`; no `degreeOf_eq_zero_iff`
[E] Name pattern      grep of `.lake/packages/mathlib/Mathlib` for `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`, `MvPolynomial.hasseDeriv_mul`, `hasseDeriv_mul_of_hasseDeriv_eq_zero`   no hits

Searched for both the user's form and the literature-standard Leibniz form.

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Univariate analogue `Polynomial.hasseDeriv_mul` exists at Mathlib/Algebra/Polynomial/HasseDeriv.lean:211.

### Normal-form check — `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`

Equivalent formalisms: `∀ j ∈ d.support, degreeOf j f = 0` (current); `Disjoint f.vars d.support`; `f ∈ supported R (↑d.supportᶜ)`; weaker `∀ a ≤ d, a ≠ 0 → hasseDeriv a f = 0`.
Does mathlib already have a canonical form for this idea? Univariately the canonical result is `Polynomial.hasseDeriv_mul` (Leibniz); first-order multivariate uses `i ∉ f.vars` (`pderiv_eq_zero_of_notMem_vars`).
Our statement is stated against the canonical form? Partially: equation shape `Δ (f * g) = f * Δ g` mirrors `pderiv_C_mul`; hypothesis could be phrased via `vars` to match `pderiv_eq_zero_of_notMem_vars`.
RHS convention respected? yes.

### Syntactic generality — `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`

Alternative restatements attempted:
- Leibniz core (evidence item 2, compiles)
- lower-derivatives-vanish hypothesis (item 3, compiles)
- current `degreeOf` hypothesis as corollary (item 4, compiles)
- `Disjoint f.vars d.support` (not compiled; equivalent, cosmetic)
Chosen restatement: ship all three compiled forms; keep current name/signature for the `degreeOf` form.
Justification: both call sites (Separation.lean:157, :161) discharge `degreeOf j f = 0` via `simp [degreeOf, degrees_rename_...]`; the `degreeOf` form is easiest there.

### Superfluous-argument audit — `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `hf` | yes | needed; can be weakened (above), not dropped (`Δ_{e_0}(X_0 · 1) = 1 ≠ X_0 · 0`) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (add Leibniz core and the weakened-hypothesis corollary; keep this form)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`

Internal use count: 2 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:157 | `hasseDeriv_mul_of_degreeOf_eq_zero fun j hj ↦ by rw [...]; simp [degreeOf, degrees_rename_of_injective ...]` (in `rw` chain of `hasseDeriv_rename_mul_aeval`) |
| Roth/Separation.lean:161 | `hasseDeriv_mul_of_degreeOf_eq_zero fun j hj ↦ by simp [aeval_X_eq_rename, degreeOf, ...]` (same proof) |

Inline-derivation grep: none (`grep -rn "hasseDeriv.*\* \|hasseDeriv_monomial_mul" Roth/` finds only the private helper, used solely by this lemma).

### Composition check (Phase 6)

Can `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib alone.
  - Mathlib decls used: none applicable; `MvPolynomial.hasseDeriv` is not in mathlib; `Polynomial.hasseDeriv_mul` is univariate; `pderiv_C_mul` is first order.
  - Result: fails

Attempt 2: from the project's Leibniz rule (evidence item 2) via `Finset.sum_eq_single (0, d)` plus `hasseDeriv_eq_zero_of_degreeOf_lt`.
  - Result: succeeds, but is a short proof (case analysis), and needs non-mathlib API.

Conclusion: NOT-COMPOSABLE (from mathlib).

## Verdict: `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard multi-index Leibniz rule `Δ_α(FG) = Σ_{β+γ=α} Δ_β F Δ_γ G` (arXiv 1509.00279, 1802.09894, 2505.14472; Matsumura §27); source clean.tex l.363–414 uses the "free of differentiated variables" special case.
- Generality analysis (Phase 4): STRICTLY NARROWER; weakened hypothesis compiles (item 3), implies the current form (item 4), and is strictly weaker (item 5).
- Mathlib search (Phase 5): not in mathlib; only univariate `Polynomial.hasseDeriv_mul`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` is assessed YES-but-generalise-first because mathlib has no multivariate Hasse derivative. A product rule is essential API for such an operator: mathlib's univariate file has `Polynomial.hasseDeriv_mul`, and `PDeriv.lean` has `pderiv_mul` and `pderiv_C_mul`, but nothing for higher-order multivariate derivatives. The Roth development needs exactly the factor-out case, for the separated product `U(x_τ) V(x_none)` in Lemma 2 (Roth/Separation.lean:146).

The right upstream form is the multivariate Leibniz rule. It compiles in one line from the Taylor shift being an algebra hom (`coeff_taylor` + `hasseDeriv_map` + `coeff_mul`, evidence item 2). This lemma then follows with a strictly weaker hypothesis (lower Hasse derivatives of `f` vanish), which also covers e.g. `p`-th powers in characteristic `p` (item 5). The current `degreeOf` statement stays as a 5-line corollary under its name, and the private `hasseDeriv_monomial_mul` becomes unnecessary.

Reason for the generalisation: LITERATURE-WEAKENING (Leibniz rule and vanishing-lower-derivatives hypothesis are standard) and MODERN-IDIOM (structural proof via the Taylor ring hom replaces a monomial computation).
Proposed restatement:
```lean
theorem hasseDeriv_mul [DecidableEq σ] (d : σ →₀ ℕ) (f g : MvPolynomial σ R) :
    hasseDeriv d (f * g) =
      ∑ x ∈ Finset.antidiagonal d, hasseDeriv x.1 f * hasseDeriv x.2 g := by
  simp_rw [← eval_X_coeff_taylor, map_mul, coeff_mul]

theorem hasseDeriv_mul_of_hasseDeriv_eq_zero {d : σ →₀ ℕ} {f g : MvPolynomial σ R}
    (hf : ∀ a ≤ d, a ≠ 0 → hasseDeriv a f = 0) :
    hasseDeriv d (f * g) = f * hasseDeriv d g

theorem hasseDeriv_mul_of_degreeOf_eq_zero {d : σ →₀ ℕ} {f g : MvPolynomial σ R}
    (hf : ∀ j ∈ d.support, degreeOf j f = 0) : hasseDeriv d (f * g) = f * hasseDeriv d g :=
  hasseDeriv_mul_of_hasseDeriv_eq_zero fun a had ha ↦ ...  -- via hasseDeriv_eq_zero_of_degreeOf_lt
```
(full proofs in the evidence file).
Estimated cost of regeneralisation: CHEAP given the Taylor shift; MODERATE if Leibniz must be proved without it (multi-index Vandermonde).
Mathlib downstream this enables:
  - multivariate analogue of `Polynomial.hasseDeriv_mul`; with `factorial_smul_hasseDeriv_single`, a higher-order Leibniz rule for iterated `pderiv` (mathlib has only first-order `pderiv_mul`);
  - vanishing-order / multiplicity arguments (index of a product, method of multiplicities) that need `Δ_β(FG)`;
  - the constant-factor rule generalising `pderiv_C_mul` to higher order.
WHY it belongs in mathlib (gap): `Mathlib/Algebra/MvPolynomial/PDeriv.lean` has no higher-order product rule and mathlib has no multivariate Hasse derivative at all (parent report).
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new file, with the parent; Leibniz after the Taylor shift or via Vandermonde).
PR grouping: ship with `MvPolynomial.hasseDeriv`, `coeff_hasseDeriv`, `hasseDeriv_map`, `hasseDeriv_eq_zero_of_degreeOf_lt` (used in the corollary), and the Taylor shift `MvPolynomial.taylor`/`coeff_taylor` if the 1-line Leibniz proof is used.
Next action: run `/generalise MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` (target: Leibniz core + weakened-hypothesis corollary above) before opening a PR.

---

## Next step

Upstream with the parent: add `hasseDeriv_mul` (Leibniz) and `hasseDeriv_mul_of_hasseDeriv_eq_zero`, derive this lemma unchanged, drop the private `hasseDeriv_monomial_mul`. Locally optional: same refactor needs `Roth.Taylor` before this lemma (currently Taylor imports HasseDeriv), so keep as is unless the lemma moves to Roth/Taylor.lean. Callers Roth/Separation.lean:157, :161 need no change.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero/leibniz.lean` (imports `Roth.Taylor`, `Mathlib.Data.ZMod.Basic`), checked with `lean_diagnostic_messages`: success, no errors (only flexible-`simp` style linter notes in the example). Contents:
  - (1) `eval_X_coeff_taylor`: `(taylor X (map C P)).coeff d = hasseDeriv d P`.
  - (2) `hasseDeriv_mul`: multivariate Leibniz rule, one line.
  - (3) `hasseDeriv_mul_of_hasseDeriv_eq_zero`: weakened hypothesis.
  - (4) The project statement as a corollary of (3).
  - (5) Strictness example: `X () ^ 2` over `ZMod 2` passes through `Δ_{e_()}` although its degree is 2.
- Iterations: missing `ZMod` import; `omega` failing on `a ()` vs `a PUnit.unit` (fixed with `change`). No cold `lake env lean` run.
- Searches: LeanSearch, Lean-Finder, Loogle as in [A]–[C]; mathlib grep [D]–[E].
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project greps: `grep -rn hasseDeriv_mul_of_degreeOf_eq_zero Roth/` (call sites); `.mathlib-quality/references/clean.tex` l.363–414.
