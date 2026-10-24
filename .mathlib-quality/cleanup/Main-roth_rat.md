# Roth.roth_rat — dedicated original17 audit

Installed lean4/mathlib-quality skills, full cleanup/cleanup-all commands, full mandatory golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, style-rules, naming-conventions, mathlib-review-stages, profiling, buzz, quality-principles and PR-feedback read. The declaration maps infinitely many rationals injectively to their reduced numerator/denominator pairs; these satisfy approxSet, so accepted Roth.roth bounds κ. No helper extraction is warranted for a five-line proof.

## All 24 audit items

| # | Item | Concrete result |
|---|---|---|
|1|Lint|Initial and post-edit complete unfiltered Main diagnostics: zero errors; existing line1 copyright/header warning only; none on target.|
|2|HAVE|Entry L577 hinj has no tactic `by`, one use L579 as hinj.injOn; inline at image, preserving numerator/denominator injection. Final no have.|
|3|Options|None on target; no resource raises introduced.|
|4|Simp|No simp; terminal rwa already uses exact Rat.cast_def.|
|5|Naming|Roth.roth_rat is descriptive theorem snake_case, established rational suffix; none of forbidden patterns/abbreviations; no rename.|
|6|Packing|Full two-line signature arithmetic below; unchanged.|
|7|By|At end of signature line576.|
|8|Format|Two-space proof, four-space signature continuation, no empty lines or semicolon chains; ordinary lambda arrows changed to ↦.|
|9|Comments|Zero proof comments present; zero removed; all surrounding accepted comments frozen.|
|10|Docs|Two-line public docstring retained exactly: distinguishes rational-number formulation from integer-pair Roth.roth; module reference supplies Roth1955/clean.tex §6.|
|11|Visibility|Public headline corollary intended for external rational approximation use.|
|12|Structure|Entry five body lines, final four; ≤15 headline bound; no statement conjunction or long branches.|
|13|Mathlib|Five-method search below; use existing Rat.ext, Set.Infinite.image, Set.Infinite.mono, Rat.cast_def directly. No new wrapper/API.|
|14|Junk def|n/a theorem, no data definition.|
|15|Existential helper|n/a no existential auxiliary declaration.|
|16|Show/change|Neither occurs.|
|17|Push neg|None.|
|18|Generality|Every binder assessed below; hα mathematically dispensable with a separate rational-case argument, explicitly retained under bounded public-contract scope.|
|19|Inequality|All signature inequalities already use < or ≤; no reversed notation.|
|20|Normal form|Set.Infinite over actual Rat, denominator Rat.den, real rpow; canonical existing number/set API.|
|21|Syntactic generality|Rational-set statement directly usable without reconstructing integer pairs; no easier equivalent public restatement needed.|
|22|Import fanout|n/a no new imports.|
|23|Casts|0 dropped; signature `(x.den : ℝ)` kept genuine Nat→Real bridge fixing rpow base; `(x : ℚ)` map binder annotation load-bearing to infer num/den, not a cross-type cast. No new numeric coercions.|
|24|Instance names|n/a no instance declaration.|

## Packing

|Signature line|Codepoints|Next complete binder/token|Arithmetic|Action|
|---|---:|---|---|---|
|575|77|`(hinf : {x : ℚ ...}.Infinite)` (57)|77+1+57=135>100|ok|
|576|75|no next signature line|n/a; conclusion and := by already on line|ok|

Width100 #check will be captured by fresh independent inventory and profile. No split binder/conclusion omitted.

## Inequality scan

|Occurrence|Location|Form|Action|
|---|---|---|---|
|1|hinf predicate L576|`|α - x| < 1 / ...`|already smaller-left|
|2|conclusion L576|`κ ≤ 2`|already smaller-left|
|—|whole signature|zero ≥ or >|no rewrite/name queue|

## Mathlib search (all five methods)

A Lean-Finder query: rational determined by numerator and denominator / pair injectivity. Hits NNRat.ext_num_den, Rat.mk'_num_den, Rat.mkRat_num_den'.
B Loogle `Rat.num, Rat.den, _ = _`: Rat.mkRat_self, Rat.normalize_self, Rat.num_divInt_den (plus arithmetic internals), no better pair API among results.
C LeanSearch `Rational numerator denominator pair injective`: Rat.div_int_inj, Rat.isCoprime_num_den, Rat.intCast_injective; none shortens Rat.ext on pair projections.
D Actual Mathlib Data/Rat and v4.34.0 core Rat files: Rat.ext at Init/Data/Rat/Lemmas.lean:26; Rat.cast_def and reconstruction API. Earlier source path guesses Data/Rat/Basic, Algebra/Rat and core v4.28.0 were nonexistent; corrected to actual toolchain, not Lean failures or evidence of absence.
E lean_local_search Rat.ext: actual Rat.ext found; index warming (presence valid; no absence claim).
Auxiliary variants checked: ext/ext_num_den, mk'_num_den, num_divInt_den, mkRat_self, cast_def, infinite.image/InjOn. Common-equivalents table: finiteness/image subset matches generic set API already used.
Conclusion: partial API matches used directly; keep genuine project Roth corollary. No claim of exhaustive Mathlib theorem absence, and no new custom lemma requiring an absence probe.

## Per-binder generality

|Binder|Class|Use|Candidates considered/result|
|---|---|---|---|
|α : ℝ|structure value|irrational/algebraic and approximation center|Drop impossible in type; Real→abstract field is a different ambient approximation theorem, beyond concrete real Roth scope; no mechanical typeclass parents.|
|hα : Irrational α|proposition|accepted Roth.roth input|Drop is mathematically possible for rational-set version using separate rational α case: nonzero rational differences ≥1/(bq), so κ>2 bounds q; equality contributes one rational. Current proof cannot drop it through Roth.roth. Owner explicitly declines optional case/public-contract expansion. Retain honestly, not claimed logically necessary.|
|halg : IsAlgebraic ℚ α|proposition|accepted Roth.roth input|Drop false in general (Liouville irrational numbers); no strict→weak/pointwise/typeclass parent applicable.|
|κ : ℝ|structure value|variable exponent and conclusion|Drop impossible in type; no universe or typeclass weakening; arbitrary real κ already allowed.|
|hinf : {...}.Infinite|proposition|infinite image and Roth input|Drop false for κ>2 (without infinitude arbitrary exponent allowed); finite/nonempty weaker forms insufficient; strict→weak inequality in set would be a different theorem requiring exponent adjustment.|

No binder omitted. No false claim that compiler failure proves mathematical necessity; no unsuccessful drop trials labeled as a semantic result. Inversion check: concrete rational numerator/denominator and Roth approximation content are used throughout, so abstract mapping wrapper would only duplicate generic image/mono API.

Literature query `Roth theorem irrational algebraic real rational approximation exponent 2 generalization`: Encyclopedia of Mathematics Thue–Siegel–Roth theorem, MathWorld Roth's Theorem and Irrationality Measure agree with standard finite reduced approximation formulation; local primary formalization clean.tex §6 supplies actual project statement. Broader Ridout/p-adic or number-field forms are separate mathematics. No ChatGPT math connector available in tool inventory. Sources: https://encyclopediaofmath.org/wiki/Thue-Siegel-Roth_theorem ; https://mathworld.wolfram.com/RothsTheorem.html .

## All 42 golfing rules

|Rule|Result|
|---|---|
|1.1|n/a no by-exact wrapper.|
|1.2|n/a no by-rfl wrapper.|
|1.3|already terminal rwa in constructor.|
|1.4|n/a no simp-exact sequence.|
|1.5|n/a no trailing rfl after simp.|
|1.6|already anonymous pair constructor; no constructor sequence.|
|1.7|n/a no apply-exact sequence.|
|1.8|n/a no contradiction/negation sequence in production.|
|1.9|both map and equality proof use projections, no eta lambda; ordinary arrows corrected to ↦.|
|1.10|applied: single-use tactic-free hinj removed/inlined into image InjOn.|
|1.11|n/a no apply-intro sequence.|
|1.12|n/a no show.|
|1.13|n/a hinj not conjunction/projection pair.|
|1.14|n/a no consecutive rw.|
|1.15|n/a no simp only.|
|1.16|n/a no nonterminal simp.|
|1.17|already hinf.image and .mono; Rat.ext namespace is necessary.|
|1.18|inline lambda passed directly; grouping needed for image.mono composition.|
|1.19|n/a no push_neg.|
|1.20|n/a no trivial existential helper.|
|2.1|live bare grind failed on exponent bound; no production change. Tool's line replacement also reported residual old multiline tactic parser error; not a whole-source success.|
|2.2|n/a no existing grind predecessor.|
|2.3|n/a no simp sequence to consolidate.|
|2.4|n/a no function-property goal.|
|2.5|den_pos direct builtin lemma already shorter; whole goal is real exponent upper bound, not positivity.|
|2.6|n/a no monotonicity chain; set mono is inclusion, not order arithmetic tactic.|
|2.7|n/a no Nat/Int arithmetic proof block; denominator positivity provided by Rat API.|
|2.8|live aesop failed exhaustive search on real exponent bound; residual multiline parser error qualified as in2.1.|
|2.9|n/a no numeric computation; cast_def structural rewrite, norm_cast not rational reconstruction.|
|2.10|n/a infinitude/real exponent theorem is not finite decidable computation.|
|2.11|n/a no field identity; numerator-denominator cast is exact API rewrite.|
|2.12|n/a no ring/ring_nf endpoint.|
|2.13|n/a no symmetric branches.|
|2.14|n/a no calc.|
|2.15|n/a no repeated similar goals from refine.|
|3.1|n/a no erw.|
|3.2|n/a no legacy continuity/measurability.|
|3.3|n/a no omega;2.7 no arithmetic tactic applicable.|
|3.4|rintro with rfl already substitutes image witness; no redundant following substitution.|
|3.5|no automation attribute for headline conditional Roth theorem; would add global search cost.|
|3.6|n/a no simp_all only.|
|3.7|n/a no maxHeartbeats override.|

## Step-back/manual holistic review

Current proof is precisely image-inclusion then accepted Roth; finite-preimage contrapositive is a distinct independent check, not a production improvement. No duplicated long skeleton, missing conceptual helper, cast round-trip, or value definition. New wrappers would hide two standard set operations and are unwarranted. Built-in /simplify is unavailable; this is an actual manual holistic review and no skill invocation is claimed. Fresh independent wholefile review remains required after original17, owned by file owner.

## Failed-probe truthfulness

One live multi_attempt batch: bare grind and aesop unsuccessful; first inline attempt incorrectly supplied 3 arguments where InjOn needs5 and therefore failed elaboration. Corrected five-argument production proof passed complete diagnostics. Those unsuccessful probes are retained in probes.json. No sorry/axiom/native_decide/resource increase. No forced helper, broad search, caller edit or accepted prior-proof rewrite.

## Baseline and source preservation

Genuine project Main684 snapshot SHA f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069 and entry Main583 SHA fb8f0346210a5307f4f76fc3cc31f02ee1fb0bd5d0deb3bcddadccbb1a3cf462 preserved before any Lean/golf. Actual target451B identical in both (SHA4c1f7fc9a947e6867e9b6812a5986beec10d1facd731fffd11b4830d6669d345). Accepted exact-source preflight build/native/LSP evidence from prior originals15/16 supplies initial green baseline; no unchanged build is relabeled new. Cache download not needed. This PROOF edit received actual full build, separate Eval build, three native checks and complete fresh diagnostics below. Existing replayed dependency lint warnings remain; no warning-free whole-project claim.

Scope diff verified bytewise: only target proof changes; target signature/doc, all preceding declarations including five accepted helpers, imports, later namespace close unchanged. No definition, API, helper, caller, rename queue, shared progress or Git writes. Main583→582 lines; target declaration7→6 lines and body5→4 lines (one line saved). New production identifiers: none; all referenced constants were already present and actually compile.

## Verification and gates

All command streams/terminal receipts are under `/private/tmp/roth-main-roth-rat/`.

|Gate|Result|Actual evidence|
|---|---|---|
|lake_build/full|PASS|`lake build`, final-full-build terminal0,57.339s; actual changed Main and root built.|
|separate Eval build|PASS|`lake build Roth.LeanEval`, final-Eval-build terminal0,29.155s.|
|native Main|PASS|`lake env lean Roth/Main.lean`, terminal0,28.078s.|
|native Eval|PASS|`lake env lean Roth/LeanEval.lean`, terminal0,30.262s.|
|native root|PASS|`lake env lean Roth.lean`, terminal0,25.873s.|
|final complete unfiltered LSP|PASS|Main/Eval/root success true, partial false, timed_out false, zero errors; Main existing header warning only, Eval/root no diagnostics.|
|definition_protected|PASS|No definition changed; exact scoped byte comparison.|
|theorem_statement_protected|PASS|Entire actual target signature byte-identical; strict recursive+raw TYPE matches saved old contract.|
|structure_gate|PASS|Final four-line body≤15 headline bound; no long branch/statement conjunction.|
|naming_gate|PASS|Descriptive Roth.roth_rat; no forbidden pattern or abbreviation; no renames.|
|line_packing_gate|PASS|Both signature lines measured above; next binder cannot fit135>100; final line includes conclusion.|
|inequality_orientation_gate|PASS|Explicit occurrence table; zero reversed inequalities.|
|cumulative caller safety|PASS|Current full/root/Eval builds/native/LSP; unchanged API. Neither root nor Eval proof calls roth_rat directly; earlier validated caller TYPE/metadata can be retained without reinferring earlier caller/helper VALUES.|
|no trust/resource/scaffolding regression|PASS|No sorry, new axiom, native_decide, resource raise or profile option in production; no comments lost.|

Overall required scoped gates PASS. No unchanged-baseline-only final-build label; actual proof edit triggered required builds.

## Semantics and independence

`Independent.lean` proves the same target using contrapositive and a finite preimage under numerator/denominator, then accepted earlier Roth.roth. It does not invoke roth_rat. Actual compile terminal0,60.002s. Before any per-row TYPE/VALUE guard, actual full production/independent generated families and universes were enumerated: exactly `Roth.roth_rat` and `Roth.independentRothRat`, each opaque, each actual levelParams `[]`. No suffix/empty-universe assumption preceded enumeration.

`Semantics.lean` terminal0,49.133s: strict recursive Expr/Name/Level/BinderInfo/metadata/literal/projection comparison and complete raw TYPE equality for genuine-old/current/independent; no ExprBEq short-circuit; no hygiene exception needed. Old contract comes from accepted genuine original target caller extraction `/private/tmp/roth-main-integral-roth/Roth-roth_rat-oldTYPE.txt`, not a rewritten guess. Per actual row, actual opaque VALUE obtained and inferred IN MEMORY at default200000/20000/512, closed and free of admissions/metavariables/loose variables. Persisted only VALUE hash/length, never raw proof VALUE:

|Actual theorem|VALUE bytes|Lean hash|Axioms|
|---|---:|---|---|
|Roth.roth_rat|84945|9118739965762042344|propext, Classical.choice, Quot.sound|
|Roth.independentRothRat|60830|15462616446211803695|propext, Classical.choice, Quot.sound|

Fresh actual local dependency graph acyclic; no self-reference, no target dependency from independent, no later Main/Eval/circular wrappers. All external leaves have actual strictly upstream ModuleIdx, with explicit accepted earlier Main leaves Roth.roth/approxSet; no unchanged accepted helper/caller VALUE reinference. Different proof VALUES are not asserted identical. Receipts: `actual-family-inventory.json`, `semantic-rows.json`, `dependency-receipt.json`.

## Simplify / refactoring

Manual holistic PASS-THROUGH as described above; built-in simplify unavailable and no invocation claimed. Phase5a: no required extraction, wrapper or data refactoring. Phase5b: no rename requested/queued/applied; shared rename queue untouched. Rational-case hα observation is recorded honestly under owner-directed bounded scope, with no optional public API expansion. Independent wholefile reviewer remains file owner's next separate task after publication; this target report does not claim that final review ran.

## Buzz: FAST-BOARD

Owner HOLD ACK preceded every profile preparation operation. Exact current production prefix35248B SHA4fbfd7664a8a49418c5d75cd37a7c8dd8350750f54c1dcc329dbcf3481fc5c75 excludes appended `end Roth` plus newline (9B, separately SHA7deec3e6b243c8d21c0bd696efc684ad744733ab1e612f4077bb23327ee885be). Prefix-binding literal text uses escaped-newline notation; actual appended bytes/length/hash are authoritative. Production source SHA395b36fbb79b58e28bf362e6cc6f55a0fe70d04b385d5dadab3e40388d9d6453.

Capture command `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 .../final-profile/Prefix.lean`. Before/after complete safe environment byte equality held IN MEMORY, default budgets checked, frozen source/pins/tool binaries/maps exact. Full environment/unrelated arguments never persisted; hashes/length and approved PATH/LEAN/toolchain allowlist only. Task-owned ps observer ran escalated first try.

Actual driver34566 terminal0/absent and all five launchgroups absent were reported RAW UNPARSED; owner explicitly RELEASED before parsing. Full canonical doc/signature/proof bound to exact target; actual profiled family singleton Roth.roth_rat. Disjoint roots:

|Root|ms|
|---|---:|
|outer command|29.210|
|async proof|19.245|
|async kernel parent|1.217|
|async lint|6.767|
|sum|56.439|

Kernel Roth.roth_rat1.193ms is nested in kernel parent (not added twice); compiler roots none; lazy prior DATA roots none. Below1000ms budget and below750ms repeat trigger, so no repeat/cherry-pick/extra unchanged capture. Profile observation freshly checked opaque VALUE closed/inferred/standard axioms/default budgets in memory. `FinalProfileType.lean` terminal0,37.026s strictly binds observed profile TYPE+universes to actual current+independent TYPE, including full raw bytes. No proof VALUE reinference in this bridge.

Historical all17 indexed target41.635ms belongs to Main689 after MainLemma caller repairs, not genuine Main684/current Main582. Actual narrow target canonical/root/kernel raw byte bindings recorded. Different contexts are reported separately; no speedup ratio or causal-noise dismissal. Qualification: one early inspection inadvertently printed all17 indexed JSON metadata and the tool truncated it; historical317MB raw was read only in five bounded target-indexed chunks, never broadly reparsed. Inherited earlier overlap FAIL is not relabeled a wholepass.

No profiling scaffold/resource override shipped; maxHeartbeats raises removed0, added0; no timing deferral or performance fix claim.

## Phase checklist

All completed for this single declaration: Step1 full references; Step2 all24 audit items; Step2.5 five methods; Step2.6 every binder plus literature; Step2.7 all signature lines; Step2.8 inequality occurrences; Step3 all42 rules; Step4 reflection/manual holistic review; Step5a complete unfiltered current diagnostics; Step5b scoped build/protection/structure/naming/packing/inequality/caller/semantic gates; Step6a no rename required; scoped buzz capture+strict TYPE bridge; final report. Wholefile final review and owner publication are separate pending owner responsibilities, not counted as complete here.

## Actual END / lease release

All known task launch PIDs and process groups rechecked absent after the final strict profile TYPE driver exited0; all compiler/native/semantic/profile drivers and parser/tool sessions terminal0; all LSP/search queries complete. No active HOLD or pending query. Source freeze unchanged. Target source, report, compiler, native, semantic, LSP and profile leases released to owner; no caller/Git/shared-progress/rename writes. This is actual target END, pending owner publication and independent wholefile final review.
