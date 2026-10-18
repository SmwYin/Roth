# Approved revisit original8 — `Roth.indexSet_bddAbove`

Exact decision: [Theta-contract-proposal.md](Theta-contract-proposal.md), selected A.DecidableEq σ and C.hr only. Starting checkpoint `3f577acbfe25a9a11c829f334a0353fbc0432439`; source SHA256 `6163ff1d8e0d00c5f916828e53f4aed5b4fc28a36f35bdcb1f8fab48db973980`. Read-only preparation hold honored until explicit RELEASE. Original counts stay196/264, Theta15/35.

Applied: omit the target's DecidableEq σ section instance, remove `hr : ∀j,0<r j`, add local `classical`, repack its signature, and remove the obsolete helper `hr` argument in exactly index_le_Θ and Θ_mono. Both callers retain their entire original public telescopes, including DecidableEq σ and hr. Fintype σ, B, q and original implicit r remain. No definition/domain/conclusion/name/visibility/docstring/import change, helper, rename, Git mutation or shared sidecar write.

## Preparation and baseline

Read lean4/mathlib-quality skills, full cleanup workflow; full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates and profiling; relevant style/naming sections; prior dedicated original8 report, exact decision, immutable baseline `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`, and surrounding source/literature. Owner preceding full build53.182s THEN separate LeanEval12.704s both exit0, stable start SHA. Same-hash complete `/private/tmp/roth-index-api/final-lsp.json` reused as doctor baseline: success=true, partial=false, timed_out=false, failed_dependencies=[],0errors/27warnings. No duplicate baseline LSP or owner build launched.

All raw artifacts below are under `/private/tmp/roth-bdd-api/` unless otherwise stated.

## Full substantive24audit

|#|Item|Finding/action|
|---|---|---|
|1|LINT|Target's DecEq/hr warnings resolved by exact approved removals. Two callers expose unused-section DecEq and unused hr warnings; all their protected public binders remain. No suppression.|
|2|HAVE SCAN|No have in selected target.|
|3|SET_OPTION|No target/source option; scratch automation budget lowered to2000 only.|
|4|SIMP SQUEEZE|One terminal simpa using hRd, unsqueezed.|
|5|NAMING|Descriptive custom indexSet plus canonical BddAbove predicate; no scheme numbers/forbidden abbreviation.|
|6|LINE PACKING|One91-codepoint signature line, table below.|
|7|BY PLACEMENT|Outer by at end of signature, inner by on argument opener.|
|8|FORMAT|Two-space tactics, no empty body lines; local classical replaces removed public class. No haveI/letI.|
|9|COMMENTS|No proof comments to move/remove; existing docstring retained byte-for-byte.|
|10|DOCSTRING|Protected source-bearing docstring retained, including original positive-weight sufficient condition; theorem now proves the authorized stronger claim.|
|11|VISIBILITY|Public wrapper retained per explicit user preference.|
|12|STRUCTURE|Six body lines including classical; no conclusion conjunction, branch>10 or helper needed.|
|13|MATHLIB|Five actual searches below; generic boundedness partial matches, project index_le_card supplies mathematical bound.|
|14|JUNK DEF|n/a, theorem.|
|15|EXISTS LEMMA|n/a, public reusable boundedness result; no private witness wrapper.|
|16|SHOW/CHANGE|None.|
|17|PUSH_NEG|None.|
|18|GENERALISE|Every effective original binder probed below; apply only approved DecEq/hr removals.|
|19|INEQUALITY|No ≥/> in final target signature; old0<rj removed by approval.|
|20|NORMAL FORM|BddAbove directly serves le_csSup/csSup_le_csSup.|
|21|SYNTAX GENERALITY|Redundant public proof argument removed; q/B explicit and r implicit remain.|
|22|IMPORT FANOUT|n/a, no imports added.|
|23|CASTS|No new coercion/type-ascription; existing Int.castRingHom ℝ codomain load-bearing, cardσ coerces by expected real bound type.|
|24|INSTANCE-NAME|No instance declaration or synthetic-name scaffolding.|

## Packing and inequalities

Width100 compiled `#check @Candidate8.selected` and final public types in final-compat.log.

|Signature line|Codepoints|Next signature token|Arithmetic|Action|
|---|---:|---|---|---|
|81|91|none; proof body follows|n/a, complete signature fits≤100|ok|

|#|Location|Occurrence|Rewrite|Rename|
|---|---|---|---|---|
|1|Final whole target signature|No≥/> relation, nor remaining inequality hypothesis|none|none|
|2|Old hr|0<rj|Approved hypothesis removal|none|

## Five actual searches and clean automation

|Method|Actual query/result|
|---|---|
|A Lean-Finder|“The set of indices of nonzero multivariate polynomials with degree bounded by weights is bounded above by the number of variables”; actual native call timed out. Bounded failure recorded in search-finder.json, not absence evidence.|
|B Loogle|`BddAbove, Set.range`: range_comp_right, range_mono, range_sup variants; generic partial APIs.|
|C LeanSearch|“set bounded above if every element is less than a fixed bound”: BddAbove, bddAbove_def, bddAbove_iff_subset_Iic, bddAbove_iff_exists_ge, csSup_le_iff'.|
|D source rg|Untruncated scoped searches indexSet_bddAbove/bddAbove_def/bddAbove_iff_subset_Iic/degrees_map_of_injective; Bounds/Basic42 and MvPolynomial/Degrees196. No mathlib custom Roth result claimed.|
|E local name|bddAbove_iff limit8: actual boundedness variants plus generic Cardinal/Ordinal hits; index=unavailable, so no index-backed absence claim.|

Auxiliary variants: range_comp_right/range_mono/range_sup, subset_Iic, exists_ge, degreeOf_eq_sup/support_map, degrees_map_of_injective, map_ne_zero_iff/map_injective. Common-equivalents boundedness bucket matches; use generic constructor and existing index_le_card. Keep domain wrapper by established user preference; no new helper/wrapper or unsupported absence claim.

Fresh clean no-Theta-import exact prefix ending BEFORE target; anonymous examples so no audited target or failed named trial can contaminate exact?/apply?. Actual automation.lean expected exit1: grind[indexSet,RSet,index_le_card] fails; aesop makes no progress; exact?/apply? each exhaust conservative2000heartbeats, inconclusive. No repeated known-stalled full-Theta multi_attempt request. No expected-failure result certifies axioms.

## Every original effective binder

|Binder|Drop/weakening probe|Decision|
|---|---|---|
|σ:Type*|autoImplicit=false literal drop fails unknownσ; independent selected proof compiles universe-polymorphically.|Dependent type variable, preserve.|
|Fintypeσ|Literal drop fails synthInstance Fintypeσ; Finiteσ with explicit reconstructed Fintype.ofFinite in conclusion/proof compiles.|Same existing indexSet interface needs Fintype; preserve exact approved scope.|
|DecidableEqσ|Independent selected proof omits it, local classical; standard axioms.|Approved removal applied.|
|B:ℝ|Literal drop fails unknownB; independent proof arbitrary realB without sign assumption.|Dependent bound parameter, preserve.|
|q:σ→ℕ|Literal drop fails unknownq; independent proof arbitrary natural denominators.|Dependent value, preserve.|
|r:σ→ℕ implicit|Literal drop fails unknownr; independent proof arbitrary natural weights including zero.|Preserve value/order/implicitness.|
|hr:∀j,0<rj|Drop compiles; weak form∀j,0≤rj also compiles.|Approved full removal applied.|

positive.lean includes independent selected proof, weak-hr, Finite reconstruction and generic abstract boundedness examples; negative.lean batches literal failures separately. No same-signature field weakening applies: RSet/indexSet fix the integer coefficient/real index interfaces; speculative domain changes are outside approved scope.

Inversion diagnostic: after unpacking indexSet/RSet, B/coefficient bounds/coprimality are unused. Existing Roth.index_le_card IS the abstract nonzero degree-bounded polynomial theorem; generic arbitrary-set boundedness is the BddAbove constructor. No new abstract wrapper justified.

## Public literature

Fresh web queries “Roth theorem polynomial index Taylor degree number variables upper bound generalization” and “Formalizing Roth theorem Takloo Bighash Yin index across sets polynomials”. Primary exposition hits: [Min Ru notes](https://www.math.uh.edu/~minru/fields/roth.pdf), [Roth ICM account](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf), [AMS chapter](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf). These place polynomial indices in the standard Taylor/degree framework; no stronger same-interface claim inferred merely from search hits. Local clean.tex644–670 explicitly gives nonzero Taylor derivative weight≤m, assuming positive weights/denominators in its surrounding setup. Current proof's valid zero-weight extension rests on compiler evidence and unchanged formal conventions. No exposed ChatGPT math MCP capability; recorded unavailable, not silently skipped. Earlier public wrapper/domain preferences and declined caller hr changes remain in force.

## All42golfing rules

|Rule|Concrete status|
|---|---|
|1.1|No by-exact wrapper.|
|1.2|No by-rfl wrapper.|
|1.3|No rw+exact chain.|
|1.4|Existing terminal simpa using hRd retained.|
|1.5|No trailing rfl.|
|1.6|Anonymous bound constructor already used.|
|1.7|Direct index_le_card application retained.|
|1.8|No contradiction proof.|
|1.9|No eta-redex.|
|1.10|No have.|
|1.11|No apply/intro chain.|
|1.12|No show.|
|1.13|Nested shared witness destructured directly.|
|1.14|No rw sequence.|
|1.15|Terminal simpa unsqueezed.|
|1.16|No nonterminal simp.|
|1.17|Existing map_ne_zero_iff .2; direct index_le_card is clear.|
|1.18|Parenthesized proof argument has following point argument, grouping necessary.|
|1.19|No push_neg.|
|1.20|Not a private single-use witness lemma.|
|2.1|Fresh whole-proof grind trial failed.|
|2.2|No retained grind predecessors.|
|2.3|Existing simpa consolidated, no change.|
|2.4|No regularity property.|
|2.5|Boundedness existential needs its explicit witness, no positivity goal.|
|2.6|Exact index_le_card handles inequality, no gcongr subgoal.|
|2.7|No Nat/Int arithmetic subgoal requiring lia/omega.|
|2.8|Fresh aesop trial failed no progress.|
|2.9|No concrete numeric or cast subgoal.|
|2.10|Arbitrary real set boundedness, no finite decidable computation.|
|2.11|No rational identity.|
|2.12|No ring terminator.|
|2.13|No symmetric case branches.|
|2.14|No calc.|
|2.15|Distinct nonzero/degree hypotheses do not share solver.|
|3.1|No erw.|
|3.2|No continuity/measurability.|
|3.3|No omega.|
|3.4|Existing rintro rfl substitution retained.|
|3.5|No new global automation attribute justified.|
|3.6|No simp_all only.|
|3.7|No source limits/options added or present in target.|

Step-back/manual simplify equivalent (no callable built-in simplify tool): PASS-THROUGH beyond authorized API adjustment. Bound constructor plus pointwise index_le_card is the mathematical proof; term-only nesting adds no established clarity/performance value. Fresh automation/search results justify no alternate proof. No redundant have, long branch or new helper. Phases5a/5b no extra refactoring/rename.

## Actual verification and final diagnostic movement

Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exit0,2423jobs; module.log. Fresh COMPLETE unfiltered native lean_diagnostic_messages final-lsp.json: success=true, partial=false, timed_out=false, failed_dependencies=[],0errors/28warnings. Baseline27→final28; lsp-comparison.json compares full severity/category/message multisets without source-line artifacts. Target's unusedSectionVars DecEq and unusedDecidableInType warnings disappear; its hr warning disappears. Each changed caller now exposes unusedSectionVars DecEq and unused hr, producing the expected net+1warning. Their old unusedDecidableInType warnings remain. No warning hidden/suppressed, no claim warning-free file. No target warning remains.

Independent pre-compat.lean exit0 BEFORE production edit: immutable original namespace extracted from baseline2b64544bf9f77a8ff957bf1bcaf693ac72217ff6, including original definitions/map helpers/nonself indexSet_bddAbove and both caller proofs. No current target proves its own original. Full-old telescope adapter to independent selected proof plus exact old caller type comparisons pass. After fresh module build, final-compat.lean exit0 checks those same independent proofs against ACTUAL built production constants. Its full-old lambda is printed explicitly:

```lean
fun {σ} [Fintype σ] [DecidableEq σ] B q {r} hr ↦ Roth.indexSet_bddAbove B q
```

This kernel-equals the independent old target by rfl. Direct getConstInfo.type comparisons align universes, check full types plus telescope length/order/BinderInfo and user binder names; both actual public callers recover their exact old contracts including section instances and explicit hr. No visible-header-only inference. Actual target AST is exactly five binders σ/Fintype/B/q/r with BinderInfo implicit/instImplicit/default/default/implicit, preserved user names, no DecidableEq or hr. The selected candidate/type also kernel-equals actual target. Anonymous instance-generated name is exempt from user-name equality, as instructed.

Actual built target, both actual callers, all three independent original proofs and full-old adapter have exactly propext, Classical.choice, Quot.sound, printed in final-compat.log. No sorry/native_decide/new axiom. First final scratch metadata runs failed on `unless ... then` parsing/containsConst predicate syntax and then logging BinderInfo without ToMessageData; corrected definitive run exit0 is the only accepted actual-verification sample. No source correction was needed. positive.lean exit0 confirms independent selected/nohr/weakhr/Finite reconstruction routes. negative.lean expected exit1 confirms each dependent binder's literal drop failure, separately from successful axiom evidence. All ordinary requests completed before accepted profiling.

Focused before→after diff in focused.diff contains only target omit/hr/classical/packing and the two permitted proof-call argument deletions. Both caller signatures, all definitions, all comments/docstrings and unrelated declarations are unchanged. No new mathematical identifier introduced: omit/classical are Lean syntax; all referenced lemmas were already present and compiled. Repository-wide target caller search finds only the two internal callers; their public APIs are unchanged so no outside caller fix arises. Full project and separate LeanEval are pending owner checkpoints, never claimed by this leaf.

## Buzz — FAST-BOARD, exact prefixes only

One exact-start and one exact-final prefix preserve ALL preceding source/imports/context through Θ_mono and append only end Roth. Prefix-text identity asserted against their respective full source. Both accepted profiles ran sequentially after module/final complete LSP/ordinary checks drained, with no other compiler/LSP/build overlap:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-bdd-api/{before,after}-prefix.lean`

Both exit0;41.417s/40.611s. Raw UTF8 before-profile.log/after-profile.log; profile-summary.json and parse-profile.py record actual command anchors. Tables count the outer command and associated top-level async proof/addDecl kernel/linter; nested tactic/kernel nodes are not double-counted. For scoped omit, the outer wrapper is counted once (max enclosing command), not added to its nested theorem command.

|Declaration|Before outer/proof/kernel/linter ms|Before total|After outer/proof/kernel/linter ms|After total|
|---|---|---:|---|---:|
|indexSet_bddAbove|3.430/149.433/3.190/9.775|165.828|2.712/193.650/3.809/15.233|215.404|
|index_le_Θ|10.048/8.491/2.252/5.683|26.474|10.748/7.993/2.684/11.183|32.608|
|Θ_mono|3.383/12.426/3.682/5.327|24.818|3.596/12.075/2.232/5.891|23.794|

Actual target command anchors: before36924; after37027(inner)/37274(outer omit). Caller anchors before74405/120685, after76996/123295. All aggregates<750ms, budget1000ms; no borderline repeat needed, no speedup claimed. Whole-file profiling is NOT claimed; owner final full-module sweep remains necessary after the known late index_le_lem6 default-heartbeat issue is addressed. Source option/limit raises0, profiling scaffolding0, performance deferral0.

## Eleven leaf gates

|Gate|Evidence/result|
|---|---|
|lake_build_file|PASS actual lake build Roth.Theta exit0,2423jobs,module.log.|
|definition_protected|PASS zero def/abbrev/import/domain/value changes.|
|theorem_statement_protected|PASS exact approved target A.DecEq+C.hr only; original target full-lambda recovery, exact caller effective public types/BinderInfo verified.|
|structure_gate|PASS5→6body lines including scoped classical;≤30, no >10branch or conjunction.|
|naming_gate|PASS descriptive existing name, no forbidden pattern or rename.|
|line_packing_gate|PASS91codepoint one-line final signature and compiled width100 reference.|
|inequality_orientation_gate|PASS zero≥/> in final target signature.|
|cumulative_no_unintended_breakage|PASS both changed caller proofs actual-built/LSP/old-contract checks, no external target caller; owner full/LeanEval pending.|
|independent_original_contract|PASS immutable independent original proof, full oldλ adapter to actual target, both original caller proofs and exact metadata.|
|standard_axioms|PASS actual target/callers/old proofs/adapter exactly standard three.|
|buzz/no_scaffolding|PASS all three profile aggregates<750ms; exact-prefix evidence, all ordinary/profile requests drained.|

Leaf gates pass with expected documented0errors/28warnings. Full project THEN separate LeanEval remain owner gates; no assertion they have run for this source.

## Eleven-step checklist

1. ✓ Required preparation and references, read-only hold and explicit release observed.
2. ✓ Full24audit with concrete findings.
3. ✓ Five actual searches, bounded remote timeout/index limitation documented.
4. ✓ Every effective binder probes, public literature/inversion assessed.
5. ✓ Complete final measured signature packing table.
6. ✓ Per-occurrence inequality table.
7. ✓ All42golf rules with concrete status.
8. ✓ Step-back/manual simplify equivalent; no extra helper/refactoring.
9. ✓ Fresh COMPLETE unfiltered final LSP and full diagnostic comparison.
10. ✓ Eleven leaf gates, real module/original/actual-axiom and target+caller profiles; owner gates pending.
11. ✓ Comments/docstrings preserved, no rename/Git/shared writes, source frozen/revoked and all sessions drained.

Final source SHA256: `71d8a5a8821bfc9c787d0ae6db8b4a086c580370f0ddd13ca10a5353c0f3c460`.
Source edit authority FROZEN and REVOKED. All compiler/LSP/profile sessions completed; no orphan requests. Assigned report is the sole repository sidecar. Counts remain196/264 and Theta15/35.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 80.493 s and 22.939 s.
Theta SHA256 `71d8a5a8821bfc9c787d0ae6db8b4a086c580370f0ddd13ca10a5353c0f3c460` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-r08-full.log` and `/private/tmp/roth-theta-r08-leaneval.log`; machine record
`/private/tmp/roth-theta-r08-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this approved revisit before the next source edit. This revisits original 8; original counts
remain Theta 15/35, overall 196/264, 9/14 files. No new original or helper is counted.
