# Cleanup audit: `MvPolynomial.hasseDeriv_map`

Date: 2026-10-15 (America/Chicago). Baseline: pushed checkpoint `733ed99`.
Target: `Roth/HasseDeriv.lean:128`. Reviewed and retained without source changes.
The existing proof compares coefficients and simplifies the coefficient formula,
using the ring homomorphism's preservation of natural casts and multiplication.

## Workflow and all 24 audit items

Dedicated Phase 4 worker following the inherited mathlib-quality/lean4 workflow
and substantive reference review. Parent supplied native remote search results;
the direct MCP bridge supplied local search and fresh whole-file diagnostics.
The optional ask_chatgpt_math tool was skipped as authorized.

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Module build and complete diagnostics pass; existing header warning only. |
| 2 | HAVE SCAN | No have bindings. |
| 3 | SET_OPTION | No options present or added. |
| 4 | SIMP SQUEEZE | Terminal simp is appropriate; removing coeff_map was tested and fails. |
| 5 | NAMING | Matches Polynomial.hasseDeriv_map and LaurentSeries.hasseDeriv_map. |
| 6 | LINE PACKING | Signature lengths 78/82; next binder would make first line 101. |
| 7 | BY PLACEMENT | by already at end of signature. |
| 8 | FORMAT | Correct continuation/proof indentation; no whitespace issue. |
| 9 | COMMENTS | No proof comments; source citation preserved. |
| 10 | DOCSTRING | Accurately describes change of coefficients and project applications. |
| 11 | VISIBILITY | Public interface used in MainLemma, Separation and Theta. |
| 12 | STRUCTURE | Two short tactics; no helper extraction needed. |
| 13 | MATHLIB | Five search methods covered, two Hasse analogues inspected. |
| 14 | JUNK DEF | Theorem; no definitions introduced. |
| 15 | EXISTS LEMMA | No existential quantifier. |
| 16 | SHOW vs CHANGE | Neither present. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All parameters/context reviewed below. |
| 19 | INEQUALITY | No inequalities in statement or proof. |
| 20 | NORMAL-FORM | Pushes derivative through coefficient map, matching library orientation. |
| 21 | SYNTAX-GEN | No custom syntax or disguised predicate. |
| 22 | IMPORT-FANOUT | No import change needed. |
| 23 | CASTS | simp uses the ring homomorphism's natural-cast compatibility. |
| 24 | INSTANCE-NAME | Not an instance declaration. |

## Signature width and inequality tables

Measured Unicode codepoint lengths using Python len.

| Signature line | Before | After | Next unit | Arithmetic/action |
|---|---:|---:|---|---|
| 128: name, S, instance, f and d | 78 | 78 | (P : MvPolynomial σ R), 22 characters | 78 + 1 + 22 = 101 > 100; ok. |
| 129: P, conclusion and := by | 82 | 82 | No remaining signature unit | Complete signature; ok. |

Proof lines have lengths 7 and 36. Retain separate tactic lines for ext and simp;
line packing does not require putting tactics onto the signature line.

| Scope | Relation | Assessment |
|---|---|---|
| Statement | Equality of derivative-after-map and map-after-derivative | Conventional naturality orientation, matching univariate library. |
| Proof | Equality of coefficients after ext | No inequalities, bounds, negated orders or strictness choices. |

## Five-method mathlib search

| Method | Query/scope | Observed result |
|---|---|---|
| A Lean-Finder | Hasse derivative commutes with polynomial coefficient ring homomorphism map, limit 3 | Ordinary derivative analogues derivative_map, derivativeFinsupp_map and iterate_derivative_map; these are not Hasse derivative replacements. |
| B Loogle | "hasseDeriv_map", limit 5 | Polynomial.hasseDeriv_map and LaurentSeries.hasseDeriv_map. |
| C LeanSearch | Hasse derivative commutes with mapping polynomial coefficients along ring homomorphism, limit 3 | HTTP 500; unavailable, not evidence of absence. |
| D Pinned source/project | hasseDeriv_map, map_hasseDeriv, coeff_map | Univariate theorem, Laurent-series theorem and coefficient-map API inspected; project callers in MainLemma, Separation and Theta. |
| E Local MCP | hasseDeriv_map, limit 15 | Both library analogues and project target; source matching works, index unavailable. |

Evidence: `/private/tmp/roth-hasseDeriv_map-native-search.json` and
`/private/tmp/roth-hasseDeriv_map-local.json`.
Pinned `Mathlib/Algebra/Polynomial/HasseDeriv.lean:128` proves the univariate
version over semirings by extensionality and its coefficient formula.
`Mathlib/RingTheory/LaurentSeries.lean:171` proves compatibility of a
natural-order Hasse derivative with a linear coefficient map on Laurent series.
Neither has the multivariate polynomial type and finitely supported multi-index
of this target. The ordinary derivative results do not recover positive-
characteristic higher Hasse derivatives by division by factorials.
`Mathlib/Algebra/MvPolynomial/Eval.lean:384` supplies coeff_map; it is not a
default simp rule here, as the isolated removal experiment confirms.

Replacement checklist: definitions and computational interface inspected;
equivalent naturality formulations and related representations considered;
all five methods covered with service failure disclosed; no predicate alias,
topology or separation hypotheses. A useful, actually called public API remains.
No directly applicable replacement was found in bounded search; exhaustive
absence is not claimed.

## Parameters, generalisation, inversion and literature

| Parameter/context | Assessment |
|---|---|
| `{σ : Type u}` | Arbitrary variable type; no finiteness or nonemptiness restriction. |
| `{R : Type v}` / `[CommSemiring R]` | Matches source polynomial and derivative construction, all characteristics allowed. |
| `{S : Type w}` / `[CommSemiring S]` | Independent target universe; matches target construction. |
| `(f : R →+* S)` | Arbitrary ring homomorphism; no injectivity, surjectivity or algebra structure required. |
| `(d : σ →₀ ℕ)` | Arbitrary finitely supported order, including zero. |
| `(P : MvPolynomial σ R)` | Arbitrary polynomial; no degree/support restriction. |

The proof fundamentally uses only preservation of finite additive combinations
and natural scalar multiplication. A separate coefficient-map API for additive
homomorphisms could express this greater naturality, as illustrated by the
Laurent-series linear-map counterpart. It would require a different map operation
and public statement, so it is recorded as an optional deferred API proposal;
no substantive change is applied and it does not block routine cleanup.
Weakening the commutative-semiring requirements of the existing hasseDeriv
construction likewise requires definition/API work beyond this cleanup.
Inversion review: coefficient extensionality reduces naturality to the existing
general coeff_map and coefficient-of-derivative lemmas plus homomorphism laws.
Those ingredients already expose the reusable mathematical content; introducing
a helper for this two-tactic composition would add no useful abstraction.

Freshly inspected local `clean.tex` §1, lines 119–155, defines the monomial
operator using natural binomial coefficients and explicitly requests coefficient
map compatibility before passage between ℤ, ℚ and ℝ. The current theorem is
already more general than those named coefficient rings.
Public-literature evidence is reused from the preceding declaration audits:
§2.1, Definition 2, p.6 of
[Dvir–Kopparty–Saraf–Sudan, Extensions to the Method of Multiplicities](https://eccc.weizmann.ac.il/report/2009/004/download/)
defines Hasse derivatives by coefficients in P(X + Z). Inference: applying a
coefficient ring homomorphism commutes with that polynomial expansion and its
coefficient extraction. The paper's definition supports the mathematical
interpretation; it is not claimed to state the exact Lean semiring theorem.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | No exact wrapper. |
| 1.2 by rfl | Not a definitional equality; no rfl wrapper. |
| 1.3 rw + exact | Neither present. |
| 1.4 simp + exact | No trailing exact. |
| 1.5 trailing rfl | None. |
| 1.6 constructor chain | None. |
| 1.7 apply + exact | None. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | No lambda. |
| 1.10 single-use have | None. |
| 1.11 apply + intro | ext supplies the coefficient index directly. |
| 1.12 redundant show | None. |
| 1.13 have projections | None. |
| 1.14 merge rw | No rw. |
| 1.15 terminal simp only | Terminal unrestricted simp already used. |
| 1.16 nonterminal simp | None. |
| 1.17 dot notation | No explicit term application benefits. |
| 1.18 `<\|` | No nested application parentheses to remove. |
| 1.19 push Not | No negations. |
| 1.20 trivial existential | None. |
| 2.1 grind | Coefficient extensionality and targeted simp solve deterministically; no search needed. |
| 2.2 delete before grind | No grind. |
| 2.3 simpa consolidation | Tested removing coeff_map; fails with unsolved coefficient-map equality. |
| 2.4 fun_prop | No analytic function-property goal. |
| 2.5 positivity | No positivity goal. |
| 2.6 gcongr | Naturality equality, not monotonicity. |
| 2.7 lia/omega | No arithmetic inequality goal. |
| 2.8 aesop | Explicit coefficient argument already short and reliable. |
| 2.9 norm_num/norm_cast | simp already uses homomorphism cast and multiplication laws. |
| 2.10 decide/kernel | Symbolic arbitrary types and coefficients. |
| 2.11 field_simp/ring | No denominators; required step is homomorphism compatibility, not ring normalization. |
| 2.12 linear_combination | No equations to combine. |
| 2.13 wlog | No cases or symmetry reduction. |
| 2.14 calc | Two short steps; additional calculation scaffolding adds no clarity. |
| 2.15 `<;>` | ext generates one coefficient goal; no branch-wide sequence needed. |
| 3.1 erw/rw | Neither present. |
| 3.2 fun_prop | No legacy analytic tactic. |
| 3.3 omega/lia | Neither present. |
| 3.4 rcases rfl | No destructuring. |
| 3.5 automation attributes | Preserve current attributes; global simp-policy expansion is unnecessary for existing explicit users. |
| 3.6 simp_all | No local hypotheses requiring saturation. |
| 3.7 maxHeartbeats | No override present or added. |

Strategy reflection: retained the coefficient proof used by the corresponding
library theorem. A single bounded isolation experiment copied only the source
prefix preceding this declaration and the candidate declaration, excluding all
later project results. Removing coeff_map from simp left the map coefficients
unresolved (compiler exit 1). Lean's error recovery printed sorryAx for that
failed experiment; it was never applied to source and is not a valid proof.
The exact original proof compiled independently with exit 0. No further tactic
search was warranted after confirming the necessity of the explicit rule.
Evidence: `/private/tmp/roth-hasseDeriv_map-probe.log` and
`/private/tmp/roth-hasseDeriv_map-original.log`.

## Validation gates

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: lake build Roth.HasseDeriv, exit 0, 1430 jobs; /private/tmp/roth-hasseDeriv_map-module-build.log. |
| fresh LSP | PASS: bridge exit 0; success=true, partial=false, timed_out=false, failed_dependencies=[]; no errors, existing header warning only. /private/tmp/roth-hasseDeriv_map-postedit-diagnostics.json. |
| proof/type/axioms | PASS: isolated original proof compiles, exit 0; #check confirms original full type; axioms exactly propext, Classical.choice, Quot.sound. |
| definition_protected | PASS: no source edits. |
| theorem_statement_protected | PASS: source byte-identical. |
| structure_gate | PASS: two short proof steps. |
| naming_gate | PASS: matches both library Hasse-map analogue names. |
| line_packing_gate | PASS: 78/82-character signature; next binder would make 101. |
| inequality_orientation_gate | PASS: no inequalities. |
| scoped diff | PASS: no source diff; git diff --check exit 0. |
| dependent closure | PASS: parent reports full lake build exit 0, 2586 jobs, /private/tmp/roth-hasseDeriv_map-build.log; separate lake build Roth.LeanEval exit 0, 2585 jobs, /private/tmp/roth-hasseDeriv_map-leaneval.log. |

Existing header warning remains deferred pending ownership/license information.
No sorry, new axiom, native_decide, options, imports, versions, names, structure
or source changed.

## Phase 4 checklist

- [x] Step 1: inherited workflow/references and target context reviewed.
- [x] Step 2: all 24 target audit dispositions.
- [x] Step 2.5: five search methods with service failure disclosed.
- [x] Step 2.6: all parameters, inversion and local/public literature reviewed.
- [x] Step 2.7: complete signature-width table.
- [x] Step 2.8: complete inequality scan.
- [x] Step 3: all 42 golfing rules considered.
- [x] Step 4: strategy reassessed using isolated proof experiment.
- [x] Step 5a: module build and complete fresh diagnostics passed.
- [x] Step 5b: protection, structure, naming, packing and scoped-diff gates passed.
- [x] Step 6a: optional broader coefficient-map API deferred; no rename/structure queue.

Parent owns dependent validation, shared progress logs, commit/push and file-wide phases.
