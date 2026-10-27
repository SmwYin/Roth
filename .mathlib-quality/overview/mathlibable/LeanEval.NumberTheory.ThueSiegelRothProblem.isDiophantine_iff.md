---
decl: LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff
file: Roth/LeanEval.lean
line: 42
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: CHEAP
junk: KEEP
rationale: The harness-glue equivalence between IsDiophantine and the project-local approxSet exponent bound links two non-mathlib predicates, so it cannot go upstream as is (compiled evidence shows that both sides reduce to the mathlib form, not LiouvilleWith p for p above 2, and that the Irrational hypothesis is superfluous); whether mathlib wants the underlying uniform-lower-bound characterisation of not LiouvilleWith is a judgment call.
action: Keep in Roth/LeanEval.lean (sole caller thueSiegelRoth at LeanEval.lean:63); optionally drop the superfluous hx hypothesis (compiled isDiophantine_iff' in evidence) and add the compiled isDiophantine_iff_liouvilleWith bridge; upstream only a generic lower-bound-vs-LiouvilleWith lemma to Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean if the human approves.
---

# LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff

## Inventory entry

### `theorem LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`
- **Type**: `{x : ℝ} (hx : Irrational x) : IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2`
- **What**: For irrational `x`, the lean-eval predicate (for every `ε > 0` some `C > 0` gives `C/q^(2+ε) < |x − p/q|` for all `p/q`) is equivalent to the project's form of Roth's conclusion: every `κ` with infinitely many approximations `|x − h/q| < 1/q^κ` satisfies `κ ≤ 2`.
- **How**: (→) Suppose `κ > 2` with `approxSet x κ` infinite. Apply the harness bound at `ε = (κ−2)/2` to get `C`. `Roth.eventually_div_rpow_lt` gives `Q` with `(1/C)/q^κ < 1/q^(2+ε)` for `q > Q`. `Roth.approxSet_den_le_finite` together with `Set.Infinite.sdiff` gives a member with `q > Q`. The two inequalities then contradict (`mul_lt_mul_of_pos_left`, `lt_asymm`). (←) Given `ε`, the RHS forces `approxSet x (2+ε)` finite (`Set.not_infinite`, `linarith`). The private `exists_pos_div_rpow_lt_aux` then produces the uniform `C`.
- **Hypotheses**: `hx : Irrational x` (only used in the ← direction, via the aux lemma). Superfluous for the statement (see evidence).
- **Uses from project**: `IsDiophantine`, `Roth.approxSet`, `Roth.eventually_div_rpow_lt`, `Roth.approxSet_den_le_finite`, `exists_pos_div_rpow_lt_aux` (private)
- **Used by**: `LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth` (Roth/LeanEval.lean:63). No other use in `Roth/` (grep). `Roth.lean` does not import `Roth.LeanEval`.
- **Visibility**: public
- **Lines**: 41–56, proof length 14 lines
- **Notes**: This is the bridge between the external harness statement and the project's `Roth.roth`. Both of its sides are project or harness predicates.

## Junk check (Step 8)
- Used anywhere? Yes, once: it is the key step of the harness theorem `thueSiegelRoth`.
- Wrapper of 1–2 mathlib calls? No. It is a 14-line two-direction argument through three project lemmas.
- Does mathlib have it? No. Mathlib has neither `IsDiophantine` nor `approxSet`, and no lower-bound characterisation of `LiouvilleWith` (searches below).
- Too specific (inline?)? It could be inlined into `thueSiegelRoth` (only the ← direction is used there), but the iff is a clean, documented bridge that makes the harness file readable. Keeping it is reasonable.
- Well-chosen? Mostly. The `Irrational x` hypothesis is superfluous (compiled `isDiophantine_iff'`), and the lemma is an "orthogonal" equivalence, not one stated against mathlib's canonical form.

Conclusion: **KEEP**. Action: keep it in Roth/LeanEval.lean. Optionally drop `hx` (callers then pass nothing: `isDiophantine_iff.mpr ...`) and add the canonical-form bridge `isDiophantine_iff_liouvilleWith`.

## Mathlibable assessment (Step 9)

Pre-filter: the theorem is public, its name has no `_aux` suffix, and its docstring is not internal or auxiliary. Step 8 said KEEP. A grep of `.lake/packages/mathlib/Mathlib/` finds no `isDiophantine` or `LeanEval`. It is not a glue lemma (14-line proof, not `Iff.rfl`/unfolding), so INHERITED does not apply. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.LeanEval` elaborates with no diagnostics)
- decl `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`: resolved at Roth/LeanEval.lean:42
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the lean-eval Thue–Siegel–Roth statement, reproduced verbatim and proved from `Roth.roth`.

### Statement (Phase 1)

`isDiophantine_iff` is a theorem stating the following:

Let `x` be an irrational real. The following are equivalent:
- (a) for every `ε > 0` there is `C > 0` with `|x − p/q| > C q^{−2−ε}` for all `p ∈ ℤ`, `q ∈ ℤ_{>0}`;
- (b) for every real `κ`, if `|x − h/q| < q^{−κ}` has infinitely many solutions `(h, q) ∈ ℤ × ℕ_{>0}`, then `κ ≤ 2`.

In words: "irrationality exponent at most 2" in its lower-bound form is equivalent to the same statement in its "infinitely many approximations" form.

Variables / typeclasses involved (Lean side):
- `x : ℝ`: the number being approximated.
- `κ : ℝ` (bound inside the RHS): the approximation quality.

Hypotheses (Lean side):
- `hx : Irrational x`. It ensures that no approximation is exact. The evidence shows that the statement holds without it.

Conclusion (math): the lower-bound and approximation-count forms of `μ(x) ≤ 2` agree.

Conclusion (Lean): `IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a bridge lemma between the harness predicate and the project's statement of Roth. It is neither a main result nor a new structure.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 14 substantive lines
One-liner verdict: n/a (kind is theorem)

Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | irrationality exponent equivalent characterization infinitely many rationals abs(x - p/q) < 1/q^mu versus lower bound c/q^(mu+epsilon) | yes | `μ(x) = sup{μ : |x − p/q| < q^{−μ} infinitely often}` = `inf{μ : |x − p/q| > q^{−μ−ε} for all large q, all ε}` | MathWorld "Irrationality Measure" states the lower-bound form, and Bugeaud–Kim arXiv 2510.17177 / 2510.02059 state the sup form. The equivalence is folklore and stated without proof |
| 2 | WebSearch (general form) | irrationality measure definition supremum of mu such that 0 < abs(x - p/q) < 1/q^mu has infinitely many solutions | yes | sup form with `0 <` (exactness excluded), sometimes coprime `p, q`, `<` or `≤` | Wikipedia "Irrationality measure", Waldschmidt HCMUNS10, arXiv 2210.16553. Variants differ only in coprimality and strictness |
| 3 | WebSearch (named-after / aliases) | Diophantine type tau equivalent irrationality exponent at most 2+tau "for every epsilon" lemma | partial | "Diophantine of exponent `τ`": `|x − p/q| ≥ γ q^{−2−τ}` (arXiv math/0009232). No source states the bridge as a named lemma | aliases: Diophantine number, `CD(τ)`, irrationality measure ≤ 2 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/*.tex` for Diophantine / irrationality | partial | §6 states Roth via the approximation set (eq. (1)), the RHS form | the paper never uses the lower-bound form, and l.1643 points at mathlib's DiophantineApproximation |
| 6 | nLab | irrationality measure / Diophantine approximation | no | — | nLab has no page on approximation exponents |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | (covered by #1–#3 hits) | partial | folklore equivalence of the two forms of `μ(x)` | consistent with #1 |
| 10 | recent arXiv (last 5 years) | (results of #1–#3) | yes | arXiv 2510.17177, 2510.02059 (2025), 2210.16553 (2022) | all define `μ` via the sup form and use the lower-bound form as an immediate equivalent |

### Literature summary (Phase 3)

Concept identified as: equivalence of the two standard characterisations of "irrationality exponent `μ(x) ≤ 2`" (lower bound `c(ε) q^{−2−ε}` vs no infinite family of `q^{−κ}`-approximations for `κ > 2`).
Sources agree on the standard form: yes. The equivalence is treated as immediate folklore and is not a named lemma.
Most general standard form: for any threshold `μ₀`, (∀ ε > 0, ∃ c > 0, ∀ p/q, `|x − p/q| ≥ c q^{−μ₀−ε}`) ↔ (∀ κ > μ₀, only finitely many `|x − p/q| < q^{−κ}`) ↔ `μ(x) ≤ μ₀` (for irrational `x`). The threshold 2 is not essential.
Generality dimensions where the literature varies:
  - threshold: fixed 2 (Roth) vs general `μ₀` (exponent theory).
  - coprimality and exactness: some sources require coprime `p, q` or `0 < |x − p/q|`, which matters only for rational `x`.
Disagreement with the literature: none. The harness and the project use the standard two forms with threshold 2.

### Generality analysis — `isDiophantine_iff`

Literature-standard form (from Phase 3): for any `μ₀`, lower-bound form ↔ finitely-many-approximations form. In mathlib vocabulary the shared target is `∀ p > μ₀, ¬ LiouvilleWith p x`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hx : Irrational x` | required | usually assumed | yes (verified) | For rational `x` both sides are false. The LHS forces irrationality (exact representation `r.num/r.den`). On the RHS, `approxSet x κ` contains every non-reduced `(k·num, k·den)`, so it is infinite for `κ = 3`. `isDiophantine_iff'` compiles without `hx` |
| 2 | threshold `2` | hard-coded | general `μ₀` | not here | both sides are fixed predicates (the harness def hard-codes `2 + ε`). Generalising means replacing `IsDiophantine`, which is externally fixed |
| 3 | `x : ℝ` | real | real | no | real approximation |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (one verified superfluous hypothesis), but only as a project-local lemma. The other generalisation (threshold) is blocked by the fixed harness def.
Number of weakening opportunities found: 1 (drop `hx`, compiled: `isDiophantine_iff'` in the evidence file, `lean_diagnostic_messages` clean)
Proposed restatement:
```lean
theorem isDiophantine_iff {x : ℝ} :
    IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2
```
Cost of restatement: CHEAP. It is a mechanical `by_cases hx` wrapper around the current proof, with about 20 lines for the rational case (`approxSet_infinite_of_not_irrational` plus `irrational_of_isDiophantine`). This removes the `_h_irr` dependency in `thueSiegelRoth`'s proof, though not from its fixed harness signature.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | single real number |
| 2 | sequences to filters? | yes | RHS as `∀ p > 2, ¬ LiouvilleWith p x` (filter `∃ᶠ n in atTop` form) | `LiouvilleWith` API, `ae_not_liouvilleWith` shape |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | `approxSet` is a set of pairs; the mathlib analogue is the `LiouvilleWith` predicate, not a substructure |
| 5 | field-specific to semiring? | no | — | real setting |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (threshold) | threshold `μ₀` in place of `2` | blocked by the fixed harness def. Would apply to a mathlib lemma `lower bound at μ₀+ε ↔ ∀ p > μ₀, ¬ LiouvilleWith p x` |
| 8 | concrete-via-abstract? | no | — | the proof uses only generic facts (rpow growth, finiteness of bounded-denominator approximations), but there is no concrete named object to abstract |
| 9 | false-generalisation guard | no false generalisation | `isDiophantine_iff_liouvilleWith` (evidence) is the same statement composed with `approxSet_bound_iff_not_liouvilleWith`. Q2's reformulation keeps the meaning for irrational `x` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: state the bridge against the canonical form, `IsDiophantine x ↔ ∀ p > 2, ¬ LiouvilleWith p x` (for irrational `x`; compiled `isDiophantine_iff_liouvilleWith`), together with `(∀ κ, (approxSet x κ).Infinite → κ ≤ 2) ↔ ∀ p > 2, ¬ LiouvilleWith p x` (compiled `approxSet_bound_iff_not_liouvilleWith`).
  - Cost: CHEAP (compiled, about 40 lines).
  - Mathlib downstream this enables: the harness predicate becomes usable with `LiouvilleWith.mono`, `mul_rat_iff`, `add_rat_iff` and `ae_not_liouvilleWith`.
  - Real mathematical improvement: two O(n) bridges to the canonical form replace one O(n²) orthogonal bridge. Both LHS predicates still stay out of mathlib.

### Proof strategy — `isDiophantine_iff`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | yes | the → direction picks `Q` via `Roth.eventually_div_rpow_lt` (an `∃ Q₀, ∀ q > Q₀` statement) where an `∀ᶠ` filter statement would be cleaner | CHEAP (see Roth.eventually_div_rpow_lt report) |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | (i) "finitely many fractions with bounded denominator in a bounded set" (Roth.approxSet_den_le_finite report). (ii) A uniform lower bound from finitely many exceptional approximations (the private aux lemma). (iii) A lower-bound ↔ `¬ LiouvilleWith` bridge | follow-up PR only if the human approves (see questions) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (for a project bridge; the short proof is fine)
  - Minor: the filter form of `eventually_div_rpow_lt` would tidy the → direction, but this does not change the verdict.

### Mathlib search-status: `isDiophantine_iff`

[A] Lean-Finder       "uniform lower bound C/q^p on |x - m/q| for all rationals iff not LiouvilleWith p x"   hits: `LiouvilleWith`, `LiouvilleWith.exists_pos`, `forall_liouvilleWith_iff`, `Liouville.liouvilleWith`, `Liouville` (no lower-bound characterisation)
[B] Loogle            `LiouvilleWith, Set.Infinite`   no hits (mathlib never states LiouvilleWith via set infinitude)
[C] LeanSearch        "irrational x is LiouvilleWith p iff infinitely many rationals approximate within 1/q^p"   hits: `LiouvilleWith`, `setOf_liouville_eq_irrational_inter_iInter_iUnion`, `Liouville.frequently_exists_num`, `LiouvilleWith.irrational`, `liouvilleWith_one` (none is the bridge)
[D] Grep mathlib src  `isDiophantine`, `IsDiophantine`, `irrationalityExponent`, `irrationalityMeasure`, `LeanEval`: no hits. All theorems of Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean listed (`exists_pos`, `mono`, `frequently_lt_rpow_neg`, arithmetic closure, `irrational`, `forall_liouvilleWith_iff`). None gives a lower-bound form
[E] Name pattern      `lean_local_search isDiophantine_iff`: it was recorded unavailable in earlier runs (ripgrep missing), so it was replaced by the project grep (`isDiophantine_iff` only at Roth/LeanEval.lean:42,63) and the mathlib grep [D]

Searched for both the current form (harness ↔ approxSet) and the literature-standard form (lower-bound form ↔ exponent form, i.e. ↔ `¬ LiouvilleWith`).

Concluded: found building blocks (`LiouvilleWith`, `LiouvilleWith.frequently_lt_rpow_neg`, `Nat.frequently_atTop_iff_infinite`, `Irrational.ne_rational`). Neither form is in mathlib, and the composition needs about 30 lines of project bridges, not ≤3 mathlib calls.

### Normal-form check — `isDiophantine_iff`

Equivalent formalisms this statement could take: (a) `IsDiophantine x` (harness); (b) `∀ κ, (approxSet x κ).Infinite → κ ≤ 2` (project); (c) `∀ p > 2, ¬ LiouvilleWith p x` (mathlib idiom, `ae_not_liouvilleWith`).
Does mathlib already have a canonical form for this idea? yes: (c).
Is our statement stated against the canonical form? NO. It is the orthogonal equivalence (a) ↔ (b). REFACTOR target: (a) ↔ (c) and (b) ↔ (c), both compiled in the evidence file.
RHS convention respected? no (neither side is canonical)

### Syntactic generality — `isDiophantine_iff`

Alternative restatements attempted:
- current: `Irrational x → (IsDiophantine x ↔ ∀ κ, (approxSet x κ).Infinite → κ ≤ 2)`
- without `hx`: `IsDiophantine x ↔ ∀ κ, ...` (compiled)
- canonical: `Irrational x → (IsDiophantine x ↔ ∀ p > 2, ¬ LiouvilleWith p x)` (compiled)
Chosen restatement: inside the project, the `hx`-free version is easiest to apply (`isDiophantine_iff.mpr (Roth.roth ...)` with no irrationality argument). For any mathlib-facing use, the canonical one.
Justification: dropping `hx` removes a side goal at the call site, and the canonical RHS connects to mathlib's API.

### Superfluous-argument audit — `isDiophantine_iff`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `x` | yes | the number |
| 2 | `hx : Irrational x` | no | the conclusion holds for rational `x` (both sides false). Compiled `isDiophantine_iff'` |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (state against `∀ p > 2, ¬ LiouvilleWith p x`)
Syntactic generality: RESTATE (drop `hx`)
Superfluous arguments: 1 to drop (`hx`)

Overall: RESTATE-BEFORE-SHIP (only relevant if anything here ships; locally it is optional)

### Call sites — `isDiophantine_iff`

Internal use count: 0 outside the declaring file (grep over `Roth/`, `Roth.lean`)
External-to-file callers: 0 files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/LeanEval.lean:63 (declaring file) | `(isDiophantine_iff _h_irr).mpr (Roth.roth _h_irr (...))` in `thueSiegelRoth` |

Inline-derivation grep:
  - (none). The evidence file for `IsDiophantine` reuses `isDiophantine_iff`; it does not re-derive it. Roth/Main.lean never mentions the lower-bound form.

### Composition check (Phase 6)

Can `isDiophantine_iff` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(isDiophantine_iff_liouvilleWith hx).trans (approxSet_bound_iff_not_liouvilleWith hx).symm`
  - Mathlib decls used: none directly. Both pieces are project bridges (compiled in the evidence file). Each takes about 15 lines over `LiouvilleWith.frequently_lt_rpow_neg`, `Nat.frequently_atTop_iff_infinite`, `Irrational.ne_rational` and `Roth.approxSet_den_le_finite`.
  - Result: fails as a mathlib composition (the pieces are not in mathlib)
  - Notes: both sides of the iff are non-mathlib predicates, so no mathlib composition can state it.

Attempt 2: direct from `LiouvilleWith` API
  - Mathlib decls used: `LiouvilleWith.exists_pos`, `LiouvilleWith.frequently_lt_rpow_neg`
  - Result: fails. Mathlib has no lower-bound characterisation of `¬ LiouvilleWith`, and the "finitely many approximations ⇒ uniform constant" step (the private aux lemma) has no mathlib counterpart.

Conclusion: NOT-COMPOSABLE

### Verdict: `LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): the two folklore characterisations of `μ(x) ≤ 2` (MathWorld lower-bound form vs Wikipedia/Bugeaud sup form). No named lemma exists.
- Generality analysis (Phase 4): STRICTLY NARROWER as a local lemma. `hx` is superfluous (verified, `isDiophantine_iff'` compiles). Generalising the threshold is blocked by the fixed harness def. Modern idiom: state both sides against `∀ p > 2, ¬ LiouvilleWith p x` (compiled).
- Mathlib search (Phase 5): building blocks only (`LiouvilleWith` and its API). There is no lower-bound characterisation, no `IsDiophantine` and no irrationality exponent.
- Composition check (Phase 6): NOT-COMPOSABLE (both sides are non-mathlib predicates).

**Rationale:**

As stated, `isDiophantine_iff` cannot go to mathlib. Its LHS is the lean-eval harness predicate (assessed NO-composable, composed from `Irrational` and `LiouvilleWith`), and its RHS is the project-local `Roth.approxSet` (also NO-composable, `LiouvilleWith`). It is also an "orthogonal" equivalence between two non-canonical forms, which mathlib's normal-form policy rejects. The evidence shows that both sides are equivalent to the canonical `∀ p > 2, ¬ LiouvilleWith p x` (for irrational `x`). It also shows that the `Irrational x` hypothesis is superfluous: for rational `x`, `IsDiophantine` fails and `approxSet x 3` is infinite because of non-reduced representations. So YES-* would mean upstreaming a lemma about predicates mathlib should not have, and NO-composable fails the gate because the composition is not ≤3 mathlib calls.

There is a genuine, small mathlib gap underneath. Mathlib's `LiouvilleWith` file has only the "frequently close" side. It has no lemma turning `¬ LiouvilleWith` into a uniform lower bound `C / n^p ≤ |x − m/n|`, nor the converse, i.e. the lower-bound form that Liouville's theorem (`Liouville.exists_pos_real_of_irrational_root`) and Roth's theorem are usually stated in. Whether a generic bridge of the shape `Irrational x → ((∀ p > μ₀, ¬ LiouvilleWith p x) ↔ ∀ ε > 0, ∃ C > 0, ∀ m n, 0 < n → C / n^(μ₀+ε) < |x − m/n|)` is wanted in mathlib is a taste and policy call (it rearranges an existing notion and adds no new mathematics). That is why the verdict is BORDERLINE. The verdict does not rest on cost.

Numbered questions:
1. Should mathlib get a generic lower-bound characterisation of `¬ LiouvilleWith` (threshold `μ₀`, the `ε`-quantified uniform bound), to sit next to `LiouvilleWith.frequently_lt_rpow_neg` in Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean? (If yes, this lemma's ← direction plus the private aux lemma is the proof content. If no, the verdict becomes project-local KEEP with no upstream.)
2. Do you want the superfluous `hx : Irrational x` dropped from `isDiophantine_iff` in Roth/LeanEval.lean now (compiled `isDiophantine_iff'`, CHEAP)? The `thueSiegelRoth` signature keeps its harness-mandated `_h_irr` either way.
3. Should the compiled canonical-form bridges `isDiophantine_iff_liouvilleWith` and `approxSet_bound_iff_not_liouvilleWith` be added to the project (LeanEval.lean and Main.lean respectively), so that the harness predicate connects to mathlib's `LiouvilleWith` API?

Next action: the user answers the questions. Meanwhile keep `isDiophantine_iff` in Roth/LeanEval.lean; its single call site (`thueSiegelRoth`, LeanEval.lean:63) needs no change. If Q2 is yes, replace the statement with the `hx`-free `isDiophantine_iff'` from the evidence file and change the call site to `isDiophantine_iff.mpr (Roth.roth ...)`.

---

## Next step

Answer the three questions above. The default is to keep the lemma project-local in Roth/LeanEval.lean, optionally dropping the superfluous `Irrational x` hypothesis (compiled).

## Evidence
- `.mathlib-quality/overview/evidence/LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff/weaken_and_compose.lean` (imports `Roth.LeanEval` and `Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith`). It proves `approxSet_infinite_of_not_irrational` (rational `x` gives infinite `approxSet` for every `κ`), `isDiophantine_iff'` (the statement without `hx`), `approxSet_bound_iff_not_liouvilleWith` (RHS ↔ canonical form) and `isDiophantine_iff_liouvilleWith` (LHS ↔ canonical form, via `isDiophantine_iff`). `lean_diagnostic_messages`: no diagnostics (clean on first check).
- Searches: 3 WebSearch queries (exponent equivalence; sup-form definition; Diophantine type `τ`), Lean-Finder, Loogle (`LiouvilleWith, Set.Infinite`: no hits), LeanSearch, grep of mathlib (`isDiophantine`, `irrationalityExponent`, `irrationalityMeasure`, `LeanEval`, and the full theorem list of LiouvilleWith.lean), grep of the project (`isDiophantine_iff`, `thueSiegelRoth`) and grep of references/*.tex. ChatGPT MCP was not configured.
