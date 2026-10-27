# Roth.box — full mathlibable assessment

Verdict: **NO-composable-from-mathlib**. The coordinate box is the existing principal lower interval `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`. This is a two-operation construction from existing mathlib objects. Its local semantic name has real consumers, but does not justify a second upstream interval definition. No production changes are part of this assessment.

## Phase 0 — baseline and exact identity

All 17 source/pin hashes freshly match the shared clean baseline (2467 jobs, exit 0); see [input manifest](../evidence/Roth.box/input-manifest.json), [baseline](../evidence/Roth.box/baseline-build.txt), [source hashes](../evidence/Roth.box/source-hashes.json). The exact qualified declaration is `Roth.box`, a noncomputable definition at **Roth/Box.lean:47**; line 48 continues its body. Bare `box` has unrelated mathlib collisions, which are not a prefilter for this qualified declaration. The [complete declaring source](../evidence/Roth.box/Box-source.lean.txt) has no placeholders. The file develops boxes and real weights used by Taylor expansions, coefficient bounds and Roth's lattice estimate.

## Phase 1 — mathematical content

For a finite set of variables σ and a natural bound r(j) for each variable, the box consists of all natural multi-indices d with d(j) ≤ r(j) in every coordinate. It is a finite Cartesian product of the intervals {0,…,r(j)}, represented as finitely supported functions for use as monomial exponents. Zero bounds and the empty variable type are allowed; positivity belongs to later estimates, not this construction.

The full native type is `{σ : Type u} → [Fintype σ] → [DecidableEq σ] → (σ → ℕ) → Finset (σ →₀ ℕ)`. σ is universe-polymorphic; Fintype enumerates coordinates, DecidableEq is consumed by piFinset, and r supplies upper bounds. There are no proposition hypotheses. The body maps `Fintype.piFinset (fun j ↦ Finset.range (r j + 1))` along the inverse of `Finsupp.equivFunOnFinite`. The equivalence preserves evaluation; this accounts for every element once. [Native verification index](../evidence/Roth.box/verification.json) retains exact executed sources and complete receipts.

## Phase 2 — preliminary checks

BIG: this is a named main definition in the module, although mathematically elementary. Exhaustive literature width is unchanged. The body has **one substantive line**.

| One-line exemption | Applies? | Evidence |
|---|---|---|
| Avoid defeq abuse | no | The body is openly unfolded by `simp [box]` in Box and CoeffNorm; no seal or controlled-unfolding barrier is used. |
| Avoid typeclass diamonds | no | The result is a Finset value, with no new instance, wrapper type or alternate algebraic structure. |
| Semantic intent / stable API | yes | `MvPolynomial.eq_sum_box_hasseDeriv`, `Roth.card_filter_box_last` and `sum_box_prod_pow_le_aux` use the name as a convenient common summation domain. |

Conclusion: ONE-LINER WITH-EXEMPTION. This permits considering the name on its merits; it does not defeat the concrete existing interval replacement.

## Phase 3 — fresh exhaustive literature

Exact requests and response digests/byte counts/status are retained in [web 0](../evidence/Roth.box/web-query-0.json), [web 1](../evidence/Roth.box/web-query-1.json), [web 2](../evidence/Roth.box/web-query-2.json), [opens](../evidence/Roth.box/web-open.json), [nCatLab attempt](../evidence/Roth.box/ncatlab-explicit.json). Only locators and original summaries are retained, not web response bodies. [Channel summary](../evidence/Roth.box/literature-summary.json) records conclusions.

| Channel / actual query | Outcome and source locator |
|---|---|
| Web specific: `"multi-index" "box" Roth theorem lattice points` | No independently new box API established; local Roth source gives the precise object. |
| Web general: `finite Cartesian product order intervals product order locally finite poset` | Product order / finite interval framework found, consistent with the canonical interval construction. |
| Web aliases: `rectangular integer lattice box bounded multiindices cardinality product` | Rectangular lattice terminology found; does not imply a new structure separate from products of intervals. |
| ChatGPT mathematical MCP | N/A: `ask_chatgpt_math` unavailable. Intended historical/generality question is recorded; no fabricated response. |
| Local clean.tex | §6 Lemma8, lines1051–1074: coordinate inequalities; Lean note1132–1137: finite interval-valued functions; Lemma9,1407–1420: bounded monomial exponents. [Exact local receipt](../evidence/Roth.box/local-reference.txt). |
| nLab: site query and direct pointwise-order URL | [Pointwise order](https://ncatlab.org/nlab/show/pointwise+order), Definition: function order is coordinatewise. Search returned the relevant account; direct open failed HTTP400 unsupported XHTML. |
| nCatLab: locally finite poset site query and explicit namespace URL | nLab categorical explanation identifies product in preorders; explicit `ncatlab.org/ncatlab/show/pointwise+order` was inaccessible. No extra categorical structure is needed for this finite subset. |
| Stacks: `site:stacks.math.columbia.edu finite product sets cardinality` | [Tag000D, §3.6](https://stacks.math.columbia.edu/tag/000D), lines17–20 provides Cartesian-product/cardinality context; no box-specific refinement. |
| MathOverflow: lattice points box coordinate bounds | [Listing all Lattice Points in a Box](https://mathoverflow.net/questions/215733/listing-all-lattice-points-in-a-box), question lines32–35 uses a product rectangle and arbitrary lattice. General irrational-lattice enumeration is distinct from this coordinate box. |
| Recent arXiv: Roth/lattice-box and coordinatewise integer-poset queries restricted in query text to2021–2026 | [2410.09716](https://arxiv.org/abs/2410.09716), submitted2024-10-13, revised2024-12-15, abstract: geometric/additive Roth configurations, rejected as unrelated. Older hits were not counted as recent evidence. The checked five-year window is2021-10-26–2026-10-26. |

The standard object is a Cartesian product of intervals, equivalently a lower interval for pointwise order. Literature varies between explicit finite tuples and abstract posets; nothing makes natural multi-indices a new order concept. Positive r in the lattice estimate is stronger than needed to define the box. No source establishes a historical change requiring a second definition.

## Phase 4a–b — all parameters and generality

| Parameter | Need in current representation | Verified route / limitation |
|---|---|---|
| σ : Type u | Arbitrary universe already supported | Type1 interval comparison compiled; no cardinality/universe restriction introduced. |
| Fintype σ | Needed by literal piFinset enumeration | `[Finite σ]` suffices noncomputably using `Fintype.ofFinite`; equality with current box compiled. |
| DecidableEq σ | Required by literal piFinset interface | A classical definition with no public DecidableEq binder compiled and equals current box. This is an actual weakening, not a linter guess. |
| r : σ → ℕ | Coordinate bounds indispensable | Natural codomain fits monomial exponents. Arbitrary ambient σ works if `Function.support r` is finite, via `Iic (Finsupp.ofSupportFinite r ...)`. Membership compiled. |
| ℕ codomain | Parent monomial interface fixed | General `Finset.Iic f` on a locally finite ordered Finsupp codomain already exists; changing the polynomial exponent type is not a literal weakening of this project interface. |
| No positivity/nonempty assumptions | Correct | Zero coordinates and empty σ remain valid; adding positivity would narrow the object. |

The current declaration is STRICTLY NARROWER than existing interval API. Verified `[Finite]` and classical removals are valid local improvements, but do not imply YES when the general object is already mathlib. An unrestricted infinite variable type with constant bound1 cannot give a Finset: compiled counterexample injects every `Finsupp.single n 1` into it. Finite support, rather than no condition at all, is the meaningful expansion. The project already uses this expanded representation at MainLemma:282–323.

## Phase 4c — all nine modern-idiom rows

| # | Applies? | Analysis and concrete downstream consequence |
|---|---|---|
| 1 typeclasses | yes | Fintype may become Finite with classical enumeration; finite-support bounds permit arbitrary ambient types. Existing interval instances provide finiteness directly. |
| 2 filters/topology | no | This is a finite combinatorial set, with no limits, metrics or neighborhoods. |
| 3 universal characterization | yes | Membership `d ≤ bound` canonically characterizes `Iic`; use existing interval rather than constructing/enumerating another object. `Finset.mem_Iic` applies immediately. |
| 4 bundled substructure | no | A box is not closed under addition: bounded coordinates need not remain bounded after addition. A submonoid would change content. |
| 5 algebraic hierarchy | no literal weakening | No scalar structure occurs; natural monomial exponents are fixed by MvPolynomial. The independent abstract order interface already exists. |
| 6 higher categories | no | A finite subset gains no useful higher-category API from the preorder interpretation. |
| 7 ordered indices | yes | `Finset.Iic f` is general over locally finite orders and Finsupp bounds; enables `mem_Iic`, interval inclusion and `Finsupp.card_Iic`. |
| 8 concrete-via-abstract | yes | [Executed source diagnostic](../evidence/Roth.box/q8-diagnostic.json): body has zero Roth-specific identifiers; only product/map/equivalence. The abstract interval object is already mathlib, and MainLemma actually uses it. |
| 9 false-generalization guard | passes with finite support | Preserve pointwise order, zero lower bound and finite support. Lexicographic order, unrestricted infinite constant bounds, real boxes, and submonoids are rejected as different/nonfinite objects. The infinite-bound rejection was compiled. |

Modern idiom: use `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` for finite coordinates, or `Finset.Iic f` when the bound is already a Finsupp. This removes redundant box API and composes with interval finiteness/cardinality. Cost is CHEAP for membership, MODERATE for coordinated consumer normalization; cost is not the verdict reason.

## Phase 4.5 — all six infrastructure risks

| Risk | Verdict | Checked rationale |
|---|---|---|
| Typeclass diamond | none | No instances are installed by box. Native synth checks select existing Finsupp LocallyFiniteOrder, its bottom interval instance and DecidableEq. |
| Reducibility leak | low | Ordinary noncomputable def, no reducible attribute; exact body comparison is rfl. Enumeration may unfold explicitly but is not a new reduction rule globally. |
| Noncanonical unfolding | low | Body uses piFinset/map while order-normal form is Iic; equality is propositional, not asserted definitional. CoeffNorm:216 deliberately unfolds the former and needs coordinated adaptation if representation changes. |
| Instance priority collision | none | A value definition has no priority or instance candidate. Existing instances are used without defining alternatives. |
| Universe polymorphism | none | Native full type has arbitrary Type u; an actual Type1 comparison compiled. |
| Coercion ambiguity | none | No new CoeFun/CoeSort declaration. Existing Finsupp evaluation and Finset→Set membership compiled. |

Overall LOW; no HIGH rows. Reuse existing Iic avoids a second interval representation. Read-only native probes are indexed in verification.json.

## Phase 4.6 — all five proof-strategy rows

| Row | Applies? | Finding |
|---|---|---|
| ε–δ versus filters | no | No topology or theorem proof. |
| Elements versus substructures | no | This is not a substructure; interval order characterization is the useful abstraction. |
| Sequences versus nets | no | No convergence. |
| Explicit object versus universal property | yes | Replace a new enumeration with existing interval object; membership characterizes it. |
| Missing helper API | no established gap | Existing interval/product/Finsupp APIs suffice for the construction. Sum-product conversion was tested; any useful generic rewrite lemma deserves separate assessment, not a new box definition. |

REFACTOR-RECOMMENDED: standard interval notation locally; no new helper is counted as an existing mathlib replacement.

## Phase 5 — all five actual methods on three forms

| Method | Current finite multi-index box | Standard Cartesian interval product | Abstract locally finite Finsupp interval |
|---|---|---|---|
| Lean-Finder | [receipt](../evidence/Roth.box/finder-current.json): Behrend analogue, not exact variable-bound Finsupp replacement | [receipt](../evidence/Roth.box/finder-standard.json): Pi interval-cardinality APIs | [receipt](../evidence/Roth.box/finder-abstract.json): Finsupp.card_Iic, DFinsupp analogue |
| Loogle | [receipt](../evidence/Roth.box/loogle-current.json): Fintype.piFinset | [receipt](../evidence/Roth.box/loogle-standard.json): finite interval-cardinality primitives | [receipt](../evidence/Roth.box/loogle-abstract.json): Finsupp.card_Iic |
| LeanSearch | [receipt](../evidence/Roth.box/leansearch-current.json): Behrend.mem_box/finite-degree analogue; real BoxIntegral hits rejected | [receipt](../evidence/Roth.box/leansearch-standard.json): Pi.card_Icc/Pi.card_Iic | [receipt](../evidence/Roth.box/leansearch-abstract.json): Finsupp.instLocallyFiniteOrder |
| rg pinned source | [receipt](../evidence/Roth.box/rg-current.txt): piFinset, equivFunOnFinite | [receipt](../evidence/Roth.box/rg-standard.txt): Pi interval source | [receipt](../evidence/Roth.box/rg-abstract.txt): Finsupp interval instance/card_Iic |
| Local name search | [receipt](../evidence/Roth.box/local_search-current.json): exact local Roth.box plus unrelated bare names | [receipt](../evidence/Roth.box/local_search-standard.json): piFinset declarations | [receipt](../evidence/Roth.box/local_search-abstract.json): Finsupp.card_Iic |

Local index reports **unavailable** even when source fallback finds names; it proves no absence. External indexes may differ from the pin: Finder's CanonicallyOrderedAdd signature is not substituted for pinned IsBotZeroClass. Root's native checks establish actual pinned signatures and constructions. [Untruncated full qualified source search](../evidence/Roth.box/full-name-source-search.json) finds no `Roth.box` in mathlib, without confusing Behrend.box/Finset.box/BoxIntegral.Box.

Positive pinned building blocks: `Finset.Iic`, `Finset.mem_Iic`, `Finsupp.instLocallyFiniteOrder`, `Finsupp.equivFunOnFinite`, `Finsupp.ofSupportFinite`, `Finsupp.le_def`, `Finsupp.card_Iic`, `Finsupp.prod_fintype`, `Nat.card_Iic`; original implementation uses `Fintype.piFinset`, `Finset.range`, `Finset.map`, `Equiv.toEmbedding`. See [Finsupp interval source](../evidence/Roth.box/Finsupp-Interval-source.lean.txt), [Pi intervals](../evidence/Roth.box/Pi-Interval-source.lean.txt).

## Phase 5.5 — statement shape

Normal forms compared: mapped piFinset, `Iic bound`, `Icc 0 bound`, set `{d | ∀ j, d j ≤ r j}`, subtype of bounded functions. The canonical library object is `Iic`; membership normalizes to `d ≤ bound` and then coordinatewise bounds. A migration equality should put Iic on its RHS. This is a data definition, so the RHS convention is an equality direction, not an iff orientation.

Syntactic generality: retain function-valued r for present polynomial call sites, or accept an existing Finsupp bound for arbitrary variables. No extra bundle is needed for callers to supply ordinary r. Fintype and DecidableEq are mechanically weakenable as verified above; r and σ remain essential. Overall RESTATE-BEFORE-SHIP / use existing object, not a new upstream def.

## Phase 6.0 — complete explicit callers and inline audit

[Untruncated caller receipt](../evidence/Roth.box/callers.txt) includes direct box references and mem/card consumers. [Structured direct occurrences](../evidence/Roth.box/explicit-callers.json) records 22 code lines outside Box across five files. Counts are source lines, not kernel/simp closure, and not counts of transitive theorem users.

| Source lines | Every direct refactor plan |
|---|---|
| Box47,51–52,57–58,68 | Replace definition by interval at use sites; membership uses mem_Iic + le_def; cardinality uses card_Iic/prod_fintype/Nat.card_Iic; subset-card bound supplies mem_Iic. Theorems are assessed separately in declaration order. |
| Lattice102,104,132–133,144,148,151,159,162,168,170,177,203 | Replace each box domain by Iic of converted r, including r∘Fin.castSucc. Filters and card/sum-fibre infrastructure keep the same type. Membership normalization at109,117,124,138 uses mem_Iic/le_def; cardinal step163 uses the existing interval-cardinality composition. No one-line claim about the whole fibre proof. |
| CoeffNorm215–216,234 (membership236) | Replace both summation domains by Iic. The only external explicit body unfold is216; sum/product conversion must use the verified equality or direct mapped piFinset normalization, preserving the product-of-sums argument. Support inclusion uses mem_Iic. |
| Taylor199–200,219 (membership206) | Replace each finite expansion domain by Iic; e outside domain still yields a coordinate violating bound via le_def. Evaluation and monomial proofs otherwise carry unchanged mathematical content. |
| Main392 (nonempty404, cardinal405) | Iic contains0 by bot_le; constant-sum cardinality reduces by card_Iic/product conversion. Same strict finite-sum argument. |
| MainLemma570,608 (membership616) | Replace filtered box domains by Iic; selected J membership becomes mem_Iic. Existing cardinal-filter estimate carries through coordinated statement changes. |

Inline mathematical duplication: **MainLemma282–323** already builds the exponent domain as `Iic (Finsupp.ofSupportFinite r ...)` with finite support of r, and computes its cardinality via `Finsupp.card_Iic`. It is a stronger ambient-index implementation of the same box. This is not a second Roth.box caller and is not silently counted as one. No external downstream repository was provided or searched; no external-consumer absence claim is made.

## Phase 6 — actual composition experiments

For a definition the replacement is the value term itself:

```lean
Finset.Iic (Finsupp.equivFunOnFinite.symm r)
```

It contains the canonical lower interval and the already-existing finite-function/Finsupp conversion: ≤3 existing operations, no project helper. With a Finsupp bound f it is just `Finset.Iic f`; with finitely supported ordinary r use `Iic (Finsupp.ofSupportFinite r ...)`.

Native root experiments verified (1) rfl exact original expansion; (2) equality to interval using Finset.ext/mem_Iic/le_def; (3) interval cardinality using Finsupp.card_Iic and prod_fintype; (4) DecidableEq-free and Finite-only definitions equal original; (5) arbitrary ambient finite-support bound membership; (6) impossibility of unrestricted infinite constant bound; (7) actual sum/product normalization and coercion/universe/instance probes. The independent mathlib-only probe checks target absence, so imported own/downstream membership lemmas cannot conceal circularity. The consumer experiment verifies the structural sum/product normalizer matching CoeffNorm:216; it is not a rebuilt migration of CoeffNorm or the entire downstream source tree. Caller refactors are concrete plans, not claims that production was changed or rebuilt.

Phase6b distinction: the comparison equality and sum-product normalization contain simp/ext reasoning. Those are not advertised as ≤3-call theorem proofs or a verdict on any future interval bridge theorem. The NO verdict concerns this data definition: its replacement is an already-existing two-operation value, independently shown to have exactly the intended elements. No newly proved helper is included in the count. The original mapped product can also be inlined verbatim where definitional expansion is wanted. This is composability with verified representation normalization, not an unsupported absence assertion.

## Phases 7–8 — actionable verdict

**NO-composable-from-mathlib**. Do not upstream Roth.box as a second finite-interval definition. Prefer `Finset.Iic` with an existing Finsupp bound, converting r only at the boundary. The construction has genuine local consumers, so it is useful local notation rather than dead code/junk. If a migration is deferred, retain the semantic wrapper in `Roth/Box.lean` as project-local API; no separate Archive or satellite contribution is needed. Consider removing the public DecidableEq requirement independently, with a coordinated classical implementation. Do not change pins or production in this read-only assessment.

No new upstream file/PR/reviewer is proposed for a NO verdict. Earlier accepted YES Hasse declarations do not turn this already-existing interval construction into another item for their PR. All required phases are complete; unresolved verification items are empty. Limitations are precise: optional ChatGPT MCP unavailable, local index unavailable, nLab direct XHTML fetch failed, explicit nCatLab namespace inaccessible, recent arXiv hit unrelated. None is used as evidence of absence.
