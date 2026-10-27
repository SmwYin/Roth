# MvPolynomial.taylor_monomial — full mathlibable assessment

**NO-mathlib-has-it.** Independently verified existing law: `MvPolynomial.aeval_monomial`, `Mathlib/Algebra/MvPolynomial/Eval.lean:681`. The exact current statement is a one-call specialization, including the definitional translation bridge. This conclusion does not inherit the parent's BORDERLINE verdict.

## Phase 0 — Doctor

Canonical 57; public theorem at `Roth/Taylor.lean:59–61`. Shared clean `lake build` completed 2467 jobs, exit 0. All 17 source/pin SHA256 values freshly match the shared baseline. Declaration resolves, no unproved target; native diagnostics succeed completely, partial=false, no errors/warnings. The module develops translation, coefficient Taylor expansion using Hasse derivatives, and finite-box expansion.

Evidence: [baseline](../evidence/MvPolynomial.taylor_monomial/baseline-build.txt), [fresh hashes](../evidence/MvPolynomial.taylor_monomial/inputs.json), [canonical metadata](../evidence/MvPolynomial.taylor_monomial/canonical-entry.json), [full module](../evidence/MvPolynomial.taylor_monomial/Taylor-module.lean.txt), [native target](../evidence/MvPolynomial.taylor_monomial/native-target-success.json).

## Phase 1 — Comprehend

For a coefficient a and finitely supported exponent k, translating the monomial aX^k by α replaces every variable Xj with Xj+αj. Its image is the constant coefficient a multiplied by the finite product of the translated coordinate powers. This follows because evaluation is a coefficient-preserving algebra homomorphism.

Full elaborated type from the native #check (universes retained):

```lean
∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R]
  (α : σ → R) (k : σ →₀ ℕ) (a : R),
  (MvPolynomial.taylor α) ((MvPolynomial.monomial k) a) =
    MvPolynomial.C a * k.prod (fun j n ↦ (MvPolynomial.X j + MvPolynomial.C (α j)) ^ n)
```

σ is any variable type; R any commutative semiring; α supplies shifts, k supplies natural exponents with finite support, a is any coefficient. No field, characteristic, nonzero coefficient, finite-variable, nonempty-variable, or degree hypotheses occur. The proof is exactly `aeval_monomial _ _ _`; only project type dependency is `MvPolynomial.taylor`, no project proof-body dependencies.

## Phase 2 — Preliminary checks

SMALL: an elementary monomial evaluation law, not a main module result or a new named mathematical structure. The word Taylor reflects its parent operation; this is not the full named Taylor theorem. Exhaustive literature width still applies. Phase 2b is n/a: a theorem, not a one-line data definition. Its proof has one substantive line, recorded as a redundancy signal rather than a definition exemption.

## Phase 3 — Exhaustive literature

Each web artifact preserves exact requests, returned-response SHA256/bytes/status, titles and URL locators, with no article/search-result bodies. URLs have queries removed in stored locators to avoid signed downloads. The chronological queries are available individually below; the first three are distinct specific/general/alias forms.

| Channel | Actual query/access | Finding and limitation |
|---|---|---|
| General web specific | multivariate polynomial translation monomial product powers substitution | Magma Handbook, Representation: monomials are coordinate power products; coefficient times monomial called a term. [receipt 0](../evidence/MvPolynomial.taylor_monomial/web-0-metadata.json) |
| General web general | polynomial algebra universal property monomial evaluation commutative ring | Chambert-Loir, *(Mostly) Commutative Algebra*, Proposition 1.3.8; arbitrary set of generators, pairwise commuting target images. [receipt 1](../evidence/MvPolynomial.taylor_monomial/web-1-metadata.json) |
| General web aliases | Taylor shift multivariate monomial Hasse derivative | Shift/Hasse terminology; broader coefficient theorem distinguished from this substitution step. [receipt 2](../evidence/MvPolynomial.taylor_monomial/web-2-metadata.json) |
| ChatGPT math | Standard form, generality, historical evolution | n/a: ask_chatgpt_math unavailable; no simulated external opinion. |
| Local clean.tex | rg Taylor/monomials; §4 Index lines 500–527, 547–557 | Real finite-variable Taylor theorem reduces to monomials and binomial expansion. Lean statement already removes real/finite restrictions. [local record](../evidence/MvPolynomial.taylor_monomial/local-literature.json), [excerpt](../evidence/MvPolynomial.taylor_monomial/clean-Taylor-excerpt.tex.txt) |
| nLab | site:ncatlab.org/nlab polynomial ring universal property | Polynomial article describes free commutative R-algebra on arbitrary generator set; direct fetch failed unsupported XHTML content type, search snippet accessible. [receipt 3](../evidence/MvPolynomial.taylor_monomial/web-3-metadata.json) |
| nCatLab | site:ncatlab.org polynomial algebra substitution monomial | Same polynomial article and substitution/Lawvere-theory perspective. No distinct higher-category monomial formula found; no absence claim. [receipt 4](../evidence/MvPolynomial.taylor_monomial/web-4-metadata.json) |
| Stacks | site:stacks.math.columbia.edu polynomial ring monomial evaluation | Initial results broad algebra; initial opened 00EO was unrelated glueing, retained honestly. Refined universal-property search finds tag 07XB using polynomial-ring universal property; no exact target claim. [receipt 5](../evidence/MvPolynomial.taylor_monomial/web-5-metadata.json), [follow-up](../evidence/MvPolynomial.taylor_monomial/web-stacks-followup-metadata.json) |
| MathOverflow | site:mathoverflow.net multivariate polynomial Taylor Hasse derivative | Questions 82970 and 288218 concern characteristic-independent formal Taylor formulas and Hasse derivatives. Context supports distinction from analytic/factorial derivatives. [receipt 6](../evidence/MvPolynomial.taylor_monomial/web-6-metadata.json) |
| Recent arXiv, 2021-10-27–2026-10-27 | site:arxiv.org Hasse derivatives multivariate polynomial Taylor 2022 2023 2024 2025 2026 | 2502.09259 (2025-02-13) verified by abstract page, concerns arithmetic differential-series coefficients, not this monomial law. 2311.06374 is numerical Taylor optimization, also not exact. Older 2103.07239/1707.01354 results explicitly outside the five-year interval. [receipt 7](../evidence/MvPolynomial.taylor_monomial/web-7-metadata.json) |

Primary access and locators: [metadata](../evidence/MvPolynomial.taylor_monomial/web-primary-metadata.json). Chambert-Loir Proposition 1.3.8, printed page 14/PDF page 21, proof immediately displays the mapped coefficient-times-product rule. This is the strongest literature anchor. Magma Representation lines 31–33 confirms the terminology. No long quotations are reproduced.

Literature summary: standard concept is substitution/evaluation of a monomial in a polynomial algebra. The target translation is an arbitrary-substitution special case. Classical sources allow arbitrary coefficient rings and arbitrary generator sets; pairwise commuting images permit some noncommutative target extensions, but that is a different representation interface requiring explicit commuting hypotheses. No claim that arbitrary noncommutative images satisfy the current unordered product formula. Modern mathlib's commutative-semiring algebra evaluation covers the same positive-operation content without subtraction. Historical variation here is ring/algebra universal-property language versus finite-coordinate translation/Hasse language; no separate historical theorem attribution is inferred from search.

## Phase 4a–4b — Parameters and generality

| Parameter/hypothesis | Used? | Weakening/restatement assessment |
|---|---|---|
| σ : Type u_1 | yes | Any variable type, already universe polymorphic; no finiteness/nonemptiness/decidable equality needed. |
| R : Type u_2 | yes | Independent coefficient universe, no concrete real/integer restriction. |
| CommSemiring R | yes | Supports MvPolynomial, C, aeval and unordered product; subtraction/field/domain/char-zero already absent. Fixed parent/interface floor, no claimed drop to plain Semiring. |
| α : σ → R | yes | Arbitrary shifts; no nonzero/local hypotheses. Can replace the entire shift assignment by any g : σ → A in a commutative R-algebra A; compiled universal law already exists. |
| k : σ →₀ ℕ | yes | Finite support makes arbitrary-variable product meaningful; ℕ is polynomial exponent data. General monoid exponents would change the object. |
| a : R | yes | Coefficient preserved through algebraMap; may be zero, so no hidden nonzero assumption. |

Within the unchanged taylor/MvPolynomial interface: MAXIMALLY GENERAL (zero verified mechanical hypothesis drops). Relative to a broader substitution representation: strictly specialized assignment and target; the **accepted compiled general statement** is existing `aeval_monomial` for `[CommSemiring A] [Algebra R A] (g : σ → A)`. This is not a new helper proof or an unverified weakening proposal. It routes to NO-mathlib-has-it, not generalise-first. Root's isolated universal and let-bound-translation experiments verify both the wider form and the bridge: [raw source](../evidence/MvPolynomial.taylor_monomial/native-raw-executed.lean.txt), [raw success](../evidence/MvPolynomial.taylor_monomial/native-raw-success.json). No cost-based judgment.

## Phase 4c — All nine modern-idiom questions

| # | Question | Answer, proposed form, concrete downstream consequence |
|---|---|---|
| 1 | Typeclasses/instances | Already uses CommSemiring; no ad-hoc structure hypotheses. |
| 2 | Filters/topology | No: finite algebraic evaluation, no limits. |
| 3 | Universal property | Yes: use existing aeval of the free commutative R-algebra. It accepts arbitrary assignment and composes with eval₂Hom_monomial and substitution API. |
| 4 | Bundled substructures | No closure predicate/subobject; already an AlgHom. |
| 5 | Weaker algebra hierarchy | Already semiring, no field or characteristic assumptions. Arbitrary target commutative R-algebra uses existing law, not a new class. |
| 6 | Higher categories | No: no categorical coherence in this scalar/product equality; Lawvere viewpoint does not give a needed Lean improvement. |
| 7 | Abstract index | σ already arbitrary. ℕ exponents are essential polynomial data; arbitrary additive-group exponent replacement changes to Laurent/group algebra. |
| 8 | Concrete-via-abstract | Yes: proof body has zero occurrences of taylor and consists only of aeval_monomial. Diagnostic explicitly recorded; arbitrary g/A gives same proof. Enables evaluation into other algebras and substitutions with different variable targets. |
| 9 | False-generalisation guard | Universal aeval is a true generalization: set A=MvPolynomial σ R, g j=X j+C(α j). Removing commutativity without commuting-image conditions, or replacing ℕ exponents freely, is rejected as semantic/interface change. |

Modern idiom available and already implemented: generic algebra evaluation; no missing modernization contribution. [Diagnostic](../evidence/MvPolynomial.taylor_monomial/proof-body-diagnostic.json).

## Phase 4.5 — Infrastructure risks

n/a — theorem introduces no data, instance, or coercion infrastructure. The six possible risks (typeclass diamonds, reducibility leaks, noncanonical unfolding, priority collisions, universe issues, coercion ambiguity) are not new infrastructure supplied by this declaration. Its parent is assessed independently; this theorem adds no alternative structure path.

## Phase 4.6 — All five proof-strategy rows

| # | Question | Answer |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Elements versus subobject inclusion | No inclusion argument; direct universal substitution law is already optimal. |
| 3 | Sequences versus nets | No analytic convergence. |
| 4 | Construction versus universal property | Existing aeval law already encodes the universal-property computation; reuse it directly. |
| 5 | Missing helper API | None: aeval_monomial is exactly the needed helper and is existing mathlib. |

Strategy verdict: MATHLIB-IDIOMATIC, one existing-call proof; refactor recommendation is API deduplication, not a different proof strategy.

## Phase 5 — Five actual methods × three forms

All 12 callable search requests and complete raw responses: [formal-search](../evidence/MvPolynomial.taylor_monomial/formal-search.json). Current form = translated monomial; literature form = evaluation/substitution of coefficient times powers; abstract form = arbitrary commutative R-algebra evaluation. External search snapshots can differ from the pin; positive candidate source and native checks settle compatibility.

| Method | Current | Literature | Abstract |
|---|---|---|---|
| Finder | Translation query finds bind₁_monomial, univariate Polynomial.taylor_monomial (analogue, not qualified-name match). | General monomial-evaluation query finds eval₂Hom_monomial/eval₂_monomial. | Arbitrary R-algebra query finds aeval_monomial. |
| Loogle | `MvPolynomial.aeval, MvPolynomial.monomial`: aeval_monomial. | `MvPolynomial.eval₂, MvPolynomial.monomial`: generic evaluation laws. | `MvPolynomial.aeval, _ = algebraMap _ _ _ * _`: aeval_monomial. |
| LeanSearch | Translated-monomial prose returns mostly MvPowerSeries analogues; not an exact hit. | Monomial evaluation query returns evaluation candidates. | Arbitrary commutative-algebra query returns aeval_monomial, eval_monomial, eval₂_monomial. |
| rg source | [current](../evidence/MvPolynomial.taylor_monomial/rg-current.json) | [literature](../evidence/MvPolynomial.taylor_monomial/rg-literature.json) | [abstract](../evidence/MvPolynomial.taylor_monomial/rg-abstract.json) |
| local name search | taylor_monomial: own target + univariate name collision. | eval₂_monomial: returned broad eval names only, no exact monomial hit. | aeval_monomial: pinned MvPolynomial candidate. All three return index=unavailable; source hits are useful, empty index cannot imply absence. |

Untruncated full-name search retained: [receipt](../evidence/MvPolynomial.taylor_monomial/rg-full-name.json). No namespace-aware cheap prefilter applies: `Polynomial.taylor_monomial` is a distinct one-variable theorem. Pinned full declaring source read: [Eval](../evidence/MvPolynomial.taylor_monomial/MvPolynomial-Eval-module.lean.txt). `aeval_monomial` has type:

```lean
∀ {R : Type u} {A : Type v} {σ : Type w}
  [CommSemiring R] [CommSemiring A] [Algebra R A]
  (g : σ → A) (d : σ →₀ ℕ) (r : R),
  MvPolynomial.aeval g (MvPolynomial.monomial d r) =
    algebraMap R A r * d.prod (fun i k ↦ g i ^ k)
```

Its implementation is `eval₂Hom_monomial _ _ _ _` (same file :203, generic coefficient ring map). Native checks print exact signatures/proofs of both. Concluded: found in mathlib as **MvPolynomial.aeval_monomial**, strictly more general assignment and target. No absence inference needed or claimed.

## Phase 5.5 — All three statement-shape checks

Normal form: generic aeval of a monomial → algebraMap(coefficient) times finite product is the canonical evaluation form. Target RHS follows this form, with C=algebraMap for the polynomial target. Equivalent forms include eval₂Hom_monomial with coefficient map, the current named translation, and the explicit/let-bound aeval. No orthogonal A↔B equivalence needed; RHS convention respected.

Syntactic generality: actually attempted current exact call, generic arbitrary-target theorem, let-bound explicit translation, and typed rewrite in the full caller. All accepted. Choose generic aeval_monomial with inferred assignment where elaboration can infer it; typed show at the rewrite site preserves the original LHS matching.

Superfluous-argument audit: every row of the Phase 4 parameter table is essentially used in the conclusion or fixed parent interface; NONE to drop within that spelling. Universes already general. Overall SHIP-AS-STATED mathematically; DELETE-REDUNDANT-LOCAL-API for this project. No new restated theorem proposed upstream.

## Phase 6.0 — Explicit callers and inline audit

All explicit source callers: **1**. Internal excluding declaring file: **0**; external-to-file files: **0**. [Exact word-token grep](../evidence/MvPolynomial.taylor_monomial/rg-callers.json), [caller table](../evidence/MvPolynomial.taylor_monomial/callers.json), [inline search](../evidence/MvPolynomial.taylor_monomial/rg-inline.json).

| Caller | Exact use | Refactor |
|---|---|---|
| `MvPolynomial.eq_sum_box_hasseDeriv`, declared Taylor.lean:197, use :212 | `rw [taylor_monomial, Finsupp.prod_fintype _ _ fun _ ↦ pow_zero _]` | Replace first rewrite token with the typed equality `show taylor (fun j ↦ -α j) (monomial d (eval α (hasseDeriv d P))) = C (eval α (hasseDeriv d P)) * d.prod (fun j n ↦ (X j + C (-α j)) ^ n) from aeval_monomial _ _ _`. |

Private helper identifiers such as coeff_taylor_monomial_aux contain the substring but are not references to this theorem. No additional equivalent full formula re-derived inline was found; related monomial induction is not counted as an identical derivation. The theorem has **no simp attribute**, unlike taylor_X/C; no automatic simp-removal experiment is needed for it. Source-level names are not opaque kernel dependency closure; no whole-project deletion/build migration is claimed.

The complete current caller statement and proof (including its h1 coefficient reconstruction) were replayed in namespace MvPolynomial.TaylorMonomialCallerReplay, replacing only the target rewrite token with the typed generic law. Accepted [caller source](../evidence/MvPolynomial.taylor_monomial/native-caller-executed.lean.txt), [caller receipt](../evidence/MvPolynomial.taylor_monomial/native-caller-success.json). First attempt had one >100-column style warning; only wrapping changed. Rejected [receipt](../evidence/MvPolynomial.taylor_monomial/native-caller-rejected.json) retained separately, not accepted as verification.

## Phase 6 — Actual composition experiments

1. Exact current-target theorem `... := aeval_monomial _ _ _` accepted in native target context. One existing call, no simp/rewrite normalization proof.
2. Mathlib-only isolated `universal` at arbitrary g into arbitrary commutative R-algebra accepted; own theorem missing guarded by `#check_failure MvPolynomial.taylor_monomial`.
3. Mathlib-only let-bound translation (`let T := aeval ...`) accepted by the same single call; removes reliance on project taylor symbol and demonstrates its definitional bridge.
4. Entire one named caller proof accepted with typed rewrite substitution described above.

Conclusion COMPOSABLE, and stronger: already a direct existing law. Phase 6b trivial-simp BORDERLINE caveat does not apply: accepted proof is an exact theorem term, not `simp [defs...]`. Parent taylor remains independently BORDERLINE; neither inheriting it nor turning this into a new general theorem is warranted.

All accepted checks complete with partial=false and no errors/warnings, standard axioms only (propext, Classical.choice, Quot.sound), no extra axioms, sorry/admit, unsafe/native_decide, or raised limits. Exact archived sources, request execution paths and full untruncated native receipts: [verification manifest](../evidence/MvPolynomial.taylor_monomial/verification.json).

## Phase 7 — Actionable verdict

**NO-mathlib-has-it**: the generic monomial law is present, and the user's exact statement follows in one line:

```lean
example {σ R : Type*} [CommSemiring R] (α : σ → R) (k : σ →₀ ℕ) (a : R) :
    MvPolynomial.taylor α (MvPolynomial.monomial k a) =
      MvPolynomial.C a * k.prod (fun j n ↦ (MvPolynomial.X j + MvPolynomial.C (α j)) ^ n) :=
  MvPolynomial.aeval_monomial _ _ _
```

The true general law is useful and already upstream; the specialization adds no mathematical or organizational gap. This finding is pinned and native verified, rather than inferred from naming or inherited parent verdict. Existing exact primitive: MvPolynomial.aeval_monomial at `Mathlib/Algebra/MvPolynomial/Eval.lean:681`; its generic implementation uses MvPolynomial.eval₂Hom_monomial. A further expanded coefficient-map representation is available via eval₂, but unnecessary for the current caller.

Next action: delete local taylor_monomial and update the **one** explicit caller `eq_sum_box_hasseDeriv` with the typed show equality above (full replay already checked). Preserve parent taylor decisions separately; this does not require deleting or redesigning translation. If local narrative/API convenience is deliberately retained, the alternative destination is existing project-local `Roth/Taylor.lean`, documented as an alias specialization, not a new mathlib contribution. No PR/grouping/reviewer checklist applies to this NO verdict. The caller itself contains substantive coefficient, Taylor and inverse-translation mathematics; replacing this leaf does not classify or simplify away that caller. No production edits were made by this assessment.

## Phase 8 — Handoff and validation

Full required phases complete; 2b and 4.5 justified n/a for theorem kind. No unresolved verification. Root acceptance pending independent review. [Assessment](../evidence/MvPolynomial.taylor_monomial/assessment.json), [overview entry](../evidence/MvPolynomial.taylor_monomial/overview-entry.json), [portable validator](../evidence/MvPolynomial.taylor_monomial/validate.py), [current copy manifest](../evidence/MvPolynomial.taylor_monomial/copy-manifest.json). The validator checks current artifact hashes (historical worker-copy-manifest never substitutes), 17 inputs, clean full native receipts and standard axioms, formal methods/forms, literature request metadata, source/caller identities and all relative links. Production, Git and overview untouched.
