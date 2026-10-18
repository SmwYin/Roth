# Approved revisit of original 11 — `Roth.Θ_le_card`

Exact selected scope: menu A removes `DecidableEq σ`; menu C removes `hr : ∀ j, 0 < r j`.
`hB : 1 ≤ B` is deliberately RETAINED under the user's explicit decision declining E's extra
widening. `Fintype σ`, σ/B/q/implicit r, all retained names/types/order/BinderInfo, conclusion,
visibility and original docstring are retained. No caller/helper/import/definition/Git/shared
sidecar changes. This revisit adds no original-declaration count: Theta15/35, overall196/264.

## Preparation and baseline

Read the leaf instructions, complete lean4/mathlib-quality skills and cleanup workflow;
full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates;
relevant style, naming and full profiling reference; prior original11 report and exact contract
proposal decision. Original proof source is immutable commit
`2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`.
Read-only preparation made no writes/compiler/LSP/search/profile starts before explicit RELEASE.
Owner's r10 checkpoint `adaa87542f06102a2ef0364d63df2a817aff712f` was clean/pushed before RELEASE:
full build54.394s THEN separate LeanEval17.121s, both0 with source/config snapshots stable.
Start SHA256 `ae461a2a0c0844e362bef13a87f8beee65882f94beee558ba64ec87bd6f0928f`.
Identical-hash baseline complete LSP reused from `/private/tmp/roth-nonneg-api/final-lsp.json`:
success=true,partial=false,timed_out=false,failed_dependencies=[],0errors25warnings.

Single-declaration mode: file-wide phases belong to owner. Scope snapshot and exact focused diff
are `/private/tmp/roth-card-api/{before.lean,focused.diff,scope-metrics.json}`. Source read afresh
immediately before each narrow contextual patch. Five-line proof byte-identical; two-line signature
packed into one95-codepoint line plus one `omit` line. File980→980physical lines.

## Full substantive 24-item audit

|#|Item|Concrete finding/action|
|---|---|---|
|1|LINT|Approved DecEq/hr unused warnings removed by exact selected API removal. hB unused remains deliberately protected by explicit user choice; no suppression/underscore renaming. Final complete diagnostics recorded below.|
|2|HAVE SCAN|No have in target before/after; no single-use intermediate to inline.|
|3|SET_OPTION|No target option. No source limit raise. Only scratch automation has lowered2000heartbeats.|
|4|SIMP SQUEEZE|One terminal simpa for mapped degree; existing explicit degreeOf/degrees_map normalization appropriate. No nonterminal bare simp or terminal simp-only.|
|5|NAMING|Θ_le_card says upper bound by cardinality of established Θ. No forbidden abbreviation, numeric scheme, multipass, numbered aux, or single-letter theorem. No rename.|
|6|LINE PACKING|Shortened signature fits95codepoints on one line; measured table below.|
|7|BY PLACEMENT|by at end of95-codepoint signature line.|
|8|FORMAT|2-space proof/4-space continuation, no internal blank line, no haveI/letI.|
|9|COMMENTS|Zero original target proof comments; original source-bearing docstring byte-identical.|
|10|DOCSTRING|Accurate cardinal bound and source citation preserved.|
|11|VISIBILITY|Public headline theorem in module main-results retained despite zero actual callers.|
|12|STRUCTURE|Headline body5lines≤15, no conjunction conclusion/branch>10. Correlated R/h witnesses unpacked together.|
|13|MATHLIB|Fresh5methods below confirm Real.sSup_le is generic infrastructure; direct project-specific callback retained, no wrapper/helper.|
|14|JUNK DEF|n/a: theorem.|
|15|EXISTS LEMMA|n/a: public inequality, no private existential wrapper.|
|16|SHOW/CHANGE|None.|
|17|PUSH_NEG|None.|
|18|GENERALISE|All8original effective binders probed; approved DecEq/hr removals applied, hB preserved by explicit decision. Table below.|
|19|INEQUALITY|hB1≤B and conclusionΘ≤card already smaller-side-left; hr positive hypothesis removed exactly as approved.|
|20|NORMAL FORM|Direct real supremum upper-bound form canonical; no attribute change.|
|21|SYNTAX-GEN|Exact selected6binder API compiles; no extra widening/reordering/bundling recommended or applied.|
|22|IMPORT FANOUT|n/a: no new import.|
|23|CASTS|No proof change/new casts. Nat.cast_nonneg is genuine ℕ→ℝ bridge; Int.castRingHom ℝ fixes map codomain.|
|24|INSTANCE-NAME|n/a: no instance declaration/name introduced. Anonymous synthetic binder names exempt only from name equality, exact class/type/order/BinderInfo still checked.|

## Measured signature packing and inequality scan

Actual `#check @Roth.Θ_le_card` at format.width100 is in `positive.log`:
`∀ {σ : Type u} [Fintype σ] {B : ℝ}, 1 ≤ B → ∀ (q : σ → ℕ) {r : σ → ℕ},
Roth.Θ B q r ≤ ↑(Fintype.card σ)`.

|Signature line|Codepoints|Next complete signature token|Arithmetic|Action|
|---|---:|---|---|---|
|109|95|none; proof next|n/a, entire signature fits≤100|ok|

Before shortening, conclusion would overflow original header:84+1+30=115>100.
After approved hr deletion, complete signature95≤100, so repack applied.

|#|Location|Occurrence|Rewrite|Rename|
|---|---|---|---|---|
|1|hB|1≤B|none; canonical and retained|none|
|2|conclusion|ΘBqr≤cardσ|none; canonical|none|
|3|whole final signature|zero ≥ or > relations; → is function syntax|n/a|none|

## Five fresh actual mathlib searches

Native raw results `/private/tmp/roth-card-api/search.json`; all4native calls completed successfully.

|Method|Query/result|
|---|---|
|A Lean-Finder|A real supremum is at most any nonnegative upper bound including empty set → Real.sSup_le, Real.iSup_le, Real.sSup_nonneg'.|
|B Loogle|sSup ?s ≤ ?a → sSup_le, sSup_le_iff, sSup_le_sSup; generic complete-semiltattice assumptions differ from real conditional completeness.|
|C LeanSearch|real supremum less than or equal to nonnegative bound for every set element → Real.iSup_le, Real.sSup_le, csSup_le_iff'.|
|D source rg|Untruncated sSup_le/csSup_le/sSup_empty in real Basic and conditional-complete Basic; Real.sSup_le source222–224 inspected; degreeOf/degrees_map source inspected.|
|E local names|sSup_le limit12 → Real.sSup_le and generic variants. index unavailable; source presence valid, absence not inferred.|

Auxiliary variants: Real.iSup_le, csSup_le, csSup_le_iff, sSup_le_iff, Real.sSup_empty,
Real.sSup_of_not_bddAbove. Common-equivalent bucket: supremum/order. Generic upper-bound
infrastructure found and already used directly; concrete index-polynomial bound remains local.
No mathlib absence claim. No deleted wrapper recreated. No new identifier introduced.

Target-free anonymous automation is `/private/tmp/roth-card-api/trials.lean`: exact source
prefix ends BEFORE target and all later theorems; separate anonymous examples for grind[Θ,indexSet],
simp[Θ], aesop, gcongr, exact?, apply?, with conservative lowered2000heartbeats.
Full-Theta native multi_attempt was not repeated after known consecutive earlier stalls; ordinary
bounded compiler exploration used. Final outcomes recorded below; expected-failure batch never
certifies trust or absence. No self-target/failed-named-declaration contamination.

## Every original effective binder — compiled drop/weakening probes

Positive `/private/tmp/roth-card-api/positive.lean` compiles separately with exit0.
Negative `/private/tmp/roth-card-api/negative.lean` exits1 as expected, autoImplicit=false.

|Binder|Use/class|Fresh compiled evidence|Decision|
|---|---|---|---|
|σ:Type*|Index type in functions/Θ/card|Literal removal errors unknownσ; positive arbitrary-universe original/candidate/actual contracts compile.|Retain already-polymorphic type.|
|Fintypeσ|Θ/index/card depend on finite enumeration|Literal drop fails Fintype synthesis; Finiteσ reconstruction via Fintype.ofFinite in conclusion/proof compiles.|Retain Fintype; reconstructed public restatement unnecessary.|
|DecidableEqσ|Old section instance, unused by canonical proof|drop_decEq and actual new API compile; actual AST rejects any DecEq binder.|Approved A removal applied.|
|B:ℝ|Bound in Θ|Literal drop errors unknownB; candidate arbitrary real B compiles.|Retain dependent data; abstract codomain changes definitions.|
|hB:1≤B|Old nonempty route, unused by Real.sSup_le|Original-style literal drop errors unknownhB; drop_hB/weak_hB0≤B canonical variants compile.|RETAIN under user's explicit decline; audit evidence does not reopen decision.|
|q:σ→ℕ|Denominator data in Θ|Literal drop errors unknownq; arbitrary q positive proofs compile.|Retain dependent data.|
|r:σ→ℕ|Degree/weight data in Θ|Literal drop errors unknownr; arbitrary r canonical proof compiles.|Retain implicit dependent data.|
|hr:∀j,0<rj|Unused original/card callback|drop_hr and weak_hr0≤rj canonical variants compile, simultaneous actual selected API compiles.|Approved C removal applied.|

Catalogue parent-class/point-local hypotheses absent; strict→weak possibilities hB/hr explicitly
probed. No algebraic-codomain generalization is possible within unchanged concrete definitions.
Old degreeOf_def route without decidability fails mapped-degree simplification; degreeOf unfolding
already provides the valid canonical proof. Broader no-hB candidate is isolated audit evidence,
not a renewed recommendation or live amendment.

## Public literature and mandatory inversion check

Local `clean.tex644–669` defines the polynomial family with positive weights and B≥1, then
bounds the index by variable count using a nonzero Taylor derivative of bounded weight.
Fresh WebSearch queries: “Roth theorem polynomial index number of variables upper bound Taylor
generalization” and “mathlib Real.sSup_le real supremum empty set nonnegative upper bound”.
Roth query top relevant hits: Wikipedia Roth overview, Roth's1958ICM proceedings, Chen's Roth
biography (mixed with unrelated nonlinear-Roth search noise). Supremum query first3hits:
mathlib3 real.Sup_def, gebner mathlib docs, teorth analysis mathlib docs.
Primary [mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Real/Basic.html)
opened successfully; real supremum defaults to zero on empty sets and Real.sSup_le accepts a
nonnegative bound. [Roth's proceedings](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf)
open returned internal error; no unseen content inferred. The concrete mathematical formulation
comes from checked local clean.tex, the API claim from primary mathlib source/docs. No exposed
ChatGPT mathematics MCP available. Search availability/failure is not absence evidence.

Inversion fires: Θ disappears after Real.sSup_le; abstract statement is
`∀s:Setℝ,∀a:ℝ,(∀x∈s,x≤a)→0≤a→sSup s≤a`, exactly existing Real.sSup_le.
A separate generic example compiles. Concrete callback needs project index_le_card and
injective integer-map degree preservation. No missing abstract helper/API or useful extraction.

## All 42 golfing rules

|Rule|Concrete status|
|---|---|
|1.1 by-exact|No wrapper; proof has substantive tactics.|
|1.2 by-rfl|None.|
|1.3 rw/exact|No rw chain.|
|1.4 simp/exact|Mapped-degree terminal simpa already combines normalization and hRd.|
|1.5 trailing rfl|None; membership rfl pattern needed for substitution.|
|1.6 constructors|No constructor tactics; correlated witnesses unpacked together.|
|1.7 apply/exact|refine supplies callback/nonnegative bound; direct index_le_card cannot alone prove supremum goal.|
|1.8 contradiction|None.|
|1.9 eta|No eta-redex.|
|1.10 single-use have|None.|
|1.11 apply/intro|No separate chain; direct rintro membership unpacking.|
|1.12 show|None.|
|1.13 projections|No have/projection pair.|
|1.14 merge rw|None.|
|1.15 terminal simp|No simp-only; simpa explicitly names domain-specific normalization.|
|1.16 nonterminal simp|None.|
|1.17 dot notation|Existing .2 hR0 suitable, no useful change.|
|1.18 parentheses|Degree-proof parentheses precede another positional argument; <| would consume it.|
|1.19 push_neg|None.|
|1.20 exists helper|None.|
|2.1 grind|Fresh target-free whole-proof trial below.|
|2.2 delete before grind|No retained grind.|
|2.3 simpa|Canonical degreeOf mapped-degree simplification retained and compiled.|
|2.4 fun_prop|n/a: no regularity target.|
|2.5 positivity|Nat.cast_nonneg is direct canonical auxiliary nonnegativity; overall upper bound not positivity goal.|
|2.6 gcongr|Fresh target-free whole-proof trial below.|
|2.7 lia/omega|n/a: no Nat/Int arithmetic goal.|
|2.8 aesop|Fresh target-free whole-proof trial below.|
|2.9 norm_num/cast|No concrete computation; direct Nat.cast_nonneg handles genuine cast.|
|2.10 decide|n/a: arbitrary real inequality, no finite computation.|
|2.11 field/ring|n/a: no algebraic identity.|
|2.12 linear_combination|n/a: no ring-ending proof/hypothesis certificate.|
|2.13 wlog|n/a: no symmetric cases.|
|2.14 calc|None.|
|2.15 multiple goals|Callback and nonnegative bound are distinct obligations, no repeated goal.|
|3.1 erw|None.|
|3.2 continuity|None.|
|3.3 omega/lia|None, rule2.7 inapplicable.|
|3.4 rfl substitution|rintro rfl substitutes directly; no redundant rewrite.|
|3.5 attributes|No new automation normal form justified.|
|3.6 simp_all|None.|
|3.7 limits|No live source limit to remove/raise.|

Step-back/simplify: canonical Real.sSup_le already separates the generic supremum from the
polynomial callback clearly. Single-tactic generic automation does not supply the substantive
index bound. No long independent branch, duplicate local plumbing, or missing API found.
Direct holistic simplify outcome PASS-THROUGH; no additional files changed. Built-in Skill tool
is unavailable, so direct review is not misattributed to a tool invocation. Phase5a no new
refactor; exact approved API scope only. Phase5b no rename required/queued, sidecar untouched.

## Completed normal verification and 11 gates

Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exited0 (2423jobs), raw
`/private/tmp/roth-card-api/module.log`. Then actual `lake env lean positive.lean` exited0:
independent immutable original definitions/prerequisites/private wrappers/four-line target proof
copied from baseline into OriginalCard11, never invoking current Roth.Θ_le_card as its proof.
`ApprovedCard11.oldAdapter` explicitly takes original8binders and invokes actual new6theorem:

```lean
fun {σ} [Fintype σ] [DecidableEq σ] {B} hB q {r} hr ↦ Roth.Θ_le_card hB q
```

Its type aligns by direct getConstInfo.type defeq with the independent original, and proof
kernel equality rfl also passes. Separate expected selectedContract checks actual new type,
retained names/order/BinderInfo and exact six-binder AST σ/Fintype/B/hB/q/r. Deletion metadata
checks original positions2(DecEq) and7(hr) precisely, no other binder. Every data/hypothesis type
and conclusion checked through actual expected full type, universes aligned. Anonymous generated
instance names alone are exempt from name equality; ordinary names exact. Actual Fintype AST
class checked; DecEq/hr rejected. Actual built theorem, independent original, full-old adapter,
expected selected contract, canonical candidate, Finite reconstruction, named/inferred/old-shape
caller trials all checked programmatically for axioms ⊆{propext,Classical.choice,Quot.sound}.
`positive.log` includes exact adapter term and every PASS line.

Fresh anonymous automation compiler exits1 as expected. grind[Θ,indexSet], simp[Θ], aesop and
gcongr fail; exact?/apply? hit lowered2000heartbeats, inconclusive. `trials.log` preserves all
errors. Binder negative compiler exits1 with unknownσ/B/q/r/hB and Fintype synthesis failures;
old degreeOf_def route fails as expected. Expected-error examples are not trust evidence.
All normal compiler sessions closed; no failed scratch artifact used as successful certification.

Fresh live native lean_goal110 confirms actual six-binder context and transition Θ≤card→
∀x∈indexSet,x≤card, raw `goal.json`. Fresh COMPLETE unfiltered live native final diagnostics,
raw `/private/tmp/roth-card-api/final-lsp.json`: success=true,partial=false,timed_out=false,
failed_dependencies=[],0errors22warnings. Baseline25→22 removes precisely target DecEq-unused,
DecEq-in-type and hr-unused. Target's hB-unused remains under explicit preservation; all other
warnings inherited/outside this leaf. No linter suppression. No source edit follows diagnostics.
Every search/normal compiler/native request fully awaited and drained BEFORE real profiling.

Fresh repository-wide `rg -n Θ_le_card --glob '*.lean' --glob '!**/.lake/**' .` finds only
module-doc27/declaration109, zero actual internal/external callers; no caller correction needed.
Exact before/final scope comparison establishes all other source unchanged, five proof lines
identical, docstring identical and no comments removed. No sorry/newaxiom/native_decide/newhelper,
source option/limit increase or profiling scaffold. No introduced proof identifier to verify.

|Gate|Result|Concrete evidence|
|---|---|---|
|1 lake_build_file|pass|Actual lake build Roth.Theta exit0, module.log.|
|2 definition_protected|pass|No def/abbrev/import mutation, exact scope comparison.|
|3 theorem_statement_protected|pass approved amendment|Only A.DecEq/C.hr removed, expected actual6 type/metadata and independent old8adapter pass; hB preserved.|
|4 structure_gate|pass|Headline body5≤15, no conjunction/long branch.|
|5 naming_gate|pass|Descriptive Θ_le_card, no forbidden name.|
|6 line_packing_gate|pass|Entire final signature95codepoints, table above.|
|7 inequality_orientation_gate|pass|Two retained inequalities canonical, no ≥/>.|
|8 diagnostics|pass|Fresh complete unfiltered0errors22warnings; target hB protected.|
|9 trust_basis|pass|Actual built/independent original/fullold adapter/candidates/callers only3standardaxioms.|
|10 comments_and_scope|pass|Source outside exact target unchanged; doc/proof byte-identical; no helper/caller/Git mutation.|
|11 performance|recorded below|Real sequential exact-prefix traces, full outer+associated top-level async aggregation.|

Owner full `lake build` THEN separate `lake build Roth.LeanEval` remain pending for this revisit;
not run or claimed by leaf. Whole-Theta profile/default-heartbeat frontier remains owner work.

## Buzz — FAST-BOARD, exact-source-prefix only

After normal/compiler/native/search requests were fully drained, sequential uncontended commands:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 /private/tmp/roth-card-api/before-prefix.lean`, then identical command
on `final-prefix.lean`. Both exited0. Prefixes preserve every exact preceding import/context/source
through target, append only end Roth. Source final unchanged throughout. Real Lean4.34 profiler
flags used, correcting obsolete -Dprofiler=true-only reference. No overlapping compiler/LSP calls.

|Target|Outer command|Top async proof|Top async addDecl/kernel|Top async linter|Aggregate|
|---|---:|---:|---:|---:|---:|
|before|4.905ms|133.339ms|3.868ms|5.409ms|147.521ms|
|final|3.749ms|136.319ms|3.017ms|4.928ms|148.013ms|

RawUTF8 `before-profile.log` and `final-profile.log`; structured exact counted anchors
`profile-summary.json`. Before outer81776/proof82477/addDecl119698/linter119712; final **outer
omit82405**/proof82416/addDecl119585/linter119593. Final outer macro command used, not the
nested inner doc/theorem command. Associated top-level async addDecl includes kernel replay;
nested tactic/Meta/Kernel nodes not double-counted. No separate target compiler root event.
Both aggregates<750ms and<1000msbudget, no borderline repeat required. Difference is ordinary
run noise, no speedup claim. No source limits/scaffolding added. No performance deferral for
this target; whole-Theta late index_le_lem6 heartbeat/profile frontier still owner's obligation.
No whole-file successful profile claimed. Workflow run directly; no unavailable Skill invocation.

## Eleven-step phase checklist

- [✓] Step1 required references read, exact decision and prior report/immutable baseline inspected.
- [✓] Step2 full24audit above, concrete applicability/action for every item.
- [✓] Step2.5 all5fresh actual mathlib search methods plus variants, raw results saved.
- [✓] Step2.6 every8original effective binder compiled probes, literature and inversion checked.
- [✓] Step2.7 complete measured signature packing table, single95-codepoint line.
- [✓] Step2.8 every retained inequality canonical, per-occurrence table.
- [✓] Step3 all42golf rules concrete status; relevant bounded target-free automation executed.
- [✓] Step4 independent step-back/direct holistic simplify PASS-THROUGH.
- [✓] Step5a fresh COMPLETE unfiltered native final0errors22warnings.
- [✓] Step5b module/scope/actualtype/independent oldproof/explicitfulloldadapter/axiom/performance gates.
- [✓] Step6a no rename required or queued; shared sidecars/Git untouched by leaf.

## Final freeze and handoff

Final `Roth/Theta.lean` SHA256
`38993bdc67cd88792ffa89a59640081c117d6ad7e0bbcf03d7cb801d0592ef3d`.
Immutable source extraction cross-check `/private/tmp/roth-card-api/immutable-original-check.json`
confirms independent original prefix byte-for-byte against immutable baseline modulo namespace
and import. Exact old8proof→fulloldlambda→actualnew6 telescope/type/ordinarynames/order/BinderInfo,
precise two removed binders, retained hB/Fintype and all actual standard-axiom checks pass.
Only target signature and scoped omit changed; five-line proof/docstring and other source identical.
No actual caller exists. Report and permitted target are the only project paths written by leaf;
any parent shared-progress changes are outside this leaf's writes.

All search/native/compiler/module/profile requests awaited and drained; every terminal session
closed normally. Source editing authority frozen/revoked. No source/compiler/LSP/profile request
will follow this handoff. Parent owns frozen sequential full project THEN separate LeanEval gates,
commit/push and shared ledger; those final owner gates remain pending here. Counts unchanged.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 65.268 s and 23.107 s.
Theta SHA256 `38993bdc67cd88792ffa89a59640081c117d6ad7e0bbcf03d7cb801d0592ef3d` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-r11-full.log` and `/private/tmp/roth-theta-r11-leaneval.log`; machine record
`/private/tmp/roth-theta-r11-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this approved revisit before the next source edit. This revisits original 11; original counts
remain Theta 15/35, overall 196/264, 9/14 files. No new original or helper is counted.
