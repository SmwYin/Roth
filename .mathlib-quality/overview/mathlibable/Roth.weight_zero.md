# Full mathlibable assessment: `Roth.weight_zero`

Verdict: **NO-mathlib-has-it**, under the verified parent re-aim rule. Three existing arithmetic facts prove the exact statement: finite sums of zero terms vanish, natural zero casts to zero, and zero divided by anything is zero. All phases ran independently; the final verdict additionally applies the explicit parent re-aim rule. The underlying bundled `Finsupp.weight` also already preserves zero by `map_zero`, but identifying the project representation with that bundled map requires a bridge.

## Phase 0 — Baseline and scope

Canonical declaration 32, `Roth/Box.lean:80`, theorem, branch `ramin-cleanup`. All 17 production source/pin hashes freshly match the reusable baseline manifest; the baseline `lake build` completed 2467 jobs with exit 0. Read the full declaring module and `Index.lean`, including its potential simp consumer. No production or Git changes were made. Applied mathlib-quality, the full mathlibable command, and mathlib-search, mathlibable-verdicts, mathlib-review-stages, generalisation-patterns references.

Evidence: [fresh hashes](../evidence/Roth.weight_zero/source-pin-hashes.json), [baseline](../evidence/Roth.weight_zero/baseline-build.txt), [declaring module](../evidence/Roth.weight_zero/Box.lean.txt), [source searches](../evidence/Roth.weight_zero/source-search.json).

## Phase 1 — Statement and proof

For a finite variable type and natural parameters `r`, the zero multi-index has real weight zero. Every numerator is zero, regardless of the denominators; their finite sum is zero. The natural parameters may vanish. No positivity, nonzero-denominator, polynomial, box-membership, or nonempty-variable hypothesis is needed.

Native full type:

```lean
@Roth.weight_zero : ∀ {σ : Type u_2} [Fintype σ] (r : σ → ℕ), Roth.weight r 0 = 0
```

`σ` is arbitrary and universe polymorphic; `Fintype σ` supplies the full-index sum; `r` gives the denominator family. `DecidableEq σ` is absent: the module already omitted it. The source proof is `simp [weight]`. Native target and independent mathlib-only proofs succeed with only standard axioms `propext`, `Classical.choice`, `Quot.sound`. [Verification map](../evidence/Roth.weight_zero/verification.json) links exact executed sources and raw receipts.

## Phase 2 — Preliminary checks

**SMALL**: elementary zero evaluation, no new structure, named theorem, or module main result. Phase 2b: **n/a — theorem**, despite a one-line proof; no definition exemption is claimed.

## Phase 3 — Exhaustive literature search

Every named channel and three distinct general-web queries were executed. Metadata preserves exact requests, returned-response SHA256/bytes, status, titles/locators and original summaries without storing article bodies: [general](../evidence/Roth.weight_zero/literature-1.json), [abstract channels](../evidence/Roth.weight_zero/literature-2.json), [openings/recent search](../evidence/Roth.weight_zero/literature-3.json), [primary locators](../evidence/Roth.weight_zero/literature-4.json).

| Channel | Actual query / examination | Result and limitation |
|---|---|---|
| General specific | `Roth theorem index polynomial zero multiindex weight sum i r` | Roth's ICM1958 report preview gives index relative to positive parameters. Direct PDF opening fails size limit (74,705,952 bytes); preview only. |
| General abstract | `additive homomorphism zero identity commutative monoid weighted sum` | Identity-preserving monoid formulation; primary Cambridge algebra exercise notes and abstract finite sums discovered. No claim of a separate named Roth lemma. |
| General alias | `weighted degree monomial constant monomial degree zero` | MIT notes §1.8.7, PDF p.23, give weighted monomial degree as exponent-weight pairing. Constant monomial has zero exponent vector. Secondary MathWorld hit used only for discovery. |
| ChatGPT math MCP | Standard form, generality, historical-evolution channel | n/a: `ask_chatgpt_math` unavailable. |
| Local | `clean.tex` §4, lines 530–568 | Positive real parameters; zero weight iff zero exponent vector under positivity. Zero-input implication itself needs no positivity. [Excerpt](../evidence/Roth.weight_zero/local-reference.txt). |
| nLab | `site:ncatlab.org nlab monoid homomorphism identity` | Homomorphism page explicitly distinguishes identity-preserving monoid maps; direct opening fails 400 unsupported `application/xhtml+xml`. Search rendering only. |
| nCatLab | `site:ncatlab.org nlab free commutative monoid finite formal sums` | Free commutative monoid page describes finitely supported natural formal combinations and extension to monoid coefficients. Direct opening same XHTML failure. |
| Stacks | `site:stacks.math.columbia.edu graded ring polynomial degree zero monomial` | Opened Tag053C: positive but unequal generator degrees, adjacent weighted-grading context; no special zero-input API conclusion. |
| MathOverflow | `site:mathoverflow.net Roth theorem polynomial index weights` | Opened question332190 on effectiveness in Roth approximation; adjacent polynomial-method discussion, no replacement for elementary zero-weight identity. |
| Recent arXiv | `site:arxiv.org Roth theorem polynomial index weighted 2021 2022 2023 2024 2025 2026` | Salami2610.17589v1, 13 October2026, §8 concerns failure of naive weighted index rescaling. This does not challenge zero-input evaluation. Combinatorial Roth papers are different problems. |

Primary locators: [MIT §1.8.7](https://math.mit.edu/classes/18.721/ag-feb20.pdf), [Roth ICM1958 preview](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf), [nLab homomorphism](https://ncatlab.org/nlab/show/homomorphism), [free commutative monoid](https://ncatlab.org/nlab/show/free+commutative+monoid), [Stacks053C](https://stacks.math.columbia.edu/tag/053C), [MathOverflow332190](https://mathoverflow.net/questions/332190/optimal-roth-type-result-in-diophantine-approximation), [recent arXiv §8](https://arxiv.org/html/2610.17589v1).

Literature summary: this is zero preservation of the weighted-degree pairing on a free commutative monoid. The general abstract standard allows arbitrary additive commutative target monoids and arbitrary weights, with no positivity. Classical Roth weights use positive real reciprocal parameters; Lean's totalized division also allows zero denominators. There is no mathematical disagreement for zero input. Do not confuse the zero multi-index (constant monomial1) with the zero polynomial, whose degree/order conventions differ.

## Phase 4a–4b — All parameters and generality

| Parameter | Role and actual extension check | Conclusion |
|---|---|---|
| `σ : Type*` | Already arbitrary universe and variable names. | No restriction to remove. |
| `[Fintype σ]` | Required by the fixed parent's full sum. Arbitrary ambient type verified using `Finsupp.weight`; an infinite ambient ℕ example succeeds. | Expanded representation, not a drop from the same parent expression. |
| `r : σ → ℕ` | No positivity used. Finite sums verified for arbitrary denominator functions in a `DivisionSemiring`, including zero. | Natural parameters are project-specific; signed/zero denominators do not harm zero input. |
| zero input `σ →₀ ℕ` | Actual statement is only at zero. Finite ordinary function-family formula and arbitrary-coefficient target monoid weight are verified. | Keep zero input; replacing it with arbitrary input is false. |
| target `ℝ` | No order, completeness, or commutativity of multiplication needed; `DivisionSemiring` finite formula compiles. | Do not claim minimal classes: independently supplied `AddCommMonoid` and `GroupWithZero` produced an incoherent zero-instance diamond in a rejected attempt. |
| `DecidableEq` / positivity | Already absent. | No unused original hypothesis to remove. |

Generality: **MAXIMALLY GENERAL within the fixed parent interface**, with broader representations positively verified. The abstract statement `Finsupp.weight w 0 = 0` is already `map_zero`. These are existing general facts, so there is no new upstream generalization proposal. [Exact independent source](../evidence/Roth.weight_zero/raw-executed.lean.txt).

## Phase 4c — Nine modern-idiom rows

| # | Question | Answer and downstream consequence |
|---|---|---|
| 1 | Typeclasses / instances | Already uses `Fintype`; no new proposition-as-instance needed. |
| 2 | Filters / nets | No topology or convergence. |
| 3 | Universal property | The free commutative monoid extension explains the pairing; existing bundled `Finsupp.weight` supplies it. No new object constructed here. |
| 4 | Bundled substructure | Yes, use an additive map rather than a bare function when refactoring the parent. Then `map_zero`, `map_add`, and map-sum API apply. |
| 5 | Module / field hierarchy | Yes at representation level: arbitrary `AddCommMonoid M` with natural scalar action for `Finsupp.weight`, no field or order. Verified. |
| 6 | Higher categories | No higher coherence or categorical result needed for zero evaluation. |
| 7 | Concrete indices / scalars | Index type already arbitrary. Real scalar formula extends to `DivisionSemiring`; support pairing extends to arbitrary ambient variables. Verified. |
| 8 | Concrete-via-abstract diagnostic | Fires: proof has one `weight` occurrence, in the unfolding list, and zero subsequent proof lines using it. Abstract content is sum-of-zero or bundled-map zero preservation, already in mathlib. |
| 9 | False-generalisation guard | Preserve zero exponent vector. Native counterguard shows the singleton exponent1 with denominator1 has weight1≠0. Conversely denominator0 gives weight0 at that same nonzero input, so injectivity/zero iff inputzero cannot be inferred without stronger assumptions. |

Modern idiom available: **yes, existing bundled additive-map API**. It eliminates separate preservation lemmas after a parent migration; it does not make this theorem a new mathlib gap. The bridge from division formula to reciprocal-weight pairing is not definitional and is not silently counted as a one-call replacement of the unchanged target.

## Phase 4.5 — Infrastructure risk

**n/a — theorem.** All six definition-only risks (typeclass diamond, reducibility leak, noncanonical unfolding, instance priority, universe construction, coercion ambiguity) are inapplicable to this declaration. The rejected independent-class experiment is evidence against claiming an unverified representation weakening, not an instance introduced by this theorem.

## Phase 4.6 — Five proof-strategy rows

| # | Question | Outcome |
|---|---|---|
| 1 | Epsilon-delta versus filters | n/a: no topology. |
| 2 | Elements versus ideal/submodule inclusions | No inclusion proof; finite-sum evaluation is natural. Bundled map gives a structural alternative after parent refactor. |
| 3 | Sequences versus nets | n/a: finite sum. |
| 4 | Construction versus universal property | n/a: equality proof; existing Finsupp map already uses linear combination. |
| 5 | Missing helpers mathlib should have | None needed: `Finset.sum_eq_zero`, `Nat.cast_zero`, `zero_div`, or `map_zero` at the abstract interface. |

Strategy: **MATHLIB-IDIOMATIC**. The original simplification proof is appropriate local API. Explicit arithmetic terms are evidence for composability, not a proposed improvement over source automation.

## Phase 5 — Five actual mathlib search methods on three forms

Forms: current Roth zero-weight formula; standard finite sum of zeros; abstract additive-map/Finsupp zero preservation. [Complete tool requests/results](../evidence/Roth.weight_zero/formal-search.json), [pinned source search](../evidence/Roth.weight_zero/source-search.json), [qualified-name search](../evidence/Roth.weight_zero/full-name-source-search.json).

| Method | Current | Standard | Abstract |
|---|---|---|---|
| Lean-Finder | Roth wording collides with unrelated combinatorial Roth-number lemmas. | `Finset.sum_eq_zero`, `Finset.sum_const_zero`, `Fintype.sum_eq_zero`. | `Finsupp.weight`, degree_zero, stronger zero-characterization. |
| Loogle | Real/sum/zero query yields irrelevant analytic matches. | `Finset.sum_eq_zero` exact type-pattern hit. | `Finsupp.weight_eq_zero_iff_eq_zero` and weighted polynomial facts, requiring extra premises. |
| LeanSearch | Polynomial/power-series zero and stronger zero-characterization near misses. | `Finset.sum_eq_zero`, `Fintype.sum_eq_zero`, `List.sum_eq_zero`. | `AddMonoidHom.map_zero`, `AddMonoidHomClass.toZeroHomClass`. |
| rg source | No qualified `Roth.weight_zero` in pinned mathlib. | Generated additive finite-product API: `sum_eq_zero`; natural cast-zero and zero_div sources identified. | Weight.lean:82 is `AddMonoidHom`; its own zero-characterization proof uses `map_zero` at line185. |
| Local names | `weight_zero` returns project theorem. | `sum_eq_zero` partial textual fallback returns unrelated zero sums. | `map_zero` returns many class-specific matches. |

Local name searches explicitly return `index: unavailable`; external search revisions may differ. Neither failure nor grep silence proves absence. Positive pinned target and mathlib-only elaboration determine usability. Building blocks: `Finset.sum_eq_zero` in `Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean` (generated via `to_additive`); `Nat.cast_zero` in `Mathlib/Data/Nat/Cast/Defs.lean:80`; `zero_div` in `Mathlib/Algebra/GroupWithZero/Basic.lean:399`; `Finsupp.weight` in `Mathlib/Data/Finsupp/Weight.lean:82`; generic `map_zero` for zero-preserving maps. Native target prints the sum and division signatures and verifies the exact cast composition.

## Phase 5.5 — Three statement-shape checks

1. **Normal form:** `weight r 0 = 0` puts canonical zero on the right, appropriate for simp; reversing it would be a poor simplifier orientation.
2. **Syntactic generality:** arbitrary `r` explicit makes rewrites easy; no nonzero or positivity premise should be added. At the bundled interface the statement becomes existing `map_zero`, verified independently.
3. **Superfluous arguments:** no extra assumptions; `r` occurs in the conclusion and `Fintype` is required by the fixed parent. `DecidableEq` already omitted. No actual binder drop claimed.

Verdict: **NORMAL-FORM**, no required local restatement; upstream use existing generic API.

## Phase 6.0 — Actual callers and inline audit

| Explicit source caller | Count | Refactor |
|---|---:|---|
| None outside own declaration | 0 | No named call to replace. |

Internal explicit use count0; external files0. [Exact caller inventory](../evidence/Roth.weight_zero/explicit-callers.json). This is source-level references, not a kernel or simplifier dependency closure. The theorem has `@[simp]`; zero explicit names does **not** imply dead code. `Index.index_eq_zero_iff`, line105, has `simpa using index_le_weight ... (d := 0)` and is a potential simplifier consumer. If deleting the simp lemma, replace its zero-weight normalization by an explicit proof from the three existing facts before rewriting the bound. Native `WeightZeroConsumerChecks.upper_bound` verifies exactly this normalization shape `i ≤ weight r 0 → i ≤ 0` using the explicit three-fact result; it is a fragment, not a replay of the full Index theorem. Reversed equality and pointwise function equality also compile. Also rebuild every downstream module to detect other implicit consumers. Source audit examined all project weight/sum_eq_zero/zero_div matches; no independently named duplicate proof of this exact zero-weight identity was identified. Box.weight_eq_zero_iff is a stronger separate statement, not an extra explicit call.

## Phase 6 — Positive composition and call accounting

The following exact target proof compiles:

```lean
example {σ : Type*} [Fintype σ] (r : σ → ℕ) : Roth.weight r 0 = 0 :=
  Finset.sum_eq_zero fun j _ ↦
    (congrArg (fun x : ℝ ↦ x / (r j : ℝ)) (Nat.cast_zero (R := ℝ))).trans (zero_div _)
```

Exactly **three distinct existing mathematical fact references and three instantiated library applications**: `Finset.sum_eq_zero`, `Nat.cast_zero`, `zero_div`. `congrArg` and equality transitivity are structural proof combinators; they add no arithmetic fact. `Roth.weight` unfolds definitionally, and evaluation of the zero Finsupp at `j` reduces definitionally to natural zero. Crucially, **natural-zero casting to real zero is not definitional equality**; `Nat.cast_zero` is counted explicitly. The initial rejected two-fact attempt demonstrates this distinction.

This is not merely a closing `simp [defs...]` composition, so Phase6b's BORDERLINE rule for an opaque simplifier proof is not being used as an automatic NO. The independent mathlib-only module defines the exact formula, guards `#check_failure Roth.weight_zero`, and proves it by the same explicit term. It imports no Roth code, preventing own/downstream simp circularity. The separate replay of the original simp proof is supplementary evidence only.

At the abstract interface, `map_zero (Finsupp.weight w)` compiles for arbitrary ambient `σ` and arbitrary `AddCommMonoid M`; this is an existing result, not a newly proved helper. Replacing the unchanged project statement directly with it requires a representation bridge, so the three-fact proof certifies old-form composition while the explicit re-aim rule determines the final existing-result verdict. Accepted extensions include finite sets/functions over `DivisionSemiring` and infinite ambient support sums. Rejected attempts (missing additive structure, zero-instance diamond, omitted cast fact) are retained separately and excluded from accepted evidence.

Composition verdict: **COMPOSABLE**.

## Phase 7 — Verdict and actionable plan

**NO-mathlib-has-it**: after re-aiming the already redundant parent at `Finsupp.weight`, its zero law is existing `map_zero`. The native reciprocal bridge verifies the old notation. The independent three-fact proof remains valid evidence, but it does not override the command's explicit re-aim routing.

Proposed subsequent change: delete the theorem and handle the zero-weight normalization at the potential `Index.index_eq_zero_iff:105` simp consumer explicitly by the compiled composition, then rewrite the upper bound. There are **0 explicit named call sites**. Rebuild downstream modules because simplifier uses are not enumerated by text search. Alternatively preserve this readable simp API in **project-local `Roth/Box.lean`**, where the wrapper's semantics live; no Archive or satellite-library destination is warranted for elementary glue. This assessment itself makes no production changes.

All phase gates pass; no cost-based downgrade, unsupported absence claim, or unverified minimal-generalization claim. YES-specific upstream file/title/reviewer/grouping checklist is n/a. Current progress was read; no accepted YES verdict was inferred from a useful lemma name. No unresolved verification questions remain.

## Phase 8 — Handoff

[Assessment](../evidence/Roth.weight_zero/assessment.json), [verification](../evidence/Roth.weight_zero/verification.json), [overview entry](../evidence/Roth.weight_zero/overview-entry.json), [current copy manifest](../evidence/Roth.weight_zero/copy-manifest.json), [portable validator](../evidence/Roth.weight_zero/validate.py). Root acceptance pending independent review. The validator checks the current manifest; a later historical worker manifest never substitutes for it.

## Re-aim rule correction and supplemental verification

The initial report classified the old ratio representation by its three-fact
composition. That classification overlooked `mathlibable.md`, Mode B,
**Re-aim rule** (installed lines 1192–1207): when a parent is NO-mathlib-has-it
because a more general definition D′ exists, and D′ has the analogous law,
record the dependent lemma as NO-mathlib-has-it citing that law.
Parent `Roth.weight` was already verified against `Finsupp.weight`.
Its analogous law is existing `map_zero` for that bundled additive map.
This is a checked re-aim, not blind inheritance or an unsupported absence claim.

The [exact supplemental source](../evidence/Roth.weight_zero/reaim-executed.lean.txt)
proves the reciprocal bridge and `RawWeightReaimChecks.zero_via_existing_map` with
mathlib-only imports; [native receipt](../evidence/Roth.weight_zero/native-reaim.json)
has terminal success, no errors/warnings, and standard axioms only.
No Roth import or target theorem is used. The bridge is explicitly a proved
normalization step and is not counted as an existing library lemma.
At the re-aimed interface the law is one existing `map_zero` application.

Future action: coordinate parent migration to reciprocal `Finsupp.weight`,
then use `map_zero` and the existing quotient bridge at the consumers already
audited above. Keep a project-local compatibility wrapper until the parent
and complete dependent modules compile. No independent upstream preservation
theorem is needed. Existing original-form composition, caller fragments,
generality checks, literature and searches remain valid; production is unchanged.
The [correction record](../evidence/Roth.weight_zero/verdict-correction.json) preserves
the prior verdict and report hash. This changes the bucket, not the number
of completed declarations or the next declaration.
