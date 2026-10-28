# Roth.RSet — BORDERLINE-needs-human

The definition is a useful local name for nonzero integer polynomials in a coordinate-degree box with bounded naive coefficient height. No verified existing named mathlib definition covers the complete conjunction. Its degree component has a richer existing submodule representation, but that representation alone loses the coefficient bound and nonzero condition. Whether to upstream this particular intersection as a named set remains a design question; this completed read-only assessment requires no user interruption.

## Phase 0 — baseline

`Roth/Theta.lean:56`, public `def`, canonical index 179/293. All 985 lines of Theta were read, together with the source callers in MainLemma and dependency definitions in CoeffNorm, Index, and Box. The latest whole-project build succeeded (2467 jobs, 5.592 seconds); all 17 source/pin hashes freshly match the baseline. See [build](../evidence/Roth.RSet/separation-file-completion-2026-10-27.json), [fresh hashes](../evidence/Roth.RSet/source-hashes.json), and [entire module](../evidence/Roth.RSet/source-Theta.lean.txt). No production or pin changes were made.

## Phase 1 — mathematical content and exact type

For a real bound B and natural coordinate degree limits r, this is the set of nonzero polynomials over the integers whose degree in variable j is at most r(j), and every coefficient, cast to the reals, has absolute value at most B. Thus it is a bounded naive-height body with the origin deleted. The variables may be indexed by any type, including an infinite or empty type; finiteness becomes relevant for counting or the later index supremum, not for defining this set.

```lean
Roth.RSet : {σ : Type u_1} → ℝ → (σ → ℕ) → Set (MvPolynomial σ ℤ)
```

The exact body is `{R | R ≠ 0 ∧ (∀ j, degreeOf j R ≤ r j) ∧ ∀ d, |((R.coeff d : ℤ) : ℝ)| ≤ B}`. Although the surrounding section declares `[Fintype σ] [DecidableEq σ]`, neither occurs in the elaborated definition. There are no positivity assumptions on B or r. Native `#print` has no elision and native axioms are only `propext`, `Classical.choice`, `Quot.sound`; see [native type](../evidence/Roth.RSet/native-type.json) and [original native receipt](../evidence/Roth.RSet/rset179-original-receipt.json).

## Phase 2 — size and one-line test

BIG for workflow framing: a named mathematical set/concept, explicitly among the module's main definitions. The body has exactly one substantive line: ONE-LINER WITH-EXEMPTION.

| Exemption | Applies | Evidence |
|---|---|---|
| Avoid defeq abuse | No | Consumers unpack the conjunction directly; no sealed or specially controlled unfolding dependency was found. |
| Avoid typeclass diamonds | No | This produces a Set, installs no instance, and has no competing algebraic structure. |
| Semantic intent / stable API name | Yes | The docstring identifies source ℛ; `indexSet`, `index_le_Θ`, `sub_mem_RSet`, and auxiliary-polynomial existence statements repeatedly use the name. |

The exemption establishes a real project API, not a presumption of mathlib inclusion. Capitalization `RSet` follows source notation but does not establish an upstream name.

## Phase 3 — exhaustive literature

Exact requests and response fingerprints, status, locators and concise summaries are archived; full returned web bodies are not retained. [General searches](../evidence/Roth.RSet/web-0.json), [named namespaces](../evidence/Roth.RSet/web-1.json), [MO/recent searches](../evidence/Roth.RSet/web-2.json), [direct primary accesses](../evidence/Roth.RSet/web-primary.json), [explicit five-year query](../evidence/Roth.RSet/web-recent.json).

| Channel | Actual query or locator | Finding / limitation |
|---|---|---|
| General web, specific | integer multivariate polynomial bounded individual degrees coefficients height Roth auxiliary polynomial | Bounded degree and coefficient height are standard auxiliary-polynomial constraints; no independent universal RSet name. |
| General web, general | polynomial naive height maximum absolute coefficients multidegree bounded counting | Krick–Pardo–Sombra, §1.1.1, defines the size of a multivariate polynomial by the maximum absolute coefficient. |
| General web, alias | Roth lemma set polynomials R_m B r bounded height | Roth literature uses coefficient heights and block/coordinate degrees with varying notation. |
| ChatGPT mathematical MCP | n/a | `ask_chatgpt_math` unavailable in tool inventory; the other channels were all executed. |
| Local references | clean.tex lines 645–654 and grep for ℛ/height/absolute coefficient bounds | Exact ℛ definition: nonzero integer coefficients, separate degree bounds, coefficient absolute values at most B. Source additionally assumes m≥1, B≥1 and positive r. |
| nLab | site:ncatlab.org/nlab polynomial height bounded coefficients | Polynomial page gives free commutative algebra viewpoint, not this arithmetic body. Direct opening failed on XHTML content type; search excerpt available. |
| nCatLab | site:ncatlab.org/ncatlab polynomial height bounded coefficients | Returned off-namespace nLab material; no exact nCatLab hit. This is not evidence of absolute absence. |
| Stacks | site:stacks.math.columbia.edu polynomial height coefficients bounded; repeated polynomial/coefficients/degree query | Returned algebraic/geometry material, not naive integer coefficient boxes. Supplementary direct tag 00EP is unrelated glueing and is explicitly not evidence for this concept. |
| MathOverflow | site:mathoverflow.net polynomials bounded height multivariate coefficients | Q151556 discusses max-coefficient norms with individual degree bounds; Q108726 distinguishes projective height from the raw coefficient bound. Secondary context, not the primary basis of the definition. |
| Recent arXiv, 2021-10-27–2026-10-27 | explicit after:2021-10-27 before:2026-10-28 query plus multivariate bounded-height query | Dubickas–Sha 2409.08625 (2024), abstract lines 8–17, counts monic integer polynomials of fixed degree and bounded height. Primary direct access succeeded; univariate and monic rather than exact ℛ. |

Primary locators: [Krick–Pardo–Sombra §1.1.1](https://mate.dm.uba.ar/~krick/KrPaSo01.pdf) (search content returned; direct PDF fetch timed out), [Dubickas–Sha](https://arxiv.org/abs/2409.08625). The local source supplies the exact conjunction; the broader literature supplies naive coefficient height as the reusable concept. Variants include multihomogeneous forms, projective height, coefficient sup norm, and total rather than coordinate degree. They are not interchangeable. No claim that every source adopts a single most-general RSet definition is warranted.

## Phase 4a — parameters and hypotheses

| Item | Native form | Comparison / weakening |
|---|---|---|
| Variables σ | Arbitrary universe-polymorphic Type | Already broader than the source's m≥1 finite list. Neither finite nor decidable equality is captured. |
| Coefficients | ℤ, cast to ℝ before absolute value | Essential to this integer lattice family. Replacing ℤ by a normed ring defines a different family and changes counting / arithmetic consumers. |
| B | Any real | Source B≥1 is deliberately not required in the definition; relevant theorems supply it. Negative B gives the empty set. |
| r | σ→ℕ | Bounds can be zero and need not have finite support; source positive bounds are stronger. No binder can simply be dropped. |
| Nonzero | R≠0 | Essential for index bounds and auxiliary-polynomial existence; deleting it changes the set. |
| Degree bound | ∀j, degreeOf j R≤r j | Equivalent to support contained in the exponent box, not to totalDegree≤a scalar bound. |
| Coefficient bound | Every exponent d, including missing coefficients | Restricting to support without additional sign/nonzero analysis can change junk-value behavior. Keep this exact condition in bridges. |

## Phase 4b — generality result

Already general in the variable type and the bound parameters relative to the source. No mechanically droppable instance remains; native checks verify unrestricted σ. An abstract normed coefficient family or arbitrary support set is plausible API design, not a demonstrated one-edit generalization of the arithmetic development. No YES-but-generalise-first claim is made.

## Phase 4c — nine modern idiom checks

| # | Check | Result |
|---|---|---|
| 1 | Preambles as typeclasses | No: B and r are data, not structural laws. |
| 2 | Sequences to filters/topology | No limit or topological premise. |
| 3 | Construction to universal property | No: a constrained subset of an existing free algebra; free-algebra uniqueness would not encode its bounds. |
| 4 | Closure predicate to bundled structure | Partly: the degree-only condition is `restrictSupport ℤ {d | ∀j,d j≤r j}`, a submodule with basis, monotonicity, span and multiplication API. Full RSet excludes zero and has bounded coefficients, so it is not a submodule/subalgebra. |
| 5 | Weaken scalar structure | No instance on a varying scalar type to weaken. A generic normed-coefficient body would require a new abstraction and arithmetic specializations. |
| 6 | Higher categorical reformulation | No categorical operation occurs. |
| 7 | Concrete index to abstract group/monoid | σ is already arbitrary. Exponents ℕ describe ordinary polynomial monomials; arbitrary exponent monoids change the polynomial object. |
| 8 | Concrete-via-abstract diagnostic | The entire one-line body contains only nonzero, degree and coefficient conditions; after expanding ℤ→a normed coefficient ring its syntax can be imitated. However integer integrality is precisely the family used by callers, not an unused witness in a proof. The degree-only generic CommSemiring bridge was actually verified; no claim that all arithmetic consumers generalize follows. |
| 9 | False-generalization guard | Reject raw replacement by a submodule, total degree, projective height, or normOne: respectively loses nonzero/height, changes the box, loses scaling information, or strengthens the coefficient condition. |

The available rich representations fit together as follows. `MvPolynomial.restrictSupport` handles the degree condition exactly and has the strongest directly relevant algebraic API. With finite support of r, coefficient arrays on a finite exponent box and `Finset.finsupp` add finite enumeration/cardinality API, at the price of an extra finiteness premise and bridges. The native arbitrary-σ set cannot globally be replaced by that finite construction. `Polynomial.supNorm` supplies the exact max-coefficient numerical concept in one variable, but is not a multivariate polynomial API. `Analysis.Normed.Lp.Finsupp` explicitly has a TODO for L∞ and takes finite real p, so it does not provide an existing WithLp∞ Finsupp norm. `Height.mulHeight` is scaling invariant/projective; e.g. a nonzero constant N has projective height one while its coefficient absolute value is |N|. None is a verified complete replacement.

## Phase 4.5 — six infrastructure risks

| Risk | Level | Rationale |
|---|---|---|
| Typeclass diamond | NONE | A Set-valued definition installs no algebra, norm or order instance; native signature has no inherited Fintype/DecidableEq instance paths. |
| Reducibility leak | LOW | Ordinary semireducible def with a small conjunction; consumers rely on transparent membership, but no reducible attribute or costly recursive computation is introduced. |
| Noncanonical unfolding | LOW | Membership unfolds to a fixed triple, and callers project `.1`, `.2.1`, `.2.2`. Changing its representation would require bridge lemmas or caller rewrites; the existing spelling is predictable. |
| Instance priority collision | NONE | Not an instance and no priority or search rule is registered. |
| Universe polymorphism | NONE | Native `{σ : Type u_1}` is preserved; ℤ/ℝ live in fixed universes without restricting σ. |
| Coercion ambiguity | LOW | Existing integer-to-real cast and Set membership only; no new CoeFun/CoeSort path. Casts should remain explicit when rewriting bounds. |

Overall LOW. This is not an infrastructure objection; the unresolved issue is the right public abstraction.

## Phase 4.6 — five proof strategy checks

| # | Check | Answer / alternative |
|---|---|---|
| 1 | ε–δ instead of filters | No: no proof or topology. |
| 2 | Element arguments instead of submodule inclusion | Degree component can use restrictSupport. Complete set has no module closure; bundling the whole body as a submodule is invalid. |
| 3 | Sequences instead of nets | No convergence. |
| 4 | Explicit categorical object instead of universal property | No applicable universal property for bounded-height nonzero subsets. |
| 5 | Missing helper API | A multivariate coefficient sup-height interface and an equivalence with degree-bounded support could shorten consumers. The verified bridge is a new helper proof, not already-existing mathlib API. |

MATHLIB-IDIOMATIC for the present project definition. Upstream refactoring would select and develop the generic height/support interface first; its cost is not used to downgrade a mathematically valid contribution.

## Phase 5 — actual five-method search, all three forms

Each cell names a complete archived request and response. Online index revisions may differ from this pin. Local search explicitly reports `index: unavailable`; its heuristic hits do not prove absence.

| Form | Lean-Finder | Loogle | LeanSearch | rg | Local |
|---|---|---|---|---|---|
| Current: nonzero integer polynomials with degree/coefficient bounds | [receipt](../evidence/Roth.RSet/search-current-finder.json): degreesLE/restrictDegree | [receipt](../evidence/Roth.RSet/search-current-loogle.json): degreeOf inequalities | [receipt](../evidence/Roth.RSet/search-current-leansearch.json): support/nonzero machinery | [receipt](../evidence/Roth.RSet/rg-current.json): no exact spelling hit in searched files | [receipt](../evidence/Roth.RSet/search-current-local.json): Roth.RSet heuristic hit only |
| Literature: naive height with multidegree bound | [receipt](../evidence/Roth.RSet/search-standard-finder.json): unrelated complexity and restrict degree candidates | [receipt](../evidence/Roth.RSet/search-standard-loogle.json): restrictSupport and API | [receipt](../evidence/Roth.RSet/search-standard-leansearch.json): total/uniform degree submodules | [receipt](../evidence/Roth.RSet/rg-standard.json): restrictSupport and univariate supNorm | [receipt](../evidence/Roth.RSet/search-standard-local.json): restrictSupport candidates |
| Abstract: Finsupp support restriction plus interval coefficients | [receipt](../evidence/Roth.RSet/search-abstract-finder.json): Finset.mem_finsupp_iff | [receipt](../evidence/Roth.RSet/search-abstract-loogle.json): Finsupp.supported | [receipt](../evidence/Roth.RSet/search-abstract-leansearch.json): support_subset_iff / mem_finsupp_iff | [receipt](../evidence/Roth.RSet/rg-abstract.json): finite coefficient support and intervals | [receipt](../evidence/Roth.RSet/search-abstract-local.json): supported submodules |

Pinned positive candidate signatures and the generic exact degree bridge were checked in [isolated mathlib-only execution](../evidence/Roth.RSet/rset179-isolated-receipt.json). Its `#check_failure Roth.RSet` guards against importing the target. Archived mathlib source files and hashes document the height, Lp, coefficient-box and support APIs; see [inventory](../evidence/Roth.RSet/mathlib-inputs.json). `MvPolynomial.supported` restricts the set of variables rather than monomial exponents and is not the required degree box. `restrictDegree` uses one uniform bound; `restrictTotalDegree` bounds the sum, so neither replaces arbitrary r directly.

## Phase 5.5 — all three statement-shape checks

Normal form: the direct membership triple is appropriate for arithmetic callers. Equivalent forms include nonzero intersected with the restrictSupport carrier and the all-coefficient interval preimage. No single canonical mathlib name for the full conjunction was verified; the exact degree-only normal form is restrictSupport. A future equivalence should place that chosen form on the RHS.

Syntactic generality: the native definition already avoids redundant Fintype and DecidableEq assumptions. Actual experiments compare its literal set-builder RHS (`rfl`) and its support-submodule form (new proof). The original is easiest for current callers, which repeatedly need the three projections separately. The richer form is preferable for algebraic support reasoning.

Superfluous arguments: NONE. σ determines the polynomial algebra; B determines the allowed coefficients; r determines the allowed exponents. No explicit hypotheses or instances exist to drop. Overall SHIP-AS-STATED locally, with upstream public naming and representation still unsettled.

## Phase 6.0 — complete callers and inline audit

Lexical searches were cross-checked against tracked Git sources despite ignore rules: [rg](../evidence/Roth.RSet/callers.json), [git grep](../evidence/Roth.RSet/git-callers.json). The 6 occurrences outside Theta are all in MainLemma. Within Theta there are 9 code occurrences excluding the declaration itself (documentation is separate). The canonical 293-name kernel-value audit finds **19 direct value consumers**, and a separate fresh audit finds **12 direct type consumers**, distinct quantities from explicit textual references; neither is a full transitive kernel/simp dependency closure. See [value names](../evidence/Roth.RSet/direct-consumers.json), [type names](../evidence/Roth.RSet/direct-type-consumers.json), [raw value audit](../evidence/Roth.RSet/rset179-original-receipt.json), and [fresh type/value audit](../evidence/Roth.RSet/rset179-type-audit-receipt.json).

| Explicit source consumer | Role and local representation plan |
|---|---|
| Theta:63 `indexSet` | Existential over RSet; retain name locally. A representation change needs exact bridge inside the existential. |
| Theta:73,75 `one_mem_RSet` | Membership statement and explicit unfold; retain all three bounds. |
| Theta:99 `index_le_Θ` | Membership hypothesis supplies polynomial / point bound; preserve exact numerical conclusion. |
| Theta:125 `Θ_le_of_forall_index_le` | Quantifies over this set; changing representation rewrites the domain only after equivalence. |
| Theta:416 `index_separated_mul_le_aux` | Smaller-variable U membership. |
| Theta:425 local `hVmem` | Constructs one-variable membership from a Polynomial via uniqueAlgEquiv; all three conjuncts matter. |
| Theta:458 `index_det_le` | Inputs degree and coefficient bounds for determinant estimates. |
| Theta:559 `index_le_lem6` | Uses nonzero/degree to build a nonzero separated determinant. |
| MainLemma:390 `sub_mem_RSet` | Subtraction of nonnegative coefficient boxes yields a nonzero signed height body; B, not 2B. |
| MainLemma:555 `exists_mem_RSet_le_index_aux` | Pigeonhole construction output plus lower index bound. |
| MainLemma:585 `exists_mem_RSet_le_index_of_rpow_bound_aux` | Existence with bounded coefficients and index. |
| MainLemma:622 `exists_mem_RSet_le_index_of_log_bound_aux` | Changes the numerical coefficient cap. |
| MainLemma:647 `exists_auxiliary_polynomial_of_log_bound_aux` | Raises bound to q-power and retains derivative estimate. |
| MainLemma:698 `exists_auxiliary_polynomial_with_index_gap_aux` | Combines lower index with Θ; exact coefficient body feeds final main_lemma. |

The explicit occurrence counts include the `RSet` term inside `one_mem_RSet`'s statement/body twice and the local hVmem once; qualified declaration names containing `_RSet` are not separate exact-word occurrences. [Inline audit](../evidence/Roth.RSet/inline-audit.json) finds many separate nonzero/degree/coefficient hypotheses in CoeffNorm and Separation, plus the nonnegative `boxFamily` body. These are not redundant rediscoveries of the exact signed, nonzero RSet: boxFamily includes zero and uses [0,B], while several estimates legitimately omit nonzero or one bound. No complete independently rederived RSet alias was found.

## Phase 6 — actual composition and caller experiments

[Project composition](../evidence/Roth.RSet/rset179-composition-receipt.json) verifies:

* Exact equality with nonzero ∧ restrictSupport degree carrier ∧ every coefficient bound. It needs normalization by `degreeOf_le_iff` and reordering universal quantifiers; the executed proof is a new roughly 11-line bridge, not a ≤3 existing-call replacement.
* Negative B gives the empty set, and zero is excluded at B=1.
* Literal RHS inlining is `rfl`; this merely unfolds the project's own definition, not a mathlib definition for the full object.

[Isolated generic proof](../evidence/Roth.RSet/rset179-isolated-receipt.json) checks the degree bridge over any CommSemiring and arbitrary σ, with no Roth imports. [Caller experiment](../evidence/Roth.RSet/rset179-callers-receipt.json) restates `sub_mem_RSet` with the complete literal membership triple, and restates `index_le_Θ` with precisely that triple as input while keeping the numerical Θ conclusion. These are interface composition examples using existing project API, not full source-proof replays. These actual calls verify representation transparency; project calls do not count as mathlib replacement building blocks.

Attempts through finite coefficient arrays need finite exponent-box data and interval conversion; through supNorm need a new multivariate interface; through projective Height or ℓ¹ norm change semantics. No exact ≤3 existing-call full replacement was verified. This is a calibrated search result, not an assertion that no such expression can exist. Per Phase 6b, even a successful simp-normalization composition is not automatic NO when representation choice remains substantive. Initial project composition used a deprecated set membership name; its warning-only rejected receipt is archived separately and the accepted proof is clean.

## Phase 7 — verdict and concrete future API questions

**BORDERLINE-needs-human.** The arithmetic name has a semantic one-line exemption, genuine consumers, and an exact source definition. Mathlib already has the degree submodule and finite coefficient-array ingredients, but no verified complete named bounded-height/nonzero body was found. The central decision is whether the correct reusable addition is a multivariate naive-height API with this as a local intersection, or a public named bounded-height family. This is not a cost-based downgrade, an inherited verdict, or a claim that a nontrivial helper is already mathlib.

1. Should mathlib expose a generic multivariate coefficient sup-height API, leaving ℛ as a local degree/height intersection?
2. Should a public bounded-coefficient family include zero, with nonzero imposed by the index application?
3. Should its primary degree parameter be an arbitrary monomial support set, with coordinate boxes as a specialization?
4. Is there an independent downstream use for this precise integer, real-bound, nonzero conjunction that justifies a public name beyond the Roth proof?

Until that design is chosen, retain `Roth.RSet` in `Roth/Theta.lean`; no deletion or caller edits are recommended. A new generic API should be assessed and grouped on its own merits, not silently substitute projective height or finite-support assumptions. No upstream file path/PR grouping is proposed because this is not a YES verdict.

## Phase 8 — completion and verification limits

All requested phases and all 15 formal search cells are complete. Every accepted native experiment has a successful complete receipt and standard axioms; source/pin fingerprints match and the canonical audit checks exact ordered 293 distinct declarations. All semantic experiments preserve nonzero, separate degrees, and the actual numerical coefficient cap. External search/index limitations and rejected diagnostics are explicit. [Assessment](../evidence/Roth.RSet/assessment.json), [verification](../evidence/Roth.RSet/verification.json), [overview entry](../evidence/Roth.RSet/overview-entry.json), [portable validator](../evidence/Roth.RSet/validate.py). Verification unresolved list is empty; future upstream API design questions are the reason for BORDERLINE, not incomplete verification.
