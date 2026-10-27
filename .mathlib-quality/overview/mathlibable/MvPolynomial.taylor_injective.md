# MvPolynomial.taylor_injective — full mathlibable assessment

**BORDERLINE-needs-human**. Canonical declaration 71/293. The translation substitution is injective because the opposite translation is a left inverse. Generic left-inverse injectivity already exists; the required multivariate inverse law is project mathematics, independently reconstructed in the raw experiment. Whether a separately named injectivity corollary merits inclusion, or should be exposed through a bundled translation equivalence, is an upstream API question. No production source changes are proposed in this assessment.

## Phase 0 — Doctor and source integrity

The accepted baseline is commit 99f19fda4b3cbee38fc0d31af76075834f5cc265, clean full build of 2467 jobs. [Baseline](../evidence/MvPolynomial.taylor_injective/baseline-build.txt), [fresh 17 source/pin hash checks](../evidence/MvPolynomial.taylor_injective/inputs.json), [check summary](../evidence/MvPolynomial.taylor_injective/input-hash-check.json). All hashes match; Lean v4.34.0 and mathlib revision 5ed2965256430c3649e86755f9576b54eca72435 remain unchanged. The theorem resolves at Roth/Taylor.lean:187–188, has no sorry and no simp attribute. [Canonical metadata](../evidence/MvPolynomial.taylor_injective/canonical-entry.json), [complete declaring module](../evidence/MvPolynomial.taylor_injective/Taylor-module.lean.txt). The module develops multivariate translation, its Hasse-derivative coefficients, and bounded Taylor expansion. The full original declaration, fresh proof, actual caller and raw experiments all elaborate cleanly; no partial response is treated as success.

## Phase 1 — Mathematical comprehension

For any commutative coefficient ring A, arbitrary set of variables σ and coefficient vector α, the substitution taking each variable X_j to X_j+α_j is injective on formal polynomials. Consequently, two polynomials with the same translate are equal. Applying substitution X_j↦X_j−α_j to an equality of translated polynomials recovers the original equality. This is a statement about formal polynomials, not injectivity of evaluation at coefficient-valued points.

Full native type:
```lean
∀ {σ : Type u_1} {A : Type u_2} [CommRing A] (α : σ → A),
  Function.Injective (MvPolynomial.taylor α : MvPolynomial σ A → MvPolynomial σ A)
```
The variables and coefficient type occupy independent universes. There is no finiteness, decidable equality, nonemptiness, field, domain, characteristic or nontriviality assumption. The only value parameter is the complete shift vector. The body is exactly `Function.LeftInverse.injective (taylor_neg_taylor α)`: its first fact is generic existing logic, while its second is the project inverse-translation result. [Original type/body, replay and axioms](../evidence/MvPolynomial.taylor_injective/native-target-success.json).

## Phase 2 — Preliminary checks

**SMALL:** an elementary injectivity corollary, not a main named theorem or new structure. Literature breadth remains exhaustive. The one-line *definition* test is **n/a**, since this is a theorem; its short proof does not invoke definition exemptions or automatically establish an all-mathlib composition. The parent translation and inverse-law BORDERLINE verdicts are not inherited: the present searches, caller and composition checks are independent.

## Phase 3 — Exhaustive literature protocol

Each named channel was actually checked. Full returned article/search bodies are not archived: exact requests, response SHA256/byte counts and safe locators are retained with concise original summaries.

| Channel | Actual query or access | Result and limitations |
|---|---|---|
| General web, current form | `multivariate polynomial translation P(X+a) injective automorphism ring` | Found polynomial automorphism and free-algebra contexts; no separately named arbitrary-ring injectivity theorem. [Exact request/metadata](../evidence/MvPolynomial.taylor_injective/web-specific.json). |
| General web, broad form | `free commutative algebra substitution translation additive inverse injective` | Free commutative algebra on arbitrary generators is the appropriate universal-property anchor. The inverse shift is a direct mathematical inference from that framework, not a quotation of a theorem with our exact signature. [Metadata](../evidence/MvPolynomial.taylor_injective/web-specific.json). |
| General web, aliases | `shift automorphism polynomial algebra translations inverse substitution` | Shift/translation automorphism terminology; unrelated dynamical substitution shifts and multivariate skew rings also returned and are not accepted as the exact result. [Metadata](../evidence/MvPolynomial.taylor_injective/web-specific.json). |
| Optional ask_chatgpt_math | n/a | Tool unavailable; optional absence does not reduce other channels. |
| Local references | `Taylor`, `P_\\alpha`, variable-shift forms in clean.tex | §4 Index lines500–548 discusses finite real-coordinate Taylor expansion and recovering the original polynomial by translating back. Context supports the elementary injectivity corollary; does not constrain us to ℝ or finitely many variables. [Search](../evidence/MvPolynomial.taylor_injective/rg-local-literature.json), [excerpts](../evidence/MvPolynomial.taylor_injective/clean-excerpts.tex.txt), [hash/locator](../evidence/MvPolynomial.taylor_injective/local-literature.json). |
| nLab | `site:nlab.org polynomial algebra free commutative algebra`; direct nLab polynomial page | First query had no direct nlab.org hit; corrected platform `site:ncatlab.org/nlab/show/free+commutative+algebra polynomial` found the polynomial page. Definitions describe arbitrary-generator free commutative algebra. Directopen returned unsupported application/xhtml+xml; search content, primary Bergman and native proofs control claims. [Channels](../evidence/MvPolynomial.taylor_injective/web-channels.json), [primary request](../evidence/MvPolynomial.taylor_injective/web-primary.json), [access failure](../evidence/MvPolynomial.taylor_injective/web-locators.json). |
| nCatLab | `site:ncatlab.org polynomial algebra translation automorphism monomorphism split` | Split monomorphism page supplies retraction/mono formulation; search accessible, directopen unsupported content type. This is the same nLab platform, a separate categorical formulation rather than an invented independent source. No higher-category generalization needed. [Search](../evidence/MvPolynomial.taylor_injective/web-channels.json), [access](../evidence/MvPolynomial.taylor_injective/web-primary.json). |
| Stacks | `site:stacks.math.columbia.edu polynomial automorphism x_i c_i translation`; direct Tag051P | Lemma10.115.6 proof uses triangular polynomial variable-shift automorphisms. Contextual primary example, not exact arbitrary-ring constant-translation injectivity theorem. [Search](../evidence/MvPolynomial.taylor_injective/web-channels.json), [access](../evidence/MvPolynomial.taylor_injective/web-primary.json). |
| MathOverflow | `site:mathoverflow.net polynomial translations automorphism group`; question269602 | Johannes Hahn's 12Mar2020 comment explicitly notes a coordinate constant-shift automorphism for every scalar. Discussion corroborates standard terminology; it is not the primary proof anchor. [Search](../evidence/MvPolynomial.taylor_injective/web-channels.json), [exact locator](../evidence/MvPolynomial.taylor_injective/web-locators.json). |
| Recent arXiv, last5years | `site:arxiv.org translation subgroup polynomial automorphism 2022 2023 2024 2025 2026`; follow-up2412.09519 | Broad search returned unrelated outer-automorphism growth and old papers, not exact matches. Follow-up to relevant polynomial-translation context: Montagard–Pan–Rittatore, submitted12Dec2024, revised21Aug2025, within2021-10-27–2026-10-27. Abstract studies translation subgroups in derivation centralizers over algebraically closed characteristic-zero fields; contemporary context only. [Requests/date/locator](../evidence/MvPolynomial.taylor_injective/web-primary.json), [follow-up](../evidence/MvPolynomial.taylor_injective/web-locators.json). |

Primary anchor: [Bergman, An Invitation to General Algebra and Universal Constructions, §4.12, printed pp83–89](https://math.berkeley.edu/~gbergman/245/3.4.pdf), including free-ring and free-commutative-ring construction after Lemma4.12.1, specifically printed p88. This is an absolute free-ring context; extension to fixed coefficient rings and constant shifts is our inference, checked natively. [Exact primary detail access](../evidence/MvPolynomial.taylor_injective/web-primary-details.json). Images of generators determine substitutions; opposite shifts yield inverse homomorphisms and hence injectivity. This implication is our inference. [Stacks051P](https://stacks.math.columbia.edu/tag/051P) illustrates shift automorphisms in an actual proof. [Recent primary abstract](https://arxiv.org/abs/2412.09519) verifies dates and narrower research context, not the exact Lean statement.

Concepts identified: translation/shift substitution, polynomial automorphism, left inverse, split monomorphism. Coordinate and free-algebra descriptions agree mathematically, while packaging differs. The most general abstract implication is that a function between arbitrary sorts with a left inverse is injective. That abstract implication already exists. Its specialization to constant polynomial shifts still requires the verified inverse-substitution premise. No precise historical origin is claimed. Formal-polynomial equality and coefficient-valued polynomial functions must not be conflated.

## Phase 4a–4b — Parameters and generality

| Parameter/hypothesis | Assessment and tested conclusion |
|---|---|
| σ : Type u | Arbitrary variables, independent universe; no finite/nonempty instance to remove. |
| A : Type v | Arbitrary coefficient ring including positive characteristic, zero divisors and the trivial ring. No field/domain restriction. |
| CommRing A | Supplies fixed parent CommSemiring interface plus negation and cancellation for the current inverse proof. A CommSemiring-only application of the original theorem fails as expected. More decisively, arbitrary CommSemiring translation injectivity is false: native WithTop ℕ counterexample below. This does not prove CommRing is a mathematically minimal class among all cancellative-semiring alternatives. |
| α : σ → A | Any shift, including zero; no positivity/nonvanishing/invertibility of coefficients needed. Essential value parameter. |
| Injective conclusion | Quantifies every pair of polynomials; no bounded degree or finite support restriction beyond being formal polynomials. |

**MAXIMALLY GENERAL for the unchanged inverse-based signature among verified mechanical weakenings; zero verified hypothesis drops.** This is not a universal minimality assertion. The raw proof verifies a separate conditional CommSemiring law: if β_j+α_j=0 for every j, translation by α is injective. That is an explicitly inverse-pair-based restatement, adding a new value parameter/premise and changing the proof interface; not simply deleting CommRing. The generic law `LeftInverse g f → Injective f` removes polynomial structure entirely, but assumes the essential mathematical inverse witness and already exists in core.

The blanket semiring weakening is actually refuted: take coefficient semiring WithTop ℕ, one variable, shift α=⊤, P=X+C1 and Q=X+C2. The shifts coincide because ⊤+1=⊤+2=⊤. P and Q are distinct: evaluating at zero would give 1=2. The native raw proof establishes `topCollision` and `topNotInjective`; no untested assertion or mere interface failure substitutes for the counterexample. Cancellative semiring versions may be valid by a different argument, but have not been verified and are not advertised as accepted weakenings. [Exact raw proof](../evidence/MvPolynomial.taylor_injective/native-raw-executed.lean.txt), [success](../evidence/MvPolynomial.taylor_injective/native-raw-success.json).

## Phase 4c — All nine modern-idiom checks

| # | Question | Finding and downstream consequence |
|---|---|---|
| 1 | Typeclass versus ad-hoc preamble | Already CommRing; no custom axiom predicate to replace. |
| 2 | Sequences/metrics versus filters | No topology or convergence; n/a. |
| 3 | Construction versus universal property | Translation is a free-algebra substitution via aeval. Its inverse is computed on generators; the universal-property route avoids coefficient induction. |
| 4 | Bundled substructure | A newly constructed translation AlgEquiv makes injectivity a generic `.injective` consequence and also exposes surjectivity/inverse transport. The bundle requires new inverse proofs, so is not an already available mathlib replacement. Actual scratch specialization compiled. |
| 5 | Field versus weaker hierarchy | Already CommRing, not field; explicit inverse-pair formulation extends to suitable semiring shifts. Arbitrary CommSemiring claim is false, as verified. No verified cancellative-semiring weakening claimed. |
| 6 | Higher-category form | Ordinary functions/algebra equivalences suffice. No coherence problem warrants a higher-category reformulation. |
| 7 | Concrete numerical index | σ already arbitrary; no ℕ/ℤ/ℝ index to generalize. |
| 8 | Concrete-via-abstract | Yes: the body contains no literal taylor call and mentions only the target-specific inverse lemma. The actual generic content is LeftInverse.injective, already present. Replacing the concrete result with that generic lemma requires supplying the nontrivial shift inverse; the abstraction is not a new contribution. [Diagnostic](../evidence/MvPolynomial.taylor_injective/proof-body-diagnostic.json). |
| 9 | False-generalization guard | Keep polynomial substitution, not pointwise evaluation; arbitrary coefficient-semiring shifts can fail injectivity. Conditional inverse pairs preserve content but require a real premise. A new equivalence's `.injective` cannot be used circularly as evidence the equivalence was already available. |

Modern packaging is useful: verified new algebra equivalence allows the actual zero-iff caller to derive injectivity generically. Whether to expose a named concrete corollary alongside the bundle is an API choice. No YES-generalise-first verdict is inferred just from replacing an already-existing generic implication. [Native target/bundle specialization](../evidence/MvPolynomial.taylor_injective/native-target-executed.lean.txt), [inverse prerequisite source](../evidence/MvPolynomial.taylor_injective/prerequisite-inverse-extra.lean.txt).

## Phase 4.5 — All six infrastructure risks

Theorem-only n/a: (1) typeclass diamonds, (2) reducibility leakage, (3) noncanonical data unfolding, (4) instance priorities/search, (5) new structure-field universe restrictions, (6) coercion ambiguity. No data, instance or simp rule is installed. Native full type confirms independent universes. Optional scratch equivalence is a tested representation experiment, not silently accepted new production infrastructure.

## Phase 4.6 — All five proof-strategy checks

| # | Strategy diagnostic | Finding |
|---|---|---|
| 1 | ε–δ versus filters | Not analysis; n/a. |
| 2 | Elements versus subobject inclusions | No ideal/submodule lattice argument; abstract function injectivity is already point-free. |
| 3 | Sequences versus nets | No convergence; n/a. |
| 4 | Construction versus universal property | Free-algebra inverse substitution is a suitable justification; current final step uses generic retraction injectivity. |
| 5 | Missing helper API | No missing generic left-inverse/injectivity theorem. Possible missing bundle is multivariate translation AlgEquiv; its inverse fields are separately verified obligations. |

Strategy **MATHLIB-IDIOMATIC**: applying LeftInverse.injective is already the right short argument. A bundle changes API organization and also supplies surjectivity; no coefficient induction or subtraction of polynomial coefficients is needed. Cost does not determine the verdict.

## Phase 5 — Five actual methods × three forms

[Exact formal requests and complete responses](../evidence/MvPolynomial.taylor_injective/formal-search.json). External indexes can differ from the pinned snapshot; native positive probes and pinned source determine supported claims.

| Method | Current Function.Injective(MvPolynomial.taylor α) | Literature polynomial translation automorphism | Abstract left inverse implies injective |
|---|---|---|---|
| Finder | Polynomial.taylor_injective/taylor_inj; MvPolynomial.expand_injective is exponent substitution, not translation. | Polynomial.algEquivAevalXAddC, taylorEquiv; all univariate bundles. | Set.LeftInvOn.injOn, Function.injective_iff_hasLeftInverse and generic retraction results. |
| LeanSearch | Polynomial.taylor_injective/taylor_inj; coefficient/power-series embeddings unrelated to shift. | Univariate shift/affine algebra equivalences. | Function.injective_iff_hasLeftInverse, existence-of-inverse and restricted LeftInvOn variants. |
| Loogle | `Polynomial.taylor, Function.Injective` gives univariate theorem. | `Polynomial.taylorEquiv` gives univariate bundle. | `Function.LeftInverse, Function.Injective` gives exact generic implication. |
| Pinned rg | [Current searches](../evidence/MvPolynomial.taylor_injective/rg-current.json) | [Literature names](../evidence/MvPolynomial.taylor_injective/rg-literature.json) | [Substitution/inverse routes](../evidence/MvPolynomial.taylor_injective/rg-abstract.json), [algebraic independence route](../evidence/MvPolynomial.taylor_injective/rg-independent.json). |
| local search | `taylor_injective` finds own target and Polynomial version. | `taylorEquiv` finds Polynomial bundle. | `LeftInverse.injective` finds core function theorem. All index=unavailable; positive source results usable, empty indexed absence never inferred. |

The untruncated [full-name search](../evidence/MvPolynomial.taylor_injective/rg-full-name.json) finds the univariate theorem, not an exact multivariate counterpart. `Polynomial.taylor_injective` at Taylor130 works over Ring, rather than CommRing, on **univariate** polynomials; native exact application succeeds. It is an analogy, not a direct arbitrary-variable replacement. `Function.LeftInverse.injective` in [core Function source](../evidence/MvPolynomial.taylor_injective/Function-module.lean.txt) works for arbitrary sorts and is verified/printed natively. Its hypothesis is essential. Generic `injective_iff_map_eq_zero'` offers a kernel route but requires the target-specific zero-reflection law; the existing project zero-iff is downstream, so using it to prove this injectivity would be circular.

Additional abstract route: `algebraicIndependent_iff_injective_aeval` and `MvPolynomial.algebraicIndependent_X` exist in [Defs](../evidence/MvPolynomial.taylor_injective/AlgebraicIndependent-Defs.lean.txt) and [Basic](../evidence/MvPolynomial.taylor_injective/AlgebraicIndependent-Basic.lean.txt). One would still need algebraic independence of X_j+Cα_j; merely knowing independence of X_j or the equivalence defining independence does not discharge that premise. No translated-independence preservation candidate was found by the explicit searches. This is a missing-premise analysis, not a source-only proof of global absence.

Mode-B re-aim rule does not force a NO here: parent taylor is BORDERLINE, not a NO-parent replaced by a more general existing mathlib object. This is not rfl glue. No generic typeclass magically supplies an injective arbitrary AlgHom; the verified semiring counterexample rules that claim out.

## Phase 5.5 — All three statement-shape checks

**Normal form:** Function.Injective on the shift is the standard canonical interface. The pointwise equivalent `taylor α P = taylor α Q ↔ P=Q` follows generically via `.eq_iff`; zero-reflection follows via `.eq_iff' (map_zero _)`. This respects the usual original-polynomial equality on the right. **Syntactic generality:** α remains explicit, variable and coefficient types implicit; Function.Injective directly serves the actual zero-iff caller. A bundled equivalence is an alternative primary object, not an alternative equality normal form. **Superfluous arguments:** σ,A and CommRing provide the parent polynomial/shift plus inverse interface, α specifies the substitution; none mechanically removable. No extraneous Fintype/DecidableEq/Nontrivial/CharZero assumptions. Bare commutative semiring widening fails mathematically, not merely by elaboration. **SHIP-AS-STATED** relative to present API; future bundle/corollary policy is separate.

## Phase 6.0 — Explicit caller and inline audit

Exactly **one explicit named caller**, zero outside the declaring file: `MvPolynomial.taylor_eq_zero_iff` at Taylor193. [Token search](../evidence/MvPolynomial.taylor_injective/rg-callers.json), [caller inventory](../evidence/MvPolynomial.taylor_injective/callers.json), [inline audit](../evidence/MvPolynomial.taylor_injective/rg-inline.json). It calls `(taylor_injective α).eq_iff' (map_zero _)` to reflect zero through translation. Full actual proof compiles with fresh replay instead of the original theorem. Inlining plan: replace it with `(Function.LeftInverse.injective (taylor_neg_taylor α)).eq_iff' (map_zero _)`, or, after an independently constructed translation equivalence, use that equivalence's injectivity. If the inverse API is also removed, include the independently checked substitution-inverse argument rather than pretending only a generic function fact is needed.

The Index uses of zero-iff are transitive consumers, not additional explicit injectivity callers. Source token results are not an exhaustive opaque kernel/simp dependency closure. The target has no simp attribute; no independent inline derivation of the same injectivity was found. Live zero-reflection use rules out declaring it dead code from its small body. [Full Index module](../evidence/MvPolynomial.taylor_injective/Index-module.lean.txt).

## Phase 6 — Actual composition and verification

1. Original-shaped fresh replay applies `Function.LeftInverse.injective (taylor_neg_taylor α)` and compiles. Direct proof-constant audit excludes the original taylor_injective theorem. This is **one generic existing fact plus one project inverse fact**, not one all-mathlib call.
2. A second fresh injectivity proof uses the separately replayed inverse source rather than the original inverse theorem. The inverse replay and new bundle prerequisite sources are archived, and the target receipt includes successful elaboration/axioms for them. A third proof uses the verified **new** equivalence's `.injective`. The bundle is not already in mathlib.
3. Raw mathlib-only snippet guards both missing project inverse and missing injectivity target, defines shift by aeval, and independently proves the generator-level conditional inverse. That proof uses comp_aeval_apply, map_add, aeval_X, algHom_C, additive association, C/map addition, the cancellation premise, map_zero, add_zero and aeval_X_left_apply, plus structural congruence. It exceeds three mathematical building blocks. Ring injectivity then uses LeftInverse.injective on the new inverse; conditional semiring injectivity uses it on the inverse-pair proof. Counting the newly proved inverse as one *existing* mathlib fact would be invalid.
4. The raw inverse also closes with `by simp [shift, comp_aeval_apply, add_assoc, aeval_X_left_apply]`; adding the generic injectivity step yields a short tactic proof whose real premise normalization is independently exhibited. Phase6b's closing-simp/API-design issue therefore persists after the final generic step; this is independent evidence, not merely inheriting the inverse theorem's verdict.
5. The generic theorem accepting an explicit LeftInverse premise compiles in one call; it proves exactly the existing abstract implication and does **not** establish unconditional shift injectivity without that premise. Positive univariate Polynomial.taylor_injective exact use compiles; arbitrary-variable transport is not definitional.
6. The actual zero-iff caller compiles in full, expanded `aeval(X+Cα)` spelling is definitionally the same shift, the old CommSemiring-only interface guard fails as expected, and actual WithTop ℕ collision/noninjectivity compiles. This is stronger evidence against the blanket weakening than an elaboration guard alone.

[Target source](../evidence/MvPolynomial.taylor_injective/native-target-executed.lean.txt), [target receipt](../evidence/MvPolynomial.taylor_injective/native-target-success.json), [raw source](../evidence/MvPolynomial.taylor_injective/native-raw-executed.lean.txt), [raw receipt](../evidence/MvPolynomial.taylor_injective/native-raw-success.json), [extra source](../evidence/MvPolynomial.taylor_injective/native-extra-executed.lean.txt), [extra receipt](../evidence/MvPolynomial.taylor_injective/native-extra-success.json).

All three accepted native runs are complete, success=true, partial=false, no failed dependencies/errors/warnings, standard axioms only (propext, Classical.choice, Quot.sound). No sorry/admit/new axioms/unsafe/native_decide or raised resource limits. Two preparation failures are retained separately: raw constant-map normalization needed algebraMap_eq, extra expanded aeval needed explicit coefficient ring R:=A. They are not accepted successes. [Rejected raw source](../evidence/MvPolynomial.taylor_injective/native-raw-rejected.lean.txt), [receipt](../evidence/MvPolynomial.taylor_injective/native-raw-rejected.json), [rejected extra source](../evidence/MvPolynomial.taylor_injective/native-extra-rejected.lean.txt), [receipt](../evidence/MvPolynomial.taylor_injective/native-extra-rejected.json). [Verification inventory](../evidence/MvPolynomial.taylor_injective/verification.json).

## Phase 7 — Actionable verdict and gate

**BORDERLINE-needs-human**.** Existing generic retraction injectivity and univariate translation injectivity are verified, but neither gives the arbitrary-variable shift inverse for free. The independently reconstructed inverse can close by simp; the concrete injectivity corollary's separate upstream status depends on translation API organization. Not NO-mathlib-has-it: univariate Polynomial and multivariate formal polynomial types differ, and the generic abstract premise must still be proved. Not NO-composable merely because the final line has two identifiers: one is a project result with substantive generator-normalization prerequisites. Not YES-generalise-first: no mechanical hypothesis removal is verified, and generalization to arbitrary functions with a left inverse is already in core. The conditional semiring theorem is genuine positive evidence but a changed signature; unrestricted semiring claim is false. No cost-based downgrade is made.

Future upstream questions, all answerable briefly:

1. Should a named multivariate translation API export a separate injectivity theorem, matching Polynomial.taylor_injective, even if a bundled equivalence already supplies it?
2. Should the primary ring-level translation object be a new AlgEquiv, with this theorem and zero-reflection derived from its generic API?
3. Should an explicit inverse-pair semiring variant be exposed, or should that conditional behavior remain covered by generic LeftInverse.injective and substitution laws?

Recommendation: retain the current theorem in Roth/Taylor.lean during this read-only survey. Resolve the bundle/corollary choices in one coherent future multivariate translation proposal; no new generic injectivity theorem is needed. If the concrete corollary is declined, inline the tested LeftInverse.injective term at Taylor193, preserving the inverse premise and validating dependents. Archive/ or another satellite library offers no benefit for this elementary interface. No source edits, PRs or outside communication are performed. These are future API choices, not unfinished verification: unresolved=[] and no user response is required to publish this completed assessment.

Gate: all named literature channels, every parameter and nine modern rows, six theorem-only infrastructure exclusions, five strategy rows, actual five-method/three-form searches, three shape checks, full actual caller replay, independent raw composition and the real semiring counterexample are complete. No incomplete assessment is marked complete.

## Phase 8 — Evidence and handoff

[Assessment](../evidence/MvPolynomial.taylor_injective/assessment.json), [overview entry](../evidence/MvPolynomial.taylor_injective/overview-entry.json), [current artifact manifest](../evidence/MvPolynomial.taylor_injective/copy-manifest.json), [portable read-only validator](../evidence/MvPolynomial.taylor_injective/validate.py). All evidence is intended for Git tracking after root acceptance; root alone updates overview/progress, commits and pushes. Current root acceptance is pending independent review. No intermediate Git checkpoint is requested.
