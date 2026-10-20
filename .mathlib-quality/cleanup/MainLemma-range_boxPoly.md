# Original16 — private `Roth.range_boxPoly`

Worker scope is complete for owner review; publication remains owner controlled. Entry HEAD/origin was `1dd1abd0fc2bd0c3ab32b985e8fb6f93feb99beb`, source/audit `1fc499cf21fc91ab2cdb7aecb6fa394036200ca5`. Counts remain231/264 and MainLemma15/27 until owner publication. No Git operations, children, shared progress writes, caller edits, new helper or rename were performed.

The range equality now accepts arbitrary `σ : Type*` with the exact constructor `Fintype σ` and `DecidableEq σ` instances. The reverse direction still constructs ONE bounded coefficient array from the polynomial’s integer coefficients. `Int.toNat_le` supplies its upper bound directly, and supported exponents belong to the box by the coordinate degree bounds. This removes the arithmetic side goal and bad-coordinate detour while preserving exact range=boxFamily meaning.

Source699→694lines, declaration28→23, saved5; proof21lines, forward10/reverse9. Before SHA `817016b9057fbbbedaa9c6db38280bffb9cdbfcdb063b88cba4704c75f89ed48`, final `6808b77320c176564d9d60b450f59ddff6b7b319cc9a03da01dbf2a159a111eb`, target `c04f0e10a4587d1425c2b05112a1049af66f7386a12aed637947b33e281c6b2c`. Main remains685lines/SHA `5f384557dccacaec469699cc7d32bd5666c9d525267e00433b7ae401fee98d09`. All outside-target prefix/suffix bytes,16other source/config pins,3protected helpers, existing docs/quotations/7signposts, and4renamequeue rows are exact (`source-protection16.json`, `source16.diff`). No private docstring was needed or added.

Artifacts resolve under `/private/tmp/roth-mainlemma-range-box-poly/`. `final16-artifact-manifest.json` records actual bytes/SHA/strictUTF8 and explicit compiled binary exceptions; `final16-release.json` binds the report, manifest, source, complete group drain and lease revocation. Self/release hash cycles are excluded. Historical failures and unused harness revisions are retained accurately.

## Phases0–3 — baseline, preparation and scope

Full lean4/mathlib-quality skills, cleanup/cleanup-all/buzz workflows, mandatory references, explicit854-line prompt1–300/301–600/601–854 and112-line profiler instructions were read, recovering truncations. The workflow’s embedded854-line prompt is byte-identical (`worker-prompt-identical.json`). `read-input-provenance16.json` hashes immutable instructions; mutable owner state/ledger observations are historical, with local ledger snapshot and exact owner legacy backup noted separately. The actual fresh16dispatch supersedes prospective draft notes.

Classic Lean dialect. Warm cache retained; no download needed. Normal builds run Mathlib linters; no dedicated runLinter executable is configured. Baseline affected/full builds and full unfiltered nativeML/Main passed before API edits, with0errors and inherited1/4warnings. All17source/config files and104actual project companions/setup files were copied before changes. The full12201import union/1803557376bytes was freshly hash-verified against the accepted15external catalog plus genuine16project BEFORE copies. Direct `--deps` output is recorded separately, never called a full catalog.

Actual imported TYPE+opaqueVALUE `getUsedConstants` inventory v2 exit0 identifies exactly `Roth.boxFamily_finite` and `Roth.ncard_boxFamily`, both VALUE edges. Source and LSP references agree. Full caller types/bodies/order and correct doc attachments are preserved in both profile scopes. No foreign17+ audit or final GLOBAL credit is taken. No additional file-wide source action was needed; owner retains the full-file phases.

## Full24 audit

1. LINT: target none; inherited header warning onlyML. Native Main4inherited warnings remain foreign.
2. HAVE SCAN: anonymous upper coefficient bound in reverse witness, no by, used once by omega→inline via Int.toNat_le. Anonymous monomial_le_degreeOf, no by, used once→compose directly into support-in-box contradiction.
3. SET_OPTION: no target option; no limit changes.
4. SIMP SQUEEZE: none in target; rw/split_ifs preserves canonical dependent coefficient lookup. Whole terminal simp was attempted and did not close the goal.
5. NAMING: range_boxPoly names the range of named DATA boxPoly, accepted lowerCamelCase DATA fragment inside snake_case theorem, no forbidden abbreviation/numeric pattern. No target rename warranted.
6. PACKING: original61chars first line plus complete next conclusion45 gives107>100. Generic first line89 plus conclusion45 gives135>100; final measured table below.
7. BY: correct at end of signature line; preserve.
8. FORMAT: replace mathematical => by↦, keep2space indentation; no haveI/letI/semicolon/blank bodylines.
9. COMMENTS: none target; preserve every outside byte and all7source signposts/originalquotes.
10. DOCSTRING: private lemma; no docstring needed/added.
11. VISIBILITY: private implementation lemma, two same-file consumers, retain private.
12. STRUCTURE:28lines before; forward branch10, reverse15. Genuine proof golf via direct toNat bound and supported-exponent contradiction reduces reverse to9 and the declaration to23lines. No opaque local packaging or substantive helper is needed.
13. MATHLIB: all5methods actually queried. Finder finds as_sum/support_sum_monomial_coeff and FirstOrder.Ring.mvPolynomialSupportLEEquiv; Loogle corrected quoted coeff query and LeanSearch find coefficient APIs. Source/name checks find degreeOf_le_iff, monomial_le_degreeOf, Int.toNat_le. Existing broad equivalence uses unrestricted coefficient functions and a family index, no bounded Fin(B+1) domain; importing/rebundling it would need different DATA/extra wrapper and gives no direct replacement. Reuse existing local coefficient formula and pinned standard degree/support APIs.
14. JUNK DEF: n/a lemma.
15. EXISTS: theorem is range equality; reverse constructs one shared coefficient array, not a trivial single-use existence helper.
16. SHOW: none.
17. PUSH_NEG: original target had push Not, not deprecated push_neg; removed the entire bad-coordinate detour.
18. GENERALISE: arbitrary σ:Type* with matching actual Fintype/DecidableEq constructor classes. Full outer/inner table below. API edit only after complete baseline; class alternatives require actual tests and exact oldFinm transfer, not sameprinting #check.
19. INEQUALITY: complete signature0≥/>; all coefficient degree bounds≤. No reversed orientation/naming.
20. NORMAL-FORM: Set.range(boxPoly)=boxFamily canonical range equality, rewrite consumers use directly.
21. SYNTAX-GEN: retain explicit r/B, no unnecessary Equiv wrapper; arbitrary finite σ aligns constructorAPI.
22. IMPORT-FANOUT: no new import needed or added.
23. CASTS: subtype→multiindex, Nat→Int coefficient casts genuine. Removed redundant annotation `(d : Fin m→₀ℕ)` under coeff expectedtype; retain same coercion in elaboratedTYPEVALUE. Nat.lt_succ_of_le and Int.toNat_le avoid cast arithmetic tactic.
24. INSTANCE-NAME: no instance declarations; anonymous class binders only.

Issues/actions: generalize finite index with actual oldFinm specialization; inline both one-use anonymous haves; direct support contradiction; remove omega/Not detour; mathematical arrows. No unrelatedfile/doc/helper edits.

## All effective outer and inner binders,2.6a–e

|Binder|Role|Candidate, actual verification and disposition|
|---|---|---|
|m:ℕ implicit|finite variable enumeration|σ:Type*, universe-polymorphic finite index; keep oldFinm adapter exactly.|
|σ:Type* universe|indexvariable|Type restricts, Sort invalid for MvPolynomial/Finsupp; keep Type*.|
|Fintypeσ|box enumeration DATA|Direct drop fails Fintype synthesis; Finite.ofFinite body passes std3 but oldFinm adapter TYPE mismatches. Explicit class retained.|
|DecidableEqσ|box construction DATA|Direct drop fails DecidableEq synthesis; scopedClassical body passes std3 but oldFinm adapter TYPE mismatches. Explicit class retained.|
|r:σ→ℕ explicit|coordinate degreebound|Drop loses box and family, scalar/type change changes DATA contract. Retain.|
|r coordinate j:σ|bound function effective innerbinder|Arbitrary σ propagates uniformly; no hypothesis to weaken.|
|B:ℕ explicit|common upper coefficientbound|Drop loses array domain; Intbound would restate construction. Retain.|
|range array c:boxr→Fin(B+1)|shared witness|All coefficients must belong to one assignment; cannot replace by per-exponent ∃. Retain.|
|array d:boxr|monomial domain|Dropping restriction changes polynomial support/range. Retain.|
|subtype exponent d:σ→₀ℕ|finite-support exponent|Arbitraryσ generalizes variables, Finsupp/Nat representation retained.|
|subtype h:d∈boxr|coordinatebound certificate|Essential exact bounded array domain; no proofirrelevance shortcut for DATA.|
|range witness equality|polynomial images|Exact equality needed to establish range, weaker relation changes theorem.|
|W:MvPolynomialσℤ|set extensionality input|Arbitrary integer polynomial, coefficient ring fixed by construction and family.|
|family degree j:σ|∀coordinatebound|Drop/localize changes family; all coordinates needed.|
|family coefficient d:σ→₀ℕ|∀coefficientbounds|Retain lower0≤W.coeffd and upper≤B, both used in witness and cast recovery.|
|hdeg:∀j,degreeOfjW≤rj|reverse membership|Drop permits support outsidebox; retain nonstrictbound.|
|hcoeff:∀d,0≤W.coeffd∧W.coeffd≤B|reverse membership|Drop lower cannot recover Int.toNat, drop upper violates Finbound; point locality cannot reconstruct shared assignment.|
|nonnegative lower 0|coefficient order|Already weak; strictpositive restriction invalid for missing/zero coefficients.|
|upper≤B|coefficient order|Already weak; arbitrary largerbound changes range.|
|support e and he:e∈support|forward degree test|Retain all supported exponents; implied boxmembership derived via coefficient lookup.|
|coeff d and split h:d∈boxr|forward coefficient test|Retain dependent lookup branch; outsidebox is0.|
|reverse ext e and split h:e∈boxr|equality at all exponents|Retain both branches, all indices required for polynomial extensionality.|
|reverse hne:0≠coeffeW|outsidebox contradiction|Exact orientation matters; Ne.symm for mem_support_iff; derive boxmembership from all degreebounds.|

2.6b actual candidate checks completed: generic candidate and all3class-body alternatives pass closedTYPE/VALUE/inferredTYPE/std3; direct class drops fail synthesis and classical/Finite oldFinm adapters fail actualTYPE matching.2.6c genericindex explicitly authorized by dispatch; scalar generalization restates fixed integer construction and is not beneficial here.2.6d three actual literature queries with top3 saved even though private exemption applies; no mathematicsMCP exposed. Polynomial coefficient representation is standard; no stronger premise weakening evidenced.2.6e retain only verified changes. Inversion check: support/coeff APIs standard; the named bounded constructor is essential to range meaning, not an arbitrary object with an unused concrete label.

## All42 golfing rules: final dispositions

|Rule|Status|
|---|---|
|1.1|n/a no byexact wrapper.|
|1.2|n/a no byrfl wrapper.|
|1.3|n/a no rw+exact samegoal simplification currently.|
|1.4|Native whole simp did not close the range equality; explicit coefficient rewrites retained.|
|1.5|n/a no trailingrfl aftersimp.|
|1.6|constructor splits two genuinely different directions; retained after all whole automation attempts failed.|
|1.7|Compose monomialbound directly into mem_box contradiction.|
|1.8|No push_neg; remove existing by_contra+pushNot badcoordinate argument.|
|1.9|Replace mathematical=> by↦; no removable eta lambdas whose body just application.|
|1.10|Inline both one-use anonymoushaves (bound and monomialbound).|
|1.11|n/a original already uses refine+fun; keep commonarray while discharging its bound directly.|
|1.12|n/a noshow.|
|1.13|rintro⟨hdeg,hcoeff⟩ already direct projections, no haveblock.|
|1.14|No consecutiverw samegoal to merge.|
|1.15|No terminalsimponly.|
|1.16|No nonterminalbaresimp.|
|1.17|Use trans composition, mem_box.2, Int.toNat_le.2 direct API.|
|1.18|Remove redundant subtype-to-multiindex typeannotation after the complete generic and class-body checks.|
|1.19|No deprecatedpush_neg; remove pushNot detour.|
|1.20|n/a no trivial existencehelper.|
|2.1|Wholegrind native attempt failed; raw diagnostics preserved.|
|2.2|n/a no existinggrind.|
|2.3|Actual whole simp fails to close the range equality; keep short explicit coefficient proof.|
|2.4|n/a no analysis property.|
|2.5|Existing positivity for coefficientnonneg/zeroupper; retain: direct positivity is already short and fast.|
|2.6|n/a no monotone algebra inequality chain; coordinatebound directtrans.|
|2.7|Replace omega by exact Int.toNat_le+Nat.lt_succ_of_le; actual pinned #check and complete proof validate orientation.|
|2.8|Wholeaesop native attempt failed; raw diagnostics preserved.|
|2.9|Existing exact_mod_cast converts finite coefficientupper; retained: this directly checks the cross-type integer inequality.|
|2.10|n/a arbitrary quantified data, no concrete decidable computation.|
|2.11|n/a no denominators/ring identity.|
|2.12|n/a no ring/ring_nf with hypotheses.|
|2.13|n/a branches are different domainmembership cases, no symmetry.|
|2.14|n/a nocalc.|
|2.15|Two different cases require different mathematics; no repeated parallelgoal closure.|
|3.1|n/a noerw.|
|3.2|n/a no legacy analytic tactics.|
|3.3|Remove omega via directAPI rather than replacing arithmetic tactic.|
|3.4|Forward rintro⟨c,rfl⟩ already substitutes witness equality.|
|3.5|No new global/private attribute needed; explicit existinglookup consumed.|
|3.6|n/a nosimp_allonly.|
|3.7|No targetlimit override; none added.|

## Step4 — Stepback

Search found general reconstruction and broad support equivalences, but neither directly preserves this bounded coefficientarray DATA/range. Direct coefficient extensionality is the natural shortproof. Actual native whole grind/simp/aesop/exact? fail. apply? produces partial suggestions and an empty goal display, rejected entirely under the pinned admitGoal caveat. Positive selected proof passes closedTYPE/actualopaqueVALUE/inferredTYPE/std3 and wholeexit0. No substantive helper is warranted: the forward branch is10lines and reverse9, total23declaration/21bodylines.

## Inequality scan

|Location|≥/> in Lean code|Action|
|---|---|---|
|Full signature plus effectiveinnerbinders|0|n/a no reversedorientation.|

## Steps2.7–2.8 — measured packing and inequality artifacts

Actual width100 private-type #check completed successfully in `final16-packing-native.json`:

```lean
@Roth.range_boxPoly✝ : ∀ {σ : Type u_1} [inst : Fintype σ] [inst_1 : DecidableEq σ] (r : σ → ℕ) (B : ℕ),
  Set.range (Roth.boxPoly✝ r B) = Roth.boxFamily r B
```

Widths below count Unicode codepoints, including indentation; the next complete conclusion clause includes `:= by`.

|Signature line|Chars|Next complete clause|Clause chars|Arithmetic|Action|
|---|---:|---|---:|---|---|
|286, generic parameters|89|`Set.range (boxPoly r B) = boxFamily r B := by`|45|89+1+45=135>100|ok|
|287, conclusion and by|49|none, proof follows|n/a|n/a|ok|

Original first line61 plus1plus45=107>100, so its original break was already justified. No packing defect is falsely counted as fixed. No target line exceeds100.

|Location|≥/> occurrences|Disposition|
|---|---:|---|
|Complete signature and all effective inner hypotheses|0|No rewrite or inequality rename needed.|

## Five-method search and literature evidence

Actual Finder/Loogle/LeanSearch/local-name responses are saved in `search16-*.json`, source search in `search16-source.txt`. Finder located `MvPolynomial.as_sum`, `support_sum_monomial_coeff` and the broad `FirstOrder.Ring.mvPolynomialSupportLEEquiv`. The latter supplies unrestricted coefficient functions/families and would require a new import/domain conversion; it gives no beneficial direct replacement for this fixed bounded Fin(B+1) constructor. Existing coefficient, degree and support APIs supply the short proof directly. No new wrapper/import was added; no global absence claim is inferred from text search alone. Auxiliary coefficient-zero/support/monomial and degree bound variants were searched.

Three real literature queries/top3 were recorded despite the private-declaration exemption; no mathematical MCP was exposed. These are context/search observations, with all technical implementation decisions checked against pinned sources and actual proof gates:

|Query|First3 returned pages|
|---|---|
|multivariate coefficient representation/arbitraryvariables/boundedcoefficients|[Magma introduction](https://docs.magma-maths.org/BasicRings/MultivariatePolynomialRings/introduction.html), [Magma handbook](https://magma.maths.usyd.edu.au/magma/handbook/text/243), [MathWorks coeffs](https://www.mathworks.com/help/symbolic/sym.coeffs.html)|
|monomial basis/coordinate degreebounds/finitebox|[Learn Math Class](https://www.learnmathclass.com/linear-algebra/vector-spaces/basis), [polyrat bases](https://polyrat.readthedocs.io/en/latest/basis.html), [EPFL monomial basis](https://graphsearch.epfl.ch/en/concept/976666)|
|Stacks/polynomialring/monomials/arbitraryvariables|[Stacks0G8Q](https://stacks.math.columbia.edu/tag/0G8Q), [arbitrary variables in ZF](https://math.stackexchange.com/questions/1838860/polynomial-ring-with-arbitrarily-many-variables-in-zf?noredirect=1), [arbitrary index set](https://math.stackexchange.com/questions/1762956/polynomial-ring-indexed-by-an-arbitrary-set)|

Raw responses are `literature16-{0,1,2}.json`. Secondary search hits above are recorded as returned, not used to justify Lean technical facts. No further beneficial premise weakening was evidenced; scalar changes would restate fixed integer DATA.

|New external identifier|Actual verification|
|---|---|
|`Int.toNat_le`|Local positive hit (index warming), pinned Init/Data/Int/LemmasAux.lean110, successful #check and complete generic/independent proofs.|
|`Nat.lt_succ_of_le`|Local returned exact hit while index reported error; honest fallback pinned Init/Prelude.lean2056, successful #check and complete proofs.|

## Phases4–6 — actual contracts, proof values and cumulative gates

`final16-independent-v3.lean` SHA `7157646366e76666c67158f8944ba93566e1942bcab0566faa219b9e22ad62fc` passed wholeexit0 in300.812974083s, nontimeout and drained. Raw SHA `6cfe7d6d42622df1731937a95fecb7406213f8ccef1b6a948e3ead75285e6fb7`.

The entire entry MainLemma body is byte-exact and independently reelaborated. Genuine PROJECToriginal Fin-m boxFamily DATA, private boxPoly DATA, coeff_boxPoly full proof and range_boxPoly full proof are independent bytecopies of project-original.lean704/SHAa3d09825fb878c5d512cfdd3feca517465e0a8215807b1261b988f664915f3a8. Owner caught the prepared v2 original-family reliance before any independent compile; v3 added the original family bytecopy and explicit oldFinm current-family adapter. V1/v2 are unexecuted scaffolds, not passes.

Twelve full exact contracts validate expected/current generic target, explicit original/entry oldFinm target contracts, both complete old direct callers, unchanged constructor/coeff support and original/current-family TYPE plus actual VALUE. Thirty-four closedTYPE/actualopaqueVALUE/inferredTYPE/std3 validations include repeated declarations; this is not a unique-declaration count. Ten independent old TYPE+VALUE closure roots ban current target, both callers, current box/coeff/injectivity/family and all3actual helpers. Five boundary/property theorems cover Fin0, B0, Bool, ULift.{{1}}Bool and the expanded common-array existential membership formulation. Final imported direct inventory again confirms only finite+ncard.

All raw written binder names, order, BinderInfo, universe parameters and full nested TYPE AST are logged and checked, with actual isDefEq and only both-sided generated macroScopes normalized. True private Name objects/fresh universe levels are used. SIX explicitly justified named DATA unfolds are original/entry/current boxPoly and original/entry/current boxFamily; restricted application-spine beta is used, with no changed-arity bareName map or proof-irrelevance shortcut. Theorems are thmInfo, DATA defnInfo. Both TYPE and actual VALUE reject expression/universe metavariables, fvars, loose bvars and sorry; axioms are limited to propext/Classical.choice/Quot.sound. Actual effective limits200000/20000/512; no limit raise, builtin max0 heartbeat counter, sorry/admit or new axiom.

Generic candidate and all3class-body alternatives pass complete compiler/std3 checks. Direct Fintype/DecidableEq drops fail synthesis. Classical/Finite oldFinm adapters fail TYPE matching because constructor DATA instance arguments differ; these are not heartbeat failures, wall timeouts, counterexamples or impossibility claims. Whole grind/simp/aesop/exact? fail; apply? only partial suggestions/empty goal display, rejected under the pinned admission caveat. No partial result from a failed run is used as positive proof evidence.

|Actual command/artifact|Exit|Wall seconds|
|---|---:|---:|
|`before16-affected-build`: `lake build Roth.MainLemma Roth.Main`|0|3.102116|
|`before16-full-build`: `lake build`|0|4.844572|
|`final16-affected-build`: `lake build Roth.MainLemma Roth.Main`|0|75.849397|
|`final16-full-build`: `lake build`|0|42.029810|
|`final16-eval-build`: `lake build Roth.LeanEval`|0|38.560958|

All recorded build groups drained, all17pins immutable, separate stdout/stderr strictUTF8. Fresh native `lean_diagnostic_messages(file_path,timeout_s=240)` for ML/Main/Eval completed success/nonpartial/nontimeout/failed_dependencies[]/0errors and inherited1/4/0warnings; exact unfiltered responses saved in final16-native-*.json and binding metadata.

|Gate|Result/evidence|
|---|---|
|lake_build_file / lake_build|pass; actual affected/full/Eval commands and exit0 above.|
|definition_protected|pass; no sourceDATA changed, exact outside-target bytes.|
|theorem_statement_protected|pass with authorized audit18generalization; exact expectednew and explicit oldFinm recovery.|
|structure_gate|pass;23declaration/21bodylines, forward10/reverse9, no top-level conjunction or new helper.|
|naming_gate|pass; meaningful range of named constructor, no forbidden pattern; no rename.|
|line_packing_gate|pass; complete89/49codepoint table above.|
|inequality_orientation_gate|pass;0≥/> in full signature/hypotheses.|
|comments/docs/staticprotection|pass; none target, every outside byte and3helperSHA/fourqueue rows exact.|
|cumulative_no_unintended_breakage|pass; both actual callers’ full contracts/proofs plus full builds and nativeML/Main/Eval.|
|no-scaffolding/no-limit-raise|pass; source has no added profiling/debug/resource options.|

## Phase5a/5b and Phase6.5 scoped simplify review

Phase5a: authorized generic finite index change and genuine proof golf applied; no other refactor or decompose follow-up needed. Phase5b: no new rename warranted, no queue write, existing4rows stay for project-end single owner pass. No in-place rename.

Scoped holistic self-review outcome PASS-THROUGH: no duplicated skeleton, missing helper, extra import or efficiency change remains. The Claude-Code built-in simplify Skill tool is unavailable; no invocation or fresh independent reviewer is invented. Owner’s later fresh independent whole-file simplify pass remains mandatory, with no foreign/full-file credit claimed here.

## Phase6.6 — matched scoped Buzz

Exact CLI both sides: `lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`. Full target and both direct consumer types/bodies/order are preserved. True flags precede attached docblocks, never separate them from declarations. Canonical source recovery by removing only inserted flags is byte exact. Unique written tokens+separator, exact actual full qualified private proofName and column0disjoint command/async/compiler/kernel/lint roots are verified. Meta/nested/next/trailing-end times are excluded; process drain is separately checked.

|Declaration|BEFORE ms|AFTER ms|Delta ms|
|---|---:|---:|---:|
|`range_boxPoly`|109.494|89.367|-20.127|
|`boxFamily_finite`|8.715|10.640|+1.925|
|`ncard_boxFamily`|16.962|20.568|+3.606|

FAST-BOARD for the scoped target/direct callers. Every row and meaningful combined total stays below750ms, so no frozen repeat trigger fired. No unchanged-source third sample or cherry-pick. No aggregate/project speedup claim; scoped results do not discharge owner’s final GLOBAL all-retained-row gate. No heartbeat counter used. BEFORE raw SHA `ba793721dc14ddfbe86179deef7c7349232557a742f3e90b11cc6e5749d68ce4`, AFTER `6322a6735b8a41519e1d48bbc2ce76dd8458610a2db09ee1cb45e95ea6b91e64`. Scaffold SHA BEFORE `31ac2ac6aee6162fff26eb6fd490ba34724ad4d83300e4eea022f747869df7b9`, AFTER `29e39cbd89894b3ca21464899b6ee89fd223d90a9cabe2987a24dbd1cbee14a2`.

## Setup, provenance, failures and final result

Final17pins/104cache companions/setup are copied and freshly hashed. MainLemma/Main setup bytes match BEFORE; options weak.linter.mathlibStandardSet=true, relaxedAutoImplicit=false, pp.unicode.fun=true, maxSynthPendingDepth=3; packageRoth, classic isModule=false, empty plugins/dynlibs. Full final import union12201artifacts/1803538672bytes freshly verified; exact changed project artifacts are listed in final16-import-summary.json. Actual PATH lake resolution and pinned4.34.0 lean binary/hash are recorded in actual16-resolution.json. Actual environment comparison: byte-identical actual BEFORE/AFTER environment.

Initial BEFORE import summary’s environment_equal compared BEFORE bytes to themselves; that tautology is withdrawn in before16-import-summary-corrected.json, with original metadata preserved. Only final actual comparison supplies cross-phase evidence. Initial API inventory also included2unverified coefficient-zero #checks, failed exit1 and was wholly rejected; corrected v2wholeexit0 supplies accepted inventory. Initial unquoted Loogle query failed and was corrected. Wrong rc2stdlib source path search failed and was corrected to actual pinned4.34.0. These are preserved search/scratch failures, not accepted mathematical or timing evidence. Generic/classbody positive checks and classdrop/oldadapter failures are separately labeled. No profile source failed or overbudget sample occurred. Mutable owner-state/ledger hashes are historical observations, with exact local/owner backups, not immutable current-state claims.

Result28→23lines, saved5; mechanical rules1.7/1.9/1.10/1.18/2.7/3.3 and audit18 generalized index/removed detours. No helper, caller edit, rename, new import, altered constructor DATA, weaker conclusion or trust change. All worker gates pass; no original16publication credit yet.

- [✓] Step1 — required full references/854prompt/112scope read.
- [✓] Step2 — full24audit printed.
- [✓] Step2.5 — all5actual search paths and auxiliary variants recorded.
- [✓] Step2.6 — outer/inner binders, actual probes/contracts/values/axioms, literature top3/inversion check.
- [✓] Step2.7 — complete final packing table and actualwidth100#check.
- [✓] Step2.8 — inequality scan table.
- [✓] Step3 — all42rules individually resolved.
- [✓] Step4 — automation/alternative-strategy stepback completed.
- [✓] Step5a — full fresh unfiltered nativeML/Main/Eval success0errors.
- [✓] Step5b — actual build, diff, exact contract and cumulative gates pass.
- [✓] Step6a — no new rename; existing queue unchanged.

END freezes all artifacts/report/source SHA, drains all owned groups and revokes all target/doc/narrowcaller/report/source/compiler/native/profile leases. Owner review→own FULL→separate Eval/rootEvalnative→exact stage/sourceA+actualhashB/pushclean remain before17. Later full-file27/freshindependentsimplify/GLOBAL/cumulativeALLoriginalpublicDATA+ALLretainedaxioms/importdocscommentsreference gates remain owner scope.
