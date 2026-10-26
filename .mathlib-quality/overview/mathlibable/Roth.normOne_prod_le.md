---
decl: Roth.normOne_prod_le
file: Roth/CoeffNorm.lean
line: 105
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Finite-product submultiplicativity of the l1 coefficient norm (length of a product of k polynomials) is absent from mathlib (no l1 norm on (Mv)Polynomial, Norm.lean l1 TODO); the project proof compiles verbatim for MvPolynomial over any SeminormedCommRing once a norm-of-one hypothesis is added (NormOneClass R, or the weaker norm 1 le 1), plus a hypothesis-free nonempty variant mirroring Finset.norm_prod_le' (evidence clean).
action: Ship as MvPolynomial.l1Norm_prod_le [NormOneClass R] and l1Norm_prod_le' (s.Nonempty) in the MvPolynomial.l1Norm PR next to l1Norm_mul_le (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the Z form for the call site Roth/CoeffNorm.lean:127 (normOne_det_le).
---

# Roth.normOne_prod_le

## Inventory entry

### `theorem Roth.normOne_prod_le`
- **Type**: `{σ : Type*} {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℤ) : Roth.normOne (∏ i ∈ s, f i) ≤ ∏ i ∈ s, Roth.normOne (f i)`
- **What**: The ℓ¹ coefficient norm of a finite product of integer multivariate polynomials is at most the product of their ℓ¹ norms.
- **How**: Term-mode application of `Finset.le_prod_of_submultiplicative_of_nonneg` with `f := normOne`, nonnegativity `Roth.normOne_nonneg`, `normOne 1 ≤ 1` from `Roth.normOne_monomial 0 1` (via `simpa`), and submultiplicativity `Roth.normOne_mul_le`.
- **Hypotheses**: none.
- **Uses from project**: `Roth.normOne`, `Roth.normOne_nonneg`, `Roth.normOne_monomial`, `Roth.normOne_mul_le`
- **Used by**: Roth/CoeffNorm.lean:127 (`Roth.normOne_det_le`, bounding each Leibniz term `∏ i, M (τ i) i`). No other uses (`grep -rn normOne_prod_le Roth/`).
- **Visibility**: public
- **Lines**: 103–108, proof length 3 lines
- **Notes**: Not listed in the module docstring's main results (only `normOne_mul_le`, `normOne_det_le`).

## Junk check (Step 8)
- Used anywhere? Yes: by `normOne_det_le` (hence Lemma 3, `abs_coeff_det_hasseDeriv_le`).
- Wrapper of 1–2 mathlib calls? Yes, in the sense that it is one application of `Finset.le_prod_of_submultiplicative_of_nonneg` fed with three project facts — but this is exactly the shape of mathlib's own `Finset.norm_prod_le` / `List.norm_prod_le` API lemmas, which are standard companions to `norm_mul_le`.
- Does mathlib have it? No (no ℓ¹ polynomial norm at all; see Phase 5).
- Too specific (inline)? Borderline for a single call site, but it is the canonical big-operator companion of the submultiplicativity lemma; inlining would make `normOne_det_le` noisier.
- Well-chosen? Yes, modulo the parent's ℤ / `|·|` specialisation.
- Conclusion: `KEEP` — action: keep; re-aim at `MvPolynomial.l1Norm` together with the parent and `normOne_mul_le`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.normOne_prod_le` not in mathlib (no `namespace Roth` in `Mathlib/`). Not a glue lemma (a genuine, if short, big-operator derivation, not `rfl`/unfolding). Full run in the generalised setting fixed by the parent verdict (`Roth.normOne`: YES-but-generalise-first to `MvPolynomial.l1Norm` over `[SeminormedCommRing R]`) and the sibling `Roth.normOne_mul_le` (YES-but-generalise-first).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` compiles with no output)
- decl `Roth.normOne_prod_le`: resolved at Roth/CoeffNorm.lean:105
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne_prod_le` is a theorem stating the following: for a finite family `f_i ∈ ℤ[X_σ]`, `i ∈ s`, the length (sum of absolute values of coefficients) of the product is at most the product of the lengths, `L(∏_{i∈s} f_i) ≤ ∏_{i∈s} L(f_i)`. It is the k-factor form of `L(PQ) ≤ L(P)L(Q)`, i.e. finite-product submultiplicativity of the ℓ¹ norm on the monoid algebra `ℤ[ℕ^(σ)]`; for `s = ∅` it says `L(1) ≤ 1`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variables.
- `ι : Type*`, `s : Finset ι` — index set of the factors.
- `f : ι → MvPolynomial σ ℤ` — the factors.

Hypotheses (Lean side):
- none.

Conclusion (math): `L(∏ f_i) ≤ ∏ L(f_i)`.

Conclusion (Lean): `Roth.normOne (∏ i ∈ s, f i) ≤ ∏ i ∈ s, Roth.normOne (f i)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: big-operator corollary of a helper norm's submultiplicativity; not a main result, not named, not a structure.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3 (one term-mode application)
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: check skipped (theorem). Noted for Phase 7: it is a one-call corollary, justified as standard companion API (cf. `Finset.norm_prod_le`).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | length of a product of polynomials L(P1...Pk) ≤ L(P1)...L(Pk) sum of absolute values of coefficients | partial | `L(P) = ∑ |a_i|` (Schinzel, Funct. Approx. 35, 37); Mahler 1962 J. London Math. Soc. 37 length-of-product inequality; arXiv 1606.07622 uses the bound for products of cyclotomic polynomials | k-factor form treated as immediate induction from two factors |
| 2 | WebSearch (general form) | submultiplicative norm finite product, Banach algebra, ℓ¹, unital norm one | yes | `‖a_1⋯a_n‖ ≤ ‖a_1‖⋯‖a_n‖` by induction; normalisation `‖1‖ = 1` (or `‖1‖ ≤ 1`) is a separate axiom some authors drop (nLab "Banach algebra" and nForum discussion on the norm of the identity) | confirms the empty-product case needs `‖1‖ ≤ 1` — mirrors mathlib's `NormOneClass` split |
| 3 | WebSearch (named-after / aliases) | Mahler measure / length / height of product of polynomials, Gelfond lemma several factors | yes | Gelfond–Mahler multi-factor bounds (Mahler 1962; Hindry–Silverman p. 232 via arXiv 1406.5659; arithmetic Nullstellensatz arXiv math/9911094) | these are the hard reverse inequalities; the length's forward product bound is the easy companion |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` line 495 | yes | "submultiplicativity for ‖·‖₁, then use these for the determinant" | the determinant use is exactly the k-factor product over a Leibniz term |
| 6 | nLab | Banach algebra | yes | submultiplicative norm with optional `‖1‖ ≤ 1` normalisation; ℓ¹(G) as the standard example | — |
| 7 | nCatLab | — | n/a | — | not a categorical statement |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no coefficient norms |
| 9 | MathOverflow / Math.SE | length of product of polynomials | yes | `L(f_1⋯f_k) ≤ ∏ L(f_i)` used as folklore in factor-bound discussions (as recorded for `normOne_mul_le`) | — |
| 10 | recent arXiv (last 5 years) | sparse cofactor / factor bounds (arXiv 2308.03885) | yes | same ℓ¹ product inequality | no competing form |

### Literature summary (Phase 3)

Concept identified as: finite-product submultiplicativity of the length / ℓ¹ coefficient norm; the n-factor form of the `ℓ¹(M)` Banach-algebra inequality.
Sources agree on the standard form: yes (with the usual caveat that the empty product needs `‖1‖ ≤ 1`).
Most general standard form: for a (semi)normed ring `R` with `‖1‖ ≤ 1` (or for nonempty index sets without it) and a commutative monoid `M` (commutativity needed only for the unordered `Finset` product; lists for noncommutative), `‖∏ f_i‖₁ ≤ ∏ ‖f_i‖₁` in `R[M]`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℝ / ℂ / seminormed ring — proof needs only `‖·‖₁` submultiplicative, nonnegative, and `‖1‖₁ ≤ 1`.
  - normalisation: `‖1‖ = 1`, `‖1‖ ≤ 1`, or none (then nonempty products only).
  - index monoid: ℕ^σ (MvPolynomial), ℕ, any commutative monoid.
Disagreement with the literature: only the inherited ℤ / `|·|` specialisation.

### Generality analysis — `Roth.normOne_prod_le`

Literature-standard form (from Phase 3): `l1Norm (∏ i ∈ s, f i) ≤ ∏ i ∈ s, l1Norm (f i)` for `f : ι → MvPolynomial σ R`, `[SeminormedCommRing R] [NormOneClass R]`; plus a nonempty variant without `NormOneClass`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (via `normOne`) | `[SeminormedCommRing R]` | yes | project proof verbatim with `l1Norm_*`; verified (`Evidence85.l1Norm_prod_le_of_norm_one_le`) |
| 2 | norm of `1` | automatic for ℤ | `[NormOneClass R]` or `‖(1:R)‖ ≤ 1` | needed, not droppable | `l1Norm 1 = ‖(1:R)‖` (`Evidence85.l1Norm_one`) and the empty product is `1`, so for `s = ∅` the hypothesis is necessary (a seminormed ring may have `‖1‖ > 1`); weakest form `‖1‖ ≤ 1` compiled, `NormOneClass` corollary compiled |
| 3 | `s` arbitrary vs nonempty | arbitrary | nonempty variant drops row 2 | yes (option) | `Evidence85.l1Norm_prod_le'` (cons-induction with `l1Norm_mul_le`) compiles with no hypothesis on `‖1‖`, mirroring `Finset.norm_prod_le'` |
| 4 | norm structure | `|(· : ℝ)|` | `‖·‖` | yes | bridge `Evidence85.l1Norm_int_eq_normOne` via `Int.norm_eq_abs`; recovery `example` of the exact project statement compiles |
| 5 | commutativity of `R` | `ℤ` commutative | `CommMonoid (MvPolynomial σ R)` needed for `Finset.prod` | no | `MvPolynomial` requires `CommSemiring R` anyway; noncommutative `AddMonoidAlgebra` version would need a `List` form (option, as for the sibling) |
| 6 | `σ`, `ι : Type*` | arbitrary | arbitrary | no | already maximal |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (inherited from the parent def's ℤ-specialisation)
Number of weakening opportunities found: 1 primary (ℤ → `[SeminormedCommRing R]` with `[NormOneClass R]`), plus 1 companion (nonempty `s`, no norm-one hypothesis)
Verification: `.mathlib-quality/overview/evidence/Roth.normOne_prod_le/general_prod.lean` — `lake env lean` produced no output (no errors, no warnings): `l1Norm_prod_le_of_norm_one_le`, `l1Norm_prod_le` (`NormOneClass`), `l1Norm_prod_le'` (nonempty), `l1Norm_one`, ℤ bridge and recovery `example`.
Proposed restatement:

```lean
theorem MvPolynomial.l1Norm_prod_le {σ R ι : Type*} [SeminormedCommRing R] [NormOneClass R]
    (s : Finset ι) (f : ι → MvPolynomial σ R) :
    (∏ i ∈ s, f i).l1Norm ≤ ∏ i ∈ s, (f i).l1Norm

theorem MvPolynomial.l1Norm_prod_le' {σ R ι : Type*} [SeminormedCommRing R]
    (s : Finset ι) (hs : s.Nonempty) (f : ι → MvPolynomial σ R) :
    (∏ i ∈ s, f i).l1Norm ≤ ∏ i ∈ s, (f i).l1Norm
```

Cost of restatement: CHEAP — the project proof unchanged (with `l1Norm_one.trans_le norm_one.le` for `h_one`); the primed variant is a 5-line cons-induction.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | yes | the norm-one condition as `[NormOneClass R]` (mathlib idiom of `Finset.norm_prod_le`) | composes with every `NormOneClass` instance (ℝ, ℂ, ℚ_p, ℤ, …) |
| 2 | Sequences → filters? | no | finite algebraic inequality | — |
| 3 | Construction → universal property? | no | an inequality | — |
| 4 | Set predicate → bundled substructure? | no | — | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ → `[SeminormedCommRing R]` (with the parent) | determinant / product bounds for any seminormed coefficient ring |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general monoid? | option | AddMonoidAlgebra version with `List.prod` for noncommutative `R` (as offered for the sibling) | one proof for Polynomial / MvPolynomial / group rings |
| 8 | Concrete-via-abstract? | yes | the proof uses only nonnegativity, `normOne 1 ≤ 1` and submultiplicativity — i.e. `normOne` as a submultiplicative seminorm; if the parent is packaged as a `RingSeminorm` (or a `SeminormedRing` on a type synonym) the result is literally `map_prod_le`-style / `Finset.norm_prod_le` and needs no separate proof | a `RingSeminorm (MvPolynomial σ R)` packaging would make this lemma (and the sibling) free; recorded as an option for the parent `/generalise` |
| 9 | False-generalisation guard | no | for `R = ℤ` the general statement reduces to the project one (compiled `example`); the added `NormOneClass` holds for ℤ | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.l1Norm_prod_le` over `[SeminormedCommRing R] [NormOneClass R]` and `l1Norm_prod_le'` for nonempty `s` (above), exactly paralleling `Finset.norm_prod_le` / `Finset.norm_prod_le'`.
  - Cost: CHEAP
  - Mathlib downstream this enables: Leibniz determinant bound `l1Norm_det_le` for any seminormed coefficient ring; product bounds feeding Mignotte-type factor estimates together with `Polynomial.mahlerMeasure_mul` / `mahlerMeasure_le_sum_norm_coeff`; closes part of the ℓ¹ TODO in `Mathlib/Analysis/Polynomial/Norm.lean`.
  - Real mathematical improvement: one product bound for every seminormed coefficient ring, with the norm-one condition made explicit in mathlib's standard way.

### Proof strategy — `Roth.normOne_prod_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ instead of filters? | no | — | — |
| 2 | Elementwise algebra instead of ideals? | no | — | — |
| 3 | Sequences instead of filters? | no | — | — |
| 4 | Construction instead of universal property? | no | — | — |
| 5 | Missing mathlib helpers? | yes | `l1Norm_nonneg`, `l1Norm_one` (or `l1Norm_monomial`), `l1Norm_mul_le` — all in the same PR | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(A single `Finset.le_prod_of_submultiplicative_of_nonneg`, as in mathlib's own norm-product lemmas; a separate `l1Norm_one` simp lemma would replace the `simpa using normOne_monomial 0 1` step.)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.normOne_prod_le`

[A] Lean-Finder       "sum of norms of coefficients of a finite product of polynomials is at most the product of the sums of norms of coefficients"  no hits (only `Polynomial.mahlerMeasure_mul`, degree-of-product lemmas `natDegree_prod_le`, `MvPolynomial.degrees_prod_le`)
[B] Loogle            `MvPolynomial.coeff, Finset.prod, Norm.norm`  n/a: loogle rejected the query (unknown identifier in its index); covered by [C]/[D]
[C] LeanSearch        "l1 norm of coefficients of a product of finitely many multivariate polynomials is at most product of l1 norms"  no polynomial hit; returned the abstract analogues `Finset.norm_prod_le` ([NormOneClass]), `Finset.norm_prod_le'` (nonempty), `Finset.nnnorm_prod_le(')` — which apply to a `NormedCommRing` instance, which `MvPolynomial` does not have
[D] Grep mathlib src  `l1Norm`, `normOne_prod`, `sum_norm_coeff`, `gaussNorm_prod`, `supNorm_prod`, `l1Norm_prod`, `namespace Roth`  no ℓ¹ polynomial norm (only `mahlerMeasure_le_sum_norm_coeff` in MahlerMeasure.lean); ℓ¹ ("length") TODO at Analysis/Polynomial/Norm.lean:34–38; no `namespace Roth`
[E] Name pattern      `l1Norm_prod_le`, `normOne_prod_le` (grep, plus the leansearch name hits above)  no hits

Searched for both:
  - the user's current form (ℤ, `|·|`)
  - the literature-standard form (ℓ¹ on (Mv)Polynomial over a seminormed ring; abstract submultiplicative-norm product)

Concluded: found building blocks (`Finset.le_prod_of_submultiplicative_of_nonneg`; `Finset.norm_prod_le` would apply only if an ℓ¹ normed-ring instance existed); the ℓ¹ form itself is not in mathlib.

### Normal-form check — `Roth.normOne_prod_le`

Equivalent formalisms: `l1Norm (∏ i ∈ s, f i) ≤ ∏ i ∈ s, l1Norm (f i)`; `List`/`Multiset` versions; the instance of `Finset.norm_prod_le` for an ℓ¹ `NormedCommRing` type synonym.
Does mathlib already have a canonical form? Yes for norms: `Finset.norm_prod_le` / `Finset.norm_prod_le'`. Our statement matches their shape (explicit `s f`, `∏ ‖f i‖` on the RHS). RHS convention respected? n/a (inequality).

### Syntactic generality — `Roth.normOne_prod_le`

Alternative restatements attempted:
- `[NormOneClass R]` form, any `s` (compiled)
- `‖(1 : R)‖ ≤ 1` hypothesis form (compiled; slightly more general but not idiomatic)
- nonempty `s`, no norm-one assumption (compiled)
Chosen restatement: the `NormOneClass` form plus the primed nonempty form. Justification: these are exactly mathlib's `Finset.norm_prod_le` / `Finset.norm_prod_le'` conventions; the ℤ call site gets `NormOneClass ℤ` by instance.

### Superfluous-argument audit — `Roth.normOne_prod_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `σ`, `ι` | yes | index types |
| 2 | `s`, `f` | yes | — |
| 3 | ℤ coefficients (via `normOne`) | no | generalise with parent to `[SeminormedCommRing R]` |
| 4 | (new) `[NormOneClass R]` | yes for empty `s` | necessary since `l1Norm 1 = ‖1‖`; droppable only in the nonempty variant |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (add the `NormOneClass` / nonempty pair, following `Finset.norm_prod_le(')`)
Superfluous arguments: 1 to drop (ℤ specialisation, via parent def)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.normOne_prod_le`

Internal use count: 0 outside the declaring file; 1 inside Roth/CoeffNorm.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:127 | `simpa [h, normOne_neg] using (normOne_prod_le Finset.univ fun i ↦ M (τ i) i).trans ...` (`normOne_det_le`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne_prod_le`?):
  - (none; `grep -rn "le_prod_of_submultiplicative" Roth/` hits only CoeffNorm.lean:107, the declaration itself).

Note: K = 1, which leans toward inlining; but the lemma is the standard big-operator companion of submultiplicativity (mathlib ships `Finset.norm_prod_le` alongside `norm_mul_le` for the same reason), so it is canonical API rather than a wrong abstraction.

### Composition check (Phase 6)

Can `Roth.normOne_prod_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Finset.norm_prod_le s f` for an ℓ¹ normed ring
  - Mathlib decls used: `Finset.norm_prod_le`
  - Result: fails — mathlib has no ℓ¹ `NormedCommRing` (or any norm) instance on `MvPolynomial`.
Attempt 2: `Finset.le_prod_of_submultiplicative_of_nonneg l1Norm l1Norm_nonneg h_one l1Norm_mul_le s f` (the project proof)
  - Mathlib decls used: `Finset.le_prod_of_submultiplicative_of_nonneg`
  - Result: succeeds as a one-call composition, but three of its four inputs (`l1Norm_nonneg`, `l1Norm 1 ≤ 1`, `l1Norm_mul_le`) are themselves non-mathlib (YES-but-generalise-first siblings).
  - Notes: once the sibling API lands in mathlib this becomes a one-liner over mathlib — which is precisely why it belongs in the same PR as named API (mirroring `Finset.norm_prod_le`), not as an inline at call sites outside mathlib.

Conclusion: NOT-COMPOSABLE (from current mathlib; composable only from the proposed sibling API)

## Verdict: `Roth.normOne_prod_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): k-factor length inequality `L(∏ f_i) ≤ ∏ L(f_i)`, standard (Mahler 1962; Banach-algebra normalisation `‖1‖ ≤ 1` for the empty product); requested by the source for the determinant (clean.tex:495).
- Generality analysis (Phase 4): STRICTLY NARROWER (ℤ via parent def); general `[SeminormedCommRing R] [NormOneClass R]` and nonempty variants compiled.
- Mathlib search (Phase 5): not in mathlib; only the abstract `Finset.norm_prod_le(')`, inapplicable without an ℓ¹ instance.
- Composition check (Phase 6): NOT-COMPOSABLE from current mathlib.

**Rationale:**

Mathlib has no ℓ¹ coefficient norm on `Polynomial` or `MvPolynomial` — `Mathlib/Analysis/Polynomial/Norm.lean` lists the ℓ¹ norm ("length") as an explicit TODO — so neither the two-factor nor the finite-product bound exists, and the abstract `Finset.norm_prod_le` / `Finset.norm_prod_le'` cannot be applied because `MvPolynomial` carries no norm instance. The finite-product bound is the form actually consumed by Leibniz-determinant estimates (the project's `normOne_det_le`, and Lemma 3 of the source), so it is the natural big-operator companion of `l1Norm_mul_le`, exactly as `Finset.norm_prod_le` accompanies `norm_mul_le` in mathlib.

The evidence file shows the project proof is unchanged in the general setting; the only new ingredient is the norm-of-one condition, which is genuinely necessary for the empty product (`l1Norm 1 = ‖(1 : R)‖`) and is supplied in mathlib's idiom by `[NormOneClass R]` (automatic for ℤ, ℝ, ℂ, ℚ_p). A primed variant for nonempty `s` needs no such assumption and compiled by cons-induction. One-call corollary status is acknowledged; it is justified as standard companion API. If the parent is later packaged as a `RingSeminorm` or as a `SeminormedRing` on an ℓ¹ type synonym, this lemma becomes an instance of `Finset.norm_prod_le` and could be dropped — an option for the parent `/generalise`.

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (coefficient ring via the normed hierarchy; norm-one via `NormOneClass`), inherited from the parent.

Proposed restatement:
```lean
theorem MvPolynomial.l1Norm_prod_le {σ R ι : Type*} [SeminormedCommRing R] [NormOneClass R]
    (s : Finset ι) (f : ι → MvPolynomial σ R) :
    (∏ i ∈ s, f i).l1Norm ≤ ∏ i ∈ s, (f i).l1Norm := by
  sorry  -- proof in evidence file (project proof verbatim)

theorem MvPolynomial.l1Norm_prod_le' {σ R ι : Type*} [SeminormedCommRing R]
    (s : Finset ι) (hs : s.Nonempty) (f : ι → MvPolynomial σ R) :
    (∏ i ∈ s, f i).l1Norm ≤ ∏ i ∈ s, (f i).l1Norm := by
  sorry  -- proof in evidence file (cons-induction on l1Norm_mul_le)
```

Estimated cost of regeneralisation: CHEAP.

Mathlib downstream this enables:
- `l1Norm_det_le` (Leibniz determinant bound `l! C^l`) for any seminormed coefficient ring;
- a univariate `Polynomial.l1Norm_prod_le` companion for the ℓ¹ TODO in `Mathlib/Analysis/Polynomial/Norm.lean`;
- k-factor length bounds for Mignotte-type factor estimates alongside `Polynomial.mahlerMeasure_mul`.

PR grouping: ship with `MvPolynomial.l1Norm` and its API (`l1Norm_nonneg`, `l1Norm_one`, `l1Norm_monomial`, `l1Norm_zero`, `norm_coeff_le_l1Norm`, `l1Norm_add_le`, `l1Norm_neg`, `l1Norm_sum_le`, `l1Norm_mul_le`) as one PR.

Next action: run `/generalise Roth.normOne_prod_le` together with the parent `/generalise Roth.normOne`, restate as `MvPolynomial.l1Norm_prod_le` [NormOneClass R] plus `l1Norm_prod_le'` (nonempty), and keep the ℤ form at the call site Roth/CoeffNorm.lean:127 (`normOne_det_le`).

---

## Next step

Restate as `MvPolynomial.l1Norm_prod_le` over `[SeminormedCommRing R] [NormOneClass R]` (plus the nonempty `l1Norm_prod_le'`) in the `MvPolynomial.l1Norm` PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean), with the project call site Roth/CoeffNorm.lean:127 using the ℤ specialisation.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.normOne_prod_le/general_prod.lean` (imports `Roth.CoeffNorm`, `Mathlib.Analysis.Normed.Ring.Int`; reproduces the sibling `l1Norm` API from `.mathlib-quality/overview/evidence/Roth.normOne_mul_le/general_and_composition.lean`): `l1Norm_one`, `l1Norm_prod_le_of_norm_one_le`, `l1Norm_prod_le` ([NormOneClass R]), `l1Norm_prod_le'` (nonempty, no norm-one assumption), ℤ bridge `l1Norm_int_eq_normOne`, recovery `example` of the exact project statement. `lake env lean` (single run, ~34 s): no output — no errors, no warnings.
- Mathlib greps: `l1Norm`, `normOne_prod`, `sum_norm_coeff`, `gaussNorm_prod`, `supNorm_prod`, `l1Norm_prod`, `namespace Roth`, `le_prod_of_submultiplicative` — no ℓ¹ polynomial norm; ℓ¹ TODO at Analysis/Polynomial/Norm.lean; abstract `Finset.norm_prod_le(')` at Analysis/Normed/Ring/Basic.lean:373–383.
- Lean-Finder / LeanSearch queries as in Phase 5 (no polynomial hit); Loogle query rejected by the service.
- WebSearch ×3 (length of a k-fold product; submultiplicative norm finite product and unit normalisation; Mahler/Gelfond several factors); local reference clean.tex line 495.
- ChatGPT MCP: n/a (not configured in this session).
