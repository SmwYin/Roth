---
decl: Roth.coeff_kronecker
file: Roth/GenWronskian.lean
line: 88
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The coefficient lemma is the core API fact of the Kronecker substitution and mathlib has no coefficient lemma for aeval (X ^ w ·); restated for weightedSubst w over CommSemiring (any σ, no Field, no Fintype) as an exact coefficient formula plus an InjOn-weight corollary, both verified clean, and the hypothesis 1 < k is superfluous (verified).
action: Ship MvPolynomial.coeff_weightedSubst (sum over support with weight = n) and coeff_weightedSubst_weight (InjOn weight) with the weightedSubst PR in Mathlib/Algebra/MvPolynomial/ (next to Expand.lean); locally drop hk from coeff_kronecker (l.88) and update its sole caller kronecker_eq_zero_iff (l.111).
---

# Roth.coeff_kronecker

## Inventory entry

### `theorem Roth.coeff_kronecker`
- **Type**: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] {k : ℕ} (hk : 1 < k) {P : MvPolynomial σ K} (hP : ∀ j, degreeOf j P < k) {d : σ →₀ ℕ} (hd : ∀ j, d j < k) : (kronecker k P).coeff (kroneckerExp k d) = P.coeff d`
- **What**: If every partial degree of `P` is `< k` and every entry of `d` is `< k`, then the coefficient of `t^{∑ d_j k^{e j}}` in the Kronecker substitution of `P` equals the coefficient of `X^d` in `P`.
- **How**: Expands `P` as a sum of monomials (`MvPolynomial.as_sum`), pushes through `map_sum` / `Polynomial.finsetSum_coeff`, rewrites each term with `Roth.kronecker_monomial` and `Polynomial.coeff_C_mul_X_pow`, then `Finset.sum_eq_single d`. Off-diagonal terms vanish by `Roth.kroneckerExp_injOn` plus `MvPolynomial.monomial_le_degreeOf`; the case `d ∉ support` uses `MvPolynomial.notMem_support_iff`.
- **Hypotheses**: `hk : 1 < k` (only passed on to `kroneckerExp_injOn`; superfluous, verified); `hP` (puts the support in the box `{e | ∀ j, e j < k}`); `hd` (puts `d` in the box); section variables `[Field K]` (not used, a CommSemiring is enough) and `[Fintype σ]` (only for `equivFin`).
- **Uses from project**: `Roth.kronecker`, `Roth.kroneckerExp`, `Roth.kronecker_monomial`, `Roth.kroneckerExp_injOn`
- **Used by**: `Roth.kronecker_eq_zero_iff` (Roth/GenWronskian.lean:111). Through that lemma it reaches `Roth.linearIndependent_kronecker` (l.121) and Lemma 1. No uses outside Roth/GenWronskian.lean.
- **Visibility**: public
- **Lines**: 84-97, proof length 9 lines (89-97)
- **Notes**: `hk` can be dropped. Once `kroneckerExp_injOn` is proved from `Behrend.map_injOn`, nothing in this proof needs `1 < k`. For `k ≤ 1` the box is a subsingleton, so the claim holds anyway. Verified: `Evidence.coeff_kronecker'`.

## Junk check (Step 8)
- Used anywhere? Yes, once directly (`kronecker_eq_zero_iff`, l.111). It is on the critical path of Lemma 1.
- Wrapper of 1-2 mathlib calls? No. It is a support-sum argument that combines base-`k` injectivity with the monomial lemma. Mathlib has no coefficient lemma for `aeval (fun j ↦ X ^ w j)`.
- Does mathlib have it? No. Loogle `Polynomial.coeff (MvPolynomial.aeval _ _) _` returns no hits. The nearest analogues are the univariate `Polynomial.coeff_expand_mul` and the private Noether-normalisation argument (`NoetherNormalization.sum_r_mul_ne`, which works with degrees rather than coefficients).
- Too specific? Not as a statement. It is the source's "comparing the coefficient" step and the natural API lemma of the substitution.
- Well-chosen? Mostly. `hk` and `Field` are superfluous, and the lemma should be stated against `Finsupp.weight` / an InjOn hypothesis.
- Conclusion: `KEEP`. Action: drop `hk` (verified), keep as the local specialisation, and upstream the general form with the `weightedSubst` package.

## Mathlibable assessment (Step 9)

Pre-filter: the name does not end in `_aux` and the docstring does not start with internal/auxiliary. Step 8 said KEEP. `Roth.coeff_kronecker` and `coeff_kronecker` are not in mathlib (grep). It is not a glue lemma (9-line proof). The parent `Roth.kronecker` is `YES-but-generalise-first`, re-aimed at `MvPolynomial.weightedSubst w := aeval (fun j ↦ X ^ w j)`. The exponent parent `Roth.kroneckerExp` is `NO-mathlib-has-it` (it is `Finsupp.weight`). Re-aim rule: `Finsupp.weight` / `weightedSubst` has no analogous coefficient lemma in mathlib, so this is a full run aimed at the `weightedSubst` + `Finsupp.weight` form.

### Baseline (Phase 0)
- lake build:               ✓ clean (the project was built per the brief; the evidence file importing Roth.GenWronskian elaborates clean)
- decl `Roth.coeff_kronecker`:  ✓ resolved at Roth/GenWronskian.lean:88
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Generalized Wronskians and Lemma 1 (a linearly independent family has a nonvanishing generalized Wronskian), proved via Kronecker substitution.

### Statement (Phase 1)

`Roth.coeff_kronecker` is a theorem stating the following:

Let `P ∈ K[x_j : j ∈ σ]` have degree `< k` in every variable. Let `h(t) = P(t^{k^{e(0)}}, …)` be its Kronecker substitution, where `e` enumerates σ. Then for every exponent vector `d` with all `d_j < k`, the coefficient of `t^{∑_j d_j k^{e(j)}}` in `h` equals the coefficient of `x^d` in `P`. The reason is that distinct monomials in the box map to distinct powers of `t` (uniqueness of base-`k` digits).

Variables / typeclasses involved (Lean side):
- `K` with `[Field K]`: coefficient ring (only commutative-semiring structure is used).
- `σ` with `[Fintype σ]`: variable set, enumerated by `Fintype.equivFin`.
- `k : ℕ`: the base.
- `P : MvPolynomial σ K`, `d : σ →₀ ℕ`.

Hypotheses (Lean side):
- `hk : 1 < k`: the base is at least 2 (superfluous).
- `hP : ∀ j, degreeOf j P < k`: the support lies in the digit box.
- `hd : ∀ j, d j < k`: `d` lies in the digit box.

Conclusion (math): `[t^{κ(d)}] h = [x^d] P`, where `κ(d) = ∑ d_j k^{e j}`.

Conclusion (Lean): `(kronecker k P).coeff (kroneckerExp k d) = P.coeff d`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an API lemma of the Kronecker substitution, not a new structure or a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 9 substantive lines
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel                          | Query | Hit? | Standard form found | Notes |
|----|----------------------------------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form)        | Kronecker substitution multivariate polynomial coefficient preserved degree less than k | yes | `g(z) = f(z, z^D, …, z^{D^{n-1}})`; for max partial degree `< D` it is a bijection of terms that preserves coefficients | Arnold–Roche arXiv:1401.6694; Roche survey arXiv:1807.08289 |
|  2 | WebSearch (general form)         | weighted substitution x_i -> t^{w_i} coefficient of t^n sum of coefficients of monomials of weighted degree n | partial | coefficient of `t^n` is the sum of the coefficients of the monomials of weighted degree `n` (cancellation possible); weighted-homogeneous characterisation `f(t^{a}z) = t^d f(z)` | mathlib WeightedHomogeneous docs, Wolfram forum; the general identity is the exact formula our general lemma states |
|  3 | WebSearch (named-after / aliases)| "Kronecker substitution" injective map polynomials bounded degree reduction to univariate | yes | "each monomial maps to a unique monomial", hence invertible on the degree box | arXiv:2411.17330, Sinhababu WACT 2023 slides |
|  4 | ChatGPT MCP                      | (standard form / generality of the Kronecker-substitution coefficient lemma) | n/a | — | `ask_chatgpt_math` MCP not configured in this session |
|  5 | Local references                 | grep `.mathlib-quality/references/clean.tex` for "Comparing the coefficient", "kronecker", "s_1 + k" | yes | clean.tex l.243-252: "Comparing the coefficient of `t^{s_1+ks_2+⋯}`" after the base-`k` uniqueness FACT; l.266 Lean note defining the substitution as an algebra hom | the source states exactly the box version |
|  6 | nLab                             | Kronecker substitution / weighted grading | no | — | nLab has graded rings and weighted gradings but no page on this computer-algebra substitution trick |
|  7 | nCatLab (if categorical)         | n/a | n/a | — | not a categorical concept (a concrete coefficient identity) |
|  8 | Stacks Project (if alg geom)     | n/a | n/a | — | not an algebraic-geometry concept. Stacks treats gradings, not this substitution |
|  9 | MathOverflow / Math.StackExchange| Kronecker substitution coefficients (covered by WebSearch hits) | partial | same box statement as #1 | the folklore treatment matches #1 and #3. No more general form beyond weighted substitution |
| 10 | recent arXiv (last 5 years)      | iterative / randomized Kronecker substitution | yes | arXiv:2403.12716 (iterative KS), arXiv:2411.17330 | modern variants pick weights `w` with few collisions, i.e. the general weighted form with injectivity only on a subset (the support), not on a full box |

### Literature summary (Phase 3)

Concept identified as: Kronecker substitution, the coefficient-preservation / term-bijection property.
Sources agree on the standard form: yes. For partial degrees `< D`, the map `x_i ↦ z^{D^{i-1}}` is a bijection on terms that preserves coefficients.
Most general standard form: for any weight `w : σ → ℕ`, `[t^n] P(t^{w}) = ∑_{e ∈ supp P, w·e = n} [x^e] P`. Consequently, if `w·` is injective on a set containing `supp P ∪ {d}`, then `[t^{w·d}] P(t^w) = [x^d] P`. Randomized and iterative KS (Arnold–Roche, 2024 work) rely on exactly this "injective on the support" form.
Generality dimensions where the literature varies:
  - weights: `D^{i-1}` (classical) up to arbitrary `w` with injectivity on the support (randomized KS); the most general is arbitrary `w`.
  - coefficient ring: fields / ℤ in computer algebra; any commutative (semi)ring works.
  - domain of injectivity: full box `[0,D)^n` up to any set containing the support.
Disagreement with the literature: none in content. The Lean form carries a superfluous `1 < k` and a superfluous `Field`, and is tied to the box and to `Fintype.equivFin`.

### Generality analysis — `Roth.coeff_kronecker`

Literature-standard form (from Phase 3): for `weightedSubst w` over a commutative semiring and `S` with `Finsupp.weight w` injective on `S`, `supp P ⊆ S` and `d ∈ S`, the coefficient at `weight w d` is `P.coeff d`. Underlying exact formula: `coeff n = ∑_{e ∈ supp P, weight w e = n} P.coeff e`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hk : 1 < k` | base ≥ 2 | none | yes | only feeds `kroneckerExp_injOn`, which holds without it (Behrend route). `Evidence.coeff_kronecker'` compiles without `hk` |
| 2 | `[Field K]` | field | commutative semiring | yes | the proof is a support sum. `Evidence.coeff_weightedSubst_weight` compiles over `[CommSemiring R]` |
| 3 | `[Fintype σ]` | finite, with `equivFin` | any σ, arbitrary weight `w` | yes | only needed to define the weight `k ^ equivFin j`. The general lemma has no `Fintype` |
| 4 | `hP`, `hd` (box) | partial degrees `< k`, entries `< k` | `supp P ⊆ S`, `d ∈ S`, `InjOn (weight w) S` | yes | the box is one instance of `S`. The general lemma takes an InjOn hypothesis and the project lemma is a specialisation (evidence item 4) |
| 5 | (implicit) injectivity | built in via box | none (exact sum formula) | yes | `Evidence.coeff_weightedSubst` gives the coefficient for all `w`, `n` with no hypothesis |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 5 (all verified compiling in `evidence/Roth.coeff_kronecker/generalise.lean`, `lean_diagnostic_messages` clean)
Proposed restatement:

```lean
theorem MvPolynomial.coeff_weightedSubst [CommSemiring R] (w : σ → ℕ) (P : MvPolynomial σ R) (n : ℕ) :
    (weightedSubst w P).coeff n = ∑ e ∈ P.support with Finsupp.weight w e = n, P.coeff e

theorem MvPolynomial.coeff_weightedSubst_weight [CommSemiring R] {w : σ → ℕ}
    {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) {P : MvPolynomial σ R}
    (hP : ↑P.support ⊆ S) {d : σ →₀ ℕ} (hd : d ∈ S) :
    (weightedSubst w P).coeff (Finsupp.weight w d) = P.coeff d
```

Local: `Roth.coeff_kronecker` without `hk`.

Cost of restatement: CHEAP (mechanical, all compiled).

### Modern-idiom check (Phase 4c)

| #  | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|----|---|---|---|---|
|  1 | preambles → typeclasses? | no | no bundled structure hypotheses | — |
|  2 | sequences → filters? | no | no topology | — |
|  3 | construction → universal property? | no | an identity about a fixed map | — |
|  4 | set-with-predicate → bundled substructure? | no | the box is a hypothesis set. Could use `Finset.pi`/`Set.pi`, but InjOn on an arbitrary `S` is more general | — |
|  5 | field-specific → (semi)ring? | yes | `[CommSemiring R]` | works over ℤ / ℕ (computer algebra, Noether normalisation over any field `k` where the private argument lives) |
|  6 | 1-categorical → higher? | no | not categorical | — |
|  7 | concrete index → general? | yes | arbitrary weight `w : σ → ℕ` with `Finsupp.weight`, instead of `k ^ equivFin σ j` | composes with `Finsupp.weight` API and `weightedHomogeneousComponent` (coeff `n` of `weightedSubst w P` is the evaluation at 1 of the weight-`n` component) |
|  8 | concrete-via-abstract? | yes | after `kronecker_monomial` the proof only uses that the exponent map is injective on a set containing the support. `kroneckerExp`'s concrete base-`k` form appears only through `kroneckerExp_injOn` | the abstract InjOn lemma serves any weight (randomized KS, Noether normalisation's `r ^ i` weights) |
|  9 | false-generalisation guard | no false generalisation | `weightedSubst (k ^ equivFin ·)` is definitionally `Roth.kronecker` (rfl, parent evidence) and `Finsupp.weight` equals `kroneckerExp` (proved). Evidence item 4 recovers the exact project statement | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the two `weightedSubst` lemmas above.
  - Cost: CHEAP
  - Mathlib downstream this enables: `Finsupp.weight` API (`weight_apply`, `map_add`), `Behrend.map_injOn` as the box-injectivity input, the Noether-normalisation substitution `T` (weights `r ^ i`), and the univariate analogue pattern `Polynomial.coeff_expand_mul`.
  - Real mathematical improvement: the exact coefficient formula holds for every weight with no hypothesis. The box is only one choice of a set on which the weight is injective.

### Proof strategy — `Roth.coeff_kronecker`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals/submodules | no | coefficient identity, element-level is natural | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `weightedSubst_monomial` and an InjOn-weight injectivity lemma (box version from `Behrend.map_injOn`). Both belong to the parent PR | CHEAP (verified) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: prove the exact sum formula `coeff_weightedSubst` once, then derive the InjOn corollary with `Finset.sum_eq_single` (verified, 6 + 7 lines).
  - Cost: CHEAP
  - Missing mathlib API (if any): `MvPolynomial.weightedSubst`, `weightedSubst_monomial` (parent package)
  - Would refactoring make the proof strictly shorter / cleaner? yes. The project lemma becomes a 3-line specialisation (evidence item 4).

### Phase 4.5
n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.coeff_kronecker`

[A] Lean-Finder       "Kronecker substitution x_i to t^(k^i) preserves coefficients of polynomials with partial degrees less than k"   no relevant hits (`Polynomial.ofFn_comp_toFn_eq_id_of_natDegree_lt`, `finSuccEquiv_coeff_coeff`, `Polynomial.contract`: unrelated)
[B] Loogle            `Polynomial.coeff (MvPolynomial.aeval _ _) _`   no hits
[C] LeanSearch        "coefficient of aeval of multivariate polynomial substituting powers of X equals coefficient"   no relevant hits (`coeff_eval_eq_eval_coeff`, `Polynomial.aeval_eq_sum_range`: unrelated)
[D] Grep mathlib src  `theorem coeff_aeval`, `coeff_expand`, `coeff_eval₂`, `Kronecker substitution`, `weightedSubst`, NoetherNormalization.lean   only the univariate/power-series `coeff_expand*` (Algebra/Polynomial/Expand.lean:91-116) and the private `NoetherNormalization.sum_r_mul_ne` (degree-based, l.90). `weightedHomogeneousComponent` / `coeff_weightedHomogeneousComponent` exist (RingTheory/MvPolynomial/WeightedHomogeneous.lean:381-395) but nothing links them to substitution
[E] Name pattern      lean_local_search `coeff_kronecker`: n/a (ripgrep not on PATH). Substituted by a namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `coeff_kronecker` / `coeff_weightedSubst`: no hits

Searched for both:
  - the user's current form (box, base `k`)
  - the literature-standard form (arbitrary weight, InjOn / exact sum formula)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Building blocks only: `MvPolynomial.as_sum`, `aeval_monomial`, `Polynomial.coeff_C_mul_X_pow`, `Finset.sum_eq_single`, `Finsupp.weight`, `Behrend.map_injOn`.

### Normal-form check — `Roth.coeff_kronecker`

Equivalent formalisms this statement could take: (a) box form with base `k`; (b) InjOn-weight form; (c) exact sum formula; (d) `coeff n (weightedSubst w P) = eval 1 (weightedHomogeneousComponent w n P)`.
Does mathlib already have a canonical form for this idea? no
Proposed canonical form: (c) as the basic `coeff_weightedSubst` lemma (the analogue of `Polynomial.coeff_expand`), with (b) as the corollary. The canonical side (`P.coeff`) is on the RHS.
RHS convention respected? yes

### Syntactic generality — `Roth.coeff_kronecker`

Alternative restatements attempted (list):
- box form with `degreeOf` bounds (current)
- InjOn on `S` with `↑P.support ⊆ S`, `d ∈ S`
- exact filtered sum

Chosen restatement: the exact sum (simp-friendly, no hypotheses) plus the InjOn corollary.
Justification: at call sites the InjOn form is supplied by any injectivity lemma (box via `Behrend.map_injOn`, support-only for randomized weights). The box form is a 3-line specialisation.

### Superfluous-argument audit — `Roth.coeff_kronecker`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hk : 1 < k` | no | verified: `Evidence.coeff_kronecker'` compiles without it |
| 2 | `[Field K]` | no | CommSemiring suffices (verified in general lemma). Locally it is inherited from `kronecker`'s section |
| 3 | `[Fintype σ]` | only for the weight `k ^ equivFin j` | absent from the general lemma |
| 4 | `hP` | yes | without it collisions occur |
| 5 | `hd` | yes | otherwise the injectivity set must contain `d` some other way |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (exact sum formula as the canonical lemma, InjOn corollary)
Syntactic generality: RESTATE (InjOn-weight form)
Superfluous arguments: 2 to drop (`hk`, `Field`). `Fintype` also goes in the general form

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.coeff_kronecker`

Internal use count: 0 outside the declaring file (1 inside it)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/GenWronskian.lean:111 (`kronecker_eq_zero_iff`, same file) | `simpa [h] using (coeff_kronecker hk hP fun j ↦ (monomial_le_degreeOf j hd).trans_lt (hP j)).symm` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.coeff_kronecker`?):
  - (none in the project). In mathlib, `NoetherNormalization` re-derives the same injectivity idea privately (`sum_r_mul_ne`, `T_leadingcoeff_isUnit`), at the level of degrees and leading coefficients.

### Composition check (Phase 6)

Can `Roth.coeff_kronecker` be derived from mathlib in ≤3 chained calls?

Attempt 1: `as_sum` + `map_sum` + `finsetSum_coeff` + `aeval_monomial` + `sum_eq_single` + base-`k` injectivity.
  - Mathlib decls used: `MvPolynomial.as_sum`, `Polynomial.finsetSum_coeff`, `MvPolynomial.aeval_monomial`, `Polynomial.coeff_C_mul_X_pow`, `Finset.sum_eq_single`, `Behrend.map_injOn`
  - Result: fails as a ≤3-call composition. It is a real 7-9-line proof (support sum with two side cases), not a chain.
  - Notes: with the proposed `coeff_weightedSubst` in mathlib, the project lemma would be a 3-line specialisation.

Attempt 2: via `weightedHomogeneousComponent` (`coeff_weightedHomogeneousComponent`, `aeval` of a weighted-homogeneous polynomial).
  - Result: fails. Mathlib has no lemma computing `aeval (X ^ w ·)` of a weighted-homogeneous component, so this route is longer.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.coeff_kronecker`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): KS coefficient preservation is standard (Arnold–Roche, Roche survey, source clean.tex l.252). The general form for arbitrary weights with injectivity on the support is what randomized and iterative KS use.
- Generality analysis (Phase 4): STRICTLY NARROWER. `hk`, `Field`, `Fintype` and the box are all removable, verified clean.
- Mathlib search (Phase 5): not in mathlib in either form. Only building blocks and the univariate analogue `Polynomial.coeff_expand`.
- Composition check (Phase 6): NOT-COMPOSABLE (real support-sum proof).

**Rationale:**

This lemma is the substantive API fact behind the Kronecker substitution: on the digit box, coefficients pass through unchanged. It is the step the source calls "comparing the coefficient". Mathlib has no coefficient lemma for `aeval (fun j ↦ X ^ w j)` at all, so the parent `Roth.kronecker` → `MvPolynomial.weightedSubst` package is incomplete without it. It also has the same shape as the existing `Polynomial.coeff_expand` / `coeff_expand_mul` for the univariate substitution `X ↦ X^p`.

The project form is narrower than it needs to be. The hypothesis `1 < k` is superfluous: `Evidence.coeff_kronecker'` compiles without it once `kroneckerExp_injOn` is proved from `Behrend.map_injOn`, which confirms the `kroneckerExp_injOn` report. `Field` and `Fintype` are also unused. The right mathlib statements, both compiled, are (i) the exact formula `coeff n (weightedSubst w P) = ∑_{e ∈ supp P, weight w e = n} P.coeff e` over any commutative semiring, and (ii) its corollary for `Set.InjOn (Finsupp.weight w) S` with `supp P ⊆ S ∋ d`. The project lemma follows from (ii) in 3 lines, using the box injectivity.

Reason for the generalisation: LITERATURE-WEAKENING (arbitrary weights, injectivity on a set containing the support; `1 < k` and the field hypothesis dropped) and MODERN-IDIOM (`Finsupp.weight` / `weightedSubst` in place of `kroneckerExp` / `Fintype.equivFin`).

Proposed restatement:
```lean
theorem MvPolynomial.coeff_weightedSubst {R σ : Type*} [CommSemiring R] (w : σ → ℕ)
    (P : MvPolynomial σ R) (n : ℕ) :
    (weightedSubst w P).coeff n = ∑ e ∈ P.support with Finsupp.weight w e = n, P.coeff e

theorem MvPolynomial.coeff_weightedSubst_weight {R σ : Type*} [CommSemiring R] {w : σ → ℕ}
    {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) {P : MvPolynomial σ R}
    (hP : ↑P.support ⊆ S) {d : σ →₀ ℕ} (hd : d ∈ S) :
    (weightedSubst w P).coeff (Finsupp.weight w d) = P.coeff d
```
(Both already proved in the evidence file; no `sorry` needed.)

Estimated cost of regeneralisation: CHEAP

Mathlib downstream this enables:
- The `weightedSubst` package (parent `Roth.kronecker`) gets its coefficient lemma, analogous to `Polynomial.coeff_expand`.
- `Mathlib/RingTheory/NoetherNormalization.lean` could replace the private `sum_r_mul_ne` + leading-coefficient argument with `coeff_weightedSubst_weight` and a weight-injectivity lemma.
- Combined with `Behrend.map_injOn` it gives the box version. Combined with any support-injective weight it gives randomized KS.
- The eq_zero_iff lemma (`Roth.kronecker_eq_zero_iff`) becomes a corollary for arbitrary InjOn weights.

PR grouping: ship together with `MvPolynomial.weightedSubst`, `weightedSubst_monomial` (from `Roth.kronecker_monomial`) and the eq_zero_iff port of `Roth.kronecker_eq_zero_iff`, as one PR in `Mathlib/Algebra/MvPolynomial/` next to `Expand.lean`.

Local refactor: in Roth/GenWronskian.lean:88 drop `hk`, and update the call site l.111 (`coeff_kronecker hk hP …` becomes `coeff_kronecker hP …`). This depends on the `kroneckerExp_injOn` refactor (l.69-82, Behrend route, no `hk`). Then check `kronecker_eq_zero_iff` / `linearIndependent_kronecker` for `hk` (only `Nat.zero_lt_of_lt hk` in l.121 remains, which needs `0 < k`).

Next action: run `/generalise Roth.coeff_kronecker` aimed at the two `weightedSubst` lemmas above (both verified), apply the local `hk` drop, then include them in the `weightedSubst` PR.

## Next step

Drop `hk` from `Roth.coeff_kronecker` (Roth/GenWronskian.lean:88) and its caller l.111, after the `kroneckerExp_injOn` Behrend refactor. Upstream `MvPolynomial.coeff_weightedSubst` and `coeff_weightedSubst_weight` (verified) together with the `weightedSubst` package in `Mathlib/Algebra/MvPolynomial/`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.coeff_kronecker/generalise.lean` (imports `Roth.GenWronskian`, `Mathlib.Combinatorics.Additive.AP.Three.Behrend`). `lean_diagnostic_messages`: clean (no errors, no warnings). Contents:
  1. `Evidence.coeff_weightedSubst`: the exact sum formula over `CommSemiring`, any σ.
  2. `Evidence.coeff_weightedSubst_weight`: the InjOn corollary.
  3. `Evidence.coeff_kronecker'`: the project statement without `hk`, with the original proof otherwise unchanged (uses the hk-free `kroneckerExp_injOn'` via `Behrend.map_injOn`).
  4. an `example` deriving the project statement (without `hk`) from item 2 in 3 lines, via `kroneckerExp_eq_weight`.
- Searches:
  - WebSearch ×3 (see the literature table).
  - Loogle `Polynomial.coeff (MvPolynomial.aeval _ _) _`: no hits.
  - LeanSearch and Lean-Finder: no relevant hits.
  - Grep of mathlib for `coeff_aeval` / `coeff_expand` / `coeff_eval₂` / `Kronecker substitution` / `weightedHomogeneousComponent`, and of NoetherNormalization.lean.
  - Grep of the project for call sites.
  - Grep of `clean.tex`, l.243-266.
- Unavailable channels:
  - `lean_local_search`: n/a, ripgrep is not on PATH (replaced by grep).
  - ChatGPT channel: n/a, the `ask_chatgpt_math` MCP is not configured in this session.
