# MvPolynomial.coeff_taylor — full mathlibable assessment

Verdict: **YES-add-as-is** for the mathematical coefficient identity, grouped with multivariate Hasse derivatives. The missing API is the bridge between the binomial-weighted multivariate Hasse operator and coefficient extraction after substitution `X ↦ X + C α`. Existing `Polynomial.taylor_coeff` proves the one-variable case; it does not cover arbitrary variable types. The proposed theorem can be stated directly against existing `MvPolynomial.aeval`, so this assessment does not resolve the separate BORDERLINE choice about adding a named multivariate `taylor` endomorphism.

## Phase 0 — baseline and scope

The reusable baseline is clean: `lake build` exited 0 with 2467 jobs and no warnings/errors. All 17 source/pin hashes were freshly recomputed and match the baseline manifest. Target resolves at `Roth/Taylor.lean:134`, is a public theorem, has no `sorry`, and is a main result in the declaring module's documentation. Entire Taylor, HasseDeriv and Index modules were read. No production, Git or overview mutations were made by this assessment.

[Baseline](../evidence/MvPolynomial.coeff_taylor/baseline-build.txt), [fresh hashes](../evidence/MvPolynomial.coeff_taylor/input-hash-check.json), [declaring module](../evidence/MvPolynomial.coeff_taylor/Taylor-module.lean.txt), [caller module](../evidence/MvPolynomial.coeff_taylor/Index-module.lean.txt).

## Phase 1 — exact content and proof

For every commutative semiring R, arbitrary set of variables σ, point α and finitely supported natural exponent vector d, the coefficient of X^d in P(X+α) equals the value at α of the d-th Hasse derivative of P. This is an identity of formal polynomials, not an assertion about equality of polynomial functions. It works in positive characteristic, with zero divisors, over the zero semiring, and without finiteness or decidable equality assumptions on σ.

Full native type (universes independently polymorphic):

```lean
∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R]
  (α : σ → R) (d : σ →₀ ℕ) (P : MvPolynomial σ R),
  (MvPolynomial.taylor α P).coeff d =
    MvPolynomial.eval α (MvPolynomial.hasseDeriv d P)
```

The source proof uses polynomial additive induction. The additive branch follows from additivity of translation, coefficient extraction, Hasse differentiation and evaluation. The monomial branch uses finite-support induction on exponents, the univariate binomial coefficient formula, separation of a chosen variable from the remaining variables, and the multiplicative binomial factor. This is not merely linear-map extensionality: the monomial normalization premise contains the mathematical content.

The independent native replay uses the separately verified public scratch monomial proof and polynomial induction. Its direct constant audit contains no `MvPolynomial.coeff_taylor`; the monomial replay's direct constants likewise avoid it. Private source helpers 58–62 have SKIP visibility assessments, not public NO judgments. They remain genuine proof ingredients. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur.

[Exact executed native document](../evidence/MvPolynomial.coeff_taylor/native-target-executed.lean.txt), [complete native success and direct constants](../evidence/MvPolynomial.coeff_taylor/native-target-success.json).

## Phase 2 — preliminary checks

BIG: Taylor's coefficient theorem is explicitly listed among the module's main results and is a named classical theorem. The definition-only one-line test is n/a because this is a theorem. Its short top-level induction is not evidence of trivial composition: it delegates the substantial monomial calculation.

## Phase 3 — exhaustive literature

Every named channel was attempted. The command's informal nine-channel label does not replace its actual channel table. Search batch responses are evidence of the batch, not evidence that each query individually returned a hit. Full copyrighted web bodies were not persisted; metadata preserves exact requests, response hashes/bytes, returned URLs and concise original summaries.

| Channel | Actual query/access | Finding |
|---|---|---|
| General web, specific | `multivariate polynomial Taylor expansion Hasse derivatives coefficient translation` | Classical multivariate Taylor coefficient law and computational applications. |
| General web, general | `Hasse Schmidt derivation Taylor homomorphism arbitrary commutative ring coefficients` | Hasse–Schmidt families package higher coefficients as a homomorphism; characteristic-free algebraic context. |
| General web, aliases | `divided derivatives multivariable Taylor formula positive characteristic` | Divided/Hasse derivatives avoid factorial division; ordinary derivative quotient is not universally equivalent. |
| ChatGPT mathematical MCP | unavailable | n/a: optional `ask_chatgpt_math` capability unavailable; no opinion fabricated. |
| Local source | `clean.tex`, §4, lines501–532 and549–558 | Polynomial expansion proved by linearity and monomials; explicit translated-coefficient identity in implementation note. |
| nLab | `site:ncatlab.org/nlab/show Hasse Schmidt derivation Taylor`; targeted `site:ncatlab.org/nlab/show "Hasse" "Taylor"`; direct Hasse-Schmidt derivative page | Search mainly gave adjacent or false Hasse–Weil hits. Direct page failed HTTP400 unsupported XHTML. No claim its body was read. |
| nCatLab/categorical context | `site:ncatlab.org Taylor polynomial Hasse derivative` | Brief check found no exact categorical replacement. Homomorphism/universal-property packaging is relevant context, not a theorem about every algebra homomorphism. |
| Stacks | `site:stacks.math.columbia.edu divided power Taylor differential operators`; direct tag09CH | §10.133 defines finite-order differential operators and principal parts; useful broader language but does not replace this coordinate coefficient identity. |
| MathOverflow | `site:mathoverflow.net Hasse derivative multivariate Taylor expansion` | Recentring/tangent-cone and Hasse derivative discussions; no stronger canonical statement needed here. |
| recent arXiv | `site:arxiv.org Hasse Schmidt Taylor polynomial multivariate 2021 2022 2023 2024 2025 2026`; targeted paper-title search | First broad search mixed older papers. Targeted 2022 paper is inside 2021-10-27–2026-10-27 window; primary HTML §3.2 Definition3.4 and Property3.5 inspected. |

The clearest independent primary source is Bhargava–Ghosh–Guo–Kumar–Umans, [Fast Multivariate Multipoint Evaluation Over All Finite Fields](https://arxiv.org/html/2205.00342v1), §3.2 Definition3.4: Hasse derivatives are coefficients in formal translation over a commutative ring. Property3.5 identifies the binomial-weighted monomial expansion. Evaluating the original-variable block at α produces the assessed law; that last step is this assessment's algebraic inference. The source's finite-variable presentation extends here to arbitrary σ because every polynomial and multi-index has finite support. The local manuscript states the real finite-variable specialization, while the implemented theorem already removes those unnecessary restrictions.

[Web requests/metadata0](../evidence/MvPolynomial.coeff_taylor/web-0.json), [named channels](../evidence/MvPolynomial.coeff_taylor/web-3.json), [MO/arXiv broad](../evidence/MvPolynomial.coeff_taylor/web-6.json), [nLab follow-up](../evidence/MvPolynomial.coeff_taylor/web-N.json), [2022 record](../evidence/MvPolynomial.coeff_taylor/web-A.json), [direct accesses](../evidence/MvPolynomial.coeff_taylor/web-O.json), [primary locators](../evidence/MvPolynomial.coeff_taylor/web-L.json).

Literature summary: standard names are algebraic Taylor formula, Hasse/divided derivative coefficient characterization, and the polynomial example of Hasse–Schmidt derivations. Field, characteristic-zero, analyticity, degree bounds and finite total variable sets are unnecessary for this individual coefficient identity. Universal formal translation is an equivalent organizing characterization, not grounds for replacing the theorem by an arbitrary linear/homomorphism axiom.

## Phase 4 — all parameters and generality

| Parameter/hypothesis | Essential role and generality |
|---|---|
| `σ : Type u` | Arbitrary universe and variable type already allowed; no Fintype, Unique, Nonempty or DecidableEq assumption to drop. Empty σ is valid. |
| `R : Type v` | Arbitrary independent coefficient universe; no numeric specialization. |
| `[CommSemiring R]` | Supports existing multivariate polynomial, algebra substitution, evaluation and Hasse interfaces. No subtraction, field, domain, order, characteristic or nontriviality assumptions. Semiring-only old spelling is blocked by fixed parent interfaces; this is distinguished from any redesigned noncommutative representation. |
| `α : σ → R` | Any point, including zero coordinates; no regularity/nonvanishing conditions. |
| `d : σ →₀ ℕ` | Any monomial index, including0 and orders above degree; finite support represents the polynomial monomial, not an unnecessary restriction on variables. |
| `P : MvPolynomial σ R` | Arbitrary polynomial, including0; no support or degree hypotheses. |

Generality verdict: maximal for these existing semiring-valued interfaces. Root checked Semiring-only parent failures; these are elaboration boundary checks, not mathematical counterexamples to all conceivable noncommutative formulations. A coefficient-map extension with `f : R →+* S`, `α : σ → S`, has RHS `eval₂ f α (hasseDeriv d P)` and LHS `coeff d (taylor α (map f P))`; it follows from the same theorem plus `hasseDeriv_map` and `eval₂_eq_eval_map`. This useful extension does not require weakening an existing hypothesis and does not make the core theorem a bad upstream entry point. No generalise-first weakening is claimed.

### Nine modern-idiom rows

| # | Diagnostic | Answer and downstream consequence |
|---|---|---|
|1|Typeclasses instead of preambles|Already `[CommSemiring R]`; no manual structure predicate.|
|2|Filters instead of sequences/metric language|No: finite algebraic identity with no limit.|
|3|Universal property instead of construction|Translation already uses the free algebra's `aeval`; Hasse–Schmidt packaging gives a future organizing view, but does not supply the coefficient computation without proving its normalization.|
|4|Bundled substructures|No subset-closure construction. Equivalent equality of bundled linear functionals is checked, and composes via `LinearMap.comp`; pointwise rewrite form better serves all current callers.|
|5|Weaker hierarchy than fields/vector spaces|Already characteristic-free commutative semiring; no linear-space-only constraint. Fixed parent Semiring guard recorded.|
|6|Higher categories|No categorical coherence needed for coefficient identity.|
|7|Generalize concrete indices|Natural exponents define ordinary polynomial monomials. Replacing by arbitrary monoid indices loses binomial coefficients and changes the object. σ itself already arbitrary.|
|8|Concrete-via-abstract adversarial diagnostic|No specialized named witness: σ,R,α,d,P arbitrary. Top-level proof has zero bare `taylor`/`hasseDeriv` occurrences after the statement, but delegates to a monomial helper that uses both throughout. Thus this is a proof decomposition, not evidence that any linear map can replace Hasse derivatives. Direct aeval spelling and bundled equality preserve exactly the same theorem.|
|9|False-generalization guard|Reject removing formal polynomial content in favor of polynomial-function extensionality (finite fields distinguish these); reject ordinary derivatives divided by factorials without invertibility; reject arbitrary additive exponent groups or arbitrary homomorphisms with no normalization premise. Accepted equivalent forms preserve content.|

Modern-idiom verdict: no compulsory semantic modernization. Direct `aeval` spelling avoids requiring a new named translation def; bundled linear equality is a derived companion, not a stronger theorem.

### Five proof-strategy rows

| # | Question | Answer |
|---|---|---|
|1|Topology ε–δ versus filters|n/a, no topology.|
|2|Elements versus ideal/submodule inclusions|No ideal-inclusion conclusion; coefficient equality genuinely evaluates linear functionals. Polynomial additive induction is appropriate.|
|3|Analysis sequences versus nets|n/a, no analysis.|
|4|Explicit categorical construction versus universal property|Existing `aeval` already supplies substitution by the free-algebra universal property; its coefficient calculation remains nontrivial.|
|5|Missing helper API that should exist|The separation-of-one-variable coefficient helper and multivariate binomial normalization are reusable proof machinery. Their private visibility does not imply triviality or public NO. Evaluate helper names/public scope during cleanup; no cost-based downgrade.|

Strategy verdict: MATHLIB-IDIOMATIC at the mathematical level; preserve finite monomial induction or use `linearMap_ext` with the actual monomial premise. Univariate `taylor_coeff` plus iterated polynomial equivalences is another possible proof strategy, but requires finite variable restriction, transport and multivariate Hasse compatibility; it is not a three-call existing proof for arbitrary σ.

Phase4.5 infrastructure risks: n/a — theorem introduces no definition, class or instance. This justifies n/a for each of typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priorities, universe infrastructure and coercion ambiguity; the separate parent-definition risks are not reassessed as theorem risks.

## Phase 5 — five actual methods × three forms

All four API-backed search tools ran with exact requests and complete raw responses. The fifth method was full untruncated pinned-source `rg`. Current: translated polynomial coefficient; literature: multivariate Hasse/Taylor characterization; abstract: coefficient functional composed with substitution versus evaluation composed with Hasse linear map.

| Method | Current | Literature | Abstract |
|---|---|---|---|
|Lean-Finder|Univariate `Polynomial.taylor_coeff` and related results|Same univariate main candidate|Same univariate candidate, not arbitrary-variable bridge|
|Loogle|Actual `"coeff", "taylor"` query: univariate results|Actual `"hasseDeriv"`: univariate Hasse API|Actual `"MvPolynomial.coeff", "MvPolynomial.aeval"`: empty|
|LeanSearch|Univariate `Polynomial.taylor_coeff`|Univariate coefficient law|Adjacent Laurent-series/Hasse results; no replacement|
|rg pinned mathlib|Univariate Taylor laws; no full-name multivariate theorem|HasseDeriv/Taylor univariate source inspected|`lcoeff`, `linearMap_ext`, `aeval` building blocks; coefficient normalization still missing|
|local name index|Finds this project target/helpers (not mathlib evidence)|Finds project/scratch/archive hits and unrelated Laurent series|Finds scratch/project coefficient helpers; filter by path before attribution|

[Current rg](../evidence/MvPolynomial.coeff_taylor/rg-current.json), [literature rg](../evidence/MvPolynomial.coeff_taylor/rg-literature.json), [abstract rg](../evidence/MvPolynomial.coeff_taylor/rg-abstract.json), [full-name rg](../evidence/MvPolynomial.coeff_taylor/rg-full-name.json). Raw tool receipts are listed in the [verification index](../evidence/MvPolynomial.coeff_taylor/verification.json).

Pinned positive candidate:

```lean
Polynomial.taylor_coeff {R} [Semiring R] (r : R) (f : Polynomial R) (n : ℕ) :
  (Polynomial.taylor r f).coeff n =
    Polynomial.eval r (Polynomial.hasseDeriv n f)
```

Located `Mathlib/Algebra/Polynomial/Taylor.lean:68`. Root natively checked the full explicit argument order and replayed its exact application. It requires a univariate input polynomial and natural index; neither arbitrary σ nor a multivariate exponent is accepted. One-variable `uniqueAlgEquiv` bridges elsewhere in the project do not establish the full theorem for arbitrary σ. LaurentSeries and PowerSeries Hasse operators act on different representations and likewise do not directly prove the target. Search/index revisions can differ; failed or empty search alone is not a proof of absence.

[Positive-candidate native source](../evidence/MvPolynomial.coeff_taylor/native-univ-executed.lean.txt), [success](../evidence/MvPolynomial.coeff_taylor/native-univ-success.json). Rejected root attempts with incorrect implicit argument guesses and a command whitespace warning are separately archived and never counted as accepted proof evidence.

## Phase 5.5 — statement shape

Normal forms compared: (1) translated-polynomial coefficient equals evaluated Hasse derivative; (2) direct `aeval (X+Cα)` spelling; (3) equality of linear functionals `(lcoeff R d).comp (taylor α).toLinearMap = (aeval α).toLinearMap.comp (hasseDeriv d)`. A fourth universal two-variable-block translation theorem is the literature characterization and could be proved as companion API. The first and second have the desired evaluated Hasse expression on the RHS and match `Polynomial.taylor_coeff`; source name `coeff_taylor` versus univariate `taylor_coeff` is a cleanup naming decision.

Syntactic-generality experiments: root checked the direct aeval version, bundled functional equality and the eval₂ coefficient-map extension. The pointwise equality remains the chosen public rewrite form because callers rewrite coefficients and support membership directly; bundled equality would first require applying to P. No superfluous argument or typeclass exists: σ/R determine the objects, α the point, d the coefficient, P the polynomial, and CommSemiring the current interfaces. No Fintype/DecidableEq/Nontrivial restriction is accidentally inherited.

[Actual extra-form native success](../evidence/MvPolynomial.coeff_taylor/native-extra-success.json), [exact executed forms](../evidence/MvPolynomial.coeff_taylor/native-extra-executed.lean.txt). Statement-shape verdict: SHIP-AS-STATED mathematically. If a named `taylor` definition is not upstreamed, ship the equivalent existing-`aeval` statement. This is a definitional respelling, not a claimed generality improvement. Unlike the command’s Class5 foundational refactor, it changes neither the Hasse operator nor its coefficient representation, requires no caller-wide foundational migration, and is directly checked by the same proof term. Thus the parent packaging choice does not force BORDERLINE for this independent coefficient law.

## Phase 6 — complete callers and composition

Five explicit source references occur across four caller declarations. Three references are external to Taylor, in one distinct external file. Two are in the declaring file. Documentation mentions and private helper names are excluded. The target is not tagged simp; implicit simp/kernel closure is not equated with this explicit inventory.

| Source location | Caller and actual use | Replay |
|---|---|---|
|Taylor173|`degreeOf_taylor_le`: replace nonzero translated coefficient by nonzero evaluated derivative to contradict degree bound|full original body with independent replay substituted|
|Taylor202|`eq_sum_box_hasseDeriv`: coefficientwise reconstruction in bounded box|full original body, including ring inverse-translation step|
|Index64|private `mem_support_taylor_iff`: support membership iff evaluated derivative nonzero|full equivalence|
|Index153|`index_eq_weightedOrder_div`: power-series coefficient witness gives index upper bound|full enclosing declaration|
|Index158|same caller: derivative nonvanishing supplies weighted-order lower-bound witness|same full declaration|

[Exact caller grep](../evidence/MvPolynomial.coeff_taylor/rg-callers.json), [inline audit](../evidence/MvPolynomial.coeff_taylor/rg-inline.json), [caller probes](../evidence/MvPolynomial.coeff_taylor/caller-probes.lean.txt), [actual native caller success](../evidence/MvPolynomial.coeff_taylor/native-callers-success.json), [actual caller execution](../evidence/MvPolynomial.coeff_taylor/native-callers-executed.lean.txt). Root qualified `MvPolynomial.mem_support_iff` in the Roth namespace to resolve the existing global `Polynomial` ambiguity; the initial rejected caller attempt is separate. The inline audit found the separate univariate `index_unique` calculation via `Polynomial.taylor_coeff` and project `uniqueAlgEquiv_hasseDeriv`; this is only a Unique-variable specialization, not a bypass/rederivation of the arbitrary-variable theorem. No full multivariate inline rederivation found.

Composition attempt1: `Polynomial.taylor_coeff` — verified true and useful univariate law; fails as full replacement because representations and indices differ. Iterating it requires new transport/induction proofs.

Attempt2: `MvPolynomial.linearMap_ext` or `LinearMap.ext` — these reduce equality to monomials/inputs and leave precisely the coefficient-normalization premise. Root's independently checked replay uses a newly proved project/scratch monomial helper; that helper is not existing mathlib API and cannot count as one of three calls.

Attempt3: mathlib-only expanded finite-sum target after unfolding substitution/coefficients. Root actually ran two unclosed mathlib-only examples using the full approved11-import prefix and guarded missing project target. The corrected pinned expansion uses `MvPolynomial.eval₂_eq`; simp leaves the coefficient of a product of translated powers inside a sum, and default `exact?` reports that it cannot close the goal. Neither attempt times out or raises heartbeats. The earlier preparation attempt guessed nonexistent `MvPolynomial.eval₂_eq_sum` and is separately rejected, not counted as a mathematical obstruction. These failures do not prove absence; they measure the tested routes. The successful full project replay plus monomial normalization demonstrates a real proof. The explicit mathematical obstacle remains coefficient extraction through a product of translated powers with disjoint variable supports.

[Actual composition residual and default search failures](../evidence/MvPolynomial.coeff_taylor/native-composition-rejected.json), [exact executed composition examples](../evidence/MvPolynomial.coeff_taylor/native-composition-rejected.lean.txt). Conclusion: NOT-COMPOSABLE from existing mathlib in ≤3 calls on the evidence. No successful closing `simp [defs]` composition is claimed; if one were found, the command would require BORDERLINE handling. Prior accepted YES Hasse API is proposed new infrastructure, not existing pinned mathlib, and does not by itself decide this theorem's Taylor fit.

## Phase 7 — actionable verdict

**YES-add-as-is.** This law connects two useful computational views of a multivariate polynomial: the coefficient/support view after translation and the binomial Hasse derivative evaluated at a point. The project uses that bridge for degree control, finite Taylor reconstruction, and comparison of weighted order with the Roth index. Independently, the primary 2022 computational-algebra source uses the same characterization over commutative rings, including positive characteristic. The theorem extends existing univariate mathlib Taylor API to arbitrary variable sets without adding unnecessary degree or finite-variable hypotheses.

Specific missing API anchor: pinned `Polynomial.taylor_coeff` is the direct univariate analogue, while pinned `MvPolynomial.aeval`, `lcoeff` and `linearMap_ext` provide only the substitution and linear-functional infrastructure. No existing multivariate normalization theorem was found or natively demonstrated. The new proof supplies exactly that missing bridge; private helper visibility and a short outer induction do not remove its content.

Proposed upstream file: **`Mathlib/Algebra/MvPolynomial/Taylor.lean`**, importing the proposed **`Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`** from the already accepted public Hasse package. Proposed PR title: **feat(Algebra/MvPolynomial): Taylor coefficients as evaluated Hasse derivatives**. Group with accepted YES declarations `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_rename`, and the accepted composition/degree API as appropriate for staged PR size; [fresh accepted inventory](../evidence/MvPolynomial.coeff_taylor/accepted-grouping.json) is authoritative. Do not list parent `taylor` or private helpers58–62 as accepted public YES declarations.

Upstream sequence:

1. Run `/generalise MvPolynomial.coeff_taylor` as a final regression of the semiring/arbitrary-variable floor; retain core law and optionally add the verified eval₂ companion.
2. Resolve the separately assessed naming choice for `MvPolynomial.taylor`. If it stays local, state this theorem using existing `aeval`; do not block or misclassify the coefficient theorem on that choice.
3. Run `/cleanup Roth/Taylor.lean MvPolynomial.coeff_taylor` over the extracted proof and helpers, decide whether naming should align with `Polynomial.taylor_coeff`, and minimize imports. Preserve mathematical normalization in the proof; do not pretend scratch helpers are mathlib replacements.
4. Pick Yaël Dillies (pinned recent MvPolynomial coefficient refactor `631b214f7c`) as a relevant reviewer; Moritz Firsching (`334438dace`) and Aaron Liu (`274ed6d67d`, Eval API cleanup) are alternatives. Root ran fresh read-only history, preserved in [reviewer receipt](../evidence/MvPolynomial.coeff_taylor/reviewer-history.json); prioritize these human algebra API contributors over automation/bot-only changes. Recheck then-current upstream duplication before opening the PR.
5. Re-run exact theorem/caller checks in the intended upstream import context and full required checks. No production change or PR has been made by this read-only assessment.

Alternative local destination while the companion Hasse PR is pending: keep `Roth/Taylor.lean`; it is currently the appropriate dependency boundary. There is no recommendation to delete the theorem or inline its real monomial proof into all five references.

## Phase 8 — consolidated handoff

Assessment complete, root acceptance pending. Four accepted native receipts verify the original theorem and independent full replay, the pinned one-variable analogy, every explicit caller declaration, and the equivalent/direct/bundled/base-change forms. Rejected experiments remain separate from accepted proof evidence. Verification limitations are search coverage and future upstream API/reviewer decisions, not unresolved native checks. Parent `taylor` naming remains its own independently assessed question; it does not invalidate the existing-`aeval` statement verified here.

[Assessment](../evidence/MvPolynomial.coeff_taylor/assessment.json), [verification index](../evidence/MvPolynomial.coeff_taylor/verification.json), [portable read-only validator](../evidence/MvPolynomial.coeff_taylor/validate.py), [current copy manifest](../evidence/MvPolynomial.coeff_taylor/copy-manifest.json).
