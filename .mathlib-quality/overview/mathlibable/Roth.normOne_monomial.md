---
decl: Roth.normOne_monomial
file: Roth/CoeffNorm.lean
line: 59
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Standard simp-style evaluation lemma for the new l1 coefficient norm (exact analogue of mathlib's Polynomial.supNorm_monomial and Polynomial.gaussNorm_monomial); mathlib has no l1 polynomial norm and the verbatim proof compiles for MvPolynomial.l1Norm over any SeminormedCommRing (evidence file, diagnostics clean).
action: Ship as MvPolynomial.l1Norm_monomial over [SeminormedCommRing R] in the same PR as MvPolynomial.l1Norm (Mathlib/Analysis/Polynomial/Norm.lean next to Polynomial.supNorm_monomial, or a new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the R = ℤ form for call sites Roth/CoeffNorm.lean:102, 108, 155.
---

# Roth.normOne_monomial

## Inventory entry

### `theorem Roth.normOne_monomial`
- **Type**: `{σ : Type*} (e : σ →₀ ℕ) (c : ℤ) : Roth.normOne (MvPolynomial.monomial e c) = |(c : ℝ)|`
- **What**: The ℓ¹ coefficient norm of the monomial `c X^e` is `|c|`.
- **How**: `classical`; rewrite with `normOne_eq_sum_of_support_subset support_monomial_subset` to sum over `{e}`, then `simp` (`Finset.sum_singleton`, `coeff_monomial`).
- **Hypotheses**: none.
- **Uses from project**: `Roth.normOne`, `Roth.normOne_eq_sum_of_support_subset`
- **Used by**: Roth/CoeffNorm.lean:102 (`normOne_mul_le`, as a simp lemma for the product of two monomials), Roth/CoeffNorm.lean:108 (`normOne_prod_le`, `normOne_monomial 0 1` gives `normOne 1 ≤ 1`), Roth/CoeffNorm.lean:155 (`normOne_hasseDeriv_le`, rewriting each Hasse-derivative monomial term). No uses outside CoeffNorm.lean (`grep -rn normOne_monomial Roth/`).
- **Visibility**: public
- **Lines**: 58–62, proof length 3 lines
- **Notes**: none

## Junk check (Step 8)
- Used anywhere? Yes, 3 call sites in three different lemmas of CoeffNorm.lean (102, 108, 155).
- Wrapper of 1–2 mathlib calls? It is a two-step proof (support-enlargement + `simp`), the standard evaluation lemma of a sum-over-support def on a monomial; mathlib ships exactly this shape for the sibling norms (`Polynomial.supNorm_monomial`, `Polynomial.gaussNorm_monomial`, `PowerSeries.gaussNorm_monomial`).
- Does mathlib have it? No — mathlib has no ℓ¹ polynomial norm (parent `Roth.normOne`).
- Too specific (inline)? No; inlining would duplicate the support computation at three sites, one of them inside a `simp` set.
- Well-chosen? Yes, modulo the parent's ℤ-specialisation.
- Conclusion: `KEEP` — action: keep; re-aim at the generalised `MvPolynomial.l1Norm` together with the parent def.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.normOne_monomial` not in mathlib (no `namespace Roth` in Mathlib). Not a glue lemma (proof is a support rewrite plus `simp`, not `rfl`/unfolding), so a full run, assessed in the generalised setting fixed by the parent verdict (`Roth.normOne`: YES-but-generalise-first to an ℓ¹ norm on `MvPolynomial σ R`, `[SeminormedCommRing R]`).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` elaborates with no diagnostics per `lean_diagnostic_messages`)
- decl `Roth.normOne_monomial`: resolved at Roth/CoeffNorm.lean:59
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne_monomial` is a theorem stating the following: for an exponent vector `e` and an integer `c`, the monomial `c X^e ∈ ℤ[X_σ]` has length (ℓ¹ coefficient norm) `‖c X^e‖₁ = |c|`. This holds also for `c = 0`, where both sides vanish.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the variables.
- `e : σ →₀ ℕ` — the exponent vector.
- `c : ℤ` — the coefficient.

Hypotheses (Lean side):
- none.

Conclusion (math): `‖c X^e‖₁ = |c|`.

Conclusion (Lean): `Roth.normOne (monomial e c) = |(c : ℝ)|`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic evaluation API lemma for a helper definition; not a structure, not a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE-check skipped (theorem). Note for Phase 7: monomial-evaluation lemmas are standard mathlib API for coefficient norms (`Polynomial.supNorm_monomial`).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | length of a polynomial L(P) sum of absolute values coefficients monomial c x^e | yes | `L(P) = ∑ |a_i|` (Schinzel's length) | Schinzel, Funct. Approx. 2006/2007; OEIS A061553; `L(cX^e) = |c|` is immediate and used silently |
| 2 | WebSearch (general form) | l1 norm of single element finitely supported function / Finsupp.single ℓ1 | partial | `‖δ_a b‖₁ = ‖b‖` for the ℓ¹ norm on finitely supported functions | only building blocks (`Finsupp.support_single_ne_zero`) surfaced; identity is folklore |
| 3 | WebSearch (aliases / mathlib) | mathlib Polynomial supNorm monomial norm_monomial ℓ1 norm group algebra single | partial | no ℓ¹ polynomial norm docs; monoid-algebra `single` | confirms absence; mathlib sibling found via Loogle (`Polynomial.supNorm_monomial`) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` lines 447–452 | yes | `‖f‖₁ = ∑_e |a_e|`; "For monomials (including the zero polynomial), ‖f₁⋯f_l‖₁ = ∏‖f_ν‖₁" | the source uses the monomial evaluation implicitly in Lemma 3 |
| 6 | nLab | ℓ¹ / group algebra (Banach algebra ℓ¹(G)) | yes | `‖δ_g‖ = 1`, `‖c δ_g‖ = |c|` in ℓ¹(G) | no polynomial-specific page; the monomial is a point mass |
| 7 | nCatLab | — | n/a | — | not a categorical statement (finite-sum evaluation) |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no coefficient norms |
| 9 | MathOverflow / Math.SE | length of polynomial L(PQ) ≤ L(P)L(Q) (via parent) | yes | same `L(P)` | monomial case used as the base of submultiplicativity |
| 10 | recent arXiv (last 5 years) | ℓ¹ coefficient norm height bounds (arXiv 1911.00480 surfaced by #1) | yes | same | no competing form |

### Literature summary (Phase 3)

Concept identified as: the length (ℓ¹ coefficient norm) of a monomial equals the norm of its coefficient — the ℓ¹ norm of a point mass.
Sources agree on the standard form: yes — immediate from the definition.
Most general standard form: for `p = c X^e` over a seminormed ring, `‖p‖₁ = ‖c‖`; in ℓ¹(M, R), `‖single m c‖ = ‖c‖`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℝ / ℂ / any (semi)normed ring; most general is seminormed.
  - index set: ℕ, ℕ^σ, arbitrary monoid.
Disagreement with the literature: only the inherited ℤ / `|·|` specialisation of the parent def.

### Generality analysis — `Roth.normOne_monomial`

Literature-standard form (from Phase 3): `l1Norm (monomial e c) = ‖c‖`, `c : R`, `[SeminormedCommRing R]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (via `normOne`) | `[SeminormedCommRing R]` | yes | proof uses only `‖0‖ = 0` and the support of a monomial; verified (`Evidence3.l1Norm_monomial`) |
| 2 | `|(c : ℝ)|` | absolute value of real cast | `‖c‖` | yes | follows the parent's restatement; bridge via `Int.norm_eq_abs` compiled |
| 3 | `c ≠ 0` | not assumed | not assumed | no | already maximal (zero case holds) |
| 4 | `σ : Type*` | arbitrary | arbitrary | no | already maximal |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (inherited solely from the parent def's ℤ-specialisation)
Number of weakening opportunities found: 1 (ℤ → `[SeminormedCommRing R]` via the parent def)
Verification: `.mathlib-quality/overview/evidence/Roth.normOne_monomial/general_and_composition.lean` proves `Evidence3.l1Norm_monomial` over `[SeminormedCommRing R]` with the verbatim proof, a composition variant `Evidence3.l1Norm_monomial'` (`MvPolynomial.sum_def` + `MvPolynomial.sum_monomial_eq norm_zero`), and an `example` recovering the exact project statement for `R = ℤ`; `lean_diagnostic_messages`: no diagnostics. The parent evidence `.mathlib-quality/overview/evidence/Roth.normOne/generalise_seminormedring.lean` also contains the general `l1Norm_monomial`.
Proposed restatement:

```lean
theorem MvPolynomial.l1Norm_monomial {σ R : Type*} [SeminormedCommRing R]
    (e : σ →₀ ℕ) (c : R) : (monomial e c).l1Norm = ‖c‖ := by
  classical
  rw [l1Norm_eq_sum_of_support_subset support_monomial_subset]
  simp
```

Cost of restatement: CHEAP — proof is verbatim.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | no hypotheses | — |
| 2 | Sequences → filters? | no | finite identity | — |
| 3 | Construction → universal property? | no | an equation | — |
| 4 | Set predicate → bundled substructure? | no | — | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ → `[SeminormedCommRing R]` (with the parent) | `l1Norm_mul_le`, `l1Norm_C`, `l1Norm_X`, `l1Norm_one` for every normed coefficient ring |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general monoid? | option | `AddMonoidAlgebra R M` version (`‖single m c‖₁ = ‖c‖`), parent's unverified option | not needed by consumers |
| 8 | Concrete-via-abstract? | yes | proof uses only that a monomial has support ⊆ {e} and `‖0‖ = 0`; covered by row 5; via `Finsupp.sum` it is literally `MvPolynomial.sum_monomial_eq` (compiled) | same proof for all coefficient rings |
| 9 | False-generalisation guard | no | for `R = ℤ` the general statement reduces to the project one (compiled `example`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.l1Norm_monomial` over `[SeminormedCommRing R]` (above), mirroring `Polynomial.supNorm_monomial`.
  - Cost: CHEAP
  - Mathlib downstream this enables: monomial base case of `l1Norm_mul_le`; `l1Norm_C`, `l1Norm_X`, `l1Norm_one` corollaries (as `Polynomial.supNorm_X` follows from `supNorm_monomial`); `l1Norm_prod_le` base case.
  - Real mathematical improvement: one monomial evaluation for all seminormed coefficient rings instead of a ℤ copy.

### Proof strategy — `Roth.normOne_monomial`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ vs filters? | no | — | — |
| 2 | Element-wise vs point-free algebra? | no | — | — |
| 3 | Sequences vs filters? | no | — | — |
| 4 | Construction vs universal property? | no | — | — |
| 5 | Missing mathlib helpers? | no | `support_monomial_subset` / `sum_monomial_eq` suffice | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.normOne_monomial`

[A] Lean-Finder       "norm of coefficients of a monomial polynomial equals norm of its coefficient"   hits `Polynomial.gaussNorm_monomial`, `PowerSeries.gaussNorm_monomial`, `Polynomial.coeffs_monomial`, `Polynomial.content_monomial`; no ℓ¹ lemma
[B] Loogle            `Polynomial.supNorm, Polynomial.monomial`; `Finsupp.sum, MvPolynomial.monomial`   `Polynomial.supNorm_monomial` (sibling sup-norm lemma, Mathlib/Analysis/Polynomial/Norm.lean:74); `MvPolynomial.sum_monomial_eq` (generic building block)
[C] LeanSearch        "sum over support of monomial of a function of coefficient equals the function of the coefficient"   `MvPolynomial.sum_def`, `MvPolynomial.support_sum_monomial_coeff`, `Polynomial.as_sum_support`; no norm lemma
[D] Grep mathlib src  `l1Norm` over Mathlib/; `sum_monomial` in Algebra/MvPolynomial/Basic.lean; TODO block of Analysis/Polynomial/Norm.lean   no `l1Norm` anywhere; `sum_monomial_eq` at Basic.lean:276; Norm.lean TODO lists the ℓ¹ norm ("length")
[E] Name pattern      `l1Norm_monomial`, `normOne_monomial`   none in mathlib (only project/evidence decls)

Searched for both the ℤ form and the general `[SeminormedCommRing R]` form.

Concluded: found building blocks (`MvPolynomial.support_monomial_subset`, `MvPolynomial.sum_monomial_eq`, `MvPolynomial.sum_def`) and a sibling lemma for a different norm (`Polynomial.supNorm_monomial`); the statement concerns a def (`l1Norm`) not in mathlib.

### Normal-form check — `Roth.normOne_monomial`

Equivalent formalisms: `l1Norm (monomial e c) = ‖c‖`; `l1Norm (C c * X^e-monomial) = ‖c‖`; `(coeff (monomial e c)).sum (fun _ a ↦ ‖a‖) = ‖c‖`.
Does mathlib already have a canonical form for this idea? yes — `Polynomial.supNorm_monomial : (monomial n a).supNorm = ‖a‖` (norm of a `monomial` on the LHS, `‖a‖` on the RHS).
RHS convention respected? yes (simp-normal: the evaluated norm on the RHS).

### Syntactic generality — `Roth.normOne_monomial`

Alternative restatements attempted:
- current form with explicit `e`, `c` (current)
- implicit `{c}` as in `Polynomial.supNorm_monomial`
- separate `c ≠ 0` version (rejected: zero case holds, hypothesis unnecessary)

Chosen restatement: explicit `e`, `c`, no hypotheses; tag `@[simp]` upstream.
Justification: call site 108 instantiates `(0 : σ →₀ ℕ) 1` explicitly; explicit arguments are convenient there and harmless for `simp`/`rw` uses at 102 and 155.

### Superfluous-argument audit — `Roth.normOne_monomial`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | coefficients in `ℤ` | no | only `‖0‖ = 0` needed; generalise with the parent |
| 2 | `e`, `c` | yes | data |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (ℤ → `[SeminormedCommRing R]`, following the parent; add `@[simp]`)
Superfluous arguments: 1 to drop (the fixed coefficient ring ℤ)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.normOne_monomial`

Internal use count: 0 (outside the declaring file); 3 inside CoeffNorm.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:102 (same file) | `Finset.sum_congr rfl fun b _ ↦ by simp [normOne_monomial, abs_mul]` |
| Roth/CoeffNorm.lean:108 (same file) | `(by simpa using (normOne_monomial (0 : σ →₀ ℕ) 1).le) normOne_mul_le s f` |
| Roth/CoeffNorm.lean:155 (same file) | `rw [normOne_monomial, Int.cast_mul, Int.cast_natCast, abs_mul, Nat.abs_cast]` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne_monomial`?):
  - (none) — no other `support_monomial_subset` use in CoeffNorm.lean besides the lemma's own proof (line 61).

### Composition check (Phase 6)

Can `Roth.normOne_monomial` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [l1Norm_eq_sum_of_support_subset support_monomial_subset]; simp`.
  - Mathlib decls used: `MvPolynomial.support_monomial_subset`, simp set (`Finset.sum_singleton`, `coeff_monomial`)
  - Result: succeeds (current proof), but uses the project's support-enlargement lemma about the new def.

Attempt 2: `rw [l1Norm, ← MvPolynomial.sum_def (b := fun _ a ↦ ‖a‖)]; exact MvPolynomial.sum_monomial_eq norm_zero`.
  - Mathlib decls used: `MvPolynomial.sum_def`, `MvPolynomial.sum_monomial_eq`, `norm_zero`
  - Result: succeeds (compiled as `Evidence3.l1Norm_monomial'`)
  - Notes: only after unfolding the def mathlib lacks.

Conclusion: NOT-COMPOSABLE (as a statement about `l1Norm`, which is new; the proof is a short composition, as expected of a basic API lemma — exactly how `Polynomial.supNorm_monomial` accompanies `Polynomial.supNorm`)

## Verdict: `Roth.normOne_monomial`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the length of a monomial is the norm of its coefficient (ℓ¹ norm of a point mass); standard and immediate at seminormed-coefficient generality; the source paper uses it in Lemma 3 (clean.tex 451–452).
- Generality analysis (Phase 4): STRICTLY NARROWER (via the parent's ℤ-specialisation); `Evidence3.l1Norm_monomial` over `[SeminormedCommRing R]` compiles with diagnostics clean, plus a bridge `example` back to the project statement.
- Mathlib search (Phase 5): not in mathlib; sibling `Polynomial.supNorm_monomial` for the sup norm, building block `MvPolynomial.sum_monomial_eq`.
- Composition check (Phase 6): NOT-COMPOSABLE as a statement (the def is new); the proof is a two-call composition.

**Rationale:**

The parent verdict puts an ℓ¹ coefficient norm `MvPolynomial.l1Norm` over `[SeminormedCommRing R]` into mathlib, filling the TODO in `Mathlib/Analysis/Polynomial/Norm.lean` (the ℓ¹ norm, "length"). Every coefficient norm in mathlib comes with its monomial evaluation lemma: `Polynomial.supNorm_monomial` next to `Polynomial.supNorm`, and `Polynomial.gaussNorm_monomial` / `PowerSeries.gaussNorm_monomial` next to the Gauss norms. The ℓ¹ version is the base case of submultiplicativity (call site 102), gives `l1Norm 1 = 1` (call site 108) and evaluates Hasse-derivative terms (call site 155). The ℤ restriction comes only from the parent def; the identical proof compiles for the general def.

As a three-line theorem it is not a one-liner (Phase 2b n/a). It is a companion of a new def, used at three distinct lemmas and nowhere re-derived inline, so it is real API rather than a skipped wrapper.

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (coefficient ring via the normed typeclass hierarchy), inherited from `Roth.normOne`.

Proposed restatement:
```lean
@[simp]
theorem MvPolynomial.l1Norm_monomial {σ R : Type*} [SeminormedCommRing R]
    (e : σ →₀ ℕ) (c : R) : (monomial e c).l1Norm = ‖c‖ := by
  classical
  rw [l1Norm_eq_sum_of_support_subset support_monomial_subset]
  simp
```

Estimated cost of regeneralisation: CHEAP (done in the evidence file).

Mathlib downstream this enables:
- `l1Norm_mul_le` (monomial base case), `l1Norm_C`, `l1Norm_X`, `l1Norm_one` for any seminormed coefficient ring;
- parallels `Polynomial.supNorm_monomial` for the univariate companion.

PR grouping: ship in the same PR as `MvPolynomial.l1Norm` and its core API (`_nonneg`, `_eq_sum_of_support_subset`, `_zero`, `norm_coeff_le_l1Norm`, `_add_le`, `_sum_le`, `_mul_le`).

Next action: run `/generalise Roth.normOne` (parent) and port this lemma as `MvPolynomial.l1Norm_monomial` (with `@[simp]`); keep the ℤ form at call sites Roth/CoeffNorm.lean:102, 108, 155.

---

## Next step

Port as `MvPolynomial.l1Norm_monomial` together with the parent def `MvPolynomial.l1Norm` over `[SeminormedCommRing R]` (proof verbatim), proposed location `Mathlib/Analysis/Polynomial/Norm.lean` (next to `Polynomial.supNorm_monomial`) or a new `Mathlib/Analysis/MvPolynomial/Norm.lean`.

## Evidence
- WebSearch ×3 (length of a polynomial / monomial; ℓ¹ norm of a single-point finitely supported function; mathlib supNorm/monomial/ℓ¹ group algebra): standard form confirmed, no mathlib ℓ¹ polynomial norm. Sources: https://projecteuclid.org/journals/functiones-et-approximatio-commentarii-mathematici/volume-35/issue-none/On-the-reduced-length-of-a-polynomial-with-real-coefficients/10.7169/facm/1229442629.pdf, https://oeis.org/A061553, https://arxiv.org/pdf/1911.00480, https://leansearch.net/doc/Mathlib.Data.Finsupp.Single.html
- Lean-Finder, Loogle, LeanSearch queries as in the Phase 5 block: sibling `Polynomial.supNorm_monomial`, `Polynomial.gaussNorm_monomial`; building block `MvPolynomial.sum_monomial_eq`.
- Mathlib grep: no `l1Norm`; ℓ¹ norm listed as TODO in `Mathlib/Analysis/Polynomial/Norm.lean`; `supNorm_monomial` at Norm.lean:74; `MvPolynomial.sum_monomial_eq` at `Mathlib/Algebra/MvPolynomial/Basic.lean:276`.
- New evidence file `.mathlib-quality/overview/evidence/Roth.normOne_monomial/general_and_composition.lean`: general lemma over `[SeminormedCommRing R]`, `sum_monomial_eq` composition variant, and `R = ℤ` bridge `example`; `lean_diagnostic_messages` reports no diagnostics.
- Local reference `.mathlib-quality/references/clean.tex` lines 447–452 checked.
- ChatGPT MCP: n/a (not configured in this session).
