# Roth.hasseDeriv_rename_mul_aeval

Verdict: **YES-but-generalise-first**. The factorwise Hasse law is useful algebraic API, and the arbitrary fresh-coordinate formulation has now been proved. Its current `Option τ` representation is unnecessarily restrictive for callers that already embed their variables into a larger type. The original statement is a verified one-call specialization of the new result. This is a new theorem using the project Hasse foundation, not an existing mathlib replacement.

## Phase 0 — baseline

All17 source/pin hashes freshly match the successful shared build (exit0,2467 jobs). [inputs.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/inputs.json), [input-manifest.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/input-manifest.json), [baseline-build.txt](../evidence/Roth.hasseDeriv_rename_mul_aeval/baseline-build.txt) and the successful current index-file-completion receipt are preserved. Production/Git/pins/overview/progress unchanged. Entire declaring module, project Hasse module and complete sole caller were read; complete source copies and hashes are in [source-links.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/source-links.json). Scope is one canonical declaration160.

## Phase 1 — full statement and mathematics

```lean
@Roth.hasseDeriv_rename_mul_aeval.{u_1,
    u_2} : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring.{u_2} R] (d : Finsupp.{u_1, 0} τ ℕ) (ν : ℕ)
  (U : MvPolynomial.{u_1, u_2} τ R) (V : Polynomial.{u_2} R),
  Eq.{max (u_1 + 1) (u_2 + 1)}
    ((MvPolynomial.hasseDeriv.{u_1, u_2}
        (HAdd.hAdd.{u_1, u_1, u_1} (Finsupp.mapDomain.{u_1, u_1, 0} some.{u_1} d)
          (Finsupp.single.{u_1, 0} none.{u_1} ν)))
      (HMul.hMul.{max u_1 u_2, max u_1 u_2, max u_1 u_2} ((MvPolynomial.rename.{u_1, u_1, u_2} some.{u_1}) U)
        ((Polynomial.aeval.{u_2, max u_1 u_2} (MvPolynomial.X.{u_2, u_1} none.{u_1})) V)))
    (HMul.hMul.{max u_1 u_2, max u_1 u_2, max u_1 u_2}
      ((MvPolynomial.rename.{u_1, u_1, u_2} some.{u_1}) ((MvPolynomial.hasseDeriv.{u_1, u_2} d) U))
      ((Polynomial.aeval.{u_2, max u_1 u_2} (MvPolynomial.X.{u_2, u_1} none.{u_1}))
        ((Polynomial.hasseDeriv.{u_2} ν) V)))
```

Native full type/axioms and kernel-value audit: [hasse-separation-original-audit-receipt.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/hasse-separation-original-audit-receipt.json). The pretty-printer explicitly elides3558 characters in its large proof-body dump; this is not claimed to be a complete kernel-body print. Complete executed source, full native type, standard axioms and canonical value audit remain available.

Let `U` involve the old variables and let `V` involve a fresh coordinate. Then differentiating with multiorder `(d,ν)` differentiates `U` with order `d` and `V` with order `ν`. Since the supports of the two multiorders are disjoint, their Hasse operators compose without a binomial factor. Each other factor has degree zero in the active coordinate block, so it can be pulled outside that operator. Injective variable renaming commutes with Hasse differentiation, and the fresh-coordinate embedding commutes with the univariate Hasse operator. This proves the formula over arbitrary commutative semirings, including positive characteristic.

Project dependencies: `hasseDeriv`, disjoint composition, degree-zero product extraction, single-coordinate `aeval` compatibility and injective rename compatibility all come from `Roth/HasseDeriv.lean`. The original also uses the wrapper `Roth.aeval_X_eq_rename`; the fresh proof replay replaces it by `AlgHom.congr_fun (Polynomial.toMvPolynomial_eq_rename_comp none)`. A theorem being named `MvPolynomial.*` does not mean it belongs to the pinned mathlib.

## Phase 2 — size and prefilters

SMALL: algebraic compatibility law supporting determinant entries. The one-line definition-only test is n/a because this is a theorem. It is public substantive API, with a complete proof rather than a mere name alias. One explicit use supplies a weak positive API signal; no verdict is inferred from count alone.

## Phase 3 — exhaustive literature

Exact requests, response representation SHA256/bytes/status, URLs/titles and original summaries are in [literature-search.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/literature-search.json) and [literature-primary.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/literature-primary.json). Full web/search bodies are not archived. Returned locator query strings were removed preventively. Channel availability is in [literature-availability.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/literature-availability.json).

| Channel | Actual query/access and finding |
|---|---|
| Specific web | `Hasse derivative separated variables product formula`: primary ECCC2024 §2.1 gives product/composition rules and coefficient definition. |
| General web | `multivariate Hasse Schmidt derivatives polynomial rings arbitrary characteristic product rule`: multivariate HS/substitution descriptions. |
| Alias web | `hyperderivatives divided power derivatives disjoint variables`: hyperderivative/divided-derivative terminology and characteristic caveats. |
| ChatGPT mathematics | n/a: `ask_chatgpt_math` is unavailable; historical/general-form inquiry cannot be run with that optional tool. |
| Local manuscript | Actual rg in `clean.tex`; §2 Lemma2 proof, lines408–417, matrix entry is the mixed derivative of a separated product. [local-literature-search.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/local-literature-search.json), [clean-excerpt.tex.txt](../evidence/Roth.hasseDeriv_rename_mul_aeval/clean-excerpt.tex.txt). |
| nLab | `site:ncatlab.org/nlab/ Hasse Schmidt derivation`: [HS derivation](https://ncatlab.org/nlab/show/Hasse-Schmidt%2Bderivation) and derivative pages returned. Actual direct access failed400 unsupported XHTML; search snippets are context, not a full page verification. |
| nCatLab | `site:ncatlab.org/ncatlab Hasse Schmidt derivation polynomial`: results were in `/nlab`, no exact `/ncatlab` entry established. This is an honestly recorded distinct namespace attempt. |
| Stacks | `site:stacks.math.columbia.edu Hasse Schmidt derivations`, then actual [09CH §10.133](https://stacks.math.columbia.edu/tag/09CH): broader finite-order differential operators, not the exact coordinate factorization. |
| MathOverflow | `site:mathoverflow.net Hasse derivative multivariate product`: [71423](https://mathoverflow.net/questions/71423/replacement-for-derivations-in-characteristic-p) and other discussion locate characteristic issues; no direct replacement theorem. |
| Recent arXiv | Actual year query plus refined2023/2024 queries and primary opens. [Barajas2023](https://arxiv.org/abs/2305.04537), submitted2023-05-08, concerns high-order derivations of HS algebras. [Barajas–Duarte2026](https://arxiv.org/abs/2605.20664), submitted2026-05-20, treats generalized multi HS systems. Both are within five years; abstracts provide context, not proof of this exact coordinate identity. |

Concept: separated-variable product law for multivariate Hasse/hyperderivatives. Literature agrees on Taylor coefficient and binomial descriptions; ordinary derivatives divided by factorials only give an unrestricted equivalent formula when those factorials can be inverted. The most general coordinate form embeds disjoint variable blocks into a common variable set. The fresh-coordinate/injective-map form assessed here is a verified expansion of the original interface. This inference follows from coefficient/renaming naturality and the product rule; it is not attributed verbatim to the recent abstracts. General abstract HS families need specified coordinate behavior and cannot simply replace the canonical polynomial family.

## Phase 4a — parameter and generality audit

| Parameter | Current | Generality decision |
|---|---|---|
| `τ : Type u₁` | arbitrary, independent universe | Already arbitrary; no finiteness or decidable equality assumption. |
| `R : Type u₂` | arbitrary | No coefficient specialization. |
| `CommSemiring R` | parent `MvPolynomial.hasseDeriv` interface | Minimal fixed parent interface. Isolated univariate `Semiring` law compiles, but this does not weaken the multivariate theorem without changing its parent representation. |
| `d : τ →₀ ℕ` | finite-support natural multiorder | All orders including0; necessary for polynomial exponents/binomial factors. Arbitrary monoid indices would change the object. |
| `ν : ℕ` | distinguished-coordinate order | Includes0; no positivity needed. |
| `U,V` | arbitrary polynomials | Zero allowed; no field/domain/nonzero assumptions. |
| `some/none` | exact Option presentation | Verified expansion to any injective `f : τ → σ` and fresh `i : σ`, with `∀ j, f j ≠ i`; no requirement that `σ` consist of only these variables. |

## Phase 4b — verified broader form

STRICTLY NARROWER representation interface, with an actual compiled proof of the following statement (same fixed parent coefficient interface):

```lean
theorem freshCoordinate (f : τ → σ) (hf : Function.Injective f) (i : σ)
    (hi : ∀ j, f j ≠ i) (d : τ →₀ ℕ) (ν : ℕ)
    (U : MvPolynomial τ R) (V : Polynomial R) :
    hasseDeriv (d.mapDomain f + Finsupp.single i ν)
      (rename f U * Polynomial.aeval (X i : MvPolynomial σ R) V) =
      rename f (hasseDeriv d U) *
        Polynomial.aeval (X i : MvPolynomial σ R) (Polynomial.hasseDeriv ν V)
```

Actual [hasse-separation-generality-executed.lean.txt](../evidence/Roth.hasseDeriv_rename_mul_aeval/hasse-separation-generality-executed.lean.txt) and [hasse-separation-generality-receipt.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/hasse-separation-generality-receipt.json) prove the theorem by the freshly reproved factorwise law, the injective extension `g : Option τ → σ`, and substantive rename/mapDomain normalization. This is a new theorem built from project prerequisites. [hasse-separation-specialization-receipt.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/hasse-separation-specialization-receipt.json) verifies the exact old statement by one call to `freshCoordinate some (Option.some_injective τ) none (fun j ↦ Option.some_ne_none j)`. No unsupported assumption-drop claim is made. Generalization cost MODERATE; cost does not decide the verdict.

## Phase 4c — modern idioms

| # | Question | Assessment and downstream consequence |
|---|---|---|
|1| Typeclass preambles | No: algebraic hypotheses are already typeclasses; `hf/hi` are data-dependent propositions. |
|2| Filters/nets | No topology or convergence. |
|3| Universal property | Polynomial renaming/`aeval` are already bundled homomorphisms; do not introduce a new class. |
|4| Bundled substructures | No ad hoc closure subset. A subalgebra-based support formulation is possible future API, not a verified substitute here. |
|5| Hierarchy | Already CommSemiring, no field/domain restriction; univariate Semiring is diagnostic only. |
|6| Higher category | No categorical coherence problem requiring a new abstraction. |
|7| Concrete index | Natural orders encode polynomial exponents; changing to arbitrary monoids changes Hasse differentiation. |
|8| Concrete-via-abstract | YES: source proof uses `some/none` only for injectivity and fresh-coordinate support separation, not Option exhaustiveness. Diagnostic: `some/none` remain in several support/degree normalization lines, and each use was inspected; thus not a mechanical zero-occurrence trigger. The successful freshCoordinate proof confirms the abstraction. Larger ambient types now work without constructing/reindexing an Option equivalence. |
|9| False-generalization guard | Preserve the very same canonical Hasse operators through injective renaming. Freshness cannot be removed: isolated `overlapSumOrderCounterexample` proves `D₂(X·X²) ≠ D₁(X)D₁(X²)` over ℕ, with coefficient1 equal to3 versus2. This faithfully preserves the sum of the two derivative orders. The earlier `overlapCounterexample` only diagnoses failure of ordinary multiplicativity and is not itself a direct freshness-drop counterexample. General arbitrary HS systems or ordinary derivatives in small characteristic would change content. |

Modern idiom available: YES, the verified arbitrary embedding/fresh-coordinate interface. It composes with existing rename/aeval maps directly and permits unused ambient variables. This is a real application improvement, not a category-theoretic change of vocabulary.

## Phase 4.5 — infrastructure risk

n/a: theorem. Each of the six definition-risk rows (typeclass diamond, reducibility leak, non-canonical unfolding, instance priority collision, universe-polymorphism issues, coercion ambiguity) is n/a: this introduces no definition/class/instance/coercion, so no such new computational or instance-search path. The native type preserves independent universes. Proposed file depends on the upstream parent Hasse API; import layering should be checked during that PR, rather than introduced by this read-only assessment.

## Phase 4.6 — proof strategy

| # | Strategy question | Result |
|---|---|---|
|1| ε–δ versus filters | No topology. |
|2| Elements versus substructures | Coordinate support/degree-zero is the needed algebra; no ideal-inclusion shortcut. |
|3| Sequences versus nets | No limiting process. |
|4| Construction versus universal property | Existing rename/aeval homomorphisms already implement substitution. |
|5| Helpers mathlib should have | YES: upstream multivariate Hasse family, disjoint composition, degree-zero factor extraction, single-coordinate and rename compatibility. Actual current project lemmas have those statements; they are not pinned mathlib. |

REFACTOR-RECOMMENDED: upstream the fresh-coordinate form and specialize at callers. Its proof can reuse the same support-separation strategy; a future two-block `Sum` law could subsume it, but no unverified broader law is used to justify the present verdict. The generalization already compiles. The target replay also removes the duplicate previous159 wrapper.

## Phase 5 — all fifteen formal search cells

Full raw responses and exact queries: [formal-search.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/formal-search.json). Sources: [rg-current.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/rg-current.json), [rg-standard.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/rg-standard.json), [rg-abstract.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/rg-abstract.json).

| Form | Finder | Loogle | LeanSearch | rg source | Local index |
|---|---|---|---|---|---|
| Current separated rename/aeval law | univariate Hasse product, first pderiv | Hasse coefficient/product rules | same partial matches | no multivariate Hasse declaration in mathlib | project target and replay hits; index unavailable |
| Literature HS/disjoint product | univariate product, unrelated tensor pderiv | constant Hasse rules | univariate Hasse/pderiv | univariate Hasse rules present | project degree-zero helper and mathlib univariate product; index unavailable |
| Abstract Taylor/coefficient substitution | Taylor algebra hom/multiplicativity | Hasse-map compatibility | Taylor coefficient/product, power-series coefficient products | Taylor/sumToIter infrastructure | Taylor coefficient hits; index unavailable |

Every method ran on every form. Source hits are pinned and positive candidates signatures actually checked in isolated native source. External indexes may use different revisions; local unavailable does not prove absence. The compiled mathlib-only guards show both this project theorem and `MvPolynomial.hasseDeriv` are unavailable under the exact mathlib import prefix. Searches plus guards establish the current interface gap rather than a universal impossibility claim. No expensive failed `exact?` repetition or raised limits was used.

## Phase 5.5 — statement shape

Normal forms considered: Option-separated pointwise equality; arbitrary injective fresh-coordinate pointwise equality; a two-block Sum formulation; a polynomial-over-polynomial coefficient formulation. Existing canonical building blocks are rename and `Polynomial.aeval`; no exact pinned multivariate law selects a canonical normal form. Choose `freshCoordinate` with the differentiated factorwise product on the RHS for rewrites. This preserves orientation of the original caller.

Syntactic generality: RESTATE to `f/hf/i/hi`, proved and specialized back; no ambient enumeration required. Superfluous-argument audit: τ/R, CommSemiring, d/ν/U/V are all used. Fintype/DecidableEq are already omitted and absent in native type. hf and hi are explicit mathematical separation conditions in the generalized theorem. Overall RESTATE-BEFORE-SHIP.

## Phase 6.0 — complete caller and inline audit

Fresh `rg --no-ignore`, tracked `git grep`, and canonical-source lexical enumeration: [caller-rg.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/caller-rg.json), [caller-git-grep.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/caller-git-grep.json), [lexical-enumeration.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/lexical-enumeration.json). Exactly two source occurrences: declaration146 and caller365. One explicit caller, zero external-to-file caller files. Ordered293 native kernel-value audit independently finds only `Roth.det_hasseDeriv_separated`; this is direct value use, not transitive dependencies or simp closure.

| Caller | Use | Refactor plan / experiment |
|---|---|---|
| `Roth/Separation.lean:365`, `Roth.det_hasseDeriv_separated` | After determinant/matrix expansion and commuting factors, rewrite each entry by factorwise law | Retain complete Field interface, replace rewrite with generalized theorem specialized to some/none. Full caller replay using fresh proof `factorwise` succeeds with standard axioms. Generalized specialization back to exact old law also succeeds. Complete direct generalized-caller replay using `freshCoordinate some ... none ...` succeeds with the original Field interface: [exact executed source](../evidence/Roth.hasseDeriv_rename_mul_aeval/hasse-separation-generalized-caller-executed.lean.txt), [native receipt](../evidence/Roth.hasseDeriv_rename_mul_aeval/hasse-separation-generalized-caller-receipt.json). |

Inline re-derivation search [rg-inline.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/rg-inline.json): no additional production equivalent derivation bypasses this theorem; occurrences of its component lemmas in the declaration itself are not separate callers. The project foundational Hasse law proofs are prerequisite infrastructure, not a duplicated separated-product theorem.

## Phase 6 — real composition and replacement experiments

1. Existing `Polynomial.hasseDeriv_mul` fails to close the actual target because it is univariate and gives a convolution sum. Exact bounded `fail_if_success` experiment succeeds as a negative test inside the fresh target replay.
2. Existing previous159 bridge alone (`simp only [Polynomial.toMvPolynomial_eq_rename_comp]`) fails to close the multivariate target, also natively checked. The bridge fixes representation of one factor, not multivariate Hasse differentiation.
3. A genuine isolated mathlib-only proof `constantFactor` uses coefficient extensionality, Hasse coefficient formula and commutative multiplication. `separatedCoefficients` then uses Hasse-map compatibility and coefficient multiplication/map. These are real proof experiments ([hasse-separation-isolated-executed.lean.txt](../evidence/Roth.hasseDeriv_rename_mul_aeval/hasse-separation-isolated-executed.lean.txt), [hasse-separation-isolated-receipt.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/hasse-separation-isolated-receipt.json)), but only solve the outer univariate/fresh-coordinate portion. Identifying and differentiating old-variable coefficients requires missing multivariate API.
4. Full target law is reproved using project disjoint composition/degree-zero/single-coordinate/rename lemmas. Complete determinant caller then compiles using this new proof. These project prerequisites do not count as existing mathlib calls, even though their names sit in `MvPolynomial`.
5. Generalized freshCoordinate and originalFormAgain are genuine new project-context proofs; their one-call relation validates the generalization, not a NO verdict. The faithful overlapping-order guard additionally succeeds in the exact same mathlib-only imports: [source](../evidence/Roth.hasseDeriv_rename_mul_aeval/hasse-separation-sum-guard-executed.lean.txt), [receipt](../evidence/Roth.hasseDeriv_rename_mul_aeval/hasse-separation-sum-guard-receipt.json).

Conclusion: NOT-COMPOSABLE from current mathlib in ≤3 calls. No successful closing simp composition was found; none is classified as automatic NO. Prior parent159 has an existing generalized `aeval` law, but the dependent Hasse law has no analogous existing mathlib Hasse family/law after that representation bridge, so the parent re-aim NO gate does not fire here.

## Phase 7 — actionable verdict

**YES-but-generalise-first**, reasons LITERATURE-WEAKENING of coordinate representation and MODERN-IDIOM arbitrary embedding, both mechanically verified. This is not based on prerequisite absence or proof cost: the law is substantive disjoint-variable API, and the successful generalized theorem makes it applicable in any ambient variable type. Isolated actual mathlib candidates cover only part; the target needs new Hasse content. One determinant caller confirms concrete use.

Exact proposed upstream path: `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`, in namespace `MvPolynomial`, after foundational parent/rename compatibility. Proposed PR title: `feat(Algebra/MvPolynomial/HasseDeriv): differentiate products in a fresh variable`. Group with already accepted YES parent and coefficient/rename/disjoint-composition/degree-zero extraction API listed freshly from progress in [accepted-grouping.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/accepted-grouping.json); do not assert those are already upstream. The foundational Hasse PR can come first, followed by this compatibility addition. The file is a proposed new module, not an existing import.

Reviewer candidates from actual relevant recent pinned commits: Moritz Firsching (`hasseDeriv_map`, #42428) and Yaël Dillies (MvPolynomial coefficient API, #41427), evidence [reviewers.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/reviewers.json). These are candidates, not an assertion of availability or assignment.

Checklist: `/generalise Roth.hasseDeriv_rename_mul_aeval`; adopt verified freshCoordinate signature and choose mathlib naming; `/cleanup Roth/Separation.lean Roth.hasseDeriv_rename_mul_aeval`; stage parent imports and documentation; rerun full tests after real changes; migrate the sole caller and remove obsolete wrapper. This assessment makes no production edit or PR.

## Phase 8 — validation and evidence limits

All required phases complete; unresolved verification list empty. Root acceptance is pending independent review. Accepted native evidence is exclusively complete successful diagnostics, no warnings/errors, with standard axioms `propext`, `Classical.choice`, `Quot.sound`. Initial isolated counterexample normalization failure, freshCoordinate Option.elim-order failure, and initial sum-order guard coefficient normalization failure remain explicitly rejected; their recovered `sorryAx` does not contaminate accepted evidence. Exact preparations are distinct from actual executed versions. See [verification.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/verification.json), [copy-manifest.json](../evidence/Roth.hasseDeriv_rename_mul_aeval/copy-manifest.json) and portable read-only [validate.py](../evidence/Roth.hasseDeriv_rename_mul_aeval/validate.py). The validator checks current manifest hashes/bytes, links, canonical exact293 order and names, phase schema, all17 inputs and fresh mathlib/caller hashes, exact accepted native source/receipts, and the credential guard. Historical worker manifests never replace current manifest validation.
