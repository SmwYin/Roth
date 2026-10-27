# MvPolynomial.taylor_zero — full mathlibable assessment

**NO-composable-from-mathlib**. The exact old spelling has an independently verified term using three existing mathematical facts: `map_zero` for `MvPolynomial.C`, `add_zero`, and `MvPolynomial.aeval_X_left_apply`. Equality transport is explicit. This is not an inheritance from the parent assessment and is not a verdict based only on the source's closing `simp`.

## Phase 0 — Doctor

Canonical 66, public simp theorem, `Roth/Taylor.lean:152–153`. The shared baseline `lake build` completed 2467 jobs with exit 0. Freshly recomputed hashes match all 17 source/pin entries. The target resolves and its exact proof and axioms are checked by the root's complete native receipt. The module develops multivariate polynomial translation and coefficient and finite-box Taylor formulas.

Evidence: [baseline](../evidence/MvPolynomial.taylor_zero/baseline-build.txt), [fresh inputs](../evidence/MvPolynomial.taylor_zero/inputs.json), [hash check](../evidence/MvPolynomial.taylor_zero/input-hash-check.json), [canonical entry](../evidence/MvPolynomial.taylor_zero/canonical-entry.json), [full module](../evidence/MvPolynomial.taylor_zero/Taylor-module.lean.txt), [native target](../evidence/MvPolynomial.taylor_zero/native-target-success.json).

## Phase 1 — Comprehend

For any polynomial P in an arbitrary collection of variables over a commutative semiring, translation by the all-zero vector fixes P. Every substituted generator is Xj+C(0)=Xj, and substitution of the original generators is the identity. No Taylor coefficient formula or derivative theorem is needed.

Full native statement (universe names are immaterial):

```lean
∀ {σ : Type u_3} {R : Type u_4} [CommSemiring R]
  (P : MvPolynomial σ R), (MvPolynomial.taylor fun x ↦ 0) P = P
```

σ indexes variables, R supplies coefficients and zero, and P is arbitrary. The only class assumption is CommSemiring R; there are no finite-variable, decidable-equality, nonempty, nonzero, field, or characteristic assumptions. The sole project definition in the statement/body is `MvPolynomial.taylor`. The proof's mathematical content is the existing identity evaluation law after two elementary normalization facts.

## Phase 2 — Preliminary checks

SMALL: the neutral-translation helper, not the full named Taylor theorem or a main module result. Exhaustive literature width remains mandatory. Phase 2b is n/a: theorem rather than a one-line data definition. Its one tactic line is recorded as proof shape, not as a definition exemption.

## Phase 3 — Exhaustive literature

All named channels were actually queried. Web metadata records exact query batches or URLs, SHA256 and byte count of the serialized returned tool response, status, locators and concise original summaries; no search-result or article bodies are archived. Source summaries below distinguish an exact law from broader context.

| Channel | Exact query or locator | Result |
|---|---|---|
| General web specific | `multivariate polynomial translation zero identity P(X+0)` | No independently named multivariate zero theorem established. Substitution context found. [batch](../evidence/MvPolynomial.taylor_zero/web0-metadata.json) |
| General web general | `polynomial ring universal property substitution variables identity commutative ring` | Bergman §4.12, printed p.85/PDF p.92: polynomial algebra is free commutative algebra on a set; substitution is its universal map. Zero translation follows by identity assignment, an inference. [batch](../evidence/MvPolynomial.taylor_zero/web0-metadata.json), [primary](../evidence/MvPolynomial.taylor_zero/webfollow-metadata.json), [locator](../evidence/MvPolynomial.taylor_zero/weblocator-metadata.json) |
| General web aliases | `Hasse Schmidt Taylor homomorphism translation zero polynomial` | Taylor/Hasse–Schmidt language gives broader formal substitution context; does not establish a separate name for this neutral law. [batch](../evidence/MvPolynomial.taylor_zero/web0-metadata.json) |
| ChatGPT math | Standard formulation, generality, historical evolution | n/a: ask_chatgpt_math unavailable. No substitute opinion claimed. |
| Local references | `clean.tex`, §4 Index, lines 500–557 | Defines Pα(X)=P(X+α); finite real-polynomial Taylor expansion. Zero specialization immediate, not separately named. [record](../evidence/MvPolynomial.taylor_zero/local-literature.json), [excerpt](../evidence/MvPolynomial.taylor_zero/clean-Taylor-excerpt.tex.txt) |
| nLab | `site:ncatlab.org/nlab polynomial algebra universal property` | Polynomial/free algebra entry provides universal-property context. Direct article open failed: unsupported application/xhtml+xml. Search text was accessible; no successful direct fetch claimed. [search](../evidence/MvPolynomial.taylor_zero/web0-metadata.json), [access](../evidence/MvPolynomial.taylor_zero/webprimary-metadata.json) |
| nCatLab | `site:ncatlab.org polynomial algebra free commutative algebra` | Same site's polynomial article discusses substitution and free commutative algebra. No higher-categorical zero-translation law established. [search](../evidence/MvPolynomial.taylor_zero/web4-metadata.json) |
| Stacks | `site:stacks.math.columbia.edu polynomial algebra universal property` | Search led to 07H4, divided-power polynomial algebra: different object and mapping property, not exact target. Initial opened 00F2 concerns finite presentations, also not exact. Both recorded honestly. [search](../evidence/MvPolynomial.taylor_zero/web4-metadata.json), [initial](../evidence/MvPolynomial.taylor_zero/webprimary-metadata.json), [07H4](../evidence/MvPolynomial.taylor_zero/webfollow-metadata.json) |
| MathOverflow | `site:mathoverflow.net Hasse Schmidt derivation Taylor homomorphism` | Question 71664 concerns formal vector-field integration and Hasse–Schmidt derivations in positive characteristic. Context only; no exact neutral-polynomial theorem inferred. [search](../evidence/MvPolynomial.taylor_zero/web4-metadata.json), [access](../evidence/MvPolynomial.taylor_zero/webprimary-metadata.json) |
| Recent arXiv | `site:arxiv.org Hasse Schmidt derivation Taylor homomorphism 2022 2023 2024 2025 2026` | 2605.20664, submitted 2026-05-20, *n-trivial extensions and multi Hasse-Schmidt derivations*, lies within 2021-10-27–2026-10-27. Abstract confirms broader derivation/generalization topic, not exact zero-translation statement. Results 1110.6108, 2007.14171 and 1810.08075 are outside the window and not counted as recent. [search](../evidence/MvPolynomial.taylor_zero/web4-metadata.json), [date/access](../evidence/MvPolynomial.taylor_zero/webprimary-metadata.json) |

Primary source anchor: [Bergman, An Invitation to General Algebra and Universal Constructions, §4.12](https://math.berkeley.edu/~gbergman/245/3.4.pdf). It treats arbitrary generator sets and free commutative algebras, supporting the universal substitution interpretation. Supplementary primary [Conrad, Universal Identities, Theorem 2.1 and Remark 2.4](https://kconrad.math.uconn.edu/blurbs/linmultialg/univid.pdf) describes multivariable substitution as a homomorphism and the obstruction from noncommuting images.

Literature summary: neutral translation / identity substitution is the standard concept, not a separate analytic Taylor theorem. Finite real-coordinate wording is one presentation; free commutative algebra gives arbitrary variables/coefficient rings. The Lean formulation already allows semirings because no subtraction or division is used. Historical terminology varies between substitution/universal properties and formal Taylor/Hasse–Schmidt language; the searches do not justify a precise historical attribution or a claim that all formal-group laws coincide. No disagreement with the mathematical content was found.

## Phase 4a–4b — Generality and all parameters

| Parameter | Necessity and generality |
|---|---|
| σ : Type u | Arbitrary independent universe; no finiteness, nonemptiness or DecidableEq required. Empty/infinite variable types included. |
| R : Type v | Arbitrary independent coefficient universe, not restricted to ℝ/fields. |
| CommSemiring R | Required by fixed taylor/MvPolynomial algebra-evaluation interface. Semiring-only application is explicitly rejected by a guarded native check. This is an interface floor, not a mathematical claim that noncommutative polynomial identities are impossible. |
| P : MvPolynomial σ R | Every polynomial, including zero; cannot drop the object being fixed. |
| all-zero vector | Essential identity parameter of this law. A general nonzero translation fixes neither each generator nor every polynomial. No weakening to arbitrary α asserted. |

Within unchanged parent interface: MAXIMALLY GENERAL, zero verified mechanical hypothesis drops. The broader reformulation uses arbitrary assignment g into a commutative R-algebra A: adding algebraMap(0) to every g j leaves evaluation unchanged. This is a compiled representation extension using map_zero/add_zero and congruence, not a newly discovered upstream theorem or a class weakening of taylor. The actual identity-substitution law already exists as aeval_X_left_apply; bundled identity exists as aeval_X_left. No cost-based verdict.

[Raw experiments](../evidence/MvPolynomial.taylor_zero/native-raw-executed.lean.txt), [receipt](../evidence/MvPolynomial.taylor_zero/native-raw-success.json).

## Phase 4c — All nine modern-idiom rows

| # | Question | Answer, form and downstream consequence |
|---|---|---|
| 1 | Typeclass preambles | Already CommSemiring, no ad-hoc structural predicate. |
| 2 | Sequences versus filters | No topology or limit argument. |
| 3 | Universal property | Yes: aeval_X_left/aeval_X_left_apply encode the free-algebra identity assignment. Removes dependence on translation name and interoperates with substitution composition. Existing API, not a new contribution. |
| 4 | Bundled substructure | Already an AlgHom; no set-with-closure predicate. Bundled equality to AlgHom.id is a useful equivalent shape, verified. |
| 5 | Field versus semiring hierarchy | Already semiring; no inverse, domain, characteristic or nontriviality assumption. CommSemiring is fixed interface floor. |
| 6 | Higher categories | No coherence/categorical construction needed for this elementary equality. |
| 7 | Concrete index | σ arbitrary; no numerical index to generalize. |
| 8 | Concrete-via-abstract | Yes diagnostic: proof body has one taylor occurrence inside the unfolding simp list, zero after unfolding. The content is zero normalization plus existing identity evaluation. Arbitrary g/A perturbation version is verified; useful for zero shifts after arbitrary substitutions. |
| 9 | False-generalisation guard | Adding zero to arbitrary assignments preserves the same substitution. Replacing identity assignment by arbitrary g and concluding aeval g P=P is rejected; arbitrary noncommuting target images are also not licensed by the current interface. |

Modern idiom available and already implemented for the identity law. The zero-shift normalization still requires propositional arithmetic facts: it is not a definitional bridge. [Body diagnostic](../evidence/MvPolynomial.taylor_zero/proof-body-diagnostic.json).

## Phase 4.5 — Infrastructure risks

n/a: theorem, not a data/instance declaration. It adds no class diamond, reducibility equation, noncanonical data unfolding, instance priority, universe restriction or coercion path. The simp attribute is an automation API whose callers are audited in Phase 6; it is not a new typeclass infrastructure diamond.

## Phase 4.6 — All five proof-strategy rows

| # | Question | Finding |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Elements versus subobject inclusions | No ideal/submodule inclusion; direct substitution normalization is appropriate. |
| 3 | Sequences versus nets | No analysis/convergence. |
| 4 | Construction versus universal property | Existing aeval identity law is already the universal-property route. No new object constructed. |
| 5 | Missing helper API | None mathematically necessary: C preserves zero, additive zero identity and aeval_X_left_apply suffice. Named translation simp API is a local presentation question. |

Strategy MATHLIB-IDIOMATIC. Existing closing simp is appropriate executable proof. Explicit exact composition independently demonstrates the substantive calls without automation; it is assessment evidence, not a recommendation to expand the local proof into verbose transport.

## Phase 5 — Five actual methods × three forms

Complete raw callable requests/responses: [formal search](../evidence/MvPolynomial.taylor_zero/formal-search.json). Current = zero translation; literature = substitution of original variables; abstract = universal-property/bundled algebra identity. Search index snapshots may differ from the pinned project; positive source/native checks establish compatibility.

| Method | Current | Literature | Abstract |
|---|---|---|---|
| Finder | Finds Polynomial.taylor_zero and taylor_zero': univariate analogues only. | Primarily univariate substitution identities; no false exact hit. | Finds generator/FreeAlgebra universal-property facts, contextual rather than exact. |
| Loogle | `MvPolynomial.aeval (fun i => MvPolynomial.X i + MvPolynomial.C 0) _ = _`: empty, not proof of absence. | `MvPolynomial.aeval MvPolynomial.X _ = _`: exact aeval_X_left_apply. | `MvPolynomial.aeval _ = AlgHom.id _ _`: exact aeval_X_left. |
| LeanSearch | Univariate Taylor neutral law and function translate_zero, different types/interfaces. | aeval_X_left_apply, eval₂_eta. | MvPolynomial.is_id, algHom_ext_iff and related identity/extensionality laws. |
| rg pinned source | [current](../evidence/MvPolynomial.taylor_zero/rg-current.json) | [literature](../evidence/MvPolynomial.taylor_zero/rg-literature.json) | [abstract](../evidence/MvPolynomial.taylor_zero/rg-abstract.json) |
| local name search | taylor_zero includes project target and Polynomial analogues. | aeval_X includes pinned MvPolynomial identity laws. | aeval_X_left confirms source declarations. All return index=unavailable; no absence inference from local index. |

Untruncated namespace-specific full-name search: [receipt](../evidence/MvPolynomial.taylor_zero/rg-full-name.json). No cheap namespace-aware prefilter: Polynomial.taylor_zero is a different declaration on a different polynomial type. Read pinned [Eval full module](../evidence/MvPolynomial.taylor_zero/MvPolynomial-Eval-module.lean.txt):

```lean
-- Mathlib/Algebra/MvPolynomial/Eval.lean:601,604
MvPolynomial.aeval_X_left :
  MvPolynomial.aeval MvPolynomial.X = AlgHom.id R (MvPolynomial σ R)
MvPolynomial.aeval_X_left_apply (p : MvPolynomial σ R) :
  MvPolynomial.aeval MvPolynomial.X p = p
```

The latter proof is `AlgHom.congr_fun aeval_X_left p`; the former follows from aeval_unique. `MvPolynomial.C_0` (Basic.lean:142) is `map_zero _`; the accepted independent composition uses generic map_zero directly. `add_zero` is the generic additive identity fact. These candidates are checked natively. Conclusion: exact identity-assignment law exists, and the old translation spelling is composed from it with two normalization facts. Parent taylor is BORDERLINE, so the special Mode-B NO-parent re-aim rule is not invoked.

## Phase 5.5 — All three statement-shape checks

Normal form: neutral translation reduces to unchanged P on the RHS, appropriate simp orientation. Equivalent forms include pointwise lambda zero, `(0 : σ → R)`, equality of bundled AlgHoms to AlgHom.id, and aeval_X_left_apply after normalization. No orthogonal equivalence network is introduced.

Syntactic generality: old pointwise statement, function-zero notation, bundled identity, independently defined raw substitution and arbitrary-target zero perturbation are actually probed. Keep pointwise form for local rewriting/simp; generic aeval_X_left is useful for composing homomorphisms. Shape is mathematically SHIP-AS-STATED; no syntactic change is needed to validate its content.

Superfluous arguments: all σ/R/CommSemiring/P rows above are essential to conclusion or fixed parent interface; NONE to drop. No hidden finite-variable, real-coefficient or nonzero hypothesis remains. No unsupported class weakening proposed.

## Phase 6.0 — Complete explicit caller and inline audit

Explicit named references outside the declaration: **0**, including same file and other project files. Internal count excluding declaring file: 0; external-to-file files: 0. This does **not** imply unused/dead code: `@[simp]` makes the law usable without its name.

[Exact token search](../evidence/MvPolynomial.taylor_zero/rg-callers.json), [all translation/identity inline search](../evidence/MvPolynomial.taylor_zero/rg-inline.json), [caller table](../evidence/MvPolynomial.taylor_zero/callers.json). Full Roth/Taylor.lean and Roth/Index.lean were read. No independent same zero law is re-derived inline in source. Inverse translation is a distinct law but has an implicit simplifier dependency:

| Caller | Use and concrete migration |
|---|---|
| MvPolynomial.taylor_neg_taylor, Taylor.lean:182–184 | `simp [taylor_taylor]` normalizes the summed shift to zero and implicitly uses taylor_zero. Remove target from simp locally in the native guard, demonstrate the old tactic no longer closes, then use `rw [taylor_taylor]` and `simpa only [neg_add_cancel] using <explicit zero composition at P>`. The native replay names the independent composition TaylorZeroAssessment.composed; inline its exact body for a production deletion. |
| MvPolynomial.taylor_injective, Taylor.lean:187–188 | Uses negative translation explicitly, not taylor_zero; replay against the replacement inverse proof. |
| MvPolynomial.taylor_eq_zero_iff, Taylor.lean:192–193 | Uses injectivity; replay against replacement injectivity. |

Remaining later Taylor proofs use inverse translation and ordinary map/support laws, not a further explicit zero law. Index.lean uses taylor_eq_zero_iff to simplify nonzero/support/power-series conditions; this is a transitive API consumer rather than another named taylor_zero call. No claim of exhaustive opaque kernel dependency closure or whole-project deletion migration. Native disabling/replacement experiment checks the identified implicit use and immediate chain, with used-constant evidence; [caller source](../evidence/MvPolynomial.taylor_zero/native-caller-executed.lean.txt), [success](../evidence/MvPolynomial.taylor_zero/native-caller-success.json).

## Phase 6 — Actual composition experiments

The original `simp [taylor, aeval_X_left_apply]` alone is a Phase-6b **trivial-simp borderline** signal. An independent exact old-form term succeeds with no simp/rw and no project proof lemma:

```lean
(congrArg (fun f : σ → MvPolynomial σ R ↦ aeval f P)
  (funext fun j ↦ (congrArg (fun q : MvPolynomial σ R ↦ X j + q)
    (map_zero (C : R →+* MvPolynomial σ R))).trans (add_zero (X j)))).trans
  (aeval_X_left_apply P)
```

Honest count: **three mathematical fact calls** (`map_zero`, `add_zero`, `aeval_X_left_apply`); equality plumbing additionally uses congrArg twice, funext once and Eq.trans twice. Counting every core equality combinator gives eight applications; no assertion of “three total kernel constants” is made. Definitional unfolding of taylor only exposes its aeval expression. The C(0) and +0 normalization is propositional, not assumed definitional. The explicit exact composition is the independent ≤3-existing-mathematical-facts criterion, so the closing-simp heuristic does not override it.

Accepted experiments also cover a mathlib-only raw assignment version with missing-target guard, bundled/pointwise shapes, arbitrary-algebra zero perturbation, fixed-interface Semiring rejection, and the simp-dependent inverse caller/refactor. All accepted native responses are complete, partial=false, success=true, with no errors/warnings and only standard axioms (propext, Classical.choice, Quot.sound). Sources, original execution paths and raw receipts are preserved in [verification](../evidence/MvPolynomial.taylor_zero/verification.json). No sorry/admit/unsafe/native_decide, new axiom or raised resource limits are accepted.

Conclusion **COMPOSABLE**. This is not NO-mathlib-has-it: aeval_X_left_apply alone is a different assignment spelling; the non-definitional bridge has been counted. It is not inherited BORDERLINE: the independent three-fact composition settles the composition criterion.

## Phase 7 — Actionable verdict

**NO-composable-from-mathlib**. Existing blocks: generic map_zero (`C` is a RingHom; specialized C_0 at Mathlib/Algebra/MvPolynomial/Basic.lean:142), generic add_zero, and MvPolynomial.aeval_X_left_apply at Mathlib/Algebra/MvPolynomial/Eval.lean:604. Their exact composition above establishes the old statement with only structural equality transport. No derivative or coefficient API gap is needed.

Refactor plan for all **0 explicit named callers**: none to replace by name. For the identified implicit caller taylor_neg_taylor at Taylor.lean:184, replace its proof with `rw [taylor_taylor]` followed by `simpa only [neg_add_cancel] using <explicit composition at P>` as verified using the independent scratch composition (inline that body when deleting the wrapper); keep its dependent injectivity/nonzero proofs against that result. Remove taylor_zero only together with this automation migration and a full project build; the assessment is read-only and does not claim that migration/build has been applied. Do not infer dead code from the empty named-reference list.

Alternative destination: retain the simp theorem in project-local `Roth/Taylor.lean` while the named translation API remains useful. It documents and automates a local semantic operation; this is compatible with declining a separate upstream contribution. Archive/ or a satellite library is unnecessary for an elementary normalization wrapper. Upstream design questions for the parent taylor remain separate; this report proposes no PR or production edit. Cost is not a verdict factor.

## Phase 8 — Evidence and verification handoff

All mandatory phases completed; definition-only checks 2b and 4.5 justified n/a. Raw web access limitations and unavailable optional ChatGPT channel are recorded, not treated as mathematical uncertainty. Native evidence and all source/pin hashes are portable and checked by [validator](../evidence/MvPolynomial.taylor_zero/validate.py), using the current [copy manifest](../evidence/MvPolynomial.taylor_zero/copy-manifest.json). Assessment [metadata](../evidence/MvPolynomial.taylor_zero/assessment.json) and [overview entry](../evidence/MvPolynomial.taylor_zero/overview-entry.json) carry the full statement, provenance and action. Root independent acceptance remains pending. No production Lean, Git or overview file was changed by the worker.
