### Auditing: `Roth.approxSet` (lines 48–49, 2 lines)

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. Installed Lean4/mathlib-quality skills, style-rules and naming-conventions also read.

1. LINT: none in target; complete fresh Main native diagnostics success=true, partial=false, no failed dependencies; four existing warnings at 1,333,474,475.
2. HAVE SCAN: n/a: data term contains no `have`.
3. SET_OPTION: none; defaults 200000/20000/512 independently checked.
4. SIMP SQUEEZE: n/a: no simp calls.
5. NAMING: `approxSet` returns set data and follows lowerCamelCase, describes approximation set, no forbidden abbreviation or numeric pattern, not single letter; no rename warranted.
6. LINE PACKING: one signature line, measured below. Whole definition cannot join: 40+1+62=103 codepoints.
7. BY PLACEMENT: n/a: term-mode data construction has no `by`.
8. FORMAT: body 2-space indentation, no internal blank lines or tactic chains; no haveI/letI.
9. COMMENTS: no inline comments; attached source docstring preserved byte-for-byte.
10. DOCSTRING: present, describes approximations of quality κ and source §6 eq.(1), no proof strategy.
11. VISIBILITY: retain public: direct external users in Roth/LeanEval.lean lines17,32,46, plus Main API.
12. STRUCTURE: one-line set body, no branches; conjunction is set-membership content, not a theorem conjunction to split.
13. MATHLIB: five-method search below. Partial match LiouvilleWith has different type and mathematical content; retain individual-pair set.
14. JUNK DEF: substantive named mathematical object; used by denominator finiteness, reduction, reduced approximants, exists_approximants, Roth statements and LeanEval. Inlining duplicates predicate and hides public theorem's mathematical object. Not a composition wrapper.
15. EXISTS LEMMA: n/a: not an existential lemma.
16. SHOW vs CHANGE: n/a: no show.
17. PUSH_NEG: n/a: no push_neg.
18. GENERALISE: all parameters operational data, no hypotheses or typeclass constraints to weaken; table below. Abstract ambient field would require a new real-power operation and public API restatement without downstream benefit; no supported change recommended.
19. INEQUALITY: 0 occurrences of ≥ or > in Lean target; two < occurrences already smaller-first; table below.
20. NORMAL-FORM: direct Set.ofPred comprehension and positive denominator, ordinary real rpow threshold. No canonical equivalent replacement identified; retain. LiouvilleWith is an infinitude predicate with arbitrary C and nonzero error, not this set.
21. SYNTAX-GEN: OK: pair set supports membership, Infinite, images, bounded-denominator subsets directly at actual call sites. Scratch independent intersection construction equivalent by rfl both ways, but adds syntax with no application benefit.
22. IMPORT-FANOUT: n/a: no new imports.
23. CASTS: diff casts: 0 dropped / 0 kept cross-type / 0 kept load-bearing (empty diff). Existing integer-to-real numerator and natural-to-real power base are genuine cross-type coercions; preserve.
24. INSTANCE-NAME: n/a: definition is not an instance.

Issues to fix: none.
Refactoring needed: none.

### Line packing — `approxSet`

Reference: n/a — definition.

| Sig line | Chars | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 48 | 40 | no next signature line; body begins at49 | n/a: signature ends at := | ok |

The body has64 codepoints including indent; unindented62, so entire declaration would need103.

### Inequality scan — `approxSet`

| # | Location | Original | Rewrite | Rename? |
|---|---|---|---|---|
| 1 | body49 | `0 < hq.2` | already oriented | none |
| 2 | body49 | `|α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ` | already oriented | none |
| — | signature48, all hypotheses | no ≥ or > | none required | no _ge_/_gt_ name |

### Mathlib search-status: `approxSet`

[A] Lean-Finder: individual integer/natural pairs with real power error bound; hits LiouvilleWith, Liouville.frequently_exists_num, Real.ContfracLegendre.Ass.
[B] Loogle: `ℝ → ℝ → Set (ℤ × ℕ)` returned empty, isError=false; no absence inference from this alone.
[C] LeanSearch: first descriptive query timed out; bounded retry `LiouvilleWith` succeeded with definition and rat_mul/sub_nat_iff.
[D] Source search: untruncated full-name `approxSet` search over mathlib NumberTheory returned none. Read exact LiouvilleWith definition at lines51–52; it is `∃ C, ∃ᶠ n in atTop, ∃ m, x ≠ m/n ∧ |x-m/n| < C/n^p`. DiophantineApproximation.Basic has Legendre.Ass with coprimality and a different threshold.
[E] Local name pattern `approx`: target, bounded-denominator theorem and unrelated measurable/Urysohn approximations; index unavailable (therefore no absence claim). Actual partial-match definition verified from installed source.

Auxiliary variants: LiouvilleWith.exists_pos/mono/frequently_lt_rpow_neg, Legendre.Ass; these concern different propositions/thresholds. Common-equivalents lookup: no matching bucket.
Concluded: partial match LiouvilleWith; retain existing Set.ofPred construction, built directly on mathlib set/real arithmetic. No new declaration asserting a mathlib absence claim was introduced; independent scratch construction and both definitional equivalences compiled. Six strict rules reviewed: no wrapper theorem, no custom class predicate, no equivalent found requiring deletion, no new mathlib-use documentation needed.

### Generalisation status: `approxSet`

| # | Parameter | Class | Used as | Mechanical candidates | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `(α : ℝ)` | structure value | target of error subtraction | drop inspection: free occurrence in body, deleting binder changes API/introduces implicit binder; no hypothesis drop; type follows real arithmetic | n/a: no meaning-preserving small candidate | keep |
| 2 | `(κ : ℝ)` | structure value | real exponent | drop inspection: free occurrence as rpow exponent; no strict/global hypothesis, typeclass or universe binder | n/a: no meaning-preserving small candidate | keep |

No proposition/typeclass/decidability/type-variable/universe hypotheses omitted. Strict→weak does not apply to inequalities inside the set's defining predicate: replacing them changes the object rather than weakening a theorem assumption. Inversion check n/a: data construction, no named-witness proof after unfolding.
Big-change candidates: none recommended; abstract base fields, simultaneous/p-adic approximation are different APIs requiring further mathematical structure, not removal of unnecessary assumptions here.

### Literature search status: `approxSet`

[A] WebSearch query: `Roth theorem rational approximation pairs denominator exponent generalization`. Top3 returned: rational approximations to differential equations (PMC384210), GNT lecture notes §4.5 Roth's theorem, and Thue–Siegel–Roth–Schmidt for algebraic functions (1978). These generalizations change the approximation problem and do not justify changing this elementary set. Primary original Roth article and standard irrationality measure formulation also returned. Relevant primary source: https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F . Standard formulation reference https://en.wikipedia.org/wiki/Irrationality_measure confirms real target/rational approximants/positive denominator.
[B] ChatGPT math MCP n/a: no such tool available.
Literature-driven big-change candidates: none supported for this definition.

### Golfing rule pass

Phase1:
[1.1] n/a: no by exact wrapper.
[1.2] n/a: no by rfl.
[1.3] n/a: no rw/exact.
[1.4] n/a: no simp/exact.
[1.5] n/a: no trailing rfl.
[1.6] n/a: no proof constructor.
[1.7] n/a: no apply/exact.
[1.8] n/a: no contradiction proof.
[1.9] n/a: set predicate depends on both projections and α/κ, not eta form.
[1.10] n/a: no have.
[1.11] n/a: no apply/intro.
[1.12] n/a: no show.
[1.13] n/a: no have projections.
[1.14] n/a: no rw.
[1.15] n/a: no simp only.
[1.16] n/a: no simp.
[1.17] n/a: no eligible method call.
[1.18] n/a: no avoidable argument parentheses; casts load required type.
[1.19] n/a: no push_neg.
[1.20] n/a: not a private existential lemma.
Phase2:
[2.1] n/a: data-valued construction; grind would be proof automation, not data definition.
[2.2] n/a: no grind.
[2.3] n/a: no simp chains.
[2.4] n/a: no function-property proof.
[2.5] n/a: no positivity proof goal.
[2.6] n/a: no inequality proof goal.
[2.7] n/a: no Nat/Int arithmetic proof.
[2.8] n/a: no proposition proof.
[2.9] n/a: no numeric/cast proof.
[2.10] n/a: not a decidable proposition to prove.
[2.11] n/a: not an algebraic identity proof.
[2.12] n/a: no ring proof or hypotheses.
[2.13] n/a: no symmetric cases.
[2.14] n/a: no calc.
[2.15] n/a: no subgoals.
Phase3:
[3.1] n/a: no erw.
[3.2] n/a: no continuity/measurability tactic.
[3.3] n/a: no omega.
[3.4] n/a: no rcases.
[3.5] n/a: no new lemma or automation-registration need.
[3.6] n/a: no simp_all.
[3.7] n/a: no resource option.

### Step back and think

Already a direct term-mode set construction. A tactic proof, exact?/apply? search for a proof, or optional membership companion would not simplify construction. Independent construction as intersection of denominator-positive pairs and error-bounded pairs checked with rfl in both directions. Kept existing comprehension because it is shorter and used directly by APIs; no helper/extraction warranted. Target source unchanged from genuine original as well as entry snapshot.


### Verification and timing — `approxSet`

Independent.lean compiled exit0: independentlyConstructed uses intersection of two sets, both equivalences proved by rfl. Actual target family dynamically checked exactly [Roth.approxSet]. Its full TYPE and opaque VALUE compared recursively to saved original Expr constructor trees without ExprBEq shortcircuit: binder names/info, names/universes, let flags, literals, metadata and projections preserved. Current full emitted TYPE/VALUE/universes/axioms/name also equal original accepted raw pair. Value inferred type matches; no mvars/levelmvars/freevars/loose binders/sorryAx/self dependency; only propext, Classical.choice, Quot.sound. Scratch constructions are evidence only, not new project API.

Fresh full unfiltered Main diagnostics passed (four existing warnings); fresh Eval/root each passed without messages. Full objects saved in native-receipt.json and native-Main-full-response.json; Main response faithfully transcribed from actual returned response with provenance, no invented timing. Empty worker.diff; genuine original/entry/current target code equal (target code SHA5afd616731229f9be85a1ced23a509ca255c0794b76b2c9ceb6e56f40f753d53).

Main source SHA6668ff83a7e7b156f6f29b8f2d0163e699da002b70338d5ee0715065ade9b25f. All17 recorded project input identities exactly match accepted full-build then Eval-build evidence, so no unchanged build repeat. Full lake build exit0 78.484126s, then separate lake build Roth.LeanEval exit0 29.257324s; both actual process groups absent. Evidence: /private/tmp/roth-mainlemma-wholefile-final1/build-final-{full,eval}-result-v1.json and build-final-source17-v1.json; reuse binding same-source-build-reuse.json.

Explicit HOLD→owner ACK→complete capture/maps/env/freeze/drain→owner explicit RELEASE occurred before raw parsing. One actual capture `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Main.lean`, exit0 394.590105s. Raw stdout316988310 bytes SHA571e61badc4bef4cfff57ec39643dd26150ae32858be02cc940defaa9db5cfbb. Capture and all5 launched process groups drained; driver session exited0. Full parent and Lake environment bytes compared in memory, only hashes/length plus PATH/LEAN/toolchain allowlist persisted; unrelated process arguments never collected. Frozen source/olean/toolchain inputs exact before and after each launch. Carried tool identity evidence: /private/tmp/roth-main-owner/approxSet-reused-tool-identity.json binds four actual proxy/resolved binaries current-byteexact to prior accepted final-safe/initial-identities.json; this is explicit prior-map reuse plus current equality, not newly observed pre-phase binary hashes. Defaults200000/20000/512 before/after. Initial sandbox process-read denial preceded all captures and was resolved by approved read-only process check escalation.

Complete attached canonical payload matched after whitespace/standalone-comment layout normalization only. Actual target generated family is singleton Roth.approxSet. Sum of disjoint roots:

| Root | Milliseconds | Raw line |
|---|---:|---:|
| Elab.command outer |31.634|216|
| addDeclCore async parent (actual kernel Roth.approxSet)|0.128|1652|
| compileDecls async parent (actual compiler Roth.approxSet)|0.068|1654|
| runLintersAsync|15.686|1657|
| Total |47.516| |

Nested kernel0.119ms and compiler0.030ms retained as family evidence but not double counted. No separate proof root for DATA; no lazy prior DATA kernel roots. Full lint subtree included through its async parent. No threshold rejection and no >=750ms repeat band; no unchanged extra capture. approxSet-profile-acceptance-v2.json contains full source/printed payload and root offsets; raw streamed line-by-line, never decoded as one whole trace. Optional all17 map has16 exact canonical bindings and one explicitly unaccepted mismatch (abs_eval_lt_of_le_index); no all-file performance pass claimed. Existing unrelated Main overbudget rows remain for their own workers.

### Gate status — `approxSet` (Phase4)

| Gate | Result | Details |
|---|---|---|
| lake_build_file | pass | exact unchanged source: actual full-build78.484s then separate Eval29.257s exit0 reused |
| definition_protected | pass | empty worker diff; full original TYPE/VALUE preserved |
| theorem_statement_protected | pass | no theorem signature changes |
| structure_gate | pass | one-line data body, no proof branches; no theorem conjunction |
| naming_gate | pass | descriptive lowerCamelCase data def, no forbidden patterns/abbreviations |
| line_packing_gate | pass | all signature lines measured; only line48, 40codepoints, body starts after := |
| inequality_orientation_gate | pass | no ≥/> in signature/body; both existing < correctly oriented |
| cumulative_no_unintended_external_breakage | pass | fresh Main/Eval/root complete diagnostics plus same-source full/Eval build gates |
| performance | pass |47.516ms complete disjoint work, below1000ms; no repeat band |

Overall: pass for target; no global Main completion/performance claim.

### Result: `approxSet`

Before2 lines; After2 lines; Saved0. Audit issues found0; Fixed0; Refactoring deferred0. Rules applied:none (direct data construction; all rules individually considered above). Renames queued:none. Comments preserved:no inline comments; attached docstring unchanged. Refactoring needed:none. Source changes:none. Only target report written in project; no Git/central/queue changes.

Phase checklist:
- [✓] Step1 reference docs read.
- [✓] Step2 full24-item audit printed.
- [✓] Step2.5 five-method search-status block printed.
- [✓] Step2.6 generalisation and literature status printed.
- [✓] Step2.7 all signature widths measured.
- [✓] Step2.8 all inequality occurrences scanned.
- [✓] Step3 every golfing rule has individual status.
- [✓] Step4 reflection and independent construction done.
- [✓] Step5a fresh complete Main/Eval/root native diagnostics passed.
- [✓] Step5b protection/content/build/performance gates passed on target.
- [✓] Step6a no rename required; no queue write.
