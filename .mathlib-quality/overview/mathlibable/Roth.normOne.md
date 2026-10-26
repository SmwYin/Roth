---
decl: Roth.normOne
file: Roth/CoeffNorm.lean
line: 47
kind: def
visibility: public
verdict: YES-but-generalise-first
cost: MODERATE
junk: KEEP
rationale: The l1 coefficient norm (the length L(P) of a polynomial) is absent from mathlib, whose Analysis/Polynomial/Norm.lean lists l^p norms incl. l^1 as a TODO; the Z-only def generalises verbatim to MvPolynomial over any SeminormedCommRing with nonneg, coeff bound, triangle and submultiplicativity re-proved and a bridge back to Roth.normOne (compiled).
action: Restate as a norm-valued l1Norm on MvPolynomial σ R for [SeminormedCommRing R] (with a univariate Polynomial companion next to Polynomial.supNorm in Mathlib/Analysis/Polynomial/Norm.lean), keep Roth.normOne as the R = ℤ abbreviation via Int.norm_eq_abs, and re-aim the 13 CoeffNorm.lean API lemmas at the general def before upstreaming.
---

# Roth.normOne

## Inventory entry

### `def Roth.normOne`
- **Type**: `{σ : Type*} (P : MvPolynomial σ ℤ) : ℝ`
- **What**: The ℓ¹ norm `‖P‖₁ = ∑_e |a_e|` of the integer coefficients of a multivariate polynomial, as a real number.
- **How**: Direct definition `∑ d ∈ P.support, |((P.coeff d : ℤ) : ℝ)|`.
- **Hypotheses**: none (no typeclass assumptions on `σ`).
- **Uses from project**: `[]`
- **Used by**: Roth/CoeffNorm.lean only (no other file mentions `normOne`; Theta.lean and Separation.lean import the module but use only the downstream `abs_coeff_det_hasseDeriv_le`/`abs_coeff_diag_le`/`abs_eval_le`, whose statements do not mention `normOne`). Within CoeffNorm.lean: `normOne_nonneg` 50, `normOne_eq_sum_of_support_subset` 54, `normOne_monomial` 59, `normOne_zero` 66, `abs_coeff_le_normOne` 71, `normOne_add_le` 77, `normOne_neg` 86, `normOne_sum_le` 90, `normOne_mul_le` 96, `normOne_prod_le` 105, `normOne_le_card_mul` 113, `normOne_det_le` 119, `normOne_hasseDeriv_le` 148, and the proof of `abs_coeff_det_hasseDeriv_le` (lines 265-270).
- **Visibility**: public
- **Lines**: 46–47, body 1 line
- **Notes**: Listed under "Main definitions" of the module docstring. Serves purely as an intermediate quantity in the proof of Lemma 3 (the final statement bounds `|coeff|`, not `normOne`).

## Junk check (Step 8)
- Used anywhere? Yes: 13 API lemmas plus the Lemma 3 proof, all in CoeffNorm.lean (K = 0 external-file uses, but ~60 occurrences in-file).
- Wrapper of 1–2 mathlib calls? No mathlib def to wrap; it is a single `Finset.sum`. Mathlib only writes the quantity inline (`p.sum fun _ a ↦ ‖a‖` in `Polynomial.mahlerMeasure_le_sum_norm_coeff`).
- Does mathlib have it? No (see Phase 5): mathlib has `Polynomial.supNorm` (ℓ^∞) and `PiLp 1`/`lp` (functions on index types, not polynomials/Finsupp), and its Norm.lean explicitly lists the ℓ¹ norm as a TODO.
- Too specific (inline)? No: a named quantity with a submultiplicative API is exactly what makes the Lemma 3 bound a short `calc`; inlining would duplicate the triangle/submultiplicativity arguments.
- Well-chosen? Mostly; the only defect is the hard-coded `ℤ` coefficients and `|(z : ℝ)|` instead of `‖z‖` (see Phase 4).
- Conclusion: `KEEP` — action: keep the def but restate it over `[SeminormedCommRing R]` with `‖·‖` (Roth.normOne becomes the `R = ℤ` case).

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.normOne` not in mathlib (no `namespace Roth` in `Mathlib/`). It is a def, not a glue lemma. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` elaborates with no errors)
- decl `Roth.normOne`:       resolved at Roth/CoeffNorm.lean:47
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne` is a definition of the following: for a polynomial `P = ∑_e a_e X^e ∈ ℤ[X_σ]`, its ℓ¹ norm (classically the *length* `L(P)`) is `‖P‖₁ = ∑_e |a_e| ∈ ℝ`. It is a norm on the coefficient vector, submultiplicative with respect to polynomial multiplication, and dominates every coefficient.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the set of variables (arbitrary, possibly infinite).
- `P : MvPolynomial σ ℤ` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `‖P‖₁ = ∑_e |a_e|`.

Conclusion (Lean): n/a — definition (`∑ d ∈ P.support, |((P.coeff d : ℤ) : ℝ)|`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-line def of a classical auxiliary quantity (polynomial length), not a new structure nor a main result; it is a "main definition" of a helper file only.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                 | no       | Proofs unfold it explicitly (`rw [normOne]`, `simp [normOne]`); no proof relies on it being sealed. |
| Avoid typeclass diamonds          | no       | It is an unbundled real-valued function; no instance involved. |
| Mark semantic intent / API name   | yes      | 13 API lemmas (triangle, submultiplicativity, determinant bound) are stated against the name; in mathlib the same name would serve `mahlerMeasure_le_sum_norm_coeff`, Landau–Mignotte-type bounds and the TODO in Analysis/Polynomial/Norm.lean. |

Conclusion: ONE-LINER WITH-EXEMPTION

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | "length of a polynomial sum of absolute values of coefficients L(P) submultiplicative" | yes | `L(P) = ∑ |a_i|` (length) | Schinzel's papers on reduced length; Wikipedia Landau–Mignotte bound uses the same quantity; L(PQ) ≤ L(P)L(Q) is the folklore triangle-inequality fact |
| 2 | WebSearch (general form) | "l1 norm Banach algebra group algebra ℓ1(G) submultiplicative convolution monoid algebra" | yes | `ℓ¹(G)` with convolution is a Banach algebra; norm `∑ |f(g)|` submultiplicative | The fully general form: ℓ¹ norm on a (semi)group/monoid algebra over a normed ring; polynomials are the case `G = ℕ^σ` |
| 3 | WebSearch (named-after / project context) | Roth's theorem proof lemma coefficients determinant bound "l!" polynomial norm sum absolute coefficients | partial | heights `h(P)` / coefficient bounds in expositions of Roth (arXiv 2502.00731, Klazar AKTC notes) | Confirms the use as an auxiliary height-type quantity in Roth's proof; no different standard form |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP is not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `norm`, `abc`, `\|f\|_1` | yes | `\|f\|_1 = ∑_e |a_e|`, `abc(f) = max_e |a_e|` (lines 445-452) | Source §3 proof of Lemma 3 defines exactly this; uses triangle inequality and multiplicativity on monomials |
| 6 | nLab | "Banach algebra", "group algebra" ℓ¹ | yes | ℓ¹(G) as the standard Banach group algebra | No polynomial-specific page; confirms the monoid-algebra generality |
| 7 | nCatLab | — | n/a | — | Not a categorical concept (a concrete norm on a coefficient vector); briefly checked nLab entries above suffice |
| 8 | Stacks Project | — | n/a | — | Not an algebraic-geometry concept; Stacks has no coefficient norms |
| 9 | MathOverflow / Math.SE | length of polynomial L(PQ) ≤ L(P)L(Q) | yes (via #1 sources) | same `L(P)`; standard inequalities `M(P) ≤ L(P) ≤ 2^n M(P)` | The Mahler-measure comparison is the main consumer in the literature |
| 10 | recent arXiv (last 5 years) | trace polynomials / Roth expositions (from #1, #3) | yes | ℓ¹ and Frobenius norms of coefficient vectors used for height bounds | No competing definition |

### Literature summary (Phase 3)

Concept identified as: the *length* `L(P)` (ℓ¹ norm of the coefficient vector) of a polynomial; a special case of the ℓ¹ norm on a monoid algebra `ℓ¹(M, R)`.
Sources agree on the standard form: yes — `∑ |a_e|` (or `∑ ‖a_e‖` over a normed coefficient ring).
Most general standard form: for a (semi)normed ring `R` and a monoid `M`, `‖f‖₁ = ∑_m ‖f(m)‖` on finitely supported `f : M →₀ R`, submultiplicative for convolution; polynomials are `M = ℕ` / `ℕ^σ`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℂ / any normed ring; the most general is a seminormed ring (commutative for `MvPolynomial`).
  - index monoid: ℕ (univariate), ℕ^σ (multivariate), arbitrary monoid (group algebra).
Disagreement with the literature: the user's form fixes coefficients in ℤ and writes `|(z : ℝ)|` instead of `‖z‖`; otherwise it matches.

### Generality analysis — `Roth.normOne`

Literature-standard form (from Phase 3): `‖p‖₁ = ∑_e ‖coeff e p‖` for `p : MvPolynomial σ R`, `R` a seminormed (commutative) ring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (fixed) | any `[SeminormedCommRing R]` | yes | Every API lemma uses only norm axioms (`norm_add_le`, `norm_mul_le`, `norm_nonneg`); verified in evidence file |
| 2 | `|((z : ℤ) : ℝ)|` | absolute value of the real cast | `‖z‖` | yes | `Int.norm_eq_abs` identifies them; bridge lemma compiled |
| 3 | `σ : Type*` | arbitrary | arbitrary | no | already maximal |
| 4 | index monoid | `σ →₀ ℕ` (MvPolynomial) | any `AddMonoidAlgebra R M` | yes, in principle | Not verified; MvPolynomial is the form with downstream users, so the `AddMonoidAlgebra` widening is noted only as an option |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 2 verified (coefficient ring ℤ → `[SeminormedCommRing R]`; `|·|` → `‖·‖`), 1 unverified option (monoid algebra).
Verification: `.mathlib-quality/overview/evidence/Roth.normOne/generalise_seminormedring.lean` defines `Evidence.l1Norm` over `[SeminormedCommRing R]` and proves `l1Norm_eq`, `l1Norm_nonneg`, `l1Norm_eq_sum_of_support_subset`, `l1Norm_zero`, `l1Norm_monomial`, `norm_coeff_le_l1Norm`, `l1Norm_add_le`, `l1Norm_sum_le`, `l1Norm_mul_le`, and the bridge `l1Norm_int_eq_normOne : l1Norm P = Roth.normOne P`; `lean_diagnostic_messages` reports no errors (only a long-line lint, since fixed). Note `MvPolynomial` itself requires `CommSemiring R`, so `SeminormedCommRing` (not `SeminormedRing`) is the natural floor for the MvPolynomial statement.
Proposed restatement:

```lean
noncomputable def MvPolynomial.l1Norm {σ R : Type*} [SeminormedCommRing R]
    (p : MvPolynomial σ R) : ℝ :=
  ∑ d ∈ p.support, ‖p.coeff d‖
```

Cost of restatement: MODERATE — the def and core lemmas port mechanically (done in the evidence file); the remaining CoeffNorm lemmas (`normOne_prod_le` needs `‖1‖ ≤ 1`, i.e. `[NormOneClass R]`; `normOne_hasseDeriv_le` needs `norm_nsmul_le`; `normOne_det_le` needs `‖-x‖ = ‖x‖`) need small edits, and the project would restate its ℤ-hypotheses `|(c : ℝ)| ≤ B` via `Int.norm_eq_abs`.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | no bundled hypotheses | — |
| 2 | Sequences → filters? | no | finite algebraic sum, no limits | — |
| 3 | Construction → universal property? | no | a norm is not characterised by a universal property here | — |
| 4 | Set predicate → bundled substructure? | no | no sets | — |
| 5 | Field/specific → typeclass hierarchy? | yes | `ℤ` → `[SeminormedCommRing R]`, `|·|` → `‖·‖` | `norm_add_le`/`norm_mul_le` API; `Polynomial.mahlerMeasure_le_sum_norm_coeff` and `mapMahlerMeasure_le_sum_norm_coeff` could be stated against it |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general monoid? | yes (option) | `AddMonoidAlgebra R M` ℓ¹ norm, possibly a `NormedRing` instance on a type synonym | Banach-algebra ℓ¹(M) API; not needed by current consumers |
| 8 | Concrete-via-abstract? | yes | The body/proofs never use anything specific to ℤ beyond `|·|` being a ring norm | Same proofs serve ℂ-polynomials (Mahler-measure file) and p-adic coefficient rings |
| 9 | False-generalisation guard | no | For `R = ℤ`, `‖z‖ = |(z:ℝ)|` exactly (compiled bridge), so the generalised def is the same object | prevents ship-then-revert |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.l1Norm` (and `Polynomial.l1Norm`) over `[SeminormedCommRing R]` / `[SeminormedRing R]`, a real-valued function next to `Polynomial.supNorm` (unbundled, like `supNorm`; a bundled `NormedAddCommGroup` instance would conflict with other possible polynomial norms, which is why mathlib keeps `supNorm` unbundled).
  - Cost: MODERATE
  - Mathlib downstream this enables: discharges the ℓ¹ TODO in `Mathlib/Analysis/Polynomial/Norm.lean`; gives a name to the inline `p.sum fun _ a ↦ ‖a‖` in `Polynomial.mahlerMeasure_le_sum_norm_coeff` / `mapMahlerMeasure_le_sum_norm_coeff`; `supNorm ≤ l1Norm ≤ (natDegree+1) • supNorm` comparison lemmas.
  - Real mathematical improvement: one submultiplicative coefficient norm for all normed coefficient rings instead of a ℤ-only copy.

### Proof strategy — `Roth.normOne`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ vs filters? | no | — | — |
| 2 | Element-wise vs point-free algebra? | no | finite sums are the natural argument | — |
| 3 | Sequences vs filters? | no | — | — |
| 4 | Construction vs universal property? | no | — | — |
| 5 | Missing mathlib helpers? | yes | the whole ℓ¹-norm API (triangle, submultiplicativity, coefficient bound) is missing; it is exactly what the evidence file proves | MODERATE (file follow-up PR) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (a def; the API proofs via `Finset.sum_subset`, `Finset.le_sum_of_subadditive`, `MvPolynomial.mul_def` are idiomatic)
  - Missing mathlib API: the ℓ¹ norm and its API themselves.

### Diamond / defeq risk — `Roth.normOne`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | Unbundled `MvPolynomial σ R → ℝ` function; no instance introduced. (A bundled `Norm (MvPolynomial σ R)` instance WOULD be risky — sup vs ℓ¹ vs Gauss norms — so stay unbundled like `Polynomial.supNorm`.) |
| 2 | Reducibility leak | none | Plain (semireducible) def, not `@[reducible]`; `l1Norm_eq` is `rfl` and used for unfolding. |
| 3 | Non-canonical unfolding | low | `simp` does not unfold it unless asked; `rfl` unfolding to the support sum is expected and stable. |
| 4 | Instance priority collision | none | not an instance. |
| 5 | Universe-polymorphism issues | none | `σ R : Type*`, no universe constraint forced (evidence file elaborates universe-polymorphically). |
| 6 | Coercion ambiguity | none | no coercions introduced. |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none (row 3 low)

### Mathlib search-status: `Roth.normOne`

[A] Lean-Finder       "l1 norm of a finitely supported function, sum of norms of values"   hits only `PiLp.norm_eq_of_L1` (Fintype index, not Finsupp/polynomial), `lp.*` (functions on index types); no polynomial ℓ¹ norm
[B] Loogle            `MvPolynomial.sum, ‖_‖` (no such constant in this mathlib); `Finsupp.sum, ‖_‖, |- _ ≤ _`   no hits
[C] LeanSearch        "sum of norms of coefficients of a polynomial is submultiplicative"   hits `Polynomial.mahlerMeasure_le_sum_norm_coeff` (inline `p.sum fun _ a ↦ ‖a‖`), `Polynomial.le_gaussNorm`; no ℓ¹ def
[D] Grep mathlib src  `l1Norm`, `oneNorm`, `normOne`, `sum_norm_coeff`, `instance.*Norm.*(Finsupp|AddMonoidAlgebra|MvPolynomial|Polynomial)`, `def .*[Nn]orm` in Analysis/Polynomial, Algebra/(Mv)Polynomial, RingTheory/(Mv)Polynomial   only `Polynomial.supNorm` (Analysis/Polynomial/Norm.lean:53), `Polynomial.gaussNorm`, `MvPowerSeries` Gauss norm; Norm.lean:36 TODO "All other `l^p` norms can be defined on Polynomials as well. In the literature, the `l^1` norm is sometimes called the polynomial's _length_"; no norm on `Finsupp` / `AddMonoidAlgebra` anywhere under Analysis/
[E] Name pattern      lean_local_search-style grep for `normOne`, `l1Norm`, `sum_norm_coeff`   none except the project's own `Roth.normOne`

Searched for both the user's ℤ-form and the general seminormed-ring / monoid-algebra form.

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); mathlib records it as an explicit TODO.

### Normal-form check — `Roth.normOne`

Equivalent formalisms: `∑ d ∈ p.support, ‖p.coeff d‖`; `p.sum fun _ a ↦ ‖a‖` (Finsupp.sum style, used inline in MahlerMeasure.lean); `‖(PiLp 1 ...)‖` on a finite box (needs a Fintype index, unsuitable).
Does mathlib already have a canonical form? No def; the inline idiom is the `sum`-over-support form.
Proposed canonical form: the support sum of `‖coeff‖`, with an `_eq_sum_of_support_subset` lemma (the project already has it).
RHS convention respected? yes (unfolding lemmas put the explicit sum on the RHS).

### Syntactic generality — `Roth.normOne`

Alternative restatements attempted:
- `∑ d ∈ P.support, |((P.coeff d : ℤ) : ℝ)|` (current)
- `∑ d ∈ p.support, ‖p.coeff d‖` over `[SeminormedCommRing R]` (evidence file)
- `Finsupp.sum` form (did not elaborate: `MvPolynomial`/`AddMonoidAlgebra` has no `.sum` field in this mathlib version)

Chosen restatement: the `‖·‖` support-sum over `[SeminormedCommRing R]`.
Justification: applies to every normed coefficient ring and composes with the `norm_*` API; the ℤ case is recovered by `Int.norm_eq_abs`.

### Superfluous-argument audit — `Roth.normOne`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | coefficients in `ℤ` | no | only norm axioms are used; generalise to `[SeminormedCommRing R]` |
| 2 | `σ : Type*` | yes | the variable type; no constraint |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (`ℤ`/`|·|` → `R`/`‖·‖`)
Superfluous arguments: 1 to drop (the fixed coefficient ring ℤ)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.normOne`

Internal use count: 0 (outside the declaring file)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| (none outside Roth/CoeffNorm.lean) | In-file: 13 API lemmas (lines 50–155) and the `calc` in `abs_coeff_det_hasseDeriv_le` (265–270): `_ ≤ normOne (...).det := abs_coeff_le_normOne _ _` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne`?):
  - Roth/CoeffNorm.lean:223 `abs_eval_le` sums absolute coefficients by hand against the sup bound `B` rather than through `normOne` (a different estimate, coefficient-sup times box size); no genuine duplicate.

### Composition check (Phase 6)

Can `Roth.normOne` be derived from mathlib in ≤3 chained calls?

Attempt 1: `fun P ↦ (P.toFinsupp? ...)` as a `PiLp 1` / `lp 1` norm.
  - Mathlib decls used: `PiLp.norm_eq_of_L1`, `lp`
  - Result: fails
  - Notes: `PiLp` needs a `Fintype` index (the exponent type `σ →₀ ℕ` is infinite); `lp E 1` is a subtype of all functions with a summability witness, so a polynomial would need an embedding into `lp` plus a proof of membership and submultiplicativity is not available — a new construction, not a composition.

Attempt 2: express via `Polynomial.supNorm`/`gaussNorm`.
  - Result: fails — these are sup (ℓ^∞) norms, univariate only.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.normOne`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the quantity is the classical *length* `L(P) = ∑ ‖a_e‖` (Schinzel, Landau–Mignotte, Mahler-measure comparisons), special case of the ℓ¹ monoid-algebra norm; the source paper §3 uses exactly `‖f‖₁`.
- Generality analysis (Phase 4): STRICTLY NARROWER — ℤ coefficients generalise to `[SeminormedCommRing R]`, verified in the evidence file together with a bridge back to `Roth.normOne`.
- Mathlib search (Phase 5): not in mathlib; `Mathlib/Analysis/Polynomial/Norm.lean` lists the ℓ¹ norm as a TODO, and `mahlerMeasure_le_sum_norm_coeff` writes it inline.
- Composition check (Phase 6): NOT-COMPOSABLE (`PiLp 1` needs a finite index; `lp` is the wrong carrier).

**Rationale:**

Mathlib has a sup norm on polynomials (`Polynomial.supNorm`) but no ℓ¹ coefficient norm on `Polynomial`, `MvPolynomial`, `Finsupp` or `AddMonoidAlgebra`; its own docstring names the ℓ¹ norm ("length") as a TODO, and the Mahler-measure file already needs it (inline `p.sum fun _ a ↦ ‖a‖`). The project's definition fills that gap but only for ℤ coefficients written as `|(z : ℝ)|`. The evidence file shows the def and its central API (nonnegativity, support-subset formula, monomials, coefficient bound, triangle inequality, finite-sum triangle, submultiplicativity) go through unchanged over any `[SeminormedCommRing R]`, and that the ℤ case is definitionally the project's `normOne` up to `Int.norm_eq_abs`. The one-liner is justified by the API-name exemption: 13 lemmas and a mathlib TODO hang on the name.

Re-aim consequences for downstream lemmas: all 13 `normOne_*` lemmas in CoeffNorm.lean are re-aimed at the general def. `normOne_nonneg`, `_eq_sum_of_support_subset`, `_monomial`, `_zero`, `abs_coeff_le_normOne` (→ `norm_coeff_le_l1Norm`), `_add_le`, `_sum_le`, `_mul_le` are already verified in the evidence file; `normOne_neg` needs `norm_neg` (SeminormedCommRing gives it); `normOne_prod_le` needs `‖1‖ ≤ 1` (add `[NormOneClass R]` or use `norm_one_le`-style hypothesis); `normOne_le_card_mul` and `normOne_det_le` port with `‖·‖` in place of `|·|`; `normOne_hasseDeriv_le` is Hasse-derivative-specific and would stay project-side (or go with the MvPolynomial Hasse derivative PR), proved via `norm_nsmul_le`. Downstream of the file nothing changes: `abs_coeff_det_hasseDeriv_le` (used by Theta.lean / Separation.lean) never mentions `normOne` in its statement, so the refactor is file-local.

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (Bourbaki 2.0: coefficient ring via the normed typeclass hierarchy).

Proposed restatement:
```lean
namespace MvPolynomial
variable {σ R : Type*} [SeminormedCommRing R]
/-- The ℓ¹ norm (length) `∑ ‖a_e‖` of the coefficients. -/
noncomputable def l1Norm (p : MvPolynomial σ R) : ℝ := ∑ d ∈ p.support, ‖p.coeff d‖
theorem l1Norm_mul_le (p q : MvPolynomial σ R) : l1Norm (p * q) ≤ l1Norm p * l1Norm q := by
  sorry  -- proof in evidence file
end MvPolynomial
-- project side
noncomputable abbrev Roth.normOne (P : MvPolynomial σ ℤ) : ℝ := P.l1Norm
```

Estimated cost of regeneralisation: MODERATE (def + 8 lemmas done in evidence; 5 lemmas need small typeclass edits; ℤ-call sites inside CoeffNorm.lean switch `|(c : ℝ)|` ↔ `‖c‖` via `Int.norm_eq_abs`).

Mathlib downstream this enables:
- closes the ℓ¹ TODO in `Mathlib/Analysis/Polynomial/Norm.lean` (with a univariate `Polynomial.l1Norm` companion and `supNorm ≤ l1Norm` comparison);
- `Polynomial.mahlerMeasure_le_sum_norm_coeff` and `mapMahlerMeasure_le_sum_norm_coeff` can be restated as `mahlerMeasure ≤ l1Norm`;
- submultiplicativity gives the standard Gelfond/Landau–Mignotte-type factor bounds directly.

Next action: run `/generalise Roth.normOne` targeting `MvPolynomial.l1Norm` over `[SeminormedCommRing R]` (proposed location `Mathlib/Analysis/Polynomial/Norm.lean` or a new `Mathlib/Analysis/MvPolynomial/Norm.lean`), port the CoeffNorm.lean API lemmas, keep `Roth.normOne` as the ℤ abbreviation; PR-group with the univariate `Polynomial.l1Norm`.

---

## Next step

Run `/generalise Roth.normOne` to restate it as `MvPolynomial.l1Norm` over `[SeminormedCommRing R]` (evidence file already proves the core API and the ℤ bridge), re-aim the 13 `normOne_*` lemmas in Roth/CoeffNorm.lean, then upstream together with a univariate `Polynomial.l1Norm` next to `Polynomial.supNorm`.

## Evidence
- Mathlib greps (`l1Norm`, `oneNorm`, `normOne`, `sum_norm_coeff`, norm instances on Finsupp/AddMonoidAlgebra/(Mv)Polynomial, `def .*Norm` in polynomial dirs): only `Polynomial.supNorm`, `gaussNorm`, MvPowerSeries Gauss norm; ℓ¹ TODO at `Mathlib/Analysis/Polynomial/Norm.lean:36`.
- LeanSearch / Lean-Finder / Loogle queries as in the Phase 5 block (no ℓ¹ def; `PiLp.norm_eq_of_L1` needs a Fintype index).
- WebSearch ×3 (length of polynomial; ℓ¹ group algebra; Roth expositions), local reference `clean.tex` lines 445–452.
- Evidence file `.mathlib-quality/overview/evidence/Roth.normOne/generalise_seminormedring.lean` (imports `Roth.CoeffNorm`, `Mathlib.Analysis.Normed.Ring.Int`): general `l1Norm` over `[SeminormedCommRing R]` with 9 lemmas and the bridge `l1Norm_int_eq_normOne`; `lean_diagnostic_messages`: no errors. Earlier attempts in the same file: `[SeminormedRing R]` fails (MvPolynomial needs `CommSemiring`), `p.sum` fails (no `AddMonoidAlgebra.sum` in this mathlib).
- ChatGPT MCP: n/a (not configured in this session).
