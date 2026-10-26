---
decl: Roth.wronskian_ne_zero_of_linearIndependent
file: Roth/Wronskian.lean
line: 205
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The hard direction of the n-ary Wronskian criterion (linearly independent polynomials have nonzero Wronskian in char 0, Bostan-Dumas Thm 2) is absent from mathlib, which only has the 2-ary Wronskian; [Field K] weakens to [CommRing R] [IsDomain R] [CharZero R] via the fraction field (verified), and CharZero is necessary (ZMod 2 counterexample verified).
action: Upstream with the n-ary Wronskian PR to Mathlib/RingTheory/Polynomial/Wronskian.lean over [CommRing R] [IsDomain R] [CharZero R] (field case as now, domain case by fraction-field transfer as in evidence), together with the iff form; locally keep (call sites Roth/Wronskian.lean:221, Roth/GenWronskian.lean:262, Roth/Separation.lean:534).
---

# Roth.wronskian_ne_zero_of_linearIndependent

## Inventory entry

### `theorem Roth.wronskian_ne_zero_of_linearIndependent`
- **Type**: `∀ {K : Type*} [Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]}, LinearIndependent K φ → wronskian φ ≠ 0`
- **What**: In characteristic zero, a linearly independent family `φ_0, …, φ_{l−1}` of univariate polynomials has nonzero (Hasse) Wronskian `det (D^{(μ)} φ_ν)`.
- **How**: Strong induction (`Nat.strong_induction_on`) on the total degree `∑ ν, natDegree (φ ν)`. If the degrees are pairwise distinct, conclude by `wronskian_ne_zero_of_natDegree_injective` (with `LinearIndependent.ne_zero`). Otherwise pick `ν ≠ ν'` of equal degree (`Function.not_injective_iff`), replace `φ ν'` by `φ ν' − (lc φ ν' / lc φ ν) φ ν`. This leaves the Wronskian unchanged (`wronskian_update_sub_smul`), keeps the family independent (`linearIndependent_update_sub_smul`) and strictly lowers the total degree (`sum_natDegree_update_lt`), so the induction hypothesis applies.
- **Hypotheses**: `[Field K]` (section variable), `[CharZero K]`, `h : LinearIndependent K φ`.
- **Uses from project**: `Roth.wronskian`, `Roth.wronskian_ne_zero_of_natDegree_injective`, `Roth.wronskian_update_sub_smul`, `Roth.linearIndependent_update_sub_smul`, `Roth.sum_natDegree_update_lt`
- **Used by**: Roth/Wronskian.lean:221 (`wronskian_eq_zero_iff`, forward direction); Roth/GenWronskian.lean:262 (`exists_genWronskian_ne_zero`, applied to the Kronecker-substituted family); Roth/Separation.lean:534 (the separated representation of the main induction).
- **Visibility**: public
- **Lines**: 205–214, proof length 8 lines
- **Notes**: This is the hard direction of §2, first lemma of the source. The iff form `wronskian_eq_zero_iff` sits next to it.

## Junk check (Step 8)
- Used anywhere? Yes: 3 call sites in 3 files (Wronskian, GenWronskian, Separation).
- Wrapper of 1–2 mathlib calls? No: an 8-line strong induction over four project lemmas.
- Does mathlib have it? No. Mathlib has only the 2-ary `Polynomial.wronskian` and `IsCoprime.wronskian_eq_zero_iff`; there is no n-ary Wronskian and no linear-independence criterion (LeanSearch, Loogle `LinearIndependent, Polynomial.wronskian`: no hits).
- Too specific (inline?)? No: it is the classical named criterion and is used across files.
- Well-chosen? Yes. `[Field K]` is stronger than needed (see Phase 4).
- Conclusion: `KEEP`. Action: keep; generalise when upstreaming.

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring not internal/auxiliary; Step 8 KEEP; the qualified name is absent from mathlib (grep `wronskian_ne_zero`, `wronskian.*linearIndependent` over `.lake/packages/mathlib/Mathlib/`: no hits). It is not a glue lemma, so the full workflow is run. It reuses the parent assessments `Roth.wronskian` and `Roth.wronskian_ne_zero_of_natDegree_injective`, both YES-but-generalise-first.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the evidence file importing `Roth.Wronskian` elaborates in the LSP with no errors)
- decl `Roth.wronskian_ne_zero_of_linearIndependent`: resolved at Roth/Wronskian.lean:205
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Wronskians of finitely many univariate polynomials (Hasse `l × l` determinant) and the linear-independence criterion in characteristic zero.

### Statement (Phase 1)

`Roth.wronskian_ne_zero_of_linearIndependent` is a theorem stating: let `K` be a field of characteristic zero and `φ_0, …, φ_{l−1} ∈ K[t]` polynomials that are linearly independent over `K`. Then the Hasse Wronskian `W = det (D^{(μ)} φ_ν)_{0 ≤ μ, ν < l}` is not the zero polynomial. Here `D^{(μ)} = (1/μ!) d^μ/dt^μ`.

Variables / typeclasses involved (Lean side):
- `K` with `[Field K] [CharZero K]`: the coefficient field.
- `l : ℕ`, `φ : Fin l → K[X]`: the family.

Hypotheses (Lean side):
- `h : LinearIndependent K φ`

Conclusion (math): `W(φ_0, …, φ_{l−1}) ≠ 0`.

Conclusion (Lean): `wronskian φ ≠ 0`.

### Size classification (Phase 2a)

Verdict: SMALL (borderline BIG)
Reason: one direction of the classical Wronskian criterion. The iff `wronskian_eq_zero_iff` is the main result listed in the module docstring, and this lemma is its content.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 8
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Wronskian nonzero if and only if polynomials linearly independent characteristic zero proof | yes | Bostan–Dumas, "Wronskians and linear independence" (Amer. Math. Monthly 2010, arXiv 1301.6598), Thm 2: over a char-0 field, formal power series (or rational functions) with zero Wronskian are linearly dependent; for polynomials they cite an earlier Thm 4.7(a) | exactly our statement, more general (power series) |
| 2 | WebSearch (general form) | Wronskian linear independence integral domain characteristic zero power series Bostan Dumas | yes | same Thm 2; arXiv 1611.00248 (Wronskians and linear dependence of formal power series) gives several-variable / fraction-field versions; Bôcher: fails for C^∞ functions | the coefficient domain can be a char-0 domain via the fraction field; analyticity/formality is essential |
| 3 | WebSearch (named-after / aliases) | Hasse Wronskian generalized Wronskian criterion linear independence positive characteristic Garcia Voloch | yes | Garcia–Voloch (1987) and Wang (1999): in char p, independence is detected by a Hasse-derivative determinant with suitable (gap) orders, not the fixed orders `0..l−1` | char-0 is needed for the fixed-order statement (`1, x^p` counterexample, Wikipedia "Wronskian") |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §2 l.157–202 | yes | "the Wronskian vanishes if and only if they are linearly dependent" (l.166), proof of the converse l.174–194 by column operations reducing to distinct degrees | the exact source statement and proof strategy (over ℚ) |
| 6 | nLab | Wronskian | n/a | — | no nLab entry for the Wronskian criterion; not a categorical concept |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | Stacks does not treat Wronskians of polynomials |
| 9 | MathOverflow / Math.SE | covered by WebSearch #1–#3 (no thread surfaced in results) | no | — | folklore; standard textbook fact (ODE / Diophantine approximation, e.g. Roth's theorem expositions) |
| 10 | recent arXiv (last 5 years) | results of #1–#3 | yes | arXiv 2410.18867 (2024), 2107.11266 (2021), 2502.00731 (2025, subspace theorem notes) | statement is standard and in active use |

### Literature summary (Phase 3)

Concept identified as: the Wronskian criterion for linear independence (hard direction: independent ⇒ Wronskian ≠ 0), for polynomials / formal power series.
Sources agree on the standard form: yes. Over a field of characteristic zero, polynomials (more generally formal power series or rational functions) are linearly independent iff their Wronskian is nonzero.
Most general standard form: coefficients in a characteristic-zero field, objects formal power series or rational functions. By passing to the fraction field the same holds over any characteristic-zero integral domain. In char p one needs Hasse derivatives with other orders (Garcia–Voloch), which is a different statement.
Generality dimensions where the literature varies:
  - coefficients: ℚ / char-0 field / char-0 domain (via fraction field); char p only with modified orders.
  - objects: polynomials ⊂ rational functions ⊂ power series (and analytic functions); several variables via generalized Wronskians.
Disagreement with the literature: none (the Hasse normalisation differs from the classical one by the nonzero factor `∏ μ!` in char 0).

### Generality analysis — `Roth.wronskian_ne_zero_of_linearIndependent`

Literature-standard form (from Phase 3): char-0 field (or domain), polynomials/power series, independent ⇒ `W ≠ 0`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | `[CommRing R] [IsDomain R]` | yes | Verified: `Evidence.wronskian_ne_zero_of_linearIndependent` over `[CommRing R] [IsDomain R] [CharZero R]`. It passes to `FractionRing R` (`LinearIndependent.iff_fractionRing`, `Polynomial.map_injective`, `charZero_of_injective_algebraMap`, Wronskian commutes with `map`) and applies the field statement. Also checked over ℤ |
| 2 | `[CharZero K]` | char 0 | char 0 | no | Verified counterexample: `![1, X^2]` is linearly independent over `ZMod 2` but `Roth.wronskian` of it is 0 |
| 3 | `h : LinearIndependent K φ` | independence over the coefficient ring | same | no | it is the hypothesis of the criterion; the converse direction already holds (`wronskian_eq_zero_of_not_linearIndependent`) |
| 4 | objects `K[X]` | polynomials | power series | yes in principle (not proposed) | the n-ary Wronskian in mathlib would be stated for polynomials (as the 2-ary one is); power series need a separate `PowerSeries` Hasse-derivative API, so this is out of scope for this lemma |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (`Field` → `CommRing` + `IsDomain`, keeping `CharZero`). It was verified clean with `lean_diagnostic_messages`, and the project statement is recovered as the field specialisation (verified).
Proposed restatement:

```lean
theorem wronskian_ne_zero_of_linearIndependent {R : Type*} [CommRing R] [IsDomain R]
    [CharZero R] {l : ℕ} {φ : Fin l → R[X]} (h : LinearIndependent R φ) : wronskian φ ≠ 0
```
Cost of restatement: CHEAP. The field case keeps the current proof; the domain case is a 10-line fraction-field transfer (evidence). The alternative is to rerun the induction over the domain with the column operation `lc φ ν • φ ν' − lc φ ν' • φ ν`, which scales the Wronskian by the nonzero `lc φ ν`.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no bundled preamble |
| 2 | sequences to filters? | no | — | algebraic statement, no topology |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | no | — | `LinearIndependent` is already the mathlib idiom |
| 5 | field-specific to (semi)ring? | yes | `[CommRing R] [IsDomain R] [CharZero R]` (Phase 4b row 1) | ℤ[X] families directly; matches `Algebra.discr_zero_of_not_linearIndependent`'s domain setting |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | `Fin l` indexes derivative orders, so it must be `Fin l` (or a `Fintype` with an equivalence) |
| 8 | concrete-via-abstract? | no | — | the statement names no concrete object |
| 9 | false-generalisation guard | checked | the domain form is the same statement (the field case is a special case, and `LinearIndependent R` over a domain is the standard notion); dropping `CharZero` is false (ZMod 2) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the only change is the typeclass weakening already recorded in Phase 4b; the iff form `wronskian_eq_zero_iff` is the natural companion.

### Proof strategy — `Roth.wronskian_ne_zero_of_linearIndependent`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | partly | a point-free proof: take a basis of `span K (range φ)` with distinct degrees (echelon form), then use `det` multiplicativity under the change of basis. The current induction on column operations is a hands-on version of this | MODERATE; the current proof is short and clear |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | the n-ary Wronskian with its column-operation invariance (`wronskian_update_sub_smul`, from `Matrix.det_updateCol_add_smul_self`) and the distinct-degree base case are missing from mathlib (sibling reports) | CHEAP, same PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. It follows the source (clean.tex l.174–194) and is 8 lines given the helpers. Upstream, the domain case should be derived from the field case via the fraction field (evidence) rather than redoing the induction.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.wronskian_ne_zero_of_linearIndependent`

[A] Lean-Finder       "linearly independent family of polynomials over a characteristic zero field has nonzero determinant of matrix of derivatives"   hits: `Matrix.det_mvPolynomialX_ne_zero`, `Matrix.det_matrixOfPolynomials`, `Algebra.discr_zero_of_not_linearIndependent`, `Matrix.det_vandermonde_ne_zero_iff`, submersive-presentation Jacobian lemmas; none is a Wronskian criterion
[B] Loogle            `LinearIndependent, Polynomial.wronskian`   no hits
[C] LeanSearch        "Wronskian of linearly independent polynomials is nonzero"   hits: 2-ary `Polynomial.wronskian`, `IsCoprime.wronskian_eq_zero_iff`, `wronskianBilin`, `wronskian_eq_of_sum_zero`, `wronskian_add_*`; only 2-ary API, no linear-independence statement
[D] Grep mathlib src  `wronskian_ne_zero`, `wronskian.*linearIndependent`, `linearIndependent.*wronskian`; files containing both `hasseDeriv` and `det`   no hits
[E] Name pattern      `Roth.wronskian_ne_zero_of_linearIndependent`, `Polynomial.wronskian_ne_zero*`, `Polynomial.wronskian_eq_zero_iff*`   absent (only `IsCoprime.wronskian_eq_zero_iff`, about two coprime polynomials and derivatives)

Searched for both the user's form (char-0 field) and the literature-standard form (char-0 domain / power series).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Mathlib has no n-ary Wronskian; it is a TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean`.

### Normal-form check — `Roth.wronskian_ne_zero_of_linearIndependent`

Equivalent formalisms:
- `LinearIndependent K φ → wronskian φ ≠ 0` (current);
- `wronskian φ = 0 ↔ ¬ LinearIndependent K φ` (project `wronskian_eq_zero_iff`);
- `wronskian φ ≠ 0 ↔ LinearIndependent K φ`.

Does mathlib already have a canonical form? No (no n-ary Wronskian). The analogous mathlib pattern is `Algebra.discr_zero_of_not_linearIndependent` (an implication), with iff forms stated separately.
Proposed canonical form: keep the implication (it is what call sites apply) plus the iff `wronskian_ne_zero_iff : wronskian φ ≠ 0 ↔ LinearIndependent R φ`, with `LinearIndependent` on the RHS.
RHS convention respected? yes for the proposed iff; the project's `wronskian_eq_zero_iff` has `¬ LinearIndependent` on the RHS, which is also acceptable.

### Syntactic generality — `Roth.wronskian_ne_zero_of_linearIndependent`

Alternative restatements attempted:
- over `[CommRing R] [IsDomain R] [CharZero R]` (compiles, evidence (1), also over ℤ (1'));
- dropping `CharZero` (refuted, evidence (3));
- iff form (already in the project as `wronskian_eq_zero_iff`).

Chosen restatement: the domain form, as an implication with `h` explicit.
Justification: all 3 call sites pass a `LinearIndependent` proof directly; they are recovered by specialisation (evidence (2)).

### Superfluous-argument audit — `Roth.wronskian_ne_zero_of_linearIndependent`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `[CommRing R] [IsDomain R]` suffices (verified) |
| 2 | `[CharZero K]` | yes | counterexample `![1, X^2]` over `ZMod 2` (verified) |
| 3 | `h` | yes | the hypothesis of the criterion |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (`[CommRing R] [IsDomain R] [CharZero R]`)
Superfluous arguments: 0 to drop (1 to weaken: `[Field K]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.wronskian_ne_zero_of_linearIndependent`

Internal use count: 2 outside the declaring file (plus 1 inside it).
External-to-file callers: 2 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Wronskian.lean:221 | `⟨imp_not_comm.mp wronskian_ne_zero_of_linearIndependent, ...⟩` (`wronskian_eq_zero_iff`) |
| Roth/GenWronskian.lean:262 | `apply wronskian_ne_zero_of_linearIndependent (linearIndependent_kronecker ...)` (`exists_genWronskian_ne_zero`) |
| Roth/Separation.lean:534 | `exact ⟨l, hl1, hl2, D, hD, _, _, hG, wronskian_ne_zero_of_linearIndependent hφ, hFmap⟩` |

Inline-derivation grep: `grep -rn "wronskian_eq_zero_iff\|wronskian_ne_zero_of_natDegree_injective\|sum_natDegree_update_lt" Roth/`. The degree-reduction induction appears only here; no other file re-derives it. (none)

### Composition check (Phase 6)

Can `Roth.wronskian_ne_zero_of_linearIndependent` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Polynomial.wronskian` (2-ary) + `IsCoprime.wronskian_eq_zero_iff`.
  - Mathlib decls used: `IsCoprime.wronskian_eq_zero_iff`
  - Result: fails. It is 2-ary only and needs coprimality, and it says nothing about families of size `l`.

Attempt 2: `Matrix.det_ne_zero_of_...` / `Matrix.exists_mulVec_eq_zero_iff` on the Hasse matrix.
  - Mathlib decls used: `Matrix.exists_mulVec_eq_zero_iff`
  - Result: fails. A nonzero kernel vector over `K[X]` has polynomial, not constant, entries. Turning it into a constant relation is exactly the content of the criterion: either the degree induction plus the distinct-degree leading-term computation, or the ODE/power-series argument.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.wronskian_ne_zero_of_linearIndependent`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the classical Wronskian criterion. Bostan–Dumas Thm 2 (arXiv 1301.6598) covers char-0 power series; the source states it at clean.tex l.166/194. Char p needs the Garcia–Voloch modification.
- Generality analysis (Phase 4): STRICTLY NARROWER. `Field` → `CommRing` + `IsDomain` + `CharZero` is verified via the fraction field; `CharZero` is shown necessary by a verified counterexample.
- Mathlib search (Phase 5): not in mathlib (only the 2-ary Wronskian; n-ary is a TODO).
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

`Mathlib/RingTheory/Polynomial/Wronskian.lean` defines only the Wronskian of two polynomials, and its module docstring lists the general n-ary Wronskian as a TODO. The criterion "in characteristic zero, polynomials are linearly independent iff their Wronskian is nonzero" is the main reason anyone wants the n-ary Wronskian: Diophantine approximation (Roth, Schmidt subspace), abc/Mason–Stothers proofs in several variables, ODEs. This lemma is the hard direction. It completes the API proposed in the sibling reports (`Roth.wronskian`, `Roth.wronskian_eq_zero_of_not_linearIndependent`, `Roth.wronskian_ne_zero_of_natDegree_injective`, `Roth.wronskian_update_sub_smul`, `Roth.linearIndependent_update_sub_smul`, all YES-but-generalise-first). Without it the n-ary Wronskian PR would lack its headline theorem. The project uses it in 3 files.

The field hypothesis is stronger than needed. Over a characteristic-zero domain `R`, `LinearIndependent R φ` transfers to the fraction field (`LinearIndependent.iff_fractionRing` composed with the injective `Polynomial.mapAlg`). The Wronskian commutes with coefficient maps, and `Polynomial.map` along `R → Frac R` is injective, so the domain statement follows from the field one (verified in evidence, also instantiated over ℤ). `CharZero` cannot be dropped: `1, X^2` over `ZMod 2` is independent with zero Hasse Wronskian (verified). The power-series generalisation in the literature is out of scope for a polynomial Wronskian API and is not proposed.

Reason for the generalisation: LITERATURE-WEAKENING (`Field` → char-0 domain).
Proposed restatement:
```lean
theorem Polynomial.wronskian_ne_zero_of_linearIndependent {R : Type*} [CommRing R] [IsDomain R]
    [CharZero R] {l : ℕ} {φ : Fin l → R[X]} (h : LinearIndependent R φ) :
    wronskian φ ≠ 0 := by
  sorry -- proved in evidence (Evidence.wronskian_ne_zero_of_linearIndependent) from the field case

theorem Polynomial.wronskian_ne_zero_iff {R : Type*} [CommRing R] [IsDomain R] [CharZero R]
    {l : ℕ} {φ : Fin l → R[X]} : wronskian φ ≠ 0 ↔ LinearIndependent R φ := by
  sorry -- combine with the generalised wronskian_eq_zero_of_not_linearIndependent
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
- the full n-ary Wronskian criterion for linear independence (closing the TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean`);
- generalized-Wronskian (several-variable) criteria via Kronecker substitution, as in Roth/GenWronskian.lean;
- integral (ℤ[X]) applications without a manual pass to ℚ.
PR grouping: the n-ary Wronskian PR (with `Roth.wronskianMatrix`, `Roth.wronskian`, `Roth.wronskian_eq_zero_of_not_linearIndependent`, `Roth.coeff_wronskian_of_natDegree_injective`, `Roth.wronskian_ne_zero_of_natDegree_injective`, `Roth.wronskian_update_sub_smul`, `Roth.linearIndependent_update_sub_smul`, `Roth.wronskian_eq_zero_iff`). It depends on the Vandermonde/binomial-determinant PR (parent `Roth.det_choose_eq`).
Next action: run `/generalise Roth.wronskian_ne_zero_of_linearIndependent` targeting `[CommRing R] [IsDomain R] [CharZero R]` (keep the field proof, add the fraction-field transfer), then include it with the iff form in the n-ary Wronskian PR to `Mathlib/RingTheory/Polynomial/Wronskian.lean`.

---

## Next step

Generalise to a characteristic-zero commutative domain via the fraction field (verified), then upstream with the n-ary Wronskian and the iff form to `Mathlib/RingTheory/Polynomial/Wronskian.lean`. Locally keep (call sites Roth/Wronskian.lean:221, Roth/GenWronskian.lean:262, Roth/Separation.lean:534).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.wronskian_ne_zero_of_linearIndependent/weaken_domain.lean` (imports `Roth.Wronskian`, `Mathlib.RingTheory.Localization.Module`, `Mathlib.RingTheory.Localization.FractionRing`, `Mathlib.Algebra.Field.ZMod`, `Mathlib.Algebra.CharP.Algebra`). Checked with `lean_diagnostic_messages`: no errors; the only notes are flexible-`simp` linter warnings on the counterexample. It proves:
  - (1) `Evidence.wronskian_ne_zero_of_linearIndependent` over `[CommRing R] [IsDomain R] [CharZero R]` (fraction-field transfer plus `Roth.wronskian_ne_zero_of_linearIndependent`), with (1') an instance over ℤ.
  - (2) the project statement as the field specialisation.
  - (3) `LinearIndependent (ZMod 2) ![1, X ^ 2]` and `Roth.wronskian (K := ZMod 2) ![1, X ^ 2] = 0`, so `CharZero` is needed.

  The CommRing Wronskian and `map_wronskian` are copied from the `Roth.wronskian` evidence file.
- Mathlib grep `wronskian_ne_zero`, `wronskian.*linearIndependent`, `linearIndependent.*wronskian`, and files combining `hasseDeriv` with `det`: no hits.
- LeanSearch, Lean-Finder, Loogle as in Phase 5 (Loogle: no hits).
- WebSearch: 3 queries (Phase 3 table). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn wronskian_ne_zero_of_linearIndependent Roth/`: l.205 (decl), Roth/Wronskian.lean:221, Roth/GenWronskian.lean:262, Roth/Separation.lean:534.
