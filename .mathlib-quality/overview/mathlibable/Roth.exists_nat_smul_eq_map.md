---
decl: Roth.exists_nat_smul_eq_map
file: Roth/Separation.lean
line: 380
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: REPLACE
rationale: Mathlib has denominator clearing for univariate polynomials (IsLocalization.integerNormalization_spec) but no MvPolynomial analogue; the ℤ→ℚ positive-N form is a specialisation of the localization statement (∃ b ∈ M, ∃ U, map (algebraMap R S) U = b • G), which is verified to compile and to serve the only call site.
action: Add `MvPolynomial.exists_smul_eq_map_of_isLocalization` (evidence (2)) to Mathlib/RingTheory/MvPolynomial/Localization.lean; in the project, use it at Roth/Separation.lean:410 (exists_primitive_smul_eq, compiled as evidence (5)) and delete exists_nat_smul_eq_map.
---

# Roth.exists_nat_smul_eq_map

## Inventory entry

### `theorem Roth.exists_nat_smul_eq_map`
- **Type**: `∀ {σ : Type u_1} (G : MvPolynomial σ ℚ), ∃ N U, 0 < N ∧ (map (Int.castRingHom ℚ)) U = ↑N • G` (from `#check`, evidence (0)), with `N : ℕ` and `U : MvPolynomial σ ℤ`
- **What**: clearing denominators. Every rational multivariate polynomial `G` has a positive integer multiple `N • G` whose coefficients all lie in ℤ, i.e. `N • G` is the image of an integer polynomial `U`.
- **How**: takes `N := ∏ d ∈ G.support, (G.coeff d).den`. For each `d` it shows `N * G.coeff d` is an integer using `Finset.dvd_prod_of_mem` and `Rat.den_mul_eq_num` (and `notMem_support_iff` off the support). It then `choose`s those integers `c d`, sets `U := ∑ d ∈ G.support, monomial d (c d)`, and checks coefficients using `coeff_map`, `coeff_sum`, `coeff_smul`, `coeff_monomial` and `Finset.sum_ite_eq'`. Positivity comes from `Finset.prod_pos` and `Rat.den_pos`.
- **Hypotheses**: none. Base rings are fixed to ℤ ⊂ ℚ, and the multiplier must be a positive natural number.
- **Uses from project**: `[]`
- **Used by**: `Roth.exists_primitive_smul_eq` (Roth/Separation.lean:410, `obtain ⟨N, U0, hN, hU0⟩ := exists_nat_smul_eq_map G`). There are no other uses (`grep -rn exists_nat_smul_eq_map Roth/`).
- **Visibility**: public
- **Lines**: 378–400, proof length 19 lines
- **Notes**: Section `Integrality` of Separation.lean. The docstring cites clean.tex §2, proof of Lemma 2 ("by clearing denominators"). The only consumer needs `N ≠ 0` as a rational, not `N : ℕ` with `0 < N`.

## Junk check (Step 8)
- Used anywhere? Yes, once (Separation.lean:410).
- Wrapper of 1–2 mathlib calls? No. The proof is a 19-line direct construction. The general localization form is a 4-line composition of `IsLocalization.surj` with the instance `MvPolynomial.isLocalization` (evidence (3)), or about 8 lines from `IsLocalization.exist_integer_multiples` and `MvPolynomial.mem_range_map_iff_coeffs_subset` (evidence (2)).
- Does mathlib have it? Only the univariate version: `IsLocalization.integerNormalization` / `integerNormalization_spec` (Mathlib/RingTheory/Localization/Integral.lean:50,53). Mathlib has no `MvPolynomial` analogue, and no ℤ/ℚ-specific multivariate statement.
- Too specific? Yes. ℤ → ℚ with a positive natural `N` is a specialisation of "S is a localization of R at M". The call site works with any `b ∈ ℤ⁰`, as compiled in evidence (5).
- Well-chosen? The content is right but the form is over-specialised.
- Conclusion: `REPLACE`. Use the general localization lemma (evidence (2)) at Separation.lean:410, then delete this theorem.

## Mathlibable assessment (Step 9)

Pre-filter: the declaration is not private. The name does not end in `_aux`, and the docstring does not start with internal/auxiliary. Step 8 gave REPLACE, not REMOVE. The qualified name is absent from mathlib (grepping `exists_nat_smul_eq_map` over `.lake/packages/mathlib/Mathlib/` finds nothing). It is not a glue lemma about any project definition, so the full workflow follows.

### Baseline (Phase 0)
- lake build:               clean (per brief; the evidence file importing `Roth.Separation` elaborates)
- decl `Roth.exists_nat_smul_eq_map`: resolved at Roth/Separation.lean:380
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable: the determinant `F = U(x_1, …, x_{p-1}) V(x_p)` (Lemma 2), including the integrality/primitivity rescaling.

### Statement (Phase 1)

`Roth.exists_nat_smul_eq_map` is a theorem. For every polynomial `G ∈ ℚ[x_s : s ∈ σ]` there is a positive integer `N` such that `N·G ∈ ℤ[x_s : s ∈ σ]`. In other words, the denominators of a rational polynomial can be cleared by one positive integer.

Variables / typeclasses involved (Lean side):
- `σ : Type*`: the set of variables (arbitrary, possibly infinite).
- `G : MvPolynomial σ ℚ`: the rational polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `∃ N ∈ ℤ_{>0}, N·G ∈ image of ℤ[x] → ℚ[x]`.

Conclusion (Lean): `∃ (N : ℕ) (U : MvPolynomial σ ℤ), 0 < N ∧ map (Int.castRingHom ℚ) U = (N : ℚ) • G`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a standard helper fact ("clear denominators") used once in the proof of Lemma 2. It is not a main result and not a named theorem.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 19
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | clearing denominators polynomial rational coefficients integer multiple primitive polynomial | yes | multiply a ℚ-polynomial by the lcm of its coefficient denominators to get a ℤ-polynomial | CoCoA `ClearDenom` manual, rational-root lecture notes, and mathlib `DenomsClearable` (which is about evaluation, a different notion) |
| 2 | WebSearch (general form) | polynomial ring localization S^{-1}A[x] = S^{-1}(A[x]) every polynomial over localization is s^{-1} times polynomial over A | yes | `(S⁻¹A)[x] ≅ S⁻¹(A[x])`, localized at constants in S, so every element is `s⁻¹ f` with `f ∈ A[x]` | Yale HW exercise, Wikipedia "Localization of a ring". This is the most general standard form, for any localization and any number of variables. |
| 3 | WebSearch (named-after / mathlib aliases) | Mathlib IsLocalization integerNormalization MvPolynomial multivariate | yes | univariate `IsLocalization.integerNormalization(_spec)`; multivariate `MvPolynomial.isLocalization` instance | found no multivariate `integerNormalization`, which Phase 5 confirms |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: the `ask_chatgpt_math` MCP is not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "clearing"/"denominator" | yes | clean.tex:420–422: "Choose g∈ℚ^× so that U=gG is an integral primitive polynomial, by clearing denominators and then dividing by the gcd of its coefficients" | the source only needs a nonzero rational `g`, not a positive integer |
| 6 | nLab | localization of a commutative ring / polynomial ring | partial | localization commutes with base change, so `S⁻¹A ⊗_A A[x] = S⁻¹A[x]` (reached through #2 sources) | gives no finer statement than #2 |
| 7 | nCatLab | n/a | n/a | — | this is elementary commutative algebra, not a categorical concept |
| 8 | Stacks Project | localization commutes with polynomial rings (Algebra, localization chapter) | partial | `S⁻¹(A[x]) = (S⁻¹A)[x]` appears as a basic property of localization (base change) | same content as #2 |
| 9 | MathOverflow / Math.SE | (covered by #1/#2) | no | — | too elementary to be discussed separately |
| 10 | recent arXiv | n/a | n/a | — | classical fact. #2 (SageMath localization docs) shows CAS systems implement the same `s⁻¹ f` normal form. |

### Literature summary (Phase 3)

Concept identified as: clearing denominators; equivalently, polynomial rings commute with localization.
Sources agree on the standard form: yes.
Most general standard form: if `S = M⁻¹R`, then every `G ∈ S[x_σ]` can be written as `b⁻¹·U` with `b ∈ M` and `U ∈ R[x_σ]`, so `b·G` lies in the image of `R[x_σ]`.
Generality dimensions where the literature varies:
  - base ring: ℤ ⊂ ℚ → domain ⊂ fraction field → arbitrary localization `R → M⁻¹R`. The most general is an arbitrary localization.
  - number of variables: one → any set σ. The proof is uniform.
  - multiplier: lcm of denominators (canonical over ℤ) versus some element of `M`. The general statement only promises some `b ∈ M`.
Disagreement with the literature: none. The project form is the ℤ/ℚ specialisation with a positive representative.

### Generality analysis — `Roth.exists_nat_smul_eq_map`

Literature-standard form (from Phase 3): `[CommRing R] [CommRing S] [Algebra R S] (M : Submonoid R) [IsLocalization M S] (G : MvPolynomial σ S) : ∃ b ∈ M, ∃ U : MvPolynomial σ R, map (algebraMap R S) U = (b : R) • G`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | base rings ℤ → ℚ | concrete `Int.castRingHom ℚ` | any `IsLocalization M S` | yes | verified: evidence (2) and (3) prove the general statement |
| 2 | multiplier `N : ℕ`, `0 < N` | positive natural | `b ∈ M` | yes | positivity is specific to ℤ and recoverable by a sign fix (evidence (4)); the only call site needs just `b ≠ 0` (evidence (5)) |
| 3 | `σ : Type*` | arbitrary | arbitrary | no | already general |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 2 (verified: evidence (2) compiles for an arbitrary localization; evidence (4) recovers the project statement from it; evidence (5) recompiles the only consumer against the general form)
Proposed restatement (if STRICTLY NARROWER):

```lean
theorem MvPolynomial.exists_smul_eq_map_of_isLocalization {σ R S : Type*} [CommRing R]
    [CommRing S] [Algebra R S] (M : Submonoid R) [IsLocalization M S] (G : MvPolynomial σ S) :
    ∃ b ∈ M, ∃ U : MvPolynomial σ R, map (algebraMap R S) U = (b : R) • G
```

Cost of restatement: CHEAP. The proofs in evidence (2) and (3) compile.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | yes | ℤ/ℚ replaced by `[IsLocalization M S]` | all localizations (fraction fields, `Localization.Away`, number rings) |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | yes | the existence follows from the universal property / instance `MvPolynomial.isLocalization` via `IsLocalization.surj` | it parallels `Polynomial.isLocalization` + `integerNormalization_spec` |
| 4 | Set-with-predicate to bundled? | partial | could be phrased as `b • G ∈ (map (algebraMap R S)).range` or via `coeffsIn` | `mem_range_map_iff_coeffs_subset` |
| 5 | Field/specific to (semi)ring? | yes | ℚ to any `CommRing S` localizing `R` | same as row 1 |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general structure? | yes | `N : ℕ` to `b ∈ M` | same as row 1 |
| 8 | Concrete-via-abstract? | yes | the proof uses only that each rational is `num/den` with `den` in a multiplicative set, i.e. the localization property | the abstract form is the proposed restatement |
| 9 | False-generalisation guard | no | the general statement specialises back exactly (evidence (4)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.exists_smul_eq_map_of_isLocalization`, as above.
  - Cost: CHEAP
  - Mathlib downstream this enables: the MvPolynomial counterpart of `IsLocalization.integerNormalization_spec`. It applies to Gauss-lemma style arguments for `MvPolynomial` over `FractionRing R` and to number-field integrality, without users having to unfold the `algebraMvPolynomial` local instance.
  - Real mathematical improvement: one statement covers all localizations and any variable set, instead of an ℤ/ℚ coefficient-by-coefficient construction.

### Proof strategy — `Roth.exists_nat_smul_eq_map`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals/submodules | yes | point-free via `mem_range_map_iff_coeffs_subset` plus `IsLocalization.exist_integer_multiples`, instead of building `U` monomial by monomial | CHEAP (evidence (2)) |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | `IsLocalization.surj` on `MvPolynomial.isLocalization` | CHEAP (evidence (3)) |
| 5 | missing mathlib helpers | yes | the MvPolynomial analogue of `integerNormalization_spec` is missing | this proposal |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: compose `IsLocalization.exist_integer_multiples` with `MvPolynomial.mem_range_map_iff_coeffs_subset` (or `IsLocalization.surj` on `MvPolynomial.isLocalization`).
  - Cost: CHEAP
  - Missing mathlib API (if any): `MvPolynomial.exists_smul_eq_map_of_isLocalization`.
  - Would refactoring make the proof strictly shorter / cleaner? yes (about 8 lines general versus 19 lines specific).

### Diamond / defeq risk

n/a: declaration kind is theorem. (Evidence (2) deliberately avoids the `algebraMvPolynomial` local instance, so no instance is exported.)

### Mathlib search-status: `Roth.exists_nat_smul_eq_map`

[A] Lean-Finder       "clearing denominators of a rational multivariate polynomial: some positive integer multiple lifts to an integer polynomial"   hits: `DenomsClearable` family (evaluation, a different notion), `IsLocalization.integerNormalization` (univariate only)
[B] Loogle            `MvPolynomial.map (algebraMap _ _) _ = _ • _`   no hits
[C] LeanSearch        "multivariate polynomial over field of fractions times a nonzero denominator has integer coefficients"   hits: `IsFractionRing.isInteger_of_isUnit_den`, `MvPolynomial.isIntegral_iff_isIntegral_coeff` (neither is the statement)
[D] Grep mathlib src  `integerNormalization`, `exist_integer_multiples`, `mem_range_map_iff_coeffs_subset`, `IsInteger` with MvPolynomial, `isLocalization` in RingTheory/MvPolynomial   found `IsLocalization.integerNormalization(_spec)` Localization/Integral.lean:50,53 (Polynomial only); `IsLocalization.exist_integer_multiples` Localization/Integer.lean:87; `MvPolynomial.mem_range_map_iff_coeffs_subset` Algebra/MvPolynomial/Eval.lean:506; `MvPolynomial.isLocalization` RingTheory/MvPolynomial/Localization.lean:44; `Rat.isFractionRing` Localization/FractionRing.lean:66. No `IsInteger`/`integerNormalization` statement for MvPolynomial.
[E] Name pattern      `exists_nat_smul_eq_map`, `exists_smul_eq_map`, `integerNormalization`   no MvPolynomial hit (grep over Mathlib/)

Searched for both:
  - the user's current form (ℤ/ℚ, positive `N`): absent.
  - the literature-standard form (arbitrary localization, MvPolynomial): absent as a lemma. It is present only implicitly through the instance `MvPolynomial.isLocalization` and present for `Polynomial`.

Concluded: found building blocks (`IsLocalization.exist_integer_multiples`, `MvPolynomial.mem_range_map_iff_coeffs_subset`, `MvPolynomial.isLocalization` + `IsLocalization.surj`, `Rat.isFractionRing`). There is a partial match for the univariate case (`IsLocalization.integerNormalization_spec`). The multivariate statement is not in mathlib.

### Normal-form check — `Roth.exists_nat_smul_eq_map`

Equivalent formalisms: (a) `∃ N U, 0 < N ∧ map U = N • G` (project); (b) `∃ b ∈ M, ∃ U, map (algebraMap R S) U = b • G` (mirrors `integerNormalization_spec`); (c) `∃ b ∈ M, b • G ∈ Set.range (map (algebraMap R S))`.
Does mathlib already have a canonical form? yes for Polynomial, namely shape (b) (`integerNormalization_spec : ∃ b ∈ M, map (algebraMap R S) (integerNormalization M p) = b • p`).
Is our statement stated against the canonical form? NO. It should follow shape (b).
RHS convention respected? yes, in shape (b) (`map … = b • G`).

### Syntactic generality — `Roth.exists_nat_smul_eq_map`

Alternative restatements attempted:
- (b) with an existential `U` (evidence (2)/(3)).
- (b′) a def `MvPolynomial.integerNormalization` plus a spec lemma, mirroring Polynomial. This is heavier and a candidate for review discussion.
Chosen restatement: (b).
Justification: an existential is what consumers destructure (`obtain`), as in evidence (5). A def is only needed if a support lemma like `integerNormalization_support` is wanted.

### Superfluous-argument audit — `Roth.exists_nat_smul_eq_map`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `G : MvPolynomial σ ℚ` | yes | data; ℚ is over-specific |
| 2 | `0 < N` with `N : ℕ` (conclusion strength) | no (for consumers) | the only call site uses only `(N : ℚ) ≠ 0` (evidence (5)) |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (to shape (b), the `integerNormalization_spec` shape)
Syntactic generality: RESTATE (existential over `b ∈ M`, arbitrary localization)
Superfluous arguments: 1 to drop (the positivity / ℕ-valuedness of the multiplier)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.exists_nat_smul_eq_map`

Internal use count: 0 outside the declaring file; 1 inside Roth/Separation.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:410 | `exists_primitive_smul_eq`: `obtain ⟨N, U0, hN, hU0⟩ := exists_nat_smul_eq_map G` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `exists_nat_smul_eq_map`?):
  - (none). Grepping `Roth/` for `\.den`, `integerNormalization` and `exist_integer_multiples` finds only this proof.

### Composition check (Phase 6)

Can `Roth.exists_nat_smul_eq_map` be derived from mathlib in ≤3 chained calls?

Attempt 1: `IsLocalization.surj (M.map C) G` on the instance `MvPolynomial.isLocalization`, followed by `ext; simp [Algebra.smul_def, mul_comm]`
  - Mathlib decls used: `MvPolynomial.isLocalization`, `MvPolynomial.algebraMvPolynomial` (local instance), `IsLocalization.surj`
  - Result: succeeds for the general form (evidence (3)), but it needs a local instance plus an `ext`/`simp` coefficient computation, so it is a proof rather than a composition.
Attempt 2: `IsLocalization.exist_integer_multiples M G.support G.coeff` with `mem_range_map_iff_coeffs_subset`
  - Result: succeeds (evidence (2)), in about 8 lines with a coefficient-membership argument.
Attempt 3: recover the exact project form (`N : ℕ`, `0 < N`) at ℤ → ℚ
  - Result: succeeds from attempt 2 plus a sign fix (`C b.sign * U`, `Int.sign_mul_self_eq_abs`, `Nat.cast_natAbs`; evidence (4)). That adds about 6 more lines.

Conclusion: NOT-COMPOSABLE (within ≤3 calls). Each route is a short proof, not a chain of calls, and the missing piece is a named MvPolynomial gap.

## Verdict: `Roth.exists_nat_smul_eq_map`

Verdict: YES-but-generalise-first

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the standard form is "polynomials over `M⁻¹R` are `b⁻¹ U` with `b ∈ M`" (`(S⁻¹A)[x] ≅ S⁻¹(A[x])`). The source needs only a nonzero rational multiplier.
- Generality analysis (Phase 4): STRICTLY NARROWER (ℤ/ℚ, positive `N`). The general form is verified in evidence (2)/(3), and the specialisation back in evidence (4).
- Mathlib search (Phase 5): the univariate `IsLocalization.integerNormalization_spec` exists; no multivariate lemma exists; building blocks are found.
- Composition check (Phase 6): NOT-COMPOSABLE in ≤3 calls (4–8 line proofs).

**Rationale:**
Mathlib's clearing-denominators API is univariate. `IsLocalization.integerNormalization` and `integerNormalization_spec` (Mathlib/RingTheory/Localization/Integral.lean) state exactly this fact for `Polynomial S`. `IsLocalization.exist_integer_multiples` does it for finite families of elements. For `MvPolynomial` there is only the instance `MvPolynomial.isLocalization` (Mathlib/RingTheory/MvPolynomial/Localization.lean:44). Using it requires the non-global `algebraMvPolynomial` instance and a coefficient computation (evidence (3)). Users therefore re-derive the fact by hand, as this project does in 19 lines with `Rat.den` products.

The project statement is the ℤ → ℚ, positive-`N` instance of the general statement `∃ b ∈ M, ∃ U, map (algebraMap R S) U = b • G`. The general statement compiles (evidence (2)), the exact project form follows from it with a sign fix (evidence (4)), and the sole consumer `exists_primitive_smul_eq` recompiles against the general form directly with `b : ℤ`, `b ≠ 0` (evidence (5)). The right contribution is therefore the MvPolynomial analogue of `integerNormalization_spec` for an arbitrary localization, not the ℤ/ℚ statement. Q9 holds: the general statement specialises back exactly.

Reason for the generalisation: LITERATURE-WEAKENING (ℤ/ℚ → arbitrary localization; `N : ℕ, 0 < N` → `b ∈ M`), plus MODERN-IDIOM (it is stated as a localization fact, parallel to the Polynomial API).
Proposed restatement:
```lean
theorem MvPolynomial.exists_smul_eq_map_of_isLocalization {σ R S : Type*} [CommRing R]
    [CommRing S] [Algebra R S] (M : Submonoid R) [IsLocalization M S] (G : MvPolynomial σ S) :
    ∃ b ∈ M, ∃ U : MvPolynomial σ R, map (algebraMap R S) U = (b : R) • G := by
  classical
  obtain ⟨b, hb⟩ := IsLocalization.exist_integer_multiples M G.support G.coeff
  refine ⟨b, b.2, ?_⟩
  have hmem : (b : R) • G ∈ Set.range (map (algebraMap R S)) := by
    rw [mem_range_map_iff_coeffs_subset]
    intro q hq
    simp only [Finset.mem_coe, coeffs, Finset.mem_image] at hq
    obtain ⟨d, hd, rfl⟩ := hq
    rw [coeff_smul]
    exact hb d (support_smul hd)
  exact hmem
```
Estimated cost of regeneralisation: CHEAP (already compiled).
Mathlib downstream this enables:
  - It is the MvPolynomial counterpart of `IsLocalization.integerNormalization_spec`, which Gauss-lemma arguments use (`Polynomial.IsPrimitive` / GaussLemma.lean). It is a prerequisite for primitive-part/content arguments for `MvPolynomial σ (FractionRing R)`.
  - Users no longer need the local `algebraMvPolynomial` instance to get at `MvPolynomial.isLocalization`.
Proposed mathlib location: `Mathlib/RingTheory/MvPolynomial/Localization.lean` (next to `MvPolynomial.isLocalization`). An optional follow-up is a def `MvPolynomial.integerNormalization` with a support lemma, if reviewers prefer the Polynomial-style API.
Call sites in our project (from Phase 6.0): 1.
Refactor plan: at Roth/Separation.lean:410 (`exists_primitive_smul_eq`), replace the `obtain` with `obtain ⟨N, hNM, U0, hU0⟩ := exists_smul_eq_map_of_isLocalization (nonZeroDivisors ℤ) G`. Then add `have hN : (N : ℚ) ≠ 0 := by exact_mod_cast nonZeroDivisors.ne_zero hNM` and `replace hU0 : map (Int.castRingHom ℚ) U0 = (N : ℚ) • G := by rw [Int.cast_smul_eq_zsmul]; exact hU0`, and change `hN.ne'` to `hN` (two places). The whole proof compiles as evidence (5). Until the lemma lands in mathlib, keep the general lemma project-local in place of `exists_nat_smul_eq_map`.
Next action: run `/generalise Roth.exists_nat_smul_eq_map` with the target above, replace the project lemma by the general one, update the call site, then open a mathlib PR "feat(RingTheory/MvPolynomial/Localization): clear denominators of multivariate polynomials". There are no related YES verdicts in this batch to group with. `exists_primitive_smul_eq` could follow as a GCD-domain generalisation in a later PR.

---

## Next step

Replace `exists_nat_smul_eq_map` with the general `exists_smul_eq_map_of_isLocalization` (evidence (2)), adapt Separation.lean:410 as in evidence (5), and upstream the general lemma to Mathlib/RingTheory/MvPolynomial/Localization.lean.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.exists_nat_smul_eq_map/compose.lean` (imports `Roth.Separation`, `Mathlib.RingTheory.MvPolynomial.Localization`, `Mathlib.RingTheory.Localization.Integral`). After one `lake env lean` run (about 39 s; its errors were fixed), the final version was checked with `lean_diagnostic_messages`: 0 errors.
  - (0) `#check @Roth.exists_nat_smul_eq_map`
  - (1) `#check @IsLocalization.integerNormalization_spec` (univariate mathlib analogue)
  - (2) `exists_smul_eq_map_of_isLocalization`: the general form, from `exist_integer_multiples` and `mem_range_map_iff_coeffs_subset`
  - (3) the same general form from `IsLocalization.surj` on `MvPolynomial.isLocalization`
  - (4) the exact project statement recovered from (2) at ℤ → ℚ with a sign fix
  - (5) `exists_primitive_smul_eq'`: the sole consumer, reproved against (2)
- Searches: 3 WebSearch queries (recorded above). Loogle returned no hits. Lean-Finder and LeanSearch returned only the univariate `integerNormalization` and unrelated integrality lemmas. A mathlib grep confirmed there is no MvPolynomial clearing-denominators lemma. ChatGPT MCP was n/a (not configured).
