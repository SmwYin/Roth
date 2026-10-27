# Full mathlibable assessment: `Roth.weight_nonneg`

Verdict: **NO-composable-from-mathlib**. This is an independent assessment of the theorem, not inheritance of the earlier verdict on `Roth.weight`. Its content is a finite sum of nonnegative quotients. Three distinct existing library facts suffice, with the universal natural-cast fact used at two coordinates. There are three explicit project references, so it is useful project API; that does not create a missing upstream theorem.

## Phase 0 — Baseline and scope

Canonical declaration 31, `Roth/Box.lean:75`, branch `ramin-cleanup`. All 17 production-source/pin SHA256 values freshly match the shared baseline manifest. The reusable baseline is `lake build`, exit 0, 2467 jobs. No production source, pin, or Git operation was performed by this worker. Read the complete declaring module and the caller modules `Index`, `Lattice`, and `Theta`.

Evidence: [fresh hashes](../evidence/Roth.weight_nonneg/source-pin-hashes.json), [baseline receipt](../evidence/Roth.weight_nonneg/baseline-build.txt), [full declaring source](../evidence/Roth.weight_nonneg/Box.lean.txt), [exact source searches](../evidence/Roth.weight_nonneg/source-search.json).

Applied the installed mathlib-quality skill and the complete `/mathlibable` command, with mathlib-search, mathlibable-verdicts, mathlib-review-stages, and generalisation-patterns references. All mandatory phases run; theorem-only exceptions are explicitly marked below.

## Phase 1 — Mathematical and elaborated statement

For any finite variable type, natural parameters `r`, and natural multi-index `d`, the real number `sum j, d j / r j` is nonnegative. No parameter positivity, nonzero denominator, membership in a box, polynomial, or nonzero multi-index is assumed. Lean defines division by zero as zero, so the statement includes zero coordinates of `r`.

The actual native full type is:

```lean
@Roth.weight_nonneg : ∀ {σ : Type u_2} [Fintype σ]
  (r : σ → ℕ) (d : σ →₀ ℕ), 0 ≤ Roth.weight r d
```

The ambient `DecidableEq σ` was already omitted before this declaration; it is absent from the elaborated type. `σ` is universe polymorphic, `Fintype σ` supplies the finite full-index sum, `r` supplies nonnegative denominators, and `d` supplies nonnegative numerators. The proof is mathematically: natural casts are nonnegative, their quotients are nonnegative, and a finite sum of them is nonnegative. Standard axioms only: `propext`, `Classical.choice`, `Quot.sound`.

Evidence: [verification map](../evidence/Roth.weight_nonneg/verification.json), [native target receipt](../evidence/Roth.weight_nonneg/native-target.json), [exact executed source](../evidence/Roth.weight_nonneg/target-executed.lean.txt).

## Phase 2 — Preliminary checks

**SMALL**: an elementary order helper, neither a new structure nor a named major theorem or listed module main result. Phase 2b one-line definition test: **n/a — theorem**, even though its proof is one line. No definition exemption is being used to justify it.

## Phase 3 — Exhaustive literature protocol

Every named protocol channel and three distinct general queries were checked. Exact requests, SHA256/byte counts of returned responses, statuses, and source titles/URLs are retained, without article or search-result bodies: [search metadata](../evidence/Roth.weight_nonneg/literature-search.json), [direct opening metadata](../evidence/Roth.weight_nonneg/literature-open.json), [recent-paper metadata](../evidence/Roth.weight_nonneg/literature-recent.json).

| Channel | Actual query / examination | Result and limitation |
|---|---|---|
| General web: specific | `Roth theorem index polynomial weight sum i_j r_j nonnegative` | Soundararajan/Petrow lecture notes, Definition 1, printed p.56, PDF p.55: index uses this weighted sum. Also Min Ru's Roth notes and the Uppsala thesis §4. |
| General web: general | `finite sum nonnegative elements ordered additive commutative monoid nonnegative weights` | Mathlib order-big-operator documentation identifies the general finite-sum order statement. Search hit is discovery evidence; pinned native signatures settle usability. |
| General web: alias | `weighted degree multiindex nonnegative weights polynomial index Roth lemma` | Weighted degree terminology; MIT algebraic geometry notes §1.7.8 as a primary educational source, alongside secondary MathWorld discovery. |
| ChatGPT mathematical MCP | Standard form, generality, historical formulation channel | n/a: `ask_chatgpt_math` is unavailable; no fabricated query or expert opinion. |
| Local reference | `clean.tex` §4, lines 530–567 | Allows positive real parameters; explicitly derives index nonnegativity from nonnegative weights. |
| nLab | `site.ncatlab.org nLab ordered commutative monoid positive cone` | Positive cone / ordered-group previews; direct positive-cone page returns 400 unsupported `application/xhtml+xml`. Preview-only adjacent evidence, not verified full-page theorem. |
| nCatLab | `site:ncatlab.org weighted degree polynomial monoid` | Degree-of-polynomial preview, no categorical reformulation needed. Direct page fails with the same XHTML limitation. |
| Stacks | `site:stacks.math.columbia.edu graded polynomial weighted degree nonnegative` | Opened Tag 053C, Lemma 15.26.3: positive variable degrees in graded polynomial algebras. Adjacent grading usage, no separate Roth-weight nonnegativity result. |
| MathOverflow | `site:mathoverflow.net Roth theorem polynomial index weights` | Opened question 64709: polynomial Diophantine approximation, not the finite weight lemma. No replacement or stronger theorem inferred. |
| Recent arXiv, five years | `site:arxiv.org Roth theorem index polynomial weighted degree 2021 2022 2023 2024 2025 2026` | Salami, arXiv:2610.17589v1, submitted 13 Oct 2026, §8 lines 658–675: weighted index and failure of a naive degree-box rescaling. This concerns auxiliary-polynomial degree bounds, and does not dispute nonnegativity of each weighted sum. Older search hits are not counted as recent. |

Primary locators: [Soundararajan/Petrow](https://math.stanford.edu/~ksound/TransNotes.pdf), [Min Ru](https://www.math.uh.edu/~minru/fields/roth.pdf), [MIT notes](https://math.mit.edu/classes/18.721/ag-nov25-2020.pdf), [Stacks 053C](https://stacks.math.columbia.edu/tag/053C), [MathOverflow examination](https://mathoverflow.net/questions/64709/diophantine-approximation), [Salami §8](https://arxiv.org/html/2610.17589v1).

Literature synthesis: this is nonnegativity of a monomial's weighted degree / Roth index weight. The immediate mathematical standard is a finite sum of nonnegative terms. Reciprocal parameters are a particular choice of nonnegative weights. Classical Roth definitions often use positive real parameters, whereas this Lean theorem uses natural parameters including zero. Thus neither blanket 'more general' nor blanket 'less general' compares the parameter domains: positive nonintegral parameters expand one direction, Lean's totalized zero-denominator convention expands another. No literature channel supplies a distinct deep theorem here; no failed search establishes absence.

## Phase 4a–4b — Parameters and actual generality

| Parameter / hypothesis | Role and attempted broader form | Assessment |
|---|---|---|
| `σ : Type*` | Arbitrary universe and arbitrary variable names already allowed. | No finite ordinal or universe restriction to remove. |
| `[Fintype σ]` | Required by the fixed parent `Roth.weight` full-index sum. | Not mechanically removable while keeping that parent signature. Arbitrary ambient types work with support sums / `Finsupp.weight`; verified as expanded representation. |
| `(r : σ → ℕ)` | Cast gives denominator nonnegativity, with zeros allowed. | Expanded finite-sum statement permits real nonnegative denominators. Positivity is not required. Unrestricted signed denominators are false. |
| `(d : σ →₀ ℕ)` | Supplies natural numerator values; finite support is not needed on finite σ. | Ordinary function families over finite sets verified. Changing the fixed parent domain is representation refactoring, not dropping an unused original binder. |
| result in `ℝ` | Only ordered arithmetic is used. | Expanded quotient proof verified for a general ordered field; abstract `Finsupp.weight` proof uses ordered additive monoids. No claim that `Roth.weight` itself has a field parameter. |
| positivity / nonzero premises | None exist in actual target. | Nothing to drop; zero parameters explicitly compile to weight zero. |
| `[DecidableEq σ]` | Absent from actual target. | Already absent; do not count it as newly weakened. |

Generality verdict: **MAXIMALLY GENERAL within the fixed `Roth.weight` interface**, with independently verified broader representations. The result is not routed to `YES-but-generalise-first`: broad finite-sum positivity is already supplied by mathlib, and an unrestricted-denominator broadening changes a true statement into a false one. Accepted exact probes and all claimed representation extensions are mapped in [verification](../evidence/Roth.weight_nonneg/verification.json).

## Phase 4c — All nine modern-idiom rows

| # | Question | Answer, concrete consequence |
|---|---|---|
| 1 | Typeclasses / instances? | No new instance needed; `Fintype` and order classes already carry the relevant structure. A proposition about this function should not be a global instance. |
| 2 | Filters instead of sequences / metrics? | No: finite order arithmetic has no convergence notion. |
| 3 | Universal property instead of construction? | No object is constructed by this theorem. |
| 4 | Bundled substructure? | Nonnegative reals could bundle the image, but changing the parent codomain would alter downstream infimum/arithmetic interfaces; no benefit to this proof alone. |
| 5 | Field / module hierarchy? | Yes at expanded representation level: sum nonnegativity in ordered additive monoids and natural scalar positivity avoid the real-specific arithmetic. Existing sum and scalar-order API supplies it. |
| 6 | Higher categories? | No categorical data, morphisms, or coherence involved. |
| 7 | Concrete index / scalar type? | Variable index type is already arbitrary. Real target can be replaced in the explicit formula by an ordered field; verified. This permits rational versions without a new lemma. |
| 8 | Concrete-via-abstract diagnostic? | Fires: `weight` appears in zero proof-body lines; the sole line is `Fintype.sum_nonneg` plus `positivity`. After reduction it uses only summand nonnegativity. The abstract result is existing `Finset.sum_nonneg`; on finite support use existing `Finsupp.sum_nonneg'` plus `nsmul_nonneg`. |
| 9 | False-generalisation guard? | Reject arbitrary signed denominators / negative weights. Preserve nonnegative hypotheses in real and abstract versions. Support sums coincide with full sums because omitted terms are zero; changing the sum to an arbitrary infinite series would require a separate summability analysis and is not claimed. |

Modern idiom available: **yes, already existing finite-sum / Finsupp API**, not a new upstream gap. It reuses ordered sums, natural scalar actions, arbitrary ambient variable types, and `Finsupp.weight`'s additive-map interface. No cost-based verdict argument is used.

## Phase 4.5 — Infrastructure risk

**n/a — theorem.** It adds no definition, typeclass instance, coercion, reducibility path, universe construction, or instance priority. The six definition-only risk rows are therefore inapplicable; the parent definition's separate assessment is not inherited.

## Phase 4.6 — All five proof-strategy rows

| # | Question | Outcome |
|---|---|---|
| 1 | Topology / epsilon-delta versus filters | n/a: no topology. |
| 2 | Algebra elements versus substructure inclusion | No inclusion argument exists; summand positivity is the natural abstraction. |
| 3 | Sequences versus nets | n/a: finite sum, no limits. |
| 4 | Construction versus universal property | n/a: theorem proves an inequality. |
| 5 | Missing helper mathlib should have | No necessary missing helper: finite-sum positivity, natural-cast positivity and quotient positivity suffice. A convenience `Finsupp.weight_nonneg` name was not found, but its abstract proof also composes from existing sum/scalar facts. No absence claim is made. |

Strategy verdict: **MATHLIB-IDIOMATIC**. The original sum-nonnegative plus positivity proof is mathematically optimal. An explicit three-fact proof is useful assessment evidence, not an assertion that source automation is defective.

## Phase 5 — Actual five-method search on three forms

Forms: current = natural ratios / `Roth.weight`; standard = nonnegative finite weighted sums; abstract = `Finsupp.weight` and ordered finite-support sums. [Raw tool requests/results](../evidence/Roth.weight_nonneg/formal-search.json), [rg requests/results](../evidence/Roth.weight_nonneg/source-search.json), [untruncated qualified-name search](../evidence/Roth.weight_nonneg/full-name-source-search.json).

| Method | Current | Literature-standard | Abstract |
|---|---|---|---|
| Lean-Finder | Natural-ratio sum query: `Finsupp.sum_nonneg'` plus unrelated analytic hits. | Weighted finite nonnegative sum query: `Fintype.sum_nonneg`, `Finsupp.sum_nonneg'`. | Finsupp natural weights query: `le_weight_of_ne_zero`, `le_weight_of_ne_zero'`, `weight_eq_zero_iff_eq_zero`; they need extra premises or different targets. |
| Loogle | `Real, 0 ≤ ∑ _, (_ : ℝ) / _`: empty. | `Finset.sum, 0 ≤ _`: `Finset.sum_nonneg`, `sum_nonneg'`. | `Finsupp.sum, 0 ≤ _`: `Finsupp.sum_nonneg`, `sum_nonneg'`. |
| LeanSearch | Natural ratios nonnegative query: cast / rational positivity and near misses. | Finite sum nonnegative real numbers: `Fintype.sum_nonneg`, `Finset.sum_nonneg`, `finsum_nonneg`. | Ordered finitely supported nonnegative terms: `Finsupp.sum_nonneg'`. |
| rg pinned source | Exact qualified target absent; weight/nonneg search in Finsupp files yields no standalone weight theorem. | Sum API in `Algebra/Order/BigOperators/Group/Finset.lean` includes generated additive declarations. | `Data/Finsupp/Order.lean:56–58` sum positivity; full `Weight.lean` examined. |
| Local name search | `weight_nonneg`: project theorem and unrelated `Quiver.Path.weight_nonneg`. | `sum_nonneg`: Finsupp and unrelated partition-of-unity hits. | `Finsupp.sum_nonneg`: both sum positivity lemmas. |

All local-name results explicitly report `index: unavailable`; their returned partial textual matches are useful discovery only. External search signatures sometimes use older order-class assumptions; actual pinned native elaboration is authoritative. No method's failure proves theorem absence. The concrete proof is verified positively rather than inferred from search silence.

Positive pinned building blocks: `Finset.sum_nonneg` (`Mathlib/Algebra/Order/BigOperators/Group/Finset.lean`, generated by `to_additive` near line 151); `div_nonneg` (`Mathlib/Algebra/Order/GroupWithZero/Basic.lean:878`); `Nat.cast_nonneg` (`Mathlib/Data/Nat/Cast/Order/Ring.lean:30`); abstract `Finsupp.sum_nonneg'` (`Mathlib/Data/Finsupp/Order.lean:58`), `nsmul_nonneg`, and `Finsupp.weight_apply` (`Mathlib/Data/Finsupp/Weight.lean:85`). Full pinned signatures and accepted proofs are in the native receipts.

## Phase 5.5 — All three statement-shape checks

1. **Normal form:** `0 ≤ weight r d` is conventional nonnegativity orientation; `weight r d ≥ 0` is notation for the same proposition. The sum-level normal form reduces definitionally, with no imported theorem about weight needed.
2. **Syntactic generality:** explicit `r d` is convenient at all three callers. Ordinary function families and finite sets expose the true arithmetic abstraction, verified independently. The abstract Finsupp form avoids ambient `Fintype`; it is a representation alternative, not deletion of a binder from the same expression.
3. **Superfluous arguments:** no extra positivity or decidability premises exist. Both `r` and `d` occur in the conclusion; `Fintype` belongs to the fixed full-sum definition. The only absent hypotheses are already absent, so no linter-inspired fictitious weakening is proposed.

Statement-shape verdict: **NORMAL-FORM; no required restatement to use this local theorem**. If contributing related material upstream, state it against generic existing sums / `Finsupp.weight`, not the project-specific wrapper.

## Phase 6.0 — Every explicit source caller and inline audit

| Caller | Occurrences | Use and mechanical refactor |
|---|---:|---|
| `Roth/Lattice.lean:145`, private `filter_weight_le_eq_empty` | 1 | In a `linarith` contradiction. Introduce the explicit sum-nonnegative proof as `hw`, then pass `hw` to `linarith` instead of `weight_nonneg r d`. |
| `Roth/Index.lean:94`, `index_nonneg` | 1 | Supplies image elements' lower bounds to `Real.sInf_nonneg`. Replace the inner lambda body by the explicit quotient-sum proof for that `d`. |
| `Roth/Theta.lean:395`, `sum_max_sub_le_index_det` | 1 | Chains `weight_nonneg (r ∘ some) (D μ)` through `h2` to obtain `0 ≤ δ`. Introduce `hw` with these instantiated parameters, then use `hw.trans h2` in the existing `add_nonneg` / `max_le` chain. |

**3 occurrences, 3 caller declarations, 3 external files**, excluding the definition. This is a source-reference inventory, not an opaque kernel dependency or simp closure. The theorem is not tagged simp. Its API value is real and is not classified as dead code.

Inline-derivation grep examined every `weight`, `sum_nonneg`, and `positivity` occurrence in Box/Index/Lattice/Theta, plus all project exact-name matches. `weight_eq_zero_iff` uses nonnegative summand hypotheses for a stronger zero-characterisation; `Lattice:183` proves one scalar summand nonnegative; neither is an additional explicit whole-weight nonnegativity call. No additional bypass proof of this exact complete sum was identified. Caller patterns with the replacement, including the actual sInf image shape and max/trans chain, are native-verified; see [verification](../evidence/Roth.weight_nonneg/verification.json).

## Phase 6 — Actual composition experiments and honest call count

Original-target replay and explicit composition both compile, without using `Roth.weight_nonneg` or any downstream weight theorem in their proof. The positive composition is:

```lean
example {σ : Type*} [Fintype σ] (r : σ → ℕ) (d : σ →₀ ℕ) :
    0 ≤ Roth.weight r d := by
  have hn : ∀ n : ℕ, (0 : ℝ) ≤ n := Nat.cast_nonneg
  exact Finset.sum_nonneg fun j _ ↦ div_nonneg (hn (d j)) (hn (r j))
```

There are exactly **three distinct existing library facts/references**: `Nat.cast_nonneg`, `Finset.sum_nonneg`, `div_nonneg`. The universally quantified existing cast theorem is bound once as `hn` without proving any new helper proposition. It is applied **twice** per coordinate, to `d j` and `r j`. Fully expanding the universal binding gives **four instantiated theorem applications** (one sum, one division, two casts), not three. The final term references each of the three library facts once and reuses the local theorem value. This is the concrete three-existing-fact composition supporting the verdict; there is no hidden parent-project lemma, new mathematical helper, or closing `simp [defs...]` argument. Ordinary definitional reduction of the finite sum in `Roth.weight` exposes the goal.

Phase6b's warning about a merely closing `simp [defs...]` does not apply to this explicit proof. The separately replayed original `Fintype.sum_nonneg` plus positivity proof is confirmation of the source strategy, not the sole composition evidence. Zero parameters are accepted without a positivity premise. All broader finite-family, ordered-field, real-nonnegative-denominator, arbitrary-ambient Finsupp, and negative-denominator guard experiments are documented with accepted sources/receipts in [verification](../evidence/Roth.weight_nonneg/verification.json).

Composition verdict: **COMPOSABLE**, with repeated-cast application accounting stated explicitly. The abstract Finsupp route is also composition, and does not imply a pre-existing named `Finsupp.weight_nonneg` theorem. Failed missing-import attempts are retained separately and excluded from accepted evidence.

## Phase 7 — Actionable verdict and gate

**NO-composable-from-mathlib.** Finite-sum nonnegativity, division nonnegativity, and the universal natural-cast nonnegativity theorem give the exact project statement. No project-dependent result is counted among these building blocks. This conclusion was reached from the positive proof and all searches, not from the earlier `Roth.weight` verdict. Modern abstraction strengthens the reason to use existing generic sum API rather than proposing a Roth-specific fact upstream.

For a refactor, remove this theorem only after replacing all three named callers according to Phase 6.0. At each caller, use the explicit proof above with the caller's `r` and `d`; the reused cast fact may be bound once in the surrounding proof. Native caller fragments establish the argument flow. This is a proposed subsequent source change; this assessment leaves production untouched. If preserving the readable project API is preferable, its appropriate alternative destination is **project-local `Roth/Box.lean`**, where its meaning and three uses belong. Neither Archive nor a separate satellite library is warranted for elementary arithmetic glue.

Gate: all phases complete; all named literature channels and at least three general queries executed; five actual mathlib methods across all three forms; nine modern rows; five strategy rows; three statement-shape rows; exact caller/inline audit; native positive composition and generality guards; no unsupported absence or cost argument. No unresolved verification or upstream design questions remain for this NO assessment. YES-specific PR path/title/reviewer/grouping requirements are n/a; already accepted YES entries were read from progress rather than inferred from names.

## Phase 8 — Handoff

The completed package includes [assessment](../evidence/Roth.weight_nonneg/assessment.json), [verification](../evidence/Roth.weight_nonneg/verification.json), [overview entry](../evidence/Roth.weight_nonneg/overview-entry.json), [current copy manifest](../evidence/Roth.weight_nonneg/copy-manifest.json), and [portable validator](../evidence/Roth.weight_nonneg/validate.py). Root acceptance remains pending until independent review. The validator checks current manifest bytes/hashes in scratch or integrated layout; any worker manifest retained later is historical only.
