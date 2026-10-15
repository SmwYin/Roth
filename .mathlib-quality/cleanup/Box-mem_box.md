# Declaration cleanup: `Roth.mem_box`

Dedicated Phase-4 worker, baseline commit `13b99bb`; scope `Roth/Box.lean:47–48` and this report only. All required reference documents were read: golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, relevant style-rules, and the full supplied worker prompt. The Lean 4 skill was applied. Existing API and docstring were preserved.

## Step 2 — Full audit

1. **LINT:** No warning/error at this declaration. Complete final LSP reports only the preexisting header and later-declaration warnings.
2. **HAVE SCAN:** None; the entire body is one terminal `simp`.
3. **SET_OPTION:** None in declaration or diff.
4. **SIMP SQUEEZE:** Existing terminal `simp [box, Finset.mem_map_equiv, Nat.lt_succ_iff]` stays unsqueezed. Live testing proves the explicit `Finset.mem_map_equiv` argument redundant; remove it.
5. **NAMING:** `mem_box` describes membership in the named `box` construction, follows snake_case membership naming, and matches no forbidden numerical pattern, single-letter name, or abbreviation. No rename warranted or queued.
6. **LINE PACKING:** Single signature line, 75 codepoints; complete measured table below. No repack needed.
7. **BY PLACEMENT:** `by` ends signature line 47.
8. **FORMAT:** Two-space tactic indentation, one tactic, no interior blank lines or trailing whitespace, no `haveI`/`letI`.
9. **COMMENTS:** No inline proof comments; existing one-line docstring preserved byte-for-byte.
10. **DOCSTRING:** Existing statement-oriented sentence explains coordinatewise membership and includes source attribution; no proof sketch to relocate.
11. **VISIBILITY:** Public API used externally in Taylor, CoeffNorm, Lattice, MainLemma, and Main. Keep public.
12. **STRUCTURE:** One proof-body line, no conjunction in statement, no branches. No extraction or decomposition needed.
13. **MATHLIB:** Generic product/map/range membership API already provides the proof ingredients. Five-method search and compiled direct-reuse probes below. Keep this API for the preserved project-specific `Roth.box`; no exact replacement for its full statement was found by `exact?`. No coset or global decidability anti-pattern.
14. **JUNK DEF:** n/a: theorem, not a definition.
15. **EXISTS LEMMA:** n/a: public membership equivalence, not an existential helper.
16. **SHOW vs CHANGE:** n/a: neither occurs.
17. **PUSH_NEG:** n/a: none occurs.
18. **GENERALISE:** All five elaborated parameters considered and drop-tested; no small-safe weakening preserves the existing box expression. Full table and literature search below.
19. **INEQUALITY:** One `≤` in conclusion; no reversed comparison. Required table below.
20. **NORMAL-FORM:** Already canonical membership-to-coordinate-bound equivalence; natural successor strict bounds reduce to `≤` on RHS.
21. **SYNTAX-GEN:** OK: implicit `r` and `d` are inferred from the membership expression; equivalence supports `.1`, `.2`, `rw`, and `simp` at existing callers. No restatement proposed.
22. **IMPORT-FANOUT:** n/a: no imports changed or added.
23. **CASTS:** 0 dropped / 0 kept as cross-type / 0 kept as load-bearing; no coercions or type ascriptions in the diff.
24. **INSTANCE-NAME:** n/a: theorem, no named instances introduced.

Issues found: one redundant explicit simplifier argument; fixed. Refactoring needed: none. No public deletion or generalisation is proposed.

## Step 2.5 — Mathlib search status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `Membership in finite product of finite sets iff each coordinate belongs to corresponding finite set` | `Fintype.mem_piFinset`, `Finset.mem_pi`, `Finset.mem_product` |
| B Loogle | `Fintype.piFinset, _ ∈ _` | `Fintype.mem_piFinset` plus filtered-product variants |
| C LeanSearch | Product membership natural-language search | Unavailable: parent established repeated service HTTP 500 failures; per explicit handoff instruction, not retried. This is not evidence of absence. |
| D Source | Full untruncated searches for `mem_box`, `mem_map_equiv`; product/range membership sources | `Fintype.mem_piFinset` in Data/Fintype/Pi:37; `Finset.mem_map_equiv` in Data/Finset/Image:74; `Finset.mem_range_succ_iff` in Data/Finset/Range:98. Other `mem_box` names concern Behrend's uniform function box or unrelated geometric boxes. |
| E Local name search | `mem_piFinset` | Returned generic product membership and `Fin.mem_piFinset_iff_last_init`, `_zero_tail`, `_pivot_removeNth`; index warming, positive source hits used, not a negative absence claim. |

Initial source search named nonexistent Data/Finset/Map.lean; corrected with the whole-source full-name search locating Data/Finset/Image.lean. Every retained/considered concrete building-block name was compiler-checked with `#check` (`Finset.mem_map_equiv`, `Fintype.mem_piFinset`, `Finset.mem_range_succ_iff`). Auxiliary variants investigated: dependent `Finset.mem_pi`, tuple last/init and zero/tail, filtered products, range successor. Common-equivalents lookup: no listed bucket applies; generic product membership is the matching abstraction.

Conclusion: partial generic match already used by simplification. `exact?` failed at the live pre-proof position; `apply?` suggested only generic Iff scaffolds with remaining goals, not a completed proof. The local statement mentions preserved `Roth.box`, including the Finsupp transport and nonuniform bounds; retaining this membership API avoids exposing that implementation to many callers. This is not a claim that generic product membership is absent from mathlib. No new wrapper/API was added.

## Step 2.6 — Generalisation status

All probes were isolated `lean_run_code` examples; none modified the public statement. Drop probes explicitly used `autoImplicit false` for value/type binders so Lean could not silently recreate them.

| Parameter | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|
| `{σ : Type*}` | type variable | Index of `r`, `d`, box | Drop; universe audit | Yes: unknown `σ` when dropped | Retain; already universe-polymorphic `Type u_1` |
| `[Fintype σ]` | typeclass | Required in `Roth.box` signature | Drop; weaken to `[Finite σ]` | Yes: both fail to synthesize `Fintype σ` in statement | Retain; obtaining a chosen Fintype changes the box expression/API |
| `[DecidableEq σ]` | decidability | Required in `Roth.box` signature | Drop | Yes: fails to synthesize `DecidableEq σ` in statement | Retain; local `classical` in proof does not supply a statement instance |
| `{r : σ → ℕ}` | structure value | Bounds both sides | Drop | Yes: unknown `r` in box and bound | Retain; changing bound codomain changes the construction |
| `{d : σ →₀ ℕ}` | structure value | Membership element and coordinates | Drop | Yes: unknown `d` on both sides | Retain; replacing by a function changes public argument type |

No proposition hypotheses exist, so strict-to-weak, global-to-pointwise, and conjunction unbundling passes have no candidate. No algebra/analysis structures exist to weaken. No universe restriction remains. Inversion check: unfolding box exposes the generic finite-product membership theorem already available as `Fintype.mem_piFinset`; the proof has no independent abstract remainder needing extraction. General finite families are supported by mathlib already, so no duplicate general companion is warranted. Big-change candidates: none proposed.

### Literature search

Web query: `Cartesian product finite sets membership coordinatewise generalization`. Top three captured hits:

1. [Duke discrete mathematics — Sets](https://donaldlab.cs.duke.edu/Teaching/discretemath/Online/handouts/sets.revised2.shtml): product membership is given by component membership.
2. [Generalized Union, Intersection and Cartesian Product](https://www.sciencedirect.com/science/chapter/bookseries/abs/pii/S0049237X08710577): arbitrary-family generalisation; search-result abstract only, no claim to have read the book chapter.
3. [Applied Combinatorics — Cartesian Products](https://appliedcombinatorics.org/book/s_background_products.html): extends the coordinate membership description to finite families.

The elementary coordinatewise formulation supports the current mathematical statement. General finite-family membership already exists in the compiler-checked `Fintype.mem_piFinset`; literature does not reveal a needed additional hypothesis weakening. ChatGPT math MCP: n/a, no such callable tool in the tool inventory. Literature-driven big changes: none.

## Step 2.7 — Line packing

Actual `#check @Roth.mem_box` with `format.width 100`:

```lean
@Roth.mem_box : ∀ {σ : Type u_1} [inst : Fintype σ] [inst_1 : DecidableEq σ] {r : σ → ℕ} {d : σ →₀ ℕ},
  d ∈ Roth.box r ↔ ∀ (j : σ), d j ≤ r j
```

The source uses section binders; its one signature line is fully present and measured using Python `len` (Unicode codepoints).

| Sig line | Chars | Next signature token | current + 1 + next ≤ 100? | Action |
|---|---:|---|---|---|
| 47 | 75 | None; body follows after `:= by` | n/a: no signature break exists | ok |

Before and after table are identical; no repack rows. Final proof line is 29 codepoints (previously 51).

## Step 2.8 — Inequality scan

| # | Location | Original | Rewrite | Rename? |
|---|---|---|---|---|
| 1 | L47 RHS | `d j ≤ r j` | None; already smaller-side-left | No |
| — | Entire signature and hypotheses | No `≥` or `>` | n/a | Name has neither `_ge_` nor `_gt_` |

## Step 3 — All golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: no exact wrapper |
| 1.2 by rfl | n/a: no rfl wrapper; live `rfl` replacement fails |
| 1.3 rw + exact | n/a: neither chain exists |
| 1.4 simp + exact | n/a: simp already closes |
| 1.5 trailing rfl | n/a: no trailing tactic |
| 1.6 constructor + exact | n/a: no constructors |
| 1.7 apply + exact | n/a: no apply chain |
| 1.8 by_contra + push_neg | n/a: no contradiction proof |
| 1.9 eta lambdas | n/a: no proof lambdas |
| 1.10 single-use have | n/a: no have |
| 1.11 apply + intro | n/a: no introductions |
| 1.12 redundant show | n/a: no show |
| 1.13 have + projections | n/a: no have or projections |
| 1.14 merge rw | n/a: no rewrites |
| 1.15 terminal simp only | Already unsqueezed terminal simp; remove redundant explicit map-membership argument after successful test |
| 1.16 nonterminal simp | n/a: sole simp is terminal |
| 1.17 dot notation | n/a: no explicit theorem application needing dot notation |
| 1.18 trailing parentheses | n/a: no such applications |
| 1.19 push_neg | n/a: none |
| 1.20 single-use existential | n/a: no existential |
| 2.1 grind | Tried bare and with `[box, Finset.mem_map_equiv, Nat.lt_succ_iff]`; both fail, keep simp |
| 2.2 delete before grind | n/a: no grind retained or preceding tactics |
| 2.3 simpa consolidation | n/a: no subsequent closing step; terminal simp already one tactic |
| 2.4 fun_prop | n/a: no regularity property |
| 2.5 positivity | n/a: goal is an iff, not positivity/nonnegativity |
| 2.6 gcongr | n/a: no monotone inequality chain |
| 2.7 lia/omega | Tried `lia` because RHS compares naturals; fails on opaque box membership. No arithmetic step remains after successful simp, so omega not introduced |
| 2.8 aesop | Tried; leaves membership/bound implications unsolved |
| 2.9 norm_num/norm_cast | n/a: no concrete arithmetic computation or casts |
| 2.10 decide | Tried; fails because expected type has free variables; no closed finite computation |
| 2.11 field_simp; ring | n/a: no denominators or algebraic identity |
| 2.12 linear_combination | n/a: no ring-ending proof or algebra hypotheses |
| 2.13 symmetric wlog | n/a: no case branches |
| 2.14 collapse calc | n/a: no calc |
| 2.15 shared goals | n/a: no retained branching tactics |
| 3.1 erw → rw | n/a: no erw |
| 3.2 continuity/measurability | n/a: no legacy property tactic |
| 3.3 omega → lia | n/a: no omega; lia tested under 2.7 |
| 3.4 rcases rfl | n/a: no rcases |
| 3.5 automation attributes | Considered; caller-driven rewrite theorem already usable with `simp [mem_box]`; changing global simp normal form is unnecessary and outside proof-only cleanup |
| 3.6 simp_all | n/a: no simp_all only or hypotheses to combine |
| 3.7 heartbeat options | n/a: no options |

## Step 4 — Reflection and actual experiments

Live goal at L48 is exactly the declared membership equivalence. The existing proof closes it in one tactic. `rfl` fails definitional equality. `simp [box]` leaves the equivalence between coordinatewise `< r a + 1` and `≤ r a`. Adding only `Nat.lt_succ_iff` closes. The original three-argument simp also closes. Bare/hinted grind, aesop, and lia fail; decide rejects the free variables. `exact?` finds no completed proof. `apply?` returns generic Iff scaffolds, explicitly not solutions. There are no haves to compose, branches to extract, or redundant tactic steps. Removing the redundant map lemma improves clarity without changing the proof strategy or introducing automation churn. No new public lemma, attribute, definition, or import was needed.

## Step 5 — Verification and gates

Final native `lean_diagnostic_messages` on the entire file: `success=true`, `partial=false`, `timed_out=false`, no failed dependencies or errors, and no target warnings. Header and later-declaration warnings are preexisting and belong to their file/declaration workflows.

Actual command `/Users/ramin/.elan/bin/lake build Roth.Box > /private/tmp/roth-box-d02-module.log 2>&1`, execution session `73593`, exited **0**, final line `Build completed successfully (1154 jobs).` Parent handles full project/dependent checkpoints.

Isolated `lean_run_code` example of the final proof compiled successfully, with unchanged full type printed at width 100. Scratch import emitted an out-of-date-import informational notice while the module rebuild was in flight; complete live-file diagnostics and the completed module build independently verify the changed source. Native `lean_verify` after module completion returned `trust=standard`, axioms `[propext, Classical.choice, Quot.sound]`, `non_standard_axioms=[]`, `warnings=[]`.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module command/session above exited 0 |
| definition_protected | pass | Exact diff changes only the simp body, no def/abbrev lines |
| theorem_statement_protected | pass | Signature and all five elaborated parameters unchanged |
| structure_gate | pass | One-line body, no conjunction or branches |
| naming_gate | pass | Descriptive snake_case; no forbidden pattern/abbreviation |
| line_packing_gate | pass | Complete measured single-row table, 75 codepoints, no breaks |
| inequality_orientation_gate | pass | Complete table; no reversed comparisons or `_ge_`/`_gt_` |
| isolation | pass | Native standalone final-proof example compiles |
| type | pass | Compiler-printed full type unchanged |
| axioms/source | pass | Native verify standard trust and empty warning list |
| comments/docstrings | pass | Existing docstring unchanged; no proof comments existed |
| whitespace | pass | `git diff --check -- Roth/Box.lean` exits 0 |

Overall: **pass**.

## Step 6 — Result and checklist

Before: 2 declaration lines / 1 body line. After: 2 declaration lines / 1 body line. Saved: 0 lines, 22 characters. Audit issues found: 1; fixed: 1. No renames queued, no refactoring needed, no outstanding proposal. Applied terminal-simp maintenance associated with rule 1.15; all 42 rules considered above. Docstring preserved; no proof comments present. Source ownership released to the parent for its dependent builds and publication checkpoint.

- [x] Step 1 — full required references and worker prompt read.
- [x] Step 2 — all 24 audit items answered.
- [x] Step 2.5 — five-method search block and compiled reuse probes.
- [x] Step 2.6 — all elaborated parameters/drop tests, inversion and literature checks.
- [x] Step 2.7 — complete codepoint width table.
- [x] Step 2.8 — complete inequality table.
- [x] Step 3 — all 42 rules individually recorded.
- [x] Step 4 — proof strategies tested and reflected on.
- [x] Step 5a — complete full-file native LSP succeeds.
- [x] Step 5b — module build, diff and type/isolation/axiom gates pass.
- [x] Step 6a — no rename warranted; sidecar untouched.

Publication verification for `Roth.mem_box`: full `lake build` session 29589 exited 0
(2586 jobs; `/private/tmp/roth-box-d02-full.log`); separate `lake build Roth.LeanEval`
session 68459 exited 0 (2585 jobs; `/private/tmp/roth-box-d02-leaneval.log`).
