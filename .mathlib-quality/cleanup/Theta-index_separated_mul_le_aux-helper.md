# Dedicated fresh helper audit — `index_separated_mul_le_aux`

This audit covers only the private separated-product estimate in `Roth/Theta.lean`, lines 405–437. It counts **0 original declarations** toward the owner's original-declaration total. No Git operation, rename queue, shared ledger, public signature change, new production helper, or unrelated source edit was made.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md in full, both SKILL.md files, the full cleanup workflow, and relevant style, naming and profiling references. The parent supplied the standing instruction to implement recommended changes, superseding old approval wording. The public wrapper/domain and prior public-hypothesis preferences remain untouched.

## Baseline, mathematics, and result

Inherited baseline source SHA256: `90d8ca91b9a74bcc44ee2ca84fb599a4160957417bf78f529d918fe02ec2d5de`, 943 lines. Same-source complete unfiltered native LSP `/private/tmp/roth-theta-coeff-helper/final-lsp.json`: success true, partial false, timed_out false, no failed dependencies, 0 errors, 11 warnings. The parent's same-source module/actual compatibility gates passed. These are explicitly **inherited** baseline evidence, not fresh executions by this leaf. The inherited accepted uncontended real global prefix trace in that directory measured this helper at **610.207ms** and public `index_det_le` at **668.264ms**. No baseline LSP/profile duplication was needed.

Independent immutable first introduction: `/private/tmp/roth-theta-index-det/index_separated_mul_le_aux-FIRST.lean`, SHA256 `82ea1dcd2a8ced63947dc92f7a43f06b3cf868156e85895cd843a16873a03c92`, 26 proof lines. The full first-introduction snapshot and manifest remain preserved at the parent's paths. This leaf independently compiles the exact first text under a separate namespace; it never substitutes a call to the current helper for that proof.

Mathematics: convert the univariate integer factor V into a Unit-indexed multivariate polynomial. Its nonzero, degree and coefficient bounds give RSet membership. Injective variable renamings and coefficient maps preserve the two factors' nonzeroness; product index is the sum of their indices. Each is bounded by its defining Θ at weights l·r. The index scaling identity divides these bounds by l; positive l lets us clear that denominator. Adding the two inequalities gives l·Φ.

Recommended and implemented: remove only the redundant inner `(V.coeff b : ℤ)` ascription in the private hVc hypothesis, retaining its genuine integer-to-real cast as `(V.coeff b : ℝ)`. This does not change the elaborated type. The proof remains 26 lines. Its measured terminal `simpa only` exception is preserved. No further helper or API change is recommended.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | No inherited warning in lines 405–437. Final complete unfiltered diagnostics below; unrelated public retained-hypothesis warnings are reported, never suppressed. |
| 2 | HAVE SCAN | All six haves inventoried below; none is an untyped single-use alias. |
| 3 | SET_OPTION | None in production target. Scratch search uses a smaller 10000-heartbeat local budget; no production/profile limit is raised. |
| 4 | SIMP SQUEEZE | Only terminal simpa is squeezed. This is an existing measured performance exception, not gratuitous squeeze: generic terminal 291.457ms / helper 970.052ms versus selected terminal 109.546ms / helper 733.357ms in the original comparison; current baseline helper 610.207ms. Preserve its selected list. Other conversions use rw/rwa. |
| 5 | NAMING | `index_separated_mul_le_aux` describes index, separated product and comparison; snake_case/private `_aux`, no forbidden abbreviation, scheme digits, `_ge_` or `_gt_`. No rename. |
| 6 | LINE PACKING | Complete codepoint arithmetic table below, including every conclusion continuation. Complete next binder/application groups are used; no split MvPolynomial type or dangling identifier introduced. |
| 7 | BY PLACEMENT | All `:= by` occur at the preceding statement line's end. |
| 8 | FORMAT | Two-space proof indentation, four-space signature continuation, no blank proof lines, no semicolon chain, no haveI/letI, Unicode mathematical lambdas. |
| 9 | COMMENTS | No helper proof comments existed; none removed. All three public Step comments remain unchanged. |
| 10 | DOCSTRING | Private helper has none, as required. No public docstring edited. |
| 11 | VISIBILITY | Private helper is used by one same-file public proof; remains private. Classic import dialect. |
| 12 | STRUCTURE | 26 proof lines ≤30; hVmem block has short ≤2-line branches, no >10-line branch. No conjunction conclusion or existential output requiring splitting. No third helper needed. |
| 13 | MATHLIB | Five actual methods and clean compiled generic-route trials below; generic power-series order results are partial matches, not this rational-point Θ bound. Existing rename/equivalence/index APIs are used directly. This 26-line argument is substantive, not a 1–3-call wrapper. |
| 14 | JUNK DEF | n/a: lemma, no def or abbrev added. |
| 15 | EXISTS LEMMA | n/a: inequality, not a trivial witness lemma. |
| 16 | SHOW/CHANGE | Neither occurs in helper. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All 16 effective binders compiled through drop tests. Strict→weak and Fintype→Finite failures, successful equivalent and support-local forms documented below. No semantic impossibility inferred from a failed unchanged proof. |
| 19 | INEQUALITY | Every signature comparison has smaller side left; full scan table below. |
| 20 | NORMAL-FORM | RSet membership, natural degree bounds and real index ≤ lΦ already match surrounding APIs. Φ is a named sum, expanded only at the final normalization. |
| 21 | SYNTAX-GEN | Existing hU membership and hV degree/coefficient hypotheses match the sole actual caller. Rebundling V as Unit-RSet would force caller conversion; not easier to apply. |
| 22 | IMPORT-FANOUT | n/a: no import added or changed. |
| 23 | CASTS | Removed 1 redundant ℤ→ℤ ascription in hVc. Remaining integer→real and natural→real casts are genuine; MvPolynomial Unit/Option τ and ℤ target ascriptions select the correct equivalences/maps. No proof-body cast added. |
| 24 | INSTANCE-NAME | No instance declarations or explicit synthetic binder names introduced. Original omitted DecidableEq remains omitted; Fintype is anonymous and its full effective type is checked. |

### Every have

| Name | Proof/content and use count | Decision |
|---|---|---|
| hV′0 | Typed `by rwa` converts V≠0 through uniqueAlgEquiv; used in hVmem and mapped-factor nonzeroness | keep |
| hVmem | Typed `by refine` carries actual nonzero/degree/coefficient conversion; used once | keep proof content |
| hinjV | Typed term proof by Subsingleton.elim; used in rename nonzero and index_rename | keep, 2 uses |
| hUΘ | Applied Θ bound; rewritten by index_mul_left_weights and used terminally | keep, 2 uses |
| hVΘ | Applied Θ bound; rewritten by index_mul_left_weights and used terminally | keep, 2 uses |
| hlR | Typed `by exact_mod_cast hl`; used in both div_le_iff₀ applications | keep, 2 uses |

V′ is a `set` abbreviation with a defining equation, not a single-use have. Its equation is used in all three V conversions. The successful targeted positivity trial also proves hlR, but saves no line or mathematical step; the explicit cast proof remains clearer for this exact bridge.

## Five actual search methods and generic-route trials

All raw native responses are saved in `/private/tmp/roth-theta-separated-helper/search-results.json`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | weighted index of product in disjoint variables, coefficient bounds, sum of maximal indices | weighted-homogeneous product and MvPowerSeries.le_weightedOrder_prod; partial generic ingredients, no Θ bound |
| B Loogle | `MvPolynomial.rename, _ * _` | generic generators/presentation/rename identities; no matching estimate |
| C LeanSearch | weighted order of vanishing index of a product equals sum of indices | MvPowerSeries.weightedOrder_mul/prod, analyticOrderNatAt_mul; not the finite rational weighted-index/supremum statement |
| D source rg | full helper name, weightedOrder_mul, aeval_X_eq_rename, coeff/degree uniqueAlgEquiv, rename_injective | direct existing equivalence and map/rename APIs; untruncated raw grep log preserved |
| E native local-name | index_mul | Roth.index_mul/index_mul_left_weights plus unrelated subgroup results. Index status unavailable: source-backed hits, not generated-name absence proof. |

Auxiliary variants checked: product/order_mul/prod, rename/injective/rename_eq_zero, uniqueAlgEquiv symm coefficient and degree conversion, map_ne_zero_iff, index_rename and index_mul_left_weights. Common-equivalents table: no compact/discrete/bornology/coset pattern applies. Existing direct APIs remain the correct partial match; no direct mathlib replacement found within these bounded searches, and unavailable symbol-index evidence is not claimed as exhaustive absence.

Clean ordinary-compiler automation uses the **exact production prefix ending before the assigned private helper**, closes `end Lemma6` then `end Roth`, and adds anonymous examples only. It imports no current Theta or circular public `index_det_le`. Whole-goal grind failed, aesop and simp_all left unsolved goals, exact? could not close, and apply? suggested generic inequality rearrangements but hit the deliberately smaller search budget during delaboration without producing a proof. These expected failures are isolated from successful axiom gates. No self-reference or named failed theorem can be suggested. Native multi_attempt was not repeated: the parent's documented consecutive unbounded stalls justify the bounded compiler fallback. `automation.lean`/`.log` retain the actual trials, including partial suggestions.

## Every effective binder and mechanical generalisation

`binder-negative.lean` uses autoImplicit false; all 16 deletions produce errors in their own mapped source interval. `binder-map.json` and `binder-results.json` contain exact declaration ranges and errors. Removing a data binder necessarily leaves its dependent statement ill-scoped; these are signature-formation tests, not claims of mathematical necessity.

| Binder | Class / use | Compiled candidates and result | Decision |
|---|---|---|---|
| τ : Type* | universe-polymorphic variable type | drop fails unknown τ; already Type* | retain |
| [Fintype τ] | finite variable context used in Θ/index/RSet | drop fails synthesis; [Finite τ] fails synthesis at type/API formation | retain existing explicit finite structure; no local-instance scaffold |
| r | natural weight/degree function | drop fails unknown r; changing codomain would change domain-specific index/RSet APIs | retain |
| hr0 | all positive weights for index_mul and Θ bounds | drop fails unknown hr0; replacing all < by ≤ fails Nat.mul_pos/index_mul application; ∀j,rj≠0 equivalent compiles after Nat.pos_of_ne_zero | retain positive formulation |
| q | natural denominators in points and Φ | drop fails unknown q; no stronger class assumption exists to weaken | retain |
| h | integer numerators in points | drop fails unknown h; changing ℤ would restate indexSet/RSet domain | retain |
| hh | coprimality of every rational coordinate | drop fails unknown hh; some/none restrictions cover all Option τ, so no proper point-localisation for unrestricted U,V | retain |
| M | real coefficient bound and Θ input | drop fails unknown M; no positivity hypothesis to weaken | retain arbitrary real M |
| l | natural scale/degree bound | drop fails unknown l; replacing ℕ changes polynomial degree/weight APIs | retain |
| hl | positive l for division clearing | drop fails unknown hl; 0≤l fails Nat.mul_pos; l≠0 equivalent compiles via Nat.pos_of_ne_zero | retain canonical positive form |
| U | arbitrary multivariate integer factor | drop fails unknown U; already arbitrary | retain |
| hU | RSet nonzero, degrees, coefficients | drop fails unknown hU; retaining only nonzero, only degrees, or only coefficients each fails genuine projection/Θ membership requirements | retain bundled membership matching caller |
| V | arbitrary univariate integer factor | drop fails unknown V; already arbitrary | retain |
| hV | nonzero factor for product index and RSet | drop fails nonzero conversion; `0≤V` is not a valid ordered-polynomial relaxation, and all-zero extensions would change proof stage | retain intentional product-stage scope |
| hVd | degree upper bound | drop fails unknown hVd; an arbitrary looser bound would not establish required RSet membership; degree versus natDegree would be equivalent here | retain |
| hVc | global coefficient bound | drop fails unknown hVc; restriction to b∈V.support compiles after deriving M≥0 and extending zeros | equivalent under hV, adds conversion/caller obligations; do not restate |

The successful `alternative.lean` probes both natural nonzero equivalents with the full independent proof, exit 0. `support-bound.lean` independently compiles the support-local form, exit 0: nonzero V gives a supported coefficient, its bound implies M≥0, and zero coefficients then satisfy the full bound. Thus this apparent weakening is equivalent under hV. It adds a witness, a case split, and reconstruction for this helper's sole already-global-bound caller. No signature churn recommended.

Positive weights/l and nonzero factors explicitly describe the private positive product stage used by the public caller. Failure of unchanged-proof zero-weight/zero-factor trials is **not** a counterexample to possible extensions. Such extensions would require zero-case wrappers and additional audits without benefiting the one existing positive caller; no all-zero-cycle helper was introduced. Bounds and coprimality remain unbundled/bundled where the current caller supplies them directly.

DecidableEq τ is not an effective helper binder: the immutable first introduction already used omit. Independent first/selected full telescopes have exactly 16 effective parameters and no DecidableEq. No hidden section instance was silently dropped.

Literature: **n/a: private declaration, public-literature requirement exempt by explicit cleanup scope**. The public caller's statement is unchanged. Inversion check performed: determinant/R/D are absent already, because this is precisely the arbitrary-separated-product abstraction extracted from that proof. V is converted through the standard uniqueAlgEquiv, and Θ/lem6Φ remain the actual supremum content. A more abstract pair of renamed MvPolynomials would merely relocate the existing index_mul/index_rename calls and force the sole univariate caller to build the equivalence/RSet data. No further independent mathematical abstraction or public promotion is justified.

## Measured signature packing and inequalities

Complete original/selected full `#check` and telescopes are printed in `independent-helper-final.log`. Widths below count Unicode codepoints. The conclusion's dependent application is kept as complete application/binder groups, rather than breaking after `index` or inside its type annotation.

| Signature line | Codepoints | Next binder/application group (width) | Arithmetic | Action |
|---|---:|---|---|---|
| 405 | 99 | `{h : Option τ → ℤ}` (18) | 99+1+18=118 >100 | ok |
| 406 | 89 | `{U : MvPolynomial τ ℤ}` (22) | 89+1+22=112 >100 | ok |
| 407 | 88 | `(hV : V ≠ 0)` (12) | 88+1+12=101 >100 | ok |
| 408 | 86 | `index (map (Int.castRingHom ℝ)` (30) | 86+1+30=117 >100 | ok |
| 409 | 34 | complete renamed product argument (74) | 34+1+74=109 >100 | ok |
| 410 | 82 | `(fun j ↦ (h j : ℝ) / q j)` (25) | 82+1+25=108 >100 | ok |
| 411 | 59 | no next signature line | n/a | ok |

| Occurrence | Signature location | Form | Rewrite/rename |
|---|---|---|---|
| 1 | hr0 | 0 < r j | already correct |
| 2 | hl | 0 < l | already correct |
| 3 | hVd | V.natDegree ≤ l*r none | already correct |
| 4 | hVc | absolute coefficient ≤ M | already correct |
| 5 | conclusion | index … ≤ l*lem6Φ … | already correct |
| 6 | entire signature | zero ≥/> occurrences | no reversal or `_ge_`/`_gt_` rename |

## All 42 golfing rules

| Rule | Substantive status |
|---|---|
| 1.1 by exact | n/a: no wrapper. |
| 1.2 by rfl | n/a: no wrapper. |
| 1.3 rw+exact | hV′0 already uses rwa. hVmem degree/coeff rw followed by exact carries actual conversion, not a missing term after rw. |
| 1.4 simp+exact | Final combination already `simpa only […] using add_le_add …`. |
| 1.5 trailing rfl | n/a: absent. |
| 1.6 anonymous constructor | hVmem already refines ⟨nonzero, degree, coefficients⟩ with real dependent subproofs. |
| 1.7 apply+exact | n/a: direct exact/application terms already. |
| 1.8 by_contra | n/a: no contradiction. |
| 1.9 eta reduction | Lambdas encode constant functions, positivity, coordinate restriction or Subsingleton injectivity; none is an eta-only wrapper. |
| 1.10 have inlining | Complete inventory above; rewrites and multiple uses justify retaining each term. |
| 1.11 apply+intro | n/a: absent. |
| 1.12 redundant show | n/a: absent. |
| 1.13 obtain projections | hU.1 is one nonzero field; the other hU membership is passed as a whole. No repeated pair decomposition to obtain. |
| 1.14 merge rw | All map/product/index rewrites are already one chain; hVmem branch rewrites separate distinct goals. |
| 1.15 unsqueeze terminal | Independently compiled exact first text already tests broad simpa. Inherited actual timings establish the permitted exception; retain selected terminal only list. |
| 1.16 squeeze nonterminal | n/a: no bare nonterminal simp. |
| 1.17 dot notation | Existing map iff .2, hU.1 and equivalence .symm.injective appropriate. |
| 1.18 trailing parentheses | All retained parentheses group arguments of nested maps/division clearing; no gratuitous f(fun…) or f(by…) wrapper. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial ∃ helper | n/a: no existential declaration. |
| 2.1 grind | Actual clean whole-goal trial fails; log retained. |
| 2.2 pre-grind deletion | n/a: no grind in selected proof. |
| 2.3 simpa consolidation | Already consolidated terminal add_le_add. |
| 2.4 fun_prop | n/a: no continuity/measurability/function-property goal. |
| 2.5 positivity | Targeted hlR alternative compiles; same one-line bridge, retain explicit exact_mod_cast without churn. |
| 2.6 gcongr | Whole goal requires index/rename/Θ structure before arithmetic; final monotonicity already direct add_le_add, not a calc chain needing gcongr. |
| 2.7 lia/omega | n/a: no linear Nat/Int arithmetic subgoal; Nat.mul_pos and cast positivity already direct. |
| 2.8 aesop | Actual clean whole-goal trial leaves unsolved goal. |
| 2.9 norm_num/cast | exact_mod_cast already crosses the one real positivity bridge; no numeric computation or repeated normalization. |
| 2.10 decide | n/a: symbolic arbitrary polynomials/real supremum inequality, not closed decidable computation. |
| 2.11 field_simp/ring | n/a: division is cleared by div_le_iff₀; no algebraic identity. |
| 2.12 linear_combination | n/a: no ring/ring_nf terminal with hypotheses. |
| 2.13 wlog | n/a: no symmetric case branches. |
| 2.14 calc compression | n/a: no calc. |
| 2.15 <;> | hVmem's degree and coefficient goals require different lemmas and data; common automation does not replace those conversions. |
| 3.1 erw→rw | n/a: no erw; actual rw/rwa already. |
| 3.2 legacy analysis | n/a: neither legacy tactic. |
| 3.3 omega→lia | n/a: no omega. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 attributes | Private one-caller stage, no canonical simp/automation rewrite needed; no attributes added. |
| 3.6 simp_all | Actual whole-goal simp_all trial fails; no simp_all only in production. |
| 3.7 remove limits | No production limit override. |

Step-back reflection: exact?/apply? cannot replace the composed index/Θ proof, and converting everything into nested terms would hide rather than shorten the two rewritten bounds. The current proof follows the independent mathematical stages with the minimum already-available APIs. Cast cleanup is the only recommended edit. No new identifier was added to production, so hallucinated-name checks are vacuous; all existing invoked names are rechecked by independent and module compilation.

## Fresh sequential verification and exact compatibility

1. Independent exact first introduction and selected proof: `lake env lean /private/tmp/roth-theta-separated-helper/independent-helper.lean`, final exit 0. `independent-helper-final.log` prints both whole types, all 16 binders, proof-value checks using `value! true`, and only propext/Classical.choice/Quot.sound. A first scratch run failed solely because BinderInfo lacks ToMessageData; formatting was corrected with reprStr. Its failed `independent-helper.log` is retained and is not certification evidence.
2. Every drop/weakening, clean automation and positive alternative: actual source files, logs, interval maps and elapsed/exit statuses retained in this scratch directory. Expected-failure files exited 1; positive alternative/support/targeted positivity files exited 0. Only successful independent/actual checks certify axioms.
3. Fresh `lake build Roth.Theta`: exit 0, **44.291383167s**, raw `module-build.log`. This is the actual module build gate from this leaf, after the source edit.
4. Only after that build: `lake env lean /private/tmp/roth-theta-separated-helper/actual-compatibility.lean`, exit 0, **51.777429375s**. The original Index+Theta namespaces and exact public old-telescope adapter checks were copied as an immutable byte-identical prefix from the preceding accepted probe; only the new private audit tail is appended. Prefix equality is asserted, never weakened.
5. Fresh complete **unfiltered** native live-file `lean_diagnostic_messages` for `/Users/ramin/LEAN/Roth/Roth/Theta.lean`: success true, partial false, timed_out false, still_elaborating_lines null, failed_dependencies [], 0 errors, 11 warnings; full raw JSON `final-lsp.json`. No normal compiler/LSP request remained active before profiling.

Actual-built compatibility explicitly checks: exact approved public28 drop set `[DecidableEq, δ, hB, hl′, hδ]`; every retained public binder's type, order, BinderInfo and ordinary name; ENTIRE old `index_le_lem6` caller telescope with **no drops**, including hq, hB, δ and DecidableEq; independently elaborated original proof values; the actual private constant resolved programmatically by suffix; its entire first-introduction type, universes, ordinary names and BinderInfo; opaque actual proof value with `value! true`; allowed standard axioms only. The actual deleted `coeff_det_le_lem6M_aux` absence assertion still passes. The raw successful logs contain no PANIC, error or sorryAx.

All final warnings are outside the target range: header copyright at 1; retained unused hr at 93, hB/hr at 101, hB at 109, hr at 129 and 252; retained caller DecidableEq at 484 and 480, hq at 486; Θ_option_le DecidableEq at 582. These are unchanged earlier preferences or later original29 scope. No warning suppression was added.

The parent owns fresh whole-project `lake build` and separate `lake build Roth.LeanEval` after this frozen handoff. **Neither owner gate is claimed completed by this leaf.** Prior older full builds are not current-batch evidence. A whole-Theta instrumented profile is known to fail later at original29 `index_le_lem6` under default heartbeats, so this leaf's successful performance gate is explicitly prefix-only through original28.

## Scoped simplify and buzz

The host exposes no built-in Skill invocation for `/simplify`; the required holistic review was performed directly on this scoped change and proof: independent conversion, two Θ bounds and final scaling are coherent, no repeated proof skeleton or useful additional helper remains. Outcome: **ISSUES-FOUND-AND-FIXED**, redundant inner ℤ ascription removed; no additional recommendation. No automated handoff is falsely claimed.

Buzz uses the corrected Lean 4.34 real global `--profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0` command on the exact production prefix through public28, with both open named scopes closed. No target masks, source profiling options, limit raises, or imported self-theorem. The old terminal-only choice is a documented class-2 fat-simp exception with actual earlier measurements; it is preserved. Final rows/anchors and budget result are appended below from the fresh trace after all ordinary requests drained.

## Eleven-step checklist

- [✓] Step 1: full mandatory references and applicable workflows read.
- [✓] Step 2: full substantive 24-item audit, all haves/comments/casts covered.
- [✓] Step 2.5: five actual search methods, raw results, clean compiled generic-route trials.
- [✓] Step 2.6: all 16 effective binders have compiled drops; applicable weakenings/equivalents/support-localisation assessed; private literature exemption and inversion explicit.
- [✓] Step 2.7: every signature line has measured Unicode-codepoint packing arithmetic.
- [✓] Step 2.8: full per-occurrence inequality scan, no reversed comparison.
- [✓] Step 3: all 42 golfing rules have a concrete result or substantive n/a.
- [✓] Step 4: whole-goal/term-mode/strategy alternatives reflected on with clean search evidence.
- [✓] Step 5a: complete unfiltered final native LSP has 0 errors and no partial/timeout/dependency failure.
- [✓] Step 5b: module build, immutable independent originals, exact built adapters/values/axioms, scope and final performance gates recorded.
- [✓] Step 6a: no rename needed; no rename queue or shared report touched.

Refactoring needed: none. No new helper requiring another audit. Comments-preserved: none present in assigned private proof; all surrounding public documentation/three Step comments unchanged. Total proof lines **26 → 26**, module **943 → 943**; one redundant type annotation removed. Public `index_det_le` remains **24 proof lines including all 3 Step comments**, under its ordinary **≤30** cap; it is not a module Main results headline and no ≤15 requirement is invented.


## Accepted fresh real global profile and final gates

Command: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-separated-helper/final-prefix.lean`, **exit 0**, 132.680699708s wall time, raw UTF8 log **115495771 bytes**. Every preceding source/import/context byte is preserved; only final `end Lemma6` / `end Roth` closes the prefix. No declaration mask or production source option is used. All ordinary requests were drained before this sole uncontended profile. This is prefix-only, not a whole-file performance pass.

| Declaration | Inherited same-source baseline | Fresh final | Raw outer / proof anchors | Result |
|---|---:|---:|---|---|
| index_separated_mul_le_aux | 610.207ms | **655.221ms** | final-profile.log 856951 / 857048 | <750ms and <1000ms |
| public index_det_le | 668.264ms | **742.222ms** | final-profile.log 974329 / 974461 | <750ms and <1000ms |

Totals include outer command plus associated disjoint top-level async elaboration, realizeConst/addDecl/kernel and linter jobs. Nested tactic/command nodes are not double counted. Exact names, line anchors and component times are recorded in `final-timings.json` and `final-profile-manifest.json`. Both final measurements are below the >=750ms repeat trigger, so no repeat is required. These are fresh final numbers; the older terminal-simp comparison and baseline are explicitly inherited. The small redundant-ascription edit is not presented as a measured performance optimization.

Buzz outcome: **FAST-BOARD** for assigned helper and protected public28; no declaration over 1000ms, no performance deferral, no new limit/scaffolding/instance change. The deleted coefficient helper is absent from both final source and trace.

| Gate | Result | Concrete evidence |
|---|---|---|
| lake_build_file | PASS | fresh `lake build Roth.Theta`, exit 0, module-build.log, 44.291383167s |
| definition_protected | PASS | no def/abbrev or visibility change |
| theorem_statement_protected | PASS | only redundant private coefficient ascription; elaborated entire first private type and all public contracts exact; immutable old adapters/values compiled |
| structure_gate | PASS | helper 26≤30, no >10 branch; public28 unchanged 24≤30 |
| naming_gate | PASS | descriptive private snake_case `_aux`, no forbidden pattern |
| line_packing_gate | PASS | seven measured signature rows, no outstanding repack |
| inequality_orientation_gate | PASS | all five comparison occurrences correctly oriented, no ≥/> |
| no_unintended_breakage | PASS within leaf | actual public28 exact drop5 and entire original29 caller no-drop adapter compile after actual module build |
| actual_axioms_and_original_values | PASS | value! true, clean raw outputs, standard3 only; actual deleted helper absence |
| final_live_LSP | PASS | complete unfiltered success, no partial/timeout/dependencies; 0 errors/11 inherited warnings |
| final_real_profile | PASS | real global exact prefix exit0; both retained targets below repeat/budget thresholds |
| owner_full_build / separate LeanEval | pending owner | deliberately not run or claimed by this leaf |

Overall dedicated helper audit: **PASS**. Final source SHA256 **`c6e59b0ff252c0cdfc0e00070bb7c0c5bea3a53e0786889767f4b1594f5e6ee3`**, 943 lines. Source is frozen, edit authority revoked, **all compiler/LSP/profile requests drained**. No new helper, recommendation, rename, or confirmation remains. This report contributes **0 original declarations** to owner counters.
