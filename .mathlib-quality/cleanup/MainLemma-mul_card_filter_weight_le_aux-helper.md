# Fresh Mode B helper11 audit: `mul_card_filter_weight_le_aux`

Result: PASS for this private helper, pending the owner's independent acceptance of the sealed evidence. Original proof12 lines/max branch9; final proof8/max branch5, saved4 proof lines. Signature4→3 lines. Whole file747→742. All local recommendations are implemented. No new helper, API, import, caller change, rename, axiom, limit option or weaker conclusion. Source SHA `00bd95d36dc17efae966a3cc56fb6990cdcf5a6d7433bd0881d2f598629c6574` is distinct from the earlier accepted helper10's742-line source.

The public main proof remains89 lines (headline limit15) and its measured1408.695/1421.639ms remains a valid performance failure. It belongs to the parked original27 lifecycle, which this audit does not complete. Counts remain242/264, MainLemma26/27 and10/14; no243 or helper264 credit. Whole-file review, global profiling/repairs, public original27 completion and publication remain with the owner.

## Scope, first draft and independent understanding

Scope is exactly one ordinary private auxiliary lemma at final L616–626. The entire entry747-line MainLemma source was read, including the public main declaration and its attached doc. The full installed lean4 and mathlib-quality skills and full cleanup.md, cleanup-all.md and buzz.md were read, together with all eleven applicable mathlib-quality references (style, naming, golfing, proof patterns, mathlib search, generalisation, cleanup gates, profiling, review stages, quality principles and PR examples). Source dialect is classic. No optional cache download was needed; pinned Lean4.34/mathlib were already installed.

Entry source SHA `aff73af494d2ad780a88ae0891298f7b0422fc4547c8747ddf0d25402bbc7c5a` and genuine first ungolfed helper SHA `cccd6e219795f5e5634478b295576989b3baaebf5e3d4b3134a610d46b8bbc45` are immutable in the scratch root `/private/tmp/roth-mainlemma-helper11-fresh1`. The first proof is12 lines, not a reconstructed already-golfed proof. The original author's parked partial lifecycle, and its direct-source validation, were readiness evidence only; this auditor separately rebuilt and validated the helper.

The theorem bounds a real scale times the number of low-weight points in a finite coordinate box by half the box cardinality. The scale `a` is an arbitrary real number, including zero and negatives. For positive `a`, apply the existing lattice estimate at deviation `4*a*sqrt(m)`, multiply by nonnegative `a` and cancel the positive denominator. For nonpositive `a`, the LHS is nonpositive and the RHS is nonnegative. There is no delta, polynomial-degree, nonzero-scale or positive-scale caller assumption.

The paper reference was checked against actual clean.tex L1483–1486 (saved `reference-main-count-v1.txt`): its weighted-cardinality cancellation is exactly the domain step isolated here. Existing public docs, reference quotes and all nine literal proof comment lines remain byte-exact. No copyright, year, author or license metadata was invented; the inherited header warning remains explicit.

## Full24 audit, final dispositions

| Item | Finding and disposition |
|---|---|
|1 LINT|No target warning. Complete final native diagnostics have inherited counts1/4/0 in MainLemma/Main/LeanEval, no errors or new warnings.|
|2 HAVE|Removed all three original local facts hcard/ht/hs by inlining their single-use application/proofs; final eight-line candidate was freshly guarded after hs inlining. No have-by wrapper remains.|
|3 SET_OPTION|No target or production limit/debug option. Scratch profiling toggles tracing only and guards defaults on entry/exit.|
|4 SIMP SQUEEZE|No original or selected simp. push_cast and field_simp serve distinct cast/algebra steps; no bare nonterminal simp to squeeze.|
|5 NAMING|Descriptive mul/card/filter/weight/le, private `_aux`; no numeric name or forbidden abbreviation. No rename needed or queued.|
|6 PACKING|Measured every final signature line: widths100/99/44. Final width100 #check compiled; complete-next-chunk arithmetic108/101 rules out underpacking. Initial failed arithmetic is retained and corrected.|
|7 BY|At the end of final signature line618.|
|8 FORMAT|Two-space tactic blocks, one tactic per line, correct bullets/continuations/blank separator. No accidental scratch whitespace remains.|
|9 COMMENTS|No helper comment to move; all nine existing proof comments/paper quotations and public main doc preserved by exact inverse. No content removed.|
|10 DOCSTRING|Private helper needs none; all existing public docs protected.|
|11 VISIBILITY|Private auxiliary with one same-file main consumer, no public API expansion.|
|12 STRUCTURE|Proof12→8, maximum branch9→5, below ordinary30/10 limits. No conjunction, duplicated proof skeleton or meaningful extraction recommended.|
|13 MATHLIB|Five fresh actual searches plus exact?/apply? probes; existing project lattice estimate is the substantive dependency. No equivalent identified. Actual API definitions and compiled applications verified.|
|14 JUNK DEF|Not applicable: proposition lemma, no data definition. All retained generated/DATA declarations nevertheless inventoried and VALUE-checked.|
|15 EXISTS|Not applicable: inequality conclusion.|
|16 SHOW|No show wrapper or conversion scaffolding.|
|17 PUSH_NEG|No push_neg; sign split by_cases is direct.|
|18 GENERALISE|Every outer/inner binder, universe/typeclass possibility and hypothesis weakening assessed below. Arbitrary real a retained; positive dimension and coordinate bounds certified necessary.|
|19 INEQUALITY|All four signature comparisons use `<` or `≤`; zero `>`/`≥` occurrences, no `_gt_`/`_ge_` rename. Per-occurrence table below.|
|20 NORMAL FORM|Multiplied cardinality bound avoids division by possibly nonpositive a; natural box/product/cardinalities cast to reals at genuine bridges. Domain normal form retained.|
|21 SYNTAX GENERALITY|Main supplies `(1+3δ)*n` directly, without a sign proof; no optional equivalent wrapper or abstract API recommended.|
|22 IMPORT FANOUT|No new import or fanout.|
|23 CASTS|Actual omission probes compiled, but m/card/product annotations mark real Nat→Real crossings; retain original bridges rather than add or obscure coercions.|
|24 INSTANCE NAME|No instance declaration.|

Phase2 A.1–A.7, B and C: inherited unknown header metadata retained; module doc/import grouping/section organization protected;742 lines below1000; no production limits, dollar/lambda/push_neg migration needed; no target lint, visibility/doc/name/structure issue remains. Phase3 requires no file-wide changes in this lease. Phase5a has no new declaration, duplicate convenience API, junk-data/existential or extraction queue. Phase5b target rename queue is empty; unrelated project-END renames and central files were not touched.

## Five fresh search methods and actual APIs

| Method | Saved actual attempt and result |
|---|---|
|LeanFinder|`search-finder-v1.json`: semantic weighted finite-box/cardinality query, returned unrelated Behrend results; no equivalent.|
|Loogle|`search-loogle-v1.json`: Finset.card/Real.sqrt/inequality pattern, empty result for that query.|
|LeanSearch|`search-leansearch-v1.json`: semantic lattice-count query, unrelated results.|
|Local declaration index|`search-local-v1.json`: card_filter_weight names returned the project estimate. Index was WARMING; positive hits usable, no absence claim inferred from missing hits.|
|Repository/source search|`search-source-v1.log/.json`: complete actual generic Mathlib and Roth source searches, including alternate count/card/filter/weight/sqrt forms; no matching convenience lemma found. Full generic8542-file source universe is separately included in closure, not only hits.|

`api-source-definitions-v1.log/.json` binds the actual Mathlib definitions of Real.sqrt_pos, mul_le_mul_of_nonneg_left, mul_nonpos_of_nonpos_of_nonneg and Nat.cast_nonneg; Roth/Lattice.lean196–214 supplies card_filter_weight_le. Existing same-file trans_eq uses were checked. The final proof actually compiles these exact APIs. No unverified recalled lemma or imported renamed alias is used. Optional ask_chatgpt is skipped; private-declaration literature search is n/a under the scope rule, not falsely reported as performed.

## Generalisation2.6a–e and all bindings

The outer audit considered all18 dimensions plus universes: unnecessary assumptions; drop/weak/strict/equivalent hypotheses; pointwise/localized forms; structural dependencies; concrete-type/typeclass weakening; ordered algebra; finite-index requirements; support restrictions; zero/empty/boundary cases; implicitness; conclusion strength/normal form; caller usefulness; abstractions; alternate equivalent APIs; additional companions; dependency/import cost; visibility/migration; and universe polymorphism. These checks yield no additional recommended API change. The concrete table and actual counterproofs distinguish an ill-formed mechanical deletion from mathematical necessity.

| Binding/conclusion | Drop, weakening, localization, type and boundary decision |
|---|---|
|`m : ℕ`|Dimension occurs in Fin m, threshold and sqrt. Removing it cannot retain statement. Natural dimension is the Fin/box API; no field/general-index abstraction recommended. Actual `clear m` fails because hm depends on m. Includes m=1 and arbitrary positive dimensions.|
|`hm : 0 < m`|Used for positive sqrt and nonzero cancellation. Direct removal/clear and replacing by0≤m fail in actual probes. More decisively m=0,a=1 gives singleton empty-dimensional box and1≤1/2, false. Nonzero natural dimension is equivalent, not a useful new API.|
|`r : Fin m → ℕ`|Occurs in box, weight and RHS product. Actual clear fails because hr depends on r. Coordinate natural caps cannot become arbitrary reals while retaining the finite lattice API. No hidden upper bound or special uniform-r assumption.|
|`hr : ∀ j, 0 < r j`|Used by the domain estimate. Drop and weak0≤ probes fail. Actual m=16,r=0,a=1 counterexample has sqrt16=4 and all weights0, hence singleton counted box and1≤1/2 false. Pointwise positivity is already localized to exactly the same Fin m coordinates; no extra global/support assumption.|
|`a : ℝ`|Arbitrary real, including negative and zero. Occurs in LHS and threshold; actual clear fails. No positive/nonzero restriction added. General ordered-field replacement is incompatible with the existing real sqrt/weight estimate without a new substantive API.|
|Conclusion|Same multiplied weak bound by exactly half the full natural-product cardinality, with no weakening, extra premise or alternate normalization. No claim of optimality. Dividing by a would lose negative/zero-scale coverage.|
|Universes/classes|No ambient universe or typeclass binder; Fin m→ℕ and real sqrt/weight are actual interfaces. No unused instance or unnecessary finite/nonempty class. Universe-polymorphic alternative would restate the substantive domain theorem rather than safely delete a binder.|

Inner binders: hr's j ranges over every Fin m; the filter's d is every member of box r and genuinely occurs in weight r d; the RHS product's j is the same Fin m; no inner variable is accidentally specialized, no hidden coefficient/polynomial/support premise is introduced. All their comparisons are already weak/positive in the needed places. Local ha is a proof case split, not a caller hypothesis.

2.6b actual bounded proof and counterexample validation: all five clear attempts retained in clear-batch-v2 (errors include Lean's `error(…)` form, not just `error:`); weak-hm/weak-hr/drop-hm/drop-hr failures retained. `counterchecks-v5` is terminal exit0 with actual opaque VALUE/TYPE, closed/inferred/std3/default guards for both named counterexamples. Rendering was compact only after checks; no acceptance rests on a printed hash. Full statements are in counterchecks-acceptance-v1.json.

2.6c no large change/optional API is recommended; no user fact or preference is undecidable.2.6d n/a: private auxiliary, literature search not required; actual paper passage checked separately.2.6e no extra hypothesis weakening survives, so the original full contract stays byte/AST protected. All identified small safe proof/packing changes have been applied. No deferred helper recommendation.

## Signature packing and per-occurrence inequalities

Final signature actual codepoint measurements, not byte counts:

| Line | Width | Next complete chunk | Chunk width | current+1+next | Disposition |
|---|---:|---|---:|---:|---|
|616|100|`(a : ℝ)`|7|108|ok|
|617|99|`≤`|1|101|ok|
|618|44|none|—|—|ok, final signature line|

Actual `set_option format.width 100 in #check @mul_card_filter_weight_le_aux` compiled in selected8-final-perdecl-v2. The first arithmetic assertion incorrectly missed that adding hr makes line1 exactly100 and that the whole cardinality expression makes line2 exactly99. That failed assertion and the historical743-line source remain immutable. The corrected packing changes whitespace only; all final gates were rerun on742/00bd, with no old-hash gate credit. `final-packing-inequality-v2.json` and final-source-diff-v2.patch are the exact artifacts.

| Occurrence | Final line/code | Orientation/action |
|---|---|---|
|hm|616 `0 < m`|already `<`, keep|
|hr|616 `0 < r j`|already `<`, keep|
|filter|617 `weight r d ≤ …`|already `≤`, keep|
|conclusion|618 `… ≤ … / 2`|already `≤`, keep|

No reversed signature occurrence remains and the name already uses le. No rename sidecar write.

## Every42 golfing rule

| Rule | Actual finding/action |
|---|---|
|1.1 by-exact|n/a: no wrapper.|
|1.2 by-rfl|n/a: no reflexivity wrapper.|
|1.3 rw/exact|n/a: no adjacent rewrite/exact sequence.|
|1.4 simp/exact|n/a: no simp/exact sequence.|
|1.5 trailing rfl|n/a: no trailing rfl.|
|1.6 constructors|n/a: single inequality, no constructor.|
|1.7 apply/exact|n/a: direct lemma applications already used.|
|1.8 contradiction|n/a: by_cases sign split, no by_contra/push_neg.|
|1.9 eta|n/a: filter's d genuinely occurs, no redundant lambda.|
|1.10 single-use have|Inline hcard and positivity fact; positive-sqrt hs inline probe and final eight-line all65 opaque VALUE/TYPE/std3/default/old-contract checks passed.|
|1.11 apply/intro|n/a: no intro chain.|
|1.12 redundant show|n/a: original helper has none.|
|1.13 have projections|n/a: no tuple projection staging.|
|1.14 consecutive rw|n/a: no consecutive rewrite tactics.|
|1.15 terminal simp-only|n/a: helper has no simp.|
|1.16 nonterminal simp|n/a: helper has no bare simp.|
|1.17 dot notation|Apply trans_eq directly to scaled count bound; negative trans already dot notation.|
|1.18 application grouping|Parentheses identify receiver of trans_eq; removing them changes parsing. No cosmetic wrapper introduced.|
|1.19 push_neg|n/a: absent.|
|1.20 trivial existential|n/a: not an existential lemma.|
|2.1 grind|Whole grind failed; hinted grind with existing domain count/sqrt lemmas also failed in the actual final preselection series.|
|2.2 before-grind tactics|n/a: no selected grind, nothing to delete before it.|
|2.3 simpa consolidation|n/a: no selected simp/exact pair.|
|2.4 fun_prop|n/a: no function-property goal.|
|2.5 positivity|Actual side-condition proofs use positivity; sqrt-positivity alternative compiled but is less direct than existing sqrt_pos API, then the local fact was inlined.|
|2.6 gcongr|Original calc monotonicity replaced by gcongr in actual probe, compiles; keeps named hcard and calc, no shortening. Not selected/accepted as a new proof without its own VALUE guard. Direct one-term monotonicity in trans_eq is shorter.|
|2.7 lia/omega|n/a: target is real cardinality estimate, not a Nat/Int arithmetic goal. Whole linarith/nlinarith probes failed.|
|2.8 aesop|Actual whole proof aesop failed.|
|2.9 norm_num/norm_cast|Cast-omission alternatives compiled; kept genuine Nat→Real bridge annotations. Numerical counterexample certificates use actual norm_num guarded with closed VALUE/std3/default checks.|
|2.10 decide|n/a: arbitrary real scale and symbolic box bounds, no finite executable closed proposition. native_decide prohibited and unused.|
|2.11 field_simp/ring|Actual targeted algebraic proof retained; field_simp without final ring fails with unsolved polynomial equality.|
|2.12 linear_combination|Actual replacement compiles after denominator clearing but uses no hypotheses, is no shorter than targeted ring, not selected.|
|2.13 wlog|n/a: sign cases are not symmetric mathematical reductions.|
|2.14 calc composition|Applied: entire two-step calc becomes scaled-inequality.trans_eq with one remaining algebraic goal.|
|2.15 <;>|n/a: no repeated similar terminal goals.|
|3.1 erw/rw|n/a: no erw.|
|3.2 legacy fun_prop|n/a: no legacy continuity/measurability.|
|3.3 omega/lia|n/a: neither selected; target not Nat/Int arithmetic.|
|3.4 rcases rfl|n/a: no equality destructuring.|
|3.5 attributes|No global simp/grind attribute recommended for this private domain estimate; no canonical rewriting RHS.|
|3.6 simp_all|Actual whole simp_all failed, count estimate cannot emerge from local hypotheses alone.|
|3.7 limits|No raised option present or added; every accepted proof guards defaults200000/20000/512.|

Whole rfl/simp/ring/linarith/nlinarith/exact?/grind/aesop attempts failed. apply? exit0 is expressly rejected because it emitted303 partial-goal suggestions and a sorry warning. No proof acceptance relies on that exit status. Automation/cast/terminal probes that compiled but were not selected are compilation experiments only, not claimed as independently guarded production proofs. Failed files/raw/terminals remain immutable.


## Reflection and final selection

The Claude Code built-in Skill(simplify) is unavailable. `holistic-reflection-final-v3.md` is the actual fresh-auditor whole-helper adaptation, performed by a different agent from the original helper author; no nonexistent tool invocation is claimed. It reviewed reuse, quality and efficiency. The selected proof uses the established lattice estimate directly, composes its scaled inequality by trans_eq and inlines all three single-use local facts. No additional wrapper, helper, class, import, attribute or broader abstraction improves this caller. Targeted field_simp plus ring is the shortest tested clear algebra; deleting ring leaves a real unsolved equality. All reflection findings were fixed before the final timing captures. The parent reviewed the narrow recommendation. Later independent whole-file review is a separate owner obligation.

The final diff changes only the target's signature whitespace and proof. Original declaration L616–631 becomes final L616–626; the following blank separator is original632/final627 and the main doc begins original633/final628. No main call repair was necessary. `final-source-protection-v2.json` verifies the inverse recovers the exact entry SHA, all ten earlier helper blocks and reports, main TYPE/doc/body, all nine comments, Main689 SHA6668ff83…, and original27 report576 SHA335a73b4…. Explicit source declaration inventory38 is context, not38 audited declarations. Audit target count is1.

## Formal proof gates and eleven verification checks

1. Actual full baseline build completed first on entry747/aff73 (36.785s), followed by the separate Roth.LeanEval build (17.975s). The compiled cache before that was helper10 source742/4e837; the explicit baseline-built747-v1 snapshots record the transition before any imported-origin credit.
2. Fresh before inventory enumerated65 actual local declarations, including all retained generated/DATA, and actual allowOpaque=true values. One guard per declaration avoids cumulative200000-budget failure. All65 complete raw TYPE/universes and actual opaque VALUE records were captured only from a terminal exit0 run.
3. Original/candidate/final comparison: final selected8-final-perdecl-v2 is terminal exit0/drained on exact742/00bd. All65 raw TYPE/universes equal the original, all64 non-target raw VALUEs are exact, and the target VALUE alone changes. All are closed (no free/meta/loose-bound/level-meta variables), inferred VALUE type defeq declared TYPE, no sorryAx, only propext/Classical.choice/Quot.sound and actual defaults200000/20000/512. No generated-name normalization was needed for this local comparison.
4. The compiled old-helper/main contract guards recover the original TYPE/universe contract. Final imported contract additionally compares actual imported helper and main against original full TYPEs: only BOTH-generated binder macro scopes may erase for comparison. Written names, BinderInfo, order, constant names and universes remain fixed. No general ASTNameMap/counter/name normalization or broad prettyprinter exception.
5. Independent proof: independent-guard-closure-v2 actually proves the original theorem by a separate sign split and positive-denominator inequality cancellation. Its raw TYPE/universes equal original, actual VALUE differs from both original and selected target, and it passes closed/inferred/std3/default guards. The complete recursively expanded13023-node dependency graph excludes target, every denied scratch alias and sorryAx; every actual dependency edge is accounted for. This is not the selected theorem imported under another name.
6. Fresh final complete imported module inventory after final builds finds461 declarations across13 actual defining modules (Theta71, Box20, GenWronskian28, Main57, Separation36, HasseDeriv36, Wronskian22, MainLemma65, Lattice40, LeanEval5, Taylor29, Index20, CoeffNorm32). It enumerates by actual defining module before testing hasValue, then asserts every declaration has an actual VALUE. It is not a hasValue(false)-filtered theorem subset. Name/origin set exactly matches the fresh baseline inventory. Counts happen to match earlier audits but were independently derived.
7. Five final-imported-retained batches all terminal exit0 before acceptance. Every461 actual TYPE+allowOpaque VALUE, sourceOrigin, closed/inferred/std3/default guard passed. Full raw logs are preserved; acceptance includes exact TYPE/VALUE hashes and inventories. Full raw source/API proof evidence remains available, not only hashes. Serializer typeCode has unsupported-node markers for some generated types, so no claim of recompiling all65/461 typeCode strings is made: raw TYPE/actual VALUE/inference checks are the guards; only supported helper/main expressions were recompiled as old-contract guards.
8. Final FULL project build v2 on742/00bd exit0/drained/immutable33.492823s, raw SHA9cdecee7adca218d688ab73751607690c3eb24ba9acfe3d12348f8f10dd8c607. THEN separate final Eval build v2 exit0/drained/immutable14.240846s, raw SHA598803c6498eb6c6e8fe35433ded5ff597e6835d6bba89edad1359471b97dc0c. Exact order/source checked in final-build-acceptance-v3.json. Historical743 builds are retained, not credited to final source.
9. Actual final file_path-only, unfiltered native diagnostics MainLemma/Main/LeanEval all success=true, partial=false, timed_out=false, failed_dependencies=[], errors0. Inherited warnings1/4/0 are fully saved: header in MainLemma, header plus hδ/hQ/hc in Main, none in Eval. Each has source17 pre→actual request→immediate return timestamp→full raw save→SHA/bytes/save observation→post; all preparation/save/post executions completed exit0 without an outstanding session before the dependent step. Source17 exact across every boundary. Native receipt final-native-contract-acceptance-v2.json.
10. Prospective matched helper+main whole-command profiling, all four captures plus observations/drain, exact payload/root/CLI/default/source/cache/environment gates, passes helper<1000 as detailed below; main valid failures remain. No native_decide, admitted proof, new axiom or raised Lean limit.
11. Source/report/static/protection checks and complete two-stream closure with fresh process drain/seal form the release evidence. No meaningful production subhelper introduced and self-audited. Owner independent third stream/proof/native/profile/report review is required before acceptance. No whole-file/global/publication result inferred.

## Seven diff gates

| Gate | Final result |
|---|---|
|definition_protected|PASS: all retained data and non-target declarations raw values exact; no new/removed definition.|
|theorem_statement_protected|PASS: all65 local raw TYPE/universes exact, original helper/main contract recovered and imported guard compiled.|
|no_sorry/trust/defaults|PASS: accepted actual opaque values closed/inferred/std3, defaults200000/20000/512; no production scaffolding/limit changes.|
|structure_gate|PASS helper8≤30/maxbranch5≤10; main89>15 retained separately, no helper completion credit for it.|
|naming_gate|PASS descriptive private name, no rename or central queue change.|
|line_packing_gate|PASS every signature row measured100/99/44 and compiled width100 check.|
|inequality_orientation_gate|PASS full per-occurrence table and zero reversed comparisons.|

## Matched profiling, raw framing and immutable inputs

Owner explicit profiling HOLD ACK is saved before captures. Owner and parent had no competing compiler/native/profile/raw parsing/heavy review/admin mutation through the entire four-capture series, preparation and postfreeze/drain. All four captures and pre/post observers completed exit0, then all12 actual capture/printenv groups were absent and a completion receipt was saved. Only then was the owner notified of completion/HOLD release and raw parsing begun. No partially observed row, early parse or contaminated pair is credited.

Each exact full helper and direct-consumer main command (including main attached doc) is scoped from the genuine entry747 source and final742 source. The rest of each full source is preserved; only trace toggles and entry/exit guards are added. Exact source reconstruction and canonical payload matching allow whitespace and standalone comments only. The CLI is identical: lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE. Threshold is Nat milliseconds. External420-second kill bound does not alter Lean's budgets.

| Sample | Helper ms | Main89 ms | Helper+main sum ms |
|---|---:|---:|---:|
|before A|144.765|1438.524|1583.289|
|after A|121.957|1421.639|1543.596|
|before B|139.652|1415.875|1555.527|
|after B|119.199|1408.695|1527.894|

All samples retained. Both selected helper samples are<750 and<1000; no third sample is needed or used. The main consumer fails1000 in both before and after measurements and fails headline15; these are real original27 obligations, not discounted as noise or excused by prefix profiling. The smaller helper samples do not establish a causal runtime improvement; no unrelated historical scope/CLI/runtime numeric comparison is made.

Strict parser sums only column0 DISJOINT Elab.command, async proof, kernel addDeclCore, compiler and linter roots for the exact full command; nested and Meta/trailing-end rows are excluded without subtraction from another scope. Actual helper kernel name is `_private._stdin.0.Roth.mul_card_filter_weight_le_aux`; main family is actual main plus its proof_1_1/proof_1_2 generated declarations. Families were freshly derived from65 actual metadata records; no generalized generated-name map. Complete actual printed command payloads and raw root-line bindings are saved. All four wall traces passed full framing/default/CLI/source/raw-byte validation.

Actual pre/each-prelaunch/post source17, cache104, root8, setup14/importArts12202, package12202/core12592 availability, four proxy/pinned binaries and resolved paths, frozen parent environment and actual Lake environment bytes are equal. Parent env SHA c7f894578d6d472468835adbcd4f44f81d88b4f13cca332bf87397efdc321103; actual Lake stdout SHA ba6f8374c1117c9eba9f850399884d211c13be0f886aa24d130e0029cba1064f, stderr empty. Private environment values stay out of the report. Existing immutable compiled blobs are reused only after complete actual byte/hash equality, avoiding duplicated gigabytes.

Optional count_heartbeats is skipped: installed macro disables budgets with maxHeartbeats0. No such macro was invoked and no heartbeat counter is treated as milliseconds or a wall gate. Source/cache/setup/catalog observations establish availability supersets, not an exact loaded-runtime closure. `profile-four-acceptance-v1.json` holds all four strict acceptance results.

## Failed experiments, harness repairs and qualifications

All failed sources, raw logs, terminals and corrections remain immutable; no failed run receives proof or final-source gate credit.

- Initial recovery included a read-only Git status before the full no-Git rail was ingested. Parent was informed. No Git mutation occurred, and no later Git calls were made; git-read-deviation-v1.json records it.
- First runner invocation put label before options, so argparse consumed the frozen-env arguments and asserted before starting a compiler. Corrected option order produced baseline-full-build-v2.
- An interim parent message misstated the apply? partial-goal count as355. Actual saved count is303, immediately corrected to parent in progress-count-correction-v1.json. The exit0 probe is rejected for its explicit sorry/partial-goal output; no accepted proof depends on it.
- First formal bundle used invalid pp.width; actual pinned core option format.width was source-verified and the narrow harness repaired. Failed bundle-v2 remains; bundle-v3 and final per-declaration v2 guards actually pass.
- Counterchecks-v2 had unsolved goals. Counterchecks-v4 exited137 while emitting a giant proof value, timed_out=false; cause is UNKNOWN, not asserted to be memory exhaustion. Partial output is not accepted. V5 uses smaller independently checked counterproofs, obtains actual c.value! true and validates it before compact rendering; it passes wholly.
- Initial signature packing assertion failed on100/99 codepoint arithmetic. Historical743 artifacts remain. Final whitespace-only correction is742/00bd and all final TYPE/VALUE/full-build/Eval/import/native/profile gates bind that exact source.
- Whole automation rfl/simp/ring/linarith/nlinarith/exact?/grind/aesop/simp_all and hinted grind fail. gcongr/linear_combination/cast-omission alternatives compile but were not selected; they are experiments, not separately accepted replacement proofs without actual VALUE guards. The nine-line accepted candidate and final eight-line candidates each have actual fresh local guards.
- During report preparation two guessed predecessor report filenames did not exist (card_pencil_eq_aux and prod_bound_aux); those read-only lookup failures are retained in auxiliary-read-failures-v1.json. No missing report was reconstructed and neither lookup supplies evidence; actual reports were inventoried by rg.

## Current available closure and release

The immutable dispatch, P5 partial seal/current available closure, Q10/Q9/P4 accepted history and archive are provenance, never substituted for this fresh lifecycle. The exact historical lost771-byte administrative row and unknown timestamp remain explicit; no reconstruction or complete old P8/R3 manifest rehash claim. Current available rows are re-streamed, changed historical live tuples represented by actual saved old-stage aliases. Missing pre-reboot unselected runtime data remains unavailable.

Final evidence root is `/private/tmp/roth-mainlemma-helper11-fresh1`. Administrative closure snapshots only small relevant owner evidence into immutable local files plus map; mutable live owner paths are excluded. Closure includes every actual own artifact/failure, report, source17, instructions/references, actual generic8542 Mathlib source universe, cache104/root8/setup14/package12202/core12592/four-binary availability catalogs and exact observed binary provenance. All692 archive logical records and645 stored blobs are streamed and decoded/checked. Existing saved binaries are reused only under actual hash/byte equality. This is an actual available-input closure, not an invented exact loaded-runtime closure.

The exact four self-reference exclusions are manifest.json, second-rehash.json, final-drain.json and final-seal.json. All other own artifacts are included. Two genuinely fresh complete streams precede a fresh full-process observation and actual manifest-bound current launch-group absence checks (including all parked198 predecessor groups and own launches). Historical numeric PIDs are not identities. Source17/report hashes and second→PS→seal chronology are checked. Only after these complete may the ALL7END seal release source/caller/report/artifacts/compiler/build/native/profile; no active calls or children. Final source/evidence then remain immutable until owner explicitly resumes. Owner performs independent THIRD/proof/native/profile/report review before acceptance.

## Result and all11 phase checks

Audit findings resolved: three single-use facts, duplicated calc composition and all-line signature packing; all implemented. Rules applied1.10/1.17/2.14, existing2.5/2.11 retained. Gates PASS for helper. Renames queued: none. Comments preserved:9 of9 existing proof lines plus public docs, none moved/removed. Refactoring needed: none in helper scope. No local follow-up recommendation is deferred.

- [x] Step1 reference documents fully read.
- [x] Step2 complete24-item audit.
- [x] Step2.5 five actual saved search methods and API validation.
- [x] Step2.6 a–e every binder/generalisation/countercheck/private-literature status.
- [x] Step2.7 every signature line/codepoint packing table and compiled width100 check.
- [x] Step2.8 every inequality occurrence and post-scan.
- [x] Step3 all42 golfing slots and bounded attempts.
- [x] Step4 fresh whole-helper reflection; all recommendations fixed.
- [x] Step5 formal/independent/full-build/Eval/native/performance/diff gates completed.
- [x] Step6a no target rename; protected central queue untouched.
- [x] Step6b complete report; final current available closure/drain/seal accompanies release, with owner independent acceptance still separate.
