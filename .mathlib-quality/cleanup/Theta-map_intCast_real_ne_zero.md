# Dedicated cleanup: `Roth.map_intCast_real_ne_zero`

## Scope and outcome

Original private helper at baseline `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`, lines 64–66.
Worker start: `79b262cdf52b5db9b07e870d3ee4925ab138ba1d`.
Deleted the three-line wrapper and replaced its seven uses in five existing proofs with
`(map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 ...`.
Unconstrained `have` bindings explicitly fix `map (Int.castRingHom ℝ)` to supply the target type.
No replacement declaration was introduced. Public definitions, theorem types, names, visibility,
instances, positivity assumptions, imports, header metadata, and all existing comments are unchanged.
The wider public-contract candidate menu remains unapplied.

Source frozen: SHA256 `03f19edccc38ff0718a400d1c948084ef16a5ac4063109a4828b2815ffc846da`.
No source edits after this freeze. This worker performs no Git mutations or shared-report/queue writes.

## References and baseline

Read the Lean and mathlib-quality skills, the full cleanup workflow, full golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, profiling, and the
declaration-relevant formatting, naming, comments, hypotheses, normal-form, and API style sections.
Mode A: dedicated single original declaration. File-wide preparation/fixes and final project gates
belong to the owner; source/header changes outside the assigned helper and routine callers are excluded.

Baseline live LSP: complete, unfiltered, success=true, partial=false, timed_out=false;
no errors or warnings on the original helper. Existing warnings elsewhere concern header metadata,
unused section/decidability/Fintype arguments, and unused hypotheses. They are preserved under scope.
Raw baseline response: `/private/tmp/roth-theta-map-intcast/baseline-lsp.json`.
The owner supplied an already-built checkpoint; this worker additionally built the edited module below.

## Full 24-item audit

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | No original-helper warning. Preserve unrelated baseline warnings. |
| 2 | HAVE SCAN | Original has no `have`. Three existing caller `have` bindings remain in their original roles; only right sides changed. |
| 3 | SET_OPTION | None in helper; no limits or options added to source. |
| 4 | SIMP SQUEEZE | No original `simp`; replacement is a direct term. |
| 5 | NAMING | Descriptive standard `map`/`intCast`/`real`/`ne_zero` naming; no forbidden numbered/abbreviated pattern. Deleted, no rename needed. |
| 6 | LINE PACKING | Measured every original signature line below. Final helper has zero signature lines; no retained underpacked signature. Added caller lines ≤99 codepoints. |
| 7 | BY PLACEMENT | Original term proof; replacement term proofs. No isolated `by`. |
| 8 | FORMAT | Two-space proof indentation, no blank proof lines introduced, no `haveI`/`letI`, no tactic chains introduced. |
| 9 | COMMENTS | No helper comments. All 42 existing source comment blocks/line comments preserved byte-for-byte in order. |
| 10 | DOCSTRING | Private helper has none. Every existing docstring preserved; module-doc additions excluded by explicit scope. |
| 11 | VISIBILITY | Private implementation wrapper deleted; no public visibility changes. |
| 12 | STRUCTURE | Original proof two body lines including lambda, no conjunction or long branch. Deleted; no helper extraction needed. |
| 13 | MATHLIB | Generic `map_ne_zero_iff` plus `MvPolynomial.map_injective` is sufficient; delete wrapper and use directly. Five methods below. |
| 14 | JUNK DEF | n/a: lemma, no data definition. |
| 15 | EXISTS LEMMA | n/a: no existential conclusion. |
| 16 | SHOW/CHANGE | Neither occurs in helper or replacement. |
| 17 | PUSH_NEG | None in helper or replacement. |
| 18 | GENERALISE | All three effective parameters probed, including compiled negative drops and generic positive forms below. No new API retained. |
| 19 | INEQUALITY | Zero ordered inequalities; `≠` is nonzeroness, not reversed order. Table below. |
| 20 | NORMAL-FORM | The canonical map-nonzero iff is already Mathlib's root `map_ne_zero_iff`; use its forward construction `.2`. |
| 21 | SYNTAX-GEN | Generic bundled map plus injectivity composes at each consumer; explicit real target needed only without an expected type. |
| 22 | IMPORT-FANOUT | No imports added. |
| 23 | CASTS | No coercion expression introduced. Three explicit `ℝ` target arguments to `Int.castRingHom` retained as elaboration-load-bearing. |
| 24 | INSTANCE-NAME | n/a: helper and replacements introduce no instances. |

Issues fixed: duplicated Mathlib wrapper removed. Refactoring deferred: none for this helper.

## Five actual Mathlib searches

Raw remote/native results: `/private/tmp/roth-theta-map-intcast/searches.json`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `MvPolynomial map preserves nonzero for injective ring homomorphism` | Found `MvPolynomial.map_injective`, support preservation, and univariate map nonzero iff. |
| B Loogle | `MvPolynomial.map, _ ≠ 0` | Returned algebraic divisibility result, no direct match. Bounded query completed. |
| C LeanSearch | `An injective coefficient ring homomorphism maps a nonzero multivariate polynomial to a nonzero polynomial` | Found `MvPolynomial.map_injective`/`map_injective_iff` and univariate `Polynomial.map_ne_zero_iff`. |
| D source `rg` | `map_eq_zero`, `map_ne_zero`, `map_injective` in MvPolynomial; full-name generic searches | Found `MvPolynomial.map_injective` in `Algebra/MvPolynomial/Eval.lean:396`; existing Theta callers already use generic `map_ne_zero_iff`. Root zero lemma is generated by `@[to_additive]` from `map_ne_one_iff` at `Algebra/Group/Hom/Defs.lean:253`. |
| E native local search | `MvPolynomial.map_ne_zero`; then `map_ne_zero_iff` | First index unavailable; second returned source matches but index=error. Neither is absence evidence. Compiled checks independently establish the exact generic root constant. |

Auxiliary variants examined: `map_eq_zero_iff`, `map_ne_zero_iff`, `map_injective_iff`,
`Polynomial.map_ne_zero_iff`, support preservation, and additive-generation route.
Common-equivalents table: no topology/finiteness bucket applies; this is the generic
zero-preserving injective-map API. No claim of absence is made.
Compiled native `lean_run_code` checked the root type and exact target application successfully.
The persistent independent `positive.lean` repeats those checks and compiles with exit 0.

Conclusion: Mathlib is more general. Delete local wrapper, specialize Mathlib at all seven uses.
Strict replacement rules: no new wrapper/predicate; all methods attempted; variants checked;
local helper deleted; Mathlib dependency documented here while protected module docs stay unchanged.

## Effective generalisation, drop tests, and inversion

Independent file `/private/tmp/roth-theta-map-intcast/positive.lean` copies the exact baseline
original statement and proof under `AuditMapIntCast.original_source`; it does not invoke the current
theorem or its replacement. `#print` confirms its proof value, and `#check @original_source` gives:

```lean
∀ {σ : Type u_1} {R : MvPolynomial σ ℤ},
  R ≠ 0 → (MvPolynomial.map (Int.castRingHom ℝ)) R ≠ 0
```

No Fintype/DecidableEq section instance is an effective original parameter: the fresh `{σ : Type*}`
shadows the file variable, and neither instance appears in the independently elaborated type.

| Effective parameter | Class/use | Actual compiled probes | Result |
|---|---|---|---|
| `{σ : Type*}` | Universe-polymorphic index type; determines polynomial variables | Remove binder under `autoImplicit=false`: `dropSigma`, negative. Positive `generic` retains arbitrary universe without any finiteness/decidability assumption. | Drop fails at line 13 with unknown σ; no finite or decidable assumption to weaken. Already universe-polymorphic. |
| `{R : MvPolynomial σ ℤ}` | Structure value whose nonzeroness is mapped | Remove binder under `autoImplicit=false`: `dropR`, negative. Positive `generic` replaces concrete coefficients by arbitrary commutative semirings and arbitrary injective coefficient homomorphism. | Drop fails at line 17 with unknown R. Generic formulation compiles; use existing Mathlib, retain no new lemma. |
| `(hR : R ≠ 0)` | Proposition needed to exclude zero | `dropHR` removes binder and replays term; `dropNonzero_counterexample` proves the claimed unconditional map-nonzero statement false by taking R=0. | Drop fails at line 22 with unknown hR; mathematical necessity independently certified by counterexample. |

Negative probes share one import and occupy distinct named source ranges in `negative.lean`;
exit 1 is expected and logged. Positive probes compile in a separate file with exit 0;
failed-probe declarations are never used for axiom certification.
No strict-to-weak order or pointwise localisation candidate applies to these parameters.
No bundled conjunction hypothesis to split. σ and R are dependent data, not disposable premises.

Concrete-to-abstract probes: `charZeroTarget` compiles over arbitrary `[CommRing K] [CharZero K]`;
`generic` compiles over arbitrary `[CommSemiring A] [CommSemiring B]`, an injective `f : A →+* B`,
and arbitrary MvPolynomial. This is a substantive generality gain supplied directly by Mathlib.
No public/generalized declaration is added and no old public hypotheses removed.

Literature: n/a, original is private; the public-literal literature requirement does not apply.
Inversion check: YES, the proof's mathematical work is injectivity plus preservation of zero,
not a property special to ℝ or integer polynomials. The generic Mathlib map theorem already supplies
the abstraction, so deleting the specialization is preferable to inventing a new abstract helper.

## Signature packing and inequality artifacts

Widths count Unicode codepoints, not bytes. Baseline signature ends at `:=`; lambda is proof text.
`#check @original_source` above is the independently compiled type reference (`format.width=100`).

| Original signature line | Chars | Next token | Arithmetic | Action |
|---|---|---|---|---|
| 64 | 88 | `map` (3) | 88 + 1 + 3 = 92 ≤100 | Original could begin next fragment here; entire declaration deleted rather than cosmetically repacked. |
| 65 through `:=` | 36 | no next signature token | n/a | Deleted. Complete conclusion fragment is 32 chars; 88+1+32=121. |

Final helper signature table: zero rows because the declaration is absent. No retained row needs
repacking. Public consumer signatures are byte-identical to the worker-start snapshot; this worker
does not apply the separate public-contract menu. Every newly added proof line has width ≤99.

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| none | Both original signature lines, all hypotheses, replacement | no `≥` or `>` ordered inequality | n/a | none; no `_ge_`/`_gt_` name |

## All 42 golfing rules

The Mathlib deletion takes precedence over retaining any shorter local proof. Actual automation
experiments are named independently in `automation.lean`; failures were not applied to source.

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: original is already a term. |
| 1.2 by rfl | n/a: no reflexivity proof. |
| 1.3 rw + exact | n/a: no tactic rewrite chain. |
| 1.4 simp + exact | n/a: no simp. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor | n/a: no conjunction. |
| 1.7 apply + exact | n/a: no tactic apply chain. |
| 1.8 by_contra | n/a: original direct lambda; replaced by canonical iff application. |
| 1.9 eta reduction | Original lambda consumes an equation, not an eta-redex; eliminated together with wrapper. |
| 1.10 single-use have | No helper have. Existing caller bindings are routine consumers, not newly extracted lemmas. |
| 1.11 apply + intro | n/a: no such chain. |
| 1.12 redundant show | n/a: none. |
| 1.13 have projections | n/a: no such chain. |
| 1.14 consecutive rw | n/a: none in original helper/replacement. |
| 1.15 terminal simp only | n/a: none. |
| 1.16 nonterminal simp | n/a: none. |
| 1.17 dot notation | `.2 hR` selects the constructive direction directly. |
| 1.18 trailing parentheses | Nested term arguments require their grouping; no `by`/lambda trailing-parenthesis opportunity. |
| 1.19 push_neg | n/a: none. |
| 1.20 trivial exists | n/a: no existential. |
| 2.1 grind | Plain `grind` tried, failed to derive injectivity; exact?/apply? separately find `grind hR`. Direct Mathlib composition retained at consumers. |
| 2.2 delete before grind | n/a: original has no grind. |
| 2.3 simpa | No simp-followed-by-close chain; canonical iff is clearer. Plain simp experiment leaves map-nonzero goal. |
| 2.4 fun_prop | n/a: algebraic nonzero proposition, no analytic function property. |
| 2.5 positivity | Tried; failed to prove nonzeroness. |
| 2.6 gcongr | n/a: no order/monotonicity goal. |
| 2.7 lia/omega | n/a: no linear Nat/Int arithmetic goal. |
| 2.8 aesop | Tried; failed at default depth 30. No depth raised. |
| 2.9 norm_num/norm_cast | n/a: not a concrete numeric computation or cast-equality goal. |
| 2.10 decide/kernel | n/a: arbitrary-polynomial nonzero implication, not a closed finite computation. |
| 2.11 field_simp/ring | n/a: no denominator identity. |
| 2.12 linear_combination | n/a: no ring-normalization conclusion with polynomial-equation hypotheses. |
| 2.13 wlog | n/a: no symmetric case branches. |
| 2.14 calc | n/a: no calc block. |
| 2.15 multiple goals | n/a: one nonzero goal. |
| 3.1 erw/rw | n/a: none. |
| 3.2 legacy fun tactics | n/a: none. |
| 3.3 omega/lia | n/a: no omega introduced or used in the helper/replacement. |
| 3.4 rcases rfl | n/a: no cases. |
| 3.5 attributes | n/a: deleted duplicate; no local simp/grind attribute added. |
| 3.6 simp_all | n/a: none. |
| 3.7 heartbeat option | None present or introduced; default limits preserved. |

Step-back reflection: exact? and apply? both suggest `exact grind hR` in the isolated experiment;
plain grind, simp, aesop, and positivity fail. The canonical explicit two-lemma composition removes
the duplicate and makes dependencies clear. No new API is warranted. This is a dependency cleanup,
not a claim that expanding seven uses reduces proof-token count.

## Verification and gates

`/Users/ramin/.elan/bin/lake build Roth.Theta` exited 0: `Build completed successfully (2423 jobs)`.
Raw log: `/private/tmp/roth-theta-map-intcast/module-build.log`.
Independent positive/type/value/axiom compile: `lake env lean positive.lean`, exit 0, 24.565s.
An initial scratch run used the nonexistent `pp.width` option; corrected to `format.width` and
reran cleanly. This was scratch-only; no source option was added.
Expected negative and automation experiments exit 1; their logs are exploratory, not success gates.

Built-consumer axioms, final live LSP, and after-prefix profile results are recorded in the final
verification supplement below. Owner final `lake build` and separate `lake build Roth.LeanEval`
remain owner gates; this report does not claim they were run by this worker.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | Exact module command above, exit 0, UTF-8 log retained. |
| definition_protected | PASS | No def/abbrev/import/instance lines changed. |
| theorem_statement_protected | PASS | Only original private Mathlib wrapper deleted (declared replacement action); all public signatures unchanged. |
| structure_gate | PASS | Target deleted, no retained body/conjunction/branch. No new helpers. |
| naming_gate | PASS | No forbidden original name pattern, no new name, no rename. |
| line_packing_gate | PASS (deleted declaration) | Both original signature lines measured; no remaining target signature; additions ≤99 chars. |
| inequality_orientation_gate | PASS | Complete zero-occurrence table above. |
| comments_preserved | PASS | 42/42 original comment blocks/lines identical in order. |
| new_identifier_verification | PASS | `map_ne_zero_iff`, `MvPolynomial.map_injective`, `Int.cast_injective` compiler-checked; generic root generation source found. |

Phase 5a: wrapper deletion with seven direct specializations, applied. Phase 5b: no renames;
no queue writes authorized or needed. No source TODO/FIXME, sorry, axiom, native_decide, raised
limits, profiling traces, or temporary scratch declarations introduced.

Simplify pass: PASS-THROUGH on the final diff. Native `/simplify` skill/tool is not available;
manual holistic review confirms reuse of existing generic API, no unnecessary new helper,
preserved comments, and only necessary target annotations. No extra edits.

Buzz baseline: exact source prefix lines 1–66 plus `end Roth`, no changed preceding context.
Command: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 before-prefix.lean`.
Raw log `before-profile.log`; exit 0. Original command 12.331ms, associated async proof 28.082ms,
async kernel 2.212ms (nested kernel node 2.192ms counted only once): 42.625ms total, below 1000ms.
No repeated borderline sample needed (<750ms). This is PREFIX-ONLY, not a whole-file sweep.
Whole-file late `index_le_lem6` profile failure was supplied by owner; no claim it has been repaired.

Original target: 3 lines → 0. Whole Theta: 982 → 981 lines (net −1; annotation wrapping adds 3).
No mathematical statement weakening. No open refactor or rename request for this helper.

## Eleven-step checklist

- [x] Step 1: reference documents read.
- [x] Step 2: complete 24-item audit recorded.
- [x] Step 2.5: five actual search methods, limitations, variants, and compiled match recorded.
- [x] Step 2.6: every effective parameter classified; negative drop and positive abstraction probes compiled.
- [x] Step 2.7: every original signature line measured; final target deleted.
- [x] Step 2.8: complete inequality occurrence table recorded.
- [x] Step 3: all 42 golf rules given concrete status.
- [x] Step 4: step-back reflection and actual exact?/apply? probes done.
- [x] Step 5a: final complete unfiltered live LSP passed; supplement below.
- [x] Step 5b: protection/content gates and actual module build recorded; owner project gates pending.
- [x] Step 6a: no rename required, no unauthorized queue/sidecar write.

## Final verification supplement

All requests and compiler processes started by this worker have completed. Source hash remains
`03f19edccc38ff0718a400d1c948084ef16a5ac4063109a4828b2815ffc846da`.

- Final native live LSP: complete and unfiltered, success=true, partial=false, timed_out=false,
  zero errors, 28 warnings. The warning severity/message multiset is identical to baseline;
  only source line numbers move. Raw response: `final-lsp.json` in the scratch directory above.
- Built actual-consumer check: `lake env lean actual-built-axioms.lean`, exit 0, 58.465s.
  All five distinct public consumers covering the seven use sites depend only on
  `[propext, Classical.choice, Quot.sound]`: `Roth.indexSet_bddAbove`, `Roth.Θ_le_card`,
  `Roth.Θ_unique_le`, `Roth.index_det_le` (two uses), `Roth.index_le_lem6` (two uses).
  The same successful check enumerates the actual imported environment programmatically and finds
  zero constants ending in `.Roth.map_intCast_real_ne_zero`. There is no retained target constant
  whose axioms could honestly be reported. Initial scratch spelling `matches` was a reserved token;
  renamed scratch variable and reran cleanly. No production source change was involved.
- Exact prior public type application recovery: `lake env lean exact-old-consumer-types.lean`,
  exit 0, 36.161s (initial application-only version).
  All five explicit old forall types recover the actual built constants, including original
  `[Fintype σ]`, `[DecidableEq σ]`, `[Unique σ]` where applicable, τ instances, and every positive
  hypothesis. Additionally, each expected forall type is independently elaborated and compared
  directly against `getConstInfo.type` using `Lean.Meta.isDefEq`; all five log
  `Exact original type matches`. This direct comparison does not apply a theorem and cannot hide
  missing implicit binders through inserted lambdas. The direct check asserts exactly one universe
  parameter and alpha-renames the actual parameter to the quoted type's `u_1`: the two τ constants
  inherit the raw name `u_2` from their later section. An initial comparison without alpha-renaming
  detected precisely that rigid universe-name difference; debug output is retained. No public
  binder/positivity change is applied. The final direct-check log is
  `exact-old-consumer-types-strong.log`, distinct from the initial application-only compile;
  this final direct-check command exited 0 and contains all five success messages and zero errors.
- Independent original proof/type/value and replacement composition: `positive.lean` exit 0.
  Both have exactly the standard three axioms. Generic root `map_ne_zero_iff` has no axioms;
  `MvPolynomial.map_injective` uses the standard three, and `Int.cast_injective` only `propext`.
- Original-only timing remains 42.625ms. The deleted target has no retained timing. An additional
  exact current source prefix through line 111 (`Θ_le_card`) compiled with the real profiler, exit 0,
  29.880s including import time. As consumer-only context: `indexSet_bddAbove` command 3.515ms +
  proof 54.553ms + async kernel 2.943ms =61.011ms; `Θ_le_card` command 4.692ms + proof 44.656ms +
  async kernel 3.360ms =52.708ms. Nested proof/kernel nodes are not counted again.
  This prefix is not a whole-file profile and says nothing about the known late profile failure.
- `git diff --check` passes for the source and report. Source delta is limited to the deleted helper
  and seven necessary routine proof-callers; no new declaration, public type, definition, instance,
  import, header change, or comment deletion. Reports modified concurrently by the owner are not
  part of this worker's edits.

Worker gate result: PASS. Owner's final sequential whole-project build and separate LeanEval build,
then commit/push, remain pending owner work. This worker has no further source-write authority.

## Owner frozen checkpoint gates

All leaf compiler/LSP sessions drained and source-write authority revoked before owner checks.
Frozen SHA256 `03f19edccc38ff0718a400d1c948084ef16a5ac4063109a4828b2815ffc846da` remained
identical through sequential `lake build` (exit0,125.449s) THEN separate `lake build Roth.LeanEval`
(exit0,34.928s). Raw logs `/private/tmp/roth-theta-d04-{full,leaneval}.log`; structured hashes and
exit codes `/private/tmp/roth-theta-d04-builds.json`. Exact-path staging, commit and successful
cleanup-branch push complete this checkpoint before the next original declaration edit.
Original audit count after successful publication: Theta4/35; overall185/264;9/14files complete.
No new helper or public contract amendment; whole-file performance remains explicitly pending.
