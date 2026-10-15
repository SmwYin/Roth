# Declaration audit: `Roth.weight_mapDomain`

Worker: fresh declaration-14 worker. Start: `8268ad8`; scope: this declaration and this report.
Original lines 130–135 (6 lines); final lines 131–134 (4 lines). The added scoped `omit`
makes the source change a net saving of one line. No other declaration or call site changed.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, as well as the transferred
Steps 1–6 prompt and the applicable Lean 4, style, and naming guidance.

## Full audit

| # | Item | Concrete result |
|---|---|---|
| 1 | LINT | Original unused section `DecidableEq σ` and unused-in-type `DecidableEq σ`, `DecidableEq τ` warnings. Removed both approved assumptions; final target has no warning. Whole-file header warning deliberately retained under the user's decision. |
| 2 | HAVE SCAN | No `have`, `let`, or local instance declarations. |
| 3 | SET_OPTION | None in target or diff; no heartbeat/recursion overrides added. |
| 4 | SIMP SQUEEZE | Original two terminal `simp` calls needed no squeezing. Final terminal `simpa [Finsupp.sum_fintype, weight] using ...` remains unsqueezed. |
| 5 | NAMING | `weight_mapDomain` names the operation on the left of the equality and preserves Mathlib's `mapDomain` identifier spelling inside a theorem name. No forbidden numeric pattern, abbreviation, single-letter public name, `_ge_`, or `_gt_`; no rename queued. |
| 6 | LINE PACKING | Removed unused instance binder and repacked to two signature lines, measured below at 100 and 68 codepoints. |
| 7 | BY PLACEMENT | `:= by` ends the conclusion line. |
| 8 | FORMAT | Two-space proof indentation, four-space signature continuation, no internal blank line; new mathematical lambda uses `↦`. |
| 9 | COMMENTS | No inline proof comments originally; none deleted. |
| 10 | DOCSTRING | Existing public statement and reference docstring byte-preserved; it explains the change-of-variables interpretation and its polynomial application. |
| 11 | VISIBILITY | Public API used in `Roth/Index.lean:233`, `Roth/Lattice.lean:160`, and `Roth/Theta.lean:386`; preserve public visibility. |
| 12 | STRUCTURE | Headline result, final proof two lines, no conjunction or branches. No extraction needed. |
| 13 | MATHLIB | Found `Finsupp.sum_mapDomain_index_inj`; use it with `sum_fintype` to convert support sums to the project's `weight`. Five-method evidence below. |
| 14 | JUNK DEF | n/a: theorem, no definition introduced. |
| 15 | EXISTS LEMMA | n/a: no existential statement or helper. |
| 16 | SHOW vs CHANGE | Neither occurs. |
| 17 | PUSH_NEG | No negation-pushing tactic. |
| 18 | GENERALISE | Approved removal of both decidability arguments verified in isolation and in the actual file. Other arguments preserved; detailed inventory below. |
| 19 | INEQUALITY | Equality conclusion and injectivity hypothesis; zero inequality occurrences, table below. |
| 20 | NORMAL-FORM | Rewrite form eliminates `weight` of `mapDomain` in favor of pulled-back parameters. The equivalent generic Mathlib form uses `Finsupp.sum`; no representation migration needed. |
| 21 | SYNTAX-GEN | Existing `hf`, `r`, `d` order supports the three external rewrite/application sites. Preserved. |
| 22 | IMPORT-FANOUT | n/a: no imports changed; generic sum lemmas already available. |
| 23 | CASTS | 0 redundant casts dropped; 1 genuine cross-type cast retained: `n : ℝ` converts the natural coefficient for real division. No other explicit ascription introduced. |
| 24 | INSTANCE-NAME | n/a: no named instance declaration. |

Issues fixed: unnecessary decidability assumptions; signature packing after removal;
manual two-case reindexing replaced with the generic Mathlib theorem; mathematical
lambda syntax normalized as part of that replacement. All four categories resolved.
Refactoring needed: none. No rename or decomposition flag.

## Mathlib search status

| Method | Query and observed result |
|---|---|
| A — Lean-Finder | `Finsupp mapDomain sum injective weighted sum`: returned `Finsupp.sum_mapDomain_index_inj` as the first result, plus `finsum_mem_image'` and `finsum_mem_range'`. |
| B — Loogle | `Finsupp.mapDomain, Finset.sum`: returned `mapDomain_finsetSum`, its alias, and `mapDomain_fintype`. These expand the mapped function; the Finder sum theorem fits the goal better. |
| C — LeanSearch | Unavailable: inherited session evidence of HTTP 500. Parent explicitly instructed bounded fallback instead of repeated failing calls; no absence claim is made from this service failure. |
| D — source | Untruncated `rg` for `sum_mapDomain`, `weight_mapDomain`, `sum_of_injective`, `mapDomain_apply_of_injective`, `mapDomain_of_notMem_range` in Mathlib Finsupp/big-operator sources and Roth found the generic APIs and all project call sites. `Basic.lean:402–420` inspected for the additive, potentially noninjective variant. |
| E — name pattern | Native `lean_local_search` for `sum_mapDomain` returned `Finsupp.sum_mapDomain_index_addMonoidHom`; index reported `unavailable`, so its incomplete output is not evidence of absence. `#check` positively verified the generated additive `sum_mapDomain_index_inj` and `sum_fintype`. |

Auxiliary variants checked: `_index_inj`, `_index`, `_index_addMonoidHom`,
`mapDomain_fintype`, `_apply_of_injective`, `_of_notMem_range`, `sum_of_injective`.
Common-equivalents table: no discrete/compact/bornological match.

Conclusion: found a generic partial match, now used directly in the proof. The target
is a theorem about the retained project definition `Roth.weight`; removing that public
API or migrating its definition is outside the authorized cleanup. No claim that the
generic mathematics is absent from Mathlib, no new wrapper/helper introduced, and no
new module documentation or imports needed.

## Generalisation status

| Parameter/hypothesis | Class | Mechanical test or dependency | Result |
|---|---|---|---|
| `σ : Type*` | type variable | Already universe-polymorphic; source of `f`, `d`, and pulled-back weight. Dropping the bound type would leave these ill-scoped. | Retain. |
| `[Fintype σ]` | typeclass | Isolated drop-test reports `failed to synthesize Fintype σ` in RHS weight and theorem application. A `Finite` replacement would require choosing a different instance in the statement. | Retain existing finite-sum API. |
| `[DecidableEq σ]` | decidability | Omitted in isolated selected proof and scoped `omit` in live file; complete diagnostics clean. | Removed, user-approved. |
| `τ : Type*` | type variable | Already independently universe-polymorphic; target of `f` and domain of `r`. Deletion ill-scopes the statement. | Retain. |
| `[Fintype τ]` | typeclass | Isolated drop-test reports `failed to synthesize Fintype τ` at LHS weight and application. | Retain. |
| `[DecidableEq τ]` | decidability | Deleted from isolated and live signatures; proof compiles without local classical invocation. | Removed, user-approved. |
| `f : σ → τ` | structure value | Used in both mapped multi-index and parameter composition. No point-localization or parent-class weakening applies to a function value. | Retain. |
| `hf : Function.Injective f` | proposition | Drop-test with selected generic theorem leaves unprovable `Function.Injective f` premise (`assumption` fails). A left-inverse hypothesis is a public restatement, not a mechanical weakening. | Preserve as explicitly directed. |
| `r : τ → ℕ` | structure value | Appears on both sides and in the coefficient denominator. Deletion leaves statement ill-scoped. No positivity hypothesis exists to weaken. | Retain. |
| `d : σ →₀ ℕ` | structure value | Appears on both sides, controls the support sum. Deletion leaves statement ill-scoped. | Retain. |

Inversion check: after unfolding `weight`, this is abstract finite-support reindexing;
Mathlib already supplies exactly that abstract theorem. Reuse it rather than adding
another abstract API. Broad coefficient/weight-target changes would alter the retained
definition and are not proposed here. The noninjective additive variant was observed,
but the user specifically directed preservation of `hf`; it is not treated as an
approved hypothesis removal or silently applied. No further generalisation work queued.

## Public literature search

Web query: `weighted sum injective reindexing Finsupp mapDomain generalization`.
Top three returned hits were Gebner's historical `data.finsupp.basic` documentation,
Mathlib3's `data.finsupp.basic` documentation, and the expdb Mathlib4 mirror. The
official current [Mathlib Finsupp documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finsupp/Basic.html)
was also returned and opened; only that primary documentation and checked local source
were used for the mathematical conclusion. They expose reindexing of arbitrary
finite-support sums, with an injective variant and an additive variant. The chosen
proof specializes the injective variant to natural coefficients divided in the reals.
ChatGPT math MCP: n/a, no such callable tool exposed in this worker's tool inventory.
No literature-driven public restatement proposed beyond the already approved removals.

## Line packing

Original signature widths: line 130 = 76, line 131 = 58, line 132 = 53.
Original first-next binder test: `76 + 1 + 27 = 104`, so that initial break was justified.
After deleting `[DecidableEq τ]`, repacking takes both `hf` and `r` onto the first line.

`#check @Roth.weight_mapDomain`, with `format.width = 100`:

```lean
@Roth.weight_mapDomain : ∀ {σ : Type u_1} [inst : Fintype σ] {τ : Type u_2} [inst_1 : Fintype τ] {f : σ → τ},
  Function.Injective f → ∀ (r : τ → ℕ) (d : σ →₀ ℕ), Roth.weight r (Finsupp.mapDomain f d) = Roth.weight (r ∘ f) d
```

The printer includes the fully qualified name and inherited binders; source widths are
measured separately and obey the source limit.

| Final signature line | Codepoints | Next indivisible binder/token | Arithmetic | Action |
|---|---:|---|---|---|
| 131 | 100 | `(d : σ →₀ ℕ)` = 12 | 100 + 1 + 12 = 113 > 100 | ok |
| 132 | 68 | none; proof body next | n/a | ok |

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | Entire signature and all hypotheses | No `≥`, `>`, `≤`, or `<` | n/a | Name contains neither `_ge_` nor `_gt_` |

## Golfing-rule pass

- [1.1] `by exact`: n/a, no redundant wrapper; selected `simpa` performs a genuine conversion.
- [1.2] `by rfl`: n/a, equality requires reindexing.
- [1.3] `rw + exact`: n/a, no such chain.
- [1.4] `simp + exact`: applied in substance via the consolidated `simpa using` generic theorem.
- [1.5] trailing `rfl`: n/a, none.
- [1.6] anonymous constructor: n/a, no conjunction or constructor.
- [1.7] `apply + exact`: n/a, no such chain.
- [1.8] `by_contra!`: n/a, no contradiction proof.
- [1.9] eta reduction: new `fun j n ↦ (n : ℝ) / r j` uses both variables and is not an eta expansion.
- [1.10] single-use `have`: n/a, none.
- [1.11] `apply + intro`: n/a; old explicit sum witnesses eliminated by the generic theorem.
- [1.12] redundant `show`: n/a, none.
- [1.13] `obtain`: n/a, no projections or existential hypotheses.
- [1.14] merge rewrites: n/a, no `rw`.
- [1.15] terminal `simp only`: n/a, no squeezed call.
- [1.16] nonterminal bare simp: n/a, both original branch calls and final `simpa` are terminal.
- [1.17] dot notation: old `.symm` was already used; new theorem is namespace-resolved because no receiver naturally shortens its application.
- [1.18] `<|`: no trailing proof parentheses remain; outer parentheses around the theorem supplied to `using` were removed after testing.
- [1.19] `push_neg`: n/a, absent.
- [1.20] trivial existential helper: n/a, none.
- [2.1] `grind`: live whole-goal attempt failed to prove the weight equality.
- [2.2] delete before grind: n/a, final proof has no grind.
- [2.3] simpa consolidation: selected and compiled; replaces manual reindexing branches using `sum_mapDomain_index_inj`.
- [2.4] `fun_prop`: n/a, no analytic function property.
- [2.5] positivity: n/a, target is a reindexing equality, not a sign claim.
- [2.6] `gcongr`: n/a, no inequality or monotonicity subgoal.
- [2.7] `lia`/`omega`: n/a, no Presburger arithmetic goal; index types arbitrary and values real sums.
- [2.8] `aesop`: live attempt failed, made no progress.
- [2.9] `norm_num`/`norm_cast`: n/a, no concrete numeral or cast-only goal; natural-to-real cast stays inside reindexed sums.
- [2.10] `decide`: n/a, equality of arbitrary real sums is not closed finite computation.
- [2.11] `field_simp; ring`: n/a, denominators are inside sums over different types; clearing them cannot establish the missing reindexing.
- [2.12] `linear_combination`: n/a, no ring-ending proof or equality hypotheses for combination.
- [2.13] `wlog`: n/a, no symmetric case split.
- [2.14] collapse calc: n/a, no calc block.
- [2.15] `<;>`: obsolete after selecting a single terminal proof with no branches.
- [3.1] `erw`: n/a, none.
- [3.2] legacy continuity: n/a, none.
- [3.3] `omega` to `lia`: n/a, neither used or needed.
- [3.4] `rcases ... rfl`: n/a, no cases.
- [3.5] automation attributes: no new attribute; public rewrite behavior retained without changing the simp set.
- [3.6] `simp_all`: n/a, no `simp_all only`; no contextual hypotheses need saturation.
- [3.7] heartbeat options: none present or added.

## Step back and live experiments

Native `lean_multi_attempt` at original line 133 tested `grind`, `simp [weight]`,
`aesop`, `exact?`, `apply?`, and a term-style `Fintype.sum_of_injective` expression.
`simp [weight]` only exposed the unequal-index sums; `exact?` found no closing term;
`apply?` suggested unhelpful real Cauchy extensionality. The term-style expression
closed the goal, with the remaining original branch lines correctly diagnosed as
`No goals to be solved`; a separate isolated example verified this candidate without
either decidability instance. It still carried the two zero/image obligations.

The selected alternative is a single `simpa` invocation using the dedicated Mathlib
finite-support reindexing theorem. It is shorter and expresses the mathematical step
directly. A standalone `example`, importing `Roth.Box` but never invoking
`Roth.weight_mapDomain`, compiled with no diagnostics and no decidability instances.
This independently checks the actual proof rather than reusing the theorem under audit.

Separate negative assumption tests intentionally failed for absent `Fintype σ`,
absent `Fintype τ`, and the absent injectivity premise of the selected generic theorem.
Those scratch failures never touched the live source; the final isolated proof was
rerun alone and returned `success=true`, `timed_out=false`, `diagnostics=[]`.

## Verification and diff gates

Actual module command:
`/Users/ramin/.elan/bin/lake build Roth.Box > /private/tmp/roth-box-d14-module.log 2>&1`.
Execution session 77723 was polled to **exit 0**, with **1154 jobs** completed.
Complete native file diagnostics: `success=true`, `partial=false`, `timed_out=false`,
no errors, no target warnings, exactly the previously preserved header warning.
Native `lean_verify` and `#print axioms` both give only
`propext`, `Classical.choice`, `Quot.sound`; source scan warnings empty.
`git diff --check` passed. Diff changes only the owned theorem and its scoped omission;
all declaration docs, mathematical expressions, other binders, name, and visibility remain intact.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module exit 0, log and session above. |
| definition_protected | pass | No definition or abbreviation changed. |
| theorem_statement_protected | pass, authorized exception | Only the two explicitly approved DecidableEq arguments removed; all mathematical hypotheses and conclusion preserved. |
| structure_gate | pass | Two-line proof, headline threshold ≤15, no conjunction or branches. |
| naming_gate | pass | Mathematical operation name, no forbidden patterns; no rename needed. |
| line_packing_gate | pass | Both final signature lines measured above, neither underpacked. |
| inequality_orientation_gate | pass | Exhaustive signature scan has zero reverse inequalities. |
| trust/isolation | pass | Standard three axioms; independent selected proof compiles without target invocation. |
| docs/comments | pass | Docstring byte-preserved; no original inline comments. |

Overall: **pass**. Parent owns the separate full-project build, `Roth.LeanEval` build,
staging, commit, and push. This worker does not claim those pending parent gates ran here.

## Result and phase checklist

Before 6 declaration lines; after 4; saved 2 declaration lines (net file saving 1 with `omit`).
Four issue categories fixed. Rules applied: 1.4, 1.18, 2.3, plus approved assumption
removal, line packing, and `↦` lambda syntax. Renames queued: none. Refactoring needed:
none. Comments preserved: none originally; public docstring unchanged.

- [✓] Step 1 — required references read.
- [✓] Step 2 — all 24 audit items recorded.
- [✓] Step 2.5 — five search methods recorded, including unavailable-service limitations.
- [✓] Step 2.6 — every parameter/hypothesis, inversion check, and public literature search recorded.
- [✓] Step 2.7 — complete final per-signature-line width table.
- [✓] Step 2.8 — complete inequality scan.
- [✓] Step 3 — all 42 golfing rules have a concrete status.
- [✓] Step 4 — whole-proof alternatives and generic-theorem strategy tested.
- [✓] Step 5a — complete live-file diagnostics clean except agreed header limitation.
- [✓] Step 5b — actual module build and every diff gate pass.
- [✓] Step 6a — no rename needed; queue unchanged.
- [✓] Step 6b — report complete; source and report ownership released to parent.

Publication verification: full `lake build` session 56521 exited 0 (2586 jobs;
`/private/tmp/roth-box-d14-full.log`); separate `lake build Roth.LeanEval` session 76596
exited 0 (2585 jobs; `/private/tmp/roth-box-d14-leaneval.log`). All affected dependents pass.
