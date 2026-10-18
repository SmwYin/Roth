# Dedicated original24 audit: `Roth.floor_sq_div_two_le_sum`

Fresh dedicated leaf; only this original declaration audited. Immutable original: `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`. Released checkpoint: `c711c7135fa1cc307a8ab9ca7b49051c69279d80`; released Theta SHA256 `5c4aa2d1347aba94a182fdbe58a06e78f19ada9568e8f0b33876469ce8781cea`.

## References and baseline

Read `lean4/SKILL.md`, `mathlib-quality/SKILL.md`, complete cleanup worker workflow, full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, profiling, and relevant declaration formatting, casts, naming, documentation, and visibility references. The task-specific leaf instructions override generic API/visibility policies and prohibit unrelated edits and shared logs.

Inherited baseline doctor: owner reports full build exit0 in 73.770s, followed separately by Roth.LeanEval exit0 in 26.327s. Complete unfiltered baseline LSP `/private/tmp/roth-theta-one-le-m/final-lsp.json` on identical released source: success=true, partial=false, timed_out=false, failed_dependencies=[], 0 errors, 17 warnings. No warning in target range 284–296. Existing warnings elsewhere and header metadata stay with their assigned owners. Cache/bootstrap not needed.

Fresh baseline real profile: exact source prefix through this declaration, with section/namespace closing commands appended, `/private/tmp/roth-theta-floor-sum/baseline-prefix.lean`. Command `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-floor-sum/baseline-prefix.lean`, exit0. Raw UTF8 log `baseline-profile.log` in that directory. This is prefix-only evidence, not a complete-module profile. Target outer command 43.033ms + associated async proof 433.049ms + kernel/addDecl 16.533ms + linters 10.662ms = **503.277ms**. Nested value 427.375ms and nested kernel 16.483ms are not counted again. Below 750ms repeat threshold and 1000ms budget. No concurrent compiler/LSP request during measurement.

## Mathematics and full 24-item audit (before edit)

Write n=⌊a⌋₊. Gauss' formula gives 2∑ν=(n+1)n, so the right side is (n+1)a−n(n+1)/2. Since 0≤n≤a, this is at least n²/2. The proposed edit keeps this mathematics and crosses the cast bridge once, removing the intermediate natural equality and redundant named floor bound.

| Item | Concrete finding/action |
|---|---|
| 1 LINT | No target diagnostic in inherited complete LSP. Fresh final complete LSP required below. |
| 2 HAVE SCAN | `hn` has no by, used only by terminal nlinarith: inline as `Nat.floor_le ha`. `h1` is used to simplify then cast: merge construction into `congrArg`. `h2` has proof content: replace entire cast block with directly cast Gauss equality. Inner anonymous `have` used by push_cast and exact: remove intermediate handoff. Final `hsum` is rewritten and used by nlinarith, so retained. |
| 3 SET_OPTION | None in target; no limit/debug option introduced. |
| 4 SIMP SQUEEZE | Existing nonterminal `simp only [Nat.add_sub_cancel]` remains explicit. No terminal simp to unsqueeze. |
| 5 NAMING | `floor_sq_div_two_le_sum` describes the left expression and comparison; snake_case, standard `sq`/`div`/`le`, no forbidden abbreviation or numeric scheme. Rename unnecessary. |
| 6 LINE PACKING | Measured two signature lines below; full conclusion does not fit after first line. Signature unchanged. |
| 7 BY PLACEMENT | `:= by` ends conclusion line. |
| 8 FORMAT | Two-space tactics, no blank proof lines, no semicolon chains, no haveI/letI; selected proof has six lines. |
| 9 COMMENTS | No inline comments originally; docstring and source quotation preserved byte-for-byte. |
| 10 DOCSTRING | Existing public source-based mathematical description retained. |
| 11 VISIBILITY | Public API retained per task instructions; only local caller is min_le_sum_max. No visibility churn. |
| 12 STRUCTURE | Original 11 body lines, selected 6; no conjunction, branch, or extraction threshold; no helper added. |
| 13 MATHLIB | Five actual methods and clean anonymous exact?/apply? probes below. Partial match is Gauss formula; no exact replacement established. |
| 14 JUNK DEF | n/a: theorem, not data definition. |
| 15 EXISTS LEMMA | n/a: no existential output/witness. |
| 16 SHOW/CHANGE | None. |
| 17 PUSH_NEG | None. |
| 18 GENERALISE | Both effective binders assessed by compiled probes below; no inherited σ/τ instances effective. Ordered-field candidate assessed; retain real domain for the source-specific API. |
| 19 INEQUALITY | Hypothesis and conclusion both use ≤; per-occurrence table below. |
| 20 NORMAL FORM | Natural floor and range(n+1) are the canonical nonnegative integer indexing used by the local caller. No equivalence wrapper needed. |
| 21 SYNTAX GENERALITY | Implicit a inferred from ha; caller applies theorem directly. No easier-to-apply restatement warranted. |
| 22 IMPORT FANOUT | No new import. |
| 23 CASTS | Remove explicit type-ascribed h2 and n/hn casts; retain `Nat.cast (R := ℝ)` as load-bearing map target. Signature coercions remain cross-type ℕ→ℝ. |
| 24 INSTANCE NAME | n/a: theorem declares no instance. |

## Signature packing and inequality artifacts

All widths are Unicode codepoints. `#check @Roth.floor_sq_div_two_le_sum` is captured in the successful independent-original log below with format.width=100.

| Signature line | Width | Next indivisible mathematical signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 284 theorem and both arguments | 54 | Entire conclusion through `:= by`, excluding continuation indentation: 65 | 54+1+65=120 >100 | Keep break at colon |
| 285 complete conclusion | 69 | No next signature line | n/a | Keep |

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | ha | 0 ≤ a | Already oriented | None |
| 2 | conclusion | floor-square/2 ≤ sum | Already oriented | None |
| — | signature scan | Zero ≥ or > | None | No `_ge_`/`_gt_` name |

## Five-method actual mathlib search

Raw native results: `/private/tmp/roth-theta-floor-sum/{finder,loogle,leansearch,local}.json`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | Nonnegative real floor squared/2 bounded by sum(a−n), zero through floor | Returned unrelated floor-power and harmonic bounds, no direct replacement. |
| B Loogle | `Finset.sum, Nat.cast, Finset.range` | Returned binomial/cast identities, no matching floor inequality. |
| C LeanSearch | Sum of natural numbers cast to field equals n(n−1)/2 | Found Finset.sum_range_id and Finset.sum_range_id_mul_two, partial building blocks. |
| D Source rg | `sum_range_cast`, `sum_range.*(id|natCast)`, `sum.*floor.*(sq|sub)`, `floor.*sq.*sum`; full untruncated exact target-name search | Gauss formula in Algebra/BigOperators/Intervals.lean; no exact target-name match. No claim that this proves absence. |
| E Native name pattern | `sum_range`, limit40 | Returned Gauss formula and unrelated sum bounds; result explicitly index=unavailable, therefore no indexed absence claim. Source and compilation verify used names. |

Auxiliary variants inspected: sum_range_id, sum_range_id_mul_two, sum_range_reflect, sum_range_tsub, sum_range_by_parts; no real-valued direct replacement established. Common-equivalents table does not match this arithmetic inequality. Anonymous exact? failed; apply? produced only partial reductions with unresolved goals. Searches run in an exact prefix ending BEFORE the target: no imported current target and no named failed matching theorem. The known stalled native multi_attempt route was deliberately not repeated; native run_code was used once, then ordinary isolated compiler batches. Search-only absence is not asserted.

## Generalisation and literature

Actual effective telescope must be read from the compiled constant, not guessed from section text. Expected two binders are a and ha; final successful metaprogram output below confirms it. Compiled generic candidate plus negative drops in dedicated scratch files assess both.

| Binder | Class/use | Drop/weakening probe | Decision |
|---|---|---|---|
| `{a : ℝ}` | Structure value in floor, sum, bound | Removing a with autoImplicit=false is ill-scoped (expected-failure probe). Generic K with Field, LinearOrder, IsStrictOrderedRing, FloorRing tested with same six-line proof. | Mathematical generalisation supported; retain real public API to avoid domain churn for this paper-specific supporting result. No conclusion weakened. |
| `(ha : 0 ≤ a)` | Proposition supplies floor_le bound | Proof deletion probe fails at unknown ha. Separate certified counterexample a=−1 gives false inequality 0≤−1 without ha. | Essential; retained. Strict→weak already at weak form; no point/global or bundled components apply. |

No effective σ/τ/Fintype/DecidableEq binders expected; verify actual telescope below. No global/function hypothesis to localise. No universe binder exists in real-only type.

Public literature search actually run: “Roth 1955 rational approximations algebraic numbers lemma 6 alpha sum alpha nu floor” and “sum arithmetic progression floor nonnegative real triangular numbers formula”. Opened Roth's primary paper PDF ([Cambridge, DOI 10.1112/S0025579300000644](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/div-class-title-rational-approximations-to-algebraic-numbers-div.pdf)); source §5 identifies this as the first elementary fact in Lemma6's proof. Search also surfaced arithmetic progression/Faulhaber descriptions, but they are not used as technical evidence. One subsequent PDF positioned-open returned an HTTP error; no stronger claim is drawn from that failure. No ChatGPT math MCP available in callable metadata. The elementary argument itself compiles for an ordered floor field, so no completeness/analytic property of ℝ is needed. No public abstract-field change recommended: this would add class surface without helping the existing real caller.

Mandatory inversion check: floor appears in Gauss range and floor_le; after setting n the remaining algebra depends only on n≥0 and n≤a. Thus an abstract natural-cutoff inequality is mathematically valid, as is the compiled ordered-field candidate. Extracting a single-use helper would duplicate six simple proof lines and create an additional audit obligation without current reuse; keep the direct proof. This is a substantive inversion assessment, not a skipped check.

## All 42 golfing rules

| Rule | Status and evidence |
|---|---|
| 1.1 by exact wrapper | n/a: no such wrapper. |
| 1.2 by rfl | n/a: none. |
| 1.3 rw+exact→rwa | n/a: rw followed by arithmetic normalization, not exact. |
| 1.4 simp+exact→simpa | Original inner cast handoff eliminated as a whole; final nonterminal simp does not precede exact. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: no conjunction/structure. |
| 1.7 apply+exact | n/a: none. |
| 1.8 by_contra! | n/a: direct inequality proof. |
| 1.9 eta reduction | n/a: no introduced lambda. |
| 1.10 single-use have | Applied: inline hn as nlinarith input; fold natural h1 into congrArg; eliminate h2/inner have. |
| 1.11 refine+fun | n/a: no apply/intro chain. |
| 1.12 redundant show | n/a: none. |
| 1.13 obtain components | n/a: no product hypothesis. |
| 1.14 merge rw | Already one rw list. |
| 1.15 terminal simp unsqueeze | n/a: no terminal simp only. |
| 1.16 nonterminal simp squeeze | Existing explicit Nat.add_sub_cancel retained. |
| 1.17 dot notation | n/a: congrArg and Gauss formula have no clearer receiver here. |
| 1.18 avoid parentheses | Necessary congrArg application grouping retained; no gratuitous by/lambda parentheses. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial existential | n/a: no existential. |
| 2.1 whole grind | Tried bounded grind with floor_le hint; failed, Gauss sum input needed. |
| 2.2 delete pre-grind | n/a: selected proof has no grind; whole-goal attempt covered. |
| 2.3 simpa consolidation | First exact_mod_cast candidate failed (cast sum/natural subtraction mismatch); corrected explicit congrArg/normalization compiled. No final simp+closing-term pair. |
| 2.4 fun_prop | n/a: no analytic-function property goal. |
| 2.5 positivity | Tried whole goal: not a positivity goal. No separate positivity lemma needed. |
| 2.6 gcongr | Tried: no progress without sum identity. |
| 2.7 lia/omega | Both tried: fail on real nonlinear sum inequality. |
| 2.8 aesop | Bounded maxRuleApplications20 tried; exhausted, no proof. |
| 2.9 norm_num/norm_cast | Whole norm_num fails; selected cast bridge push_cast succeeds. Negative counterexample needs floor_of_nonpos before norm_num. |
| 2.10 decide/kernel | n/a: universally quantified real inequality has no finite decidable computation. |
| 2.11 field_simp/ring | n/a: inequality, not denominator identity. Whole ring tried and failed; no isolated algebra equality needs it. |
| 2.12 linear_combination | n/a: no proof ending in ring/ring_nf; inequality needs nonnegative-product reasoning furnished by nlinarith. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 calc term | n/a: no calc chain. |
| 2.15 <;> | n/a: no repeated sibling subgoals. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 legacy analysis tactics | n/a: neither present. |
| 3.3 omega→lia | Both tested at 2.7; neither suitable, no omega in output. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attributes | Ordinary source inequality is not a rewrite normal form and has one caller; no global attribute warranted. |
| 3.6 simp_all | Tried whole goal, fails; no squeezed simp_all in output. |
| 3.7 heartbeat limits | None before or after; no raises. |

Automation log: `/private/tmp/roth-theta-floor-sum/automation.log` (expected exit1); 15 anonymous tactics against pre-target source prefix. Additionally rfl, simp, ring, linarith, nlinarith, exact?, apply? were checked. This failed exploratory file does not certify axioms. Native initial exact_mod_cast candidate emitted sorryAx because of its elaboration error; that failed candidate is discarded. Successful selected proof has separate exit0 standard-axiom log.

## Step back / simplify assessment

Whole-goal automation cannot supply the Gauss identity. Six lines express precisely one cast bridge, one sum expansion, and the inequality. Keeping a local n only adds a naming step; adding an API helper lacks reuse. Direct congrArg is clearer than a typed temporary equality with a nested cast proof. No further simplification recommended. Built-in simplify invocation is unavailable in this host; this explicit holistic review performs its scope without pretending an unavailable command ran. No helper, import, public name, visibility, hypothesis, or caller edit recommended.

## Verification, final profile, and freeze

`/Users/ramin/.elan/bin/lake build Roth.Theta` exited **0**, 2423 jobs; raw `module-build.log` in the scratch directory. This gate was run after the live edit.

`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-theta-floor-sum/independent-original.lean` exited **0** after that module build. It copies the immutable original declaration body into `ImmutableOriginal` and proves it independently; it does not invoke the current theorem. Metaprogram comparison of the independent original type against the ACTUAL built `Roth.floor_sq_div_two_le_sum` type succeeds. Both constants' actual axiom lists are exactly `[propext, Classical.choice, Quot.sound]`. Successful raw output `independent-original.log` also prints the complete effective telescope:

```lean
{a : ℝ} (ha : 0 ≤ a) :
  (⌊a⌋₊ : ℝ) ^ 2 / 2 ≤ ∑ ν ∈ Finset.range (⌊a⌋₊ + 1), (a - ν)
```

Binder metadata: a implicit, ha explicit/default. No universe or typeclass parameter exists; outer section instances do not enter this theorem. Thus every effective original parameter received its actual compiled drop/weakening assessment. `generality.lean` and its corrected log exit0 (27.733s), including generic theorem standard axioms and certified negative-a counterexample; `drop-negative.lean` expected exit1 (24.516s), precisely unknown a/ha at deletion sites. The earlier counterexample attempt failed because norm_num alone did not simplify negative natural floor; corrected successful file explicitly rewrites `Nat.floor_of_nonpos` first. This earlier failure is not counted as certification.

Final native complete **unfiltered** live Theta LSP call, file_path only plus timeout_s120: `final-lsp.json`, success=true, partial=false, timed_out=false, still_elaborating_lines=null, failed_dependencies=[], **0 errors and 17 existing warnings**. No target-range diagnostic; caller and all remaining declarations elaborate. No filtered diagnostic view substitutes for this gate.

Diff verification compared full current source against released snapshot and asserted byte equality before/after the assigned declaration, plus exact signature equality. Only six proof lines replace eleven. No new global identifier is introduced: congrArg, Nat.cast, Finset.sum_range_id_mul_two, Nat.add_sub_cancel, and Nat.floor_le were already in the original proof and compiled successfully. Docstring/comments, imports, caller, and every other source byte preserved. No sorry/native_decide/new axiom/limit raise/profiling scaffold in the changed proof.

Final real profile command `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-floor-sum/final-prefix.lean` exited **0** after every ordinary request drained. Raw UTF8 `final-profile.log`, actual target anchor `Roth.floor_sq_div_two_le_sum`. Exact source prefix (all preceding source/imports/context preserved) only; namespace closings appended. Final outer command60.905ms + associated async proof331.463ms + kernel/addDecl16.613ms + linters5.974ms = **414.955ms**. Nested definition.value327.716ms and nested kernel16.577ms are not added again. Baseline503.277ms versus final414.955ms: 88.322ms lower in these runs. Both below750ms repeat threshold and1000ms budget; no borderline repeat needed. Timing variability applies.

Buzz outcome: **FAST-BOARD**, no target over budget, no deferral. maxHeartbeats raises removed0/added0. No profiler scaffolding in production. The /buzz wrapper is unavailable here; its actual Lean4.34 real profiler workflow was executed directly. Owner full-project build, separate Roth.LeanEval build, and actual whole-module profile sweep remain owner work after this leaf freeze; no claim those final owner gates ran here.

## Leaf gate status and handoff

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | Actual `lake build Roth.Theta`, exit0, module-build.log. |
| definition_protected | PASS | No def/abbrev edits; full snapshot comparison. |
| theorem_statement_protected | PASS | Exact source signature equality and independent original-vs-actual type metaprogram exit0. |
| standard_axioms | PASS | Independent immutable original and actual built current constant each only propext/Classical.choice/Quot.sound. |
| structure | PASS | Six body lines, no branches/conjunction/new helper. |
| naming | PASS | Mathematical snake_case, no prohibited pattern. |
| packing | PASS | Both measured signature rows above. |
| inequality_orientation | PASS | Both occurrences use standard orientation; no reversed code inequality. |
| cumulative_no_unintended_breakage (leaf scope) | PASS | Same-file sole caller unchanged; whole Theta module build and complete live LSP passed. Owner cumulative project gates pending. |
| live diagnostics | PASS | Complete unfiltered final JSON success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors; 17 preexisting warnings. |
| performance | PASS | Real final profile414.955ms <1000ms; prefix-only limitation explicit. |

Overall leaf gates: **PASS**. Full project and separate LeanEval final owner gates: **PENDING OWNER**, not claimed run by this leaf.

Phase3 file-level changes: none (single declaration scope). Phase5a non-rename refactoring: none beyond proof simplification; field generalisation assessed and not recommended for this source-specific API. Phase5b rename pass: no candidate/queued/applied rename, zero caller edits; shared sidecar untouched. Simplify outcome: PASS-THROUGH after explicit holistic review of selected proof; no extra source changes. No decomposition flag or new private helper requiring another dedicated audit.

Result: **11 to 6 body lines, saved5**. Audit issues fixed: redundant local floor name/bound and nested cast-equality handoff. Rules applied primarily1.10 and cast normalization2.9; all42 assessed above. Comments-preserved: original docstring/source quotation intact; no original inline comments present. Renames queued: none. Refactoring needed: none.

11-step phase checklist:
- [x] Step1 references read.
- [x] Step2 full24 audit recorded before edit.
- [x] Step2.5 all five actual mathlib methods and raw results recorded.
- [x] Step2.6 every effective original binder compiled drop/weakening assessment; public literature and inversion check.
- [x] Step2.7 measured full signature packing table.
- [x] Step2.8 inequality occurrence table.
- [x] Step3 all42 golfing rules with statuses and actual applicable tactic experiments.
- [x] Step4 alternative strategy, whole automation, term-mode and simplify review completed.
- [x] Step5a complete unfiltered final live LSP passed.
- [x] Step5b scoped diff, module build, exact original type/proof/axioms and real performance gates passed.
- [x] Step6a no rename required; no shared sidecar write.

Source edits revoked/frozen. Final Theta SHA256: `3522af0920e133d0f34f3da6c162e288d3987a0fb948ded6d3a89ef87ee1d62f`. All requests drained. Raw evidence directory `/private/tmp/roth-theta-floor-sum/`; no Git mutation or shared report/log mutation performed.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (83.621 s),
then separate `lake build Roth.LeanEval` (29.992 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `3522af0920e133d0f34f3da6c162e288d3987a0fb948ded6d3a89ef87ee1d62f`.
Raw logs: `/private/tmp/roth-theta-d24-full.log`, `/private/tmp/roth-theta-d24-leaneval.log`; machine record
`/private/tmp/roth-theta-d24-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 24/35, overall 205/264 original
declarations, 9/14 completed files. No new production helper; the prior helper remains separately audited.
