# Cleanup audit: `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`

Date: 2026-10-15 (America/Chicago). Baseline: pushed `d20b6d5`.
Target: public theorem at `Roth/HasseDeriv.lean:182`.
Decision: inline the single-use `h1` into the composition rewrite and use `↦`
for its lambda. The proof still occupies three lines. Its statement, name,
visibility, docstring and source citation are unchanged.

## Workflow and 24 audit items

Dedicated Phase 4 worker using inherited mathlib-quality/lean4 references.
Parent supplied native remote searches. Native local search returned source
matches with index unavailable. As the native proof server's missing `lake`
PATH had already been established, proof execution and diagnostics used the
verified direct-client bridge. No native proof-tool retry or configuration
change was needed. Optional ask_chatgpt_math skipped.

| # | Item | Disposition |
|---|---|---|
| 1 | LINT | Module and complete fresh diagnostics passed; existing header warning only. |
| 2 | HAVE SCAN | Single-use h1 inlined as a typed proof in rw. |
| 3 | SET_OPTION | None present or added. |
| 4 | SIMP SQUEEZE | Existing terminal simp proves each binomial equals one; retained. |
| 5 | NAMING | Repeated derivative name and of_disjoint accurately describe the specialization. |
| 6 | LINE PACKING | Signature and proof within 100 columns; table below. |
| 7 | BY PLACEMENT | by stays on conclusion line. |
| 8 | FORMAT | One wrapped rw with an explicit inline coefficient identity; lambda uses ↦. |
| 9 | COMMENTS | No proof comments; source citation preserved. |
| 10 | DOCSTRING | Explains disjoint supports and disappearance of the binomial factor. |
| 11 | VISIBILITY | Public; directly used by Roth.Separation. |
| 12 | STRUCTURE | Three-line proof remains local; no helper or declaration moved. |
| 13 | MATHLIB | Five methods and candidate assessment below. |
| 14 | JUNK DEF | No definition. |
| 15 | EXISTS LEMMA | No existential conclusion. |
| 16 | SHOW vs CHANGE | Typed show supplies the rewrite equality without a named local have. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Arbitrary index type, commutative semiring and polynomial; no extra characteristic restriction. |
| 19 | INEQUALITY | Equality statement; no bound to weaken. |
| 20 | NORMAL-FORM | Nested application reduces to addition of disjoint derivative orders. |
| 21 | SYNTAX-GEN | hasseCoeff product and hasseDeriv definitions inspected, including predecessor composition theorem. |
| 22 | IMPORT-FANOUT | Existing finite-product and support APIs suffice; no imports added. |
| 23 | CASTS | Nat.cast_one and one_smul directly eliminate the scalar factor. |
| 24 | INSTANCE-NAME | No instance declaration. |

## Signature width and inequality tables

Lengths count Unicode codepoints. The complete signature is unchanged.

| Signature line | Before | After | Next unit | Arithmetic/action |
|---|---:|---:|---|---|
| 182: theorem name, orders and disjointness | 91 | 91 | Polynomial binder, 22 characters | 91 + 1 + 22 = 114 > 100; ok. |
| 183: polynomial binder, conclusion and := by | 87 | 87 | None | Complete signature; ok. |

Final proof-line widths are 63, 36 and 96. The typed inline proof remains
visibly separate from the composition identity and final scalar reductions.

| Scope | Relation | Assessment |
|---|---|---|
| Statement | Equality under support disjointness | No strict inequality or orientation choice. |
| Proof | Coefficient factor equals one | Exact equality, not a weakened bound. |

## Five-method mathlib search

| Method | Query/scope | Result |
|---|---|---|
| A Lean-Finder | Hasse derivatives with disjoint multi-index supports compose without binomial coefficient; limit 3 | Polynomial.hasseDeriv_comp, Polynomial.hasseDeriv_mul, LaurentSeries.hasseDeriv_comp_coeff. |
| B Loogle | "hasseDeriv_comp"; limit 5 | Polynomial.hasseDeriv_comp and LaurentSeries.hasseDeriv_comp/comp_coeff. |
| C LeanSearch | Same natural-language disjoint-support query; limit 3 | HTTP 500; unavailable, not negative evidence. |
| D Pinned sources/project | Composition, disjoint_left, prod_eq_one and target usages | Inspected polynomial/series analogues, finite-product/support APIs and Roth.Separation caller. |
| E Native local search | prod_eq_one; limit 5 | Finset, DFinsupp, Fintype, List and Multiset variants; index unavailable, source matches returned. |

Remote evidence: `/private/tmp/roth-hasseDeriv_hasseDeriv_of_disjoint-native-search.json`.
Pinned `Mathlib/Algebra/Polynomial/HasseDeriv.lean:154` concerns a single
natural derivative order and univariate linear maps. The Laurent-series
composition results at `Mathlib/RingTheory/LaurentSeries.lean:156` and `:165`
also use single natural orders, with integer-indexed series coefficients.
Neither directly replaces this finite-support multivariate specialization.
The product rule returned by Finder concerns differentiation of a product,
not nested derivative composition. No exact replacement was identified among
these candidates; the unavailable search service establishes no absence.

`Finset.prod_eq_one` at
`Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean:108` matches the expanded
hasseCoeff definition directly. `Finset.disjoint_left` at
`Mathlib/Data/Finset/Disjoint.lean:47` turns membership in d.support into
nonmembership in e.support; `Finsupp.notMem_support_iff` then supplies e i = 0.
The existing simp uses this equality to reduce the binomial to choose-self.
These are the appropriate existing APIs. The disjointness projection alias
also exists, but the existing explicit projection chain is short and clear.

Replacement checklist: inspected actual definitions and candidate types,
searched composition and disjoint-specialization formulations, and retained
the general local composition theorem as the mathematical input. The caller
at `Roth/Separation.lean:218` rewrites backwards with this exact theorem to
separate orders supported on some-variables and the distinguished none-variable.
The public specialization therefore serves a concrete downstream use.

## Parameters, generalisation, inversion and literature

| Parameter/context | Assessment |
|---|---|
| σ : Type* | Arbitrary variable type, without Fintype or DecidableEq assumptions. |
| R : Type*, CommSemiring R | Matches the existing multivariate polynomial and derivative interface. |
| d, e : σ →₀ ℕ | Arbitrary finite-support derivative orders, including zero. |
| h : Disjoint d.support e.support | Used precisely to make each binomial coefficient one. |
| P : MvPolynomial σ R | Arbitrary polynomial, including zero. |
| Characteristic/nontriviality | No restriction; no division or nonzero scalar required. |

Inverting the proof isolates the coefficient-equals-one assertion; it is used
once and can be inserted directly in rw. A standalone coefficient theorem
could be a future API extension if additional callers appear, but is not
needed here and is not introduced. Replacing support disjointness by an
assumption that the coefficient equals one would alter the public statement
and obscure this caller-facing specialization. The preceding composition
theorem already handles overlapping orders with the correct scalar. Dropping
the hypothesis while retaining the scalar-free conclusion is not valid in
general. Weakening CommSemiring would require changing the underlying
multivariate derivative interface, beyond routine proof cleanup. No substantive
statement, definition or structure proposal is applied.

Local `.mathlib-quality/references/clean.tex:571–588` gives the composition
identity in the proof of index-of-derivative. Freshly inspected
[ECCC report 2026/032, Lemma 2.7(3)](https://eccc.weizmann.ac.il/report/2026/032/download/)
states the multivariate iteration identity over fields. The disjoint-support
specialization here follows from that formula because each coordinate's
binomial coefficient is one; this specialization is an inference from the
formula, not a separately quoted claim from the report. The Lean statement
works over arbitrary commutative semirings and finite-support variable indices.

## All 42 golfing rules

| Rule | Disposition |
|---|---|
| 1.1 by exact | Requires composition rewrite and scalar normalization. |
| 1.2 by rfl | Composition identity is not definitional. |
| 1.3 rw + exact | No trailing exact. |
| 1.4 simp + exact | None. |
| 1.5 trailing rfl | None. |
| 1.6 constructor chain | None. |
| 1.7 apply + exact | None. |
| 1.8 by_contra + push_neg | None. |
| 1.9 eta reduction | Lambda uses both bound arguments in the support calculation; not eta-reducible. |
| 1.10 single-use have | Applied: h1 inlined into rw as a typed proof. |
| 1.11 apply + intro | None. |
| 1.12 redundant show | Typed show is necessary to identify the hasseCoeff equality used by rw. |
| 1.13 have projections | No local have remains. |
| 1.14 merge rw | One rw chain already contains composition and scalar reductions. |
| 1.15 terminal simp only | Original terminal simp is already unrestricted; no simp only to shorten. |
| 1.16 nonterminal simp | Inner simp closes its factor goal. |
| 1.17 dot notation | Existing projection chain directly exposes support/disjointness conversions; retained. |
| 1.18 `<\|` | No nested application needing regrouping. |
| 1.19 push Not | None. |
| 1.20 trivial existential | None. |
| 2.1 grind | Product identity and named composition theorem solve the goal directly. |
| 2.2 delete before grind | No grind. |
| 2.3 simpa consolidation | Existing three-line rw retains all exact inputs without extra normalization search. |
| 2.4 fun_prop | No function-property goal. |
| 2.5 positivity | No positivity goal. |
| 2.6 gcongr | Equality specialization, not monotonicity. |
| 2.7 lia/omega | Symbolic binomial/product identity, not linear arithmetic. |
| 2.8 aesop | Explicit product-equals-one proof already closes each factor with simp. |
| 2.9 norm_num/norm_cast | Nat.cast_one is the only cast reduction needed. |
| 2.10 decide/kernel | Symbolic theorem with arbitrary polynomials. |
| 2.11 field_simp/ring | No division; ring does not supply support-disjointness facts. |
| 2.12 linear_combination | No linear combination of polynomial hypotheses. |
| 2.13 wlog | No symmetry case split required. |
| 2.14 calc | Three-line rewrite already displays the mathematical dependency. |
| 2.15 `<;>` | No parallel goals. |
| 3.1 erw/rw | No coercion mismatch; rw succeeds. |
| 3.2 fun_prop | No analytic automation. |
| 3.3 omega/lia | Neither occurs. |
| 3.4 rcases rfl | No destructuring. |
| 3.5 automation attributes | No attributes added or removed. |
| 3.6 simp_all | Explicit support fact suffices; no context saturation needed. |
| 3.7 maxHeartbeats | None introduced or present. |

Strategy reflection: the isolated candidate inlined the coefficient proof
into the existing rw, succeeded immediately, and retained the same mathematical
steps. Its final scalar rewrites were then packed onto the preceding line,
keeping three proof lines within 100 columns. The prefix-only scratch module
contains earlier definitions and results but excludes this target and every
downstream declaration; there is no circular simp proof. No unmeasured
automation or performance improvement is claimed.

## Validation gates

| Gate | Result/evidence |
|---|---|
| lake_build_file | PASS: lake build Roth.HasseDeriv, exit 0, 1430 jobs; /private/tmp/roth-hasseDeriv_hasseDeriv_of_disjoint-module-build.log. |
| Fresh whole-file LSP | PASS: direct-client exit 0; success=true, partial=false, timed_out=false, failed_dependencies=[]; no errors, existing header warning only. /private/tmp/roth-hasseDeriv_hasseDeriv_of_disjoint-postedit-diagnostics.json. |
| Proof/type/axioms | PASS: prefix-only candidate, exit 0, success=true, timed_out=false; exact type and only propext, Classical.choice, Quot.sound. /private/tmp/roth-disjoint-probe.log. |
| definition_protected | PASS: comparison confirms all text outside target theorem unchanged. |
| theorem_statement_protected | PASS: target signature before := by byte-identical. |
| structure_gate | PASS: proof-only edit, no declaration additions/removals/moves. |
| naming_gate | PASS: public name unchanged; local single-use h1 eliminated. |
| line_packing_gate | PASS: widths and arithmetic above. |
| inequality_orientation_gate | PASS: equality only. |
| Scoped diff | PASS: before/after target boundaries and signatures checked; git diff --check exit 0. |
| Dependent closure | PASS: orchestrator full `lake build` (2586 jobs) and separate `lake build Roth.LeanEval` (2585 jobs), both exit 0. Logs `/private/tmp/roth-hasseDeriv_hasseDeriv_of_disjoint-build.log` and `/private/tmp/roth-hasseDeriv_hasseDeriv_of_disjoint-leaneval.log`. |

The bridge emitted asynchronous transport shutdown warnings but returned
complete successful Lean results and process exit 0. These warnings are not
Lean proof errors. Module and LSP processes are finished; no probes remain
active. No sorry, new axiom, native_decide, option, import, version,
mathematical statement, definition, visibility or project structure changed.
Existing header warning remains deferred for ownership/license information.

## Phase 4 checklist

- [x] Step 1: inherited references and target context reviewed.
- [x] Step 2: all 24 audit items assessed.
- [x] Step 2.5: five searches, pinned candidates and unavailable service disclosed.
- [x] Step 2.6: parameters, generalisation, inversion and local/public literature.
- [x] Step 2.7: complete signature-width table.
- [x] Step 2.8: inequality scan.
- [x] Step 3: all 42 golfing rules considered.
- [x] Step 4: isolated inline proof tested and saved, with strategy reflection.
- [x] Step 5a: module and complete fresh diagnostics passed.
- [x] Step 5b: protection, naming, packing and scoped-diff gates.
- [x] Step 6a: no applied substantive proposal or rename queue.

Parent owns dependent validation, shared logs, commit/push and file-wide phases.
Work stops here for the requested session handover; no seventeenth declaration
was started by this worker.
