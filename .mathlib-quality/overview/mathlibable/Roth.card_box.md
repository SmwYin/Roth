# Roth.card_box — full mathlibable assessment

Verdict: **NO-composable-from-mathlib**. The original statement follows from precisely three existing cardinality facts, with equality transitivity/congruence as logical glue. This is an independent assessment, not an inherited verdict about Roth.box or Roth.mem_box.

## Phase 0 — baseline
The shared successful lake build is reusable: all 17 current source/pin SHA256 values were freshly checked against the manifest. No production files or pins were edited. Declaration resolves at Roth/Box.lean:57; theorem, no sorry. Box.lean sets up finite boxes and real weights of polynomial multi-indices.
Evidence: [baseline](../evidence/Roth.card_box/baseline-build.txt), [manifest](../evidence/Roth.card_box/input-manifest.json), [hashes](../evidence/Roth.card_box/source-hashes.json), [complete declaring module](../evidence/Roth.card_box/Roth-Box.lean.txt).

## Phase 1 — comprehension
For a finite index set σ and arbitrary natural bounds r(j), the finite family of natural multi-indices d with 0≤d(j)≤r(j) has cardinality ∏j(r(j)+1). Each coordinate has r(j)+1 independent choices. Transport through the equivalence between functions and finitely supported functions preserves cardinality.

Full elaborated type: `∀ {σ : Type u} [Fintype σ] [DecidableEq σ] (r : σ → ℕ), (Roth.box r).card = ∏ j, (r j + 1)`.
σ is universe-polymorphic; Fintype enumerates coordinates and the product; DecidableEq supplies the parent box interface; r is arbitrary and explicit. No positivity, nonempty, ordering on σ, or polynomial hypothesis occurs. The proof unfolds box and uses map, dependent product, and natural range cardinalities.

## Phase 2 — preliminary
**BIG**, because the module lists card_box among Main results (the criterion is syntactic; the mathematics is elementary).
One-line definition-only test: **n/a — theorem**. Its short proof is not a definition-only exemption or automatic negative verdict.

## Phase 3 — fresh exhaustive literature
All nine channels were attempted afresh. Exact requests, returned-response SHA256, bytes, status and source URLs appear in web-0 through web-11; article/search bodies were not persisted.

| Channel | Fresh result and locator |
|---|---|
| General web, ≥3 distinct queries | Box multi-index counting; bounded Roth indices; lower Finsupp intervals; later product principle search. Finite product counting is the ordinary multiplication rule. |
| ask_chatgpt_math | Unavailable: no callable tool in current tool inventory; no claimed second opinion. |
| Local reference | clean.tex §6 Lemma 8 lines 1070–1075 states the product counts coordinatewise bounded solutions; Lemma 9 equation (43), lines 1419–1421 records the same product. |
| nLab | Search found “cartesian product” and “cardinal arithmetic”: finite set multiplication is represented by Cartesian product. Direct fetch failed with unsupported application/xhtml+xml (400). Search metadata only. |
| nCatLab | Separate categorical finite-product query found “finite product”; distinct category-theoretic lens. The actual categorical query contained the misspelled domain filter `site.ncatlab.org`; its request is preserved. An [explicit nCatLab namespace open](../evidence/Roth.card_box/web-11.json) failed as inaccessible. No new cardinality result. |
| Stacks | Targeted search found Sets chapter; direct tag 0005 was accessible but concerns categories, not this identity. No exact useful theorem located. |
| MathOverflow | Targeted cardinality/product query returned elementary counting material, no directly matching MO result. This is not evidence of absence. |
| arXiv, last five years | Dated 2022–2026 query; opened arXiv:2509.17880, submitted 2025-09-22, revised 2026-01-21. “A non-linear Roth theorem for thick Cantor sets” concerns progressions, not bounded-multi-index cardinality. No alternative formulation extracted. |
| Primary teaching source | Edinburgh Etessami Counting notes search locator Chapter 6 slide 3 gives product rule. Direct PDF fetch returned 410 Gone; search metadata only. |

All named protocol channels and at least three distinct general-web forms were covered; the teaching source is supplementary. See [channel ledger](../evidence/Roth.card_box/literature-summary.json) and [every exact query/access row](../evidence/Roth.card_box/literature-requests.md) for exact accounting. [local excerpt](../evidence/Roth.card_box/local-reference.txt), [general web](../evidence/Roth.card_box/web-0.json), [nLab search](../evidence/Roth.card_box/web-1.json), [categorical search](../evidence/Roth.card_box/web-2.json), [Stacks](../evidence/Roth.card_box/web-3.json), [MO](../evidence/Roth.card_box/web-4.json), [arXiv search](../evidence/Roth.card_box/web-5.json), [primary accesses](../evidence/Roth.card_box/web-10.json).

The standard form is cardinality of a finite dependent Cartesian product of arbitrary finite coordinate sets. The natural-range and Finsupp choices are representations specific to polynomial exponents. The local paper additionally assumes positive dimensions/bounds for analytic arguments; the count itself holds with zero bounds and empty σ. No literature-based novelty claim is made.

## Phase 4a–b — parameters and generality
| Parameter or restriction | Actual check | Consequence |
|---|---|---|
| Type u | Already universe-polymorphic | No universe weakening needed. |
| Fintype σ | Original product and parent box require enumeration; dropping literally does not state the same interface | Finite-only would choose Fintype.ofFinite or use support-indexed product, changing representation. |
| DecidableEq σ | Direct omission inside the existing instance section failed; scoped Classical statement compiles with no public DecidableEq binder | This chooses Classical inside the parent box application; it does not establish definitional independence from every supplied decision instance. |
| Natural coordinates | Mapped arbitrary dependent finite coordinate sets compile with card_map + card_piFinset | Genuine counting generalisation, already supplied by mathlib. |
| Global finite index | Finsupp lower intervals over arbitrary σ compile using support-indexed cardinality | General finite-support formulation exists as Finsupp.card_Iic; not a literal weakening of Roth.box. |
| r | Arbitrary, explicit, no side conditions | No hypothesis to drop or localise. |
| Positivity/nonempty | Absent already; zero bound and Empty cases compile | Cannot impose paper assumptions as extra requirements. |
| Infinite unconstrained index | An everywhere-positive bound allows infinitely many single-coordinate vectors | Reject unrestricted finite cardinality; finite-support bound or finite coordinates is essential. |

Relative to the fixed parent interface the theorem uses the required instances. Relative to the literature-standard abstract counting form it is strictly specialised; the broader actual native experiment verifies that claim, and the broader API already exists. No generalise-first ticket is needed for a duplicate.

## Phase 4c — nine modern idiom rows
| # | Question | Result / reformulation / actual downstream effect |
|---|---|---|
| 1 | Typeclass preambles | Already Fintype and DecidableEq; no bundled hypothesis to replace. Scoped Classical can remove public decision requirement with the caveat above. |
| 2 | Sequences to filters | No: finite cardinality, no limits/topology. |
| 3 | Construction to universal property | No new characterising class needed; the dependent Cartesian product is existing piFinset. |
| 4 | Predicate to bundled substructure | No closure substructure. Finset.Iic is a canonical ordered interval with membership/subset APIs. |
| 5 | Algebraic hierarchy | No ring/field assumptions. Arbitrary finite dependent coordinate sets remove reliance on ℕ arithmetic, via existing card_piFinset. |
| 6 | Higher category | No: cardinality in finite sets does not benefit from categorical lifting here. |
| 7 | Concrete ℕ to ordered structure | Yes: Finsupp.card_Iic counts principal lower intervals in locally finite ordered additive types, over finite support; Pi.card_Iic counts dependent coordinate intervals. Enables arbitrary finite interval counting. |
| 8 | Concrete-via-abstract | **Fires**: proof body `simp [box]` has one line mentioning box, zero after unfolding. Abstract mapped dependent-product cardinality is card_map followed by card_piFinset; no missing abstract lemma. |
| 9 | False-generalisation guard | Arbitrary dependent finite sets and embeddings preserve independent-choice counting; noninjective maps would collapse points and invalidate equality. Infinite unrestricted boxes are rejected. |

Modern idiom available: yes, but already in mathlib. The useful consequence is access to arbitrary coordinate sets/embeddings and support-indexed intervals, not an upstream Roth-specific wrapper. [Q8 diagnostic](../evidence/Roth.card_box/q8-diagnostic.json).

## Phase 4.5 — infrastructure risks
**n/a — theorem**: no instances, definitions, coercions or reduction rules are introduced. All six definition risk rows (diamond, reducibility leak, unfolding, instance priority, universes, coercions) are n/a for this declaration. Parent box representation issues were considered in Phase 4, not attributed to this proof.

## Phase 4.6 — proof strategy
| # | Strategy check | Result |
|---|---|---|
| 1 | εδ versus filters | n/a: no topology. |
| 2 | Element algebra versus substructures | n/a: no algebraic closure argument. |
| 3 | Sequences versus nets | n/a: no analysis. |
| 4 | Explicit construction versus universal property | Existing dependent product is the appropriate finite-set construction; no new universal property API. |
| 5 | Missing helpers mathlib should have | None identified: map cardinality, dependent-product cardinality and range cardinality exist. |

**MATHLIB-IDIOMATIC** counting strategy. The original simp proof is natural; the explicit term below makes the composability audit independent of automation.

## Phase 5 — actual five methods × three forms
Forms: current bounded Finsupp box; standard arbitrary finite dependent Cartesian product; abstract lower interval in Finsupp.
| Method | Current | Standard | Abstract |
|---|---|---|---|
| Finder | Finsupp.card_Iic, DFinsupp.card_Iic, Behrend.card_box | Fintype.card_piFinset/card_pi, Finset.card_pi | Finsupp/DFinsupp.card_Iic/Icc |
| Loogle | Finset.card_map | Fintype.card_pi | Finsupp.card_Iic, Pi.card_Iic, Nat.card_Iic |
| LeanSearch | Finsupp.card_pi/Icc, DFinsupp.card_Iic | Nat.card_pi, set/cardinal product APIs | Finsupp.card_Iic, Pi.card_Iic |
| rg pinned source | map/range and piFinset facts | pi/card product sources | Finsupp/Pi interval facts |
| Local name search | card_piFinset located | card_pi located | Finsupp.card_Iic located |

Local index reports **unavailable** while source-backed matches are returned: not an indexed absence proof. External indices need not match the pinned revision; all decisive candidates are source-inspected and native checked. Behrend.card_box uses uniform ordinary-function boxes, so is a near-match, not Roth.card_box.

Raw exact requests/results: [Finder current](../evidence/Roth.card_box/finder-current.json), [Finder standard](../evidence/Roth.card_box/finder-standard.json), [Finder abstract](../evidence/Roth.card_box/finder-abstract.json), [Loogle current](../evidence/Roth.card_box/loogle-current.json), [Loogle standard](../evidence/Roth.card_box/loogle-standard.json), [Loogle abstract](../evidence/Roth.card_box/loogle-abstract.json), [LeanSearch current](../evidence/Roth.card_box/leansearch-current.json), [LeanSearch standard](../evidence/Roth.card_box/leansearch-standard.json), [LeanSearch abstract](../evidence/Roth.card_box/leansearch-abstract.json), [local current](../evidence/Roth.card_box/local_search-current.json), [local standard](../evidence/Roth.card_box/local_search-standard.json), [local abstract](../evidence/Roth.card_box/local_search-abstract.json), [rg current](../evidence/Roth.card_box/rg-current.json), [rg standard](../evidence/Roth.card_box/rg-standard.json), [rg abstract](../evidence/Roth.card_box/rg-abstract.json), [untruncated full name search](../evidence/Roth.card_box/full-name-source-search.json).
Conclusion: existing building blocks yield the original form; no claimed exhaustive absence.

## Phase 5.5 — statement shape
1. **Normal form:** finite cardinality equals product of coordinate cardinalities; after evaluating ranges RHS becomes ∏j(rj+1). Canonical arithmetic expression is already on RHS. Alternatives are successor spelling, ∏j Fintype.card(Fin(rj+1)), Nat.card finite coordinate types, or support-indexed Iic. The last requires a representation choice.
2. **Syntactic generality:** successor and Fintype-card Fin forms were actually compiled; the original product is easiest in all three existing numerical consumers. Natural-card variant checked separately with its requisite import, not assumed available through current imports.
3. **Superfluous arguments:** no ordinary proposition hypotheses. r must remain; σ and its finiteness determine the parent box/product. DecidableEq may be hidden by scoped Classical, with the explicit instance-choice limitation above. No blind unused-binder claim.

Shape verdict: **KEEP** for the local representation, while deleting the redundant wrapper during a coordinated caller refactor.

## Phase 6.0 — callers and inline audit
Internal use count: **3 occurrences in 3 declaration callers**, two external modules. Module documentation and the definition head are excluded.
| File:line | Caller | Mechanical replacement |
|---|---|---|
| Roth/Box.lean:68 | card_le_card_box | Replace `card_box r` in trans_eq with the explicit three-fact equality. |
| Roth/Lattice.lean:163 | private card_filter_weight_le_of_le_sqrt_aux | Rewrite the natural cardinality by the composition, then Nat.cast_prod, Nat.cast_add, Nat.cast_one. |
| Roth/Main.lean:405 | abs_eval_lt_of_le_index | After sum_const rewrite cardinality by the composition; retain nsmul_eq_mul, push_cast, ring. |

All three actual caller **patterns** (subset bound, real cast, constant finite sum) were compiled with the replacement. This is not a rebuilt production refactor, because production changes are prohibited for this read-only assessment. Source-level refs are not opaque kernel/simp dependency closure. The theorem has no simp attribute.
Inline-derivation grep: zero independent instances of this same box cardinality; boxFamily ncard is a different coefficient-family count. Three uses establish real local utility but do not override an exact existing-call composition.
Evidence: [callers](../evidence/Roth.card_box/explicit-callers.json), [source search](../evidence/Roth.card_box/callers.json), [inline audit](../evidence/Roth.card_box/inline-audit.json), [Lattice complete](../evidence/Roth.card_box/Roth-Lattice.lean.txt), [Main complete](../evidence/Roth.card_box/Roth-Main.lean.txt).

## Phase 6 — actual composition and Phase6b guard
Pinned building blocks:
* Finset.card_map — Mathlib/Data/Finset/Card.lean:271.
* Fintype.card_piFinset — Mathlib/Data/Fintype/BigOperators.lean:124.
* Finset.card_range — Mathlib/Data/Finset/Card.lean:174.

```lean
  (Finset.card_map _).trans ((Fintype.card_piFinset _).trans
    (congrArg (fun f : σ → ℕ ↦ ∏ j, f j) (funext fun j ↦ Finset.card_range (r j + 1))))
```

These are three domain facts. Eq.trans, congrArg and funext only compose equalities; they are not extra mathematical counting lemmas. The term uses no simp, Roth.card_box, Roth.mem_box, new bridge lemma or downstream project fact. Roth.box unfolds definitionally. A matching isolated mathlib-only replay uses the same raw definition and guards Roth.card_box as absent.

The Iic route is additionally available through Finsupp.card_Iic, Finsupp.prod_fintype and Nat.card_Iic; it counts over support before extending to all finite coordinates. It is evidence for generality, not a reason to pretend that Roth.box is definitionally Iic.

**Phase6b guard preserved:** a bare closing `simp [box]` alone would leave the BORDERLINE question of packaging/API value. This verdict instead rests on an actually compiled explicit original-shape three-fact term and isolated replay, so it is not that guarded case.

## Phase 7 — verdict and action
**NO-composable-from-mathlib.** Existing generic finite-set counting already supplies the original result; the broader modern forms also exist. The reason is the positive compiled composition, not search failure, proof size, expected review cost, or prior verdicts.

Refactor plan: delete Roth.card_box only together with updating all three caller occurrences using the concrete replacements above. A short local `have hcard := <composition>` at the cast/sum consumers is sufficient; do not introduce an exported wrapper with a different name. Alternative destination if readability requires preserving the theorem: project-local Roth/Box.lean, documenting its polynomial multi-index notation. No Archive or satellite destination is needed for an elementary generic identity.

No upstream PR, reviewer selection, grouping or cleanup/generalise ticket applies to this NO verdict. Verification unresolved: []; root acceptance remains pending independent review.

## Phase 8 — evidence completion
[Verification ledger](../evidence/Roth.card_box/verification.json), [assessment](../evidence/Roth.card_box/assessment.json), [portable validator](../evidence/Roth.card_box/validate.py), [copy manifest](../evidence/Roth.card_box/copy-manifest.json). Native executed exact source and raw receipts are linked by the verification ledger. Accepted evidence has complete success (partial=false), no error/warning/sorry, and only propext, Classical.choice, Quot.sound axioms.

