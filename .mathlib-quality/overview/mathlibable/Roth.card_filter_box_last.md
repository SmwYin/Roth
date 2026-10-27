# Roth.card_filter_box_last — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** Finite fibre counting is already `Finset.card_eq_sum_card_fiberwise`; the original spelling also needs a genuine identification of each Finsupp fibre with a smaller box. That identification is the project's private `card_filter_box_fiber_aux`, not existing mathlib. The arbitrary filtered product form closes by `simp only [Finset.card_filter, Finset.sum_product]`, which is explicitly a Phase6b borderline composition. The remaining API question is whether to package general tuple sections and their representation bridge upstream. No proof-cost judgment is used.

## Phase 0 — baseline

Declaration127 resolves at Roth/Lattice.lean:131, a public theorem without sorry. The module proves the lattice counting estimate used in Roth's argument. All17 source/pin hashes freshly match the successful2467-job baseline. Production and Git remain unchanged. [Fresh hashes](../evidence/Roth.card_filter_box_last/source-hashes.json), [input manifest](../evidence/Roth.card_filter_box_last/input-manifest.json), [build](../evidence/Roth.card_filter_box_last/baseline-build.txt), [whole declaring module](../evidence/Roth.card_filter_box_last/Roth-Lattice.lean.txt), [parent module](../evidence/Roth.card_filter_box_last/Roth-Box.lean.txt).

## Phase 1 — comprehension

Given bounds r on m+1 natural coordinates and any predicate p on the associated finitely supported vectors, count the vectors satisfying p by their last coordinate. For each value i between0 and the last bound, the corresponding fibre is the m-coordinate box with p evaluated after extending the vector by i. Summing these fibre cardinalities counts each vector exactly once.

Full native type:

```lean
∀ {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop)
  [inst : DecidablePred p],
  (Finset.filter p (Roth.box r)).card =
    ∑ i ∈ Finset.range (r (Fin.last m) + 1),
      {d ∈ Roth.box (r ∘ Fin.castSucc) |
        p (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i)}.card
```

m determines the split; r supplies arbitrary natural bounds; p is entirely arbitrary; its decision instance makes the filters executable. No positivity, nonempty, real scalar or polynomial assumptions occur. The original proof first applies fibre counting with the last-coordinate map, proves its range lies in the bounded range using mem_box, then rewrites each summand with the private fibre bijection. The private bijection checks bounds, injectivity by restriction and surjectivity by reconstruction. [Native evidence ledger](../evidence/Roth.card_filter_box_last/verification.json).

## Phase 2 — preliminary checks

**SMALL:** an elementary helper, neither a new structure nor a named main result. One-line definition-only test: **n/a — theorem**. Shortness of the public proof does not erase its substantive private bridge.

## Phase 3 — exhaustive literature

Every named channel was attempted afresh, including three distinct general-web queries. Web receipts contain exact requests, returned-response SHA256/bytes/status and title/URL locators, without article/search bodies. [Web specific/standard/alias requests](../evidence/Roth.card_filter_box_last/web-0.json), [nLab/nCatLab/Stacks requests](../evidence/Roth.card_filter_box_last/web-3.json), [MO/arXiv requests](../evidence/Roth.card_filter_box_last/web-6.json), [direct accesses and dated retry](../evidence/Roth.card_filter_box_last/web-open.json), [channel ledger](../evidence/Roth.card_filter_box_last/literature-summary.json).

| Channel | Actual query/access and result |
|---|---|
| General specific | `bounded multi-index lattice box counting by last coordinate fibers Roth theorem`; no independently exact Roth-box law established. |
| General standard | `finite set cardinality sum cardinalities fibers counting principle`; finite partitions and fibre counting are the standard underlying formulation. |
| General alias | `rule of sum partition counting Cartesian product sections`; [Cornell Lecture16](https://www.cs.cornell.edu/courses/cs2800/2017fa/lectures/lec16-combinatorics.html), Sum rule lines12–23 and generalized product rule49–51, explains disjoint subdivision. |
| ChatGPT math MCP | n/a: ask_chatgpt_math unavailable. Intended question: standard form/generality and historical evolution of counting a filtered product by coordinate fibres; no fabricated opinion. |
| Local clean.tex | §6 Lemma8 proof fixes the last coordinate and sums smaller-box counts; implementation note1132–1137 explicitly calls for last-coordinate fibres. [Exact local excerpt](../evidence/Roth.card_filter_box_last/local-reference.txt). |
| nLab | `site:ncatlab.org/nlab fiber finite set cardinality`; [cardinal number](https://ncatlab.org/nlab/show/cardinal%2Bnumber) search locator describes addition by indexed disjoint union. Direct fetch failed400 unsupported XHTML. |
| nCatLab | `site:ncatlab.org/ncatlab finite sets coproduct fibers`; results pointed to nLab FinSet/coproduct material. Explicit nCatLab finite-set namespace URL was inaccessible. Categorical language does not provide the missing concrete bridge. |
| Stacks | `site:stacks.math.columbia.edu sets fibre disjoint union`; direct [Tag000D §3.6](https://stacks.math.columbia.edu/tag/000D), lines17–20, defines cardinality and disjoint-union addition. General background, not this exact statement. |
| MathOverflow | `site:mathoverflow.net counting cardinality fibers finite sets`; [Aggregations internal to a syntactic category](https://mathoverflow.net/questions/348794/aggregations-e-g-cardinality-indexed-sums-products-internal-to-a-syntactic), lines34–52, treats finite-fibre cardinality more abstractly. Its additional internal-category questions are outside the present finite-set equality. |
| Recent arXiv | Initial query included2022–2026 but returned older2012/2013 Cartesian-code papers; those are explicitly rejected as recent evidence. Retry `site:arxiv.org/abs/ "fiber" "counting" "finite sets" after:2021-10-27 before:2026-10-28` returned no results. Five-year search attempted; no recent exact paper located, no absence inference. |

Standard concept: the sum rule for a finite partition into fibres, with bijections identifying the sections of a Cartesian product. Bounds in ℕ and Finsupp representation are project choices. Sources vary between finite sets, indexed disjoint unions and categorical families; no historical change requiring a Roth-specific API was established. The local paper's analytic positivity assumptions are not counting hypotheses.

## Phase 4a–b — parameter/generality audit

| Parameter/restriction | Actual mathematical need and verified alternatives |
|---|---|
| m : ℕ, Fin(m+1) | Required by this literal last/castSucc interface. Generic finite-set fibre counting removes the coordinate type entirely; dependent tuple sections permit arbitrary coordinate types. Both compiled. |
| r : Fin(m+1) → ℕ | Essential bounds in current box interface; zero bounds are allowed. Arbitrary dependent finite coordinate sets are the supported expanded representation, not a literal r-binder deletion. |
| p | Essential and already arbitrary; predicates depending on the last coordinate must remain supported. |
| DecidablePred p | Required by literal filters; a statement-local classical predicate decision removes the public binder in the verified variant. A global classical decision instance initially changed the Fin decision instance and failed; this rejected attempt is retained. |
| ℕ coordinates | Fixed by the parent's exponent representation. Generic filtered products/tuples have arbitrary coordinate types, with no Zero/Add/order classes at all. This changes representation, not a mechanical weakening of Finsupp.mapDomain/single. |
| Finiteness | Supplied by finite boxes/finite coordinate sets. Generic fibre law needs only finite s,t and MapsTo; global finite α/β is unnecessary. Unrestricted infinite boxes are not finite-cardinality domains. |
| Positivity/nonempty | Absent already. Do not add hypotheses used only by the later analytic estimate; m=0 and r=0 are legitimate. |

Current form is **STRICTLY NARROWER** than standard finite fibre counting, but the geometric identification of smaller Finsupp boxes is additional content. The accepted parent Roth.box verdict is **NO-composable-from-mathlib**. Therefore the special ModeB re-aim-hit gate does not apply automatically. Re-aiming was independently checked anyway: the existing snoc cardinal law only permits predicates on init, whereas the present p depends on the entire vector.

## Phase 4c — nine modern-idiom rows

| # | Applies? | Analysis and concrete consequence |
|---|---|---|
| 1 typeclasses | limited | Classical predicate decidability can be hidden; no mathematical hypothesis should become a new instance. |
| 2 filters/nets/topology | no | Finite combinatorics, no convergence or topology. |
| 3 universal characterization | no new class | Fibres and Cartesian products already have standard membership APIs. A new universal-property class adds no use here. |
| 4 bundled substructure | no | A filtered bounded box need not be closed under addition. A submonoid would change the object. |
| 5 algebraic hierarchy | yes via representation | Arbitrary finite coordinate sets remove natural-additive structure; Finset product/map/card APIs then apply. This is not a weakening of the fixed Finsupp syntax. |
| 6 higher categories | no | Ordinary finite-set cardinality suffices. Groupoid cardinality changes the invariant. |
| 7 concrete indices/order | yes | Generic finite α/β fibre maps and arbitrary dependent Fin-indexed coordinate types compile; usable for arbitrary finite sections rather than just natural bounds. |
| 8 concrete-via-abstract | yes | No bare box construction occurs in the public proof body; mem_box normalizes range containment, then the private helper supplies geometry. [Explicit diagnostic](../evidence/Roth.card_filter_box_last/q8-diagnostic.json). Abstract fibre counting already exists; the bridge must remain visible. |
| 9 false-generalization guard | pass | Preserve arbitrary full-vector p, bijective section identification, finite coordinate choices and exact disjoint counting. Reject restricted init-only predicates, noninjective transports, unconstrained infinite boxes and groupoid weights as substitutes. A native singleton-product/False-predicate counterexample guards against replacing filtered cardinality by unfiltered product cardinality. |

Modern idiom: generic fibre cardinality where fibres themselves are desired; generic dependent tuple sections where recursive dimension reduction is desired. The latter composes with Fin.init/snoc and arbitrary piFinset families. The concrete downstream improvement is that finite-field/alphabet tuples can use the same sections theorem without manufacturing natural exponents. The verified generic product identity is a simp composition; packaging this and the tuple bridge is an API-design question, not an assumed contribution.

## Phase 4.5 — six infrastructure risks

**n/a — theorem.** Typeclass diamond, reducibility leak, noncanonical unfolding, instance-priority collision, universe and coercion rows are all n/a: no data definition, instance, coercion or reduction rule is introduced. Decision-instance representation sensitivity was genuinely tested above rather than attributed to a new theorem instance.

## Phase 4.6 — five proof-strategy rows

| Row | Applies? | Finding |
|---|---|---|
| εδ versus filters | no | No topology. |
| Elements versus substructures | no | Arbitrary filtered finite subsets have no closure structure. |
| Sequences versus nets | no | No limiting argument. |
| Construction versus universal property | limited | Use an existing finite product equivalence; no categorical class needed. |
| Missing helper API | possible design gap | Arbitrary dependent tuple sections is proved with a genuine bijection plus generic filtered-product counting; existing snoc cardinal law only treats init predicates. Whether this warrants a named upstream theorem remains the concrete question. |

Strategy: **MATHLIB-IDIOMATIC** for the existing Finsupp interface: standard finite fibre counting followed by explicit fibre identification. For an upstream proposal, **REFACTOR-RECOMMENDED** to general tuple/product sections. Cost is not a verdict factor.

## Phase 5 — five actual methods on three forms

Forms: bounded natural Finsupp box with arbitrary predicate; filtered Cartesian-product sections; generic finite-set fibre count. Each formal receipt preserves exact request and complete response. Local index is unavailable even where source fallback returns names; scratch replay names are not treated as mathlib. External revisions may differ; decisive signatures/proofs are natively checked against this pin.

| Method | Current form | Standard product sections | Abstract fibre count |
|---|---|---|---|
| Finder | Finsupp.card_Iic near-match counts unfiltered box | card_snocEquiv_filter_piFinset, restricted predicate; filter_product_card concerns predicate agreement | card_eq_sum_card_fiberwise exact abstract count |
| Loogle | Finsupp support/card facts, not exact | no hits for card/filter/product query | card_eq_sum_card_fiberwise exact |
| LeanSearch | Finsupp/Nat.count near-matches | fixed-coordinate product-card lemmas, no arbitrary p hit | card_eq_sum_card_fiberwise, sum_card_fiberwise_eq_card_filter |
| rg pinned source | source implementation and helper | snoc membership/map/card laws | generic fibre and filtered-sum laws |
| Local name | snocEquiv | card_filter; local Roth/replay names rejected as library hits | card_eq_sum_card_fiberwise |

[Formal-search index](../evidence/Roth.card_filter_box_last/formal-search-index.json), [rg current](../evidence/Roth.card_filter_box_last/rg-current.json), [rg standard](../evidence/Roth.card_filter_box_last/rg-standard.json), [rg abstract](../evidence/Roth.card_filter_box_last/rg-abstract.json), [untruncated full-name search](../evidence/Roth.card_filter_box_last/full-name-source-search.json). No qualified Roth target occurs in mathlib source; this alone proves no absence. [Pinned tuple source](../evidence/Roth.card_filter_box_last/Tuple-Finset-source.lean.txt), [pinned fibre source](../evidence/Roth.card_filter_box_last/Finset-Basic-source.lean.txt).

Positive building blocks include Finset.card_eq_sum_card_fiberwise, card_filter, sum_product, card_bij, sum_congr, card_map, filter_map and Fin.snocEquiv. Existing Finset.card_snocEquiv_filter_piFinset is not an analogous arbitrary-p law: its conclusion multiplies by the last-coordinate cardinality because its predicate ignores that coordinate. A p testing whether the last coordinate is0 need not have equal-size sections. The separate native false-generalization guard proves a singleton product filtered by False has cardinality0 rather than the unfiltered product cardinality1; it does not challenge the correctly formulated sections theorem.

## Phase 5.5 — three statement-shape checks

1. **Normal form:** original filtered-box count equals sum of smaller filtered-box counts; generic equivalent is cardinality equals sum of actual fibres. Canonical fibre counting is already mathlib. The recursive smaller-domain RHS serves the induction caller; equality orientation is useful for rewriting. A generic tuple-section statement should similarly put the section sum on RHS.
2. **Syntactic generality:** arbitrary dependent tuple sets, arbitrary binary filtered product, and arbitrary finite s/t/f with MapsTo were actually compiled. The existing init-only product cardinality is rejected as too narrow for the caller. Classical statement-local decision hides a computational binder while preserving parent decision choices.
3. **Superfluous arguments:** m,r,p determine the literal expression and cannot simply disappear; no proposition hypotheses can be dropped. DecidablePred p can be hidden classically as tested. General α/β finite types need no global Fintype instance in the generic fibre/product forms.

Overall **RESTATE-BEFORE-SHIP** if upstreaming: general finite product or dependent tuple sections. Keep the original local orientation for the lattice induction until a coordinated representation change is chosen.

## Phase 6.0 — all explicit callers and inline audit

Exactly **1 explicit source occurrence** outside the declaration head: Roth/Lattice.lean:175, private `card_filter_weight_le_succ_aux`. Zero external-to-file occurrences. It rewrites the filtered-box cardinality, casts the finite sum to ℝ, then changes the weight predicate in each smaller box before invoking induction. This is useful live code, not junk. [Caller search](../evidence/Roth.card_filter_box_last/callers.json), [structured caller](../evidence/Roth.card_filter_box_last/explicit-callers.json), [inline audit](../evidence/Roth.card_filter_box_last/inline-audit.json). No independent inline derivation of the same last-coordinate formula was found. Source references are not kernel/simp closure; canonical audit independently found the same single direct value consumer. The target has no simp attribute.

The actual original private helper was accessed using a term elaborator returning its existing constant via Lean.mkPrivateNameCore, with no new axiom. The target proof was replayed with that actual helper, and the full original sole consumer was replayed using the fresh theorem and actual other private helper. Whole-module replay additionally recompiles all private geometric and analytic dependencies. These are actual caller validations, not production edits or claims about a rebuilt migration.

Concrete local refactor alternatives: retain the public theorem as the induction interface; or make it private since its sole explicit consumer is in the same file. To remove it, inline its original fibre-counting proof immediately before line175, keeping the private fibre identification; this is a local proof refactor, **not** a three-existing-mathlib-call substitution. If adopting tuple sections, first transport both box domains and the extension map, then rewrite the caller using that law; preserve the weight-predicate conversion and Nat.cast_sum step. No deletion is authorized by this assessment.

## Phase 6 — actual composition experiments and Phase6b

**Attempt1:** `Finset.card_eq_sum_card_fiberwise` yields a sum of actual last-coordinate fibres after proving MapsTo. This compiles in completely arbitrary α/β, without global finiteness. It does not identify a fibre with a smaller box.

**Attempt2:** original proof uses that theorem, mem_box/range normalization, sum_congr and the project's private fibre-bijection theorem. Native replay succeeds, including the real caller. The private helper is new project proof and cannot be counted among existing mathlib calls. No original-form ≤3-existing-call term was established.

**Attempt3:** for arbitrary finite s,t and full predicate p:

```lean
((s ×ˢ t).filter p).card = ∑ a ∈ s, (t.filter fun b ↦ p (a,b)).card
```

The proof `by classical; simp only [Finset.card_filter, Finset.sum_product]` closes. This is exactly the **Phase6b** trivial-simp case, hence BORDERLINE rather than automatic NO-composable. The generic dependent tuple sections experiment supplies an actual bijection to this filtered product; it is a genuine bridge proof, not a definitional equality or existing theorem. This is an independently verified alternate representation: no complete specialization through equivFunOnFinite to the original Roth spelling is claimed.

**Attempt4:** restricted `card_snocEquiv_filter_piFinset` is independently signature-checked and rejected for arbitrary full-vector p; ordinary Finsupp interval cardinality also ignores p. A parent's NO verdict cannot replace these checks. No search timeout, proof length or cost is used as an absence argument.

## Phases 7–8 — actionable disposition

**BORDERLINE-needs-human**, with these concrete future upstream API questions:

1. Should mathlib name the arbitrary dependent tuple sections identity, alongside `Finset.card_snocEquiv_filter_piFinset`, rather than leave its bijection and filtered-product sum inline?
2. Should the simpler binary filtered-product cardinality identity receive a named theorem despite closing by the two existing simp rewrites?
3. Should Roth retain the Finsupp wrapper locally, or migrate this induction boundary to piFinset/Fin.snoc and keep only a project-local weight-transport bridge?

These are design questions for a future contribution, not missing verification and not a request to pause the overview. No YES proposal, PR/reviewer selection or grouping is asserted. If retained unchanged, its appropriate destination is project-local Roth/Lattice.lean; consider private visibility based on the sole same-file consumer. The assessment and all required checks are complete; unresolved verification items are empty. [Assessment](../evidence/Roth.card_filter_box_last/assessment.json), [verification](../evidence/Roth.card_filter_box_last/verification.json), [portable validator](../evidence/Roth.card_filter_box_last/validate.py), [copy manifest](../evidence/Roth.card_filter_box_last/copy-manifest.json).

Accepted native receipts are complete successful checks, with zero errors/warnings, no partial disk response and only propext, Classical.choice, Quot.sound. Rejected initial attempts are explicitly separated in the ledger. Exact written sources and original execution locations are retained. Web limitations are recorded honestly: optional ChatGPT absent, local index unavailable, nLab XHTML inaccessible, explicit nCatLab namespace inaccessible, dated arXiv search empty. None supports a claim of exhaustive absence.
