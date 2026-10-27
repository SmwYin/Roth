# MvPolynomial.taylor_apply — full mathlibable assessment

**NO-composable-from-mathlib.** Canonical declaration 54, `Roth/Taylor.lean:46–47`, assessed independently on 2026-10-27. This is the constitutive application equation for the local translation definition; its exact proof is kernel reflexivity after unfolding that definition. It contributes no further polynomial identity. The parent translation definition's BORDERLINE verdict is neither inherited nor counted as an existing mathlib declaration.

## Phase 0 — baseline and scope

The shared successful `lake build` completed 2467 jobs, exit 0. All 17 production source/pin SHA256 values were freshly compared with the baseline manifest and match. The declaration resolves and its original proof and a fresh direct `rfl` reproduction elaborate cleanly. No production files or pins were changed. See [build receipt](../evidence/MvPolynomial.taylor_apply/baseline-build.txt), [fresh input comparison](../evidence/MvPolynomial.taylor_apply/inputs.json), [native target receipt](../evidence/MvPolynomial.taylor_apply/native-target-success.json), and [exact executed persistent document](../evidence/MvPolynomial.taylor_apply/native-target-executed.lean.txt). The document includes older completed checks as well; the target-specific messages occur at lines 2306–2314.

The entire [declaring module](../evidence/MvPolynomial.taylor_apply/Taylor-module.lean.txt) was read: it packages translation as an algebra endomorphism, proves the Hasse coefficient theorem, and derives polynomial/evaluation Taylor expansions. This theorem is neither the coefficient theorem nor Taylor's expansion theorem. The native printer marks its existing proof `@[defeq]`; there is no `@[simp]` annotation on this source theorem. Standard axioms are exactly `propext`, `Classical.choice`, `Quot.sound`; no new axioms, sorry, raised limits, unsafe proofs, or native decision procedures are introduced.

## Phase 1 — comprehend

For a polynomial in any set of variables over a commutative semiring, applying the translation endomorphism with translation vector α means substituting each variable Xⱼ with Xⱼ + αⱼ. This equality exposes precisely how the local endomorphism was defined. It is not an assertion about derivative coefficients or convergence.

Full native type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R]
  (α : σ → R) (P : MvPolynomial σ R),
  (MvPolynomial.taylor α) P =
    (MvPolynomial.aeval fun j ↦ MvPolynomial.X j + MvPolynomial.C (α j)) P
```

The proof printed by Lean is `fun {σ} {R} [CommSemiring R] α P ↦ rfl`. The only project dependency in the statement is `MvPolynomial.taylor`; the proof uses its defining body, not another project theorem. The two independently polymorphic types parameterize the variable set and coefficient semiring. The translation vector and polynomial are arbitrary. There are no proposition hypotheses, finiteness assumptions, decidable equality assumptions, characteristic assumptions, or nontriviality assumptions.

## Phase 2 — preliminary checks

SMALL: an application/unfolding bridge, not a main mathematical result or new structure. Phase 2b's one-line definition test is n/a because this declaration is a theorem. Its `rfl` proof is not used as a reason to skip any later phase. Defeq, diamond and semantic-name exemptions for one-line definitions are n/a to this theorem. A separate semantic-API argument is considered in Phase 7: a named unfold equation could be offered with an eventual upstream translation API, but no present named consumer depends on this equation.

## Phase 3 — exhaustive literature

Each request and response status, SHA256 and byte count is archived as metadata; full web bodies are deliberately not saved. Returned URL query strings were removed from locators. All required named channels were exercised, including three distinct general queries. The protocol informally calls itself nine-channel but enumerates more rows: no synthetic channel has been invented to fix that label.

| Channel | Exact query or local operation | Result / standard form / limitation |
|---|---|---|
| General, specific | `multivariate polynomial translation P(X+a) substitution algebra homomorphism` | Polynomial translation appears as substitution; Buchacher–Kauers, *On the Problem of Separating Variables in Multivariate Polynomial Ideals*, Lemma 1, uses translation as a K-algebra automorphism. |
| General, broader | `polynomial algebra universal property substitution commutative semiring translation` | Bergman, *An Invitation to General Algebra and Universal Constructions*, discussion of free commutative algebras; Land, *Commutative Algebra*, Remark 2.9: assignments of generators induce unique algebra homomorphisms. |
| General, aliases | `Taylor shift polynomial translation operator Hasse derivatives definition` | Taylor shift and Hasse expansion are the relevant names. These identify the translation operation, not a separate application law beyond its definition. |
| ChatGPT math | n/a: `ask_chatgpt_math` unavailable | No external mathematical second opinion was fabricated. |
| Local references | `rg -n 'Taylor\|P_.*alpha\|translated' .mathlib-quality/references/clean.tex` | §4 Index, lines 501–549, especially line 547, defines Pα(X)=P(X+α) before the Hasse coefficient interpretation. |
| nLab | `site:ncatlab.org/nlab polynomial algebra free commutative algebra evaluation` | Indexed *polynomial* page describes free commutative R-algebras and substitution. Direct fetch failed with 400, unsupported `application/xhtml+xml`; rely only on returned index excerpts for that page. |
| nCatLab | `site:ncatlab.org polynomial ring universal property substitution` | Returned nLab polynomial/universal-construction pages. This is the same host, not independent corroboration. Universal properties explain substitution; no distinct higher-category equation is needed here. |
| Stacks Project | `site:stacks.math.columbia.edu polynomial ring universal property evaluation` | Tag 04EB, proof lines 27–42, uses polynomial rings on arbitrary generators and generator assignments into algebras. This contextual source concerns thickenings and is not a direct Taylor-application theorem. |
| MathOverflow | `site:mathoverflow.net polynomial translation Hasse derivative Taylor` | Question 82970, arbitrary-field algebraic Taylor expansions, lines 36–41, distinguishes characteristic-free polynomial expansions from factorial formulas. It does not add content to this definitional equation. |
| Recent arXiv | `site:arxiv.org Hasse derivatives polynomial shift translation 2022 2023 2024 2025 2026` | Broad initial results were noisy and included a March 2021 skew-polynomial paper outside the five-year window; not counted as recent evidence. |
| Recent arXiv retry | `site:arxiv.org "Hasse" "Taylor" "2025"`; `site:arxiv.org "Hasse derivatives" "2023" polynomial` | Returned empty. This is not evidence of absence. |
| Recent arXiv refined | `site:arxiv.org/abs/ "Hasse derivatives" after:2021-10-27`; `site:arxiv.org "Polynomials, Divided Differences, and Codes"` | Venkitesh, arXiv:2412.01755, 2024-12-02, is within 2021-10-27–2026-10-27 and discusses characteristic-independent Taylor-like expansions via divided differences. Newer returned incidence/interpolation applications add context but do not motivate a separate unfolding theorem. |

Receipts: [three general queries](../evidence/MvPolynomial.taylor_apply/web-0-metadata.json), [nLab](../evidence/MvPolynomial.taylor_apply/web-1-metadata.json), [nCatLab](../evidence/MvPolynomial.taylor_apply/web-2-metadata.json), [Stacks](../evidence/MvPolynomial.taylor_apply/web-3-metadata.json), [MathOverflow](../evidence/MvPolynomial.taylor_apply/web-4-metadata.json), [initial arXiv](../evidence/MvPolynomial.taylor_apply/web-5-metadata.json), [empty retry](../evidence/MvPolynomial.taylor_apply/web-6-metadata.json), [primary access and recent retry](../evidence/MvPolynomial.taylor_apply/web-7-metadata.json), [local reference locator](../evidence/MvPolynomial.taylor_apply/local-literature.json).

Primary locators: [Buchacher–Kauers](https://www.algebra.uni-linz.ac.at/people/mkauers/publications/buchacher24a.pdf), [Bergman](https://web.osu.cz/~Zusmanovich/teach/2024-cat/an-invitation-to-general-algebra-and-universal-constructions.pdf), [Land](https://www.mathematik.uni-muenchen.de/~zhykhovi/Algebra2-SoSe2023/Algebra2-Script.pdf), [nLab polynomial](https://ncatlab.org/nlab/show/polynomial), [Stacks tag 04EB](https://stacks.math.columbia.edu/tag/04EB), [MathOverflow question](https://mathoverflow.net/questions/82970/algebraic-taylor-expansion-for-polynomials-rational-functions-with-coefficie), [Venkitesh 2024](https://arxiv.org/abs/2412.01755).

Literature synthesis: the standard concept is polynomial translation/Taylor shift, viewed as substitution induced by an assignment of free generators. Sources vary between finite-variable field/ring settings and arbitrary free commutative algebras. The local theorem correctly uses a characteristic-free commutative semiring and arbitrary variable type. No literature disagreement or separate mathematical statement beyond the chosen definition was found. This is a positive structural observation, not an absence claim from unsuccessful searches.

## Phase 4a–4b — every parameter and generality

| Parameter | Current form | Standard / candidate broader form | Audit conclusion |
|---|---|---|---|
| σ | `Type u_1` | Arbitrary set of generators | Already arbitrary; includes empty and infinite types. No Fintype/DecidableEq to remove. |
| R | `Type u_2` | Coefficient carrier | Already arbitrary and in an independent universe. |
| semiring instance | `CommSemiring R` | Literature often ring or field | Already weaker than those sources. Required by the fixed `taylor` and `aeval` algebra-endomorphism interfaces, even though the equality proof itself is reflexive. Dropping it would change the parent interface, not weaken this theorem alone. No successful strict weakening is claimed. |
| α | `σ → R` | Arbitrary translation vector | No restrictions to drop. Allowing α in another R-algebra changes the source/target representation to a cross-algebra substitution. |
| P | `MvPolynomial σ R` | Arbitrary formal polynomial | No degree, support, coefficient or nonzero condition to remove. |
| proposition hypotheses | None | None needed | No drop-test candidates. |

MAXIMALLY GENERAL relative to the fixed parent/interface; zero verified hypothesis weakenings. The more general arbitrary-assignment substitution is already `MvPolynomial.aeval`, and the native raw experiment checks application reflexivity for `f : σ → MvPolynomial τ R` with σ and τ arbitrary. It does not provide a newly discovered theorem or a parent generalization, and is not counted as an existing named lemma. Semiring-only univariate translation is confirmed separately, but its `Polynomial`/`LinearMap` representation does not mechanically weaken the multivariate algebra-hom theorem.

## Phase 4c — all nine modern-idiom checks

| # | Question | Answer, concrete consequence |
|---|---|---|
| 1 | Typeclasses in place of preambles? | No change: `CommSemiring` is already an instance and there are no bundled proposition hypotheses. |
| 2 | Filters/topology in place of sequences/metrics? | No: formal substitution has no topology or limiting process. |
| 3 | Universal property instead of construction? | Already uses the free-algebra evaluation `MvPolynomial.aeval`. Its generic API supplies variable and composition laws; redoing the construction categorically would add no application theorem. |
| 4 | Bundled substructure instead of closure predicates? | No: the parent is already an `AlgHom`; there is no set-with-closure predicate. |
| 5 | Weaken field/vector/metric hierarchy? | No such specialization; already a commutative semiring. The fixed interface prevents a theorem-only weakening to noncommutative coefficients. |
| 6 | Higher-categorical extension? | No mathematical need for a higher-category law; this is an equality of applied polynomial substitutions. |
| 7 | Concrete index to abstract monoid/group? | No concrete index: σ is already arbitrary. The multi-exponent ℕ infrastructure belongs to the polynomial representation, not an unnecessary theorem binder. |
| 8 | Concrete-via-abstract proof-body diagnostic? | Fires syntactically: the entire proof is `rfl`, containing zero occurrences of `taylor`. The abstraction is reflexivity of an applied substitution (raw `universal` experiment). No residual algebraic argument remains after unfolding, so there is no new abstract mathematical theorem to extract. |
| 9 | False-generalisation guard? | An arbitrary substitution is not necessarily a translation. Retain the specialization Xⱼ+C(αⱼ) when discussing translation. Noncommutative/free-associative polynomials or an additive function-space action change the object; reject those as automatic weakenings. |

Modern idiom available as a *new contribution*: no. Existing free-algebra evaluation is already the right abstraction. It supplies `aeval_X`, `comp_aeval`, and `aeval_unique`, while this equation only exposes the chosen parent body. The raw universal reflexivity probe is a diagnostic, not an extra helper counted toward a replacement.

## Phase 4.5 — infrastructure risk

n/a: declaration kind is theorem. Each of the six definition-only rows (typeclass diamonds, reducibility leak, noncanonical unfolding, instance priority collisions, universe-polymorphism infrastructure, coercion ambiguity) is n/a because the theorem creates neither a data definition nor an instance/coercion path. It records an existing definitional equality. Parent-definition design remains a separate assessment.

## Phase 4.6 — all five proof-strategy checks

| # | Check | Finding / alternative / cost |
|---|---|---|
| 1 | ε–δ versus filters | No topology; n/a. |
| 2 | Element algebra versus subobjects | No element chase or inclusion argument; `rfl` directly expresses unfolding. No switch needed. |
| 3 | Sequences versus nets | No limits; n/a. |
| 4 | Construction versus universal property | `aeval` already provides the universal substitution; this proof does not construct one. No switch needed. |
| 5 | Missing helper API | None required. The kernel closes the exact equation, so a new normalization theorem is unnecessary. |

MATHLIB-IDIOMATIC proof strategy. Optimal proof length does not by itself establish that a separate public theorem is necessary.

## Phase 5 — five actual search methods on three forms

Every external result is saved in [complete formal-search receipts](../evidence/MvPolynomial.taylor_apply/formal-search.json). Three forms were current translation/application, literature Taylor shift/substitution, and abstract free-algebra evaluation.

| Method | Current | Literature-standard | Abstract |
|---|---|---|---|
| Lean-Finder | Multivariate Taylor translation application = aeval at X plus constant; returns univariate `Polynomial.taylor_apply` | Polynomial P(X+a) substitution; univariate apply theorem | Algebra evaluation/substitution; `MvPolynomial.aeval_eq_eval₂Hom` and evaluation API |
| Loogle | `MvPolynomial.aeval, MvPolynomial.X`; `aeval_X` and generic substitutions | `Polynomial.taylor, Polynomial.comp`; exact univariate analogue | `MvPolynomial.aeval, MvPolynomial.eval₂`; `aeval_def` |
| LeanSearch | Same current natural-language form; univariate `taylor_apply` | Literature query; polynomial composition and translation | Abstract query; `MvPolynomial.aeval` and evaluation API |
| rg pinned source | [current](../evidence/MvPolynomial.taylor_apply/rg-current.json) | [literature](../evidence/MvPolynomial.taylor_apply/rg-literature.json) | [abstract](../evidence/MvPolynomial.taylor_apply/rg-abstract.json) |
| local name search | `taylor_apply`: own target plus univariate theorem | `Polynomial.taylor_apply`: univariate theorem plus name substring matches | `MvPolynomial.aeval_def`: pinned generic evaluation bridge |

Local search reports `index: unavailable`; its source matches establish presence only. Empty results would not establish absence. External indexes may differ from the pin. The pinned exact native checks, not a current web index, decide the candidates' signatures and proofs.

Pinned candidate contrast:

* `Polynomial.taylor_apply`, `Mathlib/Algebra/Polynomial/Taylor.lean:43`: `[Semiring R]`, `taylor r f = f.comp (X + C r)`, proof `rfl`. Its parent is a `LinearMap`. This is an authentic analogous unfold API and a reason an upstream translation bundle might choose such a theorem. It is not the exact multivariate theorem; no unproved identification between the two polynomial representations is asserted.
* `MvPolynomial.aeval_def`, `Mathlib/Algebra/MvPolynomial/Eval.lean:572`: `[CommSemiring R] [CommSemiring S₁] [Algebra R S₁]`, `aeval f p = eval₂ (algebraMap R S₁) f p`, proof `rfl`. It exposes the *next* evaluation implementation layer, not `taylor` to `aeval`.
* `MvPolynomial.aeval`, same file line 569, already supplies the bundled substitution in the parent body; `MvPolynomial.aeval_X`, line 588, supplies variable substitution, not the target's full application equation.

See [pinned multivariate excerpt](../evidence/MvPolynomial.taylor_apply/MvPolynomial-Eval-excerpt.lean.txt), [univariate excerpt](../evidence/MvPolynomial.taylor_apply/Polynomial-Taylor-excerpt.lean.txt), [mathlib hashes](../evidence/MvPolynomial.taylor_apply/mathlib-inputs.json), [full-name search](../evidence/MvPolynomial.taylor_apply/rg-full-name.json), [raw exact probes](../evidence/MvPolynomial.taylor_apply/native-raw-executed.lean.txt), and [complete raw receipt](../evidence/MvPolynomial.taylor_apply/native-raw-success.json). `#check_failure MvPolynomial.taylor_apply` succeeds in the mathlib-only import environment. This supports the scoped missing-name claim; it does not claim mathematical absence from all equivalent representations.

Conclusion: exact old declaration not supplied by the pinned mathlib environment; existing `aeval` supplies its whole defining operation. The target is a zero-theorem-call definitional bridge, rather than a missing mathematical law. NO-mathlib-has-it would overstate the univariate analogy.

## Phase 5.5 — statement shape

Normal form: OK. Equivalent descriptions include application of the algebra hom `aeval`, ring evaluation `eval₂ (algebraMap ...)`, and the unapplied hom equality `taylor α = aeval (...)`. The chosen RHS stays at the algebra-evaluation layer, which is the appropriate substitution API. Expanding further to sums or raw coefficients would obscure the operation. `aeval_def` explains the alternative ring-evaluation form.

Syntactic generality: OK. Application equality is convenient for `rw`; an unapplied hom equality could rewrite more generally but has no demonstrated blocked caller. Raw `universal` checks the arbitrary-variable-target applied form and `inline` checks the defining-parent form. No signature alteration is needed to justify the present assessment.

Superfluous arguments: NONE. σ and R determine the polynomial type, `CommSemiring R` supplies the fixed parent/evaluation interface, α determines translation, and P supplies the input. Reflexivity of the proof is not evidence that the typeclass can be removed from the statement. Overall: SHIP-AS-STATED if the optional theorem is retained; this is a shape conclusion, not an inclusion verdict.

## Phase 6.0 — callers and inline audit

Zero explicit named callers, both in the declaring file and outside it. The only target-spelling occurrence is its own declaration. The other project `taylor_apply` occurrence, `Roth/Index.lean:243`, explicitly names **Polynomial.taylor_apply** and is excluded. See [complete caller search](../evidence/MvPolynomial.taylor_apply/rg-callers.json), [caller accounting](../evidence/MvPolynomial.taylor_apply/callers.json), [Index source](../evidence/MvPolynomial.taylor_apply/Index-module.lean.txt), and [inline search](../evidence/MvPolynomial.taylor_apply/rg-inline.json).

The equivalent implementation expansion is already performed inline in `eval_taylor` line 143, `taylor_taylor` line 148, `taylor_zero` line 153, `taylor_map` line 159, and `taylor_rename` line 166, via `simp [taylor, ...]`. These prove stronger laws; they do not duplicate the entire target theorem as separate statements. They demonstrate present consumers access the definition directly. The residual mathematics in those proofs is not claimed composable merely because their simp calls close.

This is a source-level audit, not an exhaustive opaque kernel or simp dependency closure. The theorem lacks a simp annotation, so zero named references is not being used to infer that all possible simplification APIs are dead. No known external consumer was established.

## Phase 6 — actual composition experiments

COMPOSABLE, in the degenerate zero-named-mathlib-theorem-call case. The exact original statement was replayed as:

```lean
theorem replay (α : σ → R) (P : MvPolynomial σ R) :
    MvPolynomial.taylor α P =
      MvPolynomial.aeval (fun j ↦ MvPolynomial.X j + MvPolynomial.C (α j)) P := rfl
```

This target replay does not cite `MvPolynomial.taylor_apply`, any downstream simp theorem, or another project theorem. The dependency on the project parent is only its defining equation. It is not counted as a mathlib lemma.

The isolated mathlib-only `TaylorApplyRaw.inline` experiment writes exactly that body in a let-bound algebra hom and closes by `rfl`; `TaylorApplyRaw.universal` checks arbitrary-assignment application reflexivity. Both succeed with standard axioms, no errors/warnings, `partial=false`, no failed dependencies. The accepted raw source and receipt linked above preserve the exact snippets. Newly named scratch theorems are test declarations, not existing-library building blocks. The actual existing polynomial construction is `MvPolynomial.aeval`; its application is ordinary AlgHom function coercion, and equality is `Eq.refl` after definitional unfolding.

Trying `Polynomial.taylor_apply` as if it directly matched would compare different types; this is an analogy, not an accepted replacement term. `MvPolynomial.aeval_def` expands the wrong layer for the exact desired RHS. Neither is necessary: no normalization premise is missing because the target's own defining equation is precisely the RHS.

This verdict does not invoke the Phase 6b borderline rule for a closing `simp [definitions...]` composition: the accepted target derivation is literal kernel reflexivity and introduces no algebraic reasoning. The listed downstream simp proofs are evidence of direct-definition use, not the replacement proof.

## Phase 7 — verdict and actionable alternative

**NO-composable-from-mathlib**, independently of the parent's BORDERLINE assessment. Literature confirms a standard translation operation, and generic mathlib `aeval` implements the substitution. At the application equation there is no further mathematical content: direct `rfl` proves the exact statement without invoking another theorem. Zero named callers and five current stronger-law proofs that already unfold `taylor` make a separate required bridge unsupported by present usage. This is not a cost-based downgrade or a claim that named `rfl` lemmas are never useful.

The strongest counterargument is API stability: mathlib already offers univariate `Polynomial.taylor_apply`, also proved by `rfl`, and an upstream multivariate translation API could reasonably offer a parallel documented unfold law. That precedent is recorded rather than mislabeled as an exact hit. The parent name can encapsulate the semantic operation while this particular theorem continues to expose its exact `aeval` implementation; preserving that implementation-facing rewrite is an optional API packaging decision, not additional mathematics established here. The full audit supplies a concrete zero-call derivation and no present rewrite consumers, so there is no unresolved mathematical or verification issue requiring a BORDERLINE verdict for this theorem alone.

Existing building blocks and paths: `MvPolynomial.aeval` in `Mathlib/Algebra/MvPolynomial/Eval.lean`, standard algebra-hom application/coercion, and kernel equality reflexivity. `MvPolynomial.aeval_def` and `Polynomial.taylor_apply` are relevant contrast APIs, not falsely counted as exact matches. The only project item being unfolded is `MvPolynomial.taylor`'s own body.

Refactor plan: remove `Roth/Taylor.lean:45–47` (docstring and unused theorem) if applying the NO recommendation. There are **zero** explicit callers to update; retain the five stronger-law proofs unchanged because they already expand the parent directly. For a future exact use of the application equation, use `rfl` as shown above, or explicitly unfold `MvPolynomial.taylor` when rewriting an expression in a larger proof. Do not edit the qualified univariate call in `Roth/Index.lean:243`.

Alternative local destination: retain the small documentation/unfold lemma in `Roth/Taylor.lean` if project API discoverability is valued, without presenting it as a standalone mathematical contribution. If a future upstream translation definition is accepted with a bundled API, maintainers may elect to include the analogous equation there for consistency. No upstream PR location/title/grouping/reviewer workflow is activated by this NO verdict. Production remains unchanged in this read-only assessment.

## Phase 8 — consolidated report and gates

All phases 0, 1, 2, 3, 4a, 4b, 4c, 4.5, 4.6, 5, 5.5, 6.0, 6, 7 and 8 are complete; definition-only checks are justified n/a above. Baseline hashes match, native checks are complete and clean, exact source snippets and receipts are retained, all required literature channels and three-form formal methods ran, all explicit caller counts and the univariate exclusion are documented, and no claims of unverified weakening or search-proved mathematical absence remain. `unresolved=[]`; root acceptance is pending independent review.

Machine-readable companions: [assessment](../evidence/MvPolynomial.taylor_apply/assessment.json), [verification](../evidence/MvPolynomial.taylor_apply/verification.json), [overview entry](../evidence/MvPolynomial.taylor_apply/overview-entry.json), [portable read-only validator](../evidence/MvPolynomial.taylor_apply/validate.py), and [current copy manifest](../evidence/MvPolynomial.taylor_apply/copy-manifest.json). The validator resolves local report links against the scratch evidence directory and validates the current copy manifest in both scratch and integrated layouts. Historical worker manifests, if preserved by root, never replace current validation. Credential guard is included in validation.
