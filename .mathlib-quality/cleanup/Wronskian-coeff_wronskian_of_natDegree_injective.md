# Declaration audit: `Roth.coeff_wronskian_of_natDegree_injective`

Current status: the user-approved removal of both unused hypotheses is applied and fully validated. See the amendment section below; earlier pending references describe the historical checkpoint.

Baseline: `ab65b1b`, `Roth/Wronskian.lean` lines 127–155 (original inventory 134–162), 29 declaration lines, 24 proof lines. Routine result: lines 127–148, 22 declaration lines, 18 proof lines; 7 declaration lines saved. Dedicated worker: `decl08`. Ownership: this declaration and this report only; no Git/shared-log ownership.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md in full. Also read both SKILL.md files, the complete supplied worker contract, naming-conventions.md, and the relevant style-rules.md sections. The parent's explicit scope preserves public API/docstrings pending the specific hypothesis-removal decision.

## Mathematical reading

Expand the Wronskian determinant as a signed sum over permutations. For a permutation whose derivative orders stay below the corresponding polynomial degrees, the coefficient of the total remaining degree is the product of the individual leading coefficients, weighted by binomial coefficients. If an order exceeds a degree, both products vanish. Summing those identities gives the coefficient formula. Neither nonvanishing nor distinct degrees is used for this identity; those conditions are used by the subsequent nonvanishing theorem.

## Full 24-item audit

1. **LINT:** baseline `hφ` and `hd` are unused. Both removals compile together in scratch; exact proposal and sole caller repair sent to parent for user decision. Live arguments retained pending that decision. Header warning is outside this declaration and explicitly preserved by user.
2. **HAVE SCAN:** `key` (baseline 133–150) has a nontrivial `by` proof and one final simp use: keep, put permutation argument before colon. `hD` (139–143) has `by` and one rewrite use: eliminate through direct `Equiv.sum_comp` and `Finset.sum_tsub_distrib` rewrites. No no-`by` single-use binding remains.
3. **SET_OPTION:** none; no limits/options added.
4. **SIMP SQUEEZE:** negative branch's `simp [Nat.choose_eq_zero_of_lt hi]` is terminal and retained. Final nonterminal `simp only [Matrix.of_apply, coeff_intCast_mul, key, Finset.prod_mul_distrib]` followed by `ring` becomes terminal `simp [coeff_intCast_mul, key, Finset.prod_mul_distrib, mul_comm, mul_assoc]`. No nonterminal bare simp remains.
5. **NAMING:** descriptive snake_case coefficient/Wronskian/conclusion-of-hypothesis name; `natDegree` is the established API identifier embedded in it. No forbidden abbreviation, numeric scheme, single-letter public name, `_ge_`, or `_gt_`. Removing `hd` would make `_of_natDegree_injective` unnecessary; propose `coeff_wronskian` only if a separate rename is approved. No in-place rename or queue mutation by this worker.
6. **LINE PACKING:** measured codepoint tables below; repack RHS leading-coefficient product onto the coefficient line. Four final signature rows, maximum 99 characters. Compact local `key` signature and adjacent rw entries as well.
7. **BY PLACEMENT:** all `by` tokens at end of their preceding declaration/type line.
8. **FORMAT:** two-space proof indent, four-space signature continuation, no blank proof lines, no chained distinct tactics, all ordinary lambdas use `↦`; no `haveI`/`letI`.
9. **COMMENTS:** no inline proof comments. Existing public docstring and all block comments are byte-identical (script comparison true); no prose deleted.
10. **DOCSTRING:** existing docstring documents the coefficient formula, optional-use hypotheses, and source. Preserved under explicit scope. Its explanation already notes the unused assumptions.
11. **VISIBILITY:** public coefficient API retained; sole current code caller is the following nonvanishing theorem. Public-to-private would remove existing API and was not authorized.
12. **STRUCTURE:** baseline proof 24 lines, final 18; not among the module's Main results bullets. No conjunction in statement. Positive branch 4 lines and negative branch 5 lines after compaction, each below 10. Considered extraction of `key`; a single-use private helper would repeat a substantial signature with no gate or reuse benefit. No decomposition flag required.
13. **MATHLIB:** five-method status below; polynomial determinant coefficient results are partial matches, not this degree-varying Hasse derivative formula. Existing direct Mathlib APIs retained. Full-name search and actual `exact?` probe did not find a direct replacement.
14. **JUNK DEF:** n/a, theorem; no definition changes.
15. **EXISTS LEMMA:** n/a, not a private existential witness wrapper.
16. **SHOW vs CHANGE:** n/a, neither occurs.
17. **PUSH_NEG:** no deprecated `push_neg`; existing `push Not at h` retained.
18. **GENERALISE:** every parameter examined below. Both explicit hypotheses can be removed; concrete compiled proposal awaits user decision. The Field requirement is imposed by the existing Wronskian definition's interface.
19. **INEQUALITY:** no reversed inequalities in signature or local hypotheses; see occurrence table. Existing local derivative-order test uses `≤`.
20. **NORMAL-FORM:** coefficient at the natural truncated degree bound equals leading-coefficient product times the binomial determinant; this is the caller's needed rewrite form. No competing equivalence API introduced.
21. **SYNTAX-GEN:** removing unused explicit hypotheses simplifies the sole call; this is the concrete proposal. Keep equality and degree expression unchanged.
22. **IMPORT-FANOUT:** n/a, no new imports. `linear_combination` is unavailable under current imports; no tactic import added for a goal already solved by simp.
23. **CASTS:** removed 4 redundant ascriptions: two `σ i : Fin l`, one choose-result `: ℕ` in the statement, and one in `key`. Remaining cross-type coercions are Fin→Nat degree/order indices and Nat→K binomial coefficients. Remaining `: K` annotations select the coefficient ring; no same-type cast introduced.
24. **INSTANCE-NAME:** n/a, theorem with no instance declaration.

Issues fixed: direct degree-sum rewrite, local binder placement, terminal simp replacing ring, redundant casts, lambda style, and packing. Unused-hypothesis removal is compiled and explicitly pending user decision, not silently skipped.

## Mathlib search-status

| Method | Query/evidence | Outcome |
|---|---|---|
| A Lean-Finder | `coefficient of determinant of polynomial matrix, Wronskian leading coefficient`, 4 results | `Polynomial.wronskianBilin_apply` (two-polynomial Wronskian), `Polynomial.coeff_det_X_add_C_card`, `Polynomial.leadingCoeff_det_X_one_add_C`, `Matrix.det_matrixOfPolynomials`; all different matrix/degree shapes |
| B Loogle | `Polynomial.coeff, Matrix.det`, 4 results | `coeff_det_X_add_C_card`, `coeff_det_X_add_C_zero`, `det_matrixOfPolynomials`, `det_eq_sign_charpoly_coeff`; no direct arbitrary-order coefficient identity |
| C LeanSearch | inherited environment status from parent | HTTP 500, unavailable; not repeated per parent instruction and not counted as evidence of absence |
| D source search | untruncated `rg` over polynomial/matrix sources for `coeff_wronskian`, `coeff.*det`, `coeff_prod_of_natDegree`, `hasseDeriv_coeff`, `hasseDeriv_eq_zero_of_lt_natDegree` | coefficient determinant results above; Hasse coefficient and vanishing APIs found; constant-bound `coeff_prod_of_natDegree_le` differs from the local varying-bound lemma |
| E name search | native `lean_local_search "coeff_prod"`, limit 15 | source hits include `Polynomial.coeff_prod_of_natDegree_le`, local varying-bound lemma, and unrelated power-series/multivariate variants; index `warming`, so no absence inference from index |

Auxiliary variants considered: determinant coefficient at zero/cardinality, leading coefficient of determinant, product coefficient degree bounds, Hasse coefficient and vanishing. Common-equivalents lookup: no discrete/finite/bornology bucket applies. Actual `#check` confirmed `natDegree_hasseDeriv_le`, `hasseDeriv_coeff`, `Finset.sum_tsub_distrib`, `Equiv.sum_comp`, and constant-bound `Polynomial.coeff_prod_of_natDegree_le` signatures.

Compiled generic route: native `lean_multi_attempt` at original proof entry ran `exact?`, which failed to close. `apply?` at final entry found only generic graph-membership/inverse-equality reductions with substantial remaining goals, not a proof. No assertion of exhaustive global absence: partial matches exist, the exact target remains local and builds on the direct Hasse and determinant APIs. No wrapper or custom predicate added.

## Generalisation status

| Parameter | Class | Use | Mechanical candidates/evidence | Result |
|---|---|---|---|---|
| `{K : Type*}` | type variable | polynomial coefficient ring | Already universe-polymorphic; dropping removes the ring carrier from the statement | retain |
| `[Field K]` | typeclass | required by `Roth.wronskian` and `wronskianMatrix` signatures | Scratch `[CommRing K]` at `Roth.wronskian φ` fails application type mismatch with the Field-based polynomial instance. Dropping all algebra or using DivisionRing cannot supply that existing Field API either | no local weakening without separately changing definitions |
| `{l : ℕ}` | index size | `Fin l` determinant dimensions and derivative order sum | Cannot drop while preserving the statement. Arbitrary finite indices require assigning derivative orders and a new statement | retain |
| `{φ : Fin l → K[X]}` | structure value | argument of Wronskian and both RHS factors | Cannot drop the family appearing in the conclusion | retain |
| `hφ : ∀ ν, φ ν ≠ 0` | proposition | unused | Remove jointly with `hd` in a complete self-contained prefix; native `lean_run_code` success true, diagnostics empty | compiled proposal sent; unapplied pending approval |
| `hd : Function.Injective fun ν ↦ (φ ν).natDegree` | proposition | unused | Same simultaneous drop-test; no dependency on `hφ` either | compiled proposal sent; unapplied pending approval |

Strict→weak and point-localisation: no strict-inequality/continuity/global analytic assumption exists. These two propositions can be removed altogether, which is stronger than weakening their formulation. Inversion check: determinant expansion is generic but the key argument repeatedly uses Hasse coefficient, degree, and vanishing identities; arbitrary polynomial matrices require a new degree-bound theorem, not the same proof with an irrelevant witness erased. No speculative abstract API added.

### Concrete public-interface proposal (compiled, not yet applied)

```lean
theorem coeff_wronskian_of_natDegree_injective {φ : Fin l → K[X]} :
    (wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) =
      (∏ ν, (φ ν).leadingCoeff) *
        (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : K)).det := by
  -- same verified proof
```

All project Lean references searched. Exactly one code caller, in `wronskian_ne_zero_of_natDegree_injective`:

```diff
-  have h1 := coeff_wronskian_of_natDegree_injective hφ hd
+  have h1 := coeff_wronskian_of_natDegree_injective (φ := φ)
```

The module-doc reference needs no change if the name stays. A rename to `coeff_wronskian` is a separate optional API decision. Parent has the proposal and owns escalation to the user; the old API remains live at this checkpoint.

### Public literature search

Web query: `Wronskian polynomials leading coefficient Vandermonde generalization Bostan Dumas`. Top three relevant hits: [author-hosted final paper](https://mathexp.eu/bostan/publications/BoDu10.pdf), [arXiv record](https://arxiv.org/abs/1301.6598), and [author-hosted earlier version](https://specfun.inria.fr/bostan/publications/BoDu09.pdf). The final paper was opened and read at the relevant lemma. Its monomial Wronskian formula factors a product of coefficients, an exponent sum, and a Vandermonde determinant; the wider independence theorem concerns characteristic-zero power series/rational functions. The present Hasse-normalized coefficient identity does not itself require characteristic zero. That distinction is corroborated by the compiled Lean proof, not inferred solely from the classical ordinary-derivative statement. Extending this API to series or multivariate operators would change the theorem's objects and is not necessary for its caller. ChatGPT math MCP: unavailable (no matching callable tools).

## Signature width tables

Codepoints, not UTF-8 bytes. Next-token entries are complete binder/expression units, as in the contract's packing examples. Original positions use the pre-worker file.

| Before line | Width | Next unit width | Arithmetic | Action |
|---|---:|---:|---|---|
| 127 | 85 | `hd` binder 50 | 85 + 1 + 50 = 136 | ok |
| 128 | 56 | coefficient application 65 | 56 + 1 + 65 = 122 | ok |
| 129 | 71 | leading-coefficient product and `*`, 27 | 71 + 1 + 27 = 99 | repack |
| 130 | 33 | binomial determinant 71 | 33 + 1 + 71 = 105 | ok |
| 131 | 85 | no next signature line | n/a | ok |

| Final line | Width | Next unit width | Arithmetic | Action |
|---|---:|---:|---|---|
| 127 | 85 | `hd` binder 49 | 85 + 1 + 49 = 135 | ok |
| 128 | 55 | coefficient application 65 | 55 + 1 + 65 = 121 | ok |
| 129 | 99 | binomial determinant 64 | 99 + 1 + 64 = 164 | ok |
| 130 | 76 | no next signature line | n/a | ok |

Actual final `#check` under `set_option format.width 100`:

```text
@coeff_wronskian_of_natDegree_injective : ∀ {K : Type u_2} [inst : Field K] {l : ℕ} {φ : Fin l → K[X]},
  (∀ (ν : Fin l), φ ν ≠ 0) →
    (Function.Injective fun ν ↦ (φ ν).natDegree) →
      (wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν, ↑ν) =
        (∏ ν, (φ ν).leadingCoeff) * (Matrix.of fun μ ν ↦ ↑((φ ν).natDegree.choose ↑μ)).det
```

## Inequality occurrence table

| Occurrence | Location | Original | Rewrite | Name action |
|---|---|---|---|---|
| none | signature and explicit hypotheses | no `≥` or `>` | n/a | no `_ge_`/`_gt_` |
| 1 | local `by_cases h` | `(σ i : ℕ) ≤ (φ i).natDegree` | already forward | none |
| 2 | derived `hi` after `push Not` | `(φ i).natDegree < ↑(σ i)` | already forward | none |

## All 42 golfing rules

| Rule | Status/evidence |
|---|---|
| 1.1 by exact | n/a: no wrapper |
| 1.2 by rfl | n/a: no reflexivity proof |
| 1.3 rw + exact → rwa | Negative branch exact uses a separately constructed zero product, not a hypothesis rewrite; final algebra instead closes by simp |
| 1.4 simp + exact → simpa | n/a: no simp-followed-by-exact block; final simp+ring consolidated |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructor terms | n/a: equality proof, no constructor pair |
| 1.7 apply + exact | n/a: none |
| 1.8 by_contra! | n/a: no contradiction followed by negation pushing |
| 1.9 eta lambdas | No eta-redex with a fixed function; indexed polynomial degree expressions genuinely depend on the variable. All lambda arrows standardized |
| 1.10 single-use have | `hD` removed by direct rewrites; `key` has proof content and is retained |
| 1.11 refine + fun | Local `key` permutation moved before colon, eliminating `intro σ`; product/sum congruence already use refine+fun |
| 1.12 redundant show | n/a: none |
| 1.13 have projections | n/a: no .1/.2 binding |
| 1.14 merge rw | Degree-sum normalization and product coefficient rewrite in one rw call |
| 1.15 terminal simp only | Final squeezed simp plus ring replaced by terminal bare simp with explicit additional lemmas |
| 1.16 nonterminal simp | None remains; negative-branch simp is terminal |
| 1.17 dot notation | `.symm` on zero-product equality retained; no shorter dot form for coefficient rewriting |
| 1.18 `<|` | Nested proof is a middle argument to prod_eq_zero before `.symm`; required parentheses retained |
| 1.19 push_neg | Already `push Not`; no deprecated tactic |
| 1.20 existential helper | n/a: theorem not an existential wrapper |
| 2.1 grind whole proof | Actual native attempt fails with negated target; no result applied |
| 2.2 remove before grind | n/a: no grind retained; final grind attempt rejects redundant explicit local `key` and offers no advantage over verified simp |
| 2.3 simpa consolidation | Stronger terminal simp consolidation succeeds, removing ring |
| 2.4 fun_prop | n/a: no analytic function-property goal |
| 2.5 positivity | n/a: target is equality; no ordered-ring positivity needed |
| 2.6 gcongr | n/a: no inequality monotonicity chain; product/sum equalities use congruence APIs |
| 2.7 lia / omega | Arithmetic is exactly `Nat.sub_add_cancel (h i)` within a coefficient rewrite; direct canonical lemma solves it without an arithmetic subgoal |
| 2.8 aesop | Actual whole-proof attempt exhausted search without proving target |
| 2.9 norm_num / norm_cast | No concrete numeral computation or cast-normalization goal; deleting redundant ascriptions compiled directly |
| 2.10 decide | n/a: symbolic Field/polynomial identity with unrestricted dimension |
| 2.11 field_simp; ring | n/a: no denominator |
| 2.12 linear_combination | Actual native attempt reports unknown tactic in current import closure; no extra import justified, terminal simp solves the algebra |
| 2.13 wlog | n/a: valid-order and over-order branches are not symmetric |
| 2.14 collapse calc | n/a: no calc |
| 2.15 `<;>` | n/a: branches need distinct coefficient and zero-product arguments |
| 3.1 erw → rw | n/a: no erw |
| 3.2 fun_prop replacement | n/a: no continuity/measurability tactic |
| 3.3 omega → lia | n/a: neither arithmetic tactic retained |
| 3.4 rcases rfl | n/a: witness is an index with a strict bound, not equality substitution |
| 3.5 automation attributes | No simp/grind attribute: specialized top-degree coefficient formula is an explicit rewriting API, no broad normal-form benefit established |
| 3.6 simp_all | n/a: no simp_all only; ordinary terminal simp closes without sweeping unused assumptions |
| 3.7 maxHeartbeats | n/a: none present or added |

## Actual experiments and step-back reflection

- Complete self-contained prefix with both hypotheses removed: `lean_run_code`, success true, diagnostics empty. Live API untouched.
- Direct degree-sum rewrites, redundant-cast removal, and final simp first tried without `mul_assoc`: failed only on associativity; `mul_left_comm` reported unused. Replaced it with `mul_assoc`; full scratch prefix succeeds with only the two known unused-variable warnings.
- Local `key` binder compacted and outer signature packed; scratch compilation succeeds.
- Whole proof `grind`, `exact?`, `aesop`: all fail to close (not mistaken for success merely because one result's goals list was empty).
- Final simp native probe closes its goal, leaving old trailing `ring` with “No goals to be solved”; remove ring in the selected proof.
- `apply?` yields generic partial reductions only. Whole-proof `simp [wronskian, wronskianMatrix]` merely unfolds the determinant; it does not establish the coefficient product identity.
- A one-tactic proof would still need the permutation coefficient fact, so retained the mathematically direct two-case local argument. No extracted single-use helper or new wrapper is warranted after reaching 18 body lines and branches below 10.

## Verification and diff gates

Actual commands/tools, not inferred success:

- `/Users/ramin/.elan/bin/lake build Roth.Wronskian` final session `64287`, exit 0, 1826 jobs. Log: `/private/tmp/roth-wronskian-decl08-module-final.log`.
- Native `lean_diagnostic_messages` on the whole file: success true, partial false, timed_out false, failed_dependencies empty; no errors. Only preserved copyright header and pending `hφ`/`hd` warnings.
- Complete final isolated prefix via native `lean_run_code`: success true, timed_out false; only the same two unused hypotheses, plus requested check/axiom info.
- Separate old-signature `example` applied the revised theorem to `hφ hd`: success true. The scratch application line exceeded style width, but live file maximum is 99; no mathematical/type error.
- Native `lean_verify`: standard trust, `[propext, Classical.choice, Quot.sound]`, no nonstandard axioms, source warnings empty. Independent `#print axioms` in isolated prefix agrees.
- Comment-block comparison baseline/final: true. Target source scan: no sorry/admit/axiom/native_decide/options/λ/haveI/letI/push_neg; no definitions or unrelated declarations in diff.
- Parent notified source frozen and module/LSP passed, to run full project and separate LeanEval dependent checks before publication.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual final module build exit 0 |
| definition_protected | pass | no def/abbrev changed |
| theorem_statement_protected | pass | old signature compatibility example compiles; only defeq syntax/packing/ascriptions changed; both hypotheses remain |
| structure_gate | pass | 18 body lines, non-headline result, no conjunction, branches 4 and 5 lines |
| naming_gate | pass | mathematical snake_case; no forbidden pattern; name preserved pending separate decision |
| line_packing_gate | pass | complete before/after four-row final signature table, no repack rows remain |
| inequality_orientation_gate | pass | full occurrence table, no reversed inequality |
| comments_preserved | pass | all block comments identical; no inline proof comments existed |
| axiom/source | pass | standard 3 axioms; no placeholders/options/scaffolding |
| cumulative dependent builds | parent-owned | source-frozen handoff sent; no claim here until parent's actual checks |

Overall: routine-proof gates pass, with explicit pending public-API decision on unused assumptions. No rename/decomposition work is hidden.

## Phase checklist

- [x] Step 1: required references read.
- [x] Step 2: all 24 audit items documented.
- [x] Step 2.5: five-method status and compiled generic-route probe.
- [x] Step 2.6: all parameters, actual drop-test, public literature, and concrete proposal.
- [x] Step 2.7: complete measured before/after signature tables.
- [x] Step 2.8: inequality occurrence table.
- [x] Step 3: all 42 golfing rules have a concrete status.
- [x] Step 4: whole-proof strategy reconsidered and tested.
- [x] Step 5a: complete successful native LSP diagnostics; warnings explicitly disclosed.
- [x] Step 5b: module build, diff gates, isolation, type compatibility, axioms.
- [x] Step 6a: no rename queued; optional rename awaits explicit API decision.

Rules applied: 1.10 (direct elimination of hD), 1.11, 1.14, 1.15, 2.3, plus lambda/cast/packing cleanup. Refactoring needed: decide compiled removal of `hφ` and `hd` and sole caller repair; optional rename separately. No Git operations performed by this worker.

## User-approved hypothesis amendment (2026-10-15)

The user approved removal of both unused `hφ`/`hd` arguments from
`coeff_wronskian_of_natDegree_injective`, preserving its name and conclusion,
and the minimal sole-caller update to `(φ := φ)`. A fresh narrow worker applied exactly
those two replacements. All other source, definitions, proof, documentation and the
nonvanishing caller's hypotheses remain byte-identical. Earlier pending-proposal
statements in historical checkpoints are superseded by this approval and implementation.

Wronskian source is now271→218lines,13retained declarations; the original audit count
remains15. Module28780 exit0, complete LSP zeroerrors and only the user-preserved header
warning, independent pre-target theorem/caller compilation and standard-axiom checks pass.
Actual profiling5470 exit0: all13 below750ms, maximum586.13ms; caller457.33ms.
Full `lake build` session30588 exit0 (2587jobs), followed by separate
`lake build Roth.LeanEval` session6721 exit0 (2586jobs). The full result was recovered
successfully after a usage interruption; both source hashes stayed unchanged.
Logs `/private/tmp/roth-wronskian-approved-{full,leaneval}.log`.
Frozen Wronskian SHA256 `b4f0c0db36bcbd81983f5a38c137dcefdf57bce18e12445e8241689a8abf888e`.
[Full amendment evidence](Wronskian-approved-hypotheses.md). No API proposal remains pending.
This amendment does not increment the264original-declaration tally; Taylor remains6/20,
overall61/264. Taylor7 resumes after this separate publication checkpoint.
