### Auditing: `Roth.exists_nat_mul_isIntegral` (entry lines 55–66, 12 lines)

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. Lean4/mathlib-quality skills, style/naming references, actual cleanup/buzz workflow and source §6 integral-multiple lemma read. Genuine original and entry snapshots saved before any Lean execution in `/private/tmp/roth-main-integral-multiple`.

1. LINT: fresh native target-range diagnostics success=true, partial=false, no items or failed dependencies. Existing unrelated file warnings remain owner scope.
2. HAVE SCAN: entry L57 `hZ : IsAlgebraic ℤ α := ...`, no by, used once L58: INLINE. L62 anonymous cast equality, by proof, used once L63: replace entire branch using scalar-sign identity. L64 anonymous negative cast equality, by proof, used once L65: same action.
3. SET_OPTION: none; no raises or profiling wrappers introduced.
4. SIMP SQUEEZE: entry has no simp. Candidate uses terminal unsqueezed `simpa [...]`; a tried squeezed scalar-action variant works but is not retained.
5. NAMING: descriptive existential natural-multiple theorem, `isIntegral` retains the established predicate token; no forbidden abbreviations, numeric patterns, or single-letter public name. No rename warranted.
6. LINE PACKING: unchanged two-line signature; measured table below. Full existential conclusion is the next logical signature unit and cannot join line55.
7. BY PLACEMENT: by remains at end of conclusion line.
8. FORMAT: two-space tactics, no internal blank lines, one tactic per line, no haveI/letI.
9. COMMENTS: no inline comments present; attached source docstring preserved byte-for-byte.
10. DOCSTRING: public theorem has a statement sentence and exact §6 source; no proof prose to move. Existing docstring is preserved.
11. VISIBILITY: public API retained; this is the named source reduction fact, independently reusable for algebraic reals, not an implementation-only extraction.
12. STRUCTURE: entry10 proof lines, branches2 and3; planned3 proof lines, no branches. The conjunction binds positivity and integrality to the SAME existential witness; splitting into independent existence facts loses that content and adds companion wrappers. No extractable long branch or top-level conjunction; no helper needed.
13. MATHLIB: five-method search below; use generic integral multiple plus integer scalar sign normalization directly. No exact positive-natural statement established by search or whole-goal exact?.
14. JUNK DEF: n/a: theorem, not definition.
15. EXISTS LEMMA: not private or a trivial constructor/rfl witness; its witness comes from algebraicity and must be normalized to positive.
16. SHOW vs CHANGE: n/a: no show.
17. PUSH_NEG: n/a: no push_neg.
18. GENERALISE: all binders covered below; algebraicity is used, no mechanical parent/global/strict/universe hypothesis weakening exists. Optional abstract ambient-ring restatement is outside this target lease and not recommended.
19. INEQUALITY: sole signature inequality `0 < M` already oriented; no ≥/> in Lean code; table below.
20. NORMAL-FORM: positive natural multiplier is the form required by the later reduction; generic mathlib uses nonzero integer scalar action. Normalize that witness inside the proof, leaving the application form unchanged.
21. SYNTAX-GEN: OK: `obtain ⟨M, hM, hMint⟩` directly gives the shared multiplier and its positivity; no easier supported restatement.
22. IMPORT-FANOUT: no new imports. Narrow authorized Phase3 alphabetic/group import reorder will be applied and full builds verified.
23. CASTS: diff introduces no explicit casts (0 new redundant annotations to drop / 0 new cross-type annotations kept / 0 new load-bearing annotations kept). Six old annotations disappear with the branches: two redundant Nat annotations and four Nat/Int→Real annotations. Existing statement's `(M : ℝ)` is a genuine Nat→Real bridge, preserved.
24. INSTANCE-NAME: n/a: no instances.

Issues to fix: (1) inline single-use hZ; (2) replace manual sign branches by `hint.zsmul y.sign` and `Int.sign_mul_self`; (3) authorized Phase3 import order. Refactoring needed: none; no optional abstract generalization, extraction, companion or rename proposed.

### Line packing — `exists_nat_mul_isIntegral`

Native #check reference, 97 codepoints and fitting width100: `@Roth.exists_nat_mul_isIntegral : ∀ {α : ℝ}, IsAlgebraic ℚ α → ∃ M, 0 < M ∧ IsIntegral ℤ (↑M * α)`.

| Signature line | Codepoints | Next logical signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| entry55 / final56 |66|`∃ M : ℕ, 0 < M ∧ IsIntegral ℤ ((M : ℝ) * α) := by` (49)|66+1+49=116 >100|ok|
| entry56 / final57 |53|none; proof next|n/a|ok|

### Inequality scan — `exists_nat_mul_isIntegral`

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
|1|entry56 conclusion|`0 < M`|already smaller-first|none|
|—|all signature/hypotheses/body|no ≥ or >|none needed|no _ge_/_gt_ name|

### Mathlib search-status: `exists_nat_mul_isIntegral`

[A] Lean-Finder: "Every algebraic real number has a positive natural multiple that is integral over the integers"; top3 `IsAlgebraic.exists_integral_multiple`, `IsAlgebraic.iff_exists_smul_integral`, `Algebra.IsAlgebraic.exists_integral_multiples`.
[B] Loogle: `IsAlgebraic ℚ ?x → ∃ n : ℕ, 0 < n ∧ IsIntegral ℤ (↑n * ?x)`; empty, isError=false (not an absence proof).
[C] LeanSearch: "absolute value of an integral element is integral"; results norm and ring-of-integers lemmas, no relevant abs lemma.
[D] Source: full untruncated searches `exists_integral_multiple`, `IsIntegral.abs`, integral-closure abs/smul, `sign_mul_self`, natAbs/sign. Read Algebraic/Integral lines146–158 and IsIntegralClosure/Basic lines225–229. `IsIntegral.zsmul` and `Int.sign_mul_self` supply the exact missing normalization, verified by #check and a compiled independent example.
[E] Local `IsIntegral.abs`: empty, index=unavailable, so no absence inference. Source and #check provide positive presence evidence for the actual used names.

Auxiliary variants: integral_multiples, iff_exists_smul_integral, IsIntegral.smul/zsmul/neg, Int.sign_mul_self_eq_natAbs, natCast_zsmul. Common-equivalents buckets: none. Whole-goal exact? fails; apply? offers only unresolved generic existential rearrangements, not a proof. Partial match: retain target as the positive-Nat adaptation of the source lemma, build on mathlib directly, with no new helper or duplicate API. Strict rules reviewed: no exact replacement warranting deletion; no custom predicate/class, wrapper helper or new import added.

### Generalisation status: `exists_nat_mul_isIntegral`

| # | Parameter | Class | Used as | Mechanical candidates | Verified? | Result |
|---|---|---|---|---|---|---|
|1|`{α : ℝ}`|structure value|algebraic element and multiplied element|drop would leave free α or infer same binder; no parent, pointwise, strict, or universe hypothesis; abstract ring is public-API restatement|inspection|keep operational binder|
|2|`hα : IsAlgebraic ℚ α`|proposition|fraction-field transfer then integral multiple|drop; no bundled/global/strict/typeclass hypothesis to weaken|yes: drop probe failed at transfer, unknown hα|reverted; required by integral-multiple construction|

Inversion check: no named concrete witness unfolds and disappears; α is the arbitrary element, not a special object. General fraction-ring theorem already exists in mathlib. Big-change candidates: none recommended under target scope; changing ℝ to a general ℚ-algebra would add an API and abstract casts without simplifying this application.

### Literature search status: `exists_nat_mul_isIntegral`

[A] WebSearch `algebraic number positive integer multiple algebraic integer generalization`. Top3: [Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Algebraic_integer), [Voutsadakis algebraic-number-theory lecture Chapter2](https://www.voutsadakis.com/TEACH/LECTURES/ALGNUM/Chapter2.pdf), [Adler et al. algebraic extensions](https://adler.ieor.berkeley.edu/ilans_pubs/lp_algebraic_stoc_1992.pdf). The primary lecture formulation confirms integer multiples of algebraic numbers; supplied project source §6 proves the positive-leading-coefficient version. Standard generality is not confined to real numbers; generic scalar-clearing is already supplied by mathlib. No unnecessary mathematical hypothesis found within the real-number contract.
[B] ChatGPT math MCP: n/a: no such callable tool available. Literature-driven big-change candidates: none recommended.

### Golfing rule pass

Phase1:
[1.1] n/a: no by-exact wrapper.
[1.2] n/a: no by-rfl wrapper.
[1.3] entry positive branch already rwa; both rw/exact branches eliminated by sign normalization.
[1.4] applied: normalize the scalar action with one terminal simpa using the integral scalar multiple.
[1.5] n/a: no trailing rfl after simp.
[1.6] already constructor tuple for the shared positive witness; no separate constructor/exact sequence.
[1.7] n/a: no apply/exact sequence.
[1.8] n/a: no contradiction or push_neg.
[1.9] n/a: no lambda.
[1.10] applied: inline hZ into exists_integral_multiple.
[1.11] n/a: no apply/intro.
[1.12] n/a: no show.
[1.13] already obtain on the integral-multiple existential; no separate have/projection sequence.
[1.14] entire sign-case rewrite sequence replaced, no consecutive rw calls survive.
[1.15] applied: final terminal simpa is unsqueezed. Tried simp-only scalar-action variant compiled but was not retained.
[1.16] n/a: no nonterminal bare simp.
[1.17] applied: integral multiplication by integer sign uses `hint.zsmul y.sign`.
[1.18] n/a: no avoidable final parentheses; fraction-ring transfer parentheses delimit the receiver of .exists_integral_multiple.
[1.19] n/a: no push_neg.
[1.20] n/a: public nontrivial integral-multiple construction, not private constructor/rfl existential.

Phase2:
[2.1] tried whole-proof grind through live native multi_attempt; failed with remaining contradiction that all integral natural multiples have zero multiplier.
[2.2] n/a: no grind in retained proof.
[2.3] applied: one terminal simpa consolidates cast/action normalization with the integral proof.
[2.4] n/a: no continuity/differentiability/measurability goal.
[2.5] tried independent natAbs positivity subgoal with positivity; succeeded. Retain direct `Int.natAbs_pos.2 hy`, which names the exact condition and is already a single short term; no line saving or clarity improvement under minimum-value filter.
[2.6] n/a: no monotonicity/congruence inequality; sole positivity goal has exact iff API.
[2.7] tried lia on natAbs positivity with hy; succeeded. Same direct-term minimum-value decision as2.5; no integer-arithmetic chain remains to replace.
[2.8] tried whole-proof aesop; failed, no progress.
[2.9] cast normalization consolidated in simpa; no concrete numeric computation or separate norm_cast block.
[2.10] n/a: existential integrality over arbitrary real α has no finite computational decision procedure.
[2.11] n/a: no rational-function equality or denominator-clearing goal.
[2.12] n/a: no ring/ring_nf closing proof or polynomial relation requiring linear_combination.
[2.13] applied stronger direct strategy: both symmetric sign cases eliminated via integer sign multiplication; wlog would retain a case and invoke symmetry, adding work to the verified three-line proof.
[2.14] n/a: no calc.
[2.15] n/a: single remaining integral goal; witness positivity supplied directly, no similar repeated subgoals.

Phase3:
[3.1] n/a: no erw.
[3.2] n/a: no legacy continuity/measurability tactic.
[3.3] lia tried in2.7; no omega introduced.
[3.4] n/a: no rcases-with-rfl pattern; original sign split removed.
[3.5] n/a: no new lemmas or repeated automation API needing an attribute.
[3.6] n/a: no simp_all only.
[3.7] n/a: no resource override to remove.

### Step back and think

Whole-proof grind, simp, aesop and exact? fail; apply? offers existential rearrangements with unresolved obligations. Direct scalar multiplication by the sign proves integrality for the absolute-value witness without case analysis. Term mode would embed existential elimination and cast transport lambdas, obscuring this three-step argument; no non-by have remains. The final terminal simpa is unsqueezed and independently compiled. The source lemma's positive-Nat contract has no exact mathlib replacement found: generic integral_multiple gives only a nonzero integer scalar action, whereas reduction requires strict natural positivity and real multiplication. This is substantive shared-witness adaptation, not a newly introduced convenience wrapper; deleting it would move sign/cast plumbing into the reduction and hide the named source fact. Owner explicitly reviewed and accepted retention. No helper, companion, or optional generalization added.

### Actual semantic verification

`Semantics.lean` contains the genuine preserved ungolfed proof replayed with only its declaration name changed, and a different current-contract proof using a sign split with terminal simpa in each branch. Neither uses the target or either generated target proof. The actual current, replay and independent TYPE expressions compare fully to the accepted original constructor expression, including binder names/info, universes, names, metadata, let flags, literals and projections. The comparator recurses through Expr/Name/Level constructors and never short-circuits with ExprBEq. Current TYPE also equals the full accepted raw TYPE string. The proof VALUE deliberately changes; no proof-term identity is required or claimed between the different proofs.

All five actual declarations (production target, its two generated `_simp_1_1`/`_simp_1_2` proofs, originalReplay and independentCurrent) had their opaque VALUE retrieved, type inferred, expressions checked closed without metavariables/level metavariables/free variables/loose binders/sorryAx, and axioms checked against propext/Classical.choice/Quot.sound. Defaults were exactly200000/20000/512. The full local dependency graph is acyclic; production may use its two naturally generated simplification proofs. The actual160/159 direct dependency occurrences from replay/independent full TYPE+VALUE have136 distinct names, all mapped to Init/Mathlib origins strictly earlier than Roth.Main in the actual compiled import DAG. This excludes indirect target/generated dependencies and scratch/project wrappers, rather than relying only on a local graph. `Origins.lean` checks this against the actual environment. Full actual pairs remain in semantics-validated.stdout; actual origin rows remain in origins-final.stdout.

Temporary checker errors (syntax/reserved binder, an initially assumed singleton family, and an over-strong replay-VALUE identity assertion) and the first origin-checker errors were corrected before acceptance; their failed logs/terminal receipts are retained. These were verification-scaffold failures, not production source failures. Final semantic check exited0 in72.207446s; final origin check exited0 in42.203336s. All their launched groups drained.

### Builds, native diagnostics and scope

After the final source edit, actual `lake build` exited0 in63.249853s (build-full-terminal.json), then the separate actual `lake build Roth.LeanEval` exited0 in31.766677s (build-eval-terminal.json). Source hash remained exact throughout. Fresh complete unfiltered native Main/Eval/root responses are saved as native-Main.json, native-Eval.json, native-root.json: success=true, partial=false, no failed dependencies/errors. Main retains four pre-existing warnings at1,327,468,469 (header; unused hδ/hQ/hc); Eval/root have no messages. There is no target warning. Only the target body and explicitly authorized Phase3 import grouping/order changed; signature, attached source documentation, header metadata and every other declaration are byte-identical to entry. No pins, axioms, resource raises, sorry, native_decide, count_heartbeats, profiling wrappers, haveI/letI or project helpers were added.

| New library identifier | Verification |
|---|---|
| `IsIntegral.zsmul` | installed source; #check; final compiled proof |
| `Int.sign_mul_self`, `Int.sign` | installed source/core alias; #check for identity; final compiled proof |
| `Int.cast_mul`, `mul_assoc`, `zsmul_eq_mul` | final compiled proof and actual proof dependencies |

### Buzz pass — target only

Outcome: FAST-BOARD for this target. Accepted full-file baseline target205.767ms is reused from the unchanged original target canonical payload in the previous actual full Main capture. Final measurement is a coordinator-approved controlled derivative: exact production imports, module documentation, preceding approxSet command and complete attached target canonical payload, followed only by namespace closure and an observational environment command. Its full prefix bytes bind to final production bytes in prefix-binding.json. Baseline full-file and final scoped timings are separate measurements; no speedup ratio or same-context improvement claim is made.

Owner HOLD→ACK preceded all preparation; compiler/native checks finished and drained before capture. Actual command: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-main-integral-multiple/FinalPrefix.lean`, exit0 in41.878730s. Raw stdout4330073bytes, SHA25aff0c8f097043a2b26f45db2dbd41708ebb3c98b29325ae66ee535edb69191. All five launch groups and capture driver terminated;37 frozen source/prefix/project-olean/toolchain/tool inputs stayed exact. Full parent and Lake environment bytes were compared in memory, persisting only hashes/lengths and PATH/LEAN/toolchain allowlist; unrelated process arguments were not collected. Reused accepted immutable tool/import provenance has narrow current binary/project-input equality, not a new global transitive export. Defaults before/after200000/20000/512. Explicit owner RELEASE followed the entire-phase drain notice before raw parsing. Trace parsed strictly line-by-line; no whole-trace decoding.

Full doc/signature/body canonical payload matches using whitespace/standalone-comment layout normalization only, with no finite parenthesis exception required. Fresh actual target family is exactly the theorem plus `_simp_1_1` and `_simp_1_2`; all three full TYPE/universe payloads match production, and both generated helper VALUES match exactly. The main VALUEs are truthfully unequal across module contexts: exactly one hygienic lambda binder Name contains `_stdin` versus `Roth.Main`. Both actual Names pass hasMacroScopes and have equal eraseMacroScopes in Lean; all other constructor bytes are exact under that single explicit subterm comparison. This is not a broad normalization or a claim of strict VALUE identity. Raw differing values and the initially failed stronger cross-context assertion remain recorded in cross-context-value-difference.json and the tool transcript. Production actual VALUE verification above remains the semantic gate.

| Disjoint root | Milliseconds | Raw line |
|---|---:|---:|
| outer Elab.command |29.493|1718|
| asynchronous target proof |101.278|4954|
| generated `_simp_1_1` addDeclCore parent |0.129|26394|
| generated `_simp_1_2` addDeclCore parent |0.172|26399|
| main target addDeclCore parent |13.199|26704|
| runLintersAsync |8.703|26706|
| **Complete target total** |**152.974**| |

Nested actual kernel checks0.121/0.165/13.156ms are retained as family evidence and not double-counted. No compiler root and no lazy prior-DATA root occur in this target interval; all roots and complete lint subtree are included. 152.974ms <750ms, so no repeat-band capture is required; mandatory1000ms gate passes. No resource raises removed or added. Other Main hotspots remain assigned to their own workers; no global performance pass is claimed.

### Gate status — `exists_nat_mul_isIntegral` (Phase4)

| Gate | Result | Details |
|---|---|---|
| lake_build_file / full build | pass | actual full lake build exit0/63.249853s, then separate Eval build exit0/31.766677s |
| definition_protected | pass | no def/abbrev changed |
| theorem_statement_protected | pass | signature bytes and full original TYPE exact |
| structure_gate | pass |3 proof lines, no branches; conjunction links one existential witness |
| naming_gate | pass | descriptive name, no forbidden pattern/abbreviation; no rename needed |
| line_packing_gate | pass | both unchanged signature lines measured above |
| inequality_orientation_gate | pass | sole0<M oriented; no ≥/> in Lean code |
| cumulative_no_unintended_breakage | pass | full/Eval builds and fresh complete Main/Eval/root native diagnostics |
| semantic/trust/defaults | pass | actual five TYPE/opaqueVALUE checks, independent proofs, upstream origins, acyclic family |
| performance | pass | complete actual3-member family152.974ms, below1000ms/no repeat band |

Overall: pass for the target. No whole-Main cleanup or all-declaration performance completion claim.

### Result: `exists_nat_mul_isIntegral`

Before12 lines; After5 lines; Saved7 (body10→3). Whole Main689→683 because the authorized import grouping adds one blank line. Audit issues found3; fixed3; refactoring deferred0. Rules applied:1.4,1.10,1.15,1.17,2.3,2.13. Renames queued:none. Comments preserved:no inline comments present; attached source docstring exact. Refactoring needed:none. Production SHA256 bcc3896029a20299b992e00686ead45d38b0a4e2a70e9a9e0c40f3757a06112c,36930bytes. No Git/shared-log/queue/other-declaration writes performed.

Phase checklist:
- [✓] Step1 required references read.
- [✓] Step2 full24-item audit printed.
- [✓] Step2.5 all five search methods and strict-rule status printed.
- [✓] Step2.6 complete binder/generalisation/drop-test/literature status printed.
- [✓] Step2.7 both signature widths measured.
- [✓] Step2.8 all inequality occurrences scanned.
- [✓] Step3 all42 golfing rules individually addressed.
- [✓] Step4 reflection, original replay and different independent proof completed.
- [✓] Step5a fresh complete Main/Eval/root native diagnostics passed.
- [✓] Step5b all target protection/content/build/semantic/performance gates passed.
- [✓] Step6a no rename required; no queue write.
