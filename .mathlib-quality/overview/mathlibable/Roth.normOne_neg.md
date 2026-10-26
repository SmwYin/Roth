---
decl: Roth.normOne_neg
file: Roth/CoeffNorm.lean
line: 86
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Standard negation-invariance lemma for the new l1 coefficient norm (analogue of mathlib's MvPowerSeries.gaussNorm_neg and lp.norm_neg); mathlib has no l1 polynomial norm and the verbatim proof compiles for MvPolynomial.l1Norm over any SeminormedCommRing (evidence file, diagnostics clean).
action: Ship as @[simp] MvPolynomial.l1Norm_neg over [SeminormedCommRing R] in the same PR as MvPolynomial.l1Norm (Mathlib/Analysis/Polynomial/Norm.lean or a new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the R = ℤ form for call site Roth/CoeffNorm.lean:127 (normOne_det_le).
---

# Roth.normOne_neg

## Inventory entry

### `theorem Roth.normOne_neg`
- **Type**: `{σ : Type*} (P : MvPolynomial σ ℤ) : Roth.normOne (-P) = Roth.normOne P`
- **What**: The ℓ¹ coefficient norm is invariant under negation, `‖-P‖₁ = ‖P‖₁`.
- **How**: `simp [normOne]` — unfolds the def to a sum over the support, then `MvPolynomial.support_neg`, `MvPolynomial.coeff_neg`, `Int.cast_neg` and `abs_neg` close it.
- **Hypotheses**: none.
- **Uses from project**: `Roth.normOne`
- **Used by**: Roth/CoeffNorm.lean:127 (`normOne_det_le`, in `simpa [h, normOne_neg]` to absorb the sign `-1` of an odd permutation). No uses outside CoeffNorm.lean (`grep -rn normOne_neg Roth/`).
- **Visibility**: public
- **Lines**: 85–87, proof length 1 line
- **Notes**: not `@[simp]`-tagged in the project (it is a natural simp lemma; mathlib form should carry `@[simp]`).

## Junk check (Step 8)
- Used anywhere? Yes, Roth/CoeffNorm.lean:127 (`normOne_det_le`).
- Wrapper of 1–2 mathlib calls? The proof is a simp composition (`support_neg`, `coeff_neg`, `abs_neg`), but that is the expected shape of a `*_neg` lemma for a new norm-like def; mathlib ships the same shape for sibling norms (`MvPowerSeries.gaussNorm_neg`, `lp.norm_neg`).
- Does mathlib have it? No — mathlib has no ℓ¹ polynomial norm (parent `Roth.normOne`); grep for `l1Norm`/`normOne_neg` over Mathlib empty.
- Too specific (inline)? No; negation invariance is basic API of any seminorm (needed for the `neg'` field of `AddGroupSeminorm`) and is used to handle the sign in the Leibniz determinant expansion.
- Well-chosen? Yes, modulo the parent's ℤ-specialisation.
- Conclusion: `KEEP` — action: keep; re-aim at the generalised `MvPolynomial.l1Norm` together with the parent def, adding `@[simp]`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.normOne_neg` not in mathlib (no `namespace Roth` in Mathlib; grep for `normOne_neg` over Mathlib empty). Not a genuine glue lemma (body is `simp [normOne]` needing `support_neg`, `coeff_neg`, `abs_neg`, not `rfl`), so a full run, assessed in the generalised setting fixed by the parent verdict (`Roth.normOne`: YES-but-generalise-first to an ℓ¹ norm on `MvPolynomial σ R`, `[SeminormedCommRing R]`).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` elaborates with no diagnostics per `lean_diagnostic_messages`)
- decl `Roth.normOne_neg`:   resolved at Roth/CoeffNorm.lean:86
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne_neg` is a theorem stating the following: for every polynomial `P ∈ ℤ[X_σ]`, the length (ℓ¹ coefficient norm) of `-P` equals that of `P`, `‖-P‖₁ = ‖P‖₁`. This is the symmetry axiom of a seminorm for the ℓ¹ coefficient norm.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the variables (implicit).
- `P : MvPolynomial σ ℤ` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `‖-P‖₁ = ‖P‖₁`.

Conclusion (Lean): `Roth.normOne (-P) = Roth.normOne P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma (negation invariance) for a helper definition; not a structure, not a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE-check skipped (theorem). Note for Phase 7: negation lemmas are standard mathlib API for norm-like functions (`MvPowerSeries.gaussNorm_neg`, `lp.norm_neg`, `norm_neg`).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | length of a polynomial sum of absolute values of coefficients L(-P) = L(P) properties | yes | `L(P) = ∑ |a_i|` (Schinzel / Dubickas length and reduced length) | `L(-P) = L(P)` immediate from the definition; Schinzel lists the analogous `l(P(-x)) = l(P(x))` for reduced length |
| 2 | WebSearch (general form) | ℓ1 norm finitely supported functions seminorm symmetric norm(-x) = norm(x) group algebra | yes | ℓ¹ / ℓ^p norm on finitely supported functions; `‖-f‖ = ‖f‖` (`lp.norm_neg`) | symmetry is a (semi)norm axiom |
| 3 | WebSearch (aliases / mathlib) | mathlib MvPowerSeries gaussNorm_neg Polynomial supNorm neg lemma | no | — | web did not index; confirmed via grep: `MvPowerSeries.gaussNorm_neg` at Mathlib/RingTheory/MvPowerSeries/GaussNorm.lean:172 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` lines 445–452 | yes | `‖f‖₁ = ∑_e |a_e|`; triangle inequality `‖f+kg‖₁ ≤ ‖f‖₁ + |k|‖g‖₁` | the `k = -1` case of the source's scaled triangle inequality uses `‖-g‖₁ = ‖g‖₁` implicitly |
| 6 | nLab | normed group / seminorm | yes | `‖-x‖ = ‖x‖` as a seminorm axiom | no polynomial-specific page |
| 7 | nCatLab | — | n/a | — | not a categorical statement (finite-sum identity) |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no coefficient norms |
| 9 | MathOverflow / Math.SE | length of polynomial L(PQ) ≤ L(P)L(Q) (via parent) | yes | same `L(P)` | negation case trivial and implicit |
| 10 | recent arXiv (last 5 years) | Pisot / length papers surfaced by #1 (arXiv 1406.0518) | yes | same `L(P)` | no competing form |

### Literature summary (Phase 3)

Concept identified as: negation invariance (symmetry) of the length / ℓ¹ coefficient (semi)norm.
Sources agree on the standard form: yes — immediate from the definition and `|−a| = |a|`.
Most general standard form: `‖-p‖₁ = ‖p‖₁` for polynomials over any seminormed coefficient ring (more generally any coefficient type with `‖-a‖ = ‖a‖`); in ℓ¹(M, R), `‖-f‖ = ‖f‖`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℝ / ℂ / any (semi)normed ring; most general standard is seminormed.
  - index set: ℕ, ℕ^σ, arbitrary monoid.
Disagreement with the literature: only the inherited ℤ / `|·|` specialisation of the parent def.

### Generality analysis — `Roth.normOne_neg`

Literature-standard form (from Phase 3): `l1Norm (-p) = l1Norm p` for `p : MvPolynomial σ R`, `[SeminormedCommRing R]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (via `normOne`) | `[SeminormedCommRing R]` | yes | proof uses only `support_neg`, `coeff_neg`, `norm_neg`; verified (`Evidence5.l1Norm_neg`) |
| 2 | norm structure | `|(· : ℝ)|` | `‖·‖` | yes | follows the parent's restatement; bridge via `Int.norm_eq_abs` compiled; floor is `[CommRing R] [Norm R]` plus `‖-a‖ = ‖a‖` (`Evidence5.l1Norm_neg_floor`), but the def's own floor is the parent's |
| 3 | `σ : Type*` | arbitrary | arbitrary | no | already maximal |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (inherited solely from the parent def's ℤ-specialisation)
Number of weakening opportunities found: 1 (ℤ → `[SeminormedCommRing R]` via the parent def)
Verification: `.mathlib-quality/overview/evidence/Roth.normOne_neg/general_and_composition.lean` proves `Evidence5.l1Norm_neg` over `[SeminormedCommRing R]` with the verbatim proof `simp [l1Norm]`, a composition variant `Evidence5.l1Norm_neg'` (`simp only [l1Norm, support_neg, coeff_neg, norm_neg]`), the `[CommRing R] [Norm R]` + symmetric-norm floor `Evidence5.l1Norm_neg_floor`, and an `example` recovering the exact project statement for `R = ℤ`; `lean_diagnostic_messages`: no diagnostics.
Proposed restatement:

```lean
@[simp]
theorem MvPolynomial.l1Norm_neg {σ R : Type*} [SeminormedCommRing R] (p : MvPolynomial σ R) :
    (-p).l1Norm = p.l1Norm := by
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
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ → `[SeminormedCommRing R]` (with the parent) | `neg'` field when `l1Norm` is bundled as an `AddGroupSeminorm`; `l1Norm_sub_le`/`l1Norm_sub_comm` |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general monoid? | option | `AddMonoidAlgebra R M` version, parent's unverified option | not needed by consumers |
| 8 | Concrete-via-abstract? | yes | proof uses only `support_neg`/`coeff_neg`/`norm_neg`; covered by row 5 | same proof for all coefficient rings |
| 9 | False-generalisation guard | no | for `R = ℤ` the general statement reduces to the project one (compiled `example`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.l1Norm_neg` over `[SeminormedCommRing R]` (above), mirroring `MvPowerSeries.gaussNorm_neg`.
  - Cost: CHEAP
  - Mathlib downstream this enables: `neg'` field of a future `AddGroupSeminorm` bundling of `l1Norm`; `l1Norm_sub_le` via `sub_eq_add_neg` + `l1Norm_add_le`; simp normalisation of signs (e.g. permutation signs in determinant expansions).
  - Real mathematical improvement: one negation lemma for all seminormed coefficient rings instead of a ℤ copy.

### Proof strategy — `Roth.normOne_neg`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ vs filters? | no | — | — |
| 2 | Element-wise vs point-free algebra? | no | — | — |
| 3 | Sequences vs filters? | no | — | — |
| 4 | Construction vs universal property? | no | — | — |
| 5 | Missing mathlib helpers? | no | `support_neg`, `coeff_neg`, `norm_neg` suffice | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.normOne_neg`

[A] Lean-Finder       "sum of norms of coefficients of negated polynomial equals that of the polynomial"   `Polynomial.signVariations_neg`, `MvPolynomial.degrees_neg`, `Polynomial.mirror_neg`; no ℓ¹ lemma
[B] Loogle            `MvPolynomial.support (-_)`   `MvPolynomial.support_neg` (building block, Mathlib/Algebra/MvPolynomial/CommRing.lean:75)
[C] LeanSearch        "norm of negation of polynomial equals norm of polynomial (coefficient norm)"   `lp.norm_neg`, `norm_neg`, `MeasureTheory.eLpNorm_neg`; no ℓ¹ polynomial lemma
[D] Grep mathlib src  `l1Norm`, `normOne_neg`, `_neg` in Analysis/Polynomial/Norm.lean and Gauss-norm files   no `l1Norm` anywhere; no `supNorm_neg`; sibling `MvPowerSeries.gaussNorm_neg` at RingTheory/MvPowerSeries/GaussNorm.lean:172; `MvPolynomial.coeff_neg` at CommRing.lean:68
[E] Name pattern      `l1Norm_neg`, `normOne_neg`   none in mathlib (lean_local_search unavailable: ripgrep not on PATH; covered by grep in [D])

Searched for both the ℤ form and the general `[SeminormedCommRing R]` form.

Concluded: found building blocks (`MvPolynomial.support_neg`, `MvPolynomial.coeff_neg`, `norm_neg`) and a sibling lemma for a different norm (`MvPowerSeries.gaussNorm_neg`); the statement concerns a def (`l1Norm`) not in mathlib.

### Normal-form check — `Roth.normOne_neg`

Equivalent formalisms: `l1Norm (-p) = l1Norm p`; `l1Norm (p - q) = l1Norm (q - p)` (corollary); `(coeff (-p)).sum (fun _ a ↦ ‖a‖) = …`.
Does mathlib already have a canonical form for this idea? yes — `norm_neg : ‖-a‖ = ‖a‖`, `MvPowerSeries.gaussNorm_neg`, `lp.norm_neg`.
RHS convention respected? yes (simp-normal: `-` removed on the RHS).

### Syntactic generality — `Roth.normOne_neg`

Alternative restatements attempted:
- current form (`p` explicit)
- `l1Norm_sub_comm : l1Norm (p - q) = l1Norm (q - p)` (a corollary, not a replacement)

Chosen restatement: current shape, with `@[simp]` added.
Justification: matches `norm_neg` / `gaussNorm_neg`; call site 127 feeds it to `simpa`.

### Superfluous-argument audit — `Roth.normOne_neg`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | coefficients in `ℤ` | no | only `support_neg`, `coeff_neg`, `norm_neg` needed; generalise with the parent |
| 2 | `σ` | yes | ambient type |
| 3 | `P` | yes | the polynomial |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (ℤ → `[SeminormedCommRing R]`, following the parent; add `@[simp]`)
Superfluous arguments: 1 to drop (the fixed coefficient ring ℤ)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.normOne_neg`

Internal use count: 0 (outside the declaring file); 1 inside CoeffNorm.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:127 (same file, in `normOne_det_le`) | `simpa [h, normOne_neg] using (normOne_prod_le Finset.univ fun i ↦ M (τ i) i).trans` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne_neg`?):
  - (none) — `grep -rn "normOne (-" Roth/` hits only the declaration itself.

### Composition check (Phase 6)

Can `Roth.normOne_neg` be derived from mathlib in ≤3 chained calls?

Attempt 1: `simp [l1Norm]` (current proof).
  - Mathlib decls used: simp set (`MvPolynomial.support_neg`, `MvPolynomial.coeff_neg`, `norm_neg`)
  - Result: succeeds, after unfolding the new def.

Attempt 2: `simp only [l1Norm, support_neg, coeff_neg, norm_neg]`.
  - Mathlib decls used: `MvPolynomial.support_neg`, `MvPolynomial.coeff_neg`, `norm_neg`
  - Result: succeeds (compiled as `Evidence5.l1Norm_neg'`)
  - Notes: only after unfolding the def mathlib lacks.

Conclusion: NOT-COMPOSABLE (as a statement about `l1Norm`, which is new; the proof is a trivial simp composition, as expected of a basic API lemma — exactly how `MvPowerSeries.gaussNorm_neg` accompanies `MvPowerSeries.gaussNorm`)

## Verdict: `Roth.normOne_neg`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): `‖-p‖₁ = ‖p‖₁` is the symmetry axiom of the ℓ¹ (semi)norm, immediate at seminormed-coefficient generality; implicit in the source's scaled triangle inequality (clean.tex 445–452).
- Generality analysis (Phase 4): STRICTLY NARROWER (via the parent's ℤ-specialisation); `Evidence5.l1Norm_neg` over `[SeminormedCommRing R]` compiles with diagnostics clean, plus a bridge `example` back to the project statement.
- Mathlib search (Phase 5): not in mathlib; sibling `MvPowerSeries.gaussNorm_neg`; building blocks `MvPolynomial.support_neg`, `MvPolynomial.coeff_neg`, `norm_neg`.
- Composition check (Phase 6): NOT-COMPOSABLE as a statement (the def is new); the proof is a three-lemma simp composition.

**Rationale:**

The parent verdict puts an ℓ¹ coefficient norm `MvPolynomial.l1Norm` over `[SeminormedCommRing R]` into mathlib, filling the TODO in `Mathlib/Analysis/Polynomial/Norm.lean:34–39` (the ℓ¹ norm, "length"). Norm-like functions in mathlib ship a negation lemma (`norm_neg`, `lp.norm_neg`, `MvPowerSeries.gaussNorm_neg`); for `l1Norm` it is the `neg'` field needed to bundle it as an `AddGroupSeminorm`, and it lets `simp` discharge signs such as the `±1` permutation sign in the Leibniz determinant expansion (call site 127, `normOne_det_le`). The ℤ restriction comes only from the parent def; the identical proof compiles for the general def.

It is a one-line theorem, not a def, so Phase 2b does not apply; as a standard API lemma accompanying a new def it is expected API, not a removable wrapper.

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (coefficient ring via the normed typeclass hierarchy), inherited from `Roth.normOne`.

Proposed restatement:
```lean
@[simp]
theorem MvPolynomial.l1Norm_neg {σ R : Type*} [SeminormedCommRing R] (p : MvPolynomial σ R) :
    (-p).l1Norm = p.l1Norm := by
  simp [l1Norm]
```

Estimated cost of regeneralisation: CHEAP (done in the evidence file).

Mathlib downstream this enables:
- `neg'` field for bundling `l1Norm` as an `AddGroupSeminorm` (then `map_neg_eq_map`, `map_sub_rev` for free);
- `l1Norm_sub_le` via `sub_eq_add_neg` and `l1Norm_add_le`;
- parallels `MvPowerSeries.gaussNorm_neg`.

PR grouping: ship in the same PR as `MvPolynomial.l1Norm` and its core API (`_nonneg`, `_eq_sum_of_support_subset`, `_zero`, `_monomial`, `norm_coeff_le_l1Norm`, `_add_le`, `_sum_le`, `_mul_le`).

Next action: run `/generalise Roth.normOne` (parent) and port this lemma as `MvPolynomial.l1Norm_neg` (adding `@[simp]`); keep the ℤ form at call site Roth/CoeffNorm.lean:127.

---

## Next step

Port as `@[simp] MvPolynomial.l1Norm_neg` together with the parent def `MvPolynomial.l1Norm` over `[SeminormedCommRing R]` (proof verbatim), proposed location `Mathlib/Analysis/Polynomial/Norm.lean` or a new `Mathlib/Analysis/MvPolynomial/Norm.lean`.

## Evidence
- WebSearch ×3 (length of a polynomial / L(-P); ℓ¹ norm on finitely supported functions / symmetry; mathlib gaussNorm_neg / supNorm neg): standard form confirmed, no mathlib ℓ¹ polynomial norm. Sources: https://projecteuclid.org/journals/functiones-et-approximatio-commentarii-mathematici/volume-35/issue-none/On-the-reduced-length-of-a-polynomial-with-real-coefficients/10.7169/facm/1229442629.pdf, https://arxiv.org/pdf/1406.0518, https://florisvandoorn.com/carleson/docs/Mathlib/Analysis/Normed/Lp/lpSpace.html
- Lean-Finder, Loogle, LeanSearch queries as in the Phase 5 block: sibling `MvPowerSeries.gaussNorm_neg`; building blocks `MvPolynomial.support_neg`, `MvPolynomial.coeff_neg`, `norm_neg`.
- Mathlib grep: no `l1Norm`/`normOne_neg`; no `Polynomial.supNorm_neg`; `MvPowerSeries.gaussNorm_neg` at `Mathlib/RingTheory/MvPowerSeries/GaussNorm.lean:172`; `MvPolynomial.support_neg` at `Mathlib/Algebra/MvPolynomial/CommRing.lean:75`.
- lean_local_search: unavailable (ripgrep not on PATH); replaced by direct grep.
- New evidence file `.mathlib-quality/overview/evidence/Roth.normOne_neg/general_and_composition.lean`: general lemma over `[SeminormedCommRing R]`, `support_neg`/`coeff_neg`/`norm_neg` composition variant, `[Norm R]` + symmetric-norm floor, and `R = ℤ` bridge `example`; `lean_diagnostic_messages` reports no diagnostics.
- Local reference `.mathlib-quality/references/clean.tex` lines 445–452 checked.
- ChatGPT MCP: n/a (not configured in this session).
