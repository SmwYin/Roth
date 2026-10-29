# Roth.eventually_div_rpow_lt — canonical270

**Verdict: YES-but-generalise-first.** Contribute an eventual comparison of real powers, with an arbitrary positive right-hand constant and arbitrary real input tending to infinity. Retain the natural-number threshold as a corollary. This is a new proved API proposal, not a claim that a current mathlib theorem already supplies it. The exponent-gap comparison is reusable analysis; neither the importance of Roth's theorem nor the short arithmetic spelling determines this verdict.

## Phase0 — baseline and controls

Resolved public theorem at `Roth/Main.lean:103`. All17 production source/pin hashes freshly match the tracked shared manifest. Reuse the successful baseline `lake build` (2467 jobs); the previous file-boundary Theta build was accepted. No file-end build is due at270; next boundary289 remains root-owned. No production source, pin, Git, shared18 imports, or disk9 imports was changed by this worker. All native and local LSP work was executed by root; remote searches and preparation were worker-owned. See [inputs](../evidence/Roth.eventually_div_rpow_lt/inputs.json), [baseline](../evidence/Roth.eventually_div_rpow_lt/baseline-build.txt), [verification](../evidence/Roth.eventually_div_rpow_lt/verification.json).

The entire Main and LeanEval modules were read, including every actual caller. Original re-elaboration is **exact target only**, in `Decay270Original`, with only the theorem basename renamed to `replay` and `open Roth`; no private helper is needed by the target. Loaded public project ingredients remain imported. Native theorem equality checks type agreement through proof irrelevance, not proof construction identity. [Source reading](../evidence/Roth.eventually_div_rpow_lt/source-reading.json), [exact original execution](../evidence/Roth.eventually_div_rpow_lt/original-executed.lean.txt), [raw root receipt](../evidence/Roth.eventually_div_rpow_lt/original-receipt.json).

## Phase1 — mathematical content and kernel type

For any fixed real M and real exponents κ′<κ, the positive power q^(κ−κ′) eventually exceeds M. Therefore M/q^κ<1/q^κ′ beyond some natural threshold. M is already allowed to be zero or negative; neither exponent needs to be positive. Choosing the tail with Q<q ensures q>0 even when the extracted threshold is zero.

Full kernel type, obtained with `Lean.getConstInfo` and `pp.funBinderTypes`:

```lean
∀ {M κ κ' : ℝ}, κ' < κ → ∃ (Q₀ : ℕ), ∀ (q : ℕ),
  Q₀ < q → M / ↑q ^ κ < 1 / ↑q ^ κ'
```

M is the amplitude; κ and κ′ are decay/growth exponents. The only hypothesis is a strict exponent gap. The original proof uses `tendsto_rpow_atTop`, composition with natural casts, eventual domination, natural-tail extraction, positivity, and `Real.rpow_sub`. It has no project declaration dependencies in source, kernel type, kernel value, or transitive project closure. Full written proof and full elaborated type are retained. The raw `pp.all` kernel printer explicitly elides33987 characters: this is **not a complete kernel body dump**. [Native type](../evidence/Roth.eventually_div_rpow_lt/native-type.json), [dependencies](../evidence/Roth.eventually_div_rpow_lt/dependencies.json).

Exact canonical293 ordered/private-name audit:293 requested,293 unique,293 present,293 with values. Three direct value consumers, zero direct type consumers. The declaration is not in the simp set. The separate project type/value transitive traversal finds nine downstream consumers, including the private Main helper and final LeanEval theorem. Lexical occurrences, direct kernel dependencies, simp registration, and transitive closure are distinct scopes. [Direct audit](../evidence/Roth.eventually_div_rpow_lt/canonical-consumers.json), [scope execution](../evidence/Roth.eventually_div_rpow_lt/scope3-executed.lean.txt), [scope receipt](../evidence/Roth.eventually_div_rpow_lt/scope3-receipt.json).

## Phase2 — preliminary checks

SMALL: an analytic helper, neither a named main theorem nor a new structure. The definition-only one-line test is n/a because this is a theorem; no definition exemption is claimed. Three actual consumer declarations show a shared API need, but are evidence of use rather than automatic evidence of mathlib fit.

## Phase3 — exhaustive literature

Every named channel was executed. The exact requests, returned-response SHA256/UTF8 byte counts, clean titles/URLs and original concise summaries are archived; no article or search-result body is stored.

| Channel | Actual query / locator | Outcome |
|---|---|---|
| General specific | `"Roth theorem" "constant" "exponent"` | Classical exponent formulations with constants; contextual primary reference below. |
| General general | `"power functions" "little o" "exponents"` | Asymptotic power comparison context; not an exported Lean theorem. |
| General aliases | `"regular variation" "power" "domination"` | Regular-variation context is broader, with no need to import that machinery here. |
| Optional mathematical opinion | ask_chatgpt_math | n/a: tool unavailable; no fabricated consultation. |
| Local source | clean.tex1167–1194, §6 reduction | Explicitly absorbs M into a strict exponent loss; source assumes positive integer M, whereas the current theorem already allows signed real M. |
| nLab | `site:ncatlab.org/nlab asymptotic domination powers` | Asymptotic expansion/scale context; direct article open failed unsupported XHTML. |
| Distinct nCatLab | `site:ncatlab.org/ncatlab asymptotic power functions` | No exact namespace-specific arithmetic theorem identified; out-of-namespace hits retained honestly. |
| Stacks | `site:stacks.math.columbia.edu asymptotic powers` | No relevant standalone analytic comparison; scheme/algebra context does not dictate its generality. |
| MathOverflow | `site:mathoverflow.net irrationality exponent multiplicative constant` | Irrationality-measure discussions explain constants versus exponents; no exact replacement theorem inferred. |
| Recent arXiv | `site:arxiv.org irrationality exponent constants after:2021-10-29 before:2026-10-30` | Actual recent query;2026 bounds on irrationality exponents, plus irrelevant physics hits. No different elementary power-comparison argument identified. |

[General searches](../evidence/Roth.eventually_div_rpow_lt/web-batch0.json), [named channels](../evidence/Roth.eventually_div_rpow_lt/web-batch3.json), [MO/recent](../evidence/Roth.eventually_div_rpow_lt/web-batch6.json), [primary opens](../evidence/Roth.eventually_div_rpow_lt/web-primary.json), [local excerpt](../evidence/Roth.eventually_div_rpow_lt/local-excerpt.tex.txt).

Frank's *Approximation to real numbers by algebraic numbers of bounded degree* (2007), p.3 following the general Thue–Siegel–Roth formulation, explains that changing the constant does not change the finiteness assertion when an exponent margin is available; p.4 remark1.6.2 discusses the uniform lower-bound formulation. This supports the use of an arbitrary positive target amplitude, rather than privileging1. [Frank PDF](https://www.math.u-bordeaux.fr/~ybilu/algant/documents/theses/frank.pdf). A recent primary example is Niedbala Giraudin's2026-10-02 abstract on an improved irrationality exponent for ζ(2); it establishes topical currency, not a new proof of elementary absorption. [arXiv abstract](https://arxiv.org/abs/2610.02912).

Literature-standard mathematical principle: a strict power advantage dominates any fixed real amplitude against any positive target amplitude at infinity. The filter form is our verified Lean organization of that principle. No source is claimed to state our exact arbitrary-filter Lean signature.

## Phase4a–4b — parameter and generality audit

| Parameter / restriction | Analysis and actual verification |
|---|---|
| M:ℝ | Already maximally signed: no positivity hypothesis to remove. Nonpositive M satisfies the positive-input comparison for every exponent pair. |
| κ,κ′:ℝ | Keep arbitrary real exponents, including negative ones; examples with negative exponents compile. A generic ordered field cannot replace ℝ while keeping `Real.rpow`. |
| κ′<κ | Essential for the uniform arbitrary-M theorem: compiled iff proves it necessary and sufficient. Not necessary pointwise for small/nonpositive M. Equal exponents give exactly M<C for positive inputs. |
| RHS constant1 | Replace by semantic parameter C:ℝ with0<C. This is a real additional amplitude, not renaming arithmetic syntax. Compiled threshold with M=9,C=3,κ=−2,κ′=−3 is one specialization. C=0 fails for M=0. |
| q:ℕ | Replace natural casts by any f:α→ℝ tending to atTop along any filter l. This removes an index restriction; natural, real, and other cofinal real inputs share one proof. |
| Strict Q<q | Retain on the natural corollary; extracted eventual N≤q is strengthened to Q<q so q>0. A q=0 counterexample shows that dropping eventual positivity is invalid. |
| Implicitness/universes | No unnecessary typeclass hypotheses in the original. Generic α:Type* is universe polymorphic. Filter l need not be assumed nontrivial: eventual statements over bottom are valid. |

Current form is STRICTLY NARROWER than the verified useful analytic form, in two concrete ways: fixed C=1 and natural-cast input. The changes are local to the theorem, require no foundational project-definition redesign, and have compiled recovery. The signed-M feature is retained. This is not a speculative generalization to a different power operation.

Proposed upstream primary signature, proved as `Decay270Generic.eventual_filter`:

```lean
theorem eventual_filter {α : Type*} {l : Filter α} {f : α → ℝ}
    (hf : Filter.Tendsto f l Filter.atTop) {M C κ κ' : ℝ}
    (hκ : κ' < κ) (hC : 0 < C) :
    ∀ᶠ x in l, M / f x ^ κ < C / f x ^ κ'
```

The real-atTop specialization and natural threshold are compiled, and the original follows as `threshold hκ zero_lt_one`. This uses **our new generic theorem**, not an already existing mathlib replacement. [Clean isolated source](../evidence/Roth.eventually_div_rpow_lt/isolated3-executed.lean.txt), [clean raw receipt](../evidence/Roth.eventually_div_rpow_lt/isolated3-receipt.json), [uniform-necessity/guards](../evidence/Roth.eventually_div_rpow_lt/supplement3-executed.lean.txt), [supplement receipt](../evidence/Roth.eventually_div_rpow_lt/supplement3-receipt.json).

## Phase4c — all nine modern-idiom checks

| # | Question | Answer and consequence |
|---|---|---|
|1|Typeclasses replacing hypotheses|No: numerical inequalities and an input-limit hypothesis are data-level assumptions, not instance classes.|
|2|Filters versus sequences/metric notions|Yes for the statement: use any input tending to infinity. The original proof already uses Filter.Tendsto and eventual domination; no ε–δ modernization is invented.|
|3|Universal property|No constructed object requiring a universal property; only a tail witness.|
|4|Bundled substructures|No closed subset, submodule, lattice or quotient is involved.|
|5|Weaker algebraic hierarchy|No mechanical ℝ→ordered-field replacement preserves Real.rpow; generic arithmetic normalization alone does not generalize the analytic power operation.|
|6|Higher categories|No categorical structure or universal-property issue.|
|7|Concrete index|Yes: replace q:ℕ with f:α→ℝ and Tendsto f l atTop. Real and natural inputs are compiled instances.|
|8|Concrete-via-abstract diagnostic|Yes for the natural-cast input. After obtaining its atTop limit, the proof uses only real positivity and real-power algebra. Real.rpow itself remains essential throughout; it is not falsely erased as a concrete witness.|
|9|False-generalization guard|Pass for arbitrary cofinal real input and C>0, with actual original recovery. Reject arbitrary power structures, weak-gap uniform statements, q0, C0, and conflation of LiouvilleWith with fixed-constant sets or uniform IsDiophantine.|

Modern idiom is useful: `Tendsto.comp`/eventual transport handles arbitrary cofinal input; `Filter.eventually_atTop` extracts natural bounds only where the caller needs them; C directly matches positive lower-bound constants. This makes a real downstream difference without changing the analytic operation. [Concrete diagnostic](../evidence/Roth.eventually_div_rpow_lt/concrete-diagnostic.json).

## Phase4.5 — infrastructure risks

The declaration is a theorem: all six definition/class/instance-specific risks (diamond, reducibility leak, noncanonical unfolding, instance priority, universe implementation, coercion ambiguity) are n/a because no new data definition, instance, coercion, or reducibility path is introduced. There is no skipped applicable infrastructure experiment.

## Phase4.6 — all five proof-strategy checks

| # | Check | Finding |
|---|---|---|
|1|ε–δ versus filters|Current proof is already filter-based; keep its strategy.|
|2|Element algebra versus substructures|No ideal/submodule/subring semantics; scalar inequalities are appropriate.|
|3|Sequences versus nets|Statement can use arbitrary-filter input; the proof's existing limit composition already transfers.|
|4|Construction versus universal property|No applicable object construction.|
|5|Missing helper API|An exported eventual constant-absorption comparison would remove repeated power normalization, including the internal argument of LiouvilleWith.frequently_lt_rpow_neg.|

Strategy verdict: MATHLIB-IDIOMATIC. Refactor the statement/interface and factor the scalar normalization once. The missing helper is the proposed comparison itself; no cost-based downgrade or imaginary foundational API is needed.

## Phase5 — all15 formal search cells

| Form | Lean-Finder | Loogle | LeanSearch | Pinned rg | Root local search |
|---|---|---|---|---|---|
|Current natural-threshold fractions|Executed: unrelated recurrence/approximation results|Executed `Real.rpow, _ / _ < _ / _`: no items|Executed: partial LiouvilleWith and power-limit results|Executed: target absent; asymptotic ingredients|Executed `eventually_div_rpow`: target item; index:error|
|Standard exponent-gap domination|Executed: exponential/rpow comparisons, not target|Executed `Filter.Tendsto, Real.rpow, Filter.atTop`: no items|Executed: tendsto_rpow_atTop and natural-power comparisons|Executed: tendsto and internal LiouvilleWith proof|Executed `rpow_lt_rpow`:18 related pointwise comparisons; index:error|
|Abstract little-o/power comparison|Executed: natural-power little-o and rpow-exp results|Executed `Asymptotics.IsLittleO, Real.rpow`: no items|Executed: little-o API and partial matches|Executed: rpow asymptotics, no matching exported fraction comparison|Executed `isLittleO_rpow`:2 rpow-exp items; index:error|

All raw requests/results are retained in the [15-cell matrix](../evidence/Roth.eventually_div_rpow_lt/formal-search-matrix.json). External index snapshots need not match the pin. Root's local index:error is an access limitation, never absence evidence. An untruncated pinned full-name search has no exact target declaration; no inference that all mathematically equivalent statements are absent follows from its exit1 alone. Native signature and proof probes ground the actual candidates. [Full-name search](../evidence/Roth.eventually_div_rpow_lt/full-name-search.json), [pinned source hashes](../evidence/Roth.eventually_div_rpow_lt/mathlib-inputs.json).

Positive ingredients are `tendsto_rpow_atTop` (Asymptotics:38), `Filter.Tendsto.comp`, `Filter.Tendsto.eventually_gt_atTop`, `Filter.eventually_atTop`, `tendsto_natCast_atTop_atTop`, `Real.rpow_pos_of_pos`, and `Real.rpow_sub` (Real:263). These give a starting limit and normalization, not a single exported target theorem.

The closest semantic hit is `LiouvilleWith.frequently_lt_rpow_neg`, whose own proof performs the same absorption internally. `LiouvilleWith` quantifies an existential real constant and frequent denominators, with an explicit exclusion of exact equality. It is not fixed-constant1 pair membership, reduced rational approximation, or the for-every-positive-ε uniform lower-bound API `IsDiophantine`. Its `exists_pos`, `mono`, `frequently_lt_rpow_neg`, and rational/integer/natural affine-invariance implementations were read. Native checks confirm signatures, exponent-loss and natural-multiplication compositions. `liouvilleWith_one 0` compiles, demonstrating that rational0 satisfies exponent1; irrationality cannot be inferred without the actual exponent hypotheses. These are relevant higher-level APIs, not direct replacements for an arbitrary signed-M comparison.

## Phase5.5 — statement shape

Normal forms considered: natural strict threshold, real-atTop eventual comparison, and arbitrary-filter cofinal real-input comparison. `Filter.Eventually` is the compositional form; natural threshold extraction is appropriate at finite-exception callers. Division and negative-power spellings are equivalent only with the relevant positive input hypotheses, so normalization must not lose q0 guards. No orthogonal iff between competing project definitions is introduced; RHS normal-form convention is n/a for this implication theorem.

Syntactic-generality experiments actually compile all three forms and original recovery. Prefer an eventual statement as upstream primary API with M,C implicit and positivity explicit. The original arguments M,κ,κ′ all occur essentially in the conclusion; no unused typeclass or binder can simply be dropped. Strict gap is needed uniformly, while nonpositive-M and equal-exponent branches are separate valid theorems. Overall: RESTATE-BEFORE-SHIP, with the explicit proposed primary signature above and natural corollary.

## Phase6.0 — complete actual callers and inline audit

Three explicit call occurrences in three consumer declarations: two inside Main and one outside the declaring file in LeanEval. Under the command's strict “exclude declaring file” count, internal-use count is1; total project consumer count is3; external-to-file caller files1. No duplicate inline derivation of this exact exponent-gap lemma was found elsewhere in production. Other metric-neighborhood existence proofs in Main/MainLemma concern δ, not this power comparison.

| Caller | Invocation | Role and verified full-body replacement |
|---|---|---|
|Roth.reduction, Main:118 / call122|M=(positive integral multiplier), κ′=(κ+2)/2|Absorb scaling before discarding bounded denominators. Full body retains original irrational/integral conclusion.|
|Roth.exists_reduced_approx, Main:164 / call181|M=1/abs(α−x), κ′=0|Each rational fiber has bounded denominator. M differs from reduction; irrationality supplies the positive nonzero error where the caller divides. Full reduced/coprime conclusion retained.|
|LeanEval…isDiophantine_iff, LeanEval:42 / call46|M=1/C, κ′=2+(κ−2)/2|Compare a uniform positive lower bound with infinite upper approximations. Full equivalence and reverse private-helper branch retained.|

Each complete caller was re-elaborated twice: with the literal original local proof, and with our new generic threshold/recovery. Two necessary private helper declarations were copied completely into each fresh namespace. Six native theorem-type agreements and six standard axiom prints passed; transitive project/scratch value closure rejects the original target and generated auxiliaries. This proves actual callers can use the proposal without signature change; it does not make the proposal “existing mathlib.” [Caller inventory](../evidence/Roth.eventually_div_rpow_lt/callers.json), [full executed callers](../evidence/Roth.eventually_div_rpow_lt/inline2-executed.lean.txt), [raw receipt](../evidence/Roth.eventually_div_rpow_lt/inline2-receipt.json), [inline audit](../evidence/Roth.eventually_div_rpow_lt/inline-audit.json).

## Phase6 — composition and closure

NOT-COMPOSABLE under the actual ≤3-existing-call criterion. The three-call power-limit composition reaches an eventual M<q^(κ−κ′), not the desired natural threshold and fractions. Positivity and nondefinitional `rpow_sub`/division rewrites remain a real proof. `LiouvilleWith.frequently_lt_rpow_neg` has an unrelated additional approximation predicate premise and cannot be applied to arbitrary M. Our generic recovery is a new proof and cannot be counted as a currently existing building block. [Composition accounting](../evidence/Roth.eventually_div_rpow_lt/composition.json).

Before declaring any new generic helpers, a clean mathlib-only original-form example verifies that direct `exact?` does not close; it then closes with the literal original proof. A direct tendsto candidate and closing `simp` probe are also checked. These are bounded discovery evidence, not an absolute mathematical absence theorem. A rejected `apply?` experiment produced suggestions with remaining subgoals and a misleading tactic-success flag under `solve`; it is explicitly excluded from absence/presence evidence. No successful ≤3-call replacement was established.

Original01, isolated03, inline02, scope03 and supplement03 are clean accepted sources. Earlier errors/linter warnings and the poorly placed own-helper closure probe are retained as rejected, with their exact sources and full raw receipts. No partial response, recovered sorryAx, disabled linter, raised resource limit, new axiom, unsafe proof, or native_decide belongs to accepted evidence. All accepted axiom sets are subsets of propext/Classical.choice/Quot.sound. [Attempt accounting](../evidence/Roth.eventually_div_rpow_lt/verification.json).

## Phase7 — verdict and concrete upstream plan

**YES-but-generalise-first**, reasons MODERN-IDIOM and LITERATURE-WEAKENING. Estimated restatement cost: MODERATE, local scalar normalization and statement reorganization; the scratch proof is already completed. This estimate does not determine the verdict. The contribution is justified because the proposed eventual comparison is a reusable real-analysis API, has a complete verified signed-M/C-positive/cofinal-input proof and exact natural recovery, and fills a specific exported comparison gap exemplified by the repeated internal absorption in `LiouvilleWith.frequently_lt_rpow_neg`. Existing mathlib limit operations remain the implementation ingredients. This is not NO-mathlib-has-it: no exact general exported hit and specialization has been demonstrated. It is not NO-composable: translating the eventual power bound into fractions needs positivity and genuine arithmetic normalization. Cost is not a verdict factor.

Home: `Mathlib/Analysis/SpecialFunctions/Pow/Asymptotics.lean`, in the limits-at-+∞ section after `tendsto_rpow_atTop`. Suggested primary name `Filter.Tendsto.eventually_div_rpow_lt_div_rpow`, with real-atTop specialization if useful and natural-tail extraction as a corollary. Proposed PR title: **feat(Analysis/SpecialFunctions/Pow/Asymptotics): eventual constant absorption across real exponent gaps**. Keep arbitrary signed M and positive C; do not upstream the κ′<κ statement with a gratuitous M>0 hypothesis. Final naming is normal PR review, not an unresolved mathematical assessment blocker.

Reviewer suggestion grounded in recent pinned history: Terence Tao (`teorth`), substantive power-limit addition commit `f682f8f0e2edb6a764ffbd330c1b4ef5b2aa7d2e`,2026-07-05, PR41375. Marcelo Lynch's2026-08-21/08-11 edits concern open-scoped cleanup, useful for presentation but not claimed as analytic specialization evidence. [Exact recent commit receipt](../evidence/Roth.eventually_div_rpow_lt/reviewer-commits.json).

Grouping: a standalone power-asymptotics PR. The actual accepted-YES snapshot contains `Roth.main_lemma` and polynomial/derivative results, but no accepted same-home power-comparison declaration; do not bundle unrelated polynomial API simply because it was accepted earlier. The accepted Roth main-lemma contribution can later consume this independent analytic support. [Accepted-YES snapshot](../evidence/Roth.eventually_div_rpow_lt/accepted-YES.json).

Concrete next actions: run `/generalise Roth.eventually_div_rpow_lt` toward the compiled generic signature and `/cleanup Roth/Main.lean Roth.eventually_div_rpow_lt` for the eventual upstream presentation; add the comparison in the specified mathlib home, optionally refactor LiouvilleWith's internal absorption through it, then retain/recover the original threshold at all three named callers. Until upstream, `Roth/Main.lean` is a justified local home; it is not dead code or junk. No production refactor was performed by this read-only assessment.

## Phase8 — completion

All required phases are complete, with no unresolved proof/verification items and root acceptance pending. The report, exact executed sources, original full-file/caller archives, all15 formal receipts, all literature requests/hashes/metadata, fresh17 controls, current copy manifest, portable validator and credential scan form the review package. Root independently reviews and publishes; no automatic mathematical acceptance is implied by root execution.
