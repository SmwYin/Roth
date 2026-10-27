# `Roth.coeff_wronskian_of_natDegree_injective`

**Verdict: YES-but-generalise-first (MODERN-IDIOM).** Contribute the coefficient formula for a determinant of Hasse derivatives over a commutative ring, with an arbitrary finite index and arbitrary natural derivative orders. The current historical name suggests an injectivity premise that the theorem no longer has. No production edits are proposed as part of this assessment.

## Phase 0 — Baseline and scope

The declaration resolves at `Roth/Wronskian.lean:122`. The shared successful `lake build` completed 2467 jobs; all 17 source/pin hashes were freshly compared and agree with that baseline. See [baseline](../evidence/Roth.coeff_wronskian_of_natDegree_injective/baseline-build.txt), [fresh hashes](../evidence/Roth.coeff_wronskian_of_natDegree_injective/source-pin-hashes.json), and [entire declaring module](../evidence/Roth.coeff_wronskian_of_natDegree_injective/source-wronskian.lean.txt). Root separately replayed the exact original proof, replacing only the private helper's identifier by its independently verified generic replay. Native diagnostics report success with no errors or warnings, and standard axioms only. See [target receipt](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-target-success.json) and [exact execution](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-target-executed.lean.txt).

This is a full assessment, not inherited from the parent Wronskian definitions or the binomial-determinant theorem. The matrix and determinant parents were assessed BORDERLINE; their independent mathematical laws must still be assessed. The declaration is public, outside examples/tests, not an `_aux`, and its docstring is not marked internal. The private coefficient-product helper is a reviewed SKIP, not an existing mathlib theorem or an accepted YES contribution.

## Phase 1 — Statement and proof

For any family of polynomials φ indexed by `Fin l`, put dν = natDegree(φν) and D = (Σdν) − (Σν), using truncated natural subtraction. The coefficient of Xᴰ in the determinant of the matrix of Hasse derivatives of orders 0,…,l−1 is the product of the leading coefficients times the determinant of the binomial matrix (choose(dν,μ)). This is an equality even when its right side vanishes. There is no assumption of nonzero polynomials, distinct degrees, characteristic zero, positive l, or linear independence.

The full type, as printed natively (universe names made explicit), is:

```lean
∀ {K : Type u} [Field K] {l : ℕ} {φ : Fin l → K[X]},
  (Roth.wronskian φ).coeff
      (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) =
    (∏ ν, (φ ν).leadingCoeff) *
      (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : K)).det
```

K is the coefficient type; its Field instance currently makes the project parent definitions available. l gives the finite family size, including the empty family. φ is arbitrary. The proof first computes the coefficient in each permutation product. If every row order is at most its matched column degree, the exponent is the sum of the individual degree bounds; the varying-bound coefficient-product lemma and `hasseDeriv_coeff` identify its coefficient. Otherwise a Hasse derivative and its binomial coefficient are both zero. The signed Leibniz expansions then assemble the determinant identity. This second branch is essential when truncated subtraction would otherwise obscure the degree count.

## Phase 2 — Preliminary checks

**SMALL by the actual command rule.** This is a helper coefficient calculation, not a new structure, not listed in the module's `Main results` bullets, and not a theorem named after a person/place: “Wronskian” names the object, rather than attributing this coefficient identity as Wroński's theorem. Its occurrence in `Implementation notes` does not make it a main-result bullet. The literature sweep remains exhaustive. The one-line-definition test is **n/a: theorem**, not a definition; the original proof is a substantive permutation calculation.

## Phase 3 — Exhaustive literature

Every named channel and the three distinct general-web queries were executed. The [literature ledger](../evidence/Roth.coeff_wronskian_of_natDegree_injective/literature.json) records each query, hit and limitation. Exact requests, response byte counts/SHA256, source titles and locators are in [general queries](../evidence/Roth.coeff_wronskian_of_natDegree_injective/web-general-metadata.json), [named channels](../evidence/Roth.coeff_wronskian_of_natDegree_injective/web-named-metadata.json), [recent queries](../evidence/Roth.coeff_wronskian_of_natDegree_injective/web-recent-metadata.json), [initial arXiv queries](../evidence/Roth.coeff_wronskian_of_natDegree_injective/web-arxiv-metadata.json), [opens](../evidence/Roth.coeff_wronskian_of_natDegree_injective/web-opens-metadata.json), [supplementary queries](../evidence/Roth.coeff_wronskian_of_natDegree_injective/web-supplement-metadata.json), and [primary opens](../evidence/Roth.coeff_wronskian_of_natDegree_injective/web-primary-metadata.json). Full returned bodies are not archived; URL query parameters are omitted from general returned locators as documented.

| Channel | Actual search / access | Finding |
|---|---|---|
| Web specific | Wronskian polynomials leading coefficient degrees binomial determinant Hasse | Monomial determinant and top coefficient mechanism identified. |
| Web general | Hasse Wronskian commutative ring polynomial leading coefficient determinant | Differential-ring and Hasse formulations; no retrieved source asserts this exact all-ring formula. |
| Web aliases | Wronskian Vandermonde leading term polynomial degrees falling factorial | Bostan–Dumas Lemma 1 supplies the ordinary-derivative monomial computation. |
| ChatGPT MCP | standard form/generality/history | n/a: `ask_chatgpt_math` unavailable. |
| Local | clean.tex §2, first lemma | Exact divided-derivative coefficient formula in the distinct-degree nonvanishing argument. |
| nLab | domain query and direct Wronskian page | Search hits; direct fetch rejected unsupported XHTML. |
| nCatLab | separate domain query and direct `/ncatlab/show/Wronskian` | No exact theorem; direct URL inaccessible. |
| Stacks | unquoted and quoted Wronskian domain queries | No relevant source locator returned. |
| MathOverflow | polynomial/degree/leading-coefficient queries | Context on basis recovery and Wronskian/Vandermonde determinants; no exact replacement. |
| arXiv, five years | 2024 polynomial and 2022 Hasse queries | Hermoso–Alcázar 2410.18867v1, 2024-10-24, §2 Proposition 2; inside the 2021-10-26–2026-10-26 window. |

The [local source excerpt](../evidence/Roth.coeff_wronskian_of_natDegree_injective/source-clean.tex.txt) is the closest exact source. [Bostan–Dumas, Lemma 1, pp.2–3](https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf) computes the Wronskian of monomials via falling factorials; it uses ordinary derivatives. [Hermoso–Alcázar, Proposition 2](https://arxiv.org/html/2410.18867v1#S2) uses the same leading-monomial mechanism for distinct-degree polynomials over characteristic-zero fields. These are evidence that the calculation is reusable beyond Roth's proof. The 2019 Hermite paper is supplementary historical context, not a recent-five-year result.

Hasse derivatives encode binomial coefficients without division; the Jeong 2008 author-upload search excerpt §2 confirms their arbitrary-characteristic formulation. Its DOI fetch failed, and the NSF generalized-Wronskian paper fetch timed out; neither was silently treated as a fully read primary source. The ring and arbitrary-row claims below are justified by actual native proofs, not attributed to those inaccessible texts. Standard forms vary between ordinary and divided derivatives, top polynomial degrees and lowest power-series orders, and consecutive and generalized row orders. The formal top-coefficient identity must retain its binomial determinant to stay valid in positive characteristic.

## Phase 4a–b — Generality

| Parameter / condition | Current form | Tested target / finding |
|---|---|---|
| Coefficients K | `[Field K]` | Expanded determinant formula verifies under `[CommRing K]`, including zero divisors and the zero ring. No inverses or domain cancellation are used. |
| Parent spelling | `Roth.wronskian` / `wronskianMatrix` have Field interfaces | Merely deleting Field in the original statement would not elaborate these parents. Use the raw determinant formula; no parent migration is required to contribute that theorem. |
| Family index | `Fin l` | Arbitrary `ι`, `[Fintype ι] [DecidableEq ι]`, verified. |
| Row schedule | natural value of `μ : Fin l` | Arbitrary `r : ι → ℕ`, verified; neither injectivity nor increasing order is required. |
| φ | arbitrary family | Retain; no nonzero/distinct-degree/independence binder exists to delete. |
| Exponents | natural degrees and natural derivative orders | Retain for polynomial/Hasse API. Natural subtraction and the zero branch are essential. |
| Characteristic / domain / nontriviality | no extra conditions | No need to add them; verified all-ring proof. |
| Universes and empty index | polymorphic K, natural l including zero | Generalized K and ι are independently universe-polymorphic; finite empty case handled by determinant/product conventions. |

**Current representation is strictly narrower than the verified modern target.** [Ring proof](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-ring-executed.lean.txt) and its [receipt](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-ring-success.json) preserve the source argument over a local generic W. [Finite arbitrary-row proof](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-finite-executed.lean.txt) and [receipt](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-finite-success.json) verify the stronger formulation. The local coefficient-product proof is new supporting proof, not an existing mathlib building block.

The proposed upstream signature is:

```lean
theorem Polynomial.coeff_det_hasseDeriv
    {R : Type u} [CommRing R] {ι : Type v} [Fintype ι] [DecidableEq ι]
    (r : ι → ℕ) (φ : ι → R[X]) :
    ((Matrix.of fun μ ν : ι ↦ hasseDeriv (r μ) (φ ν)).det).coeff
        (∑ ν, (φ ν).natDegree - ∑ μ, r μ) =
      (∏ ν, (φ ν).leadingCoeff) *
        (Matrix.of fun μ ν : ι ↦ ((φ ν).natDegree.choose (r μ) : R)).det
```

The exact declaration name remains a cleanup choice. This is a local mechanical restatement of this theorem's determinant expression; it does not depend on a multi-file redefinition of Roth's public parent API. Thus the “foundational API migration” false-positive rule does not force BORDERLINE here. The reason is MODERN-IDIOM; the retrieved literature does not itself establish that arbitrary commutative rings are the most commonly printed textbook form.

## Phase 4c — All modern-idiom checks

| # | Check | Answer, reformulation and concrete consequence |
|---|---|---|
| 1 | Typeclass preambles | Already class-based. Generalized signature uses existing CommRing/Fintype/DecidableEq; no new class. |
| 2 | Filters/topology | No; a finite polynomial identity has no convergence hypotheses. |
| 3 | Universal property | No constructed universal object; coefficient extraction is the needed operation. |
| 4 | Bundled substructures | No closure predicate/subspace is being represented ad hoc. |
| 5 | Field → ring/module hierarchy | Yes: CommRing determinant formula allows ℤ and rings with zero divisors, and use with existing polynomial Hasse coefficient/degree API before passing to a fraction field. |
| 6 | Higher category | No categorical structure or coherence law here. |
| 7 | Concrete index | Yes: replace Fin l row schedule by arbitrary finite ι and r : ι → ℕ; use with Matrix reindexing and generalized Hasse minors without choosing an ordered enumeration first. ℕ derivative orders remain intrinsic. |
| 8 | Concrete-via-abstract diagnostic | Yes, scoped carefully: proof body mentions the project Wronskian only on its final unfolding line, then zero later occurrences. It actually computes a raw determinant. The arbitrary-row finite proof verifies removal of the consecutive-order witness; no claim of a fully arbitrary weighted-polynomial-matrix theorem was made. |
| 9 | False-generalization guard | Pass: the Fin.val specialization recovers exactly the same Hasse determinant. Do not replace Hasse by ordinary derivatives in positive characteristic; do not assert the displayed coefficient is the actual leading coefficient when it is zero. |

**Modern idiom available: yes.** It removes a field restriction created by the surrounding definitions and exposes the finite determinant API with arbitrary row orders. This enables integral and positive-characteristic use of the binomial coefficient formula and existing matrix reindexing, rather than merely changing notation.

## Phase 4.5 — Infrastructure risk

n/a: theorem. It introduces no new definition, class, instance, coercion, reducibility setting or universe equation. Therefore the six definition-only rows (typeclass diamond, reducibility leak, noncanonical unfolding, instance priority, universe constraints, coercion ambiguity) do not apply. A future decision to add a named n-ary Wronskian definition needs the separate parent assessments; this formula can be stated on an existing Matrix expression.

## Phase 4.6 — Proof strategy

| # | Check | Finding |
|---|---|---|
| 1 | Topology / ε–δ | n/a; no topology. |
| 2 | Elements versus subobjects | No ideal/submodule inclusion encodes this scalar coefficient equality more directly; permutation expansion is appropriate. |
| 3 | Sequences versus nets | n/a; no limits. |
| 4 | Constructed categorical object | n/a; no universal property. |
| 5 | Missing supporting API | Yes: varying individual degree bounds in coefficient products. The existing same-bound theorem uses `s.card * n`; the local helper uses `∑ i ∈ s, n i`. That helper can shorten the source without pretending it already exists upstream. |

**MATHLIB-IDIOMATIC**, with a small API extraction opportunity: retain the permutation-product zero/nonzero split, then signed determinant assembly; generalize the product helper separately or keep it private to the upstream proof. A more abstract polynomial-matrix top-coefficient theorem might organize this further, but arbitrary truncated shifts need explicit zero-entry conditions and have not been asserted or verified here.

## Phase 5 — Five actual mathlib methods, all three forms

Exact requests and complete raw formal-search receipts: [current](../evidence/Roth.coeff_wronskian_of_natDegree_injective/formal-current.json), [literature](../evidence/Roth.coeff_wronskian_of_natDegree_injective/formal-literature.json), [abstract](../evidence/Roth.coeff_wronskian_of_natDegree_injective/formal-abstract.json). Pinned full-source searches: [current](../evidence/Roth.coeff_wronskian_of_natDegree_injective/rg-current.json), [literature](../evidence/Roth.coeff_wronskian_of_natDegree_injective/rg-literature.json), [abstract](../evidence/Roth.coeff_wronskian_of_natDegree_injective/rg-abstract.json). No output was truncated in these archives.

| Method | Current coefficient-Wronskian form | Literature Hasse/leading-term form | Abstract polynomial-matrix form |
|---|---|---|---|
| Finder | Binary Wronskian and coefficient-matrix triangular lemma | Binary Wronskian, Hasse and degree tools | Affine polynomial determinant top coefficient; evaluated monic-polynomial matrices |
| Loogle | `Polynomial.coeff, Matrix.det` | `"wronskian"` | `Matrix.det, Polynomial.natDegree` |
| LeanSearch | Coefficient of finite Wronskian query | Leading Hasse divided-Wronskian query | Shifted-degree determinant coefficient query |
| rg | Full target name and coeff/Wronskian | Hasse/determinant and Wronskian terms | coeff_det, det_matrixOfPolynomials, coefficient-product terms |
| local | coeff_wronskian | wronskian | coeff_det |

The local tool reports `index: unavailable`; it did return source-name candidates, but that is not an exhaustive local-index absence result. External search versions can differ from this project's pin. Positive candidates were checked against pinned source and natively; their precise types matter.

`Polynomial.wronskian` in `Mathlib/RingTheory/Polynomial/Wronskian.lean` treats two polynomials and explicitly TODOs n-tuples. `Polynomial.coeff_det_X_add_C_card` at `Mathlib/LinearAlgebra/Matrix/Polynomial.lean:72` extracts the coefficient of card ι from a matrix affine in X with common degree bound 1. `coeff_det_X_add_C_zero` at line62 handles its constant coefficient. `Matrix.det_matrixOfPolynomials` at `Mathlib/LinearAlgebra/Matrix/Block.lean:417` concerns the scalar coefficient matrix of a family of monic polynomials of degrees exactly their indices, with determinant 1. None is the shifted, arbitrary-degree Hasse determinant coefficient law. The common-bound `Polynomial.coeff_prod_of_natDegree_le` at `Algebra/Polynomial/BigOperators.lean:230` does not supply the varying-bound step by a single specialization.

The concrete gap is the n-ary Hasse determinant's top-possible-coefficient law, adjacent to the existing n-tuple Wronskian TODO. Searches found useful primitives, not an exact or more-general replacement. This is a bounded search conclusion with native composition experiments, not an absolute proof of absence.

## Phase 5.5 — Statement shape

Normal form: coefficient at the explicit possible top degree, equal to a scalar product times a binomial determinant. An actual `leadingCoeff` or `natDegree = D` statement would require nonvanishing information; over positive-characteristic rings the binomial determinant can vanish. An ordinary-derivative version includes row factorials and is not interchangeable without conditions. These are meaningful alternative forms, but the coefficient equality remains the canonical useful unconditional RHS computation.

Syntactic alternatives attempted: raw determinant over CommRing; arbitrary row orders; arbitrary finite index; specialize back to Fin.val and the original public statement. They avoid selecting an enumeration or proving nonzero polynomials merely to apply a coefficient identity. Existing φ is implicit for inference; proposed primary φ can be explicit for discoverability. No assumed degree injectivity is present. Field is required only by the project parent spelling, not by the expanded theorem; Fintype supplies finite sums/permutations, DecidableEq supplies the matrix determinant interface, r supplies intrinsic natural Hasse orders. No remaining superfluous mathematical hypotheses were identified.

**RESTATE-BEFORE-SHIP:** use the raw finite arbitrary-row CommRing formula and a name such as `coeff_det_hasseDeriv`. Do not ship the historical `_of_natDegree_injective` name as a primary upstream name.

## Phase 6.0 — Callers and inline audit

| Caller | Excerpt / role | Future update |
|---|---|---|
| `Roth/Wronskian.lean:148–152`, `wronskian_ne_zero_of_natDegree_injective` | `using coeff_wronskian_of_natDegree_injective (φ := φ)` after the nonzero determinant simplification | Replace this term with the upstream generalized coefficient theorem at r = Fin.val; unfold only the local Wronskian spelling if required. |

Internal use count by the command's external-to-declaring-file convention: **0**; external-to-file callers: **0 files**. There is **one** explicit same-file proof caller, above. The implementation-note mention at line41 is prose, not a proof caller. This accounting is source-level explicit references, not an opaque kernel/simp dependency closure. The target has no simp attribute. [Caller and inline audit receipt](../evidence/Roth.coeff_wronskian_of_natDegree_injective/rg-callers.json) found no other inline rederivation of this coefficient formula; generalized-Wronskian code uses a different determinant expansion. This is not dead code: its sole local use supplies the distinct-degree nonvanishing base case used downstream.

## Phase 6 — Actual composition experiments

1. Isolated `exact?` on the raw ring identity failed to close the goal under default resources, without timeout. This is evidence of this attempted route only.
2. `simp [W, Matrix.det_apply', finsetSum_coeff]` leaves the genuine permutation-product coefficient equality. It did not close the goal. See [exact rejected experiment](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-composition-executed.lean.txt) and [raw rejection](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-composition-rejected.json). Rejected evidence is not accepted proof evidence. The finite probe initially emitted formatting warnings; [that rejected intermediate receipt](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-finite-warnings-rejected.json) is separate from the final clean proof evidence.
3. Existing affine determinant coefficient lemmas cannot represent a generic polynomial Hasse matrix (the row-zero entry can have arbitrary degree), and the monic scalar coefficient-matrix determinant has different hypotheses and conclusion. Coefficient extraction at positive degree is additive, not a ring homomorphism, so `map_det` cannot move it through the determinant.
4. The independent generic proof and the reconstruction of the sole caller succeeded. Those are new proof evidence and a project specialization, not a ≤3-call derivation from existing mathlib.

**NOT-COMPOSABLE by the tested existing routes.** The needed permutation degree/zero split and varying-bound product step are mathematical reasoning. No closing trivial-simp composition was found; hence Phase6b's special BORDERLINE simp rule does not fire.

## Phase 7 — Actionable verdict

**YES-but-generalise-first, MODERN-IDIOM.** The native proof establishes a reusable arbitrary-ring law of a finite determinant of Hasse derivatives. The source's single nonvanishing caller needs the identity only as a specialization; the mathematical content is broader than its historical name and surrounding Field interface. The concrete upstream anchor is the n-tuple TODO in the pinned polynomial-Wronskian module, while existing matrix-polynomial coefficient lemmas cover affine common-degree cases. This theorem computes arbitrary Hasse-determinant coefficients and is substantial beyond those primitives.

Contribute the raw formula to **`Mathlib/RingTheory/Polynomial/Wronskian.lean`**, importing the necessary Hasse derivative and determinant API; consider a dedicated n-ary extension file if maintainers prefer to avoid import growth in the binary module. Proposed PR title: **“feat(Polynomial): compute the top coefficient of finite Hasse derivative determinants”**. Group with the already accepted YES-generalise `Roth.det_choose_eq` (canonical43), whose cancellation-free binomial determinant formula supplies the next mathematical step. Do not label private helper44 or the BORDERLINE parent definitions as accepted YES declarations. Other accepted multivariable Hasse API results are separate subject-grain contributions, not a reason to enlarge this PR.

Future local integration is concrete: keep the present parents untouched, introduce/use the upstream raw theorem, specialize r to Fin.val, and replace the sole line152 term. The [native recovery and caller source](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-caller-executed.lean.txt) and [successful receipt](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-caller-success.json) validate this bridge. The finite receipt also checks the pinned affine/triangular candidate signatures; its expanded theorem exposes the exact raw formula without the local W wrapper. A future parent-definition design change is independent. If upstream declines an n-ary API, `Roth/Wronskian.lean` remains the justified project-local destination; this is a useful coefficient lemma rather than junk.

Pre-PR checklist:

- [ ] `/generalise Roth.coeff_wronskian_of_natDegree_injective` using the verified raw ring/finite-row signature; do not suggest deleting already absent binders.
- [ ] `/cleanup Roth/Wronskian.lean Roth.coeff_wronskian_of_natDegree_injective`; rename the historical theorem, settle helper visibility and preserve the zero branch.
- [ ] Coordinate with the accepted `Roth.det_choose_eq` contribution and assess imports in the upstream destination.
- [ ] Invite Moritz Firsching for the Hasse-derivative interface: the recent pinned history includes commit `334438dace` on `hasseDeriv_map`; coordinate with the polynomial-Wronskian maintainers. See [reviewer history](../evidence/Roth.coeff_wronskian_of_natDegree_injective/reviewer-history.json).

The assessment is complete with no verification obligations left open. These are future actions, not production edits or an attempted upstream submission.

## Phase 8 — Verification, completion and handoff

All required phases are complete; `unresolved = []`. The [verification ledger](../evidence/Roth.coeff_wronskian_of_natDegree_injective/verification.json) identifies the exact archived sources and raw receipts for four clean accepted executions: [original target replay](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-target-success.json), [CommRing replay](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-ring-success.json), [arbitrary finite-index/order identity and expanded formula](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-finite-success.json), and [original-statement recovery and sole caller reconstruction](../evidence/Roth.coeff_wronskian_of_natDegree_injective/native-caller-success.json). Each accepted execution finishes successfully with no warning/error, no partial result, no timeout, and only `propext`, `Classical.choice`, and `Quot.sound` among printed axioms. Exact executed source files are linked by the verification ledger and their SHA256 values are checked.

The failed `exact?`/`simp` composition experiment and the intermediate finite-probe formatting warnings are preserved separately as rejected evidence. They are not counted as accepted proofs. The caller reconstruction verifies the original theorem's specialization and the changed coefficient-lemma fragment in its sole consumer; it is not a fresh full-project build of proposed production changes. Production source and pins remain unchanged, and the reusable full-project baseline is supported by the fresh matching 17-input hash check.

The [current copy manifest](../evidence/Roth.coeff_wronskian_of_natDegree_injective/copy-manifest.json) lists every supporting artifact's source, destination, SHA256 and byte count. The [portable read-only validator](../evidence/Roth.coeff_wronskian_of_natDegree_injective/validate.py) validates that current manifest in scratch or integrated layouts, phase completion, exact accepted source/receipt relationships, clean native success, standard axioms, source/pin hashes and report links. The [credential-guard receipt](../evidence/Roth.coeff_wronskian_of_natDegree_injective/secret-scan-receipt.json) records a successful targeted credential/signed-URL scan. The package is frozen for root's independent acceptance; `root_acceptance = pending` is intentional and does not leave mathematical verification unresolved. No production edits, Git actions or upstream submission were made.
