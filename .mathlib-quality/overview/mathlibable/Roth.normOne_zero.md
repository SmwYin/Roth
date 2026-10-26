---
decl: Roth.normOne_zero
file: Roth/CoeffNorm.lean
line: 66
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Standard simp-normal zero lemma for the new l1 coefficient norm (exact analogue of mathlib's Polynomial.supNorm_zero and Polynomial.gaussNorm_zero); mathlib has no l1 polynomial norm and the verbatim proof compiles for MvPolynomial.l1Norm over any SeminormedCommRing (evidence file, diagnostics clean).
action: Ship as @[simp] MvPolynomial.l1Norm_zero over [SeminormedCommRing R] in the same PR as MvPolynomial.l1Norm (Mathlib/Analysis/Polynomial/Norm.lean next to Polynomial.supNorm_zero, or a new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the R = ℤ form for call site Roth/CoeffNorm.lean:92.
---

# Roth.normOne_zero

## Inventory entry

### `theorem Roth.normOne_zero`
- **Type**: `{σ : Type*} : Roth.normOne (0 : MvPolynomial σ ℤ) = 0`
- **What**: The ℓ¹ coefficient norm of the zero polynomial is `0`.
- **How**: `simp [normOne]` — unfolds the def to a sum over `(0 : MvPolynomial σ ℤ).support`, which `MvPolynomial.support_zero` rewrites to `∅`, then `Finset.sum_empty`.
- **Hypotheses**: none.
- **Uses from project**: `Roth.normOne`
- **Used by**: Roth/CoeffNorm.lean:92 (`normOne_sum_le`, as `normOne_zero.le` for `Finset.le_sum_of_subadditive`); also tagged `@[simp]`, so available to any `simp` call in CoeffNorm.lean on `normOne 0`. No uses outside CoeffNorm.lean (`grep -rn normOne_zero Roth/`).
- **Visibility**: public
- **Lines**: 64–67, proof length 1 line
- **Notes**: `@[simp]`-tagged.

## Junk check (Step 8)
- Used anywhere? Yes, Roth/CoeffNorm.lean:92 (`normOne_sum_le`), plus as a simp lemma.
- Wrapper of 1–2 mathlib calls? Yes in proof (`support_zero` + `Finset.sum_empty`), but that is the norm for a `*_zero` evaluation lemma of a new def; mathlib ships exactly this shape for sibling norms (`Polynomial.supNorm_zero`, `Polynomial.gaussNorm_zero`, `MvPowerSeries.gaussNorm_zero`).
- Does mathlib have it? No — mathlib has no ℓ¹ polynomial norm (parent `Roth.normOne`).
- Too specific (inline)? No; a `@[simp]` zero lemma is basic API for any norm-like def and is needed as the `f 0 ≤ 0` input of `Finset.le_sum_of_subadditive`.
- Well-chosen? Yes, modulo the parent's ℤ-specialisation.
- Conclusion: `KEEP` — action: keep; re-aim at the generalised `MvPolynomial.l1Norm` together with the parent def.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.normOne_zero` not in mathlib (no `namespace Roth` in Mathlib; grep for `normOne_zero` over Mathlib empty). Not a genuine glue lemma (body is `simp [normOne]`, which needs `support_zero` and `Finset.sum_empty`, not `rfl`), so a full run, assessed in the generalised setting fixed by the parent verdict (`Roth.normOne`: YES-but-generalise-first to an ℓ¹ norm on `MvPolynomial σ R`, `[SeminormedCommRing R]`).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` elaborates with no diagnostics per `lean_diagnostic_messages`)
- decl `Roth.normOne_zero`:  resolved at Roth/CoeffNorm.lean:66
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne_zero` is a theorem stating the following: the zero polynomial in `ℤ[X_σ]` has length (ℓ¹ coefficient norm) `‖0‖₁ = 0`. This is the "zero" axiom of a seminorm for the ℓ¹ coefficient norm.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the variables (implicit).

Hypotheses (Lean side):
- none.

Conclusion (math): `‖0‖₁ = 0`.

Conclusion (Lean): `Roth.normOne (0 : MvPolynomial σ ℤ) = 0`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic simp API lemma (zero evaluation) for a helper definition; not a structure, not a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE-check skipped (theorem). Note for Phase 7: zero-evaluation lemmas are standard mathlib API for every coefficient norm (`Polynomial.supNorm_zero`, `Polynomial.gaussNorm_zero`).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | length of a polynomial sum of absolute values of coefficients L(P) norm properties zero polynomial | yes | `L(P) = ∑ |a_i|` (Schinzel's length; Mahler's inequalities) | `L(0) = 0` immediate from the definition, never stated explicitly |
| 2 | WebSearch (general form) | l1 norm finitely supported functions norm of zero ℓ1 group algebra seminormed ring | partial | ℓ¹ / ℓ^p norm on finitely supported functions; `‖0‖ = 0` is a norm axiom | mathlib `lp.norm_zero` docs; ring seminorm axioms |
| 3 | WebSearch (aliases / mathlib) | mathlib Polynomial supNorm_zero gaussNorm_zero Analysis Polynomial Norm | no | — | web search did not index the decls; confirmed via Loogle/grep (`Polynomial.supNorm_zero`, Norm.lean:64) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` lines 445–452 | yes | `‖f‖₁ = ∑_e |a_e|`, with `abc(0) = 0` stated for the sup analogue; "For monomials (including the zero polynomial)" | the source treats `‖0‖₁ = 0` as part of the definition |
| 6 | nLab | normed group / ℓ¹ space (Banach space) | yes | `‖0‖ = 0` as a (semi)norm axiom | no polynomial-specific page |
| 7 | nCatLab | — | n/a | — | not a categorical statement (finite-sum evaluation) |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no coefficient norms |
| 9 | MathOverflow / Math.SE | length of polynomial L(PQ) ≤ L(P)L(Q) (via parent) | yes | same `L(P)` | zero case is trivial and implicit |
| 10 | recent arXiv (last 5 years) | Mahler measure / length (arXiv 2103.07126 surfaced by #1) | yes | same `L(P)` | no competing form |

### Literature summary (Phase 3)

Concept identified as: the length (ℓ¹ coefficient norm) vanishes at the zero polynomial — the zero axiom of the ℓ¹ (semi)norm.
Sources agree on the standard form: yes — immediate from the definition.
Most general standard form: for `p = 0` over any seminormed coefficient ring, `‖p‖₁ = 0`; in ℓ¹(M, R), `‖0‖ = 0`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℝ / ℂ / any (semi)normed ring; most general is seminormed (in fact any type with a `Norm`, since the sum is empty).
  - index set: ℕ, ℕ^σ, arbitrary monoid.
Disagreement with the literature: only the inherited ℤ / `|·|` specialisation of the parent def.

### Generality analysis — `Roth.normOne_zero`

Literature-standard form (from Phase 3): `l1Norm (0 : MvPolynomial σ R) = 0`, `[SeminormedCommRing R]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (via `normOne`) | `[SeminormedCommRing R]` | yes | proof uses only `support_zero`; verified (`Evidence4.l1Norm_zero`) |
| 2 | norm structure | `|(· : ℝ)|` | `‖·‖` | yes | follows the parent's restatement; bridge via `Int.norm_eq_abs` compiled; even a bare `[Norm R]` suffices (`Evidence4.l1Norm_zero_norm`), but the def's own floor is the parent's |
| 3 | `σ : Type*` | arbitrary | arbitrary | no | already maximal |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (inherited solely from the parent def's ℤ-specialisation)
Number of weakening opportunities found: 1 (ℤ → `[SeminormedCommRing R]` via the parent def)
Verification: `.mathlib-quality/overview/evidence/Roth.normOne_zero/general_and_composition.lean` proves `Evidence4.l1Norm_zero` over `[SeminormedCommRing R]` with the verbatim proof `simp [l1Norm]`, a composition variant `Evidence4.l1Norm_zero'` (`rw [l1Norm, support_zero, Finset.sum_empty]`), the `[CommSemiring R] [Norm R]` floor `Evidence4.l1Norm_zero_norm`, and an `example` recovering the exact project statement for `R = ℤ`; `lean_diagnostic_messages`: no diagnostics. The parent evidence `.mathlib-quality/overview/evidence/Roth.normOne/generalise_seminormedring.lean:29` also contains the general `@[simp] l1Norm_zero`.
Proposed restatement:

```lean
@[simp]
theorem MvPolynomial.l1Norm_zero {σ R : Type*} [SeminormedCommRing R] :
    (0 : MvPolynomial σ R).l1Norm = 0 := by
  simp [l1Norm]
```

Cost of restatement: CHEAP — proof is verbatim.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | no hypotheses | — |
| 2 | Sequences → filters? | no | finite identity | — |
| 3 | Construction → universal property? | no | an equation | — |
| 4 | Set predicate → bundled substructure? | no | — | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ → `[SeminormedCommRing R]` (with the parent) | `l1Norm_sum_le` via `Finset.le_sum_of_subadditive`, eventual `AddGroupSeminorm` / `NormedAddCommGroup`-style packaging of `l1Norm` for every seminormed coefficient ring |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general monoid? | option | `AddMonoidAlgebra R M` version, parent's unverified option | not needed by consumers |
| 8 | Concrete-via-abstract? | yes | proof uses only `support_zero`; covered by row 5 | same proof for all coefficient rings |
| 9 | False-generalisation guard | no | for `R = ℤ` the general statement reduces to the project one (compiled `example`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.l1Norm_zero` over `[SeminormedCommRing R]` (above), mirroring `Polynomial.supNorm_zero`.
  - Cost: CHEAP
  - Mathlib downstream this enables: `l1Norm_sum_le` (zero input of `Finset.le_sum_of_subadditive`); `map_zero'` field if `l1Norm` is later bundled as an `AddGroupSeminorm`; simp normalisation of `l1Norm 0`.
  - Real mathematical improvement: one zero lemma for all seminormed coefficient rings instead of a ℤ copy.

### Proof strategy — `Roth.normOne_zero`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ vs filters? | no | — | — |
| 2 | Element-wise vs point-free algebra? | no | — | — |
| 3 | Sequences vs filters? | no | — | — |
| 4 | Construction vs universal property? | no | — | — |
| 5 | Missing mathlib helpers? | no | `support_zero` / `Finset.sum_empty` suffice | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.normOne_zero`

[A] Lean-Finder       "sum of norms of coefficients of the zero polynomial is zero"   `Polynomial.gaussNorm_zero`, `Polynomial.sum_zero_index`, `Polynomial.mahlerMeasure_zero`, `Polynomial.cauchyBound_zero`; no ℓ¹ lemma
[B] Loogle            `Polynomial.supNorm 0`   `Polynomial.supNorm_zero` (sibling sup-norm lemma, Mathlib/Analysis/Polynomial/Norm.lean:64, `[SeminormedRing A]`)
[C] LeanSearch        "norm of the zero polynomial equals zero"   `Polynomial.gaussNorm_zero`, `lp.norm_zero`, `norm_zero`, `Polynomial.gaussNorm_eq_zero_iff`; no ℓ¹ polynomial lemma
[D] Grep mathlib src  `l1Norm`, `normOne` over Mathlib/; `support_zero` in Algebra/MvPolynomial/Basic.lean; TODO block of Analysis/Polynomial/Norm.lean   no `l1Norm` anywhere (only unrelated `NormOneClass`); `MvPolynomial.support_zero` at Basic.lean:492; Norm.lean:34–39 TODO lists the ℓ¹ norm ("length")
[E] Name pattern      `l1Norm_zero`, `normOne_zero`   none in mathlib (only project/evidence decls)

Searched for both the ℤ form and the general `[SeminormedCommRing R]` form.

Concluded: found building blocks (`MvPolynomial.support_zero`, `Finset.sum_empty`) and sibling lemmas for different norms (`Polynomial.supNorm_zero`, `Polynomial.gaussNorm_zero`); the statement concerns a def (`l1Norm`) not in mathlib.

### Normal-form check — `Roth.normOne_zero`

Equivalent formalisms: `l1Norm 0 = 0`; `l1Norm p = 0` for `p = 0` (special case of a future `l1Norm_eq_zero_iff`); `(coeff 0).sum (fun _ a ↦ ‖a‖) = 0`.
Does mathlib already have a canonical form for this idea? yes — `Polynomial.supNorm_zero : (0 : A[X]).supNorm = 0`.
RHS convention respected? yes (simp-normal: `0` on the RHS).

### Syntactic generality — `Roth.normOne_zero`

Alternative restatements attempted:
- current form (no arguments, `σ` implicit)
- `l1Norm_eq_zero_iff : l1Norm p = 0 ↔ p = 0` (requires a genuine norm, not a seminorm; a separate lemma, not a replacement)

Chosen restatement: current shape, `@[simp]`.
Justification: matches `Polynomial.supNorm_zero`; call site 92 uses `.le` directly.

### Superfluous-argument audit — `Roth.normOne_zero`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | coefficients in `ℤ` | no | only `support_zero` needed; generalise with the parent |
| 2 | `σ` | yes | ambient type |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (ℤ → `[SeminormedCommRing R]`, following the parent; keep `@[simp]`)
Superfluous arguments: 1 to drop (the fixed coefficient ring ℤ)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.normOne_zero`

Internal use count: 0 (outside the declaring file); 1 explicit inside CoeffNorm.lean, plus implicit `@[simp]` availability
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:92 (same file) | `Finset.le_sum_of_subadditive normOne normOne_zero.le normOne_add_le s f` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne_zero`?):
  - (none) — `grep -rn "normOne 0\|normOne (0" Roth/` hits only the declaration itself.

### Composition check (Phase 6)

Can `Roth.normOne_zero` be derived from mathlib in ≤3 chained calls?

Attempt 1: `simp [l1Norm]` (current proof).
  - Mathlib decls used: simp set (`MvPolynomial.support_zero`, `Finset.sum_empty`)
  - Result: succeeds, after unfolding the new def.

Attempt 2: `rw [l1Norm, support_zero, Finset.sum_empty]`.
  - Mathlib decls used: `MvPolynomial.support_zero`, `Finset.sum_empty`
  - Result: succeeds (compiled as `Evidence4.l1Norm_zero'`)
  - Notes: only after unfolding the def mathlib lacks.

Conclusion: NOT-COMPOSABLE (as a statement about `l1Norm`, which is new; the proof is a trivial composition, as expected of a basic simp lemma — exactly how `Polynomial.supNorm_zero` accompanies `Polynomial.supNorm`)

## Verdict: `Roth.normOne_zero`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): `‖0‖₁ = 0` is the zero axiom of the ℓ¹ (semi)norm, immediate at seminormed-coefficient generality; the source paper builds it into the definition (clean.tex 445–452).
- Generality analysis (Phase 4): STRICTLY NARROWER (via the parent's ℤ-specialisation); `Evidence4.l1Norm_zero` over `[SeminormedCommRing R]` compiles with diagnostics clean, plus a bridge `example` back to the project statement.
- Mathlib search (Phase 5): not in mathlib; siblings `Polynomial.supNorm_zero`, `Polynomial.gaussNorm_zero`; building blocks `MvPolynomial.support_zero`, `Finset.sum_empty`.
- Composition check (Phase 6): NOT-COMPOSABLE as a statement (the def is new); the proof is a two-rewrite composition.

**Rationale:**

The parent verdict puts an ℓ¹ coefficient norm `MvPolynomial.l1Norm` over `[SeminormedCommRing R]` into mathlib, filling the TODO in `Mathlib/Analysis/Polynomial/Norm.lean:34–39` (the ℓ¹ norm, "length"). Every coefficient norm in mathlib ships a `@[simp]` zero lemma: `Polynomial.supNorm_zero` next to `Polynomial.supNorm`, `Polynomial.gaussNorm_zero` / `MvPowerSeries.gaussNorm_zero` next to the Gauss norms. The ℓ¹ version is the `f 0 ≤ 0` input to `Finset.le_sum_of_subadditive` (call site 92, `normOne_sum_le`), and the `map_zero'` field if `l1Norm` is later bundled as an `AddGroupSeminorm`. The ℤ restriction comes only from the parent def; the identical proof compiles for the general def.

It is a one-line theorem, not a def, so Phase 2b does not apply; as a standard simp lemma accompanying a new def it is expected API, not a removable wrapper.

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (coefficient ring via the normed typeclass hierarchy), inherited from `Roth.normOne`.

Proposed restatement:
```lean
@[simp]
theorem MvPolynomial.l1Norm_zero {σ R : Type*} [SeminormedCommRing R] :
    (0 : MvPolynomial σ R).l1Norm = 0 := by
  simp [l1Norm]
```

Estimated cost of regeneralisation: CHEAP (done in the evidence file).

Mathlib downstream this enables:
- `l1Norm_sum_le` via `Finset.le_sum_of_subadditive` for any seminormed coefficient ring;
- bundling `l1Norm` as an `AddGroupSeminorm` (`map_zero'`);
- parallels `Polynomial.supNorm_zero` for the univariate companion.

PR grouping: ship in the same PR as `MvPolynomial.l1Norm` and its core API (`_nonneg`, `_eq_sum_of_support_subset`, `_monomial`, `norm_coeff_le_l1Norm`, `_add_le`, `_neg`, `_sum_le`, `_mul_le`).

Next action: run `/generalise Roth.normOne` (parent) and port this lemma as `MvPolynomial.l1Norm_zero` (with `@[simp]`); keep the ℤ form at call site Roth/CoeffNorm.lean:92.

---

## Next step

Port as `@[simp] MvPolynomial.l1Norm_zero` together with the parent def `MvPolynomial.l1Norm` over `[SeminormedCommRing R]` (proof verbatim), proposed location `Mathlib/Analysis/Polynomial/Norm.lean` (next to `Polynomial.supNorm_zero`) or a new `Mathlib/Analysis/MvPolynomial/Norm.lean`.

## Evidence
- WebSearch ×3 (length of a polynomial / zero polynomial; ℓ¹ norm on finitely supported functions / norm of zero; mathlib supNorm_zero / gaussNorm_zero): standard form confirmed, no mathlib ℓ¹ polynomial norm. Sources: https://projecteuclid.org/journals/functiones-et-approximatio-commentarii-mathematici/volume-35/issue-none/On-the-reduced-length-of-a-polynomial-with-real-coefficients/10.7169/facm/1229442629.pdf, https://arxiv.org/pdf/2103.07126, https://florisvandoorn.com/carleson/docs/Mathlib/Analysis/Normed/Lp/lpSpace.html, https://math.iisc.ac.in/~gadgil/PfsProgs25doc/Mathlib/Analysis/Normed/Ring/Seminorm.html
- Lean-Finder, Loogle, LeanSearch queries as in the Phase 5 block: siblings `Polynomial.supNorm_zero`, `Polynomial.gaussNorm_zero`; building block `MvPolynomial.support_zero`.
- Mathlib grep: no `l1Norm`/`normOne_zero`; ℓ¹ norm listed as TODO in `Mathlib/Analysis/Polynomial/Norm.lean:34–39`; `supNorm_zero` at Norm.lean:64; `MvPolynomial.support_zero` at `Mathlib/Algebra/MvPolynomial/Basic.lean:492`.
- New evidence file `.mathlib-quality/overview/evidence/Roth.normOne_zero/general_and_composition.lean`: general lemma over `[SeminormedCommRing R]`, `support_zero`/`sum_empty` composition variant, `[Norm R]` floor, and `R = ℤ` bridge `example`; `lean_diagnostic_messages` reports no diagnostics.
- Local reference `.mathlib-quality/references/clean.tex` lines 445–452 checked.
- ChatGPT MCP: n/a (not configured in this session).
