# Cleanup audit: `MvPolynomial.hasseCoeff_eq_zero_iff`

Date: 2026-10-15 (America/Chicago). Baseline: pushed checkpoint `373ec6d`.
Target: `Roth/HasseDeriv.lean:74–76`. Replaced terminal `simp only` by terminal
`simp`, retaining the structural unfolding and removing explicit `not_le` and
`exists_prop`, which the simp set already handles. The statement, binders, name,
visibility, documentation, citation, imports and other declarations are unchanged.

## Workflow basis

This dedicated Phase 4 worker applied mathlib-quality and lean4, reusing the inherited
reference review and inspecting the declaration, previous audit, local source and
pinned library. Native Lean MCP tools are absent from this leaf's registry; actual
searches and fresh diagnostics used the approved Lean LSP MCP 0.31.0 bridge.
No installation or activation claim is made from this worker's tool availability.

## All 24 audit items

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Complete post-edit diagnostics: no errors; only existing file-header warning. |
| 2 | HAVE SCAN | None. |
| 3 | SET_OPTION | No override present or added. |
| 4 | SIMP SQUEEZE | Terminal simp-only replaced by independently verified terminal simp. |
| 5 | NAMING | Operation name followed by `eq_zero_iff` accurately describes the equivalence. |
| 6 | LINE PACKING | Signature is already one 81-character line; proof packing checked below. |
| 7 | BY PLACEMENT | `by` remains at the signature line's end. |
| 8 | FORMAT | Two-space proof indent, four-space list continuation, no internal blank lines. |
| 9 | COMMENTS | No proof comments; original documentation and source citation preserved. |
| 10 | DOCSTRING | Accurately states vanishing of the natural-number binomial factor. |
| 11 | VISIBILITY | Public interface used by coefficient/constant results here and twice in Taylor.lean; retain. |
| 12 | STRUCTURE | One tactic, no branches or conjunction construction; no extraction warranted. |
| 13 | MATHLIB | Five methods attempted; local/Loogle/Finder useful, LeanSearch HTTP 500. |
| 14 | JUNK DEF | n/a: theorem. |
| 15 | EXISTS LEMMA | Public statement is an iff; existential appears only after unfolding pointwise order. |
| 16 | SHOW vs CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None; standard simp lemmas normalize the negation. |
| 18 | GENERALISE | Every parameter reviewed below; broader coefficient definition deferred. |
| 19 | INEQUALITY | One negated non-strict order, with smaller multi-index on the left. |
| 20 | NORMAL-FORM | Vanishing of coefficient relates to failure of coordinatewise domination; suitable public interface. |
| 21 | SYNTAX-GEN | No custom syntax or unnecessary bundled structure. |
| 22 | IMPORT-FANOUT | No import/dependency change. |
| 23 | CASTS | 0 dropped / 0 retained / 0 added. The coefficient is in ℕ. |
| 24 | INSTANCE-NAME | n/a: not an instance. |

## Signature width and inequality tables

Lengths are Unicode codepoints measured with Python `len`.

| Signature line | Before | After | Next syntactic unit | Arithmetic/action |
|---|---:|---:|---|---|
| 74, complete declaration signature | 81 | 81 | None; proof follows | 81 ≤ 100; ok. |

Proof line 75 has length 98; appending the remaining ` not_forall]` would give
98 + 12 = 110 > 100, so the continuation at line 76 is required. Its length is 15.

| Occurrence | Orientation | Action |
|---|---|---|
| Signature `¬d ≤ k` | Coordinatewise derivative order d compared to upper exponent k; smaller side left | Retain. The negation is essential; replacing ≤ by < changes the boundary. |
| Proof | No explicit inequality expression, only named library lemmas | No rewrite or rename. |

## Five-method mathlib search

| Method | Query/scope | Observed result |
|---|---|---|
| A Lean-Finder | `product of binomial coefficients is zero iff some lower index exceeds upper index` | Initial sandbox DNS failure; approved retry returned `Nat.choose_eq_zero_iff`, `Nat.choose_eq_zero_of_lt`, `Ring.multichoose_neg_of_lt`. |
| B Loogle | `"choose_eq_zero_iff"` | Initial DNS failure; approved retry returned the exact natural-number criterion. |
| C LeanSearch | `product of binomial coefficients vanishes if lower multi-index is not bounded above` | Initial DNS failure; approved retry returned HTTP 500. Service unavailable, not evidence of no matches. |
| D Pinned source/project search | `choose_eq_zero_iff`, `prod_eq_zero_iff`, target name | Inspected natural choose zero criterion, generic finite/Finsupp product zero criteria, and project callers. |
| E Local MCP | `hasseCoeff`, limit 20 | Found seven project coefficient declarations; index reports `unavailable`, but source-name matches work. |

Bridge evidence: `/private/tmp/roth-hasseCoeff_eq_zero_iff-{finder,loogle,leansearch,local}.json`.
Pinned `Mathlib/Data/Nat/Choose/Basic.lean` provides the exact factor criterion;
`Mathlib/Algebra/BigOperators/Finsupp/Basic.lean` supplies a generic product-zero iff.
The retained proof already composes the generic finite-product criterion with the
natural binomial criterion and pointwise order. The ring multichoose candidate concerns
a different operation, so it does not replace this statement.

Replacement checks: public wrapper has actual downstream uses; all five methods
attempted with failures disclosed; generic product and coordinatewise variants inspected;
no custom predicate to normalize; no identical theorem for this project-specific
definition established; no import or module-documentation update needed. The common
topology/finiteness/separation equivalents table has no applicable entry. These bounded
searches do not establish exhaustive absence of related mathematics.

## Generalisation, inversion and literature

| Parameter/context | Role and analysis |
|---|---|
| `{σ : Type u}` | Already arbitrary, with no finiteness/decidability/nonemptiness assumption. Needed to type the multi-indices. |
| `(d : σ →₀ ℕ)` | Finite support defines the product; occurs in both sides. Dropping or fixing it changes the result. |
| `(k : σ →₀ ℕ)` | Upper exponent occurs in the factor and order comparison. Could conceptually be an arbitrary function if the underlying coefficient definition were generalized. |
| Section `{R}` and `[CommSemiring R]` | Not used and not captured by this theorem; isolated `#check` confirms only σ, d and k. No omit annotation is needed. |

There are no propositional assumptions to drop or analytic/global hypotheses to localize.
The existing theorem already exceeds the finite-variable presentation of the local source.
Generalizing k to `σ → ℕ` would require changing the earlier public definition and restating
this result using pointwise order/coercions. This is the same substantive API proposal
already deferred in the hasseCoeff audit: leave it unapplied pending user approval,
and continue independent cleanup as the user authorized. No duplicate implementation
or new generalized theorem is introduced here. Arbitrary natural coefficients cannot
be replaced by arbitrary semiring casts while retaining this iff: positive characteristic
can make additional binomial factors zero (for example, choose(2,1) in characteristic 2).

The inversion test fires: the proof is generic product-zero reasoning plus the standard
binomial zero criterion. Both ingredients already exist; no new generic helper is needed.
Keeping the named theorem avoids downstream callers unfolding a project definition.

Local `clean.tex` §1 explicitly gives the zero case when coordinatewise domination fails.
A fresh public literature search and inspection of §2.1, p.6 of
[Dvir–Kopparty–Saraf–Sudan, Extensions to the Method of Multiplicities](https://eccc.weizmann.ac.il/report/2009/004/download/)
confirmed the product definition of a multi-index binomial coefficient and its relation
to Hasse derivatives. Inference: over ℕ, the product vanishes exactly when one component
binomial vanishes; this is the natural supporting criterion here. The paper is not claimed
to state this exact Lean iff. A separate attempted JACM page fetch returned HTTP 403;
no unavailable page content was relied on. Optional `ask_chatgpt_math` skipped as authorized.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | No exact wrapper. |
| 1.2 by rfl | No such wrapper. |
| 1.3 rw + exact | Neither occurs. |
| 1.4 simp + exact | No exact suffix. |
| 1.5 trailing rfl | None. |
| 1.6 constructor chain | One-step simplification proves the iff; no manual pair construction. |
| 1.7 apply + exact | None. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | No target lambda. |
| 1.10 single-use have | None. |
| 1.11 apply + intro | None. |
| 1.12 redundant show | None. |
| 1.13 have projections | None. |
| 1.14 merge rw | No rw. |
| 1.15 terminal simp only | Applied: terminal simp is unsqueezed; two default logical lemmas need no explicit mention. |
| 1.16 nonterminal simp | None. |
| 1.17 dot notation | Named structural lemmas, no suitable receiver expression. |
| 1.18 `<\|` | No nested final function argument. |
| 1.19 push Not | No push_neg; simp normalizes existing negated order. |
| 1.20 trivial existential | No existential construction. |
| 2.1 grind | Direct deterministic simp succeeds; heavier search not needed. |
| 2.2 delete before grind | n/a: no grind. |
| 2.3 simpa consolidation | Direct simp closes goal; no premise for a using clause. |
| 2.4 fun_prop | n/a: no analytic/function-property goal. |
| 2.5 positivity | No independent positivity subgoal; exact zero criterion already available. |
| 2.6 gcongr | n/a: iff, not a monotonicity bound. |
| 2.7 lia/omega | Symbolic product/choose iff; structural library lemmas suffice without arithmetic automation. |
| 2.8 aesop | Direct simp already succeeds; no search needed. |
| 2.9 norm_num/norm_cast | No numeric evaluation or casts. |
| 2.10 decide/kernel | Arbitrary variable type and exponents, no finite closed decision problem. |
| 2.11 field_simp/ring | No field denominator or polynomial ring identity. |
| 2.12 linear_combination | No algebraic hypotheses to combine. |
| 2.13 wlog | No symmetric cases. |
| 2.14 calc | No equality/inequality chain; adds structure to a one-tactic proof. |
| 2.15 `<;>` | Single goal, no branching. |
| 3.1 erw/rw | Neither occurs. |
| 3.2 fun_prop | No legacy analytic tactic. |
| 3.3 omega/lia | Neither occurs. |
| 3.4 rcases rfl | No case split. |
| 3.5 automation attributes | No attribute added: retain established explicit API and avoid unnecessary global simp changes. |
| 3.6 simp_all | No propositional context requiring it. |
| 3.7 maxHeartbeats | No override present or added. |

Strategy reflection: preserve the existing mathematical argument, letting terminal simp
handle routine logical normalization. No benefit from manual forward/backward witnesses
or added helper lemmas; the proof remains one deterministic tactic over standard criteria.

## Experiments and validation

An isolated probe imports only the original mathlib dependencies and copies hasseCoeff;
it excludes this target and every later project result. The first smaller list
`simp [hasseCoeff, Finsupp.prod, Finsupp.le_iff, not_forall]` left the finite-product-zero
equivalence unsolved. Adding `Finset.prod_eq_zero_iff` and `Nat.choose_eq_zero_iff`
produced the chosen proof, compiled with exit 0. A subsequent named-probe check confirmed
the parameter list and only standard axioms `[propext, Classical.choice, Quot.sound]`.
Evidence: `/private/tmp/roth-hasseCoeff_eq_zero_iff-probe.lean`. No circular simp reuse.

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: `lake build Roth.HasseDeriv`, exit 0, 1430 jobs. `/private/tmp/roth-hasseCoeff_eq_zero_iff-module-build.log`. |
| post-edit LSP | PASS: complete, success=true, partial=false, timed_out=false, failed_dependencies=[]; only existing header warning. `/private/tmp/roth-hasseCoeff_eq_zero_iff-postedit-diagnostics.json`. |
| definition_protected | PASS: no definition or abbreviation changed. |
| theorem_statement_protected | PASS: exact binders, statement, name, visibility and documentation unchanged. |
| structure_gate | PASS: one tactic, no branches/extraction needed. |
| naming_gate | PASS: existing descriptive name retained. |
| line_packing_gate | PASS: complete signature table; source maximum in target 98. |
| inequality_orientation_gate | PASS: sole negated order has d on left, k on right. |
| scoped diff | PASS: whole-file comparison to HEAD equals only the intended proof replacement; `git diff --check` exit 0. |
| dependent closure | PASS: orchestrator full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs), both exit 0. Logs `/private/tmp/roth-hasseCoeff_eq_zero_iff-build.log` and `/private/tmp/roth-hasseCoeff_eq_zero_iff-leaneval.log`. |

The bridge emitted an asynchronous destructor warning after returning complete successful
diagnostics and exited 0; it did not report a Lean error or partial result. No new axiom,
placeholder, `native_decide`, option, import or version change. No rename or structural
action queued. Broader coefficient API proposal remains deferred; existing header warning
requires ownership/license information and remains deferred rather than inventing attribution.

## Phase 4 checklist

- [x] Step 1: inherited workflow/reference review and target context.
- [x] Step 2: all 24 target-specific audit dispositions.
- [x] Step 2.5: all five search methods; unavailable service distinguished from absence.
- [x] Step 2.6: every parameter, inversion and public/local literature considered.
- [x] Step 2.7: complete signature width table.
- [x] Step 2.8: complete inequality scan.
- [x] Step 3: all 42 golfing rules considered; terminal simp replacement tested.
- [x] Step 4: strategy reconsidered and proof independently compiled.
- [x] Step 5a: module build and fresh complete diagnostics passed.
- [x] Step 5b: protection, naming, structure, packing and scoped-diff gates passed.
- [x] Step 6a: no rename/structural queue entry; existing generalisation deferral documented.

Parent owns dependent validation, shared progress logs, commit/push and file-wide phases.
