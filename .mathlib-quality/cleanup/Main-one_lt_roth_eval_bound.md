# Cleanup: `Roth.one_lt_roth_eval_bound_aux`

Locally accepted helper work; the parent resumes under its original worker and is audited separately. This report grants no parent audit credit or original-declaration count and authorizes no standalone publication. Only this helper was changed; its immediate ordinary comment and both original proof comments were preserved. The two preceding accepted helpers and their reports remain byte-identical.

## Genuine baseline and outcome

The genuine first ungolfed helper was saved before any helper Lean or golf in `/private/tmp/roth-main-integral-roth/helper-polynomial-FIRSTUNGOLFED.lean`, SHA `3fce52537d382083b458dca1a315bb0d133a1132a52f136cf8d7b195ff545697`. Entry source SHA `c4c1c2938431231208eafbf45003d3bb282b0d80d4dc3349f8825d5b31033136`. Genuine 34 declaration / 20 body lines became **25 / 15**. Signature tokens are identical, including every hypothesis, binder order and conclusion. Final source SHA `9ea17c21e76ee58e3fd597626ea87ab749808007a1d2d30dc697d4c27c3c0b36`; target SHA `bd3675663468617901ae73fcd713c6df17dae5aaa229c9d681157fcf71d31601`.

The helper eliminates the integer multivariate polynomial from the main lemma. Its real degree/index bounds give a strict Taylor estimate; its nonzero rational evaluation gives the denominator-product lower estimate. Combining them produces the numerical product greater than one needed by the parent. This is one substantive mathematical stage, not a tuple or a thin library wrapper. No forced extraction was necessary at 20 original body lines.

Removed the unused mapped-polynomial nonzero proof and ignored its unused `hQ0` projection. Inlined the one-use index bound, upper/lower bounds and product positivity proof. Replaced explicit exponential conversion with the verified `Real.rpow_le_iff_le_log` API. Standardized lambda arrows and packed the complete signature. The degree-map shortcut was boundedly investigated: the relevant API is multiset `degrees_map_le`, not univariate `Polynomial.degree_map_le`; attempted count composition encountered decidability/elaboration mismatches and was reverted. The original injective-support degree transport remains intact. No new imported identifiers remain unverified: the retained rpow API was verified in source and actual compilation.

## Full substantive audit

The complete 24-item initial audit, every-binder table, HAVE scan, five-method search status, normal-form/syntactic-generality/cast review and private-literature qualification are in `/private/tmp/roth-main-roth-eval-bound/initial-audit.md`. The full 42-rule status, all 10 signature-line codepoint measurements, inequality scan and manual holistic review are in `/private/tmp/roth-main-roth-eval-bound/audit-and-golf.md` (included below). No hypothesis weakening was applied: every parameter remains necessary for the selected API/type dependencies. Unsupported drops were reviewed mathematically/by dependency, not falsely labeled as compiled weakening tests. No ambient generalization or public-contract restatement is proposed.

Five methods: LeanFinder found `degrees_map_le`; Loogle queried degreeOf/map (no result); LeanSearch found log/rpow APIs; source search verified these and the injective degree/support alternatives; local name search was warming, so its empty/nonmatching results are not absence evidence. Auxiliary variants and common-equivalent table were considered. Whole-target `grind`, `exact?` and `apply?` did not replace this stage; degree-subgoal automation also failed. The LSP replacement probes retained trailing original code, so their extra trailing-code/no-goals diagnostics are qualified rather than represented as successful full proofs. No search-only absence claim is made.

The built-in `/simplify` skill is unavailable. A substantive manual holistic review was performed; this was **not an actual `/simplify` invocation**. It found no further scope-appropriate changes. Whole-file holistic review remains the owner's later obligation.

## Actual verification

All compiler, native, semantics and LSP jobs were serial. No source edits occurred during final validation.

| Gate | Actual result |
|---|---|
| Full project | `lake build` exit 0, 56.358 s (`final-full-build-{launch,terminal}.json`) |
| Separate Eval | then `lake build Roth.LeanEval` exit 0, 29.323 s |
| Native Main / Eval / root | `lake env lean` each exit 0, 28.596 / 29.649 / 33.689 s |
| Complete unfiltered LSP | Main / Eval / root: partial=false, success=true, 0 errors; only preexisting Main line-1 header warning |
| Definition protection | no def/abbrev edits |
| Statement protection | exact signature tokens, no weakening or conclusion change |
| Structure | 15 body lines, no conjunction conclusion, no case branches |
| Naming | descriptive snake_case/private/_aux, no forbidden pattern; no rename queue entry |
| Packing | all 10 signature lines measured; max 99; no remaining repack row |
| Inequality | zero reversed ≥/> in signature/hypotheses |
| Comments | all 3 immediate/proof signposts preserved |
| No trust/limit/scaffolding change | no sorry, new axiom, native_decide, resource raise or production profiling scaffolding |
| Scope | replacing final helper with genuine helper recovers exact entry Main bytes |

The full build validates the actual current source, including existing parent adaptations, but does not count as a separate parent audit. No redundant unchanged baseline build was run solely to change a label.

## TYPE, opaque VALUE and dependency checks

Distinct independent proof: `/private/tmp/roth-main-roth-eval-bound/IndependentEvalBound.lean`, compile exit 0, 29.474 s. It uses the original exponential/log argument and a calc composition instead of the final direct rpow API/composed term. It does not use the production helper or the later parent.

Actual complete production/independent families and actual universes were enumerated **before** guards (`Enumerate.lean`, exit 0, 52.134 s). Exactly two total rows: `_private.Roth.Main.0.Roth.one_lt_roth_eval_bound_aux` and `Roth.independentEvalBound`, each with actually discovered universe list `[]`; no suffix or universe assumption. Both actual opaque proof VALUEs were checked in memory under defaults **200000 / 20000 / 512**, inferred against their declared types, closed/no admits, and standard axioms only (`propext`, `Classical.choice`, `Quot.sound`). Receipt stores hashes/lengths, not full VALUE dumps or VALUE identity claims.

Strict comparison traverses Name/Level/BinderInfo/Expr/metadata/literal/projection structure recursively, with no ExprBEq short-circuit. The actual genuine-prefix/current/independent raw TYPEs differ only at the ninth anonymous NeZero binder, body/body/body/body/body/body/body/body/binderName. The literal actual Name pairs (all hasMacroScopes, equal eraseMacroScopes=`inst`, matching `.instImplicit`) are recorded in `finite-hygiene-actual.json`; complete remaining raw TYPE bytes and recursive Exprs match. No generic alpha-normalization is used. Final regular profile TYPE is raw-exact to genuine-prefix TYPE, binding the final scoped capture to this comparison.

The first aggregate semantics compile failed because a pasted internal `_@` Name component needed quoting. Its **two valid opaque VALUE rows were preserved** (`semantics-valid-rows.json`). Only the outstanding strict root TYPE check was supplemented (`SemanticsRoot.lean`, exit 0, 37.701 s); no VALUE row was rerun. This failure is not claimed a whole-pass success. Actual local graph has no edges and is acyclic. External origins were checked strictly upstream of Main (346 production / 345 independent references); only the two accepted preceding Main evaluation bounds were reused as leaves. No unchanged accepted helper proof was cloned, re-proved or re-inferred. All subsequent Main/circular/self dependencies were denied.

## Scoped performance

Each phase requested and received OWNER HOLD **before preparation**. Owner writes/review/parsing/compiler/native/LSP remained idle through preparation/capture/default/environment/freeze/drain. Actual driver and child process groups were confirmed absent; raw-unparsed notice preceded explicit OWNER RELEASE, and parsing followed release. Full parent/Lake environment bytes were compared only in memory; persisted environment data is hashes/lengths and the safe PATH/LEAN/toolchain allowlist.

Both phases use exact source prefix, unchanged imports/preceding commands/target and namespace close, plus actual family/TYPE/VALUE/default/format-width observation. Full canonical printed payload matches the target. Every disjoint command/proof/kernel-parent/lint root is counted; nested kernel nodes are not double-counted. Actual family has one member; no compiler root or lazy prior DATA root belongs to this target. No inner macro command is present, so no indentation-based macro-parent inference is needed.

| Exact context | Command | Proof | Kernel parent | Lint | Total |
|---|---:|---:|---:|---:|---:|
| Genuine first draft | 152.536 | 273.885 | 8.497 | 23.113 | **458.031 ms** |
| Final helper | 131.084 | 244.052 | 10.231 | 18.923 | **404.290 ms** |

Both totals are below 750 ms, so no repeat is required; both pass the 1000 ms budget. No cross-context speedup claim is made. These helper timings do not replace the owner's required later fresh whole-file capture.

Genuine driver 21746 and groups 21749/21775/21800/21926/21957 drained before release. Final driver 22908 and groups 22912/22937/22961/23019/23044 drained before release. Actual raw-drain receipts and explicit hold/release records live under the two profile directories. No unchanged extra capture was made.

## Phase checklist and handoff

References ✓; full 24-item audit ✓; five-method status ✓; every-binder mechanical review ✓ (no unsupported compiled-test claim); HAVE ✓; complete line table ✓; inequality ✓; all 42 rules ✓; step-back ✓; final complete diagnostics ✓; actual builds/native ✓; strict TYPE/actual opaque VALUE/default/dependency gates ✓ with recorded narrow hygiene exception and initial failed aggregate qualification; manual simplify substitute ✓; scoped buzz ✓; rename queue empty ✓; accepted helpers/reports unchanged ✓. No further refactoring is proposed.

Final process drain / leases are recorded in `/private/tmp/roth-main-roth-eval-bound/END.json`; final machine-readable handoff in `FINAL.json`. SAME parent worker resumes after owner local acceptance, then joint parent/helper publication only.

---

# Initial substantive audit — one_lt_roth_eval_bound_aux

Read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, style-rules.md, naming-conventions.md, mathlib-review-stages.md, profiling.md and buzz command. Scoped cleanup uses Lean4 and mathlib-quality. Genuine first ungolfed saved before any helper Lean/golf: SHA 3fce52537d382083b458dca1a315bb0d133a1132a52f136cf8d7b195ff545697, 34 declaration / 20 body lines. Entry source c4c1c2938431231208eafbf45003d3bb282b0d80d4dc3349f8825d5b31033136. Parent and accepted helpers frozen.

Mathematics: eliminate a nonzero integer multivariate polynomial supplied by main_lemma. Its degree and index bounds imply a strict Taylor upper estimate. The nonzero rational evaluation gives a lower estimate after multiplication by denominator powers. Positive multiplication combines the estimates into a numerical product strictly greater than one. This removes Q from the conclusion and isolates a coherent stage; it is not a fact tuple or a wrapper for 1–3 mathlib calls.

1. LINT: complete entry LSP, no target warnings/errors; header warning at line 1 outside scope.
2. HAVE: hidx no by/one use -> inline; hqR has by (lambda)/four uses -> retain; hmapQ no by/zero uses -> remove; hdmap has by/one use -> retain unless API term replaces; hqr has by/one use -> retain mathematical logarithm conversion; inner hrj has by/one use -> retain cast fact; hupper no by/one use -> inline; hlower no by/one use -> inline; hP0 no by/one use -> inline.
3. SET_OPTION: none, defaults 200000/20000/512.
4. SIMP: none.
5. NAMING: one_lt_roth_eval_bound_aux describes oriented numerical bound, snake_case/private/_aux, no forbidden pattern.
6. PACKING: measure every signature line after bounded cleanup; no signature change is anticipated.
7. BY: all at preceding line end.
8. FORMAT: replace lambda => by ↦, no empty proof lines or semicolon chains.
9. COMMENTS: preserve immediate ordinary stage comment and both Lemma 9 / upper-bound comments.
10. DOCSTRING: none required/private; immediate ordinary comment preserved.
11. VISIBILITY: private auxiliary, sole intended parent consumer.
12. STRUCTURE: 20-body lines before cleanup, no conjunction conclusion or branching; no extraction needed.
13. MATHLIB: five methods on useful substeps: LeanFinder degrees_map_le hit; Loogle degreeOf/map no results; LeanSearch log/rpow hits; direct source finds degrees_map_le and rpow_le_iff_le_log; local name search warming (not absence evidence). Generic degree count API to be compiler tested. Common-equivalent table none (not topology/finiteness). The combined theorem depends on project main_lemma/index/height/Taylor bounds, cannot be replaced by generic mathlib statement. Auxiliary variants degrees_map_of_injective, degreeOf_def, rpow_le_iff_le_log reviewed; no absence claim.
14. JUNK DEF: n/a lemma.
15. EXISTS: n/a numerical inequality conclusion.
16. SHOW: none.
17. PUSH_NEG: none.
18. GENERALISE: all binders below; no supported signature weakening identified; no ambient restatement.
19. INEQUALITY: zero reversed ≥ or > in Lean signature. Existing ≤/< retained; no rename.
20. NORMAL FORM: numerical real inequality 1 < product; existing rpow/casts canonical, no equivalence family.
21. SYNTAX: useful eliminated-Q statement for caller; weakening to an existential or fact tuple would hurt use.
22. IMPORT: no imports added.
23. CASTS: ℤ→ℝ and ℕ→ℝ are cross-type; B₁ cast fixes real rpow; (0 : ℝ) fixes quantified cast facts. Audit changes only; no redundant cross-type cast deletion.
24. INSTANCE NAME: n/a no named instance.

## Per-binder mechanical review
Every binder receives a row. Drop-test support is dependency/type review followed by actual proof checks; unsupported drops are not claimed compiled.

| Binder | Class/use | Candidates / decision |
|---|---|---|
| α | real value/root/approximation | drop prevents types; real logs/evaluation fix concrete domain, no universe candidate |
| κ | real value/exponent | conclusion and happ, cannot drop |
| f | polynomial value | conclusion natDegree and monic/root/coefficient bounds, cannot drop |
| hf | proposition | main_lemma requires Monic, no unused/drop evidence |
| hfα | proposition | main_lemma requires exact root, no order weakening |
| A | real value | hA,h32, cannot drop |
| hA | global proposition | main_lemma needs all coefficients; no pointwise restriction supported |
| m | natural dimension | Fin m, gam, eta fix value |
| NeZero m | instance | Fin.rev 0/q 0/r 0 require zero index; cannot drop without restatement |
| δ | real value | bounds, exponent/index stage, cannot drop |
| hδ0 | proposition | already weak nonnegative; main_lemma consumes it |
| hδm | proposition | already weak; main_lemma consumes it |
| r | function value | all degree and index expressions depend on it |
| hr0 | global positivity | rpow/log division needs each r j positive; ≤ would permit zero denominator |
| hrlast | proposition | weak lower degree hypothesis main_lemma requires |
| h31b | global proposition | main_lemma needs each adjacent pair, no restriction supported |
| q | function value | conclusion and approximation, cannot drop |
| hq0 | global positivity | lower evaluation and upper bound require each denominator nonzero, ≤ would permit 0 |
| hκ0 | proposition | already weak, upper estimate consumes |
| h | integer function | happ/hcop and rational evaluation, cannot drop |
| happ | global proposition | already weak approximation for all j, upper bound consumes |
| hcop | global proposition | main_lemma nonzero evaluation consumes each coprimality fact |
| h32 | proposition | already weak, main_lemma consumes height bound |
| h33 | global proposition | balanced logs for every j, needs all j for power bound |

No type variable/universe or weakening catalogue algebra class is present; universe generalization n/a. Inversion check: B₁/gam/eta remain substantively tied to main_lemma and Taylor stage, no concrete witness unfolded into a generic theorem. Private lemma literature search n/a.


# Golf and pre-gate audit completion

Initial 24-item audit and every binder reviewed in initial-audit.md. Kept public/library contracts; production signature tokens unchanged. No supported unused parameter detected; zero API weakening means no affected caller recovery contract needed. Failed multiset-count replacement probes (unknown guessed count_le_count; count_le_of_le then DecidableEq mismatch) were reverted. No unsupported lemma survives. Original support rewrite retained. Real.rpow_le_iff_le_log is source-verified and successful, eliminating explicit exp conversion. No new imports. Three comments preserved. Scope is only helper.

Manual holistic simplify review (built-in simplify unavailable; not an invocation): substantive polynomial elimination, degree/index transport, log conversion and strict/lower estimate composition remain coherent; no duplicate helper extraction required. Accepted prior helpers are untouched and reused only as accepted context. Parent remains separately audited later.

## Signature packing
Units are complete next binder/expression factor, widths in codepoints (not bytes). Every line included. Colon at end of h33 stays with full conclusion requiring separate line.

| Line | Width | Next unit width | width+1+next | Action |
|---|---:|---:|---:|---|
| 449 | 84 | 30 | 115 | ok |
| 450 | 97 | 7 | 105 | ok |
| 451 | 80 | 26 | 107 | ok |
| 452 | 96 | 15 | 112 | ok |
| 453 | 70 | 55 | 126 | ok |
| 454 | 99 | 98 | 198 | ok |
| 455 | 78 | 23 | 102 | ok |
| 456 | 94 | 52 | 147 | ok |
| 457 | 97 | 64 | 162 | ok |
| 458 | 70 | None | n/a | ok |

## Inequality scan
| Location | Reversed occurrences | Action |
|---|---:|---|
| Full signature and each hypothesis | 0 | all ≤/<, no rename |

## All 42 rules
- 1.1: no by-exact wrappers remain; cast proof is substantive exact_mod_cast
- 1.2: n/a no rfl proof
- 1.3: n/a rewrite followed by degree proof requires original bound, no rw/exact redundant rewrite of result
- 1.4: n/a no simp+exact
- 1.5: n/a no simp/rfl
- 1.6: n/a no constructor chain
- 1.7: n/a no apply/exact
- 1.8: n/a no contradiction
- 1.9: n/a lambdas bind indexed cast evidence, not eta expansion
- 1.10: inlined hidx/hupper/hlower/hP0; removed unused hmapQ
- 1.11: n/a no apply+intro
- 1.12: n/a no show
- 1.13: already obtain main_lemma tuple, ignored unused hQ0
- 1.14: n/a no consecutive rw
- 1.15: n/a no simp only
- 1.16: n/a no bare simp
- 1.17: trans_lt composition used in final estimate
- 1.18: final application natural parentheses retained to group product estimate; no $
- 1.19: n/a no push_neg
- 1.20: n/a nonexistential substantive result
- 2.1: whole target grind and degree subgoal grind tried through LSP, failed (not a proof simplification)
- 2.2: n/a no grind retained
- 2.3: n/a no simp chain
- 2.4: n/a no function regularity property
- 2.5: product positivity explicit Finset.prod_pos/pow_pos term; no arithmetic search needed
- 2.6: mul_lt_mul_of_pos_left is exact monotonicity API; avoids side-goal search
- 2.7: n/a no Nat/Int arithmetic goal, real logarithm inequality uses linarith
- 2.8: degree subgoal aesop tried, failed exhaustive search
- 2.9: cast bridges retain exact_mod_cast; no concrete numeric computation
- 2.10: n/a noncomputable real inequality, no finite decidable calculation
- 2.11: n/a no field identity goal
- 2.12: n/a no ring-ending block
- 2.13: n/a no symmetric cases
- 2.14: final inequality trans_lt term composes lower/upper bounds
- 2.15: n/a no parallel similar goals
- 3.1: n/a no erw
- 3.2: n/a no legacy continuity/measurability
- 3.3: n/a no omega
- 3.4: n/a no rcases rfl
- 3.5: private one-off stage, no automation attributes justified
- 3.6: n/a no simp_all only
- 3.7: no set_option limit overrides present

Step back: wholeproof grind/exact?/apply? attempts did not supply a replacement. The mathematical dependency on main_lemma and specialized Taylor bounds supports keeping this stage. Body 15 lines, no conjunction conclusion or case branch. Retain named degree/log intermediate proofs for clarity. No optional generalization/extraction.

Pre-final checklist: references ✓; 24 audit items ✓; five-method search ✓ (local warming qualified); every binder mechanical dependency review ✓ (no claimed compiled unsupported drop); line table ✓; inequality table ✓; 42 rules ✓; step-back ✓; edited complete LSP ✓ (0 errors; header warning outside scope); no renames ✓. Actual final native/build/semantics/profile still pending, not claimed passed.
