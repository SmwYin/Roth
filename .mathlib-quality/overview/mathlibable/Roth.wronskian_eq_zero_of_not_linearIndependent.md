# Roth.wronskian_eq_zero_of_not_linearIndependent

Verdict: **BORDERLINE-needs-human**. The easy Wronskian implication is standard and useful, but the upstream API choice is between a named Hasse-family theorem and a law for determinants of linear-operator families. A verified four-call mathlib derivation connects these representations. This is an independent assessment, not inheritance from the two parent definitions.

## 0. Baseline

The shared build completed successfully (2467 jobs); all 17 source/pin hashes freshly match its manifest. The public theorem resolves at Roth/Wronskian.lean:65, has no sorry, and replays with standard axioms only. The declaring module was read in full; it develops finite polynomial Wronskians and the characteristic-zero independence criterion. Evidence: [baseline](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/baseline-build.txt), [fresh hashes](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/source-pin-hashes.json), [native target](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/native-target-success.json), [full source](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/source-wronskian.lean.txt).

## 1. Statement and proof

For any finite family of polynomials over a field, linear dependence over the coefficient field implies that the determinant of its Hasse derivatives of orders 0 through l−1 is zero. Characteristic zero is unnecessary in this direction.

Full native type:
```lean
@Roth.wronskian_eq_zero_of_not_linearIndependent :
  ∀ {K : Type u_1} [inst : Field K] {l : ℕ} {φ : Fin l → K[X]},
    ¬ LinearIndependent K φ → Roth.wronskian φ = 0
```

K is the coefficient field, l is the family length (including zero), φ is the family, and h is its dependence hypothesis. Obtain a nontrivial constant relation from Fintype.not_linearIndependent_iff. Applying each Hasse derivative preserves this relation. Its coefficients, embedded by Polynomial.C, provide a nonzero polynomial vector in the matrix kernel; Matrix.exists_mulVec_eq_zero_iff gives vanishing determinant. No characteristic, degree, or nonzero-polynomial assumptions are used.

Project dependencies: wronskian and wronskianMatrix. The proof does not use other project theorems. This is not a definitional glue lemma.

## 2. Preliminary checks

SMALL: a supporting direction of the main equivalence, not itself a new structure or the module's named main result. Literature width remains exhaustive. One-line definition test: n/a, theorem. The proof is a substantive witness/linearity argument; a short rewritten proof does not make it a one-line definition.

## 3. Literature

Exact requests, response hashes/bytes, URLs and concise original summaries are in [web1](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/web1-metadata.json), [web2](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/web2-metadata.json), [web3](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/web3-metadata.json), and [web4](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/web4-metadata.json). Full returned bodies are not archived.

| Channel / actual query | Result and locator |
|---|---|
| General web: “Wronskian linearly dependent polynomials Hasse derivatives determinant vanishes” | Standard determinant implication; primary Bostan–Dumas located. |
| General web: “Wronskian linear dependence arbitrary field positive characteristic Hasse derivative” | Positive-characteristic issues concern the converse, not this implication. |
| General web: “generalized Wronskian alternating multilinear maps determinant linear dependence integral domain” | Alternating multilinear determinant formulation; differential-operator variants. |
| ChatGPT math | n/a: ask_chatgpt_math unavailable; no substitute model opinion fabricated. |
| Local clean.tex | §2 lines157–194: normalized Wronskian and easy dependence direction; lines207–222: generalized differential operators. [Excerpt](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/local-literature.txt). |
| nLab: site:ncatlab.org/nlab Wronskian linear dependence | Wronskian entry found; direct fetch failed with unsupported XHTML content type. |
| nCatLab: site:ncatlab.org Wronskian Hasse derivative | Same host's categorical material searched independently; no additional exact theorem identified. Direct abstract alternating-map page cache miss. |
| Stacks: site:stacks.math.columbia.edu Wronskian determinant linear dependence | Global book result, no matching specific tag identified; no absence conclusion. |
| MathOverflow: site:mathoverflow.net Wronskian linearly dependent positive characteristic | Generalized and geometric Wronskians discussed, e.g. questions487552 and498824; contextual rather than primary authority. |
| Recent arXiv: site:arxiv.org Wronskian Hasse derivatives 2021 2022 2023 2024 2025 2026 | Kiselev2511.03848 (2025), abstract generalized differential determinants; 2206.10855 (2022), Stieltjes derivative variants. Older returned papers explicitly excluded from “recent” evidence. |

[Bostan–Dumas, *Wronskians and Linear Independence*](https://mathexp.eu/bostan/publications/BoDu10.pdf), Monthly117 (2010), p722 introductory implication, is the principal external reference. Pages723 and725 distinguish characteristic-sensitive converses and generalized operator families. [Kiselev2025](https://arxiv.org/abs/2511.03848), abstract, confirms continuing use of generalized Wronskians with selected differential operators; it is not evidence that the exact Hasse API already exists.

The standard name is the easy direction of the Wronskian criterion. Standard statements range from sufficiently differentiable functions to formal series and generalized differential operators. The shared reason is a nontrivial constant relation preserved by linear operators. The project already goes beyond its source's rational-coefficient wording; no mathematical novelty claim is made.

## 4a–b. Generality

| Parameter/hypothesis | Assessment |
|---|---|
| Type universe K | Already universe-polymorphic. No forced Type0. |
| Field K | Inverses unused. Expanded matrix/W definitions admit CommRing R with NoZeroDivisors R, including the zero ring; verified below. |
| l : ℕ | Includes l=0; dependence is impossible there, so no positivity hypothesis needed. |
| Fin l indices | Match derivative orders0,…,l−1. Arbitrary finite columns require ordered/enumerated derivative rows or explicit row operators; replacing indices blindly changes the object. |
| φ | Arbitrary polynomials, with no degree restrictions. A generic module-family abstraction is meaningful through explicit linear maps. |
| h : ¬ LinearIndependent K φ | Essential. For singleton φ=[1], W=1; it cannot be dropped. Equivalent explicit coefficient witnesses are less convenient for the sole caller. |

[Domain proof](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/native-domain-executed.lean.txt) verifies the original argument unchanged over CommRing+IsDomain. [Guard/generalization](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/native-guard-executed.lean.txt) further verifies CommRing+NoZeroDivisors by separating subsingleton and nontrivial rings. Thus the expanded expression is strictly narrower than necessary in its Field presentation. This is not a one-edit theorem-signature weakening against fixed Roth.wronskian: both public parent definitions currently demand Field. The representation changes must be coordinated; no hypothetical mechanical generalise-first claim is made.

Verified target shape:
```lean
{R : Type*} [CommRing R] [NoZeroDivisors R] {l : ℕ}
{φ : Fin l → R[X]} (h : ¬ LinearIndependent R φ) :
  (Matrix.of fun μ ν : Fin l ↦ Polynomial.hasseDeriv μ (φ ν)).det = 0
```

A blanket CommRing statement is false: in ℤ×ℤ the singleton polynomial C(1,0) has the nontrivial annihilating coefficient (0,1), yet its one-by-one determinant is C(1,0)≠0. Both assertions compile in the accepted guard. Dropping commutativity also prevents use of this ordinary determinant API; replacing determinant with a noncommutative invariant would change the mathematical problem. A semiring-only claim is not proposed: ordinary determinant uses additive inverses.

## 4c. Modern idioms

| # | Check | Finding and concrete consequence |
|---|---|---|
| 1 | Typeclass preambles | Already typeclasses; retain algebra/module/torsion assumptions explicitly in abstract form. |
| 2 | Filters/nets | No topology or limits. |
| 3 | Universal properties | No new object needing a universal-property class. Existing alternating maps are appropriate bundles. |
| 4 | Bundled substructures | No ad hoc closure predicate. A separate dependence-submodule API is unnecessary here. |
| 5 | Field→module/ring hierarchy | Yes: verified NoZeroDivisors ring version; allows integral coefficient domains and trivial rings after expanding parents. |
| 6 | Higher categories | No categorical content or downstream gain. |
| 7 | Concrete indexing | Fin l fixes successive derivative orders; arbitrary finite operator families are an expanded representation, not a blind index weakening. |
| 8 | Concrete-via-abstract | Yes. The proof body mentions wronskian zero times and wronskianMatrix on one line; hasseDeriv appears only as the linear relation-preserving map on one line. No Leibniz, degree or composition law is used. Existing AlternatingMap.map_linearDependent proves the abstract vanishing law. A verified four-call scalar-restriction/column bridge applies the determinant API directly; the analogous multivariate proof at GenWronskian:40–50 exposes a second consumer. |
| 9 | False-generalization guard | Accepted ring weakening preserves the exact Hasse determinant. Generic operator matrices explicitly enlarge the construction. Arbitrary CommRing dependence implication rejected by compiled ℤ×ℤ counterexample; binary Polynomial.wronskian is not a replacement for arbitrary l. |

The [generic-family probe](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/native-family-executed.lean.txt) also verifies the same four-call proof for arbitrary scalar-linear maps D into a domain algebra. The [stronger semiring probe](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/native-semiring-executed.lean.txt) weakens its base to CommSemiring R and source to AddCommMonoid M, with CommRing S, IsDomain S, Algebra R S and FaithfulSMul R S. This is a new scratch theorem, not an existing mathlib replacement; no maximality claim is made for scalar-action formulations. It establishes the common abstraction without claiming the multivariate production module was migrated.

Modern idiom available: yes, with concrete benefit: determinant column independence, restriction of scalars, and bundled linear derivative maps eliminate the hand-built kernel witness and apply to univariate and multivariate operator families. The existing abstract law itself is not missing. The remaining design question is whether to bundle/name the Hasse alternating map, retain a specialized scalar-family theorem, or use a general determinant bridge.

## 4.5. Infrastructure risk

n/a — theorem. It introduces no instance, coercion or definitional equality. The six definition-only risks (diamond, reducibility leak, unfolding, priority, universe and coercion ambiguity) therefore do not require probes on this declaration. Parent-definition design remains a separate API consideration.

## 4.6. Proof strategy

| # | Check | Finding |
|---|---|---|
| 1 | Topology: epsilon-delta versus filters | n/a, algebraic determinant. |
| 2 | Algebra: element versus structural argument | REFACTOR-RECOMMENDED: use determinant column independence, restriction of scalars and of_comp rather than reconstructing coefficient witnesses. Actual compiled alternative below. |
| 3 | Analysis: sequences versus nets | n/a. |
| 4 | Category theory: construction versus universal property | n/a. |
| 5 | Helpers mathlib should have | Existing abstract vanishing law present. Optional missing packaging: a named determinant law for scalar-linear operator families / a bundled finite Hasse Wronskian, depending on upstream design. No invented helper counted as existing. |

The alternative is shorter and avoids explicit sums. Proof strategy cost is CHEAP for this proof; coordinating parent representations is an API decision, not a cost-based verdict.

## 5. Mathlib search

[All12 raw search receipts](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/formal-search-raw.json) cover all four callable search methods on current, literature-standard and abstract forms. [Exact rg commands and full results](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/source-search-raw.json) provide the fifth method and source/caller audit. [Pinned excerpts](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/mathlib-source-excerpts.lean.txt), [hashes](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/mathlib-source-hashes.json).

| Form | Finder | Loogle | LeanSearch | rg | Local names |
|---|---|---|---|---|---|
| Hasse polynomial dependence | binary Wronskian, discriminant analog | no combined Hasse/det result | binary Wronskian, discriminant | Hasse API plus binary Wronskian | wronskian family names |
| Classical constant dependence | binary alternating bilinear form | no combined LI/Wronskian result | binary polynomial identities | no finite Hasse criterion found | map_linearDependent |
| Abstract alternating family | map_linearDependent | exact abstract law | exact abstract law | determinant rows/columns laws | both determinant dependence laws |

Local search returned source results with index unavailable; this is not index-certified absence. External indices can differ from the pinned revision. Positive candidates were checked natively at the pin.

Existing blocks:
- AlternatingMap.map_linearDependent, Mathlib/LinearAlgebra/Alternating/Basic.lean:785: ring/domain, torsion-free target, arbitrary alternating map.
- Matrix.det_eq_zero_of_not_linearIndependent_cols, Matrix/Determinant/Basic.lean:496: domain-valued square matrix; dependence is over the matrix coefficient ring.
- LinearIndependent.restrict_scalars', LinearIndependent/Basic.lean:85: bigger-scalar independence implies smaller-scalar independence under faithful scalar action.
- LinearIndependent.of_comp, LinearIndependent/Defs.lean:312: independence after a linear map implies independence before it.
- LinearMap.pi: bundles the Hasse derivatives into one vector-valued linear map.
- Original proof blocks Fintype.not_linearIndependent_iff and Matrix.exists_mulVec_eq_zero_iff remain valid alternatives.

These are positive building-block findings, not a universal absence claim. Algebra.discr_zero_of_not_linearIndependent concerns a trace discriminant, a different determinant. Polynomial.wronskian concerns two inputs only. The analogous abstract law alone does not typecheck directly against φ: the Hasse family must first be represented as an alternating map or its column-independence bridge supplied.

## 5.5. Statement shape

Normal form: OK for a directional vanishing theorem. Equivalent forms are contrapositive W≠0→LinearIndependent and a nontrivial constant relation→W=0; the first aids nonvanishing uses, the second is already the proof witness. This is not an orthogonal equivalence; RHS-zero normal form is respected.

Syntactic generality: attempted raw domain determinant and abstract alternating-map statements natively. Keep h as a dependence hypothesis for the sole iff caller; upstream coefficient assumptions/parent representation should be restated before shipping. Superfluous-argument audit: K/l/φ/h all determine the conclusion or premise; Field is stronger than necessary only after expanding parents, CharZero already absent. Overall RESTATE-BEFORE-SHIP, conditional on upstream parent representation.

## 6. Callers and composition

Explicit same-project use count: **1**, all in the declaring file; external-to-file use count: **0**, external-to-file distinct files: **0**. These counts are source references, not opaque kernel dependency closure.

| Caller | Excerpt and mechanical replacement |
|---|---|
| Roth/Wronskian.lean:222, wronskian_eq_zero_iff | Second component of the iff proof is this theorem. Replace it by the four-call proof below if retaining local definitions; [actual caller experiment](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/native-caller-executed.lean.txt) compiles against the current conclusion without invoking this theorem or the old iff. Hard direction remains the independently proved project theorem. |

Inline audit: Roth/GenWronskian.lean:40–50 repeats the coefficient-witness/kernel argument for multivariate Hasse derivatives. This is an analogous broader-representation proof, not an exact univariate inline duplicate and not an explicit caller. The entire module was read. [Source copy](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/source-genwronskian.lean.txt). Its relationship strengthens the case for a shared operator-family bridge. No other such witness/kernel proof appeared in the project grep.

Attempt1: direct abstract AlternatingMap.map_linearDependent. Abstract version compiles in one call, but φ is not itself a supplied alternating map, so this does not give a direct old-form one-call proof.

Attempt2: determinant columns plus scalar restriction and bundled derivatives succeeds:
```lean
  apply Matrix.det_eq_zero_of_not_linearIndependent_cols
  intro hc
  exact h ((hc.restrict_scalars' R).of_comp
    (LinearMap.pi fun μ : Fin l ↦ Polynomial.hasseDeriv (μ : ℕ)))
```

[Exact isolated execution](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/native-composition-executed.lean.txt), [success receipt](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/native-composition-success.json). It uses **four** named existing calls, including LinearMap.pi; no hidden normalization premise or project helper. Matrix transposition/Function.comp align by elaboration. This is NOT-COMPOSABLE under the strict ≤3-call test **for the tested routes**, not a proof no three-call proof can ever exist. No exact? timeout is used as absence evidence.

The source witness proof is also an actual independently replayed composition experiment, but involves witness extraction, nonzero transfer and linearity normalization beyond three calls. No closing simp composition has been misclassified as NO. The parent definitions were BORDERLINE, not NO via a more-general D′, so the mandatory parent re-aim NO gate does not apply.

## 7. Verdict and action

**BORDERLINE-needs-human**, based on upstream API granularity and representation choice. The original statement is useful mathematics, the expanded ring theorem compiles, and the improved proof is almost entirely existing infrastructure. Evidence neither justifies an automatic ≤3-call NO nor establishes that this particular specialized API should be added independently of its parents.

Concrete future upstream questions, not blockers to this completed read-only assessment:

1. Should the finite Hasse Wronskian be bundled as an R-alternating map so this law is supplied by existing map_linearDependent?
2. Should a general scalar-linear-family determinant vanishing lemma be the shared API for the univariate and multivariate consumers, rather than separate witness proofs?
3. If a named finite Hasse Wronskian API is accepted, should its easy direction use CommRing+NoZeroDivisors (including the zero ring), while the converse retains characteristic-zero field assumptions?

Retain this theorem project-locally in Roth/Wronskian.lean until that upstream design is settled; an optional local proof cleanup can use the verified four-call bridge. If the generic route is selected, update the one explicit iff caller with the compiled fragment and refactor the multivariate analogous proof under its own assessment. Do not delete based on an inherited parent verdict.

YES-only PR-title/grouping/reviewer workflow: n/a, no YES claim. No production files, pins, Git or overview were modified by this worker.

## 8. Verification and audit package

[Verification index](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/verification.json) names exact executed sources and raw success receipts; [assessment metadata](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/assessment.json) records all phases. Accepted native checks have success=true, partial=false/absent, no errors/warnings, and only propext, Classical.choice, Quot.sound. Rejected name/weakening attempts are archived separately and never counted as accepted proof evidence. The current copy-manifest, not a historical worker manifest, is authoritative. [Portable validator](../evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/validate.py) checks source/pin hashes, native outcomes, axioms, links and current artifact hashes/bytes. Standard resource limits were retained; no sorry/new axioms/unsafe/native_decide were introduced.

