---
decl: Roth.normOne_mul_le
file: Roth/CoeffNorm.lean
line: 96
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Submultiplicativity of the l1 coefficient norm (length L(PQ) ≤ L(P)L(Q), the l1(M) Banach-algebra inequality) is absent from mathlib (no l1 norm on (Mv)Polynomial or AddMonoidAlgebra; only the nonarchimedean gaussNorm_mul_le); the Z-only proof compiles with abs_mul replaced by norm_mul_le for MvPolynomial over any SeminormedCommRing, and also for AddMonoidAlgebra R M over a SeminormedRing and any AddMonoid (evidence file clean).
action: Ship as MvPolynomial.l1Norm_mul_le over [SeminormedCommRing R] in the MvPolynomial.l1Norm PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean), optionally deriving it from an AddMonoidAlgebra l1 norm; keep the Z form for the call site Roth/CoeffNorm.lean:108 (normOne_prod_le) via Int.norm_eq_abs.
---

# Roth.normOne_mul_le

## Inventory entry

### `theorem Roth.normOne_mul_le`
- **Type**: `{σ : Type*} (P Q : MvPolynomial σ ℤ) : Roth.normOne (P * Q) ≤ Roth.normOne P * Roth.normOne Q`
- **What**: The ℓ¹ coefficient norm (length) of integer multivariate polynomials is submultiplicative: `‖PQ‖₁ ≤ ‖P‖₁ ‖Q‖₁`.
- **How**: Expand `P * Q` with `MvPolynomial.mul_def` as a double `Finsupp.sum` of monomials `monomial (a + b) (P_a Q_b)`; apply `Roth.normOne_sum_le` to the outer sum, rewrite the RHS by `Finset.sum_mul_sum`, then termwise apply `Roth.normOne_sum_le` again to the inner sum and close each term by `Roth.normOne_monomial` and `abs_mul` (via `Finset.sum_le_sum`, `Finset.sum_congr`).
- **Hypotheses**: none.
- **Uses from project**: `Roth.normOne`, `Roth.normOne_sum_le`, `Roth.normOne_monomial`
- **Used by**: Roth/CoeffNorm.lean:108 (`Roth.normOne_prod_le`, passed to `Finset.le_prod_of_submultiplicative_of_nonneg`); mentioned in the module docstring (line 27). No uses outside CoeffNorm.lean (`grep -rn normOne_mul_le Roth/`).
- **Visibility**: public
- **Lines**: 94–102, proof length 6 lines
- **Notes**: Listed under "Main results" of the module docstring. Source: clean.tex:495 (Lean note: "submultiplicativity for ‖·‖₁, then use these for the determinant").

## Junk check (Step 8)
- Used anywhere? Yes: by `normOne_prod_le`, which feeds `normOne_det_le` and hence Lemma 3 (`abs_coeff_det_hasseDeriv_le`, used in Theta.lean / Separation.lean).
- Wrapper of 1–2 mathlib calls? No — a 6-line proof with two applications of the finite triangle inequality and a monomial computation.
- Does mathlib have it? No (Phase 5): no ℓ¹ norm on `Polynomial`/`MvPolynomial`/`AddMonoidAlgebra`; mathlib's only polynomial submultiplicativity results are `Polynomial.gaussNorm_mul_le` / `MvPowerSeries.gaussNorm_mul_le` for **nonarchimedean** sup-type Gauss norms, and `Polynomial.mahlerMeasure_mul` (Mahler measure, a different quantity).
- Too specific (inline)? No: standard named norm inequality (cf. `norm_mul_le`), used by the product lemma.
- Well-chosen? Yes, modulo the parent's ℤ / `|·|` specialisation.
- Conclusion: `KEEP` — action: keep; re-aim at `MvPolynomial.l1Norm` with the parent def.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.normOne_mul_le` not in mathlib (no `namespace Roth` in `Mathlib/`). Not a glue lemma (6-line genuine proof). Full run in the generalised setting fixed by the parent verdict (`Roth.normOne`: YES-but-generalise-first to `MvPolynomial.l1Norm` over `[SeminormedCommRing R]`).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` elaborates without errors)
- decl `Roth.normOne_mul_le`: resolved at Roth/CoeffNorm.lean:96
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne_mul_le` is a theorem stating the following: for polynomials `P, Q ∈ ℤ[X_σ]`, the length (sum of absolute values of coefficients) of the product is at most the product of the lengths, `L(PQ) ≤ L(P) L(Q)`. Equivalently, the ℓ¹ norm on the coefficient vectors is submultiplicative for the convolution product of the monoid algebra `ℤ[ℕ^(σ)]`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the variables (arbitrary).
- `P Q : MvPolynomial σ ℤ` — the two factors.

Hypotheses (Lean side):
- none.

Conclusion (math): `L(PQ) ≤ L(P) L(Q)`.

Conclusion (Lean): `Roth.normOne (P * Q) ≤ Roth.normOne P * Roth.normOne Q`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API inequality of a helper norm (listed as a main result of a helper file, but not a project main theorem, not named, not a structure).

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 6
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: check skipped (theorem).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | length of polynomial L(PQ) ≤ L(P) L(Q) sum of absolute values of coefficients submultiplicative | partial | `L(P) = ∑ |a_i|` (Schinzel, Funct. Approx. 35, 37); Mahler 1962 "On some inequalities for polynomials in several variables" gives a length-of-product inequality | the bare inequality is treated as immediate from the triangle inequality |
| 2 | WebSearch (general form) | ℓ1 group algebra l1(G) Banach algebra convolution norm submultiplicative monoid algebra | yes | `‖f * g‖₁ ≤ ‖f‖₁ ‖g‖₁` making `ℓ¹(G)` / `L¹(G)` a Banach algebra (Young's inequality; arXiv 2301.12298, Lectures on C*-algebras arXiv 1211.3404) | most general standard form: ℓ¹ of a (discrete) monoid with coefficients in a normed ring |
| 3 | WebSearch (named-after / aliases) | Gelfond lemma height product of polynomials length inequality Mignotte bound | yes | Gelfond/Mahler/Mignotte factor bounds (Mahler 1962, Mignotte 1974, Abbott arXiv 0904.03057, arXiv 2308.03885); the length is the "1-norm" | the length's submultiplicativity is the easy companion of these bounds |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` line 495 | yes | "submultiplicativity for ‖·‖₁, then use these for the determinant" | the source's Lean note asks for exactly this lemma |
| 6 | nLab | Banach algebra / group algebra | yes | `ℓ¹(G)` as the standard example of a Banach algebra | no polynomial-specific page |
| 7 | nCatLab | — | n/a | — | not a categorical statement (a norm inequality) |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no coefficient norms |
| 9 | MathOverflow / Math.SE | length of polynomial / ℓ¹ norm of product of polynomials | yes | `L(fg) ≤ L(f)L(g)` used without comment in factor-bound discussions | standard folklore |
| 10 | recent arXiv (last 5 years) | sparse cofactor bounds (arXiv 2308.03885); model theory of convolution algebras (arXiv 2608.04308) | yes | same ℓ¹/convolution inequality | no competing form |

### Literature summary (Phase 3)

Concept identified as: submultiplicativity of the length / ℓ¹ coefficient norm; special case of the Banach-algebra inequality in `ℓ¹(M, R)` for a monoid `M`.
Sources agree on the standard form: yes.
Most general standard form: for a (semi)normed ring `R` (not necessarily commutative) and any monoid `M`, the ℓ¹ norm on the monoid algebra `R[M]` satisfies `‖fg‖₁ ≤ ‖f‖₁‖g‖₁`; polynomials are `M = ℕ^(σ)`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℝ / ℂ / normed ring / absolute value on a semiring — proof needs only subadditivity and submultiplicativity of the coefficient norm.
  - index monoid: ℕ, ℕ^σ, any (additive) monoid, groups (with ℓ¹ completion).
Disagreement with the literature: only the inherited ℤ / `|·|` specialisation of the parent def.

### Generality analysis — `Roth.normOne_mul_le`

Literature-standard form (from Phase 3): `l1Norm (p * q) ≤ l1Norm p * l1Norm q` for `p q : MvPolynomial σ R`, `[SeminormedCommRing R]` (and more generally for `R[M]`, `[SeminormedRing R] [AddMonoid M]`).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (via `normOne`) | `[SeminormedCommRing R]` | yes | proof needs only `norm_mul_le` in place of `abs_mul`; verified (`Evidence84.l1Norm_mul_le`) |
| 2 | norm structure | `|(· : ℝ)|` | `‖·‖` | yes | parent restatement; bridge `Evidence84.l1Norm_int_eq_normOne` via `Int.norm_eq_abs`; recovery `example` of the exact project statement compiles |
| 3 | negation in `R` | ring | not needed | yes (option) | `Evidence84.l1NormAbv_mul_le` for `v : AbsoluteValue R ℝ` on `[CommSemiring R]` compiles; parent-def design choice |
| 4 | index monoid | `σ →₀ ℕ` (MvPolynomial) | any `[AddMonoid M]`, noncommutative `[SeminormedRing R]` | yes (option) | `Evidence84.l1NormAMA_mul_le` on `AddMonoidAlgebra R M` compiles with the same proof shape; requires an ℓ¹ def on `AddMonoidAlgebra` (bigger design change than the parent proposed) |
| 5 | `σ : Type*` | arbitrary | arbitrary | no | already maximal |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (inherited from the parent def's ℤ-specialisation)
Number of weakening opportunities found: 1 primary (ℤ → `[SeminormedCommRing R]`), plus 2 optional (absolute value on a `CommSemiring`; `AddMonoidAlgebra R M` over `[SeminormedRing R] [AddMonoid M]`)
Verification: `.mathlib-quality/overview/evidence/Roth.normOne_mul_le/general_and_composition.lean` — all three general versions plus the ℤ bridge and a recovery `example`; `lean_diagnostic_messages`: no errors (one unused-section-variable linter warning only).
Proposed restatement:

```lean
theorem MvPolynomial.l1Norm_mul_le {σ R : Type*} [SeminormedCommRing R]
    (p q : MvPolynomial σ R) : (p * q).l1Norm ≤ p.l1Norm * q.l1Norm
```

Cost of restatement: CHEAP — the project proof with `abs_mul` replaced by `norm_mul_le` (one term changed).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | no hypotheses | — |
| 2 | Sequences → filters? | no | finite algebraic inequality | — |
| 3 | Construction → universal property? | no | an inequality | — |
| 4 | Set predicate → bundled substructure? | no | — | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ → `[SeminormedCommRing R]` (with the parent) | `l1Norm_prod_le`, determinant bounds over ℝ, ℂ, ℚ_p, … |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general monoid? | option | ℓ¹ norm on `AddMonoidAlgebra R M` (any `AddMonoid M`), `MvPolynomial`/`Polynomial` versions as corollaries | one proof for `Polynomial`, `MvPolynomial`, Laurent polynomials, group rings; could later underlie a `NormedRing` structure on a type synonym (ℓ¹ completion) |
| 8 | Concrete-via-abstract? | yes | after `mul_def` the proof uses only subadditivity (`normOne_sum_le`), the monomial computation and multiplicativity of `|·|` on ℤ — exactly `norm_mul_le` for any seminormed ring; covered by row 5 | — |
| 9 | False-generalisation guard | no | for `R = ℤ` the general statement reduces to the project one (compiled `example`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.l1Norm_mul_le` over `[SeminormedCommRing R]` (above); optional upgrade to `AddMonoidAlgebra` with polynomial corollaries.
  - Cost: CHEAP (MvPolynomial) / MODERATE (AddMonoidAlgebra route, requires redesigning the parent def)
  - Mathlib downstream this enables: `l1Norm_prod_le` (via `Finset.le_prod_of_submultiplicative_of_nonneg`), Leibniz determinant bounds, univariate `Polynomial.l1Norm_mul_le` companion closing the ℓ¹ TODO of `Mathlib/Analysis/Polynomial/Norm.lean`, and comparison with `Polynomial.mahlerMeasure_mul` / `mahlerMeasure_le_sum_norm_coeff` for Mignotte-type factor bounds.
  - Real mathematical improvement: one submultiplicativity statement for every seminormed coefficient ring instead of a ℤ copy.

### Proof strategy — `Roth.normOne_mul_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ instead of filters? | no | — | — |
| 2 | Elementwise algebra instead of ideals? | no | inequality on coefficients is inherently elementwise | — |
| 3 | Sequences instead of filters? | no | — | — |
| 4 | Construction instead of universal property? | no | — | — |
| 5 | Missing mathlib helpers? | yes | `l1Norm_sum_le` and `l1Norm_monomial` (ship in the same PR, already assessed YES-but-generalise-first) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(Expand by `mul_def`, two finite triangle inequalities, monomial norm — the standard proof; in the general setting `Finset.sum_congr … abs_mul` becomes `trans_le (norm_mul_le _ _)`.)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.normOne_mul_le`

[A] Lean-Finder       "sum of norms of coefficients of a product of polynomials is at most the product of the sums of norms of coefficients"  no hits (only `Polynomial.mahlerMeasure_mul`, `Polynomial.le_gaussNorm`, degree-of-product lemmas)
[B] Loogle            `Finsupp.sum (_ * _) _ ≤ _ * _`  no hits
[C] LeanSearch        "l1 norm of convolution in monoid algebra is submultiplicative"  no hits (`Finset.nnnorm_prod_le`, `AddMonoidAlgebra.mul_apply`, `WithLp.instUnitizationNormedRing` — unrelated)
[D] Grep mathlib src  `l1Norm`, `sum_norm_coeff`, `norm_mul_le_sum`, `gaussNorm_mul`, `supNorm_mul`, norm instances on `AddMonoidAlgebra`/`MonoidAlgebra`, `namespace Roth`  no ℓ¹ polynomial/monoid-algebra norm; ℓ¹ TODO at Analysis/Polynomial/Norm.lean:34–38; `Polynomial.gaussNorm_mul_le` (RingTheory/Polynomial/GaussNorm.lean:197) and `MvPowerSeries.gaussNorm_mul_le` (RingTheory/MvPowerSeries/GaussNorm.lean:137) need a **nonarchimedean** `v` (sup-type norm), so they do not cover the archimedean ℓ¹ case
[E] Name pattern      `l1Norm_mul`, `normOne_mul` via grep of Mathlib (lean_local_search covered by [D])  no hits

Searched for both:
  - the user's current form (ℤ, `|·|`)
  - the literature-standard form (ℓ¹ on (Mv)Polynomial / monoid algebra over a seminormed ring)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form).

### Normal-form check — `Roth.normOne_mul_le`

Equivalent formalisms: `l1Norm (p * q) ≤ l1Norm p * l1Norm q`; a `NormedRing`/`SeminormedRing` instance on an ℓ¹ type synonym giving `norm_mul_le`; a bundled `RingSeminorm`-like structure (`mul_le'` field).
Does mathlib already have a canonical form? Yes for norms: `norm_mul_le (a b : α) : ‖a * b‖ ≤ ‖a‖ * ‖b‖`. Our statement matches that shape and argument order. RHS convention respected? n/a (inequality).

### Syntactic generality — `Roth.normOne_mul_le`

Alternative restatements attempted:
- `l1Norm (p * q) ≤ l1Norm p * l1Norm q` (explicit `p q`, as `norm_mul_le`)
- `l1Norm p ≤ a → l1Norm q ≤ b → l1Norm (p * q) ≤ a * b` (cf. `norm_mul_le_of_le`)
- a `RingSeminorm (MvPolynomial σ R)` packaging `l1Norm` (gives `map_mul_le_mul`)
Chosen restatement: the explicit `p q` form. Justification: matches `norm_mul_le`, and is exactly the shape `Finset.le_prod_of_submultiplicative_of_nonneg` consumes at the one call site.

### Superfluous-argument audit — `Roth.normOne_mul_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `σ : Type*` | yes | index type |
| 2 | `P Q` | yes | — |
| 3 | ℤ coefficients (via `normOne`) | no | generalise with parent to `[SeminormedCommRing R]` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: 1 to drop (ℤ specialisation, via parent def)

Overall: RESTATE-BEFORE-SHIP (state against `MvPolynomial.l1Norm` with `‖·‖`; name `l1Norm_mul_le`)

### Call sites — `Roth.normOne_mul_le`

Internal use count: 0 outside the declaring file; 1 inside Roth/CoeffNorm.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:108 | `(by simpa using (normOne_monomial (0 : σ →₀ ℕ) 1).le) normOne_mul_le s f` (`normOne_prod_le`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne_mul_le`?):
  - (none; no other `mul_def` expansion of a normOne bound in `Roth/`).

Note: K = 1, but the single consumer is the standard `prod_le` corollary, and submultiplicativity is the defining Banach-algebra property of the norm — canonical API, not a wrong abstraction.

### Composition check (Phase 6)

Can `Roth.normOne_mul_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: via a mathlib norm on `MvPolynomial`/`AddMonoidAlgebra` and `norm_mul_le`
  - Mathlib decls used: `norm_mul_le`
  - Result: fails — no ℓ¹ norm/NormedRing instance on `MvPolynomial`, `AddMonoidAlgebra` or `Finsupp` in mathlib.
Attempt 2: via `Polynomial.gaussNorm_mul_le` / `MvPowerSeries.gaussNorm_mul_le`
  - Result: fails — these need `IsNonarchimedean v` and are sup-type norms; `|·|` on ℤ is archimedean and the ℓ¹ sum is not a Gauss norm.
Attempt 3: `mul_def` + two finite triangle inequalities + monomial norm (the project proof)
  - Result: succeeds, but is a 6-line proof using non-mathlib lemmas (`normOne_sum_le`, `normOne_monomial`) — a genuine proof, not a composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.normOne_mul_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): `L(PQ) ≤ L(P)L(Q)`, the polynomial case of the `ℓ¹(M)` Banach-algebra inequality; requested verbatim by the source (clean.tex:495).
- Generality analysis (Phase 4): STRICTLY NARROWER (ℤ via parent def); general form over `[SeminormedCommRing R]` compiled, plus AbsoluteValue/CommSemiring and AddMonoidAlgebra/SeminormedRing variants.
- Mathlib search (Phase 5): not in mathlib (no ℓ¹ polynomial norm; Norm.lean ℓ¹ TODO; only nonarchimedean Gauss-norm submultiplicativity).
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Mathlib has no ℓ¹ coefficient norm on `Polynomial`, `MvPolynomial` or `AddMonoidAlgebra` — `Mathlib/Analysis/Polynomial/Norm.lean` explicitly lists the ℓ¹ norm ("length") as a TODO — and its only submultiplicativity results for polynomial norms are `Polynomial.gaussNorm_mul_le` / `MvPowerSeries.gaussNorm_mul_le`, which require a nonarchimedean absolute value and so say nothing about the archimedean ℓ¹ length. Submultiplicativity is the key property of the length (it is what makes ℓ¹(M) a Banach algebra and drives Gelfond/Mahler-type factor estimates), and it is the step that turns the triangle inequality into the product and Leibniz-determinant bounds of Lemma 3. It therefore belongs in the parent `MvPolynomial.l1Norm` API.

The evidence file shows the project proof goes through for any `[SeminormedCommRing R]` with the single change `abs_mul` → `norm_mul_le`, recovering the ℤ statement via `Int.norm_eq_abs`. The same proof also works for an `AbsoluteValue`-based ℓ¹ norm on a commutative semiring, and — with the same shape — for the ℓ¹ norm on `AddMonoidAlgebra R M` over a noncommutative `[SeminormedRing R]` and any `[AddMonoid M]`; the latter is the literature-maximal form and is offered as an option for the parent `/generalise` (it would make the `MvPolynomial` and `Polynomial` versions one-line corollaries).

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (coefficient ring via the normed typeclass hierarchy), inherited from the parent.

Proposed restatement:
```lean
theorem MvPolynomial.l1Norm_mul_le {σ R : Type*} [SeminormedCommRing R]
    (p q : MvPolynomial σ R) : (p * q).l1Norm ≤ p.l1Norm * q.l1Norm := by
  sorry  -- proof in evidence file (project proof with norm_mul_le in place of abs_mul)
```

Estimated cost of regeneralisation: CHEAP.

Mathlib downstream this enables:
- `l1Norm_prod_le` (with `‖1‖ ≤ 1`/`NormOneClass`) and Leibniz determinant bounds `l1Norm_det_le` for every seminormed coefficient ring;
- a univariate `Polynomial.l1Norm_mul_le` companion closing the ℓ¹ TODO in `Mathlib/Analysis/Polynomial/Norm.lean`, alongside `supNorm`;
- together with `Polynomial.mahlerMeasure_mul` and `mahlerMeasure_le_sum_norm_coeff`, the standard Mignotte factor-bound chain.

PR grouping: ship with `MvPolynomial.l1Norm` and its API (`l1Norm_nonneg`, `l1Norm_eq_sum_of_support_subset`, `l1Norm_monomial`, `l1Norm_zero`, `norm_coeff_le_l1Norm`, `l1Norm_add_le`, `l1Norm_neg`, `l1Norm_sum_le`, `l1Norm_prod_le`) as one PR.

Next action: run `/generalise Roth.normOne_mul_le` together with the parent `/generalise Roth.normOne`, restate as `MvPolynomial.l1Norm_mul_le` (deciding whether to base the def on `AddMonoidAlgebra`), and keep the ℤ form via `Int.norm_eq_abs` at the call site Roth/CoeffNorm.lean:108.

---

## Next step

Restate as `MvPolynomial.l1Norm_mul_le` over `[SeminormedCommRing R]` in the `MvPolynomial.l1Norm` PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean), with the project call site (Roth/CoeffNorm.lean:108, `normOne_prod_le`) using the ℤ specialisation.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.normOne_mul_le/general_and_composition.lean` (imports `Roth.CoeffNorm`, `Mathlib.Analysis.Normed.Ring.Int`): (1) general `l1Norm` over `[SeminormedCommRing R]` with `l1Norm_mul_le`, ℤ bridge `l1Norm_int_eq_normOne`, recovery `example` of the exact project statement; (2) `l1NormAbv_mul_le` for `v : AbsoluteValue R ℝ` on `[CommSemiring R]`; (3) `l1NormAMA_mul_le` on `AddMonoidAlgebra R M` for `[SeminormedRing R] [AddMonoid M]`. `lean_diagnostic_messages`: no errors (one unused-section-variable linter warning). First attempt failed only in section (3) because `AddMonoidAlgebra` is now a structure with a `coeff : M →₀ R` field (not a `Finsupp` synonym); fixed by going through `.coeff`.
- Mathlib greps: `l1Norm`, `sum_norm_coeff`, `norm_mul_le_sum`, `gaussNorm_mul`, `supNorm_mul`, `namespace Roth`, AddMonoidAlgebra norm instances — no ℓ¹ norm; ℓ¹ TODO at Analysis/Polynomial/Norm.lean; nonarchimedean `gaussNorm_mul_le` only.
- Lean-Finder / LeanSearch / Loogle queries as in Phase 5 (no hit).
- WebSearch ×3 (length of product; ℓ¹(G) Banach algebra; Gelfond/Mahler/Mignotte), local reference clean.tex line 495.
- ChatGPT MCP: n/a (not configured in this session).
