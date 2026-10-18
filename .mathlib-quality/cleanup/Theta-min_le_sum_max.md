# Cleanup — original26 `Roth.min_le_sum_max`

## Scope, authorization, baseline

Fresh dedicated original26 audit; only this original counts toward the original declaration total.
The two newly introduced private helpers require separate fresh dedicated audits after this freeze.
No Git mutations, shared-ledger edits, pin changes, imports, or unrelated source changes were made.

- Release HEAD: `ec403072e0c731ef90f90301ce2e23ef9b61128a` (`ramin-cleanup`).
- Release Theta SHA256: `c24f9782e08680eaaebf16b134c8b86cbe13e05c9778d1606119f28f392cc7b9`.
- Immutable original: `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6:Roth/Theta.lean`.
- Owner's inherited baseline full build: exit0, 89.100s; separate LeanEval: exit0, 28.568s.
- Identical-source complete baseline LSP reused from
  `/private/tmp/roth-theta-sq-floor/final-lsp.json`: success=true, partial=false,
  timed_out=false, failed_dependencies=[], zero errors, 17 warnings.
- Optional cache fetch and separate runLinter: unnecessary; caches and native lint diagnostics present.
- Read lean4/mathlib-quality skills, full cleanup worker workflow, all five required full references
  (golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates), relevant
  style sections, naming guide and full profiling reference. Lean4.34 profiler override from dispatch
  takes precedence over the older reference's incorrect CLI example.

The user's standing authorization requires implementation of well-supported recommendations.
The owner reviewed the compiled unconditional candidate and full old-signature adapter before
application, endorsed removing both `hrp` and `hθ`, and authorized an additive documentation sentence.
All original paper/source prose remains. Previously audited public floor estimates remain unchanged.

## Result and mathematics

The conclusion and public name/domain remain exactly the same. Both assumptions disappear:

```lean
theorem min_le_sum_max {θ : ℝ} {rp : ℕ} (l : ℕ) :
    min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / rp)
```

If `rp=0`, the second member of the minimum is zero; if `θ≤0`, the first is nonpositive.
The sum is always nonnegative. For positive `rp,θ`, the proof splits at `l≤θ*rp`.
In the first case the unclipped triangular sum is at least `l*θ/2`, and replacing its terms
by their maxima with zero only increases it. In the second case use `n=⌊θ*rp⌋₊` and sum through
`n`; the exact triangular identity and `n≤θ*rp<n+1` give the quadratic bound directly.
For `x=n+t`, `0≤t<1`, the sharper underlying identity is
`rp*fullSum−x²/2 = n/2+t−t²/2≥0`; thus the source's cutoff `10<x` is unnecessary.

The sole routine caller now reads:

```lean
have hmin := min_le_sum_max (θ := θ) (rp := r none) l
```

Named parameters pin the two implicit values after the proof arguments disappear.
`index_le_lem6` retains its entire original public telescope, including `hq` and its class binders.
Its independent original proof/type/value and actual built axioms are verified below.

Main body: **46 → 13 lines**. Two private helpers: initially **11 and 25**, finally **12 and 26 body lines** after arithmetic profiling.
No substantive branch exceeds 10 lines. File delta is +12 lines, reflecting explicit decomposition
and the stronger theorem rather than a claim of total-file compression.

## Full substantive audit (24 items)

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | No target-range baseline warning. Final target/helpers have none; all 17 existing file warnings remain outside scope. |
| 2 | HAVE SCAN | Complete original inventory below; remove conditional positivity and max-equality scaffolding, reuse the actual triangular identity in the two independent estimates. |
| 3 | SET_OPTION | None in target; none introduced. |
| 4 | SIMP SQUEEZE | Original terminal `simp` stays terminal. New nonterminal zero simplification uses explicit `simp only [Nat.cast_zero, zero_mul, zero_div]`; no nonterminal bare simp. |
| 5 | NAMING | `min_le_sum_max` is snake_case, describes the result, and matches no forbidden pattern/abbreviation. No rename. New private names describe their linear/quadratic estimates and end `_aux`. |
| 6 | LINE PACKING | Measured codepoint tables below; all three declarations packed, width≤100. |
| 7 | BY PLACEMENT | All `by` delimiters at the end of signature/have lines. |
| 8 | FORMAT | Two-space proof indentation, no empty body lines, no sequential tactic semicolons in new code, no `haveI`/`letI`. |
| 9 | COMMENTS | Original body had no narrative comments. All four original docstring lines retained; one owner-approved extension sentence added. |
| 10 | DOCSTRING | Public source citation/narrative protected. Added explanation that the result holds without the source's positivity and size assumptions. Helpers have no docstrings. |
| 11 | VISIBILITY | Public original retained under explicit scope/API preference. Both new implementation lemmas private. |
| 12 | STRUCTURE | Independent linear/quadratic branches extracted. Main13/helpers12,26≤30, branches≤10. No conjunction in theorem. |
| 13 | MATHLIB | Five actual search methods and bounded uncontaminated compiler searches recorded below. Reuse existing triangular-sum, floor and finite-sum APIs. No direct replacement found; no assertion of exhaustive global absence. |
| 14 | JUNK DEF | n/a: theorem, no definition introduced. |
| 15 | EXISTS LEMMA | n/a: no existential conclusion/witness wrapper. |
| 16 | SHOW/CHANGE | No `show`/`change` scaffolding. |
| 17 | PUSH_NEG | No deprecated `push_neg`. Original `push Not` disappears with the old case proof. |
| 18 | GENERALISE | Every effective binder checked below. Remove BOTH conditions using a compiled unconditional proof, not textual non-use. |
| 19 | INEQUALITY | Every signature/local inequality uses `<`/`≤`; zero reversed-code occurrences. Source prose remains intact. |
| 20 | NORMAL-FORM | `min`, `max 0`, finite `range` and natural casts directly match the source and sole caller. Positive-part notation is equivalent but provides no caller simplification; no restatement. |
| 21 | SYNTAX-GEN | Removing conditions makes application simpler. Retain ordinary natural-weight domain and exact conclusion; no new bundled predicate. |
| 22 | IMPORT-FANOUT | n/a: no added imports. |
| 23 | CASTS | New explicit casts are Nat→Real bridges or load-bearing annotations fixing arithmetic/sum type inference. No same-type coercion introduced. |
| 24 | INSTANCE-NAME | n/a: no instance declaration/local instance introduced. Actual numeric original has no section type/class arguments. |

Original `have` inventory (release lines):

| Local | Uses/purpose | Action |
|---|---|---|
| `hrp'` | Positive real denominator, multiple uses | Derive locally from nonzero natural `rp`; retain real-denominator hypotheses only in helpers. |
| `hθ0` | Positive `θ`, used in positivity | Remove source size assumption; handle `θ≤0` directly. |
| `hterm` | Single-use equality of clipped and unclipped terms | Delete; `Finset.sum_le_sum` with `le_max_right` suffices. |
| `hν'` inside `hterm` | One cast bound | Deleted with the unnecessary equality proof. |
| `h1` | Single-use `sum_range_id_mul_two l` | Inline into `congrArg` in linear estimate. |
| `h2` | Triangular sum real identity | Preserve substantive content as helper-local `hsum`. |
| anonymous Nat-sub cast identity | Rewrites real cast of `l-1` | `push_cast [Nat.cast_sub hl0]` handles it directly. |
| anonymous cast of `h1` | Used by push_cast and exact | Fold into the retained `hsum` proof. |
| `hl0` | Single-use nonnegativity cast | Inline typed fact in scoped `linarith only`. |
| `hθr` | Nonnegative floor argument | Retain necessary helper-local mathematical fact. |
| `hn` | Prefix inclusion | Preserve prefix-bound content in quadratic helper. |
| `hnle` | Floor lower bound | Preserve as input to sharper quadratic arithmetic. |
| inner `hν'` in quadratic max equality | One index bound | Delete; only inequality to positive part is needed. |

## Five actual mathlib search methods

| Method | Queries and result |
|---|---|
| A Lean-Finder | “lower bound for finite sum max zero arithmetic progression minimum quadratic linear floor” found unrelated floor-power bounds; refined “finite arithmetic progression sum natural numbers cast equals n times n minus one divided by two” found `Finset.sum_range_id`, `Finset.sum_range_id_mul_two`, `Nat.triangle_succ`. Existing triangular formula used directly. |
| B Loogle | Initial `Finset.sum, max, min` rejected ambiguous `max`; corrected `Finset.sum, Max.max` succeeded and returned `Finset.max_sum_le` plus unrelated results. This compares sums to pointwise max but does not establish the needed triangular/quadratic estimate. |
| C LeanSearch | “lower bound sum positive parts arithmetic progression” returned `Finset.sum_nonneg`, positive-part and infinite-sum APIs. Refined explicit min/max numerical query returned `Finset.max_sum_le`, `min_add_max`, unrelated results. |
| D Source rg | Full-name `min_le_sum_max`, both proposed helper names: no source matches. `sum_range.*id`, arithmetic sum/cast and max/min variants inspected in `Mathlib/Algebra/BigOperators/Intervals.lean` and related files. `sum_range_id_mul_two` is Nat-valued; its cast is required. No output truncation in the full-name search. |
| E Local name index | Native `lean_local_search "sum_range_id"` finds the two existing formulas; index=`unavailable`. `mul_div_cancel_right₀` finds the actual declaration, index=`warming`. Positive results verified by successful compiler checks; incomplete index explicitly NOT used as absence evidence. |

Auxiliary variants considered: range/succ formulas, finite-sum monotonicity, max-of-sums,
pointwise positive-part bounds, floor lower/upper bounds, `_left`, `_right`, `_of_subset` routes.
Common-equivalents lookup has no matching disguised topology/finiteness predicate.

Clean generic-route probes are anonymous examples in an exact source prefix ending BEFORE the
audited theorem. No current theorem or named failed theorem is imported into that search context.
`automation.lean` tries whole original goal with `grind`, `aesop`, `simp`, `nlinarith`, `exact?`,
`apply?`; both helper goals also get `grind`, `aesop`, `exact?`, `apply?`. None closes.
`apply?` produces only generic inequality conversions and exhausts a conservative 10000-heartbeat
scratch budget; this is bounded inconclusiveness, not an absence proof. Expected-failure batch
exits1 and is never used as positive/axiom evidence. Historical stalled `lean_multi_attempt` is
not repeated per dispatch; native `lean_run_code` and bounded ordinary compiler exploration used.
Raw batch: `/private/tmp/roth-theta-min-sum/automation.{lean,log}`.

## Every-effective-binder generalization check

| Binder | Kind | Compiled probe | Result |
|---|---|---|---|
| `{θ : ℝ}` | Structure value | Remove with `autoImplicit=false` in `drop_theta` | Unknown `θ` in the exact conclusion: retain value, permit all signs via the unconditional candidate. |
| `{rp : ℕ}` | Structure value | Remove with `autoImplicit=false` in `drop_rp` | Unknown `rp` in exact conclusion: retain domain/value, admit zero by a separate proof branch. |
| `(hrp : 0 < rp)` | Proposition | Derive from `hθ` by zero contradiction; then unconditional candidate with no `hrp` | Both compile. Drop is stronger than replacing by `0≤rp` or `rp≠0`. |
| `(hθ : 10 < θ * rp)` | Proposition | Unconditional candidate and explicit full-old-telescope adapter | Compiles with NO bound, hence also covers the weak `10≤θ*rp` candidate. Drop entirely. |
| `(l : ℕ)` | Structure value | Remove with `autoImplicit=false` in `drop_l` | Unknown `l` in exact conclusion: retain value, no positivity requirement added. |
| Section `σ,τ`, Fintype, DecidableEq | Not effective binders | Printed actual/immutable fully explicit types and telescope comparison | None occurs in this numeric theorem. No fictitious section-instance drop is claimed. |

Positive isolated candidate/adapters:
`/private/tmp/roth-theta-min-sum/candidate-compatibility.{lean,log}` exit0.
Expected dependent-value drop failures:
`/private/tmp/roth-theta-min-sum/negative-binders.{lean,log}` exit1 as intended.
Weakening flags are not merely based on whether a name occurs in source.

Concrete→abstract review: real-denominator private estimates already work with arbitrary positive
real `r`, rather than just natural weights. A full public arbitrary-ordered-field/floor restatement
would change the domain and introduce new class-facing API with no project caller need. It is not
recommended in this cleanup. Inversion check: the statement is already an elementary parametric
sum inequality; there is no concrete named construction unfolded and then forgotten. No inversion
wrapper/API extraction is needed beyond the two actual independent estimates.

Literature check: two actual web queries were “Roth rational approximations algebraic numbers 1955
Lemma 6 sum max theta nu r” and “positive part arithmetic progression sum triangular lower bound
floor generalization”. The primary [1955 paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/rational_approximations_to_algebraic_numbers.pdf)
was identified. Local supplied primary exposition `.mathlib-quality/references/clean.tex:842–917`
was read directly: it gives the same two regimes and the sufficient `θ*rp>10` cutoff, not a claim
that the cutoff is necessary. The unconditional extension is our compiled elementary strengthening,
not attributed to an external search result. No ChatGPT math MCP tool is available (metadata checked).

## Golfing rule pass — all 42 rules

| Rule | Status |
|---|---|
| 1.1 by-exact wrapper | n/a: no final wrapper to remove. |
| 1.2 by-rfl | n/a: no reflexivity proof body. |
| 1.3 rw+exact→rwa | Reviewed; cast transformation and exact identity are separated by `push_cast`, so no matching pair remains. |
| 1.4 simp+exact→simpa | Zero simplification changes the goal, followed by general sum nonnegativity; explicit short sequence retained. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor packing | n/a: no conjunction/structure construction. |
| 1.7 apply+exact | Replaced old max-equality proof by direct finite-sum monotonicity; final result branches use composed exact terms. |
| 1.8 by-contra! | n/a: no production contradiction/negation chain. |
| 1.9 eta reduction | New callbacks genuinely use their bound argument; no eta-only lambda. |
| 1.10 single-use have | Inline original h1/nonnegative l; delete hterm/index-cast scaffolding; new helper-local floor facts are subject to their separate fresh audits. |
| 1.11 apply+intro | Use `Finset.sum_le_sum fun … ↦ …` directly. |
| 1.12 redundant show | n/a: none. |
| 1.13 have projection | n/a: no paired projection use. |
| 1.14 merge rw | Each algebraic rewrite chain merged; no adjacent rw calls to combine. |
| 1.15 terminal simp only | New zero simp is nonterminal. Existing linear zero branch remains terminal bare simp. |
| 1.16 squeeze bare simp | No new nonterminal bare simp. |
| 1.17 dot notation | `.trans`, `.2`, `.le`, `.ne'` used where appropriate. |
| 1.18 avoid parentheses | Sum callbacks use direct `fun`; retained parentheses group composed inequalities/type-sensitive arithmetic. |
| 1.19 push_neg | n/a: none. |
| 1.20 trivial exists | n/a: no existential helper. |
| 2.1 whole grind | Actually tried clean original/helper goals; fails, explicit arithmetic needed. |
| 2.2 delete before grind | n/a: no grind selected in final source. |
| 2.3 simpa consolidation | Assessed; explicit zero simplification then sum nonnegativity is direct and short. |
| 2.4 fun_prop | n/a: no analytic function property. |
| 2.5 positivity | Used for positive denominator after clearing fractions; explicit sign facts handle negative/zero cases. Initial unnormalized zero-branch positivity trial failed and was corrected. |
| 2.6 gcongr | Isolated division monotonicity trial compiles in the final exit0 verification file; direct `(div_le_div_iff_of_pos_right hr).2 hbound` retained as a single term. |
| 2.7 lia/omega | Positive Nat successor-inclusion trial with `lia` compiles; final source uses `Nat.pos_of_ne_zero` and existing range-subset API directly. No omega added. |
| 2.8 aesop | Actually tried clean whole/helper goals; no closure. |
| 2.9 norm_num/norm_cast | Numeric denominator positivity via norm_num and Nat→Real via exact_mod_cast/push_cast. |
| 2.10 decide/kernel | n/a: open real inequalities, not closed finite computation. |
| 2.11 field_simp/ring | `field_simp` alone closes the scaling identity; no trailing ring needed. |
| 2.12 linear_combination | n/a trigger: no final ring/ring_nf goal with hypotheses; nonlinear inequalities use explicit nonnegative products and `linarith only`, avoiding nonlinear preprocessing. |
| 2.13 wlog | n/a: the linear/quadratic regimes are different estimates, not symmetric duplicate branches. |
| 2.14 calc composition | Final min branches composed with `.trans`; quadratic chain has distinct scaling, arithmetic and prefix-inclusion steps. |
| 2.15 <;> | n/a: no multiple homogeneous open goals remain. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 legacy analysis | n/a: no continuity/measurability. |
| 3.3 omega→lia | No omega introduced; isolated lia trial passes. |
| 3.4 rfl substitution | `rcases … with rfl` and `subst rp` directly substitute; no redundant equality cleanup. |
| 3.5 automation attrs | No global attribute: specialized inequality would enlarge search sets without a clear normal-form use. |
| 3.6 simp_all | n/a: no simp_all-only closing block. |
| 3.7 heartbeat removal | No production limit option present or added. Search scratch only lowers the budget. |

Step-back reflection: single-tactic/direct-library routes were tried in clean contexts. The main
proof now explicitly dispatches degenerate/sign cases and then the two mathematically independent
estimates. The old unnecessary equality-to-positive-part proofs were replaced by termwise bounds.
A larger generic field wrapper or an extra one-use stage lemma would add API without clarifying
this 13-line proof; no further original-source edit recommended.

## Measured signature packing and inequality tables

Reference: compiled `#check @Roth.min_le_sum_max` at `format.width 100`, and actual built helper
types printed in `optimized-actual-compatibility.log`. Widths count Unicode codepoints, not UTF-8 bytes.
Next-token units here are the next complete binder or mathematical conclusion, as in the worker
workflow's examples; no expression is split merely to fill a line.

| Declaration / signature line | Width | Next binder/conclusion width | Arithmetic | Action |
|---|---:|---:|---|---|
| linear helper L299 | 96 | 57 | 96+1+57=154>100 | ok |
| linear helper L300 | 61 | — | final signature line | ok |
| quadratic helper L314 | 89 | 18 (`(hl : θ * r < l) :`) | 89+1+18=108>100 | ok |
| quadratic helper L315 | 84 | — | final signature line | ok |
| public theorem L348 | 49 | 81 | 49+1+81=131>100 | ok |
| public theorem L349 | 85 | — | final signature line | ok |

The first linear-helper candidate used three lines (71/28/61); the complete `(hl : …)` binder
fit the first line, so it was repacked to 96/61. The initial quadratic-helper candidate used
81/30/65; `{l : ℕ}` fit the first line and the bound fit the second, yielding 89/84.

| Declaration | Reversed code inequality occurrences | Action |
|---|---:|---|
| `min_le_sum_max` | 0 | All code uses `<`/`≤`; no rename. |
| linear helper | 0 | Same. |
| quadratic helper | 0 | Same. |

## Independent original/caller recovery and actual axioms

`lake build Roth.Theta` exited0 again after the arithmetic optimization; its final log reports
`Built Roth.Theta (43s)` and
`Build completed successfully (2423 jobs)`.

Only after that build, the successful verifier imported the actual built module and independently
reproved the immutable Index+Theta source under `Roth.IndexThetaOriginalAllProof`. This includes
the unmodified original proof of the audited theorem AND the entire original `index_le_lem6` proof.
It does not use the current theorem as an independent proof of the original.

`/private/tmp/roth-theta-min-sum/actual-compatibility.lean` and final
`optimized-actual-compatibility.log`: compiler exit0.
It checks retained effective binder names (except anonymous synthetic instance names), types,
BinderInfo, universe arity, exact original conclusion, explicit full-old-telescope lambda and
proof-value equality. The exact permitted drop set is `[hrp,hθ]` for the target and `[]` for its
caller. Every original caller binder, including `hq`, is retained.

The verifier prints:

```lean
fun {θ} {rp} hrp hθ l ↦ Roth.min_le_sum_max l
fun {τ} [Fintype τ] [DecidableEq τ] {δ} hδ0 hδ1 {r} hr0 hrp hratio {r₁} hr₁
    {q} hq {B} hB {R} hR {h} hh ↦
  Roth.index_le_lem6 hδ0 hδ1 hr0 hrp hratio hr₁ hq hB hR hh
```

Actual built target, actual built caller, both independent original proofs, both proof-value
recoveries, and both actual private helper constants use only
`[propext, Classical.choice, Quot.sound]`. The helper suffixes are located programmatically in the
built environment, rather than guessed as public constants:

- `_private.Roth.Theta.0.Roth.mul_div_two_le_sum_max_aux`
- `_private.Roth.Theta.0.Roth.mul_sq_div_three_le_sum_max_aux`

Positive new-identifier verification:

| Identifier | Evidence | Result |
|---|---|---|
| `Nat.pos_of_ne_zero` | successful final `#check` and module/LSP | pass |
| `div_nonpos_of_nonpos_of_nonneg` | same | pass |
| `mul_nonpos_of_nonneg_of_nonpos` | same | pass |
| `sub_div` | same | pass |
| `mul_div_cancel_right₀` | native local search positive hit, final `#check` | pass |
| `mul_nonneg`, `le_or_gt`, `sq_nonneg` | successful final `#check` and module/LSP | pass |
| existing triangular/floor/finite-sum lemmas | native positive search, concrete source inspection, successful selected proofs | pass |

Scratch corrections are not positive evidence: the initial adapter needed explicit real/natural
binder types to avoid an overloaded `10`/multiplication inference error; the first full-source
extraction accidentally stopped at the earlier Index namespace close and was corrected to include
BOTH original namespace blocks. Only the corrected final exit0 files/logs certify the results.
The independent zero-contradiction positivity probe also needed `norm_num` rather than bare simp.

## Complete final diagnostics

Fresh full unfiltered native `lean_diagnostic_messages` after the arithmetic optimization:
`/private/tmp/roth-theta-min-sum/optimized-final-lsp.json`.

`success=true`, `partial=false`, `timed_out=false`, `failed_dependencies=[]`, **0 errors,
17 warnings**. None is in the audited target/helper range. All are inherited, with line shifts:

- L1: protected short copyright metadata.
- L93,101,101,109,129,252: earlier retained unused `hr`/`hB` hypotheses.
- L367,367,364: later `sum_max_sub_le_index_det` unused DecidableEq/hR findings.
- L406,409,414,402: later `index_det_le` unused DecidableEq/hl'/hδ findings.
- L619: retained `Θ_option_le` DecidableEq finding.
- L521,515: retained caller `hq`/DecidableEq findings, reserved for its own original audit.

No header rewrite, suppression, or unrelated signature removal was used to reduce warning counts.

## Simplify and source gates

Manual holistic simplify review: **ISSUES-FOUND-AND-FIXED**. A separate built-in `/simplify`
invocation is not exposed in this session, so no nonexistent tool invocation is claimed.
The substantive fixes are the deletion of unnecessary termwise max equalities, the two independent
estimates, and the unconditional sign/zero treatment. No unhandled holistic issue remains for the
original. New helpers still require their independent fresh audits.

| Gate | Status | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit0; `final-module-build.log`, built target43s. |
| definition_protected | pass | No def/abbrev change. |
| theorem_statement_protected | pass, authorized strengthening | Exactly the approved `[hrp,hθ]` deletion; independent full-old recovery succeeds. Sole caller's entire type/value recovered. |
| structure_gate | pass for original | Main13; extracted independent helpers12/26; all branches≤10; no conjunction. |
| naming_gate | pass | No prohibited abbreviation/scheme pattern; no rename queued. |
| line_packing_gate | pass | Measured complete tables above. |
| inequality_orientation_gate | pass | Zero reversed code inequalities; protected source prose retained. |
| complete native LSP | pass | Fresh optimized-source unfiltered full result above. |
| original nonself proof/type/value | pass | Corrected final actual-compatibility exit0, independent immutable source namespace. |
| actual axioms | pass | Actual built original, caller, both helpers, and independent original recoveries: standard3 only. |
| source hygiene | pass | `git diff --check -- Roth/Theta.lean` clean; no sorry/native_decide/new axiom/limit/debug option/TODO/FIXME in Theta. |
| full build + separate LeanEval | owner pending | Owner performs both sequentially on frozen source after helper audits. No worker claim of completion. |

No shared rename queue or learning log mutation. Refactoring owed by owner: two fresh private-helper
audits; frozen whole-project build followed separately by LeanEval; final all-original compatibility
sweep and actual whole-module profiling after the later reserved slow caller is cleaned.

## Initial helper inventory for fresh dedicated audits

Helpers are **not counted as original declarations** and have not been represented as independently
completed cleanup leaves. Each needs its own fresh dedicated audit after this original freeze.
The initial declarations/contracts were preserved before performance edits:

| Initial private helper | Initial body | Frozen body | Contract |
|---|---:|---:|---|
| `Roth.mul_div_two_le_sum_max_aux` | 11 | 12 | For real `θ,r`, `0<r`, natural `l` with `l≤θ*r`, conclude `l*θ/2≤∑ν<l max 0 (θ−ν/r)`. |
| `Roth.mul_sq_div_three_le_sum_max_aux` | 25 | 26 | For real `θ,r`, `0<r`, `0≤θ`, natural `l` with `θ*r<l`, conclude `r*θ²/3≤∑ν<l max 0 (θ−ν/r)`. |

Full initial contracts:

```lean
private lemma mul_div_two_le_sum_max_aux {θ r : ℝ} (hr : 0 < r) {l : ℕ} (hl : (l : ℝ) ≤ θ * r) :
    l * θ / 2 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r)
private lemma mul_sq_div_three_le_sum_max_aux {θ r : ℝ} (hr : 0 < r) (hθ : 0 ≤ θ) {l : ℕ}
    (hl : θ * r < l) : r * θ ^ 2 / 3 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / r)
```

Snapshots under `/private/tmp/roth-theta-min-sum/`:

- **Initial compiled full source to use for helper-original recovery:** `edited-source.lean`,
  SHA256 `08e55dec3fe02fe2cf3c9324eca959cf60c81f180bee5af389b9f5aa40ea1248`.
  It contains the exact initial11/25-line helper proofs and was certified by first-stage module
  build/full LSP/actual compatibility. The only later source edits narrow arithmetic in the helpers.
- Exact initial two-helper text: `initial-helpers.lean`, SHA256
  `f87ff08d34f1db5705f643ee0fbf779eadacc50064cde54da2457868438bb23b`.
- Literal first-introduction full snapshot: `initial-helpers-full-source.lean`, SHA256
  `154c5f6a6c71e6f525255fae7e3aaf78ab746485849305cd3294fd3f00b1bfac`.
  This predates adding the necessary named implicit parameters at the sole caller; it is historical
  evidence of unchanged initial helper bodies, not a claimed successful full-source build.
- Frozen optimized full source: `frozen-source.lean`; exact final helper text: `final-helpers.lean`.
  Contracts, names, visibility, and all data domains are unchanged from the initial helper snapshot.

## Eleven-step completion checklist

- [x] Step1 — skills, full worker workflow and required references read.
- [x] Step2 — all24 substantive audit items answered, every original `have` inventoried.
- [x] Step2.5 — all5 actual mathlib search methods, auxiliary variants, clean bounded compiler routes.
- [x] Step2.6 — every effective binder mechanically probed; literature/inversion review; exact approved extension.
- [x] Step2.7 — measured complete signature packing tables, including conclusion lines.
- [x] Step2.8 — per-declaration inequality scan table.
- [x] Step3 — all42 golfing rules have a concrete status.
- [x] Step4 — holistic reflection and alternative proof strategies reviewed.
- [x] Step5a — fresh COMPLETE native full-file diagnostics on final optimized source.
- [x] Step5b — module build, actual-constant original/caller recovery, standard axioms and hygiene gates.
- [x] Step6a — no rename required; shared rename queue unchanged.

Comments-preserved: all original source narrative retained; no original body comments existed.
Renames-queued: none. Original-scope substantive issues fixed: independent-branch decomposition,
unnecessary hypotheses, unnecessary max-equality proofs. New helpers remain separately auditable.

## Buzz / actual final performance gates

**Outcome: FIXED — all final declarations below the 1000ms budget.**
Normal builds/LSP/ordinary compiler probes were completely drained before each real profile.
Every invocation used the actual Lean4.34 command:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE
```

These are exact source-prefix profiles, ending immediately after `min_le_sum_max` and closing the
existing namespaces/section. They preserve the preceding source/imports/context. They do NOT
certify caller or whole-module profiling: the later known `index_le_lem6` instrumentation heartbeat
failure remains reserved for its own original audit and the owner's final whole-module sweep.
No production limit or profiling option was added.

| Declaration | Initial source profile | Required repeat | Final optimized profile | Verdict |
|---|---:|---:|---:|---|
| immutable-release `min_le_sum_max` | 934.905ms | 837.370ms | 259.890ms | pass |
| linear helper | 1009.421ms | 403.735ms | 351.522ms | pass |
| quadratic helper | 1794.840ms | 756.991ms | 527.652ms | pass |

Before optimization, the first implementation's public proof measured470.379ms, repeated248.305ms.
The baseline repeat was mandatory because its first reading was≥750ms; the first helper-source
repeat was mandatory for the same reason. On the frozen optimized source every measured declaration
is<750ms, so no further repeat is required. All profile compiler invocations exited0.

The trace identified actual hotspots: the linear `nlinarith` closure took542ms, and the quadratic
closure1229ms, including760ms in nonlinear extras that discover squares/products. The fix supplies
those mathematical nonnegative-product/square facts explicitly and uses `linarith only`.
The quadratic argument first abstracts `θ*r` as a single real `a`, so arithmetic normalization
handles a small quadratic expression instead of expanding products of independent variables.
This adds one body line to each helper and improves predictable elaboration without changing types.

Timing aggregation sums the outer `Elab.command` with associated top-level async proof,
`addDeclCore` kernel/compiler work and linters. Nested children are not counted again.
Linters are included conservatively. Raw UTF-8 logs, source snapshots and declaration anchors:

- `baseline-prefix.lean`, `baseline-profile.log`, `baseline-target-anchor.txt`.
- `baseline-repeat-profile.log`, `baseline-repeat-profile-min_le_sum_max-anchor.txt`.
- `final-prefix.lean`, `final-profile.log`, `final-repeat-profile.log` (first helper implementation).
- **Final:** `optimized-final-prefix.lean`, `optimized-final-profile.log`,
  `optimized-profile-status.jsonl`, and all three
  `optimized-final-profile-<declaration>-anchor.txt` files.

All reside under `/private/tmp/roth-theta-min-sum/`.
maxHeartbeats raises removed:0; added:0. Slow original-scope declarations deferred: none.
The separate helper audits and owner's later whole-module sweep remain required publication work.

## Final freeze and handback

Final Theta SHA256:
`235a2a6a64ae919e1fbb884eb7bc2287d74996e4133bf25180385c37cec262aa`.
`frozen-source.lean` matches the live file byte-for-byte. Source diff:60 insertions/48 deletions,
net+12 lines; original main body46→13. Every pre-existing public definition and unrelated public
statement is protected, with the exact authorized target condition removal and sole caller proof
adaptation independently verified.

Final module build: exit0 (`final-module-build.log`, target43s).
Final full native LSP: zero errors, unchanged17 warnings, complete/nonpartial/no timeout/no failed deps
(`optimized-final-lsp.json`). Final actual built type/value/BinderInfo/standard-axiom verification:
exit0 (`optimized-actual-compatibility.log`). Final target+helper profiles: pass as above.
No running compiler/LSP/search/profile request remains.

**Source editing is frozen/revoked for this leaf.** The owner now arranges exactly two separate fresh
helper audits, then frozen sequential full build and separate LeanEval, final compatibility and
publication. This report does not claim those owner gates have run and does not count helpers as
additional originals.


## Final owner-frozen helper batch

The separate fresh helper audits supersede the earlier leaf freeze and two-helper handoff
above. All **three** helpers now have their own dedicated fresh audit; none contributes to
original-declaration counts:

- [Linear estimate](Theta-mul_div_two_le_sum_max_aux-helper.md): remove its private `hr`
  assumption by handling the degenerate/sign cases; final15 proof lines.
- [Quadratic wrapper](Theta-mul_sq_div_three_le_sum_max_aux-helper.md): remove private `hr`,
  weaken the cutoff to `θ * r ≤ l`, and extract the positive/strict core to satisfy the
  branch-length gate; final7 proof lines. The public min proof simplifies13→7 lines.
- [Positive quadratic core](Theta-mul_sq_div_three_le_sum_max_of_pos_aux-helper.md):
  independent first-introduction proof/type/value/axiom recovery, all effective binder
  probes and boundary alternatives; inline single-use `hn`, final22 lines and no new helper.

Final Theta SHA256 `e6360c9acdc9d7be22356ba3a26006e24cc1b0b667b5992395759228e1087530`,
983 source lines (published original25 source968). Public original26 proof46→7 lines.
The public target exact drop set remains `[hrp, hθ]`; all names, retained binders/modes,
real/natural domains and conclusion remain. The sole caller uses named θ/rp inference
arguments; its complete original effective type, including hq and DecidableEq, is preserved.
No other original declaration is counted by this batch or by these routine proof edits.

On this exact final source, the final helper leaf ran `lake build Roth.Theta` successfully,
then full **unfiltered** native diagnostics: success=true, partial=false, timed_out=false,
failed_dependencies=[],0errors17warnings. Independent initial core proof and actual opaque
proof values (`value! true`), exact names/types/BinderInfo/universes, and standard axiom sets
pass. The immutable full original Index+Theta proof replay re-ran byte-identically from
`/private/tmp/roth-theta-min-sum/actual-compatibility.lean` (SHA256
`bcb7e0d315c6b7277d83279f0bc147d70ed7e3f608e5e3111deb4ef5f768cafe`),
exit0 in55.562s, recovering both the min exact old telescope and the **entire** original
index_le_lem6 proof/type. Actual current linear/quadratic/public/caller axioms and the
separate current positive-core axioms are standard only. Prior helper first-contract
adapters remain supported by byte-identical assigned declarations; the last audit changes
only the new positive core's internal proof. Initial erroneous scratch runs are explicitly
superseded by the clean successful runs in the individual reports.

After all ordinary requests drained, the final uncontended exact-prefix real profiler
completed exit0 in99.527s, including all preceding source/imports/context through public min:
linear460.921ms, positivecore543.552ms, quadraticwrapper304.757ms, publicmin165.806ms.
All are below750ms, so no further repeat trigger fires; all meet the1000ms budget. These
per-declaration totals include outer command and disjoint proof/kernel/compiler/linter work;
nested children are not double-counted. This structural/generalisation batch is not claimed
to reduce the aggregate implementation cost relative to the old proof. No whole-Theta
performance pass is claimed: the known later instrumented index_le_lem6 default-heartbeat
failure remains reserved to original29. No limits raised or masking/scaffolding introduced.

Final raw UTF-8 logs and exact source correspondence manifest:
`/private/tmp/roth-theta-positive-audit/{final-module-build.log,final-lsp.json,actual-positive.log,
immutable-public.log,final-profile.log,profile-status.jsonl,evidence-manifest.json}` and the
four declaration anchor files. Owner verified all manifest file hashes, no PANIC/error/sorryAx
in the positive verification logs, and both exact-original PASS markers. All helper source
and report ownership is revoked, with requests drained. Owner cumulative full build, then
separate LeanEval and publication gates follow below.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (92.510 s),
then separate `lake build Roth.LeanEval` (33.553 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `e6360c9acdc9d7be22356ba3a26006e24cc1b0b667b5992395759228e1087530`.
Raw logs: `/private/tmp/roth-theta-d26-full.log`, `/private/tmp/roth-theta-d26-leaneval.log`; machine record
`/private/tmp/roth-theta-d26-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 26/35, overall 207/264 original
declarations, 9/14 completed files. Three new private helpers each received separate fresh dedicated audits; final bodies linear15, positivecore22, quadraticwrapper7. Helpers add0 original declarations.
