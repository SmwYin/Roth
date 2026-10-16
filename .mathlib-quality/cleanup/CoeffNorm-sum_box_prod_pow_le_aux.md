# Fresh Phase-4 audit: `sum_box_prod_pow_le_aux`

Scope: private helper added during `abs_eval_le` cleanup; no original-declaration tally increment.
Owned source range originally L208–218 (11 lines), finally scoped command L208 and theorem L209–214
(7 lines including scope, 6 theorem lines). Proof body: 8 → 4 lines. Sole caller: `abs_eval_le`, L235.
Public API, mathematics, header, docstrings and comments unchanged. No new helper introduced.
SOURCE FROZEN SHA256: `7270e6f1cb84f697ca7016758951801f6805d2867ca2a1ad0597f6bc7be8ca68`.
Ownership revoked after this hash: all subsequent work only scratch probes and this report.

## Step 1: references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read both SKILL.md files,
cleanup/cleanup-all workflows, supplied full Phase-4 contract, style-rules.md,
naming-conventions.md, mathlib-review-stages.md and the buzz command.
Filewide baseline/project stages belong to the fileowner; this report is the mandatory
fresh single-helper audit, not a claim to have run all filewide stages independently.

## Step 2: all 24 audit items

1. LINT: native baseline and final complete diagnostics contain no warning in helper range.
   Six inherited warnings elsewhere: header, four public DecidableEq arguments and `hC`.
2. HAVE SCAN: no `have` in original/final helper; nothing to inline.
3. SET_OPTION: none; no heartbeat/recursion options added.
4. SIMP SQUEEZE: original equality-closing simp terminal; kept unsqueezed in spirit.
   Replaced calc plus terminal simp by terminal `simpa [← Finset.mul_sum, box,
   Finset.prod_univ_sum] using ...`; no nonterminal bare simp remains.
5. NAMING: descriptive snake_case; private `_aux` encouraged; no forbidden abbreviation,
   numbered suffix, scheme number, `_ge_` or `_gt_`. Rename queue: none.
6. LINE PACKING: repacked from three signature lines to two; exact table below.
7. BY PLACEMENT: `:= by` ends conclusion line.
8. FORMAT: 2-space proof indentation, 4-space signature continuation, no blank proof lines,
   no `haveI`/`letI`, no trailing whitespace; every line ≤100 codepoints.
9. COMMENTS: no inline comments in helper; all surrounding comments untouched.
10. DOCSTRING: private technical helper correctly has none.
11. VISIBILITY: private and solely used by `abs_eval_le`; keep private.
12. STRUCTURE: four proof lines, no conjunction or case branches; no extraction needed.
13. MATHLIB: five actual search methods below; distributivity and monotonicity reused.
14. JUNK DEF: n/a, theorem.
15. EXISTS LEMMA: n/a, inequality, no existential witness.
16. SHOW vs CHANGE: neither present.
17. PUSH_NEG: none.
18. GENERALISE: removed unused private `[DecidableEq σ]`, with declaration-local Classical
    scope for `box` in the statement; full table below. No public API touched.
19. INEQUALITY: hB and conclusion both use ≤; zero ≥/>. Table below.
20. NORMAL-FORM: bound stated with sum on left/product on right; Cartesian product-of-sums
    intermediate normalized by `Finset.prod_univ_sum`; no equivalence API added.
21. SYNTAX-GEN: current `(r) {B} (hB) (x)` matches caller exactly; removing redundant instance
    improves application. Arbitrary finite-product restatement would hide needed project `box`.
22. IMPORT-FANOUT: n/a, zero import changes.
23. CASTS: zero dropped/zero cross-type/zero load-bearing casts in diff; `(x j)` parentheses
    are application grouping; `(s := Finset.univ)` is a necessary explicit index-set argument.
24. INSTANCE-NAME: n/a, no instance declarations.

Issues fixed: signature underpacking; unused private decidability argument; redundant calc
intermediate. Refactoring needed: none. Comments preserved: all (none inside helper).

## Step 2.5: five actual mathlib searches

| Method | Actual query / operation | Finding |
|---|---|---|
| A Lean-Finder | `sum over finite cartesian product of products equals product of sums`, 3 results | `Finset.sum_prod_piFinset`, `Fintype.sum_prod_type`, `Finset.prod_univ_sum` |
| B Loogle | `Finset.prod_univ_sum`, 3 results | exact generic distributivity signature in `Algebra.BigOperators.Ring.Finset` |
| C LeanSearch | `sum over finsupp box product powers bound product geometric sums`, 3 results | `Finsupp.prod_pow`, `Nat.geom_sum_le`, `geom_sum_mul_of_le_one`; no complete bound |
| D full-name/source rg | untruncated `sum_box_prod_pow_le_aux|prod_univ_sum|prod_le_prod₀` in ring/order Finset sources | distributivity declaration L157 plus usages L163/167/302; no full helper equivalent |
| E local name search | `prod_univ_sum`, limit 10 | verified `Finset.prod_univ_sum` source; index warming, positive hit only (no absence conclusion) |

`exact?` at helper entry did not close. `apply?` suggested only partial general order lemmas,
with fresh unsolved hypotheses; no complete proof. Thus no direct replacement demonstrated.
Six-rule check: (1) retained because combines project-specific `box`, nontrivial same-file
geometric-binomial lemma and finite distributivity/positivity/monotonicity; not solely 1–3
mathlib calls, and inlining expands headline caller beyond its target proof budget;
(2) all five methods plus full-name search and actual elaborator search completed;
(3) auxiliary Cartesian variants inspected; (4) existing Fintype/mathlib structures reused;
(5) no exact equivalent found to delete; (6) existing header protected by explicit user scope,
mathlib usage documented here. Common-equivalents table consulted: no set/discrete/coset wrapper.
No claim that generic libraries cannot express the result; they supply the combinatorial
building blocks actually used.

## Step 2.6: mechanical generalisation

| Binder | Kind | Used in | Candidates / actual result |
|---|---|---|---|
| `{σ : Type*}` | type/universe | box indices and functions | already universe-polymorphic; dropping leaves dependent binders without a type; no further universe restriction |
| `[Fintype σ]` | typeclass | finite products and `box` | cannot drop: finite products and `box` require it; `Finite` alone changes instance construction, with classical Fintype recovery merely repackaging the same finiteness |
| `[DecidableEq σ]` | decidability | statement elaboration of `box` | bare deletion actually fails synthInstance at old L210; declaration-local `open scoped Classical in` plus deletion compiles, kept; not global instance |
| `(r : σ → ℕ)` | data | upper bounds, conclusion | cannot drop without changing mathematical statement; no point-local or strict hypothesis here |
| `{B : ℝ}` | data | scalar both sides | cannot drop: required free scalar; explicit/implicit reorder not beneficial |
| `(hB : 0 ≤ B)` | proposition | scalar monotonicity | weakest sign assumption already; cannot drop: B=-1, one variable r=2,x=1 yields false -3≤-4; no strict-to-weak change possible |
| `(x : σ → ℝ)` | data | absolute powers both sides | cannot drop without statement change; already arbitrary coordinatewise function, no global predicate to point-localise |

Private signature drop verified by scratch compilation and complete native final diagnostics.
Abstract ℝ→ordered ring is a different signature family and requires generalizing same-file
`geom_sum_le_one_add_pow`; no such cross-declaration/public restatement made. Inversion check:
`box` appears only in normalization; generic Cartesian distributivity already covers that
abstract equality. Remaining inequality additionally needs the same-file geometric bound;
adding an arbitrary-bound wrapper would just rename existing monotonicity. No extra API added.
Literature status: n/a, private decl; literature search not required. Big-change flags: none.

## Step 2.7: line packing

Native hover confirms no DecidableEq in final type. Width reference uses
`set_option format.width 100 in #check @sum_box_prod_pow_le_aux` in isolated verification.

| Signature line | Codepoints | Next complete token | Arithmetic | Action |
|---|---:|---|---|---|
| 209 | 98 | `∑ k ∈ box r, B * ∏ j, ∣x j∣ ^ k j` (33 codepoints; actual source uses ASCII absolute bars) | 98 + 1 + 33 = 132 > 100 | ok |
| 210 | 72 | none, proof next | n/a | ok |

The final first line contains every binder and colon. Scope command L208 is 24 codepoints
and is not a theorem-signature line; it must remain a preceding command.

## Step 2.8: inequality scan

| Location | Original/final | Rewrite | Rename |
|---|---|---|---|
| hB, L209 | `0 ≤ B` | none | none |
| conclusion, L210 | sum `≤` scalar product | none | none |
| reverse inequalities | no `≥`/`>` in signature or explicit hypotheses | n/a | n/a |

## Step 3: all 42 golfing rules

- [1.1] n/a: no by-exact wrapper.
- [1.2] n/a: no by-rfl.
- [1.3] n/a: no rw/exact chain.
- [1.4] applied: terminal simp equality and inequality composed by simpa using.
- [1.5] n/a: no trailing rfl.
- [1.6] n/a: no constructor.
- [1.7] n/a: no apply/exact pair.
- [1.8] n/a: no contradiction.
- [1.9] n/a: bound depends on j and ignores a membership argument, not eta-reducible.
- [1.10] n/a: no have.
- [1.11] n/a: no apply/intro.
- [1.12] n/a: no show.
- [1.13] n/a: no projected have.
- [1.14] n/a: no consecutive rewrites.
- [1.15] n/a: terminal simp originally already unsqueezed.
- [1.16] n/a: no nonterminal bare simp.
- [1.17] n/a: no beneficial receiver argument on finite-set monotonicity.
- [1.18] n/a: grouping belongs to first argument of binary scalar monotonicity.
- [1.19] n/a: no push_neg.
- [1.20] n/a: no existential.
- [2.1] tried native grind: fails with negated sum bound and no contradiction.
- [2.2] n/a: no preexisting grind.
- [2.3] applied: direct simpa composition, explicit s := univ required.
- [2.4] n/a: no function-property goal.
- [2.5] retained actual working positivity for each power-sum nonnegativity.
- [2.6] actual independent scratch gcongr proof checked; final named product lemma shorter and explicit.
- [2.7] n/a: real finite-sum inequality, no Nat/Int arithmetic subgoal beyond existing geometric lemma.
- [2.8] tried native aesop: made no progress.
- [2.9] n/a: no concrete arithmetic or cross-type casts.
- [2.10] n/a: variables are arbitrary functions/reals, not closed finite computation.
- [2.11] n/a: no fractions or ring identity.
- [2.12] n/a: no terminal ring/ring_nf.
- [2.13] n/a: no symmetric cases.
- [2.14] applied: equality-plus-inequality calc collapsed into simpa using monotonicity.
- [2.15] n/a: no repeated parallel goals.
- [3.1] n/a: no erw.
- [3.2] n/a: no continuity/measurability tactic.
- [3.3] n/a: no omega.
- [3.4] n/a: no cases/substitutions.
- [3.5] n/a: private single-caller bound not a simp normal form.
- [3.6] n/a: no simp_all only.
- [3.7] n/a: no maxHeartbeats option.

## Step 4: holistic reflection / simplify

Whole-goal grind/simp/aesop/exact? do not solve the theorem. `apply?` finds partial order
facts, not a complete proof. `simp [box]` only unfolds the box. The direct composition is
shorter than the initial calc and retains clear dependencies. No one-use have or duplicated
branch remains. A bare direct simpa initially failed because its product index set was an
unconstrained metavariable; `(s := Finset.univ)` fixes this without an ascribed intermediate.
Built-in `/simplify` capability is not exposed in this environment: performed its reuse,
quality and efficiency review in-thread; PASS-THROUGH after the documented direct composition.
No further changes proposed. Filewide simplify integration remains with fileowner.

## Step 5: verification and gates

Native full-file diagnostics at final source: `partial=false`, `success=true`,
`timed_out=false`, `failed_dependencies=[]`, zero errors and zero target-range warnings.
Module command `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm` exited 0,
`Built Roth.CoeffNorm (15s)`, 1658 jobs. Whole-project/separate dependent builds are
fileowner-owned and are not laundered as this worker's independent checks.
Native `lean_verify` target `Roth.sum_box_prod_pow_le_aux`: trust standard,
axioms exactly `[propext, Classical.choice, Quot.sound]`, no warnings/custom axioms.


### Isolated original-type and independent proof evidence

`/Users/ramin/.elan/bin/lake env lean /private/tmp/box-helper-verify.lean` exited 0.
Scratch imports built `Roth.CoeffNorm`, copies the exact frozen private helper body/signature
under a scratch private name (private imported names are not source-accessible), checks its
type at `format.width 100`, then assigns it to the original helper type including arbitrary
`[instD : DecidableEq σ]`. Required transport is explicit:

```lean
  classical
  cases Subsingleton.elim instD (Classical.decEq σ)
  exact sum_box_prod_pow_le_aux r hB x
```

The naive `exact` and `simpa [box]` attempts failed because `box`/`piFinset` still carry the
DecidableEq argument in their elaborated terms; this was detected and resolved rather than
claimed definitionally equal. DecidableEq subsingleton elimination proves the original
statement for every old instance. Actual live helper axioms checked separately by native
`lean_verify` above.

The same scratch contains `box_independent`, a genuinely nonself reproof: finite-product
monotonicity by `gcongr`, direct binomial expansion (`add_pow`) and positivity of binomial
coefficients (`Nat.choose_pos`). It calls neither `sum_box_prod_pow_le_aux` nor
`geom_sum_le_one_add_pow`. Its compiled `#print axioms` output is exactly:
`[propext, Classical.choice, Quot.sound]`. Log: `/private/tmp/box-helper-verify.log`.

### Gate status

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual `lake build Roth.CoeffNorm`, exit 0, 15s |
| definition_protected | pass | worker-start snapshot diff changes no def/abbrev |
| theorem_statement_protected | pass, scoped weakening | only private DecidableEq removed as documented item18; all public types unchanged, old type recovered in compiled scratch |
| structure_gate | pass | four proof lines, no ∧ or branches |
| naming_gate | pass | descriptive private `_aux`, no forbidden token; no rename |
| line_packing_gate | pass | every signature line in exact codepoint table |
| inequality_orientation_gate | pass | per-occurrence table, zero ≥/> |
| no-trust-downgrade | pass | native actual helper and independent scratch use standard three axioms |
| comments/header protected | pass | snapshot diff only helper code/scope; no prose changes |
| cumulative_no_unintended_breakage | pass (fileowner evidence) | full + separate `Roth.LeanEval` builds session13387 exit0; logs `/private/tmp/roth-coeffnorm-helper-box-{full,leaneval}.log` |

Overall: pass. Fileowner independently ran cumulative builds; no Git work performed by worker.

## Buzz pass

Outcome: FAST-BOARD, budget 1000ms. Native `lean_profile_proof` extraction failed (drops
same-file geometric lemma and local Classical scope); corrected imported scratch profiling
retains the exact declaration code and adds declaration-scoped profiler options only in /tmp.
Commands `lake env lean /private/tmp/box-helper-profile-before.lean` and
`lake env lean /private/tmp/box-helper-profile.lean` both exited 0. Sum of all cumulative
reported categories: before 149.656ms, after 317.814ms; each category and the conservative
sum are below 1000ms. Final main categories: typeclass inference 162ms, simp 100ms,
tactic execution 35.8ms. These are profiling-category totals, not claimed whole-process
wall times, and no speedup is claimed. No over-budget declaration or fix requiring tracing.
No limit raises removed/added, no profiling scaffolding in source, no deferral.
Logs: `/private/tmp/box-helper-profile-before.log`, `/private/tmp/box-helper-profile.log`.

## Result and eleven required checks

Before: 11 lines; after: 7 including local-scope command (saved 4). Issues found/fixed: 3/3.
Rules applied: 1.4, 2.3, 2.14. Generalisation: removed private decidability parameter.
Renames queued: none. Comments preserved: all; none inside helper. Refactoring needed: none.

- [x] Step 1: reference docs read.
- [x] Step 2: full 24-item audit recorded.
- [x] Step 2.5: all five actual mathlib searches recorded.
- [x] Step 2.6: every binder assessed, private instance weakening compiled.
- [x] Step 2.7: every signature line measured and packed.
- [x] Step 2.8: complete inequality scan recorded.
- [x] Step 3: all 42 golfing rules have explicit statuses.
- [x] Step 4: automation alternatives and independent holistic reflection completed.
- [x] Step 5a: complete final native diagnostics clean, no partial elaboration.
- [x] Step 5b: actual module build, original-type assignment, independent nonself proof,
  standard axioms and diff gates pass.
- [x] Step 6a: naming clean; no rename sidecar needed.

Source hash stayed frozen after revocation. No original cleanup tally increment.
