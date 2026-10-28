# Roth.Θ_lt — full mathlibable assessment

**Canonical228; BORDERLINE-needs-human.** The substantive contribution is Roth's uniform arithmetic index estimate (original Lemma7), not the supremum operation. Keep the named endpoint in `Roth/Theta.lean`. A fresh successful full proof weakens the final natural weight from≥3 to≥1; this carries newly proved stronger finite-sum/Lemma6 ingredients and changes several private induction interfaces. It is not an existing mathlib replacement. The bounded upstream questions below concern API grain and audience, and do not block this completed read-only assessment. No production changes were made.

## Phase0 — baseline and provenance

The declaration resolves at `Roth/Theta.lean:962–981`, the final declaration of the985-line module. All17 production/pin hashes match baseline99f19fda4b3cbee38fc0d31af76075834f5cc265, on branch `ramin-cleanup`, Lean4.34 and pinned mathlib5ed296… . The original reusable build was clean. The mandatory fresh file-end **full** `/Users/ramin/.elan/bin/lake build` also passed exit0,2467 jobs,5.798706792 seconds; stderr is empty. All17 inputs were freshly rechecked after that build. Exact command, duration and log hashes are in [full-build.json](../evidence/Roth.Θ_lt/full-build.json), [stdout](../evidence/Roth.Θ_lt/full-build.stdout.txt), [stderr](../evidence/Roth.Θ_lt/full-build.stderr.txt), and [inputs](../evidence/Roth.Θ_lt/inputs.json).

The [complete declaring module](../evidence/Roth.Θ_lt/source-module.lean.txt), [canonical metadata](../evidence/Roth.Θ_lt/target-metadata.json), and [full caller module](../evidence/Roth.Θ_lt/caller-module.lean.txt) were read. Original whole-module replay, complete direct kernel type, standard axioms and exact ordered293 private-aware present/value audit passed without warning/error. The guard was run before each canonical-source execution. [Original source](../evidence/Roth.Θ_lt/original-executed.lean.txt), [raw original receipt](../evidence/Roth.Θ_lt/original-receipt.json), and [native type](../evidence/Roth.Θ_lt/native-type.json) retain that evidence. The first cold diagnostic response was partial and is separately excluded. The full statement below comes directly from `ci.type`, rather than parsing the `#print` proof display. The original proof display has4,479 characters and contains no elision marker; the complete written proof is archived separately.

## Phase1 — mathematical content

Let m=n+1 be positive, and let r,q be natural degree bounds and denominators. Suppose δ>0, the final degree is at least3, successive degrees satisfy rᵢ₊₁≤δrᵢ, log q₁≥m(2m+1)/δ, and all rⱼlog qⱼ≥r₁log q₁. Then every nonzero integer polynomial of coordinate degrees≤r and coefficients bounded by q₁^(δr₁), evaluated at rational tuples with reduced denominators q, has normalized index uniformly small: their supremum Θ is strictly less than10^m δ^(2^(-m)). The conclusion holds for every δ>0; no δ upper bound is assumed. The small-δ induction and large-δ cardinality comparison are separate branches.

Complete native type:

```lean
∀ (n : ℕ) {δ : ℝ},
  0 < δ →
    ∀ {r q : Fin (n + 1) → ℕ},
      3 ≤ ↑(r (Fin.last n)) →
        (∀ (i : Fin n), ↑(r i.succ) ≤ δ * ↑(r i.castSucc)) →
          (↑n + 1) * (2 * (↑n + 1) + 1) / δ ≤ Real.log ↑(q 0) →
            (∀ (j : Fin (n + 1)), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
              Roth.Θ (↑(q 0) ^ (δ * ↑(r 0))) q r < 10 ^ (n + 1) * δ ^ (1 / 2) ^ (n + 1)
```

There are no generalized typeclass parameters in this public endpoint: `Fin (n+1)` supplies finiteness and decidable equality. The named parameters n,δ,r,q and five hypotheses (includingδ positivity) have the roles just stated. The actual proof inducts on n, generalizing δ. At n=0 it uses `theta_lt_base_aux` and `theta_denominators_one_lt_aux`, or `theta_lt_of_large_delta_aux`. The successor uses `theta_lt_succ_aux` in the small-δ range, otherwise the same large-δ helper. The successor helper transports through `Θ_equiv` to `Θ_option_le`, bounds its finite maximum by `theta_phi_lt_aux`, and the latter uses `lem6M_lt`, `theta_scaled_unique_le_aux`, `theta_prefix_lt_aux`, `theta_delta_succ_lt_aux`, `lem7_Φ_bound` and `lem7_numeric`. This is the quantitative polynomial-height argument; `Nat` induction and finite supremum rules organize it but do not prove its arithmetic premises.

## Phase2 — preliminary checks

**BIG:** this is a module-listed main result and Roth's named Lemma7, feeding Roth's main lemma. One-line-definition test is **n/a: theorem**, not data, instance or abbreviation. The written declaration spans20 lines, with a16-line proof including its opening `by`, and delegates substantial verified project results; a short displayed proof is not evidence of≤3 existing mathlib calls.

## Phase3 — exhaustive literature

Only exact requests, response hashes/byte counts/status, clean locators and original concise summaries are archived. No complete web bodies are persisted. Publication/crawl labels are not treated as mathematical dates or evidence of current novelty.

| Channel | Actual request/evidence | Finding |
|---|---|---|
| General web, specific | `Roth "Theta" "10" "index" polynomial lemma 7` in [general web receipt](../evidence/Roth.Θ_lt/web-general.json) | Arithmetic index lemma context; distinguish additive-combinatorial Roth. |
| General web, broader | `Roth index theorem bounded height multivariate polynomial rational points`, same receipt | Integer coefficient height, rational evaluation, normalized index. |
| General web, aliases | `Roth lemma polynomial index bound Dyson lemma Thue Siegel`, same receipt | Dyson's algebraic two-variable estimate is related but not the same full arithmetic endpoint. These are three distinct actual queries. |
| Additional named/quantitative web | Three further queries in [aliases receipt](../evidence/Roth.Θ_lt/web-aliases.json), including `Roth "lemma 7" "index" "polynomials"` | Finds the exact publisher primary source and Lemma7. |
| ChatGPT mathematics | n/a: `ask_chatgpt_math` unavailable | No simulated second opinion; other channels executed. |
| Local source | [clean.tex excerpt](../evidence/Roth.Θ_lt/local-literature.txt), [hash/lines](../evidence/Roth.Θ_lt/literature-source.json), Lemma `roth:lem7`, equations19–23 | δ<1/m, r_m>10/δ, strict ratios/log threshold, weak balance. Current Lean already strengthens these. |
| nLab | [actual nLab request](../evidence/Roth.Θ_lt/nlab.json) | Analytic/operator index and general polynomial/rational-zero pages are not this arithmetic index law. One visibly truncated returned prose URL omitted without guessing. |
| distinct nCatLab | [actual `site:ncatlab.org/ncatlab` request](../evidence/Roth.Θ_lt/ncatlab.json) | Results came from `/nlab`, outside the requested namespace; no exact in-namespace hit identified. |
| Stacks | [actual Stacks request](../evidence/Roth.Θ_lt/stacks.json) | Krull height, projective curves and related algebraic geometry; no exact quantitative arithmetic endpoint identified. |
| MathOverflow | [actual MO request](../evidence/Roth.Θ_lt/mathoverflow.json) | Questions431381 and332190 provide discussion of small-index arguments and the role of Roth's lemma; not a primary proof of these constants. |
| recent arXiv | [five-year query](../evidence/Roth.Θ_lt/arxiv.json), [two narrow retries](../evidence/Roth.Θ_lt/arxiv-retry.json), each `after:2021-10-28 before:2026-10-29` | Mostly additive Roth/unrelated heights; narrower results also irrelevant. No exact recent alternative identified; not proof of absence. |
| Supplementary primary access | [ICM1958 failed open](../evidence/Roth.Θ_lt/primary.json) | Direct74.7MB volume open fails400; no full-volume reading claimed. |
| Primary publisher source | [publisher PDF access](../evidence/Roth.Θ_lt/primary-extra.json), [targeted Lemma7 access](../evidence/Roth.Θ_lt/primary-lemma.json) | K.F.Roth, *Rational approximations to algebraic numbers*, Mathematika2(1955),1–20, Lemma7 p12, proof pp12–13. OCR corruption disclosed and cross-checked with local source and search-visible math. |

The primary source is [Roth1955, publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/div-class-title-rational-approximations-to-algebraic-numbers-div.pdf). Its Lemma7 is the exact10^mδ^(2^-m) estimate, not merely a theorem sharing Roth's name. Its hypotheses are sufficient rather than a claim of optimality. The production endpoint permits allδ>0, weak ratios/log thresholds and final weight≥3 instead of>10/δ. Fresh scratch evidence below further permits≥1. Literature formulations using number-field heights, general places or Dyson's estimates change the surrounding representation/theorem, so no unverified general-field replacement is claimed.

## Phase4a–b — every generality dimension

| Parameter/hypothesis | Examination and result |
|---|---|
| `n : ℕ`, dimension n+1 | Positive finite dimension is intended. `Fin(n+1)` makes first/last/successor coordinates explicit. Arbitrary finite nonempty ordered families require a chosen enumeration and a proved transport; not a free binder weakening. |
| `δ : ℝ`, `0<δ` | No upper bound already. Positivity is used in log and power comparisons. `deltaZeroGuard` compiles a genuine n=0 counterexample if onlyδ≥0: q=1,r=3 meet all other public hypotheses (division by0 gives0), but nonnegativeΘ cannot be<0. |
| final weight≥3 | **Not maximal. Fresh whole-module proof with≥1 passed.** Equivalently natural final weight>0, separately compiled as `positiveLast`. Only local positivity and induction-threshold occurrences were changed; numerical coefficient3 in the Φ and square bounds stays3. |
| natural `r` | Integer coordinate degrees, finite derivative ranks, factorials and finite intervals are used. Real reciprocal weights can represent index differently but would require reworking the height/determinant bounds. No full real-degree extension verified. |
| natural `q` | Rational reduced denominators and primitive integral linear factors supply arithmetic coefficient estimates. Replacing q with arbitrary reals changes that arithmetic content. Positivity of all denominators is already derived, not a public premise to delete. |
| `hratio` | Already weak≤, used to get antitonicity whenδ<1, bound derivative weights and transfer induction. In the large-δ branch it is unused because the cardinality bound suffices; this does not remove it uniformly inδ. |
| `hq1` | Already weak≤, supplies denominator>1 and absorbs factorial/determinant heights in smallδ. The n=0 theorem `oneVariable` separately compiles with just q₀>1 and r₀>0; this base-case weakening is not asserted as a uniform all-dimension replacement. |
| `hqr` | Already weak balance. Used for the one-variable term at the last denominator and prefix induction; it is automatic at j=0. Could be syntactically restricted to nonzero coordinates by a proof of the omitted reflexive case, but no mathematical weakening is claimed. |
| integer coefficient ring and real bounds | `Θ` fixes these parent interfaces. Integer nonzero coefficient magnitude≥1 and primitive-factor arithmetic matter. Normed fields/number fields and valuations need a new representation and height API, not an automatic hierarchy weakening. |
| strict conclusion and constants | Strictness is obtained with slack and a finite maximum. No optimal10 or exponent claim. Prior independent numeric improvements do not establish joint extensions here. |
| implicit instances/universes | No public class binder or universe parameter to remove; finiteness is used in index, degree bounds and induction. |

Verified sources: [broader whole module](../evidence/Roth.Θ_lt/broader-executed.lean.txt), [clean broader receipt](../evidence/Roth.Θ_lt/broader-receipt.json), [shapes and counterexample source](../evidence/Roth.Θ_lt/shapes-executed.lean.txt), [clean shapes receipt](../evidence/Roth.Θ_lt/shapes-receipt.json). The≥1 proof includes the existing scratch213/214 strengthened finite-sum /2 argument and its changed Lemma6 numeric proof, which are new proofs, **not pinned mathlib API**. No necessity claim for≥1 or other retained quantitative hypotheses is made; zero final weights are not refuted. Generality verdict: the production statement is demonstrably narrower than a verified sufficient positive-weight interface, while already broader than the original publication. No maximality claim. This is a multi-lemma interface change, not evidence for a mechanical one-binder upstream PR.

## Phase4c — all nine modern-idiom checks

| # | Question | Answer, reformulation and consequence |
|---|---|---|
| 1 | Typeclasses instead of explicit hypotheses | No: numerical inequalities at this point in an argument should remain hypotheses; manufacturing instances would obscure δ/r/q choices. |
| 2 | Filters/nets | No: finite-degree quantitative inequality, no convergence. |
| 3 | Universal property | No: no constructed universal object in this endpoint. |
| 4 | Bundled substructures | No: nonzero bounded-height polynomials are not a submodule under arbitrary addition/scaling. A finite bounded family interface may aid enumeration but needs proof and is not a substructure replacement. |
| 5 | Algebraic hierarchy | Parent fixesℤ coefficients andℝ analytic bounds; coefficient discreteness and logs/powers are substantive. No verified general-ring endpoint. |
| 6 | Higher category | No categorical content or concrete downstream benefit. |
| 7 | Concrete finite index | A finite family with a chosen enumeration could use `Θ_equiv`; ordered successive growth must still be expressed and transported. Proposed future API question, not executed full arbitrary-family generalization. |
| 8 | Concrete-via-abstract diagnostic | Bare `Θ` has zero occurrences in the endpoint proof body; the diagnostic fires syntactically. Inspection shows base/successor helpers each encode the same specific arithmeticΘ bound. Abstracting them produces induction with supplied arithmetic base/step premises, not an abstract theorem proving those premises. The native independent order-transport theorem compiles and demonstrates precisely that boundary. No claim of a generic sSup quantitative replacement. |
| 9 | False-generalization guard |≥1 and natural>0 preserve the same index, coefficient family and conclusion and compile. Replacing arithmetic denominators by real parameters or using arbitrary sSup without the polynomial arithmetic premises would change/erase content, so these are rejected as full replacements. |

Modern-idiom verdict: generic order transport is available already, and a coordinate-free presentation is a possible future organizational choice. There is no verified new abstract theorem that alone supplies the full arithmetic estimate; no categorification or general-field claim is used to determine the verdict.

## Phase4.5 — infrastructure risk

Theorem: all six definition-introducing risks are n/a. It creates no typeclass diamond, reducible data definition, new unfolding rule, instance priority, data universe constraint, or coercion instance. Existing parent representation questions are reviewed separately and do not turn this theorem into an instance declaration.

## Phase4.6 — all five proof-strategy rows

| # | Check | Result |
|---|---|---|
| 1 | ε–δ versus filters | No topological argument. |
| 2 | Elements versus ideals/submodules | Bounded integral coefficients and separated polynomial factors are the content; the admissible nonzero-height family is not an ideal. |
| 3 | Sequences versus limits | No sequence convergence. |
| 4 | Construction versus universal characterization | No categorical construction. |
| 5 | Missing helpers mathlib should have | Candidate reusable gaps are generalized Wronskian separation, determinant coefficient bounds, and weighted index/height inequalities. Existing csSup and finite-sup lemmas are sufficient for order transport. The final recursive arithmetic endpoint's upstream packaging is undecided. |

The dimension-induction strategy matches the primary proof. Refactor recommended before any contribution: expose the positive-weight ingredient chain coherently, retain named arithmetic stages and distinguish reusable determinant/height API from the specialized10^m endpoint. This is mathematical API organization, not a cost-based verdict.

## Phase5 — all15 actual formal-method/form cells

Each cell retains the exact query/request and full raw formal-search receipt. External index revisions can differ from the pin; local search reported `warming` and also returned scratch declarations. Neither is a proof of absence.

| Form | Finder | Loogle | LeanSearch | rg | local name |
|---|---|---|---|---|---|
| Current Θ_lt | [receipt](../evidence/Roth.Θ_lt/search-current-leanfinder.json): additive Roth near-misses | [receipt](../evidence/Roth.Θ_lt/search-current-loogle.json): no exact name | [receipt](../evidence/Roth.Θ_lt/search-current-leansearch.json): root/coefficient/additive bounds | [receipt](../evidence/Roth.Θ_lt/search-current-rg.json): full untruncated target pattern, zero hits | [receipt](../evidence/Roth.Θ_lt/search-current-local_search.json): project target only, warming |
| Literature arithmetic index/height | [receipt](../evidence/Roth.Θ_lt/search-standard-leanfinder.json): Chevalley/additive bounds | [receipt](../evidence/Roth.Θ_lt/search-standard-loogle.json): log/type pattern no hit | [receipt](../evidence/Roth.Θ_lt/search-standard-leansearch.json): Schwartz–Zippel, Mahler height | [receipt](../evidence/Roth.Θ_lt/search-standard-rg.json): exact partial candidates | [receipt](../evidence/Roth.Θ_lt/search-standard-local_search.json): project/scratch index bounds, warming |
| Abstract weighted-order/sup bound | [receipt](../evidence/Roth.Θ_lt/search-abstract-leanfinder.json): weightedOrder coefficient witness law | [receipt](../evidence/Roth.Θ_lt/search-abstract-loogle.json): finite-sup strict laws | [receipt](../evidence/Roth.Θ_lt/search-abstract-leansearch.json): Real.sSup_le and csSup_le | [receipt](../evidence/Roth.Θ_lt/search-abstract-rg.json): order/weighted-order candidates | [receipt](../evidence/Roth.Θ_lt/search-abstract-local_search.json): finite-sup laws, warming |

Pinned source statements were read: `csSup_le` in `Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:201`; `csSup_Iio` at326; `Set.Finite.csSup_lt_iff` in `Mathlib/Order/ConditionallyCompleteLattice/Finset.lean:71`; `MvPolynomial.schwartz_zippel_sup_sum` in `Mathlib/Algebra/MvPolynomial/SchwartzZippel.lean:72` counts roots in finite product sets, rather than bounding a weighted vanishing index at prescribed rational denominators. `ChevalleyThm.MvPolynomialC.numBound` concerns complexity of constructible images, not this arithmetic height law. NumberTheory's LiouvilleWith docstring mentions Thue–Siegel–Roth but does not provide this lemma; [topic grep](../evidence/Roth.Θ_lt/mathlib-topic-search.json) records the whole search. `Height.mulHeight/logHeight` index types concern finite coordinates of heights. Additive Roth number results solve a different problem.

Fresh [isolated exact18-import source](../evidence/Roth.Θ_lt/isolated-executed.lean.txt) and [clean raw receipt](../evidence/Roth.Θ_lt/isolated-receipt.json) check pinned positive candidate signatures and prove actual generic strict transport. The same source reconstructs Taylor translation with `MvPolynomial.aeval`, the normalized index, the bounded integer family and its supremum without importing Roth; `#check_failure Roth.Θ_lt` guards independence. One bounded full-goal `exact?` inside `fail_if_success` fails to supply the arithmetic endpoint under its real hypotheses; the wrapper closes with `True`. This is evidence about that attempted route, not a proof no possible mathlib proof exists. No resource limit was raised and no exhausted broad search was repeated. The initial use of project-only `MvPolynomial.taylor` and associated warnings is retained as rejected and corrected with its actual underlying aeval construction.

## Phase5.5 — statement shape

**Normal form:**Θ as sSup of the index family and pointwise index bounds are the two natural forms. The fresh `individualIndex` theorem derives the pointwise estimate using `index_le_Θ` and the broader endpoint. `Θ` re-aims at existing sSup, and normalized index may be represented by `AddMonoidAlgebra.infDegree`/`MvPowerSeries.weightedOrder` after bridges. Existing supremum/weighted-order laws do not supply the full height-dependent uniform small bound. No orthogonal equivalence is proposed; normal form is OK.

**Syntactic generality:** tested≥1 real cast versus0<natural last degree, a pointwise endpoint, and the n=0 form with justq₀>1. All compile. For present callers, retain the supremum endpoint and use natural positivity if the full strengthened ingredient stack is adopted. Future ordered-family enumeration is a separate design decision.

**Superfluous argument audit:** n fixes dimension, δ determines the height and bound, r and q occur inΘ and the hypotheses; positivity ofδ is necessary (native counterexample), while≥3 is stronger than necessary (native≥1 proof). Each remaining numerical premise is used in the small-δ arithmetic proof; the large-δ branch deliberately needs none of them. No omitted public typeclass exists. No retained premise is advertised as necessary merely because the present proof uses it. Overall: **RESTATE-BEFORE-SHIP** if contributing the strengthened interface; no production restatement in this assessment.

## Phase6.0 — exact callers and inline audit

[Ignore-independent source search](../evidence/Roth.Θ_lt/source-search.json) and [tracked git-grep cross-check](../evidence/Roth.Θ_lt/tracked-source-search.json) agree. Beyond the declaring header/docstring and declaration there is **one application occurrence, one source caller, one external-to-file module**:

| Caller | Use and verified effect |
|---|---|
| `Roth.theta_lt_eta_of_sq_log_bound_aux`, `Roth/MainLemma.lean:671–690`, application687 | Derivesδ>0 and the stronger log bound fromδm≤1 andδ²logq₁≥2m+1, converts reverse-last/adjacent ratio hypotheses, appliesΘ_lt, and unfolds eta. Complete caller body read. |

The fresh ordered canonical audit finds exactly the direct kernel-value consumer `_private.Roth.MainLemma.0.Roth.theta_lt_eta_of_sq_log_bound_aux`; [consumer list](../evidence/Roth.Θ_lt/canonical-consumers.json). This is a direct canonical expression audit, not transitive/simp dependency closure. `exists_auxiliary_polynomial_with_index_gap_aux` subsequently calls that helper and obtains the strict gap used by `main_lemma`; it is not a directΘ_lt call.

[Inline-pattern search](../evidence/Roth.Θ_lt/inline-audit.json) finds no independent rederivation of the full theorem. The eta helper packages its application; it does not bypass the arithmetic bound. This is live code. Complete [broader-to-original caller source](../evidence/Roth.Θ_lt/callers-executed.lean.txt) and [clean receipt](../evidence/Roth.Θ_lt/callers-receipt.json) replay the entire MainLemma module against≥1 with its original caller statement preserved. The explicit `Theta228Broad.bridge` (rfl) identifies the replayΘ with productionΘ; the original≥3 last-weight premise supplies≥1 by natural arithmetic. Complete [actual inline source](../evidence/Roth.Θ_lt/inline-executed.lean.txt) and [clean receipt](../evidence/Roth.Θ_lt/inline-receipt.json) instead insert the exact original endpoint body as a local `endpoint` inside the actual caller and replay all MainLemma declarations. This verifies possible inlining, without pretending project arithmetic helpers are mathlib building blocks.

## Phase6 — actual composition experiments and parent re-aim

1. The native independent generic theorem is `(csSup_le hS hb).trans_lt hbc`; its real empty-family variant is `(Real.sSup_le hb hb0).trans_lt hbc`. These existing-call terms require a **uniform bound b<c** as input. They do not derive the arithmetic b from δ,r,q and bounded integer coefficients. Thus they replace only the outer transport if such a bound has already been proved.
2. `Set.Finite.csSup_lt_iff`/`Finset.sup'_lt_iff` handle strict bounds over finite sets. The generic native Iio(1) counterexample shows strict pointwise inequalities alone cannot imply a strict supremum inequality for an arbitrary set; it **does not assert that this arithmetic indexSet is infinite**. Indeed bounded-degree indices take values among finitely many box weights, so a separate finite-image argument is plausible. Even that bridge would still require the substantive arithmetic pointwise bound. The actual proof uses an explicitly finite rank interval inside Lemma6.
3. Existing `weightedOrder_le` needs a specific nonzero coefficient, and `infDegree` reorganizes weighted support. Neither supplies the small weight forced by the rational denominator/height constraints. Pinned signatures and generic laws are executed in the isolated source; re-aiming the parentΘ or index definitions therefore does not independently replace Lemma7.
4. The complete original proof inlined into its caller compiles, but still calls project `theta_lt_succ_aux`, base, denominator and large-δ lemmas. Those encode determinant and height proofs absent from the identified generic laws. It is a proof, not≤3 pinned mathlib calls. A single local use does not make the substantial named mathematical endpoint dead code.

Conclusion: **NOT-COMPOSABLE as a whole endpoint by the tested≤3 existing-call routes.** No universal absence claim is based on a failed search; no closing simp composition of the whole arithmetic estimate was found.

## Phase7–8 — actionable verdict and complete handoff

**BORDERLINE-needs-human.** The exact result is classical, mathematically substantive, and central to the current theorem. Its production form is stronger than the primary source, and the independently compiled positive-weight extension is real. The unresolved issue is the appropriate upstream layer: a bounded-height/weighted-index arithmetic API versus a specialized numerical endpoint in a Roth development. It is neither an existing generic supremum lemma nor an automatic consequence of current polynomial root-counting or weighted-order lemmas. The verdict does not depend on the expense of developing the right generality.

Retain the named theorem locally. If later editing, adopt the verified≥1/positive-natural last-weight interface only together with its stronger finite-sum, Lemma6 numeric and recursive helper statements; the complete caller experiment gives the sole direct refactor: prove≥1 from its original≥3 input and apply the new endpoint through the explicitΘ bridge. Keep all other caller hypotheses and conclusions as demonstrated. Do not deleteΘ_lt merely becauseΘ itself re-aims to sSup. A suitable current destination is the existing project-local `Roth/Theta.lean`, with reusable algebraic/height ingredients considered separately. No YES PR, reviewer selection or inheritance/grouping is claimed.

Bounded future upstream questions (not user blockers):

1. Should a future mathlib contribution expose the full10^mδ^(2^-m) Roth endpoint, or keep it in a Diophantine/Roth downstream development while contributing its reusable height/determinant ingredients?
2. Should that arithmetic API use the verified positive-natural last-weight interface and an explicitly ordered finite enumeration, rather than the present≥3/Fin successor presentation?
3. Should reusable generalized-Wronskian separation, bounded integral coefficient families and weighted-index bridges be accepted as a coherent prerequisite API before presenting the specializedΘ endpoint?

All required phases are complete; verification unresolved is empty. [Verification manifest](../evidence/Roth.Θ_lt/verification.json), [phase evidence](../evidence/Roth.Θ_lt/phase-evidence.json), [assessment](../evidence/Roth.Θ_lt/assessment.json), and [portable validator](../evidence/Roth.Θ_lt/validate.py) make the handoff reviewable. The separate rejected caller drafts record (1) an unnormalized natural cast in linarith, and (2) missing explicit replayΘ normalization; the rejected shape draft records a name collision with an existing scratch Lemma6 helper. Only final clean warning/error-free executions with standard axioms are accepted. Preparation and complete exact sources are retained. Root independently reviews, integrates and publishes; this package does not alter production Lean, pins, Git, overview or progress.
