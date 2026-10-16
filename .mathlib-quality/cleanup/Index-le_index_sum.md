# Cleanup: `Roth.le_index_sum`

Single-declaration Phase-4 worker, starting at `ef0230f`, `ramin-cleanup`.
Source authority is confined to this declaration and this report. No Git, shared ledger,
rename queue, or other declaration was changed. The file owner runs full-project builds,
LeanEval, cumulative caller verification, and independent final simplify/profile sweeps.

## Result and scope

Applied the explicitly approved `omit [DecidableEq σ] in` before the existing docstring,
and changed the two mathematical lambda arrows from `=>` to `↦`. The public type loses
exactly the approved decidability argument. The literal statement, remaining hypotheses,
argument order, mathematical conclusion, and all existing comments/docstrings are unchanged.
`hs` and the nonzero-summand guard in `hf` are retained. No helpers or imports were added.
The declaration remains 8 nonblank code lines (3 signature + 5 proof lines);
the file changes 269 → 270 lines because the scoped omission adds one line.

The mathematics: every nonzero Taylor coefficient of the sum has a nonzero summand.
That summand is a nonzero polynomial, so its assumed index bound bounds the coefficient's
weight. The lower-bound characterization then gives the desired index bound.

## References read

Read both `lean4/SKILL.md` and `mathlib-quality/SKILL.md`, full `commands/cleanup.md`,
`cleanup-all.md`'s worker/rename/verification contract, full `golfing-rules.md`,
`proof-patterns.md`, `mathlib-search.md`, `generalisation-patterns.md`, `cleanup-gates.md`,
relevant `style-rules.md` and `naming-conventions.md`, `mathlib-review-stages.md`,
`profiling.md`, full `commands/buzz.md`, and the applicable style, generality, automation,
API-extraction and performance sections of `pr-feedback-examples.md`.
I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md.

## Full audit (24 items)

| # | Item | Concrete finding and disposition |
|---|---|---|
| 1 | LINT | Baseline native diagnostics reported unused section σ-DecidableEq and unused decidability-in-type for this theorem. Both disappear after the approved omission. Final complete native diagnostics have zero target warnings/errors. |
| 2 | HAVE SCAN | Only `hfi : f i ≠ 0 := fun h0 ↦ …`; no outer `by`, used twice in `(le_index_iff hfi)` and `hf i hi hfi`. Keep to avoid duplication. Its nested proof has real rewrite content. |
| 3 | SET_OPTION | None in declaration; none introduced. |
| 4 | SIMP SQUEEZE | No `simp`, `simp only`, or `simpa` in retained proof. No squeeze applies. |
| 5 | NAMING | `le_index_sum` states a lower bound for the index of a sum; snake_case, descriptive `le/index/sum`, no forbidden abbreviation, scheme number, single-letter public name, `_ge_` or `_gt_`. No rename needed/queued. |
| 6 | LINE PACKING | All three signature lines measured in Unicode codepoints; full arithmetic table below. No repack required. Actual built width-100 `#check` below. |
| 7 | BY PLACEMENT | Outer `:= by` stays at end of conclusion line; nested `(by rw …)` is a term argument. |
| 8 | FORMAT | Two-space tactics, four-space statement continuation; no blank lines inside declaration, no semicolon chains, no `haveI`/`letI`. Two lambda arrows normalized to `↦`. |
| 9 | COMMENTS | No inline proof comments present. Existing two-line declaration docstring preserved byte-for-byte; all declaration docstrings in the entire file compared equal to worker-start snapshot. |
| 10 | DOCSTRING | Existing source citation and common-bound application guidance preserved. It distinguishes the finite-sum application from the two-polynomial source inequality. |
| 11 | VISIBILITY | Public theorem is used externally at `Roth/Theta.lean:394`, so public visibility is appropriate. Classic import dialect, no module-system visibility rewrite needed. |
| 12 | STRUCTURE | Five proof lines, no conjunction conclusion, no long branches; below 15-line headline theorem budget. No helper or decomposition flag justified. |
| 13 | MATHLIB | Five actual search methods attempted; remote methods DNS-unavailable. Local positive building-block matches verified by compiled `#check`. No unsupported assertion of mathlib absence. See search block. |
| 14 | JUNK DEF | n/a: theorem, no data definition or local wrapper added. |
| 15 | EXISTS LEMMA | n/a: public inequality theorem, not private existential witness wrapper. Existing `obtain` uses mathlib directly. |
| 16 | SHOW vs CHANGE | No `show` or `change` in retained proof. |
| 17 | PUSH_NEG | No `push_neg`, negation-normalization tactic, or contradiction wrapper. |
| 18 | GENERALISE | All 11 outer binders tested mechanically, including data drops with autoImplicit=false. DecidableEq omission is approved and retained; others retained. Parent-class and point-local/nonnegative probes recorded below. |
| 19 | INEQUALITY | Both bound occurrences already use `≤`; no `≥`/`>` in signature. Table below. |
| 20 | NORMAL-FORM | Common lower-bound form is appropriate for this real-valued index with zero mapped to zero; no direct extended-valued valuation replacement preserves this definition. |
| 21 | SYNTAX-GEN | `hf` already localizes to membership in the finite sum and nonzero summands; this is directly useful to Theta's determinant expansion. No beneficial equivalent restatement identified. |
| 22 | IMPORT-FANOUT | n/a: no added or changed imports. |
| 23 | CASTS | 0 dropped, 0 cross-type casts, 0 new load-bearing ascriptions. Diff introduces no cast/ascription. Existing `hfi` proposition annotation is purposeful. |
| 24 | INSTANCE-NAME | n/a: no instance declaration; only approved omission of a section instance. |

Issues found/fixed: the two manifestations of the same unused instance and two lambda arrows.
No deferred source refactoring or rename. The header warning is explicitly user-preserved.

## Mathlib five-method search

| Method | Actual query | Evidence/result |
|---|---|---|
| A Lean-Finder | `weighted order index polynomial finite sum lower bound` | Bounded direct MCP helper attempt; DNS error `[Errno 8] nodename nor servname provided, or not known`. `/private/tmp/roth-index-sum-finder.json`. Unavailable, not no hits. |
| B Loogle | `Finset.sum, _ ≠ 0` | Bounded direct MCP helper attempt; same DNS failure. `/private/tmp/roth-index-sum-loogle.json`. |
| C LeanSearch | `A nonzero finite sum has a nonzero summand` | Bounded direct MCP helper attempt; same DNS failure. `/private/tmp/roth-index-sum-search.json`. |
| D source | Untruncated `rg` for `le_index_sum`, `exists_ne_zero_of_sum_ne_zero`, `weightedOrder.*sum`, `sum.*weightedOrder` in mathlib + project | Local theorem only in project; numerous mathlib uses of `Finset.exists_ne_zero_of_sum_ne_zero`; power-series order APIs found in `MvPowerSeries/Order.lean` and `NoZeroDivisors.lean`. |
| E names | native `lean_local_search exists_ne_zero_of_sum_ne_zero` | Positive `Finset.exists_ne_zero_of_sum_ne_zero` and List variant; index warming disclosed. Compiled checks verify the positive hit. |

Auxiliary variants considered: `min_weightedOrder_le_add`, `weightedOrder_add`,
`le_weightedOrder_mul`, sum variants, nonzero-sum witnesses, List counterpart.
`MvPowerSeries.min_weightedOrder_le_add` is a verified partial analogue over arbitrary
semirings, but it uses natural weights and extended natural orders. It does not replace
this public real-index statement without changing definitions and handling zero.
The common-equivalents table's topology/finiteness/separation buckets do not match.

Whole-goal native `exact?` and `apply?` both hit the default 200000-heartbeat limit;
these are failed generic routes, not a proof of absence. No new mathematical declaration
is being justified by an absence claim. Retain the project-specific theorem and its
existing direct mathlib witness API. No replacement wrapper was introduced; there is no
cast juggling, typeclass plumbing, `rfl` escape, or other missing-API extraction signal.

## Public literature search

Initial exploratory calls batched two queries and produced mixed rankings; those are not
used to infer a per-query ordering. The table records the first three displayed leads of
subsequent single-query calls, including exact-query repeats whose rankings changed.

| Actual single query | First displayed lead | Second | Third | Assessment |
|---|---|---|---|---|
| `Roth polynomial index sum minimum weighted order inequality generalization` (repeat of initial exploratory query) | [Roth, ICM 1958](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf) | [Higher degree polynomials in π(x), v2](https://www.preprints.org/manuscript/202407.1276/v2) | [Same, v3](https://www.preprints.org/manuscript/202407.1276/v3) | Roth's primary text defines the weighted derivative index; the latter leads are unrelated. |
| `Stacks project valuation sum minimum order vanishing` (repeat of initial exploratory query) | [SEC Blockstack filing](https://www.sec.gov/Archives/edgar/data/1693656/000110465919039757/a18-15736_1partiiandiii.htm) | [SEC Blockstack filing](https://www.sec.gov/Archives/edgar/data/1719379/000141057818000410/filename10.htm) | [SEC Blockstack filing](https://www.sec.gov/Archives/edgar/data/1719379/000110465919020748/a18-15736_1partiiandiii.htm) | All irrelevant; motivated the domain-restricted query. |
| `site.stacks.math.columbia.edu valuation v x+y min` (single-query repeat after grouped search) | [Stacks, Lemma 10.50.14](https://stacks.math.columbia.edu/tag/00IF) | [Stacks, valuation rings](https://stacks.math.columbia.edu/tag/00I8) | [Stacks, more morphisms PDF](https://stacks.math.columbia.edu/download/stacks-more-morphisms.pdf) | First primary source supplies the analogous nonzero-sum valuation inequality; third is not used. |
| `Roth index polynomial sum index minimum` (single-query repeat after grouped search) | [Milojević, elementary approach](https://aleksa-milojevic.github.io/expository/roth.pdf) | [Roth, ICM 1958](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf) | [Thue–Siegel–Roth exposition](https://uu.diva-portal.org/smash/get/diva2%3A302893/FULLTEXT01) | Confirms weighted vanishing-order context; the third displayed excerpt includes the sum/min inequality. |

The primary [Stacks lemma](https://stacks.math.columbia.edu/tag/00IF) states the analogous
minimum lower bound with a nonzero sum. The local primary source `clean.tex:589–604`
uses the same addition inequality, derived by vanishing of coefficients below the
smaller index. Its infinity convention for zero differs from this project's real-valued
zero convention. Generalization to an abstract filtered additive structure or to an
extended-valued index is a conceptual future API design, not a compiled public-type
proposal or an approved change. No unsupported claim that arbitrary valuations apply
to this existing `index` is made.

ChatGPT math MCP: n/a, no mathematical second-opinion connector is available in this
session. No literature finding licenses dropping `hs` or changing `hf`.

## Mechanical generalisation: every binder

All drop probes are actual fresh CLI compilations with `set_option autoImplicit false`,
using the original proof and an explicit complete binder list. They import the actual
built module only to access existing APIs, then declare a differently named probe.
Probe evidence is `/private/tmp/roth-index-sum-binder-results.json` and the individual
`roth-index-sum-binder-<label>.lean[.log]` files. Failures are expected negative tests,
not accepted proofs. Results below were collected after the runner completed.

| # | Binder | Class | Use and candidates actually tried | Compiled result / disposition |
|---|---|---|---|---|
| 1 | `{σ : Type*}` | type-variable | Polynomial variable/point/weight domain; drop with autoImplicit=false. Already universe-polymorphic. | exit 1, unknown σ at probe line 5; retain. No stronger universe constraint to weaken. |
| 2 | `[Fintype σ]` | typeclass/data | Required by `index`/`weight` in statement. Drop; replace with parent finiteness class `[Finite σ]`. | Both exit 1, failed Fintype synthesis at probe signature lines 6–7. Retain; current definition needs explicit Fintype data. |
| 3 | `[DecidableEq σ]` | decidability | No required use; drop. | exit 0 with no diagnostics; approved omission applied before docstring. |
| 4 | `{ι : Type*}` | type-variable | Finite-sum indexing type; drop with autoImplicit=false. Already independent polymorphic universe. | exit 1, unknown ι at probe line 5; retain. |
| 5 | `{s : Finset ι}` | structure-value | Both sums and membership restriction; drop. | exit 1, unknown s at probe lines 6–7; retain. No global finiteness assumption to localize: already a Finset. |
| 6 | `{f : ι → MvPolynomial σ ℝ}` | data/function | Summands throughout statement, maps and witness. Drop. | exit 1, unknown f at probe lines 6–7; retain. Coefficient-type abstraction would restate the fixed index definition and requires a separate compiled proposal. |
| 7 | `{α : σ → ℝ}` | data/function | Taylor/evaluation point in every index; drop. | exit 1, unknown α at probe lines 6–7; retain. No global continuity hypothesis or other parent-class weakening applies. |
| 8 | `{r : σ → ℕ}` | data/function | Weight parameter in every index; drop. | exit 1, unknown r at probe lines 6–7; retain. No positivity hypothesis is present, so no strict-to-weak weight assumption to test. |
| 9 | `(hs : ∑ i ∈ s, f i ≠ 0)` | proposition/nonzero | Used by `le_index_iff` for sum. Drop; nonnegative-index replacement `0 ≤ index (∑ i ∈ s, f i) α r`. | Drop exit 1, unknown hs at line 8; nonnegative alternative exit 1, expected polynomial nonzero but got real inequality at line 8. Retain original; no compiled proposal to drop this API argument. |
| 10 | `{c : ℝ}` | data/value | Common lower bound in hf and conclusion. Drop with autoImplicit=false. | exit 1, unknown c at probe lines 6–7; retain. No dependent class to weaken. |
| 11 | `(hf : ∀ i ∈ s, f i ≠ 0 → c ≤ index (f i) α r)` | proposition/local bound | Applied to selected i, membership, nonzero proof. Drop; point-local weakening to a bound only when `eval α (hasseDeriv 0 (f i)) ≠ 0`. | Drop exit 1, unknown hf at line 12. Point-local alternative exit 1: nonzero polynomial hfi cannot discharge the nonzero point-evaluation condition at line 12. Retain original. |

The quantified components of `hf` were also classified: `i` is bound sum-index data,
`i ∈ s` is already a point/set-local restriction, and `f i ≠ 0` excludes the zero-summand
case. Removing a premise of an implication inside `hf` would strengthen the required
hypothesis, not weaken the theorem's outer assumptions. All genuinely applicable
catalogue candidates are covered by the drop/Finite/point/nonnegative probes. No
strict `<` hypothesis, bijection, topology, differentiability, completeness, field class,
or bundled conjunction hypothesis occurs here.

Inversion check: after moving maps through the sum, the nonzero-summand witness is a
generic additive-map fact, but the initial/final `le_index_iff` conversions are still
specific to index. The abstract mathematical idea is a filtered additive lower-bound
principle, already reflected by the partial power-series order API found in search.
Changing the coefficient/order model or the zero convention is an API restatement,
not a hidden unused-hypothesis deletion. No additional public API change is applied
or represented as approved. All 14 independent probe processes reached the expected
statuses and exited before source release.

## Signature packing and inequalities

The source signature is byte-identical to the start snapshot. Unicode codepoint widths,
including indentation, were measured with Python `len`, not byte lengths.

| Signature line | Width | Next complete syntactic token | Arithmetic | Action |
|---|---:|---|---|---|
| 117 | 98 | `(hs : ∑ i ∈ s, f i ≠ 0)` (23) | 98 + 1 + 23 = 122 > 100 | ok |
| 118 | 83 | `c ≤ index (∑ i ∈ s, f i) α r := by` (34) | 83 + 1 + 34 = 118 > 100 | ok |
| 119 | 38 | none; proof body next | n/a, final signature line | ok |

Before and after packing tables coincide: no parameter or conclusion fits across either
break. No narrow wide-hypothesis exception was used.

Actual built `#check @Roth.le_index_sum` with `set_option format.width 100`:

```lean
@Roth.le_index_sum : ∀ {σ : Type u_1} [inst : Fintype σ] {ι : Type u_2} {s : Finset ι} {f : ι → MvPolynomial σ ℝ}
  {α : σ → ℝ} {r : σ → ℕ},
  ∑ i ∈ s, f i ≠ 0 → ∀ {c : ℝ}, (∀ i ∈ s, f i ≠ 0 → c ≤ Roth.index (f i) α r) → c ≤ Roth.index (∑ i ∈ s, f i) α r
```

This is verbatim tool output, including the pretty-printer's own wrapping. There is no
σ-DecidableEq argument. Both independent type universes remain polymorphic.

| Occurrence | Location | Form | Rewrite | Rename |
|---|---|---|---|---|
| 1 | `hf`, line 118 | `c ≤ index (f i) α r` | none, already smaller-left | none |
| 2 | conclusion, line 119 | `c ≤ index (∑ i ∈ s, f i) α r` | none, already smaller-left | none |
| reversed orientation scan | entire signature | n/a: zero `≥` and zero `>` | none | no `_ge_`/`_gt_` in target name |

The `≥` inside the source quotation is preserved prose, outside this gate.

## All 42 golf rules

| Rule | Status and concrete evidence |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | n/a: outer `rw … at hd` is followed by witness extraction, not immediate `exact`; inner `rw` closes a zero equality. |
| 1.4 | n/a: no simp/exact pair. |
| 1.5 | n/a: no trailing `rfl` after simp. |
| 1.6 | n/a: no constructor branches. |
| 1.7 | n/a: no apply/exact pair. |
| 1.8 | n/a: no contradiction/push_neg pair. |
| 1.9 | Considered both lambdas: first binds `d` and `hd` for a proof block; second transforms `h0` using rewrite. Neither is a removable eta expansion. Arrows normalized. |
| 1.10 | Sole `hfi` used twice, so retained. |
| 1.11 | Already `refine … fun d hd ↦ ?_`; no apply/intro boilerplate. |
| 1.12 | n/a: no redundant `show`. |
| 1.13 | Already direct `obtain ⟨i, hi, hid⟩`, no projected temporary. |
| 1.14 | Already merged `[map_sum, map_sum]`; repeated applications act on two different maps. Inner `[h0, map_zero, map_zero]` also merged. |
| 1.15 | n/a: no terminal simp only. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | Existing `.2`/`.1` use the iff API directly; no more useful dot-notation chain identified. |
| 1.18 | n/a: parenthesized nested proof is an argument to `hid` within a lambda; changing it to `<|` gives no useful clarity/size gain. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no trivial private existential helper. |
| 2.1 | Native whole-proof `grind` tried; failed with the desired inequality unresolved, no source change. |
| 2.2 | n/a: retained proof has no grind, so no preceding tactics to delete. |
| 2.3 | Native `simp_all` whole-proof attempt leaves the index goal; generated follow-on `hd` error reflects replacing the first line, not a successful replacement. No consolidation applies to retained code. |
| 2.4 | n/a: no continuity/differentiability/measurability goal. |
| 2.5 | n/a: no structure-derived positivity goal. `f i ≠ 0` requires the selected nonzero coefficient and is not derivable from positivity instances. |
| 2.6 | Native whole-proof `gcongr` tried; explicitly reports no progress. The index operation has no applicable monotonicity congruence here. |
| 2.7 | n/a: no Nat/Int linear-arithmetic goal; real inequality follows index API. |
| 2.8 | Native whole-proof `aesop` tried; default 200000-heartbeat timeout. No limit increase. |
| 2.9 | n/a: no numeric evaluation or coercion arithmetic. |
| 2.10 | n/a: universally quantified polynomial/index inequality is not a finite decidable computation. |
| 2.11 | n/a: no rational expression identity or denominator manipulation in proof. |
| 2.12 | n/a: no terminal ring/ring_nf goal with algebraic hypotheses. |
| 2.13 | n/a: no symmetric cases. |
| 2.14 | n/a: no calc block. |
| 2.15 | n/a: only one active goal at each step; no repeated independent closing branches. |
| 3.1 | n/a: no erw, ordinary rw already used. |
| 3.2 | n/a: no continuity/measurability tactics. |
| 3.3 | n/a: no omega, and no applicable integer arithmetic per 2.7. |
| 3.4 | n/a: no rcases-with-rfl substitution. |
| 3.5 | No attribute added: a conditional arbitrary lower-bound theorem is not a simp normal-form rule; ext/fun_prop also do not apply. Global grind registration would be a separate API decision. |
| 3.6 | n/a: no retained simp_all only; trial simp_all did not close goal. |
| 3.7 | n/a: no heartbeat/recursion override to remove. |

Step-back reflection: this proof follows the mathematical coefficient argument directly.
Whole-proof automation and `exact?`/`apply?` did not close efficiently; the latter two
hit the default heartbeat limit. A direct coefficient/sInf proof was independently
constructed and compiled (below), but is longer. Inlining `hfi` duplicates its proof and
obscures the single reason the chosen summand is nonzero. No alternative was selected
on an unmeasured performance claim. Retain this explicit five-line proof.

## Compilation, trust, and independent proof gates

- Actual `/Users/ramin/.elan/bin/lake build Roth.Index` exited **0**, built target in 21s,
  completed 1501 jobs. Full output: `/private/tmp/roth-index-sum-build.log`.
  Warnings are the preserved header and declarations still awaiting their own workers;
  the target has none.
- Actual complete native `lean_diagnostic_messages` on the **unfiltered entire Index file**:
  `success=true`, `partial=false`, `timed_out=false`, `failed_dependencies=[]`, no errors.
  Exact full JSON: `/private/tmp/roth-index-sum-final-diagnostics.json`.
- Fresh independent proof: `/private/tmp/roth-index-sum-independent.lean`, CLI exit **0**,
  log `/private/tmp/roth-index-sum-independent.log`. It imports only the original
  lower-level dependencies, reproduces the unchanged `index` definition, and proves the
  original public type directly using Taylor coefficients, support membership, nonzero
  sum witnesses and `le_csInf`/`csInf_le`. It does not import `Roth.Index`, call the target,
  use its private support helper, or use any other theorem declared in Index.
- Original public-type recovery: original signature was extracted from
  `/private/tmp/roth-index-original.lean` (e557886), then elaborated with its original
  `[DecidableEq σ]` section argument against the actual built module in
  `/private/tmp/roth-index-sum-check.lean`; CLI exit **0**. The unused-instance warning in
  this recovery is expected evidence that the original argument was retained.
- Actual built `#print axioms Roth.le_index_sum` and separate recovery declaration both
  return exactly `[propext, Classical.choice, Quot.sound]`.
- Independent `#print axioms Roth.independent_sum` returns exactly the same standard set.
  No `sorryAx`, trust extension, or new axiom appears in the accepted proofs.

The first independent scratch attempts failed due to aggressive simplification of a sum,
coefficient API spelling, goal ordering after `apply`, and using `map_sum` instead of
`coeff_sum`. Those failed attempts were repaired; only the final exit-0 standard-axiom
proof is accepted as evidence. Native profile extraction also failed as documented
below. Scratch errors never entered project source.

### Complete remaining native warning inventory

| Line | Warning |
|---:|---|
| 1 | user-preserved copyright/header too short |
| 205 | index_C_mul: unused section σ-DecidableEq |
| 233 | index_le_card: unused section σ-DecidableEq |
| 200 | index_neg: unused section σ-DecidableEq |
| 222 | index_rename: unused section σ-DecidableEq |
| 210 | index_mul_left_weights: unused section σ-DecidableEq |
| 129 | weight_eq_finsuppWeight_div: unused section σ-DecidableEq |
| 243 | index_unique: unused section σ-DecidableEq |
| 199 | index_neg: unused decidability in type |
| 126 | weight_eq_finsuppWeight_div: unused decidability in type |
| 204 | index_C_mul: unused decidability in type |
| 166 | index_mul: unused decidability in type |
| 233 | index_le_card: unused `hr` |
| 230 | index_le_card: unused decidability in type |
| 182 | index_prod: unused decidability in type |
| 219 | index_rename: unused σ- and τ-decidability in type |
| 209 | index_mul_left_weights: unused decidability in type |
| 140 | index_eq_weightedOrder_div: unused decidability in type |
| 240 | index_unique: unused decidability in type |

All 19 are recorded, not suppressed or filtered away. Target range has zero warnings/errors.

### Diff and preservation gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.Index`, exit 0; output log above. |
| definition_protected | pass | Snapshot diff changes no definition/abbrev and no data. |
| theorem_statement_protected | pass with explicit approved instance omission | Literal declaration statement unchanged; actual public type loses exactly the authorized σ-DecidableEq. Original type recovered separately. |
| structure_gate | pass | Five proof lines, no ∧, no long branch; headline threshold 15. |
| naming_gate | pass | Descriptive snake_case, zero forbidden patterns/abbreviations; no rename. |
| line_packing_gate | pass | Every signature line included in measured table; both joins exceed 100. |
| inequality_orientation_gate | pass | Complete occurrence table, zero reversed Lean inequalities. |
| comments-preserved | pass | Zero proof comments originally; two-line target docstring exact. All file declaration docstrings compared equal. |
| no-scaffolding/no-limit-raises | pass | No profiling/trace/count-heartbeat commands or limit raises added to source. |
| new identifiers | pass | Diff introduces no mathematical identifier; only built-in scoped `omit` and Unicode lambda syntax. Existing named lemmas verified by build and compiled checks. |
| cumulative_no_unintended_breakage | owner checkpoint | External caller Theta:394 identified; owner controls complete caller/full build/LeanEval gates. No claim that this worker ran full-project checks. |

Diff evidence: `/private/tmp/roth-index-sum.diff` (compared against worker-start snapshot,
not the original file-wide baseline). No loss of comments, headers, imports or previous
workers' edits. No rename sidecar mutation; unrelated queue entry remains owner's.

## Scoped simplify and buzz

Scoped simplify review: PASS-THROUGH after the approved syntax cleanup. No duplicated
single-use proof skeleton, unnecessary helper, redundant import, duplicated `hfi`, or
further quality/efficiency issue warrants a new source change. The built-in `/simplify`
invocation tool is unavailable; this is an explicit manual scoped review, with the file
owner's independent final holistic simplify pass still required.

Native `lean_profile_proof` at target line 117 was attempted and failed to compile its
standalone extraction: `cannot omit referenced section variable` and `unexpected end of
input; expected 'lemma'`. This is the documented same-file/scoped-omit extraction
limitation, not a target compilation failure.

Actual CLI fallback completed with exit **0**:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean
python3 /private/tmp/roth-index-profile-parse.py sum-final
```

Full trace `/private/tmp/roth-index-sum-final-profile-trace.log`; parsed 19/19 anchored
current declarations in `/private/tmp/roth-index-sum-final-profile-table.json`.
An initial parser call happened before the compiler finished and correctly failed its
all-declarations assertion; after process exit 0, rerunning the parser succeeded. Only
the complete successful table is accepted.

| Decl | Source line | Command ms | Proof ms | Full command + async ms | Largest tactic |
|---|---:|---:|---:|---:|---|
| le_index_sum | 117 | 25.453 | 358.515 | 394.921 | `rw [map_sum, map_sum] at hd`, 187.690ms |

Budget 1000ms; target is below the 750ms borderline threshold. Outcome FAST-BOARD for this
single declaration. No performance fix, before/after speedup, or heartbeat reduction is
claimed. Zero limit raises added/removed; no deferrals. Broader sweeps remain owner gates.

## Eleven checked worker phase steps

- [x] Step 1: reference documents read; applicable skill instructions applied.
- [x] Step 2: all 24 audit rows present with concrete findings.
- [x] Step 2.5: all five actual search methods, positive local verification, remote failures disclosed.
- [x] Step 2.6: every outer binder mechanically probed; parent/point/nonnegative alternatives and literature recorded.
- [x] Step 2.7: every signature line measured; actual built width-100 check included.
- [x] Step 2.8: full inequality occurrence/orientation table included.
- [x] Step 3: all 42 numbered golf rules have status and evidence/inapplicability.
- [x] Step 4: strategy, term composition, automation and independent coefficient proof reviewed.
- [x] Step 5a: complete native LSP success, no target warnings/errors.
- [x] Step 5b: actual module build, diff protection, structure/naming/packing/orientation and trust gates.
- [x] Step 6a: no rename needed; sidecar intentionally untouched.

Full-project build, separate LeanEval, cumulative source/Expr audits and publication are
file-owner checks after source authority release, not claimed by this worker.

## Source freeze and handoff

All Lean requests and every compiler/process session completed before release. Frozen
source SHA256: `ca55d5c8adada4876194803c57bc4ab41cad3f30c13f17d414827852de268aeb`.
`SOURCE AUTHORITY RELEASED` was sent and acknowledged by the file owner; source
authority was revoked. Subsequent work was report-only. No source edits, source reads,
Lean requests, or builds occurred after release. Owner checkpoint results are maintained
by the owner and are not fabricated here.


## Owner checkpoint d11

Frozen SHA256 `ca55d5c8adada4876194803c57bc4ab41cad3f30c13f17d414827852de268aeb`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session73801 exit0, `/private/tmp/roth-index-d11-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval86657 both exit0(150.60s/35.53s),
Index+Theta hashes stable; `/private/tmp/roth-index-d11-{full,leaneval}.log`.
Worker COMPLETE unfiltered Index LSP success=true partial=false timed_out=false, 0target diagnostics/19other warnings. External Theta complete native LSP0errors/23inheritedwarnings, noinfos/no faileddependencies after one45second partial request followed complete retry; sole le_index_sum callerTheta:394 accepted. Raw /private/tmp/roth-index-d11-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
