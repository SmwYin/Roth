# MvPolynomial.hasseDeriv_map

Verdict: **YES-add-as-is**. This is useful coefficient-change API with seven explicit invocations in five caller declarations. The coefficient proof is short, but its normalization uses a project-specific coefficient theorem and scalar preservation. The raw mathlib-only construction requires a substantive monomial/additive induction. No existing mathlib replacement has been verified. A closing simplification through project lemmas is not evidence of a three-call existing-mathlib composition. An additive coefficient-map extension is mathematically meaningful; it changes the coefficient-map representation and must not be advertised as simply weakening the existing `MvPolynomial.map` signature.

## Phase 0 — baseline and boundaries

All 17 source/pin SHA256 values freshly match the shared successful `lake build` baseline (2467 jobs, exit 0). [source-check.json](../evidence/MvPolynomial.hasseDeriv_map/source-check.json), [baseline-build.txt](../evidence/MvPolynomial.hasseDeriv_map/baseline-build.txt), and [worker-source-manifest.json](../evidence/MvPolynomial.hasseDeriv_map/worker-source-manifest.json) retain the check. Production Lean files, pins and Git are unchanged. The entire declaring module was read; the five caller declarations and surrounding context were read. Scope is explicit source uses, not hidden kernel or simp dependency closure.

## Phase 1 — statement and mathematics

`Roth/HasseDeriv.lean:134`, public theorem in namespace `MvPolynomial`:

```lean
theorem hasseDeriv_map {σ R : Type*} [CommSemiring R]
    {S : Type*} [CommSemiring S] (f : R →+* S) (d : σ →₀ ℕ)
    (P : MvPolynomial σ R) :
    hasseDeriv d (map f P) = map f (hasseDeriv d P)
```

The full native elaborated type and standard axioms are in the accepted target receipt listed by [verification.json](../evidence/MvPolynomial.hasseDeriv_map/verification.json). Variable type and coefficient rings have independent universes. `map` changes coefficients and fixes monomials. At exponent `e`, both sides have coefficient `(hasseCoeff d (e+d) : S) * f (P.coeff (e+d))`: `f` preserves multiplication and every natural-number cast. This last step is an essential normalization premise, not supplied by extensionality alone.

The original proof is `ext e; simp [coeff_hasseDeriv, coeff_map]`. Accepted forced replay specifies `simp only [coeff_hasseDeriv, coeff_map, map_mul, map_natCast]`, excluding accidental use of its own theorem or downstream simplification. Project dependencies are `hasseDeriv`, `hasseCoeff` through `coeff_hasseDeriv`, and `coeff_hasseDeriv` itself. None is an existing mathlib replacement merely because its project proof has already been assessed.

## Phase 2 — size

SMALL: a compatibility law, not a new foundational construction. Definition-only one-line check is N/A because this is a theorem; proof length does not activate that prefilter. No inherited verdict and no exact namespace match in pinned mathlib.

## Phase 3 — exhaustive literature

Exact requests, hashes/byte counts of returned representations, status, and concise original summaries are retained in [web-requests.json](../evidence/MvPolynomial.hasseDeriv_map/web-requests.json) and [web-sources.json](../evidence/MvPolynomial.hasseDeriv_map/web-sources.json). No article/search-result bodies are archived. Each row records an actual query/access; access failures are not negative mathematical findings.

| Channel | Actual query/access | Finding |
|---|---|---|
| Specific web | Hasse derivative polynomial coefficient ring homomorphism base change naturality | Polynomial coefficient-extraction characterization; base-change interpretation follows algebraically. |
| General web | Hasse Schmidt derivation polynomial algebra arbitrary base ring divided partial derivatives | Narváez Macarro, AIF 59 (2009), pp.2979–3014; polynomial divided differential operators over commutative bases. |
| Alias web | multivariate Hasse derivatives coefficient homomorphism characteristic p Taylor expansion | Recent finite-field algorithm papers use Taylor coefficient extraction; no factorial inverses. |
| ChatGPT mathematical MCP | Standard form, generality and historical evolution | N/A: `ask_chatgpt_math` unavailable. Other channels still completed. |
| Local references | `rg Hasse|Delta|derivative clean.tex` | §1 lines119–154 defines binomial monomial operators over any commutative semiring and explicitly asks for coefficient-map compatibility. |
| nLab | Hasse Schmidt derivative base change | [Hasse-Schmidt derivative](https://ncatlab.org/nlab/show/Hasse-Schmidt%2Bderivative), one/several indeterminates: commutative rigs and linear extension. |
| nCatLab | Hasse Schmidt derivation functor; direct derivation page | Categorical/natural transformation framing considered; direct page returned 400 unsupported XHTML. Indexed nearby material does not establish an exact naturality theorem. |
| Stacks | Hasse Schmidt derivations base change | [Tag05G3](https://stacks.math.columbia.edu/tag/05G3), §10.14: coefficient change on polynomial presentations and tensor base change. No exact Hasse law located. |
| MathOverflow | Hasse Schmidt derivatives / coefficient ring | [Question440759](https://mathoverflow.net/questions/440759/what-is-the-relationship-between-higher-order-derivations-in-the-sense-of-hasse), 2023: generalized Leibniz operators versus jet functors. Context, not a replacement theorem. |
| Recent arXiv | Hasse Schmidt derivations 2022 2023 2024 2025 2026 | [2305.04537](https://arxiv.org/abs/2305.04537), 2023 high-order algebra; [2509.00887v2](https://arxiv.org/abs/2509.00887), 2025 lifting/deformation; [2605.20664](https://arxiv.org/abs/2605.20664), May2026 multi-HS and n-trivial extensions. Abstracts accessed; no claim of full-paper theorem inspection. |

Standard concept: naturality of polynomial Hasse/divided derivatives under coefficient homomorphisms. Classical finite-variable field versions, arbitrary commutative rings, and semiring combinatorial formulations agree on the natural-number monomial factors. Arbitrary-base HS derivations have additional product/iterativity data; not every abstract HS derivation is this chosen coordinate operator. Historical ordinary divided derivatives in characteristic zero motivate the definition but do not justify characteristic-zero restrictions. The coefficient-change conclusion is inferred from the formulas, rather than quoted as a theorem in every source. Recent abstract extensions do not force replacing this API with jets or higher categories.

## Phase 4a–b — generality

| Parameter/axis | Audit and actual probe |
|---|---|
| σ | Arbitrary type, no finite/decidable/inhabited assumption. Only each multi-index has finite support. |
| R/S | Both CommSemiring, no additive inverses, characteristic assumption, nontriviality or cancellation. Native scalar-preservation probes compile under the weaker Semiring hypotheses. |
| CommSemiring → Semiring in current theorem | Actual `#check_failure` elaborations audit the fixed parent/operator/map interface: weakening the scalar proof does not weaken the declared parent automatically. |
| RingHom f | No injectivity/surjectivity or field embedding assumption. This handles reduction modulo primes as well as ℤ→ℚ→ℝ. |
| Additive hom f | The binomial factor only uses natural scalar multiplication. Native additive theorem uses `AddMonoidAlgebra.map (f : R →+ S) P` and `coeff_addMonoidAlgebraMap`, with `map_nsmul`; a zero additive map on ℕ witnesses a nonunital map unavailable as a RingHom. This is an expanded API representation, not literal `MvPolynomial.map` with a weaker binder. |
| d/P | All orders including zero and all polynomials including zero; no degree or support bound needed. |
| Unused binders | None: f, d, P and typeclass interfaces appear in the statement. |
| Noncommutative/general coefficient modules | Underlying additive/Finsupp operations admit broader versions; rebuilding the parent linear operator outside its fixed CommSemiring interface is structural work, not a verified one-edit weakening. |
| Arbitrary coefficient function | Rejected: without additivity/natural scalar preservation there is no reason a coefficient function commutes with integer weights. The accepted abstraction explicitly retains the weight law through an additive hom. |

Generality verdict: maximally general **within the fixed RingHom/MvPolynomial parent interface**; genuine additive coefficient-map extension verified separately. The canonical RingHom interface agrees with pinned univariate Hasse and multivariate partial derivative laws; the additive extension is an optional companion, not a required primary-interface restatement.

## Phase 4c — modern idiom (all nine rows)

| # | Diagnostic | Result / downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of preambles | Already CommSemiring instances and bundled RingHom. No custom structure predicate. |
| 2 | Filters/nets | No topology or limits. |
| 3 | Universal property | Polynomial universal property can package substitution naturality; no existing universal-property theorem identified that supplies this chosen operator's coefficients. |
| 4 | Bundled substructure | No closure predicate or subobject to bundle. |
| 5 | Modules/semirings | Already semiring rather than field. Additive coefficient-map extension enables nonunital coefficient maps; scalar calculation needs only Semiring. |
| 6 | Higher categories | No demonstrated higher-categorical downstream advantage for this pointwise law. |
| 7 | Abstract index monoid | Exponents/multi-index use natural numbers and binomial/truncated subtraction. Arbitrary index monoid changes the chosen operator; generic weighted coefficient operators are a separate abstraction. |
| 8 | Concrete-via-abstract | Fires: after coefficient normalization, no property of binomial weights remains besides being natural numbers; shift `e↦e+d` can be arbitrary. Accepted generic theorem takes two operators DR/DS and their weighted-coefficient formulas hR/hS. It is a newly proved helper, not an existing mathlib result. It would reuse normalization for other natural weighted coefficient shifts; no project caller needs arbitrary operators today. |
| 9 | False-generalization guard | Additive map preserves precisely the additive/natural scalar content; hR/hS are retained. Dropping them or claiming arbitrary linear maps automatically form the same natural family is rejected. Index-monoid and jet replacements change structure and are not mechanical proposals. |

Modern-idiom verdict: a real additive/weighted naturality extension exists, but does not establish that the public coordinate Hasse API should disappear. No YES-generalise-first claim from untested typeclass guesses. The abstract coefficient premises contain the substantive operator information; the abstraction is not itself grounds to replace the concrete coordinate API.

## Phase 4.5 — six infrastructure risks

Defeq abuse, instance diamonds, coercion coherence, reducibility/performance barriers, overlapping instances, and canonical-construction stability are each N/A: theorem adds no definition/class/instance. Ordinary rewrite orientation is audited separately below; it is not a typeclass diamond.

## Phase 4.6 — proof strategy (all five rows)

| # | Question | Finding |
|---|---|---|
| 1 | Topology ε–δ vs filters | N/A finite algebra. |
| 2 | Elements vs submodule/ideal inclusion | Coefficient extensionality is the native equality interface; no ideal/submodule claim to abstract. |
| 3 | Sequences vs nets | N/A. |
| 4 | Construction vs universal property | No object constructed. Functorial square version compiles but pointwise form rewrites actual callers directly. |
| 5 | Missing helper | Natural weighted coefficient normalization over additive maps is proven as a new helper candidate. Existing `map_nsmul` handles the scalar step, so no new natural-cast theorem is required. |

Proof-strategy verdict: current coefficient strategy is idiomatic. Induction over monomials is an alternative, not a demonstrated improvement. Broad `ext` recursion and uncontrolled simp are avoided in evidence probes.

## Phase 5 — five actual search methods, three forms

| Method | Current form | Literature form | Abstract form |
|---|---|---|---|
| Lean-Finder | Multivariate Hasse derivative / coefficient change | HS naturality / base change | Natural-number weighted finitely-supported reindexing / additive hom |
| Loogle | `Polynomial.hasseDeriv, Polynomial.map` | `MvPolynomial.map, MvPolynomial.pderiv` | `Finsupp.mapRange, Finsupp.mapDomain` |
| LeanSearch | Same natural-language current query | Same base-change query | Same weighted additive query |
| Source rg | Full qualified target plus hasseDeriv_map declarations | HS/higher derivative/pderiv_map source names | mapDomain_mapRange, mapRange_smul, mapRange_finsetSum, lsum interactions |
| Local partial-name | `hasseDeriv_map` | `map_hasseDeriv` | `mapRange_smul` |

All 12 API receipts and eight exact rg commands are retained. The local index reports unavailable; fallback includes project and assessment excerpts, so hits require provenance filtering. External indexes may differ from the pin. Neither empty results nor failed methods prove absence.

Positive pinned signatures checked by native Lean: `Polynomial.hasseDeriv_map` (`Algebra/Polynomial/HasseDeriv.lean:128`), `MvPolynomial.pderiv_map` (`Algebra/MvPolynomial/PDeriv.lean`), `Finsupp.mapDomain_mapRange` (`Data/Finsupp/Basic.lean:463`), `Finsupp.mapRange_smul` (`Data/Finsupp/SMulWithZero.lean:102`), `MvPolynomial.coeff_map`, and `MvPolynomial.coeff_addMonoidAlgebraMap`. The first two cover one variable and first-order derivatives respectively; no transport term from either to all multivariate orders was supplied. The Finsupp theorems concern domain reindexing/uniform scalar mapping; index-dependent weights still require normalization. No direct existing target replacement is verified.

The isolated probe guards target/parent nonexistence in its mathlib-only imports using `#check_failure`. This checks that import environment only, not global absence. A prior unrelated `exact?` on the Hasse delta exhausted default200k heartbeats; no unsupported repeated heavy search was run. Positive coefficient and scalar normalization probes address the actual obstruction instead.

## Phase 5.5 — statement shape (all three checks)

1. Normal form: current left-to-right rewrite moves coefficient change out of the derivative, matching bounds/evaluation and determinant consumers. Opposite use at MainLemma492 is intentional. A function-square equality compiles; bundling as an R-linear equality would require scalar restriction/semilinear handling across different rings.
2. Syntactic generality: explicit `d,P,f` order and function equality alternatives compile. No extra hypothesis was hidden in argument order.
3. Superfluous arguments: all binders used; no finite-variable/decidable assumptions to drop. Literal map and hasseDeriv typeclass weakening was actually checked, and additive representation is distinguished explicitly.

Statement-shape verdict: current rewrite form is appropriate. The optional additive companion does not require restating the canonical RingHom law before shipping.

## Phase 6.0 — all explicit source callers and inline audit

Target is **not** registered `[simp]`; each simp use below explicitly supplies it. Seven invocations in five declarations, no in-file use after declaration. [grep-receipts.json](../evidence/MvPolynomial.hasseDeriv_map/grep-receipts.json) includes broad inline audit (`hasseDeriv.*map|map.*hasseDeriv|coeff_map|coeff_hasseDeriv`). Numerous mapped-derivative expressions are consumers of this interface, not independent proof duplicates.

| Source | Caller | Use and concrete alternative if locally inlined |
|---|---|---|
| Separation533 | private exists_rat_factors_det_hasseDeriv_aux | Explicit `rw` normalizes matrix derivative entries after ℤ→ℚ. A local coefficient-change identity instantiated at `Int.castRingHom ℚ` supplies the same rewrite. |
| Theta524 | private mapped_det_ne_zero_aux | Matrix.ext entry goal; replace simp target with the local coefficient-ext proof instantiated ℤ→ℝ. |
| Theta580 | index_le_lem6 | `simp only` at `hlower`; a local polymorphic-in-d/P map identity supplies exactly that rewriting. |
| MainLemma409 | eval_hasseDeriv_sub_eq_zero | Simpa changes derivative of mapped difference into mapped derivative before eval_map. Supply local identity at the ℤ→S map and same remainder simplifications. |
| MainLemma489 | private exists_hasseDeriv_index_eval_bound_aux | Simpa transports nonvanishing; local identity specializes to order k. |
| MainLemma492 | same | Reverse rw exposes derivative before coefficient change for index inequality; use local identity.symm in that direction. |
| MainLemma495 | same | Simpa transports the two derivative bounds; inner/outer instances of local identity normalize the required nesting. |

The initially proposed additive dotted `P.map f` incorrectly selected the RingHom map; the rejected attempt is retained separately. Accepted code explicitly uses `AddMonoidAlgebra.map`.

The accepted `observe` and `twice` fragments verify arbitrary outer contexts and nested normalization with the forced theorem, independently of using the target. These are **scoped interface experiments**, not a full reconstruction of private downstream declarations. Baseline source hashes certify existing callers compile unchanged. No production caller refactor is proposed in this read-only YES assessment. The table makes a hypothetical deletion plan concrete without pretending inline proofs become existing upstream building blocks.

## Phase 6 — actual composition experiments

Forced target replay closes by coefficient extensionality plus `simp only` over the project coefficient formula and pinned `coeff_map`, `map_mul`, `map_natCast`. The isolated generic theorem repeats the proof with explicit hR/hS. Thus it is not a ≤3-call existing-mathlib normalization term: the project-specific coefficient law is a premise, and weighted-operator naturality is newly proved.

Pinned `Polynomial.hasseDeriv_map` is a genuine analogous law but not a replacement on arbitrary variable types. `pderiv_map` handles first order and cannot recover all positive-characteristic divided derivatives by dividing factorials. `Finsupp.mapDomain_mapRange` alone has no index-dependent weight-normalization premise. The native cast and additive-weight proofs explicitly verify that premise. The raw isolated reconstruction builds delta from `Finsupp.lsum` and the coefficient linear equivalence, proves its monomial calculation with the existing typed `Finsupp.lsum_single` term, then proves coefficient-change naturality by polynomial induction. This uses no Roth import and assumes no project coefficient law. The induction splits monomial scalar preservation from additive extension, so this is a proof, not just composition of three already available naturality calls. No new axioms, sorry/admit, unsafe/native_decide or raised limits are accepted.

Composition verdict: **NOT-COMPOSABLE from verified existing pinned mathlib calls**. The isolated raw delta reconstruction needs verified monomial evaluation and induction over polynomial sums/monomials. Generic helper discovery is not proof that mathlib already contains the helper; no NO verdict is inferred from it. The shorter project-coefficient proof is useful proof engineering but cannot by itself activate the existing-mathlib trivial-simp criterion.

## Phase 7 — decision and action

**YES-add-as-is.** Concrete missing API: the arbitrary-variable, all-multiorder coefficient-change law for the multivariate Hasse operator. It permits transfer of divided-derivative matrices, evaluations, index inequalities and coefficient bounds across coefficient rings, as the seven actual uses demonstrate. Mathlib has the corresponding univariate `Polynomial.hasseDeriv_map` and first-order `MvPolynomial.pderiv_map`; neither supplies a verified replacement for all divided multiorders in arbitrary characteristic. This is a reusable algebraic compatibility law rather than Roth-specific bookkeeping.

The raw isolated proof establishes the law from the actual operator construction with verified monomial evaluation and additive induction. The shorter coefficient proof depends on the substantive project coefficient formula. Thus neither is evidence of a ≤3 existing-mathlib-call replacement. Shortness after adding the parent coefficient interface is ordinary API design, not grounds to delete a repeatedly used naturality law.

The literature-standard coefficient-ring homomorphism formulation and the two pinned analogous map laws support the present RingHom surface. The verified additive coefficient-map theorem is a useful optional companion: it preserves the same combinatorial operation but expresses coefficient change through `AddMonoidAlgebra.map`. Sources do not establish this additive interface as the preferred standard primary formulation, and the abstract DR/DS theorem still assumes the operator coefficient formulas. Neither observation forces generalise-first or a material human-policy question. YES is based on the fresh target-specific checks, not inheritance from its parent.

**Proposed mathlib path:** `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`.

**Proposed PR title:** `feat(Algebra/MvPolynomial/HasseDeriv): add coefficient-change naturality for Hasse derivatives`.

**Grouping:** include with the already-assessed YES declarations `MvPolynomial.hasseDeriv` and `MvPolynomial.coeff_hasseDeriv` as one coherent multivariate Hasse API. Do not infer verdicts for unassessed identities or automatically upstream the separately assessed scalar `hasseCoeff` alias. The public parent must exist upstream before this law can be submitted independently.

**Pre-PR checklist:**

1. Run `/generalise MvPolynomial.hasseDeriv_map`, retaining arbitrary variables/semirings; consider the verified additive companion without falsely weakening literal `MvPolynomial.map`.
2. Run `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_map`, with coefficient proof avoiding circular simp and appropriate upstream import/module style.
3. Recheck the then-current mathlib snapshot for duplication and decide `[simp]` registration consistently with `Polynomial.hasseDeriv_map`; ordinary rewrite-attribute review is not an unresolved assessment gate.
4. Select Moritz Firsching, author of pinned commit `334438dace` adding `Polynomial.hasseDeriv_map` (#42428), as a relevant reviewer candidate; Yaël Dillies, `631b214f7c` on the MvPolynomial coefficient API (#41427), is another candidate. These are candidates from actual recent file history, not claims that they agreed to review. The exact read-only history request/result is in `reviewer-commits.json`.

**Alternative destination:** retain in `Roth/HasseDeriv.lean` while preparing the coherent upstream parent API. Core general algebra is appropriate for mathlib rather than Archive. No deletion, production refactor or external PR action is authorized by this assessment. Next action is independent root review/publication of the completed assessment, followed by the next declaration in overview order.

## Phase 8 — evidence and verification

[assessment.json](../evidence/MvPolynomial.hasseDeriv_map/assessment.json), [verification.json](../evidence/MvPolynomial.hasseDeriv_map/verification.json), [copy-manifest.json](../evidence/MvPolynomial.hasseDeriv_map/copy-manifest.json), and [validate.py](../evidence/MvPolynomial.hasseDeriv_map/validate.py) are the machine-readable handoff. The portable validator checks source/pin hashes, complete successful native receipts, exact executed snippets, standard axioms, phase completion, search coverage, links and copy bytes/hashes. Root acceptance is pending independent review. No source changes were requested or made.
