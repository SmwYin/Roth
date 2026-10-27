# Roth.wronskian_ne_zero_of_natDegree_injective — full mathlibable assessment

Canonical declaration 47, `Roth/Wronskian.lean:148`. **Recommended verdict: YES-but-generalise-first.** The verified local change removes global characteristic zero in favor of injectivity of the degrees after casting into the coefficient field. A separately verified expanded determinant statement additionally works over an integral domain. This judgment is independent of the earlier assessments of the Wronskian definitions and its coefficient/determinant helpers.

## Phase 0 — baseline and declaration

The shared baseline `lake build` completed successfully (2467 jobs). All 17 production-source and pin hashes were freshly matched to the shared baseline manifest. The entire declaring module, its actual caller, and the relevant mathlib files were read. The root's native replay compiles the original proof and resolves the target with no errors, warnings, partial result or nonstandard axioms. Production files and pins remain unchanged.

Evidence: [baseline](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/baseline-build.txt), [fresh source/pin hashes](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/source-pin-hashes.json), [complete declaring module](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/source-wronskian.lean.txt), [native target receipt](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/native-target-success.json), [selected native evidence](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/native-selected.json).

Full native elaborated type:

```lean
@Roth.wronskian_ne_zero_of_natDegree_injective :
  ∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]},
    (∀ (ν : Fin l), φ ν ≠ 0) →
    (Function.Injective fun ν ↦ (φ ν).natDegree) → Roth.wronskian φ ≠ 0
```

## Phase 1 — mathematical content

A finite family of nonzero univariate polynomials over a characteristic-zero field, with pairwise distinct degrees, has nonzero Hasse Wronskian. This Wronskian uses derivative orders 0 through l−1, each divided by its factorial in characteristic zero. Empty families are included: their determinant is1.

`K` is the universe-polymorphic coefficient carrier; `Field K` supplies commutative arithmetic and the existing parent interface; `l` is the finite square size; `φ` is the polynomial family. `hφ` excludes zero columns, including the ambiguity that zero and nonzero constants both have natural degree0. `hd` separates the top degrees; `CharZero` transfers this separation to scalar degree casts and prevents factorial vanishing in the source proof. The conclusion asserts inequality with the zero polynomial, not nonvanishing at every scalar point.

The source proof contradicts an assumed zero Wronskian by computing one coefficient, in degree Σdegφ−Σrow. Its value is the product of leading coefficients times the binomial determinant. `Roth.det_choose_eq` rewrites that determinant as inverse factorials times the Vandermonde difference product. Every factor is nonzero under the hypotheses. These two Roth lemmas are project contributions, not existing mathlib calls.

## Phase 2 — preliminary checks

**BIG**: explicitly listed in the module's Main results, line 30. The definition-only one-line test and its three exemptions are **n/a: theorem**. The short source proof does not establish mathlib composability because its mathematical work is in project helpers.

## Phase 3 — exhaustive literature

Every named channel was searched or explicitly recorded unavailable; three distinct actual general-web queries were executed. [Literature ledger](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/literature.json), [general requests and response hashes](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/web-general-metadata.json), [named channels](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/web-named-metadata.json), [recent/MO queries](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/web-recent-metadata.json), [primary access](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/web-primary-metadata.json), [direct opens](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/web-opens-metadata.json). Web artifacts retain exact requests, hashes/bytes/status and locators, with original concise summaries; article/search bodies are not persisted.

| Channel | Actual request/access | Result |
|---|---|---|
| General specific | `Wronskian polynomials distinct degrees nonzero Vandermonde` | Located Bostan–Dumas and a recent exact polynomial degree calculation. |
| General generality | `Hasse Wronskian distinct degrees modulo characteristic nonzero` | Characteristic obstruction and degree-cast separation need explicit treatment. |
| General aliases | `Bostan Dumas Wronskians linearly independent polynomials leading coefficients` | Ordinary Wronskians and formal-series orders; normalization differs from Hasse form. |
| ChatGPT MCP | n/a: `ask_chatgpt_math` unavailable | No second-opinion/historical response claimed. |
| Local references | `clean.tex` §2 first lemma, lines170–194; exact `rg` recorded | Exact Hasse normalization and distinct-degree nonvanishing proof. |
| nLab | `site:ncatlab.org/nlab Wronskian`; direct page | Search returns conventional definition. Direct open fails400 unsupported XHTML. |
| nCatLab | `site:ncatlab.org/ncatlab Wronskian determinant`; direct path | Search gives nLab context; direct path inaccessible. No separate categorical refinement found. |
| Stacks | `site:stacks.math.columbia.edu Wronskian`; tag0FJ9 | Read finite-projective determinant infrastructure; no degree-separation theorem on accessed page. |
| MathOverflow | `site:mathoverflow.net Wronskian polynomials positive characteristic distinct degrees` | Eremenko's answer361565 gives coordinate-recovery applications; no exact target. A separate guessed question33270 direct open was inaccessible, not treated as a hit. |
| arXiv last five years | `site:arxiv.org Wronskian polynomials distinct degrees after:2021-10-26 before:2026-10-27` | Hermoso–Alcázar2024 Proposition2 is a direct polynomial leading-degree source; Kenins–Kiselev2026 gives related iterated-degree applications. |

Primary anchor: [Bostan–Dumas, *Wronskians and linear independence*, PDF pp2–3, Lemmas1 and3](https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf) proves the ordinary monomial determinant formula and a lowest-order analogue for formal series. Its characteristic paragraph gives the obstruction1,Xᵖ. These are related but distinct from the polynomial highest-degree statement. [Hermoso–Alcázar, arXiv2410.18867v1, §2 Proposition2 and its proof](https://arxiv.org/html/2410.18867v1) supplies the exact polynomial highest-degree calculation: product of leading coefficients, Vandermonde in degrees, and total degree minus the triangular number. Both use ordinary derivatives; the local `clean.tex` supplies Hasse normalization. The cast-separated positive-characteristic version below is a verified consequence of the integral determinant calculation, not a claim that these sources explicitly state the final Lean signature.

Concept: distinct-degree polynomial Wronskian nonvanishing. Sources agree on the characteristic-zero standard form; formal series, Laurent polynomials and general differential fields are adjacent theories with different degree/order or constant-field hypotheses. They do not license merely dropping `CharZero` while keeping natural-degree separation.

## Phase 4a–b — full parameter and generality analysis

| Parameter/hypothesis | Use and possible weakening | Verified conclusion |
|---|---|---|
| `K : Type*` | Coefficient carrier | Already universe-polymorphic. |
| `Field K` | Current Wronskian parent definition requires it; source quotient uses inverses | Same-parent weakening keeps it. Expanded determinant needs only `CommRing` and `IsDomain`, independently compiled. |
| `CharZero K` | Source uses nonzero factorial casts and injective natural casts | Can remove it when `hd` instead separates degree casts in K. |
| `{l : ℕ}` | Square size, ordered row degrees0,…,l−1 | Arbitrary including0. Arbitrary finite indexing requires an enumeration of row orders; arbitrary orders require a different binomial determinant premise. |
| `{φ : Fin l → K[X]}` | Nonconstant and constant polynomial family | No monicity, degree bounds, positivity, sortedness, or nonempty condition needed. |
| `hφ : ∀ ν, φ ν ≠ 0` | Nonzero leading coefficients | Cannot simply remove: size1 zero polynomial has zero determinant. Could replace by a stronger product/unit premise but that does not improve the domain theorem. |
| Natural-degree `hd` | Nonzero Vandermonde in characteristic zero | Replace combined `CharZero`+`hd` by scalar-cast injectivity. Repeated family1,1 shows separation cannot simply disappear. |

**Current form matches the cited characteristic-zero standard but is STRICTLY NARROWER than the verified characteristic-aware algebraic form**, with an actual compiled local weakening. Preferred same-parent signature:

```lean
theorem wronskian_ne_zero_of_natDegree_cast_injective
    {K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]}
    (hφ : ∀ ν, φ ν ≠ 0)
    (hd : Function.Injective fun ν ↦ ((φ ν).natDegree : K)) :
    Roth.wronskian φ ≠ 0
```

This changes only hypotheses at the existing parent interface. It does not demand changing the definitions across the project. The original follows by passing `Nat.cast_injective.comp hd`; the actual caller passes that composition to the replacement. [Same-parent recovery and full caller experiment](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/native-recovery-executed.lean.txt), [complete receipt](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/native-recovery-success.json).

A separately verified expanded representation works over every integral domain:

```lean
theorem hasseWronskian_ne_zero_of_natDegree_cast_injective
    {R : Type*} [CommRing R] [IsDomain R] {l : ℕ} {φ : Fin l → R[X]}
    (hφ : ∀ ν, φ ν ≠ 0)
    (hd : Function.Injective fun ν ↦ ((φ ν).natDegree : R)) :
    (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (μ : ℕ) (φ ν)).det ≠ 0
```

[Exact executed domain proof and guards](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/native-domain-executed.lean.txt), [complete success receipt](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/native-domain-success.json). Its new helpers compute the coefficient over a commutative ring and multiply the binomial determinant by the product of row factorials to obtain the Vandermonde product. If the binomial determinant were zero then the Vandermonde would be zero; no factorial cancellation, inverse or factorial-nonzero hypothesis is needed. The product of leading coefficients is nonzero in a domain. The same-parent Field result is a specialization through unfolding.

The positive characteristic2 family1,X verifies strict improvement. The characteristic2 family1,X² has distinct natural degrees but zero Wronskian, validating the guard against the false claim with no cast-separation condition. This cast condition is sufficient, not necessary for all Hasse Wronskians: higher Hasse rows can retain information when ordinary degree casts repeat. No iff or arbitrary-row theorem is claimed. An arbitrary ring with zero divisors needs product/non-zero-divisor hypotheses; merely nonzero leading coefficients and pairwise nonzero differences do not ensure their product is nonzero. This was natively verified over ℤ×ℤ: the family of monomials of degrees 0 and 1 with orthogonal idempotent leading coefficients (1,0) and (0,1) has nonzero members and injective degree casts, but zero determinant. [Exact ring guard](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/native-guards-executed.lean.txt), [complete receipt](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/native-guards-success.json). The domain theorem is the natural usable hierarchy level here; a regular-element API is a separate design option, not an unverified weakening.

The verified cost is moderate and localized: reuse the coefficient and cancellation-free binomial helpers. They are new proofs, not existing mathlib replacements. Extending the parent definition itself to domains remains a distinct representation decision; it is not required to substantiate this verdict.

## Phase 4c — all modern-idiom questions

| # | Question | Answer and concrete downstream consequence |
|---|---|---|
| 1 | Typeclass preambles | Standard `Field`, `CharZero` already used. Replace global characteristic by a finite-family value hypothesis; no new typeclass. |
| 2 | Filters/nets | No, finite polynomial algebra with no convergence. |
| 3 | Universal property | No object construction; determinant and Hasse operators already have canonical APIs. |
| 4 | Bundled substructures | No set-with-closure condition. Linear span would describe independence but does not prove this nonvanishing step. |
| 5 | Algebra hierarchy | Yes, same-parent cast-degree condition admits ZMod2 and expanded domain statement admits ℤ-polynomials without a fraction field. |
| 6 | Higher categories | No, determinant lines do not resolve the missing degree-coefficient calculation and bring no necessary downstream use here. |
| 7 | Concrete indices | Fin l orders derivative rows. Arbitrary finite columns can be reindexed; arbitrary derivative orders are generalized Wronskians with a different binomial minor. Keep these meanings separate. |
| 8 | Concrete-via-abstract diagnostic | The source proof has no direct `wronskian` occurrence after taking h0; it uses a coefficient identity, binomial normalization, product nonvanishing. Thus the generic nonzero-coefficient step is already abstract. Exact `Matrix.det_vandermonde_ne_zero_iff` is existing mathlib; the Hasse coefficient and binomial bridges are substantive new content, not definitional normalization. Do not contribute a duplicate generic Vandermonde theorem. |
| 9 | False-generalization guard | Cast separation preserves the same Hasse determinant; positive-char success/failure verified. Replacing it by natural-degree separation in positive characteristic is false. Changing Hasse to ordinary derivatives or arbitrary rows changes the problem and needs explicit normalization/premises. |

Modern-idiom verdict: a real characteristic-aware algebraic improvement is available. It serves finite-field polynomial computations and integral polynomial families. The named parent can stay fixed for the local weakening; any later public n-ary naming/API decision is coordinated separately.

## Phase 4.6 — all proof-strategy rows

| # | Strategy | Finding |
|---|---|---|
| 1 | ε–δ versus filters | n/a, no topology. |
| 2 | Elements versus ideal/submodule inclusions | No inclusion argument replaces a leading-term determinant computation; coefficient and determinant APIs are appropriate. |
| 3 | Sequences versus nets | n/a, finite algebra. |
| 4 | Construction versus universal property | n/a, no constructed object. |
| 5 | Helpers mathlib should have | N-ary Hasse determinant coefficient law and characteristic-aware binomial determinant bridge are the concrete missing helpers. Generic Vandermonde nonvanishing is already present. |

Current strategy: **REFACTOR-RECOMMENDED for generality**. Retain the leading-coefficient strategy but use the cancellation-free determinant identity and existing `Matrix.det_vandermonde_ne_zero_iff`, avoiding unnecessary inverse-factorial assumptions. New helper work is already demonstrated in the accepted isolated source. This is about mathematical hypotheses, not code-length taste or cost.

## Phase 4.5 — infrastructure risks

**n/a: theorem.** All six rows are explicitly n/a: typeclass diamond (no instance introduced), reducibility leak (no new data definition), noncanonical unfolding (no new definitional equality), instance-priority collision (no instance), universe issues (universe-polymorphic proposition, native checked), coercion ambiguity (no coercion path added; natural casts in the statement native checked). The separate parent-definition assessment owns those definitions' design risks.

## Phase 5 — five actual mathlib methods on three forms

Complete raw formal requests/responses: [current](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/formal-current.json), [literature](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/formal-literature.json), [abstract](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/formal-abstract.json). Exact pinned source searches, untruncated: [current](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/rg-current.json), [literature](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/rg-literature.json), [abstract](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/rg-abstract.json). Source/hash artifacts pin all positive candidates; external search indices may differ in revision.

| Method | Current form | Literature-standard form | Abstract form |
|---|---|---|---|
| Finder | Binary Wronskian degree bounds, coprime criterion | Same binary partial matches | Exact Vandermonde nonzero iff injective. |
| Loogle | `Polynomial.hasseDeriv, Matrix.det`: empty | `"wronskian"`: binary API | `Matrix.vandermonde, Ne`: exact iff and zero criterion. |
| LeanSearch | Binary Wronskian and coprime criterion | Binary degree/coeff lemmas | Exact Vandermonde nonvanishing and determinant formula. |
| rg | No n-ary nonvanishing law; all source results preserved | Binary Wronskian file and explicit n-tuple TODO | Vandermonde theorem233 and monic evaluation theorem280. |
| Local name | `wronskian`: project and binary results | `wronskian_ne`: project result, not a replacement | `det_vandermonde`: exact candidate; all three searches report `index=unavailable`. |

Index-unavailable and search failure do not prove absence. The root actually ran a mathlib-only `exact?` probe on the expanded goal before adding new helpers; it failed to close without timing out. [Exact attempted composition](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/native-composition-executed.lean.txt), [rejection receipt](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/native-composition-rejected.json). This is negative route evidence, not a proof that no possible proof term exists.

Pinned positive candidates: `Matrix.det_vandermonde_ne_zero_iff`, `Matrix.det_vandermonde`, `Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde`, `Polynomial.leadingCoeff_ne_zero`, Hasse coefficient arithmetic and determinant expansion. The abstract nonvanishing goal was closed by one existing call in an isolated compile: [source](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/native-abstract-executed.lean.txt), [receipt](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/native-abstract-success.json). It says nothing by itself about the Hasse matrix.

Mathlib's `Polynomial.wronskian` is binary; `IsCoprime.wronskian_eq_zero_iff` requires coprime inputs and characterizes simultaneous zero derivatives. It is not a family theorem or a distinct-degree criterion. The file explicitly says TODO: define n-tuple Wronskians. This is a concrete gap anchor, beyond search absence. The guessed `Polynomial.wronskian_ne_zero_iff` and `hasseDeriv_X_pow` names do not exist in the pinned source and are not cited as APIs. The private binomial conversion in Vandermonde cannot be cited as public API.

## Phase 5.5 — all statement-shape checks

Normal forms considered: named Hasse Wronskian nonzero; expanded Hasse determinant nonzero; one computed coefficient nonzero; degree equal to Σdegrees minus triangular number. The direct nonzero conclusion is exactly what the sole caller needs. Degree equality is stronger and belongs with a degree/leading-coefficient API; the generic coefficient-nonzero implication is existing elementary infrastructure. No ad hoc predicate equivalence or problematic RHS normal form occurs.

Syntactic-generality experiments: the domain expanded form, same-parent cast-injective form, original characteristic-zero recovery and full actual caller all compile. The original corollary is convenient for existing characteristic-zero callers; the cast-separated theorem is the preferred primary hypothesis form, without an unnecessary factorial premise.

Superfluous-argument audit: universe carrier, polynomial family and size remain genuine; hφ cannot simply disappear; separation cannot disappear; the global `CharZero` can be replaced by family-local cast separation; `Field` is needed by the unchanged parent signature but not the expanded theorem. Commutativity is needed by determinant; the domain premise justifies multiplication of nonzero factors. No positivity/nonempty/monicity condition should be added. **Overall: RESTATE-BEFORE-SHIP**, carrying the cast-separated signature into the next action. The expanded domain form is a useful additional target, not a misleading claim that the current Field parent has already changed.

## Phase 6.0 — actual callers and inline audit

Source-level explicit proof caller count 1, all inside the declaring module. Under the command's convention excluding that file, internal-use countK=0 and external-to-file files 0. The documentation occurrence is not a caller. These counts are not the opaque kernel/simp dependency closure.

| Actual caller | Usage and concrete future refactor |
|---|---|
| `Roth/Wronskian.lean:210`, `Roth.wronskian_ne_zero_of_linearIndependent` | Distinct-degree branch of strong induction: replace `wronskian_ne_zero_of_natDegree_injective h.ne_zero hinj` by the cast-separated theorem applied to `h.ne_zero` and `Nat.cast_injective.comp hinj`, or retain a CharZero corollary with the old signature. The full induction proof was rebuilt in the native caller experiment. |

[Exact caller/inline scan](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/rg-callers.json). No separate inline rederivation was found. The sole use is essential in the proof of the Wronskian criterion, so this is not dead code despite K=0 outside its file. Sparse usage motivates checking abstraction, but does not erase the standard mathematical theorem or turn project helpers into mathlib primitives.

## Phase 6 — composition experiments

The original is short only after calling `Roth.coeff_wronskian_of_natDegree_injective` and `Roth.det_choose_eq`. Both are project lemmas. The abstract Vandermonde theorem is genuinely one existing call, but the coefficient calculation and binomial conversion bridge are not mathlib replacements. The isolated exact? experiment on the unnormalized Hasse goal failed; the successful generalized proof contains both full new helper proofs. No ≤3-existing-call composition for the original was established. **NOT-COMPOSABLE from existing mathlib at the assessed level**, with the precise gap named rather than absence inferred from search failure.

The criterion `Roth.wronskian_ne_zero_of_linearIndependent` is downstream of this theorem and cannot be used as a replacement; that would be circular. An alternating-map nonvanishing theorem would require an actual nonvanishing/injectivity premise for this particular differential determinant, which is the point needing proof. No closing `simp [defs]` route from an existing Wronskian family theorem was found or claimed.

## Phase 7 — verdict and actionable upstream plan

**YES-but-generalise-first**, reason: **MODERN-IDIOM**, a verified local characteristic weakening with concrete finite-field applications. This is a standard reusable polynomial nonvanishing law, with applications beyond Roth's theorem documented in the literature. The upstream gap is explicitly named by mathlib's n-tuple-Wronskian TODO and the missing Hasse coefficient/binomial determinant bridges. Generic Vandermonde nonvanishing already exists and should be reused. A short source proof with two project mathematical helpers is not a ≤3-call mathlib wrapper.

Preferred upstream path: `Mathlib/RingTheory/Polynomial/Wronskian.lean`, extending its n-tuple TODO with a carefully named Hasse family API. Scalar binomial determinant normalization belongs separately in `Mathlib/LinearAlgebra/Vandermonde.lean`. Proposed PR title: **feat(Polynomial): nonvanishing of Hasse Wronskians with separated degree casts**. The primary local weakening can be implemented against the present Field parent; exposing the domain form needs the separately coordinated public family-definition choice. That foundational choice does not block the already verified local weakening and is not used to force a cost-based BORDERLINE verdict.

Group with the already accepted YES-generalise coefficient theorem `Roth.coeff_wronskian_of_natDegree_injective`, and coordinate with accepted YES-generalise `Roth.det_choose_eq` in the Vandermonde support PR. Their accepted statuses were read from current progress; the earlier BORDERLINE definitions are not called accepted YES material. Other accepted multivariate Hasse results can be separate PRs; there is no reason to force this into their scope.

Next actions:

1. `/generalise Roth.wronskian_ne_zero_of_natDegree_injective`: remove global CharZero in favor of cast-degree injectivity, use the cancellation-free binomial helper, keep the old characteristic-zero corollary if useful.
2. Coordinate n-ary Hasse naming and the optional domain parent extension with the coefficient theorem. Preserve the verified distinction from the binary ordinary Wronskian.
3. `/cleanup Roth/Wronskian.lean Roth.wronskian_ne_zero_of_natDegree_injective`; update the sole caller as above and run the relevant build/checks before a PR.
4. Reviewer candidates from actual relevant pinned history: Yaël Dillies (Vandermonde reorganization, commit a00728860c), Yury Kudryashov (Vandermonde golf,32a0a63fe2), Peter Nelson (Vandermonde exceptional rows,b8853be26e). Binary Wronskian authors Jineon Baek and Seewoo Lee are additional topic candidates identified from the source header, not invented recent commits. [Exact history receipt](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/reviewer-history.json).

Alternative local destination if a n-ary API proposal is deferred: retain in `Roth/Wronskian.lean` beside its coefficient lemma and essential induction caller. No declaration deletion is recommended at this stage. No production edit, PR submission, reviewer contact or parent-design resolution is performed by this read-only assessment.

## Phase 8 — completion and verification

All required phases, all nine modern-idiom questions, all five strategy rows, all three statement-shape checks, all named literature channels, all five actual mathlib search methods on three forms, every explicit caller and actual composition experiments are complete. Theorem-only infrastructure n/a reasons are explicit. Accepted exact sources and complete raw native receipts are linked in [verification.json](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/verification.json); rejected experiments remain separately labeled and are never treated as accepted proofs. Accepted sources contain no sorry, new axioms, unsafe, native_decide or raised limits, and native axiom reports use only propext, Classical.choice and Quot.sound.

The portable read-only validator checks current manifest hashes/bytes, all 17 baseline inputs, pinned mathlib sources, exact executed code where supplied, native success with no partial/error/warning, standard axioms, report links, required phase metadata and safe-web metadata. [Validator](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/validate.py), [credential guard receipt](../evidence/Roth.wronskian_ne_zero_of_natDegree_injective/secret-scan-receipt.json). Verification unresolved items: **[]**. Root acceptance is pending independent review; the worker has not published or changed the project.
