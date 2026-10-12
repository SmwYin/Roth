# Development Plan: Roth's theorem

## Goal

Formalise **Roth's theorem** on rational approximation of algebraic numbers, following the
proof in the attached reference (Takloo-Bighash–Yin, *Formalizing Roth's theorem*,
`.mathlib-quality/references/clean.tex`), which is Roth's original 1955 argument organised as
Lemmas 1–9.

Main statement (`Roth/Main.lean`):

```lean
/-- The set of pairs `(h, q)`, `q > 0`, with `|α - h/q| < 1/q^κ`. -/
def Roth.approxSet (α κ : ℝ) : Set (ℤ × ℕ) :=
  {hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ}

theorem Roth.roth {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : (approxSet α κ).Infinite) : κ ≤ 2

theorem Roth.roth_rat {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2
```

The power `(q : ℝ) ^ κ` is the real power (`Real.rpow`); the statement is exactly the Theorem
(Roth) of §6 of the reference.

## References

- **[TY]** R. Takloo-Bighash, S. Yin, *Formalizing Roth's theorem* — the attached `clean.tex`,
  saved verbatim at `.mathlib-quality/references/clean.tex`. Every leaf of the decomposition
  cites a section/lemma of [TY] and quotes it verbatim (see `decomposition.md`). Section map:
  - §1 Derivatives (multivariate Hasse operators `Δ_i`) → `Roth/HasseDeriv.lean`
  - §2 Wronskians: one-variable Wronskian lemma, generalized Wronskians, Lemma 1 (Kronecker
    substitution), Lemma 2 (`F = U V`) → `Roth/Wronskian.lean`, `Roth/GenWronskian.lean`,
    `Roth/Separation.lean`
  - §3 Lemma 3 (coefficient bound for `F`) → `Roth/CoeffNorm.lean`
  - §4 Index: Taylor expansion, the index and Lemmas 4-1, 4-2, `index-of-derivative`, scaling →
    `Roth/Taylor.lean`, `Roth/Index.lean`
  - §5 `ℛ_m`, `Θ_m`, Lemmas 5, 6, 7 → `Roth/Theta.lean`
  - §6 Lattice count (Lemma 8) → `Roth/Lattice.lean`
  - §6 Reduction to algebraic integers, Lemma `m-δ`, `B_1` estimates, Lemma 9 →
    `Roth/MainLemma.lean`, `Roth/Main.lean`
  - §7 Proof of the theorem → `Roth/Main.lean`
- [TY] is self-contained; no other source is used for any leaf. (For orientation only: the
  argument is Roth, *Rational approximations to algebraic numbers*, Mathematika 2 (1955), and
  is also exposed in Cassels, *An introduction to Diophantine approximation*, Ch. VI; these are
  not cited by any leaf.)

## Mathlib inventory (names checked against mathlib `v4.34.0-rc2` by `#check` compilation; the project now uses `v4.34.0`, where `MvPolynomial.coeff m p` has become `p.coeff m`)

| Concept | Mathlib status | Our action |
|---------|----------------|------------|
| Univariate Hasse derivative `Polynomial.hasseDeriv`, `hasseDeriv_coeff`, `hasseDeriv_comp`, `hasseDeriv_mul`, `natDegree_hasseDeriv_le`, `factorial_smul_hasseDeriv` | `Mathlib.Algebra.Polynomial.HasseDeriv` | USE for the one-variable Wronskian and as the model for the multivariate operator |
| Multivariate Hasse derivative | **not in mathlib** | DEFINE `MvPolynomial.hasseDeriv (d : σ →₀ ℕ)` with full API (`Roth/HasseDeriv.lean`) |
| Partial derivatives `MvPolynomial.pderiv`, `coeff_pderiv`, `pderiv_monomial` | `Mathlib.Algebra.MvPolynomial.PDeriv` | USE (chain rule, `pderiv_hasseDeriv`) |
| Univariate Taylor `Polynomial.taylor`, `taylor_coeff` | `Mathlib.Algebra.Polynomial.Taylor` | USE as model; multivariate `MvPolynomial.taylor` is new (`Roth/Taylor.lean`) |
| Wronskian of two polynomials `Polynomial.wronskian` | `Mathlib.RingTheory.Polynomial.Wronskian` | NOT applicable (only 2 polynomials); DEFINE `Roth.wronskian` for `Fin l` families |
| Vandermonde `Matrix.det_vandermonde`, `det_vandermonde_ne_zero_iff`, `det_eval_matrixOfPolynomials_eq_det_vandermonde` | `Mathlib.LinearAlgebra.Vandermonde` | USE for the binomial determinant |
| `descPochhammer`, `descPochhammer_eval_eq_descFactorial`, `monic_descPochhammer`, `Nat.descFactorial_eq_factorial_mul_choose` | `Mathlib.RingTheory.Polynomial.Pochhammer`, `Mathlib.Data.Nat.Choose.Basic` | USE (`binom X μ` is monic of degree `μ` up to `μ!`) |
| `Matrix.det_apply'`, `det_mul`, `det_transpose`, `det_updateCol_add_smul_self`, `det_updateRow_sum`, `exists_mulVec_eq_zero_iff`, `RingHom.map_det` | `Mathlib.LinearAlgebra.Matrix.Determinant.Basic`, `.../NonsingularInverse` | USE |
| Row-multilinear expansion `MultilinearMap.map_sum_finset`, `map_smul_univ`, `Matrix.detRowAlternating` | `Mathlib.LinearAlgebra.Multilinear.Basic` | USE for `det_sum_rows` |
| `LinearIndependent.map`, `linearIndependent_iff_card_eq_finrank_span`, `Module.Basis.coord`, `Module.finBasis` | `Mathlib.LinearAlgebra.*` | USE |
| Base-`k` digit uniqueness `Nat.ofDigits_inj_of_len_eq` | `Mathlib.Data.Nat.Digits.Defs` | USE (Kronecker injectivity) or reprove by induction |
| `MvPolynomial.optionEquivLeft`, `uniqueAlgEquiv`, `rename`, `coeff_rename_mapDomain`, `rename_injective`, `Finsupp.some` | `Mathlib.Algebra.MvPolynomial.Equiv`, `.../Rename` | USE to split off one variable (`Option τ`) |
| `MvPolynomial.degreeOf` API, `degreeOf_mul_eq` (domains) | `Mathlib.Algebra.MvPolynomial.Degrees`, `.../NoZeroDivisors` | USE |
| Weighted order `MvPowerSeries.weightedOrder`, `weightedOrder_mul`, `weightedOrder_le`, `exists_coeff_ne_zero_and_weightedOrder`, `le_weightedOrder` | `Mathlib.RingTheory.MvPowerSeries.Order`, `.../NoZeroDivisors` | USE for the product formula `ind(PQ) = ind P + ind Q` via a bridge lemma |
| Root multiplicity `rootMultiplicity_eq_natTrailingDegree`, `eq_rootMultiplicity_map`, `pow_rootMultiplicity_dvd` | `Mathlib.Algebra.Polynomial.RingDivision`, `.../Roots`, `.../Div` | USE (Lemma 5) |
| Gauss's lemma `Polynomial.IsPrimitive.dvd_of_fraction_map_dvd_fraction_map`, `IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast` | `Mathlib.RingTheory.Polynomial.GaussLemma` | USE (Lemma 5) |
| `Finset.gcd`, Bézout `Int.gcd_eq_gcd_ab` | `Mathlib.Algebra.GCDMonoid.Finset`, `Mathlib.Data.Int.GCD` | USE; finite Bézout `exists_sum_mul_eq_gcd` is new |
| `Polynomial.modByMonic`, `modByMonic_eq_of_dvd_sub`, `sub_modByMonic`, `degree_modByMonic_lt`, `modByMonic_eq_zero_iff_dvd` | `Mathlib.Algebra.Polynomial.Div` | USE (Lemma 9 remainders) |
| Pigeonhole `Finset.exists_ne_map_eq_of_card_lt_of_maps_to`, `Fintype.exists_ne_map_eq_of_card_lt` | `Mathlib.Data.Finset.Card`, `Mathlib.Data.Fintype.Pigeonhole` | USE |
| `Nat.choose_le_two_pow`, `Nat.sum_range_choose`, `Nat.choose_succ_right_eq`, `Nat.add_choose_mul_factorial_mul_factorial` | `Mathlib.Data.Nat.Choose.*` | USE |
| Boxes `Finsupp` intervals `Finsupp.card_Iic`, `Fintype.piFinset`, `Fintype.card_piFinset` | `Mathlib.Data.Finsupp.Interval`, `Mathlib.Data.Fintype.Pi` | USE for `Roth.box` |
| `Finsupp.degree`, `Finsupp.weight`, `degree_eq_weight_one` | `Mathlib.Data.Finsupp.Weight` | USE (orders of operators) |
| Real powers/logs `Real.rpow_*`, `Real.log_rpow`, `Real.rpow_lt_rpow_left_iff`, `Real.sqrt_eq_rpow` | `Mathlib.Analysis.SpecialFunctions.Pow.Real`, `.../Log.Basic` | USE (numerics) |
| Floors `Int.sub_one_lt_floor`, `Nat.floor_le`, `Nat.lt_floor_add_one` | `Mathlib.Algebra.Order.Floor.*` | USE |
| `IsAlgebraic.exists_integral_multiple`, `IsIntegral.neg`, `IsFractionRing.isAlgebraic_iff` | `Mathlib.RingTheory.Algebraic.Integral`, `.../Localization/Integral` | USE (reduction to algebraic integers) |
| `Irrational`, `irrational_iff_ne_rational` | `Mathlib.NumberTheory.Real.Irrational` | USE |
| Diophantine approximation module | `Mathlib.NumberTheory.DiophantineApproximation.Basic` | reference only (Dirichlet's theorem, convergents) — not needed |
| Liouville's theorem | `Mathlib.NumberTheory.Transcendental.Liouville` | not needed (Roth is proved from scratch) |
| Roth's theorem, Thue–Siegel–Roth | **not in mathlib** | PROVE |

## File structure

```
Roth.lean                 -- root, imports everything below
Roth/HasseDeriv.lean      -- MvPolynomial.hasseDeriv + API                       (§1)
Roth/Box.lean             -- Roth.box r (multi-index box), Roth.weight r d        (§4, §6)
Roth/Wronskian.lean       -- one-variable Wronskian of a Fin l family, criterion  (§2)
Roth/Taylor.lean          -- MvPolynomial.taylor, coeff_taylor, Taylor's theorem   (§4)
Roth/CoeffNorm.lean       -- ℓ¹ coefficient norm, det bounds, Lemma 3, diag, eval (§3, §6)
Roth/GenWronskian.lean    -- generalized Wronskians, Kronecker substitution, Lemma 1 (§2)
Roth/Lattice.lean         -- Lemma 8                                             (§6)
Roth/Index.lean           -- Roth.index, Lemmas 4-1, 4-2, index-of-derivative    (§4)
Roth/Separation.lean      -- Lemma 2: det (Δ_μ Δ^{(p)}_ν R) = U V                 (§2)
Roth/Theta.lean           -- ℛ_m, Θ_m, Lemmas 5, 6, 7                            (§5)
Roth/MainLemma.lean       -- constants λ γ η B₁, Lemma m-δ, B₁ bounds, Lemma 9  (§6)
Roth/Main.lean            -- reduction, parameter choices, Roth's theorem         (§6–§7)
```

## Dependency graph

```
HasseDeriv ──┬── Taylor ──────────── Index ─────────┐
             ├── CoeffNorm ─────┐                    ├── Theta ──── MainLemma ──── Main
             └── GenWronskian ──┴── Separation ─────┘       ▲
Box ─────────┬── Taylor, CoeffNorm, Index, Lattice ──────────┘
Wronskian ───┴── GenWronskian
```

Build order (= order of imports in `Roth.lean`): HasseDeriv, Box, Wronskian, Taylor, CoeffNorm,
GenWronskian, Lattice, Index, Separation, Theta, MainLemma, Main.

## Key design decisions

1. **Variables.** Polynomials are `MvPolynomial σ R` over an arbitrary finite index type `σ`
   wherever possible. The source's "split off the last variable `x_p`" (Lemmas 2, 3, 6) is
   modelled with `σ = Option τ`: `none` is `x_p` and `some j` are `x_1, …, x_{p-1}`. The
   induction of Lemma 7 runs over `Fin (n+1)` and uses `finSuccEquivLast : Fin (n+1) ≃ Option
   (Fin n)` (`Fin.last ↦ none`), so the source's ordering `x_1, …, x_m` ↔ `0, …, m-1 : Fin m`
   is kept, with `r` decreasing along the chain exactly as in the source.
2. **Hasse derivatives** are `R`-linear maps `MvPolynomial.hasseDeriv (d : σ →₀ ℕ)` defined on
   monomials by the binomial formula (as in the source and as `Polynomial.hasseDeriv`), over
   any commutative semiring; no division by factorials is ever needed, so coefficients can be
   kept in `ℤ` and mapped to `ℚ`/`ℝ` (`hasseDeriv_map`). The source's `(1/ν!) ∂^ν_{x_p}` is
   `hasseDeriv (Finsupp.single none ν)`.
3. **Index.** `Roth.index P α r : ℝ` is the minimum of `weight r d = ∑ d j / r j` over the
   support of the translate `taylor α P`, for `r : σ → ℕ` (the source allows positive reals but
   only ever uses positive integers). The source's convention `ind 0 = +∞` is replaced by
   explicit `≠ 0` hypotheses in every lemma (this is exactly how the convention is used in the
   source: "Zero entries and zero permutation products have index +∞ and cannot worsen the
   lower bound"). The product formula is imported from mathlib's `MvPowerSeries.weightedOrder_mul`
   through the bridge `index_eq_weightedOrder_div` with natural weights `D / r j`, `D = ∏ r j`.
4. **Coefficient bounds** are sup-bounds `∀ d, |coeff d P| ≤ B` with `B : ℝ` (as in `ℛ_m(B; r)`)
   plus the ℓ¹ norm `Roth.normOne` for the determinant estimate (as the source's Lean note
   prescribes: triangle inequality + submultiplicativity).
5. **One-variable Wronskian criterion** is proved by strong induction on the sum of degrees,
   performing the source's "elimination of equal leading degrees" one column operation at a
   time (`det_updateCol_add_smul_self`), and the distinct-degree case by the source's leading
   coefficient computation (Vandermonde of `binom(d_ν, μ)`).
6. **Lemma 2's separated representation** is built from a basis of the span of the
   `x_p`-coefficient polynomials (the source's Lean note), not by minimising `l`; integrality
   of `U, V` is obtained by the source's Bézout argument.
7. **Generality.** Hasse derivatives and Taylor expansion are stated over `CommSemiring R`;
   Wronskian lemmas over a field `K` (`CharZero K` where the source needs characteristic
   zero); `Θ`-material over `ℤ`/`ℝ` as in the source. Nothing is specialised to `Fin m` before
   Lemma 7.

## Toolchain note

Resolved 2026-10-12: the project now pins `leanprover/lean4:v4.34.0` with mathlib `v4.34.0`, and
`lake build` works. (History: the original pin `v4.34.0-rc2` has a `lake` binary that crashes with
SIGTRAP (exit 133) on this machine — macOS 27.0.1, arm64 — on every subcommand except `--version`
and `init`; the installed binaries were byte-identical to the official release, and v4.33.1,
v4.34.0, v4.35.0-rc1/rc3 all work. The bump required one API migration: mathlib `v4.34.0` deleted
`MvPolynomial.coeff`; the skeleton now writes `p.coeff m` (`AddMonoidAlgebra.coeff`).) The
direct-lean scripts below are kept as an optional fallback:

- `.mathlib-quality/scripts/lean-direct.sh <file.lean>` — run `lean` with the project's
  `LEAN_PATH` (the mathlib cache is complete);
- `.mathlib-quality/scripts/build-direct.sh [Roth.Module …]` — compile the project modules in
  dependency order, writing `.olean` files where `lake` would.

The language-server tools (`lean_diagnostic_messages` etc.) work again after the bump.

## Milestones

- M1: every `.lean` file compiles (skeleton with `sorry`) — done at planning time.
- M2: `Roth/HasseDeriv.lean`, `Roth/Taylor.lean`, `Roth/Box.lean`, `Roth/CoeffNorm.lean` sorry-free
  (the algebraic foundation).
- M3: `Roth/Wronskian.lean`, `Roth/GenWronskian.lean`, `Roth/Separation.lean` sorry-free (Lemmas 1–3).
- M4: `Roth/Index.lean`, `Roth/Theta.lean` sorry-free (Lemmas 4–7).
- M5: `Roth/Lattice.lean`, `Roth/MainLemma.lean` sorry-free (Lemmas 8–9).
- M6: `Roth/Main.lean` sorry-free — **`Roth.roth`** proved; `#print axioms` shows only
  `propext`, `Classical.choice`, `Quot.sound`.
