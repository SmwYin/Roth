---
decl: LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth
file: Roth/LeanEval.lean
line: 61
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: EXPENSIVE
junk: KEEP
rationale: The harness theorem is the Thue-Siegel-Roth theorem, a named gap that mathlib's LiouvilleWith docstring states without proof, but its signature is fixed by lean-eval and uses the non-mathlib predicate IsDiophantine; the mathlib form is IsAlgebraic.not_liouvilleWith (compiled from Roth.roth, with Irrational superfluous there although it is necessary in the harness form), and the harness statement is a compiled two-step corollary of that form.
action: Keep thueSiegelRoth verbatim in Roth/LeanEval.lean (harness-mandated; no project callers); upstream the content as IsAlgebraic.not_liouvilleWith plus LiouvilleWith.transcendental in a new Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean together with Roth.roth, after the development lands bottom-up; do not upstream the harness statement itself.
---

# LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth

## Inventory entry

### `theorem LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`
- **Type**: `(x : ℝ) (_h_irr : Irrational x) (_h_alg : IsAlgebraic ℤ x) : IsDiophantine x`
- **What**: Every irrational algebraic real `x` is Diophantine in the lean-eval sense: for every `ε > 0` there is `C > 0` with `C / q^(2+ε) < |x − p/q|` for all `p ∈ ℤ`, `q ∈ ℤ_{>0}`. This is the Thue–Siegel–Roth theorem in its lower-bound form.
- **How**: a two-call term proof. `Roth.roth` gives `∀ κ, (approxSet x κ).Infinite → κ ≤ 2`. Its algebraicity hypothesis over `ℚ` comes from `IsAlgebraic.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)`. `(isDiophantine_iff _h_irr).mpr` then converts this into `IsDiophantine x`.
- **Hypotheses**: `_h_irr : Irrational x` is necessary in this form (compiled: `IsDiophantine 0` is false). `_h_alg : IsAlgebraic ℤ x` is interchangeable with the `ℚ` version (compiled `thueSiegelRoth_rat`).
- **Uses from project**: `IsDiophantine`, `isDiophantine_iff`, `Roth.roth`
- **Used by**: unused in project. This is the harness endpoint: grep of `Roth/` and `Roth.lean` finds only the declaration at Roth/LeanEval.lean:61, and `Roth.lean` does not import `Roth.LeanEval`.
- **Visibility**: public
- **Lines**: 58–64, proof length 2 lines
- **Notes**: the statement (name, namespace, binder names, `IsDiophantine` def) must match https://github.com/leanprover/lean-eval/blob/main/LeanEval/NumberTheory/ThueSiegelRoth.lean verbatim. The underscore binder names come from the harness.

## Junk check (Step 8)
- Used anywhere? Not inside the project. It is the deliverable consumed by the external lean-eval harness, so "unused" is expected.
- Wrapper of 1–2 mathlib calls? It wraps two project calls (`isDiophantine_iff`, `Roth.roth`) plus one mathlib scalar-extension call. The wrapper exists because the harness fixes the statement.
- Does mathlib have it? No. Mathlib has no Roth theorem in any form. The LiouvilleWith.lean module docstring (line 27) states Thue–Siegel–Roth as context without proof. Searches below find only Liouville's theorem (`Liouville.exists_pos_real_of_irrational_root`, exponent = degree).
- Too specific (inline?)? No. The harness requires this exact name.
- Well-chosen? Yes for its purpose. It cannot be restated.

Conclusion: **KEEP**. Action: keep it verbatim in Roth/LeanEval.lean.

## Mathlibable assessment (Step 9)

Pre-filter: the theorem is public, has no `_aux` suffix and no internal/auxiliary docstring, and Step 8 said KEEP. A namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `thueSiegelRoth`, `IsDiophantine` and `LeanEval` finds nothing. It is not a glue lemma (it composes two non-trivial results, not `rfl`/unfolding), so it gets a full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the evidence file importing `Roth.LeanEval` elaborates with no diagnostics)
- decl `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`: resolved at Roth/LeanEval.lean:61
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the exact lean-eval Thue–Siegel–Roth statement, proved using `Roth.roth`.

### Statement (Phase 1)

`thueSiegelRoth` is a theorem stating the following:

Let `x ∈ ℝ` be irrational and algebraic over `ℤ`. Then for every `ε > 0` there is a constant `C = C(x, ε) > 0` such that `|x − p/q| > C / q^{2+ε}` for all integers `p` and all positive integers `q`. Equivalently, the irrationality exponent of `x` is at most 2 (Roth 1955).

Variables / typeclasses involved (Lean side):
- `x : ℝ`: the algebraic number being approximated.

Hypotheses (Lean side):
- `_h_irr : Irrational x`: rules out rational `x`, for which the conclusion fails because the approximation is exact.
- `_h_alg : IsAlgebraic ℤ x`: `x` is a root of a non-zero integer polynomial.

Conclusion (math): uniform lower bound `C(ε) q^{−2−ε}` for the approximation error.

Conclusion (Lean): `IsDiophantine x`

### Size classification (Phase 2a)

Verdict: BIG
Reason: a named theorem (Thue–Siegel–Roth) and the harness-facing main result of the project.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 2
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Thue-Siegel-Roth theorem statement algebraic irrational abs(alpha - p/q) > c(alpha,epsilon)/q^(2+epsilon) | yes | lower-bound form `|α − p/q| > c(α,ε) q^{−2−ε}`; finiteness form: `|α − p/q| < q^{−2−δ}` has finitely many solutions | Wikipedia "Roth's theorem", Encyclopedia of Mathematics "Thue–Siegel–Roth theorem", lean-lang.org/eval problem page. The constant is ineffective. Exponent 2 is sharp by Dirichlet |
| 2 | WebSearch (general form) | Roth theorem irrationality measure algebraic numbers equals 2 general form Schmidt subspace theorem | yes | `μ(α) = 2` for algebraic irrational `α`. Generalisations: Ridout (p-adic), Wirsing (degree-`d` approximants, exponent `2d+ε`), Schmidt subspace theorem | arXiv 1210.2983, Bugeaud JTNB 749, Waldschmidt HCMUNS10. Roth is a special case of the subspace theorem |
| 3 | WebSearch (named-after / aliases) | lean-eval ThueSiegelRoth IsDiophantine formalization Lean | yes | lean-eval problem "Thue–Siegel–Roth theorem (irrationality measure ≤ 2 for algebraic irrationals)", submitted by Kim Morrison | the problem page notes that mathlib has Liouville, Dirichlet and `ae_not_liouvilleWith`, but no Roth lemma and no `IsDiophantine` predicate. Aliases: Roth's theorem, Thue–Siegel–Roth, irrationality measure 2 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for Roth / Diophantine | yes | §"The proof of Roth's theorem" (l.1571): for `κ > 2`, infinitely many `|α − h/q| < q^{−κ}` is impossible (finiteness form) | the paper uses the finiteness form, which is the project's `Roth.roth` form, not the harness lower-bound form |
| 6 | nLab | Roth's theorem / Diophantine approximation | no | — | nLab has no page on Roth's theorem or approximation exponents |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry concept (Diophantine approximation of reals) |
| 9 | MathOverflow / Math.SE | (covered by #1–#2 hits: equivalence of the finiteness and lower-bound forms) | partial | folklore equivalence of the forms | consistent with #1 |
| 10 | recent arXiv (last 5 years) | (from #2 and the sibling report) | yes | Bugeaud–Kim 2025 (arXiv 2510.17177) define `μ` via the sup form. Quantitative subspace-theorem papers | no new form for Roth itself |

### Literature summary (Phase 3)

Concept identified as: the Thue–Siegel–Roth theorem (Roth 1955), i.e. irrationality measure `μ(α) = 2` for every algebraic irrational `α`.
Sources agree on the standard form: yes. There are three interchangeable forms: (i) finiteness of `|α − p/q| < q^{−2−δ}`; (ii) lower bound `c(α,ε) q^{−2−ε}`; (iii) `μ(α) ≤ 2`.
Most general standard form: Schmidt's subspace theorem (and Ridout/Schlickewei p-adic versions). Within single-number approximation, the standard is form (i)/(iii) for any algebraic `α`, where irrationality is automatic in form (iii) (the exponent of a rational is 1).
Generality dimensions where the literature varies:
  - form: finiteness (Roth, Encyclopedia) vs lower bound (MathWorld, lean-eval) vs exponent.
  - place: archimedean only vs several places (Ridout, Schlickewei).
  - approximants: rationals vs bounded-degree algebraics (Wirsing, Schmidt).
Disagreement with the literature: none. The harness uses the standard lower-bound form (ii).

### Generality analysis — `thueSiegelRoth`

Literature-standard form (from Phase 3): for algebraic `α` and `p > 2`, `α` is not `p`-approximable (mathlib: `¬ LiouvilleWith p α`). In this form irrationality is automatic.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `_h_irr : Irrational x` | required | implicit / automatic in exponent form | not in this form (verified): `IsDiophantine 0` is false while `0` is algebraic (`not_isDiophantine_zero`). In the `LiouvilleWith` form it is superfluous (`IsAlgebraic.not_liouvilleWith'`, Roth.roth evidence) | the harness predicate forces irrationality |
| 2 | `_h_alg : IsAlgebraic ℤ x` | integer coefficients | algebraic over `ℚ` | equivalent, not weaker (compiled `thueSiegelRoth_rat` for `ℚ`) | `ℤ` vs `ℚ` is immaterial |
| 3 | conclusion `IsDiophantine x` | harness predicate | `∀ p > 2, ¬ LiouvilleWith p x` | different vocabulary (IsDiophantine report: `IsDiophantine x ↔ Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x`, compiled) | the harness predicate is not mathlib vocabulary |
| 4 | threshold 2 / rational approximants | fixed | subspace theorem / Wirsing | yes in literature | far beyond the project (needs new mathematics; not a weakening) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD in vocabulary, not in content. The harness signature cannot change. The mathlib-facing restatement removes the irrationality hypothesis and replaces the non-mathlib predicate. It is verified: `IsAlgebraic.not_liouvilleWith'` compiles from `Roth.roth` (evidence/Roth.roth/mathlib_form.lean), and `thueSiegelRoth_of_not_liouvilleWith` (this decl's evidence) recovers the harness statement from it, so the restatement is not weaker in content.
Number of weakening opportunities found: 1 (restate as `¬ LiouvilleWith`, which drops `Irrational`; compiled)
Proposed restatement:
```lean
theorem IsAlgebraic.not_liouvilleWith {α p : ℝ} (halg : IsAlgebraic ℤ α) (hp : 2 < p) :
    ¬ LiouvilleWith p α
```
Cost of restatement: CHEAP as a project-level statement (compiled). EXPENSIVE to upstream, because the proof needs the whole ~4.8k-line Roth development (see Roth.roth report).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | single real number |
| 2 | sequences to filters? | yes | `¬ LiouvilleWith p α` (defined via `∃ᶠ n in atTop`) in place of the ε-C lower bound | `LiouvilleWith.mono`, `add_rat_iff`, `mul_rat_iff`, `ae_not_liouvilleWith`, `LiouvilleWith.irrational` |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | real setting |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no (in scope) | — | the threshold 2 is sharp (Dirichlet). Generalising approximants is new mathematics |
| 8 | concrete-via-abstract? | no | — | no concrete named object. The proof is a two-call composition |
| 9 | false-generalisation guard | no false generalisation | the `LiouvilleWith` form implies the harness form (compiled `thueSiegelRoth_of_not_liouvilleWith`) and conversely (Roth.roth evidence (3)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `IsAlgebraic.not_liouvilleWith` (above), plus the contrapositive `LiouvilleWith.transcendental {α p : ℝ} (h : LiouvilleWith p α) (hp : 2 < p) : Transcendental ℤ α`, which the mathlib docstring announces.
  - Cost: CHEAP for the statement (compiled). EXPENSIVE for the upstream proof.
  - Mathlib downstream this enables: it plugs into the `LiouvilleWith` API (arithmetic closure gives Roth for `r·α + s` for free) and strengthens `Liouville.transcendental` to all `LiouvilleWith p` with `p > 2`. It also pairs with `ae_not_liouvilleWith` (generic numbers vs algebraic numbers).
  - Real mathematical improvement: it removes a hypothesis (irrationality) and a non-mathlib predicate. It also states the theorem in the vocabulary mathlib already uses for the metric counterpart.

### Proof strategy — `thueSiegelRoth`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no (locally) | the 2-line proof delegates. The ε-C bookkeeping lives in `isDiophantine_iff` | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | Roth's theorem itself (the whole development). A `¬ LiouvilleWith` ↔ uniform lower-bound bridge (see isDiophantine_iff report, BORDERLINE) | follow-up PRs |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (the harness proof is a direct two-call composition and cannot be simpler given the fixed statement)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `thueSiegelRoth`

[A] Lean-Finder       "Roth's theorem: an irrational algebraic number cannot be approximated by rationals to order greater than 2"   hits: `Liouville.exists_pos_real_of_irrational_root` (exponent = degree), `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational` (Dirichlet), `Liouville`. No Roth
[B] Loogle            `IsAlgebraic, LiouvilleWith`   no hits
[C] LeanSearch        "algebraic irrational real number has uniform lower bound C / q^(2+ε) for rational approximations"   hits: `Irrational.eventually_forall_le_dist_cast_rat_of_den_le`, `Real.exists_rat_abs_sub_lt_and_lt_of_irrational`, `Liouville.frequently_exists_num`. No Roth
[D] Grep mathlib src  `thueSiegelRoth`, `IsDiophantine`, `not_liouvilleWith`, `irrationalityMeasure`, `Roth` in Transcendental/Liouville: the only hits are `ae_not_liouvilleWith` (Measure.lean:115, the metric statement) and the docstring mention of Thue–Siegel–Roth (LiouvilleWith.lean:27, no proof)
[E] Name pattern      the project grep finds `thueSiegelRoth` only at Roth/LeanEval.lean:61. The mathlib grep [D] covers the qualified-name check

Searched for both the harness form (lower bound / `IsDiophantine`) and the literature/mathlib form (`¬ LiouvilleWith p α` for algebraic `α`, `Transcendental` contrapositive).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Mathlib has only Liouville's (degree-exponent) theorem and the measure-theoretic `ae_not_liouvilleWith`.

### Normal-form check — `thueSiegelRoth`

Equivalent formalisms this statement could take: (a) `IsDiophantine x` (harness); (b) `∀ κ, (approxSet x κ).Infinite → κ ≤ 2` (`Roth.roth`); (c) `∀ p > 2, ¬ LiouvilleWith p x` (mathlib idiom); (d) `LiouvilleWith p x → 2 < p → Transcendental ℤ x`.
Does mathlib already have a canonical form for this idea? yes: (c), the shape of `ae_not_liouvilleWith`.
Is our statement stated against the canonical form? NO, but the harness fixes it. The mathlib-facing theorem should be (c)/(d), with the harness statement a corollary (compiled).
RHS convention respected? n/a (not an iff)

### Syntactic generality — `thueSiegelRoth`

Alternative restatements attempted:
- harness: `Irrational x → IsAlgebraic ℤ x → IsDiophantine x` (fixed)
- `ℚ` coefficients: `thueSiegelRoth_rat` (compiled)
- mathlib: `IsAlgebraic ℤ α → 2 < p → ¬ LiouvilleWith p α` (compiled in Roth.roth evidence)
Chosen restatement: the mathlib form for upstreaming. It has one fewer hypothesis and composes with `LiouvilleWith` API at call sites.
Justification: callers supply algebraicity only. Irrationality is derived via `LiouvilleWith.irrational`.

### Superfluous-argument audit — `thueSiegelRoth`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `x` | yes | the number |
| 2 | `_h_irr : Irrational x` | yes (in this form) | `IsDiophantine 0` is false and `0` is algebraic (compiled). It is superfluous only in the `LiouvilleWith` restatement |
| 3 | `_h_alg : IsAlgebraic ℤ x` | yes | Roth's hypothesis. Equivalent to the `ℚ` version |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR for upstreaming (state as `IsAlgebraic.not_liouvilleWith`). The harness statement stays fixed in the project.
Syntactic generality: RESTATE (mathlib form)
Superfluous arguments: NONE in the harness form; 1 (`Irrational`) disappears in the mathlib form

Overall: RESTATE-BEFORE-SHIP

### Call sites — `thueSiegelRoth`

Internal use count: 0 (grep over `Roth/`, `Roth.lean`, excluding the declaring file; the declaring file has no use either)
External-to-file callers: 0 files (the consumer is the external lean-eval harness)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| (none in project) | consumed externally by lean-eval as `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`. It is also used in evidence/LeanEval...IsDiophantine/liouvilleWith_bridge.lean (evidence only) |

Inline-derivation grep:
  - (none). `Roth.roth_rat` (Main.lean) states the den-form of the same theorem but derives it from `Roth.roth`, not from this decl.

### Composition check (Phase 6)

Can `thueSiegelRoth` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(isDiophantine_iff hx).mpr (Roth.roth hx (halg.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)))` (the current proof)
  - Mathlib decls used: `IsAlgebraic.extendScalars`, `FaithfulSMul.algebraMap_injective`. The core (`Roth.roth`, `isDiophantine_iff`) is project code.
  - Result: fails as a mathlib composition, because Roth's theorem is not in mathlib.

Attempt 2: from mathlib's Liouville theorem `Liouville.exists_pos_real_of_irrational_root`
  - Result: fails. It gives exponent `deg f`, not `2 + ε`.

Conclusion: NOT-COMPOSABLE (it would become a ≤2-call corollary once `IsAlgebraic.not_liouvilleWith` is in mathlib; compiled `thueSiegelRoth_of_not_liouvilleWith`)

### Verdict: `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the standard Thue–Siegel–Roth theorem (Roth 1955; Encyclopedia of Mathematics; lean-eval problem page). Three interchangeable forms, with irrationality automatic in the exponent form.
- Generality analysis (Phase 4): STRICTLY NARROWER in vocabulary. The verified restatement `IsAlgebraic.not_liouvilleWith` drops `Irrational` and the non-mathlib `IsDiophantine` (compiled). The harness form follows back from it (compiled).
- Mathlib search (Phase 5): not in mathlib. Only Liouville's theorem and `ae_not_liouvilleWith` are there, and LiouvilleWith.lean:27 cites Roth without proof.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The mathematical content is exactly the gap mathlib names. The module docstring of Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean mentions the Thue–Siegel–Roth theorem as the reason `LiouvilleWith p` for `p > 2` implies transcendence, but mathlib has no proof. The lean-eval problem page records the same absence. The harness theorem itself cannot go upstream as stated. Its signature is fixed by the external harness, and its conclusion uses the harness predicate `IsDiophantine`, which is NO-composable-from-mathlib (it is `Irrational x ∧ ∀ p > 2, ¬ LiouvilleWith p x`). The upstream statement is the modern-idiom restatement `IsAlgebraic.not_liouvilleWith`. In that form the `Irrational` hypothesis, which is necessary in the harness form (`IsDiophantine 0` is false), becomes superfluous. That restatement is compiled from `Roth.roth`, and this decl's evidence shows the harness statement is a two-step corollary of it. So this verdict coincides with Roth.roth's (YES-but-generalise-first, EXPENSIVE). The cost is the upstreaming of the full development, and it does not affect the bucket.

Reason for the generalisation: MODERN-IDIOM (and LITERATURE-WEAKENING: no irrationality hypothesis in the exponent form).
Proposed restatement:
```lean
theorem IsAlgebraic.not_liouvilleWith {α p : ℝ} (halg : IsAlgebraic ℤ α) (hp : 2 < p) :
    ¬ LiouvilleWith p α := by
  sorry  -- proof = Roth.roth + LiouvilleWith bridge (compiled in evidence/Roth.roth/mathlib_form.lean)

theorem LiouvilleWith.transcendental {α p : ℝ} (h : LiouvilleWith p α) (hp : 2 < p) :
    Transcendental ℤ α := fun halg ↦ halg.not_liouvilleWith hp h
```
Estimated cost of regeneralisation: EXPENSIVE (upstream needs the whole Roth development; the statement switch alone is CHEAP and compiled)
Mathlib downstream this enables:
  - `LiouvilleWith.transcendental` for every `p > 2`, strengthening `Liouville.transcendental`.
  - Through `LiouvilleWith.add_rat_iff` / `mul_rat_iff`, Roth for all `r·α + s` for free.
  - A clean contrast with `ae_not_liouvilleWith` (almost every real vs every algebraic real).
Next action: keep `thueSiegelRoth` verbatim in Roth/LeanEval.lean (no project call sites; harness-mandated). Upstream `IsAlgebraic.not_liouvilleWith` / `LiouvilleWith.transcendental` in a new Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean together with `Roth.roth`, after the Hasse-derivative, index and main-lemma layers land. Optionally re-prove `thueSiegelRoth` in the project via `thueSiegelRoth_of_not_liouvilleWith` once the mathlib form is in the project. Run `/generalise Roth.roth` before the PR.

---

## Next step

Keep the harness theorem as is. Upstream Roth's theorem in the form `IsAlgebraic.not_liouvilleWith` (with `LiouvilleWith.transcendental`) as part of the Roth.roth upstreaming plan, in a new Mathlib/NumberTheory/Transcendental/Liouville/Roth.lean.

## Evidence
- `.mathlib-quality/overview/evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth/hypotheses_and_mathlib_form.lean` (imports `Roth.LeanEval` and `Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith`) proves three things. (1) `not_isDiophantine_zero`: `Irrational` is necessary in the harness form. (2) `thueSiegelRoth_rat`: the `ℚ`-coefficient variant. (3) `thueSiegelRoth_of_not_liouvilleWith`: the harness theorem from the mathlib form `IsAlgebraic ℤ α → 2 < p → ¬ LiouvilleWith p α`. `lean_diagnostic_messages`: the first check flagged one unused simp argument (`zero_div`), which was removed; the re-check reported no diagnostics.
- Reused compiled evidence: `evidence/Roth.roth/mathlib_form.lean` (`IsAlgebraic.not_liouvilleWith'`, `LiouvilleWith.transcendental'` from `Roth.roth`) and `evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine/liouvilleWith_bridge.lean` (`isDiophantine_iff_liouvilleWith`).
- Searches: 3 WebSearch queries (lower-bound statement; irrationality measure / subspace theorem; lean-eval formalization), Lean-Finder, LeanSearch, Loogle (`IsAlgebraic, LiouvilleWith`: no hits), grep of mathlib (`thueSiegelRoth`, `IsDiophantine`, `not_liouvilleWith`, `irrationalityMeasure`, `Roth`), grep of the project (`thueSiegelRoth`, `LeanEval`) and grep of references/clean.tex. ChatGPT MCP was not configured.
