# Cleanup audit: `MvPolynomial.hasseDeriv_apply`

Date: 2026-10-15 (America/Chicago). Baseline: pushed checkpoint `1bfa9f3`.
Target: `Roth/HasseDeriv.lean:67–69`. Replaced the two-tactic conversion/rewrite
proof by `simp [hasseDeriv, sum_def]`, removing one line. The statement, name,
visibility, documentation, citation, imports and surrounding declarations are unchanged.

## Workflow basis

Applied the inherited mathlib-quality Phase 4 and lean4 reference instructions,
including all audit and golfing categories. This dedicated declaration worker
reused the parent's reference review and inspected the target, previous report,
relevant pinned library definitions and local mathematical source. Its tool registry
has no native Lean MCP namespace (`typeof` the native run-code method was undefined),
so actual search and diagnostics used the approved Lean LSP MCP 0.31.0 bridge.
This does not contradict the parent's independently verified native registration.

## All 24 audit items

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Complete post-edit diagnostics: no errors; only existing file-header warning. |
| 2 | HAVE SCAN | No `have` terms. |
| 3 | SET_OPTION | No local option or override. |
| 4 | SIMP SQUEEZE | Original and replacement simp are terminal; retain unsqueezed terminal simp. |
| 5 | NAMING | Operation name plus `apply` matches the pinned univariate API. No forbidden pattern. |
| 6 | LINE PACKING | Complete width table below; both lines fit 100 characters. |
| 7 | BY PLACEMENT | `by` remains at the conclusion line's end. |
| 8 | FORMAT | Four-space statement continuation, two-space proof indent, no internal blank lines. |
| 9 | COMMENTS | No proof comments; original documentation and source citation preserved. |
| 10 | DOCSTRING | Existing support-sum description accurately explains the interface. |
| 11 | VISIBILITY | Public expansion interface for the project-defined operator; retain. No explicit project caller found by name search, which does not justify an API deletion. |
| 12 | STRUCTURE | One-line equality proof, no branches or conjunctions; no extraction. |
| 13 | MATHLIB | Five methods attempted; useful local and remote results, LeanSearch unavailable (HTTP 500). |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: equality, no existential. |
| 16 | SHOW vs CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All five parameters reviewed below; no signature change warranted. |
| 19 | INEQUALITY | None; complete scan below. |
| 20 | NORMAL-FORM | Operator application expands to a finite sum of monomials with explicit coefficients. |
| 21 | SYNTAX-GEN | Support sum is the documented public computation form; changing to a bundled sum is unnecessary API churn. |
| 22 | IMPORT-FANOUT | No import or dependency change. |
| 23 | CASTS | 0 dropped / 1 kept cross-type / 0 new: natural binomial coefficient cast to R remains necessary. |
| 24 | INSTANCE-NAME | n/a: not an instance. |

## Signature width and inequality tables

Lengths are Unicode codepoints measured by Python `len`; signature is unchanged.

| Signature line | Before | After | Next syntactic unit | Arithmetic/action |
|---|---:|---:|---|---|
| 67 | 62 | 62 | Full conclusion through `:= by`, 91 without indentation | 62 + 1 + 91 = 154 > 100; ok, retain conventional colon break. |
| 68 | 95 | 95 | None; proof follows | 95 ≤ 100; ok. |

The complete equality is the conclusion unit; no arbitrary mid-expression split
is introduced just to fill the preceding line.

| Scope | Inequality occurrences | Action |
|---|---|---|
| Entire signature, hypotheses and proof | None; the conclusion uses equality | No orientation change or rename. |

## Five-method mathlib search

| Method | Query/scope | Observed result |
|---|---|---|
| A Lean-Finder | `Hasse derivative polynomial expressed as sum over support monomial coefficients` | Initial sandbox DNS failure; approved retry succeeded with `Polynomial.hasseDeriv_apply`, `hasseDeriv`, `hasseDeriv_coeff`. |
| B Loogle | `"hasseDeriv_apply"` | Initial DNS failure; approved retry succeeded with univariate `hasseDeriv_apply` and `hasseDeriv_apply_one`. |
| C LeanSearch | `Hasse derivative polynomial support sum monomials` | Initial DNS failure; approved retry returned HTTP 500. Unavailable, not an empty theorem search. |
| D Pinned source and project search | `hasseDeriv_apply`, `lsum_apply`, `sum_def`, `as_sum`; definitions of polynomial support | Found/inspected the univariate expansion, generic `Finsupp.lsum_apply`, `MvPolynomial.sum_def`, `as_sum` and definitional coefficient-support equality. |
| E Local MCP | `hasseDeriv_apply`, limit 20 | Returned the project target and two univariate matches; source search works although index reports `unavailable`. |

Bridge evidence: `/private/tmp/roth-hasseDeriv_apply-{finder,loogle,leansearch,local}.json`.
Remote candidates were checked against pinned source. The univariate expansion
has domain `Polynomial R`, so it does not replace this multivariate statement.
The generic linear-extension evaluation and polynomial sum interface already supply
the actual proof, now used directly by simplification.

Replacement considerations: retain the useful public interface for a project-defined
operator; all five methods attempted with failures explicit; generic finite-sum variants
inspected; no custom predicate to normalize; no identical existing multivariate operator
theorem established; no new import or module-documentation update needed. The common
topology/finiteness/separation equivalents table has no applicable entry. These bounded
searches do not establish exhaustive absence of related mathematics.

## Generalisation, inversion and literature

| Parameter | Role | Drop/weaken analysis |
|---|---|---|
| `{σ : Type u}` | Polynomial variable type | Already arbitrary; no finite or decidable constraint. Needed to type exponents and P. |
| `{R : Type v}` | Coefficient type | Independent universe and arbitrary type; needed throughout. |
| `[CommSemiring R]` | Structure for the current multivariate operator and its R-linear map | Current definition requires this interface. Weakening to the univariate theorem's `Semiring` would require a substantive operator refactor, not merely dropping a hypothesis. |
| `(d : σ →₀ ℕ)` | Derivative multi-index | Occurs in the input operator and output monomials; cannot remove without changing the result. |
| `(P : MvPolynomial σ R)` | Arbitrary input polynomial | Used on both sides; specializing or removing it weakens or changes the theorem. |

No propositional hypothesis, strict inequality, global analytic assumption or bundled
equivalence is present. Arbitrary variable types already permit more than finite-dimensional
polynomials; finite support is intrinsic to the polynomial representation. No approved
routine generalisation or statement adjustment emerged.

The inversion test fires: once the Hasse operator is unfolded, this is evaluation of
a generic linear extension as a finite sum. That infrastructure already exists as
`Finsupp.lsum_apply` and `MvPolynomial.sum_def`. No new generic helper is needed; the
named expansion remains a useful interface that avoids callers unfolding construction details.

Local `clean.tex` §1 defines the monomial action and its linear extension. A fresh public
literature search found the explicit multivariate coefficient sum in Definition 3.4 of
[Fast Multivariate Multipoint Evaluation over All Finite Fields](https://doi.org/10.1145/3652025).
The retrieved definition matches this support-sum form (terms outside support vanish).
Inference from that formula and the local source: no broader assertion is needed for
this elementary expansion interface. No full-paper inspection is claimed. Optional
`ask_chatgpt_math` skipped as authorized.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | No redundant exact wrapper. |
| 1.2 by rfl | No such wrapper to remove. |
| 1.3 rw + exact | No exact suffix; entire conversion/rewrite step removed by direct simplification. |
| 1.4 simp + exact | No such pair. |
| 1.5 trailing rfl | None. |
| 1.6 constructor chain | n/a: equality computation. |
| 1.7 apply + exact | None. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | No lambda in the target proof. |
| 1.10 single-use have | None. |
| 1.11 apply + intro | None. |
| 1.12 redundant show | None. |
| 1.13 have projections | None. |
| 1.14 merge rw | Only one original rw list; direct simp removes it. |
| 1.15 terminal simp only | Neither original nor replacement has squeezed terminal simp. |
| 1.16 nonterminal simp | None. |
| 1.17 dot notation | Original `P.as_sum` was natural; no longer needed. |
| 1.18 `<\|` | No nested final function argument. |
| 1.19 push Not | None. |
| 1.20 trivial existential | n/a: not existential. |
| 2.1 grind | Considered; direct one-step simplification already proves the computation, so no heavier automation trial needed. |
| 2.2 delete before grind | n/a: no grind. |
| 2.3 simpa consolidation | Direct simp consolidation independently verified; no `using` premise needed. |
| 2.4 fun_prop | n/a: no analytic/function-property goal. |
| 2.5 positivity | n/a: no positivity goal. |
| 2.6 gcongr | n/a: no inequality. |
| 2.7 lia/omega | n/a: finite-sum identity, not linear arithmetic. |
| 2.8 aesop | Considered; deterministic simp solves the goal without search, so no aesop trial needed. |
| 2.9 norm_num/norm_cast | n/a: symbolic orders and coefficients; no numeric or cast-normalization subgoal. |
| 2.10 decide/kernel | n/a: arbitrary coefficient types and polynomials, not a finite decision problem. |
| 2.11 field_simp/ring | n/a: no denominator or ring-normalization problem. |
| 2.12 linear_combination | n/a: no algebraic hypotheses to combine. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 calc | No equality chain remains; a calc block would expand the one-line proof. |
| 2.15 `<;>` | n/a: one goal with no branching. |
| 3.1 erw/rw | No erw; original rw eliminated. |
| 3.2 fun_prop | No legacy analytic tactic. |
| 3.3 omega/lia | Neither occurs. |
| 3.4 rcases rfl | No case split. |
| 3.5 automation attributes | No existing attribute; retain explicit expansion interface without adding a potentially expansive global simp rule. |
| 3.6 simp_all | No propositional context or simp_all. |
| 3.7 maxHeartbeats | No override; none introduced. |

Strategy reflection: evaluate the defining linear extension directly, then use the
polynomial sum interface to express its support. This replaces rewriting the input
polynomial into monomials and then mapping the sum; it preserves the exact conclusion.

## Experiments and validation

An isolated Lean file imported only the original library imports and copied the preceding
two definitions, excluding this target and every later theorem. Its initial
`simp [hasseDeriv, Finsupp.sum]` left the definitional equality between coefficient
support and polynomial support. Replacing `Finsupp.sum` by the polynomial-facing
`sum_def` solved the goal: `lake env lean /private/tmp/roth-hasseDeriv_apply-probe.lean`
exited 0. Thus the proof does not use the theorem being proved, directly or through simp.

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: `lake build Roth.HasseDeriv`, exit 0, 1430 jobs. `/private/tmp/roth-hasseDeriv_apply-module-build.log`. |
| post-edit LSP | PASS: complete, success=true, partial=false, timed_out=false, failed_dependencies=[]; only existing header warning. `/private/tmp/roth-hasseDeriv_apply-postedit-diagnostics.json`. |
| definition_protected | PASS: no definition/abbreviation edited. |
| theorem_statement_protected | PASS: exact statement, binders, name, visibility and documentation unchanged. |
| structure_gate | PASS: one-line proof; no branches or extraction need. |
| naming_gate | PASS: descriptive existing apply name, aligned with univariate API. |
| line_packing_gate | PASS: complete table, maximum signature width 95. |
| inequality_orientation_gate | PASS: none. |
| scoped diff | PASS: exact whole-file comparison to `git show HEAD:Roth/HasseDeriv.lean` equals only the intended proof replacement; `git diff --check` exit 0. |
| dependent closure | PASS: orchestrator full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs), both exit 0. Logs `/private/tmp/roth-hasseDeriv_apply-build.log` and `/private/tmp/roth-hasseDeriv_apply-leaneval.log`. |

No new axiom, placeholder, `native_decide`, option, import or version change.
No rename, generalisation or structural action queued. Existing header warning remains
deferred to ownership/license confirmation; no legal attribution invented.

## Phase 4 checklist

- [x] Step 1: inherited workflow/reference review and target context.
- [x] Step 2: all 24 target-specific audit dispositions.
- [x] Step 2.5: all five search methods; unavailable service distinguished from absence.
- [x] Step 2.6: every parameter, inversion and literature considered.
- [x] Step 2.7: complete signature width table.
- [x] Step 2.8: complete inequality scan.
- [x] Step 3: all 42 golfing rules considered; simpler applicable proof tested.
- [x] Step 4: strategy reconsidered and direct evaluation independently verified.
- [x] Step 5a: module build and complete fresh diagnostics passed.
- [x] Step 5b: protection, naming, structure, packing and scoped-diff gates passed.
- [x] Step 6a: no rename or structural queue entry required.

Parent owns dependent validation, shared progress logs, commit/push and file-wide phases.
