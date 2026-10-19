# Fresh helper audit: `Roth.sqrt_lt_nat_floor_aux`

Dedicated introduced-helper audit only; original7 `sqrt_lt_floor` remains OPEN.
No original/file/project completion credit is claimed. Counts remain MainLemma6/27,
overall222/264, fully completed files10/14. No Git, shared progress, rename queue, Main,
copyright, author, license, pin, or independent-original edits were made.

Source: `Roth/MainLemma.lean`, entry94–97 (4 declaration /3 body lines), final94–96
(3 declaration /2 body lines). Before4 → after3, saved1; file698 →697 lines.
Final source SHA256: `85af4993b70decb29489013593420d99644a93e2ac6891cecfa7cad5fb2b55f8`.
Worker diff: `/private/tmp/roth-mainlemma-sqrt-helper/worker-term.diff`.
All evidence below is under `/private/tmp/roth-mainlemma-sqrt-helper/` unless qualified.

## Step 1 — References

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md.
Also read installed lean4/mathlib-quality skills, cleanup.md/cleanup-all.md/buzz.md,
the exact saved worker prompt, relevant style-rules sections (formatting, comments,
visibility, inequalities, casts, generalisation), naming-conventions.md, profiling.md,
mathlib-review-stages.md, the prospective scoped-profiler instructions, and both preserved
first/current helper contexts and helper-history.json. No AGENTS.md applies.

The actual first draft is the preserved linarith prerequisite proof, not the later
positivity variant present at worker entry. First-draft declaration SHA256:
`6acacb51195465e4e5a2e8706972ee7adcaf9e2db1567b82bc458f960004a88c`.
Its full context SHA256:
`524044ba0c5530950f2d6ad5d2725b772272161a5330493e0319f3e67927f057`.
Fresh independent first-context compilation passed (44.998s, first-draft.json).
Entry positivity declaration SHA256:
`5c1233dd7d9b3c8052efa3ef9dd49fa4fa7bcbef2110821c9124ffc38dc5efda`.
The prior original7 evidence directory remains untouched.

## Step 2 — Full 24-item audit

1. LINT — none at helper94–96. Unfiltered native-final-term.json returns success=true,
   partial=false, timed_out=false, failed_dependencies=[], isError=false, zero errors.
   Existing file header warning and log_B₁_gt hδ0/hr₁ warnings at138 are outside scope.
2. HAVE SCAN — exactly one: L95 `have hfloor : (2 : ℝ) ≤ ⌊X⌋₊ := by ...`;
   has proof content; two uses in L96 (positivity and nlinarith). KEEP.
3. SET_OPTION — none in helper; no limits, traces or instrumentation enter source.
4. SIMP SQUEEZE — n/a: no simp invocation in selected proof.
5. NAMING — snake_case describes real square root versus natural floor, with required
   private _aux suffix. No forbidden abbreviations, number patterns, _ge_/_gt_, or
   single-letter public declaration. No rename required or applied.
6. LINE PACKING — complete measured signature tables below; all rows pass.
7. BY PLACEMENT — selected declaration is term mode; each nested tactic begins with
   inline `by`. No standalone by line.
8. FORMAT — two-space term indentation, no blank body lines, no haveI/letI, no lambda,
   semicolon, redundant show, or consecutive rewrites. Closed proof arguments use
   one tactic apiece.
9. COMMENTS — none in helper. Exact prefix/suffix comparison preserves every other
   comment, including the paired caller's historical X>4 source quote.
10. DOCSTRING — none, as required for a private helper. Paired public docstring unchanged.
11. VISIBILITY — classic namespace file; private and _aux retained. One actual local caller.
12. STRUCTURE — two body lines, no conjunction, no case branches, no extraction needed.
   Ordinary≤30 and branch≤10 bounds pass; helper is not a named headline result.
13. MATHLIB — five-method block below. Retain the new numerical estimate, building on
   existing sqrt/floor API; no direct replacement found.
14. JUNK DEF — n/a: this is a lemma; no definition changed.
15. EXISTS LEMMA — n/a: conclusion is a strict inequality, not existential.
16. SHOW vs CHANGE — n/a: neither appears.
17. PUSH_NEG — n/a: no push_neg or push Not in helper.
18. GENERALISE — full binder/inner-hypothesis table below. Sharp 2≤X retained;
   all applicable drop and weaker-bound attempts were performed and rejected.
19. INEQUALITY — zero ≥/> in signature or helper hypotheses/body; table below.
20. NORMAL-FORM — already canonical Real.sqrt, Nat.floor, real cast and smaller-left
   inequalities. Natural-floor hfloor restatement was tried and failed the final
   arithmetic step; retain its real-valued form.
21. SYNTAX-GEN — OK: implicit real X and explicit sharp lower bound apply directly
   in the paired caller. No bundled premise or alternative restatement helps this use.
22. IMPORT-FANOUT — n/a: no source import added.
23. CASTS — three explicit ascriptions removed: the positivity proof annotation, its
   zero literal annotation, and the floor cast in the deleted square hint. Zero explicit
   cross-type ascriptions retained; one load-bearing numeric annotation `(2 : ℝ)` retained.
   The genuine natural-floor-to-real coercions remain implicit. Removing that real
   annotation through a natural-floor formulation failed nlinarith; evidence retained.
24. INSTANCE-NAME — n/a: no instance declaration or local instance introduced.

Issues fixed: remove redundant positivity annotation, remove redundant square hint,
compose the sqrt equivalence with its arithmetic proof in term mode. The first-draft
linarith→positivity improvement was independently checked and retained.
Refactoring needed: none for this helper. No new source helper was introduced.

## Line packing — complete per-line tables

Width-100 compiled reference from actual-metadata-v3.log:

`@independentFirstDraft : ∀ {X : ℝ}, 2 ≤ X → √X < ↑⌊X⌋₊`
`@independentSelected : ∀ {X : ℝ}, 2 ≤ X → √X < ↑⌊X⌋₊`

| State / sig line | Codepoints | Next signature token | current+1+next≤100? | Action |
|---|---:|---|---|---|
| Entry94 |74|none; body follows|n/a; complete signature is74≤100|ok|
| Final94 |71|none; term body follows|n/a; complete signature is71≤100|ok|

There are no other signature lines and no dangling conclusion. Final body widths:
L95=67, L96=88 codepoints (measured again by static-check.json).

## Inequality scan — complete signature and hypotheses

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
|1|signature plus all hypotheses|n/a — no ≥/>|none|none|

The only signature inequalities are hX:2≤X and √X<↑⌊X⌋₊. Inner hfloor is
(2:ℝ)≤↑⌊X⌋₊; the generated positivity prerequisite is 0<↑⌊X⌋₊.
No reversed occurrence survives in the body either.

## Mathlib search-status

| Method | Actual query / evidence | Result |
|---|---|---|
|A Lean-Finder|“For a real x at least two, sqrt x is strictly less than the natural floor of x” / search-lean_leanfinder.json|Nat.sqrt_lt_self, real_sqrt_lt_nat_sqrt_succ and related partial facts; no direct real-input estimate|
|B Loogle|`Real.sqrt _, Nat.floor _` / search-lean_loogle.json|floor-of-square-root identity and unrelated number-theory bounds; no direct estimate|
|C LeanSearch|“square root real less than natural floor when two less than or equal” / search-lean_leansearch.json|Nat.sqrt_lt, Nat.sqrt_lt_self, real/natural sqrt comparisons; partial matches|
|D source rg|sqrt/floor, sqrt_lt_nat, sqrt_lt_iff, sqrt_lt', lt_floor_add_one, le_floor in standard sqrt/floor files; untruncated full-name search / search-source.txt, search-full-names.txt|Real.sqrt_lt', Nat.le_floor, Nat.lt_floor_add_one verified; full local target names absent|
|E local names|sqrt_lt_floor, sqrt_lt / search-lean_local_search.json, search-sqrt-lt.json|project target/helper plus standard sqrt API; index unavailable/warming, honestly not used as an absence oracle|

Auxiliary variants examined: sqrt_lt', sqrt_lt_sqrt_iff, sqrt_lt_self_iff,
nat_floor_real_sqrt_eq_nat_sqrt, floor_lt', one_le_floor_iff, le_floor, lt_floor_add_one.
Common-equivalents lookup: no matching discrete/finite/separation/bornology bucket.

Concluded: found partial matches Real.sqrt_lt', Nat.le_floor, Nat.lt_floor_add_one;
ACTION: keep the genuinely new numerical floor estimate and build on that API.
It is not a thin replacement of an existing theorem: nonlinear reasoning from the sharp
threshold is still required. No wrapper or new predicate was introduced.
Fresh compiled generic-route controls in controls-v2.lean reject exact? and all whole-goal
automation tested. apply? is explicitly REJECTED: its purported result contains sorryAx;
the saved tactic state is restored, then a separate closed proof passes standard-axiom checks.
No imported-self shortcut establishes the first draft.

## Generalisation status — all effective binders and inner hypotheses

| # | Hypothesis | Class | Used as | Mechanical candidates actually tried | Verified? | Result |
|---|---|---|---|---|---|---|
|1|{X:ℝ}|structure value|sqrt/floor input|drop explicit binder in actual source|yes, native-drop-X.json|failed at94: X resolves to opened MvPolynomial.X; retained. The type cannot be dropped from the effective telescope|
|2|(hX:2≤X)|proposition|Nat.le_floor at95|drop;0≤X;1≤X, each actual-source native substitution|yes, native-drop-hX/native-weaken-zero/native-weaken-one.json|all failed and reverted. controls-v2 certifies counterexamples at0 and1 and proves the converse √X<floorX→2≤X|
|3|inner hfloor:(2:ℝ)≤floorX|derived proposition|positivity and nlinarith|drop actual source; natural bound2≤Nat.floor X with direct Nat.le_floor|yes, native-drop-hfloor.json; natural-floor-control.json|drop failed positivity/arithmetic; natural variant failed nlinarith; real bound retained|

All local/effective parameters are X and hX; there are no implicit section typeclasses,
type variables, decidability binders or universe parameters. The derived hfloor is the
only named inner hypothesis. Both explicit inequalities are already weak (≤), so strict→weak
does not apply. There is no global function property to point-localise, no bundled
hypothesis to unbundle, and no Type→Type* parameter. Real→abstract field would require a
different square-root operation/conclusion, not a mechanical weakening of this Real.sqrt
statement. Inversion check: no concrete named witness is unfolded away; sqrt/floor remain
the mathematical operations throughout. The positive-floor argument is a proved prerequisite
of Real.sqrt_lt', not an additional input assumption.

Big-change candidates: none. Literature: n/a — private decl, literature search not required.
ChatGPT math MCP: n/a — not required for this private helper.

The sharp converse and false-weakened-contract witnesses in controls-v2.log are independently
kernel checked using only propext, Classical.choice, Quot.sound. Failed native substitutions
include expected direct-caller type errors; no weakening is accepted on that basis.

## Golfing rule pass — all42 rules

Phase1 (instant wins):

- [1.1] n/a: no by-exact wrapper.
- [1.2] n/a: no by-rfl proof.
- [1.3] n/a: no rewrite/exact chain.
- [1.4] n/a: no simp/exact chain.
- [1.5] n/a: no trailing rfl.
- [1.6] n/a: no conjunction constructor in helper.
- [1.7] applied: compose Real.sqrt_lt'.2 with the closed arithmetic argument; term mode saves one line.
- [1.8] n/a: no contradiction/push-neg chain.
- [1.9] n/a: no lambda.
- [1.10] hfloor has by and is used twice; retain, no single-use term-have to inline.
- [1.11] n/a: no intro after apply.
- [1.12] n/a: no show.
- [1.13] n/a: no conjunction projections from a have.
- [1.14] n/a: no rw.
- [1.15] n/a: no terminal simp only.
- [1.16] n/a: no nonterminal simp.
- [1.17] .2 projection already uses dot notation; no eligible receiver rewrite.
- [1.18] n/a: parentheses are needed for the equivalence projection; <| would not simplify it.
- [1.19] n/a: no push_neg.
- [1.20] n/a: not an existential lemma.

Phase2 (automation upgrades):

- [2.1] tried whole-proof grind via native attempts and closed control; failed.
- [2.2] n/a: no selected grind prefix.
- [2.3] n/a: no simp consolidation.
- [2.4] n/a: no function-property goal.
- [2.5] retained/independently verified: first-draft linarith positivity prerequisite → positivity.
- [2.6] n/a: sqrt X versus floor X is not a matching-argument monotonicity/congruence chain.
- [2.7] tried lia and omega in controls; both fail on the nonlinear real/floor goal.
- [2.8] tried aesop; fails, no progress.
- [2.9] norm_num fails whole goal; exact_mod_cast remains necessary for the real floor bound.
  Natural-bound/direct-Nat.le_floor alternative was compiled and rejected.
- [2.10] n/a: real inequalities with arbitrary X are not finite executable decidable data.
- [2.11] n/a: no denominator equality.
- [2.12] n/a: no terminal ring/ring_nf equality.
- [2.13] n/a: no symmetric cases.
- [2.14] n/a: no calc block.
- [2.15] n/a: no multiple similar subgoals.

Phase3 (cleanup):

- [3.1] n/a: no erw.
- [3.2] n/a: no legacy continuity/measurability tactic.
- [3.3] lia was tried first; no omega remains in source.
- [3.4] n/a: no rcases.
- [3.5] n/a: private numerical helper is not a canonical global rewrite/automation rule.
- [3.6] n/a: no simp_all only.
- [3.7] n/a: no source maxHeartbeats, maxRecDepth or synthInstance limit raise.

## Step4 — Step back

Whole-goal grind, simp, aesop, lia, omega, norm_num and exact? do not close the goal.
apply? only supplies partial admitted search output and is rejected. The final proof keeps
the useful real floor bound, removes the redundant sq_nonneg hint, and expresses the
remaining equivalence/application in term mode. Both a compact tactic version and the final
term version were compiled; heartbeats corroborate the simplification. The natural-floor
variant fails, so the real annotation is supported by evidence rather than guesswork.

Mathematics: n=floor X≥2, X<n+1, hence X<n²; positive n lets Real.sqrt_lt' conclude √X<n.
The paired caller still packages that strict lower bound with Nat.floor_le; BOTH conclusions
are preserved and its exact source is unchanged.

## Actual compilation, contract, proof and value checks

- Fresh original-context compile: first-draft.json, exit0,44.998s, no self import.
- First/compact independent proof bodies and standard axioms: candidates.json, exit0.
- Simplified arithmetic without the square hint: no-square-hint.json, exit0, standard axioms.
- Positive automation/sharpness/false-weakening controls: controls-v2.json, exit0.
- Final actual affected module: final-term-build.json; `lake build Roth.MainLemma`,
  exit0,41.586s. Build warnings are the existing outside-helper warnings.
- Actual imported private name: `_private.Roth.MainLemma.0.Roth.sqrt_lt_nat_floor_aux`,
  obtained from the rebuilt environment, not a scratch alias.
- actual-metadata-v3.json compiles independent first-draft and selected proof bodies,
  two actual-private old/current contract adapters, and checks exact full raw type AST,
  every dependent binder type/name/order/BinderInfo, universes, actual theorem kind,
  opaque proof-body inferred types and transitive standard axioms.
  Raw old/current names are preserved without normalisation; no eraseMacroScopes was needed.
- Expected telescope: X implicit Real, hX explicit/default2≤X; universe parameters empty.
  Both adapters recover the full original helper signature. Raw opaque bodies are retained
  in actual-metadata-v3.log. Independent proof-closure checks exclude the current helper
  and paired public theorem (183/187 visited constants, per actual final log).
- final-imported-module.json hashes the actual rebuilt olean and verifies it stays unchanged
  through actual-private verification. No definition or data value changed: source outside
  the helper is byte-identical to worker entry (static-check.json).

## Buzz — matched scoped first-draft/final captures

Required real command template used for BOTH captures:

`/Users/ramin/.elan/bin/lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`

Temporary scaffolds preserve all actual declaration bodies/types/order, substituting only
the selected helper proof. Trace is false over unrelated prefix/suffix, true over the exact
helper and actual paired caller, starting before the leading caller docstring.
No committed source instrumentation. Construction checks and all17 source/config pins,
actual CLI, input/scaffold SHA, separate strict-UTF8 stdout/stderr hashes, complete exit/timeout
metadata and actual PGID absence are preserved.

| Declaration | First draft | Final | Heartbeats first→final |
|---|---:|---:|---:|
|sqrt_lt_nat_floor_aux|129.381ms|95.857ms|1369→825|
|actual paired sqrt_lt_floor|21.728ms|17.544ms|142→140|

Canonical anchored_profile_span.py and verify_profile_roots.py validate exact unique
command→next-command spans and complete matching named proof, compiler/kernel and lint roots.
Only column-zero Elab.command and Elab.async disjoint roots are added; internal Meta/nested
events, preceding roots and adjacent/end commands are excluded. No unmatched scoped/global
comparison. Both helper/caller samples are below750ms; no repeat required.
Outcome: FAST-BOARD, no helper/caller profile failure or deferral, no limit raises.
Heartbeat measurement uses a bounded custom command disabling only Elab.async, preserving
the current heartbeat limits; built-in count_heartbeats was avoided because its implementation
temporarily sets maxHeartbeats0. Exact final helper/caller bodies are measured in heartbeats-v3.
Final whole-file global ALL-row profiling remains parent/original7 duty.

## Retained rejected/intermediate evidence

- native-candidates.json: scratch native diagnostic path outside any project rejected by MCP;
  this is not claimed as a native pass. All mechanical substitutions and final diagnostics
  were subsequently run on the actual project source.
- attempts-native.json: apply? gives partial suggestions with apparent zero goals; not accepted.
- controls.json: first harness had invalid solve syntax and consequently failed its explicit
  axiom guard. Retained and repaired as controls-v2, whose accepted proofs all have standard axioms.
- actual-metadata.json: numeric private-name quotation failed parsing; retained, replaced by
  environment name lookup in v2/v3. Its failed adapters are not positive evidence.
- heartbeats.json: first counter lacked a CommandElabM options instance; retained and repaired
  using a scoped command option in v2/v3, without raising any limits.
- natural-floor-control.json: arithmetic proof fails; sorryAx from failed elaboration is
  explicitly rejected. The real-valued hfloor is retained.
- v2 metadata/build/heartbeat and compact candidate evidence correspond to intermediate proofs;
  final acceptance uses v3 metadata, final-term-build and after-term-profile only.
- Prior original7 malformed global UTF8/unknown-exit evidence remains frozen and rejected in
  its own report; this worker does not reuse or overwrite it.
- A ps inspection was denied by the sandbox. Actual os.killpg(PGID,0) absence checks, rather
  than ps output, supply the final drain evidence.

## Gate status — Phase4

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|pass|lake build Roth.MainLemma exit0,41.586s; final-term-build.json|
|definition_protected|pass|no def/abbrev or data value changed; exact outside-helper comparison|
|theorem_statement_protected|pass|same full signature/type AST/telescope/universes; only proof syntax/body changed|
|structure_gate|pass|2 body lines, no ∧ or branches|
|naming_gate|pass|descriptive snake_case, private _aux, no forbidden pattern; no rename|
|line_packing_gate|pass|complete71-codepoint single-line final signature table|
|inequality_orientation_gate|pass|complete scan; zero ≥/>|
|no_limit_raise / no_scaffolding|pass|none added to actual source|
|actual direct caller|pass|unchanged full paired caller builds, native clean, complete scoped profile|

Overall: pass for this helper only.
Renames-queued: none. Comments-preserved: none in helper; every outside comment preserved.
Refactoring needed: none for helper.
Audit issues found3 additional to entry, fixed3; first-draft positivity improvement also
independently validated. Applied rule1.7, retained/verified2.5, plus Step4 and cast/hint cleanup.

## Required phase checklist — all11

- [✓] Step1 — installed skills/reference docs read.
- [✓] Step2 — all24 audit items concretely answered.
- [✓] Step2.5 — all five actual mathlib searches reported.
- [✓] Step2.6 — every effective binder and inner hypothesis audited.
- [✓] Step2.7 — complete measured signature width tables.
- [✓] Step2.8 — complete inequality scan.
- [✓] Step3 — all42 rules have explicit status.
- [✓] Step4 — whole automation, API search, term mode and alternative cast strategy checked.
- [✓] Step5a — actual unfiltered native-final-term diagnostics clean.
- [✓] Step5b — actual build/contract/proof/profile and all diff gates pass.
- [✓] Step6a — no helper rename required; shared queue untouched.

## Handoff scope

ALL helper source/report/compiler/native/profile ownership released and drained upon return.
final-drain.json independently rechecks every actual tracked PGID (including failed runs);
all native requests returned. No compiler, native request, profiler or outer runner remains
owned by this worker after the final sequence joins.

Original7 remains open. The same original7 worker must resume its final global after-captures,
required repeats, causal-regression checks, complete report and owner-build/publication gates.
Project-original cumulative historical scaffold and final whole-file global ALL-row gates
remain the parent's duties. Previously slow three_small_factors/main_lemma/Main.roth_of_isIntegral
remain their separate later audit queues. No Main audit credit, original7 completion credit,
file completion or project completion follows from this helper audit.
