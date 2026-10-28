# Roth.Θ_unique_le — canonical declaration199

Verdict: **BORDERLINE-needs-human**. This is Lemma5's substantive logarithmic bound on an arithmetic extremal family. The supremum step is existing mathlib, but its required pointwise bound contains new polynomial arithmetic. Keep the theorem in `Roth/Theta.lean` while the upstream scope of `RSet` and the extremal family is decided. This is a completed read-only assessment; future API-design questions are distinct from verification obligations.

## Phase 0 — Baseline and native declaration

All17 production-source/pin hashes freshly match the shared clean2467-job baseline. No production Lean file, dependency pin, Git state, or overview record was edited by this worker. The entire985-line declaring module was read, including the two complete callers. See [fresh hashes](../evidence/Roth.Θ_unique_le/source-hashes.json), [baseline](../evidence/Roth.Θ_unique_le/baseline-build.txt), [full source](../evidence/Roth.Θ_unique_le/source-Theta.lean.txt), and [original native receipt](../evidence/Roth.Θ_unique_le/theta-unique199-original-receipt.json).

Kind: public theorem, source `Roth/Theta.lean:256`. Full elaborated native type:

```lean
∀ {σ : Type u_1} [Fintype σ] [Unique σ] {B : ℝ},
  1 ≤ B → ∀ {q : σ → ℕ}, 1 < q default → ∀ {r : σ → ℕ},
  Roth.Θ B q r ≤ Real.log B / (↑(r default) * Real.log ↑(q default))
```

There is no `DecidableEq σ` binder. Original and accepted new proofs use only `propext`, `Classical.choice`, and `Quot.sound`; no sorry/axiom/unsafe/native_decide/raised limits. Root's exact canonical ordered293-entry audit has293 distinct names and293 values, with2 direct value consumers and0 direct type consumers. Source occurrences and direct kernel consumers were audited separately.

## Phase 1 — Mathematical content and proof

For a singleton variable type, fix a coefficient bound B≥1, a denominator q>1, and a natural weight r. Consider all nonzero integer polynomials of degree≤r with every coefficient of absolute value≤B, at all reduced fractions h/q. Their weighted indices have supremum at most log B/(r log q). The conclusion includes r=0 under Lean's total division convention; the paper instead assumes positive weights.

The proof supplies the generic supremum upper-bound theorem with a pointwise arithmetic estimate. Convert the singleton-variable polynomial to an ordinary polynomial. Its rational root multiplicity t gives index=t/r. Gauss's lemma yields an integer factorization R=(qX−h)^t Q. Nonzero integral leading coefficients imply q^t≤|lc R|≤B. Taking logarithms and dividing by log q>0 and by nonnegative r gives the pointwise estimate, hence the supremum bound. The current declaration extracts only the leading-coefficient instance of its stronger all-coefficient assumption.

Direct project proof dependencies are `Roth.Θ_le_of_forall_index_le` and private `Roth.index_unique_le_log_div`; the latter contains the conversion/logarithm work and invokes `Roth.pow_rootMultiplicity_le`, which uses `Roth.exists_eq_pow_mul_of_rootMultiplicity`. The all-coefficient-to-leading-coefficient bridge uses mathlib `Polynomial.leadingCoeff` and `MvPolynomial.coeff_uniqueAlgEquiv`.

## Phase 2 — Preliminary checks

**BIG**: module main result, explicitly Lemma5 of the source and base input for Lemma7. It introduces no structure. The one-line-definition test is **n/a**, because this is a theorem; its short proof calls substantive project arithmetic and is not evidence of a short composition of existing mathlib laws. No private/collision prefilter applies.

## Phase 3 — Exhaustive literature

Exact requests, returned-response SHA256/bytes, locators, and original summaries are archived in [web evidence](../evidence/Roth.Θ_unique_le/web-evidence.json). Full external article/search bodies were not persisted. Supplementary access details appear in [primary opens](../evidence/Roth.Θ_unique_le/web-primary.json), [Stacks retry](../evidence/Roth.Θ_unique_le/web-stacks.json), [supplementary search](../evidence/Roth.Θ_unique_le/web-supplementary.json), and [five-year query](../evidence/Roth.Θ_unique_le/web-recent-window.json).

| Channel | Actual query or locator | Result and implication |
|---|---|---|
| General web: specific | Roth theorem "Theta" "log B" polynomial index lemma5 | A Thue–Siegel–Roth thesis §4 gives the extremal-index viewpoint and a number-field estimate with additional terms. Its formula is not identical to the present rational-denominator bound. |
| General web: standard | integer polynomial rational root multiplicity denominator leading coefficient bound Gauss lemma | Stanford Gauss-lemma notes and NIU algebra notes give primitive factorization and denominator-divides-leading-coefficient background. |
| General web: alias | rational root theorem multiplicity height polynomial logarithm vanishing order | Rational-root/Gauss terminology identified; no more general identical supremum law confirmed. |
| ChatGPT math MCP | optional standard-form/generality/historical query | n/a: `ask_chatgpt_math` unavailable; other channels were all executed. |
| Local reference | clean.tex §5 Lemma `roth:lem5`, lines671–705 | Exact Θ1 bound and factorization→leading-coefficient→log→supremum proof. [Excerpt](../evidence/Roth.Θ_unique_le/clean-lemma5-excerpt.tex.txt), [reference hash](../evidence/Roth.Θ_unique_le/local-literature.json). |
| nLab | site:ncatlab.org/nlab rational root polynomial multiplicity | Rational zero theorem, root, polynomial pages; background only. Direct rational-zero open failed with unsupported XHTML, honestly retained. Its search-result formulation is not used as the authoritative theorem. |
| nCatLab | site:ncatlab.org/ncatlab rational root polynomial multiplicity; follow-up "rational" "polynomial" | Returned /nlab pages, no exact in-namespace result. This is not a proof of absence. No categorical arithmetic-height formulation established. |
| Stacks | site:stacks.math.columbia.edu polynomial Gauss lemma primitive rational roots; independent retry Gauss lemma polynomial unique factorization | Tags00EZ/00F0 use Gauss and denominator clearing, background only. Exploratory direct tag00FC was unrelated and is not supporting evidence. |
| MathOverflow | site:mathoverflow.net rational root multiplicity denominator leading coefficient | Related multiplicity/fewnomial and rational-root discussions, no exact Θ bound or validated weakening. |
| Recent arXiv | rational root multiplicity polynomial height2021…2026; explicit after:2021-10-27 before:2026-10-28 Roth polynomial index | Broad query found adjacent root algorithms and height counting; exact date-window query returned empty. arXiv2301.07880 has a2023 upload but2004 journal reference and does not establish a recent mathematical reformulation. |

Primary background locators: [NIU propositions4.3.1 and4.3.4–5](https://faculty.niu.edu/math_beachy/aaol/polynomials.shtml), [Stanford Gauss lemma](https://crypto.stanford.edu/pbc/notes/numberfield/gausslemma.html), [Stacks00EZ](https://stacks.math.columbia.edu/tag/00EZ), [Stacks00F0](https://stacks.math.columbia.edu/tag/00F0). Stanford search snippets returned successfully, but the direct open timed out. The primary local source is authoritative for the exact bound. Literature-standard concept: one-variable Roth index bound, underpinned by the rational-root theorem with multiplicity. Number-field heights suggest a wider theory, but their additional terms prevent claiming a mechanical weakening of this statement.

## Phase 4a — Parameters and mathematical generality

| Parameter/hypothesis | Role | Assessment |
|---|---|---|
| `σ : Type*` | names the variable | Universe-polymorphic already; no special Unit/Fin restriction. |
| `[Fintype σ]` | inherited parent interface | Redundant given `[Unique σ]`; full proof without explicit Fintype binder compiled. This is syntactic simplification, not new arithmetic generality. |
| `[Unique σ]` | one variable and a canonical default | Essential to this specific one-variable estimate; dropping it would replace the mathematical problem by multivariable Roth's lemma. Arbitrary singleton representations already supported. |
| `B : ℝ` | coefficient height cutoff | Arbitrary real bound already; logarithm naturally real. Replacing by a natural bound would narrow the theorem. |
| `hB : 1 ≤ B` | nonempty polynomial family and nonnegative logarithm | Cannot simply drop: B=1/2 gives nonnegative Θ but right side−1 for q2,r1. Native guard included. B0 is not this counterexample because log0=0 in Lean. |
| `q : σ → ℕ`, `1 < q default` | positive reduced-fraction denominator and positive log | q1 fails mathematically: X−1 with B1,r1,h1 has index1, but RHS0. This q1 illustration is a mathematical necessity argument, not claimed as a separately compiled example. A signed denominator API requires abs q and its own representation bridge. |
| `r : σ → ℕ` | degree bound and index normalization | Already permits zero, stronger than paper's positive weight convention. Real weights or separate degree bounds would change parent index/family interfaces and need a new proof/bridge. |
| integer coefficients | discrete lower bound on nonzero leading coefficient | Cannot replace by arbitrary rational/real coefficients with same bound: X−1/2 has root multiplicity1 at1/2, coefficients≤1, and contradicts denominator growth. A general absolute-value theorem needs a lower bound on nonzero coefficient size. |
| degree and every coefficient bound (inside RSet) | family definition | Pointwise proof uses only nonzero and leading-coefficient bound; degree bound is unused by that arithmetic step, but retained in the present extremal-family meaning. Enlarging family is a different presentation requiring a bridge, not deleting a visible binder. |
| varying reduced numerator | coprimality quantified inside family | Essential to denominator extraction; changing h/q to a nonreduced presentation cannot preserve the estimate. |

## Phase 4b — Verified weakening

`RothThetaUnique199.fullUniqueOnly` is a native successful full theorem with `[Unique σ]` alone; no explicit Fintype or DecidableEq binder. `fullNoDecEq` is an original-context replay (the original already omits DecidableEq), not a weakening. [Executed source](../evidence/Roth.Θ_unique_le/theta-unique199-project-executed.lean.txt), [receipt](../evidence/Roth.Θ_unique_le/theta-unique199-project-receipt.json).

No further mathematical weakening of this fixed natural-weight integer-family statement was verified; the explicit Fintype binder can be omitted. No speculative number-field, arbitrary-field, multivariable, or arbitrary-height extension is claimed mechanically verified. Existing independent generalizations of the arithmetic helpers at declarations196/197 are new proofs, not evidence that their conclusion is already an existing mathlib theorem.

## Phase 4c — Nine modern-idiom checks

| # | Question | Decision and downstream effect |
|---|---|---|
|1|Typeclass preambles?|Already uses Fintype/Unique appropriately; remove redundant explicit Fintype under Unique. Coprimality remains a property of individual numerators, not a global class.|
|2|Sequences/metrics→filters?|No limits or metric argument. Logarithm monotonicity is finite algebraic analysis.|
|3|Constructed object→universal property?|No new object constructed by this theorem. Parent Θ is ordinary `sSup`, already the appropriate universal order object.|
|4|Set closure→bundled substructure?|RSet is not additive/multiplicative closure: fixed coefficient/degree cutoffs and nonzero condition do not define a subring/submodule. Bundle only if a later height-family design benefits.|
|5|Field/vector hierarchy weakening?|Arithmetic core generalizes to GCD-domain divisibility and signed integer ordered-ring bounds, addressed separately at196/197. The real logarithm and discrete height bound remain here.|
|6|Higher category generalization?|No categorical statement or coherence data. None justified.|
|7|Concrete index→ordered structure?|Supremum packaging works in conditional complete lattices; logarithmic multiplicity conversion is specifically real. Generic packaging is verified in isolated mathlib, not confused with the complete arithmetic theorem.|
|8|Concrete-via-abstract adversarial diagnostic?|The3-line body contains no literal Θ/indexSet/RSet after its signature; it calls a supremum helper and the private arithmetic helper. Diagnostic fires for outer packaging. Honest abstract form is a supremum law WITH a supplied pointwise exponential bound; arithmetic does not disappear. It isolates the already-existing order API and the genuinely substantive denominator estimate.|
|9|False-generalization guard?|Replacing the complete Θ law by `csSup_le hs hc` while quietly supplying the whole logarithmic hc changes the task. Reject that as a complete replacement. Replacing integer polynomials by arbitrary rational/real ones without discreteness is false. GCD-domain core plus a measured height is a real potential extension, with additional hypotheses.|

Modern idiom: use `Polynomial.rootMultiplicity` for the single-polynomial arithmetic; keep plain `sSup` for extrema. Isolated `logarithmicOfPow` and `supremumOfLog` compile, showing precisely which exponential premise must be supplied. [Source](../evidence/Roth.Θ_unique_le/theta-unique199-isolated-executed.lean.txt), [raw clean receipt](../evidence/Roth.Θ_unique_le/theta-unique199-isolated-receipt.json). These are new probe proofs of packaging with a supplied premise, not existing full arithmetic replacements.

## Phase 4.5 — Infrastructure risk

All six rows are n/a: this is a theorem introducing no operation, instance, bundled structure, coercion, or definitional representation. Respectively: typeclass diamonds n/a; competing instances n/a; definitional-equality mismatch n/a; coercion ambiguity n/a; reducibility barrier n/a; import/API representation risk n/a. A future upstream extremal-family definition must separately assess those risks. This theorem's proof depends on the existing parent representation, not a new instance.

## Phase 4.6 — Five proof-strategy checks

| # | Strategy | Assessment |
|---|---|---|
|1|ε–δ→filters|n/a: no topology proof.|
|2|Elements→ideal/submodule inclusions|No: coefficient/degree cutoff family is not a submodule. Divisibility belongs in polynomial arithmetic helper, already isolated.|
|3|Sequences→nets|n/a: no limiting process.|
|4|Construction→universal property|No new construction; sSup already captures upper-bound universality.|
|5|Missing upstream helpers|Yes: multiplicity-sensitive denominator divisibility and its numerical leading-coefficient bound are plausible separate upstream API (196/197), followed by logarithmic conversion if useful. Existing csSup does not supply them.|

Strategy is mathematically idiomatic: arithmetic first, monotone logarithm second, supremum last. Refactor recommendation concerns API ownership: put general arithmetic downstream of RationalRoot/GaussLemma, retain this project-family endpoint until that family is accepted. No cost-based downgrade is used.

## Phase 5 — Five methods on three forms

Each formal method was actually called separately for each form. Complete raw tool receipts are `search-0.json` through `search-11.json`; source searches are [current](../evidence/Roth.Θ_unique_le/rg-current.json), [standard](../evidence/Roth.Θ_unique_le/rg-standard.json), [abstract](../evidence/Roth.Θ_unique_le/rg-abstract.json). The corrected current Loogle query is [retry2](../evidence/Roth.Θ_unique_le/search-current-loogle-retry2.json); the initial unknown `sSup` identifier and intermediate rate limit are retained separately, not treated as empty success.

| Form | Finder | Loogle | LeanSearch | rg | Local |
|---|---|---|---|---|---|
|Current Θ1 logarithmic index supremum|Unrelated combinatorial Roth-number/Chevalley bounds|`Real.log, SupSet.sSup, _ ≤ _` empty after correction|Weighted power-series orders and analytic order, not arithmetic-height bound|No exact Θ_unique_le mathlib declaration|Empty; index unavailable, not absence|
|Standard rational-root multiplicity denominator/leading coefficient|`den_dvd_of_is_root`, rational evaluation lower bound, rootMultiplicity|`Polynomial.rootMultiplicity, Polynomial.leadingCoeff` empty|den/num divisibility, multiplicity and root cardinality laws|pow-root-multiplicity divisor and single-root denominator divisor|Root-multiplicity declarations found from source; index unavailable|
|Abstract supremum from exponential bound|Logarithmic absolute-value/asymptotic estimates, not complete target|Generic complete lattice supremum laws|`csSup_le`, `csSup_le_iff`, indexed variants|Pinned generic conditional supremum and logarithm laws|csSup variants found from source; index unavailable|

Pinned positive candidates: `csSup_le` in `Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:201`; `Real.log_pow` in `Mathlib/Analysis/SpecialFunctions/Log/Basic.lean:288`; `Polynomial.pow_rootMultiplicity_dvd` in `Mathlib/Algebra/Polynomial/Div.lean:538`; `den_dvd_of_is_root` in `Mathlib/RingTheory/Polynomial/RationalRoot.lean:89`; primitive-fraction divisibility in `Mathlib/RingTheory/Polynomial/GaussLemma.lean`. [Pinned files/hash list](../evidence/Roth.Θ_unique_le/mathlib-inputs.json). Native checks verify the generic order/log/divisibility candidates. Rational-root single-denominator divisibility gives q∣lcR, not q^t∣lcR; its multiplicity strengthening needs the primitive factorization/iteration argument. Root cardinality or separability only bound multiplicity by degree or1, not log B/log q. Weighted order describes vanishing, not coefficient-height growth.

External indexes may differ from the project pin. Search failures and unavailable local index are not absence proofs. Accepted native mathlib-only probes guard `#check_failure Roth.Θ_unique_le` and the private project helper. No global theorem-absence claim is made.

## Phase 5.5 — Three statement-shape checks

1. **Normal form:** singleton `MvPolynomial` is transportable to `Polynomial`; ordinary root multiplicity is the natural arithmetic target. The project uses singleton variable types to compose with Option/Fin induction. The bridge is not silently definitional: coefficients, map compatibility, and index/rootMultiplicity need real lemmas.
2. **Syntactic generality:** remove explicit Fintype binder under Unique; keep q,r implicit functions so existing Unit and Fin1 callers infer them. Native full caller replay confirms both representations still elaborate.
3. **Superfluous assumptions:** original already omits DecidableEq. r positivity is already removed. hB and q>1 cannot be dropped unchanged; tests/necessity arguments above. The bound on every coefficient is stronger than the pointwise leading-coefficient condition, but belongs to the chosen extremal family.

## Phase 6.0 — Callers and inline audit

Fresh [all-source rg](../evidence/Roth.Θ_unique_le/callers.json), [canonical source inventory search](../evidence/Roth.Θ_unique_le/inventory-callers.json), and [lexical body enumeration](../evidence/Roth.Θ_unique_le/lexical-enumeration.json) agree on two actual body calls. Module documentation at35 and declaration signature at256 are not callers. Root's direct kernel-value audit independently returns the same two private constants, no type consumer. This is not a claim about transitive kernel/simp dependency closure.

| Caller | Occurrence | Mathematical use and concrete refactor |
|---|---|---|
|private `Roth.theta_scaled_unique_le_aux`|Theta759|Bounds one-variable scaled Θ byδ using the logarithmic expression and balanced log hypothesis. Full body replay with `fullUniqueOnly` compiles. Keep this endpoint locally; if deleted, inline its entire supremum+arithmetic proof here, not merely csSup.|
|private `Roth.theta_lt_base_aux`|Theta822|The m1 induction base sets B=q^(δr), cancels log/r and comparesδ to10√δ. Full body replay with `fullUniqueOnly` compiles. Same local theorem reuse or honest full arithmetic inline.|

[Both complete caller bodies and execution](../evidence/Roth.Θ_unique_le/theta-unique199-fullcaller-executed.lean.txt), [receipt](../evidence/Roth.Θ_unique_le/theta-unique199-fullcaller-receipt.json). Only the target occurrence is replaced; surrounding arithmetic is preserved. These experiments do not use the imported target to prove its replacement.

## Phase 6 — Actual composition experiments

The old proof has two project helper applications plus coefficient normalization. Those helper names are not mathlib building blocks. The genuine mathlib order endpoint is `csSup_le hs hc`; for declaration190 hc is the input, so that parent re-aim is NO-mathlib-has-it. Here hc is the main mathematical conclusion to prove, so190's verdict does not transfer. Re-aiming Θ to SupSet.sSup removes the named supremum wrapper but leaves the complete arithmetic estimate.

Actual-context negative probes compile `fail_if_success exact csSup_le (Roth.indexSet_nonempty hB q r)` and a closing `simp only [Roth.Θ, Roth.indexSet, Roth.RSet]`: both fail to close the full logarithmic target; the proof then closes with the independently replayed arithmetic argument. They are actual-context candidate experiments, not mathlib-only isolation. The separate isolated experiment proves generic logarithmic conversion and supremum transfer with q^t≤B explicitly assumed; it deliberately documents that remaining premise. It does not prove a new integer-polynomial theorem by assumption smuggling.

No ≤3 existing-mathlib-call full replacement was verified. A short new helper proof, a previous project theorem, or a closing `simp [defs...]` would not automatically satisfy the strict NO gate. The present proof length alone is irrelevant. Substantive new arithmetic is already separated in196/197; the unresolved issue is whether the additional extremal-family endpoint belongs in mathlib, independent of accepting those arithmetic contributions.

## Phase 7 — Verdict and concrete upstream questions

**BORDERLINE-needs-human**, because upstream scope of this particular coefficient/degree-bounded arithmetic extremal family remains a design question. This is neither a downgrade based on effort nor a claim that mathlib already contains the whole theorem. Literature identifies the result exactly and the arithmetic core is meaningful; a theorem in terms of project RSet/Θ needs that family API accepted first. Parent Θ's exact sSup representation is existing mathlib, but the arithmetic family law remains substantive.

1. Should mathlib expose a coefficient/degree-bounded integer-polynomial family and its extremal rational-point index as public number-theory API, rather than keeping this endpoint in Roth?
2. If yes, should one-variable height bounds be stated first for `Polynomial.rootMultiplicity` with a leading-coefficient bound, and the extremal-family corollary placed only after that API?
3. Should a future logarithmic height API handle signed reduced denominators through abs q and abstract discrete absolute values, before introducing an extremal Θ notation?

These are future upstream questions, not requests to pause the authorized assessment. Immediate local action: retain the named Lemma5 endpoint, remove redundant Fintype binder when cleanup is authorized, and pursue196/197's independent arithmetic APIs separately. Alternative local destination remains `Roth/Theta.lean`, adjacent to the arithmetic helpers and its two consumers. No source edit or PR is performed in this assessment. If family inclusion is approved, a provisional leaf module `Mathlib/NumberTheory/DiophantineApproximation/PolynomialIndex.lean` would need import-layer review; no existing filename or accepted design is asserted.

## Phase 8 — Verification and handoff

All required phases completed with honest n/a rows. Accepted native sources, original paths/requests, source hashes, scoped diagnostic markers, and standard-axiom checks are in [verification](../evidence/Roth.Θ_unique_le/verification.json). The sharp Bhalf guard demonstrates that hB cannot simply be removed. The hq necessity example above is explicitly mathematical rather than native. Full source/caller proofs and mathlib-only order/log candidate experiments succeeded; no unresolved proof obligation remains in the assessment. The package has a current hash/byte [copy manifest](../evidence/Roth.Θ_unique_le/copy-manifest.json) and [portable read-only validator](../evidence/Roth.Θ_unique_le/validate.py). Root independently reviews this frozen worker package before integration; root acceptance starts pending.
