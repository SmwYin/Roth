# `MvPolynomial.eval_eq_sum_box` — final original declaration audit

Scope: only this declaration in `Roth/Taylor.lean` (original inventory L231–235;
worker-entry L212–216; final L212–215) and this report. Baseline commit supplied by
parent: `8994327`, branch `ramin-cleanup`; worker-entry file SHA256
`eda896cd346e776d923237cdc4235045d1dd2e4fe32a8d039f561ca6068221a6`.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read both skills, the complete
worker contract, naming conventions, relevant style sections, review stages, and
the source Taylor theorem in `.mathlib-quality/references/clean.tex` L500–527.
Session authorization to preserve existing mathematical API/docstrings/header
overrides conflicting generic deletion/visibility/documentation advice.

Result: replace conversion rewriting followed by `simp` with the direct evaluation
of the preceding polynomial identity:

```lean
  simpa using congrArg (eval x) (eq_sum_box_hasseDeriv α r P hP)
```

The signature's `P` binder now fits on its first line, exactly 100 codepoints.
The theorem's type, name, visibility and docstring are unchanged. No substantive
mathematical proposal was necessary.

## Full 24-item audit

| # | Item | Actual finding/action |
|---|---|---|
| 1 | LINT | Complete native diagnostics before/after: no target warnings/errors. Preserved pre-existing file L1 copyright warning. |
| 2 | HAVE SCAN | Zero `have` declarations in either body; no single-use intermediary. |
| 3 | SET_OPTION | No local options or resource limits; none introduced. |
| 4 | SIMP SQUEEZE | Original `simp` was terminal; final `simpa` closes the entire goal, unsqueezed. |
| 5 | NAMING | `eval_eq_sum_box` describes evaluation as a box sum; no forbidden pattern/abbreviation, no rename required. |
| 6 | LINE PACKING | Initial L212 had 77 chars and next binder 22 chars: 77+1+22=100. Moved binder; complete final table below. |
| 7 | BY PLACEMENT | `by` remains on the final signature line. |
| 8 | FORMAT | Two-space proof indent; one tactic; no internal empty line, semicolon chain, `haveI`, or `letI`. |
| 9 | COMMENTS | No proof-body comments existed; docstring and surrounding module documentation byte-preserved. |
| 10 | DOCSTRING | Existing two-line source-citing evaluation-form docstring preserved under Rule A. |
| 11 | VISIBILITY | Public headline result used as evaluated Taylor API; preserve public visibility. |
| 12 | STRUCTURE | Body shrinks 2 to 1 lines; no conjunction/case split; below headline 15-line threshold. |
| 13 | MATHLIB | All five methods executed; generic evaluation API and univariate Taylor are partial matches, not this multivariate box result. Details below. |
| 14 | JUNK DEF | n/a: theorem, no definition. |
| 15 | EXISTS LEMMA | n/a: no existential statement/helper. |
| 16 | SHOW vs CHANGE | Neither tactic occurs. |
| 17 | PUSH_NEG | No negation-pushing tactic occurs. |
| 18 | GENERALISE | All parameters audited and compiled drop/parent probes below; no successful semantic weakening. |
| 19 | INEQUALITY | Only `degreeOf j P ≤ r j`; no reversed inequalities or `_ge_`/`_gt_` name. Table below. |
| 20 | NORMAL-FORM | Canonical explicit finite Taylor expansion RHS; evaluation morphism directly transports polynomial identity. No new normal form/attribute. |
| 21 | SYNTAX-GEN | Explicit center/evaluation point/coordinate bound remain convenient for applying and rewriting. Equivalent support-bound reformulation adds no demonstrated benefit. |
| 22 | IMPORT-FANOUT | n/a: no import added or changed. |
| 23 | CASTS | 0 dropped / 0 cross-type / 0 load-bearing casts in diff. `(eval x)` groups a function, not a type cast. |
| 24 | INSTANCE-NAME | n/a: no instance declaration. |

Issues fixed: underpacked first signature line; conversion proof replaced by direct
transport of equality. Refactoring needed: none. Renames queued: none.

## Mathlib search status

| Method | Query/evidence | Result |
|---|---|---|
| A Lean-Finder | `MvPolynomial evaluate Taylor expansion Hasse derivative finite sum degree bound`, 3 results | `Polynomial.taylor_coeff`, `Polynomial.eval_sumIDeriv_of_pos`, `Polynomial.aeval_sumIDeriv`: univariate partial matches. |
| B Loogle | `MvPolynomial.eval, Finset.sum`, 3 results | `MvPolynomial.eval_sum`, `MvPolynomial.eval_eq'`, `MvPolynomial.eval_eq`; generic evaluation building blocks. |
| C LeanSearch | `multivariate polynomial Taylor expansion evaluation Hasse derivatives`, 3 results | `Polynomial.taylor_coeff`, `Polynomial.taylor`, `Polynomial.taylor_apply`; univariate analogues. |
| D Source `rg` | Full `eval_eq_sum_box`, `eval.*taylor`, `taylor.*eval`, `eq_sum.*hasse` over mathlib MvPolynomial and Polynomial/Taylor | No full-name multivariate box hit; `Polynomial.taylor_eval`, `Polynomial.taylor_eval_sub`, and coefficient results are partial analogues. Untruncated bounded-topic search. |
| E Name search | Native `lean_local_search`, `eval_eq_sum`, limit 6 | Local target plus Polynomial sum/range results; index warming explicitly reported, so not relied on alone. Source and compiled checks supplied independent evidence. |

Auxiliary variants checked: `eval_sum`, `eval_eq`, `eval_eq'`, `taylor_coeff`,
`taylor_eval`, `taylor_eval_sub`, and range/degree bounds. Compiled `#check`
confirmed `@MvPolynomial.eval_sum` and `@MvPolynomial.eval_eq'` in the actual imports.
Common-equivalents table: no discrete/finite/bornology disguise applies.

Compiled live `exact?` failed to close the target. `apply?` exhausted its bounded
search and offered only generic partial constructions, not a complete theorem.
This is evidence from elaboration, not an absence claim based solely on grep.
No matching replacement was discovered; retain the existing public result,
building directly on the project's substantial polynomial Taylor theorem and
mathlib evaluation simplification. All six strict rules considered: no new
wrapper/predicate, exhaustive searches plus elaboration probe, auxiliary variants
checked, no equivalent warranting deletion, and existing module documentation
preserved under the stronger session instruction. A generic `eval_sum` lemma alone
does not prove the Taylor formula.

## Generalisation status

Mechanical probes use the entire pretarget prefix with the target excluded, close
its sections, then restate one candidate with `autoImplicit false`. Each is compiled
by `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-decl20-<candidate>.lean`.
No source mutation was made to test public API changes. Logs are beside scratch
files with `.lean.log` suffix. All rejected candidates exited 1 with actual Lean
errors; no timeout or resource-limit override was used.

| Parameter | Class/use | Candidates tested | Evidence/result |
|---|---|---|---|
| `{σ : Type*}` | Index type throughout | Drop (`drop_sigma`); universe widening | Unknown `σ`; already universe-polymorphic, no wider universe candidate. |
| `{A : Type*}` | Coefficient type throughout | Drop (`drop_A`); universe widening | Unknown `A`; already independently universe-polymorphic. |
| `[CommRing A]` | Polynomial evaluation, product and subtraction | Drop, `[Ring A]`, `[CommSemiring A]` | Drop/Ring fail `CommSemiring A` synthesis; CommSemiring fails subtraction synthesis and predecessor argument compatibility. Retained. |
| `[Fintype σ]` | Box and full coordinate product | Drop (`drop_Fintype`) | Missing `Fintype σ` at RHS box. `[Finite σ]` alone cannot elaborate this exact signature; changing binder construction would restate public API, no demonstrated need. |
| `[DecidableEq σ]` | `Roth.box r` signature | Drop (`drop_DecidableEq`) | Missing `DecidableEq σ` at RHS box. Proof-local classical choice cannot repair a signature that fails before entering the proof. |
| `α : σ → A` | Center in coefficients and differences | Drop (`drop_alpha`) | Unknown `α` in conclusion. No continuity/global-pointwise predicate or strict hypothesis to weaken. |
| `x : σ → A` | Evaluation point and differences | Drop (`drop_x`) | Unknown `x` in conclusion. No catalogue property weakening applies to this value. |
| `r : σ → ℕ` | Box and degree bound | Drop (`drop_r`, corrected probe) | Unknown `r` in bound/conclusion. Natural exponents are the polynomial API, not an induction-only parameter eligible for arbitrary order types. |
| `P : MvPolynomial σ A` | Polynomial and degree bound | Drop (`drop_P`) | Unknown `P`. Already arbitrary polynomial; no concrete restriction. |
| `hP : ∀ j, degreeOf j P ≤ r j` | Supplies predecessor degree bound | Drop (`drop_hP`) | Unknown `hP` at predecessor invocation. Already weak `≤`; no strict-to-weak candidate. Point-localisation would lose other coordinate bounds required by box truncation. |

The initially generated `drop_r` probe did not remove the newline-adjacent binder;
its exit 0 was correctly rejected as evidence. The corrected candidate removed the
binder and failed with unknown `r`, recorded above. Binder deletion failures for
values/types establish syntactic dependency, not an independent impossibility
theorem. No successful generalisation is claimed from them.

Inversion check: the result is parametric in an arbitrary polynomial, center and
point. Applying any function to an equality is already `congrArg`; that abstraction
is now used directly, so no new abstract theorem is needed. Big-change candidates:
none supported by a compiled useful statement; none applied.

## Public literature search

Queries: `Hasse derivative multivariate Taylor expansion arbitrary commutative ring
generalization`; `"Hasse derivative" "Taylor" "commutative ring" multivariate`.
Top three results from the focused query:

1. [Fast Multivariate Multipoint Evaluation over All Finite Fields, §3.2](https://doi.org/10.1145/3652025): Hasse derivatives over commutative rings, matching coefficient generality.
2. [Putz thesis, Theorem 1.28](https://research.vu.nl/files/367784086/Thesis_CasperPutz.pdf): univariate Hasse–Taylor expansion, a related special case.
3. [Faster Algorithms for Multivariate Interpolation With Multiplicities](https://perso.ens-lyon.fr/gilles.villard/BIBLIOGRAPHIE/PDF/ieee-2015.pdf): multivariate Hasse Taylor expansion over a commutative ring with unity.

Primary-source search text supports the arbitrary commutative-ring formulation;
no characteristic-zero/domain/field condition is needed. The current theorem
already has this generality, exceeding the local source's real coefficients.
ChatGPT math MCP: n/a, no mathematical consultation tool exposed in ALL_TOOLS;
the exposed ChatGPT tools concern Pages, not mathematical second opinions.
Literature-driven API-change proposals: none.

## Line packing

`#check @MvPolynomial.eval_eq_sum_box` at `format.width 100`:

```text
@MvPolynomial.eval_eq_sum_box : ∀ {σ : Type u_1} {A : Type u_2} [inst : CommRing A] [inst_1 : Fintype σ]
  [inst_2 : DecidableEq σ] (α x : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A),
  (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) →
    (MvPolynomial.eval x) P =
      ∑ d ∈ Roth.box r, (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) * ∏ j, (x j - α j) ^ d j
```

Initial L212: 77 + 1 + 22 (`(P : MvPolynomial σ A)`) = 100 → repack, applied.
The conclusion is one equation, measured as the complete next syntactic unit.

| Final sig line | Codepoints | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 212 | 100 | `(hP : ∀ j, degreeOf j P ≤ r j)` (30) | 100+1+30=131 >100 | ok |
| 213 | 36 | Complete conclusion and `:= by` (83) | 36+1+83=120 >100 | ok |
| 214 | 87 | No next signature line | n/a, proof next | ok |

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | L213 hypothesis `hP` | `degreeOf j P ≤ r j` | Already oriented | none |
| n/a | Entire signature | No `≥` or `>` in Lean code | none | No `_ge_`/`_gt_` name |

## All 42 golfing rules

| Rule | Status/evidence |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | n/a: no rewrite followed by exact. |
| 1.4 | Applied principle: evaluation equality transported by `congrArg`, terminal simplification consolidated into one `simpa using`. |
| 1.5 | n/a: no trailing `rfl`. |
| 1.6 | n/a: no constructor. |
| 1.7 | n/a: no apply/exact pair. |
| 1.8 | n/a: no contradiction proof. |
| 1.9 | Already eta-reduced: use `(eval x)` directly. |
| 1.10 | n/a: no `have`. |
| 1.11 | n/a: no apply/intro pair. |
| 1.12 | n/a: no `show`. |
| 1.13 | n/a: no projected conjunction. |
| 1.14 | n/a: no sequential rewrite pair. |
| 1.15 | n/a: no terminal `simp only`. |
| 1.16 | n/a: original simp terminal, final simpa terminal. |
| 1.17 | n/a: `congrArg` is the direct general equality API; no improved dot-form chain. |
| 1.18 | n/a: both grouped applications are explicit arguments of `congrArg`; no trailing lambda/by block. |
| 1.19 | n/a: no `push_neg`. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Native attempt `grind` failed; `grind [eq_sum_box_hasseDeriv α r P hP]` also failed. |
| 2.2 | n/a: no grind retained. |
| 2.3 | Applied direct one-line `simpa using congrArg ...`; compiled and complete diagnostics. |
| 2.4 | n/a: no function regularity proposition. |
| 2.5 | n/a: no positivity/nonzero goal. |
| 2.6 | n/a: equality expansion, no monotone inequality goal. |
| 2.7 | n/a: no natural/integer arithmetic goal. |
| 2.8 | Native `aesop` tried: failed, made no progress. |
| 2.9 | n/a: no concrete numerical/cast goal. |
| 2.10 | n/a: arbitrary coefficient ring equality is not finite decidable computation. |
| 2.11 | n/a: no denominators. |
| 2.12 | n/a: no `ring` ending or ring-normalisation subproof. |
| 2.13 | n/a: no symmetric branches. |
| 2.14 | n/a: no calc chain. |
| 2.15 | n/a: single goal. |
| 3.1 | n/a: no `erw`. |
| 3.2 | n/a: no continuity/measurability tactic. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases/substitution. |
| 3.5 | No attribute added: Taylor expansion increases expression size and introduces center/bound, so an unconditional simp normal form is inappropriate. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no resource-limit option. |

Step-back reflection: native whole-proof `simp` made no progress, `grind` and
`aesop` failed, `exact?` found no complete lemma, and bounded `apply?` supplied only
generic partial suggestions. The explicit congruence proof succeeds and states
the mathematical step directly. The first multi-attempt accidentally targeted
blank L217 (all syntax errors), was discarded, and was rerun at correct L215.
Inserting the successful one-line snippet above the old terminal simp produced
`No goals to be solved` at L216; deleting that now-superfluous old tactic and
running actual diagnostics/build verified the complete replacement.

## Verification gates and 11 required checks

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | PASS | `/Users/ramin/.elan/bin/lake build Roth.Taylor` exit 0 after proof change (12s module), and again after signature packing (17s module), 1439 jobs successful. |
| definition_protected | PASS | Worker snapshot diff has no def/abbrev changes. |
| theorem_statement_protected | PASS | Whitespace-normalised pre-`:= by` type exactly equal to worker-entry signature. |
| structure_gate | PASS | One-line body; no conjunction or branch. |
| naming_gate | PASS | No forbidden name pattern/abbreviation. |
| line_packing_gate | PASS | All three signature lines measured above; first line exactly 100. |
| inequality_orientation_gate | PASS | Actual signature scan finds zero reversed inequalities. |
| docs/API/scope | PASS | Snapshot substitution check proves all text outside owned declaration byte-identical; docstring outside replacement span identical. |
| original-type isolated proof | PASS | `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-decl20-originaltype.lean` exit 0; full pretarget prefix, excluding target declaration, independently states/proves its original type. |
| standard axioms | PASS | Compiled isolated theorem and imported target both print exactly `[propext, Classical.choice, Quot.sound]`. |
| complete native LSP | PASS | Final whole-file diagnostic result `success=true, partial=false, timed_out=false, failed_dependencies=[]`; only original L1 header warning. |

Overall: PASS. No sorry, custom axiom, native_decide, raised limits, changed imports,
public deletion or docstring change. Parent owns the separate full project build
and post-build LeanEval checks; this report does not claim those gates.

Before 5 declaration lines / after 4 / saved 1; proof body 2 → 1.
Issues fixed 2; refactoring deferred 0; comments removed 0; renames queued none.

Phase checklist (all 11):

- [✓] Step 1 references.
- [✓] Step 2 complete 24-item audit.
- [✓] Step 2.5 five searches.
- [✓] Step 2.6 parameter/generalisation and literature.
- [✓] Step 2.7 width table.
- [✓] Step 2.8 inequality table.
- [✓] Step 3 all 42 rules.
- [✓] Step 4 reflection and actual alternatives.
- [✓] Step 5a complete native diagnostics.
- [✓] Step 5b actual diff/module/isolated-proof/axiom gates.
- [✓] Step 6a no rename needed.

Source frozen SHA256 `4878106187d61fe102f4f1b52582772cbc6938085e3e1e1845843279cfd356de`.
Freeze communicated to parent after final module gate and native diagnostics.
Source ownership revoked; subsequent work limited to report and `/private/tmp`
negative-parameter probes. No Git command or full-project build run by this worker.
