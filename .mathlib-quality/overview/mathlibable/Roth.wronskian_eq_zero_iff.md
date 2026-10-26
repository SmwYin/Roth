---
decl: Roth.wronskian_eq_zero_iff
file: Roth/Wronskian.lean
line: 219
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The n-ary Wronskian criterion (Wronskian vanishes iff the family is dependent, char 0) is absent from mathlib (n-ary Wronskian is a TODO in Mathlib/RingTheory/Polynomial/Wronskian.lean); [Field K] weakens to [CommRing R] [IsDomain R] [CharZero R] (verified), and both CharZero (ZMod 2) and IsDomain (QxQ) are necessary (verified counterexamples).
action: Ship as the headline theorem of the n-ary Wronskian PR to Mathlib/RingTheory/Polynomial/Wronskian.lean over [CommRing R] [IsDomain R] [CharZero R], adding the companion wronskian_ne_zero_iff (W ne 0 iff LinearIndependent); locally keep (no project call sites, it is the module's stated main result).
---

# Roth.wronskian_eq_zero_iff

## Inventory entry

### `theorem Roth.wronskian_eq_zero_iff`
- **Type**: `∀ {K : Type*} [Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]}, wronskian φ = 0 ↔ ¬ LinearIndependent K φ`
- **What**: In characteristic zero, the (Hasse) Wronskian `det (D^{(μ)} φ_ν)` of a family of `l` polynomials is zero iff the family is linearly dependent over `K`.
- **How**: Term-mode `Iff.intro`: forward direction is `imp_not_comm.mp wronskian_ne_zero_of_linearIndependent`, backward direction is `wronskian_eq_zero_of_not_linearIndependent`.
- **Hypotheses**: `[Field K]` (section variable), `[CharZero K]`.
- **Uses from project**: `Roth.wronskian`, `Roth.wronskian_ne_zero_of_linearIndependent`, `Roth.wronskian_eq_zero_of_not_linearIndependent`
- **Used by**: unused in project (`grep -rn wronskian_eq_zero_iff Roth/ Roth.lean`: only the module docstring l.32 and the declaration l.219; call sites use the two directional lemmas directly)
- **Visibility**: public
- **Lines**: 219–223, proof length 3 lines
- **Notes**: Listed under `## Main results` of the module docstring; it is the source statement (clean.tex §2, first lemma, l.166).

## Junk check (Step 8)
- Used anywhere? No project call sites; consumers apply the two directional lemmas (`wronskian_ne_zero_of_linearIndependent` at GenWronskian.lean:262 and Separation.lean:534).
- Wrapper of 1–2 mathlib calls? It is the pairing of two project lemmas with `imp_not_comm` (mathlib logic glue). It is not a wrapper of mathlib content.
- Does mathlib have it? No. Mathlib has only the 2-ary `Polynomial.wronskian` and `IsCoprime.wronskian_eq_zero_iff` (2-ary, coprime, derivatives), no n-ary Wronskian (TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean` l.27–29).
- Too specific (inline?)? No: it is the named criterion and the declared main result of the file. Iff forms are conventional mathlib API even when call sites use the directions.
- Well-chosen? Yes, modulo `[Field K]` being stronger than needed and the orientation (see Phase 5.5).
- Conclusion: `KEEP`. Action: keep as the headline iff; generalise when upstreaming.

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.wronskian_eq_zero_iff` absent from mathlib (only `IsCoprime.wronskian_eq_zero_iff` in a different namespace with a different statement: MAYBE-COLLISION on bare name, resolved below). The body is an `Iff` assembly of two theorems, not `rfl`/`Iff.rfl`/unfolding of a def, so it is not a glue lemma in the inheritance sense; full workflow run. It reuses the sibling assessments `Roth.wronskian_ne_zero_of_linearIndependent` and `Roth.wronskian_eq_zero_of_not_linearIndependent` (both YES-but-generalise-first) and their evidence.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the evidence file importing `Roth.Wronskian` elaborates in the LSP with no errors)
- decl `Roth.wronskian_eq_zero_iff`: resolved at Roth/Wronskian.lean:219
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Wronskians of finitely many univariate polynomials (Hasse `l × l` determinant) and the linear-independence criterion in characteristic zero.

### Statement (Phase 1)

`Roth.wronskian_eq_zero_iff` is a theorem stating: let `K` be a field of characteristic zero and `φ_0, …, φ_{l−1} ∈ K[t]`. Then the Hasse Wronskian `W = det (D^{(μ)} φ_ν)_{0 ≤ μ, ν < l}`, with `D^{(μ)} = (1/μ!) d^μ/dt^μ`, is the zero polynomial if and only if there are constants `c_ν ∈ K`, not all zero, with `∑ c_ν φ_ν = 0`.

Variables / typeclasses involved (Lean side):
- `K` with `[Field K] [CharZero K]`: the coefficient field.
- `l : ℕ`, `φ : Fin l → K[X]`: the family.

Hypotheses (Lean side):
- none besides the typeclasses.

Conclusion (math): `W(φ_0, …, φ_{l−1}) = 0 ⇔ φ_0, …, φ_{l−1}` are `K`-linearly dependent.

Conclusion (Lean): `wronskian φ = 0 ↔ ¬ LinearIndependent K φ`.

### Size classification (Phase 2a)

Verdict: BIG
Reason: it is the main result listed under `## Main results` of Roth/Wronskian.lean and the classical (named) Wronskian criterion.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 2 (term-mode pair)
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Wronskian vanishes if and only if polynomials linearly dependent characteristic zero | yes | arXiv 2602.20832 (2026): polynomials over a field of char 0 (or char p > max degree) are dependent iff Wronskian identically zero, proved by reduction to distinct degrees and leading terms; Bostan–Dumas arXiv 1301.6598; Wikipedia "Wronskian" | exactly our statement and our proof strategy |
| 2 | WebSearch (general form) | Wronskian criterion linear dependence formal power series integral domain Bostan Dumas theorem | yes | Bostan–Dumas (Amer. Math. Monthly 2010): power series / rational functions over a char-0 field; Ball–Parks–Pong arXiv 1611.00248: several variables, fraction fields | most general standard form is power series over a char-0 field; no source states an integral-domain version explicitly (it follows via the fraction field) |
| 3 | WebSearch (named-after / aliases) | Hasse Wronskian linear independence positive characteristic Garcia Voloch counterexample x^p | yes | Garcia–Voloch (1987) / Wang (1999): in char p, independence iff some Hasse-Wronskian with gap orders `0 = ε_1 < … < ε_n < p^s` is nonzero; `1, x^p` is the standard counterexample for fixed orders | confirms CharZero is needed for the fixed-order iff |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex`, grep "if and only if they are linearly" | yes | l.166: "the Wronskian vanishes if and only if they are linearly dependent" (rational coefficients) | the exact source statement (over ℚ) |
| 6 | nLab | Wronskian | n/a | — | no nLab entry for the Wronskian criterion; not a categorical concept |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | Stacks does not treat Wronskians of polynomials (not an algebraic-geometry construction there) |
| 9 | MathOverflow / Math.SE | covered by WebSearch #1–#3 (no thread surfaced) | no | — | folklore textbook fact; Peano's `x^2, x|x|` is the standard warning that analyticity/algebraicity is essential |
| 10 | recent arXiv (last 5 years) | results of #1–#3 | yes | arXiv 2602.20832 (2026), 2410.18867 (2024), 2107.11266 (2021) | statement standard and actively used (PIT, Diophantine geometry) |

### Literature summary (Phase 3)

Concept identified as: the Wronskian criterion for linear independence (both directions), for polynomials / formal power series.
Sources agree on the standard form: yes. Over a field of characteristic zero, polynomials (more generally formal power series or rational functions) are linearly dependent iff their Wronskian vanishes; the dependent ⇒ zero direction holds over any domain.
Most general standard form: coefficients in a characteristic-zero field (equivalently, via the fraction field, a characteristic-zero domain), objects power series / rational functions. In char p the fixed-order iff fails; for polynomials it survives when p exceeds the maximal degree (arXiv 2602.20832), a different side condition.
Generality dimensions where the literature varies:
  - coefficients: ℚ / char-0 field / char-0 domain; char p > max degree for polynomials; general char p only with Garcia–Voloch orders.
  - objects: polynomials ⊂ rational functions ⊂ power series; several variables via generalized Wronskians.
Disagreement with the literature: none (Hasse normalisation differs from the classical Wronskian by the factor `∏ μ!`, nonzero in char 0).

### Generality analysis — `Roth.wronskian_eq_zero_iff`

Literature-standard form (from Phase 3): char-0 field (or domain); `W = 0 ⇔` linearly dependent.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | `[CommRing R] [IsDomain R]` | yes | Verified: `Evidence.wronskian_eq_zero_iff` over `[CommRing R] [IsDomain R] [CharZero R]`, combining the domain form of the easy direction (proof verbatim) and the fraction-field transfer of the hard direction; instantiated over ℤ |
| 2 | `[IsDomain R]` (in the weakened form) | — | domain | no | Verified counterexample with `CharZero`: over `ℚ × ℚ`, `![C (1,0)]` is dependent but has Wronskian `C (1,0) ≠ 0` |
| 3 | `[CharZero K]` | char 0 | char 0 | no | Verified counterexample: `![1, X^2]` over `ZMod 2` is independent with zero Wronskian, so the iff is false |
| 4 | objects `K[X]` | polynomials | power series | yes in principle (not proposed) | needs a `PowerSeries` Hasse-derivative API; out of scope, mathlib's 2-ary Wronskian is also polynomial |
| 5 | char p > max degree variant | — | arXiv 2602.20832 | different statement | would add a degree side-condition hypothesis; not a weakening of this iff, possible follow-up |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (`Field` → `CommRing` + `IsDomain`, keeping `CharZero`), verified clean with `lean_diagnostic_messages` (evidence (1), (1'), (2)); both remaining hypotheses shown necessary (evidence (3), (4)).
Proposed restatement:

```lean
theorem wronskian_eq_zero_iff {R : Type*} [CommRing R] [IsDomain R] [CharZero R]
    {l : ℕ} {φ : Fin l → R[X]} : wronskian φ = 0 ↔ ¬ LinearIndependent R φ
```
Cost of restatement: CHEAP (the same two-term pairing of the generalised directions; verified).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no bundled preamble |
| 2 | sequences to filters? | no | — | algebraic statement, no topology |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | no | — | `LinearIndependent` is the mathlib idiom |
| 5 | field-specific to (semi)ring? | yes | `[CommRing R] [IsDomain R] [CharZero R]` (4b row 1) | ℤ[X] families directly, same setting as `Algebra.discr_zero_of_not_linearIndependent` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | `Fin l` indexes derivative orders |
| 8 | concrete-via-abstract? | no | — | statement names no concrete object; proof is pure pairing |
| 9 | false-generalisation guard | checked, no false generalisation | the domain form specialises to the field form (evidence (2)); `LinearIndependent R` over a domain is the standard notion; dropping `IsDomain` or `CharZero` is false (evidence (3), (4)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the only change is the typeclass weakening already recorded in Phase 4b, plus the orientation choice handled in Phase 5.5.

### Proof strategy — `Roth.wronskian_eq_zero_iff`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | pairing of two directions | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | the n-ary Wronskian and both directions (sibling reports) are missing; they ship in the same PR | CHEAP, same PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (`⟨imp_not_comm.mp _, _⟩` is the standard way to assemble an iff from the two directions).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.wronskian_eq_zero_iff`

[A] Lean-Finder       "determinant of the matrix of derivatives of a family of polynomials vanishes iff the family is linearly dependent in characteristic zero"   hits: `Matrix.det_matrixOfPolynomials`, `Matrix.det_mvPolynomialX_ne_zero`, `Polynomial.sylvesterDeriv`, `Polynomial.wronskian_self_eq_zero`, `Polynomial.isAlt_wronskianBilin`; none is the criterion
[B] Loogle            `Polynomial.wronskian, LinearIndependent`   no hits
[C] LeanSearch        "Wronskian of polynomials is zero iff they are linearly dependent"   hits: `Polynomial.wronskian`, `wronskianBilin`, `wronskian_neg_left`, `wronskian_add_right`, `wronskian_neg_eq`; 2-ary API only
[D] Grep mathlib src  `wronskian_eq_zero_iff`, `wronskian_ne_zero_iff` (files: only `RingTheory/Polynomial/Wronskian.lean` (`IsCoprime.wronskian_eq_zero_iff`, 2-ary, coprime pair, about derivatives) and `NumberTheory/FLT/MasonStothers.lean` (its use)); `wronskian.*linearIndependent`: no hits
[E] Name pattern      `Roth.wronskian_eq_zero_iff`, `Polynomial.wronskian_eq_zero_iff`, `Polynomial.wronskian_ne_zero_iff`   absent (only `IsCoprime.wronskian_eq_zero_iff`, unrelated statement)

Searched for both the user's form (char-0 field) and the literature-standard form (char-0 domain / power series).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). The n-ary Wronskian is an explicit TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean`.

### Normal-form check — `Roth.wronskian_eq_zero_iff`

Equivalent formalisms:
- `wronskian φ = 0 ↔ ¬ LinearIndependent R φ` (current);
- `wronskian φ ≠ 0 ↔ LinearIndependent R φ`;
- the two implications (project lemmas).

Does mathlib already have a canonical form? No n-ary Wronskian. Mathlib convention for such criteria puts the canonical predicate on the RHS without negation where possible (e.g. `Matrix.det_vandermonde_ne_zero_iff : det ≠ 0 ↔ Injective v`). The `_eq_zero_iff` form is also standard and simp-usable on `W = 0` goals.
Proposed canonical form: ship both `wronskian_eq_zero_iff` (current orientation) and `wronskian_ne_zero_iff : wronskian φ ≠ 0 ↔ LinearIndependent R φ` (verified in evidence as a one-line corollary).
RHS convention respected? yes (`LinearIndependent` on the RHS in both).

### Syntactic generality — `Roth.wronskian_eq_zero_iff`

Alternative restatements attempted:
- domain form `[CommRing R] [IsDomain R] [CharZero R]` (compiles, evidence (1));
- `ne_zero_iff` orientation (compiles, evidence (1));
- dropping `CharZero` (refuted, evidence (3)); dropping `IsDomain` (refuted, evidence (4)).

Chosen restatement: the domain form, both orientations.
Justification: `_ne_zero_iff` with positive `LinearIndependent` is what applications want (prove independence from a nonzero Wronskian, or vice versa) without `not_not`.

### Superfluous-argument audit — `Roth.wronskian_eq_zero_iff`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `[CommRing R] [IsDomain R]` suffices (verified) |
| 2 | `[CharZero K]` | yes | ZMod 2 counterexample (verified) |
| 3 | (domain) | yes | ℚ × ℚ counterexample (verified) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (add the `ne_zero_iff` companion)
Syntactic generality: RESTATE (`[CommRing R] [IsDomain R] [CharZero R]`)
Superfluous arguments: 0 to drop (1 to weaken: `[Field K]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.wronskian_eq_zero_iff`

Internal use count: 0 (not counting the declaring file, which also has no use besides the docstring)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| (none) | `grep -rn wronskian_eq_zero_iff Roth/ Roth.lean`: only Roth/Wronskian.lean:32 (docstring) and :219 (declaration) |

Inline-derivation grep: `grep -rn "imp_not_comm\|wronskian_eq_zero_of_not_linearIndependent" Roth/`: the iff is not re-derived elsewhere; consumers (GenWronskian.lean:262, Separation.lean:534) use the hard direction directly. (none)

K = 0 with no re-derivation: per 6.0.1 this would suggest junk or genuinely-new; here it is the stated main result and the API iff of a criterion whose directions are both used, so it is API, not dead code.

### Composition check (Phase 6)

Can `Roth.wronskian_eq_zero_iff` be derived from mathlib in ≤3 chained calls?

Attempt 1: `IsCoprime.wronskian_eq_zero_iff`.
  - Mathlib decls used: `IsCoprime.wronskian_eq_zero_iff`
  - Result: fails. 2-ary only, needs coprimality, and characterises vanishing derivatives rather than linear dependence.

Attempt 2: `Matrix.exists_mulVec_eq_zero_iff` on the Hasse matrix.
  - Mathlib decls used: `Matrix.exists_mulVec_eq_zero_iff`
  - Result: partial. It gives the easy direction (the project proof of `wronskian_eq_zero_of_not_linearIndependent`), but for the hard direction a polynomial kernel vector must be turned into a constant relation, which is the content of the degree-reduction induction plus the distinct-degree leading-coefficient computation (`Roth.det_choose_eq`).

Conclusion: NOT-COMPOSABLE (from mathlib; within the proposed PR it is a two-term pairing of the two directions, which is exactly how mathlib states such iff lemmas)

## Verdict: `Roth.wronskian_eq_zero_iff`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the classical Wronskian criterion; char-0 field (Bostan–Dumas arXiv 1301.6598; arXiv 2602.20832 for polynomials with the same distinct-degree proof); source clean.tex l.166.
- Generality analysis (Phase 4): STRICTLY NARROWER; `Field` → `CommRing` + `IsDomain` + `CharZero` verified; `CharZero` and `IsDomain` each shown necessary by verified counterexamples.
- Mathlib search (Phase 5): not in mathlib; n-ary Wronskian is a TODO.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

`Mathlib/RingTheory/Polynomial/Wronskian.lean` defines only the Wronskian of two polynomials and lists "Define Wronskian for n-tuple of polynomials" as a TODO. The criterion "in characteristic zero a family of polynomials is linearly dependent iff its Wronskian vanishes" is the headline theorem that justifies the n-ary Wronskian (Roth's lemma, Schmidt subspace, generalized Mason–Stothers, polynomial identity testing). This iff is the statement users will search for; the two implications (sibling reports, YES-but-generalise-first) are its directions. Having no project call site is not an argument against it: project code applies the hard direction directly, but mathlib convention is to provide the iff alongside the implications.

The field hypothesis is stronger than needed: over a char-0 domain the easy direction holds verbatim and the hard direction transfers via the fraction field, so the iff holds over `[CommRing R] [IsDomain R] [CharZero R]` (verified, including over ℤ). The remaining hypotheses are sharp: `![1, X^2]` over `ZMod 2` breaks the iff without `CharZero`, and `![C (1,0)]` over `ℚ × ℚ` breaks it without `IsDomain` even in char 0 (both verified). The statement should also get the `ne_zero_iff` companion with positive `LinearIndependent` on the RHS.

Reason for the generalisation: LITERATURE-WEAKENING (`Field` → char-0 domain).
Proposed restatement:
```lean
theorem Polynomial.wronskianDet_eq_zero_iff {R : Type*} [CommRing R] [IsDomain R] [CharZero R]
    {l : ℕ} {φ : Fin l → R[X]} : wronskianDet φ = 0 ↔ ¬ LinearIndependent R φ :=
  ⟨imp_not_comm.mp wronskianDet_ne_zero_of_linearIndependent,
    wronskianDet_eq_zero_of_not_linearIndependent⟩

theorem Polynomial.wronskianDet_ne_zero_iff {R : Type*} [CommRing R] [IsDomain R] [CharZero R]
    {l : ℕ} {φ : Fin l → R[X]} : wronskianDet φ ≠ 0 ↔ LinearIndependent R φ := by
  rw [ne_eq, wronskianDet_eq_zero_iff, not_not]
```
(`wronskianDet` = placeholder n-ary name chosen when upstreaming the parent def `Roth.wronskian`; both proofs verified in evidence under the name `Evidence.wronskian`.)
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
- closes the TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean` with its main theorem;
- linear independence of integer/rational polynomial families decided by a determinant computation;
- several-variable generalized Wronskian criteria via Kronecker substitution (Roth/GenWronskian.lean).
PR grouping: the n-ary Wronskian PR with `Roth.wronskianMatrix`, `Roth.wronskian`, `Roth.wronskian_eq_zero_of_not_linearIndependent`, `Roth.coeff_wronskian_of_natDegree_injective`, `Roth.wronskian_ne_zero_of_natDegree_injective`, `Roth.wronskian_update_sub_smul`, `Roth.linearIndependent_update_sub_smul`, `Roth.wronskian_ne_zero_of_linearIndependent`; depends on the Vandermonde/binomial-determinant PR (`Roth.det_choose_eq`).
Next action: run `/generalise Roth.wronskian_eq_zero_iff` targeting `[CommRing R] [IsDomain R] [CharZero R]` (after the two directional lemmas are generalised), add `wronskian_ne_zero_iff`, then include both in the n-ary Wronskian PR to `Mathlib/RingTheory/Polynomial/Wronskian.lean`.

---

## Next step

Generalise to a characteristic-zero commutative domain (verified), add the `ne_zero_iff` companion, and ship as the headline theorem of the n-ary Wronskian PR to `Mathlib/RingTheory/Polynomial/Wronskian.lean`. Locally keep (no call sites; it is the file's stated main result).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.wronskian_eq_zero_iff/weaken_domain_iff.lean` (imports `Roth.Wronskian`, `Mathlib.RingTheory.Localization.Module`, `Mathlib.RingTheory.Localization.FractionRing`, `Mathlib.Algebra.Field.ZMod`, `Mathlib.Algebra.CharP.Algebra`). Checked with `lean_diagnostic_messages`: no errors; only a flexible-`simp` linter warning in the ZMod 2 computation. It proves:
  - (1) `Evidence.wronskian_eq_zero_iff` and `Evidence.wronskian_ne_zero_iff` over `[CommRing R] [IsDomain R] [CharZero R]` (from the domain forms of both directions, copied from the sibling evidence files), with (1') an instance over ℤ;
  - (2) the project statement as the field specialisation;
  - (3) the iff fails over `ZMod 2` for `![1, X^2]` (so `CharZero` is needed);
  - (4) over `ℚ × ℚ`, `![C (1,0)]` is dependent with nonzero Wronskian (so `IsDomain` is needed even in char 0).
- Mathlib grep `wronskian_eq_zero_iff`, `wronskian_ne_zero_iff`, `wronskian.*linearIndependent`; read TODO at `Mathlib/RingTheory/Polynomial/Wronskian.lean` l.27–29.
- LeanSearch, Lean-Finder, Loogle as in Phase 5 (Loogle: no hits).
- WebSearch: 3 queries (Phase 3 table). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn wronskian_eq_zero_iff Roth/ Roth.lean`: l.32 (docstring), l.219 (decl) only.
