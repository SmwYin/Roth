# Roth.three_small_factors — original10

**COMPLETE original10.** Final source/build/native/semantic/paired-profile gates pass. Owner retains final file-wide and publication gates; no file completion or push is claimed.

Evidence directory: `/private/tmp/roth-mainlemma-three-factors/` (P below). The immutable historical partial report is `partial10-report-preserved.md`; all earlier failures remain preserved. The initial inherited range/count 34 declaration/28 proof lines was incorrect: exact frozen entry is **31 declaration/25 proof lines**, final **30/26**. The separately audited substantive private helper adds15 declaration/13 proof lines. Full MainLemma696→714; Main685 remains685. No Git or central-progress writes. Existing three rename entries remain byte-identical.

The public theorem removes `hm`, `hδm`, `hq₁`; weakens δ positivity to nonnegativity, A≥1 to A≥0, and strict (32) to≤. All three original conclusions remain strict. Both callers keep their exact written contracts; only their applications change. The inner shared estimate removes its positive-base premise and allows a non-strict logarithmic bound. The application doc now explicitly includes positive r₁, nonnegative δ/A, zero variables and the hypothesis boundary. Original source quotation and single proof signpost are exact.

## Full 24-item audit

The pre-edit full audit is `initial-audit.md`; its inherited line-count error is corrected above.

|Item|Finding and disposition|
|---|---|
|1 Lint|Removed unused hδm/hq₁; hm also proved redundant. Final native diagnostics recorded separately; no suppression.|
|2 Have scan|hm0 is a direct cast fact reused throughout; hlogA/hlogα direct reusable log facts; h1 proof used twice; hlog2 proof reused for hX and first component; hX reused in floor/log estimates; hδ proof needed in key; key proof reused three times. Removed old one-use hlogB, hr and anonymous log fact; inlined hB0. Explicit `(y := B₁ ...)` prevents floor unfolding from breaking arithmetic normalization.|
|3 Options|No production option added/raised; proof recursion, heartbeat and synthesis limits unchanged and positive.|
|4 Simp|No production bare simp/simp-only candidate. Unconditional log_pow replaces the positive-base exponential round trip.|
|5 Naming|Public descriptive source terminology and snake_case retained; no new rename. Private helper name/visibility separately accepted by fresh helper audit.|
|6 Packing|Measured every final signature line, including next complete token: 88+1+12=101;91+1+20=112;72+1+43=116; final97. All≤100, no further legal pack. Full tables in packing10-final.json and orientation-packing10-v2-final.json; before widths88,68,78,28,91,55, after88,91,72,97. Final doc widths92,73,0,87,54,0,85,31.|
|7 by|At signature end.|
|8 Format|No haveI/letI/inline λ/dollar/empty proof lines introduced; local key uses ordinary binder and existing idioms.|
|9 Comments|Exact original key signpost retained1/1; no narrative comment deleted.|
|10 Doc|Retains exact historical source quotation; applicability states positive r₁/nonnegative δ,A/non-strict32 and zero m.|
|11 Visibility|Public target has a cross-file actual consumer; helper stays private.|
|12 Structure|Final ordinary body26 lines; component branches≤3. Shared key reused3; substantive extracted estimate independently audited. No thin component wrappers.|
|13 Mathlib|Five actual methods plus guarded compiled whole-target probes; existing Real.log_pow/lt_rpow_of_log_lt reused. No exact full target found, not a universal absence claim.|
|14 Junk def|n/a theorem; B₁ definition protected.|
|15 Existential helper|n/a no existential helper.|
|16 Show|Removed old typed cast show; explicit y retained because failed build demonstrates required folding.|
|17 Push neg|n/a none.|
|18 Generalise|Full outer/inner table and actual boundary certificates below; all accepted small changes implemented.|
|19 Orientation|All10 entry and7 final outer signature relations and3 entry/2 final inner-key relations use≤/<. No > or ≥ occurrence in signature; per-occurrence lines/operators are in orientation-packing10-v2-final.json.|
|20 Normal form|Natural degrees/denominators, natural powers, real floor bound and real rpow kept in caller-compatible form.|
|21 Syntax generality|Conjunction retained as both callers destructure it; generic local key handles all bases including nonpositive.|
|22 Imports|No production import/fanout change.|
|23 Casts|Nat.cast_nonneg and push_cast replace hand-proved hr; explicit real cast of2/floor ensures intended domains. Actual expected-type guard checks inference.|
|24 Instance names|n/a no instance declaration/typeclass binder.|

## Generalisation 2.6a–e: every effective binder

|Binder|Drop/weakening test, result and reason|
|---|---|
|δ:ℝ|Value occurs in B₁ and exponent; cannot delete while binding conclusion. Real log/rpow/sqrt API fixes domain; no class/universe binder to weaken.|
|hδ0:0<δ|0≤δ compiled/kept. Dropping sign is refuted at δ=-1,m1,q64,r1,Aα0 with (32) but failed first conclusion (floor0). δ=0 is already impossible under other final assumptions; derived hδ only where needed.|
|hδm|Individual drop and combined drop compile with opaque-value guards; removed.|
|m:ℕ|Value occurs in powers/log condition; natural degree context retained. Positivity hm removed; actual m0 example has all strict conclusions. No Fin/countability/typeclass surplus binder.|
|hm:1≤m|Removed in simultaneous candidate-v3 and final actual proof. m0 certified.|
|q₁:ℕ|Value occurs in floor/log; natural denominator context and discrete lower bound log2 are substantive. q0/q1 impossible under final assumptions, certified. No artificial positive denominator premise retained.|
|hq₁:1<q₁|Individual drop/both-drop certified; removed, implied by logarithmic condition.|
|r₁:ℕ|Value occurs in all powers and floor; natural exponent context retained.|
|hr₁:0<r₁|Retained. Dropping/weaking to≤ includes r0, with other final premises satisfied but strict1<1 false; certified.|
|A:ℝ|Value occurs in condition and second conclusion; real parameter already unbundled.|
|hA:1≤A|Weakened to0≤A, compiled/kept, actual A0 boundary certified. Full deletion refuted by A=-63/64,m1,q2,δ1,r1,α0. A≥0 is a useful conventional domain, not claimed absolutely sharp numeric threshold.|
|α:ℝ|Value occurs under abs and in third conclusion; unrestricted already.|
|h32:strict|Weakened≤ compiled/kept. Equality δ=√(3/log2),m1,q2,r1,Aα0 is nonvacuous and certified; dropping condition refuted by δ1,m1,q2,r1,Aα0.|
|inner key t:ℝ|Unrestricted real value; conclusion uses t, so cannot delete. More general than three positive source bases.|
|inner key ht:0<t|Removed altogether by unconditional Real.log_pow and lt_rpow_of_log_lt; final compiled key covers t0/negative values without premise.|
|inner key h:strict log bound|Weakened≤ and kept; supplies actual multiplication inequality; dropping it permits unbounded base, so no valid uniform conclusion.|

No bundled assumptions, local universes, typeclasses, finiteness/countability or stronger algebraic structures remain available to weaken. No undecidable big-change request remains. Replacing the real transcendental floor/rpow setting with abstract ordered structures is unsupported by available operations and would obscure actual denominator/degree consumers.

Compiled evidence: `drop-tests-positive10`, `candidate10-v3`; actual final source and imported metadata guards; `boundaries10-v2` contains11 guarded facts; final-v3 adds an explicit inner-key logarithmic-premise counterexample under otherwise valid outer assumptions. These include nonvacuous m0/A0/equality cases, impossible δ0/q0/q1 and negative sign/r0/A/condition counterexamples. Both TYPE and actual opaque VALUE must be closed, infer the declaration type, and use only propext/Classical.choice/Quot.sound. Recovered sorryAx in failed v1/v2 candidates/boundary-v1 is explicitly rejected.

Literature2.6d: raw query1 top3 are Pottmeyer Diophantine Approximation (two domain variants), Bombieri–Gubler Heights in Diophantine Geometry. Query2 top3 are FEVER2020 proceedings, Daniel Khashabi research statement, and a nonfunctional-requirements paper; query3 top3 are Kusner differential privacy, Popular Progression Differences, and a regularity-lemma chapter. Exact titles/URLs/top3 are in literature10-top3.json and full raw query files. Queries2/3 were irrelevant; these results do not establish maximality or justify further changes. Local clean.tex1350–1388 supplies the actual source argument. No ChatGPT math MCP was available.

## Search status 2.5

Five actual methods: lemma-finder query (irrelevant Behrend hits), Loogle log/power query (empty), LeanSearch (partial Real.pow_lt_iff_lt_log family), lean local search (source partial hit/index unavailable, not absence), and direct rg of full source names/API declarations (no exact target-name hit, explicit exit1). Artifacts search10-{finder,loogle,leansearch,local}.json, source-search.txt and full-candidate-name-search.{txt,exit}. Actual source confirms unconditional Real.log_pow and Real.lt_rpow_of_log_lt, now used. No new production imports. Compiled generic-route probes use the complete prefix without importing the target and guard actual opaque values: rfl,simp,ring,linarith,nlinarith,lia,omega,exact?,apply?,grind,aesop,positivity,gcongr,simp_all all fail or contain rejected sorryAx. The apply? partial-goal trap is not counted as proof. automation10-v2 has compiler exit1 as expected for rejected alternatives, never a passing build. v1 metadata identifier syntax failure is preserved.

## All42 golfing slots

|Rule|Actual disposition|
|---|---|
|1.1|Direct expression haves used; no by-exact wrappers remain.|
|1.2|n/a no by-rfl proof.|
|1.3|n/a no rw-followed-exact pair after logarithm rewrite.|
|1.4|n/a no simp-followed-exact pair; helper simpa attempt failed and accepted restricted linarith kept by its fresh audit.|
|1.5|n/a no trailing rfl after simp.|
|1.6|Triple constructed with refine⟨...⟩.|
|1.7|Key's apply leaves a real logarithmic goal, so cannot replace by a final exact application.|
|1.8|n/a no by_contra/push_neg pair.|
|1.9|n/a no eta-expanded lambda survives; generic key reused directly.|
|1.10|Inlined hlogB/hB0/old hr and anonymous log fact; reusable facts retained with restricted arithmetic dependencies.|
|1.11|n/a no apply-intro pair.|
|1.12|Removed old typed cast show; explicit `(y := B₁...)` required by failed build-v1.|
|1.13|n/a no have-then-projection destructuring.|
|1.14|Single unconditional log_pow rewrite replaces old chain.|
|1.15|n/a no terminal simp-only.|
|1.16|n/a no nonterminal bare simp.|
|1.17|Dot chaining used for log bound/transitivity and hX.le.|
|1.18|apply...<| used for floor positivity argument.|
|1.19|n/a no push_neg.|
|1.20|n/a no single-use existential wrapper.|
|2.1|Actual whole grind probe fails/recovery rejected.|
|2.2|n/a no grind retained.|
|2.3|n/a no simp block to consolidate; direct logarithm API adopted.|
|2.4|n/a no continuity/differentiability function-property goal.|
|2.5|Actual whole positivity probe rejects non-positivity goal; direct Nat.cast_nonneg/log_nonneg/mul_nonneg used locally.|
|2.6|Actual whole gcongr probe fails; old rpow exponential gcongr roundtrip removed.|
|2.7|Actual whole lia and omega probes fail on real transcendental arithmetic; restricted nlinarith required.|
|2.8|Actual whole aesop probe leaves goals/sorry; rejected.|
|2.9|norm_num used for δ0 contradiction; push_cast normalizes exponent product.|
|2.10|n/a real inequalities not decidable closed propositions; no decide/kernel shortcut.|
|2.11|n/a no denominator normalization; whole ring probe fails on inequalities.|
|2.12|Restricted linarith/nlinarith use essential strict products/log estimates; a linear_combination equality cannot establish strict inequalities; no applicable equality block.|
|2.13|n/a three different bases are not symmetric variable cases.|
|2.14|n/a no calc chain remains.|
|2.15|Three terminal bounds need different discarded nonnegative terms; explicit restricted branches retained.|
|3.1|n/a no erw.|
|3.2|n/a no continuity/measurability tactic.|
|3.3|No omega retained; see actual lia/omega failure2.7.|
|3.4|rintro rfl substitutes δ0 directly.|
|3.5|No automation attribute for private one-use estimate/public source-specific triple; no global attribute pollution.|
|3.6|Actual whole simp_all probe makes no progress; no retained simp_all-only.|
|3.7|No maxHeartbeats override present/added.|

Step-back/simplify: reuse the library logarithmic comparison, make positivity local and derived, and isolate only the substantive discrete-denominator estimate. The three conclusion branches share a single unrestricted-base key. The proof is26 lines and arithmetic contexts are bounded. No additional component wrapper or generic framework is warranted. Built-in simplify skill is unavailable in this worker; an actual manual reuse/quality/efficiency pass is recorded, not a claim that an unavailable tool ran. No further refactoring deferred.

## Accepted separate helper audit

The first-draft extraction was handed off with immutable context and all leases released. A fresh separate worker audited the helper; owner accepted its complete evidence and returned this same original10 worker. The accepted helper weakens the first-draft1≤δ²logq premise to log2<δ²logq and retains strict2<q^(δr). Its final13-line body is unchanged here. The target’s hX application was simplified from the helper audit’s inline restricted-linarith argument to the shared `hlog2.trans_le h1` argument. Full helper report: `.mathlib-quality/cleanup/MainLemma-two_lt_rpow_aux-helper.md`; helper evidence `/private/tmp/roth-mainlemma-two-rpow-helper/`, manifest SHA645e27ea5b1da600162be9bf89387acd329462a47f17a8542306b37a545f44ff. This audit does not add another original count. Original10 AFTER captures below include the helper rather than substituting its independent helper-audit timings for the original10 baseline.

## Semantic, source and performance gates

Final MainLemma SHA `8a90958369a5f7fc9357169270737fb0c6473b1d4fd8d2d3a8d6defd95119791`; Main SHA `5f384557dccacaec469699cc7d32bd5666c9d525267e00433b7ae401fee98d09`. Final source/config17 pins are identical across all acceptance runs. Full `lake build` final10-build-v3 exited0 in71.991s; fixed build-v1 failure (missing folded y in key) remains preserved, as does successful pre-doc build-v2. Final imported independent semantic run exited0 in58.964s. Five complete contract pairs and four independent original dependency closures pass. All12 final boundary certificate opaque values and final imported helper opaque value pass standard-axiom/closed TYPE/VALUE/inferred-type guards. No source change follows build-v3.

Fresh full unfiltered native ML/Main diagnostics both success/nonpartial/nontimeout/zeroerrors: ML only its existing header warning, Main its four old header/hδ/hQ/hc warnings. Original10 unused warnings and doc long line are removed. Final-source native binding is native10-final-pins.json.

|Exact complete scope|BEFORE first/repeat ms|AFTER first/repeat ms|
|---|---:|---:|
|Public target|1812.331 /1737.768|499.967 /504.370|
|New private helper|absent|181.923 /181.318|
|Combined helper+target|1812.331 /1737.768|**681.890 /685.688**|
|ML.main_lemma|5210.167 /4831.233|5093.245 /4954.639|
|Main.roth_of_isIntegral|2958.421 /3009.772|2971.147 /3031.316|

Target cost falls62.375%/60.542%, both combined rows<750 and<1000. All required first/repeats pass exact complete command/proof/kernel/lint/root guards and17 immutable pins, strictUTF8, actual exit0/non-timeout/drain. Private proof name is exact `_private._stdin.0.Roth.two_lt_rpow_aux`; source marker is separately exact `private lemma two_lt_rpow_aux `, checked by owner verify_profile_roots_exact.py. No third unchanged sample or numerical substitution from helper-audit captures.

Foreign multi-second caller costs remain explicit later-original queues. Both ML AFTER roots are within the BEFORE range. Main first is within baseline range; repeat is+21.544ms/+0.716% against baseline repeat. Necessary weakened-premise application steps cost ML4.971/4.164→7.243/6.794ms and Main2.265/2.289→3.940/3.925ms. Those small adapters are disclosed; no broad foreign cleanup is added. Nested diagnostic steps never enter canonical root sums. Full caller diagnosis is caller10-regression-diagnosis-final.json.

Bounded custom counter, actual positive options200000/20000/512 on every wrapped declaration: original target24,868 units; AFTER helper2050 +target5859 =7909. Raw counts24,868,514→2,050,581+5,859,966 are preserved. Only temporary Elab.async=false; no builtin zero-limit heartbeat wrapper invoked. These corroborate, rather than replace, root timing acceptance.

Current104 project cache companions are physically frozen in final-cache/. All12,201 actual resolved import artifacts/split companions (1.8GB) are hashed; external artifacts exactly match the accepted helper baseline and only project MainLemma.olean changes. Actual final environment/dependency-resolution and final17 source/config snapshots are preserved. The original10 entry104 old companions remain physically preserved separately. Raw/binary manifest and actual owned29-PGID drain checks are in final-manifest.json/drain-release10-final.json; exact manifest SHA is handed to owner after hashing.

Before evidence was captured before any API/source edit: exact full actual target and both complete direct callers, all104 old cache companions, all17 source/config pins, actual environment/dependency resolution. Root totals count only unique exact token-anchored complete command plus matching proof/kernel/lint async roots; nested Meta and trailing end are excluded. Target >=750 and both callers >=750 triggered BEFORE repeats and frozen AFTER repeats. New helper cost is included with public target in AFTER comparison. Custom bounded heartbeat corroboration explicitly retains inherited positive limits; builtin #count_heartbeats is not used (its internal maxHeartbeats0 invalidates prior optional original6/9 heartbeat claims, already withdrawn by owner). These optional withdrawn counts are not relied upon here.

Baseline target1812.331/1737.768ms; main_lemma5210.167/4831.233; roth_of_isIntegral2958.421/3009.772. Exact roots and raw streams retain their own hashes. The owner’s final file-wide ALL-row global profiling gate remains mandatory; these authorized intermediate scoped captures do not substitute for it. Only complete scoped declaration roots enter original10 canonical acceptance. BEFORE entry opaque metadata unexpectedly produced2.4GiB; full raw is preserved/hash/strictUTF8 verified, compact full TYPE AST/universe/value-check extraction retained. No further whole opaque VALUE printing is necessary or performed.

The independent project-original proof reconstruction includes exact OLD sqrt_lt_floor/four_lt_rpow/log_B₁_gt and target from immutable project-original.lean SHAa3d09825fb878c5d512cfdd3feca517465e0a8215807b1261b988f664915f3a8. Complete entry ML/Main caller bodies are independently reconstructed. Banned-current-constant closures reject accidental reuse of current target/helper/four/log/sqrt/callers. Full raw expected/actual TYPE AST equality permits only declared data migration and generated macro hygiene normalization; written names/order/binderInfo/universes/data-isDefEq remain exact. Actual opaque VALUE is retrieved with value!true and checked closed/no sorry/inferred type/std axioms. Old contract adapter and expected-new signature adapter are both guarded; no strengthened caller premise or weakened conclusion is hidden.

Protected source reconstruction reverses precisely helper+target+doc and two necessary application lines back to exact frozen entry bytes; all other15 pins unchanged. Accepted helper SHA28d5e3d918bf76bd34e2a0bbf7e68a32f1d6785d18d5229545201a4f2afecf46 is exact. New source SHA/config pins, full current cache and resolved import hashes are frozen in final artifacts. Every raw artifact is hashed/strictUTF8 verified except actual enumerated binary cache companions. Owned PGIDs must be absent and all native jobs complete before final release.

## Required11 phase checklist

- [✓] Step1: both installed skills, full cleanup/cleanup-all/buzz, full854-line mandatory prompt and all required references read; scope/HB/private-root errata applied.
- [✓] Step2: full pre-edit24 audit retained and final24 dispositions printed.
- [✓] Step2.5: five actual searches, compiled generic-route rejection and search-status block.
- [✓] Step2.6: full outer/inner effective binder2.6a–e table, actual substitutions/drop/edge proofs and literature top3.
- [✓] Step2.7: measured before/final line widths and next complete tokens, no legal further pack.
- [✓] Step2.8: every10→7 outer and3→2 inner inequality occurrence canonical; exact table retained.
- [✓] Step3: all42 golfing slots have dispositions, actual applicable automation attempts retained.
- [✓] Step4: actual holistic reuse/quality/efficiency reflection; no additional helper or deferred refactor.
- [✓] Step5a: fresh complete native diagnostics zeroerrors, target warning-clean, historical foreign warnings explicitly retained.
- [✓] Step5b: source/comment/import/options/standard-axiom/full TYPE+actual VALUE/caller contracts/packing/orientation/naming/structure and combined target performance gates pass; foreign performance queues explicit.
- [✓] Step6a: no rename appended; exact existing three-entry queue preserved.

Gate status: PASS original10 scope. Structure ordinary26-line body; naming unchanged/private helper separately audited; packing max97 signature/max92 doc; orientation canonical; no sorry/admit/new axioms/limit raises; comments1/1 exact and source quotation exact; all affected full build/native checks pass; exact original proof and entry callers recovered independently. Refactoring deferred: none. Built-in simplify unavailable, manual simplify pass performed; buzz target repair verified by identical-scope actual paired captures and bounded corroboration. No original/helper count inflation.

Owner retains final whole-file FULL→separate Eval/root native verification, exact source review/staging, source audit commit, hash-metadata child, actual push and clean-worktree publication before original11. This report completes only original10; helper is not an extra original count and file completion is not claimed.
