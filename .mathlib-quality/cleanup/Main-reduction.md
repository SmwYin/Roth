# Roth.reduction — dedicated original declaration 5 cleanup

Completed target only. Mathematical conclusion, all six binders, public name/metadata and imports preserved; exact full compiler TYPE matches the accepted genuine original TYPE. The accepted caller repair for eventually_div_rpow_lt is preserved. No project helper, axiom, limit raise, native_decide, or profiling scaffolding was introduced.

## References and baseline

Read installed lean4/mathlib-quality SKILL.md, full cleanup/cleanup-all workflows, golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, relevant style/naming/review-stage sections, and buzz/profiling references. Followed the owner binding header where its correlated-witness, lease, standard-default, no-self, and complete-build rules override the generic template. No Skill(simplify) invocation is claimed; fresh independent file-final review remains with the owner.

Entry reused actual same-source full build, separate Eval build, unfiltered native Main/Eval/root and complete Main diagnostics from /private/tmp/roth-main-eventual-power; no unchanged baseline replay was made. Genuine ORIGINAL and ENTRY snapshots were saved before any Lean/golf. Existing global five-rename queue was read but never modified.

### Auditing: `reduction` (L111–134, 24 declaration lines, 21 tactic-body lines (22 including := by))
1. LINT: none in target, reused complete same-source Main diagnostics from declaration4.
2. HAVE SCAN: hMR has by/cast proof, used once in positive scaling, removed after the passing positivity probe; hS no by used once, inline into image; hginj has by/injectivity proof used once, replace manual product ext with mathlib prodMap, then inline if readable; hqQ no by used once, inline at hQ₀; anonymous scaling equality has by/push_cast/ring proof used once, probe direct rewrites.
3. SET_OPTION: none, retain default limits.
4. SIMP SQUEEZE: [hg, Prod.mk.injEq] at hab nonterminal squeezed, eliminated by prodMap candidate; [hg] nonterminal squeezed, preserve unless direct unfolding makes unnecessary.
5. NAMING: reduction is snake_case, no forbidden patterns/abbreviations or scheme number. Namespace plus source outline explicitly identify reduction to algebraic integers. No rename needed or queued.
6. LINE PACKING: L111 91 chars + next full binder 33 +1 =125, justified; L112 39 + next existential binder 14 +1=54, repack. L113 94 chars final. Final table to be remeasured after edit.
7. BY PLACEMENT: ends signature, fine.
8. FORMAT: three mathematical lambdas use =>; the map/injection lambdas were eliminated and the threshold lambda now uses ↦; no empty internal lines or haveI/letI, no sequential rw pair.
9. COMMENTS: no inline proof comments; retain all source citation text.
10. DOCSTRING: existing describes reduction, distinguishes previous integrality-only lemma. Add application tip: resulting exponent can be smaller, which matters when applying the algebraic-integer theorem.
11. VISIBILITY: public proof-outline result, keep public contract/metadata; not a cosmetic private helper.
12. STRUCTURE: 21 tactic-body lines <30; no case branches; conjunction inside ∃ correlates one α',κ' witness and must not be split into unrelated existential facts. No helper required.
13. MATHLIB: partial matches LiouvilleWith.nat_mul (different approximation predicate), Function.Injective.prodMap replaces manual componentwise product cancellation. No new wrapper.
14. JUNK DEF: n/a theorem.
15. EXISTS LEMMA: n/a substantial public reduction, not private trivial witness.
16. SHOW vs CHANGE: show exponent-gap is a term annotation needed for implicit κ', not a tactic-mode goal rewrite.
17. PUSH_NEG: none.
18. GENERALISE: all six parameters classified below; drop/weak probes completed in bounded scratch probes, no ambient-domain expansion.
19. INEQUALITY: signature hκ and witness exponent both use <; no ≥/>. Arrow => is not an inequality.
20. NORMAL-FORM: Set.Infinite and IsIntegral are canonical existing predicates. LiouvilleWith would change interface and require approximation equivalence; retain current canonical pair-set contract.
21. SYNTAX-GEN: OK: consumer obtains a correlated algebraic integer and exponent in one obtain, exactly matching integer theorem.
22. IMPORT-FANOUT: n/a no new import proposed.
23. CASTS: 0 redundant casts dropped; 4 cross-type value casts kept in changed lines (M→ℤ, M→ℝ, twice q→ℝ); 2 load-bearing annotations kept (nonzero proof fixes the ℤ map and positivity fixes the ℝ order); removed casts belonged to eliminated intermediate statements.
24. INSTANCE-NAME: n/a no instances declared.

### Mathlib search-status
[A] Lean-Finder: integer scaling/irrational algebraic integer/infinite rational approximations → LiouvilleWith.nat_mul/mul_nat/mul_int partial matches.
[B] Loogle: Function.Injective (Prod.map ?f ?g) → Function.Injective.prodMap, Prod.map_injective.
[C] LeanSearch: injective product map → Function.Injective.prodMap/Embedding.prodMap.
[D] rg full names in Mathlib/Data/Prod/Basic and Algebra/GroupWithZero/Defs → Injective.prodMap, mul_right_injective₀, mul_left_injective₀; denominator algebra from Group/Basic mul_div_assoc.
[E] lean_local_search Prod.map_injective → source hit (index unavailable, not used as absence evidence).
Auxiliary variants: prodMap/map_injective, mul_right_injective₀/mul_left_injective₀, nat_mul/mul_nat/mul_int. Common-equivalents table: finite set removal matches Set.Infinite.sdiff, already used. Conclusion: partial matches, keep substantive reduction and use mathlib product injection directly. No absence claim from searches alone.

### Generalisation status (pre-experiment candidate record)
| Parameter | Class | Use | Candidates |
|---|---|---|---|
| {α : ℝ} | structure value | approximation/Irrational/integrality | drop binder leaves free α; fixed Real structure supplies real powers and irrationality, no typeclass/universe variable to weaken |
| hα | proposition | natCast_mul | drop; no point-localisation catalogue form for Irrational |
| halg | proposition | exists_nat_mul_isIntegral | drop; already IsAlgebraic, not stronger IsIntegral |
| {κ : ℝ} | structure value | approximate exponent/midpoint | drop binder leaves free κ; no polymorphic universe/typeclass parameter |
| hκ | proposition | midpoint exponent bounds | drop, weaken to 2 ≤ κ (endpoint κ=2 prevents strict midpoint) |
| hinf | proposition | sdiff/image infinite set | drop; weaken to Nonempty cannot yield Infinite via finite removal |
No decidability/universe/typeclass binders; no global pointwise-function hypotheses.
Inversion check: approxSet remains throughout tail membership; generic infinite-image fact is already mathlib; abstracting all target-specific scaling would be an optional companion, not necessary.

### Inequality scan
| Location | Original | Rewrite | Rename |
|---|---|---|---|
| signature/hypotheses | n/a: zero ≥/> occurrences | none | none |


## Final action resolution

The original hMR/hS/hginj/hqQ/anonymous equality are all eliminated. Mathlib's nonzero left multiplication injection and Injective.prodMap feed Infinite.image directly. One dsimp only unfolds Prod.map/id; push_cast crosses the integer/real bridge once; four named algebra/absolute-value rewrites expose positive scaling. The two-step strict calc preserves the distinction between the original approximation estimate and exponent-gap bound. The docstring now warns that the output exponent may be smaller.

### Generalisation status — completed

| Parameter | Class | Used as | Mechanical candidates actually tested | Verification/result |
|---|---|---|---|---|
| {α : ℝ} | structure value | real irrationality/approximation/integrality | no class-parent/universe parameter; deleting the value binder under autoImplicit reintroduces the same binder | n/a: abstracting Real changes irrationality/real-power API and is outside authorized ambient-domain scope |
| hα : Irrational α | proposition | natCast_mul | remove hα | DropProbes exit1 at hα.natCast_mul; restored; local α=0 scaling counterexample passes separately |
| halg : IsAlgebraic ℚ α | proposition | integral-multiple input | remove halg | DropProbes exit1 at halg; restored; already weaker than IsIntegral, no point-local catalogue form |
| {κ : ℝ} | structure value | exponent and midpoint | no class-parent/universe parameter; deleting name reintroduces same implicit real binder | n/a: concrete real exponent is part of approxSet and Real.rpow contract |
| hκ : 2 < κ | proposition | strict midpoint upper/lower bounds | remove; replace by 2 ≤ κ | DropProbes exit1 at both strict midpoint obligations; restored; Subproofs-v2 proves endpoint midpoint is not >2 |
| hinf : (approxSet α κ).Infinite | proposition | Infinite.sdiff/image | remove hinf | DropProbes exit1 at hinf.sdiff and residual infinite goal; restored; no typeclass/global-function localisation candidate |

Verified means the bounded scratch substitution actually ran, not that a false theorem was certified. No failed proof-dependency probe is claimed to establish logical necessity. No weakening kept. No optional big-change candidates or helpers proposed. The proof uses approxSet throughout; generic finite-removal/image transport is already supplied by mathlib.

### Literature search status

Query: `Roth theorem reduction algebraic integers multiply integer approximation exponent generalization`.
Top three surfaced hits were Math StackExchange's generalisation question, Wikipedia's Roth theorem page, and Eduard Valcarce Dalmau's thesis. Mathematical conclusions rely on primary expositions and the local source, not the discussion page: [Milojevic, An elementary approach to Roth's theorem](https://aleksa-milojevic.github.io/expository/roth.pdf) and [Valcarce Dalmau, Diophantine Approximation in the framework of Roth's Theorem](https://diposit.ub.edu/bitstreams/8cfc8916-c376-44d7-8822-14f9fed3aa15/download). Evertse's notes were attempted but the web tool could not access the PDF. The primary expositions support the usual reduction to algebraic integers; number-field generalisations introduce heights and different approximation objects, so they do not justify a mechanical real-parameter weakening here. The local clean.tex §6 explicitly separates the three preceding helpers and then performs this same correlated scaling argument. No new broad literature/API loop was opened. ChatGPT math MCP: n/a, no such tool is available. Literature-driven mandatory changes: none.

### Line packing (codepoints)

The width100 #check @reduction output in Subproofs-v2.stdout is the compiler reference; its nested forall/exists display agrees with the existing binder structure.

| Initial signature line | Chars | Next whole binder/token | Arithmetic | Action |
|---|---:|---|---|---|
|111|91|(hinf : (approxSet α κ).Infinite),33|91+1+33=125>100|ok|
|112|39|∃ (α' κ' : ℝ),14|39+1+14=54≤100|repack, applied|
|113|94|none|n/a|ok|

| Final signature line | Chars | Next whole binder/token | Arithmetic | Action |
|---|---:|---|---|---|
|112|91|(hinf : (approxSet α κ).Infinite),33|91+1+33=125>100|ok|
|113|97|(approxSet α' κ').Infinite := by,32|97+1+32=130>100|ok|
|114|36|none: proof body follows|n/a|ok|

### Inequality orientation scan — final

| Location | Occurrence | Rewrite | Rename |
|---|---|---|---|
|signature hκ|2 < κ|none|none|
|signature correlated witness|2 < κ'|none|none|
|term exponent annotation|(κ + 2) / 2 < κ|none|none|
|positive scaling calc|M * abs(...) < M / q^κ|none|none|
|positivity annotation|0 < (M : ℝ)|none|none|
|last exponent-gap calc|M / q^κ < 1 / q^((κ+2)/2)|none|none|
|≥/> scan|n/a: zero such Lean-code occurrences|none|none|

### Golfing-rule pass (all 42 rules)
1.1 n/a: no by-exact wrapper in retained proof; positivity is an actual tactic.
1.2 n/a: no by-rfl.
1.3 n/a: no rw followed by exact; rewrite chain precedes strict estimate.
1.4 applied: scaling estimate transported directly with simpa only [mul_one_div].
1.5 n/a: no trailing rfl.
1.6 already anonymous constructor for correlated witnesses and membership.
1.7 n/a: no apply/exact pair.
1.8 n/a: no contradiction/negation pair.
1.9 applied through Function.injective_id in prodMap, no eta-expanded identity.
1.10 applied: hS and hqQ inlined; hginj replaced by direct mathlib proof and inlined; hMR removed using positivity at use.
1.11 n/a: rintro destructs an image witness rather than an apply/intro pair.
1.12 retained term-mode show: gives implicit exponent κ' to eventually_div_rpow_lt.
1.13 eliminated original hab.1/hab.2 product-ext proof by Injective.prodMap.
1.14 applied: direct rw chain [mul_div_assoc, ← mul_sub, abs_mul, Nat.abs_cast] replaces scaling equality have and its rewrite.
1.15 n/a: no terminal `simp only` tactic; final `simpa only [mul_one_div]` is a single-lemma transport of a supplied inequality.
1.16 n/a: no bare nonterminal simp; dsimp only targets Prod.map/id, then push_cast normalises genuine casts.
1.17 applied: .prodMap/.injOn/.image/.mono compose existing APIs.
1.18 n/a: remaining parentheses fix method receivers, type annotations or implicit proof arguments; no trailing whole lambda/proof parens removable by <|.
1.19 n/a: no push_neg.
1.20 n/a: public substantive existential reduction, not a trivial private witness helper.
2.1 tried whole proof at actual L114, grind fails existential algebraic-integer reduction; also failed remaining infinite-image goal at L118. No grind retained.
2.2 n/a: no retained grind.
2.3 applied: simpa single-lemma transport replaces separate ring equality in calc.
2.4 n/a: no function-property goal.
2.5 applied: standalone positivity probe passes for natural cast; replace hMR cast proof by positivity at scaling use.
2.6 tried: standalone scaling monotonicity gcongr succeeds; retained explicit mul_lt_mul_of_pos_left names the positive scaling argument equally briefly and avoids search.
2.7 n/a: midpoint inequalities are real, not Nat/Int linear goals; no Nat/Int arithmetic block beyond cast nonzero.
2.8 tried whole proof at actual L114, aesop leaves correlated existential; image-tail aesop also fails. No aesop retained.
2.9 tried: norm_num proves the endpoint midpoint counterexample; exact_mod_cast remains the one-step ℕ→ℤ nonzero bridge, push_cast handles ℤ→ℝ product.
2.10 n/a: theorem ranges over arbitrary reals/infinite sets; not a finite decidable computation.
2.11 tried scaling equality: field_simp alone closes it (following ring produced truthful no-goals error, removed in passing Subproofs-v2). Direct named rewrites chosen instead, with no denominator case split.
2.12 tried scaling equality: push_cast; linear_combination succeeds in Subproofs-v2; direct mul_div_assoc/mul_sub rewrites are clearer and remove auxiliary equality entirely.
2.13 n/a: no symmetric cases.
2.14 applied: eliminated calc's equality step by transporting positive scaling directly; remaining two strict steps show approximation estimate followed by exponent gap. A composed .trans term would retain the same long transport without improving clarity.
2.15 n/a: witness refinement has one remaining mathematical membership goal; no duplicated closing branches.
3.1 n/a: no erw.
3.2 n/a: no continuity/measurability.
3.3 n/a: no omega and no integer linear arithmetic tactic.
3.4 already image witness destructured with rfl, no later substitution rewrite.
3.5 n/a: theorem is a contextual existential reduction; no canonical simp/grind normalization attribute warranted.
3.6 n/a: no simp_all only.
3.7 n/a: no local/global resource option introduced or retained by this target.

### Step-back reflection
Whole proof grind/aesop/exact? failed on the actual pre-declaration context; apply? on the infinite-image stage gave only partial generic infinity reformulations, not a proof. Search found a useful smaller API (prodMap), not a replacement of the correlated reduction. A term-mode monolith would hide witness choice and image membership. The independent check uses a different exponent witness `(κ + 6) / 4`; no new project helper, alternate ambient domain, or later Roth theorem is needed.

### Generalisation experiment results
Actual bounded DropProbes.lean (exit1 by design) removes each proposition separately and tests hκ weakened to 2 ≤ κ. hα fails at natCast_mul, halg at integral-multiple input, hinf at sdiff, hκ dropped/weak at both strict midpoint bounds. These are proof-dependency failures, not claims that all logically stronger global conclusions are false. Subproofs-v2 (exit0) certifies local counterexamples: κ=2 gives midpoint 2, rational α=0 is not irrational after multiplication by 1, and multiplying numerator by M=0 is not injective. α/κ are fixed real value binders needed in the predicate/type, not typeclass/universe assumptions; dropping their names under autoImplicit would silently reintroduce the same parameters. No point-localisation or typeclass-parent catalogue entry applies. No weakening kept.


## Actual verification and gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file / FULL | PASS | run.py final-full-build: actual `lake build`, exit0,60.784s; Main and root rebuilt,2467 jobs |
| separate Eval build | PASS | after FULL: actual `lake build Roth.LeanEval`, exit0,31.991s;2466 jobs |
| complete unfiltered native Main/Eval/root | PASS | launch/terminal+stdout/stderr artifacts; exits0,33.664/29.802/26.549s; driver terminal all0 |
| complete Main LSP | PASS | final-Main-lsp.json: partial=false,success=true,0errors;4existing outside-target warnings at1/307/448/449 |
| definition_protected | PASS | focused entry diff changes no def/abbrev |
| theorem_statement_protected | PASS | declaration keyword/name line unchanged; only signature wrapping; strict full TYPE equality including Names, universes, BinderInfo, metadata |
| structure_gate | PASS | 14 tactic-body lines (15 including :=by), no cases; membership tail7lines; correlated existential conjunction preserved under binding header |
| naming_gate | PASS | reduction is valid snake_case, no forbidden abbreviation/pattern; mathematical role explicit in namespace and proof outline; no rename queued |
| line_packing_gate | PASS | all3 measured final signature rows ok |
| inequality_orientation_gate | PASS | zero ≥/> in statement/hypotheses/body; no _gt_/_ge_ name |
| standard axioms / trust | PASS | actual opaque production+fresh independent VALUES inferred/closed; only propext/Classical.choice/Quot.sound; defaults200000/20000/512 |
| cumulative dependents | PASS | actual FULL plus separate Eval plus unfiltered Main/Eval/root; no caller/API change |
| no scaffolding / limits | PASS | production diff contains no option/trace/count_heartbeats/sorry/axiom/native_decide/import changes |

Overall: PASS. No build deferral or decomposition flag.

New references were confirmed by actual compiled candidate/subproof/production use, plus source searches: mul_right_injective₀ in Algebra/GroupWithZero/Defs, Function.Injective.prodMap in Data/Prod/Basic; Function.injective_id, Prod.map, id, mul_div_assoc, mul_sub, mul_one_div all elaborated in the passing proof. Positivity, gcongr, linear_combination and field_simp were actually tested in Subproofs-v2 (exit0). These do not rely on guessing an unverified lemma name.

### New-identifier verification

| Identifier | Verified via | Result |
|---|---|---|
|mul_right_injective₀|full source match in GroupWithZero/Defs and Probe-v4/native compile|PASS|
|Function.Injective.prodMap|Loogle/LeanSearch, Data/Prod/Basic source, Probe-v4/native compile|PASS|
|Function.injective_id|Probe-v4 and actual production native compile|PASS|
|Prod.map / id|Probe-v4 dsimp and actual production native compile|PASS|
|mul_div_assoc / mul_sub|Probe-v2/v4 and actual production native rewrite|PASS|
|mul_one_div|Probe-v4 and actual production native simpa|PASS|
|positivity|Subproofs-v2 and actual production native compile|PASS|

## Semantic evidence / no-self closure

Genuine old target source is bound exactly (modulo declaration-name and accepted old-helper rename) to the already compiled originalCallerReplay in RothMainEventualPowerReplay.lean/.olean. Its full actual TYPE/VALUE, default/standard/closed/inferred/no-current-target/no-cycle checks are reused from declaration4's actual valid raw v4 rows plus supplement; see genuine-original-reuse.json. No unchanged original/helper proof was recompiled just for a fresh label.

A fresh independentReduction proof uses the alternate exponent `(κ+6)/4`, with a complete source-level scaling/image proof. IndependentReduction.olean compiled exit0,32.861s. Semantics.lean then imported this small proof fixture and inspected current production/independent actual opaque VALUES in memory: root TYPE exactly equals the accepted compiler Expr by strict constructor recursion including Names, levels, BinderInfo and metadata; no Expr.BEq shortcut or hygienic exception was needed. Actual families were singleton `[Roth.reduction]` and `[independentReduction]`, each with its actual universe list `[]`; no blanket universe assumption was placed on other declarations. VALUES had repr lengths2168246 and5108581 bytes, respectively; only hash/length receipts are persisted from this in-memory proof check, so this report does not claim those full semantic raw VALUES were persisted. The profile separately emits its actual full prefix VALUE.

Actual proofs contain no open term/level metavariables, free variables, loose binders, sorryAx or nonstandard axioms. The recursive graph permits only accepted preceding approxSet/exists_nat_mul_isIntegral/approxSet_den_le_finite/eventually_div_rpow_lt families in Main, denies target use from the independent/preceding closure, denies all later Main constants including completed Roth's theorem, checks local acyclicity and strictly upstream external module origins. Standard default option checks passed. Semantics process exit0,53.801s; semantics.stdout and semantics-receipt.json carry the small receipt and origin graph. No proof VALUE identity was required between different proofs or module contexts.

## Focused profile acceptance

Owner ACKed whole-phase HOLD before preparation and explicitly RELEASEd only after all five profile launches were terminal0/groups absent, source/tool freeze exact and both before/after defaults/environment checks passed. Full environment bytes were compared only in memory; persisted data is hash/length plus approved toolchain/path fields. No unrelated process arguments were collected. Historical original source/context differs from ENTRY because the preceding helper API was cleaned earlier; no speedup ratio or causal comparison is claimed.

Historical genuine-original row605.368ms = command17.449 + proof520.547 + kernel-parent13.764 + lint53.608. Nested kernel12.825ms is not added again, compiler roots absent. The indexed narrow full-canonical row matches the saved genuine original target exactly; historical-profile-row.json reuses the all17 index/raw binding and offsets without reparsing the317MB historical raw trace. This is separately scoped historical evidence, not an ENTRY-source timing.

Final exact-source prefix score331.730ms = command15.477 + proof294.970 + kernel-parent9.161 + lint12.122. Nested kernel9.099ms is included within its parent and not double-counted. Actual family singleton Roth.reduction, compiler roots0, lazy prior DATA roots0. Full emitted canonical doc/signature/body matched the target command; full TYPE/universes match the production guard; actual full VALUE was emitted by the prefix compiler. No VALUE identity across module contexts is asserted. `--profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0` output was streamed after explicit RELEASE with raw checksum/length verification.331.730<750<1000, so no extra unchanged capture was made. See final-profile/target-profile-acceptance.json, prefix-binding.json, profile-family-map.json and phase-complete.json. Outcome FAST-BOARD, no deferrals, no limit raises.

## Failed experiments preserved truthfully

The first scratch extraction accidentally started inside the docstring: Probe-failed-extraction.lean/log, exit1, no proof credit. An early L112 LSP replacement targeted signature syntax, and an L120 whole-have replacement left stale inner tactics; these discarded position experiments are not counted as successful automation. Whole-proof tactics were subsequently tested at the actual first tactic L114 and failed substantively. Probe-v3 failed because Prod.map projections needed unfolding; Probe-v4 added only dsimp and passed. Subproofs initially had a trailing ring after field_simp had already solved the equality; Subproofs-v2 removed that redundant tactic and passed. The first independent olean invocation lacked -R and was rejected before elaboration; adding the correct scratch root produced independent-build-v2 exit0. DropProbes exit1 is expected negative evidence, not a failed final gate. No failed scratch result was relabelled as a whole pass.

## Result and handoff

Declaration24→17lines; tactic body21→14 (or22→15 including :=by). Target including doc/trailing separator30→24lines; the net source savings is6lines because one documentation line was added. Audit issues found:6; fixed:6; refactoring deferred:0. Issues fixed: inline single-use facts, use product-map API, remove intermediate ring identity/extra calc equality, compact signature, document exponent loss. No refactoring deferred; no new renames; comments preserved (none were present in the proof); full source citation retained.

Phase checklist: Step1 references✓; Step2 all24items✓;2.5 actualfive-method search✓;2.6 bounded generalisation/literature✓;2.7 allsignaturewidths✓;2.8 inequalitytable✓;Step3 all42rules✓;Step4 reflection✓;5a completeLSP✓;5b actualbuild/diffgates✓;6a renamequeueunchanged/no newrename✓. File-final holistic review is assigned to the owner, not falsely reported as Skill(simplify).

### Source bindings

| Artifact | Bytes | SHA256 |
|---|---:|---|
|/Users/ramin/LEAN/Roth/Roth/Main.lean|36269|84c2a9dc00bab32468251e3a83bc4be7944bd2b3e933553d64e7170e362e8dd2|
|/Users/ramin/LEAN/Roth/Roth/LeanEval.lean|3010|610ec95658c5d43c931217bfb56b54d62f825473de17b3bdf6a1dde85dd900ca|
|/private/tmp/roth-main-reduction/entry-Main.lean|36491|4fbecf03eddef02596d342333df93856519d7c01fdc27f3104e024693a7cb2c5|
|/private/tmp/roth-main-reduction/genuine-original-target.lean|1665|33383b932fc4b6fd81d1fb71a60af46b0e4573f053fa0658b5b5f93023a75582|
|/private/tmp/roth-main-reduction/entry-target.lean|1670|64c01f804f7447f946d47b387b0c101a962b57ac665d1f1a29b182190677cf89|
|/private/tmp/roth-main-reduction/final-target.lean|1448|e20f316328084cf7e32b4d191ef52da72ce6d6035f9f0b466dc832518ab4be08|

### END / drain / leases

final-drain.json checks all19 known task launch groups absent and every corresponding launch terminal (including truthful failed experiments); native, semantics and profile drivers are terminal. Initial direct extraction-probe session55579 is also terminal exit1. All LSP queries completed; no pending tool calls/compiler/native/profile jobs. All target/report/compiler/native/LSP/profile leases released to the owner. No next target edited; no Git/shared queue/progress writes. FINAL: target5 authorized closure complete, ready for independent owner acceptance/publication.
