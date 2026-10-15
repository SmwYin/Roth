# Cleanup audit: `MvPolynomial.coeff_hasseDeriv`

Date: 2026-10-15 (America/Chicago). Baseline: pushed checkpoint `2d62138`.
Target: `Roth/HasseDeriv.lean:83–94`. Replaced a hand-written subtraction
contradiction inside `simp` with the standard `tsub_eq_iff_eq_add_of_le` lemma.
The public statement, parameters, name, visibility, documentation and citation are
unchanged. The proof still uses monomial/addition induction and the same case split.

## Workflow basis

This dedicated Phase 4 worker applied the inherited mathlib-quality and lean4
workflow and full reference review. Native Lean MCP tools are absent from this
leaf's registry. The orchestrator supplied actual native remote-search results;
local search and diagnostics use the approved Lean LSP MCP 0.31.0 bridge.
This distinction describes actual session capabilities, not an installation claim.

## All 24 audit items

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Fresh complete post-edit diagnostics: no errors; only existing header warning. |
| 2 | HAVE SCAN | No have bindings. |
| 3 | SET_OPTION | No options present or added. |
| 4 | SIMP SQUEEZE | All simp calls are terminal; retain unsqueezed simp. |
| 5 | NAMING | `coeff_hasseDeriv` describes the outer coefficient and inner operator. Retain established API. |
| 6 | LINE PACKING | Both signature lines checked below; combined signature exceeds 100. |
| 7 | BY PLACEMENT | `by` remains at the end of the conclusion line. |
| 8 | FORMAT | Existing indentation and case arrows correct; removed semicolon-chained nested proof. |
| 9 | COMMENTS | No proof comments; documentation and source citation preserved. |
| 10 | DOCSTRING | Describes exact coefficient formula and its downstream computational role. |
| 11 | VISIBILITY | Public result used throughout this file and in CoeffNorm; retain. |
| 12 | STRUCTURE | Short two-constructor induction with explicit monomial cases; no extraction needed. |
| 13 | MATHLIB | Five methods attempted; reuse standard subtraction lemma. LeanSearch failed with HTTP 500. |
| 14 | JUNK DEF | n/a: theorem. |
| 15 | EXISTS LEMMA | No existential statement. |
| 16 | SHOW vs CHANGE | Removed inline show entirely by using a library equivalence. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every parameter/context reviewed below; no unsupported statement change. |
| 19 | INEQUALITY | One case condition d ≤ k, already smaller side left. |
| 20 | NORMAL-FORM | Coefficient of an operation rewrites to a scalar times an original coefficient. |
| 21 | SYNTAX-GEN | No custom syntax or redundant bundled property. |
| 22 | IMPORT-FANOUT | No import change; lemma already available from existing dependencies. |
| 23 | CASTS | 0 dropped / 1 retained / 0 added in statement; natural coefficient must enter R. |
| 24 | INSTANCE-NAME | n/a: not an instance. |

## Signature width and inequality tables

Lengths are Unicode codepoints measured with Python `len`.

| Signature line | Before | After | Next syntactic unit | Arithmetic/action |
|---|---:|---:|---|---|
| 83, name and binders | 64 | 64 | Complete conclusion plus `:= by` (77 unindented characters) | 64 + 1 + 77 = 142 > 100; ok to break. |
| 84, conclusion and `:= by` | 81 | 81 | None | 81 ≤ 100; ok. |

The changed proof line shrinks from 88 to 45 characters. No overlong target line,
split binder, standalone `by`, or avoidable continuation remains.

| Occurrence | Orientation | Action |
|---|---|---|
| Statement | No inequality | No change. |
| `by_cases hdk : d ≤ k` | Derivative multi-index ≤ monomial exponent | Retain the correct non-strict boundary and smaller side on the left. |
| Removed inline contradiction | Was the disequality `k - d ≠ e`, not an order comparison | Replaced by standard subtraction equivalence; hk already supplies the contradiction. |

## Five-method mathlib search

| Method | Query/scope | Observed result |
|---|---|---|
| A Lean-Finder | `coefficient of multivariate Hasse derivative at e equals binomial factor times coefficient at e plus derivative multi-index` | Polynomial.hasseDeriv_coeff, Polynomial.hasseDeriv_apply, LaurentSeries.hasseDeriv_comp_coeff. |
| B Loogle | `"hasseDeriv_coeff"` | Polynomial.hasseDeriv_coeff and LaurentSeries.hasseDeriv_coeff. |
| C LeanSearch | `Hasse derivative coefficient formula for polynomials` | HTTP 500; unavailable service, not evidence of no matches. |
| D Pinned source/project search | `coeff_hasseDeriv`, `hasseDeriv_coeff`, subtraction equivalence names | Inspected univariate and Laurent-series formulas, existing project callers, and tsub_eq_iff_eq_add_of_le. |
| E Local MCP | `coeff_hasseDeriv`, limit 20 | Found the project declaration. Index reports unavailable; source-name matching works. |

Evidence: `/private/tmp/roth-coeff_hasseDeriv-native-search.json` and
`/private/tmp/roth-coeff_hasseDeriv-local.json`. Remote results were checked against
the pinned sources, rather than assuming that a remote index matches project versions.
The polynomial theorem has a single natural exponent; Laurent-series coefficients
use integer exponents and a different representation. Neither directly replaces this
multivariate theorem. The local theorem is important public API, not a redundant
wrapper around an identical library result. The generic truncated-subtraction lemma
in `Mathlib/Algebra/Order/Sub/Unbundled/Basic.lean` applies directly to the proof and
is now used. No import or module-doc change is needed.

Replacement checklist: actual callers inspected; all five methods attempted;
generic algebraic ingredients and univariate/series variants checked; no custom
predicate requires normalization; no identical replacement established; no deletion
or downstream rewrite warranted. Topology/finiteness/separation equivalents are
inapplicable. Bounded searches do not prove exhaustive absence of related results.

## Generalisation, inversion and literature

| Parameter/context | Role and assessment |
|---|---|
| `{σ : Type u}` | Already arbitrary, without finiteness, decidability or nonemptiness requirements. |
| `{R : Type v}` | Arbitrary coefficient type supporting the given commutative semiring structure. |
| `[CommSemiring R]` | Supplies the existing public hasseDeriv construction and coefficient arithmetic; no field, characteristic-zero or domain assumption. |
| `(d : σ →₀ ℕ)` | Derivative order occurs in both sides; not removable. |
| `(e : σ →₀ ℕ)` | Coefficient exponent occurs in both sides; not removable. |
| `(P : MvPolynomial σ R)` | Arbitrary polynomial; no degree, support or nonzero hypothesis. |

No propositional hypothesis can be dropped or localized. There is no unnecessary
finiteness assumption to weaken. A noncommutative-semiring or module-valued
formulation would first require reviewing/changing the earlier derivative
construction and its typeclass interface; this is an unimplemented broader API
proposal, not a proved generalization. It is deferred under the user's instruction
to leave substantial definition/statement changes unapplied and continue independent
cleanup. The existing result already works in positive characteristic, unlike
factorial-division formulas. Fixing d or e would specialize rather than generalize it.

Inversion review: the mathematical content is the coefficient rule for a linear
operator on a monomial basis. The generic coefficient, induction, and subtraction
facts already exist. The old nested contradiction was a special instance of the
library subtraction equivalence; the new proof reuses that abstraction. A new
generic linear-operator helper would add structure without eliminating substantial
repeated work here, so none is introduced.

Local `clean.tex` §1 explicitly states this coefficient formula in its Lean note.
A fresh public inspection of §2.1, p.6 of
[Dvir–Kopparty–Saraf–Sudan, Extensions to the Method of Multiplicities](https://eccc.weizmann.ac.il/report/2009/004/download/)
confirmed the multi-index binomial product and Hasse derivative defined by extracting
coefficients of a translated polynomial. Inference: expanding monomials in that
definition yields the coefficient formula here. The paper's field formulation is
not claimed to contain this exact Lean statement over arbitrary commutative semirings.
Optional ask_chatgpt_math skipped as authorized.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | No whole-proof wrapper; nested exact removed with standard lemma. |
| 1.2 by rfl | None. |
| 1.3 rw + exact | Rewriting is followed by meaningful cases, not a directly reusable premise. |
| 1.4 simp + exact | None. |
| 1.5 trailing rfl | None. |
| 1.6 constructor chain | No conjunction constructor. Induction is substantive. |
| 1.7 apply + exact | None. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | No lambda; induction case arrows are syntax. |
| 1.10 single-use have | None. |
| 1.11 apply + intro | None. |
| 1.12 redundant show | Applied: removed nested show proof, reuse subtraction iff. |
| 1.13 have projections | None. |
| 1.14 merge rw | One rw call already groups the required rewrites. |
| 1.15 terminal simp only | All terminal calls already use simp. |
| 1.16 nonterminal simp | None. |
| 1.17 dot notation | Existing iff projection .2 and coefficient notation are appropriate; no new opportunity. |
| 1.18 `<\|` | No nested final function argument needing it. |
| 1.19 push Not | No push_neg. |
| 1.20 trivial existential | No existential. |
| 2.1 grind | Deterministic library lemma closes the relevant branch; broader search unnecessary. |
| 2.2 delete before grind | n/a: no grind. |
| 2.3 simpa consolidation | Direct terminal simp closes each branch; no using premise needed. |
| 2.4 fun_prop | No analytic/function-property goal. |
| 2.5 positivity | No independent positivity subgoal. |
| 2.6 gcongr | Equality goal, not monotonicity. |
| 2.7 lia/omega | Generic subtraction equivalence avoids coordinatewise arithmetic automation. |
| 2.8 aesop | Explicit short induction and deterministic branch simplification retained. |
| 2.9 norm_num/norm_cast | Symbolic coefficients; retained cast is essential. |
| 2.10 decide/kernel | Open symbolic theorem, not a finite closed decision problem. |
| 2.11 field_simp/ring | No denominators; distributivity in addition branch already handled by simp. |
| 2.12 linear_combination | No algebraic hypotheses to combine. |
| 2.13 wlog | Cases have distinct algebraic roles, not symmetry. |
| 2.14 calc | Would add structure to a local equivalence rewrite without clarifying the induction. |
| 2.15 `<;>` | Cases use different hypotheses; no repeated identical tactic sequence. |
| 3.1 erw/rw | Existing rw suffices. |
| 3.2 fun_prop | No legacy analytic tactic. |
| 3.3 omega/lia | Neither occurs. |
| 3.4 rcases rfl | Removed nested rintro rfl with the whole manual contradiction. |
| 3.5 automation attributes | No attribute change; public simp behavior remains unchanged. |
| 3.6 simp_all | Context is small; explicit hypotheses show the two mathematical cases. |
| 3.7 maxHeartbeats | No override present or added. |

Strategy reflection: a first isolated attempt dropped the equality split and split
only on d ≤ k. That left conditional coefficient equalities unsolved. Retaining the
existing equality split keeps the proof explicit, while the standard subtraction
lemma removes the only manually proved algebraic fact. No new helper is needed.

## Experiments and validation

The final isolated probe imports only the original mathlib dependencies and copies
the preceding project declarations, renaming the target to `probe`. It excludes the
actual target and all later declarations, so simp cannot circularly use the theorem
under audit. `lake env lean` exited 0; `#print axioms` returned only
`[propext, Classical.choice, Quot.sound]`. Evidence:
`/private/tmp/roth-coeff_hasseDeriv-probe.lean`.

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: lake build Roth.HasseDeriv, exit 0, 1430 jobs. /private/tmp/roth-coeff_hasseDeriv-module-build.log. |
| post-edit LSP | PASS: complete success=true, partial=false, timed_out=false, failed_dependencies=[]; no errors, only existing header warning. /private/tmp/roth-coeff_hasseDeriv-postedit-diagnostics.json. |
| definition_protected | PASS: no definition or abbreviation changed. |
| theorem_statement_protected | PASS: statement, binders, name, visibility, documentation and citation unchanged. |
| structure_gate | PASS: same short induction/case structure; no extraction needed. |
| naming_gate | PASS: descriptive established API retained. |
| line_packing_gate | PASS: complete signature table; target maximum 81 after edit. |
| inequality_orientation_gate | PASS: sole order case is d ≤ k. |
| scoped diff | PASS: only intended proof-line replacement in source; git diff --check exits 0. |
| dependent closure | PASS: orchestrator full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs), both exit 0. Logs `/private/tmp/roth-coeff_hasseDeriv-build.log` and `/private/tmp/roth-coeff_hasseDeriv-leaneval.log`. |

No new axiom, placeholder, native_decide, option, import or version change.
The bridge emitted an asynchronous destructor warning after returning the complete
successful diagnostic result and exited 0; the warning is not a Lean error.
No rename or structural action queued. Broader coefficient-type API proposal is
deferred as above; existing file-header ownership/license warning is not repaired
with invented attribution.

## Phase 4 checklist

- [x] Step 1: inherited workflow/reference review and target context.
- [x] Step 2: all 24 target-specific audit dispositions.
- [x] Step 2.5: all five search methods, with remote failure disclosed.
- [x] Step 2.6: every parameter, inversion and local/public literature considered.
- [x] Step 2.7: complete signature width table.
- [x] Step 2.8: complete inequality scan.
- [x] Step 3: all 42 golfing rules considered; library-lemma simplification tested.
- [x] Step 4: strategy reconsidered and proof independently compiled.
- [x] Step 5a: module build and fresh complete diagnostics passed.
- [x] Step 5b: protection, naming, structure, packing and scoped-diff gates.
- [x] Step 6a: no rename/structural queue entry; broader API proposal deferred.

Parent owns dependent validation, shared progress logs, commit/push and file-wide phases.
