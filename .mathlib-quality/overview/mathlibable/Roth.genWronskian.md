---
decl: Roth.genWronskian
file: Roth/GenWronskian.lean
line: 32
kind: def
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The generalized (Ostrowski-Roth) Wronskian det (Delta_{D mu} phi_nu) of multivariate polynomials is a standard named object (Roth 1955 Lemma 1, Schmidt LNM 785, Bostan-Dumas, Ball-Parks-Pong) absent from mathlib, which has only the 2-ary Polynomial.wronskian; [Field K] weakens to [CommRing R] with an rfl-equal body (verified), and it must ship after MvPolynomial.hasseDeriv.
action: Upstream as MvPolynomial.genWronskian (placeholder name) over [CommRing R] in a new Mathlib/RingTheory/MvPolynomial/Wronskian.lean, after MvPolynomial.hasseDeriv and the n-ary Polynomial Wronskian, with the verified map and univariate bridge lemmas plus genWronskian_eq_zero_of_not_linearIndependent; locally keep (call sites Roth/GenWronskian.lean:42/242/244/256, Roth/Separation.lean:355/357/524/527).
---

# Roth.genWronskian

## Inventory entry

### `def Roth.genWronskian`
- **Type**: `{K : Type*} → [Field K] → {σ : Type*} → {l : ℕ} → (D : Fin l → σ →₀ ℕ) → (φ : Fin l → MvPolynomial σ K) → MvPolynomial σ K`
- **What**: The generalized Wronskian of `l` multivariate polynomials `φ_0, …, φ_{l-1}` with respect to `l` Hasse operators `Δ_{D 0}, …, Δ_{D (l-1)}`: the determinant `det (Δ_{D μ} φ_ν)_{μ, ν}`.
- **How**: One-line definition `(Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)).det`, i.e. mathlib's `Matrix.det` applied to the matrix of the project's `MvPolynomial.hasseDeriv`.
- **Hypotheses**: `[Field K]` (section variable). The section's `[Fintype σ]` is not included (hover confirms). No order constraint `|D μ| ≤ μ` is imposed; that constraint lives in `exists_genWronskian_ne_zero`.
- **Uses from project**: `MvPolynomial.hasseDeriv`
- **Used by**: Roth/GenWronskian.lean: `genWronskian_eq_zero_of_not_linearIndependent` (l.42), `wronskian_kronecker_eq_sum_aux` (private, l.242 statement, l.244 unfolds it), `exists_genWronskian_ne_zero` (l.256); Roth/Separation.lean: `det_hasseDeriv_separated` (l.355 statement, l.357 unfolds it), `exists_rat_factors_det_hasseDeriv_aux` (private, l.524 uses `exists_genWronskian_ne_zero`, l.527 states `hFmap`); also mentioned in the Separation.lean module docstring (l.34)
- **Visibility**: public
- **Lines**: 30–34, proof length 1 line (definition body)
- **Notes**: Hasse normalisation: it differs from the ordinary-derivative generalized Wronskian by the constant `∏_μ (D μ)!`, following the source. The literature allows arbitrary constant-coefficient operators `Δ_μ` of order `≤ μ`. Here each `Δ_μ` is a single monomial Hasse operator, but by multilinearity of `det` every general generalized Wronskian is a linear combination of these, and the Kronecker proof (`wronskian_kronecker_eq_sum_aux`) uses exactly that expansion.

## Junk check (Step 8)
- Used anywhere? Yes. Three public and two private declarations in 2 files state or use it, including Lemma 1 (`exists_genWronskian_ne_zero`) and the separation identity `det_hasseDeriv_separated`.
- Wrapper of 1–2 mathlib calls? Syntactically it is one `Matrix.det` over a project def. It names the central object of §2 of the source, and statements are phrased about `genWronskian D φ`.
- Does mathlib have it? No. Grep finds `wronsk` only in 3 mathlib files, all about the 2-ary univariate `Polynomial.wronskian`, and mathlib has no multivariate Hasse derivative (`MvPolynomial.hasseDeriv` report: absent).
- Too specific (inline?)? No: inlining would replace every statement with a raw determinant and lose the named concept.
- Well-chosen definition? Yes. Unconstrained `D` keeps the def total and simple, and the order constraint sits in the theorem that needs it.
- Conclusion: `KEEP`. Action: keep as is locally. It is the upstream candidate described below.

## Mathlibable assessment (Step 9)

Pre-filter: not private, no `_aux` suffix, docstring not internal/auxiliary, Step 8 KEEP, and a namespace-aware grep of `.lake/packages/mathlib/Mathlib/` finds no `genWronskian` (or any multivariate Wronskian). Not a glue lemma. Full run follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; `lean_diagnostic_messages` on the evidence file importing `Roth.GenWronskian` is clean)
- decl `Roth.genWronskian`:  ✓ resolved at Roth/GenWronskian.lean:32
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  Generalized Wronskians `det (Δ_{D μ} φ_ν)` of multivariate polynomials, and Lemma 1: a linearly independent family has a nonvanishing generalized Wronskian (via Kronecker substitution).

### Statement (Phase 1)

`Roth.genWronskian` is a definition of the following. Given polynomials `φ_0, …, φ_{l-1} ∈ K[x_j : j ∈ σ]` and multi-indices `D_0, …, D_{l-1} ∈ ℕ^{(σ)}`, the generalized Wronskian is the polynomial `W(φ; Δ_{D_0}, …, Δ_{D_{l-1}}) = det (Δ_{D_μ} φ_ν)_{0 ≤ μ, ν < l}`, where `Δ_d = ∏_j (1/d_j!) ∂_j^{d_j}` is the multivariate Hasse derivative. When `|D_μ| ≤ μ` for all `μ`, this is a generalized Wronskian in the sense of Ostrowski and Roth.

Variables / typeclasses involved (Lean side):
- `K : Type*`, `[Field K]`: coefficient ring.
- `σ : Type*`: variable index (any type; no finiteness needed for the def).
- `l : ℕ`: number of polynomials.
- `D : Fin l → σ →₀ ℕ`: the orders of the Hasse operators (row index).
- `φ : Fin l → MvPolynomial σ K`: the family (column index).

Hypotheses (Lean side):
- none.

Conclusion (math): the polynomial `det (Δ_{D μ} φ_ν)`.

Conclusion (Lean): n/a — definition (value in `MvPolynomial σ K`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a named classical tool (generalized Wronskian) used inside Roth's lemma. It is a polynomial-valued function, not a new structure and not a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | yes (weak) | Unfolded only deliberately: `rw [genWronskian, wronskian, AlgHom.map_det, …]` in Separation.lean l.357 and `simpa [… genWronskian, AlgHom.map_det, Matrix.map]` in GenWronskian.lean l.244. Keeping it sealed keeps statements such as `exists_genWronskian_ne_zero` from being simp-rewritten into raw determinants |
| Avoid typeclass diamonds         | no       | no instances involved |
| Mark semantic intent / API name  | yes      | `genWronskian_eq_zero_of_not_linearIndependent`, `exists_genWronskian_ne_zero` (Lemma 1 of the source, Roth 1955 Lemma 1) and `det_hasseDeriv_separated` are stated about `genWronskian D φ`. "Generalized Wronskian" is the classical named object |

Conclusion: ONE-LINER WITH-EXEMPTION

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | generalized Wronskian multivariate polynomials linear independence determinant partial derivatives order at most i | yes | `det (D_i f_j)` where `D_i` is a constant-coefficient partial differential operator of order `≤ i` (or `= i`); in monomial form `W_{μ_1..μ_n} = det (∂^{μ_i} φ_j)` with `\|μ_i\| ≤ i-1`; polynomials are linearly independent iff some such `W` is nonzero (char 0) | arXiv 2502.00731 Lemma 2.25 (proof by Kronecker substitution `t, t^d, …`, same as the project); Wikipedia "Wronskian"; arXiv 1301.6598 (char-p caveat `1, x^p`) |
| 2 | WebSearch (general form) | "generalized Wronskians" Ostrowski functions of several variables linearly independent Bostan Dumas | yes | same definition for analytic functions and for formal power series over any char-0 field; the easy direction (dependent implies all vanish) holds for any functions | Bostan–Dumas arXiv 1301.6598; Ball–Parks–Pong arXiv 1611.00248; Walker (Penn State) on minimal subcollections |
| 3 | WebSearch (named-after / aliases) | generalized Wronskian Roth's lemma Schmidt Diophantine approximation differential operators Hasse | yes | Ostrowski's generalized Wronskian; Roth 1955 Lemma 1 (and Siegel before him); Schmidt LNM 785 | Roth, Mathematika 2 (1955); Evertse subspace notes. Sources use ordinary derivatives; the Hasse normalisation is the project source's char-free choice |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "generalized Wronskian" | yes | §2 l.206–210: `W(φ_0..φ_{l-1}; Δ_0..Δ_{l-1}) = det (Δ_μ φ_ν)`, with `Δ_i` a differential operator of order `≤ i`; Lemma l.213 (dependent implies zero) and Lemma 1 l.225 | exact source of the def |
| 6 | nLab | nLab OR mathoverflow "generalized Wronskian" linear dependence several variables | no | — | no nLab page; classical analytic/algebraic tool not covered by nLab |
| 7 | nCatLab | — | n/a | — | not a categorical concept (nLab query #6 found nothing either) |
| 8 | Stacks Project | — | n/a | — | not scheme-theoretic. Generalized Wronskians of sections appear in projective-geometry papers (arXiv 2108.02993), not in Stacks |
| 9 | MathOverflow / Math.SE | same query as #6 | no | no MO/MSE thread surfaced | the encyclopediaofmath "Wronskian" page surfaced; covers the classical 1-variable case |
| 10 | recent arXiv (last 5 years) | results of #1–#3, #6 | yes | arXiv 2502.00731 (2025, Roth/subspace exposition, Lemma 2.25), 2108.02993 (2021, "geometric" generalized Wronskians on projective varieties), 2511.03848 (Wronskians over multidimensions) | same definition throughout |

### Literature summary (Phase 3)

Concept identified as: the generalized Wronskian (Ostrowski; Roth's lemma) of a finite family of multivariate polynomials, power series or analytic functions.
Sources agree on the standard form: mostly. All use `det (Δ_i f_j)` with constant-coefficient operators of order bounded by `i`. Variants: some require order `≤ i`, some exactly `i`, and some restrict to monomial operators `∂^{μ_i}` (2502.00731). Classical sources use ordinary derivatives; the project source uses Hasse derivatives.
Most general standard form: for `f_1..f_n` in a commutative ring `A` with commuting derivations (or a Hasse–Schmidt structure), `det (Δ_i f_j)` for operators `Δ_i` in the algebra of differential operators. For polynomials, any commutative coefficient ring.
Generality dimensions where the literature varies:
  - operators: monomial `∂^{μ}` up to arbitrary constant-coefficient operators. Arbitrary operators reduce to monomial ones by multilinearity of `det`.
  - derivative normalisation: ordinary (char 0) or Hasse (any characteristic). Hasse is the char-free choice.
  - coefficient ring: ℝ/ℂ analytic functions, char-0 fields, up to any commutative ring (only `det` needs commutativity).
  - order constraint: part of the definition in some sources, part of the theorem in others.
Disagreement with the literature: none of substance. The order constraint is moved to the theorem, which is more general.

### Generality analysis — `Roth.genWronskian`

Literature-standard form (from Phase 3): `det (Δ_{D μ} φ_ν)` for `φ : Fin l → MvPolynomial σ R`, `R` a commutative ring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | commutative ring | yes | `Matrix.det` needs `[CommRing R]` and `MvPolynomial.hasseDeriv` only `[CommSemiring R]`. Verified: `Evidence.genWronskian` over `[CommRing R]` compiles, `Roth.genWronskian D φ = Evidence.genWronskian D φ` holds by `rfl`, and it elaborates at `MvPolynomial ℕ ℤ` |
| 2 | `[CommRing R]` to `[CommSemiring R]` | — | — | no (in mathlib) | `Matrix.det` exists only over `CommRing` (signs) |
| 3 | `σ` finiteness | none required | any variable set | already maximal | `[Fintype σ]` is not part of the def (hover) |
| 4 | operators | monomial Hasse `Δ_{D μ}` | arbitrary constant-coefficient operators of order `≤ μ` | not recommended | General operators expand by multilinearity into monomial ones (the project does this in `wronskian_kronecker_eq_sum_aux`). Mathlib has no bundled algebra of constant-coefficient differential operators on `MvPolynomial` to quantify over |
| 5 | order constraint `\|D μ\| ≤ μ` | absent | sometimes in the def | already more general | putting it in Lemma 1 keeps the def total |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (`[Field K]` to `[CommRing R]`, verified clean via `lean_diagnostic_messages` on the evidence file)
Proposed restatement:

```lean
namespace MvPolynomial
variable {R σ : Type*} [CommRing R]
/-- The generalized Wronskian `det (hasseDeriv (D μ) (φ ν))_{μ, ν}`. -/
noncomputable def genWronskian {l : ℕ} (D : Fin l → σ →₀ ℕ) (φ : Fin l → MvPolynomial σ R) :
    MvPolynomial σ R :=
  (Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)).det
end MvPolynomial
```

Cost of restatement: CHEAP — mechanical; the body is unchanged.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic, finite |
| 3 | construction vs universal property? | no | — | a concrete polynomial |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to (semi)ring? | yes | `[CommRing R]` (Phase 4a row 1) | base change `map_genWronskian` (verified in evidence via `RingHom.map_det` + `MvPolynomial.hasseDeriv_map`); integral generalized Wronskians over `ℤ` (Separation.lean currently passes through `Int.castRingHom ℚ` exactly for this) |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | `Fin l` rows and columns are needed for the square matrix and the order bound `\|D μ\| ≤ μ` | — |
| 8 | concrete-via-abstract? | partial | the body only uses that `hasseDeriv (D μ)` is an operator, so `det (L μ (φ ν))` for any family of linear maps `L` would work | not recommended: that generality is just `Matrix.det ∘ Matrix.of` and loses the named concept; no mathlib API about families of operators would compose with it |
| 9 | false-generalisation guard | no false generalisation | The `CommRing` version is `rfl`-equal to the project def. With one variable and `D μ = μ • e` it is exactly the Hasse Wronskian `Roth.wronskian` (evidence `genWronskian_unique`). At `l = 0` it is `1` and at `l = 1` it is `Δ_{D 0} φ_0` (evidence). Same object | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.genWronskian {R σ} [CommRing R] {l} (D : Fin l → σ →₀ ℕ) (φ : Fin l → MvPolynomial σ R)`, placed next to `MvPolynomial.hasseDeriv`.
  - Cost: CHEAP
  - Mathlib downstream this enables: base change along ring homs (`RingHom.map_det`, `MvPolynomial.map`), compatibility with `rename` (via `MvPolynomial.hasseDeriv_rename`, used in Separation.lean), and the univariate specialisation to the n-ary Hasse Wronskian (the mathlib TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean`) through `MvPolynomial.uniqueAlgEquiv_hasseDeriv`.
  - Real mathematical improvement: the determinant uses only commutativity of the coefficients, and the general form makes integral generalized Wronskians first-class instead of going through `ℚ`.

### Proof strategy — `Roth.genWronskian`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | (a) `MvPolynomial.hasseDeriv` itself (prerequisite, parent report YES-but-generalise-first); (b) the n-ary univariate Hasse Wronskian (`Roth.wronskian`, YES-but-generalise-first) for the bridge lemma; (c) `map_genWronskian`, `genWronskian_unique` (both verified in evidence) | ship (a), (b) first |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (definition via `Matrix.det` of `Matrix.of`; no proof).
  - Missing mathlib API: the prerequisites in row 5.

### Diamond / defeq risk — `Roth.genWronskian`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | defines a polynomial value; introduces no instances; uses only `CommRing` for `Matrix.det` and `Fin l`'s `DecidableEq`/`Fintype` |
| 2 | Reducibility leak | none | plain semireducible `noncomputable def`; `rfl`-equal to the weakened version; unfolded only via explicit `rw`/`simp [genWronskian]` (2 sites) |
| 3 | Non-canonical unfolding | low | `simp [genWronskian]` exposes `Matrix.det (Matrix.of …)`. For `Fin 0`/`Fin 1` simp computes it cleanly (evidence), so bridge simp lemmas are easy |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `Type*` for `R` and `σ`; elaborates at `ℤ`/`ℕ` and generic types in evidence |
| 6 | Coercion ambiguity | none | no coercions. The name `genWronskian` does not clash in mathlib; an `MvPolynomial.wronskian` name would be free too, but it would be confused with the univariate 2-ary `Polynomial.wronskian` |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none
Recommended mitigations: n/a

### Mathlib search-status: `Roth.genWronskian`

[A] Lean-Finder       "generalized Wronskian of multivariate polynomials: determinant of matrix of partial derivatives of a family of functions"   only the 2-ary `Polynomial.wronskian`, `wronskianBilin(_apply)`, `isAlt_wronskianBilin`, and the unrelated `Polynomial.sylvesterDeriv`
[B] Loogle            `Matrix.det, MvPolynomial.pderiv`   no hits
[C] LeanSearch        "determinant of matrix of partial derivatives of n multivariate polynomials vanishes if linearly dependent"   only building blocks `Matrix.det_eq_zero_of_not_linearIndependent_cols/_rows`, `Matrix.det`; nothing multivariate-Wronskian
[D] Grep mathlib src  case-insensitive `wronsk` over `.lake/packages/mathlib/Mathlib`: 3 files (RingTheory/Polynomial/Wronskian.lean, RingTheory/Polynomial/Radical.lean, NumberTheory/FLT/MasonStothers.lean), all 2-ary univariate; `genWronskian`/`hasseDeriv` under Algebra/MvPolynomial and RingTheory/MvPolynomial: no hits   no multivariate hit
[E] Name pattern      `lean_local_search "genWronskian"` unavailable (ripgrep not installed); replaced by the grep in [D] for `genWronskian`, `generalizedWronskian`   absent

Searched for both the user's form (Hasse-operator determinant over a field) and the literature-standard form (generalized Wronskian with partial derivatives over a commutative ring).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). The nearest relative is the 2-ary univariate `Polynomial.wronskian` (`Mathlib/RingTheory/Polynomial/Wronskian.lean:43`), and mathlib has no multivariate Hasse derivative at all.

### Normal-form check — `Roth.genWronskian`

Equivalent formalisms: `det (hasseDeriv (D μ) (φ ν))`; `det` of the transpose; ordinary-derivative form `det (∏_j pderiv j ^ (D μ j) (φ ν))` (= `∏_μ (D μ)!` times ours); general operators `det (Δ_μ φ_ν)` (a linear combination of ours).
Does mathlib already have a canonical form? no.
Proposed canonical form: the Hasse determinant (char-free), with bridges `uniqueAlgEquiv (genWronskian (single default ∘ val) φ) = <n-ary Wronskian> (uniqueAlgEquiv ∘ φ)` (univariate form on the RHS) and `map f (genWronskian D φ) = genWronskian D (map f ∘ φ)` (map pushed inside, the simp-normal direction as for `RingHom.map_det`).
RHS convention respected? yes

### Syntactic generality — `Roth.genWronskian`

Alternative restatements attempted:
- `[CommRing R]`, `φ : Fin l → MvPolynomial σ R`, unconstrained `D` (compiles, evidence)
- `D : Fin l → σ →₀ ℕ` bundled with the order constraint as a subtype (rejected: forces proofs at every use; the dependent-vanishing lemma does not need it)
- abstract operator family `L : Fin l → MvPolynomial σ R →ₗ[R] MvPolynomial σ R` (rejected, Phase 4c row 8)
Chosen restatement: `[CommRing R]`, unconstrained `D`, defined directly as `det (Matrix.of …)`.
Justification: call sites pass the Kronecker-substitution row choices `f : Fin l → σ →₀ ℕ` from `Fintype.piFinset` directly, and the order bound is needed only in Lemma 1.

### Superfluous-argument audit — `Roth.genWronskian`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `[CommRing R]` suffices (verified) |
| 2 | `D` | yes | operator orders |
| 3 | `φ` | yes | the family |
| 4 | `l` | yes | matrix size |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (`[CommRing R]`, `MvPolynomial` namespace)
Superfluous arguments: 1 to drop (`[Field K]` weakened to `[CommRing R]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.genWronskian`

Internal use count: 4 lines outside the declaring file (2 declarations, 1 private); 4 lines inside Roth/GenWronskian.lean (3 declarations, 1 private)
External-to-file callers: 1 distinct file (Roth/Separation.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/GenWronskian.lean:42 | `{φ : Fin l → MvPolynomial σ K} (h : ¬ LinearIndependent K φ) : genWronskian D φ = 0 := by` |
| Roth/GenWronskian.lean:242 | `∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * kronecker k (genWronskian f φ) := by` (private `wronskian_kronecker_eq_sum_aux`) |
| Roth/GenWronskian.lean:244 | `simpa [wronskian, wronskianMatrix, hc, genWronskian, AlgHom.map_det, Matrix.map] using` |
| Roth/GenWronskian.lean:256 | `∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0 := by` (`exists_genWronskian_ne_zero`) |
| Roth/Separation.lean:355 | `rename some (ψ ρ))).det = rename some (genWronskian D ψ) *` (`det_hasseDeriv_separated`) |
| Roth/Separation.lean:357 | `rw [genWronskian, wronskian, AlgHom.map_det, AlgHom.map_det,` |
| Roth/Separation.lean:524 | `obtain ⟨D, hD, hG⟩ := exists_genWronskian_ne_zero hψ` (private `exists_rat_factors_det_hasseDeriv_aux`) |
| Roth/Separation.lean:527 | `have hFmap : map (Int.castRingHom ℚ) F = rename some (genWronskian D ψ) *` |

Inline-derivation grep: Separation.lean l.352 and l.525 build `(Matrix.of fun μ ν ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none ν) P).det`. That is a determinant whose rows vary the operator and whose columns are not a family `φ ν`, so it is not literally `genWronskian`. With `P` replaced by the separated sum it is identified with `rename (genWronskian D ψ) * aeval (wronskian φ)` by `det_hasseDeriv_separated`. No literal re-derivation of `genWronskian`.

### Composition check (Phase 6)

Can `Roth.genWronskian` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(Matrix.of fun μ ν ↦ MvPolynomial.hasseDeriv (D μ) (φ ν)).det`, the body inlined.
  - Mathlib decls used: `Matrix.det`, `Matrix.of`; `MvPolynomial.hasseDeriv` is NOT in mathlib.
  - Result: fails as a mathlib-only composition (no multivariate Hasse derivative). Even after `hasseDeriv` is upstreamed it is a trivial term, but it names a classical concept carrying Lemma 1.
  - Notes: if `hasseDeriv` were upstreamed, this would count as "trivial composition; user decides if worth a definition". The API-name exemption (Phase 2b) applies.

Attempt 2: ordinary partials `(Matrix.of fun μ ν ↦ (D μ).prod (fun j n ↦ (pderiv j)^[n]) (φ ν)).det` from mathlib's `MvPolynomial.pderiv`.
  - Mathlib decls used: `MvPolynomial.pderiv`, `Finsupp.prod`, `Matrix.det`
  - Result: partial. It gives a different object (scaled by `∏ (D μ)!`), which is useless in positive characteristic and not the source's normalisation.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.genWronskian`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the generalized Wronskian is a classical named object (Ostrowski; Siegel; Roth 1955 Lemma 1; Schmidt LNM 785; Bostan–Dumas arXiv 1301.6598; Ball–Parks–Pong arXiv 1611.00248; arXiv 2502.00731 Lemma 2.25; project source §2).
- Generality analysis (Phase 4): STRICTLY NARROWER. `[Field K]` is superfluous, and `[CommRing R]` is verified in the evidence file (`rfl`-equal body).
- Mathlib search (Phase 5): not in mathlib. Mathlib has only the 2-ary univariate `Polynomial.wronskian` and no multivariate Hasse derivative.
- Composition check (Phase 6): NOT-COMPOSABLE (prerequisite `MvPolynomial.hasseDeriv` missing; otherwise a trivial body that names a concept).

**Rationale:**

Mathlib's Wronskian coverage stops at `Polynomial.wronskian a b` (two univariate polynomials), with an explicit TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean` for the n-tuple case. The multivariate generalized Wronskian is the next standard step. It is the linear-independence test for several-variable polynomials and power series (Roth's Lemma 1, Bostan–Dumas), and it is the tool any formalisation of Roth's theorem, Schmidt's subspace theorem, or Wronskian-based identity tests needs. `Roth.genWronskian` is that object in the char-free Hasse normalisation. The evidence shows it fits the planned upstream pieces. It commutes with base change (`map_genWronskian`, via `RingHom.map_det` and `MvPolynomial.hasseDeriv_map`). In one variable with `D μ = μ • e`, it is exactly the n-ary Hasse Wronskian `Roth.wronskian` (`genWronskian_unique`, via `uniqueAlgEquiv_hasseDeriv`), which is that report's upstream target. The degenerate sizes come out correctly. The def is a one-liner, but the API-name exemption applies: Lemma 1 (`exists_genWronskian_ne_zero`), the dependent-vanishing lemma and the separation identity are all stated about the named object. Phase 4.5 risk is LOW.

The defect is generality: `[Field K]` is unused. `Matrix.det` needs only `[CommRing R]`, and the restated def is `rfl`-equal to the project def (Phase 5.5 RESTATE-BEFORE-SHIP: weaken to `[CommRing R]` and move to the `MvPolynomial` namespace). The upstream also depends on `MvPolynomial.hasseDeriv` landing first (parent report YES-but-generalise-first). This is a sequencing constraint, not a cost argument.

Reason for the generalisation: LITERATURE-WEAKENING (field to commutative ring) plus MODERN-IDIOM (`MvPolynomial` namespace beside `MvPolynomial.hasseDeriv`, with the univariate n-ary Wronskian as a verified specialisation).
Proposed restatement:
```lean
namespace MvPolynomial
variable {R σ : Type*} [CommRing R]
/-- The generalized Wronskian `det (hasseDeriv (D μ) (φ ν))_{μ, ν}`. -/
noncomputable def genWronskian {l : ℕ} (D : Fin l → σ →₀ ℕ) (φ : Fin l → MvPolynomial σ R) :
    MvPolynomial σ R :=
  (Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)).det
theorem map_genWronskian {S : Type*} [CommRing S] (f : R →+* S) {l : ℕ} (D : Fin l → σ →₀ ℕ)
    (φ : Fin l → MvPolynomial σ R) :
    map f (genWronskian D φ) = genWronskian D fun ν ↦ map f (φ ν) := by
  sorry -- proved in evidence: RingHom.map_det + hasseDeriv_map
end MvPolynomial
```
Estimated cost of regeneralisation: CHEAP (body unchanged; field-dependent lemmas keep their own hypotheses).
Mathlib downstream this enables:
- the multivariate linear-independence criterion (dependent implies all generalized Wronskians vanish, over domains; Roth's Lemma 1 in char 0), extending the n-ary univariate TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean`;
- base change and `rename` compatibility (`RingHom.map_det`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_rename`); integral generalized Wronskians over `ℤ` without passing through `ℚ`;
- the univariate n-ary Hasse Wronskian as the one-variable special case (`genWronskian_unique`).
PR grouping: after (1) `MvPolynomial.hasseDeriv` and its API and (2) the n-ary `Polynomial` Hasse Wronskian (`Roth.wronskianMatrix`/`Roth.wronskian`), ship one PR with `genWronskian`, `map_genWronskian`, the univariate bridge, and `genWronskian_eq_zero_of_not_linearIndependent`. Ship Lemma 1 (`exists_genWronskian_ne_zero`, with the Kronecker substitution helpers) as a follow-up.
Next action: run `/generalise Roth.genWronskian` (target `[CommRing R]`), then upstream it to a new `Mathlib/RingTheory/MvPolynomial/Wronskian.lean` once the prerequisites land; PR title "feat(RingTheory/MvPolynomial/Wronskian): generalized Wronskians".

---

## Next step

Run `/generalise Roth.genWronskian`. After `MvPolynomial.hasseDeriv` and the n-ary Hasse Wronskian are upstreamed, upstream it as `MvPolynomial.genWronskian` over `[CommRing R]`, with `map_genWronskian` and the univariate bridge.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.genWronskian/weaken_and_relate.lean` (imports only `Roth.GenWronskian`), checked with `lean_diagnostic_messages`: clean, no errors or warnings. The first check failed in `genWronskian_unique`, because `ext` descended into polynomial coefficients. That proof now uses `congrArg Matrix.det (Matrix.ext …)` with `uniqueAlgEquiv_hasseDeriv`. The file verifies: (1) the `[CommRing R]` def with no `Fintype σ`, `Roth.genWronskian D φ = Evidence.genWronskian D φ` by `rfl`, and elaboration over `MvPolynomial ℕ ℤ`; (2) `map_genWronskian`; (3) `genWronskian_unique`: the one-variable specialisation equals `Roth.wronskian` after `uniqueAlgEquiv`; (4) the `l = 0` value is `1` and the `l = 1` value is `hasseDeriv (D 0) (φ 0)`.
- `lean_hover_info` on the def: `[Fintype σ]` not included.
- Mathlib grep: case-insensitive `wronsk` (3 files, all 2-ary univariate); no `genWronskian`/`hasseDeriv` under `Algebra/MvPolynomial` or `RingTheory/MvPolynomial`.
- Lean-Finder and LeanSearch returned only the 2-ary family and the det building blocks. Loogle `Matrix.det, MvPolynomial.pderiv` returned no hits. `lean_local_search` was unavailable (ripgrep missing), so grep replaced it.
- WebSearch: 4 queries, summarised in the literature table. ChatGPT MCP: n/a (not configured).
- Project grep `grep -n genWronskian Roth/*.lean` produced the call-sites table.
- Parent reports consulted: `Roth.wronskian.md`, `Roth.wronskianMatrix.md`, `MvPolynomial.hasseDeriv.md`, `MvPolynomial.hasseDeriv_map.md`, `Roth.wronskian_eq_zero_of_not_linearIndependent.md`.
