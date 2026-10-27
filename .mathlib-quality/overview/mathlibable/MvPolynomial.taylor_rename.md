# Full mathlibable assessment: `MvPolynomial.taylor_rename`

Canonical declaration **68/293**, `Roth/Taylor.lean:164–166`. Verdict **BORDERLINE-needs-human**: a standard variable-renaming convenience law for a proposed named translation API. This read-only assessment is complete; future upstream API questions are not unresolved verification or a request to modify production.

## Phase 0: baseline and scope

The unchanged baseline `99f19fda4b3cbee38fc0d31af76075834f5cc265` built successfully, 2467 jobs, exit0, no warnings/errors. All 17 production source/version-pin hashes freshly match ([build](../evidence/MvPolynomial.taylor_rename/baseline-build.txt), [inputs](../evidence/MvPolynomial.taylor_rename/inputs.json), [hash check](../evidence/MvPolynomial.taylor_rename/input-hash-check.json)). Root verified the target and independent replay in a persistent Lean document, raw mathlib-only compositions, and the full actual caller. Production Lean, versions and project structure are unchanged.

## Phase 1: mathematical comprehension

For any map `f : σ → τ`, renaming the variables of `P` by `f` and then translating by `α : τ → R` is the same polynomial as translating `P` by the pulled-back vector `α ∘ f`, then renaming. Variable collisions are allowed: the map need not be injective. On each generator both sides produce `X (f j) + C (α (f j))`; the universal property extends this agreement to every polynomial.

Full statement with section binders and independent universes (original native signature/print and proof-constant audit in [target receipt](../evidence/MvPolynomial.taylor_rename/native-target-success.json)):

```lean
∀ {σ : Type u} {R : Type v} [CommSemiring R]
  {τ : Type w} (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R),
  MvPolynomial.taylor α (MvPolynomial.rename f P) =
    MvPolynomial.rename f (MvPolynomial.taylor (α ∘ f) P)
```

Only direct project dependency is `MvPolynomial.taylor`. The original proof unfolds this definition, expresses renaming as algebra evaluation, composes evaluations, and normalizes generator images. The fresh replay uses this proof rather than the target theorem. Direct proof constants were inspected with `allowOpaque := true`; no circular call to `MvPolynomial.taylor_rename` is used. Entire [Taylor module](../evidence/MvPolynomial.taylor_rename/Taylor-module.lean.txt) and [Index caller module](../evidence/MvPolynomial.taylor_rename/Index-module.lean.txt) were read and preserved.

## Phase 2: preliminary checks

**SMALL**: structural naturality law, not one of the named main Taylor-expansion results. Phase2b **n/a**, a theorem rather than a one-line data definition. Parent `taylor` was BORDERLINE, but this theorem is not definitional glue and receives its own full assessment. Qualified-name mathlib search finds no exact named target; this search alone is not an absence proof ([receipt](../evidence/MvPolynomial.taylor_rename/rg-full-name.json)).

## Phase 3: exhaustive literature protocol

Exact requests, response SHA256/byte counts, credential-safe locators and original summaries are archived; full returned articles/search bodies are not. Returned URL queries/fragments are stripped. See [specific/general/alias batch](../evidence/MvPolynomial.taylor_rename/web0-metadata.json), [named-channel batch](../evidence/MvPolynomial.taylor_rename/web4-metadata.json), [follow-up](../evidence/MvPolynomial.taylor_rename/webfollow-metadata.json), [direct sources](../evidence/MvPolynomial.taylor_rename/webprimary-metadata.json), [Stacks follow-up](../evidence/MvPolynomial.taylor_rename/webstacks-metadata.json).

| Channel | Actual query/check | Finding and limitation |
|---|---|---|
| Web, specific | `multivariate polynomial translation renaming variables substitution naturality` | Substitution and variable-renaming documentation; no exact stand-alone translation-renaming theorem established. |
| Web, general | `polynomial algebra free commutative algebra variable relabelling universal property` | Free commutative algebra on an arbitrary generator set; generator images determine algebra maps. |
| Web, alias | `Hasse Schmidt Taylor homomorphism naturality substitution variables` | Hasse–Schmidt substitution-map context, including Narváez Macarro's work; not a proof that this theorem needs differential or characteristic-zero assumptions. |
| Optional ChatGPT math | `ask_chatgpt_math` | Unavailable/optional, skipped; no expert answer invented. |
| Local reference | `clean.tex` renaming/embedding search | Lemma4-2 proof lines621–623 describes embedding translated polynomials in larger variable sets; implementation note632 explicitly requests variable-renaming invariance. [Exact excerpt](../evidence/MvPolynomial.taylor_rename/clean-excerpts.tex.txt), [search](../evidence/MvPolynomial.taylor_rename/rg-local-literature.json), [source hash](../evidence/MvPolynomial.taylor_rename/local-literature.json). This application uses an embedding, whereas the target correctly permits all maps. |
| nLab | `site:ncatlab.org/nlab polynomial free commutative algebra` | [Polynomial](https://ncatlab.org/nlab/show/polynomial) search content describes the universal generator map into a free commutative algebra and substitution. Direct page access failed unsupported XHTML; not claimed as direct full-page access. |
| nCatLab/categorical | `site:ncatlab.org/nlab polynomial functor free algebra variable substitution naturality` | Polynomial operations as natural transformations and the free-functor viewpoint support the abstraction. Container/polynomial-endofunctor hits are different objects, not accepted replacements. Direct free-functor page also unsupported XHTML. |
| Stacks | `site:stacks.math.columbia.edu polynomial ring variables universal property homomorphism`; follow-up `site:stacks.math.columbia.edu "polynomial ring" "universal property"` | Returned divided-power/universal-thickening material is not the same polynomial algebra. Direct [05G3](https://stacks.math.columbia.edu/tag/05G3), polynomial-presentations remark following Definition10.14.1, confirms coefficient/generator substitution context only. Two exploratory direct tags00CV/00EP are tensor products/gluing, respectively, and are explicitly not target evidence. |
| MathOverflow | `site:mathoverflow.net polynomial translation renaming variables substitution`; follow-up `site:mathoverflow.net polynomial ring universal property substitution variables` | Follow-up returned [What is the theory of polynomials?](https://mathoverflow.net/questions/73664/what-is-the-theory-of-polynomials) and substitution discussions. No exact target law established; no MO answer used as mathematical verification. |
| Recent arXiv, last five years | `site:arxiv.org polynomial shift equivalence sparse 2022 2026` | [Chillara–Grichener–Shpilka2207.10588](https://arxiv.org/abs/2207.10588), directly confirmed submitted21July2022, defines shifts of multivariate polynomials over rings. Within five years of27October2026; context rather than source of renaming law. Search also returned2026 sparse-shift and2024 equivalence-testing papers; not needed for a generality claim. |

Concept: **naturality of polynomial substitution under maps of variable sets**, specialized to coordinate translations. Sources agree on generator-image/universal-property language. Most general standard form allows arbitrary variable maps and arbitrary substitution targets; mathlib already expresses this through `aeval_rename` and composition of algebra evaluations. Applications often use finite variables/fields/injections; none of those restrictions are present in the assessed law. No disagreement requiring a statement change is found.

## Phases 4a–4b: all parameters and verified generality

| Parameter | Role and generality |
|---|---|
| `σ : Type u` | Arbitrary source variable type, including empty/infinite; no Fintype/DecidableEq. |
| `τ : Type w` | Independent arbitrary target variable type; no cardinality relation required. |
| `R : Type v`, `[CommSemiring R]` | Coefficients admit positive characteristic, zero divisors and trivial semiring; no subtraction, inverses, field or domain used. Semiring-only guarded probe cannot form the current parent `taylor` interface. This is an interface constraint, not a mathematical impossibility proof for a different construction. |
| `f : σ → τ` | Any map, not necessarily injective/surjective. The full native generic and old-form proofs quantify arbitrary `f`. |
| `α : τ → R` | Any target translation vector; source shift must be `α ∘ f`. Omitting this pullback changes the mathematical square. |
| `P` | Any polynomial, no nonzero/degree/support assumptions. |

**MAXIMALLY GENERAL within the fixed parent interface; no verified mechanical hypothesis weakening.** The native abstract `afterRename` allows arbitrary commutative `R`-algebra target `A` and assignment `g : τ → A`, exactly existing `aeval_rename`. Native `afterSubstitution` allows arbitrary assignment into another multivariate polynomial algebra and independent variable target, exactly existing `comp_aeval_apply`. These are existing abstract results, not missing generalise-first contributions. Native `square` packages the target as equality of bundled AlgHom compositions in independent universes, without new assumptions. [Raw source](../evidence/MvPolynomial.taylor_rename/native-raw-executed.lean.txt), [extra source](../evidence/MvPolynomial.taylor_rename/native-extra-executed.lean.txt).

## Phase 4c: all nine modern-idiom checks

| # | Check | Answer and concrete consequence |
|---|---|---|
| 1 | Typeclasses versus bundled preambles | No improvement: coefficient typeclass and existing AlgHom/rename interfaces are already used. |
| 2 | Sequences/metrics versus filters | No; purely algebraic identity, no topology. |
| 3 | Construction versus universal property | Yes in interpretation: free commutative algebra generators determine maps. Existing `aeval_rename`/`comp_aeval_apply` already implement this, avoiding a new induction. |
| 4 | Closure predicate versus bundled structure | No closure predicate. Bundled AlgHom square is natively verified, useful for composition rewriting rather than a new substructure theory. |
| 5 | Field/vector-space versus semiring/module | No surplus field assumptions; already CommSemiring. Parent Semiring weakening cannot be formed, as guarded native probe records. |
| 6 | Higher category | No demonstrated downstream advantage from introducing category infrastructure; naturality language alone does not establish one. |
| 7 | Concrete index | No: both variable types arbitrary and independent; no finite/natural-index restriction to remove. |
| 8 | Concrete-via-abstract proof body | Yes: after unfolding `taylor`, only generic algebra evaluation/renaming and generator-map facts remain. Re-aim gives existing broad laws; named shift square still needs propositional normalization. [Diagnostic](../evidence/MvPolynomial.taylor_rename/proof-body-diagnostic.json). |
| 9 | False-generalization guard | No false widening accepted. Arbitrary maps preserve the law even with collisions; the caller's stronger injectivity is not transferred into the target. Pulling back α along f remains essential. Generic substitution and bundled square specialize correctly; not claimed definitionally equal to the normalized shift square. |

Modern abstract idiom **already available**. No novel modern restatement justifies YES-but-generalise-first. A named shift law might serve an accepted translation API; that is an API design question.

## Phase 4.5: infrastructure risks

**Theorem n/a** for all six rows: definitional equality, instance diamonds, coercion diamonds, reducibility, universe-instance ambiguity and representation/elaboration infrastructure. This theorem adds no definition or instance. Independent-universe bundled square successfully elaborates; no hidden coercion-risk claim is needed.

## Phase 4.6: all five proof-strategy checks

| Check | Assessment |
|---|---|
| Epsilon/neighborhood versus filters | n/a, no analysis. |
| Element arguments versus structural maps | Original proof uses generic evaluation composition; bundled square verified by AlgHom.ext. No missing substructure argument. |
| Sequences versus nets | n/a, no topology. |
| Construction versus universal property | Generator-image equality via existing algebra maps is appropriate; no independent monomial induction required. |
| Missing helper | No missing abstract helper: aeval_rename/comp_aeval_apply and rename generator laws exist. |

Strategy **MATHLIB-IDIOMATIC**. Narrow explicit normalization provides transparent supporting evidence rather than a new helper theory.

## Phase 5: five actual mathlib methods, three forms

[Raw formal-search receipts](../evidence/MvPolynomial.taylor_rename/formal-search.json) preserve all actual Finder, Loogle, LeanSearch and local requests/responses. `rg` is untruncated.

| Method | Current translation/rename form | Literature shift/relabel form | Abstract aevaluation naturality form |
|---|---|---|---|
| Finder | rename_expand / rename_comp_expand and univariate Taylor near-matches | rename_eval₂, rename polynomial embedding | aeval_comp_rename, aeval_rename, comp_aeval |
| Loogle | `MvPolynomial.aeval, MvPolynomial.rename`: aeval_rename and bundled version | `"rename_eval₂"`: exact named generic candidate | `"aeval_rename"`: exact generic candidate |
| LeanSearch | rename / rename_X / expansion and univariate Taylor near-matches | bind₁_rename and substitution near-matches | aeval_rename, comp_aeval_apply, bundled version |
| rg | [current](../evidence/MvPolynomial.taylor_rename/rg-current.json) | [literature](../evidence/MvPolynomial.taylor_rename/rg-literature.json) | [abstract](../evidence/MvPolynomial.taylor_rename/rg-abstract.json) |
| Local symbols | taylor_rename resolves project target | rename_eval₂ prefix gives rename_eval broad match | aeval_rename resolves pinned module |

Local index status is **unavailable**, so no local empty result establishes absence. External indexes can differ from pinned mathlib. Actual pinned source and native signatures/proofs resolve positive candidates:

* `MvPolynomial.aeval_rename`, `Mathlib/Algebra/MvPolynomial/Rename.lean:250`: arbitrary assignment into a commutative coefficient algebra; exact one-call raw `afterRename`. Native printed proof invokes eval₂Hom_rename, whose source reaches eval₂_rename induction.
* `MvPolynomial.aeval_comp_rename`, same file253: bundled algebra-hom equality, native signature verified.
* `MvPolynomial.comp_aeval_apply`, `Mathlib/Algebra/MvPolynomial/Eval.lean:612`: arbitrary algebra hom after evaluation; exact one-call raw `afterSubstitution`. This transports the right-hand translation through rename.
* `rename_eq_aeval`, Rename98; `rename_X`, Rename62; `rename_C`, Rename58: actual source and native normalization facts. See full pinned [Rename](../evidence/MvPolynomial.taylor_rename/MvPolynomial-Rename-module.lean.txt) and [Eval](../evidence/MvPolynomial.taylor_rename/MvPolynomial-Eval-module.lean.txt) modules.
* `rename_eval₂`, Rename257, has a specialized assignment shape `g ∘ k`; it is related generic naturality, not automatically the displayed target. `bind₁_rename` in [Monad](../evidence/MvPolynomial.taylor_rename/MvPolynomial-Monad-module.lean.txt) is source-inspected supplementary substitution vocabulary, not separately native-tested/imported as an accepted replacement. Expansion and univariate Taylor hits concern different operators/representations.

## Phase 5.5: all three statement-shape checks

1. **Normal form:** translation-after-rename equals rename-after-pulled-back-translation is coherent. Reverse orientation could align with an alternate rename-first naming convention but is not a mathematical strengthening.
2. **Syntactic generality:** full arbitrary-algebra evaluation form and bundled square were actually verified. Existing generic law does not make normalized shifted-generator spelling definitionally identical.
3. **Superfluous arguments:** none. Both types, coefficient interface, f, α and P are used. No injectivity to remove; do not confuse the stronger Index caller with target assumptions.

Overall **KEEP-SHAPE** for a retained convenience theorem; no required restatement-before-ship established.

## Phase 6.0: complete caller and inline audit

| Caller | Use | Verified migration option |
|---|---|---|
| `Roth.index_rename`, `Roth/Index.lean:216` | Rewrites translation before transporting support through injective rename and weights through mapDomain | Full copied caller proof uses fresh `TaylorRenameAssessment.replay` in the same rewrite; all remaining support/image/weight steps checked. If deleting the named law later, insert the raw five-fact local `have` and rewrite with it; no source change performed. |

**K=1 explicit production caller.** Target is not simp-tagged. Search finds declaration plus this caller and no independent inline rederivation of this shift square ([caller receipt](../evidence/MvPolynomial.taylor_rename/rg-callers.json), [inline audit](../evidence/MvPolynomial.taylor_rename/rg-inline.json), [summary](../evidence/MvPolynomial.taylor_rename/callers.json)). This is source-level coverage, not an exhaustive implicit kernel-dependency closure. `hasseDeriv_rename` is a different derivative naturality law. The caller's injection hypothesis is needed by support and weight transport, while the assessed translation identity accepts any f. One use is a composability signal, not a deletion proof.

## Phase 6: actual composition and verification

The raw mathlib-only module imports no Roth, guards the unavailable target name, and defines its own `shift`. Abstract forms close by exact existing calls. Original normalized shape closes with:

```lean
change aeval (fun j ↦ X j + C (α j)) (rename f P) =
  rename f (aeval (fun j ↦ X j + C (α (f j))) P)
rw [aeval_rename, comp_aeval_apply]
apply congrArg (fun g : σ → MvPolynomial τ R ↦ aeval g P)
funext j
simp only [Function.comp_apply, map_add, rename_X, rename_C]
```

**Five distinct mathematical facts**: aeval_rename, comp_aeval_apply, map_add, rename_X, rename_C. Structural congruence/extensionality/function-composition reduction is additional bookkeeping. This is not a verified ≤3-mathlib-call term; no claim of minimality or impossibility of a shorter route is made. Merely counting the two composition lemmas omits the actual shifted-generator bridge. Under Phase6b a closing `simp [defs]` composition supports **BORDERLINE**, not automatic NO-composable. Parent taylor is not a mathlib building block; its prior verdict is not inherited and no Mode-B more-general-parent re-aim rule fires.

Accepted [target source](../evidence/MvPolynomial.taylor_rename/native-target-executed.lean.txt), [target receipt](../evidence/MvPolynomial.taylor_rename/native-target-success.json), [raw source](../evidence/MvPolynomial.taylor_rename/native-raw-executed.lean.txt), [raw receipt](../evidence/MvPolynomial.taylor_rename/native-raw-success.json), [extra source](../evidence/MvPolynomial.taylor_rename/native-extra-executed.lean.txt), [extra receipt](../evidence/MvPolynomial.taylor_rename/native-extra-success.json). All complete success, partial false, no errors/warnings/unproved declarations, standard axioms only (`propext`, `Classical.choice`, `Quot.sound`). Full actual Index caller and independent-universe square pass. No limit raises, new axioms, sorry or unsafe proofs.

One initial raw attempt used `congr 1`, which stopped at an AlgHom equality, so the next `funext` failed. Corrected explicit assignment-function `congrArg` passes. [Rejected receipt](../evidence/MvPolynomial.taylor_rename/native-raw-rejected.json) and [source](../evidence/MvPolynomial.taylor_rename/native-raw-rejected.lean.txt) are separate and not accepted evidence or proof of absence.

## Phases 7–8: verdict gates and next action

**BORDERLINE-needs-human**. Generic substitution naturality already exists; the normalized coordinate-shift square remains a plausible standard convenience law of a named translation API. No new abstract mathematics, exact existing normalized target or ≤3-fact old-form composition was established. No mechanical weakening verified. This verdict is driven by the Phase6b API criterion, not cost, inherited parent judgment or search absence.

Future upstream design questions, not input required to complete this read-only assessment:

1. If mathlib adopts named multivariate translation, should variable-renaming naturality be an explicit convenience theorem rather than relying on generic substitution laws?
2. Should the bundled AlgHom square be primary, with this pointwise law derived from it?
3. Should naming/orientation follow `rename_expand` (rename after operation) or retain `taylor_rename` (operation after rename)?

Alternative local destination: retain `Roth/Taylor.lean` alongside translation laws if the upstream named API is declined; it serves `index_rename` and keeps the actual support/weight proof readable. No Archive relocation warranted. No upstream PR, production refactor or reviewer contact is authorized by this assessment.

All phases, parameter/idiom/strategy/shape rows, full search protocol, caller/native evidence and actionable questions complete; verification unresolved list empty. Revisit these design questions when planning an upstream translation API. [Assessment](../evidence/MvPolynomial.taylor_rename/assessment.json), [verification](../evidence/MvPolynomial.taylor_rename/verification.json), [portable validator](../evidence/MvPolynomial.taylor_rename/validate.py).
