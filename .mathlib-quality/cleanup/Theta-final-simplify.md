# Fresh independent filewide Theta review — findings handoff

Outcome: **ISSUES-FOUND-NOT-FIXED**. The frozen source needs two supported public
hypothesis removals, each through its own fresh dedicated declaration checkpoint. No live
Lean source changed. This is a findings handoff, not final file completion or publication.
No standalone simplify skill is exposed; I performed its independent reuse, quality and
efficiency assessment directly, using lean4 and mathlib-quality plus installed cleanup
Phases5a/6/6.5/6.6, cleanup-gates and golfing-rules. Standing user authorization governs
these recommendations; the explicit retained global Θ/hq/header/wrapper/domain choices stay.

Reviewed complete current file (990 lines,50 declarations), cumulative diff against2b64544
(706 insertions/697 deletions), all35 original audit paths,18 retained introduced helpers,
and4 introduced/deleted helpers. HEAD `af23763141cda3be5157d5662ba440c5e1e99448`.
Theta SHA256 `1b62c7dd177609e4cf6544e8c06b9ead761506122391e2345fd5db35fa46b4cc`.
Evidence root: `/private/tmp/theta-filewide-review/`.

## Concrete substantive recommendations, assessed before mutation

1. Remove only `index_le_Θ.hr : ∀ j,0<r j` (original9). Boundedness is already unconditional;
   its proof is the same direct `le_csSup` application. This permits zero weights, removes
   an unused public obligation/warning and deletes two redundant positivity arguments in
   `index_separated_mul_le_aux` plus the argument at MainLemma676. `main_lemma.hr0` has
   other uses and remains. No public caller theorem type needs changing.
2. Remove only `Θ_unique_le.hr : 0<r default` (original20). The existing private logarithmic
   bound already accepts arbitrary natural weights. This exposes its zero-weight case
   `Θ B q (fun _ ↦ 0) ≤ 0`, removes an unused public obligation/warning and deletes two
   arguments in `theta_lt_base_aux` / `theta_scaled_unique_le_aux`. Keep hB, hq, Fintype,
   names, conclusion, retained argument order and all other public contracts.

`TechnicalRetentions.lean` independently copies/proves the entire current Theta file with
exactly these two drops and routine internal callers, old positive-weight adapters and two
zero-weight applications. `TechnicalRetentionsWithMainLemma.lean` also independently
copies/proves the ENTIRE updated current MainLemma file, changing only its obsolete
`index_le_Θ hr0` argument (plus namespace context). `ExactOriginalAdapters.lean` separately
uses the exact original target signatures including explicitly stated old Fintype/DecidableEq
section instances. All three actual `lake env lean <absolute scratch path>` commands exited0;
raw logs, exact SHA256 and command results are in `positive-compiler-results.json`.
These are concrete candidates, not new actual Root metadata/opaque-value/axiom certificates.

Production inventory is `technical-retention-callers.json`: original9 has2 internal calls
and1 external MainLemma call; original20 has2 internal calls and no external production call.
The module-doc mention is classified as prose, not a caller. No other substantive proof,
helper, API, import or structure recommendation survived this whole-file assessment.
Routine header/doc/import edits have deliberately not been mixed into these API checkpoints.

## Structural / reuse / style assessment

`structure.json` records all50 bodies. All7 module Main-results meet15 noncomment body lines
(Θ_lt15; Θ_option_le5; Θ_unique_le3; Θ_le_card5; others≤3). All other proof bodies≤30; the longest are
`index_separated_mul_le_aux`, `theta_prefix_lt_aux`, `theta_phi_lt_aux` at30. Signature-local
`let M :=` in the phi statement is not mistakenly counted as its proof boundary. All explicit
branches and local subproofs were inspected: numeric quadratic branch9, prefix ratio branch8,
public induction zero branch8, and remaining blocks≤10. `signature-packing.json` measures183
signature lines in codepoints and next complete items; maximum file width100. Parenthesized
casts/conclusions are semantic expressions, not binder-packing opportunities. No repacking
or declaration rewrite is needed.

The two repeated index-bound specializations in boundedness/cardinality are short direct
applications serving different supremum facts; extracting a forwarding wrapper adds no useful
mathematics. The linear/quadratic positive-part estimates, determinant mapping, separated
product estimate, coefficient/exponential estimates and induction stages have distinct
mathematical roles; no duplicated substantial proof skeleton needs another helper. The
correlated existential witnesses in factorization and index_le_lem6 remain together. RSet's
conjunction is its data predicate, not an ordinary theorem bundle. No instance declaration,
numbered helper, new custom predicate, trust/limit/scaffolding change or unwanted API rename.
The one authorized Index rename remains the owner's global-pass item.

Import set is unchanged cumulatively (only order changed): logarithms, real powers and Gauss
lemma are used directly; CoeffNorm, Index and Separation provide coefficient/index/determinant
APIs. CoeffNorm is also transitively reachable through Separation; retaining its direct import
accurately records actual API use and adds no fanout. No new dependency or promotion needed.
Five public definition values/types remain unchanged (lambda arrow spelling only in2 bodies),
with the exact kernel checks inherited in the owner's cumulative scaffold.

## Cumulative comment, identifier and audit artifacts

- `proof-comments.md/json`: every one of11 original proof signposts traced.10 retained/re-anchored;
  the removed antitone comment restates `have hanti : Antitone r`; a new small-index explanation
  makes the total11. The lower/upper determinant comment only changes capitalization. This is
  explicit justification, not a blanket count claim. Source attribution/header content matches
  the local §5 source and preserved user header decision.
- `external-reference-table.md/json`: full cumulative new-identifier classification and97
  normalized positive external `#check` expressions, with per-name actual native lookup and
  pinned source-search hits. Index availability is reported honestly as unavailable; empty
  searches never prove absence. `References.lean` compiled exit0 after refreshed local/source
  searches, with no errors. Core/generated names unresolved by text lookup are positively
  checked in Lean. Project declarations, binders, projections and syntax are classified apart.
- `audit-inventory.md` / `report-inventory.json`: all35 originals and22 introduced-helper
  histories,78 report hashes and concrete gate/FIRST line pointers.3 removed ORIGINAL private
  declarations are separate from4 introduced/deleted helpers. The latest mapped performance
  report supplements the frozen inventory. No helper or performance revisit inflates originals.
- `hash-FIRST-verification.json`:17/17 frozen source pins and23/23 inherited FIRST paths
  exactly match;9 older-helper FIRST supplements are present/hashed, including the logarithmic,
  linear/quadratic, coefficient/exponential and deleted coefficient-wrapper provenance.
- `textual-gates.log`: actual rg over Theta/MainLemma/Main/LeanEval/root finds no TODO/FIXME,
  option, inline code λ, dollar, push_neg, sorry/admit/axiom scaffolding. Only2 MainLemma docstring
  λ occurrences match, and are prose. No suppression was introduced.

## Gate boundary and pending work

Fresh full native diagnostics are recorded separately below when drained. All warning
exceptions remain visible. Theta's protected exceptions are copyright/header, Θ_nonneg hB/hr,
Θ_le_card hB, Θ_mono hr and index_le_lem6 hq; its two technical hr warnings are the proposed
removals. MainLemma/Main existing unused premises and headers are outside this file's scope.

Owner's preceding exact-source semantic806-check/full-build/separate-LeanEval/performance
results are inherited evidence, not freshly run here. No duplicate whole semantic scaffold,
full build, or actual whole-file profiling sweep was run in this bounded review. Owner must
perform EACH dedicated original9/original20 checkpoint sequentially with exact original
adapters,4 byte-identical canonical proof blocks, new actual Root telescope/opaque values/
standard axioms and entire updated MainLemma proof, unfiltered native checks, affected real
profiles, full build THEN separate LeanEval, exact stage/commit/push/clean. Necessary metadata
probe migrations must be inverse-recoverable and old compatibility probes labelled honestly.
Then obtain a fresh final independent review and final owner cumulative whole-file gates.
MainLemma actual finite timing is still unmeasured; no performance pass is claimed for it.

Pending: `[index_le_Θ dedicated hr checkpoint, Θ_unique_le dedicated hr checkpoint,
fresh final independent assessment, owner final cumulative gates/publication]`.
New helpers this review:0. Source/proof edits this review:0. Original/file credit this review:0.

## Fresh complete native diagnostics and terminal release

Actual unfiltered `lean_diagnostic_messages` calls completed on all5 modules (no declaration,
range or severity filter): Theta0errors/8warnings, MainLemma0/3, Main0/4, LeanEval0/0, root0/0.
Every result has success=true,partial=false,timed_out=false,failed_dependencies=[]. Raw complete
responses are `native-*.json`; `native-summary.json` preserves every warning's line/message.
No warning is suppressed. Source pins remain the published17/17; full actual MainLemma source
copy recovery is separately checked in `entire-mainlemma-copy-check.json`.

All4 ordinary compiler probes and all97 native search calls plus5 diagnostic calls are drained;
no profiler was started. There are no in-flight reviewer requests. Live source and compiler/
native/scratch/report authority are revoked at this terminal handoff. Owner alone may apply
and publish the two dedicated fixes, then commission fresh final review. This report's status
remains ISSUES-FOUND-NOT-FIXED; pending work above prevents final Theta completion credit.

Process-enumeration limitation: the final `ps -Ao pid,command` check was denied by the sandbox
(`operation not permitted: ps`). Drain evidence is the observed completion/exit0 of every
reviewer-started compiler session and completion of every native call; this is not a claim
that an unrestricted system-wide process scan succeeded. Owner may use its established drain
method before final profiling. No review-started compiler/profile/native work remains active.
