# Cleanup: `Roth.card_filter_fiber_eq`

Scope: private declaration only, `Roth/Lattice.lean`; no rename, public API, documentation,
header, import, version, or mathematical changes. Original 11 lines → 10 lines; body 5 → 4.

Read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md,
cleanup-gates.md in full; Phase-4 worker prompt, Lean skill, mathlib-quality skill, relevant
style/naming sections read. Baseline supplied by file owner: d08 full and separate LeanEval
both exit 0, logs `/private/tmp/roth-lattice-d08-{full,leaneval}.log`.

## Full 24-item audit

| Item | Finding/action |
|---|---|
| 1 LINT | Final complete LSP recorded below; header warning is pre-existing and user-preserved. |
| 2 HAVE SCAN | No have declarations. |
| 3 SET_OPTION | None; no limits added. |
| 4 SIMP SQUEEZE | No simp calls. |
| 5 NAMING | Descriptive snake_case; no forbidden abbreviations/patterns; no rename. |
| 6 LINE PACKING | All six signature lines measured below, structural expression boundaries. |
| 7 BY PLACEMENT | `:= by` ends the last signature line. |
| 8 FORMAT | Three ordinary lambda arrows converted to ↦; continuation indents normalized. |
| 9 COMMENTS | No comments in target; all file comments preserved. |
| 10 DOCSTRING | Private helper has no docstring. |
| 11 VISIBILITY | Already private, only file-local caller. |
| 12 STRUCTURE | Four proof lines, no conjunction or long branch. |
| 13 MATHLIB | All five actual searches below; use existing filter_congr. |
| 14 JUNK DEF | n/a: lemma. |
| 15 EXISTS LEMMA | n/a: no existential conclusion. |
| 16 SHOW | None. |
| 17 PUSH_NEG | None. |
| 18 GENERALISE | Four parameter drop probes below; no assumptions to weaken. |
| 19 INEQUALITY | Two ≤ predicates; no reverse inequalities. |
| 20 NORMAL-FORM | Cardinal equality is the form used by sum_congr; weight decomposes via existing API. |
| 21 SYNTAX-GEN | Current caller consumes exact real-cardinality equality; no beneficial restatement. |
| 22 IMPORT-FANOUT | n/a: no imports added. |
| 23 CASTS | 0 dropped; 5 explicit Nat→Real coercions kept; inner Nat ascription pins original sum type. |
| 24 INSTANCE-NAME | n/a: not an instance. |

Issues fixed: lambda syntax, continuation alignment, arithmetic proof automation.
Refactoring needed: none. Optional abstract weight/field API closed: it would change fixed
project definitions and has no benefit for the existing caller.

## Mathlib search-status

All searches actually invoked during this worker session:

| Method | Query | Result |
|---|---|---|
| A Lean-Finder | Finset filter equality when predicates equivalent on members | filter_congr, filter_inj, filter_inj' |
| B Loogle | `Finset.filter, (_ ↔ _)` | filter_eq_self, filter_nonempty_iff, filter_eq_empty_iff |
| C LeanSearch | Finset filter congruence predicates equivalent | filter_congr, filter.congr_simp, filter_inj' |
| D source rg | `theorem filter_congr\|lemma filter_congr\|card_filter_fiber_eq` | Finset/Filter.lean:176, Multiset/Filter.lean:53; local target and caller |
| E local name | `filter_congr` | Finset/Multiset/List/Array variants; source results, index unavailable |

Partial match: `Finset.filter_congr`, already used and retained. Auxiliary variants checked:
filter_congr_decidable, filter_inj, filter_inj', filter.congr_simp. Common-equivalents table:
no matching discrete/finite/metric bucket. No claim of global absence is made; this lemma
also uses three project weight lemmas and a real arithmetic identity, beyond a 1–3-call
mathlib wrapper. `exact?` actually failed on the original predicate-equivalence goal.

Six strict rules considered: no duplicated mathlib result, all five searches performed,
auxiliary variants checked, no custom class predicate, no equivalent to delete, no new
mathlib reliance requiring documentation changes.

## Generalisation status

Compiled `/private/tmp/fiber_drops.lean` with `autoImplicit false`, removing one binder per
clone. Exit 1 with unknown identifier for each removed binder (n, r, lam, i), as expected;
failed scratch probes introduce no project declarations.

| Parameter | Class | Use | Mechanical probes | Result |
|---|---|---|---|---|
| `{n : ℕ}` | value/index | Fin n, Fin.last n, castSucc | drop → unknown n; concrete abstraction requires changing weight/box API | retain |
| `r : Fin (n+1) → ℕ` | function value | both boxes and all weight denominators | drop → unknown r; no proposition to localise | retain |
| `lam : ℝ` | value | both thresholds | drop → unknown lam; field abstraction blocked by real-valued weight | retain |
| `i : ℕ` | value | single coordinate and real shift | drop → unknown i; type fixed by Nat-valued Finsupp | retain |

No typeclass, decidability, proposition, strictness, or universe parameters occur, so their
catalogue weakenings do not apply. Inversion check: generic filter congruence is already
used; remaining algebra is project-weight decomposition plus threshold identity. A new
single-use abstraction provides no current caller benefit. Big-change candidates: none.
Literature: n/a, private declaration; literature search not required.

## Line packing

Width-100 `#check @fiber_nopush` (independent clone of original exact type):

```lean
@fiber_nopush : ∀ {n : ℕ} (r : Fin (n + 1) → ℕ) (lam : ℝ) (i : ℕ),
  ↑(#({d ∈ box (r ∘ Fin.castSucc) |
          weight r (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last n) i) ≤ (↑(n + 1) - lam) / 2})) =
    ↑(#({d ∈ box (r ∘ Fin.castSucc) | weight (r ∘ Fin.castSucc) d ≤ (↑n - (lam - 1 + 2 * ↑i / ↑(r (Fin.last n)))) / 2}))
```

The printer's Unicode card notation renders differently from source. Source expressions
retain original exact types. Next token means the next complete structural expression,
not an arbitrary identifier split inside parentheses.

| Sig line | Chars | Next expression | Arithmetic | Action |
|---|---:|---|---|---|
| 141 | 84 | filter prefix through `weight r` (50) | 84 + 1 + 50 = 135 > 100 | ok |
| 142 | 54 | extended Finsupp argument (58) | 54 + 1 + 58 = 113 > 100 | ok |
| 143 | 66 | cast threshold/card equality tail (42) | 66 + 1 + 42 = 109 > 100 | ok |
| 144 | 50 | RHS filter prefix through ≤ (71) | 50 + 1 + 71 = 122 > 100 | ok |
| 145 | 77 | RHS threshold/card/`:= by` (73) | 77 + 1 + 73 = 151 > 100 | ok |
| 146 | 81 | proof body next | n/a | ok |

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | first filter | weight … ≤ threshold | already forward | none |
| 2 | second filter | weight … ≤ shifted threshold | already forward | none |
| — | signature | no ≥ or > | n/a | none |

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 | n/a: no by-exact wrapper |
| 1.2 | n/a: no by-rfl |
| 1.3 | n/a: rw followed by arithmetic, not exact |
| 1.4 | n/a: no simp/exact sequence |
| 1.5 | n/a: no trailing rfl |
| 1.6 | Original constructor branches require arithmetic; replaced by grind |
| 1.7 | n/a: no apply/exact sequence |
| 1.8 | n/a: no contradiction/push-neg |
| 1.9 | n/a: lambdas contain actual predicates, not eta wrappers |
| 1.10 | n/a: no have |
| 1.11 | Existing refine/filter_congr lambda already direct |
| 1.12 | n/a: no show |
| 1.13 | n/a: no projected have |
| 1.14 | Existing four rewrite lemmas already merged |
| 1.15 | n/a: no terminal simp only |
| 1.16 | n/a: no nonterminal simp |
| 1.17 | n/a: no useful receiver method simplification |
| 1.18 | n/a: no avoidable outer application parentheses |
| 1.19 | n/a: no push_neg |
| 1.20 | n/a: no existential lemma |
| 2.1 | Whole hinted grind actually failed; terminal grind succeeded |
| 2.2 | Deleted push_cast before terminal grind; independent exact-type clone compiled |
| 2.3 | Actual simp weight-decomposition probe left arithmetic; no consolidation |
| 2.4 | n/a: no function-property goal |
| 2.5 | n/a: iff between arbitrary threshold inequalities, not positivity |
| 2.6 | n/a: cardinal equality and iff, no monotonicity subgoal |
| 2.7 | n/a: remaining arithmetic is real; Nat cast handled by grind |
| 2.8 | Actual aesop failed; left both real inequality directions |
| 2.9 | Cast normalization subsumed by grind; no concrete numerical goal |
| 2.10 | n/a: arbitrary real predicate, not finite computation |
| 2.11 | n/a: no field equality goal; clearing r needs zero split unnecessarily |
| 2.12 | n/a: no ring/ring_nf goal with hypotheses |
| 2.13 | n/a: no symmetric case split |
| 2.14 | n/a: no calc |
| 2.15 | constructor/introduction chain subsumed entirely by grind |
| 3.1 | n/a: no erw |
| 3.2 | n/a: no continuity/measurability |
| 3.3 | n/a: no omega |
| 3.4 | n/a: no rcases-rfl |
| 3.5 | No attributes needed for private one-use helper |
| 3.6 | n/a: no simp_all only |
| 3.7 | No maxHeartbeats/maxRecDepth limits |

Step-back: keep explicit congruence and named weight rewrites; grind handles cast and exact
iff arithmetic in one step. Direct terminal linarith failed because it does not split iff;
whole hinted grind failed at card/filter equality; aesop left arithmetic unresolved.

## Verification and gates

Module build passed: `/Users/ramin/.elan/bin/lake build Roth.Lattice`, exit 0, 58s
(module job); only the user-preserved header warning. Independent final original-type clone
`/private/tmp/fiber_exact_original.lean` passed exit 0 after module build, without referencing
the target; `#print axioms` gave `[propext, Classical.choice, Quot.sound]`. Actual private
`Roth.card_filter_fiber_eq` verified through direct `lean_verify`: standard trust, precisely
those three axioms, no nonstandard axioms, no source warnings. Final complete LSP via persistent direct session 42366 passed: `partial=false`,
`success=true`, `timed_out=false`, no failed dependencies. Only warning: preserved header
at line 1. Earlier partial one-shot calls were not counted as passes. The independent `/private/tmp/fiber_nopush.lean` already compiled
exit 0 without referring to the target; it established the final proof on the original type.
No sorry/new axiom/limit/suppression/import was introduced. Whole-project build and separate
LeanEval remain file-owner obligations after explicit freeze.

## Worker phase checklist

- [x] Step 1 references read.
- [x] Step 2 all 24 audit items.
- [x] Step 2.5 five actual searches.
- [x] Step 2.6 every parameter mechanically probed.
- [x] Step 2.7 six-line packing table and width-100 check.
- [x] Step 2.8 inequality table.
- [x] Step 3 all 42 rules.
- [x] Step 4 holistic reflection.
- [x] Step 5a complete LSP clean (only preserved header warning).
- [x] Step 5b all diff gates.
- [x] Step 6a no rename necessary.

## Gate status — Phase 4

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual `/Users/ramin/.elan/bin/lake build Roth.Lattice`, exit 0, module 58s |
| definition_protected | pass | target-only edit, no def/abbrev lines changed |
| theorem_statement_protected | pass | whitespace/↦ only in signature; original exact-type clone independently compiled |
| structure_gate | pass | four proof lines, no conjunction or long branch |
| naming_gate | pass | descriptive snake_case; no forbidden pattern |
| line_packing_gate | pass | six measured signature lines and width-100 #check above |
| inequality_orientation_gate | pass | two forward ≤, zero ≥/> |
| cumulative_no_unintended_breakage | pass at module scope | private target, sole in-file caller compiled in Roth.Lattice |
| docstring_only_changes | n/a | proof cleanup scope |
| complete_LSP | pass | partial=false/success=true, no failed dependencies |
| trust | pass | actual private theorem and independent clone use only standard three axioms |

Overall worker gates: PASS. Source frozen at
`00bedd0a4607a8fa4017206e750d8827f2b5c672ec116b8664093d1b386bfbea`.
No rename/decomposition/generalisation/API action remains open. File-owner final whole-project
build, separate LeanEval, simplify and actual performance sweep remain orchestration duties.

Owner checkpoint: explicit source edit revocation before sequential full/separate LeanEval session72585; both exit0 (70.69s/28.67s), frozen hash stable. Logs `/private/tmp/roth-lattice-d09-{full,leaneval}.log`.
