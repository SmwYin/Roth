# Roth.exists_m — original 8 cleanup

Scope: target declaration and its documentation in Roth/Main.lean, plus the sole application in roth_of_isIntegral under the owner's explicit narrow caller lease. No new helpers, imports, definitions, renames, limits, axioms, Git operations or shared progress writes.

## Baseline and original preservation

The genuine project-original target and entry target were saved before any Lean or golf. They are byte-identical (target SHA256 0de63876c56a9f460d7b4af76c046f249a3649ae3573e63a7359c317dc31b600). Entry Main SHA256 8f25b12a5dc43b92b8020d100a5a4b2978a7377994adfdb8c22f5bab2e18e958. Baseline reuses the owner's exact-source full build 59.282 s, separate Eval 32.261 s, native Main/Eval/root 26.940/25.476/27.484 s, and complete LSP evidence (four warnings outside target). No redundant baseline compilation was performed.

Original declaration: 24 physical lines, of which 22 are proof-body lines. Final declaration: 21 physical lines, of which 19 are proof-body lines. These are measured at the first `:= by` boundary, without splitting on nested `by`. The initial audit's estimated 25 body lines and signature widths were corrected by measurement; they are not acceptance measurements.

## Full 24-item audit

1. **LINT:** no errors or warnings on target. Complete Main diagnostics retain only the same four out-of-scope warnings.
2. **HAVE SCAN:** original hκ2 (by; positivity), hs4 (by; natural bound), hsR (by; twice), hceil (term; once, removed), hn' (term; consumed by broad nonlinear searches, removed), hs4R (by; real bounds), hkey (by; quotient), its anonymous division bound (by; once, eliminated), hsq (by; twice, eliminated), hspos (by; real bounds). Final hs4 (by; twice explicitly), hs4R (by; twice), hspos (term; twice), hkey (by; once), hmul (by; twice). Every remaining term-style have is used at least twice. No single-use non-proof have survives.
3. **SET_OPTION:** none originally or finally; default limits remain 200000/20000/512.
4. **SIMP SQUEEZE:** final `simpa [pow_two] using ...` and `simpa using hmul` both close their goals; unsqueezed. No nonterminal bare simp. Repeated cast-normalization scaffolding reduced to one explicit final push_cast and one exact_mod_cast bridge.
5. **NAMING:** exists_m is snake_case with no forbidden abbreviation or scheme-number pattern; m is a quantified mathematical witness, not a single-letter public declaration. No rename queued.
6. **LINE PACKING:** complete final signature table below. First line 96 codepoints, second 44. No repack row survives.
7. **BY PLACEMENT:** by closes the signature line; local proof blocks likewise.
8. **FORMAT:** two-space proof indentation, four-space signature continuation; no empty proof lines or semicolon chains. No haveI/letI.
9. **COMMENTS:** no original inline proof comments to preserve. Source citation preserved. No comment removed.
10. **DOCSTRING:** retained precise §7 equation (47) citation; added explicit n=0 applicability. This is statement/application information, not proof strategy.
11. **VISIBILITY:** retain public named numerical parameter-selection API documented in the module outline and exists_delta's documentation. This is classic Lean syntax, not a module-system file.
12. **STRUCTURE:** ordinary theorem (not in Main results), body 19 ≤30; final branches one and three lines, hkey block six lines. The conjunction records three constraints on one common existential witness; splitting into separately chosen witnesses would lose its mathematical content. No artificial split/extraction.
13. **MATHLIB:** five-method status below. Build directly on Nat.le_ceil, Real.sqrt_sq, division-order API and monotone multiplication. No duplicate replacement found; no missing wrapper/coercion API requires extraction.
14. **JUNK DEF:** n/a, theorem rather than definition.
15. **EXISTS LEMMA:** n/a, nontrivial public construction rather than a private tuple of reflexivity proofs.
16. **SHOW vs CHANGE:** final `show ... by` is a term passed to exact_mod_cast, pinning a natural-number inequality. It does not change a tactic goal.
17. **PUSH_NEG:** none.
18. **GENERALISE:** dropped hn after actual compiled generalized entry proof; retained hκ after concrete drop and weak-bound compilation tests. Full table below. No typeclasses, type variables or universes to weaken.
19. **INEQUALITY:** no ≥ or > in Lean code; scan table below. Docstring/source-quotation mathematical prose may retain >.
20. **NORMAL FORM:** Nat witness, Real.sqrt and ordinary quotient inequalities already use the canonical library forms. No alternative custom predicate or equivalence API.
21. **SYNTAX GENERALITY:** same common witness and conclusion retained; removing hn directly simplifies application. No other restatement improves the actual caller.
22. **IMPORT FANOUT:** n/a, no added/reordered imports.
23. **CASTS:** removed the hsR real-cast expansion and the dedicated hsq cast/sqrt equality, including their explicit annotations. Retained genuine Nat→Real bridges and annotations fixing real arithmetic/sqrt (s, zero and m); no redundant cast of an already-real expression. Final ascription occurrences: two m:ℝ in signature; 4*n:ℝ at hs4R, 0:ℝ at hspos, s:ℝ at hkey, two s:ℝ at hmul. Five explicit Nat→Real m/s ascriptions plus two load-bearing real arithmetic/zero annotations. Cast status: 4 old-only scaffold ascriptions dropped / 5 retained as cross-type / 2 retained as load-bearing. No other explicit coercion/ascription added.
24. **INSTANCE NAME:** n/a, no instances.

Issues fixed: unnecessary n positivity assumption/caller obligation; broad nonlinear search context; repeated cast expansion; underpacked signature; semicolon chains; missing n=0 application guidance. No refactoring remains deferred. Rename queue untouched.

## Mathlib search status

| Method | Actual query | Finding/action |
|---|---|---|
| A Lean-Finder | common natural m with 16*n²<m, 4*n*sqrt(m)<m and quotient<κ | unrelated additive-combinatorics Roth-number results; no replacement |
| B Loogle | `Nat.ceil, _ ≤ _` | Nat.le_ceil / Nat.ceil_le / Nat.floor_le_ceil; Nat.le_ceil used directly |
| C LeanSearch | natural ceiling strictly greater than real number | ENat floor API; not this statement |
| D source search | lt_ceil, ceil_lt, lt_add_one, ceil_pos in Floor Defs/Ring/Semiring | Nat.lt_of_ceil_lt, Nat.le_ceil and positive-ceiling API; square/ceil proof retained |
| E local name pattern | ceil_lt | Nat.ceil_lt_add_one / ceil_lt_mul and Int/ENat variants; source index warming, so absence not inferred from that index |

Auxiliary variants considered: Nat.lt_ceil, Nat.lt_of_ceil_lt, Nat.ceil_lt_add_one, division lt iff forms, square-root square cancellation and multiplication strict monotonicity. Common-equivalents lookup: no matching custom topology/finiteness/bornology predicate. Whole-goal exact? failed; apply? offered only general existential/logical constructors, not a mathematical proof. Thus retain the numerical construction using partial matches directly; no claim that five search misses alone establish library absence.

## Generalisation status

| Parameter | Class | Used as | Mechanical candidates and verification | Result |
|---|---|---|---|---|
| {n : ℕ} | structure value | shared coefficient in conclusion/witness | drop inapplicable: n appears in conclusion; no typeclass parent or point-localisation/universe candidate | retained |
| (hn : 0<n) | proposition | unnecessary original arithmetic context | drop tested by compiling exact entry prefix without hn, exit0, 37.607 s; zero≤n is weaker than positivity but follows for every natural, so drop is the weakest form | removed permanently |
| {κ : ℝ} | structure value | quotient threshold and ceil witness | drop inapplicable: κ appears in conclusion; changing fixed ℝ and sqrt to a new abstract structure is a different API project, not mechanical weakening | retained |
| (hκ : 2<κ) | proposition | positive denominator κ−2 | actual substitution by 2≤κ fails at sub_pos.mpr; removing it fails because hκ is absent at the same use | retained |

No global/pointwise or decidability hypotheses exist. Inversion diagnostic: n and κ occur throughout the estimates, and the statement names no concrete special object unfolded away by the proof; abstract-via-concrete inversion does not fire. No optional abstract-field generalisation, companion theorem or helper was introduced. The authorized hn API change has its original contract recovered separately and repairs the only actual caller.

Literature search: query `Roth theorem proof choose m 2m m 4n square root generalization`; top three hits were MIT additive-combinatorics lecture, independent-set paper, and Scribd graph-combinatorics text, all irrelevant to this numerical lemma. Relevant returned higher results: Wikipedia Roth's theorem, the Encyclopedia of Mathematics Thue–Siegel–Roth entry, and Schmidt's Subspace Theorem overview. They concern generalisations of the final Diophantine theorem, not weakening this elementary parameter estimate. The local paper's §7 equation (47) remains the actual source. No math second-opinion MCP is installed. No literature-driven scoped change beyond the compiled hn drop.

## Final line-packing table

Reference: actual #check @Roth.exists_m at format.width100 is captured by final profile suffix.

| Signature line | Codepoints | Next atomic signature fragment | Arithmetic | Action |
|---|---:|---|---|---|
| 190 | 96 | `2 * m / (m - 4 * n * √(m : ℝ)) < κ` (34) | 96+1+34=131>100 | ok |
| 191 | 44 | none (proof next) | n/a | ok |

Widths include indentation and := by. Conclusion participates in packing: existential prefix and first two constraints occupy the first line.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | signature/all hypotheses and final body | no ≥/> in Lean code | none | no _ge_/_gt_ name |

## Golfing-rule pass (all 42)

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a, no wrapper; hs4R has actual exact_mod_cast work |
| 1.2 by rfl | n/a, none |
| 1.3 rw+exact→rwa | removed hsR/hsq rewrite scaffolding entirely |
| 1.4 simp+exact→simpa | final square and real multiplicative bound close with simpa using |
| 1.5 trailing rfl | n/a, none |
| 1.6 tuple constructor | already used one existential/common-witness tuple |
| 1.7 apply+exact | hkey uses apply to expose inequality then trans_lt, not an apply/exact wrapper |
| 1.8 contradiction/push_neg | n/a, constructive proof |
| 1.9 eta-reduce | n/a, no lambda |
| 1.10 single-use have | hceil removed; its direct Nat.le_ceil application composed with trans_lt |
| 1.11 apply+intro | n/a, no introduced function argument |
| 1.12 show | retained only load-bearing term-mode show inside exact_mod_cast |
| 1.13 have projections→obtain | n/a, no projected tuple have |
| 1.14 merge rw | sqrt and denominator-order rewrite combined in one final rw |
| 1.15 terminal simp only | final simpa [pow_two] is unsqueezed; no squeezed terminal simp |
| 1.16 nonterminal simp | n/a, no bare nonterminal simp |
| 1.17 dot notation | (Nat.le_ceil _).trans_lt used directly |
| 1.18 <\| | n/a, no needless trailing function/lambda parentheses |
| 1.19 push Not | n/a, no negation pushing |
| 1.20 trivial existential helper | n/a, no private trivial existential helper |
| 2.1 grind whole | tried, failed to construct the square/ceiling witness |
| 2.2 delete before grind | n/a, no retained grind |
| 2.3 simpa consolidation | real square estimate and sqrt-cast conversion close directly |
| 2.4 fun_prop | n/a, no function-property goal |
| 2.5 positivity | used for nonnegative 4*n in hspos |
| 2.6 gcongr | monotonicity expressed directly by mul_lt_mul_of_pos_right; no congruence calc remains |
| 2.7 lia/omega | both natural ceiling comparisons use lia, replacing omega |
| 2.8 aesop | whole-goal attempt failed, made no progress |
| 2.9 norm_num/norm_cast | exact_mod_cast carries natural s bounds to/from reals; one final push_cast |
| 2.10 decide/kernel | n/a, existential over unbounded naturals and real parameter |
| 2.11 field_simp;ring | n/a, no rational identity remains; ordered division handled by div_lt_iff₀ |
| 2.12 linear_combination | n/a, no retained ring/ring_nf identity; inequalities use explicit positive multiplication |
| 2.13 wlog | n/a, no symmetric case split |
| 2.14 collapse calc | hkey composes le_ceil.trans_lt, no two-step calc remains |
| 2.15 <;> | n/a, final constraints require different natural/sqrt/division conversions |
| 3.1 erw→rw | n/a, none |
| 3.2 fun_prop | n/a, no continuity/measurability |
| 3.3 omega→lia | applied as 2.7 |
| 3.4 rcases rfl | n/a, no case substitution |
| 3.5 automation attributes | n/a, one-off numerical existence result; no useful simp normal form |
| 3.6 simp_all | n/a, no simp_all only |
| 3.7 maxHeartbeats | n/a, none to remove; no limits added |

## Step-back reflection

Whole-goal grind/aesop/exact? did not construct the witness, while apply? produced only logical/existential reformulations. The existing square witness is mathematically efficient: choose its root beyond both 4n and the ceiling threshold, then square. Term-mode assembly already handles the common witness. The useful strategy change was to replace repeated cast identities and full-context nonlinear arithmetic by monotone multiplication plus a single explicitly supplied cubic inequality. The target needs no new helper.

## Simplify and performance qualification

Actual built-in Skill(simplify) is unavailable in this environment, and was not falsely invoked. The scoped holistic review checks reuse, quality and efficiency directly; owner's fresh independent whole-file final review remains a later file-level obligation. Historical genuine measurement 3908.904 ms is valid FAIL in a different source context; it is not a speedup-ratio baseline. Historical async proof root 3682.863 ms plus command/kernel/linter roots is consistent with the source's broad nonlinear arithmetic. No unsupported per-tactic percentage is claimed. The targeted fix supplies only hs4 or a single positive-multiplied hkey inequality and removes repeated cast normalization; final focused profile acceptance is recorded separately.


## Verification and semantic gates

All artifacts below are under `/private/tmp/roth-main-choose-m` unless otherwise stated.

| Gate | Result | Actual evidence |
|---|---|---|
| full lake build | PASS | `lake build` exit0 60.322 s; after signature packing `lake build` exit0 38.104 s (`packed-full-build-*`) |
| separate evaluation build | PASS | subsequent `lake build Roth.LeanEval` exit0 31.246 s (`final-eval-build-*`); root default build excludes Eval |
| native Main | PASS | complete unfiltered `lake env lean Roth/Main.lean` exit0 33.122 s |
| native Eval | PASS | complete unfiltered `lake env lean Roth/LeanEval.lean` exit0 30.585 s |
| native root | PASS | complete unfiltered `lake env lean Roth.lean` exit0 27.274 s |
| complete LSP | PASS | final-Main/Eval/root-lsp.json: Main0 errors and four unchanged warnings at1/279/420/421; Eval/root no diagnostics |
| definition_protected | PASS | no def/abbrev/import changes |
| theorem_statement_protected | PASS, authorized generalisation | hn removed under explicit owner instruction; original full contract recovered exactly; caller full TYPE unchanged |
| structure_gate | PASS | 19-line ordinary proof; shared-witness conjunction is inseparable; branches1/3 lines |
| naming_gate | PASS | no forbidden name; no rename needed |
| line_packing_gate | PASS | complete measured table96/44; next34-codepoint atomic constraint would give131 |
| inequality_orientation_gate | PASS | zero ≥/> in Lean code |
| cumulative external breakage | PASS | sole application repaired under narrow lease; Main/Eval/root native and LSP gates pass |
| no limits/trust scaffolding | PASS | no limits, axioms, sorry, native_decide, heartbeat counters or profiling options in production diff |
| source preservation | PASS | Main-worker.diff contains only target/doc and authorized caller application |

The owner's final direct doc sentence was applied at a drained boundary after full→Eval builds. Those build gates are reused for the byte-identical mathematical source; the final wording is freshly checked by all three complete native commands, all three complete LSP queries, semantics and exact-prefix profile. No new build was run solely for wording or a worker label. All source/dependency bytes remained exact through final freeze verification.

New proof identifiers are verified by successful native compilation and actual getConstInfo/inference/origin inspection in semantics (in particular mul_lt_mul_of_pos_right and lt_of_le_of_lt); no guessed identifier survived.

### Strict contracts and actual values

`accepted-old-types.json` contains only the needed genuine old TYPE strings and their indexed metadata, decoded by exact target/caller offsets; TYPE hashes match the accepted791247479-byte source log. No giant old VALUE was exported or replayed. The accepted strict comparator is retained: Names, Levels, BinderInfo, metadata, literal/projection/syntax fields are recursively compared without an Expr BEq shortcut.

The successful distinct scratch independent proof uses `exists_nat_gt (max (4*n) (4*κ*n/(κ-2)))`, not the production ceiling definition or any target theorem. Its compilation exited0 in32.713 s. `semantics-*` exited0 in160.486 s at actual defaults200000/20000/512 and checked:

* Full generalized production/independent TYPE equality, including binder names and metadata.
* Full recovered-old-contract TYPE equality to the genuine original; recovery is actually opaque, universe-free, closed, inferred and standard-axiom-only.
* Full original caller TYPE equality; actual opaque caller VALUE closed/inferred with only propext/Classical.choice/Quot.sound.
* Actual current family root plus `_proof_1_1` through `_proof_1_4`, and the independent root, with full TYPE/actual universe observations and actual opaque VALUE checks in memory.
* Fresh local closure acyclic and no self/circular shortcuts; independent cannot use target/family, production cannot use independent. All836 actual external-origin entries have strictly upstream module indices; no accepted preceding Main leaf was needed.

All five actual production generated-family universe lists were observed as[]; this was not assumed as a generic generated-helper rule. Actual current/profile full TYPE representations and universe observations agree for all five family members (`final-profile/production-profile-family-types.json`). Proof VALUE identity across modules/proofs is explicitly not claimed. Receipts contain only VALUE hashes/lengths after in-memory actual-value inspection, not full raw VALUE exports.

### Preserved failures and qualifications

* `failed-root-independent-build-*`: scratch -o compilation lacked a scratch root flag; corrected with -R. Not proof evidence.
* `failed-import-race-semantics-*`: an LSP dependency rebuild removed Main.olean during the overlapping semantic launch. No pass credit; all LSP calls were then fully drained, and remaining compiler/native work ran sequentially.
* `failed-default-semantics-*`: the first monolithic semantic check of the ungolfed independent replay timed out at the default200000 heartbeat limit after160.520 s. Its independent source had compiled, but that default guard run failed and is not counted as passing. The scratch-only independent proof was replaced by the distinct Archimedean construction; no limits or production source were changed to evade it. The subsequent actual strict run passed.
* Earlier scratch LSP weak/drop probes reported out-of-date imports and were not accepted as mathematical test results. The actual native WeakKappa and DropKappa substitutions subsequently exited1 with the expected strict-premise/absent-hκ errors. The boundary n=0, κ=2 also makes the quotient2 for every admissible positive m, explaining why weak κ is not enough.
* Two misplaced exploratory multi-attempt calls hit declaration boundaries and were disregarded. Actual native compilation, complete diagnostics and strict semantic/profile guards establish the retained proof.

All failed scratch/terminal artifacts are retained. No failure was relabeled as a pass, and there were no generic harness/reproof loops or limit raises.

## Final buzz profile

Outcome: FIXED, with no deferrals. Historical original source context3908.904 ms remains a separate valid FAIL, not a speedup-ratio baseline. Final focused exact-prefix context is687.909 ms, a valid PASS under1000 ms and below the750 ms repeat threshold; no repeat or unchanged-source extra capture was performed.

| Disjoint root | ms |
|---|---:|
| command/canonical payload | 61.272 |
| async proof | 581.223 |
| generated/kernel parent1 | 0.109 |
| generated/kernel parent2 | 4.018 |
| generated/kernel parent3 | 0.117 |
| generated/kernel parent4 | 2.350 |
| theorem kernel/compilation parent | 26.183 |
| async lint | 12.637 |
| **Total** | **687.909** |

All five fresh family kernel declarations are accounted for under these parents. Compiler list is empty; no lazy prior DATA root occurs in this target row. Nested kernel time is not added again. Full canonical doc/signature/body payload matching, raw hash/length/byte-offset roots, actual family/default/TYPE/VALUE checks and source bindings are in `final-profile/target-profile-acceptance.json` and companion receipts. The actual invocation was `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 .../Prefix.lean`; stdout/stderr were captured separately.

Owner HOLD ACK preceded every timing preparation. Exact imports and preceding commands match the entry, then the exact final production target prefix was closed with end Roth and actual observation commands. The41 frozen source/dependency/tool/input bindings remained exact. Safe parent/Lake full-environment byte equality was checked only in memory; only lengths/hashes and allowed path/toolchain fields were persisted. Process observations included only owned PID/start/executable/arguments, with narrow escalation on first ps attempt. All five phase launches and the capture driver actually exited0, groups were absent and defaults/env/freeze passed before the UNPARSED notice. Explicit owner RELEASE preceded any profiler parsing. No full environment or unrelated arguments were persisted.

Actual requested `format.width 100` #check reference:

```lean
@Roth.exists_m : ∀ {n : ℕ} {κ : ℝ}, 2 < κ → ∃ m, 16 * n ^ 2 < m ∧ 4 * ↑n * √↑m < ↑m ∧ 2 * ↑m / (↑m - 4 * ↑n * √↑m) < κ
```

This is the actual Lean #check output; source packing is independently measured in the table above.

## Result and phase checklist

Before24 declaration/22 proof-body lines; after21 declaration/19 proof-body lines; saved3 lines. Full Main638→635 lines. Six audit issues fixed; no refactoring, helper lifecycle or rename remains pending. Rules applied:1.3,1.4,1.10,1.14,1.15,1.17,2.3,2.5,2.7,2.9,2.14,3.3. Gates PASS. Comments preserved: none originally inside target proof; source citation retained. Renames queued:none; five global END rename entries untouched.

* [✓] Step1 — required skills/workflows/reference documents read.
* [✓] Step2 — full24-item audit.
* [✓] Step2.5 — five-method search and compiled exact?/apply? routes.
* [✓] Step2.6 — every parameter classified, actual hn drop and κ weaken/drop checks.
* [✓] Step2.7 — every signature line measured and packed.
* [✓] Step2.8 — inequality scan.
* [✓] Step3 — all42 rule statuses.
* [✓] Step4 — strategy/reflection.
* [✓] Step5a — complete Main/Eval/root diagnostics.
* [✓] Step5b — all diff/build/semantic/performance gates.
* [✓] Step6a — no rename required; queue untouched.
* [✓] Step6b — full report and actual END/drain.

Actual Skill(simplify) unavailable; no invocation claimed. The scoped holistic review is complete; the owner's fresh independent whole-file final review and full-source all-row profile are later file-level obligations, not silently credited here. Owner's narrow independent source/evidence review is accepted in `/private/tmp/roth-main-owner/choose-m-owner-review-v1.json`.

## END

Actual final Main SHA256 `ba920c954bb74fe8012f5c01fdbdf2e87740256028c9ad093ba190f8e9c1ae00`,34921 bytes/635 lines. `final-END.json` confirms all20 known launch groups absent, actual final verification/profile driver exits0, profile driver PID absent, all queries and earlier failed drivers terminal, no active HOLD and41 frozen inputs still exact. No Git/shared progress writes and no next-target edits. All target-source, sole-caller-repair, report, compiler, native, LSP and profile leases are released. Actual FINAL: target cleanup complete; ready for owner's exact-path review/publication.
