---
decl: Roth.det_hasseDeriv_separated
file: Roth/Separation.lean
line: 351
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The factorisation GW_(D,nu)(sum_rho phi_rho(x_none) psi_rho(x_tau)) = GW_D(psi) W(phi) (Hasse matrix of a separated sum is A B^T) is absent from mathlib, which has no multivariate Hasse derivative or n-ary Wronskian; it is the natural product formula for the planned generalized-Wronskian API and weakens from [Field K] to [CommRing R] with the proof unchanged (verified), but should ship at the optionElim index decided for its helper.
action: Upstream with Roth.genWronskian and Roth.wronskian (CommRing versions) in the planned Mathlib/RingTheory/MvPolynomial/Wronskian.lean, restated over [CommRing R] with matrix index (D mu).optionElim nu; locally keep, updating the single call site exists_rat_factors_det_hasseDeriv_aux (Roth/Separation.lean:529) if the index changes.
---

# Roth.det_hasseDeriv_separated

## Inventory entry

### `theorem Roth.det_hasseDeriv_separated`
- **Type**: `{τ K : Type*} [Field K] {l : ℕ} (D : Fin l → τ →₀ ℕ) (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K) : (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none ν) (∑ ρ, Polynomial.aeval (X none) (φ ρ) * rename some (ψ ρ))).det = rename some (genWronskian D ψ) * Polynomial.aeval (X none) (wronskian φ)` (section `[Fintype τ] [DecidableEq τ]` omitted; confirmed by `#check`, evidence (0))
- **What**: For a separated sum `P = ∑_ρ φ_ρ(x_none) ψ_ρ(x_τ)`, the determinant `det(Δ_{(D μ, ν)} P)_{μ,ν}` equals `GW_D(ψ)(x_τ) · W(φ)(x_none)`, the product of the generalized Wronskian of `ψ` and the (Hasse) Wronskian of `φ`.
- **How**: Unfolds `genWronskian`, `wronskian`; pushes `rename some` and `aeval (X none)` inside the determinants with `AlgHom.map_det`; rewrites `det B = det Bᵀ` (`Matrix.det_transpose`) and combines with `Matrix.det_mul`; then entrywise (`Matrix.ext`, `map_sum`, `Matrix.mul_apply`, `Finset.sum_congr`) each summand is handled by `hasseDeriv_rename_mul_aeval` after `mul_comm`, closing with `rfl`.
- **Hypotheses**: `[Field K]` (section variable; only needed because the parent defs `genWronskian`, `wronskian` are stated over a field).
- **Uses from project**: `Roth.genWronskian`, `Roth.wronskian`, `Roth.wronskianMatrix`, `MvPolynomial.hasseDeriv`, `Roth.hasseDeriv_rename_mul_aeval`
- **Used by**: `Roth.exists_rat_factors_det_hasseDeriv_aux` (private) at Roth/Separation.lean:529 (`rw [hFdef, RingHom.map_det, ← det_hasseDeriv_separated D φ ψ, ← hPQ]`). Also named in the module docstring (Separation.lean:33). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 351–366, proof length 11 lines
- **Notes**: Matrix index `(D μ).mapDomain some + Finsupp.single none ν` is the non-canonical spelling flagged in the `Roth.hasseDeriv_rename_mul_aeval` report (mathlib normal form `(D μ).optionElim ν`).

## Junk check (Step 8)
- Used anywhere? Yes, once (Separation.lean:529), the `F = G·W` step of Lemma 2.
- Wrapper of 1–2 mathlib calls? No: `det_mul` + `det_transpose` + two `map_det` + an entrywise identity via the project's `hasseDeriv_rename_mul_aeval`.
- Does mathlib have it? No (no multivariate Hasse derivative, no n-ary or generalized Wronskian; Phase 5).
- Too specific (inline?)? Single use, but it is exactly the displayed identity of the source (clean.tex:408–417) and a clean named statement; inlining it would bloat the already long private aux lemma.
- Well-chosen? Yes, modulo the index spelling.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name does not end `_aux`; docstring does not start internal/auxiliary; Step 8 = KEEP; qualified name `Roth.det_hasseDeriv_separated` (and any `det_hasseDeriv`/`genWronskian`) absent from `.lake/packages/mathlib/Mathlib/` (grep, no hits). Not a glue lemma (11-line proof), so no inheritance; full workflow below.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` compiles with no errors)
- decl `Roth.det_hasseDeriv_separated`: resolved at Roth/Separation.lean:351
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`); Lemma 2 of the source, `det(Δ_{Dμ} Δ^{(none)}_ν R) = U(x_τ) V(x_none)`.

### Statement (Phase 1)

`Roth.det_hasseDeriv_separated` is a theorem stating the following: let `φ_0, …, φ_{l-1} ∈ K[y]` and `ψ_0, …, ψ_{l-1} ∈ K[x_τ]`, and put `P = ∑_ρ φ_ρ(x_*) ψ_ρ(x_τ) ∈ K[x_τ, x_*]`. For multi-indices `D_0, …, D_{l-1}` on `τ`, the determinant of the `l × l` matrix `(Δ_{D_μ} (1/ν!) ∂^ν/∂x_*^ν P)_{μ,ν}` equals `GW(ψ; Δ_{D_0}, …, Δ_{D_{l-1}})(x_τ) · W(φ)(x_*)`. Equivalently, the matrix is `A Bᵀ` with `A_{μρ} = Δ_{D_μ} ψ_ρ`, `B_{νρ} = D^{(ν)} φ_ρ`, so its determinant is `det A · det B`.

Variables / typeclasses involved (Lean side):
- `τ : Type*` — the non-distinguished variables; `none : Option τ` is the distinguished one.
- `K`, `[Field K]` — coefficients.
- `l : ℕ` — size of the family.
- `D : Fin l → τ →₀ ℕ` — Hasse operators in the `τ`-variables.
- `φ : Fin l → Polynomial K`, `ψ : Fin l → MvPolynomial τ K` — the two factor families.

Hypotheses (Lean side):
- none (no independence or degree hypotheses).

Conclusion (math): `det(Δ_{(D_μ, ν)} ∑_ρ φ_ρ(x_*)ψ_ρ(x_τ)) = GW_D(ψ)(x_τ) · W(φ)(x_*)`.

Conclusion (Lean): `(Matrix.of fun μ ν ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none ν) (∑ ρ, aeval (X none) (φ ρ) * rename some (ψ ρ))).det = rename some (genWronskian D ψ) * aeval (X none) (wronskian φ)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: one step in the proof of Lemma 2 of the source; not a main result and introduces no structure.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 11
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | generalized Wronskian of f(x)g(y) separated sum factorization product of Wronskians determinant | partial | generalized Wronskian `det(D_i f_j)` with constant-coefficient operators (Wikipedia "Wronskian"; arXiv 1310.4683; Gatto–Scherbak arXiv 1310.3345) | no source states the separated-sum factorisation by name |
| 2 | WebSearch (general form) | Wronskian of products of functions in separate variables W(f_i(x) g_j(y)) Kronecker product determinant multivariate | partial | `det(AB) = det A det B` / Cauchy–Binet framework; Kronecker determinant (arXiv 2012.10240) | the identity is a direct `det(ABᵀ)` instance, not a named result |
| 3 | WebSearch (named-after / context) | Roth lemma generalized Wronskian F = U(x_1..x_{p-1}) V(x_p) proof det A det B Schmidt | yes | Roth 1955 (Mathematika) Lemma 1/2; Bombieri–Gubler App. D.6 (induction proof); Bostan–Dumas arXiv 1301.6598 | the factorisation is the induction step of Roth's / Bombieri–Gubler's proof of the Wronskian lemma |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `det A`, `transpose` | yes | lines 408–417: `A_{μρ} = Δ_μ ψ_ρ`, `B_{νρ} = Δ_ν φ_ρ`, "The matrix defining F is A Bᵀ, so F = det A det B", `GW = det(∑_ρ Δ_μ (1/ν!) ∂^ν φ_ρ ψ_ρ)` | exactly this theorem |
| 6 | nLab | generalized Wronskian / Hasse-Schmidt derivative | partial | Hasse–Schmidt derivations with Leibniz rule; no Wronskian page treating separated sums | consistent with the factorwise action used in the proof |
| 7 | nCatLab | (same as nLab) | n/a | — | not a categorical concept; only the nLab Hasse–Schmidt page exists |
| 8 | Stacks Project | n/a | n/a | — | Stacks has no Wronskian/Hasse-operator material; not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | (covered by #1–#3; no thread surfaced) | no | — | identity is an elementary `det(ABᵀ)` step, not discussed separately |
| 10 | recent arXiv | Bostan–Dumas 1301.6598, arXiv 1611.00248 (Wronskians and formal power series) surfaced by #1/#3 | partial | multivariate generalized Wronskian criterion; proofs by Kronecker substitution or by induction on variables | the induction proof (Bombieri–Gubler D.6.1) uses this factorisation |

### Literature summary (Phase 3)

Concept identified as: product formula for generalized (Ostrowski–Roth) Wronskians of a sum of separated products: with operators `Δ_μ` in one block of variables and `D^{(ν)}` in the other, `det(Δ_μ D^{(ν)} ∑_ρ φ_ρ ψ_ρ) = det(Δ_μ ψ_ρ) · det(D^{(ν)} φ_ρ)`.
Sources agree on the standard form: yes — it is stated (as a step, not a numbered lemma) in Roth 1955 and in the project source (clean.tex:408–417), and used in the induction proof of the Wronskian criterion (Bombieri–Gubler D.6.1).
Most general standard form: for commutative coefficient ring `R`, disjoint variable blocks `X`, `Y`, families `p_ρ ∈ R[X]`, `q_ρ ∈ R[Y]` and Hasse operators `Δ_μ` on `X`, `Δ'_ν` on `Y`: `det(Δ_μ Δ'_ν ∑_ρ p_ρ q_ρ) = det(Δ_μ p_ρ) det(Δ'_ν q_ρ)`.
Generality dimensions where the literature varies:
  - coefficients: `ℚ`/field (project, source) up to any commutative ring (determinants need only `CommRing`).
  - second block: one variable with operators `D^{(ν)}` (project, source) up to arbitrary block and arbitrary operators.
Disagreement with the literature: none mathematically; the project is the source's specialisation (field, one-variable second block with `ν = 0..l-1`).

### Generality analysis — `Roth.det_hasseDeriv_separated`

Literature-standard form (from Phase 3): over `[CommRing R]`, `det(Δ_{(D μ, ν)} ∑ φ_ρ(x_*)ψ_ρ(x_τ)) = GW_D(ψ) · W(φ)`; more generally the two-block Sum form with arbitrary operators on both blocks.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | commutative ring | yes | verified: with `CommRing` versions of `genWronskian`/`wronskian` (as already proposed and verified in their reports) the project proof compiles verbatim over `[CommRing R]` (evidence (1)); `hasseDeriv_rename_mul_aeval` is `CommSemiring` |
| 2 | index `(D μ).mapDomain some + single none ν` | non-canonical | `(D μ).optionElim ν` | yes (restatement) | inherits the index normalisation verified for `hasseDeriv_rename_mul_aeval` (its evidence (1)); not re-compiled here |
| 3 | second block `{none}`, operators `D^{(ν)}`, `ν < l` | one variable | arbitrary block / operators | possibly | would need a two-block genWronskian-of-Sum statement; not compiled, so NOT claimed as a verified weakening |
| 4 | `τ : Type*` | arbitrary | arbitrary | no | `Fintype`/`DecidableEq` already omitted |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (coefficients)
Number of weakening opportunities found: 1 verified (`[Field K]` to `[CommRing R]`, evidence (1), `lake env lean` clean), plus 1 index restatement inherited from the helper's verified evidence.
Proposed restatement:

```lean
theorem det_hasseDeriv_separated {τ R : Type*} [CommRing R] {l : ℕ} (D : Fin l → (τ →₀ ℕ))
    (φ : Fin l → Polynomial R) (ψ : Fin l → MvPolynomial τ R) :
    (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).optionElim ν)
        (∑ ρ, Polynomial.aeval (X none : MvPolynomial (Option τ) R) (φ ρ) *
          rename some (ψ ρ))).det =
      rename some (genWronskian D ψ) * Polynomial.aeval (X none) (wronskian φ)
```

Cost of restatement: CHEAP — the `CommRing` form compiles with the existing proof once the parent defs are stated over `CommRing` (which their own reports already require); the index change follows the helper's restatement.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | no hypotheses | — |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | no | an identity of determinants | — |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field-specific to (semi)ring? | yes | `[Field K]` to `[CommRing R]` (verified) | applies over `ℤ` directly (evidence (2)), matching mathlib's `Polynomial.wronskian` over `CommRing` |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general? | partially | second block `Option`/one variable could become a general block (`Sum` form) | not verified; noted for the PR author only |
| 8 | Concrete-via-abstract? | yes (mild) | after unfolding, the proof is `det(ABᵀ) = det A det B` plus an entrywise identity; it never uses the field structure | the abstract content is `Matrix.det_mul`/`det_transpose`, already in mathlib; the remaining content is the entrywise Hasse identity (the helper lemma) |
| 9 | False-generalisation guard | no | `CommRing` form specialises definitionally to the project statement (evidence, `rfl` bridges); no change of meaning | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the `[CommRing R]`, `optionElim`-index form above.
  - Cost: CHEAP
  - Mathlib downstream this enables: coherent with `Polynomial.wronskian` (`Mathlib/RingTheory/Polynomial/Wronskian.lean`, `CommRing`), with the CommRing `genWronskian`/n-ary `wronskian` proposed in their reports, and with the `optionEquivLeft_coeff_coeff` index normal form.
  - Real mathematical improvement: the factorisation is ring-theoretic, so over `ℤ` it can be applied without the detour through `ℚ` that the only caller currently makes (`map (Int.castRingHom ℚ)` at Separation.lean:529).

### Proof strategy — `Roth.det_hasseDeriv_separated`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | multivariate `MvPolynomial.hasseDeriv`, n-ary Wronskian, generalized Wronskian and the factorwise lemma `hasseDeriv_rename_mul_aeval` (all project API to be upstreamed first) | CHEAP once those land |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
  - The proof is the textbook `det(ABᵀ) = det A · det Bᵀ` (`Matrix.det_mul`, `Matrix.det_transpose`, `AlgHom.map_det`) plus an entrywise rewrite; nothing to refactor beyond the index spelling inherited from the helper.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.det_hasseDeriv_separated`

[A] Lean-Finder       "determinant of matrix with entries sum over rho of a(mu,rho) b(nu,rho) equals det A times det B"   hits only building blocks: `Matrix.det_mul`, `Matrix.det_kronecker`, `Matrix.det_kroneckerMapBilinear`, `Matrix.det_kroneckerTMul`
[B] Loogle            `Matrix.det, Polynomial.wronskian`   no results
[C] LeanSearch        "Wronskian of a product of polynomials in disjoint variables factors as product of Wronskians"   no hit: only the 2-ary `Polynomial.wronskian` API (`wronskian_add_left/right`, `natDegree_wronskian_lt_add`)
[D] Grep mathlib src  `wronskian` (files: RingTheory/Polynomial/Wronskian.lean, RingTheory/Polynomial/Radical.lean, NumberTheory/FLT/MasonStothers.lean — all 2-ary), `genWronskian`, `det_hasseDeriv`, `hasseDeriv` in MvPolynomial   no hits beyond the 2-ary Wronskian
[E] Name pattern      `det_hasseDeriv_separated`, `genWronskian`   project-only

Searched for both:
  - the user's current form (Option / one-variable block): not in mathlib.
  - the literature-standard form (CommRing / two-block separated-sum Wronskian factorisation): not in mathlib (no multivariate Hasse derivative, no n-ary or generalized Wronskian).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); building blocks `Matrix.det_mul`, `Matrix.det_transpose`, `AlgHom.map_det`.

### Normal-form check — `Roth.det_hasseDeriv_separated`

Equivalent formalisms: (a) index `(D μ).mapDomain some + single none ν` (project); (b) `(D μ).optionElim ν` (mathlib normal form for `Option` indices); (c) two-block `Sum` form with `Finsupp.sumElim`.
Does mathlib already have a canonical form? yes for the index (`optionElim`, cf. `optionEquivLeft_coeff_coeff`).
Is our statement stated against the canonical form? NO → REFACTOR to (b), together with the helper `hasseDeriv_rename_mul_aeval`.
RHS convention respected? yes (factored product on the RHS).

### Syntactic generality — `Roth.det_hasseDeriv_separated`

Alternative restatements attempted:
- `[CommRing R]` form (evidence (1)): compiles.
- `optionElim` index: inherited from the helper's verified restatement; not separately compiled.
- `det A * det B` form with explicit matrices instead of `genWronskian`/`wronskian`: would hide the named objects; rejected.

Chosen restatement: `[CommRing R]` with `optionElim` index, RHS in terms of `genWronskian` and `wronskian`.
Justification: the caller builds the matrix index itself and immediately compares with the named Wronskians, so the named-object RHS is easiest to rewrite with.

### Superfluous-argument audit — `Roth.det_hasseDeriv_separated`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | only `CommRing` structure used (evidence (1)); kept locally because parent defs require it |
| 2 | section `[Fintype τ] [DecidableEq τ]` | no | already omitted |
| 3 | `D`, `φ`, `ψ`, `l` | yes | data of the statement |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (index `(D μ).optionElim ν`)
Syntactic generality: OK
Superfluous arguments: 1 to drop (`[Field K]` to `[CommRing R]`, conditional on the parent defs)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.det_hasseDeriv_separated`

Internal use count: 0 (outside the declaring file); 1 inside Roth/Separation.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:529 | `rw [hFdef, RingHom.map_det, ← det_hasseDeriv_separated D φ ψ, ← hPQ]` in private `exists_rat_factors_det_hasseDeriv_aux` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.det_hasseDeriv_separated`?):
  - (none) — `grep -rn "det_mul\|det_transpose" Roth/` shows no other `det(ABᵀ)` Wronskian factorisation.

K = 1 leans toward inlining, but the statement is exactly the source's displayed identity and the natural product formula for generalized Wronskians; the single use reflects the project's one consumer (Lemma 2).

### Composition check (Phase 6)

Can `Roth.det_hasseDeriv_separated` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Matrix.det_mul` + `Matrix.det_transpose` + `AlgHom.map_det`
  - Mathlib decls used: `Matrix.det_mul`, `Matrix.det_transpose`, `AlgHom.map_det`
  - Result: partial — reduces to the matrix identity `M = A Bᵀ`, which needs an entrywise `Matrix.ext`/`Finset.sum_congr` argument and the (non-mathlib) Hasse identity `hasseDeriv_rename_mul_aeval`.

Attempt 2: from the to-be-upstreamed project API
  - Decls used: the above plus `hasseDeriv_rename_mul_aeval`, `map_sum`, `Matrix.mul_apply`
  - Result: an 11-line proof, not a composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.det_hasseDeriv_separated`

Verdict: YES-but-generalise-first

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard step of Roth 1955 / Bombieri–Gubler D.6.1; stated verbatim in the source (clean.tex:408–417, "The matrix defining F is A Bᵀ, so F = det A det B").
- Generality analysis (Phase 4): STRICTLY NARROWER (coefficients); `[CommRing R]` version verified to compile (evidence (1)).
- Mathlib search (Phase 5): not in mathlib in either form; mathlib has only the 2-ary `Polynomial.wronskian` and no multivariate Hasse derivative.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**
The gap is the generalized Wronskian API itself: `Mathlib/RingTheory/Polynomial/Wronskian.lean` has only the 2-ary Wronskian (its n-ary version is listed as a TODO there, per the `Roth.wronskian` report), and there is no `MvPolynomial.hasseDeriv`. Once `genWronskian` and the n-ary `wronskian` are upstreamed (both assessed YES-but-generalise-first), this factorisation — the generalized Wronskian of a sum of separated products is the product of the two Wronskians — is the expected companion lemma: it is how the multivariate Wronskian criterion is proved by induction on the number of variables (Bombieri–Gubler D.6.1) and how Roth's Lemma 2 is obtained. Its proof is the idiomatic `det(ABᵀ)` argument over mathlib's `Matrix.det_mul`/`det_transpose`, with the only non-mathlib content in the entrywise helper.

It should not ship as stated: the field hypothesis is spurious (evidence (1) compiles the same proof over `[CommRing R]`, which also lets the caller apply it over `ℤ` directly), and the matrix index should use the `optionElim` normal form, as already decided for the helper `hasseDeriv_rename_mul_aeval`. A two-block `Sum` form with arbitrary operators on both blocks is the most general literature statement; it was not compiled here, so it is offered only as an option for the PR author, not as a verified target.

Reason for the generalisation: both apply.
- LITERATURE-WEAKENING: `[Field K]` to `[CommRing R]` (verified).
- MODERN-IDIOM: index normalised to `(D μ).optionElim ν`, matching `optionEquivLeft_coeff_coeff` and the helper's restatement.

Proposed restatement:
```lean
theorem MvPolynomial.det_hasseDeriv_sum_aeval_mul_rename {τ R : Type*} [CommRing R] {l : ℕ}
    (D : Fin l → (τ →₀ ℕ)) (φ : Fin l → Polynomial R) (ψ : Fin l → MvPolynomial τ R) :
    (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).optionElim ν)
        (∑ ρ, Polynomial.aeval (X none : MvPolynomial (Option τ) R) (φ ρ) *
          rename some (ψ ρ))).det =
      rename some (genWronskian D ψ) * Polynomial.aeval (X none) (wronskian φ) := by
  sorry  -- current proof survives after the index change in the helper
```
Estimated cost of regeneralisation: CHEAP
Mathlib downstream this enables:
- product formula for the planned generalized Wronskian API; gives the induction step of the multivariate Wronskian criterion
- usable over `ℤ` (removes the `ℚ` detour at the caller for this step), consistent with `Polynomial.wronskian` over `CommRing`
- same index normal form as `optionEquivLeft_coeff_coeff` and the helper `hasseDeriv_rename_some_mul_aeval_X_none`

Proposed mathlib location: the planned `Mathlib/RingTheory/MvPolynomial/Wronskian.lean` (with `genWronskian`), after `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean` and the n-ary Wronskian.
Proposed PR title: "feat(RingTheory/MvPolynomial/Wronskian): generalized Wronskian of a separated sum"
PR grouping: ship with `Roth.genWronskian`, `Roth.genWronskian_eq_zero_of_not_linearIndependent`, and after the PRs for `MvPolynomial.hasseDeriv` (incl. `hasseDeriv_rename_mul_aeval`) and `Roth.wronskian`/`Roth.wronskianMatrix`.
Local refactor: when the helper moves to the `optionElim` index, change the matrix index here (Separation.lean:353) and in the caller `exists_rat_factors_det_hasseDeriv_aux` (Separation.lean:507, 524–529).
Next action: run `/generalise Roth.det_hasseDeriv_separated` with the `CommRing` / `optionElim` targets once the parent defs are generalised, then `/cleanup` and fold into the generalized-Wronskian PR.

---

## Next step

Restate over `[CommRing R]` with index `(D μ).optionElim ν` (after `genWronskian`, `wronskian` and `hasseDeriv_rename_mul_aeval` are restated), update the single caller at Roth/Separation.lean:529, and upstream with the generalized Wronskian API.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.det_hasseDeriv_separated/weaken.lean` (imports `Roth.Separation`), compiled with `lake env lean`: no errors or warnings, only the `#check` output. (0) `#check @Roth.det_hasseDeriv_separated` shows `[Field K]` and no `Fintype`/`DecidableEq`. (1) With local `[CommRing R]` copies of `genWronskian`, `wronskianMatrix`, `wronskian`, the project proof compiles verbatim over `[CommRing R]`; `rfl` bridges show the project defs are the field specialisation. (2) The CommRing lemma elaborates over `ℤ`.
- Searches: 3 WebSearch queries (recorded above); Lean-Finder ×1, LeanSearch ×1, Loogle ×1 (no results); mathlib grep for `wronskian` (3 files, all 2-ary), `genWronskian`, `det_hasseDeriv` (none); local reference grep of clean.tex (lines 180, 408–417). ChatGPT MCP n/a (not configured in this session).
