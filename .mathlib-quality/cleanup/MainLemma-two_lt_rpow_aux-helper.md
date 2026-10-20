# Roth.two_lt_rpow_aux — helper #2 audit

Status: COMPLETE FOR THIS HELPER AND NECESSARY APPLICATION ONLY. This helper is separate from the 264-original tally;
original10 and the file are not complete. No Git/progress writes or additional helpers.
Evidence: `/private/tmp/roth-mainlemma-two-rpow-helper/` (abbreviated E below).

## Scope and mathematical change

Only the private helper and its sole direct application in `three_small_factors` changed.
`h1 : 1 ≤ δ² log q₁` becomes `h1 : log 2 < δ² log q₁`. The conclusion, other written
binders/order/implicitness, natural q₁/r₁ domain, and nonnegative δ remain unchanged. The
caller supplies this from its existing1-bound via log2<1. All three strict caller conclusions,
its full written contract, prose/source quotations/signpost and all other source are protected.
No private docstring, new imports/options/axioms, sorry/admit, trust extensions or limit raises.

For L=log q₁ and c=log2, the positive hypothesis gives L>0 and natural q₁≥2, hence L≥c>0.
If δL≤c, squaring and multiplying the strict hypothesis by L give
(δL)²≤c²≤cL<δ²L², a contradiction. Finally r₁≥1 gives c<δr₁L, and
`Real.lt_rpow_of_log_lt` gives the claimed strict bound. The estimate remains substantive
mathematics; replacing its premise by the desired linear logarithmic comparison would merely
wrap mathlib and remove the useful squared estimate.

The threshold is the weakest uniform numeric threshold of this form: q₁=2,δ=1,r₁=1
has δ²logq₁=log2 and power=2. Thus ≤ at log2 fails, and every strictly lower uniform
threshold admits this same counterexample. `boundaries-v2` certifies these claims with closed
TYPE/opaque VALUE/inferredtype/standard-axiom checks and actual compilerexit0.

## Phase 0 doctor and Phase 1 preparation

| Check | Actual evidence |
|---|---|
| Optional cache download | skipped: all imports already built; no dependency change |
| Full baseline `lake build` | E/doctor.json:exit0,98.677858708s,PGID65392 drained |
| Full native ML diagnostics | E/native-before.json:success,true;partial,false;timed_out,false;zero errors |
| Baseline warnings | existing header; original10 caller doc long line162. No helper warning |
| Separate runLinter | n/a:no standalone executable configured; actual build/native mathlib linters ran |

Classic dialect. Full MainLemma read, all17 source/config bytes matched the immutable
firstdraft-context before work. Firstdraft helper SHA
`4f07250ae2ad318a874900e1e7dcf15a1d951f091714d7586274b3ada8f0d256`;
entry MainLemma SHA`64e6e3cedaa243a90c6bb35c52e40983b89976b5bf084cbba80e9a60a3040637`;
Main SHA`5f384557dccacaec469699cc7d32bd5666c9d525267e00433b7ae401fee98d09`.
Full commands cleanup/cleanup-all/buzz, both skills, complete854-line worker prompt,
golf/proof/search/generalization/gates/style/naming/profiling/review/principles references,
and future-profiler instructions were read. Truncated combined reads were recovered in bounded
reads. One dedicated leaf audit; no children. Declaration inventory for this helper scope:
private helper146–160,15 declaration lines/13 body lines, non-headline.

## Phase 2 punch-list and Phase 3 file fixes

A.1 existing absent copyright is protected outside helper scope; A.2 module doc present;
A.3 imports unchanged/ordered; A.4 no contentless scoped headers; A.5 entry717 lines;
A.6 no options; A.7 no λ/$/push_neg in helper. B: no helper lint, full file warnings above.
C: meaningful private snake_case name, no docstring,13-line body, substantive squared estimate.
Action: audit the numeric premise, test automation/casts, measure actual helper+caller, and
implement the justified weakening. No file-level fixes were needed/authorized in this scope.
The caller doc long-line issue remains with original10's owner and is explicitly unhidden.

## Phase 4 — all24 audit items

| # | Item | Concrete result/action |
|---|---|---|
|1|LINT|No helper warning; unfiltered full native warning lists retained.|
|2|HAVE|Final hlog2 expression used twice(hL,weighted log bound),keep; hL expression used in hq,square,multiplication,final bound,keep; hq cast-by proof used once,keep proof content; hr cast-by proof used once,keep proof content; hprod contradiction-by proof used once,keep proof content. Old hlog2<1 by-proof removed as no longer needed by helper; caller still has its own existing fact.|
|3|SET_OPTION|None in canonical source; scaffold options temporary only.|
|4|SIMP|No helper simp. Caller adapter uses restricted linarith after actual simpa normalization failure; no hidden nonterminal simp.|
|5|NAMING|two_lt_rpow_aux is mathematical snake_case/private/_aux, no forbidden abbreviation/numeric scheme/_ge_/_gt_. No rename justified.|
|6|PACKING|Complete before/after signature tables below; all breaks justified arithmetically.|
|7|BY|Every by ends preceding line.|
|8|FORMAT|2-space proof,4-space signature continuation,no blank proof lines,semicolon,haveI/letI.|
|9|COMMENTS|Helper0 before/after; caller's one signpost and all docs/source quotes byte-preserved.|
|10|DOCSTRING|None, required for private helper.|
|11|VISIBILITY|Private, sole direct consumer in same file.|
|12|STRUCTURE|13 body lines before/after≤30, no conjunction, contradiction branch6 lines≤10; no extraction necessary. Caller body27→28≤30.|
|13|MATHLIB|Five actual methods and generic automation probes below; partial log/rpow APIs used directly. No exact duplicate found, no absence claim from grep alone.|
|14|JUNK DEF|n/a:lemma, no data definition.|
|15|EXISTS|n/a:no existential witness lemma.|
|16|SHOW|n/a:no show/change in helper.|
|17|PUSH_NEG|n/a:none; by_contra! retained.|
|18|GENERALISE|Every outer/effective inner binder below; accepted sharp uniform bound, certified retained-premise/domain counterexamples.|
|19|INEQUALITY|No reversed ≥/> in Lean signature/body; table below.|
|20|NORMAL FORM|Existing Real.log/Real.rpow with ≤/<; no competing predicate/equivalence/simp normal form.|
|21|SYNTAX GEN|Squared log premise composes with caller's existing condition; linear-log rephrasing would force caller to redo the estimate. No better equivalent call contract.|
|22|IMPORT FANOUT|n/a:no new imports.|
|23|CASTS|Real base coercion, real degree bound and explicit typed log comparison are load-bearing; actual removal probe failed with unconstrained real metavariables. See failed probes.|
|24|INSTANCE NAME|n/a:no instances.|

## Line packing

Raw `#check @Roth.HelperAudit.expected_new` at width100 is in independent-final.log. Private
actual helper's full exact raw TYPE AST is independently checked there; written binders are
preserved, generated macro-scope normalization is restricted to both generated sides.
Widths are Unicode codepoints (not bytes). The entire `(h1 : ...)` is the next signature token.

| State/line | Chars | Next token/width | Arithmetic | Action |
|---|---:|---|---|---|
|before146|78|`(h1 : 1 ≤ δ ^ 2 * Real.log q₁)`/30|78+1+30=109>100|ok|
|before147|66|none(proof follows)|n/a|ok|
|after146|78|`(h1 : Real.log 2 < δ ^ 2 * Real.log q₁)`/39|78+1+39=118>100|ok|
|after147|75|none(proof follows)|n/a|ok|

Conclusion and `:= by` are already packed on the last signature line. No remaining repack.

| Inequality occurrence | Original | Final | Rename |
|---|---|---|---|
|hδ0|0≤δ|0≤δ|none|
|hr₁|0<r₁|0<r₁|none|
|h1|1≤δ²logq₁|log2<δ²logq₁|authorized generalization|
|conclusion|2<q₁^(δr₁)|same|none|
|reversed ≥/> occurrences|none|none|n/a|

## Five actual searches (Step2.5)

| Method | Query/evidence | Actual result |
|---|---|---|
|A Lean-Finder|search-finder.json:nonnegative δ,positive naturals,squared-log bound⇒power>2|Real.lt_pow_of_log_lt,le_zpow_of_log_le etc.; partial log/power comparison|
|B Loogle|search-loogle.json:`Real.log, _ < _ ^ (_ * _)`|empty result|
|C LeanSearch|search-leansearch.json:squared logarithm lower bound implies real power exceeds2|lt_pow_of_log_lt/le_pow_iff_log_le/log_natCast_le_rpow_div; partial|
|D source grep|source-search.txt:log/sq,rpow/exponent/log comparison; full-name search separately retained|existing Real.lt_rpow_of_log_lt and comparison APIs; no local exact squared estimate|
|E local/name pattern|search-local.json:`lt_rpow_of_log_lt`|source hit Real.lt_rpow_of_log_lt; index unavailable, not evidence of absence|

Auxiliary variants checked: lt_pow_of_log_lt,le_rpow_of_log_le,rpow_lt_rpow_of_exponent_lt,
log_pos_iff/log_le_log. Common-equivalent table:no relevant discrete/compact/etc.bucket.
Actual compiled generic-route probes exact?/apply? plus automation are in automation.lean/log:
all failed or recovered sorry, all13 actual values rejected. Consequently no single mathlib
replacement or 1–3-call wrapper was demonstrated. Retain this substantive estimate using
mathlib log/power APIs; no speculative public API extraction/additional helper.

## Generalization2.6a–e (drop-first, outer and effective inner binders)

| Binder | Class/use | Drop/weakening/domain candidate | Actual verification/result |
|---|---|---|---|
|δ:ℝ,implicit|structure value used in square/exponent|drop invalid: appears in conclusion; abstract field would lack Real.log/rpow|Real functions fix ℝ; no artificial typeclass abstraction|
|hδ0:0≤δ|proposition, square-order sign|drop first; replace by mere δ≠0|certified drop_sign:δ=-1,q₁=4,r₁=1 meets other new premises but power≤2. Nonnegative already weakest useful sign form; zero ruled out jointly|
|q₁:ℕ,implicit|structure value, discrete q₁≥2 from log positivity|drop invalid: conclusion depends; Nat→arbitrary real with positivity|certified real_q_fails:q=√2,δ=2,r=1 meets bound but power=2. Adding explicit q≥2 for a real base changes API with no caller benefit; keep natural denominator domain|
|r₁:ℕ,implicit|structure value, positive implies≥1|drop invalid: conclusion depends; arbitrary positive real|certified real_r_fails:q=4,δ=1,r=1/2 gives power=2. Real r≥1 would be valid abstract extension but adds a different domain for a natural degree without a useful caller; not recommended|
|hr₁:0<r₁|proposition, real r≥1|drop first; weaken to0≤r₁|certified drop_r_pos:r₁=0,δ=1,q₁=4 meets bound but power=1; retain|
|h1|proposition, squared logarithmic comparison|drop first; replace1≤ by log2<; weaken strict to≤; uniform lower threshold|drop_bound, bound_equality,any_lower_threshold certify failures; candidate-v2 compilerexit0 proves accepted weaker premise|
|inner h from by_contra!|temporary proposition δlogq₁≤log2, exact negation of strict goal|drop would remove contradiction assumption; no independent API premise|Full hprod proof kernelchecked; not an exposed hypothesis to generalize; branch≤10|
|derived locals hlog2,hL,hq,hr,hprod|proofs, not extra assumptions|inline-single-use test; all expression locals reused, remaining have-by blocks hold mathematics|No unused typeclass/decidability/universe/global continuity binders; no point localization/unbundling applicable|

Positive/generalized proof checked by closed full TYPE and actual VALUE guards. Numeric equality,
δ=0,q=0/1,r=0 and sign/domain controls are actual certified boundary lemmas, stronger evidence
than an unchanged-body unknown-identifier failure. All10 certificates passed together with
actual exit0 in boundaries-v2. Original1-bound contract, including equality1, recovered for
all parameters by exact old-type adapter in independent-final. No conclusion changed.

2.6c big candidates:none recommended; real-domain reformulations above would add abstractions
without a natural-degree/denominator caller. Inversion check:not applicable:no named concrete
object is unfolded away.2.6d literature:n/a private helper, scope rule expressly skips it;
no math-MCP queried.2.6e accepted useful numeric weakening implemented, caller repaired.

## All42 golfing slots (Step3)

| Rule | Actual outcome |
|---|---|
|1.1 by exact|n/a:no wrapper|
|1.2 by rfl|n/a:none|
|1.3 rw+exact|n/a:no rw|
|1.4 simp+exact|n/a:no helper simp|
|1.5 trailing rfl|n/a:none|
|1.6 anonymous constructors|n/a:no conjunction|
|1.7 apply+exact|n/a:apply followed by substantive nonlinear bound, not exact wrapper|
|1.8 by_contra!|already used for squared estimate; preserved|
|1.9 eta reduction|n/a:no lambda|
|1.10 inline single-use have|hL/hlog2 expressions reused; hq/hr/hprod contain by-proofs; no eligible expression remains|
|1.11 apply+intro|n/a:no introduced function|
|1.12 show|n/a:none|
|1.13 obtain projections|n/a:no tuple projections|
|1.14 merge rw|n/a:no rw|
|1.15 terminal simp|n/a:no helper simp|
|1.16 nonterminal simp|n/a:no helper simp|
|1.17 dot notation|hlog2.trans h1,hL.le,hr etc. used; no longer explicit trans combinator|
|1.18 <\||apply with a single positivity proof stays concise; no redundant trailing application parentheses chain to remove|
|1.19 push Not|n/a:no deprecated push_neg; by_contra! retained|
|1.20 trivial exists|n/a:not existential|
|2.1 grind|actual whole-proof probe9 fails; no opaque accepted term|
|2.2 delete before grind|n/a:selected proof has no grind|
|2.3 simpa consolidation|caller adapter actually tried simpa; failed Real2-1 normalization in full build; repaired restricted linarith|
|2.4 fun_prop|n/a:arithmetic/rpow inequality, no function property|
|2.5 positivity|used for positive natural base after q≥2/log positivity; whole-proof probe11 rejected(nonpositivity goal)|
|2.6 gcongr|whole-proof probe12 fails, no progress; cannot create squared log estimate|
|2.7 lia/omega|whole probes5/6 fail on real transcendental estimate; no retained omega|
|2.8 aesop|whole probe10 failed,no progress|
|2.9 norm_num/norm_cast|norm_num discharges concrete2 positivity; exact_mod_cast bridges log→natural q and positive r→real≥1|
|2.10 decide+kernel|n/a:arbitrary real symbolic inequality, not finite computation; no native_decide|
|2.11 field_simp/ring|n/a:no denominator identity|
|2.12 linear_combination|n/a:no ring/ring_nf terminal identity; strict inequality needs order lemmas|
|2.13 wlog|n/a:no symmetric cases|
|2.14 calc term|n/a:no calc block|
|2.15 <;>|n/a:no parallel constructor obligations|
|3.1 erw→rw|n/a:no erw|
|3.2 legacy analysis automation|n/a:none|
|3.3 omega→lia|no retained omega; both actual attempts failed as above|
|3.4 rcases rfl|n/a:no rcases|
|3.5 automation attributes|not recommended:private single-use numeric estimate, no stable simp rewrite/automation trigger|
|3.6 simp_all|n/a:no simp_all only; whole symbolic rpow requires log API|
|3.7 remove limits|none present;0 raised/added|

## Step4 and Phase6.5 holistic simplification

Whole rfl/simp/ring/linarith/nlinarith/lia/omega/exact?/apply?/grind/aesop/positivity/gcongr
were actually compiled in automation probes. Every resulting recovered/open VALUE was rejected,
including partial-search/admission risk; ultimately failed compiler never supplied proof credit.
No one-tactic proof or exact mathlib duplicate was established. The squared comparison is the
mathematical core, isolated as a13-line proof; scalar sign/degree bridges are shared within it.
Term-mode composition would retain both substantive arithmetic subproofs and add nesting.
A different strategy via square-root/division would introduce denominators/side conditions.

The built-in Skill(/simplify) tool is unavailable in this host; its stated reuse/quality/
efficiency review was performed directly in this dedicated helper audit, without claiming an
unavailable tool invocation. Outcome:PASS-THROUGH after applying the useful threshold change.
No duplicated new skeleton/need for another helper, no gratuitous abstraction or scope growth.
Files changed by this holistic pass:none; actual final gates below still required.

## Failed evidence retained (never acceptance)

candidate:first squared comparison failed because weighted log monotonicity was missing;
opaque VALUE guard rejected sorry recovery. candidate-v2 adds exactly that multiplication and
passes. boundaries:first real-q certificate ended with wrong expected arithmetic type; v2 uses
restricted linarith and all10 pass. automation:13 failed or recovered terms,all13 rejected.
candidate-v3-casts:removing explicit typed log-comparison ascriptions left0<?m and ?m≤?m,
then opaque guard rejected; original load-bearing ascriptions retained.
final-build:first caller simpa did not normalize Real2-1; actual buildexit1 retained, repaired
by restricted linarith. No source/proof was accepted on a partial PASS line.

Canonical profile parser initially accepted suffix helper name; full-qualified reparse exposed
a canonical verifier regex limitation (qualified target preceded by space, not dot/start).
Local verify_exact_profile_roots.py changes only proof-name validation to exact full string
following `elaborating proof of `; all other completeness/accounting checks unchanged. Exact
private `_private._stdin.0.Roth.two_lt_rpow_aux` then passes. Owner scripts untouched. Rejection
and precise repair saved; no capture/time was discarded or replaced. No root double counting.

## Phase5a and5b

Nonrename refactoring:accepted numeric premise weakening and necessary hX application only.
Rename queue raw/deduped3; all3 existing exact bytes preserved; helper queues0; no in-place
rename. The project-wide sequential rename pass remains at project end per cleanup-all override.
No conflict/new rename/decomposition flag.

## Final gates, buzz and freeze

Completed: full build-v2, full native ML/Main, independent-final full-contract/closure checks,
matched after profile, bounded deterministic heartbeat cross-check, source protection and
final artifact manifest. No original10/file completion is claimed.

### Actual completed final correctness gates

`lake build` in E/final-build-v2.json exited0 in96.891736875s after actual helper/caller source
repair. This rebuilds MainLemma and affected Main/transitive project modules before final
imported metadata/native/profiles. No subsequent canonical source edit.

Full unfiltered fresh native-final-ml.json and native-final-main.json each report success,
partial=false,timed_out=false,zero errors. All warning items retained: ML header+caller doc
long line162; Main header+unused hδ333,hQ474,hc475. Native results are bound to all17 current
pins in native-final-source-bind.json. No LSP result was partial/timed-out or laundered.

Independent-final-v2 compilerexit0 checks expected-new versus actual unique opaque helper,
immutable firstDraft versus exact old-type adapter, and independent firstdraft consumer versus
actual consumer. Full raw TYPE ASTs, all written/generated binder names/order/BinderInfo,
universes, BOTH TYPE/VALUE closedness, actual opaque VALUE inferred type, and standard axioms
are checked. Only both-generated macro scopes may normalize; no written names normalize.
All six theorem metadata values use only propext/Classical.choice/Quot.sound.
Independent old helper/consumer dependency closures visit238/334 constants and explicitly ban
current actual helper+consumer. No self-reference or use of current consumer supplies old proof.
The prior independent-final v1 failed because numeric private-name components cannot be parsed
as ordinary identifiers; its original bytes are preserved under independent-final-v1-rejected.
V2 constructs the exact actual Name with Name.num and a scratch term elaborator, then all
complete guards pass. No whole opaque VALUE repr was dumped.

New identifiers/ascriptions verified in actual compiled source, independent proof and full build:

| Identifier | Verification |
|---|---|
|Real.log_pos|source search + candidate-v2 + final imported TYPE/VALUE checks|
|mul_lt_mul_of_pos_right|actual candidate-v2 and full final build|
|mul_le_mul_of_nonneg_left|actual candidate-v2 and full final build|
|lt_of_lt_of_le|actual old-contract adapter and full final build|
|Real.log_lt_sub_one_of_pos,zero_lt_two|actual old-contract adapter and full final build|

Additional output-base-cast-negative probe fails and its actual TYPE/VALUE guard rejects it;
real base ascription retained. Along with candidate-v3-casts, this checks both external base
and internal log comparison ascriptions instead of claiming they are redundant.

### Matched buzz pass (Phase6.6)

Outcome:FAST-BOARD for helper and actual direct consumer. No performance-driven proof edit.

| Actual declaration | BEFORE ms | AFTER ms | Budget |
|---|---:|---:|---:|
|private two_lt_rpow_aux|197.486|195.840|1000|
|three_small_factors|495.854|530.039|1000|
|combined disjoint cost|693.340|725.879|1000|

All samples, including combined cost, are below750ms; no repeat requirement triggered.
Every BEFORE capture completed before the API edit. Both full-source scaffolds retain all
actual bodies/types/order, with identical false→true(two complete declarations)→false scope.
Complete CLI:`lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`.
Raw stdout/stderr separate, strictUTF8, hashes, actual exit0/non-timeout,17 immutable source pins
and PGID drain are recorded per capture. Account only disjoint column-zero command+async roots;
exact declaration token/separator anchors; private proof name matched in full; complete proof,
kernel/compiler and lint roots; no Meta/nested/end double count or scoped/global comparison.
A deliberate wrong private target is rejected by the exact verifier (negative-foreign-target*).
No failed target timing was discarded, no unchanged fast third selected, no cost laundering.
Limits removed0/added0; profiling scaffolding in canonical source0. No buzz deferral/new helper.


### Bounded heartbeat corroboration

Custom complete-declaration wrapper counts IO.getNumHeartbeats with only local Elab.async=false,
never a limit change. Effective inherited options printed and checked for both commands/sides:
maxHeartbeats200000,synthInstance.maxHeartbeats20000,maxRecDepth512. Heartbeats-v4 both exited0,
non-timeout,17pins immutable, strictUTF8, owned PGIDs drained. Helper2229→2050 user units;
caller5901→6045. Raw counts2229848/5901911→2050581/6045338 are preserved. This is distinct
corroboration; matched disjoint wallclock roots above remain the performance acceptance gate.
The old heartbeat side is exact frozen firstdraft source replay, imports no current MainLemma,
and is not a new BEFORE wallclock sample or a substituted imported theorem.

Pinned builtin #count_heartbeats internally sets maxHeartbeats0 and was not executed. The
initial bare count_heartbeats syntax (as in skill prose) failed parsing and counted nothing;
v2 bounded custom wrapper passed but did not log effective options. V3 logging wrongly asked
for Repr Options and failed; retained without metric credit. V4 prints registered numeric
limits directly. All failed sources/raw streams/exit statuses retained. No unbounded helper
measurement was performed and no limit was raised, even in scratch.

### Final gates and required11-step checklist

| Gate | Result/evidence |
|---|---|
|lake_build_file/lake_build|PASS:actual `lake build`,final-build-v2.json,exit0; all affected modules|
|diagnostics|PASS:full unfiltered native ML/Main,zero errors; known warnings explicitly above|
|definition_protected|PASS:exact reconstruction protects all definitions/imports/options/other decls|
|theorem_statement_protected|PASS:only authorized audit18 helper premise weakening; exact old adapter and expected-new full AST; consumer contract byte/AST unchanged|
|structure_gate|PASS:helper13/caller28 body lines≤30,helper contradiction branch≤10,no helper conjunction|
|naming_gate|PASS:descriptive private snake_case/_aux,no banned pattern; no rename needed|
|line_packing_gate|PASS:all4 before/after signature rows above,109/118 overflow arithmetic|
|inequality_orientation_gate|PASS:all occurrences above,no reversed inequalities|
|cumulative_no_unintended_breakage|PASS:full project build+native affected Main,independent caller contract|
|standard axioms and closure|PASS:actual opaque values/TYPE/inferredtype+independent old closure guards|
|buzz/re-sweep/no limits/scaffolding|PASS:matched final roots<1000,combined725.879ms; no canonical scaffold or limit addition|

- [✓] Step1 reference documents read completely (bounded/recovered truncations).
- [✓] Step2 all24 audit items, with every have and all scoped warning items.
- [✓] Step2.5 five actual searches plus untruncated full-name grep and compiled generic probes.
- [✓] Step2.6 all outer/effective inner binders,drop-first controls,weakest uniform numeric bound,
  equality/sign/domain checks,private literature scope,accepted weakening implemented.
- [✓] Step2.7 complete measured codepoint signature packing tables and arithmetic.
- [✓] Step2.8 complete inequality table and no reversed code inequalities.
- [✓] Step3 all42 golfing statuses,actual applicable automation/cast attempts preserved.
- [✓] Step4 different strategy/term mode/whole automation/mathlib reuse/holistic review considered.
- [✓] Step5a fresh complete native diagnostics zero errors; warnings disclosed.
- [✓] Step5b actual full build/diff/source/AST/value/axiom/closure/performance gates pass.
- [✓] Step6a helper queues0 renames; existing3 records exact bytes preserved; project-end pass deferred
  by cleanup-all standing scope,not an in-place private rename.

ModeB phases0,1,2,3,4,5a,5b(queue preservation),6,6.5(manual equivalent; tool unavailable),6.6,7
are all recorded above. No silent phase skip or claim of an unavailable Skill invocation.
Total line delta:helper15→15 (body13→13),caller33→34 (body27→28),MainLemma717→718(+1).
The additional application line recovers the previous caller contract while the helper's
numeric premise becomes strictly weaker. No extra helper or deferred helper issue.

### Freeze and release

Final MainLemma SHA`1a0c73dd30f82ef9c684b80262314cc1c449dd92ecf680fc25f76cf8dc370a94`;
helper SHA`28d5e3d918bf76bd34e2a0bbf7e68a32f1d6785d18d5229545201a4f2afecf46`.
Source-protection-final.json restores exactly the firstdraft file after reversing only the
helper and single necessary application; all other16 pins unchanged,renames3 exact bytes.
The standalone firstdraft-helper10 artifact has one final newline beyond the exact extracted
source bytes; corrected firstdraft-exact-source-check.json preserves this initially failed
artifact-equality assertion and verifies the full-context source SHA exactly4f07250a….

Both104-entry project cache snapshots include all local binaries/companions/setup; actual Lake
environment,CLI,--deps and full importArts recorded. All12201 resolved import artifacts were
hashed; external split .olean/.server/.private/IR companions remain byte-stable at their actual
resolved paths. Only the intended imported MainLemma.olean changed; source hash unchanged
since accepted final build. final-manifest.json hashes every E artifact byte, verifies strict
UTF8 or explicitly records actual binary cache exceptions, and binds current17 source/config
pins, all current project cache hashes and this report. It excludes only itself from self-hash.

Entry published HEAD03e09ed remains historical. Owner informed this worker of a source-neutral
metadata erratum publication to596dc28ba76eaa55e0e392fe452f8f133a01b320 during this lease;
17 source/config pins unchanged by that publication. This worker performed no Git/progress writes.

Drain-release.json verifies every owned runner process group absent (including all failed
probes), and releases all source/compiler/native/profile/report leases. Persistent shared LSP
server is not owned or killed. Helper #2 is complete; original10 SAME worker must resume its
own remaining original/caller/boundary/after-profile/gates, and owner retains final file-wide
ALL-row/global/Eval/native/review/publication gates. No original tally increment or file completion.


### Report-only line-count correction

Owner review identified a prose typo: the immutable firstdraft file has717 lines and final
MainLemma has718 (both Python splitlines and wc agree), as already recorded correctly in
source-protection-final.json. The earlier711/712 prose, including initial-audit.md's historical
count, was incorrect; original report/manifest/release bytes are preserved in E/*-v1-line-count-typo.*.
Only this report and evidence metadata changed; all17 source/config pins and all accepted proof,
native/build/performance evidence remain unchanged. No compiler/native/profile/probe was run.
Owner reports current source-neutral metadata HEAD18eaf4b7bb45e2c254d27cbf8c17ecdc7572474d;
596dc28 remains the earlier publication noted above. Report/manifest correction lease released.
