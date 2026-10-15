# Cleanup audit: `MvPolynomial.hasseCoeff_mul_hasseCoeff`

Date: 2026-10-15 (America/Chicago). Baseline: pushed `d7575e6`.
Target: private lemma at `Roth/HasseDeriv.lean:152`.
Lambda arrows now use `↦`; terminal `simpa [← add_assoc]` replaces
`simpa only [Finsupp.add_apply, ← add_assoc]`. The shared-support product
argument is retained: it already uses the relevant mathlib API directly.
The full signature, private visibility, surrounding text and every other
source declaration are byte-identical.

## Workflow and 24 audit items

Dedicated Phase 4 worker, using inherited mathlib-quality/lean4 cleanup
references and inspecting target-specific APIs. Parent supplied native remote
search results; direct MCP supplied local search, live goal, isolated proof
execution and complete fresh diagnostics. Optional ask_chatgpt_math skipped.

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Module and fresh complete diagnostics passed; existing header warning only. |
| 2 | HAVE SCAN | hd is used twice, so its support inclusion remains named. |
| 3 | SET_OPTION | None present or introduced. |
| 4 | SIMP SQUEEZE | Terminal simpa uses standard simplification; explicit add_apply removed. |
| 5 | NAMING | Existing private product identity name matches both sides. |
| 6 | LINE PACKING | All three signature lines measured below. |
| 7 | BY PLACEMENT | by remains on the conclusion line. |
| 8 | FORMAT | Five lambda arrows normalized; indentation preserved. |
| 9 | COMMENTS | No internal comments to alter; adjacent source citations preserved. |
| 10 | DOCSTRING | Private helper has no public-documentation obligation. |
| 11 | VISIBILITY | Private; used by following composition theorem. |
| 12 | STRUCTURE | Short support-product proof is a useful separation from polynomial coefficient reasoning. |
| 13 | MATHLIB | Five methods and pinned candidate inspection below. |
| 14 | JUNK DEF | No definition. |
| 15 | EXISTS LEMMA | No existential conclusion. |
| 16 | SHOW vs CHANGE | Neither occurs. |
| 17 | PUSH_NEG | No negation tactic. |
| 18 | GENERALISE | Arbitrary index type and arbitrary natural-valued finite supports; no unnecessary instances. |
| 19 | INEQUALITY | Only proof-local support containment, supplied by exact library lemmas. |
| 20 | NORMAL-FORM | Product equation orientation matches its coefficient-level caller. |
| 21 | SYNTAX-GEN | hasseCoeff definition inspected; ordinary product of natural binomial coefficients. |
| 22 | IMPORT-FANOUT | Existing imported support-product API suffices; imports unchanged. |
| 23 | CASTS | Natural-valued identity has no casts. |
| 24 | INSTANCE-NAME | No instance declaration. |

## Signature width and inequality tables

Measured Unicode codepoint lengths; signature unchanged.

| Signature line | Before | After | Next unit | Arithmetic/action |
|---|---:|---:|---|---|
| 152: private lemma, parameters, colon | 58 | 58 | Left side and equality, 49 characters | 58 + 1 + 49 = 108 > 100; ok. |
| 153: left side and equality | 53 | 53 | Right side and := by, 61 characters | 53 + 1 + 61 = 115 > 100; ok. |
| 154: right side and := by | 67 | 67 | None | Complete signature; ok. |

| Scope | Relation | Assessment |
|---|---|---|
| Statement | Equality of products | No strictness or inequality-direction choice. |
| hd | d.support ⊆ d.support ∪ e.support | Exact Finset.subset_union_left; retained twice-used fact. |
| e support | e.support ⊆ d.support ∪ e.support | Exact Finset.subset_union_right. |
| sum support | (d + e).support ⊆ d.support ∪ e.support | Exact Finsupp.support_add; no new assumptions. |

## Five-method mathlib search

| Method | Query/scope | Result |
|---|---|---|
| A Lean-Finder | product of multi-index binomial coefficients composition Hasse derivative; limit 3 | Polynomial.hasseDeriv_comp, apply and mul. Composition is the univariate analogue; no direct multivariate coefficient replacement returned. |
| B Loogle | "prod_of_support_subset"; limit 5 | Finsupp.prod_of_support_subset and dependent DFinsupp variant. Existing proof uses the appropriate one. |
| C LeanSearch | multivariate binomial coefficients product composition identity; limit 3 | HTTP 500; unavailable, not negative search evidence. |
| D Pinned sources/project | prod_congr, prod_mul, prod_add_index, support-extension APIs; hasseCoeff_mul_hasseCoeff uses | Inspected types/proofs in Finsupp/Basic and Polynomial/HasseDeriv; single project caller is hasseDeriv_hasseDeriv. |
| E Local MCP | prod_of_support_subset; limit 10 | Both Finsupp and DFinsupp declarations found; index unavailable but source matching worked. |

Evidence: `/private/tmp/roth-hasseCoeff_mul_hasseCoeff-native-search.json`
and `/private/tmp/roth-hasseCoeff_mul_hasseCoeff-local.json`.
Pinned `Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:57` extends a product
provided zero inputs map to one. All four occurrences use choose-zero-right,
so extending to the union of d and e supports is valid. `prod_congr` (183)
and `prod_mul` (327) alone require a shared finsupp support; the original
products do not have one. `prod_congr_of_eq_on_union` (192) compares two
products, whereas this goal compares products of two products. It does not
remove the need to align supports. `prod_add_index` (348) and its primed
version (364) require multiplicativity in the input, which binomial
coefficients do not satisfy. The existing support extension followed by
Finset.prod_mul_distrib and Finset.prod_congr is appropriate.
`Polynomial.hasseDeriv_comp` (154) proves an identity of univariate linear
maps, not this project-specific multivariate natural coefficient equation;
its proof confirms the underlying combinatorial approach.

Replacement checklist: actual definition and candidate types inspected;
searched both multivariate composition and generic support-product
formulations; retained the existing mathlib composition rather than adding
another abstraction. No hidden predicate or topological separation hypothesis.
No exact replacement was found in the inspected results; failed LeanSearch
is not counted as establishing absence.

## Parameters, generalisation, inversion and literature

| Parameter/context | Assessment |
|---|---|
| σ : Type* | Arbitrary index type; no finite or decidable-equality assumption in signature. |
| f : σ →₀ ℕ | Arbitrary remaining multi-index; zero allowed. |
| d, e : σ →₀ ℕ | Arbitrary derivative multi-indices; no disjointness, positivity or ordering assumptions. |
| R and CommSemiring R | Absent from elaborated type, confirmed by #check. |
| classical | Local proof support operations require decidable equality; no public assumption added. |

The indexed product of the previous scalar choose identity is the natural
statement. Inverting the proof exposes a general principle already supplied
by support extension and finite product congruence, not a missing theorem.
A finite-variable full-product formulation would add a needless Fintype
constraint. Allowing an arbitrary function f in place of its finite support
would require redesigning hasseCoeff's upper argument and addition interfaces;
that substantive definition/API proposal remains unapplied, consistent with
the earlier hasseCoeff audit. Generalized integer binomials would change the
underlying mathematical object and are outside routine cleanup.

Local source `.mathlib-quality/references/clean.tex:571–588` gives the Hasse
composition identity in the proof of the index-of-derivative lemma. This
private result supplies its coefficient-level combinatorial factor.
Freshly inspected [NIST DLMF §26.3, equation 26.3.1](https://dlmf.nist.gov/26.3.E1)
gives binomial symmetry and the factorial formula. Inference: coordinatewise,
both products equal (fᵢ+dᵢ+eᵢ)!/(fᵢ! dᵢ! eᵢ!), and multiplying those equalities
over the union of d and e supports gives this lemma. Outside that union all
factors are one. DLMF is not claimed to state this exact multivariate identity.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | Proof has required support transformations before final exact. |
| 1.2 by rfl | Binomial product identity is not definitional. |
| 1.3 rw + exact | rw aligns four supports; terminal congruence handles pointwise identity. |
| 1.4 simp + exact | Initial simp only unfolds the local coefficient definition deliberately. |
| 1.5 trailing rfl | rfl is the same-finset argument of product congruence, not redundant trailing tactic. |
| 1.6 constructor chain | None. |
| 1.7 apply + exact | None. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | Membership-discarding lambdas still pass necessary arguments; no removable eta wrapper. |
| 1.10 single-use have | hd used twice, retained. |
| 1.11 apply + intro | None. |
| 1.12 redundant show | None. |
| 1.13 have projections | None. |
| 1.14 merge rw | All dependent support rewrites already share one rw. |
| 1.15 terminal simp only | Applied: terminal simpa now uses ordinary simp with reverse associativity. |
| 1.16 nonterminal simp | Initial simp only retained for precise unfolding before support rewrites. |
| 1.17 dot notation | Free generic support arguments are clearer in existing applications. |
| 1.18 `<\|` | Existing explicit applications need no extra grouping. |
| 1.19 push Not | None. |
| 1.20 trivial existential | None. |
| 2.1 grind | Explicit support extension and named scalar identity directly solve the mathematical steps. |
| 2.2 delete before grind | No grind. |
| 2.3 simpa consolidation | Removed explicit Finsupp.add_apply and only from final transport. |
| 2.4 fun_prop | No function-property goal. |
| 2.5 positivity | No positivity goal. |
| 2.6 gcongr | Equality, not monotonicity; product congruence already exact. |
| 2.7 lia/omega | No arithmetic side goal remains after named scalar identity. |
| 2.8 aesop | Support alignment requires intentional choice of union; named APIs already close proof. |
| 2.9 norm_num/norm_cast | Symbolic binomial products with no casts. |
| 2.10 decide/kernel | Symbolic multi-indices; not a closed decision problem. |
| 2.11 field_simp/ring | No denominators in Lean statement; ring cannot prove choose identity or align supports. |
| 2.12 linear_combination | No polynomial equation combination. |
| 2.13 wlog | No case symmetry reduction needed. |
| 2.14 calc | Existing one-chain support normalization is concise; no intermediate conceptual equality needed. |
| 2.15 `<;>` | No parallel goals to distribute over. |
| 3.1 erw/rw | No coercion-sensitive rewrite. |
| 3.2 fun_prop | No analytic automation. |
| 3.3 omega/lia | Neither occurs. |
| 3.4 rcases rfl | No destructuring. |
| 3.5 automation attributes | None added or changed. |
| 3.6 simp_all | No hypothesis saturation needed. |
| 3.7 maxHeartbeats | None introduced or present. |

Strategy reflection: preserve the finite-support argument because candidate
APIs do not subsume its mixed products without equivalent support bookkeeping.
The focused simplification passed on the first isolated attempt. The probe
copies only the source prefix followed by the edited target: neither the
original target proof nor downstream project results are available to it.
No broad automation failure or unrun alternative is claimed as measured evidence.
`/private/tmp/roth-hasseCoeff_mul_hasseCoeff-probe.log` records success=true,
timed_out=false, original elaborated type, and exactly propext,
Classical.choice and Quot.sound. Bridge shutdown emitted an asynchronous
transport warning after the successful response, with process exit 0.

## Validation gates

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: lake build Roth.HasseDeriv, exit 0,1430 jobs (14s); /private/tmp/roth-hasseCoeff_mul_hasseCoeff-module-build.log. |
| Fresh whole-file LSP | PASS: exit 0; success=true,partial=false,timed_out=false,failed_dependencies=[]; zero errors, existing header warning only. /private/tmp/roth-hasseCoeff_mul_hasseCoeff-postedit-diagnostics.json. |
| Proof/type/axioms | PASS: isolated prefix-only candidate succeeded; original type and standard axioms only. |
| definition_protected | PASS: no definition changed. |
| theorem_statement_protected | PASS: byte-identical signature. |
| structure_gate | PASS: proof-local syntax/simplification only. |
| naming_gate | PASS: existing private name preserved. |
| line_packing_gate | PASS: signature widths 58/53/67; packing arithmetic above. |
| inequality_orientation_gate | PASS: standard support inclusions, no new hypothesis. |
| Scoped diff | PASS: byte-identical prefix/suffix and signature; git diff --check exit 0. |
| Dependent closure | PASS: orchestrator full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs), both exit 0. Logs `/private/tmp/roth-hasseCoeff_mul_hasseCoeff-build.log` and `/private/tmp/roth-hasseCoeff_mul_hasseCoeff-leaneval.log`. |

No sorry, new axiom, native_decide, option, import, version, mathematical
statement, definition, visibility or project structure changed. Existing header
warning remains deferred for ownership/license information.

## Phase 4 checklist

- [x] Step 1: inherited workflow/reference knowledge and target context reviewed.
- [x] Step 2: all 24 audit items assessed.
- [x] Step 2.5: five searches, candidate inspection and service failure disclosed.
- [x] Step 2.6: parameters, generalisation, inversion and local/public literature.
- [x] Step 2.7: full signature-width table.
- [x] Step 2.8: inequality scan.
- [x] Step 3: all 42 golfing rules considered.
- [x] Step 4: isolated edited proof tested and strategy reflection recorded.
- [x] Step 5a: module and complete fresh diagnostics passed.
- [x] Step 5b: protection, naming, packing and scoped-diff gates passed.
- [x] Step 6a: substantive definition-generalization proposal remains unapplied; no rename queue.

Parent owns dependent validation, shared logs, commit/push and file-wide phases.
