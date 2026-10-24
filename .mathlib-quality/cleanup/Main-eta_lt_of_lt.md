# Result: `Roth.eta_lt_of_lt` — original Main declaration 9

Complete single-declaration cleanup. Proof body 6 → 3 physical lines; declaration 8 → 5 lines; Main 635 → 632 lines. Source SHA256 `910ef04480715846d6b22eacf0aa70f5d9e260e0af2abccfef644088758fbc83`, 34,752 bytes. Scope is target plus the owner-leased sole caller repair and this report; no Git/shared-progress/rename-queue writes, no new source helper or import, no next target edit.

The two positive-base hypotheses were safely weakened to nonnegativity, keeping the conclusion exactly `eta δ m < 10 ^ m * c`. The original strict contract is recovered by an actual opaque proof whose complete type matches the accepted original type strictly. The sole caller `exists_delta` supplies `.le` proofs; its full original type and actual opaque proof value passed fresh checks. A direct mathlib inverse-power equivalence replaces the manual rpow rewrite chain. The private docstring becomes an ordinary comment with identical prose.

## References and entry preservation

Read installed mathlib-quality and lean4 SKILL.md, full cleanup.md/cleanup-all.md, full golfing-rules/proof-patterns/mathlib-search/generalisation-patterns/cleanup-gates, relevant style rules and naming conventions, and profiling reference. Actual built-in Skill(simplify) unavailable; no false invocation claim. Owner independent exact-diff review supports final proof and has no additional recommendations. Fresh independent whole-file review remains with owner at file final.

Before any Lean or golf, saved genuine original Main and entry Main, plus each target separately. `entry-original-save.json` proves exact target bytes equal: SHA256 `9b267dc7478d7ab244461aae66ea597a9b7ba59356132e6fa744021c6461be43`; genuine original Main SHA `f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069`, entry SHA `ba920c954bb74fe8012f5c01fdbdf2e87740256028c9ad093ba190f8e9c1ae00`. Exact earlier build/native/LSP evidence was reused only for baseline, without redundant unchanged-source compiles. Lean 4.34.0 and project/mathlib pins unchanged.

# Auditing: `eta_lt_of_lt` (entry lines 213–220, 6 physical body lines)

1. LINT: accepted same-source complete Main diagnostics have no target-range warning.
2. HAVE SCAN: `hz` at L215 has `by positivity`, used once at L216; valid proof-content have, test inline. `hpow` at L216 has no `by`, used at L218 rewrite and L220 conclusion (2 uses); keep mutable local or replace with direct equivalent rpow API if verified.
3. SET_OPTION: none in declaration.
4. SIMP SQUEEZE: no simp call in original.
5. NAMING: `eta_lt_of_lt` is snake_case, subject eta and conclusion lt under lt premise. No forbidden abbreviation, scheme number, or reversed inequality; no new rename needed. Do not expand five accepted global END renames.
6. LINE PACKING: two original signature lines; measure final widths and next-token arithmetic below.
7. BY PLACEMENT: original by at end of L214; preserve.
8. FORMAT: original uses two-space proof/four-space signature continuation, no empty body lines or semicolon chains; preserve.
9. COMMENTS: no inline proof comment. Preserve mathematical meaning of existing single comment by changing private docstring to ordinary comment.
10. DOCSTRING: private declaration must have no API docstring; convert opener `/--` to `/-`.
11. VISIBILITY: already private, sole caller `exists_delta`; retain. A mathematically named private local estimate does not require speculative renaming.
12. STRUCTURE: 6 physical body lines, no conjunction or branch; no extraction required.
13. MATHLIB: five-method status below. Existing rpow monotonicity is a partial match; eta is project-specific.
14. JUNK DEF: n/a, theorem not definition.
15. EXISTS LEMMA: n/a, conclusion is inequality.
16. SHOW vs CHANGE: `show (2 : ℝ) * (1 / 2) = 1 by norm_num` is term-mode rewrite argument, retained unless replaced by simpler API proof.
17. PUSH_NEG: none.
18. GENERALISE: strict δ/c positivity used only via .le. Bounded actual test simultaneous 0 ≤ δ/0 ≤ c with same conclusion and required .le removal; caller repair lease obtained conditionally. All six binders classified below.
19. INEQUALITY: no ≥ or > in signature; all inequalities already smaller-side-left.
20. NORMAL-FORM: existing eta estimate is canonical for local caller, no simp attribute or new equivalence.
21. SYNTAX-GEN: explicit m and power threshold match caller; no conclusion restatement.
22. IMPORT-FANOUT: n/a, no import changes.
23. CASTS: original `(0 : ℝ)` and `(1 / 2 : ℝ)` fix rpow base/exponent numerals; `(2 : ℝ)` in term equality is load-bearing. Audit final diff separately.
24. INSTANCE-NAME: n/a, no instance declaration.

Issues to fix: (1) private docstring → ordinary comment with identical content; (2) test/retain nonnegative δ/c assumptions when verified; (3) bounded golf to remove redundant positivity scaffolding or use existing inverse-power API, with exact conclusion preserved.
Refactoring needed: narrow sole caller .le repair is authorized conditionally on verified weakening. No optional extraction/generalization or new global rename.

## Generalisation status

| # | Binder | Class | Use | Catalogue/drop-test assessment | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | δ : ℝ | structure value | eta and threshold | Cannot drop: free in conclusion/premise; abstract field restatement outside project eta domain | source | retained |
| 2 | c : ℝ | structure value | bound and threshold | Cannot drop: free in conclusion/premise; concrete eta fixes ℝ | source | retained |
| 3 | hδ0 : 0 < δ | proposition | rpow monotonicity nonnegativity | strict→weak 0 ≤ δ; drop loses the base-sign premise of the existing rpow API; source-use check rejects deleting this binder, no extra compiled drop variant claimed | pending | pending |
| 4 | hc : 0 < c | proposition | rpow multiplication nonnegativity | strict→weak 0 ≤ c; drop would admit negative c and even threshold, invalid for δ=0,c=-1,m=1 | pending | pending |
| 5 | m : ℕ | structure value | iterated-root exponent and 10-power | Cannot drop free m; no pointwise/universe candidate | source | retained |
| 6 | h : δ < c^(2^m) | proposition | strict rpow comparison | drop/weakening to ≤ cannot preserve strict conclusion at δ=c=1 | semantic | retained |

No typeclass/decidability/type-variable binder; no universe or point-localize candidate. Big-change candidates: none in authorized scope. Inversion check: eta unfolds once and remaining proof is the standard rpow estimate; reuse existing `Real.rpow_inv_lt_iff_of_pos` rather than creating new abstraction. Literature: n/a, private decl, literature search not required.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | complete signature | n/a — zero ≥ or > | none | none: name uses lt |

## Mathlib search-status: `eta_lt_of_lt`

| Method | Actual query / status | Result |
|---|---|---|
| A Lean-Finder | real power root inequality x < y^n implies x^(1/n) < y for nonnegative reals | `Real.rpow_inv_lt_iff_of_pos`, `Real.lt_rpow_inv_iff_of_pos` |
| B Loogle | `Real.rpow, _ < _ ^ _` | no hits for this query; no absence claim |
| C LeanSearch | nonnegative real x below y to a positive natural power implies reciprocal-power bound | `Real.rpow_inv_lt_iff_of_pos` |
| D source search | untruncated `rpow_inv_lt_iff_of_pos`, `rpow_natCast`, `rpow_mul_natCast`, `rpow_natCast_mul`, `rpow_lt_rpow` in Pow/Real.lean | local pinned source confirms reciprocal-power theorem at line 593; monotonicity at 538; cast at 62 |
| E name pattern | `rpow_lt` local search, 30 results, index unavailable | text-backed hits include `Real.rpow_lt_rpow` and variants; result is presence evidence only |

Auxiliary variants inspected: inverse-power `<`/`≤`, `rpow_lt_rpow_iff`, `rpow_natCast_mul`, `rpow_mul_natCast`, `_of_pos`, negative-exponent variants. Common-equivalents table: no discrete/finiteness/separation/bornology match. Conclusion: partial match `Real.rpow_inv_lt_iff_of_pos`; retain the project eta estimate and build its proof directly on the existing mathlib API. No new abstraction, wrapper or generic missing-lemma claim. Six rules: no new wrappers/predicates; replacement is a partial match, not whole eta theorem; exact?/apply? actual live probes attempted; full existing-name source verified; no imports or module documentation expansion needed for this scoped private proof change.

The whole-proof `lean_multi_attempt` batch tried `grind [eta]`, `exact?`, `apply?`, `aesop`, `simp [eta]`, and one multiline inverse-power attempt. `grind` and `aesop` failed; `exact?` found no closing term; `apply?` returned partial conversion suggestions rather than a closed proof. `simp [eta]` exposed the exact inverse-power goal. The multiline attempt was malformed in line-replacement context and is not claimed as proof evidence. The raw batch result was excessively large due to apply? partial suggestions and not saved in full. Direct live edits then verified the final three-line proof. Two direct cast variants failed (natural versus real exponent) before the final explicit cast plus `simpa only [Real.rpow_natCast]` conversion passed.

## Golfing rule pass (all 42)

| Rule | Status / evidence |
|---|---|
| 1.1 by exact wrapper | n/a: original had six tactics, no by-exact wrapper |
| 1.2 by rfl | n/a: no by-rfl proof |
| 1.3 rw + exact | original final rw/exact chain superseded by terminal simpa from reciprocal-power API |
| 1.4 simp + exact | applied conceptually via final simpa-using consolidation |
| 1.5 trailing rfl | n/a: no trailing rfl |
| 1.6 constructor pair | n/a: inequality has no constructor |
| 1.7 apply + exact | n/a: no original apply/exact pair |
| 1.8 by_contra + push_neg | n/a: neither occurs |
| 1.9 eta reduce lambdas | n/a: no lambda |
| 1.10 inline single-use have | original hz positivity and hpow rewrite scaffolding removed by direct rpow API |
| 1.11 apply + intro | n/a: no introductions |
| 1.12 redundant show | original term-mode numeric show removed with old rewrite chain; final show fixes real positivity goal and is load-bearing |
| 1.13 have with projections | n/a: no conjunction projections |
| 1.14 consecutive rw | n/a: original rewrites act on different locations; both superseded by API |
| 1.15 terminal simp only | no original simp; final inner simpa-only cast conversion is necessary: bare simpa actually failed by rewriting casts too early |
| 1.16 nonterminal bare simp | n/a: final simpa calls are terminal in their subproofs |
| 1.17 dot notation | `.2` selects implication from mathlib equivalence; no superior dot-notation rewrite needed |
| 1.18 use <| | n/a: parentheses identify an Iff projection or a proof argument inside a larger application; no trailing by-parenthesis-only wrapper |
| 1.19 push_neg | n/a: absent |
| 1.20 trivial existential | n/a: no existential conclusion |
| 2.1 grind | actually tried `grind [eta]`, failed on strict eta bound |
| 2.2 delete before grind | n/a: no retained grind |
| 2.3 simpa consolidation | applied; final proof is simpa using inverse-power equivalence |
| 2.4 fun_prop | n/a: no analytic function-property goal |
| 2.5 positivity | applied at positive real natural-power exponent; original positivity worked too |
| 2.6 gcongr | bounded malformed multiline attempt included gcongr, not accepted; final simp cancels positive 10^m factor automatically |
| 2.7 lia/omega | n/a: goal concerns real rpow, not linear Nat/Int arithmetic |
| 2.8 aesop | actually tried; made no progress |
| 2.9 norm_num/norm_cast | old norm_num numeric rewrite removed; final explicit nat-to-real cast and rpow_natCast bridge handles mathematical type distinction |
| 2.10 decide/kernel | n/a: arbitrary real inequality is not finite computation |
| 2.11 field_simp/ring | n/a: no polynomial equality or rational-expression identity goal |
| 2.12 linear_combination | n/a: no ring-ending proof with algebraic hypotheses |
| 2.13 wlog | n/a: no symmetric case branches |
| 2.14 calc collapse | n/a: no calc block |
| 2.15 close multiple goals | n/a: no parallel similar goals |
| 3.1 erw→rw | n/a: no erw |
| 3.2 continuity/measurability | n/a: absent |
| 3.3 omega→lia | n/a: no omega |
| 3.4 rcases rfl | n/a: absent |
| 3.5 automation attributes | n/a: one local eta estimate does not need global automation registration |
| 3.6 simp_all | n/a: no simp_all-only |
| 3.7 remove maxHeartbeats | n/a: no declaration option or limit raise |

## Step back and think

The mathematical proof raises a threshold to its reciprocal power and cancels the positive 10^m factor. Search found exactly that inverse-power API, so the explicit monotonicity/rewrite proof became three lines. Whole-goal automation did not close it. Term mode would obscure the needed natural/real exponent conversion; the accepted terminal simpa is shorter and exposes the mathematical API. No helper extraction or optional abstract restatement is needed.

## Final generalisation findings

Both strict→weak substitutions passed actual compiled `WeakEta.lean`, then complete live Main diagnostics passed with the caller repaired under its narrow lease. The conclusion string and binder order are unchanged. The weakening is small-safe and explicitly authorized. The three proof hypotheses all have mathematical uses: δ nonnegativity enters `rpow_inv_lt_iff_of_pos`, c nonnegativity enters the same theorem, and h supplies its right side. Drop-test source checks fail at those exact references; the source-level checks are not misreported as compiled drop variants. Weakening h itself to ≤ or dropping it cannot prove the strict conclusion at δ=c=1. Concrete δ,c,m are free in statement so cannot be removed. No typeclass, point-locality, decidability, or universe weakening applies. Inversion result: existing generic rpow theorem already supplies the abstraction, so no new generic theorem or companion is introduced.

## Line packing: `eta_lt_of_lt`

| Signature line | Codepoints | Next complete signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 213 | 95 | `eta δ m < 10 ^ m * c := by` (26) | 95 + 1 + 26 = 122 > 100 | ok |
| 214 | 30 | no next signature line | n/a, proof begins next | ok |

The cast observation at width 100 is captured in the profile prefix. Original signature widths are also 95 and 30. No ≥/> occurs in final signature, so the inequality scan has one explicit zero-occurrence row in the initial audit. Name is snake_case and uses neither a forbidden token nor numbering; private declaration remains private. New `.le` caller syntax refers to existing strict proofs and retains their other uses.

## Cast audit

Final added code: `(0 : ℝ)` fixes the positivity statement's ambient field; `(2 ^ m : ℕ)` fixes the natural exponent before the genuine ℕ→ℝ coercion. These are load-bearing (the two failed actual live variants demonstrate the natural/real exponent ambiguity). No redundant annotation was added. The old real `(1 / 2 : ℝ)` and `(2 : ℝ)` scaffolding disappeared with the rewrite proof. Status: 0 redundant casts dropped / 1 cross-type ℕ→ℝ coercion retained / 2 explicit load-bearing ascriptions retained. No instance name or local-instance syntax introduced.

## Simplify review

Actual `Skill(simplify)` is unavailable in this host; no invocation is claimed. Owner independently reviewed the exact final source diff and found no additional source recommendations. This targeted review and the step-back analysis found no duplication, extra imports, unexplained coercions, or extraction need. Fresh independent whole-file review remains with owner at file final.

## Qualifications

Scratch absolute-path LSP request failed because the temporary file had no Lean-project ancestor; actual weak proof compilation and live-file complete diagnostics passed later. The malformed multi_attempt multiline probe is not counted as evidence; the accepted direct live proof is. Two cast failures were repaired and final whole-file LSP was clean. Old accepted evidence extraction sought the two indexed target/caller rows only, checked their raw row hashes, and persisted TYPE/metadata with VALUE omitted. However, json.loads transiently decoded the old caller's 26MB VALUE in memory before discarding it, contrary to the requested TYPE-only decoding. It was not printed, persisted, or re-inferred; no repeat or broad remediation was performed. This bounded-read protocol deviation does not support any claim of old/current VALUE identity.


## Gate status — `eta_lt_of_lt`

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build | pass | `final-full-build`: actual `lake build`, exit 0, 57.773s |
| lake_build_file | pass | full build includes Main; separate `lake build Roth.LeanEval`, exit 0, 31.506s; root default target excludes Eval |
| definition_protected | pass | snapshot diff has no def/abbrev/import edit |
| theorem_statement_protected | pass, authorized weakening | item18 and binding owner scope authorize strict→weak hypotheses; same conclusion and old full contract recovered strictly; caller TYPE unchanged |
| structure_gate | pass | 3 proof lines, no conjunction/branch; no extraction needed |
| naming_gate | pass | mathematical snake_case eta_lt_of_lt, no forbidden abbreviation or numbering; no new rename |
| line_packing_gate | pass | complete two-line width table 95/30, 95+1+26=122 |
| inequality_orientation_gate | pass | signature occurrence scan zero ≥/>; name uses lt |
| cumulative_no_unintended_breakage | pass | complete Main/Eval/root diagnostics and fresh native compiles; actual caller full TYPE and VALUE checked |
| default/axiom/value gate | pass | defaults200000/20000/512; actual opaque values inferred closed and standard axioms only |
| performance gate | pass | exact-prefix 127.774ms, no ≥750 repeat needed |

Overall: pass. `Main-worker.diff` is captured against entry; its only code changes are the audited private lemma and the exact leased caller `.le` arguments.

## Verification evidence

All compiler/native and LSP work was strictly serial, with no compiler/native/semantic driver overlapping any LSP query. Final live Main complete diagnostics: zero errors, four existing warnings at 1/276/417/418 outside target scope (header plus unused hδ/hQ/hc). Same exact-source diagnostics reused at final without a redundant label call. Fresh complete Eval/root diagnostics: zero errors and zero warnings. All three fresh native checks were complete and unfiltered: Main exit0 29.589s (three existing unused-variable warnings), Eval exit0 27.911s, root exit0 24.383s. No warning suppression or heartbeat/recursion limit raise.

Semantic evidence: `IndependentEta.lean` uses the genuine original monotonicity proof with the successful nonnegative substitutions, different from the new inverse-power proof. It was saved before Lean and compiled exit0 51.081s. `Semantics.lean` compiled exit0 111.418s, checking actual target and independent opaque VALUE in memory, complete strict TYPE equality without Expr.BEq shortcuts, actual level parameters, closure, inference, and only propext/Classical.choice/Quot.sound. The target's raw opaque VALUE was 138,388 bytes; independent's was 331,021 bytes. These are in-memory checked hash/length receipts, not full raw VALUE dumps or proof-identity claims.

Actual root `_private.Roth.Main.0.Roth.eta_lt_of_lt` found via privateToUserName?, family contains exactly that actual name. Independent family is exactly independentEta; both actual universes are []. Fresh local graph has no edges or cycles. All actual external constants have strictly smaller upstream module indices, including Roth.eta from Roth.MainLemma; no same/later Main shortcut, self-target/generated-family dependence, or circular independent proof. No accepted earlier Main helper is needed by this fresh closure. Original-contract recovery is an actual opaque `recoveredOldEta` with strict full original TYPE, and its VALUE was inferred closed/std3. Current caller Roth.exists_delta full TYPE strictly matches accepted Q18 original, with its actual opaque VALUE inferred closed/std3. No VALUE identity across changed proofs/modules is claimed.

Accepted old TYPE metadata came from the two exact indexed Q18 raw rows after validating row hashes; this does not reopen accepted earlier audits. Preserve the bounded-read qualification below: the old caller VALUE was transiently decoded but not persisted/printed/inferred.

## Buzz pass — exact-source declaration checkpoint

Outcome: FAST-BOARD. Final exact-prefix derivative preserves imports, every preceding command, target source, ordinary comment, and namespace close; binding at `final-profile/prefix-binding.json`. Owner HOLD ACK preceded any phase preparation; all writes/heavy review/parsing/compiler/native/LSP on owner side stayed idle until actual capture/driver drain. Only after raw-UNPARSED drain notice and explicit owner RELEASE was any raw profile parsed.

Actual invocation: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 .../final-profile/Prefix.lean`, exit0. Raw stdout39,126,754 bytes, SHA256 `b20e9e14bfde654f8f3484cecea97dde2cb664b3ba95db7ca98c9c2c7a26132f`; separate stderr859 bytes contains cumulative profiler summary, no errors. Canonical complete source matches the printed lemma payload. Disjoint total127.774ms = source lemma outer20.233 + async proof98.665 + kernel-parent2.924 + lint5.952. Nested kernel2.866ms and expanded private-theorem macro command19.364ms are already included in their parents and not doubled; the two command rows both print at indent0, so nesting is justified by installed implementation, not indentation. Expanded command raw byte35795196/line342326 fully matches target after lemma→theorem; source outer is byte35907916/line343827. Mathlib/Tactic/Lemma.lean20–30 expands lemma to theorem; Lean/Elab/Command.lean691–719 wraps recursive macro elaboration in withTraceNode, invokes elabCommand stxNew at770, and finally addTraceAsMessages at695 flushes inner before outer. Exact two-file hashes and raw canonical payload are in final-profile/expanded-command-parent-binding.json; no compiler or lazy DATA roots for target. Actual family `_private._stdin.0.Roth.eta_lt_of_lt` has full5618-byte TYPE and actual universes[] equal to production target; actual VALUE inferred closed/std3 in profile too. Family match is via actual private user name, not guessed prefix names. Default observations before and after both `DEFAULTS=200000/20000/512`; parent full environment bytes and Lake full environment bytes equal in memory only; persisted safe allowlist/hash/length, no full environment or unrelated process arguments. Final frozen source/dependency/tool/map inputs remain exact.

Historical genuine whole-file target114.370ms recorded separately with actual narrow root/kernel bytes checked against original canonical source. Different contexts: no speedup ratio or causal-noise conclusion. Final127.774ms is below750ms, so no repeat or additional capture. MaxHeartbeat raises removed0/added0; deferred none; big changes none. The first end-tail width extractor missed the leading `@` and asserted; correcting that text selector produced the actual width100 observation without a new Lean/capture. Actual #check output is kept at `final-profile/check-width100.txt`; its printed @name prefix makes the one-line observation102 codepoints, while production signature is independently measured95/30.

## Result and phase checklist

Audit issues found3; fixed3: private docstring, excessive positivity assumptions with caller repair, and manual rpow proof scaffolding. Physical proof lines saved3. Rules applied1.3/1.4/1.10/1.12/2.3/2.5; 42/42 rule slots assessed above. Renames queued none; existing five global END renames untouched. Comments preserved1/1 as identical ordinary comment, none deleted. Refactoring needed none. No new helper lifecycle or additional independent source reviewer needed: no helper was added to project source; owner exact-diff review is recorded.

- [✓] Step1 references read.
- [✓] Step2 full24-item audit.
- [✓] Step2.5 five-method search-status.
- [✓] Step2.6 all six binders classified, bounded actual strict→weak test kept; no extra compiled drop probes claimed (owner instructed no extra probes after supported final source review).
- [✓] Step2.7 complete signature width arithmetic.
- [✓] Step2.8 explicit zero-occurrence inequality scan.
- [✓] Step3 all42 golf-rule statuses.
- [✓] Step4 mathematical step-back and actual exact?/apply?/automation probes.
- [✓] Step5a complete diagnostics clean of errors; existing out-of-scope warnings retained explicitly.
- [✓] Step5b actual build/native/semantic/profile diff gates pass.
- [✓] Step6a no rename needed; shared queue untouched.

## END

All13 known compiler/native/profile/env/default launches exited0, their process groups actually absent in final minimal-metadata ps check, all outer drivers and LSP queries terminal; final frozen inputs exact. Owner explicitly released profile HOLD before parsing. No active jobs, queries, HOLD, or unreleased leases. All scoped source/report/compiler/native/LSP/profile leases RELEASED. No further source edits or Lean jobs planned. Git/publication and shared progress belong to owner. Actual FINAL accompanies this report.
