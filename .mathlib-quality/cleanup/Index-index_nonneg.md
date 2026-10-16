# Cleanup: `Roth.index_nonneg`

Single-declaration worker, `Roth/Index.lean`, starting at branch `ramin-cleanup`, owner-supplied HEAD `da34f92`. Source authority released at SHA256 `2497bbf3fc19aa862b47a5c66474cc336a2e04b745cd9f74f424c7ae05913755`; all worker Lean requests and processes had finished before release. Subsequent work is report-only. No Git operations, other declarations, shared logs, or whole-project build were performed by this worker.

## Result and scope

Applied the user-approved `omit [DecidableEq σ] in` immediately before the unchanged docstring. Replaced the three-line tactic proof with a direct application of the same nonnegative-infimum argument:

```lean
omit [DecidableEq σ] in
/-- The index is nonnegative. Source: §4, first lemma on the index ("We have `ind(P) ≥ 0`"). -/
theorem index_nonneg (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : 0 ≤ index P α r :=
  Real.sInf_nonneg (Set.forall_mem_image.mpr fun d _ ↦ weight_nonneg r d)
```

Mathematics: every value in the image defining the index is a nonnegative weight. `Real.sInf_nonneg` applies even when that image is empty, consistently with the protected real-valued definition's empty-infimum convention. `Set.forall_mem_image` supplies the image-membership transport previously performed by `rintro`. No helper, new import, definition change, attribute, rename, assumption addition, limit raise, or trust extension.

Declaration including signature: 4 → 2 lines; body: 3 → 1 lines. Adding the scoped omission yields net file change −1 line, 270 → 269. Docstring and all other source text preserved by the focused patch. Two input target warnings resolved. No deferred refactoring and no renames queued.

## References read

Read `/Users/ramin/.codex/skills/lean4/SKILL.md`, `/Users/ramin/.codex/skills/mathlib-quality/SKILL.md`, the complete `/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md` including the Phase-4 contract, and the relevant cleanup-all ownership/reporting contract. Read the full reference files `golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`, `generalisation-patterns.md`, `cleanup-gates.md`, `naming-conventions.md`, `profiling.md`, and `commands/buzz.md`. Read style-rules sections on headers, formatting, comments/docs, inequality orientation, unused variables, syntax, declaration/tactic layout, visibility, hypotheses, imports, normal forms, transparency, performance, implicit binders, show/change, local instances, generalisation, casts, and simp normal forms. Skill usage/read confirmation was sent to the file owner before editing.

## Full audit — all 24 items

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | Initial complete native diagnostics: success true, partial false, timed_out false; unusedSectionVars and unusedDecidableInType warnings for DecidableEq. Applied approved omission; final target warnings zero. |
| 2 | HAVE SCAN | No `have` in the original or final proof; no inlining candidate. |
| 3 | SET_OPTION | No scoped option or limit override in this declaration. |
| 4 | SIMP SQUEEZE | No simp call in either version. Trial simp made no progress; no squeeze required. |
| 5 | NAMING | `index_nonneg` describes the nonnegative index, uses snake_case and standard `nonneg`; no forbidden abbreviation, numeric scheme, single-letter name, `_ge_`, or `_gt_`. No rename needed. |
| 6 | LINE PACKING | One signature line, measured 91 codepoints originally, 88 finally. Required table below. Earlier preliminary prose misstated these as 100/97; measured values here supersede it. |
| 7 | BY PLACEMENT | Original `by` ended the signature line; final term proof removes `by`. |
| 8 | FORMAT | Two-space body indentation; no empty line inside declaration, trailing whitespace, semicolon chain, haveI, letI, or duplicated rewrites. Final proof is a term. |
| 9 | COMMENTS | No inline proof comments existed; none deleted. |
| 10 | DOCSTRING | Existing one-sentence public docstring with source attribution preserved byte-for-byte. Its prose `≥` is permitted. |
| 11 | VISIBILITY | Public reusable API, with external uses in Roth.Theta at 105, 388, 539. No visibility change. Owner handles external-call verification. |
| 12 | STRUCTURE | Original body 3 lines, final 1; no conjunction in conclusion, branching, long branch, or extraction need. |
| 13 | MATHLIB | All five actual search methods below found the abstract `Real.sInf_nonneg` ingredient. Reuse it with image transport; no claim of exhaustive absence. |
| 14 | JUNK DEF | n/a: target is a theorem; protected `index` definition untouched. |
| 15 | EXISTS LEMMA | n/a: no existential statement or single-use existential helper. |
| 16 | SHOW/CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every binder checked below. Only approved unused DecidableEq omitted. No proposition hypotheses to localise or weaken. |
| 19 | INEQUALITY | Single conclusion inequality `0 ≤ index P α r` already correctly oriented; table below. |
| 20 | NORMAL-FORM | Standard smaller-left nonnegativity; no equivalent-form proliferation. |
| 21 | SYNTAX-GEN | Explicit P, α, r arguments make the assertion directly applicable; no bundled hypothesis or restatement improves application. |
| 22 | IMPORT-FANOUT | n/a: no new imports. |
| 23 | CASTS | casts: 0 dropped / 0 kept as cross-type / 0 kept as load-bearing in diff; no explicit coercion added. |
| 24 | INSTANCE-NAME | n/a: no instance declaration or instance name. |

## Line packing

Actual `#check @index_nonneg`, with `set_option format.width 100 in`, against the newly built module:

```lean
@index_nonneg : ∀ {σ : Type u_2} [inst : Fintype σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ), 0 ≤ index P α r
```

Lean printed the explicit `#check` on one line even at width 100; the source signature is shorter because inherited binders are in scope. No DecidableEq argument remains.

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| Original L89 | 91 | none; body follows `:= by` | n/a, no next signature token | ok |
| Final L90 | 88 | none; body follows `:=` | n/a, no next signature token | ok |

All binders and the conclusion occupy the single signature line. The final proof-body line has 73 codepoints. No token on another signature line can be packed upward because there is no second signature line.

## Inequality scan

| # | Location | Original | Rewrite | Rename? |
|---|---|---|---|---|
| 1 | Conclusion, final L90 | `0 ≤ index P α r` | none; smaller side already left | no |
| 2 | Whole signature/hypotheses | n/a: zero `≥` or `>` in Lean code | none | no `_ge_`/`_gt_` in name |

The original/final docstring contains prose `ind(P) ≥ 0`, outside the code gate.

## Five-method mathlib search

Native Lean tools were discovered through ALL_TOOLS metadata; tool schemas were read separately from common documentation. All remote requests finished.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `The infimum of a set of nonnegative real numbers is nonnegative` | Hit `Real.sInf_nonneg`, `Real.iInf_nonneg`, `NNReal.coe_iInf`. Remote snapshot uses historical module names; local source/check verified current name. |
| B Loogle | `Real.sInf, 0 ≤ _`; `sInf, (0 : ℝ) ≤ _`; then `"sInf_nonneg"` | First two returned unknown-identifier query errors; quoted-name retry succeeded with `Real.sInf_nonneg` and current module. Errors are query failures, not absence evidence. |
| C LeanSearch | `infimum of nonnegative real set is nonnegative` | Hit `Real.sInf_nonneg`, `Real.iInf_nonneg`, `ENNReal.coe_sInf`. |
| D Source search | `sInf_nonneg`, `le_csInf`, `csInf_le` in conditionally complete lattice Basic and real Archimedean Basic; `forall_mem_image` in Set/Image | Located actual `Real.sInf_nonneg` at real Basic:258; generic bounds/image variants and Set/Image:206. Direct source inspection confirms `sInf_nonneg` uses `Real.le_sInf`. |
| E Name-pattern | native `lean_local_search` for `sInf_nonneg` | Found `Real.sInf_nonneg` at current real Basic path. Index status `unavailable`, so source fallback hit establishes presence only; empty results would not establish absence. |

Auxiliary variants examined: `Real.iInf_nonneg`, `Real.le_sInf`, `le_csInf`, `csInf_le`, image-bound variants, and the exact image predicate transport `Set.forall_mem_image`. The common-equivalents table has no direct polynomial-index bucket. Compiled `#check @Real.sInf_nonneg` and `#check @Set.forall_mem_image` succeeded in a target-independent snippet. Native `exact?` before the target was declared could not close the goal; `apply?` suggested the preceding local `le_index_iff` but left an unavailable P ≠ 0 premise, so it cannot prove the unconditional statement.

Conclusion: partial abstract match already used; retain the public polynomial-index API within the owner's explicit retained-declaration scope and compose existing mathlib API directly in its proof. No new wrapper/helper introduced and no assertion that a generic theorem is absent. Deleting this public declaration or rewriting external callers is not applied by this single-declaration worker.

## Generalisation — every binder

Tests used native `lean_run_code` with `autoImplicit false` for negative drop probes. Expected failing probes were isolated from source and do not count as verification failures of the final source.

| # | Binder | Class | Use | Mechanical candidates actually tested | Result |
|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type-variable/universe | Variable type in polynomial, point, weights | Remove σ binder with autoImplicit false | Unknown identifier σ in each dependent type. Retain. Already universe-polymorphic; no `Type` restriction to weaken. |
| 2 | `[Fintype σ]` | typeclass | Required by protected `index`/`weight` | Drop; replace with `[Finite σ]` in fresh namespaces with no Fintype in scope | Both fail synthesising Fintype σ in conclusion. Retain. |
| 3 | `[DecidableEq σ]` | decidability | Unused section inclusion | Compile direct term without instance; exact original proof also compiled without it in independentIndex probe | Success; apply only user-approved scoped omission. |
| 4 | `(P : MvPolynomial σ ℝ)` | structure value | Subject polynomial of index | Remove P binder with autoImplicit false | Unknown identifier P. Retain dependent data argument. |
| 5 | `(α : σ → ℝ)` | structure value | Evaluation/Taylor point | Remove α binder with autoImplicit false | Unknown identifier α. Retain dependent data argument. |
| 6 | `(r : σ → ℕ)` | structure value | Weight function | Remove r binder with autoImplicit false | Unknown identifier r. Retain dependent data argument. |

An initial attempt to test Fintype removal using `omit` inside a context that still contained a Fintype local was inconclusive: elaboration could still use that local for the definition's implicit argument. Discarded that result and reran both drop and Finite probes in truly fresh namespaces, obtaining the failures above. No untested weakening is labelled verified. Point-localisation, strict→weak, and bundled-condition decomposition do not apply: there are no proposition hypotheses of those forms.

Inversion check: the generic content after unfolding the index is already exactly `Real.sInf_nonneg`, which accepts any set of nonnegative reals. Its existing generic API is reused. Abstracting coefficient types or real weights would require changing the protected `index`/`weight` definitions and the theorem family; no such structural/public restatement is proposed or applied here. Literature confirms positive real weights are a broader mathematical setting, but that is a definition-level extension outside this approved local omission. Big-change candidate requiring an owner proposal: none recommended for this declaration alone.

## Public literature search

Actual WebSearch queries:

1. `polynomial index Roth theorem nonnegative weighted order generalization`.
2. `infimum nonnegative set real numbers empty infimum zero Lean`.

The initial batched search merged results. For an auditable per-query top-three record, reran the two searches independently while writing this report (after source freeze, without any Lean request or source edit):

| Query | First three displayed hits | Relevance |
|---|---|---|
| 1 | [Vojta, Applications of Arithmetic Algebraic Geometry](https://math.berkeley.edu/~vojta/ftp/cime.pdf); [Min Ru, Roth’s Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf); [Weighted Ehrhart theory](https://www.sciencedirect.com/science/article/pii/S0001870824001427) | First two discuss index/order; third concerns a different invariant and gives no applicable weakening. Search rankings varied between repeated requests; this records the final separately displayed result. |
| 2 | [Wikipedia, Empty set](https://en.wikipedia.org/wiki/Empty_set); [PSU, The Real Numbers chapter](https://personal.science.psu.edu/rcv4/INTAN.pdf); [TCD, Some basic concepts](https://www.maths.tcd.ie/~pete/maths121/ch1.pdf) | Elementary infimum conventions distinguish nonempty bounded sets from empty sets; none justifies changing Lean's totalised real sInf. Only primary mathematical texts and local formal API were relied on for mathematical conclusions. |

Read primary [Min Ru, Roth’s Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf), definition across pp. 2–3: index is a minimum of sums of nonnegative multi-indices divided by positive integer weights. Read primary [Jiří Lebl, Basic Analysis, the real numbers](https://www.jirka.org/ra/html/sec_setofreals.html), treating greatest lower bounds and extended-real empty-set conventions. Read project `.mathlib-quality/references/clean.tex` §4, lines 530–569: the mathematical setup allows positive real weights, nonzero P, and assigns infinity at zero; the first lemma follows from every weight being nonnegative. The protected project implementation is ℝ-valued and already proves nonnegativity for all natural weights, including zero denominators under total division, and all P. Those convention differences were preserved, not silently redefined.

ChatGPT math MCP: n/a, no matching capability in discovered tools. No external message was sent. Literature yields no extra assumption to drop beyond the verified DecidableEq omission.

## All 42 golfing rules

Native `lean_multi_attempt` tested whole-goal `grind`, `simp`, `aesop`, `positivity`, `exact?`, `apply?`, and two explicit nonnegative-infimum compositions. Its replacement point was the first tactic line, so successful closers also reported `No goals to be solved` on retained original following tactics. That is a tool replacement-range artifact; the final whole term was separately compiled by `lean_run_code` and the actual module build. No failed multi-attempt result is presented as a source-build success.

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: original has a substantive three-step proof, no by-exact wrapper. Term conversion applied after composition verification. |
| 1.2 by rfl | n/a: none. |
| 1.3 rw + exact | n/a: no rw. |
| 1.4 simp + exact | n/a: no simp chain. |
| 1.5 trailing rfl after simp | n/a: none. |
| 1.6 constructor pairs | n/a: no conjunction/constructor. |
| 1.7 apply + exact | Applied equivalent composition: nonnegative-infimum refinement and image-membership introduction become direct Real.sInf_nonneg term. |
| 1.8 by_contra + push_neg | n/a: no contradiction proof. |
| 1.9 eta-reduce | n/a: final lambda ignores membership but genuinely specialises d; not `fun x ↦ f x`. |
| 1.10 inline have | n/a: no have. |
| 1.11 apply + intro | Applied via `Set.forall_mem_image.mpr fun d _ ↦ ...`; removes explicit refinement/rintro. |
| 1.12 redundant show | n/a: none. |
| 1.13 have + projections | n/a: none. |
| 1.14 merge rw | n/a: none. |
| 1.15 terminal simp only | n/a: none. |
| 1.16 nonterminal bare simp | n/a: none. |
| 1.17 dot notation | n/a: Real.sInf_nonneg has no subject receiver; existing `mpr` is already dot notation. |
| 1.18 avoid parens | Parentheses are needed around the argument to sInf_nonneg; `<|` spelling gives no clarity or brevity gain. Direct term retained. |
| 1.19 push_neg migration | n/a: none. |
| 1.20 trivial existential helper | n/a: no helper. |
| 2.1 grind | Actually tried: failed on opaque index nonnegativity. |
| 2.2 delete before grind | n/a: no grind in original/final proof. |
| 2.3 simpa consolidation | n/a: no simp-followed-by-closing-tactic chain. |
| 2.4 fun_prop | n/a: no analytic function-property goal. |
| 2.5 positivity | Actually tried: failed to prove positivity/nonnegativity/nonzeroness of opaque index. |
| 2.6 gcongr | n/a: no comparison of monotone compound expressions or calc. |
| 2.7 lia / omega | n/a: goal is real sInf, not Nat/Int arithmetic. |
| 2.8 aesop | Actually tried: failed, made no progress. |
| 2.9 norm_num / norm_cast | n/a: no concrete numeric computation/cast goal. |
| 2.10 decide / decide +kernel | n/a: arbitrary real inequality is not finite decidable computation. |
| 2.11 field_simp; ring | n/a: no algebraic identity or denominator manipulation. |
| 2.12 linear_combination | n/a: no ring/ring_nf endpoint or algebraic hypotheses. |
| 2.13 wlog | n/a: no symmetric case branches. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 close multiple goals | n/a: no repeated parallel subgoals. |
| 3.1 erw → rw | n/a: neither. |
| 3.2 analytic tactics → fun_prop | n/a: none. |
| 3.3 omega → lia | n/a: neither arithmetic tactic present. |
| 3.4 rcases with rfl | Original rintro rfl already substituted; term proof removes the membership case entirely. |
| 3.5 register automation | Considered; no new global simp/grind attribute required or applied. Existing public API is kept plain. |
| 3.6 simp_all | n/a: no simp_all. |
| 3.7 remove heartbeat options | n/a: none existed; none added. |

Step-back reflection: bare automation does not see through the domain definition, whereas a direct mathlib term states exactly the mathematical reason. `exact?` did not find a closing theorem and `apply?` introduced unnecessary nonvanishing premises. The image-transport term is shorter and leaves no auxiliary API. No unused intermediate fact or alternative strategy remains.

## Verification and trust

* Actual command `lake build Roth.Index` completed exit 0, target reported `Built Roth.Index (16s)`, 1501 jobs. Replayed dependencies and other declarations emit existing warnings, including the explicitly preserved short copyright header and other unused DecidableEq arguments. Target emits none. This is not a whole-project build claim.
* Final native full-file `lean_diagnostic_messages`, timeout_s 45: success true, partial false, timed_out false, failed_dependencies empty; 25 unrelated existing warnings, zero items at target L88–91. A separate target-range complete request likewise returned no items.
* Independent original proof: native `lean_run_code` imported only Roth.Box, Roth.Taylor and real Archimedean Basic; it recreated the protected index definition and proved `Roth.index_nonneg_original_independent` with the original three tactics and original public DecidableEq binder. No import of Roth.Index, target theorem, private Index helper, or same-file theorem was used. success true, timed_out false. Expected unused-DecidableEq warnings remain on that deliberately original scratch signature.
* A separate independentIndex snippet compiled both original argument without DecidableEq and the candidate term. success true, timed_out false. `#check` verified Real.sInf_nonneg and Set.forall_mem_image.
* Exact original public type was extracted from `/private/tmp/roth-index-original.lean` to `/private/tmp/roth-index-nonneg-compatibility.lean`, with original section Fintype and DecidableEq. After the actual module build, `lake env lean /private/tmp/roth-index-nonneg-compatibility.lean` completed exit 0, recovering that original type by applying the actual built theorem. Its deliberate unused-DecidableEq warning is not a source regression.
* `#print axioms` on actual `Roth.index_nonneg`, original-type recovery, original independent proof, and independently checked candidate all reported only `[propext, Classical.choice, Quot.sound]`.

Actual original independent signature, printed at width 100:

```lean
@index_nonneg_original_independent : ∀ {σ : Type u_2} [inst : Fintype σ] [DecidableEq σ] (P : MvPolynomial σ ℝ)
  (α : σ → ℝ) (r : σ → ℕ), 0 ≤ index P α r
```

## Gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.Index`, exit 0, target 16s. |
| definition_protected | pass | No def/abbrev edit; protected index body and arguments unchanged. |
| theorem_statement_protected | pass with approved omission | Same P/α/r, conclusion, universe, name, order, visibility; only user-approved section DecidableEq omitted. Original type recovered from actual built theorem. |
| structure_gate | pass | One-line body; no conjunction or long branch. |
| naming_gate | pass | Descriptive snake_case, no forbidden pattern/abbreviation; no rename. |
| line_packing_gate | pass | Complete measured one-line table above; no repack row. |
| inequality_orientation_gate | pass | Complete occurrence scan; zero ≥/> in code. |
| no-limit-raise / no-scaffolding | pass | No options, profiler wrappers, sorry, native_decide, axiom, or debug commands added to source. |
| external call sites / full project | owner gate | Owner separately checks Theta and whole project after source release; worker makes no success claim for those. |

Overall worker gates: pass. Header metadata was explicitly preserved by user instruction; no invented authors or linter suppression.

## Simplify pass

Outcome: PASS-THROUGH after the term composition. No builtin Skill/simplify callable exists in this session; performed the equivalent scoped holistic review manually and disclosed the limitation. Checked reuse, duplication, proof structure, applicability, and efficiency. Existing generic mathlib API supplies all necessary structure, no helper or import duplication introduced, no further issue found. No additional source changes.

## Buzz pass — target budget 1000ms

Performed the profiling workflow directly; there is no callable Skill hand-off tool. Used actual CLI source-anchored traces, not aggregate cumulative timing as per-declaration evidence. Native per-declaration profiler was not needed.

Both commands completed exit 0 before their accepted parses:

```text
lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean > /private/tmp/roth-index-nonneg-before-profile-trace.log
lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean > /private/tmp/roth-index-nonneg-after-profile-trace.log
```

Parsed with `/private/tmp/roth-index-profile-parse.py nonneg-before` and `nonneg-after` after completion. An earlier premature parse of the running before-log failed its completeness assertion; discarded it and reran after exit 0. No timing is taken from that incomplete parse.

| Declaration | Anchor | Before command/proof/total | Final command/proof/total | Budget |
|---|---|---|---|---|
| Roth.index_nonneg | L89 → L90 | 7.75 / 5.98 / 18.34ms | 1.92 / 1.93 / 4.37ms | below 1000ms |

Outcome: FAST-BOARD. Original and final already far below 750ms borderline threshold. No slow-declaration diagnosis/fix, no performance deferral, no propagation target in this single-declaration scope. Timings vary with machine/cache; the measured reduction is reported without attributing all of it to proof compression. maxHeartbeats raises removed 0; added 0. Scaffolding added to source 0. No inference about whole-project speed.

## Required eleven-step checklist

- [x] Step 1: reference docs read.
- [x] Step 2: all 24 audit items reported.
- [x] Step 2.5: all five actual mathlib search methods and failure disclosures.
- [x] Step 2.6: every binder mechanical drop/generalisation status and public literature search.
- [x] Step 2.7: every signature line measured, width arithmetic/n-a boundary explicit, actual width-100 #check.
- [x] Step 2.8: inequality occurrence scan table.
- [x] Step 3: all 42 golf rules have concrete status.
- [x] Step 4: step-back reflection and alternative automation evaluated.
- [x] Step 5a: complete native diagnostics; target warning-clean.
- [x] Step 5b: actual module build, protection/content gates, independent original proof, original-type recovery, actual axiom checks.
- [x] Step 6a: no rename needed, no queue mutation.

Renames queued: none. Comments preserved: none present in proof; existing public docstring unchanged. Refactoring needed: none. Source frozen and authority returned before owner compatibility/full verification.


## Owner checkpoint d08

Frozen SHA256 `2497bbf3fc19aa862b47a5c66474cc336a2e04b745cd9f74f424c7ae05913755`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session55139 exit0, `/private/tmp/roth-index-d08-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval87007 both exit0(153.09s/35.49s),
Index+Theta hashes stable; `/private/tmp/roth-index-d08-{full,leaneval}.log`.
Worker complete Index LSP success=true partial=false timed_out=false, 0target diagnostics/25unrelated warnings. External Theta complete native LSP after one45second partial timeout and immediate complete retry: success=true partial=false timed_out=false, 0errors/23inherited warnings, noinfos/no faileddependencies. All3 index_nonneg callers accepted; raw /private/tmp/roth-index-d08-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
