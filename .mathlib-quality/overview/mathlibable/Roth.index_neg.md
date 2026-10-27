# Roth.index_neg — NO-mathlib-has-it

## Phase 0 — Baseline

Declaration146 is `Roth/Index.lean:190`, a theorem, on `ramin-cleanup`.
The shared build succeeded (2467 jobs, no warnings/errors); all17 source/pin hashes were freshly recomputed and match its input manifest. No production source was edited. See [baseline](../evidence/Roth.index_neg/baseline-build.txt), [fresh inputs](../evidence/Roth.index_neg/inputs.json), and [source](../evidence/Roth.index_neg/Roth-Index.lean.txt).

The fresh native target check prints this full elaborated type:

```lean
Roth.index_neg.{u_1} {σ : Type u_1} [Fintype σ]
  (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
  Roth.index (-P) α r = Roth.index P α r
```

The original proof has no sorry, only standard axioms `propext`, `Classical.choice`, `Quot.sound`. Its fresh kernel print has no elision. Historical index_mul output elsewhere in persistent diagnostics has a printer elision; this does not affect the complete index_neg print. [Original raw receipt](../evidence/Roth.index_neg/index-neg-original-audit-receipt.json).

## Phase 1 — Comprehend

Changing every coefficient of a real multivariate polynomial to its negative leaves its weighted order of vanishing at every point unchanged. Translation commutes with negation, and a coefficient is nonzero exactly when its negative is nonzero. The two translated supports, hence the sets of weights and their infima, agree. This includes the zero polynomial, empty variable types, and zero entries of `r` under the project's totalized division and real infimum conventions.

Parameters: `σ` indexes variables; `[Fintype σ]` supplies the finite sum in the parent weight/index interface; `P` is any polynomial; `α` is any center; `r` is any natural weight vector. There are no nonvanishing or positivity hypotheses. The file develops index lower bounds, sums, products, scaling and renaming. The entire module was read, together with the neighboring Taylor/weight interfaces and the relevant determinant sign passage.

## Phase 2 — Preliminary checks

SMALL: a support-invariance helper, not a named main theorem or new structure. The one-line-definition test is n/a: this is a theorem, even though its proof is one tactic line. It is not definitional glue and receives an independent full assessment. Its body is `simp [index, support_neg]`; native kernel output exposes `map_neg (taylor α)` followed by `MvPolynomial.support_neg`.

## Phase 3 — Exhaustive literature

Every named channel was attempted, including three distinct actual general web queries. Web artifacts contain exact requests, response SHA256/bytes/status, locators and concise original summaries only; no full web bodies were archived.

| Channel | Actual query / check | Result and limitation |
|---|---|---|
| Web specific | Roth theorem polynomial index multiplication sign negation weighted vanishing | Roth index sources, including Roth1958 ICM and expository notes; no isolated exact sign theorem |
| Web general | weighted order polynomial invariant under multiplication by unit | Weight-order documentation; no exact sign statement |
| Web aliases | order of vanishing valuation v(-f) equals v(f) | Valuation/vanishing-order terminology and primary lecture sources |
| ChatGPT math | Tool inventory | n/a: ask_chatgpt_math unavailable |
| Local | `rg sign\|index\|ind` in clean.tex | §4 defines weighted Taylor-support minimum; §5 line825 explicitly says multiplication by a sign preserves index |
| nLab | site:ncatlab.org/nlab valuation order vanishing units | Valuation and valuation-ring pages; direct valuation fetch failed400 unsupported application/xhtml+xml; search snippets available |
| nCatLab | site:ncatlab.org/ncatlab valuation order vanishing units | Returned /nlab pages outside requested namespace; no exact /ncatlab hit established |
| Stacks | site:stacks.math.columbia.edu order vanishing unit discrete valuation | §10.121 Definition10.121.2, tag02MB, fetched; quotient-length formulation gives unit invariance contextually |
| MathOverflow | site:mathoverflow.net weighted order vanishing polynomial valuation | Related questions on weighted order and prescribed vanishing; no exact sign theorem established |
| arXiv recent | site:arxiv.org weighted order vanishing polynomial valuation 2022 2023 2024 2025 2026 | 2023 ring vanishing-polynomial papers, fetched2302.12637 abstract; different notion (annihilating entire rings), not this law. Other results unrelated; no absence claim |

Evidence: [local index excerpt](../evidence/Roth.index_neg/clean-index-excerpt.tex.txt), [local sign excerpt](../evidence/Roth.index_neg/clean-sign-excerpt.tex.txt), [local search](../evidence/Roth.index_neg/local-literature-search.json), [specific](../evidence/Roth.index_neg/web-specific.json), [general](../evidence/Roth.index_neg/web-general.json), [aliases](../evidence/Roth.index_neg/web-alias.json), [nLab](../evidence/Roth.index_neg/web-nlab.json), [nCatLab](../evidence/Roth.index_neg/web-ncatlab.json), [Stacks](../evidence/Roth.index_neg/web-stacks.json), [MO](../evidence/Roth.index_neg/web-mathoverflow.json), [arXiv](../evidence/Roth.index_neg/web-arxiv.json), [primary access](../evidence/Roth.index_neg/web-primary.json).

Standard concept: weighted order of vanishing, invariant under multiplying by units, with negation its simplest case. For finite support, the exact mathematical mechanism needs only support-preserving negation and an arbitrary map assigning a degree to each exponent; neither positivity of weights nor arithmetic of degrees is used. The local text permits positive real weights and uses infinity at zero, whereas this API uses natural denominators and index0=0. Those conventions affect other valuation laws but not negation invariance. Stacks supplies contextual unit invariance, not an exact theorem about the project's weighted formula. No literature non-hit is treated as proof of absence.

## Phase 4a — Parameters and generality

| Parameter/hypothesis | Assessment |
|---|---|
| `σ : Type*` | Already universe polymorphic. The generic degree theorem permits arbitrary exponent type `A`, no additive operation required. |
| `[Fintype σ]` | Fixed by current `Roth.weight`/`index` signature, not needed by abstract negation-support law. Removing it from the existing spelling is not claimed as a compiled weakening. |
| coefficients `ℝ` | Expanded representation verified over `[Ring R]`, no commutativity/domain/nontriviality assumptions. Ring is the pinned existing theorem's interface, not a claimed logically minimal support structure. |
| `P` | Fully arbitrary, zero allowed; verified zero guard. |
| center `α` | Arbitrary; only Taylor's additive map property used. The abstract finite-support theorem needs no center. |
| `r : σ → ℕ` | Arbitrary including zero; no `hr` to drop. Generic theorem accepts any `D : A → T`, not necessarily additive, nonnegative or rational. |
| result `ℝ` | Generic theorem verified for `[SemilatticeInf T] [OrderTop T]`; WithTop real projection recovers the parent convention. |

## Phase 4b — Verified general form

Within the fixed parent interface, no argument/hypothesis weakening is proposed. The expanded representation is strictly more general and actually compiled in isolation:

```lean
theorem modern {A : Type u} {R : Type v} {T : Type w} [Ring R]
    [SemilatticeInf T] [OrderTop T] (D : A → T) (f : AddMonoidAlgebra R A) :
    AddMonoidAlgebra.infDegree D (-f) = AddMonoidAlgebra.infDegree D f :=
  AddMonoidAlgebra.supDegree_neg (B := OrderDual T)
```

This is already one existing library theorem under order duality, not a new helper contribution. Projecting via `WithTop.untopD 0` was separately compiled. Cost is cheap and is not used to downgrade any verdict. [Exact isolated source](../evidence/Roth.index_neg/index-neg-mathlib-clean-executed.lean.txt), [raw receipt](../evidence/Roth.index_neg/index-neg-mathlib-clean-receipt.json).

## Phase 4c — All nine modern-idiom rows

| # | Diagnostic | Answer / consequence |
|---|---|---|
| 1 | Preambles to typeclasses | No new preambles; generic Ring/order structures already use typeclasses. |
| 2 | Sequences/metrics to filters | No; finite-support algebra, no topology. |
| 3 | Construction to universal property | No object construction in this equality. |
| 4 | Closure predicate to bundled substructure | No closure predicate or subobject involved. |
| 5 | Field/vector-space to weaker algebra | Yes, Ring coefficients suffice in compiled generic theorem; no real field arithmetic is used. |
| 6 | Higher categorical form | No categorical statement or relevant higher structure. |
| 7 | Concrete numeric degree to ordered structure | Yes, arbitrary semilattice inf with top and arbitrary D; existing supDegree_neg on OrderDual. |
| 8 | Concrete-via-abstract body diagnostic | Yes: after `index` unfolds, zero body occurrences of ℝ/α/r-specific arithmetic; only `support_neg` remains (one line). Taylor is used solely through map_neg. The compiled generic theorem captures exactly this. |
| 9 | False-generalization guard | Pass: infDegree on WithTop ℝ plus untopD0 bridge is verified against actual index for every P including zero. Unprojected infinity-valued order is not asserted equal to the real index. |

Modern idiom available: use finite-support infDegree, via order dual of existing supDegree_neg. This enables arbitrary coefficient rings and degree targets, removes irrelevant finiteness/positivity demands from the support law, and composes with the degree API already selected for parent133. The original proof is already short; mathematical organization, not proof length, motivates this route.

## Phase 4.5 — Infrastructure risk

n/a — theorem, not a definition/class/instance. Each of the six infrastructure risks (typeclass diamonds, reducibility leak, noncanonical unfolding, instance priority collision, universe issues, coercion ambiguity) is n/a for adding this proposition proof; no new data or instance path is introduced. Representation changes belong to parent index design, not a theorem-level instance modification.

## Phase 4.6 — All proof-strategy rows

| # | Question | Answer |
|---|---|---|
| 1 | ε-δ versus filters | No topology. |
| 2 | Elements versus ideal/submodule abstraction | No elementwise ideal argument; already uses exact support equality. Generic degree law is the reusable abstraction. |
| 3 | Sequences versus nets | No analysis or limits. |
| 4 | Construction versus universal property | No category/construction. |
| 5 | Helpers mathlib should have | No essential missing mathematics: exact law exists as supDegree_neg on OrderDual. An infDegree_neg name would be discoverability alias only, not established novel API. |

Current strategy MATHLIB-IDIOMATIC under the retained real index representation. Under parent133 re-aim, directly reuse the existing generic degree equality and project. No missing helper is hidden by a longer proof.

## Phase 5 — All five actual mathlib methods

[Complete exact requests and raw returns](../evidence/Roth.index_neg/formal-search.json).

| Form | Finder | Loogle | LeanSearch | rg source | local name |
|---|---|---|---|---|---|
| Current weighted Taylor index negation | Mostly unrelated division-polynomial sign hits | index-name collisions | Taylor/negation/roots partial matches | no Roth-specific index in mathlib | Roth.index_neg itself and unrelated LinearMap.index_neg |
| Literature order of vanishing / negative unit | MvPowerSeries.weightedOrder_neg/order_neg, multiplicity_neg | exact weightedOrder_neg | analyticOrderAt_neg, natTrailingDegree_neg, related | weightedOrder_neg/order_neg present | weightedOrder_neg source hit |
| Abstract signed support / infDegree | exact AddMonoidAlgebra.supDegree_neg, infDegree | exact supDegree_neg | exact supDegree_neg | supDegree_neg line264; no named infDegree_neg | supDegree_neg source hit |

All three local returns report `index: unavailable`; their source hits remain useful, but an empty index result would not prove absence. External indexes may differ from this pin; accepted candidates were read in pinned source and natively checked. [Current rg](../evidence/Roth.index_neg/rg-current.json), [literature rg](../evidence/Roth.index_neg/rg-literature.json), [abstract rg](../evidence/Roth.index_neg/rg-abstract.json), [pinned Degree source](../evidence/Roth.index_neg/Mathlib-Algebra-MonoidAlgebra-Degree.lean.txt).

Pinned positive primary hit:

```lean
AddMonoidAlgebra.supDegree_neg
  {R' A B : Type*} [Ring R'] [SemilatticeSup B] [OrderBot B]
  {D : A → B} {f : AddMonoidAlgebra R' A} :
  AddMonoidAlgebra.supDegree D (-f) = AddMonoidAlgebra.supDegree D f
```

Its instantiation `B := OrderDual T` is definitionally the infDegree negation law. The isolated file guards `#check_failure Roth.index_neg`, imports no Roth module and prints standard axioms for both generic and projected proofs. `#check_failure AddMonoidAlgebra.infDegree_neg` verifies only that exact name is absent in the loaded pinned context; it does not negate the law already supplied by order duality. WeightedOrder_neg is a supporting alternative, not needed by the accepted arbitrary-real-degree bridge.

## Phase 5.5 — Statement shape

1. Normal form: original equality `index (-P) = index P` correctly puts the unnegated normal form on the RHS. Equivalent representations are equality of translated supports, infDegree negation on OrderDual, and weightedOrder_neg after denominator conversion. Canonical reusable form is the existing degree theorem; the project spelling is an adapter.
2. Syntactic generality: tried and compiled explicit P/α/r replacement, generic arbitrary D form, and projected WithTop-real form. Keep original explicit arguments if retaining local compatibility; use implicit polynomial as in the library theorem when re-aimed.
3. Superfluous arguments: no nonvanishing/positivity hypotheses exist. Fintype is fixed by parent signature; α/r are semantically relevant to each index value although irrelevant to its invariance mechanism. ℝ is fixed by parent and is not asserted mechanically droppable without changing representation. No spurious local typeclass can be removed from the original spelling independently of the parent.

Overall: retained local statement SHIP-AS-STATED; upstream should use the existing canonical law, not export another Roth-index specialization.

## Phase 6.0 — Callers and inline audit

Explicit source callers: **0**; statement applications0, proof-body applications0, distinct external files0. Fresh `rg --no-ignore` scoped to all production sources and `git grep` each find only the declaration at Index190. Lexical enumeration covers every file in the canonical declaration inventory and recomputes all hashes. [Full search](../evidence/Roth.index_neg/complete-caller-search.json), [enumeration](../evidence/Roth.index_neg/lexical-enumeration.json), [caller plans](../evidence/Roth.index_neg/callers.json).

Fresh exact-order canonical kernel audit: requested293, unique293, present293, values293; direct target consumers **0**. This is direct kernel-value reference evidence, not a transitive kernel/simp dependency-closure claim. The theorem is not tagged simp. [Exact executed audit](../evidence/Roth.index_neg/index-neg-audit-executed.lean.txt), [direct consumers](../evidence/Roth.index_neg/direct-consumers.json).

Inline-equivalent audit: Theta402–406 removes permutation signs using the broader `index_C_mul`, not `index_neg` or a rederived support-negation proof. This is a bypass via a stronger existing project law; do not count it as an explicit consumer or exact inline reproof of this theorem. [Source fragment](../evidence/Roth.index_neg/theta-sign-excerpt.lean.txt), [inline search](../evidence/Roth.index_neg/rg-inline.json). No source callers need replay/refactoring; zero direct consumers independently corroborates that scope. No claim about unknown external library consumers is made.

## Phase 6 — Actual compositions and parent re-aim

The original-form definition normalization actually closes:

```lean
by simp only [index, map_neg, support_neg]
```

This is a closing simp-with-definitions composition, explicitly the Phase6b BORDERLINE signal in isolation; it is not falsely counted as a three-existing-call replacement or used alone to force NO. The independently verified re-aim rule determines the verdict because the parent133 canonical infDegree already has precisely the analogous law via OrderDual.

The actual target replacement compiles without using `index_neg`:

```lean
by
  rw [IndexConsumers133.targetBridge, IndexConsumers133.targetBridge, map_neg]
  exact congrArg (WithTop.untopD 0)
    (AddMonoidAlgebra.supDegree_neg (B := OrderDual (WithTop ℝ)))
```

Call accounting: the re-aimed law uses **one existing mathlib call**. Projection adds congrArg; original-form transport additionally invokes the previously verified **new project bridge** twice and map_neg. Those bridge invocations are neither definitional nor existing mathlib building blocks. Parent133 bridge evidence is explicitly a prerequisite, not a fresh146 or library theorem. Its exact finite-support-to-real-sInf proof handles empty support separately. No circular use of old/downstream target simp rules occurs: accepted source names every transformation; generic isolated law cannot import the target. A zero-polynomial guard compiles and confirms index0=0 compatibility. [Target exact source](../evidence/Roth.index_neg/index-neg-target-executed.lean.txt), [target receipt](../evidence/Roth.index_neg/index-neg-target-receipt.json), [prerequisite bridge source](../evidence/Roth.index_neg/index-consumers-executed.lean.txt), [bridge receipt](../evidence/Roth.index_neg/index-consumers-receipt.json).

## Phase 7 — Verdict and action

**NO-mathlib-has-it**, by independently verified ModeB parent re-aim. Existing analogous law: `AddMonoidAlgebra.supDegree_neg` at `Mathlib/Algebra/MonoidAlgebra/Degree.lean:264`, instantiated on OrderDual. This verdict is not inherited blindly from parent index and is not based on a name-only search result.

Existing blocks: supDegree_neg/OrderDual for the actual generic law; map_neg for Taylor; WithTop.untopD/congrArg for the real convention; support_neg for the current direct normalization. No missing essential API, no upstream PR or reviewer selection needed for this NO declaration. Do not submit a project-specific index-negation theorem. If parent index remains local, its appropriate alternative destination is the current local `Roth/Index.lean`, optionally retaining this harmless compatibility helper; zero explicit callers need refactoring. If parent133 is re-aimed, replace the helper by direct canonical supDegree_neg on the dual and projection where needed. No production deletion or API change was made in this read-only assessment.

## Phase 8 — Verification and handoff

All requested phases complete; unresolved verification=[]; root acceptance pending. [Verification index](../evidence/Roth.index_neg/verification.json), [phase record](../evidence/Roth.index_neg/assessment.json), [overview entry](../evidence/Roth.index_neg/overview-entry.json), [portable validator](../evidence/Roth.index_neg/validate.py), [copy manifest](../evidence/Roth.index_neg/copy-manifest.json).

Accepted native proofs are clean, nonpartial where disk format provides partial, and use only standard axioms. Required assertions are scoped to fresh native region lines; full-file errors/warnings/sorry checks remain global. Initial isolated attempt had a leading whitespace linter warning and is preserved separately as rejected; only the corrected exact execution is accepted. Raw run_code has diagnostics and no partial field. The validator checks current manifest hashes/bytes in both scratch/integrated layouts, source/pin hashes, exact ordered canonical293 names including private names, evidence links, all phases, native receipts and credential scan.
