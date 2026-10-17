# Cleanup: private `Roth.mapDomain_add_single_none`

Dedicated original d04 worker, owner-supplied HEAD aca2c7b. No Git operations. Scope: only this private helper and two exact use substitutions in Roth/Separation.lean. Start snapshot: `/private/tmp/roth-separation-d04-start.lean`; ORIGINAL snapshot: `/private/tmp/roth-separation-original.lean`. Parent supplied baseline module/full/separate LeanEval success and complete native LSP 0 errors/32 warnings. Public instance proposal remains pending; nothing from it applied.

Read both installed SKILL.md files, full cleanup command, golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, relevant style and naming references. No subdelegation. I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md.

## Full audit (24 items)

| # | Item | Finding/action |
|---|---|---|
|1|LINT|No target warning; baseline 32 warnings outside target.|
|2|HAVE SCAN|No have, no use counts to reduce.|
|3|SET_OPTION|No scoped options or limit raises.|
|4|SIMP SQUEEZE|Sole simp is terminal; unsqueezed library simp retained at use sites.|
|5|NAMING|Name describes mapDomain/add/single/none; no forbidden pattern or abbreviation. Removal supersedes suffix considerations; no rename.|
|6|LINE PACKING|Every original signature line measured below. Final target removed.|
|7|BY PLACEMENT|by ends conclusion line; inline replacement uses term-mode show ... by.|
|8|FORMAT|Two-space proof indent, no empty interior lines/trailing whitespace/haveI/letI.|
|9|COMMENTS|No target comments; all existing block comments preserved byte-for-byte.|
|10|DOCSTRING|Private helper has none; existing public docs unchanged.|
|11|VISIBILITY|Private, exactly two uses in this file; delete redundant wrapper.|
|12|STRUCTURE|One-line proof, no conjunction/branches; no extraction/decomposition.|
|13|MATHLIB|Generic mapDomain_of_notMem_range plus simp provides whole result. Delete, inline at two uses.|
|14|JUNK DEF|n/a: lemma.|
|15|EXISTS LEMMA|n/a: equality.|
|16|SHOW vs CHANGE|No original show. New show is a term argument with tactic proof, not tactic-mode goal change.|
|17|PUSH_NEG|None.|
|18|GENERALISE|All effective binders individually probed; generic coefficient AddCommMonoid candidate compiles; existing library API supplies it, no new helper.|
|19|INEQUALITY|No ≥/> in signature, hypotheses or name.|
|20|NORMAL-FORM|Evaluation outside range is zero, then zero_add; existing library canonical form.|
|21|SYNTAX-GEN|Generic library theorem already supports arbitrary maps/monoids/off-range points.|
|22|IMPORT-FANOUT|No imports added.|
|23|CASTS|Two replacement Option τ →₀ ℕ ascriptions are load-bearing: dropping them produced unknown application/metavariable rewrite errors. 0 dropped, 0 cross-type, 2 load-bearing kept.|
|24|INSTANCE-NAME|n/a: no instance.|

Issue/action: delete one-call simp wrapper with two local substitutions. No public type, definition, docstring, import, pin or mathematical meaning change. No rename queue or other declaration cleanup.

## Five actual search methods

| Method | Query/action | Finding |
|---|---|---|
|A Lean-Finder|Finsupp mapDomain some evaluates at none zero|embDomain_some_none, some_apply, some_single_none.|
|B Loogle|Finsupp.mapDomain, _ = 0|mapDomain_of_notMem_range and image-support/zero variants.|
|C LeanSearch|finitely supported function mapDomain is zero outside the range|off-range generic theorem (deprecated alias returned), range-characterisation theorem.|
|D source|mapDomain.*none, mapDomain_of_notMem_range, mapDomain.*apply in Basic/Option|Basic:286 exact generic API; Basic:270,273 evaluation; direct source read verified signature and deprecated alias.|
|E local name|Finsupp.mapDomain limit40|mapDomain family including off-range alias; warming index means no absence inference.|

Auxiliary variants inspected: mapDomain_of_not_mem_image_support, mapDomain_apply_of_injective, embDomain_some_none, mapDomain_equiv_apply; deprecated alias not used. Common-equivalents table has no special Finsupp bucket. Conclusion: composition of existing generic library API, delete wrapper and use library directly. No absence claim.

## Generalisation: every binder and individual probes

| Binder | Class/use | Candidate and verified result |
|---|---|---|
|{τ : Type*}|Universe-polymorphic type, Finsupp domain|Already universe-polymorphic; individual drop with autoImplicit false fails unknown τ. Sort not admissible Finsupp domain.|
|(d : τ →₀ ℕ)|Structure value being evaluated|Individual drop fails unknown d.mapDomain. Generalise coefficients to arbitrary M with AddCommMonoid M: independent native run_code success.|
|(ν : ℕ)|Value at none|Individual drop fails unknown ν; same generic-M candidate succeeds.|
|[Fintype τ]|Already omitted section instance|Effective type lacks it; independent theorem without it compiles.|
|[DecidableEq τ]|Already omitted section instance|Effective type lacks it; independent theorem without it compiles.|
|{R}, [CommSemiring R]|Unused section variables, absent from effective type|Independent theorem has neither and compiles.|

Individual native drop probes ran separately (not combined), with autoImplicit false. Native run_code checked exact original mathematical type and the generic AddCommMonoid coefficient version. No propositional hypotheses exist: point-localisation, strict-to-weak and bundled-hypothesis decomposition do not apply. Inversion check identifies generic library off-range API; deletion is preferable to exporting another version. Literature search: n/a: private decl, literature search not required. No public generalisation applied.

## Line-packing table

Independent width100 #check:

```lean
@independent : ∀ {τ : Type u_1} (d : τ →₀ ℕ) (ν : ℕ), (Finsupp.mapDomain some d + Finsupp.single none ν) none = ν
```

| Original signature line | Codepoints | Next complete syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
|57|62|Conclusion (73 chars excluding four-space indentation)|62 + 1 + 73 = 136 > 100|ok|
|58|77|none; proof body next|n/a|ok|
|Final target|deleted|none|n/a|ok|

Original scoped omit L56 is 35 codepoints; proof L59 is42. Added caller lines measure46,79,65 and39,79,65, all ≤100. Public caller signatures remain byte-identical.

## Inequality scan

| Location | Original | Rewrite | Rename |
|---|---|---|---|
|Whole signature/all hypotheses|n/a: no ≥ or >|none|none|

## Every golfing rule (42)

| Rule | Status |
|---|---|
|1.1 by exact|n/a: terminal simp.|
|1.2 by rfl|rfl tried live, fails definitional equality.|
|1.3 rw+exact|n/a: no such sequence.|
|1.4 simp+exact|n/a: simp closes.|
|1.5 trailing rfl|n/a: none.|
|1.6 constructor|n/a: equality/no constructor.|
|1.7 apply+exact|n/a: neither.|
|1.8 contradiction|n/a: none.|
|1.9 eta|n/a: no lambda.|
|1.10 have|n/a: none.|
|1.11 apply+intro|n/a: neither.|
|1.12 redundant show|n/a original; replacement show is load-bearing term type.|
|1.13 projections|n/a: no have.|
|1.14 merge rw|n/a original; caller existing rewrite sequence kept.|
|1.15 terminal simp only|n/a: simp already unsqueezed.|
|1.16 nonterminal simp|n/a: simp closes equality subproof.|
|1.17 dot notation|n/a: no useful receiver form.|
|1.18 trailing parentheses|n/a: library name in simp list.|
|1.19 push_neg|n/a: none.|
|1.20 existential inline|n/a: not existential; redundant equality wrapper removed per mathlib rules.|
|2.1 grind|Live trial failed; simp with off-range API succeeds.|
|2.2 pre-grind deletion|n/a: no retained grind.|
|2.3 simpa consolidation|n/a: no following closing tactic.|
|2.4 fun_prop|n/a: no function property.|
|2.5 positivity|n/a: equality, no positive/nonnegative/nonzero goal.|
|2.6 gcongr|n/a: no inequality or monotonicity.|
|2.7 lia/omega|n/a: uninterpreted Finsupp evaluation, no arithmetic relation assumptions.|
|2.8 aesop|Live trial failed, leaves mapDomain none=0.|
|2.9 norm_num/norm_cast|n/a: symbolic evaluation, no numeric/cast subgoal.|
|2.10 decide|n/a: unbounded symbolic data, no finite proposition computation.|
|2.11 field_simp/ring|n/a: no field/division.|
|2.12 linear_combination|n/a: no ring-ending proof/hypotheses.|
|2.13 wlog|n/a: no branches.|
|2.14 calc term|n/a: no calc.|
|2.15 multiple goals|n/a: one goal.|
|3.1 erw|n/a: none.|
|3.2 legacy fun_prop|n/a: none.|
|3.3 omega→lia|n/a: none in owned target/substitutions.|
|3.4 rcases rfl|n/a: none.|
|3.5 automation attributes|n/a: deleted private wrapper; generic API used directly.|
|3.6 simp_all|n/a: none.|
|3.7 maxHeartbeats|n/a: no raised limit.|

## Step back / simplify review

Bare simp leaves mapDomain some d none=0; rfl, grind, aesop and exact? fail. apply? gives only partial suggestions and its discarded experiment emitted sorry, which is not an accepted proof. Existing simp with generic API closes immediately. Initial attempt to unfold Finsupp.add_apply directly inside simp_rw caused dependent-if transparency/type errors and underconstrained off-range proof; discarded completely. Explicit inline equality proof with terminal simp replaces the wrapper safely. Its Option-Finsupp type ascription is required by elaboration. Holistic reuse/quality/efficiency review: PASS-THROUGH after deletion; no extra helper/API and no comments lost. Built-in simplify callable unavailable; review performed directly, not claimed as a tool invocation.

## Verification and gates

- `lake build Roth.Separation` session35267 exited0, build completed successfully (1876 jobs); `/private/tmp/roth-separation-d04-build.log`.
- Native complete unfiltered LSP: success true, partial false, 0 errors/32 warnings; `/private/tmp/roth-separation-d04-lsp.json`. Warnings outside target persist for later workers and pending public proposal.
- Independent exact original type/proof imports only Mathlib.Data.Finsupp.Option, not Roth.Separation; session96354 exit0; `/private/tmp/roth-separation-d04-independent.lean` and `.log`; axioms propext, Classical.choice, Quot.sound only.
- Public signatures/definitions and existing block docs verified byte-identical by direct parsing against worker snapshot. No sorry/new axiom/haveI/letI/limit/debug source additions.

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|pass|actual module build exit0 above|
|definition_protected|pass|no def/abbrev changed|
|theorem_statement_protected|pass|only authorised redundant private wrapper deletion; all public signatures unchanged|
|structure_gate|pass|one-line original body removed; no new branches|
|naming_gate|pass|no forbidden name, no rename|
|line_packing_gate|pass|table above, final target deleted|
|inequality_orientation_gate|pass|zero reverse inequalities|
|comments/docs|pass|all preserved|

No rename queued; no decomposition flag. Parent owns full-project, separate LeanEval, cumulative compatibility approval, exact-path commit/push; this worker does not claim those later gates.

## Delta and phase checklist

Original target3 lines →0; including scoped omit and separator,5 lines removed. Two caller replacements add2 lines each: source611→610, net−1 exactly (5 removed −4 added). Diff is three hunks only. Comments-preserved: none in target, all existing block docs identical. Refactoring needed: none beyond applied authorised wrapper deletion. Public instance proposal remains pending and untouched.

- [✓] Step1 references read.
- [✓] Step2 all24 audit items.
- [✓] Step2.5 five actual searches.
- [✓] Step2.6 every binder/individual probes/private literature exemption.
- [✓] Step2.7 every original signature line width table.
- [✓] Step2.8 inequality table.
- [✓] Step3 every42 rule status.
- [✓] Step4 holistic reflection.
- [✓] Step5a complete clean native diagnostics.
- [✓] Step5b actual module/diff gates.
- [✓] Step6a no rename required.

Final actual-module profile, cumulative original proof/actual axiom results and source freeze recorded below after requests drain.

## Actual module profile / buzz

`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`, session79783, exited0. Full native trace `/private/tmp/roth-separation-d04-final-profile.log`; per-declaration anchor extraction `/private/tmp/roth-separation-d04-profile-anchors.json`. Baseline is owner-supplied actual module trace `/private/tmp/roth-separation-d03-final-profile.log`, whose target was unchanged at worker start. These are actual repository module anchors, not independent-copy or aggregate categories.

| Declaration | Before command + async | After command + async | Outcome |
|---|---:|---:|---|
|private mapDomain_add_single_none|9.941 +59.390 =69.331ms|removed|No retained target cost|
|coeff_coeffNone (changed use)|12.997 +38.009 =51.006ms|8.384 +100.362 =108.746ms|under1000ms|
|coeff_rename_mul_aeval (changed use)|27.491 +367.018 =394.509ms|45.540 +479.209 =524.749ms|under1000ms|

Nested value/header/repeated syntax expansion timings are not added a second time. Inline simp raises the two measured caller times in this run; no overall speedup claimed. All owned/affected declarations remain comfortably below budget (none near750ms); no performance fix or deferral needed. Buzz outcome FAST-BOARD. Raised limits removed0, added0. No source profiling scaffolding.

## Cumulative original compatibility / actual axioms

`lake env lean /private/tmp/roth-separation-d04-compatibility.lean`, session39457, exited0; full log `/private/tmp/roth-separation-d04-compatibility.log`. This adapts owner's earlier full ORIGINAL-source compatibility harness by removing the deleted target from the expected retained-constant inventory only. All30 ORIGINAL declarations re-elaborate in independent namespace, including original target proof and type; all20 original public type/value recovery examples succeed by rfl. Actual imported environment lookup by exact suffix (not fabricated private-name strings) checks all27 retained original declarations, public/private, using Lean.collectAxioms. Every actual axiom set is a subset of propext/Classical.choice/Quot.sound. Deleted private original types are witnessed by independently compiled ORIGINAL proofs, not self references. Individual binder raw results: `/private/tmp/roth-separation-d04-binder-probes.json`.

The discarded first direct-rewrite module attempt session23206 exited1; later native diagnostics, actual module build, final actual module profile and full original compatibility all exited cleanly on the corrected source. No failure output is represented as success.

## Frozen handoff

All Lean/native requests and compiler sessions drained before source release. Source SHA256 `1fd92ece12094dc1d71783cfcfe6b7f92e92cf019d409e048e70f1074208831d`. Worker explicitly revoked ALL source ownership to parent and entered report-only mode before this append. No further source edits will be made. Parent must independently run sequential full project and separate Roth.LeanEval gates, cumulative compatibility, then exact-path commit/push before next declaration. Public instance menu remains pending approval and unapplied.

## Owner cumulative publication gates

Source FROZEN SHA256 `1fd92ece12094dc1d71783cfcfe6b7f92e92cf019d409e048e70f1074208831d`; leaf ownership revoked and requests drained before owner gates. Owner probe `48051` exit0,39.71s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d04-compatibility.{lean,log,json}`. Owner build session `79342` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,117.27s/27.24s; source hash stable. `/private/tmp/roth-separation-d04-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
