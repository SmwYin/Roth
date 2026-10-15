# Cleanup audit: `MvPolynomial.hasseCoeff_eq_prod`

Date: 2026-10-15 (America/Chicago). Baseline: pushed checkpoint `b37a775`.
Target: `Roth/HasseDeriv.lean:100`. Packed the complete signature onto one
99-character line, used dot notation for `Finsupp.prod_fintype`, and changed the
proof lambda arrow to `↦`. The mathematical statement, parameters, name,
visibility, documentation, citation and underlying library proof are unchanged.

## Workflow and all 24 audit items

This dedicated Phase 4 worker follows the inherited mathlib-quality and lean4
workflow/reference review. Native Lean MCP tools are absent from this leaf's
registry; the orchestrator supplied actual native remote-search results. Local
search and complete diagnostics worked through the approved MCP 0.31.0 bridge.

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Fresh complete diagnostics: no errors; only existing header warning. |
| 2 | HAVE SCAN | No have bindings. |
| 3 | SET_OPTION | No options present or added. |
| 4 | SIMP SQUEEZE | No simp calls; direct proof term retained. |
| 5 | NAMING | Name describes hasseCoeff as a product; established API retained. |
| 6 | LINE PACKING | Applied: complete signature fits 99 columns; see arithmetic below. |
| 7 | BY PLACEMENT | No tactic wrapper or standalone by. |
| 8 | FORMAT | Lambda uses ↦; body remains indented two spaces. |
| 9 | COMMENTS | No proof comments; source citation preserved. |
| 10 | DOCSTRING | Correctly identifies the full finite-type product. |
| 11 | VISIBILITY | Public named rewrite used in hasseCoeff_le_two_pow; retain. |
| 12 | STRUCTURE | Single direct term; no decomposition needed. |
| 13 | MATHLIB | Five methods attempted; existing generic theorem already used. |
| 14 | JUNK DEF | n/a: theorem, no definition introduced. |
| 15 | EXISTS LEMMA | No existential statement. |
| 16 | SHOW vs CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Parameter and inversion review below; no substantial API change. |
| 19 | INEQUALITY | No inequalities in statement or proof. |
| 20 | NORMAL-FORM | Named coefficient rewrites to the conventional full product. |
| 21 | SYNTAX-GEN | No custom syntax or redundant bundled predicate. |
| 22 | IMPORT-FANOUT | No imports changed; generic theorem already available. |
| 23 | CASTS | 0 dropped / 0 retained / 0 added. |
| 24 | INSTANCE-NAME | n/a: not an instance. |

## Signature width and inequality tables

Lengths are Unicode codepoints, measured with Python `len`.

| Signature line | Before | After | Next syntactic unit | Arithmetic/action |
|---|---:|---:|---|---|
| Original line 100: name and binders | 55 | 99 | Full conclusion and :=, 43 unindented characters | 55 + 1 + 43 = 99 ≤ 100; merge. |
| Original line 101: conclusion and := | 47 | Absorbed above | Entire conclusion | Removed unnecessary continuation; ok. |
| Final line 100: full signature | — | 99 | Proof term, 48 unindented characters | 99 + 1 + 48 = 148 > 100; keep proof on next line. |

Proof line shrinks from 59 to 50 characters. No split binder, overlong line,
blank line inside the declaration or avoidable signature continuation remains.

| Scope | Inequalities | Action |
|---|---|---|
| Statement | None; equality only | No orientation change. |
| Proof | None; uses choose-zero equality | No orientation change. |

## Five-method mathlib search

| Method | Query/scope | Observed result |
|---|---|---|
| A Lean-Finder | finitely supported product over support equals product over all elements of a finite type when zero maps to one | Finsupp.prod_fintype, Finsupp.onFinset_prod, DFinsupp.prod_eq_prod_fintype. |
| B Loogle | `"prod_fintype"`, limit 5 | Finsupp.prod_fintype, dependent and topological variants. |
| C LeanSearch | Finsupp product finite type full product zero maps to one | HTTP 500; unavailable, not evidence of absent results. |
| D Pinned source/project | prod_fintype, prod_of_support_subset, hasseCoeff_eq_prod | Inspected the generic proofs and actual downstream rewrite. |
| E Local MCP | prod_fintype, limit 20 | Found Finsupp.prod_fintype in pinned source; index reports unavailable, source-name matching works. |

Evidence: `/private/tmp/roth-hasseCoeff_eq_prod-native-search.json` and
`/private/tmp/roth-hasseCoeff_eq_prod-local.json`. Checked remote matches against
the project's pinned `Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:57–65`.
`Finsupp.prod_fintype` is exactly the general product conversion already used;
its premise is discharged by `Nat.choose_zero_right`. `prod_of_support_subset`
further generalizes the index set to any finite set containing the support.
The dependent-function and topological products use different representations
and add no useful simplification here.

Replacement checklist: actual usage in `hasseCoeff_le_two_pow` inspected; five
methods attempted; generic support-set and finite-type formulations checked;
no disguised predicate or alternative topology/separation definition involved.
This public theorem exposes the project-specific definition through a convenient
rewrite without unfolding it at callers. Its proof already delegates all generic
work to mathlib. Retain that API; adding a second generic theorem or deleting this
named rewrite is not warranted. Bounded search is not an exhaustive absence claim.

## Generalisation, inversion and literature

| Parameter/context | Assessment |
|---|---|
| `{σ : Type u}` | Arbitrary universe/type, including empty types; no nonempty assumption. |
| `[Fintype σ]` | Required to express the given unrestricted finite product. Replacing it with Finite would require inserting a chosen enumeration into the statement. |
| `(d : σ →₀ ℕ)` | Supplies the finite support and lower binomial indices; essential. |
| `(k : σ →₀ ℕ)` | Supplies upper binomial indices and is required by the current hasseCoeff definition. |
| Ambient R and CommSemiring R | Not included in the elaborated theorem; it is purely about natural numbers. No unused instance to remove. |

There is no propositional assumption to weaken or localize. A product over an
arbitrary finite set containing d.support would remove global finiteness, but
that generalization is already provided by `Finsupp.prod_of_support_subset`.
No new project API is proposed for it. Changing k to an arbitrary function first
requires the earlier hasseCoeff definition change already recorded as deferred;
this checkpoint leaves that definition and all statements intact. Thus that
inherited substantial-definition proposal remains unapplied under the user's
approval requirement, while this declaration's routine cleanup is complete.

Inversion review: the underlying principle is that extending a product by factors
equal to one does not change it. Mathlib already captures precisely that principle
for arbitrary zero-valued finitely supported maps and commutative monoid targets.
The current proof is already the desired abstraction reuse, rather than a manual
binomial-specific proof requiring extraction.

Local `clean.tex` §1 defines the binomial factor as the product over all p variables.
A fresh inspection of §2.1, p.6 of
[Dvir–Kopparty–Saraf–Sudan, Extensions to the Method of Multiplicities](https://eccc.weizmann.ac.il/report/2009/004/download/)
confirmed the same multi-index binomial convention. Inference: the support product
agrees with that convention because every omitted lower index is zero and the
corresponding binomial factor is one. The paper is not claimed to discuss this
Lean representation or its finite-support conversion theorem. Optional
ask_chatgpt_math skipped as authorized.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | No redundant tactic wrapper. |
| 1.2 by rfl | No wrapper; equality uses a genuine support-product theorem. |
| 1.3 rw + exact | None; direct library term already used. |
| 1.4 simp + exact | None. |
| 1.5 trailing rfl | None. |
| 1.6 constructor chain | No constructor chain. |
| 1.7 apply + exact | None; direct term retained. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | The lambda supplies the coordinate-indexed choose-zero proof; retained. |
| 1.10 single-use have | None. |
| 1.11 apply + intro | None. |
| 1.12 redundant show | None. |
| 1.13 have projections | None. |
| 1.14 merge rw | No rw calls. |
| 1.15 terminal simp only | No simp call. |
| 1.16 nonterminal simp | None. |
| 1.17 dot notation | Applied: d.prod_fintype replaces Finsupp.prod_fintype _; explicit subject improves readability. |
| 1.18 `<\|` | Trailing lambda already parses without extra parentheses. |
| 1.19 push Not | No push_neg. |
| 1.20 trivial existential | No existential. |
| 2.1 grind | Direct deterministic library proof needs no search. |
| 2.2 delete before grind | n/a: no grind. |
| 2.3 simpa consolidation | No tactic sequence to consolidate. |
| 2.4 fun_prop | No function-property goal. |
| 2.5 positivity | No positivity subgoal. |
| 2.6 gcongr | Equality, not monotonicity. |
| 2.7 lia/omega | No arithmetic reasoning needed beyond choose_zero_right. |
| 2.8 aesop | Direct library term is clearer and avoids search. |
| 2.9 norm_num/norm_cast | No numerical instance or casts. |
| 2.10 decide/kernel | Symbolic product theorem, not a closed decision. |
| 2.11 field_simp/ring | No denominators or polynomial normalization needed. |
| 2.12 linear_combination | No equations to combine. |
| 2.13 wlog | No symmetric case split. |
| 2.14 calc | Single equality already supplied by one theorem. |
| 2.15 `<;>` | No branching tactic sequence. |
| 3.1 erw/rw | Neither occurs. |
| 3.2 fun_prop | No legacy analytic tactic. |
| 3.3 omega/lia | Neither occurs. |
| 3.4 rcases rfl | No destructuring. |
| 3.5 automation attributes | No attributes changed or needed for existing explicit rewrite. |
| 3.6 simp_all | No tactic context to simplify. |
| 3.7 maxHeartbeats | No override present or added. |

Strategy reflection: a direct generic theorem is already the simplest proof.
Changing to tactic search would obscure that dependency. The useful changes are
packing and readable notation; the mathematical strategy remains unchanged.

## Experiments and validation

The isolated probe imports only the original mathlib dependencies, copies the
hasseCoeff definition, and states the cleaned theorem as `probe`. It imports
neither the actual target nor its downstream declarations. `lake env lean` exited
0; `#print axioms` returned `[propext, Classical.choice, Quot.sound]`; `#check`
confirmed only σ, Fintype σ, d and k are parameters. Evidence:
`/private/tmp/roth-hasseCoeff_eq_prod-probe.lean`.

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: lake build Roth.HasseDeriv, exit 0, 1430 jobs. /private/tmp/roth-hasseCoeff_eq_prod-module-build.log. |
| post-edit LSP | PASS: complete success=true, partial=false, timed_out=false, failed_dependencies=[]; no errors, only existing header warning. /private/tmp/roth-hasseCoeff_eq_prod-postedit-diagnostics.json. |
| definition_protected | PASS: no definition or abbreviation changed. |
| theorem_statement_protected | PASS: whitespace-normalized statement identical, same binders, name and visibility. |
| structure_gate | PASS: one direct term remains; no extraction needed. |
| naming_gate | PASS: established descriptive rewrite name retained. |
| line_packing_gate | PASS: table accounts for every old and new signature line; maximum 99. |
| inequality_orientation_gate | PASS: no inequalities. |
| scoped diff | PASS: replacing only this declaration in HEAD reproduces the complete source file; git diff --check exit 0. |
| dependent closure | PASS: orchestrator full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs), both exit 0. Logs `/private/tmp/roth-hasseCoeff_eq_prod-build.log` and `/private/tmp/roth-hasseCoeff_eq_prod-leaneval.log`. |

No sorry, new axiom, native_decide, option, import, version or unrelated source edit.
No rename/structural action queued. Earlier k-parameter definition generalization
remains deferred as explained above; existing header warning remains deferred
pending actual ownership/license information.

## Phase 4 checklist

- [x] Step 1: inherited workflow/references and target context reviewed.
- [x] Step 2: all 24 target audit dispositions.
- [x] Step 2.5: all five searches, including unavailable LeanSearch disclosure.
- [x] Step 2.6: every parameter, inversion and local/public literature reviewed.
- [x] Step 2.7: complete signature width table and packing applied.
- [x] Step 2.8: complete inequality scan.
- [x] Step 3: all 42 golfing rules considered.
- [x] Step 4: direct-proof strategy reassessed and independent probe compiled.
- [x] Step 5a: module build and complete fresh diagnostics passed.
- [x] Step 5b: protection, structure, naming, packing and scoped-diff gates passed.
- [x] Step 6a: no new rename/structure queue; earlier definition proposal remains deferred.

Parent owns dependent validation, shared progress logs, commit/push and file-wide phases.
