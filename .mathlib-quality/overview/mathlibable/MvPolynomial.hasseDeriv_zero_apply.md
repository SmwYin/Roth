# MvPolynomial.hasseDeriv_zero_apply — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** The mathematical normalization law belongs with the proposed multivariate Hasse derivative API. Whether to export this pointwise helper separately from the bundled linear-map identity is an API design decision. Short closing simplification proofs are explicitly borderline under the skill's Phase 6b; they are not automatically a verified composition of at most three existing mathlib calls. This is a completed read-only assessment; the questions below concern future upstream design. Production sources and dependency pins remain unchanged.

## Phase 0 — baseline and provenance

Resolved public theorem at `Roth/HasseDeriv.lean:112–114`, in namespace `MvPolynomial`, with section parameters `{σ R : Type*} [CommSemiring R]`. The complete 294-line source file was read, including all preceding definitions and subsequent results. The file constructs multivariate Hasse derivatives and develops coefficient, composition, partial derivative, degree, and univariate compatibility interfaces.

The shared baseline is a successful `lake build` of 2467 jobs, exit 0. Reuse is justified by freshly recomputing and matching **all 17** source/pin hashes, not merely the target file. See [baseline](../evidence/MvPolynomial.hasseDeriv_zero_apply/baseline-build.txt), [hash check](../evidence/MvPolynomial.hasseDeriv_zero_apply/source-check.json), [manifest](../evidence/MvPolynomial.hasseDeriv_zero_apply/input-manifest.json), and [corrected target metadata](../evidence/MvPolynomial.hasseDeriv_zero_apply/corrected-target.json). The latter is source metadata, not a fresh elaborator output. Fresh formal receipts and exact executed sources are indexed by [verification](../evidence/MvPolynomial.hasseDeriv_zero_apply/verification.json). No admitted proof, new axiom, raised heartbeat/recursion limit, or production edit is used.

## Phase 1 — mathematical content

For every polynomial P over a commutative semiring, in any set of variables, the Hasse derivative of multi-order zero fixes P: Δ₀P=P. In the monomial formula, subtracting zero leaves the exponent unchanged and the product of binomial coefficients indexed by the support of the zero multi-index is the empty product, hence one. Equivalently, the zeroth operator is the identity linear map.

| Parameter | Mathematical role | Restriction |
|---|---|---|
| σ | Variable index type | Arbitrary; need not be finite, inhabited, or have decidable equality |
| R | Coefficient type | Arbitrary universe, commutative semiring |
| CommSemiring R | Coefficient/scalar algebra | Supplies polynomial operations and the existing R-linear derivative |
| P : MvPolynomial σ R | Input polynomial | Arbitrary, including zero and constants |

There are no additional hypotheses. Lean conclusion: `MvPolynomial.hasseDeriv 0 P = P`. The proof applies coefficient extensionality, rewrites by the project theorem `coeff_hasseDeriv`, and simplifies the zero-index binomial factor. Explicit project dependencies are `hasseDeriv` in the type and `coeff_hasseDeriv`, `hasseCoeff` in the body. No Roth-specific estimates, boxes, weights, or arithmetic hypotheses enter.

## Phase 2 — preliminary checks

**SMALL:** a basic operator normalization helper; it introduces no structure, is not the main theorem, and is not a named theorem. Hasse's name identifies the operator, not a distinct named theorem here. The one-line **definition** check is **n/a**, because this declaration is a theorem; the two proof tactics do not activate that definition-only exclusion. All literature channels were still run.

## Phase 3 — exhaustive literature search

Exact requests, response SHA256/byte counts, access outcomes, original concise summaries, source titles/URLs and locators are preserved in [web receipts](../evidence/MvPolynomial.hasseDeriv_zero_apply/web-requests.json). Full web responses and article text are not copied into this evidence package.

| Channel | Actual query/action | Finding and relevance |
|---|---|---|
| General web: specific | `multivariate Hasse derivative order zero identity arbitrary commutative ring` | Primary Berkeley paper, Example 2.6; polynomial translation coefficient definition in JACM Definition 3.4 |
| General web: general | `Hasse Schmidt derivation D0 identity commutative algebra` | Normalized endomorphic higher derivations have zero component identity |
| General web: aliases | `divided power differential operators Taylor expansion Hasse derivatives zeroth order` | Higher/divided derivatives, translation coefficients, and factorial-normalized derivatives are related formulations; characteristic restrictions belong to factorial division, not Δ₀ |
| ChatGPT math | Tool inventory checked | **n/a: ask_chatgpt_math unavailable**; no opinion fabricated |
| Local references | Read `.mathlib-quality/references/clean.tex:117–155`, and zero-order use at line 567 | Monomial definition and coefficient implementation note imply Δ₀P=P; paper later uses it in the index characterization |
| nLab | Domain search, specific-page search, direct page open | Indexed definition of Hasse-Schmidt derivation includes D⁰=Id over commutative rigs; direct XHTML unsupported |
| nCatLab | `site:ncatlab.org Hasse Schmidt derivation`; direct `/ncatlab/show/Hasse-Schmidt+derivation` | Domain search reaches nLab; distinct nCatLab route inaccessible. No separate categorical replacement inferred |
| Stacks | `site:stacks.math.columbia.edu Hasse Schmidt derivation`; directly read Tag 09CH | Definition 10.133.1 concerns general differential operators: order zero means S-linear, which need not be identity |
| MathOverflow | `site:mathoverflow.net Hasse Schmidt derivation characteristic zero` | Questions 71423 and 440759 distinguish higher/Hasse derivations, ordinary derivations, and differential operators; used as terminology/context leads |
| Recent arXiv | `site:arxiv.org Hasse Schmidt derivations 2022 2023 2024 2025 2026`; actual abs/PDF opens | Barajas 2305.04537, submitted 8 May 2023, Definition 1.1; Miyamoto 2509.00887, submitted 31 Aug 2025. Both within 2021-10-26–2026-10-26 |

The normalized multivariate law is explicit in [Moosa–Scanlon, *Generalised Hasse-Schmidt varieties*, Example 2.6](https://math.berkeley.edu/~scanlon/papers/jetB.pdf). The polynomial translation coefficient formulation in [*Fast Multivariate Multipoint Evaluation over All Finite Fields*, Definition 3.4](https://doi.org/10.1145/3652025) also gives the zero coefficient as P; the indexed definition was accessible, while direct DOI access returned 403. These establish standardness, not an existing Lean replacement.

The broader literature varies the codomain. [Barajas, Definition 1.1](https://arxiv.org/pdf/2305.04537) permits a zero component that is a general algebra homomorphism A→B, rather than identity. Thus replacing the concrete normalized polynomial operator with an arbitrary higher derivation into a different algebra changes this theorem's conclusion. [Stacks Tag 09CH, Definition 10.133.1](https://stacks.math.columbia.edu/tag/09CH) gives a second guard: arbitrary operators of order zero are linear maps, not all identity. Recent work [Miyamoto](https://arxiv.org/abs/2509.00887) confirms continuing geometric interest; its abstract is context, not evidence for a new weakening.

**Standard form:** the zeroth component of a normalized polynomial Hasse derivative family is identity. Generality dimensions: finite versus arbitrary variable types; ring versus semiring coefficients; normalized endomorphism versus a family with arbitrary algebra homomorphism as zero component. Current Lean already handles arbitrary variable types and commutative semirings. General-codomain families are related objects, not a missing hypothesis weakening of this fixed interface.

## Phase 4a–b — generality and all arguments

| Parameter/hypothesis | Literature comparison | Finding |
|---|---|---|
| σ : Type* | Papers commonly use finitely many variables | Current interface already allows infinitely many variables; each polynomial and multi-index is finitely supported |
| R : Type* | Commonly a commutative ring or field | Arbitrary universe retained; no characteristic, domain, field, or nontriviality assumption |
| CommSemiring R | Weaker than commutative ring | Fixed `hasseDeriv` is R-linear with this instance; merely removing commutativity is not a well-typed weakening of the present construction |
| P | Arbitrary polynomial | No support, degree, nonvanishing, or finiteness hypothesis to remove |

**MAXIMALLY GENERAL for the existing operator interface:** no verified mechanical weakening proposed. A module-valued or noncommutative reconstruction would require a new underlying family/construction; this assessment does not label it an available specialization theorem. Replacing the conclusion by arbitrary-map identity is false, as formally guarded below.

## Phase 4c — all nine modern-idiom checks

| # | Question | Applies? / proposed form | Concrete consequence |
|---|---|---|---|
| 1 | Typeclass preambles | Already done | CommSemiring is an instance; no custom ring predicate |
| 2 | Filters/nets instead of metric data | No | No topology or convergence |
| 3 | Universal-property characterization | Limited underlying diagnostic | Finsupp.lsum is a linear equivalence extending monomial maps; generic extension uniqueness organizes the construction, but does not remove the zero-order normalization proof |
| 4 | Bundled substructures | No | No closure predicate or subset in the statement |
| 5 | Weaken vector-space/field hierarchy | Already semiring | Compatible with positive characteristic and natural coefficients without division |
| 6 | Higher categorical reformulation | No | No categorical statement; no concrete downstream gain from categorification identified |
| 7 | Generalize concrete index ℕ | No for same object | Binomial coefficients and polynomial exponents are natural multi-indices; arbitrary additive indices require a different derivative family |
| 8 | Concrete-via-abstract proof diagnostic | **Fires** | After `coeff_hasseDeriv`, only equality of coefficients and empty product normalization remain. Any coefficient-preserving operator fixes polynomials; existing `MvPolynomial.ext` provides this generic step |
| 9 | False-generalization guard | **Reject arbitrary T / arbitrary weights** | Zero linear map on `MvPolynomial Unit ℕ` does not fix 1. Coefficient preservation/normalized zero weights must be supplied; an unnormalized HS zero homomorphism is not identity |

See [diagnostic](../evidence/MvPolynomial.hasseDeriv_zero_apply/concrete-via-abstract.json). The coefficient-preserving-map probe is a **new local helper proof**, demonstrating the abstraction, not an existing mathlib replacement for the normalization theorem. It enables maps with different constructions once their coefficient law is established; that law still contains the concrete content here. Therefore Q8 does not justify `YES-but-generalise-first` or a new generic API contribution without further evidence. The bundled equality `hasseDeriv 0 = LinearMap.id` does improve rewriting of compositions; the pointwise version is useful in evaluated nonvanishing goals. Their coexistence is the actual API choice.

## Phase 4.5 — infrastructure risk

**n/a — theorem.** This declaration introduces no definition, reducibility boundary, instance path, or coercion. Risks of the separately assessed `hasseDeriv` definition are not silently imported as this theorem's risk verdict.

## Phase 4.6 — all five strategy checks

| # | Check | Applies? | Alternative and decision |
|---|---|---|---|
| 1 | ε–δ versus filters | No | Algebraic finite coefficient identity |
| 2 | Elements versus ideal/submodule inclusion | No | Coefficient extensionality is the appropriate equality eliminator; no substructure inclusion to exploit |
| 3 | Sequences versus nets | No | No limiting process |
| 4 | Construction versus universal property | Limited | lsum uniqueness can organize the parent definition; not needed for this coefficient proof |
| 5 | Missing helper mathlib should have | No separate helper established | Empty-product simplification, extensionality, and reconstruction already exist; a dedicated multivariate zero lemma is an API question in the Hasse bundle |

**MATHLIB-IDIOMATIC.** Prove operator normalization from the coefficient formula or monomial extension; derive a pointwise corollary from the map equality if maintainers prefer that direction. No additional unrelated helper is needed. A proof depending on the already-proved project map identity must not count as independent composition evidence.

## Phase 5 — actual five-method search

All methods were actually invoked afresh on both the normalized current/literature statement and the abstract reconstruction form. The current and normalized literature forms coincide mathematically; they do not require different Lean names. Search services may index a different mathlib version; every actionable candidate must resolve in the pin, not merely in service output.

| Method | Queries | Findings / evidence |
|---|---|---|
| Lean-Finder | Multivariate Hasse derivative order zero identity; linear extension of single monomial maps identity | `Polynomial.hasseDeriv_zero'`, `Polynomial.hasseDeriv_zero`, LaurentSeries analogue; abstract Finsupp/DFinsupp extension lemmas. [Current](../evidence/MvPolynomial.hasseDeriv_zero_apply/finder-current.json), [abstract](../evidence/MvPolynomial.hasseDeriv_zero_apply/finder-abstract.json) |
| Loogle | `Polynomial.hasseDeriv 0 _ = _`; `Finsupp.lsum` | Univariate pointwise identity; lsum extension and inverse formulas. [Current](../evidence/MvPolynomial.hasseDeriv_zero_apply/loogle-current.json), [abstract](../evidence/MvPolynomial.hasseDeriv_zero_apply/loogle-abstract.json) |
| LeanSearch | Zeroth multivariate derivative itself; summing monomials recovers polynomial | Univariate analogues and reconstruction candidates. [Current](../evidence/MvPolynomial.hasseDeriv_zero_apply/search-current.json), [abstract](../evidence/MvPolynomial.hasseDeriv_zero_apply/search-abstract.json) |
| rg source | Untruncated full names, zero-operator aliases, lsum, sum reconstruction, coefficient equivalence | Positive pinned sources in Polynomial/HasseDeriv, MvPolynomial/Basic, Finsupp/LSum, MonoidAlgebra. [Exact commands/results](../evidence/MvPolynomial.hasseDeriv_zero_apply/grep-receipts.json) |
| Local name search | `hasseDeriv_zero`; `lsum` | Positive source candidates, with **index unavailable**. Evidence-artifact copies were excluded as authoritative candidates. Empty/generated-name absence is not inferred. [Current](../evidence/MvPolynomial.hasseDeriv_zero_apply/local-current.json), [abstract](../evidence/MvPolynomial.hasseDeriv_zero_apply/local-abstract.json) |

Candidate distinction: `Polynomial.hasseDeriv_zero'` takes a univariate polynomial and natural order; it does not directly accept arbitrary `MvPolynomial σ R` with multi-index. A `Unique σ` equivalence would restrict σ and need the project's compatibility result, so it is not an independent replacement. `LaurentSeries.hasseDeriv_zero` similarly has another domain and cannot replace this theorem. `MvPolynomial.support_sum_monomial_coeff` and `AddMonoidAlgebra.sum_coeff_single` reconstruct a polynomial; they are building blocks after normalization, not an immediate statement about the Hasse operator. `Finsupp.lsum_single` only evaluates an extension on a single supported input, not a general P. An assumed `Finsupp.lsum_lsingle` is absent from the inspected pinned LSum source; the actual generic inverse law is `LinearEquiv.apply_symm_apply` with `Finsupp.lsum_symm_apply`.

**Conclusion:** positive analogues and generic building blocks found; no verified direct existing-mathlib replacement for the arbitrary-variable target. This is a bounded evidence conclusion, not a theorem of global absence. The isolated formal probe guards against importing the project theorem and probes generic elaboration routes.

## Phase 5.5 — all three statement-shape checks

**Normal form:** equivalent forms are Δ₀P=P, Δ₀=id as linear maps, and coefficientwise preservation. The first two mirror `Polynomial.hasseDeriv_zero'`/`Polynomial.hasseDeriv_zero`; coefficientwise equality is a proof interface. RHS P/id is the simplified normal form. No orthogonal equivalence web is introduced. **OK.**

**Syntactic generality:** pointwise form takes an explicit P and rewrites nested eval/nonzero goals; map equality rewrites higher-order operators and compositions without introducing P. Both were actually tested. Prefer the map equality as the bundled normalization, with a pointwise corollary only if API policy requests it. No independent mathematical generalization occurs. **OK, subject to the recorded API choice.**

**Superfluous arguments:** σ supplies the exponent index; R supplies coefficients/scalars; CommSemiring supplies the existing linear operator; P is the pointwise input. All are required by the stated interface. P can disappear only by changing to map equality, not by deleting a redundant hypothesis. No extra Fintype, DecidableEq, Nontrivial, characteristic, or field assumption exists. **NONE to drop.** Overall **SHIP-AS-STATED if the pointwise corollary is retained**, otherwise use the existing project map identity after choosing its independent proof.

## Phase 6 — callers, inline audit, actual composition attempts

Scope is **explicit Lean source references**, not an opaque kernel or simp dependency closure. There are three caller occurrences in two declarations: one within the declaring file and two outside it in one file.

| Caller | Exact use | Proposed future alternative |
|---|---|---|
| `MvPolynomial.hasseDeriv_zero`, HasseDeriv.lean:121 | `LinearMap.ext hasseDeriv_zero_apply` | Independently prove map equality by extensionality and coefficient normalization; avoid circularly using the pointwise theorem being removed |
| `Roth.index_eq_zero_iff`, Index.lean:104 | `simpa [hasseDeriv_zero_apply] using hd` | Use `[hasseDeriv_zero]` or its simp normal form |
| Same, Index.lean:105 | `by simpa [hasseDeriv_zero_apply] using h` | Same map identity normalization at d=0 |

Outside-the-declaring-file count K=2 occurrences, 1 distinct declaration, 1 file. Including the in-file caller: 3 occurrences, 2 declarations. No external downstream library was searched or claimed. Inline audit searched `hasseDeriv 0`, zero-operator names, and coefficient normalization across production Roth files; no independent re-derivation of this identical pointwise assertion was found. Other zero-order uses relying on the `[simp]` map theorem are API consumers, not necessarily explicit references to this helper. This count is not a dead-code judgment.

Actual attempted routes and exact accepted/rejected diagnostics are recorded in [verification](../evidence/MvPolynomial.hasseDeriv_zero_apply/verification.json):

1. **Coefficient route:** extensionality followed by the project coefficient formula and empty-product simplification. An explicit `simp only` replay avoids accidentally succeeding through the downstream project `hasseDeriv_zero` simp theorem. This is a proof using a project API, not solely existing mathlib calls.
2. **Unfolded construction:** test simplification of the underlying lsum extension, zero exponent subtraction, scalar one, and sum reconstruction. A rejected initial short simplification is retained separately; only the final clean version counts. The isolated reconstruction imports mathlib only and uses `#check_failure MvPolynomial.hasseDeriv_zero_apply`.
3. **Generic routes:** `exact?` was actually attempted on the isolated local operator and reached the default 200,000 heartbeat limit during normalization. This rejected search run is preserved as a limitation, not an absence result; it is excluded from accepted diagnostics and no limits were raised. `apply?` was not reached on that target. Separate `exact?` and `apply?` positive controls succeeded, and candidate univariate identity, full reconstruction and linear-map extensionality signatures were checked. A newly proved local generic helper does not count as an existing replacement. Any bare imported-target `simp` success is circular design evidence only.
4. **Caller replacement:** actual independent map-equality proof and the complete index characterization proof with pointwise-helper mentions replaced by the map identity. Formal success means these future alternatives are viable, not that source files were edited.

**Composition classification:** no standalone ≤3 existing-call replacement established for the underlying operator identity. A terminal `simp` proof after expanding definitions is a **trivial simp composition** under Phase 6b, hence **BORDERLINE**, not automatic NO. A normalization proof can still justify a named API law. Conversely the pointwise wrapper could be removed if maintainers choose only the bundled map normalization; that removal is conditional on API policy, not on a fabricated pre-existing multivariate mathlib theorem.

## Phase 7 — verdict and actionable next step

**BORDERLINE-needs-human.** Literature establishes a standard normalization law and current hypotheses already cover the fixed operator broadly. Searches establish relevant univariate analogues and generic normalization machinery. Formal tests distinguish independent proofs from circular use of the project's later `[simp]` theorem, and show how explicit callers can use the bundled equality. The remaining choice is whether the multivariate API should expose both forms, or one canonical bundled identity with simplification supplying the pointwise use.

The result belongs with the prospective `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean` API, grouped with the already-assessed `hasseDeriv` and `coeff_hasseDeriv` work if retained. It does not belong in Archive or an unrelated algebra abstraction: the law normalizes a standard polynomial operator. No fresh standalone PR or generic weighted-operator theorem is proposed merely to justify this small corollary.

Numbered future upstream design questions (short answers; no approval is required to finish this read-only overview):

1. Should the multivariate API export both the pointwise zero law and the `[simp]` bundled map equality, following the existing univariate API? **yes/no**
2. If both are exported, should the pointwise theorem be named `hasseDeriv_zero_apply`, or match the univariate `hasseDeriv_zero'`? **name choice**
3. If only map equality is exported, should its independent coefficient-normalization proof replace the pointwise-helper proof and should `index_eq_zero_iff` simplify via that map theorem? **yes/no**

If question 1 is yes, retain the normalization corollary inside the Hasse API PR and run `/generalise MvPolynomial.hasseDeriv_zero_apply`, then `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_zero_apply` before upstreaming. If no, prove `hasseDeriv_zero` independently, update both Index occurrences to use it, then delete the helper; the caller probes make that alternative reviewable. The assessment itself makes no source edit and does not await these future choices.

## Phase 8 — completion and evidence limitations

All workflow phases completed, with theorem-only n/a in Phase 4.5 and the optional unavailable ChatGPT channel recorded. Verification has no unresolved technical item; future API questions are not failed checks. Search-service versions may differ from the pin, local symbol indexing is unavailable, nLab direct XHTML and nCatLab access failed, one arXiv HTML-version guess failed before the PDF/abstract fallback succeeded, and an isolated `exact?` search hit the default heartbeat bound (no negative inference). These are retained as access limitations, not negative absence claims. Full raw formal/native receipts and exact executed Lean sources are preserved; web evidence is metadata and original concise summaries only. Root acceptance remains pending independent review.
