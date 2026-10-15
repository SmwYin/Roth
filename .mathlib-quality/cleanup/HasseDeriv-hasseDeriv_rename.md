# Cleanup audit: `MvPolynomial.hasseDeriv_rename`

Date: 2026-10-15 (America/Chicago). Baseline: pushed checkpoint `4a32dea`.
Target: `Roth/HasseDeriv.lean:137`. Inlined the single-use binomial-factor
transport proof into the monomial simplification. The proof shrinks from eight
lines to six, keeping the same monomial/addition induction and mathematical
statement, docstring, citation, visibility, name and attributes.

## Workflow and all 24 audit items

Dedicated Phase 4 worker following the inherited mathlib-quality/lean4 workflow
and substantive reference review. Parent supplied native remote search results;
the direct MCP bridge supplied local search and fresh complete diagnostics.
The optional ask_chatgpt_math tool was skipped as authorized.

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Module build and complete diagnostics pass; existing header warning only. |
| 2 | HAVE SCAN | Inlined the one-use hc proof using the same product/transport rules. |
| 3 | SET_OPTION | No options present or added. |
| 4 | SIMP SQUEEZE | Two terminal simp calls; monomial call now handles transport directly. |
| 5 | NAMING | Matches library pderiv_rename naturality naming. |
| 6 | LINE PACKING | All three signature lines checked below; neither continuation fits preceding line. |
| 7 | BY PLACEMENT | by already at end of conclusion. |
| 8 | FORMAT | Standard induction alternatives and four/six-space continuation. |
| 9 | COMMENTS | No proof comments removed or added. |
| 10 | DOCSTRING | Accurate injective transport explanation and citation preserved. |
| 11 | VISIBILITY | Public theorem used by Separation.hasseDeriv_rename_mul_aeval. |
| 12 | STRUCTURE | Six-line proof; no helper extraction needed. |
| 13 | MATHLIB | Five methods covered; pinned related results inspected. |
| 14 | JUNK DEF | No definitions introduced. |
| 15 | EXISTS LEMMA | No existential quantifier. |
| 16 | SHOW vs CHANGE | Neither present. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All parameters/context reviewed below; injectivity essential in general. |
| 19 | INEQUALITY | No inequalities; truncated subtraction transport is already a library lemma. |
| 20 | NORMAL-FORM | Derivative through rename matches pderiv_rename orientation. |
| 21 | SYNTAX-GEN | No custom syntax or disguised predicate. |
| 22 | IMPORT-FANOUT | Existing imports supply every rule; no changes. |
| 23 | CASTS | Natural binomial-factor casts handled by existing simp rules. |
| 24 | INSTANCE-NAME | Not an instance. |

## Signature width and inequality tables

Measured Unicode codepoint lengths using Python len; signature byte-identical.

| Signature line | Before | After | Next unit | Arithmetic/action |
|---|---:|---:|---|---|
| 137: name, τ, f, hf and d | 90 | 90 | (P : MvPolynomial σ R), 22 characters | 90 + 1 + 22 = 113 > 100; ok. |
| 138: P and colon | 28 | 28 | Complete conclusion including := by, 73 characters | 28 + 1 + 73 = 102 > 100; ok. |
| 139: complete conclusion and := by | 77 | 77 | None | Complete signature; ok. |

| Scope | Relation | Assessment |
|---|---|---|
| Statement | Equality between derivative of renamed P and renamed derivative | Conventional naturality orientation. |
| Proof | Product and monomial equalities under injective mapDomain | No inequality, strictness, bound or negated-order choice. |
| Truncated subtraction | mapDomain transports k - d | Existing mapDomain_tsub used in reverse to normalize exponent; no hypothesis changed. |

## Five-method mathlib search

| Method | Query/scope | Observed result |
|---|---|---|
| A Lean-Finder | multivariate Hasse derivative commutes with injective variable renaming, limit 3 | MvPolynomial.pderiv_rename, coeff_rename_mapDomain, IsHomogeneous.rename_isHomogeneous_iff. |
| B Loogle | "hasseDeriv", "rename", limit 5 | Successful empty result. Initial two-string query without a comma was invalid; corrected query supplies the usable search result. |
| C LeanSearch | Hasse derivative multivariate polynomial injective renaming mapDomain, limit 3 | HTTP 500; unavailable, not evidence of absence. |
| D Pinned source/project | hasseDeriv_rename, product/mapDomain/subtraction transport and three returned candidates | Existing general transport rules already used; downstream Separation caller found. |
| E Local MCP | hasseDeriv_rename, limit 10 | Target and Separation.hasseDeriv_rename_mul_aeval; source matching works, index unavailable. |

Evidence: `/private/tmp/roth-hasseDeriv_rename-native-search.json`,
`/private/tmp/roth-hasseDeriv_rename-loogle-retry.json` and
`/private/tmp/roth-hasseDeriv_rename-local.json`.
Pinned source candidates were inspected:

- `Mathlib/Algebra/MvPolynomial/PDeriv.lean:143`: ordinary first partial
  derivative naturality, with the same injective-variable-map assumption.
  It does not replace arbitrary-order Hasse derivatives in all characteristics.
- `Mathlib/Algebra/MvPolynomial/Rename.lean:334`: coefficient preservation at
  transported exponents. A coefficient proof could use it but would additionally
  need treatment of exponents outside the image; the monomial proof is direct.
- `Mathlib/RingTheory/MvPolynomial/Homogeneous.lean:337`: homogeneity preservation
  and reflection under injective rename, not derivative naturality.
- `Mathlib/Data/Finsupp/Basic.lean:430`: prod_mapDomain_index_inj transports the
  finite product; mapDomain_apply_of_injective supplies individual entries.
- `Mathlib/Data/Finsupp/Order.lean:295`: mapDomain_tsub supplies exponent transport.
- `Mathlib/Algebra/MvPolynomial/Rename.lean:94`: rename_monomial is an explicit
  needed rule here, not supplied automatically by the default simp set.

Replacement checklist: definitions and computational interface inspected;
ordinary derivatives, coefficient formulas and domain embeddings considered;
five search methods covered with failures disclosed; no predicate alias,
topological or separation hypothesis. Existing library transport lemmas are
reused, while the useful called public API remains. Bounded search found no
same-type direct replacement; exhaustive absence is not claimed.

## Parameters, generalisation, inversion and literature

| Parameter/context | Assessment |
|---|---|
| `{σ : Type u}` | Arbitrary source variable type; no finiteness/nonemptiness constraint. |
| `{R : Type v}` / `[CommSemiring R]` | Matches existing polynomial/derivative construction, all characteristics allowed. |
| `{τ : Type w}` | Arbitrary independently universe-polymorphic target variable type. |
| `{f : σ → τ}` | Arbitrary variable map subject only to explicit injectivity. |
| `(hf : Function.Injective f)` | Ensures factors/exponents are transported without merging variables; necessary in general. |
| `(d : σ →₀ ℕ)` | Arbitrary finite-support order, including zero. |
| `(P : MvPolynomial σ R)` | Arbitrary polynomial, without degree/support restrictions. |

Dropping injectivity is mathematically invalid in general: over ℕ, collapse two
distinct variables x and y to one variable z, take P = y and differentiate in
order one in x. Before renaming the derivative is zero; after renaming P = z
and the transported order is one, so the derivative is one. A support-specific
injectivity variant would require a different theorem statement and supporting
transport API; it is optional deferred API work and was not applied. Weakening
the coefficient algebra assumptions requires changes to the underlying
construction and is outside routine cleanup. No stronger assumptions introduced.

Inversion review: the monomial case factors through two existing reusable
principles, product transport and truncated-subtraction transport. The local hc
merely combines those general APIs with the project definition of hasseCoeff;
inlining avoids an unnecessary one-use local abstraction. A separate public
hasseCoeff transport lemma could be useful if another caller appears, but no
such need was found and adding public API is unnecessary here.

Freshly inspected `.mathlib-quality/references/clean.tex` §4, lines 614–634:
Lemma 4-2 embeds polynomials into a larger variable ring; the following Lean
note explicitly requests variable-renaming invariance as a separate lemma.
The source docstring therefore remains accurate.
Public-literature evidence is reused from preceding declaration audits:
§2.1, Definition 2, p.6 of
[Dvir–Kopparty–Saraf–Sudan, Extensions to the Method of Multiplicities](https://eccc.weizmann.ac.il/report/2009/004/download/)
defines Hasse derivatives by coefficients in P(X + Z). Inference: injective
relabelling transports the monomials and corresponding coefficient indices
without identification. This supports the interpretation, not a claim that the
paper states this exact arbitrary-variable semiring theorem.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | No exact wrapper. |
| 1.2 by rfl | Naturality is not definitionally reflexive. |
| 1.3 rw + exact | Neither present. |
| 1.4 simp + exact | No trailing exact. |
| 1.5 trailing rfl | None. |
| 1.6 constructor chain | None. |
| 1.7 apply + exact | None. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | No lambda. |
| 1.10 single-use have | Applied: eliminated hc and integrated its rules into terminal simp. |
| 1.11 apply + intro | Induction already names case binders directly. |
| 1.12 redundant show | None. |
| 1.13 have projections | None. |
| 1.14 merge rw | No rw. |
| 1.15 terminal simp only | Both terminal simp calls unrestricted already. |
| 1.16 nonterminal simp | None. |
| 1.17 dot notation | Library function applications clear; no change helps. |
| 1.18 `<\|` | No nested term application to simplify. |
| 1.19 push Not | No negations. |
| 1.20 trivial existential | None. |
| 2.1 grind | Direct induction and targeted transport simp solve deterministically. |
| 2.2 delete before grind | No grind. |
| 2.3 simpa consolidation | Consolidated local transport proof and monomial simp into one simp. |
| 2.4 fun_prop | No analytic function property. |
| 2.5 positivity | No positivity goal. |
| 2.6 gcongr | Naturality equality, not monotonicity. |
| 2.7 lia/omega | No arithmetic side goal; existing transport lemma suffices. |
| 2.8 aesop | No search needed after short deterministic proof succeeds. |
| 2.9 norm_num/norm_cast | Existing simp rules handle natural casts. |
| 2.10 decide/kernel | Arbitrary symbolic types, maps and polynomials. |
| 2.11 field_simp/ring | No denominators or ring normalization goal. |
| 2.12 linear_combination | No equations to combine. |
| 2.13 wlog | No symmetry reduction. |
| 2.14 calc | Induction with two immediately solved cases; no useful calc chain. |
| 2.15 `<;>` | Different case arguments make explicit alternatives clearer. |
| 3.1 erw/rw | Neither present. |
| 3.2 fun_prop | No legacy analytic tactic. |
| 3.3 omega/lia | Neither present. |
| 3.4 rcases rfl | No destructuring. |
| 3.5 automation attributes | Existing attributes unchanged; no broad simp-policy expansion. |
| 3.6 simp_all | Add case uses exactly hp/hq; no saturation needed. |
| 3.7 maxHeartbeats | No override present or added. |

Strategy reflection: first isolated candidate mistakenly omitted the existing
explicit rename_monomial rule, leaving an unresolved monomial-renaming goal
(exit 1). Adding that rule compiled the desired inline proof (exit 0). Scratch
error recovery for the failed attempt reported sorryAx; that attempt was never
applied to source. The accepted isolated proof reports only propext,
Classical.choice and Quot.sound. The experiment copies only the source prefix
and candidate, excluding the target's original proof and all later project
results, preventing circular use of the theorem being cleaned.
Evidence: `/private/tmp/roth-hasseDeriv_rename-probe.log` (failed attempt) and
`/private/tmp/roth-hasseDeriv_rename-probe-final.log` (accepted proof).
No additional vague automation search was warranted after this direct success.

## Validation gates

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: lake build Roth.HasseDeriv, exit 0, 1430 jobs; /private/tmp/roth-hasseDeriv_rename-module-build.log. |
| fresh LSP | PASS: bridge exit 0; success=true, partial=false, timed_out=false, failed_dependencies=[]; no errors, existing header warning only. /private/tmp/roth-hasseDeriv_rename-postedit-diagnostics.json. |
| proof/type/axioms | PASS: isolated accepted proof compiles, exit 0; #check confirms original full type; axioms exactly propext, Classical.choice, Quot.sound. |
| definition_protected | PASS: no definitions changed. |
| theorem_statement_protected | PASS: exact signature equality and source prefix/suffix assertions passed. |
| structure_gate | PASS: six-line proof; single-use local proof removed. |
| naming_gate | PASS: analogous to pderiv_rename. |
| line_packing_gate | PASS: 90/28/77-character signature; neither next unit fits. |
| inequality_orientation_gate | PASS: no inequalities. |
| scoped diff | PASS: only target proof changed; git diff --check exit 0. |
| dependent closure | PASS: orchestrator full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs), both exit 0. Logs `/private/tmp/roth-hasseDeriv_rename-build.log` and `/private/tmp/roth-hasseDeriv_rename-leaneval.log`. |

The bridge emitted an asynchronous subprocess cleanup warning after returning
complete successful diagnostics; its process exited 0. The complete result is
recorded rather than treating the shutdown warning as an elaboration failure.
Existing header warning remains deferred pending ownership/license information.
No sorry, new axiom, native_decide, option, import, version, name, mathematical
statement or project structure changed.

## Phase 4 checklist

- [x] Step 1: inherited workflow/references and target context reviewed.
- [x] Step 2: all 24 target audit dispositions.
- [x] Step 2.5: five search methods with syntax correction/service failure disclosed.
- [x] Step 2.6: all parameters, inversion and local/public literature reviewed.
- [x] Step 2.7: complete signature-width table.
- [x] Step 2.8: complete inequality scan.
- [x] Step 3: all 42 golfing rules considered.
- [x] Step 4: strategy reassessed using isolated proof experiments.
- [x] Step 5a: module build and complete fresh diagnostics passed.
- [x] Step 5b: protection, structure, naming, packing and scoped-diff gates passed.
- [x] Step 6a: optional support-specific API deferred; no rename/structure queue.

Parent owns dependent validation, shared progress logs, commit/push and file-wide phases.
