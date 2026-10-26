---
decl: Roth.wronskianMatrix
file: Roth/Wronskian.lean
line: 56
kind: def
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The l x l Hasse-derivative Wronskian matrix is standard (Hasse/Schmidt Wronskian, Garcia-Voloch) and fills mathlib's explicit TODO in RingTheory/Polynomial/Wronskian.lean (only the 2-polynomial Polynomial.wronskian exists, and its det equals ours for l = 2, verified); the def should be stated over an arbitrary semiring in the Polynomial namespace, not over a field.
action: Upstream with Roth.wronskian as Polynomial.wronskianMatrix over [Semiring R] (verified in evidence) in Mathlib/RingTheory/Polynomial/Wronskian.lean, adding a lemma that its det for l = 2 is Polynomial.wronskian; locally keep (call sites Roth/Wronskian.lean l.60/71/139/161/163, Roth/GenWronskian.lean:244, Roth/Separation.lean:358).
---

# Roth.wronskianMatrix

## Inventory entry

### `def Roth.wronskianMatrix`
- **Type**: `{K : Type*} → [Field K] → {l : ℕ} → (φ : Fin l → K[X]) → Matrix (Fin l) (Fin l) K[X]`
- **What**: The `l × l` Wronskian matrix of a family of univariate polynomials built from Hasse derivatives: entry `(μ, ν)` is `hasseDeriv μ (φ ν) = (1/μ!) d^μ φ_ν / dt^μ`.
- **How**: One-line definition `Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)` using mathlib's `Polynomial.hasseDeriv` and `Matrix.of`.
- **Hypotheses**: `[Field K]` (section variable); no other hypotheses.
- **Uses from project**: `[]` (`hasseDeriv` here is mathlib's `Polynomial.hasseDeriv`)
- **Used by**: Roth/Wronskian.lean: `Roth.wronskian` (l.60, definition), `wronskian_eq_zero_of_not_linearIndependent` (l.71), `coeff_wronskian_of_natDegree_injective` (l.139), `wronskian_update_sub_smul` (l.161, l.163); Roth/GenWronskian.lean: `wronskian_kronecker_eq_sum_aux` (private, l.244); Roth/Separation.lean: `det_hasseDeriv_separated` (l.358)
- **Visibility**: public
- **Lines**: 55–57, proof length 1 line (definition body)
- **Notes**: Uses Hasse derivatives, not ordinary derivatives, so the determinant differs from the classical Wronskian by the constant `∏ μ!` (equal for `l ≤ 2`). For `l = 2` its determinant is exactly mathlib's `Polynomial.wronskian a b` (verified in evidence).

## Junk check (Step 8)
- Used anywhere? Yes: it is the body of `Roth.wronskian` and is unfolded or referenced explicitly in 4 further proofs across 3 files (`Matrix.det_updateCol_add_smul_self (wronskianMatrix φ)`, `(aeval (X none)).mapMatrix (wronskianMatrix φ)` in Separation.lean).
- Wrapper of 1–2 mathlib calls? Syntactically yes (`Matrix.of` + `Polynomial.hasseDeriv`), but it names a standard object and is the handle used for column operations and `mapMatrix`/transpose arguments on the matrix (not only its determinant).
- Does mathlib have it? No: mathlib only has the two-polynomial `Polynomial.wronskian a b = a * b' - a' * b` and `wronskianBilin`; its module docstring lists "Define Wronskian for n-tuple of polynomials" as a TODO.
- Too specific / inline? No: inlining would force `Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)` into `Roth.wronskian` and the Separation.lean `mapMatrix` argument; the named matrix is the natural API.
- Well-chosen definition? Yes (Hasse derivatives make the Wronskian work in every characteristic and match the source's `(1/μ!) d^μ/dt^μ`); only the `[Field K]` assumption is stronger than needed.
- Conclusion: `KEEP` — action: keep; generalise the ring when upstreaming.

## Mathlibable assessment (Step 9)

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Wronskian` compiles with `lake env lean`)
- decl `Roth.wronskianMatrix`: resolved at Roth/Wronskian.lean:56
- kind:                      def
- has sorry:                 no
- module docstring summary:  Wronskians of finitely many univariate polynomials (Hasse-derivative `l × l` determinant) and the linear-independence criterion in characteristic zero.

### Statement (Phase 1)

`Roth.wronskianMatrix` is a definition of the following: given polynomials `φ_0, …, φ_{l-1} ∈ K[t]`, the Wronskian matrix is the `l × l` matrix with entries `W_{μν} = D^{(μ)} φ_ν`, where `D^{(μ)} = (1/μ!) d^μ/dt^μ` is the `μ`-th Hasse derivative (rows: derivative order `0 ≤ μ < l`; columns: the polynomials). Its determinant is the (Hasse) Wronskian `W(φ_0, …, φ_{l-1})`.

Variables / typeclasses involved (Lean side):
- `K : Type*` with `[Field K]` — coefficient ring.
- `l : ℕ` — number of polynomials (= size of the matrix).
- `φ : Fin l → K[X]` — the family of polynomials.

Hypotheses (Lean side):
- none.

Conclusion (math): the matrix `(D^{(μ)} φ_ν)_{μ,ν}` with entries in `K[t]`.

Conclusion (Lean): n/a — definition (`Matrix (Fin l) (Fin l) K[X]`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: auxiliary matrix underlying the Wronskian; the named concept (`Roth.wronskian`) is its determinant, and neither is a main result of the project.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | yes (weak) | proofs unfold it deliberately (`simp [wronskianMatrix, ...]` in Wronskian.lean l.71, l.163, GenWronskian.lean l.244; `rw [wronskian, wronskianMatrix, Matrix.det_apply', ...]` l.139); keeping it sealed lets `Matrix.det_updateCol_add_smul_self (wronskianMatrix φ)` be applied before entries are exposed |
| Avoid typeclass diamonds         | no       | no instances involved |
| Mark semantic intent / API name  | yes      | consumers that need the matrix itself, not just the determinant: `wronskian_update_sub_smul` (column operation on `wronskianMatrix φ`), `det_hasseDeriv_separated` in Separation.lean (`(aeval (X none)).mapMatrix (wronskianMatrix φ)` and its transpose) |

Conclusion: ONE-LINER WITH-EXEMPTION

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Hasse derivative Wronskian determinant linear independence polynomials positive characteristic | yes | `det (D^{(μ)} f_ν)` with Hasse derivatives; criterion for linear independence over constants in char p (Garcia–Voloch 1987, Wang 1999); Hasse vs ordinary Wronskian differ by a constant nonzero when `n < char` | arXiv 1509.01650, 0807.4332, 0901.3843 |
| 2 | WebSearch (general form) | Wronskian matrix of n functions definition derivatives determinant | yes | `n × n` matrix with row `i` the `i`-th derivatives of `f_1..f_n`; "Wronskian matrix", Wronskian = its determinant | Wikipedia "Wronskian", Rutgers lecture notes; ordinary derivatives, functions on an interval |
| 3 | WebSearch (named-after / aliases) | "generalized Wronskian" Roth's theorem lemma Schmidt Hasse-Schmidt derivation Wronskian | yes | generalized Wronskians (Ostrowski) used in Roth's lemma; F. K. Schmidt (1939) Hasse-derivative Wronskians for Weierstrass points | arXiv 1310.4683, 1611.00248; Roth 1955 Lemma 1 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for Wronsk | yes | §2 l.157-163: `W(φ_0..φ_{l-1})(t) = det ((1/μ!) d^μ/dt^μ φ_ν(t))_{0≤μ,ν≤l-1}` | exact source of the def |
| 6 | nLab | nLab Wronskian (query: nLab Wronskian OR mathoverflow Wronskian Hasse derivatives characteristic p linearly dependent polynomials) | no | — | no nLab page surfaced; Wronskian is classical analysis/algebra, not covered by nLab |
| 7 | nCatLab | — | n/a | — | not a categorical concept (nLab check #6 found nothing either) |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry concept in Stacks (Wronskians appear only in curve theory texts like Stöhr–Voloch, surfaced via #6 query: arXiv math/0011091) |
| 9 | MathOverflow / Math.SE | same query as #6 | partial | no MO thread surfaced; arXiv 1301.6598 "Wronskians and linear independence" (Bostan–Dumas) gives the characteristic caveat (`x^p, 1`) | confirms why Hasse derivatives are preferred |
| 10 | recent arXiv (last 5 years) | results of #1, #6 | yes | arXiv 2602.20832 (2026, PIT via Wronskian), 2107.11266 (2021, Hasse-derivative Wronskians over function fields) | Hasse-derivative Wronskian is the standard form in char-free treatments |

### Literature summary (Phase 3)

Concept identified as: Wronskian matrix (and Wronskian) of a finite family of polynomials; in its characteristic-free form, the Hasse (Schmidt) Wronskian `det (D^{(μ)} f_ν)`.
Sources agree on the standard form: no — classical texts use ordinary derivatives `f_ν^{(μ)}`; algebraic / char-p texts (Schmidt, Garcia–Voloch, Wang, Stöhr–Voloch) and the project source use Hasse derivatives `(1/μ!) f_ν^{(μ)}`. The two determinants differ by the constant `∏_{μ<l} μ!`.
Most general standard form: for an `n`-tuple `f_1..f_n` in a commutative ring with a (Hasse–Schmidt) higher derivation `(D^{(i)})`, the matrix `(D^{(i)} f_j)_{0≤i<n, 1≤j≤n}`; for polynomials, any coefficient (semi)ring.
Generality dimensions where the literature varies:
  - derivative: ordinary (char 0 only meaningful) to Hasse (all characteristics); Hasse is the more general/robust choice.
  - coefficient ring: real/complex functions, fields, to arbitrary commutative rings; the matrix itself needs no hypotheses on the ring.
  - ambient object: polynomials, power series, or a general differential ring with Hasse–Schmidt derivation.
Disagreement with the literature: none beyond the Hasse-vs-ordinary normalisation; the project follows the char-free convention and its source.

### Generality analysis — `Roth.wronskianMatrix`

Literature-standard form (from Phase 3): `(D^{(μ)} f_ν)_{μ,ν}` for `f : Fin n → R[X]`, `R` any (semi)ring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | any (semi)ring | yes | `Polynomial.hasseDeriv` and `Matrix.of` need only `[Semiring R]`; verified: `wronskianMatrix'` over `[Semiring R]` compiles and the project def is `rfl`-equal to its specialisation (evidence file) |
| 2 | columns `Fin l` | `Fin l → K[X]` | `n`-tuple | yes (for the matrix) | the matrix makes sense with any column type `ι` (verified, `Matrix (Fin l) ι R[X]`), but the determinant needs a square matrix, so `Fin l` columns is the right choice for the Wronskian API |
| 3 | rows `Fin l`, `μ` cast to ℕ | derivative orders `0..l-1` | `0..n-1` | no | standard |
| 4 | Hasse vs ordinary derivative | Hasse | Hasse (char-free) / ordinary (classical) | no | Hasse is the more general convention (meaningful in char p) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 recommended (`[Field K]` to `[Semiring R]`; verified clean with `lake env lean`), 1 verified but not recommended (general column type).
Proposed restatement (if STRICTLY NARROWER):

```lean
namespace Polynomial
variable {R : Type*} [Semiring R]
/-- The Wronskian matrix `(hasseDeriv μ (φ ν))_{μ, ν}` of `l` polynomials. -/
noncomputable def wronskianMatrix {l : ℕ} (φ : Fin l → R[X]) : Matrix (Fin l) (Fin l) R[X] :=
  Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)
end Polynomial
```

Cost of restatement: CHEAP — mechanical; the body is unchanged, field-dependent lemmas just specialise.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic finite object |
| 3 | construction vs universal property? | no | — | a concrete matrix |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to (semi)ring? | yes | `[Semiring R]` (row 1 of Phase 4a) | `Matrix.det` over `[CommRing R]`, `RingHom.mapMatrix`/`AlgHom.map_det` base change, `Matrix.det_updateCol_add_smul_self`, all available over comm rings; integrality / ℤ[X] Wronskians |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | partial | column index `ι` possible but not useful for a determinant | — |
| 8 | concrete-via-abstract? | partial | the body only uses that `hasseDeriv μ` is a family of linear maps; a version for any `ℕ`-indexed family of operators (Hasse–Schmidt derivation) on a ring is conceivable | not recommended: mathlib has no bundled Hasse–Schmidt derivation for polynomials beyond `Polynomial.hasseDeriv`, so the polynomial form is the right first target |
| 9 | false-generalisation guard | no false generalisation | the `[Semiring R]` version is literally the same matrix (`rfl`, evidence); and for `l = 2` its determinant is exactly mathlib's `Polynomial.wronskian` (evidence), so the upstream n-ary notion is a genuine generalisation of the existing mathlib def | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Polynomial.wronskianMatrix {R} [Semiring R] {l} (φ : Fin l → R[X])` (Phase 4b), with the n-ary determinant `Polynomial.wronskianDet`-style companion (naming to be settled against the existing two-argument `Polynomial.wronskian`) and a bridge lemma `det (wronskianMatrix ![a, b]) = wronskian a b`.
  - Cost: CHEAP
  - Mathlib downstream this enables: fills the TODO "Define Wronskian for n-tuple of polynomials" in `Mathlib/RingTheory/Polynomial/Wronskian.lean`; n-ary Mason–Stothers / abc for polynomials (generalising `Mathlib/NumberTheory/FLT/MasonStothers.lean`, which uses the 2-ary Wronskian), linear-independence criterion `LinearIndependent K φ ↔ det ≠ 0` in char 0.
  - Real mathematical improvement: namespace `Polynomial` and semiring generality match where mathlib keeps `Polynomial.hasseDeriv` and `Polynomial.wronskian`; nothing in the definition uses a field.

### Proof strategy — `Roth.wronskianMatrix`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | n-ary Wronskian API: `wronskian_eq_zero_of_not_linearIndependent`, `wronskian_eq_zero_iff` (char 0), relation to `Polynomial.wronskian` for `l = 2`, Hasse-vs-ordinary scaling by `∏ μ!` | follow-up PR together with the def |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (definition via `Matrix.of` of `Polynomial.hasseDeriv`; no proof).
  - Missing mathlib API: the n-ary Wronskian lemmas in row 5.

### Diamond / defeq risk — `Roth.wronskianMatrix`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | defines a matrix value; no instances defined; only `Semiring`/`Field` assumed and used by `hasseDeriv` |
| 2 | Reducibility leak | none | plain semireducible `noncomputable def`; entry formula available by `rfl` (evidence probe) and unfolded only via explicit `simp [wronskianMatrix]`/`rw` |
| 3 | Non-canonical unfolding | low | `Matrix.of` application needs `Matrix.of_apply` after unfolding; standard, and an `@[simp] wronskianMatrix_apply` lemma would remove it |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | evidence probe elaborates with `K : Type 1` and `Type*` |
| 6 | Coercion ambiguity | none | no `CoeFun`/`CoeSort`; name `Polynomial.wronskianMatrix` free in mathlib (grep); only clash is the determinant name with the existing 2-ary `Polynomial.wronskian` |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none (naming of the n-ary determinant vs existing `Polynomial.wronskian` is a design point, not a defeq risk)
Recommended mitigations: n/a

### Mathlib search-status: `Roth.wronskianMatrix`

[A] Lean-Finder       "matrix whose (i,j) entry is the i-th derivative of the j-th polynomial (Wronskian matrix)"   no hit for the n-ary form (only `Polynomial.wronskian`, `wronskianBilin`, `Polynomial.sylvesterDeriv`)
[B] Loogle            `Polynomial.hasseDeriv, Matrix`   no hits
[C] LeanSearch        "Wronskian of a family of n polynomials determinant of matrix of iterated derivatives"   only the 2-ary `Polynomial.wronskian` family
[D] Grep mathlib src  `wronsk` (case-insensitive: only RingTheory/Polynomial/Wronskian.lean, NumberTheory/FLT/MasonStothers.lean, RingTheory/Polynomial/Radical.lean, all 2-ary), `Matrix.of fun.*hasseDeriv`, `Matrix.of fun.*derivative`, `iteratedDeriv.*Matrix`, `def .*[wW]ronsk`   no n-ary hit; `Mathlib/RingTheory/Polynomial/Wronskian.lean` has TODO "Define Wronskian for n-tuple of polynomials, not necessarily two."
[E] Name pattern      grep `wronskianMatrix`, `Matrix.wronskian`   no hits

Searched for both the user's form (Hasse-derivative matrix over a field) and the literature-standard form (n-ary Wronskian with ordinary or Hasse derivatives over a ring).

Concluded: found a partial match (`Polynomial.wronskian`, `Mathlib/RingTheory/Polynomial/Wronskian.lean:43`); covers only `l = 2` (and the determinant, not the matrix). For `l = 2`, `det (wronskianMatrix ![a, b]) = Polynomial.wronskian a b` holds exactly (evidence). The n-ary form is not in mathlib.

### Normal-form check — `Roth.wronskianMatrix`

Equivalent formalisms: `Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)`; its transpose `(hasseDeriv ν (φ μ))`; ordinary-derivative matrix `(derivative^[μ] (φ ν))` (differs by row scaling `1/μ!`, only over ℚ-algebras).
Does mathlib already have a canonical form? no (only 2-ary `a * b' - a' * b`).
Proposed canonical form: rows = derivative order, columns = polynomials, Hasse derivatives (char-free); bridge lemmas to `Polynomial.wronskian` (l = 2) and to the ordinary-derivative matrix (det scaled by `∏ μ!`) with the canonical form on the RHS.
RHS convention respected? yes (n/a for the def; bridge lemmas to be stated with the n-ary form on the RHS).

### Syntactic generality — `Roth.wronskianMatrix`

Alternative restatements attempted:
- `[Semiring R]`, `φ : Fin l → R[X]` (compiles, evidence)
- `[Semiring R]`, `φ : ι → R[X]`, `Matrix (Fin l) ι R[X]` (compiles, evidence)
- transpose convention (rows = polynomials) — not tried in Lean; would just transpose every consumer
Chosen restatement: `[Semiring R]`, `φ : Fin l → R[X]`, square.
Justification: the determinant is the only consumer that matters and needs a square matrix; row = derivative order matches the source and the classical layout.

### Superfluous-argument audit — `Roth.wronskianMatrix`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `Semiring` suffices (verified) |
| 2 | `l` | yes | matrix size |
| 3 | `φ` | yes | the family |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (`[Semiring R]`, `Polynomial` namespace)
Superfluous arguments: 1 to drop (`[Field K]` weakened to `[Semiring R]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.wronskianMatrix`

Internal use count: 2 (outside the declaring file); 5 inside Roth/Wronskian.lean
External-to-file callers: 2 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Wronskian.lean:60 | `noncomputable def wronskian (φ : Fin l → K[X]) : K[X] := (wronskianMatrix φ).det` |
| Roth/Wronskian.lean:71 | `simpa [wronskianMatrix, Matrix.mulVec, dotProduct, ← smul_eq_C_mul, mul_comm]` |
| Roth/Wronskian.lean:139 | `rw [wronskian, wronskianMatrix, Matrix.det_apply', Matrix.det_apply', finsetSum_coeff,` |
| Roth/Wronskian.lean:161 | `(Matrix.det_updateCol_add_smul_self (wronskianMatrix φ) h.symm (-C c))` |
| Roth/Wronskian.lean:163 | `simp [wronskianMatrix, Matrix.updateCol_apply, Function.update_apply, apply_ite,` |
| Roth/GenWronskian.lean:244 | `simpa [wronskian, wronskianMatrix, hc, genWronskian, AlgHom.map_det, Matrix.map] using` |
| Roth/Separation.lean:358 | `← Matrix.det_transpose ((Polynomial.aeval (X none)).mapMatrix (wronskianMatrix φ)),` |

Inline-derivation grep: Roth/Separation.lean:352 and Roth/GenWronskian.lean build related but different matrices (`Matrix.of fun μ ν ↦ hasseDeriv (...multi-index...) (...)` for generalized Wronskians, MvPolynomial Hasse derivatives); no re-derivation of `Matrix.of fun μ ν ↦ Polynomial.hasseDeriv μ (φ ν)` outside the def.

### Composition check (Phase 6)

Can `Roth.wronskianMatrix` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Matrix.of fun μ ν ↦ Polynomial.hasseDeriv μ (φ ν)` — this is the body itself.
  - Mathlib decls used: `Matrix.of`, `Polynomial.hasseDeriv`
  - Result: succeeds as a term, but there is no mathlib concept it composes into; the named object is needed for `Roth.wronskian`, column operations, and `mapMatrix` base change.
  - Notes: trivial composition; record as "trivial composition; user decides if worth a definition".

Attempt 2: derive from `Polynomial.wronskian`.
  - Mathlib decls used: `Polynomial.wronskian`
  - Result: fails for `l ≠ 2` (2-ary only, and gives a determinant, not a matrix).

Conclusion: NOT-COMPOSABLE as a replacement for the named n-ary concept.

## Verdict: `Roth.wronskianMatrix`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the `l × l` Wronskian matrix is classical (Wikipedia; Muir), and its Hasse-derivative form is the char-free standard (F. K. Schmidt 1939; Garcia–Voloch 1987; Wang 1999; project source §2).
- Generality analysis (Phase 4): STRICTLY NARROWER — `[Field K]` is superfluous; `[Semiring R]` verified in the evidence file.
- Mathlib search (Phase 5): only the 2-ary `Polynomial.wronskian` (partial match); mathlib's own TODO asks for the n-ary version.
- Composition check (Phase 6): NOT-COMPOSABLE (trivial body, no n-ary concept to compose with).

**Rationale:**

Mathlib's `Mathlib/RingTheory/Polynomial/Wronskian.lean` defines only `Polynomial.wronskian a b = a * b' - a' * b` (with `wronskianBilin`) and records "Define Wronskian for n-tuple of polynomials, not necessarily two" as a TODO. The project's `wronskianMatrix` with `Roth.wronskian` is exactly that n-ary object. Its Hasse-derivative normalisation is the right one for mathlib: it works in every characteristic, and for `l = 2` the determinant is exactly mathlib's `Polynomial.wronskian a b`, because `hasseDeriv 1 = derivative` and `0!·1! = 1`. Both `det (wronskianMatrix' 2 ![a, b]) = Polynomial.wronskian a b` over any `CommRing` and `Roth.wronskian ![a, b] = Polynomial.wronskian a b` compile in the evidence file. So the upstream def is a genuine generalisation of the existing mathlib def, not a competing notion. The one-liner is covered by the API-name exemption (Phase 2b): consumers manipulate the matrix itself (column operations in `wronskian_update_sub_smul`, `mapMatrix`/transpose in Separation.lean's `det_hasseDeriv_separated`). Phase 4.5 risk is LOW.

The only defect is generality: nothing uses `[Field K]`, since `Polynomial.hasseDeriv` and `Matrix.of` need only `[Semiring R]`. The verified restatement is `rfl`-equal to the project def.

Reason for the generalisation: LITERATURE-WEAKENING (field to semiring) plus MODERN-IDIOM (Polynomial namespace next to `Polynomial.hasseDeriv`/`Polynomial.wronskian`).
Proposed restatement:
```lean
namespace Polynomial
variable {R : Type*} [Semiring R]
/-- The Wronskian matrix `(hasseDeriv μ (φ ν))_{μ, ν}` of `l` polynomials. -/
noncomputable def wronskianMatrix {l : ℕ} (φ : Fin l → R[X]) : Matrix (Fin l) (Fin l) R[X] :=
  Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)
@[simp] theorem wronskianMatrix_apply {l : ℕ} (φ : Fin l → R[X]) (μ ν : Fin l) :
    wronskianMatrix φ μ ν = hasseDeriv μ (φ ν) := rfl
theorem det_wronskianMatrix_fin_two {R : Type*} [CommRing R] (a b : R[X]) :
    (wronskianMatrix ![a, b]).det = wronskian a b := by
  sorry -- proved in evidence file by simp [Matrix.det_fin_two, hasseDeriv_one, mul_comm]
end Polynomial
```
Estimated cost of regeneralisation: CHEAP (body unchanged; the Roth section variable `[Field K]` stays for the lemmas that need it).
Mathlib downstream this enables:
- closes the n-tuple TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean`, with `Polynomial.wronskian` recovered at `l = 2`;
- n-ary linear-independence criterion (`Roth.wronskian_eq_zero_iff`, char 0) and the easy direction over any field (`wronskian_eq_zero_of_not_linearIndependent`);
- base change of the Wronskian via `RingHom.mapMatrix`/`AlgHom.map_det` over commutative rings (as used in Separation.lean), and n-ary Mason–Stothers-style degree bounds extending `Mathlib/NumberTheory/FLT/MasonStothers.lean`.
PR grouping: ship together with `Roth.wronskian` (the determinant; its n-ary name must be reconciled with the existing 2-ary `Polynomial.wronskian`, e.g. by a different name or by `l = 2` bridge lemmas) and `wronskian_eq_zero_of_not_linearIndependent`; a lone matrix def would be an orphan one-liner.
Next action: run `/generalise Roth.wronskianMatrix`, then upstream as `Polynomial.wronskianMatrix` over `[Semiring R]` in `Mathlib/RingTheory/Polynomial/Wronskian.lean` together with the n-ary determinant and the `l = 2` bridge lemma; PR title "feat(RingTheory/Polynomial/Wronskian): Wronskian of n polynomials".

---

## Next step

Run `/generalise Roth.wronskianMatrix`; upstream as `Polynomial.wronskianMatrix` over `[Semiring R]` with `Roth.wronskian` and the `l = 2` bridge lemma to `Polynomial.wronskian`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.wronskianMatrix/weaken_and_relate.lean` (compiles cleanly with `lake env lean`, after one fix: the first run failed only because a probe `example` returning a noncomputable matrix needed `noncomputable`; replaced with an `rfl` entry probe). It verifies: (1) `wronskianMatrix'` over `[Semiring R]` with an arbitrary column type elaborates, and `Roth.wronskianMatrix φ = wronskianMatrix' l φ` by `rfl`; (2) `det (wronskianMatrix' 2 ![a, b]) = Polynomial.wronskian a b` over any `CommRing`, and `Roth.wronskian ![a, b] = Polynomial.wronskian a b`; (3) the entry formula holds by `rfl` and the def elaborates at `K : Type 1`.
- Mathlib greps: `wronsk` (3 files, all 2-ary), `Matrix.of fun.*hasseDeriv`, `Matrix.of fun.*derivative`, `def .*[wW]ronsk`, `iteratedDeriv.*Matrix`: no n-ary Wronskian; TODO located in `Mathlib/RingTheory/Polynomial/Wronskian.lean` module docstring.
- Lean-Finder / LeanSearch: only `Polynomial.wronskian` family; Loogle `Polynomial.hasseDeriv, Matrix`: no hits.
- WebSearch: 4 queries (results summarised in the literature table). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn wronskianMatrix Roth/` for the call-sites table.
