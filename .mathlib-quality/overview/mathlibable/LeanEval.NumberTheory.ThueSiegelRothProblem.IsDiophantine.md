---
decl: LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine
file: Roth/LeanEval.lean
line: 16
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: IsDiophantine is the external lean-eval harness's verbatim problem predicate; a compiled bridge shows IsDiophantine x is equivalent to Irrational x and no LiouvilleWith p x for p above 2, i.e. a composition of mathlib's Irrational and LiouvilleWith (the idiom of ae_not_liouvilleWith), so the predicate itself has nothing to upstream.
action: Keep IsDiophantine unchanged in Roth/LeanEval.lean (it must match the lean-eval statement verbatim; callers isDiophantine_iff at line 43 and thueSiegelRoth at line 62); do not upstream it; if Roth is upstreamed, state it as IsAlgebraic.not_liouvilleWith next to Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean (see Roth.roth report), optionally adding the compiled bridge isDiophantine_iff_liouvilleWith to LeanEval.lean.
---

# LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine

## Inventory entry

### `def LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`
- **Type**: `(x : ℝ) : Prop`
- **What**: For every `ε > 0` there is `C > 0` such that `C / q^(2+ε) < |x - p/q|` for all integers `p` and `q > 0` (real power). This says the irrationality exponent of `x` is at most 2, with a strict uniform lower bound.
- **How**: Direct `∀ ε, 0 < ε → ∃ C, 0 < C ∧ ∀ p q, 0 < q → ...` over `Real.rpow`, `abs` and integer casts.
- **Hypotheses**: none.
- **Uses from project**: `[]`
- **Used by**: Roth/LeanEval.lean only: `isDiophantine_iff` (43, statement) and `thueSiegelRoth` (62, conclusion). It is not used in Roth/Main.lean or any other project file. `Roth.lean` does not import `Roth.LeanEval` (grep), and no other file imports it.
- **Visibility**: public
- **Lines**: 16–18, proof length 0 lines (3-line def body)
- **Notes**: Roth/LeanEval.lean is the external evaluation-harness file. Its header says it holds "the exact statement from `LeanEval/NumberTheory/ThueSiegelRoth.lean`" (leanprover/lean-eval) and that it is proved using `Roth.roth`. The def's name, namespace and body are fixed by that external statement, and the lean-eval problem page lists the "`IsDiophantine` predicate" among the pieces Mathlib lacks. Subtlety: with the strict inequality and "all `p`, `q > 0`", the predicate forces irrationality (for `x = r` take `p/q = r.num/r.den`). So the `Irrational` hypothesis of `thueSiegelRoth` is formally redundant in the conclusion direction, though it is part of the external statement.

## Junk check (Step 8)
- Used anywhere? Yes, by the two LeanEval declarations. It is the conclusion type of the harness theorem `thueSiegelRoth`.
- Wrapper of 1–2 mathlib calls? Not syntactically, but it is equivalent to a short mathlib composition: `Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x` (compiled, see Evidence).
- Does mathlib have it? Not under this name or shape (grep for `IsDiophantine`, `irrationalityExponent`, `irrationalityMeasure`, `BadlyApprox`: no hits). Mathlib states the same property as `∀ p > 2, ¬ LiouvilleWith p x` (e.g. `ae_not_liouvilleWith`, Measure.lean:115).
- Too specific (inline?)? It cannot be inlined or renamed. The harness checks the exact statement `thueSiegelRoth x _ _ : IsDiophantine x`.
- Well-chosen definition? It is the external problem's choice, and it is a faithful rendering of "irrationality measure ≤ 2". It is not the mathlib-idiomatic form.

Conclusion: KEEP. Leave it unchanged: it is externally fixed.

## Mathlibable assessment (Step 9)

Pre-filter: the def is public, its name has no `_aux` suffix, its docstring is not internal or auxiliary, and Step 8 said KEEP. Mathlib has no `LeanEval` namespace and no `IsDiophantine` (grep over `.lake/packages/mathlib/Mathlib/`). It is not a glue lemma. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the evidence file importing `Roth.LeanEval` elaborates with no diagnostics)
- decl `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`: resolved at Roth/LeanEval.lean:16
- kind:                      def
- has sorry:                 no
- module docstring summary:  the lean-eval Thue–Siegel–Roth statement, reproduced verbatim and proved from `Roth.roth`.

### Statement (Phase 1)

`IsDiophantine` is a definition. A real `x` is *Diophantine* (in the sense of the harness) if for every `ε > 0` there exists `C = C(x, ε) > 0` such that

  `|x − p/q| > C / q^{2+ε}` for all `p ∈ ℤ`, `q ∈ ℤ_{>0}`.

Equivalently, `x` is irrational and its irrationality exponent `μ(x)` is at most 2. The harness theorem says that irrational algebraic numbers are Diophantine (Roth).

Variables / typeclasses involved (Lean side):
- `x : ℝ`: the number being approximated.

Hypotheses (Lean side):
- none.

Conclusion (math): a predicate on reals.

Conclusion (Lean): n/a — definition (`∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧ ∀ (p q : ℤ), 0 < q → C / (q : ℝ) ^ ((2 : ℝ) + ε) < |x - (p : ℝ) / (q : ℝ)|`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: it is the target predicate of the external benchmark statement, but it introduces no new structure. It encodes "irrationality exponent ≤ 2", a notion mathlib already expresses through `LiouvilleWith`.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive logical line (wrapped over 2 source lines)
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | no       | `isDiophantine_iff` unfolds it freely (`h ((κ - 2) / 2) ...`, `fun h ε hε ↦ ...`); nothing relies on sealing |
| Avoid typeclass diamonds         | no       | no instances |
| Mark semantic intent / API name  | yes (external only) | the name is fixed by the lean-eval harness (`thueSiegelRoth : IsDiophantine x`). For mathlib, the stable name for this idea is the negation of `LiouvilleWith` for all `p > 2` |

Conclusion: ONE-LINER WITH-EXEMPTION (the exemption serves the external harness and does not argue for mathlib)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Diophantine number definition abs(x - p/q) > C/q^(2+epsilon) Diophantine condition of type tau | yes | "Diophantine of type τ": `x` irrational with `∃ γ > 0, ∀ p, q > 0, |x − p/q| ≥ γ/q^{2+τ}`; class `CD(τ)`, union `CD` | arXiv math/0009232 (Def. 4.6), arXiv 2603.08378, arXiv math/9912019 (Roth gives algebraic numbers in `CD(τ)` for every `τ > 0`). Small-divisor/KAM usage: non-strict `≥`, fixed `τ`, irrationality built in |
| 2 | WebSearch (general form) | irrationality exponent equal to 2, for every ε exists c(x,ε), abs(x - p/q) > c/q^(2+ε), Roth theorem statement | yes | Roth: `μ(α) = 2`; equivalently `|α − p/q| ≥ c(α, ε)/q^{2+ε}` for all `p/q` | Wikipedia "Roth's theorem"; Bugeaud arXiv 2510.02059; Waldschmidt HCMUNS10. The literature uses `≥`, and the harness's strict `<` is equivalent after halving `C` |
| 3 | WebSearch (named-after / aliases) | lean-eval ThueSiegelRoth IsDiophantine leanprover lean-eval | yes | lean-lang.org/eval/problems/thue_siegel_roth: "irrationality measure ≤ 2 for algebraic irrationals". It lists "the `IsDiophantine` predicate" as missing from Mathlib | confirms this is the harness's own predicate. Aliases in the literature: "Diophantine number", "irrationality measure ≤ 2", "not `q^{-p}`-well-approximable for `p > 2`" |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for Diophantine / irrationality / LeanEval | partial | §6 states Roth via the approximation set (eq. (1)); l.1643 points at mathlib's DiophantineApproximation module | the paper never uses the lower-bound "Diophantine" form or the name |
| 6 | nLab | Diophantine number / irrationality measure | no | — | nLab has no page on Diophantine approximation exponents |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | (results of #1, #2) | partial | "Diophantine numbers" = `⋃_τ CD(τ)`; "irrationality measure 2" | folklore, consistent with #1 and #2 |
| 10 | recent arXiv (last 5 years) | (results of #1, #2) | yes | arXiv 2603.08378 (2026, `CD(τ)`), 2510.02059 (2025), 2210.16553 (2022) | all define the property via the exponent or a type-`τ` class. None uses the "for all `ε`" bundle as a named predicate |

### Literature summary (Phase 3)

Concept identified as: irrationality exponent (Liouville–Roth irrationality measure) at most 2, i.e. `x ∈ ⋂_{τ>0} CD(τ)` in small-divisor terminology. Here `CD(τ)` is the set of Diophantine numbers of type `τ`.
Sources agree on the standard form: yes, up to `<` vs `≤` (immaterial, since `C` can be halved) and whether irrationality is stated separately (the uniform bound over all `p/q` forces it).
Most general standard form: Diophantine of type `τ` (`|x − p/q| ≥ γ q^{−2−τ}` for all `p/q`), or the irrationality exponent `μ(x) = sup{μ : |x − p/q| < q^{−μ} infinitely often}`. `IsDiophantine x` is `∀ τ > 0, x ∈ CD(τ)`, equivalently `μ(x) ≤ 2` together with irrationality.
Generality dimensions where the literature varies:
  - exponent: fixed type `τ` (KAM) vs all `τ > 0` (Roth, here) vs a general function `ψ` (badly-approximable / `ψ`-approximability).
  - packaging: a named class `CD(τ)` vs the real-valued exponent `μ(x)` vs negated "well-approximable" predicates (mathlib's `LiouvilleWith`).
Disagreement with the literature: none. The harness uses the standard Roth-lower-bound form.

### Generality analysis — `IsDiophantine`

Literature-standard form (from Phase 3): `μ(x) ≤ 2` (with `x` irrational), or `∀ τ > 0, x ∈ CD(τ)`. In mathlib vocabulary: `Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | exponent `2 + ε` for all `ε > 0` | fixed bundle "for all `ε`" | type-`τ` class `CD(τ)` with `τ` a parameter | yes, as a parametrised family, but this is a reformulation, not a weakening | parametrising by `τ` gives a different predicate. It cannot be done here because the def is fixed by the external harness |
| 2 | strict `<` | `C / q^(2+ε) < |x - p/q|` | `≥` | equivalent | halve `C` |
| 3 | `p q : ℤ`, `0 < q` | integer pairs | rationals `p/q` | equivalent | — |
| 4 | `x : ℝ` | real | real | no | real Diophantine approximation |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (as a predicate with no hypotheses; rows 1–3 are reformulations, and the def is externally fixed)
Number of weakening opportunities found: 0
Proposed restatement: none for the def. The mathlib-facing restatement of what it expresses is the `LiouvilleWith` composition (Phase 4c, compiled).
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | yes | `∀ p > 2, ¬ LiouvilleWith p x` (`LiouvilleWith` is the `∃ C, ∃ᶠ n in atTop, ...` filter form), together with `Irrational x` | the `LiouvilleWith` API (`mono`, `mul_rat_iff`, `add_rat_iff`, `irrational`, `frequently_lt_rpow_neg`) and `ae_not_liouvilleWith`, which already states the a.e. version in exactly this shape |
| 3 | construction vs universal property? | no | — | a predicate |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | real setting |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | `ℤ` numerators and denominators are standard |
| 8 | concrete-via-abstract? | no | — | no proof body |
| 9 | false-generalisation guard | no false generalisation | evidence `isDiophantine_iff_liouvilleWith` proves `IsDiophantine x ↔ Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x` with no extra hypothesis, so the reformulation is the same predicate. The `Irrational` conjunct is needed: rationals satisfy `¬ LiouvilleWith p x` for `p > 1` but fail `IsDiophantine` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes, but it is a composition of existing mathlib notions, not a new def.
  - Proposed mathlib-idiomatic restatement: `Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x` (and for Roth: `∀ p > 2, ¬ LiouvilleWith p x` for algebraic `x`, as in the Roth.roth report).
  - Cost: CHEAP (bridge compiled, about 40 lines including the copied `approxSet` bridges).
  - Mathlib downstream this enables: it lines up with `ae_not_liouvilleWith` (Measure.lean:115) and the whole `LiouvilleWith` API, with no new predicate.
  - Real mathematical improvement: no new name for a notion mathlib already has. A named exponent `irrationalityExponent : ℝ → ℝ≥0∞` would be a separate, larger contribution, unrelated to this def.

### Proof strategy — `IsDiophantine`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | yes | the explicit `∀ ε ∃ C ∀ p q` bound is the complement of the filter-form `LiouvilleWith` | n/a: the def is externally fixed. The bridge is CHEAP |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | bridges between "uniform lower bound for all `p/q`" and `¬ LiouvilleWith` (mathlib only has `LiouvilleWith.frequently_lt_rpow_neg` and `Liouville.exists_pos_real_of_irrational_root`, the latter having this exact lower-bound shape for degree-`d` exponents) | follow-up only if Roth is upstreamed |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (a definition with no proof; as a faithful copy of the external statement it is correct as is)

### Diamond / defeq risk — `IsDiophantine`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | no instances defined; it uses only `ℝ` order, `abs`, `Real.rpow` and `ℤ → ℝ` casts |
| 2 | Reducibility leak | none | plain semireducible def. `isDiophantine_iff` and the evidence apply it directly to `ε` (`h 1 one_pos`), which is the intended use |
| 3 | Non-canonical unfolding | low | `C / q ^ (2 + ε)` with `q : ℤ` cast to `ℝ` (mathlib's `LiouvilleWith` uses `n : ℕ`). The evidence needs one `Int.cast_natCast` / `lift` step |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | monomorphic |
| 6 | Coercion ambiguity | none | standard casts only |

### Risk verdict (Phase 4.5)

Overall risk: NONE
Top risks: none
Recommended mitigations: n/a

### Mathlib search-status: `IsDiophantine`

[A] Lean-Finder       "real x such that for every ε > 0 there is C > 0 with |x - p/q| > C/q^(2+ε) for all p q; irrationality measure at most 2"   hits: `Liouville`, `LiouvilleWith`, `forall_liouvilleWith_iff`, `ae_not_liouvilleWith`, `LiouvilleWith.irrational`, `Liouville.irrational`
[B] Loogle            `|_ - (_ : ℝ) / _|, Irrational`   hits: `Liouville.exists_pos_real_of_irrational_root` (Liouville's lower bound `1 ≤ (b+1)^d · |α − a/(b+1)| · A`, the same shape with exponent `d`)
[C] LeanSearch        "Diophantine number: uniform lower bound C / q^(2+ε) on |x - p/q| for all rationals"   hits: `LiouvilleWith`, `Liouville`, `Liouville.liouvilleWith`, `Liouville.frequently_exists_num`, `Liouville.transcendental`, `Irrational.eventually_forall_le_dist_cast_div`
[D] Grep mathlib src  `IsDiophantine`, `irrationalityMeasure`, `irrationalityExponent`, `BadlyApprox`, `badlyApprox`, `namespace LeanEval`: no hits. `def LiouvilleWith` (NumberTheory/Transcendental/Liouville/LiouvilleWith.lean:51); `ae_not_liouvilleWith : ∀ᵐ x, ∀ p > (2 : ℝ), ¬LiouvilleWith p x` (Liouville/Measure.lean:115)
[E] Name pattern      `lean_local_search IsDiophantine`: n/a (ripgrep not installed for the LSP tool); replaced by grep [D] and project grep (only Roth/LeanEval.lean)

Searched for both the harness form (uniform lower bound for all `ε`) and the literature-standard form (irrationality exponent ≤ 2 / `CD(τ)`).

Concluded: found building blocks (`Irrational`, `LiouvilleWith`); composition would yield our form, with the `ae_not_liouvilleWith` idiom `∀ p > 2, ¬ LiouvilleWith p x`. Mathlib has no `IsDiophantine` and no irrationality-exponent def.

### Normal-form check — `IsDiophantine`

Equivalent formalisms: (a) the harness's uniform lower bound; (b) `∀ κ, (Roth.approxSet x κ).Infinite → κ ≤ 2` for irrational `x` (`isDiophantine_iff`); (c) `Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x` (evidence); (d) `μ(x) ≤ 2` (no mathlib def).
Does mathlib already have a canonical form for this idea? yes: `∀ p > 2, ¬ LiouvilleWith p x` (the shape used in `ae_not_liouvilleWith`).
Is our statement stated against the canonical form? The def itself is not (it is externally fixed). The project bridge `isDiophantine_iff` is an "orthogonal" equivalence with the project-local `approxSet`. The evidence bridge `isDiophantine_iff_liouvilleWith` has the canonical form on the RHS.
RHS convention respected? yes in the evidence bridge. `isDiophantine_iff` targets a project-local form, which is acceptable for a harness file.

### Syntactic generality — `IsDiophantine`

Alternative restatements attempted:
- the harness form (current)
- the `approxSet` form (`isDiophantine_iff`, needs `Irrational`)
- the `LiouvilleWith` form (evidence, no side hypothesis)
Chosen restatement: the harness form, which is mandatory for the evaluation. The `LiouvilleWith` form is the right one for mathlib.
Justification: the harness statement cannot change. The `LiouvilleWith` form is easiest to use with mathlib.

### Superfluous-argument audit — `IsDiophantine`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `x` | yes | the number |

(Side observation on the consumer: `thueSiegelRoth`'s `_h_irr` is mathematically implied by its conclusion, but it is part of the external statement and is used in the proof via `isDiophantine_iff`.)

### Statement-shape verdict (Phase 5.5)

Normal form: OK for the harness. The mathlib canonical form is `Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x` (bridge compiled).
Syntactic generality: OK (externally fixed)
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as the harness def; not for mathlib)

### Call sites — `IsDiophantine`

Internal use count: 0 outside the declaring file (grep over `Roth/`, `Roth.lean`, `lakefile.toml`)
External-to-file callers: 0 files in the project. The external consumer is the lean-eval harness, which checks `thueSiegelRoth`.

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/LeanEval.lean:43 (declaring file) | `IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2` |
| Roth/LeanEval.lean:62 (declaring file) | `theorem thueSiegelRoth ... : IsDiophantine x` |

Inline-derivation grep:
  - Roth/LeanEval.lean:20–22 private `exists_pos_div_rpow_lt_aux` proves the body for a fixed exponent `κ` (`∃ C > 0, ∀ p q, 0 < q → C / q ^ κ < |x - p/q|`). It is a building block of `isDiophantine_iff`, not a bypass.
  - No other restatement in Roth/Main.lean. Roth's theorem there is stated through `approxSet`.

### Composition check (Phase 6)

Can `IsDiophantine` be derived from mathlib in ≤3 chained calls?

Attempt 1: `IsDiophantine x := Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x`
  - Mathlib decls used: `Irrational`, `LiouvilleWith`, plus `LiouvilleWith.frequently_lt_rpow_neg`, `Nat.frequently_atTop_iff_infinite` and `Irrational.ne_rational` for the bridge
  - Result: succeeds as a definition-level composition (two mathlib predicates and one conjunction). The equivalence `isDiophantine_iff_liouvilleWith` is compiled in the evidence file. Its proof is about 40 lines through `approxSet`, but the composed predicate is one line.
  - Notes: the `Irrational x` conjunct is essential (rationals are not `LiouvilleWith p` for `p > 1`, yet fail `IsDiophantine`).

Conclusion: COMPOSABLE

## Verdict: `LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): standard notion "irrationality exponent ≤ 2" / `⋂_τ CD(τ)` (Diophantine numbers of every type `τ > 0`). The lean-eval page itself says mathlib lacks the predicate.
- Generality analysis (Phase 4): MAXIMALLY GENERAL as a hypothesis-free, externally fixed predicate. Modern idiom: `Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x` (compiled).
- Mathlib search (Phase 5): building blocks `Irrational`, `LiouvilleWith`, idiom `ae_not_liouvilleWith`. No `IsDiophantine` or irrationality exponent.
- Composition check (Phase 6): COMPOSABLE.

**Rationale:**

`IsDiophantine` is the lean-eval harness's rendering of "irrationality measure ≤ 2". It is copied verbatim into Roth/LeanEval.lean so that `thueSiegelRoth` matches the benchmark statement exactly, so its name and body are not the project's to choose. Mathematically it is a standard notion (the Roth lower bound `|x − p/q| ≥ c(x, ε) q^{−2−ε}`, i.e. membership in every Diophantine class `CD(τ)`). Mathlib already expresses this through `LiouvilleWith`: the evidence file proves, with no side hypothesis, `IsDiophantine x ↔ Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x`. The right-hand side is exactly the shape of mathlib's `ae_not_liouvilleWith`. A mathlib PR adding `IsDiophantine` would add a second name for an existing notion. The genuine mathlib gap is Roth's theorem itself, which the Roth.roth report targets as `IsAlgebraic.not_liouvilleWith`.

This agrees with the Roth.approxSet report (NO-composable, with `LiouvilleWith` as the mathlib concept) and the Roth.roth report (YES-but-generalise-first, with mathlib form `¬ LiouvilleWith p α`). `IsDiophantine` is the third formulation of the same content, and it too reduces to `LiouvilleWith`. One thing the bridge brings out: the predicate already implies irrationality. So the mathlib-facing statement needs the explicit `Irrational x` conjunct only if one wants an exact equivalence, and Roth in mathlib form needs no irrationality hypothesis.

WHY not (refactor-actionable): mathlib's `Irrational` and `LiouvilleWith` (Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean:51) compose to the same predicate. There is nothing to upstream. Unlike an ordinary NO-composable def, it must **not** be inlined at its call sites, because the harness checks the literal statement `thueSiegelRoth x _ _ : IsDiophantine x`.

Belongs-elsewhere check: keep it in Roth/LeanEval.lean, the external evaluation-harness file, exactly as given by leanprover/lean-eval.

Mathlib building blocks:      `Irrational` (Mathlib/Data/Real/Irrational.lean), `LiouvilleWith` (Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean:51), `LiouvilleWith.frequently_lt_rpow_neg` (same file:97), `ae_not_liouvilleWith` (Liouville/Measure.lean:115, idiom), `Nat.frequently_atTop_iff_infinite`, `Irrational.ne_rational`
Composition sketch (≤3 lines):
```lean
-- compiled in the evidence file:
theorem isDiophantine_iff_liouvilleWith {x : ℝ} :
    IsDiophantine x ↔ Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x
```
Call sites in our project (from Phase 6.0):  0 outside the declaring file; 2 inside it (LeanEval.lean:43 `isDiophantine_iff`, LeanEval.lean:62 `thueSiegelRoth`)
Refactor plan: no inlining at either call site. Line 62 is the fixed harness statement, and line 43 is the bridge that consumes it. Optionally add `isDiophantine_iff_liouvilleWith` (and its helper `irrational_of_isDiophantine`) from the evidence file to Roth/LeanEval.lean after `isDiophantine_iff`, as the mathlib-vocabulary reading of the harness predicate.
Next action: keep `IsDiophantine` unchanged and do not upstream it. If Roth is upstreamed, state it against `LiouvilleWith` (see Roth.roth report), next to Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean.

---

## Next step

Keep `IsDiophantine` verbatim in Roth/LeanEval.lean (it is the external harness statement). Optionally add the compiled `isDiophantine_iff_liouvilleWith` bridge after `isDiophantine_iff`. Do not upstream it.

## Evidence
- `.mathlib-quality/overview/evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/liouvilleWith_bridge.lean` (imports `Roth.LeanEval` and `Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith`): it proves `irrational_of_isDiophantine`, the two `approxSet`/`LiouvilleWith` bridges (copied from the Roth.approxSet evidence), `isDiophantine_iff_liouvilleWith` (`IsDiophantine x ↔ Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x`), and the harness theorem in `¬ LiouvilleWith` form. `lean_diagnostic_messages` reports no diagnostics (clean, first try).
- Searches: 3 WebSearch queries (Diophantine type `τ`; Roth lower-bound form; lean-eval problem page), Lean-Finder, LeanSearch, Loogle, grep over mathlib (`IsDiophantine`, `irrationalityMeasure`, `irrationalityExponent`, `BadlyApprox`, `LeanEval`, `ae_not_liouvilleWith`), grep of the project (`IsDiophantine`, `LeanEval`, `thueSiegelRoth`) and grep of clean.tex. `lean_local_search` was unavailable because ripgrep is not installed. ChatGPT MCP was not configured.
