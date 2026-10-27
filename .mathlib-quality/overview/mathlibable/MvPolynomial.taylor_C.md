# MvPolynomial.taylor_C — mathlibable assessment

**NO-mathlib-has-it** — the existing `MvPolynomial.algHom_C` is the complete, more general law: every R-algebra homomorphism from multivariate polynomials sends a scalar constant to its algebra-map image. The source statement follows by the single exact call `algHom_C _ _`. This verdict is independently verified, not inherited from the parent `taylor` (BORDERLINE) or sibling `taylor_X` (NO).

Canonical declaration 56; `Roth/Taylor.lean:55`; public theorem, `@[simp]`. Read-only assessment on `ramin-cleanup`; no production or Git changes. Root acceptance pending.

## Phase 0 — baseline

The successful shared `lake build` completed 2467 jobs with no errors or warnings: [baseline receipt](../evidence/MvPolynomial.taylor_C/baseline-build.txt). All 17 source/pin hashes were freshly matched to that baseline: [inputs](../evidence/MvPolynomial.taylor_C/inputs.json), [hash check](../evidence/MvPolynomial.taylor_C/input-hash-check.json). The declaration exists, has no sorry, and belongs to the module on multivariate translation and Taylor expansion. The entire [Taylor module](../evidence/MvPolynomial.taylor_C/Taylor-module.lean.txt) and entire explicit caller's [Index module](../evidence/MvPolynomial.taylor_C/Index-module.lean.txt) were read. [Canonical entry](../evidence/MvPolynomial.taylor_C/canonical-entry.json), [ordered entry](../evidence/MvPolynomial.taylor_C/order-entry.json).

Instructions consulted: installed mathlib-quality SKILL.md, complete commands/mathlibable.md, mathlib-search.md, mathlibable-verdicts.md, generalisation-patterns.md, mathlib-review-stages.md and worker contract. Root ran native Lean serially; evidence contains complete executed documents and original request paths.

## Phase 1 — comprehension

Substituting X_j+α_j for each variable leaves a constant polynomial unchanged. The reason is independent of translation: an R-algebra homomorphism preserves coefficients through the structure map. No differentiation or analytic Taylor convergence is involved.

Full native elaborated type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (α : σ → R) (a : R),
  (MvPolynomial.taylor α) (MvPolynomial.C a) = MvPolynomial.C a
```

Here σ is any variable type, R any commutative semiring, α an arbitrary translation vector and a any coefficient. No finiteness, nonzero, characteristic, decidability, field or order hypotheses appear. The exact source proof is `algHom_C _ _`; [target receipt](../evidence/MvPolynomial.taylor_C/native-target-success.json) prints the original declaration, its proof and full type, and accepts an independent replay. [Executed source](../evidence/MvPolynomial.taylor_C/native-target-executed.lean.txt).

## Phase 2 — preliminary checks

SMALL: elementary constant substitution helper, not the module's Taylor expansion theorem. The name of the parent operation does not make this an eponymous main result. Phase 2b n/a: theorem, not a one-line data definition. Its one-call proof is independently investigated below.

## Phase 3 — exhaustive literature

Every named channel was actually attempted, including three distinct general-web forms. Exact requests, original returned-response SHA256/byte counts, returned titles/locators and original concise summaries are preserved without article/search-result bodies. Returned URL query strings are conservatively omitted from locator lists; response hashes refer to the original responses.

| Channel | Actual query/locator | Finding |
|---|---|---|
| General web, specific | `"multivariate polynomial" translation "constant"` | Buchacher–Kauers, *On the Problem of Separating Variables in Multivariate Polynomial Ideals* (2024), Lemma 1, treats translation as a K-algebra map. Search excerpt only. [metadata](../evidence/MvPolynomial.taylor_C/web-0-metadata.json) |
| General web, general | `"algebra homomorphism" "constants" polynomial` | Ziyu Zhang, Lecture 6, Definition 3.16 and Lemma 3.18: coefficient preservation is part of algebra maps and polynomial pullbacks. [metadata](../evidence/MvPolynomial.taylor_C/web-1-metadata.json) |
| General web, alias | `"Taylor shift" constant polynomial` | FLINT composition/Taylor-shift documentation returned; computational name for substitution. [metadata](../evidence/MvPolynomial.taylor_C/web-2-metadata.json) |
| ChatGPT mathematical MCP | Standard form, generality and historical evolution question | n/a: ask_chatgpt_math unavailable; no invented answer. |
| Local references | clean.tex §4, lines 501–555 | P_α(X)=P(X+α), after Taylor theorem. Real coefficients and finite variables are application assumptions. [summary](../evidence/MvPolynomial.taylor_C/local-literature.json), [excerpt](../evidence/MvPolynomial.taylor_C/clean-Taylor-excerpt.tex.txt), [exact search](../evidence/MvPolynomial.taylor_C/rg-local-literature.json) |
| nCatLab | `site:ncatlab.org polynomial algebra morphism` | Regular map, polynomial and functional calculus pages returned; abstract substitution context, no distinct constant law used. [metadata](../evidence/MvPolynomial.taylor_C/web-3-metadata.json) |
| nLab | `site:ncatlab.org/nlab algebra homomorphism polynomial` | Polynomial and homomorphism pages returned. Direct polynomial access failed unsupported application/xhtml+xml. [search](../evidence/MvPolynomial.taylor_C/web-4-metadata.json), [access](../evidence/MvPolynomial.taylor_C/web-primary-metadata.json) |
| Stacks | `site:stacks.math.columbia.edu algebra homomorphism polynomial ring` | Polynomial-algebra construction context returned; no stronger distinct translation-constant theorem asserted. [metadata](../evidence/MvPolynomial.taylor_C/web-5-metadata.json) |
| MathOverflow | `site:mathoverflow.net polynomial translation constants automorphism` | Polynomial automorphism discussions; no stronger replacement used. [metadata](../evidence/MvPolynomial.taylor_C/web-6-metadata.json) |
| Recent arXiv, last five years | `site:arxiv.org polynomial Taylor shift 2022 2023 2024 2025 2026` | 2023–2026 Taylor approximation/regression papers are adjacent, not this elementary algebraic law. Supplementary direct Chen–Du–Fang arXiv 2204.06968 (2022, revised 2025) gives polynomial shift-equivalence context. [search](../evidence/MvPolynomial.taylor_C/web-7-metadata.json), [access](../evidence/MvPolynomial.taylor_C/web-primary-metadata.json) |

Primary [Zhang Lecture 6](https://ziyuzhang.github.io/ma40188/Lecture06.pdf), PDF page 1, Definition 3.16 and Lemma 3.18, was directly read: algebra homomorphisms preserve scalar constants, and pullback along polynomial maps preserves constants. The supplementary [Chen–Du–Fang abstract](https://arxiv.org/abs/2204.06968) explicitly uses shift equivalence of polynomials; it is context, not evidence for a new constant theorem. Direct FLINT access failed 403. Exploratory Stacks tags 00D3 and 00D4 were wrong (preordered sets/colimits), are explicitly rejected as supporting evidence, and remain recorded honestly; a follow-up search returned divided-power polynomial universal-property context, also not claimed to be this theorem. [Follow-up metadata](../evidence/MvPolynomial.taylor_C/web-stacks-followup-metadata.json).

Synthesis: translation/Taylor shift is coefficient-preserving polynomial substitution. The abstract standard is preservation of the scalar structure map by an algebra homomorphism. Textbook finite-variable field presentations are special contexts. No historical claim is inferred from the unavailable optional channel. The Lean generality is supported independently by the pinned algebra-homomorphism law, rather than extrapolating semiring details from field-specific sources.

## Phase 4a–b — generality and parameters

| Parameter/hypothesis | Current form | Audit |
|---|---|---|
| σ : Type u_1 | arbitrary variable type | No finiteness, inhabitedness, order or decidability to remove. |
| R : Type u_2 | arbitrary coefficient type | No concrete real/field restriction. |
| CommSemiring R | fixed parent-interface constraint | MvPolynomial/taylor/AlgHom over R use this interface. Removing commutativity of R changes representation; no mechanical weakening is claimed. |
| α : σ → R | arbitrary translation vector | Required to choose the named translate, although RHS and mathematical proof are independent of its coordinates. Broader form replaces the whole translate by arbitrary AlgHom f. |
| a : R | arbitrary scalar constant | Needed to choose the constant; no nonzero assumption. |

MAXIMALLY GENERAL relative to the fixed translation interface; zero verified assumption-drop opportunities. A verified expanded representation is already in mathlib: arbitrary `f : MvPolynomial σ R →ₐ[R] A`, with only `[Semiring A] [Algebra R A]`, satisfies `f (C a)=algebraMap R A a`. In particular, **A need not be commutative**. This does not claim arbitrary variable assignments into a noncommutative A define an aeval map. The supplied AlgHom already carries the required algebraic compatibility. The [isolated raw probe](../evidence/MvPolynomial.taylor_C/native-raw-executed.lean.txt) compiles both the broader law and independently written let-bound translation with `algHom_C _ _`; [raw receipt](../evidence/MvPolynomial.taylor_C/native-raw-success.json). This is not an unverified generalise-first proposal.

## Phase 4c — all modern-idiom questions

| # | Question | Result and downstream consequence |
|---|---|---|
| 1 | Typeclasses for mathematical preambles? | Already CommSemiring; no extra custom predicate or instance. |
| 2 | Filters/nets instead of sequences/metrics? | No topology. |
| 3 | Universal property instead of construction? | Abstract to an arbitrary AlgHom's scalar compatibility, already algHom_C/AlgHom.commutes. No translation construction needed. |
| 4 | Bundled substructure instead of closure predicates? | Already bundled AlgHom, so composition carries coefficient preservation. |
| 5 | Module/semiring instead of field hierarchy? | Already CommSemiring R; abstract codomain only Semiring A, verified in raw probe. This serves algebra homomorphisms to possibly noncommutative algebras. |
| 6 | Higher-category generalisation? | No concrete benefit identified for this scalar equation. |
| 7 | Arbitrary index instead of concrete ℕ/ℝ? | σ already arbitrary and universe independent. |
| 8 | Concrete-via-abstract diagnostic? | Fires: proof body `algHom_C _ _` contains zero `taylor` occurrences and no unfolding; it uses only the AlgHom interface. Exact abstract restatement compiled; [literal proof diagnostic](../evidence/MvPolynomial.taylor_C/proof-body-diagnostic.json). |
| 9 | False-generalisation guard? | Preserves intended scalar law by specializing f=taylor α; does not assert unconstrained substitution into a noncommutative target or weaken the source coefficient ring by changing polynomial objects. |

Modern idiom is available and already exists. It removes duplicated scalar-normalization rules for every particular algebra endomorphism and composes with AlgHom scalar compatibility. This is a real organizational advantage, but no missing theorem needs adding.

## Phase 4.5 — infrastructure risk

n/a: theorem. It introduces no instance diamond, reducibility setting, new data unfolding, instance priority, universe constructor or coercion path. Simp API effects are audited in Phase 6; they are not a newly introduced data/instance infrastructure risk.

## Phase 4.6 — all proof-strategy questions

| # | Strategy | Finding |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Elements versus substructure inclusion | The scalar equation is the intended normalization law; no inclusion to abstract. |
| 3 | Sequences versus nets | No convergence. |
| 4 | Explicit construction versus universal property | Already uses the algebra-homomorphism coefficient law directly. |
| 5 | Missing helper API | None: algHom_C is the complete law, with proof AlgHom.commutes. |

MATHLIB-IDIOMATIC proof strategy. The issue is duplicate specialization, not mathematical proof design. Cost does not affect the verdict.

## Phase 5 — five actual methods × three forms

All twelve tool calls and their complete responses are in [formal searches](../evidence/MvPolynomial.taylor_C/formal-search.json). Each method actually searched current (translation fixes constants), literature-standard (substitution preserves coefficients), and abstract (arbitrary AlgHom preserves the scalar map) forms.

| Method | Current | Literature | Abstract |
|---|---|---|---|
| Finder | Polynomial.taylor_C, expand_C | eval₂_C, aeval_C | algHom_C |
| Loogle | aeval/C constants query → aeval_C | aeval ?f (C ?r)=_ → aeval_C | algHom_C signature |
| LeanSearch | Polynomial.taylor_C | eval₂_C and evaluation/tower API | algHom_C |
| rg | taylor_C | aeval_C/eval₂_C | algHom_C/commutes |
| local name pattern | taylor_C | aeval_C | algHom_C |

Exact rg receipts: [current](../evidence/MvPolynomial.taylor_C/rg-current.json), [literature](../evidence/MvPolynomial.taylor_C/rg-literature.json), [abstract](../evidence/MvPolynomial.taylor_C/rg-abstract.json), [untruncated full-name](../evidence/MvPolynomial.taylor_C/rg-full-name.json). Local tools reported index unavailable despite source hits; this proves no absence. External indices may differ from the project pin. Pinned source, actual signatures and successful native specialization decide presence.

The complete replacement is **MvPolynomial.algHom_C**, `Mathlib/Algebra/MvPolynomial/Basic.lean:441`:

```lean
∀ {R σ} [CommSemiring R] {A} [Semiring A] [Algebra R A]
  (f : MvPolynomial σ R →ₐ[R] A) (r : R), f (C r) = algebraMap R A r
```

Its source proof is `f.commutes r`. [Pinned source](../evidence/MvPolynomial.taylor_C/MvPolynomial-Basic-excerpt.lean.txt). `MvPolynomial.aeval_C` at Eval.lean:590 is a narrower arbitrary-assignment variant requiring a commutative target: [source](../evidence/MvPolynomial.taylor_C/MvPolynomial-Eval-excerpt.lean.txt). `Polynomial.taylor_C` is a univariate analogue, not the same declaration: [source](../evidence/MvPolynomial.taylor_C/Polynomial-Taylor-excerpt.lean.txt). All three signatures and proofs were printed in the clean raw receipt. No project lemma is counted as a mathlib building block.

## Phase 5.5 — statement shape

Normal forms compared: `taylor α (C a)=C a`, `aeval f (C a)=algebraMap R A a`, and `g (C a)=algebraMap R A a` for any AlgHom g. All reduce evaluation away and put constants/structure-map images on the RHS. This is compatible with the canonical generic algHom_C simp law; no orthogonal equivalence needs introducing.

Syntactic forms actually tested: original exact term, raw let-bound translation, arbitrary AlgHom into a possibly noncommutative semiring algebra, typed equality in the actual named caller, and target-disabled `simp only [algHom_C, algebraMap_eq]`. The typed equality is directly usable as an rw entry in Index. The proof-relevant α is replaceable by f in the abstract representation, but α is not superfluous in the fixed named-translation statement. σ/R/CommSemiring R are needed to state that interface; a selects the constant. No argument/typeclass can simply be deleted from the same statement. Shape verdict SHIP-AS-STATED if retained locally; canonical reuse is algHom_C.

## Phase 6.0 — callers, inline audit and simp scope

[Caller search](../evidence/MvPolynomial.taylor_C/rg-callers.json), [caller inventory](../evidence/MvPolynomial.taylor_C/callers.json), [inline audit](../evidence/MvPolynomial.taylor_C/rg-inline.json).

| Caller | Use | Concrete replacement |
|---|---|---|
| Roth/Index.lean:197, Roth.index_C_mul | `rw [index, index, map_mul, taylor_C, ← smul_eq_C_mul, support_smul_eq hc]` | Replace taylor_C entry by `show taylor α (C c) = C c from algHom_C _ _`. |

All explicit callers 1; within declaring file 0; internal excluding declaring file 1; external-to-file files 1. There is no extra external downstream-library caller identified. No explicit independent multivariate Taylor-constant rederivation was found. Broader `simp [taylor,...]` identities and univariate Polynomial.aeval_C in Separation are different and are not counted as equivalent inline rederivations.

These are source-level counts, not opaque kernel or simp dependency closure. This is a simp API; absence of a named reference would not imply unused. In particular the named Index caller is affirmative usage evidence.

The complete [caller replay document](../evidence/MvPolynomial.taylor_C/native-caller-executed.lean.txt) contains a fresh namespace with the exact index definition body and the complete index_C_mul proof, replacing only the taylor_C rewrite by the typed algHom_C law. This avoids importing the heavy Index module; it is a duplicated definition-body plus full caller proof experiment, not a literal whole-module production migration. `support_smul_eq` is existing mathlib API. The target's simp attribute is disabled before that replay and before inline_simp/composite consumers. It is restored only afterward. [Clean complete receipt](../evidence/MvPolynomial.taylor_C/native-caller-success.json).

Both constant normalization and a product/power consumer work without `[taylor]`, using only `algHom_C`, `algebraMap_eq`, `map_mul`, `map_pow`. A production deletion should still run the full project build to discover any additional implicit consumers; this read-only assessment does not claim their absence.

## Phase 6 — independent composition and Phase 6b

The original follows by one existing-law specialization:

```lean
example {σ R : Type*} [CommSemiring R] (α : σ → R) (a : R) :
    MvPolynomial.taylor α (MvPolynomial.C a) = MvPolynomial.C a :=
  MvPolynomial.algHom_C _ _
```

The target replay compiles. The isolated raw probe imports no Roth modules, guards `#check_failure MvPolynomial.taylor_C`, and proves independently let-bound translation by that same term; it also proves the broader arbitrary-AlgHom law. Only the existing homomorphism property is used, and translation itself need not be unfolded. This is COMPOSABLE in the broad sense and specifically direct reuse of an existing law, hence NO-mathlib-has-it takes precedence over NO-composable.

The separate simp-only experiment is a normalization demonstration. A closing simp composition alone would be BORDERLINE under Phase 6b; that is not the basis for this verdict, since the independent one-call exact specialization meets the stronger existing-law criterion. No circular use of taylor_C contributes to accepted replacement proofs.

## Phase 7 — verdict and action

**NO-mathlib-has-it**. Existing `MvPolynomial.algHom_C` at Basic.lean:441 already states the entire coefficient-preservation law, in greater generality than translation and even than arbitrary commutative-target aeval. The exact term above, with one call and no normalization tactics, proves the current statement. This conclusion is checked independently of parent/sibling verdicts and does not decide whether a future upstream translation bundle should include a semantic constant simp alias.

Recommended refactor: delete the standalone specialized theorem; in the sole named caller Index:197 replace `taylor_C` by the typed equality shown in the table. The full copied caller proof was verified unchanged otherwise. Generic `algHom_C` already handles the demonstrated implicit constant/product/power simplifications, so this law does not require exposing the parent definition to simp. Validate the full project after production deletion to find remaining implicit consumers. This assessment makes no production changes.

Alternative local destination if a stable translation-specific simp API is intentionally retained: **Roth/Taylor.lean**, beside taylor, with a documented project API rationale. It is not junk or dead code. Upstream bundle design may choose its own constant law (as the univariate API does), but there is no new mathematical gap in this independently assessed law. No YES PR location/title/grouping/reviewer checklist or generalise-first ticket is warranted.

## Phase 8 — verification and handoff

All mandatory phases complete; theorem-only 2b and 4.5 exclusions justified; unresolved verification items `[]`. [Assessment](../evidence/MvPolynomial.taylor_C/assessment.json), [verification index](../evidence/MvPolynomial.taylor_C/verification.json), [overview entry](../evidence/MvPolynomial.taylor_C/overview-entry.json), [portable validator](../evidence/MvPolynomial.taylor_C/validate.py), [copy manifest](../evidence/MvPolynomial.taylor_C/copy-manifest.json). Accepted native target/raw/caller receipts are complete success, partial=false, with no errors/warnings and only standard propext/Classical.choice/Quot.sound axioms. There were no rejected native attempts for this declaration. Exact execution paths remain in native receipts. Current copy-manifest remains authoritative in scratch and integrated layouts; historical worker manifests never replace validation of current artifacts. Root acceptance remains pending until independent review.
