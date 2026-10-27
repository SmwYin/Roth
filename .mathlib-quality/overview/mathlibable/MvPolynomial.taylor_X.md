# MvPolynomial.taylor_X — full mathlibable assessment

**NO-mathlib-has-it**. The existing, more general `MvPolynomial.aeval_X` proves the original statement directly, without a rewrite or closing simplification. This is an independent assessment of canonical declaration 55, `Roth/Taylor.lean:51`; neither the parent's BORDERLINE nor declaration 54's NO-composable verdict is inherited. Production sources and pins remain unchanged.

## Phase 0 — baseline and scope

The successful baseline was `lake build`, exit 0, 2467 jobs, no reported errors or warnings. All 17 sources/pins freshly match the baseline hashes: [baseline](../evidence/MvPolynomial.taylor_X/baseline-build.txt), [fresh checks](../evidence/MvPolynomial.taylor_X/inputs.json), [hash summary](../evidence/MvPolynomial.taylor_X/input-hash-check.json). The entire [declaring module](../evidence/MvPolynomial.taylor_X/Taylor-module.lean.txt), including its private caller and helper proofs, was read. The theorem has no sorry and has `@[simp]`. Canonical metadata agrees: [canonical entry](../evidence/MvPolynomial.taylor_X/canonical-entry.json), [ordered entry](../evidence/MvPolynomial.taylor_X/order-entry.json).

Instructions consulted: installed mathlib-quality SKILL.md; commands/mathlibable.md in full; mathlib-search.md, mathlibable-verdicts.md, generalisation-patterns.md, mathlib-review-stages.md; worker contract. Native checks were run serially by root in its persistent warm document and mathlib-only pool. Exact whole executed sources, not reconstructed excerpts, accompany the receipts.

## Phase 1 — statement and proof

Translation substitutes each variable by that variable plus the corresponding scalar. Therefore the translated generator X_j is X_j + α_j. This is a law of substitution on generators; it does not involve Taylor coefficients or Hasse derivatives.

Full native elaborated type:

```lean
∀ {σ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (α : σ → R) (j : σ),
  (MvPolynomial.taylor α) (MvPolynomial.X j) = MvPolynomial.X j + MvPolynomial.C (α j)
```

σ is an arbitrary variable type; R an arbitrary commutative semiring; α an arbitrary scalar assignment; j any variable. There are no finite-dimensional, nonzero, characteristic, decidability, or field hypotheses. The definition of `taylor` is `aeval (fun j ↦ X j + C (α j))`; the source proof is exactly `aeval_X _ _`. [Target receipt](../evidence/MvPolynomial.taylor_X/native-target-success.json) prints both the full type and that exact proof. [Target executed source](../evidence/MvPolynomial.taylor_X/native-target-executed.lean.txt).

## Phase 2 — preliminary checks

SMALL: a generator evaluation helper, not a new structure or module main result. The person-derived parent name does not turn this substitution law into the Taylor expansion theorem. Phase 2b is n/a: this is a theorem, not a one-line data definition. The short proof is examined independently in Phase 6.

## Phase 3 — exhaustive literature

Each evidence file preserves exact requests, returned-response SHA256 and byte count, titles/URLs/locators, and original concise summaries, without article/search-result bodies. Returned URL query strings are conservatively omitted from locator lists; exact response hashes refer to the original responses. This avoids preserving signed URLs. The initial first-query invocation encountered an orchestration `TextEncoder` error after the response; it was repeated and the retained request/response metadata below records the successful repeat.

| Channel | Exact query or locator | Finding and evidence |
|---|---|---|
| General web, specific | `"multivariate polynomial" translation "variables" substitution` | Buchacher–Kauers, *On the Problem of Separating Variables in Multivariate Polynomial Ideals* (2024), Lemma 1: translation is a polynomial-algebra map. [metadata](../evidence/MvPolynomial.taylor_X/web-0-metadata.json) |
| General web, general | `"polynomial algebra" "universal property" evaluation generators` | Polynomial algebra and arbitrary assignments, not derivative identities. [metadata](../evidence/MvPolynomial.taylor_X/web-1-metadata.json) |
| General web, alias | `"Taylor shift" polynomial "X" translation` | Taylor shift as polynomial substitution; FLINT primary documentation among results. [metadata](../evidence/MvPolynomial.taylor_X/web-2-metadata.json) |
| ChatGPT mathematical MCP | Standard form/generality/history query | n/a: ask_chatgpt_math unavailable; no invented response. |
| Local references | clean.tex §4, lines 501–550 | Translation P_α(X)=P(X+α) after the Taylor theorem; stronger real/finite assumptions belong to the surrounding application. [local summary](../evidence/MvPolynomial.taylor_X/local-literature.json), [excerpt](../evidence/MvPolynomial.taylor_X/clean-Taylor-excerpt.tex.txt), [exact rg](../evidence/MvPolynomial.taylor_X/rg-local-literature.json) |
| nCatLab | `site:ncatlab.org polynomial algebra universal property` | Abstract context searched; spectral symmetric algebra and other adjacent sources returned, no new generator law identified. [metadata](../evidence/MvPolynomial.taylor_X/web-3-metadata.json) |
| nLab | `site:ncatlab.org/nlab polynomial ring free commutative algebra` | Polynomial page returned in search. Direct page access failed: unsupported application/xhtml+xml. No claim to have read its full text. [search metadata](../evidence/MvPolynomial.taylor_X/web-4-metadata.json), [access metadata](../evidence/MvPolynomial.taylor_X/web-primary-metadata.json) |
| Stacks | `site:stacks.math.columbia.edu polynomial ring universal property` | Lemma 10.149.1 (04EB), proof first paragraph, uses an arbitrary-set polynomial ring and map sending x_i to z_i. This is supporting generator-map context, not the assertion that this unramified-map lemma is our theorem. [search](../evidence/MvPolynomial.taylor_X/web-5-metadata.json), [access](../evidence/MvPolynomial.taylor_X/web-primary-metadata.json) |
| MathOverflow | `site:mathoverflow.net polynomial translation shift automorphism` | Automorphism discussions found; no stronger replacement law used. [metadata](../evidence/MvPolynomial.taylor_X/web-6-metadata.json) |
| Recent arXiv | `site:arxiv.org polynomial Taylor shift multivariate 2022 2023 2024 2025 2026` | Chen–Du–Fang arXiv 2204.06968 (2022 v1; 2025 v3), shift equivalence. Current title is *Symbolic Summation of Multivariate Rational Functions*, differing from the indexed v1 title. Both dates fall within the last five years. [search](../evidence/MvPolynomial.taylor_X/web-7-metadata.json), [access](../evidence/MvPolynomial.taylor_X/web-primary-metadata.json) |

The primary [Stacks proof](https://stacks.math.columbia.edu/tag/04EB) and [Chen–Du–Fang paper](https://arxiv.org/abs/2204.06968) support the arbitrary-generator substitution and shift context. Buchacher–Kauers full PDF timed out on direct access; its Lemma 1 evidence here is limited to the returned search excerpt. No history of this elementary law was inferred from the unavailable optional channel.

Literature synthesis: polynomial translation/Taylor shift is the standard operation, with plus-shift convention in this project. The most general relevant generator rule is evaluation at an arbitrary assignment into a commutative R-algebra. Familiar field/finite-variable presentations are applications; neither finiteness nor differentiation is part of this rule. Translation over semirings need not be invertible, and no inverse is asserted here.

## Phase 4a–b — generality

| Parameter | Existing form | Audit |
|---|---|---|
| σ : Type u_1 | arbitrary, independent universe | No finiteness, decidability, order, or distinguished indexing needed. |
| R : Type u_2 | arbitrary coefficients | No concrete-ring restriction. |
| CommSemiring R | parent-interface constraint | Needed to state this existing MvPolynomial/taylor/AlgHom interface. Dropping commutativity requires a different representation, not a verified mechanical weakening. |
| α : σ → R | arbitrary values | Every coordinate is permitted. Can expand to an arbitrary substitution f into an arbitrary R-algebra A; that expansion is exactly existing aeval_X. |
| j : σ | arbitrary variable | Necessary to select the generator and assigned value. |

MAXIMALLY GENERAL relative to the fixed parent interface; zero verified assumption-drop opportunities. There is a verified broader **representation**, not a claim of a typeclass weakening: [raw executed source](../evidence/MvPolynomial.taylor_X/native-raw-executed.lean.txt) proves `aeval (R := R) f (X j) = f j` for arbitrary commutative R-algebra A with exactly `MvPolynomial.aeval_X _ _`, and independently proves the raw let-bound translation specialization. [Raw receipt](../evidence/MvPolynomial.taylor_X/native-raw-success.json). This broader result already exists, so the false-positive generalise-first route does not apply.

## Phase 4c — modern idiom (all nine questions)

| # | Question | Result and downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of preambles? | Already uses CommSemiring; no new class. |
| 2 | Filters instead of sequences/metrics? | No topology or convergence. |
| 3 | Universal property instead of construction? | Yes, already represented by `aeval` and its generator law. Arbitrary R-algebra targets compose with `aeval_unique` and algebra maps. No new class or theorem needed. |
| 4 | Bundled substructures instead of closure sets? | Already an AlgHom; no closure predicates. |
| 5 | Module/semiring hierarchy instead of field-specific? | Already CommSemiring, weaker than the local real-coefficient application. No verified weakening of this parent interface. |
| 6 | Higher category restatement? | No concrete downstream advantage for one generator equation. |
| 7 | Abstract index instead of ℕ/ℤ/ℝ? | σ already arbitrary. |
| 8 | Concrete-via-abstract proof diagnostic? | Fires: source body `aeval_X _ _` contains zero occurrences of `taylor` and no unfolding rewrite. Its mathematical content is arbitrary substitution on generators. Native raw universal test verifies this exact abstraction. |
| 9 | False-generalisation guard? | Arbitrary assignments preserve specialization to the same translation by f j=X j+C(α j); arbitrary noncommutative targets without commuting-generator data would change the free commutative algebra problem and are rejected. |

Modern idiom available as the **already existing** aeval API. Concrete benefit is arbitrary-target evaluation and composition; no missing modern theorem is proposed.

## Phase 4.5 — infrastructure risk

n/a, theorem. It introduces no typeclass diamond, reducibility setting, new data unfolding, instance priority, universe constructor, or coercion path. Its simp annotation is an API consideration audited in Phase 6, not a data/instance infrastructure risk.

## Phase 4.6 — proof strategy

| # | Strategy question | Finding |
|---|---|---|
| 1 | ε–δ versus filters? | No topology. |
| 2 | Elements versus substructure inclusions? | Generator equation is the intended pointwise law; no inclusion proof to abstract. |
| 3 | Sequences versus nets? | No analysis. |
| 4 | Construction versus universal property? | Already uses the universal-property evaluation law directly. |
| 5 | Missing helper API? | None: aeval_X supplies the complete law. |

MATHLIB-IDIOMATIC proof strategy; standalone duplication is the issue. No cost-based decision is used.

## Phase 5 — five actual methods × three forms

All twelve external/local calls and raw complete responses are in [formal searches](../evidence/MvPolynomial.taylor_X/formal-search.json). Current form: translation on X_j; literature form: substitution evaluated on a generator; abstract form: the free commutative algebra evaluation law. All three were actually queried by every method.

| Method | Current | Literature | Abstract |
|---|---|---|---|
| Finder | Polynomial.taylor_X and related univariate API | eval₂_X, eval₂Hom_X' | FreeAlgebra lift and Algebra.Generators near matches |
| Loogle | aeval/X constants find aeval_X | aeval application pattern attempted | eval₂ generator pattern finds eval₂_X |
| LeanSearch | Polynomial Taylor API | evaluation/substitution API | FreeAlgebra/Generators context |
| rg | taylor_X/taylor_X_pow | aeval_X/aeval_unique | eval₂_X/aeval_unique |
| local name index | taylor_X | aeval_X | eval₂_X (tool returns broader eval names) |

Exact rg receipts: [current](../evidence/MvPolynomial.taylor_X/rg-current.json), [literature](../evidence/MvPolynomial.taylor_X/rg-literature.json), [abstract](../evidence/MvPolynomial.taylor_X/rg-abstract.json), [untruncated full-name](../evidence/MvPolynomial.taylor_X/rg-full-name.json). Local tools report `index: unavailable` despite source matches; these calls establish no absence claim. External versions may differ from the project pin; pinned source and native signatures settle positive candidates.

Found in mathlib as **MvPolynomial.aeval_X**, more general form, at `Mathlib/Algebra/MvPolynomial/Eval.lean:587`:

```lean
∀ {R S₁ σ} [CommSemiring R] [CommSemiring S₁] [Algebra R S₁]
  (f : σ → S₁) (s : σ), (MvPolynomial.aeval f) (MvPolynomial.X s) = f s
```

Its proof is `eval₂_X _ _ _`; the latter permits an arbitrary coefficient ring homomorphism. [Pinned source excerpt](../evidence/MvPolynomial.taylor_X/MvPolynomial-Eval-excerpt.lean.txt), [native raw print](../evidence/MvPolynomial.taylor_X/native-raw-success.json). `Polynomial.taylor_X` at `Mathlib/Algebra/Polynomial/Taylor.lean:47` is a genuine univariate analogy (Semiring R, proof X_comp), not an identical multivariate declaration. [Pinned analogous source](../evidence/MvPolynomial.taylor_X/Polynomial-Taylor-excerpt.lean.txt), [candidate checks](../evidence/MvPolynomial.taylor_X/native-candidates-success.json), [exact candidate source](../evidence/MvPolynomial.taylor_X/native-candidates-executed.lean.txt). Unrelated FreeAlgebra hits are not replacements.

## Phase 5.5 — statement shape

Normal forms compared: `taylor α (X j)=X j+C(α j)`; `aeval f (X j)=f j`; `eval₂ φ f (X j)=f j`. Evaluation-free RHS respects simp orientation. The current shape is appropriate if retaining a local translation API; the library's canonical generic generator law is already aeval_X. Syntactic alternatives actually tested: the original statement with an explicit exact term, raw let-bound translation, arbitrary algebra-target evaluation, and a typed rewrite in the real caller. The explicit R argument is necessary in the general raw test to disambiguate the coefficient ring.

Superfluous audit: σ, R, CommSemiring R are needed to state the fixed polynomial/translation objects; α occurs on both sides; j selects the variable. None are removable. Shape verdict SHIP-AS-STATED **if retained locally**, no orthogonal equivalence or superfluous argument to repair. The NO recommendation is reuse of an existing more general law.

## Phase 6.0 — all callers and implicit simp scope

[Exact source search](../evidence/MvPolynomial.taylor_X/rg-callers.json), [caller inventory](../evidence/MvPolynomial.taylor_X/callers.json), [inline audit](../evidence/MvPolynomial.taylor_X/rg-inline.json).

| Caller | Use | Refactor |
|---|---|---|
| Roth/Taylor.lean:114, private coeff_taylor_monomial_single_add_aux | Named token in `rw [monomial_single_add, map_mul, map_pow, taylor_X, hXC, ...]` | Replace token by `show taylor α (X i) = X i + C (α i) from aeval_X _ _`. |

All explicit caller count 1; within declaring file 1; external 0; internal count excluding declaring file 0. No separate explicit inline rederivation of this X law was found. Other `simp [taylor,...]` proofs are broader translation identities; they are not counted as named callers. These are source-level counts, not opaque kernel or simplifier dependency closure. `@[simp]` means no named external references would still not imply unused code.

The [full caller replay](../evidence/MvPolynomial.taylor_X/native-caller-executed.lean.txt) copies the three prerequisite private helpers and the entire actual caller into a fresh MvPolynomial namespace, changes the named rewrite token to the typed existing aeval_X term, and disables the target's simp annotation before replay. The prerequisite helper proofs are project proofs, not claimed mathlib replacement calls. [Complete clean receipt](../evidence/MvPolynomial.taylor_X/native-caller-success.json). This is a full local caller proof experiment, not a claim that the whole project was migrated or its opaque transitive dependency closure removed.

The same accepted document proves explicit generator normalization with `simp only [taylor, aeval_X]` and a product/power/constant consumer with map_mul, map_pow, algHom_C, algebraMap_eq plus the exact aeval_X rewrite, all while target simp is disabled. Thus the normalized simplification behavior has a concrete replacement, though deleting a global simp lemma can require adding `[taylor]` at additional implicit consumers. A production deletion should run the full build to find those consumers; this read-only assessment does not assert their absence.

## Phase 6 — independent composition and Phase 6b distinction

The old statement is proved by the single existing theorem call:

```lean
example {σ R : Type*} [CommSemiring R] (α : σ → R) (j : σ) :
    MvPolynomial.taylor α (MvPolynomial.X j) = MvPolynomial.X j + MvPolynomial.C (α j) :=
  MvPolynomial.aeval_X _ _
```

Native target replay succeeds; the isolated raw probe guards `#check_failure MvPolynomial.taylor_X`, imports no Roth module, and proves the independently written translation let-form with the same term. No project theorem contributes a proof premise; the parent only fixes the definitionally equal expression. This is COMPOSABLE in the broad sense, and specifically a direct existing-law specialization, hence NO-mathlib-has-it takes precedence over NO-composable.

The separate closing `simp only [taylor, aeval_X]` experiment would, by Phase 6b alone, support BORDERLINE/trivial-simp-composition. It does **not** determine this verdict: the direct exact term independently passes the stronger one-line-existing-law test. The generic law is verified rather than inferred from a short proof, the parent's assessment, or a grep.

## Phase 7 — verdict and actionable destination

**NO-mathlib-has-it**. MvPolynomial.aeval_X already states the whole generator substitution rule at arbitrary target and assignment. The native one-call specialization is sufficient evidence under this bucket's definition. Parent translation remains separately BORDERLINE; no conclusion about adding the parent definition follows here. Declaration 54's rfl/application bridge is a different issue.

Recommend deleting this standalone theorem and replacing the **one named caller** at Taylor:114 by the typed aeval_X rewrite above. Preserve the rest of that caller's proof. For simplifier consumers, use local `[taylor]` with existing aeval_X as demonstrated; check the full project build during an authorized production refactor to locate implicit consumers. If the project chooses a stable semantic translation interface with a dedicated simp law, the alternative destination is **Roth/Taylor.lean**, beside the parent, with a documented local API rationale; this is not dead code. A future upstream translation bundle may independently choose to include its standard generator simp law, just as the univariate API does. That bundle design is not a new mathematical gap in this law.

No YES upstream PR plan, grouping, reviewer, or generalise-first ticket is warranted for this independently redundant theorem. No user permission question is needed to complete the read-only assessment.

## Phase 8 — verification and handoff

All phases complete; theorem-only 2b and 4.5 exclusions are justified; unresolved verification items `[]`. [Verification index](../evidence/MvPolynomial.taylor_X/verification.json), [assessment](../evidence/MvPolynomial.taylor_X/assessment.json), [portable validator](../evidence/MvPolynomial.taylor_X/validate.py), [copy manifest](../evidence/MvPolynomial.taylor_X/copy-manifest.json). Accepted proof receipts are complete success, partial=false, no warnings/errors, and only standard propext/Classical.choice/Quot.sound axioms; candidate-only checks need no separate axiom print. Failed raw/caller preparation attempts are archived separately and are not proof evidence. Exact execution paths remain in native receipts. Root acceptance remains pending until independent integration review.
