# Cleanup audit: `MvPolynomial.hasseDeriv_zero`

Date: 2026-10-15 (America/Chicago). Baseline: pushed checkpoint `f9f649f`.
Target: `Roth/HasseDeriv.lean:114`. Reviewed and retained without source changes.
The existing one-term proof packages the preceding pointwise identity using
`LinearMap.ext`, exactly the approach used by mathlib's univariate counterpart.

## Workflow and all 24 audit items

Dedicated Phase 4 worker following the inherited mathlib-quality/lean4 workflow
and substantive reference review. The native Lean tool namespace is absent from
this leaf registry. The direct MCP bridge supplies local search and fresh
verification; the immediately preceding zero-order review supplies relevant
remote-search and public-literature evidence, explicitly reused below.

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Module build and fresh complete diagnostics pass; existing header warning only. |
| 2 | HAVE SCAN | No have bindings. |
| 3 | SET_OPTION | No options present or added. |
| 4 | SIMP SQUEEZE | No simp invocation; exact extensionality term is already minimal. |
| 5 | NAMING | hasseDeriv_zero follows mathlib's bundled-identity name. |
| 6 | LINE PACKING | Complete signature is 96 characters; body cannot be appended within 100. |
| 7 | BY PLACEMENT | Direct term proof; no by needed. |
| 8 | FORMAT | Two-space body indentation; no whitespace defect. |
| 9 | COMMENTS | No proof comments; source citation preserved. |
| 10 | DOCSTRING | Correctly explains zero binomial indices and identity. |
| 11 | VISIBILITY | Useful public simp identity, even without explicit named downstream calls. |
| 12 | STRUCTURE | One proof term; no extraction. |
| 13 | MATHLIB | Five search methods covered; library analogues inspected. |
| 14 | JUNK DEF | Theorem, no definition introduced. |
| 15 | EXISTS LEMMA | No existential statement. |
| 16 | SHOW vs CHANGE | Neither present. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All parameters and inversion reviewed below; no API change. |
| 19 | INEQUALITY | No inequalities in statement or proof. |
| 20 | NORMAL-FORM | Bundled zero-order derivative simplifies to identity linear map. |
| 21 | SYNTAX-GEN | No custom syntax or disguised predicate. |
| 22 | IMPORT-FANOUT | No imports changed or needed. |
| 23 | CASTS | No coercion casts; two existing type annotations select variable and coefficient types. |
| 24 | INSTANCE-NAME | Not an instance declaration. |

## Signature width and inequality tables

Measured Unicode codepoint lengths with Python len.

| Signature line | Before | After | Next unit | Arithmetic/action |
|---|---:|---:|---|---|
| 114: full theorem, conclusion and := | 96 | 96 | LinearMap.ext hasseDeriv_zero_apply (35 characters) | 96 + 1 + 35 = 132 > 100; retain separate body; ok. |

The indented proof body is 37 characters. There are no signature continuation
lines, split binders, blank lines inside the declaration or overlong lines.

| Scope | Inequalities | Action |
|---|---|---|
| Statement | None; equality of linear maps | No orientation change. |
| Proof | None; extensionality term | No orientation change. |

## Five-method mathlib search

| Method | Query/scope | Observed result |
|---|---|---|
| A Lean-Finder | zero order Hasse derivative is identity polynomial | Reused immediately preceding results: Polynomial.hasseDeriv_zero', Polynomial.hasseDeriv_zero, LaurentSeries.hasseDeriv_zero. |
| B Loogle | "hasseDeriv_zero", limit 5 | Reused immediately preceding query, directly matching this target's bundled identity; same three analogues. |
| C LeanSearch | Hasse derivative order zero equals original polynomial | Prior adjacent review received HTTP 500; unavailable, not evidence of absence. |
| D Pinned source/project | hasseDeriv_zero / LinearMap.ext hasseDeriv | Fresh source inspection of library analogues, target and project callers. |
| E Local MCP | hasseDeriv_zero, limit 20 | Fresh search found those analogues and both project zero-order declarations; index unavailable, source matching works. |

Remote evidence: `/private/tmp/roth-hasseDeriv_zero_apply-native-search.json`.
Fresh local evidence: `/private/tmp/roth-hasseDeriv_zero-local.json`.
Pinned `Mathlib/Algebra/Polynomial/HasseDeriv.lean:86` proves the bundled identity
using `LinearMap.ext` applied to its pointwise theorem. The Laurent-series
analogue at `Mathlib/RingTheory/LaurentSeries.lean:139` uses coefficient
extensionality and simp for a different representation. Neither has the
multivariate polynomial type required here. The target already composes mathlib
extensionality with the existing project pointwise theorem in one application.

Replacement checklist: project source and underlying library definitions
inspected; pointwise and bundled equivalents considered; five search methods
covered with the failed service disclosed; no predicate aliases, topology or
separation conditions. No direct named downstream call was found for the
bundled target, but its simp attribute provides normalization and parallels the
established library API. Removing it would discard useful behavior. Re-encoding
multivariate polynomials to apply an unrelated univariate theorem would add
representation machinery. Bounded search does not prove exhaustive absence.

## Parameters, generalisation, inversion and literature

| Parameter/context | Assessment |
|---|---|
| `{σ : Type u}` | Arbitrary variables, including empty and infinite types. |
| `{R : Type v}` | Arbitrary universe and characteristic. |
| `[CommSemiring R]` | Used by the existing multivariate polynomial and derivative construction; weakening the representation would be a definition/API change. |

No explicit propositional hypothesis or polynomial argument remains: equality
of bundled linear maps already quantifies over every polynomial. The preceding
pointwise theorem supplies the equivalent applied formulation. No parameter is
unused, and no finite-variable, field, nontriviality or nonemptiness assumption
needs removal. Inversion review identifies the universal principle: linear
maps equal on every argument are equal. `LinearMap.ext` is precisely the general
mathlib theorem for that principle, and the target already uses it directly.
No additional abstraction, generalization or approval-dependent change is proposed.

Fresh inspection of local `clean.tex` §1 confirms linear extension of the
binomial-coefficient action; zero order fixes each monomial and therefore the
entire linear map. Public-literature inspection is reused from the adjacent
zero-order pointwise review: §2.1, Definition 2, p.6 of
[Dvir–Kopparty–Saraf–Sudan, Extensions to the Method of Multiplicities](https://eccc.weizmann.ac.il/report/2009/004/download/)
defines Hasse derivatives as coefficients in the expansion of P(X + Z).
Inference from that definition: the constant coefficient in Z equals P(X),
and extensionality yields this bundled identity. No claim is made that the paper
states this exact Lean commutative-semiring formulation. Optional
ask_chatgpt_math skipped as authorized.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | Already a direct term; no wrapper. |
| 1.2 by rfl | No wrapper; equality follows by extensionality, not presumed definitional. |
| 1.3 rw + exact | None. |
| 1.4 simp + exact | None. |
| 1.5 trailing rfl | None. |
| 1.6 constructor chain | None. |
| 1.7 apply + exact | Already consolidated into one extensionality application. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | Pointwise theorem passed directly, with no lambda. |
| 1.10 single-use have | None. |
| 1.11 apply + intro | None. |
| 1.12 redundant show | None. |
| 1.13 have projections | None. |
| 1.14 merge rw | No rewrites. |
| 1.15 terminal simp only | No simp. |
| 1.16 nonterminal simp | No simp. |
| 1.17 dot notation | Existing LinearMap.ext application clearly names the principle. |
| 1.18 `<\|` | No nested application or parentheses to remove. |
| 1.19 push Not | No negation. |
| 1.20 trivial existential | None. |
| 2.1 grind | Deterministic single-term proof already sufficient; automation adds no benefit. |
| 2.2 delete before grind | No grind. |
| 2.3 simpa consolidation | No equality chain; direct application is already shorter. |
| 2.4 fun_prop | No function-property goal. |
| 2.5 positivity | No positivity goal. |
| 2.6 gcongr | Equality, not monotonicity. |
| 2.7 lia/omega | No arithmetic reasoning. |
| 2.8 aesop | Exact theorem application avoids search. |
| 2.9 norm_num/norm_cast | No numeric evaluation or coercion normalization. |
| 2.10 decide/kernel | Not a closed decidable instance. |
| 2.11 field_simp/ring | No denominators or ring-normalization goal. |
| 2.12 linear_combination | No equations to combine. |
| 2.13 wlog | No case split. |
| 2.14 calc | One equality established in one step. |
| 2.15 `<;>` | No tactic branches. |
| 3.1 erw/rw | Neither present. |
| 3.2 fun_prop | No legacy analytic tactic. |
| 3.3 omega/lia | Neither present. |
| 3.4 rcases rfl | No destructuring. |
| 3.5 automation attributes | Existing simp attribute gives canonical zero-order normalization, matching mathlib. |
| 3.6 simp_all | No hypotheses to simplify. |
| 3.7 maxHeartbeats | No override present or added. |

Strategy reflection: keep the already minimal exact composition. A tactic
experiment would not improve this one-term proof; no speculative alternatives
were run or applied. The fresh compiler and diagnostics checks validate the
retained declaration itself.

## Validation gates

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: lake build Roth.HasseDeriv, exit 0, 1430 jobs. /private/tmp/roth-hasseDeriv_zero-module-build.log. |
| fresh LSP | PASS: bridge exit 0; success=true, partial=false, timed_out=false, failed_dependencies=[]; no errors, only existing header warning. /private/tmp/roth-hasseDeriv_zero-postedit-diagnostics.json. |
| definition_protected | PASS: no source edits. |
| theorem_statement_protected | PASS: full source byte-identical. |
| structure_gate | PASS: one-term proof; no extraction needed. |
| naming_gate | PASS: existing name matches mathlib counterpart. |
| line_packing_gate | PASS: signature 96 characters; appending body would produce 132. |
| inequality_orientation_gate | PASS: no inequalities. |
| scoped diff | PASS: git diff for source empty; git diff --check exit 0. |
| dependent closure | PASS: parent reports full lake build exit 0, 2586 jobs; separate lake build Roth.LeanEval exit 0, 2585 jobs. Logs /private/tmp/roth-hasseDeriv_zero-build.log and /private/tmp/roth-hasseDeriv_zero-leaneval.log. |

A fresh `lean_run_code` inspection imports the built module to check the exact
target's type and axioms; it is an inspection of the existing theorem, not an
isolated candidate proof. Bridge exit 0, success=true, timed_out=false;
`#check` confirms the original arbitrary σ/R/CommSemiring parameters and bundled
identity conclusion. `#print axioms` reports exactly
`[propext, Classical.choice, Quot.sound]`. Evidence:
`/private/tmp/roth-hasseDeriv_zero-axioms.json`. A subprocess teardown warning
followed the successful diagnostics response; it did not invalidate the complete
result or change the process's zero exit status.

No sorry, new axiom, native_decide, option, import, version, rename, structure or
source edit. Existing header warning remains deferred pending ownership/license
information. This checkpoint records a completed review without unnecessary edits.

## Phase 4 checklist

- [x] Step 1: inherited workflow/references and target context reviewed.
- [x] Step 2: all 24 target audit dispositions.
- [x] Step 2.5: five search methods with directly relevant evidence reuse disclosed.
- [x] Step 2.6: all parameters, inversion and local/public literature reviewed.
- [x] Step 2.7: complete signature-width table.
- [x] Step 2.8: complete inequality scan.
- [x] Step 3: all 42 golfing rules considered.
- [x] Step 4: strategy reassessed; no gratuitous replacement.
- [x] Step 5a: module build and complete fresh diagnostics passed.
- [x] Step 5b: protection, structure, naming, packing and scoped-diff gates passed.
- [x] Step 6a: no new rename or structure queue.

Parent owns dependent validation, shared progress logs, commit/push and file-wide phases.
