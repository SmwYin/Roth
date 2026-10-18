# Dedicated new-helper audit: `Roth.mul_div_two_le_sum_max_aux`

This leaf audits exactly the new private linear estimate, not an original declaration. Original
count contribution: **0**. The sibling quadratic estimate is assigned to a separate fresh leaf.
Standing authority permits supported recommendations; public domains, names, conclusions and
previous explicit public choices remain protected. Full project build and separate LeanEval are
owner gates, pending after both helper audits.

## Baseline and scope

Release Theta SHA256: `235a2a6a64ae919e1fbb884eb7bc2287d74996e4133bf25180385c37cec262aa`.
The inherited SAME-SOURCE complete baseline native diagnostics are
`/private/tmp/roth-theta-min-sum/optimized-final-lsp.json`: success true, partial false,
timed_out false, failed_dependencies [], zero errors, 17 inherited warnings, none in this helper.
Inherited real exact-prefix profile: `optimized-final-profile.log`, with explicit declaration
anchors and `optimized-profile-status.jsonl`: linear351.522ms, quadratic527.652ms,
publicmin259.890ms. These are inherited measurements, not fresh leaf measurements.
Earlier published full builds are not evidence for this unpublished helper batch.

Scratch and raw logs: `/private/tmp/roth-theta-linear-helper/` throughout this report.
`release.lean` preserves the exact starting source. No Git or shared-log mutation is authorized.
Read: lean4 and mathlib-quality SKILL.md, full cleanup worker workflow, full golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns and cleanup-gates; relevant formatting,
visibility, casts, normal-form, naming and profiling references. Single-declaration mode applies.

Initial independent proof source is the certified `edited-source.lean` under
`/private/tmp/roth-theta-min-sum/`, SHA256
`08e55dec3fe02fe2cf3c9324eca959cf60c81f180bee5af389b9f5aa40ea1248`.
Its helper text agrees with `initial-helpers.lean`, SHA256
`f87ff08d34f1db5705f643ee0fbf779eadacc50064cde54da2457868438bb23b`.
The literal first-introduction full snapshot is not used as successful full-module evidence.
`initial-independent.lean` independently compiles the initial11-line nlinarith proof, exit0,
standard3 axioms; it does not invoke the current helper. See `initial-independent.log` and
`probe-status.jsonl`.

## Full 24-item audit

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | Lint | No baseline warning in target; retain unrelated protected findings. |
| 2 | Have scan | Initial/release `hsum := by` has mathematical proof content; keep. Its inner anonymous congrArg result is transformed by push_cast then consumed, two uses; keep transformation. Final `hr` term used in two denominator side conditions; keep. Final `hsum` term used by push_cast and arithmetic closure; keep. Zero-length split moved outward, eliminating nested identity case split. |
| 3 | Options | No production limit/debug/suppression option. |
| 4 | Simp | Sole production simp closes zero-length branch; terminal and unsqueezed. No nonterminal bare simp. |
| 5 | Naming | snake_case describes lθ/2 versus the positive-part sum; `_aux` is the accepted unnumbered private suffix. No forbidden abbreviation/scheme number or rename. |
| 6 | Packing | Complete measured signature table below. |
| 7 | By placement | End of statement line. |
| 8 | Format | Two-space proof indentation; no empty internal lines, semicolon, haveI/letI or consecutive rw calls. |
| 9 | Comments | No initial helper body comment; all surrounding original narrative preserved. |
| 10 | Docstring | Private helper correctly has none. |
| 11 | Visibility | Private; sole production user is public min estimate in the same file. |
| 12 | Structure | Initial11, release12, selected15 body lines; independent triangular identity and positivity stages, no conjunction. Explicit terminating branches1/3 lines; final arithmetic continuation9 lines. No new helper. |
| 13 | Mathlib | All five actual methods and corrected anonymous automation probes below; triangular identity reused directly, no whole-result match found. |
| 14 | Junk def | n/a: theorem, not data definition. |
| 15 | Exists | n/a: no existential conclusion or witness wrapper. |
| 16 | Show/change | n/a: neither occurs. |
| 17 | Push_neg | n/a: none occurs. |
| 18 | Generality | Compile-supported removal of private hr; every effective binder examined below. |
| 19 | Inequality | Zero reversed code inequalities; occurrence table below. |
| 20 | Normal form | Finite range, ordinary real division and `max 0` already match parent consumer; positive-part notation adds conversion without a consumer advantage. |
| 21 | Syntactic generality | Dropping hr lets callers provide only the actual length bound; zero/negative denominators supported. No argument reorder or public change. |
| 22 | Import fanout | n/a: no new imports. |
| 23 | Casts | 0 dropped. Signature `(l : ℝ)` is the genuine cross-type cast. `Nat.cast (R := ℝ)` and the explicit real nonnegativity proposition fix otherwise-polymorphic arithmetic codomains; keep these 2 load-bearing annotations. |
| 24 | Instance names | n/a: no instance declaration or effective section instance. |

## Five actual mathlib-search methods

| Method | Actual query/evidence | Result |
|---|---|---|
| A Lean-Finder | Lower bound sum max zero theta minus natural index divided by r over range l by l theta/2 when l≤theta*r; `search-finder.json` | Returned floor-power/AkraBazzi bounds; no matching estimate. |
| B Loogle | `Finset.sum, Max.max, (_ / 2 ≤ _)`; `search-loogle-corrected.json` | Empty items. Initial `max` identifier rejected; corrected rerun is the usable result. |
| C LeanSearch | Sum of positive parts of an arithmetic progression lower bound half length times initial term; `search-search.json` | Positive-part definitions/normal forms, not the sum bound. |
| D Source rg | Complete full-name search `mul_div_two_le_sum_max_aux`; sum/max/range/sub variants in Algebra/BigOperators, Algebra/Order/BigOperators and Data/Nat | No full-name hit; useful `Finset.sum_range_id_mul_two`, `sum_range_reflect`, `sum_range_id`, `sum_range_tsub`. Actual source inspected, especially Intervals.lean:171. |
| E Native local name | `sum_range_id`; `search-local.json` | Positive hits for triangular identity and divided form. Index unavailable, so absence is not inferred from the name index. |

Auxiliary variants: sum_range_id, sum_range_reflect, sum_range_tsub, sum_le_sum, le_max_right,
positive-part def/of_nonneg, numerator-cleared arithmetic sum. Common-equivalents table has no
applicable bucket. Full-name source absence alone is not an absence proof.

Clean anonymous `example`s in `automation.lean` import only preceding imports/context, never the
audited helper, and try grind/simp/aesop/exact?/apply?. They are isolated from the named negative
trials; no audited or failed named theorem can be suggested. `automation.log` exit1 honestly
records failures/partial proof suggestions and a conservative10000-heartbeat timeout. These are
bounded failures, not an exhaustive theorem-absence certification. Known stalled native
multi_attempt is not repeated. Exact/apply search found no closing replacement. The helper has
substantive sign, Gauss-sum, division-clearing and polynomial-certificate work, rather than a thin
1–3-call wrapper. Keep the private helper, building on mathlib's triangular identity.

## Generalisation, inversion and initial-contract recovery

| Effective binder | Class/use | Compiled mechanical probe | Decision |
|---|---|---|---|
| θ : ℝ implicit | Value; conclusion, hl, summands | `clear θ` fails dependency check in negative-binders; generic ordered-field candidate additionally tested | Retain real domain; no generic consumer justifies extra field API in this private decomposition. |
| r : ℝ implicit | Value; hl and quotient | `clear r` fails dependency check; generic candidate tested | Retain domain and binder. |
| hr : 0<r explicit | Proposition; denominator clearing in release | Original proof after clear hr fails; independently reorganized candidate with hr entirely absent succeeds, so weak0≤r is subsumed | Drop hr entirely. In positive-length/positive-θ case recover hr from hl by ordered-product positivity. |
| l : ℕ implicit | Value; range, casts and bound | `clear l` fails dependency check | Retain natural index domain; arbitrary indices would restate the actual arithmetic progression. |
| hl : (l:ℝ)≤θ*r explicit | Proposition; product certificate | `clear hl` fails; separate compiled counterexample θ=r=1,l=3 refutes removing it, and also the proposed loose hl+3 weakening | Retain hl. It is already weak≤, not strict; no global/pointwise or bundled-predicate weakening applies. |

All expected-failure binder probes are in a separate named file with autoImplicit false.
Expected-failure exit1 never certifies axioms. Positive/counterexample probes are separate exit0
evidence. Real-to-ordered-field experiment is an assessed optional API expansion, not a recommended
production change: current private use is uniformly real, with no extra typeclass consumer.

Literature status: n/a, private declaration; private scope exemption applies. Inversion check:
there is no concrete named Roth object to unfold. The genuinely used concrete range is consumed by
Gauss' summation formula; replacing it by an arbitrary finite set requires a new first-moment
hypothesis and does not reveal an obscured concrete-object theorem. No abstraction/helper added.

The selected proof treats l=0 and θ≤0 directly; otherwise hl gives a positive product θ*r and
therefore r>0. It casts the triangular identity once, compares summands with their maxima, clears
positive denominators and feeds `l*(θ*r-l)≥0` explicitly to `linarith only`.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no wrapper. |
| 1.2 by rfl | n/a: no reflexivity body. |
| 1.3 rw/exact→rwa | n/a: intervening cast normalization is necessary; final rw followed by arithmetic. |
| 1.4 simp/exact→simpa | n/a: only simp closes its branch. |
| 1.5 trailing rfl | n/a: absent. |
| 1.6 constructors | n/a: no product/structure construction. |
| 1.7 apply/exact | Direct `.trans` and comparison terms already used. |
| 1.8 by_contra! | n/a: no contradiction chain. |
| 1.9 eta | Callback uses ν inside expression; not eta-only. |
| 1.10 have inlining | Final hr and hsum each have two uses; nested initial identity proof eliminated by outer zero split. |
| 1.11 apply/intro | Direct sum callback already used. |
| 1.12 redundant show | n/a: absent. |
| 1.13 have projections | n/a: absent. |
| 1.14 merge rw | One merged rewrite chain. |
| 1.15 terminal simp | Unsqueezed zero branch retained. |
| 1.16 nonterminal simp | n/a: none. |
| 1.17 dot notation | `.trans`, `.trans_le`, `.mpr`, `.ne'` used. |
| 1.18 parentheses | Direct lambda; parentheses retained for grouped inequalities/certificates. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 exists | n/a: no existential wrapper. |
| 2.1 grind | Actual clean whole-goal trial fails under bounded budget. |
| 2.2 pre-grind deletion | n/a: no selected grind. |
| 2.3 simpa | n/a: no simplification-plus-close sequence. |
| 2.4 fun_prop | n/a: no function regularity. |
| 2.5 positivity | Used for positive denominator after rewriting; selected sign branches use direct order lemmas. |
| 2.6 gcongr | Sum monotonicity is already one explicit term; no multistep monotonicity calc to replace. |
| 2.7 lia | n/a: no unresolved Nat/Int arithmetic goal; Gauss identity used directly. |
| 2.8 aesop | Actual clean whole-goal trial fails. |
| 2.9 norm_num/cast | norm_num proves numeric positivity; push_cast performs single codomain crossing. |
| 2.10 decide | n/a: open real variables, not closed finite computation. |
| 2.11 field_simp/ring | n/a: inequality rather than rational identity; rw clears the positive denominator directly. |
| 2.12 linear_combination | n/a trigger: no ring/ring_nf endpoint; actual inequality certificate via linarith only. |
| 2.13 wlog | n/a: zero/sign cases have different conclusions, not symmetric duplicated arguments. |
| 2.14 calc | Term-mode `.trans` already used; no calc remains. |
| 2.15 <;> | n/a: no homogeneous multi-goal branch. |
| 3.1 erw | n/a: absent. |
| 3.2 analysis tactics | n/a: absent. |
| 3.3 omega→lia | n/a: no omega. |
| 3.4 rcases rfl | l=0 substituted immediately, no redundant cleanup. |
| 3.5 automation attr | Specialized private lower bound is not a canonical rewrite; no global attribute warranted. |
| 3.6 simp_all | n/a: no simp_all block. |
| 3.7 limit removal | No production option present or introduced. |

Step-back/simplify reflection: whole-goal automation and library replacement were actually tried.
The useful change is a stronger private contract with simpler Gauss-sum handling. A generic
finite-set stage or another one-use helper would add API without serving the current consumer.
Manual holistic simplify pass: ISSUES-FOUND-AND-FIXED, hr removed and identity zero branch shared.
No separate built-in simplify tool is exposed, and no such invocation is claimed.

## Signature packing and inequality scan

Compiled actual-type pretty-printing uses `format.width 100`. Measurements are Unicode codepoints.

| Signature line | Chars | Next complete conclusion token width | Arithmetic | Action |
|---|---:|---:|---|---|
| First, private lemma + all binders | 83 | 57 | 83+1+57=141>100 | ok |
| Conclusion + `:= by` | 61 | — | Final signature line | ok |

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 0 | Entire signature/hypotheses/body | No ≥ or > in code | none | none |

## Final gates, fresh timing and freeze

Private initial-contract verifier: `private-compatibility.lean`,
`private-compatibility-corrected.log`, `compatibility-corrected-status.jsonl`: exit0,39.958s.
It locates the actual built constant by unique environment suffix:
`_private.Roth.Theta.0.Roth.mul_div_two_le_sum_max_aux`.
All retained θ/r/l/hl names, exact dependent types and BinderInfo match; initial/current universe
arity is zero. Exact private drop set is `[hr]`; initial conclusion is definitionally identical.
The full old-telescope adapter is `fun {θ r} hr {l} hl ↦ actual_private_helper hl`.
Independent initial proof, actual built constant, and proof-value recovery each have exactly
`[propext, Classical.choice, Quot.sound]`. The adapter is checked against the complete initial
type, and the equality to the independently recovered original proof is kernel checked.

New identifier verification: `pos_of_mul_pos_right` found in mathlib source and explicitly #checked;
`le_of_not_ge` explicitly #checked. Both also elaborate in successful candidate and module builds.
Existing triangular/sum/division/cast lemmas likewise pass selected-proof and module checks.
Scratch corrections: first candidate needed a real type annotation for the experimental
Nat.cast_pos/nlinarith inference; the selected direct-product route avoids that automation.
First private verifier used reserved identifier `matches`; corrected to `constantsFound`.
Only the corrected exit0 logs certify anything; failed scratch axioms are not accepted evidence.

Final module command: `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit0;
`module-build.log` reports Built Roth.Theta40s and successful2423jobs.
Fresh complete unfiltered native `lean_diagnostic_messages` after source edits:
`final-lsp.json` (also `diagnostic-summary.json`): success=true, partial=false, timed_out=false,
failed_dependencies=[],0errors17warnings. None is in the target range. Complete inherited list:
header L1; earlier retained hr/hB at93,101(two),109,129,252; later sum_max_sub_le_index_det
DecidableEq/hR at370(two),367; later index_det_le DecidableEq/hl'/hδ at409,412,417,405;
protected caller hq/DecidableEq at524,518; Θ_option_le DecidableEq at622. No suppression used.

Public/caller verifier is a byte-identical copy of
`/private/tmp/roth-theta-min-sum/actual-compatibility.lean`, SHA256
`bcb7e0d315c6b7277d83279f0bc147d70ed7e3f608e5e3111deb4ef5f768cafe`.
`actual-compatibility-corrected.log`, `compatibility-corrected-status.jsonl`: exit0,54.621s.
It independently recompiles the immutable original Index+Theta proof namespace, including both
the original min proof and complete original index_le_lem6 proof. Original public drop sets remain
exactly `[hrp,hθ]` for min and `[]` for index_le_lem6. Retained effective names/types/BinderInfo,
universe arity, complete original conclusions and full-old-telescope proof-value equalities pass.
The complete caller still includes hq and its DecidableEq instance. Actual original public
constants, independently recovered originals, recovery equalities and both actual private
helpers use standard3 only. The immutable namespace and permitted-drop sets were not edited.

| Gate | Status | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.Theta`, exit0,40s target; module-build.log. |
| definition_protected | pass | No def/abbrev change in worker.diff. |
| theorem_statement_protected | pass, authorized private strengthening | Exact hr deletion only; full initial-telescope adapter and public/caller recoveries succeed. |
| structure_gate | pass | Helper15 lines, public caller13, explicit terminating branches≤3, final arithmetic continuation9; no new helper or conjunction. |
| naming_gate | pass | Descriptive snake_case, unnumbered `_aux`; no rename. |
| line_packing_gate | pass | Both signature lines measured above. |
| inequality_orientation_gate | pass | Zero reversed code inequalities; table above. |
| complete live LSP | pass | Fresh full unfiltered result,0errors17 inherited warnings, complete/no timeout/no failed dependencies. |
| initial nonself/type/value/binders/axioms | pass | Independent initial11-line proof and unique actual-constant exact adapter, corrected exit0 logs. |
| public and full caller compatibility | pass | Unchanged immutable original verifier rerun after module build, exit0. |
| source hygiene and scope | pass | worker.diff contains target plus one routine call only; no lines>100/trailing whitespace/sorry/native_decide/new axiom/options/TODO/FIXME. |
| full project + separate LeanEval | owner pending | Run sequentially after both helper leaves freeze. |

Comments-preserved: none existed inside the initial helper; all surrounding source narrative
preserved. Renames-queued:none; shared queue untouched. No external call sites exist for this
private helper. No additional private declaration was introduced; no new fresh helper audit owed.
Source delta for this leaf:+3 lines (release body12→15; initial body11→15).

## Buzz: fresh final exact-prefix measurement

**Outcome: FAST-BOARD — every measured declaration below1000ms and750ms.**
All ordinary build/LSP/compiler requests completed before profiling; owner confirmed its compiler
window was clear. Actual command:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-linear-helper/final-prefix.lean
```

`final-prefix.lean` copies the exact live source/imports/context through the end of public
min_le_sum_max, then closes existing section/namespaces. `final-profile.log` is complete raw UTF-8;
compiler exit0,92.401s including all preceding tracing. `profile-status.jsonl` records the exit and
timings, with one `final-profile-<name>-anchor.txt` per declaration.

| Declaration | Inherited identical-release baseline | Fresh selected-source final | Verdict |
|---|---:|---:|---|
| audited linear helper | 351.522ms | 467.473ms | pass |
| unchanged quadratic sibling | 527.652ms | 562.377ms | pass; reusable next-leaf baseline on this exact SHA |
| public min_le_sum_max | 259.890ms | 267.293ms | pass |

The stronger private contract adds sign handling while staying comfortably under budget.
No repeat threshold was reached. Roots for the audited helper are outer command36.274ms,
async proof404.443ms, addDeclCore/kernel/compiler13.903ms and linters12.853ms; sum467.473ms.
Sibling sum includes its seven additional tiny generated addDeclCore roots as well as the main
kernel/compiler root. Public sum includes43.603+211.614+3.822+8.254=267.293ms.
Nested descendants are not double counted. In particular the macro-expanded `private theorem`
command is inside the inclusive later `private lemma` command; the outer lemma command is counted
once, exactly as in the inherited baseline. Raw traces and anchors expose every chosen root.
No production profiling option, heartbeat raise or masking introduced; raises removed0,added0.
Whole-module/caller profiling is not certified by this prefix. The later known index_le_lem6
instrumented heartbeat issue remains reserved for original29 and the owner's final whole-file
sweep. Full project build and separate LeanEval remain owner pending.

## Eleven-step completion checklist and freeze

- [x] Step1: skills, full worker workflow, full required core references and relevant style/naming/profile references read.
- [x] Step2: all24 substantive audit items and every have inventoried.
- [x] Step2.5: all5 actual search methods, variants and clean anonymous bounded compiler routes.
- [x] Step2.6: every effective binder probed, optional domains assessed, private literature exemption and inversion recorded; initial old-telescope recovery compiled.
- [x] Step2.7: measured complete signature packing table and actual built width100 type.
- [x] Step2.8: full inequality scan table.
- [x] Step3: all42 golfing rules assigned concrete status.
- [x] Step4: holistic simplify reflection and alternate strategies reviewed.
- [x] Step5a: fresh COMPLETE unfiltered native final diagnostics.
- [x] Step5b: module build, private/public/caller independent proof/type/value/binders/actual axioms, hygiene and fresh real profile pass.
- [x] Step6a: no rename needed; no shared queue/log mutation.

All requests have drained. Final live Theta and `frozen-source.lean` SHA256:
`ed77a5f89c25d8a54cb4d66a2a3d0ca05478906540635d8aebaef84eb97ee328`.
Only this private helper and its one routine public-min call changed. Real/natural domains, exact
conclusions and all public types are retained relative to release. Sibling source is unchanged.
No unresolved leaf gate or additional helper audit was created. **This leaf's source and report
editing authority is frozen/revoked.** Owner continues with the separate sibling audit, then
frozen sequential full build and separate LeanEval and publication. Original-count contribution0.
