---
decl: Roth.abs_coeff_le_normOne
file: Roth/CoeffNorm.lean
line: 71
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Basic coefficient-domination lemma for the new l1 coefficient norm (exact analogue of mathlib's Polynomial.le_supNorm and Polynomial.le_gaussNorm); mathlib has no l1 polynomial norm, and the project's one-call proof via Finsupp.single_eval_le_sum compiles verbatim for MvPolynomial.l1Norm over any SeminormedCommRing (evidence file, diagnostics clean).
action: Ship as MvPolynomial.norm_coeff_le_l1Norm (or le_l1Norm, mirroring Polynomial.le_supNorm) over [SeminormedCommRing R] in the same PR as MvPolynomial.l1Norm (Mathlib/Analysis/Polynomial/Norm.lean or a new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the ℤ form for the call site Roth/CoeffNorm.lean:266 via Int.norm_eq_abs.
---

# Roth.abs_coeff_le_normOne

## Inventory entry

### `theorem Roth.abs_coeff_le_normOne`
- **Type**: `{σ : Type*} (P : MvPolynomial σ ℤ) (d : σ →₀ ℕ) : |((P.coeff d : ℤ) : ℝ)| ≤ Roth.normOne P`
- **What**: Each coefficient of an integer polynomial is bounded in absolute value by the ℓ¹ coefficient norm (`|a_d| ≤ ∑_e |a_e|`).
- **How**: One term: `Finsupp.single_eval_le_sum P.coeff (g := fun z ↦ |(z : ℝ)|) (by simp) (fun _ ↦ abs_nonneg _) d` — a single summand of a sum of nonnegative terms is at most the sum (`Finsupp.single_eval_le_sum`, Mathlib/Data/Finsupp/Order.lean:165), with `g 0 = 0` by `simp` and nonnegativity by `abs_nonneg`; the RHS `Finsupp.sum` is definitionally `Roth.normOne P`.
- **Hypotheses**: none.
- **Uses from project**: `Roth.normOne`
- **Used by**: Roth/CoeffNorm.lean:266 (first step of the `calc` in `Roth.abs_coeff_det_hasseDeriv_le`, Lemma 3). No other uses project-wide (`grep -rn abs_coeff_le_normOne Roth/`).
- **Visibility**: public
- **Lines**: 69–73, proof length 1 line
- **Notes**: Explicitly requested by the source's Lean note (clean.tex:494, "Prove abc(f) ≤ ‖f‖₁").

## Junk check (Step 8)
- Used anywhere? Yes, Roth/CoeffNorm.lean:266 — the step converting the `normOne` bound of Lemma 3 into the coefficient bound actually stated.
- Wrapper of 1–2 mathlib calls? Yes (one call to `Finsupp.single_eval_le_sum`), but that is the norm for a basic API lemma of a new def; mathlib ships the same shape for the sibling coefficient norms (`Polynomial.le_supNorm`, `Polynomial.le_gaussNorm`).
- Does mathlib have it? No — no ℓ¹ polynomial norm exists in mathlib (parent `Roth.normOne`), so no lemma about it. The generic `Finsupp.single_eval_le_sum` is the building block, not the statement.
- Too specific (inline)? No: inlining needs the `g`, `hg`, `h` arguments and relies on the defeq `normOne P = P.coeff.sum …`, fragile at call sites; a named coefficient bound is basic API of any coefficient norm.
- Well-chosen? Yes, modulo the parent's ℤ / `|·|` specialisation.
- Conclusion: `KEEP` — action: keep; re-aim at `MvPolynomial.l1Norm` together with the parent def.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.abs_coeff_le_normOne` not in mathlib (no `namespace Roth` in Mathlib; grep for `abs_coeff_le`/`normOne` lemma names empty). Not a glue lemma (proof needs `Finsupp.single_eval_le_sum`, not `rfl`), so a full run in the generalised setting fixed by the parent verdict (`Roth.normOne`: YES-but-generalise-first to `MvPolynomial.l1Norm` over `[SeminormedCommRing R]`).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` has no diagnostics)
- decl `Roth.abs_coeff_le_normOne`: resolved at Roth/CoeffNorm.lean:71
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.abs_coeff_le_normOne` is a theorem stating the following: for a polynomial `P = ∑_e a_e X^e ∈ ℤ[X_σ]` and any exponent `d`, `|a_d| ≤ ‖P‖₁ = ∑_e |a_e|`. Equivalently the sup (height) norm is dominated by the ℓ¹ norm (length): `H(P) ≤ L(P)`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the variables.
- `P : MvPolynomial σ ℤ` — the polynomial.
- `d : σ →₀ ℕ` — the exponent of the coefficient.

Hypotheses (Lean side):
- none.

Conclusion (math): `|a_d| ≤ ‖P‖₁`.

Conclusion (Lean): `|((P.coeff d : ℤ) : ℝ)| ≤ Roth.normOne P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API inequality of a helper definition; not a structure, not a main result, not named.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE-check skipped (theorem). Note for Phase 7: coefficient-domination lemmas are standard mathlib API for every coefficient norm (`Polynomial.le_supNorm`, `Polynomial.le_gaussNorm`).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | length of a polynomial L(P) sum of absolute values of coefficients each coefficient bounded by length | yes | `L(P) = ∑ |a_i|` (Schinzel, reduced length papers, Funct. Approx. 2006/07) | coefficient bound immediate from the definition, used implicitly |
| 2 | WebSearch (general form) | ℓ1 norm dominates sup norm finitely supported sequence |a_i| ≤ ||a||_1 | yes | `‖x‖_∞ ≤ ‖x‖_1` for ℓ¹ sequences, constant 1 sharp | CUHK MMAT5010 solutions; Stanford ENGR207C norms notes |
| 3 | WebSearch (aliases / mathlib) | mathlib Polynomial le_supNorm norm coeff le l1 norm polynomial length | no | — | web did not index it; confirmed `Polynomial.le_supNorm` at Mathlib/Analysis/Polynomial/Norm.lean:83 by grep |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` lines 445–452 and 492–494 | yes | `abc(f) = max_e |a_e|`, `‖f‖₁ = ∑_e |a_e|`, Lean note "Prove abc(f) ≤ ‖f‖₁" | the source asks for exactly this lemma |
| 6 | nLab | normed group / ℓ^p space (Banach space) | partial | ℓ^p inclusions `ℓ¹ ⊂ ℓ^∞`, norm-decreasing | no polynomial-specific page |
| 7 | nCatLab | — | n/a | — | not a categorical statement (finite-sum inequality) |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no coefficient norms |
| 9 | MathOverflow / Math.SE | sup norm vs ℓ¹ norm of coefficients (H(P) ≤ L(P) ≤ (n+1) H(P)) | yes | `H(P) ≤ L(P)` standard comparison of height and length | used in Mahler-measure inequalities |
| 10 | recent arXiv (last 5 years) | sup-norm vs norm of coefficients (arXiv 1602.01735 surfaced in #3); polynomials with integer roots (arXiv 1911.00480, #1) | yes | same length / height comparisons | no competing form |

### Literature summary (Phase 3)

Concept identified as: domination of each coefficient (hence of the height / sup norm `H(P)`) by the length / ℓ¹ coefficient norm `L(P)`.
Sources agree on the standard form: yes — immediate from the definition; the constant 1 is sharp (monomials).
Most general standard form: for `p` over any (semi)normed coefficient ring, `‖a_d‖ ≤ ‖p‖₁`; abstractly `‖x i‖ ≤ ‖x‖_{ℓ¹}` for finitely supported `x`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℝ / ℂ / any (semi)normed ring (or any absolute value); most general is seminormed (the inequality itself only needs a nonnegative `Norm` with `‖0‖ = 0`).
  - index set: ℕ, ℕ^σ, any set.
Disagreement with the literature: only the inherited ℤ / `|·|` specialisation of the parent def.

### Generality analysis — `Roth.abs_coeff_le_normOne`

Literature-standard form (from Phase 3): `‖p.coeff d‖ ≤ l1Norm p` for `p : MvPolynomial σ R`, `[SeminormedCommRing R]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (via `normOne`) | `[SeminormedCommRing R]` | yes | proof uses only `‖0‖ = 0` and `0 ≤ ‖·‖`; verified (`Evidence80.norm_coeff_le_l1Norm`) |
| 2 | norm structure | `|(· : ℝ)|` | `‖·‖` | yes | follows the parent's restatement; bridge `Evidence80.l1Norm_int_eq_normOne` via `Int.norm_eq_abs`; a bare `[Norm R]` with `‖0‖ = 0` and nonnegativity suffices (`Evidence80.norm_coeff_le_l1Norm_norm`) but the def's own floor is the parent's |
| 3 | `σ : Type*` | arbitrary | arbitrary | no | already maximal |
| 4 | `d : σ →₀ ℕ` | arbitrary exponent | arbitrary | no | already maximal (no `d ∈ support` hypothesis) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (inherited solely from the parent def's ℤ-specialisation)
Number of weakening opportunities found: 1 (ℤ → `[SeminormedCommRing R]` via the parent def)
Verification: `.mathlib-quality/overview/evidence/Roth.abs_coeff_le_normOne/general_and_composition.lean` proves `Evidence80.norm_coeff_le_l1Norm` over `[SeminormedCommRing R]` with the project's proof verbatim (`|·|` ↦ `‖·‖`), an alternative proof `norm_coeff_le_l1Norm'` via `Finset.single_le_sum`, the `[Norm R]` floor `norm_coeff_le_l1Norm_norm`, the bridge `l1Norm_int_eq_normOne`, and an `example` recovering the exact project statement for `R = ℤ`; `lean_diagnostic_messages`: no diagnostics. (The parent evidence `.mathlib-quality/overview/evidence/Roth.normOne/generalise_seminormedring.lean` also contains a general `norm_coeff_le_l1Norm`.)
Proposed restatement:

```lean
theorem MvPolynomial.norm_coeff_le_l1Norm {σ R : Type*} [SeminormedCommRing R]
    (p : MvPolynomial σ R) (d : σ →₀ ℕ) : ‖p.coeff d‖ ≤ p.l1Norm :=
  Finsupp.single_eval_le_sum p.coeff (g := fun z ↦ ‖z‖) (by simp) (fun _ ↦ norm_nonneg _) d
```

Cost of restatement: CHEAP — proof is verbatim.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | no hypotheses | — |
| 2 | Sequences → filters? | no | finite inequality | — |
| 3 | Construction → universal property? | no | an inequality | — |
| 4 | Set predicate → bundled substructure? | no | — | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ → `[SeminormedCommRing R]` (with the parent) | `supNorm ≤ l1Norm` comparison for univariate polynomials; coefficient bounds from `l1Norm_mul_le` for every seminormed ring |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general monoid? | option | `AddMonoidAlgebra R M` version (parent's unverified option) | not needed by consumers |
| 8 | Concrete-via-abstract? | yes | proof uses only `‖0‖ = 0` and nonnegativity; covered by row 5 | same proof for all coefficient rings |
| 9 | False-generalisation guard | no | for `R = ℤ` the general statement reduces to the project one (compiled `example`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.norm_coeff_le_l1Norm` over `[SeminormedCommRing R]` (above), mirroring `Polynomial.le_supNorm`.
  - Cost: CHEAP
  - Mathlib downstream this enables: univariate companion `Polynomial.le_l1Norm` and `supNorm_le_l1Norm`; the inline `single_eval_le_sum` step in `Mathlib/NumberTheory/Height/MvPolynomial.lean:277` (coefficient ≤ sum of absolute values) becomes an instance of the named bound if `l1Norm` is stated for an absolute value; Mahler-measure coefficient bounds can be phrased through `l1Norm`.
  - Real mathematical improvement: one coefficient bound for all seminormed coefficient rings instead of a ℤ copy.

### Proof strategy — `Roth.abs_coeff_le_normOne`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ instead of filters? | no | — | — |
| 2 | Elementwise algebra instead of ideals? | no | — | — |
| 3 | Sequences instead of filters? | no | — | — |
| 4 | Construction instead of universal property? | no | — | — |
| 5 | Missing mathlib helpers? | no | uses existing `Finsupp.single_eval_le_sum` | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(One call to the exact mathlib lemma for "a summand is at most the sum of nonnegative terms"; mathlib itself uses the same lemma for the same purpose in Height/MvPolynomial.lean:277.)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.abs_coeff_le_normOne`

[A] Lean-Finder       "single coefficient bounded by l1 norm (sum of absolute values of coefficients) of polynomial"  no hits (only `cauchyBound`, `leading_coeff_le_mahlerMeasure`, `mahlerMeasure_le_sum_norm_coeff`, `norm_coeff_le_choose_mul_mahlerMeasure`)
[B] Loogle            `‖MvPolynomial.coeff _ _‖ ≤ _`  n/a: Loogle server index lacks `MvPolynomial.coeff` ("Unknown constant"); replaced by grep [D]
[C] LeanSearch        "norm of each coefficient of a multivariate polynomial is at most the sum of norms of all coefficients"  no hits (closest: `Polynomial.le_gaussNorm`, `Polynomial.mahlerMeasure_le_sum_norm_coeff`)
[D] Grep mathlib src  `l1Norm`, `abs_coeff_le`, `coeff_le_sum`, `le_sum_norm_coeff`, `normOne`, `single_eval_le_sum`, `le_supNorm`  no ℓ¹ lemma; found `Polynomial.le_supNorm` (Norm.lean:83, sup analogue), `Finsupp.single_eval_le_sum` (Data/Finsupp/Order.lean:165, building block, used inline at NumberTheory/Height/MvPolynomial.lean:277)
[E] Name pattern      `lean_local_search norm_coeff_le`  n/a: tool unavailable (ripgrep not installed); covered by grep [D]

Searched for both:
  - the user's current form (ℤ, `|·|`)
  - the literature-standard form (`‖coeff‖ ≤ ℓ¹ norm` over a seminormed ring)

Concluded: found building blocks (`Finsupp.single_eval_le_sum`); the statement itself is not in mathlib because the def `l1Norm` is not (Norm.lean:36 lists the ℓ¹ norm as a TODO).

### Normal-form check — `Roth.abs_coeff_le_normOne`

Equivalent formalisms: `‖p.coeff d‖ ≤ l1Norm p`; `supNorm p ≤ l1Norm p` (univariate); `p.coeff.sum (fun _ z ↦ ‖z‖)` inline.
Does mathlib already have a canonical form? Yes for the sibling norm: `Polynomial.le_supNorm (i) : ‖p.coeff i‖ ≤ p.supNorm`. Our statement follows that canonical shape. RHS convention respected? yes (n/a for an inequality; the named norm is on the larger side as in `le_supNorm`).

### Syntactic generality — `Roth.abs_coeff_le_normOne`

Alternative restatements attempted:
- `‖p.coeff d‖ ≤ p.l1Norm` (pointwise, explicit `d`)
- `∀ d, ‖p.coeff d‖ ≤ p.l1Norm`
- `⨆ d, ‖p.coeff d‖ ≤ p.l1Norm`
Chosen restatement: pointwise with explicit `p d`. Justification: applies directly as the first step of a `calc` (as at CoeffNorm.lean:266) and matches `Polynomial.le_supNorm`.

### Superfluous-argument audit — `Roth.abs_coeff_le_normOne`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `σ : Type*` | yes | index type |
| 2 | `P` | yes | — |
| 3 | `d` | yes | no `d ∈ support` hypothesis needed |
| 4 | ℤ coefficients (via `normOne`) | no | generalise with parent to `[SeminormedCommRing R]` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: 1 to drop (ℤ specialisation, via parent def)

Overall: RESTATE-BEFORE-SHIP (state against `MvPolynomial.l1Norm` with `‖·‖`; name `norm_coeff_le_l1Norm` or `le_l1Norm` after `Polynomial.le_supNorm`)

### Call sites — `Roth.abs_coeff_le_normOne`

Internal use count: 0 (outside the declaring file); 1 inside Roth/CoeffNorm.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:266 | `calc _ ≤ normOne (...).det := abs_coeff_le_normOne _ _` (Lemma 3, `abs_coeff_det_hasseDeriv_le`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.abs_coeff_le_normOne`?):
  - (none in the project). In mathlib, the analogous inline step `single_eval_le_sum _ v.map_zero (fun _ ↦ by positivity) _` appears at Mathlib/NumberTheory/Height/MvPolynomial.lean:277 (coefficient ≤ sum of absolute values), evidence of the API gap.

### Composition check (Phase 6)

Can `Roth.abs_coeff_le_normOne` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Finsupp.single_eval_le_sum P.coeff (g := fun z ↦ |(z : ℝ)|) (by simp) (fun _ ↦ abs_nonneg _) d` (the current proof)
  - Mathlib decls used: `Finsupp.single_eval_le_sum`, `abs_nonneg`
  - Result: succeeds, but only against the project's def `normOne` (defeq to the `Finsupp.sum`); mathlib has no `l1Norm` to state the conclusion against.
  - Notes: at call sites without the named def, one would have to restate the RHS as `P.coeff.sum fun _ z ↦ |(z : ℝ)|` (mathlib's inline idiom).

Conclusion: NOT-COMPOSABLE as a mathlib statement (the conclusion mentions a def mathlib lacks); the proof is a one-call composition, which is expected for a basic API lemma of a new def (cf. `Polynomial.le_supNorm`, a one-call `simpa` from `le_gaussNorm`).

## Verdict: `Roth.abs_coeff_le_normOne`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): `|a_d| ≤ L(P)` (height ≤ length) is the standard, immediate comparison; the source paper explicitly asks for it (clean.tex:494).
- Generality analysis (Phase 4): STRICTLY NARROWER (ℤ via the parent def); general form compiled in the evidence file.
- Mathlib search (Phase 5): not in mathlib; only the building block `Finsupp.single_eval_le_sum` and the sup analogue `Polynomial.le_supNorm`.
- Composition check (Phase 6): NOT-COMPOSABLE as a statement (depends on the new `l1Norm`).

**Rationale:**

Mathlib has a sup coefficient norm with its domination lemma `Polynomial.le_supNorm`, but no ℓ¹ coefficient norm; `Mathlib/Analysis/Polynomial/Norm.lean:36` lists the ℓ¹ norm ("length") as a TODO, and mathlib already re-derives "coefficient ≤ sum of coefficient absolute values" inline at `Mathlib/NumberTheory/Height/MvPolynomial.lean:277`. This lemma is the canonical coefficient bound for the parent's proposed `MvPolynomial.l1Norm`, and the evidence file shows its one-line proof goes through unchanged over `[SeminormedCommRing R]`, with the project's ℤ statement recovered via `Int.norm_eq_abs`. As a theorem, no one-liner exemption is needed; it is standard basic API for the new def (the zero, nonneg, monomial, triangle and submultiplicativity lemmas of the same PR come with it).

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (coefficient ring via the normed typeclass hierarchy), inherited from the parent.

Proposed restatement:
```lean
theorem MvPolynomial.norm_coeff_le_l1Norm {σ R : Type*} [SeminormedCommRing R]
    (p : MvPolynomial σ R) (d : σ →₀ ℕ) : ‖p.coeff d‖ ≤ p.l1Norm := by
  sorry  -- verbatim proof compiled in the evidence file
```

Estimated cost of regeneralisation: CHEAP.

Mathlib downstream this enables:
- univariate `Polynomial.le_l1Norm` / `supNorm_le_l1Norm` closing part of the ℓ^p TODO in Norm.lean;
- the inline step in NumberTheory/Height/MvPolynomial.lean:277 becomes a named lemma (for an absolute-value-valued variant);
- coefficient bounds of products via `l1Norm_mul_le` then `norm_coeff_le_l1Norm` (the Lemma 3 pattern) for any seminormed coefficient ring.

PR grouping: ship with `MvPolynomial.l1Norm` and its API (`l1Norm_nonneg`, `l1Norm_eq_sum_of_support_subset`, `l1Norm_monomial`, `l1Norm_zero`, `l1Norm_add_le`, `l1Norm_sum_le`, `l1Norm_mul_le`) as one PR.

Next action: run `/generalise Roth.abs_coeff_le_normOne` together with the parent `/generalise Roth.normOne`, restate as `MvPolynomial.norm_coeff_le_l1Norm`, and keep the ℤ form (or rewrite via `Int.norm_eq_abs`) at Roth/CoeffNorm.lean:266.

---

## Next step

Restate as `MvPolynomial.norm_coeff_le_l1Norm` over `[SeminormedCommRing R]` in the `MvPolynomial.l1Norm` PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean), with Roth/CoeffNorm.lean:266 using the ℤ specialisation.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.abs_coeff_le_normOne/general_and_composition.lean` (imports `Roth.CoeffNorm`, `Mathlib.Analysis.Normed.Ring.Int`): general `l1Norm`, `norm_coeff_le_l1Norm` (verbatim proof), `norm_coeff_le_l1Norm'` (alternative), `[Norm R]` floor, ℤ bridge and recovery `example`; `lean_diagnostic_messages`: no diagnostics.
- Mathlib greps: `l1Norm`, `abs_coeff_le`, `coeff_le_sum`, `le_sum_norm_coeff`, `normOne` (no ℓ¹ lemma); `single_eval_le_sum` (Data/Finsupp/Order.lean:165, used at NumberTheory/Height/MvPolynomial.lean:277); `le_supNorm` (Analysis/Polynomial/Norm.lean:83); ℓ¹ TODO at Norm.lean:36.
- LeanSearch / Lean-Finder queries as in Phase 5 (no hit); Loogle failed (unknown constant on server); lean_local_search unavailable (ripgrep missing).
- WebSearch ×3 (length of polynomial; ℓ¹ dominates sup; mathlib le_supNorm), local reference clean.tex lines 445–452, 492–494.
- ChatGPT MCP: n/a (not configured in this session).
