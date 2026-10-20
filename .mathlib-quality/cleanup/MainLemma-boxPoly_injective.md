# Original15 — private `Roth.boxPoly_injective`

Worker scope is complete for owner review; publication remains owner controlled. Entry HEAD/origin was `5688199da32654b6af22e695c786a4ef42a9ccc3` (source/audit `7363ffd707344839aeba9dd84c227292e43ec6bd`). No Git operations, children, shared progress edits, rename writes, or original16 audit were performed. Counts remain230/264 and MainLemma14/27 until owner publication. Actual dispatch supersedes prospective text in the saved draft.

The lemma now accepts arbitrary `σ : Type*` with the exact `Fintype σ` and `DecidableEq σ` constructor instances. Its bounded coefficient array and integer polynomial DATA are unchanged. Recovering a coefficient from the polynomial equality, then applying `Fin.ext`, proves injectivity in three source lines rather than six. No substantive helper was introduced; no helper audit credit is claimed.

```lean
private lemma boxPoly_injective {σ : Type*} [Fintype σ] [DecidableEq σ] (r : σ → ℕ) (B : ℕ) :
    Function.Injective (boxPoly r B) := fun c c' hcc' ↦ funext fun d ↦ Fin.ext <| by
  simpa [coeff_boxPoly, d.2] using congrArg (fun W ↦ W.coeff d) hcc'
```

Source `Roth/MainLemma.lean`:702→699 lines; declaration6→3, saved3. Source SHA before `a2f7c750073759a03b09f9400705f87ade7c5c18aa568fc3d72a6cf0451a15c8`, after `817016b9057fbbbedaa9c6db38280bffb9cdbfcdb063b88cba4704c75f89ed48`. Final target SHA `e80f006043add36d86ad1bc51493a0ca1c4734988cb5d1fc3c46c498242a65ad`. Main remains685 lines, SHA `5f384557dccacaec469699cc7d32bd5666c9d525267e00433b7ae401fee98d09`.

Artifacts are under `/private/tmp/roth-mainlemma-box-poly-injective/`; every relative artifact name below resolves there. `final15-artifact-manifest.json` records actual byte counts/SHA256 and strict UTF8 results, including explicit binary exceptions. `final15-release.json` separately binds that manifest, this report and the final source, and records final process-group drain and lease revocation. The manifest excludes itself and the final release to avoid a hash cycle. Historical attempts and unused scaffolds are retained, never silently relabeled as passes.

## Baseline (Phase0), inventory (Phase1), and file-level scope (Phase3)

All required skills, workflows, references, full854-line worker prompt in explicit1–300/301–600/601–854 ranges, and full112-line future profiler instructions were read, recovering truncations. `read-input-provenance15.json` records hashes at read time, including mutable owner state as a historical observation rather than an immutable current-state assertion. Dialect is classic Lean. No additional file-wide change was needed in this declaration-only dispatch.

Before any API edit: affected build and full build passed; full unfiltered native MainLemma/Main completed successfully with0 errors and inherited warnings1/4. MainLemma native raw is saved; the baseline Main native response remains in tool history, not a separately saved raw artifact. Seventeen source/config files and104 actual project cache artifacts, including companions/setup, were copied. `before15-complete-import-catalog.json` freshly hashed all12201 imported artifacts (1803555232 bytes), honestly reusing original14 external catalog provenance only after actual hash verification; project BEFORE copies are original15's own. `before15-deps.log` is a direct dependency list and is not represented as the full import catalog.

Source search, corrected LSP references at declaration line282, and actual imported TYPE plus opaque VALUE `getUsedConstants` direct-edge inventory agree: the sole actual direct consumer is `Roth.ncard_boxFamily`. It is included in full, with type, body, and source order, in both matched profile scopes. The incorrect first LSP query targeted `Function.Injective` on line283 and is rejected as target inventory evidence. Final imported inventory is independently rerun in the complete semantic harness; transitive consumers are not mislabeled direct.

## Audit (Phase2), full24 items

1. LINT: native full file success nonpartial nontimeout, no target warning; one inherited header warning.
2. HAVE: L285 h := congrArg ..., no by, used once as cast premise after simp; inline via terminal simpa.
3. SET_OPTION: none target; limits unchanged.
4. SIMP SQUEEZE: original nonterminal simp only correctly explicit; consolidate with final cast conversion.
5. NAMING: boxPoly_injective states injectivity of the named boxPoly constructor; named DATA fragment lowerCamelCase preserved inside standard property suffix, no forbidden abbreviation or numbered pattern. No rename.
6. PACKING: final measured table below passes. Correction to historical initial audit: original L282 width65; the complete next conclusion has32 characters, and its ` :=` has3 more. Thus65+1+35=101>100; the original break was justified. No packing defect is claimed. Final generic first line93 plus next complete clause35 also cannot fit.
7. BY: already ends line, preserve.
8. FORMAT: two-space proof, no blank lines; change mathematical lambda arrows to ↦. No haveI/letI.
9. COMMENTS: target has none; preserve all outside prose/signposts.
10. DOCSTRING: private lemma, none required or added.
11. VISIBILITY: private property of private constructor used locally, preserve.
12. STRUCTURE: six target lines, four tactic-body lines; no conjunction or long branch/helper need.
13. MATHLIB: actual Finder/Loogle/LeanSearch/local-name searches find coefficient extensionality and Int.natCast_inj, source search finds actual standard cast theorem. No replacement about private constructor; use existing coefficient formula. Full search evidence retained.
14. JUNK DEF: n/a lemma.
15. EXISTS: n/a injectivity, no existential.
16. SHOW: none.
17. PUSH_NEG: none.
18. GENERALISE: test arbitrary σ Type* matching current boxPoly and coeff_boxPoly, Fintype/DecidableEq drop and alternatives, all outer and expanded inner binders; preserve old Fin m specialization and actual integer bounded array semantics.
19. INEQUALITY: no ≥/> in signature or hypotheses, no inequality rename.
20. NORMAL-FORM: Function.Injective is canonical and caller consumes it directly.
21. SYNTAX-GEN: keep explicit r/B and implicit equality arguments provided by Injective; arbitrary finite σ allows natural existing constructor API.
22. IMPORT-FANOUT: no new imports planned.
23. CASTS: original d subtype→multiindex coercion genuine; test dropping ascription if expected coeff domain supplies it. Integer→natural cast inference handled by actual Int.natCast_inj, no changed DATA.
24. INSTANCE-NAME: no declared instances, anonymous class binders only.

Issues: remove Fin m restriction if complete verified; inline single-use have; use ↦; test direct cast lemma/simpa and automation. No helper expected. No undecidable preference found.


## Step2.5 — five actual mathlib searches

|Path|Actual result and use|
|---|---|
|LeanFinder|Coefficient-array injectivity query returned `Polynomial.injective_ofFn`, `Polynomial.coeff_injective`, and partial MvPolynomial embeddings. No hit directly states the private constructor property.|
|Loogle|Quoted coeff/injective query returned generic monoid-algebra and univariate coefficient APIs.|
|LeanSearch|Coefficient uniqueness/cast query returned partial power-series and natural-cast polynomial analogues.|
|Pinned source `rg`|Searched coeff/injective, monomial/sum variants, `natCast_inj`/`ofNat_inj`, and `Fin.ext`; canonical `Int.natCast_inj` is present.|
|Local name search|Positive `Int.natCast_inj` hit; index warming does not establish negative absence.|

`search15.json` and `source-search15.json` plus separate raw source-search outputs preserve the queries/results. Common equivalent statements: coefficient equality, coefficient-array extensionality, injective natural-to-integer cast, monomial sum support. No relevant topology/bornology translation applies. Standard coefficient congruence, `Fin.ext`, and cast simplification are reused; no new wrapper or broad basis import is needed.

### Step2.6d — literature top3 and inversion check

Three actual web queries were made despite the private-declaration exemption. Search response snapshots are `literature15-query0.json`, `literature15-query1.json`, `literature15-query2.json`.

|Query purpose|First three returned pages|Assessment|
|---|---|---|
|Multivariate-polynomial coefficient uniqueness|[mathlib phrasebook](https://leanprover-community.github.io/mathlib-phrasebook/Polynomials/Multivariate-polynomials/), [legacy basic docs](https://leanprover-community.github.io/mathlib_docs/data/mv_polynomial/basic.html), [current Basic docs](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Basic.html)|Supports the standard coefficient representation; actual code decisions checked against pinned source and compiler.|
|Finite monomial sums and coefficients|[ProofWiki multiple variables](https://proofwiki.org/wiki/Definition%3AMonomial_of_Polynomial_Ring/Multiple_Variables), [alternate path](https://proofwiki.org/wiki/Definition%3AMonomial_of_Polynomial_Ring_in_Multiple_Variables), [definition2](https://proofwiki.org/wiki/Definition%3AMonomial_of_Polynomial_Ring/Multiple_Variables/Definition_2)|Duplicate definition results; no stronger reusable theorem inferred or technical implementation based on these.|
|Polynomial-algebra coefficient/basis generality|[Stacks0G8Q](https://stacks.math.columbia.edu/tag/0G8Q), [Stacks book](https://stacks.math.columbia.edu/download/book.pdf), [Stacks algebra](https://stacks.math.columbia.edu/download/algebra.pdf)|Broad context, not a constructor-specific replacement; no relevant new premise weakening evidenced.|

No mathematics MCP was exposed. Inversion check reduces the proof to standard coefficient extraction and injective integer cast. A new helper would only wrap existing APIs. Finite index generalization is the useful change, verified below; scalar-ring generalization would change the fixed integer DATA and is outside this constructor contract.

## All42 golfing statuses

|Rule|Status/action|
|---|---|
|1.1 by exact|n/a: original is multistep coefficient/extensionality proof.|
|1.2 by rfl|n/a: no rfl wrapper.|
|1.3 rw+exact|n/a: no rw followed by exact.|
|1.4 simp+exact|Consolidate nonterminal simp and final cast into terminal simpa using coefficient congruence.|
|1.5 trailing rfl|n/a: none.|
|1.6 constructor|n/a: injectivity has no conjunction-constructor chain.|
|1.7 apply+exact|Try explicit Fin.ext followed by cast equality, then composed term Fin.ext.|
|1.8 contradiction|n/a: no by_contra/push_neg.|
|1.9 eta|Change mathematical arrows to ↦; coefficient lambda genuinely depends on W.|
|1.10 have|Inline sole one-use h from congrArg into simpa using.|
|1.11 apply+intro|n/a: Fin.ext changes equality to natural values; no following intro.|
|1.12 show|n/a: no show.|
|1.13 have projections|n/a: no conjunction projections.|
|1.14 merge rw|n/a: no sequential rewrites.|
|1.15 terminal simp|Terminal broad simpa selected after actual complete preflight24.782ms vs explicit15.513ms; both fast, broad idiomatic and one proof line, no squeeze-performance exception needed.|
|1.16 nonterminal simp|Original nonterminal simp only already squeezed; terminal consolidation removes this step.|
|1.17 dot notation|Fin.ext is canonical constructor/ext lemma, Int.natCast_inj standard iff; no receiver-style improvement.|
|1.18 parenthesis|Test dropping subtype-to-multiindex ascription and use Fin.ext <| by term.|
|1.19 push_neg|n/a: none.|
|1.20 trivial existential|n/a: no existential.|
|2.1 grind|Actual whole-goal native attempt fails; coefficient expression does not become c=c' automatically. Scratch bounded whole-proof retry retained.|
|2.2 delete before grind|n/a: no selected grind.|
|2.3 simpa|Generic explicit Int.natCast_inj variant and broad terminal simpa both pass full closedTYPE/VALUE/std3; broad selected, terminal consolidation applied.|
|2.4 fun_prop|n/a: no analytic property.|
|2.5 positivity|n/a: equality goal, no sign premise.|
|2.6 gcongr|n/a: no inequality or monotonicity.|
|2.7 lia/omega|n/a: no arithmetic inequality; cast equality has direct standard injectivity lemma.|
|2.8 aesop|Actual native whole-goal attempt fails without coefficient extraction; scratch negative retained.|
|2.9 norm_num/norm_cast|Replace original exact_mod_cast with actual Int.natCast_inj; generic candidate passes. No concrete numeric computation.|
|2.10 decide|n/a: theorem quantifies arbitrary arrays, variables and bounds; no finite concrete decision goal.|
|2.11 field_simp/ring|n/a: no denominator/ring expression identity.|
|2.12 linear_combination|n/a: no ring/ring_nf block with algebraic hypotheses.|
|2.13 wlog|n/a: no symmetric case branches.|
|2.14 calc|n/a: no calc.|
|2.15 multiple goals|n/a: no parallel goals with repeated closing tactics.|
|3.1 erw|n/a: none.|
|3.2 legacy analysis|n/a: none.|
|3.3 omega→lia|n/a: no omega in target.|
|3.4 rcases rfl|n/a: none.|
|3.5 attributes|No new attribute: private constructor-specific injectivity is supplied directly to Set.ncard_range_of_injective.|
|3.6 simp_all|n/a: no simp_all only; one congruence premise enough.|
|3.7 options|No limit raise or override present/added; defaults retained in all scratch compilations.|

Step4: native whole grind/simp/aesop fail; exact? finds no full proof; apply? produces partial suggestions and a misleading empty-goal state, rejected entirely under pinned admitGoal caveat. The existing coefficient lookup is the relevant API; no new helper or broad basis import needed. Term composition and direct natural-to-integer injectivity are the natural proof. No claim that evaluation equality determines a polynomial is used.

## Generalisation2.6a–e, all effective outer and inner binders

|Binder|Class/use|Candidate/drop test|Resolution|
|---|---|---|---|
|old m:ℕ implicit|Fin m cardinality index|Arbitrary σ Type* with published construction instances|Generic-v1 actual compiler exit0 closedTYPE/actualVALUE/std3; old Fin m exact adapter checked in final independent gate.|
|σ:Type* and universe|variable index|Retain universe polymorphism; Type would restrict, Sort constrained to Type by MvPolynomial/Finsupp/Fintype|Expectednew full TYPE AST and ULift boundary probe required.|
|Fintype σ|finite box enumeration DATA|Direct drop; Finite.ofFinite plus classical alternative|Directdrop fails class synthesis; alternative body compiles but old Fin m adapter TYPE mismatch, different constructor instance DATA. Explicit Fintype retained.|
|DecidableEq σ|constructor box DATA choice|Direct drop; scoped Classical alternative|Directdrop fails class synthesis; classical body compiles but old Fin m adapter TYPE mismatch, different constructor instance DATA. Explicit DecidableEq retained.|
|r:σ→ℕ|entire degree-bound function|Dropping r removes box r; coordinate-point locality changes domain|Retain exact bound function.|
|r arrow coordinate a:σ|function domain|same arbitrary σ; no independent premise|Retain generalized σ domain and Nat values.|
|B:ℕ|Fin(B+1) coefficient bound|Dropping B loses bounded-array type; changing coefficient ring restates fixed integer constructor|Retain exact integer/bounded-array semantics.|
|Injective implicit arrays a₁/a₂|functions box r→Fin(B+1)|Unfold Injective and inspect complete TYPE; arbitrary arrays essential|Retain both equality inputs, no pointwise restriction.|
|array arrow coordinate d:box r|monomial subtype domain|Removing box restriction changes support/cardinality|Retain exact subtype domain.|
|subtype value x:σ→₀ℕ|finite support exponent|Arbitrary σ applied; unrestricted functions change polynomial monomials|Retain Finsupp/Nat representation.|
|subtype membership witness x∈box r|bound certificate|Dropping it changes domain; proof irrelevance never used to bypass DATA validation|Retain.|
|injectivity equality hcc'|proposition polynomial images equal|Drop cannot prove equality of arbitrary arrays; weaker relation changes injectivity|Retain exact equality.|
|output equality c=c'|function extensional equality|Restate as pointwise iff? Existing Injective directly consumed|Keep canonical conclusion.|
|local c,c',hcc'|proof lambda names|No extra theorem assumption, instantiate Injective inputs|Preserve mathematical meaning; arrows ↦.|
|local d|function extensionality coordinate|Every coefficient needed to recover array|Retain local funext lambda; composed funext/Fin.ext term passes and selected.|
|local W|congrArg polynomial variable|Remove would lose coefficient projection|Retain coefficient function; explicit d coercion annotation removed after positive compiler gate; inference preserves same subtype-to-multiindex coercion.|
|sum d in underlying DATA|finite enumeration|Existing construction protected, no source edit|Validated by named DATA unfolding and restricted spine beta.|

No scalar ring/typeclass hierarchy, sign/strict premise, pointwise analytic premise or bundled conjunction to weaken. Inversion check: coefficient recovery is abstract extensionality plus injective cast, both standard APIs; no missing abstraction warrants a new substantive helper.2.6c generic index change explicitly authorized by actual dispatch; no unresolved preference.2.6b all positive selections require full compiler exit0 and exact oldadapter/expectednew TYPE AST; failed recovery is UNVERIFIED, not a counterexample.2.6d despite private exemption three real queries/top3 retained, no math MCP exposed.2.6e keep only completely verified changes.


## Steps2.7–2.8 — final packing and inequality artifacts

Packing counts Unicode codepoints, including indentation. The signature ends before the proof lambda on physical line283. The full physical line is also recorded to make the distinction explicit.

|Source line|Final signature text/extent|Width|Next complete clause including ` :=`|Width|Would fit≤100?|Action|
|---|---|---:|---|---:|---|---|
|282|`private lemma boxPoly_injective {σ : Type*} [Fintype σ] [DecidableEq σ] (r : σ → ℕ) (B : ℕ) :`|93|`Function.Injective (boxPoly r B) :=`|35|No,129|Keep break.|
|283|`    Function.Injective (boxPoly r B) :=` (signature extent)|39|none|n/a|n/a|Proof starts on same line; full physical width84.|

The final proof line has width68. No line exceeds100. Correction to initial historical estimate: old first line65 plus a space plus complete conclusion32 plus ` :=`3 is101, so the old signature break was justified. The saved initial audit's claim of underpacking is withdrawn; this final table governs the gate.

|Signature/hypothesis location|`≥`/`>` occurrences|Disposition|
|---|---:|---|
|Complete target signature, including expanded effective binders|0|n/a: equality/injectivity statement; no orientation or `_ge_`/`_gt_` rename.|

## Phase4 verification and candidate evidence

All attempted positive proof/class alternatives received actual compiler checks; no zero-goal display was accepted as a closed proof. `probe15-generic-v1` passed in51.929s, `probe15-classes` in56.588s, `probe15-positive` in51.351s. Explicit `Int.natCast_inj` and composed `funext`/`Fin.ext` candidates pass closed actual TYPE/VALUE, inferred type, and standard-axiom checks. Direct omission of `Fintype` or `DecidableEq` fails class synthesis. Classical/`Finite.ofFinite` bodies compile, but their old `Fin m` adapters fail actual TYPE matching because constructor instance DATA differs. These are rejected API alternatives, not mathematical counterexamples and not heartbeat timeouts.

Whole-goal `grind`, `simp`, `aesop`, `exact?`, and `apply?` were actually attempted. The bounded scratch negative batch exits1 and preserves failures; in particular `apply?` can display empty goals through synthetic admission, and the resulting sorry warning makes it invalid. All partial successes within that failed batch are rejected. No `sorry`, `admit`, new axiom, weakened conclusion, limit raise, or builtin heartbeat counter was introduced. Actual limits remain200000 heartbeats/20000 synthInstance/512 maxRecDepth.

Preflight `probe15-preflight` used the exact profiler CLI and completed exit0: explicit narrow cast proof15.513ms and terminal broad simpa24.782ms, each complete and closed. This is selection evidence in a small context, not a matched speedup. The conventional one-line terminal `simpa` was selected; its measured cost is small. The final matched whole-target/caller rows below are the performance result.

### Phase4 gate status — `boxPoly_injective`

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|pass|Affected and full builds exit0; no deferral.|
|definition_protected|pass|No supporting DATA declaration edited; exact prefix/suffix outside target.|
|theorem_statement_protected|pass, authorized audit18 generalization|Exact generic expected contract and exact old `Fin m` adapter validated with actual DATA unfolding/isDefEq.|
|structure_gate|pass|Three-line declaration, one tactic-body line, no conjunction/branch, ordinary≤30/branch≤10; no helper/decompose flag.|
|naming_gate|pass|`boxPoly_injective` names a property of the named constructor, standard suffix and meaningful DATA fragment, no abbreviation/number/forbidden pattern.|
|line_packing_gate|pass|Final measured table above;129 cannot fit100.|
|inequality_orientation_gate|pass|0 occurrences in full signature/effective hypotheses.|
|comments/docs/prose|pass|None in target; all outside comments, original quotations, helper/signpost bytes exact. Private lemma needs no new docstring.|
|cumulative_no_unintended_breakage|pass|Full project and Eval builds, independent caller/type/value gates, fresh complete nativeML/Main/Eval.|

Overall: pass for worker scope, pending owner publication.

## Verification (Phase6) — independent exact contracts and original proof

`final15-independent-and-boundaries-v3.lean` SHA `070b88d0a472234f742a402911cf6df8535e62139808dcb3bec58925f999c31e` completed actual exit0 in272.771639333s, nontimeout and drained. Raw SHA `853de3d41e5970661ba2227c25f7123b1a4ba3dbface25e964e777983c7b1ff4`.

The genuine project-original target, old private `boxPoly`, and old `coeff_boxPoly` are byte copies of `/private/tmp/roth-mainlemma-owner/project-original.lean` SHA `a3d09825fb878c5d512cfdd3feca517465e0a8215807b1261b988f664915f3a8`, independently reelaborated. The entire entry MainLemma body is also byte-copied and independently reelaborated. `final15-construction-v3.json` records exact copied byte hashes. Current target/caller/box/coeff and actual current substantive helper Names are banned in the seven old proof closures; the current lemma is never substituted for the original proof.

Nine exact contracts cover expected/current generic box DATA, entry/current box DATA, original coeff/old contract, entry/current coeff, original box/old DATA contract, expected/current generic injectivity, original injectivity/old `Fin m` contract, entry injectivity/old `Fin m` contract, and entry/current direct caller. Twenty-five declarations pass complete actual TYPE and opaque VALUE checks: no expression/universe metavariables, fvars, loose variables, sorry; inferred type matches and only `propext`, `Classical.choice`, `Quot.sound` axioms are allowed. Seven independent old closures and four boundary applications pass: `Fin 0`, `B=0`, `Bool`, and universe-polymorphic `ULift.{1} Bool`.

Actual private Names are resolved as Name objects through elaborators with fresh universe levels. Five named DATA bodies are explicitly validated/unfolded with restricted application-spine beta, rather than using a changed-arity bare Name map or proof irrelevance. Raw written binder names, order, BinderInfo, universe parameters, complete nested dependent TYPEAST, and actual `isDefEq` pass; only generated macroScopes are normalized on both sides. Lemmas are `.thmInfo`, DATA is `.defnInfo`. Original integer coefficient witnesses/branches and bounded coefficient arrays are preserved.

The supplemental `final15-expanded-binders.lean` explicitly expands effective `Function.Injective` array/equality binders with `forallTelescopeReducing`, logs raw actual/expected/old `Fin m` types, and checks exact AST/isDefEq plus closedTYPEVALUE/std3. Actual exit0 in87.747877s; raw SHA `4f1b080ec10813460e281b9947f3c70f2d6ec2b1d9b716af6317cb025ec2684c`. No source changed between these gates and matched AFTER.

### Actual build and native results

|Artifact/command|Exit/status|Wall seconds/details|
|---|---|---|
|`before15-build`: `lake build Roth.MainLemma Roth.Main`|0|6.381541458; nontimeout, owned group drained.|
|`before15-full-build`: `lake build`|0|5.376196084; nontimeout, owned group drained.|
|`final15-affected-build`: `lake build Roth.MainLemma Roth.Main`|0|90.504192625; nontimeout, owned group drained.|
|`final15-full-build`: `lake build`|0|40.553821000; nontimeout, owned group drained.|
|`final15-eval-build`: `lake build Roth.LeanEval`|0|38.022494500; nontimeout, owned group drained.|
|Fresh native MainLemma, `lean_diagnostic_messages(file_path, timeout_s=240)`|success, complete, nonpartial, nontimeout|0 errors,1 inherited warning.|
|Fresh native Main, same unfiltered request|success, complete, nonpartial, nontimeout|0 errors,4 inherited warnings.|
|Fresh native LeanEval, same unfiltered request|success, complete, nonpartial, nontimeout|0 errors,0 warnings.|

Exact native responses, arguments, and17source/104cache binding are in `final15-native-{ml,main,eval}.json` and `final15-native-binding.json`. No severity/range filtering or partial timeout result is accepted. All failed dependencies lists are empty. No inherited warning is attributed to the target.

## Simplify pass (Phase6.5), scoped review

Outcome: PASS-THROUGH in worker self-review. The Claude-Code built-in `/simplify` Skill tool is unavailable in this Codex environment; this report does not invent an invocation or independent reviewer. The required scoped holistic review was performed directly: coefficient extraction is already the shared API, no repeated skeleton warrants a helper, and the composed proof is clear and fast. Issues identified: none beyond audited/generalized/golfed changes; fixes after final gates: none; files changed by review: none. The fresh independent whole-file simplify review remains explicitly in the owner's later full-file scope; no foreign or full-file credit is taken here.

## Buzz pass (Phase6.6) — actual matched scoped FAST-BOARD

Both scopes preserve the full target and complete direct caller types/bodies/order, with profiler trace settings bracketing whole commands and including the caller docstring correctly. Exact CLI for each is `lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`. BEFORE scaffold SHA `c1cf24f0e98ece0799dae2572ac512ee1da1e3e85572f0fca32816433c8652fc`; AFTER `cf8aaf169a0417261e5d9486c317787852a4563aa019c6c9c472e46849d287d4`. Uninstrumented source recovery is byte exact. Both scopes use unique written declaration tokens plus separator and exact actual fully qualified proof Names; frozen owner parsers verify complete column0 disjoint command/proof/kernel/lint roots. Nested Meta events, nested descendants, next commands and trailing `end` are excluded. No invented metadata or duplicated generated roots.

|Declaration|BEFORE ms|AFTER ms|Delta ms|Disposition|
|---|---:|---:|---:|---|
|`_private._stdin.0.Roth.boxPoly_injective`|27.752|46.624|+18.872|FAST-BOARD, below750ms repeat and1000ms goal.|
|`Roth.ncard_boxFamily` sole direct caller|16.982|19.117|+2.135|FAST-BOARD, below thresholds.|

No speedup is claimed. No unchanged-source third run or favorable sample selection occurred. Neither target nor direct caller reached750ms, so the mandatory frozen BEFORE+AFTER repeat trigger did not fire. These scoped rows are not final GLOBAL results or a project aggregate. Final GLOBAL all retained rows/δ remains owner full-file work.

Accepted BEFORE `before15-v2-first`: actual exit0,42.963897166s, raw SHA `90fe790776919d74ccf6f32a28112a9689dd79f66cff89208515266529671e41`. AFTER `final15-after-first`: actual exit0,45.221965250s, raw SHA `437512cfa07ae3d56e480c319e142bd0ec572464b1c5eb58e21db54bbc9c2c4f`. Separate strictUTF8 stdout/stderr, source17pins, source/scaffold SHA, timeout and drainedPGID evidence are saved in each runner JSON; `*-timing.json` and `*-complete.json` prove exact root completeness rather than process drain, which is separately checked by the runner/release.

## Preserved failures and unexecuted prospects

- Initial runner argument placement accidentally treated `--timeout` as the program; compiler never started. Empty streams and rejection metadata are preserved in `rejected-preflight-attempts15.json`; no timing credit.
- `before15-first-valid` exits1 because a profiler flag was inserted between the direct caller's docstring and theorem. All timing is rejected. The corrected v2 scaffold moves the flag before the docstring.
- Direct instance-drop and whole automation failures remain in `probe15-negative.*`; classical/Finite old adapters in `probe15-classes-old.*` fail TYPE matching. All failed scratch compiler samples remain immutable; no partial PASS counts.
- Earlier semantic v1/v2 and `full-project15-inventory.lean`/`before15-isolated-env.json` are unexecuted scaffolds/prospects, not verification gates. The accepted final v3 imported direct inventory, source and LSP evidence suffice for the actual private target.
- An ordinary process diagnostic was denied by the sandbox; a later explicitly permitted read-only process check succeeded. Neither is counted as a Lean gate or a build failure. No automatic approval rejection remains unresolved.

## Setup, import catalog, pins, and immutability

`final15-pins.json` and `final15-cache.json` bind all17source/config and104 actual project artifacts. All16 nontarget source/config pins, exact target prefix/suffix, supporting DATA, comments/docstrings, original quotations and signposts are unchanged (`source-protection15.json`, `source15.diff`). No helper/caller/import edit. Three previously audited substantive helpers remain byte protected, without original15 helper credit.

MainLemma/Main setup JSON bytes match their BEFORE copies exactly: options `weak.linter.mathlibStandardSet=true`, `relaxedAutoImplicit=false`, `pp.unicode.fun=true`, `maxSynthPendingDepth=3`; package `Roth`, exact module names, `isModule=false`, empty plugins and dynlibs. Full final import union12201 artifacts/1803557376 bytes is freshly hashed in `final15-complete-import-catalog.json`. Only project `MainLemma.olean` differs from the BEFORE import union. Compiled import binary artifacts are actual strictUTF8 failures recorded as binary exceptions; direct dependency output is kept distinct.

Raw environment bytes differ only in `SHLVL`1→2 due to shell nesting (`environment15-comparison.json`); `LEAN_PATH`, `PATH`, and all Lean resolution variables match. Byte-identical environment is not claimed. CLI options, setup/import resolution, sources and copied project caches are frozen and bound to the matched scopes. No limits were changed and no builtin `countHeartbeats(max := 0)` or optional custom counter was used.

Historical required-input provenance includes the mutable owner state hash at original read time; owner state may subsequently change. The final manifest hashes immutable instructions/references and local artifact snapshots rather than asserting mutable owner state still has its historical hash.

## Phase5a/5b, result, and11-step checklist

Phase5a non-rename refactoring: authorized audit18 generic index change applied and verified; no other refactoring/decompose follow-up. Phase5b rename pass: no new rename warranted by target name; no worker queue writes. Existing four-entry rename queue is byte-identical to original14 entry (`renames15-provenance.json`, `unchanged-renames15.jsonl`) and is deferred only to the single project-end owner pass. No in-place rename.

Result:6→3 lines, saved3. Three planned changes implemented: generic finite index type, inline one-use coefficient congruence/cast conversion, and mathematical lambda arrows/composed extensionality. Historical packing mismeasurement corrected above, not counted as a defect fixed. Rules applied1.4,1.7,1.9,1.10,1.15,1.18,2.3,2.9 and audit18. Gates pass in worker scope. Renames queued: none. Comments preserved: none present in target; all outside bytes exact. Refactoring needed: none for this target. Owner full-file/publication gates remain outside this leaf's completed scope.

- [✓] Step1 — all reference docs read; full854/112-line instructions recovered.
- [✓] Step2 — full24-item audit printed; final measured correction explicit.
- [✓] Step2.5 — all five search paths actually used and status printed.
- [✓] Step2.6 — all effective outer/inner binders audited, actual probes/expanded TYPEAST, literature top3, inversion check.
- [✓] Step2.7 — final per-line packing table printed.
- [✓] Step2.8 — complete inequality scan table printed.
- [✓] Step3 — all42 golfing rules have an individual status.
- [✓] Step4 — whole automation attempted; coefficient/extensionality step-back reflection completed.
- [✓] Step5a — full unfiltered fresh nativeMainLemma/Main/Eval success, complete/nonpartial/nontimeout/0errors.
- [✓] Step5b — diff and cumulative gate status printed and actual builds passed.
- [✓] Step6a — no target rename required, shared four-entry sidecar untouched and proven exact.

Worker finalization freezes source/report/artifacts, verifies all owned process groups absent, and revokes every original15 target/doc/narrow-caller/report/source/compiler/native/profile lease at END in `final15-release.json`. No publication count is taken here. Owner review, own FULL build, separate Eval/root Eval native, exact staging/sourceA+actualhashB/pushclean are required before16; later whole-file27 review/simplify/GLOBAL/cumulative-original/data/docs/reference gates remain owner's responsibility.
