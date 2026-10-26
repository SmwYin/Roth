# MvPolynomial.hasseDeriv_hasseDeriv — full fresh assessment

Verdict: **YES-add-as-is**. Root acceptance pending. This is the missing multivariate iterativity law for the canonical polynomial Hasse derivatives, matching `Polynomial.hasseDeriv_comp` while permitting arbitrary variable types. It belongs with the new multivariate Hasse API, rather than as a standalone addition without its parent definitions. No production changes are proposed by this assessment.

## 0. Baseline and scope

Freshly checked all 17 source/pin SHA256 values against the shared successful `lake build` manifest: 17/17 match. Shared build exit 0, 2467 jobs, no reported warnings/errors. Exact target is public theorem at `Roth/HasseDeriv.lean:175`; source contains no sorry or raised resource limit. Entire declaring module and entire direct external caller module `Roth/Index.lean` read. Full elaborated type and standard axioms are in accepted target native receipt. The private coefficient cocycle at line 153 is separately overview-prefilter SKIP only; its replay is evidence for this theorem, not a full standalone verdict for that private helper.

## 1. Mathematical content

For any commutative semiring R, arbitrary variable type σ and finitely supported natural multi-indices d,e, applying the e-th then d-th Hasse derivative equals the (d+e)-th Hasse derivative multiplied by ∏j binom(dj+ej,dj). This works in positive characteristic without factorial division. The scalar may vanish in R. On coefficients of X^f both sides have input coefficient at f+d+e; equality is the coordinatewise binomial cocycle, multiplied over the finite union of supports.

```lean
∀ {σ : Type u} {R : Type v} [CommSemiring R]
  (d e : σ →₀ ℕ) (P : MvPolynomial σ R),
  hasseDeriv d (hasseDeriv e P) =
    (hasseCoeff d (d + e) : R) • hasseDeriv (d + e) P
```

Project dependencies: hasseDeriv, hasseCoeff, coeff_hasseDeriv, private hasseCoeff_mul_hasseCoeff. Existing mathlib infrastructure supplies coefficient extensionality, coeff_smul, casts, support products, and Nat.choose_mul; it does not supply the multivariate normalization premise.

## 2. Preliminary checks

BIG: explicitly listed among module main results. One-line definition test n/a: theorem. Not glue/rfl and no inherited verdict. The short final coefficient rewrite hides a substantive finite-product binomial identity and the coefficient formula for the newly constructed operator.

## 3. Exhaustive literature

Exact requests and returned-response SHA256/byte counts are retained in `web-receipts.json` and `web5-receipt.json`; full web bodies are deliberately not archived.

| Channel | Actual query/access | Finding and locator |
|---|---|---|
| General web, specific | multivariate Hasse derivative composition binomial coefficient iterativity | Coordinate coefficient definition and positive-characteristic uses; no contrary normalization. |
| General web, abstract | Hasse Schmidt derivation iterative multivariate higher derivations divided power composition | Iterative higher-derivation language; formal-group action formulation. |
| General web, aliases/generality | canonical Hasse derivatives polynomial ring iteration positive characteristic | Characteristic-free coefficient formula; factorial conversion requires invertibility. |
| ChatGPT math | unavailable | n/a: ask_chatgpt_math is not exposed. No substitute claimed. |
| Local source | clean.tex123–152,571–587 | The exact product-binomial iteration formula appears in proof of Lemma index-of-derivative, lines581–582. `local-literature.txt` retains locators. |
| nLab | Hasse-Schmidt derivative; direct open | Search returned several-indeterminate definition over a commutative rig; direct page fetch failed unsupported XHTML400. [Page](https://ncatlab.org/nlab/show/Hasse-Schmidt+derivative). |
| nCatLab | Hasse-Schmidt derivation / formal group search and direct open | Same site hosts nLab; categorical HS action route investigated; direct derivation page fetch failed XHTML400, not treated as full access. |
| Stacks | site:stacks.math.columbia.edu Hasse derivations; higher derivations | No matching result returned; no absence inference. |
| MathOverflow | Hasse iterative; related jets search | Related 2023 question on higher derivations versus differential operators surfaced through [jets tag](https://mathoverflow.net/questions/tagged/jets?tab=Unanswered); does not prove canonical iterativity. |
| Recent arXiv, five-year window | Hasse iterative after2021-10-26; HS iterative2025 | [Dobrowolski–León Sánchez2506.19489](https://arxiv.org/abs/2506.19489), abstract read: local-algebra operator frameworks include iterative truncated HS operators. [Ganapathy2407.13604](https://arxiv.org/abs/2407.13604), abstract and revision date read: infinite-variable polynomial modules in characteristic p and categorifications of Hasse derivatives. Neither abstract establishes our exact theorem. |
| Primary abstract/classical bridge | [Hoffmann–Kowalski1212.5788 full HTML](https://arxiv.org/html/1212.5788) | Definitions2.1/2.2 distinguish higher Leibniz from the extra iterativity equation; introduction and §5 connect additive formal-group actions and several commuting HS systems. Full HTML accessible; Wrocław alternate PDF502 honestly recorded. |

Literature-standard target is canonical coordinate polynomial iterativity. A general HS family need not be iterative merely because it obeys higher Leibniz. An abstract iterative HS bundle would have the desired law as an axiom, leaving the substantive obligation to instantiate the canonical polynomial family. The current law proves that obligation.

## 4a–b. Generality

| Parameter/assumption | Check | Conclusion |
|---|---|---|
| σ universe/type | arbitrary Type*, independent coefficient universe; Finsupp indices | No finite, inhabited, decidable equality, Unique or nonempty assumption. Empty and infinite variable types supported. |
| R | CommSemiring; no additive inverses used | Characteristic-free; no domain, field, CharZero, nontriviality, factorial units or cancellation. |
| Semiring weakening | actual #check_failure MvPolynomial σ S under only Semiring S | Fixed parent interface needs commutative coefficients. Replacing representation by noncommutative monoid algebra is a separate development, not a mechanical weakening. |
| d,e | all finite natural multi-indices | No support disjointness or dominance restriction. Truncated subtraction safely handled by vanishing binomial weights. |
| P | arbitrary polynomial including zero | No degree or support hypothesis. |
| scalar | essential | ℕ, σ=Unit, d=e=single()1 and P=X² gives 2 on LHS and1 for unscaled Δ₂. Accepted native counterexample records exact proof. |

Generality: MAXIMALLY GENERAL for the canonical operator's pinned interface. No verified strengthening is being hidden as scope exclusion.

## 4c. Nine modern-idiom rows

| # | Diagnostic | Finding / concrete consequence |
|---|---|---|
| 1 | Typeclasses instead of hypotheses | Already CommSemiring and linear-map family; no extra predicate to bundle. |
| 2 | Filters/nets | No topology or convergence. |
| 3 | Universal property | Taylor additive coaction is conceptually apt and gives iterativity by comparing two translations, but constructing a formal-action bundle does not remove canonical coefficient normalization. No verified shorter replacement from existing coaction API. |
| 4 | Bundled substructures | Already bundled linear maps; no closed subset. Equivalent operator identity checked separately. |
| 5 | Fields → modules/semirings | Already generalized beyond classical fields/rings to CommSemiring. Noncommutative coefficient representation is not literal parent weakening. |
| 6 | Higher categories | Recent categorified Hasse work is adjacent, no necessary replacement of this algebraic identity. |
| 7 | Abstract index | σ arbitrary; ℕ exponents encode polynomial powers and binomial counts. Arbitrary additive monoid would lose choose and truncated-subtraction semantics. |
| 8 | Concrete-via-abstract | Named hasseDeriv disappears after one coefficient rewrite line (three occurrences of coeff_hasseDeriv; zero later occurrences). Diagnostic fires. Exact generic `weighted` theorem tested: any family L with coeff shift formula and weight cocycle has the same composition law. It retains both substantive normalization premises, with arbitrary w,c. This is a proof abstraction, not a demonstrated necessary public reorganization: the polynomial family remains the canonical concrete instantiation to prove, and no second verified downstream consumer requiring this bundle was found. |
| 9 | False-generalization guard | Reject removing iterativity from HS assumptions, replacing ℕ freely, or dividing factorials in characteristic p. The weighted diagnostic preserves meaning because its explicit cocycle is required; it is not claimed to follow from higher Leibniz alone. |

Formal modern-idiom verdict: **no material public modernization established**. Q8=yes is a proof diagnostic; the verified candidate has signature shape below, but no material mathematical reorganization of this public canonical law is established.

```lean
theorem weighted (L : (σ →₀ ℕ) → MvPolynomial σ R →ₗ[R] MvPolynomial σ R)
    (w c : (σ →₀ ℕ) → (σ →₀ ℕ) → R)
    (hL : ∀ d f P, (L d P).coeff f = w d (f + d) * P.coeff (f + d))
    (hc : ∀ f d e, w d (f + d) * w e (f + d + e) =
      c d e * w (d + e) (f + (d + e))) (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    L d (L e P) = c d e • L (d + e) P
``` Do not force a new arbitrary-weight API solely to restate a coefficient extensionality proof. This is not a cost-based choice.

## 4.5. Infrastructure risk

n/a — theorem introduces no definition, class, instance, reduction rule, universe-constraining construction or coercion. Accordingly each of the six risk rows (typeclass diamond, reducibility leak, noncanonical unfolding, instance priority, universe issue, coercion ambiguity) is n/a for this declaration. Parent definition risks are not inherited as theorem verdicts.

## 4.6. Five strategy rows

| # | Question | Result |
|---|---|---|
|1|Topology ε–δ vs filters|No topology.|
|2|Elements vs ideals/submodules|Coefficient extensionality is canonical for this polynomial equality; operator equality is equivalent, not a shorter algebraic subobject argument.|
|3|Sequences vs nets|No analysis.|
|4|Construction vs universal property|Taylor coaction offers conceptual organization; no existing abstract action theorem supplies the canonical instance.|
|5|Missing helper API|Yes: multivariate coefficient law and finite-support product choose cocycle. The cocycle may remain private support for this API; independent raw proof constructs it explicitly from Nat.choose_mul.|

MATHLIB-IDIOMATIC: coefficient comparison plus a scalar cocycle. No proof-strategy rewrite prerequisite. Group the coefficient interface and operator with this composition theorem; do not count new helpers as existing mathlib calls.

## 5. Actual five-method mathlib search

| Method | Current / literature / abstract forms | Actual outcome |
|---|---|---|
| Finder | multivariate Hasse composition / iterative HS / weighted coefficient cocycle | Polynomial.hasseDeriv_comp; LaurentSeries.hasseDeriv_comp; abstract query also unrelated cochains/vertex operators. |
| Loogle | Polynomial.hasseDeriv,LinearMap.comp; hasseDeriv,comp / Finsupp.prod,Nat.choose | Univariate and Laurent analogues; no abstract product hit. |
| LeanSearch | multivariate composition / iterative divided powers / additive formal group | Univariate API; divided powers algebra constructors; ordinary mkDerivation. None has multivariate canonical iteration signature. |
| rg | untruncated qualified-name/decl searches over pinned mathlib; variants in MvPolynomial, Polynomial, LaurentSeries | No multivariate target or HS bundle text match. Polynomial154 and LaurentSeries156/165 exact analogues. Complete commands/stdout retained. |
| local | hasseDeriv_hasseDeriv / hasseDeriv_comp / HasseSchmidt | Project target and univariate analogues; abstract empty; index explicitly unavailable. Fallback results do not establish absence. |

Pinned `Polynomial.hasseDeriv_comp` is over Semiring R and natural k,l, as equality of univariate linear maps with natural-number smul. It is a genuine analogue, not a direct arbitrary-σ specialization. Laurent series uses integer exponents and one variable, so also not a direct replacement. Compiled `#check_failure` controls establish that the target and parent names are absent in the mathlib-only imports. The raw exact? negative guards were removed before execution; only a positive exact? control ran. No failed exact? search is claimed for this target.

## 5.5. Statement shape (three checks)

1. Normal form: RHS combined order with scalar is the useful normalization, agreeing with Polynomial.hasseDeriv_comp. No competing existing multivariate normal form found.
2. Syntactic generality: a linear-map composition equality is compiled via LinearMap.ext and the pointwise law. It helps operator algebra but pointwise application directly supports both current consumers. Keep current theorem; consider `_comp` naming/operator sibling in cleanup, no mathematical restatement required.
3. Superfluous arguments: σ,R,d,e,P all used; only typeclass CommSemiring fixes the parent interface. No proof hypotheses to drop. Nat-smul versus cast-R-smul is equivalent scalar packaging, not stronger generality.

Statement-shape verdict: normal form OK; syntactic generality OK; superfluous arguments NONE; overall SHIP-AS-STATED.

## 6.0. Explicit caller and inline audit

| Caller | Exact site | Use and action |
|---|---|---|
| MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint | HasseDeriv187 | Rewrite nested derivative, prove factor1 from disjoint supports, simplify cast1/one_smul. Preserve theorem invocation when upstream import replaces local API. This caller is not independently assessed here. |
| Roth.index_sub_weight_le_index_hasseDeriv | Index113 | Rewrite nested derivative inside nonzero evaluation, turn smul into constant multiplication, extract nonzero combined-order evaluation. Preserve invocation; adjust name only if upstream operator `_comp` form chosen. |

Within declaring file explicit uses1; project internal use count excluding declaring file1, external-to-file distinct files1, total explicit invocations2. Searches distinguish definition/docstring/longer `_of_disjoint` names from exact invocation. Separation156 calls the disjoint theorem, not this theorem directly. All source-level callers are covered; this is not an opaque kernel/simp dependency closure. No additional inline full binomial-composition derivation found; pderiv_hasseDeriv and the scalar successor helper encode only the single-coordinate first-order consequence, not another full caller. Native caller verification is scoped algebraic contexts, not a complete rebuild of downstream Index.

## 6. Composition experiments

The project coefficient replay closes by extensionality plus rewrites, but depends on project coeff_hasseDeriv and the private cocycle replay: these are new API and cannot justify NO-composable. Independently expanded raw delta uses only mathlib imports and reconstructs its coefficient identity by monomial/add induction, a finite-support product cocycle from Nat.choose_mul, and iterativity. This is substantive proof, not ≤3 existing-call composition or raw closing simp. General weighted normalization still needs an explicit weight-cocycle premise. Univariate composition cannot immediately handle arbitrary σ without a new commuting coordinate-operator product/Taylor transport development.

Conclusion: NOT-COMPOSABLE from verified existing pinned mathlib calls. Search results and the missing-name controls are bounded evidence, not proofs of universal absence.

## 7. Actionable verdict

**YES-add-as-is**, grouped with the canonical multivariate Hasse API. Concrete gap: mathlib has univariate `Polynomial.hasseDeriv_comp` but no arbitrary-variable, finitely supported multi-order polynomial iterativity theorem or canonical multivariate Hasse operator providing its normalization premises. This law is useful beyond Roth in characteristic-p polynomial multiplicity, higher derivations and Taylor-coefficient calculations. It belongs in mathlib proper, not Archive or an exclusively Roth module.

Proposed file: `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`.
Proposed PR title: `feat(Algebra/MvPolynomial/HasseDeriv): add the Hasse derivative composition rule`.
Group with already accepted YES parent/coefficient API: hasseDeriv, coeff_hasseDeriv, hasseDeriv_map, hasseDeriv_rename (their prior verdicts are grouping context only; this assessment does not inherit them). Keep helper scalar cocycle private unless separate API assessment warrants public exposure. The disjoint-support theorem remains next/unassessed.

Checklist: `/generalise MvPolynomial.hasseDeriv_hasseDeriv`; `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_hasseDeriv`; then pre-submit for the grouped module, including `_comp` naming/operator-sibling choice. Reviewer candidates and recent relevant commit locators are recorded separately. No user approval is needed to finish this read-only assessment.

## 8. Verification and limits

Accepted exact executed sources and complete native receipts are enumerated in `verification.json`; current copy manifest hashes all supporting evidence. Root independently reviews before publication. All accepted results must be success=true, partial=false, timeout=false, no errors/warnings, no sorryAx, only propext/Classical.choice/Quot.sound. Portable validator supports scratch and integrated report paths and validates the current copy-manifest, never substitutes historical worker-copy-manifest.

Limitations: unavailable ChatGPT math; nLab direct XHTML and alternate PDF failures; local symbol index unavailable; external search indexes may differ from pinned revision; current arXiv abstracts only; caller contexts scoped, no claim of full downstream rebuild. These do not leave verification unresolved after accepted native receipts. Initial raw attempt needed a final rfl after cocycle rewriting; extra attempts repaired coefficient-field syntax and explicit single-index subtraction normalization in the counterexample. Rejected exact attempts are retained separately and never counted as accepted verification. Negative exact? guards in the proposed draft were not run and are not evidence.
