# Cleanup audit: `MvPolynomial.hasseDeriv_hasseDeriv`

Date: 2026-10-15 (America/Chicago). Baseline: pushed `7df4a50`.
Target: public theorem at `Roth/HasseDeriv.lean:172`.
Decision: retain the source unchanged. Its coefficient-extensionality proof
already expresses the composition law directly through the preceding private
binomial-product identity. An isolated simplifier alternative failed because
associativity changed the helper's matching subterm too early. The ordered
rewrite sequence remains concise and deliberate.

## Workflow and 24 audit items

Dedicated Phase 4 worker using the inherited mathlib-quality/lean4 references.
Parent supplied native remote searches. Native local search returned source
matches with index=unavailable. Native lean_run_code could not launch the
server because lake was missing from that server's PATH; the established
direct-client bridge was used for proof execution and diagnostics instead.
Optional ask_chatgpt_math skipped. No configuration changed.

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Module and complete fresh diagnostics passed; existing header warning only. |
| 2 | HAVE SCAN | No local have. |
| 3 | SET_OPTION | None. |
| 4 | SIMP SQUEEZE | Ordered rw is intentional; single simp alternative failed as detailed below. |
| 5 | NAMING | Repeated operator name accurately describes nested application. |
| 6 | LINE PACKING | Signature and proof all within 100 columns. |
| 7 | BY PLACEMENT | by remains on conclusion line. |
| 8 | FORMAT | Standard ext followed by one wrapped rw. |
| 9 | COMMENTS | No proof comments; source citation preserved. |
| 10 | DOCSTRING | Gives formula, binomial interpretation and disjoint specialization. |
| 11 | VISIBILITY | Public; used by Index and the next theorem. |
| 12 | STRUCTURE | Three-line proof, with combinatorial identity already separated appropriately. |
| 13 | MATHLIB | Five search methods and candidate assessment below. |
| 14 | JUNK DEF | No definition. |
| 15 | EXISTS LEMMA | No existential conclusion. |
| 16 | SHOW vs CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Arbitrary index type, commutative semiring and polynomial; no characteristic constraint. |
| 19 | INEQUALITY | Equality statement; no bounds to weaken. |
| 20 | NORMAL-FORM | Nested application reduces to summed derivative order with its exact scalar factor. |
| 21 | SYNTAX-GEN | Actual hasseDeriv/hasseCoeff definitions and coefficient theorem inspected. |
| 22 | IMPORT-FANOUT | No new import or abstraction needed. |
| 23 | CASTS | Two reverse Nat.cast_mul rewrites transport the natural coefficient identity to R. |
| 24 | INSTANCE-NAME | No instance declaration. |

## Signature width and inequality tables

Lengths count Unicode codepoints. The complete source is unchanged.

| Signature line | Before | After | Next unit | Arithmetic/action |
|---|---:|---:|---|---|
| 172: name, parameters and colon | 69 | 69 | Conclusion and := by, 87 characters | 69 + 1 + 87 = 157 > 100; ok. |
| 173: conclusion and := by | 91 | 91 | None | Complete signature; ok. |

Proof lines have widths 7, 97 and 86. The existing wrapping satisfies 100 columns.

| Scope | Relation | Assessment |
|---|---|---|
| Statement | Equality of multivariate polynomials | No strictness, ordering or inequality-direction choice. |
| Proof | Equality of every coefficient | Exact extensionality, with no extra hypothesis. |

## Five-method mathlib search

| Method | Query/scope | Result |
|---|---|---|
| A Lean-Finder | multivariate Hasse derivative composition binomial coefficient scalar multiplication; limit 3 | Polynomial.hasseDeriv_comp, mul and apply. |
| B Loogle | "hasseDeriv_comp"; limit 5 | Polynomial.hasseDeriv_comp and LaurentSeries.hasseDeriv_comp/comp_coeff. |
| C LeanSearch | Same natural-language composition query; limit 3 | HTTP 500; unavailable, not evidence of absence. |
| D Pinned sources/project | hasseDeriv_comp and hasseDeriv_hasseDeriv; inspected definitions, coefficients and callers | Polynomial and LaurentSeries analogues; Roth.Index uses this theorem directly. |
| E Native local search | hasseDeriv_comp; limit 10 | Same three declarations; index unavailable, source matches returned successfully. |

Remote evidence: `/private/tmp/roth-hasseDeriv_hasseDeriv-native-search.json`.
Pinned `Mathlib/Algebra/Polynomial/HasseDeriv.lean:154` states composition of
univariate linear maps with a single natural order and binomial coefficient.
It does not directly supply the multivariate finite-support order identity.
`Mathlib/RingTheory/LaurentSeries.lean:156` and `:165` use a single natural
order on Laurent series with integer-indexed coefficients. Their coefficient
proof confirms the same structure but uses generalized integer binomials;
transporting through a different polynomial/series representation would add
substantial machinery. The existing coefficient theorem and private product
identity are the appropriate local APIs. No exact replacement was found among
the inspected candidates, and the failed search service is not counted as
negative evidence.

Replacement checklist: inspected actual definitions and candidate types;
searched both application-level and composition-level formulations; retained
the direct coefficient API rather than adding an equivalent wrapper. No
hidden predicate or separation hypothesis needs unfolding. Source usage in
`Roth/Index.lean:115` requires exactly this application-level orientation.

## Parameters, generalisation, inversion and literature

| Parameter/context | Assessment |
|---|---|
| σ : Type* | Arbitrary variables; no Fintype or DecidableEq assumption. |
| R : Type*, CommSemiring R | Matches the MvPolynomial representation and existing linear derivative API. |
| d, e : σ →₀ ℕ | Arbitrary finite-support orders; neither positivity nor disjointness imposed. |
| P : MvPolynomial σ R | Arbitrary polynomial, including zero. |
| Characteristic/nontriviality | No restriction; the binomial factor is allowed to vanish. |

The univariate mathlib theorem uses Semiring, but weakening this theorem's
instance would require changing the multivariate polynomial/derivative
interface, not deleting an unused hypothesis. No such change is proposed as
routine cleanup. A linear-map composition version follows by extensionality,
but adding a new public API is unnecessary for current callers. Inversion of
the coefficient proof exposes precisely hasseCoeff_mul_hasseCoeff, already
proved separately. Removing its scalar factor would be false in general;
the following theorem legitimately specializes to disjoint supports instead.

Local `.mathlib-quality/references/clean.tex:571–588` uses this exact
multivariate composition identity in the proof of index-of-derivative.
Freshly inspected [ECCC report 2026/032, Lemma 2.7(3)](https://eccc.weizmann.ac.il/report/2026/032/download/)
states the multivariate Hasse iteration identity over fields; Lemma 2.4(3)
gives the univariate version. The Lean theorem has arbitrary commutative
semiring coefficients and finite-support variable indices. Inference from
the coefficient argument: the proof needs neither division nor a nonzero
factor, so its broader coefficient setting is consistent with the formula.
No substantive generalization, renaming or structural change is needed.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | Coefficient extensionality and normalization are necessary. |
| 1.2 by rfl | Composition law is not definitional. |
| 1.3 rw + exact | No trailing exact. |
| 1.4 simp + exact | None. |
| 1.5 trailing rfl | None. |
| 1.6 constructor chain | None. |
| 1.7 apply + exact | None. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | No lambda. |
| 1.10 single-use have | No have. |
| 1.11 apply + intro | None. |
| 1.12 redundant show | None. |
| 1.13 have projections | None. |
| 1.14 merge rw | Already one rw chain; repeated rules act at distinct occurrences. |
| 1.15 terminal simp only | Original has no simp only; proposed terminal simp only failed. |
| 1.16 nonterminal simp | Splitting normalization from the final rewrite would lengthen the proof. |
| 1.17 dot notation | Global coefficient/cast identities appropriate as written. |
| 1.18 `<\|` | No nested term application needing regrouping. |
| 1.19 push Not | None. |
| 1.20 trivial existential | None. |
| 2.1 grind | No residual propositional or arithmetic goal; explicit named identity solves it directly. |
| 2.2 delete before grind | No grind. |
| 2.3 simpa consolidation | Tested normalization fails to preserve the helper's matching form; retain ordered rewrites. |
| 2.4 fun_prop | No function-property goal. |
| 2.5 positivity | No positivity goal. |
| 2.6 gcongr | Equality proof uses coefficient extensionality, not monotonicity. |
| 2.7 lia/omega | Symbolic binomial identity, not linear arithmetic. |
| 2.8 aesop | Existing three-line proof exposes all mathematical inputs without search. |
| 2.9 norm_num/norm_cast | Reverse cast multiplication is explicitly needed twice; no numeric evaluation. |
| 2.10 decide/kernel | Symbolic polynomial statement. |
| 2.11 field_simp/ring | No division; ring cannot supply the binomial composition identity. |
| 2.12 linear_combination | No combination of polynomial hypotheses. |
| 2.13 wlog | No case symmetry argument needed. |
| 2.14 calc | Single coefficient normalization has no missing conceptual intermediate. |
| 2.15 `<;>` | No parallel goals. |
| 3.1 erw/rw | No definitional coercion mismatch. |
| 3.2 fun_prop | No analytic automation. |
| 3.3 omega/lia | Neither occurs. |
| 3.4 rcases rfl | No destructuring. |
| 3.5 automation attributes | None added; public theorem's attributes retained. |
| 3.6 simp_all | No local hypotheses to saturate. |
| 3.7 maxHeartbeats | None introduced or present. |

Strategy reflection: the candidate used simp only with coeff_smul,
coeff_hasseDeriv, smul_eq_mul, reverse mul_assoc, reverse Nat.cast_mul,
hasseCoeff_mul_hasseCoeff and add_assoc. Simplification normalized f+d+e
inside the coefficient factors before the private helper could match;
Lean reported an unsolved coefficient equality and an unused helper argument.
This failure is recorded in `/private/tmp/roth-hasseDeriv_hasseDeriv-probe.log`.
The failed scratch theorem's sorryAx diagnostic is the elaborator's placeholder
for its unsolved goal, not accepted proof evidence or a repository change.
The original ordered proof was tested separately in a prefix-only scratch
module: it cannot use itself or any downstream theorem. No broad automation
failure or performance result is claimed without measurement.

## Validation gates

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: lake build Roth.HasseDeriv, exit 0,1430 jobs; /private/tmp/roth-hasseDeriv_hasseDeriv-module-build.log. |
| Fresh whole-file LSP | PASS: direct-client exit 0; success=true,partial=false,timed_out=false,failed_dependencies=[]; no errors, existing header warning only. /private/tmp/roth-hasseDeriv_hasseDeriv-postedit-diagnostics.json. |
| Proof/type/axioms | PASS: prefix-only original proof, exit 0,success=true,timed_out=false; exact type and only propext,Classical.choice,Quot.sound. /private/tmp/roth-hasseDeriv_hasseDeriv-original-probe.log. |
| definition_protected | PASS: source byte-identical. |
| theorem_statement_protected | PASS: source byte-identical. |
| structure_gate | PASS: no source change. |
| naming_gate | PASS: no rename needed or applied. |
| line_packing_gate | PASS: widths and arithmetic above. |
| inequality_orientation_gate | PASS: equality only. |
| Scoped diff | PASS: git diff -- Roth/HasseDeriv.lean empty; git diff --check exit 0. |
| Dependent closure | PASS: orchestrator full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs), both exit 0. Logs `/private/tmp/roth-hasseDeriv_hasseDeriv-build.log` and `/private/tmp/roth-hasseDeriv_hasseDeriv-leaneval.log`. |

Native server failure evidence:
`/private/tmp/roth-hasseDeriv_hasseDeriv-native-runcode-error.json`.
It reports `[Errno 2] No such file or directory: 'lake'`; native tool
registration alone is not proof of usable native LSP execution. Direct-client
fallback outcomes are tracked independently above.
The original-proof bridge emitted an asynchronous transport shutdown warning,
but returned a complete successful Lean response and process exit 0.

No sorry, new axiom, native_decide, option, import, version, mathematical
statement, definition, visibility or project structure changed. Existing
header warning remains deferred for ownership/license information.

## Phase 4 checklist

- [x] Step 1: inherited references and target context reviewed.
- [x] Step 2: all 24 audit items assessed.
- [x] Step 2.5: five searches, pinned candidate inspection and unavailable service disclosed.
- [x] Step 2.6: parameters, generalisation, inversion and local/public literature.
- [x] Step 2.7: full signature-width table.
- [x] Step 2.8: inequality scan.
- [x] Step 3: all 42 golfing rules considered.
- [x] Step 4: isolated alternative tested; source retained with strategy reflection.
- [x] Step 5a: module and fresh complete diagnostics passed.
- [x] Step 5b: protection, naming, packing and scoped-diff gates.
- [x] Step 6a: no substantive proposal requiring changes; no rename queue.

Parent owns dependent validation, shared logs, commit/push and file-wide phases.
