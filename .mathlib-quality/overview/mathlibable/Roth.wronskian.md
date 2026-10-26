---
decl: Roth.wronskian
file: Roth/Wronskian.lean
line: 60
kind: def
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The n-ary (Hasse) Wronskian det (D^(mu) phi_nu) is the object mathlib's RingTheory/Polynomial/Wronskian.lean lists as a TODO (only the 2-ary Polynomial.wronskian exists, and ours equals it at l = 2 over any CommRing, verified); the def only needs [CommRing R], not [Field K], and its name must be reconciled with the existing 2-ary Polynomial.wronskian.
action: Upstream together with Roth.wronskianMatrix in Mathlib/RingTheory/Polynomial/Wronskian.lean over [CommRing R] (verified in evidence) under a non-clashing n-ary name, with the l = 2 bridge lemma to Polynomial.wronskian, a map/base-change lemma (verified) and wronskian_eq_zero_of_not_linearIndependent; locally keep (call sites Roth/Wronskian.lean l.66/123/139/149/159/206/220, Roth/GenWronskian.lean:241/244, Roth/Separation.lean:356/357/528).
---

# Roth.wronskian

## Inventory entry

### `def Roth.wronskian`
- **Type**: `{K : Type*} → [Field K] → {l : ℕ} → (φ : Fin l → K[X]) → K[X]`
- **What**: The Wronskian of `l` univariate polynomials, `W(φ_0, …, φ_{l-1}) = det (D^{(μ)} φ_ν)_{0 ≤ μ, ν < l}` with `D^{(μ)} = hasseDeriv μ` the `μ`-th Hasse derivative (`(1/μ!) d^μ/dt^μ`).
- **How**: One-line definition `(wronskianMatrix φ).det`, i.e. mathlib's `Matrix.det` of the project's `Roth.wronskianMatrix`.
- **Hypotheses**: `[Field K]` (section variable); no other hypotheses.
- **Uses from project**: `Roth.wronskianMatrix`
- **Used by**: Roth/Wronskian.lean: `wronskian_eq_zero_of_not_linearIndependent` (l.66), `coeff_wronskian_of_natDegree_injective` (l.123 statement, l.139 unfolds it), `wronskian_ne_zero_of_natDegree_injective` (l.149), `wronskian_update_sub_smul` (l.159), `wronskian_ne_zero_of_linearIndependent` (l.206), `wronskian_eq_zero_iff` (l.220); Roth/GenWronskian.lean: `wronskian_kronecker_eq_sum_aux` (private, l.241 statement, l.244 unfolds it); Roth/Separation.lean: `det_hasseDeriv_separated` (l.356 statement, l.357 unfolds it), `exists_rat_factors_det_hasseDeriv_aux` (private, l.528)
- **Visibility**: public
- **Lines**: 59–60, proof length 1 line (definition body)
- **Notes**: Hasse-derivative normalisation: differs from the classical Wronskian by the constant `∏_{μ<l} μ!` (equal for `l ≤ 2`). For `l = 2` it is exactly mathlib's `Polynomial.wronskian a b` over any commutative ring (verified in evidence). The name clashes conceptually with mathlib's 2-ary `Polynomial.wronskian` if moved to the `Polynomial` namespace.

## Junk check (Step 8)
- Used anywhere? Yes: 8 project declarations across 3 files state results about it (the whole linear-independence criterion of §2, the generalized-Wronskian reduction in GenWronskian.lean, the separation lemma in Separation.lean).
- Wrapper of 1–2 mathlib calls? Syntactically one call (`Matrix.det`) on a project def, but it names the central object of §2 of the source; all statements are about `wronskian φ`, never about the raw determinant.
- Does mathlib have it? No: only the 2-ary `Polynomial.wronskian a b = a * b' - a' * b` (and `wronskianBilin`); `Mathlib/RingTheory/Polynomial/Wronskian.lean` lists "Define Wronskian for n-tuple of polynomials, not necessarily two." as a TODO.
- Too specific / inline? No: inlining `(wronskianMatrix φ).det` into 8 statements would make the API unreadable and lose the named concept.
- Well-chosen definition? Yes (Hasse derivatives work in every characteristic and match the source); only `[Field K]` is stronger than needed (`[CommRing R]` suffices for the determinant).
- Conclusion: `KEEP` — action: keep; generalise the ring and pick a non-clashing name when upstreaming with `wronskianMatrix`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name has no `_aux`; docstring does not start with internal/auxiliary; Step 8 said KEEP; qualified name `Roth.wronskian` absent from mathlib (mathlib has `Polynomial.wronskian`, a different, 2-ary declaration). Not a glue lemma (it is a new def, the determinant of the parent matrix), so the full workflow is run below; it reuses the parent assessment `Roth.wronskianMatrix` (YES-but-generalise-first) where the evidence is shared.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Wronskian` elaborates clean in the LSP)
- decl `Roth.wronskian`:     resolved at Roth/Wronskian.lean:60
- kind:                      def
- has sorry:                 no
- module docstring summary:  Wronskians of finitely many univariate polynomials (Hasse-derivative `l × l` determinant) and the linear-independence criterion in characteristic zero.

### Statement (Phase 1)

`Roth.wronskian` is a definition of the following: for polynomials `φ_0, …, φ_{l-1} ∈ K[t]`, their Wronskian is the polynomial `W(φ_0, …, φ_{l-1}) = det (D^{(μ)} φ_ν)_{0 ≤ μ, ν ≤ l-1}`, where `D^{(μ)} = (1/μ!) d^μ/dt^μ` is the `μ`-th Hasse derivative. Over a field of characteristic zero it vanishes iff the `φ_ν` are linearly dependent over `K` (proved in the same file).

Variables / typeclasses involved (Lean side):
- `K : Type*` with `[Field K]` — coefficient ring.
- `l : ℕ` — number of polynomials.
- `φ : Fin l → K[X]` — the family.

Hypotheses (Lean side):
- none.

Conclusion (math): the polynomial `det (D^{(μ)} φ_ν)`.

Conclusion (Lean): n/a — definition (value in `K[X]`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a named classical concept used as a tool for Roth's lemma, not a main result and not a new structure (it is a polynomial-valued function); the file's main results are the theorems about it.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | yes (weak) | proofs unfold it only deliberately (`rw [wronskian, wronskianMatrix, Matrix.det_apply', ...]` l.139; `rw [genWronskian, wronskian, AlgHom.map_det, ...]` Separation.lean l.357; `simpa [wronskian, wronskianMatrix, ...]` GenWronskian.lean l.244); keeping it sealed keeps statements like `wronskian_eq_zero_iff` from being rewritten into raw determinants by `simp` |
| Avoid typeclass diamonds         | no       | no instances involved |
| Mark semantic intent / API name  | yes      | 8 consumers in 3 files state results about `wronskian φ` (e.g. `wronskian_eq_zero_iff`, `wronskian_ne_zero_of_linearIndependent` used in GenWronskian.lean l.262 and Separation.lean l.534, `det_hasseDeriv_separated`); "the Wronskian" is the classical named object |

Conclusion: ONE-LINER WITH-EXEMPTION

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Wronskian of n polynomials determinant Hasse derivatives linear independence characteristic p | yes | `det (D^{(i)} P_j)` with Hasse derivatives; nonvanishing iff linearly independent when `char = 0` or `char > degree`; Hasse vs ordinary differs by a constant nonzero for `n < char` | arXiv 1404.4506 (Thm 3.2), 2602.20832 (Thm 2.11), 1301.6598 (`1, x^p` counterexample), 2107.11266 (Garcia–Voloch / Wang hyperderivative Wronskian) |
| 2 | WebSearch (general form) | Wronskian determinant of n functions over a commutative ring differential ring definition | yes | Wronskian of `y_1..y_n` in a differential ring = det of the `n × n` matrix of successive derivatives, determinant taken in the (commutative) ring | Magma handbook "Wronskian Matrix"; arXiv 1708.04137; Wikipedia "Wronskian" |
| 3 | WebSearch (named-after / aliases) | "Hasse-Schmidt Wronskian" OR "generalized Wronskian" Roth lemma Schmidt | yes | generalized Wronskians (Ostrowski) in Roth's lemma; F. K. Schmidt 1939 Wronskians for Weierstrass points; Roth 1955 Lemma | arXiv 1611.00248, 1310.4683; Roth, Mathematika 1955 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for Wronsk | yes | §2 l.157–166: `W(φ_0..φ_{l-1})(t) = det ((1/μ!) d^μ/dt^μ φ_ν(t))`, vanishes iff linearly dependent over ℚ | exact source of the def and its main lemma |
| 6 | nLab | nLab OR mathoverflow Wronskian linearly dependent polynomials Hasse derivative | no | — | no nLab page surfaced; classical algebra/ODE concept, not covered by nLab |
| 7 | nCatLab | — | n/a | — | not a categorical concept (nLab query #6 found nothing either) |
| 8 | Stacks Project | — | n/a | — | not a scheme-theoretic concept in Stacks; Wronskians appear in curve-theory literature (Stöhr–Voloch), surfaced via #1/#3 |
| 9 | MathOverflow / Math.SE | same query as #6 | partial | no MO thread surfaced; Bostan–Dumas arXiv 1301.6598 "Wronskians and linear independence" gives the characteristic caveat | confirms Hasse normalisation and the char-p failure |
| 10 | recent arXiv (last 5 years) | results of #1 | yes | arXiv 2602.20832 (2026, PIT via Wronskian), 2107.11266 (2021, hyperderivative Wronskians) | Hasse-derivative Wronskian is the char-free standard |

### Literature summary (Phase 3)

Concept identified as: the Wronskian (determinant) of a finite family of polynomials; char-free form: the Hasse (Schmidt) Wronskian `det (D^{(μ)} f_ν)`.
Sources agree on the standard form: no — classical texts use ordinary derivatives `f_ν^{(μ)}`; char-free texts (F. K. Schmidt, Garcia–Voloch, Wang, project source) use Hasse derivatives. The two determinants differ by `∏_{μ<l} μ!`; they coincide for `l ≤ 2`.
Most general standard form: for `f_1..f_n` in a commutative ring with a (Hasse–Schmidt) higher derivation, the determinant of `(D^{(i)} f_j)`; for polynomials, any commutative coefficient ring.
Generality dimensions where the literature varies:
  - derivative: ordinary (meaningful in char 0) to Hasse (all characteristics); Hasse is more general.
  - coefficient ring: ℝ/ℂ functions, fields, to arbitrary commutative rings (determinant needs commutativity).
  - ambient object: polynomials, power series, general differential rings.
Disagreement with the literature: none beyond the Hasse-vs-ordinary normalisation, which follows the source.

### Generality analysis — `Roth.wronskian`

Literature-standard form (from Phase 3): `det (D^{(μ)} f_ν)` for `f : Fin n → R[X]`, `R` a commutative ring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | commutative ring | yes | `Matrix.det` needs `[CommRing R]`, `hasseDeriv` only `[Semiring R]`; verified: `Evidence.wronskian` over `[CommRing R]` compiles and `Roth.wronskian φ = Evidence.wronskian φ` by `rfl` (evidence file) |
| 2 | `[CommRing R]` to `[CommSemiring R]` | — | — | no (in mathlib) | `Matrix.det` is defined only over `CommRing` in mathlib (signs); not attempted further |
| 3 | `φ : Fin l → K[X]` | `Fin l`-indexed | `n`-tuple | no | determinant needs a square matrix indexed by derivative orders `0..l-1`; a general `Fintype ι` column index would need an equivalence `ι ≃ Fin l` and a sign convention |
| 4 | Hasse vs ordinary derivative | Hasse | Hasse (char-free) | no | Hasse is the more general convention |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (`[Field K]` to `[CommRing R]`; verified clean via `lean_diagnostic_messages` on the evidence file, including `ℤ[X]` elaboration)
Proposed restatement (if STRICTLY NARROWER):

```lean
namespace Polynomial
variable {R : Type*} [CommRing R]
/-- The (Hasse) Wronskian `det (hasseDeriv μ (φ ν))_{μ, ν}` of `l` polynomials. -/
noncomputable def wronskianDet {l : ℕ} (φ : Fin l → R[X]) : R[X] := (wronskianMatrix φ).det
end Polynomial
```
(name `wronskianDet` is a placeholder; see Phase 5.5 on reconciling with the 2-ary `Polynomial.wronskian`.)

Cost of restatement: CHEAP — mechanical; the body is unchanged.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic, finite |
| 3 | construction vs universal property? | no | — | a concrete polynomial |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to (semi)ring? | yes | `[CommRing R]` (Phase 4a row 1) | `RingHom.map_det`/`AlgHom.map_det` base change (verified `map_wronskian` in evidence), integral Wronskians over `ℤ[X]`, compatibility with the existing 2-ary `Polynomial.wronskian` (also over `CommRing`) |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | `Fin l` needed for the square matrix of derivative orders | — |
| 8 | concrete-via-abstract? | partial | body only uses that `hasseDeriv μ` is a family of operators; a Hasse–Schmidt-derivation version is conceivable | not recommended: mathlib has no bundled Hasse–Schmidt derivation API beyond `Polynomial.hasseDeriv` |
| 9 | false-generalisation guard | no false generalisation | the `CommRing` version is `rfl`-equal to the project def; at `l = 2` it equals mathlib's `Polynomial.wronskian` (evidence `wronskian_fin_two`), at `l = 0` it is `1` and at `l = 1` it is `φ 0` (evidence) — same object | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Polynomial.<n-ary name> {R} [CommRing R] {l} (φ : Fin l → R[X]) : R[X] := (Polynomial.wronskianMatrix φ).det`, with `@[simp]` bridges at `l = 2` (to `Polynomial.wronskian`), `l = 0`, `l = 1`.
  - Cost: CHEAP
  - Mathlib downstream this enables: closes the n-tuple TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean`; base change via `Polynomial.map` (`map_wronskian`, verified); n-ary Mason–Stothers-type degree bounds generalising `Mathlib/NumberTheory/FLT/MasonStothers.lean`; the linear-independence criterion in char 0.
  - Real mathematical improvement: the determinant uses only commutativity of the coefficient ring; placing it next to `Polynomial.hasseDeriv` and `Polynomial.wronskian` in the `Polynomial` namespace makes the 2-ary mathlib def its `l = 2` case.

### Proof strategy — `Roth.wronskian`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | n-ary Wronskian API: `l = 2` bridge to `Polynomial.wronskian`, `map_wronskian` base change, `wronskian_eq_zero_of_not_linearIndependent` (any field; over domains via `Matrix.det_eq_zero_of_not_linearIndependent_cols`-style argument), `wronskian_eq_zero_iff` (char 0), Hasse-vs-ordinary scaling by `∏ μ!` | ship with the def |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (definition via `Matrix.det` of the Wronskian matrix; no proof).
  - Missing mathlib API: the n-ary lemmas in row 5.

### Diamond / defeq risk — `Roth.wronskian`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | defines a polynomial value; no instances introduced; uses only the `CommRing` structure for `Matrix.det` |
| 2 | Reducibility leak | none | plain semireducible `noncomputable def`; `Roth.wronskian φ = Evidence.wronskian φ` by `rfl`; unfolded only via explicit `rw [wronskian]`/`simp [wronskian]` in the three proofs listed |
| 3 | Non-canonical unfolding | low | `simp [wronskian, wronskianMatrix]` exposes `Matrix.det (Matrix.of ...)`; for small `l` (`Fin 0`, `Fin 1`, `Fin 2`) simp computes it cleanly (evidence), so bridge simp lemmas are easy to state |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `Type*` throughout; elaborates at `ℤ` and generic `R` in evidence; parent assessment probed `Type 1` |
| 6 | Coercion ambiguity | low | no coercions; but a name collision: mathlib's `Polynomial.wronskian (a b : R[X])` already exists, so the n-ary def cannot be called `Polynomial.wronskian` — naming decision, not a defeq risk |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none HIGH (naming clash with the 2-ary `Polynomial.wronskian` is a design point)
Recommended mitigations: n/a (choose a distinct n-ary name, e.g. `Polynomial.wronskianDet` or `Polynomial.Wronskian.det`, and prove the `l = 2` bridge)

### Mathlib search-status: `Roth.wronskian`

[A] Lean-Finder       "Wronskian of a finite family of n polynomials as determinant of matrix of derivatives"   only `Polynomial.wronskian`, `wronskianBilin(_apply)`, `wronskian_self_eq_zero` (2-ary), and unrelated `Matrix.det_matrixOfPolynomials`
[B] Loogle            `Matrix.det, Polynomial.hasseDeriv`   no hits
[C] LeanSearch        "Wronskian determinant of n polynomials vanishes iff linearly dependent"   only 2-ary `Polynomial.wronskian` family, `IsCoprime.wronskian_eq_zero_iff`, and the building block `Matrix.det_eq_zero_of_not_linearIndependent_cols`
[D] Grep mathlib src  case-insensitive `wronsk` (3 files: RingTheory/Polynomial/Wronskian.lean, RingTheory/Polynomial/Radical.lean, NumberTheory/FLT/MasonStothers.lean, all 2-ary); `def .*[wW]ronsk` (only `wronskian`, `wronskianBilin`, l.43/48)   no n-ary hit; TODO at Wronskian.lean l.27–29 "Define Wronskian for n-tuple of polynomials, not necessarily two."
[E] Name pattern      `lean_local_search` unavailable (ripgrep not installed); replaced by grep of mathlib for `wronskian`, `Roth.wronskian`, `wronskianDet`   only the 2-ary `Polynomial.wronskian`; `Roth.wronskian` and n-ary names absent

Searched for both the user's form (Hasse-derivative determinant over a field) and the literature-standard form (n-ary Wronskian over a commutative ring, ordinary or Hasse derivatives).

Concluded: found a partial match (`Polynomial.wronskian`, `Mathlib/RingTheory/Polynomial/Wronskian.lean:43`); covers only `l = 2`, where it agrees exactly with ours (evidence `wronskian_fin_two`). The n-ary form is not in mathlib.

### Normal-form check — `Roth.wronskian`

Equivalent formalisms: `det (hasseDeriv μ (φ ν))`; `det` of the transpose; ordinary-derivative determinant `det (derivative^[μ] (φ ν))` (= `∏ μ!` times ours); for `l = 2`, `a * b' - a' * b`.
Does mathlib already have a canonical form? only for `l = 2` (`Polynomial.wronskian a b`).
Proposed canonical form: the Hasse determinant (char-free); bridge `n-ary ![a, b] = Polynomial.wronskian a b` with the existing mathlib form on the RHS for `l = 2` (it is the established canonical spelling there), and the ordinary-derivative relation `det (derivative^[μ] φ ν) = (∏ μ!) • n-ary φ` with the n-ary form on the RHS.
RHS convention respected? yes

### Syntactic generality — `Roth.wronskian`

Alternative restatements attempted:
- `[CommRing R]`, `φ : Fin l → R[X]` (compiles, evidence)
- matrix inlined: `(Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)).det` without a named matrix (rejected: Separation.lean and `wronskian_update_sub_smul` manipulate the matrix)
- ordinary derivatives (rejected: wrong in char p, loses the char-free criterion)
Chosen restatement: `[CommRing R]`, `φ : Fin l → R[X]`, defined as `det` of the named matrix.
Justification: call sites apply `Matrix.det_*` and `RingHom.map_det` lemmas to the named matrix, and the `Fin l → R[X]` argument matches `![a, b]` for the 2-ary bridge.

### Superfluous-argument audit — `Roth.wronskian`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `[CommRing R]` suffices (verified) |
| 2 | `l` | yes | number of polynomials / matrix size |
| 3 | `φ` | yes | the family |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (bridge lemmas to be stated with the canonical forms on the RHS)
Syntactic generality: RESTATE (`[CommRing R]`, `Polynomial` namespace, non-clashing n-ary name)
Superfluous arguments: 1 to drop (`[Field K]` weakened to `[CommRing R]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.wronskian`

Internal use count: 5 lines outside the declaring file (4 declarations, 2 of them private); 8 lines inside Roth/Wronskian.lean (6 declarations)
External-to-file callers: 2 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Wronskian.lean:66 | `: wronskian φ = 0 := by` (`wronskian_eq_zero_of_not_linearIndependent`) |
| Roth/Wronskian.lean:123 | `(wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) = ...` |
| Roth/Wronskian.lean:139 | `rw [wronskian, wronskianMatrix, Matrix.det_apply', Matrix.det_apply', finsetSum_coeff,` |
| Roth/Wronskian.lean:149 | `(hd : Function.Injective fun ν ↦ (φ ν).natDegree) : wronskian φ ≠ 0 := by` |
| Roth/Wronskian.lean:159 | `wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = wronskian φ := by` |
| Roth/Wronskian.lean:206 | `(h : LinearIndependent K φ) : wronskian φ ≠ 0 := by` |
| Roth/Wronskian.lean:220 | `wronskian φ = 0 ↔ ¬ LinearIndependent K φ :=` |
| Roth/GenWronskian.lean:241 | `... : wronskian (fun ν ↦ kronecker k (φ ν)) =` (private `wronskian_kronecker_eq_sum_aux`) |
| Roth/GenWronskian.lean:244 | `simpa [wronskian, wronskianMatrix, hc, genWronskian, AlgHom.map_det, Matrix.map] using` |
| Roth/Separation.lean:356 | `Polynomial.aeval (X none : MvPolynomial (Option τ) K) (wronskian φ) := by` (`det_hasseDeriv_separated`) |
| Roth/Separation.lean:357 | `rw [genWronskian, wronskian, AlgHom.map_det, AlgHom.map_det,` |
| Roth/Separation.lean:528 | `Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) (wronskian φ) := by` (private `exists_rat_factors_det_hasseDeriv_aux`) |

Inline-derivation grep: no `(Matrix.of fun μ ν ↦ hasseDeriv μ (φ ν)).det` outside the def; Roth/Separation.lean:352/525 and Roth/GenWronskian.lean build determinants of multivariate (generalized) Hasse-derivative matrices, a different object (`Roth.genWronskian`).

### Composition check (Phase 6)

Can `Roth.wronskian` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(Matrix.of fun μ ν ↦ Polynomial.hasseDeriv μ (φ ν)).det` — the body with the matrix inlined.
  - Mathlib decls used: `Matrix.det`, `Matrix.of`, `Polynomial.hasseDeriv`
  - Result: succeeds as a term, but there is no mathlib concept it composes into for `l ≠ 2`; the named object carries 8 project statements.
  - Notes: trivial composition; record as "trivial composition; user decides if worth a definition" — and the exemption (named classical concept, mathlib TODO) applies.

Attempt 2: `Polynomial.wronskian (φ 0) (φ 1)`.
  - Mathlib decls used: `Polynomial.wronskian`
  - Result: fails for `l ≠ 2`; succeeds at `l = 2` (evidence `wronskian_fin_two`).

Conclusion: NOT-COMPOSABLE as a replacement for the named n-ary concept.

## Verdict: `Roth.wronskian`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the Wronskian of `n` functions/polynomials is classical (Wikipedia, Magma handbook for differential rings), its Hasse-derivative form is the char-free standard (Schmidt 1939; Garcia–Voloch; Wang; arXiv 1404.4506, 1301.6598; project source §2).
- Generality analysis (Phase 4): STRICTLY NARROWER — `[Field K]` is superfluous; `[CommRing R]` verified in the evidence file.
- Mathlib search (Phase 5): only the 2-ary `Polynomial.wronskian` (partial match, agrees at `l = 2`); mathlib's own TODO asks for the n-ary version.
- Composition check (Phase 6): NOT-COMPOSABLE (trivial body, but no n-ary concept to compose with).

**Rationale:**

`Mathlib/RingTheory/Polynomial/Wronskian.lean` defines only `Polynomial.wronskian a b = a * b' - a' * b` and lists "Define Wronskian for n-tuple of polynomials, not necessarily two" as a TODO. `Roth.wronskian` is that n-ary Wronskian, in the Hasse-derivative normalisation, which works in every characteristic. The evidence file shows that this choice is consistent with mathlib. Over any `CommRing`, `wronskian ![a, b] = Polynomial.wronskian a b`, so the existing def is the `l = 2` case and nothing competes with it. The degenerate cases come out correctly (`1` for `l = 0`, `φ 0` for `l = 1`), and the Wronskian commutes with `Polynomial.map` under any ring homomorphism (`map_wronskian`, the fact Separation.lean uses through `RingHom.map_det`/`AlgHom.map_det`). The def is a one-liner, but the API-name exemption applies: 8 project declarations state results about `wronskian φ`, including the char-0 criterion `wronskian_eq_zero_iff` that Roth's lemma needs. Phase 4.5 risk is LOW.

The defect is generality. Nothing uses `[Field K]`: `Matrix.det` needs only `[CommRing R]`, and the restated def is `rfl`-equal to the project def. The upstream name must also differ from the existing 2-ary `Polynomial.wronskian` (Phase 5.5 RESTATE-BEFORE-SHIP).

Reason for the generalisation: LITERATURE-WEAKENING (field to commutative ring) plus MODERN-IDIOM (Polynomial namespace next to `Polynomial.hasseDeriv`/`Polynomial.wronskian`, with the 2-ary def recovered at `l = 2`).
Proposed restatement:
```lean
namespace Polynomial
variable {R : Type*} [CommRing R]
/-- The Wronskian `det (hasseDeriv μ (φ ν))_{μ, ν}` of `l` polynomials. -/
noncomputable def wronskianDet {l : ℕ} (φ : Fin l → R[X]) : R[X] := (wronskianMatrix φ).det
@[simp] theorem wronskianDet_fin_two (a b : R[X]) : wronskianDet ![a, b] = wronskian a b := by
  sorry -- proved in evidence by simp [Matrix.det_fin_two, hasseDeriv_one, mul_comm]
theorem map_wronskianDet {S : Type*} [CommRing S] (f : R →+* S) {l : ℕ} (φ : Fin l → R[X]) :
    (wronskianDet φ).map f = wronskianDet fun ν ↦ (φ ν).map f := by
  sorry -- proved in evidence via RingHom.map_det and hasseDeriv_map
end Polynomial
```
Estimated cost of regeneralisation: CHEAP (body unchanged; field-dependent lemmas keep `[Field K]`).
Mathlib downstream this enables:
- closes the n-tuple TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean`, with `Polynomial.wronskian` as the `l = 2` case;
- base change of Wronskians along ring homomorphisms (`RingHom.map_det`, `Polynomial.map`), integral Wronskians over `ℤ[X]`;
- the n-ary linear-independence criterion (easy direction over any field, iff in char 0) and n-ary Mason–Stothers-type bounds extending `Mathlib/NumberTheory/FLT/MasonStothers.lean`.
PR grouping: one PR with `Roth.wronskianMatrix` (parent, YES-but-generalise-first), `wronskian_eq_zero_of_not_linearIndependent`, and the bridge lemmas; the char-0 iff (`wronskian_eq_zero_iff` with its helper lemmas) as a follow-up PR.
Next action: run `/generalise Roth.wronskian` (the target is `[CommRing R]`), then upstream it under a non-clashing n-ary name in `Mathlib/RingTheory/Polynomial/Wronskian.lean` with the `l = 2` bridge and `map` lemmas; PR title "feat(RingTheory/Polynomial/Wronskian): Wronskian of n polynomials".

---

## Next step

Run `/generalise Roth.wronskian`; upstream it with `Roth.wronskianMatrix` over `[CommRing R]` under a non-clashing name (for example `Polynomial.wronskianDet`), with the `l = 2` bridge to `Polynomial.wronskian` and the `map` lemma.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.wronskian/weaken_and_relate.lean`, checked with `lean_diagnostic_messages`: clean, no errors or warnings. The first check had a header-linter warning and one error, because a probe `example` returning a noncomputable value needed `noncomputable`; both are fixed. The file verifies: (1) the `[CommRing R]` Wronskian elaborates (also at `ℤ[X]`), and `Roth.wronskian φ = Evidence.wronskian φ` holds by `rfl`; (2) `wronskian ![a, b] = Polynomial.wronskian a b` over any `CommRing`; (3) the `l = 0` value is `1` and the `l = 1` value is `φ 0`; (4) `map_wronskian`: the Wronskian commutes with `Polynomial.map f` for a ring hom `f`.
- Parent evidence reused: `.mathlib-quality/overview/evidence/Roth.wronskianMatrix/weaken_and_relate.lean` (semiring matrix, `Type 1` probe).
- Mathlib greps: case-insensitive `wronsk` (3 files, all 2-ary), `def .*[wW]ronsk` (2 defs). The TODO is at `Mathlib/RingTheory/Polynomial/Wronskian.lean` l.27–29.
- Lean-Finder and LeanSearch returned only the 2-ary family. Loogle `Matrix.det, Polynomial.hasseDeriv` returned no hits. `lean_local_search` was unavailable (ripgrep missing), so grep replaced it.
- WebSearch: 4 queries, summarised in the literature table. ChatGPT MCP: n/a (not configured).
- Project grep `grep -rnw wronskian Roth/` produced the call-sites table.
