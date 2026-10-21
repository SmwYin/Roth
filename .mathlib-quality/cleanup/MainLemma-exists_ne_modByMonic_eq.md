# Original20: `Roth.exists_ne_modByMonic_eq`

Fresh dedicated original20 worker, full authorized Mode B. No helpers introduced, no
original21+ cleanup/audit credit, no Git/shared-progress/rename edits. Owner retains publication.
The final source is 704 lines, SHA `0b204a8c710990afeaca6151e06cc381c94a1b7f071ab717a189cfa22cf69e4b`;
entry was 721 lines, SHA `5622adfc4372f9e84ee0239f2c14a1b810649a8a83fd7c3fe6b6691a44e18731`.
Target proof 35→14 lines; declaration excluding doc 41→21, whole-file saving17 includes
expanded accurate public doc and necessary three-line caller specialization. Common witnesses
remain outside `∀ j ∈ J`; neither distinctness nor either box-membership is lost.

The proof maps the finite box subtype directly to a function of bounded integer coefficients,
uses `Fintype.exists_ne_map_eq_of_card_lt`, and reconstructs each remainder with
`Polynomial.sum_modByMonic_coeff`. This removes manual image/cardinality finsets and the
separate high-coefficient/WithBot argument. The statement now permits arbitrary universe
`σ` with finite `Function.support r`, uses `finprod`, and bounds only coefficients below
`f.natDegree`. The sole actual direct consumer is `Roth.main_lemma`, inventoried from actual
TYPE+opaque VALUE references before and after. Its original all-coefficient bound specializes
by a lambda and its finite product by `finprod_eq_prod_of_fintype`.

Evidence root: `/private/tmp/roth-mainlemma-exists-ne-mod`. All raw failed variants and
unlaunched prospects are retained with their distinct status. Reports never treat partial
output, zero remaining tactic goals, or failed whole processes as passes.

## Full references and scope

Read full original20 dispatch, worker prompt854lines in bounded chunks, future profiler
instructions112lines, installed Lean4/mathlib-quality skills, commands cleanup1847,
cleanup-all488, buzz279, generalise603, and full golfing342/proof-patterns408/search493/
generalisation189/cleanup-gates361/style1300/naming517/review206/profiling233 references.
Read central takeover and MainLemma ledger. Explicit user standing authorization governs
beneficial implementation. No additional helper lifecycle was necessary. Headline cap15,
ordinary helper30/branch10 observed. Foreign main's final GLOBAL and original27 work remain
with the owner and get no audit credit here.

## Complete 24-item audit

1. **LINT:** actual complete native file has only preserved header warning; target none.
2. **HAVE SCAN:** original hscard411–413, htcard414–418, hlt419–421, hmaps424–429,
   hdegf436–438 each one use; h0 439–440 had two uses in final rw. Entire manual counting
   and high-index branch removed through direct APIs. Current target has no `have`.
   Anonymous local Fintype is used implicitly; F is used for cardinal collision and reconstruction.
3. **SET_OPTION:** none introduced; actual runtime defaults200000/20000/512 checked.
4. **SIMP SQUEEZE:** counting `simpa only [...]` and terminal reconstruction `simpa [...]`;
   unsqueezing terminal reconstruction compiled guarded whole0 with same expression hash. Counting retains `only` as the measured exception detailed below.
5. **NAMING:** existing `exists_ne_modByMonic_eq` accurately describes simultaneous distinct
   witnesses and uses Polynomial API's embedded spelling. No forbidden scheme/abbreviation;
   no new rename. All four queued project-end renames retained byte-exact.
6. **LINE PACKING:** machine measured seven-row table below, all `ok`; width100 #check
   included in successful independent replay, every signature code line≤100.
7. **BY PLACEMENT:** `:= by` at final signature line, no change needed.
8. **FORMAT:** ↦ lambdas, modern `lia`, anonymous typed local instance, no blank proof lines.
9. **COMMENTS:** no original inline target comments. Full Source quote byte-exact, all seven
   main proof signposts and every unrelated source byte preserved by exact reversal check.
10. **DOCSTRING:** public summary describes finite support, common pair, low-degree bound,
    finite specialization and usual product. Source quotation retained verbatim.
11. **VISIBILITY:** public module headline and reusable collision statement stays public.
12. **STRUCTURE:** proof14≤15, no branches/helpers. Correlated existential conjunctions are
    retained under explicit task instruction; splitting would destroy the common-pair API.
13. **MATHLIB:** five actual searches below, partial generic APIs reused directly;
    no existing exact simultaneous box/diagonal-Hasse statement found in consulted results.
14. **JUNK DEF:** n/a substantive theorem, no new DATA definition.
15. **EXISTS LEMMA:** n/a substantive common-pair existence, not trivial packaging.
16. **SHOW/CHANGE:** no redundant tactic show/change. Term `show` fixes Nat count and
    integer toNat normal form for `lia`/`exact_mod_cast`; keep.
17. **PUSH_NEG:** original high-degree negative branch removed, no push_neg remains.
18. **GENERALISE:** complete outer/inner2.6a–e below, exact old recovery and callers checked.
19. **INEQUALITY:** zero reverse inequality occurrences; explicit scan table below.
20. **NORMAL FORM:** remainder equality remains canonical, coefficient reconstruction stays
    internal, no duplicate equivalent public APIs.
21. **SYNTAX-GEN:** hC localized to low coefficients, eases callers without changing conclusion.
22. **IMPORT FANOUT:** no import change, all reused APIs already available.
23. **CASTS:** actual drop-codomain-ascription probe whole0 kept; genuine Nat→Real/Int,
    Fin→Nat and bounded-subtype→Int coercions remain. Explicit `.1` projections are required
    to avoid observed default200k elaboration timeout, not cosmetic.
24. **INSTANCE NAME:** no declared named instance; anonymous local Fintype only.

## Packing and inequality artifacts

|Line|Current chars|Next complete unit|Next chars|Arithmetic|Action|
|---|---:|---|---:|---|---|
|402|93|`{f : Polynomial ℤ}`|18|93 + 1 + 18 = 112 > 100|ok|
|403|67|`(hC : ∀ W ∈ boxFamily r B, ∀ j ∈ J, ∀ i < f.natDegree, \|(diag (hasseDeriv j W) %ₘ f).coeff i\| ≤ C)`|98|67 + 1 + 98 = 166 > 100|ok|
|404|58|`\|(diag (hasseDeriv j W) %ₘ f).coeff i\| ≤ C)`|43|58 + 1 + 43 = 102 > 100|ok|
|405|49|`(hcount : ((2 * C + 1 : ℕ) : ℝ) ^ (f.natDegree * J.card) < ((B : ℝ) + 1) ^ ∏ᶠ j, (r j + 1))`|91|49 + 1 + 91 = 141 > 100|ok|
|406|97|`∃ W' ∈ boxFamily r B,`|21|97 + 1 + 21 = 119 > 100|ok|
|407|59|`∀ j ∈ J, diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f := by`|73|59 + 1 + 73 = 133 > 100|ok|
|408|79|`proof follows`|—|—|ok|

The 98-character hC parameter is continued only at its logical low-index/body boundary;
58+1+43=102 prevents moving its coefficient body up. All rows use actual codepoint counts.

|Occurrence|Scope|Before ≥/>|Final ≥/>|Rewrite/rename|
|---|---|---:|---:|---|
|1|entire target signature and hypotheses|0|0|none|

## Actual five-search status

|Search|Actual evidence|Result/action|
|---|---|---|
|A semantic Finder|finder-search.json|Generic finite polynomial coefficient APIs partial; reuse reconstruction sum|
|B type Loogle|loogle-search.json|Finset/Fintype collision APIs partial, use Fintype direct|
|C natural-language LeanSearch|leansearch-search.json|Set/Finset/Fintype collision APIs partial, no exact full statement|
|D complete source/name variants|source-search20.stdout.txt + metadata|Exact target existing project result, generic coefficient/collision names confirmed|
|E local name lookup|local-search.json|Index unavailable; honestly not evidence of absence, source search supplies fallback|

Queries and untruncated returns are retained. Math MCP unavailable in this session; no
second-opinion response invented. Existing generalized family/count from17/18 are reused,
not re-audited for new credit. No exact library duplicate claimed.

## Generalisation2.6a: every outer and inner binder

|Binder|Kind/role|Actual result and justification|
|---|---|---|
|old `{m : ℕ}` / new `{σ : Type u}`|type/value universe|Finite-index-only restriction removed; actual Nat ambient and ULift.{1} positive applications passed|
|`r : σ → ℕ`|degree-bound value|Keep; theorem counts r-dependent box, no meaningful omission|
|`[Finite (Function.support r)]`|new instance|Matches existing finite box/count API; drop probe fails synthesis. Not claimed mathematically necessary: infinite-support collision may follow by fresh variables, but finprod count ceases to count that family|
|`B : ℕ`|coefficient-box value|Keep discrete Nat parameter used by box/count; no extra positivity added|
|`{f : Polynomial ℤ}`|divisor value|Keep integer ring because coefficient interval is finite with cardinal2C+1; arbitrary real ring invalidates counting model|
|`hf : f.Monic`|Prop|Keep; full-premise f=0 counterexample when removed passed|
|`J : Finset (σ →₀ ℕ)`|finite selected derivatives|Keep arbitrary finite collection, no extra order/sign/size assumption|
|`C : ℕ`|bound value|Keep arbitrary, including0; finite interval cardinal used, no positivity requirement|
|`hC`|Prop|Restricted to needed low-degree indices; high-index coefficients are automatically zero under monicity and C:Nat. Actual positive degree f=X example and exact old specialization passed|
|hC `W`, membership|inner value/Prop|Keep all box members; needed to define coefficient map on entire box|
|hC `j`, membership|inner value/Prop|Keep all selected j under same map/common witnesses|
|hC `i`, `i<f.natDegree`|inner value/Prop|Nat index + explicit low-degree restriction, no high-index obligation; reconstruction handles rest|
|`hcount`|Prop|Strict bound essential; weak≤ and omitted-count singleton counter boundary passed|
|product `j`|inner variable|General finprod, exact finite-product recovery checked|
|`W'`, membership, `W''`, membership|inner existential values/Props|Keep order and common pair; no independent per-j witnesses|
|`hne`|inner Prop|Keep distinctness, enforced counterexamples cannot conclude|
|conclusion `j`, membership|inner value/Prop|Keep every selected derivative beneath same pair|

2.6b: mechanical negative file tests drop support/monic/bound/count and weak count, whole
failure honestly retained. Proof-bearing final8 properties/counters are accepted only from
whole0 closed TYPE+actual opaque VALUE/inferredTYPE/std3 verification. Positive cases:
Nat ambient r=0/Jempty; Nat ambient two common selected indices; Nat ambient nonzero finite
support; Nat ambient f=X positive divisor degree; universe-lifted ambient. Three full-premise
counters: B=0/Jempty singleton under weak count; nonmonic f=0 with vacuous low-coefficient
bound and strict count but no equal remainder pair; monic f=X with strict count but missing
hC and no equal remainder pair. Removing strict count covered by weak-count counter.

2.6c: arbitrary ambient finite-support and low-coefficient bound were beneficial evidenced
changes under standing authorization and were implemented. No arbitrary-ring change:
finite integer interval cardinality is the concrete input, not a gratuitous class restriction.
Infinite-support mathematical extension is a separate API question and is not falsely
refuted by finite-instance implementation failure. No additional convenience wrappers.

2.6d: exactly three actual public-literature queries and actual top-three results each:

Query1: `Roth auxiliary polynomial pigeonhole bounded coefficients lemma9 generalization` (complete raw literature20-query1.json).

1. [Proof of Roth’s Theorem](https://diposit.ub.edu/bitstreams/8cfc8916-c376-44d7-8822-14f9fed3aa15/download).
2. [Compositio Mathematica paper](https://www.numdam.org/item/CM_1996__101_3_225_0.pdf).
3. [An elementary approach to Roth’s theorem](https://aleksa-milojevic.github.io/expository/roth.pdf).

Query2: `Siegel lemma pigeonhole polynomial coefficients monic remainder generalization` (complete raw literature20-query2.json).

1. [Siegel’s lemma](https://en.wikipedia.org/wiki/Siegel%27s_lemma).
2. [O.B. Berrevoets thesis](https://www.universiteitleiden.nl/binaries/content/assets/science/mi/scripties/bachberrevoets.pdf).
3. [EMS Survey, Tao](https://ems.press/content/serial-article-files/36979?nt=1).

Query3: `polynomial method pigeonhole simultaneous Hasse derivatives auxiliary polynomial finite support` (complete raw literature20-query3.json).

1. [Bounding the Number of Common Zeros](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/bounding-the-number-of-common-zeros-of-multivariate-polynomials-and-their-consecutive-derivatives/678AC5C9D8B85601FDD844BA63126937).
2. [The Method of Multiplicities](https://sites.math.rutgers.edu/~ss1984/thesis.pdf).
3. [On an analogue of BRK-type sets in finite fields](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/on-an-analogue-of-brktype-sets-in-finite-fields/2F7EDE5A8CA3950976A24109DF83BEA0).

These concern classical pigeonhole/Siegel auxiliary polynomials and polynomial derivative
constraints; the useful abstraction here is a finite simultaneous coefficient map. Generic
pigeonhole is already in mathlib. The Wikipedia hit is retained as an actual result, not
used as authority; no strongest-known-form claim. Primary Tao/expository/research results
support the structural interpretation, not a claimed new mathematical theorem.

2.6e: ambient generalization and low-index input form applied, accurate doc/caller updated; actual old704 and
entry721 complete proofs, final target and full old/current callers verified independently.

## Every golfing rule (42 statuses)

- [1.1] n/a no trivial by-exact wrapper.
- [1.2] n/a no rfl wrapper.
- [1.3] old rw/exact route replaced by direct map/reconstruction.
- [1.4] applied simpa counting and reconstruction.
- [1.5] n/a no trailing rfl after simp.
- [1.6] tuple witness packaging retained.
- [1.7] direct existing generic Fintype API used.
- [1.8] n/a no contradiction route.
- [1.9] ↦ lambda used; remaining lambdas not eta reducible.
- [1.10] n/a original non-by h0 had two uses; by-haves removed through strategy rewrite; current no have.
- [1.11] n/a no apply-intro chain.
- [1.12] n/a no tactic show; term show expected types load-bearing.
- [1.13] obtain retained.
- [1.14] old separated rewrites superseded by reconstruction.
- [1.15] terminal reconstruction unsqueeze whole0 kept; counting only retained after measured unsqueezed1125.758/1428.514ms regression and corrected explicit-only probe.
- [1.16] n/a no nonterminal bare simp.
- [1.17] dot notation used for hC membership projections and Subtype.coe_ne_coe.2; generic Fintype function is not an object-method candidate.
- [1.18] <| by applied and final module/independent replay passed.
- [1.19] old push Not branch eliminated.
- [1.20] public substantive theorem cannot inline.
- [2.1] actual whole-proof grind failed, retained.
- [2.2] n/a no grind retained.
- [2.3] simpa reconstruction applied.
- [2.4] n/a no analytic scalar goal.
- [2.5] n/a no positivity subgoal.
- [2.6] n/a no gcongr chain.
- [2.7] lia closes integer toNat cardinal normalization.
- [2.8] actual whole-proof aesop failed, retained.
- [2.9] exact_mod_cast moves real count to Nat, kept.
- [2.10] n/a arbitrary ambient existential theorem not a finite decision computation.
- [2.11] n/a no field denominators.
- [2.12] n/a no ring-normalization ending.
- [2.13] collision API avoids duplicate symmetric branches.
- [2.14] n/a no calc.
- [2.15] n/a no repeated branch structure.
- [3.1] n/a no erw.
- [3.2] n/a no legacy analytic lemmas.
- [3.3] lia used before omega; no omega retained.
- [3.4] n/a no rcases rfl.
- [3.5] n/a high-level existence inappropriate as simp attribute.
- [3.6] n/a no simp_all.
- [3.7] no heartbeat/recursion/synthesis option raises.

## Step back, actual failures, and trusted acceptance

Whole-proof simp/aesop/grind/exact?/apply? were actually compiled under a closed-value guard;
all failed and are retained as rejected, including any automation-created sorryAx. The new
mathematical strategy is a direct bounded-coefficient function, not helper extraction solely
for a line cap. Existing generic pigeonhole plus monic coefficient-sum reconstruction exposes
that strategy and removes original35-line proof's redundant cardinal/image/high-index work.

Candidate sixth failed at default200k because elaboration unfolded ambiguous bounded subtype
coercions; explicit `.1` projections fixed it. Seventh failed on interval `toNat` normal form;
explicit typed `show` + lia fixed it. Eighth, unsqueeze and redundant ascription removal all
passed whole guarded compiles. First–fifth/pipeline prospects without runs are unlaunched,
not successes. Initial property file failed arithmetic/ext/count-type elaboration; corrected
v2 passed. First inventory used invalid `Options.getNat`, failed and was corrected using
actual option declarations. These are implementation failures, not mathematical negatives.

Initial source7e301085/after20 and2ba/final20 snapshots remain historical.2ba applied `<| by` but failed the binding performance limit on both1125.758/1428.514ms samples (5roots), main5266.210/5282.571ms (9roots). Nested diagnosis is saved separately, never added into root sums: broad counting simpa invoked unnecessary card_eq_zero/Nonempty discharge. Actual guarded simpa? succeeded; narrower only probe failed because interval cardinality became Set.ncard. Replacing the instance name card_Icc with actual card_ofFinset plus explicit sub_neg_eq_add/card_coe/card_fin compiled guarded whole0. The production0b repair changes only three count-simplification lines from2ba; statement/doc/caller/proof14 and every other byte stay fixed. Full repaired gates below use distinct repaired20 names. Original2ba draft/caches/scaffolds/raw/run records are preserved, no historical inputs overwritten.

Historical2ba independent combined verifier is2476lines, SHA
`e2d8f6cfb2ef2df030a54ac4150173c6c51fb9016baefeba4e9c24c2b431d5b4`, whole0/217.627701583s.
Raw SHA `2fe5a72d46ecc863b303a8666147f8ab2c86046b2a90f255e84ebf5f532e52c6`.
The generated2342line base SHA66e693d25482270b072aea7885c6de20cf99efabd2172c22f44ddc778c3b2e10
is the byte-exact prefix of that combined file, which appends8 property declarations and their guards.
construction.generated_sha256 denotes the2342line base, not the2476line combined input. Original704 SHAa3d09825fb878c5d512cfdd3feca517465e0a8215807b1261b988f664915f3a8,
entry721, selected2ba704 and all complete caller bodies are copied byte-exact under independent
namespaces. Old family/box and Θ compatibility data are independent originals, not current20
self-use. Full28 exact contracts,70 closed TYPE+actual opaque VALUE/inferredTYPE/std3 checks,
6 complete nonself proof closures,1 exact H5 clone closure16966,8 positive/counter guards.
Own actual data reference inventory has8 literal references/4 Root–Entry pairs; every actual
TYPE+opaque VALUE AST, universes, all binder names/order/BinderInfo, closure/inferredTYPE/std3
is pre-gated before narrow expansion inside explicitly named DATA. No proof irrelevance,
arbitrary unfolding or name-map equating. Only propext/Classical.choice/Quot.sound allowed.
Actual default resource options200000/20000/512 checked. Owner independently reviewed exact2ba source construction and full guard tail without extra compiler jobs; new0b replay results are recorded below. The owner independently checked current0b full namespace bytes and the unchanged complete guard/property tail against2ba, including newbase97f5 and combinedeea73d.

## Final build, native, timing and provenance

Repaired0b independent combined WHOLE0/133.209580708s; actual input {'/private/tmp/roth-mainlemma-exists-ne-mod/repaired20-independent-combined.lean': 'eea73d7c27d0721a19b5a72729abf8eac6bf76c81e00f0bc80fbe4832a050430'}; raw SHA 1da5693864c3bd1ebbc508bedfb01c3fc41528a5aee25a4ee7716a8f76974c1a; exact generated base SHA 97f5e33d8bab98729889f2ca8d0273896b055573ff81bbec0d3d6490e230a4f1. Actual28contracts/70closed TYPE+opaque VALUE/inferredTYPE/std3/6nonself closures/4literalpairs/8literalrefs/H5clone1/8properties(5positive+3counter) all pass; actual defaults200000/20000/512. Three whole byte-exact original/entry/selected namespace bodies and all complete callers replayed, old704 source and own support independent of currenttarget.

Full build and separate Eval whole0; exact actual elapsed values and raw hashes are in repaired20-full.json and repaired20-Eval.json. Repaired module build whole0/99.726689042s. Actual baseline build whole0/3.035080083s.
|Repaired0b whole process|Exit|Seconds|Actual PGID drained|
|---|---:|---:|---:|
|repaired20-module|0|99.726689042|20705|
|repaired20-independent-combined|0|133.209580708|21118|
|repaired20-full|0|40.907744708|21182|
|repaired20-Eval|0|43.303179208|21229|
|repaired20-inventory|0|118.364960292|21344|
|repaired20-deps-ML|0|5.171539750|21388|

Fresh complete unfiltered MainLemma/Main/LeanEval native requests used only absolute
file_path and timeout_s60, no severity/range/declaration filters; all success=true,
partial=false, timed_out=false, failed_dependencies=[],0errors, preserved1/4/0warnings.
Actual request/result and17contemporaneous before/after source/config pins retained.

Identical inventory input261b69072db5edef690e4a2bbc3fae73ca1836a5f046bdb0ebb52bd65f58480c
was run before and final, both whole0, capturing FULL actual types and opaque values of
target and actual sole directconsumer main_lemma. Before113.116s; repaired final actual elapsed recorded in repaired20-inventory.json.
Repaired inventory whole0/118.364960292s, raw SHAe8df41019813c81f07c25ff6ff411188747395094857fd96a55b658e6074b1e1; full unfiltered raw values retained.
Final same-CLI `lean --deps Roth/MainLemma.lean` whole0 also retained.

|Matched frozen sample|Target ms|Actual disjoint roots|Complete main_lemma ms|Actual disjoint roots|
|---|---:|---:|---:|---:|
|before20-profile|274.340|5|4993.440|9|
|before20-profile-repeat|265.281|5|4898.593|9|
|repaired20-profile|322.983|5|5121.505|9|
|repaired20-profile-repeat|305.703|5|5000.879|9|

target paired mean 269.810500→314.343000ms, +16.505103%.

consumer paired mean 4946.016500→5061.192000ms, +2.328652%.

|Nested diagnostic sample|hC ms|necessary call ms|hγ ms|
|---|---:|---:|---:|
|before20-profile|652.486|9.467|16.904|
|before20-profile-repeat|640.211|9.957|13.330|
|final20-profile|721.925|36.149|24.859|
|final20-profile-repeat|667.073|31.054|14.167|
|repaired20-profile|661.904|32.271|13.475|
|repaired20-profile-repeat|643.704|33.620|13.431|

Nested times are inclusive diagnostic observations only, never added into root sums. The necessary call increases9.712→32.9455ms mean (+23.2335ms); hC646.3485→652.804ms and hγ15.117→13.453ms remain near baseline. The complete main pair retains115.1755ms/+2.32865% mean increase; the remaining distributed variation is not assigned a causal explanation. No hB1/context deletion or hC877ms regression, no third unchanged run, and no original27 credit.

Target+introduced-helper group is target alone and passes1000ms on both final captures.
Every ≥750ms target/actual-directconsumer received the required same-frozen-source paired
repeat BEFORE editing and AFTER finalization. No unchanged third run. Full main remains
preexisting multi-second work reserved to original27/final GLOBAL. Its bounded comparison
and actual nested costs are disclosed in timing diagnostics; no false whole-file performance pass.

Actual CLI each: `/Users/ramin/.elan/bin/lake env lean -j1 --profile
-Dtrace.profiler=true -Dtrace.profiler.threshold=0 <phase-scoped.lean>`.
Standalone trace scope begins before each full doc/Classical wrapper and ends after complete
command. Scaffold removal recovers exact canonical source; target and all actual direct
consumer complete types/bodies/context/order traced identically before/after. Anchors verify
exact qualified root/command payload/source-token boundary; column0 disjoint command/proof/
kernel/lint sibling roots counted once; nested/inclusive/internal Meta and trailing end
excluded. All actual kernel sibling names inventoried, no fixed4-root guess. Corrected parser
v2 excludes even column0 zero-duration Lean.Meta.realizeConst; initial parser outputs retained.

Frozen observed parent environment SHAa0ead8cc98afbe65b47d57087f3bd886f92675c5c47732fe8d6f8b0563f31582,
actual rawLakeenvironment observed before/after each run equal. No options/pins/import changes.
The full installed core compiled-artifact12592path SUPERSET and actual MainLemma/Main
setup.importArts+companions12201path PACKAGE/SETUP availability union are separately scoped,
not claimed exact loaded closure. Full unique union24793 paths was freshly hashed before
and after; it includes11 exact paths also in104saved project cache, so strict external
subset24782paths is the union minus that exact intersection, not a generic repo-path test.
Full availability bytes3929104384; strict external bytes3918200888. All strict external bytes unchanged,4actual binary/proxy hashes unchanged. All source/config17
and cache104 files preserved before API edits and final, all104 final actual/saved bytes
rehashed after gates. Exact scopes/counts/bytes and explicit UTF8/binary exceptions are in
catalogs/manifest. Unknown irrecoverable historical metadata remains unknown; no retrospective
claims for original19's captures. Runtime defaults preserved. Main.lean5f384557... and queued
rename file2be6064f... unchanged; other entry bytes exact by full reversal. No source comments,
helpers or preceding main context changed. All38 actual worker compiler/profile process groups are absent; native calls are complete. Sandbox ps observations failed and are not process-drain passes; kernel os.killpg(group,0) observations in each actual runner and fresh END checks provide the drain evidence. Optional heartbeat counters were not used.

## Eleven-step verification checklist and gates

- [✓] Step1 references: full mandatory skills/commands/references and dispatch read, listed above.
- [✓] Step2 audit: all24 items, full original-have inventory and final actions above.
- [✓] Step2.5 search: all5 actual searches/raw/source fallback and exact-vs-partial outcome above.
- [✓] Step2.6 generalisation: outer+inner a–e tables,3actual public queries/top3, guarded positive/counters and exact recovery.
- [✓] Step2.7 packing: seven actual codepoint rows allok + width100 #check output in independent whole0.
- [✓] Step2.8 inequality: full signature scan table0reverse occurrences, no rename needed.
- [✓] Step3 golfing: every42 rule actual status, failed automation retained, accepted variants guarded.
- [✓] Step4 step back: direct finite function collision/reconstruction replaces manual route, no artificial helper.
- [✓] Step5a native: fresh complete unfiltered actual ML/Main/Eval results, no errors/sorry, immutable pins.
- [✓] Step5b diff gates: definition protected (no DATA changes), theorem statement protected by authorized item18 ambient generalization/low-index interface + exact old recovery; structure14≤15 and common-pair conjunction exception explicitly required; naming clean/no in-place rename; packing/inequality pass; full module/project/Eval builds pass. Original/current full target+caller contracts/values/std3 and source integrity independent replay pass; timing target<1000. Whole-file GLOBAL not asserted.
- [✓] Step6a renames: none added; all four existing project-end renames unchanged, parent retains sidecar/Git/progress.

No refactoring deferred for original20; no helper introduced; no264helper inflation.
Retained original27/final GLOBAL multi-second findings are outside this task and must remain
visible to the owner. All worker compiler/process groups verified absent in repaired20-END.json;
no persistent LSP was killed. Source/compiler/native/profile leases released at END.
Owner independent review, ownerFULL→Eval/native and publication metadata remain owner work.


### Gate status — `exists_ne_modByMonic_eq` (Phase 4)

| Gate | Result | Details |
|---|---|---|
| lake_build_file | ✓ pass | Actual `lake build Roth.MainLemma Roth.Main` whole exit0/99.726689042s, source0b immutable; later full project and separate Eval builds also whole0. |
| definition_protected | ✓ pass | No `def`/`abbrev` changed. Snapshot reversal of only target/doc and necessary caller adapter recovers the entire721-line entry byte-exact; all retained DATA/helpers unchanged. |
| theorem_statement_protected | ✓ pass | Authorized audit item18: arbitrary universe σ with finite support and finprod count, plus equivalent low-degree input interface. Standing user authorization applies; actual old704/entry contracts, common-pair conclusion, complete callers, TYPE+opaque VALUE/std3 and positive/counter cases pass. |
| structure_gate | ✓ pass | Headline body14≤15, no branch/helper. The conjunctions correlate one distinct pair and both memberships across every j; preserving this common-pair structure is an explicit user requirement overriding mechanical splitting. |
| naming_gate | ✓ pass | Existing accurate name matches no forbidden scheme or abbreviation; no in-place rename. All four existing queued project-end renames unchanged. |
| line_packing_gate | ✓ pass | All seven measured signature rows above are ok; actual codepoint arithmetic and width100 #check retained; every signature line≤100. |
| inequality_orientation_gate | ✓ pass | Full signature/hypothesis scan table above: zero ≥/>; no orientation rewrite or rename needed. |

Overall: pass

### Result: `exists_ne_modByMonic_eq`

Before: 41 lines  After: 21 lines  Saved: 20 lines (declaration excluding doc).
Proof body: 35→14, saved21; whole file: 721→704, saved17 including expanded doc and necessary caller.

Audit issues found: 5    Fixed: 5    Refactoring deferred: 0.
These are five explicitly grouped worker findings: (1) headline proof exceeded15 lines;
(2) finite-ambient API restriction; (3) unnecessary high-index input obligation and matching
interface documentation; (4) proof style/ascription cleanup; (5) introduced broad-simp
performance regression. The low-index obligation is logically equivalent under monicity,
not a strict logical weakening. Individual actions within these groups are detailed in the
24-item audit and42-rule status list; the count is not the number of audit rows or probes.

Rules applied: 1.4, 1.15 (reconstruction unsqueeze; counting-only measured exception), 1.18,
2.3, 2.7, 2.9, 3.3. All other rules retain their explicit applied/kept/n/a/failure statuses above.

Gates: pass

Renames-queued: none. The four pre-existing project-end entries remain byte-exact.

Comments-preserved: no original target inline comments present; target Source quote1/1
byte-exact; main signposts7/7 preserved;0relocated and0removed. All other source comments
remain byte-exact by full-entry reversal.

Refactoring needed: none for original20. Original27/final GLOBAL work remains outside
this declaration's acceptance and has no original20 audit credit.

This report-only recovery supplies the two mandatory artifacts omitted from the earlier
sealed report. It adds no mathematical/source change or new Lean/native/profile run. The
historical8ac report,7ac manifest and7ec END are retained with explicit immutable-copy path
aliases in `repaired20-historical-sealed-path-aliases.json`; the old manifest is not asserted
to describe the replacement report/END bytes. Source/compiler/native/profile leases remain
released and were not granted for this recovery.
