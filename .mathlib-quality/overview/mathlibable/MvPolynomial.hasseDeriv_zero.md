# MvPolynomial.hasseDeriv_zero — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** The canonical bundled normalization law is standard and useful as a simp rule, but the independently reconstructed operator normalizes using a closing `simp`. Phase 6b explicitly treats this as a policy judgment. This assessment does not inherit another declaration's verdict. The original one-line term invokes a project theorem; `LinearMap.ext` alone does not establish Hasse normalization.

Read-only assessment of `Roth/HasseDeriv.lean:120–121`, branch `ramin-cleanup`. No production, dependency-pin, Git, progress, or overview changes. All questions below concern future upstream design; no user input is required to finish this assessment.

## Phase 0 — Doctor

All 17 source/pin hashes independently match the shared successful baseline. See [hash check](../evidence/MvPolynomial.hasseDeriv_zero/source-check.json), [input manifest](../evidence/MvPolynomial.hasseDeriv_zero/input-manifest.json), and [baseline build](../evidence/MvPolynomial.hasseDeriv_zero/baseline-build.txt). Canonical corrected metadata is preserved in [target metadata](../evidence/MvPolynomial.hasseDeriv_zero/corrected-target.json).

The current theorem resolves with its full elaborated type in [native target receipt](../evidence/MvPolynomial.hasseDeriv_zero/target-lsp.json). It has no placeholder proof. Module purpose: multivariate Hasse derivatives and their coefficient, composition, and univariate compatibility API. Axioms are only `propext`, `Classical.choice`, `Quot.sound`.

```lean
∀ {σ R : Type*} [CommSemiring R],
  MvPolynomial.hasseDeriv (0 : σ →₀ ℕ) =
    (LinearMap.id : MvPolynomial σ R →ₗ[R] MvPolynomial σ R)
```

The [exact executed target source](../evidence/MvPolynomial.hasseDeriv_zero/target-executed.lean) checks the original term, a coefficient proof that avoids the normalization theorem, and an unfolded construction proof. All pass with zero errors and zero warnings. The [isolated mathlib source](../evidence/MvPolynomial.hasseDeriv_zero/mathlib-executed.lean) imports only `Mathlib.Algebra.MvPolynomial.PDeriv`, `Mathlib.Algebra.Polynomial.HasseDeriv`, and `Mathlib.Data.Nat.Choose.Bounds`, guards `#check_failure MvPolynomial.hasseDeriv_zero`, and proves the independently copied construction identity. Its [native receipt](../evidence/MvPolynomial.hasseDeriv_zero/mathlib-lsp.json) is successful, without resource-limit changes.

## Phase 1 — Comprehend

For polynomials in any collection of commuting variables with coefficients in a commutative semiring, taking the Hasse derivative at the zero multi-index does nothing. More precisely, the entire linear operator equals the identity operator, so it can be rewritten inside compositions before applying it to a polynomial. Each monomial retains its exponent and coefficient because subtracting zero changes no exponent and every binomial factor has lower entry zero.

Parameters: `σ` is an arbitrary variable type; `R` is an arbitrary coefficient type; `[CommSemiring R]` supports multivariate polynomials and the coefficient-linear operator. There are no explicit hypotheses, finiteness assumptions, nontriviality assumptions, characteristic restrictions, or decidable-equality requirements. The zero multi-index is the distinguished index of this normalization law.

The direct project dependency is `MvPolynomial.hasseDeriv_zero_apply`; the statement uses the definition `MvPolynomial.hasseDeriv`. The current proof is exactly `LinearMap.ext hasseDeriv_zero_apply`.

## Phase 2 — Preliminary checks

SMALL: a structural normalization theorem, not a new structure or a principal project theorem. Theorem/lemma one-line-definition exemptions are n/a. Its one-line proof is neither `rfl` nor a single unfold, so narrow glue inheritance does not apply. Shortness reflects an extensionality step over a project-local mathematical identity, not an existing mathlib replacement.

## Phase 3 — Exhaustive literature

All nine required channels were checked. Every actual request, returned-representation SHA256/byte length, status, title URL, locator where relevant, and original concise summary is in [web metadata](../evidence/MvPolynomial.hasseDeriv_zero/web-requests.json). No copied article or search-result bodies are persisted. Thirteen distinct real web search queries ran, followed by primary-source opening and locator checks.

| Channel | Actual query or inspection | Result and relevance |
|---|---|---|
| WebSearch, specific | `multivariate Hasse derivative order zero identity arbitrary characteristic` | Polynomial Hasse derivatives use the binomial monomial formula; zero order preserves the polynomial. |
| WebSearch, general | `Hasse Schmidt derivation D_0 identity commutative algebra` | Normalized higher endomorphism families have identity zero component; source/target variants require care. |
| WebSearch, aliases | `divided power derivatives multiindex Taylor coefficients zero order` | Taylor coefficient and divided differential terminology; factorial inversion is unnecessary. |
| ChatGPT MCP | Capability inventory inspected | n/a: `ask_chatgpt_math` unavailable. Optional channel; other channels completed. |
| Local references | `.mathlib-quality/references/clean.tex`, §Derivatives, lines 121–155 | Explicit monomial formula over any commutative semiring; empty product and zero exponent shift give this law. [Exact excerpt](../evidence/MvPolynomial.hasseDeriv_zero/local-reference-excerpt.tex). |
| nLab | `site:ncatlab.org/nlab Hasse Schmidt derivation`; `site:ncatlab.org/nlab divided power differential operator` | Indexed Hasse-Schmidt derivative entry gives the rig-level construction and zero-order law. Direct XHTML opening unsupported; indexed text inspected. |
| nCatLab | `site:ncatlab.org Hasse Schmidt derivation higher derivation`; `site:ncatlab.org/nlab jet algebra Taylor expansion` | nLab higher-derivation and jet formulations found; separate nCatLab path inaccessible. No independent categorical replacement found. |
| Stacks | `site:stacks.math.columbia.edu Hasse Schmidt derivation`; `site:stacks.math.columbia.edu divided power differential operators` | Opened tag 07GL. Divided-power operations have a different zero normalization; not a substitute. |
| MathOverflow / MSE | `site:mathoverflow.net Hasse Schmidt derivation D_0`; `site:math.stackexchange.com Hasse derivative multivariate` | Higher derivation versus differential operator discussion and jet interpretation. First-order chain-rule question is a terminology near miss. |
| Recent arXiv | `site:arxiv.org Hasse Schmidt derivations 2022 2023 2024`; `site:arxiv.org multivariate Hasse derivatives 2025 2026` | Relevant 2023 and May 2026 work found in 2021-10-26 through 2026-10-26 window. Opened May 2026 paper Definition 2.1, Proposition 2.3; not merely search dates. |

Primary mathematical anchors: [Narváez Macarro, mini-course, Definition 2.1.1, printed pp. 14–15](https://personal.us.es/narvaez/course_HS_2018.pdf) explicitly separates general algebra-map zero components from normalized endomorphisms. [Barajas–Duarte, May 2026, Definition 2.1 and Proposition 2.3](https://arxiv.org/html/2605.20664v1) retains that distinction. These support the judgment that abstract higher-derivation infrastructure is a possible future framework, but changing to it would not automatically prove the concrete polynomial normalization. The [Stacks definition of divided powers](https://stacks.math.columbia.edu/tag/07GL) concerns a different operation. The [MO higher-derivation/differential-operator question](https://mathoverflow.net/questions/440759/what-is-the-relationship-between-higher-order-derivations-in-the-sense-of-hasse) is contextual evidence, not the primary proof source.

Concept: zeroth multivariate Hasse derivative / normalized higher derivative. Sources agree on the concrete polynomial law. Generality varies between finite lists of variables and finitely supported multi-indices, semirings/rings/fields, and normalized endomorphisms versus general source/target higher derivations. The project already supports arbitrary variable types and commutative semirings. No historical claim is inferred from search ranking or crawl dates.

## Phase 4a–b — Every argument and generality

| Parameter or assumption | Essential role | Weakening assessment |
|---|---|---|
| `σ : Type*` | Variables and finitely supported multi-indices | Already arbitrary, universe-polymorphic; no `Finite`, `Fintype`, or `DecidableEq` to drop. |
| `R : Type*` | Coefficients and scalars | Arbitrary, universe-polymorphic; no field, domain, characteristic, or nontriviality assumptions. |
| `[CommSemiring R]` | Existing `MvPolynomial σ R` and `R`-linear operator interface | At the existing interface floor. Noncommutative coefficients require rebuilding the operator/scalar interface, not dropping an instance from this statement. |
| Index fixed as zero | Encodes normalization | Replacing zero with arbitrary `d` is false: positive-order derivatives kill constants. |
| Bundled linear-map conclusion | Captures operator equality | Already avoids quantifying a particular polynomial; can rewrite inside composition and obtain application equality. |

MAXIMALLY GENERAL for the existing operator interface; zero verified droppable arguments. The isolated native proof verifies the current arbitrary-variable semiring formulation. We do not report an untested class weakening as successful. A module-valued or arbitrary higher-derivation framework is a separate foundational design, not an established one-edit generalization.

## Phase 4c — All nine modern-idiom checks

| # | Check | Answer, proposed form, and downstream consequence |
|---|---|---|
| 1 | Typeclass preambles | No new change: `CommSemiring` is already an instance, no bundled predicate to replace. |
| 2 | Filters/nets | No: finite algebraic sums, no topology. |
| 3 | Universal property | Possible framework only: Taylor substitution with constant coefficient projection recovers normalization, but constructing that bridge is substantive. It would organize future Taylor coefficient and substitution laws, not eliminate this construction check. |
| 4 | Bundled substructures | No: result is already an equality in bundled linear maps, not a closure predicate. |
| 5 | Module hierarchy | No mechanical improvement: semiring scalars already present; module-valued polynomial extension needs new definitions and compatibility API. |
| 6 | Higher category | No relevant higher-categorical statement with concrete benefits here. |
| 7 | Generalize natural index | No: natural exponent combinatorics defines polynomial Hasse derivatives; arbitrary additive indices lack binomial coefficients and truncated exponent subtraction. |
| 8 | Concrete-via-abstract | Diagnostic fires: proof body has one line containing `hasseDeriv`, solely in the project normalization lemma name, and the combinator `LinearMap.ext` is abstract. Proposed abstract statement: `(∀ P, T P = P) → T = LinearMap.id`; existing `LinearMap.ext` proves it. This supports bundling any pointwise identity, but the hypothesis is precisely the normalization content. It is not an independent proof of `Δ₀ = id`. Coefficient-preserving variant also checked. |
| 9 | False-generalization guard | Reject unconditional `T = id` for arbitrary linear maps; the zero map on `MvPolynomial Unit ℕ` is a compiled counterexample. Reject replacing Hasse differential operators by divided-power operations or arbitrary source/target higher derivations: their zero components have different semantics. |

[Exact isolated source](../evidence/MvPolynomial.hasseDeriv_zero/mathlib-executed.lean) proves both proposed abstract implications and the false-map guard, all with standard axioms. No supported modern-idiom restatement removes specialized normalization while preserving the result. Bundling is already the useful modern form, enabling linear-map composition normalization.

## Phase 4.6 — Five proof-strategy checks

| # | Question | Assessment |
|---|---|---|
| 1 | Topology: filters versus explicit neighborhoods | n/a: no topology. |
| 2 | Algebra: elements versus bundled inclusions | Current proof is idiomatic extensionality for bundled operator equality; no ideal/submodule inclusion is involved. |
| 3 | Analysis: sequences versus nets | n/a: no limits. |
| 4 | Category theory: construction versus universal property | Taylor/universal-property approach is a broader future API, with an unproved compatibility bridge; unnecessary for this local normalization. |
| 5 | Missing helper mathlib should have | Multivariate Hasse derivative definition and coefficient API are the specific missing context. `LinearMap.ext` and polynomial reconstruction already exist; no invented abstract helper is needed. |

MATHLIB-IDIOMATIC. The existing one-line extensionality proof is appropriate if the pointwise theorem remains. If exporting only bundled normalization, prove it independently by the checked coefficient or unfolded route, then derive pointwise equality with `LinearMap.congr_fun`. This avoids making the bundled theorem depend on a helper that would be removed.

## Phase 4.5 — Infrastructure risk

n/a: theorem introduces no definition, class, instance, coercion, reducibility boundary, or typeclass path. Simp orientation is assessed separately below.

## Phase 5 — All five actual mathlib methods, all three forms

Current form: multivariate `hasseDeriv 0 = LinearMap.id`. Literature form: zero component of a normalized Hasse–Schmidt family is identity. Abstract form: a pointwise identity linear map is identity, with polynomial reconstruction as a potential route. The current and literature forms coincide on this object; both were still searched explicitly.

| Method | Current / literature / abstract requests | Result |
|---|---|---|
| Lean-Finder | `Multivariate polynomial Hasse derivative of multi-index zero equals the identity linear map`; `Zero component of a Hasse Schmidt derivation is the identity endomorphism`; `A linear map that fixes every polynomial is the identity; reconstruct polynomial as sum of monomials` | Univariate and Laurent-series analogues; abstract search returned polynomial reconstruction near matches, no independent concrete multivariate identity. |
| Loogle | `"hasseDeriv", "zero"`; `"hasseDeriv", LinearMap.id`; `LinearMap, _ = LinearMap.id` | `Polynomial.hasseDeriv_zero`, Laurent-series analogue, generic map identity API. |
| LeanSearch | `Hasse derivative order zero is identity for multivariate polynomials`; `zeroth higher divided derivative is identity linear endomorphism`; `linear map equals identity if it fixes every element` | Same analogues; fixed-point and map application identities. |
| `rg` pinned source | Hasse/zero identifiers; `support_sum_monomial_coeff`, `sum_coeff_single`, `lsum_comp_lsingle`, `coeffLinearEquiv`; project inline identity patterns | Univariate exact analogous statement and reconstruction/extension building blocks. No multivariate Hasse API in inspected pinned source. |
| Local name search | `hasseDeriv_zero`; `HasseSchmidt`; `LinearMap.ext` | Reports index unavailable. Positive filesystem fallbacks include source target and univariate/Laurent-series names; project/evidence copies excluded as mathlib hits. Empty fallback results imply no absence claim. |

Twelve exact external/name search receipts accompany the [untruncated pinned/source searches](../evidence/MvPolynomial.hasseDeriv_zero/grep-receipts.json): `finder-{current,literature,abstract}.json`, `loogle-{current,literature,abstract}.json`, `search-{current,literature,abstract}.json`, `local-{current,literature,abstract}.json` in this evidence directory. External indexes may use another mathlib version; pinned source and native checks verify positive candidates.

`Polynomial.hasseDeriv_zero` at `Mathlib/Algebra/Polynomial/HasseDeriv.lean:86` has precisely the analogous bundled equality over `[Semiring R]`, and its proof is `LinearMap.ext <| hasseDeriv_zero'`. It is about `Polynomial R`, not `MvPolynomial σ R`; no supplied transport turns arbitrary many-variable operators into that theorem in one line. `LaurentSeries.hasseDeriv_zero` is likewise a distinct type and indexing construction. Generic `LinearMap.ext` needs the unproved concrete pointwise premise. These are moral analogues and building blocks, not an exact duplicate.

## Phase 5.5 — Statement shape

Normal-form alternatives: bundled `Δ₀ = LinearMap.id`; pointwise `Δ₀ P = P`; coefficientwise equality. The bundled form agrees with mathlib's univariate canonical shape, has identity on the RHS, and supports both higher-order rewriting and application simplification. It is oriented correctly as a terminating simp rule. Coefficient form is the computational proof interface, not a better public zero-law normal form.

Syntactic generality: bundled form chosen; pointwise form is easier at a polynomial-specific site but follows from the bundled equality via `LinearMap.congr_fun`. Both were actually exercised in native checks. Generic coefficient-preservation implication retains explicit hypotheses and is not a replacement statement. Superfluous-argument audit: `σ`, `R`, and `[CommSemiring R]` have the roles in Phase 4; none can be dropped from the existing interface. Overall SHIP-AS-STATED if inclusion is approved; selection of one or both public zero-law forms remains a design question.

## Phase 6.0 — Callers and inline audit

Scope is explicit references in project Lean source only, not an exhaustive opaque kernel or simp dependency closure. Search roots were `Roth` and `Roth.lean`, excluding `.lake` and assessment evidence.

| Scope | Count / finding |
|---|---|
| In-file explicit theorem-name proof callers | 0; own declaration and preceding documentation excluded. |
| External-to-file explicit callers | 0 in 0 files. |
| Pointwise neighboring theorem callers | Two references in `Roth/Index.lean:104–105`, to `hasseDeriv_zero_apply`, not this bundled theorem. |
| Inline bundled re-derivations | None found in searched project source. The preceding pointwise theorem is related normalization, not an inline bundled-map proof. |
| Implicit use | Target is tagged `[simp]`; zero explicit references do not establish dead code. Native representative application and map-composition consumers close with bare `simp`. |

[Consumer source](../evidence/MvPolynomial.hasseDeriv_zero/consumer-executed.lean) and [native receipt](../evidence/MvPolynomial.hasseDeriv_zero/consumer-lsp.json) demonstrate actual simplifier value without claiming to enumerate every existing implicit use. Removing the theorem would require auditing simplifier uses as well as explicit references.

## Phase 6 — Actual compositions and policy boundary

1. **Original project route, succeeds:** `LinearMap.ext MvPolynomial.hasseDeriv_zero_apply`. One existing mathlib call plus a project theorem. It is not a mathlib-only composition, and it does not qualify for glue inheritance.
2. **Generic abstract route, succeeds conditionally:** `LinearMap.ext h` for `h : ∀ P, T P = P`. Existing combinator, but concrete normalization remains in `h`; the false-map guard prevents discarding it.
3. **Univariate replacement, partial only:** `Polynomial.hasseDeriv_zero` proves the analogous theorem on another type. No identified <=3 existing-call transport establishes the arbitrary-variable operator identity.
4. **Coefficient route, succeeds independently of both zero theorems:** explicit linear-map and coefficient extensionality, then `simp only [coeff_hasseDeriv, add_zero, hasseCoeff, Finsupp.prod_zero_index, Nat.cast_one, one_mul]`. Uses a project computational theorem; no accidental target simp lemma invocation.
5. **Mathlib-only construction route, succeeds independently:** exact local `delta` copies the operator with the coefficient product written out. Native proof:

```lean
  apply LinearMap.ext
  intro P
  change delta 0 P = P
  simp [delta, Function.comp_def, LinearMap.lsmul_apply, sum_def]
```

Reconstruction is supported by `MvPolynomial.support_sum_monomial_coeff`, `AddMonoidAlgebra.sum_coeff_single`, linear extension, and binomial/empty-product normalization. This closes the bundled equality too, not only its pointwise version. It is a closing-simp proof, explicitly BORDERLINE under Phase 6b. No verified <=3 existing-term derivation of the concrete map identity was identified. This does not assert mathematical nonexistence of such a term; search failure and prior unrelated heartbeat limits are not absence evidence. No resource limit was raised or used as a verdict reason.

## Phase 7 — Actionable verdict and alternatives

**BORDERLINE-needs-human**, based on the independently demonstrated closing-simp composition and API choice, rather than an inherited verdict or missing evidence. The standard bundled law provides a useful, discoverable rewrite with the exact same shape as univariate mathlib. Conversely it adds no new mathematics beyond construction normalization and can be obtained by the checked proof. Phase 6b assigns this boundary to API taste. Zero explicit references are weak evidence because the theorem is a registered simp rule; representative implicit consumers actually pass.

Future upstream design questions (no input needed for this read-only assessment):

1. Should the multivariate Hasse API export its bundled zero-order equality as a named `[simp]` normalization theorem, despite its short construction-normalization proof?
2. Should it also export the pointwise theorem, or derive pointwise identities from bundled normalization when needed?
3. If both forms are exported, should pointwise naming match univariate `hasseDeriv_zero'` or use the descriptive `_zero_apply` name?

If inclusion is approved, ship with the accepted-YES definition `MvPolynomial.hasseDeriv` and coefficient interface `MvPolynomial.coeff_hasseDeriv`, in proposed `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`. Proposed PR title: `feat(Algebra/MvPolynomial): add multivariate Hasse derivatives`. Checklist: `/generalise MvPolynomial.hasseDeriv_zero` to reconfirm the instance floor; `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_zero` and related exported API; choose a reviewer from recent commits to `Mathlib/Algebra/Polynomial/HasseDeriv.lean` and the multivariate polynomial area. This is a future plan, not an opened PR or production edit.

If the bundled theorem is rejected as API duplication, retain normalization project-locally until simplifier callers have been audited. Its explicit caller refactor list is empty; implicit uses must receive the checked construction/coefficient normalization at their actual sites or keep a local simp fact. The two `Index.lean` pointwise sites are not callers of this target and must not be silently changed as part of deleting only the bundled theorem. An unconditional NO-composable claim based only on `LinearMap.ext` would omit a necessary mathematical premise.

Rejected buckets: NO-mathlib-has-it lacks a matching multivariate theorem; NO-composable lacks a verified <=3 genuine existing-call term and would override the explicit closing-simp policy; YES-but-generalise-first lacks a verified one-edit weakening with preserved meaning; YES-add-as-is would silently resolve the explicit policy boundary without the upstream API decision.

## Phase 8 — Completion and evidence limits

All phases PASS; Phase 4.5 is n/a for theorem. [Verification index](../evidence/MvPolynomial.hasseDeriv_zero/verification.json) identifies exact successful native sources and receipts; all accepted probes have zero errors/warnings, no placeholder axioms, and only the standard printed axioms. [Assessment JSON](../evidence/MvPolynomial.hasseDeriv_zero/assessment.json), [overview entry](../evidence/MvPolynomial.hasseDeriv_zero/overview-entry.json), [copy manifest](../evidence/MvPolynomial.hasseDeriv_zero/copy-manifest.json), and [portable validator](../evidence/MvPolynomial.hasseDeriv_zero/validate.py) complete the package.

Limitations: optional ChatGPT mathematical service unavailable; local index unavailable; direct nLab XHTML and separate nCatLab access failed, with indexed relevant content inspected; external search versions can differ from the pin; explicit caller scope excludes opaque/implicit dependency closure. No limitation prevents the read-only assessment, and none is treated as proof of absence. Root acceptance remains pending.
