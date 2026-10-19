# Fresh mapped determinant performance revisit

Scope: private `mapped_det_ne_zero_aux`, its actual entire direct consumer `index_le_lem6`, and an additional preserved independent `index_det_le` check. The dispatch initially misidentified `index_det_le` as the direct consumer; the owner corrected this before verification. `index_det_le` precedes the helper and does not depend on it. No caller proof edit was necessary. Counts remain216/264,Theta35/35,9/14files. This revisit adds0original declarations.

I used the Lean4 and mathlib-quality skills, read the full cleanup/buzz workflows, all five mandatory audit/search/golf/generality/gate references, and relevant style/naming/profiling references. No additional worker or helper was introduced. No Git, shared-progress, rename-queue, import, public contract, definition, header metadata, docstring or comment edit occurred. The owner's full project build THEN separate `Roth.LeanEval` and publication remain owner gates.

## Baseline and immutable evidence

Authorized published baseline HEAD `ad41bf6e380dc68da744c9265797f4b5aca3ef5d`; exact source SHA `2a41e042e8a363fd01a5038dadd04e3ddbd5d6e9ff57d788aa418e389ff7cd52`,992lines. Baseline source hash was checked before candidate creation. Inherited complete native evidence is explicitly inherited from `/private/tmp/theta-summax-second-performance/native-{theta,mainlemma}-final.json` and its native source binding: success=true,partial=false,timed_out=false,0errors,8/3warnings. The owner reports baseline full70.803s THEN separateLeanEval38.034s pass. No duplicate baseline compiler/native run was made.

Exact immutable FIRST: `/private/tmp/roth-theta-lem6/mapped_det_ne_zero_aux-FIRST-with-context.lean`, SHA `52d001067f8c51f34e14f870145f76fef796676f8957788a239ca36c00cb6104`. Its first full source had later numeric errors, not a whole-file success; clean confirmation is `FIRST-compiled-numeric-full.lean` SHA `b182acef13adc414fa0e27880cf048a66578a83f9afbc6ae42b30f925f8573b8` with `helper-candidate2.log` exit0. The original first-manifest.json and all source/context/success-log hashes are retained in `mapped-FIRST-provenance-hashes.json`. FIRST ALREADY omitted Fintypeτ and DecidableEqτ. No guessed old telescope or fictional new class removal is used.

Earlier dedicated retention/deletion audits are preserved, including `.mathlib-quality/cleanup/Theta-mapped_det_ne_zero_aux-helper.md`. Its rejected consolidated-simp source04171753 first1010.205ms/repeat779.268ms remains rejected history. The supplied26 actual whole-source histories are preserved at `/private/tmp/roth-theta-mapped-det-supplied26-history.json`: exactly one mapped observation≥1000, the present1049.976failure. These26 do not include every older prefix/rejected experiment. `historical-mapped-table-observations.json` additionally records51 discoverable table/timing observations without asserting exhaustive raw-log coverage. No old profile was rerun.

The inherited protected-report map certifies its earlier worker freeze. The owner's subsequent publication changed some reports, including Theta.md. Those differences are recorded explicitly in `owner-publication-report-map-differences.json`; the current baseline versions are pinned by `current-baseline-protected-report-hashes.json`. The inherited manifests remain untouched.

## Failed trace diagnosis before repair

The failure is actual1049.976ms on source2a41, raw `/private/tmp/theta-summax-second-performance/actual-profile-final-first.log`, SHA `1431ecbd966c7e075e6bd6c618bbc74cad5f38d8734910fff88334a907af0e64`. Its strict mapped slice covers raw byte offsets99161376–110755188, SHA `d2d7b419fb5666f63037cc1a38721a8f777ba97843938eb5d5fbbdefcd0f066a`. Disjoint outer totals: command172.910 + async proof828.781 + addDecl12.362 + linter35.923. The later unchanged-source829.583ms sample is preserved and does not clear the failure.

The nested hmapdet313.241ms includes type127.515ms and subproof182.535ms; these are nonadditive diagnostics. Three separate map_ne_zero_iff refinement steps155.021/157.019/151.553ms are substantial. Entry simp64.526ms is only about6% of the failed total. The source-free hotspot JSON and the complete eight-cause assessment are retained separately; no nested macro/kernel timing is added to the declaration total.

|Cause|Assessment and action|
|---|---|
|1 instance synthesis|Generic hom/class inference supports the expensive transports, but no single dominant synthInstance node is established. No instances/priorities changed.|
|2 fat simp|Not the primary cause: entry simp64.526ms; original rw/congr/ext certificate retained. Prior consolidated-simp failure preserved.|
|3 defeq/unification|Primary: underspecified polymorphic hom transports must unify with a large expected expression. Replace refinement with goal-directed map_eq_zero_iff rewriting.|
|4 terminal automation|No grind/aesop/arithmetic search in production; not the cause.|
|5 expected-type/metavariable churn|Primary: three placeholder-heavy equivalence refinements each≈150ms. Existing goal occurrences now determine the map before rewriting.|
|6 coercion churn|Necessary Fin→Nat and integer coefficient mapping remain; no repeated push_cast tower.|
|7 duplicated large subterms|Secondary: full matrix expressions in hmapdet type cost127.515ms. Keep the typed certificate and repair transports first; no extra helper hiding cost.|
|8 kernel/compiler|addDecl12.362ms includes nested kernel replay; small relative to async proof828.781ms. Nested kernel is excluded from additive totals.|

## Change, alternatives and holistic simplify

Replace all three `map_ne_zero_iff` refinements with `map_eq_zero_iff` rewrites. Rewrite multiplication by `mul_eq_zero/not_or`, discharge the first factor with hU, and transport the second through the existing evaluation/rename/equivalence wrappers. Merge consecutive rewrites. Mathematics, hF, both nonzero factors, both variable renamings, coefficient injectivity and the original hmapdet certificate are unchanged. Proof14→12lines; file992→990. Local hmapdet subproof3lines; no branch/subproof exceeds10. Signature byte-identical, all50declarations remain.

An initial scratch rewrite incorrectly requested mul_ne_zero_iff after expanding ne_eq; the second retained redundant ne_eq rewrites after the goal was already negated equality. Both expected-failure candidate sources/logs are retained. Corrected candidate3 compiled. Final merged proof separately compiled in the corrected heartbeat probe. Initial heartbeat scratch used obsolete missing-# command syntax; that failure/source is retained. Correct pinned syntax `#count_heartbeats in` passed: before3266,after3283. Deterministic work is essentially unchanged; actual profiled timing decides acceptance. No limits were raised.

Holistic simplify: ISSUES-FOUND-AND-FIXED. The costly transport pattern was replaced coherently and adjacent rewrites merged; no duplicated independent skeleton requires extraction. hmapdet is a typed proof-bearing fact, not a trivial term-have. A fully nested proof would obscure the transports. No equivalent whole Mathlib replacement was found by the bounded methods below. The generic injective-hom fact itself already exists in Mathlib and is used directly. The remaining statement specifically combines project Hasse/Option separation APIs; it is not a1–3-call wrapper. The built-in simplify tool is unavailable, so the full review was performed directly.

Fresh final-source nested diagnostics are preserved in `final-nested-hotspots.json`, keyed to both strict-slice hashes/offsets. First/repeat hmapdet249.501/270.011ms; main goal-directed transport rewrite244.310/214.862ms; second-factor transport116.926/148.640ms; final equivalence transport29.447/28.412ms. These are nested diagnostic rows, never added to outer declaration totals. The direct caller proof is byte-identical and no new helper was added; no work was shifted into a caller/helper.

|New proof identifier|Positive presence verification|
|---|---|
|mul_eq_zero,not_or|Final merged proof in successful corrected heartbeat probe, fresh module build and actual built opaque value/type/standard-axiom checks.|
|map_eq_zero_iff|Already used in the original final transport; actual native search/build and the same positive current proof checks verify all added uses.|

## All24 audit items

|#|Item|Result|
|---:|---|---|
|1|Lint|Inherited complete baseline8/3warnings; none on helper. Fresh complete unfiltered final evidence is recorded below.|
|2|Have scan|Only hmapdet, typed proof-bearing `have ... := by`, used once; retain for determinant functoriality. No term-have to inline.|
|3|Options|No production options or limit raises.|
|4|Simp|One terminal Matrix.ext entry simp[hasseDeriv_map], unchanged and unsqueezed. No nonterminal bare simp.|
|5|Naming|Private descriptive snake_case mapped_det_ne_zero_aux, unnumbered `_aux`; no forbidden abbreviation/pattern or rename.|
|6|Packing|All7signature rows measured below; existing wrapping retained exactly.|
|7|By|All `by` remain at the end of preceding lines.|
|8|Format|2-space tactics, no semicolon/blank proof lines, lambdas↦, widths≤100. Consecutive rw merged.|
|9|Comments|No target comment existed;0removed. Entire surrounding narratives preserved byte-identically.|
|10|Doc|Private helper has no docstring; all public documentation protected.|
|11|Visibility|Private, used by index_le_lem6 only. Public visibility unchanged.|
|12|Structure|12≤30lines, local certificate3, no ∧/∃ conclusion and no independent long branch.|
|13|Mathlib|Five actual methods and clean anonymous exact?/apply? probes completed; partial generic building blocks used directly.|
|14|Junk def|n/a theorem, no data definition.|
|15|Exists|n/a nonzero theorem, no existential wrapper.|
|16|Show/change|Neither in target.|
|17|Push_neg|Absent.|
|18|Generality|Every effective binder and both removed ambient instances audited below; no contract change.|
|19|Inequality|No≥/> in signature; nonzero is correctly oriented; no _ge_/_gt_ name.|
|20|Normal form|Determinant≠0 and factor≠0 canonical; local ¬equal rewriting does not change public normal form/attributes.|
|21|Syntax generality|hF is exactly the caller-supplied factorization. Replacing it with det≠0 would shift mathematics to the sole caller without benefit.|
|22|Imports|No new production import or fanout.|
|23|Casts|0new casts; existing Fin→Nat genuine cross-type; X-none coefficient/variable-ring annotation is load-bearing.|
|24|Instance names|No new instances or synthetic-name preservation scaffolding.|

## Five actual search methods and clean automation

|Method|Actual query/result|
|---|---|
|A LeanFinder|Nonzero determinant/Hasse derivatives/mapped polynomial/separated factors: returns generic variable-matrix determinant and unrelated polynomial facts, no full replacement. Raw native-search-finder.json.|
|B Loogle|map_ne_zero_iff: generic injective ZeroHom theorem, actual type verified; replacement transport uses generic map_eq_zero_iff. Raw native-search-loogle.json.|
|C LeanSearch|Injective coefficient homomorphism/nonzero polynomial/rename/determinant: map_injective and polynomial nonzero building blocks. Raw native-search-search.json.|
|D Source rg|Full-name Mathlib grep empty, untruncated mathlib-full-name.log; hasseDeriv_map and aeval_X_eq_rename are project facts. Source log retained.|
|E Native local|map_eq_zero_iff name-pattern returns existing variants; index unavailable, so no absence inference from index. Actual selected compiler verifies generic names. Raw native-search-local.json.|

Auxiliary variants: map_injective, rename_injective, map_ne_zero_iff, map_eq_zero_iff, rename_eq_zero_iff_of_injective, RingHom.map_det, hasseDeriv_map and aeval_X_eq_rename. Common-equivalents table has no separated-Hasse determinant entry. Presence of building blocks is established; no global mathematical-absence claim is made.

`PrefixAbsence.lean` succeeds separately against the exact production prefix BEFORE the target: both qualified and private suffix target/later index_le_lem6 are absent, preceding public index_det_le and private weight helper are present. `Automation.lean` uses anonymous examples with literal current header and exactly that prefix; it does not import Roth.Theta or name failed search theorems. exact? fails; apply? suggests only `refine ne_zero_iff.mpr ?_`, leaving a coefficient witness and then reaching the default200000heartbeat limit. grind fails, aesop/simp_all leave the nonzero goal, positivity cannot prove it. All six ranges/errors/suggestions remain in raw logs. No maxErrors or resource raise. Known native multi_attempt stall limitation is preserved; bounded ordinary compiler fallback was used.

## Generalisation, inversion and literature

The exact FIRST and current helper telescope is τ,R,l,D,U,V,hU,hV,hF; there is no Fintype/DecidableEq binder. Full effective names/order/BinderInfo/universes/conclusion and exact old full adapter are checked independently below. Negative tests are proof drop-tests, not claims that every imaginable restatement is impossible.

|Binder|Compiled drop/weakening probe and role|Decision|
|---|---|---|
|τ:Type u|omitτ rejected referenced section variable; determines R,D,U/renaming; already universe-polymorphic.|Keep.|
|R|autoImplicit=false drop rejects referenced R in hF/conclusion/proof.|Keep arbitrary polynomial.|
|l|Drop rejects matrix dimension,Fin l,D.|Keep arbitrary dimension, including0; no positivity assumption.|
|D|Drop rejects multi-indices under derivatives.|Keep arbitrary map; no injectivity/finiteτ assumptions.|
|U|Drop rejects factor/hU/hF.|Keep arbitrary first factor.|
|V|Drop rejects factor/hV/hF.|Keep arbitrary second factor.|
|hU|Drop unknown at factor discharge; True weakening type mismatch.|Keep nonzero. Positive zero-factor witness demonstrates why naive dropping fails.|
|hV|Drop/True weakening leaves V≠0 unresolved.|Keep nonzero; zero second factor similarly collapses product.|
|hF|Drop reaches unknown hF and unresolved determinant; R=0,U=V=1 counterexample building blocks compile separately.|Keep exact separated factorization.|
|Fintypeτ,DecidableEqτ|Both omissions already in immutable FIRST. Exact FIRST and current proof compile without either; actual metadata confirms no binder.|No new removal claimed.|

`Binders.lean/log` contains every expected-failure probe with autoImplicit=false for syntactic drops; no parse-error/missing-work substitution supports the hF probe. `Generality.lean/log` separately passes: zero1×1 determinant, either zero factor, nonzero unit factors, and the same mathematical argument over arbitrary CommRingA/IsDomainA/CommRingB with injective f:A→+*B. Standard axioms only. No expected-failure file certifies axioms.

The generic coefficient statement is valid but adds7effective context binders and has no extra actual caller. Current statement is already arbitrary inτ,D,R,U,V; the only real application isℤ→ℝ. Recommendation: preserve this private contract and use generic Mathlib transport facts directly; no additional unused helper/API churn. This is a technical retention recommendation, not a user veto.

Inversion: determinant functoriality is already RingHom.map_det; injective hom nonvanishing is already generic Mathlib API. Remaining content genuinely uses Hasse derivative compatibility, separated Option variables, both nonzero factors and polynomial/one-variable equivalence. An abstract det≠0 assumption would merely move proof work into index_le_lem6. Literature search: n/a private auxiliary, explicitly exempt by cleanup Step2.6d; no web absence claim. Public caller was not edited and retains its previously completed public literature audit.

## Packing and inequality

Reference: fresh independent FIRST #check and final full effective metadata at format.width100. Complete next binder/expression units are measured, not arbitrary token fragments. Signature was not edited.

|Sig line|Codepoints|Next complete unit width|Arithmetic|Action|
|---:|---:|---:|---|---|
|506|99|22|99+1+22=122>100|ok|
|507|71|34|71+1+34=106>100|ok|
|508|38|72|38+1+72=111>100|ok|
|509|78|74|78+1+74=153>100|ok|
|510|82|63|82+1+63=146>100|ok|
|511|67|71|67+1+71=139>100|ok|
|512|77|proof next|n/a|ok|


|Occurrence|Location|Result|
|---|---|---|
|none|Entire signature and hypotheses|No≥/>; ≠ expresses canonical nonzero. No rename required.|

## All42 golfing rules

|Rule|Result|
|---|---|
|1.1|n/a no by-exact wrapper.|
|1.2|n/a no by-rfl.|
|1.3|Final rwa retains rewrite+closure.|
|1.4|n/a no simp/exact pair.|
|1.5|n/a no trailing rfl.|
|1.6|Nonzero pair uses direct refine⟨hU,?_⟩; no constructor/exact pair.|
|1.7|n/a no apply/exact pair.|
|1.8|n/a no contradiction proof.|
|1.9|Matrix.ext lambda has mathematical indices; Unit injectivity lambda closes equality. Neither is an eta-redex.|
|1.10|Typed proof-bearing hmapdet retained; no single-use term-have.|
|1.11|n/a no apply/intro chain.|
|1.12|n/a no show.|
|1.13|n/a no have/projection destructuring.|
|1.14|Applied: four adjacent rewrites merged and two later rewrites merged.|
|1.15|Terminal entry simp remains unsqueezed.|
|1.16|n/a no nonterminal simp.|
|1.17|Equivalence `.2` transports replaced by goal-directed rewrites; existing dot injectivity remains direct.|
|1.18|No trailing parentheses avoided by `<|` without obscuring rewrite arguments.|
|1.19|n/a no push_neg.|
|1.20|n/a no trivial existential.|
|2.1|Actual anonymous whole grind failed.|
|2.2|n/a selected proof contains no grind prefix.|
|2.3|Consolidated determinant simp is a previously compiled/rejected performance variant; retain explicit certificate and repair measured transport cause.|
|2.4|n/a no analytic function-property goal.|
|2.5|Actual positivity failed.|
|2.6|n/a no ordered monotonicity goal.|
|2.7|n/a no Nat/Int linear arithmetic.|
|2.8|Actual aesop left determinant nonzero goal.|
|2.9|n/a no concrete numerical/cast computation; counterexample simp independently passes.|
|2.10|Symbolic polynomial nonzero is not finite decidable computation; no native_decide.|
|2.11|n/a no denominators.|
|2.12|n/a no ring/ring_nf endpoint.|
|2.13|n/a no symmetric cases.|
|2.14|n/a no calc block.|
|2.15|n/a no parallel similar goals needing a shared tactic.|
|3.1|No erw; deterministic rw used throughout.|
|3.2|n/a no continuity/measurability.|
|3.3|n/a no omega/arithmetic.|
|3.4|n/a no rcases/rfl.|
|3.5|Private one-consumer technical fact; no global automation attribute justified.|
|3.6|Actual whole simp_all failed; no production simp_all only.|
|3.7|No production maxHeartbeats or recursion raise to remove/add.|

Step back: no one-tactic whole proof found; direct existing Mathlib building blocks support the specialized mathematical chain. Term nesting would hide transport stages. No new abstraction, thin wrapper, deferred extraction, rename or import is required. Explicitly retained aeval_X_eq_rename/coeff_uniqueAlgEquiv_symm wrappers, hq and all publicΘ hB/hr/domain/header choices remain intact.

## Final semantic/native/performance gates

All static decisions were complete before the final sequential validation cycle. No production source edit followed.

|Gate|Result|Concrete evidence|
|---|---|---|
|build-theta-final|PASS|`/Users/ramin/.elan/bin/lake build Roth.Theta` exit0,31.375s; build-theta-final.log/json|
|build-mainlemma-final|PASS|`/Users/ramin/.elan/bin/lake build Roth.MainLemma` exit0,34.840s; build-mainlemma-final.log/json|
|independent-final|PASS|`/Users/ramin/.elan/bin/lake env lean /private/tmp/theta-mapped-performance/Independent.lean` exit0,39.133s; independent-final.log/json|
|actual-semantics-final|PASS|`/Users/ramin/.elan/bin/lake env lean /private/tmp/theta-mapped-performance/ActualSemanticsAugmented.lean` exit0,228.531s; actual-semantics-final.log/json|
|Entire preceding semantic scaffold|PASS|All627371prior bytes SHA43d17f09… unchanged; all727prior marker categories/counts +79fresh =806. Augmented SHA `80f9e72e4f94b13ede0a1c51660a8a6c9c574aae8eeaf15be42241cf58999a47`.|
|Canonical original/current proof blocks|PASS|All4full blocks retain exact offsets/hashes in immutable-scaffold-and-blocks.json. Immutable all29public recoveries/five definition VALUES/whole original2bMainLemma/independent currentMainLemma and all prior helper audits remain and re-elaborate.|
|Fresh independent FIRST/current/full callers|PASS|Exact FIRST proof copied unchanged and re-elaborated; current entire prefix+whole index_le_lem6/index_det_le independently elaborated. Full effective types, ordinary names/order/BinderInfo/universes/conclusion and exact old full adapters compare. Opaque value!true types/standard axioms/nonself plus actual/independent mapped→index_le_lem6 positive dependencies pass.|
|Actual RootTheta/MainLemma|PASS semantics|Fresh built Θ_lt/main_lemma values/types/stdaxioms and direct MainLemma→Θ_lt dependency refreshed; all prior actual dependency checks rerun. Actual timing remains unmeasured.|
|Fresh complete unfiltered native theta|PASS|success=true,partial=false,timed_out=false,deps=[],0errors,8warnings; native-theta-final.json. Every warning preserved.|
|Fresh complete unfiltered native mainlemma|PASS|success=true,partial=false,timed_out=false,deps=[],0errors,3warnings; native-mainlemma-final.json. Every warning preserved.|
|Protection/style/structure|PASS|Exact signature; only target proof changes;12≤30lines/local3≤10,50declarations; no new helper/import/option/axiom/sorry/native_decide/API/caller edit. All current baseline protected reports and FIRST/pins unchanged.|
|Full owner build THEN separateLeanEval/publication|PENDING OWNER|Not run or claimed by this worker.|

The native warnings concern retained header metadata/public parameters; none belongs to the target. No filtering, suppression or masking. The complete final-native source binding is native-final-source-binding.json.

Buzz outcome: FIXED for scoped helper and its entire actual direct consumer. Budget1000ms. Actual command: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean`. Capture window420s; no Lean limit change. All ordinary/native requests drained beforehand.

|Declaration|Inherited failed-source first/repeat ms|Final first ms|Required final repeat ms|Scope|
|---|---:|---:|---:|---|
|mapped_det_ne_zero_aux|1049.976/829.583|837.283|861.675|mandatory target/direct caller|
|index_le_lem6|659.696/552.163|520.369|621.220|mandatory target/direct caller|
|index_det_le|887.091/785.454|780.766|754.760|additional preserved check; no helper dependency|

First scoped≥750 predicate: True. Exactly one identical-final-source repeat was required and performed; no third sample.

final-first: exit0,223.164s,raw185463171strictUTF8bytes,SHA `3261ebfda85052a36084c7175d38b23bd5c5ec6dec20a0460b2467ba8a5fc0ae`; raw/table/status paths `actual-profile-final-first.log`, `actual-profile-final-first-table.json`, `actual-profile-final-first.json`. Source SHA `1b62c7dd177609e4cf6544e8c06b9ead761506122391e2345fd5db35fa46b4cc`. All50current declarations matched; no invalidUTF8/literalreplacement sequences.

final-repeat: exit0,234.335s,raw185143400strictUTF8bytes,SHA `b77c452be053b7f08ee2cb5242870bcc617be05724c28689d02dd1373ae2fca4`; raw/table/status paths `actual-profile-final-repeat.log`, `actual-profile-final-repeat-table.json`, `actual-profile-final-repeat.json`. Source SHA `1b62c7dd177609e4cf6544e8c06b9ead761506122391e2345fd5db35fa46b4cc`. All50current declarations matched; no invalidUTF8/literalreplacement sequences.

Each strict-slice descriptor includes exact source/raw/slice hashes and byte offsets plus anchored disjoint command/async proof/addDecl/compiler/linter rows. Nested tactic/macro/kernel rows are diagnostic-only and never double-counted. All failure slices are preserved separately.

New final-source unrelated≥1000 observations: none in the retained final sample(s). These observations do not discharge other historical mandatory repairs or owner final allactual gates.

Final source SHA256 **`1b62c7dd177609e4cf6544e8c06b9ead761506122391e2345fd5db35fa46b4cc`**. Source proof14→12/file992→990; no added helper, no original-count increment. Full artifact root `/private/tmp/theta-mapped-performance/`; complete path→SHA map in evidence-manifest.json, full source/pin/FIRST/caller/canonical-block maps in complete-source-proof-hash-map.json, terminal revocation/drain in final-freeze.json.

Artifact map: baseline/final source snapshots; inherited-failing-and-lower-repeat + source-free eight-cause diagnosis + supplied26history; all five native search rawJSON/source full-name logs; literal-prefix/anonymous Automation/ranges and successful PrefixAbsence; Binders/ranges; exactFirstIndependent; positiveGenerality; failed/corrected candidate and heartbeat sources/logs/statuses; current/independent entire semantic sources/raw outputs/806marker summary/fourblocks; sequential module builds; complete unfiltered native JSON/sourcebinding; actual fullsource rawUTF8 profile/status/all50tables/strict target-caller slices/allfailure slices; all pin/FIRST/currentbaseline report hashes and final process-group drain.


## Eleven-step checklist

- [✓] Step1: skills/full workflows/all required references.
- [✓] Step2: all24 substantive audit entries.
- [✓] Step2.5: all5 actual searches, variants, clean literal-prefix anonymous generic probes and separate absence/control gate.
- [✓] Step2.6: every binder/drop/weakening/positive generic/counterexample probe, inversion and private-literature exemption.
- [✓] Step2.7: all7packing rows with measured arithmetic.
- [✓] Step2.8: entire-signature inequality occurrence table.
- [✓] Step3: all42golf rules with actual applicable automation attempts.
- [✓] Step4: full-proof/term/alternative/generic/helper/simplify assessment.
- [✓] Step5a: fresh complete unfiltered native final diagnostics.
- [✓] Step5b: exact proof/type/opaque/stdaxiom/FIRST/fulloldadapter/allpublic/caller/sourceprotection/module/native/actualprofile gates.
- [✓] Step6a: no rename required; no queue/shared-progress/Git mutation.

Terminal source/scratch/report/compiler/native revocation, all own process-group checks and empty request arrays are recorded in final-freeze.json. Owner full project build THEN separateLeanEval, cumulative/allactual final checks and exact-path publication are pending and are not claimed here. MainLemma actual timing remains unmeasured after its bounded cutoff before main_lemma. No whole-file or whole-project timing pass follows from this scoped certificate. Other known mandatory repairs are outside this scoped declaration revisit; all newly observed actual failures are preserved in the final tables and strict failure slices.


## Owner independent evidence review

The exact leaf report is archived at `/private/tmp/theta-mapped-performance/leaf-final-report-owner-input.md`,
SHA256 `715c0b6995c4d10c6efeac41959873d54ff1c5466dd51ffaf2b1bfe0ec59365e`. Owner hash verification passes all17source hashes,3pins,23FIRST provenance hashes,214artifacts
and four complete canonical blocks. `owner-checked.json` independently verifies only the assigned
proof changed, the entire727-check627371-byte prefix is preserved,79/806semantic markers and
complete native0errors8/3warnings pass, and all50disjoint declaration totals in both captures
are below1000ms with exact strictUTF8 slices. Five anonymous automation errors are located
inside their example ranges. The apply? attempt gives a partial `ne_zero_iff` suggestion then
a global default-heartbeat timeout at1:5 outside its range: classify it as a bounded inconclusive
attempt, never a positive proof or a located negative result. The exact immutable FIRST declaration
is present byte-for-byte in the clean no-import-self FIRST file; its whole source is an exact
pre-target context plus that declaration, not a file beginning with the declaration fragment.
The inherited protected-report map is historical; the fresh dispatch baseline map is verified
against the current published reports. Neither schema/expectation adjustment changes source or
invalidates the successful Lean/native/profile evidence.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 75.708 s and 52.572 s.
Theta SHA256 `1b62c7dd177609e4cf6544e8c06b9ead761506122391e2345fd5db35fa46b4cc` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-p11-full.log` and `/private/tmp/roth-theta-p11-leaneval.log`; machine record
`/private/tmp/roth-theta-p11-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this validated revisit before the next source edit. This revisit belongs to the original 29 batch; original counts
remain Theta 35/35, overall 216/264, 9/14 files. No original-count increase comes from revisits or helper audits.
