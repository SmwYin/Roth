# Cleanup original Θ32: `lem6M_lt`

Scope: one fresh public declaration audit; two substantive new private helpers and the necessary single `Θ_lt` application edit. The helpers require their own later fresh dedicated audits. The full original35 `Θ_lt` cleanup is not claimed here. No Git or shared-log writes.

## Baseline and mathematics

Published baseline HEAD `45a85d5b868d5f125061fd7f7abf58892556a9d2`; exact source SHA256 `30a8d16687baacb2c21383934dcbb22cb0e8458da0392504d81acf9eadf6b0d7`, 944 lines. Inherited complete unfiltered baseline live diagnostics `/private/tmp/roth-d31-log/final-lsp.json`: success, partial=false, timed_out=false, zero errors/eight warnings. Owner baseline full build 103.738s and separate LeanEval 34.051s are inherited, not rerun or claimed as this leaf's final gates. Classic dialect; imports/header/definitions/protected hypotheses unchanged.

Read lean4 and mathlib-quality skills, full cleanup workflow, full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, profiling, and relevant style/naming rules. Scratch evidence is `/private/tmp/roth-d32-log/`.

Mathematics: bound the coefficient factor `(r₁+1)^(p*l) * l! * 2^(p*l*r₁)` by `2^((2*p+1)*r₁*l)` using `r₁+1 ≤ 2^r₁` and `l! ≤ l^l`. The logarithmic lower bound and `log 2 < 1` turn this into a strict real-power bound. Multiply by the positive `B^l` and combine the exponents. These are two independent estimates, not 1–3-call convenience wrappers.

Supported API strengthening, explicitly recommended to owner after the concrete independent compatibility pass and approved under standing user authority:

- `hp : 2 ≤ p` becomes `hp : 0 < p`.
- Remove `hr₁ : 0 < r₁`, derived from `1 ≤ l ≤ r₁`.
- `hq₁` becomes nonstrict `p*(2*p+1)/δ ≤ log q₁`; the conclusion remains strict because `log 2 < 1`.

One caller argument `(hr0 0)` is removed. The entire `Θ_lt` type is preserved, including all effective parameters; its full proof remains independently checked. The public docstring changes only the affected assumptions while preserving the source attribution and narrative.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
|1|Lint|No original target warning; eight inherited file warnings are outside scope. Final complete native diagnostics recorded below.|
|2|Have scan|Original hp0: by/cast retained. hlogq: one-use direct term inlined into hq1pos. hq1pos: case proof replaced by direct Mathlib log iff, used repeatedly. hr2/hlr/h1/h2: natural bound moved into substantive coefficient helper. hnat: extracted; hnatR: proof-bearing cast retained. hB: one-use rpow identity inlined in final rewrite. h2N: substantive exponent estimate extracted and its one-use call inlined. Nested hlog2/anonymous log bound, hlr0, h3 and h4 belong to that extracted estimate. No one-use non-by have remains in the public proof. New-helper own have audits are left to their required separate fresh workers.|
|3|Set option|No production option changed; no raised limits, profiling scaffolding or masks. Lower 10000 heartbeat budgets occur only in anonymous expected-negative automation scratch.|
|4|Simp squeeze|Original terminal `simp [h] at hlogq` disappears with the case split. Public final proof has no simp.|
|5|Naming|`lem6M_lt` names the existing `lem6M` quantity and comparison, with no forbidden abbreviation/numbered structural pattern. New helpers name coefficient and exponential estimates; no rename.|
|6|Line packing|Measured table below; public32 passes, coefficient-helper packing finding belongs to its mandatory fresh helper audit.|
|7|By placement|Every by is at the end of its signature/proof-start line.|
|8|Format|2-space proof indentation, no blank proof lines, haveI/letI, lambda, semicolon, or trailing whitespace introduced.|
|9|Comments|One original signpost comment preserved verbatim in public proof. Entire caller narrative retained.|
|10|Docstring|Public docstring retained with mathematically necessary hypothesis update; source quotation/attribution retained. Private helpers have no docstrings.|
|11|Visibility|Retain the existing public result; new internal estimates private.|
|12|Structure|Public proof 53→21 body lines (ordinary cap30); new helpers10 and20. All nested subproofs/branches ≤10; no conjunction. Headline caller's full structure belongs to original35.|
|13|Mathlib|Five actual search methods and anonymous compiled generic-route trials below. Building blocks found; no whole-result replacement found. Search availability distinctions recorded.|
|14|Junk def|n/a: theorem; no definition changed.|
|15|Exists lemma|n/a: no existential witness.|
|16|Show/change|No show/change introduced or present in public proof.|
|17|Push negation|No push_neg or negation proof remains.|
|18|Generalise|Every effective original binder audited below; all three recommended strengthenings have full concrete compiled proof/contract/caller evidence.|
|19|Inequality|All code inequalities smaller-side-left; occurrence table below.|
|20|Normal form|Retain canonical natural powers/real rpow and original closed-form conclusion. No new custom predicate.|
|21|Syntax generality|Weaker numeric/log assumptions directly accept more callers; removing a derived argument simplifies the one current call.|
|22|Import fanout|No new production imports.|
|23|Casts|All explicit natural-to-real casts bridge genuine types or fix the ambient real power/log expression. Removed the old extra real hnat/hB plumbing via one cast and one final rpow rewrite; no redundant cast added.|
|24|Instance name|No instance declarations/binders in the effective target type; no σ/τ instances silently inherited.|

## Measured packing and inequalities

`#check @Roth.lem6M_lt` at format.width100 appears in the final actual compatibility log.

| Signature line | Codepoints including :=by | Next logical token/group | Arithmetic | Action |
|---|---:|---|---|---|
|public643|71|hq₁ binder,47|71+1+47=119|ok|
|public644|89|conclusion first full `lem6M ... l`,34|89+1+34=124|ok|
|public645|86|none|n/a|ok|
|coefficient603|79|leading factor and trailing `*`,20|79+1+20=100|repack pending mandatory fresh helper audit|
|coefficient604|90|none|n/a|ok|
|exponential616|95|hlog binder,47|95+1+47=143|ok|
|exponential617|72|whole real-power comparison,57|72+1+57=130|ok|
|exponential618|67|none|n/a|ok|

The helper signature packing was improved after the immutable first clean context was saved: coefficient conclusion joined, q positivity binder moved onto the preceding line. No mathematical helper proof change followed that first clean snapshot.

| Location | Occurrences | Rewrite/name action |
|---|---|---|
|public hp/hδ0/hq₁/hl/hl'/conclusion|`0 < p`, `0 < δ`, quotient `≤ log`, `1 ≤ l`, `l ≤ r₁`, strict result|none; already `<`/`≤`|
|coefficient hl/conclusion|`l ≤ r₁`, coefficient `≤` power|none|
|exponential hp/hδ/hq/hlog/hlr/conclusion|positive p/δ/q/product; weak log bound; strict comparison|none|
|all signatures|zero `≥` or `>` in Lean code|no rename|

## Every-effective-binder compiled probes

Successful concrete candidate: `candidate-compatibility.lean/.log` exit0, plus exact polished full candidate `candidate-final.lean/.log` exit0 before application. The immutable original32 type/proof is retained in the complete independent original Index+Theta namespace, not inferred from the weakened current theorem.

Expected-negative files/logs are separate from successful/axiom certificates. `negative-binders.lean/.log` contains named isolated drop/weakening trials after the exact source prefix ending before target, with autoImplicit=false; these are proof-dependence experiments, not claims that a failed tactic proves mathematical impossibility. A q-binder removal initially failed to remove the newline-adjacent binder; corrected separate `negative-drop-q-corrected.lean/.log` records the actual removal. No false q-drop claim is based on the initial trial.

| Original effective binder | Kind/use | Compiled candidates/result |
|---|---|---|
|p:ℕ|Value, counts integer powers|Drop fails unknown p with autoImplicit=false. Keep the natural domain because lem6M's count is natural.|
|hp:2≤p|Proposition, denominator positivity|Concrete full proof at0<p succeeds. Drop/0≤p fail selected proof; certified p=0 negated conclusion in successful native run. p=1 application separately checked against built module.|
|δ:ℝ|Value, real log/rpow exponent|Drop fails unknown δ; Real specialization is load-bearing. No abstract ordered-field replacement supplies this real log/rpow API.|
|hδ0:0<δ|Proposition, positive quotient/multiplication|Drop and0≤δ fail positivity/helper application. Certified δ=0 negated conclusion in successful native run. Strict retained.|
|r₁:ℕ|Value, degree/coefficient bound|Drop fails unknown r₁. Concrete natural degree retained.|
|hr₁:0<r₁|Proposition, positive strict factor|Full concrete proof omitting it succeeds, deriving positive l*r₁ from1≤l≤r₁. Exact old adapter recovers it harmlessly as an unused old argument.|
|q₁:ℕ|Value, denominator/log input|Actual corrected drop fails unknown q₁. The natural denominator domain provides nonnegativity for log_pos_iff and matches current callers.|
|hq₁:quotient<log|Proposition, exponent comparison|Full nonstrict replacement succeeds with strict output via log2<1. Drop fails unknown hq₁; no additional weakening recommended.|
|l:ℕ|Value, factorial/natural powers|Drop fails unknown l. Natural domain required by factorial.|
|hl:1≤l|Proposition, positive multiplication|Drop/0≤l fail positive l*r₁ proof. At l=0 both sides reduce to1, so strict output requires positivity.|
|hl':l≤r₁|Proposition, factorial bound and r₁ positivity|Drop fails coefficient argument/positive product proof. Replacing with only l≤2^r₁ loses positivity at r₁=0,l=1; would need an extra assumption, so retained current simpler API.|

No hidden universes/typeclasses: actual effective types and complete old telescope adapter verified by the actual-constant gate. No class parent/point-localisation/universe weakening applies to these fixed scalar/natural binders.

Inversion: lem6M appears once at the unfolding comparison; its independent mathematical content is exactly the natural coefficient estimate plus the logarithmic real-power estimate. Extracting those two substantive estimates isolates that content without inventing an abstract object with a generality of one. General real base q would require a nonnegativity condition; existing project callers use natural denominators, which also match the lem6M count API. No broader domain statement is recommended here.

Public literature search: web queries `"Formalizing Roth" "Takloo" Yin` and `Roth theorem lemma index sets polynomial M factorial 2 delta generalization logarithm`; inspected [Roth’s theorem notes](https://www.math.uh.edu/~minru/fields/roth.pdf), [UCL transcendence notes](https://www.ucl.ac.uk/~ucahpet/TransNotes.pdf) (open failed), and [elementary approach](https://aleksa-milojevic.github.io/expository/roth.pdf). These concern the general auxiliary-polynomial/index method, not this exact coefficient boundary. Authoritative project source `.mathlib-quality/references/clean.tex`960–983 has this exact estimate with p≥2 and strict log growth. The p>0/weak-log refinements are this proof's compiled deductions, not attributed to those sources. No connected math-second-opinion MCP is available; none claimed. No further literature-driven public restatement recommended.

## Five-method Mathlib search

| Method | Actual query/result |
|---|---|
|A Lean-Finder|Factorial coefficient bound and explicit two-power/log-rpow comparison. Factorial_two_mul and Behrend estimates returned, not the target.|
|B Loogle|`Nat.factorial _ ≤ _ ^ _` → Nat.factorial_le_pow; `Real.log ?x < ?x - 1` → Real.log_lt_sub_one_of_pos.|
|C LeanSearch|Power-two/rpow from log bound → Real.lt_pow_of_log_lt, le_zpow_of_log_le (natural/integer exponents); factorial/powers query → factorial comparison building blocks.|
|D rg source|Untruncated candidate-name/building-block search in factorial/basic, pow/real, log/basic; `mathlib-rg.log`. No local whole-result candidate name found.|
|E local name|factorial_le_pow source hit (index unavailable); rpow_lt_rpow variants hit (index warming). Those are presence evidence, not indexed absence evidence.|

Auxiliary variants checked: factorial_mul_pow, factorial_two_mul, rpow_lt_rpow/iff, log bound/pow comparison forms. Common-equivalents table has no specialized factorial/log coefficient bucket. Conclusion: use the verified Mathlib building blocks directly inside two substantive estimates; no evidence of a ready-made whole target. Anonymous exact?/apply? trials against exact source prefix before target additionally tested generic routes; no matching self-theorem was present. No general claim of global Mathlib absence from search failures.

Native/compiled identifier verification: successful `lean_run_code` checks Nat.factorial_le_pow, Nat.pow_le_pow_left, Nat.lt_two_pow_self, Real.log_lt_sub_one_of_pos, Real.rpow_mul_natCast, Real.rpow_add, Real.log_pos_iff; full exact candidate elaboration also verifies every retained identifier. Raw responses in `native-search-and-run.json`; additional native search calls recorded in session tool outputs.

## All 42 golfing rules

- [1.1] n/a: no by-exact wrapper.
- [1.2] n/a: no by-rfl.
- [1.3] n/a: no rw/exact pair to combine.
- [1.4] Applied: direct canonical log iff removes old simp/case proof.
- [1.5] n/a: no trailing rfl.
- [1.6] n/a: no constructor.
- [1.7] n/a: no apply/exact pair.
- [1.8] n/a: no contradiction proof.
- [1.9] n/a: no eta lambda.
- [1.10] Applied: inline hlogq,hB and final h2N call; coefficient haves moved into independent estimate.
- [1.11] n/a: no apply/intro.
- [1.12] n/a: no show.
- [1.13] n/a: no conjunction projection.
- [1.14] Applied: final rpow rewrite combines the two transformations; h3's intervening rewrite-location dependency retained.
- [1.15] n/a: no terminal simp-only.
- [1.16] n/a: no nonterminal bare simp.
- [1.17] Applied: direct .trans/.trans_le composition in estimate.
- [1.18] Applied: <| for log iff inputs.
- [1.19] n/a: no push_neg.
- [1.20] n/a: no trivial private existential.
- [2.1] Tried anonymous grind on complete target; failed under lower scratch budget.
- [2.2] n/a: no selected grind chain to delete.
- [2.3] Applied: log comparison simpa was tested; `simpa` alone did not normalize2−1, corrected by the original log inequality/linarith proof. The failed initial attempt is preserved, not success evidence.
- [2.4] n/a: no function regularity property.
- [2.5] Applied: strict quotient/nonnegative coefficient/rpow positivity obligations.
- [2.6] Applied: coefficient monotonicity uses gcongr.
- [2.7] Applied: lia proves positive l and r₁ for product; preexisting caller omega unchanged to keep caller edit minimal.
- [2.8] Tried anonymous aesop, failed complete target.
- [2.9] Applied: numeric log-bound side conditions and exact_mod_cast bridges.
- [2.10] n/a: target has arbitrary real analytic input, no closed finite computation; native_decide never used.
- [2.11] n/a: no field identity requiring cancellation; inverse p is an algebraic atom for ring.
- [2.12] Tried linear_combination on final exponent identity in positive scratch; ring retained as the direct normalization of an identity, no premises needed.
- [2.13] n/a: no symmetric cases.
- [2.14] n/a: final calculation has coefficient bound, strict exponential bound, and exponent identity, not a redundant two-step chain.
- [2.15] n/a: no duplicate multi-goal closure.
- [3.1] n/a: no erw.
- [3.2] n/a: no continuity/measurability tactic.
- [3.3] Satisfied by2.7; no new omega.
- [3.4] n/a: no rfl substitution case.
- [3.5] n/a: specialized estimates are not canonical simp/grind normal-form rules.
- [3.6] Tried anonymous simp_all on whole target; failed.
- [3.7] No production heartbeat/recursion limits, raises or masks.

Step-back review: a one-tactic proof was not found; factor-counting, strict logarithmic comparison and rpow assembly are distinct mathematical steps. Original public proof is now an outline of those steps. Term mode would obscure the cast/rewrite calculations without useful savings. No thin wrapper was introduced.

## Independent/actual contract and first-helper evidence

First clean helper context `/private/tmp/roth-d32-log/helpers-first-context.lean`, SHA256 `807e99748225d46c5acaeaa802f15ae3743c5357f2c10e81a339613c0e03f6cb`, preserved byte-for-byte with the complete preceding source/section context; `helpers-first.log` exit0. First helper body counts10 and20; production bodies unchanged, only signature packing changed. This is independent first-proof evidence, not a claim of a later fresh helper audit.

Preapplication `candidate-compatibility.lean/.log` exit0 preserves the entire immutable old Index+Theta proof namespace, checks exact original32 adapter type, complete original/new Θ_lt type and opaque proof values, new35→new32 dependency, and standard axioms for old32, candidate32, adapter, old35, candidate35 and both helpers. `candidate-final.lean/.log` then compiles the exact final source including the entire actual caller before live apply. Owner explicitly accepted the recommendation after receiving the preapply evidence.

Actual built compatibility and final live diagnostics/performance gates recorded below. Expected-negative automation/binder experiments never certify axioms or a successful theorem. Native run-code p1 trial saw cached old imports; its failure is recorded separately. Direct built-module p1 application was corrected to supply explicit parameters after an apply-unification failure; only its final clean success is evidence.

## Verification gates

| Gate | Status | Evidence |
|---|---|---|
|lake_build_file|PASS|Actual `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit0, `module-build.log`:2423jobs completed.|
|definition_protected|PASS|Snapshot diff has no def/abbrev/import/header edits.|
|theorem_statement_protected|PASS with authorized strengthening|Three exact documented weakenings supported by concrete candidate and full immutable old32 adapter; no conclusion weakening.|
|caller effective contract|PASS|`actual-compatibility-final.lean/.log` exit0; entire original old Index+Theta proofs, exact effective retained names/BinderInfo/order, full Θ_lt adapter/value/dependency.|
|opaque values/axioms|PASS|Actual32, old32, adapter, actual/old35 and both actual/FIRST helpers; only propext/Classical.choice/Quot.sound. No PANIC/error/sorryAx in success log.|
|native final complete file|PASS|`final-lsp.json`, complete UNFILTERED live Roth/Theta.lean, success=true, partial=false, timed_out=false, zero errors/eight inherited warnings. `final-goal.json` independently sees new public binders.|
|public32 structure|PASS|21lines≤30, all nested subproofs≤10, no conjunction.|
|public32 naming/packing/inequalities|PASS|Measured public rows; no forbidden name or reversed code inequality.|
|new helper fresh audits|PENDING owner dispatch|Exactly two private estimates, first exact context preserved. Coefficient helper has concrete100-character repack candidate below; no helper fresh audit claimed here.|
|external usage|PASS scoped|rg found only the one same-file actual Θ_lt call; entire caller compiles and semantic contract is checked. Owner fullproject/LeanEval still required.|
|full lake build then separate LeanEval|OWNER PENDING|Do not count this checkpoint until the owner completes these sequential gates after fresh helpers.|

`negative-automation.lean/.log` exit1 as expected: grind/aesop/simp_all/exact? fail whole analytic target; apply? offers unrelated partial suggestions and reaches the deliberately lower10000-heartbeat delaboration budget. All examples are anonymous; exact prefix ends BEFORE the target. This is not a production default-heartbeat failure, not a successful proof, and not axiom evidence. The known inherited unbounded native multi_attempt stall was not repeated, per dispatch; bounded native goal/run-code tools and ordinary compiler probes were used instead.

Successful final `positive-p1.lean` compiles against the built module with explicit p=1, r/q/l parameters, `Nat.cast_one` normalization and converted3/δ hypothesis. It additionally tests linear_combination on the exponent identity and prints standard actual32 axioms. Its sole scratch unnecessarySeqFocus warning has no production counterpart. Earlier cached-native/import and apply/numeric-normalization failures are exploratory logs only.

## Simplify review and fresh-helper boundary

Native `/simplify` and `/buzz` invocation tools are not exposed. An in-agent scoped simplify review found no duplicated independent public skeleton, further public wrapper, or useful canonical restatement. The selected proof exposes the coefficient bound, strict exponential bound, and final exponent assembly directly. This is a scoped pass-through, not an assertion of invoking an unavailable skill tool. Real profiling below implements the performance measurement gate.

Mandatory later fresh audits, one dedicated fresh worker per helper:

1. `_private.Roth.Theta.0.Roth.factorial_coefficient_le_two_pow_aux`, source603–614, proof10lines. First exact declaration/context in `helpers-first-context.lean`. Concrete packing candidate: line60379chars plus one separator plus `(r₁ + 1) ^ (p * l) *`20chars =100; move the remaining product/comparison to its continuation. Its current helper packing gate is deliberately left pending for that fresh audit. Parent explicitly accepted this scope boundary.
2. `_private.Roth.Theta.0.Roth.two_pow_lt_rpow_aux`, source616–638, proof20lines. First exact declaration/context in the same immutable snapshot. Its own full mechanical binder/golf/performance audit remains a separate fresh-worker obligation.

These are not original-declaration checkpoint inflation. Full original35 caller cleanup and mandatory file-final performance repair remain independent.

## Real performance / buzz

Actual command for baseline and final: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`. Both use the exact original/production prefix through32 and correct `end Lemma7` / `end Roth` closures, exit0. Final prefix is from frozen live sourceSHA `52868a517597da434ede705309f6563030ce587eaafbffb28d991e782c9f7a9d`. All ordinary compiler/native requests were drained before each profiler. Raw UTF8 `baseline-profile.log` and `final-profile.log`; exact disjoint command/async/kernel/linter anchors in `baseline-profile-summary.json` and `final-profile-summary.json`.

Totals include outer command plus associated disjoint async proof/addDecl/kernel/linter work. The `lemma` macro emits a nested `theorem` command: that inner command is explicitly recorded and NOT counted twice. Nested kernel rows are already included in their addDecl parent. No duration is inferred from process wall time.

| Declaration | Baseline ms | Final ms | Repeat requirement/status |
|---|---:|---:|---|
|lem6M_lt|1679.405|627.089|<750; no threshold repeat required; <1000 PASS|
|factorial_coefficient_le_two_pow_aux|new substantive estimate|263.134|<750; no repeat required; <1000 PASS|
|two_pow_lt_rpow_aux|new substantive estimate|590.813|<750; no repeat required; <1000 PASS|

Scoped32 performance outcome: **FIXED**, with the two new helpers' full fresh audits pending. This is prefix-only evidence and does not establish whole-file/caller performance. Baseline trace had finite proof1540.535ms plus disjoint associated work; decomposing the natural coefficient and analytic exponential comparisons distributes that elaboration work, and the public log/cast/rpow assembly is simplified. No limits/masks/scaffolding added.

Mandatory inherited file-final repair queue remains: original31 repeat at the prior identical source observed `index_numeric_bound_aux`1068.193ms and `index_le_lem6`1115.157ms, despite first876.997/935.661ms. Those nonconsumer declarations were outside this leaf's scope and were not silently edited. No all-five/whole-file FAST-BOARD claim and no cherry-picked third sweep. Entire actual Θ_lt profiling previously stalled at giant unchanged output and was interrupted without a finite timing or explicit Lean/default-heartbeat error. This known inherited profiler limitation was not rediscovered by another unbounded whole-caller trace here; actual full Θ_lt semantic compatibility was freshly checked. Original35/final owner must resolve whole-caller performance.

## Eleven required phase checks

- [✓] Step1: mandated skills/reference workflow read.
- [✓] Step2: all24 original32 audit items recorded.
- [✓] Step2.5: five actual Mathlib search methods and generic-route trials recorded.
- [✓] Step2.6: every effective original binder tested/reviewed; compiled strengthenings and exact old contract; public literature/inversion check.
- [✓] Step2.7: public32 signature per-line packing measured; separate helper's concrete100-char packing finding explicitly pending its fresh audit.
- [✓] Step2.8: code inequality occurrence scan.
- [✓] Step3: all42 golf rules addressed with actual applicable trials.
- [✓] Step4: holistic reflection and substantive decomposition.
- [✓] Step5a: fresh complete unfiltered final live native diagnostics0errors, success/partial=false/no timeout.
- [✓] Step5b: scoped public diff/contract/module/actual value/standard axiom/performance gates passed; separate helper audits and owner builds not falsely marked done.
- [✓] Step6a: no renames, no shared queue edits.

Source freeze: SHA256 `52868a517597da434ede705309f6563030ce587eaafbffb28d991e782c9f7a9d`; 944→949file lines (+5). Public proof53→21 (−32), two substantive helper proofs10+20 (=30); no helper original-count inflation. One of one narrative comments retained. Source edit authority is revoked at handoff; report-only work complete. All this leaf's compiler/native requests drained, pending[]. Owner retains two fresh helper audits, complete file-final performance repair/original35, and final frozen fullbuild THEN separateLeanEval/publication gates.


## Final32 batch after BOTH separate fresh helper audits

The initial source/profiles above document the dedicated original32 leaf. Both new helpers now
have separate completed fresh audits: [coefficient](Theta-factorial_coefficient_le_two_pow_aux.md)
and [exponential](Theta-two_pow_lt_rpow_aux.md). Final coefficient proof9lines accepts
`l ≤ 2 ^ r₁`; final exponential proof21lines accepts `0 ≤ q`. Public32 remains21lines with
its documented p/log/r₁ changes, and its strict result and entire public Θ_lt caller contract
are preserved. Final source949lines, SHA256
`edd28b8b48e01767e9d4434e08c0190f8a8848a873497bd647fa25e8ecdbc35f`.

Final module, exact INITIAL helper adapters/independent proof values/actual standard axioms,
original32 adapter, ENTIRE old/new Θ_lt semantic proof/type/value/standard axioms, and complete
unfiltered native LSP pass (0errors8samewarnings). Final same-source real prefix profiles:
public32675.914ms, coefficient290.063ms, exponential597.526ms, all below750; no threshold repeat
required. Raw/final source manifests are in `/private/tmp/roth-exponential-audit/handoff.json`.
This remains a scoped prefix result; the existing numeric/index29 repeat failures and actual
whole Θ_lt profiling stall remain mandatory file-final repair obligations.

Owner cumulative verification on this exact final source passed47.118s:29explicit original
public adapters,87opaque body-type checks and87actual standard-axiom sets,29PASS markers.
Both entire original Index/Theta proof blocks remain byte-identical (72cf/355a). Exact successful
verifier `/private/tmp/ThetaApprovedOriginalFinalProbe-d32-values-corrected.lean`, SHA256
`1a673f9914a15a60ce5d80d5e864b7c12e1e3b87e790bb919d1f2bd4e1301b70`; log/record
`/private/tmp/roth-theta-d32-values-corrected-cumulative29.{log,json}` and explicit owner counts
`/private/tmp/roth-theta-d32-owner-cumulative-checked.json`.

The first owner attempt invoked the previous generated verifier because the generator had been
edited but not executed. It correctly rejected new hp at25completed adapters; this was a stale
scratch-verifier failure, with no production change. Failed log/manifest
`/private/tmp/roth-theta-d32-values-cumulative29.{log,json}` and exact old generated source
`/private/tmp/ThetaApprovedOriginalFinalProbe-d32-values-failed-old-generated.lean` are retained.
The corrected exit0 run above is the accepted current evidence.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (91.810 s),
then separate `lake build Roth.LeanEval` (31.678 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `edd28b8b48e01767e9d4434e08c0190f8a8848a873497bd647fa25e8ecdbc35f`.
Raw logs: `/private/tmp/roth-theta-d32-full.log`, `/private/tmp/roth-theta-d32-leaneval.log`; machine record
`/private/tmp/roth-theta-d32-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 32/35, overall 213/264 original
declarations, 9/14 completed files. Two substantive private estimates have separate fresh completed audits: coefficient proof9lines with l≤2^r₁, exponential proof21lines with q≥0. Helper audits and supported revisits do not inflate original counts.
