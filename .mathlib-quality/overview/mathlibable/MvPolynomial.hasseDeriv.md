---
decl: MvPolynomial.hasseDeriv
file: Roth/HasseDeriv.lean
line: 57
kind: def
visibility: public
verdict: YES-but-generalise-first
cost: MODERATE
junk: KEEP
rationale: The multivariate Hasse derivative is standard (DKSS method of multiplicities, nLab, Roth-type arguments) and absent from mathlib, which has only univariate Polynomial.hasseDeriv and LaurentSeries.hasseDeriv; it should ship with its coefficient spelled via the multi-index binomial Finsupp.choose and ideally with an MvPowerSeries companion beside MvPowerSeries.pderiv.
action: Upstream to a new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean together with Finsupp.choose (from the hasseCoeff report), coeff_hasseDeriv, hasseDeriv_hasseDeriv, pderiv_hasseDeriv, factorial_smul_hasseDeriv_single, uniqueAlgEquiv_hasseDeriv; locally keep as is (used in 8 Roth files).
---

# MvPolynomial.hasseDeriv

## Inventory entry

### `def MvPolynomial.hasseDeriv`
- **Type**: `{σ R : Type*} → [CommSemiring R] → (d : σ →₀ ℕ) → MvPolynomial σ R →ₗ[R] MvPolynomial σ R`
- **What**: The multivariate Hasse derivative `Δ_d`, the `R`-linear map with `Δ_d (a X^k) = binom(k, d) a X^(k - d)` (zero unless `d ≤ k`); over a `ℚ`-algebra it is `(∏ j (d j)!)⁻¹ ∏ j ∂_j^(d j)`.
- **How**: `Finsupp.lsum R (fun k ↦ (monomial (k - d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R)))` precomposed with `AddMonoidAlgebra.coeffLinearEquiv R`, i.e. extend the monomial rule linearly; key API lemma `hasseDeriv_monomial` is proved by `simp [hasseDeriv]`.
- **Hypotheses**: `[CommSemiring R]` (section variable); no other hypotheses.
- **Uses from project**: `MvPolynomial.hasseCoeff`
- **Used by**: Roth/HasseDeriv.lean (all lemmas from `hasseDeriv_monomial` to `factorial_smul_hasseDeriv_single`, ~60 occurrences); Roth/CoeffNorm.lean (`abs_coeff_hasseDeriv_le`, `normOne_hasseDeriv_le`, generalised-Wronskian degree/coefficient bounds l.247-265); Roth/GenWronskian.lean (`genWronskian` l.34, `kronHasse` l.146, l.241-245); Roth/Index.lean (l.63, l.70, taylor/index lemmas); Roth/Taylor.lean (l.103-105, coefficient of `taylor` as `eval α (hasseDeriv d P)`); Roth/Separation.lean (l.147-148); Roth/Theta.lean (l.378-383); Roth/MainLemma.lean (27 occurrences, l.362-745); Roth/Main.lean (l.385, l.392). Roth/Wronskian.lean uses the univariate `Polynomial.hasseDeriv`, not this one.
- **Visibility**: public
- **Lines**: 57–60, proof length 3 lines (definition body)
- **Notes**: `noncomputable`. Argument order of the coefficient is `hasseCoeff d k` (lower index first), see the parent report `MvPolynomial.hasseCoeff.md`.

## Junk check (Step 8)
- Used anywhere? Yes, heavily: 8 project files besides the declaring one; it is the central operator of the Roth formalisation (index, Taylor expansion, generalised Wronskians, main lemma).
- Wrapper of 1–2 mathlib calls? No in substance: it is a new linear operator (lsum over monomials) with a full lemma API; mathlib has no multivariate counterpart.
- Does mathlib have it? No (Phase 5): only `Polynomial.hasseDeriv` (univariate, `Semiring R`), `LaurentSeries.hasseDeriv` (univariate Laurent series), `MvPolynomial.pderiv`, `MvPowerSeries.pderiv`.
- Too specific / inline? No.
- Well-chosen definition? Yes; matches the paper and mathlib's univariate definition pattern (`lsum` of `monomial (k - d)` scaled by a binomial), with compatibility lemmas to `Polynomial.hasseDeriv` (`hasseDeriv_single_aeval_X`, `uniqueAlgEquiv_hasseDeriv`) and to `pderiv` (`factorial_smul_hasseDeriv_single`).
- Conclusion: `KEEP` — action: keep; upstream (see verdict).

## Mathlibable assessment (Step 9)

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` compiles)
- decl `MvPolynomial.hasseDeriv`: resolved at Roth/HasseDeriv.lean:57
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseDeriv` is a definition of the following: for a commutative semiring `R`, a set of variables `σ` and a multi-index `d ∈ ℕ^(σ)`, the Hasse derivative `Δ_d : R[X_σ] → R[X_σ]` is the `R`-linear map determined on monomials by
`Δ_d (X^k) = binom(k, d) X^(k-d)`, where `binom(k,d) = ∏_j binom(k_j, d_j)` (zero unless `d ≤ k`). Equivalently `Δ_d P` is the coefficient of `Z^d` in `P(X + Z)`, and over `ℚ` it equals `(1/d!) ∂^d`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables (arbitrary).
- `R : Type*`, `[CommSemiring R]` — coefficient ring.
- `d : σ →₀ ℕ` — order multi-index of the derivative.

Hypotheses (Lean side):
- none.

Conclusion (math): the linear operator `Δ_d`.

Conclusion (Lean): n/a — definition (`MvPolynomial σ R →ₗ[R] MvPolynomial σ R`).

### Size classification (Phase 2a)

Verdict: BIG
Reason: introduces a named mathematical operator (new structure-level definition, listed under `## Main definitions`) that the whole project is built on.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3 substantive lines (one `∘ₗ` expression split over 3 lines)
One-liner verdict: MULTI-LINE (and in any case a genuine new operator, not an alias)

Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multivariate Hasse derivative polynomial several variables definition binomial coefficient monomial | yes | `D^e f = Σ_a binom(a,e) f_a x^(a-e)`; equivalently coeff of `z^e` in `f(x+z)` | arXiv 2111.07572, 2403.19824, 2603.03841, 2205.00342; exactly our definition |
| 2 | WebSearch (general form) | Hasse-Schmidt derivation power series ring several variables higher derivation divided power | yes | multivariate Hasse–Schmidt derivations `A → A[[s_1..s_q]]` indexed by `ℕ^q` | Wikipedia "Hasse–Schmidt derivation"; Narváez Macarro arXiv 1807.10193, 1901.03580; our `Δ_d` is the canonical HS derivation of `R[X]` (coefficients of `P(X+S)`) |
| 3 | WebSearch (named-after / aliases) | "Hasse derivatives" multiplicity polynomial method finite fields Dvir Kopparty Saraf Sudan | yes | `P^(β)` = coeff of `y^β` in `P(x+y)`; multiplicity via vanishing of `P^(β)`, `|β| < M` | DKSS (method of multiplicities), arXiv 1909.03180, 1909.02431, 0912.1436; standard alias "Hasse derivative w.r.t. x^β" |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for hasse / Delta_ / binom | yes | l.122-137: `Δ_i(x^k) = ∏ binom(k_j,i_j) x^(k-i)`, `Δ_i = (1/i!) ∂^i` over ℚ, "over any commutative semiring by casting the binomial coefficients"; l.148-153 Lean implementation note | project source paper §1 |
| 6 | nLab | nLab Hasse-Schmidt derivative | yes | `P^(n)` for polynomials over a commutative rig, with a section on several indeterminates | nLab "Hasse-Schmidt derivative" and "Hasse-Schmidt derivation"; confirms commutative (semi)ring generality |
| 7 | nCatLab | (same nLab pages, #6) | partial | link to differential linear logic / graded bimonoids | no further categorical formulation needed for an operator on polynomial rings |
| 8 | Stacks Project | — | n/a | — | Stacks treats differential operators/divided powers in general; no standalone multivariate Hasse derivative tag, and the concept here is polynomial-algebraic, not scheme-theoretic |
| 9 | MathOverflow / Math.SE | (results of #3; DKSS restatements) | partial | same coefficient-of-`P(x+y)` definition | no dedicated MO thread surfaced; usage in MO-cited multiplicity-method papers agrees |
| 10 | recent arXiv (last 5 years) | (results of #1, #3) | yes | arXiv 2403.19824 (2024), 2111.07572 (2021), 2511.05176 (2025), 1909.03180 | all use `binom(α,β)` componentwise, arbitrary field / ring, finitely many variables |

### Literature summary (Phase 3)

Concept identified as: multivariate Hasse derivative (Hasse–Schmidt derivative of several variables) `Δ_d`, the canonical higher derivation of `R[X_σ]`.
Sources agree on the standard form: yes — `Δ_d P = [Z^d] P(X+Z)`, i.e. `Δ_d X^k = binom(k,d) X^(k-d)`.
Most general standard form: over any commutative (semi)ring `R` (nLab: commutative rig; paper: any commutative semiring), any (finite in the literature) set of variables; it also makes sense coefficientwise on formal power series `R[[X_σ]]`, and as a Hasse–Schmidt derivation of any `R`-algebra.
Generality dimensions where the literature varies:
  - coefficient ring: field (coding theory) to commutative semiring (nLab, paper); ours is commutative semiring, the most general available for `MvPolynomial`.
  - ambient object: polynomials (most sources) to power series / arbitrary algebras (Hasse–Schmidt derivations); mathlib already splits polynomials and power series into separate types with separate `pderiv`s.
  - index set: `{1..n}` vs arbitrary; ours is arbitrary `σ`.
Disagreement with the literature: none mathematically.

### Generality analysis — `MvPolynomial.hasseDeriv`

Literature-standard form (from Phase 3): `Δ_d X^k = binom(k,d) X^(k-d)` on `R[X_σ]`, `R` a commutative semiring; coefficientwise extension to `R[[X_σ]]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring (rig) | no (for `MvPolynomial`) | `MvPolynomial σ R` itself requires `CommSemiring R`; `[Semiring R]` fails to elaborate (evidence `weaken_semiring_fails.lean`) |
| 2 | `σ : Type*` | arbitrary | finite index set | no (already more general) | — |
| 3 | `d : σ →₀ ℕ` | finitely supported | multi-index | no | finiteness needed for `binom(k,d)` as a finite product |
| 4 | ambient type `MvPolynomial σ R` | polynomials | polynomials (also power series) | yes, as a companion | `MvPowerSeries.hasseDeriv d` defined coefficientwise compiles over plain `[Semiring R]`, and `↑(hasseDeriv d P) = MvPowerSeries.hasseDeriv d ↑P` is proved (evidence `generalise_mvpowerseries.lean`); but mathlib keeps polynomial and power-series operators as separate defs (cf. `MvPolynomial.pderiv` vs `MvPowerSeries.pderiv`), so this is a companion, not a replacement |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (for an operator on `MvPolynomial`; the only typeclass weakening tried, `Semiring R`, is verified to fail).
Number of weakening opportunities found: 0 on the declaration itself; 1 verified companion generalisation (`MvPowerSeries`, compiles).
Cost of restatement: CHEAP (companion is ~10 lines plus compatibility lemma, both compiled).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | purely algebraic |
| 3 | construction vs universal property? | partial | characterise as the canonical Hasse–Schmidt derivation `P ↦ P(X+Z)` (coefficient of `Z^d` in `aeval (X + Z) P`) | Taylor expansion `P(X+Z) = Σ_d Δ_d P · Z^d` (project has a `taylor` file); not required for the definition itself — record as a follow-up lemma, not a replacement |
| 4 | set-with-predicate to bundled substructure? | no | — | already a bundled `LinearMap` |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | no | — | concrete operator |
| 7 | concrete index to general? | yes (coefficient spelling) | write the coefficient as `k.choose d` with `Finsupp.choose` (multi-index binomial, top index first) rather than the Hasse-specific `hasseCoeff d k` | statements like `coeff_hasseDeriv : coeff e (Δ_d P) = (e + d).choose d * coeff (e + d) P` match `Polynomial.hasseDeriv_coeff : (n + k).choose k * …` verbatim; reusable multi-index binomial API |
| 8 | concrete-via-abstract? | no | the body is genuinely about polynomials (monomial, coefficients); `hasseCoeff` is the abstract piece and is handled by its own report | — |
| 9 | false-generalisation guard | no false generalisation | `hasseDeriv'` with `k.choose d` is `rfl`-equal to `hasseDeriv` (evidence file); the MvPowerSeries companion agrees on polynomials (proved) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: same operator, coefficient spelled with `Finsupp.choose`:
    `noncomputable def hasseDeriv (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R := Finsupp.lsum R (fun k ↦ (monomial (k - d)).comp (LinearMap.lsmul R R (k.choose d : R))) ∘ₗ (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap`, plus optional companion `MvPowerSeries.hasseDeriv` over `[Semiring R]`.
  - Cost: MODERATE (def CHEAP; rename of `hasseCoeff d k` to `k.choose d` across Roth/HasseDeriv.lean, Roth/CoeffNorm.lean, Roth/Taylor.lean if done locally).
  - Mathlib downstream this enables: uniform statements with univariate `Polynomial.hasseDeriv_coeff` / `hasseDeriv_monomial`; multi-index binomial lemmas shared with a future multivariate Taylor / binomial theorem; power-series companion next to `MvPowerSeries.pderiv` (Mathlib/RingTheory/MvPowerSeries/Derivative.lean).
  - Real mathematical improvement: the coefficient is the standard multi-index `binom(k,d)`, not a Hasse-specific number, so naming it as such matches the literature and mathlib's univariate statements.

### Proof strategy — `MvPolynomial.hasseDeriv`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no (definition by linear extension from monomials is how mathlib defines `Polynomial.hasseDeriv` and `MvPolynomial.pderiv` coefficients) | — | — |
| 5 | missing mathlib helpers | yes | `Finsupp.choose` multi-index binomial and its composition identity (project's private `hasseCoeff_mul_hasseCoeff`), needed for `hasseDeriv_hasseDeriv` | follow-up / same PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (mirrors `Polynomial.hasseDeriv := lsum fun i ↦ monomial (i - k) ∘ₗ DistribSMul.toLinearMap R R (i.choose k)`; the extra `coeffLinearEquiv` is the standard bridge from `MvPolynomial` to `Finsupp.lsum`).
  - Missing mathlib API: multi-index binomial `Finsupp.choose` (row 5).

### Diamond / defeq risk — `MvPolynomial.hasseDeriv`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | defines a `LinearMap`, no instances; the only scalar action is `R` on `MvPolynomial σ R` (unique `Module` instance) |
| 2 | Reducibility leak | none | plain semireducible `noncomputable def`; consumers go through `hasseDeriv_monomial` / `coeff_hasseDeriv`, and `simp [hasseDeriv]` is used only inside the two API proofs |
| 3 | Non-canonical unfolding | low | unfolding exposes `Finsupp.lsum` and `coeffLinearEquiv`; harmless because `coeff_hasseDeriv` is the stated interface and every downstream identity is proved by `ext` + `coeff_hasseDeriv` |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `σ R : Type*` independent; MvPowerSeries companion and restatement in the evidence file elaborate with `Type*` |
| 6 | Coercion ambiguity | none | coerces to a function via the standard `LinearMap` `FunLike`; name `MvPolynomial.hasseDeriv` does not clash (mathlib has `Polynomial.hasseDeriv`, `LaurentSeries.hasseDeriv` in other namespaces) |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none
Recommended mitigations: n/a

### Mathlib search-status: `MvPolynomial.hasseDeriv`

[A] Lean-Finder       "multivariate Hasse derivative Δ_d on MvPolynomial sending X^k to binomial(k,d) X^(k-d)"   no hits (only `Polynomial.hasseDeriv*`, `MvPolynomial.pderiv_monomial*`)
[B] Loogle            `(_ →₀ ℕ) → MvPolynomial _ _ →ₗ[_] MvPolynomial _ _`; `MvPolynomial.monomial, Nat.choose`   no hits
[C] LeanSearch        "Hasse derivative of multivariate polynomial with multi-index"   no hits (univariate `Polynomial.hasseDeriv`, `MvPolynomial.pderiv`, `mkDerivation`)
[D] Grep mathlib src  `def hasseDeriv` (only Mathlib/Algebra/Polynomial/HasseDeriv.lean:59 and Mathlib/RingTheory/LaurentSeries.lean:118); `hasse` case-insensitive in MvPolynomial / MvPowerSeries dirs; `deriv` defs in Algebra/MvPolynomial (only `pderiv`, `mkDerivation*`); `taylor` in MvPolynomial / MvPowerSeries   no multivariate hit; found `MvPowerSeries.pderiv` (Mathlib/RingTheory/MvPowerSeries/Derivative.lean) as the natural neighbour
[E] Name pattern      `MvPolynomial.hasseDeriv`, `MvPowerSeries.hasseDeriv`   no hits

Searched for both the user's form and the literature-standard form (Hasse–Schmidt / power-series version).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); building blocks `Polynomial.hasseDeriv` (univariate), `MvPolynomial.pderiv`, `MvPowerSeries.pderiv` exist.

### Normal-form check — `MvPolynomial.hasseDeriv`

Equivalent formalisms: linear extension of the monomial rule (ours); coefficient formula `coeff e (Δ_d P) = binom(e+d,d) coeff (e+d) P`; `[Z^d] P(X+Z)`; `(1/d!) ∂^d` over `ℚ`-algebras.
Does mathlib already have a canonical form? For one variable yes: `Polynomial.hasseDeriv` (linear extension), with `hasseDeriv_coeff` and `factorial_smul_hasseDeriv` as equivalence lemmas.
Our statement follows the same canonical form and provides the analogous lemmas `coeff_hasseDeriv`, `factorial_smul_hasseDeriv_single`, plus bridges `hasseDeriv_single_aeval_X`, `uniqueAlgEquiv_hasseDeriv` to the univariate canonical form.
RHS convention respected? yes.

### Syntactic generality — `MvPolynomial.hasseDeriv`

Alternative restatements attempted:
- coefficient `hasseCoeff d k` (current)
- coefficient `k.choose d` via `Finsupp.choose` (compiles, `rfl`-equal; evidence file)
- coefficientwise power-series operator `MvPowerSeries.hasseDeriv` (compiles, agrees on polynomials; evidence file)
Chosen restatement: `k.choose d` coefficient, with the power-series companion optional.
Justification: matches `Polynomial.hasseDeriv`'s `i.choose k` and the literature `binom(k,d)`; argument order `binom(top, bottom)`.

### Superfluous-argument audit — `MvPolynomial.hasseDeriv`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial` itself (Semiring weakening fails) |
| 2 | `σ` | yes | variables |
| 3 | `d : σ →₀ ℕ` | yes | order of the derivative |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (coefficient as `k.choose d`, `Finsupp.choose`)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.hasseDeriv`

Internal use count: about 90 occurrences of `hasseDeriv` (bare word) outside the declaring file, across 8 files (Roth/Wronskian.lean excluded: it uses univariate `Polynomial.hasseDeriv`)
External-to-file callers: 8 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:136 | `|(((hasseDeriv d P).coeff e : ℤ) : ℝ)| ≤ 2 ^ (∑ j, r j) * B` (5 occurrences in file) |
| Roth/CoeffNorm.lean:247 | `degreeOf j (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det ≤ l * r j` |
| Roth/GenWronskian.lean:34 | `(Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)).det` (generalised Wronskian; 9 occurrences) |
| Roth/GenWronskian.lean:146 | `fun P ↦ kronecker k (hasseDeriv d P)` |
| Roth/Index.lean:63 | `d ∈ (taylor α P).support ↔ eval α (hasseDeriv d P) ≠ 0` (8 occurrences) |
| Roth/Taylor.lean:103 | `(taylor α (monomial k a)).coeff d = eval α (hasseDeriv d (monomial k a))` (7 occurrences) |
| Roth/Separation.lean:147 | `hasseDeriv (d.mapDomain some + Finsupp.single none ν) (rename some U * …)` (7 occurrences) |
| Roth/Theta.lean:378 | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det ≠ 0` (10 occurrences) |
| Roth/MainLemma.lean:362 | `|(diag (hasseDeriv j W) %ₘ f).coeff i| ≤ C` (27 occurrences, l.362-745) |
| Roth/MainLemma.lean:462 | `eval … (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))` |
| Roth/Main.lean:385 | `|eval (fun _ ↦ α) (hasseDeriv i Q)| < C` (3 occurrences) |

Inline-derivation grep: (none) — no file re-derives the operator via `Finsupp.lsum`/`monomial (k - d)` or via iterated `pderiv` divided by factorials; the only `pderiv` iterate is `factorial_smul_hasseDeriv_single` in the declaring file.

### Composition check (Phase 6)

Can `MvPolynomial.hasseDeriv` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(∏ j, (d j)!)⁻¹ • ∏ j, (pderiv j)^[d j]`
  - Mathlib decls used: `MvPolynomial.pderiv`, `Function.iterate`
  - Result: fails — needs factorials invertible (only over `ℚ`-algebras); the whole point of Hasse derivatives is characteristic-free (here `R = ℤ` is used in Roth/MainLemma.lean).
Attempt 2: transport `Polynomial.hasseDeriv` along `finSuccEquiv` / `optionEquivLeft` one variable at a time and compose
  - Mathlib decls used: `Polynomial.hasseDeriv`, `MvPolynomial.optionEquivLeft`, `Polynomial.map`
  - Result: fails as a ≤3-call composition — requires induction over the support of `d` and an independence-of-order argument; a new proof, not a composition.
Attempt 3: `[Z^d] (aeval (fun j ↦ X j + Z j) P)` in `MvPolynomial (σ ⊕ σ) R`
  - Result: partial — gives the values but not a linear map without further API (coefficient extraction in one block of variables), and no lemmas.

Conclusion: NOT-COMPOSABLE

## Verdict: `MvPolynomial.hasseDeriv`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): multivariate Hasse derivative `Δ_d X^k = binom(k,d) X^(k-d)` is standard (DKSS method of multiplicities; arXiv 2111.07572, 2403.19824; nLab "Hasse-Schmidt derivative" several-indeterminates section; project paper §1).
- Generality analysis (Phase 4): MAXIMALLY GENERAL for `MvPolynomial` (`Semiring R` verified to fail); Phase 4c MODERN-IDIOM: coefficient should be the multi-index binomial `Finsupp.choose`; verified power-series companion over `Semiring R`.
- Mathlib search (Phase 5): not in mathlib; only univariate `Polynomial.hasseDeriv`, `LaurentSeries.hasseDeriv`, and `MvPolynomial.pderiv` / `MvPowerSeries.pderiv`.
- Composition check (Phase 6): NOT-COMPOSABLE (iterated `pderiv` needs `ℚ`; variable-by-variable transport is a new proof).

**Rationale:**

Mathlib has the univariate Hasse derivative (`Polynomial.hasseDeriv`, with `hasseDeriv_coeff`, `hasseDeriv_comp`, `factorial_smul_hasseDeriv`) and the multivariate partial derivatives `MvPolynomial.pderiv`, but no multivariate Hasse derivative. That is a concrete gap: characteristic-free multivariate Taylor expansion, vanishing-to-order / multiplicity of multivariate polynomials (Schwartz–Zippel with multiplicities, DKSS), index arguments in Diophantine approximation (Roth, Thue–Siegel), and generalised Wronskians all need `Δ_d` with `d` a multi-index; over `ℤ` or `𝔽_p` it cannot be replaced by `(1/d!) ∂^d`. The project's definition already follows mathlib's univariate pattern and comes with a full API (`coeff_hasseDeriv`, composition rule `hasseDeriv_hasseDeriv`, `pderiv_hasseDeriv`, `factorial_smul_hasseDeriv_single`, compatibility with `Polynomial.hasseDeriv` and with `rename`/`map`), all of which should go upstream together. Risk is LOW.

The generalise-first part is a single mechanical, verified restatement inherited from the parent `MvPolynomial.hasseCoeff` (YES-but-generalise-first): the coefficient should be the multi-index binomial `Finsupp.choose k d` (top index first), which is `rfl`-equal (evidence file) and makes `coeff_hasseDeriv` read exactly like `Polynomial.hasseDeriv_coeff`. Optionally add the coefficientwise `MvPowerSeries.hasseDeriv` (compiles over a plain `Semiring R`, agrees with ours on polynomials, proved) next to `MvPowerSeries.pderiv`; mathlib keeps polynomial and power-series operators separate, so this is a companion rather than a replacement.

Reason for the generalisation: MODERN-IDIOM (coefficient as the standard multi-index binomial; Q7), plus a verified companion generalisation to `MvPowerSeries`.
Proposed restatement:
```lean
namespace MvPolynomial
variable {σ R : Type*} [CommSemiring R]
/-- The multivariate Hasse derivative `Δ_d`, sending `monomial k a` to
`monomial (k - d) (k.choose d * a)`. -/
noncomputable def hasseDeriv (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ ↦
      (monomial (k - d)).comp (LinearMap.lsmul R R (k.choose d : R))) ∘ₗ
    (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap
theorem coeff_hasseDeriv (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (hasseDeriv d P).coeff e = ((e + d).choose d : R) * P.coeff (e + d) := by
  sorry -- port of the current proof
end MvPolynomial
```
Estimated cost of regeneralisation: MODERATE (definition CHEAP; renaming `hasseCoeff d k` to `k.choose d` in Roth/HasseDeriv.lean, Roth/CoeffNorm.lean, Roth/Taylor.lean if adopted locally).
Mathlib downstream this enables:
- statements uniform with `Polynomial.hasseDeriv_coeff` / `hasseDeriv_monomial` (`(n + k).choose k`);
- multi-index binomial lemmas (`Finsupp.choose_mul_choose`) reusable for a multivariate binomial/Taylor theorem;
- a power-series companion beside `MvPowerSeries.pderiv` in Mathlib/RingTheory/MvPowerSeries/Derivative.lean;
- multiplicity of a multivariate polynomial at a point (`∀ d, |d| < M → eval a (Δ_d P) = 0`), currently impossible to state characteristic-free in mathlib.
Next action: run `/generalise MvPolynomial.hasseDeriv`, then open "feat(Algebra/MvPolynomial): multivariate Hasse derivatives" adding Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, bundled with `Finsupp.choose` (parent report) and the lemmas `hasseDeriv_monomial`, `coeff_hasseDeriv`, `hasseDeriv_zero`, `hasseDeriv_C`, `hasseDeriv_map`, `hasseDeriv_rename`, `hasseDeriv_hasseDeriv`, `pderiv_hasseDeriv`, `factorial_smul_hasseDeriv_single`, `hasseDeriv_single_aeval_X`, `uniqueAlgEquiv_hasseDeriv`.

---

## Next step

Run `/generalise MvPolynomial.hasseDeriv`; upstream with the coefficient spelled `k.choose d` (`Finsupp.choose`) as a new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean together with the Hasse-derivative API from Roth/HasseDeriv.lean.

## Evidence
- `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/generalise_mvpowerseries.lean` (compiles with `lake env lean`, no errors or warnings): defines `MvPowerSeries.hasseDeriv` over `[Semiring R]`, proves `MvPolynomial.coe_hasseDeriv : ↑(hasseDeriv d P) = MvPowerSeries.hasseDeriv d ↑P`, and checks that the `Finsupp.choose`-spelled `hasseDeriv'` is `rfl`-equal to `MvPolynomial.hasseDeriv`.
- `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/weaken_semiring_fails.lean` (FAILS by design, this failure is the evidence): with `[Semiring R]` the definition errors with "failed to synthesize instance CommSemiring R" because `MvPolynomial σ R` requires it.
- Mathlib greps: `def hasseDeriv` (only Polynomial and LaurentSeries), `hasse` in MvPolynomial/MvPowerSeries dirs (none), derivative defs in Algebra/MvPolynomial (`pderiv`, `mkDerivation`), Mathlib/RingTheory/MvPowerSeries/Derivative.lean (`MvPowerSeries.pderiv`).
- LeanSearch, Lean-Finder: univariate / pderiv only; Loogle: two queries, no hits.
- WebSearch: 4 queries (table rows 1, 2, 3, 6). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rnw hasseDeriv Roth/` for Used-by and call sites.
