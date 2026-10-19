# Positive quadratic helper: dedicated performance revisit

Scope: `Roth.mul_sq_div_three_le_sum_max_of_pos_aux`, first of eight older Theta
performance revisits. This is a proof-only repair, with no new helper, API change,
caller edit, Git mutation, shared-log write, or progress-count increase. Original progress
remains 216/264, Theta 35/35, completed files 9/14; Theta file-final gates remain separate.
The historical dedicated helper and min reports remain untouched.

Artifacts below use `/private/tmp/theta-positive-performance/` unless an absolute path is given.
Frozen published input: `34493e4989783bcfaa229321308016f3131042ff`.
Baseline Theta SHA256: `cfa05489380deeae6eb1bc63202249c3754b791357912aabff24e29e1cae4788`.
The owner supplied successful sequential full project and separate LeanEval builds
(61.547s then 31.863s) and full final native diagnostics on that identical baseline.
Those are inherited baseline evidence, not fresh leaf builds.

## References and diagnosis

Read the Lean and mathlib-quality skills, complete cleanup worker workflow, full
`golfing-rules`, `proof-patterns`, `mathlib-search`, `generalisation-patterns`,
`cleanup-gates`, relevant style/naming sections, and full buzz/profiling workflow.
Standing leaf instructions and the complete current positive-revisit dispatch govern scope.

Historical 9faa pair **1074.965 / 908.077ms** remains a failed first sample followed by
its repeat. Current cfa pair **903.926 / 781.005ms** is the inherited baseline, not an
erasure of that failure. `preserved-profile-pairs.json` independently verifies the exact
source and raw log SHA256, strict UTF-8 decoding, selected byte offsets, complete proof
anchor and disjoint rows for all four observations. Four strict slices preserve those
observations locally. Original complete raw logs/tables/sources remain in their immutable
`/private/tmp/theta35-phi-fresh/` and `/private/tmp/theta35-prefix-performance/` locations.
No third unchanged-source sample was used for acceptance.

The actual first failed sample has `linarith only` at **394.627ms** and outer
`field_simp` at **166.205ms**. `historical-and-baseline-hotspots.json` independently
extracts these raw lines with exact byte offsets and hashes from the strict first-failure
slice, as well as both baseline samples. The failed source's repeat diagnostic identifies
the local arithmetic block
(272.363ms inclusive; `linarith only` child 220.889ms), the scaling identity's broad
`field_simp` (135.555ms), and 113.983ms asynchronous lint. These diagnostic rows overlap
and are **not added together**. Aggregate failure totals come exclusively from the
anchored disjoint table rows, never nested macro/kernel double counting.

| Taxonomy cause | Diagnosis |
|---|---|
| 1 instance synthesis | No dominant repeated failing synthesis trace; no instance changes warranted. |
| 2 fat simp | `field_simp` carries broad normalization work for a single division identity; replace with targeted `eq_div_iff` and polynomial normalization. Existing finite-sum simp is already explicit and retained. |
| 3 defeq | No independent dominant unification blowup; no casts/type hierarchy changed. |
| 4 heavy automation | Arithmetic certificate search is avoidable: provide the exact nonnegative linear combination. |
| 5 metavariables | No wide retry signature establishing missing expected types as primary cause. |
| 6 coercions | Existing cast normalization occurs once at hsum and once at the finite-sum bridge; retained. |
| 7 repeated subterms | `n` already shares the floor; scalar generalization already isolates θr. No new sharing helper needed. |
| 8 kernel/compiler | Separate addDecl/linter overhead is preserved in totals; reduce proof search/normalization rather than masking overhead. |

## Repair and mathematical content

Write a=θr, n=⌊a⌋, and T=∑ν<n+1 ν. The exact identity 2T=n(n+1) gives

`(n+1)a − T − a²/3 = a²/6 + a/2 + (a−n)(n+1−a)/2`.

Every term on the right is nonnegative: a≥n≥0 and n≤a<n+1. Replace `linarith only`
with this explicit `linear_combination` certificate. Replace `field_simp` in the
scaling identity with `(eq_div_iff hr.ne').2 (by ring)`. The rest of the proof still
divides by positive r, compares each summand to its positive part, and extends the range.

`Candidate.lean` tests the explicit certificate; `CandidateRing.lean` tests the targeted
identity in tactic form; `CandidateFinal.lean` tests the exact selected final term form.
Each is an exact pretarget-prefix proof with exit0, and no imported target theorem.
`owned-proof.diff` contains the entire live change. All other source bytes, comments,
imports, declaration names and callers are identical to the baseline.

Scratch-only deterministic comparison: `heartbeats-before-corrected.log` reports
**2624**, `heartbeats-after.log` reports **2111** (513 fewer, about 19.6%). The initial
before probe used unsupported `count_heartbeats in` syntax; its exit1/source/log/status
are retained. Corrected probes use pinned `#count_heartbeats in`, both exit0, at the
same unchanged default maximum 200000. No counting/profiling option enters production.

## Full 24-item audit

| # | Item | Current finding/action |
|---|---|---|
| 1 | Lint | No target-range warning in candidate; final complete native diagnostics recorded below. Other retained public-hypothesis/header warnings remain outside this proof's scope. |
| 2 | Have scan | hnle used in generalization, a≥0 and product certificate; keep. hnlt is generalized before its single certificate use, so inlining its original floor expression would lose the scalar relation; keep. hsum is transformed by push_cast, then used in the certificate; keep. hbound has a substantive six-line subproof; keep. No disposable one-use untransformed fact. |
| 3 | Options | No production option, limit raise, or linter suppression. |
| 4 | Simp | Existing sum/division `simp only` is nonterminal and explicitly restricted; keep. Broad `field_simp` removed. |
| 5 | Naming | Descriptive snake case, positive-case `_aux`, no numeric scheme or forbidden abbreviation. No rename. |
| 6 | Packing | Both signature lines measured below; unchanged and packed. |
| 7 | By | All tactic/local `by` tokens end their preceding line; selected identity uses term form. |
| 8 | Format | Two-space proof indent, four-space signature continuation, ≤100 columns, no blank body line or semicolon chain. |
| 9 | Comments | No comment in assigned original body; none removed. Outside narratives byte-identical. |
| 10 | Docstring | Private auxiliary has none; retain. |
| 11 | Visibility | Private substantive floor estimate, one boundary-wrapper caller; retain. |
| 12 | Structure | 22→22 body lines, ≤30; hbound six lines, each calc subproof ≤10, no case branch or conjunction. |
| 13 | Mathlib | Five actual searches plus clean bounded automation below; no complete replacement established. |
| 14 | Junk def | n/a: proposition, no new def/abbrev. |
| 15 | Existential | n/a: no existential statement or trivial witness helper. |
| 16 | Show/change | n/a: neither occurs. |
| 17 | Push-neg | n/a: none. |
| 18 | Generality | Every effective parameter tested; preserve FIRST six-binder core because existing wrapper already supplies broader boundary result. |
| 19 | Inequality | Four signature occurrences already use smaller-left `<`/`≤`; no rename or reversal. |
| 20 | Normal form | Real finite-range sum of positive parts; standard mathlib operations, no custom predicate. |
| 21 | Syntactic generality | Current implicit data / explicit proof arguments apply directly in the sole wrapper; no supported restatement needed. |
| 22 | Import fanout | n/a: imports unchanged. |
| 23 | Casts | The old linarith argument's proof-type and `(0 : ℝ)` ascriptions disappear: hnle now fixes the real type of Nat.cast_nonneg n. No cross-type coercion added/removed. Retain `(n : ℝ)` as genuine Nat→Real and `Nat.cast (R := ℝ)` as the load-bearing cast-map target. |
| 24 | Instance names | n/a: no instance introduced and no effective class/universe binder in this numerical helper. |

## Signature packing and inequality gates

Widths are Unicode codepoints, including `:= by`. Actual effective type is also printed
at `format.width 100` in the successful final semantic probe.

| Line | Width | Next complete token | Arithmetic | Action |
|---|---:|---|---|---|
| 317 | 96 | `(hl : θ * r < l)` (16) | 96+1+16=113>100 | keep |
| 318 | 84 | proof body follows | n/a | keep |

| Occurrence | Location | Orientation | Action |
|---|---|---|---|
| 1 | hr | 0<r | keep |
| 2 | hθ | 0≤θ | keep |
| 3 | hl | θr<l | keep |
| 4 | conclusion | rθ²/3≤sum | keep |
| 5 | complete signature | no ≥ or > | no rewrite/rename |

## Five actual mathlib searches and automation

| Method | Current query / artifact | Result |
|---|---|---|
| A Lean-Finder | Quadratic lower bound finite sum max zero arithmetic progression theta minus n / positive radius; `search-finder.json` | FloorPow/Hurwitz/Zeta estimates do not supply this finite positive-part bound. |
| B Loogle | `Finset.sum, Max.max, _ ≤ _`; `search-loogle.json` | Finset.max_sum_le is a pointwise max/sum comparison, not the floor-based quadratic bound. |
| C LeanSearch | quadratic lower bound positive parts sum arithmetic progression floor; `search-search.json` | Floor/division bounds, no whole-result match established. |
| D Source rg | Full helper name, sum_max/square variants, sum_range_id_mul_two, subset nonnegative sum and eq_div_iff; `mathlib-source.log` | No full-name or square/sum-max hit; verifies actual building blocks, targeted division lemma. Log contains complete untruncated searches and exit codes. |
| E Local name | sum_range_id; `search-local.json` | Both arithmetic-progression sum identities found. Index unavailable, so no indexed absence claim. |

Auxiliary variants assessed: exact range-sum identity, subset sum monotonicity,
max-sum comparison, floor inequalities. None of the custom-concept replacement buckets
applies. This helper proves substantive mathematics, not a one-to-three-call wrapper.
No broad claim that mathlib lacks any equivalent follows from bounded failed searches.
No complete direct replacement established, so retain the elementary proof.

`PrefixAbsence.lean` separately compiles exit0 and asserts the audited private target,
its wrapper and public min are absent. `Automation.lean` uses the literal current header
as anonymous examples against the exact current source prefix **before** the target,
without importing Theta or naming failed theorem trials. `exact?`, `apply?`, grind, simp,
aesop, positivity, gcongr, lia, norm_num, decide, field_simp/ring, and nlinarith were tried.
All fail to close. `apply?` returns incomplete generic transformations and reaches the
conservative 5000-heartbeat budget; no suggested limit increase was adopted. The batch
exit1, every error/suggestion and all source ranges are retained. This is not positive
axiom/absence verification. Repeated known stalled full-Theta native multi_attempt was
not retried; bounded compiler exploration completed and drained.

New-identifier verification: `eq_div_iff` exists in
`Mathlib/Algebra/GroupWithZero/Units/Basic.lean:348`; the selected exact instance and
`linear_combination` tactic compile in both the positive candidate and final module.
The remaining nonnegativity APIs already occurred in this proof. No fabricated name.

## Every effective parameter: drop and weakening probes

`BindersNegative.lean` uses autoImplicit=false and copies the selected final proof for
all eight trials. Exit1 is expected and each trial's error range is retained in
`binder-ranges.json`; no maxErrors increase. `Boundary.lean` is a fresh successful
recompile of the immutable independent initial proof, broader radius/cutoff proofs and
two explicit counterexamples, with standard axiom output. It calls neither the actual
current positive target nor its downstream wrapper.

| Effective binder | Trials | Evidence and decision |
|---|---|---|
| θ : ℝ | Drop | Unknown θ in statement/proof. Essential value in square/cutoff/summands. |
| r : ℝ | Drop | Unknown r in statement/proof. Essential divisor and scale. |
| hr : 0<r | Drop; weaken to 0≤r | Current proof fails missing positive cancellation/division. Independent unrestricted-r proof compiles by nonpositive case plus immutable FIRST core. Existing wrapper already does this; retain positive core. |
| hθ : 0≤θ | Drop | Floor premise unavailable. θ=-1,r=1,l=0 refutes unrestricted result; nonnegativity already weakest useful boundary. |
| l : ℕ | Drop | Unknown l in range/cutoff. Essential data value. |
| hl : θr<l | Drop; weaken to ≤ | Floor range inclusion fails; θ=4,r=1,l=1 refutes absent cutoff. Independent equality-inclusive proof compiles with preceding linear estimate; existing wrapper already states this boundary. Retain strict core. |

No effective universe/typeclass/decidability binders exist here; exact compiled FIRST6
metadata comparison checks this rather than reading only surface syntax. Abstract
ordered-field/floor restatement was assessed: no current caller benefits enough to
warrant changing this private real-only core. Literature search is n/a for this private
helper. Inversion check: no named Roth-specific concrete object in the statement;
already arbitrary θ,r,l and standard finite sums. No additional API recommendation.

## All 42 golfing rules

| Rule | Result/action |
|---|---|
| 1.1 by exact | n/a: none. |
| 1.2 by rfl | n/a: none. |
| 1.3 rwa | n/a: no rewrite followed by a closing exact. |
| 1.4 simpa | Existing sum/division simp changes the goal before termwise sum comparison; no existing whole premise to simpa. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructors | n/a: no product/conjunction. |
| 1.7 apply/exact | Selected scaling step directly applies eq_div_iff rather than retaining the tested apply block. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta | The two sum callbacks ignore indices; not eta expansions. |
| 1.10 one-use have | All four facts retained for transformations/reuse/subproof content as detailed in audit item2. |
| 1.11 refine/fun | n/a: no apply/intro pair. |
| 1.12 redundant show | n/a: none. |
| 1.13 obtain | n/a: no projections from a conjunction. |
| 1.14 merge rw | n/a: no consecutive rewrite calls. |
| 1.15 terminal simp | n/a: sole simp is nonterminal. |
| 1.16 squeeze simp | Existing nonterminal simp has an explicit list. |
| 1.17 dot notation | Existing .2, .ne', .le retained; targeted division proof uses .2. |
| 1.18 trailing parentheses | Parentheses identify certificate summands/lemma hypotheses; no removable trailing lambda/tactic wrapper. |
| 1.19 push Not | n/a: none. |
| 1.20 trivial exists | n/a: no existential helper. |
| 2.1 grind | Fresh clean anonymous whole-proof trial fails. |
| 2.2 before grind | n/a: no production grind; whole-goal trial already discards setup. |
| 2.3 simpa consolidation | Assessed with1.4; whole-goal simp trial fails. |
| 2.4 fun_prop | n/a: no function regularity goal. |
| 2.5 positivity | Fresh whole-goal trial reports not a positivity goal; explicit product/square witnesses remain direct. |
| 2.6 gcongr | Fresh whole-goal trial makes no progress; positive division lemma already supplies the monotone step. |
| 2.7 lia | Fresh whole-goal trial fails for nonlinear real finite-sum estimate; no omega introduced. |
| 2.8 aesop | Fresh anonymous trial fails to progress. |
| 2.9 norm_num/cast | Whole-goal numeric trial leaves goal; existing centralized push_cast retained. |
| 2.10 decide | Fresh trial rejects free variables. |
| 2.11 field_simp/ring | Whole-goal trial fails; local field_simp replaced by targeted eq_div_iff plus ring. |
| 2.12 linear_combination | Applied exact polynomial certificate, eliminating linarith search. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 calc | Four different mathematical transitions; no redundant two-step calc. |
| 2.15 <;> | n/a: no repeated similar subgoals. |
| 3.1 erw | n/a: none. |
| 3.2 regularity | n/a: no continuity/measurability. |
| 3.3 omega→lia | Covered by2.7; no omega. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attrs | Private specialized estimate; no global registration or simp normal-form change recommended. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 limits | No production raise or masking; none added. |

## Step back, helper retention, simplify and static gates

Clean automation does not establish a one-tactic replacement. The selected proof displays
its arithmetic certificate, then follows the mathematical finite-sum argument. Integral
comparison would add analysis machinery for this elementary estimate. No new extraction
is needed: both the whole proof and every local block fit the required caps. Retain the
positive helper because inlining this substantive floor argument into the boundary
wrapper would create a branch longer than10 lines. Retain the existing boundary wrapper,
which supplies nonpositive-radius and equality cases for min. This is a technical clarity
choice supported by actual callers, not a user veto on API improvement.

All11 previous helper deletion/retention audits and prefix-pre35 repair remain intact.
No historical introduced-helper audit is treated as this fresh revisit, and no fresh
helper/count increase is claimed. No optional generality candidate is a blocker.

Holistic simplify performed directly (no callable built-in simplify skill is exposed):
ISSUES-FOUND-AND-FIXED. The unnecessary search and broad denominator normalization were
replaced with the exact certificate/lemma. No remaining duplicated proof skeleton needs
another helper. All static decisions were completed before final validation/profiling.

`static-gates.json`, `owned-proof.diff`, `packing.json` prove: only the assigned proof
changed; signature and all outside source bytes match; no def/abbrev/import/visibility/name
change;22 lines, local arithmetic block six lines; ≤100 columns; no lost narrative,
TODO/FIXME, sorry/new axiom/native_decide, raised limit, or production profiling scaffolding.
Phase5a additional refactoring: none. Phase5b renames: none; queue untouched.

## Exact FIRST and entire semantic preservation

Immutable FIRST helper source:
`/private/tmp/roth-theta-quadratic-helper/new-helper-initial.lean`, SHA256
`bbfaa4824d09a1f10356cbeb795bfae23d296889f76a675a576bfaedcaa2225c`.
Full FIRST introduction/context SHA256:
`7685f1536fd898cfe55e148154245193b37cb1c23bd642dd32bcea7429f265c5`.
Historical independent FIRST source/log SHA256:
`464a44a93b4eb1c365d8f34d911e363850b61d9a40806588e30494c4945feff9` /
`2de42ddbba407bfa829991c0efbde5ed6659f36ffa1dd34178e9a6b600567ad7`.
`first-immutable-hashes.json` rechecks all four immutable files.
`all-FIRST-immutable-hashes.json` additionally rechecks all13 supplied preceding/current
FIRST source and success-evidence hashes; none changed.

`FirstContextIndependent.lean` extracts the exact original source prefix through the
FIRST target from the full introduction snapshot, closes its actual Lemma6/Roth scopes,
and independently checks its real opaque proof value/type/standard axioms. No current
Theta import or actual target call proves that FIRST proof. Full original source snapshot
is also retained locally as `FirstIndependent.lean`; extraction offsets/hash are recorded
in `first-context-map.json`.

`ActualSemanticsAugmented.lean` preserves the **entire** preceding359 semantic scaffold
as a byte-identical prefix with SHA256
`b7f8b1456db538ba9b1ea6e4b2440b04c2edd8e26b5e16085192d24998215106`.
No retained inventory edit was required, so inverse recovery is simple truncation at the
recorded byte boundary. Appended independent FIRST/current checks verify exactly six
binders, retained names/order/BinderInfo/universes/conclusion, actual opaque `value! true`,
standard axes, nonself initial proof, and the actual positive→wrapper→min dependency chain.

All four entire immutable original/current proof blocks remain unchanged, verified in
`immutable-scaffold-and-blocks.json`:

| Entire block | SHA256 |
|---|---|
| Original Index proof block | 72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f |
| Original Theta proof block | 355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da |
| Whole original2b MainLemma | 96f1abe996f5a0bc024939263ab8e92f355ba531dd87357d8de28871b715024a |
| Whole independent current MainLemma | 859af5c80ed9022535c15ba6a5d36e206ae63345d6d91133b1d2bf3a8130fe41 |

This retains the all29 public old adapters, full old index_le_lem6 telescope, all existing
helper deletion/retention/FIRST checks, complete independent original and current
MainLemma proofs, actual RootTheta/MainLemma full types/values/standard axes/dependencies,
and accurate all50 current source declaration inventory. No stale34-tail substitute.

## Final ordinary and native gates

Fresh sequential commands, all actual invocations from this revisit:

| Gate | Exit/time | Complete evidence |
|---|---|---|
| `/Users/ramin/.elan/bin/lake build Roth.Theta` | 0 /22.805s | build-theta-final.log/json |
| `/Users/ramin/.elan/bin/lake build Roth.MainLemma` | 0 /29.976s | build-mainlemma-final.log/json |
| Exact FIRST context independent compiler | 0 /32.193s | FirstContextIndependent.lean; first-independent-final.log/json |
| Entire augmented semantic compiler | 0 /184.984s | ActualSemanticsAugmented.lean; actual-semantics-final.log/json |

`semantic-marker-summary-final.json` checks **366 PASS markers**, all359 preceding
semantic gates plus seven appended scoped gates, and the independent FIRST-context PASS.
It rejects PANIC, errors, sorryAx, nonstandard axes, source drift, or changed immutable
blocks. Every actual target/wrapper/min opaque proof value and full type checks; six
FIRST binders match exactly, no hypotheses removed; actual caller dependencies check.

Fresh native `lean_diagnostic_messages` requests supplied only the complete absolute
file path, no declaration/line/severity filtering. Complete unfiltered raw results:

| Module | success | partial | timed_out | Errors | Warnings |
|---|---|---|---|---:|---:|
| Theta | true | false | false |0|8|
| MainLemma | true | false | false |0|3|

`native-theta-final.json` and `native-mainlemma-final.json` preserve every warning,
including retained public hr/hB/hq and header issues. None is in the numerical target or
its wrapper/min. Failed dependency lists are empty. Native requests returned completely.
`pre-profile-drain.json` verifies all14 owned ordinary child processes and process groups
are gone, both full native requests returned, no pending requests, and exact source hashes.
No ordinary/native compiler runs concurrently with the real profile capture.

| Gate | Status | Evidence |
|---|---|---|
| lake_build_file and downstream | pass | Sequential actual Theta and MainLemma builds above, exit0 |
| definition_protected | pass | No def/abbrev changed |
| theorem_statement_protected | pass | Byte-identical signature, exact actual FIRST6 type/metadata comparison |
| structure_gate | pass |22≤30, six-line local arithmetic block, no branch/subproof>10 |
| naming_gate | pass | Descriptive snake-case `_aux`, no scheme number/forbidden abbreviation |
| line_packing_gate | pass | Both signature rows and arithmetic above |
| inequality_orientation_gate | pass | Complete four-occurrence signature scan above |
| local caller semantic compatibility | pass | Actual full wrapper/min type/value/axes/dependencies and all29 public recoveries |
| original/current MainLemma semantic compatibility | pass | Both complete independent proofs plus actual Root checks, immutable full scaffold |
| no limit/masking/scaffolding | pass | Static diff gate; exact default limits used |
| full `lake build` then separate `Roth.LeanEval` | owner pending | Reserved to owner after terminal leaf freeze; not run by this leaf |

## Fresh complete actual profiles and buzz result

After all ordinary and native requests drained, ran the actual live-module command:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean`

`actual-profile-final-first.log/json`: exit0, no timeout, 261.944s, full source SHA `e94ada9acfbd31f74bf65a04ea750e022c117d5e8d6e0ffb32ff6a8e56fb2ad5`.

`actual-profile-final-repeat.log/json`: exit0, no timeout, 259.666s, full source SHA `e94ada9acfbd31f74bf65a04ea750e022c117d5e8d6e0ffb32ff6a8e56fb2ad5`.

Each full raw capture matches all50 current source declarations, strict UTF-8 with zero
invalid or replacement sequences. Scope aggregates add only the selected outer command
and disjoint async proof/addDecl/compiler/linter rows. Nested macro, tactic and kernel
children are preserved but never added a second time. Exact raw byte boundaries, hashes
and every selected row live in the two `profile-final-*-strict-slices.json` files and
eight strict scope slices. Complete raw logs and full all50 tables are retained.

| Declaration | Inherited cfa baseline pair ms | Fresh first ms | Fresh repeat ms |
|---|---|---:|---:|
| mul_div_two_le_sum_max_aux | 621.519 /512.939 | 517.157 | 572.210 |
| mul_sq_div_three_le_sum_max_of_pos_aux | 903.926 /781.005 | 585.259 | 569.809 |
| mul_sq_div_three_le_sum_max_aux | 405.931 /322.748 | 400.861 | 381.226 |
| min_le_sum_max | 215.153 /186.701 | 176.910 | 182.737 |

Buzz outcome: **FIXED for the assigned positive helper**, all four scoped declarations
below1000ms in both completed captures. The first scoped target/direct consumers are
all below750ms, so a repeat was not required by the scoped threshold policy. The owner
clarified that unrelated queued failures alone do not trigger an extra capture. An
optional repeat was already launched; an early attempt to stop only its verified own
process group was denied by the sandbox (PermissionError), so the owner directed it to
finish under the original420s bound. `repeat-cancellation-attempt.json` records that no
cancellation occurred. Both completed observations are retained; **no third unchanged-
source sample**, no erased failure, no masking or raised limit. All production source
remained identical throughout both captures. No new helper was introduced.

## Remaining scope and limitations

The seven older declarations below remain the separate mandatory sequential performance
repair queue. These are not silently accepted by the assigned helper's timing PASS.

| Remaining older declaration | Fresh first ms | Fresh repeat ms |
|---|---:|---:|
| sum_max_sub_le_index_det | 1351.681 | 1698.334 |
| index_separated_mul_le_aux | 1127.761 | 1331.828 |
| index_det_le | 1179.250 | 1424.714 |
| index_numeric_bound_aux | 1046.137 | 1341.474 |
| index_le_lem6 | 1235.462 | 1644.559 |
| lem7_Φ_bound | 1116.601 | 1366.011 |
| lem7_numeric | 1154.574 | 1380.174 |

Both complete capture inventories were checked for newly failing already-audited helpers;
there are **no new queue additions** in this pair. Per-capture full rows and dispositions
are in `profile-final-first-remaining-queue.json` and `profile-final-repeat-remaining-queue.json`.

No whole-Theta performance PASS is claimed. MainLemma's actual caller timing remains
**unmeasured after its earlier bounded cutoff before main_lemma**, despite successful
ordinary semantic/build/native gates. No caller timing PASS is inferred from a build.
The owner alone performs final cumulative/allactual checks, full project build THEN
separate `Roth.LeanEval`, exact-path stage/commit/push/clean before the next revisit edit.

## Eleven-step checklist

- [✓] Step1: required skills, complete worker/references/buzz/profiling read.
- [✓] Step2: full24-item current audit and every local fact assessed.
- [✓] Step2.5: five actual searches; clean bounded exact?/apply? examples and positive absence gate.
- [✓] Step2.6: all6 effective parameters,8 compiled negative drop/weakening trials, independent boundary proofs/counterexamples, private literature/inversion decision.
- [✓] Step2.7: both measured signature lines and complete next-token arithmetic.
- [✓] Step2.8: all4 signature inequalities scanned, no reversal/name drift.
- [✓] Step3: all42 golf statuses and supported local repairs.
- [✓] Step4: alternate proof/retention/API/simplify assessment; no new extraction.
- [✓] Step5a: complete unfiltered native diagnostics for Theta and MainLemma,0 errors.
- [✓] Step5b: actual module/downstream builds, exact FIRST context and six-binder metadata, full366 semantic checks, all4 whole blocks, actual values/std axes/dependencies, real complete scope timing gates.
- [✓] Step6a: no renames needed; shared queue/logs untouched.

Result:22→22 body lines (line delta0), supported explicit arithmetic and targeted division
repair; no original/helper progress-count increase. Comments-preserved: none in assigned
body, all outside narratives byte-identical. Full project/Eval/publication remain owner
pending. Detailed evidence map and terminal authority release follow.

## Artifact map and terminal freeze

| Evidence | Concrete artifact |
|---|---|
| Exact source/pins | baseline-Theta.lean; final-Theta.lean; source-hashes.json; all-source-pin-hashes.json; owned-proof.diff; static-gates.json |
| Immutable FIRST | first-immutable-hashes.json; FirstIndependent.lean; FirstContextIndependent.lean; first-context-map.json; first-independent-final.log/json |
| Historical failure and inherited baseline | preserved-profile-pairs.json; historical-and-baseline-hotspots.json; four historical/baseline strict slices; immutable full paths/hashes in those maps |
| Current exploratory probes | Candidate*.lean and candidate*.log/json; PrefixAbsence.lean and prefix-absence.log/json; Automation.lean and automation.log/json/ranges; BindersNegative.lean and binders.log/json, binder-ranges/results.json; Boundary.lean and boundary.log/json |
| Deterministic proof cost | Heartbeats-before/after.lean; heartbeats-before-corrected/after.log/json; failed original syntax source/log/status preserved separately |
| Full mathematical semantics | ActualSemanticsAugmented.lean; actual-semantics-final.log/json; immutable-scaffold-and-blocks.json; semantic-marker-summary-final.json |
| Actual module gates | build-theta-final.log/json; build-mainlemma-final.log/json |
| Complete native diagnostics | native-theta-final.json; native-mainlemma-final.json |
| Full actual profile pair | actual-profile-final-first/repeat.log/json and -table.json; profile-final-first/repeat-strict-slices.json; all eight exact scope slice logs |
| Queue accounting | profile-final-first/repeat-remaining-queue.json |
| Drain and release | pre-profile-drain.json; pre-repeat-drain.json; final-process-drain.json; final-freeze.json; evidence-manifest.json |

Final Theta SHA256: `e94ada9acfbd31f74bf65a04ea750e022c117d5e8d6e0ffb32ff6a8e56fb2ad5`.

All16 other source/pin files match the supplied release hashes. The evidence manifest
records strict artifact SHA256 and byte lengths. Final drain proves no owned ordinary
process/group or native request pending. Terminal release: source, scratch and report
edit authority **REVOKED**, compiler/native authority **RELEASED**; no further own request
or edit will be made after the freeze. Owner gates/publication remain pending as stated.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 77.937 s and 35.334 s.
Theta SHA256 `e94ada9acfbd31f74bf65a04ea750e022c117d5e8d6e0ffb32ff6a8e56fb2ad5` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-p01-full.log` and `/private/tmp/roth-theta-p01-leaneval.log`; machine record
`/private/tmp/roth-theta-p01-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this validated revisit before the next source edit. This revisit belongs to the original 26 batch; original counts
remain Theta 35/35, overall 216/264, 9/14 files. No original-count increase comes from revisits or helper audits.

Owner evidence qualification: all12 anonymous clean-prefix trial headers were checked. Eleven diagnostics have source positions inside their trial spans. The bounded apply? attempt returns partial suggestions and a5000-heartbeat whnf timeout reported at line1, outside its span; that diagnostic is not claimed as span-verified. This limitation affects only solver-search evidence, not the successful FIRST/366 semantic/native/profile gates. Owner checked all121 artifact/source-map hashes,17 project/pin hashes,13 immutable FIRST/source/success hashes, exact only-body diff, full prior359-byte-prefix preservation/four block hashes, complete native responses, all50 actual profile anchors/disjoint totals/strict UTF8, historical failure slices/raw hashes and dead groups. Detailed checks: `/private/tmp/theta-positive-performance/owner-hash-checked.json` and `owner-checked.json`.
