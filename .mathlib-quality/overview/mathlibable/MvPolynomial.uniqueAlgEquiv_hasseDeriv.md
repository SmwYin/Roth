# MvPolynomial.uniqueAlgEquiv_hasseDeriv

**BORDERLINE-needs-human.** The single-variable compatibility is standard, but the complete identity reduces to existing linear-map extensionality and a closing definition-expanding simp. Phase 6b calls this a review decision about the public API. No production Lean source or pin is changed.

## Phase 0: baseline

The shared `lake build` completed successfully (2467 jobs, exit 0). All 17 source/pin SHA256 values freshly match its input manifest; [fresh checks](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/input-check.json), [manifest](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/input-manifest.json), [build receipt](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/baseline-build.txt). This is baseline reuse, not a new whole-project build. The public theorem resolves at `Roth/HasseDeriv.lean:266`, has no sorry, and its module develops multivariate Hasse derivatives over arbitrary commutative semirings. The entire declaring module and entire explicit-caller module were read. [Source hashes](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/source-hashes.json).

## Phase 1: mathematical content

If the variable type has exactly one element, identify its multivariate polynomial algebra with the univariate polynomial algebra by sending the unique variable to T. This identification commutes with every Hasse derivative: order n in the unique coordinate becomes the univariate order n derivative. Both sides send the monomial aT^k to a binom(k,n) T^(k-n), including zero order and orders above the degree, in every characteristic.

The elaborated statement is universe-polymorphic in independent `σ` and `R`, with `[CommSemiring R] [Unique σ]`, `(n : ℕ)`, `(P : MvPolynomial σ R)`:

```lean
uniqueAlgEquiv R σ (hasseDeriv (R := R) (Finsupp.single (default : σ) n) P) =
  Polynomial.hasseDeriv n (uniqueAlgEquiv R σ P)
```

The source proof takes coefficients, uses the two Hasse coefficient formulas and `coeff_uniqueAlgEquiv`, then normalizes singleton addition and the binomial product. The multivariate `hasseDeriv`, `hasseCoeff`, and `coeff_hasseDeriv` are project API; the univariate derivative and equivalence are mathlib API. [Full source](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/target-source.lean.txt).

## Phase 2: preliminary checks

BIG: the module explicitly lists this theorem in Main results as univariate compatibility. The one-line-definition test is n/a for a theorem. This is neither definitional equality nor an inherited glue lemma.

## Phase 3: exhaustive literature

[Web receipts](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/web-receipts.json) retain exact requests, returned-response SHA256/bytes and access status; full article/search bodies are deliberately not retained. The following are original summaries, not quotations.

| Channel | Actual query / primary locator | Finding |
|---|---|---|
| Web specific | `Hasse derivatives multivariate polynomial one variable binomial coefficient Hasse Schmidt` | [Bhargava–Ghosh–Guo–Kumar–Umans](https://doi.org/10.1145/3652025), §3.2 Def. 3.4 and Prop. 3.5: Hasse derivatives are coefficients of translation and have the binomial monomial formula. The one-variable identification preserves these coefficients. |
| Web general | `Hasse Schmidt derivations polynomial algebra change of coordinates single variable` | [Joints of Varieties](https://link.springer.com/article/10.1007/s00039-022-00597-5), §4.1 equation (4.1), characterizes Hasse derivatives by Taylor expansion and discusses affine coordinate transformations. This suggests broader covariance, not commutation with an arbitrary algebra equivalence without coordinate data. |
| Web aliases | `Hasse derivative divided derivative polynomial positive characteristic binomial definition` | [Goresky–Klapper, §15.4.1](https://www.math.ias.edu/~goresky/pdf/algebraic0.pdf) defines the binomially normalized derivative; factorial division alone fails in positive characteristic. |
| ChatGPT math | Standard form, generality and historical formulation | n/a: `ask_chatgpt_math` is absent from available tools. No second opinion is invented. |
| Local references | `clean.tex:122–155`, Hasse/Delta/derivative grep | Defines monomial-normalized operators and explicitly points to univariate `Polynomial.hasseDeriv` as model. The semiring setting is explicit. [Local source](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/clean-source.tex.txt). |
| nLab | `site=ncatlab.org/nlab Hasse Schmidt derivation`; [Hasse-Schmidt derivative](https://ncatlab.org/nlab/show/Hasse-Schmidt+derivative) | Indexed text presents one and several indeterminates over commutative rigs and linear extension. A direct page open failed: unsupported `application/xhtml+xml`. Indexed content and direct-open failure are distinguished. |
| nCatLab | `/ncatlab/show/Hasse-Schmidt+derivative` direct access | Namespace URL was inaccessible via the web tool. The nLab result is not counted as independent nCatLab corroboration. |
| Stacks | `site=stacks.math.columbia.edu Hasse Schmidt derivations polynomial`, then `site:stacks.math.columbia.edu "divided powers" "polynomial"` | [Divided Power Algebra, 09PD](https://stacks.math.columbia.edu/tag/09PD), particularly §23.5, supplies related divided-power algebra context. It is not this polynomial-equivalence compatibility theorem. |
| MathOverflow | `site=mathoverflow.net Hasse derivatives polynomial coordinates`, then `site:mathoverflow.net "Hasse" "derivative"` | [Replacement for derivations in characteristic p?](https://mathoverflow.net/questions/71423/replacement-for-derivations-in-characteristic-p) identifies Hasse derivatives/hyperdifferentiations and jets as the appropriate characteristic-independent framework. Context only, not a proof source. |
| Recent arXiv | `site:arxiv.org "Fast Multivariate Multipoint Evaluation over All Finite Fields"`, plus 2022/2025 Hasse queries | [arXiv:2205.00342](https://arxiv.org/abs/2205.00342), submitted April 30, 2022, lies within five years of October 26, 2026. Its published §3.2 gives the exact translation/binomial formalism cited above. Other returned Hasse-diagram/principle/author-name matches were irrelevant and rejected. |

Standard form: a coordinate-preserving identification of polynomial algebras transports the binomial Hasse operator. A one-variable algebra isomorphism fixing the generator is exactly this theorem. Fields and finite coordinate tuples are common in applications, but the monomial formula already works over commutative semirings and arbitrary finite-support variable types. General Hasse–Schmidt derivations, jets, principal parts, and divided-power algebras are broader objects; they do not remove the coordinate normalization premise from this concrete theorem.

## Phase 4a–b: all parameters and generality

| Parameter | Necessity / weakening check |
|---|---|
| `σ : Type*` | Arbitrary variable type and universe. Exactly one variable is imposed only by the equivalence, not by a finite-type restriction. |
| `R : Type*` | Arbitrary coefficient type and universe. No concrete field or characteristic to abstract. |
| `[CommSemiring R]` | Canonical parent interface of `MvPolynomial`, its algebra equivalence and the project operator. Univariate `Polynomial.hasseDeriv` alone requires only Semiring; replacing the entire multivariate representation by a noncommutative monoid algebra would be a parent-API redesign. |
| `[Unique σ]` | Supplies the unique coordinate and the canonical equivalence. `Subsingleton σ` plus an explicitly chosen `j : σ` is equivalent data: j supplies nonemptiness and a local Unique instance. It is equivalent repackaging, not strictly weaker mathematics. Subsingleton alone allows an empty type, whose polynomial algebra is R rather than R[T]. |
| `n : ℕ` | Arbitrary Hasse order including zero. Binomial coefficients require natural exponents; arbitrary additive-monoid indices change the object. |
| `P : MvPolynomial σ R` | Arbitrary polynomial; no support, degree, monicity, nonzero, or regularity hypothesis. Removing P by bundling yields an equivalent map identity. |

MAXIMALLY GENERAL within the fixed canonical parent interface. The native parent guard confirms that `MvPolynomial σ S` does not elaborate under only `[Semiring S]`. No verified strict hypothesis weakening. Equivalent chosen-coordinate, inverse and bundled forms are useful shape checks, not grounds for YES-but-generalise-first. Every argument selects an operator or polynomial in the conclusion; no superfluous hypothesis survives the audit.

## Phase 4c: nine modern-idiom questions

| # | Question | Answer and downstream consequence |
|---|---|---|
| 1 | Typeclasses | Already uses canonical `CommSemiring` and `Unique`; no bespoke predicates to replace. Subsingleton plus j is equivalent data and needs a local Unique instance for the existing equivalence. |
| 2 | Filters/nets | No topology, limits or infinite summation. |
| 3 | Universal property | The canonical algebra equivalence already fixes coefficients and sends the unique generator to T. Its universal property identifies the equivalence; it does not automatically identify two linear differential operators. |
| 4 | Bundled substructure | No set with closure conditions. An equivalent equality of composed linear maps enables point-free rewrites and is tested. |
| 5 | Algebra hierarchy | Already semirings and no characteristic assumptions; weakening the parent interface is a representation change. |
| 6 | Higher categories | No higher coherence or categorical-limit content. Conjugacy of linear maps suffices. |
| 7 | Abstract indices | ℕ is the actual Hasse/binomial index, not accidental induction syntax. |
| 8 | Concrete-via-abstract | Diagnostic fires: the named equivalence occurs on the coefficient-rewrite line and zero lines after it. Abstract restatement: if an equivalence transports the coefficient/basis formula for two linear operators, it intertwines them. Generic linear-map extensionality already provides the abstract equality principle; the actual monomial normalization is essential and the minimal experiment discharges it by definitions. |
| 9 | False-generalization guard | Reject unconditional commutation with an arbitrary algebra equivalence. The compiled counterexample constructs the scaling automorphism T ↦ 2T over ℚ with inverse T ↦ (1/2)T using `Polynomial.algEquivOfCompEqX`, and composes it with `uniqueAlgEquiv`. At P=X and n=1 the two sides are 1 and C 2. The equivalence must preserve the distinguished coordinate or carry an appropriate derivative transformation rule. Reject dropping Unique to Subsingleton without a point, because the empty-variable algebra is different. |

[Q8 counts](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/q8-diagnostic.json). Modern idiom available as equivalent inverse/bundled packaging, not as a demonstrated semantic improvement requiring a new primary theorem. A conditional abstract conjugacy theorem merely moves the real normalization into a hypothesis. Q9 prevents treating all algebra equivalences as coordinate-preserving.

## Phase 4.5: infrastructure risks

All six risks are n/a for this theorem: typeclass diamonds; reducibility leaks; noncanonical unfolding; instance-priority collisions; universe-polymorphism construction issues; coercion ambiguity. The theorem introduces no definition, instance, or coercion. Existing canonical parent interfaces remain unchanged.

## Phase 4.6: all five proof-strategy rows

| # | Strategy | Assessment |
|---|---|---|
| 1 | ε–δ versus filters | n/a: no topology. |
| 2 | Element algebra versus inclusion/bundling | Coefficient extensionality is natural for polynomial operators. Linear-map equality is equivalent and supports composition; the actual caller wants a pointwise rewrite. |
| 3 | Sequences versus nets | n/a: no convergence. |
| 4 | Construction versus universal property | The equivalence is already canonical. Hasse derivatives of positive order are linear maps, not algebra homomorphisms; algebra-hom extensionality alone is insufficient. |
| 5 | Missing helpers | The multivariate operator/coefficient formula is project API, while the equivalence coefficient formula is pinned mathlib API. A shorter raw proof uses linear-map basis extensionality plus definition simp, verified without new coefficient helpers. |

MATHLIB-IDIOMATIC. The minimal basis proof is a possible alternative, but the short coefficient proof expresses exactly the existing computational interface. Neither strategy changes the mathematical assumptions.

## Phase 5: five actual methods on all three forms

[Formal receipts](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/formal-search.json) contain all 12 exact API requests and complete returned responses; [rg receipts](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/source-search.json) contain all exact source commands and complete outputs. Search failure is not proof of absence; external indexes can differ from the pinned revision. Local queries report `index: unavailable`, even when fallback source hits were returned.

| Form | Finder | Loogle | LeanSearch | rg | Local |
|---|---|---|---|---|---|
| Current uniqueAlgEquiv/Hasse | Ordinary bivariate pderiv transport, univariate order-one Hasse | `MvPolynomial.uniqueAlgEquiv, Polynomial.hasseDeriv`: empty | Univariate Hasse, finSuccEquiv, ordinary pderiv | No matching pinned multivariate Hasse transport | Project target only; index unavailable |
| Literature single-variable Hasse–Schmidt identification | Univariate Hasse and polynomial derivations | `Polynomial.hasseDeriv, Polynomial.aeval`: empty | Univariate Hasse and related derivative API | No Hasse/Schmidt declaration in pinned MvPolynomial subtree | Univariate/project Hasse hits; index unavailable |
| Abstract intertwining/conjugacy | Generic equivalence/conjugation candidates | `LinearEquiv, LinearMap.comp`: generic comp cancellation | `LinearEquiv.conj_apply_apply` and conjugation algebra equivalences | Canonical equivalence coefficient formulas and generic comp cancellation | `LinearEquiv.conj` among unrelated conj matches; index unavailable |

Positive pinned building blocks: `MvPolynomial.uniqueAlgEquiv`, `coeff_uniqueAlgEquiv`, `coeff_uniqueAlgEquiv_symm`, and monomial equivalence lemmas in `Mathlib/Algebra/MvPolynomial/Equiv.lean`; `Polynomial.hasseDeriv`, `hasseDeriv_coeff`, and `hasseDeriv_monomial` in `Mathlib/Algebra/Polynomial/HasseDeriv.lean`; `MvPolynomial.linearMap_ext`, `LinearMap.ext`, and `LinearEquiv.conj_apply_apply`. Positive signatures were checked natively; `uniqueAlgEquiv_symm_eq` was separately checked to fail and is not a positive candidate. [Equiv source](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/equiv-source.lean.txt), [Hasse source](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/polynomial-hasse-source.lean.txt).

Ordinary derivations cover first order only and cannot recover higher Hasse orders in positive characteristic. Generic conjugation names a transported operator but does not equate it to the binomial operator. No existing named replacement was found or is asserted. The isolated raw probe guards missing project declarations with `#check_failure` and proves the entire identity using a reconstructed raw operator, without importing Roth.

## Phase 5.5: statement shape

Normal form: derivative after transporting to the canonical univariate representation is the RHS. Equivalent alternatives are inverse transport, a commuting square of linear maps, and a conjugation equality. The current orientation supports rewriting either direction; the actual caller uses the reverse orientation to translate a univariate Hasse coefficient into a multivariate derivative.

Syntactic generality: inverse, chosen-coordinate/Subsingleton, and bundled forms were compiled in the [complete disk execution](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/complete-executed.lean.txt), with [complete native success](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/complete-success.json), with the bundled form

```lean
(uniqueAlgEquiv R σ).toLinearMap.comp (hasseDeriv (Finsupp.single default n)) =
  (Polynomial.hasseDeriv n).comp (uniqueAlgEquiv R σ).toLinearMap
```

The inverse form is useful when starting with `Polynomial R`; the current pointwise form directly matches the only caller. Chosen-coordinate/Subsingleton packaging changes how the unique coordinate is supplied, not its content. Superfluous arguments: NONE, as audited individually in Phase 4a. Normal form OK; syntactic generality OK; overall SHIP-AS-STATED if the public lemma is retained.

## Phase 6.0: complete explicit caller and inline audit

| Caller | Exact role and refactor plan |
|---|---|
| `Roth/Index.lean:239`, `Roth.index_unique` (234–251) | Within local `key`, rewrites `Polynomial.taylor_coeff` backwards through this theorem, then uses `Finsupp.unique_single` and mathlib evaluation transport. n is `d default`; R is ℝ; σ retains Unique. If the public lemma is omitted, replace this single occurrence by a local `have hbridge` proved by the exact replay or the verified minimal linear-square proof, specialize to `d default` and P, and rewrite backwards with it. |

Internal explicit proof use count: **1**, in one external-to-file module. The defining declaration and module-docstring mention are excluded. Full [caller module](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/caller-source.lean.txt) was read. Inline grep finds `Theta.lean:234` comparing equivalence and coefficient maps, and `Separation.lean:170–184` coefficient/degree identities for the inverse equivalence; these do not rederive this Hasse bridge. The nearby single-coordinate aeval theorem is a different orientation on a larger variable type. Source-level references do not enumerate opaque kernel or simp dependency closure, and no external consumer is claimed.

## Phase 6: actual composition experiments

The exact coefficient proof was replayed independently of the target theorem. Its bundled linear-square and inverse consequences were compiled. The complete actual `index_unique` key equation was also compiled under arbitrary `CommSemiring R`, covering its ℝ caller as a specialization. Transport from the independently replayed coordinate bridge is also an experiment in API organization; that bridge remains **new project API**, so a short derivation from it is not a ≤3 existing-mathlib-call replacement.

The decisive isolated experiment reconstructs only the raw multivariate `Finsupp.lsum` operator. It has no new coefficient or monomial helper, no induction, no target import, and proves the bundled identity by:

```lean
apply MvPolynomial.linearMap_ext
intro k
apply LinearMap.ext
intro a
simp [-map_natCast, CoeffAssessment.delta, Polynomial.hasseDeriv,
  Polynomial.C_mul_X_pow_eq_monomial, Polynomial.C_mul_monomial, mul_assoc]
```

The extensionality premise is actually closed by definition simp, not left as a hypothesis. [Minimal exact executed source](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/minimal-executed.lean.txt), [complete native success](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/minimal-success.json). This is the explicit Phase 6b closing-simp case. It supports BORDERLINE, not automatic NO, and prevents portraying the remaining normalization as a substantial missing proof. Two initial normalization failures, an inverse broad-simp failure, an extra-import/local-instance warning attempt, and an initial counterexample-normalization failure are retained separately from accepted evidence; no rejected proof is counted as successful.

## Phase 7–8: verdict and action

**BORDERLINE-needs-human**, with completed read-only assessment and no unresolved verification. The concrete missing API is compatibility between the proposed multivariate Hasse operator and the existing canonical univariate algebra equivalence. The identity is standard, general enough, and actually used; however its whole proof closes through existing basis extensionality and definition expansion. The skill explicitly leaves a closing-simp composition to API judgment. No cost argument or inherited verdict is used.

Concrete future upstream API questions:

1. Should the multivariate Hasse PR expose this unique-variable transport as a public rewrite lemma, given the closing-simp basis proof and one current consumer?
2. Should the broader single-coordinate aeval bridge be the primary compatibility API, with this theorem derived locally, or should both orientations be public?
3. Should the PR include the equivalent inverse or bundled commuting-square form, or retain only the pointwise form used by `index_unique`?

Retain locally in `Roth/HasseDeriv.lean` pending those upstream design choices. If retained publicly, proposed location is **`Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`**, next to the new parent operator and coordinate compatibility; proposed PR title: `feat(Algebra/MvPolynomial): add multivariate Hasse derivatives and univariate transport`. If omitted, the precise one-caller local-proof replacement is described above. No pinned mathlib theorem is falsely named as a direct replacement.

Grouping uses the actual [completed progress entries](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/progress-read.json): accepted YES declarations are `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.hasseDeriv_hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.pderiv_hasseDeriv`, `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, and `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`. The preceding coordinate bridge is BORDERLINE, not silently included as YES; monomial/apply/zero wrappers likewise are not counted as accepted YES.

Before an upstream PR run `/generalise MvPolynomial.uniqueAlgEquiv_hasseDeriv`, `/cleanup Roth/HasseDeriv.lean MvPolynomial.uniqueAlgEquiv_hasseDeriv`, and `/pre-submit`. Reviewer candidates from relevant recent pinned commits are Yaël Dillies (`631b214f7c`, MvPolynomial coefficient API), Moritz Firsching (`334438dace`, Hasse derivative map), and Marcelo Lynch (`b0bf9145fc`, relevant variable cleanup). [Fresh commit receipt](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/reviewer-commits.json).

[Verification manifest](../evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/verification.json) records accepted exact sources and complete native receipts, standard axioms, inverse/bundled forms, the chosen `Subsingleton σ` plus `j : σ` wrapper, the parent Semiring failure guard, and the scaling algebra-equivalence counterexample. The caller verification proves the complete local `Index` key equality under arbitrary `CommSemiring R`, specializing to the actual ℝ caller; it does not replay the whole `index_unique` theorem. `uniqueAlgEquiv_symm_eq` is honestly a missing candidate, not a positive signature. Verification here does not claim a fresh downstream whole-project rebuild. The portable validator checks current artifact hashes and links in both scratch and integrated layouts; the historical worker manifest is not substituted for the current manifest.
