# Roth.exists_reduced_approx — canonical274

**Verdict: YES-but-generalise-first.** The reduced, unbounded-denominator existence theorem has substantive finite-fiber content. Its `0 < κ` hypothesis can be removed. A separate, stronger theorem for **every `κ ≤ 2`** supplies the same conclusion for every irrational real **without any supplied infinitude hypothesis**. Both are new scratch proofs, not names of existing mathlib theorems. Root acceptance is pending; production sources and pins remain unchanged.

## Phase0 — baseline and scope

The shared baseline built2467 jobs successfully; fresh hashes of all17 production sources/pins match the tracked shared manifest. The successful prior Theta228 file-end build remains applicable; the next mandatory literal file-end build is289, so274 requires no additional full build. See [baseline](../evidence/Roth.exists_reduced_approx/baseline-build.txt), [fresh inputs](../evidence/Roth.exists_reduced_approx/inputs.json), and [shared input manifest](../evidence/Roth.exists_reduced_approx/input-manifest.json).

I read all of Main, including the target/private normalization helper, the full sole direct caller `exists_approximants`, subsequent use through `exists_roth_approximants_aux` and the Roth proofs, and the full LeanEval continuation. Full archives: [Main](../evidence/Roth.exists_reduced_approx/source-Main.lean.txt), [LeanEval](../evidence/Roth.exists_reduced_approx/source-LeanEval.lean.txt). No further agents or production/Git mutations were used. All native Lean and project-LSP work was executed by root, with exact requests, sources, hashes, timings, and raw returns preserved.

The original replay scope is **exact target plus its necessary private normalization helper**, in `Reduced274Original`; unrelated Main declarations were not replayed. Public prerequisites remain imported. The target is renamed only outside the directly generated canonical array; the helper loses its private modifier in the scratch namespace. Exact original/replay theorem type agreement is checked using `Subsingleton.elim`, which proves same proposition type rather than proof construction identity. See [exact original execution source](../evidence/Roth.exists_reduced_approx/original-executed.lean.txt) and [raw receipt](../evidence/Roth.exists_reduced_approx/original-receipt.json).

## Phase1 — mathematical content and exact type

If an irrational real α admits infinitely many pairs of integers h and positive natural denominators q with `|α−h/q| < 1/q^κ`, the theorem returns such an approximant in lowest terms beyond any supplied natural threshold Q₀. The current statement assumes κ positive. It returns **actual integer coprimality** and the **strict** inequality Q₀<q, not merely a large unreduced pair or a rational identity.

Native `Lean.getConstInfo`, printed with `pp.funBinderTypes` under a target-specific tag, gives:

```lean
∀ {α : ℝ}, Irrational α → ∀ {κ : ℝ},
  0 < κ → (Roth.approxSet α κ).Infinite → ∀ Q₀ : ℕ,
    ∃ hq ∈ Roth.approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 ↑hq.2
```

The proof sends pairs to their rational value ρ(h,q)=h/q. If all reduced solutions had denominator≤Q₀, canonicalization would put the rational image inside a finite bounded-denominator set. For each fixed rational x, irrationality gives a positive error `|α−x|`; positive-power decay bounds the original denominators in that fiber. Finite rational image plus finite fibers would make the original pair set finite, contradicting the hypothesis.

Direct project constants in the loaded target value are `approxSet`, `approxSet_den_le_finite`, the private `approxSet_num_den_mem_aux`, and `eventually_div_rpow_lt`; these agree with the project-restricted closure. See [native type/body metadata](../evidence/Roth.exists_reduced_approx/native-type.json). The pp.all kernel value print explicitly elides **86997 characters**. It is **not a complete kernel-body dump**; the complete written proof, complete type/constants audit, actual kernel values for all293 canonical declarations, and standard-axiom check remain preserved.

## Phase2 — size and one-line test

**SMALL:** a preparatory reduction lemma, not one of Main's named main results. The mathematical argument is nevertheless nontrivial. The one-line-definition check is **justified n/a: theorem**, so no definition exemption or wrapper inference applies.

## Phase3 — exhaustive literature

Every named channel was executed; the optional mathematical second-opinion tool is unavailable. Exact requests, returned-response hashes/byte counts/status, clean titles/URLs/locators, and original concise summaries are retained in [literature accounting](../evidence/Roth.exists_reduced_approx/literature.json) and the [first web receipt](../evidence/Roth.exists_reduced_approx/web1-receipt.json), [second](../evidence/Roth.exists_reduced_approx/web2-receipt.json), [third](../evidence/Roth.exists_reduced_approx/web3-receipt.json), [fourth](../evidence/Roth.exists_reduced_approx/web4-receipt.json), [fifth](../evidence/Roth.exists_reduced_approx/web5-receipt.json). No complete third-party article/search-result bodies were persisted.

| Channel | Actual query/scope | Finding and limitation |
|---|---|---|
| General specific | irrational rational approximation reduced fractions unbounded denominators infinitely many pairs exponent positive | Standard reduced/unreduced distinction; no identity-only solution to the target. |
| General functions | Diophantine approximation approximation function tending zero reduced rational denominators infinite fibers | Approximation-function and height generalizations; their hypotheses require independent checking. |
| General alias | Dirichlet approximation theorem infinitely many coprime rational approximations denominators | Irrational Dirichlet exponent2 theorem supports the subcritical branch. |
| ask_chatgpt_math | unavailable | Justified optional n/a; other channels unchanged. |
| Local references | clean.tex §6 reduction and §7 first paragraph | Exactly the finite-value-fiber and reduced-denominator argument; [local evidence](../evidence/Roth.exists_reduced_approx/literature-local.txt). |
| nLab | `site:ncatlab.org/nlab Diophantine approximation irrational rational reduced fractions` | Fraction/coprimality and continued-fraction context. |
| nCatLab | distinct `site:ncatlab.org/ncatlab Diophantine approximation irrational reduced fractions` | Returned material outside that namespace; no exact in-namespace theorem established, not an absence claim. |
| Stacks | `site:stacks.math.columbia.edu irrational rational approximation denominators` | No applicable pointwise reduction theorem located; generic algebraic-geometric locality is different. |
| MathOverflow | `site:mathoverflow.net rational approximation reduced denominators infinite irrational` | Congruence restrictions reinforce the content of reduced versus unreduced denominators. |
| recent arXiv | `site:arxiv.org Diophantine approximation reduced fractions approximation function after:2021-10-29 before:2026-10-30` | 2403.11257, submitted2024-03-17, concerns almost-everywhere multidimensional reduced approximation, not this pointwise lemma. |

The standard content is rational canonicalization plus local finiteness and shrinking-error fiber control. Waldschmidt's [*Diophantine approximations and continued fractions*](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/RNTA2017.pdf), §1 p1 lines18–52 in the returned extraction, gives both rational separation and infinitely many coprime exponent2 approximants for irrational reals. This proves why a separate Dirichlet argument can cover κ≤2; it does not justify applying the original positive-decay fiber proof unchanged to negative κ. The modern [Frühwirth–Hauke paper](https://arxiv.org/abs/2403.11257), abstract, is contextual evidence for approximation-function/coprimality APIs, not a proof of our conclusion. Root independently checked these primary sources: [cross-check](../evidence/Roth.exists_reduced_approx/root-primary-crosscheck.json).

## Phase4a–b — complete generality audit

| Parameter/hypothesis | Assessment |
|---|---|
| α:ℝ | The proof uses the actual real rational embedding, absolute value, and real powers. No unsupported arbitrary-field or p-adic extension is claimed. |
| Irrational α | Uniform deletion is false. At α=0, κ=3 every `(0,q)` with q>0 is an exact approximant, while no coprime approximant can have q>1. A native counterexample certifies the whole claim, not just that a proof step fails. |
| κ:ℝ and 0<κ | **Remove positivity entirely.** The positive branch retains the original argument. Otherwise Dirichlet2 produces reduced arbitrarily large approximants and exponent monotonicity gives the same fixed1 κ bound. The stronger native theorem does this for allκ≤2. |
| Infinite supplied pair set | Retained in the unrestricted theorem. Removable in the verified κ≤2 theorem. No unconditional theorem above2 is claimed. |
| Q₀:ℕ | Arbitrary threshold, including0, remains; output stays strict Q₀<q. Native zero-threshold recovery is included. |
| Integer numerator/natural denominator | Positive denominator and actual IsCoprime are retained. Rational canonicalization is a representation bridge with quantitative obligations. |
| Fixed coefficient1/tolerance | A real supplied-quality predicate. Replacing1 by an existential C or arbitrary function changes the interface. The own generic schema accepts an arbitrary set/value map/canonicalizer/height/good predicate under explicit local-finiteness, finite-fiber, and normalization premises; complete exact arithmetic recovery was verified. It is not an unproved arbitrary-tolerance analytic theorem. |

**STRICTLY NARROWER THAN STANDARD, with native verified weakening.** The proposed compatible statement is:

```lean
∀ {α : ℝ}, Irrational α → ∀ {κ : ℝ}, (Roth.approxSet α κ).Infinite →
  ∀ Q₀ : ℕ, ∃ hq ∈ Roth.approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 (hq.2 : ℤ)
```

Also expose the stronger subcritical result:

```lean
∀ {α : ℝ}, Irrational α → ∀ {κ : ℝ}, κ ≤ 2 →
  ∀ Q₀ : ℕ, ∃ hq ∈ Roth.approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 (hq.2 : ℤ)
```

[Exact accepted mathlib-only proofs](../evidence/Roth.exists_reduced_approx/isolated2-executed.lean.txt), [raw unrestricted/subcritical receipt](../evidence/Roth.exists_reduced_approx/isolated2-receipt.json), [generality details](../evidence/Roth.exists_reduced_approx/generality.json). These new proofs reconstruct the project predicate and positive arithmetic from mathlib only, check the project target unavailable, and recover the exact original statement and Q₀=0. The original normalization helper needs κ≥0 and is never directly applied at negative κ. Cost is not a verdict criterion; proof adjustment is modest and does not change the underlying predicate or foundational project definitions.

## Phase4c — all nine modern-idiom rows

| # | Question | Finding / concrete consequence |
|---|---|---|
|1|Typeclasses instead of mathematical premises?|No: irrationality and infinitude are predicates, not missing structural instances.|
|2|Filters/nets?|Arbitrarily large q can be represented by frequently-atTop, enabling Filter monotonic transport. Existing LiouvilleWith uses that idiom, but its existential C and exact-equality exclusion are different; no unproved equivalence is asserted.|
|3|Universal property?|No categorical construction; rational num/den is the relevant canonical representation.|
|4|Bundled substructure?|No: approximation sets are not subrings or submodules.|
|5|Typeclass hierarchy weakening?|No unchecked field/ring generalization: real power decay and rational embedding are essential to this arithmetic proof.|
|6|Higher categories?|No applicable content.|
|7|Concrete index/height?|A universe-polymorphic canonicalization/height/fiber theorem was actually proved; exact ℤ×ℕ recovery retains arithmetic and coprimality.|
|8|Concrete-via-abstract diagnostic?|Exact `approxSet` occurs in3 original proof-body lines, with no initial unfolding eliminating all arithmetic, so the ≤1-line diagnostic does not automatically fire. The structural scaffold was independently abstracted and fully recovered anyway.|
|9|False-generalization guard?|PASS: unrestricted κ retains the fixed1 predicate, strict height bound, and actual coprimality. It is not silently replaced by LiouvilleWith, uniform IsDiophantine, an almost-everywhere theorem, or a predicate supplied with the desired conclusion.|

[Generic theorem and full arithmetic recovery](../evidence/Roth.exists_reduced_approx/generic-executed.lean.txt), [raw generic receipt](../evidence/Roth.exists_reduced_approx/generic-receipt.json). `unbounded_canonical` is **our new proof**, not an existing mathlib replacement. It separates the finite-set scaffold from the reusable arithmetic obligations. The selected public improvement is removing positivity and exposing subcritical existence; a filter presentation is optional organization, not the reason for the YES verdict.

## Phase4.5 — six infrastructure risks

Each of typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priorities, universe issues, and coercion ambiguity is **justified n/a** for this theorem. It introduces no new data definition, instance search path, or coercion. Scratch generic definitions are evidence, not a proposal to install a new competing rational representation. [All rows](../evidence/Roth.exists_reduced_approx/phase-checks.json).

## Phase4.6 — all five proof-strategy rows

| Question | Finding |
|---|---|
|Topology εδ instead of filters?|No: power growth is already obtained via atTop limits.|
|Algebra elements instead of substructures?|No relevant ideal/submodule inclusion replaces actual rational reduction/coprimality.|
|Analysis sequences instead of nets?|No sequence-limit proof in this target.|
|Categorical construction instead of universal property?|No applicable categorical object.|
|Missing reusable helper API?|Yes: finite fibers of rational values for shrinking-error pairs, followed by canonicalization and unbounded height. The generic scaffold and current arithmetic recovery are native verified.|

**REFACTOR-RECOMMENDED:** separate finite rational fibers and normalization from structural unboundedness; add the independent Dirichlet2 branch for subcritical κ. This isolates mathematical content and avoids conflating an unreduced denominator with rational height. It is not a≤3existing-call composition.

## Phase5 — all15 formal-search cells

Each of current, literature-standard, and abstract forms used Finder, Loogle, LeanSearch, source rg, and root-owned local search. Exact requests/full raw returns are preserved and indexed in [15-cell matrix](../evidence/Roth.exists_reduced_approx/formal-search-matrix.json).

| Form | Finder | Loogle | LeanSearch | Source rg | Local LSP |
|---|---|---|---|---|---|
|Current fixed-quality pairs|Dirichlet2/LiouvilleWith partial matches|Irrational+IsCoprime pattern: no result|Dirichlet/finite rational partial matches|No query matches; no absence inference|Project target returned, **index=error**|
|Standard reduced rationals|Dirichlet2 and rational separation|Dirichlet2/iff irrational|Dirichlet/Legendre|Pinned Dirichlet/Liouville signatures|Two Dirichlet names returned, **index=error**|
|Abstract finite fibers|Finite-image/fiber API|`Set.Finite.of_finite_fibers`|Exact same building block|Pinned finite-fiber source|Finite-fiber name returned, **index=error**|

All three local calls were attempted but did not consult a healthy local index. Returned positive names were checked against the pinned source and native signatures; these index errors cannot establish absence. Remote indexes can differ from the pin. The source fallback also performed an untruncated full-name search; a native `exact?` closure probe was executed separately.

Pinned candidates include `Rat.den_dvd`, `Rat.num_div_den`, `Rat.reduced`, `Int.isCoprime_iff_gcd_eq_one`, `Set.Finite.of_finite_fibers` (Finite/Lattice:234), and `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational` (DiophantineApproximation/Basic:197). The latter is an exponent2 **rational-set** theorem, not the arbitrary suppliedκ pair theorem. `LiouvilleWith.exists_pos`, `.mono`, and `.frequently_lt_rpow_neg` use existential coefficient C, allow lower exponents via absorption, and exclude equality; `.irrational` requires `1<p`. In particular `liouvilleWith_one` holds for rational as well as irrational centers. None of these alone justifies identifying all three APIs. [Pinned source/hash inventory](../evidence/Roth.exists_reduced_approx/mathlib-inputs.json).

## Phase5.5 — three statement-shape checks

**Normal form:** rational values canonically use `Rat.num`/`Rat.den`; the current supplied-quality pair predicate remains meaningful. The compatible unrestricted statement deliberately preserves it. A proposed rational-form bridge would need actual denominator/coprimality recovery, not just equality of fractions; no unverified equivalence is claimed.

**Syntactic generality:** keep explicit Q₀ because the recursive caller supplies varying thresholds; drop `hκ` in the general theorem and offer a κ≤2 result requiring no `hinf`.

**Superfluous hypotheses:** `hκ` is globally unnecessary by the actual proof; `hinf` is unnecessary only in the quantified subcritical range. Irrationality is uniformly essential by native rational-center counterexample. No typeclass is silently dropped. **Overall: RESTATE-BEFORE-SHIP.**

## Phase6.0 — complete actual callers and closures

| Caller | Reference | Full actual verification |
|---|---|---|
|`Roth.exists_approximants`|Main:261, `choose ... using fun Q₀ ↦ exists_reduced_approx hα hκ hinf Q₀`|Complete original signature/body replayed with the full target proof locally inlined, including normalization helper; exact type agreement and standard axioms PASS.|

One explicit same-file call; zero external-to-file direct calls. Per the command's excluding-declaring-file convention, the internal-use count excluding that file is0. Inline-rederivation search found no independent proof of the same full reduced-unbounded result. This is not a dead-code inference: kernel audit confirms the sole direct value consumer, plus downstream chain through `exists_roth_approximants_aux`, `roth_of_isIntegral`, `roth`, `roth_rat`, and LeanEval `thueSiegelRoth`. No direct type consumer was found among the293 declarations. Source/caller details: [callers](../evidence/Roth.exists_reduced_approx/callers.json), [fresh lexical receipt](../evidence/Roth.exists_reduced_approx/source-search.json), [inline-search receipt](../evidence/Roth.exists_reduced_approx/inline-search.json), [full inline caller](../evidence/Roth.exists_reduced_approx/callers-executed.lean.txt), [raw caller receipt](../evidence/Roth.exists_reduced_approx/callers-receipt.json).

The canonical array is derived directly from tracked order with correct private modules; pre-execution and portable validators compare all293 names in exact order, not count alone. Runtime293 requested/unique/present/values are all293. [Accepted project-only transitive audit](../evidence/Roth.exists_reduced_approx/consumer-scope2-executed.lean.txt), [raw scope receipt](../evidence/Roth.exists_reduced_approx/consumers2-receipt.json), [consumer summary](../evidence/Roth.exists_reduced_approx/canonical-consumers.json). Traversal is explicitly restricted to canonical project/private constants; it does **not** traverse all mathlib. Lexical, direct kernel type/value, transitive project, and simp scopes remain distinct; no global simp-closure claim is made.

## Phase6 — composition and trust

1. `Rat.num_div_den` plus `Rat.reduced` supply equality and coprimality only; they do not bound original rational-value fibers or guarantee large reduced denominators.
2. `Set.Finite.of_finite_fibers` is the exact structural building block, but requires two substantive arithmetic premises. The full native arithmetic recovery proves those premises; calling our own generic theorem is not an existing mathlib replacement.
3. Dirichlet2 supplies the entire κ≤2 regime after actual pair transport and monotonicity. It does not supply arbitraryκ>2 approximants matching the input hypothesis.
4. Native bounded `exact?` and simp-only closure probes did not close the original arithmetic goal; the same example then closes by the complete nontrivial proof. This is supporting bounded search evidence, not a universal proof that no term exists.

**NOT-COMPOSABLE** under the≤3existing-call criterion. One caller alone is not a cost-based reason to erase the arithmetic API. [Exact composition probe](../evidence/Roth.exists_reduced_approx/composition-executed.lean.txt), [raw receipt](../evidence/Roth.exists_reduced_approx/composition-receipt.json).

The rational-center obstruction is independently native proved: [counterexample source](../evidence/Roth.exists_reduced_approx/counterexample2-executed.lean.txt), [raw receipt](../evidence/Roth.exists_reduced_approx/counterexample2-receipt.json). It proves both an infinite unreduced set and absence of every reduced solution beyond1, not just the existence of a repeated rational value.

All accepted proofs use only standard axioms `propext`, `Classical.choice`, `Quot.sound`; no new axiom, sorry, unsafe, native_decide, or resource-limit increase is accepted. Root's fresh declaration-specific authorization permits stable18 plus `Mathlib.NumberTheory.DiophantineApproximation.Basic`; no previous worker's import exception was inherited. [Authorization](../evidence/Roth.exists_reduced_approx/native-prefix-authorization.json).

Rejected attempts are immutable and separately classified: original isolated01 needed explicit set-membership normalization and produced recovered sorryAx, consumers01 used nonexistent Array.union, and counterexample01 needed pair-projection simplification and had unused ring warnings. None is accepted verification. Their exact sources/raw returns remain in the package. See [complete verification/attempt accounting](../evidence/Roth.exists_reduced_approx/verification.json).

## Phase7 — actionable upstream recommendation

**YES-but-generalise-first**, specifically remove exponent positivity and expose the unconditional subcritical result before shipping. The gap is the bridge from infinitely many supplied approximating pairs to unbounded **reduced** denominators: canonicalization, finite rational-value fibers, and local bounded-height finiteness must interact. Existing rational Dirichlet and finite-fiber APIs provide ingredients, while the verified arbitraryκ theorem and generic recovery are new proofs. This is mathematical content beyond rational reconstruction and beyond an existential-constant Liouville predicate.

Proposed home: **`Mathlib/NumberTheory/DiophantineApproximation/Basic.lean`**, adjacent to irrational rational approximant infinitude, with fixed-quality predicate unfolded or locally represented and reusable fiber helpers extracted. Proposed PR title: **`feat(NumberTheory): obtain arbitrarily large reduced fixed-quality approximations`**.

Group the decay/fiber support with already accepted YES `Roth.eventually_div_rpow_lt`; the normalization and finite-strip prerequisites may remain internal or use their separately assessed mathlib alternatives. This grouping was checked against [actual accepted-YES progress snapshot](../evidence/Roth.exists_reduced_approx/accepted-YES-snapshot.json). Do not bundle unrelated polynomial `main_lemma` merely because it also has an accepted YES verdict.

At the sole `exists_approximants` call, replace `exists_reduced_approx hα hκ hinf Q₀` by the unrestricted helper `... hα hinf Q₀`; keep full caller signature initially for compatible downstream adoption. The full original caller was actually inlined and tested; no shortened prefix or supplied desired conclusion stands in for that check.

Pre-PR checklist:

- `/generalise Roth.exists_reduced_approx`: retain the native unrestricted theorem and κ≤2 theorem; audit whether to expose the structural helper or keep it internal, without substituting a different approximation predicate.
- `/cleanup Roth/Main.lean Roth.exists_reduced_approx`: decompose rational fibers and normalization, choose mathlib names/import boundaries, and preserve strict threshold/coprimality.
- Reviewer candidates from fresh authorized pinned path history: **Andrew Hendel** (834e51690b,2026-05-12, DiophantineApproximation documentation); **Yaël Dillies** (483ba09b2e,2026-06-16, rational-coercion maintenance; d99d52c36b,2026-07-17, Set.ofPred migration in relevant paths). These are candidacy evidence, not a claim they reviewed this proposal. [Full actual git request/return](../evidence/Roth.exists_reduced_approx/reviewer-git.json). No invitations or external messages were sent.

## Phase8 — package and publication boundary

Full phase records, original/current types, source/pin hashes, full exact executed sources, raw accepted and rejected receipts, named literature channels, all15 formal cells, actual caller and canonical293 scope, fresh import authorization, current recursive manifest, portable validator, actual scratch/integrated validation receipts, and secret scan are included. Root independently reviews and publishes only after completed verification; this assessment does not change production code, pins, Git, overview, or progress.

The first preparatory integrated-layout validation exposed a validator path-filter bug: its temporary ancestor name was incorrectly treated as an excluded child. The failed raw receipt is retained in `validation-integrated-rejected.json`; the filter now uses paths relative to the evidence directory, and both actual layouts passed afterward. This did not involve Lean execution or production changes.
