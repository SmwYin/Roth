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
