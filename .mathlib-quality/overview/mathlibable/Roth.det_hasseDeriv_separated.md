# Roth.det_hasseDeriv_separated — BORDERLINE-needs-human

Canonical declaration169, Roth/Separation.lean:351. This is a completed read-only assessment; upstream API questions remain design choices, not unresolved verification. Production sources and pins remain unchanged.

## Phase 0 — baseline and provenance

The shared `lake build` succeeded (2467jobs, exit0). Fresh hashes of all17 source/pin inputs match its manifest, so the build remains reusable. The target resolves to an actual theorem without sorry, with only `propext`, `Classical.choice`, `Quot.sound`. The module separates one distinguished variable, obtains a determinant factorization, and descends rational factors to integer polynomials.

Evidence: [baseline-build.txt](../evidence/Roth.det_hasseDeriv_separated/baseline-build.txt), [input-manifest.json](../evidence/Roth.det_hasseDeriv_separated/input-manifest.json), [inputs.json](../evidence/Roth.det_hasseDeriv_separated/inputs.json), [source-module.lean.txt](../evidence/Roth.det_hasseDeriv_separated/source-module.lean.txt), [canonical-target.json](../evidence/Roth.det_hasseDeriv_separated/canonical-target.json).

## Phase 1 — statement and proof

For a separated sum P(x,y)=∑ρ φρ(y)ψρ(x), form the square matrix whose (μ,ν) entry is the mixed Hasse derivative of P with multivariate order Dμ and univariate order ν. Its determinant is the product of the generalized Hasse Wronskian of ψ and the univariate Hasse Wronskian of φ, each embedded in the common polynomial ring. Neither independence, nonzero factors, characteristic zero, positive family size, nor bounds on D are assumptions.

The exact native type, including universes and finite binders, is:

```lean
∀ {τ : Type u_1} {K : Type u_2} [inst : Field K] {l : ℕ} (D : Fin l → τ →₀ ℕ)
  (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K),
  (Matrix.of fun (μ ν : Fin l) ↦
        (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν))
          (∑ ρ : Fin l, (Polynomial.aeval (X none)) (φ ρ) * (rename some) (ψ ρ))).det =
    (rename some) (genWronskian D ψ) * (Polynomial.aeval (X none)) (wronskian φ)
```

Parameters: arbitrary variable type τ; coefficient field K; natural l (including0); D:Fin l→(τ→₀ℕ); families φ:Fin l→K[X] and ψ:Fin l→K[τ]. The omitted ambient Fintype/DecidableEq τ instances do not appear in the type. The result is a polynomial equality, not a nonvanishing criterion.

Mathematically put Aμρ=ΔDμψρ and Bνρ=Hνφρ. Linearity and disjoint-variable differentiation identify the left matrix with A·Bᵀ. `Matrix.det_mul`, `Matrix.det_transpose` and two `AlgHom.map_det` transports give the result. The actual matrix-entry identification still uses project `Roth.hasseDeriv_rename_mul_aeval`; the determinant identities alone do not supply it.

Evidence: [native-type.json](../evidence/Roth.det_hasseDeriv_separated/native-type.json), [det-separated-original-audit-receipt.json](../evidence/Roth.det_hasseDeriv_separated/det-separated-original-audit-receipt.json), [det-separated-original-executed.lean.txt](../evidence/Roth.det_hasseDeriv_separated/det-separated-original-executed.lean.txt), [det-separated-context-receipt.json](../evidence/Roth.det_hasseDeriv_separated/det-separated-context-receipt.json).

The raw `#print` body explicitly elides1309characters. This report does not claim a complete printed kernel body; complete executed sources, full native type/axioms, and a kernel-value consumer audit are archived.

## Phase 2 — preliminary checks

**BIG**: the declaration is explicitly listed among the module's main results and packages its determinant factorization. This does not alter the exhaustive search width. One-line definition check: **n/a**, kind theorem; no definition-only exemption is invoked. Its proof performs bundled determinant rewrites followed by entrywise normalization.

## Phase 3 — exhaustive literature search

Every named channel was attempted; the protocol's historical “nine-channel” wording does not change the actual rows below. Exact requests, returned-response SHA256/byte counts, titles, locators and original concise summaries are archived without result/article bodies.

| Channel | Actual query or locator | Outcome |
|---|---|---|
| web-current | `Hasse derivative separated variables determinant Wronskian Roth theorem` | [Hasse-normalized Wronskians occur in algebraic linear-independence arguments; the returned Roth exposition uses normalized partial derivatives. No exact separated determinant law was located by this query.](../evidence/Roth.det_hasseDeriv_separated/web-current.json) |
| web-general | `determinant product transpose matrices commutative ring multiplicativity` | [Determinant multiplicativity and invariance under transpose are textbook matrix identities. The ring setting is supplied explicitly by the Stacks primary source and the pinned mathlib theorem, rather than assumed from introductory field examples.](../evidence/Roth.det_hasseDeriv_separated/web-general.json) |
| web-alias | `generalized Wronskian separated sum factorization determinant Roth lemma` | [Generalized Wronskians are standard in Roth proofs. Returned lecture notes and Bostan–Dumas discuss them; the exact separated-sum factorization is clearest in local clean.tex.](../evidence/Roth.det_hasseDeriv_separated/web-alias.json) |
| nlab | `site:ncatlab.org/nlab determinant commutative ring` | [The determinant article describes a universal alternating construction and matrices over commutative rings. Direct page retrieval separately failed with unsupported XHTML; the search excerpt is retained only as metadata.](../evidence/Roth.det_hasseDeriv_separated/nlab.json) |
| ncatlab | `site:ncatlab.org/ncatlab determinant matrix commutative ring` | [The exact nCatLab namespace query returned nLab pages, not an exact /ncatlab result. This is an honest out-of-namespace result, not evidence of absence.](../evidence/Roth.det_hasseDeriv_separated/ncatlab.json) |
| stacks | `site:stacks.math.columbia.edu determinant matrix multiplicativity commutative ring` | [Stacks Section 15.120 treats determinants of finite projective modules and multiplicativity over a ring. It supports the abstract ring-general formulation, not the specialized Hasse separation identity.](../evidence/Roth.det_hasseDeriv_separated/stacks.json) |
| mathoverflow | `site:mathoverflow.net Hasse derivative generalized Wronskian positive characteristic` | [Questions concern divided derivatives in characteristic p and differential operators over integers. They distinguish Hasse derivatives from ordinary derivatives; no exact separated determinant theorem was located.](../evidence/Roth.det_hasseDeriv_separated/mathoverflow.json) |
| arxiv | `site:arxiv.org/abs/ generalized Wronskian Hasse derivatives after:2021-10-27 before:2026-10-28` | [The dated query returned Kiselev's 2025 generalized Wronskian paper and unrelated results. The primary abstract concerns jet-indexed derivative determinants and Jacobi identities, not the separated product identity.](../evidence/Roth.det_hasseDeriv_separated/arxiv.json) |
| Optional mathematical second opinion | Standard form/generality/history question recorded | n/a: `ask_chatgpt_math` is unavailable; other channels were still executed. |
| Local references | clean.tex §2, Lemma2 proof lines377–418 | Exact A·Bᵀ factorization and normalized derivatives. |

The local source gives exactly this factorization in the rational setting of Roth's proof. Its field, nonzero and independence conditions belong to the surrounding decomposition/nonvanishing argument; they are not used by the determinant identity itself. The [Stacks determinant construction](https://stacks.math.columbia.edu/tag/0FJ9), opening paragraphs, places multiplicativity over rings and finite projective modules. The [2022 Roth exposition](https://aleksa-milojevic.github.io/expository/roth.pdf), §3 and Lemma5.2, supplies related normalized-derivative and generalized-Wronskian context. These references support the standard matrix-factorization mechanism; the ring-level Hasse identity is independently verified here, not attributed verbatim to either exposition.

[Kiselev's2025 paper](https://arxiv.org/abs/2511.03848), abstract, studies generalized derivative-indexed Wronskians and Jacobi identities, a contemporary related setting rather than the exact separated-sum law. The nLab direct fetch failed on unsupported XHTML; only the search excerpt is available. The exact nCatLab `/ncatlab` query returned `/nlab` results, which is recorded honestly. MathOverflow supplied related Hasse/divided-derivative discussions without an exact theorem. No failure/empty/near-match is treated as an absence proof.

Literature summary: generalized Wronskians and multiplicativity of determinant are standard; the specific factorization is a standard step in Roth's separation argument. The most general mechanism is determinant of a finite square matrix product over a commutative ring; specializing it to separated Hasse operators needs a disjoint-coordinate product law. Factorial division is not part of the Hasse formulation and no characteristic hypothesis is needed. Ring coefficients, arbitrary finite index, arbitrary selected univariate derivative orders, and a fresh coordinate outside an injected variable set preserve this identity.

Evidence: [literature-individual.json](../evidence/Roth.det_hasseDeriv_separated/literature-individual.json), [literature-availability.json](../evidence/Roth.det_hasseDeriv_separated/literature-availability.json), [clean-excerpt.tex.txt](../evidence/Roth.det_hasseDeriv_separated/clean-excerpt.tex.txt), [local-literature-search.json](../evidence/Roth.det_hasseDeriv_separated/local-literature-search.json), [primary-stacks.json](../evidence/Roth.det_hasseDeriv_separated/primary-stacks.json), [primary-nlab.json](../evidence/Roth.det_hasseDeriv_separated/primary-nlab.json), [primary-arxiv.json](../evidence/Roth.det_hasseDeriv_separated/primary-arxiv.json), [primary-roth-locator.json](../evidence/Roth.det_hasseDeriv_separated/primary-roth-locator.json).

## Phase 4a — every parameter and hypothesis

| Parameter/hypothesis | Current form | Sufficient general form and evidence |
|---|---|---|
| K, `[Field K]` | Field interface of named Wronskians | Expanded full identity compiles over `[CommRing R]`; no inverses/domain/nontriviality used. Named parents still require Field, verified separately. |
| τ | Arbitrary Type universe | Already arbitrary, no finiteness/decidability instance to drop. |
| l | Any natural, including0 | Any finite square type ι with Fintype/DecidableEq compiles; the abstract isolated proof explicitly includes Fin0. |
| D | Arbitrary row multiorders | No order≤row bound, distinctness or nonzero restriction needed. |
| ν's order | Standard Fin.val sequence | Arbitrary E:ι→ℕ compiles; standard Wronskian is its Fin.val specialization. |
| φ,ψ | Arbitrary finite families | No linear independence, nonvanishing or degree premise to drop. |
| Option τ / some / none | Disjoint coordinate presentation | Arbitrary injection f:τ→σ and i outside its range compiles; unused ambient variables allowed. |
| Commutativity/signs | Supplied by Field | CommRing is sufficient. Existing signed determinant and `AlgHom.map_det` require CommRing. Merely replacing it by CommSemiring or a noncommutative Ring does not preserve this determinant interface. |

## Phase 4b — verified generality

The current result is **STRICTLY NARROWER at the expanded mathematical level** than the verified sufficient generality, while the **original named conclusion has a fixed Field parent interface**. This distinction is essential: replacing `[Field K]` alone is not a valid edit to the original signature. The clean negative parent-floor probe confirms that `Field R` cannot be synthesized and the original named Wronskians cannot be formed at arbitrary CommRing coefficients. The original full conclusion is recovered by the compiled `originalViaRing169` bridge, unfolding only genWronskian, wronskian and wronskianMatrix; its full source caller also recompiles through this bridge. The strongest `freshOrders169` law likewise specializes via `originalViaFresh169`, with a third full caller replay.

Verified candidate (body omitted from this display; the exact successful proof is archived):

```lean
theorem freshOrders169 {ι : Type*} [Fintype ι] [DecidableEq ι]
    (f : τ → σ) (hf : Function.Injective f) (i : σ) (hi : ∀ j, f j ≠ i)
    (E : ι → ℕ) (D : ι → (τ →₀ ℕ)) (φ : ι → Polynomial R)
    (ψ : ι → MvPolynomial τ R) :
    (Matrix.of fun μ ν : ι ↦ hasseDeriv ((D μ).mapDomain f + Finsupp.single i (E ν))
        (∑ ρ, Polynomial.aeval (X i : MvPolynomial σ R) (φ ρ) *
          rename f (ψ ρ))).det = rename f ((Matrix.of fun μ ρ ↦ hasseDeriv (D μ) (ψ ρ)).det) *
      Polynomial.aeval (X i : MvPolynomial σ R)
        ((Matrix.of fun ν ρ : ι ↦ Polynomial.hasseDeriv (E ν) (φ ρ)).det)
```

This identity keeps the actual mixed Hasse derivative of the entire separated sum on the left and both embedded determinants on the right. It does not replace the conclusion by an abstract matrix premise or delete degree/independence conditions from a different theorem. Fresh-coordinate transport and the full determinant law were newly checked for169; declaration160's verdict was not inherited.

Work consists of choosing the public finite-family Wronskian API and arranging its parent definitions/imports, plus applying the already verified proofs. Under the command's false-positive class5, changing foundational named parents across Wronskian/GenWronskian is a design restatement rather than a single mechanical hypothesis weakening. Cost does not determine the verdict.

Evidence: [det-separated-guards-receipt.json](../evidence/Roth.det_hasseDeriv_separated/det-separated-guards-receipt.json), [det-separated-bridge-orders-receipt.json](../evidence/Roth.det_hasseDeriv_separated/det-separated-bridge-orders-receipt.json), [det-separated-fresh-receipt.json](../evidence/Roth.det_hasseDeriv_separated/det-separated-fresh-receipt.json), [det-separated-semantic-guard-receipt.json](../evidence/Roth.det_hasseDeriv_separated/det-separated-semantic-guard-receipt.json).

## Phase 4c — all modern-idiom rows

| # | Question | Assessment and concrete consequence |
|---|---|---|
| 1 | Typeclasses instead of preambles | Already uses Field; proposed CommRing is the sufficient scalar typeclass. No new bespoke class is needed. |
| 2 | Filters/nets instead of sequences | No: finite algebraic identity, no topology or limiting process. |
| 3 | Universal property instead of construction | No new object is constructed; homomorphism compatibility already uses `AlgHom.map_det`. Determinant's exterior-power description does not remove the derivative-entry bridge. |
| 4 | Bundled substructures | No subset-with-closure predicate occurs. Existing AlgHom embeddings are already bundled. |
| 5 | Field→module/(semi)ring hierarchy | Yes, CommRing expanded law verified. It applies directly over ℤ, finite characteristic and zero rings and composes with ring/AlgHom determinant transport, where the current named Field wrappers block elaboration. |
| 6 | Higher-categorical formulation | No: no categorical coherence problem or concrete downstream gain identified. |
| 7 | Concrete indices→abstract indices | Yes: arbitrary finite square ι and orders E replace Fin l / Fin.val in the expanded law. This composes directly with matrix reindexing and arbitrary Hasse row selections; retain natural-valued derivative orders. |
| 8 | Concrete-via-abstract proof diagnostic | Fires for named Wronskians: genWronskian and wronskian occur only in the initial unfolding; afterward0 occurrences. The determinant core is the existing abstract det_mul+transpose law. However the factorwise derivative identification remains substantive, so this is not evidence the entire result already exists. |
| 9 | False-generalization guard | Ring/arbitraryorders/injected fresh-coordinate versions preserve the same polynomial identity and specialize back. Dropping separation is rejected: the isolated ℤ counterexample has H₁(X·X)=2X while H₁(X)·X=X (coefficient1 gives2≠1). This is the singleton arbitrary-order case, not a nonvanishing test. |

Modern idiom available: **yes**, with real scalar/index/embedding consequences; the abstract determinant part is already mathlib API. Whether the specialized derivative bridge deserves a public determinant lemma or just a public matrix-entry lemma remains an upstream API-grain question. No categorical novelty is asserted.

## Phase 4.5 — infrastructure risks

**n/a: theorem**, not a def/class/instance. Typeclass diamond, reducibility leak, noncanonical unfolding, instance priority collision, universe-polymorphism and coercion-ambiguity introduction are therefore not new infrastructure introduced by this declaration. Parent-definition design is explicitly handled in4b/7; no definition was silently proposed as a new instance.

## Phase 4.6 — all proof-strategy rows

| # | Question | Result |
|---|---|---|
| 1 | ε–δ vs filters | n/a, no topology. |
| 2 | Elements vs ideal/submodule inclusions | No such inclusions; Matrix.ext is the correct finite-entry bridge after bundled determinant transport. |
| 3 | Sequences vs nets | n/a, no analysis. |
| 4 | Construction vs universal property | No constructed categorical object; exterior-power abstraction would not simplify disjoint Hasse differentiation. |
| 5 | Helpers that mathlib should have | Yes: multivariate Hasse derivative API and its injected fresh-coordinate factorwise law; possibly a finite-family Hasse-Wronskian interface. Existing project helpers are not existing mathlib replacements. |

**MATHLIB-IDIOMATIC**: identify A·Bᵀ, then multiplicativity/transpose/naturality. An optional public matrix-factorization helper could separate the missing derivative normalization from the existing determinant core; this is the concrete API question in7. No coefficient expansion of determinants is recommended.

## Phase 5 — actual five methods × three forms

All15 cells were executed; raw tool requests/responses and full untruncated rg receipts are linked by the machine-readable grid. Finder uses its v4.28 default index, which may differ from the pin. Local searches return source hits with `index: unavailable`, so they do not establish index-complete absence.

| Form | Finder | Loogle | LeanSearch | Source rg | Local |
|---|---|---|---|---|---|
| Current: separated mixed-Hasse determinant | Pairwise Polynomial.wronskian and unrelated Jacobian results | `"hasseDeriv", "det"`: empty | Pairwise Wronskian/analytic product near-matches | No exact full declaration; project multivariate parent not supplied by pin | Finds project target and scratch replays; not mathlib replacements |
| Standard: det(A·Bᵀ) | Matrix.det_mul and related products | Matrix.det_mul exact outer identity | Matrix.det_mul/det_transpose | Pinned determinant Basic contains both | Source names found, index unavailable |
| Abstract: homomorphisms/determinants | RingHom/AlgHom.map_det | map_det variants | AlgHom.map_det/RingHom.map_det | Pinned map_det signatures/proofs read | Source declarations found, index unavailable |

Pinned positive candidates: `Matrix.det_mul`, `Matrix.det_transpose`, `AlgHom.map_det` in Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean:138,203,326; exact native signatures checked in an isolated mathlib-only document. `Polynomial.wronskian` in Mathlib/RingTheory/Polynomial/Wronskian.lean:43 is binary `a*b'−a'*b`, not the arbitrary-family Hasse determinant. Its n-tuple TODO at29 is a concrete missing-API anchor; sign/normalization cannot be ignored. `Polynomial.hasseDeriv_mul` is univariate, not the mixed-variable entry law.

**Conclusion: partial matches and existing determinant building blocks, no verified exact replacement for the full theorem.** This is not a universal absence assertion. The project `Roth` namespace is guarded absent in isolated probes, while actual-context proofs explicitly retain the missing project Hasse/product infrastructure.

Evidence: [formal-search.json](../evidence/Roth.det_hasseDeriv_separated/formal-search.json), [mathlib-inputs.json](../evidence/Roth.det_hasseDeriv_separated/mathlib-inputs.json), [det-separated-isolated-receipt.json](../evidence/Roth.det_hasseDeriv_separated/det-separated-isolated-receipt.json).

## Phase 5.5 — statement shape

Normal forms compared: (1) named product of embedded Wronskians; (2) raw expanded determinants over CommRing; (3) matrix equality with embedded A·Bᵀ followed by `Matrix.det_mul`. Mathlib has the canonical matrix product/determinant form, but lacks a settled n-tuple Hasse-Wronskian API. Proposed normal form preserves product on the right and uses existing AlgHom transport. Normal form: **REFACTOR** before upstreaming parent API.

Syntactic generality experiments: raw determinants, arbitrary finite index/order family, and injected fresh coordinate were all compiled. The original theorem and its full caller recompile from the expanded ring version. This is evidence, not just a proposed nicer signature. More abstract arbitrary product-preserving operators would require explicit factorization premises; such a theorem would mostly restate the existing matrix API and is not claimed new.

Superfluous-argument audit: τ/K are needed for polynomial types; l selects square size; D/φ/ψ each determine entries. No explicit proposition hypothesis is present. Field is a parent-interface constraint, not a mathematically essential premise for the expanded identity. No ambient Fintype/DecidableEq τ survives elaboration. **RESTATE-BEFORE-SHIP**; no argument is deleted locally.

## Phase 6.0 — complete caller and inline audit

| Source | Kind and role |
|---|---|
| Roth/Separation.lean:33 | Module documentation mention, not a call. |
| Roth/Separation.lean:351 | Declaration head, not a call. |
| Roth/Separation.lean:529 | Sole explicit call, in private exists_rat_factors_det_hasseDeriv_aux; rewrites the rational image determinant into the separated product. |

Internal project use count **1** (same declaring module); external-to-file callers **0**. The full private caller body was read. Its proof first obtains separated independent φ/ψ, chooses nonvanishing generalized Wronskian, applies this identity, and uses characteristic-zero univariate nonvanishing. Three complete caller clones, using the original proof replay, expanded-ring bridge, and strongest fresh-coordinate bridge, compile. No partial terminal-goal test is substituted for caller verification.

Fresh `rg --no-ignore` over Roth/ and Roth.lean, tracked `git grep`, and lexical enumeration of every canonical production module agree on three textual occurrences. Inline scan of det_mul/det_transpose/factorwise/generalized-Wronskian uses found no second independent derivation of this full separation identity. Other determinant bounds and multilinearity arguments concern different statements. The exact293-name ordered kernel-value audit finds one direct consumer, `_private.Roth.Separation.0.Roth.exists_rat_factors_det_hasseDeriv_aux`; it is not advertised as complete transitive or simp dependency closure. The target has no simp attribute.

Evidence: [caller-rg.json](../evidence/Roth.det_hasseDeriv_separated/caller-rg.json), [caller-git-grep.json](../evidence/Roth.det_hasseDeriv_separated/caller-git-grep.json), [lexical-enumeration.json](../evidence/Roth.det_hasseDeriv_separated/lexical-enumeration.json), [rg-inline.json](../evidence/Roth.det_hasseDeriv_separated/rg-inline.json), [canonical-consumers.json](../evidence/Roth.det_hasseDeriv_separated/canonical-consumers.json), [det-separated-caller-receipt.json](../evidence/Roth.det_hasseDeriv_separated/det-separated-caller-receipt.json), [det-separated-bridge-orders-receipt.json](../evidence/Roth.det_hasseDeriv_separated/det-separated-bridge-orders-receipt.json).

## Phase 6 — actual composition experiments

1. **Existing abstract core succeeds.** Isolated mathlib-only `Det169Abstract.generic` proves det(∑k Aik Bjk)=detA·detB by `change` to A·Bᵀ, `Matrix.det_mul`, `Matrix.det_transpose` and congrArg. It compiles for arbitrary finite square index, including Fin0 and the zero ring ZMod1. The first simp-only attempt failed because it did not normalize the matrix under det; its rejected raw receipt includes recovered sorryAx and is excluded from accepted evidence.
2. **Full target direct composition fails as tried.** `exact Matrix.det_mul _ _` does not supply the original mixed-derivative matrix. A closed simp-only attempt using parent unfoldings and `AlgHom.map_det` also fails. Initial extra det_mul/transpose simp arguments were unused and produced warnings; these warning receipts remain rejected, and the clean final diagnostic uses only the arguments actually consumed. This finite test is not proof of exhaustive automation absence.
3. **Full theorem positive proof remains substantive.** The exact original proof replay and full expanded CommRing/arbitraryorders/fresh-coordinate laws compile, but use the project factorwise Hasse law plus sum/matrix-entry reasoning. Those are new supporting proofs, not ≤3 existing mathlib-call replacements. Returning only det_mul without the entry bridge would change the theorem.
4. **Caller transport succeeds.** `simpa only [genWronskian, wronskian, wronskianMatrix] using expandedRing169 D φ ψ` proves the original named conclusion; the complete private caller recompiles through it. The strongest fresh-coordinate/order law also specializes to the exact original named conclusion (`originalViaFresh169`), and `Det169FreshCaller.caller169` recompiles the full sole caller through it. This is a project-helper specialization, not a mathlib-only composition. Under Phase6b, a hypothetical closing simp composition would require an explicit BORDERLINE judgment, not automatic NO.

**No verified ≤3-existing-call full-statement replacement found.** The abstract core is composable; the full mathematical bridge and named API are the assessment's actual scope.

Evidence: [det-separated-isolated-executed.lean.txt](../evidence/Roth.det_hasseDeriv_separated/det-separated-isolated-executed.lean.txt), [det-separated-isolated-receipt.json](../evidence/Roth.det_hasseDeriv_separated/det-separated-isolated-receipt.json), [det-separated-composition-receipt.json](../evidence/Roth.det_hasseDeriv_separated/det-separated-composition-receipt.json), [det-separated-composition-executed.lean.txt](../evidence/Roth.det_hasseDeriv_separated/det-separated-composition-executed.lean.txt), [det-separated-bridge-orders-executed.lean.txt](../evidence/Roth.det_hasseDeriv_separated/det-separated-bridge-orders-executed.lean.txt).

## Phase 7 — actionable verdict

**BORDERLINE-needs-human.** The polynomial identity and stronger ring/index/order/fresh-coordinate formulations are verified; the outer matrix mechanism already exists. What remains is a public API choice: whether to expose this separation determinant law, expose only its matrix factorization, or keep it with Roth's separation machinery after the foundational Hasse/Wronskian API is settled. The sole caller is genuine and needed for the integer separation theorem, so this is not junk. No verified mathlib replacement warrants deletion. The verdict does not cite implementation expense, search failure, or difficulty as a reason.

The command's false-positive class5 applies to claiming a single mechanical weakening of the *named* conclusion: its Field constraints come from three parent definitions across two modules. This does not deny the successful stronger identity. `Roth.genWronskian` and `Roth.hasseDeriv_rename_mul_aeval` were previously accepted YES-but-generalise-first, whereas `Roth.wronskianMatrix` and `Roth.wronskian` were BORDERLINE; those facts are checked against tracked progress, not inferred from their names. Any upstream grouping must preserve that distinction.

Concrete future upstream questions:

1. Should the planned finite-family multivariate Hasse-Wronskian API include the verified fresh-coordinate separation determinant law as a public theorem, with arbitrary finite index and order family E?
2. Should the univariate n-tuple API expose arbitrary selected Hasse orders E alongside the conventional Fin.val Wronskian, or should this factorization stay in raw determinant form?
3. Should the primary reusable addition be the separated derivative **matrix equality**, leaving the determinant law as its local corollary via existing map_det/det_mul/det_transpose?

A positive API decision suggests provisional Mathlib/RingTheory/MvPolynomial/Wronskian.lean, matching the accepted genWronskian proposal after multivariate Hasse prerequisites; no unconditional import placement is asserted. A possible PR title is “feat(MvPolynomial): factor Hasse determinants of separated sums”. Group with accepted genWronskian and the fresh-coordinate factorwise Hasse law only after settling the univariate parents; do not blanket-include their BORDERLINE definitions. Relevant recent determinant commits suggest Yaël Dillies or Rao Xiaojia for initial reviewer fit, subject to current availability. Before a PR, run `/generalise Roth.det_hasseDeriv_separated` against the verified signature, then `/cleanup Roth/Separation.lean Roth.det_hasseDeriv_separated`, and settle the parent API rather than shipping Field-only wrappers by accident.

Until that design is chosen, keep the declaration in **Roth/Separation.lean** with its sole caller unchanged. It expresses the bridge used by Roth's separation lemma and has a clear downstream purpose. There is no immediate deletion/inline refactor recommendation. These questions do not require user input to complete this read-only assessment.

## Phase 8 — completion and verification boundary

All assessment phases are complete. Accepted native receipts have final success, no errors/warnings, no partial disk results, no sorryAx and only standard axioms. Original source/pin hashes, canonical ordered293/unique293/value293 audit, full caller proofs, isolated mathlib core, semantic counterexample,15 actual formal-search cells, all named literature channels, links and current copy manifest are validated. Rejected attempts are retained separately and confer no proof evidence.

[Strongest full caller receipt](../evidence/Roth.det_hasseDeriv_separated/det-separated-fresh-caller-receipt.json). Machine-readable evidence: [assessment.json](../evidence/Roth.det_hasseDeriv_separated/assessment.json), [verification.json](../evidence/Roth.det_hasseDeriv_separated/verification.json), [overview-entry.json](../evidence/Roth.det_hasseDeriv_separated/overview-entry.json), [validate.py](../evidence/Roth.det_hasseDeriv_separated/validate.py), [copy-manifest.json](../evidence/Roth.det_hasseDeriv_separated/copy-manifest.json), [reviewer-commits.json](../evidence/Roth.det_hasseDeriv_separated/reviewer-commits.json), [accepted-yes-grouping.json](../evidence/Roth.det_hasseDeriv_separated/accepted-yes-grouping.json).
