# Approved revisit original10 — `Roth.Θ_nonneg`

The exact selected A amendment removes only `DecidableEq σ`, by inserting
`omit [DecidableEq σ] in` before the original docstring. Fintype σ, B, hB, q, r, hr,
all ordinary names/order/implicitness and the conclusion are retained. The existing
canonical three-line proof stays unchanged. The user expressly retained D.hB/hr;
the stronger D candidate is not reopened or applied. No helper or caller edit.
This revisit does not increase original-declaration counts (196/264; Theta15/35).

## Preparation and baseline

Read `/private/tmp/roth_theta_leaf_instructions.md`, full Lean4/mathlib-quality skills,
full cleanup command, full golfing-rules/proof-patterns/mathlib-search/generalisation-patterns/
cleanup-gates, relevant style/naming sections and full profiling reference; read previous
Theta-Theta_nonneg report and exact Theta-contract-proposal decision. Read-only preparation
continued until owner's explicit RELEASE after r09 publication. No writes/compiler/LSP/search/
profile before RELEASE. No Git/shared log/rename queue write at any point.

Published r09 HEAD `bbd4d8a1d49b0527a8070f4b1412f1716cd60391`, source SHA256
`4d5ff0a2c7715084f7c0dfeffd93d22467e2bce175501e7e60c81d427d693607` matched locally.
Owner supplied full build57.757s THEN separate LeanEval12.932s, both0; reused identical-source
complete baseline native LSP `/private/tmp/roth-index-theta-api/final-lsp.json`, success=true,
partial=false,timed_out=false,failed_dependencies=[],0errors27warnings. Cache not needed;
baseline project gates are owner evidence, not newly claimed worker invocations.

All new raw evidence is under `/private/tmp/roth-nonneg-api/`. `before.lean` is the exact
released source. Immutable original baseline is `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`.

## Full substantive 24-item audit

|#|Item|Finding/action|
|---|---|---|
|1|LINT|Unused DecEq is precisely approved for omission; protected unused hB/hr remain without suppression.|
|2|HAVE SCAN|No have in the original or current target proof; no single-use intermediate.|
|3|SET_OPTION|None in target; no production option/limit changes. Scratch automation lowers to2000.|
|4|SIMP SQUEEZE|No simp in target; fresh isolated simp[Θ] does not close supremum goal.|
|5|NAMING|Θ_nonneg names the actual Θ object's nonnegativity, no forbidden patterns/abbreviations. Public wrapper retained by explicit choice.|
|6|LINE PACKING|Both signature lines measured below; no underpacked break.|
|7|BY PLACEMENT|by remains at end of conclusion line.|
|8|FORMAT|2-space proof/4-space signature continuation; no internal blank line, haveI/letI, lambda change or semicolon.|
|9|COMMENTS|No target inline comments originally; complete source-bearing docstring unchanged.|
|10|DOCSTRING|Protected source claim still correct with hB/hr retained; omit placed before docstring.|
|11|VISIBILITY|Public headline theorem remains public under explicit retained-wrapper preference.|
|12|STRUCTURE|Three-line headline proof≤15; no ∧ conclusion or >10-line branch; shared R/h witnesses stay correlated.|
|13|MATHLIB|Fresh five searches identify Real.sSup_nonneg, already used directly; no new wrapper/helper.|
|14|JUNK DEF|n/a: theorem, no definition.|
|15|EXISTS LEMMA|n/a: public inequality, not private trivial witness theorem.|
|16|SHOW/CHANGE|Neither occurs.|
|17|PUSH_NEG|None.|
|18|GENERALISE|All8 original effective binders freshly probed below; only selected DecEq omission applied.|
|19|INEQUALITY|hB,hr,conclusion all canonical smaller-left; no ≥/>.|
|20|NORMAL FORM|0≤Θ is canonical nonnegativity; supremum API used directly. No automation attribute changes.|
|21|SYNTAX-GEN|Selected omission improves inference without changing ordinary application syntax; D.hB/hr remain protected.|
|22|IMPORT FANOUT|n/a: no new import.|
|23|CASTS|0 dropped/0 introduced/0 retained ascriptions in diff; underlying definitions untouched.|
|24|INSTANCE-NAME|No instance declaration; anonymous generated binder renumbering exempt from name equality as instructed.|

## Signature packing and inequality tables

Actual width100 #check and actual constant metadata are recorded in `contract.log`.

|Signature line|Codepoints|Next complete token|Arithmetic|Action|
|---|---:|---|---|---|
|101|83|`0 ≤ Θ B q r := by` (17)|83+1+17=101>100|ok|
|102|21|none, proof follows|n/a|ok|

|#|Location|Occurrence|Rewrite|Rename|
|---|---|---|---|---|
|1|hB|1≤B|none, canonical|none|
|2|hr|∀j,0<r j|none, canonical|none|
|3|conclusion|0≤ΘBqr|none, canonical|none|
|4|entire signature|zero ≥/>|n/a|none|

## Fresh five actual mathlib searches

Raw native results `search.json`, all calls completed normally with isError=false.

|Method|Actual query and outcome|
|---|---|
|A Lean-Finder|supremum of set of nonnegative real numbers is nonnegative even empty → Real.sSup_nonneg, primed/iSup variants, sSup_empty.|
|B Loogle|`(∀ x ∈ ?s, 0 ≤ x) → 0 ≤ sSup ?s` → exact Real.sSup_nonneg.|
|C LeanSearch|supremum nonnegative real set all members nonnegative empty set → Real.sSup_nonneg, sSup_def, sSup_empty.|
|D source rg|Untruncated sSup_nonneg/sSup_empty/sSup_of_not_bddAbove in actual Mathlib/Algebra/Order/Archimedean/Real/Basic.lean; source locates all exact variants.|
|E local name|sSup_nonneg limit10 → Real.sSup_nonneg and primed variant; index=unavailable, valid source hits; no absence inference.|

Auxiliary variants: sSup_nonneg', iSup_nonneg, iSup_nonneg', sSup_empty,
sSup_of_not_bddAbove, le_csSup_of_le. Common equivalent bucket: order/supremum.
Presence is established; no absence claim. Canonical mathlib API is already used directly;
explicit public-wrapper preservation wins over generic wrapper-deletion guidance.
No missing-API extraction signal or new helper. Native full-Theta multi_attempt has repeatedly
stalled on prior leaves, so not repeated; clean target-free prefix compiler automation is used.

## Fresh every-binder drop/weakening probes

Actual ordinary commands `lake env lean /private/tmp/roth-nonneg-api/{positive,negative,automation}.lean`.
Positive exit0 (22.258s), negative expected exit1 (21.031s), automation expected exit1 (27.573s);
raw logs and `exploration-results.json` retain all output. Negative expected errors do not
certify axioms. Positive selected/weakened proofs print only standard3axioms.

|Original binder|Role|Fresh compiled probe|Decision|
|---|---|---|---|
|σ:Type*|Dependent function/index type|Literal drop with autoImplicit=false errors unknownσ; positive proofs universe-polymorphic.|Retain, already arbitrary universe.|
|Fintypeσ|Θ/index data instance|Literal drop fails synthesize Fintypeσ; Finite alternative reconstructing Fintype.ofFinite in conclusion/proof compiles.|Retain explicit selected Fintype, no restatement.|
|DecidableEqσ|Unused effective section instance|Selected proof without DecEq compiles; final actual AST confirms absence and exactly retained telescope.|Only approved omission applied.|
|B:ℝ|Bound in Θ|Literal drop errors unknownB; arbitraryB in canonical callback remains valid.|Retain data/domain/implicitness.|
|hB:1≤B|Paper's bound hypothesis|Fresh dropHB and weakHB0≤B proofs compile independently.|User expressly retained; report-only probes, no reopening.|
|q:σ→ℕ|Denominators in Θ|Literal drop errors unknownq; canonical proof handles arbitraryq.|Retain data/domain/explicitness.|
|r:σ→ℕ|Weights in Θ|Literal drop errors unknownr; canonical proof handles arbitraryr.|Retain data/domain/implicitness.|
|hr:∀j,0<rj|Paper's weight hypothesis|Fresh dropHR and weakHR0≤rj proofs compile independently.|User expressly retained; report-only probes, no reopening.|

No algebraic-class-parent weakening applies to these fixed data definitions; no global analytic
hypothesis can be point-localised. Universe already polymorphic. Finite alternative requires
data reconstruction in the conclusion and is not recommended over the explicitly selected API.
No optional API candidate is a worker blocker.

## Public literature and inversion

Fresh WebSearch queries: `supremum nonnegative real set empty supremum mathlib generalization`
and `Roth polynomial index Theta supremum nonnegative constant polynomial`.
First top3 hits: mathlib3 Real.Sup_def docs; LibreTexts Real Number System; MathWorld Supremum.
Second query was rerun alone to record its exact top3: Princeton Diophantine notes;
Vanderbilt Saff polynomial text; Thue–Siegel–Roth lecture PDF. Unrelated search noise is
excluded from inference.
Opened primary [current mathlib docs](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Real/Basic.html)
and [Princeton notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf).
The primary mathlib definition totalizes empty/unbounded real suprema to0 and provides
sSup_nonneg. Local clean.tex644–669 states positive weights, B≥1, positive denominators
and proves nonnegativity via constant1. The live result still states this paper-facing
special case. No assertion that classical real least-upper-bound theory gives an empty-set
real supremum. ChatGPT math MCP unavailable: no matching exposed tool.

Inversion fires: Θ vanishes at Real.sSup_nonneg; abstract content is the already-existing
`∀s:Setℝ,(∀x∈s,0≤x)→0≤sSup s`, supplied with index_nonneg. No new abstract theorem needed.
The extra D.hB/hr proposal remains declined; no fresh change request is made.

## All42 golfing rules and reflection

|Rule|Concrete status|
|---|---|
|1.1 by-exact|No wrapper.|
|1.2 by-rfl|No by-rfl.|
|1.3 rw/exact|No rw.|
|1.4 simp/exact|No chain.|
|1.5 trailing rfl|rfl is membership substitution pattern, no trailing tactic.|
|1.6 constructors|No constructor tactics; shared witnesses destructured together.|
|1.7 apply/exact|Apply builds quantified membership callback, exact index_nonneg alone cannot close.|
|1.8 contradiction|None.|
|1.9 eta|No eta redex.|
|1.10 have|No have.|
|1.11 apply/intro|Fresh direct pattern-lambda attempt fails dependent-rfl application type mismatch; clear rintro retained.|
|1.12 show|None.|
|1.13 projections|None.|
|1.14 merge rw|None.|
|1.15 terminal simp|None.|
|1.16 nonterminal simp|None.|
|1.17 dot notation|No eligible call in current proof.|
|1.18 parens|No redundant closing parentheses.|
|1.19 push_neg|None.|
|1.20 exists helper|No private trivial witness helper.|
|2.1 grind|Fresh grind[Θ,indexSet] fails, raw automation log.|
|2.2 pre-grind|No retained grind.|
|2.3 simpa|Fresh simp[Θ] leaves supremum nonnegativity unsolved; no consolidation chain.|
|2.4 fun_prop|n/a: no regularity goal.|
|2.5 positivity|Fresh positivity fails on project Θ.|
|2.6 gcongr|n/a: no monotonic compound expression.|
|2.7 lia/omega|n/a: arbitrary real supremum, not Nat/Int linear arithmetic.|
|2.8 aesop|Fresh aesop fails, no progress.|
|2.9 norm_num/cast|n/a: no numeric/cast subgoal.|
|2.10 decide|n/a: arbitrary real inequality, no finite computation.|
|2.11 field_simp/ring|n/a: no field identity.|
|2.12 linear_combination|n/a: no algebraic certificate/ring-ending proof.|
|2.13 wlog|n/a: no symmetric branches.|
|2.14 calc|No calc; canonical argument already selected.|
|2.15 multiple goals|One membership callback, no independent similar goals.|
|3.1 erw|None.|
|3.2 legacy regularity|None.|
|3.3 omega/lia|None, arithmetic route inapplicable.|
|3.4 rfl substitution|rintro rfl already substitutes, no subsequent simp.|
|3.5 attributes|No new normal-form automation attribute required/authorized.|
|3.6 simp_all|None.|
|3.7 limits|No production limit or profiler scaffolding introduced.|

Step-back: canonical generic supremum proof is clear and direct. Fresh exact?/apply? anonymous
examples in prefix ending BEFORE target hit conservative2000heartbeat bounds, hence inconclusive.
No imported target or failed named theorem can contaminate these searches. Fresh direct term
pattern failed, so marginal compression is not recommended. No source proof churn.
Simplify: PASS-THROUGH by direct holistic review; no duplicate skeleton, independence issue,
or missing API. Built-in Skill/simplify tool unavailable; no invocation falsely claimed.
Phase5a: selected API omission only. Phase5b: no rename, shared queue untouched.

## Verification and final evidence

Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exit0,44.879s, `module.log` and
`module-result.json`. Definitive ordinary `/Users/ramin/.elan/bin/lake env lean
/private/tmp/roth-nonneg-api/contract.lean` exit0, `contract-final.log`.
The first contract scratch invocation hit reserved `meta` parser errors in its verifier;
that failed log `contract.log` is not certification. Corrected `binderMeta` verifier ran
successfully; no production edit was required.

`contract.lean` copies immutable-baseline prerequisite proofs and the exact original
Θ_nonneg proof into ImmutableOriginal10, resolving the unchanged mathematical definitions
against actual imports. Original proof uses its own old index_le_Θ/one_mem_RSet/boundedness
proofs; it NEVER invokes current Θ_nonneg. `immutable-extracted.txt` is the exact old source
slice. Full explicit old lambda adapter accepts σ/Fintype/DecEq/B/hB/q/r/hr and invokes actual
new Θ_nonneg hB q hr. Kernel equality with independent old theorem compiles. Direct actual
getConstInfo.type checks compare old/adapter and actual/selected contracts after universe
alignment; ordinary names/order/BinderInfo verified, anonymous instance names exempt only
from generated-name equality. Actual old8→selected7 binder metadata matches precisely after
dropping old position2 DecEq. Actual selected AST rejects DecEq and requires protected data/
hypothesis names, with exact selected type independently declared. Fintype remains.

Actual built theorem, independent original, full old adapter, selected-contract theorem and
both caller-shape proofs each print exactly propext/Classical.choice/Quot.sound. Explicit
adapter printed in log. Actual width100 check:

```lean
@Roth.Θ_nonneg : ∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ},
  1 ≤ B → ∀ (q : σ → ℕ) {r : σ → ℕ}, (∀ (j : σ), 0 < r j) → 0 ≤ Roth.Θ B q r
```

Repository-wide Lean rg finds exactly4actual calls, two in index_le_lem6 and two in Θ_lt,
plus declaration/module-doc mention; zero external use. Both complete existing add_nonneg
call shapes compile in contract.lean against actual imported lem6Φ and new actual theorem,
without DecEq. No argument deletion or caller edits; D's prior prospective fixes do not apply.
Whole module build also checks the actual existing callers.

Fresh COMPLETE unfiltered native lean_diagnostic_messages on live Roth/Theta.lean returned
normally: success=true,partial=false,timed_out=false,failed_dependencies=[],0errors25warnings;
raw `final-lsp.json`. Baseline27→final25 removes the target's two DecEq warnings. Its protected
hB/hr warnings remain; all remaining diagnostics are recorded unfiltered, no suppression.
Only new syntax is built-in omit; no new mathematical identifier requires discovery.
Focused byte comparison proves exact one-line insertion and all other source bytes identical;
`focused.diff` and `scope-metrics.json`. No def/import/helper/comment/ordinary signature/caller
change; no sorry/axiom/native_decide/limit raise/profiler scaffolding. No proof comment existed,
original docstring exact. Source lines +1; declaration/proof body remain5/3lines.

## Eleven worker gates

|Gate|Result|Concrete evidence|
|---|---|---|
|lake_build_file|pass|Actual lake build Roth.Theta exit0,44.879s, module.log.|
|definition_protected|pass|Sole omit insertion, no definition/import/value change.|
|theorem_statement_protected|pass, approved amendment|Exactly A.DecEq omission; actual selected type/metadata and full immutable original adapter PASS.|
|structure_gate|pass|Headline body3≤15, no conjunction or long branch.|
|naming_gate|pass|Θ_nonneg names established object's property, no forbidden scheme/abbreviation.|
|line_packing_gate|pass|Both signature rows measured,101overflow justifies break.|
|inequality_orientation_gate|pass|hB/hr/conclusion canonical, zero ≥/>.|
|diagnostics|pass|Fresh complete unfiltered normal native return0errors25warnings; target DecEq warnings removed, explicit hB/hr retained.|
|trust_basis|pass|Actual built/independent old/adapter/selected/callers standard3axioms.|
|comments_scope_callers|pass|Exact protected docstring/zero proof comments removed; sole insertion, all four actual calls unchanged and checked.|
|performance|pass, prefix-only|Before15.233ms/final14.808ms inclusive non-double-counted aggregates below.|

Worker gates pass. Owner final full project build THEN separate Roth.LeanEval and publication
are pending; this report does not claim they have run for this new checkpoint. No outside
Θ_nonneg callers exist; owner's separate external MainLemma contract probe is additional
cumulative-file evidence, not this leaf's own result.

## Buzz — FAST-BOARD, exact-prefix only

After module, all exploration/contract compilers and the COMPLETE final native LSP request
returned normally and were drained, ran sequential uncontended exact source-prefix commands:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 /private/tmp/roth-nonneg-api/{before,final}-prefix.lean`.
Both exit0,45.162s/43.210s command wall time; per-declaration timings below. Each prefix
contains all exact preceding imports/source/context and ends just after target, then end Roth.
Exact final prefix matches frozen live source through target. No source profiling scaffolding.

|State|Outer command|Top async proof|Top async addDecl/kernel|Top async linter|Aggregate|
|---|---:|---:|---:|---:|---:|
|before|2.986ms|5.151ms|2.227ms|4.869ms|15.233ms|
|final|3.909ms|4.785ms|1.674ms|4.440ms|14.808ms|

RawUTF8 before-profile.log/final-profile.log, profile-results.json, profile-summary.json.
Actual declaration outer anchors80862/81399. Final counts the OUTER omit wrapper (3.909ms),
not its nested inner theorem command (3.394ms), then precisely associated top-level async
proof/addDecl/linter until next outer command. Inner tactic/Meta/kernel trace nodes not added
again. Both safely below750ms repeat threshold/1000ms budget; difference is ordinary noise,
no speedup claim. No limit raise. Whole-Theta profiling's known later index_le_lem6 default-
heartbeat issue is outside this leaf; prefix results do not assert whole-file profiling pass.
Buzz executed directly because separate Skill invocation is unavailable. No new helper audit.

## Eleven-step phase checklist

- [✓] Step1 full mandatory references/required workflow read.
- [✓] Step2 complete substantive24audit printed.
- [✓] Step2.5 five fresh actual search methods, auxiliary variants/common-equivalents.
- [✓] Step2.6 every effective original binder freshly probed; public literature/inversion.
- [✓] Step2.7 both signature lines measured with codepoint arithmetic.
- [✓] Step2.8 per-occurrence inequality table.
- [✓] Step3 all42golfing statuses, applicable fresh automation trials.
- [✓] Step4 independent reflection/direct holistic simplify.
- [✓] Step5a fresh complete unfiltered final native diagnostics normal return.
- [✓] Step5b focused scope/actual metadata/immutable original/module/axiom/performance gates.
- [✓] Step6a no rename needed, shared queue untouched.

## Final freeze and drain

Source SHA256 `ae461a2a0c0844e362bef13a87f8beee65882f94beee558ba64ec87bd6f0928f`.
Final exact comparison again confirms sole omit insertion before preserved docstring, all other
source bytes identical to released r09 snapshot. Source editing authority is frozen/revoked.
All native/search/compiler/module/profile calls are complete and all terminal sessions drained;
no further worker source edits, compiler/LSP/profile requests. Owner gates may begin.
No Git/shared report/queue mutation; only allowed dedicated report written. Total source delta+1,
proof unchanged3lines; no original-count increment. No pending optional API question.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 54.394 s and 17.121 s.
Theta SHA256 `ae461a2a0c0844e362bef13a87f8beee65882f94beee558ba64ec87bd6f0928f` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-r10-full.log` and `/private/tmp/roth-theta-r10-leaneval.log`; machine record
`/private/tmp/roth-theta-r10-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this approved revisit before the next source edit. This revisits original 10; original counts
remain Theta 15/35, overall 196/264, 9/14 files. No new original or helper is counted.
