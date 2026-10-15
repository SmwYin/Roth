# Cleanup audit: `MvPolynomial.hasseDeriv_C`

Date: 2026-10-15 (America/Chicago). Baseline: pushed checkpoint `667acf6`.
Target: `Roth/HasseDeriv.lean:120`. Reviewed and retained without source changes.
The existing proof rewrites a constant as a monomial, applies the derivative
formula and vanishing criterion, and simplifies the resulting zero coefficient.
A tested one-line alternative needs an explicit simp-rule exclusion; retaining
the clear two-step proof avoids that extra maintenance burden.

## Workflow and all 24 audit items

Dedicated Phase 4 worker following the inherited mathlib-quality/lean4 workflow
and substantive reference review. Parent supplied native remote search results;
this worker used the direct MCP bridge for local search and fresh diagnostics.
The optional ask_chatgpt_math tool was skipped as authorized.

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Module build and complete fresh diagnostics pass; existing header warning only. |
| 2 | HAVE SCAN | No have bindings. |
| 3 | SET_OPTION | No options present or added. |
| 4 | SIMP SQUEEZE | Original terminal simp is appropriate; consolidation experiments below. |
| 5 | NAMING | hasseDeriv_C matches the univariate library counterpart. |
| 6 | LINE PACKING | Complete signature is 85 characters; next proof unit cannot fit. |
| 7 | BY PLACEMENT | by already on the signature line. |
| 8 | FORMAT | Two-space proof indentation; no whitespace defect. |
| 9 | COMMENTS | No proof comments to revise; source citation preserved. |
| 10 | DOCSTRING | Correctly states vanishing for nonzero order. |
| 11 | VISIBILITY | Public standard computational interface, despite no explicit project callers. |
| 12 | STRUCTURE | Two short tactics; no extraction needed. |
| 13 | MATHLIB | Five search methods covered; pinned library analogue inspected. |
| 14 | JUNK DEF | Theorem; no new definitions. |
| 15 | EXISTS LEMMA | No existential statement. |
| 16 | SHOW vs CHANGE | Neither present. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every parameter and hypothesis considered below. |
| 19 | INEQUALITY | d ≠ 0 and auxiliary ¬d ≤ 0 have correct orientations. |
| 20 | NORMAL-FORM | Derivative of a constant normalizes to zero. |
| 21 | SYNTAX-GEN | No custom syntax or disguised predicate. |
| 22 | IMPORT-FANOUT | No import changes needed. |
| 23 | CASTS | Existing simp handles the natural zero cast; no cast machinery added. |
| 24 | INSTANCE-NAME | Not an instance declaration. |

## Signature width and inequality tables

Measured Unicode codepoint lengths with Python len.

| Signature line | Before | After | Next unit | Arithmetic/action |
|---|---:|---:|---|---|
| 120: entire signature and := by | 85 | 85 | First rw tactic, 85 characters without indentation | 85 + 1 + 85 = 171 > 100; retain separate proof line; ok. |

The proof lines measure 87 and 6 characters including indentation. No signature
continuation lines, split binders, blank proof lines or overlong lines occur.

| Scope | Relation | Assessment |
|---|---|---|
| Statement | hd : d ≠ 0 | Conventional nonzero hypothesis, not an ordered inequality. |
| Statement | hasseDeriv d (C a) = 0 | Canonical vanishing conclusion. |
| Auxiliary proof | ¬d ≤ 0 | Required by hasseCoeff_eq_zero_iff; simpa converts hd using the bottom element of natural-valued Finsupp. |

No strict-order reversal, conditional inequality or numerical bound is present.

## Five-method mathlib search

| Method | Query/scope | Observed result |
|---|---|---|
| A Lean-Finder | nonzero Hasse derivative of constant polynomial is zero, limit 3 | Polynomial.hasseDeriv_C, Polynomial.hasseDeriv_zero', Polynomial.hasseDeriv_apply_one. |
| B Loogle | "hasseDeriv_C", limit 5 | Polynomial.hasseDeriv_C and coefficient/composition results. |
| C LeanSearch | Hasse derivative of constant polynomial vanishes at nonzero order, limit 3 | HTTP 500; unavailable, not evidence of absence. |
| D Pinned source/project | hasseDeriv_C and constant/monomial formulas | Library analogue at Mathlib/Algebra/Polynomial/HasseDeriv.lean:116; no explicit project calls beyond target declaration. |
| E Local MCP | hasseDeriv_C, limit 15 | Library univariate theorem and project target; source matching works, index unavailable. |

Remote evidence: `/private/tmp/roth-hasseDeriv_C-native-search.json`.
Local evidence: `/private/tmp/roth-hasseDeriv_C-local.json`.
The pinned univariate theorem has `[Semiring R]`, natural-number order k and
hypothesis `0 < k`. Its proof rewrites the constant to a zero-degree monomial,
applies the monomial formula and vanishing binomial coefficient, then simplifies.
The project theorem follows that same argument for an arbitrary finitely
supported multi-index. The library theorem is not a direct replacement for the
multivariate type; changing representation would add unnecessary machinery.
The apply_one theorem is a specialization, not a generalization.

Replacement checklist: original definitions and upstream lemmas inspected;
related equivalent univariate formulations considered; five search methods
covered with the service failure disclosed; no predicate alias, topology or
separation condition. No direct project call does not justify deleting this
standard public interface. No directly applicable library replacement was found
in bounded search; exhaustive absence is not claimed.

## Parameters, generalisation, inversion and literature

| Parameter/context | Assessment |
|---|---|
| `{σ : Type u}` | Arbitrary variable set, already including infinite and empty types. |
| `{R : Type v}` | Arbitrary coefficient universe and characteristic. |
| `[CommSemiring R]` | Matches the existing multivariate polynomial and derivative construction; changing that construction would be a definition/API change. |
| `{d : σ →₀ ℕ}` | Arbitrary finite-support multi-index; no degree or support-size restriction. |
| `hd : d ≠ 0` | Necessary uniformly: at d = 0, the derivative of C 1 over ℕ equals C 1, not zero. |
| `(a : R)` | Arbitrary coefficient, including zero; no nonzero or characteristic hypothesis. |

The stronger API of vanishing for monomials whose exponents fail to dominate d
already follows by composing hasseDeriv_monomial with hasseCoeff_eq_zero_iff,
exactly what this proof does at exponent zero. A separate general vanishing
lemma could shorten other proofs if repeated usage emerges; adding a new public
theorem or generalizing this statement is deferred as unnecessary API expansion.
No such change is applied or blocks routine cleanup. Inversion review: the
argument uses a general binomial vanishing criterion already factored into a
project theorem, followed by the general library monomial-zero normalization.
No unused assumption or hidden finiteness hypothesis was found.

Freshly inspected local `clean.tex` §1 defines the monomial action as zero
whenever any derivative index exceeds the corresponding exponent, and extends
linearly. Constants have all exponents zero, so nonzero d implies the stated
vanishing. Public-literature evidence is reused from the adjacent zero-order
reviews: §2.1, Definition 2, p.6 of
[Dvir–Kopparty–Saraf–Sudan, Extensions to the Method of Multiplicities](https://eccc.weizmann.ac.il/report/2009/004/download/)
defines Hasse derivatives as coefficients in the expansion of P(X + Z).
Inference from that definition: a constant polynomial has no nonconstant
Z-coefficient. This is not a claim that the paper states the exact Lean
commutative-semiring formulation.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | No exact wrapper. |
| 1.2 by rfl | No rfl wrapper. |
| 1.3 rw + exact | No terminal exact. |
| 1.4 simp + exact | None. |
| 1.5 trailing rfl | None. |
| 1.6 constructor chain | None. |
| 1.7 apply + exact | None. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | No lambda. |
| 1.10 single-use have | None; the needed coefficient fact is already inline. |
| 1.11 apply + intro | None. |
| 1.12 redundant show | None. |
| 1.13 have projections | .2 selects the required implication directly; no have. |
| 1.14 merge rw | Rewrites already in one call. |
| 1.15 terminal simp only | Existing terminal simp is unrestricted and closes zero normalization. |
| 1.16 nonterminal simp | Nested simpa discharges a separate auxiliary goal; no nonterminal simplification. |
| 1.17 dot notation | Existing .2 implication application is concise. |
| 1.18 `<\|` | Parentheses isolate the fact and auxiliary proof within a rewrite list. |
| 1.19 push Not | Nonzero hypothesis directly converted by simpa. |
| 1.20 trivial existential | None. |
| 2.1 grind | Known exact rewrite facts suffice; no general automation needed. |
| 2.2 delete before grind | No grind. |
| 2.3 simpa consolidation | Tested simp consolidation; natural version loops, exclusion version works but is less maintainable. |
| 2.4 fun_prop | No function-property goal. |
| 2.5 positivity | No positivity goal. |
| 2.6 gcongr | Vanishing equality, not monotonicity. |
| 2.7 lia/omega | Auxiliary Finsupp order fact is solved by simpa, no arithmetic tactic needed. |
| 2.8 aesop | Explicit two-step proof avoids search. |
| 2.9 norm_num/norm_cast | simp already handles zero cast and multiplication. |
| 2.10 decide/kernel | Symbolic parameters, not a closed decidable instance. |
| 2.11 field_simp/ring | No denominators or ring-normalization problem. |
| 2.12 linear_combination | No equations to combine. |
| 2.13 wlog | No case split. |
| 2.14 calc | Two computational steps; calc adds structure without clarity. |
| 2.15 `<;>` | No branches. |
| 3.1 erw/rw | Existing rw suffices. |
| 3.2 fun_prop | No legacy analytic tactic. |
| 3.3 omega/lia | Neither present. |
| 3.4 rcases rfl | No destructuring. |
| 3.5 automation attributes | Existing attribute policy retained, matching univariate constant theorem. |
| 3.6 simp_all | No collection of hypotheses needing saturation. |
| 3.7 maxHeartbeats | No override present or added. |

Strategy reflection and measured experiments: an isolated temporary file copied
only the source prefix preceding this target, so neither the target nor later
project theorems could solve its own goal. The candidate
`simp [C_apply, (hasseCoeff_eq_zero_iff d 0).2 (by simpa using hd)]`
failed (compiler exit 1), warning of a loop between C_apply and monomial_zero'
and reaching the existing recursion limit. The failed diagnostic reported
sorryAx from Lean's error recovery; this experiment was never applied to source
and is not a valid proof. A second candidate added `-monomial_zero'`; compiler
exit 0, no warnings, with axioms `[propext, Classical.choice, Quot.sound]`.
The explicit simp exclusion saves one line but obscures the straightforward
rewriting argument, so both worker and parent chose to retain the original.
No option was increased and no further automation was necessary.
Logs: `/private/tmp/roth-hasseDeriv_C-probe.log` (failed natural candidate) and
`/private/tmp/roth-hasseDeriv_C-probe2.log` (successful exclusion candidate).

## Validation gates

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: lake build Roth.HasseDeriv, exit 0, 1430 jobs; /private/tmp/roth-hasseDeriv_C-module-build.log. |
| fresh LSP | PASS: bridge exit 0; success=true, partial=false, timed_out=false, failed_dependencies=[]; no errors, only existing header warning. /private/tmp/roth-hasseDeriv_C-postedit-diagnostics.json. |
| definition_protected | PASS: no source edits. |
| theorem_statement_protected | PASS: source byte-identical. |
| structure_gate | PASS: two short proof steps, no extraction needed. |
| naming_gate | PASS: name matches the library counterpart. |
| line_packing_gate | PASS: complete 85-character signature; next unit would make 171. |
| inequality_orientation_gate | PASS: auxiliary negated comparison is required by the existing criterion. |
| scoped diff | PASS: source diff empty; git diff --check exit 0. |
| dependent closure | PASS: parent reports full lake build exit 0, 2586 jobs, /private/tmp/roth-hasseDeriv_C-build.log; separate lake build Roth.LeanEval exit 0, 2585 jobs, /private/tmp/roth-hasseDeriv_C-leaneval.log. |

The exact original target, copied together with its preceding source into an
isolated temporary file, compiled with exit 0. Its #check output confirms the
unchanged arbitrary σ/R/CommSemiring parameters, nonzero hypothesis and conclusion;
#print axioms reports exactly `[propext, Classical.choice, Quot.sound]`.
Evidence: `/private/tmp/roth-hasseDeriv_C-original.log`. The LSP bridge emitted a
subprocess teardown warning after returning a complete successful result; its
exit status remained zero and the diagnostics were complete.

Existing header warning remains deferred pending ownership/license information.
No sorry, new axiom, native_decide, option, import, version, rename, structure or
source edit was introduced.

## Phase 4 checklist

- [x] Step 1: inherited workflow/references and target context reviewed.
- [x] Step 2: all 24 target audit dispositions.
- [x] Step 2.5: five search methods with service failure disclosed.
- [x] Step 2.6: all parameters, inversion and local/public literature reviewed.
- [x] Step 2.7: complete signature-width table.
- [x] Step 2.8: complete inequality scan.
- [x] Step 3: all 42 golfing rules considered.
- [x] Step 4: strategy reassessed using isolated proof experiments.
- [x] Step 5a: module build and complete fresh diagnostics passed.
- [x] Step 5b: protection, structure, naming, packing and scoped-diff gates passed.
- [x] Step 6a: optional broader API proposal deferred; no rename/structure queue.

Parent owns dependent validation, shared progress logs, commit/push and file-wide phases.
