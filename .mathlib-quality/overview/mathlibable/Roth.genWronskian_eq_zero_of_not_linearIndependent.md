# Roth.genWronskian_eq_zero_of_not_linearIndependent

## Phase 0 — baseline

Declaration106, public theorem, Roth/GenWronskian.lean:41. The source and all17 baseline source/pin hashes freshly match the shared input manifest; reusable lake build exited0 with2467 jobs. The declaring module was read in full, along with its Hasse-derivative and univariate Wronskian dependencies. No sorry in the target. The module develops generalized Wronskians and reduces their nonvanishing criterion to one variable by Kronecker substitution.

[Fresh input hashes](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/inputs.json), [baseline build](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/baseline-build.txt), [full module](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/source-0.lean.txt).

## Phase 1 — comprehend

If finitely many multivariate polynomials are linearly dependent over their coefficient field, every square matrix obtained by applying a chosen Hasse derivative to each polynomial in each row has zero determinant. There are no order constraints on the row derivatives. Unlike the nonvanishing converse, this direction needs no characteristic-zero assumption and no finite variable type.

Full native type:
```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} {l : ℕ}
  (D : Fin l → σ →₀ ℕ) {φ : Fin l → MvPolynomial σ K},
  ¬LinearIndependent K φ → Roth.genWronskian D φ = 0
```

K is the coefficient field; σ the variable type; l the matrix size; D the derivative multi-index in each row; φ the column family; h its failure of linear independence over K. The proof extracts a nonzero constant relation g, embeds g as constant polynomials, applies each K-linear Hasse operator to the relation, and invokes the matrix nonzero-kernel-vector criterion over the polynomial domain. Scalar extension from K to K[σ] is essential: the dependence hypothesis is not already over the matrix coefficient ring.

## Phase 2 — preliminary checks

SMALL: the elementary vanishing direction, not the named main nonvanishing criterion. One-line definition test n/a: theorem, not a definition. Exhaustive literature width is unchanged.

## Phase 3 — exhaustive literature

Exact requests and response hashes/byte counts are retained; article/search bodies are not archived. No credential-bearing query URL is retained.

| Channel | Actual query/access | Finding |
|---|---|---|
| General web, specific | generalized Wronskian Hasse derivatives linearly dependent polynomials determinant zero | Pottmeyer, Diophantine Approximation §3.3, theorem3.3.7; dependence direction follows constant column relation. |
| General web, abstract | determinant linear maps evaluation linearly dependent vectors integral domain | Standard determinant/alternation and linear map framework; domain hypothesis must be retained for dependence→zero. |
| General web, aliases | Wronskian linear dependence easy direction arbitrary differential operators | Classical easy direction; analytic/converse assumptions must not be imported into this direction. |
| ChatGPT math MCP | n/a: ask_chatgpt_math unavailable | Optional server absent, no substitute channel invented. |
| Local references | clean.tex206–221 | Explicit generalized determinant definition and characteristic-zero-field lemma, proof uses only linearity and determinant alternation. |
| nLab | site:ncatlab.org/nlab Wronskian linear dependence; direct Wronskian page | Search finds Wronskian; direct fetch failed400 unsupported application/xhtml+xml. No uninspected full-page claim. |
| nCatLab | site:ncatlab.org/ncatlab determinant alternating linear dependence; direct determinant page | Search mostly resolves nLab; direct page inaccessible. No categorical generalization inferred. |
| Stacks Project | site:stacks.math.columbia.edu determinant linear dependence ring; direct0FJ9 | §15.120 finite projective module determinant/exterior powers. Useful abstract context, not an exact Hasse theorem. |
| MathOverflow | site:mathoverflow.net generalized Wronskians linear dependence | Questions487552/436759 distinguish different multivariate Wronskians; no single determinant supplies every converse. |
| recent arXiv | site:arxiv.org generalized Wronskian Hasse derivatives after:2021-10-27 before:2026-10-28 | Kiselev2511.03848 submitted5Nov2025; abstract defines determinants from selected multivariate derivative rows. Its Jacobi identities are different results. |

[Web specific/general/alias metadata](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/web-0.json), [nLab/nCatLab/Stacks queries](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/web-1.json), [MO/arXiv queries](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/web-2.json), [direct fetches/access failures](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/web-direct.json), [local source excerpt](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/local-literature.txt).

Primary locators: [Pottmeyer §3.3 theorem3.3.7](https://esaga.uni-due.de/f/lukas.pottmeyer/DioApp.pdf), [Stacks0FJ9](https://stacks.math.columbia.edu/tag/0FJ9), [Kiselev abstract](https://arxiv.org/abs/2511.03848). The ring/domain extension is supported by the determinant argument and checked mechanically; it is not attributed verbatim to a field-specific source.

Literature summary: generalized Wronskian vanishing under constant linear dependence is standard. Stronger analytic/characteristic assumptions govern converses, not this direction. The natural abstract form is a finite determinant of evaluations of scalar-linear maps into a domain with faithful base scalar action. A mere coefficient-ring zero-divisor dependence is insufficient.

## Phase 4a–4b — generality

| Parameter | Actual current form | Boundary and checked proposal |
|---|---|---|
| K | Field K | Domain coefficients suffice; CommRing+NoZeroDivisors also handles the zero ring by a separate trivial case. Plain CommRing is false. |
| σ | Type* | Already arbitrary; Fintype σ explicitly omitted. Infinite variable types require no change. |
| l | ℕ with Fin l indexing | Arbitrary finite square index ι is possible; no ordering is used. No positivity needed; empty dependence premise is false over a field. |
| D | Arbitrary multi-indices | No derivative order bound used; the nonvanishing theorem's degree≤row bound is irrelevant here. Replace by arbitrary scalar-linear maps in the abstract law. |
| φ | Polynomial family | The proof uses only its module structure and linearity of row operators. |
| h | ¬LinearIndependent K φ | Essential; an identity row on a singleton nonzero constant gives nonzero determinant. Scalar ring must be distinguished from the matrix's polynomial ring. |
| Characteristic | none | Already strongest possible in this dimension. |
| Universes | independent Type* | No fixed universe introduced by source statement. |

The original fixed parent spelling itself remains Field/Fin; widened statements use an explicitly expanded determinant/generalized parent representation, not a fictitious typeclass edit to the existing parent. No project parent is counted as a mathlib building block. The parent genWronskian was independently accepted YES-but-generalise-first, so ModeB's mandatory NO-parent re-aim rule does not fire.

Native weakening checks succeeded for domain/arbitrary finite index and CommRing+NoZeroDivisors. The floor proof handles subsingleton coefficients, then installs `NoZeroDivisors.to_isDomain R` explicitly. The plain-ring proposal is refuted by the checked singleton constant polynomial C(1,0) over ℤ×ℤ, annihilated by (0,1), whose zero-order determinant is nonzero.

Generality verdict: STRICTLY NARROWER in the expanded parent representation; this is a verified mathematical extension, while a YES-generalise verdict still requires deciding which upstream representation to expose.

Proposed polynomial restatement (definitionally the generalized-parent floor checked natively):
```lean
{R σ ι : Type*} [CommRing R] [NoZeroDivisors R]
  [Fintype ι] [DecidableEq ι] (D : ι → σ →₀ ℕ)
  {φ : ι → MvPolynomial σ R} (h : ¬ LinearIndependent R φ) :
  (Matrix.of fun i j ↦ hasseDeriv (D i) (φ j)).det = 0
```
The shared abstract candidate, checked in a mathlib-only environment, has parameters:
```lean
{R A M ι : Type*} [CommSemiring R] [CommRing A] [IsDomain A]
  [Algebra R A] [FaithfulSMul R A] [AddCommMonoid M] [Module R M]
  [Fintype ι] [DecidableEq ι] (δ : ι → M →ₗ[R] A) {v : ι → M}
  (h : ¬ LinearIndependent R v) :
  (Matrix.of fun i j ↦ δ i (v j)).det = 0
```

## Phase 4c — modern idiom

| # | Question | Answer and consequence |
|---|---|---|
| 1 | Typeclasses for bundled hypotheses? | Already uses Field; abstract source module and faithful algebra action are standard typeclasses. No new class proposed. |
| 2 | Sequences/metrics→filters? | No; finite algebra, no topology. |
| 3 | Construction→universal property? | No universal-property construction in this theorem. |
| 4 | Closure predicate→bundled substructure? | No; LinearIndependent already canonical. |
| 5 | Fields→modules/rings? | Yes; row linear maps over a scalar semiring and domain target, with faithful scalar action. Specialized polynomial vanishing extends to domain coefficients. |
| 6 | Higher categories? | No categorical structure relevant. |
| 7 | Concrete indices→arbitrary indices? | Yes; Fin l→arbitrary finite square index, with decidable equality for det. |
| 8 | Concrete-via-abstract? | Fires: genWronskian occurs0 times in proof body; Hasse operators occur only in applying linearity to a constant relation. Abstract determinant-of-linear-evaluations statement removes polynomial-specific coefficient manipulations. Enables Polynomial.hasseDeriv, MvPolynomial.hasseDeriv, and other linear operator families. |
| 9 | False-generalization guard? | Faithful algebra action/domain target preserves this dependence direction. Plain coefficient CommRing rejected by explicit product-ring counterexample. Arbitrary nonlinear operators would destroy transported relations and are excluded. |

Modern idiom available: yes, shared operator-family law or alternating-map presentation. This is useful for both univariate and multivariate source proofs, not categorification for appearance. The upstream choice is API granularity; no new mathematical theorem is inferred simply from the absence of a named wrapper.

## Phase 4.5 — infrastructure

n/a — theorem. All six definition-only rows (diamonds, reducibility, noncanonical unfolding, priorities, universes, coercions) are n/a because this declaration introduces neither data nor instances. The generalized parent representation has its own independent assessment; no infrastructure risk is inherited blindly.

## Phase 4.6 — proof strategy

| # | Diagnostic | Result |
|---|---|---|
| 1 | Topology εδ→filters | n/a, algebra. |
| 2 | Element argument→abstract algebra | Yes: replace explicit coefficient witnesses by column independence, scalar restriction, and LinearIndependent.of_comp. |
| 3 | Analysis sequences→nets | n/a, algebra. |
| 4 | Category construction→universal property | n/a, no categories. |
| 5 | Missing helpers mathlib should have | Optional scalar-linear determinant API; existing four-call bridge already proves it. No missing theorem assumed to exist. |

REFACTOR-RECOMMENDED; CHEAP. The matrix-column route eliminates g/constant-polynomial witness bookkeeping. It is a tested proposal, not a cost-based verdict downgrade.

## Phase 5 — exhaustive mathlib search

All five methods ran on current, literature-standard, and abstract forms. [Formal12 query/receipt index](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/formal-search.json); exact rg commands are separately retained for [current](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/rg-current.json), [standard](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/rg-standard.json), [abstract](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/rg-abstract.json).

| Method | Current | Literature-standard | Abstract |
|---|---|---|---|
| Finder | Binary polynomial Wronskian and discriminant near matches | Binary alternating Wronskian near matches | General determinant/norm context |
| Loogle | Project-only MvPolynomial.hasseDeriv unknown identifier; successful Matrix.det,_=0 retry | LinearIndependent,Matrix.det finds det dependence laws | LinearIndependent,_=0 finds dependence building blocks |
| LeanSearch | Binary Wronskian/discriminant | Binary Wronskian | det_eq_zero_of_not_linearIndependent_cols/rows |
| rg | No generalized Hasse Wronskian API hit | Binary Wronskian; trace discriminant | Exact column-dependence, scalar restriction and image independence APIs |
| Local | Project/scratch genWronskian names, not mathlib substitutes | Wronskian query empty | Exact det dependence source declarations |

Local index unavailable throughout: emptiness is not certified absence. External search snapshots may differ from the pinned revision. Positive candidates are source-inspected and natively checked. Failed Loogle current query is archived honestly, and its [successful retry](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/loogle-current-retry.json) is additional evidence.

Building blocks with exact pinned source paths:

- Matrix.det_eq_zero_of_not_linearIndependent_cols, Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean:496, requires dependence over the matrix domain.
- LinearIndependent.restrict_scalars', Mathlib/LinearAlgebra/LinearIndependent/Basic.lean:85, transfers independence to a faithfully acting smaller scalar ring.
- LinearIndependent.of_comp, Mathlib/LinearAlgebra/LinearIndependent/Defs.lean:312, transfers independence from an image back to its source family.
- LinearMap.pi bundles row operators into one vector-valued linear map.
- AlternatingMap.map_linearDependent, Mathlib/LinearAlgebra/Alternating/Basic.lean:785, supplies the law if an alternating-map representation is already given; ring/domain base and torsion-free target are required.
- Fintype.not_linearIndependent_iff and Matrix.exists_mulVec_eq_zero_iff supply the original longer witness proof; the latter also needs a domain.

Polynomial.wronskian is a binary object, and Algebra.discr_zero_of_not_linearIndependent concerns the trace discriminant, so neither is an exact substitute. Conclusion: positive building blocks, no verified direct existing law for the original project spelling. This is not a global absence proof.

## Phase 5.5 — statement shape

Normal form OK: vanishing conclusion has zero on RHS, and linear dependence is canonical ¬LinearIndependent. Equivalent forms: nonzero determinant→linear independence, or explicit nontrivial scalar relation→zero determinant. The first is the contrapositive; the second is a witness expansion rather than a new canonical relation predicate.

Syntactic generality attempts: arbitrary finite index/domain polynomial determinant, arbitrary scalar-linear row family, and a prebundled vector-valued linear map. The last needs only three existing calls, but creating that bundle from the original D adds LinearMap.pi, restoring four calls. The prebundled input cannot be claimed to be supplied by the original statement.

Superfluous arguments: no Fintype σ/CharZero/positive-l assumptions exist to drop. D/φ/h/l/σ/K all contribute mathematically or determine types. Field is stronger than necessary only after expanding/generalizing the parent definition. Overall RESTATE-BEFORE-SHIP conditional on the shared upstream API decision; no irreversible project edit is part of this assessment.

## Phase 6.0 — source callers and inline audit

Source named callers:0; occurrences excluding declaration:0; external-to-file named callers:0. No consumer proof replay is required because no source caller uses this theorem. This is an untagged theorem, so there is no simp-attribute implicit-use claim. Kernel proof references were audited separately over all293 canonical declarations: requested293, unique293, present293, values293, zero direct consumers.

| Caller | Usage/refactor |
|---|---|
| none | No explicit caller to replay or rewrite. |

The entire declaring module is read. The inline grep found the analogous univariate law at Roth/Wronskian.lean:65, whose constant-relation proof has the same structure. It is not an exact generalized statement re-derived inline and is not a source caller. Neither the Kronecker nonvanishing proof nor the separated-variable determinant source uses this theorem by name. [Source/caller evidence](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/callers.json), [exact grep](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/rg-callers.json), [inline audit](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/rg-inline.json).

## Phase 6 — composition

The key positive candidate is:
```lean
  Matrix.det_eq_zero_of_not_linearIndependent_cols fun hc ↦
    h (LinearIndependent.of_comp (LinearMap.pi fun i ↦ hasseDeriv (D i))
      (hc.restrict_scalars' K))
```

This has four named existing calls including LinearMap.pi. Counting only its three theorem calls would undercount the necessary bundle construction. Transpose/Function.comp alignment is by elaboration; no closing simp normalization is being smuggled into a NO result. A helper abstract_zero is newly proved, so applying it in one line is not an existing-mathlib one-call replacement.

The operator-family abstraction succeeds independently; with a supplied M →ₗ[R] (ι → A) bundle, the three-result-call term is exact. That does not settle the old form's upstream design. AlternatingMap.map_linearDependent likewise discharges an existing alternating object in one call, but constructing the original polynomial determinant as such an object is extra API work.

Strict≤3-call conclusion for the tested original-form routes: NOT-COMPOSABLE. This states the actual experiments, not a theorem ruling out every possible shorter proof. No exact? timeout or guessed nonexistent name is used as absence evidence.

## Phase 7 — verdict

**BORDERLINE-needs-human.** The mathematics is standard and the abstract proof uses existing infrastructure. A named generalized Wronskian API may justify its easy vanishing law, or an alternating/shared operator-family representation may make separate easy-direction laws redundant. The accepted parent is YES-generalise, not a forced existing D′ re-aim. No ≤3-call old-form proof was verified, and a four-call proof does not automatically warrant adding a specialized wrapper.

Concrete future upstream questions, not blockers to this read-only assessment:

1. Should the proposed generalized Hasse Wronskian API expose an alternating-map representation, making dependence vanishing an application of map_linearDependent?
2. Should one scalar-linear-family determinant lemma be the shared API for univariate and multivariate easy directions?
3. If a separate generalized Wronskian vanishing theorem is accepted, should it use arbitrary finite indices and CommRing+NoZeroDivisors, with the field spelling retained only as a corollary?

Keep the theorem in Roth/GenWronskian.lean while this design is settled. An optional project-local proof cleanup can use the verified four-call term; no source callers need changes. If the shared law is added upstream, replace the body with its application, and consolidate the analogous univariate law during that law's own refactor. Alternative destination is the existing project-local module: it records the paper's easy-direction lemma even though no current source proof calls it. Zero usage is a cleanup signal, not a proof the mathematics is junk.

YES-only PR title/grouping/reviewer/checklist n/a: this is a BORDERLINE assessment, not an upstream addition recommendation. No production source, pins, Git or progress records were modified.

## Phase 8 — evidence and handoff

[Verification index](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/verification.json), [phase metadata](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/assessment.json), and [portable validator](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/validate.py) link accepted exact executed sources and raw native receipts. Current copy-manifest governs all file hashes and bytes; historical manifests are not substituted. Full-file diagnostic errors/warnings/axioms are checked while positive audit assertions are scoped to each fresh native region. Accepted evidence uses standard axioms only; rejected attempts remain explicitly separate. Preparation files are not represented as clean execution receipts.

Native accepted artifacts: [original type/proof/axioms](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/gen-wronskian-zero-original-receipt.json), [specialization/zero-divisor/inlining exact source](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/gen-wronskian-zero-probes-executed.lean.txt), [clean receipt](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/gen-wronskian-zero-probes-receipt.json), [floor and canonical293 audit exact source](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/gen-wronskian-zero-floor-audit-executed.lean.txt), [clean receipt](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/gen-wronskian-zero-floor-audit-receipt.json), [isolated mathlib-only abstract experiment](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/gen-wronskian-zero-raw-executed.lean.txt), [raw receipt](../evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/gen-wronskian-zero-raw-receipt.json). The generalized parent representation's exact source/receipt is copied as a named verification prerequisite; its definition is not counted as an existing mathlib call.

Rejected native trials: two codomain inference failures, one IsDomain inference failure, and one letI linter warning. The second inference-failure source was reconstructed exactly by root from the executed edit and is labelled as such; its actual native failure receipt is retained. Final accepted sources fix codomain inference with explicit A/v arguments and use let for the local domain instance. None of the rejected outputs certifies a proof.
