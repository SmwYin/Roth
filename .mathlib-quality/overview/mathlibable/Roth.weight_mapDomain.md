# `Roth.weight_mapDomain` — full mathlibable assessment

Verdict: **NO-mathlib-has-it**. Under the mandatory parent re-aim rule, the analogous law is already `Finsupp.linearCombination_mapDomain`, `Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean:158`. Its specialization to `Finsupp.weight` is definitional. The bridge from the project's division sum to reciprocal-generator `Finsupp.weight` requires normalization; it is not definitional. Injectivity is unnecessary for the weight identity, including when different source variables collide.

## Phase 0 — baseline and identity

The shared `lake build` completed successfully (2467 jobs, exit 0). All 17 production source/pin hashes were freshly checked and match the baseline manifest. This assessment changes no production Lean, pin, or Git files. The declaration head is **Roth/Box.lean:127**; 128 is its continuation. The native target resolves and the source proof replays without new axioms.

Evidence: [baseline](../evidence/Roth.weight_mapDomain/baseline-build.txt), [fresh inputs](../evidence/Roth.weight_mapDomain/input-check.json), [source hashes](../evidence/Roth.weight_mapDomain/source-hashes.json), [source](../evidence/Roth.weight_mapDomain/Box-source.lean.txt), [verification](../evidence/Roth.weight_mapDomain/verification.json).

## Phase 1 — comprehend

Full native Lean type (universe names are printer-generated):

```lean
@Roth.weight_mapDomain : ∀ {σ : Type u_3} [inst : Fintype σ] {τ : Type u_4}
  [inst_1 : Fintype τ] {f : σ → τ}, Function.Injective f →
  ∀ (r : τ → ℕ) (d : σ →₀ ℕ),
    Roth.weight r (Finsupp.mapDomain f d) = Roth.weight (r ∘ f) d
```

The weight is `∑ j, (d j : ℝ) / r j`. Pushing an exponent vector along an injection retains the weight after pulling back its parameters. The source uses `Finsupp.sum_mapDomain_index_inj` and finite-sum normalization. More generally, mapDomain adds coefficients in each target fibre; scalar multiplication is additive, so the same equality holds for arbitrary `f`. No positivity/nonzero denominator assumption is needed: Lean division is total and reciprocal zero contributes zero on both sides.

The entire declaring module, the Lattice module, the Index module, and the enclosing Theta caller theorem were read. Project dependency: `Roth.weight`; no other project theorem enters the source proof. Mathematical content: naturality of evaluation of a finite formal linear combination under relabelling of generators.

## Phase 2 — preliminary classification

**BIG**: it is explicitly listed in the declaring module's `Main results` at line 33. This overrides the fact that its proof is short. Definition-only one-line test: **n/a, theorem**. No definitional/diamond exemption is asserted or needed.

## Phase 3 — exhaustive literature protocol

Every named channel was attempted. Exact requests, returned response hashes/byte counts, retained title/URL locators, and original concise summaries are archived; article/search bodies were not persisted. URL query parameters were stripped from retained returned locators, while exact search requests were retained. No malformed `site:` query was used.

| Channel | Actual query / locator | Result and limit |
|---|---|---|
| General web: specific | `"Roth theorem" "index" "variables" weight embedding` | Milojevic, *An elementary approach to Roth's theorem*, January 2022, §3 p4: monomial index is sum of exponent/degree; concrete source anchor. |
| General web: general | `"finitely supported" "pushforward" "linear combination"` | Formal finite linear combinations and induced pushforward identified; no external exact division-sum theorem claimed. |
| General web: alias | `"free module" "change of basis" "map" "finite support"` | Mostly textbook/secondary results; no new exact hit accepted. |
| ChatGPT mathematics | Tool inventory | n/a: `ask_chatgpt_math` unavailable. |
| Local references | `clean.tex:530–555,613–637` | §4 definition and Lemma 4-2 embedding argument: extra variable has exponent zero. Literature allows positive real denominator parameters; project uses natural parameters including zero. |
| nLab | `site:ncatlab.org/nlab free module finitely supported universal property` | Free module/free object search hits. Direct page fetch fails unsupported XHTML; no body-level evidence claimed. |
| nCatLab | `site:ncatlab.org/nlab free commutative monoid functor pushforward` | Free commutative monoid/free functor hits; direct page fetch fails unsupported XHTML. Useful conceptual context only. |
| Stacks | `site:stacks.math.columbia.edu free module universal property direct sum`; retry with `"free module" "universal property"` | Tag 08RR uses universal property of free module in pullback compatibility. Related categorical context, no exact finite-sum identity. Guessed tag 00CG was unrelated and rejected. |
| MathOverflow | `site:mathoverflow.net finitely supported functions pushforward free module` | Sheaf pushforward/finite presentation discussions; no direct hit. |
| Recent arXiv | `site:arxiv.org free modules finitely supported pushforward 2022 2023 2024 2025 2026` | 2408.02485 (submitted 5 August 2024) inspected; categorical Cherednik actions are unrelated to exact law. Older hits excluded. No recent competing formulation found. |

Primary locators: [Milojevic §3](https://aleksa-milojevic.github.io/expository/roth.pdf), [Stacks 08RR](https://stacks.math.columbia.edu/tag/08RR), [nLab free module](https://ncatlab.org/nlab/show/free+module), [arXiv dated inspection](https://arxiv.org/abs/2408.02485). The mathematical synthesis is that weighted evaluation commutes with pushforward of finite formal combinations. This abstract interpretation is independently supported by the pinned library theorem, rather than inferred from inaccessible nLab content. No historical change of formulation is asserted from the unsuccessful alias searches.

Receipts: [specific](../evidence/Roth.weight_mapDomain/web0-metadata.json), [general](../evidence/Roth.weight_mapDomain/web1-metadata.json), [alias](../evidence/Roth.weight_mapDomain/web2-metadata.json), [nLab](../evidence/Roth.weight_mapDomain/web3-metadata.json), [nCatLab](../evidence/Roth.weight_mapDomain/web4-metadata.json), [Stacks](../evidence/Roth.weight_mapDomain/web5-metadata.json), [MO](../evidence/Roth.weight_mapDomain/web6-metadata.json), [arXiv](../evidence/Roth.weight_mapDomain/web7-metadata.json), [direct opens](../evidence/Roth.weight_mapDomain/web8-metadata.json), [Stacks retry](../evidence/Roth.weight_mapDomain/web9-metadata.json), [local excerpts](../evidence/Roth.weight_mapDomain/caller-literature-excerpts.json).

## Phases 4a–4b — all parameters and generality

| Parameter / constraint | Needed in current representation? | Generalization and verification scope |
|---|---|---|
| `σ : Type*`, `τ : Type*` | Yes, source/target index sets | Already independently universe polymorphic; general library law has arbitrary types. |
| `[Fintype σ]`, `[Fintype τ]` | Yes for both occurrences of the fixed `Roth.weight` interface | Not intrinsic to weighted evaluation. Generic `Finsupp.weight` law compiles without either finite ambient instance; finite support is enough. This is a representation expansion, not deleting binders from an otherwise unchanged ill-typed statement. |
| `{f : σ → τ}` | Yes | Arbitrary map works, not only embeddings. |
| `hf : Injective f` | No | Actual no-injectivity proof compiled; constant Bool→Unit collision case verified. Fibre coefficients add before evaluation. |
| `r : τ → ℕ` | Essential data for denominator notation | Generalize reciprocal family to arbitrary `w : τ → M`. This includes positive real denominators in the literature and zero denominators allowed by the project. |
| `d : σ →₀ ℕ` | Essential finite combination | General law permits `σ →₀ R`, `[Semiring R]`, `[AddCommMonoid M]`, `[Module R M]`; naturals and reals specialize this. |
| Real target | Part of fixed parent interface | No topology/order/completeness is needed; replace by any module in re-aimed law. |
| Decidable equality / positivity | Absent | `[DecidableEq σ]` from earlier module variables was omitted; do not list it in the theorem's native type. No new such assumptions needed. |

**STRICTLY NARROWER THAN STANDARD**: verified deletion of injectivity in the original parent interface, and existing generic re-aim expands finite indices/coefficients/values. Mechanical no-hf restatement is cheap; parent migration changes representation across the development. Cost does not determine the verdict. Proposed normal target already exists:

```lean
example {α β R M : Type*} [Semiring R] [AddCommMonoid M] [Module R M]
    (w : β → M) (f : α → β) (d : α →₀ R) :
    Finsupp.weight w (d.mapDomain f) = Finsupp.weight (w ∘ f) d :=
  Finsupp.linearCombination_mapDomain R f d
```

## Phase 4c — nine modern-idiom checks

| # | Question | Answer, proposal, downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of prose preambles | Already typeclass-based; generic law uses standard Semiring/Module hierarchy; no new class. |
| 2 | Filters instead of sequences/metrics | No: finite algebraic identity has no convergence. |
| 3 | Universal property instead of construction | Yes: free-module evaluation naturally composes with `lmapDomain`; `linearCombination_comp_lmapDomain` already gives bundled composition. |
| 4 | Bundled substructures instead of closure predicates | No subset-with-closure predicate here; evaluation is already bundled as LinearMap/AddMonoidHom upstream. |
| 5 | Field/vector-space to semiring/module hierarchy | Yes: generic Module law removes all division/order requirements once weights are arbitrary generator values. Supports semiring coefficients. |
| 6 | Higher-category generalization | No: no higher morphism data or concrete downstream need. Ordinary linear-map composition suffices. |
| 7 | Concrete ℕ/ℝ to abstract algebra | Yes: arbitrary coefficient semiring R and target module M in existing theorem. Infinite ambient index types also work. |
| 8 | Concrete-via-abstract diagnostic | Fires: proof body contains `weight` on one normalization line and no subsequent project object; remaining line invokes abstract sum transport. Replace reciprocal arithmetic with linear-combination naturality. This is actual existing API, not a proposed unproved helper. |
| 9 | False-generalization guard | Passed for the monomial identity: bridge verifies exact original weight, including denominator zero. Dropping injectivity for the *polynomial index* is not licensed: renaming can merge/cancel coefficients, so `index_rename` retains hf for its support step. |

Modern idiom available and already present. It removes repeated `Fintype` requirements from the re-aimed statement and enables noninjective maps, `linearCombination_comp_lmapDomain`, and module-valued evaluation. This is a real mathematical improvement in the existing library, not a missing new contribution.

## Phase 4.5 — infrastructure risks

Theorem: **n/a** for introduction of new definitional/typeclass paths. All six dimensions checked: no new instance diamond; no reducible definition; no new unfolding equation beyond theorem equality; no instance priority; no new universe identification; no coercion. Existing weight's representation bridge is propositional, so do not rely on definitional equality between the project sum and generic weight.

## Phase 4.6 — five proof-strategy checks

| # | Strategy check | Finding |
|---|---|---|
| 1 | Topological ε–δ versus filters | No topology; n/a. |
| 2 | Element algebra versus bundled maps | Yes: use existing linear evaluation and `lmapDomain` composition. Cheap after the parent bridge. |
| 3 | Sequences versus nets | No convergence; n/a. |
| 4 | Explicit construction versus universal property | Existing linear-combination naturality is the appropriate universal-property consequence; no new categorical construction needed. |
| 5 | Missing helpers that should be in mathlib | None for this law: exact generic transport theorem exists. A project bridge is local normalization, not new missing mathematics. |

**REFACTOR-RECOMMENDED**: migrate parent weight and use the existing theorem. The source proof is a valid finite-sum implementation but carries unnecessary injectivity. No API gap is invented merely to shorten a two-line proof.

## Phase 5 — all five actual mathlib search methods

Every method ran on current, literature-standard, and abstract forms. External search revisions are not assumed equal to the pin; all decisive candidates were checked natively against the pin.

| Method | Current form | Literature form | Abstract form |
|---|---|---|---|
| Finder | Injective renamed polynomial degree hits | `sum_mapDomain_index`, `sum_mapDomain_index_inj` | Exact `linearCombination_mapDomain`, bundled companion |
| Loogle | `Finsupp.sum_mapDomain_index_inj` hit | `Finsupp.mapDomain, Finsupp.sum`: both sum transport forms | `Finsupp.linearCombination, Finsupp.mapDomain`: exact generic theorem |
| LeanSearch | `Fintype.sum_of_injective`, weighted degree | Mostly unrelated measure pushforwards | Exact `linearCombination_mapDomain` first result |
| Source rg | Injective sum lemma generated by to_additive | Additive sum-mapDomain theorem | Pinned LinearCombination.lean:148,158 |
| Local name lookup | `Roth.weight_mapDomain` project hit | Source additive transport hit; one old indexed evidence hit excluded | Pinned exact theorem source hit |

Local responses report `index: unavailable`; their source hits are positive evidence only, and no empty lookup is used to prove absence. Current/literature queries and results: [current](../evidence/Roth.weight_mapDomain/search-current.json), [literature](../evidence/Roth.weight_mapDomain/search-literature.json), [abstract](../evidence/Roth.weight_mapDomain/search-abstract.json), [exact rg](../evidence/Roth.weight_mapDomain/source-search.json).

Conclusion: **found in mathlib as `Finsupp.linearCombination_mapDomain`; strictly more general form**, directly serving the parent re-aim. Its arguments are `R f d`; the coefficient semiring is explicit, target generator family is implicit. Original source building blocks: `Finsupp.sum_mapDomain_index_inj`, `Finsupp.sum_fintype`, `Nat.cast_zero`, `zero_div` (the last two discharge zero-coefficient normalization).

## Phase 5.5 — statement shape

Normal forms considered: project division sum; reciprocal-generator Finsupp.weight; generic Finsupp.linearCombination; bundled `linearCombination_comp_lmapDomain`. Canonical computational form is linear-combination evaluation, with `mapDomain` on the left and composed generator family on the right; RHS orientation is respected. Existing `[simp]` upstream law uses that orientation.

Syntactic alternatives actually tested: original injective statement, same weight statement without hf, generic weight/linear-combination statement, concrete colliding map, and caller split equalities. Choose existing generic pointwise law for rewriting, bundled companion when composing linear maps. Superfluous original argument: **hf only**. Both Fintype instances remain required by the fixed project definition, although unnecessary after the explicit parent migration. No DecidableEq or positivity binder to drop. **RESTATE-BEFORE-SHIP** if retaining a local wrapper; no new mathlib shipment recommended.

## Phase 6.0 — every explicit source caller and inline audit

Internal explicit use count **3**, in **3 external-to-declaring files**. Definition head and Box module docstring are excluded. This useful API signal does not override an exact upstream abstract hit. Search is source-level, not the opaque kernel/simp dependency closure; theorem is not tagged simp locally.

| Caller | Present use | Concrete refactor plan |
|---|---|---|
| `Roth/Lattice.lean:155`, `card_filter_fiber_eq` | rewrite `weight_mapDomain (Fin.castSucc_injective n)` | After parent migration rewrite using `Finsupp.linearCombination_mapDomain ℕ Fin.castSucc d`; keep split-add/single normalization and surrounding arithmetic. Before migration use verified no-hf local compatibility rewrite. |
| `Roth/Index.lean:219`, `index_rename` | `exact weight_mapDomain hf r d` | After reciprocal-weight bridge, exact `Finsupp.linearCombination_mapDomain ℕ f d`. Retain `hf` for `support_rename_of_injective` earlier in the proof. |
| `Roth/Theta.lean:391`, `sum_max_sub_le_index_det` | rewrite Option.some transport inside h1 | Use `Finsupp.linearCombination_mapDomain ℕ some (D μ)` after bridge, preserve add/single and inequality manipulations. No injectivity argument needed for this rewrite. |

Inline-derivation audit (`mapDomain|embDomain|rename|sum_mapDomain|weight_mapDomain` across all production modules) found no duplicate derivation of the same weight transport. HasseDeriv's mapDomain/rename proof transports derivative coefficients and really requires injectivity; Taylor renaming and Separation coefficient splitting are different laws. Fin/Option apply lemmas in Lattice/Separation describe coordinates, not weighted sums. The three actual replacement shapes are compiled in native probes; whole migrated production modules were not edited or claimed built.

## Phase 6 — actual composition experiments

1. Source replay: original injective finite-sum proof compiles. Its `simpa [Finsupp.sum_fintype, weight]` is normalization, not a definitional application of the generic law.
2. Old spelling composition attempt: finite-support/ambient-sum conversion on both sides plus injective transport. The zero side conditions also need `Nat.cast_zero` and `zero_div`: natural-to-real zero casting is not definitional. Thus a three-fact term counting only `zero_div` was rejected analytically and was not submitted as a Lean success. The source replay does not establish a strict ≤3-call term; it uses at least these four distinct facts through normalization, with repeated conversion/zero-normalization instances. Exact expanded application count of the simplifier proof is not certified. A closing simp proof by itself invokes Phase 6b's borderline rule and is not the decisive NO evidence here.
3. Re-aim at existing parent: `Finsupp.linearCombination_mapDomain R f d` is **one existing theorem call**, definitionally equal to the generic Finsupp.weight transport target. The bridge from Roth.weight to reciprocal Finsupp.weight is independently verified. No use of the original target/downstream simp theorem closes this experiment.
4. Generality probes: no hf, colliding Bool→Unit map, infinite ambient types, semiring/module coefficients, and all caller shapes compile. Standard axiom checks exclude sorryAx.

Conclusion: **COMPOSABLE on the re-aimed parent in one call**; exact existing analogue wins under Mode B's explicit re-aim gate. No unsupported claim that the old bridge is definitional or is a one-call proof.

## Phases 7–8 — actionable verdict and final checks

**NO-mathlib-has-it**, independently established rather than blindly inheriting the parent's verdict. `Roth.weight` was accepted as NO-mathlib-has-it in progress; its existing counterpart is `Finsupp.weight`. The law at that counterpart is exactly existing linear-combination naturality. This satisfies the parent re-aim gate even though old notation needs normalization. There is no new upstream gap, PR grouping, or reviewer request for this NO verdict.

Future recommendation: in a future parent migration (not performed or authorized by this read-only overview), replace project division weights by reciprocal-generator Finsupp.weight, update all three callers as above, and delete the redundant wrapper. If a domain-readable name is retained during migration, its alternative destination is **Roth/Box.lean**, as project compatibility API, with injectivity removed and a truthful collision-compatible docstring. Keep Index's support injectivity hypothesis. This report assesses and verifies that plan without editing production.

Accepted exact native sources and raw receipts, source equality checks, failure separation, standard-axiom checks, and limitations are in [verification](../evidence/Roth.weight_mapDomain/verification.json). [Assessment](../evidence/Roth.weight_mapDomain/assessment.json), [overview entry](../evidence/Roth.weight_mapDomain/overview-entry.json), [portable validator](../evidence/Roth.weight_mapDomain/validate.py), and [copy manifest](../evidence/Roth.weight_mapDomain/copy-manifest.json) cover publication gates. Root acceptance remains pending independent review.
