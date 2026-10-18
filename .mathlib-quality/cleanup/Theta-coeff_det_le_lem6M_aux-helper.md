# Dedicated new-helper audit: `coeff_det_le_lem6M_aux`

Scope: only the new private coefficient helper and its necessary routine use in public `index_det_le`. This is a fresh dedicated helper audit; it adds **zero original-declaration counts**. No Git operations, shared reports, or rename queue writes. No new private or public declarations were introduced.

## Outcome and mathematical reason

**Deleted the helper.** Its only use now calls existing `Roth.abs_coeff_det_hasseDeriv_le` directly at the uniform degree bound `r := fun _ ↦ r₁`. The hypothesis `degreeOf j R ≤ r j` composes with `r j ≤ r₁`; the constant product and sum reduce by `Finset.prod_const`, `Finset.sum_const`, `Fintype.card_option`, `pow_mul`, and `mul_right_comm`. This eliminates the former manual product, sum, and power monotonicity argument rather than merely repackaging it.

The public theorem's type, ordinary argument names/order, BinderInfo, conclusions, and all three Step comments are preserved. Its proof now has **21 nonblank noncomment physical lines, 24 including all three comments**, versus 16/19 before. The public result is an ordinary theorem absent from the module Main results list, so its cap is **30**, not 15. The coefficient local proof occupies seven physical lines including its type. No branch exceeds ten lines. The whole source shrinks **963 → 943 lines (−20)**.

## References and inherited baseline

Read both skills (`lean4/SKILL.md`, `mathlib-quality/SKILL.md`), the full cleanup workflow, full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, profiling, naming, and the relevant style sections. The current standing instruction to implement recommended changes supersedes older approval text. The parent also explicitly endorsed deletion after the independent uniform-route candidate compiled.

The inherited baseline source SHA is `f9ff4b423b085a156e8706bd40b8a8588826394c065e812cea5b800e2313684d`. Its complete unfiltered native LSP result is `/private/tmp/roth-theta-index-det/final-lsp.json`: success true, partial false, timed_out false, failed dependencies [], zero errors, eleven warnings. This is **inherited**, not a fresh run of this leaf. The inherited actual module build was green. The owner’s whole-project baseline 110.300 s / separate LeanEval 32.749 s belonged to older `ac43` source; neither is represented as a final gate for this batch.

Inherited uncontended real global trace, threshold zero, exact prefix through public original row 28: `/private/tmp/roth-theta-index-det/final-profile.log`, `final-profile-manifest.json`, `final-timings.json`: coefficient helper **373.647 ms**, sibling **733.357 ms**, public **430.371 ms**. These are explicitly inherited timings. Older superseded `46e49` trace measured coefficient helper 787.562 ms (generic terminal sum simpa 386.354 ms); the inherited final explicit sum simpa cost 21.7 ms. This is a real documented performance exception, not a reason to blindly unsqueeze old code. The old sum proof is now removed entirely.

The exact initial independent 18-line helper comes from `/private/tmp/roth-theta-index-det/coeff_det_le_lem6M_aux-FIRST.lean`, SHA `975db962d42a209a6d28afb22593651b0ced9ac12b39ed27acc5854d660b6335`. Its complete first-introduction snapshot is SHA `42d60acc1b1b3d587ffe568e246cb9ba637ee0a6449a6a2b29d6f02249354ba4`; associated manifest retained. The initial helper already omitted `[DecidableEq τ]`; twelve effective binders remain in its full type.

## Full 24-item audit

| # | Check | Finding / action |
|---|---|---|
| 1 | Lint | No warnings in the assigned helper's baseline range. Module has eleven inherited warnings elsewhere; protected hB/hr and other public hypotheses are not reopened. Final unfiltered result is below. |
| 2 | Every `have` | `hB0`: no `by`, used twice (bound and nonnegativity), formerly keep; `hprod`: proof-bearing, used once; `hsum`: proof-bearing, used once. All three are eliminated by uniform specialization. In caller `hFcoef` is proof-bearing and used twice, so retained locally. |
| 3 | Options | No production options, heartbeat changes, depth changes, or tracing scaffolding. Scratch negative automation uses a lower 10000 heartbeat bound, never a raised limit. |
| 4 | Simp | Old terminal hsum `simpa only` had measured performance justification. Deleted with the old proof; new terminal `simpa [...] using` is broad and compiled. Sibling terminal explicit simpa is untouched. |
| 5 | Naming | `coeff_det_le_lem6M_aux` has descriptive subject/order and permitted `_aux`, no numbered `_aux`, forbidden abbreviation, scheme prefix, or `_ge_`/`_gt_`. Deletion resolves naming entirely; no queued rename. |
| 6 | Packing | Every baseline signature line measured below; helper disappears. Caller public signature byte-identical; seven-line local proof fits 100 columns. |
| 7 | `by` | New local `by` sits at the end of its type line. |
| 8 | Format | Two-space proof indentation, four-space signature continuation, no blank proof lines, no `haveI`/`letI`, no merged distinct tactics. |
| 9 | Comments | Helper had none. All three public Step comments remain in place above the same mathematical stages. No docstrings were edited. |
| 10 | Docstrings | Private helper had none; deletion needs none. Public docstring remains byte-identical. |
| 11 | Visibility | Single-use private helper deleted, not promoted. |
| 12 | Structure | 18-line helper removed; ordinary public proof 21 code / 24 including comments ≤30. Every local branch ≤10; no conjunction/witness splitting needed. |
| 13 | Mathlib | All five actual search methods below; existing project determinant coefficient API directly specializes. No new wrapper retained. |
| 14 | Junk definition | n/a: theorem, no definition under audit. |
| 15 | Existential helper | n/a: statement is an inequality, not an existential. |
| 16 | Show/change | No `show` or `change` in assigned proof or new local replacement. |
| 17 | Deprecated negation | No `push_neg`. |
| 18 | Generalisation | Every effective binder received a compiled drop probe; successful uniform degree restatement compiled separately. Helper deleted rather than publishing optional new API. |
| 19 | Inequalities | Every bound is oriented `≤`; no `≥` or `>` in helper signature, hypotheses, or replacement. Table below. |
| 20 | Normal form | Coefficient absolute-value inequality against existing `lem6M` stays canonical for this file. No competing equivalence API. |
| 21 | Syntactic generality | General determinant API already accepts arbitrary derivative matrix and degree function. Uniform specialization composes the two pointwise degree bounds directly. |
| 22 | Import fanout | n/a: no imports added or removed. |
| 23 | Casts | New `ℤ → ℝ` cast on `R.coeff 0` is a genuine coefficient-domain bridge. Matrix entry `(ν : ℕ)` is required because ν : Fin l. Inner `(… : ℤ)` fixes the coefficient type; casts were not removed by speculative API churn. |
| 24 | Instance names | No instance declaration or explicitly named instance introduced. Effective Fintype is anonymous. |

## Five actual search methods and replacement lookup

Raw API responses: `/private/tmp/roth-theta-coeff-helper/search-results.json`; untruncated source results: `grep-search.log` in the same directory.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | “absolute value coefficient determinant multivariate polynomial Hasse derivative bound” | Returned Chevalley complexity bounds, unrelated to the needed inequality. |
| B Loogle | `MvPolynomial.coeff, Matrix.det, LE.le`; corrected `"det", "coeff"` | First query rejected the indexed identifier; corrected query returned polynomial determinant coefficient identities, not the needed bound. Error retained honestly. |
| C LeanSearch | “absolute value coefficient determinant Hasse derivatives bounded degrees” | Found `Matrix.det_le`, `Matrix.det_sum_smul_le`, and an unrelated polynomial boundedness result. The absolute-value matrix bound is a building block, not the desired coefficient theorem. |
| D Source rg | Full names `abs_coeff_det_le_lem6M_aux`, `abs_coeff.*det`, `coeff_det`, `norm.*det`, `det_le`, in mathlib matrix absolute-value and MvPolynomial sources plus project CoeffNorm | Found `Matrix.det_le` plus project `normOne_det_le` and `abs_coeff_det_hasseDeriv_le`. All full-name results preserved without truncation. |
| E Local name pattern | `abs_coeff_det` | Found `Roth.abs_coeff_det_hasseDeriv_le` at CoeffNorm:252. Index was unavailable: source search established this hit; empty results would not prove absence. |

Auxiliary route lookup: the project's general theorem already combines `abs_coeff_le_normOne`, `normOne_det_le`, `normOne_hasseDeriv_le`, the support box bound and ring normalization. Standard `_le` / `normOne_*` / `det_le` variants were inspected in CoeffNorm and mathlib's AbsoluteValue file. Common-equivalents table: no topology/finiteness/bornology disguise applies; finite constant sums/products are the relevant generic route.

Conclusion: **existing general project API supplies the whole substantive bound; specialize it directly and delete the one-use local wrapper**. This is presence evidence and a compiled replacement, not an unsupported claim that all of mathlib lacks some theorem. Anonymous `exact?` / `apply?` probes were also run against a clean exact prefix before this helper, without named failed declarations or the audited declaration in scope.

## Generalisation and every effective binder

`binder-negative.lean`, `binder-map.json`, and `binder-negative.log` contain independent `autoImplicit false` removal probes for all twelve effective binders. These are honest drop tests of the full old type/direct proof; failure establishes that the edited proof/type did not survive, not mathematical necessity. The successful `uniform.lean` restatement demonstrates the useful abstraction: keep only `degreeOf j R ≤ r₁`, removing `r` and `hr₁` together after composing them. No new production API is needed to expose this restatement.

| Binder | Role / use | Compiled drop result | Weaker-form decision |
|---|---|---|---|
| `{τ : Type*}` | Variable index domain; already universe-polymorphic | Unknown τ in dependent type | Already Type*, no universe restriction to weaken. |
| `[Fintype τ]` | Fintype.card, finite products/sums in existing theorem | Fintype synthesis fails | `[Finite τ]` alone cannot supply the exact Fintype.card statement without choosing structure; no new API for deleted helper. |
| `{r : Option τ → ℕ}` | Intermediate degree function | Unknown r in hr₁/hRd | Eliminated together with hr₁ by compiled uniform restatement. |
| `{r₁ : ℕ}` | Uniform bound and lem6M parameter | Unknown r₁ in dependent bounds | Natural exponent/degree parameter, not an unnecessary hypothesis. |
| `hr₁` | Pointwise non-strict degree comparison | Unknown hr₁ in composed bound | Already weak `≤`; conjunction with hRd composes to uniform hRd in successful positive probe. |
| `{B : ℝ}` | Coefficient bound / lem6M parameter | Unknown B in hRc/conclusion | Fixed ℝ is the existing numerical API's codomain; abstract field restatement would be new API and is unnecessary. |
| `{R : MvPolynomial (Option τ) ℤ}` | Polynomial and all coefficient/degree expressions | Unknown R | Structural data, removed only by replacing theorem's content. |
| `hRd` | Degree comparison | Unknown hRd in direct application | Already non-strict; successful uniform weakening/composition described above. |
| `hRc` | Coefficient comparison and inferred 0 ≤ B | Unknown hRc in direct application | Already weak; no extra B positivity assumption needed. |
| `{l : ℕ}` | Matrix size, factorial, exponents | Unknown l in matrix type | Structural, no positivity assumption; l=0 remains supported. |
| `E` | Arbitrary derivative indices | Unknown E in determinant | Already arbitrary matrix; no structural derivative restriction needed. |
| `d` | Arbitrary coefficient index | Unknown d in conclusion | Already arbitrary; cannot drop data while preserving conclusion. |

`[DecidableEq τ]` is **not** an effective original helper binder: the immutable first introduction had `omit [DecidableEq τ] in`. Both old independent proof and direct replacement compile with only Fintype, and printed full telescopes confirm this.

Literature: **n/a: private declaration; public literature search exempt by cleanup scope**. The necessary public caller edit changes no type or literature-level statement. Inversion check performed: after invoking the general determinant coefficient bound, the old proof only compares generic products/sums/powers. The more general result already exists as `abs_coeff_det_hasseDeriv_le` for arbitrary finite σ, so use that directly. No abstract new helper, public promotion, or third helper was introduced.

## Measured signature packing and inequality artifact

Baseline packed signature at source lines 405–409 (before deletion). The first introduction had a separate short `(d) :` line; the inherited baseline already combined it with the left side. Deleting the helper is the final packing action. No surviving helper signature is exempted or left underpacked.

| Baseline sig line | Codepoints | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 405 | 94 | `{R : MvPolynomial (Option τ) ℤ}` (31) | 94+1+31=126 >100 | ok; deleted |
| 406 | 67 | `(hRc : ∀ d, … ≤ B)` (40) | 67+1+40=108 >100 | ok; deleted |
| 407 | 90 | `(d : Option τ →₀ ℕ)` (19) | 90+1+19=110 >100 | ok; deleted |
| 408 | 96 | `lem6M (Fintype.card τ + 1) r₁ B l := by` (39) | 96+1+39=136 >100 | ok; deleted |
| 409 | 45 | proof body next | n/a | ok; deleted |

The full old type is printed in `independent-helper-final.log`; it matches original/replacement with all effective binders. Final public signature is unchanged, so this leaf introduces no public signature packing changes. All added source lines are ≤100 codepoints; the longest is measured in the final manifest.

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | All original helper signature and hypotheses | no `≥`/`>` occurrences | none | none |
| 2 | New local hFcoef and its degree-bound application | no `≥`/`>` occurrences | none | none |

## All 42 golfing rules

| Rule | Status and substantive reason |
|---|---|
| 1.1 by exact | n/a: no such wrapper in assigned proof. |
| 1.2 by rfl | n/a: no such wrapper. |
| 1.3 rw+exact | n/a: old rw is followed by a substantive inequality proof; whole proof replaced instead. |
| 1.4 simp+exact | Applied: direct bound normalized by terminal `simpa […] using`. |
| 1.5 trailing rfl | n/a: absent. |
| 1.6 constructor | n/a: no conjunction constructor proof. |
| 1.7 apply+exact | Applied at strategy level: direct existing theorem application removes transitivity bridge. |
| 1.8 by_contra | n/a: absent. |
| 1.9 eta lambdas | New `fun j ↦ (hR.2.1 j).trans (hr₁ j)` performs composition, not eta-only. Uniform `fun _ ↦ r₁` is necessary. |
| 1.10 single-use have | Eliminated hprod/hsum and formerly repeated bound scaffolding; caller hFcoef used twice remains. |
| 1.11 apply+intro | n/a: no such chain. |
| 1.12 redundant show | n/a: none. |
| 1.13 projection destructure | n/a: no intermediate projection-only have. hR projections feed APIs directly. |
| 1.14 consecutive rw | n/a: none in final replacement. |
| 1.15 terminal simp | New terminal simpa remains unsqueezed. Old measured exception documented; removed with old argument. |
| 1.16 nonterminal simp | n/a: new simp is terminal. |
| 1.17 dot notation | Used `(hR.2.1 j).trans (hr₁ j)` and `(abs_nonneg …).trans …`. |
| 1.18 trailing parentheses | New simpa-using theorem application needs no superfluous closing wrapper; ordinary dependent arguments kept grouped for readability. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential inline | n/a: no existential helper. |
| 2.1 grind whole proof | Actual bounded anonymous clean-prefix trial, failed; deterministic direct specialization selected. |
| 2.2 before grind | n/a: production proof has no grind. |
| 2.3 simpa consolidation | Applied: constant-product/sum/card/power normalization in one terminal simpa. |
| 2.4 fun_prop | n/a: no analytic function-property goal. |
| 2.5 positivity | Old structural side conditions disappear. B≥0 derives from hRc at coefficient zero, not from structural positivity alone; direct transitivity supplies it. |
| 2.6 gcongr | Manual monotonicity goal eliminated rather than automated; final normalization is equality. |
| 2.7 lia/omega | n/a: no linear arithmetic goal remains after uniform specialization. |
| 2.8 aesop | Actual bounded anonymous trial, failed. |
| 2.9 norm_num/norm_cast | Old pow-base side condition and natural comparison casts disappear; genuine integer→real coefficient cast remains. |
| 2.10 decide | n/a: arbitrary symbolic polynomial inequality not decidable finite computation. |
| 2.11 field_simp/ring | n/a: no denominators or polynomial identity tactic block. |
| 2.12 linear_combination | n/a: no ring-ending proof with hypotheses. |
| 2.13 wlog | n/a: no symmetric case split. |
| 2.14 collapse calc | Applied by eliminating hprod's comparison chain entirely. |
| 2.15 all-goal tactic | n/a: direct specialization creates no parallel similar goals. |
| 3.1 erw | n/a: absent. |
| 3.2 fun_prop migration | n/a: no continuity/measurability tactics. |
| 3.3 omega→lia | n/a: no omega in assigned proof or replacement. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attrs | n/a: single-use helper deleted; no new automation API. |
| 3.6 simp_all | Actual anonymous `simp_all` trial failed; no production simp_all only. |
| 3.7 limits | No production limit exists or was added. |

Automation raw source/log: `automation.lean` / `automation.log`. Additional exact?/apply? trials use the same anonymous-before-target hygiene. Known previous native multi_attempt stalls are not repeated; ordinary Lean compiler provides bounded isolated exploration. Expected-failure files are not used to certify any proof or axiom claim.

## Step back and simplify

The original proof solved a harder intermediate comparison than needed: it bounded the nonuniform product and sum even though the available determinant theorem can already be applied at a larger constant degree function. The direct call is shorter, clearer, and removes a private API. Re-expanding this into a new public generality theorem would duplicate existing CoeffNorm functionality. The preserved local hFcoef is useful because its two coefficient applications differ. No new private helper is justified by the actual ≤30 ordinary-public threshold.

Simplify outcome: **ISSUES-FOUND-AND-FIXED**, performed in-thread because no separate built-in simplify callable is available. Found the redundant one-use uniformization wrapper and removed it; necessary public proof remains a three-stage outline. No unrelated helpers were changed. Fresh final verification and performance follow this change.

## Fresh final verification and gates

`lake build Roth.Theta` exited **0**, with “Build completed successfully (2423 jobs)” in `module-build.log`. Then all isolated normal compiler probes ran sequentially:

| Probe | Exit | Evidence |
|---|---:|---|
| Exact-prefix short replacement candidate | 0 | `candidate.lean`, `candidate.log`; independent proof, no current helper call |
| Exact first 18-line helper plus full-old-type direct replacement | 0 | `independent-helper.lean`, `independent-helper-final.log`: both opaque values typecheck, both have only propext/Classical.choice/Quot.sound |
| Uniform degree restatement | 0 | `uniform.lean`, `uniform.log` |
| All twelve effective-binder drops | 1 expected | `binder-negative.lean`, `binder-map.json`, `binder-results.json`, `binder-negative.log`: every trial has its own compiler error range; no failed probe used as proof evidence |
| Five anonymous clean-prefix automation attempts | 1 expected | `automation.lean`, `automation.log`: grind failed, aesop bounded timeout, simp_all no progress, exact? failed, apply? bounded timeout; no self-reference suggestions |
| Built actual public/caller compatibility and private checks | 0 | `actual-compatibility.lean`, `actual-compatibility.log` |

The first metadata-printing scratch compile used `ToMessageData BinderInfo` and failed; this was corrected to `repr d.binderInfo`. Only the clean corrected exit-0 `independent-helper-final.log` certifies helper proof/type/axioms. It has both expected PASS markers and no PANIC, error, or sorryAx. The compiled twelve-row BinderInfo output compares exactly in `private-binderinfo-comparison.json`, normalizing only anonymous synthetic Fintype binder names.

The immutable complete independent original namespace in `actual-compatibility.lean` is byte-identical to the supplied source (namespace SHA `21d6e67919913a8c9a78c26cc7ca6d775d1bf307f3bcf6cad8a687dc900f02d6`). Its original proof bodies remain independent of the current results. The tail was adapted **only** to require actual absence of deleted helper, then verify the retained sibling.

- Full original public28 type, entire independent old proof, and actual built theorem checked with the exact approved drop set **[DecidableEq, δ, hB, hl′, hδ]**, retained ordinary names/order/BinderInfo, universe arity, retained types, and conclusion. The adapter was not weakened.
- Entire old `index_le_lem6` caller checked with **[]** drops, all original binders/types/BinderInfo preserved, independent old proof value checked.
- Actual built private coefficient helper constant: **ABSENCE PASS**, not omitted from checking. Production source likewise has **zero** references. Retained sibling built opaque proof value and actual full type checked.
- Independent originals, built actual public/caller, recovery theorems, and retained sibling use only **propext, Classical.choice, Quot.sound**. No PANIC, errors, or sorryAx in the successful verifier output.

Fresh **complete unfiltered native LSP**: `final-lsp.json`, success **true**, partial **false**, timed_out **false**, failed_dependencies **[]**, **0 errors / 11 inherited warnings**. No declaration/line/severity filter was supplied. The warnings are header line1; protected/unmodified hr line93; hB/hr line101; hB line109; hr line129; hr line252; unused DecidableEq section variable and DecidableEq type warning on index_le_lem6; hq line486; and DecidableEq type warning on Θ_option_le. No warning points into the replacement or retained sibling. Header metadata and protected hypotheses are outside this leaf.

| Gate | Result | Concrete evidence |
|---|---|---|
| lake_build_file | PASS | Actual command `/Users/ramin/.elan/bin/lake build Roth.Theta` → exit0; `module-build.log` |
| definition_protected | PASS | `scope-gates.json`, `diff.patch`: no definitions changed |
| theorem_statement_protected | PASS | Public type/docstring byte-identical to this checkpoint; exact immutable-original public/caller adapters also compile |
| structure | PASS | Deleted helper; public 21 code/24 including comments ≤30; coefficient local proof 7 physical lines; no >10 branch |
| naming | PASS | No forbidden identifier retained; no rename needed |
| line_packing | PASS | Measured signature table above; helper absent; added line maximum 90 codepoints |
| inequality orientation | PASS | Per-occurrence zero-reversed-inequality table above |
| comments | PASS | Three original Step comments preserved; no helper narrative existed |
| scope | PASS | Before-helper source, entire sibling, public signature/docstring, entire source after public28 unchanged |
| no unintended caller breakage | PASS at this leaf | Entire original index_le_lem6 proof/type adapter and current full module compile |
| full project / separate LeanEval | OWNER PENDING | Not run or claimed by this leaf; owner must run after remaining helper audit |

## Fresh real global profiler / buzz pass

All normal compiler/LSP/search requests finished before profiling. Frozen source SHA:
`90d8ca91b9a74bcc44ee2ca84fb599a4160957417bf78f529d918fe02ec2d5de`.
Exact prefix SHA: `c87f9b141dfa8a4542cf8ac40283998bd93ce888b8ba5bf22555706dd8ad8619`.

Command:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-coeff-helper/final-prefix.lean
```

This profiles the **entire exact source prefix**, including imports, all prior declaration/context, the retained sibling, and public original28; no target trace masking or limits are applied. Prefix closes `end Lemma6` then `end Roth`. Raw UTF-8 log `final-profile.log`; disjoint top-level accounting and source anchors in `final-timings.json`; manifest `final-profile-manifest.json`. Outer command plus associated top-level async proof/kernel/compiler/linter nodes are summed; nested child nodes are not double-counted. Deleted helper has no fictional final timing.

| Declaration | Inherited same-checkpoint baseline ms | Fresh final total ms | Raw outer-command line |
|---|---:|---:|---:|
| `index_separated_mul_le_aux` | 733.357 | 610.207 | 854708 |
| `index_det_le` | 430.371 | 668.264 | 971904 |

Both final totals are below 750 ms; no repeat is required.

Buzz outcome: **FAST-BOARD**, all retained audited extraction declarations below 1000 ms; no limit raises (removed0, added0), no performance deferrals, no new API or instance-priority change. The earlier full-file instrumented default-heartbeat failure at later original29 `index_le_lem6` remains reserved for that audit. This successful prefix trace is **not** represented as a whole-file profiling pass. Actual whole module already built normally; the owner's final whole-module profiling sweep remains separate.

## Required eleven-step checklist and terminal handoff

- [x] Step1: required references read in full, relevant style/naming/profiling consulted.
- [x] Step2: all24 audit findings recorded.
- [x] Step2.5: all five actual search methods, variants, equivalent lookup, and compiled replacement recorded.
- [x] Step2.6: all twelve effective-binder compiled drop probes; successful uniform restatement; private literature exemption and inversion check recorded.
- [x] Step2.7: all baseline signature-line measurements with arithmetic; final deletion resolves helper signature.
- [x] Step2.8: per-occurrence reversed inequality scan recorded.
- [x] Step3: all42 golfing rules have concrete status.
- [x] Step4: independent strategy review and in-thread simplify performed.
- [x] Step5a: fresh complete unfiltered native LSP clean of errors, with all inherited warnings retained in raw output.
- [x] Step5b: actual module build, immutable original proofs/types, exact public/caller adapters, actual built values/standard axioms, scope and real global performance gates completed.
- [x] Step6a: no rename warranted; rename queue/shared reports untouched.

Phase3 file-level fixes: n/a in this dedicated leaf; no header/import/other declaration edits. Phase5a non-rename refactoring: deleted this one-use private wrapper and updated its single routine use. Phase5b: no rename action, zero queue writes. Simplify and buzz outcomes are above. No new helper awaits an additional audit from this leaf; the already-existing sibling retains its scheduled independent audit.

**All normal requests and profiler processes are drained. Source edits are revoked at this terminal handoff.** Final source is immutable at the SHA above. This report contributes **0** original declaration counts. Remaining owner full-build, separate LeanEval and later whole-module profiling gates are explicitly unclaimed.
