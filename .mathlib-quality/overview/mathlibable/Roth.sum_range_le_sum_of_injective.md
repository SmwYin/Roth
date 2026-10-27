# Roth.sum_range_le_sum_of_injective

Verdict: **NO-mathlib-has-it**. The existing `Finset.sum_range_le_sum` is the same sharp discrete lower-bound law for any finite set of integers with any common lower bound. The project theorem specialises it to the integer image of an injective natural-valued family. The representation bridge is substantive normalization, not definitional equality or a claimed three-call proof.

## Phase 0 — baseline and scope

The declaration resolves at `Roth/Wronskian.lean:107–114`, public theorem, no sorry. Read the entire 224-line module and the local source-paper Wronskian section. The baseline `lake build` succeeded (2467 jobs); all **17** source/pin hashes were freshly checked and match its input manifest. Production files and Git were not changed. [Baseline](../evidence/Roth.sum_range_le_sum_of_injective/baseline-build.txt), [hash check](../evidence/Roth.sum_range_le_sum_of_injective/source-pin-check.json), [module](../evidence/Roth.sum_range_le_sum_of_injective/source-module.lean.txt), [canonical metadata](../evidence/Roth.sum_range_le_sum_of_injective/canonical-metadata.json).

## Phase 1 — statement and proof

For any l distinct nonnegative integers, their sum is at least 0+1+⋯+(l−1). Order of the family is irrelevant: sorting gives its kth member at least k. Equality is achieved by the first l natural numbers, including the empty case l=0. In the source-paper proof this ensures that the candidate leading degree of the Wronskian is nonnegative.

Full native elaborated type:
```lean
@Roth.sum_range_le_sum_of_injective : ∀ {l : ℕ} (d : Fin l → ℕ),
  Function.Injective d → ∑ ν, ↑ν ≤ ∑ ν, d ν
```
Here the sums and coercions in the conclusion are in ℕ. Parameters are implicit length `l`, family `d`, and injectivity witness `hd`. There is **no** coefficient type `K`, field or characteristic hypothesis despite surrounding section variables. The elaborator has already omitted them. Project dependencies: none. Mathlib proof dependencies: `Finset.sum_range_le_sum`, `Finset.card_image_of_injective`, `Finset.sum_image`, `Fin.sum_univ_eq_sum_range`, `Nat.cast_sum`, integer/natural cast embedding and cast-order reflection. The proof takes the finite image of d, maps it into ℤ, applies the bound with c=0, normalizes cardinality and sums, and reflects the inequality back to ℕ. [Native target and original replay](../evidence/Roth.sum_range_le_sum_of_injective/target-success.json), [executed source](../evidence/Roth.sum_range_le_sum_of_injective/target-executed.lean.txt).

## Phase 2 — preliminary checks

**SMALL**: an elementary finite-sum helper, not a new structure, not listed among the module's main results, and not an eponymous theorem. The enclosing namespace and Wronskian module do not make this helper a named-person theorem. One-line-definition test: **n/a, theorem**; source body has seven proof lines. No definition-only exemption is needed.

## Phase 3 — exhaustive literature

Exact web requests, complete-response SHA256/bytes, returned URL locators and honest access failures are in [web metadata](../evidence/Roth.sum_range_le_sum_of_injective/literature-web.json). Search bodies were not archived. The following are original summaries, not reproduced articles.

| Channel | Actual query/check | Result and relevance |
|---|---|---|
| General web, specific | `sum n distinct nonnegative integers at least n(n-1)/2 proof` | Mostly triangular-number material; no distinct named theorem established. |
| General web, general | `sharp lower bound sum distinct integers bounded below c cardinality` | Hits include related sumset bounds; these bound cardinalities of sumsets, not this sum of entries. |
| General web, aliases | `majorization smallest distinct integers triangular number lower bound` | Majorization and triangular numbers are related language, not a verified canonical name for this helper. |
| ChatGPT mathematics | Tool inventory | n/a: `ask_chatgpt_math` unavailable. Historical-formulation query could not be executed; other channels retained in full. |
| Local references | `clean.tex` §Wronskians, lines 157–204 | Direct primary project source: sorted distinct degrees and nonnegativity of D, lines 176–183. [Exact excerpt and source hash](../evidence/Roth.sum_range_le_sum_of_injective/local-reference.txt). |
| nLab | `site:ncatlab.org/nlab "majorization"`; direct `/nlab/show/majorization` | Search returns matrix-analysis notes §3.3 explaining rearrangements/majorization. Direct page inaccessible; do not claim it states the sharp discrete bound. |
| nCatLab | `site:ncatlab.org "finite" "ordered" "integers" sum`; direct `/nlab/show/finite+ordinal` | Direct access failed. No relevant categorical formulation found; a higher-category restatement would add no consequence here. |
| Stacks | `site:stacks.math.columbia.edu distinct integers sum lower bound`; repeated `"integers" "sum" "distinct"`; direct tag 09OP | Direct tag inaccessible; search hits (e.g. [0C5Z](https://stacks.math.columbia.edu/tag/0C5Z)) concern divisor components and unrelated sums. No useful standard form. |
| MathOverflow | `site:mathoverflow.net distinct nonnegative integers sum minimum`; opened [Sumset-distinct numbers](https://mathoverflow.net/questions/442361/sumset-distinct-numbers) | Confirms a dangerous near-miss: sum-distinct means all subset sums differ, much stronger than distinct entries. Not a substitute theorem. |
| Recent arXiv (2021-10-26–2026-10-26) | Three dated/distinct-integer queries plus explicit `after:2021-10-26 before:2026-10-27`; opened [Beker, 2501.10203](https://arxiv.org/abs/2501.10203), submitted 2025-01-17, revision 2026-10-02 | Primary abstract concerns k-configurations and sum-free subsets, not this elementary bound. Also returned Binary Two-Up Sequence (2022), unrelated. No modern replacement of the discrete minimum principle established. |

Literature synthesis: this is the minimum-sum principle for distinct integers, with the triangular-number bound as the nonnegative case. The local primary reference is exact; broad web results do not justify inventing a named theorem or asserting universal agreement. Translation of distinct integers bounded below by c gives the broader law summing c+k for k<card s. That broader form is directly implemented and documented in the pinned mathlib candidate.

## Phase 4a–b — parameters and generality

| Parameter/hypothesis | Current | Checked broader form or constraint | Outcome |
|---|---|---|---|
| Length | `l : ℕ`, no positivity | Empty family allowed | No weakening needed. |
| Domain | `Fin l` | Arbitrary `ι : Type*` with `[Fintype ι]` and `card ι` on left | Integer finite-family probe verifies universe-polymorphic indexing; existing finset form avoids an enumerated domain altogether. |
| Values | ℕ | ℤ with arbitrary common lower bound c | Native probe verifies; natural case is c=0 after embedding. |
| Injectivity | `Function.Injective d` | Finset representation encodes distinctness; a finset-local statement could use `Set.InjOn` | Cannot simply drop: d≡0, l=2 gives 1≤0. Native `decide` counterexample. No unverified extra generalization claimed. |
| Lower bound | Implicit nonnegativity of ℕ | Explicit `hc : ∀ i, c ≤ d i` over ℤ | Native generalized probe; removes the special role of zero. |
| Surrounding Field K | Not in actual type | Already omitted by elaboration | No Field-weakening claim. |

**STRICTLY NARROWER than the verified integer finite-set form**, already present upstream. This is a change of representation and a codomain/lower-bound restatement, not a claim that deleting a single binder generalizes the proof. The generalized family probe is evidence of compatibility, not a new existing mathlib replacement. No proposal requires new project infrastructure.

Verified broader statement:
```lean
{ι : Type*} → [Fintype ι] → (d : ι → ℤ) → Function.Injective d →
  (c : ℤ) → (∀ i, c ≤ d i) →
  (∑ n ∈ Finset.range (Fintype.card ι), (c + n)) ≤ ∑ i, d i
```
[Isolated exact source](../evidence/Roth.sum_range_le_sum_of_injective/isolated-executed.lean.txt), [native success](../evidence/Roth.sum_range_le_sum_of_injective/isolated-success.json).

## Phase 4c — all modern-idiom checks

| # | Question | Answer, restatement and downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of preambles? | No new class; the generalized domain uses the established `Fintype` class. Injectivity is a property of this function, not a global ambient structure. |
| 2 | Filters/topology? | No; finite discrete extremal inequality has no convergence. |
| 3 | Universal property? | No object construction characterized by a universal property. |
| 4 | Bundled substructure? | No closure property. Finset is the relevant existing finite collection representation. |
| 5 | Weaken field/module hierarchy? | No coefficient field survives in the theorem's type. |
| 6 | Higher categories? | No categorical data or useful downstream categorical API. |
| 7 | Concrete index/ordered structure? | Yes: `Fin l` → arbitrary finite domain, ℕ → lower-bounded ℤ. Enables `Finset.sum_range_le_sum`/`sum_Ico_le_sum`, arbitrary lower bounds and cardinality API. Arbitrary dense ordered groups are rejected: two distinct numbers 0 and 1/2 already violate a unit-spaced triangular lower bound. |
| 8 | Concrete-via-abstract diagnostic? | No named polynomial or Wronskian appears in the statement or body (zero occurrences), so no named-object witness abstraction. The body explicitly uses ℕ/ℤ casts and discrete cardinality; those concrete arithmetic properties remain essential. The finite-set restatement from row 7 captures the real abstraction. |
| 9 | False-generalization guard? | No false generalization in the verified ℤ/finite-domain proposal: distinctness and lower bound remain, same extremal problem. Dropping injectivity or moving to arbitrary dense ordered groups changes truth and is rejected. The rational guard was also verified natively: the Fin 2 family 0, 1/2 is injective and nonnegative but has sum below 1. |

Modern idiom available: **yes, already in mathlib**. The improvement is using the finite set of values with arbitrary lower bound; there is no new modernized contribution absent from mathlib. Translation into cardinality/interval form enables existing sharp-bound API directly.

## Phase 4.5 — infrastructure risk

n/a, theorem: no new typeclass path, reducible data definition, instance priority, universe-bearing data constructor or coercion. Each of the six risks (diamond, reducibility leak, noncanonical unfolding, priority collision, universe restriction, coercion ambiguity) is n/a for this declaration kind.

## Phase 4.6 — all proof-strategy checks

| # | Question | Applies? / finding |
|---|---|---|
| 1 | Epsilon-delta versus filters | No topology. |
| 2 | Element proof versus substructure inclusions | No ideal/submodule/subring content. Passing to a finite image is already appropriate. |
| 3 | Sequences versus nets | No limits or infinitary argument. |
| 4 | Explicit categorical construction versus universal property | No categorical construction. |
| 5 | Missing helpers mathlib should have | No missing mathematical helper: the sharp integer bound already exists. A Nat/Fin convenience corollary would shorten casts, but is not a new extremal law. |

Current strategy **MATHLIB-IDIOMATIC** for the old statement: use the existing sharp inequality and transport representations. Refactoring the *API use* is recommended because the wrapper has no callers and is redundant with a broader existing theorem. No cost argument affects the verdict.

## Phase 5 — five actual methods × three forms

[Raw complete formal-search requests and responses](../evidence/Roth.sum_range_le_sum_of_injective/formal-search.json); [exact source rg receipts](../evidence/Roth.sum_range_le_sum_of_injective/source-search.json); [pinned candidate file](../evidence/Roth.sum_range_le_sum_of_injective/candidate-module.lean.txt).

| Method | Current Fin/ℕ form | Literature lower-bounded integer form | Abstract finite-family/cardinality form |
|---|---|---|---|
| Lean-Finder | Exact broader `Finset.sum_range_le_sum` | Same hit | Same hit plus interval version |
| Loogle | `Function.Injective, Finset.sum, (_ ≤ _)`: unrelated `geomSum_injective` | `"sum_range_le_sum"`: exact candidate | `Finset.sum, Finset.card, Int, (_ ≤ _)`: candidate and interval variants |
| LeanSearch | Sum image/map and unrelated infinite-sum hits | Exact candidate, interval variant | `card_nsmul_le_sum` and unrelated hits; coarse bound alone is insufficient |
| rg | Full qualified-name spelling has no mathlib hit; project declaration only | Candidate at Int.Sum:72 | Source signature search also finds interval/bounded-sum laws; read entire candidate module |
| local names | Target project declaration | Candidate plus target | `Finset.sum_Ico_le_sum`; all three responses report index unavailable, so no absence inference |

External indices can differ from the pinned revision. Native `#check` and proof replay confirm pinned signatures. Conclusion: **found in mathlib as `Finset.sum_range_le_sum`, strictly broader discrete law**, not merely a list of components from which a new extremal principle must be proved.

## Phase 5.5 — statement shape

1. **Normal form:** finite set of distinct integer values bounded below by c, with range/interval sum bounded by its sum. Current Nat/Fin statement is an equivalent specialization; casts and image normalization are not defeq. Range form avoids natural subtraction/division used in a triangular-number closed form.
2. **Syntactic generality:** tested the finite integer family with arbitrary `Fintype ι`; proved it by image, cardinality, sum-image normalization. The canonical finset statement is exactly a one-call application of the existing theorem. Embeddings could package hd without changing content, but no untested embedding theorem is asserted.
3. **Superfluous arguments:** no extra class/parameter; hd is essential by counterexample, d and l determine both sums. The implicit l and explicit d/hd are reasonable for the retained spelling.

Overall: use existing canonical form; **no new upstream statement required**.

## Phase 6 — callers, inline audit and actual composition experiments

Internal use count **0**. Caller table: **empty**; the only qualified/bare-name source hit is its declaration. Source-level references are not a claim about exhaustive kernel/simp dependencies. This theorem carries no simp attribute. Inline grep found the same degree-sum expression in `coeff_wronskian_of_natDegree_injective`, but that theorem deliberately proves its coefficient identity for *all* families and never re-proves this injective bound; hence **0 inline re-derivations**. The later nonvanishing theorem also does not call it.

| Experiment | Result |
|---|---|
| Original Nat/Fin spelling using existing integer bound | PASS, exact cast/image proof replay, no project theorem dependency. Requires `exact_mod_cast` plus multiple normalizations, so do **not** count this as ≤3 existing calls. |
| Arbitrary finite integer family with c | PASS, one main existing theorem plus explicit cardinality/sum-image normalization; a convenience helper used only as experimental evidence. |
| Existing canonical finset form | PASS, `Finset.sum_range_le_sum hs` directly, one existing call. |
| Drop injectivity | False; native Fin 2 constant-zero counterexample PASS. |
| Dense ordered codomain with same unit spacing | False; native rational family 0, 1/2 counterexample PASS, with injectivity/nonnegativity proved. |

Phase 6 conclusion: old spelling **NOT-COMPOSABLE by the tested routes under the strict ≤3-call test**; its cast/simp bridge is real normalization. This records the tested routes, not a formal lower bound on the shortest possible proof. A closing simp-only bridge would itself be Phase-6b borderline. That does not undo Phase 5's positive same-law hit in a broader existing representation: the verdict is **NO-mathlib-has-it**, not NO-composable. We preserve the complete old-form proof so a reviewer can assess the bridge honestly.

The [dense-order guard](../evidence/Roth.sum_range_le_sum_of_injective/dense-success.json) and its [exact executed code](../evidence/Roth.sum_range_le_sum_of_injective/dense-executed.lean.txt) are accepted evidence. The [first decide attempt](../evidence/Roth.sum_range_le_sum_of_injective/dense-rejected.json) failed on noncomputable rational inverse and is retained separately as rejected evidence; final verification uses norm_num.

## Phase 7 — actionable verdict

**NO-mathlib-has-it**: `Finset.sum_range_le_sum`, `Mathlib/Algebra/Order/Group/Int/Sum.lean:72`; interval sibling `Finset.sum_Ico_le_sum` at line 57. Its c=0 instance on the natural image contains precisely this theorem. Injectivity establishes cardinality and permits reindexing, while Nat→Int casts preserve sums and order. These are representational bridges around an existing sharp theorem, not new mathematics.

Canonical one-call form:
```lean
example {s : Finset ℤ} {c : ℤ} (hs : ∀ x ∈ s, c ≤ x) :
    ∑ n ∈ Finset.range s.card, (c + n) ≤ ∑ x ∈ s, x := Finset.sum_range_le_sum hs
```
The old statement's full successful proof is archived; we do not pretend the canonical one-call form is the identical elaborated Nat/Fin goal.

**Every-caller refactor plan:** there are zero explicit callers to update. Delete the unused theorem at Wronskian:107–114 in a separately authorized cleanup; check whether its `Mathlib.Algebra.Order.Group.Int.Sum` import then becomes unnecessary. If a future Wronskian degree argument needs it, apply the existing theorem to the image at that site with the archived cast/image normalization. If maintaining the pedagogical Nat/Fin spelling is preferred, keep it as a private local helper in `Roth/Wronskian.lean`; no Archive/satellite library is appropriate because mathlib already owns the general arithmetic content.

No production edit was performed during assessment. No upstream PR, reviewer selection or YES grouping is applicable. No unresolved mathematical verification or user decision is needed; convenience-API taste is a future upstream discussion, not a blocker.

## Phase 8 — evidence and portability

The [verification record](../evidence/Roth.sum_range_le_sum_of_injective/verification.json) identifies exact executed sources and native receipts. [Portable validator](../evidence/Roth.sum_range_le_sum_of_injective/validate.py) checks the current copy manifest, accepted native success, standard axioms, source/pin hashes and report links in scratch or integrated layouts. Root acceptance remains pending until independent review. All accepted evidence uses only standard axioms and no sorry/new axioms/resource-limit changes.
