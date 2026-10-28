# Roth.Θ_mono — NO-mathlib-has-it

## Phase 0 — Baseline and scope

Resolved public theorem at `Roth/Theta.lean:134`, canonical declaration191/293. The declaring module was read in full, including the two complete callers and their Lemma7 context. The module develops polynomial-index suprema and Roth Lemmas5–7. The reusable baseline `lake build` succeeded with2467 jobs and no reported errors/warnings; all17 source/pin hashes were freshly compared and match. No production source, pin or Git changes were made by this assessment.

Evidence: [baseline-build.txt](../evidence/Roth.Θ_mono/baseline-build.txt), [source-hashes.json](../evidence/Roth.Θ_mono/source-hashes.json), [input-manifest.json](../evidence/Roth.Θ_mono/input-manifest.json), [Theta.lean.txt](../evidence/Roth.Θ_mono/Theta.lean.txt), [canonical-target.json](../evidence/Roth.Θ_mono/canonical-target.json).

## Phase 1 — Exact content

For fixed denominator and degree-weight vectors, increasing the permitted coefficient height enlarges the family of admissible nonzero integer polynomials. Consequently the supremum of their indices cannot decrease, provided the smaller family is nonempty. The statement uses `1 ≤ B` to obtain that nonemptiness. The proof keeps every polynomial and numerator vector unchanged, composes the coefficient inequality with `B ≤ B′`, and applies conditional supremum monotonicity.

Full native type, including all implicit parameters:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {B B' : ℝ},
  1 ≤ B → B ≤ B' → ∀ (q : σ → ℕ) {r : σ → ℕ}, Roth.Θ B q r ≤ Roth.Θ B' q r
```

The type has `[Fintype σ]`, and no `[DecidableEq σ]`. There is no nonempty-variable, positive-denominator, positive-weight or strict-height hypothesis. `Θ` is definitionally `sSup (indexSet B q r)`; the arithmetic family inclusion is not definitional.

Evidence: [native-type.json](../evidence/Roth.Θ_mono/native-type.json), [theta-mono191-original-executed.lean.txt](../evidence/Roth.Θ_mono/theta-mono191-original-executed.lean.txt), [theta-mono191-original-receipt.json](../evidence/Roth.Θ_mono/theta-mono191-original-receipt.json).

## Phase 2 — Preliminary checks

BIG by the command's explicit module-main-results criterion: `Θ_mono` is listed in the module's Main results, although its order-theoretic content is elementary. This classification does not reduce the exhaustive search. One-line definition-only test: n/a, kind is theorem. Its proof is three substantive tactic lines; no definition exemption is being invoked.

## Phase 3 — Exhaustive literature

Every requested channel was actually queried; the optional `ask_chatgpt_math` tool is unavailable. The protocol's informal nine-channel label is not a reason to invent a channel: the three general forms and each named source are recorded below. Metadata archives contain exact requests, serialized returned-response SHA256/bytes, titles/URLs/locators, access statuses and original summaries; full web bodies are not archived. No credential URL redaction was needed.

| Channel/query | Result and interpretation | Evidence |
|---|---|---|
| General specific: `Roth theorem polynomial index Theta supremum monotone coefficient bound` | Princeton Diophantine notes, Chapter17, identify the index setting; abstract inclusion law is not a new Roth phenomenon. | [web0-metadata.json](../evidence/Roth.Θ_mono/web0-metadata.json) |
| General standard: `supremum monotonicity subset nonempty bounded above ordered set` | Penn analysis search excerpt defines the least upper bound for nonempty bounded real sets. | [web0-metadata.json](../evidence/Roth.Θ_mono/web0-metadata.json) |
| General aliases: `least upper bound inclusion monotonicity supremum` | Same order-theoretic concept; nonempty and bounded clauses matter for real-valued suprema. | [web0-metadata.json](../evidence/Roth.Θ_mono/web0-metadata.json) |
| Local references: `nondecreasing`, `increasing.*B`, `supremum`, `\Theta` in clean.tex | §5 lines665–669 states well-definedness and monotonicity because allowed polynomials increase. | [local-literature.json](../evidence/Roth.Θ_mono/local-literature.json), [clean-section5-excerpt.tex.txt](../evidence/Roth.Θ_mono/clean-section5-excerpt.tex.txt) |
| nLab: `site:ncatlab.org/nlab supremum monotone subset` | `join`, Definition/Special cases, gives the least-upper-bound universal property and distinguishes zero-ary join/bottom. Direct opening failed unsupported XHTML400; search excerpt available. | [web1-metadata.json](../evidence/Roth.Θ_mono/web1-metadata.json), [web3-metadata.json](../evidence/Roth.Θ_mono/web3-metadata.json) |
| nCatLab: `site:ncatlab.org/ncatlab supremum monotonicity` | Returned nLab pages, no exact namespace hit. This is an honest search outcome, not evidence of mathematical absence. | [web1-metadata.json](../evidence/Roth.Θ_mono/web1-metadata.json) |
| nCatLab retry: `site:ncatlab.org/ncatlab "supremum" "order"` | Again nLab results only; no higher-categorical reformulation necessary. | [web2-metadata.json](../evidence/Roth.Θ_mono/web2-metadata.json) |
| Stacks: `site:stacks.math.columbia.edu supremum ordered set` | Tag05N1, §3.4, direct lines20–21, discusses ordinal supremum. A different object, not the real-supremum law sought here. | [web1-metadata.json](../evidence/Roth.Θ_mono/web1-metadata.json), [web3-metadata.json](../evidence/Roth.Θ_mono/web3-metadata.json) |
| MathOverflow: `site:mathoverflow.net supremum monotone inclusion complete lattice` | Question331490, answers79,108–113 discuss lattices of lower sets; supports order-theoretic framing but no special arithmetic law. | [web2-metadata.json](../evidence/Roth.Θ_mono/web2-metadata.json), [web4-metadata.json](../evidence/Roth.Θ_mono/web4-metadata.json) |
| Recent arXiv: `site:arxiv.org Roth theorem polynomial index height after:2021-10-27` | Results concern additive-combinatorial Roth theorems; 2307.00271 is about corners. No matching Diophantine index-monotonicity contribution located. | [web2-metadata.json](../evidence/Roth.Θ_mono/web2-metadata.json) |
| Recent arXiv retry: `site:arxiv.org "Roth" "Diophantine" "formalization" after:2021-10-27` | No results. Opened2610.13204:9Oct2026 submission,12Oct revision, withdrawn; unrelated nonlinear additive Roth theorem, excluded as mathematical support. | [web4-metadata.json](../evidence/Roth.Θ_mono/web4-metadata.json) |
| Optional mathematical second opinion | n/a: `ask_chatgpt_math` unavailable. | Tool inventory/contract limitation |

Direct primary-source access also tried the Princeton PDF (400 timeout) and Penn analysis page (403 Forbidden). These access failures are preserved and are not represented as full-page reading. Authoritative mathematical support for the exact local claim is the supplied clean.tex; the abstract law is independently verified against pinned mathlib. Primary locators: [Penn analysis](https://www2.math.upenn.edu/~gressman/analysis/01-completeness.html), [Princeton Diophantine notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), [nLab join](https://ncatlab.org/nlab/show/join), [Stacks05N1](https://stacks.math.columbia.edu/tag/05N1), [MO331490](https://mathoverflow.net/questions/331490/reference-request-lower-sets-of-a-preorder-form-a-lattice), [arXiv2610.13204 withdrawn](https://arxiv.org/abs/2610.13204).

Literature synthesis: this is monotonicity of a supremum under inclusion. Standard real formulation assumes the smaller set nonempty and the larger set bounded above; the abstract conditionally complete lattice statement has precisely the same clauses. Complete lattices allow all subsets, a different interface. The Roth source specializes the general law to height-filtered integer polynomial families. No historical formulation change relevant to the verdict was located; a negative search result is not a claim of novelty or absence.

## Phase 4a — Parameters and generality

| Parameter/hypothesis | Role; weakening audit |
|---|---|
| `σ : Type*` | Arbitrary universe and arbitrary finite variable type; no forced enumeration such as Fin n. |
| `[Fintype σ]` | Needed by the fixed Θ/index parent interface. Not claimed removable. The isolated abstract set law has no polynomial index and is a different interface. |
| `B B′ : ℝ` | Heights in the supplied coefficient-bound definition. Generic set monotonicity replaces heights by arbitrary nested sets, not by changing the meaning of integer-polynomial coefficients. |
| `hB : 1 ≤ B` | Used by the original proof to witness the smaller set's nonemptiness. Actual theorem can drop it, proved natively by the nonnegative-target real-supremum route. |
| `hBB′ : B ≤ B′` | Used exactly to enlarge every coefficient bound via `(hRc d).trans hBB′`; inclusion is the substantive representation bridge. No unsupported deletion claimed. |
| `q : σ → ℕ` | Fixed rational denominator vector; no positivity/coprimality hypothesis on q itself. Coprimality lives in each indexSet witness. |
| `r : σ → ℕ` | Fixed degree/weight vector; zero entries allowed. No positivity introduced. |
| `[DecidableEq σ]` | Already omitted from elaborated theorem; no further weakening to claim. |

## Phase 4b — Verified generality verdict

STRICTLY NARROWER in the single concrete hypothesis `hB`. Native project probe proves:

```lean
theorem all_bounds {σ : Type*} [Fintype σ] {B B' : ℝ} (hBB' : B ≤ B')
    (q : σ → ℕ) {r : σ → ℕ} : Roth.Θ B q r ≤ Roth.Θ B' q r := by
  exact Real.sSup_le
    (fun _ hx ↦ le_csSup (Roth.indexSet_bddAbove B' q) (height_subset hBB' q r hx))
    (Roth.Θ_nonneg q)
```

`height_subset` is a new local proof with the full polynomial membership/witness transport, not an existing mathlib lemma. `monotone_all` packages the strengthened result as `Monotone (fun B ↦ Θ B q r)`. Both pass with all original parent instances. This proof does not need to assert or reproves an arithmetic threshold for the full family. It covers empty families using the nonnegativity of the target supremum. The isolated analogous theorem explicitly supplies target-set nonnegativity. No conclusion is inferred merely from a unit witness failing at small heights.

Cost: CHEAP local strengthening, irrelevant to the mathlib verdict because the abstract monotonicity law already exists. Evidence: [project-probe.lean.txt](../evidence/Roth.Θ_mono/project-probe.lean.txt), [theta-mono191-project-executed.lean.txt](../evidence/Roth.Θ_mono/theta-mono191-project-executed.lean.txt), [theta-mono191-project-receipt.json](../evidence/Roth.Θ_mono/theta-mono191-project-receipt.json).

## Phase 4c — Modern idiom, all nine checks

| # | Question | Answer, proposal, concrete consequence |
|---|---|---|
|1| Typeclasses replacing preambles | Already `[Fintype σ]`; use existing `[ConditionallyCompleteLattice α]` for abstract sSup law. No new class. |
|2| Filters replacing metric/sequences | No limits, metric or convergence argument. n/a. |
|3| Universal-property formulation | Yes, IsLUB characterization explains the law, and existing csSup_le_csSup exposes its useful sSup form; no new construction. |
|4| Bundled substructure | No closure condition: admissible polynomials are height-filtered sets, generally not subrings/modules. Bundling would change content. |
|5| Weaker algebra hierarchy | Order theorem already works over ConditionallyCompleteLattice; polynomial arithmetic stays in project membership/boundedness premises. |
|6| Higher categories | No higher-categorical data; poset join viewpoint adds no needed downstream power. |
|7| Concrete ℝ to abstract order | Yes: existing csSup_le_csSup supports arbitrary conditionally complete lattices and composes with le_csSup, csSup_le, IsLUB API. |
|8| Concrete-via-abstract diagnostic | Fires: excluding the statement, Θ appears0 times in the three-line proof body. First line invokes csSup_le_csSup; remainder only transports family witnesses and a bound. Propose the already-existing abstract law, keeping the arithmetic inclusion local. |
|9| False-generalization guard | Preserve boundedness/nonempty in generic real sSup law. Isolated ∅⊆{−1} counterexample compiles. ℝ is not CompleteLattice/OrderBot; csSup_le_csSup′ requires ConditionallyCompleteLinearOrderBot. The stronger all_bounds is valid only using actual target nonnegativity. |

Modern idiom available: yes, already implemented in mathlib. Abstracting separates the order proof from the polynomial-height inclusion and lets arbitrary index families reuse it. That is organizational reuse, not a new upstream theorem. No rewrite to extended reals/NNReal is needed or silently substituted.

## Phase 4.5 — Infrastructure risk

n/a: theorem. Typeclass diamond, reducibility leak, noncanonical unfolding, instance-priority collision, universe-polymorphism and coercion-ambiguity risk rows are each n/a because this proof declaration adds no instances, data, coercions or new definitional equations. The definitional Θ bridge is independently checked, without changing reducibility attributes.

## Phase 4.6 — Proof strategy, all five checks

| # | Strategy diagnostic | Finding |
|---|---|---|
|1| ε–δ versus filters | No topology; no change. |
|2| Element algebra versus inclusion | The order part uses set inclusion correctly; witness destructuring proves exactly the project height inclusion. A named local inclusion helper can organize it. |
|3| Sequences versus nets | No sequences/limits; no change. |
|4| Explicit construction versus universal property | csSup_le_csSup already packages the least-upper-bound property; retain it. |
|5| Missing helper mathlib should have | Generic monotonicity already present. New height_subset belongs with project RSet/indexSet unless those arithmetic interfaces are independently redesigned. Substantive uniform boundedness is not solved by this order law. |

MATHLIB-IDIOMATIC for the original strategy. Optional local strengthening uses Real.sSup_le and nonnegativity instead of requiring nonemptiness; it is a verified small theorem, not evidence for a novel generic law.

## Phase 5 — Actual five-method mathlib search

All five methods executed on current, literature-standard and abstract forms. Complete raw formal receipts: [formal-search.json](../evidence/Roth.Θ_mono/formal-search.json). Source receipts: [rg-current.json](../evidence/Roth.Θ_mono/rg-current.json), [rg-literature.json](../evidence/Roth.Θ_mono/rg-literature.json), [rg-abstract.json](../evidence/Roth.Θ_mono/rg-abstract.json).

| Method | Current form | Literature-standard form | Abstract form |
|---|---|---|---|
| Finder | `Roth polynomial index supremum monotone coefficient bound`; unrelated Chevalley bounds | `supremum monotonicity nonempty bounded sets subset`; csSup_le_csSup hit | `conditionally complete lattice supremum monotone subset nonempty bounded above`; csSup_le_csSup hit |
| Loogle | `"Θ_mono"`; no hits | `sSup ?s ≤ sSup ?t`; sSup_le_sSup and conditional variants | `"csSup_le_csSup"`; relevant general and directed partial-order variants |
| LeanSearch | Same current natural-language query; unrelated coefficient bounds | Same literature query; IsLUB.mono and supremum API | Same abstract query; isLUB_csSup and conditional API |
| rg pinned source | Qualified current name absent | csSup_le_csSup at Basic:209 | csSup_le_csSup and related variants; no inference of project-law absence from a failed query |
| Local search | `Θ_mono`: index unavailable, not absence | `csSup_le_csSup`: exact and directed variants | `csSup_le_csSup`: exact and directed variants |

Conclusion: found in mathlib as `csSup_le_csSup`, more general form, at `Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:209`:

```lean
{α : Type*} [ConditionallyCompleteLattice α] {s t : Set α}
(ht : BddAbove t) (hs : s.Nonempty) (h : s ⊆ t) : sSup s ≤ sSup t
```

Pinned source proof is `csSup_le hs fun _ ha => le_csSup ht (h ha)`. This signature and the actual isolated application were both verified natively. `csSup_le_csSup′` at548 is a different bottom-order theorem; native signature confirms ConditionallyCompleteLinearOrderBot, so it cannot justify dropping nonempty for arbitrary ℝ. `Real.sSup_le` is at `Mathlib/Algebra/Order/Archimedean/Real/Basic.lean:222`, requiring a nonnegative proposed bound. External search index versions may differ from this pin; pinned source/native checks control the conclusion.

Evidence: [mathlib-inputs.json](../evidence/Roth.Θ_mono/mathlib-inputs.json), [theta-mono191-isolated-executed.lean.txt](../evidence/Roth.Θ_mono/theta-mono191-isolated-executed.lean.txt), [theta-mono191-isolated-receipt.json](../evidence/Roth.Θ_mono/theta-mono191-isolated-receipt.json).

## Phase 5.5 — Three statement-shape checks

Normal form: specialize `sSup s ≤ sSup t`; equivalent presentations are the Θ wrapper, the sSup-of-indexSet statement and `Monotone (fun B ↦ Θ B q r)`. Existing mathlib's conditional sSup law is canonical. This theorem is an inequality, so the simplifier RHS convention for equivalence normal forms is not applicable. No pairwise equivalence web is proposed.

Syntactic generality: both the original implication form (`replacement`) and `Monotone` form (`monotone_all`) actually compiled. The latter makes repeated local applications easier and removes a redundant1≤B premise; retaining the implication wrapper preserves current call signatures.

Superfluous-argument audit: hB is semantically redundant by all_bounds; `[DecidableEq]` already absent. σ/Fintype/q/r remain part of the fixed parent interface. B/B′ specify the two heights and hBB′ supplies the verified inclusion direction; none is mechanically erased here. The generic s/t formulation changes interface and its nonempty hypothesis is not deletable without another condition, as the isolated counterexample shows.

Overall: RESTATE-BEFORE-SHIP if maintaining a polished local API: drop hB and optionally use Monotone. For upstream, reuse the existing abstract theorem, so no separate shipping proposal follows.

## Phase 6.0 — Complete caller and inline audit

Fresh lexical search uses `rg --no-ignore` over all production Roth/ and Roth.lean, cross-checked against git grep and the canonical inventory. Four source occurrences: docline34, declaration134, call758, call790. Exactly two body call occurrences in two private declarations, both within Theta.lean; zero external-to-file callers, zero explicit statement/type uses. Under the command's exclusion-of-declaring-file convention, internal-use count is0; total within-project body uses is2. The canonical kernel audit independently sees the two direct value consumers and0 type consumers; this is not a claim about the full kernel/simp dependency closure.

| Caller | Actual use/refactor |
|---|---|
| private Roth.theta_scaled_unique_le_aux, Theta:758 | `(Θ_mono hM1 hM _).trans ...`; inline csSup_le_csSup for Unit variables at heights M and q₁^(δ(lr₁)), using boundedness of the larger indexSet, nonemptiness from hM1 and coefficient inclusion from hM. Retain full Θ_unique_le/log/arithmetic continuation. |
| private Roth.theta_prefix_lt_aux, Theta:790 | `(Θ_mono hM1 hM _).trans_lt ...`; inline same law on Fin(n+1), q∘castSucc and scaled weights. Retain hCeq, ih and all finite-index/growth arithmetic. |

Both entire callers, not just schematic prefixes, were replayed natively with explicit hmono proofs and full witness transport, without invoking Θ_mono. Original assumptions including hM1 are retained. There are no auxiliary private-name bridges. Inline search finds no separate rederivation of this height-monotonicity law; csSup/Real.sSup uses elsewhere concern other bounds. This theorem is not tagged simp, and its two uses mean it is not dead code.

Evidence: [callers-rg.json](../evidence/Roth.Θ_mono/callers-rg.json), [callers-git.json](../evidence/Roth.Θ_mono/callers-git.json), [callers.json](../evidence/Roth.Θ_mono/callers.json), [inline-audit.json](../evidence/Roth.Θ_mono/inline-audit.json), [caller-probe.lean.txt](../evidence/Roth.Θ_mono/caller-probe.lean.txt), [theta-mono191-callers-executed.lean.txt](../evidence/Roth.Θ_mono/theta-mono191-callers-executed.lean.txt), [theta-mono191-callers-receipt.json](../evidence/Roth.Θ_mono/theta-mono191-callers-receipt.json).

## Phase 6 — Actual composition and parent re-aim

Parent Θ was assessed as redundant with sSup. Independently re-aiming this law at sSup finds the exact existing analogous law csSup_le_csSup. The bridge Θ=sSup indexSet is rfl. Native project `replacement` applies it after separately proving actual height_subset:

```lean
exact csSup_le_csSup (Roth.indexSet_bddAbove B' q) (Roth.indexSet_nonempty hB q r)
  (height_subset hBB' q r)
```

Honest old-form call accounting: this is one existing mathlib order call supplied with TWO project helper proofs and ONE new project-specific inclusion proof. It is not a ≤3-existing-mathlib-call-only derivation of the original arithmetic statement. Boundedness uses the substantive project index_le_card argument; nonemptiness uses an admissible polynomial. Neither is counted as a mathlib block. No closing simp-composition is used to force NO. Isolated `abstract_mono` is exactly one existing call and axiom-free; the actual representation bridge and both caller specializations compile.

Attempt2, strengthening: `Real.sSup_le` + `le_csSup` + target nonnegativity proves the actual law for all heights. The generic isolated version explicitly assumes all target values nonnegative and uses `Real.sSup_nonneg`. This is a new three-call nonnegative-real schema, not claimed an existing named law. Its project specialization still uses project boundedness/inclusion/nonnegativity. The literal ∅⊆{−1} guard demonstrates why plain real subset monotonicity alone fails. There is no inferred complete lattice on ℝ and no fixed-interface Fintype weakening.

Composition conclusion: the re-aimed law is an EXISTING-API HIT; strict old-form mathlib-only composition not established. The binding parent re-aim rule selects NO-mathlib-has-it, irrespective of the nontrivial project witness bridge. The hB weakening does not create a new upstream gap where the underlying generic law is already present.

## Phase 7 — Actionable verdict

**NO-mathlib-has-it.** Existing declaration: `csSup_le_csSup`, `Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:209`. This is an independently verified re-aim at the sSup parent, with the actual arithmetic representation bridge, nonempty/boundedness premises and all callers checked. It is not blanket inheritance from Θ and does not assert that all arithmetic helpers already exist in mathlib.

Alternative local destination: keep a convenient monotonicity wrapper, preferably the stronger all_bounds/Monotone version, in `Roth/Theta.lean` near the RSet/indexSet height API. For an elimination refactor, replace the exact two uses at758/790 using the explicit csSup_le_csSup hmono proofs in the complete caller archive. Argument order is larger-set BddAbove, smaller-set Nonempty, then subset. Do not delete the project boundedness/nonempty infrastructure as part of that replacement. This is a follow-up plan only; production remains unchanged.

Next action: no separate upstream PR for Θ_mono. Reuse the existing sSup law and implement the verified local refactor/strengthening only when undertaking that project change. Accepted earlier verdicts were read from progress: Θ/indexSet are NO-mathlib-has-it, indexSet_bddAbove remains BORDERLINE. No YES grouping/reviewer proposal is applicable to this NO verdict. No open upstream-design question blocks completing this read-only assessment.

## Phase 8 — Verification and handoff

Four complete clean native evidence sets: original/full-type/canonical audit; project bridge/inclusion/replacement and hB deletion; mathlib-only isolated theorem/nonnegative schema/counterexample; both complete caller replays. Disk receipts are success=true, partial=false, not timed out, with no failed dependencies/errors/warnings/recovered sorry. The raw isolated run_code format has diagnostics rather than items and no partial field. Axiom sets are subsets of propext, Classical.choice, Quot.sound; isolated abstract_mono is axiom-free. There is no pretty-printer elision. Zero rejected native attempts.

Canonical audit compares the exact ordered293 names, preserves private-name modules, and checks requested/unique/present/kernel-values all293. Target direct values are the two private callers and direct type consumers are empty. Native assertions are scoped to each new region while whole-file errors/axioms are checked. Exact source archives retain original execution requests/paths in raw receipts. No own/downstream theorem is used circularly in the replacement or caller proofs.

Portable validation checks every phase, current manifest hashes/bytes, all local evidence links, canonical order, all17 source/pin hashes, clean native outcomes, allowed axioms, four actual formal-search methods on each form plus pinned rg, web-channel coverage and the credential guard. Supporting evidence: [verification.json](../evidence/Roth.Θ_mono/verification.json), [validate.py](../evidence/Roth.Θ_mono/validate.py), [validation-receipt.json](../evidence/Roth.Θ_mono/validation-receipt.json). Worker completion is separate from root's pending independent acceptance.
