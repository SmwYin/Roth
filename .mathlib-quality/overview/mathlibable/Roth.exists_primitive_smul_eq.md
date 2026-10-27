---
decl: Roth.exists_primitive_smul_eq
file: Roth/Separation.lean
line: 406
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Mathlib has content/primPart only for univariate Polynomial (RingTheory/Polynomial/Content.lean) and no MvPolynomial content or primitive-part API; the ℤ/ℚ statement is the instance of a GCD-domain/fraction-field statement that splits into an MvPolynomial content decomposition plus denominator clearing, both compiled as evidence.
action: Add MvPolynomial.exists_eq_C_gcd_mul (content decomposition, evidence (2)) and MvPolynomial.exists_primitive_smul_eq_map (GCD domain R, IsFractionRing R K, evidence (3)) next to MvPolynomial.isLocalization in Mathlib/RingTheory/MvPolynomial/Localization.lean (or a new MvPolynomial/Content.lean); in the project replace the body at Roth/Separation.lean:406 by the specialisation (evidence (4)); sole caller exists_int_factors (Separation.lean:491) is unchanged.
---

# Roth.exists_primitive_smul_eq

## Inventory entry

### `theorem Roth.exists_primitive_smul_eq`
- **Type**: `∀ {σ : Type u_1} {G : MvPolynomial σ ℚ}, G ≠ 0 → ∃ g U, g ≠ 0 ∧ (map (Int.castRingHom ℚ)) U = g • G ∧ (U.support.gcd fun d => U.coeff d) = 1` (from `#check`, evidence (0)), with `g : ℚ`, `U : MvPolynomial σ ℤ`.
- **What**: every nonzero rational multivariate polynomial has a nonzero rational multiple that is an integer polynomial whose coefficients have gcd 1 (a primitive integral polynomial).
- **How**: clears denominators with `Roth.exists_nat_smul_eq_map` to get `U0` with `map U0 = N • G`; shows `U0.support` is nonempty; applies `Finset.extract_gcd` to the coefficient function to get `g'` with `U0.coeff d = g0 * g' d` and `gcd g' = 1`; builds `U := ∑ d ∈ U0.support, monomial d (g' d)` (coefficients via `coeff_monomial`, `Finset.sum_ite_eq'`); takes `g := N / g0`; proves the map identity coefficientwise (`coeff_map`, `coeff_smul`, `eq_div_iff`) and transfers the gcd via `U.support = U0.support` and `Finset.gcd_congr`.
- **Hypotheses**: `hG : G ≠ 0` (essential: for `G = 0` the gcd condition forces `U ≠ 0`, impossible). Base rings fixed to ℤ ⊂ ℚ.
- **Uses from project**: `Roth.exists_nat_smul_eq_map`
- **Used by**: `Roth.exists_int_factors` (Roth/Separation.lean:491, `obtain ⟨g, U, hg, hUmap, hgcd⟩ := exists_primitive_smul_eq hU`). No other uses (`grep -rn exists_primitive_smul_eq Roth/`).
- **Visibility**: public
- **Lines**: 402–437 (statement 406–408), proof length 29 lines
- **Notes**: Section `Integrality`. Docstring cites clean.tex §2, proof of Lemma 2 ("Choose g ∈ ℚ× so that U = gG is an integral primitive polynomial"). The gcd conclusion is consumed by `exists_int_polynomial_of_primitive_factor_aux` (via `exists_int_eq_of_gcd_eq_one`).

## Junk check (Step 8)
- Used anywhere? Yes, once (Separation.lean:491, `exists_int_factors`).
- Wrapper of 1–2 mathlib calls? No; it combines denominator clearing with a content/primitive-part extraction (29 lines). Mathlib has `Finset.extract_gcd` but no MvPolynomial content API to finish the job.
- Does mathlib have it? No. Mathlib has the univariate pieces only: `Polynomial.content`, `Polynomial.primPart`, `Polynomial.eq_C_content_mul_primPart`, `Polynomial.isPrimitive_primPart` (Mathlib/RingTheory/Polynomial/Content.lean) and `IsLocalization.integerNormalization_spec` (Mathlib/RingTheory/Localization/Integral.lean). Grep for `MvPolynomial.content`, `MvPolynomial.IsPrimitive`, `MvPolynomial.primPart` over `.lake/packages/mathlib/Mathlib/`: no hits.
- Too specific? Over-specialised to ℤ/ℚ (see Step 9), but it is a genuine named step of the source proof and not inlinable cheaply.
- Well-chosen? Yes as a statement shape (it is exactly what the caller consumes).
- Conclusion: `KEEP` (generalise in place per Step 9; the ℤ/ℚ statement becomes a one-line specialisation).

## Mathlibable assessment (Step 9)

Pre-filter: not private; name does not end in `_aux`; docstring does not start with internal/auxiliary; Step 8 is KEEP; the qualified name and `exists_primitive_smul` are absent from mathlib (grep). Not a glue lemma. Full workflow follows.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` elaborates)
- decl `Roth.exists_primitive_smul_eq`: resolved at Roth/Separation.lean:406
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable: the determinant `F = U(x_1, …, x_{p-1}) V(x_p)` (Lemma 2), including the integrality/primitivity rescaling.

### Statement (Phase 1)

`Roth.exists_primitive_smul_eq` is a theorem stating: for every nonzero `G ∈ ℚ[x_s : s ∈ σ]` there exists `g ∈ ℚ^×` such that `gG` lies in `ℤ[x_s]` and is primitive, i.e. the gcd of its coefficients is 1. Equivalently, `G = g^{-1} U` with `U` a primitive integer polynomial (the "content times primitive part" decomposition over the fraction field).

Variables / typeclasses involved (Lean side):
- `σ : Type*`: index set of variables (arbitrary).
- `G : MvPolynomial σ ℚ`: the rational polynomial.

Hypotheses (Lean side):
- `hG : G ≠ 0`.

Conclusion (math): `∃ g ∈ ℚ^×, ∃ U ∈ ℤ[x] primitive, U = gG`.

Conclusion (Lean): `∃ (g : ℚ) (U : MvPolynomial σ ℤ), g ≠ 0 ∧ map (Int.castRingHom ℚ) U = g • G ∧ U.support.gcd (fun d ↦ U.coeff d) = 1`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: standard helper fact (content/primitive part over a fraction field) used once in Lemma 2; not a main result, not named.

### One-line check (Phase 2b)

Body line count: 29 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form) | "rational multivariate polynomial scalar multiple primitive integer polynomial content Gauss lemma" | yes | every f ∈ ℚ[X] is c·f* with f* ∈ ℤ[X] primitive | Wikipedia "Primitive part and content"; ProofWiki "Content of Rational Polynomial is Multiplicative" (stated univariate) |
|  2 | WebSearch (general form) | "polynomial over fraction field of GCD domain equals c times primitive polynomial unique up to unit" | yes | R GCD domain/UFD, K = Frac R: every nonzero f ∈ K[X] is c·f₀, c ∈ K^×, f₀ ∈ R[X] primitive, unique up to units | Queen's Math210 notes Lemma 10.0.2 (UFD); Wikipedia "Gauss's lemma (polynomials)" says this survives over GCD domains |
|  3 | WebSearch (aliases / Lean) | "Lean mathlib MvPolynomial content primPart IsPrimitive" | yes | univariate only: `Polynomial.content`, `primPart`, `eq_C_content_mul_primPart` | no MvPolynomial content API found in any doc mirror |
|  4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session |
|  5 | Local references | grep `.mathlib-quality/references/clean.tex` for "primitive" | yes | clean.tex line 420: "Choose g ∈ ℚ× so that U = gG is an integral primitive polynomial" | exactly the project statement, ℤ/ℚ, multivariate |
|  6 | nLab | content of a polynomial / Gauss lemma | no | n/a | nLab has no dedicated page for polynomial content; not a categorical concept (checked via general knowledge of nLab coverage, no page found in search results) |
|  7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
|  8 | Stacks Project | n/a | n/a | n/a | elementary commutative algebra; Stacks treats content ideals but not this GCD-domain normalisation as a tagged lemma |
|  9 | MathOverflow / Math.SE | covered by search #2 results (lecture notes) | partial | same as #2 | standard textbook fact (Lang, Algebra IV §2; Dummit–Foote §9.3) |
| 10 | recent arXiv | n/a | n/a | n/a | classical textbook result, no recent research formulation |

### Literature summary (Phase 3)

Concept identified as: content and primitive part; "every polynomial over Frac R is a scalar times a primitive polynomial over R" (the normalisation step of Gauss's lemma).
Sources agree on the standard form: yes.
Most general standard form: R a GCD domain (classically UFD), K its fraction field, any (finite or infinite) set of variables: every nonzero `f ∈ K[x]` equals `c·f₀` with `c ∈ K^×` and `f₀ ∈ R[x]` primitive (gcd of coefficients a unit), unique up to units of R.
Generality dimensions where the literature varies:
  - base ring: ℤ → UFD → GCD domain (most general: GCD domain; with normalised gcd, "gcd = 1").
  - number of variables: one → several (the content argument is identical; only coefficients matter).
Disagreement with the literature: none; the project's form is the ℤ/ℚ instance.

### Generality analysis — `Roth.exists_primitive_smul_eq`

Literature-standard form (from Phase 3): GCD domain R, fraction field K, arbitrary σ.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | base ring ℤ | `ℤ` | `[CommRing R] [IsDomain R] [NormalizedGCDMonoid R]` | yes | proof uses only `Finset.extract_gcd` (needs normalised GCD monoid) and `gcd ≠ 0` from nonzero coefficient; compiled (evidence (3)) |
| 2 | coefficient field ℚ | `ℚ` | `[Field K] [Algebra R K] [IsFractionRing R K]` | yes | denominator clearing holds for any localization; compiled (evidence (1),(3)) |
| 3 | `Int.castRingHom ℚ` | concrete map | `algebraMap R K` | yes | specialises definitionally (evidence (4) closes with the term directly) |
| 4 | `hG : G ≠ 0` | nonzero | nonzero | NO | needed: gcd = 1 forces U ≠ 0 |
| 5 | `σ : Type*` | arbitrary | arbitrary | no | already general |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 2 (ℤ → GCD domain, ℚ → its fraction field), both verified by compilation (evidence file below, 0 errors).
Proposed restatement:
```lean
theorem MvPolynomial.exists_primitive_smul_eq_map {σ R K : Type*} [CommRing R] [IsDomain R]
    [NormalizedGCDMonoid R] [Field K] [Algebra R K] [IsFractionRing R K]
    {G : MvPolynomial σ K} (hG : G ≠ 0) :
    ∃ (g : K) (U : MvPolynomial σ R), g ≠ 0 ∧ map (algebraMap R K) U = g • G ∧
      U.support.gcd U.coeff = 1
```
proved from two independent pieces:
```lean
-- content decomposition (MvPolynomial analogue of Polynomial.eq_C_content_mul_primPart)
theorem MvPolynomial.exists_eq_C_gcd_mul {σ R : Type*} [CommRing R] [IsDomain R]
    [NormalizedGCDMonoid R] {P : MvPolynomial σ R} (hP : P ≠ 0) :
    ∃ U : MvPolynomial σ R, P = C (P.support.gcd P.coeff) * U ∧ U.support.gcd U.coeff = 1
-- denominator clearing (from the Roth.exists_nat_smul_eq_map assessment)
theorem MvPolynomial.exists_smul_eq_map_of_isLocalization ... :
    ∃ b ∈ M, ∃ U : MvPolynomial σ R, map (algebraMap R S) U = (b : R) • G
```
Cost of restatement: CHEAP (all compiled).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Downstream |
|---|---|---|---|---|
| 1 | preambles → typeclasses | no | statement has no bundled structure hypotheses | — |
| 2 | sequences → filters | no | algebraic, no topology | — |
| 3 | construction → universal property | no | existence statement | — |
| 4 | set+predicate → bundled substructure | partial | "primitive" could be `IsPrimitive`-style predicate (`∀ r, C r ∣ U → IsUnit r`), matching `Polynomial.IsPrimitive` | aligns with `Polynomial.IsPrimitive` API; optional |
| 5 | field-specific → typeclass hierarchy | yes | ℤ/ℚ → GCD domain / `IsFractionRing` (evidence (3)) | applies to `MvPolynomial σ (FractionRing R)` for any GCD domain, e.g. ℤ[i], k[t] |
| 6 | 1-categorical → higher | no | n/a | — |
| 7 | concrete index → abstract | no | σ already arbitrary | — |
| 8 | concrete-via-abstract | yes | proof uses only `Rat.den` clearing + `Finset.extract_gcd`; ℤ/ℚ appear only through those, replaced by localization/GCD-monoid abstractions | same proof serves all GCD domains |
| 9 | false-generalisation guard | no false generalisation | specialisation at R = ℤ, K = ℚ recovers the exact statement by term (evidence (4)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the GCD-domain/`IsFractionRing` form above, ideally factored as an MvPolynomial content API (`MvPolynomial.content := P.support.gcd P.coeff`, `primPart`, `eq_C_content_mul_primPart`) plus denominator clearing.
  - Cost: CHEAP for the lemmas (compiled); MODERATE if reviewers want full `content`/`primPart` defs with simp API.
  - Mathlib downstream this enables: MvPolynomial analogue of the `Polynomial.content`/`primPart` API (Mathlib/RingTheory/Polynomial/Content.lean), the first step toward Gauss-lemma statements for `MvPolynomial` (GaussLemma.lean is univariate only).
  - Real mathematical improvement: one proof covers every GCD domain and isolates the reusable content decomposition.

### Proof strategy — `Roth.exists_primitive_smul_eq`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elementwise vs ideals | no | coefficientwise is standard (Polynomial API does the same) | — |
| 3 | sequences vs filters | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing helpers mathlib should have | yes | `MvPolynomial` content decomposition (evidence (2)); MvPolynomial denominator clearing (evidence (1)) | CHEAP, follow-up PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: split into denominator clearing + content decomposition, then a 15-line combination (evidence (3)).
  - Cost: CHEAP
  - Missing mathlib API: MvPolynomial content/primPart decomposition; MvPolynomial `integerNormalization` analogue.
  - Would refactoring make the proof strictly shorter / cleaner? yes

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.exists_primitive_smul_eq`

[A] Lean-Finder       "every nonzero polynomial over the fraction field is a scalar multiple of a primitive polynomial over the base ring"   only univariate GaussLemma results (`isUnit_or_eq_zero_of_isUnit_integerNormalization_primPart`, `IsPrimitive.dvd_iff_fraction_map_dvd_fraction_map`)
[B] Loogle            `MvPolynomial, Finset.gcd`   no hits
[C] LeanSearch        "content and primitive part of a multivariate polynomial over a GCD domain"   only `Polynomial.content`, `Polynomial.primPart`, `Polynomial.content_primPart`, `Polynomial.isPrimitive_iff_content_eq_one`
[D] Grep mathlib src  `MvPolynomial.content`, `MvPolynomial.IsPrimitive`, `MvPolynomial.primPart`, `exists_primitive_smul`; `def content/IsPrimitive/primPart` inside `namespace MvPolynomial`   no hits (content API exists only in RingTheory/Polynomial/Content.lean and ContentIdeal.lean, univariate)
[E] Name pattern      `lean_local_search` n/a: ripgrep not installed; replaced by [D] grep

Searched for both the ℤ/ℚ form and the GCD-domain/fraction-field form.
Concluded: found building blocks (`Finset.extract_gcd`, `IsLocalization.exist_integer_multiples`, `MvPolynomial.mem_range_map_iff_coeffs_subset`); univariate analogue exists (`IsLocalization.integerNormalization_spec` + `Polynomial.eq_C_content_mul_primPart`); not in mathlib for MvPolynomial.

### Normal-form check

Equivalent formalisms: (a) `∃ g ≠ 0, ∃ U, map U = g • G ∧ gcd coeffs = 1`; (b) `∃ U primitive, G = c • map U`; (c) via `content`/`primPart` defs.
Canonical form in mathlib: univariate uses `p = C p.content * p.primPart` with `IsPrimitive`. For MvPolynomial none exists; propose content decomposition `P = C (content P) * primPart P` as normal form, with the fraction-field statement as a corollary. RHS convention respected: yes.

### Syntactic generality

Alternatives: (a) as stated; (b) `G = g • map U` (g on the other side); (c) `IsPrimitive`-predicate conclusion.
Chosen: (a) — the caller rewrites `U = g • G` directly (see `rescale_separated_factor_aux`), and `gcd = 1` feeds `exists_int_eq_of_gcd_eq_one` without unfolding.

### Superfluous-argument audit

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hG : G ≠ 0` | yes | conclusion false for G = 0 |
| 2 | ℤ/ℚ specificity | no | replaced by GCD domain / fraction field (evidence (3)) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (for project); mathlib version should come with the content decomposition as normal form.
Syntactic generality: OK
Superfluous arguments: 1 to drop (the ℤ/ℚ concreteness; generalise base ring)
Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.exists_primitive_smul_eq`

Internal use count: 1 (in the declaring file; no other files)
External-to-file callers: 0

| Caller file:line | Usage pattern |
|---|---|
| Roth/Separation.lean:491 | `obtain ⟨g, U, hg, hUmap, hgcd⟩ := exists_primitive_smul_eq hU` (in `exists_int_factors`) |

Inline-derivation grep: (none) — no other `Finset.extract_gcd` or content extraction in `Roth/`.

### Composition check (Phase 6)

Attempt 1: `IsLocalization.exist_integer_multiples` + `Finset.extract_gcd` + `mem_range_map_iff_coeffs_subset`.
  - Result: partial; still requires building the MvPolynomial from the extracted coefficient function and transferring support/gcd (about 20 lines, evidence (2)).
Attempt 2: univariate `integerNormalization_spec` + `primPart` via `MvPolynomial ≃ Polynomial` towers: fails (σ arbitrary, content is over all coefficients, not one variable).
Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.exists_primitive_smul_eq`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard "scalar times primitive" normalisation, stated for GCD domains / UFDs and their fraction fields.
- Generality analysis (Phase 4): STRICTLY NARROWER; weakening ℤ/ℚ → GCD domain/`IsFractionRing` compiled (evidence (3)).
- Mathlib search (Phase 5): univariate analogue only; no MvPolynomial content API.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:** Mathlib's content/primitive-part theory (`Polynomial.content`, `Polynomial.primPart`, `Polynomial.eq_C_content_mul_primPart`, `IsLocalization.integerNormalization_spec`, GaussLemma.lean) is entirely univariate; there is no `MvPolynomial` content, primitive part, or "polynomial over Frac R is a scalar times a primitive polynomial over R" statement. That is the concrete gap. The project proves the ℤ/ℚ instance by hand; the same proof, with `Rat.den` replaced by localization clearing and `Finset.extract_gcd` used over any normalised GCD monoid, gives the GCD-domain statement, which specialises back to the exact project statement by a term (evidence (4)).

Reason for the generalisation: LITERATURE-WEAKENING (ℤ/ℚ → GCD domain and its fraction field) and MODERN-IDIOM (factor through an MvPolynomial content decomposition paralleling `Polynomial.eq_C_content_mul_primPart`).
Proposed restatement: `MvPolynomial.exists_primitive_smul_eq_map` (Phase 4b), built on `MvPolynomial.exists_eq_C_gcd_mul` and `MvPolynomial.exists_smul_eq_map_of_isLocalization`; all compiled.
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
  - MvPolynomial counterpart of `Polynomial.eq_C_content_mul_primPart` / `isPrimitive_primPart`; basis for an `MvPolynomial.content`/`primPart` API and MvPolynomial Gauss-lemma statements.
  - Integrality arguments for factorisations over `MvPolynomial σ (FractionRing R)` (exactly how the project uses it in `exists_int_factors`).
Proposed mathlib location: `Mathlib/RingTheory/MvPolynomial/Localization.lean` (with the clearing lemma), or a new `Mathlib/RingTheory/MvPolynomial/Content.lean` for the content decomposition.
PR grouping: ship together with `MvPolynomial.exists_smul_eq_map_of_isLocalization` (from the `Roth.exists_nat_smul_eq_map` YES-but-generalise-first verdict).
Call sites in our project: 1 (Separation.lean:491), unchanged by the refactor.
Next action: run `/generalise Roth.exists_primitive_smul_eq` with the target above; replace the project body by the specialisation of the general lemma; then open "feat(RingTheory/MvPolynomial): content decomposition and primitive multiples over a fraction field".

---

## Next step

Generalise to `MvPolynomial.exists_primitive_smul_eq_map` (GCD domain R, `IsFractionRing R K`) via `exists_eq_C_gcd_mul` + `exists_smul_eq_map_of_isLocalization` (evidence (1)–(3)), keep the project statement as the one-line specialisation (evidence (4)), and upstream together with the `exists_nat_smul_eq_map` generalisation.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.exists_primitive_smul_eq/generalise.lean` (imports `Roth.Separation`, `Mathlib.RingTheory.MvPolynomial.Localization`, `Mathlib.RingTheory.Localization.FractionRing`, `Mathlib.RingTheory.Localization.Integral`, `Mathlib.RingTheory.Polynomial.Content`). Two `lake env lean` runs (about 30 s each); first had two rewrite errors (fixed with `algebraMap_smul`), final run: 0 errors.
  - (0) `#check` of the project decl and the univariate mathlib analogues `Polynomial.eq_C_content_mul_primPart`, `Polynomial.isPrimitive_primPart`, `IsLocalization.integerNormalization_spec`
  - (1) `exists_smul_eq_map_of_isLocalization` (MvPolynomial denominator clearing)
  - (2) `exists_eq_C_gcd_mul` (MvPolynomial content decomposition over a normalised GCD domain)
  - (3) `exists_primitive_smul_eq_map` (general GCD-domain/fraction-field form)
  - (4) project statement as the term `exists_primitive_smul_eq_map hG`
- Searches: 3 WebSearch queries, Loogle, LeanSearch, Lean-Finder, mathlib grep (all recorded above). ChatGPT MCP n/a (not configured). `lean_local_search` n/a (ripgrep missing).
