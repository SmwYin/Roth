# `Roth.sum_inv_lt` — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** The strict square-root estimate is an unnamed auxiliary calculation in the Roth lattice proof. A verified broader theorem permits real `m > 1` and `2 * √m ≤ lam`. More reusable content is the symmetric reciprocal-grid bound under `1 < lam`, separated from the square-root comparison. Whether mathlib should expose that grid theorem, a general convex discrete endpoint theorem, or this corollary is an API-design question. No existing one-to-three-call mathlib replacement was established. This verdict is independently assessed, not inherited from declaration120 or the private helpers.

## Phase 0 — doctor

`Roth/Lattice.lean:68` resolves to a public theorem with no sorry. The entire220-line module and its sole source caller were read. Its module proves the lattice-count bound by last-coordinate induction. The reusable baseline is a successful2467-job build. All17 production-source/pin SHA256 values freshly match the shared baseline: [input checks](../evidence/Roth.sum_inv_lt/source-inputs.json), [build](../evidence/Roth.sum_inv_lt/baseline-build.txt). Production files remain unchanged.

The complete native elaborated type is:

```lean
Roth.sum_inv_lt {r m : ℕ} (hr : 1 ≤ r) (hm : 2 ≤ m) {lam : ℝ}
    (hlam : 2 * √↑m < lam) :
  ∑ j ∈ Finset.range (r + 1), (lam - 1 + 2 * ↑j / ↑r)⁻¹ <
    lam⁻¹ * (√(↑m - 1))⁻¹ * √↑m * (↑r + 1)
```

[Native original](../evidence/Roth.sum_inv_lt/sum-inv-lt-original-receipt.json) contains full type/check and standard axioms `[propext, Classical.choice, Quot.sound]`. The target's kernel `#print` body internally elides53225 characters at the MCP limit. This is not a complete printed proof-term claim: the [complete source](../evidence/Roth.sum_inv_lt/declaring-module.lean.txt), type, standard axioms and kernel-value existence are preserved. The independently checked canonical audit preserves exact293-entry order,293 unique names and293 existing values; its sole canonical direct consumer is the actual private `Roth.card_filter_weight_le_succ_aux` constant. [Audit](../evidence/Roth.sum_inv_lt/sum-inv-lt-audit-receipt.json).

## Phase 1 — mathematical comprehension

For integers `r ≥ 1`, `m ≥ 2`, and a real `λ > 2√m`, the sum of the reciprocals of `r+1` equally spaced points from `λ−1` to `λ+1` is strictly less than `(r+1)√m/(λ√(m−1))`. The grid is positive and symmetric about `λ`. Pairing each index with `r−j` bounds the sum by `(r+1)λ/(λ²−1)`; a separate strict square-root inequality enlarges that rational bound to the displayed expression.

Parameters: `r` controls the grid, `m` supplies the comparison factor, `lam` is the center. There are no explicit polymorphic types, universes, or typeclass arguments to weaken. The proof first obtains `λ>2`, positivity of `√(1−1/m)`, the identity `√(1−1/m)=√(m−1)/√m`, and `λ/(λ²−1)=λ⁻¹/(1−λ⁻²)`. It applies project-private `sum_inv_le`, applies project `sqrt_one_sub_inv_lt` through inverse monotonicity, and normalizes the right side. The proof is independent of `box`/`weight`; its actual project dependencies are those two arithmetic lemmas.

## Phase 2 — preliminary checks

**SMALL**: a supporting finite-sum inequality, neither a new structure nor a named main theorem. The theorem/lemma one-line-definition test is n/a; it introduces no definition barrier or instance. The public proof is about23 substantive lines and uses two nontrivial project lemmas. Its short final `calc` is not a mathlib-only composition.

## Phase 3 — exhaustive literature protocol

Exact requests, complete returned-response SHA256/byte counts, titles/URLs, access failures and original concise summaries are archived; full search/article text is not. Query strings below are verbatim.

| Channel | Actual request | Outcome and locator |
|---|---|---|
| General web: specific | `"Roth" "lattice" "sum" "lambda" reciprocal estimate Takloo Bighash Yin` | No exact independently named estimate identified; neighboring Roth/lattice material. |
| General web: general | `convex function equally spaced finite sum endpoint upper bound discrete Hermite Hadamard` | Equally spaced convex averages and discrete Hermite-Hadamard material; no exact square-root corollary. |
| General web: aliases | `reciprocal arithmetic progression sum pairing inequality lambda squared minus one` | Harmonic-progression/sum material, largely unrelated; the name is not a canonical theorem identifier. |
| ChatGPT mathematics | Availability inspected | `n/a: ask_chatgpt_math unavailable`; prepared historical/general-form question retained in optional-tool evidence. |
| Local references | Read `clean.tex` §6, lines1045–1135 | Exact statement at lines1096ff, as an unnamed step inside Lemma8. Even/odd pairing yields rational bound then square-root comparison. |
| nLab | `site:ncatlab.org/nlab "convex function"` | Search returns two-point convex-combination definition; direct page open failed400 unsupported XHTML. Search text is used only for the reported definition. |
| nCatLab | `site:ncatlab.org/ncatlab convex function Hermite Hadamard`; refined `site:ncatlab.org/ncatlab "convex" "Jensen"`; final `site:ncatlab.org/ncatlab "convex function" "finite sum"` | Initial results were nLab fallback; final targeted /ncatlab request explicitly returned empty. No distinct categorical version located. |
| Stacks | `site:stacks.math.columbia.edu convexity reciprocal sum inequality` | Returned semistable-reduction material, no pertinent theorem. This numerical finite-sum bound has no identified algebraic-geometric formulation. |
| MathOverflow | `site:mathoverflow.net discrete Hermite Hadamard inequality finite sum convex endpoints` | Question291617 concerns shifted convex Riemann-sum monotonicity, not this bound; opened lines32–34 and101. |
| Recent arXiv, last five years | `site:arxiv.org Hermite Hadamard discrete sum convex 2022 2023 2024 2025 2026`; refined `site:arxiv.org/abs/ "Hermite-Hadamard" "2025"` and `site:arxiv.org/abs/ "Hermite-Hadamard" "2022"` | Initial query returned older/irrelevant hits; refinement located2212.14796, submission2022-12-03, inside2021-10-27–2026-10-27 window. Weighted Hermite-Hadamard refinements, not the Roth threshold. |

Receipts: [general web](../evidence/Roth.sum_inv_lt/web0-metadata.json), [nCatLab/Stacks](../evidence/Roth.sum_inv_lt/web1-metadata.json), [MO/initial arXiv](../evidence/Roth.sum_inv_lt/web2-metadata.json), [refinements](../evidence/Roth.sum_inv_lt/web3-metadata.json), [primary opens/access failures](../evidence/Roth.sum_inv_lt/web4-metadata.json), [exact final nCatLab empty result](../evidence/Roth.sum_inv_lt/web5-metadata.json), [local source](../evidence/Roth.sum_inv_lt/local-literature.txt), [optional channel](../evidence/Roth.sum_inv_lt/optional-tool-availability.json).

Primary locators: [Furuichi–Minculete–Moradi2022](https://arxiv.org/abs/2212.14796), abstract lines8–16 and submission history26; [Monotonic Averages of Convex Functions](https://www.sciencedirect.com/science/article/pii/S0022247X00970872), search abstract only because open403; [nLab convex function](https://ncatlab.org/nlab/show/convex%2Bfunction), search definition only; [MO291617](https://mathoverflow.net/questions/291617/inequality-monotone-convergence-of-certain-riemann-sum). The recent matrix/set-valued variants are supplementary neighbors, not evidence for the exact scalar result.

Literature synthesis: the current source agrees exactly with the Lean statement. The broadly reusable concept is the convex chord/endpoint upper bound on symmetric finite averages, of which the positive reciprocal grid is a case. Continuous integral Hermite-Hadamard inequalities are related but are different statements. Neither weighted/matrix papers nor the nLab definition establish that this exact square-root threshold is a standard public theorem. Generality varies by scalar domain, grid/symmetric distribution, arbitrary convex functions versus reciprocal function, and separate numerical comparison factor.

## Phase 4a–4b — parameters and verified generality

| Parameter/hypothesis | Current role | Analysis and actual verification |
|---|---|---|
| `r : ℕ` | `r+1` equally spaced terms | Natural grid indexing is meaningful; arbitrary symmetric finite families belong to a different primary API layer, not a bare type replacement. |
| `hr : 1 ≤ r` | Positive spacing denominator | Cannot simply drop: native `r=0,m=2,λ=3` counterexample; Lean totalized division makes the remaining singleton too large. |
| `m : ℕ` | Comparison parameter | Integrality is unnecessary: verified `m : ℝ`, `1 < m`. The sum itself never depends on `m`. |
| `hm : 2 ≤ m` | `m−1>0` and `√m>1` | For natural `m`, equivalent to `1<m`; real generalization strictly broadens it. `m=1,r=1,λ=3` fails because inverse square root of zero is zero. |
| `lam : ℝ` | Positive reciprocal-grid center | Real square roots and order are part of this corollary. The rational intermediate theorem does not require square roots; a general ordered-field theorem is a further design candidate, not a verified claim here. |
| `hlam : 2*√m < lam` | Sufficient square-root comparison | Can weaken to `2*√m ≤ lam` while preserving the strict conclusion; native accepted. Some lower bound is essential: `r=1,m=2,λ=3/2` fails. No claim that the sufficient threshold is optimal. |
| Conclusion `<` | Strict comparison | Retained in the verified weakening. The rational grid bound uses `≤` and can have equality (endpoints); these are separate API layers. |

**STRICTLY NARROWER THAN STANDARD** in the verified real-parameter/weak-threshold direction; the exact paper helper remains in the narrower form. Proposed supported restatement:

```lean
theorem sum_inv_lt {r : ℕ} {m : ℝ} (hr : 1 ≤ r) (hm : 1 < m)
    {lam : ℝ} (hlam : 2 * √m ≤ lam) :
    ∑ j ∈ Finset.range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ <
      lam⁻¹ * (√(m - 1))⁻¹ * √m * (r + 1)
```

[Warm native proof](../evidence/Roth.sum_inv_lt/sum-inv-lt-real-receipt.json) uses the actual existing private grid theorem and the independently verified120 square-root bound. [Fully isolated proof](../evidence/Roth.sum_inv_lt/sum-inv-lt-raw-generalization-clean-receipt.json) independently reproves every helper using mathlib only and guards the missing project target. Both are clean and have standard axioms. These new helper proofs are evidence of reachability, not existing mathlib replacements. The first abstract reflection proof also exposed a cast-normalization mismatch; the accepted rerun adds `push_cast at hh` after reflection. Its rejected source/receipt is retained separately. The initial isolated attempt passed a `2<λ` term to the newly weakened `1<λ` helper; it was rejected, archived separately, and corrected with explicit arithmetic. No recovered failed proof is accepted.

The pair and rational-grid helper proofs also compile with `1 < lam` replacing `2 < lam`, unchanged otherwise. [Helper receipt](../evidence/Roth.sum_inv_lt/sum-inv-lt-helpers-receipt.json). This separates the genuinely sufficient positivity condition of the endpoint bound from the convenient threshold used by the lattice induction. [Counterexamples](../evidence/Roth.sum_inv_lt/sum-inv-lt-guards-receipt.json) compile independently.

## Phase 4c — all nine modern-idiom rows

| # | Question | Answer, proposed form and downstream consequence |
|---|---|---|
| 1 | Preambles to typeclasses | No: numerical inequalities `hr,hm,hlam` vary per application; global `Fact` instances would obstruct ordinary reuse. |
| 2 | Sequences to filters/nets | No: one fixed finite sum, with no limit or neighborhood. |
| 3 | Construction to universal property | No: produces a proposition, not a constructed object. |
| 4 | Closure predicate to bundled substructure | No: no subgroup/submodule/set closure data. `ConvexOn` is the existing appropriate predicate if the primary result becomes a convex theorem. |
| 5 | Weaker algebraic hierarchy | Corollary needs real square roots. The intermediate reciprocal-grid and convex-pair layer could use ordered-field/module API; only the real versions are mechanically verified here. |
| 6 | Higher category | No categorical construction or coherence law is present. |
| 7 | Concrete index | Yes at a distinct layer: a finite symmetric family/involution can replace the equally spaced grid when the pair bound is supplied. `Finset.sum_range_reflect` already supplies grid symmetry. Native `reflectedSum` verifies the separation; no general new index theorem is asserted to be existing mathlib. |
| 8 | Concrete-via-abstract diagnostic | Fires for the explicit reciprocal grid after the first bound: after the first `calc` line the summation/range expression occurs zero times; only scalar reciprocal/sqrt comparisons remain. The already project-private `sum_inv_le` expresses this separation. Native `inverseConvex`, `convexPair`, and `reflectedSum` test a more general organization. Their combination still needs concrete grid/endpoint normalization. |
| 9 | False-generalisation guard | Real `m` and a weak threshold preserve exactly the sum and strict inequality. A generic convex endpoint theorem preserves the intermediate content, while the particular sqrt comparison remains a separate corollary. Jensen's lower bound cannot be substituted for the desired endpoint upper bound. Omitting positivity/range hypotheses fails the native guards. No probability/integral theorem is mislabeled as the same finite sum. |

[Diagnostic and accepted native abstract experiment](../evidence/Roth.sum_inv_lt/sum-inv-lt-abstract-convex-clean-receipt.json). Modern organization is available: use the generic convex pair and reflection infrastructure to support other convex functions and symmetric sampling, then specialize to positive reciprocals and finally the numerical sqrt factor. This is a concrete downstream API benefit. It does not decide whether mathlib wants the special corollary; cost is not used to downgrade the verdict.

## Phase 4.5 — infrastructure risk

n/a: theorem introduces no definitions, classes, instances, coercions or reducibility declarations. Consequently the six definition-only risks—typeclass diamond, reducibility leak, noncanonical unfolding, instance-priority collision, universe-polymorphism constraint, coercion ambiguity—do not arise from adding this proposition. No fabricated instance/coercion probe is applicable. A future generic API should continue to use the existing `ConvexOn`/`Finset` infrastructure.

## Phase 4.6 — all five proof-strategy rows

| # | Strategy question | Answer |
|---|---|---|
| 1 | Topology: epsilon-delta versus filters | n/a: no topology argument. |
| 2 | Algebra: elements versus subobject inclusion | n/a: numerical order inequality, no subobjects. |
| 3 | Analysis: sequences versus nets | n/a: no convergence. |
| 4 | Category theory: construction versus universal property | n/a: no construction. |
| 5 | Helpers mathlib should have | Candidate: convex symmetric-pair endpoint bound and finite symmetric-average bound; alternatively the positive reciprocal rational-grid theorem. Existing `convexOn_zpow`, `ConvexOn`'s chord law and `sum_range_reflect` supply foundations. Native new proofs identify exactly what remains. |

**REFACTOR-RECOMMENDED** for upstreaming: decide the generic endpoint API first, derive the rational reciprocal bound, then keep or expose the square-root corollary according to actual audience. The current parity-free reflection strategy is mathematically idiomatic and cleaner than paper even/odd casework. This recommendation concerns API organization, not missing mathematical justification or an expense-based objection.

## Phase 5 — actual five methods on three forms

Forms searched: current reciprocal-grid/sqrt estimate; literature-standard convex finite equally spaced endpoint average; abstract finite symmetric-pair sum. [Complete exact formal requests/raw receipts](../evidence/Roth.sum_inv_lt/formal-search.json) and [complete source commands/outputs](../evidence/Roth.sum_inv_lt/source-search-raw.json).

| Method | Current | Literature-standard | Abstract |
|---|---|---|---|
| Finder | Reciprocal progression and sqrt comparison query; ADE/floor-power hits are different | Convex finite endpoint average/Hermite-Hadamard query; secant/Jensen candidates | Pair bound plus involution query; `sum_involution`/fiber-sum results |
| Loogle | `Finset.sum, Real.sqrt, (_⁻¹)`; central-limit results are different | `ConvexOn, Finset.sum, (_ ≤ _)`; Jensen results | `Finset.sum, Finset.sum, (_ ≤ _)`; sum-permutation/bijection results |
| LeanSearch | Current progression/sqrt query; summability/geometric-series hits are different | Convex endpoint-average query; `ConvexOn.le_on_segment'` and Jensen | Involution-pair query; sum-bijection API |
| `rg` | Full mathlib tree for qualified/current names and lambda-sqrt form: no text hit | Convex files for endpoint/convex/trapezoid/Hermite-Hadamard; chord/zpow/Jensen matches | Big-operator files for reflection/involution/cardinal sum; generic reindexing and order |
| local | `sum_inv`: project/scratch hits excluded as replacements; mathlib `sum_inv_index` is only reindexing | `convexOn_inv`: empty | `sum_range_reflect`: empty |

All three local responses have `index: unavailable`; empty results are not evidence of absence. External search revisions may differ from the project pin. The supplementary exact reciprocal-convexity Finder query located `convexOn_zpow`, whose pinned source at `Mathlib/Analysis/Convex/Mul.lean:177` and actual native specialization were checked. [Supplementary receipt](../evidence/Roth.sum_inv_lt/supplementary-convex-search.json).

Pinned positive candidates:

- `convexOn_zpow` specializes integer exponent `−1` to convexity of reciprocal on `Ioi 0`; native `inverseConvex` verifies this existing-call specialization.
- `ConvexOn.le_on_segment'`, `Mathlib/Analysis/Convex/Function.lean:642`, and `ConvexOn`'s two-point chord inequality bound a point by endpoint interpolation; two instances plus algebra prove the new `convexPair`.
- `Finset.sum_range_reflect` reindexes the sum. `sum_le_sum`, `sum_add_distrib`, `sum_const`, and cardinal/cast normalization then prove the new reflected sum bound.
- Jensen's `ConvexOn.map_sum_le` has a convex function of an average on the left; it is not this upper bound on an average of function values. `sum_involution` is cancellation under opposite pairs, not a numerical bound on positive reciprocal pairs.
- `Real.sqrt_div'`, `Real.sqrt_lt'`, inverse-order rules and ordinary field algebra handle comparison/normalization after the rational bound; they do not supply that bound.

Conclusion: positive partial APIs found; no direct replacement established. All five search methods ran, with their limitations recorded. Three native `exact?` experiments on the current, rational-grid and abstract pair-bound forms failed cleanly as search experiments. They are not a proof of global absence. [Rejected search receipt](../evidence/Roth.sum_inv_lt/sum-inv-lt-direct-search-receipt.json).

## Phase 5.5 — three statement-shape checks

**Normal form.** Equivalent RHS spellings include `(r+1)*λ⁻¹/√(1−1/m)`, `(r+1)√m/(λ√(m−1))`, and the existing factored product. The `hsqrt`/`hlam'` identities and final `field_simp` in the actual native broader proof verify the relevant bridge. No canonical named mathlib theorem for the complete estimate was established. Prefer the rational-grid bound as primary normal form, with a sqrt corollary only when needed. RHS convention is n/a to an equivalence; inequality orientation already places the bound on the RHS.

**Syntactic generality.** Real `m` eliminates irrelevant casts; weak `2√m≤λ` makes boundary cases immediately usable. `range (r+1)` agrees with the sole caller's fiber sum, so no `Icc`/`Fin` conversion is needed there. Division/one-square-root spellings are mathematical alternatives; the existing factored shape helps the caller cancel `√n`. Actual full caller replay replaces only the theorem call by the real-parameter version and retains the rest of its proof. [Caller receipt](../evidence/Roth.sum_inv_lt/sum-inv-lt-consumer-receipt.json).

**Superfluous-argument audit.** `r` and `hr` are necessary for this grid; `m` is needed only for the comparison but need not be integral; `hm` becomes `1<m`; `lam` is essential; a lower bound on `lam` is essential but its strictness at `2√m` is superfluous. There are no explicit typeclasses. Each claim is backed by the successful weakening or explicit false-drop guards.

Overall **RESTATE-BEFORE-SHIP**: if the corollary ships, use the verified real parameter and weak threshold. Decide the reusable endpoint/rational API independently.

## Phase 6.0 — callers and inline audit

| Caller | Usage | Refactor consequence |
|---|---|---|
| `Roth/Lattice.lean:173`, private `card_filter_weight_le_succ_aux` | `have hs := sum_inv_lt (r := R) (m := n + 1) hr (Nat.succ_le_succ hn) hlam` | Verified broader call supplies real `m=(n+1:ℕ)`, proof `1<m` from `hn`, and `hlam.le`; following cast simplification/cancellation is unchanged. |

Counts: one explicit source caller in the declaring file; zero external-to-file source callers; zero identified external-library uses. Native exact canonical dependency scan independently confirms the same actual private consumer. This is not a claim about full kernel/simp transitive closure. The local inline audit finds the rational helper and later fiber sums, not another independently rederived complete sqrt estimate. No simp attribute is attached to this target. Its single use is an audience-narrow signal, not sufficient for a NO verdict or dead-code claim; it supports the public lattice-count theorem.

## Phase 6 — actual composition experiments

1. Current-form mathlib-only `exact?`: failed. Rational-grid `exact?`: failed. Abstract reflected-pair `exact?`: failed. They use minimal mathlib imports, guard missing `Roth.sum_inv_lt`, and are archived as rejected searches, without an absence inference.
2. Convex route: the existing `convexOn_zpow (-1)` supplies reciprocal convexity in one `simpa` specialization. This is a partial positive. Getting pair and sum upper bounds needs two chord applications, algebra and reflection normalization, as shown in accepted new `convexPair`/`reflectedSum` proofs. These are new lemmas, not existing-call replacement evidence.
3. Original rational route: the isolated accepted proof has a genuine denominator-positivity/field inequality, finite index bound, reflected-sum manipulation and scalar square-root comparison. Replacing its two project helpers by names would hide the mathematical work. A parent project lemma is not an existing mathlib building block.
4. Scalar normalization: `rw [hsqrt]; field_simp` is necessary proof glue after the comparison. A hypothetical closing `simp [defs...]` would be a **trivial simp composition**, explicitly BORDERLINE under Phase6b; no such whole-theorem closing simp proof was established here.

**NOT-COMPOSABLE** by any established one-to-three existing-call term. Failed search is not proof of absolute nonexistence; the accepted independent proof makes the actual residual work reviewable.

## Phase 7 — verdict and actionable API questions

**BORDERLINE-needs-human**, because the exact helper is an unnamed single-use Roth comparison, whereas the reusable finite convex endpoint/rational-grid content is a plausible broader API. This is not uncertainty about truth: both the real-parameter strict corollary and positive-grid bound were verified natively. It is not cost-based: completing a generic convex theorem is worthwhile if that API is desired. Literature/search/composition evidence does not justify NO-mathlib-has-it or a one-to-three-call NO-composable claim. Verified generality also rules out YES-add-as-is.

1. Should mathlib expose the `1<λ` rational reciprocal-grid endpoint bound as a standalone reusable analysis theorem?
2. Should a generic `ConvexOn` symmetric discrete-average endpoint bound be the primary API, with the reciprocal-grid result as its specialization?
3. Should the `m`/square-root comparison corollary remain in `Roth/Lattice.lean` unless a second independent use appears?
4. If that corollary is exposed, should it use the verified real `m>1` and nonstrict `2√m≤λ` statement?

Conditional route: a generic discrete convex averaging theorem could live in a proposed `Mathlib/Analysis/Convex/Discrete.lean`, importing existing convex and big-operator infrastructure; final placement/import layering needs maintainer agreement. Reciprocal convexity itself is already in `Convex/Mul.lean` through `convexOn_zpow`. Keep the sqrt corollary in the downstream project while resolving those choices. No production edit, deletion, PR or upstream submission is implied by this read-only assessment. No related accepted YES declaration is presumed from its name; the arithmetic120 assessment is BORDERLINE and private121–122 were SKIP, not grouping approvals.

## Phase 8 — verification and handoff

[Verification ledger](../evidence/Roth.sum_inv_lt/verification.json) distinguishes accepted clean source/receipts from rejected direct-search and initial generalized-proof attempts. Native target and exact293 canonical audit, broadened warm theorem, independent mathlib-only theorem, weaker rational helpers, false-drop counterexamples, abstract convex/reflection probes and the actual sole caller replay are verified. Standard axioms only; no sorry, unsafe, new axioms, native_decide or raised limits in accepted sources. Canonical private names are generated from tracked metadata, not guessed numeric spellings. Persistent-disk receipts contain historical info, so target assertions use their fresh native-region start lines while full-file errors/warnings/axiom checks remain enforced.

All requested phases are complete. Upstream design questions are intentional BORDERLINE outcomes, not unresolved verification. The portable [validator](../evidence/Roth.sum_inv_lt/validate.py) checks the current copy manifest,17 source/pin hashes, exact293 canonical order, actual successful native receipts, separate rejected experiments, all methods/forms, literature metadata and portable report links. Root independently reviews before integration.
