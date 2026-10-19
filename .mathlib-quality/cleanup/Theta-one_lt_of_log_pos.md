# Cleanup original Θ31: `one_lt_of_log_pos`

Scope: one fresh dedicated private-declaration audit; necessary minimal proof substitutions at its three `Θ_lt` calls. No other declaration audit is claimed. The full headline `Θ_lt` cleanup remains original35.

## Baseline and references

Source: `c488d3189154ae0da29fd6d798c3b1d016e44fa588ab4ab32a5ea7c93c3837fd`, 948 lines, release HEAD `1764f974adb44c1daa623c18ed94a2b65f5212ab`. Baseline unfiltered native LSP inherited on this exact source: `/private/tmp/roth-public30-option/final-lsp.json`, complete, 0 errors, 8 warnings. Fresh original31 prefix profiling recorded separately below. Full builds are owner-only gates; they are not claimed here.

Read lean4 and mathlib-quality skills, full cleanup workflow, golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, profiling, and relevant style/naming sections. Classic dialect. Imports/header/definitions/documentation protected by dispatch. Scratch artifacts: `/private/tmp/roth-d31-log/`.

Mathematics: a natural number with positive real logarithm exceeds one. The original proves this by assuming the opposite, casting `x ≤ 1` to ℝ, deriving `log x ≤ 0`, and contradicting positivity. Mathlib already characterizes positive logarithms on nonnegative reals. Specialize at the natural cast and cast the conclusion back once. This removes a private wrapper without creating another.

Original statement and entire first proof are preserved in `first31.lean.txt`; its SHA256 is `f2dba567cf9b7ac17015b985226741e008a26b72f56f2439d3e0d1ac43093811`. It is byte-identical to the independent original namespace's old31 block (`original-equality.json`). The complete immutable original Index/Theta proof blocks are retained in the compatibility probe, not reduced to headers.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
|1|Lint|No warning in old603–608; eight baseline warnings elsewhere remain outside this private audit.|
|2|Have scan|`hx` has proof content (`exact_mod_cast hc`), used once by `Real.log_nonpos`; anonymous `have` uses that lemma once via `linarith`. Both disappear with the whole wrapper.|
|3|Set option|None in helper; no raised limits introduced.|
|4|Simp squeeze|No simp calls in original or selected direct proof.|
|5|Naming|`one_lt_of_log_pos` describes conclusion/hypothesis, snake_case, no forbidden abbreviations or numbered structural pattern. Deletion supersedes suffix choices; no rename queued.|
|6|Line packing|Single signature line, measured table below; declaration removed, no replacement production signature.|
|7|By placement|Original `by` ends signature; each new caller's `by` ends its `have` line.|
|8|Format|No blank proof lines, 2-space incremental indentation, no new `haveI`/`letI`, semicolon, or lambda.|
|9|Comments|No helper comments; all existing caller narrative comments retained byte-for-byte.|
|10|Docstring|Private helper has none; all public/module docstrings preserved.|
|11|Visibility|Private, used only by three local caller sites; deletion is appropriate.|
|12|Structure|Five proof-body lines, no conjunction, no branch over ten lines. Deletion leaves zero lines and no new helper. Caller headline restructuring is explicitly original35.|
|13|Mathlib|Five actual methods recorded below. Direct `Real.log_pos_iff` + `Nat.cast_nonneg` + one cast bridge; delete wrapper.|
|14|Junk def|n/a: proposition lemma, not a definition.|
|15|Exists lemma|n/a: no existential result or trivial witness.|
|16|Show/change|No show/change.|
|17|Push negation|Original `push Not` already current; deleted contradiction proof.|
|18|Generalise|Both effective binders checked below; natural cast specialization already subsumed by Mathlib's real statement.|
|19|Inequality|All smaller-side-left; measured occurrence table below.|
|20|Normal form|Canonical `0 < Real.log x ↔ 1 < x` with nonnegative real argument exists as `Real.log_pos_iff`; specialize its forward direction.|
|21|Syntax generality|The direct Mathlib application accepts each actual log positivity hypothesis without constructing extra data. No custom predicate or wrapper.|
|22|Import fanout|No new production imports; existing Log.Basic supplies the API.|
|23|Casts|Zero redundant explicit casts added. `Nat.cast_nonneg` supplies the genuine ℕ→ℝ bridge inferred at all sites; `exact_mod_cast` returns a natural inequality.|
|24|Instance name|No instance declarations or instance binders in effective helper type.|

## Measured signature packing and inequality scan

| Signature | Codepoints | Next token | Arithmetic | Action |
|---|---:|---|---|---|
|old603: `private lemma one_lt_of_log_pos {x : ℕ} (h : 0 < Real.log x) : 1 < x := by`|74|none; proof body follows|n/a|ok; sole signature line|

The exact `#check @First31.first` width-100 output is in the positive proof log. There is no retained production signature to repack.

| # | Location | Occurrence | Rewrite | Rename |
|---|---|---|---|---|
|1|hypothesis h|`0 < Real.log x`|none; already `<`|none|
|2|conclusion|`1 < x`|none; already `<`|none|
|3|entire signature|zero `≥` or `>`|n/a|none|

## Generalisation and inversion

| Binder | Class/use | Compiled probes | Result |
|---|---|---|---|
|`{x : ℕ}`|Structure value; log input and conclusion|Drop binder with autoImplicit disabled; replace ℕ by ℝ with explicit `0 ≤ x`; unrestricted ℝ counterexample|Cannot drop a dependent input; successful general nonnegative-real certificate is existing Mathlib, so no new API. ℝ without nonnegativity is false at −2.|
|`(h : 0 < Real.log x)`|Strict positivity proposition|Drop h; weaken to `0 ≤ Real.log x`; positive certified counterexamples at x=1|Dropping or weakening h is false; strict h retained in direct replacement.|

No hidden σ/typeclass/universe parameter: effective type verified by the first-proof and actual-constant checks. Negative attempts are separated from successful value/axiom verification. `binder-negative.lean` records expected failures; `first-positive.lean` independently proves the original and replacement, general nonnegative-real form, and three negated invalid generalizations.

Literature: n/a, private declaration; explicit scope exemption in cleanup Step2.6d. This exemption does not skip the binder or inversion checks. Inversion: the helper depends only on the order/log relationship, not any Roth polynomial object; its more general real form is exactly the existing `Real.log_pos_iff`. No fresh abstract wrapper needed. Big-change candidate: none recommended beyond using this existing API; public `Θ_lt` hypotheses/types untouched.

## Five-method actual Mathlib search

Results and raw tool responses: `search-results.json`; source grep `mathlib-grep.log`. Search availability failures are recorded as failures, never evidence of absence.

| Method | Actual query | Result |
|---|---|---|
|A Lean-Finder|positive real logarithm of a nonnegative real implies one less than the real|`Real.log_pos_iff`, also log_pos/log_nonneg_iff; native call returned isError=false.|
|B Loogle|`Real.log, 0 < _ ↔ 1 < _`|Exact `Real.log_pos_iff` hit, native call isError=false.|
|C LeanSearch|For a nonnegative real x, log x is positive if and only if x is greater than one|Exact `Real.log_pos_iff` first hit, native call isError=false.|
|D Source grep|Untruncated `rg -n` of log_pos_iff/log_nonpos_iff/log_nonneg_iff/negative variant in Log/Basic.lean|Exact declaration at181, forward/reverse variants inspected at181–225.|
|E Local name|`Real.log_pos_iff`, `Nat.cast_nonneg` via native lean_local_search|Both source hits returned isError=false; index unavailable, so presence established by source hits, no index-based absence claim.|

Auxiliary variants examined: `Real.log_pos`, `Real.log_nonpos_iff`, `Real.log_nonneg_iff`, `Real.log_pos_of_lt_neg_one`; positive/weak/negative argument distinctions explain the required nonnegative cast premise. Common-equivalents table has no log-specific bucket; exact canonical log API located directly. Conclusion: local helper is a short composition of existing API. Delete it and update exactly three calls, no thin replacement helper. Module docstring edits are outside this dispatch's protected header scope; this report documents the direct Mathlib usage.

## All 42 golfing rules

- [1.1] n/a: no by-exact wrapper.
- [1.2] n/a: no by-rfl.
- [1.3] n/a: no rw/exact pair.
- [1.4] n/a: no simp/exact pair.
- [1.5] n/a: no trailing rfl.
- [1.6] n/a: no constructor.
- [1.7] n/a: no apply/exact pair.
- [1.8] Superseded: entire contradiction and negation proof deleted in favor of direct iff direction.
- [1.9] n/a: no lambda.
- [1.10] Superseded: anonymous intermediate and hx eliminated with wrapper.
- [1.11] n/a: no apply/intro.
- [1.12] n/a: no show.
- [1.13] n/a: no have projections.
- [1.14] n/a: no rw.
- [1.15] n/a: no simp.
- [1.16] n/a: no simp.
- [1.17] Applied: `.1 h` takes forward direction of canonical iff.
- [1.18] n/a: no trailing reducible parentheses worth changing.
- [1.19] Already push Not; deleted with contradiction.
- [1.20] n/a: no existential.
- [2.1] Actual anonymous grind trial recorded in automation.log; direct canonical API chosen.
- [2.2] n/a: original has no grind.
- [2.3] Actual simp_all trial recorded; direct canonical API avoids simplifier search.
- [2.4] n/a: goal is numerical order, not a function property.
- [2.5] Actual positivity trial recorded; log positivity does not structurally determine nat magnitude.
- [2.6] n/a: not a monotonicity calc or congruence of inequalities.
- [2.7] Actual lia trial recorded; transcendental log requires a bridge lemma.
- [2.8] Actual aesop trial recorded; direct API selected.
- [2.9] Actual norm_num trial recorded; selected exact_mod_cast closes the actual cast bridge.
- [2.10] n/a: arbitrary x with transcendental hypothesis is not finite computation.
- [2.11] n/a: no denominator identity.
- [2.12] n/a: no polynomial equality or ring ending.
- [2.13] n/a: no symmetric cases.
- [2.14] n/a: no calc chain.
- [2.15] n/a: direct proof has one goal.
- [3.1] n/a: no erw.
- [3.2] n/a: no continuity/measurability.
- [3.3] n/a: no omega introduced; lia trial in2.7.
- [3.4] n/a: no rcases substitution.
- [3.5] n/a: removed private wrapper must not gain attributes.
- [3.6] n/a: no simp_all only.
- [3.7] No limit options present or introduced.


Step back: independently testing exact?/apply? and general automation does not improve the explicitly named Mathlib proof. Keeping a one-line private wrapper would conceal an existing API and violate the requested replacement policy. The selected composition is repeated directly in the three existing local facts, without touching their conclusions or the public theorem contract.

## Applied diff and independent verification

Production change: remove the six-line declaration (five body lines plus its signature) and one following blank line, expand exactly three old call lines into two-line direct proofs. Whole file948→944 (−4). Exact scope reconstruction, public caller signature, all other declaration blocks, and every comment/docstring are checked by `scope-verification.json`. No new production helper, new imports, definition edits, Git mutations, or shared-log edits.

Independent FIRST and direct certificates: `lake env lean /private/tmp/roth-d31-log/first-positive.lean` exit0; seven value/standard-axiom markers, exact old contract, and actual old private root constant's full binder/type/value/axiom check passed. The complete successful raw log has no PANIC/error/sorryAx. Invalid drop/weakening and eight anonymous automation trials have separate expected-failure logs. `exact?` did not close; `apply?` only proposed incomplete partial applications and therefore is not proof evidence.

Actual module: `/Users/ramin/.elan/bin/lake build Roth.Theta` exit0 in28.322s, source `30a8d16687baacb2c21383934dcbb22cb0e8458da0392504d81acf9eadf6b0d7`; raw `module-build.log` and manifest `module-build.json`.

Actual compatibility: `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-d31-log/actual-compatibility-final.lean` exit0 in54.081s on that same source. `actual-compatibility-final.json` checks clean raw output, entire old `Θ_lt` full type/name/BinderInfo/universe adapter and independently re-elaborated original proof value, actual new proof value, and actual standard axioms. The pre-existing original Index/Theta proof blocks are copied unchanged: hashes `72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f` and `355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da` (`immutable-block-preservation.json`). This is the exact currently compiled probe, not the owner's future all-public-state generator.

Built constant/environment check: no constant ending `.Roth.one_lt_of_log_pos` remains. Intentionally preserved independent original namespace is excluded from this root-name test. The actual `Roth.Θ_lt` opaque proof value contains zero removed-root-wrapper references and exactly3 `Real.log_pos_iff` applications. All three new call sites therefore elaborate in the actual built caller; its entire original public contract is recovered and all actual proof axioms are among propext/Classical.choice/Quot.sound.

| New identifier | Verification | Result |
|---|---|---|
|`Real.log_pos_iff`|native local search/source atLog.Basic181; successful independent and actual built proofs|PASS|
|`Nat.cast_nonneg`|native local search/source hitData.Nat.Cast.Order.Ring; independent and actual build|PASS|

| Gate | Result/evidence |
|---|---|
|lake_build_file|PASS, actual module invocation above|
|definition_protected|PASS, no definitions touched|
|theorem_statement_protected|PASS, authorized private wrapper deletion; exact entire public caller type recovery|
|structure_gate|PASS, private target removed, no new helper/branches; full headline original35 remains separately reserved|
|naming_gate|PASS, deleted descriptive old name; no rename queue|
|line_packing_gate|PASS, sole old signature measured74 codepoints; no retained replacement signature|
|inequality_orientation_gate|PASS, no reversed inequality added|
|comments/docs/imports/header|PASS, byte-identical|
|actual removed wrapper absence/caller AST|PASS, environment absence and3 direct log applications|
|complete unfiltered native LSP|PASS, native call on entire path with no filters; success=true, partial=false, timed_out=false,0errors8unchanged warnings; `final-lsp.json`|
|owner full build / separate LeanEval / publication|PENDING owner gates, not run by this leaf|


## Simplify and buzz

Native `/simplify` and `/buzz` invocation tools are not exposed in this environment. Their substantive scoped reviews are performed here: direct API eliminates the only wrapper; no further useful extraction or duplicated nontrivial skeleton arises; no narrative/documentation churn. This is an in-agent pass-through, not a claim to have invoked an unavailable tool. Real compiler profiling below implements the buzz measurement gate.

Performance command for every trace: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`. All final measurements run sequentially after complete ordinary compiler/LSP requests drained at UTC2026-10-18T23:55:02 (`source-freeze.json`), with no subsequent production edit. Totals count outer command plus disjoint associated async proof/kernel/compiler/linter rows, without double-counting nested trace nodes; every row/anchor is retained in the `*-timings.json` files.

Fresh exact original31 production-prefix baseline: exit0, original helper161.027ms (`baseline-prefix.log`, `baseline-timings.json`). Existing prior helpers' fresh baseline measurements were weight464.258, mapped856.557, numeric1119.574, index29=1089.815, option30=220.652ms. They were unchanged by this audit; differences in their measurements are not claimed as improvements caused by this change. The preceding release's accepted timings are inherited evidence only, not substituted for these fresh observations.

The final exact production prefix ends at the removed31 slot and appends only correct section/namespace closures and an explicit environment absence certificate. This is a prefix-only result. It genuinely compiles and prints `EXACT PRODUCTION PREFIX THROUGH REMOVED31 SLOT ACTUAL PRIVATE NAME ABSENCE: PASS`; it does not invent a zero-ms timing for the deleted declaration.

| Retained target | First final ms | Required same-source repeat ms | Status |
|---|---:|---:|---|
|weight_le_delta_aux|355.826|455.493|both<1000|
|mapped_det_ne_zero_aux|710.195|877.054|both<1000|
|index_numeric_bound_aux|876.997|1068.193|repeat OVER budget|
|index_le_lem6|935.661|1115.157|repeat OVER budget|
|Θ_option_le|137.863|160.000|both<1000|

Both traces exit0:178.634s and178.295s, exact same final/live sourceSHA `30a8d16687baacb2c21383934dcbb22cb0e8458da0392504d81acf9eadf6b0d7` and same prefixSHA `544a2f1a3a047a95031c1e79b36085edeebfe544e93aa8d20d8ab4f9c3f10bdf`. Raw logs/manifests/timing anchors are `final-prefix.*` and `repeat-prefix.*`. **The all-five required-repeat performance gate has not passed** on these two runs. Owner notified with exact observations; prior helper edits are outside this leaf's exclusive source scope.

Separate exact old-contract direct replacement certificate: `replacement-certificate.lean`, exit0, real total86.921ms, below750 so no threshold-triggered repeat. This is a scratch proof certificate's cost under built imports, not a production-declaration timing or an entire-caller timing. Its statement/proof are the independently checked direct replacement. Raw `replacement-profile.log`, manifest and row anchors retained.

Baseline complete actual caller / whole-file attempt: exact pre-edit `baseline.lean`, repeated unchanged218726572-byte output at the Θ_lt trace, last `Mathlib.Meta.SetNotationForOrder.delabLe._boxed` interpretation. No explicit Lean error, no finite Θ_lt total. Only own session48607 terminated, exit130, fully drained. `baseline-caller-limit.json` and raw `baseline-caller-profile.log` retain the limitation. This is a profiler stall, **not** an observed default-heartbeat failure and **not** a finite duration inferred from whole-process wall time.

Final actual whole-file/caller attempt: exact `frozen-source.lean`, sourceSHA unchanged. Output reached the actual `Θ_lt` command (raw line2084374), then became byte-identical217743378bytes at UTC00:06:38/00:07:17/00:08:02/00:08:44. Last trace: incomplete `[Meta.isDefEq]` after assigning `?m.161 := Real.instLT`. Only own session55980 interrupted; session exit130, runner KeyboardInterrupt, compiler subprocess status not separately returned. Complete raw scan found no explicit Lean error; no observed default-heartbeat failure and no finite caller duration. Raw `final-caller-profile.log`, details `final-caller-limit.json`. All requests drained after interruption. Neither a prefix nor a replacement certificate establishes full-caller performance. Original35 remains reserved; no large caller proof refactor or limit raise applied. Whole-Theta final performance remains outstanding for owner resolution.

Buzz outcome: **scoped31 PASS** (verified direct certificate86.921ms); all-five repeat gate unresolved for two unchanged prior helpers; actual whole-caller profile unresolved. Coordinator explicitly authorized this scoped checkpoint, with file-final repair mandatory. No all-file FAST-BOARD claim. Added limit raises0, production profiling scaffolding0, new helpers0; no sorry/new axiom/native_decide.


## Eleven required phase checks

- [✓] Step1 — full mandated reference workflow and relevant style/naming/profiling read.
- [✓] Step2 — all24 audit items explicitly answered.
- [✓] Step2.5 — all five actual Mathlib search methods executed and raw results saved.
- [✓] Step2.6 — every effective binder's drop/weakening probes; independent certified counterexamples; private literature exemption; inversion check.
- [✓] Step2.7 — single signature measured74 codepoints; no retained replacement signature.
- [✓] Step2.8 — explicit inequality occurrence table, no reversed inequalities.
- [✓] Step3 — all42 golfing rules have substantive status/reason, clean anonymous automation attempts separate from positive checks.
- [✓] Step4 — direct canonical Mathlib composition selected; no thin replacement wrapper.
- [✓] Step5a — complete unfiltered native diagnostics,0errors8unchanged warnings, full success/no timeout.
- [✓] Step5b — exact owned diff, module, immutable original full caller contract/proof/value, actual root absence/three direct AST uses, standard axioms; scoped31 certificate performance passed. Earlier-helper repeat and whole-caller limitations explicitly reserved by coordinator.
- [✓] Step6a — no renames required/queued; no shared queue writes. Detailed own report only.


## Scope decision from coordinator

Coordinator authorized a **scoped declaration31 checkpoint**, after the direct certificate/semantic gates, bounded final caller attempt, and subsequent owner builds. The two unchanged earlier helpers are not downstream consumers of31, so retain the deletion and queue their exact failed repeat measurements for mandatory file-final performance repair. No third prefix sweep, rollback, or legacy-helper edit is authorized. Label only scoped31 PASS; all-five-repeat and whole-file/caller performance remain explicit outstanding obligations through original35/final profiling. This decision does not turn either failed repeat into a pass.

## Ownership handoff

Final source SHA256 `30a8d16687baacb2c21383934dcbb22cb0e8458da0392504d81acf9eadf6b0d7` (944 lines), unchanged after freeze UTC2026-10-18T23:55:02. Source editing authority remains revoked. Final performance sessions, including the bounded caller attempt, are fully drained; pending_requests=[]; compiler/native-LSP window returned to owner. Only the owned report and scratch evidence were written after source freeze.

Scoped original31 result: **PASS under the recorded coordinator scope decision**. This does not claim all-five-repeat performance PASS or complete whole-file/caller performance. The failed repeat values1068.193/1115.157ms and unavailable caller timing remain mandatory file-final follow-up. No third sweep, prior-helper edit, or silent refactor of original35.

Owner still must run full `lake build` **then separately** `lake build Roth.LeanEval`, current cumulative contracts as needed, and exact stage/commit/push before original32. No owner gate or publication claimed done here. Successful owner publication would yield212/264, Theta31/35, nine files, counting the audited original once despite private-wrapper deletion.

Report: `.mathlib-quality/cleanup/Theta-one_lt_of_log_pos.md`; freshest actual compatibility source `/private/tmp/roth-d31-log/actual-compatibility-final.lean`. Gate manifests/raw logs listed above remain reviewable. No Git/shared-log mutation by this leaf.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (103.738 s),
then separate `lake build Roth.LeanEval` (34.051 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `30a8d16687baacb2c21383934dcbb22cb0e8458da0392504d81acf9eadf6b0d7`.
Raw logs: `/private/tmp/roth-theta-d31-full.log`, `/private/tmp/roth-theta-d31-leaneval.log`; machine record
`/private/tmp/roth-theta-d31-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 31/35, overall 212/264 original
declarations, 9/14 completed files. Deleted one original private wrapper; no new helper. This still reviews one original declaration and adds no count from helpers/revisits.
