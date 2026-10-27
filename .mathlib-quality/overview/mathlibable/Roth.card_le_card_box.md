# Roth.card_le_card_box — full mathlibable assessment

Verdict: **BORDERLINE-needs-human**. This is the elementary finite-product upper bound, expressed for natural-valued finitely supported multiindices. The general FUNCTION-family version is exactly a three-fact composition; transfer to the original Finsupp/natural-endpoint form adds real representation and endpoint steps. A project-parent replay is short, but its project lemmas are not mathlib building blocks. The independently checked typed-injection proof already uses four mathematical facts, before structural membership/extensionality steps. Upstream design should distinguish a general finite-family estimate from its natural-number specialization; no cost-based downgrade or search-based absence claim is made.

## Phase 0 — baseline

The shared successful build applies: all 17 source/pin SHA256 values were freshly checked against the shared manifest. No production source or pin changed. The declaration resolves at `Roth/Box.lean:65`, is a public theorem, and contains no sorry. The module develops boxes of multiindices and their real weights. Evidence: [baseline](../evidence/Roth.card_le_card_box/baseline-build.txt), [input hashes](../evidence/Roth.card_le_card_box/input-manifest.json), [source and caller hashes](../evidence/Roth.card_le_card_box/source-hashes.json).

## Phase 1 — statement and proof

For a finite index set σ, let s be a finite set of natural-valued multiindices, and let r assign a natural upper bound to each coordinate. If every d in s satisfies d(j) ≤ r(j) in every coordinate, then s has at most ∏j(r(j)+1) elements. Each independent coordinate has r(j)+1 possible values; an injective coordinate representation maps s into their product.

The complete elaborated type is:

```lean
∀ {σ : Type u} [Fintype σ] {r : σ → ℕ} {s : Finset (σ →₀ ℕ)},
  (∀ d ∈ s, ∀ j, d j ≤ r j) → s.card ≤ ∏ j, (r j + 1)
```

There is **no public DecidableEq σ binder**: the enclosing `omit` removes it and the proof uses `classical` internally. σ is universe polymorphic; Fintype supplies the finite product; r supplies coordinate bounds; s records distinct multiindices; hs supplies the essential containment hypothesis. The original proof uses `Finset.card_le_card`, project `mem_box`, project `card_box`, and transitivity with equality. Its native replay and the independent Fin-valued injection both compile with only `propext`, `Classical.choice`, `Quot.sound`: [exact executed project source](../evidence/Roth.card_le_card_box/project-executed.lean.txt), [complete native receipt](../evidence/Roth.card_le_card_box/native-project.json).

## Phase 2 — preliminary classification

**SMALL**: a finite counting helper, not a named main theorem or new structure. The module's main-results list names `card_box`, not this helper. Phase 2b is **n/a — theorem**; the one-line-definition exemptions do not apply. This does not reduce literature width.

## Phase 3 — exhaustive literature

All named literature channels were checked, including at least three distinct broad web queries; the optional mathematical ChatGPT service is unavailable. The exact requests, returned-response hashes and byte lengths are retained without search/article bodies: [requests](../evidence/Roth.card_le_card_box/literature-requests.md), [channel synthesis](../evidence/Roth.card_le_card_box/literature-summary.json).

| Channel / actual request | Result and primary locator |
|---|---|
| General web: “finite Cartesian product cardinality subset product cardinalities multiplication principle” | Multiplication principle / Cartesian counting. [receipt0](../evidence/Roth.card_le_card_box/web-0.json) |
| General web: “bounded multiindices number at most product degrees plus one polynomial support” | Polynomial multi-degree and bounded monomial contexts; no uniquely named sharper replacement. [receipt1](../evidence/Roth.card_le_card_box/web-1.json) |
| General web: “finite product cardinality upper bound coordinatewise bounded natural functions” | General finite-product formulation. [receipt2](../evidence/Roth.card_le_card_box/web-2.json) |
| ChatGPT MCP | n/a: ask_chatgpt_math unavailable; no fabricated second opinion or historical evolution answer. |
| Local clean.tex | §3 proof of Lemma3, lines454–456, sets N=∏j(rj+1) and pads the expansion; [exact excerpt](../evidence/Roth.card_le_card_box/local-reference.txt). |
| nLab: “site:ncatlab.org/nlab/show finite product cardinality”; direct finite-number page | Search access describes the cardinality functor on finite-set injections and multiplicativity. [finite number](https://ncatlab.org/nlab/show/finite%2Bnumber), section Cardinality functor. Direct XHTML access fails400; [search receipt3](../evidence/Roth.card_le_card_box/web-3.json), [fetch receipt10](../evidence/Roth.card_le_card_box/web-10.json). |
| nCatLab: “site:ncatlab.org/ncatlab finite sets products cardinality”; separate namespace page | Search routes to nLab finite-set/product material; separate nCatLab namespace inaccessible. No distinct higher-category improvement established. [search4](../evidence/Roth.card_le_card_box/web-4.json), [access8](../evidence/Roth.card_le_card_box/web-8.json). |
| Stacks: “site:stacks.math.columbia.edu cardinality finite product sets”; direct tag000D | Cardinal multiplication is defined by Cartesian product; [§3.6 Cardinality](https://stacks.math.columbia.edu/tag/000D), lines16–20. This supports the underlying principle, not an exact packaged multiindex estimate. [search5](../evidence/Roth.card_le_card_box/web-5.json), [access11](../evidence/Roth.card_le_card_box/web-11.json). |
| MathOverflow: “site:mathoverflow.net cardinality bounded multiindices product” | Returned infinite/sigma-product and ultraproduct questions; no direct finite bounded-multiindex result. [receipt6](../evidence/Roth.card_le_card_box/web-6.json) |
| Recent arXiv, 2021-10-26 through 2026-10-26 | Fresh polynomial/support/degree searches and abstracts. [Im et al., 2025](https://arxiv.org/abs/2504.02770) and [Deeds et al., 2022](https://arxiv.org/abs/2201.04166) concern database cardinality bounds and are tangential. [Bourneuf et al., revised2024](https://arxiv.org/abs/2311.03341) is graph degree-boundedness, a name collision. No change to the elementary standard form follows. [search7](../evidence/Roth.card_le_card_box/web-7.json), [search9](../evidence/Roth.card_le_card_box/web-9.json), [abstracts12](../evidence/Roth.card_le_card_box/web-12.json). |

Literature synthesis: the standard general form bounds any injectively represented finite family of tuples by the product of finite coordinate-set sizes. Natural coordinate intervals are one specialization. The local source and abstract cardinal-product description agree; no sourced historical novelty is claimed.

## Phase 4a/4b — hypotheses and generality

| Parameter / assumption | Use and generality |
|---|---|
| `σ : Type u` | Already arbitrary and universe polymorphic; no `Fin n` restriction. |
| `[Fintype σ]` | Required for the displayed all-coordinate finite product and automatic finite support. A support-local restatement permits infinite ambient σ; simply dropping the binder does not preserve the displayed statement. |
| `r : σ → ℕ` | Arbitrary function; zero bounds permitted, no positivity, uniformity, or monotonicity premise. Changing to a Finsupp upper bound changes the representation, with a support product. |
| `s : Finset (σ →₀ ℕ)` | Arbitrary distinct finite multiindices, not just polynomial support. Arbitrary injective coordinate representations and dependent finite coordinate sets give an abstract generalization. |
| `hs` | Essential containment, already localized to members of s. No condition imposed on nonmembers. |
| `DecidableEq` | Already absent publicly; classical reasoning local. |
| `ℕ` values / `rj+1` | Natural interval cardinality; general finite coordinate sets or locally finite ordered intervals replace the concrete successor formula. |

The fixed current interface is maximally general with respect to unused-argument removal. Wider representations are real restatements rather than deletion of a redundant hypothesis. Native evidence below distinguishes the validated wider forms from any untested proposal. This is not an unverified “drop Fintype” recommendation, and no YES-but-generalise-first claim is inferred from such a guess.

## Phase 4c — nine modern-idiom rows

| # | Question | Answer, proposal, and concrete downstream consequence |
|---|---|---|
| 1 | Typeclass preamble | Already `Fintype`; hs is a local finite-family membership premise, not a new instance. No new typeclass recommended. |
| 2 | Filters / nets / topology | No: finite combinatorics contains no limiting process. |
| 3 | Universal-property class | No new class: existing dependent products provide the coordinate representation and `Fintype.card_pi` counts it. |
| 4 | Bundled substructure | No closure structure; Finset is the appropriate finite container. An interval Finset uses existing order API rather than a new box bundle. |
| 5 | Modules / weaker algebra | No field/vector-space hypothesis. Generic coordinate sets require no algebra; this removes natural payload structure by restatement. |
| 6 | Higher categories | No demonstrated consequence beyond existing products of finite types; a higher-category statement adds no useful bound here. |
| 7 | Concrete ℕ index/value | Yes for values: replace natural coordinate bounds by finite coordinate-set membership; support-local Iic form serves arbitrary ambient indices and locally finite ordered values. Index σ itself already arbitrary. |
| 8 | Concrete-via-abstract diagnostic | Fires: after membership conversion the proof has zero explicit Finsupp/ℕ mentions and only cardinal containment plus product size. Abstract finite-family API can serve arbitrary finite alphabets and dependent coordinates. [diagnostic](../evidence/Roth.card_le_card_box/q8-diagnostic.json) |
| 9 | False-generalisation guard | Preserve injectivity/distinctness and all coordinate restrictions. Infinite ambient indices require finite support data; arbitrary `r : σ → ℕ` alone no longer gives a finite bounding interval. Replacing Finset by a multiset also requires accounting for multiplicities. No unchecked widening accepted. |

Modern idiom available: finite dependent product / support-local order interval. The actionable gain is reuse for arbitrary alphabets and infinite ambient sparse indices. The general FUNCTION-family estimate is already a three-fact composition, so this assessment does not claim a missing abstract theorem there. Whether an additional Finsupp/natural-endpoint convenience estimate is justified remains an upstream API-design choice.

## Phase 4.5 — infrastructure risk

n/a — theorem; introduces no definition, instance, or coercion. Therefore typeclass diamonds, reducibility leak, noncanonical unfolding, priority collision, universe implementation, and coercion ambiguity are each n/a, rather than six unchecked low-risk assertions.

## Phase 4.6 — five proof-strategy rows

| # | Strategy | Answer / alternative |
|---|---|---|
| 1 | ε–δ versus filters | n/a, no topology. |
| 2 | Elements versus ideal/submodule inclusion | n/a, no algebraic substructure. Finset containment is already the correct counting argument. |
| 3 | Sequences versus nets | n/a, no analysis. |
| 4 | Construction versus universal property | Existing product types suffice; construct an injective coordinate map and apply cardinal comparison. No new universal-property class needed. |
| 5 | Missing helper API | The generic FUNCTION-family bound already composes from three existing facts. A Finsupp/natural-endpoint convenience bound or support-local specialization could package additional conversion steps. Their necessity is not established merely by failed search. |

Verdict: **REFACTOR-RECOMMENDED** for upstream design: use existing product/interval API, expose the normalization steps, and decide which general convenience estimate is justified. Original downstream proof remains mathematically sound.

## Phase 5 — actual five methods on three forms

All methods were actually called afresh. Current form: bounded natural Finsupp cardinality. Standard form: subset of finite Cartesian product. Abstract form: locally finite Finsupp lower interval/support product. External indices may differ from the pin.

| Method | Current | Standard | Abstract |
|---|---|---|---|
| Lean-Finder | [receipt](../evidence/Roth.card_le_card_box/finder-current.json): Finsupp/DFinsupp interval cards | [receipt](../evidence/Roth.card_le_card_box/finder-standard.json): product/cardinal estimates and `card_piFinset` | [receipt](../evidence/Roth.card_le_card_box/finder-abstract.json): `Finsupp.card_Iic` |
| Loogle | [receipt](../evidence/Roth.card_le_card_box/loogle-current.json): no direct bound | [receipt](../evidence/Roth.card_le_card_box/loogle-standard.json): `Fintype.card_piFinset` | [receipt](../evidence/Roth.card_le_card_box/loogle-abstract.json): `Finsupp.card_Iic`, `Nat.card_Iic` |
| LeanSearch | [receipt](../evidence/Roth.card_le_card_box/leansearch-current.json): `card_finsupp`/`card_pi` | [receipt](../evidence/Roth.card_le_card_box/leansearch-standard.json): generic product-cardinality estimates | [receipt](../evidence/Roth.card_le_card_box/leansearch-abstract.json): intervals and `Pi.card_Iic` |
| rg pinned sources | [receipt](../evidence/Roth.card_le_card_box/rg-current.json) | [receipt](../evidence/Roth.card_le_card_box/rg-standard.json) | [receipt](../evidence/Roth.card_le_card_box/rg-abstract.json) |
| Local name search | [receipt](../evidence/Roth.card_le_card_box/local_search-current.json) | [receipt](../evidence/Roth.card_le_card_box/local_search-standard.json) | [receipt](../evidence/Roth.card_le_card_box/local_search-abstract.json) |

Local index explicitly reports **unavailable**; current local declaration may still be returned. This is not negative evidence about mathlib. The [untruncated full-name search](../evidence/Roth.card_le_card_box/full-name-source-search.json) has no pinned exact-name hit. Together these establish candidate APIs, not absence of a generic elaborated term.

Pinned candidates: `Finset.card_le_card_of_injective` and `Finset.card_le_card_of_injOn` in `Mathlib/Data/Finset/Card.lean`; `Fintype.card_pi`, `Fintype.card_piFinset` in `Mathlib/Data/Fintype/BigOperators.lean`; `Fintype.card_fin` in `Mathlib/Data/Fintype/Card.lean`; `Finset.card_finsupp` / `mem_finsupp_iff` in `Mathlib/Data/Finset/Finsupp.lean`; `Finsupp.card_Iic` in `Mathlib/Data/Finsupp/Interval.lean`; `Nat.card_Iic` in `Mathlib/Order/Interval/Finset/Nat.lean`. `Finsupp.card_Iic` uses a support product, not the original all-coordinate product. Project `box`, `mem_box`, and `card_box` never count as existing mathlib facts.

## Phase 5.5 — statement shape

Normal form: **OK**. A cardinal upper bound is correctly oriented; no simplification lemma should rewrite every Finset cardinality into a product. Alternative shapes audited: strict coordinate bounds `d j < r j + 1`, a bundled subset of an `Iic`, and a finite-family injection into a dependent product. Strict bounds align with Fin constructors; subset bounds align with order intervals; the present hs aligns directly with both actual degreeOf callers.

Superfluous-argument audit: σ determines coordinates, Fintype determines the all-coordinate finite product, r determines admissible values, s determines the counted distinct family, hs supplies containment. No public DecidableEq to drop. Finite/support formulations are restatements, not deletions of a redundant argument. Overall **SHIP-AS-STATED locally**, with **RESTATE-BEFORE-SHIP** if choosing an upstream generic estimate.

## Phase 6.0 — all explicit callers and inline audit

Internal use count: **2 occurrences in 2 declarations**, external to the declaring file in **2 files**; [complete explicit grep](../evidence/Roth.card_le_card_box/explicit-callers.json), [inline audit](../evidence/Roth.card_le_card_box/inline-audit.json). This is source-level usage, not opaque kernel/simp dependency closure. Target is not a simp lemma and is not dead code.

| Caller | Actual use and action if replaced |
|---|---|
| `Roth/CoeffNorm.lean:264`, `abs_coeff_det_hasseDeriv_le` | `exact_mod_cast card_le_card_box fun d hd j ↦ (monomial_le_degreeOf j hd).trans (hP j)`. Apply generic counting to `P.support` and degreeOf bounds; retain real-product cast normalization. |
| `Roth/MainLemma.lean:506`, private `abs_coeff_diag_hasseDeriv_modByMonic_le_aux` | Same estimate for `(hasseDeriv j P).support` using `hdP`; retain cast of the natural product. The consumer is private but is still an actual caller of this public helper. |

No additional inline derivation of the same complete bound was located. Other box-cardinality / support estimates in Roth have different conclusions. The callers show useful repeated natural-coordinate usage; they do not themselves demonstrate an upstream missing lemma.

## Phase 6 — actual composition experiments

1. **Original replay succeeds**, using project `mem_box` and `card_box`. This validates the theorem but cannot establish NO-composable-from-mathlib.
2. **Independent Fin-valued injection succeeds** with no target or project-parent calls. Its mathematical facts are `Finset.card_le_card_of_injective`, `Fintype.card_pi`, `Fintype.card_fin`, and **`Nat.lt_succ_of_le`** for hs-to-Fin conversion. Structural steps include `Finset.mem_univ`, `Subtype.ext`, `Finsupp.ext`, `congrArg`, `congrFun`, and `funext`; all remain visible in the archived exact source. This is not honestly a three-call term.

No raw ≤3 existing-call proof of the exact statement is established by these experiments. The threshold is not a proof-length contest: a true small term could support NO, whereas a closing `simp [defs...]` is explicitly **Phase6b borderline**, not an automatic NO. A failed search or unsuccessful candidate does not prove nonexistence. Wider forms and caller normalization are recorded in the native supplement below.

### Native supplement — generic re-aim, support, shapes, and actual casts

[Isolated exact executed source](../evidence/Roth.card_le_card_box/raw-executed.lean.txt) imports only mathlib and explicitly checks `#check_failure Roth.card_le_card_box`. [Complete raw native success](../evidence/Roth.card_le_card_box/native-raw.json) has success=true, partial=false, no errors/warnings and standard axioms only. It verifies:

- `expanded_original`: seven existing domain facts, `Finset.mem_map_equiv`, `Fintype.mem_piFinset`, `Finset.mem_range_succ_iff`, `Finset.card_le_card`, `Finset.card_map`, `Fintype.card_piFinset`, `Finset.card_range`, with congruence/extensionality glue. No project parent is counted.
- `fin_injection`: the four-fact route already described; `Nat.lt_succ_of_le` is counted explicitly.
- `function_family`: for arbitrary dependent coordinate types βj, finite family s of functions and finite coordinate sets tj, membership implies `s.card ≤ ∏j,(tj).card`. This **is an exact three-existing-fact composition**:

```lean
(Finset.card_le_card fun f hf ↦ Fintype.mem_piFinset.mpr (hs f hf)).trans_eq
  (Fintype.card_piFinset t)
```

This proves the modern generic FUNCTION-family form is composable, rather than showing a missing generic helper. The newly named scratch `function_family` itself is not a pre-existing mathlib declaration and cannot be used to shorten the counted original derivation.

- `support_interval`: with **arbitrary ambient σ**, upper bound `r : σ →₀ ℕ`, and finite s, the bound is `s.card ≤ ∏j∈r.support,(rj+1)`. The proof uses subset cardinality, `Finset.mem_Iic`, `Finsupp.card_Iic`, then `simp` for coordinate interval sizes. This closing normalization route is **Phase6b borderline**; a support product is not silently replaced by the all-coordinate product.
- `support_finite_bound`: the same arbitrary ambient result for an ordinary function r with `[Finite (Function.support r)]`, converted by `Finsupp.ofSupportFinite`. This is a verified wider representation, not a claim that arbitrary infinite-support r bounds a finite box.

The final [project source](../evidence/Roth.card_le_card_box/project-executed.lean.txt) and [success receipt](../evidence/Roth.card_le_card_box/native-project.json) additionally verify `strict_shape` (`dj<rj+1`), `support_local_shape` (checking only j∈d.support), and the exact expanded-real-product / cast-natural-product degreeOf consumer patterns. The support-local premise is **logically equivalent**, not a strict weakening: outside d.support the value is zero and `0≤rj`. Both actual caller formats work using the independent four-fact proof; no imported target theorem is used to prove them. A two-element Unit-indexed finite set `{0,single () 1}` with r=0 gives a compiled guard showing hs cannot be dropped.

A candidate attempt to eliminate the fourth endpoint-conversion fact through a subtype `Iic` cardinality failed at type alignment of `Nat.card_Iic`; its exact code and rejection remain separate: [rejected source](../evidence/Roth.card_le_card_box/cardLeBox-subtype-rejected-executed.lean.txt), [receipt](../evidence/Roth.card_le_card_box/cardLeBox-subtype-rejected.json). This failure is not absence evidence. Earlier argument-shape and local elaboration errors are retained separately as [target rejection](../evidence/Roth.card_le_card_box/cardLeBox-target-rejected.json) and [extra rejection](../evidence/Roth.card_le_card_box/cardLeBox-extra-rejected.json); none is counted as accepted proof evidence.

## Phase 7 — actionable verdict

**BORDERLINE-needs-human**, based on API design and normalization rather than expense or uncertainty about theorem validity. Keep the useful helper in project-local `Roth/Box.lean` while the upstream target is chosen; do not delete it merely because its parents were independently assessed NO. The exact natural formula and a support-local interval estimate have different interfaces and consumers; the generic FUNCTION-family form itself is already composable in three facts. Searches found existing counting infrastructure, but the direct ≤3-call replacement gate has not been met.

Concrete future upstream questions:

1. Should a Finsupp natural-endpoint convenience bound be added despite the verified four-fact injection route, or should its consumers keep the existing injection/product-cardinality argument locally?
2. Should `Mathlib/Data/Finsupp/Interval.lean` expose a support-local finite-subset upper bound derived from `card_Iic`, especially to serve infinite ambient indices?
3. If an upstream bound is added, should the natural successor-product form remain only a project-local specialization, or receive a named Finsupp convenience theorem with demonstrated consumers?

These are design follow-ups, not a request to stop this read-only assessment. No YES PR/grouping is proposed; the accepted YES declarations in progress concern Hasse-derivative API and do not justify grouping an unrelated counting interface. Any later contribution should run `/generalise Roth.card_le_card_box`, `/cleanup Roth/Box.lean Roth.card_le_card_box`, and select reviewers from the relevant product/interval module history.

## Phase 8 — handoff

All supporting exact sources, native success receipts, search requests, and hashes are collected in the portable package. No production edits or pin changes are proposed as part of this assessment. Root independently reviews the frozen artifacts before integration.
