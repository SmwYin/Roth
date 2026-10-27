# Roth.degreeOf_none_rename_mul_aeval

Verdict: **BORDERLINE-needs-human**. The canonical constant-multiplication degree law is already in mathlib. The unresolved upstream design choice is whether the separated-variable spelling deserves API beyond the missing normalization bridge. All verification is complete; the design questions do not block this read-only assessment.

## Phase 0 — Doctor

The theorem resolves at `Roth/Separation.lean:213`, canonical declaration164. The original project build is clean (2467jobs); all17 source/pin hashes were freshly recomputed and match the baseline manifest. No production file or Git state was modified. Module read in full: separation of one polynomial variable, Wronskian determinants, rational-to-integral rescaling and Lemma2. Evidence: [baseline-build.txt](../evidence/Roth.degreeOf_none_rename_mul_aeval/baseline-build.txt), [inputs.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/inputs.json), [Roth-Separation.lean.txt](../evidence/Roth.degreeOf_none_rename_mul_aeval/Roth-Separation.lean.txt).

## Phase 1 — Comprehend

For a nonzero polynomial U in the remaining variables and any univariate polynomial V, the product U(x_τ)V(x_none) has degree in x_none equal to the natural degree of V. This includes V=0 because both natural degrees are0. The coefficient ring is a commutative domain; τ is arbitrary and may be empty or infinite.

Full native type:

```lean
@Roth.degreeOf_none_rename_mul_aeval : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommRing R] [IsDomain R]
  {U : MvPolynomial τ R},
  U ≠ 0 →
    ∀ (V : Polynomial R),
      MvPolynomial.degreeOf none ((MvPolynomial.rename some) U * (Polynomial.aeval (MvPolynomial.X none)) V) =
        V.natDegree
```

The source handles V=0 separately, applies multivariate degree-of-product to the two nonzero embedded factors, eliminates the distinguished-variable degree of U, then identifies the degree of embedded V through the singleton-variable equivalence. Original project dependencies are `Roth.aeval_X_eq_rename` and `Roth.degreeOf_uniqueAlgEquiv_symm`. Complete kernel body printed without elision, standard axioms only: [none-degree-original-audit-receipt.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/none-degree-original-audit-receipt.json).

## Phase 2 — Preliminary checks

SMALL: this is a polynomial helper, neither a new structure nor a named main result. One-line-definition test and its three exemptions are n/a because this is a theorem. This classification did not reduce literature width.

## Phase 3 — Exhaustive literature

Each actual request, returned-response SHA256/byte length/status, source titles/URLs and original summary is preserved in [literature-individual.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/literature-individual.json); no full web bodies are archived. Actual primary access metadata is in [literature-primary-access.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/literature-primary-access.json).

| Channel | Actual query / outcome |
|---|---|
| General specific | degree in one variable separated product U other variables V polynomial integral domain; university algebra notes supply leading-term proof and regrouping of variables. |
| General standard | polynomial degree multiplication nonzero constant leading coefficient integral domain; ordinary degree-of-product law. |
| General abstract | multivariate polynomial ring as univariate polynomial ring coefficient ring partial degree; grouping variables and coefficient rings. |
| ChatGPT math | n/a: ask_chatgpt_math unavailable in enabled tools, including historical-formulation inquiry. |
| Local references | clean.tex checked; §2 Lemma2, especially line435, explicitly identifies individual degrees of disjoint nonzero factors with those of F. [local-literature-search.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/local-literature-search.json), [clean-excerpt.tex.txt](../evidence/Roth.degreeOf_none_rename_mul_aeval/clean-excerpt.tex.txt). |
| nLab | site:ncatlab.org/nlab polynomial ring degree integral domain; polynomial/degree/domain entries. Direct degree-page fetch failed: unsupported XHTML content type. |
| nCatLab | site:ncatlab.org/ncatlab polynomial ring multivariate degree; returned /nlab pages and files, no exact namespace hit. |
| Stacks | site:stacks.math.columbia.edu polynomial ring domain degree leading coefficient; factorization context §10.120, no exact Option-variable theorem. |
| MathOverflow | site:mathoverflow.net polynomial partial degree product disjoint variables; related interpolation/composition discussion, no exact result identified. |
| Recent arXiv | site:arxiv.org/abs/ multivariate polynomial individual degree product after:2021-10-27 before:2026-10-28; includes Wang et al.2024 and Chuyoon–Shpilka2026. |

The standard mathematical content is invariance of degree under multiplication by a nonzero constant, after treating the other variables as coefficients. Altman–Kleiman, *A Term of Commutative Algebra* (2013), chapter2, supports the leading-term law over domains ([primary source](https://web.mit.edu/18.705/www/13Ed-2up.pdf)). [Stacks §10.120](https://stacks.math.columbia.edu/tag/034O) supplies domain/factorization context. [Wang et al.2024](https://arxiv.org/abs/2403.12716) concerns representation reductions rather than this exact identity. These sources agree on the algebraic content; this assessment uses Lean's natDegree zero convention. Search silence is not proof of absence.

## Phase 4a — Every parameter and hypothesis

| Parameter | Assessment |
|---|---|
| R : Type u_2 | Arbitrary coefficient type; independent universe retained. |
| CommRing R | Additive inverses unused; CommSemiring verified. |
| IsDomain R | Global no-zero-divisor condition sufficient; Nontrivial unnecessary, so NoZeroDivisors verified. |
| τ : Type u_1 | Arbitrary remaining-variable type; no finiteness, enumeration or decidable equality hypothesis in native type or verified weakening. |
| U : MvPolynomial τ R | Arbitrary coefficient polynomial. U=0 cannot be allowed uniformly: V=X yields0=1. |
| hU : U≠0 | Needed under the global domain formulation; point-local nonannihilation can replace it when zero divisors are allowed. |
| V : Polynomial R | Arbitrary, with V=0 explicitly allowed; no hV should be added. |

## Phase 4b — Verified generality

STRICTLY NARROWER: the same conclusion compiles over `[CommSemiring R] [NoZeroDivisors R]`. Exact accepted source and receipt: [none-degree-isolated-executed.lean.txt](../evidence/Roth.degreeOf_none_rename_mul_aeval/none-degree-isolated-executed.lean.txt), [none-degree-isolated-receipt.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/none-degree-isolated-receipt.json). This is an actual weakening, not a hierarchy guess. U=0,V=X overℤ is a compiled counterexample to dropping hU. Overℤ×ℤ, U=C(1,0) and V=C(0,1)X are nonzero but their separated product vanishes while natDegree V=1; removing the no-zero-divisor condition with only hU is false. The V=0 supplemental theorem works for every U.

The point-local variant replaces global NoZeroDivisors by `V=0 ∨ U * (V.map C).leadingCoeff≠0` over an arbitrary commutative semiring. Its proof uses `Polynomial.natDegree_C_mul_of_mul_ne_zero`; it exposes precisely the leading-coefficient nonannihilation underlying the formula. This gives a broader coefficient setting through a verified sufficient point-local premise; no weakest necessary condition is claimed, and the canonical law already exists. [none-degree-composition-executed.lean.txt](../evidence/Roth.degreeOf_none_rename_mul_aeval/none-degree-composition-executed.lean.txt), [none-degree-composition-receipt.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/none-degree-composition-receipt.json).

## Phase 4c — Nine modern-idiom checks

| # | Question | Answer and concrete consequence |
|---|---|---|
|1| Typeclasses | Already typeclass-based; use NoZeroDivisors instead of full IsDomain. |
|2| Filters/topology | No; finite polynomial identity with no topology. |
|3| Universal property | Yes representation-level: optionEquivLeft is the existing algebra equivalence; its homomorphism extensionality normalizes rename some to Polynomial.C. This enables direct use of polynomial degree API. |
|4| Bundled substructures | No closure predicates to replace. Existing polynomial types and algebra homomorphisms are bundled. |
|5| Hierarchy | Yes; CommSemiring+NoZeroDivisors verified and point-local condition verified. Enables semiring coefficients and zero-divisor rings satisfying the local condition. |
|6| Higher categories | No categorical structure in the statement; no concrete downstream improvement from categorification. |
|7| Generalize indices | τ already arbitrary. Natural exponents are ordinary-polynomial data; generalized monoid exponents would change the object. |
|8| Concrete-via-abstract | No special named witness such as a fixed polynomial appears: U,V are universally quantified. The representation diagnostic nevertheless applies: after normalization only constant multiplication and injective coefficient-map degree remain. Those abstract laws already exist, so this is a bridge choice, not a missing abstract degree theorem. |
|9| False-generalization guard | Same polynomial content retained under the equivalence and class weakening; do not remove hU or all nonannihilation assumptions, as the two compiled counterexamples demonstrate. Do not replace ordinary polynomials by arbitrary monoid algebras while keeping natDegree. |

Modern idiom available: use `optionEquivLeft` and canonical univariate degree law. The actual new hom-ext normalization is explicitly accounted for, not hidden in a claim that two existing calls prove the old statement.

## Phase 4.5 — Infrastructure risk

n/a: theorem, not a definition/class/instance. Typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priorities, universe-polymorphism infrastructure and coercion ambiguity introduce no new definitional or instance path here. The independent universes are recorded in the full native type.

## Phase 4.6 — Five proof-strategy checks

|#|Question|Assessment|
|---|---|---|
|1| εδ vs filters | n/a, no topology. |
|2| Element chasing vs algebra abstraction | Prefer existing optionEquivLeft algebra equivalence and hom-ext on variables to coefficient support bounds. |
|3| Sequences vs nets | n/a, no analysis. |
|4| Explicit construction vs universal property | Normalize composition of algebra homomorphisms with algHom_ext; do not rebuild the polynomial equivalence. |
|5| Missing helpful API | A general optionEquivLeft/rename-some normalization theorem would shorten this and coefficient calculations. The core degree law is present. |

REFACTOR-RECOMMENDED: use the verified canonical-degree route and weaken the hypotheses; no new degree theory is needed. The open question concerns the public bridge/wrapper API. Cost does not determine the verdict.

## Phase 5 — All15 formal search cells

Actual complete returned receipts: [formal-search.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/formal-search.json).

| Form | Finder | Loogle | LeanSearch | rg | local |
|---|---|---|---|---|---|
| Current | degreeOf none separated product | degreeOf,natDegree | distinguished variable degree | [rg-current.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/rg-current.json) | degreeOf_none |
| Literature standard | natDegree nonzero constant product | natDegree(C _ * _)=_ | nonzero constant preserves natural degree | [rg-literature.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/rg-literature.json) | natDegree_C_mul |
| Abstract | optionEquivLeft natDegree degreeOf | optionEquivLeft,natDegree | natDegree equivalence and injective map | [rg-modern.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/rg-modern.json) | natDegree_optionEquivLeft |

All12 external formal calls returned non-error responses. Local index reports unavailable where present; positive textual candidates are still recorded. External index revisions are not assumed equal to the pin. Pinned candidate signatures and actual uses were checked natively.

Key positive pinned candidates:

* `MvPolynomial.natDegree_optionEquivLeft`, `Mathlib/Algebra/MvPolynomial/Equiv.lean:578`: outer natDegree equals degreeOf none, for all commutative semirings.
* `Polynomial.natDegree_C_mul`, `Mathlib/Algebra/Polynomial/Degree/Lemmas.lean:376`: multiplication by nonzero constant preserves natDegree under NoZeroDivisors.
* `Polynomial.natDegree_C_mul_of_mul_ne_zero`, same file:133: point-local leading-coefficient nonannihilation suffices.
* `Polynomial.natDegree_map_eq_of_injective`, same file:293: coefficient-map injection preserves natDegree.
* `MvPolynomial.degreeOf_mul_eq`, `Mathlib/Algebra/MvPolynomial/NoZeroDivisors.lean:43`: source proof route, not an exact old-form hit.

Conclusion: canonical degree law exists; current separated-variable statement needs normalization. No direct old-form existing theorem was verified. Positive source excerpts and hashes: [source-links.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/source-links.json), [mathlib-inputs.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/mathlib-inputs.json).

## Phase 5.5 — All three statement-shape checks

Normal form: `natDegree (C U * V.map C)=natDegree V` is the canonical univariate form after transporting through optionEquivLeft. The existing equality `natDegree_optionEquivLeft` links the outer degree to degreeOf none. The original RHS `V.natDegree` is an appropriate normal form.

Syntactic generality: compared source spelling, canonical C-multiplication form, semiring weakening and point-local leading-coefficient form in actual Lean experiments. Original spelling is easy to rewrite at the sole determinant caller; canonical form immediately composes with existing Polynomial API but requires the actual hom-ext bridge. A helper should choose one normal form instead of multiplying pairwise equivalent formulas.

Superfluous-argument audit: τ,R,U,V are substantive; hU cannot be removed uniformly. CommRing and IsDomain are stronger than needed. Fintype/DecidableEq are already omitted and must stay omitted. No hV is required. RESTATE-BEFORE-SHIP: at least weaken to CommSemiring+NoZeroDivisors; decide bridge versus derived-wrapper API first.

## Phase 6.0 — Complete callers and inline audit

| Caller | Usage |
|---|---|
| `Roth/Separation.lean:557`, `Roth.exists_det_eq_mul` | `rw [← degreeOf_none_rename_mul_aeval hU V, ← hFUV]` transfers the determinant's none-variable bound to V.natDegree. |

One explicit use, zero outside the declaring file. Source occurrence count2 includes the declaration. Fresh lexical enumeration of every canonical production module agrees with `rg --no-ignore` and `git grep`: [lexical-enumeration.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/lexical-enumeration.json), [caller-rg.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/caller-rg.json), [caller-git-grep.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/caller-git-grep.json). Direct kernel-value consumer audit over exactly293 distinct canonical names also finds only Roth.exists_det_eq_mul. This is separate from opaque/simp/transitive dependency closure.

Inline audit: [rg-inline.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/rg-inline.json); no equivalent independent rederivation found in project production sources. Nearby163 measures a different variable and is not a duplicate. Complete caller was re-proved with164 absent from the appended region, all original Finite hypotheses and other proof branches retained. Its163 invocation is legitimate and untouched. The inline replacement uses the full non-definitional bridge and canonical degree proof, so deletion is feasible but not a ≤3-existing-call substitution. [none-degree-callers-executed.lean.txt](../evidence/Roth.degreeOf_none_rename_mul_aeval/none-degree-callers-executed.lean.txt), [none-degree-callers-receipt.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/none-degree-callers-receipt.json).

## Phase 6 — Actual composition experiments

The canonical C-multiplication statement is exactly two chained existing calls:

```lean
(Polynomial.natDegree_C_mul hU).trans
  (Polynomial.natDegree_map_eq_of_injective (MvPolynomial.C_injective _ _) V)
```

The old separated form does not follow from that term by unification or `simpa only [natDegree_optionEquivLeft]`; both guarded attempts actually fail in a successful proof. Supplying an explicit normalization premise then closes using the canonical law. The accepted old-form theorem instead constructs the homomorphism equality `(optionEquivLeft R τ).toAlgHom.comp (rename some)=Polynomial.CAlgHom` by algHom_ext and simp on generators, then rewrites the aeval factor to a mapped polynomial. That is a new proof, not an existing call or definitional equality. [none-degree-composition-executed.lean.txt](../evidence/Roth.degreeOf_none_rename_mul_aeval/none-degree-composition-executed.lean.txt), [none-degree-composition-receipt.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/none-degree-composition-receipt.json).

NOT-COMPOSABLE in the strict ≤3-existing-call old-form sense. Canonical core COMPOSABLE. No timeout/search failure is used as absence evidence. A future normalization bridge could shorten the wrapper. The present BORDERLINE verdict records the concrete upstream bridge/wrapper API choice; it does not claim that an unexecuted future simp lemma closes the current goal.

## Phase 7 — Verdict and actionable choices

**BORDERLINE-needs-human**, independently reached from the evidence. The mathematical degree law is elementary, standard and already represented in mathlib; the explicit old-form normalization is a genuine bridge proof, and this source has one full caller. This leaves a concrete upstream API choice rather than a missing theorem about degree. CommSemiring+NoZeroDivisors weakening is verified, but does not by itself justify YES-generalise when the canonical core already exists. Neither NO-has nor NO-composable is claimed without a verified exact or ≤3-call old-form term.

Re-aim gate: this is not a glue law for a project parent replaced by an existing more-general definition. Its original statement and proof do not use coeffNone. The original proof dependencies159 and162 are theorem/bridge choices, not a parent definition whose analogous law forces inheritance. The canonical Polynomial law is still independently checked and fully credited above.

1. Should mathlib add a general `optionEquivLeft` normalization theorem for `rename some`, preferably its AlgHom composition form, so coefficient and degree users share one bridge?
2. After that bridge is present, should mathlib also expose this distinguished-variable separated-product degree wrapper, or should downstream users normalize and apply `Polynomial.natDegree_C_mul` directly?
3. If a wrapper is accepted, should its public hypothesis use global `NoZeroDivisors` plus U≠0, or expose the verified point-local leading-coefficient nonannihilation variant as primary API?

These are future upstream API questions, not a request to pause this overview. Candidate bridge home is `Mathlib/Algebra/MvPolynomial/Equiv.lean`; a domain wrapper may need a leaf file to avoid strengthening foundational imports. If kept local, `Roth/Separation.lean` is the natural destination alongside the factorization caller. No Archive destination is needed. Keep164 provisionally, weaken/refactor through the verified route in a separately authorized cleanup, and discuss bridge grain before proposing a PR. The full sole-caller inline experiment is ready if deletion is chosen. No production changes were made.

## Phase 8 — Package and verification

Exact original audit, semiring weakening, two faithful false-generalization guards, Vzero example, canonical composition/normalization diagnostics, point-local theorem and complete sole caller all have clean native receipts with standard axioms only. Exact293 canonical order is checked statically and at runtime. Native disk info assertions are scoped to this target's new region; complete disk diagnostics are checked for errors/warnings/sorryAx. Raw run-code diagnostics use their documented shape. One rejected point-local execution is preserved separately: rw failed on the algebraMap/C representation mismatch and recovered sorryAx. The final proof explicitly normalizes algebraMap_eq and passes; rejected evidence is not accepted proof evidence. [verification.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/verification.json), [assessment.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/assessment.json), [validate.py](../evidence/Roth.degreeOf_none_rename_mul_aeval/validate.py), [copy-manifest.json](../evidence/Roth.degreeOf_none_rename_mul_aeval/copy-manifest.json).
