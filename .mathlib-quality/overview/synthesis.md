# Project-wide synthesis (Steps 3–8 and the Recommended Action Plan)

Inputs: the 293 per-declaration reports in `.mathlib-quality/overview/mathlibable/`, the
digest `.mathlib-quality/overview/digest.md`, the `import Roth.*` lines of `Roth/*.lean`, and
direct reading of the source for every duplication pair in the table below. Paths of the form
`evidence/<Decl>/…` are relative to `.mathlib-quality/overview/`. Paths of the form
`mathlibable/<Decl>.md` are the per-declaration reports.

## Executive Summary

The project is a complete, sorry-free Lean 4 formalisation of Roth's theorem (mathlib v4.34.0):
for an irrational real algebraic `α` and `κ > 2`, only finitely many rationals `h/q` satisfy
`|α - h/q| < q^{-κ}`. It is stated as `Roth.roth` over the project set `Roth.approxSet`, as
`Roth.roth_rat` in mathlib's den-form vocabulary, and as the lean-eval harness theorem
`LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`. The development has 13 files,
4,855 lines and 293 declarations (28 defs, 191 theorems, 74 lemmas; 215 public, 78 private).
It follows the classical route. First come general algebraic tools: multivariate Hasse
derivatives (`Roth/HasseDeriv.lean`), multivariate Taylor translation (`Roth/Taylor.lean`), the
n-ary and generalised Wronskians with Roth's Lemma 1 (`Roth/Wronskian.lean`,
`Roth/GenWronskian.lean`), an ℓ¹ coefficient norm (`Roth/CoeffNorm.lean`), and box and weight
combinatorics (`Roth/Box.lean`, `Roth/Lattice.lean`). Next come the Roth-specific layers: the
index (`Roth/Index.lean`), Lemma 2 on the separation of variables (`Roth/Separation.lean`),
`Θ` with Lemmas 5–7 (`Roth/Theta.lean`), and the main Lemma 9 (`Roth/MainLemma.lean`). The
last layer is the endgame (`Roth/Main.lean`, `Roth/LeanEval.lean`).

Key findings:
1. **The general layer is a good source of mathlib PRs.** It fills documented mathlib gaps:
   there is no multivariate Hasse derivative and no `MvPolynomial.taylor`, the n-ary Wronskian
   is an explicit TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean`, and the ℓ¹ norm is a
   TODO in `Mathlib/Analysis/Polynomial/Norm.lean`. Almost all of it is
   YES-but-generalise-first. The proofs carry over verbatim to `CommSemiring`, `CommRing` or
   `SeminormedCommRing` once the `Field K` and `ℤ` specialisations are dropped, and all of these
   generalisations were compiled in the evidence files.
2. **Several definitions duplicate mathlib.** `Roth.box` is `Finset.Iic`. `Roth.weight` and
   `Roth.kroneckerExp` are `Finsupp.weight`. `Roth.kroneckerExp_injOn` is `Behrend.map_injOn`.
   `Roth.diag` is `aeval (fun _ ↦ X)`. `Roth.coeffNone` and its coefficient lemmas are the
   `optionEquivLeft` API. `Roth.exists_sum_mul_eq_gcd` is `Finset.gcd_eq_sum_mul`.
   `Roth.approxSet` is the content of `LiouvilleWith`.
3. **There is a small amount of dead or duplicated code.** Steps 5 and 8 found 8 REMOVE,
   10 REPLACE and 4 INLINE items. They also found verbatim duplicated proof bodies
   (`indexSet_bddAbove`/`Θ_le_card`, the two Wronskian vanishing lemmas, the
   `optionEquivLeft (rename some Q) = C Q` step) and about 25 superfluous hypotheses.

Top priorities:
- Delete the dead code. This needs your sign-off, because an earlier cleanup kept the public
  API on your instruction.
- Drop the superfluous hypotheses.
- Rebase `box`, `weight` and `kroneckerExp` on mathlib.
- Then open the upstream PR series in dependency order: `Finsupp.choose` →
  `MvPolynomial.hasseDeriv` → `MvPolynomial.taylor` → ℓ¹ norm → n-ary Wronskian → weighted
  substitution → generalised Wronskian.

Whether the Roth-specific internals (index, `Θ`, Lemmas 2 and 5–9) should ever go to mathlib
is a policy question for you. It covers most of the 36 BORDERLINE verdicts.

**Final verdict counts (293 declarations):** 11 YES-add-as-is (+6 INHERITED), 77
YES-but-generalise-first (+2 INHERITED), 12 NO-mathlib-has-it, 61 NO-composable-from-mathlib
(+2 INHERITED), 36 BORDERLINE-needs-human, 86 pre-filtered SKIP. The SKIPs are 78 private
helpers plus 8 public declarations marked junk REMOVE. Step 8 junk: 8 REMOVE, 10 REPLACE,
4 INLINE, 271 KEEP.

## Cross-File Dependencies

### Import graph (from the `import Roth.*` lines)

```
HasseDeriv ─┬─────────────► Taylor ◄──── Box ──┬──► Lattice ─────────────┐
            │                  │                │                         │
            │                  ▼                │                         │
            │               Index ◄─────────────┤                         │
            │                                   │                         │
            ├──────────────► CoeffNorm ◄────────┘                         │
            │                  │                                          │
Wronskian ──┴► GenWronskian    │                                          │
                     │         │                                          │
                     └──► Separation ◄─ CoeffNorm                         │
                               │                                          │
              Theta ◄── CoeffNorm, Index, Separation                      │
                │                                                         │
                └──────────────► MainLemma ◄──────────────────────────────┘
                                     │
                                     ▼
                                   Main ──► LeanEval
```

Edges written out:
- `Taylor` ← `Box`, `HasseDeriv`
- `CoeffNorm` ← `Box`, `HasseDeriv`
- `GenWronskian` ← `HasseDeriv`, `Wronskian`
- `Lattice` ← `Box`
- `Index` ← `Box`, `Taylor`
- `Separation` ← `CoeffNorm`, `GenWronskian`
- `Theta` ← `CoeffNorm`, `Index`, `Separation`
- `MainLemma` ← `Lattice`, `Theta`
- `Main` ← `MainLemma`
- `LeanEval` ← `Main`

`Roth.lean` imports all 12 `Roth/*` library files; `LeanEval` is not among them. `HasseDeriv`,
`Box` and `Wronskian` import only mathlib.

### Layering

| Layer | Files (decls) | Content | Upstream status |
|---|---|---|---|
| 0: general algebra, mathlib-only imports | `HasseDeriv` (25), `Wronskian` (13), `Box` (14) | Hasse derivative, n-ary Wronskian, box and weight | `HasseDeriv` and `Wronskian` are mathlib PR material; `Box` should be replaced by mathlib |
| 1: general algebra on top of layer 0 | `Taylor` (22), `CoeffNorm` (26), `GenWronskian` (19), `Lattice` (13) | Taylor translation, ℓ¹ norm, Kronecker substitution, Lemma 1, Lemma 8 | Mostly mathlib PR material; `Lattice` is Roth-specific |
| 2: Roth machinery | `Index` (19), `Separation` (27) | index, Lemma 2 | Mixed: small general lemmas plus Roth internals |
| 3: Roth estimates | `Theta` (50), `MainLemma` (38) | `Θ`, Lemmas 5–7, Lemma 9 | Roth-specific (BORDERLINE or NO) |
| 4: endgame | `Main` (23), `LeanEval` (4) | reduction, parameter choice, `roth`, harness | Headline theorems; LiouvilleWith form is the mathlib target |

### Notable cross-file usage (tallied from the digest's "Used by" fields)

- **`Roth/HasseDeriv.lean` is the backbone.** Its declarations are used in 7 other files:
  Separation (7 decls), Taylor (5), CoeffNorm (5), Index (5), MainLemma (4), GenWronskian (3)
  and Theta (1). `MvPolynomial.hasseDeriv` alone has about 60 occurrences, and
  `MvPolynomial.hasseDeriv_map` is used at MainLemma.lean:409,489,492,495, Theta.lean:524,580
  and Separation.lean:533.
- **`Roth/Box.lean` is used in 7 files:** Index (7), Lattice (7), MainLemma (5), Theta (5),
  CoeffNorm (4), Main (3) and Taylor (2). This is why the `box`→`Finset.Iic` and
  `weight`→`Finsupp.weight` refactors touch many call sites. The sites are listed in
  `mathlibable/Roth.box.md` and `mathlibable/Roth.weight.md`.
- **`Roth/Taylor.lean` → Index (10 decls), Main (3).** `coeff_taylor` is the bridge on which
  the whole index API rests (Index.lean:64,153,158).
- **`Roth/Index.lean` → Theta (10 decls), MainLemma (3), Main (1).**
- **`Roth/CoeffNorm.lean` → MainLemma (7 decls), Separation (1), Theta (1).**
  `abs_coeff_det_hasseDeriv_le` (Lemma 3) is consumed at Theta.lean:475.
- **`Roth/Separation.lean` → Theta (6 decls).** `exists_det_eq_mul` (Lemma 2) feeds
  `index_le_lem6`.
- **`Roth/Wronskian.lean` → GenWronskian (3), Separation (2). `Roth/GenWronskian.lean` →
  Separation (2).** `exists_genWronskian_ne_zero` (Lemma 1) has a single consumer:
  Separation.lean:524.
- **`Roth/Lattice.lean` → MainLemma (1).** Only `card_filter_weight_le` (Lemma 8) leaves the
  file, at MainLemma.lean:574.
- **`Roth/Theta.lean` → MainLemma (3)** (`Θ`, `index_le_Θ`, `Θ_lt`).
  **`Roth/MainLemma.lean` → Main (8)** (`main_lemma`, `gam`/`lam`/`eta`, `mainCoeffBound`,
  `three_small_factors`, `sqrt_lt_floor`, `four_lt_rpow`, `eta_lt_gam_iff`).
  **`Roth/Main.lean` → LeanEval (4)** (`approxSet`, `approxSet_den_le_finite`,
  `eventually_div_rpow_lt`, `roth`).

Structural consequence: everything that is upstreamable sits in layers 0–1, plus a few small
lemmas in `Separation`, `Theta` (rational root theorem), `MainLemma` (`modByMonic` bound,
box-family count) and `Main` (multivariate Liouville bound). These can be extracted without
touching layers 2–4.

## Mathlib API Audit

### Definitions to replace with mathlib

1. **`def Roth.box` → `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`** (junk REPLACE,
   NO-mathlib-has-it).
   - Current: `Fintype.piFinset`-based finset of multi-indices bounded by `r`.
   - Mathlib: the interval in the locally finite order on `σ →₀ ℕ`. Membership is
     `Finset.mem_Iic.trans Finsupp.le_def`. The cardinality is `Finsupp.card_Iic` plus
     `Nat.card_Iic` (and `Finset.prod_subset`). Both were verified in
     `evidence/Roth.box/box_eq_Iic.lean`.
   - **Action:** redefine `Roth.box r := Finset.Iic (Finsupp.equivFunOnFinite.symm r)`, keeping
     the name. Reprove `mem_box` and `card_box` as above, and keep `card_le_card_box`
     (`card_le_card` + `mem_Iic` + `card_box`). Add a `piFinset` bridge for the single unfolding
     site CoeffNorm.lean:216 (`sum_box_prod_pow_le_aux`). Call sites are in Taylor.lean:199–219,
     CoeffNorm.lean:215–236, Main.lean:392–405, MainLemma.lean:570–616 and Lattice.lean.
     `eq_sum_box_hasseDeriv` and `eval_eq_sum_box` should then be restated over `Finset.Iic`
     (`mathlibable/MvPolynomial.eq_sum_box_hasseDeriv.md`).
2. **`def Roth.weight` → `Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹)`** (junk REPLACE).
   - Verified equal for all `r`, including `r j = 0` (`evidence/Roth.weight/`). After the
     change, `weight_zero` and `weight_add` become the generic `map_zero` and `map_add`,
     `weight_single` becomes `Finsupp.weight_single`, and `weight_mapDomain` becomes
     `Finsupp.linearCombination_mapDomain` (with no injectivity).
   - **Action:** redefine with a bridge `weight_eq_sum`. Delete `weight_zero` (covered by simp
     `map_zero`). Replace `weight_add` by `map_add` at Index.lean:114, Theta.lean:391 and
     Lattice.lean:155. Repoint the unfolding sites Index.lean:133,245,249, Theta.lean:500,502
     and Main.lean:366 at the bridge. `weight_nonneg` becomes
     `Finsupp.sum_nonneg fun j _ ↦ nsmul_nonneg (by positivity) _`.
     `weight_eq_finsuppWeight_div` (Index.lean:130) becomes a statement relating two
     `Finsupp.weight`s.
3. **`def Roth.kroneckerExp` → `Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))`**
   (junk REPLACE).
   - Verified as a function equality. After reindexing along `equivFin` it is
     `Behrend.map k`.
   - **Action:** replace it in `kronecker_monomial` (GenWronskian.lean:60–62),
     `kroneckerExp_injOn` (l.69–82) and `coeff_kronecker` (l.88–97). See also item 4 and the
     weighted-substitution cluster under Generalization Opportunities.
4. **`theorem Roth.kroneckerExp_injOn` → `Behrend.map_injOn ∘ (· ∘ e.symm)`** (junk REPLACE).
   - **Action:** replace the 12-line `Nat.ofDigits` proof by the 3-line
     `Set.InjOn.comp` composition, importing
     `Mathlib.Combinatorics.Additive.AP.Three.Behrend`. Drop the superfluous `hk : 1 < k`,
     which also removes `hk` from `coeff_kronecker`, `kronecker_eq_zero_iff` and
     `linearIndependent_kronecker`. Evidence: `evidence/Roth.kroneckerExp_injOn/`.
5. **`def Roth.diag` = `MvPolynomial.aeval (fun _ ↦ Polynomial.X)`** (NO-composable, KEEP).
   - **Action:** keep the name, but optionally generalise it to `CommSemiring R` and bundle it
     as an `AlgHom`. Then `diag_sub` is `map_sub` (REPLACE), `eval_diag` is `comp_aeval_apply`
     plus `aeval_X` (REMOVE, already inlined at MainLemma.lean:409–410), and `natDegree_diag_le`
     is `MvPolynomial.aeval_natDegree_le` with `n = 1` (needs
     `import Mathlib.RingTheory.Polynomial.Basic`).
6. **`def Roth.coeffNone` = `(optionEquivLeft R τ P).coeff ν`** (rfl; NO-composable, KEEP as an
   abbreviation).
   - **Action:** re-aim the downstream lemmas at the `optionEquivLeft` API.
     `coeff_coeffNone` is `optionEquivLeft_coeff_coeff` with `d.optionElim ν` (REPLACE).
     `eq_mapDomain_some_add_single` is `Finsupp.optionElim_some` (REPLACE); its single use at
     Separation.lean:107 closes with `(optionEquivLeft_coeff_some_coeff_none R τ e P).symm`.
     `eq_sum_X_none_pow_mul_coeffNone` is `optionEquivLeft_symm_apply` plus
     `Polynomial.eval₂_eq_sum_range'` (INLINE at Separation.lean:335).
     `degreeOf_coeffNone_le` is the missing mathlib lemma `degreeOf_coeff_optionEquivLeft`
     (YES-add-as-is, REPLACE locally since it has no callers).
7. **`def Roth.approxSet` vs `LiouvilleWith`** (NO-composable, KEEP).
   - The mathlib notion carrying the same content is `LiouvilleWith`; its module docstring
     already names Thue–Siegel–Roth. A compiled bridge shows that, for irrational `α`,
     `Roth.roth` is equivalent to "no `LiouvilleWith p α` for `p > 2`"
     (`evidence/Roth.approxSet/liouvilleWith_bridge.lean`).
   - **Action:** keep `approxSet` as the paper's eq. (1). Add the compiled wrappers
     `IsAlgebraic.not_liouvilleWith` and `LiouvilleWith.transcendental` to `Roth/Main.lean` now
     (`evidence/Roth.roth/`). `Roth.reduction` in LiouvilleWith form is just `natDenominator`
     plus `LiouvilleWith.nat_mul` (`evidence/Roth.reduction/liouvilleWith_reduction.lean`).
     `IsDiophantine` is equivalent to `Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x`
     (`evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/`).
8. **`def Roth.index` vs `MvPowerSeries.weightedOrder`** (BORDERLINE).
   - For positive `r`, `index P α r = (weightedOrder w (taylor α P)).toNat / ∏ r` with
     `w j = ∏ r / r j`. This is `Roth.index_eq_weightedOrder_div`, and its `hP` is superfluous.
   - **Action:** keep the real-valued index. Reprove `index_prod` via
     `MvPowerSeries.weightedOrder_prod` (`evidence/Roth.index_prod/hyps_and_alt.lean`, needs
     `Mathlib.Data.ENat.BigOperators`). `index_neg` is REMOVE because
     `MvPowerSeries.weightedOrder_neg` and `index_C_mul` with `c = -1` already cover it. The
     other `index_*` API is listed under Moral Duplications.
9. **`def Roth.RSet`** (NO-composable). Its degree clause is exactly
   `MvPolynomial.degreesLE ℤ σ r.toMultiset` (compiled).
   - **Action:** note the `degreesLE` bridge in the docstring; no call-site change.
10. **`def Roth.boxFamily`** (NO-composable). It is `MvPolynomial.restrictSupport ℤ {d | d ≤ r}`
    intersected with the coefficient box `Icc 0 B`. Mathlib has the univariate analogue
    `Polynomial.boxPoly`/`ncard_boxPoly` (Mathlib/NumberTheory/MahlerMeasure.lean).
    - **Action:** optionally restate the body via `restrictSupport`. Upstream the general
      finite/ncard lemmas (Generalization Opportunities, cluster 9).
11. **`def Roth.normOne`** is the ℓ¹ coefficient norm, which mathlib lacks (it is listed as a
    TODO in `Mathlib/Analysis/Polynomial/Norm.lean`).
    - **Action:** generalise to `MvPolynomial.l1Norm` over `SeminormedCommRing`
      (`evidence/Roth.normOne/generalise_seminormedring.lean`). Keep `Roth.normOne` as the
      `R = ℤ` abbreviation via `Int.norm_eq_abs`.

### API choice improvements

1. **Statements over `Field K` or `ℤ` → `CommRing`/`CommSemiring`/`SeminormedCommRing`.**
   - The Wronskian files (`wronskian`, `wronskianMatrix`, `genWronskian`, `det_sum_rows`,
     `det_hasseDeriv_separated`) can move to `CommRing`. The dependence lemmas can move to
     `IsDomain`, and the independence lemmas to `IsDomain + CharZero`. All were verified, with
     necessity counterexamples over `ZMod 4`, `ZMod 2` and `ℚ×ℚ`.
   - `derivative_aeval` can move to any `Derivation`, and `diag`/`diag_eq_sum` to
     `CommSemiring`. The CoeffNorm lemmas can move to `SeminormedCommRing`.
   - `degreeOf_rename_mul_aeval` and `degreeOf_none_rename_mul_aeval` can move to
     `CommSemiring + NoZeroDivisors`.
   - **Action:** apply locally at least where the change is mechanical; it is required before
     any upstream PR.
2. **Box and `Fintype` hypotheses → support or `Finsupp.degree` forms.**
   - `hasseCoeff_le_two_pow` → `choose_le_two_pow_degree` (no `Fintype`, no `r`).
   - `normOne_hasseDeriv_le` → a `2^totalDegree` form.
   - `eq_sum_box_hasseDeriv` and `eval_eq_sum_box` → support-sum or superset forms.
   - **Action:** add the general form and derive the current one in two lines
     (`evidence/MvPolynomial.hasseCoeff_le_two_pow/`,
     `evidence/MvPolynomial.eq_sum_box_hasseDeriv/`).
3. **Weak inequalities → sharp or equality forms.**
   - `degreeOf_taylor_le` → `@[simp] degreeOf_taylor` (an equality, compiled in
     `evidence/MvPolynomial.degreeOf_taylor_le/variants.lean`).
   - `degreeOf_hasseDeriv_le` → `degreeOf j P - d j`.
   - **Action:** keep the current lemmas as `.le` corollaries.
4. **Pointwise statements → operator forms**, as in mathlib's univariate design.
   - `hasseDeriv_hasseDeriv` → `hasseDeriv_comp` using `∘ₗ` and `•`, plus the disjoint
     variant.
   - `pderiv_hasseDeriv` → `hasseDeriv_single_one` + composition.
   - `taylor_neg_taylor` → `taylorEquiv`.
   - Verified in `evidence/MvPolynomial.hasseDeriv_hasseDeriv/variants.lean` and siblings.
5. **Non-canonical index spellings → `a.optionElim b`.** `coeff_coeffNone`,
   `coeff_rename_mul_aeval`, `hasseDeriv_rename_mul_aeval` and `det_hasseDeriv_separated`
   index by `a.mapDomain some + single none b`.
   - **Action:** restate them at `a.optionElim b`, mathlib's canonical form for
     `optionEquivLeft_coeff_coeff`. Update Theta.lean:480,486 and Separation.lean:353,476.
6. **`∃ Q₀ : ℕ, ∀ q > Q₀` → filters.** `eventually_div_rpow_lt`, `exists_delta_bound` and
   `exists_delta` are hand-rolled eventually-statements.
   - **Action (optional):** restate them as `∀ᶠ x in atTop` or `∀ᶠ δ in 𝓝[≥] 0`, combined by
     `filter_upwards` (`evidence/Roth.eventually_div_rpow_lt/`,
     `evidence/Roth.exists_delta_bound/`).

### Hand-rolled patterns to replace

| Pattern | Location | Mathlib replacement | Action |
|---|---|---|---|
| Base-`k` digit injectivity via `Nat.ofDigits` | `kroneckerExp_injOn` (GenWronskian.lean:69–82) | `Behrend.map_injOn` | replace (item 4 above) |
| ℤ Bézout on a finset | `exists_sum_mul_eq_gcd` (Separation.lean:374) | `Finset.gcd_eq_sum_mul` | use at Separation.lean:446, delete (compiled) |
| Denominator clearing for ℤ→ℚ `MvPolynomial` | `exists_nat_smul_eq_map` (Separation.lean:380) | new `MvPolynomial.exists_smul_eq_map_of_isLocalization` | upstream, use at :410, delete |
| `natDenominator` by hand | `exists_nat_mul_isIntegral` (Main.lean:62) | `Algebra.natDenominator`, `isIntegral_natDenominator_smul` | INLINE at Main.lean:121 |
| `minpoly` padding | `exists_monic_aeval_eq_zero` (Main.lean:142) | `minpoly ℤ α * X ^ 2` term | INLINE at Main.lean:415 |
| Dependent-choice selection | `exists_approximants` (Main.lean:256) | `exists_seq_of_forall_finset_exists` | optional reproof (compiled) |
| `log 2 < 3/4` via the exp quadratic | `four_lt_rpow` (MainLemma.lean:122) | `Real.log_two_lt_d9` | golf |
| Finite fractions in a bounded set | `approxSet_den_le_finite` (Main.lean:73) | `Int.tendsto_coe_cofinite` + `Finite.biUnion` | optional shorter proof (`evidence/Roth.approxSet_den_le_finite/alt_proof.lean`) |
| Applied `toMvPolynomial_eq_rename_comp` | `aeval_X_eq_rename` (Separation.lean:137) | `Polynomial.toMvPolynomial_eq_rename_comp` | keep as a rewrite lemma or rewrite the 5 sites; docstring note |
| Integrality from gcd 1 | `exists_int_eq_of_gcd_eq_one` (Separation.lean:443) | `Submodule.mem_of_span_top_of_smul_mem` | optional reproof (compiled) |
| `sum_range_reflect` rewrite | `sum_inv_le` (Lattice.lean:47) | `Finset.sum_flip` | optional golf |
| `sqrt` arithmetic | `sqrt_one_sub_inv_lt` (Lattice.lean:29) | `Real.sqrt_one_add_le` | optional reproof, weaken `2 ≤ m` to `1 ≤ m` |
| Final `toMvPolynomial` step | `mapped_det_ne_zero_aux` (Theta.lean:528–529) | `map_ne_zero_iff _ (toMvPolynomial_injective none)` | golf (checked with `lean_multi_attempt`) |
| `divModByMonicAux` unfolding | `exists_norm_coeff_reduction_aux` (MainLemma.lean:212) | `Polynomial.modByMonic_eq_of_dvd_sub` | optional golf |
| One-variable `coeff_uniqueAlgEquiv_symm` | Separation.lean:169 | `MvPolynomial.coeff_uniqueAlgEquiv_symm` | REMOVE (callers already cite mathlib) |

## Moral Duplications

### Pairwise comparison table

Every pair below was checked against the source. "Verified" means I read both bodies in
`Roth/*.lean` for this synthesis; other rows rely on the cited report.

| Decl A | Decl B | Same statement? | Same proof? | Verdict |
|---|---|---|---|---|
| `Roth.wronskian_eq_zero_of_not_linearIndependent` (Wronskian.lean:65) | `Roth.genWronskian_eq_zero_of_not_linearIndependent` (GenWronskian.lean:41) | no: univariate `D^(μ)` vs multivariate `Δ_{D μ}`; the former is the special case of the latter (verified) | yes, verbatim: `Fintype.not_linearIndependent_iff` + `Matrix.exists_mulVec_eq_zero_iff` + `congrArg hasseDeriv` (verified) | UNIFY via abstract `det_linearMap_eq_zero_of_not_linearIndependent` (`evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/weaken_and_abstract.lean`) |
| `Roth.indexSet_bddAbove` (Theta.lean:87) | `Roth.Θ_le_card` (Theta.lean:114) | no: `BddAbove` vs `sSup ≤ card` | yes: identical 3-line `index_le_card` body over the `rintro` pattern (verified) | FACTOR into `card_mem_upperBounds_indexSet` (`evidence/Roth.indexSet_bddAbove/refactor.lean`) |
| `Roth.coeff_X_none_pow_mul_rename` (private, Separation.lean:64) | `Roth.coeff_rename_mul_aeval` (Separation.lean:123) | no: monomial `X none ^ ν` vs general `V(X none)`; A is the case `V = X^ν` up to index spelling | shared step: both prove `optionEquivLeft R τ (rename some Q) = C Q` from the same `h : … .comp (rename some) = CAlgHom` (verified) | EXTRACT `optionEquivLeft_rename_some` (upstream to Mathlib/Algebra/MvPolynomial/Equiv.lean); A disappears when `eq_sum_X_none_pow_mul_coeffNone` is inlined |
| `Roth.coeff_coeffNone` (Separation.lean:85) | `MvPolynomial.optionEquivLeft_coeff_coeff` | yes, up to `d.mapDomain some + single none ν` vs `d.optionElim ν` | yes: rfl after unfolding | REPLACE (delete A) |
| `Roth.eq_mapDomain_some_add_single` (Separation.lean:57) | `Finsupp.optionElim_some` | yes (non-canonical spelling) | n/a | REPLACE (delete A) |
| `Roth.exists_sum_mul_eq_gcd` (Separation.lean:374) | `Finset.gcd_eq_sum_mul` | yes (sides swapped, ℤ only) | yes: `simpa using` that lemma | REPLACE (delete A) |
| `Roth.coeff_uniqueAlgEquiv_symm` (Separation.lean:169) | `MvPolynomial.coeff_uniqueAlgEquiv_symm` | A is the `d = single default n` case and reuses the same short name | yes | REMOVE A |
| `Roth.eval_diag` (CoeffNorm.lean:193) | inline `comp_aeval_apply` + `aeval_X` at MainLemma.lean:409–410 | yes | yes | REMOVE A (dead since 96928fd) |
| `Roth.diag_sub` (CoeffNorm.lean:199) | `map_sub` | yes once `diag` is an `AlgHom` | yes | REPLACE (optional delete; one site MainLemma.lean:408) |
| `Roth.kroneckerExp` (GenWronskian.lean:57) | `Finsupp.weight (fun j ↦ k ^ equivFin σ j)` / `Behrend.map` | yes (function equality) | n/a | REPLACE |
| `Roth.kroneckerExp_injOn` (GenWronskian.lean:69) | `Behrend.map_injOn` (and mathlib's private `NoetherNormalization.sum_r_mul_ne`) | yes after reindexing; A has a superfluous `1 < k` | different (A uses `Nat.ofDigits`) | REPLACE A; upstream a deduplicated weighted-substitution injectivity |
| `Roth.weight` + `weight_zero`/`weight_add`/`weight_single`/`weight_mapDomain` (Box.lean:71–127) | `Finsupp.weight` + `map_zero`/`map_add`/`Finsupp.weight_single`/`Finsupp.linearCombination_mapDomain` | yes (B form of `weight_mapDomain` drops `hf`) | n/a | REPLACE def; delete `weight_zero`; `weight_add` → `map_add` |
| `Roth.box` + `mem_box`/`card_box` (Box.lean:47–57) | `Finset.Iic` + `Finset.mem_Iic`/`Finsupp.card_Iic` | yes | n/a | REPLACE def, reprove API |
| `Roth.weight_le_degree_div` (Box.lean:118) | `Roth.weight_le_delta_aux` (private, Theta.lean:494) | no: integer lower bound `m ≤ r j` vs real ratio `r none ≤ δ r (some j)`; same idea (weight ≤ degree / min r) (verified) | similar: both `Finsupp.degree_eq_sum` + `Finset.sum_div` + termwise bound (verified) | REMOVE A (unused); or generalise A to a real lower bound `0 < c ≤ r j` and derive B with `c = r none / δ` |
| `MvPolynomial.hasseDeriv_hasseDeriv` (HasseDeriv.lean:175) | `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` (HasseDeriv.lean:185) | B is the special case where the binomial factor is 1 | B is proved from A | KEEP both (mathlib ships both); add operator forms |
| `MvPolynomial.hasseCoeff_mul_hasseCoeff` (private, :153) | `MvPolynomial.hasseCoeff_mul_succ` (private, :191) | B is a specialisation of A (`e = single j 1`) | B is `simpa using A …` | KEEP; publish as `Finsupp.choose_mul` and a `choose_succ_right_eq` analogue in the `Finsupp.choose` PR |
| `MvPolynomial.hasseDeriv_single_aeval_X` (:253) | `MvPolynomial.uniqueAlgEquiv_hasseDeriv` (:266) | no: both bridge multivariate to univariate Hasse derivatives, via `aeval (X j)` vs `uniqueAlgEquiv` | similar (monomial `simp`) (verified) | KEEP both; generalise both to arbitrary `d` (`evidence/MvPolynomial.hasseDeriv_single_aeval_X/bridge.lean`, `evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/bridge.lean`) |
| `Roth.abs_coeff_hasseDeriv_le` (CoeffNorm.lean:134) | `Roth.normOne_hasseDeriv_le` (CoeffNorm.lean:148) | no: pointwise coefficient vs ℓ¹ | shared core: `hasseCoeff_le_two_pow ∘ monomial_le_degreeOf ∘ hP` (verified) | KEEP both; derive both from pointwise `norm_coeff_hasseDeriv_le` over `SeminormedCommRing` |
| `Roth.degreeOf_rename_mul_aeval` (Separation.lean:197) | `Roth.degreeOf_none_rename_mul_aeval` (Separation.lean:213) | no (left factor vs right factor) | twin: both are `degreeOf_mul_eq` + a rename-degree-zero fact (verified) | KEEP both; extract `degreeOf_rename_eq_zero_of_notMem_range` and `degreeOf_mul_of_degreeOf_eq_zero_{left,right}` (upstream) |
| `Roth.index_le_weight` / `exists_weight_eq_index` / `le_index_iff` (Index.lean:69–85) | `MvPowerSeries.weightedOrder_le` / `exists_coeff_ne_zero_and_weightedOrder` / `le_weightedOrder` | analogous (ℝ-valued sInf vs ℕ∞-valued order of `taylor α P`) | no (`csInf` API vs order API) | KEEP (project def); reprove only if `index` is rebased on `weightedOrder` |
| `Roth.index_mul` / `index_prod` (Index.lean:162,175) | `MvPowerSeries.weightedOrder_mul` / `weightedOrder_prod` | yes, transported through `index_eq_weightedOrder_div` | `index_mul` already is; `index_prod` uses induction | KEEP `index_mul`; reprove `index_prod` via `weightedOrder_prod` |
| `Roth.index_neg` (Index.lean:190) | `Roth.index_C_mul` (Index.lean:195) with `c = -1`; `MvPowerSeries.weightedOrder_neg` | yes (special case) | different (one-line `support_neg`) | REMOVE A (unused) |
| `Roth.le_index_sum` (Index.lean:118) | `AddValuation.map_le_sum` | analogous ultrametric bound | no | KEEP |
| `Roth.exists_hasseDeriv_eval_ne_zero` (MainLemma.lean:454) | `Roth.exists_weight_eq_index` / contrapositive of `Roth.le_index_iff` | strict-cutoff restatement | yes: one `Exists.imp` | KEEP; move next to `exists_weight_eq_index` in Index.lean |
| `Roth.le_index_of_forall_eval_eq_zero` (MainLemma.lean:419) | `Roth.le_index_iff` | the box-restricted `.2` direction | `le_index_iff.2` + `hasseDeriv_eq_zero_of_degreeOf_lt` | KEEP; move next to `le_index_iff` in Index.lean |
| `Roth.normOne_*` (12 lemmas, CoeffNorm.lean:50–128) | generalised `MvPolynomial.l1Norm_*` over `SeminormedCommRing` | yes at `R = ℤ` via `Int.norm_eq_abs` | yes (verbatim, with `abs_mul` → `norm_mul_le`) | GENERALISE; keep ℤ forms as specialisations |
| `Roth.normOne_le_card_mul` (CoeffNorm.lean:113) | `Roth.weight_le_card` (Box.lean:103) | no | same one-call `Finset.sum_le_card_nsmul` pattern | KEEP (different objects) |
| `Roth.floor_sq_div_two_le_sum` (Theta.lean:289) | inline `hbound` in `mul_sq_div_three_le_sum_max_of_pos_aux` (Theta.lean:322) | no: `⌊a⌋²/2 ≤ ∑` vs sharper `a²/3 ≤ ∑` | same Gauss-sum skeleton (`Finset.sum_range_id_mul_two` + `sum_sub_distrib`) (verified) | REMOVE A (dead since 9bf5ca8) |
| `Roth.sq_div_three_lt_floor_sq_div_two` (Theta.lean:300) | same inline `hbound` | no; A was the second half of the old two-step route | n/a (one `nlinarith`) | REMOVE A (dead since 9bf5ca8) |
| `Roth.mul_div_two_le_sum_max_aux` (private, Theta.lean:304) | `Roth.mul_sq_div_three_le_sum_max_of_pos_aux` (private, Theta.lean:322) | no: cases `l ≤ θr` vs `θr < l` of `min_le_sum_max` | same Gauss-sum computation (`Finset.sum_range_id_mul_two`, `sum_sub_distrib`, `card_range`) (verified) | KEEP (genuine case split); optional shared Gauss-sum helper |
| `Roth.mul_sq_div_three_le_sum_max_aux` (private, Theta.lean:347) | `Roth.min_le_sum_max` (Theta.lean:362) | A is a case dispatcher whose `θr = l` branch is dead at the caller (verified) | A only dispatches | INLINE A into `min_le_sum_max` (`evidence/Roth.mul_sq_div_three_le_sum_max_aux/inline_into_min_le_sum_max.lean`) |
| `Roth.sqrt_lt_nat_floor_aux` (private, MainLemma.lean:104) | `Roth.sqrt_lt_floor` (MainLemma.lean:115) | A is the first conjunct of B | B is `⟨A, Nat.floor_le …⟩` (verified) | KEEP (B is the public form); A could be inlined |
| `Roth.two_lt_rpow_aux` (private, MainLemma.lean:156) | `Roth.four_lt_rpow` (MainLemma.lean:122) | no: different thresholds (`log 2 <` vs `3 ≤`) and conclusions (2 vs 4) | same skeleton: `hL`, `hq : 2 ≤ q₁`, `by_contra` + `nlinarith`, `Real.lt_rpow_of_log_lt` (verified) | possibly unify into `c < q₁^(δ r₁)` from `log c < δ² log q₁`; neither subsumes the other as stated |
| `Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul` (MainLemma.lean:433) | inline `have hq` in `theta_lt_eta_of_sq_log_bound_aux` (MainLemma.lean:681) | no: strict vs non-strict variant | n/a | REMOVE A (dead since 6c41716), or restate it non-strict and use it at l.681 |
| `hpow` and `0 < r₁` derivations in `exists_mem_RSet_le_index_of_log_bound_aux` (MainLemma.lean:625–637) | the same in `exists_auxiliary_polynomial_of_log_bound_aux` (MainLemma.lean:656–665) | yes (same identity `B^(1+3δ) = B·(B^δ)^3`, same `Finset.single_le_sum` argument) | yes (verified) | EXTRACT a private `mainCoeffBound_rpow_one_add_three_mul` and `pos_of_sum_le_mul` |
| `0 < δ` derivation in `theta_lt_eta_of_sq_log_bound_aux` (MainLemma.lean:679–680) | same in `exists_auxiliary_polynomial_with_index_gap_aux` (MainLemma.lean:709–710) | yes | yes (verified) | EXTRACT a private helper, or pass `0 < δ` down |
| `Roth.theta_denominators_one_lt_aux` (private, Theta.lean:833) | inline argument in `theta_scaled_unique_le_aux` (Theta.lean:752–757) | yes (`1 < q j`) | similar, entangled with `hr₂` | KEEP (per report, refactor not worth it) |
| `Roth.exists_delta_bound` (MainLemma.lean:77) | `Roth.exists_delta` (Main.lean:227) | no: B consumes A and adds eqs. (48)/(49) | both are continuity-at-0 arguments | optional joint restatement as `∀ᶠ δ in 𝓝[>] 0` bounds combined by `filter_upwards` |
| `Roth.roth_of_isIntegral` (Main.lean:547) | `Roth.roth` (Main.lean:573) | A is the strictly narrower algebraic-integer case | B = A ∘ `reduction` | KEEP (A is the paper's §7 theorem) |
| `Roth.roth` (Main.lean:573) | `Roth.roth_rat` (Main.lean:581) / `thueSiegelRoth` (LeanEval.lean:61) / `IsAlgebraic.not_liouvilleWith` (evidence) | equivalent reformulations | corollaries of `roth` | KEEP; drop `Irrational` from `roth` and `roth_rat`; add the LiouvilleWith form |
| `Roth.taylor_injective` (Taylor.lean:187) | `Roth.taylor_eq_zero_iff` (Taylor.lean:192) | B follows from A over `CommRing`; B also holds over `CommSemiring`, where A fails | B uses A | KEEP both; reprove B by top-degree coefficients over `CommSemiring` |
| `MvPolynomial.eq_sum_box_hasseDeriv` (Taylor.lean:197) | `MvPolynomial.eval_eq_sum_box` (Taylor.lean:217) | B is the evaluation of A | B uses A | KEEP; both become corollaries of support-sum forms |
| `Roth.wronskian_ne_zero_of_linearIndependent` (Wronskian.lean:205) | `Roth.exists_genWronskian_ne_zero` (GenWronskian.lean:254) | A is the univariate Lemma 1; B reduces to A via Kronecker substitution | B uses A | KEEP (dependency, not duplication) |

### Numbered list with actions

1. **Wronskian vanishing pair.** Prove the abstract
   `det_linearMap_eq_zero_of_not_linearIndependent`, which belongs in
   Mathlib/LinearAlgebra/Matrix/ToLinearEquiv.lean, then derive both
   `wronskian_eq_zero_of_not_linearIndependent` and
   `genWronskian_eq_zero_of_not_linearIndependent` from it in one line each.
2. **`indexSet_bddAbove` / `Θ_le_card`.** Add `card_mem_upperBounds_indexSet B q r`, make both
   lemmas one-liners as in `evidence/Roth.indexSet_bddAbove/refactor.lean`, and remove the
   spurious "If every `r j` is positive" from the `indexSet_bddAbove` docstring.
3. **`optionEquivLeft (rename some Q) = C Q`.** Extract it as `optionEquivLeft_rename_some`
   (with `optionEquivLeft_comp_rename_some`), use it in `coeff_rename_mul_aeval`, and inline
   `eq_sum_X_none_pow_mul_coeffNone`. Inlining orphans `coeff_X_none_pow_mul_rename` and
   `eq_mapDomain_some_add_single`; delete both.
4. **Mathlib duplicates.** Replace `coeff_coeffNone`, `eq_mapDomain_some_add_single`,
   `exists_sum_mul_eq_gcd`, `coeff_uniqueAlgEquiv_symm`, `eval_diag`, `diag_sub`, `kroneckerExp`,
   `kroneckerExp_injOn`, `box` and `weight` as listed under Junk / Removable.
5. **`weight_le_degree_div` / `weight_le_delta_aux`.** Delete `weight_le_degree_div`, which is
   unused. Only if you want a single lemma: generalise it to a real lower bound and derive
   `weight_le_delta_aux` from it.
6. **`min_le_sum_max` helpers.** Inline `mul_sq_div_three_le_sum_max_aux`. Delete the dead
   `floor_sq_div_two_le_sum` and `sq_div_three_lt_floor_sq_div_two`. Optionally factor the
   three Gauss-sum computations (in the remaining two private helpers and the old floor lemma)
   into one private `sum_range_sub_eq` helper.
7. **MainLemma bookkeeping duplicates.** Extract the `hpow` identity and the `0 < r₁` and
   `0 < δ` derivations into private helpers, removing the duplicated blocks at
   MainLemma.lean:625–637/656–665 and 679–680/709–710.
8. **`two_lt_rpow_aux` / `four_lt_rpow`.** Optionally merge them into one private
   `lt_rpow_of_log_lt_sq_mul_log` helper with a threshold parameter, and golf `hlog2` with
   `Real.log_two_lt_d9`.
9. **Hasse coefficient bound pair.** Add a pointwise `norm_coeff_hasseDeriv_le` and derive both
   `abs_coeff_hasseDeriv_le` and `normOne_hasseDeriv_le` from it.
10. **Twin degree lemmas.** Extract the three building blocks named in
    `mathlibable/Roth.degreeOf_rename_mul_aeval.md` and
    `mathlibable/Roth.degreeOf_none_rename_mul_aeval.md`, then prove each twin in two rewrites.
11. **`index_*` vs `weightedOrder`.** Keep the project API. Reprove `index_prod` via
    `weightedOrder_prod` and delete `index_neg`. Move `exists_hasseDeriv_eval_ne_zero` and
    `le_index_of_forall_eval_eq_zero` from MainLemma.lean into Index.lean next to their
    parents.

## Generalization Opportunities

All 77 YES-but-generalise-first verdicts (plus the 2 INHERITED ones) fall into the clusters
below. Difficulty is that recorded in the reports: "Low" means a compiled mechanical
restatement, "Medium" means new statements with compiled proofs, and "High" means a new proof
or a large dependency chain.

1. **`Finsupp.choose`: the multi-index binomial.** Difficulty: Low.
   - Members: `hasseCoeff`, `hasseCoeff_eq_zero_iff`, `hasseCoeff_eq_prod`,
     `hasseCoeff_le_two_pow`, and the private `hasseCoeff_mul_hasseCoeff` and
     `hasseCoeff_mul_succ`.
   - Generalisation: `Finsupp.choose k d` (in `Nat.choose` argument order) with
     `choose_ne_zero_iff`, `choose_pos_iff`, `choose_eq_prod_of_support_subset` (mirroring
     `Finsupp.multinomial_eq_of_support_subset`), `choose_le_two_pow_degree` (no `Fintype`, no
     box) and `choose_mul`.
   - Target: Mathlib/Data/Nat/Choose/Multinomial.lean or a new Mathlib/Data/Finsupp/Choose.lean.
   - Literature: standard multi-index notation.
2. **Multivariate Hasse derivative API.** Difficulty: Low–Medium; depends on cluster 1.
   - Members: `hasseDeriv` and its 17 public lemmas, plus `abs_coeff_hasseDeriv_le` and
     `hasseDeriv_rename_mul_aeval`.
   - Literature: DKSS method of multiplicities, nLab. Mathlib has only `Polynomial.hasseDeriv`
     and `LaurentSeries.hasseDeriv`.
   - New statements, all compiled in `evidence/MvPolynomial.*`:
     - `hasseDeriv_comp` and `hasseDeriv_comp_of_disjoint` (operator forms);
     - `hasseDeriv_single_one : hasseDeriv (single j 1) = pderiv j`;
     - sharp `degreeOf_hasseDeriv_le` (`≤ degreeOf j P - d j`) and `totalDegree_hasseDeriv_le`;
     - `hasseDeriv_eq_zero_of_forall_not_le`;
     - the Leibniz rule `hasseDeriv_mul` and `hasseDeriv_mul_of_hasseDeriv_eq_zero`;
     - `hasseDeriv_toMvPolynomial` for general `d`, and `uniqueAlgEquiv_hasseDeriv` for
       general `d`;
     - `iterate_pderiv_hasseDeriv` for general `d`;
     - `norm_coeff_hasseDeriv_le` over `SeminormedCommRing`;
     - `hasseDeriv_rename_inl_mul_rename_inr` (Sum form).
   - Also make `hasseDeriv_map` `@[simp]`, and ideally add an `MvPowerSeries` companion next
     to `MvPowerSeries.pderiv`.
   - Target: a new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean.
3. **`MvPolynomial.taylor` API.** Difficulty: Low; `coeff_taylor` depends on cluster 2.
   - Members: `taylor` and its 14 other public lemmas, plus `eq_sum_box_hasseDeriv`
     and `eval_eq_sum_box`.
   - Restatements:
     - `taylor_taylor : taylor α (taylor β P) = taylor (α + β) P`;
     - `@[simp] taylor_zero` with Pi zero;
     - `@[simp] map_taylor`, reoriented from `taylor_map`;
     - `taylorEquiv`, `taylor_neg_taylor` and `taylor_taylor_neg` with Pi negation;
     - `taylor_eq_zero` over `CommSemiring`;
     - `aeval_taylor` (with `eval_taylor` as a corollary);
     - `@[simp] degreeOf_taylor` (equality);
     - `sum_taylor_eq` and `eq_sum_hasseDeriv_of_subset`;
     - `eval_add_eq_sum_of_subset`;
     - the `uniqueAlgEquiv_taylor` bridge.
   - Target: a new Mathlib/Algebra/MvPolynomial/Taylor.lean. Mathlib precedent:
     `Polynomial.taylor`.
4. **n-ary (Hasse) Wronskian.** Difficulty: Low–Medium.
   - Members: `wronskianMatrix`, `wronskian`, `wronskian_eq_zero_of_not_linearIndependent`,
     `det_choose_eq`, `coeff_wronskian_of_natDegree_injective`,
     `wronskian_ne_zero_of_natDegree_injective`, `wronskian_update_sub_smul`,
     `linearIndependent_update_sub_smul`, `wronskian_ne_zero_of_linearIndependent` and
     `wronskian_eq_zero_iff`.
   - Generalisation: `[Semiring R]` or `[CommRing R]` for the definitions; `IsDomain` for the
     dependence direction; `IsDomain + CharZero` for independence, transferred via the fraction
     field. A char-free core takes the hypothesis "det of the binomial matrix ≠ 0".
   - Also needed: the change-of-basis lemma `W(φA) = det A · W(φ)` and an `l = 2` bridge to
     `Polynomial.wronskian`.
   - The name must not clash with the existing 2-ary `Polynomial.wronskian`, and
     `coeff_wronskian_of_natDegree_injective` should drop its misleading `_of_…` suffix.
   - Prerequisite small PRs:
     - `det_eval_descPochhammer` and `prod_factorial_mul_det_choose` in
       Mathlib/LinearAlgebra/Vandermonde.lean, replacing the private
       `of_eval_descPochhammer_eq_mul_of_choose`;
     - `coeff_prod_of_natDegree_le'` in Mathlib/Algebra/Polynomial/BigOperators.lean;
     - `linearIndependent_update_sub_smul_iff` in Mathlib/LinearAlgebra/LinearIndependent/Defs.lean.
   - Target: Mathlib/RingTheory/Polynomial/Wronskian.lean, which fills its TODO.
   - Literature: Bostan–Dumas Lemma 3 and Thm 2; Garcia–Voloch.
5. **Weighted (Kronecker) substitution.** Difficulty: Medium.
   - Members: `kronecker`, `kronecker_monomial`, `coeff_kronecker`, `kronecker_eq_zero_iff`,
     with `kroneckerExp`→`Finsupp.weight` and `linearIndependent_kronecker` as consumers.
   - Generalisation: `MvPolynomial.weightedSubst w := aeval (fun j ↦ X ^ w j)` over
     `CommSemiring`, with no `Fintype` and no `equivFin`, and exponents via `Finsupp.weight w`.
     Its API: `weightedSubst_monomial` (simp), `coeff_weightedSubst`,
     `coeff_weightedSubst_weight`, `weightedSubst_eq_zero_iff` and
     `injOn_weightedSubst_restrictSupport`. Drop `hk : 1 < k` throughout.
   - The base-`k` injectivity would deduplicate mathlib's private reproof in
     RingTheory/NoetherNormalization.
   - Target: Mathlib/Algebra/MvPolynomial/, next to Expand.lean.
6. **Generalised (Ostrowski–Roth) Wronskian and Lemma 1.** Difficulty: Medium–High; it depends
   on clusters 2, 4 and 5 and on `derivative_aeval`.
   - Members: `genWronskian`, `genWronskian_eq_zero_of_not_linearIndependent`,
     `exists_genWronskian_ne_zero`, `det_hasseDeriv_separated` and `derivative_aeval`.
   - Generalisation: `[CommRing R]`; Lemma 1 over `IsDomain + CharZero` with no `Finite σ`
     (via `rename`). `derivative_aeval` becomes `Derivation.map_mvPolynomial_aeval`. Ship
     `det_hasseDeriv_separated` at the `(D μ).optionElim ν` index.
   - The BORDERLINE `exists_hasseDeriv_kronecker_eq_sum` should become a general
     `Polynomial.hasseDeriv_aeval` chain rule. This needs a new Taylor-expansion proof.
   - Target: a new Mathlib/RingTheory/MvPolynomial/Wronskian.lean.
   - Literature: Roth 1955 Lemma 1; Schmidt LNM 785; Bostan–Dumas Thm 3.
7. **ℓ¹ coefficient norm (polynomial length).** Difficulty: Low.
   - Members: `normOne` and its 11 basic lemmas, `normOne_det_le`, `normOne_hasseDeriv_le`, plus
     `abs_coeff_diag_le`, `diag_eq_sum`, `abs_eval_le`, `geom_sum_le_one_add_pow` and
     `degreeOf_det_hasseDeriv_le`.
   - Generalisation: `MvPolynomial.l1Norm` over `[SeminormedCommRing R]`; `NormOneClass` for
     the product and determinant lemmas.
   - Related lemmas, all compiled in `evidence/Roth.normOne*`, `evidence/Roth.abs_eval_le/`,
     `evidence/Roth.diag_eq_sum/`, `evidence/Roth.geom_sum_le_one_add_pow/weaken.lean` and
     `evidence/Roth.degreeOf_det_hasseDeriv_le/`:
     - `Matrix.norm_det_le` (Mathlib/Analysis/Matrix/Normed.lean);
     - `MvPolynomial.aeval_X_pow_eq_sum`, `coeff_aeval_X` and `norm_coeff_aeval_X_le`;
     - `MvPolynomial.norm_eval_le_mul_prod_one_add_pow` (`NormedCommRing` + `NormOneClass`);
     - `geom_sum_le_one_add_pow` over an ordered semiring (Mathlib/Algebra/Order/Ring/GeomSum.lean);
     - `MvPolynomial.degreeOf_det_le_sum` (Mathlib/LinearAlgebra/Matrix/MvPolynomial.lean).
   - Target: Mathlib/Analysis/Polynomial/Norm.lean or a new
     Mathlib/Analysis/MvPolynomial/Norm.lean.
8. **Multivariate Gauss lemma pieces and the rational root theorem.** Difficulty: Medium.
   - Members: `exists_nat_smul_eq_map` (→ `MvPolynomial.exists_smul_eq_map_of_isLocalization`)
     and `exists_primitive_smul_eq` (→ `MvPolynomial.exists_eq_C_gcd_mul` and
     `exists_primitive_smul_eq_map` over a GCD domain with fraction field). Their target is
     Mathlib/RingTheory/MvPolynomial/Localization.lean or a new MvPolynomial/Content.lean.
   - Rational root theorem: `exists_eq_pow_mul_of_rootMultiplicity` and
     `pow_rootMultiplicity_le` become `pow_rootMultiplicity_dvd_of_isRelPrime` and
     `pow_rootMultiplicity_dvd_leadingCoeff` over a normalized-GCD domain, targeting
     Mathlib/RingTheory/Polynomial/GaussLemma.lean or RationalRoot.lean. The private
     `isPrimitive_linear` and `isPrimitive_pow` would become `isPrimitive_C_mul_X_sub_C` and
     `IsPrimitive.pow`.
   - The BORDERLINE `exists_int_factors` needs this content API first.
9. **Small general lemmas from the Roth layers.** Difficulty: Low.
   - Members, all compiled in their evidence directories:
     - `weight_eq_zero_iff` → `Finsupp.weight_eq_zero_iff_of_pos` (Mathlib/Data/Finsupp/Weight.lean);
     - `degreeOf_coeffNone_le` → `degreeOf_coeff_optionEquivLeft`;
     - `degreeOf_uniqueAlgEquiv_symm` and `natDegree_uniqueAlgEquiv`;
     - `coeff_rename_mul_aeval` → `optionEquivLeft_rename_some` + the coefficient lemma at
       `a.optionElim b`;
     - `degreeOf_rename_mul_aeval` and `degreeOf_none_rename_mul_aeval` → the three building
       blocks and `Polynomial.degreeOf_toMvPolynomial_self`;
     - `boxFamily_finite` and `ncard_boxFamily` → `MvPolynomial.finite_setOf_support_subset_coeff_mem`
       and `ncard_setOf_support_subset_coeff_mem`, refactoring `Polynomial.bUnion_roots_finite`
       and possibly `ncard_boxPoly`;
     - `norm_coeff_modByMonic_le` → `Polynomial.supNorm_modByMonic_le`;
     - `one_le_prod_pow_mul_abs_eval` → `MvPolynomial.one_le_prod_pow_mul_abs_eval_div`, the
       sibling of `one_le_pow_mul_abs_eval_div` (Mathlib/Algebra/Polynomial/DenomsClearable.lean).
10. **Roth's theorem headline forms via `LiouvilleWith`.** Difficulty: High; upstreaming them
    lands the whole 4.8k-line development.
    - Members: `roth`, `roth_rat` and `thueSiegelRoth`.
    - Mathlib form: `IsAlgebraic.not_liouvilleWith`, with no `Irrational` hypothesis, plus
      `LiouvilleWith.transcendental`, and `IsAlgebraic.finite_rat_abs_sub_lt_one_div_den_rpow`
      for `roth_rat`. All are compiled from `Roth.roth` in `evidence/Roth.roth/`,
      `evidence/Roth.roth_rat/` and
      `evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/`.
    - Target: a new Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean.
    - **Local action now:** add the wrappers and drop `Irrational` from `roth_rat` (`roth_rat'`
      is compiled). Keep `thueSiegelRoth` verbatim, since the harness fixes its statement.

## API Improvements

### Missing lemmas (would simplify multiple proofs)

1. **`card_mem_upperBounds_indexSet`.** It removes the duplicated body of `indexSet_bddAbove`
   and `Θ_le_card` (`evidence/Roth.indexSet_bddAbove/refactor.lean`).
2. **`optionEquivLeft_rename_some` and `optionEquivLeft_comp_rename_some`.** They replace the
   repeated `h : (optionEquivLeft R τ).toAlgHom.comp (rename some) = Polynomial.CAlgHom` blocks
   at Separation.lean:67–70 and :124–126 (`mathlibable/Roth.coeff_rename_mul_aeval.md`).
3. **A private `B^(1+3δ) = B · (B^δ)^3` lemma and a private `0 < r₁` lemma** from
   `hs : ∑ r ≤ m r₁`. They replace the duplicated `hpow` and `hr₁` blocks at
   MainLemma.lean:625–637 and :656–665 (`mathlibable/Roth.exists_mem_RSet_le_index_of_log_bound_aux.md`,
   `mathlibable/Roth.exists_auxiliary_polynomial_of_log_bound_aux.md`).
4. **A private `0 < δ` lemma from `2m+1 ≤ δ² log q`.** It replaces the duplicated blocks at
   MainLemma.lean:679–680 and :709–710 (`mathlibable/Roth.exists_auxiliary_polynomial_with_index_gap_aux.md`).
5. **`norm_coeff_hasseDeriv_le` (pointwise).** It feeds both `abs_coeff_hasseDeriv_le` and
   `normOne_hasseDeriv_le` (`mathlibable/Roth.abs_coeff_hasseDeriv_le.md`).
6. **`degreeOf_rename_eq_zero_of_notMem_range` and
   `degreeOf_mul_of_degreeOf_eq_zero_{left,right}`.** They serve both Separation twins
   (`evidence/Roth.degreeOf_rename_mul_aeval/weaken.lean`).
7. **`hasseDeriv_monomial_of_not_le` and `hasseDeriv_one`.** These are optional companions for
   the Hasse API (`mathlibable/MvPolynomial.hasseDeriv_C.md`).
8. **`MvPolynomial.taylorEquiv` with `coe_taylorEquiv` and `taylorEquiv_symm`.** They make
   `taylor_injective` the one-liner `(taylorEquiv α).injective`
   (`mathlibable/MvPolynomial.taylor_neg_taylor.md`).
9. **A shared Gauss-sum helper**
   `∑_{ν<n+1} (a - ν) = (n+1) a - n(n+1)/2`. Its pattern is repeated in
   `mul_div_two_le_sum_max_aux`, `mul_sq_div_three_le_sum_max_of_pos_aux` and the dead
   `floor_sq_div_two_le_sum` (verified in Theta.lean:289–345).

### Missing simp attributes and simp-normal restatements

- `MvPolynomial.hasseDeriv_map` → add `@[simp]`, as for the univariate lemma; this is safe per
  `evidence/MvPolynomial.hasseDeriv_map/`.
- `MvPolynomial.taylor_zero` → restate with Pi `0`. The current `fun`-form LHS does not fire
  on `taylor 0 P` (`mathlibable/MvPolynomial.taylor_zero.md`).
- `MvPolynomial.taylor_map` → reorient as `@[simp] map_taylor` with an import-robust
  `simp [taylor, map_bind₁]` proof.
- `MvPolynomial.degreeOf_taylor_le` → add `@[simp] degreeOf_taylor` (equality).
- `MvPolynomial.taylor_injective` → add the simp companion `taylor_inj`.
- `MvPolynomial.hasseCoeff_eq_zero_iff` → state the simp-friendly `choose_ne_zero_iff` as the
  primary lemma.

### Superfluous hypotheses (drop; each compiled in the cited evidence)

| Declaration | Hypothesis | Evidence | Call sites to update |
|---|---|---|---|
| `Roth.weight_mapDomain` | `hf : Injective f` | `evidence/Roth.weight_mapDomain/` (4) | Index.lean:219, Theta.lean:391, Lattice.lean:155 |
| `Roth.kroneckerExp_injOn`, `coeff_kronecker`, `kronecker_eq_zero_iff`, `linearIndependent_kronecker` | `hk : 1 < k` | `evidence/Roth.kroneckerExp_injOn/`, `evidence/Roth.coeff_kronecker/`, `evidence/Roth.kronecker_eq_zero_iff/`, `evidence/Roth.linearIndependent_kronecker/` | GenWronskian.lean:97,111,123,263 |
| `Roth.abs_coeff_det_hasseDeriv_le` | `hB0` (follows from `hB 0`) | `evidence/Roth.abs_coeff_det_hasseDeriv_le/weaken.lean` | Theta.lean:475 |
| `Roth.index_eq_weightedOrder_div` | `hP` | `evidence/Roth.index_eq_weightedOrder_div/` | Index.lean:164–165 (three rewrites in `index_mul`) |
| `Roth.index_le_card` | `hP` | `evidence/Roth.index_le_card/hyps.lean` | Theta.lean:91,117 (drops `map_ne_zero_iff` arguments) |
| `Roth.index_unique` | `hP` | `evidence/Roth.index_unique/hyps.lean` | Theta.lean:242 |
| `Roth.Θ_mono` | `hB : 1 ≤ B` | `evidence/Roth.Θ_mono/` (`Θ_mono'`) | Theta.lean:758,790 |
| `Roth.index_det_le` | the `R ≠ 0` part of `hR` | `evidence/Roth.index_det_le/weaken.lean` | Theta.lean:578 |
| `Roth.index_le_lem6` | `_hq` | `evidence/Roth.index_le_lem6/weaken_hq.lean` | Theta.lean:600 |
| `Roth.Θ_option_le` | `hq`, `hB` | `evidence/Roth.Θ_option_le/weaken_hq.lean` | Theta.lean:920 |
| `Roth.theta_phi_lt_aux` (private) | `hanti`, `hδ1` (derivable from `hδ`, `hratio`) | `mathlibable/Roth.theta_phi_lt_aux.md` | Theta.lean:930 |
| `Roth.exists_m` | middle conjunct `4 n √m < m` (follows from `16 n² < m`) | `evidence/Roth.exists_m/` (1) | Main.lean:419 |
| `Roth.roth`, `Roth.roth_rat` | `Irrational α` | `evidence/Roth.roth/`, `evidence/Roth.roth_rat/` (`roth_rat'`) | Main.lean:583; LeanEval keeps it (harness-fixed) |
| `LeanEval…isDiophantine_iff` | `hx` | `evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/` (`isDiophantine_iff'`) | LeanEval.lean:63 |
| `Roth.sum_max_sub_le_index_det` | `hD` and `hδ` merge into `∀ μ, weight (r ∘ some) (D μ) ≤ δ` | `evidence/Roth.sum_max_sub_le_index_det/restate.lean` | Theta.lean:576 |
| `Roth.exists_separated_representation` | two degree-bound conclusions (discarded by the only caller) | `mathlibable/Roth.exists_separated_representation.md` | Separation.lean:521 |
| `Roth.degreeOf_rename_mul_aeval`, `degreeOf_none_rename_mul_aeval` | `CommRing + IsDomain` → `CommSemiring + NoZeroDivisors` | `evidence/Roth.degreeOf_rename_mul_aeval/weaken.lean`, `evidence/Roth.degreeOf_none_rename_mul_aeval/weaken.lean` | Separation.lean:554,557 |
| `Roth.sqrt_one_sub_inv_lt` | `2 ≤ m` → `1 ≤ m` | `evidence/Roth.sqrt_one_sub_inv_lt/experiments.lean` | none |
| `Roth.inv_add_inv_le`, `Roth.sum_inv_le` (private) | `2 < lam` → `1 < lam` | `evidence/Roth.inv_add_inv_le/weaken.lean`, `evidence/Roth.sum_inv_le/weaken.lean` | none required |
| `Roth.sum_natDegree_update_lt` | weaker hypotheses (`hp`, `hne`, any `Fintype`, `DivisionRing`) | `evidence/Roth.sum_natDegree_update_lt/` | Wronskian.lean:213 |
| `Roth.theta_prefix_lt_aux` (private) | `hanti` → a single inequality | `mathlibable/Roth.theta_prefix_lt_aux.md` | Theta.lean:886 |
| `Roth.exists_genWronskian_ne_zero` | `[Finite σ]` (and `Field` → domain) | `evidence/Roth.exists_genWronskian_ne_zero/` | Separation.lean:524 |
| `MvPolynomial.hasseCoeff_le_two_pow` | `[Fintype σ]`, box `r` | `evidence/MvPolynomial.hasseCoeff_le_two_pow/` | CoeffNorm.lean:140,157 (derive the current form) |
| `MvPolynomial.uniqueAlgEquiv_hasseDeriv` | `single default n` → general `d` | `evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/bridge.lean` | Index.lean:239 (drops the `Finsupp.unique_single` rewrite) |

**Action:** apply the rows for public project lemmas in one pass. Each is a statement-level
change with compiled evidence, and the call-site updates are listed. Keep `thueSiegelRoth`
unchanged, because its statement is fixed by the lean-eval harness.

### Docstring and naming fixes

- `Roth.indexSet_bddAbove`: remove "If every `r j` is positive"; the statement has no such
  hypothesis.
- `Roth.min_le_sum_max`: remove the leading "If `θ r_p > 10`"; the statement has no such
  hypothesis.
- `Roth.coeff_wronskian_of_natDegree_injective`: rename it, because the statement has no
  hypotheses (suggested: `coeff_wronskian_sum_natDegree_sub`).
- `Roth.Θ`: document the junk value `Θ = 0` for `B < 1`.
- `Roth.RSet`: note the `degreesLE` bridge.
- `Roth.aeval_X_eq_rename`: say that it is the applied form of
  `Polynomial.toMvPolynomial_eq_rename_comp`.
- `Roth.boxFamily_eq_image_finsupp_aux`: turn the plain comment at MainLemma.lean:278 into a
  docstring and drop the redundant `classical` (l.284).
- `Roth.exists_approximants`: note that `δ` needs no hypothesis (compiled with `δ = -1`).
- Private Lemma 7 helpers (`theta_scaled_unique_le_aux`, `theta_delta_succ_lt_aux`,
  `theta_prefix_lt_aux`, `theta_lt_base_aux`, `theta_denominators_one_lt_aux`,
  `theta_phi_lt_aux`, `theta_lt_succ_aux`, `theta_lt_of_large_delta_aux`) and Lemma 9 helpers
  (`mul_card_filter_weight_le_aux`, `exists_mem_RSet_le_index_of_rpow_bound_aux`,
  `theta_lt_eta_of_sq_log_bound_aux`, `exists_auxiliary_polynomial_with_index_gap_aux`): add
  one-line docstrings citing the clean.tex lines named in their reports.

### Visibility

These BORDERLINE or KEEP numeric lemmas have one private caller each. The reports suggest
making them `private`: `sum_inv_lt`, `index_det_le`, `index_le_lem6`, `lem6M_lt`,
`lem7_Φ_bound`, `lem7_numeric`, `pigeonhole_count` and `exists_ne_modByMonic_eq`.

**Action:** make them private only if you lift the earlier keep-public-API instruction for
them. Otherwise leave them public.

## Junk / Removable

Verified with `grep '^junk:'` over the reports: 8 REMOVE, 10 REPLACE and 4 INLINE.

### REMOVE (8)

You previously instructed that public API should be kept: "lack of callers is not
authorization to delete". The reports for `eval_diag`, `floor_sq_div_two_le_sum`,
`sq_div_three_lt_floor_sq_div_two` and `sum_range_le_sum_of_injective` say explicitly that
deletion needs your sign-off. The same applies to every public REMOVE below.

1. **`Roth.weight_le_degree_div`** (Box.lean:118).
   - Reason: unused; `weight_le_delta_aux` is the live variant. Its content is a single `gcongr`.
   - Action: delete Box.lean:113–122. Alternatively, generalise it to a real lower bound and
     derive `weight_le_delta_aux` from it.
2. **`Roth.sum_range_le_sum_of_injective`** (Wronskian.lean:107).
   - Reason: unused; it specialises `Finset.sum_range_le_sum`.
   - Action: delete Wronskian.lean:105–114, then check whether
     `import Mathlib.Algebra.Order.Group.Int.Sum` is still needed. The alternative is to make
     it `private`.
3. **`Roth.eval_diag`** (CoeffNorm.lean:193).
   - Reason: unused since 96928fd; it is `comp_aeval_apply` + `aeval_X`, already inline at
     MainLemma.lean:409–410.
   - Action: delete CoeffNorm.lean:190–195. This needs your sign-off.
4. **`Roth.index_neg`** (Index.lean:190).
   - Reason: unused; it is the `c = -1` case of `index_C_mul`.
   - Action: delete Index.lean:189–192.
5. **`Roth.coeff_uniqueAlgEquiv_symm`** (Separation.lean:169).
   - Reason: unused; it is an instance of `MvPolynomial.coeff_uniqueAlgEquiv_symm` and shadows
     that name.
   - Action: delete Separation.lean:169–171.
6. **`Roth.floor_sq_div_two_le_sum`** (Theta.lean:289).
   - Reason: dead since 9bf5ca8.
   - Action: delete Theta.lean:287–296, or make it `private` if you want blueprint fidelity to
     the source's first FACT. This needs your sign-off.
7. **`Roth.sq_div_three_lt_floor_sq_div_two`** (Theta.lean:300).
   - Reason: dead since 9bf5ca8.
   - Action: delete Theta.lean:298–302 together with item 6, or make it `private`. This needs
     your sign-off.
8. **`Roth.mul_two_mul_add_one_div_lt_of_le_sq_mul`** (MainLemma.lean:433).
   - Reason: dead since 6c41716.
   - Action: delete MainLemma.lean:426–443. Alternatively, restate it non-strict and use it
     for `have hq` at MainLemma.lean:681.

### REPLACE (10)

1. **`Roth.box`** (Box.lean:47) → `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`. Keep the
   name and reprove `mem_box`/`card_box` (Mathlib API Audit, item 1).
2. **`Roth.weight`** (Box.lean:71) → `Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹)`, with a
   `weight_eq_sum` bridge (Mathlib API Audit, item 2).
3. **`Roth.diag_sub`** (CoeffNorm.lean:199) → `map_sub`. At MainLemma.lean:408 use
   `simp only [diag] at h ⊢; simp [map_sub, Polynomial.sub_modByMonic, h]` (compiled), then
   delete it. Keeping it is harmless if the keep-public-API instruction stands.
4. **`Roth.kroneckerExp`** (GenWronskian.lean:57) →
   `Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))`.
5. **`Roth.kroneckerExp_injOn`** (GenWronskian.lean:69) → the `Behrend.map_injOn` composition;
   drop `hk`.
6. **`Roth.eq_mapDomain_some_add_single`** (Separation.lean:57) → `Finsupp.optionElim_some`.
   At Separation.lean:107 use `exact (optionEquivLeft_coeff_some_coeff_none R τ e P).symm`,
   then delete it.
7. **`Roth.coeff_coeffNone`** (Separation.lean:85) → `optionEquivLeft_coeff_coeff`. Use the
   mathlib lemma at Separation.lean:107 and :129 (after the `optionElim` restatement of
   `coeff_rename_mul_aeval`), then delete it or keep it as a one-line restatement.
8. **`Roth.degreeOf_coeffNone_le`** (Separation.lean:114, YES-add-as-is) → upstream as
   `MvPolynomial.degreeOf_coeff_optionEquivLeft` in Mathlib/Algebra/MvPolynomial/Equiv.lean.
   It has no local callers: delete it, or restate it as that lemma until the PR lands.
9. **`Roth.exists_sum_mul_eq_gcd`** (Separation.lean:374) → `Finset.gcd_eq_sum_mul` at
   Separation.lean:446 (compiled), then delete it.
10. **`Roth.exists_nat_smul_eq_map`** (Separation.lean:380) → the new
    `MvPolynomial.exists_smul_eq_map_of_isLocalization`. Use it at Separation.lean:410
    (`evidence/Roth.exists_nat_smul_eq_map/` (5)), then delete it. Keep it locally until the
    general lemma exists, either in the project or upstream.

### INLINE (4)

1. **`Roth.eq_sum_X_none_pow_mul_coeffNone`** (Separation.lean:98).
   - Inline the 2-line `optionEquivLeft_symm_apply` + `eval₂_eq_sum_range'` composition at
     Separation.lean:335.
   - This orphans the private `coeff_X_none_pow_mul_rename` and `eq_mapDomain_some_add_single`;
     delete both.
2. **`Roth.exists_nat_mul_isIntegral`** (Main.lean:62).
   - Take `M := Algebra.natDenominator α` at Main.lean:121 and add
     `import Mathlib.RingTheory.Algebraic.Denominator`.
   - Alternatively, keep it as the paper's §6 lemma with its body replaced by the composition
     (`evidence/Roth.exists_nat_mul_isIntegral/composition.lean`).
3. **`Roth.exists_monic_aeval_eq_zero`** (Main.lean:142).
   - Inline the term `minpoly ℤ α * X ^ 2` at Main.lean:415
     (`evidence/Roth.exists_monic_aeval_eq_zero/composition.lean`).
   - Alternatively, keep it as the paper's §6 sentence with its body replaced.
4. **`Roth.mul_sq_div_three_le_sum_max_aux`** (private, Theta.lean:347).
   - Inline it into `min_le_sum_max` as an `rp = 0` split plus a direct call to
     `mul_sq_div_three_le_sum_max_of_pos_aux`
     (`evidence/Roth.mul_sq_div_three_le_sum_max_aux/inline_into_min_le_sum_max.lean`).

## Recommended Action Plan

### Priority 1: Quick Wins (can do now)

1. **Dead code** (needs your sign-off under the keep-public-API instruction): delete
   `weight_le_degree_div`, `sum_range_le_sum_of_injective`, `eval_diag`, `index_neg`,
   `coeff_uniqueAlgEquiv_symm`, `floor_sq_div_two_le_sum`, `sq_div_three_lt_floor_sq_div_two`
   and `mul_two_mul_add_one_div_lt_of_le_sq_mul`. For blueprint FACTs, use `private` instead.
2. **Mathlib one-liners:**
   - replace `exists_sum_mul_eq_gcd` by `Finset.gcd_eq_sum_mul`;
   - replace `coeff_coeffNone` and `eq_mapDomain_some_add_single` by the `optionEquivLeft`
     lemmas;
   - replace `diag_sub` by `map_sub`;
   - inline `eq_sum_X_none_pow_mul_coeffNone`, `exists_nat_mul_isIntegral`,
     `exists_monic_aeval_eq_zero` and `mul_sq_div_three_le_sum_max_aux`.
3. **Superfluous hypotheses:** drop all rows of the API Improvements table that touch public
   project lemmas. This covers `hf`, `hk`, `hB0`, `hP` ×3, `hB` ×2, `hq` ×2, `Irrational` and
   `hx`.
4. **Duplicated bodies:** factor `card_mem_upperBounds_indexSet`, the `hpow`/`0 < r₁`/`0 < δ`
   helpers in MainLemma, and `optionEquivLeft_rename_some`.
5. **Golfs:** `Real.log_two_lt_d9` in `four_lt_rpow`; the `mapped_det_ne_zero_aux` last step;
   `Finset.sum_flip` in `sum_inv_le`.
6. **Docstrings and naming:** apply the fixes listed under API Improvements.
7. **LiouvilleWith wrappers:** add the compiled `IsAlgebraic.not_liouvilleWith` and
   `LiouvilleWith.transcendental` to `Roth/Main.lean`, and `isDiophantine_iff_liouvilleWith`
   to `Roth/LeanEval.lean`.

### Priority 2: API Improvements (significant impact)

1. Add `@[simp]` to `hasseDeriv_map`. Restate `taylor_zero` with Pi zero. Add
   `@[simp] map_taylor`, `@[simp] degreeOf_taylor` and `taylor_inj`.
2. Add the pointwise `norm_coeff_hasseDeriv_le` and derive `abs_coeff_hasseDeriv_le` and
   `normOne_hasseDeriv_le` from it.
3. Extract the two Separation degree building blocks and reprove the twin lemmas under
   `CommSemiring + NoZeroDivisors`.
4. Add `taylorEquiv`, and make `taylor_injective` a one-liner from it.
5. Derive both Wronskian vanishing lemmas from
   `det_linearMap_eq_zero_of_not_linearIndependent`.
6. Restate the `optionEquivLeft`-indexed lemmas at `a.optionElim b`.
7. Move `exists_hasseDeriv_eval_ne_zero` and `le_index_of_forall_eval_eq_zero` into
   Index.lean, and reprove `index_prod` via `weightedOrder_prod`.

### Priority 3: Generalizations (requires mathematical thought)

1. Generalise from `Field K` to `CommRing R` plus `IsDomain` or `CharZero` as needed. This
   covers the Wronskian files, `derivative_aeval` (to any `Derivation`), `diag` and
   `diag_eq_sum` (to `CommSemiring`), and the CoeffNorm lemmas (to `SeminormedCommRing`). All
   are compiled. Difficulty: Low–Medium.
2. Restate the box, `Fintype` and weak-inequality lemmas in their general forms:
   - `hasseCoeff_le_two_pow` → `2^k.degree`;
   - `eq_sum_box_hasseDeriv` and `eval_eq_sum_box` → support-sum forms;
   - sharp `degreeOf_hasseDeriv_le`;
   - `degreeOf_taylor` equality;
   - `uniqueAlgEquiv_hasseDeriv` and `hasseDeriv_single_aeval_X` → general `d`.
   Keep the current statements as corollaries. Difficulty: Low.
3. Lemma 1 without `Finite σ`, over a `CharZero` domain. Difficulty: Medium.
4. Replace `exists_hasseDeriv_kronecker_eq_sum` by a general `Polynomial.hasseDeriv_aeval`
   chain rule. This needs a new proof. Difficulty: High; do it only if cluster 6 is upstreamed.

### Priority 4: Structural Changes (major refactoring)

1. **`box` → `Finset.Iic`.** It has call sites in 6 files. Do it first, because the Taylor box
   corollaries and the `Lattice` statements depend on it.
2. **`weight` → `Finsupp.weight`.** Delete `weight_zero`, use `map_add` for `weight_add`, add
   the `weight_eq_sum` bridge, and repoint about 9 unfolding sites.
3. **`kroneckerExp` → `Finsupp.weight`, with `kroneckerExp_injOn` from `Behrend.map_injOn`.**
   Optionally go further and rebase `kronecker` on a local `weightedSubst w` over
   `CommSemiring`.
4. **`diag` as a bundled `AlgHom` `aeval (fun _ ↦ X)` over `CommSemiring`.** Optional.
5. **`index` rebased on `MvPowerSeries.weightedOrder` of `taylor α P`.** Optional; this is
   BORDERLINE question 1 below. It is only worthwhile if a "weighted order at a point" goes
   upstream.

### Priority 5: Mathlib contributions

**Proposed upstream PR batches, in dependency order.** Each lists its YES-add-as-is and
YES-but-generalise-first members.

1. **PR A: `Finsupp.choose`** (Mathlib/Data/Finsupp/Choose.lean or Nat/Choose/Multinomial.lean).
   - Members: `hasseCoeff`, `hasseCoeff_eq_zero_iff`, `hasseCoeff_eq_prod`,
     `hasseCoeff_le_two_pow`, and the private `hasseCoeff_mul_hasseCoeff` and
     `hasseCoeff_mul_succ`, published as `choose_mul` and the succ form.
   - No prerequisites.
2. **PR B: `MvPolynomial.hasseDeriv`** (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean).
   Depends on A.
   - YES-add-as-is: `hasseDeriv_zero_apply`, `hasseDeriv_zero`, `hasseDeriv_C`,
     `hasseDeriv_map` (with `@[simp]`) and `hasseDeriv_rename`.
   - YES-but-generalise-first: `hasseDeriv`, `hasseDeriv_monomial`, `hasseDeriv_apply`,
     `coeff_hasseDeriv`, `hasseDeriv_hasseDeriv`, `hasseDeriv_hasseDeriv_of_disjoint`,
     `pderiv_hasseDeriv`, `degreeOf_hasseDeriv_le`, `hasseDeriv_eq_zero_of_degreeOf_lt`,
     `hasseDeriv_mul_of_degreeOf_eq_zero` (with the Leibniz rule), `hasseDeriv_single_aeval_X`,
     `uniqueAlgEquiv_hasseDeriv`, `factorial_smul_hasseDeriv_single` and
     `hasseDeriv_rename_mul_aeval`.
3. **PR C: `MvPolynomial.taylor`** (new Mathlib/Algebra/MvPolynomial/Taylor.lean). The basic
   part is independent of B; `coeff_taylor` and the expansions depend on B.
   - YES-add-as-is: `taylor`, `taylor_apply`, `taylor_X`, `taylor_C`, `taylor_monomial`,
     `taylor_zero`, `taylor_taylor`, `taylor_map`, `taylor_rename` and `taylor_injective`.
   - YES-but-generalise-first: `coeff_taylor`, `eval_taylor`, `degreeOf_taylor_le`,
     `taylor_neg_taylor`, `taylor_eq_zero_iff`, `eq_sum_box_hasseDeriv` and `eval_eq_sum_box`.
4. **PR D: small independent `MvPolynomial` lemmas** (Equiv.lean, Degrees.lean,
   NoZeroDivisors.lean, Weight.lean). These can land in parallel with A–C.
   - YES-add-as-is: `degreeOf_coeffNone_le` (→ `degreeOf_coeff_optionEquivLeft`) and
     `degreeOf_uniqueAlgEquiv_symm` (+ `natDegree_uniqueAlgEquiv`).
   - YES-but-generalise-first: `coeff_rename_mul_aeval`, `degreeOf_rename_mul_aeval`,
     `degreeOf_none_rename_mul_aeval` and `weight_eq_zero_iff`.
5. **PR E: ℓ¹ coefficient norm** (Mathlib/Analysis/Polynomial/Norm.lean or a new
   MvPolynomial/Norm.lean). The `geom_sum` part is independent; the Hasse bounds depend on B.
   - Members: `normOne` and the 11 basic `normOne_*`/`abs_coeff_le_normOne` lemmas,
     `normOne_det_le` (+ `Matrix.norm_det_le`), `abs_coeff_hasseDeriv_le`,
     `normOne_hasseDeriv_le`, `geom_sum_le_one_add_pow` (Algebra/Order/Ring/GeomSum.lean),
     `abs_eval_le`, `diag_eq_sum`, `abs_coeff_diag_le` and `degreeOf_det_hasseDeriv_le`.
6. **PR F: n-ary Wronskian** (Mathlib/RingTheory/Polynomial/Wronskian.lean).
   - Prerequisite PRs: `det_choose_eq` (→ Vandermonde.lean), `coeff_prod_of_natDegree_le'`
     (→ BigOperators.lean) and `linearIndependent_update_sub_smul` (→ LinearIndependent/Defs.lean).
   - Members: `wronskianMatrix`, `wronskian`, `wronskian_eq_zero_of_not_linearIndependent`,
     `coeff_wronskian_of_natDegree_injective`, `wronskian_ne_zero_of_natDegree_injective`,
     `wronskian_update_sub_smul`, `wronskian_ne_zero_of_linearIndependent` and
     `wronskian_eq_zero_iff`.
7. **PR G: weighted (Kronecker) substitution** (Mathlib/Algebra/MvPolynomial/, next to
   Expand.lean). Members: `kronecker`, `kronecker_monomial`, `coeff_kronecker` and
   `kronecker_eq_zero_iff`.
8. **PR H: `Derivation.map_mvPolynomial_aeval`.** Member: `derivative_aeval`.
9. **PR I: generalised Wronskian and Lemma 1** (new Mathlib/RingTheory/MvPolynomial/Wronskian.lean).
   Depends on B, F, G and H.
   - Members: `genWronskian`, `genWronskian_eq_zero_of_not_linearIndependent`,
     `det_hasseDeriv_separated` and `exists_genWronskian_ne_zero`.
10. **PR J: Gauss lemma and rational root theorem pieces** (RingTheory/MvPolynomial/Localization.lean,
    RingTheory/Polynomial/GaussLemma.lean). Independent of the other PRs.
    - Members: `exists_nat_smul_eq_map`, `exists_primitive_smul_eq`,
      `exists_eq_pow_mul_of_rootMultiplicity` and `pow_rootMultiplicity_le`.
11. **PR K: assorted analysis and counting lemmas.** Independent of the other PRs.
    - Members: `norm_coeff_modByMonic_le` (→ `Polynomial.supNorm_modByMonic_le`),
      `boxFamily_finite` and `ncard_boxFamily` (→ RingTheory/MvPolynomial/Basic.lean) and
      `one_le_prod_pow_mul_abs_eval` (→ DenomsClearable.lean).
12. **PR L (last, policy-dependent): Roth's theorem.** It depends on everything above.
    - Members: `roth`, `roth_rat` and `thueSiegelRoth`, as `IsAlgebraic.not_liouvilleWith`,
      `LiouvilleWith.transcendental` and `IsAlgebraic.finite_rat_abs_sub_lt_one_div_den_rpow`
      in a new Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean.

Optional tiny PRs named in the reports:
- `MvPowerSeries.weightedOrder_eq_zero_iff` for positive weights;
- `MvPowerSeries.le_weightedOrder_sum`, `weightedOrder_smul` and `weightedOrder_nsmul_weight`
  (all for RingTheory/MvPowerSeries/Order.lean or NoZeroDivisors.lean);
- `isLittleO_rpow_rpow_atTop_of_lt` (Analysis/SpecialFunctions/Pow/Asymptotics.lean);
- the finset Bézout bridge `Ideal.span (u '' s) = ⊤` (RingTheory/PrincipalIdealDomain.lean).

**NO-mathlib-has-it (12): delete or replace with the mathlib term.**
- `box` → `Finset.Iic`; `mem_box` → `mem_Iic`.
- `weight`, `weight_zero`, `weight_add`, `weight_single` and `weight_mapDomain` →
  `Finsupp.weight` and its lemmas.
- `kroneckerExp` → `Finsupp.weight`.
- `diag_sub` → `map_sub`.
- `coeff_coeffNone` → `optionEquivLeft_coeff_coeff`.
- `aeval_X_eq_rename` → `Polynomial.toMvPolynomial_eq_rename_comp` (or keep as a rewrite
  lemma).
- `exists_sum_mul_eq_gcd` → `Finset.gcd_eq_sum_mul`.

**NO-composable-from-mathlib (61 + 2 INHERITED): keep locally, or inline the mathlib
composition.** Inline or replace: `exists_nat_mul_isIntegral`, `exists_monic_aeval_eq_zero`,
`eq_sum_X_none_pow_mul_coeffNone`, `kroneckerExp_injOn`, `eq_mapDomain_some_add_single`. Keep
as project API with the optional mathlib-composition reproofs given in each report:
- the `card_box` family;
- the `weight_*` API;
- `diag` and `natDegree_diag_le`;
- the whole `index_*` API;
- `coeffNone` and `linearIndependent_kronecker`;
- `sum_natDegree_update_lt` and `det_sum_rows`;
- `exists_int_eq_of_gcd_eq_one`;
- the Roth parameter definitions (`RSet`, `indexSet`, `Θ`, `lem6M`, `lem6Φ`, `lam`, `gam`,
  `eta`, `mainCoeffBound`, `boxFamily`, `approxSet`) and their glue lemmas;
- `eventually_div_rpow_lt` and `reduction`;
- the harness predicate `IsDiophantine`.

**BORDERLINE-needs-human (36): questions grouped by theme.** For each, the reports' recommended
default is given.

1. **Should Roth's proof internals go to mathlib at all?** This decides 24 of the 36. Default:
   no; keep them downstream and upstream only the general layers (PRs A–K) plus, at most, the
   final headline theorem.
   - Lemma 2: `exists_det_eq_mul`.
   - Lemma 3: `abs_coeff_det_hasseDeriv_le`.
   - Lemmas 5–7: `Θ_option_le`, `index_le_lem6`, `index_det_le`, `sum_max_sub_le_index_det`,
     `min_le_sum_max`, `lem6M_lt`, `lem7_Φ_bound`, `lem7_numeric`, `Θ_lt`.
   - Lemma 8: `card_filter_weight_le`, `sum_inv_lt`, `sqrt_one_sub_inv_lt`.
   - Lemma 9: `main_lemma`, `pigeonhole_count`, `exists_ne_modByMonic_eq`.
   - §6–7 parameter steps: `exists_delta_bound`, `exists_m`, `exists_delta`,
     `exists_approximants`, `exists_degrees`, `abs_eval_lt_of_le_index`.
   - `roth_of_isIntegral`.
   - If yes, the target is Mathlib/NumberTheory/DiophantineApproximation/ or the Archive. Land
     it as a final PR series after A–K, restated over `Finset.Iic` and `Finsupp.weight`.
2. **Should a "weighted order at a point" go upstream?** This is the `Roth.index` question.
   Default: keep the ℝ-valued index local. If you want it upstream, target an `MvPolynomial`
   weighted order via `coeToMvPowerSeries` composed with `taylor`, in Mathlib/RingTheory/MvPolynomial.
3. **Generic linear-algebra or analysis gaps exposed by Roth lemmas.** Default: upstream only on
   your approval, as separate PRs.
   - `exists_separated_representation` → `TensorProduct.exists_sum_tmul_eq_of_linearIndependent`
     (LinearAlgebra/TensorProduct/Finiteness.lean).
   - `card_filter_box_last` → the `piFinset` + `Fin.snoc` fibre count
     (`evidence/Roth.card_filter_box_last/general_piFinset.lean`, Data/Fin/Tuple/Finset.lean).
   - `approxSet_den_le_finite` → a generic finite-fractions-in-a-bounded-set lemma
     (DiophantineApproximation/Basic.lean).
   - `exists_reduced_approx` → `approxSet_infinite_iff_rat`.
   - `isDiophantine_iff` → a uniform-lower-bound-vs-`LiouvilleWith` lemma.
4. **Gauss lemma shape.** For `exists_int_factors`: does mathlib want the
   rename-some/aeval-X-none separated form (`evidence/Roth.exists_int_factors/` (6)), or only a
   general `MvPolynomial` Gauss lemma? Default: keep it local and land PR J's content API first.
5. **Chain rule.** `exists_hasseDeriv_kronecker_eq_sum`: is a general `Polynomial.hasseDeriv_aeval`
   (algebraic Faà di Bruno) worth a new proof? Default: keep it local unless PR I goes ahead.
6. **Ad-hoc real-number estimates.** `sqrt_lt_floor`, `four_lt_rpow`,
   `mul_log_div_two_lt_log_mainCoeffBound` and `three_small_factors`. Default: keep them local.
   If anything goes up, it should be only the strict half of `sqrt_lt_floor`, never the
   conjunction.

STATUS: COMPLETE
