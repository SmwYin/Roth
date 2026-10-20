# /cleanup Mode B original13 — private DATA `Roth.boxPoly`

Completed original13 worker scope only; owner retains independent review, publication and counting. No original14+ audit credit, helpers, in-place renames, Git operations, or central-progress edits. Entry trusted dispatch HEAD `c710143f359b86251d09a731ec6d223bce01f928`; original264 denominator unchanged. MainLemma707→707lines; DATA declaration3→3lines. Final source SHA256 `8812f171cfb7b6bcb4103e09f0c20cc261d5fc8e39a39ebd3b85d10f5dd41ae0`.

## Phases0–3: doctor, preparation, punch list and scope

Both Lean/mathlib-quality skills, full cleanup/cleanup-all/buzz commands, all mandatory referenced quality files, all854 prompt lines, profiler takeover instructions/current inventory and actual dispatch were read. No applicable AGENTS.md was found in repository/ancestor paths. Baseline affected build `lake build Roth.MainLemma Roth.Main Roth.LeanEval` exited0 in 3.073s; complete unfiltered native ML/Main succeeded with1/4 preserved warnings. Optional cache fetch/linter executable skipped because existing cache/build and native linter evidence were available. Full static lint runs inside compiler roots. Dialect classic.

Actual imported TYPE/VALUE dependencies, source references and complete LSP references were reconciled before editing: five source consumers `coeff_boxPoly`, `boxPoly_injective`, `range_boxPoly`, `boxFamily_finite`, `ncard_boxFamily`. Last two contain inferred direct references missing from source-word search. Generated `boxPoly.eq_1` is associated compiler equation, not a new helper or original. All six complete source declarations were profiled BEFORE API changes. Entire104 actual project-cache companions, all17 source/configuration pins, exact setup/options/package/importArts and environment were saved first; all12201 transitive import artifacts verified through actual frozen setup inventories. Baseline external catalog provenance is explicitly hybrid: accepted immutable original12 external hashes freshly reverified plus actual original13 project BEFORE binary copies. Direct --deps is supplemental only.

Initial actions: investigate Fin m→universe-polymorphic finite σ; preserve integer/bounded coefficient meaning; remove redundant written ascriptions if exact DATA permits; convert the private doc delimiter while preserving exact prose. File-level metadata, imports, other declarations, proof signposts and four queued project-end renames stay under owner scope.

## Phase4: full24 audit

1. LINT: complete unfiltered entry native ML has zero errors, one preserved header warning outside target, no target warning.
2. HAVE SCAN: none; term-mode DATA finite sum.
3. SET_OPTION: none in target.
4. SIMP SQUEEZE: none in target.
5. NAMING: `boxPoly` is descriptive lowerCamelCase data; no forbidden abbreviations/patterns; no rename needed.
6. LINE PACKING: final signature widths93/51; first+next binder93+1+25=119>100, all rows pass below.
7. BY PLACEMENT: term definition; no `by`.
8. FORMAT: term sum with two-space continuation; no empty lines/tactic chains/local instances.
9. COMMENTS: exact prose “The polynomial with coefficient `c d` at each monomial `d` of the box.” survives exactly, with only `/--`→`/-`.
10. DOCSTRING: private definition; converted `/--` to `/-` preserving exact prose.
11. VISIBILITY: private construction used only inside MainLemma; preserve.
12. STRUCTURE: one DATA-body line; no branches/conjunctions/extraction warranted; ordinary≤30/branches≤10.
13. MATHLIB: five actual search methods and compiled generic construction probes required, recorded separately.
14. JUNK DEF: has coeff/injective/range API and multiple callers; retain named constructor.
15. EXISTS LEMMA: n/a DATA definition.
16. SHOW vs CHANGE: none.
17. PUSH_NEG: none.
18. GENERALISE: implemented arbitrary universe-polymorphic finite index after actual probes; explicitly test Fintype/Finite/DecidableEq/classical alternatives; integer output and bounded Fin coefficients encode the finite counting construction and are retained unless concrete evidence supports broader scope.
19. INEQUALITY: no ≥/> in signature; B+1 is type bound, not a reversed inequality.
20. NORMAL-FORM: polynomial is a sum of monomials, standard MvPolynomial normal constructor; no proposition equivalence.
21. SYNTAX-GEN: function from coefficient arrays is needed unapplied for injectivity/range; a data definition is appropriate.
22. IMPORT-FANOUT: no new imports planned.
23. CASTS: subtype d→multiindex; Fin coefficient→Nat→Int are genuine/load-bearing bridges, three written ascriptions removed; all inferred bridges retained with exact raw value AST equality.
24. INSTANCE-NAME: no instance declarations.


### Step2.5 actual five-method mathlib search

[A] Native Lean-Finder: polynomial from coefficients on finite monomials; successful relevant monomial/as_sum/support equivalence results. [B] Native Loogle: MvPolynomial.monomial + Finset.sum; successful as_sum/support_sum/monomial_sum hits. [C] Native LeanSearch: polynomial as sum on finite support; successful sum_def/as_sum/basis hits. Full responses retained in search13-remote.json. [D] Actual complete pinned source searches and untruncated entire-mathlib `boxPoly` search retained. [E] Native local name-pattern search returned monomial hits, index=warming; no absence claim from that index. Auxiliary ofFn/ofFinsupp/onFinset/support-equivalence routes read in actual source. Common-equivalents lookup has no matching disguised predicate. The bundled FirstOrder.Ring.mvPolynomialSupportLEEquiv uses ofCoeff/support proofs and imports model-theory construction; no evidence it simplifies or definitionally preserves this bounded integer constructor. Retain the local name and standard monomial/sum construction with its coefficient/injective/range API. This is not a wrapper lemma and no absence-of-all-mathlib claim is made. Compiled explicit-vs-implicit construction routes give exact raw DATA VALUE equality.

# Step2.6 all effective binders, DATA meaning, literature

2.6a outer and inner binder table:

|Binder|Class/use|Candidates and actual evidence|Result|
|---|---|---|---|
|Original `{m : ℕ}`|Type-shape cardinality indexing `Fin m`|Replace `Fin m` by arbitrary `{σ : Type*}` with box's actual instances; positive generality-v2 TYPE/VALUE specialization guard.|Applied arbitrary σ; old m signature recovered through explicit adapter, never a constant-name arity map.|
|New `{σ : Type*}`|Universe-polymorphic type|`Type` restriction would lose universe generality; `Sort*` is incompatible with Finsupp/MvPolynomial's Type index domain. Positive actual contract/levelParams and final universe adapter inspect all levels.|Keep universe-polymorphic Type*.|
|New `[Fintype σ]`|Finite enumeration in `box r`, including coefficient-array domain|Drop-test corrected negative probe; `[Finite σ]` with Fintype.ofFinite alternative definition elaborates in generality-v2, but genuine old-domain specialization in original probe fails unchanged200000 heartbeat bound.|Keep explicit enumerating instance needed by existing box API and exact verified old specialization. Bound failure is not a mathematical impossibility claim.|
|New `[DecidableEq σ]`|Existing box argument type/data enumeration|Drop without classical tested by corrected negative probe. Open-scoped Classical alternative definition elaborates in generality-v2; original old-domain specialization fails unchanged200000 bound.|Keep explicit instance; noncomputable alone supplies none during binder-type elaboration. No blanket global classical instance introduced.|
|`(r : σ → ℕ)`|Degree bounds determine box/domain|Drop makes domain and sum undefined; point-localisation would no longer enumerate all coordinate constraints. No algebraic/strict→weak hypothesis.|Retain.|
|Arrow input `j : σ` of r|Coordinate index|Arbitrary generic σ already applies; cannot erase function domain while preserving degree vector.|Retain; no hidden Fin m assumption.|
|`(B : ℕ)`|Upper integer coefficient bound via Fin(B+1)|Drop loses coefficient-array type. Replacing ℕ by arbitrary ordered type changes finite counting interpretation; generic ring output would lose integer range/cardinality guarantee, with no concrete downstream benefit.|Retain counting parameter and integer output.|
|`(c : box r → Fin (B+1))`|Coefficient array|Drop loses polynomial coefficients; arbitrary function codomain/domain would change supported bounded integer family. No propositional/typeclass weakening applies.|Retain; function remains unapplied at range/injectivity call sites.|
|Arrow input `d : box r` of c|Bounded monomial index|Replacing by unrestricted finsupp loses finite-array cardinality. Subtype proof is retained and its hidden elaborated occurrences are checked by full TYPE/value equality.|Retain.|
|Sum binder `d : box r`|Complete finite enumeration|Same σ generality applies. Removing box restriction changes support; no lambda eta reduction because both monomial d and coefficient c d depend on it.|Retain finite sum.|

2.6b verification: positive probe13-generality-v2 and probe13-casts exit0 with closed actual TYPE+VALUE, inferred-type and standard-axiom guards. Failed whole generality probe and scratch lookup guard v1 supply no positive acceptance, including any partial PASS. Direct absent-instance probes are separately retained. Actual final original/adapter/generic contract gate is required after imported final build.

2.6c no undecidable preference remains; implemented arbitrary finite index, three omitted ascriptions with identical elaborated value, exact private comment delimiter conversion. Classical-only and hidden Fintype alternatives remain unverified under unchanged bound, not recommended replacements. No coefficients/range semantic restatement, helper, or rename warranted.

2.6d literature: although private scope ordinarily exempts this, three actual web queries were made and full returned results retained as literature13-query0/1/2.txt. Top3 per query: (0) official MvPolynomial.Basic, Variables, CommRing; (1) official Finsupp.Defs, legacy mathlib3 finsupp.defs, sphere-eversion Finsupp.Defs mirror; (2) legacy mathlib3 supported, equiv, official FreeCommRing. Legacy/mirror/variable-support hits are not pinned-library evidence. Actual pinned source searches verify MvPolynomial monomial/sum and FirstOrder.Ring.mvPolynomialSupportLEEquiv; latter bundles polynomial families via ofCoeff and support proofs, gives no simpler definitionally-identical replacement for this bounded integer constructor. Native Finder/Loogle/LeanSearch all returned relevant successful results; local name search returned hits with index=warming, so no index-based absence claim. No ChatGPT-math MCP capability is exposed. Generic ring structures in literature do not justify changing this construction's counting domain.

2.6e keep verified changes. Inversion check: the one-expression body is the actual concrete polynomial construction; it is already directly expressed through mathlib monomial and finite sum. Existing coeff/injective/range API and multiple consumers warrant its local name. There is no long proof hiding a missing abstract theorem/API.

### Packing, orientation and casts

|Signature line|Codepoints|Next complete binder/token|Arithmetic|Action|
|---|---:|---|---|---|
|268|93|`(c : box r → Fin (B + 1))`,25|93+1+25=119>100|ok|
|269|51|none; DATA body follows|n/a|ok|

Definition: #check packing reference n/a (DATA); actual contract/full binder AST is checked independently. Inequality scan: zero ≥/> occurrences in signature/hypotheses; no inequality rename. Casts: three written ascriptions dropped; subtype→finsupp and Fin→Nat→Int coercions still appear identically in elaborated value. No casts deleted semantically. Private comment exact prose unchanged. Body one finite-sum line, zero branches, below ordinary30/branch10. All helper bytes untouched, including exact helper3 SHA8036cf617651d096e302d8f52d4589051c5a213d2ef93c10ee5813de73956a44.

# All42 golf slots; DATA-specific applicability

|Rule|Status and concrete reason|
|---|---|
|1.1 by-exact|n/a: term-mode data, no proof wrapper.|
|1.2 by-rfl|n/a: no reflexivity proof.|
|1.3 rw+exact|n/a: no tactic proof.|
|1.4 simp+exact|n/a: no simp/tactic proof.|
|1.5 trailing rfl|n/a: no tactics.|
|1.6 constructors|n/a: no conjunction/structure proof.|
|1.7 apply+exact|n/a: direct monomial/sum construction.|
|1.8 contradiction|n/a: no proposition proof.|
|1.9 eta|n/a: sum's d appears both as monomial index and in c d; no eta-redex.|
|1.10 single-use have|n/a: no have.|
|1.11 apply+intro|n/a: no tactics.|
|1.12 redundant show|n/a: no show.|
|1.13 obtain|n/a: no have/projections.|
|1.14 merge rw|n/a: no rewriting.|
|1.15 terminal simp|n/a: no simp.|
|1.16 nonterminal simp|n/a: no simp.|
|1.17 dot notation|n/a: monomial has two essential arguments; sum uses canonical notation.|
|1.18 parentheses|applied via cast audit: omit all three written ascriptions and associated parentheses; probe13-casts verifies exact raw elaborated value equality and complete TYPE/VALUE guards.|
|1.19 push_neg|n/a: no tactics.|
|1.20 trivial existential|n/a: DATA, no existential lemma.|
|2.1 whole grind|n/a: DATA construction, arbitrary tactic-produced polynomial would not preserve full value.|
|2.2 delete before grind|n/a: no grind.|
|2.3 simpa|n/a: no proof blocks.|
|2.4 fun_prop|n/a: no analytic predicate.|
|2.5 positivity|n/a: no positivity obligation.|
|2.6 gcongr|n/a: no inequality goal.|
|2.7 lia/omega|n/a: no arithmetic proof; B+1 is a data type index.|
|2.8 aesop|n/a: no propositional proof.|
|2.9 norm_num/norm_cast|n/a: implicit coercion elaboration is checked for exact data-value equality, not a cast proposition.|
|2.10 decide|n/a: no decidable proposition to prove.|
|2.11 field_simp/ring|n/a: no field identity.|
|2.12 linear_combination|n/a: no ring proof with hypotheses.|
|2.13 wlog|n/a: no branches.|
|2.14 calc|n/a: no calculation chain.|
|2.15 multi-goals|n/a: no proof goals.|
|3.1 erw|n/a: no rewrites.|
|3.2 legacy analysis tactics|n/a: no tactics.|
|3.3 omega→lia|n/a: no arithmetic tactics.|
|3.4 rcases-rfl|n/a: no destructuring.|
|3.5 automation registration|n/a: private DATA constructor, existing coeff/inj/range API; no new theorem/attribute warranted.|
|3.6 simp_all|n/a: no simp/proof context.|
|3.7 limit raises|none present or introduced; negative specialization timeouts remain failures under unchanged200000.|

Step4 reflection: constructor already is a single standard finite sum. Mathlib searches found its monomial/sum building blocks and a bundled model-theory equivalence; the latter changes data representation and adds a broad import without an evidenced benefit. Keep local constructor because coefficient, injectivity and range API use it. Arbitrary finite index generality and removal of redundant written ascriptions are concrete improvements; do not invent a tactic proof or helper merely to fill an inapplicable slot. No `exact?`/`apply?` DATA probes: such tactics can produce a different polynomial with the same type, and pinned apply? partial-search admissions are explicitly prohibited. The compiled full original DATA TYPE+VALUE comparison is the meaningful construction-route check.

## Phase5a non-rename / Phase5b rename handling

Implemented evidenced generic finite index and redundant-ascription omission after complete BEFORE gates. No new production helper or caller repair. Entire source outside target+doc is byte-identical; Main remains685lines and unchanged SHA5f384557dccacaec469699cc7d32bd5666c9d525267e00433b7ae401fee98d09. Queue unchanged: Roth.index_hasseDeriv_ge→Roth.index_sub_weight_le_index_hasseDeriv; Roth.B₁→Roth.mainCoeffBound; Roth.log_B₁_gt→Roth.mul_log_div_two_lt_log_mainCoeffBound; Roth.abs_coeff_modByMonic_le→Roth.norm_coeff_modByMonic_le. All defer to the owner's SINGLE project-end pass.

## Phase6 final exact gates

All final source/doc edits preceded actual affected build108.054s and full build36.297s, both exit0/drained/immutable. Final exact imported independent gate `final13-independent-v2.lean` exited0 in122.005s. It independently re-elaborates entire entry MainLemma, independently re-elaborates genuine project-original DATA copied byte-for-byte from704line project-original.lean SHAa3d09825fb878c5d512cfdd3feca517465e0a8215807b1261b988f664915f3a8, and checks:

* Three DATA comparisons: full generic expected TYPE/VALUE versus actual imported defnInfo; genuine old Fin m type/value versus explicit actual-target specialization adapter; entry old type/value versus that adapter. Actual TYPE and VALUE!true isDefEq, full normalized AST equality, actual universe-parameter equality and every written binder name/order/BinderInfo are checked. Only generated macro scopes normalize on BOTH sides; raw full ASTs remain logged.
* All five actual old/current direct caller contracts and complete actual proof TYPE/VALUE closedness/inferred-type/standard-axiom guards. Actual generated equation is validated and independently checks its old Fin m equation adapter; this is a generated target-associated declaration, not introduced helper credit.
* Nine complete contract comparisons, nineteen closed actual TYPE/VALUE guards, seven independent old DATA/caller closure bans. Current target/callers are banned from independent old closures. No self-target proof, sorry/admit/synthetic partial search, metavariables, free variables, loose binders, or nonstandard axioms.
* Explicit true-Name term elaborators construct numeric Name component0 and emit the genuine imported current DATA/equation constants, with fresh levels resolved by the declared contracts. Namespace-only replacement is NOT used for changed boxPoly arity/universe. Only the precisely named old/original/current boxPoly DATA and unchanged old/current boxFamily DATA are unfolded, followed by restricted application-spine beta. `lam/gam/eta/B₁` namespace mappings remain same-arity; no arbitrary binder loosening/rewrite/proof-irrelevance shortcut.
* Separate final names/boundaries gate exits0 in50.196s. Four actual-target applications validate zero variables, zero coefficient bound, Bool variables, and ULift.{1} Bool variables, with closed TYPE/VALUE and standard axioms. Final imported project TYPE/VALUE edge inventory equals the same five source consumers plus actual generated equation. This explicitly verifies exact current Name resolution and no hidden new consumer.

Final complete unfiltered native ML/Main/LeanEval requests (timeout_s240, no severity/range filter) follow all source/build/independent gates and precede AFTER capture; all complete success, nonpartial and nontimeout,0errors. Warnings1/4/0 are the preserved header warning and three Main unused names; no target warning. No source edits follow them. Native raw JSON/binding hashes retained.

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|pass|final13-affected-build actualexit0|
|lake_build|pass|final13-full-build actualexit0|
|definition_protected|pass with declared generalisation|only audited target DATA changed; exact old/new DATA adapter verified|
|theorem_statement_protected|pass|all source caller theorem bytes unchanged, exact actual contracts independently checked|
|structure|pass|one DATA-body line; no branches|
|naming|pass|descriptive lowerCamelCase, no forbidden pattern|
|packing|pass|complete two-row codepoint arithmetic above|
|orientation|pass|zero ≥/> source signature occurrences|
|new identifiers|pass|σ bound locally; Fintype/DecidableEq/monomial existing and actual compiled; omitted coercions exact raw VALUE|
|outside-target/comment preservation|pass|source-protection13.json exact prefixes/suffixes; helper3 exact SHA; all other16pins and rename queue unchanged|
|cumulative breakage|pass|actual five callers, full project and affected native diagnostics; no caller edits|
|trust/options|pass|standard3 axioms only; no limit raise, sorry, admit, new axiom, pin change, or profiling scaffold in source|

## Phase6.5 holistic simplify

No callable built-in simplify tool is exposed. Manual equivalent reuse/quality/efficiency review: one standard finite sum, useful private constructor API, no duplicate proof skeleton or useful extraction. Kept verified index generality/ascription simplification. This scoped review does not substitute for owner's required fresh independent full-file simplify after all27 originals.

## Phase6.6 buzz: matched complete source direct-consumer scopes

Exact CLI on both sides: `lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`. Scope six full original-order declarations with unchanged source bodies/types except audited DATA. No imported-copy substitution. BEFORE 50.898s and AFTER 51.875s are complete file execution times, distinct from declaration metrics.

|Declaration|BEFORE ms|AFTER ms|
|---|---:|---:|
|boxPoly|40.490|48.922|
|coeff_boxPoly|89.174|92.063|
|boxPoly_injective|27.180|28.994|
|range_boxPoly|113.122|111.827|
|boxFamily_finite|10.293|9.976|
|ncard_boxFamily|18.643|19.604|

All target/consumer samples <750ms, so no frozen repeat required; no third capture or cherry-picking. FAST-BOARD for this scope;0limit raises,0slow target/caller deferrals. Only column0 disjoint Elab.command/async roots counted using owner anchored_profile_span.py + verify_profile_roots_exact.py, actual private qualified names, unique complete written name+space marker, all kernel/lint/proof roots; no Meta/nested/next-command/trailing-end double count.

Noncomputable DATA emits zero Lean.compileDecls roots: pinned Lean PreDefinition.Basic135 shouldGenCodeFor excludes modifiers.isNoncomputable, and Main307 dispatches addNonRec instead of addAndCompileNonRec. Raw target command has command+kernel+lint and actual isNoncomputable metadata. Generated boxPoly.eq_1 is lazily realized and kernelchecked inside actual coeff_boxPoly command; its cost stays counted there exactly once. DATA has no source theorem-proof-root requirement. The initial computational-definition exactly-one-compileDecls parser assertion was invalid here, retained as parse13-v1-rejected.py; corrected parser requires actual zero compileDecls for this evidenced noncomputable target and full actual roots. No raw timing was repaired or recaptured for that correction.

These matched intermediate rows do NOT replace final GLOBAL all-row profiling. Previously known GLOBAL δ11188.775ms, pigeonhole1000.235ms and main~5sec remain owner/final-file repair queues; no claim all MainLemma declarations are below budget.

## Evidence provenance, limitations and failed samples

Artifacts live in /private/tmp/roth-mainlemma-box-poly. final13-artifact-manifest.json records actual byte SHA256/size and strict UTF8 or genuine binary exception for every retained artifact and the report; source/config pins, original/reference bytes, tool scripts, raw streams, input scaffolds, actual exit/timeout/drained owned PGIDs included. Full external+project import catalog separate:12201 actual artifacts,1803540728bytes; actual BEFORE104 binary/setup companion copies and final104copies, complete identical setup bytes/options/importArts. Only ML.olean changed in the full resolved import union. Full environment snapshots differ only SHLVL, a shell nesting counter; semantic Lean path/options/pins unchanged, difference recorded exactly rather than claiming identical environment bytes. Direct --deps never stands in for transitive catalog. Shared LSP daemon is persistent and was not killed.

* before13-inventory broad all-library value scan manually stopped after99.599s, exit−15, owned group drained; corrected project-filtered v2 exited0 in48.123s with full raw actual TYPE/VALUE inventory. No timing/semantic acceptance from aborted scan.
* probe13-generality original whole file exit1: classical-only/Finite.ofFinite old-domain specialization attempts reach unchanged200000 heartbeat limit; later unknown-constant diagnostics are consequences. Not impossibility/counterexample evidence. Clean corrected generality-v2 exits0; actual generic old Fin m TYPE/VALUE both true. Definitions of alternatives also validate independently in that successful file, but their original specializations remain unverified.
* probe13-drop-instances v1 uses insufficient imports and is invalid evidence; fully retained. Corrected v2 deliberately exits1 with actual missing Fintype σ and missing DecidableEq σ at argument type/body. Negative tests do not contribute positive PASS.
* final13-independent-v1 exits1 because raw dotted numeric private-name syntax is invalid; even its early expected-new PASS is discarded. v2 corrected actual-Name elaborator exits0 and supplies all positive checks.
* No builtin #count_heartbeats/custom heartbeat probe used. No historical optional count reruns. No additional target/consumer >1000ms performance failures occurred. All raw failed runs retained without partial acceptance.

## Phase7 result and eleven-step checklist

Generalized private box constructor to arbitrary finite universe-polymorphic index; retained explicit existing box instances and bounded integer-array semantics, omitted redundant written ascriptions with exact raw value equality, converted private doc delimiter preserving exact prose.0new helpers,0caller edits,0queued renames,707→707lines,264original denominator unchanged.

|Required worker step|Status|
|---|---|
|1 references/full prompt|complete|
|2 full24 audit|complete|
|2.5 five actual search methods|complete; all outcomes honest|
|2.6 all outer/inner binder generality and literature|complete|
|2.7 complete packing widths|complete|
|2.8 per-occurrence orientation|complete;zero reversed inequalities|
|3 all42 golf statuses|complete|
|4 step-back reflection|complete|
|5a complete native diagnostics|complete;0errors, preserved warnings disclosed|
|5b exact actual diff/build/type/value/trust/performance gates|complete within worker scope|
|6a rename sidecar handling|complete; queue byte-identical, single end pass remains owner|

Final full-file independent simplify/cumulative semantic/public/data/axiom/import/comment checks, full GLOBAL repair/all rows, owner publication/review and all later originals remain mandatory. Carry the explicit validated boxPoly DATA specialization/unfold-beta migration into cumulative scaffolds; old bare Fin-m→generic constant Name replacement is unsound arity mapping. No original completion/count increment until actual owner publication.
