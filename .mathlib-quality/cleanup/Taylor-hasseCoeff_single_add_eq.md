# `MvPolynomial.hasseCoeff_single_add_eq` — declaration cleanup

Baseline: `b39e67f`, `Roth/Taylor.lean` lines 76–91. Final range: 76–84.
Before: 16 declaration lines / 13 proof lines. After: 9 / 7. Saved: 7 lines.
Only this declaration was changed. Its statement, argument order, visibility and name are unchanged;
the signature was repacked. Source SHA256 at freeze:
`72a52b08db494fd445a13c5716fc1afd32fbf315b1e41dccffe81f230ef1f7bd`.

## References and scope

Read the full worker contract, both `lean4` and `mathlib-quality` skills, and
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, `naming-conventions.md`;
read the applicable formatting, signature, tactic, and visibility sections of `style-rules.md`.
The mathematical statement separates the binomial factor at `i` from the product defining a
Hasse coefficient; `hi` identifies its upper argument with `n`.

## Full audit

1. **LINT:** no target diagnostics. Complete final LSP reports only the user-preserved file-header warning.
2. **HAVE SCAN:** original L81 `hdisj` is used once at L85. Its RHS includes a lambda with a `by`
   proof, so it has genuine proof content; naive expression inlining was not the improvement.
   Replaced the entire support-disjointness construction with `Finsupp.mul_prod_erase'`.
   No `have` remains.
3. **SET_OPTION:** none before or after; no limits or suppressions added.
4. **SIMP SQUEEZE:** initial nonterminal `simp only [hasseCoeff]` became an ordered rewrite.
   The three final simp invocations are terminal: the zero-index side condition, the factor at `i`,
   and each remaining product factor. No nonterminal bare simp remains.
5. **NAMING:** `hasseCoeff_single_add_eq` names the subject and single-plus-remainder expression.
   Embedded `hasseCoeff` follows its definition's case; remaining words are snake case.
   No forbidden abbreviation, number scheme, numeric auxiliary suffix, or single-letter name.
   This is a standard mathematical property, so an `_aux` suffix is unnecessary. No rename queued.
6. **LINE PACKING:** moved both explicit binders onto the first line; measured tables below.
7. **BY PLACEMENT:** declaration and side-condition `by` remain at the end of their preceding syntax.
8. **FORMAT:** two-space proof indentation, four-space signature continuation, no blank proof lines,
   no semicolon chains, no `haveI`/`letI`; mathematical lambda now uses `↦`.
9. **COMMENTS:** none in target; no comment removed or relocated.
10. **DOCSTRING:** n/a: private lemma; none present or introduced.
11. **VISIBILITY:** private retained; the caller is the Taylor coefficient proof in this file.
12. **STRUCTURE:** seven proof lines, no conjunction, largest branch three lines; no extraction needed.
13. **MATHLIB:** partial match `Finsupp.mul_prod_erase'` now performs the split directly;
    see five-method evidence below. The remaining binomial-factor congruence is local content.
14. **JUNK DEF:** n/a: lemma, not a definition.
15. **EXISTS LEMMA:** n/a: no existential conclusion.
16. **SHOW vs CHANGE:** neither occurs.
17. **PUSH_NEG:** none.
18. **GENERALISE:** every actual parameter audited below; dropping `hi` fails and a compiled
    counterexample certifies necessity. No signature change proposed.
19. **INEQUALITY:** no inequality in the signature or hypotheses; table below.
20. **NORMAL-FORM:** equality from Hasse coefficient at a single-plus-remainder to separated product
    is the needed rewrite direction. Finsupp erase is the canonical remainder operation.
21. **SYNTAX-GEN:** OK: the existing caller supplies `k' i = 0` directly; restating as support
    nonmembership would add a conversion without improving application.
22. **IMPORT-FANOUT:** n/a: no new import.
23. **CASTS:** 0 dropped / 0 cross-type / 0 load-bearing casts introduced or retained in the diff.
24. **INSTANCE-NAME:** n/a: this is a lemma; no instance is declared.

Issues found and fixed: explicit disjoint-support reconstruction, redundant equality case split,
underpacked signature, and lambda arrow. Refactoring needed: none.

## Mathlib search status

| Method | Actual query / evidence | Result |
|---|---|---|
| A — Lean-Finder | `product over finitely supported function equals value at an index times product over erase` | Returned `Finsupp.mul_prod_erase'`, `mul_prod_erase`, and `prod_eq_single`. |
| B — Loogle | `Finsupp.prod, Finsupp.erase` | Returned the two erase-product lemmas with their types. |
| C — LeanSearch | Existing session service failure HTTP 500, reported in parent contract | Unavailable; no redundant retry and no absence inference. |
| D — source | `prod.*erase|erase.*prod`, then full names in `Algebra/BigOperators/Finsupp/Basic.lean`; support API in `Data/Finsupp/Single.lean` and `Data/Finset/Erase.lean` | Verified `mul_prod_erase'` L170, `support_erase` L373, `ne_of_mem_erase` L63. |
| E — local name pattern | `Finsupp.prod` | Returned product API from source, including `prod_congr`; semantic index unavailable, not a negative result. |

Auxiliary variants checked: `mul_prod_erase` versus `mul_prod_erase'`,
`prod_add_index_of_disjoint`, `prod_single_index`, `prod_eq_single`, and `prod_congr`.
Common-equivalents catalogue: no discrete/compact/bounded predicate applies.
Actual `#check` verified `@Finsupp.mul_prod_erase'` and `@Finsupp.prod_congr` under the unchanged imports.
The whole-goal `exact?` failed; `apply?` supplied partial arithmetic transformations with open
premises, not a proof or direct theorem replacement. No claim of exhaustive mathematical absence.
Concluded: partial match found and used directly inside the proof; retain the local Hasse-specific
statement. No new wrapper or API declaration was added.

## Generalisation status

The isolated theorem's elaborated type confirms that section parameters `R` and `[CommSemiring R]`
were already excluded by Lean. They are not hidden hypotheses of this lemma.

| Parameter | Class | Use | Mechanical candidates / verification | Result |
|---|---|---|---|---|
| `{σ : Type*}` | type variable | index type for `i`, `k'`, and `d` | Already universe polymorphic; dropping makes dependent types unbound; no additional structure to weaken. | Retain. |
| `{i : σ}` | structure value | distinguished coordinate and erase index | Occurs in statement; removing would change the mathematical statement; no point-localisation applies. | Retain. |
| `{n : ℕ}` | structure value | natural binomial upper index | Occurs in statement; `Nat.choose` fixes the type, so abstracting it changes the object. | Retain. |
| `{k' : σ →₀ ℕ}` | structure value | finite-support remainder | Occurs in the Hasse coefficient and `hi`; drop is ill-typed. Changing to an arbitrary function restates the established Hasse API. | Retain. |
| `(hi : k' i = 0)` | proposition | simplifies the separated factor | Actual independent candidate deleted this binder and replaced `simp [hi]` by `simp`; fails with `(n + k' i).choose (d i) = n.choose (d i)`. No strict/weak or bundled-hypothesis rule applies. | Necessary; retain. |
| `(d : σ →₀ ℕ)` | structure value | product index and lower choose argument | Occurs throughout conclusion; drop is ill-typed, and abstracting natural exponents changes `choose`. | Retain. |
| decidability | absent hypothesis | local support calculation | `classical` is proof-local; no decidability parameter to drop. | Already minimal. |

The `hi` drop is also refuted by a successful compiled example: on `Unit`, take `n = 1` and
`k' = d = Finsupp.single () 1`; the two sides are unequal (2 versus 1).
Inversion check: unfolding `hasseCoeff` exposes the general product split, already supplied by
Mathlib's `mul_prod_erase'`; no missing abstract theorem to extract.
Big-change candidates: none warranted. Literature: n/a, private declaration.

## Signature packing

Actual independent `#check @probe` at `format.width 100` (the probe has the identical statement):

```lean
@probe : ∀ {σ : Type u_2} {i : σ} {n : ℕ} {k' : σ →₀ ℕ},
  k' i = 0 → ∀ (d : σ →₀ ℕ), hasseCoeff d (Finsupp.single i n + k') = n.choose (d i) * hasseCoeff (Finsupp.erase i d) k'
```

Widths count codepoints, including indentation. Conclusion is treated as the complete next
syntactic unit rather than splitting an application at an arbitrary lexical word.

| Before line | Chars | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 76 | 68 | `(hi : k' i = 0)` (15) | 68 + 1 + 15 = 84 ≤ 100 | repack |
| 77 | 34 | conclusion through `:= by` (89) | 34 + 1 + 89 = 124 > 100 | ok |
| 78 | 93 | none | n/a | ok |

| Final line | Chars | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 76 | 99 | conclusion through `:= by` (89) | 99 + 1 + 89 = 189 > 100 | ok |
| 77 | 93 | none | n/a | ok |

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | statement and every hypothesis | no `≥` or `>` | n/a | no `_ge_` or `_gt_` name |

## Golfing rule pass — all 42 rules

| Rule | Status |
|---|---|
| 1.1 by-exact wrapper | n/a: none. |
| 1.2 by-rfl | n/a: none. |
| 1.3 rw + exact | n/a: no closing rewrite/exact pair. |
| 1.4 simp + exact | n/a: no such pair. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: equality, no constructor proof. |
| 1.7 apply + exact | n/a: none. |
| 1.8 by_contra! | n/a: no contradiction chain. |
| 1.9 eta reduction | Remaining lambda uses both arguments in a proof; no eta redex. Converted `=>` to `↦`. |
| 1.10 single-use have | Replaced the whole `hdisj` construction with existing erase-product API. |
| 1.11 refine + fun | Already uses `refine Finsupp.prod_congr fun ...`; retained. |
| 1.12 redundant show | n/a: none. |
| 1.13 have projections | n/a: none. |
| 1.14 merge rewrites | Consolidated unfolding and erase split into one ordered `rw` list. |
| 1.15 unsqueeze terminal simp | No terminal `simp only`; all closing simplifiers remain bare. |
| 1.16 squeeze nonterminal simp | Original unfolding was already squeezed; replaced by `rw`. None remains. |
| 1.17 dot notation | `Finset.ne_of_mem_erase hj` is the direct namespace API; no useful receiver-chain replacement. |
| 1.18 remove parentheses | Remaining `(by simp)` is inside a rewrite theorem argument and is required grouping. |
| 1.19 push Not | n/a: no `push_neg`. |
| 1.20 existential helper | n/a: no existential. |
| 2.1 grind | Actual whole-goal trial failed; it cannot infer the finite-product split. On the old support side-goal it succeeded, but that entire construction was removed. |
| 2.2 delete before grind | n/a: no retained grind. |
| 2.3 simpa consolidation | Direct product-split route compiled; no simp-plus-closing-tactic sequence remains. |
| 2.4 fun_prop | n/a: no analytic function property. |
| 2.5 positivity | n/a: no positive/nonnegative goal. |
| 2.6 gcongr | n/a: no inequality or monotonicity chain. |
| 2.7 lia / omega | n/a: key step is a finite product identity, not linear arithmetic. |
| 2.8 aesop | Actual whole-goal trial failed without progress. It solved the old support side-goal, which was removed by API reuse. |
| 2.9 norm_num / norm_cast | n/a: no concrete arithmetic or cast goal in the target. |
| 2.10 decide | n/a: theorem has arbitrary index type and unbounded Finsupp parameters, not a closed computation. |
| 2.11 field_simp; ring | n/a: no denominators or polynomial-ring rearrangement. |
| 2.12 linear_combination | n/a: no ring-ending proof or linear combination of hypotheses. |
| 2.13 wlog | n/a: equality/inequality support branches are not symmetric; eliminated directly. |
| 2.14 calc to term | n/a: no calc. |
| 2.15 shared goal closing | The two factor goals need different facts (`hi` versus support erasure); retain explicit branches. |
| 3.1 erw → rw | n/a: no erw. |
| 3.2 legacy analytic tactics | n/a: none. |
| 3.3 omega → lia | n/a: neither occurs. |
| 3.4 rfl substitution | Removed the equality case split entirely with `Finset.ne_of_mem_erase`. |
| 3.5 automation attributes | No attribute added: private decomposition helper is explicitly rewritten at its sole caller. |
| 3.6 simp_all | No simp_all only occurs; direct API proof avoids contextual search. |
| 3.7 remove limits | n/a: none before or after. |

## Experiments and reflection

Native `lean_multi_attempt` whole-goal trials: `grind`, `simp [hasseCoeff, hi]`, `aesop`,
`exact?`, `apply?`. None produced a complete replacement. A separate first trial at the original
disjoint-support subgoal tested those same tactics: `grind` and `aesop` closed that subgoal,
but direct API reuse made it unnecessary.
An independent native `lean_run_code` proof using `mul_prod_erase'` compiled. A shorter attempt
to transport membership by `Finsupp.support_erase ▸ hj` failed with an unresolved `DecidableEq`
metavariable; the final explicit rewrite at `hj` compiled and is clearer.
The final seven-line body states exactly the mathematical argument: split at `i`, simplify its
factor with `hi`, and use support erasure to simplify all other factors. It has no missing API,
temporary helper, or useful further extraction.

## Verification and gates

* Native complete `lean_diagnostic_messages`: `success=true`, `partial=false`,
  `timed_out=false`, no failed dependencies; only existing header warning at L1.
* `lake build Roth.Taylor`: exit 0, 1439 jobs; target rebuilt in 9.2 s.
  Log: `/private/tmp/roth-taylor-hasseCoeff_single_add_eq-module.log`.
* Independent proof used only `import Roth.Box` and `import Roth.HasseDeriv`, not `Roth.Taylor`;
  thus the theorem being cleaned was unavailable to automation. Exact final proof compiled.
* Independent `#check` confirms the statement and exclusion of irrelevant section parameters.
  `#print axioms probe` returned only `propext`, `Classical.choice`, `Quot.sound`.
* Script comparison of old and new signature text, removing whitespace, returned `True`.
* Parent owns full-project and `Roth.LeanEval` dependent builds and publication.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module command exit 0 above. |
| definition_protected | pass | No definition/abbreviation changed. |
| theorem_statement_protected | pass | Exact signature tokens unchanged; whitespace repack only. |
| structure_gate | pass | Seven proof lines, no conjunction, no branch over ten lines. |
| naming_gate | pass | Descriptive subject-operation name; no forbidden pattern. |
| line_packing_gate | pass | All final rows measured; widths 99 and 93. |
| inequality_orientation_gate | pass | Table records zero reversed inequalities. |

Overall: pass. Renames queued: none. Comments preserved: none present.
Refactoring needed: none. Source frozen after module/LSP verification; subsequent edits report-only.

## Required phase checklist

- [x] Step 1 — required references read.
- [x] Step 2 — all 24 audit items reported.
- [x] Step 2.5 — five-method search and auxiliary variants reported.
- [x] Step 2.6 — every parameter audited; actual drop test and certified counterexample.
- [x] Step 2.7 — original and final signature-width tables.
- [x] Step 2.8 — inequality scan table.
- [x] Step 3 — all 42 golfing rules have a status.
- [x] Step 4 — whole-proof alternatives and structural reflection completed.
- [x] Step 5a — complete LSP and module build passed.
- [x] Step 5b — all diff gates passed.
- [x] Step 6a — no rename warranted; queue untouched.
