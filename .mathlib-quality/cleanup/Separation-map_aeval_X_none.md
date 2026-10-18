# `Roth.map_aeval_X_none` — original declaration 27

## Initial audit, before source edits

Read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, cleanup-gates.md, applicable style/naming/profiling references,
both skills, and the installed cleanup Phase 4 workflow. Scope: private helper at
451–458 (8 declaration lines, 5 body lines), with its sole caller in `exists_int_factors`.
Baseline supplied by parent: clean pushed HEAD `1ea6cec`, 561 source lines, 26 retained
declarations. Full-project baseline/final verification is owned by parent.

1. LINT: live goal obtained; complete unfiltered diagnostics gate still to run.
2. HAVE SCAN: zero `have` declarations.
3. SET_OPTION: none.
4. SIMP SQUEEZE: no simp in the current proof.
5. NAMING: `map_aeval_X_none` describes mapping evaluation at `X none`; no forbidden
   abbreviation or numbered scheme. If equivalent mathlib replacement compiles, remove
   this private wrapper rather than queue a rename.
6. LINE PACKING: three signature lines; exact widths and compiler width reference below.
7. BY PLACEMENT: `by` ends the final signature line.
8. FORMAT: 2-space tactic indentation, one tactic per line; final rw list wraps naturally.
9. COMMENTS: no comments inside target; caller narrative must remain unchanged.
10. DOCSTRING: n/a, private helper appropriately lacks one.
11. VISIBILITY: private, used only once in this file.
12. STRUCTURE: 5-line body, equality conclusion, no branches or conjunctions.
13. MATHLIB: generic `Polynomial.map_aeval_eq_aeval_map` found; compiled specialization
    and caller substitution will determine removal.
14. JUNK DEF: n/a, lemma rather than data definition.
15. EXISTS LEMMA: n/a, equality rather than existential.
16. SHOW vs CHANGE: none.
17. PUSH_NEG: none.
18. GENERALISE: effective binders are `{τ : Type u}` and `(V : Polynomial ℤ)`;
    both occur in the proposition. Existing `omit [Fintype τ] [DecidableEq τ]` already
    appears in ORIGINAL and must not be credited as new cleanup. No effective class
    hypothesis. Abstract coefficient naturality is already mathlib's generic theorem.
19. INEQUALITY: zero `<`, `≤`, `>`, or `≥` occurrences in target statement/hypotheses.
20. NORMAL-FORM: naturality of polynomial evaluation is the generic canonical form.
21. SYNTAX-GEN: direct rewriting with the generic naturality theorem should ease reuse.
22. IMPORT-FANOUT: no new imports planned; existing imports expose generic theorem.
23. CASTS: two `X none` type ascriptions select coefficient ring and variable type;
    retain statement ascriptions in independent original-type probe. No explicit ↑ casts.
24. INSTANCE-NAME: n/a, lemma not instance.

Issues: verify exact generic specialization, then delete authorized duplicate private
wrapper and substitute its sole caller if successful. No public removal, domain widening,
new helper, docstring edit, or instance removal is proposed.

## Mathlib search status

All five methods actually invoked. Lean-Finder returned `Polynomial.eval_map_apply`,
`Polynomial.eval_map`, `Polynomial.eval₂_eq_eval_map`, and related evaluation naturality.
Loogle query `Polynomial.aeval, MvPolynomial.map` returned no results (not absence).
LeanSearch returned exact generic `Polynomial.map_aeval_eq_aeval_map`.
Untruncated source/name search found its implementation at
`Mathlib/Algebra/Polynomial/AlgebraMap.lean:499` and sole helper caller at Separation:513.
Local name search `map_aeval` also returned the exact generic theorem; index unavailable,
so source evidence and compiled probes are used rather than claiming index completeness.
Private literature exemption applies explicitly: this is a private polynomial naturality
helper, so no public-result literature search is required.

## Generalisation status

| Effective binder | Drop/weakening assessment | Verification status |
|---|---|---|
| `{τ : Type u}` | Required to type `Option τ`; already universe polymorphic | Syntactic dependency; no false compiler-negative claim |
| `(V : Polynomial ℤ)` | Polynomial being evaluated on both sides | Syntactic dependency; no false compiler-negative claim |
| Fintype τ | Already omitted in ORIGINAL | Original source and live goal confirm absent |
| DecidableEq τ | Already omitted in ORIGINAL | Original source and live goal confirm absent |

Point-localisation/strict weakening/unbundling: no such hypotheses. Concrete-to-abstract
inversion fires for coefficient mapping; generic mathlib theorem already supplies the
abstract version. No new general theorem is needed.

## Inequality scan

| Occurrence | Relation | Action |
|---|---|---|
| Entire target signature and hypotheses | None (equality only) | No rewrite or rename |

Final widths, all 42 rule statuses, independent proof/axioms, diagnostics, build, actual
anchored performance and freeze evidence will be appended after probes complete.

## Applied result and exact equivalence

Deleted the 8-line private declaration, its already-existing 1-line omit, and its separator
line (10 lines); replaced its sole caller's 1-line rw with a 3-line rw (+2): net −8.
Actual `wc -l`: 561 → 553. Retained declarations: 26 → 25. No helper added.
Only caller proof changed: `Roth.exists_int_factors`; its signature and documentation
are byte-identical. `aeval_X_eq_rename` and `coeff_uniqueAlgEquiv_symm` remain present.

The exact ORIGINAL proposition was re-proved independently as `independentOriginal`,
with only `{τ : Type u}` and `(V : Polynomial ℤ)` and no finiteness/decidability classes.
Its proof uses generic polynomial evaluation naturality with coefficient map
`Int.castRingHom ℚ`, ambient ring map `MvPolynomial.map (Int.castRingHom ℚ)`, and
`map_X`. The coefficient compatibility square is equality of two ring homomorphisms
from ℤ, discharged by `Subsingleton.elim`. This preserves both sides of the original
equality exactly; it is specialization, not a change of mathematical domain.

Native independent probe: `/private/tmp/roth-d27-independent.lean` and
`/private/tmp/roth-d27-independent-native.json`: success true, timed_out false,
zero errors/warnings, 3 infos. The proof uses no reference to the removed target.
Compiler width reference (`format.width 100`, never `pp.width`):

```lean
@independentOriginal : ∀ {τ : Type u_1} (V : Polynomial ℤ),
  (map (Int.castRingHom ℚ)) ((Polynomial.aeval (X none)) V) =
    (Polynomial.aeval (X none)) (Polynomial.map (Int.castRingHom ℚ) V)
```

### Signature width table (before removal)

Widths measured in codepoints. Semantic expressions are kept intact at natural breaks.

| Signature line | Width | Next expression/token | Arithmetic | Action |
|---|---:|---|---|---|
| 451 | 51 | Left equality operand, 81 chars without indentation | 51 + 1 + 81 = 133 | ok |
| 452 | 87 | Right operand plus `:= by`, 87 chars without indentation | 87 + 1 + 87 = 175 | ok |
| 453 | 93 | None; proof begins | n/a | ok |

Final target signature: absent by authorized duplicate removal, so no underpacked
retained signature remains. Caller replacement lines are 59, 96, 12 codepoints;
the final `hVmap]` cannot join preceding line without exceeding 100:
96 + 1 + 6 = 103.

### Effective binder probes and inversion

Both effective binder drop attempts were actually run under `autoImplicit false`:
dropping τ reports `Unknown identifier τ` at the two Option types; dropping V reports
`Unknown identifier V` and `V.map`. Raw expected-negative results:
`/private/tmp/roth-d27-binder-drop-native.json`. These are syntactic well-formedness
failures, not evidence of mathematical nongeneralizability. They add no source sorries:
the failed elaborator's displayed recovery terms occur only in diagnostics.
All generic coefficient/ambient-ring generality is already expressed by mathlib's
theorem, checked at width 100 in the independent probe. No additional widening is
needed. Literature remains explicitly exempt because the audited target is private.

## Golfing-rule pass (all 42)

| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no `by exact` wrapper |
| 1.2 | n/a: no `by rfl` |
| 1.3 | n/a: no `rw; exact` sequence |
| 1.4 | n/a: no simp followed by exact/assumption |
| 1.5 | n/a: no trailing rfl |
| 1.6 | n/a: no constructor |
| 1.7 | n/a: no apply/exact chain |
| 1.8 | n/a: no contradiction proof |
| 1.9 | n/a: no lambdas |
| 1.10 | n/a: no have |
| 1.11 | n/a: no apply/intro |
| 1.12 | n/a: no show |
| 1.13 | n/a: no projected have |
| 1.14 | Already two rw calls separated by congr and ext, so cannot merge directly; target removed |
| 1.15 | n/a: no terminal simp only |
| 1.16 | n/a: no nonterminal simp |
| 1.17 | n/a: rewriting theorem names is appropriate in rw |
| 1.18 | n/a: no trailing function parentheses to replace |
| 1.19 | n/a: no push_neg |
| 1.20 | n/a: equality, not trivial existential |
| 2.1 | Live `grind [Polynomial.map_aeval_eq_aeval_map]` failed; explicit specialization closes |
| 2.2 | n/a: no retained grind chain |
| 2.3 | Independent `simpa using` generic naturality succeeds; delete wrapper rather than retain golf |
| 2.4 | n/a: no continuity/differentiability/measurability predicate |
| 2.5 | n/a: equality of polynomial evaluations, no positivity goal |
| 2.6 | n/a: no inequality/monotonicity |
| 2.7 | n/a: no linear Nat/Int arithmetic proposition |
| 2.8 | n/a for final target: removed; direct generic theorem resolves equality without aesop |
| 2.9 | n/a: no concrete numeric computation/cast normalization needed |
| 2.10 | n/a: universally quantified polynomial identity, not finite decision computation |
| 2.11 | n/a: no denominators |
| 2.12 | n/a: no terminal ring/ring_nf and no ring hypotheses |
| 2.13 | n/a: no symmetric branches |
| 2.14 | n/a: no calc |
| 2.15 | n/a: no similar multiple subgoals; sole caller branch closes by rw |
| 3.1 | n/a: no erw |
| 3.2 | n/a: no continuity/measurability tactics |
| 3.3 | n/a: no omega |
| 3.4 | n/a: no rcases |
| 3.5 | n/a: removed helper; generic mathlib theorem is explicitly rewritten |
| 3.6 | n/a: no simp_all only |
| 3.7 | n/a: no limit options |

Live rfl and bare simp failed; exact? failed to find the required specialization.
The initial multi-attempt's successful simpa produced `No goals to be solved` on the
following old tactic; the subsequent isolated independent proof is the definitive
successful full-proof test. The multiline caller test similarly disturbed following
line positioning; complete live module diagnostics and actual module build validate
the applied caller instead of treating those tool-local residual errors as source errors.

## Step-back / simplify review

Evaluation commutes with coefficient maps by a generic naturality square. Routing
through `uniqueAlgEquiv`, renaming, and coefficient extensionality proves the same fact
indirectly. The direct theorem removes this detour and its one-use private wrapper.
No new public API, private helper, automation attribute, definition, or import is needed.
No additional simplification warrants source churn. The explicit coefficient map and
compatibility term keep elaboration predictable at the caller.

## Verification and gates

`/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0, 1876 jobs:
`/private/tmp/roth-d27-module-build.log`. Complete unfiltered native LSP:
`/private/tmp/roth-d27-final-lsp.json`: partial false, timed_out false, success true,
0 errors, 6 warnings, 0 infos, no failed dependencies. Warnings are header (1),
retained `exists_int_factors` instance/type warnings (3, including unusedSectionVars),
and retained `exists_det_eq_mul` instance/type warnings (2). Public instance removals
remain unapproved and unapplied; user-preserved header metadata is untouched.

Fresh standalone compiler on actual built module:
`/private/tmp/roth-d27-actual-axioms.lean` →
`/private/tmp/roth-d27-actual-axioms.log`, exit 0. Exact suffix enumeration finds
0 retained private `Roth.map_aeval_X_none` constants. Actual retained caller
`Roth.exists_int_factors`, downstream `Roth.exists_det_eq_mul`, and generic mathlib
replacement each use only `[propext, Classical.choice, Quot.sound]`.
The prior native axiom probe reported stale imports and 1 old private match; it is
explicitly superseded by this fresh-process actual-built check, never used as final evidence.

| Gate | Status | Evidence |
|---|---|---|
| lake_build_file | pass | Actual Roth.Separation build exited 0 |
| definition_protected | pass | Scoped diff changes no def/abbrev |
| theorem_statement_protected | pass with authorized removal | Only owned duplicate private lemma removed; public signatures unchanged |
| structure_gate | pass | Owned target removed; no new proof/helper introduced |
| naming_gate | pass | No forbidden name survives from target; no rename needed |
| line_packing_gate | pass | Three pre-removal rows above; no retained target signature |
| inequality_orientation_gate | pass | Zero oriented inequality occurrences in owned target |
| comments/docstrings | pass | No narrative or documentation changed |
| cumulative compatibility | parent gate | Sole private caller checked by module build; full original/public sweep owned by parent |

Scoped diff: `/private/tmp/roth-d27-scoped.diff`. Search raw repeat:
`/private/tmp/roth-d27-search-native.json`; all four native search requests completed
without errors, plus untruncated source search in session. Auxiliary variants considered:
`map_aeval`, `eval_map_apply`, `eval₂_eq_eval_map`, and `map_aeval_eq_aeval_map`.
Common-equivalents table has no relevant discrete/finite/topological bucket. All six
replacement rules respected: found generic theorem, deleted wrapper, specialized at sole
caller, no custom predicate or unsupported absence claim. Existing module docstring is
user-preserved, so usage is documented here rather than modifying public documentation.

No concrete pending proposal from this leaf. No added helper needs fresh audit.

## Buzz / final profile

After every native Lean/MCP and compiler request completed, ran the actual repository
module as the sole Lean workload:

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Exit 0. Raw log `/private/tmp/roth-d27-final-profile.log`; parsed anchored table
`/private/tmp/roth-d27-final-profile.log.json`, using
`/private/tmp/roth-separation-profile-table.py` against the actual current source.
The outer command and outer async proof each appear exactly once for the changed caller;
nested trace nodes are not double-counted.

| Actual declaration | Baseline outer command + proof | Final outer command + proof | Conservative final total |
|---|---:|---:|---:|
| map_aeval_X_none | 47.117 + 81.856 ms | removed | 0 ms (no retained constant) |
| exists_int_factors | 50.333 + 588.417 ms | 64.279 + 606.011 ms | 670.290 ms |
| exists_det_eq_mul (unchanged downstream proof) | 102.116 + 392.834 ms | 108.419 + 421.044 ms | 529.463 ms |

Baseline is the parent-supplied actual-module d26 profile, valid for this previously
unchanged target and caller. Changed caller is under 750 ms and 1000 ms; no repeat or
performance repair required. No claim of whole-project speed improvement is made.
No profiler scaffolding or options were inserted into source.

## Eleven completion steps

- [x] Step 1: skills and full mandatory references read; applicable style/naming/profiling read.
- [x] Step 2: all 24 initial audit items recorded before source edit.
- [x] Step 2.5: five actual search methods, raw repeated native results, exact source theorem.
- [x] Step 2.6: every effective binder considered; actual expected-negative drop probes;
  generic coefficient naturality verified; explicit private literature exemption.
- [x] Step 2.7: all three original signature widths measured, width-100 compiler reference;
  target removed and caller rewrites packed within 100.
- [x] Step 2.8: occurrence-complete inequality table (no inequalities).
- [x] Step 3: all 42 golf rules have concrete statuses.
- [x] Step 4: independent mathematical step-back and simplify review recorded.
- [x] Step 5a: complete unfiltered native diagnostics, no errors and six known baseline warnings.
- [x] Step 5b: scoped diff gates, actual module build, independent exact original proof,
  actual built environment/axioms, and isolated actual-module profile pass.
- [x] Step 6a: no renames needed; no shared sidecar touched, no helper added.

## Final freeze

All native Lean/MCP requests and all module/compiler/profile sessions have completed.
No subagent, pending request, or compiler/profile process was left running by this leaf.
No Git mutation or shared progress/log mutation performed.
Source SHA256 at freeze:
`f8eda96bc0bc19d15d9137243f08cbac7d3d5ad2e031077526262520abfcac23`.
I revoke **ALL source ownership**, including target and callers, and am now report-only.
No source edit will occur after this freeze. Parent owns sequential full-project and
LeanEval builds, whole-original/public compatibility/axioms, exact-path commit and push.

## Owner cumulative publication gates

Source FROZEN SHA256 `f8eda96bc0bc19d15d9137243f08cbac7d3d5ad2e031077526262520abfcac23`; leaf ownership revoked and requests drained before owner gates. Owner probe `73423` exit0,39.39s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-d27-compatibility.{lean,log,json}`. Owner build session `66697` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,124.48s/30.65s; source hash stable. `/private/tmp/roth-separation-d27-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
