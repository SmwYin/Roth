# Phase 4 — Roth.eventually_div_rpow_lt

Scope: target declaration and necessary argument repairs in Roth.reduction and LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff. The initial sole-caller premise was corrected by the required separate Eval build: its actual first failure revealed the second caller, and the owner extended the lease for exactly that repair.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md, plus the installed Lean4/mathlib-quality SKILLs, relevant style and naming sections, actual cleanup/cleanup-all/buzz workflows, profiling measurement/diagnosis guidance, and the local paper's §6 reduction (clean.tex1140–1195). No agents were spawned by this worker.

## Preservation and baseline

Before any Lean experiment or golf, genuine original and exact worker-entry target were preserved in /private/tmp/roth-main-eventual-power/{genuine-original-target,entry-target}.lean. Both are identical 16-line declarations; SHA256 without final newline 588f0df35dece5cbc48263fab808660595eb311160bbbacb4b5c98b192201b18. Full entry Main snapshot also preserved, SHA999255051da3539de61e05aa13f71d0f1c3e161dcfd6cd5dad50b6d112514f48. Genuine Main-project-original.lean is the owner-supplied 684-line original, not a golfed replay substitute. The exact original target and Main caller full TYPE+VALUE raw rows were read by indexed narrow byte slices from the accepted after-imported-pairs-v1 log; row checksums validated.

Reused owner-accepted same-source entry FULL build64.762984s and separate Eval32.880271s; this worker did not relabel or repeat those as its own baseline. Actual entry complete unfiltered Main LSP diagnostics: success, partial=false, timed_out=false, 0 errors and the four existing unrelated warnings at1/321/462/463. No target warning.

Mathematics: a positive exponent gap δ=κ−κ' makes q^δ diverge past every fixed real M. The quotient inequality follows for positive q by rpow_sub. No positivity of M is needed. This is the same fixed-factor absorption used in the paper's reduction; the positive multiplier in that reduction is still needed elsewhere and remains available.

### Auditing: `eventually_div_rpow_lt` (entry lines 97–112, 16 lines)

1. LINT: actual complete unfiltered Main diagnostics succeeded; no target warnings. Four unrelated input warnings remain at 1, 321, 462, 463.
2. HAVE SCAN: `he0` (99, by proof, 2 references) keep mathematical gap; `hq1` (101, no by, 2 uses at 102/104) keep; `hqpos` (102, no by, 4 uses at 107/110/112) keep; `hMq` (103–105, by proof) keep mathematical bound; anonymous `this` (104, no by, 1 use at105) inline candidate; `hsplit` (106–109, by proof) remove through direct rpow_sub API. Final alternative may replace entire construction.
3. SET_OPTION: none.
4. SIMP SQUEEZE: no simp calls in original target.
5. NAMING: descriptive snake_case for eventual division by real powers and strict comparison; no forbidden patterns/abbreviations, `_ge_`, `_gt_`, or numerical scheme. No rename necessary.
6. LINE PACKING: entry signature rows below; conclusion is a whole expression that cannot share first line. Final remeasure required.
7. BY PLACEMENT: all bys end their preceding lines.
8. FORMAT: replace lambda `=>` with `↦`; two-space proof indent, four-space signature continuation; no blank proof lines or haveI/letI.
9. COMMENTS: no inline proof comments; preserve Source citation and mathematical content.
10. DOCSTRING: public asymptotic estimate documented with paper §6; if M positivity removed, state arbitrary M and applicability when absorbing fixed scaling by sacrificing exponent.
11. VISIBILITY: retain public reusable real-power comparison, explicitly in authorized target scope; not a new implementation helper.
12. STRUCTURE: original 14 proof lines, no conjunction or case branches; within ordinary 30-line bar. No helper extraction needed.
13. MATHLIB: partial match `tendsto_rpow_atTop`; use limit API with explicit eventual-to-Nat threshold and elementary quotient/rpow conversion. No exact one-step equivalent found by compiled exact?/apply?. See five-method block.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: n/a, public nontrivial asymptotic estimate, not a trivial private witness wrapper.
16. SHOW vs CHANGE: none in target.
17. PUSH_NEG: none.
18. GENERALISE: test removal of M sign assumption first; direct limit construction is sign-independent. Strict exponent gap cannot weaken globally: κ=κ'=0, M=1 gives strict self-comparison for every denominator. Real parameters occur in conclusion; dropping their binders would leave ill-scoped expressions. No typeclass/global-pointwise/universe hypotheses exist. No optional field generalization.
19. INEQUALITY: zero reversed inequality tokens, table below; no lemma-name rename.
20. NORMAL-FORM: natural-number threshold existential matches caller; underlying mathlib canonical limit is atTop rpow divergence; keep conclusion and explicit threshold shape.
21. SYNTAX-GEN: remove unnecessary sign witness so callers supply exponent gap only; retain implicit M and exponent arguments.
22. IMPORT-FANOUT: n/a, all proposed API already available under exact production imports.
23. CASTS: natural-to-real casts in denominators are genuine cross-type; hq0 explicitly fixes real comparison for positivity. Final diff audit to be repeated.
24. INSTANCE-NAME: n/a, no instance declaration.

Issues to fix: (1) unnecessary positivity on M, subject to compiled general proof; (2) inverse-power threshold/rpow multiplication/split boilerplate replaced by existing divergence/subtraction API; (3) lambda arrow formatting and accurate docstring after generalization.
Refactoring needed: none outside the two authorized necessary caller argument adaptations.

### Line packing — entry

| Sig line | Chars | Next semantic signature token | Arithmetic | Action |
|---|---:|---|---|---|
|97|78|entire existential conclusion through `:= by`, 68 chars without indentation|78+1+68=147>100|ok|
|98|72|no next signature line|n/a|ok|

Reference: actual width-100 #check will be captured with final profile observation.

### Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
|1|signature and every hypothesis|n/a: zero ≥/> tokens|none|none; name has neither `_ge_` nor `_gt_`|

### Mathlib search-status

[A] Lean-Finder: “For real exponents a < b any real constant M is eventually smaller than x^(b-a) at infinity” → tendsto_rpow_atTop, NNReal counterpart, natural-power little-o, rpow-exp partial matches.
[B] Loogle: `Filter.Tendsto (fun x : ℝ => x ^ _) Filter.atTop Filter.atTop` → exact divergence building block tendsto_rpow_atTop.
[C] LeanSearch: “real rpow ratio tends to zero at infinity when exponent smaller” → tendsto_rpow_neg_atTop and unrelated geometric limits.
[D] Source grep: rpow/atTop declarations and little-o/rpow variants in Pow/Asymptotics; rpow_sub in real-power API; eventual_gt_atTop and Nat cast limit.
[E] Local name-pattern: tendsto_rpow_atTop → source hits verified, symbol index unavailable (not used as absence evidence).
Auxiliary variants: negative exponent, natCast composition, eventually_gt_atTop, eventually_atTop, rpow_sub, rpow_add, rpow_mul.
Common equivalents lookup: no discrete/finite/bounded bucket applies.
Concluded: partial match; preserve target API as a threshold/quotient estimate and build on mathlib divergence. Whole-goal `exact?` failed; `apply?` supplied only generic logical constructors and partial filter formulations, no matching proof. No blanket absence claim.

### Literature search status

[A] Web queries: power functions asymptotic comparison x^a little o x^b a b; NIST DLMF asymptotic scale powers; DLMF power function asymptotic real exponents. Top relevant sources: MIT OCW Course Notes Week 8 (Lemma7.2 powers little-o, https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2005/0287cc25b80969d0e83c5ea3e854c227_ln8.pdf); NIST DLMF §2.1 asymptotic scales (https://dlmf.nist.gov/2.1); Mathlib official source (local exact version) `tendsto_rpow_atTop`. Other retrieved hits include LibreTexts 13.7 (same MIT material), Wikipedia asymptotic analysis, and NIST unrelated special-function expansions; no theorem relied upon from irrelevant hits.
[B] ChatGPT math MCP: n/a, no such tool in enabled tool inventory.
Insight: exponent-gap positivity ensures divergence against every fixed real constant; M positivity is unnecessary. The local paper's reduction uses positive M for scaling but this isolated comparison does not. No ambient-structure expansion recommended.

### Generalisation status — final intended API

| # | Parameter | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
|1|`{M : ℝ}`|structure value|numerator and threshold comparison|binder drop is not a weakening: M remains in conclusion; arbitrary signed value checked by universal proof|yes, bounded compiled universal-M probe|retain implicit value; no sign needed|
|2|`hM : 0 < M`|proposition|old rpow_mul nonnegativity|drop first (weakest); weak `0 ≤ M` follows as specialization|yes, universal proof compiled|drop; both zero and negative values covered; original positive contract recovery audited|
|3|`{κ : ℝ}`|structure value|denominator exponent|binder drop leaves κ in conclusion; no typeclass parents/pointwise/universe candidates for fixed ℝ|yes, bounded universal real exponent proof|retain real exponent|
|4|`{κ' : ℝ}`|structure value|comparison denominator exponent|binder drop leaves κ' in conclusion; no point-localization/universe candidates|yes, same universal proof|retain real exponent|
|5|`hκ : κ' < κ`|proposition|positive exponent gap|drop; strict→weak endpoint|yes, compiled κ=κ'=0 and M=1 counterexample|cannot weaken globally; retain strict gap|

No ambient typeclass, decidability, universe, continuity, monotonicity, or bundled structure hypotheses exist. Inversion check: no distinguished concrete named witness is unfolded; theorem already concerns arbitrary real values. Big-change candidates: none recommended; optional ambient-field/API expansion expressly outside scope. User/owner authorized evidence-based M-sign removal and required caller repairs.

### Golfing rule pass

Phase 1:
- [1.1] by exact wrapper: n/a, none.
- [1.2] by rfl: n/a, none.
- [1.3] rw+exact→rwa: final rw changes the goal before hN is applied; `rwa ...` at hN would require specializing it and is less direct. Original existing rwa already appropriate.
- [1.4] simp+exact→simpa: n/a, no simp in final proof.
- [1.5] trailing rfl after simp: n/a.
- [1.6] constructor+two exacts: n/a, existential already refined directly.
- [1.7] apply+exact: n/a, no such sequence.
- [1.8] by_contra+push_neg: n/a, none.
- [1.9] eta reduction: final lambda introduces threshold-specific q/hq; not eta-redex. Lambda arrow updated to ↦.
- [1.10] inline no-by single-use have: original anonymous rpow comparison, hsplit, hMq, hq1 removed with entire inverse strategy; remaining hq0 is a by proof reused twice; no remaining applicable have.
- [1.11] apply+intro: n/a, refine existential plus lambda already used.
- [1.12] redundant show: n/a, none in target.
- [1.13] have+.1/.2→obtain: n/a, original has no projection chain; final obtains N/hN directly from filter eventuality.
- [1.14] merge rw: n/a, original has no consecutive rw calls to merge; the final strategy combines quotient/rpow transformations in one rw call.
- [1.15] unsqueeze terminal simp only: n/a, no simp.
- [1.16] squeeze nonterminal simp: n/a, no simp.
- [1.17] dot notation: used .comp, .eventually_gt_atTop, .trans_lt, .le; sub_pos.2 already standard direction accessor.
- [1.18] `<|` over parentheses: n/a, chained limit/composition grouped for the receiver, no merely trailing grouping to eliminate.
- [1.19] push_neg→push Not: n/a, none.
- [1.20] trivial private existential helper: n/a, none and no helper introduced.

Phase 2:
- [2.1] whole-proof grind: actual bounded LSP multi_attempt failed, ∀ threshold negation could not contradict exponent gap.
- [2.2] delete tactics before grind: n/a, final proof contains no grind.
- [2.3] simpa consolidation: actual whole-goal simp left threshold existence unresolved; final exact hN directly matches after rw, no simp consolidation needed.
- [2.4] fun_prop: n/a, no continuity/differentiability/measurability goal.
- [2.5] positivity: original base/rpow nonnegativity already used positivity; independent inverse proof retains it. Final gap uses exact sub_pos.2 and q positivity crosses Nat→Real once, avoiding positivity search.
- [2.6] gcongr: n/a in final proof, no multiplicative monotonicity subgoal after direct rpow_sub conversion; original terminal multiplication step eliminated.
- [2.7] lia/omega: n/a, only Nat threshold order uses explicit trans_lt; no arithmetic search needed. Real exponent gap handled by sub_pos.2 (lia does not decide arbitrary real arithmetic).
- [2.8] aesop: actual bounded LSP attempt exhausted search without proof.
- [2.9] norm_num/norm_cast: cast bridge uses exact_mod_cast; endpoint fixture uses simp to refute strict self-comparison. No concrete target arithmetic to norm_num.
- [2.10] decide/decide+kernel: n/a, quantified arbitrary-real eventual estimate is not finite decidable computation.
- [2.11] field_simp;ring: n/a, final proof has no rational identity subgoal; named quotient and rpow_sub API replaces original ring splitting.
- [2.12] linear_combination: n/a after strategy change, no ring/ring_nf goal or polynomial identity remains.
- [2.13] wlog: n/a, no symmetric cases.
- [2.14] two-step calc: n/a, no calc.
- [2.15] `<;>` common-goal closing: n/a, every refine creates only one proof subgoal.

Phase 3:
- [3.1] erw→rw: n/a, no erw.
- [3.2] continuity/measurability→fun_prop: n/a.
- [3.3] omega→lia: n/a, neither appears.
- [3.4] rcases with rfl substitution: n/a.
- [3.5] register automation lemmas: n/a, existential threshold theorem is not a simp normalization rule, no new automation attributes needed.
- [3.6] simp_all over simp_all only: n/a, no simp_all.
- [3.7] remove resource options: n/a, none before/after.

### Step back and think

Actual whole-goal grind, simp, aesop and exact? did not prove the estimate. apply? produced generic logical/filter reformulations only. Existing rpow divergence plus Nat cast and direct quotient conversion replaces the original inverse-threshold construction without new helpers, case splits, ring, or linarith. Term mode would obscure the threshold extraction, cast bridge, and quotient conversion. One named hq0 carries reused positivity; no redundant step remains. The independent inverse-power/absolute-value proof gives a different strategy for the strengthened contract.

## Final source and width

Target16→8 declaration lines (14→6 proof lines), saving8 lines; Main677→669 lines. Main final SHA4fbecf03eddef02596d342333df93856519d7c01fdc27f3104e024693a7cb2c5 (36491 bytes). Eval remains60 lines; final SHA610ec95658c5d43c931217bfb56b54d62f825473de17b3bdf6a1dde85dd900ca. The Eval entry source was saved before its one-argument edit.

| Sig line | Chars | Next semantic signature token | Arithmetic | Action |
|---|---:|---|---|---|
|97|59|full existential conclusion through `:= by`,68 chars without indentation|59+1+68=128>100|ok|
|98|72|proof body follows|n/a|ok|

Final proof maximum width98; all target source lines≤100 codepoints. One remaining `have hq0` has a by proof and two uses; all old inverse-threshold have blocks removed through the new strategy. No simp, push_neg, show, resource options, instances, helpers, or reversed inequalities remain in target Lean code. Comments: no original inline proof comments; Source citation retained. The docstring accurately states arbitrary real M and explains fixed-factor absorption. Cast audit:0 redundant casts introduced; the two signature q:ℕ→ℝ casts are genuine cross-type, the hq0 real-zero ascription fixes the positivity field, and one exact_mod_cast bridges Nat order once. Explicit q types retained for the natural threshold contract.

## Validation record

- First actual FULL build after target/Main caller edit: exit0.
- First required separate Eval build: exit1 at LeanEval.lean22, second caller discovered; no false pass claimed.
- Necessary Eval edit: replace positive witness `(one_div_pos.mpr hC)` with explicit `(M := 1 / C)`. hC stays used later.
- Actual FULL build on final Main+Eval source: exit0 (final-full-build.log).
- Separate actual `lake build Roth.LeanEval` on final source: exit0, built Eval103s (final-eval-build.log).
- Rejected semantic fixture1: archived raw Name quote `_@` was invalid Lean syntax; corrected to exact Name.str constructors.
- Rejected semantic fixture2: overbroad binder-info comparator edit touched Nat projection indices; exact failed source+log/launch/terminal preserved under Semantics-failed-v2 / semantics-failed-v2. Corrected only `.proj` index comparison to Nat equality. No rejected fixture receives semantics credit.

## Historical original-body profile (separate context)

Exact original canonical doc/signature/proof payload independently bound against the historical all17 row and narrow raw slices at offsets18881551,18961686,21332282,21332439; nested target Kernel child21332354. Full command payload slice80135 bytes checked, not a new broad317MB trace parse. Receipt historical-profile-binding.json. Historical original body335.286ms = outer command8.086 + async proof261.887 + kernel parent5.927 + lint parent59.386. Kernel child5.527ms nested and not added again; actual singleton family; no compiler row. Predecessor/context differs from final prefix, so this is separate baseline evidence with no speedup ratio claim.

- Rejected semantic fixture3: exit1 after597.742s because a freshly cloned Eval DATA definition had different generated-helper constants; cross-context clone VALUE identity was an unnecessary condition. This failure receives no credit. Replaced that comparison with strict full TYPE+VALUE comparison against the accepted actual original IsDiophantine root and generated._proof_1 indexed rows (6838/2089 raw bytes), checksummed independently. Also bound the affected Eval caller TYPE to its accepted actual original row. Required original/recovery/independent/caller proofs are cached in one temporary compiled module, so observation repair does not require reproving unrelated declarations. No production helper was created.

- Rejected whole semantic run4: blanket universe-emptiness assertion rejected the legitimately parametric preceding helper Roth.approxSet_den_le_finite._simp_1_2. The complete contract/DATA guards ran before emission; three fully checked rows (actual target, production Main caller, preceding finite theorem) are retained as valid partial evidence in valid-v4-prefix-receipt.json. The whole run remains exit1 and is never called a complete pass. Those rows are neither rechecked nor re-emitted. A small supplemental check inspects only outstanding proof families and closes the actual dependency graph, using accepted preceding audits/universe metadata. Outstanding full opaque VALUES are inspected in memory; only full TYPE, universe/dependency/axiom/default and representation length/hash64 observations are persisted. Hash64 is an observation identifier, not cryptographic identity or full raw VALUE evidence.
- Fresh complete unfiltered native checks passed: Main79.199s (0 errors,3 unused-variable warnings313/454/455); Eval66.286s and root71.588s (0 errors,0 warnings). The Main header warning appears in build/editor diagnostics, not this direct native invocation. All raw stdout/stderr and per-command launch/terminal records are retained.


## Completed semantic closure and final diagnostics

Combined closure PASS: valid-v4-prefix-receipt.json preserves three completed actual full TYPE+VALUE rows, and supplement-terminal.json records exit0 after715.305s. Supplement checked8 outstanding actual opaque VALUES fully in memory, reused3 valid rows, inspected8 accepted preceding declarations' actual dependency/universe metadata, and closed2454 external origin edges. The actual local graph is acyclic; independent and genuine original proofs recursively avoid the current target/generated families and caller/recovery shortcuts. External origins are strictly upstream in the actual module DAG. No generic empty-universe assumption is imposed on generated helpers. Actual standard axioms only (`propext`, `Classical.choice`, `Quot.sound`), closed inferred TYPES/VALUES and defaults200000/20000/512 passed. Full raw VALUE evidence is retained for the three prefix rows; supplemental VALUE evidence is actual in-memory checking with representation length/hash64 observations, not a claim of persisted full raw VALUE. Receipt: combined-semantics-receipt.json.

The intentional TYPE ledger removes only the original `hM : 0 < M` binder, preserving every remaining Expr/Level/Name/binder-info/metadata constructor. Old target TYPE4445B SHA33949a97027b79d9ba99268a4c369f2a23ad4b04b94fb2a6a776ea3ffcc520e8; new TYPE3898B SHAd3d0d8f361cd05c0e6e6df1b868519150e2c7ec7eb2175e18f888b6a473501e0. Genuine original replay and exact positive-contract recovery have the old contract. A structurally different absolute-value/inverse-threshold proof has the new contract. Both production callers retain exactly their original full TYPES; genuine original caller bodies were replayed against the genuine original target. Accepted actual old Eval DATA root/helper full TYPE+VALUE comparisons passed. No VALUE identity is required between different proof strategies.

Final complete unfiltered Main LSP: partial=false, timed_out=false, success=true, no failed dependencies,0 errors and4 existing unrelated warnings1/313/454/455. Final actual Main/Eval/root native checks and final FULL+separate Eval builds passed as recorded above. No compiler/native/LSP/profile overlap was introduced.

## Final focused performance receipt

Owner whole-phase HOLD acknowledged before prep; explicit RELEASE received only after actual capture/default/environment/freeze/drain completion. Exact production prefix5396B through the target, namespace close and observational family/TYPE/VALUE/default/width100 check; no production option changes. Actual `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0` capture passed. Full canonical doc/signature/body payload802B bound to the emitted command. Dynamic actual family is exactly `[Roth.eventually_div_rpow_lt]`.

All disjoint roots total96.835ms: outer command8.964 + async proof79.284 + kernel parent2.304 + lint6.283. Nested kernel child2.241 is not added twice. No compiler or lazy prior DATA roots occurred. Under1000ms and under750ms repeat threshold; no repeat capture. Historical335.286ms is a different context and no speedup ratio is claimed. Prefix and actual production full raw TYPE/VALUE/universe representations compare exactly, without normalization: VALUE127757B SHA21eab1bbc5759c3dafd73c3c86ce86109751b6db453b6c8440d2cb72bde882d6. The actual source prefix, canonical payload, tools/imports, environments and resource defaults were frozen/checked before and after. Full environments were compared only in memory; only hashes/lengths and PATH/LEAN/toolchain allowlist persisted. Process arguments collected only for task-owned processes. Receipts: final-profile/{target-profile-acceptance,prefix-production-relation,phase-complete}.json.

### Gate status — `eventually_div_rpow_lt` (Phase 4)

| Gate | Result | Details |
|---|---|---|
| lake_build_file | ✓ pass | actual final FULL and separate Eval exit0; fresh Main/Eval/root natives exit0 |
| definition_protected | ✓ pass | no definition signature/body changed; Eval theorem has only necessary caller argument repair |
| theorem_statement_protected | ✓ pass | explicitly authorized evidence-based hM-only weakening; exact old-contract recovery and both original caller contracts/replays checked |
| structure_gate | ✓ pass | proof6 lines≤30; no conjunction/case branches/helpers |
| naming_gate | ✓ pass | no forbidden name; no rename needed |
| line_packing_gate | ✓ pass | both signature rows measured above; no repack rows; max width98 |
| inequality_orientation_gate | ✓ pass | zero ≥/> in final target Lean signature/hypotheses |

Overall: pass.

### Result: `eventually_div_rpow_lt`

Before16 lines; after8; saved8. Audit issues found3; fixed3; refactoring deferred0. Applied:1.10,1.17 and2.5 through the direct existing-limit/rpow strategy, plus lambda formatting and the evidenced M-sign weakening. All42 golfing rules have explicit status above. Renames-queued:none. Comments-preserved:no original inline comments; paper Source citation preserved and docstring updated accurately. Refactoring needed:none.

Phase checklist:
- [✓] Step1 — reference docs read.
- [✓] Step2 — full24-item audit printed.
- [✓] Step2.5 — five-method mathlib search status printed.
- [✓] Step2.6 — generalisation and literature status printed; all parameters audited.
- [✓] Step2.7 — per-signature-line packing table printed and final widths checked.
- [✓] Step2.8 — inequality scan table printed.
- [✓] Step3 — all42 golfing rules reviewed.
- [✓] Step4 — step-back reflection completed.
- [✓] Step5a — complete final diagnostics, no errors or target warnings.
- [✓] Step5b — all diff gates passed, including orientation.
- [✓] Step6a — no renames required; no queue touched.

All source changes are confined to this target doc/signature/proof and the two necessary caller argument repairs. No new imports/helpers/axioms/sorry/native_decide/resource raises or metadata changes. No Git/shared progress/queue writes. All validation jobs terminal; no pending proof or profile work. All target/caller/compiler/native/LSP/profile leases released on delivery of the final receipt.
