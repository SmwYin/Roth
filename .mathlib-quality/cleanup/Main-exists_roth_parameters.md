# Necessary parameter helper: local final acceptance evidence

The helper chooses compatible polynomial/coefficient/dimension/delta witnesses. Cleanup replaces the manual coefficient support split with `Finsupp.single_eval_le_sum`, removes unused local aliases and intermediate arithmetic, and uses bounded `nlinarith only [hm, hdeg]`. Both original mathematical proof signposts and the immediate ordinary comment remain. Declaration 24 → 17 lines; proof 19 → 12 lines; largest branch 3 lines. Name remains descriptive/private/snake_case with `_aux`.

This is **local helper acceptance only**, without original-declaration count credit, standalone publication, or wholefile completion. The original15 parent remains unchanged and must resume under the same author, use this necessary helper, complete its audit, and publish parent plus helper jointly. No Git, shared-progress, accepted-helper, caller, parent, other-report or rename-queue edits by this worker.

## Baseline and source binding

Reused accepted14 actual FULL build 47.012 s and separate Eval 33.770 s, with explicit qualification: the prior scratch/Eval overlap protocol failed; those are correctness observations, not a clean isolation certificate. Prior native/LSP evidence is historical only; fresh current checks below replace it for this helper change. No redundant unchanged baseline build was performed.

Genuine first draft saved before any helper Lean/golf at `/private/tmp/roth-main-integral-roth/helper-parameters-FIRSTUNGOLFED.lean`, SHA256 `725fc6287d4ddc39d2c060f8b82c191af850b7507c2dd9641f4518fe18683ad5`; independently verified byte-for-byte against the initial source insertion and copied locally before first launch. Worker entry Main SHA256 `eccc66e3d5e8bb97e40a04accec9c6549fc8bb6ef659591e0ef64a0d772ee11b`. Final Main SHA256 `beefff091b2311bc3ac34168e9cbc1f8e617de72e255e02c4594b676cde85c17`. Every byte outside helper declaration is identical to worker entry; parent/callers and accepted preceding helpers are unchanged. LeanEval SHA256 remains `610ec95658c5d43c931217bfb56b54d62f825473de17b3bdf6a1dde85dd900ca`.

## Actual final gates

All compiler, native, semantic and LSP launches/queries were strictly serial.

| Gate | Actual evidence | Result |
|---|---|---|
| FULL project build | `lake build`, final-full-build terminal exit 0, 58.316 s | pass |
| Separate Eval build | subsequent `lake build Roth.LeanEval`, terminal exit 0, 30.225 s | pass |
| Native Main | `lake env lean Roth/Main.lean`, exit 0, 29.367 s | pass |
| Native Eval | subsequent `lake env lean Roth/LeanEval.lean`, exit 0, 29.685 s | pass |
| Native root | subsequent `lake env lean Roth.lean`, exit 0, 26.594 s | pass |
| Complete unfiltered LSP Main/Eval/root | all terminal, partial=false, success=true, zero errors; Main sole existing header warning, Eval/root no diagnostics | pass |
| Definition protection | no def/abbrev edits | pass |
| Statement protection | same complete strict elaborated TYPE before/after; signature whitespace and redundant same-type cast only | pass |
| Structure | 12 proof lines, branches ≤3; mathematically correlated existential retained | pass |
| Naming | descriptive private exists_roth_parameters_aux, no forbidden pattern | pass |
| Packing/orientation | all 5 signature lines measured below; all inequalities ≤/< | pass |
| Scoped no unintended breakage | full/separate Eval/native/LSP checks; no helper caller yet; parent untouched | pass |
| No scaffolding/trust/limit changes | no sorry/new axioms/native_decide/count_heartbeats/options/imports introduced | pass |

## Actual semantic checks

Before any per-row guards, complete actual families and universes were enumerated to `actual-families-before-guards.json`: production only `_private.Roth.Main.0.Roth.exists_roth_parameters_aux`, independent only `Roth.independentParameters`, actual universe lists both `[]`. First draft genuinely had its root plus `_proof_1_1`, and both were checked in the first-draft profile; final has no such generated member. No assumed suffix counts or blanket empty-universe checks.

Fresh independent proof chooses a different bound `max 1 (sum abs coeff)` and proves coefficients by support cases, using only accepted preceding mathematical parameter lemmas. Its actual opaque proof does not reference the production helper, circular wrappers, later Main declarations, or Roth. Complete recursive strict Name/Level/BinderInfo/metadata/literal/projection Expr comparison, without ExprBEq shortcut, establishes genuine firstdraft/current/independent root TYPE equality. No signature weakening, old-contract recovery wrapper, or caller change is needed.

Each actual current/independent row was then checked in a separate default-budget command: actual opaque VALUE inferred at its complete TYPE, closed (including levels), no admits, only propext/Classical.choice/Quot.sound, no self or cross-target dependency, external ModuleIdx strictly upstream. Actual fresh local graph is acyclic. Accepted earlier library/DATA/proof evidence is reused; no imported-DAG replay or preceding universe clone. Proof VALUEs were inspected in memory; persisted receipts contain small hashes/lengths and full TYPEs, not full raw VALUE dumps or identity claims. Main proof repr length 3,247,703 bytes/hash 17666879361712112899; independent length 3,268,401/hash 5999546298803203897. Defaults actual 200000/20000/512. `semantics` terminal exit 0, 38.084 s.

## Buzz: actual exact-prefix profiles

Every phase acquired owner HOLD ACK **before preparation**, retained owner write/heavy-review/parsing/compiler/native/LSP idleness through preparation/capture/env/default/maps/freeze and actual unparsed drain, then waited for explicit OWNER RELEASE before parsing. All profile child and driver exits 0; all groups absent. Parent/Lake full environment equality checked IN MEMORY ONLY; persisted only safe allowlist/hash/length. Default pre/post 200000/20000/512. Exact current binary/source/import/prefix/maps frozen.

| Exact source | Full disjoint sum | Mandatory repeat | Result |
|---|---:|---|---|
| Genuine firstdraft sample 1 | 823.787 ms | ≥750, repeated same freeze | under 1000 |
| Genuine firstdraft mandatory repeat | 869.316 ms | required repeat completed, separately reported | under 1000 |
| Final helper exact prefix | 465.434 ms | <750, none required | FAST-BOARD |

Final disjoint roots: outer canonical lemma command 104.077 ms, async proof 341.176 ms, async kernel parent 9.095 ms (nested actual kernel 9.061 ms not added again), async linter parent 11.086 ms. No compiler parents or lazy prior DATA roots on the target. Actual final profile family is the one private root; its complete TYPE bytes/universes equal the corresponding current semantic row. Full target canonical payload, not an anchor alone, matched.

The macro-expanded private theorem prints earlier at raw indent 0 (104.026 ms) but is nested INSIDE the canonical lemma command; excluded from additive roots. Finite exact full inner/outer payload bindings for all three captures and unchanged installed Mathlib expandLemma/Lean recursive elabCommand source hashes reuse accepted9 source-backed ownership evidence. Indentation alone was not used. Receipts: each phase `expanded-command-parent-binding.json`. No extra captures, discarded/cherry-picked sample, historical-context speedup ratio, or noise dismissal. No performance deferral or limit raises.

## Width-100 actual #check reference

Actual final exact-prefix `set_option format.width 100 in #check @Roth.exists_roth_parameters_aux` output:

```lean
@Roth.exists_roth_parameters_aux : ∀ {α κ : ℝ},
  IsIntegral ℤ α →
    2 < κ →
      ∃ f A m δ,
        f.Monic ∧
          (Polynomial.aeval α) f = 0 ∧
            1 ≤ A ∧
              (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) ∧
                2 ≤ m ∧
                  0 < δ ∧
                    δ < 1 / ↑m ∧
                      Roth.eta δ m + 2 * (1 + 3 * δ) * ↑f.natDegree * √↑m < ↑m / 2 ∧
                        ↑m * (1 + 4 * δ) / (Roth.gam δ f.natDegree m - Roth.eta δ m) < κ
```

## Required phase checklist

- [x] Installed full skills/workflows/references read.
- [x] 24-item audit, full HAVE, five-method search and per-binder review.
- [x] Every one of 42 golfing slots considered with concrete status.
- [x] Packing/orientation artifacts and mathematical structure necessity.
- [x] Step-back review and scoped non-rename/rename decisions.
- [x] Actual full/separate Eval/native/complete unfiltered LSP gates.
- [x] Complete actual families/universes before guards; strict types and opaque values.
- [x] Manual holistic review; simplify tool unavailable, no invocation claim.
- [x] Genuine firstdraft and mandatory repeat, final exact-prefix buzz gate.
- [x] All launches/queries/drivers terminal; groups absent; all leases released at END.

Detailed scope audit and rule statuses follow.

# Parameter helper audit, original15 dependency

Scope: only private `exists_roth_parameters_aux` and immediate ordinary comment. Parent/callers and accepted earlier helpers are outside worker scope. Required full installed skills, cleanup/cleanup-all workflows and named references read. Simplify is unavailable; final substantive manual holistic review is required, with no invocation claim.

## Initial 24-item audit

| Item | Concrete finding/action |
|---|---|
| 1 LINT | Prior complete Main diagnostics: header warning only; fresh complete diagnostics required after edits. |
| 2 HAVE | hsum0 no-by used by hA1 and hA automation: replace both automation sites by ordered API; hA1 has-by used in hA and result: remove via direct result field; hA has-by used once: coefficient API proof directly in result branch; hm2 has-by used once: direct bounded nlinarith field; nested `have : 4 ≤ n²` has-by used once: eliminate via direct nlinarith. |
| 3 SET_OPTION | None in helper; actual defaults mandatory. |
| 4 SIMP | Terminal simpa in unsupported-coefficient branch disappears with generic API. New `by simp` is terminal, remains unsqueezed. |
| 5 NAMING | Descriptive snake_case existential Roth parameter choice; private `_aux`, no forbidden abbreviation/number pattern. No rename required. |
| 6 PACKING | Repack conclusion conjunct `1 ≤ A` onto preceding signature line; remove redundant same-type cast; emit final all-line width table. |
| 7 BY | Already at preceding line end; preserve. |
| 8 FORMAT | Replace all helper lambda `=>` by `↦`; remove unused set equality hAdef and n alias. No haveI/letI. |
| 9 COMMENTS | Preserve coefficient-bound and m/δ signposts verbatim, re-anchor naturally. |
| 10 DOCSTRING | None on private helper; ordinary immediate comment appropriate. |
| 11 VISIBILITY | Private and only local dependency; retain. |
| 12 STRUCTURE | Shared witnesses f/A/m/δ correlate all facts; splitting conjunction loses compatible witnesses or duplicates choices. Necessary existential choice, not tuple-of-reflexivity wrapper. 19 proof lines initially; no long branch; target ≤30, no extraction. |
| 13 MATHLIB | A–E below; use generic Finsupp.single_eval_le_sum directly; retain genuinely correlated parameter choice using accepted exists_m and exists_delta. |
| 14 JUNK DEF | n/a lemma; proof-local A names actual coefficient bound. |
| 15 EXISTS | Nontrivial coefficient and parameter inequalities, not reflexivity tuple. Necessary helper for headline ≤15 proof lines. |
| 16 SHOW | None. |
| 17 PUSH_NEG | None. |
| 18 GENERALISE | Per-binder table below; no optional ambient restatement. |
| 19 INEQUALITY | Signature/hypotheses contain no ≥ or >; all oriented ≤/<. |
| 20 NORMAL-FORM | Polynomial monicity/aeval, degree, eta/gam constraints use accepted canonical project APIs. |
| 21 SYNTAX-GEN | Existential joint choice directly supports parent obtain; splitting would harm application. |
| 22 IMPORT-FANOUT | No imports added. |
| 23 CASTS | Remove same-type ℤ ascriptions on f.coeff; retain actual ℤ→ℝ and ℕ→ℝ casts and bound A : ℝ. |
| 24 INSTANCE-NAME | No instances declared. |

## Five-method search

A Lean-Finder query: absolute value of any coefficient of an integer polynomial bounded by sum absolute values coefficients. Hits: cauchyBound, Mahler measure, no direct local contract.
B Loogle `Polynomial.coeff, abs, Finset.sum`: empty items.
C LeanSearch coefficient absolute value bounded by sum: le_gaussNorm, Mahler measure; heavier notions/imports than required.
D untruncated source searches `sum_abs|coeff.*le.*sum|le_sum.*coeff|exists.*coeff.*le|sum.*coeff.*bound`: accepted CoeffNorm.abs_coeff_le_normOne uses generic Finsupp.single_eval_le_sum. Full name grep located Data/Finsupp/Order.lean:165.
E local name `sum_abs`: index unavailable, not absence evidence; subsequent exact name `Finsupp.single_eval_le_sum` found source while index warming. Generic compiled LSP attempt at coefficient goal closes it, with only subsequent obsolete branches reporting no goals. Auxiliary variants: coefficient sum, norm, Gauss bound, single_le_sum/single_eval_le_sum. Common-equivalents: boundedness bucket would add unnecessary bornology machinery for this finite coefficient construction.
Conclusion: partial generic API match; use directly inside the nontrivial joint existence helper. Whole exact? compiled failure confirms no one-step result for full correlated contract; no claim of global mathematical absence.

## Per-binder generalisation

| Binder | Class/use | Candidates/reason | Result |
|---|---|---|---|
| {α : ℝ} | concrete value in aeval/root conclusion | drop makes statement unbound; ambient ordered-field restatement changes subject and dependencies | retain, no optional ambient generalisation |
| {κ : ℝ} | value shared by hκ and strict final ratio | drop makes statement unbound | retain |
| hint : IsIntegral ℤ α | proposition provides monic integer annihilator | drop loses only root witness source; irrational/transcendental α refutes conclusion without algebraicity | retain necessary; no false drop compilation claim |
| hκ : 2 < κ | proposition used in exists_m and final ratio | drop or 2 ≤ κ cannot provide strict ratio below κ at κ=2; numerical expression has ratio >2 for positive degree/dimension | retain strict; no false weakening compilation claim |

No typeclass, decidability, function-property, universe binder or bundled morphism. Inversion: proof essentially uses integer polynomial annihilator, degree, and Roth eta/gam parameter estimates throughout; ambient extraction would change scope. Literature n/a private helper.

## All 42 golfing slots

| Slot | Status |
|---|---|
| 1.1 | n/a no by-exact wrapper |
| 1.2 | n/a no by-rfl |
| 1.3 | n/a no rw/exact sequence |
| 1.4 | n/a no simp/exact sequence |
| 1.5 | n/a no trailing rfl |
| 1.6 | joint anonymous constructor already appropriate |
| 1.7 | direct bound term replaces manual proof plumbing |
| 1.8 | n/a no contradiction |
| 1.9 | no eta-redex; coefficient function depends on argument |
| 1.10 | remove hsum0/hA1/hA/hm2 after replacing their mathematical content directly |
| 1.11 | n/a no apply/intro sequence |
| 1.12 | n/a no show |
| 1.13 | existing obtains already destructure witnesses |
| 1.14 | n/a no rw chain |
| 1.15 | n/a no terminal simp only |
| 1.16 | n/a no nonterminal bare simp |
| 1.17 | use `.trans` ordered bound |
| 1.18 | no beneficial trailing parenthesis removal on nonfinal argument |
| 1.19 | n/a no push_neg |
| 1.20 | not trivial reflexivity existence; preserve necessary choice |
| 2.1 | actual whole grind fails; coefficient grind also fails |
| 2.2 | n/a no grind retained |
| 2.3 | obsolete coefficient simpa branch eliminated by API |
| 2.4 | n/a no function regularity goal |
| 2.5 | actual coefficient positivity fails: not positivity goal; sum nonnegative directly uses API |
| 2.6 | no monotonic composition needed beyond direct le_add/trans |
| 2.7 | replace nested omega stage by bounded nonlinear arithmetic using exact hm/hdeg |
| 2.8 | actual whole aesop exhaustive search fails; remainder errors from missing witnesses are probe fallout |
| 2.9 | n/a no concrete cast/numeric normalization subgoal after direct API |
| 2.10 | n/a infinite real existential contract not finite decidable computation |
| 2.11 | n/a no algebraic identity involving denominators |
| 2.12 | n/a no ring/ring_nf terminal proof |
| 2.13 | n/a no symmetric branches |
| 2.14 | use direct term trans instead of calc |
| 2.15 | result fields differ, shared closing tactic would not apply |
| 3.1 | n/a no erw |
| 3.2 | n/a no continuity/measurability |
| 3.3 | remove omega rather than introduce it; nonlinear dimension needs nlinarith |
| 3.4 | n/a no rfl destructuring |
| 3.5 | private existential choice is not canonical simp rewrite |
| 3.6 | n/a no simp_all only |
| 3.7 | no limit raises present or introduced |

Step-back: whole grind/aesop/exact? actual attempts failed; distinct mathematical witness choices remain necessary. Generic coefficient API shortens the proof and removes a support case split; no new helper/API extraction needed. All 24/42 slots reviewed before final gates.

## Final packing and orientation artifacts

The exact final signature is measured in codepoints, including the conclusion. Atomic binders/conjuncts are the packing units; internal expressions are not split to strand a quantifier/operator on the preceding line. The final exact-prefix profile supplies the actual width-100 #check reference.

| Signature line | Chars | Next atomic signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 406 | 89 | `∃ (f : Polynomial ℤ)` (20) | 89 + 1 + 20 = 110 > 100 | ok |
| 407 | 94 | `(∀ i, |(f.coeff i : ℝ)| ≤ A)` (28) | 94 + 1 + 28 = 123 > 100 | ok |
| 408 | 64 | `eta δ m + 2 * (1 + 3 * δ) * f.natDegree * √(m : ℝ) < m / 2` (58) | 64 + 1 + 58 = 123 > 100 | ok |
| 409 | 66 | `(m : ℝ) * (1 + 4 * δ) / (gam δ f.natDegree m - eta δ m) < κ := by` (65) | 66 + 1 + 65 = 132 > 100 | ok |
| 410 | 71 | proof body next | n/a | ok |

| Inequality occurrence | Original | Rewrite | Rename |
|---|---|---|---|
| Signature + all hypotheses/body | No `≥` or `>` tokens | n/a; all inequalities already `≤`/`<` | none |

Final HAVE scan: no `have` remains. Polynomial and parameters come from three obtains; local A is a genuine witness expression. Largest branch 3 lines; joint correlated existential conclusion retained for mathematical necessity. New API names verified by exact source grep and successful full build; no new imports or definitions.

Manual holistic simplify review (actual built-in simplify unavailable, not invoked): checked reuse, duplicate proof skeletons, joint witness dependency, coefficient API, arithmetic scope and proof/comment placement. Generic coefficient API removes missing-API plumbing; no further local issue. Parent setup duplication remains parent-owned until the same parent author resumes; no wholefile completion claim here.

Failed probes: whole grind and exact? did not solve full contract; whole aesop failed exhaustive search, with unknown witness errors in subsequent original lines (probe fallout, no source mutation). Coefficient grind failed; positivity rejected a non-positivity goal. Direct coefficient API attempt closed its goal and made the subsequently retained old branches report no goals. Scratch independent proof initially oversimplified a max-bound; fixed via explicit terminal simp-only, production unchanged. No failures hidden as passes.

Phase 5a: direct use of Finsupp.single_eval_le_sum; no new extraction. Phase 5b: no rename needed, shared queue untouched by scope. Comment preservation: immediate ordinary comment plus both original proof signposts retained verbatim. No docstrings added to private helper. Casts: all five redundant same-type coefficient ℤ annotations eliminated with obsolete code; five explicit cross-type term casts retained; witness A and callback integer binder annotations are load-bearing.
