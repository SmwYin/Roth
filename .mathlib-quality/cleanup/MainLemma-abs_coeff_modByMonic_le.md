# Roth.abs_coeff_modByMonic_le — original11 final worker report

The coefficient remainder estimate is now valid over every `SeminormedRing R`, with norms and without separate monicity or nonnegative-bound hypotheses. The exact old integer contract and all old written caller contracts are independently recovered. This is worker completion for owner review; publication, tally increment and filewide/projectwide gates remain with the owner.

Entry HEAD supplied by owner: `2b17ecab7f33143baaf138827654b1b5dad7fc8d`. Entry MainLemma SHA `8a90958369a5f7fc9357169270737fb0c6473b1d4fd8d2d3a8d6defd95119791`. Final MainLemma SHA `c1a4c252c37d2f2eb7399a556aaf67adab471fd44da859607d178c64877e5735`,706 lines. Main remains byte-identical SHA `5f384557dccacaec469699cc7d32bd5666c9d525267e00433b7ae401fee98d09`.

Artifact directory: `/private/tmp/roth-mainlemma-abs-coeff`. Paths below are relative to that directory unless marked otherwise. The complete audit24, generalization2.6a–e/effective binders, five actual searches and golf42 status block are included below, not credited from another worker.

## Mathematical change and protected scope

The natural truncated exponent `s + 1 - f.natDegree`, arbitrary degree cap and every degenerate case are preserved. `A ≥ 0` and `C ≥ 0` follow from the coefficient bounds at0. Nonmonic `modByMonic` returns the dividend, so monicity is unnecessary; the self-remainder branch covers it. Separation and commutativity are also unnecessary: actual zero-seminorm and Quaternion applications compile. No Nontrivial/NormOneClass/decidability assumption is added.

The one substantive private helper returns a lower-degree dividend, coefficient-growth bound, remainder equality, and divisor-degree facts needed for natural subtraction. It uses `Polynomial.div_wf_lemma`, pinned `divModByMonicAux` recursion in the actual multiplication order, triangle inequality and submultiplicativity. Nontriviality and monicity are derived inside the non-self case. The public induction uses direct ordered-addition facts for signs, removing two trace-diagnosed sign-only linarith calls.

Public proof15 lines, longest induction branch10; helper27 lines, longest branch8. Combined42 proof lines versus original58. Public declaration18 lines versus original62. Mainresult module-doc bullet now describes the seminormed-ring norm formulation; the historical source quote is exact. No proof comments existed in this target. `final11-v2-source-protection.json` and `final11-v2-source.patch` verify byte protection outside target/doc/module bullet/audited helper/exact sole caller application. All other16 source/config pins match entry. No production import or option was added; no limits raised, admissions, new axioms or weakened conclusion.

Actual references are only module-doc bullet, declaration and one call inside `Roth.main_lemma`. The caller applies the generic result using terminal `simpa [Int.norm_eq_abs]` bounds, then `rw [Int.norm_eq_abs] at hrem`. Main is transitive affected build/native/semantic scope, not a claimed direct performance consumer. No broad foreign Main cleanup or foreign audit credit.

## Independent helper lifecycle

The original worker saved genuine immutable FIRSTDRAFT/fullcontext/options/dependency pins before golfing, released all leases and ended. The owner dispatched a fresh full helper auditor and resumed this same original11 only after release and owner acceptance. One helper is introduced, no speculative second helper count.

Fresh report: `.mathlib-quality/cleanup/MainLemma-exists_norm_coeff_reduction_aux-helper.md`, SHA `87dd48377334fbf109ad0e4b207b7bc06762d9cec8cb00d34515ce7f67c720cb`. Helper artifact manifest `/private/tmp/roth-mainlemma-norm-reduction/artifact-manifest.json`, SHA `abd81dd60f24e980f2f3b4aa56d8b965ea84776473f16927e490b47e32e7cb1e`. Owner evidence/profile reviews accepted. Exact final helper declaration bytes SHA `8036cf617651d096e302d8f52d4589051c5a213d2ef93c10ee5813de73956a44` remains unchanged through final source edits and is checked in final source protection.

The genuine firstdraft used NormedCommRing+Nontrivial and a smaller existential conclusion; its historical enclosing draft was not accepted as compiling. The fresh auditor independently compiled its exact extracted proof and actual-value guard. Full firstdraft/current expected/helper projection contracts, effective assumptions, automation/drop/counterexamples, profiles and standard axioms were audited independently. Helper heartbeat improvement2782→2085 and public5374→5386 tiny increase are historical bounded custom-counter figures on helper-audit source `05967520b94e30cefb4984a9f29cbe418e17c71db1e4c93c647f23a27e737382`, whose public proof predates the final direct-order change; these are NOT V2/final heartbeat counts; no built-in max0 measurement is accepted or repeated. Final original11 timing uses fresh whole target+helper combined captures below.

Correction: the original partial release narrative said9 PGIDs, but `partial11-drain-release.json` actually lists11; owner confirmed all11 absent. The helper's35 groups were separately drained. The final release lists actual original11 groups without relying on that mistaken narrative.

## Final semantic and native evidence

`final11-v2-affected-build` is a fresh `lake build Roth.MainLemma Roth.Main`, exit0 in92.090s. Final source was frozen after all code/doc/helper edits. `final11-v2-independent` freshly compiles the exact semantic script SHA `d2d27f4c87ff7bb743966e3d281b4a058de9046ff5f528f2034bc3253cfd03d2`, exit0 in55.043s against the V2 built imports. The earlier owner code review is reused only for those exact script bytes; actual values/pins are freshly checked.

The script independently re-elaborates the ENTIRE PROJECT-original target proof, entire entry MainLemma source, and entire old Main source with explicit old dependency migration. It checks five exact full-contract pairs: independently designed expected-new/current target; PROJECT-original/old Int adapter; entry-original/old Int adapter; entire old/current `Roth.main_lemma`; entire old/current `Roth.roth_of_isIntegral`. Raw full TYPE ASTs, all written binder names/order/BinderInfo/universes and explicit data migrations are retained. Only generated macro scopes normalize. Each actual opaque VALUE!true and TYPE is closed, without expression/universe metavariables, free/loose variables or sorryAx; inferred value types are definitionally equal and axioms restricted to propext/Classical.choice/Quot.sound. The imported actual private helper receives the same guards.

The independent old value dependency closures exclude actual current target/helper/main callers (365/365/2540/2718 constants). This is not specialization-only elaboration or a proof reusing the new target. `expected11-independent-contract-origin.json` verifies the expected-new signature matches the immutable independently designed v7 contract modulo whitespace. Honest unused old hf/hA/hC adapter and historical Main hδ/hQ/hc warnings remain in the raw log.

`original11-v2-boundaries` freshly compiles12 guarded certificates against V2 imports, exit0 in50.234s,0warnings: divisor0, dividend0, divisor1, nonmonic constant2, cap0, impossibility of dropping hfA/hP/hs, pointwise-only hP insufficiency, Quaternion noncommutativity and actual theorem application, nontrivialℤ with zero induced seminorm actual application. All certificate TYPE/actual VALUE/inferred type/standard axioms are checked. The failed initial boundary normalization fixture is retained and never credited; V2 repairs rewrite the remainder before norm_num.

`original11-automation-drop` is actual standalone generic target automation under minimal imports and the audited helper, without importing the current target. rfl/simp/ring/linarith/nlinarith/omega/exact?/grind/aesop fail. apply? apparent zero-goal closure is REJECTED by actual open/sorry VALUE guard, state restored, then the complete fallback passes. Mechanical clear+proof probes use the actual nonhygienic local binder IDs; remaining hfA/hP/hs replay fails, and independent mathematical certificates disprove the drops. Intermediate failed runs and synthetic-admission rejection remain preserved.

Final native calls use file_path ONLY, no line/declaration/severity filtering, sequentially after final build/semantics/boundaries and before profiles. `final11-v2-native-{ml,main}.json` complete success=true, partial=false, timed_out=false, failed_dependencies=[]: MainLemma0errors/1existing header warning, Main0errors/4existing header+unused warnings. No zero-warning claim. Shared persistent LSP was not killed. Binding and source17 pins are in `final11-v2-native-binding.json`.

## Packing and inequality artifacts

`final11-v2-packing-orientation.json` rechecks every signature line on final source.

|Line|Width|Next unit width|Arithmetic|Action|
|---|---:|---:|---|---|
|241|89|28|89+1+28=118>100|ok|
|242|95|22|95+1+22=118>100|ok|
|243|99|none|conclusion joined; final line|ok|

|Signature offset|Comparison|Action|
|---:|---|---|
|118|‖f.coeff i‖ ≤ A|keep smaller-left|
|173|‖P.coeff i‖ ≤ C|keep smaller-left|
|208|P.natDegree ≤ s|keep smaller-left|
|242|remainder norm ≤ bound|keep smaller-left|

Zero ≥/> signature occurrences; no `_ge_`/`_gt_` name. Original3 rename rows and appended fourth row remain exact. Refactoring needed: rename `Roth.abs_coeff_modByMonic_le` → `Roth.norm_coeff_modByMonic_le` at project-end SINGLE pass only. No in-place rename.

## Source/cache/import provenance

BEFORE saved actual old binaries and ALL104 Roth cache companions, source17, Lake env, setup/options and actual successful `lean --deps` BEFORE API edits. Both required frozen BEFORE captures completed prospectively. `before-cache.json`, `before-source/`, `before-env.txt`, `before11-actual-deps.*` preserve exact provenance.

V2 actual built source17/cache104 are separately saved in `final11-v2-source/`, `final11-v2-cache/`, `final11-v2-cache.json`. `v2-complete-import-catalog-summary.json` and the full before/final catalogs cover ALL12,201 setup-resolved artifacts including split companions,1,803,534,984 final bytes. ALL12,185 MainLemma-profile imports match before/final exactly. Only imported MainLemma.olean changes in transitive Main's import set. Setups/options/importArts are byte identical. All12,190 external artifacts are freshly rehashed equal to the accepted prior external catalog; the reconstructed BEFORE external catalog is honestly reused prior immutable evidence, not a pretend prospective hash. Eleven project imports use actual old saved binaries. The direct deps probe is explicitly separate from this complete catalog. Every actual compiled import has a failed strict UTF8 decode and documented binary exception. Environment differs only in SHLVL2→1; all Lean/Lake paths/settings match.

The valid first AFTER capture on source83670dcf... measured helper248.168+public458.560=706.728ms/main5228.866ms. It is explicitly SUPERSEDED by the actual trace-supported direct-order proof change. Its exact scaffold/source17/cache/raw stdout/stderr/runner JSON remain at original paths and hashes. `final11-v1-superseded.json` documents the change; it is not silently discarded or compared as final. New V2 filenames preserve all that provenance. No unchanged third cherry-pick.

## Final matched performance pair

|Complete scope|BEFORE first ms|BEFORE repeat ms|V2 AFTER first ms|V2 AFTER repeat ms|
|---|---:|---:|---:|---:|
|Public target|745.518|701.298|415.072|527.094|
|All new helpers (one)|not present|not present|284.604|254.362|
|Meaningful target+newhelper combined|745.518|701.298|699.676|781.456|
|Actual sole direct consumer Roth.main_lemma|5129.205|4906.795|4914.491|5012.854|

Both required identical frozen AFTER samples completed, regardless of first result. Each uses actual CLI `lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`, separately saved stdout/stderr, actual exit0/no timeout/strict UTF8/all17 pins immutable/owned PGID absent. Before scaffold SHA3fac8d1378f650972610aae3e72bd7fa4103620493319a66353493328efa0720; V2 scaffold SHA0b42e8e0ff13a835d9460a37a76d43d70f5a373bfee7f4d69a6756cf1e53ac72. Complete canonical source recovery is exact. Target/direct-consumer scopes and CLI/options match BEFORE; the new helper is separately measured and fully INCLUDED in target acceptance. No target-cost laundering.

Each row is derived from the exact unique declaration token+separator and FULL qualified proof name, only column0 disjoint complete Elab.command+Elab.async roots, including proof/kernel/compiler/lint and excluding nested Meta/children/next command/end double counts. Public names are Roth.abs_coeff_modByMonic_le/Roth.main_lemma; standalone private name is `_private._stdin.0.Roth.exists_norm_coeff_reduction_aux`. Unmodified owner anchored_profile_span.py plus verify_profile_roots_exact.py verify all six final rows. Full *-timing/*-complete/*-rows JSON and rawstreams retained. No unchanged third sample.

The combined target satisfies the original <1000ms gate in BOTH captures. Direct main_lemma was already >1000ms BEFORE; its own slow queue remains owner/file-level work. These full pairs are reported honestly rather than claiming every caller improved. Local changed-call diagnostic old block182.301/179.507ms versus final101.651/102.334ms shows the narrow norm bridge/application does not explain any whole-main increase. Those nested Elab.step diagnostics are localized evidence, NEVER added to complete roots. Full pair changes are -4.19%/2.16%; no assertion that a whole-declaration fluctuation proves an API regression, and no foreign broad main refactor to manipulate the sample. `original11-direct-application-diagnostics-final.json` retains all actual event spans and the superseded V1 event.

# Final original11 audit details

This is the original target's fresh audit, distinct from the accepted fresh helper audit. The helper report and owner reviews provide its independent lifecycle evidence, not substitute original theorem credit.

## Audit24

1. LINT: complete unfiltered native ML one existing header warning, Main four existing header/unused warnings; no target warning, no filters/suppression. Fresh actual affected module build exits0.
2. HAVE SCAN: one public `have hA`, a coefficient-bound consequence used in both constant-divisor and self-remainder arms; shared2uses, retain. All other public local facts are induction binders or destructured substantive reduction certificate, not single-use no-by have wrappers. Original ha0/hQdeg/hQlc/hdeg/hP'deg/hP'c/hac/hfc/hmod scaffolding replaced by audited generic reduction and direct mathlib degree API. No extracted trivial tuple helper.
3. SET_OPTION: no source options added. Defaults remain bounded; no maxHeartbeats/maxRecDepth/synthInstance limit raises; builtin max0 counter not used.
4. SIMP SQUEEZE: both public simpa calls close their branches. Original nonterminal simp at hlt disappeared with the new self-remainder dichotomy. No nonterminal broad simp remains. Narrow caller Int.norm_eq_abs bridges are terminal simpa.
5. NAMING: original abs name becomes inaccurate for generic seminorm; fourth queue row requests Roth.norm_coeff_modByMonic_le at project-end SINGLE rename pass. Exact preexisting3rows preserved, no in-place rename.
6. PACKING: final3line signature has widths89/95/99; arithmetic89+1+28=118 and95+1+22=118; both mandatory breaks. Conclusion joins final hypothesis line. Actual #check output retained in semantic log; source widths are independently measured against the100-column rail. Full table separately final11-v2-packing-orientation.json.
7. BY: all by on preceding line, no standalone by.
8. FORMAT: 2space proof/4space signature; no empty proof lines; no haveI/letI; lambda arrow↦; sequential exponent rw merged.
9. COMMENTS: no inline comments in original target, none deleted. Exact original source quotation preserved. Main source/foreign declaration comments protected byte-for-byte; module Mainresult bullet now states seminormed-ring coefficient norm result.
10. DOCSTRING: present and precise about coefficient norms, arbitrary degree cap, no independent sign/monicity hypotheses, and nonmonic identity behavior. Exact historical source quote retained verbatim.
11. VISIBILITY: public module-doc Main result and reusable SeminormedRing API; private helper stays private/no docstring. No gratuitous foreign visibility changes.
12. STRUCTURE: public15body/10maximum induction branch; independently audited helper27body/8branch. Combined42prooflines compared with original58, with one mathematically substantive reduction certificate. No weaker public conclusion.
13. MATHLIB: actual five-method Finder/Loogle/LeanSearch/source rg/local name responses retained. Partial matches div_wf_lemma/modByMonic_eq_of_not_monic/modByMonic_eq_self_iff/divModByMonicAux/coeff_mul_X_pow'/norm_sub_le/norm_mul_le used directly. Submodule coefficient-membership APIs do not bound multiplicities or coefficient magnitudes. Actual exact? fails, apply? apparent closure rejected by open/sorry guard, state restored; no search-only absence claim.
14. JUNK DEF: theorem, no production def/abbrev added or modified.
15. EXISTS: introduced reduction certificate is nontrivial degree decrease, norm growth and same-remainder content, audited separately; no trivial witness+rfl wrapper.
16. SHOW: no public show/change; the direct order fact `le_add_of_nonneg_right` proves the power-base bound without a sign-only arithmetic solver.
17. PUSH_NEG: none; original push Not case split superseded.
18. GENERALISE: table below covers all12original and11new outer binders and all inner effective binders. Actual drop failures and counterexamples preserve necessary remaining hypotheses. Integer absolute-value contract recovered with literal raw AST equality and closed actual proof values.
19. INEQUALITY: all four public signature comparisons≤, zero≥/>. Explicit occurrence scan and no reversed orientation rename; existing queued name reflects norm formulation.
20. NORMAL-FORM: Polynomial.modByMonic, natDegree and norm in ℝ are pinned canonical APIs; natural truncated exponent s+1-f.natDegree preserved exactly. Int.norm_eq_abs is the canonical specialization bridge.
21. SYNTAX-GEN: sign and monicity arguments removed; arbitrary s cap retained for direct natDegree_diag_le caller use. Changing all-coefficient bounds to finite-index bounds is mathematically equivalent via coeff_eq_zero_of_natDegree_lt plus coefficient0nonnegativity, adds index-proof burden at the real caller, and gives no weaker hypothesis. Output index remains arbitraryℕ.
22. IMPORT-FANOUT: no source imports added. All complete actual setup paths/options/importArts and split companions verified, profile import identity before/after checked.
23. CASTS: nine explicit original :ℤ ascriptions and twelve :ℝ ascriptions disappear with cast-free generic norm proof. No numeric coercion added. The actual ℤ→ℝ norm interpretation is retained through Int.norm_eq_abs in old-contract adapter/caller. The retained `hA : 1 ≤ 1 + A` proposition annotation is not a numeric cast.
24. INSTANCE-NAME: no named instances introduced. SeminormedRing instance argument implicit, helper's nontriviality derived anonymously from hself. No decidability section binder leaks.

## Generalisation2.6a–e: original binders

|Original binder|Class|Candidate/actual evidence|Result|
|---|---|---|---|
|f:Polynomialℤ|structure value|appears in remainder/exponent; arbitrary SeminormedRing R replacesℤ and norm replaces integer abs; expected-new/value guards+Quaternion/zero-seminorm certificates compile|generalized|
|hf:f.Monic|proposition|drop; actual nonmonic remainder identity fallback now covered, including0andconstant2|removed|
|A:ℝ|bound value|norm codomain isℝ; retains arbitrary real A, no imposed positive restriction; deletion leaves free RHS/hfA|retain arbitrary|
|hA:0≤A|proposition|derive norm_nonneg.trans(hfA0), confirmed sign consequence and old adapter guard|removed|
|hfA:∀i,abs(coefffi)≤A|proposition|norm form; clear+replay fails on missinghfA, countercertificate f=X−2,P=X,A0,C1 shows false output without it|retain norm form|
|P:Polynomialℤ|structure value|arbitrary dividend; changing to abstract SeminormedRing proven actual; deletion leaves free remainder/hs/hP|generalized|
|C:ℝ|bound value|real norm bound, no positivity hypothesis; deletion loses RHS/hP|retain arbitrary|
|hC:0≤C|proposition|derive norm_nonneg.trans(hP0), actual zero polynomial and zero seminorm cases accepted|removed|
|hP:∀i,abs(coeffPi)≤C|proposition|norm form; clear+replay fails; C0,P1/fX countercertificate disproves removal; pointwise hP(outputi) also insufficient (P=X,divisorX−2,output0)|retain uniform norm form|
|s:ℕ|index cap value|enters natural truncated exponent and hs; free-value deletion is ill-formed, replacing by a different index type changes polynomial-degree content|retain arbitrary natural|
|hs:P.natDegree≤s|proposition|clear+replay cannot supply recursive degree cap; s0,P=X²,f=X−2 gives false4≤1 without cap; already non-strict, no strict→weak candidate|retain|
|i:ℕ|output index|appears in conclusion; deletion free/ill-formed; restricting output weakens conclusion|retain arbitrary natural|

New effective binders are universeu_1,{R:Type*},[SeminormedRingR],{f},{A},hfA,P,{C},hP,{s},hs,i (11outer parameters plus universe). Type* retains full universe polymorphism. SeminormedRing deliberately drops NormedCommRing's separation/commutativity. Ring alone cannot state/prove the norm inequalities; SeminormedAddCommGroup alone lacks multiplication/unit/monic division, and NonUnital parent lacks unit. The zero-seminormℤ certificate excludes accidentally relying on norm separation; Quaternion witness and application exclude accidental commutativity. No Nontrivial/NormOneClass/decidability assumption remains.

Inner effective binders: hfA.i and hP.i arbitrary coefficient indices; induction s and ih with smaller natural t<t_bound, generalized P,C,hP,hs; output i fixed arbitrarily; hself branches exhaust equality/inequality; hf1 exhausts unit divisor; Q,hQdeg,hQc,hmod,hn,hfs from substantive witness; hQc's inner j arbitrary. Every bound is already≤, no strict→weak predicate remains. hA's derived fact uses coefficient0 and is reused, not an assumption. Nontriviality/monicity/positive divisor degree arise ONLY within helper's non-self case; neither is silently an outer premise.

2.6b actual clear+proof probes use parsed non-hygienic original proof and actual local binder IDs; failure messages reflect missing proof inputs, not a reported successful generalized theorem. Certified mathematical counterexamples separately rule out the drops. 2.6c every beneficial broad domain/sign/monicity change is applied under standing authorization; no invented abstraction or unresolved new helper. Finite coefficient-bound formulation is equivalent and would make real applications harder, so uniform form retained. 2.6d all three actual web-query raw responses and exact top3returned blocks saved; primary standard ring long division supports the algorithm, while quantitative abstraction is independently proven in Lean. No math MCP exposed. 2.6e applied weaker assumptions/generalization pass exact original specialized adapter and all actual callers.

Inversion check: already parameterized by arbitrary polynomials, not a theorem tied to a concrete named object; no concrete object disappears after unfolding. The real additional abstraction is seminormed-ring coefficient growth, now realized with actual counterexample/endpoints and callers.

## Mathlib five-method status

A Finder query: bound coefficients of remainder monic polynomial using bounded coefficients; CoeffMem span-product and degree APIs found.
B Loogle actual `Polynomial.modByMonic, LE.le`; degree monotonicity/sum_modByMonic_coeff found.
C LeanSearch actual coefficients remainder division monic bounded norm; algebraic membership/division/root norm results are partial, no quantitative remainder match.
D full pinned rg: coeff_modByMonic/modByMonic_coeff/norm_modByMonic/abs_modByMonic/div_wf_lemma; unfiltered output saved source-search11.txt.
E actual local modByMonic names, index unavailable explicitly reported by server; genuine textual22matches returned, not an absence guarantee. Auxiliary _eq_of_not_monic,_eq_self_iff,_of_dvd_sub,_left variants reviewed. Common-equivalents table no disguised compactness/finite/topological concept applies.

Conclusion: use partial existing APIs directly; retain genuine quantitative bound. Actual generic whole-proof search fails, and apparent apply? term rejected by closed-value gate; no false claim of exhaustive absence from all mathlib formulations.

## Golf42 final status

|Rule|Final outcome|
|---|---|
|1.1|No by-exact wrapper; public proof remains a short mathematical outline|
|1.2|No by-rfl wrapper|
|1.3|Original low-degree rw+exact replaced by terminal simpa in self case|
|1.4|Terminal simpa branches consolidate simplification and inequality transport|
|1.5|No simp+rfl tail|
|1.6|No constructor/exact pair; substantive helper tuple audited separately|
|1.7|Direct le_mul_of_one_le_left/norm API terms used|
|1.8|No by_contra/push_neg pair in public proof|
|1.9|No eta-reducible lambda; pattern arrow=> appropriate, helper lambdas↦|
|1.10|Single-use original coefficient/cancellation have scaffolding eliminated; shared hA retained|
|1.11|No apply-intro chain|
|1.12|No redundant show|
|1.13|Obtain reduction certificate components directly|
|1.14|Merged mul-association/power successor rewrites|
|1.15|Public terminal simpa unsqueezed; no terminal simp only|
|1.16|Original nonterminal bare simp removed by new case strategy|
|1.17|Inequalities compose using .trans/.trans_eq|
|1.18|No unnecessary final lambda/by parentheses; retained arguments delimit compositions|
|1.19|No push_neg, old push Not no longer needed|
|1.20|Helper substantial degree/norm/remainder certificate, no trivial existential wrapper|
|2.1|Actual whole grind fails; no partial result accepted|
|2.2|No selected grind/pre-grind tactic chain|
|2.3|Terminal self/constant cases consolidated by simpa|
|2.4|No continuity/differentiability/measurability goal|
|2.5|Applied direct `le_add_of_nonneg_right` and `zero_le_one.trans hA`; both previous sign-only linarith calls removed after trace diagnosis and actual closed-value guard|
|2.6|Core norm inequalities in audited helper use direct add_le_add/mul_le_mul; helper actual gcongr probe fails; no extra public monotonicity block|
|2.7|Nat lia proves strict predecessor index and truncated exponent equality; whole omega fails|
|2.8|Actual whole aesop fails; no slower broad search selected|
|2.9|No numeric cast goals in generic proof; boundary certificates use norm_num and actual norm API|
|2.10|Arbitrary universally quantified polynomial bound not finite computation; no native_decide/trust extension|
|2.11|No denominators; noncommutative helper uses pinned recurrence rather than ring normalization|
|2.12|No final ring/ring_nf-ending public block with algebraic hypotheses; original scalar distributivity block replaced by direct rewrite|
|2.13|Unit/self-remainder/high-degree cases are not symmetric; wlog inapplicable|
|2.14|Composed inequalities via trans/trans_eq; no redundant two-step calc|
|2.15|Tried congr2<;>lia; native linter correctly rejected unnecessary sequence focus, restored separate tactics|
|3.1|No erw|
|3.2|No legacy continuity/measurability|
|3.3|Original omega replaced by lia in final public natural arithmetic|
|3.4|No public rcases-rfl sequence; helper zero contradiction independently audited|
|3.5|No global automation attributes: quantified bounds are not simplification normal forms|
|3.6|No simp_all only; whole simp makes no progress|
|3.7|No added/raised limits or production profiler/count scaffolding|

Stepback/simplify: existing div_wf_lemma removes original manual leading-term cancellation; substantive reduction helper makes induction transparent; norm formulation removes integer casting and unnecessary commutativity/separation. Whole automation and existing-lemma searches actually attempted. No public theorem merely wraps1–3 existing mathlib calls. Built-in simplify tool unavailable; explicit holistic reuse/quality/efficiency review performed, not a fabricated invocation. Helper audit completed before final aftercaptures. Direct sign simplification passed actual candidate and final imported value guards. No broad foreign Main refactor.

## Diff gates — final original11

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|PASS|fresh V2 affected build exit0,92.090s|
|definition_protected|PASS|all existing def/abbrev bytes unchanged|
|theorem_statement_protected|PASS with authorized GENERALISE change|item18 actual SeminormedRing weakening, exact old Int adapter and all written caller types/value guards pass; no weaker conclusion|
|structure_gate|PASS|public headline15/branch10, no public conjunction; helper27/branch8 independently audited|
|naming_gate|PASS with deferred action|fourth justified norm rename queued, exact prior3rows preserved, no in-place rename|
|line_packing_gate|PASS|all3rows89/95/99, correct118>100 arithmetic, all actions ok|
|inequality_orientation_gate|PASS|all4occurrences≤,0≥/> in signature|

Overall: PASS for this worker scope. Filewide global all-row/cumulative-original/all-retained-value/import/static/reference/docs final simplify and publication remain mandatory owner stages; this is not a claim that foreign slow queues or project publication are complete.

## Phase checklist

- [✓] Step1: full reference/skill/context instructions read,854-line prompt explicit ranges recovered.
- [✓] Step2: all24 original-target audit items printed below.
- [✓] Step2.5: all5 actual mathlib search statuses and actual generic automation controls printed.
- [✓] Step2.6: all outer/inner/effective binders, weakening/generalization2.6a–e/literature/counterexamples printed.
- [✓] Step2.7: complete per-line packing widths/arithmetic printed and final source rechecked.
- [✓] Step2.8: all4 inequality occurrences printed; zero reversed comparisons.
- [✓] Step3: all42 golf rules have explicit status below.
- [✓] Step4: holistic stepback/simplify/reuse/efficiency review performed; no fabricated unavailable builtin tool.
- [✓] Step5a: fresh complete unfiltered nonpartial nontimeout native ML/Main0errors;1/4existing warnings disclosed.
- [✓] Step5b: full diff gates and exact source protection printed; independent original/expected/caller TYPE+actual VALUE guards pass.
- [✓] Step6a: justified fourth rename appended earlier, exact4rows remain, project-end SINGLE pass preserved.

Original11 final artifact manifest covers all local artifacts (including failed/superseded samples), this report, current source/queue, exact helper bytes, all source17/cache/import/scaffold/CLI/raw/native bindings, strict UTF8 or actual binary exceptions. Final postcapture integrity rehashes current17 pins, before+both final saved cache104 sets, final current cache104, all12,201 current imports, exact helper8036cf and both actual final runners/rawstreams. All owned groups are independently absent in final11-drain-release.json. No Git/shared-progress mutations; no main/pin/merge/force-push changes. Explicit release of source/target/necessarycaller/report/compiler/native/profile leases and END accompanies delivery to owner.
