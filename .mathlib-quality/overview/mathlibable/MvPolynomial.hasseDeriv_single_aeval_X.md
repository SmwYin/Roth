---
decl: MvPolynomial.hasseDeriv_single_aeval_X
file: Roth/HasseDeriv.lean
line: 253
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Bridge Delta_{n e_j} (f(X_j)) = (D^(n) f)(X_j) between the multivariate and univariate Hasse derivatives, absent from mathlib (which lacks even the first-order pderiv analogue for Polynomial.toMvPolynomial); a strictly more general form for arbitrary multi-index d compiles, and the statement should be phrased with mathlib's Polynomial.toMvPolynomial.
action: Upstream with the parent to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as `hasseDeriv_toMvPolynomial` (general d, evidence bridge.lean) plus this single-index form as corollary stated via Polynomial.toMvPolynomial; locally keep as is (caller Roth/Separation.lean:160 rewrites with the aeval form).
---

# MvPolynomial.hasseDeriv_single_aeval_X

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_single_aeval_X`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (j : σ) (n : ℕ) (f : Polynomial R), hasseDeriv (Finsupp.single j n) (Polynomial.aeval (X j : MvPolynomial σ R) f) = Polynomial.aeval (X j : MvPolynomial σ R) (Polynomial.hasseDeriv n f)`
- **What**: The multivariate Hasse derivative `Δ_{n e_j}` applied to a polynomial `f(x_j)` in the single variable `x_j` is the univariate Hasse derivative `D^(n) f`, evaluated at `x_j`.
- **How**: Induction on `f` via `Polynomial.induction_on'`; the additive case is `simp`; the monomial case is a `simp` computation with `X_pow_eq_monomial`, `C_mul_monomial`, `hasseCoeff`, `Finsupp.single_tsub`, `mul_assoc` (unfolding `hasseDeriv_monomial` and `Polynomial.hasseDeriv_monomial` via simp lemmas, with `map_natCast` disabled).
- **Hypotheses**: none beyond section variables `[CommSemiring R]`.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseCoeff` (unfolded in simp; `hasseDeriv_monomial`/`hasseDeriv_apply` as simp lemmas)
- **Used by**: Roth/Separation.lean:160 (in `hasseDeriv_rename_mul_aeval`, l.146, `rw` chain). Mentioned in Roth/HasseDeriv.lean:36 (module docstring). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 253–260, proof length 5 lines
- **Notes**: Companion of `uniqueAlgEquiv_hasseDeriv` (l.266), which states the same compatibility for `σ` with `[Unique σ]`; this lemma follows from that one plus `hasseDeriv_rename` (evidence item 2).

## Junk check (Step 8)
- Used anywhere? Yes: Roth/Separation.lean:160 (factorwise action of `Δ` on a separated product, source §2 Lemma 2).
- Wrapper of 1–2 mathlib calls? No; `hasseDeriv` is not in mathlib.
- Does mathlib have it? No (Phase 5): mathlib has no multivariate Hasse derivative, and not even the first-order bridge `pderiv j (toMvPolynomial j f) = toMvPolynomial j (derivative f)`.
- Too specific / inline? No: it is the natural bridge lemma between the univariate and multivariate theories (mathlib has the analogous `Polynomial.Bivariate.pderiv_one_equivMvPolynomial` for `pderiv`).
- Well-chosen? Yes, though `Polynomial.toMvPolynomial j` is mathlib's named form of `Polynomial.aeval (X j)`.
- Conclusion: `KEEP`. Action: keep locally; upstream with the parent in the generalised form below.

## Mathlibable assessment (Step 9)

Real content (5-line induction proof), not glue; full workflow run.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; evidence file importing `Roth.HasseDeriv` elaborates)
- decl `MvPolynomial.hasseDeriv_single_aeval_X`: resolved at Roth/HasseDeriv.lean:253
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseDeriv_single_aeval_X` is a theorem stating the following:

Let `R` be a commutative semiring, `j` a variable index, `n ∈ ℕ` and `f ∈ R[t]`. Viewing `f(x_j)` as a polynomial in `R[x_σ]`, its `n`-th Hasse derivative in the direction `x_j`, `Δ_{n e_j} f(x_j)`, equals `(D^(n) f)(x_j)`, where `D^(n)` is the univariate Hasse derivative. Equivalently, the embedding `R[t] → R[x_σ]`, `t ↦ x_j`, intertwines `D^(n)` and `Δ_{n e_j}`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`: index set of variables.
- `R : Type*`, `[CommSemiring R]`: coefficients.
- `j : σ`: the variable.
- `n : ℕ`: order.
- `f : Polynomial R`: univariate polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `Δ_{n e_j}(f(x_j)) = (D^(n) f)(x_j)`.

Conclusion (Lean): `hasseDeriv (Finsupp.single j n) (Polynomial.aeval (X j) f) = Polynomial.aeval (X j) (Polynomial.hasseDeriv n f)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: compatibility lemma for the BIG parent `MvPolynomial.hasseDeriv` (it is listed in the module's `## Main results` as a compatibility result, but is a bridge lemma, not a main theorem of the project).

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 5
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Hasse derivative multivariate polynomial restricted to one variable equals univariate Hasse derivative partial | partial | arXiv 1505.07547 (multiplicity codes): for `Q(T) = P(a + bT)`, `Q^(j)(T) = Σ_{|i|=j} P^(i)(a + bT) b^i`; arXiv 1412.5012, 2111.07572 define Hasse derivatives as Taylor coefficients of `F(X + Z)` | with `b = e_j` and `P` a polynomial in `x_j` only, the sum collapses to our statement; not stated as a separate lemma |
| 2 | WebSearch (general form) | Hasse-Schmidt derivation compatible with ring homomorphism substitution x_j polynomial ring partial Hasse derivative D^(n) with respect to x_j | partial | Hasse–Schmidt derivations as algebra homs `A → A[[T]]` (Wikipedia, nLab, arXiv 2305.04537, 1802.09894 substitution maps) | general functoriality of HS-derivations under substitution; our lemma is the case of the embedding `t ↦ x_j` |
| 3 | WebSearch (named-after / aliases) | "Hasse derivative" "with respect to x_i" multi-index Δ_{n e_i} divided power derivative partial polynomial | yes | arXiv 1303.0084 Def. 5.1: `k`-th Hasse derivative with respect to `x_i` = coefficient of `y^k` in `f(x + e_i y)`; multi-index operator = composition of single-variable ones; ar5iv 0903.0246 (`Δ^{(i)}_m` acting in the `i`-th variable) | defining property: `Δ_{n e_i}` is the univariate Hasse derivative in `x_i` with other variables as constants; our lemma is the special case of no other variables |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §1 "Derivatives" (l.119–155) | yes | `Δ_i` defined on monomials; Lean note: "Use the univariate `Polynomial.hasseDeriv` as a model" | source cites the univariate operator as the model; the bridge is implicit |
| 6 | nLab | Hasse-Schmidt derivative (ncatlab.org, surfaced by query #2) | partial | HS derivation definition | no polynomial-ring restriction statement |
| 7 | nCatLab | (same nLab page) | n/a | — | not a categorical statement |
| 8 | Stacks Project | — | n/a | — | Stacks treats differential operators/PD structures but has no Hasse-derivative restriction tag; not algebraic geometry |
| 9 | MathOverflow / Math.SE | (queries #1–#3 surfaced no MO/MSE thread) | no | — | folklore |
| 10 | recent arXiv (last 5 years) | results of #1–#3 | yes | arXiv 2111.07572 (2021), 2205.00342 (2022), 2305.04537 (2023), 2311.08873 (2023) | all use the coordinate Hasse derivative = univariate Hasse derivative in that coordinate |

### Literature summary (Phase 3)

Concept identified as: compatibility of the coordinate Hasse derivative `Δ_{n e_j}` (Hasse derivative "with respect to `x_j`") with the univariate Hasse derivative under the embedding `t ↦ x_j`.
Sources agree on the standard form: yes. `Δ_{n e_j}` is the univariate `D^(n)` in `x_j` (other variables constant).
Most general standard form: `Δ_d (f(x_j)) = (D^(d_j) f)(x_j)` if `d` is supported on `{j}`, and `0` otherwise (follows from the monomial formula); more generally functoriality of Hasse–Schmidt derivations under substitution (line restriction formula of arXiv 1505.07547).
Generality dimensions where the literature varies:
  - multi-index: single `n e_j` (current) to arbitrary `d` (general; extra case is `0`).
  - substitution: `t ↦ x_j` (current) to affine lines `t ↦ a + b t` (chain-rule form, needs Leibniz/Taylor machinery; different statement).
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.hasseDeriv_single_aeval_X`

Literature-standard form (from Phase 3): `Δ_d (f(x_j)) = if d = d_j e_j then (D^(d_j) f)(x_j) else 0`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative ring/semiring | no | `MvPolynomial σ R` needs `CommSemiring R` (parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`) |
| 2 | multi-index `Finsupp.single j n` | single-direction | arbitrary `d : σ →₀ ℕ` | yes | general form `hasseDeriv_aeval_X` compiles (evidence item 3) |
| 3 | embedding `Polynomial.aeval (X j)` | `aeval (X j)` | mathlib's named `Polynomial.toMvPolynomial j` | cosmetic | definitionally the same; `toMvPolynomial` form compiles by the same term (item 1) |
| 4 | `σ` | arbitrary | arbitrary | no | — |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (arbitrary multi-index `d`; verified, evidence item 3), plus a cosmetic restatement via `Polynomial.toMvPolynomial` (item 1).
Proposed restatement:

```lean
theorem hasseDeriv_toMvPolynomial [DecidableEq σ] (j : σ) (d : σ →₀ ℕ) (f : Polynomial R) :
    hasseDeriv d (f.toMvPolynomial j) =
      if d = Finsupp.single j (d j) then (Polynomial.hasseDeriv (d j) f).toMvPolynomial j else 0

theorem hasseDeriv_single_toMvPolynomial (j : σ) (n : ℕ) (f : Polynomial R) :
    hasseDeriv (Finsupp.single j n) (f.toMvPolynomial j) =
      (Polynomial.hasseDeriv n f).toMvPolynomial j
```

Cost of restatement: CHEAP (general form: 8-line proof plus a 7-line `d ≤ single j m → d = single j (d j)` helper, compiled in the evidence file with `aeval (X j)` spelling).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic |
| 3 | construction vs universal property? | partial | operator form `Δ_{n e_j} ∘ₗ toMvPolynomial j = toMvPolynomial j ∘ₗ D^(n)` (item 1') | composes with `LinearMap.comp` API; not a different statement |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | arbitrary multi-index `d` | covers `Δ_d` with `d` not supported on `{j}` (gives `0`), used e.g. when expanding mixed derivatives of separated products |
| 8 | concrete-via-abstract? | no | the proof is a monomial computation on the concrete operator; the abstract alternative (item 2: `hasseDeriv_rename` + `uniqueAlgEquiv_hasseDeriv`) is a different proof, not a more abstract statement | — |
| 9 | false-generalisation guard | no false generalisation | same operator; the general-`d` form specialises back to the original (`if` true branch) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: state against mathlib's named algebra hom `Polynomial.toMvPolynomial j` (Mathlib/Algebra/MvPolynomial/Equiv.lean), arbitrary `d`, with the single-index form as corollary.
  - Cost: CHEAP
  - Mathlib downstream this enables: uses the existing `Polynomial.toMvPolynomial` API (`toMvPolynomial_injective`, `toMvPolynomial_eq_rename_comp`, `toMvPolynomial_X`); parallels the bivariate bridges `Polynomial.Bivariate.pderiv_zero_equivMvPolynomial` / `pderiv_one_equivMvPolynomial`.
  - Real mathematical improvement: the general-`d` form records the vanishing for mixed indices, which the single-index form cannot express.

### Proof strategy — `MvPolynomial.hasseDeriv_single_aeval_X`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | partial | derive from `hasseDeriv_rename` + `uniqueAlgEquiv_hasseDeriv` via `toMvPolynomial_eq_rename_comp` (item 2) | CHEAP, but not shorter (6 lines vs 5) |
| 5 | missing mathlib helpers | yes | `Finsupp` lemma `d ≤ single j m → d = single j (d j)` (helper in evidence; mathlib has `Finsupp.support_subset_singleton`-style lemmas but not this one, not checked exhaustively) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
  (Monomial induction mirrors `Polynomial.hasseDeriv` proofs; the structural alternative via rename is no shorter. For the general-`d` version the monomial proof is the natural one.)

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.hasseDeriv_single_aeval_X`

[A] Lean-Finder       "partial derivative of a univariate polynomial evaluated at the variable X i in MvPolynomial equals derivative then evaluated"   `pderiv_X_self`, `pderiv_X`, `pderiv_def`, `pderiv`, `Polynomial.Bivariate.pderiv_one_equivMvPolynomial` (bivariate analogue for `pderiv`, not Hasse)
[B] Loogle            `MvPolynomial.pderiv _ (Polynomial.aeval _ _)`; `Polynomial.toMvPolynomial, MvPolynomial.pderiv`   no hits (not even the first-order bridge)
[C] LeanSearch        "Hasse derivative of polynomial embedded in multivariate polynomial ring via X i"   `Polynomial.hasseDeriv`, `mkDerivation_X`, `pderiv`, `Polynomial.hasseDeriv_apply`; no bridge
[D] Grep mathlib src  `hasseDeriv` only in Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean; `toMvPolynomial` with `deriv`: no hits; `derivative` in Algebra/MvPolynomial/*.lean: none (only docstrings in PDeriv.lean)
[E] Name pattern      grep `.lake/packages/mathlib/Mathlib` for `hasseDeriv_single_aeval_X`, `hasseDeriv_toMvPolynomial`, `MvPolynomial.hasseDeriv`   no hits

Searched for both the user's form and the general-`d` / `toMvPolynomial` form.

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Closest: `Polynomial.Bivariate.pderiv_one_equivMvPolynomial` (first-order, bivariate equivalence).

### Normal-form check — `MvPolynomial.hasseDeriv_single_aeval_X`

Equivalent formalisms: `Polynomial.aeval (X j) f` (current); `f.toMvPolynomial j`; `rename (fun _ ↦ j) ((uniqueAlgEquiv R Unit).symm f)`; operator equality of linear maps.
Does mathlib already have a canonical form for this idea? Yes for the embedding: `Polynomial.toMvPolynomial j` (named `R[X] →ₐ[R] MvPolynomial σ R`).
Our statement is stated against the canonical form? Partly: `aeval (X j)` is the unfolding of `toMvPolynomial j`; upstream should use the named form (keeping `aeval` spelling locally for the caller's `rw`).
RHS convention respected? yes (univariate operator pushed inside the embedding on the RHS).

### Syntactic generality — `MvPolynomial.hasseDeriv_single_aeval_X`

Alternative restatements attempted:
- `toMvPolynomial` form (item 1, compiles)
- operator/LinearMap form (item 1', compiles)
- general `d` with `if` (item 3, compiles)
Chosen restatement: general `d` (`hasseDeriv_toMvPolynomial`) plus single-index corollary in `toMvPolynomial` spelling (simp-friendly, rewritable).
Justification: the single-index form is what callers rewrite with (Separation.lean:160); the general form covers mixed indices.

### Superfluous-argument audit — `MvPolynomial.hasseDeriv_single_aeval_X`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `j`, `n`, `f` | yes | data of the statement |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (use `Polynomial.toMvPolynomial j` upstream)
Syntactic generality: RESTATE (add general-`d` form `hasseDeriv_toMvPolynomial`)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.hasseDeriv_single_aeval_X`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:160 | `rw [..., hasseDeriv_single_aeval_X, mul_comm, ...]` in `hasseDeriv_rename_mul_aeval` |

Inline-derivation grep: none (`grep -rn "hasseDeriv.*aeval\|aeval.*hasseDeriv" Roth/` finds only this lemma, `hasseDeriv_rename_mul_aeval` and its uses); the companion `uniqueAlgEquiv_hasseDeriv` is a separate bridge, not a re-derivation.

### Composition check (Phase 6)

Can `MvPolynomial.hasseDeriv_single_aeval_X` be derived from mathlib in ≤3 chained calls?

Attempt 1: mathlib only.
  - Mathlib decls used: none applicable (`MvPolynomial.hasseDeriv` is not in mathlib).
  - Result: fails

Attempt 2: from the project's `hasseDeriv_rename` and `uniqueAlgEquiv_hasseDeriv` plus mathlib's `Polynomial.toMvPolynomial_eq_rename_comp`, `Finsupp.mapDomain_single` (evidence item 2).
  - Result: succeeds in 6 lines (a proof, not a ≤3-call composition), and needs non-mathlib API.

Conclusion: NOT-COMPOSABLE

## Verdict: `MvPolynomial.hasseDeriv_single_aeval_X`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): coordinate Hasse derivative = univariate Hasse derivative in that coordinate (arXiv 1303.0084 Def. 5.1, ar5iv 0903.0246, 1505.07547 line restriction); source clean.tex §1 uses `Polynomial.hasseDeriv` as the model.
- Generality analysis (Phase 4): STRICTLY NARROWER; general-`d` form verified (evidence item 3).
- Mathlib search (Phase 5): not in mathlib; mathlib lacks even the first-order bridge for `toMvPolynomial`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` is YES-but-generalise-first because mathlib has only the univariate `Polynomial.hasseDeriv`. A multivariate Hasse derivative file needs bridge lemmas to the univariate theory. This lemma, with `uniqueAlgEquiv_hasseDeriv`, is that bridge: it lets univariate results (`Polynomial.hasseDeriv_mul`, `hasseDeriv_coeff`, `factorial_smul_hasseDeriv`) transfer to polynomials in one variable inside `R[x_σ]`, and the Roth project uses it for the separated product `U(x_τ) V(x_none)` (Roth/Separation.lean:160).

The upstream form should handle every multi-index `d`, not only `n e_j`: `Δ_d` kills `f(x_j)` unless `d` is supported on `{j}`. This compiles cheaply (evidence item 3). It should also be phrased with mathlib's named embedding `Polynomial.toMvPolynomial j`, which is definitionally `aeval (X j)`. The single-index form stays as a corollary.

Reason for the generalisation: LITERATURE-WEAKENING (arbitrary multi-index) and MODERN-IDIOM (`Polynomial.toMvPolynomial` spelling).
Proposed restatement:
```lean
theorem hasseDeriv_toMvPolynomial [DecidableEq σ] (j : σ) (d : σ →₀ ℕ) (f : Polynomial R) :
    hasseDeriv d (f.toMvPolynomial j) =
      if d = Finsupp.single j (d j) then (Polynomial.hasseDeriv (d j) f).toMvPolynomial j
      else 0 := by
  sorry -- proof compiled (aeval spelling) in evidence bridge.lean

theorem hasseDeriv_single_toMvPolynomial (j : σ) (n : ℕ) (f : Polynomial R) :
    hasseDeriv (Finsupp.single j n) (f.toMvPolynomial j) =
      (Polynomial.hasseDeriv n f).toMvPolynomial j
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
  - transfer of univariate Hasse-derivative results (`Polynomial.hasseDeriv_mul`, `Polynomial.hasseDeriv_coeff`, `Polynomial.factorial_smul_hasseDeriv`) to one-variable subpolynomials of `MvPolynomial σ R`;
  - composes with the existing `Polynomial.toMvPolynomial` API (`toMvPolynomial_injective`, `toMvPolynomial_eq_rename_comp`) in Mathlib/Algebra/MvPolynomial/Equiv.lean;
  - via `factorial_smul_hasseDeriv_single`, the first-order bridge `pderiv j (f.toMvPolynomial j) = (derivative f).toMvPolynomial j`, which mathlib also lacks.
WHY it belongs in mathlib (gap): mathlib has no multivariate Hasse derivative, and no bridge between `MvPolynomial.pderiv` and `Polynomial.derivative` along `Polynomial.toMvPolynomial`. The only analogue is the bivariate `Polynomial.Bivariate.pderiv_one_equivMvPolynomial` (Mathlib/Algebra/Polynomial/Bivariate.lean).
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new, with the parent).
PR grouping: ship with `MvPolynomial.hasseDeriv`, `hasseDeriv_monomial`, `hasseDeriv_rename`, `uniqueAlgEquiv_hasseDeriv`.
Next action: run `/generalise MvPolynomial.hasseDeriv_single_aeval_X` (target: `hasseDeriv_toMvPolynomial` above plus the `toMvPolynomial` corollary) before opening the PR.

---

## Next step

Upstream with the parent as `hasseDeriv_toMvPolynomial` (general `d`) and `hasseDeriv_single_toMvPolynomial` (corollary). Locally, keep as is: the caller Roth/Separation.lean:160 rewrites with the `aeval (X j)` spelling and needs no change.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_single_aeval_X/bridge.lean` (imports `Roth.HasseDeriv`), checked with `lean_diagnostic_messages`: success, no errors (one long-line style warning). Contents:
  - (1) The statement with `Polynomial.toMvPolynomial j` spelling, by the project lemma (defeq).
  - (1') Operator form as an equality of linear maps.
  - (2) Composition proof from `hasseDeriv_rename`, `uniqueAlgEquiv_hasseDeriv`, `Polynomial.toMvPolynomial_eq_rename_comp`, `Finsupp.mapDomain_single`.
  - (3) `hasseDeriv_aeval_X`: general multi-index form, with helper `eq_single_of_le_single`.
- Iterations: first composition attempt failed (`rw` pattern for `uniqueAlgEquiv_hasseDeriv`), fixed with `congr 1` + injectivity; then a `simp` that unfolded too far, replaced by `rw [AlgEquiv.apply_symm_apply]`. No cold `lake env lean` run.
- Searches: Lean-Finder, Loogle (2 queries), LeanSearch as in [A]–[C]; mathlib grep [D]–[E].
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project greps: `grep -rn hasseDeriv_single_aeval_X Roth/`; `.mathlib-quality/references/clean.tex` l.119–155.
