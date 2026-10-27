# Roth.coeff_kronecker — assessment 109

## Phase 0 — Baseline and identity

Resolved exactly at `Roth/GenWronskian.lean:88`, public theorem, canonical position109. The declaring module develops generalized Wronskians, using bounded Kronecker substitution to reduce linear independence to univariate polynomials. All17 source/pin hashes freshly match the shared clean baseline: `lake build` succeeded with2467 jobs. Production files are unchanged. See [fresh inputs](../evidence/Roth.coeff_kronecker/inputs.json), [baseline](../evidence/Roth.coeff_kronecker/baseline-build.txt), [canonical entry](../evidence/Roth.coeff_kronecker/canonical-entry.json), [full module](../evidence/Roth.coeff_kronecker/source-0.lean.txt).

Native elaborated type (universe polymorphic; no hidden characteristic-zero or family-size hypothesis):

```lean
∀ {K : Type u_1} [Field K] {σ : Type u_2} [Fintype σ] {k : ℕ},
  1 < k → ∀ {P : MvPolynomial σ K},
    (∀ j : σ, MvPolynomial.degreeOf j P < k) →
      ∀ {d : σ →₀ ℕ}, (∀ j : σ, d j < k) →
        ((Roth.kronecker k) P).coeff (Roth.kroneckerExp k d) = P.coeff d
```

Exact original type, full proof term and standard-axiom check are retained in [original receipt](../evidence/Roth.coeff_kronecker/coeff-kronecker-original-receipt.json). The exact ordered293-name canonical audit independently finds only `Roth.kronecker_eq_zero_iff` as a direct proof-term consumer; source references and kernel direct consumers are distinct measurements. See [audit source](../evidence/Roth.coeff_kronecker/coeff-kronecker-audit-executed.lean.txt) and [audit receipt](../evidence/Roth.coeff_kronecker/coeff-kronecker-audit-receipt.json).

## Phase 1 — Mathematical content

Choose an enumeration of the finite variable set. Substitute each variable of position i by t raised to k^i. If P has degree below k in each variable and d is a digit vector with all entries below k, the coefficient at encoded exponent Σ dᵢkⁱ is exactly the coefficient of X^d in P. The proof expands P into monomials, computes their images, and uses uniqueness of bounded base-k digits to show that only d contributes to the chosen coefficient. The absent-support case uses coefficient zero.

Project dependencies are `kronecker`, `kroneckerExp`, `kronecker_monomial`, and `kroneckerExp_injOn`; finite-support, coefficient, degree and sum APIs supply the remaining steps. No inverse, subtraction, division, characteristic-zero argument, determinant or Hasse derivative occurs in this proof.

## Phase 2 — Preliminary checks

SMALL: this is a coefficient-recovery helper, not the named main Wronskian theorem. “Kronecker” identifies the substitution, rather than turning every auxiliary law about that substitution into a named major theorem. Literature search remains exhaustive. One-line definition test: n/a, theorem. The proof is genuinely multiple steps; the definition-only exemption table is inapplicable.

## Phase 3 — Exhaustive literature

Exact requests, response SHA256/bytes, source locators and concise original summaries are retained without full returned web bodies in [search receipts](../evidence/Roth.coeff_kronecker/literature-search.json), [direct access](../evidence/Roth.coeff_kronecker/literature-direct.json), and [recent search](../evidence/Roth.coeff_kronecker/literature-recent.json).

| Channel | Actual query or locator | Finding |
|---|---|---|
| Web, specific | Kronecker substitution coefficient recovery injective degree bound multivariate polynomial | Bounded degree coefficient encoding; direct INRIA appendix3 states coefficient read-off. |
| Web, general | monomial substitution sparse polynomial coefficients collision free Kronecker map | Separating weighted exponents, support collisions and sparse representations. |
| Web, aliases | Kronecker substitution base representation individual degree coefficient preservation | Radix encoding of exponent vectors is the classical mechanism. |
| ChatGPT mathematics | n/a: `ask_chatgpt_math` unavailable | No fabricated consultation or historical answer. |
| Local references | `clean.tex:220–280`, especially246–252 | FACT gives uniqueness of bounded digits, then compares the encoded coefficient; exactly the source argument. Full local text checked. |
| nLab | `site:ncatlab.org/nlab Kronecker substitution polynomial` | Polynomial/substitution background returned. Direct polynomial page failed with unexpected `application/xhtml+xml`; no claimed bounded recovery theorem. |
| nCatLab | `site:ncatlab.org/ncatlab polynomial substitution monoid algebra` | Search redirected to nLab background; direct nCatLab polynomial URL inaccessible. No separate categorical analogue established. |
| Stacks | `site:stacks.math.columbia.edu polynomial monoid algebra substitution coefficients` | General commutative-algebra background only. Direct00FU was a Jacobson-ring result, not this law; rejected as a matching source. |
| MathOverflow | `site:mathoverflow.net Kronecker substitution polynomial coefficients` | Returned root-of-unity and representation-theoretic Kronecker results; no matching bounded coefficient law established. |
| Recent arXiv | `site:arxiv.org "Kronecker substitution" after:2021-10-27 before:2026-10-28` | Wang–Su–Wang–Zhang2024 discusses reversible reductions and smaller exponents; Shunia2024 applies substitution to quotient rings. Older hits are not counted as recent. |

The [INRIA seminar account](https://algo.inria.fr/seminars/sem00-01/lecerf.html), appendix3 lines113–120, explicitly describes reading a bounded multivariate coefficient from the encoded univariate exponent. [Wang et al., arXiv2403.12716](https://arxiv.org/abs/2403.12716), submitted19 March2024, studies reversible reductions and exponent choices. Neither is evidence for requiring a field in the finite coefficient calculation. The local source is [archived separately](../evidence/Roth.coeff_kronecker/local-literature.txt).

Standard concept: collision-free monomial substitution / Kronecker coefficient recovery. Uniform radix bounds are sufficient, while the algebraic mechanism only needs the exponent map to separate a set containing the support and queried exponent. That abstract formulation is a mathematical inference confirmed by the native general proof; it is not falsely attributed verbatim to a literature source. Historical radix formulations and modern sparse weight choices concern the same coefficient transport, with different sufficient separation conditions.

## Phase 4a–b — Generality

| Parameter/hypothesis | Audit and verified alternative |
|---|---|
| K and `[Field K]` | K remains a coefficient type; replace Field by CommSemiring in expanded aeval formulation. No nontriviality, cancellation or inverses used. |
| σ and `[Fintype σ]` | σ remains arbitrary universe-polymorphic. Fintype supports the fixed `equivFin` interface; arbitrary supplied weights need no finiteness instance. |
| k | Relevant only for uniform positional weights. Arbitrary w:σ→ℕ is verified when separation is supplied. |
| hk:1<k | Droppable for bounded positional vectors. For k≤1 all admissible coordinates are zero or impossible. The stronger positional probe uses the separately proved108 prerequisite, not an existing mathlib theorem. |
| P | Essential object; support containment is the general replacement for degree assumptions. |
| hP | Replace by support containment in S. It implies this containment via `monomial_le_degreeOf`; dropping all separation information is false. |
| d | Essential queried exponent. It need not belong to P.support. |
| hd | Replace by d∈S. A support-only injection statement excluding queried d is insufficient when its coefficient is zero but its image collides with a supported exponent. |
| Enumeration | Supply e:σ≃Fin n explicitly in positional corollary; arbitrary weights abstract it away. Arbitrary infinite position embeddings are not claimed to have a newly proved radix-injectivity theorem here. |

The fixed parent `kronecker` is field-typed; simply changing this theorem’s local Field binder cannot make that old spelling a semiring interface. The accepted expanded proof is over CommSemiring and arbitrary σ. The verified general statement is:

```lean
theorem abstract_coeff {R σ : Type*} [CommSemiring R] (w : σ → ℕ)
    (S : Set (σ →₀ ℕ)) (P : MvPolynomial σ R)
    (hP : (P.coeff.support : Set _) ⊆ S)
    (hi : Set.InjOn (Finsupp.weight w) S) {d : σ →₀ ℕ} (hd : d ∈ S) :
    (MvPolynomial.aeval (fun j ↦ (Polynomial.X : Polynomial R) ^ w j) P).coeff
      (Finsupp.weight w d) = P.coeff d
```

STRICTLY NARROWER THAN STANDARD in the verified coefficient-type/support/weight sense. The [raw proof](../evidence/Roth.coeff_kronecker/coeff-kronecker-raw-executed.lean.txt) is fully independent of Roth imports and guards the project target as absent. Its new normalization bridge is distinguished from existing mathlib API. It proves actual weakening, not just guessed unused hypotheses.

## Phase 4c — Modern idiom, all nine rows

| # | Question | Answer and concrete consequence |
|---|---|---|
|1|Typeclasses|Already uses algebraic classes; use CommSemiring rather than introduce a custom coefficient predicate.|
|2|Filters/topology|No; finite algebraic coefficient identity has no topology.|
|3|Universal property|Yes; aeval is the existing free commutative algebra map. The mapDomain algebra hom and polynomial/Finsupp equivalence offer a generator-extensional representation bridge.|
|4|Bundled substructure|Support containment in S is appropriate for a pointwise law. A supported submodule could organize families, but is not needed to state coefficient recovery.|
|5|Hierarchy|Yes; CommSemiring suffices, opening use with ℕ and rings without field instances. The underlying mapDomain law even works for AddCommMonoid coefficients.|
|6|Higher categories|No; no higher-categorical structure is involved.|
|7|Concrete indices|Yes at the transport level: Finsupp.mapDomain works for arbitrary source/target index types, while univariate polynomial exponents remain ℕ. Do not conflate abstract reindexing with changing polynomial exponents.|
|8|Concrete-via-abstract|Yes. Proof body mentions `kronecker_monomial` once and `kroneckerExp_injOn` once, with no `equivFin` after unfolding; all later reasoning is coefficient support and injectivity. The tested abstract law permits nonradix w and arbitrary S and composes with `Finsupp.mapDomain_apply'`.|
|9|False-generalization guard|Pass for the verified aeval/weight/support formulation: it computes exactly the same polynomial under specialization. Reject global injectivity of positional weight: for k=2, (2,0) and (0,1) collide. Reject deleting queried-point membership.|

Modern idiom available: yes, with concrete coefficient transport and support APIs. This is useful mathematical organization; its exact upstream packaging still requires separating existing mapDomain content from the new aeval bridge.

## Phase 4.5 — Infrastructure

n/a: theorem. It introduces no instance, coercion, universe-restricting data, reducibility barrier, unfolding path or instance-priority choice. The six infrastructure risk rows concern definitions/classes/instances and are inapplicable to this theorem.

## Phase 4.6 — Proof strategy

| Row | Finding |
|---|---|
|Topology ε–δ|n/a: no topology.|
|Element algebra vs substructures|Pointwise coefficient statement is natural; replace repeated sum isolation with mapDomain coefficient recovery after representation transport.|
|Analysis sequences/nets|n/a: no analysis.|
|Categorical construction/universal property|Generator extensionality for the existing free algebra is an alternative bridge; no new category construction needed.|
|Missing helper API|The aeval of monomial powers to mapDomain(weight) normalization bridge is the concrete candidate; coefficient recovery on mapDomain itself is already present.|

REFACTOR-RECOMMENDED: move normalization to the map level, then apply existing support-local coefficient transport. The raw bridge uses monomial/add induction; the separately verified hom-level approach applies aeval generator uniqueness. This recommendation concerns proof organization, not computational cost.

## Phase 5 — Five methods on three forms

[Formal API receipts](../evidence/Roth.coeff_kronecker/formal-search.json) and [successful Loogle retries](../evidence/Roth.coeff_kronecker/formal-search-retry.json) retain exact requests and full returns. Search indexes may differ from the pinned revision; positive candidates are checked natively and in pinned source. Local search’s index was `unavailable`, so its source hits do not establish absence.

| Method | Current Kronecker form | Literature monomial/support form | Abstract mapDomain form |
|---|---|---|---|
|Finder|Polynomial reconstruction/contract partial matches|rename/expand and power-series substitution|`Finsupp.mapDomain_apply'`, `mapDomain_injOn` positive|
|Loogle|`Polynomial.coeff, MvPolynomial.aeval`; unrelated minimal polynomial hit|`Finsupp.mapDomain, Set.InjOn`; exact support-local law|`Finsupp.mapDomain_apply'`; exact signature|
|LeanSearch|Power-series substitution and polynomial expand|Power-series and rename partial matches|Exact mapDomain coefficient law|
|rg|Full untruncated current search, no exact target|Pinned rename/expand/global injection APIs|Pinned support-local mapDomain and algebra-hom APIs|
|local|Project target and scratch copies; no upstream claim|Project Taylor coefficient law, not this result|Pinned Finsupp declaration names; index unavailable|

Exact existing law at `Mathlib/Data/Finsupp/Basic.lean:375`:

```lean
Finsupp.mapDomain_apply' S x hS hf ha
-- : x.mapDomain f (f a) = x a
```

It works over arbitrary AddCommMonoid coefficients and arbitrary α,β. `mapDomain_apply_of_injective` is the globally injective special case; it is too strong for full positional exponent space. `Finsupp.embDomain_apply_self` similarly needs an embedding and cannot directly encode all exponent vectors. `MvPolynomial.coeff_rename_mapDomain` / `coeff_rename_embDomain` reindex variables, rather than collapse monomials to weighted total exponents. `coeff_expand_smul` is uniform scaling of all coordinates, not the weighted sum. These are real partial matches, not exact replacements. `Polynomial.toFinsuppIsoAlg`, `AddMonoidAlgebra.mapDomainAlgHom`, `MvPolynomial.algHom_ext`, `aeval_monomial`, and `Finsupp.weight` are relevant building blocks.

Parent re-aim independently checked: parent102’s replacement is `MvPolynomial.aeval`, parent103’s is `Finsupp.weight`, and parent107’s is `aeval_monomial`. The analogous coefficient law for mapDomain exists; no already-existing coefficient-recovery law directly for aeval(X^w) has been identified. Thus the automatic NO parent gate does not fire merely by citing mapDomain_apply'. The representation bridge is nondefinitional and must be accounted for; the new108 injectivity theorem does not count as existing mathlib API. [Pinned source searches](../evidence/Roth.coeff_kronecker/rg-abstract.json) and [standard-form search](../evidence/Roth.coeff_kronecker/rg-standard.json) document these distinctions.

## Phase 5.5 — Statement shape

Normal forms considered: (a) the current named radix polynomial coefficient equality, (b) coefficient recovery under aeval(X^w), (c) Finsupp.mapDomain evaluation. Mathlib already has (c); a normalization equality should put this canonical representation on the RHS. The current equality’s RHS coefficient is a suitable simplification direction.

Syntactic generality: hP on degrees is convenient in the Wronskian consumer; support containment plus InjOn is appropriate for general monomial substitutions. Both must retain the queried point in the separating set, including when it is outside support. Explicit e avoids imposed enumeration. Superfluous arguments: hk and Field are mathematically stronger than needed, Fintype belongs to the current definition rather than general support transport; k remains relevant to the radix corollary, P,d essential, hP/hd replaced rather than erased. Overall RESTATE-BEFORE-SHIP for an upstream proposal.

Counterexample guards (mathematical checks): for k=2 with positions0,1, take P=X₁ and d=(2,0); dropping hd gives encoded coefficient1 versus original0. Take P=X₀² and d=(0,1); dropping hP gives the same mismatch. These examples reject proposed weakenings; they are not asserted as extra native-verified declarations. The accepted abstract theorem verifies the safe weakenings.

## Phase 6.0 — Callers and inline audit

| Caller | Exact use | Refactor implication |
|---|---|---|
|`Roth.kronecker_eq_zero_iff`, `Roth/GenWronskian.lean:111`|`simpa [h] using (coeff_kronecker hk hP ...).symm`|Use generalized coefficient transport at the bounded supported exponent; degree-to-support inequality supplies the premise. Actual complete caller replay verified.|

One source-level use in the same module; external-to-file callers0. The command’s separately defined count excluding the declaring file is0. The exact293 ordered canonical audit confirms the sole direct proof-term consumer. The theorem is not marked simp; still, source counts are not advertised as an opaque dependency closure. Inline grep of `finsetSum_coeff`, `sum_eq_single`, `coeff_C_mul_X_pow` and mapDomain found no independent same-law rederivation in production. Taylor coefficient extraction is a different substitution. See [caller receipt](../evidence/Roth.coeff_kronecker/rg-callers.json), [inline audit](../evidence/Roth.coeff_kronecker/rg-inline.json), and [caller summary](../evidence/Roth.coeff_kronecker/callers.json).

## Phase 6 — Actual composition experiments

1. Direct variable-renaming/embedding/global-injection routes: mismatch of domain or hypotheses, as above. Positional weight is not globally injective.
2. Existing support-local law succeeds in one call on Finsupp.mapDomain, with full signature checked. For the actual aeval statement, the verified raw proof first proves a new weighted-monomial identity and a new representation bridge by induction, rewrites polynomial coefficient to its Finsupp representation, and invokes mapDomain_apply'. That is a real proof, not ≤3 existing calls.
3. Old spelling is recovered using explicit weight=sum normalization, project108 injectivity and hP-to-support. The complete sole caller is replayed with the replacement coefficient proof; no use of the target theorem supplies this verification.
4. Universal-property alternative uses the existing polynomial/Finsupp algebra equivalence and mapDomain algebra hom, compared on generators. Its exact executed source and diagnostics are retained separately; rejected versions are never accepted as proofs.

The independent generalized positional experiment drops hk, weakens Field to CommSemiring and supplies an arbitrary e:σ≃Fin n, using the separately accepted108 scratch prerequisite. This is positive generality evidence, not a claim of a short existing-mathlib composition.

The generic `exact?` probe did not close the aeval coefficient goal and did not time out. This is a negative automation observation, not a universal absence proof. Its source/receipt is classified rejected/search-only because the attempted goal remains unproved. The accepted hom bridge instead proves an equality by `MvPolynomial.algHom_ext`, evaluates the generators before unfolding X, and normalizes `mapDomain_single` and `weight_single`. The proof is short, but the actual algebraic normalization is required; the original recursive `ext` attempt did not establish it. It is not an already-existing-call derivation. See [hom source](../evidence/Roth.coeff_kronecker/coeff-kronecker-hom-executed.lean.txt), [hom receipt](../evidence/Roth.coeff_kronecker/coeff-kronecker-hom-receipt.json), [old law and sole caller replay](../evidence/Roth.coeff_kronecker/coeff-kronecker-consumer-executed.lean.txt), and [generalized positional replay](../evidence/Roth.coeff_kronecker/coeff-kronecker-generalized-executed.lean.txt).

Composition conclusion: no verified ≤3 existing-mathlib-call derivation of the old statement. The abstract mapDomain formulation already exists in one call. The new generator-normalization bridge plus existing coefficient law leaves a genuine choice of useful API surface. Phase6b explicitly treats a closing simp normalization composition as BORDERLINE rather than automatic NO; this hom-level analogue strengthens the reason to decide bridge-only versus extraction API before adding another theorem. This is not an argument from proof length or from search failure. Actual abstract coefficient proof, old-form specialization, generalized positional law and complete direct caller replay all succeeded; proof acceptance is resolved.

## Phase 7 — Verdict

**BORDERLINE-needs-human.** The specific design issue is which normalization/extraction API should be added around existing free-algebra evaluation and Finsupp coefficient transport. Uniform-base coefficient recovery is useful in the Wronskian development, and the expanded theorem has verified substantial generality. However, its coefficient-separation content is exactly existing `Finsupp.mapDomain_apply'`; the candidate new contribution is the representation bridge, possibly with a user-facing aeval corollary. It would be misleading either to submit the narrow old theorem as independent mathematics or to report an existing aeval law that was not found. No cost consideration determines this verdict.

The following are concrete future upstream API questions, not unresolved Lean checks:

1. Add the proved aeval(X^w)-to-mapDomain(weight) algebra-hom normalization equality to `Mathlib/Algebra/MvPolynomial/Eval.lean`, with the polynomial/Finsupp equivalence in the statement?
2. Expose `abstract_coeff` directly for aeval and support-local InjOn, or let users apply the existing `Finsupp.mapDomain_apply'` after that normalization?
3. If a positional coefficient corollary is desirable, group it with the already accepted YES-generalise declaration108 `Roth.kroneckerExp_injOn`, using explicit e:σ≃Fin n and no hk?

An affirmative bridge/extraction proposal would use title `feat(Algebra/MvPolynomial): normalize monomial evaluation and recover separated coefficients`, with main normalization provisionally in `Mathlib/Algebra/MvPolynomial/Eval.lean`, conditional on import layering; keep positional injectivity in declaration108’s proposed `Mathlib/Data/Nat/Digits/Finsupp.lean`, avoiding extra foundational imports in Weight. Eval currently imports MvPolynomial.Basic; this bridge additionally needs Polynomial.AlgebraMap for `toFinsuppIsoAlg`, Weight, and monoid-algebra domain mapping. A dedicated monomial-evaluation bridge file may avoid adding those imports to foundational Eval. This is an import-scope caveat, not a claimed cycle. The genuinely related accepted YES is108, verified from current progress rather than inferred from a helper name. Do not bundle unrelated Hasse or determinant results merely because they are nearby. [Accepted YES inventory](../evidence/Roth.coeff_kronecker/accepted-yes.json) and [recent relevant commit history](../evidence/Roth.coeff_kronecker/reviewer-history.json) support this plan. Yaël Dillies is a relevant reviewer candidate from recent Finsupp mapDomain and MvPolynomial coefficient work; Aaron Liu is another evaluation-API candidate. No reviewer was contacted.

Before any upstream proposal, run `/generalise Roth.coeff_kronecker`, `/cleanup <chosen upstream file> <chosen new API declaration>` on the chosen expanded formulation, and verify appropriate imports/home. For a bridge-only decision, replace the single explicit caller’s coefficient step by the verified support-local extraction after normalization; for an extraction-API decision, use the verified `abstract_coeff` specialization with degree-to-support and bounded-weight injectivity. Both routes require the separately new108 positional-injectivity prerequisite, not only old mathlib calls. Alternative local destination for the readable radix corollary is `Roth/GenWronskian.lean` as a private helper; it directly supports zero detection. This report does not authorize or perform production refactoring.

## Phase 8 — Verification and handoff

Six accepted native source/receipt pairs cover original/type, canonical audit, isolated general bridge/extraction, full old-form+caller replay, stronger positional theorem, and the independent universal-property bridge. All completed successfully with standard axioms only (`propext`, `Classical.choice`, `Quot.sound`), without raised limits, unsafe code or admitted proofs. Seven rejected/search-only attempts retain their exact sources and diagnostics separately; recovered `sorryAx` in a rejected elaboration is never accepted proof evidence. Disk receipts retain historical messages, so target assertions use their actual new region start lines; full-file errors/warnings are still checked.

The stronger positional theorem depends on declaration108’s newly proved `KroneckerExpInjOnNoBase.no_base`; its exact isolated prerequisite source/receipt is preserved and validated separately, not presented as existing mathlib API. The original293 audit preserves every private name and exact tracked order. All supporting files, current hashes and bytes, accepted sources, source locations and links are machine validated; current copy-manifest remains authoritative after integration. [Verification inventory](../evidence/Roth.coeff_kronecker/verification.json), [assessment](../evidence/Roth.coeff_kronecker/assessment.json), and [portable validator](../evidence/Roth.coeff_kronecker/validate.py) contain the checks. All phases PASS or justified theorem n/a; unresolved verification is empty; root acceptance is recorded separately in machine metadata. The three API design questions do not block completion of this read-only assessment.
