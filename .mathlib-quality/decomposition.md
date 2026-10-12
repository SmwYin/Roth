# Decomposition for Roth's theorem

Source: **[TY]** Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`
(line locators `clean.tex:NNN` refer to that file). Every leaf below carries a verbatim quote from
[TY] and a Lean ↔ source match paragraph; the Lean statements are the canonical ones in the
skeleton (every declaration ends in `:= by sorry`).

## Skeleton location

The Lean skeleton lives in (build order)

- `Roth/HasseDeriv.lean`, `Roth/Box.lean`, `Roth/Wronskian.lean`, `Roth/Taylor.lean`,
  `Roth/CoeffNorm.lean`, `Roth/GenWronskian.lean`, `Roth/Lattice.lean`, `Roth/Index.lean`,
  `Roth/Separation.lean`, `Roth/Theta.lean`, `Roth/MainLemma.lean`, `Roth/Main.lean`
  (root module `Roth.lean`).

Build status: `lake build` passes (sorry warnings only, no errors) after the bump to
`leanprover/lean4:v4.34.0` / mathlib `v4.34.0` on 2026-10-12. (The skeleton was first verified
under `v4.34.0-rc2` with the direct-lean scripts, see the build log at the end of this file; the
only change needed for the bump was the `MvPolynomial.coeff` → `p.coeff m` migration.) In prose
below, `coeff d P` means the coefficient `P.coeff d`.

## How to read the entries

- **Status tags.** `[mathlib]` = discharged by ≤ 3 mathlib lemmas (names verified by `#check`
  compilation, see `plan.md` inventory); `[gap]` = genuinely new content whose proof the source
  gives (or whose proof is a direct computation the source calls "immediate"/"follows directly");
  such a leaf is an *API gap* in the sense of the planning procedure: its sub-decomposition is the
  list of mathlib lemmas and earlier project leaves in its "Discharged by" line, and its ticket
  carries the full proof sketch. `[internal]` = composed from the leaves listed under it.
- **LOC estimates** are anchored on the source line count of the corresponding passage.
- **Attacks.** The language-server search tools were unavailable in this session (`lake serve`
  crashes, see `plan.md`); counterexample searches were done by `grep` over the mathlib sources
  (`.lake/packages/mathlib/Mathlib`), by `#check` compilation of the cited names, and by hand
  (edge-case instantiation). Each entry lists the attacks tried.
- **Prior-B2 log.** `.mathlib-quality/b2_log.jsonl` is empty (0 entries, created at planning
  time), so no leaf matches a prior B2 by name or shape; this is not repeated per leaf.
- The index convention: the source sets `ind(0) = +∞`; in Lean `Roth.index 0 α r = 0` and every
  lemma carries explicit `≠ 0` hypotheses (see `plan.md` design decision 3). Each index leaf below
  records how the source's use of the convention is matched.

---

## Result R0: the multivariate Hasse derivative (§1 of [TY])

### Plain-English proof (source structure)

[TY] §1 (`clean.tex:119-151`) defines `Δ_i` on monomials by the binomial formula, extends
linearly, notes that it works over any commutative semiring, agrees with `(1/i!)∂^i` over a
`ℚ`-algebra, and (Lean note) asks for the coefficient identity `[X^e]Δ_d P = (∏ binom(e_j+d_j, d_j))
[X^{e+d}]P` and compatibility with coefficient maps. Later sections use, about `Δ`: the
composition identity (§4, proof of `index-of-derivative`), `∂_j Δ_d = (d_j+1)Δ_{d+e_j}` (§2, proof
of Lemma 1), that `Δ_μ` in the variables `x_1..x_{p-1}` passes through `φ(x_p)` and `∂_p` passes
through `ψ(x_1..x_{p-1})` (§2, proof of Lemma 2), that derivatives do not raise partial degrees
(§2, end of Lemma 2), that multi-indices outside the degree box kill the polynomial (§6, Lemma 9),
and the binomial bound `∏ binom ≤ 2^S` (§3, Lemma 3). These are the leaves of this file.

### Leaves

- **R0.1** `[gap]` `MvPolynomial.hasseDeriv` (definition) and `hasseCoeff`
  - Lean: `Roth/HasseDeriv.lean:28`
    ```lean
    def hasseCoeff (d k : σ →₀ ℕ) : ℕ := d.prod fun j n => (k j).choose n
    noncomputable def hasseDeriv (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
      Finsupp.lsum R (fun k : σ →₀ ℕ =>
          (monomial (k - d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R))) ∘ₗ
        (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap
    ```
  - Source: §1, `clean.tex:122-131`. Quote:
    > "For a multi-index i=(i_1,…,i_p)∈ℕ^p, define the Hasse differential operator Δ_i by its
    > effect on monomials: Δ_i(x_1^{k_1}⋯x_p^{k_p}) = (∏_{j=1}^p binom(k_j, i_j)) x_1^{k_1-i_1}⋯
    > x_p^{k_p-i_p} if i_j ≤ k_j for every j, 0 otherwise. We extend this operator linearly to all
    > polynomials. ... The definition works over ℤ, ℚ, or ℝ (and over any commutative semiring by
    > casting the binomial coefficients)."
  - Match: the Lean definition is the linear extension (`Finsupp.lsum` over the coefficient
    Finsupp, the same pattern as mathlib's `MvPolynomial.mkDerivationₗ`) of the monomial formula;
    the "otherwise 0" case is automatic because `Nat.choose k_j i_j = 0` when `i_j > k_j` (R0.3).
    Over any `CommSemiring R`, exactly as the source says.
  - Discharged by: definition; well-formedness by elaboration (compiles).
  - Attacks: [2] edge `d = 0`: `hasseCoeff 0 k = 1` (empty product), `k - 0 = k`: identity ✓
    (R0.6). [3] no hypothesis to weaken; `R` is a bare `CommSemiring`. [4] drift: the source's
    product is over all `j`; `Finsupp.prod` ranges over `d.support`, the omitted factors are
    `binom(k_j,0) = 1` (R0.5 records this). [5] discharge: n/a. Verdict: SURVIVED.

- **R0.2** `[gap]` `MvPolynomial.hasseDeriv_apply`, `hasseDeriv_monomial`
  - Lean: `Roth/HasseDeriv.lean:34`, `:39`
    ```lean
    theorem hasseDeriv_apply (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
        hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k)
    theorem hasseDeriv_monomial (d k : σ →₀ ℕ) (a : R) :
        hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a)
    ```
  - Source: §1, `clean.tex:122-132` (quote as in R0.1: "define ... by its effect on monomials ...
    We extend this operator linearly to all polynomials").
  - Match: `hasseDeriv_monomial` *is* the source's monomial formula; `hasseDeriv_apply` is its
    linear extension written as a sum over the support.
  - Discharged by: unfolding R0.1 with `Finsupp.lsum_apply`, `Finsupp.sum_single_index`,
    `MvPolynomial.sum_def`/`AddMonoidAlgebra.coeffLinearEquiv` (mirrors mathlib's
    `mkDerivationₗ_monomial`, proved there by `sum_monomial_eq`). Source: 1 display; ~15 LOC.
  - Attacks: [1] grep mathlib for a conflicting `MvPolynomial.hasseDeriv`: none exists. [2] edge
    `a = 0`: both sides `0` ✓; `d ≰ k`: `hasseCoeff = 0` so RHS `= monomial _ 0 = 0` ✓. [4] drift:
    none. [5] discharge: `mkDerivationₗ_monomial` pattern verified in
    `Mathlib/Algebra/MvPolynomial/Derivation.lean:44-47`. Verdict: SURVIVED.

- **R0.3** `[gap]` `MvPolynomial.hasseCoeff_eq_zero_iff`
  - Lean: `Roth/HasseDeriv.lean:43` —
    `hasseCoeff d k = 0 ↔ ¬ d ≤ k`
  - Source: §1, `clean.tex:129-130`: > "x_1^{k_1-i_1}⋯x_p^{k_p-i_p}, if i_j ≤ k_j for every j;
    0, otherwise."
  - Match: the "otherwise" branch is encoded by the vanishing of the binomial product; this
    lemma states exactly when it vanishes.
  - Discharged by: `Finset.prod_eq_zero_iff`, `Nat.choose_eq_zero_iff`, `Finsupp.le_iff`
    (all three verified). ~8 LOC.
  - Attacks: [2] edge `d = 0`: LHS `1 ≠ 0`, RHS `¬ 0 ≤ k` false ✓. [3] none to weaken. [5]
    `Finsupp.le_iff : f ≤ g ↔ ∀ i ∈ f.support, f i ≤ g i` ✓ matches the support-restricted
    product. Verdict: SURVIVED.

- **R0.4** `[gap]` `MvPolynomial.coeff_hasseDeriv`
  - Lean: `Roth/HasseDeriv.lean:47` —
    `(hasseDeriv d P).coeff e = (hasseCoeff d (e + d) : R) * P.coeff (e + d)`
  - Source: §1, Lean note, `clean.tex:147-152`. Quote:
    > "Define each Δ_d as a linear map and prove the coefficient identity
    > [X^e]Δ_dP=(∏_j binom(e_j+d_j,d_j))[X^{e+d}]P, where [X^e] denotes coefficient extraction;
    > this shows that distinct surviving monomials do not merge under differentiation."
  - Match: identical, with `hasseCoeff d (e+d) = ∏_{j∈supp d} binom(e_j+d_j, d_j)` (R0.5).
  - Discharged by: linearity (`MvPolynomial.induction_on'`) + R0.2 + `MvPolynomial.coeff_monomial`
    + R0.3 (`hasseCoeff d k ≠ 0 → d ≤ k`, so `k - d = e ↔ k = e + d`, by `tsub_eq_iff_eq_add_of_le`).
    Source: 1 line; ~25 LOC.
  - Attacks: [1] searched mathlib (`grep -rn "coeff.*hasseDeriv"`): only the univariate
    `Polynomial.hasseDeriv_coeff : (hasseDeriv k f).coeff n = (n+k).choose k * f.coeff (n+k)`,
    which is the `σ = Unit` case ✓ (consistent). [2] edge `e + d ∉ P.support`: both sides `0` ✓.
    [4] drift: none. [5] `coeff_monomial : coeff m (monomial n a) = if n = m then a else 0` ✓.
    Verdict: SURVIVED.

- **R0.5** `[mathlib]` `MvPolynomial.hasseCoeff_eq_prod` — `hasseCoeff d k = ∏ j, (k j).choose (d j)`
  for `[Fintype σ]`. Source: §1, `clean.tex:126` ("∏_{j=1}^p binom(k_j, i_j)"). Match: the source
  product is over all variables; the extra factors are `binom(k_j, 0) = 1`. Discharged by:
  `Finsupp.prod_fintype` (hypothesis `∀ j, (k j).choose 0 = 1` is `Nat.choose_zero_right`). ~3 LOC.
  Attacks: [2] `d = 0`: both `1` ✓. [5] `Finsupp.prod_fintype` signature verified. SURVIVED.

- **R0.6** `[mathlib]` `MvPolynomial.hasseDeriv_zero`, `hasseDeriv_zero_apply` — `hasseDeriv 0 = id`.
  Source: §4, `clean.tex:565-567` ("and Δ_0 P = P"). Match: identical. Discharged by: R0.2 +
  `Finsupp.prod_zero_index` + `tsub_zero` + `MvPolynomial.as_sum`/`LinearMap.ext`. ~8 LOC.
  Attacks: [2] `P = 0` ✓. SURVIVED.

- **R0.7** `[gap]` `MvPolynomial.hasseDeriv_C` — `d ≠ 0 → hasseDeriv d (C a) = 0`.
  Source: §1 (monomial formula with `k = 0`: `binom(0, i_j) = 0` for the nonzero `i_j`),
  `clean.tex:126-131`. Match: `C a = monomial 0 a` (`MvPolynomial.C_apply`), and `hasseCoeff d 0 = 0`
  by R0.3 since `¬ d ≤ 0`. Discharged by: R0.2, R0.3, `MvPolynomial.C_apply`. ~5 LOC. Attacks: [3]
  `d ≠ 0` necessary (R0.6). SURVIVED.

- **R0.8** `[gap]` `MvPolynomial.hasseDeriv_map` — `hasseDeriv d (map f P) = map f (hasseDeriv d P)`.
  Source: §1 Lean note `clean.tex:151-152`: > "prove compatibility with coefficient maps before
  passing between ℤ, ℚ and ℝ." Match: `map f` is the coefficient map. Discharged by: `MvPolynomial.ext`
  + R0.4 + `MvPolynomial.coeff_map` + `map_natCast`/`map_mul`. ~6 LOC. Attacks: [2] `f = id` ✓.
  [5] `coeff_map : coeff m (map f p) = f (coeff m p)` ✓ (checked). SURVIVED.

- **R0.9** `[gap]` `MvPolynomial.hasseDeriv_rename` — for injective `f`,
  `hasseDeriv (d.mapDomain f) (rename f P) = rename f (hasseDeriv d P)`.
  Source: §4 Lean note `clean.tex:638-641`: > "Prove invariance under nonzero scalars and variable
  renaming ... as separate lemmas". Match: renaming the variables of `Δ_d P` is `Δ_{f(d)}` of the
  renamed polynomial; this is the operator-level statement behind "invariance under variable
  renaming". Discharged by: linearity + `MvPolynomial.rename_monomial` + R0.2 +
  `Finsupp.mapDomain_apply hf` (so `hasseCoeff (mapDomain f d) (mapDomain f k) = hasseCoeff d k`
  via `Finsupp.prod_mapDomain_index_inj`) + `Finsupp.mapDomain` commutes with `-` for injective `f`
  (`Finsupp.mapDomain_tsub`? if absent: ext with `mapDomain_apply hf`). ~30 LOC.
  Attacks: [3] injectivity is necessary: for `f` constant on two variables, `mapDomain f` merges
  exponents and the binomial product changes (e.g. `σ = Fin 2`, `f = const`, `P = X₀X₁`,
  `d = e₀`: LHS `Δ_{e}(X^2) = 2X`, RHS `rename(X₁) = X` ✗) — so the hypothesis is sharp, not
  over-specified. [2] `d = 0` ✓. SURVIVED.

- **R0.10** `[gap]` `MvPolynomial.hasseDeriv_hasseDeriv` —
  `hasseDeriv d (hasseDeriv e P) = (hasseCoeff d (d + e) : R) • hasseDeriv (d + e) P`
  - Source: §4, proof of Lemma `index-of-derivative`, `clean.tex:578-582`. Quote:
    > "The Hasse composition identity gives Δ_iΔ_kP = (∏_{j=1}^p binom(i_j+k_j, i_j)) Δ_{i+k}P."
  - Match: with `i = d`, `k = e`: `hasseCoeff d (d+e) = ∏_{j∈supp d} binom(d_j+e_j, d_j)`, equal to
    the source's product (omitted factors are `1`).
  - Discharged by: `MvPolynomial.ext` + R0.4 twice + the per-coordinate identity
    `binom(f+d,d)·binom(f+d+e,e) = binom(d+e,d)·binom(f+d+e,d+e)` from
    `Nat.add_choose_mul_factorial_mul_factorial` (three times, cancel factorials; or
    `Nat.choose_mul`). Source: 1 display; ~35 LOC.
  - Attacks: [2] by hand on `X^k`, one coordinate: `k < e` ⇒ both `0`; `k ≥ e`, `k - e < d` ⇒
    LHS `0`, RHS `binom(k, d+e) = 0` ✓; generic case the factorial identity ✓. [3] none.
    [5] `Nat.add_choose_mul_factorial_mul_factorial : (i+j).choose j * i! * j! = (i+j)!` ✓
    (checked by `#check`). SURVIVED.

- **R0.11** `[gap]` `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` — disjoint supports ⇒
  `hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P`. Source: as R0.10 (`clean.tex:578-582`);
  used in §2 Lemma 2 where `Δ_μ` (variables `x_1..x_{p-1}`) is composed with `(1/ν!)∂^ν_{x_p}`.
  Match: when supports are disjoint every factor `binom(d_j+e_j, d_j)` is `binom(d_j, d_j) = 1` or
  `binom(e_j, 0) = 1`. Discharged by: R0.10 + `Finsupp.prod` of ones (`Finset.prod_eq_one`,
  `Finset.disjoint_left`, `Nat.choose_self`). ~10 LOC. Attacks: [2] `d = 0` ✓. SURVIVED.

- **R0.12** `[gap]` `MvPolynomial.pderiv_hasseDeriv` —
  `pderiv j (hasseDeriv d P) = ((d j + 1 : ℕ) : R) • hasseDeriv (d + single j 1) P`
  - Source: §2, proof of Lemma 1, `clean.tex:303-305`. Quote:
    > "Here ∂_jΔ_d=(d_j+1)Δ_{d+e_j} follows directly on monomials."
  - Match: identical (`e_j = Finsupp.single j 1`).
  - Discharged by: `MvPolynomial.ext` + `MvPolynomial.coeff_pderiv` (`coeff m (pderiv i p) =
    coeff (m + single i 1) p * (m i + 1)`, verified) + R0.4 + `Nat.choose_succ_right_eq`
    (`n.choose (k+1) * (k+1) = n.choose k * (n - k)`). Source: 1 line; ~25 LOC.
  - Attacks: [2] on `X^k`, coordinate `j`: `k_j < d_j` both `0`; `k_j = d_j`: LHS factor
    `(k_j - d_j) = 0`, RHS `binom(k_j, d_j+1) = 0` ✓. [5] `coeff_pderiv` signature checked.
    SURVIVED.

- **R0.13** `[gap]` `MvPolynomial.degreeOf_hasseDeriv_le` — `degreeOf j (hasseDeriv d P) ≤ degreeOf j P`.
  Source: §2, end of proof of Lemma 2, `clean.tex:435-437`: > "Since F is a determinant of an l×l
  matrix whose entries are polynomials of degree at most r_j in x_j, 1 ≤ j ≤ p, F will be of
  degree at most l r_j in each variable x_j." (The entries are Hasse derivatives of `R`; the claim
  presupposes that differentiation does not raise `degreeOf`.) Match: that presupposition.
  Discharged by: `MvPolynomial.degreeOf_le_iff` + R0.4 (`coeff e (Δ_d P) ≠ 0 → coeff (e+d) P ≠ 0`)
  + `(e + d) j ≥ e j`. ~10 LOC. Attacks: [2] `d = 0` ✓. SURVIVED.

- **R0.14** `[gap]` `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` —
  `degreeOf j P < d j → hasseDeriv d P = 0`. Source: §6, proof of Lemma 9, `clean.tex:1510-1511`:
  > "Multi-indices outside the degree box give identically zero derivatives as well." Match:
  "outside the box" means `d j > r_j ≥ degreeOf j P` for some `j`. Discharged by: `ext` + R0.4 +
  `MvPolynomial.degreeOf_lt_iff` (`coeff (e+d) P = 0` as `(e+d) j ≥ d j > degreeOf j P`). ~8 LOC.
  Attacks: [2] `P = 0` ✓. SURVIVED.

- **R0.15** `[gap]` `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` —
  `(∀ j ∈ d.support, degreeOf j f = 0) → hasseDeriv d (f * g) = f * hasseDeriv d g`
  - Source: §2, proof of Lemma 2, `clean.tex:407-420`. Quote:
    > "Let A_{μρ}=Δ_μψ_ρ and B_{νρ}=Δ_νφ_ρ, viewing both matrices in the common polynomial ring.
    > The matrix defining F is AB^T ... Explicitly, we obtain GW = det(∑_ρ Δ_μ (1/ν!)∂^ν_{x_p}
    > φ_ρ(x_p)ψ_ρ(x_1,…,x_{p-1})) = det(Δ_μ (1/ν!)∂^ν_{x_p} R)."
  - Match: the displayed identity `Δ_μ (1/ν!)∂^ν(φ_ρ ψ_ρ) = (Δ_μ ψ_ρ)((1/ν!)∂^ν φ_ρ)` is used
    without comment; it holds because an operator in some variables passes through a factor not
    involving those variables. This leaf is that fact: `f` has `degreeOf j f = 0` on the support
    of `d`.
  - Discharged by: bilinearity (`MvPolynomial.induction_on'` on `f` and `g`) + R0.2 +
    `MvPolynomial.monomial_mul` + `Finsupp` arithmetic: for `a ∈ f.support`, `a j = 0` on
    `supp d` (`degreeOf_eq_sup`/`degreeOf_le_iff`), hence `hasseCoeff d (a + b) = hasseCoeff d b`
    and `a + b - d = a + (b - d)` (`tsub_add_eq_add_tsub`-type lemma, coordinatewise). ~40 LOC.
  - Attacks: [2] `d = 0` trivial; `f = C c`: `hasseDeriv_C_mul`-like ✓; `f = X i`, `d = e_i`:
    hypothesis fails, and indeed `Δ_{e_i}(X_i g) = g + X_i Δ_{e_i} g ≠ X_i Δ_{e_i} g` — so the
    hypothesis is necessary. [3] hypothesis restricted to `d.support` (not all `j`) is the sharp
    form. SURVIVED.

- **R0.16** `[gap]` `MvPolynomial.hasseDeriv_single_aeval_X` —
  `hasseDeriv (single j n) (aeval (X j) f) = aeval (X j) (Polynomial.hasseDeriv n f)`.
  Source: §1, `clean.tex:147-150` ("Use the univariate `Polynomial.hasseDeriv` as a model") and
  §2 Lemma 2 where `(1/ν!)∂^ν_{x_p}` acts on the one-variable polynomials `φ_ρ(x_p)`. Match: the
  operator `Δ_{ν e_p}` on a polynomial in `x_p` alone is the univariate Hasse derivative.
  Discharged by: `Polynomial.induction_on'`/linearity + `Polynomial.aeval_monomial` + R0.2 +
  `Polynomial.hasseDeriv_monomial` + `MvPolynomial.X_pow_eq_monomial`. ~20 LOC.
  Attacks: [2] `f = X^m`: `Δ_{n e_j} X_j^m = binom(m,n) X_j^{m-n}` both sides ✓. SURVIVED.

- **R0.17** `[gap]` `MvPolynomial.uniqueAlgEquiv_hasseDeriv` — for `[Unique σ]`,
  `uniqueAlgEquiv R σ (hasseDeriv (single default n) P) = Polynomial.hasseDeriv n (uniqueAlgEquiv R σ P)`.
  Source: as R0.16. Match: the one-variable multivariate operator is the univariate one.
  Discharged by: R0.16 applied to `(uniqueAlgEquiv R σ).symm` + `AlgEquiv.apply_symm_apply`
  (or linearity + `MvPolynomial.uniqueAlgEquiv` on monomials). ~15 LOC. Attacks: [2] `n = 0` ✓.
  [4] mathlib renamed `pUnitAlgEquiv` → `uniqueAlgEquiv` (deprecation seen at compile); the
  statement uses the current name. SURVIVED.

- **R0.18** `[mathlib]` `MvPolynomial.hasseCoeff_le_two_pow` —
  `(∀ j, k j ≤ r j) → hasseCoeff d k ≤ 2 ^ (∑ j, r j)`.
  Source: §3, proof of Lemma 3, `clean.tex:457-461`: > "An individual Hasse derivative of such a
  term is zero or a monomial whose coefficient has absolute value at most |u_i|∏_j binom(s(i)_j,
  d_j) ≤ B 2^S." Match: `∏ binom(k_j, d_j) ≤ ∏ 2^{k_j} ≤ 2^{∑ r_j}`. Discharged by: R0.5 +
  `Nat.choose_le_two_pow` + `Finset.prod_le_prod'` + `Finset.prod_pow_eq_pow_sum`. ~8 LOC.
  Attacks: [2] `d = 0`: `1 ≤ 2^S` ✓. [5] names checked. SURVIVED.

- **R0.19** `[gap]` `MvPolynomial.factorial_smul_hasseDeriv_single` —
  `(n ! : R) • hasseDeriv (single j n) P = (pderiv j)^[n] P`.
  Source: §1, `clean.tex:134-139`: > "Over a ℚ-algebra it agrees with Δ_i = 1/(i_1!⋯i_p!)
  (∂/∂x_1)^{i_1}⋯(∂/∂x_p)^{i_p}." Match: one variable at a time, multiplied out (no division);
  the identity `n!·binom(k,n) = k(k-1)⋯(k-n+1)` holds in any semiring, exactly like mathlib's
  `Polynomial.factorial_smul_hasseDeriv`, so the `ℚ`-algebra hypothesis is dropped (attack [3]
  found it over-specified). Discharged by: induction on `n` with R0.12 (`pderiv (Δ_{n e_j} P) =
  (n+1) • Δ_{(n+1)e_j} P`) + `Function.iterate_succ'` + `Nat.factorial_succ`. ~15 LOC.
  Not used by any later leaf (documentation of the source's remark); keep as API.
  Attacks: [2] `n = 0` ✓. SURVIVED.

---

## Result R1: boxes and weights (`Roth/Box.lean`)

### Plain-English proof (source structure)

[TY] uses the box `0 ≤ j_i ≤ r_i` in Lemma 8 (`clean.tex:1050-1060`) and Lemma 9 (`r = ∏(r_i+1)`,
`clean.tex:1413-1418`), and the weight `∑ i_j/r_j` throughout §4–§7. The leaves are the
cardinality of the box and the elementary properties of the weight.

- **R1.1** `[mathlib]` `Roth.box`, `mem_box`, `card_box` — `box r = (piFinset (range (r j+1))).map
  equivFunOnFinite.symm`; `d ∈ box r ↔ ∀ j, d j ≤ r j`; `(box r).card = ∏ j, (r j + 1)`.
  Source: §6 Lemma 8 `clean.tex:1053-1056` ("0 ≤ j_1 ≤ r_1, …, 0 ≤ j_m ≤ r_m"); Lemma 9 eq. (43)
  `clean.tex:1413-1418`: > "The number of such polynomials is |𝒲| = (B_1+1)^r with r = (r_1 +
  1)⋯(r_m+1)." Match: the box is the set of exponent tuples of 𝒲's monomials; its size is the
  product. Discharged by: `Finset.mem_map`, `Fintype.mem_piFinset`, `Finset.mem_range`,
  `Finsupp.equivFunOnFinite` (for `mem_box`); `Finset.card_map`, `Fintype.card_piFinset`,
  `Finset.card_range` (for `card_box`). ~12 LOC each. Attacks: [2] `σ` empty: box `= {0}`,
  card `1 = ∏_∅` ✓; `r = 0`: box `= {0}` ✓. SURVIVED.
- **R1.2** `[mathlib]` `Roth.card_le_card_box` — `(∀ d ∈ s, ∀ j, d j ≤ r j) → s.card ≤ ∏ (r j+1)`.
  Source: §3 `clean.tex:454-456` ("Pad the monomial expansion of R by zero terms ... N =
  ∏_j(r_j+1)"). Discharged by: `Finset.card_le_card` + R1.1. ~3 LOC. SURVIVED.
- **R1.3** `[mathlib]` `Roth.weight`, `weight_nonneg`, `weight_zero`, `weight_add`, `weight_single`.
  Source: §4 definition of the index `clean.tex:535-541` ("the minimum of all numbers of the form
  i_1/r_1 + ⋯ + i_p/r_p"); nonnegativity `clean.tex:565` ("Every weight ∑_j i_j/r_j is
  nonnegative"); additivity used in `clean.tex:584-585` ("∑_j(i_j+k_j)/r_j = ind(Δ_kP) +
  ∑_jk_j/r_j"). Discharged by: `Finset.sum_nonneg`, `div_nonneg`, `Finset.sum_add_distrib`,
  `Nat.cast_add`, `add_div`, `Finsupp.single_apply`/`Finset.sum_ite_eq`. ≤ 6 LOC each. Attacks:
  [2] `r j = 0`: Lean's `x / 0 = 0`; all lemmas remain true (no positivity needed) ✓. SURVIVED.
- **R1.4** `[mathlib]` `Roth.weight_eq_zero_iff` — `(∀ j, 0 < r j) → (weight r d = 0 ↔ d = 0)`.
  Source: §4 `clean.tex:565-566`: > "Since each r_j>0, such a weight is zero exactly when every
  i_j=0." Discharged by: `Finset.sum_eq_zero_iff_of_nonneg`, `div_eq_zero_iff`, `Nat.cast_eq_zero`,
  `Finsupp.ext`. ~10 LOC. Attacks: [3] positivity of `r` is necessary (`r j = 0` makes the `j`-term
  vanish for any `d j`) ✓ matches the source's "since each r_j > 0". SURVIVED.
- **R1.5** `[mathlib]` `Roth.weight_le_card` — `(∀ j, 0 < r j) → (∀ j, d j ≤ r j) → weight r d ≤ card σ`.
  Source: §5 `clean.tex:665-668`: > "Taylor's theorem gives a nonzero derivative with 0 ≤ i_j ≤ r_j,
  of weight at most m." Discharged by: `Finset.sum_le_card_nsmul` with `d j / r j ≤ 1`
  (`div_le_one`). ~8 LOC. SURVIVED.
- **R1.6** `[mathlib]` `Roth.weight_mul_left` — `0 < l → weight (fun j => l * r j) d = weight r d / l`.
  Source: §4 end `clean.tex:646-650`: > "ind(P;α;lr) = (1/l) ind(P;α;r)". Discharged by:
  `Finset.sum_div`, `Nat.cast_mul`, `div_mul_eq_div_div`/`mul_comm`. ~6 LOC. Attacks: [2] `r j = 0`:
  `d_j/(l·0) = 0 = (d_j/0)/l` ✓. SURVIVED.
- **R1.7** `[mathlib]` `Roth.weight_le_degree_div` — `0 < m → (∀ j, m ≤ r j) → weight r d ≤ d.degree / m`.
  Source: §5 proof of Lemma 6 `clean.tex:800-806`: > "≥ θ - i_1/r_1 - ⋯ - i_{p-1}/r_{p-1} - ν/r_p
  ≥ θ - w/r_{p-1} - ν/r_p." (each `i_j/r_j ≤ i_j/r_{p-1}` since `r_{p-1}` is the smallest of
  `r_1..r_{p-1}`; summing gives `w/r_{p-1}`). Match: `m` plays the role of `r_{p-1}`. Discharged
  by: `Finset.sum_le_sum` + `div_le_div_of_nonneg_left` + `Finsupp.degree_eq_weight_one`/
  `Finsupp.degree` as `∑ d j` (`Finsupp.sum_fintype`) + `Finset.sum_div`. ~12 LOC. SURVIVED.
- **R1.8** `[mathlib]` `Roth.weight_mapDomain` — injective `f` ⇒ `weight r (d.mapDomain f) = weight (r ∘ f) d`.
  Source: §4 Lemma 4-2 `clean.tex:621-624`: > "When P is embedded into the larger polynomial ring,
  its translated monomials have zero exponent in x_p, so its index is unchanged." Match: the weight
  of an embedded exponent vector is computed in the original variables. Discharged by:
  `Finsupp.mapDomain_apply hf`, `Finsupp.mapDomain_notin_range`, `Finset.sum_map`/`Fintype.sum_equiv`
  on the range of `f` with zero terms off the range (`Finset.sum_subset`). ~20 LOC. Attacks: [3]
  injectivity needed (otherwise exponents merge and `(r ∘ f)` double counts) ✓ sharp. SURVIVED.

---

## Result R2: Taylor expansion (§4 of [TY], `Roth/Taylor.lean`)

### Plain-English proof (source structure)

[TY] §4, Theorem (Taylor's expansion), `clean.tex:502-526`: for `P` of degree `≤ r_i` in `x_i`
and `d_i ≥ r_i`, `P = ∑_{i_1≤d_1}⋯∑_{i_p≤d_p} (Δ_i P)(α) ∏(x_j-α_j)^{i_j}`. Proof: the operator
`T_d` is linear ("It is clear that T(P_1+P_2)=T(P_1)+T(P_2) and T(cP)=cT(P). So it suffices to
prove the theorem for monomials"), and on a monomial it is the product of one-variable binomial
expansions. The Lean note after the index definition (`clean.tex:546-548`) reformulates: "Let
P_α(X)=P(X+α), whose coefficient at d is (Δ_dP)(α)". The Lean development takes the translation
`taylor α P = P(X+α)` as primary (R2.1), proves the coefficient identity on monomials (R2.3, this is
the source's monomial computation), and derives the displayed expansion (R2.9, R2.10).

- **R2.1** `[gap]` `MvPolynomial.taylor` (def), `taylor_apply`, `taylor_X`, `taylor_C` —
  `taylor α = aeval fun j => X j + C (α j)`. Source: `clean.tex:546-547` ("Let P_α(X)=P(X+α)").
  Match: `P(X+α)` is the substitution `X_j ↦ X_j + α_j`. Discharged by: `rfl`, `MvPolynomial.aeval_X`,
  `MvPolynomial.aeval_C`/`algebraMap_eq`. ≤ 3 LOC each. SURVIVED.
- **R2.2** `[mathlib]` `MvPolynomial.taylor_monomial` — `taylor α (monomial k a) = C a * k.prod fun j n => (X j + C (α j))^n`.
  Source: `clean.tex:521-526` ("prove the theorem for monomials ... distribution gives
  T(x_1^{s_1}⋯x_p^{s_p}) = ∏_i T_{d_i}(x_i^{s_i})"). Discharged by: `MvPolynomial.aeval_monomial`
  (`aeval f (monomial s a) = algebraMap a * s.prod fun i k => f i ^ k`) + `algebraMap_eq`. ~3 LOC.
  SURVIVED.
- **R2.3** `[gap]` `MvPolynomial.coeff_taylor` — `coeff d (taylor α P) = eval α (hasseDeriv d P)`
  - Lean: `Roth/Taylor.lean:42`
  - Source: §4 Theorem (Taylor) and its proof, `clean.tex:502-526`, plus `clean.tex:546-548`.
    Quote: > "So it suffices to prove the theorem for monomials. For any tuple 0 ≤ s_i ≤ r_i ≤ d_i,
    distribution gives T_{d_1,…,d_p}(x_1^{s_1}⋯x_p^{s_p}) = ∏_{i=1}^p T_{d_i}(x_i^{s_i}) =
    ∏_{i=1}^p x_i^{s_i} by the one-variable binomial expansion x_i^{s_i} = ((x_i-α_i)+α_i)^{s_i}."
  - Match: both sides are `R`-linear in `P`; on `monomial k a` the left side is the coefficient of
    `X^d` in `a ∏_j (X_j+α_j)^{k_j} = a ∏_j ∑_{i_j} binom(k_j,i_j) α_j^{k_j-i_j} X_j^{i_j}`, i.e.
    `a ∏_j binom(k_j,d_j) α_j^{k_j-d_j}`, and the right side is `eval α (hasseCoeff d k • a X^{k-d})`
    — the same number. This is the source's one-variable binomial expansion per variable.
  - Discharged by: linearity (`MvPolynomial.induction_on'`), R2.2, `add_pow` (per factor),
    `Finset.prod_univ_sum` (= `∏_j ∑_{i_j} … = ∑_{f ∈ piFinset} ∏_j …`), `MvPolynomial.coeff_monomial`,
    `Finset.sum_eq_single`, R0.2, `MvPolynomial.eval_monomial`, `Finsupp.prod_fintype`. Source: 6
    lines; expect ~80 LOC (the Finsupp/piFinset bookkeeping is the bulk).
  - Attacks: [1] grep mathlib for a multivariate `taylor`/`coeff_taylor`: none; the univariate
    `Polynomial.taylor_coeff : (taylor r f).coeff n = (hasseDeriv n f).eval r` is the `σ = Unit`
    case ✓ consistent. [2] `d = 0`: `coeff 0 (P(X+α)) = P(α)` ✓ (`eval_taylor` at `0`); `α = 0`:
    `coeff d P = eval 0 (Δ_d P) = coeff 0 (Δ_d P) = hasseCoeff d d · coeff d P = coeff d P` ✓ (R0.4).
    [4] drift: the source states Taylor as an expansion with a box of summation; R2.3 is the
    coefficient-wise form the source's own Lean note prescribes; R2.10 recovers the displayed
    form. [5] `Finset.prod_univ_sum` checked. SURVIVED.
- **R2.4** `[mathlib]` `MvPolynomial.eval_taylor` — `eval x (taylor α P) = eval (fun j => x j + α j) P`.
  Source: `clean.tex:546` (`P_α(X) = P(X+α)`). Discharged by: `MvPolynomial.eval_aeval`/`eval₂_comp`
  (`eval x ∘ aeval g = eval (fun j => eval x (g j))`: `MvPolynomial.eval_aeval`? else
  `MvPolynomial.aeval_eq_eval₂Hom` + `eval₂_comp_left`), `eval_X`, `eval_C`. ~6 LOC. SURVIVED.
- **R2.5** `[mathlib]` `MvPolynomial.taylor_taylor`, `taylor_zero` — `taylor α (taylor β P) =
  taylor (α + β) P`, `taylor 0 P = P`. Source: translation semantics `clean.tex:546`. Discharged by:
  `MvPolynomial.algHom_ext` (agree on `X j`), `aeval_X`, `map_add`, `C_add`; `aeval_X_left`. ~8 LOC.
  SURVIVED.
- **R2.6** `[mathlib]` `MvPolynomial.taylor_map` — `taylor (f ∘ α) (map f P) = map f (taylor α P)`.
  Source: §1 Lean note `clean.tex:151-152` ("compatibility with coefficient maps"). Discharged by:
  `MvPolynomial.algHom_ext`-free route: `MvPolynomial.map_aeval`/`aeval_map_algebraMap`, or ext on
  coefficients via R2.3 + R0.8 + `MvPolynomial.eval_map`. ~10 LOC. SURVIVED.
- **R2.7** `[mathlib]` `MvPolynomial.taylor_rename` — `taylor α (rename f P) = rename f (taylor (α ∘ f) P)`
  (any `f`). Source: §4 Lemma 4-2 `clean.tex:621-624`. Discharged by: `MvPolynomial.aeval_rename` +
  `rename` as `aeval (X ∘ f)` (`MvPolynomial.rename` = `aeval (X ∘ f)`, `rename_eq`?) + `algHom_ext`.
  ~8 LOC. Attacks: [3] no injectivity needed here (both sides substitute `X_{f i} + α_{f i}`) ✓.
  SURVIVED.
- **R2.8** `[gap]` `MvPolynomial.degreeOf_taylor_le` — `degreeOf j (taylor α P) ≤ degreeOf j P`.
  Source: §5 `clean.tex:665-668` ("Taylor's theorem gives a nonzero derivative with 0 ≤ i_j ≤ r_j")
  and the Taylor theorem's summation box `i_j ≤ d_j` with `d_j ≥ r_j`. Match: the support of `P(X+α)`
  lies in the box of `P`. Discharged by: `MvPolynomial.as_sum` + R2.2 + `degreeOf_sum_le`,
  `degreeOf_C_mul_le`, `degreeOf_prod_le`/`degreeOf_pow_le`, `degreeOf_add_le`, `degreeOf_X`,
  `degreeOf_C`. ~25 LOC. SURVIVED.
- **R2.9** `[mathlib]` `MvPolynomial.taylor_neg_taylor`, `taylor_injective`, `taylor_eq_zero_iff`
  (`[CommRing A]`). Source: translation by `-α` inverts translation by `α` (`clean.tex:546`;
  used implicitly whenever the source passes from `P` to `P(X+α)` and back, e.g. Taylor's theorem).
  Discharged by: R2.5 (`taylor (-α) (taylor α P) = taylor 0 P = P`), `Function.LeftInverse.injective`,
  `map_zero`. ~6 LOC. SURVIVED.
- **R2.10** `[gap]` `MvPolynomial.eq_sum_box_hasseDeriv`, `eval_eq_sum_box` — Taylor's theorem in
  polynomial and evaluation form:
  `P = ∑ d ∈ box r, C (eval α (Δ_d P)) * ∏ j, (X j - C (α j)) ^ d j` for `degreeOf j P ≤ r j`, and
  `eval x P = ∑ d ∈ box r, eval α (Δ_d P) * ∏ j, (x j - α j)^(d j)`.
  - Source: §4 Theorem (Taylor), `clean.tex:502-508`. Quote: > "Let P(x_1,…,x_p) be a polynomial
    with real coefficients ... of degree at most r_i in x_i. For each i pick a natural number
    d_i ≥ r_i. Let (α_1,…,α_p)∈ℝ^p. Then P(x_1,…,x_p) = ∑_{i_1=0}^{d_1}⋯∑_{i_p=0}^{d_p}
    (Δ_{i_1,…,i_p}P)(α_1,…,α_p) ∏_{j=1}^p (x_j-α_j)^{i_j}."
  - Match: summation over the box `i_j ≤ r_j` (the source allows any `d_j ≥ r_j`; the extra terms
    vanish by R0.14, so the `d = r` form is equivalent); coefficients `(Δ_i P)(α)`; evaluation form
    used in §7 `clean.tex:1655-1658`.
  - Discharged by: `P = taylor (-α) (taylor α P)` (R2.9) + `MvPolynomial.as_sum` of `taylor α P` +
    R2.3 + `Finset.sum_subset` (support ⊆ box by R2.8 + R1.1) + R2.2 for `taylor (-α)` of a
    monomial; evaluation form by `map_sum`, `eval_mul`, `eval_prod`, `eval_pow`, `eval_sub`,
    `eval_X`, `eval_C`. Source: 7 lines; ~45 LOC.
  - Attacks: [2] `P = 0` ✓; `σ` empty (`P = C c`): `c = eval α c` ✓. [3] over a `CommRing` (needs
    subtraction) — the source works over `ℝ`; `CommRing` is the honest generality. SURVIVED.

---

## Result R3: coefficient norms and Lemma 3 (§3 of [TY], `Roth/CoeffNorm.lean`)

### Plain-English proof (source structure)

[TY] §3, Lemma 3, `clean.tex:438-490`: with `abc(f) = max|a_e|` and `‖f‖₁ = ∑|a_e|`, the triangle
inequality, multiplicativity on monomials, the derivative bound `|u_i|∏binom ≤ B2^S`, expansion of
the determinant by multilinearity and the Leibniz formula give `abc(F) ≤ ‖F‖₁ ≤ N^l l! (B 2^S)^l`.
The Lean note (`clean.tex:482-488`) prescribes: "Prove abc(f) ≤ ‖f‖₁, the triangle inequality and
submultiplicativity for ‖·‖₁, then use these for the determinant bound. Keep the sharper derivative
estimate separate: each output coefficient of a fixed Hasse derivative receives at most one input
coefficient." The leaves follow that note; with submultiplicativity the multilinear expansion over
monomials of the source is replaced by bounding each entry's `‖·‖₁` directly (R3.9), which yields
the identical bound. Lemma 9 (§6) additionally needs bounds for diagonal substitution (R3.11–R3.13)
and for evaluation (R3.15–R3.16), quoted there.

- **R3.1** `[mathlib]` `Roth.normOne` (def), `normOne_nonneg`, `normOne_zero`, `abs_coeff_le_normOne`.
  Source: `clean.tex:446-449`: > "For any polynomial f=∑_e a_eX^e, put abc(f)=max_e|a_e| (abc(0)=0),
  ‖f‖₁=∑_e|a_e|." and Lean note "Prove abc(f) ≤ ‖f‖₁". Match: `normOne` is `‖·‖₁` (real-valued, over
  `ℤ` coefficients); `abc` is not defined as a function — sup-bounds are stated as
  `∀ d, |coeff d P| ≤ B` (see `plan.md` decision 4); `abs_coeff_le_normOne` is `abc ≤ ‖·‖₁`.
  Discharged by: `Finset.sum_nonneg`, `Finset.sum_empty`, `Finset.single_le_sum` (+ `coeff d P = 0`
  when `d ∉ support`: `MvPolynomial.notMem_support_iff`). ≤ 8 LOC each. SURVIVED.
- **R3.2** `[gap]` `Roth.normOne_add_le`, `normOne_neg`, `normOne_sum_le`. Source: `clean.tex:450-451`:
  > "The triangle inequality gives ‖f+kg‖₁ ≤ ‖f‖₁+|k|‖g‖₁." Discharged by: `MvPolynomial.coeff_add`,
  `abs_add`, `Finset.sum_le_sum`, `Finset.sum_subset` (support of the sum ⊆ union; `support_add`),
  `coeff_neg`, `abs_neg`, `support_neg`; `normOne_sum_le` by `Finset.induction`. ~25 LOC total.
  Attacks: [2] `P = -Q`: `0 ≤ 2‖P‖₁` ✓. SURVIVED.
- **R3.3** `[gap]` `Roth.normOne_mul_le`, `normOne_prod_le` — `‖PQ‖₁ ≤ ‖P‖₁‖Q‖₁`.
  Source: Lean note `clean.tex:484-485` ("submultiplicativity for ‖·‖₁"), generalising
  `clean.tex:451-452` ("For monomials (including the zero polynomial), ‖f_1⋯f_l‖₁=∏‖f_ν‖₁").
  Match: the general inequality implies the monomial equality's use. Discharged by:
  `MvPolynomial.coeff_mul` (sum over `antidiagonal`), `Finset.abs_sum_le_sum_abs`, `abs_mul`,
  `Finset.sum_mul_sum`, `Finset.sum_product`/`Finset.sum_sigma`/`Finset.sum_antidiagonal_eq_sum_range`-type
  reindexing (`Finset.sum_finsuppAntidiag`-free route: bound the double sum by `∑_a∑_b|p_a||q_b|`
  via `Finset.sum_le_sum_of_subset_of_nonneg` and `Finset.sum_comm`), `support_mul`. ~50 LOC;
  `normOne_prod_le` by `Finset.induction` ~12 LOC. Attacks: [2] `P = 0` ✓. [3] `DecidableEq σ`
  only for `coeff_mul`/`antidiagonal` ✓. SURVIVED.
- **R3.4** `[mathlib]` `Roth.normOne_le_card_mul` — `(∀ d, |coeff d P| ≤ B) → normOne P ≤ card supp · B`.
  Source: `clean.tex:454-456` (padding to `N` terms each `≤ B`). Discharged by:
  `Finset.sum_le_card_nsmul` + `nsmul_eq_mul`. ~4 LOC. SURVIVED.
- **R3.5** `[gap]` `Roth.normOne_det_le` — `(∀ μ ν, ‖M μ ν‖₁ ≤ C) → ‖det M‖₁ ≤ l! C^l` (`0 ≤ C`).
  Source: `clean.tex:467-479`. Quote: > "‖det(Δ_μΔ^{(p)}_να_{f(ν)})‖₁ ≤ ∑_{σ∈S_l} ‖∏_{ν=0}^{l-1}
  Δ_{σ(ν+1)-1}Δ^{(p)}_να_{f(ν)}‖₁ = ∑_{σ∈S_l}∏_{ν=0}^{l-1}‖…‖₁ ≤ l!(B2^S)^l." Match: Leibniz
  formula + triangle inequality + (sub)multiplicativity + `|sign| = 1`; `C` plays the role of
  `B2^S` (or `N B 2^S` in R3.9). Discharged by: `Matrix.det_apply'`, R3.2 (`normOne_sum_le`),
  `Int.units`-sign handling (`Equiv.Perm.sign` is `±1`: `Int.units_eq_one_or`, `normOne_neg`,
  `one_mul`/`neg_one_mul`), R3.3 (`normOne_prod_le`), `Finset.prod_le_prod`, `Fintype.card_perm`
  (`card (Perm (Fin l)) = l!`), `Finset.sum_le_card_nsmul`. Source: 6 lines; ~40 LOC.
  Attacks: [2] `l = 0`: `det = 1`, `‖1‖₁ = 1 ≤ 0! C^0 = 1` ✓. [3] `0 ≤ C` needed for `C^l`
  monotonicity, matches the source (`B ≥ 0`). SURVIVED.
- **R3.6** `[gap]` `Roth.abs_coeff_hasseDeriv_le` — `degreeOf ≤ r`, `|coeff| ≤ B` ⇒
  `|coeff e (Δ_d P)| ≤ 2^{∑ r_j} B`. Source: `clean.tex:457-461` (quoted at R0.18) and §6
  `clean.tex:1443-1446`: > "abc(Δ_{j_1,…,j_m}W) ≤ 2^{r_1+⋯+r_m}B_1". Discharged by: R0.4, R0.18
  (`(e+d) ∈ support` ⇒ `(e+d)_j ≤ r_j` by `degreeOf_le_iff`), `abs_mul`, `Nat.abs_cast`,
  `mul_le_mul`. ~15 LOC. Attacks: [2] `coeff (e+d) P = 0`: LHS `0 ≤ 2^S B` needs `0 ≤ B`, which
  follows from `hB` at any `e` (`abs_nonneg.trans`) ✓. SURVIVED.
- **R3.7** `[gap]` `Roth.normOne_hasseDeriv_le` — `‖Δ_d P‖₁ ≤ 2^{∑ r_j} ‖P‖₁`. Source: Lean note
  `clean.tex:486-488` ("each output coefficient of a fixed Hasse derivative receives at most one
  input coefficient"). Discharged by: R0.4, `Finset.sum_le_sum_of_subset`-style injection
  `e ↦ e + d` (`add_left_injective`), R0.18, `Finset.sum_image`/`Finset.sum_le_sum`, `support`
  of `Δ_d P` ⊆ image of `(· - d)`. ~30 LOC. SURVIVED.
- **R3.8** `[gap]` `Roth.degreeOf_det_hasseDeriv_le` — `degreeOf j (det (Δ_{E μ ν} P)) ≤ l · r j`.
  Source: `clean.tex:435-437` (quoted at R0.13). Discharged by: `Matrix.det_apply'`,
  `MvPolynomial.degreeOf_sum_le`, `degreeOf_C_mul_le`-type bound for the sign (`Int.cast` of `±1`
  is `± 1`: `degreeOf_neg`), `degreeOf_prod_le`, R0.13, `Finset.sum_const`, `Finset.card_fin`.
  ~25 LOC. Attacks: [2] `l = 0`: `det = 1`, `degreeOf j 1 = 0 ≤ 0` ✓. SURVIVED.
- **R3.9** `[gap]` **Lemma 3** `Roth.abs_coeff_det_hasseDeriv_le` —
  `|coeff d (det (Δ_{E μ ν} P))| ≤ (∏(r_j+1))^l · l! · B^l · 2^{(∑ r_j) l}`.
  - Lean: `Roth/CoeffNorm.lean:117`
  - Source: §3 Lemma 3 `clean.tex:438-445`. Quote: > "Let R and F be as above, and suppose all
    the coefficients of R have absolute value bounded by B. Then all the coefficients of F have
    absolute value bounded by ((r_1+1)⋯(r_p+1))^l l! B^l 2^{(r_1+⋯+r_p)l}."
  - Match: `F` in the source is `det(Δ_μ(1/ν!)∂^ν_pR)`; the Lean statement allows arbitrary
    multi-indices `E μ ν` (the source's bound never uses the orders), so it is strictly more
    general; the bound is literally the source's.
  - Discharged by: R3.1 (`|coeff| ≤ ‖F‖₁`), R3.5 with `C := 2^S · N · B` where each entry has
    `‖Δ_{E μ ν} P‖₁ ≤ 2^S ‖P‖₁` (R3.7) and `‖P‖₁ ≤ N B` (R3.4 + R1.2), then
    `l!(2^S N B)^l = N^l l! B^l 2^{Sl}` (`mul_pow`, `pow_mul`). Source: 25 lines; ~35 LOC.
  - Attacks: [2] `P = 0`: `0 ≤ RHS` ✓ (`hB0`); `l = 0`: `|coeff d 1| ≤ 1` ✓. [3] `hB0 : 0 ≤ B`
    is needed when `P = 0` and `l` odd (else `B^l < 0` possible) — attack [2] found it; it is
    implied by `hB` whenever `P ≠ 0`, so it is harmless and the source has `B ≥ 1` anyway.
    [4] drift: none. SURVIVED.
- **R3.10** `[gap]` `Roth.diag` (def), `diag_sub`, `eval_diag`.
  Source: §6 Lemma 9 `clean.tex:1441-1442` ("the remainder of the division of
  Δ_{j_1,…,j_m}W(x,…,x) by f(x)") and `clean.tex:1505-1507`: > "Hasse differentiation, diagonal
  substitution and remainder modulo the fixed monic f are additive". Match: `diag P = P(x,…,x)` is
  `aeval (fun _ => X) P`, an algebra hom (additive); `eval_diag` is "evaluate the diagonal
  substitution at `x`" = "evaluate at `(x,…,x)`", used in `clean.tex:1508-1510`. Discharged by:
  `map_sub`; `Polynomial.eval_map`/`MvPolynomial.eval_map` + `MvPolynomial.aeval_eq_eval₂Hom` +
  `eval₂_comp`/`Polynomial.eval₂_aeval`-type composition (`MvPolynomial.eval_eval₂`...). ~15 LOC.
  SURVIVED.
- **R3.11** `[gap]` `Roth.abs_coeff_diag_le` — `|coeff n (diag P)| ≤ card supp · B`.
  Source: `clean.tex:1447-1449`. Quote: > "When we replace x_1,…,x_m by the same variable x the
  absolute value of the coefficients of the resulting polynomial is at most the number of terms of
  the polynomial, which is at most r, multiplied by the coefficient bound B_1^{1+δ}." Match:
  identical (the "number of terms" is `card supp`, bounded by `∏(r_j+1)` via R1.2). Discharged by:
  `MvPolynomial.as_sum` + `map_sum` + `aeval_monomial` (`= C a * X^{∑ k_j}`), `Polynomial.finset_sum_coeff`,
  `Polynomial.coeff_C_mul_X_pow`, `Finset.abs_sum_le_sum_abs`, `Finset.sum_le_card_nsmul`,
  `abs_ite`-bound. ~30 LOC. SURVIVED.
- **R3.12** `[gap]` `Roth.natDegree_diag_le` — `natDegree (diag P) ≤ ∑ r_j`. Source:
  `clean.tex:1463-1464` ("using s ≤ ∑_j r_j ≤ m r_1"). Discharged by: as R3.11 with
  `Polynomial.natDegree_sum_le`, `natDegree_C_mul_X_pow_le`, `Finset.sum_le_sum` (`k_j ≤ r_j`).
  ~20 LOC. SURVIVED.
- **R3.13** `[mathlib]` `Roth.geom_sum_le_one_add_pow` — `0 ≤ t → ∑_{s<r+1} t^s ≤ (1+t)^r`.
  Source: `clean.tex:1545-1547`: > "for every t≥0 and integer r≥0, ∑_{j=0}^r t^j ≤ (1+t)^r, since
  each binomial coefficient binom(r,j) is at least 1." Discharged by: `add_pow` (`(t+1)^r =
  ∑_{s ∈ range (r+1)} t^s * 1^{r-s} * binom(r,s)`), `Finset.sum_le_sum`, `Nat.one_le_iff_ne_zero`/
  `Nat.choose_pos`, `le_mul_of_one_le_right`. ~10 LOC. Attacks: [2] `r = 0` ✓; `t = 0` ✓. SURVIVED.
- **R3.14** `[gap]` `Roth.abs_eval_le` — `|eval x (map P)| ≤ B · ∏_j (1+|x_j|)^{r_j}`.
  Source: `clean.tex:1545-1552`. Quote: > "Thus the coefficient bound gives |(Δ_iQ)(α,…,α)| ≤
  abc(Δ_iQ) ∏_{j=1}^m ∑_{s=0}^{r_j}|α|^s." Match: for a general point `x`; the inner sums are
  bounded by R3.13. Discharged by: `MvPolynomial.eval_eq`/`as_sum` + `map_sum`, `Finset.abs_sum_le_sum_abs`,
  `abs_mul`, `abs_prod`, `abs_pow`, `Finset.sum_le_sum_of_subset_of_nonneg` (support ⊆ box),
  `Finset.prod_univ_sum` (box sum = product of geometric sums), R3.13, `Finset.prod_le_prod`.
  ~45 LOC. Attacks: [2] `P = 0` ✓ (`0 ≤ B`); `σ` empty: `|c| ≤ B` ✓. SURVIVED.

---

## Result R4: the one-variable Wronskian criterion (§2 of [TY], `Roth/Wronskian.lean`)

### Plain-English proof (source structure)

[TY] §2, first lemma, `clean.tex:159-196`. The Wronskian of `φ_0,…,φ_{l-1}` is
`det((1/μ!) d^μ/dt^μ φ_ν)`. *Easy direction:* a linear dependence gives a constant relation
between the columns, so the determinant vanishes. *Hard direction:* if the family is linearly
independent, replace it by invertible column operations by a basis `g_0,…,g_{l-1}` of its span
with distinct degrees `d_0<⋯<d_{l-1}` ("obtained by eliminating equal leading degrees"); the
Wronskian changes by `det A ≠ 0`. For such a family the coefficient of `t^D`,
`D = ∑ d_ν − l(l−1)/2`, in the Wronskian is `(∏ a_ν)·det(binom(d_ν, μ))`, and
`det(binom(d_ν, μ)) = ∏_{i<j}(d_j − d_i)/∏ μ! ≠ 0` because `binom(X, μ)` is `X^μ/μ! + lower`
(Vandermonde). The Lean proof follows this exactly, except that the "elimination" is organised
as a strong induction on `∑ natDegree`: each step is a single column operation that cancels one
leading coefficient (R4.6–R4.8), and the distinct-degree case is R4.3–R4.5.

- **R4.1** `[gap]` `Roth.wronskianMatrix`, `Roth.wronskian` (defs).
  Lean: `Roth/Wronskian.lean:31` —
  `wronskian φ = (Matrix.of fun μ ν => hasseDeriv (μ : ℕ) (φ ν)).det`.
  Source `clean.tex:159-163`: > "If l≥1 and φ_0(t),…,φ_{l−1}(t) are l polynomials in the variable
  t, we call the determinant W(φ_0,…,φ_{l−1})(t) = det((1/μ!) d^μ/dt^μ φ_ν(t))_{0≤μ≤l−1, 0≤ν≤l−1}
  the Wronskian of the polynomials." Match: `(1/μ!) d^μ/dt^μ = Polynomial.hasseDeriv μ` (mathlib
  `Polynomial.factorial_smul_hasseDeriv`; over a field of characteristic zero the two agree, and
  the Hasse form is what the source uses in all later estimates). Rows `μ`, columns `ν` as in the
  source. (`l = 0` is allowed in Lean: the determinant of the empty matrix is `1`; the source has
  `l ≥ 1`. All lemmas below remain true for `l = 0`, checked in their attacks.) SURVIVED.

- **R4.2** `[gap]` `Roth.wronskian_eq_zero_of_not_linearIndependent`.
  Source `clean.tex:172-173`: > "Linear dependence gives a nontrivial constant linear relation
  between the columns, so the determinant vanishes." Match: identical. Discharged by:
  `Fintype.not_linearIndependent_iff` (gives `g` with `∑ g ν • φ ν = 0`, some `g ν ≠ 0`),
  linearity of `hasseDeriv` (`map_sum`, `map_smul`), `Matrix.exists_mulVec_eq_zero_iff`
  (`K[X]` is a domain; `v := fun ν => C (g ν) ≠ 0`, `M *ᵥ v = 0`). Source: 2 lines; ~25 LOC.
  Attacks: [2] `l = 0`: the empty family is linearly independent, hypothesis false ✓. [5]
  `Matrix.exists_mulVec_eq_zero_iff` exists with `[CommRing A] [IsDomain A]` (checked by
  `#check`). SURVIVED.

- **R4.3** `[gap]` `Roth.det_choose_eq` — for `CharZero K`,
  `det (of fun μ ν => (binom(d ν, μ) : K)) = (∏ μ, (μ!)⁻¹) * ∏ i, ∏ j ∈ Ioi i, (d j − d i)`.
  - Source `clean.tex:184-194`. Quote: > "(∏ a_ν) det(binom(d_ν, μ))_{μ,ν} = (∏ a_ν)
    ∏_{0≤i<j<l}(d_j−d_i)/∏_{μ}μ! ≠ 0. Indeed, binom(X, μ) has degree μ and leading coefficient
    1/μ!, so its evaluation determinant is the Vandermonde determinant multiplied by ∏_μ 1/μ!."
  - Match: identical, with `binom(X,μ) = descPochhammer K μ / μ!`.
  - Discharged by: `descPochhammer_eval_eq_descFactorial` + `Nat.descFactorial_eq_factorial_mul_choose`
    (so `binom(d ν, μ) = (μ!)⁻¹ · (descPochhammer K μ).eval (d ν)`), `Matrix.det_mul_row` (pull the
    row factors `(μ!)⁻¹`), `Matrix.det_transpose`, `Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde`
    (with `p μ := descPochhammer K μ`, `monic_descPochhammer`, `descPochhammer_natDegree`),
    `Matrix.det_vandermonde`. Source: 4 lines; ~35 LOC.
  - Attacks: [1] grep for a direct "binomial determinant" lemma in mathlib: none
    (`Matrix.det_vandermonde_id_eq_superFactorial` is the special case `d = id`, consistent:
    `det(binom(ν,μ)) = 1`, and `∏ μ!⁻¹ · ∏_{i<j}(j−i) = ∏ μ!⁻¹ · superFactorial = 1` ✓ — a
    genuine consistency check of the formula). [2] `l = 0`: `1 = 1` ✓; `l = 1`: `binom(d_0,0) = 1
    = 0!⁻¹` ✓; `l = 2`: `det [[1,1],[d_0,d_1]] = d_1 − d_0` and RHS `1·1⁻¹·(d_1−d_0)` ✓.
    [3] `CharZero K` needed for `(μ!)⁻¹` to be meaningful/nonzero; the identity as stated is
    true in any field (it only uses `μ! ≠ 0` via the inverse — in characteristic `p` the inverse
    of `μ!` would be `0` for `μ ≥ p` and the identity could fail), so the hypothesis is sharp.
    [4] the transposition: the source's matrix has rows `μ`, columns `ν` while mathlib's lemma has
    rows = points; `det_transpose` bridges — recorded above. [5] all five names `#check`ed.
    SURVIVED.

- **R4.4** `[gap]` `Roth.sum_range_le_sum_of_injective` — injective `d : Fin l → ℕ` ⇒ `∑ ν ≤ ∑ d ν`.
  Source `clean.tex:181-182`: > "set D=∑_ν d_ν − l(l−1)/2 ≥ 0." Match: `D ≥ 0` is this inequality.
  Discharged by: induction on `l` removing a maximal value (`Finset.exists_max_image`), or
  `Finset.sum_range_id_mul_two` + `Finset.card_eq_of_bijective`; ~25 LOC. Attacks: [2] `l = 0` ✓;
  `d = id` equality ✓; non-injective `d = 0` with `l = 2`: `1 ≤ 0` ✗ — so injectivity is needed ✓
  sharp. SURVIVED.

- **R4.5** `[gap]` `Roth.coeff_wronskian_of_natDegree_injective` —
  `(wronskian φ).coeff (∑ natDegree − ∑ ν) = (∏ leadingCoeff (φ ν)) * det(binom(natDegree (φ ν), μ))`
  for nonzero `φ ν` with pairwise distinct degrees.
  - Source `clean.tex:181-196`. Quote: > "Write a_ν≠0 for the leading coefficient of g_ν and set
    D=∑_ν d_ν−l(l−1)/2≥0. The coefficient of t^D in the new Wronskian is (∏_{ν} a_ν)
    det(binom(d_ν, μ))_{μ,ν} ... All other contributions have lower total degree."
  - Match: identical; `D` is the natural number `∑ d_ν − ∑ μ` (well-defined by R4.4).
  - Discharged by: `Matrix.det_apply'` + `Polynomial.finset_sum_coeff` + per-permutation
    `Polynomial.coeff_prod_of_natDegree_le` (each factor `hasseDeriv (σ ν) (φ ν)` has `natDegree ≤
    d_ν − σ ν` by `Polynomial.natDegree_hasseDeriv_le`; the case where some `σ ν > d_ν` makes that
    factor `0` by `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree` and `binom = 0` by
    `Nat.choose_eq_zero_of_lt`, so both sides vanish), `Polynomial.hasseDeriv_coeff` at the top
    degree (`= binom(d_ν, σ ν) · leadingCoeff`), and `Finset.prod_mul_distrib` to split off
    `∏ a_ν`; the sum over permutations is then `det_apply'` of the binomial matrix. Source: 5 lines;
    ~70 LOC (the ℕ-subtraction bookkeeping is the bulk).
  - Attacks: [2] `l = 1`: `coeff (d_0) (φ_0) = a_0 · 1` ✓; `l = 2`, `φ = (1, t)`: `W = det
    [[1, t],[0, 1]] = 1`, `D = 0+1−1 = 0`, RHS `1·1·det[[1,1],[0,1]] = 1` ✓. [3] injectivity of the
    degrees is what makes `D` exact (non-injective families can have `∑(d_ν − σ ν)` collisions,
    but the formula as stated with that `D` would still be the coefficient — the sharp hypothesis
    is only `∑ ν ≤ ∑ d_ν`; we keep injectivity since that is the only use). [5] `coeff_prod_of_natDegree_le`
    `#check`ed: `(∏ i ∈ s, f i).coeff (∑ i ∈ s, n i) = ∏ i ∈ s, (f i).coeff (n i)` under
    `∀ i ∈ s, natDegree (f i) ≤ n i` ✓. SURVIVED.

- **R4.6** `[gap]` `Roth.wronskian_ne_zero_of_natDegree_injective` (`CharZero K`).
  Source `clean.tex:194-196`: > "Thus the new Wronskian, and hence the original one, is nonzero."
  Discharged by: R4.5 + R4.3 + `Matrix.det_vandermonde_ne_zero_iff` (degrees injective ⇒ the
  Vandermonde product is nonzero; `Nat.cast_injective` for `(d j : K) − d i ≠ 0`) + `Finset.prod_ne_zero_iff`
  (leading coefficients and `μ!⁻¹` nonzero, `Nat.cast_ne_zero.2 (Nat.factorial_ne_zero μ)`) +
  `Polynomial.ne_zero_of_coeff_ne_zero`. ~20 LOC. Attacks: [2] `l = 0`: `1 ≠ 0` ✓. SURVIVED.

- **R4.7** `[gap]` `Roth.wronskian_update_sub_smul` — `ν ≠ ν'` ⇒
  `wronskian (update φ ν' (φ ν' − C c * φ ν)) = wronskian φ`.
  Source `clean.tex:174-180`: > "By invertible column operations over ℚ, replace them by a basis
  g_0,…,g_{l−1} of their span having distinct degrees ... If A∈GL_l(ℚ) is this change-of-basis
  matrix, then W(g_0,…,g_{l−1})=W(φ_0,…,φ_{l−1}) det A." Match: an elementary column operation has
  `det A = 1`, so the Wronskian is unchanged; this is one step of the source's change of basis.
  Discharged by: `Matrix.det_updateCol_add_smul_self` (with `c ↦ −c`), `Function.update` vs
  `Matrix.updateCol` (`Matrix.updateCol_apply`), linearity of `hasseDeriv` (`map_sub`, `map_smul`,
  `Polynomial.C_mul'`). ~20 LOC. Attacks: [3] `ν ≠ ν'` needed (`det_updateCol_add_smul_self`
  requires it; for `ν = ν'` the operation is a scaling by `1 − c`). SURVIVED.

- **R4.8** `[gap]` `Roth.linearIndependent_update_sub_smul`, `Roth.sum_natDegree_update_lt`.
  Source `clean.tex:177-178`: > "Such a basis is obtained by eliminating equal leading degrees:
  the successive quotients of the degree filtration have dimension at most one." Match: one
  elimination step preserves linear independence (the span is unchanged) and strictly lowers the
  sum of the degrees (the leading terms cancel; the difference is nonzero by independence).
  Discharged by: `linearIndependent_iff_card_eq_finrank_span` + `Submodule.span` double inclusion
  (`Submodule.span_le`, `Submodule.sub_mem`, `Submodule.smul_mem`) for the first; for the second
  `Polynomial.degree_sub_lt` (`degree p = degree q`, `p ≠ 0`, `leadingCoeff p = leadingCoeff q`
  with `q = C (lc'/lc) * φ ν`: `Polynomial.leadingCoeff_C_mul`/`degree_C_mul`), the difference is
  `≠ 0` (else `φ ν' = C c * φ ν`, contradicting `LinearIndependent.pair_iff`/`LinearIndependent.ne_zero`),
  `Polynomial.natDegree_lt_natDegree`, `Finset.sum_lt_sum_of_nonempty`/`Finset.sum_update_of_mem`.
  ~30 + ~35 LOC. Attacks: [2] *this attack found a false statement*: with only `φ ν ≠ 0` and equal
  degrees, two nonzero constants give difference `0` and no decrease (`∑ = 0 ≮ 0`); the
  statement was corrected to assume `LinearIndependent K φ`, which excludes it (two proportional
  vectors). Re-checked: with independence the difference is nonzero, so its degree is `< natDegree
  (φ ν')` strictly and `natDegree (φ ν') ≥ 1` automatically. SURVIVED (after fix).

- **R4.9** `[internal]` `Roth.wronskian_ne_zero_of_linearIndependent` (`CharZero K`), and
  `Roth.wronskian_eq_zero_iff`.
  Source `clean.tex:174-196` (quoted above): the hard direction. Composition: strong induction on
  `∑ natDegree (φ ν)` (`Nat.strong_induction_on`); if the degrees are injective, R4.6; otherwise pick
  `ν ≠ ν'` with equal degrees (`Function.Injective` fails: `not_injective_iff`), apply R4.7 (Wronskian
  unchanged), R4.8 (independence kept, measure drops), and the induction hypothesis. `wronskian_eq_zero_iff`
  is R4.2 + R4.9. Source: 23 lines; ~30 LOC for the induction.
  Composition attack: could the children hold and the parent fail? The induction needs the
  measure in `ℕ` (`∑ natDegree`) to strictly decrease (R4.8) and the Wronskian to be preserved
  (R4.7) — both proved for the *same* update; the base of the well-founded induction is the
  injective case (R4.6), which covers `l ≤ 1` too. No gap. SURVIVED.

---

## Result R5: generalized Wronskians and Lemma 1 (§2 of [TY], `Roth/GenWronskian.lean`)

### Plain-English proof (source structure)

[TY] §2, `clean.tex:198-345`. Definition of the generalized Wronskian `det(Δ_μ φ_ν)` with
`ord Δ_μ ≤ μ` (`clean.tex:198-210`). Second lemma (`clean.tex:212-222`): a linearly dependent
family has all generalized Wronskians zero (apply `Δ_μ` to the relation; columns dependent).
**Lemma 1** (`clean.tex:224-345`): if `φ_0..φ_{l−1}` are linearly independent, some generalized
Wronskian is nonzero. Proof: (a) choose `k ≥ 2` larger than all partial degrees; set
`h_ν(t) = φ_ν(t, t^k, …, t^{k^{p−1}})`; (b) the `h_ν` are linearly independent, because a monomial
`x^s` with `s_j < k` maps to `t^{s_1+ks_2+⋯}` and base-`k` representations are unique (FACT), so
coefficients can be compared; (c) hence `W(h_0,…,h_{l−1}) ≠ 0` by the one-variable lemma; (d) by the
chain rule (FACT) and induction on `μ`, `d^μ/dt^μ h_ν = ∑_i f^μ_i(t) (Δ^{(i)}_μ φ_ν)(γ(t))` with
polynomials `f^μ_i` independent of `ν` and operators of order `≤ μ`; (e) multilinearity of the
determinant in the rows gives `W(h) = ∑_{i∈𝒮} f_i(t) W(φ; Δ^{(i_0)}_0,…)(γ(t))`, so some
generalized Wronskian is nonzero. The leaves below are (a)–(e).

- **R5.1** `[gap]` `Roth.genWronskian` (def). Source `clean.tex:198-210`: > "Suppose l≥1 and
  φ_0(x_1,…,x_p),…,φ_{l−1} are l polynomials in the p variables x_1,…,x_p. Also suppose Δ_0,…,Δ_{l−1}
  are l differential operators such that for each i the order of Δ_i is at most i. We call the
  determinant W(φ_0,…,φ_{l−1};Δ_0,…,Δ_{l−1}) = det(Δ_μφ_ν(x_1,…,x_p))_{μ,ν} a generalized
  Wronskian." Match: `genWronskian D φ = det (of fun μ ν => hasseDeriv (D μ) (φ ν))`; the order
  condition `(D μ).degree ≤ μ` is carried by the lemmas, not the definition. SURVIVED.

- **R5.2** `[gap]` `Roth.genWronskian_eq_zero_of_not_linearIndependent`.
  Source `clean.tex:212-222`: > "If φ_0,…,φ_{l−1} are polynomials over a characteristic-zero field
  and are linearly dependent over that field, then all of their generalized Wronskians are
  identically zero. Proof. Let ∑_ν c_νφ_ν=0 be a nontrivial dependence relation ... Applying each
  Δ_μ gives ∑_ν c_νΔ_μφ_ν=0. Choose ν_0 with c_{ν_0}≠0 and express that column as a linear
  combination of the other columns. Multilinearity and alternation of the determinant then give
  zero." Match: identical (Lean: any field `K`; characteristic zero is not used — attack [3]:
  the hypothesis is over-specified in the source, dropped). Discharged by: as R4.2 with the domain
  `MvPolynomial σ K` (`MvPolynomial.instIsDomain`), `Fintype.not_linearIndependent_iff`,
  `Matrix.exists_mulVec_eq_zero_iff`, `map_sum`/`map_smul`. ~25 LOC. SURVIVED.

- **R5.3** `[gap]` `Roth.kronecker` (def), `kroneckerExp`, `kronecker_monomial`.
  Source `clean.tex:226-231`: > "Let k≥2 be an integer which is bigger than the degrees of the
  polynomials φ_0,…,φ_{l−1} in each of the variables x_1,…,x_p ... For each ν let h_ν(t) =
  φ_ν(t,t^k,t^{k^2},…,t^{k^{p−1}})." and the Lean note `clean.tex:265-270`: > "Define Kronecker
  substitution as the algebra homomorphism x_j ↦ t^{k^{j−1}}". Match: `kronecker k = aeval (fun j
  => X ^ (k ^ e j))` with `e = Fintype.equivFin σ` the enumeration of the variables (for `σ = Fin
  p`, `e j = j`, i.e. `x_{j+1} ↦ t^{k^j}` exactly as the source); `kroneckerExp k d = ∑ d_j k^{e j}`
  is the exponent `s_1 + k s_2 + ⋯`. Discharged by: `MvPolynomial.aeval_monomial`, `pow_mul`,
  `Finset.prod_pow_eq_pow_sum`, `Finsupp.prod_fintype`. ~10 LOC. SURVIVED.

- **R5.4** `[mathlib]` `Roth.kroneckerExp_injOn` — `1 < k` ⇒ `kroneckerExp k` injective on
  `{d | ∀ j, d j < k}`.
  Source `clean.tex:246-250`: > "FACT: Since each s_i is strictly smaller than k, the representation
  of any natural number in the form s_1 + k s_2 + ⋯ + k^{p−1} s_p is unique." Discharged by:
  `Nat.ofDigits_inj_of_len_eq` applied to the digit lists `List.ofFn (fun i => d (e.symm i))`
  (`Nat.ofDigits_eq_sum_mapIdx`/`Nat.ofDigits` unfolding to `∑ L[i] k^i`, `List.ofFn_inj`), ~30 LOC;
  alternative: induction on `card σ` with `Nat.add_mul_div_left`/`Nat.add_mul_mod_self_left`.
  Attacks: [2] `k = 2`, `d = (1,0)`, `d' = (0,1)` in `Fin 2`: exponents `1` vs `2` distinct ✓.
  [3] `d j < k` is necessary: `(k, 0)` and `(0, 1)` both give `k` (the source's Lean note makes the
  same point: "x_2 − x_1^k maps to zero"). [5] `Nat.ofDigits_inj_of_len_eq` `#check`ed. SURVIVED.

- **R5.5** `[gap]` `Roth.coeff_kronecker`, `Roth.kronecker_eq_zero_iff`.
  Source `clean.tex:252-264`: > "Comparing the coefficient of t^{s_1+ks_2+⋯+k^{p−1}s_p} gives
  ∑_ν c_ν b^{(ν)}(s_1,…,s_p)=0 (0≤s_j<k). It follows, by collecting coefficients of the
  multivariable monomials, that ∑_ν c_νφ_ν = ∑_{0≤s_1,…,s_p<k}(∑_ν c_νb^{(ν)}(s))x^s = 0." and the
  Lean note `clean.tex:265-270`: > "prove injectivity only on the subspace where every individual
  exponent is less than k. This restriction is essential: when p≥2, the nonzero polynomial
  x_2−x_1^k maps to zero." Match: `coeff_kronecker` is the coefficient comparison for one
  monomial; `kronecker_eq_zero_iff` is injectivity on the subspace `∀ j, degreeOf j P < k`.
  Discharged by: `MvPolynomial.as_sum`, `map_sum`, R5.3, `Polynomial.finset_sum_coeff`,
  `Polynomial.coeff_C_mul_X_pow`, `Finset.sum_eq_single` with R5.4 (`degreeOf_lt_iff` gives
  `d' j < k` on the support), `MvPolynomial.ext`. ~30 + ~15 LOC. Attacks: [2] `P = X₁ − X₀^k`
  (degree `k` in `x_0`, violating the hypothesis): `kronecker = t^k − t^k = 0` with `P ≠ 0` — the
  hypothesis is sharp, exactly the source's example. SURVIVED.

- **R5.6** `[mathlib]` `Roth.linearIndependent_kronecker`.
  Source `clean.tex:233-264` ("We claim that these polynomials are linearly independent ... The
  linear independence of the φ_ν implies that every c_ν is zero.") Discharged by:
  `LinearIndependent.map` with `Disjoint (span K (range φ)) (ker (kronecker k).toLinearMap)`:
  the span lies in `MvPolynomial.restrictDegree σ K (k−1)` (`mem_restrictDegree_iff_sup`,
  `Submodule.span_le`), on which the kernel is trivial by R5.5 (`Submodule.disjoint_def`). ~25 LOC.
  Attacks: [5] `LinearIndependent.map (hv : LinearIndependent R v) (hf_inj : Disjoint (span R
  (range v)) (ker f))` `#check`ed. SURVIVED.

- **R5.7** `[gap]` `Roth.derivative_aeval` — the algebraic chain rule
  `derivative (aeval γ P) = ∑ j, derivative (γ j) * aeval γ (pderiv j P)`.
  Source `clean.tex:281-290`: > "FACT: For each ν, d/dt h_ν(t) = ∂φ_ν/∂x_1(γ(t)) + k t^{k−1}
  ∂φ_ν/∂x_2(γ(t)) + ⋯ + k^{p−1}t^{k^{p−1}−1}∂φ_ν/∂x_p(γ(t)). This is the algebraic chain rule for
  polynomial substitution." and Lean note `clean.tex:306-309`: > "prove the first-order chain rule
  using algebraic partial derivatives and polynomial induction, rather than analytic
  differentiation." Match: identical with `γ_j' = derivative (γ j)` (for `γ j = X^{k^j}` this is
  `k^j t^{k^j − 1}`). Discharged by: `MvPolynomial.induction_on` (cases `C`, `+`, `* X j`):
  `Polynomial.derivative_C`, `derivative_add`, `derivative_mul`, `MvPolynomial.pderiv_mul`,
  `pderiv_X`, `aeval_X`, `aeval_C`, `map_add`, `map_mul`, `Finset.sum_add_distrib`, `Finset.mul_sum`.
  Source: 1 display + remark; ~35 LOC. Attacks: [2] `P = X j`: `derivative (γ j) = ∑_i γ_i' [i = j]`
  ✓; `P = C a`: `0 = 0` ✓. [1] grep mathlib for `derivative_aeval`/`aeval_derivative`: the only
  related lemma is `Polynomial.derivative_comp` (univariate) ✓ no conflict. SURVIVED.

- **R5.8** `[gap]` `Roth.exists_hasseDeriv_kronecker_eq_sum` (`CharZero K`) — for every `μ` there
  are a finite set `s` of multi-indices of degree `≤ μ` and coefficients `c d ∈ K[X]` with
  `∀ P, Polynomial.hasseDeriv μ (kronecker k P) = ∑ d ∈ s, c d * kronecker k (hasseDeriv d P)`.
  - Source `clean.tex:292-305`. Quote: > "Then for each μ, there is a natural number r(μ) depending
    only on μ, polynomials f^μ_1(t),…,f^μ_{r(μ)}(t) with rational coefficients, and differential
    operators Δ^{(1)}_μ,…,Δ^{(r(μ))}_μ of order less than or equal to μ such that for all ν
    d^μ/dt^μ h_ν(t) = f^μ_1(t)(Δ^{(1)}_μφ_ν)(γ(t)) + ⋯ + f^μ_{r(μ)}(t)(Δ^{(r(μ))}_μφ_ν)(γ(t)).
    For completeness, this follows by induction on μ, uniformly for all input polynomials. For μ=0,
    use the identity operator with coefficient 1. If a term at stage μ is a(t)(Δ_dφ)(γ(t)), its
    derivative is a'(t)(Δ_dφ)(γ(t)) + a(t)∑_{j=1}^p γ_j'(t)(d_j+1)(Δ_{d+e_j}φ)(γ(t)). Here
    ∂_jΔ_d=(d_j+1)Δ_{d+e_j} follows directly on monomials. The orders are at most μ+1, and all
    coefficients are rational polynomials independent of φ."
  - Match: the Lean statement uses `Polynomial.hasseDeriv μ` on the left instead of `d^μ/dt^μ`
    (they differ by the factor `μ!`, invertible in characteristic zero — the source's Lean note
    `clean.tex:313-314`: "Convert ordinary iterated derivatives to Hasse derivatives by factorial
    scaling only over ℚ"); the family `(s, c)` is the finitely supported family of coefficient
    polynomials indexed by `d` with `|d| ≤ μ` of the note (`clean.tex:310-312`), uniform in `P`.
  - Discharged by: induction on `μ`; step: `Polynomial.hasseDeriv_comp 1 μ` + `hasseDeriv_one'`
    give `(μ+1) • hasseDeriv (μ+1) f = derivative (hasseDeriv μ f)`; divide by `(μ+1 : K) ≠ 0`
    (`Nat.cast_add_one_ne_zero`); R5.7 (chain rule) applied to `kronecker k (hasseDeriv d P)`;
    R0.12 (`pderiv j (hasseDeriv d P) = (d j+1) • hasseDeriv (d + single j 1) P`); collect into
    `s' := s ∪ s.biUnion (fun d => univ.image (d + single · 1))` with
    `c' d := (μ+1)⁻¹ • (derivative (c d) + ∑ j, ∑_{d' ∈ s, d' + single j 1 = d} c d' * derivative (γ j) * (d' j + 1))`
    (`Finset.sum_biUnion`-free: write the step sum as a sum over `s ×ˢ univ` and reindex with
    `Finset.sum_fiberwise`/`Finset.sum_image`); degrees: `Finsupp.degree_add`, `degree_single`.
    Source: 12 lines; ~90 LOC.
  - Attacks: [2] `μ = 0`: `s = {0}`, `c 0 = 1` ✓ (R0.6, `hasseDeriv_zero'`). `μ = 1`, `P = X j`:
    LHS `derivative (t^{k^j}) = k^j t^{k^j−1}`; RHS has `d = e_j` with `c e_j = derivative (γ j)`
    ✓ and `d = 0` with `c 0 = derivative 1 = 0`. [3] `CharZero` necessary for the division (in
    characteristic `p`, `d^p/dt^p = 0` but `hasseDeriv p ≠ 0`). [4] drift: none (the source itself
    says the coefficients may be taken as Hasse-normalised). SURVIVED.

- **R5.9** `[mathlib]` `Roth.det_sum_rows` — rows that are sums expand:
  `det (of fun μ ν => ∑ i ∈ s μ, c μ i * N μ i ν) = ∑ f ∈ piFinset s, (∏ μ, c μ (f μ)) * det (of fun μ ν => N μ (f μ) ν)`.
  Source `clean.tex:331-343`: > "Then multilinearity of the determinant in each row gives
  W(h_0,…,h_{l−1}) = det((1/μ!) d^μ/dt^μ h_ν) = det(∑_i (1/μ!) f^μ_i(t)(Δ^{(i)}_μφ_ν)(γ(t))) =
  ∑_{i∈𝒮} f_i(t) det(Δ^{(i_μ)}_μφ_ν(γ(t)))." Match: identical (`𝒮 = ∏_μ {1..r(μ)}` is
  `Fintype.piFinset s`). Discharged by: `Matrix.det` is `Matrix.detRowAlternating M`
  (`Matrix.det_apply`/`rfl`), `MultilinearMap.map_sum_finset` on
  `detRowAlternating.toMultilinearMap`, `MultilinearMap.map_smul_univ`, `smul_eq_mul`. ~20 LOC.
  Attacks: [2] `l = 0`: `1 = ∑_{f ∈ {∅}} 1 = 1` ✓; `l = 1`: linearity in the single row ✓.
  [5] both multilinear lemmas `#check`ed. SURVIVED.

- **R5.10** `[internal]` **Lemma 1** `Roth.exists_genWronskian_ne_zero` (`CharZero K`) —
  `LinearIndependent K φ → ∃ D, (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0`.
  - Lean: `Roth/GenWronskian.lean:93`
  - Source `clean.tex:224-227` (statement): > "If φ_0(x_1,…,x_p),…,φ_{l−1}(x_1,…,x_p) are l linearly
    independent polynomials in p variables with rational coefficients, then at least one of their
    generalized Wronskians is not identically zero." and `clean.tex:343-345` (end of proof):
    > "Since W(h_0,…,h_{l−1}) is non-vanishing, this means there is a choice of differential
    operators such that W(φ_0,…,φ_{l−1};Δ^{(i_0)}_0,…,Δ^{(i_{l−1})}_{l−1}) is non-vanishing."
  - Composition: pick `k := 2 + sup of all degreeOf` (so `1 < k` and all partial degrees `< k`);
    R5.6 gives `LinearIndependent K (kronecker k ∘ φ)`; R4.9 gives `wronskian (kronecker k ∘ φ) ≠ 0`;
    R5.8 for each `μ < l` gives `(s μ, c μ)`; R5.9 expands `wronskian (kronecker k ∘ φ)` as
    `∑_{f ∈ piFinset s} (∏ c μ (f μ)) * det (of fun μ ν => kronecker k (hasseDeriv (f μ) (φ ν)))`,
    and `RingHom.map_det` turns the inner determinant into `kronecker k (genWronskian f φ)`; if all
    `genWronskian f φ = 0` the sum vanishes (`Finset.sum_eq_zero`), contradiction; the witness `D :=
    f` has `(f μ).degree ≤ μ` by R5.8. Source: 120 lines; ~50 LOC of assembly.
  - Composition attacks: (i) could `W(h) ≠ 0` while every `genWronskian f φ = 0`? No: the expansion
    R5.9 is an identity, and `kronecker k 0 = 0`. (ii) Is the degree bound of `D` the order bound
    of the source? `Finsupp.degree d = ∑ d_j = |d|` ✓. (iii) `l = 0`: `genWronskian = 1 ≠ 0` with the
    empty `D` ✓. (iv) The source states the lemma over `ℚ`; Lean: any field of characteristic zero
    (used in R4.3, R5.8) — more general, no drift in content. SURVIVED.

---

## Result R6: Lemma 2 — `det (Δ_μ Δ^{(p)}_ν R) = U(x_1..x_{p-1}) V(x_p)` (§2 of [TY], `Roth/Separation.lean`)

### Plain-English proof (source structure)

[TY] §2 Lemma 2, `clean.tex:347-437`. For `R ≠ 0` with integer coefficients, `deg_{x_j} R ≤ r_j`:
(1) write `R = ∑_{ν<l} φ_ν(x_p) ψ_ν(x_1..x_{p-1})` with rational `φ_ν` (degree `≤ r_p`) and
`ψ_ν` (degree `≤ r_j` in `x_j`); such representations exist with `l = r_p + 1` (`φ_ν = x_p^ν`,
collecting powers of `x_p`); choosing `l` least (or, per the Lean note, a basis of the span of the
coefficient polynomials) makes both families linearly independent; (2) `W(x_p) :=` Wronskian of
the `φ_ν` is nonzero (one-variable lemma), some generalized Wronskian `G(x_1..x_{p-1})` of the `ψ_ν`
is nonzero (Lemma 1); (3) with `A_{μρ} = Δ_μψ_ρ`, `B_{νρ} = Δ_νφ_ρ`, the matrix defining `F` is
`ABᵀ`, so `F = det A · det B = GW`; (4) `F` has integer coefficients; choose `g ∈ ℚ×` with `U = gG`
integral primitive, `V = g⁻¹W`; the products `u_a v_b` are coefficients of `F`, hence integers, and a
Bézout relation `∑ z_a u_a = 1` shows every `v_b` is an integer; (5) the degrees of `U, V` are the
degrees of `F`, which are at most `l r_j`. Lean: `σ = Option τ`, `none = x_p`.

- **R6.1** `[mathlib]` `Roth.eq_mapDomain_some_add_single` — every `d : Option τ →₀ ℕ` is
  `(Finsupp.some d).mapDomain some + single none (d none)`. Source: implicit in the separation of
  variables `x_p` vs `x_1..x_{p-1}` (`clean.tex:347-349`). Discharged by: `Finsupp.ext`, cases on
  `Option`, `Finsupp.mapDomain_apply (Option.some_injective _)`, `Finsupp.mapDomain_notin_range`,
  `Finsupp.some_apply`, `Finsupp.single_apply`. ~12 LOC. Attacks: [2] `d = 0` ✓. SURVIVED.

- **R6.2** `[gap]` `Roth.coeffNone` (def), `coeff_coeffNone`, `eq_sum_X_none_pow_mul_coeffNone`,
  `degreeOf_coeffNone_le`.
  Source `clean.tex:372-376`: > "It's possible to find such a representation. For example, we can
  let l−1=r_p and φ_ν(x_p)=x_p^ν by collecting the terms in terms of the powers of x_p. This in
  particular shows that there is a choice of representation such that 1≤l≤r_p+1." Match:
  `coeffNone R ν` is the coefficient of `x_p^ν` (a polynomial in `x_1..x_{p-1}`), via mathlib's
  `optionEquivLeft : MvPolynomial (Option τ) R ≃ₐ Polynomial (MvPolynomial τ R)`; the displayed
  representation is `eq_sum_X_none_pow_mul_coeffNone`; the degree bound is "the ψ_ν's of degree at
  most r_j in x_j". Discharged by: `MvPolynomial.optionEquivLeft` unfolding on monomials
  (`optionEquivLeft_X_some`, `optionEquivLeft_X_none`, `optionEquivLeft_C`, `aeval_monomial`),
  `Polynomial.coeff_C_mul_X_pow`, `MvPolynomial.coeff_rename_mapDomain`, `coeff_X_pow_mul'`,
  `MvPolynomial.ext`, `degreeOf_le_iff`. ~30 + ~35 + ~15 LOC. Attacks: [2] `R = 0` ✓;
  `τ` empty: `R` univariate, `coeffNone R ν = C (coeff ν)` ✓. [5] the three `optionEquivLeft_*`
  lemmas `#check`ed. SURVIVED.

- **R6.3** `[gap]` `Roth.coeff_rename_mul_aeval` — coefficient of `U(x_τ)V(x_none)`:
  `coeff (a.mapDomain some + single none b) (rename some U * aeval (X none) V) = coeff a U * V.coeff b`.
  Source `clean.tex:423-425`: > "For a coefficient v_b of V and any coefficient u_a of U, the
  product u_av_b is a coefficient of F: the variables of the two factors are disjoint." Match:
  identical. Discharged by: `MvPolynomial.coeff_mul`, `Finset.sum_eq_single` on the antidiagonal
  with R6.1 (the unique decomposition), `MvPolynomial.coeff_rename_mapDomain`, `Polynomial.aeval_eq_sum_range`
  + `MvPolynomial.coeff_X_pow`. ~40 LOC. Attacks: [2] `U = 0` ✓. SURVIVED.

- **R6.4** `[gap]` `Roth.hasseDeriv_rename_mul_aeval` —
  `Δ_{d ⊕ ν}(U(x_τ)V(x_none)) = (Δ_d U)(x_τ) · (Δ_ν V)(x_none)`. Source `clean.tex:407-420`
  (quoted at R0.15; the entries of `ABᵀ`). Discharged by: R0.11 (disjoint supports: `Finsupp.support_mapDomain`
  ⊆ `some`-range, `support_single`), R0.15 twice (`rename some U` has `degreeOf none = 0`
  (`degreeOf_rename_of_injective`, `degreeOf` of a variable not in `vars`); `aeval (X none) V` has
  `degreeOf (some j) = 0`), R0.9, R0.16, `mul_comm`. ~30 LOC. Attacks: [2] `d = 0`, `ν = 0` ✓.
  SURVIVED.

- **R6.5** `[gap]` `Roth.degreeOf_rename_mul_aeval`, `degreeOf_none_rename_mul_aeval` (over a
  domain). Source `clean.tex:435-436`: > "Finally, since the variables are disjoint and both
  factors are nonzero, the individual degrees of U,V equal the corresponding degrees of F."
  Discharged by: `MvPolynomial.degreeOf_mul_eq` (domain, both factors nonzero; the zero cases are
  trivial), `degreeOf_rename_of_injective`, `degreeOf` of `aeval (X none) V` in `some j` is `0` and
  in `none` is `natDegree V` (`Polynomial.aeval_eq_sum_range`, `degreeOf_sum_le`/`degreeOf_X_pow`
  and the leading term), `rename_eq_zero_iff`-type nonvanishing. ~25 + ~25 LOC. Attacks: [3] the
  nonvanishing hypotheses `V ≠ 0` resp. `U ≠ 0` are needed for `degreeOf_mul_eq`; the other factor
  may be zero (both sides `0`). SURVIVED.

- **R6.6** `[gap]` `Roth.exists_separated_representation` (over a field `K`).
  - Source `clean.tex:349-375` and `clean.tex:376-394` and Lean note `clean.tex:428-433`. Quotes:
    > "Consider all representations of R in the form R(x_1,…,x_p) = ∑_{ν=0}^{l−1} φ_ν(x_p)
    ψ_ν(x_1,…,x_{p−1}) with φ_ν,ψ_ν polynomials with rational coefficients such that φ_ν's are of
    degree at most r_p and the ψ_ν's of degree at most r_j in x_j for 1≤j≤p−1."
    > "Among all such representations, choose one with l least. If l=1, both factors are nonzero
    since R≠0, so the independence assertions below are immediate. For l≥2, we claim φ_0(x_p),…,
    φ_{l−1}(x_p) are linearly independent. ... Similarly, ψ_0,…,ψ_{l−1} are also linearly
    independent."
    > Lean note: "Construct the separated decomposition over ℚ from a basis of the span of the
    coefficient polynomials of R in x_p."
  - Match: the Lean statement asserts exactly the existence of such a representation with
    `1 ≤ l ≤ n+1` (`n ≥ deg_{x_p} R`), both families linearly independent, `natDegree φ_ν ≤ n`,
    `degreeOf j ψ_ν ≤ degreeOf (some j) R`, following the source's Lean note (basis of the span of
    the `coeffNone R ν`) rather than the minimal-`l` argument; both give the same conclusions.
  - Discharged by: R6.2 (`R = ∑_{ν ≤ n} X_none^ν ψ'_ν` with `ψ'_ν := coeffNone R ν`); `V :=
    span K (range ψ')`, finite-dimensional (`FiniteDimensional.span_of_finite`), `l := finrank K V`,
    `1 ≤ l` since `V ≠ ⊥` (`R ≠ 0` ⇒ some `ψ'_ν ≠ 0`; `Submodule.finrank_pos_iff`), `l ≤ n+1`
    (`finrank_span_le_card`, `Finset.card_range`); basis `b := Module.finBasis K V`; `ψ ρ := b ρ`
    (independent: `b.linearIndependent`, degrees: every element of `V` satisfies the per-variable
    degree bound, a submodule — `Submodule.span_le` into the submodule of polynomials with
    `degreeOf j ≤ degreeOf (some j) R`, built from `degreeOf_add_le`, `degreeOf_C_mul_le`);
    coordinates `a ν ρ := b.coord ρ ⟨ψ' ν, subset_span⟩`; `φ ρ := ∑_{ν ≤ n} C (a ν ρ) * X^ν`
    (`natDegree_sum_le`, `natDegree_C_mul_X_pow_le`); the identity `R = ∑_ρ aeval (X none) (φ ρ) *
    rename some (ψ ρ)` by `b.sum_coord`/`Module.Basis.sum_repr` and `Finset.sum_comm`; independence
    of `φ`: a relation `∑_ρ c_ρ φ_ρ = 0` gives `∑_ρ c_ρ a ν ρ = 0` for all `ν` (`Polynomial.coeff`
    of the relation), i.e. the functional `f := ∑_ρ c_ρ • b.coord ρ` vanishes on every `ψ' ν`,
    hence on `V = span` (`LinearMap.eqOn_span`/`Submodule.span_induction`), hence `f (b ρ) = c_ρ = 0`
    (`Module.Basis.coord_apply`, `Module.Basis.repr_self`). Source: 25 lines; ~120 LOC.
  - Attacks: [2] `R = C c ≠ 0` (`n = 0`): `l = 1`, `φ = (1)`, `ψ = (C c)` ✓; `R = X_none`: `ψ' = (0,
    1)`, `V = K·1`, `l = 1`, `φ_0 = X`, `ψ_0 = 1` ✓. [3] a field is needed (bases); the source works
    over `ℚ` ✓. [4] drift: the source's minimal-`l` argument vs the basis construction — the Lean
    note in the source itself prescribes the basis route, and the *conclusions* used downstream
    (both families independent, degree bounds, `1 ≤ l ≤ r_p+1`) are identical. (ii) The
    independence-of-`φ` argument is not spelled out in the source for the basis route; it is the
    functional argument above (6 lines of linear algebra), recorded here so no replanning is needed.
    SURVIVED.

- **R6.7** `[gap]` `Roth.det_hasseDeriv_separated` —
  `det (Δ_{D μ ⊕ ν} (∑_ρ φ_ρ(x_none) ψ_ρ(x_τ))) = G(x_τ) · W(x_none)` with `G = genWronskian D ψ`,
  `W = wronskian φ`.
  - Source `clean.tex:407-420` (quoted at R0.15): "The matrix defining F is ABᵀ, so F = det A det B
    by multiplicativity and invariance under transpose. Explicitly, we obtain GW = det(∑_ρ Δ_μ
    (1/ν!)∂^ν_{x_p} φ_ρ(x_p)ψ_ρ(x_1,…,x_{p−1})) = det(Δ_μ (1/ν!)∂^ν_{x_p} R)."
  - Match: identical, with `A μ ρ = rename some (Δ_{D μ} ψ_ρ)`, `B ν ρ = aeval (X none) (Δ_ν φ_ρ)`.
  - Discharged by: `map_sum` + R6.4 (entry = `∑_ρ A μ ρ * B ν ρ = (A * Bᵀ) μ ν`, `Matrix.mul_apply`,
    `Matrix.transpose_apply`), `Matrix.det_mul`, `Matrix.det_transpose`, `RingHom.map_det` twice
    (`rename some` and `aeval (X none)` as ring homs; `AlgHom.toRingHom`). Source: 6 lines; ~35 LOC.
  - Attacks: [2] `l = 1`: `Δ_{D 0 ⊕ 0}(φ_0 ψ_0) = (Δ_{D 0}ψ_0)·φ_0` ✓ (R6.4). [5] `RingHom.map_det :
    f M.det = (f.mapMatrix M).det` `#check`ed. SURVIVED.

- **R6.8** `[gap]` `Roth.exists_sum_mul_eq_gcd` — Bézout for finsets of integers.
  Source Lean note `clean.tex:428-432`: > "Isolate the integral rescaling as a separate lemma: if
  integer coefficients u_a have gcd 1 and every product u_av_b is integral, then each rational v_b
  is integral by a Bézout relation." Discharged by: `Finset.induction_on`, `Finset.gcd_insert`,
  `Int.gcd_eq_gcd_ab` (`gcd a b = a * gcdA a b + b * gcdB a b`), `Finset.sum_insert`, `Finset.mul_sum`;
  the normalisation in `Finset.gcd` over `ℤ` is handled by `Int.gcd_eq_natAbs`/`Int.coe_gcd`. ~30 LOC.
  Attacks: [2] `s = ∅`: `0 = gcd ∅ = 0` ✓ (`Finset.gcd_empty`). SURVIVED.

- **R6.9** `[gap]` `Roth.exists_nat_smul_eq_map`, `Roth.exists_primitive_smul_eq`.
  Source `clean.tex:421-423`: > "Choose g∈ℚ× so that U=gG is an integral primitive polynomial, by
  clearing denominators and then dividing by the gcd of its coefficients." Discharged by:
  `N := ∏_{d ∈ supp} (coeff d G).den` (`Rat.den_pos`, `Finset.prod_pos`), `U₀ := ∑_{d} monomial d
  ((N * coeff d G).num)` with `Rat.mul_den_eq_num`/`Rat.den_dvd`-type lemmas (`Rat.num_div_den`,
  `(N * q).den = 1` since `q.den ∣ N`: `Rat.den_mul_eq_one_iff`?/`Rat.isInt`), `MvPolynomial.ext`,
  `coeff_map`; then `Finset.extract_gcd` (`∃ g', (∀ d ∈ s, u d = s.gcd u * g' d) ∧ s.gcd g' = 1`),
  `Finset.gcd_eq_zero_iff` (nonzero gcd since `U₀ ≠ 0`), `U := ∑ monomial d (g' d)`,
  `g := N / gcd`. ~45 + ~45 LOC. Attacks: [2] `G = 0` excluded in the second (needed: the gcd of
  no coefficients is `0`) ✓ matches `G ≠ 0` in the source. [5] `Finset.extract_gcd` exists in
  `Mathlib/Algebra/GCDMonoid/Finset.lean` (grep). SURVIVED.

- **R6.10** `[gap]` `Roth.exists_int_eq_of_gcd_eq_one` — `s.gcd u = 1 → (∀ a ∈ s, u a * v ∈ ℤ) → v ∈ ℤ`.
  Source `clean.tex:425-427`: > "Primitivity gives a finite integral linear combination ∑_a z_au_a=1,
  so v_b=∑_a z_a(u_av_b) is an integer." Discharged by: R6.8, `Finset.sum_mul`, cast lemmas
  (`Int.cast_sum`, `Int.cast_mul`); `z := ∑ z_a • (witness)`. ~15 LOC. Attacks: [2] `s = ∅`: gcd `0 ≠
  1`, vacuous ✓. SURVIVED.

- **R6.11** `[internal]` `Roth.exists_int_factors` — from `map F = U'(x_τ)V'(x_none)` over `ℚ` with
  `U', V' ≠ 0`, produce integral `U, V ≠ 0` with `F = U V`, same degrees.
  Source `clean.tex:421-428` (R6.9, R6.10 quotes) and `clean.tex:427-428`: > "Thus U,V are
  integral and nonzero, as required." Composition: R6.9 gives `g, U` with `map U = g • U'` and
  `gcd = 1`; put `V'' := g⁻¹ • V'`; by R6.3 every product `coeff a U * V''.coeff b` is the coefficient
  of `map F` (`= rename some (map U) * aeval (X none) (g⁻¹ • V')` since `g • g⁻¹ = 1`:
  `MvPolynomial.map_mul`, `map_rename`, `Polynomial.map_aeval`-compatibility), hence an integer;
  R6.10 gives `V'' = map V` for an integer `V`; `F = rename some U * aeval (X none) V` by
  injectivity of `map (Int.castRingHom ℚ)` (`MvPolynomial.map_injective`, `Int.cast_injective`);
  degrees: `degreeOf_map`-type equalities for injective maps (`MvPolynomial.degreeOf_map_of_injective`?
  else via `coeff_map` + `degreeOf_le_iff`) and invariance under nonzero scaling (`degreeOf_C_mul`
  for `c ∈ R⁰`). ~70 LOC. Composition attacks: could `V''` fail to be integral because some `u_a`
  is `0`? Bézout uses the gcd of *all* coefficients on the support, where every `u_a ≠ 0`; fine.
  Could `U` be `0`? `g ≠ 0`, `U' ≠ 0` ⇒ `map U ≠ 0`. SURVIVED.

- **R6.12** `[internal]` **Lemma 2** `Roth.exists_det_eq_mul`.
  - Lean: `Roth/Separation.lean:159`
  - Source `clean.tex:347-370` (statement). Quote: > "Let R(x_1,…,x_p) be a polynomial in p≥2
    variables with integral coefficients which is not identically zero. Let R be of degree at most
    r_j in x_j for j=1,…,p. Then there is an integer l satisfying 1≤l≤r_p+1 and there are
    differential operators Δ_0,…,Δ_{l−1} on the variables x_1,…,x_{p−1} of orders at most 0,…,l−1
    respectively such that if F(x_1,…,x_p) = det(Δ_μ (1/ν!)(∂/∂x_p)^ν R)_{0≤μ≤l−1, 0≤ν≤l−1} then
    (1) F has integral coefficients and it is not identically zero; (2) we have F = U(x_1,…,x_{p−1})
    V(x_p), where U,V are nonzero, have integral coefficients, and U is of degree at most lr_j in x_j
    for j=1,…,p−1 and V is of degree at most lr_p in x_p."
  - Match: `p ≥ 2` ↔ `σ = Option τ` (the source's `p ≥ 2` is not needed; for `τ` empty the lemma
    is still true and the Lean statement allows it). Operators on `x_1..x_{p-1}` ↔ `D μ : τ →₀ ℕ`
    embedded by `mapDomain some`; `(1/ν!)∂^ν_{x_p}` ↔ `single none ν`; (1) is implied by (2)
    (`U, V ≠ 0` in a domain) and integrality is automatic in `MvPolynomial (Option τ) ℤ`; (2) is the
    displayed conclusion, with degree bounds `degreeOf j U ≤ l r_{some j}`, `natDegree V ≤ l r_none`.
  - Composition: map `R` to `ℚ` (`R_ℚ ≠ 0` by `map_injective`); R6.6 gives `l, φ, ψ` with `R_ℚ =
    ∑ φ_ρ(x_none) ψ_ρ(x_τ)`; R4.9 gives `wronskian φ ≠ 0`; R5.10 gives `D` with `genWronskian D ψ ≠ 0`
    and `degree (D μ) ≤ μ`; R6.7 gives `map F = rename some G * aeval (X none) W`; R6.11 gives
    integral `U, V ≠ 0` with `F = U V` and `degreeOf j U = degreeOf j G`, `natDegree V = natDegree W`;
    degree bounds: `degreeOf (some j) F ≤ l r_{some j}` (R3.8) and `degreeOf (some j) F = degreeOf
    j U` (R6.5), likewise for `none`. Source: 90 lines; ~60 LOC of assembly.
  - Composition attacks: (i) the orders: R5.10 gives `(D μ).degree ≤ μ`, the source's "orders at
    most 0,…,l−1" ✓. (ii) `D μ` must not involve `x_p`: in the Lean formulation `D μ : τ →₀ ℕ` by
    construction (Lemma 1 is applied over `τ`), so there is nothing to check (the source's
    operators are "on the variables x_1,…,x_{p−1}"). (iii) The `l` of R6.6 is `≤ n + 1` with `n :=
    r none ≥ degreeOf none R` ✓ `1 ≤ l` ✓. (iv) Degree bound for `U` uses `degreeOf j U = degreeOf j
    G` (R6.11) and `degreeOf (some j) (map F) = degreeOf (some j) F` — R6.5 is applied over `ℚ` to
    `G, W` and the map preserves `degreeOf` (injective coefficient map) ✓. (v) For `τ` empty
    (`p = 1`): `G` is a `0`-variable determinant `genWronskian D ψ` with `ψ_ρ ∈ ℚ`, fine. SURVIVED.

---

## Result R7: the index (§4 of [TY], `Roth/Index.lean`)

### Plain-English proof (source structure)

[TY] §4, `clean.tex:528-650`. The index of a nonzero `P` at `α` relative to `r_1..r_p` is the
minimum of `∑ i_j/r_j` over all `i` with `Δ_i P(α) ≠ 0`; it is attained (finitely many nonzero
derivatives; at least one by Taylor's theorem); `ind(0) = +∞` by convention. Lemmas: `ind ≥ 0` and
`ind = 0 ↔ P(α) ≠ 0` (`clean.tex:558-569`); `ind(Δ_k P) ≥ ind P − ∑ k_j/r_j` by the composition
identity (`clean.tex:571-587`); `ind(P+Q) ≥ min`, `ind(PQ) = ind P + ind Q` via the translated
polynomials and lowest-weight parts (`clean.tex:589-612`); disjoint variables (`clean.tex:614-626`);
invariance under nonzero scalars and the scaling `ind(P;α;lr) = ind(P;α;r)/l` (`clean.tex:646-650`).
The Lean note (`clean.tex:546-556`, `clean.tex:628-641`) prescribes: define the index as the minimum
of the weights over the nonzero coefficients of `P(X+α)`, use `MvPowerSeries.weightedOrder` with the
natural weights `D/r_j` for the product formula, and separate lemmas for scalars, renaming,
disjoint variables and scaling.

- **R7.1** `[gap]` `Roth.index` (def). Lean: `Roth/Index.lean:31` —
  `index P α r = sInf (weight r '' (taylor α P).support)`.
  Source `clean.tex:535-548`: > "We define θ to be the minimum of all numbers of the form i_1/r_1 +
  ⋯ + i_p/r_p where the minimum is over all tuples (i_1,…,i_p) such that Δ_{i_1,…,i_p}P(α_1,…,α_p)≠0
  ... Taylor's theorem shows that at least one derivative at the chosen point is nonzero; only
  finitely many derivative multi-indices can be nonzero. Thus this is an attained minimum. We
  additionally set ind(0)=+∞." Lean note: > "Let P_α(X)=P(X+α), whose coefficient at d is
  (Δ_dP)(α). Define the index as the minimum of ∑_jd_j/r_j over its nonzero coefficients".
  Match: by R2.3 the support of `taylor α P` is `{d | (Δ_d P)(α) ≠ 0}`; `sInf` of the finite
  nonempty image is its minimum (R7.3). Convention: `index 0 α r = sInf ∅ = 0` in Lean
  (`Real.sInf_empty`) instead of `+∞`; every use of the convention in the source is of the form
  "zero polynomials cannot worsen a lower bound", which is matched by explicit `≠ 0` hypotheses
  (R7.8, R7.9) — see `plan.md` decision 3. SURVIVED.

- **R7.2** `[mathlib]` `Roth.index_le_weight` — `(Δ_d P)(α) ≠ 0 → index P α r ≤ weight r d`.
  Source `clean.tex:535-541` (definition as a minimum). Discharged by: R2.3 (`d ∈ support`),
  `csInf_le` with `BddBelow` from `Set.Finite.bddBelow` (`Finset.finite_toSet`, `Set.Finite.image`),
  `Set.mem_image_of_mem`. ~8 LOC. SURVIVED.
- **R7.3** `[mathlib]` `Roth.exists_weight_eq_index` — `P ≠ 0 → ∃ d, (Δ_d P)(α) ≠ 0 ∧ weight r d = index P α r`.
  Source `clean.tex:543-545` ("Thus this is an attained minimum"). Discharged by:
  `Set.Nonempty.csInf_mem` (finite nonempty set; nonempty since `taylor α P ≠ 0` by R2.9 and
  `MvPolynomial.support_nonempty`), R2.3. ~10 LOC. Attacks: [3] `P ≠ 0` necessary (for `P = 0` no
  `d` exists) ✓ = the source's convention. SURVIVED.
- **R7.4** `[mathlib]` `Roth.le_index_iff` — `P ≠ 0 → (c ≤ index ↔ ∀ d, (Δ_d P)(α) ≠ 0 → c ≤ weight r d)`.
  Source: definition as a minimum (`clean.tex:535-541`). Discharged by: `le_csInf` (nonempty) +
  R7.2/R7.3. ~10 LOC. SURVIVED.
- **R7.5** `[mathlib]` `Roth.index_nonneg`. Source `clean.tex:558-567`: > "We have ind(P)≥0 ...
  Every weight ∑_j i_j/r_j is nonnegative." Discharged by: `Real.sInf_nonneg` + R1.3. ~4 LOC.
  Attacks: [2] `P = 0`: `0 ≤ 0` ✓ (the source: `+∞ ≥ 0`). SURVIVED.
- **R7.6** `[gap]` `Roth.index_eq_zero_iff` — `P ≠ 0 → (∀ j, 0 < r j) → (index P α r = 0 ↔ eval α P ≠ 0)`.
  Source `clean.tex:558-569`: > "ind(P)=0 if and only if P(α_1,…,α_p)≠0. Proof. Every weight
  ∑_ji_j/r_j is nonnegative. Since each r_j>0, such a weight is zero exactly when every i_j=0. The
  minimum is attained, and Δ_0P=P, proving the equivalence. For P=0 the index is infinite, so the
  assertion remains valid." Discharged by: R7.3, R1.4, R0.6, R7.2 (`d = 0`, `weight 0 = 0`), R7.5
  (`le_antisymm`). ~15 LOC. Attacks: [3] `0 < r j` needed (R1.4). SURVIVED.
- **R7.7** `[gap]` `Roth.index_hasseDeriv_ge` — `Δ_k P ≠ 0 → index P α r − weight r k ≤ index (Δ_k P) α r`.
  - Source `clean.tex:571-587`. Quote: > "Suppose k_1,…,k_p are non-negative integers such that
    Δ_{k_1,…,k_p}P is not identically zero. Then ind(Δ_kP;α;r) ≥ ind(P;α;r) − (k_1/r_1 + ⋯ +
    k_p/r_p). Proof. Choose a multi-index i attaining the index of Δ_kP. The Hasse composition
    identity gives Δ_iΔ_kP = (∏_j binom(i_j+k_j, i_j)) Δ_{i+k}P. Since its value at α is nonzero,
    (Δ_{i+k}P)(α)≠0. Therefore ind(P) ≤ ∑_j(i_j+k_j)/r_j = ind(Δ_kP) + ∑_jk_j/r_j, as required."
  - Match: identical. Discharged by: R7.3 (for `Δ_k P`), R0.10 (`Δ_i Δ_k P = c • Δ_{i+k} P` with
    `c = hasseCoeff i (i+k) ≠ 0` as a natural number by R0.3, hence nonzero in `ℝ`:
    `Nat.cast_ne_zero`), `MvPolynomial.eval_smul`/`smul_eval`, R7.2 at `i + k`, R1.3 (`weight_add`),
    `sub_le_iff_le_add`. Source: 6 lines; ~20 LOC.
  - Attacks: [2] `k = 0`: `index P − 0 ≤ index P` ✓. [3] `Δ_k P ≠ 0` needed (source's hypothesis).
    SURVIVED.
- **R7.8** `[gap]` `Roth.le_index_sum` — a nonzero sum whose nonzero summands all have index `≥ c`
  has index `≥ c`.
  - Source `clean.tex:589-604`: > "ind(P+Q) ≥ min(ind P, ind Q) ... Write P(X+α)=∑_i a_iX^i and
    Q(X+α)=∑_i b_iX^i, and give X^i weight w(i)=∑_j i_j/r_j. All coefficients of P+Q below the
    smaller index vanish, proving the addition inequality, including the case P+Q=0." and its use
    in §5 `clean.tex:823-826`: > "Zero entries and zero permutation products have index +∞ and
    cannot worsen the lower bound."
  - Match: the finite-sum form with the `+∞` convention replaced by the hypothesis "every nonzero
    summand has index `≥ c`", applied to a nonzero sum (the only case where a lower bound is used).
  - Discharged by: R7.4 (for the sum), `map_sum` for `hasseDeriv` and `eval` (`MvPolynomial.eval_sum`),
    `Finset.exists_ne_zero_of_sum_ne_zero`, R7.4 (for the summand). ~15 LOC.
  - Attacks: [2] `s = ∅`: sum `0`, hypothesis `0 ≠ 0` false ✓; `s = {i}` ✓. [4] drift: the source
    states `min`; the finite-sum-with-common-bound form is exactly how the min is used in Lemma 6
    (`clean.tex:826-840`). SURVIVED.
- **R7.9** `[gap]` `Roth.index_mul` — `P ≠ 0 → Q ≠ 0 → (∀ j, 0 < r j) → index (P*Q) = index P + index Q`.
  - Source `clean.tex:589-612`. Quote: > "ind(PQ) = ind(P)+ind(Q) ... For multiplication, if either
    factor is zero, both sides are +∞. Otherwise let u=ind(P) and v=ind(Q), and let P_u,Q_v be the
    sums of terms of weights exactly u,v in the translated polynomials. They are nonzero. Since the
    polynomial ring over ℝ is an integral domain, P_uQ_v≠0. All its terms have weight u+v, while every
    term involving a higher-weight component has weight strictly greater than u+v. Thus the lowest
    nonzero weight of the product is exactly u+v." Lean note `clean.tex:628-632`: > "For integral
    r_j, apply weightedOrder_mul through translation and the normalisation just described, under a
    no-zero-divisors assumption."
  - Match: the lowest-weight-part argument is exactly mathlib's proof of
    `MvPowerSeries.weightedOrder_mul` (via `weightedHomogeneousComponent`); we import it through the
    bridge R7.15, as the source's note prescribes.
  - Discharged by: R7.15 (three times), `taylor` is multiplicative (`map_mul`), `MvPolynomial.coe_mul`,
    `MvPowerSeries.weightedOrder_mul`, `ENat.toNat_add` (both orders finite:
    `MvPowerSeries.weightedOrder_eq_top_iff`, `MvPolynomial.coe_inj`/`coe_eq_zero`), `Nat.cast_add`,
    `add_div`. Source: 7 lines; ~30 LOC.
  - Attacks: [1] mathlib: `MvPowerSeries.weightedOrder_mul (w) (f g) : (f*g).weightedOrder w =
    f.weightedOrder w + g.weightedOrder w` under `[NoZeroDivisors R]` (read from source, line 146 of
    `NoZeroDivisors.lean`) ✓ `ℝ` qualifies. [2] `P = Q = 1`: `0 = 0 + 0` ✓; `P = X_j`, `Q = X_j`, `α =
    0`: `index (X_j²) = 2/r_j = 1/r_j + 1/r_j` ✓. [3] `0 < r j` needed to form the natural weights
    `D / r_j` and for `index_eq_weightedOrder_div`; nonvanishing needed (`index 0 = 0` would break
    additivity: `index (0 * Q) = 0 ≠ 0 + index Q`) — exactly the source's `+∞` caveat. SURVIVED.
- **R7.10** `[gap]` `Roth.index_prod` — `(∀ i ∈ s, f i ≠ 0) → index (∏ f) = ∑ index (f i)`.
  Source `clean.tex:826-833`: > "ind ∏_{ν=0}^{l−1} Δ_{σ(ν+1)−1}(1/ν!)∂^ν R ≥ ∑_{ν=0}^{l−1} ind
  Δ_{σ(ν+1)−1}(1/ν!)∂^ν R" (Lemma 4-1 iterated). Discharged by: `Finset.induction_on`, R7.9,
  `Finset.prod_ne_zero_iff` (domain), `index 1 = 0` (R7.6 with `eval α 1 = 1 ≠ 0`). ~15 LOC.
  Attacks: [2] `s = ∅`: `index 1 = 0 = ∑_∅` ✓. SURVIVED.
- **R7.11** `[gap]` `Roth.index_neg`, `Roth.index_C_mul` (`c ≠ 0`). Source `clean.tex:646-648`:
  > "For nonzero c and l>0, the same definition gives ind(cP;α;r)=ind(P;α;r)" and `clean.tex:825`:
  > "Multiplication by a sign does not change the index." Discharged by: `map_neg`/`map_mul`,
  `taylor_C`, `MvPolynomial.support_neg`, `MvPolynomial.support_C_mul`/`support_smul_eq` (field,
  `c ≠ 0`), `congrArg sInf`. ~8 LOC each. Attacks: [2] `P = 0` ✓ both `0`. SURVIVED.
- **R7.12** `[mathlib]` `Roth.index_mul_left_weights` — `0 < l → index P α (l•r) = index P α r / l`.
  Source `clean.tex:646-650`: > "ind(P;α;lr) = (1/l) ind(P;α;r), with the second identity
  interpreted in the extended nonnegative reals." Discharged by: R1.6 (`weight (l•r) = weight r /
  l` pointwise), `Set.image_image`/`Set.image_congr`, `Real.sInf_smul_of_nonneg` (`sInf (a • s) = a •
  sInf s`, `a = l⁻¹ ≥ 0`), `div_eq_inv_mul`. ~12 LOC. Attacks: [2] `P = 0`: `0 = 0/l` ✓ (so the
  Lean convention is compatible with the "extended reals" reading). SURVIVED.
- **R7.13** `[gap]` `Roth.index_rename` — injective `f` ⇒ `index (rename f P) α r = index P (α ∘ f) (r ∘ f)`.
  Source `clean.tex:621-624` (Lemma 4-2 proof, quoted at R1.8) and note `clean.tex:638-640`
  ("invariance under ... variable renaming"). Discharged by: R2.7, `MvPolynomial.support_rename_of_injective`
  (`support (rename f Q) = (support Q).map (mapDomain f)`), `Finset.coe_map`, `Set.image_image`, R1.8.
  ~15 LOC. Attacks: [3] injectivity required (R1.8). SURVIVED.
- **R7.14** `[mathlib]` `Roth.index_le_card` — `P ≠ 0`, `0 < r`, `degreeOf j P ≤ r j` ⇒ `index ≤ card σ`.
  Source `clean.tex:665-668` (quoted at R1.5). Discharged by: R7.3, R2.8 (`d ∈ box r`), R1.5. ~8
  LOC. SURVIVED.
- **R7.15** `[gap]` `Roth.weight_eq_finsuppWeight_div`, `Roth.index_eq_weightedOrder_div` — the
  bridge to `MvPowerSeries.weightedOrder` with weights `D / r_j`, `D = ∏ r_i`.
  - Source Lean note `clean.tex:549-556`: > "For positive integral r_j, an alternative is to set
    D=∏_jr_j and use the natural weights w_j=D/r_j in MvPowerSeries.weightedOrder, then divide the
    finite value by D after embedding P_α as a power series."
  - Match: `weight r d = (Finsupp.weight w d)/D` because `(D/r_j)·d_j/D = d_j/r_j` (exact division
    in `ℕ`: `r_j ∣ D` by `Finset.dvd_prod_of_mem`, `Nat.cast_div`); then the minimum over the
    support of the integer weights, divided by `D`, is the index.
  - Discharged by: `Finsupp.weight_apply`, `Finset.sum_div`, `Nat.cast_div` (`Nat.div_mul_cancel`),
    `Finset.dvd_prod_of_mem`; for the order: `MvPowerSeries.weightedOrder_le` (`coeff d ≠ 0 → order ≤
    weight w d`), `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder` (attained),
    `MvPolynomial.coeff_coe`, `le_antisymm` with R7.2/R7.3, `ENat.coe_toNat` (`order ≠ ⊤` by
    `weightedOrder_eq_top_iff`). Source: 4 lines; ~15 + ~40 LOC.
  - Attacks: [2] `σ` empty: `D = 1`, `w = 0`, `weight = 0`, `index = 0`, `order 0 = 0` ✓. [3]
    positivity of `r` required for `r_j ∣ D` to give the right quotient (`D / r_j` for `r_j = 0`
    would be `0`) ✓ matches "positive integral r_j". [5] the four `MvPowerSeries` names read from
    `Order.lean:171-207` ✓. SURVIVED.
- **R7.16** `[gap]` `Roth.index_unique` — one variable: `P ≠ 0` ⇒ `index P α r = rootMultiplicity
  (α default) (uniqueAlgEquiv ℝ σ P) / r default`.
  Source `clean.tex:677-679`: > "Let t∈ℕ be the multiplicity of h_1/q_1 as a root of R; Taylor's
  theorem gives θ=ind(R;h_1/q_1;r_1)=t/r_1." Lean note `clean.tex:692-693`: > "First identify the
  one-variable index with t/r_1, where t is the natural-number root multiplicity." Discharged by:
  the support of `taylor α P` corresponds under `uniqueAlgEquiv` to the support of
  `Polynomial.taylor (α default) P'` (`uniqueAlgEquiv` commutes with translation: `algHom_ext` on
  `X`), `Polynomial.rootMultiplicity_eq_natTrailingDegree` (`= (taylor t p).natTrailingDegree`),
  `Polynomial.natTrailingDegree_le_of_ne_zero`, `Polynomial.coeff_eq_zero_of_lt_natTrailingDegree`,
  `Polynomial.trailingCoeff_nonzero_iff_nonzero`, R1.3 (`weight_single`), `sInf` of
  `{n / r : n ∈ supp}` is `(min n)/r` (`csInf_le`/`le_csInf`, `div_le_div_of_nonneg_right`). ~50 LOC.
  Attacks: [2] `P = C c ≠ 0`: multiplicity `0`, index `0` ✓; `P = X − C a`, `α = a`: multiplicity
  `1`, index `1/r` ✓. SURVIVED.

---

## Result R8: `ℛ_m`, `Θ_m` and Lemma 5 (§5 of [TY], `Roth/Theta.lean`)

### Plain-English proof (source structure)

[TY] §5, `clean.tex:652-702`: `ℛ_m(B; r)` = nonzero integer polynomials of degree `≤ r_j` in `x_j`
with coefficients bounded by `B`; `Θ_m(B; q; r)` = sup of `ind(R; h/q; r)` over `R ∈ ℛ_m` and
`gcd(h_i,q_i)=1`; well-defined with `0 ≤ Θ_m ≤ m` (the constant `1` is allowed; Taylor gives a
nonzero derivative of weight `≤ m`); nondecreasing in `B`. **Lemma 5** (`clean.tex:671-690`):
`Θ_1(B;q_1;r_1) ≤ log B/(r_1 log q_1)` for `q_1 > 1`: the index is `t/r_1` with `t` the root
multiplicity of `h_1/q_1`; `(q_1x_1−h_1)^t` is primitive and divides `R` over `ℚ`, so by Gauss's
lemma `R = (q_1x_1−h_1)^tQ` with integral `Q ≠ 0`; comparing leading coefficients `B ≥ |lc R| ≥
q_1^t`; take logarithms and the supremum.

- **R8.1** `[gap]` `Roth.RSet`, `Roth.indexSet`, `Roth.Θ` (defs); `one_mem_RSet`, `indexSet_nonempty`,
  `indexSet_bddAbove`, `index_le_Θ`, `Θ_nonneg`, `Θ_le_card`, `Θ_le_of_forall_index_le`, `Θ_mono`.
  Source `clean.tex:655-669`: > "be the set of polynomials R(x_1,…,x_m) ... such that: (1) R has
  integral coefficients and is not identically zero; (2) R has degree at most r_j in x_j for
  1≤j≤m; (3) the coefficients of R have absolute values not exceeding B. ... We define
  Θ_m(B;q_1,…,q_m;r_1,…,r_m) to be the supremum of the numbers ind(R;h_1/q_1,…,h_m/q_m;r_1,…,r_m)
  over all R∈ℛ_m(B;r_1,…,r_m) and integers h_i with gcd(h_i,q_i)=1. This supremum is well-defined and
  satisfies 0≤Θ_m≤m: the constant polynomial 1 with every h_i=1 is allowed, and Taylor's theorem
  gives a nonzero derivative with 0≤i_j≤r_j, of weight at most m. Also, Θ_m is nondecreasing in B,
  since increasing B enlarges the set of allowed polynomials." Lean note `clean.tex:696-699`: > "For
  Θ_m, record nonemptiness and boundedness of the defining family, together with lemmas for
  bounding an individual index and monotonicity in B, before using the supremum."
  Match: `RSet B r` is (1)–(3) (coefficients in `ℤ`, bound in `ℝ`); `indexSet` is the set of
  numbers, with `IsCoprime (h j) (q j)` for `gcd = 1`; `Θ = sSup`. Discharged by: `MvPolynomial.coeff_one`,
  `degreeOf_one`; `isCoprime_one_left`; R7.14 (`index ≤ card`, with `map R ≠ 0` by `MvPolynomial.map_injective
  (Int.castRingHom ℝ) Int.cast_injective`); `le_csSup`, `csSup_le`, `csSup_le_csSup` (`Real` is a
  `ConditionallyCompleteLinearOrder`), `Set.Nonempty`, `BddAbove`. ≤ 15 LOC each. Attacks: [2] `B < 1`:
  `indexSet` may be empty and `sSup ∅ = 0` — the lemmas assume `1 ≤ B` as the source does ("real
  number B ≥ 1"); `Θ_le_of_forall_index_le` also needs `1 ≤ B` (nonempty) — recorded in its
  hypotheses. [3] `IsCoprime (h j) (q j : ℤ)` ↔ `gcd = 1` (`Int.isCoprime_iff_gcd_eq_one`) ✓. SURVIVED.
- **R8.2** `[gap]` `Roth.Θ_equiv` — `Θ B (q ∘ e) (r ∘ e) = Θ B q r` for `e : σ ≃ τ`.
  Source Lean note `clean.tex:638-640` ("variable renaming"), used in Lemma 7's induction (passing
  between `Fin (n+1)` and `Option (Fin n)`). Discharged by: `indexSet` equality via `R ↦ rename e R`
  (`MvPolynomial.rename` bijective: `renameEquiv`), `degreeOf_rename_of_injective`,
  `coeff_rename_mapDomain` (coefficient bounds), R7.13 (`index_rename`), `isCoprime` transported by
  `h ↦ h ∘ e.symm`, `Set.ext`. ~40 LOC. Attacks: [2] `e = Equiv.refl` ✓. SURVIVED.
- **R8.3** `[gap]` `Roth.exists_eq_pow_mul_of_rootMultiplicity` — `R ≠ 0`, `0 < q`, `IsCoprime h q`
  ⇒ `R = (C q * X − C h)^t * Q` with `t := rootMultiplicity (h/q) (R.map ℚ)`.
  - Source `clean.tex:679-684`. Quote: > "The polynomial (q_1x_1−h_1)^t is primitive and divides R
    over ℚ. Gauss's lemma therefore gives a nonzero Q∈ℤ[x_1] with R(x_1)=(q_1x_1−h_1)^tQ(x_1)."
    Lean note `clean.tex:693-695`: > "Use Gauss's lemma for the primitive polynomial (q_1X−h_1)^t".
  - Discharged by: `Polynomial.pow_rootMultiplicity_dvd` (over `ℚ`: `(X − C (h/q))^t ∣ R_ℚ`),
    `C q * X − C h = C q * (X − C (h/q))` over `ℚ` (`q ≠ 0`), `IsUnit (C q)` ⇒ `(C q X − C h)^t ∣ R_ℚ`
    (`Units.dvd_mul_left`/`mul_dvd_mul`), primitivity: `Polynomial.isPrimitive_iff_isUnit_of_C_dvd`
    (a constant dividing `C q X − C h` divides `q` and `h`, so is a unit by `IsCoprime.isUnit_of_dvd'`),
    `Polynomial.IsPrimitive.mul` (powers), `Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast`,
    `Polynomial.map_pow`, `Polynomial.map_sub`, `map_C`, `map_X`. Source: 3 lines; ~45 LOC.
  - Attacks: [2] `t = 0`: `R = 1 * R` ✓; `R = C q X − C h`: `t = 1`, `Q = 1` ✓. [3] coprimality is
    needed for primitivity (e.g. `q = 2, h = 2`: `2X − 2` is not primitive; indeed `R = X − 1` has
    `t = 1` but `2X − 2 ∤ X − 1` in `ℤ[X]`) ✓ sharp. [5] `IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast
    (p q : ℤ[X]) (hp : p.IsPrimitive) : p ∣ q ↔ map (Int.castRingHom ℚ) p ∣ map (Int.castRingHom ℚ)
    q` `#check`ed. SURVIVED.
- **R8.4** `[gap]` `Roth.pow_rootMultiplicity_le` — with `|coeff n R| ≤ B` for all `n`, `q^t ≤ B`.
  Source `clean.tex:685-688`: > "Comparing nonzero leading coefficients yields B ≥ |lc(R)| =
  q_1^t|lc(Q)| ≥ q_1^t." Discharged by: R8.3, `Polynomial.leadingCoeff_mul`, `leadingCoeff_pow`,
  `Polynomial.leadingCoeff` of `C q * X − C h` is `q` (`leadingCoeff_C_mul_X` after writing it as
  `C q * X + C (−h)`: `Polynomial.leadingCoeff_linear`? or `natDegree`/`coeff` computation),
  `Q ≠ 0` (else `R = 0`), `Int.one_le_abs`, `abs_mul`, `Nat.cast_pow`, `Int.cast_abs`. ~30 LOC.
  Attacks: [2] `t = 0`: `1 ≤ B` follows from `R ≠ 0` (some `|coeff| ≥ 1`) ✓. SURVIVED.
- **R8.5** `[internal]` **Lemma 5** `Roth.Θ_unique_le` — for `[Unique σ]`, `1 ≤ B`, `1 < q default`,
  `0 < r default`: `Θ B q r ≤ log B / (r default * log (q default))`.
  - Source `clean.tex:671-690` (statement): > "Suppose additionally that q_1>1. Then we have
    Θ_1(B;q_1;r_1) ≤ log B/(r_1 log q_1)." Proof quoted in R7.16, R8.3, R8.4 and `clean.tex:688-690`:
    > "Since log q_1>0 and r_1>0, taking logarithms gives θ≤log B/(r_1 log q_1). Taking the supremum
    proves the claim."
  - Composition: `Θ_le_of_forall_index_le` (R8.1); for `R ∈ RSet`, `h` coprime: R7.16 gives `index =
    t/r` with `t = rootMultiplicity (h/q) (uniqueAlgEquiv ℝ σ (map R))` = the `ℚ`-multiplicity
    (`Polynomial.eq_rootMultiplicity_map` for the injective `ℚ → ℝ` and the compatibility of
    `uniqueAlgEquiv` with `map`); R8.4 gives `q^t ≤ B`; `Real.log_le_log`, `Real.log_pow`,
    `div_le_div_iff` with `log q > 0` (`Real.log_pos`, `1 < q`) and `r > 0`. ~40 LOC of assembly.
  - Composition attacks: (i) the coefficient bound of `R` as a univariate polynomial: `coeff n
    (uniqueAlgEquiv ℤ σ R) = coeff (single default n) R` (R6.14-type lemma `coeff_uniqueAlgEquiv_symm`
    applied to the inverse) ✓ provided by `Roth.coeff_uniqueAlgEquiv_symm`. (ii) `B = 1`: `Θ ≤ 0`,
    consistent with `Θ ≥ 0` (every `R` has a coefficient `±1`, `t = 0` forced) ✓. SURVIVED.

---

## Result R9: Lemma 6 (§5 of [TY], `Roth/Theta.lean`, section `Lemma6`)

### Plain-English proof (source structure)

[TY] §5 Lemma 6, `clean.tex:704-933`. For `R ∈ ℛ_p(B;r)` and `h` coprime to `q`: Lemma 2 gives
`l ≤ r_p+1`, operators `Δ_μ`, and `F = UV`; Lemma 3 bounds the coefficients of `F` by `M`
(using `r_1 > ⋯ > r_p`), hence those of `U, V` (coefficients of `F` are products `u_a v_b`, with
`abc ≥ 1`); so `U ∈ ℛ_{p−1}(M; lr)`, `V ∈ ℛ_1(M; lr_p)`, and by the scaling identity and Lemma 4-2,
`ind F ≤ lΦ` (17). Lower bound: each entry `Δ_i (1/ν!)∂^ν R` has index `≥ θ − ∑ i_j/r_j − ν/r_p ≥
θ − δ − ν/r_p` (as `w ≤ l−1 ≤ r_p`, `r_p/r_{p−1} < δ`), hence `≥ max(0, θ−ν/r_p) − δ`; by the
Leibniz expansion and Lemma 4-1, `ind F ≥ ∑_{ν<l} max(0, θ−ν/r_p) − lδ`. If `θr_p ≤ 10` then `θ <
δ < 2√δ` and we are done; otherwise two FACTs give `∑ ≥ min(lθ/2, r_pθ²/3)`. Combining with (17):
either `θ ≤ 2(Φ+δ)` or `r_pθ²/3 ≤ (r_p+1)(Φ+δ) < (4/3)r_p(Φ+δ)`, so `θ < 2(Φ+δ)^{1/2} ≤ 2(Φ^{1/2}
+ δ^{1/2})`. In Lean the variables are `Option τ` (`none = x_p`) and the hypotheses of Lemma 6 are
the ones its proof uses: `r_p > 10/δ`, `r_p < δ r_j` for all `j ≠ p` (from the chain), `r_j ≤ r_1`.

- **R9.1** `[gap]` `Roth.lem6M`, `Roth.lem6Φ` (defs). Source `clean.tex:716-724`: > "Φ = Θ_1(M;q_p;
  lr_p) + Θ_{p−1}(M;q_1,…,q_{p−1};lr_1,…,lr_{p−1}) and M = (r_1+1)^{pl} l! B^l 2^{plr_1}." Match:
  `lem6M p r₁ B l` with `p = card τ + 1 = card (Option τ)`; `lem6Φ q r M l` has the `Θ` over `Unit`
  (one variable, `q_p = q none`, `l r_p`) and over `τ` (`q ∘ some`, `l · r ∘ some`). SURVIVED.
- **R9.2** `[gap]` `Roth.floor_sq_div_two_le_sum` — `0 ≤ a → ⌊a⌋²/2 ≤ ∑_{ν ≤ ⌊a⌋} (a − ν)`.
  Source `clean.tex:862-881`: > "FACT: For any α≥0 we have ∑_{0≤ν≤α}(α−ν) ≥ ½[α]². Proof of fact:
  ∑(α−ν) = α([α]+1) − ∑_{0≤ν≤[α]}ν = α([α]+1) − [α]([α]+1)/2 = ([α]+1)(α − [α]/2) = ([α]+1)([α]/2 +
  {α}) ≥ [α]·[α]/2." Discharged by: `Finset.sum_sub_distrib`, `Finset.sum_const`, `Finset.card_range`,
  `Finset.sum_range_id_mul_two` (`(∑_{i<n} i) * 2 = n(n−1)`), `Nat.floor_le`, `Nat.lt_floor_add_one`,
  `nlinarith`. ~20 LOC. Attacks: [2] `a = 0`: `0 ≤ 0` ✓; `a = 1.5`: `⌊a⌋ = 1`, sum `1.5 + 0.5 = 2 ≥
  0.5` ✓. SURVIVED.
- **R9.3** `[mathlib]` `Roth.sq_div_three_lt_floor_sq_div_two` — `10 < a → a²/3 < ⌊a⌋²/2`.
  Source `clean.tex:883-893`: > "FACT: If α>10, then [α]²/2 > α²/3. Proof of fact: put n=[α]. Since
  α>10, we have n≥10 and α<n+1≤(11/10)n. Therefore α² < (121/100)n² < (3/2)n², which is equivalent
  to n²/2 > α²/3." Discharged by: `Nat.lt_floor_add_one`, `Nat.le_floor` (`10 ≤ ⌊a⌋`), `nlinarith`.
  ~10 LOC. Attacks: [2] `a = 10.5`: `⌊a⌋ = 10`, `50 > 36.75` ✓; `a = 10` excluded (`a > 10`) but
  `50 > 33.3` would still hold; sharpness is not an issue. SURVIVED.
- **R9.4** `[gap]` `Roth.min_le_sum_max` — `0 < r_p`, `10 < θ r_p` ⇒
  `min (lθ/2) (r_pθ²/3) ≤ ∑_{ν<l} max 0 (θ − ν/r_p)`.
  - Source `clean.tex:855-914`. Quotes: > "Let θr_p<l. Then in order for max(0,θ−ν/r_p) to be
    positive, we need ν<θr_p. We may include the zero endpoint and sum over ν≤θr_p.
    ∑_{ν=0}^{l−1}max(0,θ−ν/r_p) = ∑_{0≤ν≤θr_p}(θ−ν/r_p) = r_p^{−1}∑_{0≤ν≤θr_p}(θr_p−ν)." ...
    > "By applying these two facts we see that the expression is bounded below by ≥ ½r_p^{−1}[θr_p]²
    > ⅓r_pθ². If θr_p≥l, ∑_{ν=0}^{l−1}max(0,θ−ν/r_p) = ∑_{ν=0}^{l−1}(θ−ν/r_p) ≥ ½lθ. In order to see
    this last inequality we proceed as follows: ∑(θ−ν/r_p) = lθ − (1/r_p)·l(l−1)/2 ≥ lθ − (1/r_p)·l²/2
    ≥ lθ − ½lθ = ½lθ. Here we have used −l/r_p ≥ −θ. Combining everything, we obtain ind F ≥
    min(½lθ, ⅓r_pθ²) − lδ." Lean note `clean.tex:915-921`: > "Extract the bound for ∑_{ν<l}
    max(0,θ−ν/r_p) into a numerical lemma with explicit positivity hypotheses. Split the argument
    into θr_p≤10, 10<θr_p<l, and l≤θr_p".
  - Match: the numerical lemma of the note (the `θ r_p ≤ 10` case is handled in R9.7).
  - Discharged by: case `l ≤ θ r_p`: `Finset.sum_congr` (`max 0 x = x` as `ν/r_p ≤ (l−1)/r_p < θ`),
    `Finset.sum_sub_distrib`, `Finset.sum_range_id_mul_two`, `nlinarith` (`min_le_left`); case `θ r_p
    < l`: `Finset.sum_le_sum_of_subset_of_nonneg` (restrict to `range (⌊θr_p⌋+1) ⊆ range l`, terms
    `≥ 0`: `le_max_left`), R9.2 (after `Finset.sum_div`/`max_eq_right` on that range), R9.3,
    `min_le_right`. Source: 20 lines; ~50 LOC.
  - Attacks: [2] `l = 0`: `min 0 _ ≤ 0` ✓ (`0 < r_p θ²`); `l = 1`: `min (θ/2) (…) ≤ max 0 θ = θ` ✓.
    [3] `10 < θ r_p` is needed for R9.3 (the source's case split). SURVIVED.
- **R9.5** `[gap]` `Roth.sum_max_sub_le_index_det` — the lower bound
  `∑_{ν<l} max 0 (θ − ν/r_none) − lδ ≤ index F`, where `θ = index R α r` and `δ` bounds the weights of
  all multi-indices of degree `≤ l−1` in the `τ`-variables.
  - Source `clean.tex:786-854`. Quotes: > "Let i_1,…,i_{p−1} be non-negative integers such that
    w=i_1+⋯+i_{p−1}≤l−1. If Δ_{i}(1/ν!)∂^ν_{x_p}R is not identically zero, then ind(Δ_i(1/ν!)∂^νR;
    h/q; r) ≥ θ − i_1/r_1 − ⋯ − i_{p−1}/r_{p−1} − ν/r_p ≥ θ − w/r_{p−1} − ν/r_p. We have w/r_{p−1} ≤
    (l−1)/r_{p−1} ≤ r_p/r_{p−1} < δ. Since the index is never negative, the index is at least max(0,
    θ−ν/r_p−δ) ≥ max(0,θ−ν/r_p) − δ." ... > "F = ∑_{σ∈S_l} sign(σ) ∏_{ν=0}^{l−1} Δ_{σ(ν+1)−1}
    (1/ν!)∂^ν R. ... Zero entries and zero permutation products have index +∞ and cannot worsen the
    lower bound. Multiplication by a sign does not change the index. By Lemma 4-1, ind(F) ≥
    min_σ ind ∏_ν … ≥ min_σ ∑_ν ind Δ_{σ(ν+1)−1}(1/ν!)∂^νR ≥ min_σ ∑_ν max(0,θ−ν/r_p) − lδ."
  - Match: the hypothesis `hδ : ∀ d, d.degree ≤ l − 1 → weight (r ∘ some) d ≤ δ` is the displayed
    "w/r_{p−1} < δ" (it is derived from the chain hypotheses in R9.7 via R1.7); the rest is
    literally the source's chain of inequalities, with `index_neg` for the sign, R7.8 for the
    sum over permutations, R7.10 for the products, R7.7 for the entries.
  - Discharged by: `Matrix.det_apply'`, R7.8 (`le_index_sum`, the determinant is nonzero by
    hypothesis), `Int.units_eq_one_or` + R7.11 (`index_neg`) for `sign σ`, R7.10 (`index_prod`, all
    factors nonzero since the product is), R7.7 (`index_hasseDeriv_ge`) + R1.3 (`weight_add`,
    `weight_single`) + R1.8 (`weight_mapDomain`) + `hδ` for each entry, R7.5 (`index_nonneg`) for
    `max 0 _`, `Finset.sum_le_sum`, `Finset.sum_sub_distrib`, `Finset.sum_const`, `le_max_iff`
    arithmetic. Source: 25 lines; ~70 LOC.
  - Attacks: [2] `l = 0`: `0 − 0 ≤ index 1 = 0` ✓. [4] the Lean entries are
    `hasseDeriv (mapDomain some (D μ) + single none ν)`, the source's `Δ_μ (1/ν!)∂^ν_p` (R0.11 with
    disjoint supports) ✓; the row/column convention: the source expands with `Δ_{σ(ν+1)−1}` in
    column `ν`, i.e. the permutation acts on rows — `Matrix.det_apply'` gives `∏ i, M (σ i) i` ✓
    same shape. SURVIVED.
- **R9.6** `[internal]` `Roth.index_det_le` — eq. (17): `index F ≤ l · Φ`.
  - Source `clean.tex:729-776`. Quotes: > "By Lemma 3 the coefficients of F have absolute value not
    exceeding ((r_1+1)⋯(r_p+1))^l l! B^l 2^{(r_1+⋯+r_p)l} < (r_1+1)^{pl} l! B^l 2^{pr_1l} = M, as
    r_1>r_2>⋯>r_p. Since F=U(x_1,…,x_{p−1})V(x_p) and U,V are nonzero integral polynomials in
    disjoint variables, each coefficient of F is a unique product of one coefficient from each
    factor. Thus abc(F)=abc(U)abc(V), while abc(U),abc(V)≥1, and hence abc(U)<M, abc(V)<M. By Lemma
    2, U∈ℛ_{p−1}(M;lr_1,…,lr_{p−1}). Hence ind(U;h/q;lr) ≤ Θ_{p−1}(M;q;lr). Consequently, by scaling
    the weights, ind(U;h/q;r) ≤ lΘ_{p−1}(M;q;lr). Similarly, V(x_p)∈ℛ_1(M;lr_p), and ind(V;h_p/q_p;
    r_p) ≤ lΘ_1(M;q_p;lr_p). By Lemma 4-2, ind(F;a;r) = ind(U;…;r_1,…,r_{p−1}) + ind(V;a_p;r_p) ≤
    lΘ_{p−1} + lΘ_1 = lΦ." Lean note `clean.tex:778-784` (keep degree bounds `lr_j` and apply the
    scaling identity to `U` first).
  - Composition: R3.9 (Lemma 3) + numerics `∏(r_j+1) ≤ (r₁+1)^p`, `∑ r_j ≤ p r₁` (`Finset.prod_le_pow_card`,
    `Finset.sum_le_card_nsmul`, `Fintype.card_option`) give `|coeff F| ≤ M`; R6.3 (coefficients of
    `UV` are products) with `|v_b| ≥ 1` for a nonzero integer coefficient (`Int.one_le_abs`) gives
    `|u_a| ≤ M` and symmetrically `|v_b| ≤ M`, so `U ∈ RSet M (l • r ∘ some)` and
    `(uniqueAlgEquiv ℤ Unit).symm V ∈ RSet M (fun _ => l r_none)` (`coeff_uniqueAlgEquiv_symm`,
    `degreeOf_uniqueAlgEquiv_symm`); R8.1 (`index_le_Θ`, needs `1 ≤ M`: `one_le_lem6M`-type numerics
    from `1 ≤ B`), R7.12 (`index_mul_left_weights`, `index U (r∘some) = l · index U (l • r∘some)`),
    R7.9 + R7.13 + `aeval_X_eq_rename` for `index F = index U (…) + index V (…)` (Lemma 4-2), `map`
    compatibility (`MvPolynomial.map_mul`, `map_rename`, `Polynomial.map_aeval`-type lemma), then
    `mul_add`. ~90 LOC.
  - Composition attacks: (i) The source's strict `< M` becomes `≤ M` in Lean (`RSet` uses `≤`) ✓
    harmless. (ii) The source claims `abc(F) = abc(U)abc(V)`; only `abc(U) ≤ abc(F)` is needed and
    that is what R6.3 + `|v_b| ≥ 1` gives ✓. (iii) `l ≤ r_none + 1` and `r_none ≤ r₁` ensure the
    numerics of `M` only use `r_j ≤ r₁` — the source's "as r_1 > ⋯ > r_p" is only used for `∏ ≤
    (r_1+1)^p`, `∑ ≤ p r_1` ✓ so the weaker hypothesis `∀ j, r j ≤ r₁` suffices. SURVIVED.
- **R9.7** `[internal]` `Roth.index_le_lem6` — Lemma 6 for one `(R, h)`: `∃ l ∈ [1, r_none+1]`,
  `index R (h/q) r ≤ 2(Φ_l + √Φ_l + √δ)`.
  - Source `clean.tex:847-854` and `clean.tex:921-933`. Quotes: > "We can suppose θr_p>10, for if
    not, then we have θ ≤ 10r_p^{−1} < δ < 2δ^{1/2}, and this shows the inequality in the statement
    of the lemma is valid." > "Combining this inequality with (17) gives min(½lθ, ⅓r_pθ²) ≤ l(Φ+δ).
    Hence either ½lθ ≤ l(Φ+δ) or ⅓r_pθ² ≤ l(Φ+δ). In the first case, θ ≤ 2(Φ+δ) which implies the
    inequality asserted in the lemma. In the second case, ⅓r_pθ² ≤ l(Φ+δ) ≤ (r_p+1)(Φ+δ) <
    (4/3)r_p(Φ+δ), as r_p>10δ^{−1}. These inequalities imply θ < 2(Φ+δ)^{1/2} ≤ 2(Φ^{1/2}+δ^{1/2}).
    This completes the proof of the lemma."
  - Composition: R6.12 (Lemma 2) gives `l, D, U, V`; `F ≠ 0` (`U, V ≠ 0`, domain, `rename`/`aeval`
    injective: `MvPolynomial.rename_injective`, `aeval (X none)` injective by R6.5-type degree
    argument or `Polynomial.aeval_X_injective`); R9.6 (upper bound `lΦ`); R9.5 (lower bound) with
    `hδ` from R1.7: a multi-index `d : τ →₀ ℕ` of degree `≤ l−1 ≤ r_none` has `weight (r∘some) d ≤
    (l−1)/m` where `m := min_j r_{some j} > r_none/δ`, so `≤ r_none·δ/r_none = δ` (`hratio`,
    `div_le_div`); the `θ r_p ≤ 10` shortcut: `θ ≤ 10/r_p < δ < √δ ≤ 2(Φ+√Φ+√δ)` (`Real.lt_sqrt`,
    `Φ ≥ 0` from `Θ_nonneg` and `1 ≤ M`); otherwise R9.4 and the two cases with `nlinarith`/
    `Real.sqrt_lt_sqrt`, `Real.sqrt_le_sqrt`, `Real.sqrt_add_le`?/squaring (`Real.sqrt_le_left`,
    `Real.lt_sqrt`), `r_p + 1 < (4/3) r_p` from `r_p > 10/δ > 10 > 3`. ~110 LOC.
  - Composition attacks: (i) the case `θ ≤ 2(Φ+δ)`: needs `δ ≤ √δ` (`δ < 1`) ✓ hypothesis `hδ1`.
    (ii) The hypothesis `hratio : r_none < δ r_{some j}` for *all* `j` is what the source derives
    from the chain `r_{j−1}/r_j > 1/δ` ("w/r_{p−1} ≤ … < δ" uses `r_{p−1}` minimal among
    `r_1..r_{p−1}` and `r_p/r_{p−1} < δ`); the Lean hypothesis is exactly that derived fact ✓.
    (iii) For `τ` empty the hypotheses `hratio` are vacuous and `Φ` has `Θ` over the empty type
    (`Θ ≤ card = 0`), fine. SURVIVED.
- **R9.8** `[internal]` **Lemma 6** `Roth.Θ_option_le` — `Θ B q r ≤ 2 · sup'_{l ∈ Icc 1 (r_none+1)}
  (Φ_l + √Φ_l + √δ)`.
  - Lean: `Roth/Theta.lean:177`
  - Source `clean.tex:704-724` (statement): > "Let p≥2 be a positive integer, and let 0<δ<1. Let
    r_1,…,r_p be positive integers satisfying r_p>10δ^{−1}, r_{j−1}/r_j>δ^{−1}, for 2≤j≤p. Also, let
    q_1,…,q_p be positive integers. Then Θ_p(B;q_1,…,q_p;r_1,…,r_p) ≤ 2 max_l(Φ + Φ^{1/2} + δ^{1/2}),
    where the maximum is taken over integers l satisfying 1≤l≤r_p+1".
  - Match: `max_l` over `Icc 1 (r_none+1)` is `Finset.sup'` (nonempty); the hypotheses are the
    derived forms discussed in R9.7 (they follow from the source's chain, see R10.3). Composition:
    R8.1 (`Θ_le_of_forall_index_le`, `1 ≤ B`), R9.7, `Finset.le_sup'` at the chosen `l`,
    `mul_le_mul_left`. ~15 LOC. Composition attack: strictness is not claimed (`≤`), consistent with
    the source; the note `clean.tex:1042-1045` ("strict bounds on each member imply a strict bound on
    a finite maximum, but not on an arbitrary supremum") is honoured in Lemma 7 by using `Θ ≤ C`
    with a *strict* numerical inequality `C < 10^p a` (R10.4). SURVIVED.

---

## Result R10: Lemma 7 (§5 of [TY], `Roth/Theta.lean`, section `Lemma7`)

### Plain-English proof (source structure)

[TY] §5 Lemma 7, `clean.tex:935-1045`: induction on `m`. `m = 1`: Lemma 5 gives `Θ_1 ≤ δ < 10δ^{1/2}`.
Step `p ≥ 2`: apply Lemma 6; estimate `M ≤ ((r_1+1)^p l 2^{pr_1} q_1^{δr_1})^l < (2^{(2p+1)r_1}
q_1^{δr_1})^l < (e^{(2p+1)r_1} q_1^{δr_1})^l < q_1^{δ_1 l r_1}` with `δ_1 = δ(1+1/p)` using (21);
then `Θ_1(M;q_p;lr_p) ≤ δ_1` by Lemma 5 and (22); `Θ_{p−1}(M; …; lr) ≤ Θ_{p−1}(q_1^{δ_1 lr_1}; …)`
and the induction hypothesis applies (hypotheses verified for `p−1, δ_1, lr`), giving `< 10^{p−1}
δ_1^{(1/2)^{p−1}}`; so `Φ < 3·10^{p−1}δ^{(1/2)^{p−1}}`; finally with `a = δ^{2^{−p}}` the numerical
estimate `2(3·10^{p−1}a² + √3·10^{(p−1)/2}a + δ^{1/2}) < 10^p a`.

- **R10.1** `[gap]` `Roth.lem6M_lt` — `M < q_1^{δ(1+1/p)(l r_1)}` under `p ≥ 2`, `0 < δ`, `0 < r_1`,
  `p(2p+1)/δ < log q_1`, `1 ≤ l ≤ r_1`.
  - Source `clean.tex:950-964`. Quote: > "M = (r_1+1)^{pl} l! 2^{plr_1} q_1^{δlr_1} ≤ ((r_1+1)^p l
    2^{pr_1} q_1^{δr_1})^l. Next, l ≤ r_p+1 < r_1+1 ≤ 2^{r_1}. Consequently, M < (2^{(2p+1)r_1}
    q_1^{δr_1})^l < (e^{(2p+1)r_1}q_1^{δr_1})^l. From Equation (21) for m=p, we have 2p+1 < δp^{−1}
    log q_1, and this gives M < (e^{(δp^{−1}log q_1)r_1}q_1^{δr_1})^l = (q_1^{(δp^{−1})r_1}
    q_1^{δr_1})^l = q_1^{δ_1lr_1} with δ_1 = δ(1+p^{−1})."
  - Match: identical; the source's `l ≤ r_p + 1 < r_1 + 1` is the hypothesis `l ≤ r_1`.
  - Discharged by: `Nat.factorial_le_pow` (`l! ≤ l^l`), `Nat.lt_two_pow_self` (`r_1 + 1 ≤ 2^{r_1}`),
    `pow_le_pow_left`, `Real.rpow_natCast`, `Real.exp_one_gt_d9`/`Real.two_lt_exp`? (`2 < e`: from
    `Real.add_one_lt_exp` at `1`: `2 < exp 1`), `Real.exp_lt_exp`, `Real.rpow_def_of_pos`
    (`q^x = exp (x log q)`), `Real.exp_log`, `Real.rpow_add`, `Real.rpow_mul`, `mul_pow`, `pow_mul`.
    Source: 10 lines; ~70 LOC of real-analysis bookkeeping.
  - Attacks: [2] `l = 1`, `p = 2`, `r_1 = 1`: `M = 4·1·B·16 = 64 B` vs `q_1^{1.5δ}` with `B = q_1^δ`:
    need `64 < q_1^{δ/2}` ⇐ `log q_1 > 10/δ > 8.4/δ` ✓ (`(2p+1)r_1 = 5`, `e^5 ≈ 148 > 64`, and
    `e^5 < q_1^{δ/2}` ⇐ `5 < δ log q_1/2` ⇐ `log q_1 > 10/δ` ✓ consistent). [3] the strict
    hypothesis `p(2p+1)/δ < log q_1` is (21) for `m = p` ✓. SURVIVED.
- **R10.2** `[gap]` `Roth.lem7_Φ_bound` — `δ_1 + 10^{p−1}δ_1^{(1/2)^{p−1}} < 3·10^{p−1}δ^{(1/2)^{p−1}}`
  for `δ_1 = δ(1+1/p)`, `p ≥ 2`, `0 < δ < 1`.
  Source `clean.tex:1008-1020`: > "Φ < δ_1 + 10^{p−1}δ_1^{(1/2)^{p−1}} = δ(1+p^{−1}) + 10^{p−1}
  δ^{(1/2)^{p−1}}(1+p^{−1})^{(1/2)^{p−1}} < 2δ + 2·10^{p−1}δ^{(1/2)^{p−1}} < 3·10^{p−1}
  δ^{(1/2)^{p−1}}. Here we have used the fact that δ_1<2δ and (1+p^{−1})^{(1/2)^{p−1}}<2, which are
  both easily verified. Also 0<δ<1, so δ ≤ δ^{2^{−(p−1)}}, justifying the last absorption above."
  Discharged by: `Real.mul_rpow`, `Real.rpow_le_rpow_of_exponent_ge` (`δ ≤ δ^e` for `δ < 1`, `e ≤ 1`:
  `Real.rpow_le_self_of_le_one`?/`Real.rpow_le_rpow_of_exponent_ge'`), `Real.rpow_le_one` /
  `(1+1/p)^e ≤ 1+1/p ≤ 3/2 < 2` (`Real.rpow_le_rpow_of_exponent_le` with base `≥ 1` and `e ≤ 1`),
  `Real.rpow_pos_of_pos`, `nlinarith` with `2 ≤ 10^{p−1}` (`Nat.one_le_two_pow`-style, `pow_le_pow_right`).
  ~45 LOC. Attacks: [2] `p = 2`, `δ = 1/2`: LHS `0.75 + 10·(0.75)^{1/2} ≈ 9.41`, RHS `30·(0.5)^{1/2} ≈
  21.2` ✓. SURVIVED.
- **R10.3** `[gap]` `Roth.lem7_numeric` — `0 ≤ Φ < 3·10^{p−1}δ^{(1/2)^{p−1}}` ⇒ `2(Φ+√Φ+√δ) < 10^pδ^{(1/2)^p}`.
  Source `clean.tex:1025-1041`: > "Set a=δ^{2^{−p}}. Then δ^{2^{−(p−1)}}=a²≤a and δ^{1/2}≤a.
  Consequently, Θ_p < 2(3·10^{p−1}a² + √3·10^{(p−1)/2}a + δ^{1/2}) ≤ 2(3/10 + √3/10^{(p+1)/2} +
  1/10^p)10^pa ≤ 2(3/10 + √3/10^{3/2} + 1/10²)10^pa < 10^pa. Here p≥2 and the numerical
  coefficient in the last line is less than 1 (for example, √3/10^{3/2}<1/10)." Lean note
  `clean.tex:1042-1045` ("define a_0=δ and a_{j+1}=√a_j and prove once that a_j=δ^{2^{−j}}").
  Discharged by: `a := δ^{(1/2)^p}` with `a^2 = δ^{(1/2)^{p−1}}` (`Real.rpow_natCast_mul`/
  `Real.rpow_mul`, `pow_succ`), `a ≤ 1`, `a² ≤ a` (`Real.rpow_le_one`, `mul_le_of_le_one_left`),
  `√δ ≤ a` (`Real.sqrt_eq_rpow`, `Real.rpow_le_rpow_of_exponent_ge`), `√Φ < √(3·10^{p−1}) a`
  (`Real.sqrt_lt_sqrt`, `Real.sqrt_mul_self`), `√(3·10^{p−1}) ≤ 10^{(p−1)/2}·√3` and the constant
  inequality `6·10^{p−1} + 2√3·10^{(p−1)/2} + 2 < 10^p` for `p ≥ 2` (`Real.sqrt_lt'`, `nlinarith`
  with `10^{(p−1)/2} ≤ 10^{p−1}`... or directly `2√3·10^{(p−1)/2} + 2 ≤ 2√3·10^{p−1} + 2 < 4·10^{p−1}`
  since `2√3 < 3.5` and `10^{p−1} ≥ 10`). ~70 LOC. Attacks: [2] `p = 2`, `δ = 0.01`: `a = 0.01^{1/4}
  ≈ 0.316`, bound `Φ < 30·0.1 = 3`, LHS `≤ 2(3 + 1.73 + 0.1) = 9.66`, RHS `100·0.316 = 31.6` ✓; the
  constant check: `6·10 + 2·1.732·3.162 + 2 = 72.95 < 100` ✓. SURVIVED.
- **R10.4** `[internal]` **Lemma 7** `Roth.Θ_lt` — for `Fin (n+1)` variables, `0 < δ < 1/(n+1)`,
  chain conditions, `(n+1)(2(n+1)+1)/δ < log q_0`, `r_0 log q_0 ≤ r_j log q_j`:
  `Θ (q_0^{δ r_0}) q r < 10^{n+1} δ^{(1/2)^{n+1}}`.
  - Lean: `Roth/Theta.lean:207`
  - Source `clean.tex:935-962` (statement): > "Let m be a positive integer and let δ satisfy 0<δ<
    m^{−1}. Let r_1,…,r_m be positive integers satisfying r_m>10δ^{−1}, r_{j−1}/r_j>δ^{−1}, 2≤j≤m.
    Let q_1,…,q_m be positive integers satisfying log q_1 > δ^{−1}m(2m+1), r_j log q_j ≥ r_1 log q_1,
    for 2≤j≤m. Then Θ_m(q_1^{δr_1};q_1,…,q_m;r_1,…,r_m) < 10^mδ^{(1/2)^m}." Base case `clean.tex:965-
    969`: > "If m=1, Lemma 5 says Θ_1(q_1^{δr_1};q_1;r_1) ≤ δr_1 log q_1/(r_1 log q_1) = δ <
    10δ^{1/2}". Step `clean.tex:971-1007` quoted in R10.1–R10.3 and: > "We verify the induction
    hypotheses for dimension p−1, parameter δ_1=δ(1+1/p), and degrees lr_1,…,lr_{p−1}. First,
    0<(p−1)δ_1<(p−1)(p+1)/p²<1. Since δ_1>δ and l≥1, the degree-ratio and final-degree bounds follow
    from (20). Moreover, log q_1>δ^{−1}p(2p+1)>δ_1^{−1}(p−1)(2p−1). The balanced-logarithm
    inequalities are unchanged when every degree is multiplied by l. Hence all four hypotheses
    hold."
  - Match: `m = n+1`, variables `0..n` ↔ `x_1..x_m` (same order), `Fin.last n = x_m`; the chain is
    `r (i.succ)/δ < r (i.castSucc)`; `q 0 = q_1`, `r 0 = r_1`. `Conditions (21)–(22) imply q_j > 1`
    is derived inside.
  - Composition: induction on `n`. **Base** `n = 0`: `Fin 1` is `Unique`; R8.5 with `B = q_0^{δ r_0} ≥
    1` (`Real.one_le_rpow`), `q 0 > 1` (from `log q_0 > 3/δ > 0`: `Real.log_pos_iff`), giving
    `Θ ≤ log(q_0^{δr_0})/(r_0 log q_0) = δ` (`Real.log_rpow`, `mul_div_assoc`, `div_self`), and
    `δ < 10√δ` (`δ < 1`: `Real.lt_sqrt`, `δ² < δ`). **Step** `n+1` (so `p = n+2 ≥ 2`): transport
    `Θ` over `Fin (n+2)` to `Option (Fin (n+1))` with R8.2 and `finSuccEquivLast` (`Fin.last ↦ none`,
    `castSucc i ↦ some i`; mathlib `finSuccEquivLast_castSucc`, `finSuccEquivLast_last`); apply R9.8
    (Lemma 6) with `r₁ := r 0`, `B := q_0^{δ r_0}` (hypotheses: `r_last > 10/δ`; `r_last < δ r_j` for
    all `j` from the chain by induction on the index — the chain gives `r_{i} > r_{i+1}/δ > r_{i+1}`
    so `r` is antitone, hence `r_j ≥ r_{n} > r_{last}/δ`; `r_j ≤ r_0` by antitonicity); for each
    `l ∈ Icc 1 (r_last+1)`: `l ≤ r_0` (`r_last + 1 ≤ r_n ≤ r_0` from the chain and `δ < 1`), R10.1
    gives `M < q_0^{δ_1 (l r_0)}`; `Θ_1(M; q_last; l r_last) ≤ Θ_1(q_0^{δ_1 l r_0}; …) ≤ δ_1` by R8.1
    (`Θ_mono`), R8.5 and `r_last log q_last ≥ r_0 log q_0` (`div_le_iff`, `Real.log_rpow`);
    `Θ_{Fin(n+1)}(M; q∘castSucc; l·r∘castSucc) ≤ Θ(q_0^{δ_1 (l r_0)}; …)` (`Θ_mono`) `< 10^{n+1}
    δ_1^{(1/2)^{n+1}}` by the induction hypothesis with `δ_1 := δ(1+1/(n+2))`, degrees `l • r ∘
    castSucc`, same `q ∘ castSucc` — hypotheses: `δ_1 < 1/(n+1)` (the source's `(p−1)δ_1 < 1`),
    `10/δ_1 < l r_n` (`δ_1 > δ`, `l ≥ 1`, `r_n > r_last/δ > 10/δ`), chain for `l • r` (`l` cancels,
    `δ_1 > δ`), `(n+1)(2(n+1)+1)/δ_1 < log q_0` (the source's `log q_1 > δ^{−1}p(2p+1) > δ_1^{−1}
    (p−1)(2p−1)`: `(p−1)(2p−1)·p/(p+1) < p(2p+1)`, `nlinarith`), `l r_0 log q_0 ≤ l r_j log q_j`;
    hence `Φ_l < 3·10^{n+1}δ^{(1/2)^{n+1}}` by R10.2 (`Φ_l ≥ 0` by `Θ_nonneg`, `1 ≤ M`); so for
    every `l`, `2(Φ_l+√Φ_l+√δ) < 10^{n+2}δ^{(1/2)^{n+2}}` by R10.3, hence the `sup'` is `<` (`Finset.sup'_lt_iff`),
    and `Θ ≤ 2·sup' < …`. Source: 75 lines; ~160 LOC.
  - Composition attacks: (i) **Does the `B` of the induction hypothesis match?** The IH is stated
    with `B = (q 0)^(δ_1 · (r' 0))` where `r' 0 = l * r 0`; we need `M < q_0^{δ_1 (l r_0)}` — R10.1
    gives exactly this (with the cast `((l * r 0 : ℕ) : ℝ) = l * r 0`) ✓. (ii) **Monotonicity in
    `B` needs `1 ≤ M`**: `M ≥ 1` since every factor is `≥ 1` (`B = q_0^{δ r_0} ≥ 1`) ✓. (iii) The
    source's induction is on `m` with Lemma 6 splitting off `x_p`; in Lean the split variable is
    `Fin.last` via `finSuccEquivLast` and the remaining variables `castSucc i` keep their order, so
    `q ∘ castSucc` has `(q ∘ castSucc) 0 = q 0` ✓ and the chain hypotheses restrict verbatim ✓.
    (iv) `q_j > 1` for all `j` is needed for `Θ_unique_le` (`q_last > 1`): from `r_j log q_j ≥ r_0
    log q_0 > 0` ✓ (the source's remark "Conditions (21)–(22) imply q_j>1"). (v) Strictness: the
    `Θ ≤` from Lemma 6 is combined with the strict numerical bound on the finite `sup'` ✓ (the
    source's Lean note). SURVIVED.

---

## Result R11: Lemma 8, the lattice count (§6 of [TY], `Roth/Lattice.lean`)

### Plain-English proof (source structure)

[TY] §6 Lemma 8, `clean.tex:1050-1138`: the number of `(j_1..j_m)` with `0 ≤ j_i ≤ r_i` and
`∑ j_i/r_i ≤ (m−λ)/2` is at most `2√m λ^{−1}∏(r_i+1)`. Induction on `m`: `m = 1` by cases `λ > 1`
(no solutions) / `λ ≤ 1` (at most `r_1+1 < 2λ^{−1}(r_1+1)`); for `m > 1`, if `λ ≤ 2√m` the bound
exceeds the size of the whole box; otherwise fix `j_m`, apply the induction hypothesis with `λ' =
λ − 1 + 2j_m/r_m > 0`, sum over `j_m`, and use the estimate `∑_{j=0}^r (λ−1+2j/r)^{−1} < λ^{−1}
(m−1)^{−1/2}m^{1/2}(r+1)` for `λ > 2√m`, proved by pairing `j ↔ r−j` (even/odd `r`) and
`1−λ^{−2} > 1−1/(4m) > √(1−1/m)`.

- **R11.1** `[gap]` `Roth.sqrt_one_sub_inv_lt` — `2 ≤ m`, `2√m < λ` ⇒ `√(1−1/m) < 1−λ^{−2}`.
  Source `clean.tex:1114-1118`: > "Now 1−λ^{−2} > 1−1/(4m) > √(1−1/m) > 0. For the middle
  inequality, square the positive quantities and use (1−1/(4m))² − (1−1/m) = 1/(2m) + 1/(16m²) > 0."
  Discharged by: `Real.sqrt_lt'` (`√x < y ↔ x < y²` for `y > 0`), `inv_lt_inv_of_lt`/`one_div_lt`
  with `λ² > 4m`, `nlinarith`/`field_simp`. ~20 LOC. Attacks: [2] `m = 2`, `λ = 3`: `√0.5 ≈ 0.707 <
  1 − 1/9 ≈ 0.889` ✓. SURVIVED.
- **R11.2** `[gap]` `Roth.sum_inv_lt` — `1 ≤ r`, `2 ≤ m`, `2√m < λ` ⇒
  `∑_{j ≤ r} (λ−1+2j/r)^{−1} < λ^{−1}(√(m−1))^{−1}√m(r+1)`.
  - Source `clean.tex:1100-1133`. Quote: > "Let r≥1 and m≥2 be integers and suppose λ>2√m. Then
    ∑_{j=0}^r(λ−1+2j/r)^{−1} < λ^{−1}(m−1)^{−1/2}m^{1/2}(r+1). There are two cases. If r is even,
    we replace j by ½r+k to obtain the sum ∑_{k=−r/2}^{r/2}(λ+2k/r)^{−1} = λ^{−1} + ∑_{k=1}^{r/2}
    2λ(λ²−4k²/r²)^{−1} ≤ λ^{−1} + ∑_{k=1}^{r/2}2λ(λ²−1)^{−1} ≤ (r+1)λ^{−1}(1−λ^{−2})^{−1}. ... Taking
    reciprocals gives the result for even r. If r is odd, we obtain ∑_{k=0}^{(r−1)/2}(1/(λ−(1+2k)/r)
    + 1/(λ+(1+2k)/r)) = ∑ 2λ/(λ²−((1+2k)/r)²) ≤ ∑ 2λ/(λ²−1) = (r+1)/2 · 2λ/(λ²−1) = λ^{−1}(r+1)/
    (1−λ^{−2}). The rest of the argument is as before." Lean note `clean.tex:1137-1138`: > "Prove
    the reciprocal-sum estimate separately by pairing j with r−j".
  - Match: identical; the pairing `j ↔ r−j` gives `(λ−1+2j/r)^{−1} + (λ−1+2(r−j)/r)^{−1} =
    2λ/(λ² − (1−2j/r)²) ≤ 2λ/(λ²−1)` for every `j` (both parities at once: summing the paired
    identity over all `j` counts each term twice, `2∑ = ∑_j (pair) ≤ (r+1)·2λ/(λ²−1)`), so `∑ ≤
    (r+1)λ^{−1}/(1−λ^{−2}) < (r+1)λ^{−1}/√(1−1/m)` by R11.1.
  - Discharged by: `Finset.sum_range_reflect` (reindex `j ↦ r−j`), `two_mul`, `add_div`,
    `div_add_div`, `div_le_div_iff` (denominators positive: `λ−1+2j/r ≥ λ−1 > 2√2−1 > 0`,
    `λ² − (1−2j/r)² ≥ λ² − 1 > 0` since `|1−2j/r| ≤ 1`), `Finset.sum_le_card_nsmul`,
    `Finset.card_range`, R11.1, `Real.sqrt_lt'`/`one_div_lt_one_div_of_lt`, `Real.sqrt_pos`,
    `Real.sqrt_div`/`Real.sqrt_mul_self`, `Nat.cast_sub`. ~80 LOC.
  - Attacks: [2] `r = 1`, `m = 2`, `λ = 3`: LHS `1/2 + 1/4 = 0.75`; RHS `(1/3)(1/1)(1.414)(2) ≈
    0.943` ✓. `r = 2`, `m = 2`, `λ = 3`: LHS `1/2 + 1/3 + 1/4 = 1.083`, RHS `≈ 1.414` ✓. [3] `2√m < λ`
    is needed (for `λ ≤ 1` the first term `(λ−1)^{−1}` blows up). SURVIVED.
- **R11.3** `[gap]` `Roth.card_filter_box_last` — fibres of the last coordinate:
  `((box r).filter p).card = ∑_{i ≤ r_last} ((box (r∘castSucc)).filter (fun d => p (d.mapDomain castSucc + single last i))).card`.
  Source Lean note `clean.tex:1134-1136`: > "Its cardinality is the product ∏_j(r_j+1), and
  induction counts the fibres of the last-coordinate projection." and `clean.tex:1070-1076` ("For a
  fixed value of j_m, the induction hypothesis is applied to j_1,…,j_{m−1}"). Discharged by:
  `Finset.card_eq_sum_card_fiberwise` with the projection `d ↦ d (Fin.last m)` into `range (r_last+1)`,
  then a bijection between each fibre and the filtered `box (r ∘ castSucc)` via `d ↦ Finsupp.comapDomain
  castSucc d` / `d' ↦ d'.mapDomain castSucc + single last i` (`Finset.card_bij`/`Finset.card_nbij'`,
  `Fin.lastCases`, `Finsupp.mapDomain_apply (Fin.castSucc_injective _)`, `Finsupp.mapDomain_notin_range`,
  `Fin.exists_castSucc_eq`, R1.1). ~60 LOC. Attacks: [2] `m = 0` (`Fin 1`): box `(r∘castSucc)` over
  `Fin 0` is `{0}`, the formula reduces to counting `i ≤ r_0` with `p (single 0 i)` ✓. SURVIVED.
- **R11.4** `[internal]` **Lemma 8** `Roth.card_filter_weight_le`.
  - Lean: `Roth/Lattice.lean:39`
  - Source `clean.tex:1050-1060` (statement): > "If m≥1, r_1,…,r_m are positive integers and λ>0,
    then the number of m-tuples of integers (j_1,…,j_m) that satisfy 0≤j_1≤r_1,…,0≤j_m≤r_m,
    j_1/r_1+⋯+j_m/r_m ≤ (m−λ)/2 does not exceed 2m^{1/2}λ^{−1}(r_1+1)⋯(r_m+1)." Proof `clean.tex:
    1062-1098` quoted in the plain-English proof above, in particular > "If m=1 ... If λ>1 then we
    have no such j_1. If 0<λ≤1, then the number of j_1 from the first inequality is at most r_1+1,
    and this number is less than 2λ^{−1}(r_1+1)" and > "If λ≤2m^{1/2} then the result is trivial
    ... So we assume λ>2m^{1/2}. ... λ' = λ−1+2j_m/r_m. We note that λ'>0 ... By the induction
    hypothesis, the number of (m−1)-tuples is at most 2(m−1)^{1/2}(λ')^{−1}(r_1+1)⋯(r_{m−1}+1).
    Summing these bounds over 0≤j_m≤r_m, it is enough to show 2√(m−1)∏_{i<m}(r_i+1)∑_{j_m}
    1/(λ−1+2j_m/r_m) ≤ (2√m/λ)∏_{i≤m}(r_i+1)."
  - Match: identical (the Lean statement also allows `m = 0`, where the count is `0 ≤ 0`).
  - Composition: induction on `m`. `m = 0`: the filter is empty (`0 ≤ −λ/2` is false) ✓ RHS `0`.
    `m = 1`: cases on `λ ≤ 1` (`Finset.card_filter_le` + R1.1: `card ≤ r_0+1 ≤ 2/λ·(r_0+1)`) or
    `1 < λ` (filter empty since `j/r ≥ 0 > (1−λ)/2`). Step `m+1 ≥ 2`: if `λ ≤ 2√(m+1)`: `card ≤
    card (box) = ∏(r_i+1) ≤ 2√(m+1)/λ · ∏` ✓; else R11.3 splits by the last coordinate `i`; each
    fibre is the count for `Fin m`, weights `r ∘ castSucc`, threshold `(m+1−λ)/2 − i/r_last =
    (m − λ')/2` with `λ' = λ − 1 + 2i/r_last > 2√(m+1) − 1 > 0` (R1.3 `weight_add`, `weight_single`,
    R1.8 `weight_mapDomain`), bounded by the IH; sum over `i`: `Finset.sum_le_sum`, `Finset.mul_sum`,
    R11.2 with `r := r_last`, `m := m+1` (`2 ≤ m+1` needs `m ≥ 1`: the case `m = 0` of the step is
    the `m = 1` base above — organise the induction as `Nat.le_induction` from `1`, or do `m = 1`
    separately), and `2√m · √(m+1)/(√m · λ) = 2√(m+1)/λ` (`Real.sqrt_div`, `mul_div_assoc`).
    Source: 45 lines; ~120 LOC.
  - Composition attacks: (i) In the step, R11.2 needs `2 ≤ m+1`, i.e. the step is for `m+1 ≥ 2`
    ✓ (and its `(m+1)−1 = m` matches `√(m−1)` in the source with `m ↦ m+1`). (ii) `λ' > 0`: `λ >
    2√(m+1) ≥ 2√2 > 1` ✓. (iii) The IH must be applied with *arbitrary* positive `λ'` ✓ (the
    statement quantifies over `λ`). (iv) Casting: `(m : ℝ)` vs `(m+1 : ℝ)` handled by `push_cast`.
    SURVIVED.

---

## Result R12: Lemma 9 and its preparation (§6 of [TY], `Roth/MainLemma.lean`)

### Plain-English proof (source structure)

[TY] §6, `clean.tex:1192-1562`. Setup: `α` an irrational real algebraic integer, `f = x^n + a_1x^{n−1}
+ ⋯ + a_n` monic integral with `f(α) = 0`, `n ≥ 2`, `A = max(1,|a_1|,…,|a_n|)`. Lemma `m-δ`: for `m >
16n²` there is `δ` with `0 < δ < 1/m` and `10^mδ^{(1/2)^m} + 2(1+3δ)n√m < m/2`; the fixed-`m` form
with an explicit threshold. Parameters: `r_j` with (31), `q_1 > 1` with (32) `δ² log q_1 > 2m+1 + 2m
log(1+A) + 2m log(1+|α|)`, `q_j` with (33); Lemma `lem7-satisfied`; `λ, γ, η, B_1` by (34)–(37); (30)
⟺ `η < γ`; `B_1` large: `log B_1 > ½δr_1 log q_1`, hence the three bounds `2^{mr_1}, (1+A)^{mr_1},
(1+|α|)^{mr_1} < B_1^δ`. **Lemma 9**: there is `Q ≠ 0` integral of degree `≤ r_j` with (1) index at
`(α,…,α)` ≥ `γ−η > 0`, (2) `Q(h/q) ≠ 0`, (3) `|Δ_iQ(α,…,α)| < B_1^{1+3δ}`. Proof: the family `𝒲` of
`(B_1+1)^r` polynomials with coefficients in `[0,B_1]`; for the `D ≤ 2√mλ^{−1}r` derivatives
`Δ_jW` with `j` in the box and weight `≤ γ` (Lemma 8), the remainders `T_j(W;x)` of `Δ_jW(x,…,x)`
modulo `f` have coefficients `< B_1^{1+3δ}` (derivative bound `2^{mr_1}B_1 < B_1^{1+δ}`, diagonal
bound `r B_1^{1+δ} < B_1^{1+2δ}`, division bound `(1+A)^{mr_1}B_1^{1+2δ} < B_1^{1+3δ}`); the number of
remainder tuples `(1+2B_1^{1+3δ})^{nD} < (1+B_1)^r` (using `(1+3δ)nD ≤ r/2`), so two distinct
`W', W''` have equal remainder tuples; `W^* = W'−W''` is nonzero, has coefficients `≤ B_1`, degrees
`≤ r_j`, and `Δ_jW^*(α,…,α) = 0` for all `j` with weight `≤ γ`, so its index at `(α,…,α)` is `≥ γ`;
`W^* ∈ ℛ_m(q_1^{δr_1}; r)` so Lemma 7 gives index at `(h/q)` `< η`; some `Q = Δ_kW^*` with weight
`k < η` has `Q(h/q) ≠ 0`; its index at `α` is `≥ γ−η` (index-of-derivative); its coefficients are
`< B_1^{1+δ}`, those of its derivatives `< B_1^{1+2δ}`, and evaluation at `(α,…,α)` gives `< B_1^{1+2δ}
(1+|α|)^{mr_1} < B_1^{1+3δ}`.

- **R12.1** `[gap]` `Roth.lam`, `gam`, `eta`, `B₁` (defs). Source `clean.tex:1337-1355`: > "λ = 4(1+3δ)
  nm^{1/2}, γ = ½(m−λ), η = 10^mδ^{(1/2)^m}, B_1 = [q_1^{δr_1}]." Match: identical (`B₁ = ⌊·⌋₊`, a
  natural number since `q_1^{δr_1} > 0`). SURVIVED.
- **R12.2** `[gap]` `Roth.exists_delta_bound` — `0 < n`, `16n² < m` ⇒ `∃ δ₀ > 0, ∀ δ ∈ (0, δ₀), δ < 1/m
  ∧ η + 2(1+3δ)n√m < m/2`.
  - Source `clean.tex:1211-1263` and Lean note `clean.tex:1303-1309`. Quotes: > "For every integer
    m>16n² there is a real δ>0 such that 0<δ<m^{−1} and 10^mδ^{(1/2)^m} + 2(1+3δ)nm^{1/2} < ½m." ...
    > "More generally, for any fixed integer m>16n², put E=m/2−2n√m>0 and choose δ = ½min{1/m,
    E/(12n√m), (E/(2·10^m))^{2^m}}. All entries are positive. This gives 10^mδ^{2^{−m}} < E/2 and
    6δn√m < E/2, proving the claim for the fixed m. Every smaller positive δ also works, since the
    left-hand side of (30) is strictly increasing in δ." Lean note: > "For each fixed m>16n², prove
    the stronger statement that some δ_0>0 makes (29) and (30) hold for every 0<δ<δ_0."
  - Match: the note's statement with `δ₀ := min{1/m, E/(12n√m), (E/(2·10^m))^{2^m}}` (every `δ <
    δ₀` works; the source's `½ min` is one such `δ`). The hypothesis `0 < n` was added (attack [2]:
    for `n = 0` the explicit threshold contains `E/(12·0·√m) = 0` in Lean's division convention,
    making `δ₀ = 0`; `n ≥ 2` in every application).
  - Discharged by: `E > 0` from `16n² < m` (`√m > 4n`: `Real.lt_sqrt`, `nlinarith`), `lt_min_iff`,
    `Real.rpow_lt_rpow` (`δ < (E/(2·10^m))^{2^m}` ⇒ `δ^{(1/2)^m} < E/(2·10^m)` via
    `Real.rpow_natCast`, `Real.rpow_mul`, `(2^m)·(1/2)^m = 1`), `Real.rpow_pos_of_pos`, `linarith`.
    Source: 12 lines; ~60 LOC.
  - Attacks: [2] `n = 1`, `m = 17`: `E = 8.5 − 8.246 = 0.254 > 0` ✓ thresholds positive ✓. [3]
    `16n² < m` is exactly the condition for `E > 0` ("the desired δ can exist precisely when
    2n√m < m/2"). SURVIVED.
- **R12.3** `[mathlib]` `Roth.eta_lt_gam_iff`. Source `clean.tex:1357-1360`: > "Inequality (30) is
  equivalent to η < γ." Discharged by: unfold `gam`, `lam`; `linarith`/`constructor <;> intro <;>
  linarith`. ~5 LOC. SURVIVED.
- **R12.4** `[gap]` `Roth.sqrt_lt_floor` — `4 < X` ⇒ `√X < ⌊X⌋₊ ∧ ⌊X⌋₊ ≤ X`.
  Source `clean.tex:1368-1373`: > "In particular, writing X=q_1^{δr_1}, we have X>4, whence B_1=⌊X⌋
  > X−1 > √X." and Lean note `clean.tex:1381-1388` ("isolate the floor estimate √X < ⌊X⌋ ≤ X for
  X>4 ... Retain the non-strict upper bound B_1 ≤ X: equality is possible when X is an integer").
  Discharged by: `Nat.sub_one_lt_floor`/`Nat.lt_floor_add_one`, `Nat.floor_le`, `Real.sqrt_lt'`/
  `Real.lt_sqrt`, `Real.sqrt_lt_sqrt`, `Real.sqrt_four`-style (`√X > 2` ⇒ `√X(√X−1) > 2 > 1` ⇒
  `X − 1 > √X`): `nlinarith [Real.sq_sqrt, Real.sqrt_nonneg]`. ~15 LOC. Attacks: [2] `X = 4.01`:
  `⌊X⌋ = 4 > 2.002` ✓; `X = 4` excluded (strict); `X = 9`: `⌊9⌋ = 9 > 3`, `9 ≤ 9` ✓ (equality case of
  the note). SURVIVED.
- **R12.5** `[gap]` `Roth.four_lt_rpow` — `0 < δ`, `1 ≤ m`, `δ < 1/m`, `0 < r₁`, `2m+1 < δ² log q₁` ⇒
  `4 < q₁^{δ r₁}`. Source `clean.tex:1362-1367`: > "B_1 is a large integer, because B_1 > q_1^{δr_1}
  −1 = (e^{δ log q_1})^{r_1} − 1 > (e^{m(2m+1)})^{r_1} − 1 > … > e^{82560} − 1." Match: only `X > 4`
  is used; `δ log q₁ > (2m+1)/δ > m(2m+1) ≥ 3` gives `X > e^3 > 4`. Discharged by: `Real.rpow_def_of_pos`,
  `Real.exp_lt_exp`/`Real.add_one_lt_exp`, `div_lt_iff`, `Real.exp_one_gt_d9` (`e > 2.7`, so `e^3 >
  19 > 4`) or `Real.add_one_le_exp` (`e^3 ≥ 4`): `nlinarith`. ~25 LOC. Attacks: [2] `m = 1`, `δ =
  0.5`, `log q₁ > 12`: `X ≥ e^{6 r₁} > 4` ✓. SURVIVED.
- **R12.6** `[gap]` `Roth.log_B₁_gt` — `δ r₁ log q₁ / 2 < log B₁`. Source `clean.tex:1370-1373`: >
  "whence B_1 = ⌊X⌋ > X−1 > √X = q_1^{δr_1/2}. Thus log B_1 > ½δr_1 log q_1." Discharged by: R12.4,
  `Real.log_lt_log` (`√X > 0`), `Real.log_sqrt`, `Real.log_rpow` (`q₁ > 0`). ~12 LOC. SURVIVED.
- **R12.7** `[gap]` `Roth.three_small_factors` — `2^{mr₁}, (1+A)^{mr₁}, (1+|α|)^{mr₁} < B₁^δ`.
  - Source `clean.tex:1374-1380`. Quote: > "Together with (32), this gives the three bounds used
    below: 2^{mr_1} < B_1^δ, (1+A)^{mr_1} < B_1^δ, (1+|α|)^{mr_1} < B_1^δ. For the first, use
    m log 2 < ½δ² log q_1; for the other two, use the corresponding logarithmic terms in (32)."
  - Match: identical. Discharged by: R12.5, R12.6, `Real.rpow_natCast`, `Real.log_lt_log_iff`,
    `Real.log_pow`, `Real.log_rpow` (`B₁ > 0` since `B₁ > √X > 2`: `Nat.cast_pos`), `Real.log_two_lt_d9`
    (`log 2 < 0.7 < 1`), `Real.log_nonneg` (`1 + A ≥ 1`, `1 + |α| ≥ 1`), `linarith` from (32).
    Source: 7 lines; ~50 LOC.
  - Attacks: [2] all three factors at `m r₁ = 0` are `1 < B₁^δ` (`B₁ > 1`) ✓ (`r₁ > 0`, `m ≥ 1`
    anyway). [3] `1 ≤ A` is used only for `log(1+A) ≥ 0` (true for `A ≥ 0`); harmless. SURVIVED.
- **R12.8** `[gap]` `Roth.abs_coeff_modByMonic_le` — `f` monic with `|coeff| ≤ A`, `|coeff P| ≤ C`,
  `natDegree P ≤ s` ⇒ `|(P %ₘ f).coeff i| ≤ (1+A)^{s+1−n} C`, `n = natDegree f`.
  - Source `clean.tex:1453-1466` and Lean note `clean.tex:1467-1474`. Quotes: > "When we divide this
    polynomial by f, the first operation we do (assuming s≥n) is to subtract w_sx^{s−n}f(x) and this
    gives a new polynomial whose coefficients are either of the form w_ν − a_{s−ν}w_s (when 1≤s−ν≤n)
    or of the form w_ν. Since the a_{s−ν}'s are bounded by A, the absolute values of the resulting
    coefficients are at most (1+A)·abc(…). If the input polynomial is zero, its remainder is zero.
    Otherwise the number of leading-term eliminations is at most max(0,s−n+1): there are none when
    s<n, and each elimination lowers the degree by at least one. It follows that abc(T) ≤
    (1+A)^{max(0,s−n+1)}B_1^{1+2δ}". Note: > "Use Polynomial.modByMonic directly in ℤ[X] ... Prove
    the coefficient bound by induction on degree, treating zero and degree less than n first; each
    leading-term elimination multiplies the bound by at most 1+A and lowers the degree."
  - Match: identical; `max(0, s−n+1) = s+1−n` in `ℕ`.
  - Discharged by: strong induction on `s`; `Polynomial.modByMonic_eq_self_iff` (`degree P < degree
    f` ⇒ `P %ₘ f = P`); else `P' := P − C (P.leadingCoeff) * X^{natDegree P − n} * f`, `natDegree P'
    < natDegree P` (`Polynomial.degree_sub_lt`, `leadingCoeff_mul`, `Monic.leadingCoeff`,
    `natDegree_C_mul_X_pow_mul`?), coefficient bound `(1+A) C` for `P'` (`Polynomial.coeff_sub`,
    `coeff_C_mul_X_pow_mul`?/`coeff_mul_X_pow'`, `abs_sub`, `abs_mul`, `hfA`), `Polynomial.modByMonic_eq_of_dvd_sub`
    (`f ∣ P − P'`: `Dvd.intro_left`), IH at `s − 1` with `C' = (1+A)C`, `pow_succ`. Source: 14 lines;
    ~70 LOC.
  - Attacks: [2] `P = 0`: remainder `0` ✓; `s < n`: exponent `0`, bound `C` ✓ (remainder is `P`);
    `f = X^n`, `P = X^s`, `s ≥ n`: remainder `0 ≤ …` ✓; `f = X − 1` (`A = 1`), `P = X^s`: remainder
    `1`, bound `2^s C` ✓ with `C ≥ 1`. [3] `0 ≤ A`, `0 ≤ C` needed for the inductive bound ✓ (implied by
    the hypotheses when `f, P ≠ 0`). SURVIVED.
- **R12.9** `[gap]` `Roth.boxFamily` (def), `ncard_boxFamily`, `boxFamily_finite`.
  Source `clean.tex:1399-1418`: > "Consider the set 𝒲 of all polynomials W = ∑_{s_1=0}^{r_1}⋯
  ∑_{s_m=0}^{r_m} c(s_1,…,s_m)x^s where the coefficients are integers satisfying 0 ≤ c(s) ≤ B_1.
  The number of such polynomials is |𝒲| = (B_1+1)^r with r = (r_1+1)⋯(r_m+1)." Discharged by: the
  bijection `boxFamily r B ≃ (box r → Icc 0 B)` via `W ↦ (d ↦ coeff d W)` and `c ↦ ∑_{d ∈ box} monomial
  d (c d)` (`MvPolynomial.ext`, `coeff_sum`, `coeff_monomial`, `Finset.sum_ite_eq`, `degreeOf_le_iff`
  + R1.1 for the degree bounds), `Set.ncard_eq_toFinset_card'`/`Set.ncard_congr`, `Fintype.card_fun`
  (`card (box r → Icc 0 B) = (B+1)^{card box}`), R1.1, `Nat.card_Icc`, `Set.Finite.of_finite_image`/
  `Set.finite_of_ncard_pos`-free: `Set.Finite` from the injection into a `Fintype`. ~70 LOC.
  Attacks: [2] `B = 0`: only `W = 0`, `ncard = 1 = 1^r` ✓; `m = 0`: `box = {0}`, `(B+1)^1` ✓.
  SURVIVED.
- **R12.10** `[gap]` `Roth.pigeonhole_count` — `1 < B`, `1 < c`, `0 < N`, `c n D ≤ N/2` ⇒
  `(2⌊B^c⌋₊+1)^{nD} < (B+1)^N`.
  - Source `clean.tex:1479-1500`. Quote: > "Pad each remainder with zero coefficients to length n.
    Each integer coefficient has fewer than 1+2B_1^{1+3δ} possible values. Since there are D
    derivatives, the number of possible remainder tuples is at most (1+2B_1^{1+3δ})^{nD}. By (45) and
    the definition of λ in (34) we have (1+3δ)nD ≤ 2(1+3δ)nm^{1/2}λ^{−1}r = ½r. Put c=1+3δ>1. Since
    B_1>1, 1+2B_1^c < [2(1+B_1)]^c. Indeed, (1+B_1)^c ≥ 1+B_1^c and 2^c ≥ 2, so the right-hand side
    is at least 2+2B_1^c. The tuple j=0 is allowed because γ>0, so D≥1. Using cnD ≤ r/2, we obtain
    (1+2B_1^c)^{nD} < [2(1+B_1)]^{cnD} ≤ [2(1+B_1)]^{r/2} < (1+B_1)^r = |𝒲|. The last strict
    inequality follows from 2(1+B_1) < (1+B_1)², or B_1>1."
  - Match: `1 + 2⌊B^c⌋ ≤ 1 + 2B^c` (integer coefficients bounded by `B^c` take at most `2⌊B^c⌋+1`
    values); the hypothesis `0 < N` replaces the source's `D ≥ 1` (attack [2] found the statement
    false for `N = 0`: `1 < 1`; with `N ≥ 1` the chain `… ≤ [2(1+B)]^{N/2} < (1+B)^N` is strict even
    when `nD = 0`, which is all that is needed — `N = ∏(r_j+1) ≥ 1` always).
  - Discharged by: `Nat.floor_le` (`⌊B^c⌋ ≤ B^c`), `Real.add_rpow_le_rpow_add` (`1 + B^c ≤ (1+B)^c`),
    `Real.rpow_le_rpow_left_iff`/`Real.one_lt_rpow` (`2 ≤ 2^c`), `Real.mul_rpow`, `Real.rpow_natCast`,
    `Real.rpow_le_rpow_of_exponent_le` (`[2(1+B)]^{cnD} ≤ [2(1+B)]^{N/2}`), `Real.rpow_natCast_mul`/
    `Real.sqrt_eq_rpow` (`[2(1+B)]^{N/2} = (2(1+B))^{N/2}` as `((2(1+B))^N)^{1/2}`), `pow_lt_pow_left`
    (`2(1+B) < (1+B)²`), `Real.sqrt_lt_sqrt`. Source: 10 lines; ~60 LOC.
  - Attacks: [2] `nD = 0`, `N = 1`, `B = 2`: `1 < 3` ✓; `n = D = 1`, `c = 1.5`, `B = 4`, `N = 3`
    (`c n D = 1.5 ≤ 1.5`): `(2·8+1)^1 = 17 < 5^3 = 125` ✓. [5] `Real.add_rpow_le_rpow_add` exists
    (grep `Mathlib/Analysis/SpecialFunctions/Pow/NNRpow.lean`/`Real.lean`: `Real.add_rpow_le_rpow_add
    {p : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y) (hp1 : 1 ≤ p) : x ^ p + y ^ p ≤ (x + y) ^ p`) — to be
    confirmed by `#check` at ticket time; fallback: convexity `Real.rpow` via `one_add_mul_self_le_rpow_one_add`
    (Bernoulli, `Real.one_add_mul_self_le_rpow_one_add`) also gives `1 + B^c ≤ (1+B)^c`? — no:
    Bernoulli gives `1 + c·B ≤ (1+B)^c`, not enough; the superadditivity lemma is the one needed, and
    if absent it follows from `Real.rpow_add_le_add_rpow`'s converse for `p ≥ 1`
    (`Real.rpow_add_le_add_rpow` is the `p ≤ 1` direction); as a last resort prove `1 + B^c ≤ (1+B)^c`
    from `Real.rpow_le_rpow` + `(1+B)^c = (1+B)^{c−1}(1+B) ≥ B^{c−1}·B + 1·1`. Recorded for the
    ticket. SURVIVED.
- **R12.11** `[internal]` `Roth.exists_ne_modByMonic_eq` — two distinct members of `𝒲` with the same
  remainder tuple.
  - Source `clean.tex:1501-1505`: > "Thus there are fewer remainder tuples than elements of 𝒲. By
    the pigeonhole principle, there are two distinct polynomials W',W''∈𝒲 such that Δ_jW'(x,…,x)
    − Δ_jW''(x,…,x) is divisible by f(x) for all j_1,…,j_m that satisfy (44)." Lean note
    `clean.tex:1515-1521`: > "map it to the nD integer coefficients of its remainder tuple. Apply
    finite pigeonhole using the strict cardinality estimate above."
  - Composition: the map `W ↦ (fun (j : J) (i : Fin n) => (diag (Δ_j W) %ₘ f).coeff i)` sends
    `boxFamily r B` (finite, R12.9) into `Fintype.piFinset (fun _ => Icc (−C) C)` (`hC`; degree `<
    n` so `coeff i` for `i ≥ n` vanish and need not be recorded: `Polynomial.degree_modByMonic_lt`,
    `Polynomial.coeff_eq_zero_of_degree_lt`); `Finset.exists_ne_map_eq_of_card_lt_of_maps_to` with
    `card (piFinset) = (2C+1)^{n·|J|}` (`Fintype.card_piFinset`, `Int.card_Icc`) `< (B+1)^{∏} =
    card 𝒲` (R12.9, `hcount` cast from `ℝ` to `ℕ`: `Nat.cast_lt`, `Nat.cast_pow`); equal images give
    equal remainders coefficientwise (`Polynomial.ext` with the vanishing of high coefficients).
    ~70 LOC.
  - Composition attack: the strict inequality in `hcount` is between real numbers; both sides are
    naturals, so `Nat.cast_lt` transfers ✓. If `J = ∅` the codomain has one element and the
    hypothesis `1 < (B+1)^N` must hold — it does when `B ≥ 1` and `N ≥ 1` ✓ (`hcount` as given).
    SURVIVED.
- **R12.12** `[gap]` `Roth.sub_mem_RSet` — `W', W'' ∈ 𝒲`, `W' ≠ W''` ⇒ `W' − W'' ∈ RSet B r`.
  Source `clean.tex:1511-1513` and note `clean.tex:1522-1523`: > "Also W^* is not identically zero,
  and its coefficients in absolute value do not exceed B_1." > "Distinct arrays give a nonzero
  difference with coefficient bound B_1, not 2B_1, because both arrays lie in [0,B_1] coordinatewise".
  Discharged by: `sub_ne_zero.2`, `MvPolynomial.degreeOf_sub_le`, `max_le`, `coeff_sub`, `abs_sub_le_iff`
  (`0 ≤ c', c'' ≤ B` ⇒ `|c' − c''| ≤ B`), `Int.cast_le`. ~15 LOC. SURVIVED.
- **R12.13** `[gap]` `Roth.eval_hasseDeriv_sub_eq_zero` — equal remainders ⇒ `Δ_j(W'−W'')(α,…,α) = 0`.
  Source `clean.tex:1505-1510`: > "Hasse differentiation, diagonal substitution and remainder
  modulo the fixed monic f are additive, so equality of remainder tuples implies the stated
  divisibility for the difference. For all j satisfying (44) Δ_jW^*(x_1,…,x_m) are zero when
  x_1=⋯=x_m=α." Discharged by: `map_sub` (`hasseDeriv`), R3.10 (`diag_sub`), `Polynomial.sub_modByMonic`,
  `Polynomial.modByMonic_eq_zero_iff_dvd`, `Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero`
  (`f ∣ g`, `aeval α f = 0` ⇒ `aeval α g = 0`), R3.10 (`eval_diag`) + R0.8 (`hasseDeriv_map`) +
  `Polynomial.aeval_def`/`eval_map`. ~25 LOC. Attacks: [2] `W' = W''`: trivially `0` ✓. SURVIVED.
- **R12.14** `[gap]` `Roth.le_index_of_forall_eval_eq_zero` — vanishing of all box-derivatives of
  weight `≤ c` at `α` ⇒ `c ≤ index`. Source `clean.tex:1510-1511`: > "Multi-indices outside the
  degree box give identically zero derivatives as well. Hence the index of W^* at the point (α,…,α)
  relative to r_1,…,r_m is at least γ." Discharged by: R7.4 (`le_index_iff`), by cases `d ∈ box r`
  (`hvan` + `not_le`) or not (R0.14 + R1.1 `mem_box`). ~15 LOC. SURVIVED.
- **R12.15** `[mathlib]` `Roth.lem7_hyp_of_h32` — `m(2m+1)/δ < log q₁` from (29) and (32).
  Source `clean.tex:1330-1336`: > "If m,δ,r,q satisfy (29)–(33) then they satisfy the conditions of
  Lemma 7. Proof. We just need to verify δ log q_1 > m(2m+1) but this is immediate from (29) and
  (32)." Discharged by: `Real.log_nonneg`, `div_lt_iff`, `nlinarith` (`δ² log q₁ > 2m+1`, `δ m < 1`
  ⇒ `δ log q₁ > (2m+1)/δ > m(2m+1)`). ~12 LOC. Attacks: [2] `m = 0`: `δ < 1/0 = 0` contradicts
  `0 < δ` — vacuous ✓. SURVIVED.
- **R12.16** `[mathlib]` `Roth.exists_hasseDeriv_eval_ne_zero` — `index P α r < c` ⇒ `∃ k, weight r k
  < c ∧ (Δ_k P)(α) ≠ 0`. Source `clean.tex:1529-1536`: > "By Lemma 7 the index of W^* at (h_1/q_1,
  …,h_m/q_m) relative to r_1,…,r_m is less than η. Hence W^* has some derivative Q = Δ_kW^* with
  k_1/r_1+⋯+k_m/r_m < η such that Q(h_1/q_1,…,h_m/q_m) ≠ 0." Discharged by: R7.3. ~4 LOC. SURVIVED.
- **R12.17** `[internal]` **Lemma 9** `Roth.main_lemma`.
  - Lean: `Roth/MainLemma.lean:141`
  - Source `clean.tex:1393-1407` (statement): > "Suppose (29)–(33) are satisfied, and suppose h_1,
    …,h_m are integers that are coprime to q_1,…,q_m respectively. Then there exists a nonzero
    polynomial Q(x_1,…,x_m) with integral coefficients, of degree at most r_j in x_j for 1≤j≤m, such
    that (1) The index of Q at the point (α,…,α) relative to r_1,…,r_m is at least γ−η>0; (2)
    Q(h_1/q_1,…,h_m/q_m)≠0; (3) for all non-negative integers i_1,…,i_m we have |Δ_{i_1,…,i_m}Q(α,…,α)|
    < B_1^{1+3δ}." Proof `clean.tex:1408-1562`, quoted in R12.9–R12.16 and: > "For W∈𝒲 we have
    abc(Δ_jW) ≤ 2^{r_1+⋯+r_m}B_1 ≤ 2^{mr_1}B_1 < B_1^{1+δ} ... r = (r_1+1)⋯(r_m+1) ≤ 2^{r_1+⋯+r_m} ≤
    2^{mr_1} < B_1^δ, and this implies rB_1^{1+δ} < B_1^{1+2δ}" ... > "By Lemma 8 and Equation (35),
    the number D of such derivatives satisfies D ≤ 2m^{1/2}λ^{−1}r" ... > "By Lemma index-of-derivative
    the index of Q at (α,…,α) relative to r_1,…,r_m is at least γ−η. This Q has properties (1) and
    (2) of Lemma 9. Since the coefficients of W^* have absolute value at most B_1, the coefficients of
    Q have absolute value at most 2^{r_1+⋯+r_m}B_1 ≤ 2^{mr_1}B_1 < B_1^{1+δ}. Hence the coefficients of
    any further derivative of Q have absolute value at most 2^{r_1+⋯+r_m}B_1^{1+δ} < B_1^{1+2δ}. ...
    For a zero derivative the desired estimate is immediate; otherwise the strict coefficient bound
    yields |Δ_iQ(α,…,α)| < B_1^{1+2δ}(1+|α|)^{r_1+⋯+r_m}, and this implies (3), since (1+|α|)^{mr_1}
    < B_1^δ."
  - Match: the statement is literal, with `A` any real `≥ 1` bounding `|a_i|` (the source's `A =
    max(1,|a_1|,…)` is one such), `m` with `[NeZero m]` and the chain (31) in consecutive-index form
    (`h31a`, `h31b`), `q 0 = q_1`, `r 0 = r_1`; "γ − η > 0" is R12.3 from `h30` (not restated in the
    conclusion, available as a separate fact).
  - Composition: constants `n := natDegree f`, `λ, γ, η, B₁` (R12.1); `η < γ` (R12.3); `X := q_0^{δ
    r_0} > 4` (R12.5 using `h32`'s first term), `B₁ > √X > 2` and `B₁ ≤ X` (R12.4), the three small
    factors (R12.7); `J := (box r).filter (weight r · ≤ γ)` with `|J| ≤ 2√m/λ · N` (R11.4, cast);
    for `W ∈ 𝒲` and `j ∈ J`: `|coeff (Δ_j W)| ≤ 2^{∑r} B₁ ≤ 2^{m r₀} B₁ < B₁^{1+δ}` (R3.6, `∑ r_j ≤ m
    r_0` from the chain's antitonicity, R12.7), `|coeff (diag …)| ≤ N·2^{m r₀}B₁ < B₁^{1+2δ}` (R3.11,
    R1.2, `N ≤ 2^{∑ r} < B₁^δ` via `∏(r_j+1) ≤ ∏ 2^{r_j}`: `Nat.lt_two_pow`/`Finset.prod_le_prod`,
    `Finset.prod_pow_eq_pow_sum`), `natDegree (diag …) ≤ ∑ r ≤ m r₀` (R3.12), remainder coefficients
    `≤ (1+A)^{m r₀ + 1 − n} B₁^{1+2δ} ≤ (1+A)^{m r₀} B₁^{1+2δ} < B₁^{1+3δ}` (R12.8, `pow_le_pow_right`,
    R12.7), so with `C := ⌊B₁^{1+3δ}⌋₊` the hypothesis `hC` of R12.11 holds (`Int.natAbs`/`Nat.floor`
    cast: `|z| ≤ x → |z| ≤ ⌊x⌋₊` for integers `z`); `hcount` from R12.10 with `c := 1+3δ`, `n`, `D :=
    |J|`, `N := ∏(r_j+1) > 0`, `c n D ≤ N/2` from `|J| ≤ 2√m N/λ` and `λ = 4(1+3δ)n√m` (`field_simp`,
    `mul_div_assoc`); R12.11 gives `W', W''`; `W* := W' − W'' ∈ RSet B₁ r` (R12.12) ⊆ `RSet X r`
    (`B₁ ≤ X`); `index (map W*) (fun _ => α) r ≥ γ` (R12.14 + R12.13 + R2.3-free: `eval` of the
    derivative of the *real* polynomial is the cast of the integer one — `hasseDeriv_map`, `eval_map`);
    Lemma 7 (R10.4 after `obtain ⟨n', rfl⟩ : ∃ n', m = n'+1` and converting the chain hypotheses
    `h31a`/`h31b` into `hrlast`/`hratio`; `hq1` from R12.15) gives `Θ X q r < η` and `index (map W*)
    (h/q) r ≤ Θ` (R8.1 `index_le_Θ`), so `< η`; R12.16 gives `k` with `weight r k < η` and `eval
    (h/q) (Δ_k W*) ≠ 0`; `Q := Δ_k W*` (integer polynomial; its real version is `Δ_k (map W*)` by
    R0.8); `Q ≠ 0` (its evaluation is nonzero), `degreeOf j Q ≤ r j` (R0.13), (1): R7.7 with `weight r
    k < η` (`sub_le_sub_left`), (2) ✓, (3): `|coeff Q| ≤ 2^{m r₀} B₁ < B₁^{1+δ}` (R3.6), `|coeff (Δ_i
    Q)| ≤ 2^{m r₀} · 2^{m r₀} B₁ < B₁^{1+2δ}` (R3.6 again, R12.7), `|eval| ≤ bound · ∏(1+|α|)^{r_j}
    ≤ bound · (1+|α|)^{m r₀} < B₁^{1+2δ} B₁^{δ} = B₁^{1+3δ}` (R3.14, `Finset.prod_pow_eq_pow_sum`,
    `pow_le_pow_right`, R12.7, `Real.rpow_add`). Source: 160 lines; ~250 LOC of assembly.
  - Composition attacks: (i) **Which `B` in Lemma 7?** Lemma 7 is applied with `B = q_0^{δ r_0} = X
    ≥ B₁` and `RSet B₁ r ⊆ RSet X r` ✓ (the source: "W^* ∈ ℛ_m(q_1^{δr_1}; r)"). (ii) **`D ≥ 1`?** Not
    needed in Lean (R12.10 uses `N ≥ 1`). (iii) **Strictness in (3)**: `|eval| ≤ B·(1+|α|)^{mr₀}` with
    `B < B₁^{1+2δ}` and `(1+|α|)^{mr₀} < B₁^δ`, both positive, so the product is `< B₁^{1+3δ}` ✓; for
    a zero derivative `0 < B₁^{1+3δ}` ✓. (iv) The index of `Q` at `α`: R7.7 needs `Δ_k (map W*) ≠ 0`
    ✓ (nonzero evaluation). (v) The source's `∑ r_j ≤ m r_1` uses `r_1 = max`: from `h31b` and `δ <
    1` the sequence is antitone, so `r_j ≤ r_0` ✓ (a small auxiliary fact inside the proof). (vi) All
    hypotheses of R10.4 are available: `δ < 1/m`, `r_last > 10/δ` (`h31a`), chain (`h31b`), `q_j > 0`,
    `(n+1)(2(n+1)+1)/δ < log q_0` (R12.15 with `m = n+1`), (33) ✓. SURVIVED.

---

## Result R13: the theorem (§6–§7 of [TY], `Roth/Main.lean`)

### Plain-English proof (source structure)

[TY] §6 `clean.tex:1139-1190` (reduction): if the theorem fails for `α`, pick `M > 0` with `Mα` an
algebraic integer (clear denominators of a rational annihilating polynomial), multiply the
inequality by `M`, take `2 < κ' < κ`; for `q` large `M/q^κ < 1/q^{κ'}`; only finitely many solutions
have bounded `q`, so infinitely many remain; `Mα` is still irrational. §7 `clean.tex:1565-1690`:
choose reduced solutions of arbitrarily large denominator; choose `m` with `m > 4n√m` and `2m/(m −
4n√m) < κ` (47), then `δ` with (29), (30) and (48) ⟺ (49) `m(1+4δ)/(γ−η) < κ`; pick a reduced
solution `(h_1,q_1)` with `q_1` satisfying (32), then `(h_j,q_j)` with `log q_j/log q_{j−1} > 2/δ`
(50); `r_1 > 10 log q_m/(δ log q_1)` (51), `r_j = ⌈r_1 log q_1/log q_j⌉` (52); then (33), (53) `r_j
log q_j/(r_1 log q_1) < 1 + δ/10`, and (31) hold. Lemma 9 gives `Q`; `(∏ q_j^{r_j}) Q(h/q)` is a
nonzero integer so `|Q(h/q)| ≥ ∏q_j^{−r_j} > q_1^{−mr_1(1+δ)}` (54); Taylor at `(α,…,α)`: the terms
of weight `< γ−η` vanish, the others are bounded using `|h_j/q_j − α| < q_j^{−κ}` and `q_j ≥
q_1^{r_1/r_j}`, giving `|Q(h/q)| < (∏(r_j+1))B_1^{1+3δ}q_1^{−r_1(γ−η)κ} < B_1^{1+4δ}q_1^{−r_1(γ−η)κ} ≤
q_1^{(1+4δ)δr_1 − r_1(γ−η)κ}`; comparing exponents, `κ < m(1+4δ)/(γ−η)`, contradicting (49).

- **R13.1** `[gap]` `Roth.approxSet` (def). Source `clean.tex:1139-1142`: > "Let α be an irrational
  real algebraic number and let κ∈ℝ. Suppose there are infinitely many pairs of integers h,q with
  q>0 such that |α − h/q| < 1/q^κ." Match: `approxSet α κ = {(h,q) | 0 < q ∧ |α − h/q| < 1/q^κ}`
  with `q : ℕ` (so `q > 0` is `0 < q`), real power. SURVIVED.
- **R13.2** `[mathlib]` `Roth.exists_nat_mul_isIntegral` — `IsAlgebraic ℚ α → ∃ M > 0, IsIntegral ℤ (M α)`.
  Source `clean.tex:1150-1163`: > "If α is an algebraic number, there is an integer M>0 such that Mα
  is an algebraic integer. Proof. Clear denominators in a nonzero rational polynomial annihilating α
  and change its sign so that its leading coefficient is a positive integer M ... Then β=Mα
  satisfies the monic integral equation ... Thus Mα is an algebraic integer." Discharged by:
  `IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ` (`IsAlgebraic ℤ α`), `IsAlgebraic.exists_integral_multiple`
  (`∃ y ≠ 0, IsIntegral ℤ (y • α)`), `M := y.natAbs`, `Int.natAbs_eq`/`Int.cast_natAbs`,
  `IsIntegral.neg`, `zsmul_eq_mul`. ~20 LOC. Attacks: [5] the two mathlib names `#check`ed (with
  `import Mathlib`); `exists_integral_multiple` returns the leading coefficient, as in the source.
  SURVIVED.
- **R13.3** `[gap]` `Roth.approxSet_den_le_finite` — solutions with `q ≤ Q₀` are finitely many.
  Source `clean.tex:1174-1177`: > "For a fixed upper bound on q, there are only finitely many
  possible integers h satisfying the approximation inequality." Discharged by: the set is contained
  in `Icc (−K) K ×ˢ Icc 1 Q₀` with `K := ⌈Q₀(|α| + max 1 Q₀^{−κ})⌉` (`|h| ≤ q|α| + q·q^{−κ}`,
  `Real.rpow_le_rpow_left_iff`/cases on the sign of `κ`), `Set.Finite.subset`, `Set.finite_Icc`,
  `Set.Finite.prod`. ~40 LOC. Attacks: [2] `κ < 0` makes `1/q^κ = q^{|κ|}` large but still bounded
  for `q ≤ Q₀` ✓ handled by the `max`. SURVIVED.
- **R13.4** `[mathlib]` `Roth.eventually_div_rpow_lt` — `0 < M`, `κ' < κ` ⇒ `∃ Q₀, ∀ q > Q₀, M/q^κ <
  1/q^{κ'}`. Source `clean.tex:1170-1173`: > "Pick any κ' such that 2<κ'<κ. Then for q large enough,
  M/q^κ < 1/q^{κ'}." Discharged by: `Q₀ := ⌈M^{1/(κ−κ')}⌉₊`, `Real.rpow_lt_rpow_left_iff`/
  `Real.rpow_natCast`, `div_lt_div_iff`, `Real.rpow_sub` (`q^κ = q^{κ'} q^{κ−κ'}`), `Real.rpow_lt_rpow`
  (`q > M^{1/(κ−κ')}` ⇒ `q^{κ−κ'} > M`: `Real.rpow_inv_lt_iff_of_pos`?/`Real.lt_rpow_inv_iff_of_pos`),
  `Nat.le_ceil`. ~30 LOC. SURVIVED.
- **R13.5** `[internal]` `Roth.reduction` — if infinitely many approximations with `κ > 2` exist for
  an irrational algebraic `α`, then for some irrational algebraic *integer* `α'` and some `κ' > 2`.
  Source `clean.tex:1145-1190` (quoted above; statement `clean.tex:1145-1147`: > "If the theorem
  fails, then it also fails for an irrational real algebraic integer."). Composition: R13.2 (`M`),
  `κ' := (κ+2)/2`, R13.4 (`Q₀`), the set `S := {(h,q) ∈ approxSet α κ | Q₀ < q}` is infinite
  (`Set.Infinite.diff` with R13.3), the map `(h,q) ↦ (M h, q)` is injective (`Prod.ext`,
  `mul_right_injective₀`) and sends `S` into `approxSet (M α) κ'` (`|Mα − Mh/q| = M|α − h/q| <
  M/q^κ < 1/q^{κ'}`: `abs_mul`, `mul_div_assoc`, `Nat.cast_pos`), `Set.Infinite.image`/`Set.infinite_of_injOn_mapsTo`;
  `Irrational (M α)` from `Irrational.natCast_mul` (`M ≠ 0`); `IsIntegral ℤ (M α)` from R13.2. ~60
  LOC. Composition attacks: `(κ+2)/2 > 2` ✓ and `< κ` ✓ for `κ > 2`. SURVIVED.
- **R13.6** `[gap]` `Roth.exists_monic_aeval_eq_zero` — `Irrational α`, `IsIntegral ℤ α` ⇒ `∃ f monic,
  aeval α f = 0 ∧ 2 ≤ natDegree f`. Source `clean.tex:1192-1199`: > "Since α is an algebraic
  integer, by definition, there is a polynomial f(x)=x^n+a_1x^{n−1}+⋯+a_n with integral coefficients
  such that f(α)=0. Its degree n is at least 2, since α is irrational." Discharged by: `hint : ∃ f,
  Monic f ∧ eval₂ _ α f = 0` (definition of `IsIntegral`), `Polynomial.Monic.natDegree_eq_zero_iff_eq_one`
  (degree `0` ⇒ `f = 1` ⇒ `aeval = 1 ≠ 0`), degree `1` ⇒ `f = X + C a` (`Polynomial.Monic.eq_X_add_C`
  for `natDegree = 1`) ⇒ `α = −a` rational, contradicting `irrational_iff_ne_rational`/`Irrational.ne_int`.
  ~25 LOC. SURVIVED.
- **R13.7** `[gap]` `Roth.exists_reduced_approx` — reduced solutions with arbitrarily large denominator.
  Source `clean.tex:1578-1590`: > "We first justify choosing reduced solutions of arbitrarily large
  denominator. Reducing h/q to a/b with b>0 and gcd(a,b)=1 preserves the inequality, since b≤q and
  κ>0. For a fixed rational value a/b, irrationality gives ε=|α−a/b|>0. The inequality ε<q^{−κ}
  bounds its original denominators q, so only finitely many original pairs can represent that
  rational value. There are therefore infinitely many distinct reduced solutions. For bounded b,
  their numerators a lie in finite intervals, so the reduced denominators are unbounded as well."
  Discharged by: `Rat.divInt`/`Rat.num_div_den` to reduce (`x := (h : ℚ)/q`, `a := x.num`, `b :=
  x.den`, `Rat.reduced`/`Rat.num_den`-coprimality `x.reduced : x.num.natAbs.Coprime x.den` → `IsCoprime`
  via `Int.isCoprime_iff_gcd_eq_one`, `Nat.Coprime`), `b ∣ q` hence `b ≤ q` (`Rat.den_dvd`), `1/q^κ ≤
  1/b^κ` (`Real.rpow_le_rpow`, `κ > 0`); the set of reduced solutions is infinite because the map
  `(h,q) ↦ (a,b)` has finite fibres (R13.3-style: for fixed `(a,b)`, `q^κ < 1/ε` bounds `q`:
  `Real.rpow_lt_rpow_left_iff`; `Set.Finite.of_finite_image`-converse: `Set.infinite_of_finite_fibers`?
  (`Set.Infinite.exists_not_mem_finset`/`Set.infinite_image_iff`-free: if the image were finite the
  preimage, a finite union of finite fibres, would be finite — `Set.Finite.biUnion`), then R13.3
  applied to the reduced set removes `b ≤ Q₀`. ~80 LOC. Attacks: [2] `κ > 0` needed for `b ≤ q ⇒
  q^{−κ} ≤ b^{−κ}` ✓ (hypothesis). SURVIVED.
- **R13.8** `[gap]` `Roth.exists_m` — `0 < n`, `2 < κ` ⇒ `∃ m, 16n² < m ∧ 4n√m < m ∧ 2m/(m−4n√m) < κ`.
  Source `clean.tex:1592-1597`: > "We choose a positive integer m large enough that m > 4nm^{1/2}
  and 2m/(m−4nm^{1/2}) < κ, which is possible as κ>2." Discharged by: `m := s^2` with `s := ⌈4κn/(κ−2)⌉₊
  + 4n + 1` (`Real.sqrt_sq`, `Nat.cast_pow`), `s > 4n` ⇒ `4n s < s²` and `16n² < s²`; `2s²/(s²−4ns) =
  2s/(s−4n) < κ ⟺ s(κ−2) > 4κn` (`div_lt_iff`, `Nat.le_ceil`, `nlinarith`). ~35 LOC. Attacks: [2] `n
  = 1`, `κ = 3`: `s ≥ 12 + 5 = 17`, `m = 289`, `2·289/(289 − 68) ≈ 2.62 < 3` ✓. SURVIVED.
- **R13.9** `[gap]` `Roth.exists_delta` — `0 < n`, `16n² < m`, (47) ⇒ `∃ δ, 0 < δ ∧ δ < 1/m ∧ (30) ∧
  m(1+4δ)/(γ−η) < κ`.
  - Source `clean.tex:1598-1607`. Quote: > "For δ small enough we have m − 4(1+3δ)nm^{1/2} − 2η > 0.
    This condition is the same as (30). By the fixed-m form of Lemma m-delta, we can choose δ so it
    also satisfies (29). Decreasing δ further if necessary, we also arrange that 2m(1+4δ)/(m −
    4(1+3δ)nm^{1/2} − 2η) < κ. This is possible because the left-hand side tends to the strictly
    smaller quantity in (47) as δ→0⁺. By the definition of γ and η from (35) and (36), (48) is
    equivalent to m(1+4δ)/(γ−η) < κ."
  - Match: the limit argument is replaced by explicit thresholds: with `E := κ(m−4n√m)/2 − m > 0`
    (⟺ (47)), (49) ⟺ `4mδ + 6κnδ√m + κη < E`, so `δ < E/(12m)`, `δ < E/(18κn√m)`, `δ < (E/(3κ10^m))^{2^m}`
    suffice (each term `< E/3`); combine with R12.2's `δ₀` by `δ := ½ min{…}`. The source's own
    `m-δ` proof uses the same explicit-threshold device.
  - Discharged by: R12.2 (`δ₀`), `lt_min_iff`, `Real.rpow_lt_rpow`-type bound for `η` as in R12.2,
    `div_lt_iff` (`γ − η > 0` by R12.3), `nlinarith`/`linarith` with the three term bounds,
    `Real.sqrt_pos`. ~70 LOC.
  - Attacks: [2] `n = 1`, `m = 289`, `κ = 3`: `E = 3(289−68)/2 − 289 = 42.5 > 0` ✓ thresholds
    positive ✓. [3] (47) is exactly `E > 0` ✓; `0 < n` needed for the explicit thresholds (division
    by `n`). SURVIVED.
- **R13.10** `[gap]` `Roth.exists_approximants` — `m` reduced solutions `(h_j, q_j)` with `q_j > 1`,
  `log q_0 > L` and `2/δ · log q_i < log q_{i+1}`.
  Source `clean.tex:1608-1614`: > "Next, pick a reduced solution h_1,q_1 of (46) such that q_1
  satisfies (32). This means q_1 is very large. We then choose solutions h_2,q_2;…;h_m,q_m with
  gcd(h_j,q_j)=1 for all j to satisfy log q_j/log q_{j−1} > 2/δ, 2≤j≤m." Discharged by: iterate R13.7
  (`Fin.induction`/`Nat.rec` building a sequence `s : ℕ → ℤ × ℕ` with `s 0` having `q > max(⌈e^L⌉₊, 1)`
  (`Real.exp_lt_exp`, `Real.log_exp`, `Real.lt_log_iff_exp_lt`) and `s (i+1)` having `q >
  ⌈(q_i)^{2/δ}⌉₊` (`Real.log_rpow`, `Real.log_lt_log`), then restrict to `Fin m`); the chain
  condition for consecutive indices follows from the recursion (`Fin.val` arithmetic). ~70 LOC.
  Attacks: [2] `m = 1`: only `q_0` needed ✓; `[NeZero m]` ensures `q 0` makes sense. SURVIVED.
- **R13.11** `[gap]` `Roth.exists_degrees` — the rounding lemma (51)–(53), (31), (33).
  - Source `clean.tex:1615-1635` and Lean note `clean.tex:1637-1642`. Quotes: > "We now take r_1 to
    be any integer satisfying r_1 > 10 log q_m/(δ log q_1) and define integers r_2,…,r_m by
    r_1 log q_1/log q_j ≤ r_j < 1 + r_1 log q_1/log q_j, 2≤j≤m. Then (33) is satisfied. Also,
    r_j log q_j/(r_1 log q_1) < 1 + log q_j/(r_1 log q_1) ≤ 1 + log q_m/(r_1 log q_1) < 1 + δ/10.
    The conditions (31) are also satisfied since r_m ≥ r_1 log q_1/log q_m > 10δ^{−1}, and
    r_{j−1}/r_j > (log q_j/log q_{j−1})(1+δ/10)^{−1} > δ^{−1} by (52), (53), and (50)." Note:
    > "define r_j=⌈r_1 log q_1/log q_j⌉ for j≥2, and collect positivity, (31), (33) and (53) in one
    rounding lemma."
  - Match: identical; in Lean `r_1 := ⌈10 log q_last/(δ log q_0)⌉₊ + 1`, `r_j := ⌈r_0 log q_0/log q_j⌉₊`
    for `j ≠ 0` (with `r_0` itself), conclusions `0 < r_j`, `10/δ < r_j` for all `j` (the source's
    `r_m > 10/δ` plus antitonicity; stated for all `j` since this is what Lemma 9 consumes), the
    chain `r_{i+1}/δ < r_i`, (33), and (53) in the form `r_j log q_j < (1 + δ/10)(r_0 log q_0)`.
  - Discharged by: `Nat.le_ceil`, `Nat.ceil_lt_add_one`, `div_le_iff`, `lt_div_iff` (`log q_j > 0`:
    `Real.log_pos`), `Real.log_le_log` (`q_0 ≤ q_j` from the chain: `q_j > q_{j−1}` since `log q_j >
    (2/δ) log q_{j−1} > log q_{j−1}`), the chain of (50) in consecutive-index form, `nlinarith`
    (`(2/δ)/(1+δ/10) > 1/δ ⟺ 2 > 1 + δ/10`). Source: 20 lines; ~110 LOC.
  - Attacks: [2] `m = 1`: only `r_0 > 10 log q_0/(δ log q_0) = 10/δ` ✓, other conclusions vacuous ✓.
    [3] `δ < 1` is used in `2 > 1 + δ/10` ✓ (hypothesis `hδ1`). (ii) In (53) the source compares with
    `log q_m` (the largest); `log q_j ≤ log q_last` by monotonicity along the chain ✓ (the Lean
    statement has `r_j log q_j < (1+δ/10) r_0 log q_0` directly). SURVIVED.
- **R13.12** `[gap]` `Roth.one_le_prod_pow_mul_abs_eval` — (54), denominator clearing.
  Source `clean.tex:1647-1651`: > "Also, since Q has degree at most r_j in x_j for 1≤j≤m, the
  number (∏_jq_j^{r_j})Q(h_1/q_1,…,h_m/q_m) is a nonzero integer: each monomial denominator divides
  ∏_jq_j^{r_j}. Its absolute value is at least 1". Discharged by: `MvPolynomial.eval_eq` (sum over
  support), `Finset.mul_sum`, per monomial `(∏ q_j^{r_j}) c_d ∏ (h_j/q_j)^{d_j} = c_d ∏ h_j^{d_j}
  q_j^{r_j−d_j}` (`Finset.prod_mul_distrib`, `div_pow`, `pow_sub₀`-free: `q_j^{r_j} = q_j^{d_j}
  q_j^{r_j−d_j}` with `d_j ≤ r_j` from `degreeOf_le_iff`, `mul_div_cancel_left₀`), an integer
  (`Int.cast_sum`, `Int.cast_mul`, `Int.cast_pow`); `Int.one_le_abs` (nonzero since the real value
  is nonzero and `∏ q_j^{r_j} ≠ 0`). ~50 LOC. Attacks: [2] `Q = C c`, `c ≠ 0`: `∏ q^{r} |c| ≥ 1` ✓.
  SURVIVED.
- **R13.13** `[gap]` `Roth.abs_eval_lt_of_le_index` — the Taylor upper bound.
  - Source `clean.tex:1655-1675`. Quote: > "On the other hand, we have Q(h_1/q_1,…,h_m/q_m) =
    ∑_{i_1=0}^{r_1}⋯∑_{i_m=0}^{r_m}Δ_{i}Q(α,…,α)(h_1/q_1−α)^{i_1}⋯(h_m/q_m−α)^{i_m}. By (1) of Lemma 9
    the terms with i_1/r_1+⋯+i_m/r_m < γ−η vanish. In every other term, the weight is positive, so
    at least one i_j is positive and the product estimate is strict. We have |(h_1/q_1−α)^{i_1}⋯
    (h_m/q_m−α)^{i_m}| < 1/(q_1^{i_1}⋯q_m^{i_m})^κ ≤ q_1^{−r_1(γ−η)κ}, since q_j ≥ q_1^{r_1/r_j} by
    (52). By using (3) of Lemma 9 we have |Q(h_1/q_1,…,h_m/q_m)| < (r_1+1)⋯(r_m+1)B_1^{1+3δ}
    q_1^{−r_1(γ−η)κ}". Lean note `clean.tex:1691-1694`: > "For strictness, use γ−η>0 to ensure each
    surviving Taylor term has a positive exponent; treat zero coefficients separately."
  - Match: stated for a general real polynomial `Q ≠ 0` with `c ≤ index Q (α,…,α) r`, `c > 0` (the
    role of `γ−η`), `|Δ_i Q(α,…,α)| < C` (the role of `B_1^{1+3δ}`), `q_j ≥ q_0^{r_0/r_j}`; conclusion
    `|Q(h/q)| < (∏(r_j+1)) · C · q_0^{−r_0 c κ}`.
  - Discharged by: R2.10 (`eval_eq_sum_box`), `Finset.abs_sum_le_sum_abs`, for `d ∈ box r`: if
    `weight r d < c` then `eval α (Δ_d Q) = 0` (R7.2 contrapositive), else `|∏ (h_j/q_j − α)^{d_j}| ≤
    ∏ (q_j^{−κ})^{d_j}` (`abs_prod`, `abs_pow`, `pow_le_pow_left`, `happ`, `Real.rpow_neg`) `≤ ∏
    (q_0^{r_0/r_j})^{−κ d_j} = q_0^{−κ r_0 · weight r d} ≤ q_0^{−κ r_0 c}` (`Real.rpow_le_rpow_left_iff`
    with `q_0 ≥ 1`, `Real.rpow_natCast`, `Real.rpow_mul`, `Finset.prod_pow_eq_pow_sum`-type
    `Real.rpow_sum_of_pos`, `weight r d ≥ c`, `κ > 0`), hence each term is `≤ C · q_0^{−r_0cκ}` with
    strict inequality whenever the term is nonzero (`mul_lt_mul_of_pos_right`/`abs_mul`), and the sum
    of `card (box r) = ∏(r_j+1)` terms is `< ∏(r_j+1) · C · q_0^{…}` (`Finset.sum_lt_sum` with at
    least one strict term, or all terms zero and `0 < RHS`), R1.1. Source: 15 lines; ~100 LOC.
  - Attacks: [2] all box terms vanish except possibly `d = 0`; `d = 0` has weight `0 < c` so it
    vanishes too ⇒ `eval = 0 < RHS` ✓ consistent. [3] `q_0 ≥ 1` (from `hq`) suffices for the
    exponent comparison (for `q_0 = 1` both sides are `1`) ✓; `c > 0` is needed only for the
    source's strictness remark, which the Lean proof gets from `C > |…| ≥ 0` instead — kept as a
    hypothesis for fidelity. SURVIVED.
- **R13.14** `[internal]` `Roth.roth_of_isIntegral` — Roth's theorem for irrational algebraic integers.
  - Lean: `Roth/Main.lean:112`
  - Source `clean.tex:1565-1690` (§7, quoted in R13.7–R13.13), conclusion `clean.tex:1680-1690`:
    > "Comparing this with (54), and using q_1>1, we obtain −mr_1(1+δ) < (1+4δ)δr_1 − r_1(γ−η)κ, or
    κ < (m(1+δ) + δ(1+4δ))/(γ−η) < m(1+4δ)/(γ−η), where the second inequality uses 1+4δ<3m, which
    follows from m>16n²≥64 and δ<1/m. This contradicts (49) and finishes the proof of the theorem."
  - Composition: `by_contra` (`2 < κ`); R13.6 (`f`, `n ≥ 2`), `A := max 1 (sup |a_i|)` (`Finset.le_sup`,
    `1 ≤ A`); R13.8 (`m`), `[NeZero m]` (`m > 0`); R13.9 (`δ`); `L := (2m+1 + 2m log(1+A) + 2m
    log(1+|α|))/δ²` and R13.10 (`h, q`; `log q_0 > L` gives (32)); R13.11 (`r`); R12.17 (Lemma 9) gives
    `Q`; R13.12 and R13.13 with `c := γ−η`, `C := B₁^{1+3δ}`, `q_j ≥ q_0^{r_0/r_j}` from (33)
    (`Real.rpow_le_iff_le_log`/`Real.log_rpow`, `div_mul_eq_mul_div`); then: `∏ q_j^{r_j} <
    q_0^{m r_0 (1+δ)}` from (53) (`Real.exp_sum`/logs: `∑ r_j log q_j < m(1+δ/10) r_0 log q_0 ≤ m(1+δ)
    r_0 log q_0`, `Real.rpow_natCast`, `Real.exp_lt_exp`), `∏(r_j+1) ≤ 2^{m r_0} < B₁^δ` (R12.7,
    antitone `r`), `B₁ ≤ q_0^{δ r_0}` (R12.4), so `q_0^{−m r_0(1+δ)} < |Q(h/q)| < q_0^{δ r_0(1+4δ) −
    r_0(γ−η)κ}` (`Real.rpow_add`, `Real.rpow_mul`), `Real.rpow_lt_rpow_left_iff` (`q_0 > 1`) gives
    `−m(1+δ) < δ(1+4δ) − (γ−η)κ` (divide by `r_0 > 0`), hence `(γ−η)κ < m(1+δ) + δ(1+4δ) < m(1+4δ)`
    (`1 + 4δ < 3m` from `m ≥ 65`, `δ < 1`), i.e. `κ < m(1+4δ)/(γ−η)` (`lt_div_iff`, `γ−η > 0`),
    contradicting R13.9's (49). Source: 50 lines; ~200 LOC of assembly.
  - Composition attacks: (i) **(32) for `q_0`:** R13.10 provides `log q_0 > L` with `L` chosen as
    `(RHS of (32))/δ²` ⇒ `δ² log q_0 > RHS` ✓ (`δ² > 0`). (ii) **Lemma 9 needs `16n² < m`** ✓ (R13.8)
    and `h30` ✓ (R13.9), `h31a/h31b/h33` ✓ (R13.11), `hq1 : 1 < q 0` ✓ (R13.10), coprimality ✓
    (R13.10). (iii) **The exponent comparison** uses `q_0 > 1` so that `rpow` is strictly monotone in
    the exponent ✓. (iv) `1 + 4δ < 3m`: `m > 16n² ≥ 64` ✓ (`n ≥ 2`), `δ < 1/m < 1` ✓. (v) `κ > 0` is
    needed for R13.7/R13.13 — true since `κ > 2` ✓. SURVIVED.
- **R13.15** `[internal]` **`Roth.roth`** and `Roth.roth_rat`.
  - Lean: `Roth/Main.lean:118`, `:122`
  - Source `clean.tex:1143-1146`: > "Theorem (Roth). Under the above conditions, κ ≤ 2."
  - Composition: `roth`: if `κ ≤ 2` done; else R13.5 gives `α', κ'` and R13.14 gives `κ' ≤ 2`,
    contradiction (`le_of_not_lt`). `roth_rat`: the map `x ↦ (x.num, x.den)` is injective
    (`Rat.ext`/`Rat.num_den`) and sends the given set into `approxSet α κ` (`Rat.den_pos`, `Rat.cast_def`/
    `Rat.num_div_den`), so `Set.Infinite.image`/`Set.infinite_of_injective_forall_mem` + `roth`.
    ~15 + ~20 LOC. Composition attacks: the only case not covered by R13.14 is `κ ≤ 2`, which is the
    conclusion itself ✓. SURVIVED.

---

## API gaps summary

Every `[gap]` leaf above is new content whose proof is given by the source (quoted) and whose
discharge is a short composition of verified mathlib lemmas and earlier leaves; none requires
mathematics absent from the source. The only places where the Lean route differs *in form* from
the source's text are (each sanctioned by the source's own Lean implementation notes, quoted at the
leaf): the basis construction in Lemma 2 (R6.6, note `clean.tex:428-433`), submultiplicativity of
`‖·‖₁` in Lemma 3 (R3.3, note `clean.tex:482-488`), the `weightedOrder` bridge for the product
formula (R7.9/R7.15, note `clean.tex:549-556`), the explicit-threshold form of the `δ` choices
(R12.2/R13.9, note `clean.tex:1303-1309` and the source's own proof of Lemma `m-δ`), and the
`≠ 0`-hypothesis form of the `ind(0) = +∞` convention (R7.8–R7.10).

Statements corrected during the adversarial pass (recorded so the tickets do not re-introduce
them): R4.8 (`sum_natDegree_update_lt` needs linear independence), R0.19 (dropped an unnecessary
`[Algebra ℚ R]`), R12.10 (`pigeonhole_count` needs `0 < N`), R12.2/R13.9 (`0 < n`).

## Confidence gate (Step 5) — checklist

1. Every leaf is `[mathlib]` (≤ 3 verified lemmas) or `[gap]` with its discharge list of verified
   mathlib lemmas + earlier leaves (the API-gap sub-decomposition) — ✓ (all entries above).
2. The Lean skeleton compiles (`build-direct.sh`, all 12 modules, sorry warnings only) — ✓ (log
   below).
3. Every leaf has a verbatim source quote and a Lean ↔ source match paragraph — ✓.
4. Every leaf and internal node has an attack log with ≥ 3 categories and verdict SURVIVED — ✓
   (four statements were corrected, see summary above).
5. Prior-B2 log consulted: empty — ✓.
6. The tree mirrors the source's structure (sections → results, the source's lemmas → internal
   nodes, the source's displayed steps/FACTs → leaves), LOC estimates anchored on source line
   counts — ✓.
7. Every leaf is single-conclusion: the two-part conclusions `exists_separated_representation`,
   `exists_det_eq_mul`, `main_lemma`, `three_small_factors`, `sqrt_lt_floor`, `exists_degrees`,
   `exists_approximants`, `exists_m`, `exists_delta`, `exists_delta_bound`, `reduction` are
   shared-witness existentials (the components refer to the same witnesses `l, D, U, V`, `Q`, `δ`,
   `r`, `h, q`, `m`, `δ₀`, `α', κ'`) — the documented exception of `references/statement-splitting.md`;
   `three_small_factors` bundles three bounds on the same `B₁` that are always used together (one
   ticket; a split would triple the shared `log B₁` setup) and `sqrt_lt_floor` bundles the two sides
   of the floor estimate the source states in one line. No other leaf has a top-level `∧`.

REVIEW-PENDING leaves: none. The gate passes for the whole tree.

## Build log (skeleton verification)

Command: `.mathlib-quality/scripts/build-direct.sh` (all modules, dependency order), run after the last statement fix. Modules built: Roth.HasseDeriv, Roth.Box, Roth.Wronskian, Roth.Taylor, Roth.CoeffNorm, Roth.GenWronskian, Roth.Lattice, Roth.Index, Roth.Separation, Roth.Theta, Roth.MainLemma, Roth.Main.
Result: exit code 0, 0 errors, 182 `declaration uses 'sorry'` warnings (one per skeleton declaration), no other diagnostics. Per-file `sorry` counts (grep): `Box.lean` 12, `CoeffNorm.lean` 20, `GenWronskian.lean` 10, `HasseDeriv.lean` 20, `Index.lean` 17, `Lattice.lean` 4, `Main.lean` 15, `MainLemma.lean` 17, `Separation.lean` 19, `Taylor.lean` 15, `Theta.lean` 23, `Wronskian.lean` 10.
