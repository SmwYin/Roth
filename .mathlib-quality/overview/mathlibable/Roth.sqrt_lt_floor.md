# Roth.sqrt_lt_floor — canonical 237

**Verdict: BORDERLINE-needs-human.** The strict estimate is useful and is not certified as a composition of at most three existing mathlib calls. Its conjunction with `Nat.floor_le` is a local convenience. The completed assessment leaves three concrete upstream API choices below; none blocks this read-only survey. No production files or pins changed.

## Phase 0 — baseline and scope

Fresh hashes of all 17 production sources/pins match the shared manifest and the clean 2467-job baseline. The declaring module is `Roth/MainLemma.lean`, which constructs the auxiliary polynomial for Roth's main lemma. The target is a public theorem at line 115, with no `sorry`, options or simp attribute. Both entire declaring and caller modules were read and archived. No file-end build is due at 237; the preceding accepted file-end Theta build remains applicable under identical source hashes.

Evidence: [fresh inputs](../evidence/Roth.sqrt_lt_floor/inputs.json), [baseline](../evidence/Roth.sqrt_lt_floor/baseline-build.txt), [MainLemma](../evidence/Roth.sqrt_lt_floor/source-MainLemma.lean.txt), [Main](../evidence/Roth.sqrt_lt_floor/source-Main.lean.txt).

## Phase 1 — exact statement and mathematics

For a real number at least two, its natural floor is strictly larger than its real square root, and casting that natural floor back to the reals gives a number at most the input. The implicit parameter `X` is arbitrary; the sole assumption is `2 ≤ X`.

The fresh `Lean.getConstInfo` type, printed with binder types enabled, is:

```lean
∀ {X : ℝ}, 2 ≤ X → √X < ↑⌊X⌋₊ ∧ ↑⌊X⌋₊ ≤ X
```

The original body packages the private `Roth.sqrt_lt_nat_floor_aux` with `Nat.floor_le`. The private arithmetic argument obtains `2 ≤ floor X`, uses `X < floor X + 1`, and proves `X < (floor X)^2`; positivity then permits the square-root comparison. The upper bound uses nonnegativity derived from the hypothesis. Natural floor, natural cast and real square root are essential distinctions; this is neither `Nat.sqrt X` nor floor applied to the square root.

The complete original MainLemma replay renamed only the target outside the canonical array. Its type is definitionally equal to the original. Full original kernel body and axioms were returned without printer elision. All replay public theorem axioms are standard. The ordered canonical array was generated directly from the tracked order, checked before execution, and verified at runtime: 293 requested, unique, present and with values. There are three direct body consumers, zero direct type consumers. These counts concern direct expression constants, not simp or transitive dependencies.

Evidence: [original exact source](../evidence/Roth.sqrt_lt_floor/original-executed.lean.txt), [raw native receipt](../evidence/Roth.sqrt_lt_floor/original-receipt.json), [type](../evidence/Roth.sqrt_lt_floor/native-type.json), [canonical consumers](../evidence/Roth.sqrt_lt_floor/canonical-consumers.json).

## Phase 2 — preliminary classification

SMALL: an elementary auxiliary inequality, not a new structure, named theorem or listed main result. The body has one substantive packaging line; the definition-only one-line exemption test is **n/a: theorem**. Its short spelling does not erase the new lower-bound proof hidden behind the private helper, and the helper's prefilter verdict is not inherited.

## Phase 3 — exhaustive literature

| Channel | Actual query / locator | Result and mathematical relevance |
|---|---|---|
| General specific | `"sqrt" "floor" "x ≥ 2"` | No exact named theorem identified. |
| General abstract | `floor function lower bound square root integer part inequality general ordered field` | Standard integer-part sandwich and ordered-field discussion. |
| General aliases / use | `Roth theorem coefficient bound floor X square root B1` | Diophantine context; unrelated additive-combinatorics Roth hits excluded. |
| Optional ChatGPT math | n/a: `ask_chatgpt_math` unavailable | No external second-opinion result invented. |
| Local clean.tex | §6, lines 1360–1389 | Uses a stronger `X > 4` estimate and explicitly retains non-strict upper bound. |
| nLab | `site:ncatlab.org/nlab floor integer part square root order adjoint` | Floor is right adjoint to integer inclusion; this explains the upper bound, not the nonlinear lower estimate. |
| Distinct nCatLab | `site:ncatlab.org/ncatlab floor function square root inequality` | Returned /nlab pages, no /ncatlab exact hit; namespace mismatch recorded. |
| Stacks | `site:stacks.math.columbia.edu floor function square root ordered field` | Field/algebraic-geometry results, no exact comparison; no broader AG formulation justified. |
| MathOverflow | `site:mathoverflow.net floor square root inequality generalization` | Related radical/floor problems, no replacement for this elementary estimate. |
| Recent arXiv | `site:arxiv.org floor square root inequality after:2021-10-28 before:2026-10-29` | Date-window query executed; returned topics differ and do not establish a relevant new generality. |
| Primary follow-up | Edinburgh Number Theory Problem Sheet 1, page 1, exercises 2–3 | Gives the floor sandwich and the commuting floor/square-root identity for nonnegative real input. |

The standard mathematical language is integer part, floor sandwich, and square-root comparison. The literature does not establish a canonical name for this conjunction. The local paper's stronger lower threshold is unnecessary: the native sharpness proof below confirms two is exact. The nLab adjunction concerns the inclusion of **ℤ** into ℝ. Natural floor needs nonnegative real input for its cast counit/adjunction law; that is automatic from `2 ≤ X` here. No global `Nat.cast ⊣ Nat.floor` over all ℝ is claimed. Order adjunctions supply one component but alone say nothing about squaring or its threshold. No modern categorical reformulation of the entire inequality follows merely from the adjunction viewpoint.

Web artifacts retain exact requests, returned-response SHA256/byte/status, clean locator metadata and original concise summaries only. They do not persist full articles or search-result bodies. Primary sources: [Edinburgh problem sheet](https://webhomes.maths.ed.ac.uk/~chris/NTh/wkp1_12sol.pdf), [nLab floors](https://ncatlab.org/nlab/show/floor). Evidence: [general queries](../evidence/Roth.sqrt_lt_floor/web-general.json), [nLab](../evidence/Roth.sqrt_lt_floor/web-nlab.json), [nCatLab](../evidence/Roth.sqrt_lt_floor/web-ncatlab.json), [Stacks](../evidence/Roth.sqrt_lt_floor/web-stacks.json), [MathOverflow](../evidence/Roth.sqrt_lt_floor/web-mathoverflow.json), [arXiv](../evidence/Roth.sqrt_lt_floor/web-arxiv.json), [primary follow-up](../evidence/Roth.sqrt_lt_floor/web-primary.json), [local reference receipt](../evidence/Roth.sqrt_lt_floor/literature-local.json).

## Phase 4a — generality status

| Parameter / assumption / representation | Audit and actual experiment |
|---|---|
| Real `X` | Arbitrary already; no dependency on `mainCoeffBound`, rpow, dimension, polynomial or Diophantine hypotheses. |
| `2 ≤ X` | Sharp: compiled `√X < floor₊ X ↔ 2 ≤ X` and full-conjunction iff. Every `X < 2` fails; explicit zero, one and negative-one checks also compile. |
| Non-strict endpoint | `X = 2` compiles, with upper equality. Strict upper bound is invalid at integer inputs. |
| Real square root | Replacing ℝ by an arbitrary field while retaining `Real.sqrt` is ill typed. A new semantic witness `y` satisfying `y² ≤ X` supports a real algebraic extension, rather than a mechanical type substitution. |
| Natural floor | Correct for natural coefficient bounds. Integer floor is an alternative representation requiring a bridge; the current threshold already ensures nonnegativity, so truncation causes no loss here. |
| Implicit parameter / sign assumptions | No redundant explicit hypothesis; `0 ≤ X` is derivable, not an additional obligation. |

## Phase 4b — verified generality verdict

**Original-form verdict: MAXIMALLY GENERAL for its sole numerical hypothesis; `2 ≤ X` is sharp.** The broader witness form below is a verified algebraic representation extension, rather than a mechanical weakening retaining `Real.sqrt`.

For the unchanged square-root statement the hypothesis is maximally weak: removing or lowering the threshold is refuted by the iff. A broader algebraic kernel was **actually proved**, including a rational witness:

```lean
theorem floorSquare {K : Type*} [Semiring K] [LinearOrder K] [IsStrictOrderedRing K]
    [FloorSemiring K] {X : K} (hX : 2 ≤ X) : X < (⌊X⌋₊ : K) ^ 2

theorem rootBound {K : Type*} [Semiring K] [LinearOrder K] [IsStrictOrderedRing K]
    [FloorSemiring K] {X y : K} (hX : 2 ≤ X) (hy : y ^ 2 ≤ X) : y < (⌊X⌋₊ : K)
```

The semiring proof first proves `floor X + 1 ≤ (floor X)^2` in ℕ and casts it; an attempted direct generic `nlinarith` transfer failed and is preserved separately. The root witness hypothesis has independent mathematical content and is satisfied by `Real.sqrt` through `Real.sq_sqrt`; it is not a disguised assumption of the desired floor inequality. This new generic proof is **not existing mathlib API**, and no NO verdict follows from composing it with `Nat.floor_le`. The final power-API experiment below shows that `floorSquare` itself is an existing three-block composition. Choosing a broader root-witness interface remains an API design question, not a claim that the quadratic step is a missing primitive or a cost issue.

Evidence: [isolated exact source](../evidence/Roth.sqrt_lt_floor/isolated-executed.lean.txt), [accepted raw receipt](../evidence/Roth.sqrt_lt_floor/isolated-receipt.json). Initial rejected syntax/import and proof-transfer attempts remain in separately named rejected files and are never accepted proof evidence.

## Phase 4c — all nine modern-idiom checks

| # | Check | Finding and consequence |
|---|---|---|
| 1 | Hypotheses to classes | Existing `FloorSemiring` handles floor in the generic kernel; no bespoke floor predicate needed. The numerical threshold remains a value hypothesis. |
| 2 | Sequences to filters | No sequence, limit or topology in this pointwise estimate. |
| 3 | Construction to universal property | Floor has the existing adjunction interface, but the quadratic gap still needs arithmetic. No new universal-property construction is proposed. |
| 4 | Sets to bundled substructures | No closure predicate, subspace or set presentation to replace. |
| 5 | Weaker algebra hierarchy | The quadratic kernel compiles over an ordered semiring, with no division, subtraction or real completeness. A later power-API experiment also derives it from three existing building blocks; it is not a missing primitive. |
| 6 | Higher categorical version | No higher-categorical mathematical content; poset adjunction supplies only the floor component. |
| 7 | Concrete index to general order | ℕ is the target of natural floor and the coefficient bound, not an incidental index. `FloorSemiring K` abstracts the ambient order while retaining that meaning. |
| 8 | Concrete-via-abstract | The public body hides the named sqrt/floor objects in one private call, so the helper was expanded and read. Its real use is square-root comparison plus the generic quadratic gap. The compiled `rootBound` witness captures that mechanism, with a rational witness showing it is not a generality of one. |
| 9 | False-generalisation guard | `hy : y² ≤ X` preserves the lower-comparison mechanism. Arbitrary ordered fields need not possess a chosen square-root operation; silently retaining the notation would change/obscure meaning. Reject that unqualified widening. |

Modern abstraction available: yes for the algebraic kernel, with concrete downstream access to `Nat.floor_le`, `Nat.lt_floor_add_one`, `pow_le_pow_left₀` and `Real.sq_sqrt`. The original conjunction need not become a new abstraction; the useful API grain remains the upstream question. A final successful power route establishes the generic quadratic step using exactly `Nat.le_floor`, `lt_self_pow₀`, and `Nat.lt_floor_add_one`, with mechanical Nat-order/cast/transitivity transport. Its scratch name is new, but its mathematical content is already a three-block composition.

## Phase 4.5 — infrastructure risk

All six definition-only rows (typeclass diamond, reducibility leak, noncanonical unfolding, priority collision, universe forcing, coercion ambiguity) are **n/a: theorem**. Neither the target nor scratch propositions introduce instances or definitional equalities. The generic exploratory theorems merely consume existing floor and order instances.

## Phase 4.6 — proof strategy

| # | Check | Finding |
|---|---|---|
| 1 | Topology via filters | n/a: no topology. |
| 2 | Element algebra vs substructures | No substructure inclusion is involved; ordered scalar arithmetic is appropriate. |
| 3 | Sequences vs nets | n/a: no convergence. |
| 4 | Construction vs universal property | No new object constructed. Floor adjunction alone does not establish the quadratic comparison. |
| 5 | Missing helper API | The arbitrary-real floor/sqrt bridge and a chosen strict real comparison API are candidate additions. The generic quadratic gap itself composes from existing floor/power API, so it is not claimed as a missing primitive. |

Strategy verdict: MATHLIB-IDIOMATIC for the original square-root arithmetic; REFACTOR-RECOMMENDED for packaging if upstreamed: expose a selected strict/kernel lemma and obtain the non-strict upper bound separately. No cost-based decision is used.

## Phase 5 — all 15 formal search cells

Each linked cell preserves its exact request and full raw response; the source rows preserve exact command/stdout/stderr/exit. Finder and LeanSearch indexes differ from the pinned revision; actual candidate statements were checked in pinned source and native Lean. Local search reports `index: unavailable`, so text hits are useful but an empty result would not certify absence. The returned `MainLemmaPrivate236.sqrt_lt_floor` is an earlier scratch declaration, and `Roth.sqrt_lt_floor`/its private helper are project hits; none is counted as a mathlib positive.

| Form | Finder | Loogle | LeanSearch | rg | Local names |
|---|---|---|---|---|---|
| Current conjunction | Real/natural sqrt near matches | Chebyshev and class-number uses, not target | Nat.sqrt and natural-input floor-sqrt | No exact combination | `sqrt_lt` finds project and sqrt API |
| Standard floor sandwich | Integer sqrt lemmas | `Nat.lt_floor_add_one`, `floor_eq_iff` | Floor/sqrt building blocks | `floor_le`, `le_floor`, strict successor | `floor` finds floor interface |
| Abstract ordered floor/quadratic | `Nat.mul_lt_floor`, `div_two_lt_floor`, unit-gap | `Nat.le_floor` etc. | Floor and integer floor unit gap | Generic floor bounds; no certified quadratic replacement | `lt_floor` unit gap |

Cell files are `search-{current,standard,abstract}-{leanfinder,loogle,leansearch,rg,local_search}.json`, all in this declaration's evidence directory. Supplementary exact bridge searches return the natural-input identity, not the arbitrary-real bridge.

Pinned building blocks: `Nat.le_floor` (Floor/Defs:141), `Nat.floor_le` (Floor/Semiring), `Nat.lt_floor_add_one` (Floor/Semiring), `Real.sqrt_lt'` (Analysis/Real/Sqrt:235), `Real.nat_floor_real_sqrt_eq_nat_sqrt` (Sqrt:435), `Nat.sqrt_lt_self` (Data/Nat/Sqrt:62). `Nat.mul_lt_floor` and `Nat.div_two_lt_floor` live at Floor/Semifield:54/81 and are absent from the stable 18-import virtual environment. Their supplementary CLI probe has the explicitly authorized extra mathlib import; it does not modify or claim membership in the shared prefix.

Evidence: [pinned mathlib hashes](../evidence/Roth.sqrt_lt_floor/mathlib-inputs.json), [full-name grep](../evidence/Roth.sqrt_lt_floor/full-name-search.json), [sqrt/floor source search](../evidence/Roth.sqrt_lt_floor/sqrt-floor-full-source-search.json), [bridge Loogle](../evidence/Roth.sqrt_lt_floor/search-bridge-loogle.json), [bridge LeanSearch](../evidence/Roth.sqrt_lt_floor/search-bridge-leansearch.json).

## Phase 5.5 — statement shape

| Check | Conclusion |
|---|---|
| Normal form | Natural floor with explicit real cast is already the correct coefficient-bound representation. Other forms are `X < (floor X)^2`, a standalone strict inequality, or its sharp iff. No orthogonal equivalence should duplicate floor's established API. |
| Syntactic generality | The iff has canonical threshold on its RHS and has been compiled. Standalone lower bound avoids `.1` in two callers; `.2` can be `Nat.floor_le`. The third caller genuinely uses both, so the original is useful locally. |
| Superfluous arguments | `X` and `hX` are essential; sharp iff proves the necessity of the hypothesis. No extraneous typeclass or sign premise is present. |

Overall: RESTATE-BEFORE-SHIP for the public conjunction's API grain, while preserving all original caller signatures in any local refactor. Separating components is an API recommendation, not an assertion that the strict component already exists.

## Phase 6.0 — complete callers and inline audit

| Caller | Source use | Actual full-body validation and refactor |
|---|---|---|
| `Roth.mul_log_div_two_lt_log_mainCoeffBound`, MainLemma:149–154 | `(sqrt_lt_floor hX).1` | Supplies lower comparison to `Real.log_lt_log`; a local copy of the complete arithmetic proof replaces the projection. Original signature retained. |
| `Roth.three_small_factors`, MainLemma:180–210 | `(sqrt_lt_floor hX).1` inside `key` | Establishes positivity for `Real.lt_rpow_of_log_lt`; local arithmetic proof replaces projection. Complete proof including logarithmic bounds replays. |
| private `Roth.roth_product_bound_aux`, Main:481–501 | Destructures both projections at line494 | Separates a local complete lower proof and `Nat.floor_le`; mainCoeffBound/floor coercions elaborate unchanged. Complete signature retained. |

Three explicit executable references in three declarations: two in the declaring file, one in one external file. Fresh `rg --no-ignore` and tracked `git grep` agree. The broader floor/sqrt scan finds related counting bounds, not another derivation of this same strict square-root estimate. The theorem has no simp attribute; lexical counts are not generalized to hidden transitive or simp use.

The entire MainLemma and Main modules were replayed together with the target and private helper removed, local lower proofs inserted in the three actual callers, and upper bound separated in Main. Seven kernel type comparisons passed: all three callers and `main_lemma`, `roth_of_isIntegral`, `roth`, `roth_rat`. All seven returned standard axioms. Imported project declarations provide unchanged dependencies; this is an actual-context refactor check, not an isolated claim that those dependencies belong to mathlib. Publicizing the private Main caller in scratch merely exposes it for the signature comparison.

Evidence: [full callers](../evidence/Roth.sqrt_lt_floor/callers.json), [fresh source enumeration](../evidence/Roth.sqrt_lt_floor/source-search.json), [tracked enumeration](../evidence/Roth.sqrt_lt_floor/tracked-source-search.json), [inline scan](../evidence/Roth.sqrt_lt_floor/inline-search.json), [complete inline source](../evidence/Roth.sqrt_lt_floor/inline-executed.lean.txt), [clean receipt](../evidence/Roth.sqrt_lt_floor/inline-receipt.json).

## Phase 6 — composition experiments

1. Upper projection: `Nat.floor_le (by positivity)` is existing mathlib. Lower projection: `Real.sqrt_lt'` reduces it to a quadratic gap; establishing that gap uses the floor unit interval, cast lower bound, and nonlinear arithmetic. This is a new proof, not a ≤3-call composition. Packaging the private Roth proof with `Nat.floor_le` is not a mathlib-only composition.
2. Abstract root route: `rootBound hX (Real.sq_sqrt ...).le` plus `Nat.floor_le` compiles, but `rootBound` and its floorSquare kernel are newly proved here. They are not preexisting mathlib building blocks.
3. Nat.sqrt route: the pinned identity takes natural input and fails to directly prove the arbitrary-real bridge. The new bridge `⌊√X⌋₊ = Nat.sqrt ⌊X⌋₊` and a full route through `Nat.sqrt_lt_self` compile. Their proof contains substantive floor/cast/square transport, so this route does not certify an existing-only composition either.
4. Power route: `Nat.le_floor`, `lt_self_pow₀` at GroupWithZero/Basic:620, and `Nat.lt_floor_add_one` prove the generic quadratic gap using three mathematical building blocks, with Nat strictness/cast transport. The full original adds `Real.sqrt_lt'` and `Nat.floor_le` and positivity transport; this does not certify an at-most-three-call term for the full conjunction. The generic kernel is therefore **not** a missing primitive.
5. Semifield floor route: `Nat.div_two_lt_floor` supplies `X/2 < floor X` under `1 ≤ X`; the needed `√X ≤ X/2` is false at two, as verified. `Nat.mul_lt_floor` requires a parameter and ceiling threshold; it is not the target's uniform sharp threshold without a further proof. The supplementary CLI tests the general `exact?` route before introducing new lemmas; failure is only a failed search, not proof of global absence. The two candidate signatures and failure of the half-bound route at two are verified.

Conclusion: **NOT-COMPOSABLE in the required existing-only ≤3-call sense**. This is a bounded evidence claim, not a theorem that no unknown library composition can exist. Inlining complete proofs succeeds, which demonstrates refactor feasibility rather than absence of new content.

Evidence: [Nat.sqrt exact source](../evidence/Roth.sqrt_lt_floor/sqrt-route-executed.lean.txt), [Nat.sqrt receipt](../evidence/Roth.sqrt_lt_floor/sqrt-route-receipt.json), [supplementary CLI source](../evidence/Roth.sqrt_lt_floor/candidates-cli-executed.lean.txt), [CLI receipt](../evidence/Roth.sqrt_lt_floor/candidates-cli-receipt.json), [explicit import authorization](../evidence/Roth.sqrt_lt_floor/root-supplementary-cli-scope-authorization.json), [power route source](../evidence/Roth.sqrt_lt_floor/power-route-executed.lean.txt), [power route receipt](../evidence/Roth.sqrt_lt_floor/power-route-receipt.json).

## Phase 7 — verdict and concrete next actions

**BORDERLINE-needs-human.** The strict inequality is more than the current upper-bound API, is sharp, and has three real callers. Neither the prior private-helper SKIP nor the coefficient-bound definition's NO decides it. On the other hand, shipping this conjunction would duplicate `Nat.floor_le` and commit to one packaging choice among a standalone strict bound, a sharp iff, and a broader root-witness interface. The quadratic kernel underneath the last option already composes from existing mathlib. The literature and experiments establish these real alternatives, but do not select the best public API grain. That is the remaining judgment; cost is not a reason for this verdict.

Concrete future upstream questions (not blockers for completion):

1. Should mathlib expose the strict real square-root/natural-floor estimate as a standalone lemma, obtaining the upper bound separately from `Nat.floor_le`?
2. Is a broader `rootBound` interface with `y² ≤ X` worth exposing, or should the real lemma use the existing three-block quadratic-floor argument directly?
3. Should the real API use the sharp equivalence `√X < floor₊ X ↔ 2 ≤ X`, rather than only its forward bound?

Until one option is selected, retain the helper/package in `Roth/MainLemma.lean` as project-local coefficient-bound API. If selecting the standalone estimate, update exactly the two `.1` callers directly and split the private Main caller into the strict estimate and `Nat.floor_le`; the completed full-module scratch replay proves those signatures survive. If selecting the broader root-witness interface, distinguish that API choice from the already composable quadratic kernel; do not advertise `floorSquare` as a missing primitive. No PR title, reviewer assignment or YES grouping is asserted for a BORDERLINE decision.

## Phase 8 — overview synthesis and verification

| Comparison | Same statement? | Same proof? | Action |
|---|---|---|---|
| target vs private sqrt helper | Only lower projection | Lower content shared | Helper supplies actual new content; no inherited prefilter verdict. |
| target vs `Nat.floor_le` | Upper projection only | Exactly upper argument | Split upper API if upstreaming. |
| target vs new floorSquare/rootBound | Related stronger algebraic representation | Shared quadratic gap | Quadratic kernel composes from three existing blocks; choose strict/root API grain, without claiming a missing primitive. |
| target vs natural-input floor-sqrt identity | Different inputs and conclusions | Requires a new bridge | Do not treat search hit as an exact replacement. |
| target vs Theta floor counting bounds | Different asymptotic inequalities | Shared unit-gap building blocks only | No moral duplication of the strict square-root estimate. |

Overview API audit: use the existing natural-floor interface, avoid a second coefficient-bound representation. Missing API candidates are a selected standalone strict/iff or root-witness API and the arbitrary-real bridge. The generic quadratic step itself is composable and is not a missing primitive. Junk audit: not dead (three actual consumers), not proven redundant by ≤3 mathlib calls; the conjunction is a local convenience pending API selection. Generalization: threshold is exact; generic quadratic witness is verified, meaningful and separately identified as newly proved. Production/pins unchanged; accepted native sources are warning-free, nonpartial where applicable, and use only `propext`, `Classical.choice`, `Quot.sound`. Rejected attempts are preserved and excluded from accepted evidence.

[Verification ledger](../evidence/Roth.sqrt_lt_floor/verification.json), [assessment](../evidence/Roth.sqrt_lt_floor/assessment.json), [portable validator](../evidence/Roth.sqrt_lt_floor/validate.py), [current copy manifest](../evidence/Roth.sqrt_lt_floor/copy-manifest.json).
