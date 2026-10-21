# Original 23 — `Roth.le_index_of_forall_eval_eq_zero`

Status: original23 COMPLETE. All seven declaration diff gates pass, with complete current-source proof/property/build/native/input-boundary evidence. Aggregate file cleanup and the preexisting original27/main_lemma performance failure remain owner work; this is not a whole-file completion claim.

Scope is one ordinary declaration in `Roth/MainLemma.lean`, its attached documentation, and the necessary two-line bridge in `Roth.main_lemma`. No helper was introduced. The owner retains Git, publication, shared progress, rename queue, learning files, and the aggregate file review. The user-authorized generalizations are arbitrary universe-polymorphic finite variables and vanishing strictly below the cutoff. The coordinate inequality formulation avoids an additional DecidableEq instance. Original finite-box closed-cutoff applications recover through `mem_box.2` and `.le`.

Entry source: `e3c8e950614bc5701b2c82691e7faac9513ff7692c9051da80911a85fc42e37f` (699 lines). Final source: `e35102a497c66d1d28ba37f4c73afb4a873946c3dde85cb1cb04a86d1bdb8fd7` (696 lines). Target declaration 12→7 lines; proof 9→3 lines. The initial 13/10 count included the following blank line; `initial23-audit-count-erratum.json` corrects it explicitly. Main remains SHA `5f384557dccacaec469699cc7d32bd5666c9d525267e00433b7ae401fee98d09`, 685 lines. All five previously audited helper declarations, paper quotation, and nine inline comment lines constituting the seven narrative/signpost blocks remain byte-identical (`static23-source-guards.json`). There remain 32 written declarations: six definitions and 26 theorems. No original24 cleanup was performed.

## Complete 24-item audit

|#|Item|Concrete result|
|---|---|---|
|1|LINT|Before unfiltered native target file complete, no errors; only existing copyright header warning. Final unfiltered observations are recorded below.|
|2|HAVE SCAN|No `have` in old or selected target.|
|3|SET_OPTION|No target options, heartbeats, recursion changes, or named local instances. Default effective limits checked in executable guards.|
|4|SIMP SQUEEZE|No simp in target; final directed rw is explicit and stable.|
|5|NAMING|`le_index_of_forall_eval_eq_zero` describes its lower-bound conclusion and vanishing premise. No numeric, multipass, m-number, `_auxN`, forbidden abbreviation, `_gt_`, or `_ge_` pattern. No rename.|
|6|LINE PACKING|Every final signature row measured below. All whole next parameters/conclusion exceed the 100-column limit if moved up.|
|7|BY PLACEMENT|`:= by` ends the final signature line.|
|8|FORMAT|Two-space proof indentation; ordinary lambda arrows changed to ↦ in the target. Rule 1.18 uses `<|`. Existing caller syntax otherwise preserved.|
|9|COMMENTS|Exact paper quotation retained. Every caller inline comment/signpost retained, including hB₁/pre-count context elsewhere.|
|10|DOCSTRING|Explains strict cutoff and the coordinate box, including zero bounds; preserves source quotation.|
|11|VISIBILITY|Public API used by public main_lemma; classic file dialect. Public retained.|
|12|STRUCTURE|Ordinary result, absent from module headline list: applicable user limit ≤30 proof lines, each branch ≤10. Three proof lines, one short contradiction, no conjunction conclusion; no extraction/helper.|
|13|MATHLIB|All five actual search methods executed; relevant weightedOrder lemmas are partial matches, not this real-valued index/zero-bound API. Actual tactic attempts and literature details below. No unsupported absence claim.|
|14|JUNK DEF|n/a: theorem. No wrapper definition introduced.|
|15|EXISTS LEMMA|n/a: no existential conclusion or private witness theorem.|
|16|SHOW vs CHANGE|No show/change.|
|17|PUSH_NEG|Old explicit negation push replaced by le_of_not_gt and by_contra!. No deprecated push_neg.|
|18|GENERALISE|Full outer/inner binder audit below; Fintype-only coordinate-box and strict cutoff compiled, exact old contract and full caller recovered. Failed alternatives preserved.|
|19|INEQUALITY|Four signature order relations, all < or ≤, enumerated below; zero ≥ or >. No orientation rename.|
|20|NORMAL-FORM|Canonical lower bound on the real-valued index; le_index_iff supplies unrestricted nonzero-derivative characterization. Useful bounded-degree hypothesis restricts vanishing to the box.|
|21|SYNTAX-GEN|Coordinate box is an extensional predicate with no DecidableEq requirement. Keeps filtered-box application with one membership bridge.|
|22|IMPORT-FANOUT|No new production imports. Diagnostic imports exist only in saved scratch checks.|
|23|CASTS|No explicit coercions/ascriptions in target. Universe/type parameter annotations are necessary declarations.|
|24|INSTANCE-NAME|No named instance; no global/local Classical DecidableEq workaround.|

## Final per-line packing and inequality scan

|Signature row|Codepoints|Next whole parameter/conclusion|Arithmetic|Action|
|---|---:|---|---|---|
|1|99|`{r : σ → ℕ}`|99+1+11=111>100|ok|
|2|66|`(hvan : ∀ d, (∀ j, d j ≤ r j) → weight r d < c → eval α (hasseDeriv d P) = 0)`|66+1+77=144>100|ok|
|3|83|`c ≤ index P α r :=`|83+1+18=102>100|ok|
|4|25|``|last row; n/a|ok|

Actual `#check` uses `format.width 100` in the independent check. The table measures source codepoints, not bytes. No wide-hyp escape is used.

|Occurrence|Location|Final expression|Action|
|---|---|---|---|
|1|hd|degreeOf j P ≤ r j|already oriented|
|2|hvan inner coordinate box|d j ≤ r j|already oriented|
|3|hvan inner cutoff|weight r d < c|strict weakening verified; oriented|
|4|conclusion|c ≤ index P α r|already oriented|

No ≥ or > occurs in signature/hypotheses; `<|` is term application, not an order relation.

## Full 2.6a–e generalization audit

The used-as column includes TYPE dependencies, opaque proof VALUE uses, and inner functional binders. “Drop” means an actual changed-signature probe, not inferring necessity from textual occurrence. `drops23-all.lean` contains 14 actual probes with whole exit 1, errors mapped in `drops23-ranges.json` and `drops23-actual-summary.json`. These probes used the DecidableEq/Finset intermediate draft; the subsequent Fintype-only coordinate alternative is separately compiled. Failed proof candidates are never accepted from partial PASS markers.

|Binder|Class / used as|2.6a drop/weakening and 2.6b evidence|2.6c larger candidate / 2.6e action|
|---|---|---|---|
|m / σ|structure value / universe-polymorphic indexing of P,r,α,d|Dropping indexing data leaves ill-typed dependent binders. Arbitrary σ : Type* compiled in candidate v4.|Keep generalized σ; no enumeration or Fin m surrogate.|
|Fintype σ|typeclass / existing weight,index API|Actual drop and Finite-only probes fail to synthesize Fintype. Existing index definition fixes this interface.|Retain Fintype, no API-wide Index/Box rewrite.|
|DecidableEq σ (intermediate)|decidability / Finset box elaboration|v1 Fintype-only Finset box cannot elaborate. v2 explicit DecEq compiles. v3 fixed Classical theorem passes its own check but exact old-contract adapter fails; whole exit 1 rejected. v4 coordinate box compiles old contract without DecEq.|Remove extra instance via extensional box; do not change Box/Index or add a helper.|
|P|polynomial structure value / hP,hd,derivative,index|Actual drop leaves dependent hP/hd/expressions ill typed.|Retain arbitrary P.|
|ℝ coefficient type|fixed structure interface / existing real index|General-field actual signature probe cannot use real index API. Literature supports broader multiplicity theories but no small local replacement.|No forced Index rewrite, no unapproved broad refactor.|
|hP|proposition / le_index_iff|Actual drop leaves hP unavailable; zero P,r=1,c=1 certificate satisfies hd and hvan but refutes bound.|Retain necessary nonzero premise.|
|r|bound data / degree,box,weight,index|Actual drop leaves dependent expressions ill typed. No positivity assumption is introduced.|Retain all natural bounds, including zero.|
|hd|proposition / zero derivative outside box|Actual drop fails proof. X with all r=0,c=1 satisfies remaining vanishing but refutes bound.|Retain coordinate degree bound.|
|hd.j|inner coordinate data / degreeOf j,r j|Actual positive-coordinate-only draft fails; X/r=0 certificate satisfies the vacuous localized premise but refutes bound.|Retain all coordinates; strict/equality bounds would strengthen, not weaken hd.|
|α|point data / eval and index|Actual drop leaves dependent terms ill typed.|Retain arbitrary point; no equal-coordinate specialization.|
|c|real data / cutoff and result|Actual drop leaves cutoff/result ill typed. Compiled c=0 and c=-1 examples cover endpoints.|Retain arbitrary real c; no positivity premise.|
|hvan|functional proposition / contradiction at nonzero derivative|Actual drop fails; constant1,c=1 certificate refutes bound with hP/hd retained.|Retain equality vanishing, with weaker strict cutoff.|
|hvan.d|inner multi-index data / weight, hasseDeriv|Finitely supported multi-index is required by existing API; dropping it leaves derivative and weight dependent arguments missing.|Retain arbitrary d, not a chosen minimizer or total function conversion.|
|hvan.box|inner proposition / coordinate-restricted domain|Finset membership replaced by ∀j,d j≤r j; actual exact old adapter compiles. Removing box antecedent strengthens hvan rather than weakens theorem assumptions.|Keep useful degree box; no change to box definition.|
|hvan.box.j|inner coordinate data / d j,r j|Deleting coordinate constraints, or keeping constraints only when r j>0, enlarges the vanishing domain and therefore strengthens hvan. This is not a premise weakening; the hd.j counterexample is not misapplied to this contravariant position.|Retain the useful full bounded box; no stronger vanishing requirement introduced.|
|hvan.cutoff|inner proposition / below-c vanishing|≤c→<c is a weaker premise, compiled v4 and exact old-contract recovery. X,r=1,α=0,c=1 has index1 but first derivative at weight1 equals1, refuting old premise.|Keep strict cutoff; deleting cutoff strengthens hvan.|
|hvan.equality|inner proposition / exact vanishing|Actual ≤0 replacement probe fails proof; -1,c=1 certificate has all derivatives nonpositive but index0. Sign reversal follows constant1 certificate; no sign hypothesis can replace zero.|Keep equality; no weaker conclusion.|

2.6c: no remaining small beneficial generalization was identified. The nonpositive-cutoff case is already covered separately by `Roth.index_nonneg` (Index.lean:86). Folding that trivial case into a cutoff-dependent replacement for hP would complicate this reusable nonzero-polynomial criterion and does not improve its actual caller; it is not recommended as a local API change. General coefficient fields require changing the Index API and related infrastructure; that is a substantial separate project, not an omitted local typeclass weakening. 2.6d literature below is complete. 2.6e: both verified beneficial local changes are implemented. All premise counters retain the other mathematical premises; ill-typed dependent-value drops are described as elaboration failures, not mathematical counterexamples.

## Five actual search methods and automation

Bound observations `bound23-{finder,loogle,leansearch,local,references,automation}-{request,response,before-pins,after-pins}.json` preserve actual native args, times, complete responses, and fresh 17-pin observations for each call. Earlier unbound exploratory responses are preserved and are not input-closure gates.

|Method|Actual query / result|Disposition|
|---|---|---|
|LeanFinder|“A multivariate polynomial has weighted index at least c if every Hasse derivative of weighted order less than c vanishes at the point”, 8 hits including MvPowerSeries.le_weightedOrder and nat_le_weightedOrder.|Relevant analogue; Nat weights/Nat∞ order and positivity bridges do not directly supply the real index with zero bounds.|
|Loogle|`MvPowerSeries.weightedOrder, _ ≤ _`, 12 hits including le_weightedOrder.|Same partial match. Initial malformed `MvPolynomial.hasseDeriv, _ = 0` error preserved; not absence evidence.|
|LeanSearch|“multivariate polynomial weighted order of vanishing Hasse derivatives all lower derivatives zero”, 10 hits including orderNat∞ and analytic order.|No direct replacement demonstrated; avoid claiming exhaustive absence.|
|Source search / local index|Actual untruncated rg over mathlib MvPolynomial/MvPowerSeries and project Hasse/Index; weightedOrder local search had 14 hits; local index status `error` is not absence.|Exact-name source search exit1 is only a literal name search. Existing project le_index_iff plus derivative-degree lemma is the direct proof.|
|Actual goal attempts / references|grind, simp, aesop, exact?, apply? tested at actual goal. All fail to close whole proof; apply? suggestions are partial. Actual references total2: declaration and main_lemma caller.|`automation23-summary.json` records every returned item/error count; no successful full automation claim. Environment inventory independently finds sole direct TYPE+opaque VALUE consumer Roth.main_lemma.|

## 2.6d — Three actual literature queries, top three results each

Each query has its own complete actual request/response in `literature23-query1.json` through `query3.json`; initial combined exploratory response is retained separately. These are external mathematical context, not kernel proof evidence.

1. “Roth polynomial index vanishing Hasse derivatives weighted multiplicity generalization”:
   - [Discrete Analysis 2021:22, NSF-hosted paper](https://par.nsf.gov/servlets/purl/10322567): weighted multiplicity uses vanishing below a strict threshold, supporting the minimum-order viewpoint.
   - [Author-hosted multiplicity-code paper](https://people.csail.mit.edu/madhu/papers/2009/merger-eccc.pdf): Hasse derivatives encode multiplicity without factorial divisions.
   - [Hilbert functions and the finite degree Zariski closure in finite field combinatorial geometry](https://doi.org/10.1016/j.jcta.2015.03.011): finite-field polynomial and multiplicity context; not a direct replacement for this weighted-index API.
2. “multivariate polynomial Hasse derivative multiplicity weighted order vanishing general field”:
   - [Geil–Thomsen, More results on the number of zeros of multiplicity at least r](https://www.sciencedirect.com/science/article/pii/S0012365X17300043).
   - [Authors’ arXiv version](https://arxiv.org/abs/1410.7084).
   - [Conical Kakeya paper](https://www.sciencedirect.com/science/article/pii/S1071579719300607).
   These support broader-field multiplicity theory, but do not identify a small replacement for this project's real-valued Index API.
3. “Roth index polynomial derivatives degree box strict weight vanishing”:
   - [Baker–Wüstholz, Logarithmic Forms and Diophantine Geometry](https://nzdr.ru/data/media/biblio/kolxoz/M/MT/Baker%20A.%2C%20Wuestholz%20G.%20Logarithmic%20Forms%20and%20Diophantine%20Geometry%20%28CUP%2C%202008%29%28ISBN%200521882680%29%28210s%29_MT_.pdf): classical weighted polynomial index context; mirror is not used as proof authority.
   - [Roth, ICM 1958 proceedings](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf): primary classical index context.
   - [Androma theorem page](https://androma.org/theorems/8293): low relevance; not used for an inference.

The beneficial inference is the strict minimum cutoff; the compiled sharp-boundary certificate proves the local mathematical claim. Literature does not justify changing the coefficient API in this scoped cleanup. No MathMCP tool is installed; no fabricated call is claimed.

## All 42 golfing rules

|Rule|Actual status / reason|
|---|---|
|1.1|n/a: no by exact wrapper|
|1.2|n/a: no by rfl|
|1.3|n/a: no rw followed by an available exact term; terminal rw closes the rewritten zero evaluation|
|1.4|n/a: no simp/exact|
|1.5|n/a: no trailing rfl|
|1.6|n/a: no conjunction construction|
|1.7|n/a: no apply/exact chain; existing direct term style retained|
|1.8|applied: by_contra! hj|
|1.9|checked: lambdas bind derivative/nonzero/cutoff/coordinate and carry required arguments; no eta-redex|
|1.10|n/a: no have|
|1.11|checked: refine/fun already used at entry and retained; no apply/intro chain|
|1.12|n/a: no show|
|1.13|n/a: no have/conjunction projection|
|1.14|checked: one directed rw, no consecutive rw|
|1.15|n/a: no terminal simp only|
|1.16|n/a: no nonterminal simp|
|1.17|checked: .2 and .trans_lt already use dot notation|
|1.18|applied in final source e351: `exact he <\| by rw [...]`|
|1.19|checked: no deprecated push_neg; old explicit push Not eliminated by the proof refactor|
|1.20|n/a: not existential lemma|
|2.1|actual whole-goal grind attempt failed; retain explicit 3-line proof|
|2.2|n/a: no retained grind or preceding tactic chain|
|2.3|actual simp fails at whole goal; directed rewrite remains simpler|
|2.4|n/a: not a function regularity property|
|2.5|n/a: index vanishing cannot be obtained by sign positivity|
|2.6|n/a: no monotone congruence goal; derivative nonzero contradiction|
|2.7|n/a: no Presburger arithmetic goal in target; real weighted index needs its characterization|
|2.8|actual whole-goal aesop attempt failed|
|2.9|n/a: no numerical/cast normalization target|
|2.10|n/a: universal real polynomial proposition is not decidable computation|
|2.11|n/a: no rational algebra identity/denominator clearing|
|2.12|n/a: not a linear identity of available equations|
|2.13|n/a: no symmetric cases|
|2.14|n/a: no calc|
|2.15|checked: one contradiction goal, no repeated parallel tactics|
|3.1|n/a: no erw|
|3.2|n/a: no continuity/measurability|
|3.3|n/a: no omega|
|3.4|n/a: no rcases rfl|
|3.5|checked: theorem is specialized index criterion; no safe universal simp/aesop registration justified|
|3.6|n/a: no simp_all|
|3.7|checked: no maxHeartbeats option introduced or retained|

## Complete proof, property, and source checks

Guard review erratum: independent v1 whole exit0 is preserved but is NOT the final independence gate because its public string-prefix scans omitted descendants of actual private roots. Separate v2 uses a one-pass exact `Name.isPrefixOf` closure of every blocked current public/private Name, keeping the narrow Entry literal allowset unchanged. V2 whole rerun passed on e351 (371.511s, PGID32752 drained). Its actual deny block explicitly includes both private coeff_boxPoly._simp_1_2 and private boxPoly.eq_1. V1 remains preserved as superseded evidence, not the final gate.

The independent scratch input is constructed from byte-exact whole namespace bodies of the immutable genuine project original, preedit entry, and selected final source. It checks full all-binder/universe TYPE ASTs and actual opaque VALUEs, default effective limits, standard three axioms only, named DATA-only normalization with originating DATA-spine beta, and genuine nonself closed TYPE+VALUE dependency traversals. Both complete original and selected main_lemma proofs are elaborated, not replaced by constants. Old proofs must use their own old target/DATA; current target/caller/helpers and generated siblings are denied in old closures. Compiler literal sharing is admitted only after exact matched closed full TYPE+VALUE AST/universe/all-binder/std3 pregates. No arbitrary NameMap, proof irrelevance, proof unfolding, or current-self argument is used. Construction provenance is `independent23-construction.json`; full input and raw whole-exit evidence below.

Dynamic retained audit discovers all 32 actual source declarations and every actual generated child, including compiler-selected `_simp_1_1`/`_simp_1_2` or `_proof_1_1`… names when present; it does not assume any historical generated count. Every actual name receives closed full TYPE+opaque VALUE/inferred-type/std3 and kind/universe metadata; generated source absence is checked. Full generated ASTs and exact qualified names are preserved in raw logs. These are compiler-generated proof artifacts, not new meaningful helper declarations.

Properties include exact old contract, mixed zero bounds, empty variable type, negative cutoff, c=0 strict-vs-closed premise, necessary hP, necessary all-coordinate hd including failure of a positive-r-only localization, necessary hvan, signed-constant failure of nonpositive replacement, and the sharp positive cutoff X/r=1/α=0/c=1 with index1 and first derivative1. Every actual property and generated sibling is checked for closed TYPE+actual VALUE/std3. Drafts v1–v4 failed and remain rejected regardless of partial PASS lines. v5 whole exit0 was observed before the final `<|` style edit; the distinct final-current run below passed with 11 property roots and two actual generated children, including the added nonnegative countercertificate. A scratch native goal request failed because /private/tmp has no Lean project ancestor; its response is preserved, no gate credit, and successful CLI elaboration is used.

## Matched actual performance scope

Actual TYPE+opaque VALUE direct-consumer inventory selects only `Roth.main_lemma` inside the same source file. The byte-exact whole target and complete caller commands are bracketed by standalone trace options; stripping only those options recovers frozen canonical source exactly. All four captures use the same real argv prefix `/Users/ramin/.elan/bin/lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0` and the same frozen parent environment. Source/options/import order/binder/proof data are not replaced by #check or a surrogate theorem. Whole raw stdout and stderr are separate; all Meta roots (even zero), inclusive wrappers, nested diagnostic events, following declarations and namespace-end commands are excluded from root sums. Every actual disjoint kernel root is included once, with exact qualified actual names and full actual printed-command payload binding to the one canonical command. Old fixed root counts, substrings, headline matches, and stale sample reuse are not gates.

BEFORE first/repeat both completed before any edit: target 55.106/48.374 ms (four actual roots each); main 5124.358/4955.099 ms (nine actual roots each). PGIDs 30873/31021 drained/absent. Repeat was mandatory because the actual caller exceeded 750 ms. Final first/repeat, actual root metadata, and change-related call overhead diagnosis are recorded below. The owner's original27/main_lemma and aggregate performance problem remains outside original23 cleanup; it must not be dismissed as noise or claimed fixed.

## Actual immutable input boundary

Genuinely before edits: 17 source/config pins and 104 project compiled/setup/IR companion copies; actual dynamic setup.importArts package availability 12,201 files; fresh pinned-core availability superset 12,592 files; union 24,793; exact 11-path project-cache intersection excluded gives strict external 24,782 paths / 3,918,200,888 bytes. All strict external hashes were freshly rechecked before editing and again in final closure. These catalogs describe availability, never an exact loaded closure. Four actual proxy/pinned executables are freshly resolved and hashed. Actual binary strict UTF8 failures are declared as binary exceptions; ordinary raw/source/JSON files are strictly decoded. No pin, executable, options, dependency version or limit was changed.

Late dependency remediation is explicitly late: `lean --deps` is run on exact frozen BEFORE and FINAL target source with byte-identical imports and frozen actual profile environment. It is not labeled a preedit CLI observation or exact loaded closure. Every resolved path, including implicit core, must already have genuinely preedit package/core hash evidence and remain exact; the actual subset proof/args/times/raw stdout/stderr are preserved. A missing earlier hash is a blocker, never silently added to baseline.

Every launched Lean input is saved by SHA at launch, and every actual observed production revision is saved contemporaneously in `production-revisions/`. Exact v1 DecEq, coordinate485, and final e351 production revisions are retained. Pre-golf final snapshots were copied into `pre-golf23-final-snapshot` before refresh. A brief runner-edit variant was never loaded by the active process and was restored; originals, unlaunched variants, and `runner-variant-disclosure23.json` are retained. The package predecessor-label erratum preserves the first v1 observation and corrects its comparison label without fabricating a new hash.

## Eleven phase checks and seven diff gates

### Gate status — `Roth.le_index_of_forall_eval_eq_zero` (Phase 4)

|Gate|Result|Details|
|---|---|---|
|lake_build_file|✓ pass|Final affected build and final full build exited0; separate Eval CLI follows full build; complete unfiltered native files have no errors/sorries.|
|definition_protected|✓ pass|All definitions and all five audited helpers byte-exact; only target/doc and exact narrow caller bridge differ.|
|theorem_statement_protected|✓ pass|Accepted item18/user-authorized finite-σ and strict-cutoff generalizations; same lower-bound conclusion, exact original all-binder contract and complete original caller recovered in strengthened independent harness.|
|structure_gate|✓ pass|Ordinary target proof3 lines ≤30, branches≤10, no conjunction; no meaningful helper.|
|naming_gate|✓ pass|Descriptive name, no forbidden pattern/abbreviation/orientation; no rename.|
|line_packing_gate|✓ pass|Four measured rows:99/66/83/25; every next whole parameter/conclusion exceeds100; all actions ok.|
|inequality_orientation_gate|✓ pass|All four signature relations individually audited; zero ≥/>; no _ge_/_gt_ rename.|

Overall: pass (original23 declaration scope). Aggregate MainLemma/original27 performance remains FAIL/pending owner audit; not masked by this declaration's pass.

### 6b Result: `Roth.le_index_of_forall_eval_eq_zero`

Before:12 declaration /9 proof lines. After:7 declaration /3 proof lines. Saved:5 declaration /6 proof lines; file699→696. Audit issues found:6; fixed:6 (finite-variable generality, strict cutoff, direct contradiction structure, lambda notation, useful documentation, rule1.18). Refactoring deferred:0. Actual new golf rules applied:1.8 and1.18; all42 statuses are above. Gates:pass. Renames-queued:none. Comments-preserved:all9 caller/comment lines forming seven protected narrative blocks and exact target source quotation, none removed/relocated. New meaningful helpers:0. Refactoring needed:none for original23.

|Required phase check|Result / evidence|
|---|---|
|Step1 reference docs|✓ full installed skills/commands/references/context read; immutable reference copies and raw hashes retained.|
|Step2 full audit|✓ all24 rows, not only original19.|
|Step2.5 mathlib search|✓ five actual methods, bound args/responses/pins, full failures and partial matches disclosed.|
|Step2.6 generalization|✓ full outer/inner a–e table, actual drops/alternatives/old recovery/property counters, three actual queries Top3.|
|Step2.7 packing|✓ four measured rows with actual arithmetic.|
|Step2.8 inequalities|✓ every occurrence, zero forbidden orientation.|
|Step3 golf|✓ all42 individually addressed, actual automation failures preserved.|
|Step4 reflection|✓ Direct le_index_iff contradiction proves coordinate bounds from nonzero derivative; three lines, no helper or broad weightedOrder conversion. No successful one-tactic replacement demonstrated by the actual entry-goal searches; no claim of global proof minimality.|
|Step5a native diagnostics|✓ complete unfiltered MainLemma/Main/Eval, zero errors/sorries, existing header/unused warnings unchanged.|
|Step5b diff gates|✓ explicit seven-row block above; static exact inverse-diff guards and actual builds.|
|Step6a renames|✓ none for this target; owner queue and four project-end renames untouched.|


Refactoring needed: none for original23. No rename queued/applied; the owner's four project-end rename items are untouched. No meaningful new helper, so no helper-audit handoff was needed. File-wide Phase5/6 and aggregate original27 performance remain owner work.

## Completed actual retained audit

`final23-all-retained`: whole exit0, 391.844s, PGID32617 drained/absent, final e351 pins immutable. Actual discovery yielded 32 written and **21 generated** declarations, all closed full TYPE+opaque VALUE/inferred-type/std3. The 21 generated full AST metadata blocks include private `_private.Roth.MainLemma.0.Roth.coeff_boxPoly._simp_1_2` and private boxPoly.eq_1; counts are observed, not assumed. Full exact list and raw hash: `retained23-actual-summary.json`; raw SHA `300db3c783e89fe39ccdee12ebf033237360e1060bdbcc22ccfb88460ca8d7ee`. Strengthened independent v2 passed separately, including actual private generated descendants.

## Final matched timing results and actual changed-call diagnosis

|Capture|Target ms / actual roots|Complete main ms / actual roots|Whole process s|Raw stdout SHA256|
|---|---|---|---:|---|
|before23-profile|55.106 / 4|5124.358 / 9|216.621|`70edd19526b9fce8f054b2c7c78a8d2e99ffb3b27eefcc8319759aa5bb40a5c0`|
|before23-profile-repeat|48.374 / 4|4955.099 / 9|211.912|`b178d0a1b10fbacd5dc4bee52f161bc0bb2975f915184f4aac121ede234ae33d`|
|final23-profile|41.038 / 4|5058.397 / 9|245.814|`c5c6e404a5650c8e17ff98df8ab4b56059baa7542bf70edde71da52a1ae54d4b`|
|final23-profile-repeat|41.817 / 4|5949.890 / 9|240.174|`438fed13e70b779872273fe372dfc6a0557428f3a512ff86cc39e090334b0f0b`|

The actual changed hγ step (nested inclusive diagnostic, never summed into roots) has samples 42.085, 37.567, 43.112, 64.382 ms in capture order. Paired deltas are +1.027, +26.815 ms; mean +13.921 ms. This change-related cost is retained, not dismissed as noise. Exact raw-line references, all matched control steps, all actual root comparisons, and largest positive/negative deltas are in `main-stages23-diagnostics.json` and `main-nested23-diagnostics.json`.

|Matched control step|Before1/Before2/After1/After2 ms|Mean delta ms|
|---|---|---:|
|`✅️ have hC :`|722.920, 630.464, 652.024, 708.281|+3.461|
|`✅️ obtain ⟨W', hW', W'', hW'', hne, hWeq⟩ :=`|30.844, 33.256, 32.583, 58.694|+13.588|
|`✅️ have hWR := sub_mem_RSet hW' hW'' hne`|1.175, 1.227, 1.227, 4.799|+1.812|
|`✅️ have hΘ :=`|117.612, 116.698, 120.396, 129.078|+7.582|
|`✅️ ·` — final proof branch, actual event #104|584.809, 564.909, 574.739, 918.404|+171.713|
|`✅️ have hsX : 2 < √X :=`|884.088, 900.042, 930.852, 995.368|+71.045|
|`✅️ have h32' : (2 * ((m' + 1 : ℕ) : ℝ) + 1) < δ ^ 2 * Real.log (q 0) := by nlinarith`|472.841, 467.024, 468.078, 563.967|+46.090|

The actual full-main mean is 5039.7285→5504.1435ms: +464.415ms / +9.21508%. This is an unresolved aggregate regression alongside the preexisting over1000ms failure. The unchanged controls are evidence to retain, not grounds for a causal dismissal.

All four whole successful captures are retained, without cherry-picking or an unchanged third sample. Final target passes the1000ms threshold; mandatory repeat was performed because complete main exceeds750ms. Complete main remains over1000ms in all four samples and is an explicit original27/aggregate failure. No unrelated full original27 cleanup is claimed. Whole process/cumulative import timings are preserved separately in raw stderr and are not represented as target root times. No empirical speed ranking against the intermediate DecidableEq variant is claimed; the selected coordinate API removes that instance, has exact old recovery, and has measured final/baseline target performance.

## Final whole CLI/build evidence

Every row has real whole exit0, actual argv/start/end, separate raw streams, fresh17-pin pre/post equality, and an absent process group. Failed and superseded runs remain in the artifact manifest.

|Run|Actual argv|Whole seconds|PGID|Stdout SHA256 / stderr SHA256|
|---|---|---:|---:|---|
|selected23-final-affected|`/Users/ramin/.elan/bin/lake build Roth.MainLemma Roth.Main`|89.565|32334|`0b65c2308f7cab6b485ee0fc77896b1199100ddefd90ebac4e1a2e5a9823381d` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`|
|final23-independent-v2|`/Users/ramin/.elan/bin/lake env lean -j1 /private/tmp/roth-mainlemma-le-index-vanishing/final23-independent-v2.lean`|371.511|32752|`c8224b2f136a05c72ee60da345e8dbd6054941c7540515e4edcdd1ddee6bcca0` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`|
|final23-all-retained|`/Users/ramin/.elan/bin/lake env lean -j1 /private/tmp/roth-mainlemma-le-index-vanishing/all-retained23.lean`|391.844|32617|`300db3c783e89fe39ccdee12ebf033237360e1060bdbcc22ccfb88460ca8d7ee` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`|
|final23-properties-and-inventory|`/Users/ramin/.elan/bin/lake env lean -j1 /private/tmp/roth-mainlemma-le-index-vanishing/final23-properties-and-inventory.lean`|149.936|32902|`9d1d49e31f8ac387b8685035d3726fdd42a9f9ae5ae5f307c2dfc7daae1a7ed7` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`|
|final23-full|`/Users/ramin/.elan/bin/lake build`|62.335|33577|`18110fbdc9b3dfc7a9235646b2d2c58981f5b1ce76561007995967ec51981995` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`|
|final23-Eval-cli|`/Users/ramin/.elan/bin/lake build Roth.LeanEval`|73.134|33640|`7174c03f78e54186bf64bc990a41ed25be414615cf2509524155878db7ed52ee` / `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`|

## Complete unfiltered native observations

|Call|Actual args|Complete result|Request SHA256 / response SHA256|
|---|---|---|---|
|final23-ML|`{"file_path": "/Users/ramin/LEAN/Roth/Roth/MainLemma.lean", "timeout_s": 240}`|success=true, partial=false, timed_out=false; 1 messages, zero errors/sorries|`a8c23858c88c06433424597b4a6aaffc45f50334e1e70b708b1e18f1826d32b5` / `6acc7cbb24b342266f53bec81c7661181bf22984b33255ee1dd3543dbddec80c`|
|final23-Main|`{"file_path": "/Users/ramin/LEAN/Roth/Roth/Main.lean", "timeout_s": 240}`|success=true, partial=false, timed_out=false; 4 messages, zero errors/sorries|`b83f5dd269084d88c8e7e28d21128f69bb702d687b4c96ae3c4c3c4f6bf41c9a` / `25f8be6da8cc28a6dcfede5ce18e387b2241210aeebfbd5526d991565973945a`|
|final23-Eval|`{"file_path": "/Users/ramin/LEAN/Roth/Roth/LeanEval.lean", "timeout_s": 240}`|success=true, partial=false, timed_out=false; 0 messages, zero errors/sorries|`bdc21913c98b618a9b70f07cf50dcf83feaa3b70306fc4c3ee7f52cf71683b63` / `3aab92e3aa1f3570cf31b8dd26a46140808332cff2526d57115fd71a46ae6528`|

All actual native requests were saved before launch with started timestamp; full raw responses have completed timestamps; exact launched source is saved by SHA and each call has fresh before/after17pins. No severity/declaration/range filter was supplied. Existing MainLemma header warning and Main header/three unused-variable warnings are preserved; Eval is clean.

## Final boundary, immutable artifacts, and END

Fresh END17pins equal final17pins; only MainLemma source differs from genuine entry. All104 current compiled/setup/IR companion paths are copied and hashed; exact changed cache paths are recorded in `end23-input-boundary-checks.json`. Fresh package/core availability remains same paths and strict24,782 hashes/3,918,200,888bytes; exact11project intersection and four executable hashes/resolution are retained. All eight actual pre/post profile environments are byte-equal. Late --deps has10 emitted lines/9 unique paths (implicit Init emitted twice), all already genuinely preedit hashed; identical imports, actual frozen CLI environment/config and resolved hashes/bytes are verified. This remains explicitly a late direct-dependency/availability observation, never an exact loaded closure.

[Immutable scratch artifact manifest](/private/tmp/roth-mainlemma-le-index-vanishing/manifest23.json) lists every saved source revision, launched input, raw stdout/stderr, native request/response, fresh pin/cache/env/availability/binary observation, reference copy, failed/superseded candidate, proof/property guard and provenance file, plus this report. It is generated after this report, streamed through strict UTF8 checks with actual binary exceptions, then every listed artifact is freshly rehashed. Self-referential manifest/digest/verification sidecars are explicitly excluded. SHA256 seals and final verification are in `manifest23.sha256` / `manifest23-verification.json`; the owner receives the actual final manifest hash.

Fresh END drain checks every recorded own-leaf PGID by actual killpg0 observation, all absent; count 29. Every native call is complete; no compiler/native/profile job remains. Source e351 is final. All seven exclusive leases are released at END: **target source, target documentation, narrow callers, own report, compiler, native tools, profiler**. Git/shared reports/queues/learnings remained owner-owned and untouched. Owner independent full verification/build/native/Git publication is still required before original24.
