# Cleanup audit: `MvPolynomial.hasseDeriv_monomial`

Date: 2026-10-15 (America/Chicago). Target: `Roth/HasseDeriv.lean:60–62`.
Baseline: parent's pushed `59d451d` checkpoint. Changed only the proof from
`(sum_monomial_eq (by simp)).trans (by simp)` to `by simp [hasseDeriv]`.
The statement, name, visibility, simp attribute, documentation and citation are preserved.
Both versions have three declaration lines; the proof body shrank from 45 to 19 codepoints.

## Workflow basis

Applied the parent's complete Phase 4 workflow, reading the target, prior audit,
golfing rules, proof patterns, mathlib-search guide, generalisation catalogue,
cleanup gates, and relevant style sections. The bridge exposes Lean LSP MCP 0.31.0;
this worker's tool snapshot lacks native MCP tools, so it uses the verified direct bridge.
The parent independently verified newly registered native search tools too.

## All 24 audit items

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Fresh complete post-edit LSP has no errors; only the pre-existing file-header warning at line 1. |
| 2 | HAVE SCAN | No `have` terms. |
| 3 | SET_OPTION | No target options; none introduced. |
| 4 | SIMP SQUEEZE | Both original nested `simp` calls were terminal. Replacement `simp [hasseDeriv]` is also terminal, so leave unsqueezed. |
| 5 | NAMING | Describes the operation and monomial input; agrees with the univariate `Polynomial.hasseDeriv_monomial` naming pattern. No forbidden abbreviation or numeric pattern. |
| 6 | LINE PACKING | All signature lines measured below; complete conclusion cannot share the parameter line. |
| 7 | BY PLACEMENT | Replacement `by` is at the end of the conclusion line. |
| 8 | FORMAT | Four-space conclusion continuation, two-space proof indentation, one tactic, no internal blank lines or whitespace defects. |
| 9 | COMMENTS | No inline proof comments to relocate; existing docstring/source citation retained verbatim. |
| 10 | DOCSTRING | Existing sentence states the monomial computation and source §1; adequate for this elementary simp rule. |
| 11 | VISIBILITY | Public API used explicitly by `Roth/Taylor.lean` and the surrounding Hasse-derivative API; retain. |
| 12 | STRUCTURE | One-line proof, no conjunction, no branches; no decomposition needed. |
| 13 | MATHLIB | Five methods attempted; four produced useful results, LeanSearch returned HTTP 500 after DNS retry. Details below. |
| 14 | JUNK DEF | n/a: theorem, not definition. |
| 15 | EXISTS LEMMA | n/a: equality, not an existential. |
| 16 | SHOW vs CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | All six parameters inspected below; no safe signature weakening established. |
| 19 | INEQUALITY | None in signature, hypotheses or proof; complete scan table below. |
| 20 | NORMAL-FORM | Derivative-on-monomial reduces to a monomial with explicit coefficient/exponent; already the canonical computation direction. |
| 21 | SYNTAX-GEN | Explicit derivative index, monomial exponent and coefficient make direct rewriting straightforward; no easier restatement identified. |
| 22 | IMPORT-FANOUT | No import added or changed. |
| 23 | CASTS | 0 dropped / 1 kept cross-type / 0 new load-bearing: `(hasseCoeff d k : R)` casts ℕ to R, unchanged. |
| 24 | INSTANCE-NAME | n/a: not an instance. |

## Signature width and inequality tables

Unicode codepoint lengths measured with Python `len`. `#check` at width 100 returned:

```lean
@hasseDeriv_monomial : ∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (d k : σ →₀ ℕ) (a : R),
  (hasseDeriv d) ((monomial k) a) = (monomial (k - d)) (↑(hasseCoeff d k) * a)
```

| Signature line | Before | After | Next syntactic unit | Arithmetic/action |
|---|---:|---:|---|---|
| 60 | 52 | 52 | Full conclusion through `:= by`, 79 characters without indentation | 52 + 1 + 79 = 132 > 100; retain conventional break after colon. |
| 61 | 80 | 83 | None; proof body follows | 83 ≤ 100; packed. |

Before the proof change the same conclusion unit measured 76, so 52 + 1 + 76 = 129 > 100.
This uses the complete conclusion as the signature unit, consistent with the reference's
medium-length theorem example and the pretty-printer; it does not split the equality arbitrarily.

| Scope | Inequality occurrences | Rewrite/rename |
|---|---|---|
| Entire statement, hypotheses and body | None (`=` is equality) | None. |

## Five-method mathlib search

| Method | Query/scope | Result |
|---|---|---|
| A Lean-Finder | `Hasse derivative of a multivariate monomial binomial coefficient` | Initial sandbox DNS failure; approved direct retry succeeded, returning univariate `Polynomial.hasseDeriv_monomial`, `hasseDeriv_apply`, `hasseDeriv`. Parent's native query also found the univariate coefficient lemma. |
| B Loogle | `"hasseDeriv_monomial"` | Initial DNS failure; approved retry succeeded, returning `Polynomial.hasseDeriv_monomial`. |
| C LeanSearch | `Hasse derivative applied to monomial of multivariate polynomial` | Initial DNS failure; approved retry returned HTTP 500. Parent's native query independently returned HTTP 500. Unavailable, not a negative search. |
| D Source search | Full-name `hasseDeriv_monomial`, `sum_monomial_eq`, `lsum_single` in pinned source; project callers | Found univariate analogue, generic `MvPolynomial.sum_monomial_eq`, `Finsupp.lsum_single`, and Taylor callers. Inspected definitions/types. |
| E Local MCP | `hasseDeriv_monomial`, limit 30 | Success: project theorem, univariate theorem and private project multiplication lemma; index status `unavailable` but source results available. |

Parent's retained native-search evidence:
`/private/tmp/roth-hasseDeriv_monomial-native-search.json`.
Remote results are candidates, checked against pinned local sources. The univariate
theorem has domain `Polynomial R`, whereas this result concerns `MvPolynomial σ R`;
it is not a drop-in replacement. Generic sum/linear-extension evaluation infrastructure
already proves the calculation, and the new proof uses that infrastructure through simp.
No claim of exhaustive mathematical absence is made.

Six replacement considerations: (1) retain this useful public simp interface for the
project-defined operator; deleting it would be an API refactor outside the assigned scope,
not a routine wrapper cleanup; (2) all methods attempted with service limits explicit;
(3) generic sum and linear-extension variants inspected; (4) no custom predicate;
(5) no equivalent multivariate public operator theorem established; (6) no new import or
API dependency requiring module-doc changes. The common-equivalents topology/finiteness/
separation table has no applicable entry.

## Generalisation and inversion

| Parameter | Role | Drop/weaken analysis |
|---|---|---|
| `{σ : Type u_1}` | Variable type in exponent and polynomial | Arbitrary independent universe, no finite/decidable restrictions; needed to bind the types. |
| `{R : Type u_2}` | Coefficient type | Arbitrary independent universe; used in coefficient, cast and polynomial type. |
| `[CommSemiring R]` | Polynomial/algebra structure | Required by pinned `MvPolynomial`, `monomial` and the operator. A bare `Semiring R`, `NonUnitalCommSemiring R`, or `CommMonoidWithZero R` cannot supply that interface. No unsupported weakening claimed. |
| `(d : σ →₀ ℕ)` | Derivative order | Used in both subtraction and binomial factor; dropping changes the proposition. |
| `(k : σ →₀ ℕ)` | Monomial exponent | Used in input, output and binomial factor; dropping changes the proposition. |
| `(a : R)` | Arbitrary monomial coefficient | Needed on both sides; fixing it to one would specialize rather than generalize. |

No propositional hypothesis to drop, strict inequality to weaken, global analytic
condition to localize, or bundled equivalence to unbundle. Finite support is part of
the current polynomial exponent representation. Generalizing that representation or
the operator's coefficient algebra would require substantive changes; none proposed.

The inversion diagnostic does fire: after unfolding the named operator, its evaluation
is just evaluation of a generic finitely supported linear extension on a singleton.
That abstract result is already `Finsupp.lsum_single` (with `sum_monomial_eq` giving the
polynomial-facing version). Thus no new generic helper is needed; retain the concrete
simp API so callers need not unfold the linear-map construction.

Literature check: local `clean.tex` §1 explicitly defines the monomial action with the
product of binomial coefficients and zero outside componentwise order, and explicitly
allows commutative semirings. The present formula handles the zero case in the coefficient.
Fresh web search returned the translation/coefficient-extraction definition in
[Fast Multivariate Multipoint Evaluation over All Finite Fields, Definition 3.4](https://doi.org/10.1145/3652025)
and [Improved PIR Schemes using Matching Vectors and Derivatives, Definition 3.5](https://www.math.utoronto.ca/swastik/PIR.pdf).
The author-copy PDF fetch timed out in this worker; no full-text inspection claimed.
Inference from the retrieved definitions and local source: they do not demand a stronger
or wider statement for this monomial computation. Optional `ask_chatgpt_math` skipped as authorized.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | No redundant exact wrapper; final tactic performs simplification. |
| 1.2 by rfl | No such wrapper. Evaluation uses sum/single lemmas rather than pure reflexivity. |
| 1.3 rw + exact | n/a: absent. |
| 1.4 simp + exact | No such sequential pair; complete simp replacement verified. |
| 1.5 trailing rfl | n/a: absent. |
| 1.6 constructor chain | n/a: equality computation, no constructor chain. |
| 1.7 apply + exact | n/a: absent. |
| 1.8 by_contra + push_neg | n/a: no negation. |
| 1.9 eta reduction | n/a: no lambda in target proof. |
| 1.10 single-use have | n/a: none. |
| 1.11 apply + intro | n/a: none. |
| 1.12 redundant show | n/a: none. |
| 1.13 have projections | n/a: none. |
| 1.14 merge rw | n/a: none. |
| 1.15 terminal simp only | No original squeezed simp; final terminal simp intentionally unsqueezed. |
| 1.16 nonterminal simp | No nonterminal simp. |
| 1.17 dot notation | Original `.trans` was natural; entire chain now removed. |
| 1.18 `<\|` | Original final `(by simp)` could use `<\|`; larger verified simp consolidation removes that application. |
| 1.19 push Not | n/a: absent. |
| 1.20 trivial existential | n/a: not existential. |
| 2.1 grind | Submitted isolated and live alternatives; results recorded below, not assumed successful. |
| 2.2 delete before grind | n/a: final proof has no grind or preliminary tactics. |
| 2.3 simpa consolidation | Submitted explicit `sum_monomial_eq` alternative; direct `simp [hasseDeriv]` is independently verified and shorter. |
| 2.4 fun_prop | n/a: no analytic/function-property goal. |
| 2.5 positivity | n/a: not an order or nonzero goal. |
| 2.6 gcongr | n/a: no inequality. |
| 2.7 lia/omega | n/a: polynomial evaluation, not linear arithmetic. |
| 2.8 aesop | Submitted isolated and live alternatives; final deterministic simp is verified. |
| 2.9 norm_num/norm_cast | n/a: arbitrary coefficients/orders; no concrete numerals or cast-normalization subgoal. |
| 2.10 decide/kernel | n/a: equality over arbitrary coefficient and variable types, no finite decision problem. |
| 2.11 field_simp/ring | n/a: no denominator, field or ring normalization problem. |
| 2.12 linear_combination | n/a: no ring-closing proof with algebraic hypotheses. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 calc | Original term already composes equalities; final proof removes the chain entirely. |
| 2.15 `<;>` | n/a: one goal, no generated branches. |
| 3.1 erw/rw | n/a: neither. |
| 3.2 fun_prop | n/a: no legacy analytic tactic. |
| 3.3 omega/lia | n/a: neither. |
| 3.4 rcases rfl | n/a: no cases. |
| 3.5 automation attributes | Existing `@[simp]` has the appropriate terminating computation direction; preserved. |
| 3.6 simp_all | n/a: no local propositional context or simp_all call. |
| 3.7 maxHeartbeats | n/a: no override; none added. |

Strategy reflection: directly simplify the defining linear extension on a monomial.
This avoids an explicit equality transitivity chain without changing the mathematical
argument or forcing downstream users to unfold the definition themselves.

## Experiments and validation

The first exploratory `lean_run_code` imported `Roth.HasseDeriv` and succeeded, but its
simp evidence could see the original target theorem. It is **not** used to justify the edit.
It did supply the displayed type and baseline axiom list: `propext`, `Classical.choice`,
`Quot.sound` only.

A subsequent independent probe imported only
`Mathlib.Algebra.MvPolynomial.CommRing`, `Mathlib.Algebra.MvPolynomial.PDeriv`, and
`Mathlib.Tactic.Ring`; it recreated the two preceding definitions in a fresh `Probe`
namespace, then proved the target with `simp [hasseDeriv]`. It returned `success=true`,
`timed_out=false`, no errors, and only a scratch missing-`end Probe` style warning.
It imported neither the target nor downstream project theorems, so this test cannot
use the result being proved. The final real module build independently verifies the edit.

The earlier combined four-alternative scratch probe imported broad `Mathlib.Tactic`
and hit the bridge's 65-second timeout. No per-alternative outcome was returned;
it establishes neither success nor mathematical failure. A targeted live multi-attempt
was then submitted against the actual proof location with `grind [hasseDeriv]`, the
explicit `simpa using sum_monomial_eq` alternative, and `aesop (add simp [hasseDeriv])`.
It likewise returned only a 65-second timeout, with no per-attempt results; evidence:
`/private/tmp/roth-hasseDeriv_monomial-attempts.json`. Both bridge processes exited.
The alternatives are inconclusive, not reported as failed proofs or successful optimizations.
Read-only probes did not alter the source. The independently verified short simp proof
remains the chosen implementation.

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: `lake build Roth.HasseDeriv`, exit 0, 1430 jobs; rebuilt target in 7.1s. Log `/private/tmp/roth-hasseDeriv_monomial-module-build.log`. |
| postedit LSP | PASS: success=true, partial=false, timed_out=false, failed_dependencies=[]; only existing header warning. `/private/tmp/roth-hasseDeriv_monomial-postedit-diagnostics.json`. |
| definition_protected | PASS: no definition or abbreviation changed. |
| theorem_statement_protected | PASS: type, binders, name, attribute and visibility unchanged; only proof delimiter/body changes. |
| structure_gate | PASS: one-line proof; no branches/conjunctions. |
| naming_gate | PASS: descriptive operation/input name, no forbidden pattern. |
| line_packing_gate | PASS: complete two-line width table above, maximum 83. |
| inequality_orientation_gate | PASS: no inequalities. |
| scoped diff | PASS: exact whole-file comparison against `git show HEAD:Roth/HasseDeriv.lean` equals precisely the intended proof substitution; `git diff --check` exit 0. |
| dependent closure | PASS: orchestrator ran full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs), both exit 0. Logs `/private/tmp/roth-hasseDeriv_monomial-build.log` and `/private/tmp/roth-hasseDeriv_monomial-leaneval.log`. |

No new axiom, placeholder, native computation escape, import, version change or option
override was introduced. No rename/generalization/refactoring action is queued.

## Phase 4 checklist

- [x] Step 1: workflow/reference review.
- [x] Step 2: all 24 target-specific audit dispositions.
- [x] Step 2.5: all five search methods; service failure distinguished from empty results.
- [x] Step 2.6: every parameter, inversion and literature considered.
- [x] Step 2.7: complete signature width table.
- [x] Step 2.8: complete inequality scan.
- [x] Step 3: all 42 rules considered, applicable alternatives submitted.
- [x] Step 4: proof strategy reconsidered and simpler proof independently verified.
- [x] Step 5a: module build and fresh complete diagnostics passed.
- [x] Step 5b: protection, naming, structure, packing and scoped-diff gates passed.
- [x] Step 6a: no rename or structural queue entry required.

Parent owns full dependent validation, shared logs, commit/push and file-wide phases.
