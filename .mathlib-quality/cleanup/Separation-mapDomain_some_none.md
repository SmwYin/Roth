# Cleanup: private `Roth.mapDomain_some_none`

Dedicated original-d1 worker at owner-supplied HEAD `a39317e`, branch `ramin-cleanup`. No Git mutations. Source ownership is limited to this helper and the four replacements needed by its removal, plus the owner's requested blank line between import groups. Baseline full project build and complete native LSP were supplied by the owner: exit 0 and 0 errors/32 warnings, respectively. Baseline source `/private/tmp/roth-separation-d01-before.lean`.

## References and initial full audit (before source edits)

Read lean4 and mathlib-quality SKILL.md, installed cleanup Phase 4 in full, full golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md and cleanup-gates.md; relevant style-rules and full profiling reference. No subdelegation.

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | No target diagnostic in owner's complete baseline; unused section instances already omitted. |
| 2 | HAVE SCAN | No have in two-line target; no intermediate to inline. |
| 3 | SET_OPTION | No scoped option or raised limit. |
| 4 | SIMP SQUEEZE | The sole `by simp` is terminal proof of `none ∉ range some`; retain unsqueezed. Caller at original L88 uses nonterminal simp only and must keep an explicit rewrite set. |
| 5 | NAMING | mapDomain_some_none accurately describes operation and evaluation, no forbidden abbreviation/pattern. No rename is necessary; removal supersedes naming. |
| 6 | LINE PACKING | Original signature is a single line; measured table below. |
| 7 | BY PLACEMENT | Term proof has an inline terminal `(by simp)`; no standalone by. |
| 8 | FORMAT | Two-space body, no empty interior lines, trailing spaces or haveI/letI. |
| 9 | COMMENTS | No target proof comments; all file block comments must remain byte-identical. |
| 10 | DOCSTRING | Private helper correctly has none. |
| 11 | VISIBILITY | Already private, exactly four local uses. No external API removal. |
| 12 | STRUCTURE | Two-line declaration, one-line proof, no conjunction or branch. Wrapper is removable. |
| 13 | MATHLIB | Existing Finsupp.mapDomain_of_notMem_range proves it immediately; embDomain_some_none gives another equivalent route. Actual five searches recorded below. Remove local wrapper and specialise mathlib at all four uses. |
| 14 | JUNK DEF | n/a: lemma, no definition. |
| 15 | EXISTS LEMMA | n/a: equality, no existential. |
| 16 | SHOW/CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Effective binders are universe-polymorphic τ and u; no Fintype, DecidableEq, R or CommSemiring in effective type. Generic AddCommMonoid coefficient variant independently compiles; existing mathlib already supplies it, so delete rather than add API. |
| 19 | INEQUALITY | Equality conclusion; no inequality occurrence or ge/gt name. |
| 20 | NORMAL-FORM | mapDomain evaluated outside range equals zero is standard simplifier form. |
| 21 | SYNTAX-GEN | Generic library lemma supports arbitrary maps, coefficient monoids and off-range points; direct specialisation avoids a redundant local API. |
| 22 | IMPORT-FANOUT | No new import. Owner requested only a blank line separating existing import groups. |
| 23 | CASTS | No coercions/ascriptions in target or proposed replacement. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues to fix: delete the private one-call wrapper and replace its four uses; add requested import separator. No public signature/doc/definition changes, rename queue, extraction or decomposition flag.

## Inequality scan

| Location | Original | Rewrite | Rename |
|---|---|---|---|
| Whole original signature and hypotheses | n/a: no ≥ or > occurrence | none | none |

## Generalisation status: every effective binder

| Binder | Class | Use and mechanical candidate | Result |
|---|---|---|---|
| `{τ : Type*}` | type variable | Domain of finitely supported function; already universe-polymorphic. Dropping leaves unknown τ under autoImplicit false. Sort generalisation cannot be the domain of Finsupp. | Retain original domain. |
| `(u : τ →₀ ℕ)` | structure value | Subject of mapDomain evaluation; dropping leaves unknown u. Generalise ℕ to `[AddCommMonoid M]`. | Generic candidate compiles independently; already existing generic library API, no new helper. |
| `[Fintype τ]`, `[DecidableEq τ]` | omitted section instances | Both already omitted and absent from effective type. | No further drop needed. |
| `{R}`, `[CommSemiring R]` | unused section variables | Neither appears in effective type (independently checked original only binds τ/u). | No target hypothesis to weaken. |

Point localisation, strict-to-weak and bundled proposition decomposition do not apply: no proposition assumptions. Inversion check finds exactly the existing generic off-range theorem. Literature search n/a: private declaration. No public restatement proposed.

## Result and frozen ownership

Deleted the private wrapper and its scoped omit, replaced exactly its four local uses with direct mathlib API, and inserted the owner's import separator. Three terminal calls are `simp [Finsupp.mapDomain_of_notMem_range]`. The existing nonterminal call is now:

```lean
      simp only [Finsupp.mapDomain_of_notMem_range (f := some) _ none (by simp), Finsupp.tsub_apply,
        Finsupp.single_eq_same] at this
```

The latter replacement retains an explicit simp set. Its off-range proof needs `f := some` and `none` fixed before elaborating `by simp`; the underconstrained `_ _ (by simp)` experiment failed and was discarded. No other proof strategy was changed. In particular the caller's existing omega remains for its own dedicated worker. Existing public signatures, definitions and all block comments are unchanged. No replacement helper or extra import was introduced. Four repeated applications are legitimate library uses; retaining a local one-call wrapper would duplicate the generic API. Final file is 616 lines versus 618 originally, including the extra import separator and extra wrapped call-site line.

Source authority was explicitly released to the file owner after every Lean request and compiler process completed. Frozen SHA256: `8de29f33439259fa33927a72c7411dbd40ff2a3afacfeb97d8ea4a14bf0f3646`. All subsequent worker activity is report-only. Owner performs independent full-project and LeanEval gates, then exact-path commit/push before the next declaration worker.

## Line packing

Independent width-100 `#check @D01.original` printed:

```lean
@original : ∀ {τ : Type u_2} (u : τ →₀ ℕ), (Finsupp.mapDomain some u) none = 0
```

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| Original L49 | 79 | none: L50 is proof body after := | n/a: no second signature line | ok |
| Final target | n/a: declaration deleted | none | n/a | ok |

All original binders and conclusion fit on one signature line. Proof body L50 was 49 codepoints. Changed caller lines measure 52, 42, 100 and 42 codepoints; the wrapped continuation is within 100. No public/caller signature was changed or repacked in this worker's scope.

## Five actual mathlib search methods

Tool names and full schemas were discovered through ALL_TOOLS; native calls were used. Raw JSON for each request is saved under `/private/tmp/roth-separation-d01-{finder,loogle,search,local}.json`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `Finsupp mapDomain Option.some evaluated at none equals zero` | Finsupp.embDomain_some_none, some_single_none, optionElim_apply_none, some, optionElim. |
| B Loogle | `"mapDomain", "range"` | Finsupp.mapDomain_of_notMem_range, deprecated alias mapDomain_notin_range, mem_range_of_mapDomain_ne_zero, mem_range_mapDomain_iff and comapDomain variants. |
| C LeanSearch | `A finitely supported function mapped along Option.some is zero at none` | Finsupp.embDomain_some_none and restriction/optionElim results. |
| D Source | `mapDomain_some`, `mapDomain.*none`, `mapDomain_of_notMem_range`, `mapDomain_notin_range` in Mathlib/Data/Finsupp; then `embDomain_eq_mapDomain`, `embDomain_some_none` | Basic:286 is exact generic off-range theorem; Option:92 is embDomain specialisation; Basic:422 relates embDomain and mapDomain. No truncated absence claim. |
| E Name pattern | native local search `mapDomain`, limit40 | Found generic mapDomain family and target; index unavailable, so these source-fallback hits establish presence only. No empty-result absence inference. |

Auxiliary variants: `mapDomain_of_not_mem_image_support` (apply? suggestion), `mem_range_of_mapDomain_ne_zero`, `embDomain_eq_mapDomain`, `embDomain_some_none`, and deprecated `mapDomain_notin_range` (not used). Common-equivalents table: no matching specialised bucket; generic domain-extension API supplies the result directly. Conclusion: found in mathlib in more general form as `Finsupp.mapDomain_of_notMem_range`; delete local wrapper and specialise existing API at four uses. No absence claim or proposed new API.

## All 42 golfing rules

The first native multi_attempt targeted a term-proof position but supplied tactic text without `by`, producing unknown-identifier errors. Those are invalid probes and are not claimed as automation failures. Correct independent native run_code probes imported Mathlib.Algebra.MvPolynomial.Polynomial without importing Roth.Separation. Bare grind, simp and aesop failed; exact? could not close. apply? returned suggestions including the generic off-range theorem but left subgoals and emitted a sorry warning in the discarded scratch snippet: its success flag is not a proof-completion certificate. The original term, generic coefficient term, and simp-with-library-term independently compiled with no sorry. Raw corrected tactic results are `/private/tmp/roth-separation-d01-tactic-{grind,simp,aesop,exact,apply}.json`.

| Rule | Concrete status |
|---|---|
| 1.1 by exact | n/a: already direct term, no by-exact wrapper. |
| 1.2 by rfl | n/a: no rfl proof. |
| 1.3 rw + exact | n/a: no rw/closing-exact sequence. |
| 1.4 simp + exact | n/a: sole simp closes the range subgoal. |
| 1.5 trailing rfl | n/a: no trailing rfl. |
| 1.6 constructor pairs | n/a: equality, no constructor block. |
| 1.7 apply + exact | n/a: existing proof directly applies library theorem. |
| 1.8 by_contra + push_neg | n/a: no contradiction block. |
| 1.9 eta reduction | n/a: no lambda in target. |
| 1.10 inline have | n/a: no have. |
| 1.11 apply + intro | n/a: neither tactic. |
| 1.12 redundant show | n/a: no show. |
| 1.13 have + projections | n/a: no have or projections. |
| 1.14 merge rw | n/a: no rewrites. |
| 1.15 unsqueeze terminal simp only | n/a: target's terminal simp already unsqueezed; caller's simp only is nonterminal and preserved as such. |
| 1.16 squeeze nonterminal simp | n/a in target; replacement nonterminal caller retains simp only. |
| 1.17 dot notation | n/a: no appropriate receiver form; library API application retained at callers. |
| 1.18 avoid trailing parentheses | Original `(by simp)` could become `<| by simp`, but deleting wrapper makes cosmetic churn moot. Caller simp list needs parenthesised tactic argument. |
| 1.19 push_neg migration | n/a: none. |
| 1.20 existential helper | n/a: no existential. Generic wrapper removal is separately applied. |
| 2.1 grind | Actually tried in correct independent tactic context; failed on opaque mapDomain evaluation. |
| 2.2 delete before grind | n/a: no grind-containing sequence. |
| 2.3 simpa consolidation | n/a: no simp-followed-by-tactic chain. `simp [Finsupp.mapDomain_of_notMem_range]` independently closes, used at terminal callers. |
| 2.4 fun_prop | n/a: no continuity, differentiability or measurability property. |
| 2.5 positivity | n/a: conclusion is equality, no positive/nonnegative/nonzero goal. |
| 2.6 gcongr | n/a: no monotonicity comparison. |
| 2.7 lia/omega | n/a: target requires domain-support API, no arithmetic hypotheses. Existing caller omega left to caller worker. |
| 2.8 aesop | Actually tried independently; made no progress. |
| 2.9 norm_num/norm_cast | n/a: no numerical computation/cast. |
| 2.10 decide/kernel | n/a: arbitrary Finsupp value is not finite closed computation. |
| 2.11 field_simp/ring | n/a: no denominators or ring identity. |
| 2.12 linear_combination | n/a: target has no ring/ring_nf or algebraic hypotheses. |
| 2.13 wlog | n/a: no symmetric case branches. |
| 2.14 collapse calc | n/a: no calc. |
| 2.15 close parallel goals | n/a: no repeated subgoals. |
| 3.1 erw to rw | n/a: no erw. |
| 3.2 analytic tactics | n/a: none. |
| 3.3 omega to lia | n/a in target; caller arithmetic is outside this replacement-only scope. |
| 3.4 rcases rfl | n/a: no rcases or substitution. |
| 3.5 automation attributes | Existing library simp support is sufficient when explicitly supplied; no new attribute/global simp registration. |
| 3.6 simp_all | n/a: no simp_all. |
| 3.7 heartbeat options | n/a: none existed, none added. |

Step-back reflection: an abstract off-range theorem already expresses the precise reason. Three callers simply supply it to terminal simp; the fourth needs a specialised equality in its deliberate nonterminal rewrite list. This is more general library reuse and removes one local declaration without introducing a custom predicate or wrapper. Alternative embDomain route would add a representation conversion at callers, so the existing mapDomain API is clearer. No significant extraction opportunity or deferred decomposition remains.

## Verification and trust

- Actual `lake build Roth.Separation` completed exit0 (session25817), 1876 jobs: `/private/tmp/roth-separation-d01-module.log`. This is a module build, not a whole-project success claim.
- Final complete native unfiltered diagnostics: success=true, partial=false, timed_out=false, failed_dependencies=[]; 0errors and exactly32 existing warnings. Raw `/private/tmp/roth-separation-d01-lsp.json`. No new target/call-site errors or warnings.
- Native independent exact original type and proof, under namespace D01 and importing only Mathlib.Algebra.MvPolynomial.Polynomial, compiled successfully. Original theorem is not imported or referenced. `#print axioms D01.original` returned only propext, Classical.choice and Quot.sound; raw `/private/tmp/roth-separation-d01-independent.json`.
- The same independent request compiled the generic `[AddCommMonoid M]` coefficient version and the terminal simp replacement. `/private/tmp/roth-separation-d01-nonterminal.json` separately checks the exact specialised nonterminal replacement in a faithful congrArg/tsub context.
- Actual retained constants were located in the freshly built imported environment, including numeric private-name components, then passed to Lean.collectAxioms: mapDomain_add_single_none, coeff_X_none_pow_mul_rename, degreeOf_none_rename_some, and public eq_mapDomain_some_add_single. All four have only `[propext, Classical.choice, Quot.sound]`. Raw `/private/tmp/roth-separation-d01-retained-axioms.json`. An initial literal private-name syntax probe and a quoted-numeric-component retry failed; those discarded raw files do not constitute the final axiom check. Environment lookup avoids confusing a string `0` component with Lean's numeric component. One long-line warning belongs only to the discarded/scratch diagnostic code, not repository source.
- Automated snapshot comparison checked that all block comments match byte-for-byte and no target name remains; focused diff contains only import separation, target deletion and four use substitutions. Changed source lines are at most100 codepoints; no definition/public-signature change, sorry, axiom, native_decide, limit raise or profiling scaffolding.
- Binder-drop rows above report syntactic necessity rather than claiming negative compilation tests: τ and u occur explicitly in dependent types/terms, and no proposition hypotheses exist. Actual positive checks certify the exact original effective type and the stronger generic coefficient result; no untested candidate is labelled compilation-verified.

## Gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module build exit0, raw log above |
| definition_protected | pass | no def/abbrev change |
| theorem_statement_protected | pass, authorised private removal | only target private signature removed; all public and retained private signatures unchanged |
| structure_gate | pass | trivial wrapper deleted; no added branch/helper |
| naming_gate | pass | original descriptive mathematical name, no forbidden pattern; deleted rather than renamed |
| line_packing_gate | pass | full original signature width79, single line; no target remains; changed caller max100 |
| inequality_orientation_gate | pass | zero inequalities in target type/hypotheses |
| comments/docs | pass | all block comments byte-identical, target had no comments |
| trust/limits/scaffolding | pass | standard axioms; no limit/axiom/sorry/debug changes |
| external/full project/LeanEval | owner gate | owner will run sequential cumulative gates after freeze |

## Simplify pass

No builtin simplify skill/tool is exposed in this worker session. Equivalent scoped holistic review performed directly and disclosed: checked duplicate API, statement applicability, call-site simplicity, representation choices and imports. Outcome: wrapper removed using generic off-range API; no further changes recommended within this target scope. No suggestion silently left unfinished.

## Buzz pass: budget1000ms

Actual original source profile command completed exit0 (session62603):

```text
lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Raw `/private/tmp/roth-separation-d01-before-profile.log`. The trace explicitly anchors the target's command and actual private constant, rather than attributing an aggregate category to it. Target outer Elab.command25.436ms, proof Elab.async77.566ms (inner value76.400ms is nested and not added again); conservative command-plus-proof103.002ms. Below750ms, so no borderline resweep required. A second syntax-expansion Elab.command24.812ms node is not added again. Removed target has no final elaboration cost. No claim that global total fell by this precise amount.

Final actual profiled module command completed exit0 (session65906):

```text
lake env lean -Dprofiler=true -Dprofiler.threshold=0 Roth/Separation.lean
```

Raw `/private/tmp/roth-separation-d01-final-profile.log`. This validates the final module under profiling; its aggregate/unanchored categories are not used as per-target timings. The target is deleted, so no fabricated final target time or retained-target bottleneck is reported. No slow surviving target, limit increase, decomposition deferral or source profiler wrapper. FAST-BOARD for original target, final target removed.

## Eleven-step completion checklist

- [x] 1: references read before source edit.
- [x] 2: all24 audit items, initial report written before source edits.
- [x] 2.5: all five actual searches, variants and generic library presence established.
- [x] 2.6: every effective binder, omitted section instances, generality/inversion and private literature exemption.
- [x] 2.7: every original signature line measured; actual width100 check.
- [x] 2.8: zero-occurrence inequality table.
- [x] 3: all42 golfing rules with concrete status and corrected actual automation tests.
- [x] 4: step-back reflection and alternative representation route.
- [x] 5a: complete native unfiltered diagnostics, raw retained.
- [x] 5b: actual module build, protected source/diff checks, independent original proof, actual retained-private axiom checks.
- [x] 6a: no rename necessary, no queue mutation.

Refactoring flags: none. Renames: none. Source frozen; all ownership revoked and returned to owner; subsequent worker activity report-only.

## Owner cumulative publication gates

Source freeze unchanged. Owner73355exit0 independently compiles the whole ORIGINAL30 proof bodies in a separate namespace;all20 original public type/value recoveries rfl and ALL29 actual retained axiom sets standard-only. Owner39911 sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,127.65s/32.76s;both before/after hashes equal the frozen SHA above. Logs `/private/tmp/roth-separation-d01-compatibility.log`, `...-full.log`, `...-leaneval.log`, `...-builds.json`. Original block docs byte-identical; exact diff checked. Publication consists of the exact-path commit and successful push on ramin-cleanup before the next declaration.
