# Fresh helper16 audit: exists_auxiliary_polynomial_of_log_bound_aux

Scope: one private helper; fresh mandatory Mode B audit. This report is provisional until final builds, natives, retained values, matched after profiles, closure, and owner acceptance. It grants no original27, main-lemma, whole-file or publication credit. Owner retains all Git and shared records. Entry MainLemma789 SHA736a868c38a13d4112f661afa683fdf67b39e01a2a181514e0bc5f7eb503a4ae; Main689 SHA6668ff83a7e7b156f6f29b8f2d0163e699da002b70338d5ee0715065ade9b25f. Genuine first draft f5571524b13db7fcee3e3b7c7db372990ac8df0c35f1361726c9b572e7ed2e76 saved before any helper golf. Scratch `/private/tmp/roth-mainlemma-helper16-fresh1` (Q16) contains authoritative versioned receipts and raws.

## Phases 0–3: baseline, preparation and punch-list

Read full installed Lean/mathlib-quality skills, cleanup/cleanup-all/buzz commands and required references; primary clean.tex §6 passage, full source, original first draft and owner packet. Initial combined displays truncated; bounded rereads supplied full startup read credit. No AGENTS found in actual ancestor/repository paths. Runtime Lean4.34.0 arm64293d5d0 / Lake5.0-src293d5d0 / Python3.9.6. Pinned mathlib5ed2965256430c3649e86755f9576b54eca72435. Explicit own frozen environment, default200000/20000/512. Initial FULL build0 (34.90s), then separate Eval0 (14.92s), rebuilt789 from prior compiled769. Early native v1 returned success but had deficient raw-save chronology; strict fresh early-v2 success has full PRE→savedSEND→immediateRETURN→fullRAW/hash/bytes/saveobservation→POST. Inherited ML copyright warning1 protected; no target warning. No optional count_heartbeats macro used (it raises limits).

Punch-list: pack eleven signature lines; inline single-use arithmetic/log facts; replace stronger monic leading-coefficient argument used only for0≤A with direct hA0; remove definitional change; unsqueeze terminal simp; collapse final calc. No file-level source edits are warranted within this lease: imports/header/module docs/definitions/options/nine narrative comments remain protected. Main32 still FAIL15; scope does not hide its proof in a wrapper. All14 prior helpers and selector protected. Public main TYPE, Main source, docs and paper quotes protected.

## Full deep audit (all24 items)

| # | Item | Actual finding/action |
|---|---|---|
|1|LINT|Fresh initial native warning1 is inherited copyright, outside target. Candidate default compiled guards emit no new target warning. Actual final three natives errors0/inheritedwarnings1,4,0/no target warning.|
|2|HAVE SCAN|Original hA1 used only for0≤A: removed in favor of abs_nonneg.trans(hA0). hr₁/hlogα single-use term proofs inlined. hBpos used in rpow and derivative bound, retained. hpow has proof content and supplies final ring relation, retained. B and β reused, retain local lets.|
|3|SET_OPTION|No helper option; default guards verify200000/20000/512 throughout.|
|4|SIMP SQUEEZE|Original terminal simp only[Nat.cast_ofNat,mul_comm] becomes terminal simp[mul_comm]. Definitional change removed. No nonterminal bare simp remains. Failed terminal simpa/ring probes preserved; linear_combination accepted by full VALUE guards.|
|5|NAMING|Descriptive exists_auxiliary_polynomial_of_log_bound_aux names existence and log-budget content, private snake_case auxiliary; no numeric scheme/forbidden abbreviation. No rename required/queued.|
|6|LINE PACKING|All8 final signature rows measured below; maximum100. No underpacked row remains.|
|7|BY PLACEMENT|Main := by and hpow := by at end of their statement lines; no isolated by.|
|8|FORMAT|2-space proof indentation; no internal blank lines; grouped rw; no haveI/letI or semicolon chains.|
|9|COMMENTS|Target originally has zero narrative proof comments; removes none. All nine existing file narrative comments and docs retained byteexact by source inverse.|
|10|DOCSTRING|Private auxiliary: no new public docstring. Existing public docs and mathematical quotation untouched.|
|11|VISIBILITY|Only used locally by main construction; remains private with descriptive _aux.|
|12|STRUCTURE|23→19 proof lines; hpow branch4→3, maximum3 (≤10), ordinary ≤30. Correlated conjunction is properties of ONE common P, not independent witnesses: packet explicitly requires preserving it. Separate existential witnesses would lose the required SAME P; shared-P formulations are mathematically possible, but no beneficial replacement is established; no conjunction convenience wrapper introduced.|
|13|MATHLIB|All five fresh actual methods recorded below; no searched existing replacement proves the combined correlated algebraic/index/Hasse contract.|
|14|JUNK DEF|Not a def. No additional production declarations introduced during this fresh audit.|
|15|EXISTS LEMMA|Not trivial constructor/rfl witness packaging: obtains P via algebraic pigeonhole, proves positive scale bound and all derivative estimate. Retain meaningful helper.|
|16|SHOW vs CHANGE|Original definitional change in hpow deleted; no show/change remains.|
|17|PUSH_NEG|None.|
|18|GENERALISE|All16 binders+universe considered below; honest selected-proof drops/strict weakenings fail, no mathematical necessity inferred from failures. Certified boundary counterchecks separately recorded.|
|19|INEQUALITY|Every signature occurrence audited below: zero ≥/>. No ge/gt declaration segment.|
|20|NORMAL-FORM|Uses RSet/B₁/gam/index/hasseDeriv existing canonical APIs, no alternate duplicated definitions. hpow relates the sole real exponent bound to β³; no new normal-form API.|
|21|SYNTAX-GEN|No custom notation/macros/elaborators. Anonymous point is still diagonal α required by algebraic root step.|
|22|IMPORT-FANOUT|No imports added, no broad tactics import. All actual used identifiers compile from existing imports.|
|23|CASTS|f.coeff→ℝ chooses real height, q₁→ℝ chooses real rpow, B₁→ℝ chooses real strict bound, B→ℝ in β/hBpos/hpow chooses real order/rpow. These are necessary domain annotations; no redundant Nat.cast/Int.cast rewrites inserted. Nat.floor_le supplies exact integer-to-real coefficient bound.|
|24|INSTANCE-NAME|No instance declarations or local haveI/letI.|

## Signature packing (Unicode codepoints)

The next token is a whole dependent binder or semantic mathematical expression; splitting hL into an extra hypothesis would change the API.

| Row | Width | Next semantic token | Arithmetic | Action |
|---|---:|---|---|---|
|1|87|`(hf : f.Monic)`|87+1+14=102>100|ok|
|2|99|`(hm : 0 < m)`|99+1+12=112>100|ok|
|3|99|`(hL : 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log q₁)`|99+1+94=194>100|ok|
|4|100|`∃ P : MvPolynomial (Fin m) ℤ,`|100+1+29=130>100|ok|
|5|68|`gam δ f.natDegree m ≤ index (map (Int.castRingHom ℝ) P) (fun _ ↦ α) r`|68+1+69=138>100|ok|
|6|97|`\|eval (fun _ ↦ α) (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))\|`|97+1+76=174>100|ok|
|7|84|`(B₁ δ q₁ r₁ : ℝ) ^ (1 + 3 * δ)`|84+1+30=115>100|ok|
|8|44 (includes `:= by`)|end|n/a|ok|

## Per-occurrence inequality scan

| Location | Occurrence | Orientation/action |
|---|---|---|
|hA|abs coefficient ≤ A|≤ retained|
|hm|0 < m|< retained|
|hr|0 < r j|< retained|
|hs|sum r ≤ m*r₁|≤ retained|
|hδ0|0 ≤ δ|≤ retained|
|hL|full log budget ≤ δ² log q₁|≤ retained|
|conclusion index|gam ≤ index|≤ retained|
|conclusion all i,k|abs evaluation < B₁^(1+3δ)|< retained|

## Generalisation item18 / 2.6a–e

| # | Binder | Class | Use and actual catalogue assessment |
|---|---|---|---|
|1|f:Polynomial ℤ|structure value|Integer nonzero coefficient bound and algebraic index construction. Replacing coefficient ring would require new height/root/finite pigeonhole APIs; not a small parent-class substitution.|
|2|α:ℝ|structure value|Root, log(abs α) and diagonal evaluation; arbitrary evaluation point breaks root-dependent index theorem. No independent point extension recommended.|
|3|A:ℝ|structure value|Uniform height bound and budget; arbitrary real already, not nat/nonnegative restriction.|
|4|hf:f.Monic|proposition|Passed to accepted index construction. Actual drop-monic probe fails. No necessity theorem from this failure; nonzero/leading-coefficient normalization is a different theorem requiring new arithmetic estimates.|
|5|hfα:aeval α f=0|proposition|Passed to algebraic index construction. Actual drop-root fails; arbitrary-point conclusion is not established by that failure.|
|6|hA:∀i,abs coeff≤A|proposition|Global bound used in upstream construction plus hA0; actual drop-height fails. Point-local bound on0 alone does not supply upstream finite coefficient height. No redundant sign assumption.|
|7|m:ℕ|structure value|Dimension of Fin, exponent and gam; arbitrary nat already. Zero-dimensional extension formally fails strict ALL-derivative conclusion under budget below.|
|8|q₁:ℕ|structure value|Natural scale in accepted floor construction and log; arbitrary nat including0/1 syntactically, hypotheses force>1. Real-scale generalization needs upstream theorem/API, not mechanical class weakening.|
|9|r₁:ℕ|structure value|Natural coordinate budget/floor; positivity derived rather than assumed. r₁=0 excluded when m>0 and hr/hs.|
|10|hm:0<m|proposition|Provides Fin witness and positive r₁. Actual drop and0≤m selected proofs fail; separately certified m=0,r₁=0 feasible budget with impossible strict evaluation bound, so no unqualified zero-dimensional extension.|
|11|r:Fin m→ℕ|structure value|General coordinate sizes already; no constant/equal-size restriction. Not replaceable by real coordinates without changing polynomial degree/weighted index APIs.|
|12|hr:∀j,0<r j|proposition|Global positive coordinate hypothesis of index theorem and derivation r₁>0. Actual drop and0≤r probes fail. Zero individual coordinates may admit a redesigned theorem; no mathematical necessity or blanket impossibility inferred.|
|13|hs:sum r≤m*r₁|proposition|Already weak at equality. Used upstream and derivative bound; actual drop-sum fails. Pointwise bounds would be stronger, so not an improvement.|
|14|δ:ℝ|structure value|Arbitrary real parameter already; exponents and gam depend on it.|
|15|hδ0:0≤δ|proposition|Already weak and includesδ=0 syntactically; δ=0 budget impossible. Actual drop-sign fails; negativeδ=-4,q=2,r₁=1 formal feasible-budget/RSet obstruction disproves unqualified removal.|
|16|hL:fullbudget≤δ²logq₁|proposition|Already weak at equality; logα term projected monotonically to upstream budget. Actual drop-logbudget fails. Removing it/altering constants needs stronger theorem, no supported recommendation.|
|17|universe|universe|All data fixed ℤ,ℝ,ℕ,Fin m; actual levelParams=[] exact. No free Type parameter to change to Type*.|

2.6b: fifteen selected-proof experiments are actual isolated compiled failures (five whole-proof automation, eight hypothesis drops, two strict→weak); preserve all raws. 2.6c: no beneficial supported big-change candidate; general coefficient rings/arbitrary evaluation points require different upstream mathematics, so no deferred recommendation. 2.6d: private auxiliary; public literature three-query/Top3 requirement not applicable. Primary paper passage independently checked. 2.6e: no statement change warranted; safe proof-only direct hA0 and inlining implemented in candidate. Do not interpret unsuccessful drop probes as proofs of minimal hypotheses.

## Five fresh mathlib search methods

| Method | Actual evidence/result |
|---|---|
|leanfinder|search-leanfinder-v1.json: nonzero integer multivariate bounded-coefficient polynomial/weighted index/algebraic point query; Chevalley and combinatorial Nullstellensatz hits, no combined replacement.|
|loogle|search-loogle-v1.json: MvPolynomial existential integer-polynomial shape, no hits for that query.|
|leansearch|search-leansearch-v1.json: boundedcoeff/index/root/pigeonhole query gives Schwartz–Zippel/root/Diophantine bounds, no combined API.|
|local_search|search-local_search-v1.json actual project hit/index warming; not an absence claim from an empty/unconsulted index.|
|source rg|search-source-status-v1.json and full stdout/stderr: exact full name no hits; RSet/index/rpow variants matched relevant APIs. Direct actual source signatures read. Missing queried IsEmpty/LogBounds paths were errors, never absence evidence.|

## All42 golfing rules

| Rule | Actual status |
|---|---|
|1.1 by exact|No wrapper.|
|1.2 by rfl|None.|
|1.3 rw+exact→rwa|No such adjacent pair; hpow rw transforms a goal then terminal simp.|
|1.4 simp+exact→simpa|No pair; initial hA1 simpa removed entirely.|
|1.5 trailing rfl|None.|
|1.6 constructors|Final singleP anonymous constructor already used and retained.|
|1.7 apply+exact|No pair; theorem application composed directly.|
|1.8 by_contra!|No contradiction proof.|
|1.9 eta reduction|Dependent coefficient/derivative lambdas needed for inequalities; constant diagonal λ_↦α is meaningful, not an eta-redex.|
|1.10 single-use have|hr₁/hlogα inlined; hA1 replaced by direct weaker0≤A. hBpos/hpow have real proof content/reuse.|
|1.11 refine+fun|Final i,k introduced in constructor term via fun; no apply/intro chain.|
|1.12 show|Redundant definitional change removed; no show.|
|1.13 projections→obtain|P/hPR/hγ, h2/_/hα and nonzero coefficient obtained directly.|
|1.14 merged rw|hpow rewrite list grouped; no consecutive rw.|
|1.15 terminal simp only|Unsqueezed to simp[mul_comm], compiled default/fullVALUE pass.|
|1.16 nonterminal bare simp|None.|
|1.17 dot notation|trans, trans_le, trans_eq, .le, .mpr already use dot style.|
|1.18 `<\|`|Nat.pos_of_mul_pos_left <| avoids trailing parentheses; argument grouping elsewhere needed.|
|1.19 push_neg|None.|
|1.20 trivial ∃|This is substantive commonP algebraic+analytic construction, not trivial packaging.|
|2.1 grind|Actual isolated whole-proof grind fails; no success credit.|
|2.2 delete before grind|No retained grind suffix.|
|2.3 simpa|Terminal simpa[hpow,...] genuinely failed due reordered exponent; retain failure. Composed trans_eq+linear_combination succeeds.|
|2.4 fun_prop|No continuity/measurability/analytic regularity proposition.|
|2.5 positivity|Used on log-factor multiplier, exponent side condition and real floor argument; full compiled proofs guard success.|
|2.6 gcongr|Projection is direct le_add_of_nonneg_right.trans; no nested monotonicity goal requiring gcongr.|
|2.7 lia/omega|Whole conclusion is noncomputable algebraic polynomial existence, not Presburger arithmetic. Nat positivity obtained directly without arithmetic search; no omega/linarith suffix.|
|2.8 aesop|Actual whole-proof aesop fails.|
|2.9 norm_num/norm_cast|Int.cast_ne_zero supplies exact cast nonzero proof; no numeric/cast normalization goal. Full formal boundary probes use norm_num separately.|
|2.10 decide/+kernel|Abstract root/real exponent existential is not closed finite decidable data. No native_decide.|
|2.11 field_simp;ring|No denominators. Native ring alone fails terminal equality; original rw[hpow];ring replaced.|
|2.12 linear_combination|Actual terminal -hpow succeeds, then full candidate TYPE+opaqueVALUE/default/std3/closed/inferred guards pass; no native-only proof credit.|
|2.13 wlog|No interchangeable symmetric cases in theorem or proof.|
|2.14 collapse calc|Two-step strict derivative calc folded into .trans_eq and final linear_combination.|
|2.15 <;>|One remaining algebraic equality goal; no duplicated goal-closing suffix to distribute.|
|3.1 erw|None.|
|3.2 continuity/measurability|None.|
|3.3 omega→lia|No omega.|
|3.4 rcases rfl|No equality substitution case.|
|3.5 automation registration|Private substantive existence lemma used once; global simp registration would be inappropriate.|
|3.6 simp_all|Actual whole-proof simp_all fails. No retained simp_all only.|
|3.7 limits|No options; defaults guard every actual semantic record.|

## Step4 reflection and Phase6.5 adapted holistic review

Freshly reconsidered entire helper after the mechanical pass: whole grind/aesop/simp_all/exact?/apply? cannot close it. apply? misleadingly reports goals[] while explicit residual subgoals remain; standard-axiom/fullVALUE checks reject admission. The construction inherently combines the existing algebraic P/index theorem with the separate iterated-Hasse analytic estimate. Replacing it with a self-wrapper or an unrelated conjunction helper is rejected. Term-mode packaging is already used for the common witness; a full monolithic term would obscure the nonzero-coefficient argument and rpow identity. Single-use facts compose directly; hBpos and hpow are meaningful named steps. A different independent proof was compiled to countercheck the contract, not recommended as a shorter production proof. No additional production helper, import, parameter or companion API recommended. Builtin Claude Skill(simplify) is unavailable; this is the standing-authorized actual fresh holistic whole-helper adaptation, not a fictitious tool invocation and not the later fresh wholeFILE reviewer. All supported beneficial findings are implemented in v6 candidate; no deferred local recommendations.

## Independent contract, boundaries and failed experiments

`proof-series-acceptance-v2.json`: 17 actual jobs drained; fifteen expected failures preserved without necessity inference. Independent original proof full TYPE and opaqueVALUE/default/std3/closed/inferred guards pass. Its actual recursive TYPE+allowOpaqueVALUE graph closes over20964 constants and bans both actual target roots/generated prefixes/main/adapter/sorryAx. Independent VALUE differs both genuine and final candidate. Independent TYPE differs ONLY two actual generated λx macrocontext pairs, unchanged suffix202/236; every other TYPE byte, written binder, BinderInfo, order, constants and universe exact. `independent-two-actual-generated-Name-pairs-v1.json` preserves actual pairs. No generalized Name/mdata normalization or rawbyteexact claim.

`contracts-acceptance-v3.json`: independent-v6 and candidate-v10 compiled exact full original TYPE constructor, additionally require repr(expected).pretty1000000 == FULL original rawTYPE inside Lean, so every Name string/numeric component/quoted component and Expr field is recovered exactly by syntax encoding. Only both actual generated binder names are eligible for finite hygiene comparison. Candidate helper TYPE/universes byteexact genuine; current main32 TYPE AND VALUE byteexact genuine. Entire literal47 oldmain recovery has exactly three generated macrocontext880859934→935 replacements (inst41,x274,x338), all other TYPE bytes exact, compiled BOTH-generated full-contract guard; recovery is NOT independent. All four full actual opaqueVALUE/std3/default guards pass. Do not confuse these3 caller-recovery pairs with2 independent helper pairs.

Twelve formal default/fullVALUE boundary theorems: positive r₁ from hm/hr/hs; positive natDegree from monic real root; identically zero r excluded; budget positive; δ=0 impossible; q≤1 impossible; no nonzero integer RSet below1; δ=-4 q2 r₁1 yields RSet obstruction; that negativeδ has feasible budget; empty Fin0 polynomial strict ALL-derivative bound<1 impossible; B₁2 2 0=1; m0 δ2 q2 budget feasible. This certifies the strict-bound m0 countercheck and negativeδ obstruction. It does not prove all other assumptions mathematically necessary. Equality endpoints of hs/hδ0/hL remain accepted weak hypotheses in actual complete original and candidate contracts.

All failed probes immutable: candidate-v4 simplifier/unsolved/admitted/std3 rejection; native terminal wrong-column-v1; terminal ring and simp failures; independent TYPE strict-byte acceptance-v1 failure; constructor-v4 raw repr parse failure on Name `a._@._internal._hyg`; contracts acceptance-v1 overstrict literal-oldmain byte-equality failure. v5/v6 and constructor syntax fixes are prospective versions, never overwritten failures. An exploratory exact diff used slow SequenceMatcher and subsequently terminal0/drained; no source mutation while it ran. A counting snippet initially omitted split max1 and failed before corrected counts; no missing evidence inferred. Wrong reference/source paths and truncated displays remain qualified. No proof credit from exit0 without all guards.

## Before performance phase (completed and released)

Explicit owner HOLD preceded ANY new phaseprep/probe/scaffold/observer/capture; inherited Q15 driver-template read actually preceded HOLD, and is recorded as such, not retroactively waived. Four actual frozen captures A/B helper+attached main and A/B separate full foreigncaller; complete env/fullpre/post observers/finalfreeze/drain terminal0, all1074 manifest-bound current-runtime groups absent. Owner release followed ENTIRE series completion before any raw parse. Canonical complete attached doc/TYPE/body framing bound; fresh actual generated families; full UTF8/rawhashes; disjoint column0 command+async proof/kernel/compiler/lint roots excluding Meta/nested/trailingend; no subtraction/doublecount.

Helper260.553/254.744ms; attached main32 569.762/508.575ms. Foreign Roth.roth_of_isIntegral3231.594/3191.347ms VALIDFAIL inherited separate Main obligation. Full fields17source/104cache/8root/14setup/12202package/12592core/4binary and all8 actual Lakeenv observations pinned. No regression/cause claim until matched finalafter. No newafter prep/captures yet; NEW explicit owner HOLD mandatory.

## Resource and historical qualifications

Authoritative before raws and two already-created decoded metadata exports retained intact. Accidental decoded export duplication ≈1.3GB is a resource qualification; no silent deletion/gzip/remap or optional copies. All subsequent comparisons use full actual row bytes via raw offsets with exact rawSHA/bytes; content-addressed compiled snapshots reuse existing snapshots; at the original resource-qualification-v1 observation only2.1MB were genuinely NEW blobs, alongside reuse of existing snapshots. This is that stage’s measured finding, not a new total-size assertion for later final-stage snapshots.

Preserve every predecessor failure/lost ADMIN fact: overwritten Q12 receipt returned1792712982.471543 vs replacement1792714051.5226429; old Q12 receipt bytes/SHA/mtime unknown, no reconstruction. Historical helper8 END771B SHA9533… replaced715B ed9f…; unknown exact old bytes/times remain unknown. Three historical temporary instruction texts unavailable (854-line verbatim worker prompt,112-line future-profiler,46-line payload-binding note); available103 instructionfiles remain bound. Archive692logical/645blobs requires stored+decoded checks at closure. Old AFTER PID absence does not imply unknown PGID absence. Historical VALIDFAIL exists_delta_bound12408.373/11188.775ms and pigeonhole_count1018.335/1000.235ms remain; this leaf does not waive them.

## Historical remaining gates at the initial report stage

Production is still genuine789 at this report's initial creation. Required final narrow apply, FULL→separateEval, three strict complete natives, independently derived final inventories and all retained TYPE+opaqueVALUE comparisons, matched fourcall after profile/HOLD/release, final seven+explicit cumulative gates/11 verification/Overall6b, owner ADMINHOLD snapshots, two full closure streams and elevated full drain remain pending. No ALL8END/helpercomplete claim until those and owner final acceptance.

Application metadata qualification: apply-v1 field `all_other_sources17` actually contains14 Lean source rows (including changed MainLemma), not17 pins. `apply-source17-qualification-v1.json` independently compares complete actual17 pins against strict early-v2 PRE: MainLemma alone changed, SIXTEEN other pins byteexact. Earlier “17 other” phrasing was incorrect. Packing-v1 last row38 omitted delimiter; packing-v2 actual full last row44 includes `:= by`; retained v1 is superseded.

## Final source, builds and natives (actual completed)

Applied v6 helperONLY after entire required identifier-check job drained0: MainLemma782 SHA6c976e2a6ee367ec2e109d02fab83be939ffb1856ec2b52205f6176790a663cc, exact helper-only inverse restores genuine789736a. No caller/API repair. Body23→19/maxbranch5→3. Exact17pin set has sixteen unchanged others; fourteen Lean-source rows are a different subset.

Final FULL build exit0/drained52.0779s THEN separate Roth.LeanEval build exit0/drained24.0855s, source immutable through the whole series. Full unfiltered filepath-only actual natives ML/Main/Eval all success/nonpartial/nontimeout/errors0/faileddeps[] with inheritedwarnings1/4/0. `final-three-native-acceptance-v1.json` binds all three actual request objects, fullrawSHA/bytes, source17 PRE/POST and PRE≤savedSENDbeforeawait≤immediateRETURN≤fullRAWsave/hash/bytes/saveobservation≤POST. All nine corresponding prep/save/post execs returned terminal0, no dependent step while ongoing. Final declarations/inventories/profile/closure remain pending at this append; no earlier pending-row automatically supplies credit.

## Identifier verification and final static diff checks

Fresh `final-identifier-check-v1` compiled exit0/drained23.2736s before application. These are existing APIs, not new production declarations; actual successful #check outputs are in its immutable log.

| Identifier | Verification | Result |
|---|---|---|
|MvPolynomial.exists_coeff_ne_zero|actual #check; use in the fully VALUE-guarded helper|pass|
|Nat.pos_of_mul_pos_left|actual #check; use in the fully VALUE-guarded helper|pass|
|Real.rpow_add_of_nonneg|actual #check; use in the fully VALUE-guarded helper|pass|
|Real.rpow_mul_natCast|actual #check; use in the fully VALUE-guarded helper|pass|
|le_add_of_nonneg_right|actual #check; use in the fully VALUE-guarded helper|pass|
|LT.lt.trans_eq|actual #check; use in the fully VALUE-guarded helper|pass|
|Nat.floor_le|actual #check; use in the fully VALUE-guarded helper|pass|

`final-static-acceptance-v1.json` checks exact helper-only source inverse, no forbidden proof/option/TODO syntax, every source line≤100, signature zero≥/>, body19/maxbranch3, comments0/0 and all nine other narrative comments protected. Actual fresh call-site search saved full stdout/stderr: helper call only current main; Main imports MainLemma and calls publicmain at565. Final FULL build and full Main native independently cover this actual foreign call; separate Eval and Eval native cover the loaded root/Eval surface. No private API/caller source change.

## Final retained semantic surface (actual completed before AFTER phase)

Fresh independently derived AFTER imported inventory471 over13 nonempty defining origins, rootRoth0 explicitly, Eval5; direct inventory409=75 actual-local-source+334 imported. No copied counts, namespace-only filter or hasValuefalse omission. Both actual inventories have all hasValue true. Default full guarded AFTER imported job0/drained204.1033s and local0/drained152.6078s. `retained-pairs-acceptance-v2.json` streams exact authoritative raw rows for ALL880 actual pairs, binds fullrawSHA/bytes and exact row offsets/lineSHA/bytes, and compares complete actual TYPE and opaqueVALUE strings—not hashes alone. Every TYPE/universe/rawName/origin/axiom/default byte is exact; every VALUE is byteexact except the sole helper root in each context. Changed helper VALUE is exactly the compiled v6 candidate and differs independent and genuine proofs. Main/public/foreigncaller/allotherproject/helpers/generated/DATA values retained exact. There are546 distinct (Name,sourceOrigin/context) pairs and501 distinct actual Name strings across880 checked rows. Imported-context overlap334 is a different count from Name intersection379. No additional decoded VALUE exports made. All relevant compiler/native/build/semantic/host-parser jobs are terminal/drained before requesting AFTER HOLD.

Final findings, line packing, safe changes, all24audit/all42golf/all16binders+universe, independent proof/boundaries, fresh searches, static checks, holistic reflection and owner prose corrections are now resolved before expensive AFTER captures. No supported local recommendation deferred. Numeric after/buzz and closure gates remain pending; current main32 FAIL15 and historical/global/foreign failures remain explicit separate obligations.

## Context-count correction (preserved prior version)

Owner semantic verifier V1 completed both complete raw-context comparisons then FAILED its assertion that546 was the actual Name union; no owner acceptance from that run. My retained-pairs-v1 `union546_not880_distinct` field and earlier report wording were likewise ambiguous/incorrect as a Name-count claim. Their original artifacts remain intact; `report-before-count-correction-v1.md` preserves this report immediately before correction. Correct actual immutable before/after index counts:471 imported and409 direct rows;501 distinct actual Name strings (and rawName identities), intersection379, direct-onlyNames30. There are546 distinct (Name,sourceOrigin/context) pairs =471 imported+75 actual-local-source. Of75 actual-local-source Names,45 also occur in compiled471 under a different origin/context;334 imported rows duplicate across contexts. ALL880 actual rawrows remain individually guarded and checked; nothing is deduplicated or omitted. Full retained-pairs-v2 has re-run actual raw comparisons and certified these distinct count definitions. Source/compiler/profile reruns are unnecessary for this host-count correction. Owner independent semantic V2 PASS was reported after its complete raw/proof rerun; final closure/currentPS acceptance remains separately required.

## Final matched performance (actual completed and released)

NEW explicit owner AFTER HOLD ACK preceded every NEW AFTER phase adaptation/scaffold/probe/observer/capture. Existing disclosed P11 closure/Q15 manifest/completed BEFORE-drain reads really preceded ACK as closure planning; no contrary chronology claim. Owner remained idle through ALLfourcaptures/env/fullpre/percallprelaunch/fullpost/finalfreeze/drain. Driver29491 terminal0. Elevated full finaldrain terminal0, all1194 current-runtime manifest-bound groups absent, fullPSexit0/task+printenv0/source17exact. Actual ENTIRE completion notice preceded explicit owner RELEASE; AFTER rawparse began only after release. No sample gate inferred from exit0.

| Measured complete declaration scope | Before A/B ms | After A/B ms | Gate |
|---|---|---|---|
|private helper16|260.553 /254.744|204.025 /216.121|all samples<750 and<1000|
|attached complete main32|569.762 /508.575|467.113 /544.881|all samples<750 and<1000; headline proof32 stillFAIL15|
|separate complete foreign roth_of_isIntegral|3231.594 /3191.347|3154.765 /3111.414|VALIDFAIL≥1000 retained, preexisting separate Main obligation|

All eight captures retained, both samples per scope; no unchanged third/cherry-pick/noise/causal discount or causal speedup claim. Complete canonical attached doc/TYPE/body matches only whitespace/standalone-comment-layout normalization. Actual fresh Name.isPrefixOf families bind all kernel names (helper1, main2, foreign7), with actual compiler subsets including allowed empty. Complete disjoint column0 command+async proof/kernel/compiler/lint roots summed; Meta/nested/trailingend excluded, no subtraction or doublecount. Same CLI/default200000/20000/512/ownparent/fourbinaries/PATH/full actual env. Six full input observers per phase compare source17/cache104/root8/all14 complete setup fields/imports/package12202/core12592/four binaries and actual cache/root modes. Eight actual Lakeenv byte observations per phase equal24b49ef48be94515250ce23da9d4e052c055f67c4fea3f9197d482a8315a3484.

Matched host-v1 FAILED an overstrict across-build import-artifact catalog identity assertion, preserved; that12202 availability map also contains project MainLemma.olean, whose controlled old/new bytes differ. V2 successfully repeated complete validation with actual saved derivative binding; V3 tightens to literal ONE MainLemma.olean allowance in each import-availability map, plus explicitly enumerated cache7 and root1 derivative paths, preserving all other fields exactly. Every old/new SHA+byte tuple bound to actual full saved bytes. No broad catalog waiver or claim of all-catalog identity across builds; no new capture required for host schema repair. Final v3 matched receipt is authoritative.

Buzz outcome: FAST-BOARD for this helper’s leased scope; attached main numeric scope also below budget. Foreign existing multi-second failure and earlier GLOBAL failures remain explicit other-owner obligations, not waived or declared repaired. No concrete helper-change-related caller regression or necessary narrow caller repair established: Main source and all its actual TYPE/opaqueVALUE bytes remain exact. Raises removed0/added0; no additional local performance recommendation deferred; no fullMain/file buzz credit.

## Seven diff gates and explicit extra cumulative gate (final leased diff)

| Gate | Result | Actual evidence |
|---|---|---|
|lake_build_file|PASS|Actual `/Users/ramin/.elan/bin/lake build`, final-full-build-v1 exit0, source782; log explicitly Built Roth.MainLemma(17s) and Roth.Main(15s),2467jobs successful. This full build covers touched module; no invented separate module invocation.|
|definition_protected|PASS|Exact entry/current inverse changes only target lemma body+whitespace packing; all defs/abbrevs byteexact.|
|theorem_statement_protected|PASS|Full actual target TYPE/universe bytes exact genuine and exact original constructor roundtrip; main/public/caller/retained TYPEs exact.|
|structure_gate|PASS for leased helper|Body19≤30/maxbranch3≤10. CommonP correlated conjunction explicitly required by dispatch; separate existential witnesses rejected, no beneficial shared-P replacement established. Does not waive main32FAIL15.|
|naming_gate|PASS|Descriptive private exists_auxiliary_polynomial_of_log_bound_aux; no forbidden pattern/abbreviation; no rename queued/applied.|
|line_packing_gate|PASS|Every8 actual rows measured with complete arithmetic table; max100, final row44 includes delimiter, no repack rows.|
|inequality_orientation_gate|PASS|Eight actual occurrences table, zero≥/> in signature, no ge/gt name.|
|cumulative_no_unintended_external_breakage|PASS for leased change|Full project2467jobs, then separate Roth.LeanEval actual exit0; full unfiltered Main/Eval natives errors0, all880 retained opaqueVALUE/TYPE actual rows exact except helperproof; fresh actual call-site search Main565.|

Phase6 cumulative file-diff gates: lake_build_file PASS via actual full build above; lake_build PASS via same actual final-full-build-v1 invocation0/52.0779s; definition_protected PASS; theorem_statement_protected PASS; cumulative_no_unintended_breakage PASS via full actual Main native, separate Eval0/24.0855s and all retained values. Overall6b: PASS for this helper-only cumulative diff. This is NOT wholeMainLemma completion: original27 headline32FAIL15, genuine-original704/Main684 contracts, GLOBAL valid failures, later independent wholeFILE review and owner publication remain separate explicit obligations. Scope does not turn these failures into deferred local recommendations or a global certificate.

## Phase checklist (all11 verification items)

| Item | Result | Evidence |
|---|---|---|
|Step1 reference docs|PASS|Full installed skill/commands/required references read bounded; actual truncations separately qualified.|
|Step2 full audit|PASS|All24 items above.|
|Step2.5 mathlib search|PASS|Five actual fresh methods and raw source/tool records above.|
|Step2.6 generalisation|PASS|All16 binders+universe,2.6a–e, honest15failedprobes,12formalboundary proofs/nonself countercheck.|
|Step2.7 line packing|PASS|All8 rows actual arithmetic and v1→v2 delimiter erratum.|
|Step2.8 inequalities|PASS|All8 occurrences/zero≥/>.|
|Step3 golf|PASS|All42 explicit statuses; supported findings implemented.|
|Step4 reflection|PASS|Fresh whole-helper holistic/strategy review above, unavailable builtin tool qualified, no fictitious invocation.|
|Step5a diagnostics|PASS|Fresh strict final ML/Main/Eval success, nonpartial/nontimeout/errors0/faileddeps[], inherited protected warnings1/4/0 documented, no new target warning.|
|Step5b gates|PASS within lease|Seven+explicit extra cumulative table above; actual FULL→separateEval, retained values and matched target performance.|
|Step6a renames|PASS|None warranted/queued/applied; all preexisting queue5 entries remain untouched.|

## Worker6b result and phases5a/5b/7

Before34 helper lines→after27, saved7; proof23→19, saved4; signature11→8, saved3; maxbranch5→3. Seven code findings fixed: packing, hr₁ inline, hlogα inline, direct hA0 instead of hA1, redundant change deletion, terminal simp unsqueeze, final calc composition. Rules1.10/1.12/1.15/2.12/2.14 applied; existing constructive/dot/obtain/positivity forms retained. Additional production declarations introduced during this fresh audit0; API/caller source changes0; local rename/refactoring/decomposition recommendations deferred0. Comments preserved: target0of0, allnine file narrative comments byteexact. File docs/primary quotes/public main TYPE/Main source/all14 prior helpers/selector protected by exact source inverse and complete retained values. Phases5a/5b require no further supported change; existing projectEND queue belongs to owner.

Final recommendations implemented, including owner’s three precise prose corrections. No new source/compiler/native/profile calls are needed. New fresh independent wholeFILE review and original27/fullfile/project obligations remain owner-controlled and receive no credit here. Owner preclosure semantic/native/profile/static review and final administrative snapshot/closure acceptance are separate requirements; this report itself does not certify unfinished closure.

## Closure protocol (no pre-execution credit)

After owner preclosure acceptance and explicit ADMINHOLD/exact small immutable owner-file list, snapshot all specified owner files with exact tuple/fullread binding, leaving mutable live O paths outside the manifest. Then two genuinely fresh full byte/UTF8/binary-provenance streams over ALL current and available predecessor evidence/source/reference/generic8542/durable692logical645blobs(stored+decoded), exact historical aliases and exceptions. Exactly four self receipts excluded: manifest.json,second-rehash.json,final-seal.json,final-drain.json. Fresh elevated fullPS after second stream must bind all known current-runtime launches to actual manifested bytes, all groups absent/task+bare/resolvedprintenv0/source17exact. Final-seal.json records actual outcomes, counts and ALL8END (source,necessarycaller,report,artifacts,compiler,build,native,profile); actual FINAL releases all eight, zero calls/children. No claim that those prospective steps have executed appears here; owner independent THIRD/currentPS/final acceptance remains necessary before helpercomplete. After END all leaf source/artifacts immutable until explicit resume.

## Actual width100 #check packing reference

The existing successful candidate-contracts-v10 fixture914–915 executed `set_option format.width 100 in #check @Roth.exists_auxiliary_polynomial_of_log_bound_aux`. Its COMPLETE actual output below is copied from the immutable v10 raw log; no new compiler run or prettyprinter normalization is asserted. This is a reference for actual elaborated binder/dependent-type shape, alongside the separately measured full written-signature packing table. The seven API identifier #checks establish actual name/type availability and use in a fully VALUE-guarded helper, not separate VALUE guards on all seven library constants.

```text
@Roth.exists_auxiliary_polynomial_of_log_bound_aux : ∀ {f : Polynomial ℤ} {α A : ℝ},
  f.Monic →
    (Polynomial.aeval α) f = 0 →
      (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
        ∀ {m q₁ r₁ : ℕ},
          0 < m →
            ∀ (r : Fin m → ℕ),
              (∀ (j : Fin m), 0 < r j) →
                ∑ j, r j ≤ m * r₁ →
                  ∀ {δ : ℝ},
                    0 ≤ δ →
                      2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log ↑q₁ →
                        ∃ P ∈ Roth.RSet (↑q₁ ^ (δ * ↑r₁)) r,
                          Roth.gam δ f.natDegree m ≤
                              Roth.index ((MvPolynomial.map (Int.castRingHom ℝ)) P) (fun x => α) r ∧
                            ∀ (i k : Fin m →₀ ℕ),
                              |(MvPolynomial.eval fun x => α)
                                    ((MvPolynomial.map (Int.castRingHom ℝ))
                                      ((MvPolynomial.hasseDeriv i) ((MvPolynomial.hasseDeriv k) P)))| <
                                ↑(Roth.B₁ δ q₁ r₁) ^ (1 + 3 * δ)
```
