# Original22 — Roth.eval_hasseDeriv_sub_eq_zero

Mode B, scoped original22. Branch ramin-cleanup. Sole worker; no children, Git actions, central ledger/queue edits, or other declaration edits. Parent independently reviews/builds/publishes before original23. This is not a claim that all27 originals or the global main budget have passed.

Entry MainLemma source699 SHA78693d6e1c2fe5520fda8825a55224aac0e74ececaa3485fd597a82bd71c9ae0. Selected699 SHAe3c8e950614bc5701b2c82691e7faac9513ff7692c9051da80911a85fc42e37f. Only attached target doc and target declaration changed. Every byte outside this interval, all five audited helpers, all32 retained written declarations, Main, B₁/pre-count context, paper quotation, and nine literal signpost lines grouped into seven blocks are preserved. Main SHA5f384557dccacaec469699cc7d32bd5666c9d525267e00433b7ae401fee98d09.

## Full audit (items1–24)

1. LINT: target no warnings; complete canonical MainLemma/Main/LeanEval native warnings match baseline1/4/0. No target admission or failed dependency.
2. HAVE SCAN: entry hdvd/h1 blocks and single-use h2/h0 inspected. Replace hand-built remainder witness with dvd_modByMonic_iff_dvd and aeval_eq_zero_of_dvd_aeval_eq_zero. Final only hdvd, used once to isolate the mathematical divisibility step; its two-tactic proof closes directly. No disposable bookkeeping remains.
3. SET_OPTION: none in production. Actual effective defaults200000/20000/512 checked in kernel harnesses; no raises.
4. SIMP SQUEEZE: final hdvd `simp [map_sub, diag_sub, Polynomial.sub_modByMonic, h]` closes its goal. Final `simpa` transports the established evaluation fact. Candidate v3 `simpa only` compiled; unsqueezed v4/v5 compiled with deliberate stable explicit normalization. Neither nonterminal bare simp nor decorative `only`.
5. NAMING: eval_hasseDeriv_sub_eq_zero names evaluation, canonical hasseDeriv API and subtraction vanishing. No forbidden abbreviation, number scheme, single-letter public name, _ge_/_gt_ or numeric_aux. No rename justified/queued.
6. LINE PACKING: all four actual final signature lines measured in table below. No complete next binder fits100.
7. BY PLACEMENT: both := by occur at ends of their lines.
8. FORMAT: two-space tactic indentation, four-space continuations, no blank proof line, haveI/letI, semicolon chains or repeated rw; mapsto lambda syntax used.
9. COMMENTS: no inline target proof comments existed; none removed. Exact attached paper quotation and all outside comments/signposts preserved.
10. DOCSTRING: existing summary and paper quote retained; one sentence states arbitrary variables/commutative target ring, adding application scope beyond old finite-real type.
11. VISIBILITY: public mathematical root/remainder interface, sole direct project consumer main_lemma. Public API remains reusable for arbitrary variables/rings; hiding would discard verified generality.
12. STRUCTURE: final proof6 lines, hdvd branch2, ordinary limit30/branch10; target is not headline15. No conjunction or decomposition needed. Initial audit's proof9 estimate was mistaken: actual entry proof7/declaration11; selected proof6/declaration10.
13. MATHLIB: five actual searches below, existing divisibility/root and hom-composition APIs used, no duplicated helper. No global decidability instance/coset anti-pattern.
14. JUNK DEF: n/a theorem, no definition added/changed.
15. EXISTS LEMMA: n/a no existential witness helper.
16. SHOW vs CHANGE: n/a no show in selected proof.
17. PUSH_NEG: n/a none.
18. GENERALISE: verified Fin m→arbitrary σ and ℝ→independent CommRing S, detailed full mechanical audit below. Integer coefficient API retained. Exact entry and project-original finite-real contracts independently recovered.
19. INEQUALITY: zero occurrences ≥/> in signature, every hypothesis, conclusion and inner premises; table below.
20. NORMAL FORM: canonical equality-to-zero on evaluation of mapped Hasse derivative of subtraction; divisibility is a local bridge rather than a competing public equivalence API.
21. SYNTAX-GEN: root hypothesis then remainder hypothesis remain explicit in same order; σ/S/j/polynomials infer from call. Existing main call compiles byte unchanged. No bundled witness burden introduced.
22. IMPORT-FANOUT: n/a no import changes; all APIs already imported.
23. CASTS:0 dropped /1 genuine cross-type integer coefficient transport kept (`Int.castRingHom S`) /0 new load-bearing ascriptions. `algebraMap_int_eq` identifies the existing transport, not a redundant cast.
24. INSTANCE-NAME: anonymous [CommRing S]; no named/global instance added.

Issues found5, fixed5: finite-variable restriction, real-only restriction, remainder witness bookkeeping, single-use evaluation bookkeeping, lambda/doc scope and packing treated as one presentation issue. Refactoring needed:none. No written helper introduced; generated compiler siblings do not start a helper lifecycle.

## Mathlib search-status (all five actual methods)

Actual responses: search22-finder.json, search22-loogle.json, search22-leansearch.json, search22-local.json, search22-references.json. Finder's evaluation/root/remainder query returns aeval_modByMonic_eq_self_of_root (requires monicity), eval₂ equivalent and modByMonic_eq_of_dvd_sub/IsAdjoinRootMonic interfaces. Loogle `Polynomial.aeval, _ ∣ _, _ = 0` and LeanSearch natural-language equal-remainder/root query return the used aeval_eq_zero_of_dvd_aeval_eq_zero. Local index returned relevant names with index:error; this is not an absence certificate. Actual source rg validates Div.lean264/269 and AlgebraMap511 plus MvPolynomial Eval608–614/432 (comp_aeval_apply/eval_map). References reports exactly declaration and main call (total2); imported full TYPE+opaqueVALUE environment scans independently confirm sole direct consumer main_lemma.

Partial mathlib matches were composed directly. No assertion that a monolithic mathlib theorem is absent or that searches establish mathematical optimality. Dependency-only exact?/apply? actual probes do not close this full goal. No new thin helper.

## Generalisation2.6a: every outer binder and every inner premise

Actual12 whole-file mechanical drop/parent tests: drops22-all.lean, drops22-actual-summary.json. autoImplicit false, all other premises retained. Tested same selected signature with v4 proof before final one-line hdvd golf. Whole exit1, every candidate actual error; these are proof/type dependence tests, not by themselves proofs of logical necessity.

| Outer binder | Drop/weakening actual result | Disposition |
|---|---|---|
| σ : Type* | dropping gives unknown σ; original Fin m proof compiled at arbitrary σ | keep arbitrary independent universe, no finite/enumeration assumption |
| S : Type* | dropping gives unknown S | keep independent universe, ℝ restriction removed |
| [CommRing S] | dropping fails required operations/classes; Ring and CommSemiring replacements actually fail required CommRing/NonAssocRing syntheses | keep current API minimum verified, no maximality claim |
| f : Polynomial ℤ | dropping gives unknown f | coefficient ring ℤ retained to use unchanged project diag API |
| α : S | dropping gives unknown α | keep general target value |
| hfα : aeval α f = 0 | removing yields unknown hfα in actual proof; independent complete countercertificate shows false conclusion with all remaining premises | necessary root condition |
| W′ | dropping gives unknown W′ | arbitrary variable-index integer polynomial |
| W″ | dropping gives unknown W″ | arbitrary variable-index integer polynomial |
| j : σ →₀ ℕ | dropping gives unknown j | finite-support multi-index is actual Hasse API, no variable finiteness |
| h : equal remainders | removing yields unknown h in actual proof; complete independent countercertificate retains root/all other premises | necessary congruence condition |

Every outer hypothesis is covered: CommRing is an anonymous structure instance, hfα/h are equalities with no forall/implication/ordered inner hypotheses. σ/S/f/α/W′/W″/j are data binders and have zero inner logical premises. There is no hidden Fintype, Nontrivial, domain, monicity, or characteristic hypothesis. Full elaborated TYPE binder names/order/BI and universe parameters were independently checked.

2.6b candidate verification: generic original proof compiles for arbitrary σ (generic22-original-proof). Selected generic proof compiles for independent σ/S universes; isolated v1/v2 failed normalization attempts retained and not credited. Two premise countercertificates and ten properties pass in properties22-v4, complete closed TYPE+actual opaqueVALUE, inferred TYPE/std3/default checks.

Ten properties: root-premise necessary (f=X, α=1, W′=X₀, W″=0,j=0 overℤ); remainder-premise necessary (f=X,α=0,W′=1,W″=0); zero divisor-polynomial f=0 boundary; equal polynomials; nonmonic constant2 over ZMod2; nonzero nilpotent2 over ZMod4 with f=X²; Empty variables; ULift.{1}Nat versus ℤ independent universes; infinite Nat variables with j=single1372/W′=X₁₃₇³; trivial ring ZMod1. “zero_divisor_boundary” names f=0, not a claim that all zero-divisor rings are represented by that one property. ZMod4 supplies the actual ring zero-divisor example. Small kernel decide only, no native_decide.

2.6c big-change candidates: none newly deferred. Coefficient-ring generalization would require reopening unchanged CoeffNorm.diag and outside API; dependency search confirms its integer source. This task adopts both beneficial independently verified local widenings under standing user authorization. No unasked full27 audit.

2.6d public literature — three actual separate queries, ordered Top3 preserved even duplicates/weak matches:

1. `Hasse derivative polynomial arbitrary commutative ring diagonal evaluation`: [mathlib3 Hasse docs](https://leanprover-community.github.io/mathlib_docs/data/polynomial/hasse_deriv.html), [PlanetMath](https://planetmath.org/derivativeofpolynomial), [ACM paper](https://doi.org/10.1145/3652025). Primary Hasse material supports commutative-ring setting; no theorem equivalence claimed.
2. `Hasse Schmidt derivations polynomial ring arbitrary commutative ring generalization`: [thesis bitstream](https://idus.us.es/bitstreams/24b8adfd-de4a-476b-8704-2c4743678f54/download), [same thesis API](https://idus.us.es/server/api/core/bitstreams/24b8adfd-de4a-476b-8704-2c4743678f54/content), [Journal of Algebra paper](https://doi.org/10.1016/j.jalgebra.2025.10.039). Arbitrary-variable/commutative-ring setting corroborates the selected scope, not a proof or exact optimality certificate.
3. `polynomial evaluation universal property kernel ideal root factor theorem commutative ring`: [Androma](https://androma.org/theorems/17387), [Wikipedia](https://en.wikipedia.org/wiki/Polynomial_ring), [Scribd](https://www.scribd.com/document/927671343/Anneaux-Corps-Commutatifs). Search leads only; kernel validation supplies mathematical evidence. Optional ChatGPT math tool unavailable, no fabricated invocation. Exact query args/full raw responses in literature22-query1/2/3.json.

2.6e small-safe results applied: arbitrary σ and CommRing S, all original uses unchanged and old finite-real statements independently recovered. No extra hypothesis or weakened conclusion.

## Line packing — full signature

| Line | Codepoints | Complete next token | Next width | Current+1+next | Action |
|---|---:|---|---:|---:|---|
|445|99|hfα binder|32|132|retain break, exceeds100|
|446|77|h binder|64|142|retain break, exceeds100|
|447|70|complete conclusion/`:= by`|78|149|retain break, exceeds100|
|448|82|none|—|—|final line|

Actual complete text/token strings in packing22-final.json, not a first-line-only estimate.

## Inequality scan

| Scope | ≥ | > | Occurrences/actions |
|---|---:|---:|---|
| data/typeclass binders σ,S,CommRing,f,α,W′,W″,j |0|0|n/a no ordered relation|
| root hypothesis hfα |0|0|equality only, zero inner premises|
| remainder hypothesis h |0|0|equality only, zero inner premises|
| conclusion |0|0|equality to zero|
| proof-local hdvd and proof body |0|0|divisibility, no orientation repair|

## Golfing — all42 rules

| Rule | Status |
|---|---|
|1.1|n/a no by-exact wrapper|
|1.2|n/a no by-rfl wrapper|
|1.3|rw+exact: entry final rwa chain replaced by direct terminal simpa; no remaining rw+exact pair|
|1.4|applied final simpa transport|
|1.5|n/a no trailing rfl after simp|
|1.6|n/a no conjunction constructor|
|1.7|apply+exact: n/a final apply exposes a simp obligation rather than exact; no pair to collapse|
|1.8|n/a no by_contra/push_neg pair|
|1.9|constant evaluation lambda is mathematically needed, no eta reduction|
|1.10|applied remove h2/h0, replace h1 witness block with existing divisibility API|
|1.11|n/a no apply+intro chain|
|1.12|n/a no redundant show|
|1.13|n/a no have followed by projection .1/.2|
|1.14|n/a no consecutive rw pair|
|1.15|v3 simpa-only then v4/v5 explicit unsqueezed simpa actually verified|
|1.16|both simp/simpa terminal; no nonterminal bare simp|
|1.17|dot notation: `.mp` applies the existing iff directly; namespaced API arguments remain clear|
|1.18|n/a no gratuitous function proof-argument parentheses|
|1.19|n/a no push_neg|
|1.20|n/a no trivial single-use existential lemma|
|2.1|actual isolated grind failed, no admission credited|
|2.2|no grind source or conversion remaining|
|2.3|applied selected terminal simpa|
|2.4|n/a no continuity/differentiability goal for fun_prop|
|2.5|n/a no ordered goal|
|2.6|n/a no inequality/gcongr goal|
|2.7|n/a no Nat arithmetic goal|
|2.8|actual isolated aesop exhaustive failure|
|2.9|genuine Int coefficient transport retained, no redundant cast|
|2.10|generic ring proof requires no decidable equality automation|
|2.11|n/a no denominators|
|2.12|n/a no linear-combination relation goal|
|2.13|n/a no symmetric case analysis for wlog|
|2.14|n/a no calc chain|
|2.15|n/a no duplicate independent goals|
|3.1|n/a no erw|
|3.2|n/a no legacy function property tactic|
|3.3|n/a no omega|
|3.4|n/a no rcases rfl pattern|
|3.5|explicit library normalization set, no new attributes/normal-form API|
|3.6|n/a no simp_all only|
|3.7|no limit raise, default positive limits independently verified|

All five actual isolated proof-search probes (grind,simp,aesop,exact?,apply?) depend only on Roth.Lattice/Theta and Div, not selected target or an earlier failed proof. First four fail; apply? returns inadmissible partial proofs rejected by the closed-value guard and proposed limit0 was ignored. Whole runs and post-proof closed-value guards prevent an admitted snippet counting as success. automation22-actual-five-summary.json preserves actual outcomes.

## Step back, independent evidence and timings

The useful mathematical decomposition is equal remainders→divisibility→evaluation at a root. Existing hom-composition APIs permit the broader variable/ring setting without a helper. Final proof6 lines is readable and below limits; preserve this rather than hiding the core content in a new wrapper. Built-in /simplify is unavailable in this session; equivalent scoped manual holistic review completed, not claimed as an invoked tool. Owner's final whole-file simplification after27 remains separate.

final22-independent.lean clones the ENTIRE immutable project-original704, entry699, selected699 namespace bodies, plus legacy adapters/H5 contracts. Actual immutable source SHA and exact full payload copies retained.28 full contracts,70 closed TYPE+actual opaqueVALUE/inferred TYPE/std3 checks,6 full target/main non-self dependency closures,4 dynamic literal-pair pregates/eight actual references. Narrow named unchanged DATA normalization only, β at DATA origins only. No arbitrary NameMap, proof irrelevance, arbitrary unfold, target/current-helper fallback, unrelated Entry dependency or discarded opaque value. Old/current literal sharing allowed only AFTER exact TYPE+opaqueVALUE AST/axioms/universe/binder checks. Old main TYPE→old gam VALUE→prevalidated literal closure explicitly checked. Whole exit0 at defaults. Parent independently reviewed the complete actual guard/source clones.

Actual before/after profiles precede/follow edits, use identical CLI/pinned inputs and frozen actual parent environment, repeat captured before edits. Full printed command (including every proof operand) is bound to immutable canonical source; layout whitespace and omitted standalone comments are the only comparison normalization. Every disjoint command/proof/kernel/lint root is included; internal Meta roots excluded. No forced root count.

| Scope | Before1 | After1 | Before2 | After2 |
|---|---:|---:|---:|---:|
| target ms |138.752|379.299|129.650|343.294|
| sole complete consumer main ms |4907.788|5254.537|5019.497|4981.138|

Target root count4→6, because actual compiler-generated theorem siblings `Roth.eval_hasseDeriv_sub_eq_zero._simp_1_1` and `._simp_1_2` are additional disjoint kernel roots. All six retained numerically, qualified actual names/kinds/closed TYPE+opaqueVALUE/inferred TYPE/std3 verified, source absence verified. Main retains9 roots with existing _proof_1_1…1_5. Old verifier incorrectly allowed only _proof_ names, v2 then incorrectly allowed only one-index _proof_; both rejected assumptions preserved, v3 accepts exact observed generator name forms and validates every actual complete payload. These compiler declarations are not new written helpers.

Target is slower by240.547/213.644ms but both samples remain below1000ms. Changed main hγ application rises13.976→40.647 and13.396→38.484ms (consistent ~26ms elaboration overhead). Whole main pair rises346.749ms then falls38.359ms. All matched stage/root deltas retained in main-stages22-diagnostics.json; nested inclusive steps never summed into outer roots. Residual movement cannot be causally isolated from four samples. No dismissal as environmental noise, no third sample/cherry-pick, no unasked full27 audit. Main's preexisting~5s budget failure remains original27/global work, not falsely marked passed here.

## Reproducibility, boundaries and honest failures

17 fresh source/config pins and104 actual project-cache companions copied before and after, plus END. Actual dynamic package/setup importArts availability union12201 and full pinned core availability superset12592; union24793, exact project-cache intersection11, strict external24782/3918200888bytes. These are availability/superset scopes, never claimed exact loaded closure. Fresh before/final/END exact external path/hash equality, package/core options/plugins/dynlibs, four executable/proxy resolutions/hashes, raw env and all actual CLI argv/timestamps/raw output hashes retained. UTF8 strict for source/text; binary exceptions only after actual decoding failure for actual compiled bytes. All eight actual profile pre/post lake environments are byte-identical699b2849d67d2223b43be5ab7a11f9480125e01eb1fefc054bfa5242528d795e under actual frozen parent. END independently recaptures that actual environment. Free inherited env observations remain unnormalized, including any MANPATH variation.

Every launched Lean input copied by actual hash at launch. Interim v4 source700 SHA6dc9... was a transient pin during experiments only, not a project API/performance sample; exact historical bytes recovered later by inverse final golf and checked against its captured full SHA, explicitly labeled later recovery. No backdated capture. Initial profile CLI option misplacement rejected before compiler launch. Final read-only ps inventory attempt was sandbox-denied; fresh os.killpg(pgid,0) checks are the actual drain evidence. Supplemental generated-main22.lean is an unlaunched inspection draft and receives no gate credit. Scratch native drop-test path rejected for no lean-toolchain ancestor, so actual complete CLI supplied that evidence; canonical native remains mandatory/pass. Drop-error parser regex corrected for actual diagnostic codes. Properties v1–v3 and candidates v1/v2 failed complete runs preserved, not credited; properties v4 and selected v5 complete passes. First final toolchain catalog had stale phase wording; original artifact preserved with erratum, corrected fresh recapture used. Required reference read truncations recovered. Initial proof-length estimate corrected above. Large raw AST/tool output truncation is not a discarded raw file: complete raw files/hash retained. No sorry/new axioms/admitted proof/limit raise or pin update introduced.

Final checks and END status are emitted below only after actual serialized full build, separate LeanEval build, complete native calls and fresh closure/drain verification.

## Gate status — Roth.eval_hasseDeriv_sub_eq_zero (Phase4)

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | ✓ pass | selected22-affected `lake build Roth.MainLemma Roth.Main` exit0; final22-full exit0, then separate final22-Eval exit0 |
| definition_protected | ✓ pass | no def/abbrev/instance or helper edit; exact outside-target byte identity |
| theorem_statement_protected | ✓ pass | authorized verified item18 generalization; both old finite-real contracts independently recovered and selected full generic contract verified; explicit premise order unchanged |
| structure_gate | ✓ pass | proof6≤30, branch2≤10, no conjunction, not a headline15 theorem |
| naming_gate | ✓ pass | descriptive mathematical name, no forbidden pattern, no rename required |
| line_packing_gate | ✓ pass | four-line actual width table;132/142/149>100, final82 |
| inequality_orientation_gate | ✓ pass | every outer/inner premise and conclusion audited, zero ≥/> |

Overall: pass (original22 scope). Main's original27/global~5s timing failure remains open; no global pass claim.

## Result: Roth.eval_hasseDeriv_sub_eq_zero (Step6b)

Before:11 declaration /7 proof lines. After:10 declaration /6 proof lines. Saved:1 declaration and1 proof line; doc+1 keeps file699.
Audit issues found:5. Fixed:5. Refactoring deferred:0.
Rules applied:1.3/1.4/1.10/1.15/1.17/2.3 plus verified item18 generalizations and presentation packing/mapsto.
Gates:pass (all seven explicit rows above).
Renames-queued:none; parent-owned rename queue untouched (entry SHA2be6064f493c70e58303375e24ea0d93fb43cf11788b046c5265d791c6200179).
Comments-preserved:none present in target proof; attached quotation and all9 outside narrative lines/7blocks byte exact,0 relocated/removed.
Refactoring needed:none in scope. Parent retains central counters/Phase5/whole-file final review and original27/global issue.

Phase checklist:
- [✓] Step1 — both skills, required commands/full references, dispatch and profiling amendments read, truncations recovered.
- [✓] Step2 — all24 audit items concretely reported.
- [✓] Step2.5 — all five actual search responses and honest partial matches reported.
- [✓] Step2.6 — outer/inner mechanical2.6a–e, all12 drops, verified candidates, premise counters and three actual literature queries/ordered Top3 reported.
- [✓] Step2.7 — all four signature rows measured.
- [✓] Step2.8 — per-scope full inequality table, zero occurrences.
- [✓] Step3 — all42 statuses plus five actual isolated automation outcomes.
- [✓] Step4 — scoped holistic reflection and useful interface/decomposition reviewed.
- [✓] Step5a — actual final FULL unfiltered MainLemma/Main/LeanEval native diagnostics complete, nonpartial/nontimeout/success; zero errors/failed dependencies; baseline warning objects exactly1/4/0; actual request args/timestamps/per-call17pins retained.
- [✓] Step5b — all seven explicit diff gates and Overall:pass.
- [✓] Step6a — no rename needed; parent-owned sidecar unchanged.

Final source/config/cache/external/executable/environment closure checks complete. Full build precedes separate LeanEval build and then all three native checks. All actual CLI groups freshly absent; no compiler/native/profile pending. Immutable artifact manifest and END22 record in scratch certify all saved bytes and lease release. No third timing sample, no unasked publication/Git action.
