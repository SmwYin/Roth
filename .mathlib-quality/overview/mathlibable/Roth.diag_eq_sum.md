# `Roth.diag_eq_sum` — declaration 91/293

**BORDERLINE-needs-human.** The expansion is a verified trivial-simp specialization of evaluation. Its reusable API value, after generalizing coefficients, needs an upstream packaging decision. This is a completed read-only assessment; verification unresolved list is empty. Production, pins, Git and progress are unchanged; root acceptance is pending.

## Phase 0 — baseline

Freshly matched all17 source/pin hashes against the shared successful `lake build` baseline (2467 jobs, exit0). Target resolves at `Roth/CoeffNorm.lean:164`; theorem without placeholders. Full declaring module and both callers were read. [input-hash-check.json](../evidence/Roth.diag_eq_sum/input-hash-check.json) [inputs.json](../evidence/Roth.diag_eq_sum/inputs.json) [baseline-build.txt](../evidence/Roth.diag_eq_sum/baseline-build.txt) [source-module.lean.txt](../evidence/Roth.diag_eq_sum/source-module.lean.txt)

## Phase 1 — comprehend

For a polynomial P in any variable set with integer coefficients, identifying all variables with X sends the term aₖXᵏ to aₖX^|k|. Summing these terms gives the univariate polynomial; distinct exponents with equal total degree may merge. No assumption that coefficients avoid cancellation is made.

Full native type (pretty-printer resolves `monomial` in `Polynomial`):

```lean
∀ {σ : Type u_1} (P : MvPolynomial σ ℤ),
  Roth.diag P = ∑ k ∈ P.support, (monomial (Finsupp.degree k)) (P.coeff k)
```

Parameters are σ (arbitrary universe-polymorphic variable type) and P (essential input). There are no instance hypotheses on σ and no degree, nonzero or finiteness hypotheses. Proof unfolds `diag`, then `aeval`, invokes support expansion `eval₂_eq`, and normalizes the constant-X product into the monomial of total degree. The only project dependency is `Roth.diag`. [native-type.json](../evidence/Roth.diag_eq_sum/native-type.json) [native-original-executed.lean.txt](../evidence/Roth.diag_eq_sum/native-original-executed.lean.txt) [native-original-success.json](../evidence/Roth.diag_eq_sum/native-original-success.json)

## Phase 2 — preliminary classification

SMALL: helper expansion, no new structure, named classical theorem or project main result. One-line definition test n/a: theorem. Its shared name has actual API value for two same-file callers, but theorem length itself is not a verdict factor.

## Phase 3 — exhaustive literature

Three distinct general queries and every named channel ran. ChatGPT math channel is n/a: `ask_chatgpt_math` unavailable. Local clean.tex lines1444–1461 explicitly discuss replacing all xᵢ by x and bounding merged coefficients; that is the downstream mathematical purpose. [local-literature.txt](../evidence/Roth.diag_eq_sum/local-literature.txt) [local-literature-source.json](../evidence/Roth.diag_eq_sum/local-literature-source.json)

| Receipt | Exact query | Result / interpretation |
|---|---|---|
| 0 | `multivariate polynomial diagonal substitution total degree sum monomials` | Search returned primary teaching/computational references defining total degree as exponent sum; no named separate diagonal expansion theorem. [receipt](../evidence/Roth.diag_eq_sum/web-0.json) |
| 1 | `polynomial ring universal property evaluation arbitrary commutative semiring` | Search returned primary university commutative-algebra notes and semiring universal-property references. [receipt](../evidence/Roth.diag_eq_sum/web-1.json) |
| 2 | `diagonal specialization polynomial sum homogeneous components` | Search connected diagonal specialization with homogeneous components; the target expansion is the ordinary substitution expansion. [receipt](../evidence/Roth.diag_eq_sum/web-2.json) |
| 3 | `site:ncatlab.org/nlab polynomial ring universal property` | nLab search identifies polynomial rings as free commutative algebras; abstraction concerns evaluation rather than novel diagonal content. [receipt](../evidence/Roth.diag_eq_sum/web-3.json) |
| 4 | `site:ncatlab.org polynomial algebra diagonal substitution` | nCatLab domain search found categorical polynomial/free-algebra context; no separate diagonal-sum API. [receipt](../evidence/Roth.diag_eq_sum/web-4.json) |
| 5 | `site:stacks.math.columbia.edu polynomial algebra evaluation homomorphism` | Stacks search gives polynomial-ring universal-property context, without a standalone diagonal coefficient expansion. [receipt](../evidence/Roth.diag_eq_sum/web-5.json) |
| 6 | `site:mathoverflow.net polynomial diagonal specialization total degree` | MathOverflow results concern specializations and diagonals in differing senses; none identified the exact elementary law. [receipt](../evidence/Roth.diag_eq_sum/web-6.json) |
| 7 | `site:arxiv.org polynomial diagonal specialization after:2021-10-27 before:2026-10-28` | Recent arXiv window produced 2609.10609 using diagonal specialization for a multivariate polynomial; applications do not change the elementary evaluation formula. [receipt](../evidence/Roth.diag_eq_sum/web-7.json) |
| 8 | `site:ncatlab.org/nlab free commutative semiring polynomial evaluation` | Supplementary search in the current, standard, or abstract formulation. Related results supply context; no new exact diagonal expansion theorem identified. [receipt](../evidence/Roth.diag_eq_sum/web-8.json) |
| 9 | `site:ncatlab.org/nlab total degree polynomial` | Supplementary search in the current, standard, or abstract formulation. Related results supply context; no new exact diagonal expansion theorem identified. [receipt](../evidence/Roth.diag_eq_sum/web-9.json) |
| 10 | `site:ncatlab.org/ncatlab polynomial universal property` | Supplementary search in the current, standard, or abstract formulation. Related results supply context; no new exact diagonal expansion theorem identified. [receipt](../evidence/Roth.diag_eq_sum/web-10.json) |
| 11 | `site:ncatlab.org/ncatlab monoid algebra` | Supplementary search in the current, standard, or abstract formulation. Related results supply context; no new exact diagonal expansion theorem identified. [receipt](../evidence/Roth.diag_eq_sum/web-11.json) |
| 12 | `site:stacks.math.columbia.edu polynomial ring universal property evaluation` | Supplementary search in the current, standard, or abstract formulation. Related results supply context; no new exact diagonal expansion theorem identified. [receipt](../evidence/Roth.diag_eq_sum/web-12.json) |
| 13 | `site:stacks.math.columbia.edu multivariate polynomial diagonal substitution` | Supplementary search in the current, standard, or abstract formulation. Related results supply context; no new exact diagonal expansion theorem identified. [receipt](../evidence/Roth.diag_eq_sum/web-13.json) |
| 14 | `site:mathoverflow.net polynomial evaluation universal property semiring` | Supplementary search in the current, standard, or abstract formulation. Related results supply context; no new exact diagonal expansion theorem identified. [receipt](../evidence/Roth.diag_eq_sum/web-14.json) |
| 15 | `site:mathoverflow.net multivariate polynomial all variables equal` | Supplementary search in the current, standard, or abstract formulation. Related results supply context; no new exact diagonal expansion theorem identified. [receipt](../evidence/Roth.diag_eq_sum/web-15.json) |
| 16 | `site:arxiv.org multivariate polynomial specialization all variables equal after:2021-10-27 before:2026-10-28` | Supplementary search in the current, standard, or abstract formulation. Related results supply context; no new exact diagonal expansion theorem identified. [receipt](../evidence/Roth.diag_eq_sum/web-16.json) |
| 17 | `site:arxiv.org commutative semiring polynomial universal property after:2021-10-27 before:2026-10-28` | Supplementary search in the current, standard, or abstract formulation. Related results supply context; no new exact diagonal expansion theorem identified. [receipt](../evidence/Roth.diag_eq_sum/web-17.json) |

Primary context: [nLab polynomial](https://ncatlab.org/nlab/show/polynomial) search identifies the free-algebra viewpoint (direct open failed due to unsupported XHTML); [Thiel's commutative-algebra notes](https://ulthiel.com/math/files/Commutative-Algebra.pdf) were returned for the polynomial universal property (direct fetch timed out). [Jiang, arXiv2609.10609](https://arxiv.org/abs/2609.10609), submitted2026-09-08, uses diagonal specialization in a recent application; its abstract confirms terminology rather than proving our formula. Stacks00EX was accessible but concerns spectra examples, so is not claimed as the universal-property proof. Exact multi-page open request/failures: [web-18.json](../evidence/Roth.diag_eq_sum/web-18.json).

The standard mathematical content is ordinary polynomial evaluation and its monomial expansion, with diagonal specialization as the constant valuation. Coefficient bases range from integers in the Roth application to commutative rings/semirings in universal-property formulations. The universal-property abstraction is already `aeval`/`eval₂`; recent applications do not require a new definition. Power-series coefficient-extraction “diagonal” and quadratic diagonal forms are different concepts and excluded. Search results do not prove absence of an upstream theorem. Web records store hashes/bytes, exact requests, titles/locators and original summaries only; all URL queries and oversized returned headings are omitted.

## Phase 4a — parameters and hypotheses

| Parameter | Generality / audit |
|---|---|
| σ : Type u | Already arbitrary, including empty/infinite types; finite supports suffice. No Fintype/DecidableEq parameter to drop. |
| P : MvPolynomial σ ℤ | Essential polynomial argument; ℤ coefficients can expand to arbitrary CommSemiring R. |
| diag | Existing parent signature fixes ℤ; generic claim is stated against aeval, not falsely described as dropping a target hypothesis. |
| Natural exponents / degree | Define ordinary polynomials and total degree; arbitrary additive exponents would change representation and need a separate monoid-algebra API. |

## Phase 4b — verified generality

STRICTLY NARROWER in coefficient representation: both `generic` and `existingExpansion` compiled in isolated mathlib-only code under `[CommSemiring R]`, with arbitrary σ. Generalized signature:

```lean
{σ R : Type*} [CommSemiring R] (P : MvPolynomial σ R) :
  MvPolynomial.aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P =
    ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k)
```

This is a mechanical expanded representation (CHEAP sequencing observation, never a verdict reason). No ring subtraction, field, characteristic, order, nontriviality or finite variable assumption is used. Generalized proof and specialization route: [native-raw-executed.lean.txt](../evidence/Roth.diag_eq_sum/native-raw-executed.lean.txt) [native-raw-success.json](../evidence/Roth.diag_eq_sum/native-raw-success.json). Arbitrary coefficient homomorphisms/valuations are already covered by `eval₂_eq` (verified native signature); retaining the monomial-degree RHS requires the constant-X valuation.

## Phase 4c — all nine modern-idiom rows

| Question | Assessment / concrete downstream consequences |
|---|---|
| Typeclasses | No new class; use existing CommSemiring R. |
| Filters/topology | n/a: finite algebraic identity. |
| Universal property | Already aeval; arbitrary valuation expansion is eval₂_eq. No new universal-property class. |
| Bundled substructures | n/a: no closure predicates; aeval is already an AlgHom. |
| Hierarchy weakening | Yes: integers expand to arbitrary CommSemiring coefficients; native generic compiled. |
| Higher categories | n/a: ordinary polynomial substitution has no higher coherence requirement. |
| Concrete index | σ is already arbitrary Type u; natural exponents define ordinary polynomials. General additive exponents change representation. |
| Concrete-via-abstract | Fires: after unfolding diag there is no integer-specific reasoning; generic CommSemiring proof compiled. Arbitrary valuation formula already exists as eval₂_eq. |
| False-generalization guard | CommSemiring preserves original substitution on specialization. Reject confusing substitution P(X,…,X) with power-series diagonal coefficient extraction or arbitrary images while retaining total-degree RHS. |

Concrete downstream benefit of CommSemiring coefficients: the same monomial expansion applies to ℕ, finite-characteristic coefficients and arbitrary commutative semirings, while both existing integer coefficient/degree estimates remain rewrites by specialization. A bundled total-degree map is a possible alternative representation, not a new verified existing replacement. No higher-level packaging is required to prove the formula. [generality.json](../evidence/Roth.diag_eq_sum/generality.json)

## Phase 4.5 — all six infrastructure risks

- Typeclass diamond: n/a: theorem; introduces no data, instances or coercions.
- Reducibility leak: n/a: theorem; introduces no data, instances or coercions.
- Noncanonical unfolding: n/a: theorem; introduces no data, instances or coercions.
- Instance priority: n/a: theorem; introduces no data, instances or coercions.
- Universes: n/a: theorem; introduces no data, instances or coercions.
- Coercion ambiguity: n/a: theorem; introduces no data, instances or coercions.

## Phase 4.6 — all five proof-strategy rows

| Question | Assessment |
|---|---|
| Topology | n/a: no topology. |
| Algebra inclusions | No ideals/submodules appear; rewriting support expansion is appropriate. |
| Sequences | n/a: no limits. |
| Universal property | aeval already uses polynomial universal property; rebuilding it would duplicate infrastructure. |
| Missing helpers | No required mathematical helper missing: eval₂_eq plus product-power and monomial identities suffice. Optional named diagonal expansion remains API-design question. |

Verdict: current finite-support normalization is idiomatic. Avoid induction over P or rebuilding a polynomial homomorphism. Optional naming is the issue, not unavailable proof infrastructure.

## Phase 5 — five actual mathlib methods on three forms

| Method | Actual results |
|---|---|
| lean_leanfinder | current: MvPolynomial.iterToSum, MvPolynomial.psum, matPolyEquiv_diagonal_X, MvPolynomial.supDegree_esymmAlgHomMonomial [raw](../evidence/Roth.diag_eq_sum/lean_leanfinder-current.json); standard: MvPolynomial.eval_eq', MvPolynomial.eval_eq, MvPolynomial.eval₂_eq', MvPolynomial.eval₂_eq [raw](../evidence/Roth.diag_eq_sum/lean_leanfinder-standard.json); abstract: MonoidAlgebra.mapDomain_single, AddMonoidAlgebra.mapDomain_single, MonoidAlgebra.mapRangeRingHom_single, MonoidAlgebra.mapRangeAlgHom_single [raw](../evidence/Roth.diag_eq_sum/lean_leanfinder-abstract.json) |
| lean_loogle | current: no items [raw](../evidence/Roth.diag_eq_sum/lean_loogle-current.json); standard: MvPolynomial.eval₂_sum, MvPolynomial.eval₂_eq', MvPolynomial.eval₂_eq [raw](../evidence/Roth.diag_eq_sum/lean_loogle-standard.json); abstract: MvPolynomial.eval₂_monomial, MvPolynomial.eval₂_mul_monomial [raw](../evidence/Roth.diag_eq_sum/lean_loogle-abstract.json) |
| lean_leansearch | current: MvPolynomial.homogeneousComponent_apply, MvPolynomial.sum_homogeneousComponent, MvPolynomial.eval_eq, MvPowerSeries.subst_monomial [raw](../evidence/Roth.diag_eq_sum/lean_leansearch-current.json); standard: MvPolynomial.eval₂_eq', MvPolynomial.eval_eq', MvPolynomial.eval₂_eq, MvPolynomial.eval_eq [raw](../evidence/Roth.diag_eq_sum/lean_leansearch-standard.json); abstract: Polynomial.mapAlgHom_monomial, MonoidAlgebra.mapRangeAlgHom_single, AddMonoidAlgebra.mapRangeAlgHom_single, Algebra.Generators.Hom.toAlgHom_monomial [raw](../evidence/Roth.diag_eq_sum/lean_leansearch-abstract.json) |
| lean_local_search | current: Roth.diag, IsClub.diag, MyNamespace.diag, SimplexCategory.diag [raw](../evidence/Roth.diag_eq_sum/lean_local_search-current.json); standard: eval, MvPolynomial.eval, MvPowerSeries.eval, Polynomial.eval [raw](../evidence/Roth.diag_eq_sum/lean_local_search-standard.json); abstract: Finsupp.mapDomain, MonoidAlgebra.mapDomain, SkewMonoidAlgebra.mapDomain, mapDomain_tsub [raw](../evidence/Roth.diag_eq_sum/lean_local_search-abstract.json) |
| rg source | Current diagonal/monomial form, standard eval/product-power form, and abstract mapDomain/lift form: [rg-current.json](../evidence/Roth.diag_eq_sum/rg-current.json), [rg-literature.json](../evidence/Roth.diag_eq_sum/rg-literature.json), [rg-abstract.json](../evidence/Roth.diag_eq_sum/rg-abstract.json). Full-name search: [rg-full-name.json](../evidence/Roth.diag_eq_sum/rg-full-name.json). |

External indices may differ from pinned revision; local unavailable index is not absence evidence. Positive pinned evidence is `MvPolynomial.eval₂_eq` and the normalization facts, all signatures checked natively and used in the isolated proof. Conclusion: found evaluation building blocks, not an established exact diagonal expansion theorem. This report makes no exhaustive-absence claim.

| Existing fact | Pinned path / role |
|---|---|
| MvPolynomial.eval₂_eq | Mathlib/Algebra/MvPolynomial/Eval.lean:72; rfl support expansion. |
| MvPolynomial.aeval_def | Same module; converts aeval to eval₂; needed explicitly by successful simpa. |
| Finset.prod_pow_eq_pow_sum | Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean:656; genuine power-product identity. |
| Finsupp.degree_apply | Mathlib/Data/Finsupp/Weight.lean:221; rfl exponent-sum notation. |
| Polynomial.algebraMap_eq | Mathlib/Algebra/Polynomial/AlgebraMap.lean:90; rfl canonical C map. |
| Polynomial.C_mul_X_pow_eq_monomial | Mathlib/Algebra/Polynomial/Basic.lean:658; genuine monomial identification. |

Pinned source archives/hashes: [mathlib-inputs.json](../evidence/Roth.diag_eq_sum/mathlib-inputs.json); exact native signatures and proof: [native-raw-success.json](../evidence/Roth.diag_eq_sum/native-raw-success.json). New assessment helpers are not counted as pre-existing mathlib calls.

## Phase 5.5 — statement shape

Normal forms: support sum of `Polynomial.monomial k.degree`, or support sum of `C a * X^(sum exponents)`. Existing eval₂_eq supplies the latter with a product before normalization. Monomial RHS is directly usable for coefficient and degree APIs; orientation RHS-expanded is appropriate. Syntactic alternatives actually attempted: raw aeval expansion and specialization of existing eval₂_eq via explicit `simpa only`; both now compile. P explicit is convenient for rewrites. No superfluous variables/typeclasses; σ is inferred from P and supports arbitrary universes. Overall RESTATE-BEFORE-SHIP if upstream: CommSemiring coefficients and aeval-based signature. Local fixed-parent statement is usable as written.

## Phase 6.0 — complete callers and inline audit

Internal use count excluding declaring file:0; external-to-file callers:0. Explicit same-file calls:2 (not conflated with the first count).

| Caller | Usage | Concrete refactor experiment |
|---|---|---|
| Roth.abs_coeff_diag_le, CoeffNorm.lean:176 | `rw [diag_eq_sum, Polynomial.finsetSum_coeff, …]` | Replace first rewrite by generic existingExpansion specialized to ℤ; full theorem replay compiled. |
| Roth.natDegree_diag_le, CoeffNorm.lean:185 | `rw [diag_eq_sum]` | Same specialized expansion, retain degree-of-sum proof; full theorem replay compiled. |

No equivalent diagonal expansion is re-derived inline elsewhere. Other eval₂ expansions and product-power rewrites concern other evaluations; no extra target caller inferred. [rg-callers.json](../evidence/Roth.diag_eq_sum/rg-callers.json) [rg-inline.json](../evidence/Roth.diag_eq_sum/rg-inline.json) [callers.json](../evidence/Roth.diag_eq_sum/callers.json).

Fresh audit of the canonical array generated directly from tracked JSON preserves private names and exact order: requested293, unique293, present293, values293; direct proof consumers exactly the two rows above. This is not a transitive kernel/simp dependency closure. [canonical-audit-array.lean.txt](../evidence/Roth.diag_eq_sum/canonical-audit-array.lean.txt) [canonical-order.json](../evidence/Roth.diag_eq_sum/canonical-order.json) [native-consumers-executed.lean.txt](../evidence/Roth.diag_eq_sum/native-consumers-executed.lean.txt) [native-consumers-success.json](../evidence/Roth.diag_eq_sum/native-consumers-success.json).

## Phase 6 — actual compositions and gate semantics

Attempt1: specialize `eval₂_eq` and normalize via product-power, degree, canonical coefficient map and monomial identity. The first attempted `simpa only` omitted aeval_def and failed (preserved rejected receipt); corrected proof succeeded. Attempt2: source-style `rw [aeval_def, eval₂_eq]; simp_rw […]` under CommSemiring succeeds independently. Both exact snippets are in raw accepted evidence.

There are six named existing facts in the explicit proof, not one existing diagonal lemma. Three (`eval₂_eq`, `aeval_def`, `degree_apply`) plus canonical coefficient-map normalization are definitional bridges; `prod_pow_eq_pow_sum` and `C_mul_X_pow_eq_monomial` are genuine identities. Even viewing those three core mathematical ingredients as a count of3 does not turn their nested sum-congruence normalization into a simple chained-call term. No compiled <=3 existing-call term was established. The named helper used by caller replays is newly proved evidence, not an existing replacement.

Composition classification: **trivial simp composition; Phase6b BORDERLINE**. The explicit command says a closing `simp [facts]` is borderline and the API value must be judged; `simpa only` over eval₂_eq has precisely that normalization character. NO-has-it would overstate exact specialization without the genuine product/monomial bridge. YES solely from syntactic normalization length would overstate the mathematical gap. Parent diag is NO-composable; the special ModeB re-aim gate for a NO-has-it parent therefore does not apply automatically. This assessment is independent of parent and sibling verdicts.

## Phase 7 — actionable verdict

**BORDERLINE-needs-human**, grounded in the explicit trivial-simp gate, not proof cost or unverified absence. A shared generic support-expansion theorem may be useful, but all mathematical infrastructure exists and the two consumers are local. Concrete upstream API questions:

1. Should mathlib expose the constant-X specialization of eval₂_eq as a named CommSemiring theorem with a monomial-sum RHS?
2. Should the canonical API use aeval directly, or a bundled map induced by total degree, with the diagonal expansion as its apply lemma?
3. For the two local callers, should this shared expansion remain a private/local helper if no upstream API is added?

If a named API is selected, propose the CommSemiring/aeval statement near Mathlib/Algebra/MvPolynomial/Eval.lean after coefficient-polynomial imports are reviewed; do not upstream the integer-only Roth spelling. If omitted upstream, keep a private shared helper in Roth/CoeffNorm.lean or inline the exact verified normalization at both listed callers. Neither change is authorized by this read-only assessment. Existing accepted YES groupings were freshly read, but no PR grouping/reviewer selection is applicable to this BORDERLINE verdict. [accepted-yes-grouping.json](../evidence/Roth.diag_eq_sum/accepted-yes-grouping.json)

## Phase 8 — verification and handoff

Three accepted exact native source/receipt sets: original target/type/axioms, isolated generic composition, full caller replays/canonical audit. All success=true, no errors/warnings; disk responses explicitly partial=false, completed virtual response has no partial flag; axioms only propext, Classical.choice, Quot.sound. Two rejected attempts are separately archived: first missing aeval_def type mismatch, second corrected proof with longLine warning. Neither is counted as success. [verification.json](../evidence/Roth.diag_eq_sum/verification.json)

Portable read-only validation checks current copy-manifest hashes/bytes (historical worker manifest never substitutes), sources/pins, native receipts and exact archived sources, all mandatory phases and searches, canonical293 exact name order/private handling, links and credential guard. [validate.py](../evidence/Roth.diag_eq_sum/validate.py). Root independently reviews before integrating. No user question or production edit is required to complete this assessment.
