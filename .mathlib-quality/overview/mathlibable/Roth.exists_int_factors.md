---
decl: Roth.exists_int_factors
file: Roth/Separation.lean
line: 485
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: CHEAP
junk: KEEP
rationale: A separated-variables instance of Gauss's lemma for MvPolynomial (factorisation over Frac R descends to R with equal partial degrees); mathlib's Gauss lemma is univariate only, the UFD/fraction-field generalisation compiles (evidence (6)), but whether mathlib wants this rename-some/aeval-X-none shape or only the general MvPolynomial Gauss lemma (not yet compiled, needs an MvPolynomial content API) is a judgment call.
action: Keep in project (sole caller exists_det_eq_mul, Roth/Separation.lean:552); if upstreaming, first land the MvPolynomial content API from the Roth.exists_primitive_smul_eq verdict, then decide between exists_factors_of_map_eq_rename_mul_aeval (evidence (6), UFD R, IsFractionRing R K) and a general MvPolynomial Gauss lemma in Mathlib/RingTheory/MvPolynomial/Content.lean (new) or Mathlib/RingTheory/Polynomial/GaussLemma.lean.
---

# Roth.exists_int_factors

## Inventory entry

### `theorem Roth.exists_int_factors`
- **Type**: `∀ {τ : Type u_1} {U' : MvPolynomial τ ℚ} {V' : Polynomial ℚ}, U' ≠ 0 → V' ≠ 0 → ∀ {F : MvPolynomial (Option τ) ℤ}, map (Int.castRingHom ℚ) F = rename some U' * Polynomial.aeval (X none) V' → ∃ U V, U ≠ 0 ∧ V ≠ 0 ∧ F = rename some U * Polynomial.aeval (X none) V ∧ (∀ j, degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree` (from `#check`, evidence (0)).
- **What**: if an integer polynomial `F(x_τ, y)` factors over ℚ as `U'(x_τ) V'(y)` with nonzero factors, then it factors over ℤ as `U(x_τ) V(y)` with nonzero factors of the same partial degrees.
- **How**: `exists_primitive_smul_eq` gives `g ≠ 0` and primitive integral `U` with `map U = g • U'`; `rescale_separated_factor_aux` rewrites the factorisation as `rename U * aeval (C g⁻¹ * V')`; `exists_int_polynomial_of_primitive_factor_aux` (via `exists_int_eq_of_gcd_eq_one` and `coeff_rename_mul_aeval`) shows `C g⁻¹ * V'` has integer coefficients; equality over ℤ by `MvPolynomial.map_injective` + `map_rename` + `Polynomial.map_aeval_eq_aeval_map`; degree equalities via `degrees_map_of_injective`, `degreeOf_C_mul`, `Polynomial.natDegree_map_eq_of_injective`, `Polynomial.natDegree_C_mul`.
- **Hypotheses**: `hU : U' ≠ 0` (needed for the primitive multiple), `hV : V' ≠ 0` (only for the conclusion `V ≠ 0`), `hF` the rational factorisation.
- **Uses from project**: `Roth.exists_primitive_smul_eq`, `Roth.rescale_separated_factor_aux` (private), `Roth.exists_int_polynomial_of_primitive_factor_aux` (private; itself uses `Roth.exists_int_eq_of_gcd_eq_one`, `Roth.coeff_rename_mul_aeval`)
- **Used by**: `Roth.exists_det_eq_mul` (Roth/Separation.lean:552, `obtain ⟨U, V, hU, hV, hFUV, -, -⟩ := exists_int_factors hU' hV' hFmap`); mentioned in module docstring Separation.lean:35. No other uses (`grep -rn exists_int_factors Roth/`). Indirectly feeds `Roth/Theta.lean:571` through `exists_det_eq_mul`.
- **Visibility**: public
- **Lines**: 481–505 (statement 485–489), proof length 16 lines
- **Notes**: The degree-equality conjuncts are discarded by the only caller (`-, -`); degrees are re-derived there from `degreeOf_rename_mul_aeval`. Docstring cites clean.tex §2, proof of Lemma 2.

## Junk check (Step 8)
- Used anywhere? Yes, once (Separation.lean:552).
- Wrapper of 1–2 mathlib calls? No; it assembles three project lemmas plus five degree/injectivity rewrites.
- Does mathlib have it? No. Mathlib's Gauss lemma (`Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map`, `Polynomial.IsPrimitive.irreducible_iff_irreducible_map_fraction_map`, Mathlib/RingTheory/Polynomial/GaussLemma.lean) is univariate; no MvPolynomial Gauss lemma or content API (grep of `namespace MvPolynomial` files for `IsFractionRing`/`Gauss`/`IsPrimitive` finds only FieldTheory/SeparablyGenerated.lean, unrelated).
- Too specific? Shape is specific (separated variables), but it is a named step of the source proof and the natural interface for Lemma 2.
- Well-chosen? Yes; the unused degree conjuncts could be dropped locally, but they are cheap and natural.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring does not start with internal/auxiliary; Step 8 KEEP; `exists_int_factors` / `exists_factors_of_map` absent from mathlib (grep). Not a glue lemma. Full workflow follows.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` elaborates with 0 errors)
- decl `Roth.exists_int_factors`: resolved at Roth/Separation.lean:485
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable: the determinant `F = U(x_1, …, x_{p-1}) V(x_p)` (Lemma 2), including the integrality/primitivity rescaling.

### Statement (Phase 1)

`Roth.exists_int_factors` is a theorem stating: let `F ∈ ℤ[x_s (s ∈ τ), y]`. If over ℚ we have `F = U'(x) V'(y)` with `U' ∈ ℚ[x]`, `V' ∈ ℚ[y]` both nonzero, then there are nonzero `U ∈ ℤ[x]`, `V ∈ ℤ[y]` with `F = U(x) V(y)` over ℤ, `deg_{x_j} U = deg_{x_j} U'` for all `j`, and `deg V = deg V'`. This is Gauss's lemma for a factorisation into factors in disjoint sets of variables.

Variables / typeclasses involved (Lean side):
- `τ : Type*`: the non-distinguished variables; `Option τ` adds the distinguished variable `none` (= `y`).
- `U' : MvPolynomial τ ℚ`, `V' : Polynomial ℚ`: the rational factors.
- `F : MvPolynomial (Option τ) ℤ`: the integer polynomial.

Hypotheses (Lean side):
- `hU : U' ≠ 0`, `hV : V' ≠ 0`.
- `hF : map (Int.castRingHom ℚ) F = rename some U' * Polynomial.aeval (X none) V'`.

Conclusion (math): `F` factors over ℤ as `U(x) V(y)` with the same partial degrees.

Conclusion (Lean): `∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧ F = rename some U * Polynomial.aeval (X none) V ∧ (∀ j, degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an integrality helper inside the proof of Lemma 2; not a main result, not named.

### One-line check (Phase 2b)

Body line count: 16 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form) | "Gauss lemma integer polynomial factors over rationals then factors over integers multivariate" | yes | a factorisation over ℚ of an integer polynomial rescales to one over ℤ (via content/primitive part) | Wikipedia "Gauss's lemma (polynomials)", "Primitive part and content"; Isabelle AFP Gauss_Lemma / Factorize_Rat_Poly (univariate); UW 504 worksheet notes it extends to UFDs and several variables |
|  2 | WebSearch (general form) | "Gauss lemma unique factorization domain polynomial factorization over fraction field implies factorization over ring same degrees" | yes | R UFD (or GCD domain), K = Frac R: if f ∈ R[x] factors as gh in K[x], then f = (cg)(c⁻¹h) with both factors in R[x], degrees unchanged | Wikipedia; Garrett (UMN) notes 12; Queen's Math210 notes 11; LSU M7210 lecture notes |
|  3 | WebSearch (aliases / source) | "polynomial in separated variables U(x)V(y) integral coefficients Roth lemma rational factorization integral" | no | n/a | hits concern separated-variable ideals (arXiv 2002.01541, 2405.19223), not this integrality step; the separated shape has no standard name |
|  4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session |
|  5 | Local references | grep `.mathlib-quality/references/clean.tex` for "primitive", "integral" | yes | clean.tex lines 420–431: choose g ∈ ℚ× with U = gG primitive integral; primitivity gives ∑ z_a u_a = 1 so each v_b is integral; "Thus U, V are integral and nonzero" | exactly the project statement, ℤ/ℚ |
|  6 | nLab | Gauss's lemma | no | n/a | nLab has no page on polynomial Gauss lemma (not a categorical notion) |
|  7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
|  8 | Stacks Project | n/a | n/a | n/a | elementary commutative algebra; Stacks has no tagged Gauss-lemma-for-factorisations statement |
|  9 | MathOverflow / Math.SE | covered by #2 (lecture notes) | partial | same as #2 | standard textbook (Lang, Algebra IV §2; Dummit–Foote §9.3) |
| 10 | recent arXiv | covered by #3 | no | n/a | classical result, no recent reformulation |

### Literature summary (Phase 3)

Concept identified as: Gauss's lemma (factorisations over the fraction field descend to the ring, after rescaling by a unit of K).
Sources agree on the standard form: yes.
Most general standard form: R a UFD (more generally a GCD domain), K = Frac R, polynomials in any number of variables: if `f ∈ R[x]` and `f = gh` in `K[x]` then there is `c ∈ K^×` with `cg, c⁻¹h ∈ R[x]`; in particular degrees in each variable are preserved.
Generality dimensions where the literature varies:
  - base ring: ℤ → UFD → GCD domain.
  - number of variables: one → any (multivariate via R[x_1..x_{n-1}] UFD, or directly via content over all coefficients).
  - factor shape: arbitrary factors vs. factors in disjoint variables (the project's case; literature does not single it out).
Disagreement with the literature: none; the project's statement is the ℤ/ℚ, separated-variables instance.

### Generality analysis — `Roth.exists_int_factors`

Literature-standard form (from Phase 3): UFD/GCD domain R, K = Frac R, arbitrary factors g, h of a multivariate f.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | base ring ℤ | `ℤ` | UFD (GCD domain) | yes | compiled for `[IsDomain R] [NormalizedGCDMonoid R] [UniqueFactorizationMonoid R]` (evidence (6)); UFD rather than GCD domain only because mathlib's `IsFractionRing.num`/`den` (Localization/NumDen.lean) require `UniqueFactorizationMonoid` |
| 2 | coefficient field ℚ | `ℚ` | `[IsFractionRing R K]` | yes | compiled (evidence (6)) |
| 3 | `Int.castRingHom ℚ` | concrete map | `algebraMap R K` | yes | specialises by term (evidence (7)) |
| 4 | separated factors `rename some U' * aeval (X none) V'` | disjoint variables | arbitrary factors `G * H` | yes in literature, not compiled | general MvPolynomial Gauss lemma needs a content multiplicativity argument (Gauss lemma proper, "product of primitives is primitive" for MvPolynomial) not in mathlib; the separated case avoids it because coefficients of the product are products of coefficients |
| 5 | `hU : U' ≠ 0` | nonzero | nonzero | NO | needed for the primitive multiple |
| 6 | `hV : V' ≠ 0` | nonzero | nonzero | NO | needed for conclusion `V ≠ 0` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 3 verified (ℤ → UFD, ℚ → fraction field, cast → algebraMap; evidence (6), 0 errors); 1 further (arbitrary factors) literature-standard but not compiled.
Proposed restatement (verified):
```lean
theorem MvPolynomial.exists_factors_of_map_eq_rename_mul_aeval {τ R K : Type*} [CommRing R]
    [IsDomain R] [NormalizedGCDMonoid R] [UniqueFactorizationMonoid R] [Field K] [Algebra R K]
    [IsFractionRing R K] {U' : MvPolynomial τ K} {V' : Polynomial K} (hU : U' ≠ 0) (hV : V' ≠ 0)
    {F : MvPolynomial (Option τ) R} (hF : map (algebraMap R K) F =
      rename some U' * Polynomial.aeval (X none : MvPolynomial (Option τ) K) V') :
    ∃ (U : MvPolynomial τ R) (V : Polynomial R), U ≠ 0 ∧ V ≠ 0 ∧
      F = rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V ∧
      (∀ j, degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree
```
Supporting generalised integrality test (evidence (5)), which needs no Bezout identity:
```lean
theorem isInteger_of_gcd_eq_one {ι R K : Type*} [CommRing R] [IsDomain R] [NormalizedGCDMonoid R]
    [UniqueFactorizationMonoid R] [Field K] [Algebra R K] [IsFractionRing R K] {s : Finset ι}
    {u : ι → R} (hu : s.gcd u = 1) {v : K}
    (hv : ∀ a ∈ s, IsLocalization.IsInteger R (algebraMap R K (u a) * v)) :
    IsLocalization.IsInteger R v
```
Cost of restatement: CHEAP (compiled; about 35 lines on top of the `exists_primitive_smul_eq_map` evidence).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Downstream |
|---|---|---|---|---|
| 1 | preambles → typeclasses | no | no bundled hypotheses | — |
| 2 | sequences → filters | no | algebraic | — |
| 3 | construction → universal property | no | existence statement | — |
| 4 | set+predicate → bundled substructure | partial | "integral" as `F ∈ (MvPolynomial.map (algebraMap R K)).range` / lifts | aligns with `Polynomial.lifts` API |
| 5 | field-specific → typeclass hierarchy | yes | ℤ/ℚ → UFD / `IsFractionRing` (evidence (6)) | applies over ℤ[i], k[t], number-ring UFDs |
| 6 | 1-categorical → higher | no | n/a | — |
| 7 | concrete index → abstract | no | τ arbitrary; `Option τ` is the standard way to adjoin a variable | — |
| 8 | concrete-via-abstract | yes | ℤ/ℚ enter only via `exists_primitive_smul_eq` and `exists_int_eq_of_gcd_eq_one`, both replaced by GCD/UFD + fraction-ring versions | same proof for all UFDs |
| 9 | false-generalisation guard | no false generalisation | specialisation at R = ℤ, K = ℚ recovers the exact statement by term (evidence (7)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the UFD/`IsFractionRing` form above; the more idiomatic mathlib target would be the general MvPolynomial Gauss lemma `map F = G * H → ∃ c ≠ 0, (C c * G) ∈ range map ∧ (C c⁻¹ * H) ∈ range map`, paralleling `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map`.
  - Cost: CHEAP for the separated form (compiled); MODERATE–EXPENSIVE for the general MvPolynomial Gauss lemma (needs MvPolynomial content and "product of primitives is primitive").
  - Mathlib downstream this enables: MvPolynomial analogue of GaussLemma.lean; integrality descent for factorisations in `MvPolynomial σ (FractionRing R)`.
  - Real mathematical improvement: one proof for all UFDs; isolates the integrality test as a reusable lemma.

### Proof strategy — `Roth.exists_int_factors`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elementwise vs ideals | partial | integrality test could be phrased with `Submodule.mem_of_span_top_of_smul_mem` (PID/Bezout case) or reduced fractions (UFD case, evidence (5)) | CHEAP |
| 3 | sequences vs filters | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing helpers mathlib should have | yes | MvPolynomial content/primitive multiple (from `Roth.exists_primitive_smul_eq` verdict); `isInteger_of_gcd_eq_one` over a UFD; `coeff_rename_mul_aeval` | CHEAP, follow-up PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
  - The proof is a short assembly of three helpers and injectivity/degree rewrites; the generalised proof (evidence (6)) has the same structure. The helpers themselves are the missing API.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.exists_int_factors`

[A] Lean-Finder       "if a polynomial with coefficients in a UFD factors over the fraction field, it factors over the ring with factors of the same degree"   no relevant hit (Polynomial.uniqueFactorizationMonoid, UniversalFactorizationRing)
[B] Loogle            `MvPolynomial.map, MvPolynomial.rename, Polynomial.aeval, IsFractionRing`   no hits
[C] LeanSearch        "multivariate polynomial over integers factoring over rationals factors over integers Gauss lemma MvPolynomial"   only univariate GaussLemma results (`Polynomial.IsPrimitive.Int.irreducible_iff_irreducible_map_cast`, `Polynomial.IsPrimitive.irreducible_iff_irreducible_map_fraction_map`, `Polynomial.Monic.dvd_of_fraction_map_dvd_fraction_map`, `Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast`)
[D] Grep mathlib src  `exists_int_factors`, `exists_factors_of_map`, `rename_mul_aeval`; `namespace MvPolynomial` files mentioning `IsFractionRing`/`Gauss`/`IsPrimitive`   no hits (only FieldTheory/SeparablyGenerated.lean, unrelated irreducibility criterion)
[E] Name pattern      lean_local_search not used (brief: keep Lean runs few); replaced by [D] grep

Searched for both the ℤ/ℚ separated form and the general UFD/fraction-field MvPolynomial Gauss lemma.
Concluded: found building blocks (`Polynomial.mem_map_range`, `MvPolynomial.map_injective`, `Polynomial.map_aeval_eq_aeval_map`, `IsFractionRing.num_den_reduced`, `IsFractionRing.isInteger_of_isUnit_den`, `degreeOf_C_mul`); univariate Gauss lemma exists; not in mathlib for MvPolynomial in either form.

### Normal-form check

Equivalent formalisms: (a) as stated (∃ U V with equation and degrees); (b) `F ∈ range` of the product map with explicit rescaling `U = g U'`, `V = g⁻¹ V'`; (c) general Gauss lemma for arbitrary factors.
Canonical form in mathlib: univariate uses divisibility (`p ∣ q ↔ map p ∣ map q` for primitive p) and `lifts`. No MvPolynomial canonical form. RHS convention respected: yes.

### Syntactic generality

Alternatives: (a) as stated; (b) drop the degree conjuncts (unused by the only caller); (c) conclude `U = g • U'`, `V = g⁻¹ • V'` explicitly (degrees then follow by simp).
Chosen: (a) is easiest at the call site (destructured by `obtain`). (c) would be more informative for a mathlib version.

### Superfluous-argument audit

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hU : U' ≠ 0` | yes | primitive multiple needs it |
| 2 | `hV : V' ≠ 0` | yes | only for conclusion `V ≠ 0` |
| 3 | ℤ/ℚ specificity | no | UFD / fraction field (evidence (6)) |
| 4 | degree conjuncts (conclusion) | not consumed | caller discards them; harmless |

### Statement-shape verdict (Phase 5.5)

Normal form: OK for project; a mathlib version would preferably state the general Gauss lemma or the explicit rescaling (c).
Syntactic generality: OK
Superfluous arguments: 1 to drop (ℤ/ℚ concreteness)
Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.exists_int_factors`

Internal use count: 1 (in the declaring file); 0 in other files
External-to-file callers: 0

| Caller file:line | Usage pattern |
|---|---|
| Roth/Separation.lean:552 | `obtain ⟨U, V, hU, hV, hFUV, -, -⟩ := exists_int_factors hU' hV' hFmap` (in `exists_det_eq_mul`) |

Inline-derivation grep: (none) — no other rational-to-integer factor descent in `Roth/`.

### Composition check (Phase 6)

Attempt 1: univariate Gauss lemma `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map` via `optionEquivLeft` (view F as a polynomial in `y` over ℤ[x]).
  - Result: fails; R = ℤ[x_τ] with K = Frac(ℤ[x_τ]) is not the setting (we have ℚ[x_τ], and U' is not over ℤ[x]); would need MvPolynomial ℤ ↔ ℚ fraction-field comparison plus the content API anyway.
Attempt 2: `exists_primitive_smul_eq_map` + integrality test + injectivity rewrites.
  - Result: succeeds but is a ~35-line proof using project-level helpers not in mathlib (evidence (6)).
Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.exists_int_factors`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): Gauss's lemma; standard over UFD/GCD domains and any number of variables; the separated-variables shape is not singled out in the literature.
- Generality analysis (Phase 4): STRICTLY NARROWER; ℤ/ℚ → UFD/`IsFractionRing` compiled (evidence (6), (7)); arbitrary-factor form not compiled.
- Mathlib search (Phase 5): Gauss lemma univariate only; no MvPolynomial content or Gauss lemma.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:** The mathematical content (Gauss's lemma for multivariate polynomials over a UFD) is a genuine mathlib gap: GaussLemma.lean and Content.lean are purely univariate and there is no `MvPolynomial` content, primitivity, or fraction-field factor descent. The project's proof generalises cleanly (evidence (6): UFD R, `IsFractionRing R K`, 0 errors) and the ℤ/ℚ statement is recovered by a term (evidence (7)), so a YES-but-generalise-first reading is mechanically supported. However, the statement's shape, `rename some U * Polynomial.aeval (X none) V` with disjoint variable sets, is a project-specific special case; the mathlib-idiomatic target is the general MvPolynomial Gauss lemma for arbitrary factors (needs "product of primitive MvPolynomials is primitive", not compiled, MODERATE–EXPENSIVE), from which this statement would be a corollary. Whether mathlib reviewers would accept the separated-shape lemma as a stepping stone, or require the general Gauss lemma, is a taste/policy call the evidence cannot settle. Also, the project's single caller discards the degree conjuncts.

Numbered questions:
1. Should the upstream target be the general MvPolynomial Gauss lemma (arbitrary factors G, H) rather than the separated-variables form? (If yes: YES-but-generalise-first with an EXPENSIVE target; this decl becomes a corollary.)
2. If the separated form is acceptable, is the UFD hypothesis acceptable, or must it be GCD domain (would need a reduced-fraction API that mathlib currently only provides for UFDs in Localization/NumDen.lean)?
3. Should this be bundled in one PR with the MvPolynomial content API from `Roth.exists_primitive_smul_eq` (YES-but-generalise-first) and `Roth.exists_nat_smul_eq_map`?
4. Locally, should the unused degree conjuncts be dropped from the statement (the caller destructures them as `-, -`)?

Next action: user answers the questions; meanwhile keep the decl in the project. Evidence (5) (`isInteger_of_gcd_eq_one` over a UFD) and (6) are ready to seed a `/generalise Roth.exists_int_factors` run.

---

### Next step

Answer questions 1–4; if the separated form is accepted, run `/generalise Roth.exists_int_factors` targeting `MvPolynomial.exists_factors_of_map_eq_rename_mul_aeval` (evidence (6)) after landing the MvPolynomial content API, keeping the project statement as the specialisation (evidence (7)).

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.exists_int_factors/generalise.lean` (imports `Roth.Separation`, `Mathlib.RingTheory.MvPolynomial.Localization`, `Mathlib.RingTheory.Localization.FractionRing`, `Mathlib.RingTheory.Localization.Integral`, `Mathlib.RingTheory.Localization.NumDen`). Five `lake env lean` runs (about 30 s each); intermediate errors fixed (num/den needs `UniqueFactorizationMonoid`; `mk'_spec` instance argument; commuting-square hypothesis for `map_aeval_eq_aeval_map`); final run: 0 errors.
  - (0) `#check @Roth.exists_int_factors`
  - (1)–(3) copied from the `Roth.exists_primitive_smul_eq` evidence: localization denominator clearing, MvPolynomial content decomposition, general primitive multiple `exists_primitive_smul_eq_map`
  - (5) `isInteger_of_gcd_eq_one` (UFD integrality test, no Bezout)
  - (6) `exists_factors_of_map_eq_rename_mul_aeval` (UFD R, `IsFractionRing R K` form of the decl)
  - (7) project statement as the term `exists_factors_of_map_eq_rename_mul_aeval hU hV hF`
- Searches: 3 WebSearch queries, Lean-Finder, Loogle, LeanSearch, mathlib grep (recorded above). ChatGPT MCP n/a (not configured). `lean_local_search` not used (replaced by grep).
- Web sources: https://en.wikipedia.org/wiki/Gauss%27s_lemma_(polynomials), https://en.wikipedia.org/wiki/Primitive_part_and_content, https://devel.isa-afp.org/browser_info/current/AFP/Polynomial_Factorization/Gauss_Lemma.html, https://sites.math.washington.edu/~julia/teaching/504_Fall2018/WK_Polynomials.pdf, https://www-users.cse.umn.edu/~garrett/m/algebra/notes_2023-24/12.pdf, https://mast.queensu.ca/~ggsmith/Math210/notes11.pdf
