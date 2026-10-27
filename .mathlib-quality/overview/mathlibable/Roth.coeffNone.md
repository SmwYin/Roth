---
decl: Roth.coeffNone
file: Roth/Separation.lean
line: 80
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: coeffNone P ν is by definition (rfl) mathlib's idiom (optionEquivLeft R τ P).coeff ν, which mathlib uses unnamed everywhere with a full coefficient API (optionEquivLeft_coeff_coeff, mem_support_coeff_optionEquivLeft, natDegree_optionEquivLeft), so it is a harmless project-local abbreviation, not mathlib material.
action: Keep as a local abbreviation (no mathlib PR); re-aim downstream lemmas at optionEquivLeft - restate coeff_coeffNone (Separation.lean:85) with d.optionElim ν so it is optionEquivLeft_coeff_coeff, and treat degreeOf_coeffNone_le (Separation.lean:114) as the candidate mathlib lemma degreeOf_coeff_optionEquivLeft (Mathlib/Algebra/MvPolynomial/Equiv.lean, next to degreeOf_coeff_finSuccEquiv).
---

# Roth.coeffNone

## Inventory entry

### `def Roth.coeffNone`
- **Type**: `{τ : Type*} {R : Type*} [CommSemiring R] (P : MvPolynomial (Option τ) R) (ν : ℕ) : MvPolynomial τ R` (the section's `[Fintype τ] [DecidableEq τ]` are NOT included; checked with `#check`, evidence (0))
- **What**: The coefficient of `x_none^ν` in `P`, viewed as a polynomial in the remaining variables `τ`.
- **How**: `(optionEquivLeft R τ P).coeff ν` — transport along mathlib's `MvPolynomial.optionEquivLeft : MvPolynomial (Option τ) R ≃ₐ[R] (MvPolynomial τ R)[X]`, then `Polynomial.coeff`.
- **Hypotheses**: `[CommSemiring R]` only.
- **Uses from project**: `[]`
- **Used by**: all in Roth/Separation.lean: `coeff_coeffNone` (85–87), `eq_sum_X_none_pow_mul_coeffNone` (98–107), `degreeOf_coeffNone_le` (114–115), `coeff_rename_mul_aeval` (129, unfolds it), private `eq_sum_aeval_basis_coeffNone_aux` (265–275), private `exists_coeffNone_basis_aux` (291–297), and `exists_separated_representation`'s proof (332–342). No uses outside Separation.lean.
- **Visibility**: public
- **Lines**: 78–81, body 1 line
- **Notes**: Definitionally equal (`rfl`) to `(optionEquivLeft R τ P).coeff ν` (evidence (1)).

## Junk check (Step 8)
- Used anywhere? Yes, about 20 occurrences across 7 declarations in Separation.lean.
- Wrapper of 1–2 mathlib calls? Yes: `Polynomial.coeff ∘ MvPolynomial.optionEquivLeft`.
- Does mathlib have it? Not as a named def. Mathlib writes `(optionEquivLeft R σ p).coeff i` inline in Equiv.lean, Homogeneous.lean, SeparablyGenerated.lean, IsIntegral.lean and Nullstellensatz.lean, and has the coefficient API stated against that spelling.
- Too specific (inline)? Inlining is possible but costs readability in the long `Fin (n+1)` sums at 265–342. A local name keeps the source's "collect by powers of `x_p`" step readable.
- Well-chosen? Yes as a local abbreviation. The weakness is that its lemmas restate mathlib's API in non-canonical spellings (see re-aim below).
- Conclusion: `KEEP` — keep the def locally, but re-aim its lemmas at the `optionEquivLeft` API (see Next step).

## Mathlibable assessment (Step 9)

Pre-filter: not private; not `_aux`; docstring not internal/auxiliary; Step 8 = KEEP; qualified name `Roth.coeffNone` absent from mathlib (no `namespace Roth`, no `coeffNone` anywhere in `.lake/packages/mathlib/Mathlib/`). Not a glue lemma. Full workflow run.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` compiles)
- decl `Roth.coeffNone`:     resolved at Roth/Separation.lean:80
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`) in polynomials over `Option τ`, towards Lemma 2 of the source (`F = U(x_τ) V(x_none)`).

### Statement (Phase 1)

`Roth.coeffNone` is a definition of the following: given a polynomial `P ∈ R[x_τ, x_∗]` (variables `τ ⊔ {∗}`), write `P = ∑_ν φ_ν(x_τ) x_∗^ν` using the canonical isomorphism `R[x_τ, x_∗] ≅ R[x_τ][x_∗]`. Then `coeffNone P ν = φ_ν ∈ R[x_τ]`.

Variables / typeclasses involved (Lean side):
- `τ : Type*` — the non-distinguished variables; `none` is the distinguished variable `x_∗`.
- `R : Type*`, `[CommSemiring R]` — coefficients.
- `P : MvPolynomial (Option τ) R`, `ν : ℕ`.

Hypotheses (Lean side):
- none.

Conclusion (math): n/a — definition.

Conclusion (Lean): n/a — definition (body `(optionEquivLeft R τ P).coeff ν`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a named one-line composition of two mathlib operations; not a new structure and not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | no       | No proof depends on blocking an unfolding. Callers unfold it freely (`rw [coeffNone, ...]` at 87, 129), and `rfl` equals the mathlib idiom (evidence (1)). |
| Avoid typeclass diamonds         | no       | Takes only `[CommSemiring R]`, and the body is a plain function application. |
| Mark semantic intent / API name  | yes (project-local only) | Seven project declarations use the name, and it shortens the `Fin (n+1)` sums at 265–342. Mathlib has deliberately not named this. Its ~10 consumers write `(optionEquivLeft R σ p).coeff i` directly, and the analogous `finSuccEquiv` has no named coefficient def either. |

Conclusion: ONE-LINER WITH-EXEMPTION (project-local readability only; not a mathlib-level API exemption)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multivariate polynomial as polynomial in one variable with coefficients in polynomial ring R[x1..xn-1][xn] coefficient of x_n^k | yes | `P = ∑ φ_k(x') x_n^k`, coefficients in `R[x']` (SageMath Q&A; CGAL PolynomialTraits_d treats it as univariate over `R[x_0..x_{d-2}]`) | notation, not a named operation |
| 2 | WebSearch (general form) | isomorphism R[X_1,...,X_n] ≅ R[X_1,...,X_{n-1}][X_n] polynomial ring adjoining one variable coefficients | yes | `R[X_1..X_n] ≅ R[X_1..X_{n-1}][X_n]` via the universal property (Encyclopedia of Mathematics "Polynomial ring"; arXiv 2111.12195 defines the multivariate ring iteratively) | the content is the isomorphism; "coefficient" is then ordinary `Polynomial.coeff` |
| 3 | WebSearch (aliases / mathlib) | Mathlib MvPolynomial optionEquivLeft coeff finSuccEquiv coefficient polynomial | yes | mathlib `optionEquivLeft`, `finSuccEquiv` with coefficient lemmas (`finSuccEquiv_coeff_coeff`, `coeff_isHomogeneous_of_optionEquivLeft_symm`, `totalDegree_coeff_optionEquivLeft_add_le`) | no named coefficient-extraction def in any snapshot |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "powers of" | yes | line 374: "collecting the terms in terms of the powers of `x_p`" | the source uses the operation implicitly |
| 6 | nLab | polynomial ring | yes | polynomial algebra = free commutative algebra; `A[X ⊔ Y] ≅ A[X][Y]` by coproduct preservation | general form of the isomorphism only |
| 7 | nCatLab | free commutative algebra / coproduct | yes | same as #6 | no categorical content beyond #6 |
| 8 | Stacks Project | n/a | n/a | — | basic commutative algebra; Stacks only uses `R[x_1..x_n]` notationally, with no coefficient operation to compare |
| 9 | MathOverflow / Math.SE | (covered by #1/#2 results) | no | — | too elementary to be discussed as a result |
| 10 | recent arXiv | iterated polynomial ring definition (arXiv 2111.12195, surfaced by #2) | yes | `R[X_1..X_n] := R[X_1..X_{n-1}][X_n]` | confirms the operation is "coefficient after the iterated-ring identification" |

### Literature summary (Phase 3)

Concept identified as: the coefficient of `x_n^k` after identifying `R[x_1..x_n] ≅ R[x_1..x_{n-1}][x_n]`.
Sources agree on the standard form: yes. Everyone treats it as ordinary univariate coefficient extraction after the canonical isomorphism, never as a separately named operation.
Most general standard form: for any variable set `σ` and any commutative semiring `R`, `R[σ ⊔ {∗}] ≅ R[σ][X]`, followed by `coeff_k`.
Generality dimensions where the literature varies:
  - number of split variables: one (`Option`) to a block (`Sum`, mathlib `sumAlgEquiv`).
  - coefficient ring: commutative semiring is already most general here.
Disagreement with the literature: none. The project matches the standard form, and mathlib already packages the isomorphism as `optionEquivLeft`.

### Generality analysis — `Roth.coeffNone`

Literature-standard form (from Phase 3): `Polynomial.coeff (optionEquivLeft R σ P) k` for `[CommSemiring R]`, arbitrary `σ`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | `MvPolynomial` and `optionEquivLeft` need it |
| 2 | `τ : Type*` | arbitrary type | arbitrary type | no | already general; section `[Fintype τ] [DecidableEq τ]` are not included (evidence (0)) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0
Proposed restatement (if STRICTLY NARROWER): n/a
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | no bundled hypotheses | — |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | yes (already done) | the def is already "transport along the universal-property iso `optionEquivLeft`, then coeff" | the whole `optionEquivLeft` API |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field-specific to (semi)ring? | no | already `CommSemiring` | — |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general monoid? | no | `ℕ` exponent is intrinsic to `Polynomial.coeff` | — |
| 8 | Concrete-via-abstract? | no | no named concrete object | — |
| 9 | False-generalisation guard | no | no generalisation proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the body is already mathlib's modern idiom, `Polynomial.coeff ∘ optionEquivLeft`. The only "modernisation" left is to drop the name and use the idiom directly, which is a NO direction, not a YES.

### Proof strategy — `Roth.coeffNone`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | already via `optionEquivLeft` | — |
| 5 | missing mathlib helpers | yes (for downstream lemmas) | `degreeOf_coeff_optionEquivLeft : degreeOf j ((optionEquivLeft R σ p).coeff i) ≤ degreeOf (some j) p` is missing from mathlib, though the `finSuccEquiv` analogue `degreeOf_coeff_finSuccEquiv` exists (Equiv.lean:834). Compiles as a 2-line proof (evidence (3)). | CHEAP (a small mathlib PR candidate, to be assessed under `Roth.degreeOf_coeffNone_le`) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
  - (For the def itself. The downstream lemmas restate mathlib API in non-canonical spellings; see the re-aim section below.)

### Diamond / defeq risk — `Roth.coeffNone`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | The def introduces no instance. Its only instance argument is `[CommSemiring R]`, consumed by `optionEquivLeft`. |
| 2 | Reducibility leak | none | A plain (semireducible) `def`, not `@[reducible]`. `rfl` against the idiom works (evidence (1)), and callers must `rw [coeffNone]` explicitly to see the body. |
| 3 | Non-canonical unfolding | low | Mathlib's simp lemmas (`optionEquivLeft_coeff_coeff`, `mem_support_coeff_optionEquivLeft`) do not fire on `coeffNone P ν` until it is unfolded. That is why the project needs `coeff_coeffNone` and an explicit `rw [coeffNone]` at line 129. |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `τ`, `R` are independent `Type*` universes (evidence (0)) |
| 6 | Coercion ambiguity | none | no `CoeFun` / `CoeSort` |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none HIGH. Row 3 is the only friction: the name hides the mathlib API until unfolded.
Recommended mitigations (if HIGH): n/a

### Mathlib search-status: `Roth.coeffNone`

[A] Lean-Finder       "coefficient of a power of a distinguished variable in a multivariate polynomial, as a polynomial in the remaining variables"   hits: only `MvPolynomial.coeff_X_pow`, `coeff_mul_X` etc. (monomial-level); no named extraction def
[B] Loogle            `MvPolynomial (Option ?σ) ?R → ℕ → MvPolynomial ?σ ?R`   no hits (no def of this type in mathlib)
[C] LeanSearch        "coefficient of X none ^ n in MvPolynomial (Option σ) R as MvPolynomial σ R"   hits: `MvPolynomial.optionEquivLeft_coeff_some_coeff_none`, `MvPolynomial.optionEquivLeft_coeff_coeff`, `MvPolynomial.optionEquivLeft`
[D] Grep mathlib src  `coeffNone`, `def .*coeff.*Option`, `optionEquivLeft.*coeff`   no def. The idiom `(optionEquivLeft R σ p).coeff i` is used unnamed in Mathlib/Algebra/MvPolynomial/Equiv.lean (509 `optionEquivLeft_coeff_some_coeff_none`, 549 `mem_support_coeff_optionEquivLeft`, 553 `support_optionEquivLeft`, 578 `natDegree_optionEquivLeft`, 585/598 `totalDegree_coeff_optionEquivLeft_*`, 610 `optionEquivLeft_coeff_coeff`), RingTheory/MvPolynomial/Homogeneous.lean:359, FieldTheory/SeparablyGenerated.lean:109–117, RingTheory/Polynomial/IsIntegral.lean:245, Combinatorics/Nullstellensatz.lean:118–134, and the power-series analogue RingTheory/MvPowerSeries/Equiv.lean:131 `coeff_coeff_optionEquivLeft`
[E] Name pattern      grep / lean_local_search `coeffNone`, `coeff_none`, `optionEquivLeft_coeff`   only the theorems listed in [D]; no def

Searched for both:
  - the user's current form (a named def `MvPolynomial (Option τ) R → ℕ → MvPolynomial τ R`): absent as a def.
  - the literature-standard form (coefficient after `R[σ ⊔ ∗] ≅ R[σ][X]`): present as the unnamed composition `Polynomial.coeff (optionEquivLeft R σ P)` with full API.

Concluded: found building blocks (`MvPolynomial.optionEquivLeft`, `Polynomial.coeff`); composition yields our form definitionally.

### Normal-form check — `Roth.coeffNone`

Equivalent formalisms: (a) `coeffNone P ν`; (b) `(optionEquivLeft R τ P).coeff ν` (mathlib); (c) `(finSuccEquiv R n P).coeff ν` (only for `Fin (n+1)` variables).
Does mathlib already have a canonical form? yes — (b), with the API listed in Phase 5.
Is our def stated against the canonical form? Yes: its body is (b). Its lemmas are not: `coeff_coeffNone` uses `d.mapDomain some + Finsupp.single none ν` instead of mathlib's `d.optionElim ν`.
RHS convention respected? n/a for the def; for `coeff_coeffNone`, no (non-canonical RHS).

### Syntactic generality — `Roth.coeffNone`

Alternative restatements attempted:
- inline `(optionEquivLeft R τ P).coeff ν` everywhere: works by `rfl` (evidence (1)) but makes the `Fin (n+1)` sums at 265–342 longer.
- keep the name and add the `optionElim`-spelled coefficient lemma: it is literally `optionEquivLeft_coeff_coeff R P ν d` (evidence (2)).

Chosen restatement: keep the name locally; state its lemmas in mathlib's spellings.
Justification: the name helps project readability, and canonical-spelling lemmas let mathlib's API apply after a single `rw [coeffNone]`.

### Superfluous-argument audit — `Roth.coeffNone`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | needed by `MvPolynomial` / `optionEquivLeft` |
| 2 | section `[Fintype τ] [DecidableEq τ]` | n/a | not included in the def's signature (evidence (0)) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK for the def (its body is mathlib's canonical form). The downstream `coeff_coeffNone` needs REFACTOR to the `optionElim` spelling.
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally). Not a mathlib candidate.

### Call sites — `Roth.coeffNone`

Internal use count: 0 outside the declaring file; 7 declarations inside Roth/Separation.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:85–87 | `coeff_coeffNone`: `(coeffNone P ν).coeff d = P.coeff (d.mapDomain some + Finsupp.single none ν)` by `rw [coeffNone, optionEquivLeft_coeff_coeff]` + `ext`/`simp` |
| Roth/Separation.lean:98–107 | `eq_sum_X_none_pow_mul_coeffNone`: `P = ∑ ν ∈ range (n+1), X none ^ ν * rename some (coeffNone P ν)` |
| Roth/Separation.lean:114–115 | `degreeOf_coeffNone_le`: `degreeOf j (coeffNone P ν) ≤ degreeOf (some j) P` |
| Roth/Separation.lean:129 | `coeff_rename_mul_aeval`: `rw [← coeff_coeffNone, coeffNone, map_mul, ...]` |
| Roth/Separation.lean:265–275 | private `eq_sum_aeval_basis_coeffNone_aux`: hypothesis and span of `coeffNone P ν` |
| Roth/Separation.lean:291–297 | private `exists_coeffNone_basis_aux`: `let v := fun ν ↦ coeffNone P ν` |
| Roth/Separation.lean:332–342 | `exists_separated_representation` proof: `let v := ...coeffNone P ν`, `eq_sum_X_none_pow_mul_coeffNone P hn` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `coeffNone`?):
  - Roth/Separation.lean:65–75 private `coeff_X_none_pow_mul_rename` works directly with `optionEquivLeft R τ` and `optionEquivLeft_coeff_some_coeff_none`, i.e. the unnamed idiom.
  - Roth/Separation.lean:126–131 `coeff_rename_mul_aeval` unfolds `coeffNone` back to `optionEquivLeft` to apply mathlib lemmas.

### Composition check (Phase 6)

Can `Roth.coeffNone` be derived from mathlib in ≤3 chained calls?

Attempt 1: `fun P ν ↦ (optionEquivLeft R τ P).coeff ν`
  - Mathlib decls used: `MvPolynomial.optionEquivLeft`, `Polynomial.coeff`.
  - Result: succeeds; `rfl`-equal to the project def (evidence (1)).
  - Notes: 2 calls.

Re-aim consequences for the downstream `coeffNone` lemmas (all compiled in evidence):
  - `coeff_coeffNone` → stated with `d.optionElim ν` it is literally `MvPolynomial.optionEquivLeft_coeff_coeff R P ν d` (evidence (2)). Likely NO-mathlib-has-it.
  - `degreeOf_coeffNone_le` → re-aimed as `degreeOf_coeff_optionEquivLeft`, the missing `optionEquivLeft` twin of mathlib's `degreeOf_coeff_finSuccEquiv` (Equiv.lean:834); 2-line proof via `mem_support_coeff_optionEquivLeft` (evidence (3)). This is the one genuine small mathlib gap here and should get a full run re-aimed at `optionEquivLeft`.
  - `eq_sum_X_none_pow_mul_coeffNone` → `Polynomial.as_sum_range'` transported along `optionEquivLeft` with `natDegree_optionEquivLeft`, `optionEquivLeft_X_none` and `rename some ↦ C` (evidence (4)). Likely NO-composable.
  - `coeff_rename_mul_aeval` already unfolds to `optionEquivLeft` API and needs no change.

Conclusion: COMPOSABLE

## Verdict: `Roth.coeffNone`

Verdict: NO-composable-from-mathlib

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the operation is "take the `x_n^k` coefficient after `R[x', x_n] ≅ R[x'][x_n]`", which is universally notation rather than a named operation.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (`CommSemiring R`, arbitrary `τ`).
- Mathlib search (Phase 5): building blocks `MvPolynomial.optionEquivLeft` + `Polynomial.coeff`. Mathlib uses the unnamed composition with a full API.
- Composition check (Phase 6): COMPOSABLE (2 calls, `rfl`).

**Rationale:**
`coeffNone P ν` is definitionally `(optionEquivLeft R τ P).coeff ν` (evidence (1)). This exact composition is the spelling mathlib uses at every consumer: Equiv.lean, Homogeneous.lean, SeparablyGenerated.lean, IsIntegral.lean, Nullstellensatz.lean, and in the power-series analogue. Mathlib states its coefficient, support, degree and total-degree API against that spelling (`optionEquivLeft_coeff_coeff`, `optionEquivLeft_coeff_some_coeff_none`, `mem_support_coeff_optionEquivLeft`, `support_optionEquivLeft`, `natDegree_optionEquivLeft`, `totalDegree_coeff_optionEquivLeft_le`). The `finSuccEquiv` variant has no named coefficient def either. A named def in mathlib would duplicate that idiom and hide the API behind an unfold (risk row 3), so it is not mathlib material.

Inside the project the name is a reasonable readability abbreviation for the `Fin (n+1)` sums in `exists_separated_representation`, so Step 8 keeps it. The real follow-up is downstream. `coeff_coeffNone` restates `optionEquivLeft_coeff_coeff` in a non-canonical `mapDomain + single` spelling. `degreeOf_coeffNone_le` is the missing mathlib lemma `degreeOf_coeff_optionEquivLeft`, the twin of the existing `degreeOf_coeff_finSuccEquiv`, and is a small genuine upstream candidate.

WHY not: the def is a 2-call `rfl` composition of mathlib primitives that mathlib deliberately leaves unnamed.
Belongs-elsewhere check: keep as a project-local abbreviation in Roth/Separation.lean; nowhere else.
Mathlib building blocks: `MvPolynomial.optionEquivLeft` (Mathlib/Algebra/MvPolynomial/Equiv.lean:467), `Polynomial.coeff`; API `MvPolynomial.optionEquivLeft_coeff_coeff` (Equiv.lean:610), `MvPolynomial.optionEquivLeft_coeff_some_coeff_none` (Equiv.lean:509), `MvPolynomial.mem_support_coeff_optionEquivLeft` (Equiv.lean:549), `MvPolynomial.natDegree_optionEquivLeft` (Equiv.lean:578).
Composition sketch (≤3 lines):
```lean
example (P : MvPolynomial (Option τ) R) (ν : ℕ) :
    Roth.coeffNone P ν = (optionEquivLeft R τ P).coeff ν := rfl
```
Call sites in our project (from Phase 6.0): 7 declarations, all in Roth/Separation.lean.
Refactor plan: no inlining needed; keep the def. Optionally (a) restate `coeff_coeffNone` (Separation.lean:85) as `(coeffNone P ν).coeff d = P.coeff (d.optionElim ν) := optionEquivLeft_coeff_coeff R P ν d`, and update its users at 107 (or replace with `optionEquivLeft_coeff_some_coeff_none` per the `eq_mapDomain_some_add_single` report) and 129. (b) Shorten `eq_sum_X_none_pow_mul_coeffNone` via `Polynomial.as_sum_range'` transport (evidence (4)). (c) Assess `degreeOf_coeffNone_le` re-aimed at `degreeOf_coeff_optionEquivLeft` for a mathlib PR to Mathlib/Algebra/MvPolynomial/Equiv.lean.
Next action: keep `Roth.coeffNone` as a local abbreviation (no mathlib PR); re-aim the downstream lemmas as above.

---

## Next step

No mathlib PR for `coeffNone`. Restate `coeff_coeffNone` in the `optionElim` spelling (then it is `optionEquivLeft_coeff_coeff`), and run the `degreeOf_coeffNone_le` assessment re-aimed at `degreeOf_coeff_optionEquivLeft`, which is absent from mathlib, as the `optionEquivLeft` analogue of `degreeOf_coeff_finSuccEquiv`.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.coeffNone/reaim.lean` (imports `Roth.Separation`). One `lake env lean` run (~40 s) printed only the `#check` output, with no errors. Checks: (0) `#check @Roth.coeffNone` shows signature `{τ} {R} [CommSemiring R] → MvPolynomial (Option τ) R → ℕ → MvPolynomial τ R` (no Fintype/DecidableEq); (1) `coeffNone P ν = (optionEquivLeft R τ P).coeff ν := rfl`; (2) `(coeffNone P ν).coeff d = P.coeff (d.optionElim ν) := optionEquivLeft_coeff_coeff R P ν d`; (3) `degreeOf_coeff_optionEquivLeft` proved in 2 lines from `mem_support_coeff_optionEquivLeft` + `monomial_le_degreeOf`; (4) the expansion `P = ∑ ν ∈ range (n+1), X none ^ ν * rename some (coeffNone P ν)` proved by `optionEquivLeft` injectivity + `Polynomial.as_sum_range'` + `natDegree_optionEquivLeft`.
- Searches: 3 WebSearch queries; Lean-Finder, LeanSearch and Loogle queries; mathlib grep for `coeffNone`, `def .*coeff.*Option`, and `optionEquivLeft.*coeff`, all recorded above. ChatGPT MCP was n/a (not configured in this session).
