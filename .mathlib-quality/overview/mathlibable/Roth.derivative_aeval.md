---
decl: Roth.derivative_aeval
file: Roth/GenWronskian.lean
line: 133
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The multivariate algebraic chain rule D(P(f)) = sum_i (d_i P)(f) D(f_i) is absent from mathlib (only the univariate Derivation.map_aeval exists); the project form is the special case D = Polynomial.derivative over a field, and the general derivation form over any commutative semiring compiles with the same three-case induction (evidence verified).
action: Upstream `Derivation.map_mvPolynomial_aeval` (any D : Derivation R A M, f : σ → A, Fintype σ, CommSemiring R) next to `Derivation.map_aeval` or in Mathlib/Algebra/MvPolynomial/PDeriv.lean, with the `Polynomial.derivative` form as a one-line corollary via `Polynomial.derivative'`; locally weaken `[Field K]` to `[CommSemiring R]` optional, keep the one caller Roth/GenWronskian.lean:159 unchanged.
---

# Roth.derivative_aeval

## Inventory entry

### `theorem Roth.derivative_aeval`
- **Type**: `∀ {K : Type*} [Field K] {σ : Type*} [Fintype σ] (γ : σ → Polynomial K) (P : MvPolynomial σ K), Polynomial.derivative (aeval γ P) = ∑ j, Polynomial.derivative (γ j) * aeval γ (pderiv j P)`
- **What**: The algebraic chain rule: for `γ = (γ_j)` univariate polynomials and `P` multivariate, `d/dt P(γ(t)) = ∑_j γ_j'(t) (∂_j P)(γ(t))`.
- **How**: `MvPolynomial.induction_on`: constants by `simp`; additivity by `simp [Finset.sum_add_distrib, mul_add]`; the `mul_X` step by `simp` with `Derivation.leibniz`/`pderiv_X` (simp lemmas), `Pi.single_apply`, `apply_ite (aeval γ)`, `Finset.mul_sum` and ring-normalising rewrites.
- **Hypotheses**: none beyond section variables `[Field K]`, `[Fintype σ]`.
- **Uses from project**: `[]`
- **Used by**: Roth/GenWronskian.lean:159 (`derivative_kronHasse_aux`, private, in a `simp [kronHasse, kronecker, derivative_aeval, pderiv_hasseDeriv, ...]` set). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 129–142 (docstring 129–132, statement 133–135), proof length 7 lines
- **Notes**: Implements the FACT in §2 proof of Lemma 1 of the source paper (`.mathlib-quality/references/clean.tex` l.285–290). `[Field K]` is a section variable; the proof only needs `CommSemiring` (evidence item 3).

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/GenWronskian.lean:159 (derivative of the Kronecker substitution of a Hasse derivative).
- Wrapper of 1–2 mathlib calls? No: mathlib has only the univariate chain rules (`Derivation.map_aeval`, `Derivation.comp_aeval_eq`, `Polynomial.derivative_comp`, `Polynomial.derivative_eval₂_C`); the multivariate one needs an induction.
- Does mathlib have it? No (Phase 5 below).
- Too specific / inline? No: it is a standard named identity (chain rule), stated in the paper, and the natural API lemma; inlining a 7-line induction into a `simp` call is worse.
- Well-chosen? Yes as a local lemma; for upstreaming it should be stated for an arbitrary derivation.
- Conclusion: `KEEP` — action: keep locally (optionally weaken `Field` to `CommSemiring`); upstream the general derivation form.

## Mathlibable assessment (Step 9)

Not private, no pre-filter fires (name does not end `_aux`; docstring not internal/auxiliary; Step 8 = KEEP; no `Roth.derivative_aeval` / `derivative_aeval` in mathlib per grep). Not a glue lemma (real induction proof). Full workflow run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.GenWronskian` elaborates with no diagnostics)
- decl `Roth.derivative_aeval`: resolved at Roth/GenWronskian.lean:133
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Generalised Wronskians of multivariate polynomials via Kronecker substitution and Hasse derivatives (§2 Lemma 1 of the Roth source).

### Statement (Phase 1)

`Roth.derivative_aeval` is a theorem stating the following:

Let `K` be a field, `σ` a finite set of variables, `γ = (γ_j)_{j∈σ}` a family of univariate polynomials in `K[t]` and `P ∈ K[x_σ]`. Then the formal derivative of the substitution `P(γ(t))` is `∑_j γ_j'(t) · (∂P/∂x_j)(γ(t))`. This is the formal (algebraic) multivariate chain rule.

Variables / typeclasses involved (Lean side):
- `K : Type*`, `[Field K]` — coefficients.
- `σ : Type*`, `[Fintype σ]` — variables (finite so the sum is a `Finset.univ` sum).
- `γ : σ → Polynomial K` — the substituted polynomials.
- `P : MvPolynomial σ K` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `(P ∘ γ)' = ∑_j γ_j' · (∂_j P) ∘ γ`.

Conclusion (Lean): `Polynomial.derivative (aeval γ P) = ∑ j, Polynomial.derivative (γ j) * aeval γ (pderiv j P)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: helper lemma (one step of the proof of §2 Lemma 1), not a main result, not a new structure, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 7
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | formal chain rule polynomial substitution d/dt f(g_1(t),...,g_n(t)) = sum partial_i f(g(t)) g_i'(t) formal derivative commutative ring | partial | `D(P(f_1..f_n)) = ∑ (∂P/∂x_k)(f) D(f_k)` for a derivation `D` on a differential ring | arXiv 1311.5067 (multivariate Stirling polynomials) states it for derivations; nLab "chain rule" |
| 2 | WebSearch (general form) | derivation D(f(a_1,...,a_n)) = sum (∂f/∂x_i)(a) D(a_i) chain rule derivations polynomial algebra | yes | for any `R`-derivation `D : A → M`, `A` commutative `R`-algebra: `D(f(a)) = ∑ (∂_i f)(a) D(a_i)`; univariate form `d(f(a)) = f'(a) da` is mathlib's `Derivation.comp_aeval_eq` | arXiv 1611.01940 (chain rule for higher derivations, char-free); proof = Leibniz on monomials |
| 3 | WebSearch (named-after / aliases) | Kähler differentials polynomial ring df = sum ∂f/∂x_i dx_i universal derivation | yes | `Ω_{R[x]/R}` free on `dx_i`, `df = ∑ ∂_i f dx_i`; any derivation factors through `d` | Wikipedia "Kähler differential"; Kedlaya math203b notes; this is the universal form of the chain rule (compose with `aeval f`) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `FACT` / `chain rule` | yes | l.285–290: `d/dt h_ν(t) = ∑_j k^{j-1} t^{k^{j-1}-1} ∂φ_ν/∂x_j (γ(t))`, "This is the algebraic chain rule for polynomial substitution" | the paper uses the specific Kronecker curve `γ(t) = (t, t^k, ...)`; the project lemma is already the general-`γ` form |
| 6 | nLab | chain rule | yes | chain rule in synthetic/algebraic settings; derivations compose with algebra maps | abstract form = functoriality of `Ω` |
| 7 | nCatLab | (same nLab pages) | partial | no categorical content beyond functoriality of Kähler differentials | not needed for a polynomial identity |
| 8 | Stacks Project | Kähler differentials of polynomial algebras (Tag 00RX area, "Differentials") | yes | `Ω_{R[x_i]/R}` free on `dx_i` (Lemma 10.131.x); chain rule implicit via universal property | gives the universal statement; no explicit pointwise lemma |
| 9 | MathOverflow / Math.SE | (results of #1–#3) | partial | folklore: proved by Leibniz rule on monomials | no dedicated thread needed |
| 10 | recent arXiv (last 5 years) | (results of #1–#2) | partial | arXiv 2205.10722 (noncommutative partial derivative, 2022) treats the noncommutative analogue; commutative form taken as standard | confirms commutative form is folklore |

### Literature summary (Phase 3)

Concept identified as: the (formal) multivariate chain rule for derivations — for an `R`-derivation `D : A → M` and `f : σ → A`, `D(P(f)) = ∑_i (∂_i P)(f) · D(f_i)`; equivalently, `d(aeval f P) = ∑ aeval f (∂_i P) d(f_i)` in Kähler differentials.
Sources agree on the standard form: yes.
Most general standard form: `R` a commutative (semi)ring, `A` a commutative `R`-algebra, `M` an `A`-module, `D` any `R`-derivation `A → M`, `σ` finite (or sum over `vars P`).
Generality dimensions where the literature varies:
  - derivation: `d/dt` on `K[t]` (paper) → any `R`-derivation into any module (most general).
  - coefficients: field / char 0 (paper) → any commutative semiring.
Disagreement with the literature: the project states the special case `D = d/dt`, `A = K[t]`, `K` a field.

### Generality analysis — `Roth.derivative_aeval`

Literature-standard form (from Phase 3): `D (aeval f P) = ∑ i, aeval f (pderiv i P) • D (f i)` for any `D : Derivation R A M`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | commutative semiring | yes | proof uses no division/subtraction; verified (evidence item 3) |
| 2 | target `Polynomial K` with `Polynomial.derivative` | specific derivation `d/dt` | any `D : Derivation R A M` | yes | same induction proves it for any derivation; verified (evidence item 1), project form is a one-line corollary (item 2) |
| 3 | `[Fintype σ]` | finite variables | finite, or sum over `P.vars` | no (kept) | needed for `∑ j` over `univ`; a `vars`-indexed variant is possible but not standard for mathlib's `pderiv` lemmas (cf. Euler identity uses `Fintype`) |
| 4 | `γ`, `P` | arbitrary | arbitrary | n/a | no hypotheses |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 2 (field → commutative semiring; `d/dt` → arbitrary derivation), both verified to compile.
Proposed restatement:

```lean
theorem Derivation.map_mvPolynomial_aeval {σ R A M : Type*} [Fintype σ] [CommSemiring R]
    [CommSemiring A] [Algebra R A] [AddCommMonoid M] [Module A M] [Module R M]
    [IsScalarTower R A M] (D : Derivation R A M) (f : σ → A) (P : MvPolynomial σ R) :
    D (aeval f P) = ∑ i, aeval f (pderiv i P) • D (f i)
```

with the project lemma as `by simpa [mul_comm] using Polynomial.derivative'.map_mvPolynomial_aeval γ P` (spelled `Derivation.map_mvPolynomial_aeval Polynomial.derivative' γ P` in the evidence).

Cost of restatement: CHEAP — mechanical; the same three-case induction closes it (evidence item 1, no diagnostics).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | partial | could be phrased via `KaehlerDifferential.mvPolynomialBasis_repr_D` + `Derivation.liftKaehlerDifferential` | heavier than the direct induction; the pointwise derivation form is what users rewrite with |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | yes | `[CommSemiring R]` | usable over `ℤ`, `ℕ`, polynomial rings, etc. |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete object to general? | yes | `Polynomial.derivative` → arbitrary `D : Derivation R A M` | multivariate analogue of `Derivation.map_aeval`; applies to `pderiv`, `PowerSeries.derivative`, differential algebras (`Differential`) |
| 8 | concrete-via-abstract? | yes | proof uses only Leibniz/`map_algebraMap` of `Polynomial.derivative`, i.e. that it is a derivation | general theorem with the `d/dt` case as corollary (verified) |
| 9 | false-generalisation guard | no false generalisation | the general statement specialises exactly to the project statement (evidence item 2) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Derivation.map_mvPolynomial_aeval` as above (name parallel to `Derivation.map_aeval`).
  - Cost: CHEAP
  - Mathlib downstream this enables: completes the `Derivation.map_aeval` / `Derivation.comp_aeval_eq` API to several variables; gives the chain rule for `MvPolynomial.pderiv` of a substitution (`D = pderiv k`), for `Polynomial.derivative` (this lemma), for `PowerSeries.derivative`, and for `Differential` algebras (`Differential.deriv_aeval_eq` is the univariate analogue).
  - Real mathematical improvement: the statement becomes the standard derivation chain rule rather than a statement about one specific derivation.

### Proof strategy — `Roth.derivative_aeval`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ? | no | — | — |
| 2 | Algebra elementwise vs point-free? | partial | `MvPolynomial.derivation_ext`: both sides as derivations agreeing on `X i` — but RHS needs an `MvPolynomial`-module structure on `M` via `aeval f`, which is awkward | MODERATE, not shorter |
| 3 | Analysis sequences? | no | — | — |
| 4 | Category-theory construction? | no | — | — |
| 5 | Missing mathlib helpers? | yes | the general chain rule itself (`Derivation.map_mvPolynomial_aeval`) is the missing helper | file as the upstream PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (induction on `MvPolynomial` with simp, matching `pderiv_rename`, `aeval_sumElim_pderiv_inl` in Mathlib/Algebra/MvPolynomial/PDeriv.lean). Refactor only in the sense of generalising the statement.

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.derivative_aeval`

[A] Lean-Finder       "multivariable chain rule: derivative of a multivariate polynomial evaluated at univariate polynomials equals sum of partial derivatives times derivatives"   no hit (returns univariate `Polynomial.derivative_eval₂_C`, `Polynomial.derivative_comp`, `Differential.deriv_aeval_eq`, `MvPolynomial.aeval_sumElim_pderiv_inl`)
[B] Loogle            `Derivation, MvPolynomial.aeval, MvPolynomial.pderiv`; `Polynomial.derivative (MvPolynomial.aeval _ _)`   no hit (only `aeval_sumElim_pderiv_inl`, cotangent-space basis lemmas); second query empty
[C] LeanSearch        "chain rule derivation applied to MvPolynomial.aeval equals sum of aeval of partial derivatives times derivation of variables"   no hit (univariate `Derivation.map_aeval`, `Derivation.comp_aeval_eq`, `Derivation.compAEval_eq`, `MvPolynomial.mkDerivation`)
[D] Grep mathlib src  `derivative_aeval`, `map_mvPolynomial_aeval`, `D (aeval`, `d (aeval`, `pderiv` near `aeval`/`∑` in all files mentioning `pderiv`   no hit for a multivariate chain rule; only univariate `Derivation.map_aeval` (RingTheory/Derivation/Basic.lean:151), `Derivation.comp_aeval_eq` (Algebra/Polynomial/Derivation.lean:148), `Derivation.apply_aeval_eq` (RingTheory/Derivation/MapCoeffs.lean:82); Kähler `mvPolynomialBasis_repr_D` (RingTheory/Kaehler/Polynomial.lean:69) gives `D x = ∑ pderiv i x • D X_i` only in `Ω[MvPolynomial σ R⁄R]`
[E] Name pattern      `lean_local_search`/grep `Derivation.map_mvPolynomial_aeval`, `MvPolynomial.derivative_aeval`   no hits

Searched for both:
  - the user's current form (`Polynomial.derivative (aeval γ P)`)
  - the literature-standard form (arbitrary derivation applied to `MvPolynomial.aeval`)

Concluded: found building blocks (`Derivation.leibniz`, `MvPolynomial.pderiv_X`, `MvPolynomial.induction_on`, Kähler basis `mvPolynomialBasis_repr_D`); not in mathlib (all 5 methods exhausted, plus the literature-standard form).

### Normal-form check — `Roth.derivative_aeval`

Equivalent formalisms: (a) pointwise `D (aeval f P) = ∑ aeval f (pderiv i P) • D (f i)`; (b) Kähler: `(KaehlerDifferential.map ...) (D P) = ∑ ...`; (c) operator `D.toLinearMap ∘ₗ aeval f = ∑ ...`.
Does mathlib have a canonical form? yes for one variable: `Derivation.map_aeval : D (aeval x P) = aeval x (derivative P) • D x` (simp). Our proposed form (a) matches it, with the evaluated-partial factor on the left of `•`.
RHS convention respected? yes (expanded form on the RHS, like `Derivation.map_aeval`). The project lemma writes the factors as `derivative (γ j) * aeval γ (pderiv j P)` (reversed), harmless locally.

### Syntactic generality — `Roth.derivative_aeval`

Alternative restatements attempted:
- pointwise derivation form with `•` (verified, item 1)
- `Polynomial.derivative` form, project factor order (verified, items 2–4)
- sum over `P.vars` without `Fintype σ` (not attempted; mathlib `pderiv` sum lemmas such as `IsHomogeneous.sum_X_mul_pderiv` use `Fintype`)

Chosen restatement: pointwise derivation form with `Fintype σ`.
Justification: rewrites directly, parallels `Derivation.map_aeval`, and specialises to the project form by `simpa [mul_comm]`.

### Superfluous-argument audit — `Roth.derivative_aeval`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `CommSemiring` suffices (evidence item 3) |
| 2 | `[Fintype σ]` | yes | indexes the `Finset.univ` sum |
| 3 | `γ`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (parallel to `Derivation.map_aeval`) for the general form
Syntactic generality: RESTATE (to arbitrary derivation)
Superfluous arguments: 1 to drop (`Field` → `CommSemiring`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.derivative_aeval`

Internal use count: 0 outside the declaring file; 1 inside it
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/GenWronskian.lean:159 | `simp [kronHasse, kronecker, derivative_aeval, pderiv_hasseDeriv, map_smul, ...]` in private `derivative_kronHasse_aux` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.derivative_aeval`?):
  - (none) — grep of `Roth/` for `Polynomial.derivative (aeval` / `pderiv` near `aeval` finds only this lemma and its caller.

### Composition check (Phase 6)

Can `Roth.derivative_aeval` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Derivation.map_aeval` iterated — univariate only; does not apply to `MvPolynomial.aeval`.
  - Result: fails.

Attempt 2: Kähler route — `KaehlerDifferential.mvPolynomialBasis_repr_D` gives `D_univ P = ∑ pderiv i P • D_univ (X i)` in `Ω[MvPolynomial σ R⁄R]`; push forward along `Polynomial.derivative' ∘ aeval γ` via `Derivation.liftKaehlerDifferential` and a compatibility of `aeval γ` with module structures.
  - Mathlib decls used: `KaehlerDifferential.mvPolynomialBasis_repr_D`, `Basis.sum_repr`, `Derivation.liftKaehlerDifferential_comp_D`, plus `Derivation.compAlgebraMap`-type glue
  - Result: partial — needs several `have`s and module-structure transport; a real proof, not a composition.

Attempt 3: `MvPolynomial.derivation_ext` — RHS is not a bundled derivation `MvPolynomial σ R → M` without equipping `M` with an `MvPolynomial σ R`-module structure through `aeval γ`.
  - Result: fails as a ≤3-call composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.derivative_aeval`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the standard form is the chain rule for an arbitrary `R`-derivation, `D(P(f)) = ∑ (∂_i P)(f) D(f_i)` (arXiv 1311.5067, 1611.01940; Kähler-differential texts; source paper l.285–290 for the `d/dt` case).
- Generality analysis (Phase 4): STRICTLY NARROWER — `Field` → `CommSemiring` and `Polynomial.derivative` → arbitrary `Derivation R A M`, both verified to compile.
- Mathlib search (Phase 5): not in mathlib; only the univariate `Derivation.map_aeval` / `Derivation.comp_aeval_eq` and Kähler-basis facts.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Mathlib has the univariate chain rule for derivations (`Derivation.map_aeval`, RingTheory/Derivation/Basic.lean:151; `Derivation.comp_aeval_eq`, Algebra/Polynomial/Derivation.lean:148) and the univariate polynomial chain rules (`Polynomial.derivative_comp`, `Polynomial.derivative_eval₂_C`), but no multivariate version: there is no lemma computing `D (MvPolynomial.aeval f P)` in terms of `MvPolynomial.pderiv`. The only multivariate information is inside Kähler differentials (`KaehlerDifferential.mvPolynomialBasis_repr_D`), which is not usable as a rewrite for a concrete derivation. This is a concrete API gap: the natural multivariate companion of `Derivation.map_aeval`.

The project lemma is the special case `D = Polynomial.derivative`, `A = K[t]`, `K` a field. The same three-case induction (`C`, `add`, `mul_X`) proves the statement for any derivation `D : Derivation R A M` over any commutative semiring (evidence item 1, clean), and the project statement follows in one line via `Polynomial.derivative'` (item 2). So the generalisation is a single mechanical edit, and it is the form the literature states.

Reason for the generalisation:
  - LITERATURE-WEAKENING: field → commutative semiring; specific derivation `d/dt` → arbitrary derivation.
  - MODERN-IDIOM: parallels mathlib's `Derivation.map_aeval` API.

Proposed restatement:
```lean
theorem Derivation.map_mvPolynomial_aeval {σ R A M : Type*} [Fintype σ] [CommSemiring R]
    [CommSemiring A] [Algebra R A] [AddCommMonoid M] [Module A M] [Module R M]
    [IsScalarTower R A M] (D : Derivation R A M) (f : σ → A) (P : MvPolynomial σ R) :
    D (aeval f P) = ∑ i, aeval f (pderiv i P) • D (f i) := by
  classical
  induction P using MvPolynomial.induction_on with
  | C a => simp
  | add p q hp hq => simp [hp, hq, Finset.sum_add_distrib, add_smul]
  | mul_X p j hp =>
    simp [hp, Finset.sum_add_distrib, add_smul, Finset.smul_sum, mul_smul, Pi.single_apply,
      apply_ite (aeval f), ite_smul]

theorem Polynomial.derivative_mvPolynomial_aeval {σ R : Type*} [Fintype σ] [CommSemiring R]
    (γ : σ → R[X]) (P : MvPolynomial σ R) :
    derivative (MvPolynomial.aeval γ P) = ∑ j, derivative (γ j) * MvPolynomial.aeval γ (pderiv j P) := by
  simpa [mul_comm] using Derivation.map_mvPolynomial_aeval Polynomial.derivative' γ P
```
(both verified in the evidence file).

Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
  - the multivariate analogue of `Derivation.map_aeval`; chain rule for `MvPolynomial.pderiv k` applied to a substitution, for `PowerSeries.derivative`, and for `Differential` algebras (cf. univariate `Differential.deriv_aeval_eq`).
  - removes the need to go through `KaehlerDifferential.mvPolynomialBasis` for concrete derivations.
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/PDeriv.lean (has `pderiv`, `Derivation`; the `Polynomial.derivative'` corollary needs `Mathlib.Algebra.Polynomial.Derivation`, so it may go in a file importing both). Proposed PR title: "feat(Algebra/MvPolynomial/PDeriv): chain rule for derivations of `aeval`".
Next action: run `/generalise Roth.derivative_aeval` (target: the derivation form above); locally optionally restate with `[CommSemiring R]`; the single caller Roth/GenWronskian.lean:159 needs no change (the corollary has the same shape).

## Next step

Upstream `Derivation.map_mvPolynomial_aeval` (arbitrary derivation, `CommSemiring R`) with `Polynomial.derivative_mvPolynomial_aeval` as corollary; keep `Roth.derivative_aeval` locally (or replace it by the corollary) — caller Roth/GenWronskian.lean:159 unchanged.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.derivative_aeval/generalise.lean` (imports `Roth.GenWronskian`, `Mathlib.Algebra.Polynomial.Derivation`): (1) `Derivation.map_mvPolynomial_aeval` for arbitrary `D : Derivation R A M`, `CommSemiring R` — compiles; (2) project statement over `CommSemiring R` as a one-line corollary via `Polynomial.derivative'` — compiles; (3) the project proof verbatim under `CommSemiring R` — compiles; (4) `Roth.derivative_aeval` reference check — compiles. `lean_diagnostic_messages` on the file: no diagnostics (after fixing an initially-missing import of `Polynomial.derivative'` and an unused simp arg).
- Searches: Loogle ×2, LeanSearch ×1, Lean-Finder ×1, mathlib grep (`derivative_aeval`, `map_mvPolynomial_aeval`, `D (aeval`, `pderiv`+`aeval`/`∑`), WebSearch ×3; `ask_chatgpt_math` n/a (not configured).
