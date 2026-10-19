# Audit: `Roth.sqrt_lt_floor` — original7/27

Original7 per-declaration gates are complete, ready for independent owner closure/publication. Counts remain222/264 (ML6/27, files10/14) until owner publication. Whole-file performance is FAIL on the explicit foreign rows below; file/project completion is not claimed.

Final source `Roth/MainLemma.lean`: helper94–96, public105–106,697 lines,
SHA256 `85af4993b70decb29489013593420d99644a93e2ac6891cecfa7cad5fb2b55f8`.
Main684 lines, SHA256 `879e16516770f1b7ccd88ed77968197ef02a77f4e7d4b1e73b3614c9db361a65`.
Entry MainLemma695 lines, SHA256 `770a6ff1cb79679adfd37cdf765f475e33e1300497537ccd2fb3ae1508f6c26d`.

Evidence: initial complete audit/probes/captures at `/private/tmp/roth-mainlemma-sqrt-floor/`
(frozen145 files, untouched); final source gates/captures at
`/private/tmp/roth-mainlemma-sqrt-floor-final7/`. Original partial report is preserved as
entry-original7-report.md. No Git/shared-progress/rename-queue operations.

## Step1 — references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md and cleanup-gates.md, installed lean4/mathlib-quality skills,
cleanup/cleanup-all/buzz and the exact worker prompt. Standing user authorization covers
the sharp public-hypothesis weakening and the four necessary caller repairs. Explicit task
rails preserve both paired conclusions and require a fresh dedicated helper audit.

## Step2 — full24-item audit

1. LINT: final unfiltered ML/Main native after actual affected build: success=true,
   partial=false,timed_out=false,failed_dependencies=[],isError=false,zero errors.
   Only preexisting header/unused-variable warnings outside target/helper remain.
2. HAVE SCAN: original h1 had no by and one arithmetic use; hs no outer by and reused;
   hs0 had zero textual uses but supplied context-sensitive square-root nonnegativity;
   hs2 had by and one final use. All four disappear with the new strategy. Final public
   proof has no have. Helper hfloor has by and is used by positivity and nlinarith: KEEP.
3. SET_OPTION: no declaration-local limit changes; no instrumentation entered source.
4. SIMP SQUEEZE: n/a, no simp in selected public/helper bodies.
5. NAMING: sqrt_lt_floor and private sqrt_lt_nat_floor_aux carry mathematical content,
   snake_case, no forbidden patterns/abbreviations/orientation rename. Queue untouched.
6. LINE PACKING: complete measured tables below; public74/helper71 codepoints, no
   dangling signature token or wide-hyp escape needed.
7. BY PLACEMENT: both declarations term mode; each nested tactic starts inline by.
8. FORMAT: two-space body indentation, no blank proof-body lines or long branches;
   no sequential rewrites/haveI/letI/semicolon/show/lambda to fix.
9. COMMENTS: no proof comments. Entire exact historical source quote/Lean note preserved.
10. DOCSTRING: lead sharpens to X≥2; application tip explains natural floor and both
    projections. Private helper correctly has no docstring.
11. VISIBILITY: public pair retained for real internal/Main callers, private strict
    helper above it; no trivial right-hand wrapper introduced.
12. STRUCTURE: original6 body lines→public1 plus helper2. Both conclusions preserved
    under explicit task rail; ordinary≤30, branches≤10. Fresh helper audit complete.
13. MATHLIB: five actual methods plus separate compiled automation controls below;
    partial sqrt/floor APIs found, nonlinear estimate remains substantive.
14. JUNK DEF: n/a, target theorem; no def/abbrev/data value changed.
15. EXISTS LEMMA: n/a, target is a pair of inequalities.
16. SHOW/CHANGE: n/a, neither in selected declarations.
17. PUSH_NEG: n/a, none.
18. GENERALISE: all effective binders/candidates below. Sharp2≤X is both sufficient and
    necessary; old4<X full contract independently recovered and full old proof compiled.
19. INEQUALITY: zero ≥/> in changed Lean signatures/hypotheses; table below.
20. NORMAL FORM: Real.sqrt/Nat.floor/canonical real coercion and smaller-side-left form;
    no alternate predicate/restatement network introduced.
21. SYNTAX-GEN: implicit real X/explicit sharp bound apply directly; genuine callers
    use both projections, so preserving the pair is intentional.
22. IMPORT-FANOUT: n/a, no import added.
23. CASTS: public statement's two genuine floor-to-real coercions retained. Fresh helper
    removes3 redundant explicit ascriptions; retains only load-bearing `(2 : ℝ)`.
    Natural-floor-only bound was compiled and rejected by its arithmetic step.
24. INSTANCE-NAME: n/a, no instance declaration/local instance introduced.

Changes: sharpen4<X→2≤X, extract meaningful strict helper and recombine directly with
Nat.floor_le, repair exactly four calls using hX.le.trans' (by norm_num), add application tip.
No unrelated caller proof/statement/import/attribute/option changes. Historical quote unchanged.

## Mathlib search-status

[A] Lean-Finder: “For a real number x at least two, the square root of x is less than its natural floor”; success, partial hits Nat.sqrt_lt_self, Real.real_sqrt_lt_nat_sqrt_succ, Nat.add_one_sqrt_le_of_ne_zero, Real.nat_sqrt_le_real_sqrt.
[B] Loogle: `Real.sqrt, Nat.floor`; success, Real.nat_floor_real_sqrt_eq_nat_sqrt and unrelated number-theory bounds, no direct target.
[C] LeanSearch: “Real square root strictly less than natural floor when two is at most x”; success, Real.sqrt_lt', Real.sqrt_lt_sqrt, Nat.sqrt_lt partial hits.
[D] Full local source grep: `sqrt.*floor|floor.*sqrt|lt_floor_add_one|le_floor|sqrt_lt_iff` in relevant floor/sqrt source; Nat.le_floor, Nat.floor_le, Nat.lt_floor_add_one and sqrt/floor commuting facts. Full candidate-name grep and compiled generic probes retained below.
[E] lean_local_search `sqrt_lt`: partial relevant sqrt hits; index=unavailable, so absence is NOT inferred from its empty/missing names. Local source and compiled exact?/apply? provide fallback.
Auxiliary variants: sqrt_lt, sqrt_lt', sqrt_lt_self_iff, nat_floor_real_sqrt_eq_nat_sqrt, floor_real_sqrt_eq_nat_sqrt, lt_floor_add_one, sub_one_lt_floor, le_floor, floor_le. Common-equivalents table: no bucket applies (elementary floor arithmetic).
Concluded: partial match Real.sqrt_lt' + floor bounds; retain the nontrivial local strict argument. Separate compiled exact?/apply? diagnostic probes and restored-state closed-proof controls below found no complete direct substitute. This is a search conclusion, not a claim of mathematical nonexistence.

## Generalisation status — 2.6a–e

| # | Binder | Class | Used as | Candidates | Verification/result |
|---|---|---|---|---|---|
| 1 | {X : ℝ} | structure value | sqrt/floor argument | drop X; ℝ→ordered field; universe | X cannot be dropped from a statement mentioning it; real-specific sqrt prevents a mechanical ordered-field substitution; no universe binder to weaken. Explicit/implicit order unchanged. |
| 2 | (hX : 4 < X) | proposition | nonnegativity, lower threshold | drop; 0≤X; 1≤X; 1<X; 2≤X; 4≤X | Kernel-checked boundary-controls-v2 rejects drop, 0≤X, 1≤X, 1<X; candidate-controls-v2 proves 2≤X, specialization 4≤X and X=2, and necessity of 2≤X for the strict conclusion. Hence 2≤X is exact. No point/global or typeclass-parent catalogue entry applies. |

2.6b: compiled candidates and diagnostic evidence recorded below; failed candidates never enter live source.
2.6c: public numeric-hypothesis weakening is authorized and applied only after valid before-consumer profiles. No unrelated abstract-type restatement is recommended because Real.sqrt is intrinsically real.
2.6d: public literature search performed; see next section.
2.6e: retain kernel-checked exact necessary/sufficient threshold 2≤X. Inversion check: n/a, X is arbitrary and the proof never unfolds a distinguished named construction.

## Literature search

WebSearch queries: “floor function square root inequality x greater than 2 generalization”; “floor function definition inequalities n ≤ x < n+1”; “square root floor x inequality sqrt x floor x”. Top relevant hits: Wikipedia Floor and ceiling functions; Math by First Principles Floor and Ceiling; Algebrica Floor and Ceiling Functions; Book of Proofs floor definition; ProofWiki definition/range; U. Toronto MAT246 notes; UC Davis ECS20 homework solutions; Math.SE square-root floor identity; nor's floor/ceiling notes. The canonical property is k≤X<k+1. Primary [UC Davis solutions](https://www.cs.ucdavis.edu/~koehl/Teaching/ECS20_F16/Homeworks/homework5_solution.pdf) and [U. Toronto notes](https://www.math.utoronto.ca/campesat/ens/21W/l17.pdf) support the floor characterization. The inference k≥2 ⇒ k²≥k+1>X is our elementary deduction, not attributed as a source theorem. No alternate abstract formulation found that improves this real-square-root API.
ChatGPT math MCP: n/a, no callable ChatGPT-math tool available.

## Golfing-rule pass (all 42 rules; empirical attempt outcomes appended below)

| Rule | Status/action |
|---|---|
| 1.1 | n/a: original was not by-exact. Separately, the new paired proof uses a direct term. |
| 1.2 | n/a: no by-rfl proof. |
| 1.3 | n/a: no rewrite-exact pair. |
| 1.4 | n/a: no simp-exact pair. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | Applied: recombine directly with anonymous pair. |
| 1.7 | Applied by fresh helper audit: compose Real.sqrt_lt'.2 with its closed arithmetic proof in term mode. |
| 1.8 | n/a: no contradiction/negation chain. |
| 1.9 | n/a: no lambda. |
| 1.10 | Applied: old one-use floor have removed with replacement strategy; no new unproved single-use have in paired body. |
| 1.11 | n/a: no apply-intro pair. |
| 1.12 | n/a: no redundant show. |
| 1.13 | n/a: no temporary conjunction projected in target. |
| 1.14 | n/a: no consecutive rw. |
| 1.15 | n/a: no terminal simp only. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | Caller repairs use order-proof dot notation; all other mathlib arguments appropriately explicit. |
| 1.18 | n/a: no outer parentheses whose removal helps a trailing multiline expression. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential lemma. |
| 2.1 | Failed to close: separate whole-proof grind and hinted arithmetic grind controls; closed fallback proofs and standard-axiom checks passed. |
| 2.2 | n/a: grind failed; no final grind prefix. |
| 2.3 | n/a: no simplification chain to consolidate. |
| 2.4 | n/a: sqrt/floor inequality is not a function-regularity goal. |
| 2.5 | Applied: positivity closes the helper positive-floor prerequisite and public nonnegative-X prerequisite; candidate-controls-v2 kernel-checks both. |
| 2.6 | gcongr attempted on strict comparison; no common monotone outer expression bridges sqrt/floor. |
| 2.7 | lia attempted on whole arithmetic goal; nonlinear real square comparison requires stronger arithmetic. |
| 2.8 | Failed to close in separate pretarget whole-proof controls; no theorem/helper self-use. |
| 2.9 | Whole goal failed; norm_num closes exact numeric caller order bridges. Boundary norm_num-only floor attempt failed and was replaced by explicit floor_eq_iff in v2. |
| 2.10 | n/a: arbitrary real inequality has no effective decidable finite computation. |
| 2.11 | n/a: no denominator identity. |
| 2.12 | n/a: no ring/ring_nf terminal identity with hypotheses. |
| 2.13 | n/a: no symmetric cases. |
| 2.14 | n/a: no two-step calc. |
| 2.15 | n/a: two genuinely different conclusions, one arithmetic strict bound and one floor API call; pair term is clearer. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability tactics. |
| 3.3 | lia tested in 2.7; no omega retained. |
| 3.4 | n/a: no rcases/substitution. |
| 3.5 | No global simp/grind attribute: paired theorem is specialized API and helper private; automation registration would add unrelated global search. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no resource options present or added. |


## Fresh introduced-helper audit and Step4

Mandatory separate helper audit is complete and independently accepted by owner:
`.mathlib-quality/cleanup/MainLemma-sqrt_lt_nat_floor_aux.md`, SHA256
`839071e8469e6bf207cb0714531d239ff0bf2a2c73284241b01189ee8efd96b4`.
Its first draft was saved before any compile/golf: declaration6acacb51195465e4e5a2e8706972ee7adcaf9e2db1567b82bc458f960004a88c,
full context524044ba0c5530950f2d6ad5d2725b772272161a5330493e0319f3e67927f057.
First unchanged context passed; positivity prerequisite then independently verified.
Fresh worker additionally removes the square hint/annotations and composes the proof in
term mode, saving1 line. Its117 frozen artifacts/strictUTF8/17pins/actual private metadata,
full raw type/telescope/opaque value/standard axioms, independent first/selected proofs and
closed dependency exclusions passed owner review. Current actual private name:
`_private.Roth.MainLemma.0.Roth.sqrt_lt_nat_floor_aux`.

Matched SCOPED helper129.381→95.857ms, paired caller21.728→17.544ms; bounded custom
heartbeat counts1369→825. These scoped measurements are not numerically compared with our
GLOBAL captures. No builtin count_heartbeats/maxHeartbeats0 or resource-limit raise.

Step4: whole-goal grind/simp/aesop/lia/gcongr/norm_num and exact? do not close the original
claim; helper alternatives/term mode/have composition were checked. Selected proof uses
k=floorX≥2 and X<k+1 to show X<k², then Real.sqrt_lt'. The upper bound uses Nat.floor_le
directly. Exact sharpness controls reject weaker bounds. ChatGPT-math and builtin simplify
are unavailable; manual declaration reflection is complete. Parent file-wide simplify/buzz
and final-file repairs remain separate duties.

## Packing and inequality artifacts

| State / declaration | Signature line | Codepoints | Next token | current+1+next≤100 / action |
|---|---:|---:|---|---|
|entry public|98|77|none|n/a; complete77≤100, ok|
|final private helper|94|71|none|n/a; complete71≤100, ok|
|final public|105|74|none|n/a; complete74≤100, ok|

| # | Location | Original ≥/> | Rewrite | Rename |
|---|---|---|---|---|
|1|all changed Lean signatures/hypotheses|zero|none|none|

Prose X≥2 and exact historical X>4 are excluded from Lean orientation scan. Helper body2,
public1; no branch over10. Header/documentation/source quotation preserved.

## Actual final source build/native/proof/contract gates

Actual `lake build Roth.MainLemma Roth.Main` exited0 in38.405s (final7-affected-build.json).
Fresh unfiltered final7-native-ml.json and final7-native-main.json both return complete
success/zero errors/no failed dependencies after that build. ML warnings: header + old
log_B₁_gt hδ0/hr₁ at138. Main warnings: header + old hδ/hQ/hc. Target/helper have none.
Rebuilt actual olean hashes are retained in final7-imported-modules-after-build.json.

Independent target gate final7-independent-target.json: exit0,32.721s, strictUTF8,17pins
immutable. Full original six-line proof compiles independently; old4<X adapter exact full
type AST equals original, new2≤X actual full AST equals expected. All X/hX names/order/
BinderInfo/universes and actual opaque proof-body inferred types checked; standard axioms only.

Independent callers gate final7-independent-callers.json: exit0,58.398s, strictUTF8,17pins
immutable. Entire exact accepted pre7 ML/Main proof bodies are replayed in fresh namespaces,
with only explicit old-ML reference qualification in Main; transformations reverse byte-for-byte
(per preserved v5 construction/proofbytes evidence). All four current/old full dependent types,
written/base binder names/order/BinderInfo/universes, opaque actual proof values and standard
axioms pass. Precisely3 main_lemma generated names differ module hygiene (`_stdin` vs
Roth.MainLemma); RAW names logged/preserved, only Name.eraseMacroScopes used for generated
names on both sides. Written names are never normalized. Full AST/defeq checks remain exact
after declared namespace-constant migrations. Pinned Init/Prelude source explains hygiene.
All five old-proof dependency closures exclude current target, all four current callers,
and the uniquely environment-resolved actual new private helper. No imported-self shortcut.

This is per-change entry-contract recovery, not an original Main audit or cumulative
project-original proof pass. Historical scaffold v1 remains failed/pending parent cumulative
closure; its partial PASS messages are not accepted as gates.

## Retained rejected evidence

- Pinned Lean4.34 apply? can call admitGoal after partial suggestions. Diagnostic exit0
  printed sorryAx; REJECTED, never selected/imported/used in positive proof/profile gates.
  Separate controls restore state, then check actual closed proof type and standard axioms.
- First boundary norm_num-only floor attempt failed; v2 explicit floor_eq_iff passes.
  Unexpected positivity failguard retained; positive candidate-v2 subsequently proves it.
- Caller v1 alias/noncomputable/equation/closure failures, v2/v3 raw hygiene comparator
  failures retained. Repaired v5 passes with explicit exact-name/hygiene distinction.
- Initial merged full-ML raw335925674bytes has malformedUTF8 at byte692240 from interleaved
  stderr splitting a Unicode character. Runner exited1 before child flags were recorded;
  child exit/timeout UNKNOWN, not called a timeout/pass. Raw/hash/context retained; PGID40146
  absent. No timings accepted. Separate streams and supported -j1 fix the infrastructure.
- One argument-order retry failed before process creation; retained, corrected.
- Initial default-worker target346.599ms is diagnostic only, never matched to -j1 numbers.


## Final matched GLOBAL profiling and extraction accounting

Exact actual CLI for accepted before/after captures:
`lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`.
No source instrumentation or Lean limit raises. Separate stdout/stderr, strictUTF8,exit0,
no timeout, exact input SHA,17 source/config pins immutable and actual PGID absence.
Canonical anchored_profile_span.py selects each unique complete command→next-command span;
only column-zero Elab.command/Elab.async disjoint roots count. Nested/internal Meta events,
preceding/adjacent/end commands excluded. verify_profile_roots.py checks actual named proof,
compiler/kernel/lint roots and absence of foreign proof roots. BOTH full-file captures have
ALL28 ML and ALL17 Main rows complete:90 accepted rows, final7-complete-row-board.json.
This is a timing census, not45 new declaration audits or an all-file budget pass.

| Whole capture | First seconds | Frozen repeat seconds | Exact source SHA |
|---|---:|---:|---|
|MainLemma|433.089|412.016|85af4993…55f8|
|Main|419.145|403.027|879e1651…1a65|

| Declaration | Before first ms | Before repeat ms | After first ms | After repeat ms |
|---|---:|---:|---:|---:|
|sqrt_lt_floor|178.143|178.631|22.373|16.945|
|log_B₁_gt|92.760|94.440|120.938|96.766|
|three_small_factors|1735.730|1817.841|1835.599|1699.293|
|main_lemma|5065.963|5037.212|5216.969|4880.648|
|roth_of_isIntegral|2968.688|3196.609|3176.075|3044.742|
|private extracted helper|absent|absent|105.609|87.419|
|public plus helper accounting|178.143|178.631|127.982|104.364|

Matched exact-prefix control: original173.076ms → public16.360ms + helper86.712ms
=103.072ms. Extraction costs are acknowledged. All selected public/helper samples<750ms:
original7 is FAST-BOARD, no own budget failure/deferral/limit raise. Frozen whole-file repeats
were required by slow consumers. No best-sample selection or unchanged third retry.
Scoped helper-audit numbers remain separate and are never compared with GLOBAL samples.

Causal consumer review: four calls only add explicit constant-order conversion.
log_B₁_gt remains<125ms (repeat96.766 vs before94.440); small arithmetic elaboration is
disclosed. three_small_factors/main_lemma/roth_of_isIntegral pairs overlap pre-edit costs
without a consistent budget regression. Their existing>1000 costs remain later own-audit/
final-file repairs, not passes granted by this worker.

### Whole-file budget result: FAIL, pending final-file repairs

| Foreign module/declaration | First ms | Repeat ms | Disposition |
|---|---:|---:|---|
|ml.exists_delta_bound|12408.373|11188.775|FAIL: final-file repair required|
|ml.four_lt_rpow|818.063|754.120|soft board; repeat done, later own audit|
|ml.three_small_factors|1835.599|1699.293|FAIL: final-file repair required|
|ml.abs_coeff_modByMonic_le|804.066|731.834|soft board; repeat done, later own audit|
|ml.pigeonhole_count|1018.335|1000.235|FAIL: final-file repair required|
|ml.main_lemma|5216.969|4880.648|FAIL: final-file repair required|
|main.exists_m|1968.638|1888.848|FAIL: final-file repair required|
|main.exists_delta|988.719|1041.285|FAIL: final-file repair required|
|main.exists_degrees|1858.969|1810.132|FAIL: final-file repair required|
|main.abs_eval_lt_of_le_index|947.282|854.374|soft board; repeat done, later own audit|
|main.roth_of_isIntegral|3176.075|3044.742|FAIL: final-file repair required|

Earlier exists_delta_bound has a valid failed GLOBAL row, despite prior prefix passes.
Exact pre7 full-file controls11594.369/12164.962ms versus final12408.373/11188.775ms establish
preexisting cost, not an original7-caused failure; they do not dismiss the whole-file failure.
Owner must repair/revalidate before file completion. Pigeonhole1000.235ms is>1000 and not
rounded into a pass. Main exists_delta988.719/1041.285 also fails on its repeat. No Main
original audit, extra declaration credit or file/project completion is claimed.

Read-only extraction rejected short `theorem exists_m` because it also matched
exists_monic_aeval_eq_zero. No incomplete aggregate was accepted. Name-plus-trailing-space
markers preserve identical canonical accounting; all90 subsequently pass, including roth
versus roth_rat. Rejected parser aggregate and corrected report-assembly CLI-slice assertion
retained; captures were not overwritten/rerun for those defects. Final report was initially
read-only444; only this explicitly owned report was made writable, preserving the old f4e…
copy/hash and every frozen145 original tmp artifact. No source edit resulted.

## Gate status — original7 Phase4

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|pass|actual lake build Roth.MainLemma Roth.Main exit0,38.405s|
|definition_protected|pass|exact entry/current diff has no def/abbrev/data-value change|
|theorem_statement_protected|authorized pass|initial GENERALISE18/STRUCTURE12 plus standing authorization; sharp hypothesis, exact paired conclusions and caller full contracts retained|
|structure_gate|pass under explicit task rail|public1/helper2, ordinary≤30, branches≤10; paired API explicitly required, strict helper separately audited|
|naming_gate|pass|clean names, no renames needed/applied|
|line_packing_gate|pass|complete71/74-codepoint table, no dangling token|
|inequality_orientation_gate|pass|complete scan, zero ≥/> in changed Lean signatures/hypotheses|
|actual proof/type/axiom gate|pass|rebuilt imports; independent full old/current target + all4 callers, dependent types/binders/opaque values/std axioms|
|native caller closure|pass|both unfiltered final native calls complete success/zeroerrors/no failed deps|
|original7 performance|pass|all public/helper rows<750, extraction accounted, frozen4-consumer pairs validated|
|whole-file all-row performance|FAIL / owner repair pending|actual foreign hard failures above; no all-file budget pass|
|docstring_only_changes|n/a|authorized code/generalisation cleanup|
|full project build/separate Eval/cumulative project-original closure/Git publication|pending owner|historical project scaffold v1 remains unaccepted|

Overall: original7 per-declaration gates pass; whole-file performance FAIL remains explicit.
Source85af frozen, all17 source/config pins and actual ML/Main olean hashes unchanged through
final native/metadata/profiles. Historical quote/both conclusions exact; exactly four caller
repairs; final7-static-check.json and final7-source.diff. Current helper source/context hashes
saved in final7-helper-source-hashes.json. No report claim of raw generated-name equality.

## Result and required11-phase checklist

Before7 declaration lines→public2+helper3=5 (net saved2); proof bodies6→1+2=3 (saved3).
File695→697 (+2 due to helper/docs); Main684→684. Target issues3 fixed (sharpness/structure/
application documentation); fresh helper separately fixes3 further entry issues.
Rules applied1.6,1.7,1.10,1.17,2.5,2.9 and audit12/18/23. Renames queued:none; shared queue
untouched. Proof comments:none; exact historical quotation and Lean note preserved verbatim.
Refactoring needed:none for original7/helper. Foreign file repairs remain explicit above.

- [✓] Step1 — required skills and five reference documents read.
- [✓] Step2 — all24 concrete audit items answered.
- [✓] Step2.5 — all five actual Mathlib methods/status reported.
- [✓] Step2.6 — every effective binder/candidate, sharpness and public literature reported.
- [✓] Step2.7 — complete measured per-signature-line packing table.
- [✓] Step2.8 — complete inequality scan/orientation check.
- [✓] Step3 — all42 rules have explicit statuses.
- [✓] Step4 — whole-proof/API/term-mode/composition/reflection/alternative strategy checks.
- [✓] Step5a — actual unfiltered ML/Main native complete and clean for target/helper.
- [✓] Step5b — original7 diff/build/proof/contract/axiom/profile gates pass; foreign whole-file FAIL explicit.
- [✓] Step6a — no rename required; sidecar untouched.

All tracked compiler/profile groups, including failed/legacy runs, absent by direct
os.killpg(PGID,0); all native/read-only parser requests returned (final7-drain.json).
All source/compiler/native/profile/report leases revoked/released on final handoff.
Owner independently performs full lake build, separate Eval/native closure/review and
publication before original7 counts as223/264 and ML7/27. No Main audit/file completion.
