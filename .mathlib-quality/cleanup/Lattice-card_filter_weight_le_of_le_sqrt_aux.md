# Phase 4 — `Roth.card_filter_weight_le_of_le_sqrt_aux`

Scope: only the private helper at original L152–159, now L152–158, and this report.
Initial HEAD supplied by owner: `7536ea6`; baseline full/separate checks supplied by owner:
exit 0, 6.37s/3.15s, `/private/tmp/roth-lattice-d10-packed-{full,leaneval}.log`.
No Git operations, shared-progress writes, or original-264 count increment performed.

## References and comprehension

Read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md,
cleanup-gates.md; full Phase-4 prompt; relevant formatting, visibility, cast, inequality,
helper-name and forbidden-abbreviation sections of style-rules.md/naming-conventions.md.
Read lean4/SKILL.md and mathlib-quality/SKILL.md.

Mathematics: the filtered box has at most the full box's cardinality; the full box has
cardinality `∏ j, (r j + 1)`; the factor `2 * √m / lam` is at least one when
`0 < lam ≤ 2 * √m`. No positivity premise on `r` is used or introduced.

## Full audit (24 items)

| Item | Finding and action |
|---|---|
| 1 LINT | Complete initial/final LSP: no target warnings/errors. Existing file header warning at L1 preserved by user instruction. |
| 2 HAVE SCAN | No `have` declarations. |
| 3 SET_OPTION | No declaration options or limits. |
| 4 SIMP SQUEEZE | Initial `rw; push_cast; rfl` replaced by terminal unsqueezed `simp [card_box]`; no nonterminal simp. |
| 5 NAMING | Snake case describes filtered-weight cardinality, small-lambda condition, and private helper role. No forbidden abbreviation, numeric `_aux`, numeric scheme, `_ge_`, or `_gt_`. No rename required/queued. |
| 6 LINE PACKING | Repacked four signature lines to three; arithmetic table below covers every line, including final conclusion. |
| 7 BY PLACEMENT | `:= by` and local equality's `by` remain at line ends. |
| 8 FORMAT | Removed semicolon chain. Two-space proof indentation; no blank body lines or `haveI`/`letI`. |
| 9 COMMENTS | None present in target; no comments removed. |
| 10 DOCSTRING | Private auxiliary lemma, no docstring appropriate. |
| 11 VISIBILITY | Already private, one local caller in the induction proof. |
| 12 STRUCTURE | Four proof lines, no conjunction or branching; no decomposition needed. |
| 13 MATHLIB | Five actual searches below; partial match `Finset.card_filter_le` retained as building block. |
| 14 JUNK DEF | n/a: lemma, not data definition. |
| 15 EXISTS LEMMA | n/a: inequality, not an existential witness wrapper. |
| 16 SHOW/CHANGE | Neither occurs. |
| 17 PUSH_NEG | None. |
| 18 GENERALISE | All five binders mechanically drop-tested; `0 < lam` weakened to `0 ≤ lam` experimentally and rejected. Details below. |
| 19 INEQUALITY | Every occurrence already `<` or `≤`; table below. |
| 20 NORMAL-FORM | Standard real cardinality estimate, non-strict conclusion and left-to-right order orientation. |
| 21 SYNTAX-GEN | Existing parameters match its induction caller; no easier applicable equivalent supplied by search. |
| 22 IMPORT-FANOUT | n/a: no imports added. |
| 23 CASTS | 0 dropped; 7 explicit cross-type ℕ→ℝ coercions retained across target; none introduced semantically. |
| 24 INSTANCE-NAME | n/a: no instance declaration. |

Issues fixed: terminal cast-normalization chain, semicolon style, and underpacked signature.
Refactoring needed: none. Optional abstract finite-set/scalar API has no current caller benefit;
retain this substantive induction-case helper. No exact Mathlib replacement was found.

## Mathlib search-status (actual calls)

| Method | Query | Result |
|---|---|---|
| A Lean-Finder | cardinality of filtered finite set at most cardinality multiplied by scalar at least one | `Finset.card_filter_le`; unrelated pair-set/density bounds. |
| B Loogle | `Finset.card_filter_le` | Exact generic filtering-cardinality building block. |
| C LeanSearch | cardinality filter finset is less than or equal to cardinality | `Finset.card_filter_le`, `Finset.card_filter_le_iff`, cardinal comparison. |
| D Source rg | `card_filter_weight_le_of_le_sqrt_aux\|card_filter_le\|le_mul_of_one_le_left` in relevant sources; untruncated full-name search throughout Mathlib | Existing generic building blocks; no target-named match. |
| E Local search | `card_filter_le` | `Finset.card_filter_le`, `Finset.card_filter_le_iff`, variants; index warming, positive source hits valid. |

Auxiliary variants: source/local `_iff`, multiplication `_left` and order division forms examined.
Common-equivalents lookup: finite-set/cardinality bucket; no custom topological or algebraic predicate.
Concluded partial match: keep helper, use existing `Finset.card_filter_le`, `card_box`,
`le_mul_of_one_le_left`, `one_le_div`. This is not a claim of absolute Mathlib absence.
Independent exact-initial-type `exact?` failed to close (scratch imports Box/Sqrt, no Lattice import
or self declaration). `apply?` in the live context produced only partial generic order routes,
not a replacement. The initial live multi-attempt at line-only calc positions also emitted parser
errors; these were not used as proof-success evidence. The equality was retested at exact column
36 successfully. No wrapper was introduced, no custom predicate, and no module-docstring change
was needed or authorized.

## Generalisation status

Every drop probe used scratch `autoImplicit false` so dropping a dependent value could not
silently reintroduce it as an implicit parameter. Original signature retained after failed probes.

| Binder | Class/use | Mechanical probe | Actual result |
|---|---|---|---|
| `(m : ℕ)` | structure value: `Fin m`, threshold and square root | drop | Rejected: unknown `m` in dependent type and conclusion. |
| `(r : Fin m → ℕ)` | structure value: box, weight, cardinal product | drop | Rejected: unknown `r` in conclusion and proof. No pointwise/global property binder applies. |
| `{lam : ℝ}` | structure value: threshold, quotient and hypotheses | drop | Rejected: unknown `lam`. Its concrete real type is fixed by weight/sqrt API. |
| `(hlam : 0 < lam)` | proposition: `one_le_div hlam` | drop; `0 ≤ lam` | Rejected: unknown `hlam`; weaker form type mismatch, `one_le_div` needs strict positivity. |
| `(h : lam ≤ 2 * √(m : ℝ))` | proposition: proves factor at least one | drop | Rejected: unknown `h`. Already weak inequality; no strict-to-weak candidate. |

CLI logs `/private/tmp/lattice-easy-{drop-m,drop-r,drop-lam,drop-hlam,drop-h,weak-hlam}.log`
and corresponding `-fresh.log` files record these failures. No typeclass, universe, bundled
hypothesis, or local/global continuity hypothesis is present. All safe candidates exhausted;
no generalisation applied. No radius-positive assumption existed or was added.

Inversion check: abstract cardinal-filter and scalar multiplication facts are already Mathlib
lemmas; retaining the domain-specific induction case avoids a new abstract API without a user.
Literature: n/a, private auxiliary lemma; no required public-declaration literature search.

## Signature line packing

`#check @card_filter_weight_le_of_le_sqrt_aux` at `format.width 100` in an independent
scratch copy of the INITIAL declaration (exit 0):

```lean
card_filter_weight_le_of_le_sqrt_aux : ∀ (m : ℕ) (r : Fin m → ℕ) {lam : ℝ},
  0 < lam → lam ≤ 2 * √↑m → ↑(#({d ∈ box r | weight r d ≤ (↑m - lam) / 2})) ≤ 2 * √↑m / lam * ∏ j, (↑(r j) + 1)
```

Lean's printed private-name type is a reference; source widths are independently measured
in Unicode codepoints, including indentation. Initial line widths: 84, 47, 74, 53.
Initial L153 could absorb the 24-character prefix `(((box r).filter fun d ↦`:
`47 + 1 + 24 = 72`; the remaining conclusion fits together at 99 characters.

| Final signature line | Width | Next indivisible source unit | Arithmetic | Action |
|---|---:|---|---|---|
| L152 | 84 | `(hlam : 0 < lam)` (16) | 84 + 1 + 16 = 101 > 100 | ok |
| L153 | 72 | `weight r d ≤ ((m : ℝ) - lam) / 2).card : ℝ) ≤` (45) | 72 + 1 + 45 = 118 > 100 | ok |
| L154 | 99 | proof body next | n/a, final `:= by` packed | ok |

All binder joins examined, including the final hypothesis-to-conclusion join now applied.
Within L153 the units have widths 16 (`hlam`), 24 (`h`), and 24 (conclusion prefix), plus
colon/spacing/indentation; no later binder is left on an unnecessary separate line.

## Inequality scan (every occurrence)

| Location | Occurrence | Orientation/action |
|---|---|---|
| L153 | `0 < lam` | canonical, keep |
| L153 | `lam ≤ 2 * √(m : ℝ)` | canonical, keep |
| L154 | `weight r d ≤ ((m : ℝ) - lam) / 2` | canonical, keep |
| L154 | filtered card `≤` bound | canonical, keep |
| L156 | filtered card `≤` full card | canonical, keep |
| L158 | product `≤` scaled product | canonical, keep |

Zero `≥`/`>` in target code; zero reversed-order name patterns.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 | n/a: no `by exact` wrapper; `exact_mod_cast` is substantive. |
| 1.2 | n/a: no standalone `by rfl`. |
| 1.3 | n/a: no `rw` followed by `exact`. |
| 1.4 | Applied normalization consolidation: chained cast steps → terminal `simp [card_box]`. |
| 1.5 | Applied: trailing `rfl` eliminated with the cast chain. |
| 1.6 | n/a: no constructor. |
| 1.7 | n/a: no apply/exact sequence. |
| 1.8 | n/a: no contradiction proof. |
| 1.9 | n/a: predicate and product lambdas are not eta expansions. |
| 1.10 | n/a: no have. |
| 1.11 | n/a: no apply/intro. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projected have. |
| 1.14 | n/a: no consecutive rw; entire normalization replaced. |
| 1.15 | Terminal simp remains unsqueezed. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | n/a: existing functions do not improve with receiver notation. |
| 1.18 | n/a: parentheses in nested term arguments are load-bearing. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: not an existential helper. |
| 2.1 | Whole-goal `grind [card_box]` tried: failed to derive filtered-count bound. |
| 2.2 | n/a: no grind in original or final proof. |
| 2.3 | Direct terminal `simp [card_box]` succeeded on equality at exact column. |
| 2.4 | n/a: no function regularity goal. |
| 2.5 | Existing positivity solves product nonnegativity; whole final inequality positivity rejected as not a positivity goal. |
| 2.6 | Final inequality `gcongr` tried: no progress. |
| 2.7 | n/a: no remaining Nat/Int arithmetic goal; real square-root quotient/order goal. |
| 2.8 | Whole-goal aesop tried: no progress. |
| 2.9 | Equality norm_cast leaves `card_box`; final inequality norm_num unsolved. Retain simp and exact_mod_cast. |
| 2.10 | n/a: symbolic unbounded real inequality, not finite decidable computation. |
| 2.11 | n/a: no algebraic equality with denominators. |
| 2.12 | n/a: no ring/ring_nf closing block. |
| 2.13 | n/a: no symmetric case split. |
| 2.14 | n/a: three-stage calc, not two-stage; transitivity term would obscure cardinal identity. |
| 2.15 | n/a: no repeated sibling goals. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability tactic. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases. |
| 3.5 | n/a: private induction-case lemma, not a canonical rewrite or regularity fact. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no maxHeartbeats or other limit change. |

## Step-back review and independent validation

The calculation expresses the three mathematical steps directly. Whole-goal grind/simp/aesop
and exact search did not supply a complete alternative. A new abstract wrapper would add API
without a caller benefit. The successful direct equality simp removes cast plumbing cleanly.

Independent INITIAL exact type, non-self proof: `/private/tmp/lattice-easy-proof.lean`,
`/Users/ramin/.elan/bin/lake env lean ...` exited 0; imports only Sqrt and Roth.Box.
The final signature was also mechanically compared with initial signature ignoring whitespace:
identical. Original type `#check` file `/private/tmp/lattice-easy-check.lean` exited 0.

Actual built private theorem: native `lean_verify` on
`Roth.card_filter_weight_le_of_le_sqrt_aux` returned trust `standard`, axioms exactly
`[propext, Classical.choice, Quot.sound]`, nonstandard axioms `[]`, source warnings `[]`.
No numeric private-name literal was used.

New identifiers: none. `simp` tactic and `card_box` were already present in the source;
`Finset.card_filter_le`, `one_le_div`, `le_mul_of_one_le_left` verified by source/search/#check.
No sorry, new axiom, suppression, limit increase, version or header change.

## Gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `/Users/ramin/.elan/bin/lake build Roth.Lattice` exit 0; built Lattice in 61s; `/private/tmp/lattice-easy-build.log`. |
| definition_protected | pass | No def/abbrev changed. |
| theorem_statement_protected | pass | Initial/final signatures equal modulo whitespace; packing only. |
| structure_gate | pass | Four body lines, no conjunction or branches. |
| naming_gate | pass | Descriptive snake case, allowed `_aux`, no forbidden tokens/patterns. |
| line_packing_gate | pass | All 3 signature rows, widths 84/72/99. |
| inequality_orientation_gate | pass | All 6 occurrences scanned, no reversed notation. |
| cumulative_no_unintended_breakage | pass locally | Private helper's local caller remains in successfully built file. Owner performs full/separate final gates. |
| source preservation | pass | Only target proof and whitespace changed; comments/header/docs preserved. |
| LSP | pass | Complete native final diagnostic result success=true, partial=false; existing L1 header warning only. |
| axioms | pass | Actual private theorem, standard three only. |

Overall per-declaration: pass. Full-project and separate LeanEval final checks belong to owner;
no optional profiling/compiler work started after owner's source freeze.

## Result and required checklist

Before: 8 declaration lines / 4 body lines. After: 7 declaration lines / 4 body lines.
Saved: 1 line; normalization readability/style improved. Renames queued: none.
Comments-preserved: none present. Refactoring needed: none.

- [x] Step 1 — references read.
- [x] Step 2 — all 24 audit items.
- [x] Step 2.5 — five actual search methods and auxiliary routes.
- [x] Step 2.6 — all five binders mechanically probed, private literature exemption.
- [x] Step 2.7 — every signature line width, `#check` reference, final join arithmetic.
- [x] Step 2.8 — every inequality occurrence.
- [x] Step 3 — all 42 rules.
- [x] Step 4 — holistic review and exact/apply search attempts.
- [x] Step 5a — complete final LSP.
- [x] Step 5b — actual module build, protection/content/axiom gates.
- [x] Step 6a — no rename required, no queue mutation.

Source frozen at owner acceptance: full-file SHA256
`c4001f0b35048a95614d8a819471d639a1d9f66dcfbf41633728f2a290ffb73e`.
Target (stripped declaration) SHA256
`5867bf405d78638f48dd6bf546f38c6d44bcb85b9317d45730cf4e3c30b69bbc`.

Owner checkpoint: explicit source edit revocation before sequential full/separate LeanEval session37542; both exit0(115.31s/45.69s), frozen hash stable. Logs `/private/tmp/roth-lattice-helper-easy-{full,leaneval}.log`. No original264 tally increment.
