# Roth.mem_box — NO-composable-from-mathlib

Full independent assessment, canonical declaration 28, `Roth/Box.lean:51`. Root acceptance pending; production untouched.

## Phase 0 — baseline

All 17 current source/pin SHA256 values freshly matched the shared baseline manifest. The reusable `lake build` exited 0, 2467 jobs. [Manifest](../evidence/Roth.mem_box/input-manifest.json), [baseline](../evidence/Roth.mem_box/baseline-build.txt), [additional source hashes](../evidence/Roth.mem_box/source-hashes.json).

## Phase 1 — comprehension

`{σ : Type u} [Fintype σ] [DecidableEq σ] {r : σ → ℕ} {d : σ →₀ ℕ}`: `d ∈ Roth.box r ↔ ∀ j, d j ≤ r j`. No positivity or nonempty-index assumption. `box` maps the Cartesian product of `range (r j + 1)` through the inverse finite-function equivalence. Membership transports across that equivalence, is coordinatewise membership in each range, then becomes the weak natural-number bound. Original proof: `simp [box, Nat.lt_succ_iff]`. The native replay shows `Nat.lt_succ_iff` redundant under the current simp set. [Declaring module](../evidence/Roth.mem_box/Roth-Box.lean.txt), [native exact source](../evidence/Roth.mem_box/project-executed.lean.txt), [native receipt](../evidence/Roth.mem_box/native-project.json).

## Phase 2 — size and one-line check

SMALL: elementary characterization, not a main named theorem. Definition-only one-line test n/a: theorem, not a definition/class/instance. Small size does not skip literature, generality, or actual composition checks.

## Phase 3 — exhaustive literature

All required channels were freshly attempted. [Channel table and concise original summaries](../evidence/Roth.mem_box/literature-summary.json). Exact requests and response SHA256/bytes/status, with source locators only, are retained in [web0](../evidence/Roth.mem_box/web-0.json), [web1](../evidence/Roth.mem_box/web-1.json), [web2](../evidence/Roth.mem_box/web-2.json), [web3](../evidence/Roth.mem_box/web-3.json), [web4](../evidence/Roth.mem_box/web-4.json), [web5](../evidence/Roth.mem_box/web-5.json), [web6](../evidence/Roth.mem_box/web-6.json), [web7](../evidence/Roth.mem_box/web-7.json), [web8](../evidence/Roth.mem_box/web-8.json), [web9](../evidence/Roth.mem_box/web-9.json). No article/search-result bodies archived.

| Channel | Actual result |
|---|---|
| General web ≥3 distinct queries | Finite Cartesian product/order interval/multi-index box; multiindex polynomial coordinate order; arbitrary-family Cartesian membership. Standard coordinatewise criterion. |
| Optional ask_chatgpt_math | unavailable tool, n/a |
| Local clean.tex | §6 `roth:lem8`, lines1050–1074: integer tuples with coordinate bounds; [excerpt](../evidence/Roth.mem_box/local-reference.txt). |
| nLab | Partial-order page search exposes interval definition; direct open400 unsupported XHTML. |
| nCatLab | Distinct explicit namespace searched/opened; inaccessible, honestly retained. |
| Stacks | Product-set query attempted; opened tag0005 is categories and irrelevant. No false supporting attribution. |
| MathOverflow | Helfgott, oblong box question2020, displayed product of intervals; counting is substantially stronger than membership. |
| Recent arXiv within five years | Date-specific2022–2026 and2023/2024 queries attempted.2015 approximation excluded;2024 quantum-circuit hit irrelevant; precise final query empty. |

Primary educational source locator from general search: Binghamton, Definition5.5, Cartesian product of a family; domain-theory source Abramsky–Jung Definition3.2.1 uses coordinatewise order. No separate conventional theorem name is needed: this is product membership. Most general standard form is membership in an indexed product of sets, or membership in a lower interval of a pointwise order. Natural nonnegativity is implicit. Positivity and `m≥1` in the Roth count concern its inequality and do not restrict this membership statement.

## Phase 4a/4b — parameters and verified generality

| Parameter | Current need | Broader form and finding |
|---|---|---|
| `σ : Type*` | universe-polymorphic already | No imposed fixed universe. |
| `[Fintype σ]` | fixed `box` interface enumerates all coordinates | Reaim interval form works with `[Finite σ]`; native verified. Removing finiteness while keeping an unrestricted function bound would be false in general. |
| `[DecidableEq σ]` | fixed `box` interface | Classical construction can hide it; direct generic Finsupp lower-interval form supports arbitrary ambient indices with a finitely supported bound. This requires reaiming the parent, not merely deleting an argument of the current theorem. |
| `r : σ → ℕ` | coordinate upper bounds | Arbitrary finitely supported bound works on infinite ambient indices. Arbitrary unrestricted infinite positive bound does not produce a finite box. |
| `d : σ →₀ ℕ` | monomial exponents | Already arbitrary, including zero. |
| `ℕ` | concrete exponent order | Existing generic `Finset.mem_Iic` requires `LocallyFiniteOrderBot` (finite lower intervals; `LocallyFiniteOrder` plus a bottom is not being assumed sufficient), and `Finsupp.le_def` any `Zero` and `LE` codomain for pointwise inequality. No new generic API warranted. |
| strict/positive assumptions | none | No extra weakening to claim. |

Current statement is maximally general relative to its fixed project parent interface. Expanded representation is strictly narrower than existing generic interval API; verified reaim does not justify YES-generalise because that API already exists. Reaim:

```lean
d ∈ Finset.Iic (Finsupp.equivFunOnFinite.symm r) ↔ ∀ j, d j ≤ r j :=
  Finset.mem_Iic.trans Finsupp.le_def
```

## Phase 4c — all modern-idiom rows

| # | Diagnostic | Finding / consequence |
|---|---|---|
|1|Typeclasses|Already uses Fintype/DecidableEq; use existing LocallyFiniteOrderBot interval API on reaim.|
|2|Filters/nets|No: finite membership has no topology.|
|3|Universal property|No new construction needed; existing product and equivalence suffice.|
|4|Bundled substructures|No closure predicate; lower interval is an existing Finset, not a submodule.|
|5|Algebra hierarchy|No field/vector-space hypotheses to weaken.|
|6|Higher categories|No: set membership has no higher-categorical obstruction.|
|7|Concrete ℕ index/codomain|Yes, generic ordered interval is broader and already present; enables Finset interval/card/order infrastructure.|
|8|Concrete-via-abstract|Fires: one occurrence of `box` in proof, zero after unfolding. [Diagnostic](../evidence/Roth.mem_box/q8-diagnostic.json). Abstract membership is `Finset.mem_Iic` plus pointwise order, already present.|
|9|False-generalisation guard|Interval reaim preserves exactly the bounds. Infinite ambient unrestricted bound is rejected; infinite independent unit vectors violate finiteness. Finitely supported bounds preserve meaning.|

Modern idiom available: existing lower interval. Concrete improvement: direct membership/order API, cardinality via `Finsupp.card_Iic`, and arbitrary finite-support ambient indexing. No new abstraction is missing.

## Phase 4.5 — infrastructure

n/a — theorem introduces no definitional equality, instance, or coercion. Each of the six risk rows (typeclass diamonds, reducibility leak, noncanonical unfolding, instance priorities, universe polymorphism, coercion ambiguity) is n/a for this declaration. Parent construction risks belong to the independent `Roth.box` assessment and are not inherited as this theorem's risks.

## Phase 4.6 — all proof-strategy rows

| # | Strategy question | Finding |
|---|---|---|
|1|Topology ε–δ versus filters|No topology.|
|2|Algebra elements versus bundled inclusion|No algebraic closure argument; pointwise order is definitionally the right criterion.|
|3|Analysis sequences versus nets|No limit.|
|4|Category construction versus universal property|No category-theoretic construction.|
|5|Needed missing helpers|None: three membership facts prove the original target directly.|

MATHLIB-IDIOMATIC. Original simp is natural for a local API lemma; strict existing-fact term is better evidence for duplicate screening. No new helper is smuggled into the replacement.

## Phase 5 — actual five-method × three-form search

Actual Finder, Loogle, LeanSearch, source rg, and local-name queries ran on current box form, standard Cartesian-product form, and abstract lower-interval form. Each remote response is retained complete; local-index unavailability is recorded alongside its source fallback hits and never treated as absence. Remote revision may differ from pins; native checks supply pinned authority.

| Method | Current | Standard | Abstract |
|---|---|---|---|
|Finder|Behrend.mem_box (different parent/uniform Fin n box)|BoxIntegral.mem_def (real intervals, different type)|Finset.mem_Iic exact generic building block|
|Loogle|Finsupp.le_def|Fintype.mem_piFinset|Finset.mem_Iic|
|LeanSearch|Behrend.mem_box, no exact project parent|product/box candidates|Finset.mem_Iic|
|rg|mem_map_equiv; no qualified Roth.mem_box declaration|mem_piFinset, mem_range_succ_iff|mem_Iic, le_def|
|local names|mem_box family, including own target excluded|mem_piFinset family|mem_Iic variants; index unavailable|

Receipts follow `finder-{current,standard,abstract}.json`, `loogle-*`, `leansearch-*`, `local_search-*`, and `rg-*.json` in evidence. [Example Finder](../evidence/Roth.mem_box/finder-abstract.json), [Loogle](../evidence/Roth.mem_box/loogle-standard.json), [LeanSearch](../evidence/Roth.mem_box/leansearch-abstract.json), [local](../evidence/Roth.mem_box/local_search-current.json), [rg](../evidence/Roth.mem_box/rg-standard.json), [untruncated full-name search](../evidence/Roth.mem_box/full-name-source-search.json). Behrend.mem_box is not a direct replacement: uniform strict bounds and ordinary functions differ. Positive pinned candidates are native checked; no absence assertion depends on search failure.

## Phase 5.5 — all statement-shape checks

Normal form: `d ≤ bound` is canonical pointwise order, native `pointwise` succeeds. Coordinate inequalities remain useful when applying degree bounds. Syntactic-generality attempt: negative membership gives an existential violating coordinate; native `negative` succeeds and matches Taylor206. Superfluous-argument audit: Fintype/DecidableEq are tied to the current parent signature; interval reaim weakens finiteness but is a parent migration, not an unused theorem binder. Verdict KEEP-CURRENT-SHAPE for local parent API, prefer existing interval on a coordinated parent migration.

## Phase 6.0 — callers and inline audit

Nine explicit source lines in seven declaration callers; eight external occurrences in five files, one same-module use. [Exact source references](../evidence/Roth.mem_box/explicit-callers.json), [raw identifier grep](../evidence/Roth.mem_box/callers.txt). This is source-level reference accounting, not opaque kernel/simp dependency closure. The target is not tagged simp; explicit simp lists explain its uses.

| Caller | Lines | Mechanical plan after deleting mem_box |
|---|---|---|
|Roth.card_le_card_box|Box68|Replace `mem_box.2` with the strict three-fact iff's `.mpr`; retain card/trans chain.|
|private card_filter_box_fiber_aux|Lattice109,117,124|Replace explicit membership simp entry by `box`; use mapped-product/range membership simplifiers (add `Nat.lt_succ_iff` if needed), preserving filter/extension proof. Alternatively coordinate interval migration uses mem_Iic/Finsupp.le_def.|
|Roth.card_filter_box_last|Lattice138|Expand `box` membership at hd, preserve coe_filter and coordinate projection.|
|Roth.abs_eval_le|CoeffNorm236|Replace `mem_box.2` by strict iff `.mpr`; its argument remains `(monomial_le_degreeOf j hk).trans (hP j)`. Native degree_support_consumer checks precisely that type flow.|
|MvPolynomial.eq_sum_box_hasseDeriv|Taylor206|Replace `[Roth.mem_box]` with `[Roth.box]`; negative-form native verifies the bound negation/existential conversion.|
|Roth.abs_eval_lt_of_le_index|Main404|Replace `mem_box.2 (fun j ↦ Nat.zero_le _)` by strict iff `.mpr`; zero index remains a witness.|
|private exists_mem_RSet_le_index_of_rpow_bound_aux|MainLemma616|Replace `mem_box.2 hd` by strict iff `.mpr hd` inside filter constructor.|

Inline-derivation audit searched the full module and callers: mapped-product simp at the definition and product-sum consumers are representational plumbing, not independent missing mathematical results. Native consumer probes verify raw and degree/negative types. These are reviewable refactor plans, not a rebuilt migration of all downstream files; no production edits were authorized for this worker.

## Phase 6 — composition, with Phase6b guard

Attempt1 `simp [Roth.box]` closes. Under Phase6b this alone is BORDERLINE (trivial simp composition), not an automatic NO. Reaim2 is `Finset.mem_Iic.trans Finsupp.le_def`, but proving equality with the original representation is separate and cannot be hidden as an existing fact.

Attempt3 independently succeeds on the ORIGINAL target:

```lean
Finset.mem_map_equiv.trans (Fintype.mem_piFinset.trans
  (forall_congr' fun _ ↦ Finset.mem_range_succ_iff))
```

Exactly three existing mathlib membership facts: `Finset.mem_map_equiv` (Mathlib/Data/Finset/Image.lean), `Fintype.mem_piFinset` (Mathlib/Data/Fintype/Pi.lean:37), `Finset.mem_range_succ_iff` (Mathlib/Data/Finset/Range.lean). `Iff.trans` and `forall_congr'` are logical plumbing, not extra mathematical premises. Definitional unfolding of the fixed project parent is elaboration, not an invocation of a project lemma. No simp, new bridge, parent theorem, target theorem, or downstream result occurs in this term. Native project and isolated mathlib-only source-shaped reproduction both verify it. Conclusion COMPOSABLE under the strict three-fact criterion; Phase6b's mere-simp ambiguity is resolved by actual term evidence.

## Phase 7 — verdict and action

**NO-composable-from-mathlib.** Product membership, mapping by an equivalence, and bounded natural range membership already provide the exact original proposition in three calls. This conclusion does not inherit `Roth.box`'s verdict and does not rely on the lower-interval representation comparison. The three-fact term directly targets the source-shaped box.

Delete `Roth.mem_box` during the coordinated cleanup and apply the seven caller plans above; update all nine explicit sites. The alternative local destination is `Roth/Box.lean` if the project deliberately keeps its semantic membership interface for readable explicit simp lists. Such local convenience supplies no missing upstream mathematical API. Proposed upstream file, PR title/grouping, generalise/cleanup/reviewer checklist are n/a for NO. Existing generic interval membership already covers the abstract form.

## Phase 8 — handoff

All phases completed; no unresolved verification. [Verification sources and native receipts](../evidence/Roth.mem_box/verification.json), [assessment](../evidence/Roth.mem_box/assessment.json), [portable read-only validator](../evidence/Roth.mem_box/validate.py). Root independently reviews before publishing; no production edits, pin changes, or Git operations performed by this worker.
