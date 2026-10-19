# Phase 4 — `Roth.exists_delta_bound`

Scope: original declaration 5, `Roth/MainLemma.lean:66–98` on entry; final lines 67–83. This report covers this declaration and its two exact call repairs at `Roth/Main.lean:300,313` and the authorized one-line context-insulation repair at324, not completion of the file/checkpoint/project. No project helpers were introduced, even temporarily. No Git or shared progress/rename-queue writes.

The proof now uses continuity at zero and a common radius below `1/m`. The unnecessary hypothesis `hn : 0 < n` is removed. The conclusion is strengthened to the closed interval `0 ≤ δ ≤ δ₀`; the remaining outer binder names/order/implicitness and every other original declaration are preserved. The public description now states the strengthened interval; its verbatim historical source quotation remains unchanged. Declaration: 33→17 lines; actual proof: 30→15 lines. Necessary sorted import: `Mathlib.Analysis.SpecialFunctions.Pow.Continuity`. Downstream edits: `exists_delta_bound hn hm`→`exists_delta_bound hm`, and its returned bound receives `hδ0.le h1.le` in place of `hδ0 h1`. After both direct closed-contract caller samples increased, a bounded old-local-contract control returned near the high original timing; the authorized final one-line repair restricts Main324 to `linarith only [a1, a2, a3]`. This insulates the arithmetic from the changed quantified hypothesis. No Main audit/count credit is claimed.

## Step 1 — required reading and input baseline

Read installed Lean 4/mathlib-quality skills, the entire cleanup command including its complete Mode A/Phase 4 prompt, all of golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, profiling, and applicable style/naming sections. First response confirmed the five mandatory full reference reads. Native metadata/schemas were inspected through ALL_TOOLS; no ChatGPT-math/simplify/buzz callable tool is available. No subagents spawned.

Entry file SHA256 `0236435831af553f54e04569caadb7b985e0a556dbebf51d454e53abf3ea2abb`. Immutable original target matches both project-original d2eb5e9a… source and owner entry baseline exactly. Main entry is byte-identical to project-original Main, SHA256 `f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069`. Full native entry MainLemma: success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors, no target warnings. Three outside warnings: header line1; log_B₁_gt hδ0/hr₁ at original150. Full original target was profiled before edits; actual baseline data below.

## Step 2 — all 24 audit items

1. **LINT:** target has zero warnings/errors on complete unfiltered final native MainLemma. Outside warnings persist at header1 and log_B₁_gt135. Full Main is likewise error-free; its outside warnings are header1, hδ333, hQ474, hc475. No suppression added.
2. **HAVE SCAN:** all old/new have declarations audited in the table below. Explicit E/c witness locals and their denominator/rpow proof are replaced by the continuity argument. The final h4n term contains a meaningful embedded nlinarith proof; the now-single-use no-by hs was inlined.
3. **SET_OPTION:** no declaration/file limit option in the change; none added/raised.
4. **SIMP SQUEEZE:** old nonterminal `simp only [lt_min_iff] at hδ` correctly squeezed, then removed with witness change. Final inline zero-value/metric reductions use terminal `simpa … using`; no bare nonterminal simp or squeezed terminal simp remains.
5. **NAMING:** `exists_delta_bound` names exactly the common positive delta threshold, uses snake_case, matches no forbidden numeric/abbreviation/orientation pattern; no rename warranted or queued. No rename applied.
6. **LINE PACKING:** final signature codepoint widths 96/79; full arithmetic table below. Proof max width96 including signature.
7. **BY PLACEMENT:** by remains at the end of its preceding line everywhere.
8. **FORMAT:** 2-space proof indentation, no empty proof lines, one tactic per line, Unicode lambda arrow ↦, no haveI/letI, no consecutive rw chain.
9. **COMMENTS:** 0→0 proof-body comments. Existing source quotation byte-identical; first doc sentence updated to the stronger closed interval. No removed proof-body comments.
10. **DOCSTRING:** public uniform-threshold guidance strengthened to the closed interval; source lemma, equation references and quoted Lean note retained exactly; it distinguishes fixed-m uniformity. No helper docstrings introduced.
11. **VISIBILITY:** public because Main.exists_delta consumes it. Classic dialect; no module/public import rewrite.
12. **STRUCTURE:** headline proof15≤15; largest nested proof2 lines; no branch>10. No helper or decomposition flag needed. The existential conjunction deliberately remains correlated, as explicitly required by the dispatch/source note; splitting into unrelated witnesses would change the contract.
13. **MATHLIB:** all five actual methods + true pretarget exact?/apply? probe below. Partial matches supply continuity/neighborhood API; target retains the Roth-specific numeric gap and eta expression. No wrapper helper introduced.
14. **JUNK DEF:** n/a theorem; no global def/abbrev changed.
15. **EXISTS LEMMA:** public, nontrivial uniform existential with correlated bounds, not a private rfl constructor.
16. **SHOW/CHANGE:** old term-mode numerical show removed with rpow inversion. No show/change remains.
17. **PUSH_NEG:** none.
18. **GENERALISE:** all four outer binders plus the inner δ value and both interval hypotheses, actual drops, weakest hn removal, strict boundary controls, inversion and public literature search below. Current telescope has three binders; no class/decidability/section/universe binder omitted.
19. **INEQUALITY:** zero reversed ≥/> in Lean signature/hypotheses and no _ge_/_gt_ in name. Explicit scan table below.
20. **NORMAL-FORM:** source's common threshold for every nonnegative δ up to and including it established; generic point-local continuity API used internally rather than a new custom condition.
21. **SYNTAX-GEN:** hn removed with actual n=0 proof; remaining outer binder order/implicitness unchanged; stronger inner conclusion and exact old-positive adapter kernel-checked. Both calls repaired.
22. **IMPORT-FANOUT:** Pow.Continuity is necessary: actual compiler and native #check show continuousAt_rpow_const unavailable before it, and native fun_prop succeeds after it. This non-leaf module already contains Real.rpow eta; the import is mathematically appropriate and parent-authorized. All affected dependencies/Main/root/LeanEval built successfully.
23. **CASTS:** 0 redundant ascriptions dropped; 8 explicit Nat→real casts retained (signature m; h4n n/m; hgap n/m; hc m; and both minimum denominators). Three scalar/type-fixing ascriptions remain: real numeric bound, real zero for hm0, and real fractional exponent in the zero-rpow proof. The final `: … ≠ 0` and `: 0 < min …` are meaningful proposition annotations, not scalar coercions. None ascribes an expression already known to have the same scalar type. Every explicit annotation checked; no coercion workaround introduced.
24. **INSTANCE-NAME:** n/a no instance introduced/renamed.

Issues fixed: headline length/performance, unnecessary hn, unnecessary strictness at both inner interval endpoints, caller arity and returned-bound applications. Refactoring needed: none in this target. Main.exists_delta receives only the three exact repairs described here, including the authorized arithmetic premise restriction justified by caller trace/control evidence. Its independent full audit and any remaining performance work belong to the owner's next-file queue; no Main original is counted here.

### Have scan — exhaustive

| Original have(s) | by/content? | Uses/action |
|---|---|---|
| hn', hm', hm0, h4n, hE0, hsm, hc0 | tactic proofs | Mathematical content; replaced/reproved as needed by continuity strategy; hn' disappears with hn. |
| hs := Real.sq_sqrt hm0.le | no by | Used twice in the 14-line continuity version; final direct sqrt API leaves one use, so inline into the gap proof. |
| hs0 := Real.sqrt_nonneg m | no by | Used by old nonlinear estimates; eliminated by the direct sqrt comparison API. |
| heta, hpow, hz, h10, h6 | tactic proofs | Entire explicit inverse-power/linear-margin argument removed. |
| anonymous `have := Real.rpow_lt_rpow …` | no by, one use in rwa | Single-use candidate eliminated with old inverse-power strategy. |
| Final hm', hm0, hgap, hc | tactic proofs | Each contains actual cast/arithmetic/continuity/simplification reasoning; keep. |
| Final hlt | no by, transitivity of closed upper bound and half-radius inequality | Used for both strict min projections; retain shared fact, no repeated arithmetic search. |
| Final h4n | term with embedded by nlinarith proof | Mathematical square-root estimate; contains proof content, used by explicit positive multiplication. No trivial wrapper. |

## Step 2.5 — actual five-method Mathlib search

| Method | Actual query | Result |
|---|---|---|
| A LeanFinder | continuous real function at zero is below a strictly larger bound for all sufficiently small positive inputs | ContinuousAt.eventually_lt; additional generic convergence results. |
| B Loogle | `ContinuousAt, _ < _, ∀ᶠ _ in _, _` | ContinuousAt.eventually_lt, Metric.continuousAt_iff', EMetric analogue. |
| C LeanSearch | ContinuousAt eventually less than constant neighborhood metric exists positive radius | ContinuousAt.eventually_lt; continuousAt_def; Metric.continuousAt_iff. |
| D untruncated source rg | full `exists_delta_bound` (no hit); eventually_lt, eventually_lt_const, eventually_nhds_iff(_ball), continuousAt_rpow_const, lt_sqrt_of_sq_lt | Actual generic lemmas in Topology/Order/OrderClosed, MetricSpace/Pseudo/Defs, SpecialFunctions/Pow/Continuity, Analysis/Real/Sqrt. No exact project-specific theorem. |
| E native local name search | `ContinuousAt.eventually_lt` | Positive source hit (index warming; used as presence, never absence). |

Actual native `lean_goal` on original first tactic returned the target with n,m,hn,hm. Actual `lean_multi_attempt` there: grind failed, aesop exhaustive search failed, exact? could not close, apply? gave only logical existential rearrangements/unfinished suggestions. This is true pretarget context (source imports Lattice/Theta, never current MainLemma/current target), so it cannot find itself. Full-name source rg and elaborator probe supplement the five presence searches. Common-equivalents lookup: neighborhood API, not a new finiteness/discrete/bornology predicate. Auxiliary variants searched: eventually_lt/_const, eventually_nhds_iff/_ball, continuousAt_rpow_const/continuous_rpow_const, lt_sqrt_of_sq_lt. Conclusion: **partial match; retain domain-specific theorem and use Mathlib API directly**, with no convenience wrapper.

Identifiers introduced are source/native/compiler-verified: ContinuousAt, Metric.eventually_nhds_iff, ContinuousAt.eventually_lt, continuousAt_const, Real.continuousAt_rpow_const (used through fun_prop), Real.zero_rpow, Real.dist_eq, abs_of_nonneg, half_lt_self, Real.lt_sqrt_of_sq_lt, Real.sqrt_pos, mul_lt_mul_of_pos_right. Nat.zero_le/trans_lt and existing sqrt/cast/min API all compile in the actual full file. No hallucinated identifier survives.

## Step 2.6 — generalisation, all effective binders

### 2.6a — exhaustive parameter/hypothesis status

| Original binder | Kind/use | Candidates actually tested or rejected on mathematical grounds | Verified result |
|---|---|---|---|
| `{n : ℕ}` | implicit structure value, natural polynomial degree, real scalar coefficient and m bound | Drop in isolated autoImplicit=false prefix; scalar ℝ restatement would alter the specified degree/domain and need an extra nonnegativity parameter, not a useful mechanical weakening of this API. No class/point/universe weakening applies. | Drop rejected: unknown n; retain natural parameter. |
| `{m : ℕ}` | implicit dimension, natural power in eta, sqrt and reciprocal | Drop isolated autoImplicit=false; ℝ restatement would require changing eta's Nat exponent/dimension definition and conclusion, not same object. | Drop rejected: unknown m; retain. |
| `(hn : 0 < n)` | old positive denominator witness | Old-proof drop rejects unknown hn; this alone is not necessity. Reprove entire theorem without hn using continuity; this is weaker than retaining tautological 0≤n. | **Removed**, actual full-file proof and n=0,m=1 application compile. |
| `(hm : 16*n² < m)` | positive gap and m positivity | Drop; strict→weak ≤. Both isolated tests recorded; additionally compile actual semantic counterexamples at n=0,m=0 and n=1,m=16. | Drop/≤ fail; strict hypothesis necessary for this contract, retained. |
| Inner `δ : ℝ` | universally quantified input value | Removing its binder leaves δ unbound (autoImplicit=false); generalizing to an ordered field changes real rpow/sqrt and is not this real-valued eta API. | Retain real input and universal scope. |
| Inner `0 < δ` | original lower restriction | Weaken to `0 ≤ δ`; continuity and `abs_of_nonneg` include zero. Dropping all lower control is false at n=0,m=2,δ=−1, where eta=50√2>1. | **Weakened to nonnegativity**, actual zero-endpoint application and certified negative control. |
| Inner `δ < δ₀` | original upper restriction | Weaken to `δ ≤ δ₀` by choosing half the common positive radius. Dropping upper control is false at n=0,m=1,δ=1, since 1<1 fails. | **Weakened to non-strict upper bound**, actual δ=δ₀ endpoint application and certified negative control. |

### 2.6b — candidate verification

Negative compiler batch: `negative-drops.lean`, autoImplicit=false, no import of current target; expected exit1, never a positive gate. Unknown n/m/hn/hm and ≤/< mod_cast mismatch recorded unfiltered. Positive generalisation evidence is the *new full proof*, actual new opaque type and n0m1 application, not an expected-error test. Strict boundary counterexample uses exact sqrt16=4 and nonnegative eta.

The existential δ₀ is a correlated output witness, not an input assumption. Its positive-radius conclusion is deliberately retained so the interval contains usable positive inputs; removing it would permit a vacuous or zero interval and weaken the intended theorem. No typeclass, decidability, universe or implicit section parameter exists beyond the listed telescope. Inversion check: eta's continuous positive-power structure is unfolded once; its abstract neighborhood portion is already Mathlib's ContinuousAt.eventually_lt plus Metric.eventually_nhds_iff. No new abstract wrapper is warranted. The remaining numeric square-root estimate is Roth-specific. No further warranted public restatement/rename.

### 2.6c — larger candidates and authorization

Removing public hn and strengthening both inner interval conditions changes the public API, so the installed command would otherwise flag these as larger changes. The standing user authorization and explicit owner dispatch authorize implementation now. All three are implemented with explicit old-contract adapter and exact caller repair. No unresolved larger candidate remains. Changing Nat dimension or the real power/sqrt structure would restate the mathematical objects without an identified useful target, so no such rewrite is warranted.

Joint signed-interval restatement considered: continuity also bounds small negative real inputs if both interval premises are replaced by a symmetric neighborhood condition. This changes the interval/API shape together rather than dropping either present premise; the certified −1 counterexample is specifically about dropping lower control while retaining only the upper bound. No project consumer needs negative-base eta, and the fully general signed-neighborhood fact is already the Mathlib continuity API used here, so another Roth-specific signed wrapper is not warranted. The retained nonnegative closed interval is the useful numerical threshold API.

### 2.6d — public literature search

Actual web queries: “Roth theorem m 16 n squared delta continuity lemma”; “continuous function strict inequality neighborhood at point”. Primary mathematical hit: [Takloo-Bighash et al., Diophantine Analysis and Approximations, pp151–152](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), explaining the small perturbation at δ=0 after m>16n². Other returned instructional sources included Huji Chapter4_2.pdf and Ohio State analysis midterm solutions; no additional useful Roth hypothesis weakening emerged. Canonical local source clean.tex1211–1248 gives exactly the fixed-m limit argument;1305–1307 requests the correlated uniform threshold. The numerical argument does not need positive n; machine-checked n=0 evidence confirms this. ChatGPT-math unavailable (ALL_TOOLS checked; owner-authorized skip). Public approval for warranted assumption removal and necessary import was already given; no unresolved choice remains.

Additional final searches include the literal generalization keyword, with complete returns saved in literature-final-*-search.json. The first three returned hits are recorded rather than selectively presenting relevant-looking later hits:

| Exact added query | First three returned hits | Assessment |
|---|---|---|
| `Roth "16" "delta" "main lemma" generalization` | [Kiel thesis](https://www.math.uni-kiel.de/geometrie/de/malte-kliemann/master-thesis), [Kenig article](https://emis.de/ft/50692), [Impagliazzo–Paturi–Saks](https://cseweb.ucsd.edu/~paturi/myPapers/pubs/ImpagliazzoPaturiSaks_1997_siamjc.pdf) | Unrelated main lemmas; no mathematical claim here relies on them. |
| `continuous function strict inequality neighborhood at point generalization` | [Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Continuous_function), [Wikipedia](https://en.wikipedia.org/wiki/Continuous_function), [Vaia exercise](https://www.vaia.com/en-us/textbooks/math/elementary-real-analysis-1-edition/chapter-5/problem-24-let-f-be-continuous-in-a-neighborhood-u-of-the-po/) | Secondary material inventoried only; actual proof relies on primary Mathlib continuity API and the cited Roth source. |

### 2.6e — applied results

Removed hn, weakened inner positivity to nonnegativity, and weakened the strict upper restriction to a closed upper restriction. Both conclusions remain strict. Fresh native checks apply to the final changed files; old positive/strict contract is independently adapted with `.le` for both input proofs. No extra helper.

## Step 2.7 — measured line packing

Reference: actual `#check @Roth.exists_delta_bound` at `format.width=100` is in successful final-v5-semantic-check.log. It shows implicit n,m, explicit hm and exactly the uniform existential conclusion.

| Signature line | Codepoints | Next complete syntactic premise | Arithmetic | Action |
|---|---:|---|---|---|
| 67 | 96 | `δ ≤ δ₀ →` (8) | 96+1+8=105>100 | ok |
| 68 | 79 | none; `:= by` already on this line | n/a | ok |

No underpacked hypothesis/conclusion line; no wide-hyp exception used. Max target source width96.

## Step 2.8 — inequality scan

| Occurrence | Location | Original reversed inequality | Rewrite / rename |
|---|---|---|---|
| none | full signature67–68 and every outer/inner hypothesis | n/a — zero ≥/> in Lean code | none; name has no _ge_/_gt_ |


## Step 3 — all 42 golfing rules

### Golfing-rule pass (42 rules)

| Rule | Actual result / applicability |
|---|---|
| 1.1 | No by-exact wrapper in target; `exact_mod_cast` is meaningful cast automation. |
| 1.2 | No by-rfl. |
| 1.3 | Old rpow `rwa` already combined rewrite and reuse; new strategy removes inverse-power block. |
| 1.4 | Inline zero-value proof uses `simpa … using hgap`; final metric reduction uses `simpa … using` radius bound. |
| 1.5 | No simp followed by rfl. |
| 1.6 | Threshold and correlated conjunction assembled with the outer existential/positivity constructor in refine and the two correlated bounds in exact. |
| 1.7 | No apply/exact chain survives. |
| 1.8 | No contradiction/push-neg chain. |
| 1.9 | The final lambda consumes nonnegative-delta and closed-threshold proofs, so cannot eta-reduce. |
| 1.10 | Old single-use anonymous rpow fact disappears with explicit threshold strategy. In the initial 14-line version hs was used twice; the final sqrt API leaves one use, so hs is inlined into gap arithmetic. Final h4n contains a meaningful embedded nlinarith subproof. Final hlt is a shared transitivity fact used by both strict min projections; the other new have statements carry tactic proofs. |
| 1.11 | Direct refine with lambda used for the uniform-threshold conclusion. |
| 1.12 | Old numerical show disappears with explicit threshold strategy; no redundant show remains. |
| 1.13 | Existing destructuring with obtain retained; new neighborhood radius likewise destructured directly. |
| 1.14 | No consecutive rw sequence survives new strategy. |
| 1.15 | No squeezed terminal simp survives: new terminal reductions are simpa. |
| 1.16 | No bare nonterminal simp; old nonterminal simp only [lt_min_iff] removed by direct projections. |
| 1.17 | hc.eventually_lt and Metric.eventually_nhds_iff.mp use appropriate dot notation. |
| 1.18 | Parentheses retain a nested function argument / metric simplification where `<|` would not shorten a trailing-paren chain. |
| 1.19 | No push_neg. |
| 1.20 | Public nontrivial correlated threshold theorem, not a private rfl-existential constructor. |
| 2.1 | Actual native whole-goal grind at original pretarget position failed. |
| 2.2 | No grind survives in final proof; no preceding tactics to remove. |
| 2.3 | Inline zero-value proof and metric step use simpa consolidation; no simplification/assumption chains. |
| 2.4 | Actual native import probe proves the rpow ContinuousAt goal with fun_prop (disch := positivity). Final `[eta]` argument is source-verified explicit unfolding support, then compiler-verified. Without Pow.Continuity import, compiler/native both fail; necessary import authorized by owner. |
| 2.5 | Positivity discharges exponent nonzero, radius minimum positivity, and continuity side conditions; at live gap73:52 it correctly reports not a positivity goal. |
| 2.6 | New square-root estimates use ordered polynomial arithmetic; a plain gcongr cannot manufacture their strict square-root comparison. Actual native 14-line-version live goal73:52: gcongr made no progress; grind failed; positivity reports not a positivity goal. The existing nlinarith closes it. |
| 2.7 | No remaining Nat/Int linear-arithmetic goal: scalar estimates are real inequalities; exact_mod_cast handles the natural bound. |
| 2.8 | Actual native whole-goal aesop failed exhaustive search. |
| 2.9 | Actual bound cast uses exact_mod_cast; concrete edge probes use norm_num. |
| 2.10 | Quantification over reals / continuity, not a finite decidable computation; no native_decide. |
| 2.11 | Old field_simp denominator identity is removed by continuity; no final denominator equality to normalize. |
| 2.12 | No final ring/ring_nf with contextual hypotheses. |
| 2.13 | No symmetric case split. |
| 2.14 | Old two-step eta calc disappears entirely; no final calc chain. |
| 2.15 | Constructor goals are positivity and a quantified property, so no repeated closing tactic applies to both; direct correlated constructor is clearer. |
| 3.1 | No erw. |
| 3.2 | fun_prop used directly; no continuity/measurability tactic. |
| 3.3 | No omega in final target; no integer arithmetic left to migrate to lia. |
| 3.4 | No rcases-with-rfl or subsequent substitution. |
| 3.5 | One theorem, no reusable automation-normal form needing a new global attribute. |
| 3.6 | No simp_all only. |
| 3.7 | No heartbeat/depth/instance limit option in original or new target. |

Step-back reflection: actual native exact? fails; apply? finds only existential logical reshuffling. Whole grind/aesop do not find the analytic threshold. The different continuity strategy follows the source limit argument, removes the unnecessary n>0 restriction and inverse-rpow algebra, and keeps one common threshold. No new local API helper or wrapper is needed because Mathlib already provides the abstract neighborhood theorem.


## Step 4 — holistic reflection / simplify-equivalent review

The entire proof cannot be closed by grind/aesop/exact? in actual pretarget context. The source limit argument is clearer than explicit inverse-rpow thresholds. A common min radius preserves both bounds; no helper, duplicate skeleton or extra public API is needed. The initial continuity version passed at14 lines but measured926/952ms. Trace-guided use of Real.lt_sqrt_of_sq_lt and a two-fact nlinarith certificate improves the intermediate V2 positive/strict15-line proof to721.306ms. The final V4 closed-interval proof measures765.392/739.630ms, with all old/new sources and measurements retained. Speed and direct Mathlib use justify one extra line. No further marginal compression is warranted.

No callable built-in simplify/buzz skill tool is installed (ALL_TOOLS metadata checked); this is an explicit scoped manual holistic review plus the actual prescribed profiling workflow, not a claim that an unavailable tool was invoked. Mode A's required Buzz measurements/gates are fully recorded below. Holistic outcome: ISSUES-FOUND-AND-FIXED (numeric searches reduced); no unresolved target suggestion.

## Semantic protection and exact contracts

`semantic-final-v4-repaired.lean` imports the freshly rebuilt actual modules and independently proves the immutable original target with its entire old proof. That proof does not call the current target or any new helper. It also replays the entire exact original Main.exists_delta proof, replacing its target call only with the independently reproved old alias and reproducing its original private eta bound locally. It never uses current Main.exists_delta to prove the old Main result. Owner separately verified byte recovery of both complete original proofs after those justified alias substitutions.

A separate adapter retains the full exact old signature, including unused explicit name hn; its proof explicitly projects the new theorem and maps positive/strict arguments through `.le` to the stronger new theorem. Another separate expected-new declaration checks the actual new binder contract, including both non-strict inner restrictions. Recursive forall/lambda syntax comparison additionally checks inner binder names/BinderInfo/domains beneath the existential/conjunction, alongside the definitional-equality conclusion check. Native/compiler checks do not confuse these two types. Successful final `final-v5-semantic-check` (exit0) performs all three comparisons:

1. Entire independent old theorem type = old-contract adapter type.
2. Actual current theorem type = independently stated new-contract type.
3. Actual current Main.exists_delta type = entire independent original Main proof's type. The final V5 semantic run repeats these checks after rebuilding the changed actual Main opaque body; its old full-proof source remains the same immutable successful harness.

Each comparison checks exact universe parameter lists, every outer binder's name/order/BinderInfo/domain, and the conclusion by kernel definitional equality. Actual `getConstInfo` values must be opaque theorem bodies; their *values* are inferred/type-checked against the actual declaration types. Actual target and Main bodies, independent old target/Main proofs and old adapter all have exactly the standard axiom list `[propext, Classical.choice, Quot.sound]`.

Verbose actual metadata (successful `metadata-v4-check.log`):

| Contract | Universe list | Binder order, BinderInfo and domain |
|---|---|---|
| Original / old adapter | [] | n implicit ℕ; m implicit ℕ; hn default 0<n; hm default16*n²<m |
| Actual new | [] | n implicit ℕ; m implicit ℕ; hm default16*n²<m |
| Main.exists_delta original = current | [] | n implicit ℕ; m implicit ℕ; hn default0<n; hm default16*n²<m; κ implicit ℝ; h47 default4*n*√m<m; h47' default2*m/(m−4*n*√m)<κ |

Exact original/old-adapter target conclusion (preserved by adapter):
```lean
∃ δ₀ : ℝ, 0 < δ₀ ∧ ∀ δ : ℝ, 0 < δ → δ < δ₀ →
  δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2
```
Actual stronger new target conclusion:
```lean
∃ δ₀ : ℝ, 0 < δ₀ ∧ ∀ δ : ℝ, 0 ≤ δ → δ ≤ δ₀ →
  δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2
```
Main's entire original conclusion is unchanged:
```lean
∃ δ : ℝ, 0 < δ ∧ δ < 1 / m ∧
  eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧
  (m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ
```

Actual new closed-contract application at n=0,m=1 and explicit old-positive/strict adapter at n=0,m=1 succeed. One generic actual application checks δ=0 and δ=δ₀ simultaneously for every n,m satisfying hm. Separate actual negations certify impossibility of dropping the lower interval restriction (n=0,m=2,δ=−1; eta=50√2>1) and the upper interval restriction (n=0,m=1,δ=1; 1<1 fails). Actual negations at n=0,m=0 and n=1,m=16 compile, with explicitly real reciprocal/right-side bounds (no accidental Nat division). These are positive kernel-checked controls, separately from the expected-error drop probes.

## Call-site and source inventory

Actual full Lean-source rg: the only named theorem term call is Main.lean300, with its derived function application at313 also repaired. Main.lean1 and Roth.lean13 import MainLemma; Roth.lean14 and LeanEval.lean1 import Main. All affected modules MainLemma/Main/LeanEval/root Roth were built; complete unfiltered native diagnostics were required for both edited source modules and completed successfully. Root and LeanEval source were untouched; owner's later separate independent Eval remains pending owner work.

Full-file byte comparison confirms MainLemma differs only by the new sorted import, first unquoted target doc sentence and target declaration; Main differs only by the exact300 arity and313 derived-bound repairs plus the authorized324 linear-premise restriction. The proposed three-line local adapter was tested only in scratch and was not inserted live. The verbatim source quotation and both files' other original declarations/comments are byte-identical to entry. No pins change. No project helper was introduced or later removed, so there is no first-insertion helper history or extra helper audit to count. Rename queue (including Index/B₁ entries), central logs and Git untouched.

## Step 5a — actual complete native results

Final files `native-final-v4-mainlemma.json` (exact unchanged final MainLemma source) and `native-final-v5-main.json` (new final Main source) contain complete unfiltered native tool returns, each success=true, partial=false, timed_out=false, failed_dependencies=[], isError=false, zero errors. All3/4 warnings are the explicitly listed pre-existing outside-scope warnings; target and changed consumer declaration are warning-free. Actual final live source corresponds to15-line 37ac02… closed-interval version (MainLemma warning positions135), not the preceding14-line version.

Earlier successful native goal/multi-attempt evidence is retained too: the14-line live gap goal had n,m,hm,hm',hm0,hs,h4n and no hn; grind failed, gcongr made no progress, positivity said not a positivity goal. Those failed *alternatives* never modified the source and are not positive gates. The final gap proof now supplies the exact two numeric facts directly.

## Step 5b — actual tool-call and diff gates

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file / all affected dependencies | pass | `lake build Roth.MainLemma Roth.Main Roth.LeanEval Roth`, exit0,72.067s,2468jobs; final-v5-affected-build.json/log |
| lake_build | pass | actual `lake build`, exit0,5.938s,2467jobs; final-v5-full-build.json/log |
| definition_protected | pass | no global def/abbrev changed; source-protection-v5.json verifies exact full-file expected diff |
| theorem_statement_protected | pass, authorized exception | hn removal and both inner strict→non-strict weakenings explicitly authorized; exact old-positive/strict adapter and expected stronger current contract checked; Main type unchanged |
| cumulative_no_unintended_breakage | pass | sole term caller repaired; all affected modules built, both edited source files full native0errors |
| structure_gate | pass | actual15 noncomment proof lines≤15, no helper/branch>10; correlated existential preserved per explicit dispatch |
| naming_gate | pass | mathematically descriptive snake_case, no forbidden pattern, no rename needed |
| line_packing_gate | pass | complete final96/79 codepoint table, no repack row |
| inequality_orientation_gate | pass | explicit zero-reversed-inequality table; no orientation rename |
| actual bodies / standard axioms / old contracts | pass | final-v5-semantic-check exit0; metadata-v4-check exit0 |

The first final V4 semantic harness run retained two new scratch-only edge-proof failures (n0m1 cast normalization and final scalar ring identity); repaired fresh source/log exit0, all project sources unchanged. Expected-error batch negative-drops exits1 by design and is never listed as a positive build gate. Initial closed-interval candidate without explicit `[eta]` unfolding failed fun_prop and minimum type inference; its exact source/log were retained and fixed by documented `fun_prop … [eta]` plus explicit real denominator. Initial continuity compile without Pow.Continuity failed only fun_prop; retained/repaired through the necessary import. Initial semantic-print harness had reserved identifier at / unsupported pp.width / normalization issues; its exact failed source+log are retained, repaired final semantic gate exits0. Optional verbose metadata print initially used obsolete getLocalDecl, source/log retained; actual source-verified getFVarLocalDecl repair exits0. None of these scratch failures introduced a live sorry, axiom or deferred source error.

## Actual performance workflow / scoped Buzz pass

Outcome: FIXED for Roth.exists_delta_bound. The Buzz tool itself is unavailable; the installed exact profiling workflow was executed directly, with raw trace diagnosis, numerical-API repair, statement/source protection, complete builds/native checks and frozen repeat. No deferral or silent decomposition flag for this target.

| Decl | Before | After | Root cause | Fix |
|---|---|---|---|---|
| Roth.exists_delta_bound | 1341.057 / 1394.541ms | 765.392 / 739.630ms | Explicit inverse-power/denominator witness and broad nonlinear search | Continuity at zero; direct lt_sqrt_of_sq_lt; explicit multiplication certificate; closed half radius |

maxHeartbeats raises removed:0; added:0. Other Lean limits raised:0. No profiling scaffolding in live files. Deferred in this original:none. The direct consumer remains over1000ms and in the owner’s next-file performance queue; no budget pass is claimed. Final pair is compared with every original/intermediate sample below. Final caller samples below are compared with both preserved pre-edit baseline samples, rather than selecting the fastest sample.

Exact commands used lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 PREFIX, with actual full live source prefix through the target plus end Roth. Prefixes/source snapshots are preserved verbatim. Per sample, the timing JSON includes the raw UTF8 log SHA256, exact target command/proof/kernel/lint anchors and raw line numbers. Actual accepted roots in these runs are disjoint column-zero Elab.command and Elab.async events within the actual target command boundary. Compiler/kernel and lint categories are identified from their addDeclCore/runLintersAsync anchors; no separate Compiler or Elab.lint event was observed/countable in these samples. Nested kernel/linter children and Meta.whnf events are not double-counted. Preceding four definitions, any preceding caller declarations, and end-Roth command/lint are excluded. No live helpers exist. All valid runs were serialized with no compiler/native overlap; owned process PID/PGID/start/end/exit/drain metadata are retained. External420-second bounded runner is a process timeout, not a Lean limit change.

Every retained valid sample, including intermediate versions (milliseconds except wall seconds):

| Sample | Command | Proof/async | Compiler/kernel | Lint | Total ms | Wall s | Prefix SHA prefix |
|---|---:|---:|---:|---:|---:|---:|---|
| baseline-valid | 18.679 | 1228.334 | 60.517 | 33.527 | 1341.057 | 69.938 | 89f7dab7179d |
| baseline-valid-repeat | 17.989 | 1279.681 | 61.988 | 34.883 | 1394.541 | 66.386 | 89f7dab7179d |
| final-profile | 16.978 | 863.798 | 25.729 | 19.808 | 926.313 | 57.908 | a5ed9d1d3a9a |
| final-profile-repeat | 18.764 | 886.827 | 27.596 | 18.838 | 952.025 | 58.023 | a5ed9d1d3a9a |
| final-v2-profile | 17.530 | 662.324 | 23.037 | 18.415 | 721.306 | 49.918 | 1ab5815a07e7 |
| final-v3-profile | 16.477 | 664.773 | 21.877 | 16.907 | 720.034 | 48.806 | fe60148056c4 |
| final-v4-profile | 16.346 | 707.435 | 24.955 | 16.656 | 765.392 | 53.510 | b48d791a22a5 |
| final-v4-profile-repeat | 16.194 | 684.747 | 21.339 | 17.350 | 739.630 | 56.928 | b48d791a22a5 |
| Main-baseline | 57.190 | 3645.865 | 178.050 | 45.231 | 3926.336 | 305.517 | b3615cd718ee |
| Main-baseline-repeat | 59.806 | 3438.841 | 182.512 | 46.206 | 3727.365 | 300.290 | b3615cd718ee |
| Main-final | 54.997 | 3444.866 | 192.372 | 49.440 | 3741.675 | 291.581 | 1033a0bad707 |
| Main-final-v4 | 62.716 | 3912.673 | 242.047 | 51.454 | 4268.890 | 302.744 | fd6a8317ac24 |
| Main-final-v4-repeat | 51.668 | 3898.399 | 203.276 | 45.595 | 4198.938 | 285.384 | fd6a8317ac24 |
| Main-adapter-candidate | 53.669 | 3623.784 | 201.356 | 49.632 | 3928.441 | 298.839 | eb0b8498f0b0 |
| Main-final-v5 | 53.385 | 1293.410 | 30.116 | 53.648 | 1430.559 | 178.729 | 636eb6994e09 |
| Main-final-v5-repeat | 61.370 | 1311.197 | 32.022 | 54.818 | 1459.407 | 172.913 | 636eb6994e09 |

Version chronology: old33/30-line target; V1 14-line positive-input continuity proof; V2 15-line direct numeric API (still positive/strict inner interval); V3 15-line closed interval with old first doc sentence; V4 exact final closed-interval doc/source. Both V4 samples share identical b48d791a… prefix and37ac02db… full MainLemma source. The direct closed-interval V4 caller pair shares fd6a8317… prefix. The final V5 caller pair shares636eb699… exact prefix, with actual final MainLemma imported after rebuild and the authorized one-line linear-premise restriction. The changed-context pair and adapter control remain preserved, never relabeled as final V5. Earlier14-line passing samples were not mislabeled as final. V4's first765ms mandated repeat; unchanged repeat739ms passes without a third unchanged cherry-picked run.

Initial scheduling failure is retained in invalid-profiles.json: first process session was lost, duplicate launched then interrupted exit130, both excluded as uncontended baseline evidence. Exact owned ps/drain evidence confirmed original process absent; idle unrelated LSP workers were not killed. Original invalid trace remains intact (policy-root total1566.703ms; historical overbroad parser1568.866ms also retained). baseline-invalid-policy-target-timing.json explicitly marks invalid scheduling. Fresh valid original samples were captured after drain, before any source/API edit. No failed/overbudget sample was erased.

All compiler source failures and unsuccessful alternatives remain in separate sources/logs. None are positive gates. All successful candidate, final-source and caller samples are separately identified.

### Causal caller comparison and bounded repair

Final repaired caller pair: 1430.559 / 1459.407ms; both below both original caller samples 3926.336 / 3727.365ms. The observed changed-context slowdown is addressed by the premise-restricted linear proof; remaining >1000ms work stays in the separate Main queue.

Both direct closed-contract caller samples4268.890/4198.938ms exceeded both original samples3926.336/3727.365ms. The exact two call steps total6.572/6.671ms, overlapping original4.724/8.496ms; direct call elaboration is not the source of the material increase. The unchanged terminal nlinarith grows2305.445/2251.750→2588.150/2567.828ms, with broad preprocessing increases. caller-hotspot-comparison.json records all sample anchors; it does not add nested tactic times into target totals.

A separate immutable scratch control replaces the closed local forall with its original positive/strict type, clearing the former hypothesis. It compiles and profiles3928.441ms, near the high original timing. This supports sensitivity to the changed local context but does not completely eliminate host variance. No third unchanged direct-source sample was cherry-picked. The3-line control adapter was not inserted live.

The owner/coordinator authorized one narrow context-insulation repair: terminal linarith only [a1,a2,a3]. Both nlinarith-only and cheaper linarith-only candidates compiled in the actual same rewritten proof context. Summing a1,a2,a3 divided by3 is algebraically exactly the target, so no nonlinear extras or unrelated hypotheses are needed. Only this one arithmetic line was changed beyond the two exact API call repairs; no global helper, broader Main cleanup, public Main type change or Main original audit/count credit. After rebuilding, the full independent original Main proof/type and actual new opaque Main body/standard axioms are rechecked by final-v5-semantic-check. The final source-level linear step measures135.269/137.523ms versus2251.750–2588.150ms for the preserved terminal nonlinear samples (final-caller-linear-step.json and caller-hotspot-comparison-v5.json contain raw anchors). The final V5 caller pair is reported above; all failed/intermediate/control sources and raw samples remain available.

### Simplify pass — scoped manual equivalent

Outcome: ISSUES-FOUND-AND-FIXED. Callable simplify skill unavailable, honestly recorded rather than claiming invocation. Identified broad numeric search, single-use square identity, and unnecessarily strict inner endpoints. Applied direct sqrt API, inlined square identity and zero-value calculation, and used fun_prop's documented [eta] unfolding argument with half radius. Files modified: Roth/MainLemma.lean, exact two dependent calls in Roth/Main.lean, and the authorized single final arithmetic line in that same caller. The full Main audit remains separate and receives no count credit. All final source/type/axiom/native/build gates rerun after changes.

## Step 6 — worker result and all eleven checks

Result: Roth.exists_delta_bound. Before: 33 declaration/30 proof lines; after: 17 declaration/15 proof lines; saved: 16/15. Audit issues found5, fixed5, deferred0 in this original: headline length, performance, unnecessary hn, unnecessary lower/upper strictness. Import and exact caller repairs are consequences. Rules applied:1.4,1.6,1.10,1.11,1.12,1.13,1.16,1.17,2.3,2.4,2.5,2.6,2.9,3.2; every other rule has explicit applicability/status above. Gates:pass for this scoped original, with explicitly authorized stronger public API and mandatory correlated existential preserved. Caller budget status is reported from the actual final V5 pair; any remaining existing Main work is explicitly queued, never hidden as a target pass.

Renames queued:none; existing Index/B₁/other rename queue entries untouched. Comments preserved:no proof-body comments existed; historical source quotation and all neighboring declarations/comments preserved, only unquoted public interval description updated for stronger theorem. Refactoring needed in this original:none. New helper history:none, including temporary insertion/removal; no fresh helper auditor needed and no count added to original 264.

Phase checklist:

- [✓] Step1 — full required reference documents read.
- [✓] Step2 — all 24 audit items and exhaustive have scan recorded.
- [✓] Step2.5 — all 5 actual search methods, true pretarget exact?/apply? and verified API status recorded.
- [✓] Step2.6 — every outer/inner binder, drop/weakening/inversion,2.6a–e, public literature and actual endpoint/boundary controls recorded.
- [✓] Step2.7 — measured line-packing width/arithmetic table recorded.
- [✓] Step2.8 — explicit zero-reversed-inequality scan recorded.
- [✓] Step3 — all 42 golfing-rule statuses recorded.
- [✓] Step4 — holistic review/simplify-equivalent completed with tool availability stated.
- [✓] Step5a — complete unfiltered native diagnostics on both final edited files success=true, partial=false, timed_out=false, failed_dependencies=[],0errors.
- [✓] Step5b — all diff gates, original proofs/types, actual opaque bodies/standard axioms, all affected/full project builds and final measured profiles recorded.
- [✓] Step6a — no warranted rename; existing sidecar untouched.

## Freeze and ownership handoff

Final MainLemma SHA256:37ac02db4702d7c91a21f66ee1f7f22bdf8b6c6c23e3ab740cc7d1a9c679fefc.
Final Main SHA256:77379716d68354eef40ba1ae8c10c89f91dcffcc5ec4cfcee33655319e15a137.
Final exact target declaration SHA256:20b24004bca52f97241a82e72c6c54c4f91885f76b5447f48ffe6349b75068c4.
Final MainLemma prefix SHA256:b48d791a22a5b5eb6cc87464796ef8366b2646d7259db624b9b4b5dd130056d9.
Final Main prefix SHA256:636eb6994e09983505bb66991904f943508f6d41c3c2cb8d731cad51c6c31721.

All raw artifacts/sources/commands/hashes/anchors: /private/tmp/roth-mainlemma-delta. immutable-final-manifest.json enumerates every artifact SHA256/byte size/mode and report hash. source-protection-v5.json and semantic-byte-recovery-v4.json record exact full-file scope and both immutable independent old-proof recoveries. Failed/intermediate snapshots are retained, never overwritten by later passing sources.

This is a scoped worker result, not file/checkpoint/project completion or count update. Owner still performs independent review/full build, separate Eval, commit and push before next original. No Git operations or central shared progress writes performed. Final exact-owned-process ps check is empty, all native calls completed, all bounded compiler/profile runners have drained (final-owned-process-drain.json). Idle LSP workers were not modified. Source/compiler/native lease released with the final parent handoff after this freeze.
