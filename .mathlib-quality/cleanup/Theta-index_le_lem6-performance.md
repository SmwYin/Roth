# Dedicated performance revisit — `Roth.index_le_lem6` (original29)

Scope: second of eight older performance repairs, following the published positive-quadratic
repair at release `fdff81f3d1a2e0d0638584f8c15ab5bb16401cef`. Only this public proof changes.
Its direct consumer `Θ_option_le` is checked in its entirety. The coordinator explicitly
approved this reverse dependency order. Original counts stay216/264, Theta35/35, files9/14.
The original report `Theta-index_le_lem6.md` and every separate helper audit are preserved.
No Git/shared-log/rename-queue mutations, new helper, new API, or dependency-proof edit.

## Baseline, diagnosis, and proposed repair

Inherited doctor: owner's complete full build77.937s THEN separate LeanEval35.334s passed
on the published clean release, all17 source/pin hashes verified. Complete native Theta
and MainLemma diagnostics on that exact baseline are inherited from
`/private/tmp/theta-positive-performance/native-{theta,mainlemma}-final.json`.
No cache download or redundant identical baseline build/native request was needed.

Historical failing actual totals are preserved: 0cb pair1518.596/1343.022ms; 9faa repeat
1480.482ms; release e94 pair1235.462/1644.559ms. The latest direct caller already passed
152.532/167.315ms. These are inherited observations, never relabelled fresh. Exact full
raw/source/table paths and fresh strict raw slices are mapped in `preserved-baselines.json`.

Eight-cause diagnosis from the actual nested hotspots (overlapping rows are not added):

| Cause | Current assessment |
|---|---|
| 1 instance synthesis | No dominant instance-search hotspot identified. |
| 2 fat simp | Final broad `simpa [mul_add]` costs399.836–400.127ms in the diagnostic trace; replace with targeted `simpa only [mul_add]`. |
| 3 defeq | Present within ordinary elaboration; not the primary recorded cost. |
| 4 heavy automation | Weight-bound `lia` costs312.880ms; replace by `hd.trans (Nat.sub_le_iff_le_add.2 hl')`. Repeated positivity solvers replaced by cached order transitivity. |
| 5 mvar churn | Inferred bounds exist, but dominant tactic leaves already explain the concrete repair. |
| 6 coercion churn | Keep necessary Nat→Real bridges; do not alter casts globally. |
| 7 repeated terms | Existing α/Φ aliases retained; r-none positivity shared. |
| 8 kernel/compiler | Included in disjoint final command+async totals; no trust/reduction shortcut. |

The source-only preliminary suggestions were hypotheses; the fresh isolated exact-prefix
`Candidate.lean` compile exited0 in35.240s before application. Final proof has28 physical
body lines,26 nonempty/noncomment proof lines (baseline29/27), with both signpost comments
preserved. Ordinary cap30 applies: this declaration is not a module Main-results theorem.
Each branch/subproof stays≤10. Statement, universes, binder names/order/BinderInfo,
explicit user-retained `hq`, and correlated existential witness remain unchanged.

## Full24-item audit

| # | Item | Result/action |
|---|---|---|
| 1 | LINT | hq is explicitly user-retained. Preserve the named binder and its expected warning; final full diagnostics recorded below. |
| 2 | HAVE SCAN | hrp0 used twice; hr0 repeatedly; hB has proof content; hM1 used twice; hlower/hupper each rewritten before composition. Keep each; inlining defeats sharing/normalization. |
| 3 | SET_OPTION | No production option or limit change. |
| 4 | SIMP | Two nonterminal `simp only` normalization passes unchanged. Targeted terminal simp is a measured performance exception, subject to final real timing. |
| 5 | NAMING | `index_le_lem6` describes an index upper bound and matches none of the forbidden numeric/abbreviation patterns. No rename needed. |
| 6 | LINE PACKING | All8 signature lines measured below; source signature byte-identical. |
| 7 | BY | `by` remains on the final signature line. |
| 8 | FORMAT |2-space proof, no internal blank line/trailing whitespace/semicolon chain; every line≤100 codepoints; no haveI/letI. |
| 9 | COMMENTS | Both original narrative comments preserved in order. |
| 10 | DOCSTRING | Complete public source/reference docstring unchanged. |
| 11 | VISIBILITY | Public contract/wrapper retained under established user choice; no visibility churn. |
| 12 | STRUCTURE |28 physical/26 proof lines≤30; no branch/subproof>10. Shared ∃l conjunction bounds retained exactly. |
| 13 | MATHLIB | Five actual searches below; Nat certificate uses core API directly. Existing substantive private helpers retain separate immutable-FIRST audits. |
| 14 | JUNK DEF | n/a: theorem; local α/Φ improve sharing and readability. |
| 15 | EXISTS | n/a: public substantive existence theorem; D/U/V construction is not a trivial witness wrapper. |
| 16 | SHOW/CHANGE | Existing `show 0 < l from hl` is a term-level cast bridge, retained. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Full parameter inventory and compiled probes below. No contract change in this performance repair. |
| 19 | INEQUALITY |0 reversed ≥/> occurrences in signature/hypotheses. |
| 20 | NORMAL FORM | Index upper bound and one correlated witness are the established useful form; no equivalence proliferation. |
| 21 | SYNTAX-GEN | Current call matches direct Θ_option_le proof naturally; retain. |
| 22 | IMPORT FANOUT | n/a: no new import. |
| 23 | CASTS | New real ascriptions fix the positivity bridge; genuine Nat→Real casts retained;0 redundant new casts. |
| 24 | INSTANCE-NAME | No declared instance/new instance name. Existing ordinary Fintype retained. |

## Search, literature, and inversion

| Method | Query/evidence | Outcome |
|---|---|---|
| A Lean-Finder | Roth lemma polynomial index bound determinant rational point; search-finder.json | Chevalley complexity bounds are unrelated; no replacement returned. |
| B Loogle | Nat.sub_le_iff_le_add; search-loogle.json | Exact core theorem `{a b c : ℕ} : a-b≤c ↔ a≤c+b`; compiled certificate uses it directly. |
| C LeanSearch | Roth polynomial index estimate at rational points; search-search.json | No equivalent public target returned. |
| D mathlib source | Full-name index_le_lem6, lem6Φ/lem6M, sub_le_iff_le_add, index/determinant variants; mathlib-source.log | No target duplicate found; lower-level supporting API found. |
| E local name-pattern | index_le_lem6; search-local.json | Only current project theorem found; index unavailable, so no absence claim from empty index. |

Full literal-current-header anonymous examples test grind/simp/aesop/exact?/apply?/lia/
positivity/gcongr/norm_num/decide in the exact current prefix. Default maxErrors unchanged;
conservative per-example maxHeartbeats2000 bounds searches. Exact?/apply? reach that bound,
so these are bounded outcomes, not a proof of global absence. No named failed theorem or
self target is in this search environment. A separate successful positive absence command
asserts target and all later callers absent. The first absence scratch incorrectly left a
pending omit/docstring and used resolving name quotations; its failing source/log/status
are archived under `failed-prefix-pending-omit-*`. Only corrected exit0 evidence certifies
absence. A transient UTF8 scratch writer failure while saving search output was corrected
using ASCII escapes; the successful saved search JSON is the artifact.

Auxiliary variants: natural subtraction/addition iff, left/right order transitivity,
nonzero determinant and index bounds; common-equivalents table has no matching abstract
compact/discrete/etc. bucket. No new declaration is asserted absent solely on search.

Public literature: fresh searches for polynomial-index Roth lemma/determinant/generalization
returned [Princeton lecture17](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf),
[AMS rational-points chapter](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf), and
[Min Ru notes](https://www.math.uh.edu/~minru/fields/roth.pdf). These give the usual index/
auxiliary polynomial setting, not a verified stronger drop candidate. The authoritative
local source `.mathlib-quality/references/clean.tex:704–741` explicitly has positive degrees/
denominators, 0<δ<1 and r_p>10/δ. Current previously approved contract already weakens the
δ/ratio boundaries and degree cutoff; this proof-only repair adds no literature-based claim.
ChatGPT math MCP is unavailable. Inversion check: the proof needs nonzero integer
coefficients to infer1≤B, the determinant factorization, rational-point coprimality, and
specific index/Θ estimates throughout. Its abstract numerical/weight/mapped-determinant
content is already factored into three separately audited substantive helpers. No further
one-use extraction is justified merely to impose an invented cap15.

## Generality: every effective parameter

| Parameter | Role | Drop/weakening probe and result |
|---|---|---|
| τ : Type* | Arbitrary index type/universe | Already universe-polymorphic; changing its sort is not meaningful with finite cardinality. |
| [Fintype τ] | Card τ and finite sums/Theta | Fresh omit trial rejects omission of a referenced section instance; retain. |
| δ : ℝ | Square root/numeric estimate | Dependent value; dropping type/value makes statement ill-formed. Abstract ordered fields do not support this existing real sqrt/Theta API. |
| hδ0 | Weight and positivity | Fresh drop trial fails current proof; retain already weak0≤δ. |
| hδ1 | Numeric bound | Fresh drop and δ≤2 trials fail the exact numeric-bound premise; retainδ≤1. |
| r | Degrees/weights | Dependent value, occurs throughout statement; no drop candidate. |
| hrp | Cutoff and positive degrees | Fresh drop and0<r-none trial fail; retain3≤r-none. This is proof compatibility evidence, not mathematical necessity of3. |
| hratio | Weight comparison | Fresh drop fails; already pointwise and weak≤. |
| r₁ | Degree upper-bound parameter | Dependent value in M; no smaller abstract type supports factorial/exponents. |
| hr₁ | Degree bound | Fresh drop fails index_det_le application; already exactly the global range needed there. |
| q | Rational denominators | Dependent value in α/Φ; no drop candidate. |
| hq | Explicit retained public premise | Fresh successful body-drop probe records unused-body status only. USER retention is explicit; do not remove, underscore or rename. |
| B | Coefficient bound | Dependent value; hB is derived internally from hR, as previously approved. |
| R | Integer polynomial | Dependent value; specific coefficient/integrality/determinant API used. |
| hR | Nonzero, degrees, coefficients | Fresh drop fails; all components used via factorization/coefficient inference/index_det_le. |
| h | Numerator | Dependent value; cannot drop rational evaluation argument. |
| hh | Point coprimality | Fresh drop fails index_det_le; already pointwise. |

DecEq/hr0/hB are already absent from this target's actual telescope under the published
approved changes. Θ_option_le retains hB/hq and Fintype. No public parameter/API change is
recommended. Negative trials are isolated named declarations; they are never used for
exact?/apply? evidence. `binder-ranges.json`, raw binders.log and hq-drop-positive.log give
all diagnostics and successful positive proof separately.

## Measured packing and inequality tables

| Sig line | Codepoints | Next complete signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 545 | 76 | `(hrp : 3 ≤ (r none : ℝ))` | 76+1+24=101>100 | ok |
| 546 | 83 | `(hr₁ : ∀ j, r j ≤ r₁)` | 83+1+21=105>100 | ok |
| 547 | 72 | `{R : MvPolynomial (Option τ) ℤ}` | 72+1+31=104>100 | ok |
| 548 | 74 | `(hh : ∀ j, IsCoprime (h j) (q j : ℤ))` | 74+1+37=112>100 | ok |
| 549 | 73 | `index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤` | 73+1+63=137>100 | ok |
| 550 | 69 | `2 * (lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +` | 69+1+54=124>100 | ok |
| 551 | 62 | `√(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) := by` | 62+1+62=125>100 | ok |
| 552 | 72 | `proof follows` | n/a | ok |

Each binder is a complete token unit; mathematical conclusion breaks preserve complete
expressions. `packing.json` records exact codepoints, not UTF8 byte lengths. Inequality
scan: hδ0,hδ1,hrp,hratio,hr₁,hq,hl,hl′ and final index comparison all use≤/< with smaller
side left;0≥/> occurrences, no rewrite or _ge_/_gt_ rename.

## Every42 golf rule status

| Rule | Status and reason |
|---|---|
| 1.1 | n/a: no by exact wrapper |
| 1.2 | n/a: no by rfl |
| 1.3 | n/a: no rw+exact pair |
| 1.4 | Already final simpa; tightened only for measured performance |
| 1.5 | n/a: no trailing rfl |
| 1.6 | Already anonymous correlated witness constructor |
| 1.7 | Numeric apply leaves the substantive inequality, so retain |
| 1.8 | n/a: no contradiction |
| 1.9 | Lambdas carry dependent arguments; no eta reduction |
| 1.10 | Each retained non-by have shared or separately rewritten |
| 1.11 | n/a: no apply+intro |
| 1.12 | Term-level show supports Nat cast bridge |
| 1.13 | Already obtain factorization witness and coefficient witness |
| 1.14 | n/a: no consecutive rw |
| 1.15 | Final targeted simp retained as performance exception |
| 1.16 | Both nonterminal simp passes already only |
| 1.17 | Uses trans/trans_le and hd.trans directly |
| 1.18 | No beneficial parenthesis-only churn |
| 1.19 | n/a: no push_neg |
| 1.20 | n/a: no trivial private exists wrapper |
| 2.1 | Fresh bounded anonymous grind failed |
| 2.2 | n/a: no production grind |
| 2.3 | Do not redo rejected mapped-helper consolidation; no scoped simplification merger justified |
| 2.4 | n/a: no analytic regularity goal |
| 2.5 | Fresh whole-goal positivity rejected; scalar positivity handled by direct transitivity |
| 2.6 | Fresh whole-goal gcongr made no progress |
| 2.7 | Fresh whole-goal lia failed; old local lia replaced by exact Nat certificate |
| 2.8 | Fresh whole-goal aesop failed |
| 2.9 | Fresh whole-goal norm_num left goal; norm_num proves0<3 directly |
| 2.10 | Fresh whole-goal decide rejected free variables |
| 2.11 | n/a: no algebraic identity/denominator goal |
| 2.12 | n/a: no ring/ring_nf terminal |
| 2.13 | n/a: no symmetric branches |
| 2.14 | Already trans composition |
| 2.15 | Refine creates one substantive index goal; no similar goal batch |
| 3.1 | n/a: no erw |
| 3.2 | n/a: no legacy regularity tactic |
| 3.3 | No omega introduced; see2.7 |
| 3.4 | n/a: no rfl destructuring |
| 3.5 | No global automation attribute justified |
| 3.6 | n/a: no simp_all only |
| 3.7 | No production set_option or limit raise |

## Design/simplify decision before final expensive validation

No available built-in simplify skill/tool exists here; its holistic reuse/quality/efficiency
review is performed directly: the three inherited helpers retain separate necessity/audit
records, numerical/dependency repairs remain separately queued, and no new helper is
needed. Whole-goal automation does not replace the determinant argument in bounded probes.
Keep the shared positivity fact and targeted Nat certificate; preserve both signposts,
α/Φ sharing, and the exact existential contract. No further static source edit planned.
Final build/native/semantic/profile evidence and frozen handoff are appended after completion.

## Final ordinary, semantic and native gates

No production edit followed the final source snapshot. Sequential fresh commands:

| Command/gate | Exit | Seconds | Evidence |
|---|---:|---:|---|
| build-theta-final |0|29.692| build-theta-final.log/json |
| build-mainlemma-final |0|33.680| build-mainlemma-final.log/json |
| preceding-independent-final |0|27.622| preceding-independent-final.log/json |
| actual-semantics-final |0|155.273| actual-semantics-final.log/json |

The entire preceding366 semantic-check source is an exact byte prefix of the new scaffold,
SHA963c980084d82d7dc605187bfc9a4c591708a0edd9a4d4797f40c4ea0231266c;
all four whole canonical blocks keep their exact hashes72cf/355a/96f1/859a and raw byte
offsets (full hashes in immutable-scaffold-and-blocks.json). No retained-inventory edit or
inverse adaptation was needed. Every preceding check is freshly executed, including the
immutable all29 old public recovery with the approved K/closure/drop map, all11 introduced
helper audits/deletions, whole original MainLemma and independent current MainLemma proofs,
and actual Root9/26 types/opaque values/standard axioms/dependencies.

The complete original Index+Theta namespace containing independent original target29 and
ENTIRE original Θ_option_le is freshly elaborated in this preserved prefix. Its exact
standalone source extraction is OriginalIndexThetaExtracted.lean; this extraction is
byte-identical to the freshly compiled scaffold prefix, not a stale forwarding tail.
The added preceding-current target/caller proof namespace independently re-elaborates
both complete release proofs plus unchanged private context, checks actual type equality,
retained names/order/BinderInfo, exact universe parameters[u_2], conclusion, opaque
value!true/type and standard axioms, nonself proofs and actual Θ_option_le→index_le_lem6
dependency.7 new PASS markers bring the complete successful semantic run to373. A separate
successful independent compile has the same7 markers. Initial scratch universe-name
mismatch arose from omitting the preceding σ section context; failed source/log/status
are archived under failed-universe-context-*. Corrected scratch reproduces that context.
Production never changed for this scratch correction.

Deterministic #count_heartbeats checks: **4825→1946** (both below default200000). The
initial wrapper syntax failure is archived under failed-heartbeat-wrapper-*; corrected
standalone positive runs exit0. No diagnostic scaffolding enters production.

| Complete unfiltered native file | success | partial | timed_out | Errors | Warnings |
|---|---|---|---|---:|---:|
| theta |true|false|false|0|8|
| mainlemma |true|false|false|0|3|

All warnings remain verbatim in native-theta-final.json and native-mainlemma-final.json;
no severity/range filter and no truncated/timeout output certifies this gate. No PANIC,
error or sorryAx occurs in successful ordinary semantic verifiers. Exact frozen source
and pin hashes, and all immutable FIRST source/evidence hashes, are checked again.

## Fresh real profile and buzz result

After every ordinary/native request drained, ran the actual live-module command:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean`

Capture final-first: exit0, no timeout, 256.438s. Full raw log/json/table and scoped strict slices retained.

All50 actual source declarations matched, each theorem/lemma has exactly one anchored
actual proof. Strict UTF8 raw bytes and slices have no invalid/replacement sequences.
Totals add only disjoint command+asyncproof/addDecl/compiler/linter rows; nested
macro/tactic/kernel children are preserved and never double-counted. Exact hashes,
raw byte offsets and component rows are in profile-final-*-strict-slices.json.

| Scope | Inherited release pair ms | Fresh first ms | Fresh repeat ms |
|---|---|---:|---:|
|index_le_lem6|1235.462 /1644.559|498.642|not required|
|Θ_option_le|152.532 /167.315|160.903|not required|

Both scoped totals are below750ms, so no same-source repeat is required or taken.
No third unchanged-source sample or erased failure. Buzz: **FIXED for assigned index29**,
with direct caller passing. No new helper, API change, raised limit or trust downgrade.
Targeted terminal simp is justified by this measured repair plus the heartbeat reduction.

## Remaining mandatory queue and limitations

These six older failures remain separately queued; no whole-file timing PASS is claimed.
MainLemma's actual caller profile remains **unmeasured after its prior bounded cutoff
before main_lemma**. Ordinary build/semantic/native success does not certify its timing.

| Separate older target | Fresh first ms |
|---|---:|
|sum_max_sub_le_index_det|1420.445|
|index_separated_mul_le_aux|1237.218|
|index_det_le|1293.336|
|index_numeric_bound_aux|1103.140|
|lem7_Φ_bound|1281.615|
|lem7_numeric|1253.162|

No new overbudget declaration outside that queue appears in the complete inventory.

Owner alone performs final cumulative/allactual gates, full project lake build THEN
separate Roth.LeanEval and exact-path stage/commit/push/clean. Those gates remain pending.
The original completion counts do not increase for this revisit.

## Gates and eleven-step checklist

| Gate | Result/evidence |
|---|---|
| Module build | Theta then MainLemma exit0, exact commands/status logs above |
| Definition/statement protected | Only assigned proof changed; complete signature and surrounding file bytes identical |
| Structure |28 physical/26 proof lines≤30, each branch/subproof≤10; correlated witness retained |
| Naming/packing/inequality | No forbidden name; all8 measured signature rows;0 reversed inequalities |
| No new trust/limits/scaffolding | Positive opaque/std-axiom checks; static-gates.json; source diff |
| Direct caller | Entire old/current proof/type/opaque value checked; module/native/profile pass |
| Full semantics |373 PASS, immutable previous366 prefix/four whole blocks untouched |
| Real scoped performance | Target and direct caller<1000ms on every final-source sample |
| Full project/Eval/publication | Owner pending, never claimed completed here |

- [✓] Step1: required skills, cleanup/buzz workflow and required reference documents read.
- [✓] Step2: full24 audit, every local fact assessed.
- [✓] Step2.5: five actual searches;10 bounded anonymous trials, corrected separate positive absence.
- [✓] Step2.6: every effective parameter inventoried;10 negative drop/weakening probes; hq positive unused-body probe and explicit retention; public literature/inversion decision.
- [✓] Step2.7: all8 measured signature rows.
- [✓] Step2.8: inequality scan, no reverse orientation.
- [✓] Step3: all42 golf statuses and concrete focused repair.
- [✓] Step4: holistic reuse/quality/efficiency review; no new extraction.
- [✓] Step5a: fresh complete unfiltered native Theta/MainLemma diagnostics,0 errors.
- [✓] Step5b: sequential builds, independent exact old/current semantics,373 checks, real profile and all static gates.
- [✓] Step6a: no renames needed, shared queue/log untouched.

## Complete artifact map and terminal freeze

All new artifacts live in /private/tmp/theta-index29-performance:

| Evidence | Artifact |
|---|---|
| Source/pins/FIRST | baseline-Theta.lean; final-Theta.lean; source-hashes.json; release-source-pin-hashes.json; all-source-pin-hashes.json; all-FIRST-immutable-hashes.json |
| Diff/static/probes | owned-proof.diff; static-gates.json; packing.json; Candidate.lean and candidate.log/json; Automation.lean/log/json; BindersNegative.lean/log/json; bounded-probe-results.json and marker ranges; HQDropPositive.lean/log/json |
| Successful absence | PrefixAbsence.lean and prefix-absence.log/json; failed-prefix-pending-omit-* separately preserved |
| Deterministic cost | Heartbeats-before/after.lean and heartbeats-before/after.log/json; failed-heartbeat-wrapper-* preserved |
| Independent release proof | PrecedingIndependent.lean and preceding-independent-final.log/json; UniverseInspect.lean/log/json; failed-universe-context-* preserved |
| Full mathematical semantics | ActualSemanticsAugmented.lean; OriginalIndexThetaExtracted.lean; actual-semantics-final.log/json; semantic-marker-summary-final.json; immutable-scaffold-and-blocks.json |
| Module/native gates | build-theta-final.log/json; build-mainlemma-final.log/json; native-theta-final.json; native-mainlemma-final.json |
| Historical failures | preserved-baselines.json; baseline-final-first/repeat scoped strict slices; immutable earlier raw/table/source paths in preserved map and dispatch |
| Actual profiles | actual-profile-final-first.log/json/-table.json; optional final-repeat counterparts; profile-final-*-strict-slices.json; exact scoped slice logs; profile-final-*-remaining-queue.json |
| Searches | search-finder/loogle/search/local.json; mathlib-source.log; literature links and local source discussion above |
| Drain/release | pre-profile-drain.json; optional pre-repeat-drain.json; final-process-drain.json; evidence-manifest.json; final-freeze.json |

Final Theta SHA256: `5458997a96e7dfd6c5a86d35e210f86c533b3c4b62a5e532a163b5c80c34fe1a`.

All16 other source/pin files and all prior FIRST evidence hashes match the release.
Final drain confirms every owned ordinary process/group dead and no native request pending.
Terminal release: source/scratch/report authority **REVOKED**; compiler/native authority
**RELEASED**. No further own edit or request follows this frozen handoff.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 68.103 s and 33.964 s.
Theta SHA256 `5458997a96e7dfd6c5a86d35e210f86c533b3c4b62a5e532a163b5c80c34fe1a` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-p02-full.log` and `/private/tmp/roth-theta-p02-leaneval.log`; machine record
`/private/tmp/roth-theta-p02-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this validated revisit before the next source edit. This revisit belongs to the original 29 batch; original counts
remain Theta 35/35, overall 216/264, 9/14 files. No original-count increase comes from revisits or helper audits.
