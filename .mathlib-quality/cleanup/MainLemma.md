# MainLemma cleanup ledger (active)

Baseline HEAD `4d7445c6dd8fe1dd0abfd6edbd5c73f3bc5ccec6`. Entry source708 lines;
original project inventory704 lines,27 original declarations. Prior Theta caller adjustments
are part of this validated baseline. Original project count216/264 at entry.

## Phase0 baseline

- Cache: skipped, already warm and build passes.
- Actual `/Users/ramin/.elan/bin/lake build`:exit0,2465jobs;
  `/private/tmp/roth-mainlemma-owner/baseline-build.log`.
- Full unfiltered native MainLemma diagnostics:success=true,partial=false,timed_out=false,
  failed_dependencies=[],zeroerrors,3warnings; baseline-lsp.json under owner evidence directory.
- Dedicated runLinter executable:n/a; normal build includes Mathlib linters.

## Phase1 preparation

Entire source and cleanup/cleanup-all/buzz workflows read. Classic dialect (no module system).
All27 originals inventoried in source order; source and raw inventory preserved in owner directory.
Main results named by module docs:exists_delta_bound,abs_coeff_modByMonic_le,ncard_boxFamily,
pigeonhole_count,exists_ne_modByMonic_eq,main_lemma; each target≤15 proof lines.
Remaining ordinary bodies target≤30,branches≤10. Correlated existential witnesses stay together.

## Phase2 punch-list (before edits)

A.1 Header metadata absent:preserve unchanged by explicit user choice; do not invent.
A.2 Module doc present with definitions/results/reference.
A.3 Imports:Mathlib/project groups out of order; reorder in Phase3.
A.4 No contentless subsection headers; existing module headings retained.
A.5 708lines<1000; no split indicated at entry.
A.6 No resource/debug options.
A.7 No code lambda-symbol/dollar/push_neg mechanical replacements; ordinary `fun =>` audited perdecl.
B.1 L1 copyright warning:user-preserved.
B.2 L149 log_B₁_gt.hδ0 unused:dedicated drop-test/API/caller audit.
B.3 L149 log_B₁_gt.hr₁ unused:same dedicated audit; no suppression.

C scan perdecl:all public declarations have docstrings. Public definitions name meaningful
paper parameters or boxFamily with repeated API use; private boxPoly has coefficient/injectivity/range
API and an unwanted docstring to strip during its own audit. All theorem names have mathematical
content except log_B₁_gt inequality orientation, which must queue a rename. No private trivial
existential wrapper. Every decl receives full effective-binder,visibility,search,packing,length audit.
No visibility changes presumed solely from absent local callers; supported public reusable APIs remain.

|#|Original|Entry lines|Light scan / targeted audit|
|---|---|---|---|
|1|`lam`|48–48|name/docs/visibility/API/packing to deep audit|
|2|`gam`|51–51|name/docs/visibility/API/packing to deep audit|
|3|`eta`|54–54|name/docs/visibility/API/packing to deep audit|
|4|`B₁`|57–57|name/docs/visibility/API/packing to deep audit|
|5|`exists_delta_bound`|65–97|STRUCTURE:extract long proof/branches|
|6|`eta_lt_gam_iff`|102–105|name/docs/visibility/API/packing to deep audit|
|7|`sqrt_lt_floor`|111–117|name/docs/visibility/API/packing to deep audit|
|8|`four_lt_rpow`|122–144|name/docs/visibility/API/packing to deep audit|
|9|`log_B₁_gt`|149–157|unused hδ0/hr₁; queue smaller-left rename|
|10|`three_small_factors`|164–193|name/docs/visibility/API/packing to deep audit|
|11|`abs_coeff_modByMonic_le`|200–261|STRUCTURE:extract long proof/branches|
|12|`boxFamily`|266–267|name/docs/visibility/API/packing to deep audit|
|13|`boxPoly`|270–272|strip private docstring|
|14|`coeff_boxPoly`|274–287|name/docs/visibility/API/packing to deep audit|
|15|`boxPoly_injective`|289–294|name/docs/visibility/API/packing to deep audit|
|16|`range_boxPoly`|296–323|name/docs/visibility/API/packing to deep audit|
|17|`boxFamily_finite`|326–328|name/docs/visibility/API/packing to deep audit|
|18|`ncard_boxFamily`|334–337|name/docs/visibility/API/packing to deep audit|
|19|`pigeonhole_count`|343–382|STRUCTURE:extract long proof/branches|
|20|`exists_ne_modByMonic_eq`|391–430|STRUCTURE:extract long proof/branches|
|21|`sub_mem_RSet`|438–450|name/docs/visibility/API/packing to deep audit|
|22|`eval_hasseDeriv_sub_eq_zero`|457–467|name/docs/visibility/API/packing to deep audit|
|23|`le_index_of_forall_eval_eq_zero`|474–485|name/docs/visibility/API/packing to deep audit|
|24|`lem7_hyp_of_h32`|491–511|name/docs/visibility/API/packing to deep audit|
|25|`exists_hasseDeriv_eval_ne_zero`|519–523|name/docs/visibility/API/packing to deep audit|
|26|`degreeOf_map_intCast_real`|525–527|name/docs/visibility/API/packing to deep audit|
|27|`main_lemma`|535–706|STRUCTURE:extract long proof/branches|

## Phase3 file-level fixes

Grouped alphabetical Mathlib imports,blank line,alphabetical Roth imports; no removal or new import.
Complete unfiltered post-import native diagnostics pass:zeroerrors,same3warnings.
No metadata invention,contentless header,limit option or mechanical deprecated code found.

## Phase4 sequential checkpoints

Original1 `lam`:fresh dedicated full audit completed; definition unchanged,1→1lines.
[Full report](MainLemma-lam.md). All24audit/42golf/5search/11checklist artifacts present.
Actual independent original formula kernel rfl, exact fulltypeAST/universes/effective binder
names/order/BinderInfo/value and standard3axioms pass. Source/documentation remains unchanged
apart from Phase3 import grouping. Fullfile+Main builds and complete unfiltered MainLemma/Main
native diagnostics pass (0errors,3/4preservedwarnings). Actual anchored prefix profile87.948ms;
no repeat required. Owner independently rehashed all leaf evidence,verified exact original
formula/prefix and raw result flags,then ran full `lake build` exit0 in31.136s followed by
separate `lake build Roth.LeanEval` exit0 in31.436s. All17source/configuration pins immutable.
Owner evidence:`/private/tmp/roth-mainlemma-owner/lam-owner-checkpoint.json`.
No active worker,compiler,profile or native call remains. Publication source/audit hash is
recorded in central cleanup-progress history by the metadata child commit.

MainLemma1/27originals completed at publication,overall217/264;10/14fully completedfiles.
Next original:gam. Remaining MainLemma final file phases are pending; no filewide pass claimed.


### Original2: `gam`

[Fresh dedicated full audit](MainLemma-gam.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. The gam formula,public documentation and complete call contract remain unchanged.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile22.088ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild6.346s THEN separateLeanEval3.305s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/gam-owner-full.json` and
`gam-owner-eval.json`. SourceSHA256`0236435831af553f54e04569caadb7b985e0a556dbebf51d454e53abf3ea2abb`;current709lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma2/27 originals,overall218/264,10/14fullycompletedfiles;nexteta.
Filewide final phases remain pending.


### Original3: `eta`

[Fresh dedicated full audit](MainLemma-eta.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. The eta formula,public documentation and complete call contract remain unchanged.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile14.910ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild6.262s THEN separateLeanEval2.937s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/eta-owner-full.json` and
`eta-owner-eval.json`. SourceSHA256`0236435831af553f54e04569caadb7b985e0a556dbebf51d454e53abf3ea2abb`;current709lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma3/27 originals,overall219/264,10/14fullycompletedfiles;nextB₁.
Filewide final phases remain pending.


### Original4: `B₁`

[Fresh dedicated full audit](MainLemma-B₁.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Formula and domains unchanged; queued B₁→mainCoeffBound for the final project-wide rename pass,with the prior Index entry preserved.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile29.417ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild5.439s THEN separateLeanEval5.054s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/B₁-owner-full.json` and
`B₁-owner-eval.json`. SourceSHA256`0236435831af553f54e04569caadb7b985e0a556dbebf51d454e53abf3ea2abb`;current709lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma4/27 originals,overall220/264,10/14fullycompletedfiles;nextexists_delta_bound.
Filewide final phases remain pending.


### Owner correction to original1–4 profile totals

During original5 review, re-auditing immutable target traces found that earlier sums
included unindented internal `Meta.whnf` events. Exact target command/async root totals
are `lam`87.929ms (earlier87.948),`gam`22.074ms (earlier22.088),`eta`14.891ms
(earlier14.910),`B₁`29.399ms (earlier29.417). All remain below1000ms; no budget
conclusion changes. The earlier checkpoint text remains historical evidence; these
corrected totals govern accepted measurements. Dedicated reports carry explicit
addenda. Raw traces remain immutable; owner root re-audit JSON preserves both sums.
Final whole-file profiling and future workers must count only exact anchored target
`Elab.command`/`Elab.async` roots,excluding nested/internal Meta events and following
end commands/lints.


### Original5: `exists_delta_bound`

[Fresh dedicated full audit](MainLemma-exists_delta_bound.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Removed hn and strengthened the uniform interval to 0≤δ≤δ₀; proof30→15lines,0helpers. Necessary Pow.Continuity import; two exact Main calls and approved one-line explicit-premise linarith repair. Final target765.392/739.630ms; Main consumer1430.559/1459.407ms improves on original3926.336/3727.365 but remains in the Main-nextfile performance queue,with no Main audit credit. Fresh owner root/LeanEval native closure is complete,zero messages/errors. Explicit prior-parameter measurement addenda correct root accounting to lam87.929,gam22.074,eta14.891,B₁29.399ms;all raw evidence retained.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile765.392ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild6.304s THEN separateLeanEval3.290s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/exists_delta_bound-owner-full.json` and
`exists_delta_bound-owner-eval.json`. SourceSHA256`37ac02db4702d7c91a21f66ee1f7f22bdf8b6c6c23e3ab740cc7d1a9c679fefc`;current694lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma5/27 originals,overall221/264,10/14fullycompletedfiles;nexteta_lt_gam_iff.
Filewide final phases remain pending.


### Original6: `eta_lt_gam_iff`

[Fresh dedicated full audit](MainLemma-eta_lt_gam_iff.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Packed signature93/29chars and replaced two-line proof with one grind[gam,lam]; added application guidance,preserved source quote. Exact API/three effective binders/imports/callers unchanged;0helpers. Profile281.175→208.229ms;heartbeats1588→1055. Actual rebuilt-module opaque body/full independent original/type AST/universe/binder/standard-axiom gates pass. Owner independently froze/rehashed54UTF8 artifacts and verified exact prefixes/root timings;fresh full root/LeanEval native closure returns zero messages/errors.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile208.229ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild55.789s THEN separateLeanEval43.154s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/eta_lt_gam_iff-owner-full.json` and
`eta_lt_gam_iff-owner-eval.json`. SourceSHA256`770a6ff1cb79679adfd37cdf765f475e33e1300497537ccd2fb3ae1508f6c26d`;current695lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma6/27 originals,overall222/264,10/14fullycompletedfiles;nextsqrt_lt_floor.
Filewide final phases remain pending.


### Original7: `sqrt_lt_floor`

[Fresh dedicated full audit](MainLemma-sqrt_lt_floor.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Sharp2≤X replaces4<X; both conclusions and historical quote retained, exactly four caller repairs. Public body6→1 plus one separately fresh-audited private helper2bodylines (not original-count credit). Matched GLOBAL public+helper127.982/104.364ms versus178.143/178.631ms; own public22.373/16.945ms. All90 ML/Main timing rows complete. Valid foreign FAILs including exists_delta_bound11188.775ms (preexisting full-file controls11594.369/12164.962) and pigeonhole1000.235ms remain mandatory final-file repairs; Main failures stay in its next-file queue, no Main audit credit. Earlier prefix passes do not certify whole-file performance. Owner verified275 frozen UTF8 artifacts, exact old/current proof/contracts and generated-hygiene-only normalization; fresh root/LeanEval native closure complete with zero messages/errors.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile16.945ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild37.145s THEN separateLeanEval37.339s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/sqrt_lt_floor-owner-full.json` and
`sqrt_lt_floor-owner-eval.json`. SourceSHA256`85af4993b70decb29489013593420d99644a93e2ac6891cecfa7cad5fb2b55f8`;current697lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma7/27 originals,overall223/264,10/14fullycompletedfiles;nextfour_lt_rpow.
Filewide final phases remain pending.


### Original8: `four_lt_rpow`

[Fresh dedicated full audit](MainLemma-four_lt_rpow.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Stronger constant3 API removes m/hm/hδm and weakens sign to0≤δ, preserves strict conclusion and all3foreign full caller contracts; proof21→18lines,0newhelpers (existing separately audited helpercount1). Exact old/current opaque-value/fulltype/name/order/BI/universe/stdaxioms and independent original/caller closures pass. Matched scoped target774.351/862.510→367.057/430.308ms. All8captures/16complete rows independently owner-reparsed; missing beforeMain repeat recovered EXACT old689f540c olean in closed isolated library, actual pair2997.107/2993.523ms. All failed imports/probes and slow foreign samples including MLmain7871.827ms retained; actual argument overhead13–34ms and broad unchanged-subtree variation disclosed, no foreign budget/global certification. Fresh root/Eval native both complete0messages/errors. Owner verified338artifacts/1.177GB, all17pins and40PGIDdrains. New true unused three.hδm warning remains original10 drop-test; globalδ/three/pigeon/main repair queues and Main-own-file queue remain mandatory.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile430.308ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild44.709s THEN separateLeanEval81.649s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/four_lt_rpow-owner-full.json` and
`four_lt_rpow-owner-eval.json`. SourceSHA256`2b8a5cab541e92ba56eb71142867bb3f562461682ccada4c07e7ea4fcfcd87a4`;current696lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma8/27 originals,overall224/264,10/14fullycompletedfiles;nextlog_B₁_gt.
Filewide final phases remain pending.


### Original9: `log_B₁_gt`

[Fresh dedicated full audit](MainLemma-log_B₁_gt.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Authorized stronger API removes hδ0/hq₁/hr₁ and weakens4<power to sharp2≤power, retaining the identical strict logarithmic conclusion;4prooflines versus6,0newhelpers. Exact entire project-original target/old paired sqrt proof and old actual callers independently recovered; complete closedTYPE/actualopaqueVALUE/fullAST/writtennames/order/BinderInfo/universes/standardaxioms pass. One necessary three_small_factors call repair; Main byte-unchanged. Final matched target83.057/81.675ms versus103.207/113.451; deterministic heartbeats836→872 are disclosed. Foreign pre-existing three_small_factors1810.373/1847.068ms versus1780.845/1832.483 and heartbeats24607→24930 remain original10 repair obligations, with all samples and bounded call/arithmetic diagnosis retained. Fresh complete unfiltered ML/Main and owner root/Eval native gates pass without errors or partial/timeout; hδm and hq₁ warnings require original10 drop-tests. Owner independently rehashed302artifacts/310104299bytes (13explicitbinarycache exceptions),17source/configpins/104productioncache artifacts, actual27workerPGIDs drained, and canonically reparsed all8 accepted exact-token column0 command/async rows. One public log_B₁_gt rename appended; queue now3, reserved for project-end single pass. Filewide global performance/simplify/cumulative/final gates remain pending.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile83.057ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild49.267s THEN separateLeanEval46.714s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/log_B₁_gt-owner-full.json` and
`log_B₁_gt-owner-eval.json`. SourceSHA256`2bfa8a61e85ead5ff702d57ff6a28ddda85c39a0d1faf960d27cb3cdede319cd`;current696lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma9/27 originals,overall225/264,10/14fullycompletedfiles;nextthree_small_factors.
Filewide final phases remain pending.


### Original9 optional-heartbeat erratum (2026-10-20)

The optional original9 target836→872 / consumer24607→24930 heartbeat figures, and
historical v6 heartbeat figures, are withdrawn from accepted corroboration. Actual runner
inputs use builtin `#count_heartbeats in`; pinned CountHeartbeats.lean143 internally sets
`maxHeartbeats 0`. The earlier bounded/no-limit-raise description was incorrect. Original
raw evidence and published report are preserved; see the [corrected audit](MainLemma-log_B₁_gt.md).
The required actual bounded wall-clock table83.057/81.675ms, exact complete-root accounting,
independent old/current type/value/standard-axiom checks, native diagnostics, and production
builds remain valid. No source or required timing result changes; counts stay225/264,
MainLemma9/27,10/14files. Original10 draft is unvalidated and excluded from this metadata-only
publication. Future optional heartbeat checks require a verified bounded custom wrapper;
no historical optional rerun is needed. The actual erratum commit follows via metadata child.


### Original6 optional-heartbeat erratum (2026-10-20)

Readonly follow-through on the original9 reporting issue confirms original6's actual
heartbeats-final.json invokes heartbeats.lean with builtin `#count_heartbeats in` at86/92.
Pinned CountHeartbeats.lean143 internally sets maxHeartbeats0; optional1588→1055 figures
are withdrawn. The default-limit description in the [corrected original6 audit](MainLemma-eta_lt_gam_iff.md)
was incorrect. Original report SHA256c48aad9c6d1ed69049829f37538b35d390bd36f3681d574deb69f6ce74187995
and raw evidence are preserved. Required bounded wall-clock281.175/208.229ms and all
correctness/native/production build gates remain valid. Original7/8 bounded custom counters
are unaffected; original8's actual strong3-hb-v1 wrapper only disables Elab.async and leaves
all resource limits unchanged. No optional compiler reruns, source changes, or count changes.
Original10 source/reports stay unvalidated and excluded from this metadata-only publication.
Counts225/264,MainLemma9/27,10/14files; future optional counters must be verified bounded.
Actual erratum commit will be recorded by metadata child.


### Original10: `three_small_factors`

[Fresh dedicated full audit](MainLemma-three_small_factors.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Stronger API removes hm/hδm/hq₁, allows nonnegative δ/A and non-strict h32, preserving all three strict conclusions; 26-line public proof plus separately freshly audited 13-line private two_lt_rpow_aux helper (helper total2, no original-count inflation). Two narrow caller applications updated with old written contracts preserved. Matched target before1812.331/1737.768ms; final helper+public681.890/685.688ms. All14 timing rows independently re-anchored; ML consumer5093.245/4954.639 versus5210.167/4831.233 and Main2971.147/3031.316 versus2958.421/3009.772 retained, including small adapter overhead; foreign slow totals remain later obligations. Verified bounded custom heartbeat raw24868514→7910547 corroborates; historical optional6/9builtin counts remain withdrawn. Owner verified490artifacts/3703515405bytes/26binary exceptions, all12201actual import hashes, exact original proofs/type/value/standard axioms,17pins and104cache; only Eval.trace metadata changed in owner builds. Fresh root/Eval native complete0messages; ML/Main complete0errors. MainLemma714/Main685lines.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile685.688ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild5.798s THEN separateLeanEval37.183s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/three_small_factors-owner-full.json` and
`three_small_factors-owner-eval.json`. SourceSHA256`8a90958369a5f7fc9357169270737fb0c6473b1d4fd8d2d3a8d6defd95119791`;current714lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma10/27 originals,overall226/264,10/14fullycompletedfiles;nextabs_coeff_modByMonic_le.
Filewide final phases remain pending.


### Original11: `abs_coeff_modByMonic_le`

[Fresh dedicated full audit](MainLemma-abs_coeff_modByMonic_le.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Generalizes integer absolute coefficients to norms over arbitrary SeminormedRing, removing hf/hA/hC and requiring no commutativity/separation/Nontrivial/NormOneClass. Public proof58→15lines, branch10; one separately freshly audited27line helper, helper total3 without original-count inflation. Exact entire project-original proof, old integer adapter and complete entry ML/Main caller proof bodies pass5full rawAST/binder/order/universe/closedTYPE+actualVALUE/standard3axiom pairs and4nonself closures;12boundary/countercertificates include Quaternion and zero-seminorm nontrivialℤ. Final combined helper+public699.676/781.456ms versus745.518/701.298, both<1000 with no aggregate speedup claim; MLmain4914.491/5012.854 versus5129.205/4906.795 stays in baseline range, changed-call101.651/102.334 versus182.301/179.507 is nested diagnostic only. SupersededV1 source/scaffold/streams/runner/cache preserved, no unchangedthirdcapture; no finalV2 optionalheartbeat claim. Owner independently re-anchored13actual profile rows, verified740artifacts941217592bytes52binary exceptions andALL12201setup import artifacts1803534984bytes,17pins104actualsavedcache, exact helper8036cf and all23originalworker+35helper groups drained. Fresh ML/Mainnative complete0errors with1/4existingwarnings; ownerroot/Evalnative complete0messages. MainLemma714→706, Main685unchanged. Fourth rename Roth.abs_coeff_modByMonic_le→Roth.norm_coeff_modByMonic_le queued; all4 deferred to project-end SINGLEpass. MainLemma finalglobalδ/pigeon/main/simplify/cumulative stages remain mandatory.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile781.456ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild46.731s THEN separateLeanEval43.641s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/abs_coeff_modByMonic_le-owner-full.json` and
`abs_coeff_modByMonic_le-owner-eval.json`. SourceSHA256`c1a4c252c37d2f2eb7399a556aaf67adab471fd44da859607d178c64877e5735`;current706lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma11/27 originals,overall227/264,10/14fullycompletedfiles;nextboxFamily.
Filewide final phases remain pending.


### Original12: `boxFamily`

[Fresh dedicated full audit](MainLemma-boxFamily.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Generalized Fin-indexed DATA to arbitrary universe-polymorphic index type without finite or DecidableEq premises; integer predicate unchanged, all six callers/Main/queue/helper bytes preserved. Actual old DATA values and generic expected value, 10 exact contracts/20 closed TYPE+VALUE standard-axiom guards/9 nonself closures and seven boundary certificates pass. Before20.007/16.163ms to after17.191/17.009ms; main4925.516/5016.532ms remains preexisting original27 queue. Owner independently rehashed410artifacts690794734bytes26binary exceptions plus all12201imports1803535736bytes, validated28 exact profile rows,17pins104cache, fresh full ML/Main/Eval native0errors and root/Evalnative0messages; helpercount3, no original-count inflation. Full finalfile GLOBAL/simplify/cumulative gates remain pending.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile17.191ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild5.542s THEN separateLeanEval5.528s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/boxFamily-owner-full.json` and
`boxFamily-owner-eval.json`. SourceSHA256`eebbee905ea9d8083437e050614060841c8414a42c3aef00fc547aa0737e26df`;current707lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma12/27 originals,overall228/264,10/14fullycompletedfiles;nextboxPoly.
Filewide final phases remain pending.


### Original13: `boxPoly`

[Fresh dedicated full audit](MainLemma-boxPoly.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Private DATA generalized from Fin m to arbitrary universe-polymorphic finite sigma with explicit Fintype and DecidableEq; bounded integer-array semantics and exact old Fin-m TYPE/VALUE recovered. Three redundant written ascriptions removed with identical raw elaborated value; private comment exact prose retained. All five actual TYPE/VALUE direct consumers include inferred finite/cardinality uses and remain source-byte-identical; associated generated equation checked separately and its kernel cost counted once in coeff command. Nine contracts/19 closed TYPE+actualVALUE standard-axiom guards/seven independent old closures, four closed actual-target application cases and exact actual edge inventory pass. Target40.490 to48.922ms, all five consumers below114ms, no repeats required. Owner verified383artifacts116564478bytes26binary/all12201imports1803540728bytes/17pins104before-and-finalcache/12 exact profile rows plus noncomputable pinned-source zero-codegen root rule; completeML/Main/Eval native0errors1/4/0warnings and freshroot/Evalnative0messages. No helpers/caller edits/queue changes; finalfile GLOBAL/simplify/cumulative remain pending.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile48.922ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild5.618s THEN separateLeanEval3.019s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/boxPoly-owner-full.json` and
`boxPoly-owner-eval.json`. SourceSHA256`8812f171cfb7b6bcb4103e09f0c20cc261d5fc8e39a39ebd3b85d10f5dd41ae0`;current707lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma13/27 originals,overall229/264,10/14fullycompletedfiles;nextcoeff_boxPoly.
Filewide final phases remain pending.


### Original14: `coeff_boxPoly`

[Fresh dedicated full audit](MainLemma-coeff_boxPoly.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Private coefficient lookup generalized from Fin m to arbitrary universe-polymorphic finite sigma with explicit Fintype/DecidableEq; exact old dependent integer formula and full Fin-m contract recovered. Proof11 to6lines, target14 to9, ML707 to702; narrow redundant Nat ascription omitted only after exactTYPE AST/isDefEq guard. No helpers/caller/Main/queue changes. Independent8contracts/16closedTYPE+actualVALUE+inferredTYPE/std3guards/6nonselfoldclosures plus4actualtargetboundary properties and exact2directusers pass. Material compact-proof627.915ms cost retained and repaired by measured explicit-rule simplification; final matched target77.199 to78.976ms, callers22.669 to24.520 and101.289 to105.891, all below750/no repeats. Owner verified578artifacts166265072bytes39binaryexceptions/all12201imports1803555232bytes/17pins104before-final-currentcache/6selected exactrows and preserved395ref costly revision; all27leafgroups absent. CompleteML/Main/Evalnative0errors1/4/0oldwarnings and freshroot/Evalnative0messages. Finalfile GLOBAL/simplify/cumulative remain pending.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile78.976ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild6.346s THEN separateLeanEval5.512s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/coeff_boxPoly-owner-full.json` and
`coeff_boxPoly-owner-eval.json`. SourceSHA256`a2f7c750073759a03b09f9400705f87ade7c5c18aa568fc3d72a6cf0451a15c8`;current702lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma14/27 originals,overall230/264,10/14fullycompletedfiles;nextboxPoly_injective.
Filewide final phases remain pending.


### Original15: `boxPoly_injective`

[Fresh dedicated full audit](MainLemma-boxPoly_injective.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Private box polynomial injectivity generalized from Fin m to arbitrary universe-polymorphic finite sigma with explicit Fintype/DecidableEq, preserving exact original bounded integer-array DATA and old Fin-m contract. Composed function and Fin extensionality with terminal coefficient congruence simplifies declaration6 to3lines, ML702 to699; no helper/caller/Main/queue edits. Genuine project-original constructor/coefficient/injectivity proofs and entire entryML independently reelaborated:9exactcontracts/25closedTYPE+actualVALUE+inferredTYPE/std3/7nonselfoldclosures,4actualtargetboundaryproperties,sole directTYPEVALUEconsumer ncard,plus expanded effective-array/equality-binder AST/isDefEq/std3 supplement pass. Matched target27.752 to46.624ms and ncard16.982 to19.117ms, honest increases/allbelow750/no repeats or aggregate speedupclaim. Owner verified432artifacts80763349bytes26binary/all12201imports1803557376bytes/17pins104before-final-currentcache/4exactprofile rows, savedPATH resolves pinned4.34Lake;18leafgroups absent. FreshcompleteML/Main/Evalnative0errors1/4/0oldwarnings; ownerroot/Evalnative0messages and cache unchanged. Allfile GLOBAL/simplify/cumulative gates remain pending.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile46.624ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild5.600s THEN separateLeanEval5.074s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/boxPoly_injective-owner-full.json` and
`boxPoly_injective-owner-eval.json`. SourceSHA256`817016b9057fbbbedaa9c6db38280bffb9cdbfcdb063b88cba4704c75f89ed48`;current699lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma15/27 originals,overall231/264,10/14fullycompletedfiles;nextrange_boxPoly.
Filewide final phases remain pending.


### Original16: `range_boxPoly`

[Fresh dedicated full audit](MainLemma-range_boxPoly.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. Private range_boxPoly generalized from Fin m to arbitrary universe-polymorphic finite sigma with exact Fintype/DecidableEq constructor instances. Direct Int.toNat_le and supported-exponent box membership preserve one common bounded coefficient-array witness while reducing declaration28 to23/file699 to694; no helper/caller/Main/queue edit. Genuine project-original family DATA, constructor DATA, coefficient/range proofs and entire entryML independently reelaborated:12exactcontracts/34closedTYPE+actualVALUE+inferredTYPE/std3/10nonself oldclosures/5actualtarget properties including common-array existential. SIX named DATA unfolds include genuine old/original/current family and constructor, restricted spine beta only; no changed-arity Name map. Matched target109.494 to89.367ms, finite8.715 to10.640 and ncard16.962 to20.568, all below750/no repeat/aggregate speedupclaim. Owner verified415artifacts80985775bytes26binary/all12201imports1803538672bytes/17pins104cache/6exactprofile rows and15leafgroups absent; actual environment byte-identical. Fresh complete ML/Main/Evalnative0errors1/4/0oldwarnings; ownerroot/Evalnative0messages, ownercache unchanged. All file GLOBAL/simplify/cumulative gates remain pending.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile89.367ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild5.474s THEN separateLeanEval5.155s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/range_boxPoly-owner-full.json` and
`range_boxPoly-owner-eval.json`. SourceSHA256`6808b77320c176564d9d60b450f59ddff6b7b319cc9a03da01dbf2a159a111eb`;current694lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma16/27 originals,overall232/264,10/14fullycompletedfiles;nextboxFamily_finite.
Filewide final phases remain pending.


### Original17: `boxFamily_finite`

[Fresh dedicated full audit](MainLemma-boxFamily_finite.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. boxFamily_finite now accepts arbitrary-universe sigma with only Finite(Function.support r), admitting infinite ambient indices with finite degree-bound support while automatically preserving finite-index r/B calls. Two standard Finset.finsupp enumerations and image AddMonoidAlgebra.ofCoeff give13proof/15declarationlines,3to15decl/ML694to708; nohelper/caller/Main/queue edit. Necessary direct Finset.Finsupp import was already transitive; actual setup/options/importArts bytes unchanged. Only ownpublicdoc and authorized added12sentence changed. Genuine original family/ctor/coeff/injective/range/finite/ncard/direct-consumer proofs plus entire entryML independently reelaborated:14exactcontracts/42closedTYPE+actualVALUE+inferredTYPE/std3/14nonselfoldclosures/8actualtargetproperties including infiniteNat finite-support cases. Owner verified423refs106151004bytes26binary and24793actual external refs3929186304bytes, with package/setup union12201/1803563080bytes and installed pinned-toolchain compiled SUPERSET12592/2125623224bytes explicitly separate. Neither catalog is claimed exact loaded closure; historical core-beforeAPI omission disclosed, initial package-only sample retained, exactoldBEFORE replay under observed samecore matches AFTER. Accepted target17.129to38.964ms/directconsumer320.078to260.369ms,4exactrows reanchored/allbelow750/no repeats/aggregateclaim. Exact709line intermediate source reconstructed/hashbound; final708SHAff29cc40. Missingthirdliteraturequery completed honestly later in separate addendum+8ref supplementarymanifest without altering original frozen report/evidence. All22leafgroups absent; freshML/Main/Evalnativecomplete0errors1/4/0oldwarnings; ownerrootEvalnative0messages/17pins104cacheNOdelta and freshpost-gate24793external hashes unchanged. Allfile GLOBAL/simplify/cumulative gates remain pending.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile38.964ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild5.894s THEN separateLeanEval2.951s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/boxFamily_finite-owner-full.json` and
`boxFamily_finite-owner-eval.json`. SourceSHA256`ff29cc40cece7f7432c7a2ddc64fd9cc73ceafd995b37b6927b7f3d2897bbac7`;current708lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma17/27 originals,overall233/264,10/14fullycompletedfiles;nextncard_boxFamily.
Filewide final phases remain pending.

[Later literature addendum](MainLemma-boxFamily_finite-literature-addendum.md) preserves the frozen original report; missing third query and an additional targeted query were completed after END, with no source change.

Remote predecessor CI [39497338608](https://github.com/SmwYin/Roth/actions/runs/39497338608) failed before code checking on pinned Lean4.34 Linux download SSL error35; root rerun pending, no source/version/workflow edit.


### Original18: `ncard_boxFamily`

[Fresh dedicated full audit](MainLemma-ncard_boxFamily.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. ncard_boxFamily now counts arbitrary-universe variable types with Finite(Function.support r), using the standard finprod formula; an exact old Finm-product adapter and unchanged whole caller contract pass. Public proof2→6lines/8declarationlines; separately fresh-audited helper4 has14proof/19declarationlines and exact8e541df5 hash. Only own public doc, authorized added12sentence, defining Finprod import and necessary caller specialization rewrite change alongside that helper; Main685lines and old3helpers/queue/7signposts/prose remain exact. Genuine original eight declarations plus entire published17 entry and audited final helper are byte-exact independent clones: wholeV3 exit0/335.618s,19full rawAST/binder/order/BI/universe contracts,54closedTYPE+actualopaqueVALUE/inferredTYPE/std3 checks,16oldnonselfclosures,10actualproperty/countercertificates and helpernonself5729 pass. V1/V2 verification-harness failures remain wholly rejected/preserved. Matched count20.499→55.913ms; helper166.314→159.934, consumer280.309→269.328, helper+count186.813→215.847, entire467.122→485.175ms, allbelow750/no repeats/no speedupclaim. Owner independently reanchored all6rows using full outer Classical wrapper and excluding2inclusive expansion commands; actual same-source/config/CLI roots preserved. Owner checked1625files516725560bytes117binaryexceptions and all24793actual package/core refs3929236352bytes, separating package/setupunion12201/1803613128 from pinned-core compiledSUPERSET12592/2125623224; neither is exactloadedclosure. Actual distinct pinnedLake/Lean and Elan proxies agree across3observations. Raw environment differs only capture-context SHLVL1→2, explicitly disclosed without byte-equalclaim. All46initial/helper/resumed groups and owner7091/7113 absent; fresh fullML/Main/Evalnative0errors1/4/0oldwarnings and ownerroot/Evalnative0messages. Owner17pins104cacheNOdelta and fresh post-gate external/binary hashes exact. Four freshly audited helpers/31retained written declarations, no264inflation. Final-fresh-review queue: compiled3line17finite proof needs helper-order move; unused private injectivity/range and internal constructor chain remain unpruned. GLOBALdelta/pigeon/main failures, cumulative22originalpublic+ALLretainedaxioms and all final file phases remain pending. All4renames stay for project-end SINGLEpass. RootCI39497338608@d953155 failed before codecheck on pinnedLean Linux download SSL35; root rerun remains pending per supplied status, with no source/version/workflow edit.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile55.913ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild5.583s THEN separateLeanEval2.788s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/original18-owner-full.json` and
`original18-owner-eval.json`. SourceSHA256`45dba9b58a75de21900d1100d8eb255c9449d68162739b63b58d8607258657dc`;current734lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma18/27 originals,overall234/264,10/14fullycompletedfiles;nextpigeonhole_count.
Filewide final phases remain pending.

[Separate fresh helper4 audit](MainLemma-helper-boxFamily_eq_image_finsupp_aux.md) preserves its initial/final contract, raw failures and provenance recovery. The introduced helper does not change the264-original count.


### Original19: `pigeonhole_count`

[Fresh dedicated full audit](MainLemma-pigeonhole_count.md):all24audit/42golf/5search/11checklist
artifacts reviewed by owner. The strict counting bound now permits positive real B and c≥1; exact original natural-B/c>1 contract recovery and the entire genuine original/current main caller passed. Public proof37→14lines/declaration40→16; published734→721source lines, with separately freshly audited helper5 (8declaration/6prooflines, exact98c198fa) and only a necessary two-line caller update. Original hB1/order/entire pre-count context, all7signposts/paper quote/Main685/old4helpers/renamequeue remain exact. Five separately audited helpers/32retained written declarations add no264credit. Final2485-line independent replay exit0/226.389s checks28fullcontracts/70closedTYPE+actualopaqueVALUE+inferredTYPE/std3/50distinctconstants/6old-entry-selectednonselfclosures/13publicproperties/5full-premise countercertificates/exactfinalH5clone16966 at default limits. Four inventoried compiler-literal pairs receive exact TYPE+VALUE AST pregates before namedDATA-only expansion; all failed harness/cast/automation/partial-sorry evidence remains rejected/preserved. Matched declaration-scoped public1034.480/1014.405→179.463/176.595ms; meaningful helper/public1181.112/1158.710→344.114/330.658ms. Superseded hB1-removal caller regression was repaired by restoring exact context; hC661.532/653.008 and hγ13.672/13.800 recovered. Whole foreign main5146.495/4950.274ms remains the original27budget failure; mean+109.3625ms/+2.214254% and every sample are disclosed. Scoped passes are not final whole-file GLOBAL certification. Owner checked1418 original19records1600735625bytes78binaryexceptions36externaltexts plus historical helper915records with an explicit old3fdsource snapshot alias; allactual24793compiled inputs3929168768bytes+4binarypaths/postownerhashes match. PACKAGE/setupunion12201 and COREcompiledSUPERSET12592 are separate scopes, neither exactloadedclosure. Fresh unfiltered ML/Main/Eval0errors1/4/0preservedwarnings; owner root/Eval0messages. Owner17pins104cacheNOdelta; all75historical/helper/original19groups+2ownerbuildgroups absent. Owner addendum MainLemma-pigeonhole_count-owner-addendum.md preserves scope/historical-input clarifications and independent evidence. Remaining20–27 and all final simplify/cumulative22public+ALLretainedaxioms/import/docs/comments/static/reference/GLOBALallrows+repairs remain pending; four project-end renames unchanged. Root supplied CI39497338608@d953155 retry SUCCESS after preserved initialElanSSL35 failure, historical evidence only, no latest-source CI claim or version/workflow edits.
Independent original reimplementation,exact old/current effective contract metadata/value
and standard-axiom evidence reviewed; complete unfiltered livefile/affectedcaller diagnostics
and actual affected-module/fullfile validation pass. Actual anchored profile179.463ms;
required repeats/failed evidence,if any,remain in the dedicated report. Owner verified frozen
source/evidence and ran fullbuild6.004s THEN separateLeanEval3.077s,both exit0 with all17pins immutable.
Owner logs:`/private/tmp/roth-mainlemma-owner/original19-owner-full.json` and
`original19-owner-eval.json`. SourceSHA256`5622adfc4372f9e84ee0239f2c14a1b810649a8a83fd7c3fe6b6691a44e18731`;current721lines.
All worker/compiler/native/profile ownership drained before publication.
Source/audit publication hash follows in central checkpoint history via metadata child.
MainLemma19/27 originals,overall235/264,10/14fullycompletedfiles;nextexists_ne_modByMonic_eq.
Filewide final phases remain pending.

[Owner review and publication addendum](MainLemma-pigeonhole_count-owner-addendum.md) preserves scoped-profile and historical-input clarifications.
