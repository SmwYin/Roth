# MvPolynomial.eval_taylor — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** Canonical declaration 64, `Roth/Taylor.lean:141`, branch `ramin-cleanup`. The evidence supports an API-design choice: this is a valid translation-evaluation law, but its mathematical engine already exists as generic evaluation composition. The closing `simp` proof is explicitly a borderline case under Phase 6b. Neither the parent's BORDERLINE verdict nor the preceding coefficient theorem's YES verdict is inherited.

## Phase 0 — Baseline

The recorded `lake build` exited 0 with 2467 jobs. All 17 current production source and pin SHA256 values were freshly checked against that baseline and match. The declaration resolves uniquely, is a theorem with no sorry, and is part of the Taylor-expansion module. The full 224-line module was read. [Baseline](../evidence/MvPolynomial.eval_taylor/baseline-build.txt), [fresh hashes](../evidence/MvPolynomial.eval_taylor/input-hash-check.json), [complete module](../evidence/MvPolynomial.eval_taylor/Taylor-module.lean.txt), [native target receipt](../evidence/MvPolynomial.eval_taylor/native-target-success.json).

## Phase 1 — Statement and proof

For a polynomial with coefficients in a commutative semiring and an arbitrary variable set, translating every variable by a fixed vector α and then evaluating at x is the same as evaluating the original polynomial at x+α. This is formal substitution, without differentiation, limits, factorials, characteristic assumptions, finiteness of the variable set, or degree bounds. Evaluating the substituted variables gives xⱼ+αⱼ; the universal property of polynomial evaluation extends this equality to every polynomial.

Full native elaborated type (independent universes):

```lean
∀ {σ : Type u_1} {R : Type u_2} [CommSemiring R] (α x : σ → R)
  (P : MvPolynomial σ R),
  eval x (taylor α P) = eval (fun j ↦ x j + α j) P
```

Parameters: σ is the variable index type, R the coefficient semiring, α the translation vector, x the evaluation vector, and P the polynomial. The sole instance hypothesis supplies the existing `MvPolynomial`, `taylor`, and `eval` interfaces. Project proof dependency: `MvPolynomial.taylor`; it does not use `coeff_taylor`, Hasse derivatives, or `Roth.box`. Existing mathlib engine: `MvPolynomial.eval_assoc`, with `aeval_def` and evaluation's add/X/C normalization. Root's replay uses the original proof without calling the target theorem; isolated probes guard `#check_failure MvPolynomial.eval_taylor`.

## Phase 2 — Preliminary checks

SMALL: an elementary compatibility law, not a new structure or a listed main result. “Taylor” labels the existing operation here, not a new named Taylor-expansion theorem. The definition-only one-line test is n/a: declaration kind is theorem. Its one substantive proof line remains relevant to composition, not to the definition exemptions.

## Phase 3 — Exhaustive literature

Every named channel was actually searched; exact requests, response hashes/byte counts, locators and concise summaries are retained without full web bodies. The command informally says nine channels but lists three general-web forms separately; all listed forms were performed.

| Channel | Exact query or local action | Outcome |
|---|---|---|
| General web, specific | multivariate polynomial translation evaluation P(x+a) substitution | Substitution and Taylor-shift terminology; elementary evaluation law. |
| General web, general | polynomial ring evaluation homomorphism composition universal property | Primary Passau notes, Theorem 3.6.6 and Corollary 3.6.7. |
| General web, aliases | Taylor shift multivariate polynomial semiring evaluation | Shift/translation is substitution X↦X+α; no stronger hypotheses required. |
| Optional mathematical second opinion | n/a: ask_chatgpt_math unavailable | No invented response; historical formulation not independently queried. |
| Local reference | clean.tex:499–528, 547–555 | Finite real-variable Taylor theorem and Pα(X)=P(X+α) implementation note. |
| nLab | site:ncatlab.org/nlab polynomial algebra universal property evaluation | `polynomial` entry: free commutative R-algebra on arbitrary generators. Direct open later failed with unsupported XHTML; indexed search content was available. |
| nCatLab | site:ncatlab.org/ncatlab polynomial substitution evaluation | Cross-returned nLab `substitution`; no distinct nCatLab theorem. |
| Stacks | site:stacks.math.columbia.edu polynomial ring universal property evaluation | Generic universal-property applications; no exact translation-evaluation theorem. Auxiliary tag 00E0 open is unrelated and is not counted as support. |
| MathOverflow | site:mathoverflow.net multivariate polynomial substitution translation evaluation | Multivariate-system questions; no exact law found. |
| Recent arXiv, five years | site:arxiv.org multivariate polynomial Taylor shift 2022 2023 2024 2025 2026 | 2025 shift-invariant polynomial distributions and 2023 Taylor-map factorization; neither gives a stronger evaluation theorem. Relevant window: 2021-10-27–2026-10-27. |

[General-web evidence](../evidence/MvPolynomial.eval_taylor/web-0.json), [nLab](../evidence/MvPolynomial.eval_taylor/web-N.json), [nCatLab](../evidence/MvPolynomial.eval_taylor/web-C.json), [Stacks](../evidence/MvPolynomial.eval_taylor/web-S.json), [MathOverflow](../evidence/MvPolynomial.eval_taylor/web-O.json), [arXiv](../evidence/MvPolynomial.eval_taylor/web-A.json), [primary opens and access failures](../evidence/MvPolynomial.eval_taylor/web-P.json), [local reference hash/locators](../evidence/MvPolynomial.eval_taylor/local-literature.json).

The standard names are polynomial substitution, evaluation homomorphism, and Taylor shift. The abstract standard form sends arbitrary polynomial substitutions through an algebra homomorphism. [Moritz Müller's Algebra notes](https://www.fim.uni-passau.de/fileadmin/dokumente/fakultaeten/fim/lehrstuhl/muller/Algebra.pdf), §3.6 Theorem 3.6.6 / Corollary 3.6.7, give arbitrary-index commutative-ring substitution by universal property. The assessed law follows mathematically by choosing Xⱼ+αⱼ (an inference from that property). [nLab polynomial](https://ncatlab.org/nlab/show/polynomial) supplies the free-algebra viewpoint. The current semiring and arbitrary-index statement is already broader than the local finite-real formulation. Sources vary in coefficient structures and target algebras, not in the sign or order of this substitution law.

## Phase 4 — Generality

| Parameter / hypothesis | Comparison and drop audit |
|---|---|
| σ : Type* | Arbitrary type in an independent universe; neither finite nor inhabited nor decidable required. No hypothesis to drop. |
| R : Type* | Arbitrary coefficient type, independent of σ. No concrete field to abstract. |
| CommSemiring R | Floor of the existing same-ring polynomial evaluation/translation interface. Semiring-only eval is rejected in a guarded native probe. This is an interface constraint, not a theorem that every noncommutative representation is impossible. |
| α : σ → R | Essential translation input. Dropping or restricting it changes the law. Arbitrary constants already allowed. |
| x : σ → R | Essential evaluation input. Can expand the codomain to a commutative R-algebra A, with coefficient map explicit. |
| P : MvPolynomial σ R | Essential polynomial input; not a proof hypothesis, no degree or nonzero assumption. |

**MAXIMALLY GENERAL within the fixed same-ring `eval`/`taylor` interface; zero mechanical hypothesis drops.** A verified expanded representation evaluates in an arbitrary commutative R-algebra A and replaces αⱼ on the RHS by `algebraMap R A (α j)`. This adds a codomain and algebra structure rather than merely deleting a hypothesis. Generic substitution is already `comp_aeval_apply`; do not propose a new abstract wrapper as missing API. [Exact extra experiments](../evidence/MvPolynomial.eval_taylor/native-extra-executed.lean.txt), [native verification](../evidence/MvPolynomial.eval_taylor/native-extra-success.json).

### Phase 4c — Modern idiom

| # | Diagnostic | Answer and consequence |
|---|---|---|
| 1 | Typeclass preambles | No: `CommSemiring` already inferred as an instance. |
| 2 | Sequences vs filters | No topology or convergence. |
| 3 | Construction vs universal property | Yes diagnostic: translation is polynomial substitution characterized by generator images; existing `comp_aeval` already expresses functoriality. No new structure is needed. |
| 4 | Closure predicate vs bundled substructure | No closure predicate; `taylor` is already an AlgHom. |
| 5 | Field/vector-space specificity | No: semiring form already removes subtraction, division and characteristic restrictions. The expanded target-algebra law was actually tested. |
| 6 | Higher category | No higher-categorical premise or useful additional consequence identified. |
| 7 | Concrete index | No: σ is arbitrary; ℕ exponent representation is intrinsic to polynomials, not an unnecessary theorem parameter. |
| 8 | Concrete-via-abstract | Yes: the proof mentions `taylor` only once, in its unfolding list; zero lines use translation after that unfolding. Abstract restatement is existing `eval_assoc` / `comp_aeval_apply`, verified locally. Enables substitutions into arbitrary polynomial rings and algebra targets without adding translation-specific engine lemmas. |
| 9 | False-generalisation guard | Passed for the algebra-target law: specializing A=R and its identity algebra recovers the same x+α convention. A noncommutative target without commuting images would change the evaluation interface and is not claimed. Polynomial functions are not substituted for formal polynomials: finite-ring extensionality would lose information. |

Modern idiom is available and already implemented in mathlib. It does not automatically remove the potential usefulness of a named law for a separately accepted translation API. No novel abstract theorem or verified one-edit weakening supports a YES-but-generalise-first verdict.

### Phase 4.5 — Infrastructure risk

n/a — theorem, not a definition, class, structure or instance. All six definition-risk rows (diamond, reducibility, noncanonical unfolding, priority, universe, coercion) are outside this declaration's scope. Parent-definition design is recorded separately, not inherited.

### Phase 4.6 — Proof strategy

| # | Question | Answer |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Elements versus substructure inclusions | No ideal/submodule inclusion; element evaluation identity is the intended interface. Hom-level composition exists and was tested. |
| 3 | Sequences versus nets | No analysis. |
| 4 | Explicit construction versus universal property | The current composition proof already uses the polynomial universal property through `eval_assoc`; `comp_aeval_apply` is the bundled alternative. |
| 5 | Helpers mathlib should have | None required: generic composition and add/X/C evaluation laws exist. The only open choice is the translation-specific convenience surface. |

MATHLIB-IDIOMATIC. No monomial induction, coefficient convolution, or new helper is needed. This assessment does not use failed automation as evidence of mathematical difficulty.

## Phase 5 — Five methods × three forms

All fifteen combinations were executed; raw formal-search responses are preserved. Source `rg` requests include full output and exit codes. External indices may differ from the pinned checkout; positive signatures and successful uses were verified natively in the pinned project.

| Method | Current translation form | Literature substitution form | Abstract algebra-hom form |
|---|---|---|---|
| Lean-Finder | `Polynomial.taylor_eval` (univariate analogue only) | `MvPolynomial.eval_eval₂`, `aeval_bind₁` | `comp_aeval`, `comp_aeval_apply` |
| Loogle | `aeval_eq_eval` bridge | evaluation-composition family | `comp_aeval`, bind/rename analogues |
| LeanSearch | univariate shift and rename near hits | evaluation/substitution API | `comp_aeval` and `aeval_comp_bind₁` |
| rg current checkout | Taylor/shift/add patterns | `eval_assoc`, `eval_eval₂` | `comp_aeval`, `aeval_unique` |
| Local name search | Project target only | `eval_assoc` | `comp_aeval`, `comp_aeval_apply` |

Local symbol index reported `unavailable` for these lookups; positive source hits remain useful, but empty results establish no absence. No source-level exact multivariate `eval_taylor` was found in the untruncated full-name rg. This is not a proof of global absence. [Formal-search index](../evidence/MvPolynomial.eval_taylor/formal-search.json), [full-name rg](../evidence/MvPolynomial.eval_taylor/rg-full-name.json), [pinned source hashes](../evidence/MvPolynomial.eval_taylor/mathlib-inputs.json).

Verified core candidates in `Mathlib/Algebra/MvPolynomial/Eval.lean`: `eval_assoc` at 303, `eval_eval₂` at 313, `comp_aeval` at 607 and `comp_aeval_apply` at 612. The latter takes an arbitrary R-algebra hom φ and proves `φ (aeval f P) = aeval (fun i ↦ φ (f i)) P`. The former directly proves the abstract eval-after-substitution law up to symmetry. `Polynomial.taylor_eval` in `Mathlib/Algebra/Polynomial/Taylor.lean` is an exact univariate analogy, not a replacement for arbitrary σ. Conclusion: existing generic building blocks and abstract law, with genuine generator-image normalization required for the old translation spelling.

## Phase 5.5 — Statement shape

Normal forms compared: pointwise equality as written; equality of evaluation/composition homomorphisms; and the generic `eval₂ C f` substitution form. Existing canonical abstract form is `comp_aeval`; the pointwise RHS `eval (x+α) P` removes the intermediate polynomial and respects evaluation normalization. Normal form: OK.

Syntactic generality attempts: the isolated `homForm` uses existing `comp_aeval` directly; `abstractLaw` uses `(eval_assoc f x P).symm`; `baseChange` tests the arbitrary-algebra target. Choose the current pointwise statement for a translation API, since rewrite consumers supply α, x, P without constructing a hom equality. Choose existing generic composition when translation is inlined. None is a verified missing abstract theorem. Syntactic generality: OK, with the expanded target as an upstream API option.

Superfluous-argument audit: σ and R determine the polynomial type; `CommSemiring R` supports its fixed evaluation interface; α, x and P occur essentially in the assertion. No proposition hypothesis, finiteness, decidability, inhabitance or nontriviality assumption is present to remove. Superfluous arguments: NONE. Overall: SHIP-AS-STATED if a translation-specific law is accepted; naming and expanded target remain Phase 7 design choices.

## Phase 6 — Callers and actual composition

Internal named source use count: **0**. External-to-file callers: **0 files**. Same-file named callers excluding the declaration: **0**.

| Caller | Usage / refactor impact |
|---|---|
| None | Source search includes qualified, bare and dot spelling. No existing source call needs replacement if this law is removed. |

Inline exact re-derivations: none. `Roth/MainLemma.lean:409–410` uses `comp_aeval_apply` for diagonal substitution, a different assertion. `taylor_taylor`, `taylor_map`, and `taylor_rename` are related substitution laws, not callers or duplicate evaluations. The theorem is not marked simp; zero named calls gives no present source reuse signal. LSP returned five locations: the declaration and four scratch inspection references (including one overlapping identifier location); after filtering, zero production callers. This count is explicitly separate from any implicit kernel/simp dependency closure. [Raw LSP receipt](../evidence/MvPolynomial.eval_taylor/native-references.json). [Call-site inventory](../evidence/MvPolynomial.eval_taylor/callers.json), [raw rg](../evidence/MvPolynomial.eval_taylor/rg-callers.json), [inline audit](../evidence/MvPolynomial.eval_taylor/rg-inline.json).

Actual experiments, not inferred shortness:

1. Source replay in the project and independent mathlib-only copy both close with `simp [taylor/shift, aeval_def, ← eval_assoc, Function.comp_def]`. The isolated copy guards target absence and avoids project simp lemmas.
2. The abstract substitution statement is exactly `(MvPolynomial.eval_assoc f x P).symm`: one existing mathematical call. This proves the abstract law exists, not that `x+α` is definitionally the composed image.
3. The bundled attempt specializes `comp_aeval_apply` to the evaluation AlgHom, then normalizes map-add and variable/constant evaluation. A first loose `simpa` exhausted default heartbeats; a narrow attempt initially mismatched aeval and eval. Both rejected packets and recovered sorryAx are archived separately and excluded from accepted proof evidence. The repaired packet succeeds without raised limits.

[Accepted exact isolated source](../evidence/MvPolynomial.eval_taylor/native-raw-executed.lean.txt), [accepted receipt](../evidence/MvPolynomial.eval_taylor/native-raw-success.json), [verification index](../evidence/MvPolynomial.eval_taylor/verification.json).

Existing-call accounting: composition `eval_assoc`/`comp_aeval_apply` plus add preservation, variable evaluation and constant evaluation is at least four mathematical building-block families, besides definition/coercion bridges and congruence. The abstract one-call proof does not eliminate those premises. No ≤3-call old-form term was independently established. **Conclusion: trivial simp composition; BORDERLINE under Phase 6b**, rather than automatic NO-composable or absence-driven YES. The full native target print confirms map_add, eval_X and eval_C normalization, so the representation bridge is not treated as rfl.

## Phase 7 — Verdict and next action

**BORDERLINE-needs-human**, independently assessed. Literature recognizes the operation; the fixed-interface statement is general and elementary. Mathlib supplies its abstract mathematical content, while the translation-specific name might provide a convenient rewrite law if a multivariate Taylor translation API is chosen. This is exactly the closing-simp case singled out by Phase 6b. Zero present named callers adds no evidence for urgent upstream inclusion. The parent `taylor` remains BORDERLINE; this theorem's own normalization and composition checks, not inheritance, determine the verdict. The separate `coeff_taylor` YES concerns coefficient/Hasse content and does not imply this compatibility law should ship independently.

Concrete future upstream API questions (no user response needed to finish this read-only assessment):

1. If a multivariate translation API is accepted, should its evaluation law be a named convenience theorem despite its closing-simp derivation from generic composition?
2. Should that law target arbitrary commutative R-algebras via `aeval`, with this same-ring `eval` version as a specialization, or retain the minimal same-ring surface?
3. Should its name follow the existing univariate `Polynomial.taylor_eval` convention rather than `eval_taylor`, and should the chosen orientation be a simp rule?

Next action: retain the law in project-local `Roth/Taylor.lean` while those upstream design choices are resolved; there are zero named source call sites to migrate. If translation remains expressed directly by `aeval`, use existing `comp_aeval_apply`/`eval_assoc` plus generator normalization where needed. Re-run the assessment after choosing the API. No production source, pin or Git mutation is part of this report.

## Phase 8 — Evidence completion

All required phases are complete or theorem-specific n/a. Accepted raw native results must report full success, no partial elaboration, no errors or warnings, and only standard axioms `propext`, `Classical.choice`, `Quot.sound`. Rejected attempts are explicitly separate. [Portable validator](../evidence/MvPolynomial.eval_taylor/validate.py), [current copy manifest](../evidence/MvPolynomial.eval_taylor/copy-manifest.json), [assessment metadata](../evidence/MvPolynomial.eval_taylor/assessment.json). Root acceptance is pending independent review; upstream API questions are design outcomes, not unresolved verification.
