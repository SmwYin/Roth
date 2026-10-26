# Full /mathlibable assessment — `MvPolynomial.hasseDeriv_apply`

**Verdict: NO-composable-from-mathlib.** This is a full, independent assessment of the theorem at `Roth/HasseDeriv.lean:73–75`. Its actual proof `simp [hasseDeriv, sum_def]` is outside the command's narrow rfl/unfold glue-inheritance rule. No parent or future-declaration verdict is inherited.

Date: 2026-10-26; branch `ramin-cleanup`; mathlib pin `5ed2965256430c3649e86755f9576b54eca72435`; Lean v4.34.0. This worker wrote only temporary assessment artifacts. Production code, dependency pins, tracked files and Git were not edited. All assessment gates complete; independent root acceptance pending.

## Phase 0 — Doctor

The shared baseline `lake build` passed, exit0, 2467 jobs. Independently verified **17/17 source/pin hashes** match the shared baseline manifest, permitting reuse. [Baseline receipt](../evidence/MvPolynomial.hasseDeriv_apply/evidence/baseline-build.txt), [manifest](../evidence/MvPolynomial.hasseDeriv_apply/evidence/input-manifest.json), [hash verification](../evidence/MvPolynomial.hasseDeriv_apply/evidence/baseline-hash-verification.json).

The unique target is a public theorem without a simp attribute and without sorry, in the module constructing multivariate Hasse derivatives and their coefficient/composition/compatibility API. [Source/context](../evidence/MvPolynomial.hasseDeriv_apply/evidence/target-source.lean), [corrected canonical inventory entry](../evidence/MvPolynomial.hasseDeriv_apply/evidence/target-inventory.json).

The complete [target native diagnostic receipt](../evidence/MvPolynomial.hasseDeriv_apply/evidence/target-lsp.json) reports `partial=false, success=true, timed_out=false`, zero errors and failed dependencies. [Exact executed source](../evidence/MvPolynomial.hasseDeriv_apply/probes/TargetExecuted.lean). Native `#check` returns:

```lean
@MvPolynomial.hasseDeriv_apply :
  ∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R]
    (d : σ →₀ ℕ) (P : MvPolynomial σ R),
    hasseDeriv d P =
      ∑ k ∈ P.support, monomial (k-d) (↑(hasseCoeff d k) * P.coeff k)
```

The universes are independent. `#print axioms` returns exactly `propext, Classical.choice, Quot.sound`. Independent simp and direct existing-theorem-term proofs do not invoke the assessed theorem. It has no simp attribute to disable; the old monomial simp theorem is disabled in the preserved combined scratch document. The nsmul alternative intentionally uses the target only to verify equivalent statement shape. The Semiring-only `#check_failure` confirms that the existing operator requires CommSemiring; its informational missing-instance diagnostic is expected.

Two warnings in the combined document concern an earlier scratch header and earlier monomial simpa experiment; neither belongs to this target's direct proof. One redundant `change; simpa only [Finsupp.sum]` experiment failed with a type mismatch after simplification. It was replaced by the already-successful direct exact term and rerun cleanly. [Initial receipt](../evidence/MvPolynomial.hasseDeriv_apply/evidence/target-initial-lsp.json), [initial source](../evidence/MvPolynomial.hasseDeriv_apply/probes/TargetInitial.lean). No failed experiment is counted as successful verification.

## Phase 1 — Mathematical content

For a polynomial P over a commutative semiring and a finitely supported natural multiindex d, its d-th Hasse derivative equals the finite sum of the differentiated monomials of P. The term at exponent k has exponent k−d and coefficient (∏ⱼ binom(kⱼ,dⱼ)) times the coefficient of P at k. Natural subtraction is truncated, but a term whose order exceeds its exponent has zero binomial factor.

| Parameter/hypothesis | Mathematical role |
|---|---|
| `σ : Type u` | Arbitrary set of polynomial variables, including empty and infinite types |
| `R : Type v` | Arbitrary coefficient carrier |
| `[CommSemiring R]` | Existing polynomial algebra, linear operator, natural casts and coefficient multiplication |
| `d : σ →₀ ℕ` | Finite-support differentiation order; no positivity or degree restriction |
| `P : MvPolynomial σ R` | Arbitrary polynomial, including zero |

Conclusion in Lean is the support-sum equality printed above. There are no proposition hypotheses, characteristic assumptions, finite-variable assumptions or nonzero assumptions.

## Phase 2 — Preliminary checks

**SMALL:** a support-evaluation helper for the operator, neither a new structure nor one of the module's highlighted main results. The Hasse name on this helper does not make it a separately named main theorem. Literature width remains exhaustive.

**One-line definition check: n/a — theorem.** The body contains one substantive tactic line. Supplementary audit: it introduces neither an instance anchor nor a sealed data definition. Its semantic name is useful for the sole written consumer, but there is no simp attribute or other infrastructure exemption that itself overcomes a positive one-call composition.

## Phase 3 — Exhaustive literature search

[Exact web requests, URL/status receipts](../evidence/MvPolynomial.hasseDeriv_apply/evidence/web-search.json), [follow-up requests and failed fetches](../evidence/MvPolynomial.hasseDeriv_apply/evidence/web-followups.json), [primary-source requests](../evidence/MvPolynomial.hasseDeriv_apply/evidence/web-sources.json), [original source analysis and final categorical/primary queries](../evidence/MvPolynomial.hasseDeriv_apply/evidence/literature-analysis.json). Raw responses were returned in the tool transcript; saved web receipts preserve response digests, URLs and status without copying article text. Search-tool raw responses for the mathlib methods are saved separately below. Batched search output does not prove a hit for each individual query.

| Channel | Actual request | Outcome |
|---|---|---|
| Web specific | `multivariate Hasse derivative sum monomials binomial coefficients expansion polynomial` | Batch located primary expansion; exact source checked subsequently |
| Web general | `Hasse Schmidt derivation Taylor expansion commutative algebra arbitrary ring` | Broader higher-derivation family context; not a replacement for chosen coordinate operator |
| Web aliases | `divided power derivative hyperderivative multivariate polynomial Hasse definition` | Taylor-coefficient/hyperdifferentiation formulations located |
| ChatGPT MCP | Standard form, generality, historical evolution query prepared; enabled tools inspected | n/a: `ask_chatgpt_math` unavailable; [availability receipt](../evidence/MvPolynomial.hasseDeriv_apply/evidence/tool-availability.json) |
| Local references | rg `Hasse/Delta/derivative`, read `clean.tex:119–155` | Explicit binomial monomial formula, linear extension, and any commutative semiring; [excerpt](../evidence/MvPolynomial.hasseDeriv_apply/evidence/local-reference-excerpt.tex) |
| nLab | `site.ncatlab.org nlab higher derivation divided power`; direct Hasse–Schmidt derivative page | Indexed rig-valued multivariate formula/linearity inspected; direct fetch failed unsupported XHTML |
| nCatLab | `site.ncatlab.org Hasse Schmidt derivation`; later `site:ncatlab.org/ncatlab "Hasse" "derivative"` and `"higher derivation"` | Returned higher-derivation and graded-bimonoid context. No coordinate-preserving categorical replacement established |
| Stacks | `site.stacks.math.columbia.edu differential operators divided powers polynomial`; direct tag07H4 | Divided power polynomial algebras inspected; different multiplication and universal property |
| MO | `site.mathoverflow.net Hasse derivatives multivariate polynomial`; later `"Hasse" "derivative" polynomial characteristic`; direct question71423 | Positive-characteristic motivation and aliases, not used as proof authority |
| Recent arXiv | `site.arxiv.org Hasse Schmidt derivations 2021 2022 2023 2024 2025 2026` | Barajas2023 and Miyamoto2025 primary abstracts and HTML introductions inspected |
| Recent primary exact | Open arXiv2205.00342v1 and find Proposition3.5 | 2022-04-30 lies in five-year interval2021-10-26–2026-10-26; exact expansion verified |

**Literature summary.** The concept is the multivariate Hasse/hyperderivative polynomial expansion. Bhargava–Ghosh–Guo–Kumar–Umans §3.2 defines it by a Taylor coefficient and Proposition3.5 expresses it as the coefficient-weighted binomial sum over monomial exponents. This directly matches the target's finite support sum. [Primary paper](https://arxiv.org/html/2205.00342v1). The local source explicitly extends the same binomial recipe to commutative semirings; the expression requires no subtraction of coefficients or factorial inversion.

Literature presentations vary between finite-variable fields, commutative rings, and rig-valued linear extension. Arbitrary σ with finite-support exponents already accommodates finite presentations and needs no Fintype instance. The most general standard form relevant here is this finite algebraic expansion over a commutative semiring. General Hasse–Schmidt derivations on arbitrary algebras are families with a higher Leibniz property; they do not necessarily have the chosen coordinate formula. Recent work examines modules of higher derivations and lifting/deformation problems, not a forced weakening of this support-evaluation equality. [Barajas2023](https://arxiv.org/html/2305.04537v1), [Miyamoto2025](https://arxiv.org/html/2509.00887v2). The categorical and divided-power-algebra variants were considered as related objects, not interchangeable statement forms. [Stacks07H4](https://stacks.math.columbia.edu/tag/07H4).

## Phase 4a–b — Generality

| Parameter/hypothesis | Current vs standard | Verified weaker opportunity | Reason |
|---|---|---|---|
| σ | Arbitrary vs usually finitely many variables | None | Already includes empty/infinite σ; each polynomial and d has finite support |
| R | Arbitrary coefficient carrier | None | No field, domain, characteristic or nontriviality assumption |
| CommSemiring R | Rig level already represented by current operator | None | Semiring-only probe cannot form existing operator; missing CommSemiring explicitly reported |
| d | Any finitely supported natural multiindex | None | No bound, positivity or d≤k hypothesis |
| P | Any polynomial | None | Zero and arbitrary degree included; support makes sum finite |

**MAXIMALLY GENERAL for the current polynomial/operator representation; zero verified hypothesis weakenings.** Changing exponent domain or coefficient foundations would change underlying infrastructure, not drop a superfluous theorem binder. No strictly-narrower claim is made. The abstract linear-extension generality identified next already exists in mathlib.

## Phase 4c — Modern-idiom check, all nine rows

| # | Question | Answer and proposal | Concrete downstream consequence |
|---|---|---|---|
| 1 | Preambles to typeclasses? | No: CommSemiring already a typeclass | Existing polynomial/module API applies |
| 2 | Sequences/metrics to filters? | No: finite algebraic sum equality | No convergence data |
| 3 | Construction to universal property? | Theorem constructs no new object; underlying linear extension has universal sum API | `Finsupp.lsum_apply` evaluates arbitrary component-map families |
| 4 | Set predicates to bundled substructures? | No closure predicates; operator already LinearMap | Existing map/coercion structure retained |
| 5 | Field/vector assumptions to module/semiring? | Already semiring level; no field assumptions | Positive characteristic and ℕ coefficients supported |
| 6 | Higher categorical generalisation? | None preserving this coordinate computation found after actual categorical queries | Graded-bimonoid family is context, no better rewrite for sole normOne consumer |
| 7 | Concrete index to arbitrary monoid/group? | Natural polynomial exponents/binomial choices essential | Laurent/general monoid analogues need different operators and coefficient API |
| 8 | Concrete-via-abstract proof diagnostic? | **Yes.** Body is `simp [hasseDeriv, sum_def]`: one line mentioning named operator; zero after unfolding. Arbitrary-family evaluation is the abstract content | Existing `Finsupp.lsum_apply R b l` already evaluates any linear extension; applies beyond Hasse derivatives |
| 9 | False-generalisation guard? | Generic b is sound as an evaluation theorem, not a Hasse operator. Reject calling arbitrary b the same derivative or replacing ordinary polynomials by divided-power polynomials | Preserves actual coordinate/binomial semantics while reusing existing generic calculation |

**Modern-idiom verdict:** existing abstract idiom available, no new modernisation theorem needed. The Q8 diagnostic leads to the positive generic composition, not an unsupported YES-generalise-first verdict. Natural coefficient casts versus nsmul are equivalent syntax, addressed below.

## Phase 4.5 — Infrastructure risk

**n/a — declaration kind is theorem.** The command explicitly skips the six diamond/defeq rows for proposition proofs: this theorem adds no data definition, typeclass, instance priority or coercion. It also adds no simp rule. This is not inheritance from the parent definition's risk assessment.

## Phase 4.6 — Proof strategy

| # | Idiom question | Applies? / alternative | Cost |
|---|---|---|---|
| 1 | ε–δ to filters | No topology | n/a |
| 2 | Element algebra to ideal/submodule inclusions | No inclusion argument; equality computes an extension | n/a |
| 3 | Sequences to nets | No analysis | n/a |
| 4 | Explicit construction to universal property | Already the finite-support linear extension; direct `lsum_apply` identifies it | CHEAP |
| 5 | Missing helper mathlib should have | No: `Finsupp.lsum_apply` and `MvPolynomial.sum_def` already provide required evaluation/support interface | No helper contribution |

**MATHLIB-IDIOMATIC.** Unfolding and simp is a reasonable local proof. The verified direct theorem term makes the dependency explicit and shorter without adding helper API. No hidden missing lemma is being worked around.

## Phase 5 — Five actual mathlib searches

[Lean-Finder requests/raw results](../evidence/MvPolynomial.hasseDeriv_apply/evidence/search-finder.json), [Loogle](../evidence/MvPolynomial.hasseDeriv_apply/evidence/search-loogle.json), [LeanSearch](../evidence/MvPolynomial.hasseDeriv_apply/evidence/search-leansearch.json), [local name search](../evidence/MvPolynomial.hasseDeriv_apply/evidence/search-local.json), [untruncated grep receipts](../evidence/MvPolynomial.hasseDeriv_apply/evidence/grep-receipts.json).

| Method/form | Actual query | Results and interpretation |
|---|---|---|
| A current | multivariate Hasse derivative expansion as finite sum of monomials over polynomial support | `Polynomial.hasseDeriv_apply` is univariate analogue |
| A literature | Hasse Schmidt higher derivation polynomial coefficient Taylor expansion over commutative ring | Univariate Taylor/Hasse API; abstract derivation context |
| A abstract | Finsupp linear sum apply equals sum over support of coefficient linear maps | `Finsupp.lsum_apply`, `coe_lsum`, linearCombination API |
| B current | `"hasseDeriv_apply"` | Exact univariate name and apply-one result |
| B literature | `Polynomial.hasseDeriv, _ = _` | Univariate family, not arbitrary multiindex operator |
| B abstract | `Finsupp.lsum, _ = _` | `lsum_apply`, `coe_lsum`, single and composition laws |
| C current | multivariate Hasse derivative polynomial sum support monomial binomial coefficient | Univariate analogue; `MvPolynomial.sum_def`, support expansion |
| C literature | Hasse Schmidt derivative Taylor expansion polynomial arbitrary commutative ring | Polynomial Taylor/Hasse API |
| C abstract | Finsupp lsum applied to finitely supported function equals sum of linear maps | `lsum_apply`, DFinsupp and related maps |
| D all forms | `hasseDeriv/Hasse.Schmidt/hyperderiv/divided.deriv` whole mathlib; exact qualified target; `lsum_apply/coe_lsum/sum_def` candidate files | No exact textual target; positive generic and univariate candidates; all outputs preserved without head/truncation |
| E current | `hasseDeriv_apply` | Project target plus evidence copies and univariate mathlib name; copies not counted |
| E literature | `hasseDeriv` | Polynomial/Laurent/project context |
| E abstract | `lsum_apply` | Pinned `Finsupp.lsum_apply` and different `LinearMap.lsum_apply` |

Local tool reports **index unavailable**, using textual fallback. Empty or incomplete symbol results are never used as proof of absence. External indexes are discovery only; candidates were read at the actual pin and verified by Lean. The positive generic route settles composability without an absence inference.

| Candidate | Pinned source | Assessment |
|---|---|---|
| `Finsupp.lsum_apply` | `Mathlib/LinearAlgebra/Finsupp/LSum.lean:120` | Generic extension evaluation, precise positive route |
| `Finsupp.coe_lsum` | same file:117 | Function-coercion version; simp uses this underlying interface |
| `MvPolynomial.sum_def` | `Mathlib/Algebra/MvPolynomial/Basic.lean:519` | Finsupp sum to polynomial support/coeff expression |
| `Polynomial.hasseDeriv_apply` | `Mathlib/Algebra/Polynomial/HasseDeriv.lean:62` | Univariate exponents ℕ; not direct substitute for arbitrary σ→₀ℕ |
| `AddMonoidAlgebra.coeffLinearEquiv` | `Mathlib/Algebra/MonoidAlgebra/Module.lean:75` | Existing coefficient-storage transport |

[Candidate source hashes and exact excerpt boundaries](../evidence/MvPolynomial.hasseDeriv_apply/evidence/candidate-source-hashes.json), [generic source](../evidence/MvPolynomial.hasseDeriv_apply/evidence/lsum-source.lean), [support source](../evidence/MvPolynomial.hasseDeriv_apply/evidence/sum-def-source.lean), [univariate source](../evidence/MvPolynomial.hasseDeriv_apply/evidence/polynomial-source.lean). These source excerpts and positive elaborator checks establish applicability; no live-web API version is substituted for the pin.

**Search conclusion:** found building blocks `Finsupp.lsum_apply` and coefficient transport; direct evaluation yields the target. The exact qualified multivariate theorem is not resolved in the isolated mathlib-only import environment, but the abstract formula is already there.

## Phase 5.5 — Statement shape

Equivalent forms considered: (1) current finite support double-binder sum with cast-times-coefficient; (2) the same sum with natural scalar action `hasseCoeff d k • P.coeff k`; (3) `Finsupp.sum` of the component map; (4) evaluation of `Finsupp.lsum`. Current RHS is the explicit polynomial computational normal form. `MvPolynomial.sum_def` is the pinned canonical bridge from storage sums to support/coeff sums. The univariate `hasseDeriv_apply` uses the analogous cast-times-coefficient monomial expansion. RHS removes the derivative and respects the normal-form orientation.

**Syntactic generality attempts:** the nsmul alternative compiled in the target batch. The fully abstract lsum formula compiled separately; direct generic exact term also supplies the original shape. The sole caller immediately applies `normOne_sum_le` and `Finset.sum_le_sum`; explicit support sum is easier to use there than reintroducing a bundled or Finsupp expression. Keep this shape if retaining local API.

| Argument/typeclass | Essentially used? | Reason |
|---|---|---|
| σ | Yes | Domain of multiindices/variables |
| R | Yes | Coefficients and module operations |
| CommSemiring R | Yes for existing statement | Operator and polynomial type require it; floor probe confirmed |
| d | Yes | Operator order and each shifted/binomial term |
| P | Yes | Input, support and coefficients |

Normal form **OK**; syntactic generality **OK**; superfluous arguments **NONE**; overall **SHIP-AS-STATED** as a local interface. This shape finding does not override standalone composition.

## Phase 6.0 — Complete written caller audit

[Caller table and counts](../evidence/MvPolynomial.hasseDeriv_apply/evidence/call-sites.json), [actual caller source](../evidence/MvPolynomial.hasseDeriv_apply/evidence/caller-source.lean), [grep receipts](../evidence/MvPolynomial.hasseDeriv_apply/evidence/grep-receipts.json).

Internal use count outside declaring file: **1 occurrence / 1 code line / 1 caller declaration / 1 file**. Same-file callers: **0**. These counts concern explicit written references in the14 canonical production modules; copied evidence, scratch, mathlib, declaration heads and comments excluded. No use in another library is established.

| Caller file:line | Qualified caller | Usage/resolution |
|---|---|---|
| `Roth/CoeffNorm.lean:151` | `Roth.normOne_hasseDeriv_le` (declaration148) | `rw [hasseDeriv_apply]`; MvPolynomial opened, d/P inferred from normOne derivative goal, coefficients specialized to ℤ |

Inline-derivation grep over all canonical sources used `hasseDeriv.*support|sum_def|Finsupp.lsum`, then read the related support/derivative sites. No second full derivative-support expansion rederived inline was found. The definition's own lsum recipe and separate monomial/coefficient laws are different statements. This finite written-source search does not claim an exhaustive hidden kernel/tactic dependency closure.

**Signal:** a useful one-caller computational bridge, a plausible inlining candidate. It is not dead code.

## Phase 6 — Positive composition check

The direct exact term below was accepted for the **original target** without tactics, rewriting, target invocation or new axioms:

```lean
example (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P =
      ∑ k ∈ P.support, monomial (k-d) ((hasseCoeff d k : R) * P.coeff k) :=
  Finsupp.lsum_apply R (fun k : σ →₀ ℕ =>
    (monomial (k-d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R)))
      ((AddMonoidAlgebra.coeffLinearEquiv R) P)
```

This applies exactly one existing mathematical evaluation theorem. Storage transport and application of the component linear map reduce definitionally. The binomial factor is untouched input: no identity involving choose, differentiation or coefficient bounds must be proved. `MvPolynomial.sum_def` supplies a named support interface for unfolding-based proofs; it is not even needed as a separate call by the accepted direct term.

The isolated mathlib-only source imports only `Mathlib.Algebra.MvPolynomial.PDeriv` and `Mathlib.Algebra.Polynomial.HasseDeriv`, never Roth. It first checks the abstract formula with arbitrary family b and P, then demonstrates the same formula for an explicitly **new local witness** built from the defining binomial component maps. The witness is not represented as an existing mathlib derivative. [Requested isolated source](../evidence/MvPolynomial.hasseDeriv_apply/probes/mathlib-only.lean), [actual executed isolated source](../evidence/MvPolynomial.hasseDeriv_apply/probes/MathlibOnlyExecuted.lean), [complete native receipt](../evidence/MvPolynomial.hasseDeriv_apply/evidence/mathlib-only-lsp.json). The request source includes an exploratory simpa variant; the executed version uses the successful direct exact term instead. Only the executed successful receipt is counted. The final isolated receipt reports partial=false, success=true, timed_out=false, zero errors and failed dependencies; both the arbitrary-b formula and direct exact witness term passed. Two unnecessarySimpa warnings belong to earlier preserved monomial experiments. An initial combined isolated batch duplicated an already-active universe declaration; root removed that redundant scratch declaration, then reran successfully. [Initial isolated source](../evidence/MvPolynomial.hasseDeriv_apply/probes/MathlibOnlyInitial.lean), [initial isolated receipt](../evidence/MvPolynomial.hasseDeriv_apply/evidence/mathlib-only-initial-lsp.json). This was a scratch batching error, not a changed mathematical claim.

The univariate Hasse theorem is a genuine analogue, not the replacement: arbitrary variable types and multiindices cannot be instantiated by a single natural order. Iterated ordinary partial derivatives would require factorial division to reverse the scaling and fail in general positive characteristic. The actual replacement is the generic finite-support extension evaluation, not one of those partial matches.

**Conclusion: COMPOSABLE.** One existing theorem application after definitional transport, independently checked in the target and isolated environments. It does not assert that mathlib already contains the multivariate coordinate operator.

## Phase 7 — Verdict and actionable next step

**NO-composable-from-mathlib**, assessed independently. All required phases support this: standard characteristic-free expansion found; no verified narrowing; concrete-via-abstract diagnostic finds already-existing generic evaluation; theorem risk phase legitimately n/a; strategy and statement shape accepted; all five searches actually run on current/literature/abstract forms; complete one-caller audit; original target closed by the direct generic theorem term.

**Why not a standalone addition:** `Finsupp.lsum_apply` already computes any linear extension on a finitely supported coefficient vector. Substituting the component maps used in `hasseDeriv` produces the entire support expansion by definitional reduction. There is no residual derivative/binomial mathematics needing a separate theorem. The NO-composable bucket records this construction/evaluation route without claiming an already-named multivariate Hasse operator. Cost is not a verdict factor.

**Belongs elsewhere:** retaining the semantic expansion law in project-local `Roth/HasseDeriv.lean` is sensible while the operator package remains downstream. It has a real consumer and is not junk. A future upstream operator package may deliberately retain a stable evaluation API mirroring the univariate one; that package-design review is distinct from this standalone wrapper assessment. No verdict is issued about any unassessed declaration.

**Refactor plan for every current caller, if wrapper removal is later authorized:** at the sole explicit call `Roth/CoeffNorm.lean:151` inside `Roth.normOne_hasseDeriv_le`, replace `rw [hasseDeriv_apply]` by rewriting with the displayed generic equality at R=ℤ, using the existing d and P. Concretely:

```lean
rw [show hasseDeriv d P = ∑ k ∈ P.support,
  monomial (k-d) ((hasseCoeff d k : ℤ) * P.coeff k) from
  Finsupp.lsum_apply ℤ (fun k : σ →₀ ℕ =>
    (monomial (k-d)).comp (LinearMap.lsmul ℤ ℤ (hasseCoeff d k : ℤ)))
      ((AddMonoidAlgebra.coeffLinearEquiv ℤ) P)]
```

The polymorphic equality itself is verified by the exact target term; this assessment has not edited or recompiled an all-callers refactor. Then remove the theorem at73–75 and rebuild the affected modules/project. No parent docstring names this theorem, and no simp registration is removed. Before deletion, a future cleanup should still check implicit consumers; explicit grep counts do not prove their absence.

**Next action:** record the standalone NO-composable verdict and retain current production code during this read-only overview. In a later authorized cleanup, inline the accepted generic equality at the1 explicit caller, remove the wrapper and rebuild. Do not open a standalone theorem PR; consider its semantic interface only with the full parent operator package.

## Phase 8 — Completion

Assessment artifacts include baseline hash reuse, actual type and standard axioms, prose statement, SMALL/theorem-kind one-line n/a, exhaustive literature with unavailable optional ChatGPT and fetch limitations, all parameters' generality audit and actual Semiring-floor check, all9 modern-idiom rows including Q8/Q9, justified Phase4.5 n/a, all5 strategy rows, all5 actual mathlib search methods on three forms, normal-form/syntactic/superfluous-argument checks, qualified caller counts/table, independent positive exact composition and actionable refactor.

No error or sorry is admitted; failed exploratory simplification is retained and superseded by successful exact verification. Search-index unavailability is never converted into absence. [Assessment metadata](../evidence/MvPolynomial.hasseDeriv_apply/assessment.json), [target-only overview entry](../evidence/MvPolynomial.hasseDeriv_apply/overview-entry.json), [report-link validation](../evidence/MvPolynomial.hasseDeriv_apply/evidence/report-links.json), [portable validator](../evidence/MvPolynomial.hasseDeriv_apply/validate-artifacts.py), [hashed copy manifest](../evidence/MvPolynomial.hasseDeriv_apply/copy-manifest.json). Integration, independent root acceptance, commit and push remain exclusively root-owned.

