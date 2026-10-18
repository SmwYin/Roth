# Approved instance revisit: Roth.coeff_rename_mul_aeval

Initial audit written before source edits at HEAD 36737b0. Ownership: this theorem and this report only. User explicitly approved omitting Fintype τ and DecidableEq τ; all other public contracts, original documentation and both retained wrappers are protected. No source helper planned.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md, plus Lean skill and relevant style/naming/profiling references. Original audit is contextual evidence, not substituted for fresh checks.

## Initial 24-item audit

1. Lint: original target carries unused section/type instance warnings; complete fresh native diagnostics pending, no suppression.
2. Have: h is one hom equality with substantive ext/simp proof; used once, not an eligible no-by single-use alias.
3. Options: none in declaration.
4. Simp: single terminal simp in hom ext; retain unsqueezed.
5. Naming: coeff_rename_mul_aeval describes coefficient, renaming, multiplication and evaluation; snake_case, no forbidden numeric/abbreviation pattern.
6. Width: three signature lines retained, fresh measured table below.
7. By: end of preceding line.
8. Format: two-space tactics, seven proof lines, no empty lines or inline instances.
9. Comments: no inline proof comments; original source docstring preserved byte-for-byte.
10. Documentation: explains disjoint-variable factorisation and primary source.
11. Visibility: public theorem and caller contract retained by explicit instruction.
12. Structure: seven body lines, no conjunction or branches; no extraction needed.
13. Mathlib: fresh Finder, Loogle, LeanSearch, source search, local index and live automation checks; record outcomes below. Coefficient-polynomial API remains appropriate.
14. Junk definition: n/a, theorem.
15. Exists helper: n/a, no existential conclusion.
16. Show: term show folds hom application to match rw; no tactic-mode show.
17. Push_neg: none.
18. Generalise: approved removal of both variable instances. Every remaining effective binder gets fresh compiler drop tests; no other API widening authorized.
19. Inequalities: no occurrence in effective statement or hypotheses.
20. Normal form: coefficient equality uses standard polynomial APIs; no custom predicate.
21. Syntax: current a,b coefficient interface rewrites directly in exists_int_factors; tensor presentation would add constructions.
22. Import fanout: no new import required.
23. Casts: X none ambient type fixes variable/coefficient type; typed hom application supports matching. No new casts proposed.
24. Instance name: n/a, no instance declaration.

Issues to fix: prepend scoped omit before the original docstring; add local classical only if actual compilation requires it. Refactoring needed: none beyond explicit approved instance omission. No pending public proposal from this task.

## Fresh search and literature

Five actual methods: native Lean Finder returned coeff_mul, coeff_X_mul', coeff_mul_X, coeff_mul_X', coeff_monomial_mul'; Loogle returned optionEquivLeft and degree/support/generator lemmas; LeanSearch returned coefficient convolution and variable lemmas; source rg found optionEquivLeft_coeff_coeff, aeval_algHom_apply, aeval_X_left_eq_map and coeff_C_mul; native local search returned 26 optionEquivLeft names with index warming. These are compositional matches, not an established exact duplicate. Raw fresh results: `/private/tmp/roth-separation-r05-{finder,loogle,leansearch,local}.json` and `/private/tmp/roth-separation-r05-source-search.log`. Auxiliary coefficient/none/some forms were included in the source search. Common-equivalents table has no relevant finite/discrete/order case. No custom predicate or duplicate definition introduced. Neither preserved public wrapper is reconsidered for deletion.

Fresh live multi-attempt tried grind, simp, aesop, exact?, apply? on the whole goal: none closed it; replacing the opening line of multiline have also left an unrelated trial parse error. This is not a module diagnostic. A fresh isolated native lean_run_code imported only Mathlib.Algebra.MvPolynomial.Polynomial and tested exact? on the full arbitrary-τ goal: success false, timed_out false, exact? could not close. Full result `/private/tmp/roth-separation-r05-exact-search.json`; no absence inferred from failed automation alone.

Actual public literature search query: polynomial ring disjoint sets variables coefficient product arbitrary ring. Opened primary university lecture notes by Jack Jeffries, Math 817 (Fall 2025), https://jack-jeffries.github.io/F25/817text.html, §8.1, lines 2751–2753: multiplication is coefficient convolution and arbitrary variable sets use finitely many variables in each polynomial. This supports arbitrary variable types conceptually; the semiring generality is established by the compiler, not inferred from ring-only prose. Local primary reference clean.tex's disjoint-variable coefficient argument is unchanged. Tensor/product-variable reformulation is mathematically natural but offers no simpler coefficient rewrite to callers. ChatGPT mathematical MCP is unavailable in the exposed tool metadata. No further public restatement proposed.

## Signature width and inequalities

Scoped omit is before the original docstring. Original signature text and proof text are byte-identical. format.width 100 #check is in the independent log.

| Source line | Codepoints | Next complete syntactic unit | Arithmetic | Verdict |
|---|---:|---|---|---|
| 117 | 95 | full coefficient expression (79) | 95 + 1 + 79 = 175 | required break |
| 118 | 83 | exponent argument (42) | 83 + 1 + 42 = 126 | required break |
| 119 | 80 | end of signature | n/a | packed |

| Occurrence | Scope | Action |
|---|---|---|
| none | complete effective type and every hypothesis | no inequalities to orient or rename |

## All 42 golfing rules, freshly inspected

| Rule | Status |
|---|---|
| 1.1 | no by-exact wrapper |
| 1.2 | no by-rfl wrapper |
| 1.3 | final rw closes, no rw/exact |
| 1.4 | simp is terminal, no simp/exact chain |
| 1.5 | no trailing rfl |
| 1.6 | no constructor goal |
| 1.7 | no apply/exact chain |
| 1.8 | no contradiction split |
| 1.9 | no eta lambda |
| 1.10 | h has substantive by/ext/simp proof, not a no-by alias |
| 1.11 | no apply/intro chain |
| 1.12 | term show supplies folded hom-application equality for rewrite; no redundant tactic show |
| 1.13 | no projection have |
| 1.14 | one consecutive rw block already merged |
| 1.15 | single terminal simp remains unsqueezed |
| 1.16 | no nonterminal bare simp |
| 1.17 | toAlgHom.comp uses dot notation |
| 1.18 | no eligible trailing proof/lambda parentheses; show is rw-list element |
| 1.19 | no push_neg |
| 1.20 | no existential helper |
| 2.1 | fresh native whole-goal grind failed |
| 2.2 | no grind in retained proof |
| 2.3 | no simp-followed-closing chain to consolidate |
| 2.4 | no function regularity predicate |
| 2.5 | no positivity/nonzero goal |
| 2.6 | no inequalities or monotonicity |
| 2.7 | exponents index coefficients; no arithmetic proposition |
| 2.8 | fresh native aesop failed |
| 2.9 | no concrete computation/cast normalization |
| 2.10 | arbitrary coefficient equality not finite decidable computation |
| 2.11 | no field/denominator |
| 2.12 | no ring/ring_nf or additive equation hypotheses |
| 2.13 | no symmetric branches |
| 2.14 | no calc |
| 2.15 | ext yields uniform single-variable goal, no repeated branches |
| 3.1 | no erw |
| 3.2 | no continuity/measurability |
| 3.3 | no omega or arithmetic goal |
| 3.4 | no rcases |
| 3.5 | coefficient theorem is explicitly rewritten by callers; no attribute required |
| 3.6 | no simp_all only |
| 3.7 | no local limits or profiler scaffolding |

## Step-back / simplify review

The retained proof already moves to a polynomial in the distinguished variable and multiplies by a constant polynomial. This directly reflects disjoint-variable coefficient factorisation; general automation offers no simpler proof. Removing the two approved instances requires no proof adjustment and no local classical command because the bridge now has matching generality. h is a substantive hom extensionality fact; inlining would obscure the expected equality used by rw. No helper, import, cast, attribute, definition or caller edit is needed. Casts: 0 introduced/dropped; existing ambient X-none ascription and typed hom equality remain load-bearing. No holistic simplification defect identified.

## Effective binders and generalisation

Fresh actual compiler probes: `/private/tmp/roth-separation-r05-probe-CASE.lean` and `.log`. All non-instance drops use autoImplicit false. The independent proof calls coeff_coeffNone and Mathlib, never the target theorem.

| Effective binder | Candidate | Compiler result |
|---|---|---|
| τ : Type* | remove type binder | drop-tau exit 1, unknown τ |
| Fintype τ | omit with DecidableEq retained | fintype exit 0; approved omission |
| DecidableEq τ | omit with Fintype retained | decidable exit 0; approved omission |
| both variable instances | arbitrary τ | independent exit 0; new exact type assignment exit 0 |
| R : Type* | remove | drop-R exit 1, unknown R |
| CommSemiring R | remove / Semiring / NonUnitalCommSemiring | actual failures detailed below |
| U | remove | drop-U exit 1, unknown U |
| V | remove | drop-V exit 1, unknown V |
| a | remove | drop-a exit 1, unknown a |
| b | remove | drop-b exit 1, unknown b |

No field, subtraction, domain, nonzero, proposition bundle, or global regularity assumption exists. Point-localisation: already at a,b. Strict-to-weak: no inequalities. Universe weakening: τ,R already independent Type*. Inversion check: no concrete named witness, fully parametric polynomials; natural exponents are intrinsic to Polynomial/MvPolynomial and changing them changes the objects. No further public API proposal.

## Verification and gate evidence

Baseline is parent's clean pushed 36737b0 with cumulative gates. Actual-module baseline r04 applies to this unchanged target: command 27.463 ms + async proof 156.638 ms = 184.101 ms, anchors 1/1.

Actual lake build Roth.Separation exited 0, 1876 jobs; `/private/tmp/roth-separation-r05-build.log`. Complete unfiltered native module LSP `/private/tmp/roth-separation-r05-final-lsp.json`: success true, partial false, timed_out false, failed_dependencies [], 0 errors / 20 warnings. Compared with r04's 22 warnings, all three target warnings disappeared; the only new warning is automatically included Fintype/DecidableEq unused in exists_int_factors. That later public contract stays protected and untouched. No suppression.

Independent `/private/tmp/roth-separation-r05-independent.lean` and `.log` exited 0, including width-100 #check, exact arbitrary-τ assignment, explicit original-class-argument adapter, independent nonself proof, actual built target/bridge/exists_int_factors and independent axiom checks. Each axiom list is exactly propext, Classical.choice, Quot.sound. No private constant changed or added.

Diff arithmetic: 577 to 578 source lines, 25 to 25 retained declarations, +1/-0 source line, exactly scoped omit. Other source bytes and original docstring/signature/proof are preserved. No helper, option, sorry, custom axiom, native_decide, haveI/letI, or source profiler material added.

Fresh binder suite completed with eleven actual return codes in `/private/tmp/roth-separation-r05-probes-summary.log`: Fintype-only and DecidableEq-only drops exit 0; all seven binder/class removals and both Semiring/NonUnitalCommSemiring weakenings exit 1. Semiring and nonunital diagnostics explicitly fail CommSemiring synthesis at MvPolynomial/evaluation operations. Initial probes launched before the module build finished could not import its olean; those attempts are not success evidence. The final complete rerun uses the built current module and qualified Roth bridge names.

External caller search finds exists_int_factors in this module and index_det_le in Roth/Theta.lean (two applications). Actual lake build Roth.Theta exited 0, 2423 jobs, raw `/private/tmp/roth-separation-r05-callers-build.log`. Complete unfiltered native Theta diagnostics `/private/tmp/roth-separation-r05-theta-lsp.json`: success true, partial false, timed_out false, failed_dependencies [], 0 errors / 28 warnings, matching supplied baseline. Theta source and public contract untouched.

## Eleven completion steps

1. Read required references and original evidence; fresh scoped ownership established.
2. Record complete initial 24-item audit before source mutation.
3. Run five actual searches, source equivalents and generic exact? probe; preserve wrappers.
4. Probe every effective binder and weaker algebra classes; apply only two approved omissions.
5. Check width-100 signature arithmetic and all inequality occurrences.
6. Inspect all 42 golfing rules, attempt automation, retain direct coefficient proof.
7. Step-back and holistic simplify review; no new source helper.
8. Actual module and caller builds; complete unfiltered native diagnostics.
9. Compile independent new-type proof and explicit original-class adapter; actual standard axioms.
10. Final repository profile after other jobs drain, plus diff arithmetic and gates.
11. Drain profile, record SHA256, revoke all source ownership; parent handles cumulative original/public checks, sequential project and separate LeanEval builds, exact-path commit and push before next declaration.

Actual built external caller axiom check `/private/tmp/roth-separation-r05-caller-axioms.lean` and `.log` exited 0: Roth.index_det_le uses exactly propext, Classical.choice, Quot.sound.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual Roth.Separation and Roth.Theta builds exit 0 |
| definition_protected | pass | no definition/abbreviation changed |
| theorem_statement_protected | pass, approved refactor | only scoped class omission; original-class adapter compiles |
| naming_gate | pass | descriptive mathematical operations, no forbidden patterns |
| structure_gate | pass | seven unchanged proof body lines; no conjunction/branches |
| line_packing_gate | pass | all three signature rows measured above |
| inequality_orientation_gate | pass | no inequalities in effective signature |
| source_scaffolding | pass | no prohibited options, axioms or tactic scaffolding introduced |
| cumulative_no_unintended_external_breakage | pass for affected direct callers | actual module/caller builds, complete native LSP; full project gates belong to parent |
| diff_check | pass | git diff --check exit 0; byte comparison confirms exactly one added omit line |

No source helper, pending public approval, rename, decomposition or other API proposal. Broader Domain and Nat choices remain exactly as dispatched.

## Final actual-module profile and freeze

After every compiler, binder suite and native MCP request had drained, the actual repository command `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean` exited 0. Raw full trace `/private/tmp/roth-separation-r05-profile.log`; anchored parser output `/private/tmp/roth-separation-r05-profile.log.json`. Target conservative outer command 31.048 ms plus outer async proof 152.492 ms = **183.540 ms** (2 command anchors from scoped command/declaration, 1 proof anchor; max command used, nested nodes not summed). Supplied unchanged baseline 184.101 ms. Both are comfortably below 750 ms repeat threshold and 1000 ms budget. No repeat/fix required and no whole-project performance claim.

All requests, including final profiler session, have completed. Source SHA256: `9893814b3228a24b031753f740a8755c7feabd522791ab5563fe74b09c2e0b01`. I explicitly revoke ALL source ownership and become report-only. No source edit after this freeze. Parent owns cumulative compatibility, sequential full project and separate LeanEval gates, exact-path commit and successful push before any next declaration edit.

## Owner cumulative publication gates

Source FROZEN SHA256 `9893814b3228a24b031753f740a8755c7feabd522791ab5563fe74b09c2e0b01`; leaf ownership revoked and requests drained before owner gates. Owner probe `60429` exit0,42.21s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r05-compatibility.{lean,log,json}`. Owner build session `21232` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,79.22s/28.12s; source hash stable. `/private/tmp/roth-separation-r05-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
