# `Roth.abs_eval_lt_of_le_index` — completed parent audit

The necessary helper has completed fresh independent audit and owner local acceptance. It is frozen at SHA256 `8e17d0654af3467e8e015d5c7375be50fd8f74c0bf589a4c89c607b87d6056ac`; its independent evidence is reused, without helper reproof or VALUE reinference. The same original14 author resumed. Helper and parent remain a joint publication unit.

Production parent is now 28 declaration / 20 proof lines (original 51/43). Its one proof comment is preserved. Unused hQ/hr/hc are removed; κ and approximation premises are weak inequalities, with exactly the original quantitative conclusion. Only the authorized hupper invocation changed downstream; stronger caller facts and all other caller proof text remain untouched. The accepted helper is byte-identical. Candidate full-file native check exited 0 in 26.000s before final signature-only whitespace packing, with no diagnostics.

Final HAVE audit: hT has tactic-free proof but is used twice, so retained. hterm has proof content, so retained; no single-use tactic-free have remains. The former hw is inlined in the helper call, and hqR/hq1/hr'/anonymous sign facts are eliminated from the parent. Zero coefficient branch has two proof lines; nonzero branch has six. There is no conjunction conclusion. A final manual holistic pass found no duplicate polynomial work, gratuitous wrapper, new import, global instance, or automation attribute. No actual simplify-skill invocation is claimed because that skill is unavailable.

The earlier 24-item and 42-rule tables below are retained as dated work history. Final resolutions supersede their partial statuses: items 1/2/6/8/12/18 are implemented as described here; all other applicable checks remain unchanged. Rule 1.10 is now applied to hw; rule 2.14 uses absolute-sum transitivity plus sum_lt_sum_of_nonempty, without repeating the long Taylor expression; rule 2.15 is absent from the final parent because numerical normalization belongs to the frozen audited helper. Numerical field_simp/nlinarith are eliminated from the parent. Per-binder table below accounts for every old binder; the five verified premise changes are applied. No new binder exists. All final casts in changed target/caller lines bridge ℤ/ℕ→ℝ or fix real-power elaboration, and no same-type redundant cast was found. Ordinary lambdas in changed lines use ↦. No ≥/> inequality or limit/debug scaffolding is present. Docstring and source citation are preserved; no normal-form or syntactic restatement is needed.

Final packing table (codepoints; #check width-100 reference will be captured by the semantic inventory):

| Signature line | Chars | First next unit | Arithmetic | Action |
|---|---:|---|---|---|
| 376 | 95 | `(hd : ∀ j, degreeOf j Q ≤ r j)` (30) | 95+1+30=126 | ok |
| 377 | 95 | `{q : Fin m → ℕ}` (15) | 95+1+15=111 | ok |
| 378 | 60 | `(happ : ∀ j, |α - (h j : ℝ) / q j| ≤ 1 / (q j : ℝ) ^ κ)` (55) | 60+1+55=116 | ok |
| 379 | 59 | `(hqr : ∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j)` (48) | 59+1+48=108 | ok |
| 380 | 60 | `(hC : ∀ i : Fin m →₀ ℕ, |eval (fun _ ↦ α) (hasseDeriv i Q)| < C)` (64) | 60+1+64=125 | ok |
| 381 | 70 | `|eval (fun j ↦ (h j : ℝ) / q j) Q| <` (36) | 70+1+36=107 | ok |
| 382 | 69 | `(q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) := by` (38) | 69+1+38=108 | ok |
| 383 | 44 including := by | no next signature unit | n/a | ok |

Final source frozen in `final-source-freeze.json`; actual full/Eval builds, native/LSP, strict semantics/recovery/caller, and profile gates follow. This section does not assert those gates before their tool receipts exist.

---


## Validation protocol qualification

The final full build passed in 47.012s. The separate Eval build passed in 33.770s. A scratch independent compiler was mistakenly launched before the pending Eval poll had returned terminal status; their runs briefly overlapped. This is a compiler-serialization protocol FAIL. Attempted scratch cancellation returned PermissionError; no cancellation success is claimed. Both runs subsequently returned exit 0 with their groups absent. Independent command: `lake env lean -R /private/tmp/roth-main-taylor-bound -o /private/tmp/roth-main-taylor-bound/Independent.olean /private/tmp/roth-main-taylor-bound/Independent.lean`; it writes only scratch artifacts. Eval build output records only its Eval target, while its imported Main artifacts were already complete from the full build. Production source stayed frozen. Owner accepted reuse of these correctness results with this explicit qualification; no duplicate builds were run solely to relabel serialization, and no profiling time uses the overlap. Later compiler/native/LSP/profile work is serial.

Historical performance evidence is now narrowly owner-bound in `/private/tmp/roth-main-owner/taylor-old14-historical-acceptance-v1.json`: genuine declaration bytes appear in the old Main689 full-source capture (source SHA256 `6668ff83a7e7b156f6f29b8f2d0163e699da002b70338d5ee0715065ade9b25f`). One exact literal printer parenthesis pair around the complete `Finset.sum_lt_sum_of_nonempty ... hterm` term is individually bound; remaining normalized bytes match. All 11 disjoint roots and 8 actual generated-family kernel parents give 1823.341ms, a valid historical FAIL. Generated member universes vary and are not assumed empty. The prior mismatch row remains unchanged; only a supplemental acceptance receipt was added. This is one historical full-source diagnostic in a different context from the new scoped prefix: no speedup ratio or causal/noise claim, no new baseline capture.


## Completed semantic and build gates

Actual full build `final-full-build`: exit 0, 47.012s. Separate `final-Eval-build`: exit 0, 33.770s. Existing out-of-scope imported header/typeclass/Theta warnings are preserved in their unfiltered logs; changed Main's build has only its existing line-1 header warning, with hQ/hc warnings eliminated. Compiler overlap qualification above remains binding.

Before guards, `family-inventory` completed with production1 / independent1 / recovery1 / caller5 actual members and their actual universe lists (all eight empty here). Final `#check` at width 100 is saved in `final-check-width100.txt`, alongside the measured source signature table. `actual-name-observation` discovered six concrete scoped Name pairs: each comparison has one anonymous NeZero instance and two anonymous constant lambdas, at explicitly recorded distinct Expr paths. `finite-literal-TYPE-pairs.json` checks both actual Names have macro scopes, exact BinderInfo and erased Names agree, each literal replacement occurs once, and every remaining raw TYPE byte agrees. No generic alpha normalization or ExprBEq shortcut was used. The initial planned one-pair comparison generation stopped because full remaining bytes differed at two real lambda binders; its missing-file driver exited 1, and was replaced by this actual observation and finite six-pair proof. No production proof changed for this harness correction.

`type-comparison-final` exited 0 in 32.558s: full strict recursive current/independent TYPE and genuine-old/old-contract recovery TYPE hold modulo only those finite literal observed pairs, while affected caller genuine-old/current TYPE is exactly equal. `final-guards` exited 0 in 58.410s. All eight actual opaque theorem VALUES were inferred in memory, closed (no free/metavariables/loose bvars), admit-free, standard axioms only (`propext`, `Classical.choice`, `Quot.sound`), at actual defaults 200000/20000/512. Full raw VALUES were not dumped; row receipts contain actual runtime hash/byte length and full TYPE. No VALUE identity between independent proofs is claimed. Actual member TYPE/universes were rebound exactly to the prior inventory after guards. Fresh local dependency graph is acyclic; independent proof forbids target/generated/recovery/caller/later-Main references, using only upstream imports and the exact frozen accepted weighted helper. Caller may reuse exactly accepted earlier Main leaves. Accepted helper TYPE/universes were bound, without helper VALUE reinference or clone/reproof. Evidence: `final-actual-rows.json`, `final-dependencies.json`, `finite-literal-TYPE-pairs.json`, actual source/terminal receipts in scratch.

Changed target cast audit: 0 redundant same-type casts dropped, 14 displayed cross-type ℤ/ℕ→ℝ cast occurrences retained; positivity/type annotations fix real ordered-power elaboration. New identifiers used in final target are the independently accepted helper, plus original finite-sum/absolute-value/order APIs already verified through source, search and current compilation. No invented identifier remains.


## Final native, diagnostics, and performance

Fresh native Main/Eval/root checks completed serially, exits 0 in 30.353s / 28.037s / 24.255s, with complete unfiltered stdout/stderr empty. Complete unfiltered LSP Main/Eval/root each returned success, partial=false, timed_out=false, no failed dependencies and no errors. Main retains its existing line-1 header warning; Eval/root are clean. Target hQ/hc warnings are resolved, with no new warning. All query/native drivers were drained before profile HOLD.

Final profile HOLD ACK preceded every preparation step. Capture used exact production imports/preceding commands/frozen helper/target and namespace close, plus actual-family/TYPE/VALUE/default/scope-path observations. Before/after actual defaults were 200000/20000/512; full parent and Lake environment bytes were compared only in memory, persisting hash/length and approved PATH/LEAN/toolchain fields. Every frozen input/map/source remained identical. Five actual child groups and the capture driver were absent, and the tool returned 0 before the RAW UNPARSED notice. Explicit owner RELEASE preceded all trace parsing. Initial parser script had a leading-semicolon SyntaxError fixed before raw parsing; no new Lean capture was made.

Final target profile is **471.203ms**, PASS <1000 and <750, so no repeat. Full canonical docstring/signature/proof payload matches directly under accepted whitespace/standalone-proof-comment handling; no final parenthesis exception was needed. All four disjoint roots are included: outer command 63.074ms, proof 376.080ms, kernel parent 13.998ms, lint 18.051ms. The one actual fresh target family member has its sole kernel occurrence bound; compiler and lazy prior DATA roots are empty. Nested kernel 13.959ms is not double-counted. The regular capture observed and inferred the actual opaque target VALUE in memory, with closure/default/standard-axiom guards and full TYPE. Actual family/universes were emitted before row guards, without assuming suffix counts or universes. Three actual current/profile scoped-binder pairs were emitted in that same regular capture, with full remaining raw TYPE bytes equal; final recursive TYPE-only supplementation exited 0 in 41.892s, at actual defaults, comparing every remaining Expr component and the three exact actual scoped-binder path/Name pairs. No VALUE reinference was needed. No actual VALUE identity claim is made. Evidence: `final-profile/{target-profile-acceptance,selected-profile-pairs,actual-observed-family,actual-scoped-name-pairs,profile-type-raw-binding}.json`.

The old 1823.341ms historical full-source diagnostic and new 471.203ms prefix observation are separate contexts. No ratio or causal/noise dismissal is claimed. The accepted helper's own performance audit remains independently frozen and is not repeated for this parent.

Gate results: definition protection PASS (no DATA definitions edited); theorem protection PASS via explicitly authorized verified premise weakenings with genuine-old recovery; structure PASS 20-line parent body and two-/six-line branches; naming PASS; source packing table all ok and width-100 #check captured; inequality orientation PASS; no new imports/axioms/admissions/limit raises/debug scaffolding; exact scope PASS (only parent declaration and authorized two-line hupper invocation changed after helper acceptance). No renames or additional refactors queued. The separate compiler-overlap protocol FAIL above remains explicitly qualified and is not relabeled a serialization pass.

Result: original target 51→28 declaration lines, 43→20 proof lines, 23 target lines saved. Necessary independent helper contributes 25 declaration lines plus its accepted comment/separators; Main worker-entry 565→569 lines, net +4. Existing target proof comment preserved 1/1; no source/docstring/import/accepted-helper drift. Full 24-item / 42-rule audit and per-binder table are completed, with final resolutions at the top; manual holistic pass substitutes only for the unavailable simplify tool, without claiming invocation. Final TYPE-only supplement is terminal exit 0; actual final drain and release of every lease are recorded in FINAL.json.


## Final phase checklist

| Required phase/artifact | Result |
|---|---|
| Genuine/entry saved before Lean/golf | PASS; exact genuine target bytes preserved |
| Installed workflows/references | PASS; full scoped reading |
| 24-item audit / all 42 rule slots | PASS; tables plus final resolutions |
| Five-method search / compiled direct closing probes | PASS; failures qualified, existing APIs reused |
| Every binder / supported weakening tests / old-contract recovery | PASS |
| Every signature-line packing / width-100 printer / inequality scan | PASS |
| Every have / branch structure / comments / docs / casts / identifiers | PASS |
| Necessary helper fresh audit / same-author resume / helper frozen | PASS; joint publication only |
| Actual full and separate Eval builds | PASS for correctness; brief compiler-overlap protocol FAIL explicitly retained |
| Current actual family/universe enumeration before per-row guards | PASS; 8 observed rows |
| Strict old/recovery/current/independent/caller/profile TYPE and opaque VALUES | PASS; literal hygienic exceptions fully bound; no raw TYPE/VALUE identity overclaim |
| Native Main/Eval/root / complete fresh Main/Eval/root LSP | PASS; serialized and drained; one existing Main header warning |
| Holistic simplify review | Manual scoped PASS; actual Skill(simplify) unavailable and not claimed |
| Buzz / exact canonical / complete disjoint root bound / repeat rule | PASS; 471.203ms, no repeat needed |
| Final scope/production/helper freeze | PASS |
| Git/shared progress/rename changes | None; owner publication |
| END / final process drain / all leases released | FINAL.json actual receipt |

Historical partial-stage audit follows:

# `Roth.abs_eval_lt_of_le_index` — partial END for necessary helper audit

This is an unfinished declaration audit, not a cleanup acceptance. The same target author must resume after a fresh independent audit of `Roth.abs_prod_pow_le_rpow_weight_aux`; helper and parent must be published jointly. No Git/shared progress/rename writes were made.

## Entry and baseline

Genuine original and entry were saved before any Lean/golf in `/private/tmp/roth-main-taylor-bound/{genuine,entry}-{Main,target}.lean`; `entry-save.json` binds exact bytes. Genuine and entry target bytes agree: SHA256 `16314634a1af0a08df28cbd129ad4e7e09d2ea702c1fb833a7de6e2dea20b14a`, 51 declaration / 43 proof lines. Full entry Main SHA256 `f514a82586b0df1ad6d45d65471512f2524755d7be931291ff4c5b4482e6d02c`.

Baseline full/Eval builds, complete native diagnostics, and upstream audit evidence are reused from owner-accepted original13 on these exact entry bytes. No redundant baseline build was run. Those results do not certify the newly inserted, deliberately untested helper.

Installed lean4 and mathlib-quality skills, full cleanup/cleanup-all workflows, full golfing-rules/proof-patterns/mathlib-search/generalisation-patterns/cleanup-gates, relevant style/naming, full mathlib-review-stages/profiling and buzz were read. `Skill(simplify)` is unavailable; actual invocation is not claimed. A fresh whole-file review remains scheduled by the owner.

## Mathematical structure and bounded trials

The proof expands evaluation in the degree box, discards vanishing Taylor coefficients, bounds the product of approximation errors by a real power using its weight, and sums strict coefficient bounds. Strictness comes from the Hasse derivative coefficient bound; strict approximation quality, positive index bound, and polynomial nonvanishing are unnecessary here.

DirectA/B/C tried direct order multiplication with simp-based exponent normalization; the normalization did not close the actual goal. DirectD instead used `mul_le_mul_of_nonpos_left` and `ring`, and normalized the product's exponent without positive-degree denominator cancellation. It compiled with exit 0 in 11.611s and reported only newly unused `hr`. DirectE then removed `hr` and weakened approximation `<` to `≤`; exit 0 in 30.309s with no diagnostics. All bounded candidates are scratch exact prefixes; none replaced the production target. DirectE is still 52 declaration / 44 proof lines, so these direct comparison improvements do not discharge the structure requirement.

Whole-target LSP probes: `grind` failed; `aesop` exhausted search and did not close the target; `exact?` found no closing term; `apply?` exhausted its search budget and offered generic comparison reformulations, not a solution. No suggested limit increase was applied. Raw response: `target-automation.json` in scratch. The tool replaces a tactic while retaining following tactics, so downstream unknown-`hqR` errors in the aesop probe are probe-context fallout, not production diagnostics. DirectA's tool session identifier was not retained; its eventual diagnostic file records the failed normalization, and no success/exit claim is assigned to that run. DirectB/C have explicit exit-1 receipts; DirectD/E have explicit exit-0 receipts.

## Necessary helper handoff

The independent mathematical fact is a weighted monomial product bound: if `|x j| ≤ q j ^ (-κ)` and `q j ≥ q 0 ^ (r 0 / r j)`, then a monomial whose weight is at least `c` has absolute value at most `q 0 ^ (-r 0 * c * κ)`. This separates a numerical estimate from all polynomial/index/degree/derivative data. It involves power monotonicity in base and exponent, finite products, exponent summation, and weight algebra, rather than a wrapper around 1–3 library calls.

First ungolfed statement and proof were physically saved as `/private/tmp/roth-main-taylor-bound/helper-first-ungolfed.lean` BEFORE any helper Lean or helper golf. SHA256 `afe5ba31991b4eb3dd35152ce640fdb46d45116d4e11af5f5a274ed2f31985c7`, 1677 bytes / 29 declaration lines; save receipt `helper-first-ungolfed-save.json`. That exact saved helper was inserted above the target. The author has not compiled, audited, or golfed the helper. Production parent and caller are byte-unchanged. `partial-source-freeze.json` verifies that the insertion is the only Main source change.

Owner granted narrow conditional edits to the sole actual caller, the `hupper` invocation inside `roth_of_isIntegral`, for the verified target premise changes. Those caller edits remain for same-author resume; all stronger caller facts remain untouched. No Eval invocation exists by repository search. No helper-only publication is permitted.

## Initial 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | Lint | Entry native warnings hQ/hc; DirectD additionally hr; DirectE clean. Final production diagnostics pending. |
| 2 | Have | hqR reused; hq1 used once but proved by tactics; hT reused; hterm reused as bound; h0 case split; hw single-use non-tactic proof should inline after extraction; hr' disappears with ring; anonymous nonnegative product replaced by direct order API. |
| 3 | Options | No scoped limit/debug options. |
| 4 | Simp | Existing nonterminal simp_rw is explicit. No bare nonterminal simp or terminal simp-only. |
| 5 | Naming | `abs_eval_lt_of_le_index` describes its bound and hypothesis; no forbidden abbreviation/pattern. No rename queued. |
| 6 | Packing | Initial measurement below; final packing/width-100 printer reference pending parent resume. |
| 7 | By | All existing `by` tokens end preceding lines. |
| 8 | Format | Replace target ordinary lambda `=>` by `↦`; maintain one tactic/line and 100 codepoints. |
| 9 | Comments | Preserve the one Taylor-term signpost comment exactly/re-anchor it. Still present untouched. |
| 10 | Docs | Existing quantitative explanation and source quotation preserved. Parent remains public and is cited in module proof outline. |
| 11 | Visibility | Exported evaluation-bound API, referenced by module documentation and main theorem. Necessary local numerical helper is private. |
| 12 | Structure | 43-line original body and long nonzero branch require necessary numerical helper; direct candidate remains 44 lines. Fresh helper audit required before completion. |
| 13 | Mathlib | Five-method search below; use existing product/rpow/Taylor/index APIs. |
| 14 | Junk def | n/a: theorem, no definition introduced. |
| 15 | Exists | n/a: no existential witness lemma. |
| 16 | Show | n/a: no show/change in target. |
| 17 | Push neg | n/a: none. |
| 18 | Generalise | Per-binder audit below; only bounded evidence-based premise changes proposed. |
| 19 | Inequality | Zero reversed inequalities; scan below. |
| 20 | Normal form | Existing eval/hasseDeriv/index/weight vocabulary and ordered bound are canonical project APIs; no equivalence forest. |
| 21 | Syntax | Removing unused/stronger premises simplifies the actual invocation; quantitative conclusion unchanged. |
| 22 | Imports | n/a: no added imports. |
| 23 | Casts | Natural/integer-to-real casts are cross-type/load-bearing for real powers and rational evaluation; no redundant same-type cast identified. Recheck final diff. |
| 24 | Instances | n/a: no instance declaration; NeZero m selects the distinguished Fin index 0. |

## Five-method search and literature

| Method | Query | Result |
|---|---|---|
| Lean-Finder | multivariate polynomial evaluation, Hasse derivative bounds, Taylor expansion, weighted index | Chevalley polynomial complexity results, not the evaluation estimate. |
| Loogle | `Real.rpow, _ ≤ _, _ ≤ _` | No result. |
| LeanSearch | finite product of real powers, sum of exponents, nonpositive exponent monotonicity | `Real.rpow_mul`, `Real.rpow_sum_of_pos`, `Finset.prod_pow_eq_pow_sum`. |
| Source | eval_eq_sum_box; weight/product; abs_eval/index; rpow monotonicity/product/sum | Project Taylor expansion and index-to-weight, plus mathlib `Real.rpow_le_rpow_of_nonpos`, `Real.rpow_le_rpow_of_exponent_le`, `Finset.prod_le_prod₀`, absolute finite sums. |
| Name | rpow_le_rpow (15 returned names) | Existing base/exponent monotonicity APIs. Index reported unavailable, so no absence conclusion is inferred from empty indexed searches. |

Auxiliary forms considered: rpow of sum/product, nonpositive exponent base reversal, exponent monotonicity, evaluated Taylor expansion, index-to-weight specialization. No common-equivalents disguise matches. The compiled whole-target `exact?` probe found no direct closing term; the helper still requires its own independent exhaustive audit, including any helper-specific generic absence probe. No blanket mathematical absence claim is made.

Web literature queries: “Roth theorem index Taylor expansion polynomial derivative bound approximations weighted product” and exact paper authors/title. First top results were Roth's theorem, Taylor's theorem, and an arithmetic geometry text repost; the exact title search gave no relevant result. No hypothesis change is justified by these secondary hits. Primary project source `.mathlib-quality/references/clean.tex` lines 1656–1670 gives the Taylor/weight argument. Its strict monomial estimate uses positive weight, while the current theorem already gets strictness from its stronger strict coefficient bound. This supports the bounded formal premise tests, without changing the target's quantitative conclusion. Math ChatGPT MCP is unavailable in this session. No optional ambient generalization is proposed.

## Per-binder generalisation audit

| Binder | Class/use | Candidate/result |
|---|---|---|
| m : ℕ | index size, count | Retain; Fin m and degree-box cardinality determine conclusion. |
| NeZero m | typeclass, Fin index 0 | Retain; removing leaves distinguished index ill-typed. |
| Q | polynomial value | Retain; evaluation and derivative data. |
| hQ | proposition, unused | Removed in DirectD/E, compiled; apply on resume. |
| r | degree/weight value | Retain; both bound and box depend on it. |
| hr | positivity proposition | Direct ring normalization makes it unused; removed in DirectE, compiled; owner approved. |
| hd | degree bound | Retain; consumed by eval_eq_sum_box, already weak ≤. |
| α | real expansion point | Retain; derivative and approximation hypotheses depend on it. |
| c | exponent/index bound | Retain; same quantitative conclusion. |
| hc | positivity proposition, unused | Removed in DirectD/E, compiled; apply on resume. |
| hidx | index bound proposition | Retain; only use yields c ≤ weight, already weak. |
| h | integer numerators | Retain; actual evaluation argument; no ambient domain restatement. |
| q | natural denominators | Retain; positivity supplies ≥1 base automatically. |
| hq | positive denominator proposition | Retain; rpow positivity and base ≥1. Weak 0≤q allows zero denominator/base and is not supported by these APIs. |
| κ | exponent value | Retain; present in approximation and conclusion. |
| hκ | sign proposition | 0<κ → 0≤κ compiled DirectD/E; exponent reversal only requires nonnegativity. |
| happ | approximation proposition | < → ≤ compiled DirectE; strictness supplied by hC. |
| hqr | denominator comparison | Retain; rpow base monotonicity; already weak ≤. |
| C | bound value | Retain; quantitative coefficient bound. |
| hC | strict coefficient bound | Retain; provides strictness and C>0 even for zero coefficients; ≤ would fail e.g. Q=0,C=0. |

No abstract type or universe parameter exists to weaken. No bundled continuity/injectivity/decidability hypothesis exists. Inversion diagnostic: after the Taylor rewrite, Q still appears in coefficient data and index-to-weight use; the numerical monomial subargument is independent and is precisely the necessary helper, not an optional ambient companion.

## Golfing rule coverage (partial boundary)

| Rule | Status |
|---|---|
| 1.1 | n/a: no by-exact wrapper to remove (exact_mod_cast contains proof work). |
| 1.2 | n/a: no by-rfl. |
| 1.3 | n/a: rw changes product/exponent goals before nontrivial proofs. |
| 1.4 | n/a: no simp followed by exact pair. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no conjunction constructor. |
| 1.7 | DirectD order step uses composed mul_le_mul_of_nonpos_left; rpow monotonicity still needs exponent normalization. |
| 1.8 | n/a: no contradiction/negation pair. |
| 1.9 | n/a: lambdas select coordinates/coefficients, no plain eta wrapper. |
| 1.10 | hw identified for inlining into helper call on resume; no blanket inference changes. |
| 1.11 | n/a: no apply-intro pair. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projection-only have. |
| 1.14 | n/a: intervening operations separate rewrites. |
| 1.15 | n/a: no terminal simp-only. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | Existing trans chain used; retain direct theorem namespaces for numerical APIs. |
| 1.18 | n/a: no removable outer parenthesis pair improves these calls. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: not existential. |
| 2.1 | Whole-target grind tried, failed. |
| 2.2 | n/a: no retained grind. |
| 2.3 | Simp-only exponent normalization tried, failed; ring normalization compiled. |
| 2.4 | n/a: no function regularity goal. |
| 2.5 | Existing positivity for products; explicit sign multiplication compiled in DirectD/E. |
| 2.6 | Direct monotonicity API used for exponent comparison rather than context-wide nonlinear automation. |
| 2.7 | n/a: no substantive Nat/Int linear arithmetic goal; casts only. |
| 2.8 | Whole-target aesop tried, failed. |
| 2.9 | exact_mod_cast retained at cross-type positive/nonnegative bounds. |
| 2.10 | n/a: analytic variables prevent finite decision computation. |
| 2.11 | Product exponent identity normalizes with ring; field_simp removed in candidate. |
| 2.12 | n/a: exponent identities are ring normalization, not polynomial consequences of equalities. |
| 2.13 | n/a: zero/nonzero coefficient branches are intrinsically different. |
| 2.14 | Direct comparison consolidated pointwise product bounds, but whole proof still >30. |
| 2.15 | DirectD/E congruent order-normalization goals closed with <;> ring. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases-rfl. |
| 3.5 | n/a: no new global automation attributes justified by this specialized analytic bound. |
| 3.6 | n/a: no simp_all-only. |
| 3.7 | n/a: no heartbeat raise. |

## Inequality scan

| Occurrence | Location | Result |
|---|---|---|
| none | entire original signature/hypotheses | No ≥ or > inequality; all inequalities use ≤/<. Lambda => is not an inequality. |

## Gates and remaining work

All final gates are explicitly PENDING. The inserted helper has not been validated by its author. After fresh helper acceptance, the same author must apply the verified target premise changes and narrow caller repairs, reduce the parent using the helper, finish signature packing and holistic review, then run actual full build and separate Roth.LeanEval build, fresh native/complete diagnostics, actual family/universe inventory before strict semantic row checks, exact old-contract recovery and affected-caller TYPE/opaque-VALUE checks, and scoped profile under owner HOLD/ACK → raw unparsed drain → explicit release protocol. No historical target profile is accepted as a baseline. No final semantics/profile acceptance or speedup claim exists yet.

Phase checklist: entry save/reference reading/search/generalisation/bounded direct work complete; helper first-save complete; independent helper audit, parent completion, final diagnostics/diff gates, semantics, packing, manual simplify review, buzz, final report pending. This is the mandated necessary-helper partial END, not a silent structure deferral.

## Entry signature packing measurement (final repack pending)

| Entry line | Codepoints | First next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 349 | 92 | `{r : Fin m → ℕ}` (15) | 92+1+15=108 | break justified |
| 350 | 99 | `(hidx : c ≤ index Q (fun _ => α) r)` (35) | 99+1+35=135 | break justified |
| 351 | 91 | `{κ : ℝ}` (7) | 91+1+7=99 | repack |
| 352 | 80 | `(hqr : ∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j)` (48) | 80+1+48=129 | break justified |
| 353 | 60 | `(hC : ∀ i : Fin m →₀ ℕ, |eval (fun _ => α) (hasseDeriv i Q)| < C)` (65) | 60+1+65=126 | break justified |
| 354 | 71 | `|eval (fun j => (h j : ℝ) / q j) Q| <` (37) | 71+1+37=109 | break justified |
| 355 | 41 | `(∏ j, ((r j : ℝ) + 1)) * C * (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ)` (61) | 41+1+61=103 | break justified |
| 356 | 68 | `:= by` (5) | 68+1+5=74 | repack |

Original production signature retained at partial END. Width-100 current printer reference and a new all-ok post-repack table are required on parent resume; this table does not claim a packing pass.
