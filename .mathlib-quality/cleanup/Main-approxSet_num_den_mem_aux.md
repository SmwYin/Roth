# Fresh independent cleanup: `Roth.approxSet_num_den_mem_aux`

Status: helper audit complete for local owner acceptance. This is a fresh independent review of the new private helper, not the author's self-review and not completion of original declaration 7 (`exists_reduced_approx`). Original completion count remains 249. Per the coordinator's updated policy, the owner accepts this helper locally and resumes the same parent author; publication occurs with the completed parent, not as a separate helper checkpoint.

## Provenance and scope

Genuine first ungolfed source: `/private/tmp/roth-main-reduced-approx/helper-first-ungolfed.lean`, SHA256 `90116bcbfff34d8346a59e473caf4bdb15f291bf227f634aa10bd71558a44372`, saved before any helper Lean execution/golf by its author and inserted verbatim. My own entry snapshots, also saved before my Lean/golf, are `/private/tmp/roth-main-normalized-helper/entry-helper.lean` and `entry-Main.lean`. Entry Main SHA256: `89b0b5c29deb60b27e9e3fc4057b3b04acc964e94d227dd497ee651885d13b2c`.

Final helper: **26 → 8 total physical lines; 23 → 6 proof-body lines**. Signature packing accounts for the additional saved line. Main: **660 → 642 lines**, 35092 bytes, SHA256 `642d4a2f648e9ce4f72597bd6e09c1b593585357f3215c3ae8c2f1e3b27feef8`. Final helper SHA256 `58e91718c867d5eb675cf3ce0ec08fe4b5b60094cba415947fc4bc4f307b7646`. Source before and after the helper is byte-identical to my entry. No parent golf, callee-token changes, imports, global rename queue, Git, or shared progress writes.

Read installed mathlib-quality and lean4 skills, full cleanup and cleanup-all commands, golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, naming-conventions, applicable style-rules sections, mathlib-review-stages, profiling and buzz workflow. Actual `Skill(simplify)` is unavailable in this environment; the explicit independent holistic review below is not a claim of invoking it.

## Baseline

The supplied complete same-source partial-Main LSP baseline was 0 errors / four warnings outside the helper; reused as instructed. The genuine helper was independently profiled before any edits: **140.438 ms**. This is its own baseline, not the older parent declaration's timing. No full current-partial-project baseline build was claimed from the published six-declaration checkpoint.

## Full 24-item audit

| # | Item | Concrete result |
|---|---|---|
| 1 | LINT | Final complete Main diagnostics: no helper warnings/errors; four existing warnings elsewhere (header, hδ at 286, hQ at 427, hc at 428). |
| 2 | HAVE SCAN | All five original haves inspected below; final only hden remains. |
| 3 | SET_OPTION | None in helper; none added; default resource limits verified. |
| 4 | SIMP SQUEEZE | Both original empty nonterminal `simp only` calls removed. Final terminal `simpa [x, Rat.divInt_eq_div] using Rat.den_dvd h q` remains unsqueezed. |
| 5 | NAMING | Mathematical subject and conclusion explicit: numerator/denominator membership in approxSet. Correct private `_aux`, no forbidden abbreviation/numeric/scheme pattern. No evidence warrants rename. |
| 6 | LINE PACKING | Original second/third lines underpacked (35 + 1 + 60 = 96); joined. Complete final table below. |
| 7 | BY PLACEMENT | `by` ends final signature line. |
| 8 | FORMAT | Two-space body, four-space signature continuation, no internal blank lines, no haveI/letI, no semicolon chains. |
| 9 | COMMENTS | No helper proof comments originally. Parent's ordinary reduced-solution signpost and all surrounding source preserved byte-for-byte. |
| 10 | DOCSTRING | No docstring on private helper, correct. |
| 11 | VISIBILITY | Classic file; helper remains private and has `_aux`. |
| 12 | STRUCTURE | Six proof lines; no explicit conjunction in signature and no case branches. Set membership's internal positivity/error bundle is the natural contract, not an arbitrary tuple. No additional helper needed. |
| 13 | MATHLIB | Five searches found partial API Rat.den_dvd, not a replacement for the approximation-membership result. Standard cast API removes both conversion subproofs; no missing API remains. |
| 14 | JUNK DEF | n/a: theorem, not data definition. |
| 15 | EXISTS LEMMA | n/a: substantive membership theorem, not a trivial existential witness. |
| 16 | SHOW/CHANGE | None in final proof. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every parameter classified below; proposition drop/weak-bound tests failed and were restored. No warranted generalisation deferred. |
| 19 | INEQUALITY | No ≥/> Lean notation or _ge_/_gt_ identifier in target; scan table below. |
| 20 | NORMAL-FORM | Rat.num/den is the canonical reduced representation; approxSet is the established local membership contract. |
| 21 | SYNTAX-GEN | OK: bundled membership permits the parent's direct invocation; no restatement recommended. |
| 22 | IMPORT-FANOUT | n/a: no imports changed. |
| 23 | CASTS | Removed explicit real cast-identity statement and real denominator-positivity statement. The signature’s two `(h : ℚ)` annotations and the proof’s one are genuine ℤ→ℚ casts; set’s `: ℚ` fixes rational division. Remaining ℕ coercions bridge to ℚ/ℝ through expected types. No redundant same-type casts remain. |
| 24 | INSTANCE-NAME | n/a: no instance declarations. |

Original HAVE scan (original lines relative to 26-line saved helper):

| Line | Have | `by`? / uses | Action/result |
|---|---|---|---|
| 7 | hxR | yes; once in final rw | Removed; direct Rat.cast_div/intCast/natCast API does conversion. |
| 11 | hxdiv | yes; once in hden | Removed; terminal simpa with Rat.divInt_eq_div handles it. |
| 15 | hden | yes; once in monotonicity | Retained with shorter substantive proof, automatically consumed by gcongr. |
| 16 | h1 | no; used by rw and exact | Eliminated; directly normalize Rat.den_dvd into Int.natCast_dvd_natCast.1. |
| 19 | hdenR | yes; twice in explicit bound | Removed; gcongr discharges positivity from Rat.den_pos. |

Issues fixed: redundant cast conversion scaffolding, empty normalization tactics, explicit calc/monotonicity scaffolding, underpacked signature. Refactoring needed: none. Renames queued: none. No comments removed.

## Five-method mathlib search

[A] Lean-Finder: “rational reduced denominator of a fraction divides the original denominator”; found Rat.den_dvd, Rat.den_mk, product/difference denominator divisibility.

[B] Loogle: `Rat.den, _ ∣ _`; found Rat.den_dvd, add/sub/mul denominator lemmas and denominator-one iff divisibility.

[C] LeanSearch: “The denominator of a rational formed by dividing an integer by a natural number divides the natural number”; found Rat.den_dvd and related div/coprime lemmas.

[D] Source search: full untruncated searches in Data/Rat for denominator/division/cast API; Rat.den_dvd in Lemmas.lean:34, Rat.cast_div and cast_divInt in Cast/CharZero.lean, den_div_eq_of_coprime and denominator-one variants in Lemmas.lean. An initial glob for nonexistent Cast*.lean failed and was corrected to directory search; no absence conclusion rests on that failed query.

[E] Local name-pattern search: `Rat.den_`, 30 source hits including den_dvd, den_divInt, den_div_eq_of_coprime, denominator-one variants. Index reported **unavailable**; its positive source hits were verified, but an empty indexed absence claim is not made.

Auxiliary variants checked: den_div_eq_of_coprime, den_div_intCast_eq_one_iff, den_div_natCast_eq_one_iff, den_mk, cast_div, cast_divInt, divInt_eq_div, cast_def. Common-equivalents table: no matching discrete/finite/separation/bornology bucket. Whole-goal `exact?` did not close; `apply?` offered generic membership reformulations with remaining goals, not a proof. Whole `grind [approxSet]`, `simp [approxSet]`, and `aesop` did not establish the denominator monotonicity argument.

Conclusion: **partial match; keep local substantive approximation-membership lemma and build directly on Rat.den_dvd and existing cast/monotonicity API**. This is not a wrapper of one to three existing calls. No unproved assertion of exhaustive library absence and no forced additional API lemma.

## Generalisation status

| Parameter | Class | Actual use | Mechanical candidates / verification | Result |
|---|---|---|---|---|
| α : ℝ | structure value | Error expression and approxSet in hypothesis/conclusion | Drop cannot remove the quantified value from its dependent conclusion; implicit rebinding would yield the same universal statement. No point-localisation/typeclass parent/universe candidate for a fixed real value. | Retain. |
| κ : ℝ | structure value | Nonnegative exponent and rpow quality | Same dependent-value drop issue; ℝ→abstract field does not retain this concrete Real.rpow API and is outside necessary scope. | Retain; no ambient expansion proposed. |
| hκ : 0 ≤ κ | proposition | gcongr's exponent monotonicity condition | **Actual live drop + complete diagnostics** leaves `⊢ 0 ≤ κ` at final tactic (also expected caller mismatch); restored. Already weak, no strict→weak step. | Necessary in general: compiled α=3/2, κ=-1, h=0, q=2 counterexample. |
| h : ℤ | structure value | Rational construction and numerator | Dependent quantified value; removing binder merely auto-infers/rebinds it rather than weakening anything. Concrete integer/rational reduction is the mathematical object. | Retain. |
| q : ℕ | structure value | Original denominator and bound | Dependent quantified value; no removable assumption or universe/class parent. Natural positive denominator follows local contract. | Retain. |
| hq : (h,q) ∈ approxSet α κ | proposition | hq.1 in Nat.le_of_dvd; hq.2 supplies strict error | **Actual live drop + complete diagnostics** gives unknown hq at bound and final inequality; restored. **Actual strict→weak bound substitution** gives invalid trans_le on ≤ and caller mismatch; restored. Weak error bound cannot imply strict conclusion (already q=1 at equality). | Retain canonical bundle. |

Every live failed substitution was fully reverted; final strict TYPE equality with the genuine baseline proves the contract remained unchanged. The bundle's positivity fact is used to bound the original denominator; unbundling to an error-only assumption would require a separate zero-denominator boundary analysis and would discard the caller's existing membership API. No such restatement is recommended for this private normalization helper. No class/decidability/universe binders exist. Point-localisation is inapplicable because no global function property is assumed.

Inversion check: the proof unfolds the local approximation contract into its defining error inequality, while retaining the specific rational numerator/denominator and real-power operations. Abstracting an arbitrary monotone bound would introduce unused generality; no further abstraction warranted. Big-change candidates: none.

Literature status: n/a, private auxiliary declaration; literature search not required. No math MCP invoked/claimed.

## Line packing and inequality artifacts

Actual `#check` from final frozen profile, under `set_option format.width 100`:

```lean
@Roth.approxSet_num_den_mem_aux : ∀ {α κ : ℝ},
  0 ≤ κ → ∀ {h : ℤ} {q : ℕ}, (h, q) ∈ Roth.approxSet α κ → ((↑h / ↑q).num, (↑h / ↑q).den) ∈ Roth.approxSet α κ
```

| Signature line | Codepoints | Next complete signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 143 | 80 | `(hq : (h, q) ∈ approxSet α κ)` (29) | 80 + 1 + 29 = 110 > 100 | ok |
| 144 | 96 | none; proof body follows | n/a | ok |

All helper lines ≤100 codepoints. Original second line (35) plus next conclusion unit (60) gave 96, so repacking was implemented.

| # | Location | Original reversed inequality | Rewrite | Rename |
|---|---|---|---|---|
| — | Entire signature and every typed have | n/a: zero ≥/> occurrences | none | none; no _ge_/_gt_ |

## Every golfing rule (42 slots)

| Rule | Actual outcome |
|---|---|
| 1.1 by exact wrapper | n/a: none; exact_mod_cast is proof content, not an exact wrapper. |
| 1.2 by rfl | n/a: none; original rfl exits belonged to conversion subproofs, now eliminated by API. |
| 1.3 rw + exact | Eliminated h1's rewrite/consumer scaffolding using terminal simpa. |
| 1.4 simp + exact | Terminal simpa now transports Rat.den_dvd directly. |
| 1.5 trailing rfl | Both original push_cast/rfl conversion exits removed through cast API. |
| 1.6 constructors | Already anonymous pair construction; retain refine ⟨x.den_pos, ?_⟩. |
| 1.7 apply + exact | Replaced Nat.le_of_dvd application followed by cast proof with direct application. |
| 1.8 contradiction | n/a: no contradiction/negation tactics in helper. |
| 1.9 eta | n/a: no lambda. |
| 1.10 single-use have | h1/hxR/hxdiv eliminated by direct API; hden retained as substantive bound, implicitly used by gcongr. |
| 1.11 apply/intro | n/a: no introduction block. |
| 1.12 show | n/a: no show. |
| 1.13 have projections | n/a: original obtain already destructured hq; final uses direct projections with no extra binding. |
| 1.14 merge rewrites | One rw handles canonical rational cast plus division/integer/natural casts. |
| 1.15 terminal simp only | n/a: neither original empty simp-only call was terminal; both removed. |
| 1.16 nonterminal bare simp | n/a: no bare nonterminal simp remains. |
| 1.17 dot notation | hq.2.trans_le composes the strict bound. |
| 1.18 <\| | Direct denominator lemma chain uses <\| twice. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial existential | n/a: not existential. |
| 2.1 whole grind | Tried, fails on rational normalization/error bound; final explicit mathematical steps retained. |
| 2.2 delete before grind | n/a: no retained grind. |
| 2.3 simpa consolidation | Cast/divInt conversion subproofs consolidated into terminal simpa. |
| 2.4 fun_prop | n/a: no continuity/measurability/differentiability goal. |
| 2.5 positivity | Worked in intermediate explicit rpow bound; final gcongr discharges these conditions. Extra `<;> positivity` produced unreachable/unused tactic warnings and was removed. |
| 2.6 gcongr | Applied successfully to complete reciprocal/rpow monotonicity; complete diagnostics clean. |
| 2.7 lia / omega | Tried on denominator divisibility subgoal; lia/grind fail and omega cannot establish denominator divides q. Keep Rat.den_dvd. |
| 2.8 aesop | Tried at whole proof and after denominator bound; fails to prove membership. |
| 2.9 norm_num/norm_cast | norm_num [hx] and simp [hx] close original cast bridge; final uses explicit Rat.cast_* API instead. |
| 2.10 decide | n/a: quantified real error inequality is not finite decidable computation; no native_decide. |
| 2.11 field_simp/ring | n/a: the former identities are cast-homomorphism bridges, handled by their exact API; no field identity/ring goal remains. |
| 2.12 linear_combination | n/a: no ending ring/ring_nf or polynomial equation using hypotheses. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 calc composition | Replaced two-step calc by hq.2.trans_le. |
| 2.15 <;> | Tried with gcongr/positivity; gcongr already closes all goals, so removed unused trailing automation. |
| 3.1 erw | n/a: only rw. |
| 3.2 legacy function tactics | n/a: none. |
| 3.3 omega→lia | No arithmetic automation retained; both tried in 2.7, neither supplies rational divisibility. |
| 3.4 rcases rfl | n/a: no such substitution pattern. |
| 3.5 attributes | n/a: private single-use normalization result; global simp/grind registration would add unused API. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 resource options | n/a: none to remove; defaults verified, zero raises. |

## Step back / holistic review

The proof has three mathematical stages: reduced denominator divides and is no larger than q; the canonical rational fraction has the same real value; nonnegative-exponent monotonicity improves the allowed error. Generic whole-proof automation and exact?/apply? do not supply all three. Direct cast lemmas remove the previous conversion plumbing, and gcongr expresses the last stage clearly. A denominator-bound have remains because it names the substantive input consumed implicitly by monotonicity; inlining it into the generic tactic would obscure that fact. No duplicate skeleton or extra helper needed. `Skill(simplify)` unavailable: independent manual reuse/quality/efficiency review performed; no outstanding issue or false invocation claim.

## Proof semantics and dependency audit

Independent genuine-first-source replay compiled as `/private/tmp/roth-main-normalized-helper/IndependentNormalized.lean`, using the original proof and original binder names. Actual imported production name discovered through `privateToUserName?`: `_private.Roth.Main.0.Roth.approxSet_num_den_mem_aux`; independent actual family is `[independentNormalized]`. Each family has one member, with actual universe lists captured, not assumed universally empty.

`Semantics.lean` uses the working structural comparator for every Expr constructor, Name component, Level, BinderInfo, literal, metadata and syntax payload; it has no Expr-BEq shortcut. It compared actual current TYPE against the independent TYPE and the full genuine-baseline TYPE expression: **strict equality passed**. Actual full opaque VALUES were retrieved with `value! true`, checked for metavariables/free variables/loose bound variables/sorryAx, inferred against their types, and axiom-checked in memory. Only propext/Classical.choice/Quot.sound are allowed. Resource defaults 200000/20000/512 passed. No full VALUE identity claim between different proofs/modules; no broad private-name or macro-scope normalization.

Small receipts persist only actual TYPE/universe expressions and VALUE hash/length, not giant raw VALUES (current 184545 repr bytes; independent 179422; approxSet DATA 4861). Actual local closure is target→approxSet and independent→approxSet; no self-origin, parent theorem, other current/later Main declaration, final Roth theorem, or cross-proof dependency. approxSet's definition/source was unchanged and its accepted original DATA evidence is reused from `/private/tmp/roth-main-owner/approxSet-owner-accepted-v1.json`; actual current DATA VALUE was additionally checked in memory without copying the old giant payload. Every external used constant has a recorded actual origin index strictly below Roth.Main. Traversed the actual direct import closure: **3517 modules, 17027 direct edges**, each strictly decreasing in module index, hence acyclic. Full evidence: `semantics-receipt.json`, `semantics.stdout`, `Semantics.lean`, `profile-production-binding.json` in the helper scratch directory.

## Performance / buzz

Actual command for both captures: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 <exact-source-prefix derivative>`, with separate stdout/stderr. Owner ACKed HOLD before preparation of each phase, stayed idle through freeze/default/env/capture/drain, and explicitly RELEASED before raw parsing. Parent and Lake full environment bytes compared in memory; only hash/length and approved PATH/LEAN/toolchain fields persisted. Exact source/import/binary bindings frozen and checked. All five launches per successful phase terminal and process groups absent before release.

| Capture | Outer command | Proof async | Kernel parent | Lint parent | Disjoint total |
|---|---:|---:|---:|---:|---:|
| Genuine first ungolfed | 13.473 ms | 112.141 ms | 2.540 ms | 12.284 ms | **140.438 ms** |
| Final | 12.088 ms | 180.414 ms | 2.556 ms | 7.381 ms | **202.439 ms** |

Nested kernel times (2.492/2.505 ms) are included within kernel parents, not added again. No compiler roots, generated extra family members, or lazy prior-DATA roots for this helper. Full canonical private signature/body payload matched uniquely, including actual discovered private family. Prefix production TYPE/universes matched the actual production semantic receipt and baseline; proof/source bindings exact without Name normalization. Final is slower in this capture, still well below the 1000 ms budget; **no speedup claim**. Both below 750 ms, so no unchanged repeat/cherry-pick. FAST-BOARD; no limit raises/scaffolding/deferred slow item. Whole-file fresh all-row final profile remains the owner's later file-final responsibility.

## Actual final verification and gates

All final artifacts use the exact same restored final helper source. Temporary failed hypothesis substitutions were reverted; no proof edit followed final source capture. Gate logs preserve complete unfiltered stdout/stderr.

| Check | Actual tool-call result |
|---|---|
| Full `lake build` | exit 0, 63.763 s (`final-full-build-terminal.json`); Roth.Main rebuilt, existing warnings recorded. |
| Subsequent separate `lake build Roth.LeanEval` | exit 0, 37.319 s (`final-eval-build-terminal.json`); root excludes Eval. |
| Fresh native `lake env lean Roth/Main.lean` | exit 0, 42.860 s; four existing warnings; affected parent and all Main dependents included. |
| Fresh native `lake env lean Roth/LeanEval.lean` | exit 0, 43.809 s; no diagnostics. |
| Fresh native `lake env lean Roth.lean` | exit 0, 28.457 s; no diagnostics. |
| Complete Main LSP | success true, partial false, 0 errors, four existing outside-scope warnings. |
| Complete Eval/root LSP | each success true, partial false, no diagnostics. |
| Independent proof build | exit 0, 26.339 s. |
| Counterexample compile | exit 0, 26.028 s; κ<0 example and no-membership-input example. |
| Actual semantics run | exit 0, 134.931 s; SEMANTICS_PASS and actual TYPE/VALUE/origin/default evidence. |

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Full project build actually rebuilt Roth.Main, plus fresh native Main. |
| lake_build | pass | Actual full build exit0; separate Eval build exit0. |
| definition_protected | pass | No def/abbrev or surrounding source changed. |
| theorem_statement_protected | pass | Full strict elaborated TYPE equals genuine baseline; signature whitespace packing only. |
| structure_gate | pass | Six-line body, no cases or explicit statement conjunction. |
| naming_gate | pass | Mathematical private `_aux` name, no forbidden pattern. |
| line_packing_gate | pass | Both signature lines measured; no repack row. |
| inequality_orientation_gate | pass | Zero reversed Lean inequality occurrences; table emitted. |
| cumulative_no_unintended_breakage | pass | Parent/source unchanged; Main/Eval/root builds/native/LSP complete. |
| no-limit-raise / no-scaffolding | pass | No options, axioms, sorry, native_decide or profiling scaffolding added to project. |

New identifier verification: Rat.cast_div, Rat.cast_intCast, Rat.cast_natCast, Int.natCast_dvd_natCast and Nat.le_of_dvd are actual library APIs used successfully in complete LSP, compiled Main, independent/semantic and native gates; denominator/cast source searches recorded. gcongr is available and compiled. No unchecked guessed lemma name.

## Failed experiments / qualifications

The first baseline safe-observer attempt incorrectly used the sandbox despite the known ps restriction and failed with PermissionError **before any launch**. Failure preserved; owner explicitly released that failed phase and ACKed a fresh HOLD before the unchanged narrow escalated capture. No timing credit from failure. The first independent `-o` compile omitted `-R` for the temporary directory and failed before elaboration; corrected v2 exit0, original failure preserved. Intermediate whole-tactic/chunk probes often report errors in following old tactics because a replacement solved/changed that chunk; only subsequent complete-file diagnostics count as accepted edits. Extra positivity after gcongr produced two lint warnings and was removed. A process observation with an incorrect nonexistent numeric PID produced no rows; corrected observation used the recorded task PID and also found it already exited. No unrelated process arguments or full environments were saved.

## Result and lifecycle

Audit issues found: 4 categories; fixed: 4; refactoring deferred: 0. Rules applied materially: 1.3–1.5, 1.7, 1.10, 1.14, 1.17–1.18, 2.3, 2.6, 2.14 (other attempts/statuses above). Comments preserved: no helper comments existed; all surrounding source including parent signpost unchanged. Renames queued: none. All gates pass; no original7 completion credit.

- [✓] Step 1 references read.
- [✓] Step 2 all 24 audit items and every original have covered.
- [✓] Step 2.5 five-method search status and exact?/apply? probes.
- [✓] Step 2.6 every parameter, actual weakening diagnostics, inversion/literature scope.
- [✓] Step 2.7 full per-signature-line codepoint table and actual width100 reference.
- [✓] Step 2.8 inequality scan artifact.
- [✓] Step 3 all 42 golfing-rule slots.
- [✓] Step 4 independent holistic reflection, no unavailable-skill invocation claim.
- [✓] Step 5a complete clean helper diagnostics and affected callers.
- [✓] Step 5b actual builds/native/semantic/protection/content gates.
- [✓] Step 6a no warranted rename, shared queue untouched.
- [✓] Genuine before/final helper profile and actual-family/source/TYPE binding.
- [✓] All known launches/drivers/queries terminal, all known groups absent, explicit profile releases.

Evidence root: `/private/tmp/roth-main-normalized-helper`. `final-drain.json` records all 19 known launched jobs, including preserved failed scratch invocation, as terminal with groups absent. Report/source bindings and final END record accompany the owner handoff. No Git/publication performed.
