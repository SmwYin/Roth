---
decl: Roth.normOne_add_le
file: Roth/CoeffNorm.lean
line: 77
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Triangle inequality for the l1 coefficient norm (polynomial length), basic API of the parent l1Norm which mathlib lacks (Norm.lean TODO); the project proof compiles verbatim for MvPolynomial.l1Norm over any SeminormedCommRing and also for an AbsoluteValue-based l1 norm on a CommSemiring (evidence file, diagnostics clean).
action: Ship as MvPolynomial.l1Norm_add_le over [SeminormedCommRing R] in the MvPolynomial.l1Norm PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the ℤ form for the call site Roth/CoeffNorm.lean:92 (normOne_sum_le) via Int.norm_eq_abs.
---

# Roth.normOne_add_le

## Inventory entry

### `theorem Roth.normOne_add_le`
- **Type**: `{σ : Type*} (P Q : MvPolynomial σ ℤ) : Roth.normOne (P + Q) ≤ Roth.normOne P + Roth.normOne Q`
- **What**: Triangle inequality for the ℓ¹ coefficient norm: `∑ |a_e + b_e| ≤ ∑ |a_e| + ∑ |b_e|`.
- **How**: Rewrites all three norms as sums over the common finite set `P.support ∪ Q.support` with `Roth.normOne_eq_sum_of_support_subset` (using mathlib's `MvPolynomial.support_add`, `Finset.subset_union_left/right`), merges with `Finset.sum_add_distrib`, and concludes termwise via `Finset.sum_le_sum` and `abs_add_le` (after `simp` turns `coeff_add` and the `Int.cast_add`).
- **Hypotheses**: none.
- **Uses from project**: `Roth.normOne`, `Roth.normOne_eq_sum_of_support_subset`
- **Used by**: Roth/CoeffNorm.lean:92 (`Roth.normOne_sum_le`, as the subadditivity argument of `Finset.le_sum_of_subadditive`). No other uses project-wide (`grep -rn normOne_add_le Roth/`); indirectly feeds `normOne_mul_le`, `normOne_det_le`, `normOne_hasseDeriv_le` and Lemma 3 through `normOne_sum_le`.
- **Visibility**: public
- **Lines**: 75–83, proof length 7 lines
- **Notes**: Explicitly requested by the source (clean.tex:450 "The triangle inequality gives …", clean.tex:494 Lean note "Prove … the triangle inequality").

## Junk check (Step 8)
- Used anywhere? Yes, Roth/CoeffNorm.lean:92 (`normOne_sum_le`), which in turn drives submultiplicativity and the determinant bound.
- Wrapper of 1–2 mathlib calls? No: a 5-step support-padding argument; no single mathlib lemma gives it (mathlib has no ℓ¹ norm on Finsupp/MvPolynomial).
- Does mathlib have it? No (Phase 5). Mathlib does not even have `Polynomial.supNorm_add_le` for its sup norm; only `gaussNorm_add_le_max` for (Mv)PowerSeries Gauss norms (non-archimedean, different statement).
- Too specific (inline)? No: subadditivity is the input to `Finset.le_sum_of_subadditive`; basic norm API.
- Well-chosen? Yes, modulo the parent's ℤ / `|·|` specialisation.
- Conclusion: `KEEP` — action: keep; re-aim at `MvPolynomial.l1Norm` with the parent def.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.normOne_add_le` not in mathlib (no `namespace Roth` in `Mathlib/`). Not a glue lemma (genuine 7-line proof), so a full run in the generalised setting fixed by the parent verdict (`Roth.normOne`: YES-but-generalise-first to `MvPolynomial.l1Norm` over `[SeminormedCommRing R]`).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` has no diagnostics)
- decl `Roth.normOne_add_le`: resolved at Roth/CoeffNorm.lean:77
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne_add_le` is a theorem stating the following: for polynomials `P = ∑ a_e X^e`, `Q = ∑ b_e X^e` in `ℤ[X_σ]`, the length (ℓ¹ coefficient norm) is subadditive: `‖P + Q‖₁ = ∑_e |a_e + b_e| ≤ ∑_e |a_e| + ∑_e |b_e| = ‖P‖₁ + ‖Q‖₁`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the variables.
- `P Q : MvPolynomial σ ℤ` — the two polynomials.

Hypotheses (Lean side):
- none.

Conclusion (math): `L(P + Q) ≤ L(P) + L(Q)`.

Conclusion (Lean): `Roth.normOne (P + Q) ≤ Roth.normOne P + Roth.normOne Q`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API inequality (triangle inequality) of a helper definition; not a structure, not a main result, not named.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 7
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: check skipped (theorem). Note for Phase 7: a triangle inequality is standard API for every norm-like def in mathlib (`norm_add_le`, `eLpNorm_add_le`, `gaussNorm_add_le_max`).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | length of polynomial L(P+Q) ≤ L(P)+L(Q) sum of absolute values of coefficients norm triangle inequality | partial | `L(P) = ∑ |a_i|` (Schinzel, Funct. Approx. 35, 37; arXiv 1911.00480) | subadditivity used implicitly, immediate from the scalar triangle inequality; Mahler's product inequality is the multiplicative companion |
| 2 | WebSearch (general form) | ℓ1 norm finitely supported functions triangle inequality group algebra ℓ1(G) Banach algebra | yes | `ℓ¹(G)` is a Banach algebra: norm (triangle) + submultiplicative convolution | arXiv 1912.07262 (discrete group algebra = ℓ¹(Γ)); polynomials = finitely supported elements of ℓ¹(ℕ^σ) |
| 3 | WebSearch (aliases / mathlib) | mathlib polynomial l1 norm "length" Polynomial.supNorm triangle inequality | partial | 1-norm of a polynomial in the monomial basis (arXiv 2404.04190) with the triangle inequality used directly | no mathlib ℓ¹ polynomial norm indexed; only `MeasureTheory.eLpNorm_add_le` |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` lines 450 and 494 | yes | "The triangle inequality gives ‖f + k g‖₁ ≤ ‖f‖₁ + |k| ‖g‖₁"; Lean note "Prove … the triangle inequality" | the source asks for exactly this lemma |
| 6 | nLab | normed vector space / Banach space (ℓ^p) | yes | norm axioms incl. triangle inequality; ℓ¹ as the standard example | no polynomial-specific page |
| 7 | nCatLab | — | n/a | — | not a categorical statement (finite-sum inequality) |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no coefficient norms |
| 9 | MathOverflow / Math.SE | height / length of polynomials, norm properties | yes | `L` is a norm on coefficient vectors, `L(PQ) ≤ L(P)L(Q)` | standard in Mahler-measure discussions |
| 10 | recent arXiv (last 5 years) | 1-norm of polynomials in a basis (arXiv 2404.04190, from #3); polynomials with integer roots (arXiv 1911.00480, from #1) | yes | same ℓ¹ coefficient norm; triangle inequality used without comment | no competing form |

### Literature summary (Phase 3)

Concept identified as: subadditivity (triangle inequality) of the length / ℓ¹ coefficient norm `L(P)`; a special case of the ℓ¹ norm on finitely supported functions (group-algebra ℓ¹ norm).
Sources agree on the standard form: yes — it is one of the norm axioms, immediate from the scalar triangle inequality.
Most general standard form: for `p, q` over any (semi)normed coefficient ring (or with respect to any absolute value), `‖p + q‖₁ ≤ ‖p‖₁ + ‖q‖₁`; abstractly the triangle inequality in `ℓ¹(I, R)`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℝ / ℂ / any seminormed ring / any absolute value on a semiring; the proof needs only a subadditive, nonnegative, zero-preserving function on coefficients.
  - index set: ℕ, ℕ^σ, any set.
Disagreement with the literature: only the inherited ℤ / `|·|` specialisation of the parent def.

### Generality analysis — `Roth.normOne_add_le`

Literature-standard form (from Phase 3): `l1Norm (p + q) ≤ l1Norm p + l1Norm q` for `p q : MvPolynomial σ R`, `[SeminormedCommRing R]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (via `normOne`) | `[SeminormedCommRing R]` | yes | proof uses only `norm_add_le` and `‖0‖ = 0`; verified (`Evidence81.l1Norm_add_le`, verbatim proof) |
| 2 | norm structure | `|(· : ℝ)|` | `‖·‖` | yes | follows the parent restatement; bridge `Evidence81.l1Norm_int_eq_normOne` via `Int.norm_eq_abs`; recovery `example` compiles |
| 3 | negation in `R` | `ℤ` is a ring | not needed | yes (option) | `Evidence81.l1NormAbv_add_le` proves it for an `AbsoluteValue R ℝ` on any `[CommSemiring R]`, same proof with `v.add_le`; this is a parent-def design choice (cf. mathlib's `gaussNorm` parametrised by `v`), not adopted as primary target |
| 4 | `σ : Type*` | arbitrary | arbitrary | no | already maximal |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (inherited from the parent def's ℤ-specialisation)
Number of weakening opportunities found: 1 primary (ℤ → `[SeminormedCommRing R]`), plus 1 optional (absolute-value-valued ℓ¹ norm on a `CommSemiring`)
Verification: `.mathlib-quality/overview/evidence/Roth.normOne_add_le/general_and_composition.lean` — `Evidence81.l1Norm_add_le` over `[SeminormedCommRing R]` with the project proof verbatim (`abs_add_le` ↦ `norm_add_le`), the ℤ bridge, an `example` recovering the exact project statement, and `Evidence81.l1NormAbv_add_le` over `[CommSemiring R] (v : AbsoluteValue R ℝ)`; `lean_diagnostic_messages`: no diagnostics. (The parent evidence `.mathlib-quality/overview/evidence/Roth.normOne/generalise_seminormedring.lean` also contains `l1Norm_add_le`.)
Proposed restatement:

```lean
theorem MvPolynomial.l1Norm_add_le {σ R : Type*} [SeminormedCommRing R]
    (p q : MvPolynomial σ R) : (p + q).l1Norm ≤ p.l1Norm + q.l1Norm
```

Cost of restatement: CHEAP — proof is verbatim.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | no hypotheses | — |
| 2 | Sequences → filters? | no | finite inequality | — |
| 3 | Construction → universal property? | no | an inequality | — |
| 4 | Set predicate → bundled substructure? | no | — | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ → `[SeminormedCommRing R]` (with the parent) | `l1Norm_sum_le` via `Finset.le_sum_of_subadditive`, hence `l1Norm_mul_le`, for all seminormed rings |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general monoid? | option | `AddMonoidAlgebra R M` / `Finsupp` ℓ¹ norm (parent's unverified option) | not needed by consumers |
| 8 | Concrete-via-abstract? | yes | proof uses only subadditivity and `‖0‖ = 0` of the coefficient norm; covered by row 5 (and the AbsoluteValue variant) | same proof for all coefficient rings |
| 9 | False-generalisation guard | no | for `R = ℤ` the general statement reduces to the project one (compiled `example`) | — |

Further option (not proposed as the primary target): package `l1Norm` as an `AddGroupSeminorm (MvPolynomial σ R)`, of which this lemma is the `add_le'` field — enables generic seminorm API; decision belongs to the parent `/generalise`.

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.l1Norm_add_le` over `[SeminormedCommRing R]` (above).
  - Cost: CHEAP
  - Mathlib downstream this enables: `l1Norm_sum_le` (one call to `Finset.le_sum_of_subadditive`), `l1Norm_mul_le`; an `AddGroupSeminorm` packaging of `l1Norm`; univariate companion for `Polynomial`, closing the ℓ¹ TODO in `Mathlib/Analysis/Polynomial/Norm.lean`.
  - Real mathematical improvement: one triangle inequality for all seminormed coefficient rings instead of a ℤ copy.

### Proof strategy — `Roth.normOne_add_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ instead of filters? | no | — | — |
| 2 | Elementwise algebra instead of ideals? | no | — | — |
| 3 | Sequences instead of filters? | no | — | — |
| 4 | Construction instead of universal property? | no | — | — |
| 5 | Missing mathlib helpers? | no | uses `support_add`, `Finset.sum_subset`, `Finset.sum_add_distrib`, `Finset.sum_le_sum`, `abs_add_le` | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(Pad to the common support, combine, compare termwise — the standard Finset argument; no shorter route exists without an ℓ¹ norm on `Finsupp` in mathlib.)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.normOne_add_le`

[A] Lean-Finder       "triangle inequality for the l1 norm (sum of absolute values of coefficients) of polynomials"  no hits (only `cauchyBound`, `mahlerMeasure_le_sum_norm_coeff`, `gaussNorm`, `le_gaussNorm`)
[B] Loogle            `Finsupp.sum (_ + _) _ ≤ _`  no hits
[C] LeanSearch        "sum of norms of coefficients of p + q is at most sum for p plus sum for q, polynomial triangle inequality"  no hits (generic `norm_sum_le`, `Polynomial.coeff_add`)
[D] Grep mathlib src  `l1Norm`, `sum_norm_coeff`, `supNorm_add_le`, `gaussNorm_add_le`, `sum_add_index_le`, `sum_add_le` in Data/Finsupp and Algebra/MvPolynomial  no ℓ¹ lemma; only `(Mv)PowerSeries.gaussNorm_add_le_max` (non-archimedean, max form); not even `Polynomial.supNorm_add_le` exists; ℓ¹ TODO at Analysis/Polynomial/Norm.lean:34-36
[E] Name pattern      `lean_local_search l1Norm_add`  n/a: tool unavailable (ripgrep not installed); covered by grep [D]

Searched for both:
  - the user's current form (ℤ, `|·|`)
  - the literature-standard form (ℓ¹ triangle inequality over a seminormed ring / absolute value)

Concluded: not in mathlib (all 5 methods exhausted); the statement needs the def `l1Norm`, which is a documented TODO.

### Normal-form check — `Roth.normOne_add_le`

Equivalent formalisms: `l1Norm (p + q) ≤ l1Norm p + l1Norm q`; subadditivity field of an `AddGroupSeminorm`; inline `∑ ‖a_e + b_e‖ ≤ …`.
Does mathlib already have a canonical form? Yes for norms: `norm_add_le a b : ‖a + b‖ ≤ ‖a‖ + ‖b‖`; named-norm analogues `eLpNorm_add_le`, `gaussNorm_add_le_max`. Our statement follows that canonical `X_add_le` shape. RHS convention respected? yes (n/a for an inequality).

### Syntactic generality — `Roth.normOne_add_le`

Alternative restatements attempted:
- `l1Norm (p + q) ≤ l1Norm p + l1Norm q` (explicit `p q`)
- `l1Norm (p - q) ≤ l1Norm p + l1Norm q` (sub form; follows with `l1Norm_neg`)
- `l1Norm (∑ i ∈ s, f i) ≤ ∑ i ∈ s, l1Norm (f i)` (already a separate lemma, `normOne_sum_le`)
Chosen restatement: binary `add` form with explicit `p q`. Justification: it is exactly the argument `Finset.le_sum_of_subadditive` consumes (CoeffNorm.lean:92) and matches `norm_add_le`.

### Superfluous-argument audit — `Roth.normOne_add_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `σ : Type*` | yes | index type |
| 2 | `P`, `Q` | yes | — |
| 3 | ℤ coefficients (via `normOne`) | no | generalise with parent to `[SeminormedCommRing R]` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: 1 to drop (ℤ specialisation, via parent def)

Overall: RESTATE-BEFORE-SHIP (state against `MvPolynomial.l1Norm` with `‖·‖`; name `l1Norm_add_le`)

### Call sites — `Roth.normOne_add_le`

Internal use count: 0 (outside the declaring file); 1 inside Roth/CoeffNorm.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:92 | `Finset.le_sum_of_subadditive normOne normOne_zero.le normOne_add_le s f` (`normOne_sum_le`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne_add_le`?):
  - (none in the project).

### Composition check (Phase 6)

Can `Roth.normOne_add_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Finset.sum_le_sum` with `abs_add_le` directly on `normOne (P + Q)`
  - Mathlib decls used: `Finset.sum_le_sum`, `abs_add_le`
  - Result: fails — the three sums run over different supports (`(P+Q).support`, `P.support`, `Q.support`); padding to `P.support ∪ Q.support` (`support_add`, `Finset.sum_subset` ×3, `Finset.sum_add_distrib`) is needed first.
  - Notes: that padding is a genuine multi-step proof (the current 5-step `rw` + `exact`).

Attempt 2: via a mathlib ℓ¹ norm on `Finsupp` / `lp` / `PiLp 1`
  - Result: fails — no norm instance on `σ →₀ R` / `AddMonoidAlgebra`; `PiLp 1` needs a finite index; `lp` is the wrong carrier (parent Phase 6).

Conclusion: NOT-COMPOSABLE.

## Verdict: `Roth.normOne_add_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): subadditivity of the length / ℓ¹ coefficient norm is a norm axiom; the source paper uses and requests it (clean.tex:450, 494).
- Generality analysis (Phase 4): STRICTLY NARROWER (ℤ via the parent def); general form compiled verbatim in the evidence file, plus an AbsoluteValue/CommSemiring variant.
- Mathlib search (Phase 5): not in mathlib (no ℓ¹ polynomial norm; Norm.lean ℓ¹ TODO).
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Mathlib has no ℓ¹ coefficient norm on `Polynomial`/`MvPolynomial`/`Finsupp`; `Mathlib/Analysis/Polynomial/Norm.lean` lists the ℓ¹ norm ("length") as a TODO, and the only additive inequalities for coefficient norms in mathlib are the non-archimedean `gaussNorm_add_le_max` for power series. The triangle inequality is the indispensable API lemma for the parent's proposed `MvPolynomial.l1Norm`: it is what feeds `Finset.le_sum_of_subadditive` to get `l1Norm_sum_le`, and hence `l1Norm_mul_le`, the core of the Lemma 3 estimate. The evidence file shows the project's 7-line proof goes through unchanged over `[SeminormedCommRing R]` (replacing `abs_add_le` by `norm_add_le`) and recovers the exact ℤ statement via `Int.norm_eq_abs`; it even works for an ℓ¹ norm built from an `AbsoluteValue` on a commutative semiring, which the parent `/generalise` may prefer to mirror mathlib's `gaussNorm (v : F)` design.

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (coefficient ring via the normed typeclass hierarchy), inherited from the parent.

Proposed restatement:
```lean
theorem MvPolynomial.l1Norm_add_le {σ R : Type*} [SeminormedCommRing R]
    (p q : MvPolynomial σ R) : (p + q).l1Norm ≤ p.l1Norm + q.l1Norm := by
  sorry  -- verbatim proof compiled in the evidence file
```

Estimated cost of regeneralisation: CHEAP.

Mathlib downstream this enables:
- `l1Norm_sum_le` and `l1Norm_mul_le` (submultiplicativity) for every seminormed coefficient ring;
- packaging `l1Norm` as an `AddGroupSeminorm`, making generic seminorm API available;
- a univariate `Polynomial.l1Norm` companion closing the ℓ¹ TODO in Norm.lean, against which `mahlerMeasure_le_sum_norm_coeff` can be restated.

PR grouping: ship with `MvPolynomial.l1Norm` and its API (`l1Norm_nonneg`, `l1Norm_eq_sum_of_support_subset`, `l1Norm_monomial`, `l1Norm_zero`, `norm_coeff_le_l1Norm`, `l1Norm_neg`, `l1Norm_sum_le`, `l1Norm_mul_le`) as one PR.

Next action: run `/generalise Roth.normOne_add_le` together with the parent `/generalise Roth.normOne`, restate as `MvPolynomial.l1Norm_add_le`, and keep the ℤ form (via `Int.norm_eq_abs`) at its call site Roth/CoeffNorm.lean:92.

---

## Next step

Restate as `MvPolynomial.l1Norm_add_le` over `[SeminormedCommRing R]` in the `MvPolynomial.l1Norm` PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean), with `normOne_sum_le` (Roth/CoeffNorm.lean:92) using the ℤ specialisation.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.normOne_add_le/general_and_composition.lean` (imports `Roth.CoeffNorm`, `Mathlib.Analysis.Normed.Ring.Int`): general `l1Norm`, `l1Norm_add_le` (verbatim proof), ℤ bridge `l1Norm_int_eq_normOne`, recovery `example` of the exact project statement, and `l1NormAbv_add_le` for `AbsoluteValue R ℝ` on a `CommSemiring`; `lean_diagnostic_messages`: no diagnostics (first attempt had a docstring before `variable` and an unused `[Nontrivial R]`; fixed).
- Mathlib greps: `l1Norm`, `sum_norm_coeff`, `supNorm_add_le`, `gaussNorm_add_le`, `sum_add_index_le`, `sum_add_le` (only `gaussNorm_add_le_max` for power series; ℓ¹ TODO at Analysis/Polynomial/Norm.lean:34-36); no `namespace Roth` in Mathlib.
- LeanSearch / Lean-Finder / Loogle queries as in Phase 5 (no hit); lean_local_search unavailable (ripgrep missing).
- WebSearch ×3 (length triangle inequality; ℓ¹(G) group algebra; mathlib polynomial ℓ¹ norm), local reference clean.tex lines 450, 494.
- ChatGPT MCP: n/a (not configured in this session).
