# Roth.Θ_le_card — BORDERLINE-needs-human

Declaration189, `Roth/Theta.lean:114`. Read-only full overview/mathlibable assessment. Retain the local theorem. The generic supremum upper-bound rule already exists, but it requires the substantive uniform polynomial-index bound; it does not prove that arithmetic premise. All phases and native checks below are complete; the remaining questions concern upstream API design, not proof verification.

## Phase 0 — Baseline

The shared `lake build` succeeded (2467 jobs). All17 source/pin hashes freshly match that build's input manifest. The complete985-line Theta module, Index module and the sole full caller were read. This is a theorem with no unproved body. Theta collects polynomial-index suprema and the estimates for Lemmas5–7.

Evidence: [baseline](../evidence/Roth.Θ_le_card/baseline-build.txt), [fresh hashes](../evidence/Roth.Θ_le_card/source-hashes.json), [input manifest](../evidence/Roth.Θ_le_card/input-manifest.json), [Theta source](../evidence/Roth.Θ_le_card/Theta.lean.txt), [Index source](../evidence/Roth.Θ_le_card/Index.lean.txt).

## Phase 1 — Mathematical statement and full native type

For a finite variable set σ, consider the indices of all nonzero integer polynomials of coordinate degrees at most r, with coefficients bounded in absolute value by B, evaluated at rational vectors h/q with coordinatewise coprime numerators and denominators. Their supremum Θ is at most the number of variables. The result holds for all real B and natural q,r, including zero weights/denominators and empty families under the real supremum default0 convention.

Full native type (no omitted typeclass or parameter):

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ},
  Roth.Θ B q r ≤ ↑(Fintype.card σ)
```

The proof chooses the nonnegative bound card σ in `Real.sSup_le`. For a represented index it uses the nonzero integer polynomial and coordinate degree bounds; injectivity of ℤ→ℝ transports both facts, then `Roth.index_le_card` supplies the bound. Height B and coprimality never enter this pointwise arithmetic proof. Inside index_le_card, a nonzero Taylor coefficient attaining the minimum has each coordinate at most r; summing the normalized coordinates gives card σ.

Evidence: [native type](../evidence/Roth.Θ_le_card/native-type.json), [original complete receipt](../evidence/Roth.Θ_le_card/theta-le-card189-original-receipt.json), [complete executed source](../evidence/Roth.Θ_le_card/theta-le-card189-original-executed.lean.txt).

## Phase 2 — Preliminary checks

BIG: explicitly listed in the module's main results (`0 ≤ Θ_m ≤ m`), though the supremum step is small and the mathematical ingredient is the earlier index bound. One-line definition-only test: n/a, theorem. This is not literal `rfl` glue and inherits no verdict automatically.

## Phase 3 — Exhaustive literature

Every named channel was actually attempted. Returned web bodies are not archived; metadata records exact requests, serialized response SHA256/bytes, status, clean title/URL locators and original summaries. Three general web queries are distinct; the arXiv retry includes the precise five-year lower date `after:2021-10-27`.

| Channel | Actual query / locator | Finding |
|---|---|---|
| General specific | `Roth theorem polynomial index theta supremum number variables degree upper bound` | Princeton *Eighth Lecture: The Proof of Roth’s Theorem* gives the normalized index setting. |
| General broader | `weighted order multivariate polynomial normalized multiplicity degree bound Taylor theorem` | Related multiplicity and weighted polynomial material; no independent exact Θ-card statement identified. |
| General aliases | `least upper bound supremum bounded set real numbers upper bound property` | Penn *Advanced Analysis* explains supremum as the least upper bound. |
| ChatGPT mathematics | n/a | `ask_chatgpt_math` unavailable; no simulated consultation. |
| Local clean.tex | `Theta|supremum|Taylor.*theorem|index across` | §5, lines665–667 explicitly states Θ≤m using a nonzero Taylor derivative with coordinate orders≤r. Source uses positive r and nonempty admissible family; Lean handles default cases. |
| nLab | `site:ncatlab.org/nlab supremum least upper bound` | *join*, Definition: the order-theoretic rule is the universal property of a supremum; arbitrary joins generalize binary joins. |
| distinct nCatLab namespace | `site:ncatlab.org/ncatlab supremum polynomial multiplicity`; retry `site:ncatlab.org/ncatlab supremum least upper bound` | Returned nLab links outside /ncatlab; no exact namespace hit. Not evidence of global absence. |
| Stacks | `site:stacks.math.columbia.edu polynomial order vanishing degree` | Definition02MD and lemma0C49 concern valuation/local-coordinate vanishing; not normalized degree-box index supremum. |
| MathOverflow | `site:mathoverflow.net Roth polynomial index multiplicity degree` | Question81732 discusses multiplicities and degree, a univariate analogy only. |
| Recent arXiv | `site:arxiv.org Roth Diophantine approximation index polynomial after:2021-10-27` | Related2209.09182 and2509.05300; other query finds2022/2023/2026 additive-combinatorics Roth results. No exact Θ-card law located. Older2010/2017 hits were excluded from the recent accounting. |

Primary mathematical anchor is the project's [local excerpt](../evidence/Roth.Θ_le_card/clean-excerpt.tex.txt), supported by the [Princeton lecture locator](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf) for the index terminology. The abstract upper-bound rule is illustrated by [Penn's analysis notes](https://www2.math.upenn.edu/~gressman/analysis/01-completeness.html) and [nLab join](https://ncatlab.org/nlab/show/join). Direct Princeton full-text access timed out (400), Penn returned403 and nLab's XHTML returned unsupported-content400; only returned search excerpts were available through this tool. These limits are recorded and do not turn related sources into exact hits.

Evidence: [web a](../evidence/Roth.Θ_le_card/web-a-metadata.json), [web b](../evidence/Roth.Θ_le_card/web-b-metadata.json), [web c/direct attempts](../evidence/Roth.Θ_le_card/web-c-metadata.json), [web d/date and namespace retry](../evidence/Roth.Θ_le_card/web-d-metadata.json), [individual Stacks](../evidence/Roth.Θ_le_card/web-e-metadata.json), [individual MO](../evidence/Roth.Θ_le_card/web-f-metadata.json), [local search](../evidence/Roth.Θ_le_card/local-literature.json).

Literature summary: two layers are standard—normalized polynomial index controlled by coordinate degrees, and passing a pointwise upper bound to a supremum. There is no new supremum principle here. The family has a Roth-specific height/rationality restriction which the upper bound does not need. Changing that family is an expanded representation, not merely removing a visible hypothesis from the current Θ interface.

## Phase 4a — Parameters and generality

| Parameter / hidden condition | Role and weakening analysis |
|---|---|
| σ : Type u | Already arbitrary universe; finite variable set, not only Fin m. |
| Fintype σ | Used by parent index weights and card. Removing it changes the fixed parent interface; no unsupported weakening claimed. Nonempty σ is not required. |
| B : ℝ | Unrestricted, including B<1 or negative. Height condition is ignored in proof but is part of RSet. Removing B from current statement is ill-typed because Θ still depends on B. |
| q : σ→ℕ | Unrestricted, including0/1. Denominator arithmetic and coprimality are irrelevant to this bound. Replacing rational point family by arbitrary real points is verified below. |
| r : σ→ℕ | Unrestricted, no positivity assumptions. Natural division by0 contributes0 in project weight; real default conventions matter. |
| DecidableEq σ | Already omitted from the native signature; local classical proof does not add a parameter. |
| Polynomial nonzero (hidden in RSet) | Used by old index_le_card call. Verified droppable for the expanded real family because index0=0, not under the canonical∞ zero-order convention. |
| Coordinate degree≤r (hidden) | Substantive arithmetic premise. Removing it would permit X² in one variable at0 with r=1 and index2>card1. This explanatory example is not presented as a new executed counterexample. |
| Integer coefficients / coefficient bounds / coprimality | All dropped in the verified expanded family with the degree premise retained. |

## Phase 4b — Verified generality result

Within the fixed Θ representation no visible assumption remains to remove. The independently compiled `expanded_family` is a strict expansion of the admissible data, not a one-edit weakening of this theorem:

```lean
theorem expanded_family (S : Set (MvPolynomial σ ℝ)) (T : Set (σ → ℝ)) {r : σ → ℕ}
    (hd : ∀ P ∈ S, ∀ j, MvPolynomial.degreeOf j P ≤ r j) :
    sSup (Set.image2 (fun P α ↦ Roth.index P α r) S T) ≤ Fintype.card σ
```

It allows zero polynomials and empty S,T, arbitrary real coefficients and arbitrary real centers. `noNonzero` explicitly separates P=0 (using `map_zero`, empty support, `Real.sInf_empty`) from the nonzero case (`Roth.index_le_card`). This is a complete new project-context proof; its polynomial-index ingredient is not an existing mathlib replacement. Cost does not determine the verdict.

Evidence: [accepted callers/generality receipt](../evidence/Roth.Θ_le_card/theta-le-card189-callers-generality-receipt.json), [unchanged exact executed source](../evidence/Roth.Θ_le_card/theta-le-card189-callers-generality-executed.lean.txt). The first attempt mistakenly used `taylor_zero`, a translation-at-zero lemma, in the P=0 branch; its [rejected receipt](../evidence/Roth.Θ_le_card/theta-le-card189-callers-generality-rejected-receipt.json) includes an error and recovered sorryAx and is excluded from accepted proof evidence. The corrected complete execution is clean.

## Phase 4c — Nine modern-idiom checks

| # | Question | Answer and concrete consequence |
|---|---|---|
| 1 | Typeclasses instead of hypotheses? | No new structure. Fintype is already a class; making height/degree predicates global instances would obstruct multiple bounds on the same polynomial. |
| 2 | Sequences to filters? | No limits or sequences. |
| 3 | Universal property? | Yes: use `Real.sSup_le`/`csSup_le`; already used. Replacing Θ with sSup exposes existing order API. |
| 4 | Bundled substructure? | No: nonzero, coefficient-height-bounded family is not a subring/submodule. Arbitrary Set is appropriate for image2. |
| 5 | Weaker algebraic hierarchy? | Parent index is real-valued over real polynomials. Arbitrary real coefficient family compiled; arbitrary ring/semiring index would require parent redesign, no verified class weakening claimed. |
| 6 | Higher categories? | No categorical content beyond poset universal-property analogy; no useful higher-categorical restatement. |
| 7 | General ordered target? | Abstract supremum law exists for conditional complete lattices with nonempty set (`csSup_le`). Real.sSup_le handles empty sets using0≤c. Altering target changes numeric/default interface. |
| 8 | Concrete-via-abstract diagnostic? | Fires: proof body has zero Θ occurrences and zero B occurrences; height/coprimality are discarded after destructuring. The abstraction separates arithmetic degree-bound proof from the existing supremum transport. Expanded S,T form composes with Set.image2 and arbitrary evaluation families. |
| 9 | False-generalization guard? | Replacing arithmetic input with a supplied arbitrary bound generalizes only the structural layer and must not erase the original arithmetic content. No arbitrary bounded real set has supremum≤card. Zero-inclusive family is valid only under the project's default0 convention. |

Modern-idiom result: the structural order principle is already present; a reusable coordinate-degree envelope is the substantive prospective contribution. Its parent index/Taylor API and audience need design review. This does not establish a new missing supremum theorem.

## Phase 4.5 — Infrastructure risk

n/a—this is a theorem, not a definition/class/instance. All six infrastructure rows (diamonds, definitional-equality abuse, reducibility, competing coercions, instance search, universe rigidity) are n/a: no new data or instance/coercion path is introduced. The inherited real-default0 convention is a mathematical generality issue, documented above.

## Phase 4.6 — Five proof-strategy checks

| # | Strategy question | Result |
|---|---|---|
| 1 | Topology ε–δ versus filters | No topology. |
| 2 | Algebra element proof versus inclusions | Pointwise degree arithmetic needed; Set.image2 quantifier transport is verified for the outer family. A submodule inclusion cannot encode nonzero height-bounded data. |
| 3 | Analysis sequences versus nets | No convergence. |
| 4 | Explicit construction versus universal property | Supremum universal property is already the optimal outer step. No extra existence proof needed because Real.sSup_le handles empty family. |
| 5 | Helpers mathlib should have | Coordinate-degree/Taylor index bound, if upstream index representation is accepted; generic supremum transport is not missing. Factor the identical pointwise block shared with indexSet_bddAbove locally. |

Strategy: MATHLIB-IDIOMATIC for supremum transport; REFACTOR-RECOMMENDED locally for repeated arithmetic premise. Any proposed upstream envelope should be evaluated with index_le_card/Taylor API, not added as an isolated Roth-named wrapper.

## Phase 5 — Five actual mathlib methods on three forms

| Form | Finder | Loogle | LeanSearch | rg | Local name search |
|---|---|---|---|---|---|
| Current Θ/index/card | Query for Roth multivariate index supremum bound returned unrelated Chevalley complexity | `"index_le_card"` returned unrelated subgroup index results | normalized polynomial order supremum query returned polynomial degree/Schwartz–Zippel near matches | Current names: no exact mathlib target | Finds project index_le_card only; index unavailable |
| Literature degree/weighted order | Taylor/multiplicity/degree query returned analytic Taylor and univariate near matches | `"weightedOrder"` yields weightedOrder and its witness bound | weighted order by coordinate degrees yields `MvPowerSeries.weightedOrder_le` | Witness and degree lemmas found | weightedOrder declarations found; index unavailable |
| Abstract supremum upper bound | `Real.sSup_le` hit | `"sSup_le"` includes complete-lattice variants | Exact `Real.sSup_le` hit | Pinned Real.sSup_le/csSup_le and image2 transport | Real.sSup_le found; index unavailable |

Raw complete responses: [formal search](../evidence/Roth.Θ_le_card/formal-search.json). All12 formal calls succeeded; [rg current](../evidence/Roth.Θ_le_card/rg-current.json), [rg literature](../evidence/Roth.Θ_le_card/rg-literature.json), [rg abstract](../evidence/Roth.Θ_le_card/rg-abstract.json) complete the15 actual method/form cells. The unavailable local symbol index is not a proof of absence; external indices are not necessarily the pinned revision.

Pinned positive signatures independently checked in isolated mathlib context:

```lean
Real.sSup_le {s : Set ℝ} {a : ℝ}
  (hs : ∀ x ∈ s, x ≤ a) (ha : 0 ≤ a) : sSup s ≤ a
csSup_le {α : Type u} [ConditionallyCompleteLattice α] {s : Set α} {a : α}
  (h₁ : s.Nonempty) (h₂ : ∀ b ∈ s, b ≤ a) : sSup s ≤ a
Set.forall_mem_image2 :
  (∀ z ∈ Set.image2 f s t, p z) ↔ ∀ x ∈ s, ∀ y ∈ t, p (f x y)
```

`Real.sSup_le`: Mathlib/Algebra/Order/Archimedean/Real/Basic.lean:222. `csSup_le`: Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:201. `Set.forall_mem_image2`: Mathlib/Data/Set/NAry.lean:54. Near-match `MvPowerSeries.weightedOrder_le` controls order by one nonzero coefficient's weight; it does not supply the degree-box normalized bound or the real index bridge. `MvPolynomial.totalDegree_le_degrees_card` concerns total degree, not this normalized infimum. Pinned source copies/hashes are in [mathlib inputs](../evidence/Roth.Θ_le_card/mathlib-inputs.json).

Evidence: [isolated exact source](../evidence/Roth.Θ_le_card/theta-le-card189-isolated-executed.lean.txt), [isolated receipt](../evidence/Roth.Θ_le_card/theta-le-card189-isolated-receipt.json). No Roth import; `#check_failure Roth.Θ_le_card` succeeds. The abstract family law compiles from Real.sSup_le and Set.forall_mem_image2 once the pointwise premise is supplied.

## Phase 5.5 — Three statement-shape checks

1. Normal form: `sSup (indexSet B q r) ≤ card` is the canonical order layer; the old Θ form is definitionally equal, verified by `exact_sup := rfl`. An alternative family form uses `Set.image2` and composes with its quantifier API. No orthogonal equivalence web is needed.
2. Syntactic generality: direct Θ≤card is easiest at the sole caller (`simpa` specializes card Fin(n+1)). A supplied-bound generic lemma would force the caller to reconstruct the arithmetic premise. Expanded S,T form is useful for other families but changes the interface.
3. Superfluous parameters: no visible hypothesis/typeclass to drop—σ/Fintype are in the parent and cardinality, B/q/r are in Θ. No DecidableEq parameter remains. Hidden height/coprime assumptions are avoidable only through the separately verified expanded family.

Overall: keep local statement; choose upstream parent/API before shipping. No unsupported mechanical weakening claim.

## Phase 6.0 — Callers and inline audit

Fresh `rg --no-ignore` and `git grep` agree on all3 source occurrences: module-doc line33, declaration114 and one application939. One caller, zero external-file uses. Canonical kernel-value enumeration independently scanned all293 ordered unique declarations (all present, all with values): one direct body consumer `_private.Roth.Theta.0.Roth.theta_lt_of_large_delta_aux`, no direct type consumers. This is direct consumption, not transitive/simp closure.

| Caller | Exact use | Role/refactor experiment |
|---|---|---|
| Roth/Theta.lean:939, private helper933–958 | `simpa using Θ_le_card (r := r) q` | Initial bound in large-δ branch of Lemma7. Entire caller replay succeeds with `ThetaLeCard189.replacement`, then the original numeric comparison is unchanged. |

Inline audit finds `indexSet_bddAbove` repeats the same arithmetic premise proof. It concludes existence of an upper bound, not Θ≤card. No separate bypassing re-derivation of the complete target was found. One use is an API-size signal, not proof of mathlib composability or dead code.

Evidence: [rg](../evidence/Roth.Θ_le_card/callers-rg.json), [git grep](../evidence/Roth.Θ_le_card/callers-git.json), [caller record](../evidence/Roth.Θ_le_card/callers.json), [inline search](../evidence/Roth.Θ_le_card/inline.json), [canonical exact audit source](../evidence/Roth.Θ_le_card/theta-le-card189-audit-executed.lean.txt), [complete caller replay](../evidence/Roth.Θ_le_card/theta-le-card189-callers-generality-executed.lean.txt).

## Phase 6 — Actual compositions and parent re-aim

Independent parent bridge: `Roth.Θ B q r = SupSet.sSup (Roth.indexSet B q r) := rfl`. Hence re-aiming at sSup does expose existing `Real.sSup_le`; this is an exact hit for the structural layer. Its premise `∀ x∈indexSet, x≤card` is still the substantive degree-normalized polynomial-index theorem, not a provided assumption of Θ_le_card. The re-aim rule cannot manufacture that bound. The failure to classify the whole result as NO is due to this arithmetic premise, not normalization cost.

| Attempt | Actual result |
|---|---|
| `Real.sSup_le hs (Nat.cast_nonneg _)` | Compiles with supplied hs. Exact existing structural law; does not prove hs. |
| Pointwise proof + Real.sSup_le | Complete original-form `replacement` compiles without calling Θ_le_card. It reuses project index_le_card plus nonzero/degree transport through map. These are not ≤3 existing mathlib calls. |
| `Real.sSup_le (Roth.indexSet_bddAbove B q) ...` | Wrapped fail_if_success verifies the existential boundedness fact does not have the needed fixed pointwise-bound type. Then independent replacement closes the proof. |
| Arbitrary S,T with degree bounds | Complete expanded_family compiles; uses project index_le_card and the zero branch. This new helper is not an existing-call replacement. |
| Sole caller replay | Full private helper compiles using replacement; no target call remains in new proof region. |

Isolated guard proofs show why stronger structural claims fail: an empty real set with bound−1 requires the nonnegative-bound assumption; bounded singleton{2} disproves a universal `BddAbove s → sSup s≤1` law. These guards concern abstract sets, not counterexamples to the valid polynomial theorem. No strict three-mathlib-call term for the complete arithmetic target was verified. This is not a global absence claim.

Moral-duplication comparison:

| Related declaration | Shared part | Distinct mathematical content |
|---|---|---|
| Θ (parent, accepted NO-mathlib-has-it) | Literally sSup | No bound encoded by the parent definition itself. |
| indexSet (accepted NO-mathlib-has-it) | Family image structure | Image membership does not bound a polynomial's normalized index. |
| index_le_card (accepted BORDERLINE) | Full coordinate-degree arithmetic estimate | One polynomial/center rather than an admissible-family supremum. |
| indexSet_bddAbove (accepted BORDERLINE) | Identical pointwise arithmetic proof | Existential upper bound rather than known Θ≤card. |
| Θ_nonneg (accepted NO-mathlib-has-it) | Generic real supremum layer | Pointwise nonnegativity is structurally inherent in its index weight construction; fixed card upper bound needs degree constraints. |

Evidence: [project exact source](../evidence/Roth.Θ_le_card/theta-le-card189-project-executed.lean.txt), [project receipt](../evidence/Roth.Θ_le_card/theta-le-card189-project-receipt.json), [verification ledger](../evidence/Roth.Θ_le_card/verification.json). Previous verdicts were checked from progress and detailed reports; none is inherited as proof.

## Phase 7 — Verdict and actionable disposition

**BORDERLINE-needs-human.** The named Roth family bound belongs locally while the normalized index/Taylor degree-envelope API is being designed. Generic supremum and image transport are present. The full upper bound uses the substantive project theorem index_le_card; a≤3 existing-mathlib-call proof was not verified. The expanded-family proof establishes real generality but threads through parent interfaces, so it is not an automatic YES-but-generalise-first for a removable visible hypothesis. Neither search failure nor implementation cost determines this verdict.

Concrete future upstream API questions (no verification gap or immediate user response required):

1. Should a normalized Taylor-order envelope under coordinate degree bounds be a named mathlib theorem after the index parent is restated, or should clients apply a generic coefficient-weight witness bound?
2. If that envelope is accepted, should the family-supremum corollary remain local and be derived using Real.sSup_le, or join a reusable arbitrary-polynomial-family API?
3. Should a zero-inclusive envelope retain real-default0 or use the canonical∞ weighted-order representation with explicit nonzero polynomials?
4. Should the repeated fixed pointwise bound in Θ_le_card/indexSet_bddAbove be factored locally into membership in the upperBounds set, retaining both useful conclusions?

Action now: retain `Roth/Theta.lean:114` and its sole caller unchanged. Optional later local cleanup can factor the pointwise arithmetic helper and replace each duplicated block; the validated caller replay gives a concrete replacement path. Upstream location/title/reviewer/YES grouping are n/a for this BORDERLINE verdict. If pursued later, coordinate the envelope with the accepted Taylor/index contribution plan, rather than introducing a new foundational order lemma. The appropriate alternative destination today is this project's Theta module.

## Phase 8 — Completion and verification limits

All four accepted native sets—original type/kernel audit, project replacement/negative closure, isolated mathlib laws/guards, full caller plus expanded generality—returned complete success, no warning/error/sorry diagnostics, and only standard axioms propext/Classical.choice/Quot.sound. Disk receipts have partial=false; the raw isolated format uses diagnostics/success and has no partial field. Required messages are scoped to the new region while all-file error/axiom scans are retained. Original kernel printer body is complete without elision. One rejected initial generality attempt is separately retained and never accepted. Canonical audit array is generated from and checked against exact tracked order293, including private names.

All17 hashes, source excerpts, raw formal responses, exact unchanged executed sources and receipts are retained. Web metadata preserves requests/digests/clean locators only, with honest direct-access failures. No production Lean/pin/Git/progress changes were made. Root acceptance remains pending. The [portable read-only validator](../evidence/Roth.Θ_le_card/validate.py) checks current manifests, source pins, canonical order, native receipts/axioms, phase/search evidence, links and credentials in scratch and integrated layouts.
