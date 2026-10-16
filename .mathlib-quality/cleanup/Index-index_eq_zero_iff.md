# Cleanup: `Roth.index_eq_zero_iff`

Fresh single-declaration worker on `ramin-cleanup`, owner-supplied starting HEAD `4e77c87`. Source authority released and revoked at SHA256 `089b92ef70eee154e17169baf76710e227ed3dc3f8f1894496a006eca0fd86b5`. All worker Lean requests and compiler processes finished before release. Subsequent activity is report writing only. No Git operations, whole-project build, separate LeanEval, other declaration edits, or shared-report changes by this worker.

## Result and mathematical argument

Applied precisely the approved `omit [DecidableEq σ] in` before the unchanged docstring. Normalized the two mathematical lambda arrows from `=>` to `↦`. No other source changes. The literal theorem signature is unchanged, but the public type **has changed**: its formerly inherited `DecidableEq σ` argument is absent. No helper, import, rename, attribute, definition change, weakened conclusion, limit raise, or trust extension.

For the forward implication, a nonzero polynomial supplies an attained minimum weight. If that minimum is zero, positive denominators imply that the attaining multi-index is zero, whose Hasse derivative is the original polynomial. Conversely, a nonzero value supplies a nonzero coefficient at the zero multi-index. Its zero weight bounds the index above; nonnegativity bounds it below.

Declaration lines: 8 → 8; proof body: 6 → 6; scoped omission adds one file line, 269 → 270. The main theorem stays below the 15-line headline threshold. No deferred refactoring or renames.

## Reference and preparation record

Read the fresh-worker contract, Lean 4 and mathlib-quality SKILL.md instructions, the complete cleanup command including the fresh Phase-4 worker contract, and cleanup-all ownership/reporting requirements. Read the golf checklist, proof patterns, mathlib search, generalisation patterns, cleanup gates, naming, profiling and buzz documents; relevant style sections on signature packing, lambda syntax, comments/docs, inequalities, hypotheses, tactics, visibility, imports, casts, and normal forms; review-stage normal-form, syntactic-generality and documentation sections; curated PR-feedback examples. Read the complete 269-line target file, its original target in `/private/tmp/roth-index-original.lean`, and the relevant Box weight API/source literature.

Dialect: classic imports, no module-system conversion. The owner controls file headers and file-wide cleanup. Existing header warnings remain visible and were not suppressed or repaired by guessing metadata. The owner supplied a green published baseline. Worker baseline native target diagnostics completed with success=true, partial=false, timed_out=false and one observed unused-section-variable warning for DecidableEq.

## Full audit — 24 items

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | LINT | Baseline native target range returned one unusedSectionVars warning for DecidableEq. Approved omission applied. Final target-range diagnostics complete with no items; full unfiltered diagnostics are an owner checkpoint, explicitly distinguished below. |
| 2 | HAVE SCAN | No `have` declarations in original/final body. The `obtain` destructures a nontrivial attained-minimum witness and is retained. |
| 3 | SET_OPTION | No declaration-scoped options, heartbeat overrides, debug options, or recursion overrides. |
| 4 | SIMP SQUEEZE | Three terminal `simpa` calls: forward derivative-zero conversion; outer reverse weight-zero conversion; nested reverse derivative-zero conversion. None is nonterminal bare simp or terminal simp only; no squeeze needed. |
| 5 | NAMING | `index_eq_zero_iff` is descriptive snake_case, follows its LHS equality, and contains no forbidden abbreviation, numeric scheme, single-letter public name, `_ge_`, or `_gt_`. No rename queued/applied. |
| 6 | LINE PACKING | Both signature lines measured; 93+1+11=105 justifies the break before α. Conclusion and `:= by` packed with α. Full table below. |
| 7 | BY PLACEMENT | `by` at the end of signature line 97. |
| 8 | FORMAT | Two-space proof indent, four-space signature continuation, focused branches, no blank internal lines or semicolon chain; no haveI/letI. Two lambda arrows normalized to ↦. |
| 9 | COMMENTS | Zero inline proof comments before and after; none deleted. Existing docstring byte-identical. |
| 10 | DOCSTRING | Public docstring describes the nonzero/positive-weight equivalence and gives the exact source location. Preserved per explicit protection. |
| 11 | VISIBILITY | Public headline API listed in module results, used in index_prod. No visibility change. |
| 12 | STRUCTURE | Six body lines, longest branch four lines; ↔ rather than conjunction; no helper/extraction needed. |
| 13 | MATHLIB | Five methods actually attempted below. Remote services unavailable due DNS; local weightedOrder ingredients verified. No absence claim or duplicate replacement inferred from unavailable services. |
| 14 | JUNK DEF | n/a: theorem, and protected index definition untouched. |
| 15 | EXISTS LEMMA | n/a: public equivalence, not a trivial private existential wrapper. |
| 16 | SHOW/CHANGE | Neither in proof. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All eight actual inherited/explicit binders probed/classified below, plus the fixed-type generalisation check; only approved decidability omission applied. hP/hr retained. |
| 19 | INEQUALITY | Positivity hypothesis already `0 < r j`; zero reversed inequalities, table below. |
| 20 | NORMAL-FORM | Equality-to-zero on LHS, evaluation nonvanishing on RHS gives the useful polynomial-value criterion. No competing equivalent-form family introduced. |
| 21 | SYNTAX-GEN | Implicit P/r and explicit hP/hr/α support direct application; no bundled-property conversion improves current calls. |
| 22 | IMPORT-FANOUT | n/a: no imports added/removed. |
| 23 | CASTS | casts: 0 dropped / 0 kept cross-type / 0 kept load-bearing in diff; no coercion/ascription churn. |
| 24 | INSTANCE-NAME | n/a: no instance declaration; scoped omission uses an existing anonymous class binder. |

Issues fixed: unused σ-DecidableEq, two lambda-arrow occurrences. Refactoring needed: none. Existing unrelated file warnings belong to later declaration owners.

## Five-method mathlib search

Tool schemas discovered through ALL_TOOLS metadata. Bounded direct MCP helper attempts used the installed lean-lsp-mcp Python runtime. Each remote call returned a completed tool error rather than hanging; each was unavailable, **not a negative result**.

| Method | Actual query | Result/evidence |
|---|---|---|
| A Lean-Finder | `weighted polynomial index zero iff value nonzero`, num_results=3 | DNS failure (`nodename nor servname provided, or not known`), `/private/tmp/eq-zero-finder.json`; no absence conclusion. |
| B Loogle | `sInf, _ = 0`, num_results=3 | DNS failure, `/private/tmp/eq-zero-loogle.json`; no absence conclusion. |
| C LeanSearch | `minimum weighted degree zero iff constant coefficient nonzero`, num_results=3 | DNS failure, `/private/tmp/eq-zero-leansearch.json`; no absence conclusion. |
| D Source | Untruncated `index_eq_zero_iff`, `weightedOrder_eq_zero`, `constantCoeff.*weightedOrder`, `weightedOrder.*constantCoeff` over Mathlib | Only similarly named group-index result, which concerns infinite quotients and is unrelated; weighted-order component references. Inspected actual Box weight_eq_zero_iff and coefficient/taylor APIs. |
| E Name pattern | Native lean_local_search `weightedOrder`, limit=20 | Positive hits for MvPowerSeries.weightedOrder, weightedOrder_le, weightedOrder_eq_nat, weightedOrder_zero/one/neg/prod, weightedOrder_eq_top_iff, exists_coeff_ne_zero_and_weightedOrder. Symbol index reported warming, so positives establish presence but empty results could not prove absence. |

Auxiliary variants examined: weighted-order zero, nat-characterisation, finiteness/top, coefficient nonvanishing and lower bounds; `weight_eq_zero_iff`; `coeff_taylor`; derivative-zero and support-X facts. Fresh built `#check @MvPowerSeries.weightedOrder_eq_nat`, `#check @weight_eq_zero_iff`, `#check @MvPolynomial.coeff_taylor` succeeded in `/private/tmp/eq-zero-built.lean`. The common-equivalents table has no direct polynomial-index bucket. The generic weighted-order API is a partial conceptual match, but transporting through the protected rational-weight index would need more than a direct same-statement replacement. Retain the existing public index theorem and its short proof; no wrapper/helper added.

Native in-context `exact?` before the target was available failed to close the equivalence. `apply?` suggested generic logical rearrangements with residual goals, not an equivalent mathlib theorem. These are actual failed proof searches, not evidence of universal absence. Six replacement rules checked: no new wrapper/custom predicate; remote limits disclosed; auxiliary variants examined; no verified exact duplicate to delete; existing module documentation preserved rather than adding an unauthorized paragraph.

## Generalisation — every binder and mechanical probe

Fresh CLI snippets use `set_option autoImplicit false`, explicit binder lists, and the actual built `Roth.Index`. No missing data binder can be silently generalized back in. Inputs are `/private/tmp/eq-zero-<probe>.lean`; aggregate first-run record is `/private/tmp/eq-zero-binder-results.json`. Some early probes raced the module build and saw missing Index.olean. Those import failures were **discarded**, not accepted as binder evidence: finite_parent rerun in `/private/tmp/eq-zero-finite_parent-retry.log`; σ/P/hP rerun together in `/private/tmp/eq-zero-invalid-probes-retry.lean/.log`. All retries finished before release.

| # | Binder | Classification/use | Mechanical candidates tried | Verified result |
|---|---|---|---|---|
| 1 | `{σ : Type*}` | Type-variable, universe; polynomial/evaluation/weight domain | Drop with autoImplicit=false; inspect universe | Retry fails unknown σ in dependent binder types. Retain. Already Type*, no smaller fixed universe to generalize. |
| 2 | `[Fintype σ]` | Typeclass; index/weight finite sums | Drop; replace `[Finite σ]` | Both fail synthesis of Fintype σ in statement and proof; Finite retry confirms after valid import. Retain. Finite is not a direct replacement for the protected definition's Fintype argument. |
| 3 | `[DecidableEq σ]` | Decidability, unused section inclusion | Drop, original proof | Exit 0 without instance; actual module/LSP/built signature confirm omission. User-approved change applied before docstring. |
| 4 | `{P : MvPolynomial σ ℝ}` | Structure value, subject polynomial | Drop with autoImplicit=false | Retry fails unknown P in hP/conclusion/proof; retain. No weakening of a data value independent of its type. |
| 5 | `(hP : P ≠ 0)` | Proposition; attained-minimum witness | Drop | Retry fails unknown hP at exists_weight_eq_index. Built certified counterexample P=0 shows the statement is false without it under index 0=0 convention. No applicable order-weakening on polynomials. |
| 6 | `{r : σ → ℕ}` | Structure value, denominator function | Drop with autoImplicit=false | Unknown r in hr/index/calls; retain. |
| 7 | `(hr : ∀ j, 0 < r j)` | Proposition; zero weight detects zero multi-index | Drop; weak `∀ j, 0 ≤ r j`; point-local `∀ j ∈ P.vars, 0 < r j` | Drop fails unknown hr. Weak/local forms fail type checking at weight_eq_zero_iff, which needs global strict positivity. The local-form failure only rejects the unchanged proof, not the mathematical possibility of another theorem. Weak form is refuted by certified X(), α=0, r=0 counterexample. |
| 8 | `(α : σ → ℝ)` | Structure value, Taylor/evaluation point | Drop with autoImplicit=false | Unknown α in conclusion/calls; retain. |
| 9 | Implicit ℝ/ℕ structures | Fixed constants, not local binders | Concrete→abstract catalogue inspected | Altering coefficient or denominator types requires changing protected index/weight definitions; no such API edit/proposal applied. |

There are eight actual original binders when counting the two section instances and σ; the ninth row explicitly documents the fixed-type generalisation check rather than inventing a theorem binder. No continuity/filter/monotonicity/integrability hypotheses exist to point-localize. No bundled Bijective/embedding or algebraic parent-class assumptions occur. Strict/weak and relevant support-local positivity were actually tried. No silent hypothesis removal or instance strengthening.

Inversion check: the proof uses the index-specific attained-minimum and upper-bound APIs throughout; its generic minimum/nonnegative-weight reasoning is already expressed by Mathlib's csInf and coefficient API. A generic positive-weight finite-support minimum theorem is conceptually possible, but no missing plumbing API, repeated cast dance, or useful multi-caller helper emerges here. Broader real weights/fields require an owner-coordinated definition-family restatement; none recommended for this local checkpoint.

## Public literature search

Actual web queries:

1. `polynomial index Roth theorem index zero nonzero value positive weights generalization`.
2. `weighted order polynomial constant coefficient nonzero weighted valuation`.

The first combined call returned Princeton lecture notes, a book mirror, and weighted-order docs among its leading results. An individual-query rerun returned the Princeton lecture notes, a quantitative-version paper via CiteSeerX, and a Scribd book mirror as the first three displayed hits. The second individual query returned FLT-hosted Mathlib weighted-order documentation, official Mathlib documentation, and a hex-hosted Mathlib mirror as the first three. Secondary mirrors/search snippets were leads only; no mathematical assertion here relies on Scribd or unrelated additive-combinatorics Roth results.

Primary evidence: [Princeton Diophantine Analysis and Approximations notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), §14.6, Definition 14.6.4 and Lemma 14.6.5, define index using positive integer denominators and nonzero normalized derivatives over a field, with the expected zero-index/nonzero-evaluation direction. Section 17 repeats the minimum definition. Its extracted line 9068 has a contradictory zero-value direction, so that line was not used to justify the equivalence. The local project source `.mathlib-quality/references/clean.tex` §4 (530–569) explicitly allows positive real weights, proves the equivalence by attainment and positivity, and uses infinity for the zero polynomial. This repository instead uses real sInf and requires hP, so hP must remain. [Official Mathlib weighted-order documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/MvPowerSeries/Order.html) gives the natural-weight power-series formulation; the local pinned API is confirmed by compiled #check.

Inference from these sources: broader coefficient fields or positive real weights are mathematically natural, but require changing the protected definition family. They provide no justification for dropping strict positivity or the repository's nonzero-polynomial assumption. An attempted open of Roth's ICM 1958 PDF on mathunion.org returned an internal error; it contributes no evidence. ChatGPT math MCP: unavailable (no matching callable tool in ALL_TOOLS); no second-opinion result invented.

## Complete signature line packing

Actual built-module `#check @Roth.index_eq_zero_iff` with `set_option format.width 100` (not pp.width), `/private/tmp/eq-zero-built.log`:

```lean
@index_eq_zero_iff : ∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ},
  P ≠ 0 → ∀ {r : σ → ℕ}, (∀ (j : σ), 0 < r j) → ∀ (α : σ → ℝ), index P α r = 0 ↔ (eval α) P ≠ 0
```

The DecidableEq argument is actually absent. The source signature's inherited arguments are shorter than the expanded type. Both original/final source signature lines have the same codepoint lengths.

| Signature line | Chars | First next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| Original 95 / final 96 | 93 | `(α : σ → ℝ)`, 11 codepoints | 93 + 1 + 11 = 105 > 100 | ok: break required |
| Original 96 / final 97 | 54 | none; `:= by` already on this line, proof follows | n/a: final signature line | ok |

The conclusion, colon and := by are on the α line. No dangling conclusion, no unmeasured signature lines, no ≥95-character hypothesis escape needed. Measurement used Python len on Unicode source strings, not UTF-8 byte counts.

## Inequality orientation table

| # | Location | Original/final | Rewrite | Rename? |
|---|---|---|---|---|
| 1 | hr, final signature 96 | `0 < r j` | none; smaller-left strict positivity | no |
| 2 | Whole signature/hypotheses | zero `≥`/`>` tokens | n/a: no reversed inequality | no `_ge_`/`_gt_` in name |

Equality/inequality-to-zero `≠` are not reversed order inequalities. No source prose needs alteration.

## All 42 golf rules

| Rule | Status and concrete reason |
|---|---|
| 1.1 by exact wrapper | n/a: no by-exact-only wrapper. |
| 1.2 by rfl | n/a: no rfl proof. |
| 1.3 rw + exact → rwa | n/a: rw changes hdw, then subst and simpa are necessary; no immediately following exact. |
| 1.4 simp + exact → simpa | Already three terminal simpa calls. |
| 1.5 trailing rfl | n/a: no trailing rfl. |
| 1.6 constructor + exact → pair | Already refine ⟨forward, reverse⟩; branch witnesses require tactics. |
| 1.7 apply + exact | n/a: no such pair. |
| 1.8 by_contra + push_neg | n/a: no contradiction block. |
| 1.9 eta reduction | Both lambdas carry distinct proof work/placeholders; no eta-redex. Their arrows normalized to ↦. |
| 1.10 inline single-use have | n/a: zero haves. |
| 1.11 apply + intro | n/a: no apply/intro sequence. |
| 1.12 redundant show | n/a: none. |
| 1.13 have + projections | Already obtain ⟨d, hd, hdw⟩; no projection boilerplate. |
| 1.14 merge rw | Single rw call already merges h and weight_eq_zero_iff. |
| 1.15 unsqueeze terminal simp only | n/a: no simp only. |
| 1.16 squeeze nonterminal simp | n/a: all simpa calls terminal. |
| 1.17 dot notation | Existing `(index_nonneg ...).antisymm'` is direct dot notation. |
| 1.18 use <\| | Parenthesized nested proof is a named-argument application followed by `using`; changing its presentation provides no clarity/line benefit. No trailing lambda parentheses to remove. |
| 1.19 push_neg → push Not | n/a: none. |
| 1.20 inline trivial existential | n/a: exists_weight_eq_index is a nontrivial public API result; target is an iff. |
| 2.1 grind whole proof | Native multi_attempt at first tactic failed with the open zero-index/zero-value contradiction; retained explicit minimum argument. |
| 2.2 delete before grind | n/a: retained proof contains no grind. |
| 2.3 simpa consolidation | Already used; native reverse-branch trial removing explicit hasseDeriv_zero_apply also closed. Retained explicit derivative-zero hint to expose the mathematics and avoid marginal list churn. |
| 2.4 fun_prop | n/a: no analytic function-property goal. |
| 2.5 positivity | Actually tried on reverse `index ... ≤ 0`; failed `not a positivity goal`. Cannot prove upper nonpositivity structurally. |
| 2.6 gcongr | n/a: upper zero bound requires a nonzero constant coefficient, not monotonicity of arithmetic operations. |
| 2.7 lia/omega | n/a: no Nat/Int linear-arithmetic target; polynomial evaluation iff and real minimum. |
| 2.8 aesop | Actual native attempt leaves both implications/contradiction open, exhaustive search warning. |
| 2.9 norm_num/norm_cast | n/a: no concrete numeric/cast computation in the retained proof. |
| 2.10 decide/kernel | n/a: quantified real-polynomial assertion is not finite decidable computation. |
| 2.11 field_simp; ring | n/a: no denominator identity goal. |
| 2.12 linear_combination | n/a: no ring/ring_nf endpoint or polynomial identity with algebraic hypotheses. |
| 2.13 wlog | n/a: iff directions have different arguments, no symmetric cases. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 <;> | Branches are mathematically different; shared automation trial on reverse branch failed, so no common closure. |
| 3.1 erw → rw | n/a: no erw. |
| 3.2 continuity/measurability | n/a: neither tactic/property occurs. |
| 3.3 omega → lia | n/a: no arithmetic automation. |
| 3.4 rcases with rfl | Subst hdw already replaces d=0 after rewriting the weight characterization; no redundant later equality simplification. |
| 3.5 register automation | No new attribute: hP/hr are conditional inputs and changing global simp/grind behavior is outside this local cleanup. |
| 3.6 simp_all | n/a: no simp_all only. Native whole simp trial did not close the index iff. |
| 3.7 remove limits | n/a: no overrides. |

Step-back reflection: tried whole-goal grind/simp/aesop, exact? and apply? through actual native tooling. None replaced the minimum argument. The tool replaces a selected tactic and retains later source, so diagnostics about later unknown `h`/extra goals were not treated as primary proof-search failures; the first-tactic residual goal/failure is the evidence. A second native trial at the reverse branch found that `simpa ... (by simpa using h)` also succeeds, but this is a tiny hint-list change rather than a clearer proof strategy. The existing six-line proof cleanly expresses both directions; no successful nontrivial alternative was selected without measurement. Term mode would embed the same obtain/rewrite/subst block and is less direct here.

## Verification, compatibility and trust

| Gate | Actual evidence | Result |
|---|---|---|
| lake_build_file | `/Users/ramin/.elan/bin/lake build Roth.Index > /private/tmp/eq-zero-module-build.log 2>&1`, process 69717 exit 0; built Index in 18s, final build success 1501 jobs | pass |
| Target native diagnostics | final lean_diagnostic_messages with file_path Index, start_line=93, end_line=104, timeout_s=40: success=true partial=false timed_out=false items=[] failed_dependencies=[] | pass for target |
| Complete whole-file diagnostics | Worker final query was target-filtered, although elaboration returned complete. Owner explicitly notified after freeze and will obtain unfiltered whole-file diagnostics | owner checkpoint; not misreported as worker result |
| definition_protected | diff against `/private/tmp/eq-zero-start.lean`: no def/abbrev or other declaration edit | pass |
| theorem_statement_protected | Exact original signature text preserved; public type changes only through explicitly approved DecidableEq omission | pass under scoped approval |
| structure_gate | Six body lines, four-line longest branch, headline limit 15, no conjunction statement | pass |
| naming_gate | descriptive snake_case, no prohibited pattern | pass |
| line_packing_gate | Both measured rows above, no repack row | pass |
| inequality_orientation_gate | table above, zero reversed inequalities | pass |
| Original type recovery | `/private/tmp/eq-zero-built.lean` has the original σ/Fintype/DecidableEq/P/hP/r/hr/α binder order and conclusion, proved by actual built `Roth.index_eq_zero_iff hP hr α`; fresh CLI rerun process 40186 exit 0 | pass |
| Independent original-type proof | `/private/tmp/eq-zero-independent.lean` imports the original imports but NOT Roth.Index; reconstructs the literal original index definition, proves original type via csInf_mem/csInf_le and coefficient_taylor directly; never uses the target, mem_support_taylor_iff, exists_weight_eq_index, index_nonneg, index_le_weight, or any same-file theorem shortcut. CLI process 6301 exit 0 | pass |
| Actual target axioms | built `#print axioms Roth.index_eq_zero_iff`: propext, Classical.choice, Quot.sound | standard only |
| Independent axioms | `#print axioms Roth.independent`: propext, Classical.choice, Quot.sound | standard only |
| Hypothesis counterexamples | Built scratch certifies negation of iff at zero polynomial and at X(), point 0, zero denominator; final process 40186 exit 0 | pass |
| New identifiers | No new referenced declaration identifiers in source diff; only existing DecidableEq in omit and arrow syntax. Actual built target signature/axiom check also succeeds | pass, no hallucinated name |
| Comment preservation | Exact diff contains only one omit line and one lambda-arrow line replacement; existing docstring and all other comments unchanged, zero inline comments before/after | pass |
| Limits/scaffolding | None added, source diff checked before freeze | pass |
| Whole project / external callers / LeanEval | Reserved to owner after freeze; worker makes no full-project claim | owner checkpoint |

The independent original-type proof intentionally retains its original DecidableEq binder and receives an unused-section-variable warning; it still compiles with standard axioms and no sorry. This does not introduce a target-source warning. Its first draft failed because a csInf bound was not unfolded through the scratch index definition; repaired using `simpa [index]`, then rerun exit 0. The counterexample's first draft needed explicit `support_X` in terminal simp; repaired and rerun exit 0. Failed drafts and their sorryAx diagnostics were discarded and are not accepted proof/trust evidence.

## Scoped simplify and buzz

Scoped holistic simplify review: pass-through after approved omission/arrow fixes. The minimum argument is already shared through useful public APIs, no duplicated proof skeleton or new helper is warranted. The built-in simplify Skill tool is not exposed in this environment; the owner controls the required fresh file-wide independent simplify pass. No such hand-off is fabricated here.

Actual anchored profiling commands, both exited 0:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean > /private/tmp/roth-index-eq-zero-before-profile-trace.log 2>&1
python3 /private/tmp/roth-index-profile-parse.py eq-zero-before
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean > /private/tmp/roth-index-eq-zero-after-profile-trace.log 2>&1
python3 /private/tmp/roth-index-profile-parse.py eq-zero-after
```

Parser asserts all 19 current source declarations are anchored and writes the two profile-table JSONs. Target figures are anchored totals, not aggregate profiler categories:

| Target | Before command | Before proof | Before total | After command | After proof | After total |
|---|---:|---:|---:|---:|---:|---:|
| index_eq_zero_iff | 5.81ms | 108.20ms | 117.89ms | 7.36ms | 144.92ms | 154.51ms |

Baseline dominant step: forward simpa at 44.934ms; final dominant step: reverse simpa at 67.824ms. These measurements do not establish a speedup; the tiny syntax/instance change is not claimed as a performance optimization. Both are far below 750ms borderline and the 1000ms budget; no extra resweep or repair required for this target. Native lean_profile_proof was actually tried at line 96 and failed to extract a standalone snippet because scoped omit/same-file declarations are not reproduced; disclosed fallback is the actual source-anchored CLI trace above. No limit raises, deferred slow declaration, root-cause fix, profiling scaffolding, or global change. Outcome: FAST-BOARD for the scoped target. File-final profile sweep remains owner's gate.

## Required 11-step checklist

- [✓] Step 1 — mandatory reference/contract reading; skill use announced before editing.
- [✓] Step 2 — all 24 audit items recorded above.
- [✓] Step 2.5 — all five methods actually attempted; remote DNS failures disclosed, local positives verified.
- [✓] Step 2.6 — all binders classified/dropped mechanically with autoImplicit=false; parent, weak and local probes; public literature; scoped omission only.
- [✓] Step 2.7 — every signature line measured with Unicode codepoint arithmetic and actual built format.width100 check.
- [✓] Step 2.8 — inequality table emitted, zero reversed code inequalities.
- [✓] Step 3 — all 42 rule slots have concrete statuses.
- [✓] Step 4 — whole-proof/search alternatives and proof-strategy reflection completed.
- [✓] Step 5a — complete nonpartial native elaboration returned clean target-filtered diagnostics; complete unfiltered whole-file diagnostic collection explicitly handed to owner.
- [✓] Step 5b — source diff, module build, proof/trust/compatibility and structural gates above; owner-only whole-project gates clearly separated.
- [✓] Step 6a — no rename needed or applied, no sidecar queue edit.

Overall scoped result: pass, with owner checkpoints for whole-file unfiltered diagnostics, independent file-final simplify/profile, cumulative original compatibility, full build and separate LeanEval. The source remains frozen at the released hash; this report does not claim those owner checks have already happened.


## Owner checkpoint d09

Frozen SHA256 `089b92ef70eee154e17169baf76710e227ed3dc3f8f1894496a006eca0fd86b5`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session76431 exit0, `/private/tmp/roth-index-d09-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval20223 both exit0(164.93s/36.44s),
Index+Theta hashes stable; `/private/tmp/roth-index-d09-{full,leaneval}.log`.
Worker final target-filtered diagnostics clean; owner unfiltered COMPLETE Index native diagnostics after fullbuild success=true partial=false timed_out=false, no faileddependencies, 0errors/23unrelated warnings, targetlines93–104 empty. Raw /private/tmp/roth-index-d09-index-lsp.json. Source rg finds only internal index_prod caller, accepted by module/fullbuild; no external caller to query.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
