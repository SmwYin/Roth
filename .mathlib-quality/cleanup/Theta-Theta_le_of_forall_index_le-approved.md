# Approved original12 revisit — `Roth.Θ_le_of_forall_index_le`

Applied only approved A.DecidableEq σ removal, using `omit [DecidableEq σ] in` immediately
before the preserved docstring. All Fintype/B/hB/q/r/c/hc binders, ordinary names, order,
implicitness, conclusion and the canonical three-line proof remain. No caller/helper/import/
definition/header/Git/shared-log changes. Declaration body3→3; declaration6→6 plus one omit line.
This revisit does not increase original counts (Theta15/35, overall196/264).

## Preparation and baseline

Read `/private/tmp/roth_theta_leaf_instructions.md`, both full lean4/mathlib-quality skills,
full cleanup workflow, full golfing-rules, proof-patterns, mathlib-search,
generalisation-patterns, cleanup-gates and profiling references, and relevant style/naming
sections. Read original12's report and the exact decision in `Theta-contract-proposal.md`.
Remained strictly read-only until owner RELEASE after r11 publication.

Starting HEAD=origin `74fd327fad902ff31fe45f37a7ee4a6d7f75d2d0`;
Theta SHA256 `38993bdc67cd88792ffa89a59640081c117d6ad7e0bbcf03d7cb801d0592ef3d`.
Owner baseline full build65.268s THEN separate LeanEval23.107s, both exit0, frozen snapshots.
Same-source complete baseline doctor LSP reused from `/private/tmp/roth-card-api/final-lsp.json`:
success=true,partial=false,timed_out=false,failed_dependencies=[],0errors22warnings.
Optional cache/linter executables were not needed; native diagnostics supply linter evidence.
Final owner cumulative full→separateLeanEval gates remain pending and are not claimed here.

All new scratch/evidence paths below are under `/private/tmp/roth-forall-api/`.
`before.lean` is the exact release source; `immutable-original.lean` is extracted directly
from immutable commit `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`.

## Fresh substantive24 audit

|#|Item|Finding/action|
|---|---|---|
|1|LINT|Both target DecEq warnings addressed by the selected omit. Final target has no diagnostics; complete file diagnostics below.|
|2|HAVE SCAN|No have in the target, so no single-use block to inline.|
|3|SET_OPTION|No target option or limit; no production limit raised. Scratch automation lowers maxHeartbeats to2000.|
|4|SIMP SQUEEZE|No simp in the selected proof.|
|5|NAMING|Θ_le_of_forall_index_le states an upper bound from every defining index, uses snake_case components and no forbidden abbreviation/numeric scheme.|
|6|LINE PACKING|All3signature lines measured below; max92codepoints. Omit is a separate command, not a theorem binder.|
|7|BY PLACEMENT|by stays at end of the last signature line.|
|8|FORMAT|2-space tactics,4-space signature continuation with nested callback; no blank body line or haveI/letI; lambda uses ↦.|
|9|COMMENTS|No proof comment present. Both docstring lines and all surrounding narratives preserved byte-for-byte.|
|10|DOCSTRING|Public source-bearing docstring retained exactly; omit correctly precedes it.|
|11|VISIBILITY|Retained public domain API and name per established preference; two actual callers.|
|12|STRUCTURE|Body3lines; no conjunction conclusion or >10line branch; shared R/h witnesses stay correlated.|
|13|MATHLIB|Five fresh actual searches find csSup_le; generic result is used directly in the proof. No new wrapper/helper.|
|14|JUNK DEF|n/a, theorem rather than definition.|
|15|EXISTS LEMMA|n/a, public supremum inequality rather than private trivial existential.|
|16|SHOW/CHANGE|No show/change occurrence.|
|17|PUSH_NEG|No push_neg occurrence.|
|18|GENERALISE|All9original effective binders mechanically probed below; precisely selected DecEq removal applied.|
|19|INEQUALITY|hB, callback, conclusion all use ≤; complete scan below.|
|20|NORMAL FORM|Canonical csSup_le nonempty-set upper-bound form, specialized to the unchanged indexSet witnesses.|
|21|SYNTAX GENERALITY|Nonempty replacement compiles but only exposes csSup_le's existing premise; retain hB and the callback API.|
|22|IMPORT FANOUT|n/a, zero new imports.|
|23|CASTS|Zero casts changed. Existing ℤ/ℕ→ℝ conversions genuinely bridge coefficient/evaluation types; Int.castRingHom ℝ fixes map codomain.|
|24|INSTANCE-NAME|No instance declaration added or named. Retained anonymous Fintype binder may have generated-name changes; ordinary names preserved.|

## Signature packing and inequality scan

Actual `#check @Roth.Θ_le_of_forall_index_le` rendered at format.width100 in `verified.log`:
implicitσ,instanceFintypeσ,implicitB,explicithB,implicitq,implicitr,implicitc,explicithc.
Full type and every BinderInfo are printed and machine-checked there.

|Sig line|Width|Next complete block|Arithmetic|Action|
|---|---:|---|---|---|
|119|74|hc first line69chars|74+1+69=144>100|ok|
|120|73|callback index expression66chars|73+1+66=140>100|ok|
|121|92|none; proof next|n/a|ok|

The conclusion already fits its existing last line. No signature repacking is necessary.
`diff-check.json` records codepoint widths and exact expected insertion.

|#|Location|Occurrence|Action|Rename|
|---|---|---|---|---|
|1|hB|1≤B|canonical ≤ retained|none|
|2|hc|index…≤c|canonical ≤ retained|none|
|3|conclusion|ΘBqr≤c|canonical ≤ retained|none|
|4|complete signature|zero ≥/> relations; arrows excluded|none|none|

## Five fresh actual mathlib searches

Raw successful results stored in `searches.json`; returned names were inspected against
local source `.lake/packages/mathlib/Mathlib/Order/ConditionallyCompleteLattice/Basic.lean`
194–235, including actual csSup_le definition201 and its _iff/csSup variants.

|Method|Query/result|
|---|---|
|A Lean-Finder|“supremum of a nonempty set less than or equal to every upper bound”→csSup_le, ConditionallyCompleteLattice.csSup_le, csSup_le', csSup_le_iff.|
|B Loogle|`Set.Nonempty ?s → (∀ b ∈ ?s, b ≤ ?a) → sSup ?s ≤ ?a`→csSup_le and DirectedOn.csSup_le.|
|C LeanSearch|“supremum nonempty set is less than an upper bound”→csSup_le, ConditionallyCompleteLattice.csSup_le, sSup_le, csSup_le'.|
|D source rg|Untruncated csSup_le/csSup_le_iff/csSup_le_csSup search in canonical Basic.lean; inspected exact source.|
|E local-name|csSup_le limit8→base,_iff,_iff',csSup and DirectedOn variants; index unavailable but source hits valid.|

Auxiliary variants checked: csSup_le',csSup_le_iff,csSup_le_csSup,DirectedOn.csSup_le;
prior Real.sSup_empty infrastructure is used in the freshly recompiled counterexample.
Common equivalent: conditionally complete lattice supremum upper bound. Presence is
established; unavailable indexing/search timeouts are never used as absence evidence.
The existing protected domain API remains; no proposed deletion or public churn.

## Every original effective binder — fresh compiled probes

`positive.lean` compiled exit0 before the edit, independently establishing the selected
no-DecEq proof without classical, immutable original proof, nonempty alternative and
counterexample certificates. `negative.lean` freshly compiled expected exit1 with
autoImplicit=false. It is exploratory failure evidence, not an axiom/absence certificate.
`verified.lean` separately compiled exit0 against the actual built edited constant.

|#|Binder/class|Compiled drop/weakening evidence|Decision|
|---|---|---|---|
|1|σ:Type*, type variable|Literal omission reports unknownσ; selected/original proofs compile arbitrary universeσ.|Retain already-universe-polymorphic index type; no domain restatement.|
|2|Fintypeσ, class|Drop and Finite replacement both fail Fintype synthesis in index/Θ statement. No applicable weaker parent makes those expressions typecheck unchanged.|Retain; changing definition elaboration to ofFinite is unrequested restatement.|
|3|DecidableEqσ, decidability|Fresh SelectedForall12 proof compiles with no classical and noDecEq; actual AST has none after omit.|Apply exactly the approved removal. Earlier original12 needed classical because old nonempty helper still carried DecEq; revised dependency no longer does.|
|4|B:ℝ, structure value|Literal omission gives unknownB; independent selected proof arbitraryB under hB.|Retain dependent coefficient bound and implicitness.|
|5|hB:1≤B, proposition|Drop gives unknownhB in original argument; 0≤B mismatches1≤B. Fresh B=0,c=−1 certificate mathematically refutes both unrestricted and merely nonnegativeB statements.|Retain. Nonempty variant compiles but is optional existing csSup_le premise, not a selected replacement.|
|6|q:σ→ℕ, structure value|Literal omission gives unknownq; positive selected proof arbitrary naturalq and unchanged universalcoprimality callback.|Retain; no positivity restriction introduced.|
|7|r:σ→ℕ, structure value|Literal omission gives unknownr; positive selected proof arbitrary naturalr with nohr.|Retain dependent weights; no conclusion/domain change.|
|8|c:ℝ, structure value|Literal omission gives unknownc; positive selected proof arbitraryc including negative bounds.|Retain; restricting0≤c would weaken the theorem.|
|9|hc, proposition|Literal drop trial le_rfl leaves stuck typeclass metavariable, inconclusive alone; fresh hc_needed proves no bound∀c, using nonnegativity atB=1 andc=−1.|Retain exact universal callback; it supplies each member's upper bound.|

Fresh `FreshForall12.zero_empty` proves `indexSet 0 q r = ∅` by forcing every coefficient
to zero. Then `negative_counterexample` gives the callback atc=−1 vacuously while
`Θ 0 q r = sSup ∅ = 0` makes the conclusion false. All these fresh positive certificates
and hc_needed have exactly the standard three axioms.
Point-localization/strict→weak catalogues add no other useful candidate: hB is already
nonstrict, hc already restricts to exactly admissible witnesses, and data parameters
occur in the mathematical definitions. No new well-supported API recommendation or
optional companion is needed. Prior hq/D–F preservation choices remain untouched.

## Public literature and inversion

Fresh WebSearch queries: “supremum least upper bound nonempty set completeness theorem
generalization”; “Takloo Bighash Yin Formalizing Roth theorem index supremum”. Combined
response's leading hits were Wikipedia Least-upper-bound property, Berkeley Econ204
completeness lecture notes, MathBuff supremum/completeness. No exact Roth-paper match was
assumed from those generic results. Primary formulation used:
[Penn analysis notes](https://www2.math.upenn.edu/~gressman/analysis/01-completeness.html),
which state existence of the least upper bound for nonempty bounded-above real sets;
[Berkeley lecture notes](https://eml.berkeley.edu/~cshannon/e204_21/lec2sl-marked.pdf)
also formulate the supremum as below every other upper bound. Mathlib's inspected source
provides the broader conditionally complete lattice form. Local authoritative paper text
`clean.tex`650–703 defines Θ and invokes taking the supremum to conclude Lemma5.
ChatGPT math MCP is unavailable in current tool metadata; no second-opinion claim.

Inversion FIRES: after selecting csSup_le and unpacking indexSet, the proof uses the
abstract upper-bound principle. That abstract theorem already exists; no new abstraction
or helper is needed. Existing public domain callback is convenient in both actual callers
and is preserved by the explicit standing preference.

## All42 golf rules, freshly reconsidered

|Rule|Concrete status|
|---|---|
|1.1 by exact|n/a, three mathematical refine/rintro/exact steps.|
|1.2 by rfl|n/a, arbitrary supremum bound is not reflexive.|
|1.3 rwa|n/a, no rw.|
|1.4 simpa using|n/a, no simp/exact chain.|
|1.5 trailing rfl|n/a, no simp/rfl tail.|
|1.6 constructor|n/a, no constructor chain.|
|1.7 apply/exact|n/a, refine introduces a substantive witness-destructing callback.|
|1.8 by_contra!|n/a, direct proof.|
|1.9 eta|Evaluation lambda is not eta-reducible; already uses ↦.|
|1.10 inline have|n/a, no have.|
|1.11 refine/fun|Already refine; rintro destructs correlated witnesses.|
|1.12 show|n/a, no show.|
|1.13 obtain|n/a, no have/projection pair.|
|1.14 merge rw|n/a, no rw.|
|1.15 terminal simp|n/a, no selected simp.|
|1.16 nonterminal simp|n/a, no selected simp.|
|1.17 dot|csSup_le is an unbundled theorem; no natural receiver simplification.|
|1.18 <||No removable wrapper/trailing parenthesis.|
|1.19 push Not|n/a, no push_neg.|
|1.20 existential inline|n/a, not a private existential helper.|
|2.1 grind|Fresh target-free anonymous bounded trial fails; raw trials.log.|
|2.2 before grind|n/a, no grind in selected proof.|
|2.3 simpa|No simp stage; fresh simp[Θ,indexSet] trial leaves the supremum goal.|
|2.4 fun_prop|n/a, no function-property predicate.|
|2.5 positivity|n/a, arbitrary upper boundc may be negative.|
|2.6 gcongr|Fresh bounded trial makes no progress.|
|2.7 lia/omega|n/a, arbitrary real supremum membership, no Nat/Int linear arithmetic goal.|
|2.8 aesop|Fresh bounded trial makes no progress.|
|2.9 norm_num/cast|n/a, no closed numeric or cast-normalization goal.|
|2.10 decide|n/a, arbitrary real supremum/universal callback.|
|2.11 field_simp/ring|n/a, inequality is not a denominator identity.|
|2.12 linear_combination|n/a, no ring-ending proof with algebraic hypotheses.|
|2.13 wlog|n/a, no symmetric cases.|
|2.14 calc→term|n/a, no calc; explicit csSup_le plus pattern destructuring remains clear.|
|2.15 <;>|n/a, one callback goal.|
|3.1 erw→rw|n/a, no erw.|
|3.2 fun_prop|n/a, no legacy function-property tactics.|
|3.3 omega→lia|n/a, no arithmetic tactic in target.|
|3.4 rfl subst|Already rintro…rfl substitutes the witness equality.|
|3.5 attribute|No new canonical rewrite/automation use demonstrated; no attribute added.|
|3.6 simp_all|n/a, no simp_all.|
|3.7 limits|No source limit present/raised.|

Fresh `trials.lean` preserves exact release source/imports/context strictly BEFORE the
target and every later declaration; all six trials are anonymous examples, so failed
named declarations cannot contaminate exact?/apply? suggestions. grind/simp/aesop/gcongr
fail as above; exact?/apply? each hit lowered2000heartbeats and are inconclusive. No target
or prior failed trial cited. Known stalled full-Theta multi_attempt was not retried;
bounded independent direct compiler exploration completed expected exit1 and drained.
These failed trials certify neither absence nor axioms.

## Step-back / simplify review

The existing proof directly applies the generic nonempty supremum bound, unpacks an
admissible polynomial and rational point, and applies hc to those same witnesses.
A term proof would move the pattern match into a lambda without improving the argument.
No duplicated skeleton calls for a helper; no new identifier or casts introduced.
Built-in simplify tool unavailable in current metadata; direct scoped holistic review
PASS-THROUGH. No extraction/decomposition/rename or shared queue/log work is warranted.

## Verification

Actual command `/Users/ramin/.elan/bin/lake build Roth.Theta` exited0,2423jobs;
raw `module.log`. Then `/Users/ramin/.elan/bin/lake env lean
/private/tmp/roth-forall-api/verified.lean` exited0; raw `verified.log`.
The independent namespace copies the immutable original source prefix, including old
RSet/indexSet/Θ values, old one_mem_RSet/indexSet_nonempty proofs and target proof.
It never uses the current target to prove the old mathematical argument.

The verifier separately checks the full old9 argument lambda adapter against the
independent original type and kernel-checks equality to the old constant by rfl. It
compares actual-new8 type against independent selected type modulo universe alpha-renaming,
checks all retained ordinary names/order/BinderInfo, and scans the ENTIRE actual type AST
for DecidableEq. Only the removed synthetic anonymous class binder is omitted from metadata;
anonymous-instance generated names are exempt, not their types/order/BinderInfo.
All printed actual/original/selected/adapter/certificate and both actual caller axioms are
exactly `[propext,Classical.choice,Quot.sound]`.

Repository-wide actual-use inventory: only Θ_unique_le and Θ_option_le in Theta, now
lines232/629; no external direct use. Both unchanged production calls compile in the
module gate. A separate exact `refine ... hB fun R hR h hh ↦ ?_` call compiles with noDecEq
against actual Roth definitions. No caller source bytes or caller explicit arguments changed.

Fresh native COMPLETE UNFILTERED `lean_diagnostic_messages(Theta.lean,timeout_s=60)`:
`final-lsp.json` has success=true,partial=false,timed_out=false,failed_dependencies=[],
0errors21warnings. Both target DecEq warnings disappear. The simplification also exposes
an unused-section DecEq warning in Θ_unique_le (its A removal is already approved for its
later dedicated audit), giving total22→21. Other pending declarations and protected header/
hypotheses account for remaining warnings; none suppressed or broadened into this edit.

`diff-check.py` asserts final source equals the released source with exactly the single
approved omit insertion. `change.diff`/`diff-check.json` certify identical documentation,
proof, surrounding source, zero comments removed and zero new mathematical identifiers.
No hallucinated reference introduced; csSup_le independently found and compiled.

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|pass|Actual lake build Roth.Theta exit0; module.log.|
|definition_protected|pass|No definition edits; exact expected-diff assertion.|
|theorem_statement_protected|pass|Only approved DecEq removal; old9 recovery and exact new8 type/metadata/AST checks exit0.|
|structure_gate|pass|Body3, no long branch/conjunction conclusion.|
|naming_gate|pass|Descriptive bound theorem, no forbidden pattern.|
|line_packing_gate|pass|All3lines measured, max92.|
|inequality_orientation_gate|pass|Complete scan, zero reversed relation.|
|axioms|pass|Actual built constant, immutable proof, adapter, selected proof, certificates, callers standard3only.|
|live_LSP|pass|Fresh complete unfiltered0errors21warnings; no target diagnostics.|
|callers|pass|Both actual callers compiled by module build; no caller edit; separate noDecEq call trial.|
|owner full→separateLeanEval|pending owner|Only owner runs these after leaf freeze/drain; not claimed complete.|

Per-leaf ordinary gates pass. No source edit after this point; source authority revoked.

## Buzz pass

Profile results are recorded below after all ordinary compiler and native LSP requests
have fully completed. Exact source prefixes preserve all preceding imports/context and
end immediately after the target with namespace closure. This is PREFIX-ONLY evidence;
no whole-file profile pass is claimed. The owner's final whole-module sweep remains
mandatory after the known later default-heartbeat hotspot is repaired.

FAST-BOARD. Both sequential commands exited0 after all ordinary requests drained:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 /private/tmp/roth-forall-api/before-prefix.lean`

and the same real Lean4.34 command on `final-prefix.lean`.
Raw UTF8 `before-profile.log` and `final-profile.log`; reproducible parser
`profile-summary.py` and summary `profile-summary.json`.

|Target|Outercommand|Asyncproof|AsyncaddDecl/kernel|Asynclinter|Total|
|---|---:|---:|---:|---:|---:|
|Before|12.676ms|7.369ms|2.804ms|4.826ms|27.675ms|
|Final|12.934ms|8.017ms|2.670ms|5.224ms|28.845ms|

Final outercommand is the `omit ... in` command at log122472, which explicitly prints the
audited theorem. Its inner docstring command12.426ms and generated section/omit/end commands
are covered by the outer12.934ms and are NOT counted again. Before outercommand is the
docstring/theorem at log119738. All associated top-level async proof/addDecl/kernel/linter
entries through the next command are counted; nested tactic/kernel timings are not double-counted.
No theorem compilation async entry exists. Both totals are below750ms repeat threshold and
1000ms budget; no performance improvement claim for the API-only edit. Limit raises removed0,
added0; no profiling scaffolding or production helper; no deferral.

## 11-step checklist and handoff

- [✓] Step1: full required references/workflow read.
- [✓] Step2: full substantive24 audit above.
- [✓] Step2.5: five actual fresh mathlib methods and auxiliary variants.
- [✓] Step2.6: all9original binders, compiled fresh probes, public literature/inversion.
- [✓] Step2.7: complete measured signature packing table.
- [✓] Step2.8: complete inequality scan.
- [✓] Step3: all42golf rules explicitly considered; relevant anonymous trials compiled.
- [✓] Step4: step-back and direct simplify review.
- [✓] Step5a: complete fresh unfiltered native final LSP, no errors.
- [✓] Step5b: exact diff/old adapter/new AST/type/metadata/axiom/module/caller/profile gates.
- [✓] Step6a: no rename warranted; no queue/shared-log mutation.

All source authority is revoked and every native/compiler/profile session is terminal and
drained before handoff. Final source SHA256
`962dca983519c78afaa1b9c90d9addb33652a95f9f768fc417fd973a9975ed11`.
Only repository edits: single approved omit insertion and this dedicated report. Source bytes
stayed frozen through final profile. No Git mutations. Owner full project THEN separate
Roth.LeanEval and publication remain pending; no owner-gate success claimed here.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 102.795 s and 31.734 s.
Theta SHA256 `962dca983519c78afaa1b9c90d9addb33652a95f9f768fc417fd973a9975ed11` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-r12-full.log` and `/private/tmp/roth-theta-r12-leaneval.log`; machine record
`/private/tmp/roth-theta-r12-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this approved revisit before the next source edit. This revisits original 12; original counts
remain Theta 15/35, overall 196/264, 9/14 files. No new original or helper is counted.
