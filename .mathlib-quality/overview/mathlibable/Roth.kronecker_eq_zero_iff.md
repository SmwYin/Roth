---
decl: Roth.kronecker_eq_zero_iff
file: Roth/GenWronskian.lean
line: 106
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Injectivity of the Kronecker substitution on the degree box is the standard folklore fact (PIT reduction) and mathlib has no analogue; it should ship as MvPolynomial.weightedSubst_eq_zero_iff for any weight injective on a set containing the support over a CommSemiring (plus an InjOn-on-restrictSupport form), all verified clean, and hk is superfluous (verified).
action: Ship MvPolynomial.weightedSubst_eq_zero_iff and injOn_weightedSubst_restrictSupport with the weightedSubst PR in Mathlib/Algebra/MvPolynomial/ (next to Expand.lean); locally drop hk from kronecker_eq_zero_iff (l.106) and update its sole caller linearIndependent_kronecker (l.123).
---

# Roth.kronecker_eq_zero_iff

## Inventory entry

### `theorem Roth.kronecker_eq_zero_iff`
- **Type**: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] {k : ℕ} (hk : 1 < k) {P : MvPolynomial σ K} (hP : ∀ j, degreeOf j P < k) : kronecker k P = 0 ↔ P = 0`
- **What**: A multivariate polynomial whose partial degrees are all `< k` vanishes iff its Kronecker substitution `x_j ↦ t^{k^{e j}}` vanishes, i.e. the substitution is injective on the degree box (kernel form).
- **How**: Backward direction is `map_zero`. Forward: show `P.support = ∅` via `MvPolynomial.support_eq_empty` and `Finset.eq_empty_iff_forall_notMem`; for `d ∈ support`, `Roth.coeff_kronecker` (with `monomial_le_degreeOf` putting `d` in the box) gives `P.coeff d = (kronecker k P).coeff _ = 0`, contradicting `mem_support_iff`.
- **Hypotheses**: `hk : 1 < k` (only passed to `coeff_kronecker`; superfluous, verified); `hP` (support in the box; essential, e.g. `x_2 - x_1^k` maps to 0); section variables `[Field K]` (unused, CommSemiring suffices) and `[Fintype σ]` (only for `equivFin` in the weight).
- **Uses from project**: `Roth.kronecker`, `Roth.coeff_kronecker`
- **Used by**: `Roth.linearIndependent_kronecker` (Roth/GenWronskian.lean:123). Through it, Lemma 1 (`exists_genWronskian_ne_zero` chain) in the same file. No uses outside Roth/GenWronskian.lean.
- **Visibility**: public
- **Lines**: 102-111, proof length 5 lines (107-111)
- **Notes**: `hk` can be dropped (verified as `Evidence.kronecker_eq_zero_iff'`); then `linearIndependent_kronecker` still needs `0 < k` only via `Nat.zero_lt_of_lt hk`.

## Junk check (Step 8)
- Used anywhere? Yes, once (`linearIndependent_kronecker`, l.123), on the critical path of Lemma 1.
- Wrapper of 1-2 mathlib calls? No: it wraps the project lemma `coeff_kronecker` plus a support argument (5 lines).
- Does mathlib have it? No. Loogle `MvPolynomial.aeval _ _ = 0 ↔ _ = 0` gives only tower lemmas (`aeval_algebraMap_eq_zero_iff`); nearest is `MvPolynomial.expand_injective` (`x_i ↦ x_i^n`, multivariate target) and the private `NoetherNormalization.sum_r_mul_ne`.
- Too specific? No: it is the injectivity statement the source's Lean note asks for.
- Well-chosen? Mostly; `hk`, `Field`, and the box/`equivFin` specificity should go in the general form.
- Conclusion: `KEEP`. Action: drop `hk` locally; upstream the general `weightedSubst` form.

## Mathlibable assessment (Step 9)

Pre-filter: not private, not `_aux`, docstring not internal/auxiliary, Step 8 KEEP, namespace-aware grep of `.lake/packages/mathlib/Mathlib/` finds no `kronecker_eq_zero_iff` / `weightedSubst`. Not a glue lemma (5-line proof using `coeff_kronecker`). Parent `Roth.kronecker` is `YES-but-generalise-first`, re-aimed at `MvPolynomial.weightedSubst w := aeval (fun j ↦ X ^ w j)`; exponent parent `Roth.kroneckerExp` is `NO-mathlib-has-it` (`Finsupp.weight`). Re-aim rule: mathlib has no `eq_zero_iff`/injectivity lemma for `aeval (X ^ w ·)`, so this is a full run aimed at the `weightedSubst` form.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; evidence file importing Roth.GenWronskian elaborates clean)
- decl `Roth.kronecker_eq_zero_iff`:  ✓ resolved at Roth/GenWronskian.lean:106
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Generalized Wronskians and Lemma 1, proved via Kronecker substitution reducing to the univariate Wronskian criterion.

### Statement (Phase 1)

`Roth.kronecker_eq_zero_iff` is a theorem stating the following:

Let `P ∈ K[x_j : j ∈ σ]` have degree `< k` in each variable, and let `e : σ ≃ Fin p` enumerate the variables. Then `P(t^{k^{e(j)}})_j = 0` in `K[t]` iff `P = 0`. Equivalently, the Kronecker substitution has trivial kernel on the space of polynomials with all partial degrees `< k`; this is because distinct exponent vectors in the box map to distinct powers of `t` (uniqueness of base-`k` digits).

Variables / typeclasses involved (Lean side):
- `K` with `[Field K]`: coefficient ring (only commutative-semiring structure used).
- `σ` with `[Fintype σ]`: variables, enumerated by `Fintype.equivFin`.
- `k : ℕ`: the base; `P : MvPolynomial σ K`.

Hypotheses (Lean side):
- `hk : 1 < k`: base ≥ 2 (superfluous).
- `hP : ∀ j, degreeOf j P < k`: support in the digit box.

Conclusion (math): `κ_k(P) = 0 ⇔ P = 0`.

Conclusion (Lean): `kronecker k P = 0 ↔ P = 0`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: API lemma (kernel form of injectivity) of the Kronecker substitution, not a structure or main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 5 substantive lines
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel                          | Query | Hit? | Standard form found | Notes |
|----|----------------------------------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form)        | Kronecker substitution injective polynomials degree less than k in each variable zero iff | yes | the substitution is injective on polynomials with all partial degrees `< M`; bijection `V_d → W_d` onto univariate polys of degree `< d^n` | Roche arXiv:1807.08289, arXiv:2411.17330, Sinhababu WACT 2023 slides |
|  2 | WebSearch (general form)         | weighted substitution x_i -> t^{w_i} injective on polynomials support distinct weighted degrees | partial | `x_i ↦ y^{w_i}` is injective on polynomials supported on a set `S` iff `w·` is injective on `S` (modular weights `(δ+1)^{i-1} mod p` in arXiv:2411.17330; `Z`-independent weights in arXiv:1305.0093 make it injective everywhere) | general form = injectivity of the weight on a set containing the support |
|  3 | WebSearch (named-after / aliases)| "Kronecker substitution" reduction multivariate to univariate polynomial identity testing nonzero | yes | folklore: `P ≡ 0 ⇔ P(X^{(d+1)^i}) ≡ 0` for individual degrees `≤ d` (the PIT reduction) | Agrawal–Saha–Saptharishi arXiv:1107.1434; Lipton–Vishnoi SODA'03; Agrawal–Biswas ECCC 1999/018; randomized KS arXiv:1712.05481 |
|  4 | ChatGPT MCP                      | (standard form / generality of the Kronecker zero-iff lemma) | n/a | — | `ask_chatgpt_math` MCP not configured in this session |
|  5 | Local references                 | grep `.mathlib-quality/references/clean.tex` for "individual exponent", "Kronecker" | yes | clean.tex l.266-271 Lean note: "prove injectivity only on the subspace where every individual exponent is less than `k`", with counterexample `x_2 - x_1^k` | exactly the box version |
|  6 | nLab                             | Kronecker substitution | no | — | nLab covers graded rings/weights, no page on this computer-algebra substitution |
|  7 | nCatLab (if categorical)         | n/a | n/a | — | not a categorical concept (concrete injectivity statement) |
|  8 | Stacks Project (if alg geom)     | n/a | n/a | — | not an algebraic-geometry concept; Stacks treats gradings only |
|  9 | MathOverflow / Math.StackExchange| Kronecker substitution injective (covered by WebSearch hits) | partial | same box statement as #1/#3 | folklore; no more general form beyond weighted/support-injective substitution |
| 10 | recent arXiv (last 5 years)      | derandomized factoring / iterative Kronecker substitution | yes | arXiv:2411.17330 (2024), arXiv:2403.12716 (2024) | modern variants need only injectivity of the weight on the support (or monomials of bounded degree), i.e. the general weighted form |

### Literature summary (Phase 3)

Concept identified as: Kronecker substitution, injectivity / zero-test on the individual-degree box (the PIT reduction).
Sources agree on the standard form: yes. For individual degrees `< D`, `P(z, z^D, …, z^{D^{n-1}}) = 0 ⇔ P = 0`.
Most general standard form: for any weight `w : σ → ℕ` and any set `S` on which `e ↦ w·e` is injective, the substitution `x_j ↦ t^{w_j}` is injective on polynomials supported in `S` (equivalently, its kernel meets `restrictSupport S` trivially).
Generality dimensions where the literature varies:
  - weights: `D^{i-1}` (classical), `(δ+1)^{i-1} mod p` (derandomized), random weights; most general is arbitrary `w` injective on the support set.
  - coefficient ring: fields / ℤ in computer algebra; any commutative (semi)ring works.
  - support set: full box, monomials of bounded total degree, or the support of a given sparse polynomial.
Disagreement with the literature: none in content; the Lean form carries a superfluous `1 < k` and `Field`, and is tied to the box and to `Fintype.equivFin`.

### Generality analysis — `Roth.kronecker_eq_zero_iff`

Literature-standard form (from Phase 3): for `weightedSubst w` over a commutative semiring and `S` with `Set.InjOn (Finsupp.weight w) S`, `↑P.support ⊆ S → (weightedSubst w P = 0 ↔ P = 0)`; over a ring, `Set.InjOn (weightedSubst w) (restrictSupport R S)`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hk : 1 < k` | base ≥ 2 | none | yes | only fed to `coeff_kronecker`, whose `hk` is superfluous; `Evidence.kronecker_eq_zero_iff'` compiles without it |
| 2 | `[Field K]` | field | commutative semiring | yes | `Evidence.weightedSubst_eq_zero_iff` compiles over `[CommSemiring R]` |
| 3 | `[Fintype σ]` | finite with `equivFin` | any σ, arbitrary weight | yes | only used to define the weight; absent from the general lemma |
| 4 | `hP` (box) | partial degrees `< k` | `↑P.support ⊆ S`, `InjOn (weight w) S` | yes | box is one choice of `S`; project lemma is a specialisation (evidence item 3) |
| 5 | (shape) kernel form | `= 0 ↔ = 0` | also `InjOn` on `restrictSupport R S` (CommRing) | yes | `Evidence.injOn_weightedSubst_restrictSupport` and the `restrictDegree` box example compile |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 5 (all verified in `evidence/Roth.kronecker_eq_zero_iff/generalise.lean`, `lean_diagnostic_messages` clean: no errors, no warnings)
Proposed restatement:

```lean
theorem MvPolynomial.weightedSubst_eq_zero_iff {R σ : Type*} [CommSemiring R] {w : σ → ℕ}
    {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) {P : MvPolynomial σ R}
    (hP : ↑P.support ⊆ S) : weightedSubst w P = 0 ↔ P = 0

theorem MvPolynomial.injOn_weightedSubst_restrictSupport {R σ : Type*} [CommRing R]
    {w : σ → ℕ} {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) :
    Set.InjOn (weightedSubst (R := R) w) (restrictSupport R S)
```

Local: `Roth.kronecker_eq_zero_iff` without `hk`.

Cost of restatement: CHEAP (mechanical; all compiled, the project form becomes a 3-line specialisation).

### Modern-idiom check (Phase 4c)

| #  | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|----|---|---|---|---|
|  1 | preambles → typeclasses? | no | no bundled structure hypotheses | — |
|  2 | sequences → filters? | no | no topology | — |
|  3 | construction → universal property? | no | statement about a fixed map | — |
|  4 | set-with-predicate → bundled substructure? | yes | the box hypothesis becomes membership in mathlib's `restrictSupport R S` / `restrictDegree σ R (k-1)` submodule; statement `Set.InjOn (weightedSubst w) (restrictSupport R S)` | composes with `restrictSupport`/`restrictDegree` API (`basisRestrictSupport`, `mem_restrictDegree`, `restrictTotalDegree_le_restrictDegree`) and linear-algebra (linear independence transport, as in `linearIndependent_kronecker`) |
|  5 | field-specific → (semi)ring? | yes | `[CommSemiring R]` (kernel form), `[CommRing R]` (InjOn form) | usable over ℤ / ℕ, and in NoetherNormalization's base ring |
|  6 | 1-categorical → higher? | no | not categorical | — |
|  7 | concrete index → general? | yes | arbitrary weight `w : σ → ℕ` via `Finsupp.weight`, not `k ^ equivFin σ j` | `Finsupp.weight` API, randomized/modular weights |
|  8 | concrete-via-abstract? | yes | proof uses `kronecker`/box only through `coeff_kronecker`, i.e. only that the weight is injective on a set containing the support | any weight with an InjOn certificate (`Behrend.map_injOn` for the box) |
|  9 | false-generalisation guard | no false generalisation | `weightedSubst (k ^ equivFin ·)` is `rfl`-equal to `Roth.kronecker` (evidence item 4) and the box InjOn follows from `Behrend.map_injOn`; evidence item 3 recovers the exact project statement (minus `hk`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the two `weightedSubst` lemmas above (kernel form + `InjOn` on `restrictSupport`).
  - Cost: CHEAP
  - Mathlib downstream this enables: `MvPolynomial.restrictSupport` / `restrictDegree` submodules (the box is `restrictDegree σ R (k-1)`, verified), `Finsupp.weight`, `Behrend.map_injOn` as the box certificate, and a replacement of the private `NoetherNormalization.sum_r_mul_ne` argument.
  - Real mathematical improvement: the injectivity is a property of the weight on the support set, not of base-`k` digits or of a field; one lemma serves classical, modular and random weights.

### Proof strategy — `Roth.kronecker_eq_zero_iff`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals/submodules | yes (mild) | InjOn on `restrictSupport` (submodule) derived from the kernel form by `sub_mem` | CHEAP (verified) |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `weightedSubst`, `weightedSubst_monomial`, `coeff_weightedSubst_weight` (parent/sibling PR) | CHEAP (verified) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: `ext d`; on the support use `coeff_weightedSubst_weight`, off it `notMem_support_iff` (5 lines), instead of the `support_eq_empty` detour.
  - Cost: CHEAP
  - Missing mathlib API (if any): `MvPolynomial.weightedSubst`, `coeff_weightedSubst_weight` (sibling PR)
  - Would refactoring make the proof strictly shorter / cleaner? yes; the project lemma becomes a term-mode 3-liner (evidence item 3).

### Phase 4.5
n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.kronecker_eq_zero_iff`

[A] Lean-Finder       "substituting X_i ↦ t^(k^i) into a multivariate polynomial with all partial degrees < k is injective"   no match; nearest `MvPolynomial.expand_injective`, `Polynomial.expand_injective` (different substitutions: `X_i ↦ X_i^n`)
[B] Loogle            `MvPolynomial.aeval _ _ = 0 ↔ _ = 0`   only `MvPolynomial.aeval_algebraMap_eq_zero_iff(_of_injective)` (tower lemmas, unrelated)
[C] LeanSearch        "Kronecker substitution of multivariate polynomial with bounded degrees is zero iff polynomial is zero"   no match (`MvPolynomial.ker_evalₗ`, `Polynomial.degreeLTEquiv_eq_zero_iff_eq_zero`: unrelated)
[D] Grep mathlib src  `kronecker_eq_zero`, `weightedSubst`, `Kronecker substitution`, `injOn_aeval`, `aeval_injOn`   no hits; only the private `NoetherNormalization.sum_r_mul_ne` (RingTheory/NoetherNormalization.lean:90), a degree-level base-`up` injectivity
[E] Name pattern      lean_local_search not used (ripgrep not on PATH in earlier runs); substituted by the namespace-aware grep in [D] for `kronecker_eq_zero_iff` / `weightedSubst_eq_zero_iff`: no hits

Searched for both:
  - the user's current form (box, base `k`)
  - the literature-standard form (arbitrary weight injective on the support; InjOn on `restrictSupport`)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Building blocks: `MvPolynomial.restrictSupport`, `restrictDegree`, `Finsupp.weight`, `Behrend.map_injOn`, `notMem_support_iff`.

### Normal-form check — `Roth.kronecker_eq_zero_iff`

Equivalent formalisms this statement could take: (a) kernel form `f P = 0 ↔ P = 0` under a support hypothesis; (b) `Set.InjOn f (restrictSupport R S)`; (c) `LinearMap.ker (f ∘ₗ (restrictSupport R S).subtype) = ⊥`.
Does mathlib already have a canonical form for this idea? Partially: mathlib states injectivity of substitutions as `Function.Injective` (`expand_injective`) plus `_inj`/`_eq_zero_iff` simp forms.
Proposed canonical form: (b) `InjOn` on `restrictSupport` as the structural statement, with (a) as the simp-usable `_eq_zero_iff` (the `= 0` / `P = 0` side on the RHS, as in `map_eq_zero_iff`).
RHS convention respected? yes

### Syntactic generality — `Roth.kronecker_eq_zero_iff`

Alternative restatements attempted (list):
- box with `degreeOf` bounds (current)
- `↑P.support ⊆ S` with `InjOn (weight w) S` (kernel form)
- `Set.InjOn (weightedSubst w) (restrictSupport R S)`
- box via `restrictDegree σ R (k-1)` (verified, needs a `k = 0` split)

Chosen restatement: kernel form with `↑P.support ⊆ S` (+ the InjOn corollary).
Justification: call sites (`linearIndependent_kronecker`) have a polynomial and degree bounds in hand; the support-subset hypothesis is supplied by one `monomial_le_degreeOf` lambda, while the `restrictDegree` box form forces `k - 1` arithmetic.

### Superfluous-argument audit — `Roth.kronecker_eq_zero_iff`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hk : 1 < k` | no | verified: `Evidence.kronecker_eq_zero_iff'` compiles without it |
| 2 | `[Field K]` | no | CommSemiring suffices (verified) |
| 3 | `[Fintype σ]` | only for the weight `k ^ equivFin j` | absent from the general lemma |
| 4 | `hP` | yes | without it `x_2 - x_1^k ↦ 0` |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (kernel form + `InjOn` on `restrictSupport`)
Syntactic generality: RESTATE (InjOn-weight / support-subset form)
Superfluous arguments: 2 to drop (`hk`, `Field`); `Fintype` also goes in the general form

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.kronecker_eq_zero_iff`

Internal use count: 0 outside the declaring file (1 inside it)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/GenWronskian.lean:123 (`linearIndependent_kronecker`, same file) | `refine (kronecker_eq_zero_iff hk fun j ↦ ?_).mp ?_` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.kronecker_eq_zero_iff`?):
  - (none in the project). In mathlib, `NoetherNormalization` re-derives the base-`up` injectivity privately (`sum_r_mul_ne`) at the level of degrees.

### Composition check (Phase 6)

Can `Roth.kronecker_eq_zero_iff` be derived from mathlib in ≤3 chained calls?

Attempt 1: `ext d` + coefficient comparison via `as_sum`, `aeval_monomial`, `Polynomial.coeff_C_mul_X_pow`, `Finset.sum_eq_single`, `Behrend.map_injOn`.
  - Mathlib decls used: `MvPolynomial.as_sum`, `MvPolynomial.aeval_monomial`, `Polynomial.finsetSum_coeff`, `Polynomial.coeff_C_mul_X_pow`, `Finset.sum_eq_single`, `Behrend.map_injOn`
  - Result: fails as a ≤3-call composition (needs the coefficient lemma, itself a 9-line proof, plus a support case split).
  - Notes: given the proposed `coeff_weightedSubst_weight` in mathlib, this becomes a 5-line proof, still not a chain.

Attempt 2: via an existing injectivity lemma (`MvPolynomial.expand_injective`, `Polynomial.expand_injective`, `restrictSupport` basis).
  - Result: fails; no mathlib injectivity lemma for `aeval (X ^ w ·)` into `R[t]`.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.kronecker_eq_zero_iff`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the Kronecker zero-test on the individual-degree box is the standard PIT reduction (arXiv:1107.1434, Lipton–Vishnoi, Roche survey; source clean.tex l.266-271); modern variants (arXiv:2411.17330) use arbitrary weights injective on the support.
- Generality analysis (Phase 4): STRICTLY NARROWER; `hk`, `Field`, `Fintype` and the box are removable, all verified clean.
- Mathlib search (Phase 5): not in mathlib in either form; only `expand_injective` (different substitution) and the private `NoetherNormalization.sum_r_mul_ne`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

This is the injectivity statement that makes the Kronecker substitution useful: on polynomials of individual degree `< k` it loses no information. Mathlib has no injectivity or zero-test lemma for `aeval (fun j ↦ X ^ w j)` into `R[t]`; the only analogous results are `MvPolynomial.expand_injective` / `Polynomial.expand_injective` for `X ↦ X^n`, and the private `sum_r_mul_ne` in `Mathlib/RingTheory/NoetherNormalization.lean`, which re-proves the base-`up` digit injectivity inline. The `weightedSubst` package proposed for the parent `Roth.kronecker` would be missing its headline lemma without this one.

The project form is narrower than needed: `1 < k` is superfluous (it only fed `coeff_kronecker`, whose `hk` is superfluous), `Field` and `Fintype` are unused, and the box is just one set on which the weight is injective. The verified general statements are the kernel form `weightedSubst_eq_zero_iff` for `Set.InjOn (Finsupp.weight w) S` and `↑P.support ⊆ S` over any commutative semiring, and the submodule form `Set.InjOn (weightedSubst w) (restrictSupport R S)` over a commutative ring, which with `S = {n | ∀ i, n i ≤ k-1}` is exactly injectivity on mathlib's `restrictDegree σ R (k-1)` (verified). The project lemma is a 3-line term-mode specialisation (evidence item 3).

Reason for the generalisation: LITERATURE-WEAKENING (arbitrary weights, injectivity on a set containing the support; `1 < k`, `Field` dropped) and MODERN-IDIOM (`Finsupp.weight` / `weightedSubst` instead of `kroneckerExp` / `equivFin`; injectivity stated on mathlib's `restrictSupport` / `restrictDegree` submodules).

Proposed restatement:
```lean
theorem MvPolynomial.weightedSubst_eq_zero_iff {R σ : Type*} [CommSemiring R] {w : σ → ℕ}
    {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) {P : MvPolynomial σ R}
    (hP : ↑P.support ⊆ S) : weightedSubst w P = 0 ↔ P = 0

theorem MvPolynomial.injOn_weightedSubst_restrictSupport {R σ : Type*} [CommRing R]
    {w : σ → ℕ} {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) :
    Set.InjOn (weightedSubst (R := R) w) (restrictSupport R S)
```
(Both proved in the evidence file; no `sorry` needed.)

Estimated cost of regeneralisation: CHEAP

Mathlib downstream this enables:
- The `weightedSubst` package (parent `Roth.kronecker`, sibling `Roth.coeff_kronecker`) gets its injectivity lemma, analogous to `Polynomial.expand_injective`.
- `restrictSupport` / `restrictDegree` gain an injective map to `R[t]`, which transports linear independence (as `linearIndependent_kronecker` does) and dimension counts.
- `Mathlib/RingTheory/NoetherNormalization.lean` could use the InjOn-weight lemmas instead of the private `sum_r_mul_ne`.
- Together with `Behrend.map_injOn` it gives the box version; with modular or random weights it gives the derandomized/randomized KS statements.

PR grouping: ship with `MvPolynomial.weightedSubst`, `weightedSubst_monomial` (from `Roth.kronecker_monomial`), `coeff_weightedSubst` / `coeff_weightedSubst_weight` (from `Roth.coeff_kronecker`) and a box-injectivity lemma (from `Roth.kroneckerExp_injOn`), as one PR in `Mathlib/Algebra/MvPolynomial/` next to `Expand.lean`.

Local refactor: drop `hk` from Roth/GenWronskian.lean:106 (after `coeff_kronecker`'s `hk` is dropped) and change the call at l.123 to `kronecker_eq_zero_iff fun j ↦ ?_`; `linearIndependent_kronecker` then needs `0 < k` only for `Finset.sup_lt_iff`.

Next action: run `/generalise Roth.kronecker_eq_zero_iff` aimed at the two `weightedSubst` lemmas above (both verified), apply the local `hk` drop, then include them in the `weightedSubst` PR.

## Next step

Drop `hk` from `Roth.kronecker_eq_zero_iff` (Roth/GenWronskian.lean:106) and its caller l.123, after the `coeff_kronecker` / `kroneckerExp_injOn` refactors. Upstream `MvPolynomial.weightedSubst_eq_zero_iff` and `injOn_weightedSubst_restrictSupport` (verified) with the `weightedSubst` package in `Mathlib/Algebra/MvPolynomial/`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.kronecker_eq_zero_iff/generalise.lean` (imports `Roth.GenWronskian`, `Mathlib.Combinatorics.Additive.AP.Three.Behrend`, `Mathlib.RingTheory.MvPolynomial.Basic`). `lean_diagnostic_messages`: clean (no errors, no warnings) after two fix iterations (missing import for `restrictSupport`; explicit sets for `Set.InjOn.mono`). Contents:
  1. `Evidence.weightedSubst_eq_zero_iff`: kernel form over `CommSemiring`, any σ, InjOn weight on `S ⊇ support`.
  2. `Evidence.injOn_weightedSubst_restrictSupport`: InjOn on `restrictSupport R S` over `CommRing`.
  3. `Evidence.kronecker_eq_zero_iff'`: the project statement without `hk`, as a specialisation of 1 (via `weight_injOn_box`, from `Behrend.map_injOn`).
  4. `example`: `Roth.kronecker k = weightedSubst (k ^ equivFin ·)` by `rfl`.
  5. `example`: `Set.InjOn (Roth.kronecker k) (restrictDegree σ K (k - 1))` for every `k`.
- Searches: WebSearch ×3 (literature table); Loogle `MvPolynomial.aeval _ _ = 0 ↔ _ = 0`; LeanSearch and Lean-Finder (no match); grep of mathlib for `kronecker_eq_zero`, `weightedSubst`, `Kronecker substitution`, `injOn_aeval`, `aeval_injOn` (no hits) and NoetherNormalization.lean; grep of `Roth/` for call sites; grep of `clean.tex` l.255-271.
- Unavailable channels: ChatGPT channel n/a (`ask_chatgpt_math` MCP not configured in this session).
