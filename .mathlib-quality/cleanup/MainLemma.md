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
