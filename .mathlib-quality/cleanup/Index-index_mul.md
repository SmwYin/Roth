# Cleanup: `Roth.index_mul`

Single-declaration worker, starting at published 7036619 on `ramin-cleanup`. Only this theorem and this canonical report are owned here. The original source is `/private/tmp/roth-index-original.lean` at e557886. No Git, shared logs/state, caller edits, helper additions or full-project builds were performed by this worker. File-owner full build, separate LeanEval, original whole-file/type-expression checks, final independent simplify and full-file sweep remain owner gates.

## Mathematics, scope and result

After clearing positive integral weight denominators, the index is the natural weighted order of the Taylor series divided by their product. Taylor translation and the polynomial-to-power-series map preserve multiplication. Mathlib's weighted order is additive on products over a semiring without zero divisors. The two nonzero factors have finite weighted order, so `ENat.toNat_add` and the natural-number cast preserve this sum.

The approved public-type change is exactly `omit [DecidableEq σ] in`, placed before the existing byte-identical docstring. This changes the elaborated public type; it is not reported as an unchanged type. All mathematical data, nonvanishing and positivity hypotheses and the conclusion remain. Routine proof changes inline single-use `hPQ`, simplify the reusable finite-order certificate `hfin`, and normalize its lambda to `↦`. Body: 11 → 7 lines; file: 265 → 262 lines. No definition or import changes. No rename queued or applied; the existing derivative rename queue was untouched.

## References and operating contract

Read `/private/tmp/roth-index-leaf-contract.txt` fully; lean4 and mathlib-quality SKILL.md; cleanup.md, including the full 24-item fresh-worker procedure and all eleven steps; relevant cleanup-all.md worker/checklist contract; golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, style-rules.md, naming-conventions.md, mathlib-review-stages.md, profiling.md, buzz.md, and lean4/references/proof-simplification.md. Truncated combined output was supplemented by range reads. I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. No subagents were spawned.

## Complete 24-item audit

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | Baseline complete native diagnostics contained two target decidability warnings. Approved omission removes both. Final complete native diagnostics have zero target errors/warnings; other declarations' pending warnings and the preserved header warning are recorded below. |
| 2 | HAVE SCAN | Original `hPQ : P * Q ≠ 0 := mul_ne_zero hP hQ` has no `by` and one use in the bridge rewrite: inlined there. Original `hfin` has a proof and two uses (`hfin P hP`, `hfin Q hQ`): kept as a reusable local fact. Its three-line proof is replaced by terminal `simp`. Final proof has exactly this one `have`. |
| 3 | SET_OPTION | No limit, trace, diagnostic or profiling option in the target. No limit raise or shipped scaffolding. |
| 4 | SIMP SQUEEZE | The sole final `simp` is terminal inside `hfin`; left unsqueezed. No nonterminal bare simp. A first alternative `simpa using fun R hR ↦ hR` compiled but warned to use `simp`, so it was not shipped. |
| 5 | NAMING | `index_mul` states the index law for multiplication, uses snake_case and an accepted algebraic operation abbreviation. No scheme digits, forbidden abbreviation, numeric auxiliary suffix or single-letter public name. No rename needed. |
| 6 | LINE PACKING | Both signature lines measured in codepoints below; next binder would overflow line 1. The conclusion is already on the last binder line. Actual built `#check` used `format.width 100`. |
| 7 | BY PLACEMENT | Main `by` ends line 165; local `by simp` follows its explicit type on the same line. |
| 8 | FORMAT | Two-space body, four-space signature continuation, no blank body lines, semicolon chains, trailing whitespace, `haveI` or `letI`. |
| 9 | COMMENTS | Original two-line docstring byte-identical. No inline proof comments existed; zero removed or relocated. Source comparison asserts surrounding file content unchanged. |
| 10 | DOCSTRING | Existing public statement identifies product additivity and gives its source. Preserved under explicit user scope. |
| 11 | VISIBILITY | Public main result listed in the module overview and used by product induction. No private/public conversion warranted. Classic import dialect. |
| 12 | STRUCTURE | Final body seven lines, below the headline 15-line bar. No conjunction, cases or long branches. No helper/decompose flag needed. |
| 13 | MATHLIB | All five actual methods attempted below. `MvPowerSeries.weightedOrder_mul` is the abstract core and is already used directly. The project-specific rational-index bridge remains necessary for the present API. No equivalent replacement established. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: public equality, not a trivial private existential wrapper. |
| 16 | SHOW/CHANGE | n/a: no `show` or `change`. |
| 17 | PUSH_NEG | n/a: no negation-pushing tactic. |
| 18 | GENERALISE | Every outer binder classified/probed below; σ-DecidableEq omission is the only approved and applied change. Fintype parent, data drops, strict/weak and support-local positivity probes were run. |
| 19 | INEQUALITY | `hr` uses `0 < r j`; zero `≥` or `>` in signature or body; table below. |
| 20 | NORMAL-FORM | Product on the left, sum of factor indices on the right is the operational rewrite form. Natural weighted order uses mathlib's canonical law rather than a duplicate abstraction. |
| 21 | SYNTAX-GEN | Existing explicit hP/hQ/α and implicit weight function support direct `rw` applications, including `index_prod`. No easier verified public restatement found. |
| 22 | IMPORT-FANOUT | n/a: no new imports. |
| 23 | CASTS | No redundant casts introduced: `taylor α R : MvPowerSeries σ ℝ` fixes the power-series object, a load-bearing cross-type coercion. No other new ascription/coercion; 0 dropped, 1 retained as load-bearing cross-type. |
| 24 | INSTANCE-NAME | n/a: no instance declaration or named local instance. |

## Five actual search methods

| Method | Actual query/action | Result |
|---|---|---|
| A Lean-Finder | `weighted order of a product of multivariate polynomials is sum of weighted orders`, 3 results requested | Bounded direct MCP helper returned DNS failure, not a no-hits claim. `/private/tmp/roth-index-mul-lean_leanfinder.json`. |
| B Loogle | `MvPowerSeries.weightedOrder (_ * _) = _`, 3 results requested | Bounded actual request returned DNS failure; unavailable. `/private/tmp/roth-index-mul-lean_loogle.json`. |
| C LeanSearch | `weighted order product formal power series no zero divisors`, 3 results requested | Bounded actual request returned DNS failure; unavailable. `/private/tmp/roth-index-mul-lean_leansearch.json`. |
| D Source | Untruncated `rg` for `index_mul` through all Mathlib, and weightedOrder multiplication/finiteness variants through MvPowerSeries; read Order.lean 140–166 and NoZeroDivisors.lean 132–151 | Positive `MvPowerSeries.weightedOrder_mul`; `le_weightedOrder_mul`, `_eq_top_iff`, `ne_zero_iff_weightedOrder_finite`; `ENat.toNat_add` at Data/ENat/Basic.lean:240. Index-name hits elsewhere concerned subgroup indices, not this polynomial minimum. |
| E Name patterns | Native `lean_local_search "weightedOrder_mul"`, limit 10 | Positive source result `MvPowerSeries.weightedOrder_mul` in NoZeroDivisors.lean. Symbol index unavailable, so no symbol-index absence assertion. |

Auxiliary variants: `le_weightedOrder_mul`, `weightedOrder_mul_ge`, `weightedOrder_eq_top_iff`, `ne_zero_iff_weightedOrder_finite`, `toNat_add`, and polynomial/Taylor zero-coercion facts. Common-equivalents table: no discrete, compact, separation or bornology bucket applies.

The abstract multiplication law is already in mathlib over `[Semiring R] [NoZeroDivisors R]` and does not require finite variable type. The present theorem additionally connects an ℝ-valued minimum and positive reciprocal weights, so it is not simply a redundant alias of that law. The independent environment's compiled `fail_if_success exact?` plus a full fresh proof succeeds in `/private/tmp/roth-index-mul-absence.lean`; `exact?` did not close this project-index goal. This is evidence about that environment, not universal proof of absence.

Native multi-attempt at the original first proof line tried `grind`, `simp`, `aesop`, `exact?`, `apply?`. Grind failed, simp made no progress, aesop failed exhaustive search, exact? could not close; apply? gave real-number extensionality subgoals rather than an index law. This replaced the local hPQ line, so some suffix diagnostics mention unknown hPQ; those are disclosed, not treated as source validation. All attempts and results are in `/private/tmp/roth-index-mul-automation.json`.

Six replacement rules checked: no wrapper/helper added; five methods attempted with remote failures explicit; auxiliary variants inspected; no custom predicate introduced; no established replacement theorem retained as a duplicate; mathlib dependencies documented here while preserving the locked module docstring.

## Literature and generality

One web query, no requery: **“Roth theorem polynomial index product additivity generalization weights”**. First three displayed leads in order:

| Rank | Displayed lead | Treatment |
|---|---|---|
| 1 | [Min Ru, Roth’s Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf) | Opened author/university primary exposition. Page 3, lines 165–182 defines the normalized derivative minimum and states product additivity. |
| 2 | [Sajad Salami, Roth's theorem on weighted projective lines](https://arxiv.org/abs/2610.17589) | Displayed recent primary-paper lead recorded; no uninspected claim from it used. Its different weighted-projective formulation is not a basis for changing this API. |
| 3 | [Paul Vojta, Applications of Arithmetic Algebraic Geometry](https://math.berkeley.edu/~vojta/ftp/cime.pdf) | Opened author-hosted primary lecture text. Displayed §3 formulation allows positive real weights and local power-series expansions on varieties. |

The first primary source supports product additivity and positive integral weights at complex points. The third gives a broader positive-real-weight geometric index. Local project source `.mathlib-quality/references/clean.tex:530–556` explicitly distinguishes arbitrary positive real weights (direct finite-support minimum) from the positive integral weights used for the natural `weightedOrder` encoding, and uses infinity for zero. No chosen decidable equality belongs to these mathematical formulations. These broader formulations would require coordinated definitions and statements, not an inline change to the fixed `index` API; no uncompiled public proposal is applied. No ChatGPT math MCP was exposed in the tool inventory.

Inversion check: the numerical step is already mathlib's abstract weightedOrder law, valid for no-zero-divisor semirings. The remaining finite-order/cast/division bridge is specifically the rational polynomial-index API. Adding a second abstract wrapper would duplicate the existing law. No new helper or further public change is proposed.

## Every-binder mechanical generalisation

Corrected probes use `import Roth.Index`, `autoImplicit false`, and a fresh `mul_probe` declaration reproducing the original proof without calling index_mul. `/private/tmp/roth-index-mul-corrected-results.json` records every actual exit/output. Negative proof probes establish what this formulation/proof uses, not mathematical indispensability.

| Binder | Class and role | Candidates actually tested | Result |
|---|---|---|---|
| `{σ : Type*}` | Type variable, polynomial/point/weight domain; already universe-polymorphic | Drop, autoImplicit=false | Unknown σ; no Type→Type* weakening remains. |
| `[Fintype σ]` | Data-bearing finiteness used by index and products | Drop; parent `[Finite σ]` | Both fail to synthesize Fintype σ at the index signature. Choosing enumerations would change the API. |
| `[DecidableEq σ]` | Unused decidability | Drop | Exit 0 with original proof; approved omission applied and built signature confirms absence. |
| `{P : MvPolynomial σ ℝ}` | Structure value, first translated factor | Erase P from the grouped binder | Unknown P with autoImplicit=false. Coefficient-field abstraction requires changing the fixed index definition, not a class-parent substitution here. |
| `{Q : MvPolynomial σ ℝ}` | Structure value, second factor | Erase Q | Unknown Q. Same abstract-coefficient boundary. |
| `(hP : P ≠ 0)` | Proposition, finite weighted order and nonzero product | Drop | Original proof refers to unknown hP; nonzero-factor bridge unavailable. Preserved. |
| `(hQ : Q ≠ 0)` | Proposition, finite weighted order and nonzero product | Drop | Unknown hQ and unresolved index equality. Preserved. |
| `(α : σ → ℝ)` | Structure value, Taylor center | Drop | Unknown α. No continuity/monotonicity hypothesis to point-localize. |
| `{r : σ → ℕ}` | Structure value, denominator weights | Drop | Unknown r in positivity and index. Real weights need a different definition/API. |
| `(hr : ∀ j, 0 < r j)` | Proposition, all weight denominators positive | Drop; `∀ j, 0 ≤ r j`; `∀ j ∈ (taylor α (P * Q)).vars, 0 < r j` | Drop leaves unknown hr; weak and support-local versions do not match the global strict hypothesis required by the bridge. All retained unchanged. |

Bound j in hr and bound i/j in products/lambdas are local variables of those expressions, not independent theorem binders. No bundled bijectivity, topology, continuity or algebraic structure hypothesis exists to weaken. Real-field generalisation is a larger definition change, not a verified mechanical result.

First probe suite mistakenly removed the section DecidableEq from a copied prefix while leaving preceding `omit` commands. It produced prefix errors and was rejected as evidence. The corrected suite above is used instead. Its first point_hr invocation overlapped an olean replacement during module build and saw a missing Index.olean; the post-build retry produced the actual global/pointwise type mismatch and replaced that result. No failed environment probe is counted as a gate pass.

## Complete signature packing and inequalities

Original and final source signatures have the same two lines. Width includes indentation; next binder group excludes indentation.

| Signature line | Codepoints | Next syntactic group | Arithmetic | Action |
|---|---:|---|---|---|
| 164 | 92 | `(hr : ∀ j, 0 < r j)` = 19 | 92 + 1 + 19 = 112 > 100 | ok |
| 165 | 77 | no next signature line; conclusion and `:= by` already included | n/a | ok |

Actual compiled reference with `set_option format.width 100`:

```lean
@index_mul : ∀ {σ : Type u_2} [inst : Fintype σ] {P Q : MvPolynomial σ ℝ},
  P ≠ 0 → Q ≠ 0 → ∀ (α : σ → ℝ) {r : σ → ℕ}, (∀ (j : σ), 0 < r j) → index (P * Q) α r = index P α r + index Q α r
```

Lean's pretty printer itself retains the long second application segment; the source remains within 100 codepoints and packs at complete binder groups. No wide-hyp escape needed.

| # | Location | Occurrence | Rewrite | Rename |
|---|---|---|---|---|
| 1 | `hr`, line 165 | `0 < r j` | Already smaller side left | none |
| 2 | Remaining signature and body | Zero ≥ and zero > in Lean code | n/a | No _ge_/_gt_ name |

## All 42 golf rules

| Rule | Concrete status |
|---|---|
| 1.1 by-exact | n/a: no by-exact wrapper. |
| 1.2 by-rfl | n/a: not a reflexivity proof. |
| 1.3 rw/exact→rwa | Original hfin used rwa already; simplified its entire finite-order proof to terminal simp. |
| 1.4 simp/exact→simpa | Two direct `simpa using hP/hQ` certificates were compiled and profiled as an alternative; final keeps reusable hfin and terminal simp. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: no conjunction or constructor. |
| 1.7 apply/exact | n/a: no apply/exact pair; rewrites express the algebraic transport. |
| 1.8 contradiction/push | n/a: none. |
| 1.9 eta reduction | Weight lambda computes product/division, so cannot eta-reduce; arrow normalized to ↦. |
| 1.10 single-use have | Applied to hPQ; inline mul_ne_zero at its sole bridge use. hfin has proof content and two uses, retained. |
| 1.11 refine/fun | n/a: no apply/intro pair after finite-order simplification. |
| 1.12 redundant show | n/a: none. |
| 1.13 obtain | n/a: no projected existential/conjunction fact. |
| 1.14 merge rw | Existing bridge/transport rewrite chain already merged. The final rewrite follows congr and the finite-order certificate, so cannot merge across those steps. |
| 1.15 terminal simp only | n/a: final terminal simp is unsqueezed. |
| 1.16 nonterminal simp | n/a: no nonterminal simp. |
| 1.17 dot notation | Qualified weightedOrder multiplication and ENat conversion identify their subjects clearly; no useful receiver rewrite. |
| 1.18 <| | Final nested rewrite arguments need grouping; no redundant trailing parenthesized lambda/proof. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential helper | n/a: no existential helper. |
| 2.1 grind | Actual native whole-goal grind failed. |
| 2.2 pre-grind deletions | n/a: final proof contains no grind. |
| 2.3 simpa consolidation | Finite-order rewrite proof consolidated to terminal simp. Direct pair of simpa certificates tested but not retained. |
| 2.4 fun_prop | n/a: no analytic regularity goal. |
| 2.5 positivity | Compiled isolated polynomial-product nonvanishing proof by positivity, exit 0. Kept direct mul_ne_zero, which states the exact needed fact without automation. |
| 2.6 gcongr | n/a: no inequality or monotonicity goal. `congr 1` removes the common denominator. |
| 2.7 lia/omega | n/a: abstract polynomial/minimum equality, not linear Nat/Int arithmetic. |
| 2.8 aesop | Native attempt failed exhaustive search; no replacement. |
| 2.9 norm_num/norm_cast | Isolated ENat finite-sum cast goal compiled using rw[toNat_add] then norm_cast. Retained explicit Nat.cast_add for directness. |
| 2.10 decide/kernel | n/a: universal noncomputable real minimum is not finite computation. |
| 2.11 field_simp/ring | n/a: algebra alone cannot identify weighted order of a product; the named order theorem supplies the essential content. |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or applicable polynomial algebra certificate. |
| 2.13 wlog | n/a: no symmetric case branches. |
| 2.14 calc term | n/a: no calc block. |
| 2.15 common goals | n/a: no multiple identical subgoals; finite-order certificates share the local hfin. |
| 3.1 erw | n/a: no erw. |
| 3.2 analytic tactics | n/a: no continuity/measurability. |
| 3.3 omega→lia | n/a: no integer arithmetic tactic. |
| 3.4 rcases rfl | n/a: no cases or substitution. |
| 3.5 attributes | No global automation attribute added: product expansion with explicit nonzero/positivity hypotheses is deliberately rewritten at call sites. |
| 3.6 simp_all | n/a: hfin is an isolated finite-order fact; no context-wide simplification required. |
| 3.7 limits | None existed; no maxHeartbeats or recursion limit introduced. |

## Step-back and scoped simplify

Outcome: ISSUES-FOUND-AND-FIXED. The mathematical route through the existing weightedOrder product theorem is already appropriate. Kept it; eliminated the single-use nonzero-product variable and simplified the finite-order proof. A five-line alternative inlining both finite-order certificates compiled but repeated the conversion and measured worse in the actual module. The final reusable hfin exposes that shared fact once. Term-mode composition would obscure the rewrites. No shared helper is warranted for a two-use local certificate. No built-in Skill invocation tool is exposed; this is an in-thread scoped review using proof-simplification.md, not a claim that the file owner's separate final independent simplify occurred.

## Actual verification evidence

All commands ran from `/Users/ramin/LEAN/Roth` using `/Users/ramin/.elan/bin/lake`. All native/compiler processes finished before release; no request was left pending. The module build was rerun after selecting the final seven-line proof.

| Evidence | Actual result/artifact |
|---|---|
| Module build, first candidate | `lake build Roth.Index > /private/tmp/roth-index-mul-build.log 2>&1`, exit 0, 1501 jobs. |
| Module build, selected source | `lake build Roth.Index > /private/tmp/roth-index-mul-selected-build.log 2>&1`, exit 0, 1501 jobs. |
| Complete baseline native LSP | Bounded direct helper `lean_diagnostic_messages` with only file_path and timeout_s 45; `/private/tmp/roth-index-mul-lean_diagnostic_messages.json`: success true, partial false, timed_out false; includes the target's two unused-decidability warnings. |
| Complete final selected native LSP | Same unfiltered request; `/private/tmp/roth-index-mul-selected-lsp.json`: success true, partial false, timed_out false, failed_dependencies empty. 0 errors, 16 warnings, zero target diagnostics. No severity, declaration or line filters. |
| Original independent type and proof | `lake env lean /private/tmp/roth-index-mul-independent.lean`, exit 0. Imports original lower-level Mathlib dependencies plus Roth.Box/Roth.Taylor, never Roth.Index. Recreates original index formula in IndependentMul and independently establishes denominator clearing and minimum/weighted-order comparison locally, then the original product equality. Does not invoke the target, its support helper or another same-file theorem. |
| Independent generic replacement probe | `lake env lean /private/tmp/roth-index-mul-absence.lean`, exit 0. Same independent proof with `fail_if_success exact?` first; no one-step replacement found. |
| Exact original type recovered from actual built module | `/private/tmp/roth-index-mul-recovery-make.py` takes the exact original theorem header from e557886 snapshot and proves it using the actual built target, retaining the original DecidableEq section argument. Selected post-build command `lake env lean /private/tmp/roth-index-mul-recovery.lean`, exit 0; `/private/tmp/roth-index-mul-selected-recovery.log`. Recovery and actual-target axiom checks are separate commands in that file. |
| Actual signature and axioms | The selected recovery log contains width-100 `#check @Roth.index_mul`, with Fintype and no DecidableEq, and `#print axioms Roth.index_mul` = `[propext, Classical.choice, Quot.sound]`. Exact original recovery has the same standard set. |
| Independent proof axioms | `#print axioms IndependentMul.independent_mul` = `[propext, Classical.choice, Quot.sound]`, in independent and absence logs. The deliberate original DecidableEq binder causes a scratch unused-section warning; no sorry or new axiom. |
| Local tactic probes | `/private/tmp/roth-index-mul-local.lean` exit 0: positivity proves polynomial-product nonvanishing; norm_cast closes the finite ENat sum-cast identity after toNat_add. One deprecated scratch Real.Basic import warning is disclosed; it changes no project import. |
| Scope/comments/new identifiers | `/private/tmp/roth-index-mul-source-evidence.json` and `.diff` mechanically confirm source signature text, original docstring, all surrounding file bytes, and body counts. The omission is separately acknowledged as an elaborated-type change. No new external constant introduced; moved mul_ne_zero already existed. |

Native direct-helper sessions emitted an asyncio subprocess-transport cleanup warning after producing complete results. Every shell session exited 0 and the returned native result explicitly has success=true/partial=false/timed_out=false. This cleanup noise is not a Lean diagnostic or an incomplete result. The attempted process inventory using `ps` was denied by the sandbox; it is not used as proof of absence of processes. All session handles were instead polled through their tool completion.

Final complete native diagnostic inventory (all items, compact wording; full messages retained in JSON):

| Location | Severity | Diagnostic |
|---|---|---|
| 1:2 | warning | Copyright/header too short; preserved by explicit user instruction. |
| 197:1 | warning | index_C_mul unused section DecidableEq σ. |
| 214:1 | warning | index_rename unused section DecidableEq σ. |
| 225:1 | warning | index_le_card unused section DecidableEq σ. |
| 192:1 | warning | index_neg unused section DecidableEq σ. |
| 177:1 | warning | index_prod unused section DecidableEq σ. |
| 202:1 | warning | index_mul_left_weights unused section DecidableEq σ. |
| 191:1 | warning | index_neg unused DecidableEq in type. |
| 196:1 | warning | index_C_mul unused DecidableEq in type. |
| 211:1 | warning | index_rename unused DecidableEq σ and τ in type. |
| 201:1 | warning | index_mul_left_weights unused DecidableEq in type. |
| 174:1 | warning | index_prod unused DecidableEq in type. |
| 225:72 | warning | index_le_card hr unused variable. |
| 222:1 | warning | index_le_card unused DecidableEq in type. |
| 235:1 | warning | index_unique unused section DecidableEq σ. |
| 232:1 | warning | index_unique unused DecidableEq in type. |

No warning was suppressed, invented, or assigned to this target from another declaration. Those remaining declarations belong to later owner checkpoints.

New-identifier verification:

| Added-line reference | Verification | Result |
|---|---|---|
| mul_ne_zero | Already present in the original hPQ line; actual module build checks its newly inlined use | pass |
| MvPowerSeries.weightedOrder_mul | Positive native local search, source theorem and actual built #check | pass |
| ENat.toNat_add | Source theorem and actual built #check | pass |
| simp | Built-in tactic; final actual module and complete native diagnostics | pass |
| New external declaration names | None introduced | n/a |

## Anchored profiling and buzz

Actual source commands, each finished exit 0 before running `/private/tmp/roth-index-profile-parse.py LABEL`:

```text
lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean
```

Output paths `/private/tmp/roth-index-LABEL-profile-trace.log`; parser asserts all current declarations have source anchors and writes `...-profile-table.json`. Timings below are target-specific command + asynchronous elaboration/kernel totals, not aggregate profiler-category times.

| Variant | Label/artifact | Target total | Proof time | Decision |
|---|---|---:|---:|---|
| Baseline 11-line body | mul-before | 247.63 ms | 205.31 ms | Reference measurement. |
| Fully inlined five-line body, isolated preceding-API scratch | mul-alt2.log; mul-alt2-profile.json | 143.10 ms command+proof | 132.01 ms | Promising isolated measurement; required actual-module check. |
| Fully inlined five-line body, actual Index module | mul-final | 334.97 ms | 313.81 ms | Rejected: repeated direct finite-order conversions; dominant final rewrite 244.30 ms. |
| Selected reusable hfin, seven-line body | mul-selected | 308.43 ms | 274.97 ms | Under budget; measured during other verification processes. |
| Same selected source, isolated final repeat after those processes completed | mul-repeat | 209.54 ms | 184.28 ms | Final measurement; command 20.18 ms, dominant hfin step 120.05 ms. |

No strong statistical speedup claim is made from variable wall-clock samples. The final seven-line proof keeps one reusable finite-order certificate, is readable, and measures well below 750 ms and the 1000 ms budget in both actual-source samples. The five-line alternative was explicitly rejected despite its shorter source and favorable isolated timing. No further profile, limit change or decomposition is needed at this checkpoint. File-wide final independent performance sweep remains with the owner.

Buzz outcome: FAST-BOARD for this target. No pre-existing limit raise removed, zero added, no profiling scaffolding left in source, no deferred slow declaration. This is the actual CLI-backed scoped buzz workflow; no unavailable Skill/tool invocation is claimed.

## Diff gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual selected `lake build Roth.Index`, exit 0, 1501 jobs. |
| definition_protected | pass | No def/abbrev/import changes. |
| theorem_statement_protected | pass with approved type change | Source header hP/hQ/α/r/hr/conclusion is byte-identical. Scoped omission is explicitly approved, compiled, absent in actual type, and original public type recovered separately. |
| structure_gate | pass | Seven-line headline body, no conjunction/cases/branches. |
| naming_gate | pass | Descriptive index_mul, no forbidden pattern or abbreviation. |
| line_packing_gate | pass | Both signature rows and arithmetic above; 92+1+19=112. |
| inequality_orientation_gate | pass | Required table: only `0 < r j`; zero reverse inequality notation in code. |
| comments_preserved | pass | Both docstring lines byte-identical; no proof comments removed. |
| new_identifier_verification | pass | No unverified added external names. |
| no-limit-raise/no-scaffolding | pass | No options or wrappers added to source. |
| actual built signature/standard axioms | pass | Selected recovery log; original independent proof separately standard-only. |
| cumulative callers/full build/LeanEval | owner gate | Not claimed by this single-declaration worker; source released for sequential owner checks. |

Overall leaf gates: pass. No rename or decomposition action for this target; only the approved decidability removal was applied to the API. No shared log, queue, metadata or publication changes.

## All eleven checked worker steps

- [x] Step 1 — mandatory skills, contract and relevant references read, with truncated output supplemented.
- [x] Step 2 — all 24 audit items have concrete findings/actions/inapplicability above.
- [x] Step 2.5 — five actual search methods and auxiliary variants, including DNS failures and local verification.
- [x] Step 2.6 — every outer binder classified and mechanically probed; corrected suite, point/weak/parent tests, public literature top-three table and inversion check recorded.
- [x] Step 2.7 — every signature line measured with codepoint arithmetic and actual compiled width-100 reference.
- [x] Step 2.8 — per-occurrence inequality table provided.
- [x] Step 3 — all 42 golf rules resolved; actual applicable native/local trials disclosed.
- [x] Step 4 — scoped strategy/simplify review complete; shorter measured alternative rejected in favor of reusable certificate.
- [x] Step 5a — complete unfiltered native final diagnostics success, zero target warnings/errors; independent proof, built original recovery and actual axioms complete.
- [x] Step 5b — actual module build, anchored profiles and all leaf diff gates recorded.
- [x] Step 6a — no rename needed; no queue mutation or rename application.

## Freeze and hand-off

All Lean/native/compiler requests completed before SHA freeze. `Roth/Index.lean` SHA256:

```text
975ba0a5f5fc234c48bdf161c0bb178cff8c1bab7ac40d4f876dc8bcc2453e25
```

262 source lines, 19 retained declarations. Release metadata: `/private/tmp/roth-index-mul-release.json`. **SOURCE AUTHORITY RELEASED** to file owner, who acknowledged revocation. From that point this worker performed report writing only: no source read/edit, Lean request, compiler or build. Owner controls all original whole-file/type-expression checks, caller diagnostics, full build, separate LeanEval, Git and publication against this hash.


## Owner checkpoint d14

Frozen SHA256 `975ba0a5f5fc234c48bdf161c0bb178cff8c1bab7ac40d4f876dc8bcc2453e25`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session16109 exit0, `/private/tmp/roth-index-d14-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval41871 both exit0(122.00s/41.50s),
Index+Theta hashes stable; `/private/tmp/roth-index-d14-{full,leaneval}.log`.
Worker COMPLETE unfiltered native Index diagnostics success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/16other warnings; /private/tmp/roth-index-mul-selected-lsp.json. External Theta complete native LSP0errors/23inheritedwarnings/noinfos after one45second partial and complete retry, caller493 accepted; raw /private/tmp/roth-index-d14-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
